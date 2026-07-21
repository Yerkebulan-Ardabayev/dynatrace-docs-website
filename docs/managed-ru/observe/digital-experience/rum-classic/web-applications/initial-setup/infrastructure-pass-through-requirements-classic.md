---
title: Требования к сквозному прохождению инфраструктуры для RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/infrastructure-pass-through-requirements-classic
---

# Требования к сквозному прохождению инфраструктуры для RUM Classic

# Требования к сквозному прохождению инфраструктуры для RUM Classic

* Справка
* 9 минут чтения
* Обновлено 01 июня 2026 г.

Real User Monitoring Classic (RUM Classic) работает в рамках HTTP-экосистемы и опирается на набор запросов, заголовков и cookie для сбора и передачи данных о реальных пользователях, а также для их связи с распределёнными трассировками на бэкенде. Чтобы RUM работал как ожидается, инфраструктура, включая брандмауэры, прокси, балансировщики нагрузки, сети доставки контента, веб-серверы и любые другие компоненты на пути запроса, должна пропускать эти запросы, заголовки и cookie без изменений. Кроме того, OneAgent использует заголовки, описанные в разделе [Распространение контекста span и трассировки в Distributed Traces Classic](/managed/observe/application-observability/distributed-traces/context-propagation "Разберитесь, как распространяются контекст span и трассировки в Dynatrace и как их настроить."), для распределённой трассировки, которые также должны проходить через инфраструктуру.

## Веб-приложения

### Запросы

В веб-приложениях JavaScript RUM либо [внедряется автоматически](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection "Настройка автоматического внедрения JavaScript RUM на страницы приложений"), либо [вставляется вручную](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройка мониторинга без агента для веб-приложений.") на веб-страницы. Код мониторинга RUM загружается как внешний файл, если только не используется [встроенный код в формате snippet](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/snippet-formats#inline-code "Выбор формата фрагмента JavaScript RUM, наиболее подходящего для конкретного случая использования"), но даже в этом случае код мониторинга Session Replay загружается отдельным файлом. После активации JavaScript RUM начинает отправлять beacon-запросы для передачи собранных данных RUM.

Чтобы RUM работал в полном объёме, через инфраструктуру должны проходить как запросы кода мониторинга RUM, так и RUM-маячки (beacons).

#### Запросы кода мониторинга RUM

* Для мониторинга без агента запросы отправляются в CDN или Cluster ActiveGate, настроенный согласно разделу [Настройка мониторинга без агента Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройка мониторинга без агента для веб-приложений.").
* При автоматическом внедрении запросы по умолчанию отправляются на веб- или прикладной сервер, на котором размещено приложение, а путь URL содержит строку `ruxitagentjs_`.

Подробнее о URL по умолчанию и доступных параметрах настройки см. в разделе [Настройка источника кода Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-monitoring-code-source "Настройка источника кода Real User Monitoring Classic под конкретные требования.").

#### RUM-маячки (beacons)

RUM-маячки передают данные, собранные JavaScript RUM, обратно на [конечную точку маячка](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Изменение URL конечной точки маячка по умолчанию и отправка RUM-маячков в инфраструктуру Dynatrace или на другой инструментированный веб-сервер."), это beacon endpoint.

* Для мониторинга без агента маячки по умолчанию отправляются на конечную точку маячка с путём URL `/bf/<id>`, входящую в состав Cluster ActiveGate.
* При автоматическом внедрении маячки по умолчанию отправляются на веб- или прикладной сервер, на котором размещено приложение, а путь URL заканчивается на `/rb_<id>`.
* URL маячка включает строку запроса, которую нельзя изменять, это касается изменения, удаления или изменения порядка параметров.
* Тело запроса `POST` содержит полезную нагрузку, отправляемую с типом содержимого `text/plain`. Для Session Replay также может использоваться тип содержимого `application/octet-stream`.
* Для Session Replay запросам `POST` может предшествовать [предварительный запрос CORS﻿](https://developer.mozilla.org/en-US/docs/Glossary/Preflight_request), это запросы `OPTIONS`.

Доступные параметры настройки конечной точки маячка см. в разделе [Настройка конечной точки маячка для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Изменение URL конечной точки маячка по умолчанию и отправка RUM-маячков в инфраструктуру Dynatrace или на другой инструментированный веб-сервер.").

### Заголовки

RUM использует следующие HTTP-заголовки, все они должны свободно проходить через инфраструктуру.

#### Пользовательские заголовки запроса

| Заголовок | Назначение |
| --- | --- |
| `x-dtc` | Устанавливается RUM JavaScript при настройке согласно [Link cross-origin XHR user actions and their distributed traces in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/link-cross-origin-xhrs#x-dtc-header "Enable the correlation between cross-origin XHR actions and distributed traces."), для передачи информации, необходимой для сопоставления кросс-доменных XHR. |
| `x-dtpc` | Устанавливается RUM JavaScript для передачи ID, необходимых для маршрутизации RUM beacon, агрегации пользовательских сессий и корреляции RUM. |
| `x-dtreferer` | Устанавливается RUM JavaScript, когда инструментированное приложение изменяет стандартный заголовок `Referer` во время пользовательского действия, чтобы сохранить исходный referer для корреляции RUM. |
| `x-dynatrace-application` | Устанавливается OneAgent на первом инструментированном серверном уровне (ближайшем к браузеру) для передачи контекста нижестоящим OneAgent, таким как [detected application ID](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."), [cookie domain](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-cookie-attributes#cookie-domain "Learn which RUM cookie attributes you can configure and how.") и любое применимое [custom injection rule](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#custom-injection-rule "Configure automatic injection of the RUM JavaScript into the pages of your applications"). |
| `x-dynatrace-origin-url` | OneAgent версий до 1.167. Устаревший заголовок, устанавливаемый на первом инструментированном серверном уровне (ближайшем к браузеру), чтобы сохранить исходный URL запроса на случай переписывания URL. |
| `X-ruxit-Disposition` | Устанавливается OneAgent, чтобы предотвратить перехват распределённых трасс для RUM beacon модулем кода .NET. |

#### Стандартные заголовки запроса

| Заголовок | Назначение |
| --- | --- |
| [`Accept-Encoding`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Accept-Encoding) | Читается OneAgent, чтобы определить, нужно ли сжимать RUM JavaScript перед доставкой. |
| [`Cookie`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cookie) | Устанавливается или изменяется OneAgent на первом инструментированном серверном уровне (ближайшем к браузеру), если `dtCookie` ещё не установлен, для передачи значения cookie нижестоящим OneAgent. После активации RUM в браузере браузер также добавляет в этот заголовок cookie, установленные RUM JavaScript. Подробности обо всех RUM cookie см. в разделе [Cookies](#cookies-web). |
| [`If-Match`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Match) [`If-Modified-Since`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Modified-Since) [`If-None-Match`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-None-Match) [`If-Unmodified-Since`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/If-Unmodified-Since) | Изменяются OneAgent, когда активны [cache control header optimizations](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications"). |
| [`Referer`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Referer) | Устанавливается браузером. Захватывается OneAgent и [beacon endpoint](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") на Cluster ActiveGate для корреляции RUM. |
| [`User-Agent`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/User-Agent) | Устанавливается браузером. Читается OneAgent для оценки [browser exclusion rules](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/exclude-browsers-robots-and-spiders-from-monitoring#exclude-browsers "Disable Real User Monitoring Classic for certain IP addresses, browsers, bots, and spiders."), а также захватывается [beacon endpoints](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") для [browser and OS detection](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems."). Установка значения `dtHealthCheck` запускает [проверку работоспособности RUM OneAgent﻿](https://dt-url.net/qg037fw). |

#### Пользовательские заголовки ответа

| Заголовок | Назначение |
| --- | --- |
| `x-dtAgentId` | Устанавливается OneAgent, когда активна его [проверка работоспособности RUM﻿](https://dt-url.net/qg037fw), передавая ID модулей кода OneAgent, участвовавших в обработке запроса. |
| `x-dtHealthCheck` | Устанавливается OneAgent, когда активна его [проверка работоспособности RUM﻿](https://dt-url.net/qg037fw), передавая результаты проверки. |
| `X-OneAgent-JS-Injection` `X-ruxit-JS-Agent` | Устанавливается OneAgent, чтобы указать, что он начал внедрение RUM JavaScript, предотвращая повторное внедрение. |

#### Стандартные заголовки ответа

| Заголовок | Назначение |
| --- | --- |
| [`Access-Control-Allow-Headers`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Headers) [`Access-Control-Allow-Methods`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Methods) [`Access-Control-Max-Age`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Max-Age) | Устанавливается [beacon endpoints](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") для ответов на [запросы `OPTIONS`](#beacons-web). |
| [`Access-Control-Allow-Origin`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Access-Control-Allow-Origin) | Устанавливается [beacon endpoints](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") для ответов на [RUM beacons](#beacons-web). Чтобы контролировать, от каких источников принимаются beacons, нужно настроить [список разрешённых источников beacon](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted."). Также устанавливается для ответов на [запросы кода мониторинга RUM](#requests-monitoring-code), когда они обрабатываются через CDN Dynatrace. |
| [`Cache-Control`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) | Устанавливается для ответов на [RUM beacons и запросы кода мониторинга RUM](#requests-web). |
| [`Content-Encoding`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Encoding) | Устанавливается для ответов на [запросы кода мониторинга RUM](#requests-monitoring-code); также считывается при инъекции HTML. |
| [`Content-Length`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Length) | Изменяется при инъекции HTML и устанавливается для ответов на [RUM beacons и запросы кода мониторинга RUM](#requests-web). |
| [`Content-Type`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) | Устанавливается для ответов на [RUM beacons и запросы кода мониторинга RUM](#requests-web), а также считывается при инъекции HTML. |
| [`ETag`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/ETag) | Когда активны [оптимизации заголовка cache control](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications"), OneAgent добавляет суффикс к исходному значению заголовка. Заголовок может быть установлен OneAgent, если приложение этого не делает. |
| [`Expires`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Expires) | Устанавливается для ответов на [запросы кода мониторинга RUM](#requests-monitoring-code), когда они обрабатываются через CDN Dynatrace. |
| [`Last-Modified`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Last-Modified) | Когда активны [оптимизации заголовка cache control](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#cache-header-optimization "Configure automatic injection of the RUM JavaScript into the pages of your applications"), OneAgent вычитает 1 секунду из исходного значения заголовка. Этот заголовок также устанавливается для ответов на [запросы кода мониторинга RUM](#requests-monitoring-code). |
| [`Server-Timing`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Server-Timing) | Устанавливается OneAgent для передачи информации, важной для корреляции RUM. |
| [`Set-Cookie`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Set-Cookie) | Устанавливается OneAgent для размещения [`dtCookie`](#cookies-web). |
| [`Strict-Transport-Security`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) | Устанавливается [beacon endpoint](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.") на Cluster ActiveGate. |
| [`Timing-Allow-Origin`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Timing-Allow-Origin) | Устанавливается OneAgent, чтобы разрешить RUM JavaScript доступ к содержимому заголовка `Server-Timing` в кросс-доменных сценариях. Также устанавливается для ответов на [запросы кода мониторинга RUM](#requests-monitoring-code), когда они обрабатываются через CDN Dynatrace. |
| [`Transfer-Encoding`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Transfer-Encoding) | Считывается OneAgent при инъекции HTML. |
| [`Vary`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Vary) | Устанавливается для ответов на [RUM beacons и запросы кода мониторинга RUM](#requests-web). |

### Cookies

RUM использует следующие cookies. Все они должны иметь возможность достигать Dynatrace. Подробнее о том, как Dynatrace использует cookies, и с пояснением `<suffix>`, используемого в таблице, см. [Cookies и хранилище на стороне клиента для RUM и Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Узнайте, как Dynatrace RUM и Session Replay используют cookies, веб-хранилище и IndexedDB.").

| Cookie | Максимальный размер | Назначение |
| --- | --- | --- |
| `dtCookie<suffix>` | Ограничение не задано, но обычно менее 100 Б | Отслеживает визит через несколько запросов. |
| `dtPC<suffix>` | 58 Б | Требуется для маршрутизации RUM-биконов, включает session ID для агрегации пользовательских сессий. |
| `dtSa<suffix>` | Максимальная длина URL | Служит промежуточным хранилищем для действий, охватывающих несколько страниц. |
| `dtValidationCookie<suffix>` | Длина строки `dTValidationCookieValue`, то есть `23` | Используется для определения домена верхнего уровня. |
| `rxVisitor<suffix>` | 45 Б | Содержит ID посетителя для сопоставления сессий. |
| `rxvt<suffix>` | 27 Б | Хранит таймаут сессии. |
| `dtsrVID<suffix>`[1](#fn-1-1-def) | 20 Б | Указывает ID текущего записываемого просмотра. |
| `dtSR<suffix>`[2](#fn-1-2-def) | 81 Б | Если Session Replay включён, хранит значения, необходимые для согласованности записи между страницами. |

1

Cookie `dtsrVID` существует начиная с версии RUM JavaScript 1.325+ до версии RUM JavaScript 1.333.

2

Опциональный cookie `dtSR` доступен начиная с версии RUM JavaScript 1.335+.

## Мобильные приложения

### Запросы

OneAgent for Mobile отправляет beacon-запросы для передачи собранных данных RUM. Путь URL бикона зависит от настроенной конечной точки бикона:

* Если биконы обрабатываются ActiveGate, путь URL это `/mbeacon`.
* Если биконы [обрабатываются OneAgent, инструментирующим веб- или сервер приложения](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/oneagent-as-beacon-forwarder-mobile "Используйте Dynatrace OneAgent в качестве конечной точки бикона для мобильных приложений."), путь URL это `/dtmb`.

Помимо `POST`-запросов, передающих собранные данные, OneAgent for Mobile также отправляет `GET`-запросы на конечную точку бикона для получения обновлений конфигурации. Ответы бикона имеют тип содержимого `text/plain`.

URL бикона включает строку запроса, которую нельзя изменять, это касается изменения, удаления или изменения порядка параметров.

### Заголовки

В мобильных приложениях используются следующие HTTP-заголовки, все из которых должны иметь возможность беспрепятственно проходить через инфраструктуру.

#### Заголовки запроса

| Заголовок | Назначение |
| --- | --- |
| `x-dtc` | Устанавливается при использовании [Cordova Plugin](/managed/observe/digital-experience/rum-classic/mobile-applications/cross-platform-frameworks/apache-cordova "Настройте Dynatrace для мониторинга гибридных мобильных приложений с помощью плагина Cordova.") и ручного инструментирования [native web requests﻿](https://www.npmjs.com/package/@dynatrace/cordova-plugin#native-webrequests). Связывает native web requests с их серверными распределёнными трассировками. |
| `x-dynatrace` | Устанавливается OneAgent for Mobile для связывания мобильной части веб-запроса с серверной распределённой трассировкой. |

#### Заголовки ответа

| Заголовок | Назначение |
| --- | --- |
| [`Cache-Control`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Cache-Control) [`Content-Length`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Length) [`Content-Type`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Content-Type) | Устанавливаются для ответов на [RUM-биконы](#requests-mobile). |
| [`Strict-Transport-Security`﻿](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Strict-Transport-Security) | Устанавливается конечной точкой бикона ActiveGate для ответов на [RUM-биконы](#requests-mobile). |

### Cookies

Следующие cookies используются для гибридных приложений, сочетающих OneAgent for Mobile с RUM JavaScript. Они должны проходить через инфраструктуру без изменений.

| Cookie | Максимальный размер | Назначение |
| --- | --- | --- |
| `dtAdk` | 92 Б | Объединяет сессии, зафиксированные OneAgent for Mobile и RUM JavaScript. |
| `dtAdkSettings` | 36 Б | Передаёт настройки между OneAgent for Mobile и RUM JavaScript. |