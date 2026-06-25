# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/sap-hana-monitoring.md."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
from _build_l4if72_sql_snowflake import SHARED

REL = "ingest-from/extensions/develop-your-extensions/data-sources/sql"

TRANS = {
    **SHARED,
    # --- frontmatter / title / H1 ---
    "title: SAP Hana Database monitoring configuration": "title: Конфигурация мониторинга SAP Hana Database",
    "# SAP Hana Database monitoring configuration": "# Конфигурация мониторинга SAP Hana Database",
    # --- meta ---
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    # --- intro ---
    "* Databases from which to collect data": "* Базы данных, из которых собираются данные",
    # --- Example payload ---
    "Example payload to activate the SAP Hana extension:": "Пример полезной нагрузки для активации расширения SAP Hana:",
    # --- ### Endpoints unique lines ---
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlHanaRemote` section.": "В одной конфигурации мониторинга в разделе `sqlHanaRemote` можно определить до 20 000 эндпоинтов.",
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
    # --- Replace line (in ### Scope via SHARED) ---
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
    # --- ## SAP Hana JDBC Driver ---
    "## SAP Hana JDBC Driver": "## SAP Hana JDBC Driver",
    "The SAP Hana data source requires to put SAP Hana JDBC driver version 2.14.x in Dynatrace Extension Framework 2.0.": "Источник данных SAP Hana требует наличия драйвера SAP Hana JDBC версии 2.14.x в Dynatrace Extension Framework 2.0.",
    "To define the SAP Hana Database server, put `ngdbc.jar` file in the following location on the ActiveGate host:": "Чтобы задать сервер SAP Hana Database, поместите файл `ngdbc.jar` в следующее расположение на хосте ActiveGate:",
    "**Windows**: `C:\\ProgramData\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata\\libs`": "**Windows**: `C:\\ProgramData\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata\\libs`",
    "**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`": "**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`",
}

if __name__ == "__main__":
    build_one(REL, "sap-hana-monitoring.md", TRANS)
    qa_one(REL, "sap-hana-monitoring.md")
