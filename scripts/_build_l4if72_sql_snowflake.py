# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/snowflake-monitoring.md (SQL-monitoring template ANCHOR).

The 8 SQL */-monitoring.md files share most sentences verbatim. This file is the
canonical RU for those shared lines; the other SQL builders reuse SHARED below so
the whole sql/ subtree stays byte-consistent. Import it:  from
_build_l4if72_sql_snowflake import SHARED  ->  TRANS = {**SHARED, ...unique...}.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources/sql"

# Sentences shared across SQL monitoring pages (reused by sibling builders).
SHARED = {
    "* Reference": "* Справочник",
    "* 2-min read": "* Чтение: 2 мин",
    "After you define the scope of your configuration, you need to identify the following:": "После определения области конфигурации необходимо указать следующее:",
    "* ActiveGates to execute the extension and connect to your devices": "* ActiveGate для выполнения расширения и подключения к вашим устройствам",
    "## Example payload": "## Пример полезной нагрузки",
    "## Parameters": "## Параметры",
    "### Enabled": "### Enabled",
    "If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.": "Если задано значение `true`, конфигурация активна и Dynatrace немедленно начинает мониторинг.",
    "### Description": "### Description",
    "Human-readable description of the specifics of this monitoring configuration.": "Понятное человеку описание особенностей этой конфигурации мониторинга.",
    "### Version": "### Version",
    "Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.": "Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.",
    "### Feature sets": "### Feature sets",
    "Add a list of feature sets you want to monitor. To report all feature sets, add `all`.": "Добавьте список наборов функций, которые нужно отслеживать. Чтобы передавать все наборы функций, добавьте `all`.",
    "### Endpoints": "### Endpoints",
    "### Authentication": "### Authentication",
    "Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.": "Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются, и получить их невозможно.",
    "#### Credential vault": "#### Хранилище учётных данных",
    "The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:": "Тип аутентификации через хранилище учётных данных обеспечивает более безопасный подход к использованию расширений за счёт надёжного хранения учётных данных пользователя и управления ими. Чтобы использовать этот способ, нужно быть владельцем учётных данных и иметь хранилище учётных данных, отвечающее следующим критериям:",
    "* **Credential type**—User and password": "* **Тип учётных данных**: имя пользователя и пароль",
    "* **Credential scope**—Synthetic (in case of external vault usage) and Extension authentication scopes enabled": "* **Область доступа учётных данных**: включены области Synthetic (при использовании внешнего хранилища) и Extension authentication",
    "* **Owner access only** is enabled only for credential owners": "* Параметр **Owner access only** включён только для владельцев учётных данных",
    "### Scope": "### Scope",
    'Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").': 'Обратите внимание, что каждому хосту ActiveGate, на котором выполняется расширение, нужен корневой сертификат для проверки подлинности расширения. Дополнительные сведения см. в разделе [Подписание расширения](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Узнайте, как подписать расширение, загрузить сертификаты и пользовательские расширения и настроить разрешения сертификатов с помощью платформы Dynatrace Extensions Framework.").',
    'The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").': 'Область доступа, это группа ActiveGate, которая будет выполнять расширение. Эту конфигурацию мониторинга запустит только один ActiveGate из группы. Если планируется использовать один ActiveGate, назначьте его в выделенную группу. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").',
    "Use the following format when defining the ActiveGate group:": "При определении группы ActiveGate используйте следующий формат:",
}

TRANS = {
    **SHARED,
    "title: Snowflake Database monitoring configuration": "title: Конфигурация мониторинга базы данных Snowflake",
    "# Snowflake Database monitoring configuration": "# Конфигурация мониторинга базы данных Snowflake",
    "* Published Apr 19, 2023": "* Опубликовано 19 апреля 2023 г.",
    "* Databases from which to collect data": "* Базы данных, из которых собираются данные",
    "Example payload to activate the Snowflake Database extension:": "Пример полезной нагрузки для активации расширения базы данных Snowflake:",
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `SQLSnowflakeRemote` section.": "В одной конфигурации мониторинга в разделе `SQLSnowflakeRemote` можно определить до 20 000 эндпоинтов.",
    "To define the Snowflake Database server, add the following details in the `endpoints` section:": "Чтобы задать сервер базы данных Snowflake, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Database name": "* Database name",
    "* Warehouse": "* Warehouse",
    "* Schema": "* Schema",
    "* Authentication credentials": "* Учётные данные аутентификации",
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
}

if __name__ == "__main__":
    build_one(REL, "snowflake-monitoring.md", TRANS)
    qa_one(REL, "snowflake-monitoring.md")
