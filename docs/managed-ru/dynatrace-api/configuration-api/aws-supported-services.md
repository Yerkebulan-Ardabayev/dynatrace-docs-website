---
title: AWS supported services API
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/aws-supported-services
scraped: 2026-05-12T11:04:45.318300
---

# AWS supported services API

# AWS supported services API

* Reference
* Published May 31, 2022

Возвращает список всех поддерживаемых AWS-сервисов, доступных в вашем окружении.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/aws/supportedServices` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/aws/supportedServices` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CloudSupportedServicesList](#openapi-definition-CloudSupportedServicesList) | Успех |

### Объекты тела ответа

#### Объект `CloudSupportedServicesList`

Список метаданных поддерживаемых сервисов

| Элемент | Тип | Описание |
| --- | --- | --- |
| services | [CloudSupportedService[]](#openapi-definition-CloudSupportedService) | Список метаданных поддерживаемых сервисов |

#### Объект `CloudSupportedService`

Метаданные поддерживаемого сервиса

| Элемент | Тип | Описание |
| --- | --- | --- |
| cloudProviderServiceType | string | Имя сервиса, используемое облачным провайдером. |
| displayName | string | Отображаемое имя сервиса в Dynatrace UI |
| entityType | string | Тип сущности, отслеживаемый этим сервисом |
| name | string | Уникальное имя сервиса, используемое Dynatrace. |

### JSON-модели тела ответа

```
{



"services": [



{



"cloudProviderServiceType": "string",



"displayName": "string",



"entityType": "string",



"name": "string"



}



]



}
```

## Пример

В этом примере запрос возвращает список поддерживаемых AWS-сервисов, доступных для окружения **mySampleEnv**. Результат усечён до трёх записей.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl --request GET \



--url https://mySampleEnv.live.dynatrace.com/api/config/v1/aws/supportedServices \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/aws/supportedServices
```

#### Тело ответа

```
{



"services": [



{



"cloudProviderServiceType": "AWS/ApiGateway",



"name": "APIGateway",



"entityType": "cloud:aws:api_gateway",



"displayName": "Amazon API Gateway"



},



{



"cloudProviderServiceType": "AWS/RDS",



"name": "Aurora",



"entityType": "cloud:aws:aurora",



"displayName": "Amazon Aurora"



},



{



"cloudProviderServiceType": "AWS/Neptune",



"name": "neptune",



"entityType": "cloud:aws:neptune",



"displayName": "Amazon Neptune"



}



]



}
```

#### Код ответа

200

## Связанные темы

* [All AWS cloud services](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных AWS-сервисов с помощью Dynatrace и просмотр доступных метрик.")