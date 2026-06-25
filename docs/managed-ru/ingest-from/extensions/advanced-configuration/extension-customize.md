---
title: Настройка данных с помощью расширений
source: https://docs.dynatrace.com/managed/ingest-from/extensions/advanced-configuration/extension-customize
scraped: 2026-05-12T12:25:30.386143
---

# Настройка данных с помощью расширений

# Настройка данных с помощью расширений

* Практическое руководство
* Чтение: 7 мин
* Обновлено 28 октября 2025 г.

Различные аспекты Dynatrace можно настроить в соответствии со спецификой данных, получаемых расширением. Расширение также позволяет вводить новую конфигурацию в окружение: например, упорядочивать данные на панелях мониторинга, создавать оповещения или добавлять сложные метрики.

## Пользовательский интерфейс Dynatrace

Extensions 2.0 framework позволяет адаптировать интерфейс Dynatrace под конкретные потребности данных, принимаемых расширением. К расширению можно добавлять настраиваемые панели мониторинга или специализированные страницы унифицированного анализа.

Дополнительные сведения см. в разделе [Расширение Dynatrace с помощью предметно-ориентированного веб-интерфейса](/managed/ingest-from/extend-dynatrace/extend-ui "Расширение веб-интерфейса Dynatrace с помощью адаптированных под сущности страниц унифицированного анализа.").

## Пользовательские события метрик

На основе метрик, извлекаемых расширением, можно создавать пользовательские события метрик и добавлять экспортированные определения в архив расширения. Это позволяет распространять пользовательские события метрик по окружениям Dynatrace.

Экспорт определения пользовательского события для оповещения

1. Откройте **Settings** > **Anomaly detection** > **Metric events**.
2. Разверните нужное событие.
3. Прокрутите до нижней части определения, где находится параметр `Config id` (например, `id=1be8d58d-71a7-4566-9058-754d635363ab`), и сохраните его значение.
4. Выполните следующую команду для получения определения пользовательского события метрики. В данном примере используется URL Dynatrace SaaS:

   ```
   curl -X GET "https://{env-id}.live.dynatrace.com/api/config/v1/anomalyDetection/metricEvents/{custom-event-id}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token `{api-token}"
   ```

   Замените:

   * `{env-id}` на [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Знакомство с окружениями мониторинга и работа с ними.").
   * `{api-token}` на [API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для использования Dynatrace API.") с необходимыми [разрешениями](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.").
   * `{custom-event-id}` на идентификатор пользовательского события метрики, определённый на предыдущем шаге.
5. Вызов возвращает JSON-полезную нагрузку с определением пользовательского события метрики. Сохраните её как JSON-файл.
6. Объявите экспортированные JSON-файлы в файле `extension.yaml` и добавьте их в пакет расширения.

Дополнительные сведения см. в разделе [Практическое упражнение Extensions 2.0](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Знакомство с WMI-расширениями в Extensions framework.").

После загрузки или обновления расширения с пользовательскими событиями метрик необходимо включить нужные события. Импортированные расширением события по умолчанию отключены после каждой загрузки и активации, включая обновление. Для включения событий метрик откройте **Settings** > **Anomaly detection** > **Metric events**.

## Пользовательская топология

После начала отправки данных через расширение может потребоваться расширить встроенную модель топологии путём добавления собственных типов сущностей и связей, относящихся к предметной области.

Дополнительные сведения см. в разделе [Пользовательская модель топологии](/managed/ingest-from/extend-dynatrace/extend-topology "Обеспечение обогащённого контекстом анализа входящих наблюдений в контексте связанных отслеживаемых сущностей.").

## Метаданные пользовательских метрик

Для добавления контекста к точкам данных и их измерениям, принимаемым расширением, пользовательская метрика может содержать дополнительную полезную информацию: единицы измерения, отображаемое имя и диапазоны значений.

Такую информацию можно предоставить через метаданные пользовательских метрик. Метаданные хранятся независимо от точек данных и связаны с ними ключом метрики. Точки данных и метаданные можно передавать в любом порядке.

Дополнительные сведения см. в разделе [Метаданные пользовательских метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Предоставление метаданных для пользовательской метрики.").

### Фильтрация данных

Расширения также позволяют фильтровать данные по определённым критериям. Эта возможность особенно полезна для SNMP-расширений, где может потребоваться ограничить объём данных, принимаемых расширением.

Фильтры сопоставляют имена сущностей для включения или исключения определённых конфигураций из мониторинга. Это делает данные более актуальными и экономит лицензионные ресурсы. Фильтры работают с конкретным типом сущностей и поддерживают следующий синтаксис:

| Выражение | Описание |
| --- | --- |
| `$eq(<str>)` | Проверяет, соответствует ли `<str>` фильтруемому значению |
| `$prefix(...)` | Начинается с… |
| `$suffix(...)` | Заканчивается на… |
| `$contains(...)` | Содержит… |
| `$and(<expr1>, <expr2>)` | Объединяет два и более выражений оператором AND |
| `$or(<expr1>, <expr2>)` | Объединяет два и более выражений оператором OR |
| `$not(<expr>)` | Отрицает выражение. Например, для исключения всех пулов из раздела Common добавьте фильтр `$not($prefix(/Common/))`. |

## Правила обнаружения пользовательских групп процессов

Dynatrace определяет, какие процессы входят в одни и те же [группы процессов](/managed/observe/infrastructure-observability/process-groups "Анализ групп процессов и настройка именования, обнаружения и мониторинга."), используя набор правил обнаружения по умолчанию. Однако можно добавлять собственные правила обнаружения процессов, соответствующие данным, получаемым расширением.

Дополнительные сведения см. в разделе [Обнаружение групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения групп процессов").

## Метрики журналов, события и правила обработки

После включения [приёма журналов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов, какие данные он предоставляет и многое другое.") в Dynatrace можно определять метрики журналов, события и добавлять собственные правила обработки журналов, поставляемые вместе с расширением.

Общие сведения о конфигурации журналов см. в следующих разделах:

* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.")
* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.")

Файл YAML расширений поддерживает те же поля, что и схемы Settings 2.0:

* [Метрики журналов](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-schemaless-log-metric "Просмотр таблицы схемы настроек builtin:logmonitoring.schemaless-log-metric окружения мониторинга через Dynatrace API.")
* [События журналов](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events "Просмотр таблицы схемы настроек builtin:logmonitoring.log-events окружения мониторинга через Dynatrace API.")
* [Обработка](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-dpp-rules "Просмотр таблицы схемы настроек builtin:logmonitoring.log-dpp-rules окружения мониторинга через Dynatrace API.")

Пользовательская конфигурация журналов определяется в файле YAML расширений, начиная со следующих узлов в корне файла:

* `logMetrics`
* `logEvents`
* `logProcessingRules`

Для изучения структуры определения обратитесь к схемам Extensions:

* `log.events.schema.json`
* `log.metrics.schema.json`
* `log.processing.rule.schema.dql.json`
* `log.processing.rule.schema.json`
* `log.processing.rule.schema.lql.json`

Сведения о том, как получить JSON-файлы схем, см. в разделе [Файл YAML расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#schemas "Узнайте, как создать файл YAML расширения с помощью Extensions framework.").

Примеры определения метрик журналов, событий и правил обработки в файле YAML расширения приведены ниже.

Метрики журналов

```
name: custom:dynatrace.logmetric.test.extension



version: 1.0.0



minDynatraceVersion: "1.281.0"



author:



name: "John Doe"



logMetrics:



- key: log.test.extension.occurrence



query: content="AllProcessed"



enabled: true



measure: OCCURRENCE



- key: log.test.extension.attribute



query: content="AllProcessed"



enabled: true



measure: ATTRIBUTE



measureAttribute: dt.os.type



- key: log.test.extension.dimensions



query: content="AllProcessed"



enabled: true



measure: OCCURRENCE



dimensions: [



dimension1,



dimension2



]
```

События журналов

```
ame: custom:dynatrace.logevent.test.extension2



version: 1.0.0



minDynatraceVersion: "1.281.0"



author:



name: "John Doe"



logEvents:



- query: content="a"



enabled: true



summary: abc



eventTemplate:



title: log_event_a



description: ''



eventType: CUSTOM_ALERT



davisMerge: false



- query: content="a"



enabled: true



summary: abd



eventTemplate:



title: abd



description: My custom log event description :)



eventType: CUSTOM_ALERT



davisMerge: false
```

Правило обработки журналов

В данном определении используется `RAPLACE_PATTERN` для маскировки конфиденциальных данных, полученных через источник данных SQL.

```
logProcessingRules:



- ruleName: TopN statements masking



query: event.group="query_performance"



enabled: true



ProcessorDefinition:



rule: |



USING(INOUT content) | FIELDS_ADD(content: REPLACE_PATTERN(content, "(\"'\"):p1 (LD):p2 (\"'\"):p3", "${p1}${p2|sha1}${p3}"))



RuleTesting:



sampleLog: |



{



"event.group": "query_performance",



"content": "/*dt:ownQuery*/SELECT DECODE(name, 'sessions', value) AS sessions_limit, DECODE(name, 'processes', value) AS processes_limit FROM v$parameter WHERE name IN('sessions', 'processes')"



}
```