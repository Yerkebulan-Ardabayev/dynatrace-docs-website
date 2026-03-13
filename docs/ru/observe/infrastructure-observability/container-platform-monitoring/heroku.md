---
title: Heroku monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/heroku
scraped: 2026-02-06T16:28:55.999404
---

# Мониторинг Heroku

# Мониторинг Heroku

* Reference
* Чтение: 2 мин
* Опубликовано 22 мая 2019 г.

Благодаря облачно-нативному мониторингу Dynatrace, включённому для ваших приложений Heroku, вы получаете:

* Глубокий мониторинг приложений и детализацию на уровне кода для Java, PHP, Node.js и многого другого — с помощью единственного, независимого от языка buildpack
* [Автоматический анализ первопричин](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.") для ваших веб-приложений Heroku
* Сведения о том, как ваши приложения Heroku используют [базы данных](/docs/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.") — включая детальные метрики для каждого оператора базы данных
* Данные [Real User Monitoring](/docs/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.") о поведении клиентов в веб-браузере и на мобильных устройствах
* Автоматический мониторинг внешних и сторонних сервисов (например, обращения к внешним REST API)

## Предварительные требования

[Настройте и сконфигурируйте интеграцию Dynatrace с Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.").

## Просмотр результатов мониторинга

После связывания вашей учётной записи Dynatrace с приложением Heroku вы получите полный спектр видимости мониторинга приложений и сервисов, которую предоставляет Dynatrace (например, **Smartscape** и аналитику на уровне сервисов с помощью **Service flow**). Dynatrace автоматически определяет, что ваше приложение работает на Heroku, а также обнаруживает сервисы, связанные с вашим приложением Heroku.

![Heroku monitoring](https://dt-cdn.net/images/heroku1-2874-778cc74486.png)

Dynatrace автоматически инициирует глубокий мониторинг приложений для ваших приложений Heroku и обеспечивает видимость на уровне кода для сервисов ваших приложений. **Service flow** в Dynatrace позволяет отслеживать, как запросы к сервисам, предоставляемым вашим приложением Heroku, распространяются по системе. Трассировка сервисов также помогает выявлять узкие места в производительности и неудавшиеся запросы в цепочке взаимодействия между сервисами. С Dynatrace определить первопричину низкой производительности в гетерогенных стеках микросервисов стало проще, чем когда-либо.

![Heroku monitoring](https://dt-cdn.net/images/heroku2-2884-8bad582082.png)

## Теггирование приложений Heroku

Вы можете использовать мощный [механизм тегирования](/docs/manage/tags-and-metadata "Learn how to define tags and metadata. Understand how to use tags and metadata to organize your environment.") Dynatrace для автоматической организации и фильтрации всех отслеживаемых компонентов приложений Heroku. Dynatrace позволяет применять теги к процессам и хостам на основе переменных окружения.

`heroku config:set DT_TAGS=owner=team-easytravel`

## Связанные темы

* [Настройка Dynatrace на Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.")
