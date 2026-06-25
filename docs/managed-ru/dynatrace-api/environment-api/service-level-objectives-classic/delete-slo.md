---
title: Service-level objectives API - DELETE SLO
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/service-level-objectives-classic/delete-slo
scraped: 2026-05-12T11:57:33.093339
---

# Service-level objectives API - DELETE SLO

# Service-level objectives API - DELETE SLO

* Справочник
* Обновлено 7 января 2025 г.

Удаляет указанную цель уровня обслуживания (SLO).

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/slo/{id}` |
| DELETE | Environment и Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/slo/{id}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `slo.write`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого SLO. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. SLO удалён. Тело ответа отсутствует. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Запрошенный ресурс не существует. |
| **409** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Конфликт ресурса. |
| **500** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Внутренняя ошибка сервера. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Связанные темы

* [Service-Level Objectives](/managed/deliver/service-level-objectives-classic "Мониторинг и алертинг по service-level objectives в Dynatrace через Service-Level Objectives Classic.")