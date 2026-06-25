---
title: Set or update cluster proxy configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/put-cluster-proxy-configuration
scraped: 2026-05-12T12:06:58.940572
---

# Set or update cluster proxy configuration

# Set or update cluster proxy configuration

* Published Nov 18, 2020

Этот API-вызов обновляет proxy-конфигурацию кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/configuration`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [InternetProxyChangeRequest](#openapi-definition-InternetProxyChangeRequest) | Конфигурация proxy-сервера для интернет-подключения. | body | Required |

### Объекты тела запроса

#### Объект `InternetProxyChangeRequest`

Конфигурация proxy-сервера для интернет-подключения.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| nonProxyHosts | string[] | Хосты, для которых proxy не будет использоваться. Можно указать несколько хостов. Каждый хост может начинаться или заканчиваться wildcard '\*' (например, чтобы покрыть весь домен). | Optional |
| password | string | Пароль proxy-сервера. null означает «не менять предыдущее значение». | Optional |
| port | integer | Порт proxy-сервера. | Required |
| scheme | string | Протокол, используемый proxy-сервером. Возможные значения: * `http` * `https` | Required |
| server | string | Адрес (IP или hostname) proxy-сервера. | Required |
| user | string | Пользователь proxy-сервера. null означает «не менять предыдущее значение». | Optional |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её нужно адаптировать для реального запроса.

```
{



"nonProxyHosts": [



"string"



],



"password": "string",



"port": 1,



"scheme": "http",



"server": "string",



"user": "string"



}
```

## Ответ

### Коды ответа

| Код | Описание |
| --- | --- |
| **201** | Успешно, создана новая конфигурация. |
| **204** | Успешно, конфигурация обновлена. |
| **400** | Указанная proxy-конфигурация некорректна. |

## Пример

В этом примере добавляется proxy-сервер (`outbound-proxy.dynatrace.com`), работающий на порту 8080 и требующий пароль; одновременно исключается внутренний lab-хост (`*.internal.lab.company.com`).

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"scheme\":\"http\",\"server\":\"outbound-proxy.dynatrace.com\",\"port\":8080,\"nonProxyHosts\":[\"https://mycompany.com/proxy/*\",\"*.internal.lab.company.com\"],\"userOrPasswordDefined\":true}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/configuration
```

#### Тело ответа

```
{



"code": 201,



"message": "Successful, new configuration created."



}
```

#### Код ответа

`201`