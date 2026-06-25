---
title: RUM JavaScript API - GET synchronous code snippet
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync
scraped: 2026-05-12T11:55:57.616080
---

# RUM JavaScript API - GET synchronous code snippet

# RUM JavaScript API - GET synchronous code snippet

* Reference
* Updated on May 02, 2022

Возвращает встроенный скрипт, который инициализирует Dynatrace и динамически загружает код мониторинга в ваше приложение. Код мониторинга загружается синхронно.

Для получения RUM JavaScript также можно использовать эти функционально эквивалентные варианты:

* [OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Получить самый последний тег OneAgent JavaScript для ручного внедрения.")
* [JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Получить самый последний тег JavaScript для ручного внедрения.")
* [Asynchronous code snippet](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async "Получить асинхронный фрагмент кода RUM JavaScript.")
* [Inline code](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Получить самый последний встроенный код для ручного внедрения.")

Запрос возвращает данные в формате `text/plain`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/rum/syncCS/{entity}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/rum/syncCS/{entity}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| entity | string | ID сущности Dynatrace приложения.  Его можно получить из ответа вызова [GET the list of manually injected applications](https://dt-url.net/dl03sgo). | path | Required |

## Ответ

Ответ это обычный текст, содержащий встроенный HTML-код самой последней версии тега OneAgent JavaScript для указанного приложения.

## Пример

В этом примере запрос получает встроенный HTML-код последней версии RUM JavaScript для приложения easyTravel Ionic Web, у которого ID **APPLICATION-BBFA55551D507E2B**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до первой строки.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/rum/syncCS/APPLICATION-BBFA55551D507E2B \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/rum/syncCS/APPLICATION-BBFA55551D507E2B
```

#### Тело ответа

```
<script type="text/javascript"> <truncated>



</script>
```

#### Код ответа

200