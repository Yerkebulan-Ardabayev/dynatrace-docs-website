---
title: Get cluster SSL certificate details
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-details
scraped: 2026-05-12T12:12:57.209191
---

# Get cluster SSL certificate details

# Get cluster SSL certificate details

* Published Dec 29, 2020

Этот API-вызов возвращает подробности SSL-сертификата кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/sslCertificate`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| entityType | string | Тип сущности, возможные значения = "SERVER, COLLECTOR". Возможные значения: * `COLLECTOR` * `SERVER` | path | Required |
| entityId | integer | ID узла, который можно извлечь из URL во вью 'Node details'. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SSLDetails](#openapi-definition-SSLDetails) | Успех |
| **500** | - | Внутренняя ошибка сервера. |

### Объекты тела ответа

#### Объект `SSLDetails`

| Элемент | Тип | Описание |
| --- | --- | --- |
| customKeyStore | boolean | - |
| customKeyStoreWritable | boolean | - |
| default | boolean | - |
| expirationDate | string | - |
| inProgress | boolean | - |
| issuer | string | - |
| restartRequired | boolean | - |
| subject | string | - |

### JSON-модели тела ответа

```
{



"customKeyStore": true,



"customKeyStoreWritable": true,



"default": true,



"expirationDate": "string",



"inProgress": true,



"issuer": "string",



"restartRequired": true,



"subject": "string"



}
```

## Пример

В этом примере запрашиваются подробности SSL-сертификата на узле `32` кластера `myManaged.cluster.com`. В ответ возвращается информация о текущем SSL-сертификате.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/SERVER/32" -H  "accept: application/json" -H  "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/SERVER/32
```

#### Тело ответа

```
{



"issuer": "EV SSL Intermediate CA RSA",



"subject": "n32.myManaged.cluster.com",



"expirationDate": 1615956886000,



"customKeyStore": false,



"customKeyStoreWritable": true,



"inProgress": false,



"restartRequired": false,



"default": false



}
```

#### Код ответа

`200`