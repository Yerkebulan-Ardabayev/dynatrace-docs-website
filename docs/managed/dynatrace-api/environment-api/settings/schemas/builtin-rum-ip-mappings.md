---
title: Settings API - Map IP addresses to locations schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-ip-mappings
---

# Settings API - Map IP addresses to locations schema table

# Settings API - Map IP addresses to locations schema table

* Published Dec 05, 2023

### Map IP addresses to locations (`builtin:rum.ip-mappings)`

If you don't see performance data for some of your customers on the world map, it may be because those customers have private IP addresses. You can map such private IP addresses to geographic regions to make them visible on the map. You can even override settings for customer IP addresses if necessary for mapping purposes.

Granularity of regional performance analysis increases as the number of detected user requests goes up in a specific region (continent, country, state, or city). You can even override auto-detected IP addresses if necessary to improve mapping accuracy.

Dynatrace uses an IP address to geolocation mapping service offered by [MaxMind GeoIP2﻿](https://dt-url.net/6a21pxd). The names for regions and cities are following the [GeoNames database﻿](https://dt-url.net/tz41pwz).
To find out which names and IDs are used out of the box, use the geographic regions REST API (`<your-dynatrace-url>//rest-api-doc/index.jsp?urls.primaryName=Environment%20API%20v2#/Geographic%20regions`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.ip-mappings` | * `group:web-and-mobile-monitoring.geographic-regions` * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-mappings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.ip-mappings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.ip-mappings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Single IP or IP range start address `ip` | text | - | Required |
| IP range end `ipTo` | text | - | Optional |
| Country `countryCode` | text | The country code of the location.  Use the alpha-2 code of the [ISO 3166-2 standard﻿](https://dt-url.net/iso3166-2), (for example, `AT` for Austria or `PL` for Poland). | Required |
| Region `regionCode` | text | The region code of the location.  For the [USA﻿](https://dt-url.net/iso3166us) or [Canada﻿](https://dt-url.net/iso3166ca) use ISO 3166-2 state codes without `US-` or `CA-` prefix.  For the rest of the world use [FIPS 10-4 codes﻿](https://dt-url.net/fipscodes) without country prefix. | Optional |
| City `city` | text | The city name of the location. | Optional |
| Latitude `latitude` | float | - | Required |
| Longitude `longitude` | float | - | Required |