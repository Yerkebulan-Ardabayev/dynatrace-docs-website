---
title: IP address mapping rules - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration
scraped: 2026-05-12T11:18:01.412511
---

# IP address mapping rules - GET configuration

# IP address mapping rules - GET configuration

* Reference
* Published Sep 24, 2020

Возвращает конфигурацию сопоставления между IP-адресами и географическими регионами.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [IpAddressMappings](#openapi-definition-IpAddressMappings) | Успех |

### Объекты тела ответа

#### Объект `IpAddressMappings`

Конфигурация сопоставлений IP-адресов с географическими расположениями.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule[]](#openapi-definition-IpAddressMappingRule) | Список правил сопоставления IP-адресов.  Правила оцениваются сверху вниз; применяется первое подходящее правило. |

#### Объект `IpAddressMappingRule`

Конфигурация сопоставления IP-адреса с географическим расположением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | Расположение для сопоставления IP-адреса. |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | IP-адрес или диапазон IP-адресов для сопоставления с расположением. |

#### Объект `IpAddressMappingLocation`

Расположение для сопоставления IP-адреса.

| Элемент | Тип | Описание |
| --- | --- | --- |
| city | string | Название города расположения. |
| countryCode | string | Код страны расположения.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go). |
| latitude | number | Широта расположения в формате `DDD.dddd`. |
| longitude | number | Долгота расположения в формате `DDD.dddd`. |
| regionCode | string | Код региона расположения.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0). |

#### Объект `IpAddressRange`

IP-адрес или диапазон IP-адресов для сопоставления с расположением.

| Элемент | Тип | Описание |
| --- | --- | --- |
| address | string | IP-адрес для сопоставления.  Для диапазона IP-адресов это адрес **from**. |
| addressTo | string | Адрес **to** диапазона IP-адресов. |
| subnetMask | integer | Маска подсети диапазона IP-адресов. |

### JSON-модели тела ответа

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

* [Сопоставление внутренних IP-адресов с расположениями для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших веб-приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших мобильных приложений.")
* [Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших пользовательских приложений.")