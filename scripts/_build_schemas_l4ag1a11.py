# -*- coding: utf-8 -*-
"""L4-AG.1a.11 builder: 8 builtin-*.md schema-table files (6.05-6.81 KB).

Anchor canon: L4-AG.1a.10 (chr() для triple-mojibake, _normalize чистит mojibake-BOM,
empty-label rows разрешены в _param_row).

Mojibake-аудит EN:
  - triple-apos `'` (c3 a2 c2 80 c2 99): ownership-teams (1 = `team's`).
  - triple-en-dash `-` (c3 a2 c2 80 c2 93): processavailability (12 = bullet-separator
    `$contains(svc) - Matches if`, `$match(ver*_1.2.?) - Matches string`, etc.).
  - single-A (c3 a2): process-group-cloud-application-workload-detection (6 =
    fallback caption `Namespace name + Base pod name + Container name`),
    ownership-teams (1 = `team's` apostrophe = ASCII `'`? actually triple counted
    separately, so this single is somewhere else in ownership-teams).
  - mojibake-BOM `i»?` есть в нескольких файлах внутри hyperlink-текстов
    (`[See documentation](https://...)`), чистится `_normalize` (канон L4-AG.1a.7).
"""

import os, io, re as _re

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-ownership-teams.md",
    "builtin-anomaly-detection-kubernetes-node.md",
    "builtin-anomaly-detection-kubernetes-namespace.md",
    "builtin-elasticsearch-user-session-export-settings-v2.md",
    "builtin-preferences-privacy.md",
    "builtin-process-group-cloud-application-workload-detection.md",
    "builtin-processavailability.md",
    "builtin-failure-detection-environment-parameters.md",
]

# Triple-mojibake constants (canon L4-AG.1a.4 + L4-AG.1a.9, расширен в L4-AG.1a.11).
TM_APOS = chr(0xE2) + chr(0x80) + chr(0x99)  # ' (U+2019)
TM_ENDASH = chr(0xE2) + chr(0x80) + chr(0x93)  # - (U+2013)
TM_EMDASH = (
    chr(0xE2) + chr(0x80) + chr(0x94)
)  # - (U+2014) - новый, ownership-teams строка 44
TM_LQUOTE = chr(0xE2) + chr(0x80) + chr(0x9C)  # " (U+201C) - новый, process-group-cloud
TM_RQUOTE = chr(0xE2) + chr(0x80) + chr(0x9D)  # " (U+201D) - новый, process-group-cloud

DISPLAY_NAME = {
    "Ownership teams": "Команды ответственности",
    "Kubernetes node anomaly detection": "Обнаружение аномалий узла Kubernetes",
    "Kubernetes namespace anomaly detection": "Обнаружение аномалий namespace Kubernetes",
    "User session exports": "Экспорт user-сессий",
    "End users' data privacy": "Приватность данных конечных пользователей",
    "Cloud application and workload detection": "Обнаружение cloud application и workload",
    "Process availability": "Доступность процессов",
    "Failure detection parameters": "Параметры failure detection",
}

SCHEMA_DESC = {
    # 1. ownership-teams
    "Set up teams and assign responsibilities to them. Link teams to monitored entities in Dynatrace by referencing the team identifier in entity metadata. [See documentation](https://dt-url.net/ownership)": "Задайте команды и назначьте им зоны ответственности. Свяжите команды с monitored entities в Dynatrace, указывая идентификатор команды в metadata сущности. [See documentation](https://dt-url.net/ownership)",
    # 2. anomaly-detection-kubernetes-node
    "Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes nodes. Changing thresholds resets the observation period. Additional information can be found on our [documentation page](https://dt-url.net/wq02okj#node).": "Dynatrace автоматически обнаруживает широкий спектр типичных Kubernetes-проблем. Используйте эти параметры для настройки оповещений по узлам Kubernetes. Изменение порогов сбрасывает observation period. Дополнительные сведения см. на нашей [странице документации](https://dt-url.net/wq02okj#node).",
    # 3. anomaly-detection-kubernetes-namespace
    "Dynatrace automatically detects a wide range of common Kubernetes-related issues. Use these settings to configure alerts relevant to your Kubernetes namespace. Changing thresholds resets the observation period. Additional information can be found on our [documentation page](https://dt-url.net/wq02okj#namespace).": "Dynatrace автоматически обнаруживает широкий спектр типичных Kubernetes-проблем. Используйте эти параметры для настройки оповещений по namespace Kubernetes. Изменение порогов сбрасывает observation period. Дополнительные сведения см. на нашей [странице документации](https://dt-url.net/wq02okj#namespace).",
    # 4. elasticsearch-user-session-export-settings-v2 (7 paragraphs)
    "A user session export enables you to stream real user monitoring data from Dynatrace to an external data source where it can be leveraged as input for big data analytics, or for extending data retention.": "User session export позволяет передавать данные real user monitoring из Dynatrace во внешний источник данных, где их можно использовать как вход для big data analytics или для увеличения срока хранения данных.",
    "Streamed data includes all user sessions, user actions, events, and high-level timing and error data.": "В потоковые данные входят все user sessions, user actions, события и высокоуровневые тайминги и данные об ошибках.",
    "Use your existing analytics infrastructure to perform ad-hoc analysis on large numbers of user sessions, and combine this data with data mined from other sources.": "Используйте существующую analytics-инфраструктуру для ad-hoc анализа большого количества user-сессий и объединяйте эти данные с данными из других источников.",
    "Once enabled, user session export automatically sends JSON data for all monitored user sessions in your environment to the configured HTTPS endpoint.": "После включения user session export автоматически отправляет JSON-данные обо всех мониторимых user-сессиях вашего окружения на настроенный HTTPS-эндпоинт.",
    "You can also filter on a management zone per user session export.": "Также можно фильтровать по management zone отдельно для каждого user session export.",
    "You can define up to three user session exports to send specific data to different endpoints.": "Можно задать до трёх user session export, чтобы отправлять конкретные данные на разные эндпоинты.",
    "For complete details, visit [Configure user session exports](https://dt-url.net/user-session-exports).": "Подробнее см. [Configure user session exports](https://dt-url.net/user-session-exports).",
    # 5. preferences-privacy (2 paragraphs)
    "Use the settings on this page to mask the personal data of your end users and ensure your organization's compliance with data-privacy regulations, including [GDPR](https://dt-url.net/8m3u0pxk).": "Используйте параметры на этой странице, чтобы маскировать персональные данные конечных пользователей и обеспечивать соответствие вашей организации требованиям приватности, включая [GDPR](https://dt-url.net/8m3u0pxk).",
    "Unless otherwise stated, all privacy settings below apply to both the data captured with RUM Javascript and the data captured by OneAgent on the server side. These settings ensure that none of your end-users' personal data are stored by Dynatrace. For complete details on ensuring the data privacy of your end users, see [Data privacy and security](https://dt-url.net/zn03sq4) in Dynatrace Help.": "Если не указано иное, все приведённые ниже параметры приватности применяются и к данным, захватываемым RUM JavaScript, и к данным, захватываемым OneAgent на стороне сервера. Эти параметры гарантируют, что персональные данные конечных пользователей не сохраняются в Dynatrace. Подробнее о защите приватности конечных пользователей см. [Data privacy and security](https://dt-url.net/zn03sq4) в Dynatrace Help.",
    # 6. process-group-cloud-application-workload-detection
    "Enabling this setting merges processes of similar workloads into process groups, and consequently, services. Please note that [fine-grained process detection rules](https://www.dynatrace.com/support/help/shortlink/process-groups) will still be applied, while ignoring container or platform specific properties.": "Включение этого параметра объединяет процессы схожих workloads в process groups и, как следствие, в сервисы. Учтите, что [fine-grained process detection rules](https://www.dynatrace.com/support/help/shortlink/process-groups) всё равно применяются, игнорируя свойства, специфичные для контейнера или платформы.",
    # 7. processavailability (3 paragraphs)
    "This feature allows you to monitor if a minimum number of processes matching the specified monitoring rule are running on your host. If there aren't enough processes matching the rule, you receive an alert. If you also enable **Process instance snapshots**, you receive a detailed report on the activity of the most resource-consuming processes, as well as on the latest activity of the processes matching the rule.": "Эта функция позволяет мониторить, что на вашем хосте работает минимальное число процессов, попадающих под заданное monitoring rule. Если процессов, соответствующих правилу, недостаточно, вы получаете оповещение. Если дополнительно включить **Process instance snapshots**, вы получаете детальный отчёт об активности самых ресурсоёмких процессов и о последней активности процессов, попадающих под правило.",
    "In order to monitor the availability of a certain group of processes, you must first define a monitoring rule. Give your monitoring rule a unique name and add its detection rules to which Dynatrace will match the processes on your host.": "Чтобы мониторить доступность определённой группы процессов, сначала задайте monitoring rule. Дайте правилу уникальное имя и добавьте detection rules, по которым Dynatrace будет сопоставлять процессы на вашем хосте.",
    "For more details, see [Process availability](https://dt-url.net/v923x37)": "Подробнее см. [Process availability](https://dt-url.net/v923x37)",
    # 8. failure-detection-environment-parameters (2 paragraphs)
    "Failure detection parameters that determine whether a service call is considered successful or failed. Use failure detection rules (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.rules`) to configure which services these parameters apply to.": "Параметры failure detection, определяющие, считается ли вызов сервиса успешным или провалившимся. Используйте failure detection rules (`<your-dynatrace-url>//ui/settings/builtin:failure-detection.environment.rules`), чтобы задать, к каким сервисам применяются эти параметры.",
    "These settings are not applied to [Unified services](https://dt-url.net/gy03cmt).": "Эти настройки не применяются к [Unified services](https://dt-url.net/gy03cmt).",
}


PARAM_LABEL = {
    # Shared
    "Enabled": "Включено",
    "Name": "Имя",
    "Description": "Описание",
    "Value": "Значение",
    "Key": "Ключ",
    "Condition": "Условие",
    "Target": "Цель",
    "URL": "URL",
    "Email": "Email",
    "Activate": "Активировать",
    "Scope": "Scope",
    # 1. ownership-teams
    "Team name": "Имя команды",
    "Team identifier": "Идентификатор команды",
    "Supplementary identifiers": "Дополнительные идентификаторы",
    "Supplementary Identifier": "Дополнительный идентификатор",
    "Responsibilities": "Зоны ответственности",
    "Contact details": "Контактные данные",
    "Links": "Ссылки",
    "Additional information": "Дополнительная информация",
    "External ID": "External ID",
    "Development": "Development",
    "Security": "Security",
    "Operations": "Operations",
    "Infrastructure": "Infrastructure",
    "Line of Business": "Line of Business",
    "Integration type": "Тип интеграции",
    "Team": "Team",
    "Jira": "Jira",
    "Channel": "Канал",
    "Type": "Тип",
    "Project": "Project",
    "Default Assignee": "Default Assignee",
    # 2. anomaly-detection-kubernetes-node
    "Detect node readiness issues": "Обнаруживать проблемы readiness узла",
    "Detect problematic node conditions": "Обнаруживать проблемные condition узла",
    "Detect node CPU-request saturation": "Обнаруживать насыщение CPU-request узла",
    "Detect node memory-request saturation": "Обнаруживать насыщение memory-request узла",
    "Detect node pod-saturation": "Обнаруживать насыщение по подам узла",
    "node is not ready for at least": "узел не готов в течение как минимум",
    "within the last": "за последние",
    "node has problematic conditions for at least": "у узла проблемные condition в течение как минимум",
    "amount of requested CPU is higher than": "объём запрошенного CPU превышает",
    "of node CPU capacity for at least": "от ёмкости CPU узла в течение как минимум",
    "amount of requested memory is higher than": "объём запрошенной памяти превышает",
    "of node memory capacity for at least": "от ёмкости памяти узла в течение как минимум",
    "number of pods running on node is higher than": "число подов, работающих на узле, превышает",
    "of node capacity for at least": "от ёмкости узла в течение как минимум",
    # 3. anomaly-detection-kubernetes-namespace
    "Detect namespace CPU-request quota saturation": "Обнаруживать насыщение квоты CPU-request namespace",
    "Detect namespace CPU-limit quota saturation": "Обнаруживать насыщение квоты CPU-limit namespace",
    "Detect namespace memory-request quota saturation": "Обнаруживать насыщение квоты memory-request namespace",
    "Detect namespace memory-limit quota saturation": "Обнаруживать насыщение квоты memory-limit namespace",
    "Detect namespace pod quota saturation": "Обнаруживать насыщение квоты подов namespace",
    "amount of requested namespace CPU is above": "объём запрошенного CPU namespace превышает",
    "of quota for at least": "от квоты в течение как минимум",
    "amount of utilized namespace CPU is above": "объём используемого CPU namespace превышает",
    "amount of requested namespace memory is above": "объём запрошенной памяти namespace превышает",
    "amount of utilized namespace memory is above": "объём используемой памяти namespace превышает",
    "number of utilized namespace pods is above": "число используемых подов namespace превышает",
    # 4. elasticsearch-user-session-export-settings-v2
    "Define your endpoint": "Задайте эндпоинт",
    "Authentication": "Authentication",
    "Send data directly to Elasticsearch": "Отправлять данные напрямую в Elasticsearch",
    "Export scope, alerting, and advanced configuration": "Scope экспорта, оповещения и расширенная настройка",
    "Endpoint URL": "URL эндпоинта",
    "Enable user session export": "Включить user session export",
    "Content type": "Content type",
    "Use POST method (instead of PUT)": "Использовать метод POST (вместо PUT)",
    "Authentication type": "Тип аутентификации",
    "Basic authentication": "Basic authentication",
    "OAuth 2.0 (Early Adopter)": "OAuth 2.0 (Early Adopter)",
    "Name of the index where data is sent": "Имя индекса, куда отправляются данные",
    "Type of documents in the Elasticsearch index": "Тип документов в индексе Elasticsearch",
    "Management zone": "Management zone",
    "Disable notification": "Отключить уведомления",
    "Custom configuration properties": "Пользовательские свойства конфигурации",
    "User name": "Имя пользователя",
    "Password": "Пароль",
    "Grant type": "Grant type",
    "Access token URL": "URL access token",
    "Client ID": "Client ID",
    "Client secret": "Client secret",
    "Scope of access": "Scope доступа",
    "Send credentials": "Отправлять credentials",
    # 5. preferences-privacy
    "User tracking": "User tracking",
    "Opt-in mode": "Opt-in mode",
    "Do Not Track": "Do Not Track",
    "Mask personal data in URIs": "Маскировать персональные данные в URI",
    "Mask user actions (web applications only)": "Маскировать user actions (только web-приложения)",
    "Use persistent cookies for user tracking": "Использовать persistent cookies для user tracking",
    "Data-collection and opt-in mode": "Data-collection и opt-in mode",
    'Comply with "Do Not Track" browser settings': 'Соблюдать настройки браузера "Do Not Track"',
    # 6. process-group-cloud-application-workload-detection
    "Serverless Container Services": "Serverless Container Services",
    "Cloud Foundry": "Cloud Foundry",
    "Docker and Podman": "Docker and Podman",
    "Kubernetes/OpenShift": "Kubernetes/OpenShift",
    "Enable container detection for serverless container services": "Включить обнаружение контейнеров для serverless container services",
    "Enable cloud application and workload detection for Cloud Foundry": "Включить обнаружение cloud application и workload для Cloud Foundry",
    "Enable cloud application and workload detection for Docker and Podman": "Включить обнаружение cloud application и workload для Docker and Podman",
    "Enable cloud application and workload detection for Kubernetes/OpenShift": "Включить обнаружение cloud application и workload для Kubernetes/OpenShift",
    "ID calculation based on": "Расчёт ID на основе",
    "When namespace": "Когда namespace",
    "Namespace name": "Имя namespace",
    "Base pod name": "Имя base pod",
    "Container name": "Имя контейнера",
    "Stage": "Stage",
    "Product": "Product",
    "Match operator": "Match operator",
    # 7. processavailability
    "Monitoring rule name": "Имя monitoring rule",
    "Operating system": "Операционная система",
    "Minimum number of matching processes": "Минимальное число подходящих процессов",
    "Define detection rules": "Задать detection rules",
    "Properties": "Свойства",
    "Rule scope": "Scope правила",
    "Select process property": "Выберите property процесса",
    "Resource attribute": "Resource attribute",
    "Key must exist": "Ключ должен существовать",
    # 8. failure-detection-environment-parameters
    "HTTP response codes": "HTTP response codes",
    "HTTP 404 (broken links)": "HTTP 404 (broken links)",
    "Customize failure detection for specific exceptions and errors": "Настроить failure detection для конкретных исключений и ошибок",
    "HTTP response codes which indicate an error on the server side": "HTTP response codes, означающие ошибку на стороне сервера",
    "Treat missing HTTP response code as server side errors": "Считать отсутствующий HTTP response code ошибкой на стороне сервера",
    "HTTP response codes which indicate client side errors": "HTTP response codes, означающие ошибки на стороне клиента",
    "Treat missing HTTP response code as client side error": "Считать отсутствующий HTTP response code ошибкой на стороне клиента",
    "Consider 404 HTTP response codes as failures": "Считать HTTP-код 404 отказом",
    "Rules for broken links to related domains": "Правила для broken links на связанные домены",
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
}


PARAM_DESC = {
    # 1. ownership-teams
    "The team identifier is used to reference the team from any entity in Dynatrace. If you are using Kubernetes labels, keep in mind the 63 character limit that they enforce.": "Идентификатор команды используется для ссылки на команду из любой сущности Dynatrace. Если вы используете Kubernetes labels, учтите ограничение в 63 символа, накладываемое ими.",
    "The supplementary team identifiers can be optionally used in addition to the main team identifier to reference this team from any entity in Dynatrace. Up to 3 supplementary identifiers are supported.": "Дополнительные идентификаторы команды можно опционально использовать в дополнение к основному идентификатору, чтобы ссылаться на команду из любой сущности Dynatrace. Поддерживается до 3 дополнительных идентификаторов.",
    "Turn on all responsibility assignments that apply to this team.": "Включите все назначения ответственности, применимые к данной команде.",
    "Define options for messaging integration or other means of contacting this team.": "Задайте опции интеграции с мессенджерами или другие способы связи с командой.",
    "Include links to online resources where information relevant to this team"
    + TM_APOS
    + "s responsibilities can be found.": "Включите ссылки на онлайн-ресурсы, где можно найти информацию, относящуюся к зонам ответственности команды.",
    "Define key/value pairs that further describe this team "
    + TM_EMDASH
    + " for example, cost center, solution type, or business unit assignments.": "Задайте пары ключ/значение, дополнительно описывающие команду, например cost center, тип решения или принадлежность к business unit.",
    "This field should only be used for the automation purpose when importing team information.": "Это поле следует использовать только для целей автоматизации при импорте информации о команде.",
    "Responsible for developing and maintaining high quality software. Development teams are responsible for making code changes to address performance regressions, errors, or security vulnerabilities.": "Отвечает за разработку и сопровождение высококачественного ПО. Development-команды отвечают за изменения кода для устранения регрессий производительности, ошибок и уязвимостей безопасности.",
    "Responsible for the security posture of the organization. Teams with security responsibility must understand the impact, priority, and team responsible for addressing security vulnerabilities.": "Отвечает за состояние безопасности организации. Команды с зоной ответственности по security должны понимать влияние, приоритет и ответственную команду по устранению уязвимостей безопасности.",
    "Responsible for deploying and managing software, with a focus on high availability and performance. Teams with operations responsibilities needs to understand the impact, priority, and team responsible for addressing problems detected by Dynatrace.": "Отвечает за развёртывание и эксплуатацию ПО с упором на высокую доступность и производительность. Команды с зоной ответственности operations должны понимать влияние, приоритет и ответственную команду по устранению проблем, обнаруженных Dynatrace.",
    "Responsible for the administration, management, and support of the IT infrastructure including physical servers, virtualization, and cloud. Teams with infrastructure responsibility are responsible for addressing hardware issues, resource limits, and operating system vulnerabilities.": "Отвечает за администрирование, управление и поддержку IT-инфраструктуры, включая физические серверы, виртуализацию и cloud. Команды с зоной ответственности infrastructure отвечают за устранение проблем с железом, ресурсных ограничений и уязвимостей ОС.",
    "Responsible for ensuring that applications in development align with business needs and meet the usability requirements of users, stakeholders, customers, and external partners. Teams with line of business responsibility are responsible for understanding the customer experience and how it affects business goals.": "Отвечает за то, чтобы разрабатываемые приложения соответствовали бизнес-потребностям и требованиям к юзабилити со стороны пользователей, стейкхолдеров, клиентов и внешних партнёров. Команды с зоной ответственности line of business отвечают за понимание customer experience и его влияния на бизнес-цели.",
    # 2. anomaly-detection-kubernetes-node
    "Alerts if node has not been available for a given amount of time": "Оповещает, если узел был недоступен в течение заданного времени",
    "Alert if": "Оповестить, если",
    "Evaluates node condition 'Ready'": "Оценивает condition узла 'Ready'",
    "Evaluates node conditions  * MemoryPressure * DiskPressure * PIDPressure * OutOfDisk * NetworkUnavailable * KernelDeadlock * ReadonlyFilesystem * FrequentKubeletRestart * FrequentDockerRestart * FrequentContainerdRestart * KubeletUnhealthy * ContainerRuntimeUnhealthy * ContainerRuntimeProblem * CorruptDockerOverlay2 * FilesystemCorruptionProblem * FrequentGcfsdRestart * FrequentGcfsSnapshotterRestart * FrequentUnregisterNetDevice * GcfsdUnhealthy * GcfsSnapshotterMissingLayer * GcfsSnapshotterUnhealthy * KubeletProblem": "Оценивает condition узла  * MemoryPressure * DiskPressure * PIDPressure * OutOfDisk * NetworkUnavailable * KernelDeadlock * ReadonlyFilesystem * FrequentKubeletRestart * FrequentDockerRestart * FrequentContainerdRestart * KubeletUnhealthy * ContainerRuntimeUnhealthy * ContainerRuntimeProblem * CorruptDockerOverlay2 * FilesystemCorruptionProblem * FrequentGcfsdRestart * FrequentGcfsSnapshotterRestart * FrequentUnregisterNetDevice * GcfsdUnhealthy * GcfsSnapshotterMissingLayer * GcfsSnapshotterUnhealthy * KubeletProblem",
    "Number of running pods in percent of the node's maximum pod capacity": "Число работающих подов в процентах от максимальной ёмкости подов узла",
    # 3. anomaly-detection-kubernetes-namespace
    "Alerts if almost no CPU-request quota left in namespace": "Оповещает, если в namespace почти не осталось квоты CPU-request",
    "Alerts if almost no CPU-limit quota left in namespace": "Оповещает, если в namespace почти не осталось квоты CPU-limit",
    "Alerts if almost no memory-request quota left in namespace": "Оповещает, если в namespace почти не осталось квоты memory-request",
    "Alerts if almost no memory-limit quota left in namespace": "Оповещает, если в namespace почти не осталось квоты memory-limit",
    "Alerts if almost no pod quota left in namespace": "Оповещает, если в namespace почти не осталось квоты подов",
    # 4. elasticsearch-user-session-export-settings-v2
    "Dynatrace will send JSON data periodically to this endpoint. You can also pause and disable an endpoint to stop the data stream from Dynatrace to your endpoint.": "Dynatrace будет периодически отправлять JSON-данные на этот эндпоинт. Также можно поставить эндпоинт на паузу или отключить, чтобы остановить поток данных из Dynatrace.",
    "Dynatrace can automatically send bulk data to Elasticsearch. You can use an SSL certificate, basic authentication or OAuth 2.0 to secure access. For Dynatrace SaaS installations, the Elasticsearch instance must be publicly reachable by the Dynatrace Cluster.": "Dynatrace может автоматически отправлять bulk-данные в Elasticsearch. Для защиты доступа можно использовать SSL-сертификат, basic authentication или OAuth 2.0. Для установок Dynatrace SaaS instance Elasticsearch должен быть публично доступен из Dynatrace Cluster.",
    "Activate this if you want to export user session data to your own Elasticsearch cluster. If you run Elasticsearch 7, make sure to enter \\_doc as the type. For Elasticsearch 8 omit the type. If you really want to use a type, then you have to add include\\_type\\_name=true when creating your Elasticsearch index. See more information in the Dynatrace help.": "Активируйте, если хотите экспортировать данные user-сессий в собственный кластер Elasticsearch. Если у вас Elasticsearch 7, обязательно укажите \\_doc как type. Для Elasticsearch 8 type не указывайте. Если всё же хотите использовать type, добавьте include\\_type\\_name=true при создании индекса Elasticsearch. Подробнее в Dynatrace help.",
    "Define the scope of your export by using a specific management zone. You can also disable UI notifications for failing exports, or add special settings provided by Dynatrace support for troubleshooting.": "Задайте scope экспорта через конкретную management zone. Также можно отключить UI-уведомления о неудачных экспортах или добавить специальные параметры, предоставленные Dynatrace support для troubleshooting.",
    "Restrict exported sessions to management zone": "Ограничить экспортируемые сессии конкретной management zone",
    "Here you can set additional properties for this export configuration. Changing these values might only be necessary in some rare cases. Please contact support before changing this field.": "Здесь можно задать дополнительные свойства для этой конфигурации экспорта. Изменять эти значения может понадобиться только в редких случаях. До изменения этого поля свяжитесь с поддержкой.",
    "The scope of access you are requesting": "Запрашиваемый scope доступа",
    # 5. preferences-privacy
    "To provide your end users with the ability to decide for themselves if their activities should be tracked to measure application performance and usage, enable opt-in mode.": "Чтобы дать конечным пользователям возможность самим решать, нужно ли отслеживать их активность для измерения производительности и использования приложения, включите opt-in mode.",
    'Most modern web browsers have a privacy feature called ["Do Not Track"](https://dt-url.net/sb3n0pnl) that individual users may have enabled on their devices. Customize how Dynatrace should behave when it encounters this setting.': 'У большинства современных web-браузеров есть функция приватности ["Do Not Track"](https://dt-url.net/sb3n0pnl), которую отдельные пользователи могут включить на своих устройствах. Настройте поведение Dynatrace при обнаружении этой настройки.',
    "Dynatrace captures the URIs and request headers sent from desktop and mobile browsers. Dynatrace also captures request data on the server-side to enable detailed performance analysis of your applications. For complete details, visit [Mask personal data in URIs](https://dt-url.net/mask-personal-data-in-URIs).  URIs, query strings, headers, exception messages and data captured for request attributes can contain personal data. When this setting is enabled, Dynatrace automatically detects UUIDs, credit card numbers, email addresses, IP addresses, and other IDs and replaces those values with placeholders. The personal data is then masked in PurePath analysis, error analysis, user action naming for RUM, and elsewhere in Dynatrace.": "Dynatrace захватывает URI и request-заголовки, отправляемые из desktop- и mobile-браузеров. Dynatrace также захватывает данные запросов на стороне сервера для детального анализа производительности приложений. Подробнее см. [Mask personal data in URIs](https://dt-url.net/mask-personal-data-in-URIs).  URI, query-строки, заголовки, сообщения об исключениях и данные, захватываемые для request attributes, могут содержать персональные данные. При включении этого параметра Dynatrace автоматически обнаруживает UUID, номера кредитных карт, email-адреса, IP-адреса и другие идентификаторы и заменяет их значения placeholder'ами. Затем персональные данные маскируются в PurePath analysis, error analysis, именовании user actions для RUM и в других местах Dynatrace.",
    'When Dynatrace detects a user action that triggers a page load or an AJAX/XHR action. To learn more about masking user actions, visit [Mask user actions](https://dt-url.net/mask-user-action).  When Dynatrace detects a user action that triggers a page load or an AJAX/XHR action, it constructs a name for the user action based on:  * User event type (click on..., loading of page..., or keypress on...) * Title, caption, label, value, ID, className, or other available property of the related HTML element (for example, an image, button, checkbox, or text input field).  In most instances, the default approach to user-action naming works well, resulting in user-action names such as:  * click on "Search" on page /search.html * keypress on "Feedback" on page /contact.html * touch on "Homescreen" of page /list.jsf  In rare circumstances, confidential data (for example, email addresses, usernames, or account numbers) can be unintentionally included in user action names because the confidential data itself is included in an HTML element label, attribute, or other value (for example, click on "my Account Number: 1231231"...). If such confidential data appears in your application\'s user action names, enable the Mask user action names setting. This setting replaces specific HTML element names and values with generic HTML element names. With user-action name masking enabled, the user action names listed above appear as:  * click on INPUT on page /search.html * keypress on TEXTAREA on page /contact.html * touch on DIV of page /list.jsf': 'Когда Dynatrace обнаруживает user action, инициирующее загрузку страницы или AJAX/XHR-действие. Подробнее о маскировании user actions см. [Mask user actions](https://dt-url.net/mask-user-action).  Когда Dynatrace обнаруживает user action, инициирующее загрузку страницы или AJAX/XHR-действие, оно формирует имя user action на основе:  * Типа user-события (click on..., loading of page... или keypress on...) * Title, caption, label, value, ID, className или другого доступного свойства связанного HTML-элемента (например, image, button, checkbox или text input field).  В большинстве случаев подход по умолчанию к именованию user-action работает хорошо, и имена выглядят так:  * click on "Search" on page /search.html * keypress on "Feedback" on page /contact.html * touch on "Homescreen" of page /list.jsf  В редких случаях конфиденциальные данные (например, email-адреса, имена пользователей или номера счетов) могут непреднамеренно попасть в имена user actions, потому что сами эти данные содержатся в label, атрибуте или другом значении HTML-элемента (например, click on "my Account Number: 1231231"...). Если такие конфиденциальные данные появляются в именах user actions вашего приложения, включите параметр маскирования имён user actions. Этот параметр заменяет конкретные имена и значения HTML-элементов на generic-имена. С включённым маскированием имён user-actions перечисленные выше имена выглядят так:  * click on INPUT on page /search.html * keypress on TEXTAREA on page /contact.html * touch on DIV of page /list.jsf',
    "When enabled, Dynatrace places a [persistent cookie](https://dt-url.net/313o0p4n) on all end-user devices to identify returning users.": "При включении Dynatrace размещает [persistent cookie](https://dt-url.net/313o0p4n) на всех устройствах конечных пользователей для идентификации возвращающихся пользователей.",
    "With [Data-collection and opt-in mode](https://dt-url.net/7l3p0p3h) enabled, Real User Monitoring data isn't captured until dtrum.enable() is called for specific user sessions.": "При включённом [Data-collection и opt-in mode](https://dt-url.net/7l3p0p3h) данные Real User Monitoring не захватываются, пока для конкретных user-сессий не вызвано dtrum.enable().",
    # 6. process-group-cloud-application-workload-detection
    "Enable this setting to  * Detect containers based on captured cloud-vendor metadata such as e.g. AWS ECS / Fargate, Azure Container Apps, [and many more](https://dt-url.net/2m02q7b). * Container resource metrics (Container group instance entities) and [related screens](https://www.dynatrace.com/support/help/shortlink/container-groups).": "Включите этот параметр, чтобы  * Обнаруживать контейнеры на основе захваченных metadata cloud-vendor, например AWS ECS / Fargate, Azure Container Apps, [и многих других](https://dt-url.net/2m02q7b). * Получать метрики ресурсов контейнеров (сущности Container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups).",
    "Enable this setting to get  * Processes of Cloud Foundry application instances merged into process groups by Cloud Foundry application. * Container resource metrics (Container group instance entities) and [related screens](https://www.dynatrace.com/support/help/shortlink/container-groups).": "Включите этот параметр, чтобы получать  * Процессы экземпляров Cloud Foundry-приложений, объединённые в process groups по Cloud Foundry-приложению. * Метрики ресурсов контейнеров (сущности Container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups).",
    "Enable this setting for plain Docker and Podman environments to get  * Container resource metrics (Container group instance entities) and [related screens](https://www.dynatrace.com/support/help/shortlink/container-groups). * Docker support requires OneAgent 1.257+. * Podman support requires OneAgent 1.267+.": "Включите этот параметр для чистых окружений Docker и Podman, чтобы получать  * Метрики ресурсов контейнеров (сущности Container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups). * Docker поддерживается с OneAgent 1.257+. * Podman поддерживается с OneAgent 1.267+.",
    "Enable this setting to get  * Insights into your Kubernetes namespaces, workloads and pods (cloud application namespace, cloud application and cloud application instance and entities). * Container resource metrics (container group instance entities) and [related screens](https://www.dynatrace.com/support/help/shortlink/container-groups). * Similar workloads merged into process groups based on defined rules (see below). * Version detection for services that run in Kubernetes workloads.": "Включите этот параметр, чтобы получать  * Инсайты по namespaces, workloads и pods Kubernetes (сущности cloud application namespace, cloud application и cloud application instance). * Метрики ресурсов контейнеров (сущности container group instance) и [связанные экраны](https://www.dynatrace.com/support/help/shortlink/container-groups). * Объединение схожих workloads в process groups по заданным правилам (см. ниже). * Определение версии для сервисов, работающих в Kubernetes-workloads.",
    "Define rules to merge similar Kubernetes workloads into process groups.  You can use workload properties like namespace name, base pod name or container name as well as the [environment variables DT\\_RELEASE\\_STAGE and DT\\_RELEASE\\_PRODUCT](https://dt-url.net/sb02v2a) for grouping processes of similar workloads. The first applicable rule will be applied. If no rule matches, "
    + TM_LQUOTE
    + "Namespace name"
    + TM_RQUOTE
    + " + "
    + TM_LQUOTE
    + "Base pod name"
    + TM_RQUOTE
    + " + "
    + TM_LQUOTE
    + "Container name"
    + TM_RQUOTE
    + " is used as fallback.": 'Задайте правила объединения схожих Kubernetes-workloads в process groups.  Можно использовать свойства workload, например имя namespace, имя base pod или имя контейнера, а также [переменные окружения DT\\_RELEASE\\_STAGE и DT\\_RELEASE\\_PRODUCT](https://dt-url.net/sb02v2a) для группировки процессов схожих workloads. Применяется первое подходящее правило. Если ни одно не подошло, в качестве fallback используется "Имя namespace" + "Имя base pod" + "Имя контейнера".',
    'E.g. "cloud-credential-operator-" for "cloud-credential-operator-5ff6dbff57-gszgq"': 'Например, "cloud-credential-operator-" для "cloud-credential-operator-5ff6dbff57-gszgq"',
    "If Product is enabled and has no value, it defaults to Base pod name": "Если Product включён и не имеет значения, по умолчанию используется имя base pod",
    # 7. processavailability
    "Select the operating systems on which the monitoring rule should be applied.": "Выберите операционные системы, к которым нужно применить monitoring rule.",
    "Specify a minimum number of processes matching the monitoring rule. An alert is triggered if any host falls below this threshold.": "Укажите минимальное число процессов, попадающих под monitoring rule. Если на каком-либо хосте число процессов опускается ниже этого порога, срабатывает оповещение.",
    "Define process detection rules by selecting a process property and a condition. Each monitoring rule can have multiple detection rules associated with it.": "Задайте detection rules, выбрав property процесса и условие. У каждого monitoring rule может быть несколько связанных detection rules.",
    "Set of additional key-value properties to be attached to the triggered event. You can retrieve the available property keys using the [Events API v2](https://dt-url.net/9622g1w). Additionally any Host resource attribute can be dynamically substituted (agent 1.325+).": "Набор дополнительных key-value свойств, прикрепляемых к сработавшему событию. Доступные ключи свойств можно получить через [Events API v2](https://dt-url.net/9622g1w). Дополнительно любой Host resource attribute может быть динамически подставлен (agent 1.325+).",
    "* $contains(svc) "
    + TM_ENDASH
    + " Matches if svc appears anywhere in the process property value. * $eq(svc.exe) "
    + TM_ENDASH
    + " Matches if svc.exe matches the process property value exactly. * $prefix(svc) "
    + TM_ENDASH
    + " Matches if app matches the prefix of the process property value. * $suffix(svc.py) "
    + TM_ENDASH
    + " Matches if svc.py matches the suffix of the process property value.  For example, $suffix(svc.py) would detect processes named loyaltysvc.py and paymentssvc.py.  For more details, see [Process availability](https://dt-url.net/v923x37).": "* $contains(svc), совпадает, если svc встречается в значении property процесса. * $eq(svc.exe), совпадает, если svc.exe точно совпадает со значением property процесса. * $prefix(svc), совпадает, если app совпадает с префиксом значения property процесса. * $suffix(svc.py), совпадает, если svc.py совпадает с суффиксом значения property процесса.  Например, $suffix(svc.py) обнаружит процессы с именами loyaltysvc.py и paymentssvc.py.  Подробнее см. [Process availability](https://dt-url.net/v923x37).",
    "Host resource attributes are dimensions enriching the host including custom metadata which are user-defined key-value pairs that you can assign to hosts monitored by Dynatrace.  By defining custom metadata, you can enrich the monitoring data with context specific to your organization's needs, such as environment names, team ownership, application versions, or any other relevant details.  See [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw).  Note: Starting from version 1.325 host resource attributes are supported in addition to host custom metadata.": "Host resource attributes, это dimensions, обогащающие хост, в том числе custom metadata, которые представляют собой пары ключ-значение, назначаемые хостам, мониторимым Dynatrace.  Задавая custom metadata, можно обогащать данные мониторинга контекстом, специфичным для нужд вашей организации: имена окружений, team ownership, версии приложений и любые другие релевантные детали.  См. [Define tags and metadata for hosts](https://dt-url.net/w3hv0kbw).  Примечание: начиная с версии 1.325 host resource attributes поддерживаются в дополнение к host custom metadata.",
    "Type 'dt.' for key hints.": "Введите 'dt.' для подсказок по ключам.",
    "Type '{' for placeholder hints.": "Введите '{' для подсказок по placeholder'ам.",
    "When enabled, the condition requires a resource attribute to exist and match the constraints; when disabled, the key is optional but must still match the constrains if it is present.": "При включении условие требует, чтобы resource attribute существовал и удовлетворял ограничениям; при отключении ключ опционален, но если он присутствует, всё равно должен удовлетворять ограничениям.",
    "This string has to match a required format.  * `$match(ver*_1.2.?)` "
    + TM_ENDASH
    + " Matches string with wildcards: `*` any number (including zero) of characters and `?` exactly one character. * `$contains(production)` "
    + TM_ENDASH
    + " Matches if `production` appears anywhere in the host metadata value. * `$eq(production)` "
    + TM_ENDASH
    + " Matches if `production` matches the host metadata value exactly. * `$prefix(production)` "
    + TM_ENDASH
    + " Matches if `production` matches the prefix of the host metadata value. * `$suffix(production)` "
    + TM_ENDASH
    + " Matches if `production` matches the suffix of the host metadata value.  Available logic operations:  * `$not($eq(production))` "
    + TM_ENDASH
    + " Matches if the host metadata value is different from `production`. * `$and($prefix(production),$suffix(main))` "
    + TM_ENDASH
    + " Matches if host metadata value starts with `production` and ends with `main`. * `$or($prefix(production),$suffix(main))` "
    + TM_ENDASH
    + " Matches if host metadata value starts with `production` or ends with `main`.  Brackets **(** and **)** that are part of the matched property **must be escaped with a tilde (~)**": "Эта строка должна совпадать с требуемым форматом.  * `$match(ver*_1.2.?)`, совпадает со строкой с wildcards: `*`, любое число (включая ноль) символов, `?`, ровно один символ. * `$contains(production)`, совпадает, если `production` встречается в значении host metadata. * `$eq(production)`, совпадает, если `production` точно совпадает со значением host metadata. * `$prefix(production)`, совпадает, если `production` совпадает с префиксом значения host metadata. * `$suffix(production)`, совпадает, если `production` совпадает с суффиксом значения host metadata.  Доступные логические операции:  * `$not($eq(production))`, совпадает, если значение host metadata отличается от `production`. * `$and($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` и заканчивается на `main`. * `$or($prefix(production),$suffix(main))`, совпадает, если значение host metadata начинается с `production` или заканчивается на `main`.  Скобки **(** и **)**, входящие в сопоставляемое property, **должны экранироваться тильдой (~)**",
    # 8. failure-detection-environment-parameters
    "HTTP 404 response codes are thrown when a web server can't find a certain page. 404s are classified as broken links on the client side and therefore aren't considered to be service failures. By enabling this setting, you can have 404s treated as server-side service failures.": "HTTP-коды 404 возвращаются, когда web-сервер не может найти определённую страницу. 404 классифицируются как broken links на стороне клиента и поэтому не считаются service failures. Включив этот параметр, можно трактовать 404 как server-side service failures.",
    "If your application relies on other hosts at other domains, add the associated domain names here. Once configured, Dynatrace will consider 404s thrown by hosts at these domains to be service failures related to your application.": "Если ваше приложение зависит от других хостов на других доменах, добавьте сюда соответствующие имена доменов. После настройки Dynatrace будет считать 404 от хостов на этих доменах service failures, связанными с вашим приложением.",
    "Define exceptions which indicate that an entire service call should not be considered as failed. E.g. an exception indicating that the client aborted the operation. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will be considered successful. Compared to ignored exceptions, the request will be considered successful even if other exceptions occur in the same request.": "Задайте исключения, означающие, что весь вызов сервиса не должен считаться провалившимся. Например, исключение о том, что клиент прервал операцию. Если на **entry node** сервиса возникает исключение, совпадающее с одним из заданных шаблонов, вызов считается успешным. В отличие от ignored exceptions, запрос считается успешным даже при появлении других исключений в этом же запросе.",
    "Some exceptions that are thrown by legacy or 3rd-party code indicate a specific response, not an error. Use this setting to instruct Dynatrace to treat such exceptions as non-failed requests. If an exception matching any of the defined patterns occurs on the **entry node** of the service, it will not be considered as a failure. Other exceptions occurring at the same request might still mark the request as failed.": "Некоторые исключения, выбрасываемые legacy- или 3rd-party-кодом, означают конкретный ответ, а не ошибку. Используйте этот параметр, чтобы Dynatrace трактовал такие исключения как непровалившиеся запросы. Если на **entry node** сервиса возникает исключение, совпадающее с одним из заданных шаблонов, оно не считается failure. Прочие исключения в этом же запросе всё равно могут пометить запрос как провалившийся.",
    "There may be situations where your application code handles exceptions gracefully in a manner that these failures aren't detected by Dynatrace. Use this setting to define specific gracefully-handled exceptions that should be treated as service failures.": "Возможны ситуации, когда код вашего приложения корректно обрабатывает исключения так, что Dynatrace не обнаруживает эти отказы. Используйте этот параметр, чтобы задать конкретные gracefully-обрабатываемые исключения, которые должны трактоваться как service failures.",
    "Some custom error situations are only detectable via a return value or other means. To support such cases, [define a request attribute](https://dt-url.net/ys5k0p4y) that captures the required data. Then define a custom error rule that determines if the request has failed based on the value of the request attribute.": "Некоторые пользовательские ошибочные ситуации можно обнаружить только через возвращаемое значение или иными способами. Для таких случаев [задайте request attribute](https://dt-url.net/ys5k0p4y), захватывающий нужные данные. Затем задайте custom error rule, определяющее по значению request attribute, провалился ли запрос.",
    "The pattern will match if it is contained within the actual class name.": "Шаблон совпадает, если он содержится в фактическом имени класса.",
    "Optionally, define an exception message pattern. The pattern will match if the actual exception message contains the pattern.": "При желании задайте шаблон сообщения исключения. Шаблон совпадает, если фактическое сообщение исключения содержит шаблон.",
}

# Structural canon (shared with L4-AG.1a.1-10 / L4-AF).
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
