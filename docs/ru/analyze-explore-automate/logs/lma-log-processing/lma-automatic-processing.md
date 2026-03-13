---
title: Automatic log processing at ingestion
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-processing/lma-automatic-processing
scraped: 2026-03-05T21:33:12.923279
---

# Автоматическая обработка логов при приёме

# Автоматическая обработка логов при приёме

* Последняя версия Dynatrace
* Пояснение
* Чтение: 2 минуты
* Опубликовано 08 декабря 2025 г.

Автоматически принимайте и обрабатывайте логи с помощью [OneAgent](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Принимайте данные логов в Dynatrace с помощью OneAgent и преобразуйте их в понятные сообщения журнала."), [приёма JSON и TXT логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Узнайте, как обрабатываются JSON и TXT логи — в плоском или необработанном режиме.") или [конечных точек Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") для удобного управления логами.

Dynatrace применяет единый подход к обработке при приёме.
Этот подход обеспечивает совместимость при переключении механизмов интеграции — например, при переходе с интеграции через шиппер логов на OneAgent — без необходимости дополнительной или, в ряде случаев, минимальной конфигурации.

Логи автоматически подготавливаются к обработке: система предварительно настроена для работы с ключевыми атрибутами, такими как `severity` и `timestamp`.
Кроме того, разбор полезной нагрузки логов и поддерживаемые форматы файлов — JSON, OTLP и TXT — уже учтены и не требуют ручного вмешательства.

### Обзор интеграций для приёма и обработки логов

В зависимости от интеграции для работы с логами автоматическая обработка адаптируется под разные форматы.

#### OneAgent (рекомендуемая интеграция)

OneAgent — предпочтительный метод приёма логов.
Он обеспечивает наибольшую ценность с точки зрения наблюдаемости и исключает необходимость ручной настройки разбора.
Дополнительная конфигурация не требуется.
При наличии особых потребностей у вас есть возможность настроить процесс под себя.

Вы можете воспользоваться следующими готовыми возможностями:

* Поддержка формата данных [JSON логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-one-agent-log-data-format#json-logs "В этом разделе перечислены все форматы логов, поддерживаемые системой управления логами и аналитики").
* Автоматическое извлечение атрибута `severity` с помощью [автоматического обогащения логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa "Общий приём логов автоматически преобразует данные в выходные значения атрибута loglevel.") для уже обогащённых данных.
* Автоматическое извлечение [топологического контекста](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa#autoattributes "Общий приём логов автоматически преобразует данные в выходные значения атрибута loglevel.") для привязки логов к соответствующим объектам.
* Извлечение временных меток поддерживается для перечисленных [поддерживаемых форматов временных меток](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-supported-timestamp-format "Поддерживаемые временные метки для последней версии системы управления логами и аналитики.") без дополнительной настройки.

Для оптимальной автоматической обработки логов вы можете воспользоваться следующими возможностями:

* **Шаблоны временных меток/разбиения** для [настройки временных меток/разбиения](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-timestamp-configuration "Задайте конкретный формат даты с помощью правил временных меток, определяющих, что должно считаться временной меткой в записи лога.").
* [Связывайте](/docs/analyze-explore-automate/logs/lma-log-enrichment "Связывайте входящие данные логов с трассировками для более точного анализа в Dynatrace.") данные логов с трассировками для ускорения устранения проблем и лёгкого переключения контекста.

#### Log Monitoring API — конечная точка JSON и TXT

Log Monitoring API автоматически обрабатывает принятые логи путём:

* Проверки поддерживаемых ключей **Severity** и **Timestamp** в [объекте `LogMessageJson`](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs#data-transformation-and-automatic-json-parsing "Узнайте, как обрабатываются JSON и TXT логи — в плоском или необработанном режиме.").
* JSON логи обрабатываются на конечных точках Log Monitoring API для сохранения исходной структуры лога.
  Дополнительную информацию о моделях данных см. в разделе [Приём JSON и TXT логов](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-api/lma-ingest-json-txt-logs "Узнайте, как обрабатываются JSON и TXT логи — в плоском или необработанном режиме.").

#### Dynatrace OTLP API

[Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.") автоматически обрабатывает принятые логи путём:

* Проверки поддерживаемых ключей [`severity` и `timestamp`](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#semantic-attributes "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").
* Структурированные логи обрабатываются на конечных точках Dynatrace OTLP API для сохранения исходной структуры лога.
  Дополнительную информацию о моделях данных см. в разделе [Приём OTLP логов](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#otlp-structured-logs "Узнайте, как Dynatrace принимает записи логов OpenTelemetry и какие ограничения применяются.").

## Связанные темы

* [Обработка логов с помощью OpenPipeline](/docs/analyze-explore-automate/logs/lma-log-processing/lma-openpipeline "Обрабатывайте логи с помощью Dynatrace OpenPipeline.")
