---
title: SQL data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql
scraped: 2026-03-06T21:31:46.228065
---

# Источник данных SQL

# Источник данных SQL

* Последняя версия Dynatrace
* Обзор
* Время чтения: 2 мин
* Опубликовано 11 апреля 2022 г.

Dynatrace предоставляет фреймворк, который позволяет расширить наблюдаемость за счёт данных, получаемых из базы данных с помощью SQL-запросов.

Предполагается следующее:

* Вы обладаете достаточными экспертными знаниями в области баз данных для создания расширения. В частности, вы знаете, как строить и выполнять SQL-запросы.
* Вы знакомы с [основными концепциями расширений](/docs/ingest-from/extensions/concepts "Подробнее об основных концепциях расширений Dynatrace.") и общей структурой [файла YAML расширения](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Узнайте, как создать файл YAML расширения с использованием фреймворка расширений.").

Ознакомьтесь с предварительными условиями и объёмом поддерживаемых технологий. Об ограничениях, применимых к вашему расширению, см. в разделе [Ограничения расширений](/docs/ingest-from/extensions/concepts "Подробнее об основных концепциях расширений Dynatrace.").

## Поддерживаемые версии Dynatrace

* Dynatrace версии 1.295+
* ActiveGate окружения версии 1.295+

## Поддерживаемые поставщики баз данных

* Oracle
* Microsoft SQL Server
* IBM DB2
* MySQL
* PostgreSQL
* SAP Hana
* Snowflake
* Любой поставщик баз данных, предоставляющий JDBC-драйвер, позволяющий приложениям подключаться к базе данных и выполнять запросы. Например, MariaDB, Sybase или Informix.

## Удалённый мониторинг

Источник данных SQL поддерживает удалённый доступ к базам данных с использованием различных схем аутентификации. Поддерживается базовая аутентификация, а также более продвинутые схемы, такие как Kerberos и NTLM, для источника данных Microsoft SQL.

## Создание расширения

* См. [Справочник по источнику данных SQL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sql-reference "Узнайте о структуре файла YAML расширения для SQL-расширений."), чтобы ознакомиться со структурой файла YAML расширения.

## Конфигурация мониторинга

* См. [Конфигурация мониторинга Oracle Database](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring "Создание и активация конфигурации мониторинга для расширения на основе источника данных SQL для Oracle Database."), чтобы узнать, как создать конфигурацию мониторинга для Oracle Database.
* См. [Конфигурация мониторинга Microsoft SQL Server](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring "Расширения Microsoft SQL в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для Microsoft Database.
* См. [Конфигурация мониторинга IBM Database](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring "Расширения IBM DB2 в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для IBM Database.
* См. [Конфигурация мониторинга MySQL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/mysql-monitoring "Расширения MySQL в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для MySQL.
* См. [Конфигурация мониторинга PostgreSQL](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/postgresql-monitoring "Расширения PostgreSQL в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для PostgreSQL.
* См. [Конфигурация мониторинга SAP Hana Database](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/sap-hana-monitoring "Расширения SAP Hana в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для SAP Hana Database.
* См. [Конфигурация мониторинга Snowflake Database](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring "Расширения Snowflake Database в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для Snowflake Database.
* См. [Конфигурация мониторинга JDBC](/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring "Расширения JDBC в фреймворке расширений."), чтобы узнать, как создать конфигурацию мониторинга для JDBC Database.
