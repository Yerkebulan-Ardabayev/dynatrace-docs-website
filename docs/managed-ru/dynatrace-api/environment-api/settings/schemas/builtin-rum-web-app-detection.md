---
title: Settings API - Application detection schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-app-detection
scraped: 2026-05-12T11:47:12.243425
---

# Settings API - Application detection schema table

# Settings API - Application detection schema table

* Published Dec 05, 2023

### Обнаружение приложений (`builtin:rum.web.app-detection)`

Задайте новые приложения для Real User Monitoring (RUM) с помощью [application detection rules](https://dt-url.net/wb3f0pfr), проверьте, как существующие правила соотносятся с вашими приложениями.

По умолчанию Dynatrace связывает все данные мониторинга с приложением-placeholder (`<your-dynatrace-url>//#uemapplications/uemappmetrics;uemapplicationId=APPLICATION-EA7C4B59F27D43EB`). Задайте собственные правила обнаружения, чтобы группировать данные мониторинга в отдельные приложения Dynatrace.

Если ещё не сделали этого, разверните OneAgent (`<your-dynatrace-url>//#install`). После развёртывания [RUM](https://dt-url.net/1n2b0prq) включается по умолчанию для всех web-приложений, автоматически обнаруженных OneAgent. OneAgent [автоматически инжектит](https://dt-url.net/kp5f0p5z) JavaScript-сниппет в HTML всех страниц мониторимых web-приложений, чтобы захватывать данные мониторинга и обеспечивать end-to-end видимость.

* Правила применяются последовательно, причём верхние правила имеют приоритет над нижними.
* [Не видите своих приложений или RUM-данных?](https://dt-url.net/kl2a0pm4)
* Подробнее об [определении вашего web-приложения](https://dt-url.net/r63b0pgq).

Для следующего набора URL:

* http://www.mybookshop.com/about
* http://checkout.mybookshop.com/proceed
* http://mybook.shop.com/about/index.php
* http://www.this-is-mybookshop.com/about/index.php

Правило *Domain (host) contains* **mybook** совпадает с:

* http://www.**mybook**shop.com/about
* http://checkout.**mybook**shop.com/proceed
* http://**mybook**.shop.com/about/index.php
* http://www.this-is-**mybook**shop.com/about/index.php

Правило *Domain (host) ends with* **shop.com** совпадает с:

* http://www.mybook**shop.com**/about
* http://checkout.mybook**shop.com**/proceed
* http://mybook.**shop.com**/about/index.php
* http://www.this-is-mybook**shop.com**/about/index.php

Правило *Domain (host) equals* **www.mybookshop.com** совпадает с:

* http://**www.mybookshop.com**/about/index.php

Правило *Domain (host) matches* **mybookshop.com** совпадает с:

* http://www.**mybookshop.com**/about
* http://checkout.**mybookshop.com**/proceed

Правило *Domain (host) starts with* **checkout** совпадает с:

* http://**checkout**.mybookshop.com/proceed

Правило *URL contains* **mybookshop.com/about** совпадает с:

* http://www.**mybookshop.com/about**
* http://www.this-is-**mybookshop.com/about**/index.php

Правило *URL ends with* **about/index.php** совпадает с:

* http://mybook.shop.com/**about/index.php**
* http://www.this-is-mybookshop.com/**about/index.php**

Правило *URL equals* **http://www.mybookshop.com/about** совпадает с:

* **http://www.mybookshop.com/about**

Правило *URL starts with* **http://www.mybookshop.com** совпадает с:

* **http://www.mybookshop.com**/about

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.app-detection` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.app-detection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.app-detection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.app-detection` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Сопоставитель `matcher` | enum | Возможные значения: * `DOMAIN_CONTAINS` * `DOMAIN_ENDS_WITH` * `DOMAIN_EQUALS` * `DOMAIN_MATCHES` * `DOMAIN_STARTS_WITH` * `URL_CONTAINS` * `URL_ENDS_WITH` * `URL_EQUALS` * `URL_STARTS_WITH` | Required |
| Шаблон `pattern` | text | - | Required |
| Приложение `applicationId` | text | Выберите существующее приложение или создайте новое. | Required |
| Описание `description` | text | Добавьте описание для вашего правила | Optional |