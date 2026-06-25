# -*- coding: utf-8 -*-
"""L4-AG.1a.4 builder: 30 builtin-*.md schema-table files (2.2-2.4 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Class L4-AF schema-table (## Authentication + ## Parameters + Schema-ID/Scope
row + GET endpoints). Anchor canon: L4-AG.1a.3 _build_schemas_l4ag1a3.py.

Включает «семью» openpipeline-routing (12 идентичных файлов с одинаковой
структурой RoutingEntry). Описание схемы у них тоже одно и то же
(«Contains configuration of routing»), различие только в DISPLAY_NAME
(spans/events/metrics/...).

Mojibake byte-keys preserved verbatim:
  - synthetic-browser-kpms `userâs`  (single-mojibake U+00E2 of U+2019)
"""

import os, io

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-devobs-agent-optin.md",
    "builtin-openpipeline-spans-routing.md",
    "builtin-openpipeline-events-routing.md",
    "builtin-openpipeline-metrics-routing.md",
    "builtin-hyperscaler-authentication-aws-connection.md",
    "builtin-openpipeline-bizevents-routing.md",
    "builtin-kubernetes-security-posture-management.md",
    "builtin-logmonitoring-log-dpp-rules.md",
    "builtin-openpipeline-events-sdlc-routing.md",
    "builtin-openpipeline-user-events-routing.md",
    "builtin-sessionreplay-web-resource-capturing.md",
    "builtin-openpipeline-davis-events-routing.md",
    "builtin-openpipeline-usersessions-routing.md",
    "builtin-rum-mobile-beacon-endpoint.md",
    "builtin-openpipeline-system-events-routing.md",
    "builtin-bizevents-processing-buckets-rule.md",
    "builtin-openpipeline-davis-problems-routing.md",
    "builtin-rum-web-beacon-domain-origins.md",
    "builtin-appsec-rule-settings.md",
    "builtin-openpipeline-events-security-routing.md",
    "builtin-openpipeline-security-events-routing.md",
    "builtin-rum-web-custom-injection-rules.md",
    "builtin-remote-environment.md",
    "builtin-rum-web-rum-javascript-updates.md",
    "builtin-appsec-notification-alerting-profile.md",
    "builtin-rum-resource-timing-origins.md",
    "builtin-dt-javascript-runtime-allowed-outbound-connections.md",
    "builtin-rum-web-capture-custom-properties.md",
    "builtin-synthetic-browser-kpms.md",
    "builtin-synthetic-http-outage-handling.md",
]

# Schema heading display-name. EN product/tech terms kept.
# Технические API-имена в скобках с точкой (events.sdlc, davis.events, ...)
# и продуктовые названия (bizevents, AWS, ...) НЕ переводим.
DISPLAY_NAME = {
    "Enable Observability For Developers": "Enable Observability For Developers",
    "Ingest routing configuration (spans)": "Конфигурация маршрутизации ingest (spans)",
    "Ingest routing configuration (events)": "Конфигурация маршрутизации ingest (события)",
    "Ingest routing configuration (metrics)": "Конфигурация маршрутизации ingest (метрики)",
    "AWS Connections": "AWS Connections",
    "Ingest routing configuration (bizevents)": "Конфигурация маршрутизации ingest (bizevents)",
    "Security Posture Management: Kubernetes": "Security Posture Management: Kubernetes",
    "Processing": "Обработка",
    "Ingest routing configuration (events.sdlc)": "Конфигурация маршрутизации ingest (events.sdlc)",
    "Ingest routing configuration (user.events)": "Конфигурация маршрутизации ingest (user.events)",
    "Resource capture for Session Replay": "Захват ресурсов для Session Replay",
    "Ingest routing configuration (davis.events)": "Конфигурация маршрутизации ingest (davis.events)",
    "Ingest routing configuration (usersessions)": "Конфигурация маршрутизации ingest (usersessions)",
    "Beacon endpoint settings": "Настройки эндпоинта beacon",
    "Ingest routing configuration (system.events)": "Конфигурация маршрутизации ingest (system.events)",
    "Business event bucket assignment": "Назначение бакетов для Business events",
    "Ingest routing configuration (davis.problems)": "Конфигурация маршрутизации ingest (davis.problems)",
    "Beacon origins for CORS": "Источники beacon для CORS",
    "Vulnerability Analytics: Monitoring rules for third-party vulnerabilities": "Vulnerability Analytics: правила мониторинга уязвимостей сторонних компонентов",
    "Ingest routing configuration (events.security)": "Конфигурация маршрутизации ingest (events.security)",
    "Ingest routing configuration (security.events)": "Конфигурация маршрутизации ingest (security.events)",
    "Define custom injection rules": "Задание правил пользовательского внедрения",
    "Remote environments": "Удалённые окружения",
    "RUM JavaScript updates": "Обновления JavaScript-кода RUM",
    "Vulnerability alerting profiles": "Профили оповещений об уязвимостях",
    "Advanced correlation": "Расширенная корреляция",
    "Limit outbound connections": "Ограничение исходящих соединений",
    "Custom Properties Capture Restrictions": "Ограничения захвата пользовательских свойств",
    "Key performance metrics": "Ключевые метрики производительности",
    "Outage handling": "Обработка простоев",
}

# Whole-line schema descriptions (replaced as `\n` + EN + `\n` -> `\n` + RU + `\n`).
SCHEMA_DESC = {
    # 1. devobs-agent-optin
    "Observability For Developers allows you to instantly access the code-level data you need without adding code or waiting for deployment. With Observability For Developers, you can troubleshoot faster and understand complex, modern, cloud-native applications.": "Observability For Developers даёт мгновенный доступ к данным уровня кода без добавления кода или ожидания развёртывания. С Observability For Developers можно быстрее проводить траблшутинг и понимать сложные современные cloud-native приложения.",
    "Note: Enabling Observability For Developers consumes Container Monitoring units.": "Примечание: включение Observability For Developers расходует Container Monitoring units.",
    "For further details, see the [Code Monitoring documentation](https://docs.dynatrace.com/docs/manage/dynatrace-platform-subscription/capabilities/container-monitoring#code-monitoring)": "Подробнее см. [Code Monitoring documentation](https://docs.dynatrace.com/docs/manage/dynatrace-platform-subscription/capabilities/container-monitoring#code-monitoring)",
    # 2-3-4-6-9-10-12-13-15-17-20-21. openpipeline-*-routing (12 шт., один и тот же текст)
    "Contains configuration of routing": "Содержит конфигурацию маршрутизации",
    # 5. hyperscaler-authentication-aws-connection (BOM stripped from link text)
    "Available connections for [AWS for Workflows](https://dt-url.net/s803q9r). A connection is used to authenticate against your AWS account. The retrieved, temporary AWS credentials are used to execute the AWS workflow actions.": "Доступные подключения для [AWS for Workflows](https://dt-url.net/s803q9r). Подключение используется для аутентификации в AWS-аккаунте. Полученные временные учётные данные AWS применяются для выполнения действий AWS workflow.",
    # 7. kubernetes-security-posture-management (BOM stripped from link text)
    "[Kubernetes Security Posture Management (KSPM)](https://dt-url.net/b303utv) helps you assess and ensure the security and compliance of a Kubernetes environment by adhering to security best practices and regulatory standards.": "[Kubernetes Security Posture Management (KSPM)](https://dt-url.net/b303utv) помогает оценить и обеспечить безопасность и соответствие требованиям Kubernetes-окружения, придерживаясь лучших практик безопасности и регуляторных стандартов.",
    "Note: You can [enable Kubernetes Security Posture Management](https://dt-url.net/o003ue9) per environment or cluster.": "Примечание: [enable Kubernetes Security Posture Management](https://dt-url.net/o003ue9) можно на уровне окружения или кластера.",
    # 8. logmonitoring-log-dpp-rules
    "Logs can be transformed through processing rules. Note that rules are processed sequentially, making the order important; a different rule order could give different results.": "Логи можно преобразовывать через правила обработки. Учтите, что правила обрабатываются последовательно, поэтому порядок важен: другой порядок правил может дать другой результат.",
    # 11. sessionreplay-web-resource-capturing (BOM stripped)
    "Resource capture allows you to capture and store stylesheets during user session recording. For details, see [Resource capturing](https://dt-url.net/sr-resource-capturing).": "Захват ресурсов позволяет захватывать и сохранять стили во время записи пользовательских сессий. Подробнее см. [Resource capturing](https://dt-url.net/sr-resource-capturing).",
    # 14. rum-mobile-beacon-endpoint (BOM stripped, две строки с трейлинг-пробелами)
    "Define where OneAgent is to send your iOS and Android monitoring data.  ": "Задайте, куда OneAgent должен отправлять данные мониторинга iOS и Android.  ",
    "**Note:** To use an Environment ActiveGate as beacon endpoint, beacon forwarding must be enabled in the ActiveGate config first. Learn more about how to configure an [Environment ActiveGate](https://dt-url.net/90r039v) or how to use [OneAgent as a beacon endpoint](https://dt-url.net/hr4e0ijr).": "**Примечание:** чтобы использовать Environment ActiveGate как эндпоинт beacon, сначала включите пересылку beacon в конфигурации ActiveGate. Подробнее о настройке [Environment ActiveGate](https://dt-url.net/90r039v) или об использовании [OneAgent as a beacon endpoint](https://dt-url.net/hr4e0ijr).",
    # 16. bizevents-processing-buckets-rule (BOM stripped)
    "Business events can be stored in different buckets. The first user-defined rule that matches will determine bucket assignment. If no rules match, the default bucket will be used.": "Business events можно хранить в разных бакетах. Первое пользовательское правило, которое совпадёт, определит назначение бакета. Если ни одно правило не совпадёт, будет использован бакет по умолчанию.",
    "Learn to create custom buckets and more by visiting [our documentation](https://dt-url.net/4c034xt).": "О создании пользовательских бакетов и других возможностях см. [our documentation](https://dt-url.net/4c034xt).",
    # 18. rum-web-beacon-domain-origins
    "Specify the RUM beacon origins that must be accepted by OneAgent and ActiveGate. Dynatrace tries to match each of your defined rules against the `Origin` request header of your incoming beacons and copies the origin from the matched header to the `Access-Control-Allow-Origin` response header. Beacon origins that aren't part of the defined rule set will be rejected and the beacon response will return HTTP 403. If your rule set is empty, beacon origins will be accepted from any domain. Note that when you enable the first rule, applications that don't match the rule no longer collect RUM data.": "Укажите источники RUM beacon, которые должны приниматься OneAgent и ActiveGate. Dynatrace сопоставляет каждое заданное правило с заголовком запроса `Origin` входящих beacon и копирует источник из совпавшего заголовка в заголовок ответа `Access-Control-Allow-Origin`. Источники beacon, не входящие в набор правил, отклоняются, а ответ beacon возвращает HTTP 403. Если набор правил пуст, источники beacon принимаются с любого домена. Учтите: при включении первого правила приложения, не совпадающие с правилом, перестают собирать RUM-данные.",
    # 19. appsec-rule-settings
    "The global third-party vulnerability detection control defines the default monitoring mode. To override the default, define custom monitoring rules here. Note that monitoring rules are ordered; the first matching rule applies.": "Глобальное управление определением уязвимостей сторонних компонентов задаёт режим мониторинга по умолчанию. Чтобы переопределить значение по умолчанию, задайте здесь пользовательские правила мониторинга. Учтите: правила мониторинга упорядочены, применяется первое совпавшее правило.",
    # 22. rum-web-custom-injection-rules
    "Define custom injection rules to control when and where RUM is automatically injected into your application's pages.": "Задайте правила пользовательского внедрения, чтобы контролировать, когда и куда RUM автоматически внедряется в страницы приложения.",
    # 23. remote-environment (BOM stripped)
    "Configure connections to other Dynatrace environments for cross-environment capabilities (e.g. dashboards)": "Настройте подключения к другим окружениям Dynatrace для межсредовых возможностей (например, дашбордов)",
    "For help on remote environments, see [Remote environment API documentation](https://dt-url.net/lc5n0p4z)": "О работе с удалёнными окружениями см. [Remote environment API documentation](https://dt-url.net/lc5n0p4z)",
    # 24. rum-web-rum-javascript-updates
    "Define the RUM JavaScript version to be used globally (in the global settings) or for a specific web application (in the application settings). In order to profit from RUM JavaScript updates, it is recommended to choose a dynamic version like **Latest stable** or **Previous stable**. If dynamic versions are not an option for you, choose **Custom** instead. This option refers to a static version defined in the Custom RUM JavaScript version (`<your-dynatrace-url>//ui/settings/builtin:rum.web.custom-rum-javascript-version`) environment settings.": "Задайте версию RUM JavaScript, которая будет использоваться глобально (в общих настройках) или для конкретного веб-приложения (в настройках приложения). Чтобы получать преимущества от обновлений RUM JavaScript, рекомендуется выбирать динамическую версию, например **Latest stable** или **Previous stable**. Если динамические версии не подходят, выберите **Custom**. Этот вариант ссылается на статическую версию, заданную в настройках окружения Custom RUM JavaScript version (`<your-dynatrace-url>//ui/settings/builtin:rum.web.custom-rum-javascript-version`).",
    # 25. appsec-notification-alerting-profile
    "Vulnerability alerting profiles enable you to set up alert-filtering rules that are based on the risk level of detected vulnerabilities. This allows you to control which conditions result in security notifications and which don't.": "Профили оповещений об уязвимостях позволяют настроить правила фильтрации оповещений на основе уровня риска обнаруженных уязвимостей. Это даёт возможность контролировать, какие условия приводят к уведомлениям безопасности, а какие нет.",
    # 26. rum-resource-timing-origins
    "OneAgent uses the `Server-Timing` response header to communicate RUM correlation data to the RUM JavaScript. For cross-origin requests, the RUM JavaScript can only access the `Server-Timing` header value if the `Timing-Allow-Origin` header permits the origin of the request. Therefore, OneAgent automatically adds the `Timing-Allow-Origin` header to your web application's response if it is not already set by your application. The `Timing-Allow-Origin` header controls access not only to the `Server-Timing` header value, but also to detailed resource timing data.": "OneAgent использует заголовок ответа `Server-Timing` для передачи данных корреляции RUM в RUM JavaScript. Для cross-origin запросов RUM JavaScript может получить доступ к значению заголовка `Server-Timing`, только если заголовок `Timing-Allow-Origin` разрешает источник запроса. Поэтому OneAgent автоматически добавляет заголовок `Timing-Allow-Origin` в ответ веб-приложения, если приложение его ещё не установило. Заголовок `Timing-Allow-Origin` управляет доступом не только к значению заголовка `Server-Timing`, но и к подробным данным resource timing.",
    "By default, access is granted to all origins. Add rules to restrict access to specified origins.": "По умолчанию доступ предоставляется всем источникам. Добавьте правила, чтобы ограничить доступ указанными источниками.",
    # 27. dt-javascript-runtime-allowed-outbound-connections
    "You can limit the accessibility of public endpoints from functions running in the Dynatrace JavaScript Runtime, for example, the backends of apps and functions written in the Dashboards, Notebooks and Automations app.": "Можно ограничить доступ к публичным эндпоинтам из функций, запущенных в Dynatrace JavaScript Runtime, например к backend'ам приложений и функций, написанных в Dashboards, Notebooks и Automations app.",
    # 28. rum-web-capture-custom-properties
    "Define specific properties to restrict event/session capturing, with options to allow by property name or allow all properties.": "Задайте конкретные свойства для ограничения захвата событий и сессий: можно разрешать по имени свойства или разрешить все свойства.",
    # 29. synthetic-browser-kpms (BOM stripped)
    "Select the [key performance metric](https://dt-url.net/kpms) that best represents the user experience of this synthetic monitor.": "Выберите [key performance metric](https://dt-url.net/kpms), которая лучше всего отражает пользовательский опыт этого synthetic-монитора.",
    # triple-mojibake: `user` + U+00E2 U+0080 U+0099 + `s` = bytes c3 a2 c2 80 c2 99
    "**Visually complete** is the default metric for load and XHR actions. It measures how long it takes for the visible portion of each user" + chr(0xE2) + chr(0x80) + chr(0x99) + "s browser screen to be fully rendered.": "**Visually complete**: метрика по умолчанию для load- и XHR-действий. Она измеряет, сколько времени нужно для полной отрисовки видимой части экрана браузера пользователя.",
    "The key performance metric for custom actions is always **User action duration**.": "Ключевая метрика производительности для пользовательских действий всегда **User action duration**.",
    # 30. synthetic-http-outage-handling
    "Dynatrace can generate problems for both global outages and/or local outages based on the availability of either all configured locations or only individual locations over consecutive runs.": "Dynatrace может генерировать проблемы как для глобальных, так и для локальных простоев на основе доступности всех настроенных расположений или только отдельных расположений в последовательных прогонах.",
}

# Parameter table col-1 label (text before `\`code\``).
PARAM_LABEL = {
    # 1. devobs-agent-optin
    "Enable Observability For Developers": "Включить Observability For Developers",
    # 2-3-4-6-9-10-12-13-15-17-20-21. openpipeline-*-routing (12 файлов)
    "Routing for pipelines": "Маршрутизация для pipeline",
    "Enabled": "Включено",
    "Pipeline Type": "Тип pipeline",
    "Pipeline ID": "ID pipeline",
    "Builtin Pipeline ID": "ID встроенного pipeline",
    "Query which determines whether the record should be routed to the target pipeline of this rule.": "Запрос, определяющий, должна ли запись быть направлена в целевой pipeline этого правила.",
    "Description": "Описание",
    # 5. hyperscaler-authentication-aws-connection
    "Name": "Имя",
    "Credential Type": "Тип учётных данных",
    "Role ARN": "Role ARN",
    "Policy ARNs": "Policy ARNs",
    # 7. kubernetes-security-posture-management
    "Enable Security Posture Management": "Включить Security Posture Management",
    # 8. logmonitoring-log-dpp-rules
    "Active": "Активно",
    "Rule name": "Имя правила",
    "Matcher": "Сопоставитель",
    "Processor definition": "Определение процессора",
    "Log sample": "Образец лога",
    # 11. sessionreplay-web-resource-capturing
    "Enable resource capture": "Включить захват ресурсов",
    "URL exclusion": "Исключение URL",
    # 14. rum-mobile-beacon-endpoint
    "Type": "Тип",
    "URL": "URL",
    # 16. bizevents-processing-buckets-rule
    "Bucket": "Бакет",
    "Matcher (DQL)": "Сопоставитель (DQL)",
    # 18. rum-web-beacon-domain-origins / 26. rum-resource-timing-origins
    "Pattern": "Шаблон",
    # 19. appsec-rule-settings
    "Control": "Управление",
    "Property": "Свойство",
    "Condition operator": "Условный оператор",
    "Condition value": "Значение условия",
    # 22. rum-web-custom-injection-rules
    "Enable rule": "Включить правило",
    "Operator": "Оператор",
    "URL pattern": "URL-шаблон",
    "Rule": "Правило",
    # 23. remote-environment
    "Remote environment URI": "URI удалённого окружения",
    "Network scope": "Сетевая область",
    "Token": "Токен",
    # 24. rum-web-rum-javascript-updates
    "Choose version": "Выбор версии",
    # 25. appsec-notification-alerting-profile
    "Alert for the following events:": "Оповещать о следующих событиях:",
    "Alert only if the following management zone is affected (optional)": "Оповещать только при затронутой management zone (необязательно)",
    "Risk Levels": "Уровни риска",
    # 27. dt-javascript-runtime-allowed-outbound-connections
    "Limit outbound connections to endpoints in the allowlist": "Ограничить исходящие соединения эндпоинтами в allowlist",
    "Allowlist": "Allowlist",
    # 28. rum-web-capture-custom-properties
    "List of allowed custom event properties": "Список разрешённых пользовательских свойств события",
    "List of allowed custom session properties": "Список разрешённых пользовательских свойств сессии",
    "Field name": "Имя поля",
    "Field name validation should be case-insensitive": "Валидация имени поля должна быть нечувствительной к регистру",
    "Datatype": "Тип данных",
    # 29. synthetic-browser-kpms
    "Load action key performance metric": "Ключевая метрика производительности load-действия",
    "XHR action key performance metric": "Ключевая метрика производительности XHR-действия",
    # 30. synthetic-http-outage-handling
    "Generate a problem and send an alert when the monitor is unavailable at all configured locations.": "Генерировать проблему и отправлять оповещение, когда монитор недоступен во всех настроенных расположениях.",
    "Alert if all locations are unable to access my web application": "Оповестить, если все расположения не могут получить доступ к веб-приложению",
    "Generate a problem and send an alert when the monitor is unavailable for one or more consecutive runs at any location.": "Генерировать проблему и отправлять оповещение, когда монитор недоступен в течение одного или нескольких последовательных прогонов в любом расположении.",
    "Alert if at least": "Оповестить, если как минимум",
    "are unable to access my web application": "не могут получить доступ к веб-приложению",
}

# Parameter table col-3 description (when not just `-` and not enum-tail).
PARAM_DESC = {
    # 5. hyperscaler-authentication-aws-connection
    "The ARN of the AWS role that should be assumed": "ARN AWS-роли, которую следует принять",
    "An optional list of policies that can be used to restrict the AWS role": "Опциональный список политик, которыми можно ограничить AWS-роль",
    # 7. kubernetes-security-posture-management
    "Follow the [installation instructions](https://dt-url.net/4x23ut5) to deploy the Security Posture Management components.": "Следуйте [installation instructions](https://dt-url.net/4x23ut5), чтобы развернуть компоненты Security Posture Management.",
    # 8. logmonitoring-log-dpp-rules
    "Sample log in JSON format.": "Образец лога в формате JSON.",
    # 11. sessionreplay-web-resource-capturing
    "When turned on, Dynatrace captures resources for up to 0.1% of user sessions recorded with Session Replay. For details, see [Resource capture](https://dt-url.net/sr-resource-capturing).": "Если включено, Dynatrace захватывает ресурсы для не более 0,1% сессий пользователей, записанных через Session Replay. Подробнее см. [Resource capture](https://dt-url.net/sr-resource-capturing).",
    "Add exclusion rules to avoid the capture of resources from certain pages.": "Добавьте правила исключений, чтобы избежать захвата ресурсов с определённых страниц.",
    # 14. rum-mobile-beacon-endpoint
    "This must be a valid beacon endpoint URL.  The URL must start with 'http://' or 'https://'. Environment ActiveGate URL must end with '/mbeacon/{{environment-id}}', Instrumented Web Server URL must end with '/dtmb'.": "Должен быть валидным URL эндпоинта beacon.  URL должен начинаться с 'http://' или 'https://'. URL Environment ActiveGate должен заканчиваться на '/mbeacon/{{environment-id}}', URL Instrumented Web Server заканчивается на '/dtmb'.",
    # 16. bizevents-processing-buckets-rule
    "Events will be stored in the selected bucket. Analyze bucket contents in the log & event viewer. (`<your-dynatrace-url>//ui/logs-events?advancedQueryMode=true&query=fetch+bizevents`)": "События сохраняются в выбранном бакете. Содержимое бакета можно анализировать в log & event viewer. (`<your-dynatrace-url>//ui/logs-events?advancedQueryMode=true&query=fetch+bizevents`)",
    "[See our documentation](https://dt-url.net/bp234rv)": "[See our documentation](https://dt-url.net/bp234rv)",
    # 22. rum-web-custom-injection-rules — длинный head перед enum
    "**Example**:  **For the URL:**  `http://www.example.com:8080/lorem/ipsum.jsp?mode=desktop`  A rule can be specified on the URL pattern:  `/lorem/ipsum.jsp`  Using the operator:  `URL ends with`  **Result:**  If URL ends with .jsp do not inject the JavaScript library": "**Пример**:  **Для URL:**  `http://www.example.com:8080/lorem/ipsum.jsp?mode=desktop`  Правило можно задать на URL-шаблоне:  `/lorem/ipsum.jsp`  С использованием оператора:  `URL ends with`  **Результат:**  если URL заканчивается на .jsp, не внедрять JavaScript-библиотеку",
    # 23. remote-environment
    "Specify the full URI to the remote environment. Your local environment will have to be able to connect this URI on a network level.": "Укажите полный URI удалённого окружения. Локальное окружение должно иметь возможность сетевого подключения к этому URI.",
    "* External: The remote environment is located in an another network. * Internal: The remote environment is located in the same network. * Cluster: The remote environment is located in the same cluster.  Dynatrace SaaS can only use External.": "* External: удалённое окружение находится в другой сети. * Internal: удалённое окружение находится в той же сети. * Cluster: удалённое окружение находится в том же кластере.  Dynatrace SaaS поддерживает только External.",
    "Provide a valid token created on the remote environment.": "Укажите валидный токен, созданный в удалённом окружении.",
    # 27. dt-javascript-runtime-allowed-outbound-connections
    "If enabled, the Dynatrace JavaScript Runtime will only be able to connect to the specified hosts.": "Если включено, Dynatrace JavaScript Runtime сможет подключаться только к указанным хостам.",
    "A host that app backends should be able to connect to.": "Хост, к которому должны подключаться backend'ы приложений.",
}

# Structural canon (shared with L4-AG.1a.1 / L4-AG.1a.2 / L4-AG.1a.3 / L4-AF).
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
    if label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL[label]
    d = cdesc
    # Global ENUM substring-replace runs BEFORE per-line, so by here cdesc
    # may already contain RU «Возможные значения:» instead of EN marker.
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


import re as _re

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
