---
title: Delete cluster proxy configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/delete-cluster-proxy-configuration
scraped: 2026-05-12T12:13:00.611439
---

# Delete cluster proxy configuration

# Delete cluster proxy configuration

* Published Nov 18, 2020

Этот API-вызов удаляет proxy-конфигурацию кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/configuration`

## Параметры

У запроса нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Успешно, возвращена предыдущая конфигурация. |
| **404** | - | Proxy не был настроен. |

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

В этом примере удаляется proxy-конфигурация из Dynatrace Managed развёртывания (`myManaged.cluster.com`). В ответ возвращается предыдущая proxy-конфигурация.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration
```

#### Тело ответа

```
{



"scheme": "http",



"server": "outbound-proxy.dynatrace.com",



"port": 8080,



"nonProxyHosts": [



"https://mycompany.com/proxy/*",



"*.internal.lab.company.com"



],



"userOrPasswordDefined": true



}
```

#### Код ответа

`200`