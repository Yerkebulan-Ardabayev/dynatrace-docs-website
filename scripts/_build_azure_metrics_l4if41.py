#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""L4-IF.41 — RU build for the 28 "standard" Azure metric files (app/integration/
messaging/IoT/misc families), finishing all std-layout leafs of
azure-cloud-services-metrics except builtin-*/irregular (next batch).

Chain: imports L4-IF.40 wrapper (-> 38 -> 37); base DESC/UNIT/REC/HEADER/DATE/
PROSE/EXACT_LINE win for shared strings; this batch adds its own on top.

New vs L4-IF.40:
  * COLMAP_OVERRIDE — two files ship broken EN headers where the header order
    does not match the data order (mesh-application: Unit<->Dimensions swapped;
    stream-analytics: Dimensions<->Description swapped). Headers stay translated
    by their literal cell text (canon: container-registry L4-IF.40), data cells
    are translated by their FACTUAL meaning via the override colmap.
  * Two extra Recommended header labels (time-series-insights has two
    Recommended columns, Environment / Event Source).

Canon: Description/Unit/Recommended + header labels translated; Name +
Dimensions stay EN (Azure Metrics API identifiers). Image alt + captions stay
EN byte-identical. H3 product-name sub-table headings stay EN (anchor fidelity,
L4-IF.33). throttled -> "подвергнутые регулированию" (Cosmos DB shipped canon).
topic -> "топик" (corpus 67x). deprecated -> "(устарело)" (GCP shipped canon).
No em-dash (CLAUDE.md §0).

Source-quirks kept/flagged (fidelity):
  * front-door "HTTP/S proxyMySQL" (EN concatenation slip) — RU renders the
    metric meaning ("HTTP/S-прокси"), the garbage token is not mirrored.
  * api-management "(depracated)" EN typo -> RU "(устаревший)".
  * media-service "content key polices" EN typo -> RU normal plural.
  * cache-for-redis "The number errors" EN slip -> RU normal grammar.
"""

import os
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "e40", os.path.join(os.path.dirname(__file__), "_build_azure_metrics_l4if40.py")
)
e40 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(e40)

EN_DIR = e40.EN_DIR
RU_DIR = e40.RU_DIR

BATCH = [
    "monitor-azure-api-management-service.md",
    "monitor-azure-app-configuration.md",
    "monitor-azure-application-gateway.md",
    "monitor-azure-automation-account.md",
    "monitor-azure-batch.md",
    "monitor-azure-blockchain-service.md",
    "monitor-azure-cache-for-redis.md",
    "monitor-azure-cognitive-services-ink-recognizer.md",
    "monitor-azure-event-grid.md",
    "monitor-azure-event-hubs.md",
    "monitor-azure-front-door.md",
    "monitor-azure-front-door-cdn-profiles.md",
    "monitor-azure-integration-service-environment.md",
    "monitor-azure-iot-central-applications.md",
    "monitor-azure-iot-hub.md",
    "monitor-azure-device-provisioning-service.md",
    "monitor-azure-key-vault.md",
    "monitor-azure-logic-apps.md",
    "monitor-azure-maps-account.md",
    "monitor-azure-media-service.md",
    "monitor-azure-mesh-application.md",
    "monitor-azure-notification-hub.md",
    "monitor-azure-power-bi.md",
    "monitor-azure-recovery-services-vault.md",
    "monitor-azure-search.md",
    "monitor-azure-signalr.md",
    "monitor-azure-stream-analytics.md",
    "monitor-azure-time-series-insights.md",
]

TITLE_MAP = {
    "monitor-azure-api-management-service.md": (
        "Azure API Management Service monitoring",
        "Мониторинг Azure API Management Service",
    ),
    "monitor-azure-app-configuration.md": (
        "Azure App Configuration monitoring",
        "Мониторинг Azure App Configuration",
    ),
    "monitor-azure-application-gateway.md": (
        "Azure Application Gateway monitoring",
        "Мониторинг Azure Application Gateway",
    ),
    "monitor-azure-automation-account.md": (
        "Azure Automation Account monitoring",
        "Мониторинг Azure Automation Account",
    ),
    "monitor-azure-batch.md": (
        "Azure Batch monitoring",
        "Мониторинг Azure Batch",
    ),
    "monitor-azure-blockchain-service.md": (
        "Azure Blockchain monitoring",
        "Мониторинг Azure Blockchain",
    ),
    "monitor-azure-cache-for-redis.md": (
        "Azure Cache for Redis monitoring",
        "Мониторинг Azure Cache for Redis",
    ),
    "monitor-azure-cognitive-services-ink-recognizer.md": (
        "Azure Cognitive Services - Ink Recognizer monitoring (deprecated)",
        "Мониторинг Azure Cognitive Services - Ink Recognizer (устарело)",
    ),
    "monitor-azure-event-grid.md": (
        "Azure Event Grid (Domain Topics, Topics, System Topics) monitoring",
        "Мониторинг Azure Event Grid (Domain Topics, Topics, System Topics)",
    ),
    "monitor-azure-event-hubs.md": (
        "Azure Event Hubs (Clusters) monitoring",
        "Мониторинг Azure Event Hubs (Clusters)",
    ),
    "monitor-azure-front-door.md": (
        "Azure Front Door (classic) monitoring",
        "Мониторинг Azure Front Door (classic)",
    ),
    "monitor-azure-front-door-cdn-profiles.md": (
        "Azure Front Door Standard/Premium and CDN profiles monitoring",
        "Мониторинг Azure Front Door Standard/Premium и CDN profiles",
    ),
    "monitor-azure-integration-service-environment.md": (
        "Azure Integration Service Environment monitoring",
        "Мониторинг Azure Integration Service Environment",
    ),
    "monitor-azure-iot-central-applications.md": (
        "Azure IoT Central Applications monitoring",
        "Мониторинг Azure IoT Central Applications",
    ),
    "monitor-azure-iot-hub.md": (
        "Azure IoT Hub monitoring",
        "Мониторинг Azure IoT Hub",
    ),
    "monitor-azure-device-provisioning-service.md": (
        "Azure Device Provisioning Service monitoring",
        "Мониторинг Azure Device Provisioning Service",
    ),
    "monitor-azure-key-vault.md": (
        "Azure Key Vault monitoring",
        "Мониторинг Azure Key Vault",
    ),
    "monitor-azure-logic-apps.md": (
        "Azure Logic Apps monitoring",
        "Мониторинг Azure Logic Apps",
    ),
    "monitor-azure-maps-account.md": (
        "Azure Maps Account monitoring",
        "Мониторинг Azure Maps Account",
    ),
    "monitor-azure-media-service.md": (
        "Azure Media Services monitoring",
        "Мониторинг Azure Media Services",
    ),
    "monitor-azure-mesh-application.md": (
        "Azure Mesh Application monitoring",
        "Мониторинг Azure Mesh Application",
    ),
    "monitor-azure-notification-hub.md": (
        "Azure Notification Hub monitoring",
        "Мониторинг Azure Notification Hub",
    ),
    "monitor-azure-power-bi.md": (
        "Azure Power BI Embedded monitoring",
        "Мониторинг Azure Power BI Embedded",
    ),
    # pure product name, no "monitoring" verb part -> stays EN (canon: product
    # names untranslated; the same string is whitelisted in PASS_EN below)
    "monitor-azure-recovery-services-vault.md": (
        "Azure Recovery Services Vault",
        "Azure Recovery Services Vault",
    ),
    "monitor-azure-search.md": (
        "Azure Search Service monitoring",
        "Мониторинг Azure Search Service",
    ),
    "monitor-azure-signalr.md": (
        "Monitor Azure SignalR",
        "Мониторинг Azure SignalR",
    ),
    "monitor-azure-stream-analytics.md": (
        "Azure Stream Analytics monitoring",
        "Мониторинг Azure Stream Analytics",
    ),
    "monitor-azure-time-series-insights.md": (
        "Azure Time Series Insights (Environment, Event Source) monitoring",
        "Мониторинг Azure Time Series Insights (Environment, Event Source)",
    ),
}

DATE_MAP = dict(e40.DATE_MAP)
DATE_MAP.update(
    {
        "* Published Jun 19, 2024": "* Опубликовано 19 июня 2024 г.",
        "* Published Mar 07, 2024": "* Опубликовано 7 марта 2024 г.",
        "* Published Sep 10, 2020": "* Опубликовано 10 сентября 2020 г.",
        "* Published Sep 17, 2020": "* Опубликовано 17 сентября 2020 г.",
        "* Updated on Sep 27, 2023": "* Обновлено 27 сентября 2023 г.",
    }
)

PROSE = list(e40.PROSE) + [
    ("* 7-min read", "* Чтение: 7 мин"),
    ("* 10-min read", "* Чтение: 10 мин"),
    ("* 23-min read", "* Чтение: 23 мин"),
]

HEADER_LABEL = dict(e40.HEADER_LABEL)
HEADER_LABEL.update(
    {
        # time-series-insights: two Recommended columns; Environment / Event
        # Source are entity names of the service (EN in the page title too)
        "Recommended (Environment)": "Рекомендуется (Environment)",
        "Recommended (Event Source)": "Рекомендуется (Event Source)",
    }
)
REC_MAP = dict(e40.REC_MAP)
UNIT_MAP = dict(e40.UNIT_MAP)

# ---- broken EN headers: header text order != data order. Headers stay
# translated by literal text; data cells use the FACTUAL column meaning. ----
COLMAP_OVERRIDE = {
    # header: | Name | Description | Unit | Dimensions | Recommended |
    # data:   | Name | Description | DIMS | UNIT       | Recommended |
    "monitor-azure-mesh-application.md": [
        "Name",
        "Description",
        "Dimensions",
        "Unit",
        "Recommended",
    ],
    # header: | Name | Dimensions | Description | Unit | Recommended |
    # data:   | Name | DESC       | DIMS        | Unit | Recommended |
    "monitor-azure-stream-analytics.md": [
        "Name",
        "Description",
        "Dimensions",
        "Unit",
        "Recommended",
    ],
}

# ---- full-line overrides (applied before any substring replace) ----
EXACT_LINE = dict(e40.EXACT_LINE)
EXACT_LINE.update(
    {
        # api-management ("(depracated)" is an EN typo for deprecated)
        "This service monitors a part of Azure API Management (Microsoft.ApiManagement/service). While you have this service configured, you can't have Azure Application Service (built-in) (depracated) service turned on.": "Этот сервис отслеживает часть Azure API Management (Microsoft.ApiManagement/service). Пока этот сервис настроен, вы не можете включить сервис Azure Application Service (built-in) (устаревший).",
        # application-gateway
        "This service monitors a part of Azure Application Gateway (Microsoft.Network/applicationGateways). While you have this service configured, you can't have Azure Application Gateway service turned on.": "Этот сервис отслеживает часть Azure Application Gateway (Microsoft.Network/applicationGateways). Пока этот сервис настроен, вы не можете включить сервис Azure Application Gateway.",
        # batch (verbatim reuse of the shipped data-warehouse RU sentence pair)
        "The Azure Batch overview page gives you a comprehensive view of how many jobs and tasks were completed over a period of time. You can also track nodes in different states, such as running, idle, or offline.": "Страница обзора Azure Batch даёт полное представление о том, сколько заданий и задач было выполнено за период времени. Вы также можете отслеживать узлы в различных состояниях, таких как работающие, простаивающие или отключённые.",
        # cache-for-redis
        "This service monitors a part of Azure Cache for Redis (`Microsoft.Cache/redis`).": "Этот сервис отслеживает часть Azure Cache for Redis (`Microsoft.Cache/redis`).",
        "While you have this service configured, you **can't** have Azure Redis Cache (built-in) service turned on.": "Пока этот сервис настроен, вы **не можете** включить сервис Azure Redis Cache (built-in).",
        "Enterprise Azure Cache for Redis service (`Microsoft.Cache/redisEnterprise`) currently cannot be monitored; to request this type of monitoring, please create an RFE (Request for Enhancement).": "Сервис Enterprise Azure Cache for Redis (`Microsoft.Cache/redisEnterprise`) в настоящее время не может отслеживаться; чтобы запросить этот тип мониторинга, создайте RFE (Request for Enhancement).",
        # front-door (classic)
        "The Azure Front Door (classic) overview page gives you visibility into the number of served client requests, latency, and the efficiency of your routing.": "Страница обзора Azure Front Door (classic) даёт представление о количестве обслуженных клиентских запросов, задержке и эффективности вашей маршрутизации.",
        "This service monitors previous (classic) offering of [Azure Front Door](https://dt-url.net/rz0390g).": "Этот сервис отслеживает предыдущее (классическое) предложение [Azure Front Door](https://dt-url.net/rz0390g).",
        'For information regarding the latest Microsoft [Azure Front Door Standard and Premium](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview) service, `Front Door and CDN profile`, see [Azure Front Door Standard/Premium and CDN profiles monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles "Monitor Azure Front Door Standard/Premium and CDN profiles and view available metrics.").': 'Информацию о новейшем сервисе Microsoft [Azure Front Door Standard and Premium](https://learn.microsoft.com/en-us/azure/frontdoor/front-door-overview), `Front Door and CDN profile`, см. в разделе [Мониторинг Azure Front Door Standard/Premium и CDN profiles](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door-cdn-profiles "Мониторинг Azure Front Door Standard/Premium и CDN profiles, просмотр доступных метрик.").',
        # front-door-cdn-profiles
        "The Azure Front Door Standard/Premium, and CDN profiles overview pages give you visibility into the number of served client requests, latency, and the efficiency of your routing.": "Страницы обзора Azure Front Door Standard/Premium и CDN profiles дают представление о количестве обслуженных клиентских запросов, задержке и эффективности вашей маршрутизации.",
        'For information regarding the previous (classic) offering of Microsoft [Azure Front Door](https://dt-url.net/rz0390g), see [Azure Front Door (classic) monitoring](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door "Monitor Azure Front Door (classic) and view available metrics.").': 'Информацию о предыдущем (классическом) предложении Microsoft [Azure Front Door](https://dt-url.net/rz0390g) см. в разделе [Мониторинг Azure Front Door (classic)](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics/monitor-azure-front-door "Мониторинг Azure Front Door (classic) и просмотр доступных метрик.").',
        # integration-service-environment
        "Azure Integration Service Environment can be connected with Azure Logic Apps. For more information, see [Connect to Azure virtual networks from Azure Logic Apps by using an integration service environment](https://docs.microsoft.com/en-us/azure/logic-apps/connect-virtual-network-vnet-isolated-environment).": "Azure Integration Service Environment можно подключить к Azure Logic Apps. Дополнительную информацию см. в разделе [Подключение к виртуальным сетям Azure из Azure Logic Apps с помощью среды Integration Service Environment](https://docs.microsoft.com/en-us/azure/logic-apps/connect-virtual-network-vnet-isolated-environment).",
        "**Dashboard for Azure Integration Service Environment with Azure Logic Apps**": "**Дашборд для Azure Integration Service Environment с Azure Logic Apps**",
        # iot-hub
        "This service monitors a part of Azure IoT Hub (Microsoft.Devices/IotHubs). While you have this service configured, you can't have Azure Iot Hub (built-in) service turned on.": "Этот сервис отслеживает часть Azure IoT Hub (Microsoft.Devices/IotHubs). Пока этот сервис настроен, вы не можете включить сервис Azure Iot Hub (built-in).",
        # device-provisioning-service
        "The Device Provisioning Service instance needs to be linked to IoT Hubs in order to be able to create group and individual enrollments.": "Экземпляр Device Provisioning Service должен быть связан с IoT-хабами, чтобы можно было создавать групповые и индивидуальные регистрации.",
        # logic-apps
        "Logic Apps created on the Standard Plan are supported using the Azure App Services (built-in) service, **not** the Logic App service. You can find it on the Azure overview page, **Functions** view.": "Logic Apps, созданные по плану Standard, поддерживаются через сервис Azure App Services (built-in), а **не** через сервис Logic App. Найти его можно на странице обзора Azure в представлении **Functions**.",
        # mesh-application (retired canon: "выведен из эксплуатации")
        "This service has been retired by Microsoft. For more information, see the [Microsoft announcement](https://azure.microsoft.com/en-us/updates/azure-service-fabric-mesh-preview-retirement/).": "Этот сервис выведен Microsoft из эксплуатации. Дополнительную информацию см. в [объявлении Microsoft](https://azure.microsoft.com/en-us/updates/azure-service-fabric-mesh-preview-retirement/).",
    }
)

# ---- deliberately-EN pass-through lines (leftover-scan whitelist) ----
PASS_EN = set(e40.PASS_EN)
PASS_EN.update(
    {
        # image captions (shipped canon: stay EN byte-identical)
        "App config",
        "Auto acc",
        "Azure batch dash",
        "Blockchain",
        "Cognitive services",
        "Eventgrid dash",
        "Topics",
        "System",
        "Eventhub",
        "Frontdoor dash",
        "Azure Front Door Standard and Premium",
        "Azure Front Door CDN profiles",
        "Azure Integration Service Environment",
        "Azure Integration Service Environment + Logic Apps",
        "IoT",
        "Device provisioning",
        "Key vault",
        "Logic apps",
        "Maps dash",
        "Media serv",
        "Mesh",
        "Notification hub",
        "Power bi",
        "Search",
        "Signalr",
        "Stream",
        "Timeseries",
        "Time series event sources",
        # H3 sub-table headings: pure product names (EN canon + anchor fidelity)
        "### Azure Event Grid Domain Topics",
        "### Azure Event Grid Topics",
        "### Azure Event Grid System Topics",
        "### Azure Front Door Standard/Premium",
        "### Azure Front Door CDN profiles",
        # recovery-services-vault: title/H1 = pure product name, stays EN
        "# Azure Recovery Services Vault",
    }
)

# ---- batch Description cells (EN exact -> RU); base maps win for shared ----
NEW_DESC = {
    # --- api-management-service ---
    "Overall Duration of Gateway Requests in milliseconds": "Общая длительность запросов шлюза в миллисекундах",
    "Duration of Backend Requests in milliseconds": "Длительность запросов к бэкенду в миллисекундах",
    "Utilization metric for ApiManagement service. Note: For skus other than Premium, 'Max' aggregation will show the value as 0.": "Метрика использования для сервиса ApiManagement. Примечание: для SKU, отличных от Premium, агрегация 'Max' покажет значение 0.",
    "Number of events sent to EventHub": "Количество событий, отправленных в EventHub",
    "Number of successful EventHub events": "Количество успешных событий EventHub",
    "Number of failed EventHub events": "Количество неудачных событий EventHub",
    "Number of rejected EventHub events (wrong configuration or unauthorized)": "Количество отклонённых событий EventHub (неверная конфигурация или отсутствие авторизации)",
    "Number of throttled EventHub events": "Количество событий EventHub, подвергнутых регулированию",
    "Number of timed out EventHub events": "Количество событий EventHub с истёкшим временем ожидания",
    "Number of events skipped because of queue size limit reached": "Количество событий, пропущенных из-за достижения лимита размера очереди",
    "Total size of EventHub events in bytes": "Общий размер событий EventHub в байтах",
    "Gateway request metrics with multiple dimensions": "Метрики запросов шлюза с несколькими измерениями",
    "Network Connectivity status of dependent resource types from API Management service": "Статус сетевой связности зависимых типов ресурсов со стороны сервиса API Management",
    "Count of WebSocket messages based on selected source and destination": "Количество сообщений WebSocket по выбранному источнику и назначению",
    "Count of WebSocket connection attempts based on selected source and destination": "Количество попыток подключения WebSocket по выбранному источнику и назначению",
    # --- app-configuration ---
    "Total number of incoming HTTP requests": "Общее количество входящих HTTP-запросов",
    "Latency on an HTTP request": "Задержка HTTP-запроса",
    "Throttled HTTP requests": "HTTP-запросы, подвергнутые регулированию",
    # --- application-gateway ---
    "Number of bytes per second the Application Gateway has served": "Количество байтов в секунду, обслуженных Application Gateway",
    "Number of unhealthy backend hosts": "Количество неработоспособных хостов бэкенда",
    "Number of healthy backend hosts": "Количество работоспособных хостов бэкенда",
    "Count of successful requests that Application Gateway has served": "Количество успешных запросов, обслуженных Application Gateway",
    "Average request count per minute per healthy backend host in a pool": "Среднее количество запросов в минуту на работоспособный хост бэкенда в пуле",
    "Count of failed requests that Application Gateway has served": "Количество неудачных запросов, обслуженных Application Gateway",
    "Http response status returned by Application Gateway": "Статус HTTP-ответа, возвращённый Application Gateway",
    "Count of current connections established with Application Gateway": "Количество текущих подключений, установленных с Application Gateway",
    "Current CPU utilization of the Application Gateway": "Текущее использование ЦП Application Gateway",
    "New connections per second established with Application Gateway": "Новые подключения в секунду, установленные с Application Gateway",
    "Capacity Units consumed": "Потреблённые единицы ёмкости",
    "Minimum capacity units that will be charged": "Минимальные единицы ёмкости, за которые будет начислена плата",
    "Estimated capacity units that will be charged": "Расчётные единицы ёмкости, за которые будет начислена плата",
    "Compute Units consumed": "Потреблённые вычислительные единицы",
    "The number of HTTP response codes generated by the backend members. This does not include any response codes generated by the Application Gateway.": "Количество кодов HTTP-ответов, сгенерированных участниками бэкенда. Не включает коды ответов, сгенерированные Application Gateway.",
    "The number of TLS and non-TLS requests initiated by the client that established connection with the Application Gateway. To view TLS protocol distribution, filter by the dimension TLS Protocol.": "Количество TLS- и не-TLS-запросов, инициированных клиентом, установившим подключение с Application Gateway. Для просмотра распределения протоколов TLS отфильтруйте по измерению TLS Protocol.",
    "The total number of bytes sent by the Application Gateway to the clients": "Общее количество байтов, отправленных Application Gateway клиентам",
    "The total number of bytes received by the Application Gateway from the clients": "Общее количество байтов, полученных Application Gateway от клиентов",
    "Round trip time between clients and Application Gateway. This metric indicates how long it takes to establish connections and return acknowledgements": "Время кругового пути между клиентами и Application Gateway. Эта метрика показывает, сколько времени занимает установка подключений и возврат подтверждений",
    "Time that it takes for a request to be processed and its response to be sent. This is the interval from the time when Application Gateway receives the first byte of an HTTP request to the time when the response send operation finishes. It's important to note that this usually includes the Application Gateway processing time, time that the request and response packets are traveling over the network and the time the backend server took to respond.": "Время, которое требуется для обработки запроса и отправки его ответа. Это интервал от момента, когда Application Gateway получает первый байт HTTP-запроса, до момента завершения операции отправки ответа. Важно отметить, что обычно это включает время обработки Application Gateway, время прохождения пакетов запроса и ответа по сети и время, которое потребовалось серверу бэкенда для ответа.",
    "Time spent establishing a connection with a backend server": "Время, затраченное на установку подключения с сервером бэкенда",
    "Time interval between start of establishing a connection to backend server and receiving the first byte of the response header, approximating processing time of backend server": "Интервал времени между началом установки подключения к серверу бэкенда и получением первого байта заголовка ответа, приблизительно соответствующий времени обработки сервером бэкенда",
    "Time interval between start of establishing a connection to backend server and receiving the last byte of the response body": "Интервал времени между началом установки подключения к серверу бэкенда и получением последнего байта тела ответа",
    "Web Application Firewall Total Rule Distribution for the incoming traffic": "Общее распределение правил Web Application Firewall для входящего трафика",
    "Web Application Firewall blocked requests rule distribution": "Распределение правил Web Application Firewall по заблокированным запросам",
    # --- automation-account ---
    "Total number of jobs": "Общее количество заданий",
    "Total software update deployment machine runs in a software update deployment run": "Общее количество запусков обновления ПО на машинах в рамках запуска развёртывания обновления ПО",
    "Total software update deployment runs": "Общее количество запусков развёртывания обновлений ПО",
    # --- batch ---
    "Total number of dedicated cores in the batch account": "Общее количество выделенных ядер в аккаунте Batch",
    "Number of nodes being created": "Количество создаваемых узлов",
    "Number of idle nodes": "Количество простаивающих узлов",
    "Total number of jobs that have been successfully deleted": "Общее количество успешно удалённых заданий",
    "Total number of jobs that have been requested to be deleted": "Общее количество заданий, для которых запрошено удаление",
    "Total number of jobs that have been successfully disabled": "Общее количество успешно отключённых заданий",
    "Total number of jobs that have been requested to be disabled": "Общее количество заданий, для которых запрошено отключение",
    "Total number of jobs that have been successfully started": "Общее количество успешно запущенных заданий",
    "Total number of jobs that have been successfully terminated": "Общее количество успешно завершённых заданий",
    "Total number of jobs that have been requested to be terminated": "Общее количество заданий, для которых запрошено завершение",
    "Number of nodes leaving the pool": "Количество узлов, покидающих пул",
    "Total number of low-priority cores in the batch account": "Общее количество низкоприоритетных ядер в аккаунте Batch",
    "Total number of low-priority nodes in the batch account": "Общее количество низкоприоритетных узлов в аккаунте Batch",
    "Number of offline nodes": "Количество отключённых узлов",
    "Total number of pools that have been created": "Общее количество созданных пулов",
    "Total number of pool deletes that have completed": "Общее количество завершённых удалений пулов",
    "Total number of pool deletes that have started": "Общее количество начатых удалений пулов",
    "Total number of pool resizes that have completed": "Общее количество завершённых изменений размера пулов",
    "Total number of pool resizes that have started": "Общее количество начатых изменений размера пулов",
    "Number of preempted nodes": "Количество вытесненных узлов",
    "Number of rebooting nodes": "Количество перезагружающихся узлов",
    "Number of reimaging nodes": "Количество узлов с переустановкой образа",
    "Number of running nodes": "Количество работающих узлов",
    "Number of nodes where the Start Task has failed": "Количество узлов, на которых стартовая задача завершилась сбоем",
    "Number of nodes starting": "Количество запускающихся узлов",
    "Total number of tasks that have completed": "Общее количество завершённых задач",
    "Total number of tasks that have completed in a failed state": "Общее количество задач, завершённых в состоянии сбоя",
    "Total number of tasks that have started": "Общее количество начатых задач",
    "Total number of dedicated nodes in the batch account": "Общее количество выделенных узлов в аккаунте Batch",
    "Number of unusable nodes": "Количество непригодных узлов",
    "Number of nodes waiting for the Start Task to complete": "Количество узлов, ожидающих завершения стартовой задачи",
    # --- blockchain-service ---
    "The number of accepted connections": "Количество принятых подключений",
    "The number of active connections": "Количество активных подключений",
    "The number of handled connections": "Количество обработанных подключений",
    "The block number of the latest block committed": "Номер последнего зафиксированного блока",
    "The number of IO read bytes": "Количество прочитанных байтов ввода-вывода",
    "The number of IO write bytes": "Количество записанных байтов ввода-вывода",
    "Memory limit": "Лимит памяти",
    "Memory usage": "Использование памяти",
    "The percentage of memory usage": "Процент использования памяти",
    "The number of pending transactions": "Количество ожидающих транзакций",
    "The number of processed blocks": "Количество обработанных блоков",
    "The number of processed transactions": "Количество обработанных транзакций",
    "The number of queued transactions": "Количество транзакций в очереди",
    "The number of handled requests": "Количество обработанных запросов",
    "Storage usage": "Использование хранилища",
    # --- cache-for-redis ---
    "The number of client connections to the cache.": "Количество клиентских подключений к кэшу.",
    "The total number of commands processed by the cache server.": "Общее количество команд, обработанных сервером кэша.",
    "The number of successful key lookups.": "Количество успешных поисков ключей.",
    "The number of failed key lookups.": "Количество неудачных поисков ключей.",
    "The % of get requests that miss.": "Процент запросов get, завершившихся промахом.",
    "The number of get operations from the cache.": "Количество операций get из кэша.",
    "The number of set operations to the cache.": "Количество операций set в кэш.",
    "The number of instantaneous operations per second executed on the cache.": "Количество мгновенных операций в секунду, выполняемых на кэше.",
    "The number of items evicted from the cache.": "Количество элементов, вытесненных из кэша.",
    "The total number of items in the cache.": "Общее количество элементов в кэше.",
    "The number of items expired from the cache.": "Количество элементов кэша с истёкшим сроком действия.",
    "The amount of cache memory used for key/value pairs in the cache in MB.": "Объём памяти кэша, используемой для пар ключ/значение в кэше, в МБ.",
    "The percentage of cache memory used for key/value pairs.": "Процент памяти кэша, используемой для пар ключ/значение.",
    "The amount of cache memory used in MB, including fragmentation and metadata.": "Объём используемой памяти кэша в МБ, включая фрагментацию и метаданные.",
    "The percentage of cycles in which the Redis server is busy processing and not waiting idle for messages.": "Процент циклов, в которых сервер Redis занят обработкой, а не простаивает в ожидании сообщений.",
    "The amount of data written to the cache in bytes per second.": "Объём данных, записываемых в кэш, в байтах в секунду.",
    "The amount of data read from the cache in bytes per second.": "Объём данных, читаемых из кэша, в байтах в секунду.",
    "The number of instantaneous connections created per second on the cache via port 6379 or 6380 (SSL).": "Количество мгновенных подключений, создаваемых в секунду на кэше через порт 6379 или 6380 (SSL).",
    "The number of instantaneous connections closed per second on the cache via port 6379 or 6380 (SSL).": "Количество мгновенных подключений, закрываемых в секунду на кэше через порт 6379 или 6380 (SSL).",
    "The CPU utilization of the Azure Redis Cache server as a percentage.": "Использование ЦП сервера Azure Redis Cache в процентах.",
    "The latency to the cache in microseconds.": "Задержка обращения к кэшу в микросекундах.",
    # EN grammar slip "The number errors" -> RU normal grammar
    "The number errors that occurred on the cache.": "Количество ошибок, произошедших на кэше.",
    "The health status of geo-replication link. 1 if healthy and 0 if disconnected or unhealthy.": "Статус работоспособности связи георепликации. 1, если работоспособна, и 0, если отключена или неработоспособна.",
    "Approximate amount of data in bytes that needs to be synchronized to geo-secondary cache.": "Приблизительный объём данных в байтах, которые необходимо синхронизировать на гео-вторичный кэш.",
    "Time in seconds since last successful data synchronization with geo-primary cache. Value will continue to increase if the link status is down.": "Время в секундах с момента последней успешной синхронизации данных с гео-первичным кэшем. Значение продолжит расти, если связь не работает.",
    "Fired on initiation of a full synchronization event between geo-replicated caches. This metric reports 0 most of the time because geo-replication uses partial resynchronizations for any new data added after the initial full synchronization.": "Срабатывает при инициации события полной синхронизации между геореплицированными кэшами. Эта метрика большую часть времени сообщает 0, поскольку георепликация использует частичные ресинхронизации для любых новых данных, добавленных после первоначальной полной синхронизации.",
    "Fired on completion of a full synchronization event between geo-replicated caches. This metric reports 0 most of the time because geo-replication uses partial resynchronizations for any new data added after the initial full synchronization.": "Срабатывает при завершении события полной синхронизации между геореплицированными кэшами. Эта метрика большую часть времени сообщает 0, поскольку георепликация использует частичные ресинхронизации для любых новых данных, добавленных после первоначальной полной синхронизации.",
    # --- cognitive-services-ink-recognizer ---
    "Number of calls that exceeded rate or quota limit": "Количество вызовов, превысивших лимит частоты или квоты",
    "Number of calls with client-side error (HTTP response code `4xx`)": "Количество вызовов с ошибкой на стороне клиента (код HTTP-ответа `4xx`)",
    "Size of incoming data in bytes": "Размер входящих данных в байтах",
    "Size of outgoing data in bytes": "Размер исходящих данных в байтах",
    "Latency in milliseconds": "Задержка в миллисекундах",
    "Number of calls with service internal error (HTTP response code `5xx`)": "Количество вызовов с внутренней ошибкой сервиса (код HTTP-ответа `5xx`)",
    "Number of successful calls": "Количество успешных вызовов",
    "Total number of calls": "Общее количество вызовов",
    "Total number of calls with error response (HTTP response code `4xx` or `5xx`)": "Общее количество вызовов с ответом об ошибке (код HTTP-ответа `4xx` или `5xx`)",
    # --- event-grid ---
    "Total dead-lettered events matching to this event subscription": "Общее количество недоставленных событий, соответствующих этой подписке на события",
    "Total events failed to deliver to this event subscription": "Общее количество событий, которые не удалось доставить в эту подписку на события",
    "Total events delivered to this event subscription": "Общее количество событий, доставленных в эту подписку на события",
    "Destination processing duration in milliseconds": "Длительность обработки в назначении в миллисекундах",
    "Total dropped events matching to this event subscription": "Общее количество отброшенных событий, соответствующих этой подписке на события",
    "Total events matched to this event subscription": "Общее количество событий, сопоставленных с этой подпиской на события",
    "Total events failed to publish to this topic": "Общее количество событий, которые не удалось опубликовать в этот топик",
    "Total events published to this topic": "Общее количество событий, опубликованных в этот топик",
    "Publish success latency in milliseconds": "Задержка успешной публикации в миллисекундах",
    "Total events not matching any of the event subscriptions for this topic": "Общее количество событий, не соответствующих ни одной подписке на события для этого топика",
    # --- event-hubs ---
    "Total active connections for Microsoft.EventHub": "Общее количество активных подключений для Microsoft.EventHub",
    "Available memory for the Event Hub Cluster as a percentage of total memory": "Доступная память кластера Event Hub в процентах от общей памяти",
    "CPU utilization for the Event Hub Cluster as a percentage": "Использование ЦП кластера Event Hub в процентах",
    "Captured backlog for Microsoft.EventHub": "Бэклог захвата для Microsoft.EventHub",
    "Captured bytes for Microsoft.EventHub": "Захваченные байты для Microsoft.EventHub",
    "Captured messages for Microsoft.EventHub": "Захваченные сообщения для Microsoft.EventHub",
    "Connections closed for Microsoft.EventHub": "Закрытые подключения для Microsoft.EventHub",
    "Connections opened for Microsoft.EventHub": "Открытые подключения для Microsoft.EventHub",
    "Incoming bytes for Microsoft.EventHub": "Входящие байты для Microsoft.EventHub",
    "Incoming messages for Microsoft.EventHub": "Входящие сообщения для Microsoft.EventHub",
    "Incoming requests for Microsoft.EventHub": "Входящие запросы для Microsoft.EventHub",
    "Outgoing bytes for Microsoft.EventHub": "Исходящие байты для Microsoft.EventHub",
    "Outgoing messages for Microsoft.EventHub": "Исходящие сообщения для Microsoft.EventHub",
    "Quota exceeded errors for Microsoft.EventHub": "Ошибки превышения квоты для Microsoft.EventHub",
    "Server errors for Microsoft.EventHub.": "Ошибки сервера для Microsoft.EventHub.",
    "Size of an EventHub in Bytes.": "Размер EventHub в байтах.",
    "Successful requests for Microsoft.EventHub": "Успешные запросы для Microsoft.EventHub",
    "Throttled requests for Microsoft.EventHub": "Запросы, подвергнутые регулированию, для Microsoft.EventHub",
    "User errors for Microsoft.EventHub": "Ошибки пользователя для Microsoft.EventHub",
    # --- front-door (classic) ---
    "Percentage of successful health probes from the HTTP/S proxy to backends": "Процент успешных проб работоспособности от HTTP/S-прокси к бэкендам",
    "Number of requests sent from the HTTP/S proxy to backends": "Количество запросов, отправленных от HTTP/S-прокси к бэкендам",
    # EN source quirk "proxyMySQL" (concatenation slip); RU renders the meaning
    "Time from when the request was sent by the HTTP/S proxyMySQL to the backend until the HTTP/S proxy received the last response byte from the backend": "Время от отправки запроса HTTP/S-прокси бэкенду до получения HTTP/S-прокси последнего байта ответа от бэкенда",
    "Number of billable bytes (minimum 2KB per request) sent as responses from HTTP/S proxy to clients": "Количество оплачиваемых байтов (минимум 2 КБ на запрос), отправленных в качестве ответов от HTTP/S-прокси клиентам",
    "Number of client requests served by the HTTP/S proxy": "Количество клиентских запросов, обслуженных HTTP/S-прокси",
    "Number of bytes sent as requests from clients to the HTTP/S proxy": "Количество байтов, отправленных в качестве запросов от клиентов к HTTP/S-прокси",
    "Number of bytes sent as responses from HTTP/S proxy to clients": "Количество байтов, отправленных в качестве ответов от HTTP/S-прокси клиентам",
    "Time calculated from when the client request was received by the HTTP/S proxy until the client acknowledged the last response byte from the HTTP/S proxy": "Время, рассчитанное от получения клиентского запроса HTTP/S-прокси до подтверждения клиентом последнего байта ответа от HTTP/S-прокси",
    "This is the ratio of the total bytes served from the cache compared to the total response bytes": "Отношение общего количества байтов, отданных из кэша, к общему количеству байтов ответов",
    "Number of client requests processed by the Web Application Firewall": "Количество клиентских запросов, обработанных Web Application Firewall",
    # --- front-door-cdn-profiles (AFDX) ---
    "The percentage of successful health probes from AFDX to backends.": "Процент успешных проб работоспособности от AFDX к бэкендам.",
    "The time calculated from when the request was sent by AFDX edge to the backend until AFDX received the last response byte from the backend.": "Время, рассчитанное от отправки запроса пограничным узлом AFDX бэкенду до получения AFDX последнего байта ответа от бэкенда.",
    "The number of requests sent from AFDX to origin.": "Количество запросов, отправленных от AFDX к источнику.",
    "The percentage of all the client requests for which the response status code is 4XX": "Процент всех клиентских запросов, для которых код статуса ответа равен 4XX",
    "The percentage of all the client requests for which the response status code is 5XX": "Процент всех клиентских запросов, для которых код статуса ответа равен 5XX",
    "The number of client requests served by the HTTP/S proxy": "Количество клиентских запросов, обслуженных HTTP/S-прокси",
    "The number of bytes sent as requests from clients to AFDX.": "Количество байтов, отправленных в качестве запросов от клиентов к AFDX.",
    "The number of bytes sent as responses from HTTP/S proxy to clients": "Количество байтов, отправленных в качестве ответов от HTTP/S-прокси клиентам",
    "The time calculated from when the client request was received by the HTTP/S proxy until the client acknowledged the last response byte from the HTTP/S proxy": "Время, рассчитанное от получения клиентского запроса HTTP/S-прокси до подтверждения клиентом последнего байта ответа от HTTP/S-прокси",
    "The number of client requests processed by the Web Application Firewall": "Количество клиентских запросов, обработанных Web Application Firewall",
    # --- integration-service-environment (workflow family, "X of Y" word order) ---
    "Latency of completed workflow actions": "Задержка завершённых действий рабочего процесса",
    "Latency of succeeded workflow actions": "Задержка успешно выполненных действий рабочего процесса",
    "Number of workflow action throttled events": "Количество событий регулирования действий рабочего процесса",
    "Number of workflow actions completed": "Количество завершённых действий рабочего процесса",
    "Number of workflow actions failed": "Количество неудачных действий рабочего процесса",
    "Number of workflow actions skipped": "Количество пропущенных действий рабочего процесса",
    "Number of workflow actions started": "Количество начатых действий рабочего процесса",
    "Number of workflow actions succeeded": "Количество успешно выполненных действий рабочего процесса",
    "Workflow memory usage for integration service environment": "Использование памяти рабочими процессами для Integration Service Environment",
    "Workflow processor usage for integration service environment": "Использование процессора рабочими процессами для Integration Service Environment",
    "Percentage of workflow runs failed": "Процент неудачных запусков рабочих процессов",
    "Latency of completed workflow runs": "Задержка завершённых запусков рабочих процессов",
    "Number of workflow run start throttled events": "Количество событий регулирования запуска рабочих процессов",
    "Latency of succeeded workflow runs": "Задержка успешно выполненных запусков рабочих процессов",
    "Number of workflow action or trigger throttled events": "Количество событий регулирования действий или триггеров рабочего процесса",
    "Number of workflow runs cancelled": "Количество отменённых запусков рабочих процессов",
    "Number of workflow runs completed": "Количество завершённых запусков рабочих процессов",
    "Number of workflow runs failed": "Количество неудачных запусков рабочих процессов",
    "Number of workflow runs started": "Количество начатых запусков рабочих процессов",
    "Number of workflow runs succeeded": "Количество успешно выполненных запусков рабочих процессов",
    "Latency of fired workflow triggers": "Задержка сработавших триггеров рабочих процессов",
    "Latency of completed workflow triggers": "Задержка завершённых триггеров рабочих процессов",
    "Latency of succeeded workflow triggers": "Задержка успешно выполненных триггеров рабочих процессов",
    "Number of workflow trigger throttled events": "Количество событий регулирования триггеров рабочих процессов",
    "Number of workflow triggers completed": "Количество завершённых триггеров рабочих процессов",
    "Number of workflow triggers failed": "Количество неудачных триггеров рабочих процессов",
    "Number of workflow triggers fired": "Количество сработавших триггеров рабочих процессов",
    "Number of workflow triggers skipped": "Количество пропущенных триггеров рабочих процессов",
    "Number of workflow triggers started": "Количество начатых триггеров рабочих процессов",
    "Number of workflow triggers succeeded": "Количество успешно выполненных триггеров рабочих процессов",
    # --- iot-central-applications ---
    "The count of all failed property reads initiated from IoT Central": "Количество всех неудачных чтений свойств, инициированных из IoT Central",
    "The count of all successful property reads initiated from IoT Central": "Количество всех успешных чтений свойств, инициированных из IoT Central",
    "The count of all failed property updates initiated from IoT Central": "Количество всех неудачных обновлений свойств, инициированных из IoT Central",
    "The count of all successful property updates initiated from IoT Central": "Количество всех успешных обновлений свойств, инициированных из IoT Central",
    "Number of devices connected to IoT Central": "Количество устройств, подключённых к IoT Central",
    "The count of all failed property reads initiated from devices": "Количество всех неудачных чтений свойств, инициированных с устройств",
    "The count of all successful property reads initiated from devices": "Количество всех успешных чтений свойств, инициированных с устройств",
    "The count of all failed property updates initiated from devices": "Количество всех неудачных обновлений свойств, инициированных с устройств",
    "The count of all successful property updates initiated from devices": "Количество всех успешных обновлений свойств, инициированных с устройств",
    # --- iot-hub: d2c/c2d messaging ---
    "Number of device-to-cloud telemetry messages attempted to be sent to your IoT hub": "Количество попыток отправки телеметрических сообщений «устройство-облако» в ваш IoT-хаб",
    "Number of device-to-cloud telemetry messages sent successfully to your IoT hub": "Количество телеметрических сообщений «устройство-облако», успешно отправленных в ваш IoT-хаб",
    "Number of cloud-to-device message deliveries completed successfully by the device": "Количество доставок сообщений «облако-устройство», успешно завершённых устройством",
    "Number of cloud-to-device messages abandoned by the device": "Количество сообщений «облако-устройство», от которых устройство отказалось",
    "Number of cloud-to-device messages rejected by the device": "Количество сообщений «облако-устройство», отклонённых устройством",
    "Number of expired cloud-to-device messages": "Количество просроченных сообщений «облако-устройство»",
    "Number of devices registered to your IoT hub": "Количество устройств, зарегистрированных в вашем IoT-хабе",
    "Number of devices connected to your IoT hub": "Количество устройств, подключённых к вашему IoT-хабу",
    # --- iot-hub: routing ---
    "The number of times messages were successfully delivered to all endpoints using IoT Hub routing. If a message is routed to multiple endpoints, this value increases by one for each successful delivery. If a message is delivered to the same endpoint multiple times, this value increases by one for each successful delivery.": "Количество раз, когда сообщения были успешно доставлены во все конечные точки с использованием маршрутизации IoT Hub. Если сообщение маршрутизируется в несколько конечных точек, это значение увеличивается на единицу за каждую успешную доставку. Если сообщение доставляется в одну и ту же конечную точку несколько раз, это значение увеличивается на единицу за каждую успешную доставку.",
    "The number of times messages were dropped by IoT Hub routing due to dead endpoints. This value does not count messages delivered to fallback route as dropped messages are not delivered there.": "Количество раз, когда сообщения были отброшены маршрутизацией IoT Hub из-за неработающих конечных точек. Это значение не учитывает сообщения, доставленные в резервный маршрут, поскольку отброшенные сообщения туда не доставляются.",
    "The number of times messages were orphaned by IoT Hub routing because they didn't match any routing rules (including the fallback rule).": "Количество раз, когда сообщения остались без назначения в маршрутизации IoT Hub, поскольку они не соответствовали ни одному правилу маршрутизации (включая резервное правило).",
    "The number of times IoT Hub routing failed to deliver messages due to an incompatibility with the endpoint. This value does not include retries.": "Количество раз, когда маршрутизации IoT Hub не удалось доставить сообщения из-за несовместимости с конечной точкой. Это значение не включает повторные попытки.",
    "The number of times IoT Hub routing delivered messages to the endpoint associated with the fallback route.": "Количество раз, когда маршрутизация IoT Hub доставила сообщения в конечную точку, связанную с резервным маршрутом.",
    "The number of times IoT Hub routing successfully delivered messages to Event Hub endpoints.": "Количество раз, когда маршрутизация IoT Hub успешно доставила сообщения в конечные точки Event Hub.",
    "The average latency (milliseconds) between message ingress to IoT Hub and message ingress into an Event Hub endpoint.": "Средняя задержка (в миллисекундах) между поступлением сообщения в IoT Hub и поступлением сообщения в конечную точку Event Hub.",
    "The number of times IoT Hub routing successfully delivered messages to Service Bus queue endpoints.": "Количество раз, когда маршрутизация IoT Hub успешно доставила сообщения в конечные точки очередей Service Bus.",
    "The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into a Service Bus queue endpoint.": "Средняя задержка (в миллисекундах) между поступлением сообщения в IoT Hub и поступлением телеметрического сообщения в конечную точку очереди Service Bus.",
    "The number of times IoT Hub routing successfully delivered messages to Service Bus topic endpoints.": "Количество раз, когда маршрутизация IoT Hub успешно доставила сообщения в конечные точки топиков Service Bus.",
    "The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into a Service Bus topic endpoint.": "Средняя задержка (в миллисекундах) между поступлением сообщения в IoT Hub и поступлением телеметрического сообщения в конечную точку топика Service Bus.",
    "The number of times IoT Hub routing successfully delivered messages to the built-in endpoint (messages/events).": "Количество раз, когда маршрутизация IoT Hub успешно доставила сообщения во встроенную конечную точку (messages/events).",
    "The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into the built-in endpoint (messages/events).": "Средняя задержка (в миллисекундах) между поступлением сообщения в IoT Hub и поступлением телеметрического сообщения во встроенную конечную точку (messages/events).",
    "The number of times IoT Hub routing successfully delivered messages to storage endpoints.": "Количество раз, когда маршрутизация IoT Hub успешно доставила сообщения в конечные точки хранилища.",
    "The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into a storage endpoint.": "Средняя задержка (в миллисекундах) между поступлением сообщения в IoT Hub и поступлением телеметрического сообщения в конечную точку хранилища.",
    "The amount of data (bytes) IoT Hub routing delivered to storage endpoints.": "Объём данных (в байтах), доставленных маршрутизацией IoT Hub в конечные точки хранилища.",
    "The number of times IoT Hub routing delivered blobs to storage endpoints.": "Количество раз, когда маршрутизация IoT Hub доставила BLOB-объекты в конечные точки хранилища.",
    "The number of IoT Hub events published to Event Grid. Use the Result dimension for the number of successful and failed requests.": "Количество событий IoT Hub, опубликованных в Event Grid. Используйте измерение Result для получения количества успешных и неудачных запросов.",
    "The average latency (milliseconds) from when the Iot Hub event was generated to when the event was published to Event Grid. This number is an average between all event types. Use the EventType dimension to see latency of a specific type of event.": "Средняя задержка (в миллисекундах) от генерации события Iot Hub до публикации события в Event Grid. Это число является средним по всем типам событий. Используйте измерение EventType для просмотра задержки конкретного типа событий.",
    "The number of times IoT Hub attempted to deliver messages to all endpoints using routing. To see the number of successful or failed attempts, use the Result dimension. To see the reason of failure, like invalid, dropped, or orphaned, use the FailureReasonCategory dimension. You can also use the EndpointName and EndpointType dimensions to understand how many messages were delivered to your different endpoints. The metric value increases by one for each delivery attempt, including if the message is delivered to multiple endpoints or if the message is delivered to the same endpoint multiple times.": "Количество раз, когда IoT Hub пытался доставить сообщения во все конечные точки с использованием маршрутизации. Чтобы увидеть количество успешных или неудачных попыток, используйте измерение Result. Чтобы увидеть причину сбоя, например invalid, dropped или orphaned, используйте измерение FailureReasonCategory. Вы также можете использовать измерения EndpointName и EndpointType, чтобы понять, сколько сообщений было доставлено в ваши различные конечные точки. Значение метрики увеличивается на единицу за каждую попытку доставки, в том числе если сообщение доставляется в несколько конечных точек или если сообщение доставляется в одну и ту же конечную точку несколько раз.",
    "The average latency (milliseconds) between message ingress to IoT Hub and telemetry message ingress into an endpoint. You can use the EndpointName and EndpointType dimensions to understand the latency to your different endpoints.": "Средняя задержка (в миллисекундах) между поступлением сообщения в IoT Hub и поступлением телеметрического сообщения в конечную точку. Вы можете использовать измерения EndpointName и EndpointType, чтобы понять задержку до ваших различных конечных точек.",
    "The total size in bytes of messages delivered by IoT hub to an endpoint. You can use the EndpointName and EndpointType dimensions to view the size of the messages in bytes delivered to your different endpoints. The metric value increases for every message delivered, including if the message is delivered to multiple endpoints or if the message is delivered to the same endpoint multiple times.": "Общий размер в байтах сообщений, доставленных IoT-хабом в конечную точку. Вы можете использовать измерения EndpointName и EndpointType для просмотра размера сообщений в байтах, доставленных в ваши различные конечные точки. Значение метрики увеличивается при каждой доставке сообщения, в том числе если сообщение доставляется в несколько конечных точек или если сообщение доставляется в одну и ту же конечную точку несколько раз.",
    # --- iot-hub: twins / direct methods / jobs ---
    "The count of all successful device-initiated twin reads.": "Количество всех успешных чтений двойника, инициированных устройством.",
    "The count of all failed device-initiated twin reads.": "Количество всех неудачных чтений двойника, инициированных устройством.",
    "The average, min, and max of all successful device-initiated twin reads.": "Среднее, минимальное и максимальное значение всех успешных чтений двойника, инициированных устройством.",
    "The count of all successful device-initiated twin updates.": "Количество всех успешных обновлений двойника, инициированных устройством.",
    "The count of all failed device-initiated twin updates.": "Количество всех неудачных обновлений двойника, инициированных устройством.",
    "The average, min, and max size of all successful device-initiated twin updates.": "Средний, минимальный и максимальный размер всех успешных обновлений двойника, инициированных устройством.",
    "The count of all successful direct method calls.": "Количество всех успешных вызовов прямых методов.",
    "The count of all failed direct method calls.": "Количество всех неудачных вызовов прямых методов.",
    "The average, min, and max of all successful direct method requests.": "Среднее, минимальное и максимальное значение всех успешных запросов прямых методов.",
    "The average, min, and max of all successful direct method responses.": "Среднее, минимальное и максимальное значение всех успешных ответов прямых методов.",
    "The count of all successful back-end-initiated twin reads.": "Количество всех успешных чтений двойника, инициированных бэкендом.",
    "The count of all failed back-end-initiated twin reads.": "Количество всех неудачных чтений двойника, инициированных бэкендом.",
    "The average, min, and max of all successful back-end-initiated twin reads.": "Среднее, минимальное и максимальное значение всех успешных чтений двойника, инициированных бэкендом.",
    "The count of all successful back-end-initiated twin updates.": "Количество всех успешных обновлений двойника, инициированных бэкендом.",
    "The count of all failed back-end-initiated twin updates.": "Количество всех неудачных обновлений двойника, инициированных бэкендом.",
    "The average, min, and max size of all successful back-end-initiated twin updates.": "Средний, минимальный и максимальный размер всех успешных обновлений двойника, инициированных бэкендом.",
    "The count of all successful twin queries.": "Количество всех успешных запросов двойников.",
    "The count of all failed twin queries.": "Количество всех неудачных запросов двойников.",
    "The average, min, and max of the result size of all successful twin queries.": "Средний, минимальный и максимальный размер результата всех успешных запросов двойников.",
    "The count of all successful creation of twin update jobs.": "Количество всех успешных созданий заданий обновления двойников.",
    "The count of all failed creation of twin update jobs.": "Количество всех неудачных созданий заданий обновления двойников.",
    "The count of all successful creation of direct method invocation jobs.": "Количество всех успешных созданий заданий вызова прямых методов.",
    "The count of all failed creation of direct method invocation jobs.": "Количество всех неудачных созданий заданий вызова прямых методов.",
    "The count of all successful calls to list jobs.": "Количество всех успешных вызовов получения списка заданий.",
    "The count of all failed calls to list jobs.": "Количество всех неудачных вызовов получения списка заданий.",
    "The count of all successful calls to cancel a job.": "Количество всех успешных вызовов отмены задания.",
    "The count of all failed calls to cancel a job.": "Количество всех неудачных вызовов отмены задания.",
    "The count of all successful calls to query jobs.": "Количество всех успешных вызовов запроса заданий.",
    "The count of all failed calls to query jobs.": "Количество всех неудачных вызовов запроса заданий.",
    "The count of all completed jobs.": "Количество всех завершённых заданий.",
    "The count of all failed jobs.": "Количество всех неудачных заданий.",
    "Number of throttling errors due to device throughput throttles": "Количество ошибок регулирования из-за ограничений пропускной способности устройств",
    "Number of total messages used today": "Общее количество сообщений, использованных за сегодня",
    "Bytes transferred to and from any devices connected to IotHub": "Байты, переданные на любые устройства, подключённые к IotHub, и от них",
    "Metrics for Configuration Operations": "Метрики операций конфигурации",
    # --- device-provisioning-service ---
    "The number of device attestations attempted": "Количество попыток аттестации устройств",
    "The number of devices assigned to an IoT hub": "Количество устройств, назначенных IoT-хабу",
    "The number of device registrations attempted": "Количество попыток регистрации устройств",
    # --- key-vault ---
    "Vault requests availability": "Доступность запросов хранилища",
    "Total number of service API hits": "Общее количество обращений к API сервиса",
    "Overall latency of service API": "Общая задержка API сервиса",
    "Total number of service API results": "Общее количество результатов API сервиса",
    "Vault capacity used": "Использованная ёмкость хранилища",
    # --- logic-apps (workflow family, "X workflow Y" word order) ---
    "Latency of successful workflow actions": "Задержка успешных действий рабочего процесса",
    "Number of completed workflow actions": "Количество завершённых действий рабочего процесса",
    "Number of failed workflow actions": "Количество неудачных действий рабочего процесса",
    "Number of skipped workflow actions": "Количество пропущенных действий рабочего процесса",
    "Number of started workflow actions": "Количество начатых действий рабочего процесса",
    "Number of successful workflow actions": "Количество успешных действий рабочего процесса",
    "Number of billed workflow action executions": "Количество оплачиваемых выполнений действий рабочего процесса",
    "Number of billed workflow trigger executions": "Количество оплачиваемых выполнений триггеров рабочего процесса",
    "Number of billed native operation executions": "Количество оплачиваемых выполнений нативных операций",
    "Number of billed standard connector executions": "Количество оплачиваемых выполнений стандартных коннекторов",
    "Number of billed storage consumption executions": "Количество оплачиваемых выполнений с потреблением хранилища",
    "Percentage of failed workflow runs": "Процент неудачных запусков рабочих процессов",
    "Latency of successful workflow runs": "Задержка успешных запусков рабочих процессов",
    "Number of cancelled workflow runs": "Количество отменённых запусков рабочих процессов",
    "Number of completed workflow runs": "Количество завершённых запусков рабочих процессов",
    "Number of failed workflow runs": "Количество неудачных запусков рабочих процессов",
    "Number of started workflow runs": "Количество начатых запусков рабочих процессов",
    "Number of successful workflow runs": "Количество успешных запусков рабочих процессов",
    "Number of billed workflow executions": "Количество оплачиваемых выполнений рабочих процессов",
    "Latency of successful workflow triggers": "Задержка успешных триггеров рабочих процессов",
    "Number of completed workflow triggers": "Количество завершённых триггеров рабочих процессов",
    "Number of failed workflow triggers": "Количество неудачных триггеров рабочих процессов",
    "Number of fired workflow triggers": "Количество сработавших триггеров рабочих процессов",
    "Number of skipped workflow triggers": "Количество пропущенных триггеров рабочих процессов",
    "Number of started workflow triggers": "Количество начатых триггеров рабочих процессов",
    "Number of successful workflow triggers": "Количество успешных триггеров рабочих процессов",
    # --- maps-account ---
    "Availability of the APIs": "Доступность API",
    "Count of API calls": "Количество вызовов API",
    # --- media-service ("polices" is an EN typo for policies) ---
    "The number of assets already created in current media service account": "Количество ресурсов, уже созданных в текущем аккаунте медиасервиса",
    "The number of assets allowed for current media service account": "Количество ресурсов, разрешённых для текущего аккаунта медиасервиса",
    "Asset used percentage in current media service account": "Процент использования ресурсов в текущем аккаунте медиасервиса",
    "The number of content key policies already created in current media service account": "Количество политик ключей контента, уже созданных в текущем аккаунте медиасервиса",
    "The number of content key polices allowed for current media service account": "Количество политик ключей контента, разрешённых для текущего аккаунта медиасервиса",
    "Content key policy used percentage in current media service account": "Процент использования политик ключей контента в текущем аккаунте медиасервиса",
    "The number of streaming policies already created in current media service account": "Количество политик потоковой передачи, уже созданных в текущем аккаунте медиасервиса",
    "The number of streaming policies allowed for current media service account": "Количество политик потоковой передачи, разрешённых для текущего аккаунта медиасервиса",
    "Streaming policy used percentage in current media service account": "Процент использования политик потоковой передачи в текущем аккаунте медиасервиса",
    # --- mesh-application ---
    "CPU allocated as per Azure Resource Manager template": "ЦП, выделенный согласно шаблону Azure Resource Manager",
    "Memory allocated as per Azure Resource Manager template": "Память, выделенная согласно шаблону Azure Resource Manager",
    "CPU usage": "Использование ЦП",
    "Percentage of actual/allocated CPU": "Процент фактического/выделенного ЦП",
    "Percentage of actual/allocated memory": "Процент фактической/выделенной памяти",
    # --- notification-hub ---
    "The count of all successful send API calls": "Количество всех успешных вызовов API отправки",
    "Total incoming failed requests for a notification hub": "Общее количество входящих неудачных запросов для хаба уведомлений",
    "Total incoming requests for a notification hub": "Общее количество входящих запросов для хаба уведомлений",
    "Scheduled push notifications sent": "Отправленные запланированные push-уведомления",
    "Scheduled push notifications cancelled": "Отменённые запланированные push-уведомления",
    "Installation management operations": "Операции управления установками",
    "Delete installation operations": "Операции удаления установок",
    "Get installation operations": "Операции получения установок",
    "Patch installation operations": "Операции исправления установок",
    "Create or update installation operations": "Операции создания или обновления установок",
    "All outgoing notifications of the notification hub": "Все исходящие уведомления хаба уведомлений",
    "The count of pushes that failed because the channel/token/registrationId in the registration was expired or invalid": "Количество push-уведомлений, не доставленных из-за того, что канал/токен/registrationId в регистрации просрочен или недействителен",
    "The count of pushes that failed because the channel was invalid, not associated with the correct app, throttled, or expired": "Количество push-уведомлений, не доставленных из-за того, что канал недействителен, не связан с правильным приложением, подвергнут регулированию или просрочен",
    "The count of pushes that failed because the PNS returned a bad payload error": "Количество push-уведомлений, не доставленных из-за того, что PNS вернула ошибку некорректной полезной нагрузки",
    "The count of pushes that failed because there was a problem communicating with the PNS (excludes authentication problems)": "Количество push-уведомлений, не доставленных из-за проблемы связи с PNS (исключая проблемы аутентификации)",
    "The count of all successful notifications": "Количество всех успешных уведомлений",
    "The count of pushes that failed because the token is invalid (APNS status code: 8)": "Количество push-уведомлений, не доставленных из-за недействительного токена (код статуса APNS: 8)",
    "The count of token that were invalidated by the APNS feedback channel": "Количество токенов, аннулированных каналом обратной связи APNS",
    "The count of pushes that failed because the PNS did not accept the provided credentials, or the credentials are blocked": "Количество push-уведомлений, не доставленных из-за того, что PNS не приняла предоставленные учётные данные, или учётные данные заблокированы",
    "The count of pushes that failed because the payload was too large (APNS status code: `7`)": "Количество push-уведомлений, не доставленных из-за слишком большой полезной нагрузки (код статуса APNS: `7`)",
    "The count of pushes that failed because of errors communicating with APNS": "Количество push-уведомлений, не доставленных из-за ошибок связи с APNS",
    "The count of pushes that failed because the PNS didn't accept the provided credentials, the credentials are blocked, or the `SenderId` isn't correctly configured in the app (GCM result: `MismatchedSenderId`)": "Количество push-уведомлений, не доставленных из-за того, что PNS не приняла предоставленные учётные данные, учётные данные заблокированы или `SenderId` неправильно настроен в приложении (результат GCM: `MismatchedSenderId`)",
    "The count of pushes that failed because the `registrationId` in the registration wasn't recognized (GCM result: `Invalid Registration`)": "Количество push-уведомлений, не доставленных из-за того, что `registrationId` в регистрации не распознан (результат GCM: `Invalid Registration`)",
    "The count of pushes that failed because the `registrationId` in the registration was expired (GCM result: `NotRegistered`)": "Количество push-уведомлений, не доставленных из-за того, что `registrationId` в регистрации просрочен (результат GCM: `NotRegistered`)",
    "The count of pushes that failed because the PNS didn't accept the provided credentials, or the credentials are blocked": "Количество push-уведомлений, не доставленных из-за того, что PNS не приняла предоставленные учётные данные, или учётные данные заблокированы",
    "The count of pushes that failed because the payload wasn't formatted correctly (GCM result: `InvalidDataKey` or `InvalidTtl`)": "Количество push-уведомлений, не доставленных из-за неправильного форматирования полезной нагрузки (результат GCM: `InvalidDataKey` или `InvalidTtl`)",
    "The count of pushes that failed because the payload was too large (GCM result: `MessageTooBig`)": "Количество push-уведомлений, не доставленных из-за слишком большой полезной нагрузки (результат GCM: `MessageTooBig`)",
    "The count of pushes that failed because of errors communicating with GCM": "Количество push-уведомлений, не доставленных из-за ошибок связи с GCM",
    "The count of pushes that failed because GCM throttled this app (GCM status code: `501`-`599` or `result:Unavailable`)": "Количество push-уведомлений, не доставленных из-за того, что GCM подвергла это приложение регулированию (код статуса GCM: `501`-`599` или `result:Unavailable`)",
    "The count of pushes that failed because the `registrationId` in the registration isn't associated to the current app (GCM result: `InvalidPackageName`)": "Количество push-уведомлений, не доставленных из-за того, что `registrationId` в регистрации не связан с текущим приложением (результат GCM: `InvalidPackageName`)",
    "The count of pushes that failed because the `ChannelURI` in the registration wasn't recognized (MPNS status: `404 not found`)": "Количество push-уведомлений, не доставленных из-за того, что `ChannelURI` в регистрации не распознан (статус MPNS: `404 not found`)",
    "The count of pushes that failed because the `ChannelURI` in the registration was disconnected (MPNS status: `412 not found`)": "Количество push-уведомлений, не доставленных из-за того, что `ChannelURI` в регистрации отключён (статус MPNS: `412 not found`)",
    "The count of pushes that were dropped by MPNS (MPNS response header: X-NotificationStatus: `QueueFull or Suppressed`)": "Количество push-уведомлений, отброшенных MPNS (заголовок ответа MPNS: X-NotificationStatus: `QueueFull or Suppressed`)",
    "The count of pushes that failed because the payload of the notification was too large": "Количество push-уведомлений, не доставленных из-за слишком большой полезной нагрузки уведомления",
    "The count of pushes that failed because of errors communicating with MPNS": "Количество push-уведомлений, не доставленных из-за ошибок связи с MPNS",
    "The count of pushes that failed because MPNS is throttling this app (WNS MPNS: `406 Not Acceptable`)": "Количество push-уведомлений, не доставленных из-за того, что MPNS подвергает это приложение регулированию (WNS MPNS: `406 Not Acceptable`)",
    "Notification not delivered because of errors communicating with Windows Live, invalid credentials, or wrong token": "Уведомление не доставлено из-за ошибок связи с Windows Live, недействительных учётных данных или неправильного токена",
    "The count of pushes that failed because the ChannelURI in the registration was not recognized (WNS status: 404 not found)": "Количество push-уведомлений, не доставленных из-за того, что ChannelURI в регистрации не распознан (статус WNS: 404 not found)",
    # EN copy-paste slip: metric name "channeldisconnected" + header value
    # `Disconnected` contradict "is throttled" -> RU renders the in-row fact
    # (same class as DataWritten direction fix, L4-IF.40)
    "The notification was dropped because the `ChannelURI` in the registration is throttled (WNS response header: X-WNS-DeviceConnectionStatus: `Disconnected`)": "Уведомление отброшено, поскольку `ChannelURI` в регистрации отключён (заголовок ответа WNS: X-WNS-DeviceConnectionStatus: `Disconnected`)",
    "The notification was dropped because the `ChannelURI` in the registration is throttled (WNS response header: X-WNS-NotificationStatus: `ChannelThrottled`)": "Уведомление отброшено, поскольку `ChannelURI` в регистрации подвергнут регулированию (заголовок ответа WNS: X-WNS-NotificationStatus: `ChannelThrottled`)",
    "The notification was dropped because the `ChannelURI` in the registration is throttled (X-WNS-NotificationStatus: dropped but not X-WNS-DeviceConnectionStatus: `Disconnected`)": "Уведомление отброшено, поскольку `ChannelURI` в регистрации подвергнут регулированию (X-WNS-NotificationStatus: dropped, но не X-WNS-DeviceConnectionStatus: `Disconnected`)",
    "The count of pushes that failed because the `ChannelURI` is expired (WNS status: `410 Gone`)": "Количество push-уведомлений, не доставленных из-за того, что `ChannelURI` просрочен (статус WNS: `410 Gone`)",
    "The count of pushes that failed because the PNS didn't accept the provided credentials, the credentials are blocked, or Windows Live doesn't recognize the credentials": "Количество push-уведомлений, не доставленных из-за того, что PNS не приняла предоставленные учётные данные, учётные данные заблокированы или Windows Live не распознаёт учётные данные",
    "The format of the notification is invalid (WNS status: `400`). Note that WNS doesn't reject all invalid payloads": "Формат уведомления недействителен (статус WNS: `400`). Обратите внимание, что WNS отклоняет не все недействительные полезные нагрузки",
    "The notification payload is too large (WNS status: `413`)": "Полезная нагрузка уведомления слишком велика (статус WNS: `413`)",
    "The token provided to WNS isn't valid (WNS status: `401 Unauthorized`)": "Токен, предоставленный WNS, недействителен (статус WNS: `401 Unauthorized`)",
    "Notification not delivered because of errors communicating with WNS": "Уведомление не доставлено из-за ошибок связи с WNS",
    "The count of pushes that failed because WNS is throttling this app (WNS status: `406 Not Acceptable`)": "Количество push-уведомлений, не доставленных из-за того, что WNS подвергает это приложение регулированию (статус WNS: `406 Not Acceptable`)",
    "Windows Live isn't reachable": "Windows Live недоступен",
    "The token provided to WNS is valid, but for another application (WNS status: `403 Forbidden`). This can happen if the `ChannelURI` in the registration is associated with another app.": "Токен, предоставленный WNS, действителен, но для другого приложения (статус WNS: `403 Forbidden`). Это может произойти, если `ChannelURI` в регистрации связан с другим приложением.",
    "The count of all successful registration operations (creations, updates, queries, and deletions)": "Количество всех успешных операций регистрации (создания, обновления, запросы и удаления)",
    "The count of all successful registration creations": "Количество всех успешных созданий регистраций",
    "The count of all successful registration deletions": "Количество всех успешных удалений регистраций",
    "The count of all successful registration queries": "Количество всех успешных запросов регистраций",
    "The count of all successful registration updates": "Количество всех успешных обновлений регистраций",
    "Pending scheduled notifications": "Ожидающие запланированные уведомления",
    # --- power-bi ---
    "DAX query duration in last interval": "Длительность запросов DAX за последний интервал",
    "Number of jobs in the queue of the query thread pool": "Количество заданий в очереди пула потоков запросов",
    "Memory ranging 0-3 GB for A1, 0-5 GB for A2, 0-10 GB for A3, 0-20 GB for A4, 0-50 GB for A5, and 0-100 GB for A6": "Память в диапазоне 0-3 ГБ для A1, 0-5 ГБ для A2, 0-10 ГБ для A3, 0-20 ГБ для A4, 0-50 ГБ для A5 и 0-100 ГБ для A6",
    "Average memory thrashing": "Средняя пробуксовка памяти",
    "QPU high utilization in last minute, `1` for high QPU utilization, otherwise `0`": "Высокое использование QPU за последнюю минуту: `1` при высоком использовании QPU, иначе `0`",
    "QPU ranging 0-100 for S1, 0-200 for S2, and 0-400 for S4": "QPU в диапазоне 0-100 для S1, 0-200 для S2 и 0-400 для S4",
    "The usage of memory in your capacity resource per workload": "Использование памяти в вашем ресурсе ёмкости по рабочим нагрузкам",
    "The query processing unit (QPU) load on your capacity, per workload": "Нагрузка единиц обработки запросов (QPU) на вашу ёмкость по рабочим нагрузкам",
    # --- search ---
    "Average search latency for the search service": "Средняя задержка поиска для сервиса поиска",
    "Search queries per second for the search service": "Поисковые запросы в секунду для сервиса поиска",
    "Percentage of search queries that were throttled for the search service": "Процент поисковых запросов, подвергнутых регулированию, для сервиса поиска",
    # --- signalr (EN grammar slips rendered with normal RU grammar) ---
    "The amount of user connection": "Количество пользовательских подключений",
    "The inbound traffic of service": "Входящий трафик сервиса",
    "The total amount of messages": "Общее количество сообщений",
    "The outbound traffic of service": "Исходящий трафик сервиса",
    "The percentage of system errors": "Процент системных ошибок",
    "The percentage of user errors": "Процент пользовательских ошибок",
    # --- stream-analytics (short name-echo cells; live in the broken
    #     "Dimensions" header column, factually Description) ---
    "Failed function requests": "Неудачные запросы функций",
    "Function events": "События функций",
    "Function requests": "Запросы функций",
    "Data conversion errors": "Ошибки преобразования данных",
    "Input deserialization errors": "Ошибки десериализации входных данных",
    "Out-of-order events": "События, поступившие не по порядку",
    "Early input events": "Преждевременные входные события",
    "Runtime errors": "Ошибки среды выполнения",
    "Input event bytes": "Байты входных событий",
    "Input events": "Входные события",
    "Backlogged input events": "Входные события в бэклоге",
    "Input sources received": "Получено источников входных данных",
    "Late input events": "Опоздавшие входные события",
    "Output events": "Выходные события",
    "Watermark delay": "Задержка водяного знака",
    "Percentage of resource utilization": "Процент использования ресурсов",
    # --- time-series-insights ---
    "The number of messages read from all Event Hub or IoT Hub event sources": "Количество сообщений, прочитанных из всех источников событий Event Hub или IoT Hub",
    "The number of invalid messages read from the event source": "Количество недействительных сообщений, прочитанных из источника событий",
    "The total size of events successfully processed and available for query": "Общий размер событий, успешно обработанных и доступных для запросов",
    "The number of bytes read from all event sources": "Количество байтов, прочитанных из всех источников событий",
    "The number of flattened events successfully processed and available for query": "Количество событий, преобразованных в плоскую структуру, успешно обработанных и доступных для запросов",
    "The difference between the time that the message is enqueued in the event source and the time it is processed in ingress": "Разница между временем постановки сообщения в очередь в источнике событий и временем его обработки при приёме",
    "The difference between the sequence number of the last enqueued message in the event source partition and the sequence number of messages being processed in ingress": "Разница между порядковым номером последнего поставленного в очередь сообщения в партиции источника событий и порядковым номером сообщений, обрабатываемых при приёме",
    "The maximum number of properties used allowed by the environment for S1/S2 SKU and the maximum number of properties allowed by warm store for PAYG SKU": "Максимальное количество используемых свойств, разрешённое средой для SKU S1/S2, и максимальное количество свойств, разрешённое тёплым хранилищем для SKU PAYG",
    "The number of properties used by the environment for S1/S2 SKU and number of properties used by warm store for PAYG SKU": "Количество свойств, используемых средой для SKU S1/S2, и количество свойств, используемых тёплым хранилищем для SKU PAYG",
}

DESC_MAP = dict(e40.DESC_MAP)
for k, v in NEW_DESC.items():
    DESC_MAP.setdefault(k, v)

warnings = []


def is_sep(cells):
    return all(set(c) <= set("-: ") for c in cells)


def tr_table_line(line, colmap, fname):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = []
    for i, cell in enumerate(cells):
        col = colmap[i] if i < len(colmap) else None
        if col == "Description":
            if cell and cell not in DESC_MAP:
                warnings.append("%s: untranslated DESC -> %r" % (fname, cell))
            out.append(DESC_MAP.get(cell, cell))
        elif col == "Unit":
            if cell not in UNIT_MAP:
                warnings.append("%s: unmapped UNIT -> %r" % (fname, cell))
            out.append(UNIT_MAP.get(cell, cell))
        elif col and col.startswith("Recommended"):
            if cell not in REC_MAP:
                warnings.append("%s: unmapped REC -> %r" % (fname, cell))
            out.append(REC_MAP.get(cell, cell))
        elif cell == "Applicable":
            # broken-header fallback (L4-IF.40 canon): the unambiguous
            # Recommended value is translated in whatever column it appears
            out.append(REC_MAP[cell])
        else:  # Name, Dimensions, unknown -> keep EN
            out.append(cell)
    return "| " + " | ".join(out) + " |"


def tr_header(line, fname):
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    out = [HEADER_LABEL.get(c, c) for c in cells]
    colmap = COLMAP_OVERRIDE.get(fname, cells)
    return "| " + " | ".join(out) + " |", colmap


def has_cyr(s):
    return any("Ѐ" <= ch <= "ӿ" for ch in s)


def leftover_scan(fname, ru_text):
    """Warn on prose lines that stayed fully EN and are not whitelisted."""
    fmc = 0
    for n, line in enumerate(ru_text.split("\n"), 1):
        if line == "---" and fmc < 2:
            fmc += 1
            continue
        if fmc == 1:
            continue
        s = line.strip()
        if not s or s.startswith("|") or s.startswith("!["):
            continue
        if s in PASS_EN:
            continue
        if has_cyr(s):
            continue
        words = [
            w
            for w in s.replace("*", " ").replace("`", " ").split()
            if w.isalpha() and len(w) >= 3
        ]
        if len(words) >= 3:
            warnings.append("%s: EN leftover L%d -> %r" % (fname, n, s[:100]))


def build_one(fname):
    en = (
        open(os.path.join(EN_DIR, fname), encoding="utf-8").read().replace("\r\n", "\n")
    )
    en_title, ru_title = TITLE_MAP[fname]
    out_lines = []
    colmap = None
    for line in en.split("\n"):
        if line.startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if is_sep(cells):
                out_lines.append(line)
            elif cells and cells[0] == "Name":
                tline, colmap = tr_header(line, fname)
                out_lines.append(tline)
            elif colmap is not None:
                out_lines.append(tr_table_line(line, colmap, fname))
            else:
                out_lines.append(line)
            continue
        colmap = None
        if line in EXACT_LINE:
            out_lines.append(EXACT_LINE[line])
            continue
        s = line
        if en_title != ru_title:
            s = s.replace(en_title, ru_title)
        for k, v in DATE_MAP.items():
            s = s.replace(k, v)
        for k, v in PROSE:
            s = s.replace(k, v)
        out_lines.append(s)
    result = "\n".join(out_lines)
    out_path = os.path.join(RU_DIR, fname)
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "wb") as f:
        f.write(result.encode("utf-8"))
    leftover_scan(fname, result)
    return en, result


def main():
    ok = 0
    for fname in BATCH:
        en, ru = build_one(fname)
        en_n, ru_n = en.count("\n"), ru.count("\n")
        status = "OK" if en_n == ru_n else "LINE MISMATCH %d!=%d" % (en_n, ru_n)
        if en_n == ru_n:
            ok += 1
        print("%-22s  %s  (%d lines)" % (status, fname, ru_n + 1))
    print("\nline-parity OK: %d/%d" % (ok, len(BATCH)))
    if warnings:
        print("\n=== WARNINGS (%d) ===" % len(warnings))
        for w in warnings:
            print("  ", w)
    else:
        print("no warnings")


if __name__ == "__main__":
    main()
