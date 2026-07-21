---
title: Персональные данные, собираемые Dynatrace
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace
---

# Персональные данные, собираемые Dynatrace

# Персональные данные, собираемые Dynatrace

* 12 мин чтения
* Обновлено 05 марта 2026

Из отслеживаемых сред Dynatrace может собирать данные конечных пользователей, потенциально включая персональную и конфиденциальную информацию о них.

На этой странице описано, где могут собираться персональные данные и как можно ограничить их сбор, хранение и отображение, чтобы соблюсти требования законодательства о конфиденциальности, включая California Consumer Privacy Act (CCPA; Калифорния, США), General Data Protection Regulation (GDPR; Европейский союз) или Lei Geral de ProteÃ§Ã£o de Dados (LGPD; Бразилия).

Dynatrace маскирует данные согласно [трём уровням защиты данных](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection."): **при сборе**, **при хранении** и **при отображении**. В следующих разделах значки показывают уровень маскирования, применяемого к каждому типу данных, которые собирает Dynatrace.

|  |  |
| --- | --- |
| Собирается по умолчанию | Собирается по умолчанию |
| Не собирается по умолчанию | Не собирается по умолчанию |
| Маскируется | Маскируется |
| Не маскируется | Не маскируется |
| Настройки маскирования можно сконфигурировать; по умолчанию маскируется | Настройки маскирования можно сконфигурировать; по умолчанию маскируется |
| Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется |
| Маскирование зависит от конфигурации, заданной при сборе и хранении | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| Настройки маскирования задаются согласно разрешению конечного пользователя | Настройки маскирования задаются согласно разрешению конечного пользователя |

## Мониторинг сервисных запросов

Dynatrace собирает наиболее важные данные входящих запросов, а также веб-запросов конечных пользователей приложения (то есть сервисных запросов). URL, IP-адреса клиентов и определённые поля HTTP-заголовков собираются автоматически.

Можно [настроить глобальные параметры конфиденциальности](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), чтобы маскировать IP-адреса клиентов, URI и параметры HTTP post.

| Тип данных | По умолчанию | Маскирование при сборе | Маскирование при хранении | Маскирование при отображении |
| --- | --- | --- | --- | --- |
| IP-адреса клиентов[1](#fn-1-1-def) | Собирается по умолчанию | Настройки маскирования можно сконфигурировать; по умолчанию маскируется | Настройки маскирования можно сконфигурировать; по умолчанию маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |
| URI[2](#fn-1-2-def) | Собирается по умолчанию | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| HTTP-заголовки[2](#fn-1-2-def), [3](#fn-1-3-def) | Собирается по умолчанию | Не маскируется | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |
| Параметры HTTP post[2](#fn-1-2-def) | Не собирается по умолчанию | Не маскируется | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |
| Параметры запроса URL[2](#fn-1-2-def), [4](#fn-1-4-def) | Собирается по умолчанию | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| Сообщения исключений[2](#fn-1-2-def), [5](#fn-1-5-def) | Собирается по умолчанию | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования можно сконфигурировать; по умолчанию не маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |
| Литералы SQL[6](#fn-1-6-def) | Собирается по умолчанию | Маскируется | Маскируется | Маскируется |
| Связанные переменные SQL (bind variables)[7](#fn-1-7-def) | Не собирается по умолчанию | Не маскируется | Не маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |
| Аргументы методов / возвращаемые значения[8](#fn-1-8-def) | Не собирается по умолчанию | Не маскируется | Не маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |

1

Настроить маскирование можно через опцию [**Mask end-user IP addresses and GPS coordinates**](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") в параметрах конфиденциальности данных.

2

Маскирование при сборе настраивается через опцию [**OneAgent-side masking**](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#oneagent-side-masking "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."), а маскирование при хранении, через опцию [**Mask personal data in URIs**](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-uris "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") в параметрах конфиденциальности данных.

3

Автоматически собираются только определённые заголовки. Остальные заголовки можно собирать через [атрибуты запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

4

Параметры запроса всегда маскируются при отображении, а также могут маскироваться при хранении. Чтобы собирать параметры явно, настройте [атрибуты запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

5

Чтобы избежать сбора определённых исключений, перейдите в **Settings** > **Server-side service monitoring** > **Deep monitoring**, разверните раздел **Exclude noisy and unnecessary exceptions** и добавьте нужные правила исключения.

6

Литералы, являющиеся частью условия `WHERE` в SQL-выражении, заменяются на `*****`, например, `WHERE userId = '*********'`.

7

Поддержка связанных переменных [зависит от развёртывания и лицензии](/managed/observe/infrastructure-observability/database-services-classic/support-for-sql-bind-variables#availability "Learn how you can enable Dynatrace OneAgent to capture the values of bind variables."). Подробнее о том, как начать собирать значения связанных переменных SQL, см. [Support for SQL bind variables](/managed/observe/infrastructure-observability/database-services-classic/support-for-sql-bind-variables "Learn how you can enable Dynatrace OneAgent to capture the values of bind variables."). Значения связанных переменных SQL заменяются на `*****`. Просматривать немаскированные значения связанных переменных в рамках сущности или зоны управления могут только пользователи, имеющие право просматривать эту сущность или зону управления.

8

Настраивается через [атрибуты запроса](/managed/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.").

## Атрибуты OpenTelemetry для распределённой трассировки

Dynatrace автоматически собирает все [атрибуты](/managed/ingest-from/opentelemetry#attribute "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") OpenTracing и OpenTelemetry, но сохраняет только те атрибуты, которые не заблокированы. См. [Enable the OpenTelemetry Span Sensor for OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

| Тип данных | По умолчанию | Маскирование при сборе | Маскирование при хранении | Маскирование при отображении |
| --- | --- | --- | --- | --- |
| Незаблокированные атрибуты | Собирается по умолчанию | Не маскируется | Не маскируется | Настройки маскирования задаются согласно разрешению конечного пользователя |

## Real User Monitoring (RUM)

С помощью [Dynatrace Real User Monitoring](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.") можно лучше понимать своих клиентов, получая доступ к анализу производительности в реальном времени. Сюда входят все выполненные пользовательские действия и то, как они влияют на производительность.

Чтобы обеспечить анализ производительности на основе географических регионов, Dynatrace собирает IP-адреса и GPS-координаты, которые по умолчанию маскируются. Чтобы маскировать пользовательские действия и URI, [настройте глобальные параметры конфиденциальности](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names."). Dynatrace также может определять возвращающихся пользователей, сохраняя случайно сгенерированный ID (тег пользователя) в браузере или на устройстве каждого пользователя; такой тип тегирования пользователей по умолчанию не включён.

| Тип данных | По умолчанию | Маскирование при сборе | Маскирование при хранении | Маскирование при отображении |
| --- | --- | --- | --- | --- |
| [Пользовательские действия](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")[1](#fn-2-1-def) | Собираются по умолчанию | Настройки маскирования можно настроить; по умолчанию не маскируются | Маскирование зависит от конфигурации, заданной при сборе и хранении | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| [IP-адреса и GPS-координаты](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")[2](#fn-2-2-def), [3](#fn-2-3-def) | Собираются по умолчанию[4](#fn-2-4-def) | Настройки маскирования можно настроить; по умолчанию маскируются | Настройки маскирования можно настроить; по умолчанию маскируются | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| URI[3](#fn-2-3-def), [5](#fn-2-5-def) | Собираются по умолчанию | Не маскируются | Настройки маскирования можно настроить; по умолчанию не маскируются | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| [Теги пользователей](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.")[6](#fn-2-6-def) | По умолчанию не собираются | Маскируются | Маскирование зависит от конфигурации, заданной при сборе и хранении | Маскирование зависит от конфигурации, заданной при сборе и хранении |
| Свойства сессии и действия[7](#fn-2-7-def) | По умолчанию не собираются | Маскируются | Маскирование зависит от конфигурации, заданной при сборе и хранении | Маскирование зависит от конфигурации, заданной при сборе и хранении |

1

Пользовательские действия содержат имя, набор временных характеристик и [метаданные](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions#add-and-use-placeholders "Customize automatically generated user action names for your web applications.").  
Веб-приложения Настройте маскирование через опцию [**Mask user actions (web applications only)**](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-user-actions "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") в настройках конфиденциальности данных. Также можно [создавать пользовательские имена пользовательских действий](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.").  
Мобильные приложения Настройте маскирование через специальное [свойство маскирования](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#user-action-masking "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region.") или задайте правила именования и извлечения действий (настройки мобильного приложения > **Naming rules**).

2

Настройте маскирование через опцию [**Mask end-user IP addresses and GPS coordinates**](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-ip-and-gps "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") в настройках конфиденциальности данных.

3

Dynatrace ищет персональные данные, такие как IP-адреса, UUID, номера платёжных карт, адреса электронной почты и другие идентифицируемые ID. Однако могут существовать другие персональные данные или отдельные символы, которые Dynatrace не может определить автоматически. Чтобы маскировать URL при отображении, используйте [пользовательские имена для пользовательских действий](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications."), группировку и именование ресурсов.

4

По умолчанию [сбор данных о местоположении](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/instrumentation/ios-auto-instrumentation-features#location "Explore the list of features that are available after you instrument your application with OneAgent.") для мобильных приложений отключён.

5

Настройте маскирование через опцию [**Mask personal data in URIs**](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#mask-uris "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.") в настройках конфиденциальности данных.

6

Веб-приложения Можно [настроить тегирование пользователей](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/identify-individual-users-for-session-analysis "Tag individual users via the JavaScript API for session analysis.") с помощью либо RUM JavaScript API, либо метаданных страницы приложения.  
Мобильные приложения Используйте вариант метода "тегирования пользователей" для добавления тега пользователя к сессии; подробнее см. [соответствующую документацию](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#user-tagging "Learn about user and error events and the types of user and error events captured by Dynatrace.").

7

Свойства сессии и действия для [веб](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications."), [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/define-mobile-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/define-custom-action-and-session-properties "Send metadata to Dynatrace and define action and session properties for your monitored custom applications.") должны быть явно определены и содержат то, чем их снабдили выбранные базовые источники данных.

Также можно использовать следующие настройки для контроля того, как собираются персональные данные при включённом RUM для приложений.

* [Режим Opt-in](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#user-opt-in-mode-gdpr "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [Do Not Track](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#do-not-track-gdpr "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")
* [Отслеживание пользователей](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings#user-tracking "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.")

## Log Monitoring

Log Monitoring, это опциональная функция, которая по умолчанию включена. С её помощью можно напрямую получать доступ к содержимому логов всех критически важных процессов системы, искать конкретные сообщения логов и хранить все логи централизованно.

Файлы логов могут содержать имена пользователей, адреса электронной почты, параметры URL и другую информацию, которую нежелательно раскрывать. По умолчанию ничего не маскируется, но Log Monitoring предлагает возможность [маскировать конфиденциальную информацию](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") в логах. Правила маскирования задаются самостоятельно, поэтому любые данные можно заменить на SHA-1-хеш или фиксированную фразу, например, `*****`, `#######`, `MASKED` или `Last name`.

| Тип данных | Маскирование при обработке логов Dynatrace | Маскирование при конфигурации OneAgent |
| --- | --- | --- |
| Содержимое файла логов | Настройки маскирования можно настроить; по умолчанию не маскируется | Настройки маскирования можно настроить; по умолчанию не маскируется |

## Session Replay

Session Replay, это опциональная функция, которая по умолчанию отключена. Можно включить [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers."), чтобы фиксировать и визуально воспроизводить полные цифровые взаимодействия пользователей с приложением.

* Для веб-приложений Session Replay фиксирует весь исходный код HTML и мутации, возникающие в результате действий пользователя. Также фиксируются все пользовательские взаимодействия, полученные через поля форм, атрибуты, контент и такие действия, как движение мыши и прокрутка.
* Для мобильных приложений Session Replay доступен только для тех сессий, которые заканчиваются сбоем. Чтобы визуально воссоздать опыт конечного пользователя с приложением перед сбоем, Session Replay фиксирует скриншоты и события из отслеживаемого приложения.

| Тип данных | Маскирование при захвате | Маскирование при хранении | Маскирование при отображении |
| --- | --- | --- | --- |
| Поля форм с паролями | Маскируются | Маскируются | Маскируются |
| Пользовательский ввод[1](#fn-3-1-def)  Текст[1](#fn-3-1-def)  Изображения[1](#fn-3-1-def), [2](#fn-3-2-def)  Атрибуты[1](#fn-3-1-def) | Настройки маскирования можно конфигурировать; по умолчанию маскируются | Маскирование зависит от конфигурации, заданной при захвате и хранении | Маскирование зависит от конфигурации, заданной при захвате и хранении |
| Взаимодействия[3](#fn-3-3-def) | Настройки маскирования можно конфигурировать; по умолчанию не маскируются | Маскирование зависит от конфигурации, заданной при захвате и хранении | Маскирование зависит от конфигурации, заданной при захвате и хранении |

1

Веб-приложения Настраивается в [настройках маскирования приложения](/managed/observe/digital-experience/session-replay/configure-session-replay-web#mask-data-via-ui "Configure monitoring consumption and data privacy settings for Session Replay Classic.") или добавлением атрибута [`data-dtrum-mask`](/managed/observe/digital-experience/session-replay/configure-session-replay-web#mask-data-via-code "Configure monitoring consumption and data privacy settings for Session Replay Classic.") к нужному элементу в коде приложения. Подробнее см. [Настройка Session Replay | Маскирование](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-masking "Configure monitoring consumption and data privacy settings for Session Replay Classic."). Пользовательский ввод и текст заменяются на `***` или `000`. Заменяются только буквенно-цифровые символы, форматирующие символы, такие как точки, запятые и двоеточия, не маскируются. Значения атрибутов заменяются на `***`. Изображения заменяются на изображение-заполнитель.  
Мобильные приложения Настраивается в коде приложения для [iOS](/managed/observe/digital-experience/session-replay/session-replay-ios#mask-sensitive-data "Prerequisites and the procedure for enabling Session Replay Classic for your iOS apps.") и [Android](/managed/observe/digital-experience/session-replay/session-replay-android#mask-sensitive-data "Set up Session Replay Classic for your Android apps to learn which actions your users perform."). Пользовательский ввод и текст заменяются на `*****` на временной шкале Session Replay и на чёрные прямоугольники на скриншотах. Маскируются все символы. Изображения заменяются на чёрный прямоугольник.

2

За исключением фоновых изображений или изображений, заданных через CSS.

3

Веб-приложения Настраивается с помощью опции **Block list** в [настройках маскирования приложения](/managed/observe/digital-experience/session-replay/configure-session-replay-web#mask-data-via-ui "Configure monitoring consumption and data privacy settings for Session Replay Classic.").  
Мобильные приложения Маскирование взаимодействий невозможно.

Также можно использовать следующие настройки, чтобы управлять тем, как персональные данные захватываются при включённом Session Replay для веб- и мобильных приложений.

| Тип приложения | Название опции | Описание | По умолчанию |
| --- | --- | --- | --- |
| Web | [Режим opt-in для Session Replay](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-opt-in-mode "Configure monitoring consumption and data privacy settings for Session Replay Classic.") | Используется для записи определённой части сессии или для реализации разрешения конечного пользователя на запись сессии. Когда этот режим включён, Session Replay отключён до вызова метода [`dtrum.enableSessionReplay(ignoreCostControl: boolean)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablesessionreplay). | Отключено |
| Mobile | [Режим Opt-in](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-rum-privacy-mobile#opt-in-mode-mobile "Leverage privacy settings that Dynatrace provides to ensure that your mobile apps comply with the data-privacy regulations of your region."): разрешение на запись повторов сбоев | Используется для реализации разрешения конечного пользователя на запись сессии. Если пользователь разрешил записывать повторы сбоев через Session Replay при сбоях:  iOS: установить `privacyConfig.crashReplayOptedIn` в значение `true`/`YES`.  Android: установить `.withCrashReplayOptedIn` в значение `true`. Экран с запросом разрешения на запись сессии Session Replay, режим opt-in Session Replay для мобильных приложений  Session Replay, режим opt-in Session Replay для мобильных приложений | - |
| Web | [Исключение URL](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-url-exclusion "Configure monitoring consumption and data privacy settings for Session Replay Classic.") | Используется для исключения определённых страниц из записи сессий. | - |
| Web | [Do Not Track](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr#do-not-track-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") | Включить эту функцию, если нужно соблюдать настройку «Do Not Track», которую пользователи могут включить в своих браузерах.При выборе **Turn Real User Monitoring off for "Do Not Track"-enabled browsers** Session Replay отключается, когда в браузере пользователя обнаружена настройка «Do Not Track». | Соблюдать настройки браузера «Do Not Track» - фиксировать анонимные пользовательские сессии для браузеров с включённым «Do Not Track» |
| Web  Mobile | [Разрешения пользователей](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-permissions "Configure monitoring consumption and data privacy settings for Session Replay Classic.")  [Management zones](/managed/observe/digital-experience/session-replay/configure-session-replay-web#sr-management-zones "Configure monitoring consumption and data privacy settings for Session Replay Classic.") | Используются разрешения **Replay sessions with masking** и **Replay sessions without masking**, чтобы управлять тем, у кого есть доступ к записям сессий с маскированием и без него. | Разрешение **Replay sessions with masking** включено для всех пользователей |

## Диагностика OneAgent

[Диагностика OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics"), это опциональная функция, которая позволяет собирать и анализировать архивы поддержки на предмет аномалий.

Архивы поддержки создаются Dynatrace OneAgent и содержат лог- и конфигурационные файлы OneAgent, а также специфические данные с отслеживаемых хостов и процессов, например имена процессов и идентификационные номера. Лог-файлы OneAgent могут содержать персональные данные, например как часть трассировки стека.

Для соблюдения региональных норм защиты данных и конфиденциальности Dynatrace выполняет следующее:

* Маскирует некоторые персональные данные перед сохранением архива поддержки в Cassandra и загрузкой его в S3-бакет AWS. Например, IBAN и учётные данные URI заменяются на `<masked>`. Однако некоторые персональные данные могут не маскироваться.
* Записывает сообщения журнала аудита при создании, анализе, доступе и удалении архивов поддержки, чтобы обеспечить прозрачность использования архивов поддержки.
* Предоставляет доступ к архивам поддержки OneAgent только пользователям, у которых есть [разрешение окружения](/managed/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") **View sensitive request data**.
* Автоматически удаляет все диагностические данные через 30 дней после их сбора. Этот [период хранения данных](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.") можно настроить.

  Это относится к данным в кластере Dynatrace. Также можно удалить собранные диагностические данные раньше.

| Тип данных | Маскирование при захвате | Маскирование при хранении | Маскирование при отображении |
| --- | --- | --- | --- |
| Лог- и конфигурационные файлы OneAgent | Не маскируются | Маскируются | Маскируются |

## Совместное использование логов

Функция API `shareLogsFile` позволяет делиться локально сохранёнными лог-файлами через панель обмена iOS (`UIActivityViewController`). Для этой функции требуется, чтобы флаг [`DTXWriteLogsToFile`](/managed/observe/digital-experience/rum-classic/mobile-applications/instrument-ios-app/customization/ios-configuration-keys#privacy-and-security "With configuration keys, you can fine-tune the auto-instrumentation of your iOS apps.") был установлен в значение `true`.

Эта функция позволяет делиться логами напрямую с устройства без необходимости доступа к Xcode для извлечения логов. Она не предназначена для использования в продуктивных приложениях.

Функция API `shareLogsFile` недоступна на tvOS.

## Live Debugger

Live Debugger, это опциональная функция. Чтобы сделать её доступной, включи [Live Debugger](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") на своих OneAgent. Live Debugger можно использовать для отладки сервисов и приложений в любом окружении в режиме реального времени без остановки приложений.

Live Debugger собирает снимки (snapshots), которые могут включать значения переменных, обрабатываемых приложением. Можно [задать правила маскирования](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), чтобы любые данные заменялись хешем SHA-1 или фиксированной фразой, например, `*****`, `#######`, `MASKED` или `Last name`. Маскирование выполняется агентом на сервере, поэтому конфиденциальные данные не покидают сервер или сеть.