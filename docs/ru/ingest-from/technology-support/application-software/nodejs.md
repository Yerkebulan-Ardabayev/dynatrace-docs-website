---
title: Node.js
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nodejs
scraped: 2026-03-05T21:25:49.885344
---

# Node.js


* Актуальная версия Dynatrace
* Справочник
* Чтение: 4 мин
* Обновлено 21 ноября 2025

[Node.js](https://nodejs.org) — это серверный фреймворк на основе [движка JavaScript V8](https://developers.google.com/v8/) от Google. Node.js использует асинхронную модель выполнения и часто применяется в качестве связующего компонента или прокси-уровня в корпоративных средах.

## Возможности

Dynatrace предоставляет широкие возможности мониторинга Node.js:

* Метрики кучи и процессов
* Дампы кучи
* Профилирование CPU
* Метрики цикла событий
* Информация о входящих и исходящих HTTP-вызовах
* Специализированная поддержка различных баз данных (включая захват запросов)
* [Поддержка OpenTelemetry](https://github.com/open-telemetry/opentelemetry-js-api/) для захвата трассировок и приёма метрик.
  Для получения дополнительной информации см. [Инструментирование JavaScript-приложения на Node.js с помощью OpenTelemetry](../../opentelemetry/walkthroughs/nodejs.md "Learn how to instrument your JavaScript application on Node.js using OpenTelemetry and Dynatrace.")
* [OneAgent SDK](../../extend-dynatrace/extend-tracing/oneagent-sdk.md "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") для пользовательской трассировки
* [Непрерывный анализ потоков для worker-потоков](#worker-threads)

См. [нашу матрицу поддерживаемых технологий](../../technology-support.md#nodejs "Find technical details related to Dynatrace support for specific platforms and development frameworks.") для получения подробной информации о поддерживаемых технологиях, которые используются совместно с Node.js.

## Поддержка и прекращение поддержки

Node.js следует [модели релизов LTS](https://github.com/nodejs/Release).

Каждая нечётная версия достигает конца жизненного цикла вскоре после выпуска новой чётной версии. Каждая чётная версия со временем становится LTS-релизом. Для корпоративных производственных сред мы рекомендуем использовать LTS-релизы.

Каждый раз, когда выходит новая мажорная версия Node.js (чётная или нечётная), мы добавляем её поддержку.

Dynatrace следует этой модели поддержки, но поддерживает каждую версию Node.js как минимум на полгода дольше, чтобы дать нашим клиентам время для обновления.

| Версия Node.js | Дата выпуска вендором | Конец жизненного цикла вендора | Первая поддерживаемая версия Dynatrace OneAgent | Последняя поддерживаемая версия Dynatrace OneAgent | Поддержка Dynatrace до | [Уровень поддержки Dynatrace](../../technology-support.md#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 25 | 2025-10-15 | 2026-06-01 | 1.333 | - | 2026-12-01 | Поддерживается |
| 24 | 2025-05-06 | 2028-04-30 | 1.329 | - | 2029-04-30 | Поддерживается |
| 23 | 2024-10-16 | 2025-06-01 | 1.305 | 1.329 | 2025-12-01 | Не поддерживается |
| 22 | 2024-04-23 | 2027-04-30 | 1.295 | - | 2028-04-30 | Поддерживается |
| 21 | 2023-10-17 | 2024-06-01 | 1.281 | 1.303 | 2024-12-01 | Не поддерживается |
| 20 | 2023-04-18 | 2026-04-30 | 1.271 | - | 2027-04-30 | Поддерживается |
| 19 | 2022-10-18 | 2023-06-01 | 1.257 | 1.285 | 2023-12-01 | Не поддерживается |
| 18 | 2022-04-19 | 2025-04-30 | 1.243 | - | 2026-04-30 | Поддерживается |
| 17 | 2021-10-19 | 2022-06-01 | 1.235 | 1.265 | 2022-12-01 | Не поддерживается |
| 16 | 2021-04-20 | 2023-09-11 | 1.219 | - | 2024-09-11 | Ограниченная[1](#fn-node-js-1-def) |
| 15 | 2020-10-20 | 2021-06-01 | 1.207 | 1.233 | 2021-12-01 | Не поддерживается |
| 14 | 2020-04-21 | 2023-04-30 | 1.195 | - | 2024-04-30 | Ограниченная[1](#fn-node-js-1-def) |
| 13 | 2019-10-22 | 2020-06-01 | 1.183 | 1.205 | 2020-12-01 | Не поддерживается |
| 12 | 2019-04-23 | 2022-04-30 | 1.171 | - | 2023-04-30 | Ограниченная[1](#fn-node-js-1-def) |
| 11 | 2018-10-23 | 2019-06-30 | 1.159 | 1.181 | 2019-12-31 | Не поддерживается |
| 10 | 2015-04-24 | 2021-04-30 | 1.147 | 1.329 | 2022-04-30 | Не поддерживается[2](#fn-node-js-2-def) |
| 9 | 2017-10-01 | 2018-06-30 | - | 1.157 | 2018-12-31 | Не поддерживается |
| 8 | 2017-05-30 | 2019-12-31 | - | 1.239 | 2020-12-31 | Не поддерживается |

1

Ограниченная поддержка: Dynatrace может решать только те проблемы, которые воспроизводятся на поддерживаемых версиях.

2

Не поддерживается: Инструментирование по умолчанию отключено (deprecated) в OneAgent версий >=1.321 и <=1.329. Определите переменную окружения DT\_SUPPORT\_DEPRECATED\_NODE\_VERSIONS для включения на этих версиях OA.

## Непрерывный анализ потоков для worker-потоков

Node.js версии 12+ OneAgent версии 1.251+ Dynatrace версии 1.256+

[Непрерывный анализ потоков](../../../observe/application-observability/profiling-and-optimization/continuous-thread-analysis.md "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") для [worker-потоков](https://nodejs.org/api/worker_threads.html#worker-thread) может автоматически определять потоки с интенсивным использованием CPU и выявлять проблемы масштабируемости при распределении работы между множеством потоков, чтобы вы могли устранить узкие места производительности до того, как они повлияют на конечных пользователей.

Непрерывный анализ потоков в действии

Статистика по `main`- и `worker`-потокам:

![Node.js worker thread stats](https://dt-cdn.net/images/worker-thread-stats-1815-5a10cfd6f5.png)

Время CPU, потребляемое различными `worker`-потоками:

![Node.js worker thread CPU times](https://dt-cdn.net/images/worker-thread-cpu-times-1815-7223ec5892.png)

Чтобы начать работу с непрерывным анализом потоков для worker-потоков, активируйте [функции OneAgent](../../dynatrace-oneagent/oneagent-features.md "Manage OneAgent features globally and per process group.") **Node.js worker threads monitoring** и **Node.js code module preloading**.

Ограничения

Метрики, специфичные для Node.js (например, память, сборка мусора и цикл событий), передаются только для `main`-потока.

Обзор классов (необходимый для пользовательских сервисов обмена сообщениями kafkajs) ограничен `main`-потоком.

Автоматическая трассировка транзакций между `main`- и `worker`-потоками не осуществляется. Для трассировки транзакций между потоками вы можете использовать [трассировку OpenTelemetry](../../dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel.md "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.") или [OneAgent SDK](../../extend-dynatrace/extend-tracing/oneagent-sdk.md "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.").

## Известные ограничения

* Из-за ограничений платформы JavaScript и Node.js видимость на уровне кода ограничена по сравнению с .NET или Java.
* При использовании неподдерживаемых сторонних модулей контекст может теряться в асинхронных обратных вызовах. В таких случаях обратитесь к эксперту Dynatrace через онлайн-чат в вашей среде Dynatrace.
* OneAgent версии 1.279+ не передаёт время CPU для сервисов Node.js. Эти числа вводили в заблуждение, так как по замыслу значительная часть любой операции обрабатывается асинхронно внутри среды выполнения Node.js без возможности корреляции фактического времени CPU с конкретным сервисом.
* Web Streams, WebSocket Client не поддерживаются.
* Функции Node.js, отмеченные как «experimental», не поддерживаются.
* Использование NPM-модуля [esm](https://github.com/standard-things/esm) в [варианте 1 для пакетов](https://github.com/standard-things/esm/tree/3.2.25#getting-started) может привести к снижению видимости (особенно при использовании для основного скрипта приложения). Предпочтительно использовать вариант 2 для предзагрузки `esm` через параметр командной строки `-r`.
* В настоящее время существует только ограниченная поддержка [ECMAScript-модулей](https://nodejs.org/api/esm.html) (также известных как «ES6-модули»):

  + Если сам основной файл скрипта является ECMAScript-модулем, для внедрения OneAgent в процесс Node.js необходима версия OneAgent 1.219+ с включённой [предзагрузкой агента](../../../../common/whats-new/preview-releases.md#oneagent-1-219-nodejs-agent-preloading "Learn about our Preview releases and how you can participate in them.").
  + Инструментирование ECMAScript-модулей в настоящее время недоступно. Это ограничивает поддержку `kafkajs` в случае, когда определённая пользователем точка входа для сенсора KafkaJs находится внутри ECMAScript-модуля.
* **Webpack** по умолчанию объединяет все модули в один файл. OneAgent не может инструментировать объединённые модули. Чтобы обойти это ограничение, все модули, которые должны быть инструментированы OneAgent (такие как `express`, `mongodb` и `pg`), необходимо вынести во внешние зависимости (externals) в конфигурации webpack. Подробности см. в документации [webpack externals](https://webpack.js.org/configuration/externals/).
* Использование **Webpack** или других сборщиков также может повлиять на автоматическое обнаружение уязвимостей. Это связано с тем, что программные компоненты не могут быть обнаружены, поскольку они скрыты за конфигурацией сборщика и недоступны во время выполнения. Только пакеты, развёрнутые как внешние, могут быть обнаружены и зарегистрированы.

## Обработка логов с помощью парсеров технологических пакетов

Через OpenPipeline вы можете использовать и настраивать технологические пакеты. Технологический пакет — это библиотека парсеров (правил обработки), которые обрабатывают логи от различных технологий, таких как Java, .NET и Microsoft IIS.

Парсеры помогают улучшить фильтрацию, поиск неисправностей, метрики, оповещения и дашборды за счёт эффективного извлечения уровней логирования и соответствующих атрибутов. Вы также можете использовать технологические пакеты для структурирования логов от технологий, которые не поддерживаются Dynatrace «из коробки».

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

Для получения дополнительной информации см. [Обработка логов с помощью парсеров технологических пакетов](../../../platform/openpipeline/use-cases/tutorial-technology-processor.md "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Мониторинг

* [Как мониторить приложения Cloud Foundry?](../../setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring.md "Install OneAgent on Cloud Foundry.")

### См. также

* [Блог: Understanding Garbage Collection and hunting Memory Leaks in Node.js](https://www.dynatrace.com/news/blog/understanding-garbage-collection-and-hunting-memory-leaks-in-node-js/)
* [Блог: How to track down CPU issues in Node.js](https://www.dynatrace.com/news/blog/how-to-track-down-cpu-issues-in-node-js/)
* [Блог: All you need to know to really understand the Node.js Event Loop and its Metrics](https://www.dynatrace.com/news/blog/all-you-need-to-know-to-really-understand-the-node-js-event-loop-and-its-metrics/)
