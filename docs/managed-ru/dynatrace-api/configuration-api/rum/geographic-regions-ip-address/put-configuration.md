---
title: IP address mapping rules - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration
---

# IP address mapping rules - PUT configuration

# IP address mapping rules - PUT configuration

* Справочник
* Обновлено 21 июл. 2026

Устарело

Этот API endpoint устарел. Вместо него используйте [схему Map IP addresses to locations](/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-mappings "Просмотр таблицы схемы настроек builtin:rum.ip-mappings вашей среды мониторинга через Dynatrace API.").

Обновляет конфигурацию сопоставления IP-адресов с географическими регионами.

Запрос принимает тело в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью `WriteConfig`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| body | [IpAddressMappings](#openapi-definition-IpAddressMappings) | Тело JSON запроса. Содержит конфигурацию сопоставления IP-адресов. | body | Опциональный |

### Объекты тела запроса

#### Объект `IpAddressMappings`

Конфигурация сопоставлений IP-адресов с географическими местоположениями.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule](#openapi-definition-IpAddressMappingRule)[] | Список правил сопоставления IP-адресов. Правила вычисляются сверху вниз; применяется первое совпавшее правило. | Опциональный |

#### Объект `IpAddressMappingRule`

Конфигурация сопоставления IP-адреса с географическим местоположением.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | Местоположение для сопоставления IP-адреса. | Обязательный |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | IP-адрес или диапазон IP-адресов, сопоставляемых с местоположением. | Обязательный |

#### Объект `IpAddressMappingLocation`

Местоположение для сопоставления IP-адреса.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| city | string | Название города для данного местоположения. | Опциональный |
| countryCode | string | Код страны для данного местоположения. Чтобы получить список доступных кодов стран, используйте запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). | Обязательный |
| latitude | number | Широта местоположения в формате `DDD.dddd`. | Опциональный |
| longitude | number | Долгота местоположения в формате `DDD.dddd`. | Опциональный |
| regionCode | string | Код региона для данного местоположения. Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). | Опциональный |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов, сопоставляемых с местоположением.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| address | string | IP-адрес для сопоставления. Для диапазона IP-адресов это адрес **from** (начало диапазона). | Обязательный |
| addressTo | string | Адрес **to** (конец) диапазона IP-адресов. | Опциональный |
| subnetMask | integer | Маска подсети для диапазона IP-адресов. | Опциональный |

### Модель JSON тела запроса

Это модель тела запроса, демонстрирующая возможные элементы. Перед использованием в реальном запросе её нужно адаптировать.

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

### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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

## Валидация тела запроса

Рекомендуется проверять тело запроса перед отправкой реального запроса. Код ответа **204** означает, что тело запроса корректно.

Запрос принимает тело в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью `WriteConfig`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответов

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Отправленная конфигурация корректна. Тело ответа отсутствует. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные недействительны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
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

## Связанные темы

* [Сопоставление внутренних IP-адресов с местоположениями для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace для использования локальных адресов, чтобы определить местонахождение пользователей ваших веб-приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Настройте Dynatrace для использования локальных адресов, чтобы определить местонахождение пользователей ваших мобильных приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace для использования локальных адресов, чтобы определить местонахождение пользователей ваших пользовательских приложений.")