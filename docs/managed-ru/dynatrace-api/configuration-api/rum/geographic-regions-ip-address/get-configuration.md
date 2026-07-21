---
title: IP address mapping rules - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration
---

# IP address mapping rules - GET configuration

# IP address mapping rules - GET configuration

* Справка
* Опубликовано 24 сентября 2020 г.

Получает конфигурацию сопоставления между IP-адресами и географическими регионами.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со scope `ReadConfig`.

О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предоставляет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [IpAddressMappings](#openapi-definition-IpAddressMappings) | Успех |

### Объекты тела ответа

#### Объект `IpAddressMappings`

Конфигурация сопоставлений IP-адресов с географическими местоположениями.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule](#openapi-definition-IpAddressMappingRule)[] | Список правил сопоставления IP-адресов.  Правила проверяются сверху вниз, применяется первое подходящее правило. |

#### Объект `IpAddressMappingRule`

Конфигурация сопоставления IP-адреса с географическим местоположением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | Местоположение для сопоставления IP-адреса. |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением. |

#### Объект `IpAddressMappingLocation`

Местоположение для сопоставления IP-адреса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Название города местоположения. |
| countryCode | string | Код страны местоположения.  Чтобы получить список доступных кодов стран, используй запрос [GET all countries﻿](https://dt-url.net/37030go?dt=m). |
| latitude | number | Широта местоположения в формате `DDD.dddd`. |
| longitude | number | Долгота местоположения в формате `DDD.dddd`. |
| regionCode | string | Код региона местоположения.  Чтобы получить список доступных кодов регионов, используй запрос [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m). |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов, сопоставляемый с местоположением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| address | string | Сопоставляемый IP-адрес.  Для диапазона IP-адресов это адрес **from** (начальный). |
| addressTo | string | Адрес **to** (конечный) диапазона IP-адресов. |
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

* [Map internal IP addresses to locations for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Map internal IP addresses to locations for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")
* [Map internal IP addresses to locations for custom applications in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")