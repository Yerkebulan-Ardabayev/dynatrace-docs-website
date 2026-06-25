---
title: Plugins API - DELETE a plugin's endpoint
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/delete-an-endpoint
scraped: 2026-05-12T11:21:04.451668
---

# Plugins API - DELETE a plugin's endpoint

# Plugins API - DELETE a plugin's endpoint

* Reference
* Published Jun 07, 2019

Удаляет указанный эндпоинт плагина ActiveGate.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}/endpoints/{endpointId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID плагина, в котором вы хотите удалить эндпоинт. | path | Required |
| endpointId | string | ID эндпоинта, который нужно удалить. | path | Required |

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **204** | Удалено. Ответ без тела. |

## Пример

В этом примере запрос удаляет эндпоинт с ID **8757307336635955682** из SAP plugin с ID **custom.remote.python.sap**. Код ответа 204 указывает, что удаление прошло успешно.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X DELETE \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
DELETE https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap/endpoints/8757307336635955682
```

#### Код ответа

204