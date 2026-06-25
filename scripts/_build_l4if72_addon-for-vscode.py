# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/develop-your-extensions/addon-for-vscode.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions"

TRANS = {
    "* Explanation": "* Пояснение",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Jun 16, 2025": "* Опубликовано 16 июня 2025 г.",
    "**Dynatrace Extensions** is an add-on for Visual Studio Code that supports all aspects of developing Extensions running on Dynatrace. Find it by searching the [VS Code extensions marketplace](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions).": "**Dynatrace Extensions** дополнение для Visual Studio Code, поддерживающее все аспекты разработки Extensions для Dynatrace. Найти его можно в [магазине расширений VS Code](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions).",
    "It gives you access to a specialized toolkit that's ready to use and helps you out with the following:": "Оно предоставляет доступ к специализированному набору инструментов, готовому к использованию, и помогает решать следующие задачи:",
    "1. Operational efficiency": "1. Операционная эффективность",
    "2. Content creation": "2. Создание контента",
    "3. Content validation": "3. Проверка контента",
    'Check out the instructions for [getting started](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes."), or keep reading to learn some of its features.': 'Ознакомьтесь с инструкциями по [началу работы](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Настройте редактор Visual Studio Code и соберите и загрузите первое расширение в Dynatrace за 5 минут.") или продолжайте читать, чтобы узнать о некоторых функциях.',
    "## Features": "## Функции",
    "Following are some features of **Dynatrace Extensions**.": "Ниже перечислены некоторые функции **Dynatrace Extensions**.",
    "### Operational efficiency": "### Операционная эффективность",
    "**Dynatrace Extensions** makes you more operationally efficient when developing Extensions. It includes the following features:": "**Dynatrace Extensions** повышает операционную эффективность при разработке Extensions. В него входят следующие функции:",
    "* Extension 2.0 project management and organization at scale.": "* Управление проектами Extension 2.0 и их организация в масштабе.",
    "* Overview of deployments across multiple environments.": "* Обзор развёртываний в нескольких окружениях.",
    "* All extension-related operations available within your editor:": "* Все операции, связанные с расширениями, доступны прямо в редакторе:",
    "+ Create, build, sign, upload, and activate extensions.": "+ Создание, сборка, подпись, загрузка и активация расширений.",
    "+ Create and manage monitoring configurations.": "+ Создание конфигураций мониторинга и управление ими.",
    "+ Create and manage credentials used in signing your extensions.": "+ Создание учётных данных для подписи расширений и управление ими.",
    "### Content creation": "### Создание контента",
    "You can also automatically generate significant portions of your extension's manifest and other content. Following are the features that you can use:": "Также возможно автоматически генерировать значительные части манифеста расширения и другого контента. Ниже перечислены доступные функции:",
    '* Generate [Unified analysis screens](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Extend the Dynatrace web UI using entity-tailored unified analysis pages.") for your entities.': '* Генерация [экранов единого анализа](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis "Расширение веб-интерфейса Dynatrace с помощью настроенных под сущности страниц единого анализа.") для ваших сущностей.',
    "* Generate documentation, dashboards, and alerts.": "* Генерация документации, дашбордов и оповещений.",
    "* Run Windows Management Instrumentation (WMI) Queries to extract metrics and dimensions automatically.": "* Выполнение запросов Windows Management Instrumentation (WMI) для автоматического извлечения метрик и измерений.",
    "* Connect to Prometheus exporters to extract metrics, dimensions, and metadata automatically.": "* Подключение к экспортёрам Prometheus для автоматического извлечения метрик, измерений и метаданных.",
    "* Use code completions where the values depend on data from your environment.": "* Использование автодополнения кода, когда значения зависят от данных вашего окружения.",
    "### Content validation": "### Проверка контента",
    "You can use the Dynatrace Extensions to validate your extension manifest early. Following are the features that you can use:": "С помощью Dynatrace Extensions можно проверять манифест расширения на раннем этапе. Ниже перечислены доступные функции:",
    "* Validate against targeted YAML schema versions.": "* Проверка соответствия целевым версиям схемы YAML.",
    "* Get custom diagnostics beyond what's included in the schema.": "* Получение пользовательской диагностики, выходящей за рамки схемы.",
    "* Validate your metric and entity selectors against environment data.": "* Проверка селекторов метрик и сущностей по данным окружения.",
    "## Support": "## Поддержка",
    "This open source project relies on community feedback and contribution and isn't officially supported by Dynatrace.": "Этот проект с открытым исходным кодом основан на обратной связи и вкладе сообщества и не поддерживается Dynatrace официально.",
    "For any issues, concerns, or contributions, leverage the [issues page](https://github.com/dynatrace-extensions/dynatrace-extensions-vscode/issues) of the GitHub repository hosting this project.": "По вопросам, предложениям или для внесения вклада используйте [страницу issues](https://github.com/dynatrace-extensions/dynatrace-extensions-vscode/issues) репозитория GitHub, где размещён этот проект.",
}

PASS = {
    "title: Add-on for VS Code",
    "# Add-on for VS Code",
}

if __name__ == "__main__":
    build_one(REL, "addon-for-vscode.md", TRANS, PASS)
    qa_one(REL, "addon-for-vscode.md")
