# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/.../data-sources/python.md (exemplar)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources"

TRANS = {
    # title + H1 kept EN (SDK product name) -> via PASS
    "* Reference": "* Справочник",
    "* 1-min read": "* Чтение: 1 мин",
    "* Updated on Mar 04, 2026": "* Обновлено 4 марта 2026 г.",
    "The Dynatrace Extensions Python SDK provides you with a framework to ingest data into Dynatrace from any technology exposing an interface.": "Dynatrace Extensions Python SDK предоставляет платформу для приёма данных в Dynatrace из любой технологии, предоставляющей интерфейс.",
    "Custom-coded extensions are based on the same principles. They're declarative, similar to other data sources, but you use the provided methods to use extracted data to create metrics and events.": "Расширения с пользовательским кодом основаны на тех же принципах. Они декларативны, как и другие источники данных, но извлечённые данные обрабатываются предоставленными методами для создания метрик и событий.",
    "This SDK offers:": "Этот SDK предоставляет:",
    "* Greater flexibility to ingest the data from your proprietary technologies or when your case requires extended customization that available data sources don't offer.": "* Большую гибкость при приёме данных из собственных технологий или когда сценарий требует расширенной настройки, которую доступные источники данных не предлагают.",
    "* Tooling to export your current OneAgent and ActiveGate extensions to the new framework.": "* Инструменты для экспорта текущих расширений OneAgent и ActiveGate в новую платформу.",
    "Set the filesystem flag to `exec` and not `noexec` to ensure a Python extension runs correctly. This configuration is crucial because it allows the execution of binaries and scripts within the specified filesystem. The extension can't execute properly without this setting, leading to potential errors and failures.": "Установите флаг файловой системы в `exec`, а не `noexec`, чтобы расширение Python работало корректно. Эта настройка критична, поскольку она разрешает выполнение двоичных файлов и скриптов в указанной файловой системе. Без неё расширение не сможет выполняться правильно, что приведёт к возможным ошибкам и сбоям.",
    "Python 3.10 reaches end of life in October 2026. For extensions built with the Dynatrace Extensions Python SDK, the build command must use `--python-version 3.14`.": "Срок поддержки Python 3.10 истекает в октябре 2026 года. Для расширений, собранных с помощью Dynatrace Extensions Python SDK, команда сборки должна использовать `--python-version 3.14`.",
    "For more information, see the [build command guide](https://github.com/dynatrace-extensions/dt-extensions-python-sdk/blob/main/docs/guides/building.rst).": "Дополнительные сведения см. в [руководстве по команде сборки](https://github.com/dynatrace-extensions/dt-extensions-python-sdk/blob/main/docs/guides/building.rst).",
    "For more information, see:": "Дополнительные сведения см. в следующих источниках:",
    "* [Dynatrace Extensions Python SDK documentation](https://dt-url.net/7g638yh)": "* [Документация Dynatrace Extensions Python SDK](https://dt-url.net/7g638yh)",
    "* [Dynatrace Extensions Python SDK repository](https://dt-url.net/jsa38pm) on Dynatrace Extensions GitHub.": "* [Репозиторий Dynatrace Extensions Python SDK](https://dt-url.net/jsa38pm) на GitHub Dynatrace Extensions.",
}

PASS = {
    "title: Dynatrace Extensions Python SDK",
    "# Dynatrace Extensions Python SDK",
}

if __name__ == "__main__":
    build_one(REL, "python.md", TRANS, PASS)
    qa_one(REL, "python.md")
