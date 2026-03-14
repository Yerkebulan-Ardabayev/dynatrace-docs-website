---
title: Deployment API - Просмотр конфигурации модуля процессов для OneAgent
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/oneagent/get-processmodule-config
scraped: 2026-03-05T21:38:44.834218
---

# Deployment API — Просмотр конфигурации модуля процессов для OneAgent

# Deployment API — Просмотр конфигурации модуля процессов для OneAgent

* Reference
* Published Mar 25, 2022

Запрос возвращает полезную нагрузку типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/installer/agent/processmoduleconfig` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/installer/agent/processmoduleconfig` |

## Аутентификация

Для выполнения этого запроса необходим токен доступа с областью действия `InstallerDownload`.

Чтобы узнать, как получить и использовать токен, см. раздел [Токены и аутентификация](../../../../discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication.md).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| revision | integer | Ранее полученная ревизия для сравнения. | query | Необязательный |
| sections | string | Список идентификаторов секций, разделённых запятыми, для которых необходимо получить значения. Поддерживаемые секции: 'general' и 'agentType'. По умолчанию — 'general'. | query | Необязательный |
| hostgroup | string | Имя группы хостов, в которую входит процесс. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AgentProcessModuleConfigResponse](#openapi-definition-AgentProcessModuleConfigResponse) | Успешно |
| **304** | - | Не изменено. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AgentProcessModuleConfigResponse`

Ответ на запрос конфигурации модуля процессов.

| Элемент | Тип | Описание |
| --- | --- | --- |
| properties | [SectionProperty[]](#openapi-definition-SectionProperty) | Свойства и их секции в данном ответе. |
| revision | integer | Новая ревизия, связанная с конфигурацией. |

#### Объект `SectionProperty`

Отдельное свойство агента с указанием его секции.

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ свойства. |
| section | string | Секция, к которой относится данное свойство. |
| value | string | Значение свойства. |

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
