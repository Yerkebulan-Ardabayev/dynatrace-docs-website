# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/ibm-monitoring.md (SQL monitoring template)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
from _build_l4if72_sql_snowflake import SHARED

REL = "ingest-from/extensions/develop-your-extensions/data-sources/sql"

# SSL block shared across IBM/JDBC/Microsoft/MySQL — defined here and reused below.
SSL_BLOCK = {
    "### SSL": "### SSL",
    "Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.": "Включите SSL, чтобы источник данных проверял сертификат сервера и использовал шифрование SSL вместо встроенного шифрования.",
    "#### Enable SSL without a local truststore": "#### Включение SSL без локального хранилища доверенных сертификатов",
    "When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.": "Если SSL включён и цепочка сертификатов сервера является публично проверяемой (например, выдана Azure или другими известными центрами сертификации), создавать хранилище доверенных сертификатов вручную не нужно. Система автоматически доверяет сертификату сервера на основе доверенных центров сертификации в среде.",
    "However, if you need to use a local truststore for certificates not globally recognized or for additional security measures": "Однако если требуется использовать локальное хранилище доверенных сертификатов для сертификатов, не признанных глобально, или для дополнительных мер безопасности:",
    "1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.": "1. В каталоге `userdata` на хостах ActiveGate, выполняющих источник данных SQL, вручную создайте хранилище доверенных сертификатов PKCS12 с именем `sqlds_truststore` и паролем `sqlds_truststore`.",
    "Command to create a truststore with keytool:": "Команда для создания хранилища доверенных сертификатов с помощью keytool:",
    "Location of `userdata` directory:": "Расположение каталога `userdata`:",
    "* Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata`": "* Windows: `%PROGRAMDATA%\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata`",
    "* Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`": "* Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`",
    "2. Add the server's certificate to it.": "2. Добавьте в него сертификат сервера.",
    "Command to import a certificate with keytool:": "Команда для импорта сертификата с помощью keytool:",
    "#### Validate SSL certificates": "#### Проверка SSL-сертификатов",
    "The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.": "Сертификат дополнительно проверяется по имени хоста, что означает: домен из сертификата должен совпадать с доменом эндпоинта, указанного в конфигурации мониторинга.",
    "Enable this option when connecting to databases using custom certificates.": "Включите этот параметр при подключении к базам данных с использованием пользовательских сертификатов.",
    "Client certificates are not supported for SQL data sources. To authenticate securely, use basic authentication with SSL enabled. For details, see [Authentication](#authentication).": "Клиентские сертификаты не поддерживаются для источников данных SQL. Для безопасной аутентификации используйте базовую аутентификацию с включённым SSL. Подробнее см. в разделе [Аутентификация](#authentication).",
}

TRANS = {
    **SHARED,
    **SSL_BLOCK,
    "title: IBM Database monitoring configuration": "title: Конфигурация мониторинга IBM Database",
    "# IBM Database monitoring configuration": "# Конфигурация мониторинга IBM Database",
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    "* Databases from which to collect data": "* Базы данных, из которых собираются данные",
    "Example payload to activate an IBM DB2 extension:": "Пример полезной нагрузки для активации расширения IBM DB2:",
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlDb2Remote` section.": "В одной конфигурации мониторинга в разделе `sqlDb2Remote` можно определить до 20 000 эндпоинтов.",
    "To define an IBM Database server, add the following details in the `endpoints` section:": "Чтобы задать сервер IBM Database, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Authentication credentials": "* Учётные данные аутентификации",
    "* Database name": "* Database name",
    # IBM has "A human-readable description..." (with "A" prefix) — different from SHARED
    "A human-readable description of the specifics of this monitoring configuration.": "Понятное человеку описание особенностей этой конфигурации мониторинга.",
    # IBM has "The version of this monitoring configuration. Note..." (with "The" prefix)
    "The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.": "Версия этой конфигурации мониторинга. Обратите внимание, что одно расширение может выполнять несколько конфигураций мониторинга.",
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
    "#### SSL": "#### SSL",
    "### SSL": "### SSL",
    "#### Enable SSL without a local truststore": "#### Включение SSL без локального хранилища доверенных сертификатов",
    "#### Validate SSL certificates": "#### Проверка SSL-сертификатов",
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
}

PASS = {
    "# IBM Database monitoring configuration",
}

if __name__ == "__main__":
    build_one(REL, "ibm-monitoring.md", TRANS, PASS)
    qa_one(REL, "ibm-monitoring.md")
