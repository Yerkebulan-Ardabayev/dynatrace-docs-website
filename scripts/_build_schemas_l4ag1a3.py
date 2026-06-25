# -*- coding: utf-8 -*-
"""L4-AG.1a.3 builder: 35 builtin-*.md schema-table files (1.95-2.2 KB) from
docs/managed/dynatrace-api/environment-api/settings/schemas/.

Class L4-AF schema-table (## Authentication + ## Parameters + Schema-ID/Scope
row + GET endpoints). Anchor canon: L4-AG.1a.2 _build_schemas_l4ag1a2.py.

Lessons L4-AG.1a.2 applied:
  - ENUM_PHRASE global substring-replace (works when row label is empty/missing).
  - mojibake byte-audit done BEFORE first build (rum-host-headers `canât` /
    `wonât` U+2019 double-mojibake, networkzones `â `
    U+26A0 warning-sign double-mojibake). EN keys verbatim with these byte-sequences.
  - "your-X" -> drop when redundant (Russian rarely needs the possessive).

BOM U+EFBBBF stripped by _normalize() inside link-text in 16 files.
"""

import os, io

EN = "docs/managed/dynatrace-api/environment-api/settings/schemas"
RU = "docs/managed-ru/dynatrace-api/environment-api/settings/schemas"

PILOT = [
    "builtin-app-engine-registry-cloud-development-environments.md",
    "builtin-dashboards-image-allowlist.md",
    "builtin-rum-web-beacon-endpoint.md",
    "builtin-synthetic-http-scheduling.md",
    "builtin-synthetic-synthetic-availability-settings.md",
    "builtin-synthetic-http-assigned-applications.md",
    "builtin-monitored-technologies-go.md",
    "builtin-problem-fields.md",
    "builtin-synthetic-browser-scheduling.md",
    "builtin-logmonitoring-log-custom-attributes.md",
    "builtin-synthetic-browser-assigned-applications.md",
    "builtin-hub-channel-subscriptions.md",
    "builtin-ownership-config.md",
    "builtin-appsec-notification-attack-alerting-profile.md",
    "builtin-rum-web-rum-javascript-file-name.md",
    "builtin-usability-analytics.md",
    "builtin-monitored-technologies-php.md",
    "builtin-settings-subscriptions-service.md",
    "builtin-attribute-block-list.md",
    "builtin-attribute-allow-list.md",
    "builtin-tokens-token-settings.md",
    "builtin-synthetic-http-cookies.md",
    "builtin-dashboards-presets.md",
    "builtin-eec-local.md",
    "builtin-monitored-technologies-wsmb.md",
    "builtin-bizevents-http-capturing-variants.md",
    "builtin-rum-web-xhr-exclusion.md",
    "builtin-logmonitoring-log-buckets-rules.md",
    "builtin-dashboards-general.md",
    "builtin-rum-host-headers.md",
    "builtin-networkzones.md",
    "builtin-rum-web-ipaddress-exclusion.md",
    "builtin-oneagent-features.md",
    "builtin-host-monitoring-advanced.md",
    "builtin-openpipeline-logs-routing.md",
]

# Schema heading display-name. EN product/tech terms kept (Go/PHP/Cookies/...).
DISPLAY_NAME = {
    "Cloud Development Environments": "Cloud Development Environments",
    "Allowed URL pattern rules": "Правила разрешённых URL-шаблонов",
    "Beacon endpoint settings": "Настройки эндпоинта beacon",
    "Frequency and locations": "Частота и расположения",
    "Synthetic availability": "Доступность Synthetic",
    "Assign synthetic monitor to applications": "Назначение synthetic-монитора приложениям",
    "Go": "Go",
    "Problem fields": "Поля проблемы",
    "Log custom attributes": "Пользовательские атрибуты логов",
    "Assign synthetic monitor to web applications": "Назначение synthetic-монитора веб-приложениям",
    "Hub subscriptions": "Подписки Hub",
    "Configure ownership": "Настройка владения",
    "Attack alerting profiles": "Профили оповещений об атаках",
    "RUM monitoring code filename": "Имя файла кода мониторинга RUM",
    "Usability analytics": "Аналитика юзабилити",
    "PHP": "PHP",
    "Key requests": "Ключевые запросы",
    "Blocked attributes": "Заблокированные атрибуты",
    "Allowed attributes": "Разрешённые атрибуты",
    "Access tokens": "Access tokens",
    "Cookies": "Cookies",
    "Preset settings": "Настройки предустановок",
    "Extension Execution Controller": "Extension Execution Controller",
    "IBM Integration Bus | IBM App Connect Enterprise": "IBM Integration Bus | IBM App Connect Enterprise",
    "OneAgent Business events capturing variants": "Варианты захвата Business events для OneAgent",
    "Exclude XHR requests from monitoring": "Исключение XHR-запросов из мониторинга",
    "Log buckets": "Бакеты логов",
    "General settings": "Общие настройки",
    "Identify host names": "Идентификация имён хостов",
    "Network zones settings": "Настройки network zones",
    "Exclude IP addresses from monitoring": "Исключение IP-адресов из мониторинга",
    "OneAgent features": "Возможности OneAgent",
    "Advanced Settings": "Расширенные настройки",
    "Ingest routing configuration (logs)": "Конфигурация маршрутизации ingest (логи)",
}

# Whole-line schema descriptions (replaced as `\n` + EN + `\n` -> `\n` + RU + `\n`).
SCHEMA_DESC = {
    # 1. cloud-development-environments
    "In order to enable Cloud Development Environment (CDE) for application development, the respective domains need to be configured here.": "Чтобы включить Cloud Development Environment (CDE) для разработки приложений, здесь нужно настроить соответствующие домены.",
    # 2. dashboards-image-allowlist
    "Configure allowed URL patterns to fetch external resources such as images. For an image to be uploaded, the configured URL must match one of the specified patterns.": "Настройте разрешённые URL-шаблоны для загрузки внешних ресурсов, таких как изображения. Чтобы изображение было загружено, настроенный URL должен соответствовать одному из указанных шаблонов.",
    # 3. rum-web-beacon-endpoint (BOM stripped from link text)
    "Define where OneAgent is to send your web application monitoring data.": "Задайте, куда OneAgent должен отправлять данные мониторинга веб-приложения.",
    "Learn more about how to [configure the beacon endpoint](https://dt-url.net/yp036lb).": "Подробнее о том, как [configure the beacon endpoint](https://dt-url.net/yp036lb).",
    # 4. synthetic-http-scheduling (BOM stripped)
    "Select how frequently this monitor should run at each enabled location. For more information, see [how do I create an HTTP monitor?](https://dt-url.net/xs03wvi)": "Выберите, как часто этот монитор должен выполняться в каждом включённом расположении. Подробнее см. [how do I create an HTTP monitor?](https://dt-url.net/xs03wvi)",
    # 5. synthetic-synthetic-availability-settings
    "Dynatrace offers the possibility to configure maintenance windows. By default maintenance windows only affect problem detection and alerting. You can change this behavior and calculate availability including/excluding maintenance window periods.": "Dynatrace позволяет настраивать окна обслуживания. По умолчанию окна обслуживания влияют только на определение проблем и оповещения. Вы можете изменить это поведение и считать доступность с учётом или без учёта периодов окон обслуживания.",
    # 6. synthetic-http-assigned-applications
    "Assigned applications will gain availability information and be considered in the root cause analysis of problems that impact this monitor.": "Назначенные приложения получат информацию о доступности и будут учитываться в анализе первопричины проблем, влияющих на этот монитор.",
    # 7. monitored-technologies-go family (enabled-by-default, BOM in link text — covered by docs/known limitations)
    "By default, Go monitoring is enabled on all hosts. If you want to disable Go monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг Go включён на всех хостах. Если вы хотите отключить мониторинг Go на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable Go monitoring only on selected hosts, disable global Go monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг Go только на отдельных хостах, отключите глобальный мониторинг Go и включите его на этих хостах через их настройки.",
    # 8. problem-fields
    "Problem fields allow you to define rules for extracting specific fields from events to problems. Events are stored in dt.davis.events and problems in dt.davis.problems. Each setting represents a unique rule, specifying which event fields should be extracted to the problem, ensuring critical information is carried over and easily accessible.": "Поля проблемы позволяют задавать правила извлечения определённых полей из событий в проблемы. События хранятся в dt.davis.events, проблемы хранятся в dt.davis.problems. Каждая настройка представляет собой уникальное правило, указывающее, какие поля события должны быть извлечены в проблему, чтобы критически важная информация переносилась и оставалась легкодоступной.",
    # 9. synthetic-browser-scheduling (BOM stripped)
    "Select how frequently this monitor should run at each enabled location. For more information, see [how do I create a browser monitor?](https://dt-url.net/qj1p0p2b)": "Выберите, как часто этот монитор должен выполняться в каждом включённом расположении. Подробнее см. [how do I create a browser monitor?](https://dt-url.net/qj1p0p2b)",
    # 10. logmonitoring-log-custom-attributes
    "Dynatrace log monitoring gives you the ability to define custom attributes for ingested logs.": "Мониторинг логов Dynatrace позволяет задавать пользовательские атрибуты для загружаемых логов.",
    # 11. synthetic-browser-assigned-applications
    "Assigned web applications will gain availability information and be considered in the root cause analysis of problems that impact this monitor.": "Назначенные веб-приложения получат информацию о доступности и будут учитываться в анализе первопричины проблем, влияющих на этот монитор.",
    # 12. hub-channel-subscriptions (BOM stripped)
    "Here you can manage your subscriptions to extend the available apps or releases listed in [Dynatrace Hub](https://www.dynatrace.com/support/help/manage/hub). Add a new token to enroll your subscription.": "Здесь можно управлять подписками для расширения списка доступных приложений или релизов в [Dynatrace Hub](https://www.dynatrace.com/support/help/manage/hub). Добавьте новый токен, чтобы зарегистрировать подписку.",
    # 13. ownership-config (BOM stripped)
    "Configure keys for ownership metadata and tags. [See documentation](https://dt-url.net/ownership-custom-keys)": "Настройте ключи для метаданных владения и тегов. [See documentation](https://dt-url.net/ownership-custom-keys)",
    # 14. appsec-notification-attack-alerting-profile
    "Attack alerting profiles enable you to set up alert-filtering rules that are based on the state of detected attacks. This allows you to control which conditions result in security notifications and which don't.": "Профили оповещений об атаках позволяют настроить правила фильтрации оповещений на основе состояния обнаруженных атак. Это даёт возможность контролировать, какие условия приводят к уведомлениям безопасности, а какие нет.",
    # 15. rum-web-rum-javascript-file-name (BOM stripped)
    "Define a custom filename prefix that should be used instead of the default prefix in the RUM monitoring code filename, which is ruxitagentjs or ruxitagent, see [Configure the Real User Monitoring code source](https://dt-url.net/wc03z4k) for details.": "Задайте пользовательский префикс имени файла, который будет использоваться вместо префикса по умолчанию в имени файла кода мониторинга RUM (ruxitagentjs или ruxitagent). Подробнее см. [Configure the Real User Monitoring code source](https://dt-url.net/wc03z4k).",
    "**Note:** Be aware that you may experience a temporary reduction in collected RUM data after changing the RUM monitoring code filename prefix. Therefore, this setting should not be changed frequently.": "**Примечание:** учтите, что после смены префикса имени файла кода мониторинга RUM возможно временное снижение объёма собираемых данных RUM. Поэтому эту настройку не следует менять часто.",
    # 16. usability-analytics (BOM stripped)
    "Analyze detected usability issues within your application.": "Анализируйте обнаруженные проблемы юзабилити в приложении.",
    "User action types that commonly reflect user frustration include dead clicks, rage clicks, rage rotates, and page refreshes.": "К типам пользовательских действий, обычно отражающих фрустрацию пользователя, относятся мёртвые клики, rage-клики, rage-повороты и обновления страницы.",
    # 17. monitored-technologies-php family (enabled-by-default)
    "By default, PHP monitoring is enabled on all hosts. If you want to disable PHP monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг PHP включён на всех хостах. Если вы хотите отключить мониторинг PHP на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable PHP monitoring only on selected hosts, disable global PHP monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг PHP только на отдельных хостах, отключите глобальный мониторинг PHP и включите его на этих хостах через их настройки.",
    # 18. settings-subscriptions-service (BOM stripped)
    "Configuration for specifying Key requests for a particular Service. Each Service could have several Key requests.": "Конфигурация для указания ключевых запросов для конкретного сервиса. У каждого сервиса может быть несколько ключевых запросов.",
    "* Key requests can be used to have long-term metric history and dedicated dashboard tiles for charting and direct access from your dashboard. Request naming rules can affect Key requests and vice versa.": "* Ключевые запросы можно использовать для долгосрочной истории метрик и выделенных плиток дашбордов для построения графиков и прямого доступа с дашборда. Правила именования запросов могут влиять на ключевые запросы и наоборот.",
    "* When you set up a Request naming rule that affects Key requests, to keep a renamed request as Key request you must provide the final name (after all Request naming rules are applied) here.": "* При настройке правила именования запросов, влияющего на ключевые запросы, чтобы переименованный запрос остался ключевым, укажите здесь итоговое имя (после применения всех правил именования запросов).",
    'You can learn more about Key requests in our [help](https://dt-url.net/ss03uui "Visit dynatrace.com").': 'Подробнее о ключевых запросах в нашей [help](https://dt-url.net/ss03uui "Visit dynatrace.com").',
    # 19. attribute-block-list (BOM stripped)
    "While Dynatrace automatically captures all OpenTelemetry attributes, to prevent the accidental storage of personal data, you may exclude certain attribute keys for which the values must not be persisted. This enables you to meet your privacy requirements while controlling the amount of monitoring data that's persisted. For further details on Dynatrace's privacy settings, visit the [Data privacy and security](https://dt-url.net/bo210srx) documentation.": "Dynatrace автоматически захватывает все атрибуты OpenTelemetry; чтобы избежать случайного сохранения персональных данных, можно исключить отдельные ключи атрибутов, значения которых не должны сохраняться. Это позволяет соответствовать требованиям приватности, контролируя объём сохраняемых данных мониторинга. Подробнее о настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/bo210srx).",
    # 20. attribute-allow-list (BOM stripped)
    "While Dynatrace automatically captures all OpenTelemetry attributes, to prevent the accidental storage of personal data, only the values of attributes for which a related key is specified in the allow-list below are persisted. This enables you to meet your privacy requirements while controlling the amount of monitoring data that's persisted. For further details on Dynatrace's privacy settings, visit the [Data privacy and security](https://dt-url.net/bo210srx) documentation.": "Dynatrace автоматически захватывает все атрибуты OpenTelemetry; чтобы избежать случайного сохранения персональных данных, сохраняются только значения тех атрибутов, ключи которых указаны в allow-list ниже. Это позволяет соответствовать требованиям приватности, контролируя объём сохраняемых данных мониторинга. Подробнее о настройках приватности Dynatrace см. документацию [Data privacy and security](https://dt-url.net/bo210srx).",
    # 21. tokens-token-settings (BOM stripped)
    "Configure Dynatrace API access token and personal access token generation. For details about tokens and authentication go to [Dynatrace API authentication documentation](https://dt-url.net/8543sda).": "Настройте генерацию access token Dynatrace API и personal access token. Подробнее о токенах и аутентификации см. [Dynatrace API authentication documentation](https://dt-url.net/8543sda).",
    # 22. synthetic-http-cookies
    "Set cookies to store state information or instruct the server not to send certain kinds of information.": "Установите cookies, чтобы хранить информацию о состоянии или указывать серверу не отправлять определённые виды информации.",
    # 23. dashboards-presets
    "Configure dashboard preset settings.": "Настройте параметры предустановок дашбордов.",
    # 24. eec-local (BOM stripped, twin к eec-remote из L4-AG.1a.2 «for ActiveGate»)
    "Extension Execution Controller configuration for OneAgent deployment": "Конфигурация Extension Execution Controller для развёртывания OneAgent",
    # 25. monitored-technologies-wsmb family (enabled-by-default, имя с pipe)
    "By default, IBM Integration Bus | IBM App Connect Enterprise monitoring is enabled on all hosts. If you want to disable IBM Integration Bus | IBM App Connect Enterprise monitoring on selected hosts, disable it on these hosts via their settings.": "По умолчанию мониторинг IBM Integration Bus | IBM App Connect Enterprise включён на всех хостах. Если вы хотите отключить мониторинг IBM Integration Bus | IBM App Connect Enterprise на отдельных хостах, отключите его на этих хостах через их настройки.",
    "If you want to enable IBM Integration Bus | IBM App Connect Enterprise monitoring only on selected hosts, disable global IBM Integration Bus | IBM App Connect Enterprise monitoring and enable it on these hosts via their settings.": "Если вы хотите включить мониторинг IBM Integration Bus | IBM App Connect Enterprise только на отдельных хостах, отключите глобальный мониторинг IBM Integration Bus | IBM App Connect Enterprise и включите его на этих хостах через их настройки.",
    # 26. bizevents-http-capturing-variants
    "OneAgent capturing variants.": "Варианты захвата OneAgent.",
    "Capture rules tell OneAgent to capture generic content-types, add capture variants below.": "Правила захвата указывают OneAgent захватывать обобщённые content-type; варианты захвата добавьте ниже.",
    # 27. rum-web-xhr-exclusion
    "Specify a regular expression to match all URLs that should be excluded from becoming XHR actions.": "Укажите регулярное выражение для совпадения со всеми URL, которые должны быть исключены из XHR-действий.",
    "Dynatrace supports the JavaScript Regular Expressions syntax. The separation between different protocols of the URIs is not supported (every protocol of the URI will be excluded).": "Dynatrace поддерживает синтаксис JavaScript Regular Expressions. Разделение по разным протоколам URI не поддерживается (каждый протокол URI будет исключён).",
    # 28. logmonitoring-log-buckets-rules (BOM stripped)
    "Dynatrace logs are stored in buckets. You can give each bucket a unique log retention period (35 days is the default). In addition, you can use buckets to set unique access rules to different logs or log areas. To create or manage buckets go to [bucket permissions](https://dt-url.net/vc034se). Read more about using buckets for logs in our [documentation](https://dt-url.net/ep234n2).": "Логи Dynatrace хранятся в бакетах. Каждому бакету можно задать уникальный период хранения логов (по умолчанию 35 дней). Кроме того, бакеты позволяют задавать уникальные правила доступа к разным логам или областям логов. Для создания и управления бакетами перейдите в [bucket permissions](https://dt-url.net/vc034se). Подробнее об использовании бакетов для логов см. [documentation](https://dt-url.net/ep234n2).",
    # 29. dashboards-general
    "Configure anonymous access and home dashboard settings.": "Настройте параметры анонимного доступа и домашнего дашборда.",
    # 30. rum-host-headers (double-mojibake U+2019 — verbatim byte-keys)
    "Specify HTTP request headers OneAgent can use to identify your application's host names, whenever Dynatrace canât automatically identify them. Provided headers are processed sequentially, with the ones at the top of the list taking priority. Learn why it's important and when we can't identify them.": "Укажите HTTP-заголовки запросов, которые OneAgent может использовать для идентификации имён хостов приложения, когда Dynatrace не может определить их автоматически. Указанные заголовки обрабатываются последовательно, приоритет имеют те, что выше в списке. Узнайте, почему это важно и когда определить имена не получается.",
    "Dynatrace uses host names as part of the URL that is matched against your application detection rules, which control when OneAgent injects the RUM JavaScript tag. For instance, when your web server operates behind a firewall using a different host name your application detection rule wonât match and OneAgent wonât inject RUM into your application.": "Dynatrace использует имена хостов как часть URL, который сопоставляется с правилами определения приложения; эти правила контролируют, когда OneAgent внедряет JavaScript-тег RUM. Например, если веб-сервер работает за файрволом и использует другое имя хоста, правило определения приложения не совпадёт и OneAgent не внедрит RUM в приложение.",
    # 31. networkzones (BOM stripped, 4-line list)
    "In combination with ActiveGates, network zones save bandwidth and infrastructure costs by": "В сочетании с ActiveGate, network zones экономят полосу пропускания и затраты на инфраструктуру за счёт:",
    "* Compressing traffic": "* Сжатия трафика",
    "* Optimizing traffic routing": "* Оптимизации маршрутизации трафика",
    "* Preventing unrelated traffic in between data centers and regions": "* Предотвращения нерелевантного трафика между ЦОД и регионами",
    # 32. rum-web-ipaddress-exclusion
    "Enable the switch below if the IP addresses are to be included. Disable the switch if they are to be excluded.": "Включите переключатель ниже, если IP-адреса должны быть включены. Выключите его, если они должны быть исключены.",
    # 33. oneagent-features
    "Dynatrace OneAgent follows a zero-configuration approach. Therefore, the set of default features apply when you roll out OneAgent the first time. When additional features become available with newer OneAgent versions, they can be activated here to make them available across your environment.": "Dynatrace OneAgent работает по принципу zero-configuration. Поэтому при первом развёртывании OneAgent применяется набор возможностей по умолчанию. Когда с новыми версиями OneAgent появляются дополнительные возможности, их можно активировать здесь, чтобы сделать доступными во всём окружении.",
    # 34. host-monitoring-advanced (BOM stripped)
    "You can switch off the injection of the ProcessAgent and of CodeModules.": "Вы можете отключить внедрение ProcessAgent и CodeModules.",
    # 35. openpipeline-logs-routing
    "Contains configuration of routing": "Содержит конфигурацию маршрутизации",
}

# Parameter table col-1 label (text before `\`code\``).
PARAM_LABEL = {
    # 1
    "Cloud Development Environments": "Cloud Development Environments",
    # 2
    "List of URL pattern matchers": "Список URL-сопоставителей",
    "Rule": "Правило",
    "Pattern": "Шаблон",
    # 3
    "Type": "Тип",
    "URL": "URL",
    "Send beacon data via CORS": "Отправлять данные beacon через CORS",
    # 4, 9, synthetic-multiprotocol-scheduling (уже в L4-AG.1a.2)
    "Frequency": "Частота",
    "Locations": "Расположения",
    "Location": "Расположение",
    # 5
    "Exclude periods with maintenance windows from availability calculation": "Исключать периоды с окнами обслуживания из расчёта доступности",
    # 6, 11
    "Assigned applications": "Назначенные приложения",
    "Application": "Приложение",
    # 7
    "Monitor Go": "Мониторить Go",
    "Enable Go static application monitoring": "Включить статический мониторинг приложений Go",
    # 8, 12, 13, 14, 19, 20, 28, 33
    "Enabled": "Включено",
    "Event field": "Поле события",
    "Problem field": "Поле проблемы",
    # 10
    "Key": "Ключ",
    "Show attribute values in side bar": "Показывать значения атрибутов в боковой панели",
    # 12
    "Subscriptions": "Подписки",
    "Name of subscription": "Имя подписки",
    "Subscription token": "Токен подписки",
    "Description": "Описание",
    # 13
    "Keys for ownership metadata and tags": "Ключи для метаданных владения и тегов",
    "Key for ownership metadata and tags": "Ключ для метаданных владения и тегов",
    # 14
    "Name": "Имя",
    "Attack State": "Состояние атаки",
    # 15
    "Custom filename prefix": "Пользовательский префикс имени файла",
    # 16
    "Detect rage clicks": "Определять rage-клики",
    # 17
    "Monitor PHP": "Мониторить PHP",
    "Enable FastCGI PHP processes launched by Apache HTTP Server": "Включить FastCGI-процессы PHP, запущенные Apache HTTP Server",
    "Monitor PHP CLI web server": "Мониторить веб-сервер PHP CLI",
    # 18
    "Key request names": "Имена ключевых запросов",
    # 19, 20
    "Attribute key": "Ключ атрибута",
    # 21
    "Create Dynatrace API tokens in the new format": "Создавать токены Dynatrace API в новом формате",
    "Enable personal access tokens": "Включить personal access tokens",
    # 22
    "Set cookies": "Установить cookies",
    "Value": "Значение",
    "Domain": "Домен",
    "Path (optional)": "Путь (необязательно)",
    # 23
    "Enable presets": "Включить предустановки",
    "Limit preset visibility": "Ограничить видимость предустановок",
    "Dashboard preset": "Предустановка дашборда",
    "User group": "Группа пользователей",
    "Home dashboard": "Домашний дашборд",
    "Home dashboards": "Домашние дашборды",
    # 24
    "Enable Extension Execution Controller": "Включить Extension Execution Controller",
    "Enable local HTTP Metric, Log and Event Ingest API": "Включить локальный HTTP-API для приёма метрик, логов и событий",
    "Enable Dynatrace StatsD": "Включить Dynatrace StatsD",
    "Performance profile": "Профиль производительности",
    # 26
    "Content-type matcher": "Сопоставитель Content-type",
    "Content-type match value": "Значение сопоставления Content-type",
    "Parser": "Парсер",
    # 28
    "Rule name": "Имя правила",
    "Bucket": "Бакет",
    "Matcher (DQL)": "Сопоставитель (DQL)",
    # 29
    "Allow anonymous access": "Разрешить анонимный доступ",
    # 30
    "HTTP header format": "Формат HTTP-заголовка",
    # 31
    "Enable network zones in this environment.": "Включить network zones в этом окружении.",
    # 32
    "IP addresses exclusion list": "Список исключения IP-адресов",
    "These are the only IP addresses that should be monitored": "Это единственные IP-адреса, которые должны быть в мониторинге",
    "Single IP or IP range start address": "Одиночный IP или начальный адрес диапазона",
    "IP range end": "Конец диапазона IP",
    # 33
    "Instrumentation enabled (change needs a process restart)": "Инструментирование включено (для изменения требуется перезапуск процесса)",
    "Activate this feature also in OneAgents only fulfilling the minimum Opt-In version": "Активировать эту возможность также в OneAgent, удовлетворяющих только минимальной Opt-In версии",
    "Feature": "Возможность",
    # 34
    "ProcessAgent injection": "Внедрение ProcessAgent",
    "CodeModule injection": "Внедрение CodeModule",
    # 35
    "Routing for pipelines": "Маршрутизация для pipeline",
    "Pipeline Type": "Тип pipeline",
    "Pipeline ID": "ID pipeline",
    "Builtin Pipeline ID": "ID встроенного pipeline",
    "Query which determines whether the record should be routed to the target pipeline of this rule.": "Запрос, определяющий, должна ли запись быть направлена в целевой pipeline этого правила.",
}

# Parameter table col-3 description (when not just `-` and not enum-tail).
PARAM_DESC = {
    # 1
    "The URL to allow app development from. E.g. `https://*.my-company.my-cde-provider.com`.": "URL, с которого разрешена разработка приложений. Например `https://*.my-company.my-cde-provider.com`.",
    # 3
    "You can specify either path segments or an absolute URL.": "Можно указать либо сегменты пути, либо абсолютный URL.",
    "Learn more about [sending beacon data via CORS](https://dt-url.net/r7038sa)": "Подробнее о [sending beacon data via CORS](https://dt-url.net/r7038sa)",
    # 4, 9, multiprotocol-scheduling (уже в L4-AG.1a.2)
    "How often the monitor is executed. Supported values are 1, 2, 5, 10, 15, 30 and 60 minutes": "Как часто выполняется монитор. Поддерживаемые значения: 1, 2, 5, 10, 15, 30 и 60 минут",
    "How often the monitor is executed. Supported values are 5, 10, 15, 30, 60, 120 and 240 minutes": "Как часто выполняется монитор. Поддерживаемые значения: 5, 10, 15, 30, 60, 120 и 240 минут",
    # 7
    "Learn more about the [known limitations for Go static monitoring](https://www.dynatrace.com/support/help/technology-support/application-software/go/support/go-known-limitations#limitations)": "Подробнее об [known limitations for Go static monitoring](https://www.dynatrace.com/support/help/technology-support/application-software/go/support/go-known-limitations#limitations)",
    # 8
    "If this is true, the field is extracted from events to problems.": "Если true, поле извлекается из событий в проблемы.",
    "Field from the event that will be extracted.": "Поле события, которое будет извлечено.",
    "Field under which the extracted event data will be stored on the problem.": "Поле, под которым извлечённые данные события будут сохранены в проблеме.",
    # 10
    "The attribute key is case sensitive in log data ingestion.": "Ключ атрибута чувствителен к регистру при приёме данных логов.",
    "In the case of Log Monitoring Classic, the change applies to newly ingested log events. This attribute won't search any log events ingested before this option was toggled on. In Logs on Grail's case, the switch's state is ignored.": "В случае Log Monitoring Classic изменение применяется к новым принятым событиям логов. Этот атрибут не будет искать события логов, принятые до включения этой опции. В случае Logs on Grail состояние переключателя игнорируется.",
    # 13
    "Tags and metadata are key-value pairs. Define keys for tags and metadata that are considered for ownership. If a tag or any metadata starts with a key defined below, the value of the tag or metadata is considered a team identifier.": "Теги и метаданные представляют собой пары ключ-значение. Задайте ключи для тегов и метаданных, которые учитываются при определении владения. Если тег или метаданные начинаются с ключа, определённого ниже, значение тега или метаданных считается идентификатором команды.",
    # 15: (no per-row desc in this file)
    # 16
    "Three or more rapid clicks within the same area of a web page are considered to be rage clicks. Rage clicks commonly reflect slow-loading or failed page resources. Rage click counts are compiled for each session and considered in the [User Experience Score](https://dt-url.net/39034wt) . With this setting enabled, a rage click count is compiled for each monitored user session.": "Три или более быстрых клика в одной области веб-страницы считаются rage-кликами. Rage-клики обычно отражают медленно загружающиеся или сломанные ресурсы страницы. Счётчики rage-кликов формируются для каждой сессии и учитываются в [User Experience Score](https://dt-url.net/39034wt) . Если эта настройка включена, счётчик rage-кликов формируется для каждой отслеживаемой пользовательской сессии.",
    # 17
    "Requires PHP monitoring enabled and from Dynatrace OneAgent version 1.191 it's ignored and permanently enabled": "Требуется включённый мониторинг PHP; начиная с Dynatrace OneAgent версии 1.191 параметр игнорируется и постоянно включён",
    "Requires enabled PHP monitoring and Dynatrace OneAgent version 1.261 or later": "Требуется включённый мониторинг PHP и Dynatrace OneAgent версии 1.261 или новее",
    # 19, 20
    "If this is true, the value of the specified key is not persisted.": "Если true, значение указанного ключа не сохраняется.",
    "Key of the attribute that should not be persisted": "Ключ атрибута, который не должен сохраняться",
    "If this is true, the value of the specified key is persisted.": "Если true, значение указанного ключа сохраняется.",
    "Key of the attribute to persist": "Ключ атрибута, который нужно сохранять",
    # 21
    "Check out this [blog post](https://dt-url.net/ho02y5r) to find out more about the new Dynatrace API token format.": "См. этот [blog post](https://dt-url.net/ho02y5r) с подробностями о новом формате токенов Dynatrace API.",
    "Allow users of this environment to generate personal access tokens based on user permissions. Note that existing personal access tokens will become unusable while this setting is disabled.": "Разрешить пользователям этого окружения генерировать personal access tokens на основе разрешений пользователя. Учтите, что существующие personal access tokens становятся непригодными к использованию, пока эта настройка отключена.",
    # 22
    "Enclose placeholder values in brackets, for example {email}": "Заключайте значения-заполнители в скобки, например {email}",
    # 23
    "Dashboard presets are visible to all users by default. For a pristine environment you may disable them entirely or opt to manually limit visibility to selected user groups.": "Предустановки дашбордов по умолчанию видны всем пользователям. Для чистого окружения их можно полностью отключить или вручную ограничить видимость определёнными группами пользователей.",
    "Show selected preset to respective user group only.": "Показывать выбранную предустановку только соответствующей группе пользователей.",
    "Dashboard preset to limit visibility for": "Предустановка дашборда, для которой ограничивается видимость",
    "User group to show selected dashboard preset to": "Группа пользователей, которой показывается выбранная предустановка дашборда",
    # 24
    "This is applicable only to non-containerized Linux and Windows hosts": "Применимо только к неконтейнеризированным хостам Linux и Windows",
    'Select performance profile for Extension Execution Controller [Documentation](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles")': 'Выберите профиль производительности для Extension Execution Controller [Documentation](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles")',
    # 28
    "A 'bucket' is the length of time your logs will be stored. Select the bucket that's best for you.": "«Бакет»: срок хранения логов. Выберите подходящий бакет.",
    # 29
    "Allow users to grant anonymous access to dashboards. No sign-in will be required to view those dashboards read-only.": "Разрешить пользователям предоставлять анонимный доступ к дашбордам. Для просмотра таких дашбордов в режиме только чтения вход не потребуется.",
    "Configure home dashboard for selected user group. The selected preset dashboard will be loaded as default landing page for this environment.": "Настройте домашний дашборд для выбранной группы пользователей. Выбранная предустановка дашборда будет загружаться как стартовая страница окружения по умолчанию.",
    "Show selected dashboard by default for this user group": "Показывать выбранный дашборд по умолчанию для этой группы пользователей",
    "Preset dashboard to show as default landing page": "Предустановка дашборда для отображения в качестве стартовой страницы по умолчанию",
    # 31 (double-mojibake U+26A0 warning sign preserved verbatim)
    "For details, see [Network zones](https://www.dynatrace.com/support/help/shortlink/network-zones).  â  Warning: You may experience network imbalance if you suddenly disable network zones in an environment that has a high number of OneAgents with network zone configuration. To avoid this and to ensure smooth adoption of network zones, follow best practices for planning and proper naming, as explained in [Network zones](https://www.dynatrace.com/support/help/shortlink/network-zones).": "Подробнее см. [Network zones](https://www.dynatrace.com/support/help/shortlink/network-zones).  â  Внимание: при резком отключении network zones в окружении с большим числом OneAgent, имеющих конфигурацию network zone, возможен сетевой дисбаланс. Чтобы избежать этого и обеспечить плавное внедрение network zones, следуйте практикам по планированию и правильному именованию, описанным в [Network zones](https://www.dynatrace.com/support/help/shortlink/network-zones).",
    # 32
    "**Examples:**  * 84.112.10.5 * fe80::10a1:c6b2:5f68:785d": "**Примеры:**  * 84.112.10.5 * fe80::10a1:c6b2:5f68:785d",
    # 34
    "Disabling this setting disables many deep process visibility features, for example: tracing, profiling, technology-specific metrics (e.g. heap usage), JMX/PMI metrics collection, runtime vulnerability analytics, live debugging, etc. For Fullstack or Infrastructure modes, we only recommend disabling this setting for troubleshooting purposes.  Disabling automatic injection via [oneagentctl](https://dt-url.net/oneagentctl) takes precedence over this setting being enabled and cannot be changed from the Dynatrace web UI.": "Отключение этой настройки отключает многие возможности глубокой видимости процессов, например: трассировку, профилирование, технологически-специфичные метрики (heap usage и т.п.), сбор метрик JMX/PMI, аналитику уязвимостей в рантайме, live-отладку и др. Для режимов Fullstack или Infrastructure отключать эту настройку рекомендуется только для целей траблшутинга.  Отключение автоматического внедрения через [oneagentctl](https://dt-url.net/oneagentctl) имеет приоритет над включением этой настройки и не может быть изменено из веб-интерфейса Dynatrace.",
    "Inject CodeModules in Discovery mode.": "Внедрять CodeModules в режиме Discovery.",
}

# Structural canon (shared with L4-AG.1a.1 / L4-AG.1a.2 / L4-AF).
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
    # Try EN first, then RU. Without this, enum-rows with non-empty EN head
    # leave the head untranslated (eec-local performanceProfile bug, L4-AG.1a.3).
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

# wsmb has a pipe `|` in the technology name «IBM Integration Bus | IBM App Connect
# Enterprise», so split-by-` | ` produces 5 cells instead of 4 and _param_row
# bails out. Whole-line replace handles it. Lesson L4-AG.1a.3.
WHOLE_LINE = {
    "| Monitor IBM Integration Bus | IBM App Connect Enterprise `enabled` | boolean | - | Required |": "| Мониторить IBM Integration Bus | IBM App Connect Enterprise `enabled` | boolean | - | Required |",
}


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
        if line in WHOLE_LINE:
            out.append(WHOLE_LINE[line])
            continue
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
