---
title: Dynatrace Extensions Python SDK
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/python
scraped: 2026-03-06T21:32:00.044917
---

* Latest Dynatrace
* 1-min read

Dynatrace Extensions Python SDK предоставляет фреймворк для загрузки данных в Dynatrace из любой технологии, предоставляющей соответствующий интерфейс.

Расширения с пользовательским кодом основаны на тех же принципах. Они являются декларативными — аналогично другим источникам данных, — но для работы с извлечёнными данными и создания метрик и событий используются предоставляемые методы.

Этот SDK предлагает:

* Большую гибкость при загрузке данных из проприетарных технологий или в случаях, требующих расширенной настройки, которую доступные источники данных не обеспечивают.
* Инструменты для экспорта текущих расширений OneAgent и ActiveGate в новый фреймворк.

Dynatrace Extensions Python SDK находится в открытом доступе начиная с [OneAgent 1.285](../../../../whats-new/oneagent/sprint-285.md#custom-coded-python-extensions "Release notes for Dynatrace OneAgent version 1.285").

Установите флаг файловой системы в значение `exec`, а не `noexec`, чтобы расширение Python выполнялось корректно. Эта конфигурация необходима, поскольку позволяет запускать двоичные файлы и скрипты в указанной файловой системе. Без этой настройки расширение не сможет работать должным образом, что приведёт к потенциальным ошибкам и сбоям.

Поддержка Python 3.10 завершается в октябре 2026 года. Для расширений, созданных с помощью Dynatrace Extensions Python SDK, команда сборки должна использовать `--python-version 3.14`.
Дополнительные сведения см. в [руководстве по команде сборки](https://github.com/dynatrace-extensions/dt-extensions-python-sdk/blob/main/docs/guides/building.rst).

Дополнительные сведения см. по ссылкам:

* [Документация Dynatrace Extensions Python SDK](https://dt-url.net/7g638yh)
* [Репозиторий Dynatrace Extensions Python SDK](https://dt-url.net/jsa38pm) на GitHub Dynatrace Extensions.
