# -*- coding: utf-8 -*-
"""L4N builder: configuration-api/plugins-api/ parent + 12 endpoints.
Splice method (L98/L100): start from EN, CRLF->LF, apply ordered
exact-string canon replacements -> byte-identical JSON + line parity.
ACTIVE API (no deprecated banner, L89/L90). No env-api twin ->
L103 case (b): anchor = config-api L99 + k8s-credentials RU shared
objects (StubList/EntityShortRepresentation/Error/ConstraintViolation/
ConfigurationMetadata). Domain corpus-dominant: "plugin"->"плагин",
"endpoint"->"эндпоинт"; object-names/enum/ActiveGate/OneAgent EN-lock."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api"
RU = "docs/managed-ru/dynatrace-api/configuration-api"
PA = "plugins-api"

FILES = [
    f"{PA}.md",
    f"{PA}/get-all-plugins.md",
    f"{PA}/get-a-plugin.md",
    f"{PA}/post-a-plugin.md",
    f"{PA}/get-plugin-binary.md",
    f"{PA}/delete-plugin-binary.md",
    f"{PA}/get-all-endpoints.md",
    f"{PA}/get-an-endpoint.md",
    f"{PA}/post-an-endpoint.md",
    f"{PA}/put-an-endpoint.md",
    f"{PA}/delete-an-endpoint.md",
    f"{PA}/get-all-ag-modules.md",
    f"{PA}/get-a-plugin-state.md",
]

# Ordered (EN, RU): specific/longer before any that could be substrings.
R = [
    # ---------- (A) PARENT card-link titles / descriptions / title-attrs ----------
    # title-attrs (inside ]( "...") ) — longest unique strings first
    (
        "View all plugin uploaded to your environment via the Dynatrace API.",
        "Просмотр всех плагинов, загруженных в ваше окружение мониторинга, через Dynatrace API.",
    ),
    (
        "View a plugin uploaded to your environment via the Dynatrace API.",
        "Просмотр плагина, загруженного в ваше окружение мониторинга, через Dynatrace API.",
    ),
    (
        "Upload a plugin file to your environment via the Dynatrace API.",
        "Загрузка файла плагина в ваше окружение мониторинга через Dynatrace API.",
    ),
    (
        "Download a plugin file from your environment via the Dynatrace API.",
        "Скачивание файла плагина из вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "Delete a binary file of a plugin from your environment via the Dynatrace API.",
        "Удаление бинарного файла плагина из вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View all endpoint of a plugin uploaded to your environment via the Dynatrace API.",
        "Просмотр всех эндпоинтов плагина, загруженного в ваше окружение мониторинга, через Dynatrace API.",
    ),
    (
        "View an endpoint of a plugin via the Dynatrace API.",
        "Просмотр эндпоинта плагина через Dynatrace API.",
    ),
    (
        "Create an endpoint in a plugin via the Dynatrace API.",
        "Создание эндпоинта в плагине через Dynatrace API.",
    ),
    (
        "Edit an endpoint in a plugin via the Dynatrace API.",
        "Редактирование эндпоинта в плагине через Dynatrace API.",
    ),
    (
        "Delete an endpoint of a plugin uploaded to your environment via the Dynatrace API.",
        "Удаление эндпоинта плагина, загруженного в ваше окружение мониторинга, через Dynatrace API.",
    ),
    (
        "View all ActiveGate plugin modules of your environment via the Dynatrace API.",
        "Просмотр всех модулей плагинов ActiveGate вашего окружения мониторинга через Dynatrace API.",
    ),
    (
        "View status an endpoint of a plugin via the Dynatrace API.",
        "Просмотр статуса эндпоинта плагина через Dynatrace API.",
    ),
    # card descriptions
    (
        "Get an overview of all plugins available in your Dynatrace environment.",
        "Обзор всех плагинов, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Get plugin parameters by plugin ID.",
        "Получить параметры плагина по ID плагина.",
    ),
    (
        "Upload a plugin ZIP file to your environment.",
        "Загрузить ZIP-файл плагина в ваше окружение.",
    ),
    (
        "Download a plugin ZIP file from your environment.",
        "Скачать ZIP-файл плагина из вашего окружения.",
    ),
    (
        "Remove a plugin ZIP file from your environment.",
        "Удалить ZIP-файл плагина из вашего окружения.",
    ),
    (
        "Get a list of available endpoints of an ActiveGate plugin.",
        "Получить список доступных эндпоинтов плагина ActiveGate.",
    ),
    (
        "Get parameters of an ActiveGate plugin by its ID.",
        "Получить параметры плагина ActiveGate по его ID.",
    ),
    (
        "Create a new endpoint for an ActiveGate plugin with the exact parameters you need.",
        "Создать новый эндпоинт для плагина ActiveGate с нужными вам параметрами.",
    ),
    (
        "Update an existing endpoint of an ActiveGate plugin.",
        "Обновить существующий эндпоинт плагина ActiveGate.",
    ),
    # delete card: EN reuses near-title wording for the description (period
    # variant) -> distinct from the "### ..." title rule, needs its own pair
    (
        "Delete an endpoint of an ActiveGate plugin.",
        "Удалить эндпоинт плагина ActiveGate.",
    ),
    (
        "Get an overview of all ActiveGate modules available in your Dynatrace environment.",
        "Обзор всех модулей ActiveGate, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Get a list of possible states of an ActiveGate plugin.",
        "Получить список возможных состояний плагина ActiveGate.",
    ),
    # card titles (### ...) — full unique H3 lines
    ("### List all plugins", "### Список всех плагинов"),
    ("### View a plugin", "### Просмотр плагина"),
    ("### Upload a plugin ZIP", "### Загрузка ZIP-файла плагина"),
    ("### Download a plugin ZIP", "### Скачивание ZIP-файла плагина"),
    ("### Delete a plugin ZIP", "### Удаление ZIP-файла плагина"),
    (
        "### List endpoints of an ActiveGate plugin",
        "### Список эндпоинтов плагина ActiveGate",
    ),
    (
        "### View an endpoint of an ActiveGate plugin",
        "### Просмотр эндпоинта плагина ActiveGate",
    ),
    (
        "### Create an endpoint of an ActiveGate plugin",
        "### Создание эндпоинта плагина ActiveGate",
    ),
    (
        "### Edit an endpoint of an ActiveGate plugin",
        "### Редактирование эндпоинта плагина ActiveGate",
    ),
    (
        "### Delete an endpoint of an ActiveGate plugin",
        "### Удаление эндпоинта плагина ActiveGate",
    ),
    ("### List all ActiveGate modules", "### Список всех модулей ActiveGate"),
    (
        "### List states of an ActiveGate plugin",
        "### Список состояний плагина ActiveGate",
    ),
    # ---------- (B) response-code rows (L101: all plugins 400 = WITH period) ----------
    (
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |",
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |",
    ),
    (
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. Plugin has been uploaded. Response contains the ID of the plugin. |",
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Плагин загружен. Тело ответа содержит ID плагина. |",
    ),
    (
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The plugin endpoint has been created. Response contains the ID of the new endpoint. |",
        "| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Успех. Эндпоинт плагина создан. Тело ответа содержит ID нового эндпоинта. |",
    ),
    (
        "| **204** | - | Validated. The submitted plugin is valid. Response doesn't have a body. |",
        "| **204** | - | Validated. Переданный плагин валиден. Ответ без тела. |",
    ),
    (
        "| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |",
        "| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |",
    ),
    (
        "| **204** | - | Success. The endpoint has been updated. Response doesn't have a body. |",
        "| **204** | - | Успех. Эндпоинт обновлён. Ответ без тела. |",
    ),
    (
        "| **204** | Deleted. Response doesn't have a body. |",
        "| **204** | Удалено. Ответ без тела. |",
    ),
    (
        "| **200** | [StubList](#openapi-definition-StubList) | Success. The response contains IDs of ActiveGate plugin modules. Use them to configure plugin endpoints. |",
        "| **200** | [StubList](#openapi-definition-StubList) | Успех. Тело ответа содержит ID модулей плагинов ActiveGate. Используйте их для настройки эндпоинтов плагинов. |",
    ),
    (" | Success |", " | Успех |"),
    # ---------- (C) table headers ----------
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
    # ---------- (D) standard phrases ----------
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
    # ---------- (E) headings (newline-anchored; ## Validate payload / #### Curl EN) ----------
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
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
    ("\n## Example\n", "\n## Пример\n"),
    ("\n#### Request URL\n", "\n#### URL запроса\n"),
    ("\n#### Request body\n", "\n#### Тело запроса\n"),
    ("\n#### Response body\n", "\n#### Тело ответа\n"),
    ("\n#### Response code\n", "\n#### Код ответа\n"),
    ("\n#### Result\n", "\n#### Результат\n"),
    # ---------- (F) object headings ----------
    ("#### The `PluginStateList` object", "#### Объект `PluginStateList`"),
    ("#### The `PluginState` object", "#### Объект `PluginState`"),
    ("#### The `StubList` object", "#### Объект `StubList`"),
    (
        "#### The `EntityShortRepresentation` object",
        "#### Объект `EntityShortRepresentation`",
    ),
    ("#### The `RemotePluginEndpoint` object", "#### Объект `RemotePluginEndpoint`"),
    ("#### The `PluginProperty` object", "#### Объект `PluginProperty`"),
    ("#### The `ConfigurationMetadata` object", "#### Объект `ConfigurationMetadata`"),
    ("#### The `Plugin` object", "#### Объект `Plugin`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    # ---------- (G) intro / multi-sentence prose (longest first) ----------
    (
        "Every ActiveGate plugin runs on a certain ActiveGate instance. The part of the ActiveGate code that runs plugins is called an *ActiveGate plugin module*.",
        "Каждый плагин ActiveGate работает на определённом инстансе ActiveGate. Часть кода ActiveGate, которая запускает плагины, называется *модулем плагина ActiveGate*.",
    ),
    (
        "This request lists all ActiveGate plugin modules available in your Dynatrace environment.",
        "Этот запрос выводит список всех модулей плагинов ActiveGate, доступных в вашем окружении Dynatrace.",
    ),
    (
        "Lists all plugins uploaded to your Dynatrace environment.",
        "Выводит список всех плагинов, загруженных в ваше окружение Dynatrace.",
    ),
    (
        "Lists the properties of the specified plugin.",
        "Выводит свойства указанного плагина.",
    ),
    (
        "Uploads a ZIP plugin file to your Dynatrace environment.",
        "Загружает ZIP-файл плагина в ваше окружение Dynatrace.",
    ),
    (
        "Downloads the ZIP file of the specified plugin.",
        "Скачивает ZIP-файл указанного плагина.",
    ),
    (
        "Deletes the ZIP file of the specified plugin from Dynatrace.",
        "Удаляет ZIP-файл указанного плагина из Dynatrace.",
    ),
    (
        "Deletion of a plugin file uninstalls the plugin, making it unavailable for use.",
        "Удаление файла плагина деинсталлирует плагин, делая его недоступным для использования.",
    ),
    (
        "Lists all endpoints of the specified plugin.",
        "Выводит список всех эндпоинтов указанного плагина.",
    ),
    (
        "Lists properties of the specified endpoint of the ActiveGate plugin.",
        "Выводит свойства указанного эндпоинта плагина ActiveGate.",
    ),
    (
        "Creates a new endpoint for the specified ActiveGate plugin.",
        "Создаёт новый эндпоинт для указанного плагина ActiveGate.",
    ),
    (
        "Updates properties of the specified endpoint of the ActiveGate plugin.",
        "Обновляет свойства указанного эндпоинта плагина ActiveGate.",
    ),
    (
        "Deletes the specified endpoint of the ActiveGate plugin.",
        "Удаляет указанный эндпоинт плагина ActiveGate.",
    ),
    (
        "Lists the endpoint states of the specified plugin.",
        "Выводит состояния эндпоинтов указанного плагина.",
    ),
    (
        "States are stored in server memory and are cleared with restart.",
        "Состояния хранятся в памяти сервера и очищаются при перезапуске.",
    ),
    (
        "A successful request downloads the ZIP file of the requested plugin.",
        "Успешный запрос скачивает ZIP-файл требуемого плагина.",
    ),
    # ---------- (H) Example prose ----------
    (
        "In this example, the request lists all the plugins uploaded to the **mySampleEnv** environment.",
        "В этом примере запрос выводит список всех плагинов, загруженных в окружение **mySampleEnv**.",
    ),
    (
        "The result is truncated to four entries. The request lists these plugins:",
        "Результат усечён до четырёх записей. Запрос выводит список этих плагинов:",
    ),
    (
        "In this example, the request inquires for parameters of the **SAP plugin**, which has the ID of **custom.remote.python.sap**.",
        "В этом примере запрос запрашивает параметры **SAP plugin** с ID **custom.remote.python.sap**.",
    ),
    (
        "In this example the request uploads the `custom.remote.python.simple_math.zip` file, which is stored in the `C:\\temp\\` directory, to the **mySampleEnv** environment.",
        "В этом примере запрос загружает файл `custom.remote.python.simple_math.zip`, хранящийся в каталоге `C:\\temp\\`, в окружение **mySampleEnv**.",
    ),
    (
        "The response code of **201** confirms a successful upload. The ID of the plugin is returned.",
        "Код ответа **201** подтверждает успешную загрузку. Возвращается ID плагина.",
    ),
    (
        "In this example, the request inquires for endpoints of the **SAP plugin**, which has the ID of **custom.remote.python.sap**.",
        "В этом примере запрос запрашивает эндпоинты **SAP plugin** с ID **custom.remote.python.sap**.",
    ),
    ("The request lists these endpoints:", "Запрос выводит список этих эндпоинтов:"),
    (
        "In this example, the request inquires for the parameter of the **SAPacceptance** endpoint, which has the ID of **5677163660730843402**. The endpoint belongs to the SAP plugin that has the ID of **custom.remote.python.sap**.",
        "В этом примере запрос запрашивает параметр эндпоинта **SAPacceptance** с ID **5677163660730843402**. Эндпоинт принадлежит SAP plugin с ID **custom.remote.python.sap**.",
    ),
    (
        "The endpoint has the following parameters:",
        "Эндпоинт имеет следующие параметры:",
    ),
    (
        "In this example, the request lists all the ActiveGate plugin modules available in the **mySampleEnv** environment.",
        "В этом примере запрос выводит список всех модулей плагинов ActiveGate, доступных в окружении **mySampleEnv**.",
    ),
    ("The result is truncated to three entries.", "Результат усечён до трёх записей."),
    (
        "In this example, the request lists the states of the **MathPlugin**, which has the ID of **custom.remote.python.simple\\_math**.",
        "В этом примере запрос выводит состояния **MathPlugin** с ID **custom.remote.python.simple\\_math**.",
    ),
    (
        "In this example, the request creates a new endpoint for the SAP plugin which has the ID of **custom.remote.python.sap**.",
        "В этом примере запрос создаёт новый эндпоинт для SAP plugin с ID **custom.remote.python.sap**.",
    ),
    (
        "The new endpoint looks like this in the UI:",
        "В UI новый эндпоинт выглядит так:",
    ),
    (
        "In this example, the request updates the **RESTtest** endpoint of the SAP plugin which has the ID of **custom.remote.python.sap**. It makes the following changes to the endpoint:",
        "В этом примере запрос обновляет эндпоинт **RESTtest** SAP plugin с ID **custom.remote.python.sap**. Он вносит следующие изменения в эндпоинт:",
    ),
    ("* **name** to `RESTtest - updated`", "* **name** на `RESTtest - updated`"),
    ("* **serverIp** to `192.168.1.1`", "* **serverIp** на `192.168.1.1`"),
    (
        "* **activeGatePluginModule** to l-009 which has the ID of `6121289130553435111`",
        "* **activeGatePluginModule** на l-009 с ID `6121289130553435111`",
    ),
    (
        "You can download or copy the example request body to try it out on your own.",
        "Вы можете скачать или скопировать пример тела запроса, чтобы попробовать самостоятельно.",
    ),
    (
        "The original endpoint has the following parameters:",
        "Исходный эндпоинт имеет следующие параметры:",
    ),
    (
        "The updated endpoint looks like this in the UI:",
        "В UI обновлённый эндпоинт выглядит так:",
    ),
    (
        "In this example, the request deletes the endpoint with the ID of **8757307336635955682** from the SAP plugin, which has the ID of **custom.remote.python.sap**. The response code of 204 indicates that the deletion was successful.",
        "В этом примере запрос удаляет эндпоинт с ID **8757307336635955682** из SAP plugin с ID **custom.remote.python.sap**. Код ответа 204 указывает, что удаление прошло успешно.",
    ),
    (
        "In this example, the request deletes the **MathPlugin** with the ID of **custom.remote.python.simple\\_math** from the **mySampleEnv** environment. The response code of **204** indicates that the deletion was successful.",
        "В этом примере запрос удаляет **MathPlugin** с ID **custom.remote.python.simple\\_math** из окружения **mySampleEnv**. Код ответа **204** указывает, что удаление прошло успешно.",
    ),
    (
        "The API token is passed in the **Authorization** header.",
        "API-токен передаётся в заголовке **Authorization**.",
    ),
    # ---------- (I) object descriptions ----------
    (
        "An ordered list of short representations of Dynatrace entities.",
        "Упорядоченный список кратких представлений сущностей Dynatrace.",
    ),
    (
        "The short representation of a Dynatrace entity.",
        "Краткое представление сущности Dynatrace.",
    ),
    ("General configuration of a plugin.", "Общая конфигурация плагина."),
    ("Configuration of a plugin endpoint.", "Конфигурация эндпоинта плагина."),
    ("A list of plugin states.", "Список состояний плагина."),
    ("A property of a plugin.", "Свойство плагина."),
    # ---------- (J) parameter cell descriptions ----------
    (
        "Plugin ZIP file to be uploaded.  The file name must match the **name** field in the `plugin.json` file.  For example, for the plugin whose **name** is `custom.remote.python.demo`, the name of the plugin file must be `custom.remote.python.demo.zip`.",
        "ZIP-файл плагина для загрузки.  Имя файла должно совпадать с полем **name** в файле `plugin.json`.  Например, для плагина, у которого **name** равно `custom.remote.python.demo`, имя файла плагина должно быть `custom.remote.python.demo.zip`.",
    ),
    (
        "Use plugin-defined thresholds for alerts (`true`) or user-defined thresholds (`false`).  Plugin-defined thresholds are stored in the `plugin.json` file.  If not set, user-defined thresholds are used.",
        "Использовать пороги, заданные плагином, для оповещений (`true`) или пороги, заданные пользователем (`false`).  Пороги, заданные плагином, хранятся в файле `plugin.json`.  Если не задано, используются пороги, заданные пользователем.",
    ),
    (
        "The ID of the plugin where you want to update an endpoint.  If you set the plugin ID in the body as well, it must match this ID.",
        "ID плагина, в котором вы хотите обновить эндпоинт.  Если вы также задаёте ID плагина в теле, он должен совпадать с этим ID.",
    ),
    (
        "The ID of the endpoint to be updated.  If you set the endpoint ID in the body as well, it must match this ID.",
        "ID эндпоинта, который нужно обновить.  Если вы также задаёте ID эндпоинта в теле, он должен совпадать с этим ID.",
    ),
    (
        "The JSON body of the request. Contains parameters of the new plugin endpoint.",
        "JSON-тело запроса. Содержит параметры нового эндпоинта плагина.",
    ),
    (
        "The JSON body of the request. Contains updated parameters of the plugin endpoint.",
        "JSON-тело запроса. Содержит обновлённые параметры эндпоинта плагина.",
    ),
    (
        "The ID of the plugin where you want to create an endpoint.",
        "ID плагина, в котором вы хотите создать эндпоинт.",
    ),
    (
        "The ID of the plugin where you want to delete an endpoint.",
        "ID плагина, в котором вы хотите удалить эндпоинт.",
    ),
    (
        "The ID of the plugin you want to download.",
        "ID плагина, который вы хотите скачать.",
    ),
    ("The ID of the plugin to be deleted.", "ID плагина, который нужно удалить."),
    ("The ID of the required plugin.", "ID требуемого плагина."),
    ("The ID of the required endpoint.", "ID требуемого эндпоинта."),
    ("The ID of the endpoint to be deleted.", "ID эндпоинта, который нужно удалить."),
    # ---------- (K) element cell descriptions ----------
    (
        "The endpoint is enabled (`true`) or disabled (`false`).",
        "Эндпоинт включён (`true`) или отключён (`false`).",
    ),
    (
        "The name of the endpoint, displayed in Dynatrace.",
        "Имя эндпоинта, отображаемое в Dynatrace.",
    ),
    (
        "The ID of the plugin to which the endpoint belongs.",
        "ID плагина, которому принадлежит эндпоинт.",
    ),
    (
        "The list of endpoint parameters.  Each parameter is a property-value pair.",
        "Список параметров эндпоинта.  Каждый параметр представляет собой пару «свойство-значение».",
    ),
    ("The ID of the endpoint.", "ID эндпоинта."),
    (
        "The ID of the plugin, for example `custom.remote.python.demo`.",
        "ID плагина, например `custom.remote.python.demo`.",
    ),
    (
        "The metric group of the plugin. All the metrics, captured by the plugin are children of this group.",
        "Группа метрик плагина. Все метрики, собираемые плагином, являются потомками этой группы.",
    ),
    (
        "The name of the plugin, displayed in Dynatrace.",
        "Имя плагина, отображаемое в Dynatrace.",
    ),
    ("A list of plugin properties.", "Список свойств плагина."),
    (
        "The type of the plugin. It indicates the runtime environment of the plugin (for example, ActiveGate).",
        "Тип плагина. Указывает среду выполнения плагина (например, ActiveGate).",
    ),
    (
        "The version of the plugin, displayed in Dynatrace.",
        "Версия плагина, отображаемая в Dynatrace.",
    ),
    ("The default value of the property.", "Значение свойства по умолчанию."),
    (
        "The list of possible values of the property.  If such a list is defined, only values from this list can be assigned to the property.",
        "Список возможных значений свойства.  Если такой список задан, свойству можно присвоить только значения из этого списка.",
    ),
    ("The key of the property.", "Ключ свойства."),
    ("The type of the property.", "Тип свойства."),
    (
        "The ID of the endpoint where the state is detected - Active Gate only.",
        "ID эндпоинта, где обнаружено состояние - только Active Gate.",
    ),
    (
        "The ID of the host on which the plugin runs.",
        "ID хоста, на котором работает плагин.",
    ),
    (
        "The ID of the entity on which the plugin is active.",
        "ID сущности, на которой активен плагин.",
    ),
    ("The state of the plugin.", "Состояние плагина."),
    ("A short description of the state.", "Краткое описание состояния."),
    (
        "The timestamp when the state was detected, in UTC milliseconds.",
        "Временная метка обнаружения состояния, в миллисекундах UTC.",
    ),
    (
        "The version of the plugin (for example `1.0.0`).",
        "Версия плагина (например `1.0.0`).",
    ),
    ("The ID of the plugin.", "ID плагина."),
    # ---------- (L) shared k8s/config canon (EntityShortRep / Error / metadata) ----------
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
    # ---------- (M) global LAST: element-can-hold -> Возможные значения: (L99) ----------
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
