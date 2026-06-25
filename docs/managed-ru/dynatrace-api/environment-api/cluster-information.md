---
title: Cluster information API
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/cluster-information
scraped: 2026-05-12T11:11:45.435570
---

# Cluster information API

# Cluster information API

* Reference
* Published Sep 24, 2018

API **Cluster information** позволяет проверить версию и внутреннее время вашего Dynatrace-окружения.

## GET cluster time

Запрос возвращает `text/plain`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/time` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/time` |

Ответ возвращает время кластера в миллисекундах UTC.

## GET cluster version

Dynatrace быстро развивается и выпускает новую версию сервера (кластера) с новыми функциями каждые две недели.

Мы эксплуатируем множество SaaS-кластеров по всему миру, и эти кластеры обновляются в разное время. Поскольку процесс обновления полностью прозрачен для клиента, сложно точно определить, когда ваше окружение обновлено до новой версии кластера.

Этот endpoint API позволяет запросить фактическую версию кластера вашего окружения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/config/clusterversion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/config/clusterversion` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `DataExport`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ClusterVersion](#openapi-definition-ClusterVersion) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка сервера. |

### Объекты тела ответа

#### Объект `ClusterVersion`

| Элемент | Тип | Описание |
| --- | --- | --- |
| version | string | Версия сервера Dynatrace. |

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



"version": "string"



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