---
title: Get cluster SSL certificate storage status
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/get-cluster-ssl-cert-storage-status
scraped: 2026-05-12T12:12:54.022593
---

# Get cluster SSL certificate storage status

# Get cluster SSL certificate storage status

* Published Dec 29, 2020

Этот API-вызов возвращает статус хранилища SSL-сертификата кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

BAD\_REQUEST

Статус хранилища сертификатов доступен только в runtime во время обновления или загрузки сертификата. После того как сертификат загружен и узел перезапущен, этот API-вызов вернёт `BAD_REQUEST`, потому что статуса хранилища нет.

## Endpoint

`/api/v1.0/onpremise/sslCertificate/store`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| entityType | string | Тип сущности, возможные значения = "COLLECTOR". Возможные значения: * `COLLECTOR` * `SERVER` | path | Required |
| entityId | integer | ID узла, который можно извлечь из URL во вью 'Node details'. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Успешно или в процессе. |
| **400** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Некорректный тип сущности. |
| **404** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Статус не найден. |
| **500** | - | Внутренняя ошибка. |
| **522** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Цепочка сертификатов некорректна. |
| **523** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Приватный ключ не соответствует сертификату публичного ключа. |
| **525** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Сертификат публичного ключа некорректен. |
| **526** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Приватный ключ некорректен. |
| **527** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Ошибка при сохранении SSL-сертификата. |
| **528** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Сертификат сохранён, но не обновлён. |
| **529** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Внутренняя ошибка. |

### Объекты тела ответа

#### Объект `CertificateStoreStatus`

| Элемент | Тип | Описание |
| --- | --- | --- |
| certificateStoreStatus | string | -Возможные значения: * `BAD_REQUEST` * `CERTIFICATE_CHAIN_IS_INVALID` * `CERTIFICATE_IS_EXPIRED` * `CERTIFICATE_STORED_BUT_NOT_REFRESHED` * `ERROR` * `GENERAL_ERROR_WHILE_STORING_CERTIFICATE` * `IN_PROGRESS` * `NOT_FOUND` * `OK` * `PRIVATE_KEY_DOES_NOT_MATCH_PUBLIC_KEY_CERTIFICATE` * `PRIVATE_KEY_IS_INVALID` * `PUBLIC_KEY_CERTIFICATE_IS_INVALID` |
| detailedError | string | - |

#### Объект `CertificateStoreStatus`

| Элемент | Тип | Описание |
| --- | --- | --- |
| certificateStoreStatus | string | -Возможные значения: * `BAD_REQUEST` * `CERTIFICATE_CHAIN_IS_INVALID` * `CERTIFICATE_IS_EXPIRED` * `CERTIFICATE_STORED_BUT_NOT_REFRESHED` * `ERROR` * `GENERAL_ERROR_WHILE_STORING_CERTIFICATE` * `IN_PROGRESS` * `NOT_FOUND` * `OK` * `PRIVATE_KEY_DOES_NOT_MATCH_PUBLIC_KEY_CERTIFICATE` * `PRIVATE_KEY_IS_INVALID` * `PUBLIC_KEY_CERTIFICATE_IS_INVALID` |
| detailedError | string | - |

### JSON-модели тела ответа

```
{



"certificateStoreStatus": "BAD_REQUEST",



"detailedError": "string"



}
```

```
{



"certificateStoreStatus": "BAD_REQUEST",



"detailedError": "string"



}
```

## Пример

В этом примере запрашивается статус хранилища SSL-сертификата на узле `32` кластера `myManaged.cluster.com`. В ответ возвращается статус, указывающий, что SSL-сертификат успешно сохранён.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32" -H  "accept: application/json" -H  "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32
```

#### Тело ответа

```
{



"certificateStoreStatus": "Successful",



"detailedError": null



}
```

#### Код ответа

`200`