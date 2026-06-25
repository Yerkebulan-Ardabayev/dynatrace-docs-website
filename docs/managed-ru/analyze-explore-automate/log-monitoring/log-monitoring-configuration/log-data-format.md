---
title: Форматы данных журналов (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-data-format
scraped: 2026-05-12T11:13:19.851975
---

# Форматы данных журналов (Logs Classic)

# Форматы данных журналов (Logs Classic)

* Чтение: 2 мин
* Обновлено 27 октября 2025 г.

Log Monitoring Classic

Log Monitoring может считывать и анализировать следующие форматы:

## Журналы событий Windows

Системные, журналы безопасности и приложений обнаруживаются автоматически на хостах. Другие журналы пользовательского формата событий можно добавить [вручную на уровне окружения](/managed/upgrade/unavailable-in-managed "Данная функция недоступна в Dynatrace Managed."). Временная метка берётся из атрибута события `Event.System.TimeCreated.<xmlattr>.SystemTime`.

## Текстовые журналы (plain-text)

Любой текстовый файл журнала допустим, если он закодирован в UTF-8 или UTF-16. Временная метка обнаруживается автоматически при её наличии согласно правилам, описанным в разделе [Поддерживаемые форматы временных меток (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Поддерживаемые временные метки для последней версии Dynatrace Log Monitoring."). Также можно [настроить временную метку](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration "Определите правила мониторинга журналов, управляющие временными метками данных журналов."). Если временная метка отсутствует, формат журнала по-прежнему является допустимым. В этом случае каждая строка, не начинающаяся с пробела, считается началом новой записи журнала и автоматически получает временную метку — время чтения записи журнала OneAgent.

Специальная поддержка JSON не предусмотрена — такие файлы обрабатываются как текст.

Подробнее см. раздел [Поддерживаемые форматы временных меток](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Поддерживаемые временные метки для последней версии Dynatrace Log Monitoring.").

## Журналы JSON

OneAgent версии 1.327+ поддерживает журналы в формате JSON.

Журналы могут быть представлены в виде объектов или массивов JSON. Символы новой строки можно использовать для создания многострочных JSON-объектов.

Заголовки и не-JSON-префиксы допустимы и анализируются как обычный текст.

OneAgent принимает заголовок в начале файла, который анализируется как обычный текст.

### Обогащение журналов JSON

OneAgent извлекает атрибуты `timestamp` и `loglevel` из соответствующих полей внутри JSON-объекта. Это аналогично поведению Log ingestion API. Список поддерживаемых ключей см. в разделе [Log Monitoring API — POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#openapi-parameter-body-objects-openapienv2 "Отправляйте пользовательские журналы в Dynatrace через Log Monitoring API v2.").

Дополнительно извлекаются атрибуты из не-JSON-префикса, если он присутствует. В этом случае значения из префикса имеют приоритет.

Если в одном JSON-объекте присутствует несколько полей `timestamp` или `loglevel`, используется только первый ключ в алфавитном порядке.

OneAgent автоматически извлекает все строковые поля, имена которых начинаются с `dt.` (например, `dt.trace_id` или `dt.span_id`), если они расположены на корневом или первом вложенном уровне JSON-объекта, и добавляет их как атрибуты.

[Поддерживаемые шаблоны временных меток](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-data-format "Поддерживаемые временные метки для последней версии Dynatrace Log Monitoring.") для журналов JSON — из полей или префиксов — аналогичны шаблонам для текстовых журналов.

Подробнее об уровнях журналов см. в разделе [Автоматическое обогащение журналов (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/lm-log-data-transformation "Общий приём журналов автоматически преобразует данные журналов в выходные значения атрибута loglevel.").

### Конфигурация

Автоматический разбор JSON включён по умолчанию. Если OneAgent не распознаёт содержимое в формате JSON, файл журнала обрабатывается как текстовый.

Можно явно отключить разбор JSON, создав правило конфигурации временных меток с отключённой опцией разбора JSON. О настройке правила временных меток см. раздел [Конфигурация временных меток/разбиения](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/timestamp-configuration#create-rule "Определите правила мониторинга журналов, управляющие временными метками данных журналов.").

Чтобы отключить разбор JSON для файла журнала:

1. Перейдите в **Settings** > **Log Monitoring** > **Timestamp/Splitting patterns**.
2. В записи настроенного правила временной метки нажмите **Edit**.
3. Отключите опцию **JSON format detector**.
4. Нажмите **Save and close**.