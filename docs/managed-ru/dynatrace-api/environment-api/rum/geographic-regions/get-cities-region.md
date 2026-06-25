---
title: Geographic regions API - GET cities of a region
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/geographic-regions/get-cities-region
scraped: 2026-05-12T11:55:27.283954
---

# Geographic regions API - GET cities of a region

# Geographic regions API - GET cities of a region

* Reference
* Updated on May 02, 2022

Выводит список городов региона.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/cities/{countryCode}/{regionCode}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/cities/{countryCode}/{regionCode}` |

## Аутентификация

Для выполнения запроса необходим access token со scope `geographicRegions.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| countryCode | string | ISO-код требуемой страны.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go). | path | Required |
| regionCode | string | Код требуемого региона.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0). | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CountryWithRegionsWithCities](#openapi-definition-CountryWithRegionsWithCities) | Успех. Ответ содержит список городов региона. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Запрашиваемый ресурс не существует. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CountryWithRegionsWithCities`

Информация о стране.

| Элемент | Тип | Описание |
| --- | --- | --- |
| countryCode | string | ISO-код страны. |
| countryName | string | Название страны. |
| regionCount | integer | Количество регионов в стране. |
| regions | [RegionWithCities[]](#openapi-definition-RegionWithCities) | Список регионов страны. |

#### Объект `RegionWithCities`

Информация о регионе страны и его городах.

| Элемент | Тип | Описание |
| --- | --- | --- |
| cities | [City[]](#openapi-definition-City) | Список городов региона. |
| cityCount | integer | Количество городов в регионе страны. |
| code | string | Код региона. |
| name | string | Название региона. |

#### Объект `City`

Информация о городе.

| Элемент | Тип | Описание |
| --- | --- | --- |
| latitude | number | Широта города. |
| longitude | number | Долгота города. |
| name | string | Название города. |

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



"countryName": "France",



"regionCount": 13,



"regions": [



{



"cities": [



{



"latitude": 46.2806,



"longitude": 6.7217,



"name": "Abondance"



},



{



"latitude": 46.1008,



"longitude": 3.4463,



"name": "Abrest"



}



],



"cityCount": 4,



"code": "ARA",



"name": "Auvergne-Rhone-Alpes"



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