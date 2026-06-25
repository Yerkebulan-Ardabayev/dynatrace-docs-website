# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/microsoft-sql-monitoring.md (SQL monitoring template)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
from _build_l4if72_sql_snowflake import SHARED
from _build_l4if72_ibm_monitoring import SSL_BLOCK

REL = "ingest-from/extensions/develop-your-extensions/data-sources/sql"

TRANS = {
    **SHARED,
    **SSL_BLOCK,
    "title: Microsoft SQL Server monitoring configuration": "title: Конфигурация мониторинга Microsoft SQL Server",
    "# Microsoft SQL Server monitoring configuration": "# Конфигурация мониторинга Microsoft SQL Server",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    "* Databases from which to collect data": "* Базы данных, из которых собираются данные",
    "Example payload to activate a Microsoft SQL extension:": "Пример полезной нагрузки для активации расширения Microsoft SQL:",
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlServerRemote` section.": "В одной конфигурации мониторинга в разделе `sqlServerRemote` можно определить до 20 000 эндпоинтов.",
    "To define a Microsoft SQL Server, add the following details in the `endpoints` section:": "Чтобы задать Microsoft SQL Server, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Instance name": "* Instance name",
    "* Database name": "* Database name",
    "* Authentication credentials": "* Учётные данные аутентификации",
    # Microsoft SQL has "A human-readable description..." (with "A" prefix)
    "A human-readable description of the specifics of this monitoring configuration.": "Понятное человеку описание особенностей этой конфигурации мониторинга.",
    # Microsoft SQL has "The version of this monitoring configuration. Note..."
    "The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.": "Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.",
    # Microsoft SQL does NOT have Feature sets section in Parameters
    # Authentication sub-sections unique to Microsoft SQL
    "Authentication details passed to the Dynatrace API when activating a monitoring configuration are obfuscated and it's impossible to retrieve them.": "Данные аутентификации, передаваемые в Dynatrace API при активации конфигурации мониторинга, скрываются, и получить их невозможно.",
    "#### Basic": "#### Базовая аутентификация",
    "Basic authentication requires only a username and password.": "Базовая аутентификация требует только имя пользователя и пароль.",
    "#### Kerberos": "#### Kerberos",
    "Requires Active Directory domain set up. Allows you to connect to a database by providing a domain username, password, Key Distribution Center (KDC), and realm.": "Требует настройки домена Active Directory. Позволяет подключиться к базе данных, указав доменное имя пользователя, пароль, центр распределения ключей (KDC) и область.",
    "#### NTLM": "#### NTLM",
    "Windows only": "Только Windows",
    "Requires Active Directory domain set up. Allows you to connect to a database by providing a domain username, a domain password, and, optionally, the domain.": "Требует настройки домена Active Directory. Позволяет подключиться к базе данных, указав доменное имя пользователя, доменный пароль и, при необходимости, домен.",
    "ActiveGate version 1.251+": "ActiveGate версии 1.251+",
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
}

PASS = {
    "# Microsoft SQL Server monitoring configuration",
}

if __name__ == "__main__":
    build_one(REL, "microsoft-sql-monitoring.md", TRANS, PASS)
    qa_one(REL, "microsoft-sql-monitoring.md")
