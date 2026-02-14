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

    def validate_links(self, content: str, filepath: str) -> list:
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

        # Проверяем незакрытые ссылки: [ без ]( или ]( без )
        open_brackets = len(re.findall(r'\[[^\]]*$', content, re.MULTILINE))
        if open_brackets > 0:
            issues.append(f"[LINK] Найдено {open_brackets} незакрытых [ в {filepath}")

        return issues

    def validate_headings(self, content: str, en_content: str, filepath: str) -> list:
        """Проверяет, что количество заголовков совпадает с оригиналом"""
        issues = []

        ru_headings = len(re.findall(r'^#{1,6}\s', content, re.MULTILINE))
        en_headings = len(re.findall(r'^#{1,6}\s', en_content, re.MULTILINE))

        if ru_headings == 0 and en_headings > 0:
            issues.append(f"[HEADINGS] Все заголовки потеряны (EN: {en_headings}, RU: 0) в {filepath}")
        elif en_headings > 0 and abs(ru_headings - en_headings) > en_headings * 0.3:
            issues.append(
                f"[HEADINGS] Расхождение заголовков (EN: {en_headings}, RU: {ru_headings}) в {filepath}"
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
        file_issues.extend(self.validate_links(ru_content, filepath))

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

        # Пустой файл
        if len(ru_content.strip()) < 10:
            file_issues.append(f"[EMPTY] Файл почти пустой (<10 символов): {filepath}")

        if file_issues:
            self.errors.extend(file_issues)
            self.stats['errors'] += len(file_issues)
            return False

        self.stats['passed'] += 1
        return True

    def run(self):
        """Запуск полной валидации"""
        print("=" * 70)
        print("🔍 ВАЛИДАЦИЯ ПЕРЕВЕДЁННЫХ ДОКУМЕНТОВ")
        print("=" * 70)
        print()

        if not self.ru_dir.exists():
            print(f"❌ Директория не найдена: {self.ru_dir}")
            return False

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

    parser = argparse.ArgumentParser(description='Validate translated Markdown documents')
    parser.add_argument('--ru-dir', default='../docs/ru', help='Russian docs directory')
    parser.add_argument('--en-dir', default='../docs/en', help='English docs directory')

    args = parser.parse_args()

    validator = TranslationValidator(args.ru_dir, args.en_dir)
    success = validator.run()
    sys.exit(0 if success else 1)
