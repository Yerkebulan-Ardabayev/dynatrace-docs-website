---
title: Get cluster proxy configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/get-cluster-proxy-configuration
scraped: 2026-05-12T12:12:25.876559
---

# Get cluster proxy configuration

# Get cluster proxy configuration

* Published Nov 18, 2020

Этот API-вызов возвращает proxy-конфигурацию кластера.

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
| **200** | [InternetProxy](#openapi-definition-InternetProxy) | Успех |
| **404** | - | Proxy не настроен |

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

В этом примере запрашивается proxy-конфигурация Dynatrace Managed развёртывания (`myManaged.cluster.com`). В ответ возвращается информация: proxy-сервер `172.16.115.211` на порту `8080`, для использования требуется пароль.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration" -H  "accept: application/json"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration
```

#### Тело ответа

```
{



"scheme": "http",



"server": "172.16.115.211",



"port": 8080,



"userOrPasswordDefined": true



}
```

#### Код ответа

`200`