---
title: Store cluster SSL certificate
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/ssl-certificates-v1/post-cluster-ssl-cert-store-status
scraped: 2026-05-12T12:01:04.935094
---

# Store cluster SSL certificate

# Store cluster SSL certificate

* Published Nov 18, 2020

Этот API-вызов сохраняет SSL-сертификат кластера.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать — смотрите [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "Как пройти аутентификацию для работы с Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/sslCertificate/store`

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| entityType | string | Тип сущности, возможные значения = "SERVER, COLLECTOR". Возможные значения: * `COLLECTOR` * `SERVER` | path | Required |
| entityId | integer | ID узла, который можно извлечь из URL во вью 'Node details'. | path | Required |
| body | [sslCertDto](#openapi-definition-sslCertDto) | Конфигурация SSL-сертификата. | body | Optional |

### Объекты тела запроса

#### Объект `sslCertDto`

Конфигурация SSL-сертификата.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| certificateChainEncoded | string | Сертификат(ы) стандарта X.509, в формате PEM base64, intermediate и root сертификаты. | Optional |
| privateKeyEncoded | string | Приватный ключ стандарта PKCS #8, в формате PEM base64. | Required |
| publicKeyCertificateEncoded | string | Сертификат стандарта X.509, в формате PEM base64, сертификат сервера. | Required |

### JSON-модель тела запроса

Это модель тела запроса с возможными элементами. Её нужно адаптировать для реального запроса.

```
{



"certificateChainEncoded": "-----BEGIN CERTIFICATE-----\nMIIDKT...XbTK+M\n-----END CERTIFICATE-----\n-----BEGIN CERTIFICATE-----\nMIIDKT...bXTK+M\n-----END CERTIFICATE-----",



"privateKeyEncoded": "-----BEGIN RSA PRIVATE KEY-----\nMIIEow...aHzMvp\n-----END RSA PRIVATE KEY-----",



"publicKeyCertificateEncoded": "-----BEGIN CERTIFICATE-----\nMIIDKT...XbTK+M\n-----END CERTIFICATE-----"



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Успешно или в процессе. |
| **400** | [CertificateStoreStatus](#openapi-definition-CertificateStoreStatus) | Некорректный тип сущности. |
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

В этом примере SSL-сертификат сохраняется на узле `32` кластера `myManaged.cluster.com`. В ответ возвращается информация о том, что SSL-сертификат успешно обновлён. Убедитесь, что запрос в формате JSON. Это означает, что объекты `privateKeyEncoded`, `publicKeyCertificateEncoded` и `certificateChainEncoded` должны быть в одну строку.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"privateKeyEncoded\":\"-----BEGIN RSA PRIVATE KEY-----\MIIEow...aHzMvp\-----END RSA PRIVATE KEY-----\",\"publicKeyCertificateEncoded\":\"-----BEGIN CERTIFICATE-----\MIIDKT...XbTK+M\-----END CERTIFICATE-----\",\"certificateChainEncoded\":\"-----BEGIN CERTIFICATE-----\MIIDKT...XbTK+M\-----END CERTIFICATE-----\-----BEGIN CERTIFICATE-----\MIIDKT...bXTK+M\-----END CERTIFICATE-----\"}"
```

#### URL запроса

```
https://myManaged.cluster.com/api/v1.0/onpremise/sslCertificate/store/SERVER/32
```

#### Тело ответа

Успешно обновлено. Тело ответа пустое.

#### Код ответа

`200`