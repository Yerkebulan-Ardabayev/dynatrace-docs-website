# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/develop-your-extensions/data-sources/sql.md (SQL hub page)."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/develop-your-extensions/data-sources"

TRANS = {
    "title: SQL data source": "title: Источник данных SQL",
    "# SQL data source": "# Источник данных SQL",
    "* Overview": "* Обзор",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Apr 11, 2022": "* Опубликовано 11 апреля 2022 г.",
    "Dynatrace provides you with a framework that you can use to extend your observability into data acquired from a database using SQL queries.": "Dynatrace предоставляет платформу, позволяющую расширить наблюдаемость за данными, получаемыми из базы данных с помощью SQL-запросов.",
    "We assume the following:": "Предполагается следующее:",
    "* You possess sufficient database subject matter expertise to create an extension. In particular, you know how to build and execute SQL queries.": "* Наличие достаточной экспертизы в области баз данных для создания расширения. В частности, знание того, как строить и выполнять SQL-запросы.",
    '* You\'re familiar with [Extensions basic concepts](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").': '* Знакомство с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [файла YAML расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").',
    'Learn about the prerequisites and scope of the supported technologies. For limits applying to your extension, see [Extensions limits](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.").': 'Сведения о предварительных требованиях и области поддерживаемых технологий. Сведения об ограничениях, применяемых к расширению, см. в разделе [Ограничения Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.").',
    "## Supported Dynatrace versions": "## Поддерживаемые версии Dynatrace",
    "* Dynatrace version 1.295+": "* Dynatrace версии 1.295+",
    "* Environment ActiveGate version 1.295+": "* Environment ActiveGate версии 1.295+",
    "## Supported database providers": "## Поддерживаемые провайдеры баз данных",
    "* Oracle": "* Oracle",
    "* Microsoft SQL Server": "* Microsoft SQL Server",
    "* IBM DB2": "* IBM DB2",
    "* MySQL": "* MySQL",
    "* PostgreSQL": "* PostgreSQL",
    "* SAP Hana": "* SAP Hana",
    "* Snowflake": "* Snowflake",
    "* Any database vendor that provides a JDBC driver that allows applications to connect a database and execute queries. For example MariaDB, Sybase, or Informix.": "* Любой провайдер баз данных, предоставляющий JDBC-драйвер, позволяющий приложениям подключаться к базе данных и выполнять запросы, например MariaDB, Sybase или Informix.",
    "## Remote monitoring": "## Удалённый мониторинг",
    "The SQL data source supports remote database access using various authentication schemes. While basic authentication is supported, more advanced schemes such as Kerberos and NTLM are also supported for Microsoft SQL data source.": "Источник данных SQL поддерживает удалённый доступ к базе данных с использованием различных схем аутентификации. Помимо базовой аутентификации, для источника данных Microsoft SQL поддерживаются и более продвинутые схемы, такие как Kerberos и NTLM.",
    "## Create extension": "## Создание расширения",
    '* See [SQL data source reference](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference "Learn about SQL extensions in the Extensions framework.") to learn about the structure of the extension YAML file.': '* Сведения о структуре файла YAML расширения см. в [справочнике по источнику данных SQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference "Learn about SQL extensions in the Extensions framework.").',
    "## Monitoring configuration": "## Конфигурация мониторинга",
    '* See [Oracle Database monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to learn how to create an Oracle Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для Oracle Database см. в разделе [Конфигурация мониторинга Oracle Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.").',
    '* See [Microsoft SQL Server monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Microsoft SQL extensions in the Extensions framework.") to learn how to create a Microsoft Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для Microsoft SQL Server см. в разделе [Конфигурация мониторинга Microsoft SQL Server](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Microsoft SQL extensions in the Extensions framework.").',
    '* See [IBM Database monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "IBM DB2 extensions in the Extensions framework.") to learn how to create an IBM Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для IBM Database см. в разделе [Конфигурация мониторинга IBM Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "IBM DB2 extensions in the Extensions framework.").',
    '* See [MySQL monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "MySQL extensions in the Extensions framework.") to learn how to create a MySQL Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для MySQL см. в разделе [Конфигурация мониторинга MySQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "MySQL extensions in the Extensions framework.").',
    '* See [PostgreSQL monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "PostgreSQL extensions in the Extensions framework.") to learn how to create a PostgreSQL Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для PostgreSQL см. в разделе [Конфигурация мониторинга PostgreSQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "PostgreSQL extensions in the Extensions framework.").',
    '* See [SAP Hana Database monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "SAP Hana extensions in the Extensions framework.") to learn how to create a SAP Hana Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для SAP Hana Database см. в разделе [Конфигурация мониторинга базы данных SAP Hana](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "SAP Hana extensions in the Extensions framework.").',
    '* See [Snowflake Database monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Snowflake Database extensions in the Extensions framework.") to learn how to create a Snowflake Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для базы данных Snowflake см. в разделе [Конфигурация мониторинга базы данных Snowflake](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Snowflake Database extensions in the Extensions framework.").',
    '* See [JDBC monitoring configuration](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "JDBC extensions in the Extensions framework.") to learn how to create a JDBC Database–specific monitoring configuration.': '* Сведения о создании конфигурации мониторинга для JDBC см. в разделе [Конфигурация мониторинга JDBC](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "JDBC extensions in the Extensions framework.").',
}

PASS = {
    "# SQL data source",
}

if __name__ == "__main__":
    build_one(REL, "sql.md", TRANS, PASS)
    qa_one(REL, "sql.md")
