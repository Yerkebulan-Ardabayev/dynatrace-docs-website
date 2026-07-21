#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Post-translation Markdown Validator
Проверяет корректность переведённых документов:
- YAML frontmatter целостность
- Markdown-ссылки не сломаны
- Заголовки сохранены
- Код-блоки парные
- Технические термины не переведены
"""

import re
import sys
from pathlib import Path


class TranslationValidator:
    def __init__(self, ru_dir: str = "../docs/ru", en_dir: str = "../docs/en"):
        self.ru_dir = Path(ru_dir)
        self.en_dir = Path(en_dir)
        self.errors = []
        self.warnings = []
        self.stats = {'checked': 0, 'errors': 0, 'warnings': 0, 'passed': 0}

        # Термины, которые НЕ должны быть переведены
        self.protected_terms = [
            'OneAgent', 'ActiveGate', 'Smartscape', 'PurePath',
            'Davis AI', 'Grail', 'DQL', 'CMC',
        ]

    def validate_frontmatter(self, content: str, filepath: str) -> list:
        """Проверяет целостность YAML frontmatter"""
        issues = []

        # Должен начинаться с ---
        if content.startswith('---'):
            # Ищем закрывающий ---
            second_marker = content.find('---', 3)
            if second_marker == -1:
                issues.append(f"[FRONTMATTER] Незакрытый frontmatter в {filepath}")
            else:
                frontmatter = content[3:second_marker]
                # Проверяем обязательные поля
                if 'title:' not in frontmatter:
                    issues.append(f"[FRONTMATTER] Отсутствует поле 'title:' в {filepath}")
                if 'source:' not in frontmatter:
                    issues.append(f"[FRONTMATTER] Отсутствует поле 'source:' в {filepath}")

        return issues

    def validate_code_blocks(self, content: str, filepath: str) -> list:
        """Проверяет парность код-блоков (```)"""
        issues = []
        count = content.count('```')
        if count % 2 != 0:
            issues.append(f"[CODE_BLOCK] Непарные ``` ({count} шт.) в {filepath}")
        return issues

    def validate_links(self, content: str, filepath: str, en_content: str = '') -> list:
        """Проверяет корректность Markdown-ссылок"""
        issues = []

        # Находим все ссылки [text](url)
        links = re.findall(r'\[([^\]]*)\]\(([^\)]*)\)', content)
        for text, url in links:
            # Пустой текст ссылки
            if not text.strip():
                issues.append(f"[LINK] Пустой текст ссылки: []({url}) в {filepath}")
            # Пустой URL
            if not url.strip():
                issues.append(f"[LINK] Пустой URL: [{text}]() в {filepath}")

        # Незакрытые ссылки. Раньше проверка была построчной (`\[[^\]]*$`) и падала
        # на КАЖДОЙ ссылке, текст которой перенесён на новую строку. Так написаны
        # 941 из 2912 английских исходников и 917 файлов уже отгруженного русского
        # корпуса, и на сайте они рендерятся нормально, то есть проверка браковала
        # здоровые файлы. Всплыло это только сейчас: гейт смотрит лишь свежие
        # переводы, а перевод не запускался с момента его появления.
        #
        # Теперь считаем баланс скобок по всему документу (перенос строки внутри
        # ссылки законен) и сверяем с оригиналом: виноват перевод только если он
        # разошёлся с английским исходником.
        ru_balance = self._bracket_balance(content)
        en_balance = self._bracket_balance(en_content) if en_content else 0
        if ru_balance != en_balance:
            issues.append(
                f"[LINK] Баланс скобок разошёлся с оригиналом "
                f"(RU {ru_balance:+d}, EN {en_balance:+d}) в {filepath}"
            )

        return issues

    @staticmethod
    def _bracket_balance(content: str) -> int:
        """Разница числа [ и ] вне кода: 0 = все ссылки закрыты."""
        body = re.sub(r'```.*?```', '', content, flags=re.DOTALL)
        body = re.sub(r'`[^`\n]*`', '', body)
        return body.count('[') - body.count(']')

    def validate_headings(self, content: str, en_content: str, filepath: str) -> list:
        """Проверяет, что количество заголовков совпадает с оригиналом (порог 15%)"""
        issues = []

        ru_headings = len(re.findall(r'^#{1,6}\s', content, re.MULTILINE))
        en_headings = len(re.findall(r'^#{1,6}\s', en_content, re.MULTILINE))

        if ru_headings == 0 and en_headings > 0:
            issues.append(f"[HEADINGS] Все заголовки потеряны (EN: {en_headings}, RU: 0) в {filepath}")
        elif en_headings > 0 and abs(ru_headings - en_headings) > en_headings * 0.15:
            issues.append(
                f"[HEADINGS] Расхождение заголовков >15% (EN: {en_headings}, RU: {ru_headings}) в {filepath}"
            )

        return issues

    def validate_protected_terms(self, content: str, filepath: str) -> list:
        """Предупреждает о возможно переведённых технических терминах"""
        issues = []

        # Известные ошибочные переводы
        bad_translations = {
            'Один Агент': 'OneAgent',
            'Один агент': 'OneAgent',
            'Активный шлюз': 'ActiveGate',
            'Активный Шлюз': 'ActiveGate',
            'Чистый путь': 'PurePath',
            'Чистый Путь': 'PurePath',
            'Умная карта': 'Smartscape',
            'Консоль управления кластером': 'Cluster Management Console',
            'Центр управления': 'Mission Control',
            'Единица хоста': 'Host Unit',
            'Группа хостов': 'Host Group',
        }

        for bad, correct in bad_translations.items():
            if bad in content:
                issues.append(
                    f"[TERM] Неправильный перевод '{bad}' -> должно быть '{correct}' в {filepath}"
                )

        return issues

    def validate_file(self, ru_file: Path) -> bool:
        """Валидация одного переведённого файла"""
        self.stats['checked'] += 1

        try:
            ru_content = ru_file.read_text(encoding='utf-8')
        except Exception as e:
            self.errors.append(f"[READ] Не удалось прочитать {ru_file}: {e}")
            self.stats['errors'] += 1
            return False

        filepath = str(ru_file)
        file_issues = []

        # Основные проверки
        file_issues.extend(self.validate_frontmatter(ru_content, filepath))
        file_issues.extend(self.validate_code_blocks(ru_content, filepath))
        # en_content нужен, чтобы не винить перевод в кривизне оригинала
        en_file = self.en_dir / ru_file.relative_to(self.ru_dir)
        en_for_links = en_file.read_text(encoding='utf-8', errors='replace') if en_file.exists() else ''
        file_issues.extend(self.validate_links(ru_content, filepath, en_for_links))

        # Проверка терминов
        term_issues = self.validate_protected_terms(ru_content, filepath)
        self.warnings.extend(term_issues)

        # Сравнение с оригиналом (если есть)
        relative = ru_file.relative_to(self.ru_dir)
        en_file = self.en_dir / relative
        if en_file.exists():
            try:
                en_content = en_file.read_text(encoding='utf-8')
                file_issues.extend(self.validate_headings(ru_content, en_content, filepath))
            except Exception:
                pass

        # Пустой файл (порог 50 символов — голый frontmatter без контента)
        if len(ru_content.strip()) < 50:
            file_issues.append(f"[EMPTY] Файл почти пустой (<50 символов): {filepath}")

        # Проверка соотношения длин (если есть оригинал)
        if en_file.exists():
            try:
                en_len = len(en_content.strip()) if 'en_content' in dir() else len(en_file.read_text(encoding='utf-8').strip())
                ru_len = len(ru_content.strip())
                if en_len > 100 and ru_len > 0:
                    ratio = ru_len / en_len
                    if ratio < 0.4:
                        file_issues.append(
                            f"[LENGTH] Перевод подозрительно короткий ({ratio:.0%} от оригинала): {filepath}"
                        )
                    elif ratio > 2.0:
                        file_issues.append(
                            f"[LENGTH] Перевод подозрительно длинный ({ratio:.0%} от оригинала): {filepath}"
                        )
            except Exception:
                pass

        if file_issues:
            self.errors.extend(file_issues)
            self.stats['errors'] += len(file_issues)
            return False

        self.stats['passed'] += 1
        return True

    def run(self, only_rel_paths=None):
        """Запуск валидации.

        only_rel_paths: если задан список относительных путей (под ru_dir) — проверяем
        ТОЛЬКО их. В CI это набор реально переведённых в этом прогоне файлов (из
        translation_result.json). Так гейт не падает на 2698 готовых файлах корпуса,
        а проверяет именно свежие записи между переводом и коммитом.
        """
        print("=" * 70)
        print("🔍 ВАЛИДАЦИЯ ПЕРЕВЕДЁННЫХ ДОКУМЕНТОВ")
        print("=" * 70)
        print()

        if not self.ru_dir.exists():
            print(f"❌ Директория не найдена: {self.ru_dir}")
            return False

        if only_rel_paths is not None:
            ru_files = [self.ru_dir / rel for rel in only_rel_paths]
            missing = [p for p in ru_files if not p.exists()]
            ru_files = [p for p in ru_files if p.exists()]
            for p in missing:
                print(f"⚠️  Пропущен (нет файла): {p}")
            if not ru_files:
                # Переводить было нечего / ничего не записалось — это не провал гейта.
                print("📚 Нет переведённых файлов для проверки — OK (нечего валидировать)")
                return True
            print(f"📚 Проверяем только изменённые файлы: {len(ru_files)}")
        else:
            ru_files = list(self.ru_dir.rglob('*.md'))
            if not ru_files:
                print(f"❌ Нет файлов для проверки в {self.ru_dir}")
                return False
            print(f"📚 Найдено файлов: {len(ru_files)}")
        print()

        for ru_file in ru_files:
            self.validate_file(ru_file)

        # Отчёт
        print()
        print("=" * 70)
        print("📊 РЕЗУЛЬТАТЫ ВАЛИДАЦИИ")
        print("=" * 70)
        print(f"✅ Проверено: {self.stats['checked']}")
        print(f"✅ Без ошибок: {self.stats['passed']}")
        print(f"❌ Ошибок: {len(self.errors)}")
        print(f"⚠️  Предупреждений: {len(self.warnings)}")

        if self.errors:
            print()
            print("❌ ОШИБКИ:")
            for error in self.errors[:50]:  # Лимит вывода
                print(f"   {error}")
            if len(self.errors) > 50:
                print(f"   ... и ещё {len(self.errors) - 50} ошибок")

        if self.warnings:
            print()
            print("⚠️  ПРЕДУПРЕЖДЕНИЯ (возможно некорректный перевод терминов):")
            for warning in self.warnings[:30]:
                print(f"   {warning}")
            if len(self.warnings) > 30:
                print(f"   ... и ещё {len(self.warnings) - 30} предупреждений")

        print()
        has_errors = len(self.errors) > 0
        if has_errors:
            print("❌ ВАЛИДАЦИЯ НЕ ПРОЙДЕНА")
        else:
            print("✅ ВАЛИДАЦИЯ ПРОЙДЕНА УСПЕШНО")

        return not has_errors


if __name__ == '__main__':
    import argparse
    import json

    parser = argparse.ArgumentParser(description='Validate translated Markdown documents')
    parser.add_argument('--ru-dir', default='../docs/managed-ru',
                        help='Russian Managed docs directory')
    parser.add_argument('--en-dir', default='../docs/managed',
                        help='English Managed docs directory')
    parser.add_argument('--report',
                        help='translation_result.json — проверять только его translated_files '
                             '(гейт CI по свежим файлам, а не по всему корпусу)')
    parser.add_argument('--files', nargs='*',
                        help='Явный список относительных путей под --ru-dir для проверки')

    args = parser.parse_args()

    only = None
    if args.files:
        only = list(args.files)
    elif args.report:
        rp = Path(args.report)
        if rp.exists():
            data = json.load(open(rp, 'r', encoding='utf-8'))
            only = list(data.get('translated_files', []))
        else:
            print(f"⚠️  Отчёт {rp} не найден — проверять нечего, гейт пропущен (OK)")
            sys.exit(0)

    validator = TranslationValidator(args.ru_dir, args.en_dir)
    success = validator.run(only_rel_paths=only)
    sys.exit(0 if success else 1)
