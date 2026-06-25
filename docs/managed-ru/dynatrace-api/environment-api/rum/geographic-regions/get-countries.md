---
title: Geographic regions API - GET countries
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/geographic-regions/get-countries
scraped: 2026-05-12T11:55:31.331904
---

# Geographic regions API - GET countries

# Geographic regions API - GET countries

* Reference
* Updated on May 02, 2022

Выводит список стран и их кодов.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/countries` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/countries` |

## Аутентификация

Для выполнения запроса необходим access token со scope `geographicRegions.read`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [CountryList](#openapi-definition-CountryList) | Успех. Ответ содержит список стран. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `CountryList`

Список стран.

| Элемент | Тип | Описание |
| --- | --- | --- |
| countries | [Country[]](#openapi-definition-Country) | Список стран. |
| countryCount | integer | Количество стран. |

#### Объект `Country`

Информация о стране.

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | string | ISO-код страны. |
| name | string | Название страны. |

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



"countries": [



{



"code": "FR",



"name": "France"



},



{



"code": "BE",



"name": "Belgium"



}



],



"countryCount": 252



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