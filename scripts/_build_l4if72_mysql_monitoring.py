# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/mysql-monitoring.md (SQL monitoring template)."""

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
    "title: MySQL monitoring configuration": "title: Конфигурация мониторинга MySQL",
    "# MySQL monitoring configuration": "# Конфигурация мониторинга MySQL",
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    "* Databases from which to collect data": "* Базы данных, из которых собираются данные",
    "Example payload to activate the MySQL extension:": "Пример полезной нагрузки для активации расширения MySQL:",
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlMySqlRemote` section.": "В одной конфигурации мониторинга в разделе `sqlMySqlRemote` можно определить до 20 000 эндпоинтов.",
    "To define the MySQL Database server, add the following details in the `endpoints` section:": "Чтобы задать сервер базы данных MySQL, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Database name": "* Database name",
    "* Authentication credentials": "* Учётные данные аутентификации",
    # MySQL uses "Authentication details passed to the Dynatrace API when activating monitoring configuration..." (no "a" before "monitoring")
    # same as SHARED — already covered
    # Auth sub-sections
    "#### Basic": "#### Базовая аутентификация",
    "Basic authentication requires only a username and password.": "Базовая аутентификация требует только имя пользователя и пароль.",
    "#### AWS IAM": "#### AWS IAM",
    "ActiveGate version 1.325+": "ActiveGate версии 1.325+",
    "Allows connection to Amazon RDS or Amazon Aurora databases using AWS IAM database authentication. Requires AWS Identity and Access Management (IAM) set up and an AWS IAM identity available to the ActiveGate host (for example, an attached IAM role).": "Позволяет подключаться к базам данных Amazon RDS или Amazon Aurora с использованием аутентификации базы данных AWS IAM. Требует настройки AWS Identity and Access Management (IAM) и наличия идентификатора AWS IAM, доступного хосту ActiveGate (например, подключённой роли IAM).",
    "The ActiveGate uses the IAM role assigned to it to authenticate, so there's no need to store a database password. You provide a username and a region (AWS region code, for example, `eu-central-1`). If `auto-detect` is used (ActiveGate version 1.331+) as the region value, the ActiveGate's region will be used. Otherwise, the region must match the region where the database is hosted.": "ActiveGate использует назначенную ему роль IAM для аутентификации, поэтому хранить пароль базы данных не требуется. Необходимо указать имя пользователя и регион (код региона AWS, например `eu-central-1`). Если в качестве значения региона используется `auto-detect` (ActiveGate версии 1.331+), будет применён регион ActiveGate. В противном случае регион должен совпадать с регионом, в котором размещена база данных.",
    "**Note**: AWS IAM authentication requires SSL/TLS to be enabled. Set `ssl` to `true` in your endpoint configuration. For more information, see [SSL](#ssl).": "**Примечание**: аутентификация AWS IAM требует включения SSL/TLS. Установите `ssl` в значение `true` в конфигурации эндпоинта. Подробнее см. в разделе [SSL](#ssl).",
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
}

PASS = {
    "# MySQL monitoring configuration",
}

if __name__ == "__main__":
    build_one(REL, "mysql-monitoring.md", TRANS, PASS)
    qa_one(REL, "mysql-monitoring.md")
