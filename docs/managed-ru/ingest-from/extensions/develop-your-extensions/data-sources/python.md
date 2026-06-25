---
title: Dynatrace Extensions Python SDK
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/python
scraped: 2026-05-12T12:11:33.469943
---

# Dynatrace Extensions Python SDK

# Dynatrace Extensions Python SDK

* Справочник
* Чтение: 1 мин
* Обновлено 4 марта 2026 г.

Dynatrace Extensions Python SDK предоставляет платформу для приёма данных в Dynatrace из любой технологии, предоставляющей интерфейс.

Расширения с пользовательским кодом основаны на тех же принципах. Они декларативны, как и другие источники данных, но извлечённые данные обрабатываются предоставленными методами для создания метрик и событий.

Этот SDK предоставляет:

* Большую гибкость при приёме данных из собственных технологий или когда сценарий требует расширенной настройки, которую доступные источники данных не предлагают.
* Инструменты для экспорта текущих расширений OneAgent и ActiveGate в новую платформу.

Установите флаг файловой системы в `exec`, а не `noexec`, чтобы расширение Python работало корректно. Эта настройка критична, поскольку она разрешает выполнение двоичных файлов и скриптов в указанной файловой системе. Без неё расширение не сможет выполняться правильно, что приведёт к возможным ошибкам и сбоям.

Срок поддержки Python 3.10 истекает в октябре 2026 года. Для расширений, собранных с помощью Dynatrace Extensions Python SDK, команда сборки должна использовать `--python-version 3.14`.
Дополнительные сведения см. в [руководстве по команде сборки](https://github.com/dynatrace-extensions/dt-extensions-python-sdk/blob/main/docs/guides/building.rst).

Дополнительные сведения см. в следующих источниках:

* [Документация Dynatrace Extensions Python SDK](https://dt-url.net/7g638yh)
* [Репозиторий Dynatrace Extensions Python SDK](https://dt-url.net/jsa38pm) на GitHub Dynatrace Extensions.