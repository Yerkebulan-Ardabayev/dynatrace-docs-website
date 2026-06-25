---
title: IP address mapping rules - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration
scraped: 2026-05-12T11:17:57.727711
---

# IP address mapping rules - PUT configuration

# IP address mapping rules - PUT configuration

* Reference
* Published Sep 24, 2020

Обновляет конфигурацию сопоставления между IP-адресами и географическими регионами.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| body | [IpAddressMappings](#openapi-definition-IpAddressMappings) | JSON-тело запроса. Содержит конфигурацию сопоставления IP-адресов. | body | Optional |

### Объекты тела запроса

#### Объект `IpAddressMappings`

Конфигурация сопоставлений IP-адресов с географическими расположениями.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule[]](#openapi-definition-IpAddressMappingRule) | Список правил сопоставления IP-адресов.  Правила оцениваются сверху вниз; применяется первое подходящее правило. | Optional |

#### Объект `IpAddressMappingRule`

Конфигурация сопоставления IP-адреса с географическим расположением.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | Расположение для сопоставления IP-адреса. | Required |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | IP-адрес или диапазон IP-адресов для сопоставления с расположением. | Required |

#### Объект `IpAddressMappingLocation`

Расположение для сопоставления IP-адреса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| city | string | Название города расположения. | Optional |
| countryCode | string | Код страны расположения.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go). | Required |
| latitude | number | Широта расположения в формате `DDD.dddd`. | Optional |
| longitude | number | Долгота расположения в формате `DDD.dddd`. | Optional |
| regionCode | string | Код региона расположения.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0). | Optional |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов для сопоставления с расположением.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| address | string | IP-адрес для сопоставления.  Для диапазона IP-адресов это адрес **from**. | Required |
| addressTo | string | Адрес **to** диапазона IP-адресов. | Optional |
| subnetMask | integer | Маска подсети диапазона IP-адресов. | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

```
{



"ipAddressMappingRules": [



{



"ipAddressMappingLocation": {



"city": "string",



"countryCode": "string",



"latitude": 1,



"longitude": 1,



"regionCode": "string"



},



"ipAddressRange": {



"address": "string",



"addressTo": "string",



"subnetMask": 1



}



}



]



}
```

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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

## Validate payload

Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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

#### JSON-модели тела ответа

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

* [Сопоставление внутренних IP-адресов с расположениями для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших веб-приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших мобильных приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших пользовательских приложений.")