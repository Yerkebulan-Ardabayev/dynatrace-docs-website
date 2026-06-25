---
title: Get cluster nodes configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-nodes-configuration
scraped: 2026-05-12T12:12:29.012269
---

# Get cluster nodes configuration

# Get cluster nodes configuration

* Published Apr 30, 2021

Этот API-запрос возвращает конфигурацию узлов кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster/configuration`

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **200** | Успех |

## Пример

Этот запрос возвращает все узлы со значениями их node capabilities и привязкой к датацентру.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration" -H  "accept: */*"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration
```

#### Тело ответа

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



},



{



"id": 2,



"ipAddress": "10.10.4.6",



"webUI": true,



"agent": false,



"datacenter": "datacenter-1",



"kubernetesRole": ""



}



}
```

#### Код ответа

`200`