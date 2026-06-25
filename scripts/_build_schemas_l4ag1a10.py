# -*- coding: utf-8 -*-
"""L4-AG.1a.10 builder: 15 builtin-*.md schema-table files (4.76-5.80 KB).

Anchor canon: L4-AG.1a.9 (chr() для triple-mojibake, _normalize чистит mojibake-BOM).

Mojibake-аудит EN:
  - triple-apos `'` (U+2019, c3 a2 c2 80 c2 99) только в:
      rum-mobile-enablement (`application's`, `there's`),
      process-custom-process-monitoring-rule (`don't`).
  - mojibake-BOM `ï»¿` есть в нескольких файлах внутри hyperlink-текстов, чистится _normalize.
  - Никаких single-â, double-B, triple-en-dash, triple-nbhyphen, WARN.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-rum-mobile-enablement.md",
    "builtin-rum-web-app-detection.md",
    "builtin-rum-web-manual-insertion.md",
    "builtin-monitoredentities-generic-relation.md",
    "builtin-rpc-based-sampling.md",
    "builtin-opentelemetry-metrics.md",
    "builtin-url-based-sampling.md",
    "builtin-deployment-management-update-windows.md",
    "builtin-process-custom-process-monitoring-rule.md",
    "builtin-failure-detection-service-general-parameters.md",
    "builtin-appsec-runtime-vulnerability-detection.md",
    "builtin-anomaly-detection-kubernetes-cluster.md",
    "builtin-sessionreplay-web-privacy-preferences.md",
    "builtin-process-group-advanced-detection-rule.md",
    "builtin-anomaly-detection-infrastructure-disks-per-disk-override.md",
]

# Triple-mojibake apostrophe `'` (U+2019): bytes c3 a2 c2 80 c2 99, 3 chars
TM = chr(0xE2) + chr(0x80) + chr(0x99)

DISPLAY_NAME = {
    "Enablement and cost control": "Включение и контроль затрат",
    "Application detection": "Обнаружение приложений",
    "Manual insertion": "Ручная вставка",
    "Generic relationships": "Универсальные связи",
    "Trace sampling for RPC requests": "Trace sampling для RPC-запросов",
    "OpenTelemetry metrics": "OpenTelemetry-метрики",
    "Trace sampling for HTTP requests": "Trace sampling для HTTP-запросов",
    "Update windows for OneAgent updates": "Окна обновления для OneAgent",
    "Custom process monitoring rules": "Пользовательские правила мониторинга процессов",
    "General failure detection parameters": "Общие параметры failure detection",
    "Vulnerability Analytics: General settings": "Vulnerability Analytics: общие параметры",
    "Kubernetes cluster anomaly detection": "Обнаружение аномалий Kubernetes-кластера",
    "Session replay data privacy": "Приватность данных Session Replay",
    "Advanced detection rules": "Расширенные правила обнаружения",
    "Anomaly detection for infrastructure": "Обнаружение аномалий инфраструктуры",
}

SCHEMA_DESC = {
    # 1. rum-mobile-enablement — SCHEMA_DESC уже переведён в L4-AG.1a.9
    "Turn on Real User Monitoring and Session Replay. Configure cost and traffic control settings.": "Включите Real User Monitoring и Session Replay. Настройте параметры контроля затрат и трафика.",
    # 2. rum-web-app-detection — большой блок с примерами URL-правил
    "Define new applications for Real User Monitoring (RUM) using [application detection rules](https://dt-url.net/wb3f0pfr), check how your existing rules map to your applications.": "Задайте новые приложения для Real User Monitoring (RUM) с помощью [application detection rules](https://dt-url.net/wb3f0pfr), проверьте, как существующие правила соотносятся с вашими приложениями.",
    "By default, Dynatrace associates all your monitoring data with a placeholder application (`<your-dynatrace-url>//#uemapplications/uemappmetrics;uemapplicationId=APPLICATION-EA7C4B59F27D43EB`). Define your own detection rules for grouping your monitoring data into distinct applications in Dynatrace.": "По умолчанию Dynatrace связывает все данные мониторинга с приложением-placeholder (`<your-dynatrace-url>//#uemapplications/uemappmetrics;uemapplicationId=APPLICATION-EA7C4B59F27D43EB`). Задайте собственные правила обнаружения, чтобы группировать данные мониторинга в отдельные приложения Dynatrace.",
    "If you haven't done so already, deploy OneAgent (`<your-dynatrace-url>//#install`). After the deployment [RUM](https://dt-url.net/1n2b0prq) is enabled by default for all web applications that are auto-detected by OneAgent. OneAgent [automatically injects](https://dt-url.net/kp5f0p5z) a JavaScript code snippet into the HTML of all the pages of your monitored web applications so that it can capture monitoring data and ensure end-to-end monitoring visibility.": "Если ещё не сделали этого, разверните OneAgent (`<your-dynatrace-url>//#install`). После развёртывания [RUM](https://dt-url.net/1n2b0prq) включается по умолчанию для всех web-приложений, автоматически обнаруженных OneAgent. OneAgent [автоматически инжектит](https://dt-url.net/kp5f0p5z) JavaScript-сниппет в HTML всех страниц мониторимых web-приложений, чтобы захватывать данные мониторинга и обеспечивать end-to-end видимость.",
    "* Rules are applied sequentially, with rules at the top taking priority over lower rules.": "* Правила применяются последовательно, причём верхние правила имеют приоритет над нижними.",
    "* [Not seeing your applications or RUM data?](https://dt-url.net/kl2a0pm4)": "* [Не видите своих приложений или RUM-данных?](https://dt-url.net/kl2a0pm4)",
    "* More details on [defining your web application](https://dt-url.net/r63b0pgq).": "* Подробнее об [определении вашего web-приложения](https://dt-url.net/r63b0pgq).",
    "Given a set of URLs:": "Для следующего набора URL:",
    "The rule *Domain (host) contains* **mybook** matches against:": "Правило *Domain (host) contains* **mybook** совпадает с:",
    "The rule *Domain (host) ends with* **shop.com** matches against:": "Правило *Domain (host) ends with* **shop.com** совпадает с:",
    "The rule *Domain (host) equals* **www.mybookshop.com** matches against:": "Правило *Domain (host) equals* **www.mybookshop.com** совпадает с:",
    "The rule *Domain (host) matches* **mybookshop.com** matches against:": "Правило *Domain (host) matches* **mybookshop.com** совпадает с:",
    "The rule *Domain (host) starts with* **checkout** matches against:": "Правило *Domain (host) starts with* **checkout** совпадает с:",
    "The rule *URL contains* **mybookshop.com/about** matches against:": "Правило *URL contains* **mybookshop.com/about** совпадает с:",
    "The rule *URL ends with* **about/index.php** matches against:": "Правило *URL ends with* **about/index.php** совпадает с:",
    "The rule *URL equals* **http://www.mybookshop.com/about** matches against:": "Правило *URL equals* **http://www.mybookshop.com/about** совпадает с:",
    "The rule *URL starts with* **http://www.mybookshop.com** matches against:": "Правило *URL starts with* **http://www.mybookshop.com** совпадает с:",
    # 3. rum-web-manual-insertion
    "Manually insert one of the snippet formats below into the pages of your application. Learn more about the different [snippet formats](https://dt-url.net/vx5g0ptn). All formats are also available via the [API](https://dt-url.net/oz43wab), allowing you to automate their insertion as part of your build process.": "Вручную вставьте один из приведённых ниже форматов сниппета на страницы вашего приложения. Подробнее о разных [snippet formats](https://dt-url.net/vx5g0ptn). Все форматы также доступны через [API](https://dt-url.net/oz43wab), что позволяет автоматизировать их вставку в рамках процесса сборки.",
    # 4. monitoredentities-generic-relation (2 paragraphs)
    'Looking for topology extraction support? Find the [topology model](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center") help page here.': 'Ищете поддержку извлечения топологии? См. страницу помощи [topology model](https://www.dynatrace.com/support/help/shortlink/topology-model#custom-topology-model "Visit Dynatrace support center").',
    "Entity types can be related to each other. The relationship registry contains rules by which relationships between related entities are automatically established.": "Типы сущностей могут быть связаны между собой. Реестр связей содержит правила, по которым связи между связанными сущностями устанавливаются автоматически.",
    # 5. rpc-based-sampling (2 paragraphs)
    "This setting allows you to configure how OneAgent treats specific Remote Procedure Calls (RPCs) when sampling is needed. More precisely, you can advise OneAgent on the importance of specific RPCs in relation to other RPCs. RPCs with higher importance will be treated to be captured more often and vice versa. Additionally, you can turn off tracing for specific RPCs completely. Full-Stack Monitoring includes a defined amount of trace data volume. Every contributing GiB of host or application memory adds a certain amount of trace volume ingest rate to your environment. Depending on that transaction volume, OneAgent captures end-to-end traces every minute up to a peak trace volume. Adaptive Traffic management automatically adjusts the sampling rate of trace data collection so that the collected trace data doesn't exceed the included trace volume. You can learn more about this [here](https://dt-url.net/na03wq0)": "Этот параметр позволяет настроить, как OneAgent обрабатывает конкретные Remote Procedure Calls (RPC), когда требуется sampling. Точнее, вы можете указать OneAgent важность конкретных RPC относительно других RPC. RPC с более высокой важностью будут чаще захватываться, и наоборот. Дополнительно можно полностью отключить трассировку для конкретных RPC. Full-Stack Monitoring включает заданный объём данных трейсов. Каждый учитываемый ГиБ памяти хоста или приложения добавляет в ваше окружение определённый объём ingest rate трейсов. В зависимости от объёма транзакций OneAgent захватывает end-to-end трейсы каждую минуту вплоть до пикового объёма. Adaptive Traffic management автоматически подстраивает sampling rate сбора трейсов так, чтобы собранные данные не превышали включённый объём. Подробнее об этом см. [здесь](https://dt-url.net/na03wq0)",
    'This configuration represents an ordered list of rules. Each rule has conditions, based on protocol, remote operation name, remote service name or endpoint name of the RPC. The first rule where all conditions are met will be applied. Each non-matching rule adds an overhead of a microsecond to the monitored process. All string comparisons of the conditions are case sensitive. Use the switch in the "Enabled" column to turn a rule on or off.': 'Эта конфигурация представляет собой упорядоченный список правил. У каждого правила есть условия по протоколу, имени удалённой операции, имени удалённого сервиса или имени эндпоинта RPC. Применяется первое правило, у которого выполнены все условия. Каждое несработавшее правило добавляет накладные расходы в одну микросекунду на мониторимый процесс. Все строковые сравнения условий чувствительны к регистру. Используйте переключатель в колонке "Enabled", чтобы включать или выключать правило.',
    # 6. opentelemetry-metrics
    "Configure how OpenTelemetry metrics are ingested into Dynatrace via the OTLP endpoint.": "Настройте, как OpenTelemetry-метрики поступают в Dynatrace через OTLP-эндпоинт.",
    "**Notes:**": "**Примечания:**",
    "* Changes made to these settings only apply to newly ingested data points. Data points that are already stored in Dynatrace will not change.": "* Изменения этих параметров применяются только к новым ingested data points. Уже сохранённые в Dynatrace data points не изменятся.",
    "* Changes made to these settings may have an impact on existing dashboards, events and alerts that use dimensions configured here. In this case, they will need to be updated manually.": "* Изменения могут повлиять на существующие дашборды, события и оповещения, использующие настроенные здесь dimensions. В этом случае их нужно обновить вручную.",
    "* Settings marked with `(Metrics Classic)` have no effect in Metrics powered by Grail. For Metrics powered by Grail all attributes (resource, scope and metric) are accepted by default. Use the block-list if you want to avoid ingesting certain attributes.": "* Параметры с пометкой `(Metrics Classic)` не действуют в Metrics powered by Grail. Для Metrics powered by Grail все атрибуты (resource, scope и metric) принимаются по умолчанию. Используйте block-list, если хотите исключить ingest определённых атрибутов.",
    "* For OpenTelemetry trace/span settings, navigate to: **Settings** > **Server-side service monitoring**.": "* Параметры OpenTelemetry trace/span находятся в: **Settings** > **Server-side service monitoring**.",
    # 7. url-based-sampling (3 paragraphs)
    "This setting allows you to configure how OneAgent treats specific HTTP requests when sampling is needed. More precisely, you can advise OneAgent on the importance of specific HTTP requests in relation to other HTTP requests. HTTP requests with the URL with higher importance will be treated to be captured more often and vice versa. Additionally, you can turn off tracing for specific HTTP requests completely. Full-Stack Monitoring includes a defined amount of trace data volume. Every contributing GiB of host or application memory adds a certain amount of trace volume ingest rate to your environment. Depending on that transaction volume, OneAgent captures end-to-end traces every minute up to a peak trace volume. Adaptive Traffic management automatically adjusts the sampling rate of trace data collection so that the collected trace data doesn't exceed the included trace volume. You can learn more about this [here](https://dt-url.net/2y23wt3)": "Этот параметр позволяет настроить, как OneAgent обрабатывает конкретные HTTP-запросы, когда требуется sampling. Точнее, вы можете указать OneAgent важность конкретных HTTP-запросов относительно других. HTTP-запросы по URL с большей важностью будут чаще захватываться, и наоборот. Дополнительно можно полностью отключить трассировку для конкретных HTTP-запросов. Full-Stack Monitoring включает заданный объём данных трейсов. Каждый учитываемый ГиБ памяти хоста или приложения добавляет в ваше окружение определённый объём ingest rate трейсов. В зависимости от объёма транзакций OneAgent захватывает end-to-end трейсы каждую минуту вплоть до пикового объёма. Adaptive Traffic management автоматически подстраивает sampling rate сбора трейсов так, чтобы собранные данные не превышали включённый объём. Подробнее об этом см. [здесь](https://dt-url.net/2y23wt3)",
    "Hint: Use this Multi-dimensional analysis (`<your-dynatrace-url>//ui/diagnostictools/mda?mdaId=atm`) to get an overview over the current sample rates per URL. Additionally use the context-menu of the URLs to up- or downscale certain URLs in a convenient way.": "Подсказка: используйте Multi-dimensional analysis (`<your-dynatrace-url>//ui/diagnostictools/mda?mdaId=atm`) для обзора текущих sample rate по URL. Дополнительно используйте контекстное меню URL для удобного повышения или понижения масштаба отдельных URL.",
    "This configuration represents an ordered list of rules. Each rule has conditions, based on request method, the URL path and query parameters. The first rule where all conditions are met will be applied. Each non-matching rule adds an overhead of a microsecond to the monitored process. All string comparisons of the conditions are case sensitive. Use the Enabled switch to turn a rule on or off.": "Эта конфигурация представляет собой упорядоченный список правил. У каждого правила есть условия по методу запроса, URL-пути и query-параметрам. Применяется первое правило, у которого выполнены все условия. Каждое несработавшее правило добавляет накладные расходы в одну микросекунду на мониторимый процесс. Все строковые сравнения условий чувствительны к регистру. Используйте переключатель Enabled, чтобы включать или выключать правило.",
    # 8. deployment-management-update-windows
    "Define update windows for how often and when to update your OneAgent instances. You will be able to apply these windows to OneAgents, Host Groups or your whole Environment in Automatic Update settings screens.": "Задайте окна обновления: как часто и когда обновлять instances OneAgent. Вы сможете применить эти окна к OneAgents, Host Groups или ко всему Environment в экранах настроек Automatic Update.",
    # 9. process-custom-process-monitoring-rule (2 paragraphs, second with triple-apos)
    "Dynatrace OneAgent automatically monitors all process groups detected in your environment (processes running during OneAgent installation must be restarted to initiate monitoring).": "Dynatrace OneAgent автоматически мониторит все process groups, обнаруженные в вашем окружении (процессы, работающие во время установки OneAgent, должны быть перезапущены, чтобы запустить мониторинг).",
    "OneAgent additionally provides deep monitoring for all processes that it can monitor at the request- and PurePath levels. Define process monitoring rules below if you don"
    + TM
    + "t want to monitor all your processes automatically, or if you need to define an exception for specific processes.": "OneAgent дополнительно обеспечивает глубокий мониторинг для всех процессов, которые он может мониторить на уровнях request и PurePath. Задайте правила мониторинга процессов ниже, если не хотите автоматически мониторить все процессы или нужно задать исключение для конкретных процессов.",
    # 10. failure-detection-service-general-parameters
    "Dynatrace failure detection automatically detects the vast majority of error conditions in your environment. However, detected service errors don't necessarily mean that the underlying requests have failed. There may be cases where the default service failure detection settings don't meet your particular needs. In such cases, you can configure the settings provided below. Please note that these settings are not applicable to services of type 'Span service'. For complete details, see [configure service failure detection](https://dt-url.net/ys5k0p4y).": "Dynatrace failure detection автоматически обнаруживает подавляющее большинство ошибочных состояний в вашем окружении. Однако обнаруженные ошибки сервиса не обязательно означают, что нижележащие запросы провалились. Бывают случаи, когда настройки failure detection по умолчанию не подходят под ваши потребности. В таких случаях можно настроить приведённые ниже параметры. Учтите, что эти настройки не применимы к сервисам типа 'Span service'. Подробнее см. [configure service failure detection](https://dt-url.net/ys5k0p4y).",
    # 11. appsec-runtime-vulnerability-detection
    "Automated [Runtime Vulnerability Analytics](https://dt-url.net/c010iio) helps you quickly and completely understand each detected vulnerability in your environment and how to remediate it, allowing you to prioritize which vulnerabilities to fix first. Note: Enabling Third-party or Code-level Vulnerability Analytics consumes Application Security units. For details, see the [Application Security Monitoring documentation](https://dt-url.net/wq031ql).": "Автоматизированная [Runtime Vulnerability Analytics](https://dt-url.net/c010iio) помогает быстро и полно понимать каждую обнаруженную уязвимость в вашем окружении и способы её устранения, позволяя приоритизировать порядок исправления. Примечание: включение Third-party или Code-level Vulnerability Analytics расходует Application Security units. Подробнее см. в [Application Security Monitoring documentation](https://dt-url.net/wq031ql).",
    # 12. anomaly-detection-kubernetes-cluster
    "Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes cluster. Changing thresholds resets the observation period. Additional information can be found on our [documentation page](https://dt-url.net/wq02okj#cluster).": "Dynatrace автоматически обнаруживает широкий спектр типичных Kubernetes-проблем. Используйте эти параметры для настройки оповещений по вашему Kubernetes-кластеру. Изменение порогов сбрасывает observation period. Дополнительные сведения см. на нашей [странице документации](https://dt-url.net/wq02okj#cluster).",
    # 13. sessionreplay-web-privacy-preferences
    "[Configure Session Replay](https://dt-url.net/2i3t0pju) to restrict data capture and protect your end users' data privacy.": "[Configure Session Replay](https://dt-url.net/2i3t0pju), чтобы ограничить сбор данных и защитить приватность данных конечных пользователей.",
    # 14. process-group-advanced-detection-rule (4 paragraphs)
    "Advanced process group detection rules enable you to adapt the detection logic for deep monitored processes by **leveraging properties that are automatically detected** by OneAgent during the startup of a process.": "Расширенные правила обнаружения process group позволяют адаптировать логику обнаружения для глубоко мониторимых процессов, **используя свойства, которые автоматически обнаруживаются** OneAgent при запуске процесса.",
    "Advanced detection rules are capable to extract additional process group and instance identifier from processes to fine tune the automatic detection logic of OneAgent. [More about custom process-group detection](https://dt-url.net/1722wrz)": "Расширенные правила обнаружения могут извлекать дополнительные идентификаторы process group и instance из процессов, чтобы точно настроить логику автоматического обнаружения OneAgent. [Подробнее о custom process-group detection](https://dt-url.net/1722wrz)",
    'Note: Detection rules change the composition, makeup, and identity of a process group, not just the name. If you only need to change default name use the naming rules (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`) instead.': 'Примечание: правила обнаружения меняют состав, структуру и identity процесс-группы, не только имя. Если нужно изменить только имя по умолчанию, используйте вместо этого naming rules (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`).',
    "Process-group detection rules only affect processes that are deep monitored by the Dynatrace OneAgent and require a restart of your processes to affect how processes are identified and grouped.": "Правила обнаружения process group влияют только на процессы, глубоко мониторимые Dynatrace OneAgent, и требуют перезапуска процессов, чтобы изменение в идентификации и группировке вступило в силу.",
    # 15. anomaly-detection-infrastructure-disks-per-disk-override
    "Dynatrace automatically detects infrastructure-related performance anomalies such as high CPU saturation, memory outages, and low disk-space conditions. Use these settings to configure detection sensitivity, set alert thresholds, or disable alerting for infrastructure components.": "Dynatrace автоматически обнаруживает связанные с инфраструктурой аномалии производительности, например высокую нагрузку CPU, нехватку памяти и нехватку дискового пространства. Используйте эти параметры для настройки чувствительности обнаружения, задания порогов оповещений или отключения оповещений для компонентов инфраструктуры.",
}


PARAM_LABEL = {
    # Shared
    "Enabled": "Включено",
    "Active": "Активно",
    "Name": "Имя",
    "Description": "Описание",
    "Value": "Значение",
    "Values": "Значения",
    "Operator": "Оператор",
    "Tags": "Теги",
    "Comment": "Комментарий",
    "On/Off": "Вкл./Выкл.",
    "Pattern": "Шаблон",
    "Mode": "Режим",
    "Condition": "Условие",
    "Start": "Начало",
    "End": "Конец",
    "Property": "Свойство",
    # 1. rum-mobile-enablement
    "Real User Monitoring": "Real User Monitoring",
    "Session Replay": "Session Replay",
    "User Interactions": "User Interactions",
    "Enable Real User Monitoring Classic": "Включить Real User Monitoring Classic",
    "Enable New Real User Monitoring Experience": "Включить новый опыт Real User Monitoring",
    "Cost and traffic control": "Контроль затрат и трафика",
    "Enable Session Replay Classic": "Включить Session Replay Classic",
    "Enable New Session Replay Experience": "Включить новый опыт Session Replay",
    "Enable Session Replay Classic on crashes": "Включить Session Replay Classic при сбоях",
    "Enable New Session Replay on Crashes Experience": "Включить новый опыт Session Replay при сбоях",
    "Enable User Interactions": "Включить User Interactions",
    # 2. rum-web-app-detection
    "Matcher": "Сопоставитель",
    "Application": "Приложение",
    # 3. rum-web-manual-insertion
    "Javascript tag": "Javascript-тег",
    "OneAgent JavaScript Tag": "OneAgent JavaScript-тег",
    "OneAgent JavaScript Tag with SRI": "OneAgent JavaScript-тег с SRI",
    "Code Snippet": "Code Snippet",
    "Cache monitoring code and configuration for": "Кэшировать monitoring-код и конфигурацию на",
    "Script execution attribute": "Атрибут выполнения скрипта",
    "Add crossorigin=anonymous attribute": "Добавить атрибут crossorigin=anonymous",
    "Load the monitoring code": "Загружать monitoring-код",
    # 4. monitoredentities-generic-relation
    "Source filters": "Source-фильтры",
    "Created by": "Кем создано",
    "Source type name": "Имя source type",
    "Role of source type": "Роль source type",
    "Type of relationship": "Тип связи",
    "Destination type": "Destination type",
    "Role of destination type": "Роль destination type",
    "Datasource type": "Тип источника данных",
    "Mapping Rules": "Mapping rules",
    "Source property": "Source-свойство",
    "Source Normalization": "Нормализация source",
    "Destination property": "Destination-свойство",
    "Destination Normalization": "Нормализация destination",
    # 5+7. rpc-based-sampling / url-based-sampling (shared)
    "Disable tracing for matching RPC requests": "Отключить трассировку для совпавших RPC-запросов",
    "Importance of the RPC": "Важность RPC",
    "Protocol": "Протокол",
    "Remote operation name": "Имя удалённой операции",
    "Remote operation name comparison condition": "Условие сравнения имени удалённой операции",
    "Remote service name": "Имя удалённого сервиса",
    "Remote service name comparison condition": "Условие сравнения имени удалённого сервиса",
    "Endpoint name": "Имя эндпоинта",
    "Endpoint name comparison condition": "Условие сравнения имени эндпоинта",
    "Disable tracing for matching HTTP requests": "Отключить трассировку для совпавших HTTP-запросов",
    "Importance of the specific URL": "Важность конкретного URL",
    "Path of the URL": "URL-путь",
    "Path comparison condition": "Условие сравнения пути",
    "Query parameters": "Query-параметры",
    "Any HTTP method": "Любой HTTP-метод",
    "HTTP method": "HTTP-метод",
    "Query parameter name": "Имя query-параметра",
    "Query parameter value": "Значение query-параметра",
    "Query parameter value is undefined": "Значение query-параметра не определено",
    # 6. opentelemetry-metrics
    "Add Meter name and version as metric dimensions (Metrics Classic)": "Добавить имя и версию Meter как dimensions метрики (Metrics Classic)",
    "Advanced OTLP metric dimensions": "Расширенные OTLP-dimensions метрики",
    "Add the resource and scope attributes configured below as dimensions (Metrics Classic)": "Добавить настроенные ниже атрибуты resource и scope как dimensions (Metrics Classic)",
    "Attribute key": "Ключ атрибута",
    # 8. deployment-management-update-windows
    "Recurrence": "Периодичность",
    "Update time": "Время обновления",
    "Every X days": "Каждые X дней",
    "Recurrence range": "Диапазон периодичности",
    "Day of the week": "День недели",
    "Every X weeks": "Каждые X недель",
    "Day of the month": "День месяца",
    "Every X months": "Каждые X месяцев",
    "Start time (24-hour clock)": "Время начала (24-часовой формат)",
    "Time zone": "Часовой пояс",
    "Duration (minutes)": "Длительность (минуты)",
    "Monday": "Понедельник",
    "Tuesday": "Вторник",
    "Wednesday": "Среда",
    "Thursday": "Четверг",
    "Friday": "Пятница",
    "Saturday": "Суббота",
    "Sunday": "Воскресенье",
    # 9. process-custom-process-monitoring-rule
    "Condition target": "Цель условия",
    "Environment variable key": "Ключ переменной окружения",
    "Condition operator": "Оператор условия",
    "Condition value": "Значение условия",
    # 10. failure-detection-service-general-parameters
    "Override global failure detection settings": "Переопределить глобальные параметры failure detection",
    "Customize failure detection for specific exceptions and errors": "Настроить failure detection для конкретных исключений и ошибок",
    "Ignore all exceptions": "Игнорировать все исключения",
    "Success forcing exceptions": "Исключения, форсирующие успех",
    "Ignored exceptions": "Игнорируемые исключения",
    "Custom handled exceptions": "Пользовательские обработанные исключения",
    "Custom error rules": "Пользовательские правила ошибок",
    "Ignore span failure detection": "Игнорировать span failure detection",
    "Class pattern": "Шаблон класса",
    "Exception message pattern": "Шаблон сообщения исключения",
    "Request attribute": "Request attribute",
    "Request attribute condition": "Условие request attribute",
    "Apply this comparison": "Применять это сравнение",
    "Case sensitive": "Чувствительно к регистру",
    # 11. appsec-runtime-vulnerability-detection
    "Enable Third-party Vulnerability Analytics": "Включить Third-party Vulnerability Analytics",
    "Enable new monitoring rules": "Включить новые правила мониторинга",
    "Global third-party vulnerability detection control": "Глобальное управление third-party vulnerability detection",
    "Technologies": "Технологии",
    "Enable Code-level Vulnerability Analytics": "Включить Code-level Vulnerability Analytics",
    "Global Java code-level vulnerability detection control": "Глобальное управление Java code-level vulnerability detection",
    "Global .NET code-level vulnerability detection control": "Глобальное управление .NET code-level vulnerability detection",
    "Global Go code-level vulnerability detection control": "Глобальное управление Go code-level vulnerability detection",
    ".NET": ".NET",
    ".NET runtimes": ".NET runtimes",
    "Go": "Go",
    "Java": "Java",
    "Java runtimes": "Java runtimes",
    "Kubernetes": "Kubernetes",
    "Node.js": "Node.js",
    "Node.js runtimes": "Node.js runtimes",
    "Python": "Python",
    "Python runtimes": "Python runtimes",
    "PHP": "PHP",
    # 12. anomaly-detection-kubernetes-cluster
    "Detect cluster readiness issues": "Обнаруживать проблемы readiness кластера",
    "Detect cluster CPU-request saturation": "Обнаруживать насыщение CPU-request кластера",
    "Detect cluster memory-request saturation": "Обнаруживать насыщение memory-request кластера",
    "Detect cluster pod-saturation": "Обнаруживать насыщение по подам кластера",
    "Detect monitoring issues": "Обнаруживать проблемы мониторинга",
    "cluster is not ready for at least": "кластер не готов в течение как минимум",
    "within the last": "за последние",
    "amount of requested CPU is above": "объём запрошенного CPU превышает",
    "of cluster CPU capacity for at least": "от ёмкости CPU кластера в течение как минимум",
    "amount of requested memory is above": "объём запрошенной памяти превышает",
    "of cluster memory capacity for at least": "от ёмкости памяти кластера в течение как минимум",
    "number of running pods is higher than": "число работающих подов превышает",
    "of schedulable pod capacity for at least": "от ёмкости schedulable подов в течение как минимум",
    "monitoring is not available for at least": "мониторинг недоступен в течение как минимум",
    # 13. sessionreplay-web-privacy-preferences
    "Enable opt-in mode for Session Replay": "Включить opt-in режим для Session Replay",
    "URL exclusion": "URL exclusion",
    "Content masking preferences": "Параметры маскирования контента",
    "Recording masking settings": "Параметры маскирования при записи",
    "Allow list rules": "Правила allow list",
    "Block list rules": "Правила block list",
    "Playback masking settings": "Параметры маскирования при воспроизведении",
    "Target": "Цель",
    "CSS selector to identify the content element": "CSS-селектор для идентификации элемента контента",
    "Attribute name (expression)": "Имя атрибута (выражение)",
    "Hide user interaction": "Скрыть пользовательское взаимодействие",
    # 14. process-group-advanced-detection-rule
    "Process group detection": "Обнаружение process group",
    "Process group extraction": "Извлечение process group",
    "Process instance extraction": "Извлечение process instance",
    "Contained string": "Содержащаяся строка",
    "Restrict this rule to specific process types.": "Ограничить это правило конкретными типами процессов.",
    "Standalone rule": "Самостоятельное правило",
    "Delimit from": "Разделитель с",
    "Delimit to": "Разделитель до",
    "Ignore numbers": "Игнорировать числа",
    # 15. anomaly-detection-infrastructure-disks-per-disk-override
    "Override low disk space detection settings": "Переопределить параметры обнаружения нехватки дискового пространства",
    "Override slow writes and reads detection settings": "Переопределить параметры обнаружения медленных операций записи и чтения",
    "Override low inodes detection settings": "Переопределить параметры обнаружения нехватки inodes",
    "Detect low disk space": "Обнаруживать нехватку дискового пространства",
    "Detection mode for low disk space": "Режим обнаружения нехватки дискового пространства",
    "Detect slow-running disks": "Обнаруживать медленно работающие диски",
    "Detection mode for slow running disks": "Режим обнаружения медленных дисков",
    "Detect low inodes number available": "Обнаруживать нехватку доступных inodes",
    "Detection mode for low inodes number available": "Режим обнаружения нехватки доступных inodes",
    "Alert if free disk space is lower than this percentage in 3 out of 5 samples": "Оповещать, если свободного дискового пространства меньше этого процента в 3 из 5 замеров",
    "Alert if disk read time or write time is higher than this threshold in 3 out of 5 samples": "Оповещать, если время чтения или записи диска превышает порог в 3 из 5 замеров",
    "Alert if the percentage of available inodes is lower than this threshold in 3 out of 5 samples": "Оповещать, если процент доступных inodes ниже порога в 3 из 5 замеров",
}


PARAM_DESC = {
    # 1. rum-mobile-enablement
    "Capture and analyze all user actions within your application. Enable [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq) to monitor and improve your application's performance, identify errors, and gain insight into your user's behavior and experience.": "Захватывает и анализирует все user actions внутри вашего приложения. Включите [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq), чтобы мониторить и улучшать производительность приложения, выявлять ошибки и получать инсайты в поведение и опыт пользователей.",
    "[Session Replay](https://dt-url.net/session-replay) captures all user interactions within your application and replays them in a movie-like experience while providing [best-in-class security and data protection](https://dt-url.net/b303zxj).": "[Session Replay](https://dt-url.net/session-replay) захватывает все пользовательские взаимодействия внутри приложения и воспроизводит их как фильм, обеспечивая при этом [best-in-class безопасность и защиту данных](https://dt-url.net/b303zxj).",
    "Please be aware that only mobile agents with version **8.309 or higher** can ingest Grail events": "Учтите, что отправлять Grail-события могут только mobile agents версии **8.309 или выше**",
    "Percentage of user sessions captured and analyzed  By default, Dynatrace captures all user actions and user sessions for analysis. This approach ensures complete insight into your application"
    + TM
    + "s performance and customer experience. You can optionally reduce the granularity of user-action and user-session analysis by capturing a lower percentage of user sessions. While this approach can reduce monitoring costs, it also results in lower visibility into how your customers are using your applications. For example, a setting of 10% results in Dynatrace analyzing only every tenth user session.": "Процент захватываемых и анализируемых user-сессий.  По умолчанию Dynatrace захватывает все user actions и user-сессии для анализа. Такой подход обеспечивает полную видимость производительности приложения и customer experience. По желанию можно снизить гранулярность анализа user-action и user-сессий, захватывая меньший процент сессий. Это уменьшает стоимость мониторинга, но также снижает видимость того, как клиенты пользуются приложениями. Например, значение 10% означает, что Dynatrace анализирует только каждую десятую user-сессию.",
    "Before enabling, Dynatrace checks your system against the [prerequisites for Session Replay](https://dt-url.net/t23s0ppi).": "До включения Dynatrace проверяет вашу систему на соответствие [предварительным требованиям Session Replay](https://dt-url.net/t23s0ppi).",
    "Percentage of user sessions recorded with Session Replay. For example, if you have 50% for RUM and 50% for Session Replay, it results in 25% of sessions recorded with Session Replay.": "Процент user-сессий, записываемых через Session Replay. Например, при 50% для RUM и 50% для Session Replay в итоге через Session Replay записывается 25% сессий.",
    "Capture screen recordings that replay the user actions preceding all detected crashes. Before enabling, Dynatrace checks your system against the [prerequisites for Session Replay](https://dt-url.net/t23s0ppi).": "Захватывать записи экрана, воспроизводящие user actions перед всеми обнаруженными сбоями. До включения Dynatrace проверяет вашу систему на соответствие [предварительным требованиям Session Replay](https://dt-url.net/t23s0ppi).",
    "Capture user interactions within your frontend, including all clicks and taps. During the Early Access period, there"
    + TM
    + "s no cost associated with this feature.": "Захватывать пользовательские взаимодействия во frontend, включая все clicks и taps. В период Early Access эта функция бесплатна.",
    # 2. rum-web-app-detection
    "Select an existing application or create a new one.": "Выберите существующее приложение или создайте новое.",
    "Add a description for your rule": "Добавьте описание для вашего правила",
    # 3. rum-web-manual-insertion
    "JavaScript tag references an external file containing monitoring code and configuration. Due to its dynamic update mechanism, it is recommended for most use cases.": "JavaScript-тег ссылается на внешний файл с monitoring-кодом и конфигурацией. Благодаря механизму динамического обновления он рекомендуется для большинства случаев.",
    "OneAgent JavaScript tag includes configuration and a reference to an external file containing the monitoring code. It needs to be updated after configuration changes and monitoring code updates.": "OneAgent JavaScript-тег содержит конфигурацию и ссылку на внешний файл с monitoring-кодом. Его нужно обновлять после изменений конфигурации и обновлений monitoring-кода.",
    "OneAgent JavaScript tag with SRI includes configuration, a reference to an external file containing the monitoring code, and a hash that allows the browser to verify the integrity of the monitoring code before executing it. It needs to be updated after configuration changes and monitoring code updates.": "OneAgent JavaScript-тег с SRI содержит конфигурацию, ссылку на внешний файл с monitoring-кодом и хеш, позволяющий браузеру проверить целостность monitoring-кода до его выполнения. Его нужно обновлять после изменений конфигурации и обновлений monitoring-кода.",
    "Code snippet is a piece of inline code that implements basic functionality and loads the full functionality either synchronously or deferred. Even though it implements an update mechanism, regular updates are still required to guarantee compatibility.": "Code snippet, это фрагмент inline-кода, реализующий базовый функционал и загружающий полный функционал синхронно или отложенно. Даже несмотря на встроенный механизм обновлений, регулярные обновления нужны для гарантии совместимости.",
    "Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability.  Add the `defer` attribute to execute the monitoring code after the page has finished parsing.": "Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его сразу по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы.",
    "Add the `crossorigin=anonymous` attribute to capture JavaScript error messages and W3C resource timings": "Добавьте атрибут `crossorigin=anonymous`, чтобы захватывать сообщения JavaScript-ошибок и W3C resource timings",
    "Add the `async` attribute to download the monitoring code in parallel with parsing the page, and execute it immediately upon availability  Add the `defer` attribute to execute the monitoring code after the page has finished parsing": "Добавьте атрибут `async`, чтобы загружать monitoring-код параллельно с парсингом страницы и выполнять его сразу по доступности.  Добавьте атрибут `defer`, чтобы выполнять monitoring-код после завершения парсинга страницы",
    # 4. monitoredentities-generic-relation
    "Enables or disables the relationship": "Включает или выключает связь",
    "Specify all sources which should be evaluated for this relationship rule. The relationship is only created when any of the filters match.": "Укажите все источники, которые должны проверяться для этого правила связи. Связь создаётся только когда совпал любой из фильтров.",
    "The user or extension that created this relationship.": "Пользователь или расширение, создавшие эту связь.",
    "Define an entity type as the source of the relationship.": "Задайте тип сущности как источник связи.",
    "Specify a role for the source entity. If both source and destination type are the same, referring different roles will allow identification of a relationships direction. If role is left blank, any role of the source type is considered for the relationship.": "Укажите роль для source-сущности. Если source и destination имеют одинаковый тип, разные роли позволяют идентифицировать направление связи. Если роль не задана, для связи учитывается любая роль source type.",
    "Type of the relationship between the Source Type and the Destination Type": "Тип связи между Source Type и Destination Type",
    "Define an entity type as the destination of the relationship. You can choose the same type as the source type. In this case you also may assign different roles for source and destination for having directed relationships.": "Задайте тип сущности как destination связи. Можно выбрать тот же тип, что и source. В этом случае также можно назначить разные роли для source и destination, чтобы получить направленные связи.",
    "Specify a role for the destination entity. If both source and destination type are the same, referring different roles will allow identification of a relationships direction. If role is left blank, any role of the destination type is considered for the relationship.": "Укажите роль для destination-сущности. Если source и destination имеют одинаковый тип, разные роли позволяют идентифицировать направление связи. Если роль не задана, для связи учитывается любая роль destination type.",
    "Specify the source type of the filter to identify which data source should be evaluated.": "Укажите source type фильтра, чтобы определить, какой источник данных следует проверять.",
    "Specify a filter that needs to match in order for the extraction to happen.  Two different filters are supported: `$eq(value)` will ensure that the source matches exactly 'value', while `$prefix(value)` will ensure that the source begins with exactly 'value'. If your value contains the characters '(', ')' or '~', you need to escape them by adding a '~' in front of them.": "Задайте фильтр, который должен совпасть, чтобы произошло извлечение.  Поддерживаются два разных фильтра: `$eq(value)` гарантирует, что источник в точности равен 'value', а `$prefix(value)` гарантирует, что источник начинается ровно с 'value'. Если значение содержит символы '(', ')' или '~', экранируйте их, поставив '~' перед ними.",
    "Specify all properties which should be compared. If all mapping rules match a relationship between entities will be created.": "Укажите все свойства, которые должны сравниваться. Связь между сущностями создаётся, если совпадают все mapping rules.",
    "The case-sensitive name of a property of the source type.": "Чувствительное к регистру имя свойства source type.",
    "Normalize text or leave it as-is?": "Нормализовать текст или оставить как есть?",
    "The case-sensitive name of a property of the destination type.": "Чувствительное к регистру имя свойства destination type.",
    # 5+7. rpc-based-sampling / url-based-sampling (shared/twin)
    "No Traces will be captured for matching RPC requests. This applies always, even if Adaptive Traffic Management is inactive.": "Для совпавших RPC-запросов трейсы захватываться не будут. Это применяется всегда, даже когда Adaptive Traffic Management неактивен.",
    "Select the scaling factor for the current sampling rate of the system. Note, that the importance is only considered when sampling is needed.": "Выберите масштабирующий коэффициент для текущего sampling rate системы. Учтите, что важность принимается во внимание только когда требуется sampling.",
    "Specify the RPC protocol that can be used for RPC matching.": "Укажите RPC-протокол, который можно использовать для сопоставления RPC.",
    "Specify the RPC operation name. If the remote operation name is empty, either remote service name or endpoint name must be specified that can be used for RPC matching.": "Укажите имя RPC-операции. Если имя удалённой операции пустое, для сопоставления RPC должны быть указаны имя удалённого сервиса или имя эндпоинта.",
    "Specify the RPC remote service name. If the remote service name is empty, either remote operation name or endpoint name must be specified that can be used for RPC matching.": "Укажите имя удалённого сервиса RPC. Если имя удалённого сервиса пустое, для сопоставления RPC должны быть указаны имя удалённой операции или имя эндпоинта.",
    "Specify the RPC endpoint name. If the endpoint name is empty, either remote operation name or remote service name must be specified that can be used for RPC matching.": "Укажите имя эндпоинта RPC. Если имя эндпоинта пустое, для сопоставления RPC должны быть указаны имя удалённой операции или имя удалённого сервиса.",
    "No Traces will be captured for the matching HTTP requests. This applies always, even if Adaptive Traffic Management is inactive.": "Для совпавших HTTP-запросов трейсы захватываться не будут. Это применяется всегда, даже когда Adaptive Traffic Management неактивен.",
    "Specify the URL path without including any preceding or subsequent elements of the URL. You can use the wildcard '\\*\\*' between two path segments to ignore that part. If the path is empty, at least one query parameter must be specified that can be used for URL matching.": "Укажите URL-путь, не включая предшествующие или последующие элементы URL. Между двумя сегментами пути можно использовать wildcard '\\*\\*', чтобы пропустить эту часть. Если путь пустой, для сопоставления URL должен быть указан хотя бы один query-параметр.",
    "Add URL parameters in any order. **All** specified parameters must be present in the query of an URL to get a match.": "Добавьте URL-параметры в любом порядке. **Все** указанные параметры должны присутствовать в query URL для совпадения.",
    "The scaling factor for the matching URLs will be applied to any HTTP method.": "Масштабирующий коэффициент для совпавших URL применяется к любому HTTP-методу.",
    "The value must be equal for a match.": "Значение должно быть равно для совпадения.",
    "If enabled, the value is treated as undefined (/...&foo), otherwise as empty (/...&foo=).": "Если включено, значение трактуется как undefined (/...&foo), иначе как пустое (/...&foo=).",
    # 6. opentelemetry-metrics
    "When enabled, the Meter name (also referred to as InstrumentationScope or InstrumentationLibrary in OpenTelemetry SDKs) and version will be added as dimensions (`otel.scope.name` and `otel.scope.version`) to ingested OTLP metrics.": "Если включено, имя Meter (также называемое InstrumentationScope или InstrumentationLibrary в OpenTelemetry SDK) и версия будут добавлены как dimensions (`otel.scope.name` и `otel.scope.version`) к ingested OTLP-метрикам.",
    "Enable advanced OpenTelemetry metric capabilities with Grail, including primary field enrichment, flexible dimensions, enhanced routing, cost allocation, and support for high-cardinality queries. For more details about this and its effect on enrichment with the `dt.entity.service` dimension, please see [this post](https://dt-url.net/otlp-metrics-advanced).": "Включить расширенные возможности OpenTelemetry-метрик с Grail: обогащение primary field, гибкие dimensions, улучшенный routing, распределение затрат и поддержку запросов с high-cardinality. Подробнее об этом и о влиянии на обогащение dimension `dt.entity.service` см. [этот пост](https://dt-url.net/otlp-metrics-advanced).",
    'When enabled, the attributes defined in the list below will be added as dimensions to ingested OTLP metrics if they are present in the OpenTelemetry resource or in the instrumentation scope.  **Notes:**  * Attributes **must** be added in their **original format**, as exported to Dynatrace by the telemetry source. For example, if the attribute is in `PascalCase`, the same case must be used when adding the attribute to the list. * Dynatrace does not recommend changing/removing the attributes starting with "dt.". Dynatrace leverages these attributes to [Enrich metrics](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics).': 'Если включено, атрибуты из списка ниже будут добавлены как dimensions к ingested OTLP-метрикам, если они присутствуют в OpenTelemetry resource или в instrumentation scope.  **Примечания:**  * Атрибуты **обязательно** добавлять в **исходном формате**, в каком они экспортируются в Dynatrace источником телеметрии. Например, если атрибут в `PascalCase`, тот же регистр нужно использовать при добавлении в список. * Dynatrace не рекомендует менять или удалять атрибуты, начинающиеся с "dt.". Dynatrace использует их для [Enrich metrics](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics).',
    'The attributes defined in the list below will be dropped from all ingested OTLP metrics.  **Notes:**  * Attributes **must** be added in their **original format**, as exported to Dynatrace by the telemetry source. For example, if the attribute is in `PascalCase`, the same case must be used when adding the attribute to the list. * Wildcards are only supported in Metrics powered by Grail. * Dynatrace does not recommend including attributes starting with "dt." to the deny list. Dynatrace leverages these attributes to [Enrich metrics](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics).': 'Атрибуты из списка ниже будут отбрасываться из всех ingested OTLP-метрик.  **Примечания:**  * Атрибуты **обязательно** добавлять в **исходном формате**, в каком они экспортируются в Dynatrace источником телеметрии. Например, если атрибут в `PascalCase`, тот же регистр нужно использовать при добавлении в список. * Wildcards поддерживаются только в Metrics powered by Grail. * Dynatrace не рекомендует включать в deny list атрибуты, начинающиеся с "dt.". Dynatrace использует их для [Enrich metrics](https://www.dynatrace.com/support/help/extend-dynatrace/extend-metrics/reference/enrich-metrics).',
    "When enabled, the attribute will be added as a dimension to ingested metrics if present in the OpenTelemetry resource or in the instrumentation scope.": "Если включено, атрибут будет добавлен как dimension к ingested-метрикам, если присутствует в OpenTelemetry resource или в instrumentation scope.",
    "When enabled, the attribute will be dropped on all ingested metrics.": "Если включено, атрибут будет отбрасываться у всех ingested-метрик.",
    # 8. deployment-management-update-windows
    "Every **X** days:  * `1` = every day, * `2` = every two days, * `3` = every three days, * etc.": "Каждые **X** дней:  * `1` = ежедневно, * `2` = раз в два дня, * `3` = раз в три дня, * и т. д.",
    "Every **X** weeks:  * `1` = every week, * `2` = every two weeks, * `3` = every three weeks, * etc.": "Каждые **X** недель:  * `1` = еженедельно, * `2` = раз в две недели, * `3` = раз в три недели, * и т. д.",
    "Every **X** months:  * `1` = every month, * `2` = every two months, * `3` = every three months, * etc.": "Каждые **X** месяцев:  * `1` = ежемесячно, * `2` = раз в два месяца, * `3` = раз в три месяца, * и т. д.",
    # 9. process-custom-process-monitoring-rule
    "supported only with OneAgent 1.167+": "поддерживается только с OneAgent 1.167+",
    # 10. failure-detection-service-general-parameters
    "Define exceptions which indicate that an entire service call should not be considered as failed. E.g. an exception indicating that the client aborted the operation. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will be considered successful. Compared to ignored exceptions, the request will be considered successful even if other exceptions occur in the same request.": "Задайте исключения, означающие, что весь вызов сервиса не должен считаться провалившимся. Например, исключение о том, что клиент прервал операцию. Если на **entry node** сервиса возникает исключение, соответствующее любому из заданных шаблонов, вызов считается успешным. В отличие от игнорируемых исключений, запрос будет считаться успешным даже при других исключениях в том же запросе.",
    "Some exceptions that are thrown by legacy or 3rd-party code indicate a specific response, not an error. Use this setting to instruct Dynatrace to treat such exceptions as non-failed requests. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will not be considered as a failure. Other exceptions occurring at the same request might still mark the request as failed.": "Некоторые исключения, бросаемые legacy- или сторонним кодом, означают конкретный ответ, а не ошибку. Используйте этот параметр, чтобы Dynatrace трактовал такие исключения как непровалившиеся запросы. Если на **entry node** сервиса возникает исключение, соответствующее любому из заданных шаблонов, оно не считается failure. Другие исключения в том же запросе по-прежнему могут пометить запрос как провалившийся.",
    "There may be situations where your application code handles exceptions gracefully in a manner that these failures aren't detected by Dynatrace. Use this setting to define specific gracefully-handled exceptions that should be treated as service failures.": "Бывают ситуации, когда код приложения корректно обрабатывает исключения так, что эти failures не обнаруживаются Dynatrace. Используйте этот параметр, чтобы задать конкретные изящно обработанные исключения, которые должны считаться отказами сервиса.",
    "Some custom error situations are only detectable via a return value or other means. To support such cases, [define a request attribute](https://dt-url.net/ys5k0p4y) that captures the required data. Then define a custom error rule that determines if the request has failed based on the value of the request attribute.": "Некоторые пользовательские ошибочные ситуации обнаруживаются только по возвращаемому значению или иным способом. Для таких случаев [задайте request attribute](https://dt-url.net/ys5k0p4y), захватывающий нужные данные. Затем задайте custom error rule, которое по значению request attribute определяет, провалился запрос или нет.",
    "The pattern will match if it is contained within the actual class name.": "Шаблон совпадает, если он содержится внутри фактического имени класса.",
    "Optionally, define an exception message pattern. The pattern will match if the actual exception message contains the pattern.": "По желанию задайте шаблон сообщения исключения. Шаблон совпадает, если фактическое сообщение исключения содержит этот шаблон.",
    # 11. appsec-runtime-vulnerability-detection
    "When new monitoring rules are enabled, classic rules are disabled. To re-enable classic rules, disable the new monitoring rules.": "Когда включены новые правила мониторинга, classic-правила отключаются. Чтобы снова включить classic-правила, отключите новые правила мониторинга.",
    "Global third-party vulnerability detection control defines the default for all processes.": "Глобальное управление third-party vulnerability detection задаёт значение по умолчанию для всех процессов.",
    "Vulnerability Analytics can be enabled/disabled per supported technology.": "Vulnerability Analytics можно включать или отключать по каждой поддерживаемой технологии.",
    'Global Java code-level vulnerability detection control defines the default for all process groups. You can use monitoring rules to override the default for certain processes.  Code-level vulnerability detection for Java has been designed to carry a production-ready performance footprint. The overhead is depending on your application, but should be negligible in most cases. You have to enable the OneAgent feature "Java code-level vulnerability evaluation" to get started.': 'Глобальное управление Java code-level vulnerability detection задаёт значение по умолчанию для всех process groups. С помощью monitoring rules можно переопределить значение по умолчанию для конкретных процессов.  Code-level vulnerability detection для Java спроектирована с production-ready накладными расходами. Overhead зависит от приложения, но в большинстве случаев пренебрежимо мал. Для начала работы необходимо включить функцию OneAgent "Java code-level vulnerability evaluation".',
    'Global .NET code-level vulnerability detection control defines the default for all process groups. You can use monitoring rules to override the default for certain processes.  Code-level vulnerability detection for .NET has been designed to carry a production-ready performance footprint. The overhead is depending on your application, but should be negligible in most cases. You have to enable the OneAgent feature ".NET code-level vulnerability evaluation" to get started.': 'Глобальное управление .NET code-level vulnerability detection задаёт значение по умолчанию для всех process groups. С помощью monitoring rules можно переопределить значение по умолчанию для конкретных процессов.  Code-level vulnerability detection для .NET спроектирована с production-ready накладными расходами. Overhead зависит от приложения, но в большинстве случаев пренебрежимо мал. Для начала работы необходимо включить функцию OneAgent ".NET code-level vulnerability evaluation".',
    'Global Go code-level vulnerability detection control defines the default for all process groups. You can use monitoring rules to override the default for certain processes.  Code-level vulnerability detection for Go has been designed to carry a production-ready performance footprint. The overhead is depending on your application, but should be negligible in most cases. You have to enable the OneAgent feature "Go code-level vulnerability evaluation" to get started.': 'Глобальное управление Go code-level vulnerability detection задаёт значение по умолчанию для всех process groups. С помощью monitoring rules можно переопределить значение по умолчанию для конкретных процессов.  Code-level vulnerability detection для Go спроектирована с production-ready накладными расходами. Overhead зависит от приложения, но в большинстве случаев пренебрежимо мал. Для начала работы необходимо включить функцию OneAgent "Go code-level vulnerability evaluation".',
    # 12. anomaly-detection-kubernetes-cluster
    "Alerts if cluster has not been ready for a given amount of time": "Оповещает, если кластер не был готов в течение заданного времени",
    "Alert if": "Оповестить, если",
    "Evaluates the Kubernetes readyz endpoint": "Оценивает Kubernetes readyz endpoint",
    # 13. sessionreplay-web-privacy-preferences
    "When [Session Replay opt-in mode](https://dt-url.net/sr-opt-in-mode) is turned on, Session Replay is deactivated until explicitly activated via an API call.": "Когда [opt-in режим Session Replay](https://dt-url.net/sr-opt-in-mode) включён, Session Replay деактивирован до явной активации через вызов API.",
    "Exclude webpages or views from Session Replay recording by adding [URL exclusion rules](https://dt-url.net/sr-url-exclusion)": "Исключайте веб-страницы или views из записи Session Replay с помощью [URL exclusion rules](https://dt-url.net/sr-url-exclusion)",
    "To protect your end users' privacy, select or customize [predefined masking options](https://dt-url.net/sr-masking-preset-options) that suit your content recording and playback requirements.": "Чтобы защитить приватность конечных пользователей, выберите или настройте [предопределённые опции маскирования](https://dt-url.net/sr-masking-preset-options), подходящие под ваши требования к записи и воспроизведению контента.",
    "Recording masking settings are applied at record time. When you set these settings to a more restrictive option, the same option is also enabled for the playback masking settings.": "Параметры маскирования при записи применяются во время записи. При выборе более ограничительной опции та же опция включается и для параметров маскирования при воспроизведении.",
    "The elements are defined by the CSS selector or attribute name.": "Элементы задаются CSS-селектором или именем атрибута.",
    "Playback masking settings are applied during playback of recorded sessions, including playback of sessions that were recorded before these settings were applied.": "Параметры маскирования при воспроизведении применяются во время воспроизведения записанных сессий, включая воспроизведение сессий, записанных до применения этих параметров.",
    "Choose the masking rule target type": "Выберите тип цели правила маскирования",
    "Content masking can be applied to webpages where personal data is displayed. When content masking is applied to parent elements, all child elements are masked by default.": "Маскирование контента применимо к веб-страницам с отображением персональных данных. Когда маскирование контента применяется к родительским элементам, все child-элементы маскируются по умолчанию.",
    "Attribute masking can be applied to web applications that store data within attributes, typically data-NAME attributes in HTML5. When you define attributes, their values are masked while recording but not removed.": "Маскирование атрибутов применимо к веб-приложениям, хранящим данные внутри атрибутов, обычно атрибутов data-NAME в HTML5. При задании атрибутов их значения маскируются во время записи, но не удаляются.",
    "Hide user interactions with these elements, including clicks that expand elements, highlighting that results from hovering a cursor over an option, and selection of specific form options.": "Скрыть пользовательские взаимодействия с этими элементами, включая клики, разворачивающие элементы, подсветку при наведении курсора и выбор конкретных опций формы.",
    # 14. process-group-advanced-detection-rule
    "Apply this rule to processes where the selected property contains the specified string.": "Применять это правило к процессам, у которых выбранное свойство содержит указанную строку.",
    "You can define the properties that should be used to identify your process groups.": "Можно задать свойства, которые будут использоваться для идентификации process groups.",
    "You can define the properties that should be used to identify your process instances.": "Можно задать свойства, которые будут использоваться для идентификации process instances.",
    "(case sensitive)": "(чувствительно к регистру)",
    "Note: Not all types can be detected at startup.": "Примечание: не все типы можно определить при запуске.",
    "Optionally delimit this property between *From* and *To*.": "По желанию ограничьте это свойство между *From* и *To*.",
    "If this option is selected, the default Dynatrace behavior is disabled for these detected processes. Only this rule is used to separate the process group.  If this option is not selected, this rule contributes to the default Dynatrace process group detection.  [See our help page for examples.](https://dt-url.net/1722wrz)": "Если эта опция выбрана, поведение Dynatrace по умолчанию отключается для обнаруженных процессов. Для разделения process group используется только это правило.  Если опция не выбрана, это правило дополняет обнаружение process group по умолчанию.  [Примеры см. на странице помощи.](https://dt-url.net/1722wrz)",
    "(e.g. versions, hex, dates, and build numbers)": "(например, версии, hex, даты и build-номера)",
}

# Structural canon (shared with L4-AG.1a.1-9 / L4-AF).
STRUCT = [
    ("Retrieve schema via Settings API", "Получить schema через Settings API"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
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
