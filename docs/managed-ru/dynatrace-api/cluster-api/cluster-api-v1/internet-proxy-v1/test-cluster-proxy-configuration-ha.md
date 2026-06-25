---
title: HA - Test proxy configuration from specific data center
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/internet-proxy-v1/test-cluster-proxy-configuration-ha
scraped: 2026-05-12T12:12:15.862327
---

# HA - Test proxy configuration from specific data center

# HA - Test proxy configuration from specific data center

* Published Nov 18, 2020

Этот API-вызов тестирует proxy-конфигурацию из конкретного датацентра.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/proxy/test`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| dc | string | Датацентр. | path | Required |
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

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ConnectionStatus](#openapi-definition-ConnectionStatus) | Запрос обработан, подробности в теле ответа. |

### Объекты тела ответа

#### Объект `ConnectionStatus`

Результат теста интернет-подключения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| connectionOk | boolean | Результат теста подключения. |
| testExecuted | boolean | Был ли тест вообще выполнен. |
| testExecutionMessage | string | Дополнительные комментарии. Обычно объясняют, почему тест не был выполнен. |

### JSON-модели тела ответа

```
{



"connectionOk": true,



"testExecuted": true,



"testExecutionMessage": "string"



}
```

## Пример

В этом примере тестируется proxy-сервер (`outbound-proxy-dc1.dynatrace.com`) на порту 8080, требующий пароль, в конкретном датацентре (`eu-west-1`); одновременно исключается внутренний lab-хост (`*.internal.lab.company.com`). В ответ возвращается JSON, указывающий, что подключение в порядке.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/proxy/test/eu-west-1" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"scheme\":\"http\",\"server\":\"outbound-proxy-dc1.dynatrace.com\",\"port\":8080,\"nonProxyHosts\":[\"https://mycompany.com/proxy/*\",\"*.internal.lab.company.com\"],\"userOrPasswordDefined\":true}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/proxy/test/eu-west-1
```

#### Тело ответа

```
{



"connectionOk": true,



"testExecuted": true,



"testExecutionMessage": "string"



}
```

#### Код ответа

`200`