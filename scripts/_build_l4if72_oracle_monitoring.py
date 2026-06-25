# -*- coding: utf-8 -*-
"""L4-IF.72 — sql/oracle-monitoring.md."""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one
from _build_l4if72_sql_snowflake import SHARED

REL = "ingest-from/extensions/develop-your-extensions/data-sources/sql"

TRANS = {
    **SHARED,
    # --- frontmatter / title / H1 ---
    "title: Oracle Database monitoring configuration": "title: Конфигурация мониторинга Oracle Database",
    "# Oracle Database monitoring configuration": "# Конфигурация мониторинга Oracle Database",
    # --- meta ---
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Apr 09, 2026": "* Обновлено 9 апреля 2026 г.",
    # --- intro (oracle has a different intro from SHARED) ---
    "After you define the scope of your configuration, you need to identify the databases you'd like to collect data from and identify the ActiveGates that will execute the extension and connect to your devices.": "После определения области конфигурации необходимо указать базы данных, из которых нужно собирать данные, и ActiveGate, которые будут выполнять расширение и подключаться к устройствам.",
    'Make sure that all the ActiveGates from the ActiveGate group you\'ll define as the scope can connect to a respective data source. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").': 'Убедитесь, что все ActiveGate из группы ActiveGate, определённой как область, могут подключиться к соответствующему источнику данных. Назначить ActiveGate в группу можно во время установки или после неё. Дополнительные сведения см. в разделе [Группа ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-group "Изучите основные концепции групп ActiveGate.").',
    'The monitoring configuration is a JSON payload defining the connection details, credentials, and feature sets that you want to monitor. For details, see [Start monitoring](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': 'Конфигурация мониторинга представляет собой JSON-полезную нагрузку, определяющую сведения о подключении, учётные данные и наборы функций для мониторинга. Подробные сведения см. в разделе [Запуск мониторинга](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").',
    "Example payload to activate an Oracle SQL extension:": "Пример полезной нагрузки для активации расширения Oracle SQL:",
    'When you have your initial extension YAML ready, package it, sign it, and upload it to your Dynatrace environment. For details, see [Manage extension lifecyle](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': 'Когда начальный файл YAML расширения будет готов, упакуйте его, подпишите и загрузите в среду Dynatrace. Подробные сведения см. в разделе [Управление жизненным циклом расширения](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").',
    "The Dynatrace Hub-based extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration": "Мастер активации расширений на основе Dynatrace Hub содержит динамически обновляемую JSON-полезную нагрузку с конфигурацией мониторинга.",
    "You can also use the Dynatrace API to download the schema for your extension that will help you create the JSON payload for your monitoring configuration.": "Также можно использовать Dynatrace API для загрузки схемы расширения, которая поможет сформировать JSON-полезную нагрузку для конфигурации мониторинга.",
    'Use the [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint.': 'Используйте эндпоинт [GET an extension schema](/managed/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.").',
    "Issue the following request:": "Выполните следующий запрос:",
    "Make sure to replace `{extension-name}` and `{extension-version}` with values from your extension YAML file. A successful call returns the JSON schema.": "Замените `{extension-name}` и `{extension-version}` значениями из YAML-файла расширения. При успешном вызове возвращается JSON-схема.",
    # --- ## Scope (heading-level, not SHARED which is ###) ---
    "## Scope": "## Область доступа",
    # SHARED has ### Scope -> "### Scope" (kept EN). Here ## Scope needs RU.
    # --- ## Version / ## Description / ## Enabled (heading-level) ---
    "## Version": "## Version",
    "## Description": "## Description",
    "## Enabled": "## Enabled",
    # --- ## Endpoints ---
    "## Endpoints": "## Endpoints",
    "You can define up to 20,000 endpoints in a single monitoring configuration in the `SQLOracleRemote` section.": "В одной конфигурации мониторинга в разделе `SQLOracleRemote` можно определить до 20 000 эндпоинтов.",
    "### Oracle JDBC Driver": "### Oracle JDBC Driver",
    "The Oracle SQL data source requires the Oracle JDBC driver distributed by Dynatrace. By setting the `licenceAccepted` property to `true`, you indicate that you have read and accepted the [Dynatrace redistribution license agreement for Oracle JDBC Driver﻿](https://dt-url.net/0s1n0pw9).": "Источник данных Oracle SQL требует наличия драйвера Oracle JDBC, распространяемого Dynatrace. Установив свойство `licenceAccepted` в значение `true`, вы подтверждаете, что ознакомились с [лицензионным соглашением Dynatrace на распространение Oracle JDBC Driver](https://dt-url.net/0s1n0pw9) и принимаете его.",
    "To define an Oracle Database server, add the following details in the `endpoints` section:": "Чтобы задать сервер Oracle Database, добавьте в раздел `endpoints` следующие сведения:",
    "* Host": "* Host",
    "* Port": "* Port",
    "* Database identifier, either `serviceName` or `sid`.": "* Идентификатор базы данных: `serviceName` или `sid`.",
    "* Authentication credentials": "* Учётные данные аутентификации",
    "The Oracle JDBC driver version shipped with the Extension Framework is `ojdbc11`.": "Версия драйвера Oracle JDBC, поставляемая с Extension Framework: `ojdbc11`.",
    # --- ## Authentication ---
    "## Authentication": "## Authentication",
    "### Credential vault": "### Хранилище учётных данных",
    # --- ## Feature sets ---
    "## Feature sets": "## Feature sets",
    "### TopN": "### TopN",
    "The feature set `topN` enables monitoring of the most resource-intensive queries. Enabled by default.": "Набор функций `topN` включает мониторинг наиболее ресурсоёмких запросов. Включён по умолчанию.",
    "This groups topN queries by an entity. The queries are displayed on the event page and on a unified analysis page for the Oracle server entity.": "Это группирует запросы topN по сущности. Запросы отображаются на странице событий и на единой странице анализа для сущности Oracle-сервера.",
    "### Multitenancy": "### Multitenancy",
    "The feature set `multitenancy` enhances the monitoring capabilities by querying and retrieving information about Container Databases (CDBs), Pluggable Databases (PDBs), and the services associated with the specified database in the monitoring configuration.": "Набор функций `multitenancy` расширяет возможности мониторинга путём запроса и получения сведений о контейнерных базах данных (CDB), подключаемых базах данных (PDB) и сервисах, связанных с указанной базой данных в конфигурации мониторинга.",
    "Example navigation": "Пример навигации",
    "To navigate through the structure of Oracle entities": "Для навигации по структуре сущностей Oracle:",
    "1. Go to **Dashboards** and open the **Oracle Database Overview** dashboard.": "1. Откройте **Dashboards** и откройте дашборд **Oracle Database Overview**.",
    "2. In the **Hosts** section of the dashboard, select the host from the **Oracle DB host** column.": "2. В разделе **Hosts** дашборда выберите хост в столбце **Oracle DB host**.",
    "3. On the **Oracle DB server** page, select a CDB.": "3. На странице **Oracle DB server** выберите CDB.",
    "![Oracle Database multitenancy: CDBs](https://dt-cdn.net/images/cbds-1640-8c7671e235.png)": "![Oracle Database multitenancy: CDBs](https://dt-cdn.net/images/cbds-1640-8c7671e235.png)",
    "Oracle Database multitenancy: CDBs": "Oracle Database multitenancy: CDBs",
    "4. On the **CDB** page, select a pluggable database.": "4. На странице **CDB** выберите подключаемую базу данных.",
    "![Oracle Database multitenancy: Pluggable databases](https://dt-cdn.net/images/pluggable-databases-1611-2ce2521bef.png)": "![Oracle Database multitenancy: Pluggable databases](https://dt-cdn.net/images/pluggable-databases-1611-2ce2521bef.png)",
    "Oracle Database multitenancy: Pluggable databases": "Oracle Database multitenancy: Pluggable databases",
    "5. The **PDB** page lists services.": "5. На странице **PDB** отображается список сервисов.",
    "![Oracle Database multitenancy: Services](https://dt-cdn.net/images/services-1621-d3ca42e060.png)": "![Oracle Database multitenancy: Services](https://dt-cdn.net/images/services-1621-d3ca42e060.png)",
    "Oracle Database multitenancy: Services": "Oracle Database multitenancy: Services",
    # --- ## Heavy query timeout ---
    "## Heavy query timeout": "## Тайм-аут тяжёлого запроса",
    "ActiveGate version 1.275+": "ActiveGate версии 1.275+",
    "Add the `long-running-query-timeout` parameter to configure the timeout duration for long-running SQL queries. This parameter is optional, and if not set, the default timeout of 10 seconds is applied.": "Добавьте параметр `long-running-query-timeout` для настройки тайм-аута длительных SQL-запросов. Параметр необязателен; если он не задан, применяется тайм-аут по умолчанию в 10 секунд.",
    # --- ## SSL ---
    "## SSL": "## SSL",
    "ActiveGate version 1.251+": "ActiveGate версии 1.251+",
    "Enable SSL to force the data source to verify the server certificate and use SSL encryption instead of native encryption.": "Включите SSL, чтобы источник данных проверял сертификат сервера и использовал шифрование SSL вместо встроенного.",
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
    "ActiveGate version 1.269+": "ActiveGate версии 1.269+",
    "The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.": "Сертификат дополнительно проверяется по имени хоста: домен из сертификата должен совпадать с доменом эндпоинта, указанного в конфигурации мониторинга.",
    "Enable this option when connecting to databases using custom certificates.": "Включите этот параметр при подключении к базам данных с использованием пользовательских сертификатов.",
    "Client certificates are not supported for SQL data sources. To authenticate securely, use basic authentication with SSL enabled. For details, see [Authentication](#authentication).": "Клиентские сертификаты не поддерживаются для источников данных SQL. Для безопасной аутентификации используйте базовую аутентификацию с включённым SSL. Подробные сведения см. в разделе [Аутентификация](#authentication).",
    # --- ## Resource consumption ---
    "## Resource consumption": "## Потребление ресурсов",
    "Resource consumption depends on the number of Oracle endpoints. The first endpoint consumes 110 MB of RAM and 0.1%–0.5% of CPU. Every following endpoint consumes 0.5–1.0 MB of RAM and ~0.01% of CPU.": "Потребление ресурсов зависит от числа эндпоинтов Oracle. Первый эндпоинт потребляет 110 МБ ОЗУ и 0,1–0,5% ЦП. Каждый следующий эндпоинт потребляет 0,5–1,0 МБ ОЗУ и ~0,01% ЦП.",
    "| Endpoints | Average CPU | Max CPU | RAM (MB) | Host (EC2 instance type) |": "| Эндпоинты | Среднее ЦП | Макс. ЦП | ОЗУ (МБ) | Хост (тип EC2) |",
    "| --- | --- | --- | --- | --- |": "| --- | --- | --- | --- | --- |",
    "| 100 | 0.6% | 0.6% (spike at beginning) | 160 | XS (`c5.large`) |": "| 100 | 0,6% | 0,6% (всплеск в начале) | 160 | XS (`c5.large`) |",
    "| 1 | 0.1% | 0.5% (spike at beginning) | 110 | XS (`c5.large`) |": "| 1 | 0,1% | 0,5% (всплеск в начале) | 110 | XS (`c5.large`) |",
    # --- SHARED lines that appear in oracle but not as ### headings ---
    "Replace `<ActiveGate-group-name>` with the actual name.": "Замените `<ActiveGate-group-name>` фактическим именем.",
}

if __name__ == "__main__":
    build_one(REL, "oracle-monitoring.md", TRANS)
    qa_one(REL, "oracle-monitoring.md")
