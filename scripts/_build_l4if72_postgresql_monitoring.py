# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/postgresql-monitoring.md."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
from _build_l4if72_sql_snowflake import SHARED

REL = "ingest-from/extensions/develop-your-extensions/data-sources/sql"

TRANS = {
    **SHARED,
    # --- frontmatter / title / H1 ---
    "title: PostgreSQL monitoring configuration": "title: Конфигурация мониторинга PostgreSQL",
    "# PostgreSQL monitoring configuration": "# Конфигурация мониторинга PostgreSQL",
    # --- meta ---
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    # --- intro ---
    "* Databases from which to collect data": "* Базы данных, из которых собираются данные",
    # --- Example payload ---
    "Example payload to activate the PostgreSQL extension:": "Пример полезной нагрузки для активации расширения PostgreSQL:",
    # --- ### Endpoints unique lines ---
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlPostgresRemote` section.": "В одной конфигурации мониторинга в разделе `sqlPostgresRemote` можно определить до 20 000 эндпоинтов.",
    "To define the PostgreSQL Database server, add the following details in the `endpoints` section:": "Чтобы задать сервер PostgreSQL Database, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Database name": "* Database name",
    "* Authentication credentials": "* Учётные данные аутентификации",
    # --- ### Authentication sub-sections ---
    "#### Basic": "#### Basic",
    "Basic authentication requires only a username and password.": "Базовая аутентификация требует только имени пользователя и пароля.",
    "#### AWS IAM": "#### AWS IAM",
    "ActiveGate version 1.325+": "ActiveGate версии 1.325+",
    "Allows connection to Amazon RDS or Amazon Aurora databases using AWS IAM database authentication. Requires AWS Identity and Access Management (IAM) set up and an AWS IAM identity available to the ActiveGate host (for example, an attached IAM role).": "Обеспечивает подключение к базам данных Amazon RDS или Amazon Aurora с использованием аутентификации AWS IAM. Требуется настройка AWS Identity and Access Management (IAM) и наличие удостоверения AWS IAM на хосте ActiveGate (например, прикреплённой роли IAM).",
    "The ActiveGate uses the IAM role assigned to it to authenticate, so there's no need to store a database password. You provide a username and a region (AWS region code, for example, `eu-central-1`). If `auto-detect` is used (ActiveGate version 1.331+) as the region value, the ActiveGate's region will be used. Otherwise, the region must match the region where the database is hosted.": "ActiveGate использует назначенную ему роль IAM для аутентификации, поэтому хранить пароль базы данных не требуется. Укажите имя пользователя и регион (код региона AWS, например `eu-central-1`). Если в качестве значения региона используется `auto-detect` (ActiveGate версии 1.331+), будет применён регион ActiveGate. В противном случае регион должен совпадать с регионом, в котором размещена база данных.",
    "**Note**: AWS IAM authentication requires SSL/TLS to be enabled. Set `ssl` to `true` in your endpoint configuration. For more information, see [SSL](#ssl).": "**Примечание**: аутентификация AWS IAM требует включения SSL/TLS. Задайте `ssl` значение `true` в конфигурации эндпоинта. Дополнительные сведения см. в разделе [SSL](#ssl).",
    # --- ### SSL ---
    "### SSL": "### SSL",
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
    "Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.": "Включите SSL, чтобы источник данных проверял сертификат сервера и использовал шифрование SSL вместо встроенного.",
    "#### Enable SSL without a local truststore": "#### Включение SSL без локального хранилища доверия",
    "When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.": "Если SSL включён и цепочка сертификатов сервера проверяется публично (например, выдана Azure или другими известными удостоверяющими центрами), создавать хранилище доверия вручную не требуется. Система автоматически доверяет сертификату сервера на основе доверенных удостоверяющих центров в среде.",
    "However, if you need to use a local truststore for certificates not globally recognized or for additional security measures": "Однако если требуется использовать локальное хранилище доверия для сертификатов, не признанных глобально, или в целях дополнительной защиты:",
    "1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.": "1. В каталоге `userdata` на ActiveGate, выполняющих источник данных SQL, вручную создайте хранилище доверия PKCS12 с именем `sqlds_truststore` и паролем `sqlds_truststore`.",
    "Command to create a truststore with keytool:": "Команда для создания хранилища доверия с помощью keytool:",
    "Location of `userdata` directory:": "Расположение каталога `userdata`:",
    "* Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata`": "* Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata`",
    "* Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`": "* Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`",
    "2. Add the server's certificate to it.": "2. Добавьте в него сертификат сервера.",
    "Command to import a certificate with keytool:": "Команда для импорта сертификата с помощью keytool:",
    "#### Validate SSL certificates": "#### Проверка SSL-сертификатов",
    "The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.": "Сертификат дополнительно проверяется по имени хоста: домен из сертификата должен совпадать с доменом эндпоинта, указанного в конфигурации мониторинга.",
    "Enable this option when connecting to databases using custom certificates.": "Включите этот параметр при подключении к базам данных с использованием пользовательских сертификатов.",
    "Client certificates are not supported for SQL data sources. To authenticate securely, use basic authentication with SSL enabled. For details, see [Authentication](#authentication).": "Клиентские сертификаты не поддерживаются для источников данных SQL. Для безопасной аутентификации используйте базовую аутентификацию с включённым SSL. Подробные сведения см. в разделе [Аутентификация](#authentication).",
    # --- ### Scope (already in SHARED as ### Scope -> "### Scope" kept EN) ---
    # SHARED handles: ### Scope heading, Sign extension link, ActiveGate group link,
    # Use the following format..., Replace <ActiveGate-group-name>...
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
    # --- Description variant in postgresql (has article "A") ---
    "A human-readable description of the specifics of this monitoring configuration.": "Понятное человеку описание особенностей этой конфигурации мониторинга.",
    # --- Version variant in postgresql (has article "The") ---
    "The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.": "Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.",
}

if __name__ == "__main__":
    build_one(REL, "postgresql-monitoring.md", TRANS)
    qa_one(REL, "postgresql-monitoring.md")
