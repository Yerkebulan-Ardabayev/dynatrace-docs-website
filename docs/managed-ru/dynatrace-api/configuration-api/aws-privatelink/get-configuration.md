---
title: AWS PrivateLink API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-privatelink/get-configuration
scraped: 2026-05-12T11:21:11.724160
---

# AWS PrivateLink API - GET configuration

# AWS PrivateLink API - GET configuration

* Reference
* Published Nov 19, 2020

Возвращает конфигурацию AWS PrivateLink.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/privateLink` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AwsPrivateLinkConfig](#openapi-definition-AwsPrivateLinkConfig) | Успех. Результат в теле ответа. |

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