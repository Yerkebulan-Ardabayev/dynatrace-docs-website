# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/advanced-configuration/extension-customize.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/advanced-configuration"

TRANS = {
    "title: Customize data with extensions": "title: Настройка данных с помощью расширений",
    "# Customize data with extensions": "# Настройка данных с помощью расширений",
    "* How-to guide": "* Практическое руководство",
    "* 7-min read": "* Чтение: 7 мин",
    "* Updated on Oct 28, 2025": "* Обновлено 28 октября 2025 г.",
    "You can tailor various aspects of Dynatrace to the specifics of data acquired by your extension. You can also use the extension to introduce a new configuration in your environment (for example, organize data in dashboards, create new alerts, or introduce complex metrics).": "Различные аспекты Dynatrace можно настроить в соответствии со спецификой данных, получаемых расширением. Расширение также позволяет вводить новую конфигурацию в окружение: например, упорядочивать данные на панелях мониторинга, создавать оповещения или добавлять сложные метрики.",
    "## Custom Dynatrace UI": "## Пользовательский интерфейс Dynatrace",
    "The Extensions 2.0 framework enables you to tailor the Dynatrace UI for the specific needs of the data ingested by your extension. You can add customized dashboards or specialized unified analysis pages to your extension.": "Extensions 2.0 framework позволяет адаптировать интерфейс Dynatrace под конкретные потребности данных, принимаемых расширением. К расширению можно добавлять настраиваемые панели мониторинга или специализированные страницы унифицированного анализа.",
    'For more information, see [Extend Dynatrace with domain-specific web UI](/managed/ingest-from/extend-dynatrace/extend-ui "Extend the Dynatrace web UI using entity-tailored unified analysis pages.").': 'Дополнительные сведения см. в разделе [Расширение Dynatrace с помощью предметно-ориентированного веб-интерфейса](/managed/ingest-from/extend-dynatrace/extend-ui "Расширение веб-интерфейса Dynatrace с помощью адаптированных под сущности страниц унифицированного анализа.").',
    "## Custom metric events": "## Пользовательские события метрик",
    "You can create custom metric events based on the metrics extracted by your extension and add the exported definitions to your extension archive. This way, you can distribute the custom metric events among Dynatrace environments.": "На основе метрик, извлекаемых расширением, можно создавать пользовательские события метрик и добавлять экспортированные определения в архив расширения. Это позволяет распространять пользовательские события метрик по окружениям Dynatrace.",
    "Export custom event for alerting definition": "Экспорт определения пользовательского события для оповещения",
    "1. Go to **Settings** > **Anomaly detection** > **Metric events**.": "1. Откройте **Settings** > **Anomaly detection** > **Metric events**.",
    "2. Expand the event of your choice.": "2. Разверните нужное событие.",
    "3. Scroll to the bottom of the definition where you'll find the `Config id` parameter (for example, `id=1be8d58d-71a7-4566-9058-754d635363ab`) and save the parameter value.": "3. Прокрутите до нижней части определения, где находится параметр `Config id` (например, `id=1be8d58d-71a7-4566-9058-754d635363ab`), и сохраните его значение.",
    "4. Run the following command to get the definition of the custom metric event. For this example, we use the Dynatrace SaaS URL:": "4. Выполните следующую команду для получения определения пользовательского события метрики. В данном примере используется URL Dynatrace SaaS:",
    "Replace:": "Замените:",
    '* `{env-id}` with your [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': '* `{env-id}` на [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Знакомство с окружениями мониторинга и работа с ними.").',
    '* `{api-token}` with an [API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': '* `{api-token}` на [API-токен](/managed/dynatrace-api/basics/dynatrace-api-authentication "Как пройти аутентификацию для использования Dynatrace API.") с необходимыми [разрешениями](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.").',
    "* `{custom-event-id}` with the custom metric event identifier you determined in the previous step.": "* `{custom-event-id}` на идентификатор пользовательского события метрики, определённый на предыдущем шаге.",
    "5. The call returns the JSON payload containing a custom metric event definition. Save it as a JSON file.": "5. Вызов возвращает JSON-полезную нагрузку с определением пользовательского события метрики. Сохраните её как JSON-файл.",
    "6. Declare the exported JSON files in your `extension.yaml` file and add them to your extension package.": "6. Объявите экспортированные JSON-файлы в файле `extension.yaml` и добавьте их в пакет расширения.",
    'For more information, see [Extensions 2.0 hands-on excercise](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Learn about WMI extensions in the Extensions framework.").': 'Дополнительные сведения см. в разделе [Практическое упражнение Extensions 2.0](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Знакомство с WMI-расширениями в Extensions framework.").',
    "After you upload or update an extension containing custom metric events, make sure you enable the events you'd like to use. The extension-imported events are disabled by default after each upload and activation, inluding an update. To enable metric events, go to **Settings** > **Anomaly detection** > **Metric events**.": "После загрузки или обновления расширения с пользовательскими событиями метрик необходимо включить нужные события. Импортированные расширением события по умолчанию отключены после каждой загрузки и активации, включая обновление. Для включения событий метрик откройте **Settings** > **Anomaly detection** > **Metric events**.",
    "## Custom topology": "## Пользовательская топология",
    "After you start to send in your own data via an extension, you might be interested in extending the built-in topology model by adding your own domain-related entity types and relationships.": "После начала отправки данных через расширение может потребоваться расширить встроенную модель топологии путём добавления собственных типов сущностей и связей, относящихся к предметной области.",
    'For more information, see [Custom topology model](/managed/ingest-from/extend-dynatrace/extend-topology "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to.").': 'Дополнительные сведения см. в разделе [Пользовательская модель топологии](/managed/ingest-from/extend-dynatrace/extend-topology "Обеспечение обогащённого контекстом анализа входящих наблюдений в контексте связанных отслеживаемых сущностей.").',
    "## Custom metric metadata": "## Метаданные пользовательских метрик",
    "To add more context to data points and their dimensions ingested by your extension, your custom metric can carry additional useful information, such as the unit of measurement, display name, and value ranges.": "Для добавления контекста к точкам данных и их измерениям, принимаемым расширением, пользовательская метрика может содержать дополнительную полезную информацию: единицы измерения, отображаемое имя и диапазоны значений.",
    "You can provide such information via custom metric metadata. Metadata is stored independently from data points and tied together by the metric key. You can push data points and set metadata in any order.": "Такую информацию можно предоставить через метаданные пользовательских метрик. Метаданные хранятся независимо от точек данных и связаны с ними ключом метрики. Точки данных и метаданные можно передавать в любом порядке.",
    'For more information, see [Custom metric metadata](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.").': 'Дополнительные сведения см. в разделе [Метаданные пользовательских метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Предоставление метаданных для пользовательской метрики.").',
    "### Data filtering": "### Фильтрация данных",
    "Extensions also allow you to filter data based on specific criteria. This filtering capability is particularly useful for SNMP extensions, where you might want to limit the data that is ingested by the extension": "Расширения также позволяют фильтровать данные по определённым критериям. Эта возможность особенно полезна для SNMP-расширений, где может потребоваться ограничить объём данных, принимаемых расширением.",
    "Filters match entity names to include/exclude certain configurations from monitoring. This makes the data more relevant and saves unnecessary license consumption. Filters work with a specific entity type and support the following syntax:": "Фильтры сопоставляют имена сущностей для включения или исключения определённых конфигураций из мониторинга. Это делает данные более актуальными и экономит лицензионные ресурсы. Фильтры работают с конкретным типом сущностей и поддерживают следующий синтаксис:",
    "| Expression | Description |": "| Выражение | Описание |",
    "| --- | --- |": "| --- | --- |",
    "| `$eq(<str>)` | Checks if `<str>` matches what you're filtering |": "| `$eq(<str>)` | Проверяет, соответствует ли `<str>` фильтруемому значению |",
    "| `$prefix(...)` | Begins with … |": "| `$prefix(...)` | Начинается с… |",
    "| `$suffix(...)` | Ends with … |": "| `$suffix(...)` | Заканчивается на… |",
    "| `$contains(...)` | Contains … |": "| `$contains(...)` | Содержит… |",
    "| `$and(<expr1>, <expr2>)` | Chains two or more of the above expressions with the AND operator |": "| `$and(<expr1>, <expr2>)` | Объединяет два и более выражений оператором AND |",
    "| `$or(<expr1>, <expr2>)` | Chains two or more of the above expressions with the OR operator |": "| `$or(<expr1>, <expr2>)` | Объединяет два и более выражений оператором OR |",
    "| `$not(<expr>)` | Negates an expression. For example, to exclude all Pools from the Common partition, you can add the `$not($prefix(/Common/))` filter. |": "| `$not(<expr>)` | Отрицает выражение. Например, для исключения всех пулов из раздела Common добавьте фильтр `$not($prefix(/Common/))`. |",
    "## Custom process group detection rules": "## Правила обнаружения пользовательских групп процессов",
    'Dynatrace detects which processes are part of the same [process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") by means of a default set of detection rules. However, you can add your own process detection rules suited to the data retrieved by your extension.': 'Dynatrace определяет, какие процессы входят в одни и те же [группы процессов](/managed/observe/infrastructure-observability/process-groups "Анализ групп процессов и настройка именования, обнаружения и мониторинга."), используя набор правил обнаружения по умолчанию. Однако можно добавлять собственные правила обнаружения процессов, соответствующие данным, получаемым расширением.',
    'For more information, see [Process group detection](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").': 'Дополнительные сведения см. в разделе [Обнаружение групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения групп процессов").',
    "## Log metrics, events, and processing rules": "## Метрики журналов, события и правила обработки",
    'After you enable [log ingestion](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") into Dynatrace you can define the log metrics, events, and add your own log processing rules to be shipped with your extension.': 'После включения [приёма журналов](/managed/analyze-explore-automate/log-monitoring "Узнайте, как включить мониторинг журналов, какие данные он предоставляет и многое другое.") в Dynatrace можно определять метрики журналов, события и добавлять собственные правила обработки журналов, поставляемые вместе с расширением.',
    "For general information, on your logs configuration, see": "Общие сведения о конфигурации журналов см. в следующих разделах:",
    '* [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.")': '* [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранный вариант недоступен в Dynatrace Managed.")',
    "The Extensions YAML file supports the same fields as the Settings 2.0 schemas:": "Файл YAML расширений поддерживает те же поля, что и схемы Settings 2.0:",
    '* [Log metrics](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-schemaless-log-metric "View builtin:logmonitoring.schemaless-log-metric settings schema table of your monitoring environment via the Dynatrace API.")': '* [Метрики журналов](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-schemaless-log-metric "Просмотр таблицы схемы настроек builtin:logmonitoring.schemaless-log-metric окружения мониторинга через Dynatrace API.")',
    '* [Log events](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events "View builtin:logmonitoring.log-events settings schema table of your monitoring environment via the Dynatrace API.")': '* [События журналов](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events "Просмотр таблицы схемы настроек builtin:logmonitoring.log-events окружения мониторинга через Dynatrace API.")',
    '* [Processing](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-dpp-rules "View builtin:logmonitoring.log-dpp-rules settings schema table of your monitoring environment via the Dynatrace API.")': '* [Обработка](/managed/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-dpp-rules "Просмотр таблицы схемы настроек builtin:logmonitoring.log-dpp-rules окружения мониторинга через Dynatrace API.")',
    "You define your custom log configuration in the Extensions YAML file, starting with the following nodes in the root of the file": "Пользовательская конфигурация журналов определяется в файле YAML расширений, начиная со следующих узлов в корне файла:",
    "* `logMetrics`": "* `logMetrics`",
    "* `logEvents`": "* `logEvents`",
    "* `logProcessingRules`": "* `logProcessingRules`",
    "To learn the structure of the definition, check the Extensions schemas:": "Для изучения структуры определения обратитесь к схемам Extensions:",
    "* `log.events.schema.json`": "* `log.events.schema.json`",
    "* `log.metrics.schema.json`": "* `log.metrics.schema.json`",
    "* `log.processing.rule.schema.dql.json`": "* `log.processing.rule.schema.dql.json`",
    "* `log.processing.rule.schema.json`": "* `log.processing.rule.schema.json`",
    "* `log.processing.rule.schema.lql.json`": "* `log.processing.rule.schema.lql.json`",
    'See [Extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#schemas "Learn how to create an extension YAML file using the Extensions framework.") to learn how to get the schema JSON files.': 'Сведения о том, как получить JSON-файлы схем, см. в разделе [Файл YAML расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#schemas "Узнайте, как создать файл YAML расширения с помощью Extensions framework.").',
    "Check the examples below on how to define your log metrics, events, and processing rules in the extension YAML file.": "Примеры определения метрик журналов, событий и правил обработки в файле YAML расширения приведены ниже.",
    "Log metrics": "Метрики журналов",
    "Log events": "События журналов",
    "Log processing rule": "Правило обработки журналов",
    "With this definition, you use the `RAPLACE_PATTERN` to mask sensitive data retrieved using the SQL data source.": "В данном определении используется `RAPLACE_PATTERN` для маскировки конфиденциальных данных, полученных через источник данных SQL.",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "extension-customize.md", TRANS, PASS)
    qa_one(REL, "extension-customize.md")
