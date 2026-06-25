---
title: HA - Get proxy configurations for all data centers
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration-ha-all
scraped: 2026-05-12T12:12:37.448874
---

# HA - Get proxy configurations for all data centers

# HA - Get proxy configurations for all data centers

* Published Nov 18, 2020

Этот API-вызов возвращает proxy-конфигурации всех датацентров в premium high availability развёртывании.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/configurations`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| dc | string | Датацентр. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Успех |
| **404** | - | Proxy для данного датацентра не настроен. |

### Объекты тела ответа

#### Объект `InternetProxy`

Конфигурация proxy-сервера для интернет-подключения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| nonProxyHosts | string[] | Хосты, для которых proxy не будет использоваться. |
| port | integer | Порт proxy-сервера. |
| scheme | string | Протокол, используемый proxy-сервером. |
| server | string | Адрес (IP или hostname) proxy-сервера. |
| userOrPasswordDefined | boolean | Указывает, настроены ли user/password для proxy. |

### JSON-модели тела ответа

```
{



"nonProxyHosts": [



"string"



],



"port": 1,



"scheme": "string",



"server": "string",



"userOrPasswordDefined": true



}
```

## Пример

В этом примере запрашиваются proxy-конфигурации всех датацентров. В ответ возвращается JSON со списком proxy-конфигураций для `eu-west-1` и `us-east-1`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configurations
```

#### Тело ответа

```
{



"configurations": {



"eu-west-1": {



"scheme": "http",



"server": "outbound-proxy-dc1.dynatrace.com",



"port": 8080,



"nonProxyHosts": [



"https://mycompany.com/proxy/*",



"*.internal.lab.company.com"



],



"userOrPasswordDefined": true



},



"us-east-1": {



"scheme": "http",



"server": "outbound-proxy-dc2.dynatrace.com",



"port": 8080,



"nonProxyHosts": [



""



],



"userOrPasswordDefined": true



}



}



}
```

#### Код ответа

`200`