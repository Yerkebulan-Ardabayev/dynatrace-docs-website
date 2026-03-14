---
title: Applications API - POST tags
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/topology-and-smartscape/applications-api/post-tags
scraped: 2026-03-05T21:27:04.307374
---

# Applications API - POST tags


* Reference
* Updated on Mar 22, 2023
* Deprecated

Присваивает [пользовательские теги](../../../../../common/manage/tags-and-metadata.md "Используйте теги и метаданные для организации данных в вашей среде Dynatrace.") указанному приложению. Достаточно указать только значение тега. Контекст `CONTEXTLESS` будет присвоен автоматически.

Использование этого API ограничено тегами, содержащими только значение. Чтобы присвоить теги формата ключ:значение, используйте [Custom tags API](../../custom-tags/post-tags.md "Присвойте пользовательские теги отслеживаемым сущностям через Dynatrace API.").

Запрос принимает полезную нагрузку типа `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/entity/applications/{meIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/entity/applications/{meIdentifier}` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `DataExport`.

Чтобы узнать, как получить и использовать его, см. [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| meIdentifier | string | Идентификатор сущности Dynatrace для приложения, которое необходимо обновить. | path | Обязательный |
| body | [UpdateEntity](#openapi-definition-UpdateEntity) | Список тегов для присвоения сущности Dynatrace. | body | Необязательный |

### Объекты тела запроса

#### Объект `UpdateEntity`

Список тегов для присвоения сущности Dynatrace.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| tags | string[] | Список тегов для присвоения сущности Dynatrace. | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Необходимо адаптировать её для использования в реальном запросе.

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
| **204** | - | Успешно. Параметры приложения обновлены. |
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
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

В данном примере запрос присваивает теги **iOS app** и **Android app** приложению **easyTravel Demo** с идентификатором **MOBILE\_APPLICATION-752C288D59734C79**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X POST \


https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79 \


-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \


-H 'Content-Type: application/json' \


-d '{


"tags": [


"iOS app",


"Android app"


]


}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/entity/applications/MOBILE_APPLICATION-752C288D59734C79
```

#### Тело запроса

```
{


"tags": [


"iOS app",


"Android app"


]


}
```

#### Код ответа

204

## Связанные темы

* [Real User Monitoring](../../../../observe/digital-experience/rum-concepts/rum-overview.md "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
