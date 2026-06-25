---
title: Deployment API - View process module configuration for OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-processmodule-config
scraped: 2026-05-12T11:58:19.737818
---

# Deployment API - View process module configuration for OneAgent

# Deployment API - View process module configuration for OneAgent

* Справочник
* Опубликовано 25 марта 2022 г.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/processmoduleconfig` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/processmoduleconfig` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| revision | integer | Ранее полученная ревизия для сравнения. | query | Необязательный |
| sections | string | Список разделённых запятыми идентификаторов секций, для которых нужно получить значения. Поддерживаемые секции: 'general' и 'agentType'. По умолчанию 'general'. | query | Необязательный |
| hostgroup | string | Имя host group, в которую входит процесс. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AgentProcessModuleConfigResponse](#openapi-definition-AgentProcessModuleConfigResponse) | Успех |
| **304** | - | Не изменено. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AgentProcessModuleConfigResponse`

Ответ на запрос конфигурации модуля процессов.

| Поле | Тип | Описание |
| --- | --- | --- |
| properties | [SectionProperty[]](#openapi-definition-SectionProperty) | Свойства и их секции в этом ответе. |
| revision | integer | Новая ревизия, связанная с конфигурацией. |

#### Объект `SectionProperty`

Одно свойство агента со связанной с ним секцией.

| Поле | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ свойства. |
| section | string | Секция, к которой относится это свойство. |
| value | string | Значение свойства. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"properties": [



{



"key": "dockerInjection",



"section": "general",



"value": "on"



}



],



"revision": 64459404400310540



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