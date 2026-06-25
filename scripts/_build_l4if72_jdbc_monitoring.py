# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/jdbc-monitoring.md (JDBC monitoring — How-to guide, unique structure)."""

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
    "title: JDBC monitoring configuration": "title: Конфигурация мониторинга JDBC",
    "# JDBC monitoring configuration": "# Конфигурация мониторинга JDBC",
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    # Intro paragraph (top-level, before Prerequisites)
    "Dynatrace Extensions SQL data source enables you to query any database allowing connections using the JDBC driver on top of all the database vendors supported by default. For such databases, some additional steps are required.": "Источник данных SQL в Dynatrace Extensions позволяет выполнять запросы к любой базе данных, поддерживающей подключение через JDBC-драйвер, в дополнение ко всем провайдерам баз данных, поддерживаемым по умолчанию. Для таких баз данных требуются дополнительные шаги.",
    "## Prerequisites": "## Предварительные требования",
    "JDBC 4.0+ based drivers are supported.": "Поддерживаются драйверы на основе JDBC 4.0+.",
    "## Upload JDBC driver to ActiveGate": "## Загрузка JDBC-драйвера на ActiveGate",
    "You need to provide the driver of your selected database vendor so that the ActiveGate running the extension can connect to the database.": "Необходимо предоставить драйвер выбранного провайдера базы данных, чтобы ActiveGate, выполняющий расширение, мог подключиться к базе данных.",
    "MariaDB example": "Пример для MariaDB",
    "For MariaDB, you can get the driver from the [Download MariaDB](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector) page.": "Для MariaDB драйвер можно загрузить со страницы [Загрузка MariaDB](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector).",
    "Download the Java 8+, platform independent connector, that is the `mariadb-java-client-3.5.0.jar`file.": "Загрузите независимый от платформы коннектор для Java 8+, то есть файл `mariadb-java-client-3.5.0.jar`.",
    "Upload the JDBC driver to an ActiveGate belonging to the group designated to run your extension:": "Загрузите JDBC-драйвер на ActiveGate, входящий в группу, назначенную для запуска расширения:",
    "**Windows**: `C:\\ProgramData\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata\\libs`": "**Windows**: `C:\\ProgramData\\dynatrace\\remotepluginmodule\\agent\\conf\\userdata\\libs`",
    "**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`": "**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`",
    "Make sure the `dtuserag` user has read access to driver. For example, for Linux, set `CHMOD` to `775`.": "Убедитесь, что пользователь `dtuserag` имеет доступ к драйверу на чтение. Например, для Linux установите `CHMOD` в значение `775`.",
    "## Monitoring configuration": "## Конфигурация мониторинга",
    # JDBC intro within Monitoring configuration section (different from standard SHARED intro)
    "After you define the scope of your configuration, you need to identify the following:": "После определения области конфигурации необходимо указать следующее:",
    "* Databases from which to collect data and their authentication details": "* Базы данных, из которых собираются данные, и их данные аутентификации",
    "* ActiveGates to execute the extension and connect to your devices. Such ActiveGates need a related [JDBC driver uploaded](#upload).": "* ActiveGate для выполнения расширения и подключения к устройствам. Такие ActiveGate должны иметь соответствующий [загруженный JDBC-драйвер](#upload).",
    "Example payload to activate the JDBC extension:": "Пример полезной нагрузки для активации расширения JDBC:",
    "Please note, that you need to provide both, the endpoint (host and port) and the related connection string.": "Обратите внимание: необходимо указать как эндпоинт (хост и порт), так и соответствующую строку подключения.",
    "Security controls": "Меры безопасности",
    "The SQL connection string syntax by its nature may expose sensitive information such as user credentials. If possible, avoid including any secret information in the connection string. If your connection string contains any sensitive information:": "Синтаксис строки подключения SQL по своей природе может раскрывать конфиденциальные сведения, например учётные данные пользователя. По возможности избегайте включения секретных данных в строку подключения. Если строка подключения содержит конфиденциальные сведения:",
    "* Limit the read and write access to JDBC monitoring configuration. Make sure that only users allowed to the secret have a read and write access to the configurations.": "* Ограничьте доступ на чтение и запись к конфигурации мониторинга JDBC. Убедитесь, что только пользователи, допущенные к секрету, имеют доступ на чтение и запись к конфигурациям.",
    "* Unlike the authentication details, the connection string is not hashed. View and edit the configuration only in safe environment where non-authorized users cannot see it.": "* В отличие от данных аутентификации, строка подключения не хешируется. Просматривайте и редактируйте конфигурацию только в безопасной среде, где неавторизованные пользователи не могут её видеть.",
    # Parameters section — JDBC has different wording for some items
    "Configuration label that should provide basic insights into of the specifics of this monitoring configuration.": "Метка конфигурации, содержащая основные сведения об особенностях данной конфигурации мониторинга.",
    "Version of this monitoring configuration.": "Версия этой конфигурации мониторинга.",
    "Add a list of feature sets you want to monitor.": "Добавьте список наборов функций, которые нужно отслеживать.",
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `jdbcRemote` section.": "В одной конфигурации мониторинга в разделе `jdbcRemote` можно определить до 20 000 эндпоинтов.",
    "To define the JDBS Database server, add the following details in the `endpoints` section:": "Чтобы задать сервер базы данных JDBC, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Connection string": "* Connection string",
    "* Authentication credentials": "* Учётные данные аутентификации",
    "ActiveGate version 1.295+": "ActiveGate версии 1.295+",
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
}

PASS = {
    "# JDBC monitoring configuration",
}

if __name__ == "__main__":
    build_one(REL, "jdbc-monitoring.md", TRANS, PASS)
    qa_one(REL, "jdbc-monitoring.md")
