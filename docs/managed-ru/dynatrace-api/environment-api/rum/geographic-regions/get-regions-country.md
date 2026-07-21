---
title: Geographic regions API - GET regions of a country
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/geographic-regions/get-regions-country
scraped: 2026-05-12T11:55:33.271595
---

# Geographic regions API - GET regions of a country

# Geographic regions API - GET regions of a country

* Reference
* Updated on May 02, 2022

Выводит список регионов страны.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/regions/{countryCode}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/regions/{countryCode}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `geographicRegions.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| countryCode | string | ISO-код требуемой страны.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go?dt=m). | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CountryWithRegions](#openapi-definition-CountryWithRegions) | Успех. Ответ содержит список регионов страны. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CountryWithRegions`

Информация о стране.

| Элемент | Тип | Описание |
| --- | --- | --- |
| countryCode | string | ISO-код страны. |
| countryName | string | Название страны. |
| regionCount | integer | Количество регионов в стране. |
| regions | [Region[]](#openapi-definition-Region) | Список регионов страны. |

#### Объект `Region`

Информация о регионе страны.

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | string | Код региона. |
| name | string | Название региона. |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"countryCode": "FR",



"countyName": "France",



"regionCount": 2,



"regions": [



{



"code": "ARA",



"name": "Auvergne-Rhone-Alpes"



},



{



"code": "BFC",



"name": "Bourgogne-Franche-Comte"



}



]



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Связанные темы

* [Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")
* [Определение IP-адресов, геолокаций и user agent'ов](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace определяет IP-адреса и геолокации (город, регион, страну), а также браузеры, устройства и операционные системы.")