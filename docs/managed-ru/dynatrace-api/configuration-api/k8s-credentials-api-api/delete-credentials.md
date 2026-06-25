---
title: Kubernetes credentials API - DELETE credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/delete-credentials
scraped: 2026-05-12T12:15:00.249027
---

# Kubernetes credentials API - DELETE credentials

# Kubernetes credentials API - DELETE credentials

* Reference
* Published Jul 22, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "Просмотр таблицы schema builtin:cloud.kubernetes окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes`) и [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "Просмотр таблицы schema builtin:cloud.kubernetes.monitoring окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`).

Удаляет указанную конфигурацию Kubernetes credentials. Удаление необратимо.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/{id}` |
| DELETE | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID удаляемой конфигурации Kubernetes credentials. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Удалено. Ответ без тела. |
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

## Связанные темы

* [Explore Kubernetes in Dynatrace Hub](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)