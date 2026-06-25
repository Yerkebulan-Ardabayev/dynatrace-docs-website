---
title: RUM JavaScript API - GET current version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-current-version
scraped: 2026-05-12T11:55:51.891871
---

# RUM JavaScript API - GET current version

# RUM JavaScript API - GET current version

* Reference
* Updated on May 02, 2022

Возвращает текущую версию Real User Monitoring JavaScript, внедрённую в указанное приложение.

Версия это натуральное число; большее число означает более новую версию. Проверить самую последнюю доступную версию можно, выполнив запрос [**GET latest version**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Получить список приложений с вручную внедрённым OneAgent JavaScript.").

Если доступна более новая версия, рекомендуется обновить RUM JavaScript в ваших приложениях. Самый последний RUM JavaScript можно получить в разных форматах фрагментов, подробнее см. [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Узнайте, как загружать теги ручного внедрения RUM через API").

Запрос возвращает данные в формате `text/plain`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/appRevision/{entity}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/appRevision/{entity}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| entity | string | ID сущности Dynatrace приложения.  Его можно получить из ответа вызова [GET the list of manually injected applications](https://dt-url.net/dl03sgo). | path | Required |

## Ответ

Ответ это обычный текст, показывающий текущую версию RUM JavaScript.

## Пример

В этом примере запрос запрашивает последнюю версию RUM JavaScript для приложения easyTravel Ionic Web, у которого ID **APPLICATION-BBFA55551D507E2B**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/appRevision/APPLICATION-BBFA55551D507E2B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/appRevision/APPLICATION-BBFA55551D507E2B
```

#### Тело ответа

```
1539600997135
```

#### Код ответа

200