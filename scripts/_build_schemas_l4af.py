# -*- coding: utf-8 -*-
"""L4-AF builder: environment-api/settings/schemas.md (parent subsection index,
one big 377-line table) + the 29 schemas/app-dynatrace-*.md schema-table files.
Out of scope: 307 builtin-* files, schemas/get-all.md, schemas/get-schema.md.

ACTIVE Settings 2.0 API (no deprecated banner). title/source/scraped + BOTH
`# Settings API - X schema table` H1 + `* Published <date>` lines EN-verbatim
(L4-AE). Schema-metadata header `| Schema ID | Schema groups | Scope |` + sep +
single value row EN-verbatim (schema/scope EN-locked domain vocab). GET endpoint
rows EN-verbatim. URLs verbatim. `Required`/`Optional` Parameters-table CELL
value EN-verbatim (column header translated). `[Tokens and authentication]`
link-text EN-verbatim.

Splice method (L98/L100/L4X): start from EN, CRLF->LF, strip BOM (the literal
3-char sequence U+00EF U+00BB U+00BF appears INSIDE link-text in 4 files:
gitlab/kubernetes/SRG/slack), apply ordered exact-string canon. Line-parity
EXACT: only translate text WITHIN a line, never add/remove/merge/split. No
fenced code blocks anywhere in these 30 files. No mojibake (no e2-80 family).
No em-dash in source; none introduced (CLAUDE#0).

CONSISTENCY GUARANTEE (highest-risk area per brief): DISPLAY_NAME is ONE dict
EN->RU reused by BOTH the parent schemas.md table-row builder AND the per-file
`### <Name> (\`app:...)\`` heading builder. A name can only resolve one way.

anchor = shipped L4-AE settings.md / settings/key-concepts.md /
settings/objects/get-object.md (read first): `## Аутентификация`, auth
paragraph, `## Параметры`, `##### Объект \`X\``, `Возможные значения:` canon.
"""

import os, io, glob

EN = "docs/managed/dynatrace-api/environment-api/settings"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings"

PARENT = "schemas.md"
APP_GLOB = "schemas/app-dynatrace-*.md"

# ----------------------------------------------------------------------------
# (1) DISPLAY-NAME R-map: EN -> RU. SINGLE source of truth, used by BOTH the
#     parent table builder and every per-file `### <Name> (\`app:...)\`` heading.
#     Only the 29 app-dynatrace schemas + every builtin row that appears in the
#     parent table. NAME RULE: pure product noun = EN; product+generic = product
#     EN + noun RU; descriptive DT phrase = natural RU keeping EN-locked terms;
#     established DT proper-noun feature = EN.
# ----------------------------------------------------------------------------
DISPLAY_NAME = {
    # ---- 29 app-dynatrace schemas (parent rows 16-45 + per-file ### heading) ----
    "AbuseIPDB Connections": "Подключения AbuseIPDB",
    "Amazon ECR": "Amazon ECR",
    "Amazon GuardDuty": "Amazon GuardDuty",
    "Microsoft Entra ID": "Microsoft Entra ID",
    "Cost & Carbon Optimization": "Cost & Carbon Optimization",
    "Business flow": "Business flow",
    "Salesforce Insights": "Salesforce Insights",
    "Compliance Assistant": "Compliance Assistant",
    "Extensions Creator": "Extensions Creator",
    "Git On-Premise Servers": "Git-серверы On-Premise",
    "Discovery findings default rules schema": "Schema правил по умолчанию для находок Discovery",
    "GitHub Connections": "Подключения GitHub",
    "GitLab Connections": "Подключения GitLab",
    "Hub Requests": "Запросы Hub",
    "Infrastructure & Operations app settings": "Настройки приложения Infrastructure & Operations",
    "Jenkins Connections": "Подключения Jenkins",
    "Jira Connections": "Подключения Jira",
    "Kubernetes Connector": "Коннектор Kubernetes",
    "Launcher": "Launcher",
    "Microsoft Defender for Cloud": "Microsoft Defender for Cloud",
    "Microsoft Sentinel": "Microsoft Sentinel",
    "Microsoft 365 Email Connections": "Подключения электронной почты Microsoft 365",
    "Microsoft Teams": "Microsoft Teams",
    "PagerDuty Connections": "Подключения PagerDuty",
    "Red Hat Ansible Automation Controller Connections": "Подключения Red Hat Ansible Automation Controller",
    "Red Hat Event-Driven Ansible Connections": "Подключения Red Hat Event-Driven Ansible",
    "ServiceNow Connections": "Подключения ServiceNow",
    "Site Reliability Guardian": "Site Reliability Guardian",
    "Slack": "Slack",
    "VirusTotal Connections": "Подключения VirusTotal",
    # ---- builtin rows (parent table only; per NAME RULE) ----
    "Network security": "Сетевая безопасность",
    "Connectivity alerts": "Оповещения о связности",
    "Maintenance windows": "Окна обслуживания",
    "Problem alerting profiles": "Профили оповещений о проблемах",
    "Anomaly detection for databases": "Обнаружение аномалий для баз данных",
    "Disk anomaly detection rules": "Правила обнаружения аномалий дисков",
    "Frequent issue detection": "Обнаружение частых проблем",
    "Holiday-aware baseline modification": "Изменение базовой линии с учётом праздников",
    "Anomaly detection for classic AWS services": "Обнаружение аномалий для классических сервисов AWS",
    "Anomaly detection for infrastructure: Disk": "Обнаружение аномалий для инфраструктуры: диск",
    "Anomaly detection for infrastructure": "Обнаружение аномалий для инфраструктуры",
    "Anomaly detection for infrastructure: Host": "Обнаружение аномалий для инфраструктуры: хост",
    "Anomaly detection for VMware": "Обнаружение аномалий для VMware",
    "Kubernetes cluster anomaly detection": "Обнаружение аномалий кластера Kubernetes",
    "Kubernetes namespace anomaly detection": "Обнаружение аномалий namespace Kubernetes",
    "Kubernetes node anomaly detection": "Обнаружение аномалий узла Kubernetes",
    "Kubernetes persistent volume claim anomaly detection": "Обнаружение аномалий persistent volume claim Kubernetes",
    "Kubernetes workload anomaly detection": "Обнаружение аномалий workload Kubernetes",
    "Metric events": "Метрические события",
    "Anomaly detection for custom applications": "Обнаружение аномалий для пользовательских приложений",
    "Crash rate increase settings for custom applications": "Настройки роста частоты сбоев для пользовательских приложений",
    "Anomaly detection for mobile applications": "Обнаружение аномалий для мобильных приложений",
    "Crash rate increase settings for mobile applications": "Настройки роста частоты сбоев для мобильных приложений",
    "Anomaly detection for applications": "Обнаружение аномалий для приложений",
    "Anomaly detection for services": "Обнаружение аномалий для сервисов",
    "Ready-made alerts category update": "Обновление категории готовых оповещений",
    "API detection rules": "Правила обнаружения API",
    "Cloud Development Environments": "Облачные среды разработки",
    "Kubernetes app": "Приложение Kubernetes",
    "Vulnerability Analytics: Monitoring rules for code-level vulnerabilities": "Vulnerability Analytics: правила мониторинга уязвимостей уровня кода",
    "Vulnerability alerting profiles": "Профили оповещений об уязвимостях",
    "Attack alerting profiles": "Профили оповещений об атаках",
    "Security notifications": "Уведомления безопасности",
    "Vulnerability Analytics: Monitoring rules for third-party vulnerabilities": "Vulnerability Analytics: правила мониторинга сторонних уязвимостей",
    "Vulnerability Analytics: General settings": "Vulnerability Analytics: общие настройки",
    "Vulnerability Analytics: Kubernetes monitoring rules for third-party vulnerabilities": "Vulnerability Analytics: правила мониторинга Kubernetes для сторонних уязвимостей",
    "Allowed attributes": "Разрешённые атрибуты",
    "Blocked attributes": "Заблокированные атрибуты",
    "Attribute data masking": "Маскирование данных атрибутов",
    "Preferences": "Предпочтения",
    "Log audit events": "События аудита логов",
    "Automation workflow approval": "Подтверждение workflow автоматизации",
    "Process group availability monitoring": "Мониторинг доступности групп процессов",
    "Business event bucket assignment": "Назначение бакета для бизнес-событий",
    "Business event metric extraction": "Извлечение метрик из бизнес-событий",
    "Business event processing": "Обработка бизнес-событий",
    "Business event security context": "Контекст безопасности бизнес-событий",
    "OneAgent Business events capturing variants": "Варианты захвата бизнес-событий OneAgent",
    "Capture business events with OneAgent": "Захват бизнес-событий с помощью OneAgent",
    "Cloud Foundry": "Cloud Foundry",
    "Connection settings": "Настройки подключения",
    "Monitoring settings": "Настройки мониторинга",
    "Built-in container monitoring rules": "Встроенные правила мониторинга контейнеров",
    "Container monitoring rules": "Правила мониторинга контейнеров",
    "Container monitoring": "Мониторинг контейнеров",
    "Crash dump analytics": "Аналитика аварийных дампов",
    "User session custom metrics": "Пользовательские метрики пользовательских сессий",
    "Custom units": "Пользовательские единицы",
    "General settings": "Общие настройки",
    "Allowed URL pattern rules": "Правила разрешённых шаблонов URL",
    "Preset settings": "Настройки пресетов",
    "Anomaly detectors": "Детекторы аномалий",
    "Declarative process grouping": "Декларативная группировка процессов",
    "ActiveGate updates": "Обновления ActiveGate",
    "Update windows for OneAgent updates": "Окна обновления для обновлений OneAgent",
    "OneAgent default mode": "Режим OneAgent по умолчанию",
    "OneAgent updates": "Обновления OneAgent",
    "Enable Observability For Developers": "Включить Observability for Developers",
    "Sensitive Data Masking": "Маскирование чувствительных данных",
    "Disk Analytics Extension": "Расширение Disk Analytics",
    "Disk options": "Параметры дисков",
    "Limit outbound connections": "Ограничение исходящих подключений",
    "App Monitoring": "Мониторинг приложений",
    "eBPF Service Discovery": "Обнаружение сервисов eBPF",
    "Extension Execution Controller": "Extension Execution Controller",
    "User session exports": "Экспорты пользовательских сессий",
    "Endpoint detection": "Обнаружение эндпоинтов",
    "Enable endpoint detection": "Включить обнаружение эндпоинтов",
    "Enhanced endpoints for SDv1": "Расширенные эндпоинты для SDv1",
    "Terms of use": "Условия использования",
    "Exclude network traffic": "Исключить сетевой трафик",
    "Failure detection": "Обнаружение сбоев",
    "Failure detection parameters": "Параметры обнаружения сбоев",
    "Failure detection rules": "Правила обнаружения сбоев",
    "General failure detection parameters": "Общие параметры обнаружения сбоев",
    "HTTP failure detection parameters": "Параметры обнаружения сбоев HTTP",
    "Geolocation settings": "Настройки геолокации",
    "Global trace ingest rate control": "Глобальное управление скоростью приёма трейсов",
    "Cloud health alerts settings": "Настройки оповещений о состоянии облака",
    "Frontend health alerts": "Оповещения о состоянии фронтенда",
    "Histogram metrics": "Гистограммные метрики",
    "Monitoring": "Мониторинг",
    "Advanced Settings": "Расширенные настройки",
    "AIX kernel extension": "Расширение ядра AIX",
    "Monitoring Mode": "Режим мониторинга",
    "Process group monitoring": "Мониторинг групп процессов",
    "Hub subscriptions": "Подписки Hub",
    "AWS Connections": "Подключения AWS",
    "Connections to AWS environments": "Подключения к средам AWS",
    "Connections to Azure environments": "Подключения к средам Azure",
    "Connections to GCP environments": "Подключения к средам GCP",
    "GCP Dynatrace Principal": "GCP Dynatrace Principal",
    "IBM MQ IMS bridges": "Мосты IBM MQ IMS",
    "IBM MQ queue managers": "Менеджеры очередей IBM MQ",
    "IBM MQ queue sharing groups": "Группы совместного использования очередей IBM MQ",
    "Anomaly detection for infrastructure: Disk Edge": "Обнаружение аномалий для инфраструктуры: Disk Edge",
    "Issue-tracking for releases": "Отслеживание задач для релизов",
    "Kubernetes Telemetry Enrichment": "Обогащение телеметрии Kubernetes",
    "Security Posture Management: Kubernetes": "Security Posture Management: Kubernetes",
    "Custom log sources": "Пользовательские источники логов",
    "Advanced log settings": "Расширенные настройки логов",
    "Log module feature flags": "Feature-флаги модуля логов",
    "Log buckets": "Бакеты логов",
    "Log custom attributes": "Пользовательские атрибуты логов",
    "Processing": "Обработка",
    "Log events": "События логов",
    "Log Security Context": "Контекст безопасности логов",
    "Log module self monitoring settings": "Настройки самомониторинга модуля логов",
    "Log ingest rules": "Правила приёма логов",
    "Log metrics": "Метрики логов",
    "Sensitive data masking": "Маскирование чувствительных данных",
    "Timestamp/Splitting patterns": "Шаблоны меток времени/разбиения",
    "IBM MQ filters": "Фильтры IBM MQ",
    "Transaction monitoring": "Мониторинг транзакций",
    "Transaction start filters": "Фильтры начала транзакций",
    "Management zones settings": "Настройки management zones",
    "Metric metadata": "Метаданные метрик",
    "Metric query": "Запрос метрик",
    "Dynatrace mobile app": "Мобильное приложение Dynatrace",
    "Apache HTTP Server": "Apache HTTP Server",
    ".NET": ".NET",
    "Go": "Go",
    "IIS": "IIS",
    "Java": "Java",
    "Nginx": "Nginx",
    "Node.js": "Node.js",
    "Envoy": "Envoy",
    "PHP": "PHP",
    "Python": "Python",
    "Varnish Cache": "Varnish Cache",
    # faithful mirror of source quirk: literal `|` inside link text (L93)
    "IBM Integration Bus | IBM App Connect Enterprise": "IBM Integration Bus | IBM App Connect Enterprise",
    "Generic relationships": "Универсальные связи",
    "Generic types": "Универсальные типы",
    "Grail security context for monitored entities": "Контекст безопасности Grail для отслеживаемых сущностей",
    "Service-level objective definitions": "Определения service-level objective",
    "Service-level objective setup": "Настройка service-level objective",
    "NetTracer traffic": "Трафик NetTracer",
    "Network zones settings": "Настройки network zones",
    "Network zone": "Network zone",
    "OneAgent features": "Возможности OneAgent",
    "OneAgent side masking": "Маскирование на стороне OneAgent",
    "Data forwarding configuration (bizevents)": "Конфигурация пересылки данных (bizevents)",
    "Ingest sources configuration (bizevents)": "Конфигурация источников приёма (bizevents)",
    "Pipeline Groups configuration (bizevents)": "Конфигурация Pipeline Groups (bizevents)",
    "Ingest pipelines configuration (bizevents)": "Конфигурация конвейеров приёма (bizevents)",
    "Ingest routing configuration (bizevents)": "Конфигурация маршрутизации приёма (bizevents)",
    "Data forwarding configuration (davis.events)": "Конфигурация пересылки данных (davis.events)",
    "Ingest sources configuration (davis.events)": "Конфигурация источников приёма (davis.events)",
    "Pipeline Groups configuration (davis.events)": "Конфигурация Pipeline Groups (davis.events)",
    "Ingest pipelines configuration (davis.events)": "Конфигурация конвейеров приёма (davis.events)",
    "Ingest routing configuration (davis.events)": "Конфигурация маршрутизации приёма (davis.events)",
    "Data forwarding configuration (davis.problems)": "Конфигурация пересылки данных (davis.problems)",
    "Ingest sources configuration (davis.problems)": "Конфигурация источников приёма (davis.problems)",
    "Pipeline Groups configuration (davis.problems)": "Конфигурация Pipeline Groups (davis.problems)",
    "Ingest pipelines configuration (davis.problems)": "Конфигурация конвейеров приёма (davis.problems)",
    "Ingest routing configuration (davis.problems)": "Конфигурация маршрутизации приёма (davis.problems)",
    "Data forwarding configuration (events)": "Конфигурация пересылки данных (events)",
    "Ingest sources configuration (events)": "Конфигурация источников приёма (events)",
    "Pipeline Groups configuration (events)": "Конфигурация Pipeline Groups (events)",
    "Ingest pipelines configuration (events)": "Конфигурация конвейеров приёма (events)",
    "Ingest routing configuration (events)": "Конфигурация маршрутизации приёма (events)",
    "Data forwarding configuration (events.sdlc)": "Конфигурация пересылки данных (events.sdlc)",
    "Ingest sources configuration (events.sdlc)": "Конфигурация источников приёма (events.sdlc)",
    "Pipeline Groups configuration (events.sdlc)": "Конфигурация Pipeline Groups (events.sdlc)",
    "Ingest pipelines configuration (events.sdlc)": "Конфигурация конвейеров приёма (events.sdlc)",
    "Ingest routing configuration (events.sdlc)": "Конфигурация маршрутизации приёма (events.sdlc)",
    "Data forwarding configuration (events.security)": "Конфигурация пересылки данных (events.security)",
    "Ingest sources configuration (events.security)": "Конфигурация источников приёма (events.security)",
    "Pipeline Groups configuration (events.security)": "Конфигурация Pipeline Groups (events.security)",
    "Ingest pipelines configuration (events.security)": "Конфигурация конвейеров приёма (events.security)",
    "Ingest routing configuration (events.security)": "Конфигурация маршрутизации приёма (events.security)",
    "Data forwarding configuration (logs)": "Конфигурация пересылки данных (logs)",
    "Ingest sources configuration (logs)": "Конфигурация источников приёма (logs)",
    "Pipeline Groups configuration (logs)": "Конфигурация Pipeline Groups (logs)",
    "Ingest pipelines configuration (logs)": "Конфигурация конвейеров приёма (logs)",
    "Ingest routing configuration (logs)": "Конфигурация маршрутизации приёма (logs)",
    "Data forwarding configuration (metrics)": "Конфигурация пересылки данных (metrics)",
    "Ingest sources configuration (metrics)": "Конфигурация источников приёма (metrics)",
    "Pipeline Groups configuration (metrics)": "Конфигурация Pipeline Groups (metrics)",
    "Ingest pipelines configuration (metrics)": "Конфигурация конвейеров приёма (metrics)",
    "Ingest routing configuration (metrics)": "Конфигурация маршрутизации приёма (metrics)",
    "Data forwarding configuration (security.events)": "Конфигурация пересылки данных (security.events)",
    "Ingest sources configuration (security.events)": "Конфигурация источников приёма (security.events)",
    "Pipeline Groups configuration (security.events)": "Конфигурация Pipeline Groups (security.events)",
    "Ingest pipelines configuration (security.events)": "Конфигурация конвейеров приёма (security.events)",
    "Ingest routing configuration (security.events)": "Конфигурация маршрутизации приёма (security.events)",
    "Data forwarding configuration (spans)": "Конфигурация пересылки данных (spans)",
    "Ingest sources configuration (spans)": "Конфигурация источников приёма (spans)",
    "Pipeline Groups configuration (spans)": "Конфигурация Pipeline Groups (spans)",
    "Ingest pipelines configuration (spans)": "Конфигурация конвейеров приёма (spans)",
    "Ingest routing configuration (spans)": "Конфигурация маршрутизации приёма (spans)",
    "Data forwarding configuration (system.events)": "Конфигурация пересылки данных (system.events)",
    "Ingest sources configuration (system.events)": "Конфигурация источников приёма (system.events)",
    "Pipeline Groups configuration (system.events)": "Конфигурация Pipeline Groups (system.events)",
    "Ingest pipelines configuration (system.events)": "Конфигурация конвейеров приёма (system.events)",
    "Ingest routing configuration (system.events)": "Конфигурация маршрутизации приёма (system.events)",
    "Data forwarding configuration (user.events)": "Конфигурация пересылки данных (user.events)",
    "Ingest sources configuration (user.events)": "Конфигурация источников приёма (user.events)",
    "Pipeline Groups configuration (user.events)": "Конфигурация Pipeline Groups (user.events)",
    "Ingest pipelines configuration (user.events)": "Конфигурация конвейеров приёма (user.events)",
    "Ingest routing configuration (user.events)": "Конфигурация маршрутизации приёма (user.events)",
    "Data forwarding configuration (usersessions)": "Конфигурация пересылки данных (usersessions)",
    "Ingest sources configuration (usersessions)": "Конфигурация источников приёма (usersessions)",
    "Pipeline Groups configuration (usersessions)": "Конфигурация Pipeline Groups (usersessions)",
    "Ingest pipelines configuration (usersessions)": "Конфигурация конвейеров приёма (usersessions)",
    "Ingest routing configuration (usersessions)": "Конфигурация маршрутизации приёма (usersessions)",
    "OpenTelemetry metrics": "Метрики OpenTelemetry",
    "OS services monitoring": "Мониторинг сервисов ОС",
    "Configure ownership": "Настройка владения",
    "Ownership teams": "Команды владения",
    "Anonymize End-User IP Addresses": "Анонимизация IP-адресов конечных пользователей",
    "End users' data privacy": "Конфиденциальность данных конечных пользователей",
    "Problem fields": "Поля проблем",
    "Problem notifications": "Уведомления о проблемах",
    "Advanced detection rules": "Расширенные правила обнаружения",
    "Cloud application and workload detection": "Обнаружение облачных приложений и workload",
    "Built-in detection rules": "Встроенные правила обнаружения",
    "Simple detection rules": "Простые правила обнаружения",
    "Process grouping rules": "Правила группировки процессов",
    "Process instance snapshots": "Снимки экземпляров процессов",
    "Built-in process monitoring rules": "Встроенные правила мониторинга процессов",
    "Custom process monitoring rules": "Пользовательские правила мониторинга процессов",
    "Process availability": "Доступность процессов",
    "Remote environments": "Удалённые среды",
    "Resource attributes": "Атрибуты ресурсов",
    "Trace sampling for RPC requests": "Сэмплирование трейсов для RPC-запросов",
    "Enablement and cost control": "Включение и контроль затрат",
    "Application name and type": "Имя и тип приложения",
    "Frontend name": "Имя фронтенда",
    "Identify host names": "Определение имён хостов",
    "IP determination": "Определение IP",
    "Map IP addresses to locations": "Сопоставление IP-адресов с местоположениями",
    "Beacon endpoint settings": "Настройки beacon-эндпоинта",
    "Apdex configuration": "Конфигурация Apdex",
    "Application name": "Имя приложения",
    "Privacy settings": "Настройки конфиденциальности",
    "Request errors": "Ошибки запросов",
    "RUM overload prevention": "Предотвращение перегрузки RUM",
    "Real User Monitoring for process group": "Real User Monitoring для группы процессов",
    "Provider breakdown": "Разбивка по провайдерам",
    "Advanced correlation": "Расширенная корреляция",
    "User experience score": "Оценка пользовательского опыта",
    "Application detection": "Обнаружение приложений",
    "Automatic injection": "Автоматическая инъекция",
    "Beacon origins for CORS": "Beacon-источники для CORS",
    "Exclude/Include browsers from monitoring": "Исключение/включение браузеров из мониторинга",
    "Custom Properties Capture Restrictions": "Ограничения захвата пользовательских свойств",
    "Custom configuration properties": "Пользовательские свойства конфигурации",
    "Custom errors": "Пользовательские ошибки",
    "Define custom injection rules": "Определение пользовательских правил инъекции",
    "Custom RUM JavaScript version": "Пользовательская версия RUM JavaScript",
    "Cookie": "Cookie",
    "Exclude IP addresses from monitoring": "Исключение IP-адресов из мониторинга",
    "Apdex configuration for custom actions": "Конфигурация Apdex для пользовательских действий",
    "Apdex configuration for load actions": "Конфигурация Apdex для действий загрузки",
    "Apdex configuration for XHR actions": "Конфигурация Apdex для XHR-действий",
    "Manual insertion": "Ручная вставка",
    "Resource URL cleanup rules": "Правила очистки URL ресурсов",
    "Resource types": "Типы ресурсов",
    "RUM monitoring code filename": "Имя файла кода мониторинга RUM",
    "RUM JavaScript updates": "Обновления RUM JavaScript",
    "Exclude XHR requests from monitoring": "Исключение XHR-запросов из мониторинга",
    "Security context settings": "Настройки контекста безопасности",
    "Security enrichment connections": "Подключения обогащения безопасности",
    "Service detection": "Обнаружение сервисов",
    "Service Detection v2 for OneAgent": "Service Detection v2 для OneAgent",
    "Service detection rules for External Web Requests": "Правила обнаружения сервисов для External Web Requests",
    "Service detection rules for External Web Services": "Правила обнаружения сервисов для External Web Services",
    "Service detection rules for Full Web Requests": "Правила обнаружения сервисов для Full Web Requests",
    "Service detection rules for Full Web Services": "Правила обнаружения сервисов для Full Web Services",
    "Service splitting": "Разделение сервисов",
    "Session Replay state cookie": "Cookie состояния Session Replay",
    "Session replay data privacy": "Конфиденциальность данных Session Replay",
    "Resource capture for Session Replay": "Захват ресурсов для Session Replay",
    "Muted requests": "Отключённые запросы",
    "Key requests": "Ключевые запросы",
    "Span attributes": "Атрибуты span",
    "Span capturing": "Захват span",
    "Span context propagation": "Распространение контекста span",
    "Span entry points": "Точки входа span",
    "Span events": "События span",
    "Security Posture Management": "Security Posture Management",
    "Assign synthetic monitor to web applications": "Назначение synthetic-монитора веб-приложениям",
    "Browser monitor enablement": "Включение браузерного монитора",
    "Key performance metrics": "Ключевые метрики производительности",
    "Monitor name": "Имя монитора",
    "Outage handling": "Обработка простоев",
    "Performance thresholds": "Пороги производительности",
    "Frequency and locations": "Частота и местоположения",
    "Advanced settings": "Расширенные настройки",
    "Assign synthetic monitor to applications": "Назначение synthetic-монитора приложениям",
    "Cookies": "Cookies",
    "Network Availability monitor config": "Конфигурация монитора доступности сети",
    "Synthetic monitor's primary grail tags": "Основные grail-теги synthetic-монитора",
    "Synthetic availability": "Доступность synthetic",
    "Automatically applied tags": "Автоматически применяемые теги",
    "Access tokens": "Access-токены",
    "Trace ingest control": "Управление приёмом трейсов",
    "Endpoint metrics": "Метрики эндпоинтов",
    "Trace sampling for HTTP requests": "Сэмплирование трейсов для HTTP-запросов",
    "URL path pattern matching": "Сопоставление шаблонов пути URL",
    "Usability analytics": "Аналитика юзабилити",
    "User action custom metrics": "Пользовательские метрики действий пользователя",
    "VMware": "VMware",
}

# ----------------------------------------------------------------------------
# (2) Per-file DESCRIPTION line(s) (the prose right under the `### X (...)`
#     heading). Exact-string EN -> RU. Product/brand names EN-locked.
# ----------------------------------------------------------------------------
DESCRIPTIONS = {
    "AbuseIPDB Connections": "Подключения AbuseIPDB",
    "Ingest Amazon Elastic Container Registry vulnerability findings and scan events.": "Приём данных об уязвимостях и событий сканирования из Amazon Elastic Container Registry.",
    "Ingest Amazon GuardDuty security findings.": "Приём данных о безопасности из Amazon GuardDuty.",
    "Authentication settings for Microsoft Entra ID.": "Настройки аутентификации для Microsoft Entra ID.",
    "Settings for the Cost & Carbon Optimization AppEngine application.": "Настройки для AppEngine-приложения Cost & Carbon Optimization.",
    "Settings for the Business flow AppEngine application.": "Настройки для AppEngine-приложения Business flow.",
    "Settings for the Salesforce Insights AppEngine application": "Настройки для AppEngine-приложения Salesforce Insights",
    "Settings for Compliance Assistant application": "Настройки для приложения Compliance Assistant",
    # Extensions Creator: no description line in source
    "Specify your On-Premise Git servers to be able to fetch source code from them": "Укажите ваши Git-серверы On-Premise, чтобы можно было получать из них исходный код",
    "Discovery findings default rules. This schema is not subject to manual changes, except for Muted setting. Any changes (except muting the rule) will be overwritten by the Discovery & Coverage application defaults.": "Правила по умолчанию для находок Discovery. Эта schema не подлежит ручным изменениям, кроме настройки Muted. Любые изменения (кроме отключения правила) будут перезаписаны значениями по умолчанию приложения Discovery & Coverage.",
    "GitHub authentication details": "Данные аутентификации GitHub",
    "Connections containing access tokens for the GitLab Platform": "Подключения, содержащие access-токены для платформы GitLab",
    "Please add at least one admin with all necessary permissions to fulfill the requests.": "Добавьте хотя бы одного администратора со всеми необходимыми правами для выполнения запросов.",
    "You can either enter team or individual email addresses to receive request notifications.": "Для получения уведомлений о запросах можно указать командные или индивидуальные адреса электронной почты.",
    "Use these settings to customize the I&O App experience. Please note: You must reload the app for any changes to take effect.": "Используйте эти настройки для кастомизации работы приложения I&O. Обратите внимание: чтобы изменения вступили в силу, нужно перезагрузить приложение.",
    "Connections contain the access information for the Jenkins app. This connection can be used to connect to the Jenkins instance.": "Подключения содержат информацию доступа для приложения Jenkins. Это подключение можно использовать для подключения к инстансу Jenkins.",
    "Credentials for the Jira App": "Учётные данные для приложения Jira",
    # Kubernetes Connector description has inline BOM links -> handled below
    "Set up your teams home launchpads to streamline your workflow and enhance productivity. Configure up to 100 custom home launchpads in this environment to suit your specific needs.": "Настройте домашние launchpad-ы ваших команд, чтобы упорядочить рабочий процесс и повысить продуктивность. Настройте до 100 пользовательских домашних launchpad-ов в этом окружении под ваши конкретные нужды.",
    "Ingest Microsoft Defender for Cloud vulnerability findings and scan events.": "Приём данных об уязвимостях и событий сканирования из Microsoft Defender for Cloud.",
    "Microsoft 365 connections for sending emails": "Подключения Microsoft 365 для отправки электронной почты",
    "Authentication details for the Microsoft Teams App": "Данные аутентификации для приложения Microsoft Teams",
    "Credentials for the PagerDuty App": "Учётные данные для приложения PagerDuty",
    "Connections containing access tokens for the Red Hat Ansible app. This connection can be used for connecting to Red Hat Ansible Automation Controller as well as the open-source project AWX.": "Подключения, содержащие access-токены для приложения Red Hat Ansible. Это подключение можно использовать для подключения к Red Hat Ansible Automation Controller, а также к проекту с открытым исходным кодом AWX.",
    "Connections containing access tokens for the Red Hat Ansible app. This connection can be used for connecting to the DT Event-Driven plugin within Red Hat Event-Driven Ansible.": "Подключения, содержащие access-токены для приложения Red Hat Ansible. Это подключение можно использовать для подключения к плагину DT Event-Driven в составе Red Hat Event-Driven Ansible.",
    "Connections allow you to integrate into ServiceNow.": "Подключения позволяют интегрироваться с ServiceNow.",
    # Site Reliability Guardian description has inline BOM link -> handled below
    "Authentication details for Slack API": "Данные аутентификации для Slack API",
    "VirusTotal Connections": "Подключения VirusTotal",
}

# Warning / multi-sentence note paragraphs (full-line exact).
NOTES = {
    "Warning! If the following configurations are modified here, in the Settings 2.0 environment, it is likely that the Business Flow application will lose access to them or will have unexpected behaviour. It is strongly advised not to make any changes and to save them here. If you want to make changes, access Business Flow app.": "Внимание! Если перечисленные ниже конфигурации изменить здесь, в окружении Settings 2.0, приложение Business Flow, скорее всего, потеряет к ним доступ или будет вести себя непредсказуемо. Настоятельно рекомендуется не вносить здесь никаких изменений и не сохранять их. Если нужно внести изменения, откройте приложение Business Flow.",
}

# Inline-link description lines containing the literal 3-char BOM (handled
# AFTER BOM strip, so keys are written WITHOUT the BOM). Whole-line exact.
LINK_LINES = {
    '(for more information read the [GitLab API documentation](https://docs.gitlab.com/ee/api/rest/ "Visit GitLab document"))': '(подробнее в [документации по GitLab API](https://docs.gitlab.com/ee/api/rest/ "Открыть документ GitLab"))',
    '(for more information read the [Slack api documentation](https://api.slack.com/authentication/basics/ "Visit Slack document"))': '(подробнее в [документации по Slack API](https://api.slack.com/authentication/basics/ "Открыть документ Slack"))',
    "Available connections for [Kubernetes Connector](https://dt-url.net/qx03q4d). A connection is bound to a Kubernetes cluster where the workflow actions operate. We recommend following the steps described [here](https://dt-url.net/mf03qvf) using the Dynatrace Operator, which automatically creates the connection.": "Доступные подключения для [Kubernetes Connector](https://dt-url.net/qx03q4d). Подключение привязано к кластеру Kubernetes, в котором выполняются действия workflow. Рекомендуем выполнить шаги, описанные [здесь](https://dt-url.net/mf03qvf), с помощью Dynatrace Operator, который автоматически создаёт подключение.",
    "Create new guardians and add objectives. [See documentation](https://dt-url.net/site-reliability-guardian)": "Создание новых guardians и добавление objectives. [См. документацию](https://dt-url.net/site-reliability-guardian)",
}

# ----------------------------------------------------------------------------
# (3) Parameters-table cell maps. LABEL = human text before the `\`code\``.
#     DESC = the Description cell content. Both translated; code/type/Required
#     EN-verbatim. Enum phrase handled separately (mid-cell).
# ----------------------------------------------------------------------------
PARAM_LABEL = {
    "Activate connection": "Активировать подключение",
    "Connection name": "Имя подключения",
    "API key": "Ключ API",
    "Amazon ECR scan type": "Тип сканирования Amazon ECR",
    "Ingest token ID": "ID токена приёма",
    "Description": "Описание",
    "Directory (tenant) ID": "ID каталога (тенанта)",
    "Application (client) ID": "ID приложения (клиента)",
    "Client secret": "Секрет клиента",
    "Workflow ID": "ID workflow",
    "GCP API key": "Ключ API GCP",
    "Should collect costs": "Собирать ли затраты",
    "Idling optimization": "Оптимизация простоя",
    "Sizing optimization": "Оптимизация размеров",
    "Data center overrides": "Переопределения дата-центра",
    "Business health performance indicator": "Индикатор эффективности бизнес-здоровья",
    "Network Receiving": "Получение по сети",
    "Network Transmitting": "Передача по сети",
    "Cpu": "Cpu",
    "Memory": "Память",
    "Data Center Id": "ID дата-центра",
    "Id": "Id",
    "Carbon Intensity": "Углеродоёмкость",
    "PUE last update": "Последнее обновление PUE",
    "Carbon Intensity last update": "Последнее обновление углеродоёмкости",
    "Event": "Событие",
    "Value": "Значение",
    "Unit": "Единица",
    "CPU threshold [%]": "Порог CPU [%]",
    "Select event": "Выбрать событие",
    "Select KPI": "Выбрать KPI",
    "KPI unit": "Единица KPI",
    "Provider": "Провайдер",
    "Name": "Имя",
    "Version": "Версия",
    "Configuration ID": "ID конфигурации",
    "Steps": "Шаги",
    "Connections": "Подключения",
    "Correlation ID": "ID корреляции",
    "KPI Label": "Метка KPI",
    "KPI": "KPI",
    "KPI Event": "Событие KPI",
    "KPI Unit": "Единица KPI",
    "Calculation type": "Тип вычисления",
    "Analysis type": "Тип анализа",
    "Analysis custom label": "Пользовательская метка анализа",
    "Analysis Unit": "Единица анализа",
    "Anomaly Detector IDs": "ID детекторов аномалий",
    "Is Smartscape Topology Enabled": "Включена ли топология Smartscape",
    "Smartscape Entity ID": "ID сущности Smartscape",
    "Priority": "Приоритет",
    "Monitoring timeframe in hours": "Период мониторинга в часах",
    "Monitoring frequency in hours": "Частота мониторинга в часах",
    "Is default query limit ignored": "Игнорируется ли лимит запроса по умолчанию",
    "ID": "ID",
    "Is Root": "Является ли корнем",
    "Events": "События",
    "Source": "Источник",
    "Target": "Цель",
    "Errors": "Ошибки",
    "Revenue": "Доход",
    "Average duration": "Средняя длительность",
    "Completed Flows": "Завершённые потоки",
    "Is Error": "Является ли ошибкой",
    "Is Disabled": "Отключено ли",
    "URL": "URL",
    "Event Types": "Типы событий",
    "Grant type": "Тип гранта",
    "Client Id": "ID клиента",
    "Username": "Имя пользователя",
    "Password": "Пароль",
    "Framework Configurations": "Конфигурации фреймворков",
    "DORA": "DORA",
    "Critical or important functions (CIFs)": "Критические или важные функции (CIF)",
    "Cost": "Затраты",
    "Date Modified": "Дата изменения",
    "User Modified": "Кем изменено",
    "Amount": "Сумма",
    "Currency": "Валюта",
    "Type": "Тип",
    "Token": "Токен",
    "Environment URL": "URL окружения",
    "API Token": "Токен API",
    "Git Provider": "Провайдер Git",
    "Server URL": "URL сервера",
    "Include Credentials": "Включить учётные данные",
    "Rule:": "Правило:",
    "Settings:": "Настройки:",
    "Title": "Заголовок",
    "Category": "Категория",
    "Actions": "Действия",
    "Rule query": "Запрос правила",
    "Environment scope": "Scope окружения",
    "Zero rated": "Нулевой тариф",
    "Muted": "Отключено",
    "Parameters": "Параметры",
    "Instant action": "Мгновенное действие",
    "Contact Email": "Контактный email",
    "Show monitoring candidates": "Показывать кандидатов на мониторинг",
    "Show app only hosts": "Показывать только app-хосты",
    "Network interface saturation threshold": "Порог насыщения сетевого интерфейса",
    "Limit the number of entities in main inventories": "Ограничить количество сущностей в основных инвентарях",
    "Limit the number of sortable rows in inventories": "Ограничить количество сортируемых строк в инвентарях",
    "Jenkins URL": "URL Jenkins",
    "Jira URL": "URL Jira",
    "User": "Пользователь",
    "EdgeConnect Name": "Имя EdgeConnect",
    "K8s Cluster UID": "UID кластера K8s",
    "Namespace": "Namespace",
    "Home launchpad": "Домашний launchpad",
    "Launchpad": "Launchpad",
    "User Group": "Группа пользователей",
    "State": "Состояние",
    "Use trused service?": "Использовать доверенный сервис?",
    "GitLab URL": "URL GitLab",
    "GitLab token": "Токен GitLab",
    '"From" email address': '"From" адрес электронной почты',
    "Client Secret": "Секрет клиента",
    "The targeted Microsoft Team": "Целевая команда Microsoft Team",
    "The targeted Channel name": "Имя целевого канала",
    "Webhook URL": "URL вебхука",
    "PagerDuty API URL": "URL API PagerDuty",
    "API token": "Токен API",
    "API URL": "URL API",
    "API access token": "Access-токен API",
    "Use Red Hat Event Streams": "Использовать Red Hat Event Streams",
    "ServiceNow instance URL": "URL инстанса ServiceNow",
    "Client ID": "ID клиента",
    "Tags": "Теги",
    "DQL variables": "Переменные DQL",
    "Objectives": "Objectives",
    "Event kind": "Вид события",
    "Objective name": "Имя цели",
    "Objective type": "Тип цели",
    "DQL query": "DQL-запрос",
    "Display Unit": "Единица отображения",
    "Enable auto adaptive threshold": "Включить авто-адаптивный порог",
    "Reference SLO": "Эталонный SLO",
    "Comparison operator": "Оператор сравнения",
    "Warning": "Предупреждение",
    "Segments": "Сегменты",
    "Links": "Ссылки",
    "Base Unit": "Базовая единица",
    "display as unit": "отображать как единицу",
    "Decimals": "Знаки после запятой",
    "Segment ID": "ID сегмента",
    "Segment Variables": "Переменные сегмента",
    "Display text": "Отображаемый текст",
    "Variable Name": "Имя переменной",
    "Variable Values": "Значения переменной",
    "Bot token": "Токен бота",
    "Custom Property": "Пользовательское свойство",
}

PARAM_DESC = {
    "Enable or disable the connection": "Включить или отключить подключение",
    "Enter a unique display name.": "Введите уникальное отображаемое имя.",
    "Log into AbuseIPDB and create an API key. Paste the key in this field.": "Войдите в AbuseIPDB и создайте ключ API. Вставьте ключ в это поле.",
    "Provide a unique display name for your connection.": "Укажите уникальное отображаемое имя для вашего подключения.",
    "Type of scan that will be performed": "Тип сканирования, которое будет выполнено",
    "ID of the Grail ingest token to be used in this connection": "ID токена приёма Grail, используемого в этом подключении",
    "The name of the Microsoft Entra ID connection": "Имя подключения Microsoft Entra ID",
    "Directory (tenant) ID of Microsoft Entra ID": "ID каталога (тенанта) Microsoft Entra ID",
    "Application (client) ID of your app registered in Microsoft Azure App registrations": "ID приложения (клиента) вашего приложения, зарегистрированного в Microsoft Azure App registrations",
    "Client secret of your app registered in Microsoft Azure App registrations": "Секрет клиента вашего приложения, зарегистрированного в Microsoft Azure App registrations",
    "Configuration Name": "Имя конфигурации",
    "Configuration description": "Описание конфигурации",
    "Configuration Steps": "Шаги конфигурации",
    "Configuration ID": "ID конфигурации",
    "The name of the GitHub connection": "Имя подключения GitHub",
    "Type of authentication method that should be used": "Тип используемого метода аутентификации",
    "Token for the selected authentication type": "Токен для выбранного типа аутентификации",
    "A unique and clearly identifiable connection name to your GitLab instance.": "Уникальное и однозначно идентифицируемое имя подключения к вашему инстансу GitLab.",
    "The GitLab URL instance you want to connect. For example, https://gitlab.com  Include the http(s):// prefix": "Инстанс GitLab по URL, к которому нужно подключиться. Например, https://gitlab.com  Укажите префикс http(s)://",
    "The GitLab token to use for authentication. Please note that this token is not refreshed and can expire.  GitLab token in the form of `******`. Not a secret for now due to problems retrieving it from the API functions": "Токен GitLab, используемый для аутентификации. Обратите внимание, что этот токен не обновляется и может истечь.  Токен GitLab в виде `******`. Пока не secret из-за проблем с его получением через функции API",
    "A friendly name for this environment": "Понятное имя для этого окружения",
    "The environment URL to retrieve Custom DB Query V1 endpoints from  This is only used by the Custom DB Query migration feature of the app.  Do not forget to allow outbout connections to this URL in Dynatrace, under **Settings > Preferences > Limit outbound connections**": "URL окружения, из которого извлекаются эндпоинты Custom DB Query V1  Используется только функцией миграции Custom DB Query этого приложения.  Не забудьте разрешить исходящие подключения к этому URL в Dynatrace, в разделе **Settings > Preferences > Limit outbound connections**",
    "A token with **ReadConfig** scope  This allows the app to make GET calls to the Configuration V1 API": "Токен со scope **ReadConfig**  Это позволяет приложению выполнять GET-вызовы к Configuration V1 API",
    "The git service provider for this server": "Провайдер git-сервиса для этого сервера",
    "An HTTPS URL of your server (HTTP not supported) Provide only the base URL of the server, not a path to a specific project or repository (For instance, https://git.example.com)": "HTTPS URL вашего сервера (HTTP не поддерживается). Укажите только базовый URL сервера, а не путь к конкретному проекту или репозиторию (например, https://git.example.com)",
    "If turned on, requests to your Gitlab server will have the `credentials` option set to `include`. Otherwise, it will be set to `omit`.": "Если включено, запросы к вашему серверу Gitlab будут иметь опцию `credentials`, установленную в `include`. Иначе она будет установлена в `omit`.",
    "ID of the Grail ingest token to be used in this connection": "ID токена приёма Grail, используемого в этом подключении",
    "The name of the GitLab connection": "Имя подключения GitLab",
    "The name of the Jenkins connection": "Имя подключения Jenkins",
    "Base URL of your Jenkins instance (e.g. https://[YOUR\\_JENKINS\\_DOMAIN]/)": "Базовый URL вашего инстанса Jenkins (например, https://[YOUR\\_JENKINS\\_DOMAIN]/)",
    "The name of your Jenkins user (e.g. jenkins)": "Имя вашего пользователя Jenkins (например, jenkins)",
    "The password of the user or API token obtained from the Jenkins UI (Dashboard > User > Configure > API Token)": "Пароль пользователя или токен API, полученный из интерфейса Jenkins (Dashboard > User > Configure > API Token)",
    "The name of the Jira connection": "Имя подключения Jira",
    "URL of the Jira server": "URL сервера Jira",
    "Username or E-Mail address": "Имя пользователя или адрес электронной почты",
    "Password of the Jira user": "Пароль пользователя Jira",
    "The name of the EdgeConnect deployment": "Имя развёртывания EdgeConnect",
    "A pseudo-ID for the cluster, set to the UID of the kube-system namespace": "Псевдо-ID кластера, равный UID namespace kube-system",
    "The namespace where EdgeConnect is deployed": "Namespace, в котором развёрнут EdgeConnect",
    "The token required by EdgeConnect to access the ServiceAccount token.": "Токен, необходимый EdgeConnect для доступа к токену ServiceAccount.",
    "Set home launchpads for user groups. The highest ranked will be shown to the user of a group.": "Задайте домашние launchpad-ы для групп пользователей. Пользователю группы будет показан launchpad с наивысшим рангом.",
    "When set to true, the app will display monitoring candidates in the Hosts table": "Если установлено в true, приложение будет отображать кандидатов на мониторинг в таблице Hosts",
    "When set to true, the app will display app only hosts in the Hosts table": "Если установлено в true, приложение будет отображать только app-хосты в таблице Hosts",
    "The threshold at which a network device interface is deemed to be saturated.": "Порог, при котором интерфейс сетевого устройства считается насыщенным.",
    "Limit the number of results returned from Grail for Host, Network device, and Extensions entities.": "Ограничить количество результатов, возвращаемых из Grail для сущностей Host, Network device и Extensions.",
    "Limit for server-side sorting in Host, Network device and Extensions inventories. Sorting is disabled when the row count exceeds the configured threshold.": "Лимит для сортировки на стороне сервера в инвентарях Host, Network device и Extensions. Сортировка отключается, когда количество строк превышает заданный порог.",
    "Provide a unique display name for your connection.": "Укажите уникальное отображаемое имя для вашего подключения.",
    "Export as a trusted service?": "Экспортировать как доверенный сервис?",
    "A unique name for the Microsoft 365 email connection  This name needs to be unique and will be listed and selectable within the connection field of the Microsoft 365 send-email workflow action": "Уникальное имя для подключения электронной почты Microsoft 365  Это имя должно быть уникальным, оно будет отображаться и доступно для выбора в поле подключения действия workflow Microsoft 365 send-email",
    "Directory (tenant) ID of your Azure Active Directory  Please find the Directory (tenant) ID in the Microsoft Azure Portal using the service Azure Active Directory.": "ID каталога (тенанта) вашего Azure Active Directory  ID каталога (тенанта) можно найти в Microsoft Azure Portal через сервис Azure Active Directory.",
    "Application (client) ID of your app registered in Microsoft Azure App registrations  Please find the Application (client) ID in the Microsoft Azure Portal using the service App registrations.": "ID приложения (клиента) вашего приложения, зарегистрированного в Microsoft Azure App registrations  ID приложения (клиента) можно найти в Microsoft Azure Portal через сервис App registrations.",
    "The email address from which the messages will be sent  Please provide a valid email address from which the messages will be sent. Example: service.user@company.com": "Адрес электронной почты, с которого будут отправляться сообщения  Укажите корректный адрес электронной почты, с которого будут отправляться сообщения. Пример: service.user@company.com",
    "Client secret of your app registered in Microsoft Azure App registrations  Please find the Client Secret in the Microsoft Azure Portal using the service App registrations.": "Секрет клиента вашего приложения, зарегистрированного в Microsoft Azure App registrations  Секрет клиента можно найти в Microsoft Azure Portal через сервис App registrations.",
    "The name of the Microsoft Teams connection": "Имя подключения Microsoft Teams",
    "Optional": "Необязательно",
    "The Webhook URL that links to the channel  The URL is created using the `Incoming Webhook` app on Teams": "URL вебхука, ведущий на канал  URL создаётся с помощью приложения `Incoming Webhook` в Teams",
    "The name of the PagerDuty connection": "Имя подключения PagerDuty",
    "URL of the PagerDuty API endpoint": "URL эндпоинта API PagerDuty",
    "Token for the PagerDuty API endpoint": "Токен для эндпоинта API PagerDuty",
    "A unique and clearly identifiable connection name.": "Уникальное и однозначно идентифицируемое имя подключения.",
    "URL of the Ansible Automation Controller API endpoint. For example, https://ansible.yourdomain.com/api/v2/": "URL эндпоинта API Ansible Automation Controller. Например, https://ansible.yourdomain.com/api/v2/",
    "Type of authentication method that should be used.": "Тип используемого метода аутентификации.",
    "API access token for the Ansible Automation Controller. Please note that this token is not refreshed and can expire.": "Access-токен API для Ansible Automation Controller. Обратите внимание, что этот токен не обновляется и может истечь.",
    "Flag if Red Hat Event Stream is use for Event-Driven Ansible": "Флаг, используется ли Red Hat Event Stream для Event-Driven Ansible",
    "URL of the Event-Driven Ansible source plugin webhook. For example, https://eda.yourdomain.com:5010": "URL вебхука плагина-источника Event-Driven Ansible. Например, https://eda.yourdomain.com:5010",
    "API access token for the Event-Driven Ansible Controller. Please note that this token is not refreshed and can expire.": "Access-токен API для Event-Driven Ansible Controller. Обратите внимание, что этот токен не обновляется и может истечь.",
    "A unique and clearly identifiable connection name to your ServiceNow instance.": "Уникальное и однозначно идентифицируемое имя подключения к вашему инстансу ServiceNow.",
    "URL of the ServiceNow instance.": "URL инстанса ServiceNow.",
    "Username or Email address.": "Имя пользователя или адрес электронной почты.",
    "Password of the ServiceNow user.": "Пароль пользователя ServiceNow.",
    "Client ID of the ServiceNow OAuth server": "ID клиента OAuth-сервера ServiceNow",
    "Client secret of the ServiceNow OAuth server": "Секрет клиента OAuth-сервера ServiceNow",
    "Define key/value pairs that further describe this guardian.": "Задайте пары ключ/значение, которые дополнительно описывают этот guardian.",
    "Define variables for dynamically defining DQL queries": "Задайте переменные для динамического определения DQL-запросов",
    "If set to null/'BIZ\\_EVENT' validation events stored as bizevents in Grail. If set to 'SDLC\\_EVENT' validation events stored as SDLC events": "Если задано null/'BIZ\\_EVENT', события валидации сохраняются как bizevents в Grail. Если задано 'SDLC\\_EVENT', события валидации сохраняются как SDLC events",
    "Please enter the metric key of your desired SLO. SLO metric keys have to start with 'func:slo.'": "Введите ключ метрики нужного SLO. Ключи метрик SLO должны начинаться с 'func:slo.'",
    "HTTPS link associated with this objective.": "HTTPS-ссылка, связанная с этой целью.",
    "Short description for the link.": "Краткое описание для ссылки.",
    "Fields for adding relevant links to this objective.": "Поля для добавления релевантных ссылок к этой цели.",
    "Provide a unique and clearly identifiable connection name to your Slack App.": "Укажите уникальное и однозначно идентифицируемое имя подключения к вашему приложению Slack.",
    "The bot token obtained from the Slack App Management UI.  Bot token in the format `xoxb-******`": "Токен бота, полученный из интерфейса Slack App Management.  Токен бота в формате `xoxb-******`",
    "Log into VirusTotal and create an API key. Paste the key in this field.": "Войдите в VirusTotal и создайте ключ API. Вставьте ключ в это поле.",
    "Changing this will break the app": "Изменение этого сломает приложение",
    "URL of salesforce instance": "URL инстанса salesforce",
    # biz-flow: desc cell literally repeats the label (rows 45/47). Correlation
    # ID must mirror its label RU; KPI is an EN-locked acronym (identity).
    "Correlation ID": "ID корреляции",
    "KPI": "KPI",
}

# ----------------------------------------------------------------------------
# (4) Structural exact-string canon (whole-line / newline-anchored).
# ----------------------------------------------------------------------------
STRUCT = [
    # parent schemas.md table header: Name->Имя (corpus-dominant `| Имя |`,
    # 5x shipped), Schema/Scopes EN-locked domain vocab (L4-AE). Single-word
    # cells -> both LATIN-RUN(>=5) and SHORT(>=2w) miss it (blind-spot class).
    ("| Name | Schema | Scopes |", "| Имя | Schema | Scopes |"),
    ("Retrieve schema via Settings API", "Получить schema через Settings API"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    (
        "To execute this request, you need an access token with **Read settings** "
        "(`settings.read`) scope. To learn how to obtain and use it, see "
        "[Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        # Canon from shipped L4-AE objects/ same-subsection anchor (L4T#1):
        # "запроса" not "этого запроса"; "использовать токен" not "его".
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
    t = t.replace("\r\n", "\n")  # EN CRLF -> RU LF
    # BOM: real U+FEFF + the literal 3-char sequence (U+00EF U+00BB U+00BF),
    # which appears INSIDE link-text in gitlab/kubernetes/SRG/slack files (L4M).
    t = t.replace(chr(0xFEFF), "")
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")
    return t


def _heading(line):
    """`### <Name> (\`app:...)\`` -> `### <RU name> (\`app:...)\``. The closing
    paren is OUTSIDE the backtick in source; preserve byte-for-byte."""
    marker = " (`app:"
    i = line.find(marker)
    if not line.startswith("### ") or i == -1:
        return None
    name = line[4:i]
    tail = line[i:]  # ` (\`app:...)\`` verbatim
    ru = DISPLAY_NAME.get(name)
    if ru is None:
        return None
    return "### " + ru + tail


def _param_row(line):
    """`| <Label> \`code\` | <type> | <Desc> | <Req> |` -> translate Label +
    Desc; code/type/Req EN-verbatim. Schema-meta/GET/endpoint/header rows are
    NOT matched here (no \`code\` token in col-1, or col-1 is empty)."""
    if not line.startswith("| ") or not line.endswith(" |"):
        return None
    cells = line[2:-2].split(" | ")
    if len(cells) != 4:
        return None
    c0, ctype, cdesc, creq = cells
    if "`" not in c0:
        return None  # not a parameter row (header / schema-meta / endpoint)
    # split col-1 into "<label> " + "`code`"
    bt = c0.find("`")
    label = c0[:bt].rstrip()
    code = c0[bt:]  # `code` (+ any trailing) verbatim
    sep = c0[len(label) : bt]  # whitespace between label and code (usually " ")
    if label not in PARAM_LABEL:
        return None
    new_label = PARAM_LABEL[label]
    # description: split off optional enum-phrase tail ("... The element has
    # these enums * `a` * `b`"). Everything from ENUM_PHRASE on stays as the
    # canon RU + verbatim enum list.
    d = cdesc
    ei = d.find(ENUM_PHRASE[0])
    if ei != -1:
        head = d[:ei].rstrip()
        enum_tail = d[ei + len(ENUM_PHRASE[0]) :]  # " * `a` * `b`" verbatim
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


def _object_heading(line):
    """`##### The \`X\` object` -> `##### Объект \`X\`` (keep level + code)."""
    s = line.lstrip("#")
    hashes = line[: len(line) - len(s)]
    s = s.strip()
    if s.startswith("The `") and s.endswith("` object"):
        code = s[len("The ") : -len(" object")]  # `X`
        return hashes + " Объект " + code
    return None


def _parent_row(line):
    """schemas.md table row: `| [Name](url) | \`schema\` | <scopes> |`.
    Translate ONLY the link display-name; URL + schema + WHOLE scopes cell
    EN-verbatim. Faithful to literal `|` inside link text (IBM row, L93)."""
    if not line.startswith("| [") or not line.endswith(" |"):
        return None
    # find `](` that closes the display-name link
    close = line.find("](")
    if close == -1:
        return None
    name = line[3:close]  # text between `[` and `](`
    ru = DISPLAY_NAME.get(name)
    if ru is None:
        return None
    return "| [" + ru + line[close:]


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    t = io.open(src, "r", encoding="utf-8", newline="").read()
    t = _normalize(t)
    # whole-line maps applied first (descriptions/notes/link-lines), then
    # structural canon, then per-line transforms.
    for en, ru in DESCRIPTIONS.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in NOTES.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in LINK_LINES.items():
        t = t.replace("\n" + en + "\n", "\n" + ru + "\n")
    for en, ru in STRUCT:
        t = t.replace(en, ru)
    out = []
    for line in t.split("\n"):
        nl = (
            _parent_row(line)
            or _heading(line)
            or _object_heading(line)
            or _param_row(line)
        )
        out.append(nl if nl is not None else line)
    t = "\n".join(out)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return src, dst


if __name__ == "__main__":
    files = [PARENT] + [
        os.path.relpath(p, EN).replace("\\", "/")
        for p in sorted(glob.glob(os.path.join(EN, APP_GLOB)))
    ]
    bad = 0
    for rel in files:
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
        print("%-78s EN=%4d RU=%4d%s" % (rel, en_n, ru_n, flag))
    print("\n%d files, %d parity mismatches" % (len(files), bad))
