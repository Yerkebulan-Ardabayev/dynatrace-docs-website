---
title: Get cluster information about known cluster nodes
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/get-cluster-info-known-servers
scraped: 2026-05-12T12:12:52.806992
---

# Get cluster information about known cluster nodes

# Get cluster information about known cluster nodes

* Published Apr 30, 2021

Этот API-вызов возвращает информацию о кластере по известным узлам.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster`

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Cluster[]](#openapi-definition-Cluster) | Успех |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `Cluster`

| Элемент | Тип | Описание |
| --- | --- | --- |
| buildVersion | string | Версия сервера. |
| clusterMemberAddress | string | Адрес участника кластера. |
| communicationUris | string[] | Communication URIs. |
| ~~dnsEntryPointUris~~ | string[] | DEPRECATED  DNS entry point URIs. |
| id | integer | ID узла. |
| jvmInfo | string | Информация о JVM. |
| operationState | string | Состояние работы. |
| osInfo | string | Информация об ОС. |
| restServiceRootUris | string[] | REST service root URIs. |

### JSON-модели тела ответа

```
[



{



"buildVersion": "string",



"clusterMemberAddress": "string",



"communicationUris": [



"string"



],



"dnsEntryPointUris": [



"string"



],



"id": 1,



"jvmInfo": "string",



"operationState": "string",



"osInfo": "string",



"restServiceRootUris": [



"string"



]



}



]
```

## Пример

В этом примере запрос обращается к кластеру за текущей конфигурацией развёртывания и статусом. Кластер возвращает информацию о каждом узле в массиве. Каждый объект узла содержит id, статус, адреса коммуникации и сведения о host-окружении.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/cluster" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster
```

#### Тело ответа

```
[



{



"id": 1,



"clusterMemberAddress": "10.10.4.2:5701",



"operationState": "RUNNING",



"buildVersion": "1.216.10.20210429-124335",



"osInfo": "Platform: Linux, Version: 5.4.0-1041, Architecture: amd64, Processors: 16",



"jvmInfo": "VM: OpenJDK 64-Bit Server VM, Version: 11.0.8, Vendor: AdoptOpenJDK, Memory [maxMemory=17408M, initHeap=17408M, maxHeap=17408M, usedMeta=17M, committedMeta=17M, totalPhysicalMemory=62851M, freePhysicalMemory=14336M]",



"dnsEntryPointUris": [],



"restServiceRootUris": [



"https://ip-10-10-4-2.eu-west-1.compute.internal:8021/api/v1.0",



"https://10.10.4.2:8021/api/v1.0"



],



"communicationUris": [



"http://ip-10-10-4-2.eu-west-1.compute.internal:8020/communication",



"http://10.176.42.242:8020/communication"



]



},



...



]
```

#### Код ответа

`200`