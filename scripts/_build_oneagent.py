# -*- coding: utf-8 -*-
"""L4M builder: oneagent-configuration/ 10 endpoint files.
Splice method (L98/L100): start from EN, apply exact-string canon
replacements -> guarantees byte-identical JSON + line parity.
Parents (4) are hand-written separately."""

import os, io

EN = "docs/managed/dynatrace-api/configuration-api/oneagent-configuration"
RU = "docs/managed-ru/dynatrace-api/configuration-api/oneagent-configuration"

FILES = [
    "oneagent-environment-wide/get-auto-update-configuration.md",
    "oneagent-environment-wide/put-auto-update-configuration.md",
    "oneagent-environment-wide/get-technology-monitoring.md",
    "oneagent-in-host-group/get-auto-update-configuration.md",
    "oneagent-in-host-group/put-auto-update-configuration.md",
    "oneagent-on-host/oneagent-auto-update/get-auto-update-configuration.md",
    "oneagent-on-host/oneagent-auto-update/put-auto-update-configuration.md",
    "oneagent-on-host/oneagent-config.md",
    "oneagent-on-host/oneagent-monitoring/put-monitoring-configuration.md",
    "oneagent-on-host/oneagent-technology-monitoring.md",
]

# Ordered list of exact (EN, RU) replacements. Order matters:
# specific/longer strings before any that could be their substrings.
R = [
    # --- (1) put-monitoring: deprecated bullet drop + bold-schema banner (maintenance-windows canon) ---
    (
        '* Updated on Jun 23, 2022\n* Deprecated\n\nThis API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Monitoring** (`builtin:host.monitoring`) schema instead.',
        '* Updated on Jun 23, 2022\n\nЭтот API устарел. Используйте [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.") со schema **Monitoring** (`builtin:host.monitoring`).',
    ),
    # --- (2) table headers (4-col -> 3-col -> code) ---
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
    # --- (3) response-code rows (period BY SOURCE, L101) ---
    (
        "| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |",
        "| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |",
    ),
    (
        "| **204** | - | Success. The submitted configuration is valid. Response doesn't have a body. |",
        "| **204** | - | Успех. Переданная конфигурация валидна. Ответ без тела. |",
    ),
    (
        "| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body. |",
        "| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |",
    ),
    (
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |",
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод. |",
    ),
    (
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |",
        "| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |",
    ),
    (" | Success |", " | Успех |"),
    # --- (4) standard phrases ---
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
    # --- (5) headings (newline-anchored; "## Validate payload" stays EN per L99) ---
    ("\n## Authentication\n", "\n## Аутентификация\n"),
    ("\n### Authentication\n", "\n### Аутентификация\n"),
    ("\n## Parameters\n", "\n## Параметры\n"),
    ("\n## Response\n", "\n## Ответ\n"),
    ("\n### Response\n", "\n### Ответ\n"),
    ("\n### Response codes\n", "\n### Коды ответа\n"),
    ("\n#### Response codes\n", "\n#### Коды ответа\n"),
    ("\n### Response body objects\n", "\n### Объекты тела ответа\n"),
    ("\n#### Response body objects\n", "\n#### Объекты тела ответа\n"),
    ("\n### Request body objects\n", "\n### Объекты тела запроса\n"),
    ("\n### Response body JSON models\n", "\n### JSON-модели тела ответа\n"),
    ("\n#### Response body JSON models\n", "\n#### JSON-модели тела ответа\n"),
    ("\n### Request body JSON model\n", "\n### JSON-модель тела запроса\n"),
    # --- (6) object headings ---
    (
        "#### The `EnvironmentAutoUpdateConfig` object",
        "#### Объект `EnvironmentAutoUpdateConfig`",
    ),
    (
        "#### The `HostGroupAutoUpdateConfig` object",
        "#### Объект `HostGroupAutoUpdateConfig`",
    ),
    ("#### The `HostAutoUpdateConfig` object", "#### Объект `HostAutoUpdateConfig`"),
    ("#### The `ConfigurationMetadata` object", "#### Объект `ConfigurationMetadata`"),
    ("#### The `UpdateWindowsConfig` object", "#### Объект `UpdateWindowsConfig`"),
    ("#### The `UpdateWindow` object", "#### Объект `UpdateWindow`"),
    ("#### The `ErrorEnvelope` object", "#### Объект `ErrorEnvelope`"),
    ("#### The `Error` object", "#### Объект `Error`"),
    ("#### The `ConstraintViolation` object", "#### Объект `ConstraintViolation`"),
    (
        "#### The `TechMonitoringConfigList` object",
        "#### Объект `TechMonitoringConfigList`",
    ),
    ("#### The `Technology` object", "#### Объект `Technology`"),
    ("#### The `HostConfig` object", "#### Объект `HostConfig`"),
    ("#### The `MonitoringConfig` object", "#### Объект `MonitoringConfig`"),
    # --- (7) intro sentences ---
    (
        "Gets the environment-wide configuration of OneAgent auto-update.",
        "Возвращает конфигурацию авто-обновления OneAgent для всего окружения.",
    ),
    (
        "Updates the environment-wide configuration of OneAgent auto-update.",
        "Обновляет конфигурацию авто-обновления OneAgent для всего окружения.",
    ),
    (
        "Gets the environment-wide technology monitoring configuration of OneAgent.",
        "Возвращает конфигурацию мониторинга технологий OneAgent для всего окружения.",
    ),
    (
        "Gets the configuration of OneAgent auto-update in the specified host group.",
        "Возвращает конфигурацию авто-обновления OneAgent в указанной группе хостов.",
    ),
    (
        "Updates the configuration of OneAgent auto-update in the specified host group.",
        "Обновляет конфигурацию авто-обновления OneAgent в указанной группе хостов.",
    ),
    (
        "Gets the configuration of OneAgent auto-update on the specified host.",
        "Возвращает конфигурацию авто-обновления OneAgent на указанном хосте.",
    ),
    (
        "Updates the configuration of OneAgent auto-update on the specified host.",
        "Обновляет конфигурацию авто-обновления OneAgent на указанном хосте.",
    ),
    (
        "Gets the configuration of monitored technologies on the specified host.",
        "Возвращает конфигурацию отслеживаемых технологий на указанном хосте.",
    ),
    (
        "Updates the monitoring configuration of OneAgent on the specified host.",
        "Обновляет конфигурацию мониторинга OneAgent на указанном хосте.",
    ),
    (
        "Gets OneAgent configuration on the specified host. You can later change the auto-update and monitoring configuration with one of the following requests:",
        "Возвращает конфигурацию OneAgent на указанном хосте. Изменить конфигурацию авто-обновления и мониторинга можно позже одним из следующих запросов:",
    ),
    (
        "OneAgents that connect to the environment use this configuration only when their **setting** is set to `INHERITED`.",
        "OneAgent, подключающиеся к окружению, используют эту конфигурацию только когда их **setting** имеет значение `INHERITED`.",
    ),
    (
        "OneAgents installed on hosts of the host group use this configuration only when their **setting** is set to `INHERITED`.",
        "OneAgent, установленные на хостах группы хостов, используют эту конфигурацию только когда их **setting** имеет значение `INHERITED`.",
    ),
    # --- (8) object descriptions ---
    (
        "Environment-wide configuration of OneAgents auto-updates.",
        "Конфигурация авто-обновлений OneAgent для всего окружения.",
    ),
    (
        "Applies to all OneAgents connecting to the environment if their **setting** parameter is set to `INHERITED`. Otherwise, the host group or host level setting applies.",
        "Применяется ко всем OneAgent, подключающимся к окружению, если их параметр **setting** имеет значение `INHERITED`. Иначе применяется настройка уровня группы хостов или хоста.",
    ),
    (
        "Configuration of OneAgent auto-update in a host group.",
        "Конфигурация авто-обновления OneAgent в группе хостов.",
    ),
    (
        "Applies to all OneAgents installed on hosts of the host group if their **setting** parameter is set to `INHERITED`. Otherwise, the host level setting applies.",
        "Применяется ко всем OneAgent, установленным на хостах группы хостов, если их параметр **setting** имеет значение `INHERITED`. Иначе применяется настройка уровня хоста.",
    ),
    (
        "Configuration of OneAgent auto-update.",
        "Конфигурация авто-обновления OneAgent.",
    ),
    ("OneAgent configuration on a host.", "Конфигурация OneAgent на хосте."),
    ("Monitoring configuration of OneAgent.", "Конфигурация мониторинга OneAgent."),
    (
        "A list of technology monitoring configurations.",
        "Список конфигураций мониторинга технологий.",
    ),
    ("Configuration of technology monitoring.", "Конфигурация мониторинга технологий."),
    (
        "Basic information about all configured update windows",
        "Базовая информация обо всех настроенных окнах обновления",
    ),
    (
        "Basic information about one maintenance window",
        "Базовая информация об одном maintenance window",
    ),
    # --- (9) parameter cell descriptions ---
    (
        "The Dynatrace entity ID of the required host group.",
        "ID сущности Dynatrace требуемой группы хостов.",
    ),
    (
        "The Dynatrace entity ID of the host where OneAgent is deployed.",
        "ID сущности Dynatrace хоста, где развёрнут OneAgent.",
    ),
    (
        "The Dynatrace entity ID of the host group.",
        "ID сущности Dynatrace группы хостов.",
    ),
    (
        "The Dynatrace entity ID of the required host.",
        "ID сущности Dynatrace требуемого хоста.",
    ),
    (
        "The JSON body of the request. Contains OneAgent auto-update parameters.",
        "JSON-тело запроса. Содержит параметры авто-обновления OneAgent.",
    ),
    (
        "The JSON body of the request. Contains OneAgent monitoring parameters.",
        "JSON-тело запроса. Содержит параметры мониторинга OneAgent.",
    ),
    # --- (10) element descriptions (full strings incl. trailing prefix before enum) ---
    (
        "The actual state of the auto-update on the host.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case the value is taken from the host group or the environment-wide configuration. ",
        "Фактическое состояние авто-обновления на хосте.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из конфигурации группы хостов или для всего окружения. ",
    ),
    (
        "The actual state of the auto-update on the hosts in a host group.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case the value is taken from the environment-wide setting. ",
        "Фактическое состояние авто-обновления на хостах группы хостов.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из настройки для всего окружения. ",
    ),
    (
        "The actual version to which the OneAgent must be updated.  Applicable only if the **setting** parameter is set to `INHERITED` and the **version** parameter is set to `null`. In that case the value is taken from the host group or the environment-wide configuration.",
        "Фактическая версия, до которой должен быть обновлён OneAgent.  Применяется только если параметр **setting** имеет значение `INHERITED`, а параметр **version** имеет значение `null`. В этом случае значение берётся из конфигурации группы хостов или для всего окружения.",
    ),
    (
        "The actual version to which the OneAgent must be updated.  Applicable only if the **setting** parameter is set to `INHERITED`. In that case the value is taken from the environment-wide setting.",
        "Фактическая версия, до которой должен быть обновлён OneAgent.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из настройки для всего окружения.",
    ),
    (
        "The auto-update state of OneAgents connecting to the environment:  * `ENABLED`: OneAgents automatically update to the most recent version. * `DISABLED`: OneAgents update to the version specified in the **version** field.  OneAgents that connect to the environment use this configuration only when their **setting** parameter is set to `INHERITED`. ",
        "Состояние авто-обновления OneAgent, подключающихся к окружению:  * `ENABLED`: OneAgent автоматически обновляются до последней версии. * `DISABLED`: OneAgent обновляются до версии, указанной в поле **version**.  OneAgent, подключающиеся к окружению, используют эту конфигурацию только когда их параметр **setting** имеет значение `INHERITED`. ",
    ),
    (
        "The auto-update state of OneAgents in a host group:  * `ENABLED`: OneAgents automatically update to the most recent version. * `DISABLED`: OneAgents update to the version specified in the **version** field. * `INHERITED`: The setting from the environment-wide configuration is used.  OneAgents installed on hosts of the host group use this configuration only when their **setting** parameter is set to `INHERITED`. ",
        "Состояние авто-обновления OneAgent в группе хостов:  * `ENABLED`: OneAgent автоматически обновляются до последней версии. * `DISABLED`: OneAgent обновляются до версии, указанной в поле **version**. * `INHERITED`: используется настройка из конфигурации для всего окружения.  OneAgent, установленные на хостах группы хостов, используют эту конфигурацию только когда их параметр **setting** имеет значение `INHERITED`. ",
    ),
    (
        "The auto-update state of OneAgents on the host:  * `ENABLED`: OneAgent automatically updates to the most recent version. * `DISABLED`: OneAgent updates to the version specified in the **version** field. * `INHERITED`: The setting from the host group (if the host is a member of a host group) or the environment-wide configuration (if the host doesn't belong to a host group) is used. ",
        "Состояние авто-обновления OneAgent на хосте:  * `ENABLED`: OneAgent автоматически обновляется до последней версии. * `DISABLED`: OneAgent обновляется до версии, указанной в поле **version**. * `INHERITED`: используется настройка из группы хостов (если хост входит в группу хостов) или конфигурации для всего окружения (если хост не принадлежит группе хостов). ",
    ),
    (
        "Version to update a OneAgent to when automatic updates are enabled.  Supports relative versions `latest`, `previous` and `older` as well as specific version in `<major>.<minor>` format (for example `1.261`) or `<major>.<minor>.<revision>.<timestamp>` format (for example `1.261.178.20230313-090930`).  Only applicable when the **setting** parameter is set to `ENABLED`.",
        "Версия, до которой обновлять OneAgent при включённых автоматических обновлениях.  Поддерживаются относительные версии `latest`, `previous` и `older`, а также конкретная версия в формате `<major>.<minor>` (например `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например `1.261.178.20230313-090930`).  Применяется только когда параметр **setting** имеет значение `ENABLED`.",
    ),
    (
        "The version to which the OneAgent must be updated.  Specify the version in the `<major>.<minor>.<revision>.<timestamp>` format (for example `1.191.0.20200326-161115`). You can fetch the list of available versions with the [GET available versions﻿](https://dt-url.net/fo23rb5) call.  If no suitable installer is found for the provided version or the value is set to `null`, OneAgent won't be updated.  Only applicable when the **effectiveSetting** value is `DISABLED`.  If the **setting** parameter is set to `INHERITED` but the **version** is still set, it will result in a one-time update: OneAgent will be updated to the specified version and the **version** value will be set to `null`. For further updates the parent setting will be used.",
        "Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>.<timestamp>` (например `1.191.0.20200326-161115`). Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5).  Если для указанной версии не найден подходящий установщик или значение равно `null`, OneAgent не будет обновлён.  Применяется только когда значение **effectiveSetting** равно `DISABLED`.  Если параметр **setting** имеет значение `INHERITED`, но **version** всё ещё задан, это приведёт к разовому обновлению: OneAgent будет обновлён до указанной версии, а значение **version** будет установлено в `null`. Для дальнейших обновлений будет использоваться родительская настройка.",
    ),
    (
        "The version to which the OneAgent must be updated.  Specify the version in the `<major>.<minor>.<revision>` format (for example `1.181.0`) or `<major>.<minor>` format (for example `1.181`). You can fetch the list of available versions with the [GET available versions﻿](https://dt-url.net/fo23rb5) call. If no suitable installer is found for the provided version or the value is set to `null`, OneAgent won't be updated.  Only applicable when the **setting** parameter is set to `DISABLED`.",
        "Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>` (например `1.181.0`) или `<major>.<minor>` (например `1.181`). Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5). Если для указанной версии не найден подходящий установщик или значение равно `null`, OneAgent не будет обновлён.  Применяется только когда параметр **setting** имеет значение `DISABLED`.",
    ),
    (
        "List of update windows when the OneAgent update can start. If there is no value and update should be performed, the update will start at earliest convenience.",
        "Список окон обновления, когда может начаться обновление OneAgent. Если значение отсутствует, а обновление должно быть выполнено, оно начнётся при первой возможности.",
    ),
    ("Identifier of maintenance window", "Идентификатор maintenance window"),
    ("The name of maintenance window", "Имя maintenance window"),
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
    (
        "The monitoring of the technology is enabled (`true`) or disabled (`false`).",
        "Мониторинг технологии включён (`true`) или отключён (`false`).",
    ),
    (
        "The monitoring is enabled (`true`) or disabled (`false`).",
        "Мониторинг включён (`true`) или отключён (`false`).",
    ),
    (
        "Code modules will be injected automatically into monitored applications if this setting is enabled. This setting won't apply if auto-injection is disabled via oneagentctl (see https://dt-url.net/oneagentctl).",
        "Кодовые модули будут автоматически внедряться в отслеживаемые приложения, если эта настройка включена. Эта настройка не применяется, если авто-внедрение отключено через oneagentctl (см. https://dt-url.net/oneagentctl).",
    ),
    (
        "The monitoring mode for the host: full stack or infrastructure only. ",
        "Режим мониторинга хоста: полный стек или только инфраструктура. ",
    ),
    (
        "The validity of the configuration:  * `HOST`: The setting is valid for OneAgent on host only. Other OneAgents, connected to the same Dynatrace server may have different setting. * `ENVIRONMENT`: The setting is valid for all OneAgents, connected to the Dynatrace server. ",
        "Валидность конфигурации:  * `HOST`: настройка действует только для OneAgent на хосте. Другие OneAgent, подключённые к тому же серверу Dynatrace, могут иметь другую настройку. * `ENVIRONMENT`: настройка действует для всех OneAgent, подключённых к серверу Dynatrace. ",
    ),
    ("The type of the technology. ", "Тип технологии. "),
    # --- (11) oneagent-config bullet doc-link titles (link-text EN per L4F/L4I) ---
    (
        "Edit the auto-update configuration of a OneAgent instance via the Dynatrace API.",
        "Редактирование конфигурации авто-обновления OneAgent-инстанса через Dynatrace API.",
    ),
    (
        "Update the monitoring configuration of a OneAgent instance via the Dynatrace API.",
        "Обновление конфигурации мониторинга OneAgent-инстанса через Dynatrace API.",
    ),
    # --- (12) BOM cleanup in inline link-text (link-text EN, L4B) ---
    ("[GET available versions﻿]", "[GET available versions]"),
    # --- (13) global: element-can-hold -> Возможные значения: WITH colon (L99) ---
    ("The element can hold these values", "Возможные значения:"),
]


def build(rel):
    src = os.path.join(EN, rel)
    dst = os.path.join(RU, rel)
    with io.open(src, "r", encoding="utf-8", newline="") as f:
        t = f.read()
    t = t.replace("\r\n", "\n")  # EN is CRLF; RU corpus convention is LF
    # Source BOM mojibake is the 3-char EF BB BF (ï»¿), NOT U+FEFF. Strip it
    # up-front (canon L4B: BOM removed, link-text EN [GET available versions]).
    t = t.replace("ï»¿", "")
    # Normalize any stray U+FEFF accidentally embedded in rule literals so
    # rule EN matches the now-clean source text.
    for en, ru in [(e.replace("﻿", ""), r) for e, r in R]:
        t = t.replace(en, ru)
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    with io.open(dst, "w", encoding="utf-8", newline="\n") as f:
        f.write(t)
    return dst


if __name__ == "__main__":
    for rel in FILES:
        d = build(rel)
        print("wrote", d)
