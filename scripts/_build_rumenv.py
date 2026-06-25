# -*- coding: utf-8 -*-
"""L4Y builder: environment-api/rum/ = 24 files (geographic-regions parent + 5
GET endpoints, real-user-monitoring-javascript-code parent + 7 GET, rum-cookie-
names, rum-manual-insertion-tags parent + 3 GET, user-sessions parent + table/
tree/user-session-structure).

Splice method (L98/L100/L4O/L4X): start from EN, CRLF->LF, normalize double-
encoded mojibake (U+00E2 + 2 C1 chars) + strip BOM (L4M), apply per-file then
COMMON ordered exact-string canon (longest/most-specific FIRST, L4T) -> byte-
identical JSON/code-fence + automatic line parity. Anything unreplaced stays
EN-verbatim (object/enum/JSON/scope, L99).

FIRST L4-era env-api batch -> anchor to freshest L99 canon (NOT pre-L99
events-v2): both H1 EN-verbatim, `* Reference`/`* Updated on`/`* Published`
EN-verbatim, `#### Curl` EN, "The element can hold these values" ->
"Возможные значения:" WITH colon. Boilerplate phrasing verified against
events-v2 RU. Related-topics link-text = actual target RU H1 verbatim (L4O/L4L);
`Tokens and authentication` link-text stays EN (corpus 188:40, L87/L4S).

mojibake here (verified by codepoint scan): U+2014 em-dash double-encoded
(e2 80 94) only in user-sessions.md / tree.md PROSE (no code fence) -> safe to
normalize; sentence translated wholesale anyway (CLAUDE#0 no em-dash). 3-byte
BOM `ï»¿` in inline link-text -> stripped. `GdaÅ\x84sk` (U+0144, c5 84) lives
ONLY inside ``` JSON fences ``` -> NOT touched by the e2-only normalizer, stays
byte-verbatim (never translate code fences). No `~~strikethrough~~` enum row;
single `DEPRECATED ` prefix in user-session-structure totalBlockingTime cell."""

import os, io

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
EN = os.path.join(ROOT, r"docs\managed\dynatrace-api\environment-api\rum")
RU = os.path.join(ROOT, r"docs\managed-ru\dynatrace-api\environment-api\rum")

FILES = [
    "geographic-regions.md",
    "geographic-regions/get-cities-country.md",
    "geographic-regions/get-cities-region.md",
    "geographic-regions/get-countries.md",
    "geographic-regions/get-regions-country.md",
    "geographic-regions/get-regions.md",
    "real-user-monitoring-javascript-code.md",
    "real-user-monitoring-javascript-code/get-available-rum-javascript-versions.md",
    "real-user-monitoring-javascript-code/get-configured-rum-javascript-versions.md",
    "real-user-monitoring-javascript-code/get-current-version.md",
    "real-user-monitoring-javascript-code/get-list-injected-applications.md",
    "real-user-monitoring-javascript-code/get-most-recent-version.md",
    "real-user-monitoring-javascript-code/get-snippet-async.md",
    "real-user-monitoring-javascript-code/get-snippet-sync.md",
    "rum-cookie-names-get-cookie-names.md",
    "rum-manual-insertion-tags.md",
    "rum-manual-insertion-tags/get-inline-code.md",
    "rum-manual-insertion-tags/get-javascript-tag.md",
    "rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri.md",
    "rum-manual-insertion-tags/get-oneagent-javascript-tag.md",
    "user-sessions.md",
    "user-sessions/table.md",
    "user-sessions/tree.md",
    "user-sessions/user-session-structure.md",
]


def _normalize(t):
    """Pure-ASCII source code: build fragile mojibake/BOM keys from codepoints
    so the literals never collapse on Write/Edit (L4X lesson 1)."""
    t = t.replace("\r\n", "\n")  # EN is CRLF; RU corpus convention is LF
    e2 = chr(0xE2)  # U+00E2; double-encoded unit = e2 + 2 C1 chars (L4W)
    for c1, c2, repl in (
        (0x80, 0x99, "'"),  # U+2019 right single quote / apostrophe
        (0x80, 0x98, "'"),  # U+2018 left single quote
        (0x80, 0x9C, '"'),  # U+201C left double quote (harmless if absent)
        (0x80, 0x9D, '"'),  # U+201D right double quote (harmless if absent)
        (0x80, 0x93, "-"),  # U+2013 en dash (harmless if absent)
        (0x80, 0x94, "-"),  # U+2014 em dash (only in user-sessions/tree prose)
    ):
        t = t.replace(e2 + chr(c1) + chr(c2), repl)
    t = t.replace(chr(0xFEFF), "")  # real BOM
    t = t.replace(chr(0xEF) + chr(0xBB) + chr(0xBF), "")  # 3-byte BOM (L4M)
    return t


# ---------------------------------------------------------------- COMMON
# Applied AFTER per-file. Each entry is within-line (or newline-anchored
# heading) => line-parity preserved. Ordered longest/most-specific FIRST to
# avoid substring collisions (L4T: generic before specific = EN/RU hybrid).
COMMON = [
    # --- structural headings (newline-anchored: "## Response" must not match
    #     inside "### Response codes") ---
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n## Example\n", "\n## Пример\n"),
    ("\n#### Request URL\n", "\n#### URL запроса\n"),
    ("\n#### Response body\n", "\n#### Тело ответа\n"),
    ("\n#### Response code\n", "\n#### Код ответа\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # `#### Curl` => EN-verbatim (L99 ALLOWED_EN)
    # --- table headers ---
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    # --- object headings -> #### Объект `X` (EN-lock backtick names; longer
    #     names first, defensively) ---
    (
        "#### The `CountryWithRegionsWithCities` object",
        "#### Объект `CountryWithRegionsWithCities`",
    ),
    (
        "#### The `CountryListWithRegions` object",
        "#### Объект `CountryListWithRegions`",
    ),
    ("#### The `RegionWithCities` object", "#### Объект `RegionWithCities`"),
    ("#### The `CountryWithRegions` object", "#### Объект `CountryWithRegions`"),
    ("#### The `AllAvailableVersions` object", "#### Объект `AllAvailableVersions`"),
    ("#### The `ConfiguredVersions` object", "#### Объект `ConfiguredVersions`"),
    ("#### The `ManualApplication` object", "#### Объект `ManualApplication`"),
    ("#### The `UsqlResultAsTable` object", "#### Объект `UsqlResultAsTable`"),
    ("#### The `UsqlResultAsTree` object", "#### Объект `UsqlResultAsTree`"),
    ("#### The `CountryRegions` object", "#### Объект `CountryRegions`"),
    ("#### The `ResponseBody` object", "#### Объект `ResponseBody`"),
    ("#### The `CountryList` object", "#### Объект `CountryList`"),
    ("#### The `CookieNames` object", "#### Объект `CookieNames`"),
    ("#### The `AnyValue` object", "#### Объект `AnyValue`"),
    ("#### The `Country` object", "#### Объект `Country`"),
    ("#### The `Region` object", "#### Объект `Region`"),
    ("#### The `City` object", "#### Объект `City`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    # --- shared boilerplate prose (L99; events-v2 RU phrasing verified) ---
    (
        "To execute this request, you need an access token with `geographicRegions.read` scope.",
        "Для выполнения запроса необходим access token со scope `geographicRegions.read`.",
    ),
    (
        "To execute this request, you need an access token with `RumJavaScriptTagManagement` scope.",
        "Для выполнения запроса необходим access token со scope `RumJavaScriptTagManagement`.",
    ),
    (
        "To execute this request, you need an access token with `rumManualInsertionTags.read` scope.",
        "Для выполнения запроса необходим access token со scope `rumManualInsertionTags.read`.",
    ),
    (
        "To execute this request, you need an access token with `rumCookieNames.read` scope.",
        "Для выполнения запроса необходим access token со scope `rumCookieNames.read`.",
    ),
    (
        "To execute this request, you need an access token with `DTAQLAccess` scope.",
        "Для выполнения запроса необходим access token со scope `DTAQLAccess`.",
    ),
    (
        "To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "О том, как получить и использовать токен, см. [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    # entity `| entity |` param-cell description: byte-identical EN (post-BOM-
    # strip) shared by get-current-version + get-snippet-async + get-snippet-
    # sync. In COMMON so all 3 render the identical RU cell. Longest-form, no
    # collision: get-list-injected's `...application. |` has no "You can obtain"
    # tail; user-session-structure's "...application.  This information" differs.
    (
        "The Dynatrace entity ID of the application.  You can obtain it from the response of the [GET the list of manually injected applications](https://dt-url.net/dl03sgo) call.",
        "ID сущности Dynatrace приложения.  Его можно получить из ответа вызова [GET the list of manually injected applications](https://dt-url.net/dl03sgo).",
    ),
    (
        "The request doesn't provide any configurable parameters.",
        "Запрос не предоставляет настраиваемых параметров.",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает данные в формате `application/json`.",
    ),
    (
        "The request produces a `text/plain` payload.",
        "Запрос возвращает данные в формате `text/plain`.",
    ),
    (
        "The API token is passed in the **Authorization** header.",
        "API-токен передаётся в заголовке **Authorization**.",
    ),
    # --- response-code description cells (longest/most-specific first; L101:
    #     trailing period stays OUTSIDE the matched span -> source-faithful) ---
    (
        "Success. The response contains the list of country's cities.",
        "Успех. Ответ содержит список городов страны.",
    ),
    (
        "Success. The response contains the list of region's cities.",
        "Успех. Ответ содержит список городов региона.",
    ),
    (
        "Success. The response contains the list of country's regions.",
        "Успех. Ответ содержит список регионов страны.",
    ),
    (
        "Success. The response contains the list of countries with regional divisions.",
        "Успех. Ответ содержит список стран с разбивкой по регионам.",
    ),
    (
        "Success. The response contains the list of countries.",
        "Успех. Ответ содержит список стран.",
    ),
    (
        "Success. The response contains all RUM cookie names",
        "Успех. Ответ содержит все имена cookie RUM",
    ),
    (
        "Success. The response contains the result of the query.",
        "Успех. Ответ содержит результат запроса.",
    ),
    (
        "The data structure of the user session. This response code is never returned.",
        "Структура данных пользовательской сессии. Этот код ответа никогда не возвращается.",
    ),
    (
        "Failed. The requested resource doesn't exist.",
        "Сбой. Запрашиваемый ресурс не существует.",
    ),
    (
        "Failed. The query is invalid. See the response body for more information.",
        "Сбой. Запрос некорректен. Подробности см. в теле ответа.",
    ),
    ("Failed. The query is missing.", "Сбой. Запрос отсутствует."),
    ("Client side error.", "Ошибка на стороне клиента."),
    ("Server side error.", "Ошибка на стороне сервера."),
    ("| Success |", "| Успех |"),
    # --- shared Error / ConstraintViolation object cells (verbatim canon) ---
    (
        "| code | integer | The HTTP status code |",
        "| code | integer | HTTP-код состояния |",
    ),
    (
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |",
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |",
    ),
    (
        "| message | string | The error message |",
        "| message | string | Сообщение об ошибке |",
    ),
    # ConstraintViolation object-intro standalone line
    ("\nA list of constraint violations\n", "\nСписок нарушений ограничений\n"),
    # --- "The element can hold these values" -> "Возможные значения:" WITH
    #     colon (L99; also handles leading-dash `-The element ...`) ---
    ("The element can hold these values", "Возможные значения:"),
    # --- Related-topics title-attrs + link-text = target RU H1 (L4O/L4L) ---
    (
        '[Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")',
        '[Мониторинг реальных пользователей](/managed/observe/digital-experience/rum-concepts/rum-overview "Узнайте о Real User Monitoring, ключевых метриках производительности, мониторинге мобильных приложений и многом другом.")',
    ),
    (
        '[Detection of IP addresses, geolocations, and user agents](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")',
        '[Определение IP-адресов, геолокаций и user agent\'ов](/managed/observe/digital-experience/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace определяет IP-адреса и геолокации (город, регион, страну), а также браузеры, устройства и операционные системы.")',
    ),
    (
        '[Custom queries, segmentation, and aggregation of session data](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.")',
        '[Пользовательские запросы, сегментация и агрегация данных сессий](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как обращаться к данным пользовательских сессий и запрашивать их с помощью ключевых слов, синтаксиса, функций и многого другого.")',
    ),
    (
        '[Cookies and client-side storage for RUM and Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Learn how Dynatrace RUM and Session Replay use cookies, web storage, and IndexedDB.")',
        '[Cookie и клиентское хранилище для RUM и Session Replay](/managed/manage/data-privacy-and-security/data-privacy/rum-cookies-and-web-storage "Узнайте, как Dynatrace RUM и Session Replay используют cookie, веб-хранилище и IndexedDB.")',
    ),
]

# ---------------------------------------------------------------- PER-FILE
# Long/unique strings; applied BEFORE COMMON. Authored longest-first.
P = {}

# ---- geographic-regions (parent) ----
P["geographic-regions.md"] = [
    (
        'Get an overview of countries and their codes.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-countries "View countries via Geographic regions API.")',
        'Обзор стран и их кодов.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-countries "Просмотр стран через Geographic regions API.")',
    ),
    (
        'Get an overview of countries with a region breakdown.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-regions "View regions via Geographic regions API.")',
        'Обзор стран с разбивкой по регионам.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-regions "Просмотр регионов через Geographic regions API.")',
    ),
    (
        'Get an overview of regions within a country.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-regions-country "View regions in a country via Geographic regions API.")',
        'Обзор регионов внутри страны.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-regions-country "Просмотр регионов страны через Geographic regions API.")',
    ),
    (
        'Get an overview of cities within a country.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-cities-country "View cities in a country via Geographic regions API.")',
        'Обзор городов внутри страны.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-cities-country "Просмотр городов страны через Geographic regions API.")',
    ),
    (
        'Get an overview of cities within a region.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-cities-region "View cities of a region via Geographic regions API.")',
        'Обзор городов внутри региона.](/managed/dynatrace-api/environment-api/rum/geographic-regions/get-cities-region "Просмотр городов региона через Geographic regions API.")',
    ),
    ("[### List countries\n", "[### Список стран\n"),
    ("[### List regions of a country\n", "[### Список регионов страны\n"),
    ("[### List regions\n", "[### Список регионов\n"),
    ("[### List cities of a country\n", "[### Список городов страны\n"),
    ("[### List cities of a region\n", "[### Список городов региона\n"),
]

# ---- geographic-regions/get-countries ----
P["geographic-regions/get-countries.md"] = [
    ("Lists countries and their codes.", "Выводит список стран и их кодов."),
    (
        "| countries | [Country[]](#openapi-definition-Country) | The list of countries. |",
        "| countries | [Country[]](#openapi-definition-Country) | Список стран. |",
    ),
    (
        "| countryCount | integer | The number of countries. |",
        "| countryCount | integer | Количество стран. |",
    ),
    ("\nThe list of countries.\n", "\nСписок стран.\n"),
    ("Information about a country.", "Информация о стране."),
    (
        "| code | string | The ISO code of the country. |",
        "| code | string | ISO-код страны. |",
    ),
    (
        "| name | string | The name of the country. |",
        "| name | string | Название страны. |",
    ),
]

# ---- geographic-regions/get-regions ----
P["geographic-regions/get-regions.md"] = [
    (
        "Lists countries and their regions.",
        "Выводит список стран и их регионов.",
    ),
    (
        "A list of countries with their regions.",
        "Список стран с их регионами.",
    ),
    (
        "| countries | [CountryRegions[]](#openapi-definition-CountryRegions) | The list of countries. |",
        "| countries | [CountryRegions[]](#openapi-definition-CountryRegions) | Список стран. |",
    ),
    (
        "| countryCount | integer | The number of countries. |",
        "| countryCount | integer | Количество стран. |",
    ),
    (
        "| regions | [Region[]](#openapi-definition-Region) | The list of regions in the country. |",
        "| regions | [Region[]](#openapi-definition-Region) | Список регионов страны. |",
    ),
    (
        "| regionCount | integer | The number of regions in the country. |",
        "| regionCount | integer | Количество регионов в стране. |",
    ),
    ("Information about a country.", "Информация о стране."),
    ("Information about a country's region.", "Информация о регионе страны."),
    (
        "| code | string | The ISO code of the country. |",
        "| code | string | ISO-код страны. |",
    ),
    (
        "| name | string | The name of the country. |",
        "| name | string | Название страны. |",
    ),
    (
        "| code | string | The code of the region. |",
        "| code | string | Код региона. |",
    ),
    (
        "| name | string | The name of the region. |",
        "| name | string | Название региона. |",
    ),
]

# ---- geographic-regions/get-regions-country ----
P["geographic-regions/get-regions-country.md"] = [
    ("Lists regions of a country.", "Выводит список регионов страны."),
    (
        "The ISO code of the required country.  To fetch the list of available country codes, use the [GET all countries](https://dt-url.net/37030go) request.",
        "ISO-код требуемой страны.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go).",
    ),
    (
        "| regions | [Region[]](#openapi-definition-Region) | The list of regions in the country. |",
        "| regions | [Region[]](#openapi-definition-Region) | Список регионов страны. |",
    ),
    (
        "| regionCount | integer | The number of regions in the country. |",
        "| regionCount | integer | Количество регионов в стране. |",
    ),
    ("Information about a country.", "Информация о стране."),
    ("Information about a country's region.", "Информация о регионе страны."),
    (
        "| countryCode | string | The ISO code of the country. |",
        "| countryCode | string | ISO-код страны. |",
    ),
    (
        "| countryName | string | The name of the country. |",
        "| countryName | string | Название страны. |",
    ),
    (
        "| code | string | The code of the region. |",
        "| code | string | Код региона. |",
    ),
    (
        "| name | string | The name of the region. |",
        "| name | string | Название региона. |",
    ),
]

# ---- geographic-regions/get-cities-country ----
P["geographic-regions/get-cities-country.md"] = [
    (
        "Lists regions and cities of a country.",
        "Выводит список регионов и городов страны.",
    ),
    (
        "The ISO code of the required country.  To fetch the list of available country codes, use the [GET all countries](https://dt-url.net/37030go) request.",
        "ISO-код требуемой страны.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go).",
    ),
    (
        "Information about a country's region and its cities.",
        "Информация о регионе страны и его городах.",
    ),
    (
        "| regions | [RegionWithCities[]](#openapi-definition-RegionWithCities) | The list of regions in the country. |",
        "| regions | [RegionWithCities[]](#openapi-definition-RegionWithCities) | Список регионов страны. |",
    ),
    (
        "| regionCount | integer | The number of regions in the country. |",
        "| regionCount | integer | Количество регионов в стране. |",
    ),
    (
        "| cities | [City[]](#openapi-definition-City) | The list of cities in the region. |",
        "| cities | [City[]](#openapi-definition-City) | Список городов региона. |",
    ),
    (
        "| cityCount | integer | The number of cities in a region of a country. |",
        "| cityCount | integer | Количество городов в регионе страны. |",
    ),
    ("Information about a country.", "Информация о стране."),
    ("Information about a city.", "Информация о городе."),
    (
        "| countryCode | string | The ISO code of the country. |",
        "| countryCode | string | ISO-код страны. |",
    ),
    (
        "| countryName | string | The name of the country. |",
        "| countryName | string | Название страны. |",
    ),
    (
        "| code | string | The code of the region. |",
        "| code | string | Код региона. |",
    ),
    (
        "| name | string | The name of the region. |",
        "| name | string | Название региона. |",
    ),
    (
        "| latitude | number | The latitude of the city. |",
        "| latitude | number | Широта города. |",
    ),
    (
        "| longitude | number | The longitude of the city. |",
        "| longitude | number | Долгота города. |",
    ),
    (
        "| name | string | The name of the city. |",
        "| name | string | Название города. |",
    ),
]

# ---- geographic-regions/get-cities-region ----
P["geographic-regions/get-cities-region.md"] = [
    ("Lists cities of a region.", "Выводит список городов региона."),
    (
        "The ISO code of the required country.  To fetch the list of available country codes, use the [GET all countries](https://dt-url.net/37030go) request.",
        "ISO-код требуемой страны.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go).",
    ),
    (
        "The code of the required region.  To fetch the list of available region codes, use the [GET regions of the country](https://dt-url.net/az230x0) request.",
        "Код требуемого региона.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0).",
    ),
    (
        "Information about a country's region and its cities.",
        "Информация о регионе страны и его городах.",
    ),
    (
        "| regions | [RegionWithCities[]](#openapi-definition-RegionWithCities) | The list of regions in the country. |",
        "| regions | [RegionWithCities[]](#openapi-definition-RegionWithCities) | Список регионов страны. |",
    ),
    (
        "| regionCount | integer | The number of regions in the country. |",
        "| regionCount | integer | Количество регионов в стране. |",
    ),
    (
        "| cities | [City[]](#openapi-definition-City) | The list of cities in the region. |",
        "| cities | [City[]](#openapi-definition-City) | Список городов региона. |",
    ),
    (
        "| cityCount | integer | The number of cities in a region of a country. |",
        "| cityCount | integer | Количество городов в регионе страны. |",
    ),
    ("Information about a country.", "Информация о стране."),
    ("Information about a city.", "Информация о городе."),
    (
        "| countryCode | string | The ISO code of the country. |",
        "| countryCode | string | ISO-код страны. |",
    ),
    (
        "| countryName | string | The name of the country. |",
        "| countryName | string | Название страны. |",
    ),
    (
        "| code | string | The code of the region. |",
        "| code | string | Код региона. |",
    ),
    (
        "| name | string | The name of the region. |",
        "| name | string | Название региона. |",
    ),
    (
        "| latitude | number | The latitude of the city. |",
        "| latitude | number | Широта города. |",
    ),
    (
        "| longitude | number | The longitude of the city. |",
        "| longitude | number | Долгота города. |",
    ),
    (
        "| name | string | The name of the city. |",
        "| name | string | Название города. |",
    ),
]

# ---- real-user-monitoring-javascript-code (parent) ----
P["real-user-monitoring-javascript-code.md"] = [
    (
        "The **Real User Monitoring JavaScript API** helps you to set up and maintain your manually injected applications.",
        "API **Real User Monitoring JavaScript** помогает настраивать и сопровождать ваши приложения с ручным внедрением.",
    ),
    (
        'The endpoints for retrieving manual insertion tags in formats other than [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case") have been deprecated. For these formats, use the newer [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API").',
        'Эндпоинты для получения тегов ручного внедрения в форматах, отличных от [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария."), устарели. Для этих форматов используйте более новый [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Узнайте, как загружать теги ручного внедрения RUM через API").',
    ),
    (
        'Fetch detailed information about your existing manually injected applications.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Fetch the list of applications with manually inject OneAgent JavaScript.")',
        'Получить подробную информацию о ваших существующих приложениях с ручным внедрением.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Получить список приложений с вручную внедрённым OneAgent JavaScript.")',
    ),
    (
        'Fetch a list of all available versions of the RUM JavaScript.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-available-rum-javascript-versions "Fetch a list of all available versions of the RUM JavaScript.")',
        'Получить список всех доступных версий RUM JavaScript.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-available-rum-javascript-versions "Получить список всех доступных версий RUM JavaScript.")',
    ),
    (
        'Check the configured latest stable, previous stable, and custom RUM JavaScript versions.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-configured-rum-javascript-versions "Check the configured latest stable, previous stable and custom RUM JavaScript versions.")',
        'Проверить настроенные последнюю стабильную, предыдущую стабильную и пользовательскую версии RUM JavaScript.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-configured-rum-javascript-versions "Проверьте настроенные последнюю стабильную, предыдущую стабильную и пользовательскую версии RUM JavaScript.")',
    ),
    (
        'Check the most recent version of the Real User Monitoring JavaScript.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-most-recent-version "View the most recent version of the RUM JavaScript injected to an application.")',
        'Проверить самую последнюю версию Real User Monitoring JavaScript.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-most-recent-version "Просмотр самой последней версии RUM JavaScript, внедрённой в приложение.")',
    ),
    (
        'Check the most recent version of the Real User Monitoring JavaScript you\'re using.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-current-version "View the current version of the RUM JavaScript injected to an application.")',
        'Проверить самую последнюю версию Real User Monitoring JavaScript, которую вы используете.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-current-version "Просмотр текущей версии RUM JavaScript, внедрённой в приложение.")',
    ),
    (
        'Obtain the most recent Real User Monitoring JavaScript as a code snippet for the synchronous load.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync "Retrieve the synchronous code snippet of RUM JavaScript.")',
        'Получить самый последний Real User Monitoring JavaScript в виде фрагмента кода для синхронной загрузки.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync "Получить синхронный фрагмент кода RUM JavaScript.")',
    ),
    (
        'Obtain the most recent Real User Monitoring JavaScript as a code snippet for the deferred load.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async "Retrieve the asynchronous code snippet of RUM JavaScript.")',
        'Получить самый последний Real User Monitoring JavaScript в виде фрагмента кода для отложенной загрузки.](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async "Получить асинхронный фрагмент кода RUM JavaScript.")',
    ),
    ("[### List injected applications\n", "[### Список внедрённых приложений\n"),
    ("[### List available versions\n", "[### Список доступных версий\n"),
    ("[### Check configured versions\n", "[### Проверка настроенных версий\n"),
    ("[### Check latest version\n", "[### Проверка последней версии\n"),
    ("[### Check your version\n", "[### Проверка вашей версии\n"),
    ("[### Get synchronous code snippet\n", "[### Получить синхронный фрагмент кода\n"),
    (
        "[### Get asynchronous code snippet\n",
        "[### Получить асинхронный фрагмент кода\n",
    ),
]

# ---- real-user-monitoring-javascript-code/get-available-rum-javascript-versions ----
P["real-user-monitoring-javascript-code/get-available-rum-javascript-versions.md"] = [
    (
        "Fetch a list of all versions of the RUM JavaScript that are available on the environment.",
        "Получить список всех версий RUM JavaScript, доступных в окружении.",
    ),
    ("All available RUM JavaScript versions", "Все доступные версии RUM JavaScript"),
    (
        "| versions | integer[] | A list of available RUM JavaScript versions |",
        "| versions | integer[] | Список доступных версий RUM JavaScript |",
    ),
    (
        "In this example, the request inquires the available RUM JavaScript versions.",
        "В этом примере запрос запрашивает доступные версии RUM JavaScript.",
    ),
]

# ---- real-user-monitoring-javascript-code/get-configured-rum-javascript-versions ----
P["real-user-monitoring-javascript-code/get-configured-rum-javascript-versions.md"] = [
    (
        "Returns the latest stable, previous stable, and custom RUM JavaScript versions configured on the environment.",
        "Возвращает настроенные в окружении последнюю стабильную, предыдущую стабильную и пользовательскую версии RUM JavaScript.",
    ),
    (
        "Configured LATEST\\_STABLE, PREVIOUS\\_STABLE and CUSTOM RUM JavaScript versions.",
        "Настроенные версии RUM JavaScript LATEST\\_STABLE, PREVIOUS\\_STABLE и CUSTOM.",
    ),
    (
        "| custom | integer | The custom configured version of the RUM JavaScript. |",
        "| custom | integer | Пользовательская настроенная версия RUM JavaScript. |",
    ),
    (
        "| latestIE11Supported | integer | The latest IE11 supported version of the RUM JavaScript. |",
        "| latestIE11Supported | integer | Последняя версия RUM JavaScript с поддержкой IE11. |",
    ),
    (
        "| latestIESupported | integer | The latest IE7-10 supported version of the RUM JavaScript. |",
        "| latestIESupported | integer | Последняя версия RUM JavaScript с поддержкой IE7-10. |",
    ),
    (
        "| latestStable | integer | The latest stable version of the RUM JavaScript. |",
        "| latestStable | integer | Последняя стабильная версия RUM JavaScript. |",
    ),
    (
        "| previousStable | integer | The previous stable version of the RUM JavaScript. |",
        "| previousStable | integer | Предыдущая стабильная версия RUM JavaScript. |",
    ),
    (
        "In this example, the request inquires the versions of the RUM JavaScript configured on the environment.",
        "В этом примере запрос запрашивает настроенные в окружении версии RUM JavaScript.",
    ),
]

# ---- real-user-monitoring-javascript-code/get-current-version ----
P["real-user-monitoring-javascript-code/get-current-version.md"] = [
    (
        "Returns the current version of the Real User Monitoring JavaScript injected into specified application.",
        "Возвращает текущую версию Real User Monitoring JavaScript, внедрённую в указанное приложение.",
    ),
    (
        'The version is a natural number; a higher number indicates a newer version. You can check the most recent available version by executing the [**GET latest version**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Fetch the list of applications with manually inject OneAgent JavaScript.") request.',
        'Версия это натуральное число; большее число означает более новую версию. Проверить самую последнюю доступную версию можно, выполнив запрос [**GET latest version**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Получить список приложений с вручную внедрённым OneAgent JavaScript.").',
    ),
    (
        'If a newer version is available, we recommend you to update the RUM JavaScript in your applications. You can get the most recent RUM JavaScript in different snippet formats, see [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API") for details.',
        'Если доступна более новая версия, рекомендуется обновить RUM JavaScript в ваших приложениях. Самый последний RUM JavaScript можно получить в разных форматах фрагментов, подробнее см. [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Узнайте, как загружать теги ручного внедрения RUM через API").',
    ),
    # entity-cell description moved to COMMON (shared byte-identical by
    # get-current-version + get-snippet-async + get-snippet-sync).
    (
        "The response is a plain text, showing the current RUM JavaScript version.",
        "Ответ это обычный текст, показывающий текущую версию RUM JavaScript.",
    ),
    (
        "In this example, the request inquires the latest version of the RUM JavaScript for the easyTravel Ionic Web application, which has the ID of **APPLICATION-BBFA55551D507E2B**.",
        "В этом примере запрос запрашивает последнюю версию RUM JavaScript для приложения easyTravel Ionic Web, у которого ID **APPLICATION-BBFA55551D507E2B**.",
    ),
]

# ---- real-user-monitoring-javascript-code/get-list-injected-applications ----
P["real-user-monitoring-javascript-code/get-list-injected-applications.md"] = [
    (
        "Lists all of your manually injected applications, along with their metadata.",
        "Выводит список всех ваших приложений с ручным внедрением вместе с их метаданными.",
    ),
    (
        "Parameters of a manually injected application.",
        "Параметры приложения с ручным внедрением.",
    ),
    (
        "| applicationId | string | The Dynatrace entity ID of the application. |",
        "| applicationId | string | ID сущности Dynatrace приложения. |",
    ),
    (
        "| displayName | string | The name of the application. |",
        "| displayName | string | Имя приложения. |",
    ),
    (
        "| monitoringEnabled | boolean | Monitoring is enabled (`true`) or disabled (`false`). |",
        "| monitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`). |",
    ),
    (
        "| revision | string | The application settings revision. |",
        "| revision | string | Ревизия настроек приложения. |",
    ),
    (
        "In this example, the request inquires all the manually injected applications of the environment",
        "В этом примере запрос запрашивает все приложения окружения с ручным внедрением",
    ),
    (
        "The result is truncated to three entries.",
        "Результат усечён до трёх записей.",
    ),
]

# ---- real-user-monitoring-javascript-code/get-most-recent-version ----
P["real-user-monitoring-javascript-code/get-most-recent-version.md"] = [
    (
        "Returns the most recent version of the Real User Monitoring JavaScript available for your environment.",
        "Возвращает самую последнюю версию Real User Monitoring JavaScript, доступную для вашего окружения.",
    ),
    (
        'The version is a natural number, a higher number indicates a newer version. You can check the version you actually use by executing the [**GET the current version of the Real User Monitoring JavaScript**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Fetch the list of applications with manually inject OneAgent JavaScript.") request.',
        'Версия это натуральное число, большее число означает более новую версию. Проверить версию, которую вы фактически используете, можно, выполнив запрос [**GET the current version of the Real User Monitoring JavaScript**](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-list-injected-applications "Получить список приложений с вручную внедрённым OneAgent JavaScript.").',
    ),
    (
        'If a newer version is available, we recommend that you update the RUM JavaScript in your applications. You can get the most recent RUM JavaScript in different snippet formats, see [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API") for details.',
        'Если доступна более новая версия, рекомендуется обновить RUM JavaScript в ваших приложениях. Самый последний RUM JavaScript можно получить в разных форматах фрагментов, подробнее см. [RUM manual insertion tags API](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Узнайте, как загружать теги ручного внедрения RUM через API").',
    ),
    (
        "The response is a plain text, showing the most recent RUM JavaScript version.",
        "Ответ это обычный текст, показывающий самую последнюю версию RUM JavaScript.",
    ),
    (
        "In this example, the request inquires the latest version of the RUM JavaScript, available for the environment.",
        "В этом примере запрос запрашивает последнюю версию RUM JavaScript, доступную для окружения.",
    ),
    (
        "The most recent RUM JavaScript is **10156181011154332**.",
        "Самый последний RUM JavaScript: **10156181011154332**.",
    ),
]

# ---- real-user-monitoring-javascript-code/get-snippet-async ----
P["real-user-monitoring-javascript-code/get-snippet-async.md"] = [
    (
        "Returns the inline script that initializes Dynatrace and dynamically downloads the monitoring code into your application. The monitoring code is loaded asynchronously.",
        "Возвращает встроенный скрипт, который инициализирует Dynatrace и динамически загружает код мониторинга в ваше приложение. Код мониторинга загружается асинхронно.",
    ),
    (
        "You can also use these functionally equivalent options to obtain the RUM JavaScript:",
        "Для получения RUM JavaScript также можно использовать эти функционально эквивалентные варианты:",
    ),
    (
        '* [OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")',
        '* [OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Получить самый последний тег OneAgent JavaScript для ручного внедрения.")',
    ),
    (
        '* [JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.")',
        '* [JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Получить самый последний тег JavaScript для ручного внедрения.")',
    ),
    (
        '* [Synchronous code snippet](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync "Retrieve the synchronous code snippet of RUM JavaScript.")',
        '* [Synchronous code snippet](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-sync "Получить синхронный фрагмент кода RUM JavaScript.")',
    ),
    (
        '* [Inline code](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Retrieve the most recent inline code for manual insertion.")',
        '* [Inline code](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Получить самый последний встроенный код для ручного внедрения.")',
    ),
    (
        "The response is a plain text, containing the inline HTML code for the most recent version of the OneAgent JavaScript tag for the specified application.",
        "Ответ это обычный текст, содержащий встроенный HTML-код самой последней версии тега OneAgent JavaScript для указанного приложения.",
    ),
    (
        "In this example, the request fetches the inline HTML code for the latest version of the RUM JavaScript for the easyTravel Ionic Web application, which has the ID of **APPLICATION-BBFA55551D507E2B**.",
        "В этом примере запрос получает встроенный HTML-код последней версии RUM JavaScript для приложения easyTravel Ionic Web, у которого ID **APPLICATION-BBFA55551D507E2B**.",
    ),
    (
        "The result is truncated to the first line.",
        "Результат усечён до первой строки.",
    ),
]

# ---- real-user-monitoring-javascript-code/get-snippet-sync ----
P["real-user-monitoring-javascript-code/get-snippet-sync.md"] = [
    (
        "Returns the inline script that initializes Dynatrace and dynamically downloads the monitoring code into your application. The monitoring code is loaded synchronously.",
        "Возвращает встроенный скрипт, который инициализирует Dynatrace и динамически загружает код мониторинга в ваше приложение. Код мониторинга загружается синхронно.",
    ),
    (
        "You can also use these functionally equivalent options to obtain the RUM JavaScript:",
        "Для получения RUM JavaScript также можно использовать эти функционально эквивалентные варианты:",
    ),
    (
        '* [OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")',
        '* [OneAgent JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Получить самый последний тег OneAgent JavaScript для ручного внедрения.")',
    ),
    (
        '* [JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.")',
        '* [JavaScript tag](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Получить самый последний тег JavaScript для ручного внедрения.")',
    ),
    (
        '* [Asynchronous code snippet](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async "Retrieve the asynchronous code snippet of RUM JavaScript.")',
        '* [Asynchronous code snippet](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code/get-snippet-async "Получить асинхронный фрагмент кода RUM JavaScript.")',
    ),
    (
        '* [Inline code](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Retrieve the most recent inline code for manual insertion.")',
        '* [Inline code](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Получить самый последний встроенный код для ручного внедрения.")',
    ),
    (
        "The response is a plain text, containing the inline HTML code for the most recent version of the OneAgent JavaScript tag for the specified application.",
        "Ответ это обычный текст, содержащий встроенный HTML-код самой последней версии тега OneAgent JavaScript для указанного приложения.",
    ),
    (
        "In this example, the request fetches the inline HTML code for the latest version of the RUM JavaScript for the easyTravel Ionic Web application, which has the ID of **APPLICATION-BBFA55551D507E2B**.",
        "В этом примере запрос получает встроенный HTML-код последней версии RUM JavaScript для приложения easyTravel Ionic Web, у которого ID **APPLICATION-BBFA55551D507E2B**.",
    ),
    (
        "The result is truncated to the first line.",
        "Результат усечён до первой строки.",
    ),
]

# ---- rum-cookie-names-get-cookie-names ----
P["rum-cookie-names-get-cookie-names.md"] = [
    ("Lists RUM cookie names.", "Выводит список имён cookie RUM."),
    ("The list of all cookie names.", "Список всех имён cookie."),
    (
        "| domainValidationCookieName | string | The name of the domain validation cookie. |",
        "| domainValidationCookieName | string | Имя cookie проверки домена. |",
    ),
    (
        "| latencyCookieName | string | The name of the latency cookie. |",
        "| latencyCookieName | string | Имя cookie задержки. |",
    ),
    (
        "| pageContextCookieName | string | The name of the page context cookie. |",
        "| pageContextCookieName | string | Имя cookie контекста страницы. |",
    ),
    (
        "| sessionCookieName | string | The name of the session cookie. |",
        "| sessionCookieName | string | Имя cookie сессии. |",
    ),
    (
        "| sessionReplayCookieName | string | The name of the session replay cookie. |",
        "| sessionReplayCookieName | string | Имя cookie Session Replay. |",
    ),
    (
        "| sessionReplayViewIdCookieName | string | The name of the session replay view ID cookie. |",
        "| sessionReplayViewIdCookieName | string | Имя cookie ID представления Session Replay. |",
    ),
    (
        "| sessionTimeoutCookieName | string | The name of the session timeout cookie. |",
        "| sessionTimeoutCookieName | string | Имя cookie тайм-аута сессии. |",
    ),
    (
        "| sourceActionCookieName | string | The name of the source action cookie. |",
        "| sourceActionCookieName | string | Имя cookie исходного действия. |",
    ),
    (
        "| visitorCookieName | string | The name of the visitor cookie. |",
        "| visitorCookieName | string | Имя cookie посетителя. |",
    ),
]

# ---- rum-manual-insertion-tags (parent) ----
P["rum-manual-insertion-tags.md"] = [
    (
        "The **RUM manual insertion tags API** allows you to retrieve the RUM JavaScript for two different manual insertion scenarios:",
        "API **RUM manual insertion tags** позволяет получать RUM JavaScript для двух разных сценариев ручного внедрения:",
    ),
    (
        '* [Agentless monitoring](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") and',
        '* [безагентный мониторинг](/managed/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Настройте безагентный мониторинг для ваших веб-приложений.") и',
    ),
    (
        '* [Manual insertion for pages of an auto-injected application](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").',
        '* [Ручное внедрение для страниц приложения с автоматической инжекцией](/managed/observe/digital-experience/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Настройте автоматическое внедрение RUM JavaScript в страницы ваших приложений").',
    ),
    (
        'Different [snippet formats](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Select a format for the RUM JavaScript snippet that best fits your specific use case") are available, and supported tag attributes can be controlled via API parameters. By integrating this API into your build scripts, you can automate the insertion of the RUM JavaScript and ensure that your application always uses the current configuration.',
        'Доступны различные [snippet formats](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария."), а поддерживаемые атрибуты тега можно контролировать через параметры API. Интегрировав этот API в свои сборочные скрипты, вы можете автоматизировать внедрение RUM JavaScript и гарантировать, что ваше приложение всегда использует текущую конфигурацию.',
    ),
    (
        'To retrieve the snippet format [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Select a format for the RUM JavaScript snippet that best fits your specific use case"), use the [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").',
        'Чтобы получить формат фрагмента [code snippet](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#code-snippet "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария."), используйте [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Узнайте, как использовать Dynatrace API для настройки и сопровождения ваших приложений с ручным внедрением через Real User Monitoring JavaScript API.").',
    ),
    (
        'Retrieve the most recent JavaScript tag for manual insertion.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Retrieve the most recent JavaScript tag for manual insertion.")',
        'Получить самый последний тег JavaScript для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-javascript-tag "Получить самый последний тег JavaScript для ручного внедрения.")',
    ),
    (
        'Retrieve the most recent OneAgent JavaScript tag for manual insertion.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Retrieve the most recent OneAgent JavaScript tag for manual insertion.")',
        'Получить самый последний тег OneAgent JavaScript для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag "Получить самый последний тег OneAgent JavaScript для ручного внедрения.")',
    ),
    (
        'Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Retrieve the most recent OneAgent JavaScript tag with SRI for manual insertion.")',
        'Получить самый последний тег OneAgent JavaScript с SRI для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri "Получить самый последний тег OneAgent JavaScript с SRI для ручного внедрения.")',
    ),
    (
        'Retrieve the most recent inline code for manual insertion.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Retrieve the most recent inline code for manual insertion.")',
        'Получить самый последний встроенный код для ручного внедрения.](/managed/dynatrace-api/environment-api/rum/rum-manual-insertion-tags/get-inline-code "Получить самый последний встроенный код для ручного внедрения.")',
    ),
    ("[### Get JavaScript tag\n", "[### Получить тег JavaScript\n"),
    (
        "[### Get OneAgent JavaScript tag with SRI\n",
        "[### Получить тег OneAgent JavaScript с SRI\n",
    ),
    ("[### Get OneAgent JavaScript tag\n", "[### Получить тег OneAgent JavaScript\n"),
    ("[### Get inline code\n", "[### Получить встроенный код\n"),
]

# ---- rum-manual-insertion-tags/get-inline-code ----
P["rum-manual-insertion-tags/get-inline-code.md"] = [
    (
        'Returns the most recent [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes both the configuration and the RUM monitoring code.',
        'Возвращает самый последний [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для ручного внедрения в код вашего веб-приложения. Он включает как конфигурацию, так и код мониторинга RUM.',
    ),
    (
        "| applicationId | string | The ID of the web application. | path | Required |",
        "| applicationId | string | ID веб-приложения. | path | Required |",
    ),
    (
        'The response includes a `text/plain` payload containing the most recent version of the [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.',
        'Ответ содержит данные в формате `text/plain` с самой последней версией [inline code](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#inline-code "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для указанного приложения.',
    ),
]

# ---- rum-manual-insertion-tags/get-javascript-tag ----
# Structural twin of get-oneagent-javascript-tag.md (Reference/Updated EN,
# Authentication/Parameters/Response via COMMON). title:/H1x2 EN-verbatim (L99,
# mirrors sibling: NO title/H1 entry). Extra crossOriginAnonymous param cell;
# `crossorigin="anonymous"` kept verbatim. `#js-tag` anchor + URL verbatim.
P["rum-manual-insertion-tags/get-javascript-tag.md"] = [
    (
        'Returns the most recent [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes a reference to an external file that contains both the monitoring code and its configuration.',
        'Возвращает самый последний [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для ручного внедрения в код вашего веб-приложения. Он включает ссылку на внешний файл, содержащий как код мониторинга, так и его конфигурацию.',
    ),
    (
        "| applicationId | string | The ID of the web application. | path | Required |",
        "| applicationId | string | ID веб-приложения. | path | Required |",
    ),
    (
        "| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |",
        "| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если задан, переопределяет настроенное значение. Возможные значения: * `ASYNC` * `DEFER` * `NONE` | query | Optional |",
    ),
    (
        '| crossOriginAnonymous | boolean | Indicates whether to add the crossorigin="anonymous" attribute to the tag. If specified, this overrides the configured value. | query | Optional |',
        '| crossOriginAnonymous | boolean | Указывает, добавлять ли атрибут crossorigin="anonymous" к тегу. Если задан, переопределяет настроенное значение. | query | Optional |',
    ),
    (
        'The response includes a `text/plain` payload containing the most recent version of the [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.',
        'Ответ содержит данные в формате `text/plain` с самой последней версией [JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для указанного приложения.',
    ),
]

# ---- rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri ----
P["rum-manual-insertion-tags/get-oneagent-javascript-tag-with-sri.md"] = [
    (
        'Returns the most recent [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes configuration, a reference to the monitoring code, and an integrity hash. For more information on SRI support for RUM, see [Use Subresource Integrity (SRI) for Real User Monitoring code](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Use the Subresource Integrity (SRI) browser feature to ensure the integrity of Real User Monitoring code.").',
        'Возвращает самый последний [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для ручного внедрения в код вашего веб-приложения. Он включает конфигурацию, ссылку на код мониторинга и хеш целостности. Подробнее о поддержке SRI для RUM см. [Use Subresource Integrity (SRI) for Real User Monitoring code](/managed/observe/digital-experience/web-applications/initial-setup/subresource-integrity "Используйте браузерную функцию Subresource Integrity (SRI) для обеспечения целостности кода Real User Monitoring.").',
    ),
    (
        "| applicationId | string | The ID of the web application. | path | Required |",
        "| applicationId | string | ID веб-приложения. | path | Required |",
    ),
    (
        "| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |",
        "| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если задан, переопределяет настроенное значение. Возможные значения: * `ASYNC` * `DEFER` * `NONE` | query | Optional |",
    ),
    (
        'The response includes a `text/plain` payload containing the most recent version of the [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.',
        'Ответ содержит данные в формате `text/plain` с самой последней версией [OneAgent JavaScript tag with SRI](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag-sri "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для указанного приложения.',
    ),
]

# ---- rum-manual-insertion-tags/get-oneagent-javascript-tag ----
P["rum-manual-insertion-tags/get-oneagent-javascript-tag.md"] = [
    (
        'Returns the most recent [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for manual insertion into your web application code. It includes configuration and a reference to the monitoring code.',
        'Возвращает самый последний [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для ручного внедрения в код вашего веб-приложения. Он включает конфигурацию и ссылку на код мониторинга.',
    ),
    (
        "| applicationId | string | The ID of the web application. | path | Required |",
        "| applicationId | string | ID веб-приложения. | path | Required |",
    ),
    (
        "| scriptExecutionAttribute | string | Specifies the script execution attribute: async, defer, or none. If specified, this overrides the configured value. The element can hold these values * `ASYNC` * `DEFER` * `NONE` | query | Optional |",
        "| scriptExecutionAttribute | string | Задаёт атрибут выполнения скрипта: async, defer или none. Если задан, переопределяет настроенное значение. Возможные значения: * `ASYNC` * `DEFER` * `NONE` | query | Optional |",
    ),
    (
        'The response includes a `text/plain` payload containing the most recent version of the [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") for the specified application.',
        'Ответ содержит данные в формате `text/plain` с самой последней версией [OneAgent JavaScript tag](/managed/observe/digital-experience/web-applications/initial-setup/snippet-formats#oneagent-js-tag "Выберите формат фрагмента RUM JavaScript, который лучше всего подходит для вашего сценария.") для указанного приложения.',
    ),
]

# ---- user-sessions (parent) ----
# NOTE: em-dash mojibake (U+2014, e2 80 94) -> normalized to "-" by _normalize
# BEFORE these run; the GET tree blurb prose key below uses post-normalization
# form "columns-a flat list".
P["user-sessions.md"] = [
    (
        'The **User Sessions** API enables you to obtain data about user sessions. The API uses [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") to query the required data. Both calls return the same data, differing only in how it\'s represented.',
        'API **User Sessions** позволяет получать данные о пользовательских сессиях. API использует [User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Узнайте, как обращаться к данным пользовательских сессий и запрашивать их с помощью ключевых слов, синтаксиса, функций и многого другого.") для запроса требуемых данных. Оба вызова возвращают одни и те же данные, отличаясь только их представлением.',
    ),
    (
        'The GET table request executes a USQL query and returns results as a table structure of the requested columns.](/managed/dynatrace-api/environment-api/rum/user-sessions/table "View user sessions data in a table form via the Dynatrace API.")',
        'Запрос GET table выполняет USQL-запрос и возвращает результаты в виде табличной структуры запрошенных столбцов.](/managed/dynatrace-api/environment-api/rum/user-sessions/table "Просмотр данных пользовательских сессий в табличной форме через Dynatrace API.")',
    ),
    (
        'The GET tree request executes a USQL query and returns results as a tree structure of the requested columns-a flat list containing the requested columns.](/managed/dynatrace-api/environment-api/rum/user-sessions/tree "View user sessions data in a tree form via the Dynatrace API.")',
        'Запрос GET tree выполняет USQL-запрос и возвращает результаты в виде древовидной структуры запрошенных столбцов: плоского списка, содержащего запрошенные столбцы.](/managed/dynatrace-api/environment-api/rum/user-sessions/tree "Просмотр данных пользовательских сессий в древовидной форме через Dynatrace API.")',
    ),
    (
        'Learn the structure of a user session that contains all possible fields.](/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure "Learn the structure of a user session in the Dynatrace User Session Query language API.")',
        'Изучите структуру пользовательской сессии, содержащую все возможные поля.](/managed/dynatrace-api/environment-api/rum/user-sessions/user-session-structure "Изучите структуру пользовательской сессии в Dynatrace User Session Query language API.")',
    ),
    ("[### GET table\n", "[### GET table\n"),
    ("[### GET tree\n", "[### GET tree\n"),
    ("[### User session structure\n", "[### Структура пользовательской сессии\n"),
]

# ---- user-sessions/table ----
P["user-sessions/table.md"] = [
    (
        "Executes a USQL query and returns results as a table structure of the requested columns.",
        "Выполняет USQL-запрос и возвращает результаты в виде табличной структуры запрошенных столбцов.",
    ),
    (
        "In the table structure, entities that are selected by the query form columns of a table. Each element of the **values** array forms a row of a table.",
        "В табличной структуре сущности, выбранные запросом, формируют столбцы таблицы. Каждый элемент массива **values** формирует строку таблицы.",
    ),
    (
        "The user session query result as a table.",
        "Результат запроса пользовательских сессий в виде таблицы.",
    ),
    (
        "A schema representing an arbitrary value type.",
        "Схема, представляющая произвольный тип значения.",
    ),
    (
        "The user session query to be executed. See [USQL documentation page](https://dt-url.net/dtusql) for syntax details.  You can find the available columns of the **usersession** table in the `UserSession` object.  Here is an example of the query: `SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city`.",
        "Выполняемый запрос пользовательских сессий. Подробности синтаксиса см. на [странице документации USQL](https://dt-url.net/dtusql).  Доступные столбцы таблицы **usersession** можно найти в объекте `UserSession`.  Пример запроса: `SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city`.",
    ),
    (
        "The start timestamp of the query, in UTC milliseconds.  If not set or set as `0`, 2 hours behind the current time is used.  If the exact times are important, set the timeframe in the query itself (**query** parameter).",
        "Начальная метка времени запроса в миллисекундах UTC.  Если не задана или задана как `0`, используется время на 2 часа раньше текущего.  Если важны точные значения времени, задайте временной диапазон в самом запросе (параметр **query**).",
    ),
    (
        "The end timestamp of the query, in UTC milliseconds.  If not set or set as `0`, the current timestamp is used.  If the exact times are important, set the timeframe in the query itself (**query** parameter).",
        "Конечная метка времени запроса в миллисекундах UTC.  Если не задана или задана как `0`, используется текущая метка времени.  Если важны точные значения времени, задайте временной диапазон в самом запросе (параметр **query**).",
    ),
    (
        "Optional offset of local time to UTC time in minutes. Offset will be applied to Date fields encountered in the query.  Can be positive or negative. E.g. if the local time is UTC+02:00, the timeOffset is 120. If it is UTC-05:00, timeOffset is -300.",
        "Необязательное смещение локального времени относительно UTC в минутах. Смещение применяется к полям Date, встречающимся в запросе.  Может быть положительным или отрицательным. Например, если локальное время UTC+02:00, то timeOffset равен 120. Если UTC-05:00, то timeOffset равен -300.",
    ),
    (
        "Optional limit on how many of the actual query results should be returned in the tabular result.",
        "Необязательное ограничение на количество фактических результатов запроса, возвращаемых в табличном результате.",
    ),
    (
        "Optional offset of the requested results from the start of tabular results. Relates to pageSize.  E.g. on a query that might return 500 results, you might want to receive results in chunks of 50 rows.  this can be achieved by using pageSize=50, and setting pageOffset in subsequent calls.In the example adding pageOffset=50 returns result rows 51-100.",
        "Необязательное смещение запрошенных результатов от начала табличных результатов. Связано с pageSize.  Например, для запроса, который может вернуть 500 результатов, вы можете захотеть получать результаты порциями по 50 строк.  Это можно сделать, используя pageSize=50 и задавая pageOffset в последующих вызовах.В примере добавление pageOffset=50 возвращает строки результата 51-100.",
    ),
    (
        "Add (`true`) to enable deep linking of additional fields in the query.  If not set, then `false` is used",
        "Добавьте (`true`), чтобы включить глубокие ссылки на дополнительные поля в запросе.  Если не задано, используется `false`",
    ),
    (
        "Add (`true`) or don't add (`false`) some additional information about the result to the response.  It helps to understand the query and how the result was calculated.  If not set, then `false` is used",
        "Добавлять (`true`) или не добавлять (`false`) некоторую дополнительную информацию о результате в ответ.  Это помогает понять запрос и то, как был вычислен результат.  Если не задано, используется `false`",
    ),
    (
        "A list of columns in the additionalValues table.  Only present if the endpoint was called with `deepLinkFields=true` parameter.",
        "Список столбцов в таблице additionalValues.  Присутствует только если эндпоинт был вызван с параметром `deepLinkFields=true`.",
    ),
    (
        "A list of data rows.  Each array element represents a row in the table of additionally linked fields.  The size of each data row and the order of the elements correspond to the **additionalColumnNames** content.  Only present if the endpoint was called with `deepLinkFields=true` parameter.",
        "Список строк данных.  Каждый элемент массива представляет строку в таблице дополнительно связанных полей.  Размер каждой строки данных и порядок элементов соответствуют содержимому **additionalColumnNames**.  Присутствует только если эндпоинт был вызван с параметром `deepLinkFields=true`.",
    ),
    (
        "A list of columns in the result table.",
        "Список столбцов в результирующей таблице.",
    ),
    (
        "Additional information about the query and the result, that helps to understand the query and how the result was calculated.  Only appears when the **explain** parameter is set to `true`.  Example: The number of results was limited to the default of 50. Use the `LIMIT` clause to increase or decrease this limit.",
        "Дополнительная информация о запросе и результате, помогающая понять запрос и то, как был вычислен результат.  Появляется только когда параметр **explain** установлен в `true`.  Пример: Количество результатов было ограничено значением по умолчанию 50. Используйте оператор `LIMIT`, чтобы увеличить или уменьшить это ограничение.",
    ),
    (
        "The extrapolation level of the result.  To improve performance, some results may be calculated from a subset of actual data. The extrapolation level indicates the share of actual data in the result.  The number is the denominator of a fraction and indicates the amount of actual data. The value `1` means that the result contains only the actual data. The value `4` means that result is calculated using 1/4 of the actual data.  If you need the analysis to be based on the actual data, reduce the timeframe of your query. For example, in case of extrapolation level of `4`, try to use 1/4 of the original timeframe.",
        "Уровень экстраполяции результата.  Для повышения производительности некоторые результаты могут вычисляться по подмножеству фактических данных. Уровень экстраполяции указывает долю фактических данных в результате.  Число это знаменатель дроби, указывающий объём фактических данных. Значение `1` означает, что результат содержит только фактические данные. Значение `4` означает, что результат вычислен с использованием 1/4 фактических данных.  Если анализ должен быть основан на фактических данных, уменьшите временной диапазон запроса. Например, при уровне экстраполяции `4` попробуйте использовать 1/4 исходного временного диапазона.",
    ),
    (
        "A list of data rows.  Each array element represents a row in the result table.  The size of each data row and the order of the elements correspond to the **columnNames** content.",
        "Список строк данных.  Каждый элемент массива представляет строку в результирующей таблице.  Размер каждой строки данных и порядок элементов соответствуют содержимому **columnNames**.",
    ),
    (
        "In this example, the request executes the `SELECT country, city, avg(duration), max(duration) FROM usersession GROUP BY country, city` query.",
        "В этом примере запрос выполняет запрос `SELECT country, city, avg(duration), max(duration) FROM usersession GROUP BY country, city`.",
    ),
    (
        "The result is truncated to 4 entries.",
        "Результат усечён до 4 записей.",
    ),
    (
        "Since the timeframe is not specified, the query uses the default timeframe of **2 hours** back from the current time.",
        "Поскольку временной диапазон не указан, запрос использует временной диапазон по умолчанию: **2 часа** назад от текущего времени.",
    ),
    (
        "The resulting table has four columns: **country**, **city**, **average duration**, and **maximal duration**. The **values** array contains rows of the table.",
        "Результирующая таблица содержит четыре столбца: **country**, **city**, **average duration** и **maximal duration**. Массив **values** содержит строки таблицы.",
    ),
    (
        "The **extrapolationLevel** of 4 indicates that the values are extrapolated from 1/4th of the actual data.",
        "Значение **extrapolationLevel** равное 4 означает, что значения экстраполированы из 1/4 фактических данных.",
    ),
]

# ---- user-sessions/tree ----
P["user-sessions/tree.md"] = [
    (
        "Executes a USQL query and returns results as a tree structure of the requested columns-a flat list containing the requested columns.",
        "Выполняет USQL-запрос и возвращает результаты в виде древовидной структуры запрошенных столбцов: плоского списка, содержащего запрошенные столбцы.",
    ),
    (
        'To get a proper tree structure, you need to specify grouping in the query. The fields used in the `GROUP BY` clause form the "branches" of the tree, each holding "leaves"-selected fields that have not been used for grouping.',
        'Чтобы получить корректную древовидную структуру, нужно указать группировку в запросе. Поля, используемые в операторе `GROUP BY`, формируют "ветви" дерева, каждая из которых содержит "листья": выбранные поля, которые не использовались для группировки.',
    ),
    (
        "The user session query result as a tree.",
        "Результат запроса пользовательских сессий в виде дерева.",
    ),
    (
        "A schema representing an arbitrary value type.",
        "Схема, представляющая произвольный тип значения.",
    ),
    (
        "The user session query to be executed. See [USQL documentation page](https://dt-url.net/dtusql) for syntax details.  You can find the available columns of the **usersession** table in the `UserSession` object.  Here is an example of the query: `SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city`.",
        "Выполняемый запрос пользовательских сессий. Подробности синтаксиса см. на [странице документации USQL](https://dt-url.net/dtusql).  Доступные столбцы таблицы **usersession** можно найти в объекте `UserSession`.  Пример запроса: `SELECT country, city, COUNT(*) FROM usersession GROUP BY country, city`.",
    ),
    (
        "The start timestamp of the query, in UTC milliseconds.  If not set or set as `0`, 2 hours behind the current time is used.  If the exact times are important, set the timeframe in the query itself (**query** parameter).",
        "Начальная метка времени запроса в миллисекундах UTC.  Если не задана или задана как `0`, используется время на 2 часа раньше текущего.  Если важны точные значения времени, задайте временной диапазон в самом запросе (параметр **query**).",
    ),
    (
        "The end timestamp of the query, in UTC milliseconds.  If not set or set as `0`, the current timestamp is used.  If the exact times are important, set the timeframe in the query itself (**query** parameter).",
        "Конечная метка времени запроса в миллисекундах UTC.  Если не задана или задана как `0`, используется текущая метка времени.  Если важны точные значения времени, задайте временной диапазон в самом запросе (параметр **query**).",
    ),
    (
        "Optional offset of local time to UTC time in minutes. Offset will be applied to Date fields encountered in the query.  Can be positive or negative. E.g. if the local time is UTC+02:00, the timeOffset is 120. If it is UTC-05:00, timeOffset is -300.",
        "Необязательное смещение локального времени относительно UTC в минутах. Смещение применяется к полям Date, встречающимся в запросе.  Может быть положительным или отрицательным. Например, если локальное время UTC+02:00, то timeOffset равен 120. Если UTC-05:00, то timeOffset равен -300.",
    ),
    (
        "Add (`true`) to enable deep linking of additional fields in the query.  If not set, then `false` is used",
        "Добавьте (`true`), чтобы включить глубокие ссылки на дополнительные поля в запросе.  Если не задано, используется `false`",
    ),
    (
        "Add (`true`) or don't add (`false`) some additional information about the result to the response.  It helps to understand the query and how the result was calculated.  If not set, then `false` is used",
        "Добавлять (`true`) или не добавлять (`false`) некоторую дополнительную информацию о результате в ответ.  Это помогает понять запрос и то, как был вычислен результат.  Если не задано, используется `false`",
    ),
    (
        "A list of columns in the additionalValues table.  Only present if the endpoint was called with `deepLinkFields=true` parameter.",
        "Список столбцов в таблице additionalValues.  Присутствует только если эндпоинт был вызван с параметром `deepLinkFields=true`.",
    ),
    (
        "A list of data rows.  Each array element represents a row in the table of additionally linked fields.  The size of each data row and the order of the elements correspond to the **additionalColumnNames** content.  Only present if the endpoint was called with `deepLinkFields=true` parameter.",
        "Список строк данных.  Каждый элемент массива представляет строку в таблице дополнительно связанных полей.  Размер каждой строки данных и порядок элементов соответствуют содержимому **additionalColumnNames**.  Присутствует только если эндпоинт был вызван с параметром `deepLinkFields=true`.",
    ),
    (
        "A list of branches of the tree.  Typically, these are fields from the `SELECT` clause, that have been used in the `GROUP BY` clause.",
        "Список ветвей дерева.  Обычно это поля из оператора `SELECT`, которые использовались в операторе `GROUP BY`.",
    ),
    (
        "Additional information about the query and the result, that helps to understand the query and how the result was calculated.  Only appears when the **explain** parameter is set to `true`.  Example: The number of results was limited to the default of 50. Use the `LIMIT` clause to increase or decrease this limit.",
        "Дополнительная информация о запросе и результате, помогающая понять запрос и то, как был вычислен результат.  Появляется только когда параметр **explain** установлен в `true`.  Пример: Количество результатов было ограничено значением по умолчанию 50. Используйте оператор `LIMIT`, чтобы увеличить или уменьшить это ограничение.",
    ),
    (
        "The extrapolation level of the result.  To improve performance, some results may be calculated from a subset of actual data. The extrapolation level indicates the share of actual data in the result.  The number is the denominator of a fraction and indicates the amount of actual data. The value `1` means that the result contains only the actual data. The value `4` means that result is calculated using 1/4 of the actual data.  If you need the analysis to be based on the actual data, reduce the timeframe of your query. For example, in case of extrapolation level of `4`, try to use 1/4 of the original timeframe.",
        "Уровень экстраполяции результата.  Для повышения производительности некоторые результаты могут вычисляться по подмножеству фактических данных. Уровень экстраполяции указывает долю фактических данных в результате.  Число это знаменатель дроби, указывающий объём фактических данных. Значение `1` означает, что результат содержит только фактические данные. Значение `4` означает, что результат вычислен с использованием 1/4 фактических данных.  Если анализ должен быть основан на фактических данных, уменьшите временной диапазон запроса. Например, при уровне экстраполяции `4` попробуйте использовать 1/4 исходного временного диапазона.",
    ),
    (
        "A list of leaves on each tree branch.  Typically, these are fields from the `SELECT` clause, that have not been used in the `GROUP BY` clause.",
        "Список листьев на каждой ветви дерева.  Обычно это поля из оператора `SELECT`, которые не использовались в операторе `GROUP BY`.",
    ),
    # `| values | string | The user session query result as a tree. |` row: its
    # description substring is already covered by the standalone-line key above
    # (str.replace hits the cell too) -> no explicit row entry needed.
    (
        "In this example, the request executes the `SELECT country, city, avg(duration), max(duration) FROM usersession GROUP BY country, city` query.",
        "В этом примере запрос выполняет запрос `SELECT country, city, avg(duration), max(duration) FROM usersession GROUP BY country, city`.",
    ),
    (
        "The result is truncated to 4 entries.",
        "Результат усечён до 4 записей.",
    ),
    (
        "Since the timeframe is not specified, the query uses the default timeframe of **2 hours** back from the current time.",
        "Поскольку временной диапазон не указан, запрос использует временной диапазон по умолчанию: **2 часа** назад от текущего времени.",
    ),
    (
        "In the resulting structure, all the values are grouped initially by the **country**, with each object of the **values** array representing a country. These objects each hold arrays of **average** and **maximal** durations of user sessions for each **city**.",
        "В результирующей структуре все значения сначала сгруппированы по **country**, и каждый объект массива **values** представляет страну. Каждый из этих объектов содержит массивы **average** и **maximal** длительностей пользовательских сессий для каждого **city**.",
    ),
    (
        "The **extrapolationLevel** of 4 indicates that the values are extrapolated from 1/4th of the actual data.",
        "Значение **extrapolationLevel** равное 4 означает, что значения экстраполированы из 1/4 фактических данных.",
    ),
]

# ---- user-sessions/user-session-structure ----
P["user-sessions/user-session-structure.md"] = [
    (
        "This page provides descriptions of all possible fields that a user session might include.",
        "На этой странице приведены описания всех возможных полей, которые может включать пользовательская сессия.",
    ),
    (
        "A [user session](https://dt-url.net/xv183rb8), encompassing multiple user actions and additional information about a user's visit.",
        "[Пользовательская сессия](https://dt-url.net/xv183rb8), охватывающая несколько пользовательских действий и дополнительную информацию о визите пользователя.",
    ),
    # --- object headings unique to this file ---
    ("#### The `UserSession` object", "#### Объект `UserSession`"),
    ("#### The `DateProperty` object", "#### Объект `DateProperty`"),
    ("#### The `DoubleProperty` object", "#### Объект `DoubleProperty`"),
    ("#### The `UserSessionErrors` object", "#### Объект `UserSessionErrors`"),
    ("#### The `UserSessionEvents` object", "#### Объект `UserSessionEvents`"),
    ("#### The `LongProperty` object", "#### Объект `LongProperty`"),
    ("#### The `StringProperty` object", "#### Объект `StringProperty`"),
    (
        "#### The `UserSessionSyntheticEvent` object",
        "#### Объект `UserSessionSyntheticEvent`",
    ),
    (
        "#### The `UserSessionUserAction` object",
        "#### Объект `UserSessionUserAction`",
    ),
    # --- object intro descriptions ---
    (
        "A custom property of the user-action with a date value.",
        "Пользовательское свойство пользовательского действия со значением-датой.",
    ),
    (
        "A custom property of the user action with a Double value.",
        "Пользовательское свойство пользовательского действия со значением Double.",
    ),
    (
        "A custom property of the user action with a Long value.",
        "Пользовательское свойство пользовательского действия со значением Long.",
    ),
    (
        "A custom property of the user action with a string value.",
        "Пользовательское свойство пользовательского действия со строковым значением.",
    ),
    ("The error of a user session.", "Ошибка пользовательской сессии."),
    (
        "The external event of a user session.",
        "Внешнее событие пользовательской сессии.",
    ),
    (
        "A synthetic event of a user session.",
        "Synthetic-событие пользовательской сессии.",
    ),
    (
        "A user action is a single action performed by the user as part of a user session, for example a mouse click.",
        "Пользовательское действие это одно действие, выполняемое пользователем в рамках пользовательской сессии, например щелчок мышью.",
    ),
    ("\nA user action.\n", "\nПользовательское действие.\n"),
    # --- UserSession element cells (longest/most-specific FIRST) ---
    (
        "| appVersion | string | The version of the application where the user session has been recorded.  This information is provided by another integration, such as OpenKit. |",
        "| appVersion | string | Версия приложения, в котором была записана пользовательская сессия.  Эта информация предоставляется другой интеграцией, например OpenKit. |",
    ),
    (
        "| applicationType | string | The type of the application used in the user session. The element can hold these values * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` * `WEB_APPLICATION` |",
        "| applicationType | string | Тип приложения, используемого в пользовательской сессии. Возможные значения: * `CUSTOM_APPLICATION` * `MOBILE_APPLICATION` * `WEB_APPLICATION` |",
    ),
    (
        "| bounce | boolean | The user session has (`true`) or doesn't have (`false`) a bounce.  A bounce means there is only one (or less) user action in the user session. |",
        "| bounce | boolean | Пользовательская сессия содержит (`true`) или не содержит (`false`) отказ.  Отказ означает, что в пользовательской сессии есть только одно (или менее) пользовательское действие. |",
    ),
    (
        "| browserFamily | string | The family of the browser used for the user session. |",
        "| browserFamily | string | Семейство браузера, использованного для пользовательской сессии. |",
    ),
    (
        "| browserMajorVersion | string | The version of the browser used for the user session. |",
        "| browserMajorVersion | string | Версия браузера, использованного для пользовательской сессии. |",
    ),
    (
        "| browserMonitorId | string | The ID of the Synthetic browser monitor that created the session. |",
        "| browserMonitorId | string | ID браузерного Synthetic-монитора, создавшего сессию. |",
    ),
    (
        "| browserMonitorName | string | The name of the Synthetic browser monitor that created the session. |",
        "| browserMonitorName | string | Имя браузерного Synthetic-монитора, создавшего сессию. |",
    ),
    (
        "| browserType | string | The type of browser used for the user session. |",
        "| browserType | string | Тип браузера, использованного для пользовательской сессии. |",
    ),
    (
        "| carrier | string | The carrier information of the mobile user session. |",
        "| carrier | string | Информация об операторе мобильной пользовательской сессии. |",
    ),
    (
        "| city | string | The city from which the user session originates (based on the IP address). |",
        "| city | string | Город, из которого происходит пользовательская сессия (на основе IP-адреса). |",
    ),
    (
        "| clientTimeOffset | integer | The time offset of the client, in milliseconds |",
        "| clientTimeOffset | integer | Смещение времени клиента в миллисекундах |",
    ),
    (
        "| clientType | string | Additional information about the client.  This field can not be queried via the user session query language. Use the **browserType** field instead. |",
        "| clientType | string | Дополнительная информация о клиенте.  Это поле нельзя запросить через user session query language. Вместо него используйте поле **browserType**. |",
    ),
    (
        "| connectionType | string | The serialized connection type of the mobile user session. The element can hold these values * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` |",
        "| connectionType | string | Сериализованный тип подключения мобильной пользовательской сессии. Возможные значения: * `LAN` * `MOBILE` * `OFFLINE` * `UNKNOWN` * `WIFI` |",
    ),
    (
        "| continent | string | The continent from which the user session originates (based on the IP address). |",
        "| continent | string | Континент, из которого происходит пользовательская сессия (на основе IP-адреса). |",
    ),
    (
        "| country | string | The country from which the user session originates (based on the IP address). |",
        "| country | string | Страна, из которой происходит пользовательская сессия (на основе IP-адреса). |",
    ),
    (
        "| crashGroupId | string | If a mobile session crashed, this is the ID of the group to which the crashed session belongs.  If the session did not crash or the session is not a mobile session, it has the `null` value. |",
        "| crashGroupId | string | Если мобильная сессия завершилась сбоем, это ID группы, к которой относится аварийная сессия.  Если сессия не завершилась сбоем или сессия не является мобильной, имеет значение `null`. |",
    ),
    (
        "| dateProperties | [DateProperty[]](#openapi-definition-DateProperty) | A list of custom properties of the user session with date values. |",
        "| dateProperties | [DateProperty[]](#openapi-definition-DateProperty) | Список пользовательских свойств пользовательской сессии со значениями-датами. |",
    ),
    (
        "| device | string | The detected device used for the user session. |",
        "| device | string | Обнаруженное устройство, использованное для пользовательской сессии. |",
    ),
    (
        "| displayResolution | string | The detected screen resolution of the device used for the user session. The element can hold these values",
        "| displayResolution | string | Обнаруженное разрешение экрана устройства, использованного для пользовательской сессии. Возможные значения:",
    ),
    (
        "| doubleProperties | [DoubleProperty[]](#openapi-definition-DoubleProperty) | A list of custom properties of the user session with floating-point numerical values. |",
        "| doubleProperties | [DoubleProperty[]](#openapi-definition-DoubleProperty) | Список пользовательских свойств пользовательской сессии с числовыми значениями с плавающей точкой. |",
    ),
    (
        "| duration | integer | The duration of the user session, in milliseconds.  This is calculated as the amount of time between the start of the first user action and the end of the last user action. |",
        "| duration | integer | Длительность пользовательской сессии в миллисекундах.  Вычисляется как промежуток времени между началом первого пользовательского действия и концом последнего пользовательского действия. |",
    ),
    (
        "| endReason | string | The reason for the end of the user session. The element can hold these values * `DURATION_LIMIT` * `END_EVENT` * `EXTENDED_TIMEOUT` * `TEST_FAILED` * `TIMEOUT` * `USER_ACTION_LIMIT` |",
        "| endReason | string | Причина окончания пользовательской сессии. Возможные значения: * `DURATION_LIMIT` * `END_EVENT` * `EXTENDED_TIMEOUT` * `TEST_FAILED` * `TIMEOUT` * `USER_ACTION_LIMIT` |",
    ),
    (
        "| endTime | integer | The timestamp of the last user action in the user session, in UTC milliseconds. |",
        "| endTime | integer | Метка времени последнего пользовательского действия в пользовательской сессии в миллисекундах UTC. |",
    ),
    (
        "| errors | [UserSessionErrors[]](#openapi-definition-UserSessionErrors) | A list of errors recorded in the user session. |",
        "| errors | [UserSessionErrors[]](#openapi-definition-UserSessionErrors) | Список ошибок, записанных в пользовательской сессии. |",
    ),
    (
        "| events | [UserSessionEvents[]](#openapi-definition-UserSessionEvents) | A list of additional events recorded in the user session. |",
        "| events | [UserSessionEvents[]](#openapi-definition-UserSessionEvents) | Список дополнительных событий, записанных в пользовательской сессии. |",
    ),
    (
        "| hasCrash | boolean | The user session includes (`true`) or doesn't include (`false`) a crash. |",
        "| hasCrash | boolean | Пользовательская сессия включает (`true`) или не включает (`false`) сбой. |",
    ),
    (
        "| hasError | boolean | The user session includes (`true`) or doesn't include (`false`) an error. |",
        "| hasError | boolean | Пользовательская сессия включает (`true`) или не включает (`false`) ошибку. |",
    ),
    (
        "| hasSessionReplay | boolean | Session Replay is (`true`) or is not (`false`) available for the session. |",
        "| hasSessionReplay | boolean | Session Replay доступен (`true`) или недоступен (`false`) для сессии. |",
    ),
    (
        "| internalUserId | string | The unique ID of the user that triggered the user session. |",
        "| internalUserId | string | Уникальный ID пользователя, инициировавшего пользовательскую сессию. |",
    ),
    (
        "| ip | string | The IP address (IPv4 or IPv6) from which the user session originates. |",
        "| ip | string | IP-адрес (IPv4 или IPv6), из которого происходит пользовательская сессия. |",
    ),
    (
        "| isp | string | The internet service provider from which the user session originates (based on the IP address). |",
        "| isp | string | Интернет-провайдер, от которого происходит пользовательская сессия (на основе IP-адреса). |",
    ),
    (
        "| longProperties | [LongProperty[]](#openapi-definition-LongProperty) | A list of custom properties of the user session with integer (short or long) values. |",
        "| longProperties | [LongProperty[]](#openapi-definition-LongProperty) | Список пользовательских свойств пользовательской сессии с целочисленными (short или long) значениями. |",
    ),
    (
        "| manufacturer | string | The detected manufacturer of the device used for the user session. |",
        "| manufacturer | string | Обнаруженный производитель устройства, использованного для пользовательской сессии. |",
    ),
    (
        "| matchingConversionGoals | string[] | A list of conversion goals achieved by the user session.  Additionally, you can define conversion goals for a single user action. |",
        "| matchingConversionGoals | string[] | Список целей конверсии, достигнутых в пользовательской сессии.  Дополнительно можно задать цели конверсии для отдельного пользовательского действия. |",
    ),
    (
        "| matchingConversionGoalsCount | integer | The number of conversion goals achieved by the user session. |",
        "| matchingConversionGoalsCount | integer | Количество целей конверсии, достигнутых в пользовательской сессии. |",
    ),
    (
        "| networkTechnology | string | The network technology information of the mobile user session. |",
        "| networkTechnology | string | Информация о сетевой технологии мобильной пользовательской сессии. |",
    ),
    (
        "| newUser | boolean | The user is a first-time (`true`) or a returning user (`false`). |",
        "| newUser | boolean | Пользователь новый (`true`) или вернувшийся (`false`). |",
    ),
    (
        "| numberOfRageClicks | integer | The number of rage clicks detected in the user session. |",
        "| numberOfRageClicks | integer | Количество rage-кликов, обнаруженных в пользовательской сессии. |",
    ),
    (
        "| numberOfRageTaps | integer | The number of rage taps detected in the user session. |",
        "| numberOfRageTaps | integer | Количество rage-тапов, обнаруженных в пользовательской сессии. |",
    ),
    (
        "| osFamily | string | The type of operating system used for the user session. |",
        "| osFamily | string | Тип операционной системы, использованной для пользовательской сессии. |",
    ),
    (
        "| osVersion | string | The version of the operating system used for the user session. |",
        "| osVersion | string | Версия операционной системы, использованной для пользовательской сессии. |",
    ),
    (
        "| partNumber | integer | User sessions can be split into multiple parts for various technical reasons (e.g. after 200 user actions). This `partNumber` represents the number of each part of the overall user session. |",
        "| partNumber | integer | Пользовательские сессии могут разбиваться на несколько частей по разным техническим причинам (например, после 200 пользовательских действий). Этот `partNumber` представляет номер каждой части всей пользовательской сессии. |",
    ),
    (
        "| reasonForNoSessionReplay | string | The reason for absence of Session Replay. The element can hold these values * `KILLED_EMERGENCY` * `KILLED_ERROR` * `KILLED_INVALID_RESPONSE` * `KILLED_MIN_JS_AGENT_VERSION` * `KILLED_NO_LICENSE` * `KILLED_WRONG_CONTENT_TYPE` * `MISCONFIGURED_CLUSTER` * `MODULE_DISABLED` * `NO_ACTIVITY` * `OPTED_OUT_SESSION` * `OPT_IN_MODE` * `ROBOT_DETECTED` * `SAMPLED_OUT` * `UNABLE_TO_LOAD_WORKER` * `UNHANDLED_EXCEPTION` * `UNKNOWN` * `UNKNOWN_DOC_LOADED` * `UNSUPPORTED_BROWSER` * `VIEW_EXCLUDED` |",
        "| reasonForNoSessionReplay | string | Причина отсутствия Session Replay. Возможные значения: * `KILLED_EMERGENCY` * `KILLED_ERROR` * `KILLED_INVALID_RESPONSE` * `KILLED_MIN_JS_AGENT_VERSION` * `KILLED_NO_LICENSE` * `KILLED_WRONG_CONTENT_TYPE` * `MISCONFIGURED_CLUSTER` * `MODULE_DISABLED` * `NO_ACTIVITY` * `OPTED_OUT_SESSION` * `OPT_IN_MODE` * `ROBOT_DETECTED` * `SAMPLED_OUT` * `UNABLE_TO_LOAD_WORKER` * `UNHANDLED_EXCEPTION` * `UNKNOWN` * `UNKNOWN_DOC_LOADED` * `UNSUPPORTED_BROWSER` * `VIEW_EXCLUDED` |",
    ),
    (
        "| reasonForNoSessionReplayMobile | string | The reason for absence of Session Replay on mobile. The element can hold these values * `COST_CONTROL` * `CRASHES_OPTED_IN` * `DISABLED` * `FULL_STORAGE` * `INVALID_CONFIGURATION` * `NO_AGENT` * `OPTED_OUT` * `RETENTION_TIME` * `UNKNOWN` |",
        "| reasonForNoSessionReplayMobile | string | Причина отсутствия Session Replay на мобильных устройствах. Возможные значения: * `COST_CONTROL` * `CRASHES_OPTED_IN` * `DISABLED` * `FULL_STORAGE` * `INVALID_CONFIGURATION` * `NO_AGENT` * `OPTED_OUT` * `RETENTION_TIME` * `UNKNOWN` |",
    ),
    (
        "| region | string | The region from which the user session originates (based on the IP address). |",
        "| region | string | Регион, из которого происходит пользовательская сессия (на основе IP-адреса). |",
    ),
    (
        "| replayEnd | integer | The timestamp of the Session Replay end, in UTC milliseconds. |",
        "| replayEnd | integer | Метка времени окончания Session Replay в миллисекундах UTC. |",
    ),
    (
        "| replayStart | integer | The timestamp of the Session Replay start, in UTC milliseconds. |",
        "| replayStart | integer | Метка времени начала Session Replay в миллисекундах UTC. |",
    ),
    (
        "| rootedOrJailbroken | boolean | The mobile device is rooted/jailbroken (`true`) or genuine (`false`).  Has the value of `null` if the status is unknown or undefined. Custom applications always report unknown/undefined. |",
        "| rootedOrJailbroken | boolean | Мобильное устройство имеет root/jailbreak (`true`) или оригинальное (`false`).  Имеет значение `null`, если статус неизвестен или не определён. Пользовательские приложения всегда сообщают неизвестно/не определено. |",
    ),
    (
        "| screenHeight | integer | The detected screen height of the device used for the user session. |",
        "| screenHeight | integer | Обнаруженная высота экрана устройства, использованного для пользовательской сессии. |",
    ),
    (
        "| screenOrientation | string | The detected screen orientation of the device used on the device for the user session. The element can hold these values * `LANDSCAPE` * `PORTRAIT` * `UNDEFINED` |",
        "| screenOrientation | string | Обнаруженная ориентация экрана устройства, использованного для пользовательской сессии. Возможные значения: * `LANDSCAPE` * `PORTRAIT` * `UNDEFINED` |",
    ),
    (
        "| screenWidth | integer | The detected screen width of the device used for the user session. |",
        "| screenWidth | integer | Обнаруженная ширина экрана устройства, использованного для пользовательской сессии. |",
    ),
    (
        "| startTime | integer | The timestamp of the first user action in the user session, in UTC milliseconds. |",
        "| startTime | integer | Метка времени первого пользовательского действия в пользовательской сессии в миллисекундах UTC. |",
    ),
    (
        "| stringProperties | [StringProperty[]](#openapi-definition-StringProperty) | A list of custom properties of the user session with string values. |",
        "| stringProperties | [StringProperty[]](#openapi-definition-StringProperty) | Список пользовательских свойств пользовательской сессии со строковыми значениями. |",
    ),
    (
        "| syntheticEvents | [UserSessionSyntheticEvent[]](#openapi-definition-UserSessionSyntheticEvent) | A list of synthetic events recorded in the user session. |",
        "| syntheticEvents | [UserSessionSyntheticEvent[]](#openapi-definition-UserSessionSyntheticEvent) | Список synthetic-событий, записанных в пользовательской сессии. |",
    ),
    (
        "| tenantId | string | The ID of the Dynatrace environment that captured the user session.  This field can not be queried via the User Session Query Language. |",
        "| tenantId | string | ID окружения Dynatrace, захватившего пользовательскую сессию.  Это поле нельзя запросить через User Session Query Language. |",
    ),
    (
        "| totalErrorCount | integer | The number of errors detected in the user session. |",
        "| totalErrorCount | integer | Количество ошибок, обнаруженных в пользовательской сессии. |",
    ),
    (
        "| totalLicenseCreditCount | integer | Number of resulting billed sessions: [Dynatrace classic licensing](https://dt-url.net/u24c0pga), [Dynatrace Platform Subscription](https://www.dynatrace.com/support/help/shortlink/dps-dem). |",
        "| totalLicenseCreditCount | integer | Количество результирующих оплачиваемых сессий: [Dynatrace classic licensing](https://dt-url.net/u24c0pga), [Dynatrace Platform Subscription](https://www.dynatrace.com/support/help/shortlink/dps-dem). |",
    ),
    (
        "| userActionCount | integer | The number of user actions in the user session. |",
        "| userActionCount | integer | Количество пользовательских действий в пользовательской сессии. |",
    ),
    (
        "| userActions | [UserSessionUserAction[]](#openapi-definition-UserSessionUserAction) | A list of user actions recorded in the user session. |",
        "| userActions | [UserSessionUserAction[]](#openapi-definition-UserSessionUserAction) | Список пользовательских действий, записанных в пользовательской сессии. |",
    ),
    (
        "| userExperienceScore | string | The user experience score of the user session. The element can hold these values * `FRUSTRATED` * `SATISFIED` * `TOLERATED` * `UNDEFINED` |",
        "| userExperienceScore | string | Оценка пользовательского опыта пользовательской сессии. Возможные значения: * `FRUSTRATED` * `SATISFIED` * `TOLERATED` * `UNDEFINED` |",
    ),
    (
        "| userId | string | The user ID provided for the user session by session tagging. |",
        "| userId | string | ID пользователя, предоставленный для пользовательской сессии тегированием сессий. |",
    ),
    (
        "| userSessionId | string | The unique ID of the user session. |",
        "| userSessionId | string | Уникальный ID пользовательской сессии. |",
    ),
    (
        "| userType | string | The type of the user. Indicates either a real human user (`REAL_USER`) or a robot (`ROBOT` or `SYNTHETIC`). The element can hold these values * `REAL_USER` * `ROBOT` * `SYNTHETIC` |",
        "| userType | string | Тип пользователя. Указывает либо реального человека (`REAL_USER`), либо робота (`ROBOT` или `SYNTHETIC`). Возможные значения: * `REAL_USER` * `ROBOT` * `SYNTHETIC` |",
    ),
    # --- DateProperty / DoubleProperty / LongProperty / StringProperty cells ---
    (
        "| key | string | The custom key of the property. |",
        "| key | string | Пользовательский ключ свойства. |",
    ),
    (
        "| value | string | The date value of the property. |",
        "| value | string | Значение свойства типа дата. |",
    ),
    (
        "| value | number | The floating-point numeric value of the property. |",
        "| value | number | Числовое значение свойства с плавающей точкой. |",
    ),
    (
        "| value | integer | The Long value of the property. |",
        "| value | integer | Значение свойства типа Long. |",
    ),
    (
        "| value | string | The string value of the property. |",
        "| value | string | Строковое значение свойства. |",
    ),
    # --- UserSessionErrors / UserSessionEvents cells ---
    (
        "| application | string | The name of the application, based on the configured detection rules. |",
        "| application | string | Имя приложения на основе настроенных правил обнаружения. |",
    ),
    (
        "| domain | string | The DNS domain where the error has been recorded. |",
        "| domain | string | DNS-домен, в котором была записана ошибка. |",
    ),
    (
        "| domain | string | The DNS domain where the event has been recorded. |",
        "| domain | string | DNS-домен, в котором было записано событие. |",
    ),
    (
        "| internalApplicationId | string | The Dynatrace entity ID of the application.  This information is useful when calling various REST APIs, for example, as a key for time series queries. |",
        "| internalApplicationId | string | ID сущности Dynatrace приложения.  Эта информация полезна при вызове различных REST API, например, в качестве ключа для запросов временных рядов. |",
    ),
    (
        "| name | string | The name of the error. |",
        "| name | string | Имя ошибки. |",
    ),
    (
        "| name | string | The name of the event. |",
        "| name | string | Имя события. |",
    ),
    (
        "| startTime | integer | The timestamp of the error, in UTC milliseconds. |",
        "| startTime | integer | Метка времени ошибки в миллисекундах UTC. |",
    ),
    (
        "| startTime | integer | The timestamp of the event, in UTC milliseconds. |",
        "| startTime | integer | Метка времени события в миллисекундах UTC. |",
    ),
    (
        "| type | string | The type of error. The element can hold these values * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |",
        "| type | string | Тип ошибки. Возможные значения: * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |",
    ),
    (
        "| type | string | The type of event. The element can hold these values * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |",
        "| type | string | Тип события. Возможные значения: * `Behavioral` * `Crash` * `Error` * `PageChange` * `RageClick` * `RageTap` * `UserTag` * `UserTagFromMetaData` * `VisitTag` |",
    ),
    (
        "| metadata | string | The metadata attached to the event. |",
        "| metadata | string | Метаданные, прикреплённые к событию. |",
    ),
    (
        "| page | string | The name of the page the user navigated to during a page change event. |",
        "| page | string | Имя страницы, на которую перешёл пользователь во время события смены страницы. |",
    ),
    (
        "| pageGroup | string | The page group is automatically derived from the page. |",
        "| pageGroup | string | Группа страниц автоматически выводится из страницы. |",
    ),
    (
        "| pageReferrer | string | The name of the previous page from which the user navigated from during a page change event. |",
        "| pageReferrer | string | Имя предыдущей страницы, с которой пользователь перешёл во время события смены страницы. |",
    ),
    (
        "| pageReferrerGroup | string | The page referrer group is automatically derived from the page referrer. |",
        "| pageReferrerGroup | string | Группа реферера страницы автоматически выводится из реферера страницы. |",
    ),
    # --- UserSessionSyntheticEvent cells ---
    (
        "| errorCode | integer | The error code of the error that occurred during this event. |",
        "| errorCode | integer | Код ошибки, произошедшей во время этого события. |",
    ),
    (
        "| errorName | string | Description of the error that occurred during this event. |",
        "| errorName | string | Описание ошибки, произошедшей во время этого события. |",
    ),
    (
        "| name | string | The name of the synthetic event. |",
        "| name | string | Имя synthetic-события. |",
    ),
    (
        "| sequenceNumber | integer | The sequence number of the synthetic event in scope of the complete browser monitor. |",
        "| sequenceNumber | integer | Порядковый номер synthetic-события в рамках полного браузерного монитора. |",
    ),
    (
        "| syntheticEventId | string | The Dynatrace entity ID for the synthetic event. |",
        "| syntheticEventId | string | ID сущности Dynatrace для synthetic-события. |",
    ),
    (
        "| timestamp | integer | The timestamp when the synthetic event was simulated, in UTC milliseconds. |",
        "| timestamp | integer | Метка времени, когда synthetic-событие было смоделировано, в миллисекундах UTC. |",
    ),
    (
        "| type | string | The type of the synthetic event. For example click or keystroke. |",
        "| type | string | Тип synthetic-события. Например, click или keystroke. |",
    ),
    # --- UserSessionUserAction cells (longest/most-specific FIRST) ---
    (
        "| apdexCategory | string | The [user experience index](https://dt-url.net/apdexdoc) of the user action. The element can hold these values * `FRUSTRATED` * `SATISFIED` * `TOLERATING` * `UNKNOWN` |",
        "| apdexCategory | string | [Индекс пользовательского опыта](https://dt-url.net/apdexdoc) пользовательского действия. Возможные значения: * `FRUSTRATED` * `SATISFIED` * `TOLERATING` * `UNKNOWN` |",
    ),
    (
        "| application | string | The name of the application where the user action has been recorded. |",
        "| application | string | Имя приложения, в котором было записано пользовательское действие. |",
    ),
    (
        "| cdnBusyTime | integer | The time spent waiting for CDN resources for the user action, in milliseconds. |",
        "| cdnBusyTime | integer | Время ожидания CDN-ресурсов для пользовательского действия в миллисекундах. |",
    ),
    (
        "| cdnResources | integer | The number of resources fetched from a CDN for the user action. |",
        "| cdnResources | integer | Количество ресурсов, полученных из CDN для пользовательского действия. |",
    ),
    (
        "| cumulativeLayoutShift | number | The cumulative layout shift (CLS) is the total amount of all individual scores for every unexpected layout shift that occurs during the entire lifespan of the page.  The CLS is an important user-centric metric for measuring visual stability. It quantifies how often users experience unexpected layout shifts. A low CLS indicates that the page is delightful. |",
        "| cumulativeLayoutShift | number | Cumulative layout shift (CLS) это суммарная величина всех отдельных оценок каждого неожиданного сдвига макета, происходящего в течение всего времени жизни страницы.  CLS это важная ориентированная на пользователя метрика для измерения визуальной стабильности. Она количественно оценивает, как часто пользователи сталкиваются с неожиданными сдвигами макета. Низкий CLS означает, что страница приятна в использовании. |",
    ),
    (
        "| customErrorCount | integer | The total number of custom errors during the user action. |",
        "| customErrorCount | integer | Общее количество пользовательских ошибок во время пользовательского действия. |",
    ),
    # dateProperties cell is byte-identical to the UserSession one above and is
    # already replaced there (str.replace hits all occurrences) -> omitted here
    # to avoid a redundant no-op MISS warning. Same for double/long/string.
    (
        "| documentInteractiveTime | integer | The amount of time spent until the document for the user action became interactive, in milliseconds. |",
        "| documentInteractiveTime | integer | Время, прошедшее до того, как документ для пользовательского действия стал интерактивным, в миллисекундах. |",
    ),
    (
        "| domCompleteTime | integer | The amount of time until the DOM tree is completed, in milliseconds. |",
        "| domCompleteTime | integer | Время до завершения построения DOM-дерева в миллисекундах. |",
    ),
    (
        "| domContentLoadedTime | integer | The amount of time until the DOM tree is loaded, in milliseconds. |",
        "| domContentLoadedTime | integer | Время до загрузки DOM-дерева в миллисекундах. |",
    ),
    (
        "| domain | string | The DNS domain where the user action has been recorded. |",
        "| domain | string | DNS-домен, в котором было записано пользовательское действие. |",
    ),
    # doubleProperties cell identical to UserSession one above (already replaced)
    (
        "| duration | integer | The duration of the user action, in milliseconds.  This is calculated as the of time between the start and the end timestamps of the user action. |",
        "| duration | integer | Длительность пользовательского действия в миллисекундах.  Вычисляется как промежуток времени между начальной и конечной метками времени пользовательского действия. |",
    ),
    (
        "| endTime | integer | The end timestamp of the user action, in UTC milliseconds. |",
        "| endTime | integer | Конечная метка времени пользовательского действия в миллисекундах UTC. |",
    ),
    (
        "| firstInputDelay | integer | The first input delay (FID) is the time (in milliseconds) that the browser took to respond to the first user input.  The FID is an important user-centric metric for measuring load responsiveness. It quantifies the user experience when trying to interact with unresponsive pages. A low FID indicates that the page is usable. |",
        "| firstInputDelay | integer | First input delay (FID) это время (в миллисекундах), которое потребовалось браузеру для реакции на первый пользовательский ввод.  FID это важная ориентированная на пользователя метрика для измерения отзывчивости при загрузке. Она количественно оценивает пользовательский опыт при попытке взаимодействия с неотзывчивыми страницами. Низкий FID означает, что страница пригодна к использованию. |",
    ),
    (
        "| firstPartyBusyTime | integer | The time spent waiting for resources from the originating server for the user action, in milliseconds. |",
        "| firstPartyBusyTime | integer | Время ожидания ресурсов с исходного сервера для пользовательского действия в миллисекундах. |",
    ),
    (
        "| firstPartyResources | integer | The number of resources fetched from the originating server for the user action. |",
        "| firstPartyResources | integer | Количество ресурсов, полученных с исходного сервера для пользовательского действия. |",
    ),
    (
        "| frontendTime | integer | The amount of time spent on the frontend rendering for the user action, in milliseconds. |",
        "| frontendTime | integer | Время, затраченное на рендеринг на фронтенде для пользовательского действия, в миллисекундах. |",
    ),
    (
        "| hasCrash | boolean | The user action has (`true`) or doesn't have (`false`) a crash. |",
        "| hasCrash | boolean | Пользовательское действие содержит (`true`) или не содержит (`false`) сбой. |",
    ),
    (
        "| internalApplicationId | string | The Dynatrace entity ID of the application where the user action has been recorded.  This information is useful when calling various REST APIs, for example as a key for time series queries. |",
        "| internalApplicationId | string | ID сущности Dynatrace приложения, в котором было записано пользовательское действие.  Эта информация полезна при вызове различных REST API, например в качестве ключа для запросов временных рядов. |",
    ),
    (
        "| internalKeyUserActionId | string | The Dynatrace entity ID of the key user action. |",
        "| internalKeyUserActionId | string | ID сущности Dynatrace ключевого пользовательского действия. |",
    ),
    (
        "| javascriptErrorCount | integer | The total number of Javascript errors during the user action. |",
        "| javascriptErrorCount | integer | Общее количество ошибок Javascript во время пользовательского действия. |",
    ),
    (
        "| keyUserAction | boolean | The action is (`true`) or is not (`false`) a key action. |",
        "| keyUserAction | boolean | Действие является (`true`) или не является (`false`) ключевым действием. |",
    ),
    (
        "| largestContentfulPaint | integer | The largest contentful paint (LCP) is the time (in milliseconds) that the largest element on the page took to render.  The LCP is an important user-centric metric for measuring load speed. It marks the point when the page's main content is likely loaded. A low LCP indicates that the page loads quickly. |",
        "| largestContentfulPaint | integer | Largest contentful paint (LCP) это время (в миллисекундах), которое потребовалось для рендеринга самого крупного элемента на странице.  LCP это важная ориентированная на пользователя метрика для измерения скорости загрузки. Она отмечает момент, когда основное содержимое страницы, вероятно, загружено. Низкий LCP означает, что страница загружается быстро. |",
    ),
    (
        "| loadEventEnd | integer | The amount of time until the load event ended, in milliseconds. |",
        "| loadEventEnd | integer | Время до окончания события load в миллисекундах. |",
    ),
    (
        "| loadEventStart | integer | The amount of time until the load event started, in milliseconds. |",
        "| loadEventStart | integer | Время до начала события load в миллисекундах. |",
    ),
    # longProperties cell identical to UserSession one above (already replaced)
    (
        "| matchingConversionGoals | string[] | A list of conversion goals achieved by the user action.  Additionally, you can define conversion goals for a user session as a whole. |",
        "| matchingConversionGoals | string[] | Список целей конверсии, достигнутых пользовательским действием.  Дополнительно можно задать цели конверсии для пользовательской сессии в целом. |",
    ),
    (
        "| name | string | The name of the user action.  Typically, this is the name of the page that is loaded as part of a user action or a textual description of the action, such as a mouse click. |",
        "| name | string | Имя пользовательского действия.  Обычно это имя страницы, загружаемой в рамках пользовательского действия, или текстовое описание действия, например щелчок мышью. |",
    ),
    (
        "| navigationStart | integer | The timestamp of the navigation start, in UTC milliseconds. |",
        "| navigationStart | integer | Метка времени начала навигации в миллисекундах UTC. |",
    ),
    (
        "| networkTime | integer | The amount of time spent on the data transfer for the user action, in milliseconds. |",
        "| networkTime | integer | Время, затраченное на передачу данных для пользовательского действия, в миллисекундах. |",
    ),
    (
        "| requestErrorCount | integer | The total number of request errors during the user action. |",
        "| requestErrorCount | integer | Общее количество ошибок запросов во время пользовательского действия. |",
    ),
    (
        "| requestStart | integer | The amount of time until the request started, in milliseconds. |",
        "| requestStart | integer | Время до начала запроса в миллисекундах. |",
    ),
    (
        "| responseEnd | integer | The amount of time until the response ended, in milliseconds. |",
        "| responseEnd | integer | Время до окончания ответа в миллисекундах. |",
    ),
    (
        "| responseStart | integer | The amount of time until the response started, in milliseconds. |",
        "| responseStart | integer | Время до начала ответа в миллисекундах. |",
    ),
    (
        "| serverTime | integer | The amount of time spent on the server-side processing for the user action, in milliseconds. |",
        "| serverTime | integer | Время, затраченное на серверную обработку для пользовательского действия, в миллисекундах. |",
    ),
    (
        "| speedIndex | integer | The [speed index](https://dt-url.net/qk1a3r19) of the user action, in milliseconds.  This is calculated as average time it takes for all visible parts of a page to display. |",
        "| speedIndex | integer | [Speed index](https://dt-url.net/qk1a3r19) пользовательского действия в миллисекундах.  Вычисляется как среднее время отображения всех видимых частей страницы. |",
    ),
    (
        "| startTime | integer | The start timestamp of the user action, in UTC milliseconds. |",
        "| startTime | integer | Начальная метка времени пользовательского действия в миллисекундах UTC. |",
    ),
    # stringProperties cell identical to UserSession one above (already replaced)
    (
        "| syntheticEvent | string | The name of the [Synthetic event](https://dt-url.net/dq1e3rmm) that triggered the user action. |",
        "| syntheticEvent | string | Имя [Synthetic-события](https://dt-url.net/dq1e3rmm), инициировавшего пользовательское действие. |",
    ),
    (
        "| syntheticEventId | string | The ID of the [Synthetic event](https://dt-url.net/dq1e3rmm) that triggered the user action. |",
        "| syntheticEventId | string | ID [Synthetic-события](https://dt-url.net/dq1e3rmm), инициировавшего пользовательское действие. |",
    ),
    (
        "| targetUrl | string | The target URL of the user action. |",
        "| targetUrl | string | Целевой URL пользовательского действия. |",
    ),
    (
        "| thirdPartyBusyTime | integer | The time spent waiting for third party resources for the user action, in milliseconds. |",
        "| thirdPartyBusyTime | integer | Время ожидания сторонних ресурсов для пользовательского действия в миллисекундах. |",
    ),
    (
        "| thirdPartyResources | integer | The number of third party resources loaded for the user action. |",
        "| thirdPartyResources | integer | Количество сторонних ресурсов, загруженных для пользовательского действия. |",
    ),
    (
        "| ~~totalBlockingTime~~ | integer | DEPRECATED  The total blocking time is the total time (in milliseconds) between the first contentful paint and the time to interactive, during which the browser has been blocked long enough to prevent input responsiveness. |",
        "| ~~totalBlockingTime~~ | integer | УСТАРЕЛО  Total blocking time это суммарное время (в миллисекундах) между first contentful paint и time to interactive, в течение которого браузер был заблокирован достаточно долго, чтобы помешать отзывчивости на ввод. |",
    ),
    (
        "| type | string | The type of the user action. The element can hold these values * `Custom` * `EndVisit` * `Error` * `Load` * `RageClick` * `SyntheticHiddenAction` * `UserSessionProperties` * `VisitTag` * `Xhr` |",
        "| type | string | Тип пользовательского действия. Возможные значения: * `Custom` * `EndVisit` * `Error` * `Load` * `RageClick` * `SyntheticHiddenAction` * `UserSessionProperties` * `VisitTag` * `Xhr` |",
    ),
    (
        "| userActionPropertyCount | integer | The total number of properties in the user action. |",
        "| userActionPropertyCount | integer | Общее количество свойств в пользовательском действии. |",
    ),
    (
        "| visuallyCompleteTime | integer | The amount of time until the page is [visually complete](https://dt-url.net/qk1a3r19), in milliseconds. |",
        "| visuallyCompleteTime | integer | Время до того, как страница станет [визуально завершённой](https://dt-url.net/qk1a3r19), в миллисекундах. |",
    ),
]


def build():
    written = []
    bad = []
    total_en = total_ru = 0
    for rel in FILES:
        ep = os.path.join(EN, rel.replace("/", os.sep))
        rp = os.path.join(RU, rel.replace("/", os.sep))
        with io.open(ep, "r", encoding="utf-8", newline="") as f:
            txt = f.read()
        en_lines = txt.replace("\r\n", "\n").count("\n")
        txt = _normalize(txt)
        for en, ru in P.get(rel, []):
            if en not in txt:
                print(f"  !! MISS per-file in {rel}: {en[:70]!r}")
            txt = txt.replace(en, ru)
        for en, ru in COMMON:
            txt = txt.replace(en, ru)
        os.makedirs(os.path.dirname(rp), exist_ok=True)
        with io.open(rp, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        ru_lines = txt.count("\n")
        total_en += en_lines
        total_ru += ru_lines
        flag = "" if en_lines == ru_lines else "  <<< MISMATCH"
        if flag:
            bad.append(rel)
        print(f"{en_lines:5d} EN | {ru_lines:5d} RU  {rel}{flag}")
        written.append(rel)
    print(f"\nTOTAL  {total_en} EN | {total_ru} RU   files={len(written)}")
    if bad:
        print("MISMATCH FILES:", bad)
    else:
        print("OK: all files line-parity equal")
    return written


if __name__ == "__main__":
    build()
