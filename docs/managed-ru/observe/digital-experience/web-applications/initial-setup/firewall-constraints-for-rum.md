---
title: Ограничения брандмауэра для RUM
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/firewall-constraints-for-rum
scraped: 2026-05-12T11:34:25.111512
---

# Ограничения брандмауэра для RUM

# Ограничения брандмауэра для RUM

* Reference
* 9-min read
* Updated on Apr 22, 2026

Real User Monitoring (RUM) использует HTTP-технологии для отправки данных производительности из браузеров конечных пользователей в Dynatrace. Для этого [RUM JavaScript инжектируется](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") в веб-страницы приложения. Этот [тег или фрагмент кода](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") взаимодействует с Dynatrace. Однако необходимо убедиться, что конфигурация брандмауэров, прокси и веб-серверов разрешает прохождение всех необходимых данных.

## Запросы

Для полноценной работы RUM через инфраструктуру должны проходить следующие HTTP-запросы:

* Запросы на код мониторинга RUM.

  + При агентлесс-мониторинге эти запросы отправляются на CDN или Cluster ActiveGate, настроенный согласно разделу [Настройка агентлесс Real User Monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.").
  + При автоматической инжекции они по умолчанию отправляются на веб-сервер или сервер приложений, размещающий приложение, и их URL-путь содержит строку `ruxitagentjs_`.

  Подробнее о URL по умолчанию и доступных параметрах настройки см. в разделе [Настройка источника кода мониторинга RUM](/managed/observe/digital-experience/web-applications/additional-configuration/configure-monitoring-code-source "Configure the Real User Monitoring code source for your specific requirements.").
* RUM-маяки, отправляющие данные, захваченные RUM JavaScript, обратно в Dynatrace.

  + При агентлесс-мониторинге маяки по умолчанию отправляются на конечную точку маяка в составе Cluster ActiveGate. URL-путь — `/bf` или `/bf/<id>`.
  + При автоматической инжекции маяки по умолчанию отправляются на веб-сервер или сервер приложений, размещающий приложение, и URL-путь заканчивается на `/rb_<id>`.
  + URL маяка содержит параметры запроса. Убедитесь, что брандмауэр не удаляет параметры запроса.
  + Тело `POST`-запроса содержит полезные данные. Полезные данные отправляются с типом содержимого `text/plain`. Для Session Replay также может использоваться тип `application/octet-stream`.

  Доступные параметры настройки конечной точки маяка см. в разделе [Настройка конечной точки маяка для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/beacon-endpoint "Change the default beacon endpoint URL and send RUM beacons to Dynatrace infrastructure or another instrumented web server.").

## Заголовки

RUM использует следующие HTTP-заголовки. Все они должны иметь возможность достигать Dynatrace.

### Заголовки запроса

| Заголовок | Назначение |
| --- | --- |
| `x-dynatrace` | Используется для сшивки транзакций в HTTP-заголовках. Устанавливается OneAgent для связи веб-серверов. Убедитесь, что сетевые компоненты (брандмауэры и маршрутизаторы) никогда не настроены на удаление этих заголовков. Некоторые сетевые компоненты отклоняют такие запросы с ошибкой `403` HTTP, поэтому необходимо настроить их для принятия заголовка `x-dynatrace`. |
| `x-dynatrace-application` | Содержит идентификатор RUM-приложения, домен cookie и правило инжекции (`noop`, `auto`, `before` или `after`). Используется при наличии прокси между браузером и исходным процессом, доставляющим страницу. |
| `x-dynatrace-origin-url` | Сохраняет исходный URL запроса при перезаписи URL. |
| `X-dynaTrace-RequestState` | Отслеживает глубину дерева подпутей для предотвращения бесконечных распределённых трассировок. |
| `x-dtpc` | Определяет правильные конечные точки для передачи маяков; содержит идентификатор сессии для корреляции. |
| `x-dtreferer` | Содержит реферер страницы для действия и улучшает результаты корреляции. |
| `x-dtc` | Содержит информацию для корреляции XHR-вызовов между разными источниками. |
| `Cookie` | Устанавливает cookie `dtCookie`, если HTTP-запрос его не содержит. |
| `X-Ruxit-Forwarded-For` | Используется для отслеживания прокси-сценариев кодовым модулем NGINX. |
| `X-ruxit-Apache-ServerNamePorts` | Используется кодовым модулем Apache для синхронизации именования сервисов с кодовым модулем PHP. |
| `X-ruxit-Disposition` | Используется кодовым модулем IIS для упрощения подпутей кодового модуля .NET. |
| `Accept-Encoding` | Отбрасывается кодовым модулем Apache при тонкой настройке поведения HTML-инжекции. |
| `Content-Encoding` | Отбрасывается при тонкой настройке поведения HTML-инжекции. |
| `If-None-Match` | Отбрасывается при подавлении кэширования. |
| `If-Not-Modified-Since` | Отбрасывается при подавлении кэширования. |
| `If-Match` | Изменяется при подавлении кэширования. |
| `If-Range` | Изменяется при подавлении кэширования. |
| `traceparent` | Используется для W3C-тегирования. |
| `tracestate` | Используется для W3C-тегирования. |
| `referer` | Содержит адрес предыдущей веб-страницы, с которой была перейдена ссылка на текущую. |
| `user-agent` | Используется для [определения браузера и ОС](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems."). |
| `x-host` | Содержит информацию о хосте для не-http(s)-доменов. |

### Заголовки ответа

| Заголовок | Назначение |
| --- | --- |
| `X-OneAgent-JS-Injection` | Подтверждает, что RUM JavaScript был инжектирован, для предотвращения дублирующей инжекции. Принимает одно из следующих значений: `true` (инжекция выполнена) или `block` (инжекцию нельзя пытаться выполнить). |
| `X-ruxit-JS-Agent` | Подтверждает, что RUM JavaScript был инжектирован. Принимает значения `true` или `block`. |
| `x-dtHealthCheck` | Содержит результаты диагностики инжекции RUM JavaScript, выполненной поддержкой Dynatrace. |
| `x-dtAgentId` | При включённой проверке работоспособности RUM каждый задействованный кодовый модуль OneAgent добавляет свой идентификатор. |
| `x-dtInjectedServlet` | Содержит полное имя инжектированного сервлета или фильтра. |
| `Set-Cookie` | Устанавливает cookie состояния сессии OneAgent. |
| `ETag` | OneAgent добавляет пользовательскую строку к исходному заголовку ответа `ETag` для отслеживания изменений в конфигурации приложения. |
| `Last-modified` | При изменении заголовка `ETag` OneAgent также вычитает 1 секунду из исходного значения этого заголовка. |
| `Content-Length` | Адаптируется при HTML-инжекции. |
| `Vary` | Адаптируется при HTML-инжекции в сжатые ответы. |
| `Content-Encoding` | Адаптируется при HTML-инжекции в сжатые ответы. |
| `Content-Type` | Устанавливается для ответов на специальные запросы. |
| `Access-Control-Allow-Origin` | Устанавливается для ответов на специальные запросы. |
| `Cache-Control` | Устанавливается для ответов на специальные запросы. |
| `Server-Timing` | Используется для передачи информации, необходимой для корреляции RUM. |
| `Timing-Allow-Origin` | Разрешает RUM JavaScript доступ к информации для корреляции при перекрёстных запросах. |
| `Access-Control-Allow-Headers` | Устанавливается для ответов на специальные запросы. |
| `Access-Control-Allow-Methods` | Устанавливается для ответов на специальные запросы. |
| `Access-Control-Max-Age` | Устанавливается для ответов на специальные запросы. |

## Cookie

RUM использует следующие cookie. Все они должны иметь возможность достигать Dynatrace. Подробнее об использовании cookie Dynatrace см. в разделе [Cookies and client-side storage for RUM and Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.").

| Cookie | Максимальный размер | Назначение |
| --- | --- | --- |
| `dtCookie<suffix>` | Без ограничений, обычно менее 100 байт | Отслеживает визит в нескольких запросах. |
| `dtPC<suffix>` | 58 байт | Определяет правильные конечные точки для передачи маяков; содержит идентификатор сессии для корреляции. |
| `dtSa<suffix>` | Максимальная длина URL | Служит промежуточным хранилищем для действий, охватывающих несколько страниц. |
| `dtValidationCookie<suffix>` | 23 байта | Определяет домен верхнего уровня. |
| `rxVisitor<suffix>` | 45 байт | Содержит идентификатор посетителя для корреляции сессий. |
| `rxvt<suffix>` | 27 байт | Включает метку времени таймаута сессии. |
| `dtsrVID<suffix>` | 20 байт | Указывает идентификатор текущего записанного представления. Существует с версии RUM JavaScript 1.325 до 1.333. |
| `dtSR<suffix>` | 81 байт | При включённом Session Replay хранит значения для сохранения консистентности записи между страницами. Доступен с версии RUM JavaScript 1.335+. |

## Mobile RUM

Для RUM Classic OneAgent для Mobile тегирует HTTP-запросы заголовком `x-dynatrace`. Dynatrace использует этот заголовок для связи мобильной части веб-запроса с сервисной частью, захваченной другим OneAgent. Для нового RUM-опыта OneAgent для Mobile тегирует HTTP-запросы с использованием заголовков `traceparent` и `tracestate`.

Для гибридных приложений cookie `dtAdk` позволяет объединить сессию OneAgent для Mobile и сессию RUM JavaScript, чтобы они отображались как одна сессия, тогда как cookie `dtAdkSettings` используется для синхронизации настроек между OneAgent для Mobile и RUM JavaScript.

`/mbeacon` — сигнал монитора, который OneAgent для Mobile отправляет обратно в Dynatrace при передаче данных через ActiveGate. При отправке данных на другой OneAgent сигнал монитора — `/dtmb`.