# -*- coding: utf-8 -*-
"""L4-AG.1a.2 builder: 34 builtin-*.md schema-table files (1.7-2.1 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Same schema-table CLASS as L4-AG.1a.1 (## Authentication + ## Parameters +
Schema-ID/Scope row + GET endpoints). EN-locks: frontmatter, both H1 lines,
`* Published <date>`, Schema-ID/groups/Scope row content, endpoint GET rows,
URLs, code identifiers, type column, Required/Optional value.

Translated: schema heading display-name, schema description paragraphs,
Authentication + Parameters section heads, auth paragraph, Property/Description
column headers, parameter label cells, parameter description cells.

Anchor canon: L4-AG.1a.1 _build_schemas_l4ag1a.py.

Source quirks preserved verbatim (L93):
  - mojibake U+00E2 in `environmentâs` (activegate-token)
  - mojibake U+00C2 U+00AE in `DavisÂ®` (mobile-notifications)
  - double-space `.  E.g` (custom-unit)
BOM U+EFBBBF stripped (L4M canon) inside link-text in several files.
"""

import os, io

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-monitored-technologies-java.md",
    "builtin-attributes-preferences.md",
    "builtin-monitored-technologies-nginx.md",
    "builtin-host-process-groups-monitoring-state.md",
    "builtin-monitored-technologies-python.md",
    "builtin-ebpf-service-discovery.md",
    "builtin-monitored-technologies-nodejs.md",
    "builtin-eec-remote.md",
    "builtin-rum-web-custom-rum-javascript-version.md",
    "builtin-nettracer-traffic.md",
    "builtin-monitored-technologies-dotnet.md",
    "builtin-app-transition-kubernetes.md",
    "builtin-monitored-technologies-open-tracing-native.md",
    "builtin-monitored-technologies-varnish.md",
    "builtin-rum-ip-determination.md",
    "builtin-mobile-notifications.md",
    "builtin-monitoring-slo-normalization.md",
    "builtin-ibmmq-queue-sharing-group.md",
    "builtin-monitored-technologies-apache.md",
    "builtin-rum-overload-prevention.md",
    "builtin-rum-web-custom-configuration-properties.md",
    "builtin-rum-custom-name.md",
    "builtin-crashdump-analytics.md",
    "builtin-rum-mobile-request-errors.md",
    "builtin-settings-mutedrequests.md",
    "builtin-endpoint-detection-rules-opt-in.md",
    "builtin-custom-unit.md",
    "builtin-host-monitoring-aix-kernel-extension.md",
    "builtin-ibmmq-ims-bridges.md",
    "builtin-unified-services-endpoint-metrics.md",
    "builtin-deployment-oneagent-default-mode.md",
    "builtin-synthetic-multiprotocol-scheduling.md",
    "builtin-activegate-token.md",
    "builtin-cloud-cloudfoundry.md",
]

# Schema heading display-name. EN-tech-product-names kept (Java/Python/Nginx/etc).
DISPLAY_NAME = {
    "Java": "Java",
    "Preferences": "Настройки",
    "Nginx": "Nginx",
    "Process group monitoring": "Мониторинг групп процессов",
    "Python": "Python",
    "eBPF Service Discovery": "eBPF Service Discovery",
    "Node.js": "Node.js",
    "Extension Execution Controller": "Extension Execution Controller",
    "Custom RUM JavaScript version": "Пользовательская версия RUM JavaScript",
    "NetTracer traffic": "Трафик NetTracer",
    ".NET": ".NET",
    "Kubernetes app": "Приложение Kubernetes",
    "Envoy": "Envoy",
    "Varnish Cache": "Varnish Cache",
    "IP determination": "Определение IP",
    "Dynatrace mobile app": "Мобильное приложение Dynatrace",
    "Service-level objective setup": "Настройка целей уровня обслуживания",
    "IBM MQ queue sharing groups": "Группы совместного использования очередей IBM MQ",
    "Apache HTTP Server": "Apache HTTP Server",
    "RUM overload prevention": "Предотвращение перегрузки RUM",
    "Custom configuration properties": "Пользовательские свойства конфигурации",
    "Application name and type": "Имя и тип приложения",
    "Crash dump analytics": "Аналитика крэш-дампов",
    "Request errors": "Ошибки запросов",
    "Muted requests": "Приглушённые запросы",
    "Enable endpoint detection": "Включение определения эндпоинтов",
    "Custom units": "Пользовательские единицы",
    "AIX kernel extension": "Расширение ядра AIX",
    "IBM MQ IMS bridges": "Мосты IBM MQ IMS",
    "Endpoint metrics": "Метрики эндпоинтов",
    "OneAgent default mode": "Режим OneAgent по умолчанию",
    "Frequency and locations": "Частота и расположения",
    "Network security": "Сетевая безопасность",
    "Cloud Foundry": "Cloud Foundry",
}

# Schema description lines (whole-line `\n` + EN + `\n` -> `\n` + RU + `\n`).
SCHEMA_DESC = {
    # monitored-technologies family: enabled-by-default (Java/Nginx/Node.js/.NET/Apache)
    "By default, Java monitoring is enabled on all hosts. If you want to disable Java monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг Java включён на всех хостах. Если вы хотите отключить мониторинг Java на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable Java monitoring only on selected hosts, disable global Java monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг Java только на отдельных хостах, отключите глобальный мониторинг Java и включите его на этих хостах через их настройки.",
    "By default, Nginx monitoring is enabled on all hosts. If you want to disable Nginx monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг Nginx включён на всех хостах. Если вы хотите отключить мониторинг Nginx на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable Nginx monitoring only on selected hosts, disable global Nginx monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг Nginx только на отдельных хостах, отключите глобальный мониторинг Nginx и включите его на этих хостах через их настройки.",
    "By default, Node.js monitoring is enabled on all hosts. If you want to disable Node.js monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг Node.js включён на всех хостах. Если вы хотите отключить мониторинг Node.js на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable Node.js monitoring only on selected hosts, disable global Node.js monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг Node.js только на отдельных хостах, отключите глобальный мониторинг Node.js и включите его на этих хостах через их настройки.",
    "By default, .NET monitoring is enabled on all hosts. If you want to disable .NET monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг .NET включён на всех хостах. Если вы хотите отключить мониторинг .NET на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable .NET monitoring only on selected hosts, disable global .NET monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг .NET только на отдельных хостах, отключите глобальный мониторинг .NET и включите его на этих хостах через их настройки.",
    "By default, Apache HTTP Server monitoring is enabled on all hosts. If you want to disable Apache HTTP Server monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг Apache HTTP Server включён на всех хостах. Если вы хотите отключить мониторинг Apache HTTP Server на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable Apache HTTP Server monitoring only on selected hosts, disable global Apache HTTP Server monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг Apache HTTP Server только на отдельных хостах, отключите глобальный мониторинг Apache HTTP Server и включите его на этих хостах через их настройки.",
    # monitored-technologies family: disabled-by-default (Python/Envoy/Varnish Cache)
    "By default, Python monitoring is disabled on all hosts. If you want to enable Python monitoring on selected hosts, enable it on these hosts via their settings.": "По умолчанию мониторинг Python отключён на всех хостах. Если вы хотите включить мониторинг Python на отдельных хостах, включите его на этих хостах через их настройки.",
    "If you want to disable Python monitoring only on selected hosts, enable global Python monitoring and disable it on these hosts via their settings.": "Если вы хотите отключить мониторинг Python только на отдельных хостах, включите глобальный мониторинг Python и отключите его на этих хостах через их настройки.",
    "By default, Envoy monitoring is disabled on all hosts. If you want to enable Envoy monitoring on selected hosts, enable it on these hosts via their settings.": "По умолчанию мониторинг Envoy отключён на всех хостах. Если вы хотите включить мониторинг Envoy на отдельных хостах, включите его на этих хостах через их настройки.",
    "If you want to disable Envoy monitoring only on selected hosts, enable global Envoy monitoring and disable it on these hosts via their settings.": "Если вы хотите отключить мониторинг Envoy только на отдельных хостах, включите глобальный мониторинг Envoy и отключите его на этих хостах через их настройки.",
    "By default, Varnish Cache monitoring is disabled on all hosts. If you want to enable Varnish Cache monitoring on selected hosts, enable it on these hosts via their settings.": "По умолчанию мониторинг Varnish Cache отключён на всех хостах. Если вы хотите включить мониторинг Varnish Cache на отдельных хостах, включите его на этих хостах через их настройки.",
    "If you want to disable Varnish Cache monitoring only on selected hosts, enable global Varnish Cache monitoring and disable it on these hosts via their settings.": "Если вы хотите отключить мониторинг Varnish Cache только на отдельных хостах, включите глобальный мониторинг Varnish Cache и отключите его на этих хостах через их настройки.",
    # attributes-preferences
    "Define the default behavior of persisting OpenTelemetry attributes. You can either choose to store all attributes except certain blocked attributes or only store explicitly allowed attributes.": "Задайте поведение сохранения атрибутов OpenTelemetry по умолчанию. Вы можете хранить все атрибуты, кроме определённых заблокированных, или хранить только явно разрешённые атрибуты.",
    # host-process-groups-monitoring-state
    "Enable or disable monitoring for certain process groups on this host": "Включите или отключите мониторинг для определённых групп процессов на этом хосте",
    # ebpf-service-discovery
    "This OneAgent module enables the discovery of active services on the network. It is a very low-overhead, safe way of identifying services that need to be monitored.": "Этот модуль OneAgent позволяет обнаруживать активные сервисы в сети. Это безопасный способ идентификации сервисов, требующих мониторинга, с минимальной нагрузкой.",
    # eec-remote (BOM stripped from link text)
    "Extension Execution Controller configuration for ActiveGate deployment": "Конфигурация Extension Execution Controller для развёртывания ActiveGate",
    # rum-web-custom-rum-javascript-version
    "Define a custom RUM JavaScript version to be added to the pool of versions for web applications to choose from.": "Задайте пользовательскую версию RUM JavaScript для добавления в пул версий, из которых могут выбирать веб-приложения.",
    # nettracer-traffic (colon instead of em-dash for "X is a tool" pattern)
    "NetTracer is an open source tool for tracing TCP events and collecting network connection metrics on Linux.": "NetTracer: open source инструмент для трассировки TCP-событий и сбора метрик сетевых соединений в Linux.",
    # app-transition-kubernetes
    "Unlock an improved experience with the new Kubernetes app.": "Раскройте улучшенный опыт работы с новым приложением Kubernetes.",
    # rum-ip-determination (3-line description including bold subheading)
    "These settings are used for web applications, mobile apps and custom applications.": "Эти настройки используются для веб-приложений, мобильных приложений и пользовательских приложений.",
    "**Identify client IP addresses**": "**Идентификация клиентских IP-адресов**",
    "Client IP addresses are automatically determined based on HTTP request header. If your client IP addresses use a different header, create a custom rule so that the IP addresses can be identified.": "Клиентские IP-адреса автоматически определяются на основе HTTP-заголовка запроса. Если клиентские IP-адреса используют другой заголовок, создайте пользовательское правило для их идентификации.",
    # mobile-notifications
    "The Dynatrace mobile application for iOS and Android enables users to receive customized push notifications on their mobile devices. Refer to the instructions below to set up the Dynatrace mobile app's access within this environment.": "Мобильное приложение Dynatrace для iOS и Android позволяет пользователям получать настраиваемые push-уведомления на свои мобильные устройства. Смотрите инструкции ниже для настройки доступа мобильного приложения Dynatrace в этом окружении.",
    # monitoring-slo-normalization (BOM stripped from link text)
    "Use these settings to configure service-level objective evaluations.": "Используйте эти настройки для конфигурации оценок целей уровня обслуживания.",
    # ibmmq-queue-sharing-group
    "A queue sharing group defines a group of queue managers that can access the same shared queues on z/OS. Dynatrace needs to know which queue managers and shared queues belong to which queue sharing group for the end-to-end tracing on z/OS.": "Группа совместного использования очередей определяет группу менеджеров очередей, которые могут обращаться к одним и тем же общим очередям на z/OS. Dynatrace должен знать, какие менеджеры очередей и общие очереди относятся к какой группе совместного использования очередей для сквозной трассировки на z/OS.",
    # rum-overload-prevention (BOM stripped from link text)
    "Adjust the limit below to control the overall cluster performance capacity and prevent unexpected high consumption of your license volume.": "Отрегулируйте лимит ниже для управления общей производительностью кластера и предотвращения неожиданно высокого потребления объёма лицензии.",
    # rum-web-custom-configuration-properties
    "Here you can set additional JavaScript tag properties that are specific to your application. To do this, type key-value pairs defined using (=).": "Здесь вы можете задать дополнительные свойства JavaScript-тега, специфичные для приложения. Для этого введите пары ключ-значение, определённые через (=).",
    # rum-custom-name (single line, source has no blank line between sentences)
    "This name is used to refer to your custom application throughout this Dynatrace environment. Be sure that your application has a meaningful name.": "Это имя используется для обозначения пользовательского приложения во всём этом окружении Dynatrace. Убедитесь, что у приложения осмысленное имя.",
    "To use a different icon to represent your application, change the application type.": "Чтобы использовать другую иконку для представления приложения, измените тип приложения.",
    # crashdump-analytics (BOM stripped from link text)
    "Dynatrace automatically detects application crashes on Windows and Linux and analyzes the crashes' core dumps. Here you can manage crash dump analytics. For details on crash analysis, see the [documentation](https://docs.dynatrace.com/docs/shortlink/crash-analysis)": "Dynatrace автоматически обнаруживает сбои приложений в Windows и Linux и анализирует core-дампы этих сбоев. Здесь вы можете управлять аналитикой крэш-дампов. Подробнее об анализе сбоев см. [documentation](https://docs.dynatrace.com/docs/shortlink/crash-analysis)",
    # rum-mobile-request-errors
    "Create exclusion rules to define which HTTP response codes should not be treated as errors. By default, Dynatrace considers all 4xx and 5xx response status codes to be web request errors.": "Создайте правила исключения, чтобы определить, какие HTTP-коды ответа не должны считаться ошибками. По умолчанию Dynatrace считает все коды состояния ответа 4xx и 5xx ошибками веб-запросов.",
    # settings-mutedrequests (BOM stripped from link text)
    "Configuration for specifying Muted requests for particular Service. Each Service could have several Muted requests.": "Конфигурация для указания приглушённых запросов для конкретного сервиса. У каждого сервиса может быть несколько приглушённых запросов.",
    'Dynatrace enables you to mute automatic alerts for selected, unimportant service requests. This will also exclude them from the service chart so that you can focus on the performance of requests that affect your customers. You can learn more about Muted requests in our [help](https://dt-url.net/ze62t5p "Visit dynatrace.com")': 'Dynatrace позволяет приглушать автоматические оповещения для отдельных неважных запросов сервиса. Это также исключит их из диаграммы сервиса, чтобы вы могли сосредоточиться на производительности запросов, влияющих на клиентов. Узнайте больше о приглушённых запросах в нашей [help](https://dt-url.net/ze62t5p "Visit dynatrace.com")',
    # endpoint-detection-rules-opt-in (BOM stripped from 2 link texts)
    "Enable SDv2 endpoint detection rules (`<your-dynatrace-url>/builtin:endpoint-detection-rules`) instead of the hard-coded ones. See [Service Detection v2 documentation](https://dt-url.net/lu030qq) and [community post](https://dt-url.net/r2230n9) for details.": "Включите правила определения эндпоинтов SDv2 (`<your-dynatrace-url>/builtin:endpoint-detection-rules`) вместо жёстко закодированных. Подробнее см. [Service Detection v2 documentation](https://dt-url.net/lu030qq) и [community post](https://dt-url.net/r2230n9).",
    # custom-unit
    "Here you can create custom units.": "Здесь вы можете создавать пользовательские единицы.",
    # host-monitoring-aix-kernel-extension (BOM stripped from link text)
    "Dynatrace can automatically inject OneAgent deep code-monitoring modules for AIX monitoring. Otherwise, manual instrumentation is required for the monitoring of Java, Apache, WebLogic, and Websphere applications on AIX. For details, see [Install OneAgent on AIX](https://dt-url.net/l24t0pm1).": "Dynatrace может автоматически инжектировать модули глубокого мониторинга кода OneAgent для мониторинга AIX. В противном случае требуется ручное инструментирование для мониторинга приложений Java, Apache, WebLogic и Websphere на AIX. Подробнее см. [Install OneAgent on AIX](https://dt-url.net/l24t0pm1).",
    # ibmmq-ims-bridges (colon instead of em-dash for "X is the component" pattern)
    "An IMS bridge is the component of IBM MQ for z/OS that allows direct access to the IMS system. Dynatrace needs to know which queue managers and queues belong to which IMS bridge for the end-to-end tracing on z/OS.": "IMS-мост: компонент IBM MQ для z/OS, обеспечивающий прямой доступ к системе IMS. Dynatrace должен знать, какие менеджеры очередей и очереди относятся к какому IMS-мосту для сквозной трассировки на z/OS.",
    # unified-services-endpoint-metrics (BOM stripped from link text)
    "This setting allows to turn on or off classic endpoint metrics. Please check the [documentation](https://dt-url.net/gy03cmt) for details.": "Эта настройка позволяет включить или отключить классические метрики эндпоинтов. Подробнее см. [documentation](https://dt-url.net/gy03cmt).",
    # deployment-oneagent-default-mode (BOM stripped from link text)
    "You can configure which OneAgent [monitoring mode](https://dt-url.net/8703q1z) will be used by default for OneAgent installation commands provided in the Dynatrace web UI. This does not affect OneAgent installer behavior. OneAgent installed without the monitoring mode parameter will run in Full-Stack Monitoring mode.": "Вы можете настроить, какой [режим мониторинга](https://dt-url.net/8703q1z) OneAgent будет использоваться по умолчанию для команд установки OneAgent, предоставляемых в веб-интерфейсе Dynatrace. Это не влияет на поведение инсталлятора OneAgent. OneAgent, установленный без параметра режима мониторинга, будет работать в режиме Full-Stack Monitoring.",
    # synthetic-multiprotocol-scheduling
    "Select how frequently this monitor should run at each enabled location.": "Выберите, как часто этот монитор должен выполняться в каждом включённом расположении.",
    # activegate-token: source has 3-char mojibake `â` (cp1252-encoded U+2019) — verbatim EN key.
    "Dynatrace assures out-of-the-box connection security between Dynatrace environmentâs elements.": "Dynatrace обеспечивает безопасность соединения между элементами окружения Dynatrace из коробки.",
    # cloud-cloudfoundry
    "Use this page to connect your Cloud Foundry foundation to Dynatrace for monitoring. Please have your Cloud Foundry API target URL, your authentication endpoint and your Cloud Foundry username and password ready.": "Используйте эту страницу для подключения Cloud Foundry к Dynatrace для мониторинга. Подготовьте целевой URL Cloud Foundry API, endpoint аутентификации и имя пользователя и пароль Cloud Foundry.",
}

# Parameter table col-1 label (before `\`code\``).
PARAM_LABEL = {
    "Monitor Java": "Мониторить Java",
    "Monitor Nginx": "Мониторить Nginx",
    "Monitor Python": "Мониторить Python",
    "Monitor Node.js": "Мониторить Node.js",
    "Monitor Envoy": "Мониторить Envoy",
    "Monitor Varnish Cache": "Мониторить Varnish Cache",
    "Monitor Apache HTTP Server": "Мониторить Apache HTTP Server",
    "Monitor .NET": "Мониторить .NET",
    "Enable .NET Core": "Включить .NET Core",
    "Process group": "Группа процессов",
    "Monitoring state": "Состояние мониторинга",
    "Performance profile": "Профиль производительности",
    "Choose custom version": "Выбрать пользовательскую версию",
    "Enable service discovery": "Включить обнаружение сервисов",
    "Enable NetTracer traffic network monitoring": "Включить сетевой мониторинг трафика NetTracer",
    "New Kubernetes experience": "Новый опыт Kubernetes",
    "Client IP header name": "Имя HTTP-заголовка с IP клиента",
    "Enabled": "Включено",
    "Normalize error budget": "Нормализовать бюджет ошибок",
    "Queue sharing group name": "Имя группы совместного использования очередей",
    "Queue managers": "Менеджеры очередей",
    "Queue manager name": "Имя менеджера очередей",
    "Queues": "Очереди",
    "Shared queues": "Общие очереди",
    "Maximum user actions per minute": "Максимум пользовательских действий в минуту",
    "Custom configuration property": "Пользовательское свойство конфигурации",
    "Update application name": "Обновить имя приложения",
    "Update application type": "Обновить тип приложения",
    "Crash dump analytics": "Аналитика крэш-дампов",
    "Exclude response codes": "Исключить коды ответа",
    "Muted request names": "Имена приглушённых запросов",
    "Enable Endpoint detection rules": "Включить правила определения эндпоинтов",
    "Unit name": "Имя единицы",
    "Unit plural name": "Имя единицы во множественном числе",
    "Unit symbol": "Символ единицы",
    "Unit description": "Описание единицы",
    "Use global settings": "Использовать глобальные настройки",
    "Allow AIX kernel extension": "Разрешить расширение ядра AIX",
    "IMS bridge name": "Имя IMS-моста",
    "Enable classic endpoint metrics": "Включить классические метрики эндпоинтов",
    "OneAgent default monitoring mode": "Режим мониторинга OneAgent по умолчанию",
    "Frequency": "Частота",
    "Locations": "Расположения",
    "Location": "Расположение",
    "Manually enforce ActiveGate token authentication": "Принудительно включить аутентификацию по токену ActiveGate вручную",
    "Enable notifications about ActiveGate tokens expiration dates": "Включить уведомления о датах истечения токенов ActiveGate",
    "Name this connection": "Имя этого подключения",
    "Cloud Foundry API Target": "Целевой Cloud Foundry API",
    "Cloud Foundry Authentication Endpoint": "Endpoint аутентификации Cloud Foundry",
    "Cloud Foundry Username": "Имя пользователя Cloud Foundry",
    "Cloud Foundry Password": "Пароль Cloud Foundry",
    "ActiveGate group": "Группа ActiveGate",
}

# Parameter table col-3 description (when not just `-` and not enum-tail).
# BOM strip via _normalize already; link-text kept inside the value here.
PARAM_DESC = {
    "When disabled, Dynatrace can only detect services in Full stack mode.": "Если отключено, Dynatrace может обнаруживать сервисы только в режиме Full Stack.",
    "When disabled, OneAgent won't use NetTracer to collect network data from containers. Disabled by default. Applies only to Linux hosts. Requires OneAgent 1.231+.": "Если отключено, OneAgent не будет использовать NetTracer для сбора сетевых данных из контейнеров. Отключено по умолчанию. Применяется только к Linux-хостам. Требует OneAgent 1.231+.",
    'Select performance profile for Extension Execution Controller [Documentation](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles")': 'Выберите профиль производительности для Extension Execution Controller [Documentation](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles")',
    # mobile-notifications (mojibake U+00C2 U+00AE preserved in EN key — L93 source-verbatim)
    "Enables mobile push notifications for DavisÂ® problems. On Dynatrace Managed environments, additionally enables mobile QR code generation.": "Включает мобильные push-уведомления для проблем DavisÂ®. В окружениях Dynatrace Managed дополнительно включает генерацию мобильного QR-кода.",
    "When set to true, the error budget left will be shown in percent of the total error budget. For more details see [SLO normalization help](https://dt-url.net/slo-normalize-error-budget).": "Если установлено в true, оставшийся бюджет ошибок будет показан в процентах от общего бюджета ошибок. Подробнее см. [SLO normalization help](https://dt-url.net/slo-normalize-error-budget).",
    "Once this limit is reached, Dynatrace [throttles the number of captured user sessions](https://dt-url.net/fm3v0p7g).": "При достижении этого лимита Dynatrace [ограничивает число захваченных пользовательских сессий](https://dt-url.net/fm3v0p7g).",
    "Disable the feature to stop receiving information about crash details and potential problems. We recommend keeping the feature enabled.": "Отключите функцию, чтобы перестать получать информацию о деталях сбоев и потенциальных проблемах. Мы рекомендуем оставлять функцию включённой.",
    "If enabled, the new endpoint detection rules will be active.": "Если включено, будут активны новые правила определения эндпоинтов.",
    "Unit name has to be unique and is used as identifier.  E.g: Byte, Second, BytePerMinute": "Имя единицы должно быть уникальным и используется как идентификатор.  Например: Byte, Second, BytePerMinute",
    "Unit plural name represent the plural form of the unit name.  E.g: Bytes, Seconds": "Имя во множественном числе представляет форму множественного числа имени единицы.  Например: Bytes, Seconds",
    "Unit symbol has to be unique.  E.g: s, m/s, B/min, bit/s": "Символ единицы должен быть уникальным.  Например: s, m/s, B/min, bit/s",
    "Unit description should provide additional information about the new unit  E.g: Byte: 8 bits of information": "Описание единицы должно содержать дополнительную информацию о новой единице.  Например: Byte: 8 bits of information",
    "Should metrics be written for endpoints? Please be aware that this setting has billing implications and does not affect metrics on Grail. Check out this [documentation](https://dt-url.net/td23cgh) for further details.": "Записывать ли метрики для эндпоинтов? Обратите внимание, что эта настройка имеет последствия для биллинга и не влияет на метрики в Grail. Подробнее см. эту [documentation](https://dt-url.net/td23cgh).",
    "How often the monitor is executed. Supported values are 1, 2, 5, 10, 15, 30 and 60 minutes": "Как часто выполняется монитор. Поддерживаемые значения: 1, 2, 5, 10, 15, 30 и 60 минут",
    "Note: ActiveGate tokens notifications are sent only when you deployed ActiveGate tokens with expiration dates in your environment and notifications are defined (see notification settings (`<your-dynatrace-url>//ui/settings/builtin:problem.notifications`))": "Примечание: уведомления о токенах ActiveGate отправляются только если в окружении развёрнуты токены ActiveGate с датами истечения и определены уведомления (см. настройки уведомлений (`<your-dynatrace-url>//ui/settings/builtin:problem.notifications`))",
}

# Structural canon (shared with L4-AG.1a.1 / L4-AF).
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
    """`### <Name> (`builtin:...`)` -> `### <RU name> (`builtin:...`)`."""
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
    """`| <Label> \`code\` | <type> | <Desc> | <Req> |`."""
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
        # No label translation: keep row untouched. Safe (label is EN).
        return None
    new_label = PARAM_LABEL[label]
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + len(ENUM_PHRASE[0]) :]
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


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    for en, ru in SCHEMA_DESC.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    # Translate ENUM_PHRASE globally so rows with empty labels (e.g. just `code`)
    # also get «Возможные значения:» substitution — fix for attributes-preferences.
    t = t.replace(ENUM_PHRASE[0], ENUM_PHRASE[1])
    out = []
    for line in t.split("\n"):
        nl = _heading(line) or _param_row(line)
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
        print("%-60s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print()
    print("PARITY:", "OK" if bad == 0 else f"BAD ({bad})")
