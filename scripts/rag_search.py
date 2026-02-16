#!/usr/bin/env python3
"""
Dynatrace Documentation RAG Search
Local search + Groq Llama for intelligent answers.

Usage:
    python scripts/rag_search.py                    # interactive mode
    python scripts/rag_search.py "your question"    # single question
    python scripts/rag_search.py --lang ru "вопрос" # answer in Russian
"""

import os
import sys
import io
import json
import time
import hashlib
import argparse
from pathlib import Path

import requests
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).parent.parent / ".env")
except ImportError:
    pass
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Fix Windows encoding (only in interactive terminal, not piped)
if sys.platform == 'win32' and sys.stdout.isatty():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

# ─── Config ───────────────────────────────────────────────
SCRIPT_DIR = Path(__file__).parent
DOCS_DIR = SCRIPT_DIR.parent / "docs"
EN_DIR = DOCS_DIR / "en"
RU_DIR = DOCS_DIR / "ru"
INDEX_CACHE = SCRIPT_DIR / ".rag_index_cache.json"

GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_API_KEY = os.environ.get("GROQ_API_KEY", "")
GROQ_MODEL = "llama-3.3-70b-versatile"

TOP_K = 5  # number of relevant docs to include in context


# ─── Document Loading ─────────────────────────────────────
def load_documents():
    """Load all markdown documents from en/ and ru/ directories."""
    docs = []

    for lang_dir, lang in [(EN_DIR, "en"), (RU_DIR, "ru")]:
        if not lang_dir.exists():
            continue
        for md_file in sorted(lang_dir.rglob("*.md")):
            try:
                content = md_file.read_text(encoding="utf-8", errors="ignore").strip()
                if len(content) < 50:  # skip empty/tiny files
                    continue
                rel_path = md_file.relative_to(DOCS_DIR)

                # Extract title from content
                title = ""
                for line in content.split("\n")[:10]:
                    line = line.strip()
                    if line.startswith("# "):
                        title = line[2:].strip()
                        break
                    if line.startswith("title:"):
                        title = line.split(":", 1)[1].strip()
                        break

                docs.append({
                    "path": str(rel_path),
                    "lang": lang,
                    "title": title or md_file.stem,
                    "content": content,
                })
            except Exception:
                continue

    return docs


# ─── Search Index ─────────────────────────────────────────
class SearchIndex:
    def __init__(self, docs):
        self.docs = docs
        self.vectorizer = TfidfVectorizer(
            max_features=50000,
            ngram_range=(1, 2),
            stop_words="english",
            sublinear_tf=True,
        )

        # Build index
        texts = [f"{d['title']} {d['content']}" for d in docs]
        self.tfidf_matrix = self.vectorizer.fit_transform(texts)

    def search(self, query, top_k=TOP_K, lang=None):
        """Search for relevant documents."""
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.tfidf_matrix).flatten()

        # Get top results
        top_indices = np.argsort(scores)[::-1]

        results = []
        for idx in top_indices:
            if len(results) >= top_k:
                break
            doc = self.docs[idx]
            score = scores[idx]
            if score < 0.01:  # skip irrelevant
                continue
            if lang and doc["lang"] != lang:
                continue
            results.append({
                "doc": doc,
                "score": float(score),
            })

        return results


# ─── Groq LLM ────────────────────────────────────────────
def ask_groq(question, context_docs, lang="ru", _retry=0):
    """Generate answer using Groq Llama with document context."""
    if not GROQ_API_KEY:
        return "GROQ_API_KEY не задан! Установи: set GROQ_API_KEY=gsk_..."

    # Build context from top documents
    context_parts = []
    for i, result in enumerate(context_docs, 1):
        doc = result["doc"]
        # Truncate content to fit in context window
        content = doc["content"][:3000]
        context_parts.append(
            f"[Документ {i}] ({doc['path']})\n"
            f"Заголовок: {doc['title']}\n"
            f"Релевантность: {result['score']:.2f}\n"
            f"Содержание:\n{content}\n"
        )

    context = "\n---\n".join(context_parts)

    lang_instruction = {
        "ru": "Отвечай на русском языке.",
        "en": "Answer in English.",
        "kk": "Қазақ тілінде жауап бер.",
    }.get(lang, "Отвечай на русском языке.")

    prompt = f"""Ты — эксперт по Dynatrace. Используй ТОЛЬКО предоставленный контекст для ответа.
{lang_instruction}

Правила:
- Отвечай точно и по существу на основе документации
- Указывай источник [Документ N] при цитировании
- Если в контексте нет ответа — честно скажи об этом
- Используй технические термины Dynatrace без перевода (OneAgent, ActiveGate, PurePath и т.д.)

Контекст из документации:
{context}

Вопрос: {question}

Ответ:"""

    try:
        response = requests.post(
            GROQ_API_URL,
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {GROQ_API_KEY}",
            },
            json={
                "model": GROQ_MODEL,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.2,
                "max_tokens": 4000,
            },
            timeout=30,
        )

        if response.status_code == 429:
            if _retry >= 2:
                return "⚠️ Groq rate limit исчерпан. Подожди пару минут и попробуй снова."
            wait = int(response.headers.get("retry-after", 5))
            print(f"  ⏳ Rate limit, жду {wait}с...")
            time.sleep(min(wait, 10))
            return ask_groq(question, context_docs, lang, _retry + 1)

        if response.status_code != 200:
            return f"Ошибка API: {response.status_code} — {response.text[:200]}"

        result = response.json()
        return result["choices"][0]["message"]["content"].strip()

    except Exception as e:
        return f"Ошибка: {e}"


# ─── CLI Interface ────────────────────────────────────────
def print_header():
    print()
    print("╔══════════════════════════════════════════════════════════╗")
    print("║   Dynatrace Documentation RAG Search                   ║")
    print("║   Powered by Groq Llama 3.3 70B + TF-IDF              ║")
    print("╚══════════════════════════════════════════════════════════╝")
    print()


def interactive_mode(index, lang):
    """Interactive question-answer loop."""
    print_header()
    print(f"  Документов в индексе: {len(index.docs)}")
    print(f"  Язык ответов: {lang}")
    print(f"  Введи вопрос или 'exit' для выхода")
    print()

    while True:
        try:
            question = input("❓ > ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\nВыход.")
            break

        if not question:
            continue
        if question.lower() in ("exit", "quit", "q", "выход"):
            print("Выход.")
            break

        # Search
        print("  🔍 Поиск по документации...")
        results = index.search(question, top_k=TOP_K)

        if not results:
            print("  ❌ Ничего не найдено.\n")
            continue

        # Show found documents
        print(f"  📄 Найдено {len(results)} релевантных документов:")
        for i, r in enumerate(results, 1):
            doc = r["doc"]
            score = r["score"]
            flag = "🇬🇧" if doc["lang"] == "en" else "🇷🇺"
            print(f"     {i}. {flag} {doc['title'][:60]}  ({score:.2f})")

        # Generate answer
        print("  🤖 Генерация ответа через Groq...")
        answer = ask_groq(question, results, lang)

        print()
        print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()
        # Print answer with indent
        for line in answer.split("\n"):
            print(f"  {line}")
        print()
        print("  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print()


def single_query(index, question, lang):
    """Answer a single question."""
    results = index.search(question, top_k=TOP_K)

    if not results:
        print("Ничего не найдено.")
        return

    print(f"\n📄 Источники ({len(results)}):")
    for i, r in enumerate(results, 1):
        doc = r["doc"]
        flag = "EN" if doc["lang"] == "en" else "RU"
        print(f"  {i}. [{flag}] {doc['title'][:70]}  (score: {r['score']:.2f})")

    print("\n🤖 Ответ:\n")
    answer = ask_groq(question, results, lang)
    print(answer)
    print()


# ─── Main ─────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Dynatrace Documentation RAG Search")
    parser.add_argument("question", nargs="?", help="Question to ask (or omit for interactive mode)")
    parser.add_argument("--lang", default="ru", choices=["ru", "en", "kk"], help="Answer language")
    args = parser.parse_args()

    # Check API key
    if not GROQ_API_KEY:
        print("⚠️  GROQ_API_KEY не задан!")
        print("   Установи: set GROQ_API_KEY=gsk_your_key")
        print("   Получить бесплатно: https://console.groq.com")
        print()
        print("   Продолжаю без LLM (только поиск)...\n")

    # Load documents
    print("📚 Загрузка документации...")
    docs = load_documents()
    print(f"   Загружено: {len(docs)} документов")

    en_count = sum(1 for d in docs if d["lang"] == "en")
    ru_count = sum(1 for d in docs if d["lang"] == "ru")
    print(f"   EN: {en_count} | RU: {ru_count}")

    # Build search index
    print("🔧 Построение поискового индекса...")
    index = SearchIndex(docs)
    print("   Индекс готов!")

    if args.question:
        single_query(index, args.question, args.lang)
    else:
        interactive_mode(index, args.lang)


if __name__ == "__main__":
    main()
