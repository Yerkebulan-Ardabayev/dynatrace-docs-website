---
title: Configure cluster nodes responsibilities
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities
scraped: 2026-05-12T12:09:04.775577
---

# Configure cluster nodes responsibilities

# Configure cluster nodes responsibilities

* Published Apr 30, 2021

Этот API-запрос настраивает обязанности (responsibilities) узлов кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster/configuration`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [ClusterNodesConfigDtoNodeResponsibilitiesConfigDto](#openapi-definition-ClusterNodesConfigDtoNodeResponsibilitiesConfigDto) | Список узлов, для которых нужно изменить responsibilities | body | Required |

### Объекты тела запроса

#### Объект `ClusterNodesConfigDtoNodeResponsibilitiesConfigDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterNodes | [NodeResponsibilitiesConfigDto[]](#openapi-definition-NodeResponsibilitiesConfigDto) | - | Optional |

#### Объект `NodeResponsibilitiesConfigDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| agent | boolean | - | Optional |
| id | integer | - | Optional |
| webUI | boolean | - | Optional |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её нужно адаптировать для реального запроса.

```
{



"clusterNodes": [



{



"agent": true,



"id": 1,



"webUI": true



}



]



}
```

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успех |

## Пример

В этом примере отключается Web UI трафик на узле 1. Статус операции можно проверить через вызов Get cluster nodes configuration current status API.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"clusterNodes\":[{\"id\":1,\"ipAddress\":\"10.10.4.2\",\"webUI\":false,\"agent\":true,\"datacenter\":\"datacenter-1\",\"kubernetesRole\":\"\"}]}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration
```

#### Тело запроса

```
{



"clusterNodes": [



{



"id": 1,



"ipAddress": "10.10.4.2",



"webUI": false,



"agent": true,



"datacenter": "datacenter-1",



"kubernetesRole": ""



}



]



}
```

#### Тело ответа

```
{



"lockAcquired": true,



"acquirationTime": 1619771074449,



"notAcquiredReason": null



}
```

#### Код ответа

`200`