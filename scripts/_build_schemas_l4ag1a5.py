# -*- coding: utf-8 -*-
"""L4-AG.1a.5 builder: 32 builtin-*.md schema-table files (2.4-3.0 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Anchor canon: L4-AG.1a.4 _build_schemas_l4ag1a4.py.

Class L4-AF schema-table (## Authentication + ## Parameters + Schema-ID/Scope
row + GET endpoints + (optional) nested ##### The X object sub-headings).

Mojibake byte-keys preserved verbatim:
  - rum-custom-enablement `applicationâ€™s` triple-mojibake (U+00E2 U+0080 U+0099)

Empty-label rows (`column-1 is just \\`code\\``): _param_row now allows empty
label, переводит только cdesc если найдено в PARAM_DESC.
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

# Triple-mojibake apostrophe sequence (3 chars => 6 bytes in UTF-8).
Q = chr(0xE2) + chr(0x80) + chr(0x99)

PILOT = [
    "builtin-bizevents-processing-metrics-rule.md",
    "builtin-preferences-ipaddressmasking.md",
    "builtin-disk-analytics-extension.md",
    "builtin-virtualization-vmware.md",
    "builtin-mainframe-mqfilters.md",
    "builtin-rum-user-experience-score.md",
    "builtin-synthetic-multiprotocol-outage-handling.md",
    "builtin-rum-web-key-performance-metric-custom-actions.md",
    "builtin-dt-javascript-runtime-app-monitoring.md",
    "builtin-exclude-network-traffic.md",
    "builtin-rum-web-browser-exclusion.md",
    "builtin-deployment-oneagent-updates.md",
    "builtin-rum-mobile-key-performance-metrics.md",
    "builtin-host-monitoring-mode.md",
    "builtin-rum-web-resource-types.md",
    "builtin-synthetic-browser-outage-handling.md",
    "builtin-rum-custom-enablement.md",
    "builtin-synthetic-browser-performance-thresholds.md",
    "builtin-mainframe-txstartfilters.md",
    "builtin-span-capturing.md",
    "builtin-container-monitoring-rule.md",
    "builtin-rum-processgroup.md",
    "builtin-rum-web-injection-cookie.md",
    "builtin-anomaly-detection-frequent-issues.md",
    "builtin-availability-process-group-alerting.md",
    "builtin-apis-detection-rules.md",
    "builtin-span-entry-points.md",
    "builtin-attribute-masking.md",
    "builtin-service-splitting-rules.md",
    "builtin-rum-web-custom-errors.md",
    "builtin-bizevents-processing-pipelines-rule.md",
    "builtin-process-group-simple-detection-rule.md",
]

# Schema heading display-name. EN product/tech terms kept where canonical.
# «Outage handling» дважды (два разных файла) — одинаковый ключ, один dict-entry.
DISPLAY_NAME = {
    "Business event metric extraction": "Извлечение метрик из Business event",
    "Anonymize End-User IP Addresses": "Анонимизация IP-адресов конечных пользователей",
    "Disk Analytics Extension": "Расширение Disk Analytics",
    "VMware": "VMware",
    "IBM MQ filters": "Фильтры IBM MQ",
    "User experience score": "Оценка пользовательского опыта",
    "Outage handling": "Обработка простоев",
    "Apdex configuration for custom actions": "Настройка Apdex для пользовательских действий",
    "App Monitoring": "Мониторинг приложений",
    "Exclude network traffic": "Исключение сетевого трафика",
    "Exclude/Include browsers from monitoring": "Исключение/включение браузеров из мониторинга",
    "OneAgent updates": "Обновления OneAgent",
    "Apdex configuration": "Настройка Apdex",
    "Monitoring Mode": "Режим мониторинга",
    "Resource types": "Типы ресурсов",
    "Enablement and cost control": "Включение и контроль стоимости",
    "Performance thresholds": "Пороги производительности",
    "Transaction start filters": "Фильтры начала транзакций",
    "Span capturing": "Захват span'ов",
    "Container monitoring rules": "Правила мониторинга контейнеров",
    "Real User Monitoring for process group": "Real User Monitoring для process group",
    "Cookie": "Cookie",
    "Frequent issue detection": "Определение частых проблем",
    "Process group availability monitoring": "Мониторинг доступности process group",
    "API detection rules": "Правила обнаружения API",
    "Span entry points": "Точки входа span'ов",
    "Attribute data masking": "Маскирование данных атрибутов",
    "Service splitting": "Разделение сервисов",
    "Custom errors": "Пользовательские ошибки",
    "Business event processing": "Обработка Business event",
    "Simple detection rules": "Простые правила обнаружения",
}

# Whole-line schema descriptions (replaced as `\n` + EN + `\n` -> `\n` + RU + `\n`).
SCHEMA_DESC = {
    # 1. bizevents-processing-metrics-rule (BOM stripped from link text)
    "With [business event metrics](https://dt-url.net/m3034if), you can use queries to create custom alerts representing specific business event occurrences or attribute values.": "С помощью [business event metrics](https://dt-url.net/m3034if) можно использовать запросы для создания пользовательских оповещений, представляющих конкретные вхождения business event или значения атрибутов.",
    "Note:": "Примечание:",
    "* Newly defined business event metrics can only be applied to Business Event data ingested after metric creation.": "* Вновь заданные метрики Business event могут применяться только к данным Business Event, поступившим после создания метрики.",
    "* Business Event metrics consume DDUs.": "* Метрики Business Event расходуют DDU.",
    "For complete details on pricing, visit [DDUs for custom metrics](https://dt-url.net/vg43xi8).": "Подробности о ценообразовании см. в [DDUs for custom metrics](https://dt-url.net/vg43xi8).",
    # 2. preferences-ipaddressmasking (BOM stripped)
    "Control what data Dynatrace is capturing. Dynatrace can capture IP addresses and GPS coordinates of end users to determine the location from which they access your application. IP Address Masking truncates IP addresses captured from your end users' web browsers and the data captured by OneAgent for effective de-identification.": "Управляйте тем, какие данные захватывает Dynatrace. Dynatrace может захватывать IP-адреса и GPS-координаты конечных пользователей, чтобы определить место, откуда они обращаются к приложению. IP Address Masking усекает IP-адреса, захваченные из браузеров конечных пользователей и данных OneAgent, для эффективной деперсонализации.",
    "To learn more, visit [Mask IPs and GPS coordinates](https://dt-url.net/mask-end-users-ip-addresses). For further details on Dynatrace's privacy settings, visit [Data privacy and security](https://dt-url.net/zn03sq4) documentation.": "Подробнее см. [Mask IPs and GPS coordinates](https://dt-url.net/mask-end-users-ip-addresses). О настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/zn03sq4).",
    # 3. disk-analytics-extension
    "This extension allows more detailed visibility on local datastores and their volumes, partitions and raid instances on Linux hosts.": "Это расширение даёт более детальную видимость локальных хранилищ данных, их томов, разделов и raid-устройств на Linux-хостах.",
    # 4. virtualization-vmware
    "Use this page to connect your VMware vCenter, standalone ESXi hosts to Dynatrace for monitoring. For VMware instances, connect all vCenter servers that manage virtual machines where Dynatrace OneAgent is installed. You don't need to add ESXi hosts if they are managed by a vCenter server that is connected to Dynatrace.": "На этой странице подключите к Dynatrace VMware vCenter и отдельные ESXi-хосты для мониторинга. Для VMware-инстансов подключите все vCenter-серверы, управляющие виртуальными машинами, на которых установлен Dynatrace OneAgent. ESXi-хосты добавлять не нужно, если ими управляет vCenter-сервер, подключённый к Dynatrace.",
    # 5. mainframe-mqfilters
    "Dynatrace automatically traces CICS and IMS transactions originating from IBM MQ queues. To limit tracing to certain queues, specify their names in the include lists. To exclude queues from tracing, specify their names in the exclude lists. For IMS, these lists apply to message processing regions.": "Dynatrace автоматически трассирует транзакции CICS и IMS, исходящие из очередей IBM MQ. Чтобы ограничить трассировку определёнными очередями, укажите их имена в списках включения. Чтобы исключить очереди из трассировки, укажите их имена в списках исключения. Для IMS эти списки применяются к регионам обработки сообщений.",
    "To only trace specific transactions submitted via the IMS bridge, specify their transaction IDs in the include list or exclude list.": "Чтобы трассировать только определённые транзакции, отправленные через IMS bridge, укажите их идентификаторы транзакций в списке включения или исключения.",
    # 6. rum-user-experience-score (BOM stripped)
    "A [user experience score](https://dt-url.net/39034wt) is calculated for each user session. Scores reflect the overall performance, usability, and detected errors of each session. Experiences are classified as either Satisfying, Tolerable, or Frustrating.": "Для каждой пользовательской сессии рассчитывается [user experience score](https://dt-url.net/39034wt). Оценки отражают общую производительность, удобство использования и обнаруженные ошибки каждой сессии. Опыт классифицируется как Satisfying, Tolerable или Frustrating.",
    # 7. synthetic-multiprotocol-outage-handling — текст идентичен L4-AG.1a.4
    "Dynatrace can generate problems for both global outages and/or local outages based on the availability of either all configured locations or only individual locations over consecutive runs.": "Dynatrace может генерировать проблемы как для глобальных, так и для локальных простоев на основе доступности всех настроенных расположений или только отдельных расположений в последовательных прогонах.",
    # 8. rum-web-key-performance-metric-custom-actions (BOM stripped)
    "Set the Tolerating and Frustrated performance thresholds to [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) for this application.": "Задайте пороги производительности Tolerating и Frustrated, чтобы [refine the Apdex calculations](https://dt-url.net/apdex-thresholds) для этого приложения.",
    "The key performance metric for custom actions is always **User action duration**.": "Ключевая метрика производительности для пользовательских действий всегда **User action duration**.",
    # 9. dt-javascript-runtime-app-monitoring (BOM stripped)
    "Set up the monitoring parameters for your custom Dynatrace applications. These parameters will establish the default behavior for logging and tracing within this environment.": "Задайте параметры мониторинга для пользовательских приложений Dynatrace. Эти параметры определяют поведение по умолчанию для логирования и трассировки в этом окружении.",
    "[Discover more about App functions and their monitoring.](https://dt-url.net/dz23v17).": "[Discover more about App functions and their monitoring.](https://dt-url.net/dz23v17).",
    # 10. exclude-network-traffic
    "OneAgent automatically detects and monitors all of your network traffic, but you can exclude traffic on specific network interfaces or hosts from monitoring.": "OneAgent автоматически обнаруживает и мониторит весь сетевой трафик, но трафик на определённых сетевых интерфейсах или хостах можно исключить из мониторинга.",
    # 11. rum-web-browser-exclusion (BOM stripped)
    "If you want to exclude certain outdated browser types from your list of monitored browsers, create [browser exclusion](https://dt-url.net/0e2z0pp0) rules for the browsers that are to be excluded.": "Чтобы исключить определённые устаревшие типы браузеров из списка мониторимых, создайте правила [browser exclusion](https://dt-url.net/0e2z0pp0) для тех браузеров, которые нужно исключить.",
    # 12. deployment-oneagent-updates (BOM stripped)
    "Select the OneAgent target version and configure update behavior. The selected version is also used for the [Deployment API](https://dt-url.net/hh03wzk) and OneAgent deployment pages. For more about the OneAgent target version, see [OneAgent update](https://dt-url.net/9901p5j). To learn more about the latest updates, see the [OneAgent release notes](https://dt-url.net/release-notes-oneagent). To configure RUM JavaScript update behavior, see RUM JavaScript updates (`<your-dynatrace-url>//ui/settings/builtin:rum.web.rum-javascript-updates`).": "Выберите целевую версию OneAgent и настройте поведение обновлений. Выбранная версия также используется на страницах [Deployment API](https://dt-url.net/hh03wzk) и развёртывания OneAgent. О целевой версии OneAgent см. [OneAgent update](https://dt-url.net/9901p5j). О последних обновлениях см. [OneAgent release notes](https://dt-url.net/release-notes-oneagent). О поведении обновлений RUM JavaScript см. RUM JavaScript updates (`<your-dynatrace-url>//ui/settings/builtin:rum.web.rum-javascript-updates`).",
    # 13. rum-mobile-key-performance-metrics (BOM stripped)
    "[Set the user-satisfaction performance thresholds](https://dt-url.net/4l023z2) (**Satisfactory**, **Tolerable**, and **Frustrating**) for the **User action duration** metric to refine the Apdex calculations for this app.": "[Set the user-satisfaction performance thresholds](https://dt-url.net/4l023z2) (**Satisfactory**, **Tolerable** и **Frustrating**) для метрики **User action duration**, чтобы уточнить расчёты Apdex для этого приложения.",
    # 14. host-monitoring-mode (BOM stripped from link text)
    "OneAgent monitoring mode can only be switched while the agent is connected.": "Режим мониторинга OneAgent можно переключить только пока агент подключён.",
    "Note that for this schema only, the [GET objects](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-objects) api will usually not return any objects as these settings are stored on the agents - please use the [GET effective values](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values) api instead.": "Учтите: только для этой схемы API [GET objects](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-objects) обычно не возвращает объекты, так как настройки хранятся на агентах. Используйте вместо него API [GET effective values](https://docs.dynatrace.com/docs/dynatrace-api/environment-api/settings/objects/get-effective-values).",
    # 15. rum-web-resource-types
    "Dynatrace identifies resource types by their file extensions. In certain cases, however, downloaded resources may lack the correct file extensions. For such cases you can set up rules that define the correct resource types of these resources. These rules ensure that resource-type breakdowns are rendered properly and that the resources types in the waterfall chart are displayed correctly.": "Dynatrace определяет типы ресурсов по расширениям файлов. Однако в некоторых случаях загруженные ресурсы могут не иметь корректных расширений. Для таких случаев можно задать правила, определяющие правильные типы этих ресурсов. Правила гарантируют, что разбивка по типам ресурсов рендерится корректно и типы ресурсов в waterfall-диаграмме отображаются правильно.",
    "Dynatrace supports Java regular expressions syntax. Resource types of resources with URL fragments that match provided regular expressions will be overriden by the value given in the *Primary resource type* field and can be further categorized by specifying a *Secondary resource type*.": "Dynatrace поддерживает синтаксис регулярных выражений Java. Типы ресурсов с URL-фрагментами, совпадающими с заданными регулярными выражениями, переопределяются значением из поля *Primary resource type* и могут дополнительно категоризироваться через *Secondary resource type*.",
    "Type *^.\\*\\.od.{1}$* into the **Regular expression field**, select *Other* as **Primary resource type** and type *OpenDocument* into the **Secondary resource type** field to override the default resource type for resources with file extension *.od*\\*.": "Введите *^.\\*\\.od.{1}$* в поле **Regular expression field**, выберите *Other* в качестве **Primary resource type** и введите *OpenDocument* в поле **Secondary resource type**, чтобы переопределить тип ресурса по умолчанию для ресурсов с расширением *.od*\\*.",
    # 16. synthetic-browser-outage-handling — same prose as #7 (collapsed in dict)
    # 17. rum-custom-enablement
    "Turn on Real User Monitoring. Configure cost and traffic control settings.": "Включите Real User Monitoring. Настройте параметры контроля стоимости и трафика.",
    # 18. synthetic-browser-performance-thresholds
    "Dynatrace generates a new problem if this synthetic monitor exceeds any of the 'Total duration' performance thresholds below in 3 of the 5 most recent executions at a given location, unless there is an open maintenance window for the synthetic monitor. Multiple locations with 3 such violations can be included in a problem. The problem is closed if no performance threshold is violated in the 5 most recent executions at each of the previously affected locations.": "Dynatrace создаёт новую проблему, если этот synthetic-монитор превышает любой из порогов производительности 'Total duration' ниже в 3 из 5 последних прогонов в данном расположении, при условии что для synthetic-монитора нет открытого maintenance window. В одну проблему могут входить несколько расположений с 3 такими нарушениями. Проблема закрывается, если в 5 последних прогонах в каждом из ранее затронутых расположений ни один порог не нарушен.",
    # 19. mainframe-txstartfilters
    "Dynatrace automatically traces CICS and IMS transactions when monitored services call them. Transactions that originate on the mainframe, on a terminal, or are called by unmonitored services must be explicitly listed to be monitored.": "Dynatrace автоматически трассирует транзакции CICS и IMS, когда их вызывают мониторимые сервисы. Транзакции, исходящие с mainframe, с терминала или вызываемые немониторимыми сервисами, должны быть явно перечислены для мониторинга.",
    "Add CICS and IMS transactions originating on a terminal (e.g., IBM 3270 green screen terminal) to the terminal transaction start filter. Add all other transactions to the transaction start filters.": "Добавьте транзакции CICS и IMS, исходящие с терминала (например, IBM 3270 green screen terminal), в фильтр начала терминальных транзакций. Остальные транзакции добавьте в фильтры начала транзакций.",
    "Note that traces started using the transaction filters will never be linked to a previous trace, regardless of how the transaction was initiated.": "Учтите: трассы, запущенные через фильтры транзакций, никогда не будут связаны с предыдущей трассой, независимо от способа инициации транзакции.",
    # 20. span-capturing
    "OpenTelemetry spans are captured by default. Define rules to exclude specific spans.": "Span'ы OpenTelemetry захватываются по умолчанию. Задайте правила для исключения конкретных span'ов.",
    "Note: This config does not apply to Trace ingest.": "Примечание: эта конфигурация не применяется к Trace ingest.",
    # 21. container-monitoring-rule (BOM stripped)
    "Within container environments, OneAgent automatically injects code modules into containerized processes to provide out of the box full-stack visibility into applications running within containers. Dynatrace provides complete control over automatic injection of code modules into the container technologies.": "В контейнерных окружениях OneAgent автоматически внедряет модули кода в контейнеризованные процессы, обеспечивая полную full-stack видимость приложений, работающих в контейнерах. Dynatrace даёт полный контроль над автоматическим внедрением модулей кода в контейнерные технологии.",
    "In Kubernetes, container monitoring rules are evaluated only in case of `classicFullStack` injection mode. The rules are ignored in case of `cloudNativeFullStack` or `applicationMonitoring`.": "В Kubernetes правила мониторинга контейнеров вычисляются только в режиме внедрения `classicFullStack`. В режимах `cloudNativeFullStack` или `applicationMonitoring` правила игнорируются.",
    "Please use the annotation-based configuration option as described [here](https://dt-url.net/k8sdtoconfig).": "Используйте вариант конфигурации на основе аннотаций, как описано [here](https://dt-url.net/k8sdtoconfig).",
    # 22. rum-processgroup (BOM stripped)
    "With [Real User Monitoring](https://dt-url.net/1n2b0prq) enabled, Dynatrace gathers details about load times and page behavior that your customers experience with your application. Only applications with injected JavaScript tags can be monitored.": "Когда включён [Real User Monitoring](https://dt-url.net/1n2b0prq), Dynatrace собирает данные о времени загрузки и поведении страниц, которые видят клиенты при работе с приложением. Мониторятся только приложения с внедрёнными JavaScript-тегами.",
    # 23. rum-web-injection-cookie (BOM stripped)
    "Dynatrace RUM uses cookies to correlate user actions with backend performance metrics. You can change the cookie settings here. Learn more about RUM cookies in our [documentation](https://dt-url.net/wmq1pti).": "Dynatrace RUM использует cookie для корреляции пользовательских действий с backend-метриками производительности. Здесь можно изменить настройки cookie. Подробнее о RUM cookies см. в [documentation](https://dt-url.net/wmq1pti).",
    # 24. anomaly-detection-frequent-issues (BOM stripped, two-line desc with trailing spaces)
    "Dynatrace is automatically detecting frequent issues over a period of one week. A problem is automatically converted into a frequent issue if the problem is detected multiple times throughout a day and over a weeks period of time and if it is not getting worse. Once it's classified as a frequent issue alerting is automatically disabled. In case that the frequent issue is getting worse problem alerts are again sent out. Within this page you can disable the frequent issue detection for all topological levels.  ": "Dynatrace автоматически обнаруживает частые проблемы за период в одну неделю. Проблема автоматически переводится в категорию частых, если она обнаруживается несколько раз в течение дня и за недельный период и при этом не усугубляется. После классификации как частая, оповещения автоматически отключаются. Если частая проблема усугубляется, оповещения снова отправляются. На этой странице можно отключить определение частых проблем для всех топологических уровней.  ",
    "See our [help documentation](https://dt-url.net/ex4v0pcw) about frequent issue detection.": "См. [help documentation](https://dt-url.net/ex4v0pcw) об определении частых проблем.",
    # 25. availability-process-group-alerting
    "Dynatrace continuously monitors the availability of this process group. Use the settings below to define the approach that Dynatrace should use for monitoring the availability of this process group.": "Dynatrace непрерывно мониторит доступность этой process group. Используйте настройки ниже, чтобы определить подход Dynatrace к мониторингу доступности этой process group.",
    # 26. apis-detection-rules
    "Modern applications use a lot of different frameworks, so stacktraces in method hotspots and exceptions can become quite long. APIs allow you to spot a component and the respective ownership that is responsible for a hotspot or degradation faster.": "Современные приложения используют много разных фреймворков, поэтому stacktrace'ы в method hotspot'ах и исключениях становятся довольно длинными. API позволяют быстрее находить компонент и ответственную команду за hotspot или деградацию.",
    "API detection rules look at a stacktrace frame and classify it based on classes (Java, .NET and PHP) or files (Node.js, PHP and GO) depending on the technology. The rules are executed in order and the first match decides the API. Marking APIs as third party will allow you to focus on non-third party APIs.": "Правила обнаружения API анализируют фрейм stacktrace и классифицируют его по классам (Java, .NET и PHP) или файлам (Node.js, PHP и GO) в зависимости от технологии. Правила выполняются по порядку, и первое совпадение определяет API. Маркировка API как сторонних позволит сосредоточиться на не-сторонних API.",
    # 27. span-entry-points
    "OpenTelemetry spans can start new PurePaths. Define rules that define which spans should not be considered as entry points.": "Span'ы OpenTelemetry могут начинать новые PurePath'ы. Задайте правила, определяющие, какие span'ы не должны считаться точками входа.",
    # 28. attribute-masking (BOM stripped)
    "Configure the visibility of stored attribute values to to meet your privacy requirements. Users with **View sensitive request data** permissions will always see the values. For further details on Dynatrace's privacy settings, visit the [Data privacy and security](https://dt-url.net/bo210srx) documentation.": "Настройте видимость хранимых значений атрибутов в соответствии с требованиями приватности. Пользователи с правами **View sensitive request data** всегда видят значения. Подробнее о настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/bo210srx).",
    # 29. service-splitting-rules (BOM stripped)
    "Define rules to split services based on resource attributes defined in the [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) and custom attributes. Rules are evaluated in order and the first matching rule applies.": "Задайте правила разделения сервисов на основе атрибутов ресурсов из [Semantic Dictionary](https://docs.dynatrace.com/docs/discover-dynatrace/references/semantic-dictionary/fields) и пользовательских атрибутов. Правила вычисляются по порядку, применяется первое совпавшее.",
    # 30. rum-web-custom-errors (BOM stripped)
    "Create rules to capture custom errors and include them in your Apdex calculations or Davis AI problem detection and analysis.": "Создайте правила для захвата пользовательских ошибок и включения их в расчёты Apdex или обнаружение и анализ проблем Davis AI.",
    "For more details, see [Configure custom errors](https://dt-url.net/sh220gh).": "Подробнее см. [Configure custom errors](https://dt-url.net/sh220gh).",
    # 31. bizevents-processing-pipelines-rule (BOM stripped)
    "Incoming business events can be transformed through processing rules using [this syntax](https://dt-url.net/pz030w5). Note that rules are processed sequentially, making the order important; a different rule order could give different results.": "Входящие business events можно преобразовывать через правила обработки с помощью [this syntax](https://dt-url.net/pz030w5). Учтите: правила обрабатываются последовательно, поэтому порядок важен, разный порядок может давать разные результаты.",
    # 32. process-group-simple-detection-rule (BOM stripped)
    "Simple process group detection rules enable you to adapt the default process-group detection logic for deep monitored processes via **environment variables** or **Java system properties**. [More about custom process-group detection](https://dt-url.net/ty02won)": "Простые правила обнаружения process group позволяют адаптировать логику обнаружения process group по умолчанию для глубокомониторимых процессов через **environment variables** или **Java system properties**. [More about custom process-group detection](https://dt-url.net/ty02won)",
    'Note: Detection rules change the composition, makeup, and identity of a process group, not just the name. If you only need to change default name use the naming rules (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`) instead.': 'Примечание: правила обнаружения меняют состав, структуру и идентичность process group, а не только имя. Если нужно изменить только имя по умолчанию, используйте правила наименования (`<your-dynatrace-url>//#settings/pgnamingsettings "Visit Naming rules page"`).',
    "Process-group detection rules only affect processes that are deep monitored by the Dynatrace OneAgent and require a restart of your processes to affect how processes are identified and grouped.": "Правила обнаружения process group влияют только на процессы, которые глубокомониторятся Dynatrace OneAgent, и для применения изменений идентификации и группировки требуют перезапуска процессов.",
}

# Parameter table col-1 label (text before `\`code\``). EN-lock for tech terms.
PARAM_LABEL = {
    # Common cross-batch
    "Enabled": "Включено",
    "Name": "Имя",
    "Type": "Тип",
    "URL": "URL",
    "Description": "Описание",
    "Pattern": "Шаблон",
    "Key": "Ключ",
    "Value": "Значение",
    "Source": "Источник",
    "Matcher": "Сопоставитель",
    "Matchers": "Сопоставители",
    "Rule": "Правило",
    "Rule name": "Имя правила",
    "Rule action": "Действие правила",
    "Property": "Свойство",
    "Mode": "Режим",
    "Operator": "Оператор",
    "Active": "Активно",
    # 1. bizevents-processing-metrics-rule
    "Key": "Ключ",
    "Matcher (DQL)": "Сопоставитель (DQL)",
    "Measure": "Способ измерения",
    "Attribute": "Атрибут",
    # 2. preferences-ipaddressmasking
    "Mask end-user IP addresses and GPS coordinates": "Маскировать IP-адреса и GPS-координаты конечных пользователей",
    # 3. disk-analytics-extension
    "Enable Disk Analytics data collection": "Включить сбор данных Disk Analytics",
    # 4. virtualization-vmware
    "Name this connection": "Имя подключения",
    "Specify the IP address or name of the vCenter or standalone ESXi host:": "Укажите IP-адрес или имя vCenter или отдельного ESXi-хоста:",
    "Provide user credentials for the vCenter or standalone ESXi host:": "Укажите учётные данные пользователя для vCenter или отдельного ESXi-хоста:",
    "Specify filter condition to limit the number of monitored clusters:": "Задайте условие фильтра, чтобы ограничить количество мониторимых кластеров:",
    # 5. mainframe-mqfilters
    "CICS: Included MQ queues": "CICS: включённые очереди MQ",
    "CICS: Excluded MQ queues": "CICS: исключённые очереди MQ",
    "IMS: Included MQ queues": "IMS: включённые очереди MQ",
    "IMS: Excluded MQ queues": "IMS: исключённые очереди MQ",
    "IMS bridge: Included transaction IDs": "IMS bridge: включённые ID транзакций",
    "IMS bridge: Excluded transaction IDs": "IMS bridge: исключённые ID транзакций",
    # 6. rum-user-experience-score
    "If last user action in a session is classified as Frustrating, classify the entire session as Frustrating": "Если последнее пользовательское действие в сессии классифицировано как Frustrating, классифицировать всю сессию как Frustrating",
    "Consider rage clicks / rage taps in score calculation": "Учитывать rage-клики и rage-тапы при расчёте оценки",
    "Threshold for Frustrating user experience": "Порог для Frustrating user experience",
    "Threshold for Satisfying user experience": "Порог для Satisfying user experience",
    # 7+16. outage-handling (multiprotocol + browser)
    "Generate a problem and send an alert when the monitor is unavailable at all configured locations.": "Генерировать проблему и отправлять оповещение, когда монитор недоступен во всех настроенных расположениях.",
    "Alert if all locations are unable to access my target address": "Оповестить, если все расположения не могут получить доступ к целевому адресу",
    "Alert if all locations are unable to access my web application": "Оповестить, если все расположения не могут получить доступ к веб-приложению",
    "Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location.": "Генерировать проблему и отправлять оповещение, когда монитор недоступен в течение одного или нескольких последовательных прогонов в любом расположении.",
    "Alert if at least": "Оповестить, если как минимум",
    "are unable to access my target address": "не могут получить доступ к целевому адресу",
    "are unable to access my web application": "не могут получить доступ к веб-приложению",
    "Automatic retry on error.": "Автоматическая повторная попытка при ошибке.",
    # 8. rum-web-key-performance-metric-custom-actions
    "User action duration thresholds": "Пороги User action duration",
    "Tolerating threshold [sec]": "Порог Tolerating [сек]",
    "Frustrated threshold [sec]": "Порог Frustrated [сек]",
    # 9. dt-javascript-runtime-app-monitoring
    "Default log level": "Уровень логирования по умолчанию",
    "App function traces": "Трассировки App-функций",
    "App ID": "ID приложения",
    "App specific log level": "Уровень логирования для конкретного приложения",
    "App specific function traces": "Трассировки функций для конкретного приложения",
    # 10. exclude-network-traffic
    "Exclude NIC": "Исключить NIC",
    "Exclude IP": "Исключить IP",
    "Operating system": "Операционная система",
    "Network interface": "Сетевой интерфейс",
    "IP address": "IP-адрес",
    # 11. rum-web-browser-exclusion
    "Browser exclusion list": "Список исключений браузеров",
    "These are the only browsers that should be monitored": "Только эти браузеры должны мониториться",
    "Browser": "Браузер",
    "Browser version comparator": "Компаратор версии браузера",
    "Version": "Версия",
    "Platform": "Платформа",
    # 12. deployment-oneagent-updates
    "Target version": "Целевая версия",
    "Revision": "Ревизия",
    "Update mode": "Режим обновления",
    "Update windows": "Окна обновления",
    "Update window": "Окно обновления",
    # 13. rum-mobile-key-performance-metrics
    "Consider reported errors / web request errors in Apdex calculations": "Учитывать сообщённые ошибки и ошибки web-запросов в расчётах Apdex",
    "Tolerable performance [sec]": "Tolerable performance [сек]",
    "Frustrating performance [sec]": "Frustrating performance [сек]",
    # 14. host-monitoring-mode
    "Monitoring mode": "Режим мониторинга",
    # 15. rum-web-resource-types
    "Regular expression": "Регулярное выражение",
    "The primary type of the resource.": "Основной тип ресурса.",
    "The secondary type of the resource.": "Вторичный тип ресурса.",
    # 17. rum-custom-enablement
    "Real User Monitoring": "Real User Monitoring",
    "Enable Real User Monitoring": "Включить Real User Monitoring",
    "Cost and traffic control": "Контроль стоимости и трафика",
    # 18. synthetic-browser-performance-thresholds
    "Generate a problem and send an alert on performance threshold violations": "Генерировать проблему и отправлять оповещение при нарушении порогов производительности",
    "Performance thresholds": "Пороги производительности",
    "Synthetic event": "Synthetic-событие",
    "Threshold (in seconds)": "Порог (в секундах)",
    "Number of violating executions in analyzed sliding window": "Количество нарушающих прогонов в анализируемом скользящем окне",
    "Number of executions in analyzed sliding window (sliding window size)": "Количество прогонов в анализируемом скользящем окне (размер окна)",
    "Number of most recent non-violating executions that closes the problem": "Количество последних ненарушающих прогонов, закрывающих проблему",
    # 19. mainframe-txstartfilters
    "CICS terminal transaction start filter": "Фильтр начала терминальных транзакций CICS",
    "CICS transaction start filter": "Фильтр начала транзакций CICS",
    "IMS terminal transaction start filter": "Фильтр начала терминальных транзакций IMS",
    "IMS transaction start filter": "Фильтр начала транзакций IMS",
    # 20. span-capturing
    "Span Capture Rule": "Правило захвата span",
    "Comparison Type": "Тип сравнения",
    "Case sensitive": "С учётом регистра",
    # 21. container-monitoring-rule
    "Container property": "Свойство контейнера",
    "Condition operator": "Условный оператор",
    "Condition value": "Значение условия",
    # 23. rum-web-injection-cookie
    "Use the Secure cookie attribute for cookies set by Dynatrace": "Использовать атрибут Secure для cookie, устанавливаемых Dynatrace",
    "SameSite cookie attribute": "Атрибут cookie SameSite",
    "Domain to be used for cookie placement": "Домен для размещения cookie",
    # 24. anomaly-detection-frequent-issues
    "Detect frequent issues within applications": "Определять частые проблемы внутри приложений",
    "Detect frequent issues within transactions and services": "Определять частые проблемы внутри транзакций и сервисов",
    "Detect frequent issues within infrastructure": "Определять частые проблемы внутри инфраструктуры",
    "Detect frequent issues on the environment singleton entity": "Определять частые проблемы на singleton-сущности окружения",
    # 25. availability-process-group-alerting
    "Enable process group availability monitoring": "Включить мониторинг доступности process group",
    "Open a new problem": "Открывать новую проблему",
    "Open a new problem if the number of active process instances in the group is fewer than:": "Открыть новую проблему, если количество активных инстансов процесса в группе меньше чем:",
    # 26. apis-detection-rules
    "API name": "Имя API",
    "Color": "Цвет",
    "Technology": "Технология",
    "This API defines a third party library": "Этот API описывает стороннюю библиотеку",
    "List of conditions": "Список условий",
    "Base": "База",
    # 27. span-entry-points
    "Entry Point Rule": "Правило точки входа",
    # 28. attribute-masking
    "Attribute key": "Ключ атрибута",
    "Masking": "Маскирование",
    # 29. service-splitting-rules
    "Matching condition": "Условие сопоставления",
    "Split services by resource attributes": "Разделять сервисы по атрибутам ресурсов",
    "Attribute key": "Ключ атрибута",
    # 30. rum-web-custom-errors
    "Ignore custom errors in Apdex calculations": "Игнорировать пользовательские ошибки в расчётах Apdex",
    "Match key": "Сопоставление ключа",
    "Key pattern": "Шаблон ключа",
    "Match value": "Сопоставление значения",
    "Value pattern": "Шаблон значения",
    "Capture settings": "Настройки захвата",
    "Capture this error": "Захватывать эту ошибку",
    "Include error in Apdex calculations": "Включать ошибку в расчёты Apdex",
    "Include error in Davis AI problem detection and analysis": "Включать ошибку в обнаружение и анализ проблем Davis AI",
    # 31. bizevents-processing-pipelines-rule
    "Transformation fields": "Поля преобразования",
    "Processor definition": "Определение процессора",
    "Optional": "Опционально",
    "Is Array": "Является массивом",
    "Read-only": "Только для чтения",
    "Event sample": "Образец события",
    # 32. process-group-simple-detection-rule
    "Property source": "Источник свойства",
    "Group identifier": "Идентификатор группы",
    "Instance identifier": "Идентификатор инстанса",
    "Restrict this rule to specific process types": "Ограничить это правило конкретными типами процессов",
}

# Parameter table col-3 description (when not just `-` and not enum-tail).
PARAM_DESC = {
    # 1. bizevents-processing-metrics-rule
    "[See our documentation](https://dt-url.net/bp234rv)": "[See our documentation](https://dt-url.net/bp234rv)",
    # 3. disk-analytics-extension
    "The Disk Analytics feature requires an extension to be added to your environment. You can add the Disk Analytics extension to your environment from Dynatrace Hub (`<your-dynatrace-url>//ui/hub/ext/com.dynatrace.extension.disk-devices#information`). The Disk Analytics extension consumes custom metrics and [Davis data units](https://www.dynatrace.com/support/help/shortlink/metric-cost-calculation).  After you have added the Disk Analytics extension, you can enable the Data Collection in host or host-group level settings. If you enable the Data Collection without adding the extension the data is only visible in the data explorer.  For details, see [Disk Analytics extension documentation](https://dt-url.net/3a03v9v).": "Функция Disk Analytics требует добавления расширения в окружение. Расширение Disk Analytics можно добавить из Dynatrace Hub (`<your-dynatrace-url>//ui/hub/ext/com.dynatrace.extension.disk-devices#information`). Расширение Disk Analytics расходует пользовательские метрики и [Davis data units](https://www.dynatrace.com/support/help/shortlink/metric-cost-calculation).  После добавления расширения Disk Analytics можно включить Data Collection в настройках уровня host или host-group. Если включить Data Collection без добавления расширения, данные будут видны только в data explorer.  Подробнее см. [Disk Analytics extension documentation](https://dt-url.net/3a03v9v).",
    # 4. virtualization-vmware
    "This string should have one of the following formats:  * $prefix(parameter) - property value starting with 'parameter' * $eq(parameter) - property value exactly matching 'parameter' * $suffix(parameter) - property value ends with 'parameter' * $contains(parameter) - property value contains 'parameter'": "Строка должна иметь один из форматов:  * $prefix(parameter) - значение свойства начинается с 'parameter' * $eq(parameter) - значение свойства точно совпадает с 'parameter' * $suffix(parameter) - значение свойства заканчивается на 'parameter' * $contains(parameter) - значение свойства содержит 'parameter'",
    # 5. mainframe-mqfilters
    "When you add a transaction ID to the include list, all the remaining transactions are ignored.": "Когда вы добавляете ID транзакции в список включения, все остальные транзакции игнорируются.",
    "When you add a transaction ID to the exclude list remaining transactions are still monitored.": "Когда вы добавляете ID транзакции в список исключения, остальные транзакции продолжают мониториться.",
    # 6. rum-user-experience-score
    "User experience is considered Frustrating when the selected percentage or more of the user actions in a session are rated as Frustrating.": "User experience считается Frustrating, когда выбранный процент или больше пользовательских действий в сессии оценены как Frustrating.",
    "User experience is considered Satisfying when at least the selected percentage of the user actions in a session are rated as Satisfying.": "User experience считается Satisfying, когда минимум выбранный процент пользовательских действий в сессии оценены как Satisfying.",
    # 8. rum-web-key-performance-metric-custom-actions
    "If **User action duration** is below this value, the action is assigned to the Satisfied performance zone.": "Если **User action duration** ниже этого значения, действие относится к зоне производительности Satisfied.",
    "If **User action duration** is above this value, the action is assigned to the Frustrated performance zone.": "Если **User action duration** выше этого значения, действие относится к зоне производительности Frustrated.",
    # 9. dt-javascript-runtime-app-monitoring
    "You can override the default monitoring setting for each app separately": "Можно переопределить настройку мониторинга по умолчанию для каждого приложения отдельно",
    # 10. exclude-network-traffic
    'Selecting a network interface, you will exclude all network traffic on that interface from being monitored. You can select from the list below what to not monitor, or input it manually using the "other one" option.': 'Выбирая сетевой интерфейс, вы исключите весь сетевой трафик на этом интерфейсе из мониторинга. Можно выбрать из списка ниже что не мониторить или ввести вручную через опцию "other one".',
    "Providing a host IP address, you will exclude network traffic only in calculating connectivity (other metrics will still be calculated).": "При указании IP-адреса хоста сетевой трафик исключается только при расчёте connectivity (другие метрики всё равно рассчитываются).",
    # 12. deployment-oneagent-updates
    "Select an update window for OneAgent updates (`<your-dynatrace-url>//ui/settings/builtin:deployment.management.update-windows`)": "Выберите окно обновления для обновлений OneAgent (`<your-dynatrace-url>//ui/settings/builtin:deployment.management.update-windows`)",
    # 13. rum-mobile-key-performance-metrics
    "Treat user actions with reported errors or web request errors as erroneous and rate their performance as Frustrating. Turn off this setting if errors should not affect the Apdex rate.": "Считать пользовательские действия с сообщёнными ошибками или ошибками web-запросов ошибочными и оценивать их производительность как Frustrating. Отключите эту настройку, если ошибки не должны влиять на показатель Apdex.",
    "If the action duration is below this value, the Apdex is considered to be **Satisfactory**.": "Если длительность действия ниже этого значения, Apdex считается **Satisfactory**.",
    "If the action duration is above this value, the Apdex is considered to be **Frustrating**.": "Если длительность действия выше этого значения, Apdex считается **Frustrating**.",
    # 14. host-monitoring-mode — large enum-prefix desc
    "Dynatrace OneAgent allows you to monitor every aspect of your environment, including all processes, services, and applications detected on your hosts.  OneAgent monitoring modes give you flexibility to adjust which capabilities of OneAgent are enabled for your host. Each successive mode increases the enabled capabilities, but also increases license consumption. To learn more, visit [Monitoring consumption](https://www.dynatrace.com/support/help/shortlink/monitoring-consumption).  Monitoring mode will be applied to a process after its restart.  The OneAgent's monitoring mode will automatically overwrite this setting whenever it is changed with [oneagentctl](https://dt-url.net/oneagentctl) or the OneAgent comes online.": "Dynatrace OneAgent позволяет мониторить любой аспект окружения, включая все процессы, сервисы и приложения, обнаруженные на хостах.  Режимы мониторинга OneAgent дают гибкость в выборе того, какие возможности OneAgent включены для хоста. Каждый последующий режим увеличивает включённые возможности, но также увеличивает потребление лицензии. Подробнее см. [Monitoring consumption](https://www.dynatrace.com/support/help/shortlink/monitoring-consumption).  Режим мониторинга применяется к процессу после его перезапуска.  Режим мониторинга OneAgent автоматически перезаписывает эту настройку при изменении через [oneagentctl](https://dt-url.net/oneagentctl) или при подключении OneAgent.",
    # 15. rum-web-resource-types
    "The regular expression to detect the resource.": "Регулярное выражение для определения ресурса.",
    # 17. rum-custom-enablement (BOM stripped)
    "Capture and analyze all user actions within your application. Enable [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq) to monitor and improve your application's performance, identify errors, and gain insight into your user's behavior and experience.": "Захватывайте и анализируйте все пользовательские действия в приложении. Включите [Real User Monitoring (RUM)](https://dt-url.net/1n2b0prq), чтобы мониторить и улучшать производительность приложения, выявлять ошибки и получать представление о поведении и опыте пользователей.",
    # 17. rum-custom-enablement — triple-mojibake `applicationâ€™s` (= application + Q + s)
    "Percentage of user sessions captured and analyzed  By default, Dynatrace captures all user actions and user sessions for analysis. This approach ensures complete insight into your application"
    + Q
    + "s performance and customer experience. You can optionally reduce the granularity of user-action and user-session analysis by capturing a lower percentage of user sessions. While this approach can reduce monitoring costs, it also results in lower visibility into how your customers are using your applications. For example, a setting of 10% results in Dynatrace analyzing only every tenth user session.": "Процент захваченных и проанализированных пользовательских сессий.  По умолчанию Dynatrace захватывает все пользовательские действия и сессии для анализа. Это обеспечивает полное представление о производительности приложения и пользовательском опыте. При желании можно снизить детализацию анализа пользовательских действий и сессий, захватывая меньший процент сессий. Это уменьшит стоимость мониторинга, но снизит видимость того, как клиенты используют приложения. Например, при значении 10% Dynatrace анализирует только каждую десятую пользовательскую сессию.",
    # 19. mainframe-txstartfilters — identical desc 4×
    "You can use \\* as wildcard. For example use A\\* to trace all transaction IDs that start with A.": "Можно использовать \\* как wildcard. Например, A\\* трассирует все ID транзакций, начинающиеся с A.",
    # 20. span-capturing + 27. span-entry-points
    "evaluated at span start": "вычисляется в начале span",
    "affects value": "влияет на значение",
    "affects value and key": "влияет на значение и ключ",
    # 23. rum-web-injection-cookie
    "If your application is only accessible via SSL, you can add the Secure attribute to all cookies set by Dynatrace. This setting prevents the display of warnings from PCI-compliance security scanners. Be aware that with this setting enabled Dynatrace correlation of user actions with server-side web requests is only possible over SSL connections.": "Если приложение доступно только по SSL, можно добавить атрибут Secure ко всем cookie, устанавливаемым Dynatrace. Это предотвращает отображение предупреждений от сканеров безопасности PCI-compliance. Учтите: при включении этой настройки корреляция пользовательских действий с серверными web-запросами возможна только через SSL-соединения.",
    "Define if your cookie should be restricted to a first-party or same-site context. Learn more about [SameSite cookies and available values](https://dt-url.net/yds1p8u).": "Определите, должен ли cookie быть ограничен first-party или same-site контекстом. Подробнее см. [SameSite cookies and available values](https://dt-url.net/yds1p8u).",
    "Specify an alternative domain for cookies set by Dynatrace. Keep in mind that your browser may not allow placement of cookies on certain domains (for example, top-level domains). Before typing a domain name here, confirm that the domain will accept cookies from your browser. For details, see the list of [forbidden top-level domains](https://dt-url.net/9n6b0pfz).": "Укажите альтернативный домен для cookie, устанавливаемых Dynatrace. Учтите: браузер может не разрешать размещение cookie на определённых доменах (например, top-level доменах). Перед вводом доменного имени убедитесь, что домен принимает cookie от вашего браузера. Подробнее см. список [forbidden top-level domains](https://dt-url.net/9n6b0pfz).",
    # 24. anomaly-detection-frequent-issues
    "Events raised at this level typically occur when no specific topological entity is applicable, often based on data such as logs and metrics. This does not impact the detection of issues within applications, transactions, services, or infrastructure.": "События, поднимаемые на этом уровне, обычно возникают, когда не применима конкретная топологическая сущность, часто на основе данных типа логов и метрик. Это не влияет на обнаружение проблем внутри приложений, транзакций, сервисов или инфраструктуры.",
    # 25. availability-process-group-alerting — large enum-prefix desc
    "**if any process becomes unavailable:** Dynatrace will open a new problem if a single process in this group shuts down or crashes.  **if minimum threshold is not met:** Dynatrace tracks the number of process instances that comprise this process group and treats the group as a cluster. This setting enables you to define a minimum number of process instances that must be available. A problem will be opened if this process group has fewer than the minimum number of required process instances.  Details of the related impact on service requests will be included in the problem summary.  **Note:** If a process is intentionally shutdown or retired while this setting is active, you'll need to manually close the problem.": "**если любой процесс становится недоступным:** Dynatrace откроет новую проблему, если один процесс в этой группе остановится или упадёт.  **если минимальный порог не достигнут:** Dynatrace отслеживает количество инстансов процесса, составляющих эту process group, и рассматривает группу как кластер. Эта настройка позволяет задать минимальное количество инстансов процесса, которые должны быть доступны. Проблема будет открыта, если в этой process group меньше требуемого минимального количества инстансов процесса.  Детали влияния на сервисные запросы будут включены в сводку проблемы.  **Примечание:** если процесс намеренно остановлен или выведен из эксплуатации при активной настройке, вам нужно вручную закрыть проблему.",
    # 26. apis-detection-rules
    "This color will be used to highlight APIs when viewing code level data, such as distributed traces or method hotspots.": "Этот цвет используется для выделения API при просмотре данных уровня кода, например distributed trace'ов или method hotspot'ов.",
    "Restrict this rule to a specific technology.": "Ограничить это правило конкретной технологией.",
    # 28. attribute-masking
    "If this is true, the masking of the specified key is applied.": "Если true, применяется маскирование указанного ключа.",
    "Key of the attribute": "Ключ атрибута",
    "Set a masking strategy to conceal its value from users  Choose **Mask entire value** to hide the whole value of this attribute from everyone who does not have 'View sensitive request data' permission. These attributes can't be used to define other configurations.  Choose **Mask only confidential data** to apply automatic masking strategies to your data. These strategies include, for example, credit card numbers, IBAN, IPs, email-addresses, etc. It may not be possible to recognize all sensitive data so please always make sure to verify that sensitive data is actually masked. If sensitive data is not recognized, please use **Mask entire value** instead. Users with 'View sensitive request data' permission will be able to see the entire value, others only the non-sensitive parts. These attributes can't be used to define other configurations.": "Задайте стратегию маскирования, чтобы скрыть значение от пользователей.  Выберите **Mask entire value**, чтобы полностью скрыть значение этого атрибута от всех, у кого нет права 'View sensitive request data'. Такие атрибуты нельзя использовать для определения других конфигураций.  Выберите **Mask only confidential data**, чтобы применить автоматические стратегии маскирования. Стратегии охватывают, например, номера кредитных карт, IBAN, IP, email-адреса и т.п. Распознать все чувствительные данные может быть невозможно, поэтому всегда проверяйте, что чувствительные данные действительно замаскированы. Если чувствительные данные не распознаны, используйте **Mask entire value**. Пользователи с правом 'View sensitive request data' увидят значение целиком; остальные видят только нечувствительные части. Такие атрибуты нельзя использовать для определения других конфигураций.",
    # 29. service-splitting-rules
    "If enabled, the rule will be evaluated.": "Если включено, правило будет вычисляться.",
    "Limits the scope of the service splitting rule using [DQL matcher](https://dt-url.net/l603wby) conditions on resource attributes.  A rule is applied only if the condition matches, otherwise the ruleset evaluation continues.  If empty, the condition will always match.": "Ограничивает область правила разделения сервисов через условия [DQL matcher](https://dt-url.net/l603wby) на атрибутах ресурсов.  Правило применяется только если условие совпало, иначе вычисление набора правил продолжается.  Если поле пустое, условие всегда совпадает.",
    "Define the entire set of resource attributes that should split your services in the matching scope.  Each attribute that exists will contribute to the final service ID.": "Задайте полный набор атрибутов ресурсов, по которым следует разделять сервисы в области сопоставления.  Каждый существующий атрибут вносит вклад в финальный ID сервиса.",
    # 30. rum-web-custom-errors
    "This setting overrides Apdex settings for individual rules listed below": "Эта настройка переопределяет настройки Apdex для отдельных правил, перечисленных ниже",
    "A case-insensitive key pattern": "Шаблон ключа, нечувствительный к регистру",
    "A case-insensitive value pattern": "Шаблон значения, нечувствительный к регистру",
    "[View more details](https://dt-url.net/hd580p2k)": "[View more details](https://dt-url.net/hd580p2k)",
    # 31. bizevents-processing-pipelines-rule
    "Sample event to use for the test run. Only JSON format is supported.": "Образец события для тестового прогона. Поддерживается только формат JSON.",
    # 32. process-group-simple-detection-rule
    "Source to use to separate processes into multiple process groups.": "Источник для разделения процессов на несколько process group.",
    "If Dynatrace detects this property at startup of a process, it will use its value to identify process groups more granular.": "Если Dynatrace обнаружит это свойство при запуске процесса, он использует его значение для более детальной идентификации process group.",
    "Use a variable to identify instances within a process group.  The type of variable is the same as selected in 'Property source'.": "Используйте переменную для идентификации инстансов внутри process group.  Тип переменной такой же, как выбранный в 'Property source'.",
    "Note: Not all types can be detected at startup.": "Примечание: не все типы могут быть обнаружены при запуске.",
    # 22. rum-processgroup — large prose
    "Allows OneAgent to:  * automatically inject the RUM JavaScript tag into each page delivered by this process group * provide the necessary info to correlate RUM data with server-side PurePaths * forward beacons to the cluster * deliver the monitoring code  If you don't enable this setting, your RUM data may not be correlated with your server-side PurePaths, which will be a problem when the root of the server-side PurePath is captured on this process group. For example, consider an Apache HTTP server as a proxy and a Java app server as a backend. Disabling this setting for the process group of the Apache HTTP server will break the RUM correlation, even if Dynatrace injects the RUM JavaScript tag on the process group of the Java backend. For RUM data to correlate with server-side PurePaths, RUM must be enabled on the OneAgent that instruments the entry point of your application (the Apache HTTP server in this example).": "Позволяет OneAgent:  * автоматически внедрять RUM JavaScript-тег в каждую страницу, отдаваемую этой process group * предоставлять информацию для корреляции RUM-данных с серверными PurePath'ами * пересылать beacon'ы в кластер * доставлять код мониторинга  Если эта настройка не включена, RUM-данные могут не коррелироваться с серверными PurePath'ами, что станет проблемой, когда корень серверного PurePath захватывается на этой process group. Например, Apache HTTP-сервер как proxy и Java app-сервер как backend. Отключение этой настройки для process group Apache HTTP-сервера сломает RUM-корреляцию, даже если Dynatrace внедряет RUM JavaScript-тег в process group Java-backend. Чтобы RUM-данные коррелировались с серверными PurePath'ами, RUM должен быть включён на OneAgent, инструментирующем точку входа приложения (Apache HTTP-сервер в этом примере).",
}

# Structural canon (shared with L4-AG.1a.1-4 / L4-AF).
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
    # Empty label (col-1 starts with backtick) is allowed; just translate cdesc.
    if label and label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL.get(label, label)
    d = cdesc
    # ENUM substring-replace runs BEFORE per-line so cdesc may already have RU marker.
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
        print("%-65s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
