---
title: Settings API - Map IP addresses to locations schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-mappings
scraped: 2026-05-12T11:42:50.757466
---

# Settings API - Map IP addresses to locations schema table

# Settings API - Map IP addresses to locations schema table

* Published Dec 05, 2023

### Сопоставление IP-адресов с локациями (`builtin:rum.ip-mappings)`

Если на карте мира нет данных производительности для части клиентов, причина может быть в том, что у этих клиентов приватные IP-адреса. Можно сопоставить такие приватные IP-адреса с географическими регионами, чтобы они стали видны на карте. При необходимости можно даже переопределить настройки для IP-адресов клиентов.

Гранулярность регионального анализа производительности растёт по мере увеличения количества обнаруженных пользовательских запросов в конкретном регионе (континент, страна, штат или город). При необходимости можно переопределить автоматически обнаруженные IP-адреса для повышения точности сопоставления.

Dynatrace использует сервис сопоставления IP-адресов с геолокацией от [MaxMind GeoIP2](https://dt-url.net/6a21pxd). Имена регионов и городов следуют [GeoNames database](https://dt-url.net/tz41pwz).
Чтобы узнать какие имена и ID используются «из коробки», воспользуйтесь geographic regions REST API (`<your-dynatrace-url>//rest-api-doc/index.jsp?urls.primaryName=Environment%20API%20v2#/Geographic%20regions`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.ip-mappings` | * `group:web-and-mobile-monitoring.geographic-regions` * `group:web-and-mobile-monitoring` | `environment` |

Получить schema через Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-mappings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.ip-mappings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-mappings` |

## Аутентификация

Для выполнения запроса необходим access token со scope **Read settings** (`settings.read`). О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Свойство | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| Один IP или начальный адрес диапазона `ip` | text | - | Required |
| Конец диапазона IP `ipTo` | text | - | Optional |
| Страна `countryCode` | text | Код страны локации.  Используйте alpha-2-код [ISO 3166-2 standard](https://dt-url.net/iso3166-2) (например, `AT` для Австрии или `PL` для Польши). | Required |
| Регион `regionCode` | text | Код региона локации.  Для [USA](https://dt-url.net/iso3166us) и [Canada](https://dt-url.net/iso3166ca) используйте коды штатов ISO 3166-2 без префиксов `US-` или `CA-`.  Для остального мира используйте [FIPS 10-4 codes](https://dt-url.net/fipscodes) без префикса страны. | Optional |
| Город `city` | text | Имя города локации. | Optional |
| Широта `latitude` | float | - | Required |
| Долгота `longitude` | float | - | Required |