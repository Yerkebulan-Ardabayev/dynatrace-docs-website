#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Splice-builder for batch L4S: configuration-api/rum/ 4 simple twin subsections
(allowed-beacon-cors / content-resources / geographic-regions-ip-address /
geographic-regions-ip-header) = 4 parents + 8 get/put-configuration endpoints.

EN -> RU exact-string replacement only (no newline added/removed) =>
line-parity automatic, code-fence byte-identical (L98/L100). EN is CRLF =>
normalize to LF first (L4M lesson). ACTIVE API, no deprecated banner (L89/L90).

Canon: L99 config-api (title/H1x2/`* Reference`/`* Published` EN-verbatim;
`## Validate payload`/`#### Curl` EN; "The element can hold these values" ->
"Возможные значения:" WITH colon; shared Error/ErrorEnvelope/ConstraintViolation/
ConfigurationMetadata from k8s-credentials RU). L101: period-by-source handled
naturally via substring `Failed. The input is invalid` (period stays outside the
match). L4I: validate-204 "Validated."-prefix kept where source says "Validated."
(content-resources only); "Success." -> "Успех." elsewhere. L4O: Related-topics
link-text = target RU H1 verbatim. L103 case (b): env-api/rum not translated ->
anchor = aws-privatelink RU (L4R, same get/put-configuration twin) + plugins-api
L4N shared-object canon. BOM `ï»¿` stripped from inline link-text.
"""

import os, sys

ROOT = r"C:\Users\yerke\Desktop\Code_and_Develop\my_develop_code\dynatrace-docs-website"
EN = os.path.join(ROOT, r"docs\managed\dynatrace-api\configuration-api\rum")
RU = os.path.join(ROOT, r"docs\managed-ru\dynatrace-api\configuration-api\rum")

FILES = [
    "allowed-beacon-cors.md",
    "allowed-beacon-cors/get-configuration.md",
    "allowed-beacon-cors/put-configuration.md",
    "content-resources.md",
    "content-resources/get-configuration.md",
    "content-resources/put-configuration.md",
    "geographic-regions-ip-address.md",
    "geographic-regions-ip-address/get-configuration.md",
    "geographic-regions-ip-address/put-configuration.md",
    "geographic-regions-ip-header.md",
    "geographic-regions-ip-header/get-configuration.md",
    "geographic-regions-ip-header/put-configuration.md",
]

# ---------------------------------------------------------------- COMMON
# Applied AFTER per-file (so long unique per-file cells replace wholesale
# first). Each entry is within-line => line-parity preserved. Ordered
# longest/most-specific first to avoid substring collisions.
COMMON = [
    # --- structural headers (newline-anchored: avoids "## Response" matching
    #     inside "### Response") ---
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n#### Response body objects\n", "\n#### Объекты тела ответа\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n#### Response body JSON models\n", "\n#### JSON-модели тела ответа\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n#### Response codes\n", "\n#### Коды ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response\n", "\n### Ответ\n"),
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # `## Validate payload` / `#### Curl` => EN-verbatim (L99 ALLOWED_EN)
    # --- table headers ---
    (
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    # --- object headers (longer names first; backtick-delimited so no real
    #     collision, ordered defensively) ---
    ("#### The `AllowedBeaconOrigins` object", "#### Объект `AllowedBeaconOrigins`"),
    ("#### The `BeaconDomainPattern` object", "#### Объект `BeaconDomainPattern`"),
    ("#### The `ConfigurationMetadata` object", "#### Объект `ConfigurationMetadata`"),
    ("#### The `ContentResources` object", "#### Объект `ContentResources`"),
    ("#### The `ResourceProvider` object", "#### Объект `ResourceProvider`"),
    (
        "#### The `ResourceUrlCleanupRule` object",
        "#### Объект `ResourceUrlCleanupRule`",
    ),
    ("#### The `ResourceType` object", "#### Объект `ResourceType`"),
    (
        "#### The `IpAddressMappingLocation` object",
        "#### Объект `IpAddressMappingLocation`",
    ),
    ("#### The `IpAddressMappingRule` object", "#### Объект `IpAddressMappingRule`"),
    ("#### The `IpAddressMappings` object", "#### Объект `IpAddressMappings`"),
    ("#### The `IpAddressRange` object", "#### Объект `IpAddressRange`"),
    ("#### The `IpDetectionHeaders` object", "#### Объект `IpDetectionHeaders`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    # --- shared boilerplate prose ---
    (
        "To execute this request, you need an access token with `ReadConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `ReadConfig`.",
    ),
    (
        "To execute this request, you need an access token with `WriteConfig` scope.",
        "Для выполнения этого запроса нужен access token со scope `WriteConfig`.",
    ),
    (
        "To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
        "Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).",
    ),
    (
        "The request doesn't provide any configurable parameters.",
        "В запросе нет настраиваемых параметров.",
    ),
    (
        "The request produces an `application/json` payload.",
        "Запрос возвращает payload `application/json`.",
    ),
    (
        "The request consumes an `application/json` payload.",
        "Запрос принимает payload `application/json`.",
    ),
    (
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется проверить payload перед его отправкой в реальном запросе. Код ответа **204** означает, что payload корректен.",
    ),
    # --- response-code cells (L101: period stays outside the matched span) ---
    (
        "Success. The configuration has been updated. Response doesn't have a body.",
        "Успех. Конфигурация обновлена. Ответ без тела.",
    ),
    (
        "Success. The submitted configuration is valid. Response doesn't have a body.",
        "Успех. Переданная конфигурация валидна. Ответ без тела.",
    ),
    (
        "Validated. The submitted configuration is valid. Response doesn't have a body.",
        "Validated. Переданная конфигурация валидна. Ответ без тела.",
    ),
    ("Failed. The input is invalid", "Сбой. Невалидный ввод"),
    ("| Success |", "| Успех |"),
    # --- "The element can hold these values" -> "Возможные значения:" WITH
    #     colon (L99; also handles leading-dash `-The element ...`) ---
    ("The element can hold these values", "Возможные значения:"),
    # --- shared Error / ConstraintViolation / ConfigurationMetadata canon
    #     (verbatim from plugins-api L4N RU) ---
    (
        "| code | integer | The HTTP status code |",
        "| code | integer | HTTP-код статуса |",
    ),
    (
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |",
        "| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |",
    ),
    (
        "| message | string | The error message |",
        "| message | string | Сообщение об ошибке |",
    ),
    ("| Dynatrace version. |", "| Версия Dynatrace. |"),
    (
        "A sorted list of the version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    (
        "A sorted list of version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    ("Metadata useful for debugging", "Метаданные для отладки"),
    # ConstraintViolation object-intro line (standalone, after the full
    # constraintViolations cell above is already consumed)
    ("\nA list of constraint violations\n", "\nСписок нарушений ограничений\n"),
]

# ---------------------------------------------------------------- PER-FILE
# Long/unique strings; applied before COMMON. Authored longest-first.
P = {}

# ---- allowed-beacon-cors (parent) ----
P["allowed-beacon-cors.md"] = [
    (
        "The **Allowed beacon domains** API enables you to manage the list of RUM beacon origins that must be accepted by OneAgent and ActiveGate.",
        "API **Allowed beacon domains** позволяет управлять списком RUM beacon origins, которые должны приниматься OneAgent и ActiveGate.",
    ),
    (
        "To manage the RUM beacon origins list in the Dynatrace web UI, go to **Settings** > **Web and mobile monitoring** > **Beacon origins for CORS**.",
        "Для управления списком RUM beacon origins в веб-интерфейсе Dynatrace перейдите в **Settings** > **Web and mobile monitoring** > **Beacon origins for CORS**.",
    ),
    (
        'Get an overview of allowed beacon origins.](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/get-configuration "Read allowed beacon domains list via the Dynatrace API.")[### Update configuration',
        'Обзор разрешённых beacon origins.](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/get-configuration "Просмотр списка Allowed beacon domains через Dynatrace API.")[### Обновление конфигурации',
    ),
    (
        'Update configuration of allowed beacon origins.](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/put-configuration "Update allowed beacon domains list via the Dynatrace API.")',
        'Обновление конфигурации разрешённых beacon origins.](/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/put-configuration "Обновление списка Allowed beacon domains через Dynatrace API.")',
    ),
    (
        '* [Configure beacon origin allowlist for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Specify the origins from which cross-origin RUM beacons should be accepted.")',
        '* [Настройка allowlist источников маяков для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-beacon-domain-allowlist "Укажите источники, из которых должны приниматься кросс-доменные RUM-маяки.")',
    ),
    ("[### View configuration", "[### Просмотр конфигурации"),
]

# ---- allowed-beacon-cors/get-configuration ----
P["allowed-beacon-cors/get-configuration.md"] = [
    (
        "Gets the configuration of the allowed beacon origins for Cross Origin Resource Sharing (CORS) requests.",
        "Возвращает конфигурацию разрешённых beacon origins для запросов Cross Origin Resource Sharing (CORS).",
    ),
    (
        "Configuration of the allowed beacon origins for CORS requests.",
        "Конфигурация разрешённых beacon origins для запросов CORS.",
    ),
    (
        "Allowed beacon origin for CORS requests.",
        "Разрешённый beacon origin для запросов CORS.",
    ),
    (
        "A list of allowed beacon origins for CORS requests.",
        "Список разрешённых beacon origins для запросов CORS.",
    ),
    (
        "Discard (`true`) or keep (`false`) beacons without the **Origin** HTTP header on the BeaconForwarder.  If not set, `false` is used.",
        "Отбрасывать (`true`) или сохранять (`false`) beacon'ы без HTTP-заголовка **Origin** на BeaconForwarder.  Если не задано, используется `false`.",
    ),
    (
        "The matching operation for the **domainNamePattern**.",
        "Операция сопоставления для **domainNamePattern**.",
    ),
    ("The pattern of the allowed domain name.", "Шаблон разрешённого доменного имени."),
]

# ---- allowed-beacon-cors/put-configuration ----
P["allowed-beacon-cors/put-configuration.md"] = [
    (
        "Updates the configuration of the allowed beacon origins for Cross Origin Resource Sharing (CORS) requests.",
        "Обновляет конфигурацию разрешённых beacon origins для запросов Cross Origin Resource Sharing (CORS).",
    ),
    (
        "The JSON body of the request. Contains the configuration of the allowed beacon origins for CORS requests.",
        "JSON-тело запроса. Содержит конфигурацию разрешённых beacon origins для запросов CORS.",
    ),
    (
        "Configuration of the allowed beacon origins for CORS requests.",
        "Конфигурация разрешённых beacon origins для запросов CORS.",
    ),
    (
        "Allowed beacon origin for CORS requests.",
        "Разрешённый beacon origin для запросов CORS.",
    ),
    (
        "A list of allowed beacon origins for CORS requests.",
        "Список разрешённых beacon origins для запросов CORS.",
    ),
    (
        "Discard (`true`) or keep (`false`) beacons without the **Origin** HTTP header on the BeaconForwarder.  If not set, `false` is used.",
        "Отбрасывать (`true`) или сохранять (`false`) beacon'ы без HTTP-заголовка **Origin** на BeaconForwarder.  Если не задано, используется `false`.",
    ),
    (
        "The matching operation for the **domainNamePattern**.",
        "Операция сопоставления для **domainNamePattern**.",
    ),
    ("The pattern of the allowed domain name.", "Шаблон разрешённого доменного имени."),
]

# ---- content-resources (parent) ----
P["content-resources.md"] = [
    (
        "The **Content resources** API enables you to manage the configuration of content providers. You can also manage the same configuration in the Dynatrace UI at **Settings > Web and mobile monitoring > Content resources**.",
        "API **Content resources** позволяет управлять конфигурацией провайдеров контента. Той же конфигурацией можно управлять в интерфейсе Dynatrace в **Settings > Web and mobile monitoring > Content resources**.",
    ),
    (
        'Get an overview of content providers configuration.](/managed/dynatrace-api/configuration-api/rum/content-resources/get-configuration "Read the configuration of content providers via the Dynatrace API.")[### Update configuration',
        'Обзор конфигурации провайдеров контента.](/managed/dynatrace-api/configuration-api/rum/content-resources/get-configuration "Просмотр конфигурации провайдеров контента через Dynatrace API.")[### Обновление конфигурации',
    ),
    (
        'Update configuration of content providers.](/managed/dynatrace-api/configuration-api/rum/content-resources/put-configuration "Update the configuration of content providers via the Dynatrace API.")',
        'Обновление конфигурации провайдеров контента.](/managed/dynatrace-api/configuration-api/rum/content-resources/put-configuration "Обновление конфигурации провайдеров контента через Dynatrace API.")',
    ),
    (
        '* [Configure first-party, third-party, and CDN resource detection for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.")',
        '* [Настройка обнаружения ресурсов первой, сторонних сторон и CDN для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших веб-приложений.")',
    ),
    (
        '* [Configure first-party, third-party, and CDN resource detection for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Manually define third-party and CDN providers along with auto-detected providers for your mobile applications.")',
        '* [Настройка определения собственных, сторонних ресурсов и ресурсов CDN для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-third-party-and-cdn-content-detection-mobile "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших мобильных приложений.")',
    ),
    (
        '* [Configure first-party, third-party, and CDN resource detection for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Manually define third-party and CDN providers along with auto-detected providers for your custom applications.")',
        '* [Настройка обнаружения ресурсов первой стороны, сторонних ресурсов и CDN в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-third-party-and-cdn-content-detection-custom "Вручную задайте сторонних провайдеров и провайдеров CDN наряду с автоматически обнаруженными для ваших пользовательских приложений.")',
    ),
    ("[### View configuration", "[### Просмотр конфигурации"),
]

# Related-topics bullets shared by content-resources get/put endpoints
_CR_RELATED = [
    r for r in P["content-resources.md"] if r[0].startswith("* [Configure first-party")
]

# ---- content-resources/get-configuration ----
P["content-resources/get-configuration.md"] = [
    (
        "Gets the configuration of content providers in your Dynatrace environment.",
        "Возвращает конфигурацию провайдеров контента в вашем окружении Dynatrace.",
    ),
    (
        "An ordered list of manually added content providers.  Rules are evaluated from top to bottom; the first matching rules applies.",
        "Упорядоченный список вручную добавленных провайдеров контента.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    (
        "An ordered list of manually defined resource types.  Rules are evaluated from top to bottom; the first matching rules applies.",
        "Упорядоченный список вручную заданных типов ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    (
        "An ordered list of resource URL cleanup rules.  Rules are evaluated from top to bottom; the first matching rules applies.",
        "Упорядоченный список правил очистки URL ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    ("The configuration of content resources.", "Конфигурация ресурсов контента."),
    ("A rule for the content provider.", "Правило для провайдера контента."),
    ("A rule for the resource type.", "Правило для типа ресурса."),
    ("A rule for the URL cleanup rule.", "Правило очистки URL."),
    ("The URL of the provider's icon.", "URL иконки провайдера."),
    (
        "A list of domain patterns of the provider.",
        "Список доменных шаблонов провайдера.",
    ),
    ("The name of the provider.", "Имя провайдера."),
    ("The type of the provider.", "Тип провайдера."),
    ("The primary type of the resource.", "Основной тип ресурса."),
    (
        "The regular expression to detect the resource.",
        "Регулярное выражение для обнаружения ресурса.",
    ),
    ("The secondary type of the resource.", "Вторичный тип ресурса."),
    (
        "The pattern (regular expression) to look for.",
        "Шаблон (регулярное выражение) для поиска.",
    ),
    (
        "The text to replace the found pattern with.",
        "Текст для замены найденного шаблона.",
    ),
    ("The name of the rule.", "Имя правила."),
] + _CR_RELATED

# ---- content-resources/put-configuration ----
P["content-resources/put-configuration.md"] = [
    (
        "Updates the configuration of content providers in your Dynatrace environment.",
        "Обновляет конфигурацию провайдеров контента в вашем окружении Dynatrace.",
    ),
    (
        "The JSON body of the request. Contains the configuration of content resources.",
        "JSON-тело запроса. Содержит конфигурацию ресурсов контента.",
    ),
    (
        "An ordered list of manually added content providers.  Rules are evaluated from top to bottom; the first matching rules applies.",
        "Упорядоченный список вручную добавленных провайдеров контента.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    (
        "An ordered list of manually defined resource types.  Rules are evaluated from top to bottom; the first matching rules applies.",
        "Упорядоченный список вручную заданных типов ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    (
        "An ordered list of resource URL cleanup rules.  Rules are evaluated from top to bottom; the first matching rules applies.",
        "Упорядоченный список правил очистки URL ресурсов.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    ("The configuration of content resources.", "Конфигурация ресурсов контента."),
    ("A rule for the content provider.", "Правило для провайдера контента."),
    ("A rule for the resource type.", "Правило для типа ресурса."),
    ("A rule for the URL cleanup rule.", "Правило очистки URL."),
    ("The URL of the provider's icon.", "URL иконки провайдера."),
    (
        "A list of domain patterns of the provider.",
        "Список доменных шаблонов провайдера.",
    ),
    ("The name of the provider.", "Имя провайдера."),
    ("The type of the provider.", "Тип провайдера."),
    ("The primary type of the resource.", "Основной тип ресурса."),
    (
        "The regular expression to detect the resource.",
        "Регулярное выражение для обнаружения ресурса.",
    ),
    ("The secondary type of the resource.", "Вторичный тип ресурса."),
    (
        "The pattern (regular expression) to look for.",
        "Шаблон (регулярное выражение) для поиска.",
    ),
    (
        "The text to replace the found pattern with.",
        "Текст для замены найденного шаблона.",
    ),
    ("The name of the rule.", "Имя правила."),
] + _CR_RELATED

# ---- geographic-regions-ip-address (parent) ----
P["geographic-regions-ip-address.md"] = [
    (
        "The **Geographic regions - IP address mapping rules** API enables you to manage the configuration of IP address mapping to geographic locations. You can also manage the same configuration in the Dynatrace UI at **Settings > Web and mobile monitoring > Map IP addresses to locations**.",
        "API **Geographic regions - IP address mapping rules** позволяет управлять конфигурацией сопоставления IP-адресов с географическими расположениями. Той же конфигурацией можно управлять в интерфейсе Dynatrace в **Settings > Web and mobile monitoring > Map IP addresses to locations**.",
    ),
    (
        'Get an overview of IP address mappings.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration "Read the configuration of IP address mapping via the Dynatrace API.")[### Update configuration',
        'Обзор сопоставлений IP-адресов.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration "Просмотр конфигурации сопоставления IP-адресов через Dynatrace API.")[### Обновление конфигурации',
    ),
    (
        'Update configuration of IP address mappings.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Update the configuration of IP address mapping via the Dynatrace API.")',
        'Обновление конфигурации сопоставлений IP-адресов.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration "Обновление конфигурации сопоставления IP-адресов через Dynatrace API.")',
    ),
    (
        '* [Map internal IP addresses to locations for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")',
        '* [Сопоставление внутренних IP-адресов с расположениями для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших веб-приложений.")',
    ),
    (
        '* [Map internal IP addresses to locations for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")',
        '* [Сопоставление внутренних IP-адресов с местоположениями для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших мобильных приложений.")',
    ),
    (
        '* [Map internal IP addresses to locations for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")',
        '* [Сопоставление внутренних IP-адресов с местоположениями в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Настройте Dynatrace на использование локальных адресов, чтобы понимать, где находятся пользователи ваших пользовательских приложений.")',
    ),
    ("[### View configuration", "[### Просмотр конфигурации"),
]
_IPA_RELATED = [
    r
    for r in P["geographic-regions-ip-address.md"]
    if r[0].startswith("* [Map internal")
]

# ---- geographic-regions-ip-address/get-configuration ----
P["geographic-regions-ip-address/get-configuration.md"] = [
    (
        "Gets the configuration of mapping between IP addresses and geographic regions.",
        "Возвращает конфигурацию сопоставления между IP-адресами и географическими регионами.",
    ),
    (
        "The country code of the location.  To fetch the list of available country codes, use the [GET all countries\xef\xbb\xbf](https://dt-url.net/37030go) request.",
        "Код страны расположения.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go).",
    ),
    (
        "The region code of the location.  To fetch the list of available region codes, use the [GET regions of the country\xef\xbb\xbf](https://dt-url.net/az230x0) request.",
        "Код региона расположения.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0).",
    ),
    (
        "A list of IP address mapping rules.  Rules are evaluated from top to bottom; the first matching rule applies.",
        "Список правил сопоставления IP-адресов.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    (
        "Configuration of the IP address mappings to geographic locations.",
        "Конфигурация сопоставлений IP-адресов с географическими расположениями.",
    ),
    (
        "Configuration of the IP address mapping to the geographic location.",
        "Конфигурация сопоставления IP-адреса с географическим расположением.",
    ),
    (
        "The IP address or the IP address range to be mapped to the location.",
        "IP-адрес или диапазон IP-адресов для сопоставления с расположением.",
    ),
    (
        "The location for an IP address mapping.",
        "Расположение для сопоставления IP-адреса.",
    ),
    ("The city name of the location.", "Название города расположения."),
    (
        "The latitude of the location in `DDD.dddd` format.",
        "Широта расположения в формате `DDD.dddd`.",
    ),
    (
        "The longitude of the location in `DDD.dddd` format.",
        "Долгота расположения в формате `DDD.dddd`.",
    ),
    (
        "The IP address to be mapped.  For an IP address range, this is the **from** address.",
        "IP-адрес для сопоставления.  Для диапазона IP-адресов это адрес **from**.",
    ),
    (
        "The **to** address of the IP address range.",
        "Адрес **to** диапазона IP-адресов.",
    ),
    ("The subnet mask of the IP address range.", "Маска подсети диапазона IP-адресов."),
] + _IPA_RELATED

# ---- geographic-regions-ip-address/put-configuration ----
P["geographic-regions-ip-address/put-configuration.md"] = [
    (
        "Updates the configuration of mapping between IP addresses and geographic regions.",
        "Обновляет конфигурацию сопоставления между IP-адресами и географическими регионами.",
    ),
    (
        "The JSON body of the request. Contains the configuration of the IP address mapping.",
        "JSON-тело запроса. Содержит конфигурацию сопоставления IP-адресов.",
    ),
    (
        "The country code of the location.  To fetch the list of available country codes, use the [GET all countries\xef\xbb\xbf](https://dt-url.net/37030go) request.",
        "Код страны расположения.  Чтобы получить список доступных кодов стран, используйте запрос [GET all countries](https://dt-url.net/37030go).",
    ),
    (
        "The region code of the location.  To fetch the list of available region codes, use the [GET regions of the country\xef\xbb\xbf](https://dt-url.net/az230x0) request.",
        "Код региона расположения.  Чтобы получить список доступных кодов регионов, используйте запрос [GET regions of the country](https://dt-url.net/az230x0).",
    ),
    (
        "A list of IP address mapping rules.  Rules are evaluated from top to bottom; the first matching rule applies.",
        "Список правил сопоставления IP-адресов.  Правила оцениваются сверху вниз; применяется первое подходящее правило.",
    ),
    (
        "Configuration of the IP address mappings to geographic locations.",
        "Конфигурация сопоставлений IP-адресов с географическими расположениями.",
    ),
    (
        "Configuration of the IP address mapping to the geographic location.",
        "Конфигурация сопоставления IP-адреса с географическим расположением.",
    ),
    (
        "The IP address or the IP address range to be mapped to the location.",
        "IP-адрес или диапазон IP-адресов для сопоставления с расположением.",
    ),
    (
        "The location for an IP address mapping.",
        "Расположение для сопоставления IP-адреса.",
    ),
    ("The city name of the location.", "Название города расположения."),
    (
        "The latitude of the location in `DDD.dddd` format.",
        "Широта расположения в формате `DDD.dddd`.",
    ),
    (
        "The longitude of the location in `DDD.dddd` format.",
        "Долгота расположения в формате `DDD.dddd`.",
    ),
    (
        "The IP address to be mapped.  For an IP address range, this is the **from** address.",
        "IP-адрес для сопоставления.  Для диапазона IP-адресов это адрес **from**.",
    ),
    (
        "The **to** address of the IP address range.",
        "Адрес **to** диапазона IP-адресов.",
    ),
    ("The subnet mask of the IP address range.", "Маска подсети диапазона IP-адресов."),
] + _IPA_RELATED

# ---- geographic-regions-ip-header (parent) ----
P["geographic-regions-ip-header.md"] = [
    (
        "The **Geographic regions - IP mapping headers** API enables you to manage the configuration of IP address mapping to geographic locations. You can also manage the same configuration in the Dynatrace UI at **Settings > Web and mobile monitoring > IP determination**.",
        "API **Geographic regions - IP mapping headers** позволяет управлять конфигурацией сопоставления IP-адресов с географическими расположениями. Той же конфигурацией можно управлять в интерфейсе Dynatrace в **Settings > Web and mobile monitoring > IP determination**.",
    ),
    (
        'Get an overview of IP address mappings.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/get-configuration "Read the configuration of IP mapping headers via the Dynatrace API.")[### Update configuration',
        'Обзор сопоставлений IP-адресов.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/get-configuration "Просмотр конфигурации IP mapping headers через Dynatrace API.")[### Обновление конфигурации',
    ),
    (
        'Update configuration of IP address mappings.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/put-configuration "Update the configuration of IP mapping headers via the Dynatrace API.")',
        'Обновление конфигурации сопоставлений IP-адресов.](/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/put-configuration "Обновление конфигурации IP mapping headers через Dynatrace API.")',
    ),
    (
        '* [Customize IP address detection for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications.")',
        '* [Настройка определения IP-адресов для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Измените способ, которым Dynatrace определяет клиентские IP-адреса для ваших веб-приложений.")',
    ),
    (
        '* [Customize IP address detection for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Change the way Dynatrace determines client IP addresses for your mobile applications.")',
        '* [Настройка определения IP-адресов для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Измените способ, которым Dynatrace определяет клиентские IP-адреса для ваших мобильных приложений.")',
    ),
    (
        '* [Customize IP address detection for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Change the way Dynatrace determines client IP addresses for your custom applications.")',
        '* [Настройка определения IP-адресов в пользовательских приложениях](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Измените способ, которым Dynatrace определяет клиентские IP-адреса для ваших пользовательских приложений.")',
    ),
    ("[### View configuration", "[### Просмотр конфигурации"),
]
_IPH_RELATED = [
    r
    for r in P["geographic-regions-ip-header.md"]
    if r[0].startswith("* [Customize IP")
]

# ---- geographic-regions-ip-header/get-configuration ----
P["geographic-regions-ip-header/get-configuration.md"] = [
    (
        "Gets the list of IP detection headers.",
        "Возвращает список заголовков определения IP.",
    ),
    (
        "A list of custom client IP headers.  Headers are evaluated from top to bottom; the first matching header applies.",
        "Список пользовательских клиентских IP-заголовков.  Заголовки оцениваются сверху вниз; применяется первый подходящий заголовок.",
    ),
    (
        "Configuration of the custom client IP headers.",
        "Конфигурация пользовательских клиентских IP-заголовков.",
    ),
] + _IPH_RELATED

# ---- geographic-regions-ip-header/put-configuration ----
P["geographic-regions-ip-header/put-configuration.md"] = [
    (
        "Updates the list of IP detection headers.",
        "Обновляет список заголовков определения IP.",
    ),
    (
        "The JSON body of the request. Contains the configuration of the custom client IP headers.",
        "JSON-тело запроса. Содержит конфигурацию пользовательских клиентских IP-заголовков.",
    ),
    (
        "A list of custom client IP headers.  Headers are evaluated from top to bottom; the first matching header applies.",
        "Список пользовательских клиентских IP-заголовков.  Заголовки оцениваются сверху вниз; применяется первый подходящий заголовок.",
    ),
    (
        "Configuration of the custom client IP headers.",
        "Конфигурация пользовательских клиентских IP-заголовков.",
    ),
] + _IPH_RELATED


def build():
    written = []
    for rel in FILES:
        ep = os.path.join(EN, rel.replace("/", os.sep))
        rp = os.path.join(RU, rel.replace("/", os.sep))
        with open(ep, "r", encoding="utf-8") as f:
            txt = f.read()
        # L4M: EN is CRLF -> normalize to LF before replacements, strip BOM
        txt = txt.replace("\r\n", "\n")
        if txt.startswith("﻿"):
            txt = txt[1:]
        for en, ru in P.get(rel, []):
            if en not in txt:
                print(f"  !! MISS per-file in {rel}: {en[:60]!r}")
            txt = txt.replace(en, ru)
        for en, ru in COMMON:
            txt = txt.replace(en, ru)
        os.makedirs(os.path.dirname(rp), exist_ok=True)
        with open(rp, "w", encoding="utf-8", newline="") as f:
            f.write(txt)
        written.append(rel)
    print(f"built {len(written)} files -> {RU}")
    return written


if __name__ == "__main__":
    build()
    sys.exit(0)
