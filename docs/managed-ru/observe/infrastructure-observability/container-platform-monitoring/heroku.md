---
title: Мониторинг Heroku
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/heroku
scraped: 2026-05-12T11:38:09.689135
---

# Heroku monitoring

# Мониторинг Heroku

* Reference
* 2-min read
* Published May 22, 2019

При включении облачного нативного мониторинга Dynatrace для ваших приложений Heroku вы получаете:

* Углублённый мониторинг приложений и детализацию на уровне кода для Java, PHP, Node.js и других платформ — с помощью единого, независимого от языка buildpack.
* [Автоматический анализ первопричин](/managed/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") ваших веб-приложений Heroku.
* Сведения об использовании [баз данных](/managed/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.") приложениями Heroku — включая подробные метрики для каждого запроса к базе данных.
* Данные [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") о поведении пользователей в веб-браузерах и на мобильных устройствах.
* Автоматизированный мониторинг внешних и сторонних сервисов (например, вызовов внешних REST API).

## Предварительные требования

[Настройте и сконфигурируйте интеграцию Dynatrace с Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## Просмотр результатов мониторинга

После привязки учётной записи Dynatrace к приложению Heroku вы получите полный спектр возможностей мониторинга приложений и сервисов, предоставляемых Dynatrace (например, **Smartscape** и детализацию на уровне сервисов с помощью **Service flow**). Dynatrace автоматически определяет, что ваше приложение работает на Heroku, а также сервисы, связанные с вашим приложением Heroku.

![Heroku monitoring](https://dt-cdn.net/images/heroku1-2874-778cc74486.png)

Мониторинг Heroku

Dynatrace автоматически запускает углублённый мониторинг приложений Heroku и обеспечивает видимость сервисов приложений на уровне кода. **Service flow** в Dynatrace позволяет отслеживать распространение запросов к сервисам, предоставляемым приложением Heroku, по всей системе. Трассировка сервисов также помогает выявлять узкие места производительности и неудачные запросы в цепочке межсервисного взаимодействия. С Dynatrace определить первопричину низкой производительности в гетерогенных стеках микросервисов стало проще, чем когда-либо.

![Heroku monitoring](https://dt-cdn.net/images/heroku2-2884-8bad582082.png)

Мониторинг Heroku

## Расстановка тегов на приложениях Heroku

Мощный [механизм тегирования](/managed/manage/tags-and-metadata "Use tags and metadata to organize data in your Dynatrace environment.") Dynatrace позволяет автоматически организовывать и фильтровать все отслеживаемые компоненты приложений Heroku. Dynatrace позволяет применять теги к процессам и хостам на основе переменных среды.

`heroku config:set DT_TAGS=owner=team-easytravel`

## Связанные темы

* [Настройка Dynatrace на Heroku](/managed/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")