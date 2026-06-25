---
title: Failure detection API - PUT reorder rules
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/service-api/failure-detection/detection-rules/reorder-rules
scraped: 2026-05-12T11:16:23.589247
---

# Failure detection API - PUT reorder rules

# Failure detection API - PUT reorder rules

* Reference
* Published Jan 11, 2021

Изменяет порядок правил обнаружения сбоев в соответствии с порядком ID в теле запроса.

Правила, отсутствующие в теле запроса, сохраняют свой относительный порядок, но помещаются после всех правил, присутствующих в запросе.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/reorderRules` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/service/failureDetection/parameterSelection/rules/reorderRules` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [FdpSelectionRuleOrder](#openapi-definition-FdpSelectionRuleOrder) | JSON-тело запроса. Содержит правила обнаружения сбоев в требуемом порядке. | body | Required |

### Объекты тела запроса

#### Объект `FdpSelectionRuleOrder`

Порядок правил в наборе правил.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ruleIds | string[] | Список ID правил. Правила в наборе располагаются так, чтобы их ID образовывали ту же последовательность, что и этот список. ID каждого правила в наборе должен встречаться в списке ровно один раз. | Required |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

```
{



"ruleIds": [



"R1",



"RZa",



"RZb"



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | - | Успех |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |

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
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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