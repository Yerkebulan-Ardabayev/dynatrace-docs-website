---
title: Hosts API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/hosts-api/post-tags
scraped: 2026-03-05T21:26:49.944416
---

* Deprecated

Назначает пользовательские теги указанному хосту. Необходимо указать только значение тега. Контекст `CONTEXTLESS` будет назначен автоматически.

Использование данного API ограничено тегами, содержащими только значение. Для назначения тегов формата «ключ:значение» используйте Custom tags API.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/infrastructure/hosts/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/infrastructure/hosts/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Сведения о получении и использовании токена см. в разделе Tokens and authentication.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace для обновляемого хоста. | path | Обязательный |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Список тегов, назначаемых сущности Dynatrace. | body | Необязательный |

### Объекты тела запроса

#### Объект `UpdateEntity`

Список тегов, назначаемых сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| tags | string[] | Список тегов, назначаемых сущности Dynatrace. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Она должна быть скорректирована для использования в реальном запросе.

```
{


"tags": [


"office-linz",


"office-klagenfurt"


]


}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успешно. Параметры хоста обновлены. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Элемент может принимать следующие значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{


"error": {


"code": 1,


"constraintViolations": [


{


"location": "string",


"message": "string",


"parameterLocation": "HEADER",


"path": "string"


}


],


"message": "string"


}


}
```

## Пример

В этом примере запрос назначает теги **Linux** и **Rack 123** хосту **tag009** с идентификатором **HOST-B7A6F9EE9F366CB5**.

Токен API передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \


https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5 \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-H 'Content-Type: application/json' \


-d '{


"tags": [


"Linux",


"Rack 123"


]


}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/infrastructure/hosts/HOST-B7A6F9EE9F366CB5
```

#### Тело запроса

```
{


"tags": [


"iOS app",


"Adnroid app"


]


}
```

#### Код ответа

204

## Связанные темы

* Hosts Classic
