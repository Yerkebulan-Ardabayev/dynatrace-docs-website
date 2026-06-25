# -*- coding: utf-8 -*-
"""L4P builder: configuration-api/extensions-api/ parent + 15 endpoints.
Splice method (L98/L100): start from EN, CRLF->LF, BOM-strip, apply ordered
exact-string canon replacements -> byte-identical JSON + line parity.
ACTIVE API (no deprecated banner, L89/L90). No env-api twin ->
L103 case (b): anchor = config-api L99 + k8s-credentials RU shared
objects (EntityShortRepresentation/StubList/Error/ConstraintViolation/
ConfigurationMetadata), plus plugins-api L4N sibling canon.
Domain corpus-dominant (L4I/L4J/L4O): "extension"->"расширение" (159x),
"instance"->"экземпляр" (corpus), "endpoint"->"эндпоинт";
EN-lock: "host group"/"management zone" (L4B canon + corpus-dominant),
object-names/enum/ActiveGate/OneAgent/JMX, title/H1x2 (L99).
L101: extensions-api ALL `Failed. The input is invalid` WITHOUT period
(grep-verified; OPPOSITE of plugins-api L4N which was WITH period).
Related-topics: link-text EN (target develop-your-extensions not
translated), title-attr per established extensions-family RU canon."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
EA = "extensions-api"

FILES = [
    f"{EA}.md",
    f"{EA}/get-all-extensions.md",
    f"{EA}/get-an-extension.md",
    f"{EA}/get-state.md",
    f"{EA}/post-an-extension.md",
    f"{EA}/get-extension-file.md",
    f"{EA}/del-extension-file.md",
    f"{EA}/get-all-instances.md",
    f"{EA}/get-an-instance.md",
    f"{EA}/post-instance.md",
    f"{EA}/put-instance.md",
    f"{EA}/del-instance.md",
    f"{EA}/get-global-configuration.md",
    f"{EA}/put-global-configuration.md",
    f"{EA}/get-all-ag-modules.md",
    f"{EA}/get-available-hosts.md",
]

# Ordered (EN, RU): specific/longer before any that could be substrings.
R = [
    # ---------- (A) PARENT card title-attrs (longest unique strings first) ----------
    (
        "Download the binary (.zip) file of an extension from your environment via the Dynatrace API.",
        "Скачивание бинарного (.zip) файла расширения из вашего окружения через Dynatrace API.",
    ),
    (
        "Delete the binary (.zip) file of an extension from your environment via the Dynatrace API.",
        "Удаление бинарного (.zip) файла расширения из вашего окружения через Dynatrace API.",
    ),
    (
        "View all instances of an extension uploaded to your environment via the Dynatrace API.",
        "Просмотр всех экземпляров расширения, загруженного в ваше окружение, через Dynatrace API.",
    ),
    (
        "Delete an instance of an extension uploaded to your environment via the Dynatrace API.",
        "Удаление экземпляра расширения, загруженного в ваше окружение, через Dynatrace API.",
    ),
    (
        "View all ActiveGate extension modules of your environment via the Dynatrace API.",
        "Просмотр всех модулей расширений ActiveGate вашего окружения через Dynatrace API.",
    ),
    (
        "Use Dynatrace API to view all extensions uploaded to your environment.",
        "Просмотр всех расширений, загруженных в ваше окружение, через Dynatrace API.",
    ),
    (
        "Use the Dynatrace API to view an extension uploaded to your environment.",
        "Просмотр расширения, загруженного в ваше окружение, через Dynatrace API.",
    ),
    (
        "View the status of an endpoint of an extension via the Dynatrace API.",
        "Просмотр статуса эндпоинта расширения через Dynatrace API.",
    ),
    (
        "Upload an extension file to your environment via the Dynatrace API.",
        "Загрузка файла расширения в ваше окружение через Dynatrace API.",
    ),
    (
        "View all hosts in your environment that run a certain technology.",
        "Просмотр всех хостов вашего окружения, на которых работает определённая технология.",
    ),
    (
        "Create an instance in an extension via the Dynatrace API.",
        "Создание экземпляра в расширении через Dynatrace API.",
    ),
    (
        "Edit an instance in an extension via the Dynatrace API.",
        "Редактирование экземпляра в расширении через Dynatrace API.",
    ),
    (
        "Check global configuration of an extension via the Dynatrace API.",
        "Просмотр глобальной конфигурации расширения через Dynatrace API.",
    ),
    (
        "Update global configuration of an extension via the Dynatrace API.",
        "Обновление глобальной конфигурации расширения через Dynatrace API.",
    ),
    (
        "View an instance of an extension via the Dynatrace API.",
        "Просмотр экземпляра расширения через Dynatrace API.",
    ),
    # ---------- (B) PARENT card descriptions ----------
    (
        "Get an overview of all extensions available in your Dynatrace environment.",
        "Обзор всех расширений, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Get an overview of all ActiveGate extension modules available in your Dynatrace environment.",
        "Обзор всех модулей расширений ActiveGate, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Create a new instance for an extension with the exact parameters you need.",
        "Создать новый экземпляр для расширения с нужными вам параметрами.",
    ),
    (
        "Check which hosts run the technology you're interested in.",
        "Проверить, на каких хостах работает интересующая вас технология.",
    ),
    (
        "Get a list of available instances of an extension.",
        "Получить список доступных экземпляров расширения.",
    ),
    (
        "Get parameters of an extension's instance by its ID.",
        "Получить параметры экземпляра расширения по его ID.",
    ),
    ("Get extension parameters by its ID.", "Получить параметры расширения по его ID."),
    (
        "Get a list of possible states of an extension.",
        "Получить список возможных состояний расширения.",
    ),
    (
        "Upload an extension .zip file to your environment.",
        "Загрузить .zip-файл расширения в ваше окружение.",
    ),
    (
        "Download an extension .zip file from your environment.",
        "Скачать .zip-файл расширения из вашего окружения.",
    ),
    (
        "Remove an extension .zip file from your environment.",
        "Удалить .zip-файл расширения из вашего окружения.",
    ),
    (
        "Update an existing instance of an extension.",
        "Обновить существующий экземпляр расширения.",
    ),
    ("Delete an instance of an extension.", "Удалить экземпляр расширения."),
    (
        "Get an overview of a OneAgent or JMX extension.",
        "Обзор расширения OneAgent или JMX.",
    ),
    (
        "Update configuration of a OneAgent or JMX extension.",
        "Обновить конфигурацию расширения OneAgent или JMX.",
    ),
    # ---------- (C) PARENT card titles (### ...) — full unique H3 lines.
    # ORDER: "...'s instance" BEFORE bare "### View an extension" (prefix
    # collision: "### View an extension" ⊂ "### View an extension's instance",
    # L4N substring-ordering lesson). ----------
    ("### List extension's instances", "### Список экземпляров расширения"),
    ("### View an extension's instance", "### Просмотр экземпляра расширения"),
    ("### Create an extension's instance", "### Создание экземпляра расширения"),
    ("### Edit an extension's instance", "### Редактирование экземпляра расширения"),
    ("### Delete an extension's instance", "### Удаление экземпляра расширения"),
    ("### List all extensions", "### Список всех расширений"),
    ("### View an extension", "### Просмотр расширения"),
    ("### Check extension's state", "### Проверка состояния расширения"),
    ("### Upload an extension .zip file", "### Загрузка .zip-файла расширения"),
    ("### Download an extension .zip file", "### Скачивание .zip-файла расширения"),
    ("### Delete an extension .zip file", "### Удаление .zip-файла расширения"),
    (
        "### View global configuration of an extension",
        "### Просмотр глобальной конфигурации расширения",
    ),
    (
        "### Update global configuration of an extension",
        "### Обновление глобальной конфигурации расширения",
    ),
    ("### List all ActiveGate modules", "### Список всех модулей ActiveGate"),
    ("### List available hosts", "### Список доступных хостов"),
    # ---------- (D) Related topics bullet (link-text EN, title-attr family canon) ----------
    (
        '* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")',
        '* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")',
    ),
    # ---------- (E) response-code rows (L101: ALL 400 WITHOUT period) ----------
    (
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |",
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |",
    ),
    (
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. Extension has been uploaded. Response contains the ID of the extension. |",
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Расширение загружено. Тело ответа содержит ID расширения. |",
    ),
    (
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The extension configuration has been created. Response contains the ID of the new configuration. |",
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Конфигурация расширения создана. Тело ответа содержит ID новой конфигурации. |",
    ),
    (
        "| **204** | - | Validated. The submitted extension is valid. Response doesn't have a body. |",
        "| **204** | - | Validated. Переданное расширение валидно. Ответ без тела. |",
    ),
    (
        "| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |",
        "| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |",
    ),
    (
        "| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |",
        "| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |",
    ),
    (
        "| **204** | - | Success. Extension configuration has been updated. Response doesn't have a body. |",
        "| **204** | - | Успех. Конфигурация расширения обновлена. Ответ без тела. |",
    ),
    (
        "| **204** | Deleted. Response doesn't have a body. |",
        "| **204** | Удалено. Ответ без тела. |",
    ),
    (
        "| **200** | [StubList](#openapi-definition-StubList) | Success. The response contains IDs of ActiveGate extension modules. Use them to configure ActiveGate extension endpoints. |",
        "| **200** | [StubList](#openapi-definition-StubList) | Успех. Тело ответа содержит ID модулей расширений ActiveGate. Используйте их для настройки эндпоинтов расширений ActiveGate. |",
    ),
    (
        "| **200** | [GlobalExtensionConfiguration](#openapi-definition-GlobalExtensionConfiguration) | Global configuration of given extension. |",
        "| **200** | [GlobalExtensionConfiguration](#openapi-definition-GlobalExtensionConfiguration) | Глобальная конфигурация указанного расширения. |",
    ),
    (" | Success |", " | Успех |"),
    # ---------- (F) table headers ----------
    (
        "| Parameter | Type | Description | In | Required |",
        "| Параметр | Тип | Описание | Где | Обязательный |",
    ),
    (
        "| Element | Type | Description | Required |",
        "| Элемент | Тип | Описание | Обязательный |",
    ),
    ("| Element | Type | Description |", "| Элемент | Тип | Описание |"),
    ("| Code | Type | Description |", "| Код | Тип | Описание |"),
    ("| Code | Description |", "| Код | Описание |"),
    # ---------- (G) standard phrases ----------
    (
        "The request consumes a `multipart/form-data` payload and produces an `application/json` payload.",
        "Запрос принимает payload `multipart/form-data` и возвращает payload `application/json`.",
    ),
    (
        "The request consumes and produces an `application/json` payload.",
        "Запрос принимает и возвращает payload `application/json`.",
    ),
    (
        "The request produces an `application/octet-stream` payload.",
        "Запрос возвращает payload `application/octet-stream`.",
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
        "This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.",
        "Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.",
    ),
    (
        "We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.",
        "Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.",
    ),
    # ---------- (H) headings (newline-anchored; ## Validate payload EN) ----------
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Parameter\n", "\n## Параметр\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n#### Response codes\n", "\n#### Коды ответа\n"),
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n#### Response body objects\n", "\n#### Объекты тела ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n#### Response body JSON models\n", "\n#### JSON-модели тела ответа\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response\n", "\n### Ответ\n"),
    ("\n## Related topics\n", "\n## Связанные темы\n"),
    # ---------- (I) object headings ----------
    (
        "#### The `ExtensionConfigurationList` object",
        "#### Объект `ExtensionConfigurationList`",
    ),
    ("#### The `ExtensionListDto` object", "#### Объект `ExtensionListDto`"),
    ("#### The `ExtensionDto` object", "#### Объект `ExtensionDto`"),
    (
        "#### The `ExtensionConfigurationDto` object",
        "#### Объект `ExtensionConfigurationDto`",
    ),
    ("#### The `ExtensionStateList` object", "#### Объект `ExtensionStateList`"),
    ("#### The `ExtensionState` object", "#### Объект `ExtensionState`"),
    (
        "#### The `GlobalExtensionConfiguration` object",
        "#### Объект `GlobalExtensionConfiguration`",
    ),
    ("#### The `ExtensionProperty` object", "#### Объект `ExtensionProperty`"),
    ("#### The `Extension` object", "#### Объект `Extension`"),
    ("#### The `HostList` object", "#### Объект `HostList`"),
    ("#### The `HostGroup` object", "#### Объект `HostGroup`"),
    ("#### The `Host` object", "#### Объект `Host`"),
    ("#### The `TagInfo` object", "#### Объект `TagInfo`"),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `ConfigurationMetadata` object", "#### Объект `ConfigurationMetadata`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    # ---------- (J) intro / prose (longest first) ----------
    (
        "Every ActiveGate extension runs on a certain ActiveGate instance. The part of the ActiveGate code that runs extensions is called an *ActiveGate extension module*.",
        "Каждое расширение ActiveGate работает на определённом экземпляре ActiveGate. Часть кода ActiveGate, которая запускает расширения, называется *модулем расширения ActiveGate*.",
    ),
    (
        "This request lists all ActiveGate extension modules available in your Dynatrace environment.",
        "Этот запрос выводит список всех модулей расширений ActiveGate, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Deletes the specified instance of the specified extension. The request doesn't delete the binary (.zip) file of the extension.",
        "Удаляет указанный экземпляр указанного расширения. Запрос не удаляет бинарный (.zip) файл расширения.",
    ),
    (
        "Deletes the .zip file of the specified extension from Dynatrace.",
        "Удаляет .zip-файл указанного расширения из Dynatrace.",
    ),
    (
        "Deletion of an extension file uninstalls the extension, making it unavailable for usage.",
        "Удаление файла расширения деинсталлирует расширение, делая его недоступным для использования.",
    ),
    (
        "Downloads the binary (.zip) file of the specified extension.",
        "Скачивает бинарный (.zip) файл указанного расширения.",
    ),
    (
        "A successful request downloads the .zip file of the requested extension.",
        "Успешный запрос скачивает .zip-файл требуемого расширения.",
    ),
    (
        "Lists all instances of the specified extension.",
        "Выводит список всех экземпляров указанного расширения.",
    ),
    (
        "Lists all extensions uploaded to your Dynatrace environment.",
        "Выводит список всех расширений, загруженных в ваше окружение Dynatrace.",
    ),
    (
        "Lists properties of the specified instance of the ActiveGate extension.",
        "Выводит свойства указанного экземпляра расширения ActiveGate.",
    ),
    (
        "Lists the endpoint states of the specified extension.",
        "Выводит состояния эндпоинтов указанного расширения.",
    ),
    (
        "States are stored in server memory and are cleared with restart.",
        "Состояния хранятся в памяти сервера и очищаются при перезапуске.",
    ),
    (
        "Gets the global configuration of the specified OneAgent or JMX extension.",
        "Возвращает глобальную конфигурацию указанного расширения OneAgent или JMX.",
    ),
    (
        "Lists all available hosts that run the specified technology.",
        "Выводит список всех доступных хостов, на которых работает указанная технология.",
    ),
    (
        "Lists the properties of the specified extension.",
        "Выводит свойства указанного расширения.",
    ),
    (
        "Updates properties of the specified instance of the extension.",
        "Обновляет свойства указанного экземпляра расширения.",
    ),
    (
        "Updates the global configuration of the specified OneAgent or JMX extension.",
        "Обновляет глобальную конфигурацию указанного расширения OneAgent или JMX.",
    ),
    (
        "Uploads a .zip extension file to your Dynatrace environment.",
        "Загружает .zip-файл расширения в ваше окружение Dynatrace.",
    ),
    (
        "Creates a new instance for the specified extension.",
        "Создаёт новый экземпляр для указанного расширения.",
    ),
    # ---------- (K) object descriptions ----------
    ("A list of configurations.", "Список конфигураций."),
    ("List of configurations.", "Список конфигураций."),
    ("A list of extensions.", "Список расширений."),
    (
        "Global Configuration of OneAgent and JMX extension",
        "Глобальная конфигурация расширения OneAgent и JMX",
    ),
    ("A list of extension states.", "Список состояний расширения."),
    ("General configuration of an extension.", "Общая конфигурация расширения."),
    ("A property of an extension.", "Свойство расширения."),
    (
        "Host details. Contains ID, name, host group, and tags.",
        "Детали хоста. Содержит ID, имя, host group и теги.",
    ),
    (
        "The list of hosts supported by extension.",
        "Список хостов, поддерживаемых расширением.",
    ),
    ("Host group to which the host belongs.", "Host group, которому принадлежит хост."),
    ("Tag of a Dynatrace entity.", "Тег сущности Dynatrace."),
    # ---------- (L) element / cell descriptions (longest/specific first) ----------
    (
        "The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result.",
        "Курсор для следующей страницы результатов. На последней странице имеет значение `null`.  Используйте его в query-параметре **nextPageKey** для получения последующих страниц результата.",
    ),
    (
        "The cursor for the next page of results.",
        "Курсор для следующей страницы результатов.",
    ),
    (
        "The number of results per result page. Must be between 1 and 500",
        "Количество результатов на страницу. Должно быть от 1 до 500",
    ),
    (
        "The total number of entries in the result.",
        "Общее количество записей в результате.",
    ),
    (
        "The type of the extension. It indicates the runtime environment of the extension (for example, ACTIVEGATE).",
        "Тип расширения. Указывает среду выполнения расширения (например, ACTIVEGATE).",
    ),
    (
        "The extension is enabled (`true`) or disabled (`false`).",
        "Расширение включено (`true`) или отключено (`false`).",
    ),
    (
        "The ID of the endpoint where the state is detected - Active Gate only.",
        "ID эндпоинта, где обнаружено состояние - только Active Gate.",
    ),
    (
        "The name of the endpoint, displayed in Dynatrace.",
        "Имя эндпоинта, отображаемое в Dynatrace.",
    ),
    ("The ID of the endpoint.", "ID эндпоинта."),
    (
        "The ID of the host on which the extension runs.",
        "ID хоста, на котором работает расширение.",
    ),
    (
        "The ID of the entity on which the extension is active.",
        "ID сущности, на которой активно расширение.",
    ),
    (
        "The list of extension parameters.  Each parameter is a key-value pair.",
        "Список параметров расширения.  Каждый параметр представляет собой пару «ключ-значение».",
    ),
    (
        "The list of configuration parameters.  Each parameter is a key-value pair.",
        "Список параметров конфигурации.  Каждый параметр представляет собой пару «ключ-значение».",
    ),
    (
        "Allows to skip current configuration and use global one.",
        "Позволяет пропустить текущую конфигурацию и использовать глобальную.",
    ),
    ("A list of extension states.", "Список состояний расширения."),
    ("The state of the extension.", "Состояние расширения."),
    ("A short description of the state.", "Краткое описание состояния."),
    (
        "The timestamp when the state was detected, in UTC milliseconds.",
        "Временная метка обнаружения состояния, в миллисекундах UTC.",
    ),
    (
        "The version of the extension (for example `1.0.0`).",
        "Версия расширения (например `1.0.0`).",
    ),
    (
        "The ID of the extension, for example `custom.remote.python.demo`.",
        "ID расширения, например `custom.remote.python.demo`.",
    ),
    (
        "The metricGroup of the extension used for grouping custom metrics into a hierarchical namespace.",
        "metricGroup расширения, используемый для группировки кастомных метрик в иерархическое пространство имён.",
    ),
    (
        "The name of the extension, displayed in Dynatrace.",
        "Имя расширения, отображаемое в Dynatrace.",
    ),
    ("A list of extension properties.", "Список свойств расширения."),
    (
        "The version of the extension, displayed in Dynatrace.",
        "Версия расширения, отображаемая в Dynatrace.",
    ),
    (
        "The plugin is enabled (`true`) or disabled (`false`) globally for hosts in infrastructure-only monitoring mode",
        "Плагин включён (`true`) или отключён (`false`) глобально для хостов в режиме мониторинга только инфраструктуры",
    ),
    (
        "The list of possible values of the property.  If such a list is defined, only values from this list can be assigned to the property.",
        "Список возможных значений свойства.  Если такой список задан, свойству можно присвоить только значения из этого списка.",
    ),
    ("The default value of the property.", "Значение свойства по умолчанию."),
    ("The key of the property.", "Ключ свойства."),
    ("The type of the property.", "Тип свойства."),
    # ---------- (M) parameter cell descriptions ----------
    (
        "The ID of the extension where you want to update the configuration.  If you set the extension ID in the body as well, it must match this ID.",
        "ID расширения, в котором вы хотите обновить конфигурацию.  Если вы также задаёте ID расширения в теле, он должен совпадать с этим ID.",
    ),
    (
        "The ID of the extension where you want to delete the configuration.",
        "ID расширения, в котором вы хотите удалить конфигурацию.",
    ),
    (
        "The ID of the extension to be deleted.",
        "ID расширения, которое нужно удалить.",
    ),
    (
        "The ID of the extension to be updated.",
        "ID расширения, которое нужно обновить.",
    ),
    ("The ID of the required extension.", "ID требуемого расширения."),
    ("The ID of the extension.", "ID расширения."),
    (
        "| id | string | The ID of the extension | path | Required |",
        "| id | string | ID расширения | path | Required |",
    ),
    (
        "The ID of the extension you want to download.",
        "ID расширения, которое вы хотите скачать.",
    ),
    (
        "The ID of the configuration to be deleted.",
        "ID конфигурации, которую нужно удалить.",
    ),
    (
        "The ID of the configuration to be updated.",
        "ID конфигурации, которую нужно обновить.",
    ),
    ("The ID of the configuration.", "ID конфигурации."),
    (
        "The JSON body of the request. Contains updated parameters of the extension configuration.",
        "JSON-тело запроса. Содержит обновлённые параметры конфигурации расширения.",
    ),
    (
        "The JSON body of the request. Contains updated configuration of the extension.",
        "JSON-тело запроса. Содержит обновлённую конфигурацию расширения.",
    ),
    (
        "The JSON body of the request. Contains new configuration of the extension.",
        "JSON-тело запроса. Содержит новую конфигурацию расширения.",
    ),
    (
        "Extension .zip file to be uploaded.  The file name must match the **name** field in the `plugin.json` file.  For example, for the extension whose **name** is `custom.remote.python.demo`, the name of the extension file must be `custom.remote.python.demo.zip`.",
        "Загружаемый .zip-файл расширения.  Имя файла должно совпадать с полем **name** в файле `plugin.json`.  Например, для расширения, у которого **name** равно `custom.remote.python.demo`, имя файла расширения должно быть `custom.remote.python.demo.zip`.",
    ),
    (
        "Use extension-defined thresholds for alerts (`true`) or user-defined thresholds (`false`).  Extension-defined thresholds are stored in the `plugin.json` file.  If not set, user-defined thresholds are used.",
        "Использовать пороги, заданные расширением, для оповещений (`true`) или пороги, заданные пользователем (`false`).  Пороги, заданные расширением, хранятся в файле `plugin.json`.  Если не задано, используются пороги, заданные пользователем.",
    ),
    ("Name of requested technology", "Имя требуемой технологии"),
    (
        "Filters the resulting set of hosts by the specified tag.  You can specify several tags in the following format: `tag=tag1&tag=tag2`. The host has to match **all** the specified tags.",
        "Фильтрует результирующий набор хостов по указанному тегу.  Вы можете указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Хост должен соответствовать **всем** указанным тегам.",
    ),
    (
        "Only return hosts that are part of the specified management zone.",
        "Возвращать только хосты, входящие в указанную management zone.",
    ),
    (
        "Filters the resulting set of hosts by the specified host group.  Specify the Dynatrace IDs of the host group you're interested in.",
        "Фильтрует результирующий набор хостов по указанной host group.  Укажите Dynatrace ID интересующей вас host group.",
    ),
    (
        "Filters the resulting set of hosts by the specified host group.  Specify the name of the host group you're interested in.",
        "Фильтрует результирующий набор хостов по указанной host group.  Укажите имя интересующей вас host group.",
    ),
    ("Extension state to filter.", "Состояние расширения для фильтрации."),
    # ---------- (N) get-available-hosts Host/HostGroup/TagInfo cells ----------
    (
        "A list of management zones to which the host belongs.",
        "Список management zone, которым принадлежит хост.",
    ),
    ("A list of tags of the host.", "Список тегов хоста."),
    ("The list of hosts", "Список хостов"),
    (
        "Next page key used for paging",
        "Ключ следующей страницы, используемый для постраничного вывода",
    ),
    ("Total number of results", "Общее количество результатов"),
    ("The ID of the host", "ID хоста"),
    ("The name of the host", "Имя хоста"),
    (
        "The Dynatrace entity ID of the host group.",
        "ID сущности Dynatrace для host group.",
    ),
    (
        "The name of the Dynatrace entity, displayed in the UI.",
        "Имя сущности Dynatrace, отображаемое в UI.",
    ),
    (
        "The origin of the tag, such as AWS or Cloud Foundry.  Custom tags use the `CONTEXTLESS` value.",
        "Источник тега, например AWS или Cloud Foundry.  Кастомные теги используют значение `CONTEXTLESS`.",
    ),
    (
        "The key of the tag.  Custom tags have the tag value here.",
        "Ключ тега.  Кастомные теги содержат здесь значение тега.",
    ),
    (
        "The value of the tag.  Not applicable to custom tags.",
        "Значение тега.  Не применимо к кастомным тегам.",
    ),
    # ---------- (O) shared k8s/config canon (EntityShortRep / Error / metadata) ----------
    (
        "An ordered list of short representations of Dynatrace entities.",
        "Упорядоченный список кратких представлений сущностей Dynatrace.",
    ),
    (
        "The short representation of a Dynatrace entity.",
        "Краткое представление сущности Dynatrace.",
    ),
    (
        "A short description of the Dynatrace entity.",
        "Краткое описание сущности Dynatrace.",
    ),
    ("The ID of the Dynatrace entity.", "ID сущности Dynatrace."),
    ("The name of the Dynatrace entity.", "Имя сущности Dynatrace."),
    ("The HTTP status code", "HTTP-код статуса"),
    ("A list of constraint violations", "Список нарушений ограничений"),
    ("The error message", "Сообщение об ошибке"),
    ("Metadata useful for debugging", "Метаданные для отладки"),
    ("Dynatrace version.", "Версия Dynatrace."),
    (
        "A sorted list of the version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    (
        "A sorted list of version numbers of the configuration.",
        "Отсортированный список номеров версий конфигурации.",
    ),
    # ---------- (P) global LAST: element-can-hold -> Возможные значения: (L99) ----------
    ("The element can hold these values", "Возможные значения:"),
]


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    with io.open(src, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    t = t.replace("\r\n", "\n")  # EN is CRLF; RU corpus convention is LF
    t = t.replace("﻿", "").replace("ï»¿", "")  # BOM-mojibake guard (L4M)
    for en, ru in R:
        t = t.replace(en, ru)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return dst


if __name__ == "__main__":
    for rel in FILES:
        print("wrote", build(rel))
