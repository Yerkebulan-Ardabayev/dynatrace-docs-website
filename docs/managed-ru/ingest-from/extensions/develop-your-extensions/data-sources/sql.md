---
title: Источник данных SQL
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql
scraped: 2026-05-12T11:50:10.045626
---

# Источник данных SQL

# Источник данных SQL

* Обзор
* Чтение: 2 мин
* Опубликовано 11 апреля 2022 г.

Dynatrace предоставляет платформу, позволяющую расширить наблюдаемость за данными, получаемыми из базы данных с помощью SQL-запросов.

Предполагается следующее:

* Наличие достаточной экспертизы в области баз данных для создания расширения. В частности, знание того, как строить и выполнять SQL-запросы.
* Знакомство с [основными концепциями Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.") и общей структурой [файла YAML расширения](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с помощью платформы Extensions framework.").

Сведения о предварительных требованиях и области поддерживаемых технологий. Сведения об ограничениях, применяемых к расширению, см. в разделе [Ограничения Extensions](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.").

## Поддерживаемые версии Dynatrace

* Dynatrace версии 1.295+
* Environment ActiveGate версии 1.295+

## Поддерживаемые провайдеры баз данных

* Oracle
* Microsoft SQL Server
* IBM DB2
* MySQL
* PostgreSQL
* SAP Hana
* Snowflake
* Любой провайдер баз данных, предоставляющий JDBC-драйвер, позволяющий приложениям подключаться к базе данных и выполнять запросы, например MariaDB, Sybase или Informix.

## Удалённый мониторинг

Источник данных SQL поддерживает удалённый доступ к базе данных с использованием различных схем аутентификации. Помимо базовой аутентификации, для источника данных Microsoft SQL поддерживаются и более продвинутые схемы, такие как Kerberos и NTLM.

## Создание расширения

* Сведения о структуре файла YAML расширения см. в [справочнике по источнику данных SQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference "Узнайте о расширениях SQL в платформе Extensions framework.").

## Конфигурация мониторинга

* Сведения о создании конфигурации мониторинга для Oracle Database см. в разделе [Конфигурация мониторинга Oracle Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Создайте и активируйте конфигурацию мониторинга для расширения на основе источника данных SQL для Oracle Database.").
* Сведения о создании конфигурации мониторинга для Microsoft SQL Server см. в разделе [Конфигурация мониторинга Microsoft SQL Server](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Расширения Microsoft SQL в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для IBM Database см. в разделе [Конфигурация мониторинга IBM Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "Расширения IBM DB2 в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для MySQL см. в разделе [Конфигурация мониторинга MySQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "Расширения MySQL в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для PostgreSQL см. в разделе [Конфигурация мониторинга PostgreSQL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "Расширения PostgreSQL в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для SAP Hana Database см. в разделе [Конфигурация мониторинга базы данных SAP Hana](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "Расширения SAP Hana в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для базы данных Snowflake см. в разделе [Конфигурация мониторинга базы данных Snowflake](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Расширения базы данных Snowflake в платформе Extensions framework.").
* Сведения о создании конфигурации мониторинга для JDBC см. в разделе [Конфигурация мониторинга JDBC](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "Расширения JDBC в платформе Extensions framework.").