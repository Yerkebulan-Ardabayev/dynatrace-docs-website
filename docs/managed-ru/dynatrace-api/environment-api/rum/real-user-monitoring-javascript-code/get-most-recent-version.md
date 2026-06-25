---
title: RUM JavaScript API - GET latest version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-most-recent-version
scraped: 2026-05-12T11:55:53.686660
---

# RUM JavaScript API - GET latest version

# RUM JavaScript API - GET latest version

* Reference
* Updated on May 02, 2022

Возвращает самую последнюю версию Real User Monitoring JavaScript, доступную для вашего окружения.

Версия это натуральное число, большее число означает более новую версию. Проверить версию, которую вы фактически используете, можно, выполнив запрос [**GET the current version of the Real User Monitoring JavaScript**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Получить список приложений с вручную внедрённым OneAgent JavaScript.").

Если доступна более новая версия, рекомендуется обновить RUM JavaScript в ваших приложениях. Самый последний RUM JavaScript можно получить в разных форматах фрагментов, подробнее см. [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Узнайте, как загружать теги ручного внедрения RUM через API").

Запрос возвращает данные в формате `text/plain`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/jsLatestVersion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/jsLatestVersion` |

## Аутентификация

Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

Ответ это обычный текст, показывающий самую последнюю версию RUM JavaScript.

## Пример

В этом примере запрос запрашивает последнюю версию RUM JavaScript, доступную для окружения.

API-токен передаётся в заголовке **Authorization**.

Самый последний RUM JavaScript: **10156181011154332**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsLatestVersion \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/jsLatestVersion
```

#### Тело ответа

```
10156181011154332
```

#### Код ответа

200