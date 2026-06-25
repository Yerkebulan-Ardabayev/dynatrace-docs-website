# -*- coding: utf-8 -*-
"""L4-AG.1a.12 builder: 10 builtin-*.md schema-table files.

Состав батча:
  - 6 anomaly-detection: metric-events, rum-mobile, rum-custom, services,
    databases, rum-web (7.7-9.0 KB)
  - 4 cleanup 2.3-2.4 KB: synthetic-http-performance-thresholds,
    logmonitoring-schemaless-log-metric, rum-web-resource-cleanup-rules,
    devobs-sensitive-data-masking.

Канон L4-AG.1a.11 (chr() для triple-mojibake, _normalize чистит mojibake-BOM
вне зависимости от позиции, empty-label rows разрешены в _param_row).

Mojibake-аудит EN:
  - BOMJ `i»?` встречается в 8/10 файлов внутри hyperlink-текстов
    ([automated anomaly detection][дшт] и т.п.), чистится `_normalize`.
  - double-B `Davis®` (c3 82 c2 ae) 2 = metric-events (line 79 DavisAI),
    logmonitoring-schemaless-log-metric (line 15 Davis data units).
  - Триплов нет.

Twin pairs:
  - rum-mobile ↔ rum-custom: идентичный SCHEMA_DESC + 11 nested object'ов;
    отличаются только DISPLAY_NAME и scope-таблицей.
  - services ↔ databases: общий блок responseTime/failureRate/loadDrops/
    loadSpikes; databases добавляет nested `databaseConnections`.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-anomaly-detection-metric-events.md",
    "builtin-anomaly-detection-rum-mobile.md",
    "builtin-anomaly-detection-rum-custom.md",
    "builtin-anomaly-detection-services.md",
    "builtin-anomaly-detection-databases.md",
    "builtin-anomaly-detection-rum-web.md",
    "builtin-synthetic-http-performance-thresholds.md",
    "builtin-logmonitoring-schemaless-log-metric.md",
    "builtin-rum-web-resource-cleanup-rules.md",
    "builtin-devobs-sensitive-data-masking.md",
]

# Double-B mojibake (Davis registered mark): c3 82 c2 ae = `Â®` (U+00C2 U+00AE).
DB_R = chr(0xC2) + chr(0xAE)

DISPLAY_NAME = {
    "Metric events": "Metric events",
    "Anomaly detection for mobile applications": "Обнаружение аномалий для mobile-приложений",
    "Anomaly detection for custom applications": "Обнаружение аномалий для custom-приложений",
    "Anomaly detection for services": "Обнаружение аномалий сервисов",
    "Anomaly detection for databases": "Обнаружение аномалий баз данных",
    "Anomaly detection for applications": "Обнаружение аномалий приложений",
    "Performance thresholds": "Пороги производительности",
    "Log metrics": "Log-метрики",
    "Resource URL cleanup rules": "Правила очистки URL ресурсов",
    "Sensitive Data Masking": "Маскирование чувствительных данных",
}

SCHEMA_DESC = {
    # metric-events
    "Metric event configurations are used to automatically detect anomalies in metric timeseries by using thresholds or baselines.": "Конфигурации metric event используются для автоматического обнаружения аномалий в metric timeseries по порогам или baseline.",
    # rum-mobile / rum-custom (общий параграф)
    "Dynatrace automatically detects application-related performance anomalies such as response time degradations and traffic spikes. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain applications.": "Dynatrace автоматически обнаруживает аномалии производительности на уровне приложений, такие как деградации времени отклика и всплески трафика. Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для отдельных приложений.",
    # rum-mobile / rum-custom / rum-web (общий параграф; BOMJ съедается _normalize)
    'To avoid false-positive problem notifications, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).': 'Чтобы избежать false-positive оповещений о проблемах, [automated anomaly detection](https://dt-url.net/op03t6j "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших не менее 20% недели (7 дней).',
    # services
    "Dynatrace automatically detects service related performance anomalies such as response time degradations and failure rate increases.": "Dynatrace автоматически обнаруживает аномалии производительности на уровне сервисов, такие как деградации времени отклика и рост failure rate.",
    # services / databases (общий параграф; BOMJ съедается)
    'Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain services. Read more about [Automated multi-dimensional baselining](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center").': 'Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для отдельных сервисов. Подробнее см. [Automated multi-dimensional baselining](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center").',
    # services (без BOMJ-line, простой текст)
    "To avoid false-positive problem notifications, automated anomaly detection is only available for applications and services that have run for at least 20% of a week (7 days).": "Чтобы избежать false-positive оповещений о проблемах, automated anomaly detection доступно только для приложений и сервисов, проработавших не менее 20% недели (7 дней).",
    # databases
    "Dynatrace automatically detects database-service related performance anomalies such as response time degradations and failure rate increases.": "Dynatrace автоматически обнаруживает аномалии производительности баз данных, такие как деградации времени отклика и рост failure rate.",
    # databases line 19 (с BOMJ, чистится)
    'To avoid false-positive problem notifications, [automated anomaly detection](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center") is only available for applications and services that have run for at least 20% of a week (7 days).': 'Чтобы избежать false-positive оповещений о проблемах, [automated anomaly detection](https://dt-url.net/5r5p0pnz/ "Visit Dynatrace support center") доступно только для приложений и сервисов, проработавших не менее 20% недели (7 дней).',
    # rum-web
    "Dynatrace automatically detects application-related performance anomalies such as response time degradations, failure rate increases, and traffic spikes. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for certain applications.": "Dynatrace автоматически обнаруживает аномалии производительности на уровне приложений, такие как деградации времени отклика, рост failure rate и всплески трафика. Используйте эти параметры, чтобы настроить чувствительность обнаружения, задать пороги оповещений или отключить алертинг для отдельных приложений.",
    # synthetic-http-performance-thresholds
    "Dynatrace generates a new problem if this synthetic monitor exceeds any of the performance thresholds below in 3 of the 5 most recent executions at a given location, unless there is an open maintenance window for the synthetic monitor. Multiple locations with 3 such violations can be included in a problem. The problem is closed if no performance threshold is violated in the 5 most recent executions at each of the previously affected locations.": "Dynatrace создаёт новую problem, если этот synthetic-монитор превышает любой из перечисленных ниже порогов производительности в 3 из 5 последних выполнений в данной локации, при условии что для synthetic-монитора нет открытого maintenance window. В одну problem могут быть включены несколько локаций с тремя такими нарушениями. Problem закрывается, если ни один из порогов производительности не нарушен в 5 последних выполнениях в каждой ранее затронутой локации.",
    # logmonitoring-schemaless-log-metric (содержит DavisÂ® и BOMJ; ключ с double-B сохраняем как есть)
    "With log metrics, you can use queries to create metrics from logs data for dashboarding, analysis, and custom alerting. Log metrics consume [Davis"
    + DB_R
    + " data units](https://dt-url.net/vg43xi8).": "С log-метриками можно по запросам строить метрики из данных логов для дашбордов, аналитики и custom-алертинга. Log-метрики расходуют [Davis"
    + DB_R
    + " data units](https://dt-url.net/vg43xi8).",
    "Note that newly-defined log metrics are available only for log data ingested after metric creation.": "Учтите, что только что определённые log-метрики применяются только к данным логов, поступившим после создания метрики.",
    # rum-web-resource-cleanup-rules (BOMJ чистится)
    "Resource URL cleanup rules are used to aggregate resource URLs that are otherwise identical except for dynamic elements such as IDs (for example, from REST APIs), query strings (for example, random arguments that disable caching), and other session data. Once such session-specific detail is stripped away, URLs are displayed in aggregate within waterfall analysis view. Note that resource URL cleanup rules are executed in the order specified below. For complete details about cleanup rules, visit [Define URL cleanup rules](https://dt-url.net/resource-cleanup-rules-response-codes).": "Resource URL cleanup rules используются для агрегации URL ресурсов, которые в остальном идентичны, но различаются динамическими элементами: идентификаторами (например, из REST API), query-строками (например, случайные аргументы, отключающие кеширование) и прочими session-данными. После того как такие session-специфичные детали отбрасываются, URL отображаются в агрегированном виде в waterfall analysis. Учтите, что resource URL cleanup rules выполняются в порядке, указанном ниже. Подробнее о cleanup rules см. [Define URL cleanup rules](https://dt-url.net/resource-cleanup-rules-response-codes).",
    # devobs-sensitive-data-masking
    "Create rules to mask any information you consider to be sensitive. Masking is done on OneAgent and no personal data is sent or stored on Dynatrace servers.": "Создавайте правила, чтобы маскировать любую информацию, которую считаете чувствительной. Маскирование выполняется на OneAgent, персональные данные не передаются и не хранятся на серверах Dynatrace.",
}

PARAM_LABEL = {
    # Shared / общие
    "Enabled": "Включено",
    "Name": "Имя",
    "Description": "Описание",
    "Type": "Тип",
    "Threshold": "Порог",
    "Sensitivity": "Чувствительность",
    "Key": "Ключ",
    "Value": "Значение",
    "Active": "Активно",
    "Operator": "Оператор",
    # metric-events
    "Summary": "Краткое описание",
    "Query definition": "Определение запроса",
    "Monitoring strategy": "Стратегия мониторинга",
    "Event template": "Шаблон события",
    "Dimension key of entity for events": "Dimension-ключ сущности для событий",
    "Config id": "Идентификатор конфигурации",
    "Metric selector": "Metric selector",
    "Metric key": "Ключ метрики",
    "Aggregation": "Агрегация",
    "Management zone": "Management zone",
    "Query offset": "Сдвиг запроса",
    "Entities": "Сущности",
    "Dimension filter": "Dimension filter",
    "Model type": "Тип модели",
    "Alert on missing data": "Оповещать при отсутствии данных",
    "Number of signal fluctuations": "Число колебаний сигнала",
    "Tolerance": "Tolerance",
    "Alert condition": "Условие оповещения",
    "Violating samples": "Нарушающие samples",
    "Sliding window": "Скользящее окно",
    "Dealerting samples": "Dealerting samples",
    "Title": "Заголовок",
    "Event type": "Тип события",
    "Allow merge": "Разрешить объединение",
    "Properties": "Свойства",
    "Dimension key of entity type": "Dimension-ключ типа сущности",
    "Dimension key": "Dimension-ключ",
    "Dimension value": "Значение dimension",
    "Filter type": "Тип фильтра",
    # rum-mobile / rum-custom / rum-web
    "Error rate increase": "Рост error rate",
    "Slow user actions": "Медленные user actions",
    "Unexpected low load": "Неожиданно низкая нагрузка",
    "Unexpected high load": "Неожиданно высокая нагрузка",
    "Detect reported error rate increase": "Обнаруживать рост сообщаемых error rate",
    "Detection strategy for error rate increases": "Стратегия обнаружения роста error rate",
    "Detect slow user actions": "Обнаруживать медленные user actions",
    "Detection strategy for slow user actions": "Стратегия обнаружения медленных user actions",
    "Detect unexpected low load": "Обнаруживать неожиданно низкую нагрузку",
    "Alert if the observed traffic drops below this threshold": "Оповестить, если наблюдаемый трафик падает ниже этого порога",
    "Detect unexpected high load": "Обнаруживать неожиданно высокую нагрузку",
    "Alert if the observed traffic exceeds this threshold": "Оповестить, если наблюдаемый трафик превышает этот порог",
    "Absolute threshold": "Абсолютный порог",
    "Relative threshold": "Относительный порог",
    "Detection sensitivity": "Чувствительность обнаружения",
    "All user actions": "Все user actions",
    "Slowest 10%": "Самые медленные 10%",
    "Avoid over-alerting": "Избегать over-alerting",
    # services / databases
    "Response time": "Response time",
    "Failure rate": "Failure rate",
    "Service load drops": "Падения нагрузки на сервис",
    "Service load spikes": "Всплески нагрузки на сервис",
    "Database failed connects": "Неудачные подключения к БД",
    "Detect response time degradations": "Обнаруживать деградации response time",
    "Detection mode for response time degradations": "Режим обнаружения деградаций response time",
    "Detect increases in failure rate": "Обнаруживать рост failure rate",
    "Detection mode for increases in failure rate": "Режим обнаружения роста failure rate",
    "Detect service load drops": "Обнаруживать падения нагрузки на сервис",
    "Alert if the observed load is less than this percentage of the expected value": "Оповестить, если наблюдаемая нагрузка меньше этого процента от ожидаемого значения",
    "Time span": "Интервал",
    "Detect service load spikes": "Обнаруживать всплески нагрузки на сервис",
    "Alert if the observed load is more than this percentage of the expected value": "Оповестить, если наблюдаемая нагрузка больше этого процента от ожидаемого значения",
    "Detect failed database connects": "Обнаруживать неудачные подключения к БД",
    "All requests": "Все запросы",
    "Only alert if there are at least": "Оповещать, только если запросов не менее",
    "Only alert if the abnormal state remains for at least": "Оповещать, только если abnormal state длится не менее",
    "Alert if the response time degrades beyond this many ms within an observation period of 5 minutes": "Оповестить, если response time деградирует более чем на столько мс в наблюдательном периоде 5 минут",
    "Alert if the response time of the slowest 10% degrades beyond this many ms within an observation period of 5 minutes": "Оповестить, если response time самых медленных 10% деградирует более чем на столько мс в наблюдательном периоде 5 минут",
    # rum-web
    "Error rate": "Error rate",
    "Detect traffic drops": "Обнаруживать падения трафика",
    "Detect traffic spikes": "Обнаруживать всплески трафика",
    "Detect key performance metric degradations": "Обнаруживать деградации key performance metric",
    "Detection strategy for key performance metric degradations": "Стратегия обнаружения деградаций key performance metric",
    "Detect increases in JavaScript errors": "Обнаруживать рост JavaScript-ошибок",
    "Detection strategy for increases in JavaScript errors": "Стратегия обнаружения роста JavaScript-ошибок",
    "Alert if this custom error rate threshold is exceeded during any 5-minute-period": "Оповестить, если этот custom error rate превышен в любом 5-минутном периоде",
    "Minimum number of actions per minute": "Минимальное число actions в минуту",
    "Amount of minutes the observed traffic has to stay in abnormal state before alert": "Сколько минут наблюдаемый трафик должен оставаться в abnormal state до оповещения",
    "Alert if the observed traffic is less than this percentage of the expected value": "Оповестить, если наблюдаемый трафик меньше этого процента от ожидаемого значения",
    "Minutes the observed traffic has to stay in abnormal state before alert": "Минуты, в течение которых наблюдаемый трафик должен оставаться в abnormal state до оповещения",
    "Alert if the observed traffic is more than this percentage of the expected value": "Оповестить, если наблюдаемый трафик больше этого процента от ожидаемого значения",
    "Minutes an application has to stay in abnormal state before alert": "Минуты, в течение которых приложение должно оставаться в abnormal state до оповещения",
    "Alert if the key performance metric degrades beyond this many ms within an observation period of 5 minutes": "Оповестить, если key performance metric деградирует более чем на столько мс в наблюдательном периоде 5 минут",
    "Alert if the key performance metric of the slowest 10% degrades beyond this many ms within an observation period of 5 minutes": "Оповестить, если key performance metric самых медленных 10% деградирует более чем на столько мс в наблюдательном периоде 5 минут",
    "Alert if the key performance metric of all requests degrades beyond this threshold": "Оповестить, если key performance metric всех запросов деградирует выше этого порога",
    "Alert if the key performance metric of the slowest 10% of requests degrades beyond this threshold": "Оповестить, если key performance metric самых медленных 10% запросов деградирует выше этого порога",
    "Alert if the median response time of all requests degrades beyond this threshold within an observation period of 5 minutes": "Оповестить, если медианный response time всех запросов деградирует выше этого порога в наблюдательном периоде 5 минут",
    "Alert if the response time of the slowest 10% of requests degrades beyond this threshold within an observation period of 5 minutes": "Оповестить, если response time самых медленных 10% запросов деградирует выше этого порога в наблюдательном периоде 5 минут",
    # synthetic-http-performance-thresholds
    "Generate a problem and send an alert on performance threshold violations": "Создавать problem и отправлять оповещение при нарушении порогов производительности",
    "Performance thresholds": "Пороги производительности",
    "Request": "Запрос",
    "Threshold (in seconds)": "Порог (в секундах)",
    # logmonitoring-schemaless-log-metric
    "Matcher": "Matcher",
    "Metric measurement": "Тип измерения метрики",
    "Attribute": "Атрибут",
    "Dimensions": "Dimensions",
    # rum-web-resource-cleanup-rules
    "Regular expression": "Регулярное выражение",
    "Replace with": "Заменить на",
    # devobs-sensitive-data-masking
    "Rule Name": "Имя правила",
    "Rule Type": "Тип правила",
    "Variable Name": "Имя переменной",
    "Comparison Type": "Тип сравнения",
    "Regex Pattern": "Regex-шаблон",
    "Data Replacement": "Замена данных",
    "Replacement Pattern": "Шаблон замены",
}

PARAM_DESC = {
    # metric-events
    "The textual summary of the metric event entry": "Текстовое краткое описание записи metric event",
    "Controls the preferred entity type used for triggered events.": "Управляет предпочтительным типом сущности, используемым для срабатывающих событий.",
    "To learn more, visit [Metric Selector](https://dt-url.net/metselad)": "Подробнее см. [Metric Selector](https://dt-url.net/metselad)",
    "Minute offset of sliding evaluation window for metrics with latency": "Сдвиг скользящего evaluation window в минутах для метрик с задержкой",
    "Use rule-based filters to define the scope this event monitors.": "Используйте rule-based фильтры, чтобы задать область, которую отслеживает это событие.",
    "Metric-key-based query definitions only support static thresholds.": "Query-definition по metric key поддерживают только статические пороги.",
    "Raise an event if this value is violated": "Создавать событие при нарушении этого значения",
    "The ability to set an alert on missing data in a metric. When enabled, missing data samples will be treated as violating samples defined in the advanced model properties. When disabled, missing data is not treated as a violation but will still contribute to dealerting. We recommend disabling alerting on missing data for sparse timeseries to avoid false alerts. To learn more, visit [anomaly detection configuration](https://dt-url.net/lz02mwi).": "Возможность задать оповещение об отсутствии данных в метрике. Если включено, missing data samples трактуются как нарушающие samples, определённые в advanced model properties. Если отключено, отсутствие данных не считается нарушением, но всё равно влияет на dealerting. Для разрежённых timeseries рекомендуется отключить оповещения по missing data, чтобы избежать ложных алертов. Подробнее см. [anomaly detection configuration](https://dt-url.net/lz02mwi).",
    "Controls how many times the signal fluctuation is added to the baseline to produce the actual threshold for alerting": "Управляет тем, сколько раз значение колебания сигнала прибавляется к baseline для получения фактического порога оповещения",
    "Controls the width of the confidence band and larger values lead to a less sensitive model": "Управляет шириной confidence band; чем больше значение, тем менее чувствительна модель",
    "The number of one-minute samples within the evaluation window that must violate to trigger an event.": "Сколько одноминутных samples в evaluation window должны нарушить условие, чтобы событие сработало.",
    "The number of one-minute samples that form the sliding evaluation window.": "Сколько одноминутных samples формируют скользящее evaluation window.",
    "The number of one-minute samples within the evaluation window that must go back to normal to close the event.": "Сколько одноминутных samples в evaluation window должны вернуться к норме, чтобы событие закрылось.",
    "The title of the event to trigger. Type '{' for placeholder hints.": "Заголовок события, которое нужно триггернуть. Введите '{' для подсказок по плейсхолдерам.",
    "The description of the event to trigger. Type '{' for placeholder hints.": "Описание события, которое нужно триггернуть. Введите '{' для подсказок по плейсхолдерам.",
    "The event type to trigger.": "Тип события, которое нужно триггернуть.",
    "Davis"
    + DB_R
    + " AI will try to merge this event into existing problems, otherwise a new problem will always be created.": "Davis"
    + DB_R
    + " AI попытается смержить это событие в существующие problems, иначе всегда будет создаваться новая problem.",
    "Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2](https://dt-url.net/9622g1w).": "Набор дополнительных key-value свойств, прикрепляемых к срабатывающему событию. Получить список доступных property keys можно через [Events API v2](https://dt-url.net/9622g1w).",
    "Dimension key of entity type to filter": "Dimension-ключ типа сущности для фильтрации",
    "Type 'dt.' for key hints.": "Введите 'dt.' для подсказок по ключам.",
    "Type '{' for placeholder hints.": "Введите '{' для подсказок по плейсхолдерам.",
    # rum-mobile / rum-custom / rum-web
    "Alert if the percentage of user actions affected by reported errors exceeds **both** the absolute threshold and the relative threshold": "Оповестить, если процент user actions, затронутых сообщаемыми ошибками, превышает **одновременно** абсолютный и относительный пороги",
    "Alert if the custom reported error rate threshold is exceeded during any 5-minute period": "Оповестить, если custom-порог сообщаемого error rate превышен в любом 5-минутном периоде",
    "Dynatrace learns your typical application traffic over an observation period of one week. Depending on this expected value Dynatrace detects abnormal traffic drops within your application.": "Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю. На основе этого ожидаемого значения Dynatrace выявляет аномальные падения трафика в приложении.",
    "Dynatrace learns your typical application traffic over an observation period of one week. Depending on this expected value Dynatrace detects abnormal traffic spikes within your application.": "Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю. На основе этого ожидаемого значения Dynatrace выявляет аномальные всплески трафика в приложении.",
    # rum-web — вариант с двойным пробелом, отличается от rum-mobile/custom формулировкой
    "Dynatrace learns your typical application traffic over an observation period of one week.  Depending on this expected value Dynatrace detects abnormal traffic drops within your application.": "Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю.  На основе этого ожидаемого значения Dynatrace выявляет аномальные падения трафика в приложении.",
    "Dynatrace learns your typical application traffic over an observation period of one week.  Depending on this expected value Dynatrace detects abnormal traffic spikes within your application.": "Dynatrace изучает типичный трафик вашего приложения за наблюдательный период в одну неделю.  На основе этого ожидаемого значения Dynatrace выявляет аномальные всплески трафика в приложении.",
    "Alert if the action duration of all user actions degrades beyond **both** the absolute and relative threshold:": "Оповестить, если длительность всех user actions деградирует выше **одновременно** абсолютного и относительного порога:",
    "Alert if the action duration of the slowest 10% of user actions degrades beyond **both** the absolute and relative threshold:": "Оповестить, если длительность самых медленных 10% user actions деградирует выше **одновременно** абсолютного и относительного порога:",
    "To avoid over-alerting do not alert for low traffic applications with less than": "Чтобы избежать over-alerting, не оповещать для low-traffic приложений с менее чем",
    "Alert if the action duration of all user actions degrades beyond the absolute threshold:": "Оповестить, если длительность всех user actions деградирует выше абсолютного порога:",
    "Alert if the action duration of the slowest 10% of user actions degrades beyond the absolute threshold:": "Оповестить, если длительность самых медленных 10% user actions деградирует выше абсолютного порога:",
    "Alert if the percentage of failing user actions increases by **both** the absolute and relative thresholds:": "Оповестить, если процент проваливающихся user actions растёт **одновременно** на абсолютный и относительный пороги:",
    # services / databases
    "Alert if the observed load is lower than the expected load by a specified margin for a specified amount of time:  Dynatrace learns your typical service load over an observation period of one week.": "Оповестить, если наблюдаемая нагрузка ниже ожидаемой на заданную величину в течение заданного времени:  Dynatrace изучает типичную нагрузку сервиса за наблюдательный период в одну неделю.",
    "Alert if the observed load exceeds the expected load by a specified margin for a specified amount of time:  Dynatrace learns your typical service load over an observation period of one week.": "Оповестить, если наблюдаемая нагрузка превышает ожидаемую на заданную величину в течение заданного времени:  Dynatrace изучает типичную нагрузку сервиса за наблюдательный период в одну неделю.",
    "Alert if the observed load is lower than the expected load by a specified margin for a specified amount of time.  Dynatrace learns your typical service load over an observation period of one week.": "Оповестить, если наблюдаемая нагрузка ниже ожидаемой на заданную величину в течение заданного времени.  Dynatrace изучает типичную нагрузку сервиса за наблюдательный период в одну неделю.",
    "Alert if the observed load exceeds the expected load by a specified margin for a specified amount of time.  Dynatrace learns your typical service load over an observation period of one week.": "Оповестить, если наблюдаемая нагрузка превышает ожидаемую на заданную величину в течение заданного времени.  Dynatrace изучает типичную нагрузку сервиса за наблюдательный период в одну неделю.",
    "Alert if the number of failed database connects within the specified time exceeds the specified absolute threshold:": "Оповестить, если число неудачных подключений к БД за заданное время превышает указанный абсолютный порог:",
    "Alert if the percentage of failing service calls increases by **both** the absolute and relative thresholds:": "Оповестить, если процент проваливающихся вызовов сервиса растёт **одновременно** на абсолютный и относительный пороги:",
    "Alert if a given failure rate is exceeded during any 5-minute-period": "Оповестить, если заданный failure rate превышен в любом 5-минутном периоде",
    "Alert if the median response time of all requests degrades beyond **both** the absolute and relative thresholds:": "Оповестить, если медианный response time всех запросов деградирует выше **одновременно** абсолютного и относительного порогов:",
    "Alert if the response time of the slowest 10% of requests degrades beyond **both** the absolute and relative thresholds:": "Оповестить, если response time самых медленных 10% запросов деградирует выше **одновременно** абсолютного и относительного порогов:",
    "Alert if the median response time of all requests degrades beyond this threshold:": "Оповестить, если медианный response time всех запросов деградирует выше этого порога:",
    "Alert if the response time of the slowest 10% of requests degrades beyond this threshold:": "Оповестить, если response time самых медленных 10% запросов деградирует выше этого порога:",
    "Alert if the median response time of all requests degrades beyond this threshold within an observation period of 5 minutes:": "Оповестить, если медианный response time всех запросов деградирует выше этого порога в наблюдательном периоде 5 минут:",
    "Alert if the response time of the slowest 10% of requests degrades beyond this threshold within an observation period of 5 minutes:": "Оповестить, если response time самых медленных 10% запросов деградирует выше этого порога в наблюдательном периоде 5 минут:",
    # rum-web — user actions варианты (rum-web использует user actions вместо requests)
    "Alert if the median response time of all user actions degrades beyond **both** the absolute and relative thresholds:": "Оповестить, если медианный response time всех user actions деградирует выше **одновременно** абсолютного и относительного порогов:",
    "Alert if the key performance metric of all requests degrades beyond this threshold:": "Оповестить, если key performance metric всех запросов деградирует выше этого порога:",
    "Alert if the key performance metric of the slowest 10% of requests degrades beyond this threshold:": "Оповестить, если key performance metric самых медленных 10% запросов деградирует выше этого порога:",
    "To avoid over-alerting for low traffic applications": "Чтобы избежать over-alerting для low-traffic приложений",
    "Only alert if there are at least": "Оповещать, только если запросов не менее",
    # logmonitoring-schemaless-log-metric
    "To enable splitting on your metric, add desired dimensions.  You can select a dimension name from the list or set it to any value. To extract fields from logs, you can use log processing (`<your-dynatrace-url>/builtin:logmonitoring.log-dpp-rules`).": "Чтобы включить splitting метрики, добавьте нужные dimensions.  Имя dimension можно выбрать из списка или задать произвольное значение. Для извлечения полей из логов используйте log processing (`<your-dynatrace-url>/builtin:logmonitoring.log-dpp-rules`).",
    # rum-web-resource-cleanup-rules
    "For example: *Mask journeyId*": "Например: *Mask journeyId*",
    r"For example: `(.*)(journeyId=)-?\d+(.*)`": r"Например: `(.*)(journeyId=)-?\d+(.*)`",
    r"For example: `$1$2\*$3`": r"Например: `$1$2\*$3`",
    # devobs-sensitive-data-masking
    "Choose whether to redact by variable name or regex.": "Выберите, маскировать по имени переменной или по regex.",
    "Select how the variable name should be matched.": "Выберите, как должно сопоставляться имя переменной.",
    "Choose how the sensitive data should be replaced.": "Выберите, как должны заменяться чувствительные данные.",
}

STRUCT = [
    (
        "* Published Dec 05, 2023",
        "* Опубликовано 05 декабря 2023",
    ),
    (
        "* Published Aug 05, 2024",
        "* Опубликовано 05 августа 2024",
    ),
    (
        "| Schema ID | Schema groups | Scope |",
        "| Schema ID | Группы схемы | Scope |",
    ),
    (
        "Retrieve schema via Settings API",
        "Получить schema через Settings API",
    ),
    (
        "## Authentication",
        "## Аутентификация",
    ),
    (
        "## Parameters",
        "## Параметры",
    ),
    (
        "To execute this request, you need an access token with **Read settings** "
        "(`settings.read`) scope. To learn how to obtain and use it, see "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Для выполнения запроса необходим access token со scope **Read settings** "
        "(`settings.read`). О том, как получить и использовать токен, см. "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "| Property | Type | Description | Required |",
        "| Свойство | Тип | Описание | Обязательный |",
    ),
]

ENUM_PHRASE = ("The element has these enums", "Возможные значения:")


def _normalize(t):
    t = t.replace("\r\n", "\n")
    t = t.replace(chr(0xFEFF), "")
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")
    return t


def _heading(line):
    marker = " (`builtin:"
    i = line.find(marker)
    if not line.startswith("### ") or i == -1:
        return None
    name = line[4:i]
    tail = line[i:]
    ru = DISPLAY_NAME.get(name)
    if ru is None:
        return None
    return "### " + ru + tail


def _param_row(line):
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 4:
        return None
    c0, ctype, cdesc, creq = cells
    if "`" not in c0:
        return None
    bt = c0.find("`")
    label = c0[:bt].rstrip()
    code = c0[bt:]
    sep = c0[len(label) : bt]
    if label and label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL.get(label, label)
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    marker_len = len(ENUM_PHRASE[0])
    if ei == -1:
        ei = d.find(ENUM_PHRASE[1])
        marker_len = len(ENUM_PHRASE[1])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + marker_len :]
        if head == "" or head == "-":
            new_desc = ENUM_PHRASE[1] + enum_tail
        else:
            head_ru = PARAM_DESC.get(head, head)
            new_desc = head_ru + " " + ENUM_PHRASE[1] + enum_tail
    else:
        new_desc = "-" if d == "-" else PARAM_DESC.get(d, d)
    return (
        "| "
        + new_label
        + sep
        + code
        + " | "
        + ctype
        + " | "
        + new_desc
        + " | "
        + creq
        + " |"
    )


NESTED_HEADING_RE = _re.compile(r"^##### The (`[^`]+`) object$")


def _nested_heading(line):
    m = NESTED_HEADING_RE.match(line)
    if not m:
        return None
    return "##### Объект " + m.group(1)


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    for en, ru in SCHEMA_DESC.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    t = t.replace(ENUM_PHRASE[0], ENUM_PHRASE[1])
    out = []
    for line in t.split("\n"):
        nl = _heading(line) or _nested_heading(line) or _param_row(line)
        out.append(nl if nl is not None else line)
    t = "\n".join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return src, dst


if __name__ == "__main__":
    bad = 0
    for rel in PILOT:
        src, dst = build(rel)
        en_n = (
            io.open(src, "r", encoding="utf-8", newline="")
            .read()
            .replace("\r\n", "\n")
            .count("\n")
        )
        ru_n = io.open(dst, "r", encoding="utf-8", newline="").read().count("\n")
        flag = "" if en_n == ru_n else "  <<< PARITY MISMATCH"
        if flag:
            bad += 1
        print("%-72s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
