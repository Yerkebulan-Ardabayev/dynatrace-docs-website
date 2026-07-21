---
title: IP address mapping rules - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration
---

# IP address mapping rules - PUT configuration

# IP address mapping rules - PUT configuration

* Справочник
* Опубликовано 24 сентября 2020 г.

Обновляет конфигурацию сопоставления IP-адресов с географическими регионами.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [IpAddressMappings](#openapi-definition-IpAddressMappings) | JSON тело запроса. Содержит конфигурацию сопоставления IP-адресов. | body | Опционально |

### Объекты тела запроса

#### Объект `IpAddressMappings`

Конфигурация сопоставлений IP-адресов с географическими местоположениями.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule](#openapi-definition-IpAddressMappingRule)[] | Список правил сопоставления IP-адресов. Правила проверяются сверху вниз, применяется первое подходящее правило. | Опционально |

#### Объект `IpAddressMappingRule`

Конфигурация сопоставления IP-адреса с географическим местоположением.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | Местоположение для сопоставления IP-адреса. | Обязательно |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением. | Обязательно |

#### Объект `IpAddressMappingLocation`

Местоположение для сопоставления IP-адреса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| city | string | Название города местоположения. | Опционально |
| countryCode | string | Код страны местоположения. Чтобы получить список доступных кодов стран, используй запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). | Обязательно |
| latitude | number | Широта местоположения в формате `DDD.dddd`. | Опционально |
| longitude | number | Долгота местоположения в формате `DDD.dddd`. | Опционально |
| regionCode | string | Код региона местоположения. Чтобы получить список доступных кодов регионов, используй запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). | Опционально |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| address | string | IP-адрес, который нужно сопоставить. Для диапазона IP-адресов это начальный адрес (**from**). | Обязательно |
| addressTo | string | Конечный адрес (**to**) диапазона IP-адресов. | Опционально |
| subnetMask | integer | Маска подсети диапазона IP-адресов. | Опционально |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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
| **204** | - | Успех. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели JSON тела ответа

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

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед её отправкой в составе реального запроса. Код ответа **204** означает, что полезная нагрузка допустима.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

Подробнее о том, как получить и использовать его, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Отправленная конфигурация допустима. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недопустимы |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели JSON тела ответа

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

## Похожие темы

* [Map internal IP addresses to locations for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Map internal IP addresses to locations for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")
* [Map internal IP addresses to locations for custom applications in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")