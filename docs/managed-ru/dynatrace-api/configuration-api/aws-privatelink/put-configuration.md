---
title: AWS PrivateLink API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/put-configuration
scraped: 2026-05-12T11:21:14.212620
---

# AWS PrivateLink API - PUT configuration

# AWS PrivateLink API - PUT configuration

* Reference
* Published Nov 19, 2020

Обновляет конфигурацию AWS PrivateLink.

Запрос принимает и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [AwsPrivateLinkConfig](#openapi-definition-AwsPrivateLinkConfig) | Конфигурация AWS PrivateLink. | body | Required |

### Объекты тела запроса

#### Объект `AwsPrivateLinkConfig`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| enabled | boolean | Включён ли AWS PrivateLink | Required |
| vpcEndpointServiceName | string | Имя VirtualPrivateCluster-сервиса | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"enabled": true,



"vpcEndpointServiceName": "string"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **201** | [AwsPrivateLinkConfig](#openapi-definition-AwsPrivateLinkConfig) | Успех. Настройки конфигурации обновлены. |

### Объекты тела ответа

#### Объект `AwsPrivateLinkConfig`

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Включён ли AWS PrivateLink |
| vpcEndpointServiceName | string | Имя VirtualPrivateCluster-сервиса |

### JSON-модели тела ответа

```
{



"enabled": true,



"vpcEndpointServiceName": "string"



}
```