---
title: ActiveGate auto-update configuration API - PUT an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/put-instance
scraped: 2026-05-12T11:59:31.506985
---

# ActiveGate auto-update configuration API - PUT an ActiveGate

# ActiveGate auto-update configuration API - PUT an ActiveGate

* Reference
* Published Mar 15, 2021

Редактирует конфигурацию авто-обновлений указанного Environment ActiveGate.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |
| PUT | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID требуемого ActiveGate. | path | Обязательный |
| body | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | JSON-тело запроса, содержащее параметры авто-обновления. | body | Обязательный |

### Объекты тела запроса

#### Объект `ActiveGateAutoUpdateConfig`

Конфигурация авто-обновлений ActiveGate.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| effectiveSetting | string | Фактическое состояние авто-обновления ActiveGate.  Применимо, только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из родительской настройки. Иначе это просто дубликат значения **setting**. Элемент может принимать значения * `ENABLED` * `DISABLED` | Опциональный |
| setting | string | Состояние авто-обновления ActiveGate: enabled, disabled или inherited.  Если установлено в `INHERITED`, настройка наследуется из глобальной конфигурации, заданной на уровне окружения или кластера Managed. Элемент может принимать значения * `DISABLED` * `ENABLED` * `INHERITED` | Обязательный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать для использования в реальном запросе.

```
{



"effectiveSetting": "ENABLED",



"setting": "INHERITED"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация авто-обновлений обновлена. У ответа нет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
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

## Validate payload

Рекомендуем валидировать payload перед отправкой реального запроса. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate/validator` |
| POST | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.write`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Валидация пройдена. Отправленная конфигурация авто-обновления корректна. У ответа нет тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Неудача. Входные данные некорректны. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния. |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений. |
| message | string | Сообщение об ошибке. |

#### Объект `ConstraintViolation`

Список нарушений ограничений.

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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

* [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Изучите основные концепции, связанные с ActiveGate.")