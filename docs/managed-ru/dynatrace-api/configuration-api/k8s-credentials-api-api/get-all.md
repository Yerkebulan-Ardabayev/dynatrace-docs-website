---
title: Kubernetes credentials API - GET all credentials
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/k8s-credentials-api-api/get-all
scraped: 2026-05-12T12:14:52.105988
---

# Kubernetes credentials API - GET all credentials

# Kubernetes credentials API - GET all credentials

* Reference
* Published Jul 22, 2019

Этот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema [Kubernetes connection settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "Просмотр таблицы schema builtin:cloud.kubernetes окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes`) и [Kubernetes platform monitoring settings](/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "Просмотр таблицы schema builtin:cloud.kubernetes.monitoring окружения мониторинга через Dynatrace API.") (`builtin:cloud.kubernetes.monitoring`).

Возвращает список всех доступных конфигураций Kubernetes credentials.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/kubernetes/credentials` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметр

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [KubernetesConfigStubListDto](#openapi-definition-KubernetesConfigStubListDto) | Успех |

### Объекты тела ответа

#### Объект `KubernetesConfigStubListDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [KubernetesConfigShortRepresentation[]](#openapi-definition-KubernetesConfigShortRepresentation) | - |

#### Объект `KubernetesConfigShortRepresentation`

Краткое представление конфигурации kubernetes.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| endpointUrl | string | URL Kubernetes API server.  Должен быть уникален в рамках Dynatrace-окружения.  URL должен быть валидным по RFC 2396. Ведущие и хвостовые пробелы не допускаются. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

### JSON-модели тела ответа

```
{



"values": [



{



"description": "string",



"endpointUrl": "string",



"id": "string",



"name": "string"



}



]



}
```

## Связанные темы

* [Explore Kubernetes in Dynatrace Hub](https://www.dynatrace.com/hub/?filter=kubernetes&utm_source=doc&utm_medium=link&utm_campaign=cross)