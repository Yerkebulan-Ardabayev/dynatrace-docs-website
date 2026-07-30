---
title: IP address mapping rules - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration
---

# IP address mapping rules - GET configuration

# IP address mapping rules - GET configuration

* Reference
* Обновлено 21 июл. 2026

Устарело

Данный API endpoint устарел. Используйте вместо него [схему Map IP addresses to locations](/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-mappings "View builtin:rum.ip-mappings settings schema table of your monitoring environment via the Dynatrace API.").

Возвращает конфигурацию сопоставления IP-адресов с географическими регионами.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Аутентификация

Для выполнения запроса нужен токен доступа с областью `ReadConfig`.

Подробнее о получении и использовании токена см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не принимает настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [IpAddressMappings](#openapi-definition-IpAddressMappings) | Успех |

### Объекты тела ответа

#### Объект `IpAddressMappings`

Конфигурация сопоставления IP-адресов с географическими локациями.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule](#openapi-definition-IpAddressMappingRule)[] | Список правил сопоставления IP-адресов. Правила оцениваются сверху вниз, применяется первое совпавшее правило. |

#### Объект `IpAddressMappingRule`

Конфигурация сопоставления IP-адреса с географической локацией.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | Локация для сопоставления IP-адреса. |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | IP-адрес или диапазон IP-адресов для сопоставления с локацией. |

#### Объект `IpAddressMappingLocation`

Локация для сопоставления IP-адреса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Название города локации. |
| countryCode | string | Код страны локации. Чтобы получить список доступных кодов стран, используйте запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| latitude | number | Широта локации в формате `DDD.dddd`. |
| longitude | number | Долгота локации в формате `DDD.dddd`. |
| regionCode | string | Код региона локации. Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов для сопоставления с локацией.

| Элемент | Тип | Описание |
| --- | --- | --- |
| address | string | IP-адрес для сопоставления. Для диапазона IP-адресов это адрес **from**. |
| addressTo | string | Адрес **to** диапазона IP-адресов. |
| subnetMask | integer | Маска подсети диапазона IP-адресов. |

### Модели JSON тела ответа

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

## Связанные темы

* [Map internal IP addresses to locations for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace на использование локальных адресов для определения местоположения пользователей ваших веб-приложений.")
* [Map internal IP addresses to locations for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Настройте Dynatrace на использование локальных адресов для определения местоположения пользователей ваших мобильных приложений.")
* [Map internal IP addresses to locations for custom applications in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace на использование локальных адресов для определения местоположения пользователей ваших пользовательских приложений.")