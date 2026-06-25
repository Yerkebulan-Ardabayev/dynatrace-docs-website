---
title: ActiveGate auto-update configuration API - GET an ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/activegates/auto-update-config/get-instance
scraped: 2026-05-12T11:59:33.516731
---

# ActiveGate auto-update configuration API - GET an ActiveGate

# ActiveGate auto-update configuration API - GET an ActiveGate

* Reference
* Published Mar 15, 2021

Возвращает конфигурацию авто-обновлений указанного Environment ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |
| GET | Environment and Cluster ActiveGate (порт по умолчанию 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/activeGates/{agId}/autoUpdate` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `activeGates.read`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| agId | string | ID требуемого ActiveGate. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateAutoUpdateConfig](#openapi-definition-ActiveGateAutoUpdateConfig) | Успех |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Не найдено. Подробности в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `ActiveGateAutoUpdateConfig`

Конфигурация авто-обновлений ActiveGate.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние авто-обновления ActiveGate.  Применимо, только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из родительской настройки. Иначе это просто дубликат значения **setting**. Элемент может принимать значения * `ENABLED` * `DISABLED` |
| setting | string | Состояние авто-обновления ActiveGate: enabled, disabled или inherited.  Если установлено в `INHERITED`, настройка наследуется из глобальной конфигурации, заданной на уровне окружения или кластера Managed. Элемент может принимать значения * `DISABLED` * `ENABLED` * `INHERITED` |

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



"effectiveSetting": "ENABLED",



"setting": "INHERITED"



}
```

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