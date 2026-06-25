# -*- coding: utf-8 -*-
"""L4-IF.72 — wmi-tutorial-01.md  (extension package)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial"

TRANS = {
    # frontmatter title
    "title: WMI tutorial - extension package": "title: WMI tutorial - extension package",
    # H1 (duplicated in source)
    "# WMI tutorial - extension package": "# WMI tutorial - пакет расширения",
    # meta lines
    "* How-to guide": "* Практическое руководство",
    "* 1-min read": "* Чтение: 1 мин",
    "* Published Mar 30, 2022": "* Опубликовано 30 марта 2022 г.",
    # intro prose
    'Extensions extensions are based on a [YAML configuration file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework."). Its minimal contents are:': 'Расширения Extensions основаны на [файле конфигурации YAML](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework."). Его минимальный состав:',
    "* `name` - Must begin with `custom:` for custom extensions": "* `name`: должно начинаться с `custom:` для пользовательских расширений",
    "* `version`": "* `version`",
    "* `author`": "* `author`",
    "* `minDynatraceVersion` - Minimum Dynatrace version to enforce a minimum version of the extension schema": "* `minDynatraceVersion`: минимальная версия Dynatrace для применения минимальной версии схемы расширения",
    "In this step you will": "На этом шаге выполните следующее.",
    # card links (each split line)
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    '**Create YAML file**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#create-file "Learn about WMI extensions in the Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': '**Создание файла YAML**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#create-file "Узнайте о расширениях WMI в платформе Extensions framework.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    '**Build your extension package**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#build-package "Learn about WMI extensions in the Extensions framework.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': '**Сборка пакета расширения**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#build-package "Узнайте о расширениях WMI в платформе Extensions framework.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
    '**Upload your extension to Dynatrace Hub**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#upload-extension "Learn about WMI extensions in the Extensions framework.")': '**Загрузка расширения в Dynatrace Hub**](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-01#upload-extension "Узнайте о расширениях WMI в платформе Extensions framework.")',
    # Step 1
    "## Step 1 Create YAML file": "## Шаг 1. Создание файла YAML",
    "Use the following template.": "Используйте следующий шаблон.",
    "Save your `extension.yaml` and developer key and certificates using the following structure:": "Сохраните файл `extension.yaml`, ключ разработчика и сертификаты в следующей структуре:",
    # Step 2
    "## Step 2 Build and sign your extension package": "## Шаг 2. Сборка и подпись пакета расширения",
    "In the `extensions` parent directory, run the following command:": "В родительском каталоге `extensions` выполните следующую команду:",
    'These commands build your [extension package](/managed/ingest-from/extensions/concepts#package "Learn more about the concept of Dynatrace Extensions.") containing only the `extension.zip` archive and the `extension.zip.sig` signature file.': 'Эти команды собирают [пакет расширения](/managed/ingest-from/extensions/concepts#package "Подробнее о концепции Dynatrace Extensions."), содержащий только архив `extension.zip` и файл подписи `extension.zip.sig`.',
    # Step 3
    "## Step 3 Upload your extension to Dynatrace Hub": "## Шаг 3. Загрузка расширения в Dynatrace Hub",
    "To upload and activate your extension, run the following command:": "Чтобы загрузить и активировать расширение, выполните следующую команду:",
    "Example successful output:": "Пример успешного вывода:",
    'For more information, see [Manage WMI extensions](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi "Learn how to extend observability in Dynatrace with declarative WMI metrics ingestion.").': 'Дополнительные сведения см. в разделе [Управление расширениями WMI](/managed/ingest-from/extensions/supported-extensions/data-sources/wmi "Узнайте, как расширить возможности наблюдаемости в Dynatrace с помощью декларативного приёма метрик WMI.").',
    # Results
    "## Results": "## Результаты",
    "Your extension shows up in Dynatrace as Active.": "Расширение отображается в Dynatrace со статусом Active.",
    "![result](https://dt-cdn.net/images/wmi-tutorial-hub-1050-7d02da15fb.png)": "![result](https://dt-cdn.net/images/wmi-tutorial-hub-1050-7d02da15fb.png)",
    "result": "result",
    '**Next step**: [WMI data source](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-02 "Learn about WMI extensions in the Extensions framework.")': '**Следующий шаг**: [Источник данных WMI](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-02 "Узнайте о расширениях WMI в платформе Extensions framework.")',
}

PASS = {
    "title: WMI tutorial - extension package",
}

if __name__ == "__main__":
    build_one(REL, "wmi-tutorial-01.md", TRANS, PASS)
    qa_one(REL, "wmi-tutorial-01.md")
