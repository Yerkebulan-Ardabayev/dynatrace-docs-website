# -*- coding: utf-8 -*-
"""Builder for customize-zremote.md (L4-IF.71 canon).

Source (EN): docs/managed/ingest-from/dynatrace-oneagent/installation-and-operation/
             zos/installation/install-zremote/customize-zremote.md
Target (RU): docs/managed-ru/...  (same relative path)

Mojibake notes in EN source (scraping artifacts -- engine _demoji cleans them;
write CLEAN EN keys):
  U+00D7 MULTIPLICATION SIGN 'x': scraper emitted 'Ã' (e.g. 'percentage limit x available')
  U+2014 EM DASH '--': scraper emitted 'a' then backtick (line 96 'LPARsa`LPARA`')
  U+2019 RIGHT SINGLE QUOTE "'": scraper emitted 'a' (e.g. 'wea've')
  U+FEFF BOM: scraper appended to some URLs (e.g. '[Linux﻿](...)')
All of these are normalised by _demoji before lookup; keys use the clean form.
"""

import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote"
FN = "customize-zremote.md"

TRANS = {
    # --- frontmatter ---
    "title: Customize the zRemote module": "title: Настройка модуля zRemote",
    # --- h1 (appears twice) ---
    "# Customize the zRemote module": "# Настройка модуля zRemote",
    # --- metadata ---
    "* 9-min read": "* Чтение: 9 мин",
    "* Updated on Aug 11, 2022": "* Обновлено 11 августа 2022 г.",
    # --- intro ---
    "You can customize the zRemote module to enable optional features and optimize its performance.": "Модуль zRemote можно настроить для включения необязательных функций и оптимизации его производительности.",
    # --- ## User configuration files ---
    "## User configuration files": "## Файлы пользовательской конфигурации",
    "The following configuration files are retained in the event of a zRemote update or uninstallation. You can make changes here.": "Перечисленные ниже файлы конфигурации сохраняются при обновлении или удалении zRemote. Здесь можно вносить изменения.",
    "You must restart the zRemote service to apply new settings.": "Для применения новых настроек необходимо перезапустить службу zRemote.",
    # --- ### zRemote module user configuration ---
    "### zRemote module user configuration": "### Пользовательская конфигурация модуля zRemote",
    "The zRemote module user configuration file (`zremoteagentuserconfig.conf`) allows you to override the default configuration defined in `ruxitagent.conf`.": "Файл пользовательской конфигурации модуля zRemote (`zremoteagentuserconfig.conf`) позволяет переопределить настройки по умолчанию, заданные в `ruxitagent.conf`.",
    "Linux": "Linux",
    "Windows": "Windows",
    "`/var/lib/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`": "`/var/lib/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`",
    "`C:/ProgramData/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`": "`C:/ProgramData/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`",
    # --- ### Watchdog user configuration ---
    "### Watchdog user configuration": "### Пользовательская конфигурация watchdog",
    "Dynatrace version 1.277+ The watchdog user configuration file (`watchdoguserconfig.conf`) allows you to override the default configuration defined in `oneagentzwatchdog.ini`.": "Dynatrace версии 1.277+ Файл пользовательской конфигурации watchdog (`watchdoguserconfig.conf`) позволяет переопределить настройки по умолчанию, заданные в `oneagentzwatchdog.ini`.",
    "`/var/lib/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`": "`/var/lib/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`",
    "`C:/ProgramData/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`": "`C:/ProgramData/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`",
    "Available parameters for configuration:": "Доступные параметры конфигурации:",
    "| Parameter | Unit | Default value | Description |": "| Параметр | Единица | Значение по умолчанию | Описание |",
    "| --- | --- | --- | --- |": "| --- | --- | --- | --- |",
    "| -healthcheck.heartbeat.timeout | Seconds | 900 | The connection timeout between the zRemote service and your Dynatrace environment |": "| -healthcheck.heartbeat.timeout | Секунды | 900 | Таймаут соединения между службой zRemote и вашим окружением Dynatrace |",
    "| -healthcheck.memory.limit\\_absolute | MiB | 500 | Absolute input for the memory calculation limit of the child process |": "| -healthcheck.memory.limit\\_absolute | МиБ | 500 | Абсолютное значение для расчёта лимита памяти дочернего процесса |",
    "| -healthcheck.memory.limit\\_percentage | % | 20 | Percentage input for the memory calculation limit of the child process |": "| -healthcheck.memory.limit\\_percentage | % | 20 | Процентное значение для расчёта лимита памяти дочернего процесса |",
    # Callout: Effective memory limit calculation
    # EN source line 54: "Effective memory limit calculation" (callout title)
    # EN source line 56: "Effective limit = percentage limit × available physical memory on the system + absolute limit"
    # EN source line 58: "For example:"
    # EN source line 60: "0.2 × 5 GiB + 500 MiB = 1.5 GiB effective memory limit"
    # The 'Ã' in the EN file is mojibake for '×'; _demoji converts to '×'; keys use clean form.
    "Effective memory limit calculation": "Расчёт эффективного лимита памяти",
    "Effective limit = percentage limit × available physical memory on the system + absolute limit": "Эффективный лимит = процентный лимит × доступная физическая память системы + абсолютный лимит",
    "For example:": "Например:",
    "0.2 × 5 GiB + 500 MiB = 1.5 GiB effective memory limit": "0.2 × 5 ГиБ + 500 МиБ = 1,5 ГиБ эффективный лимит памяти",
    # --- ## Organize LPARs with host groups ---
    "## Organize LPARs with host groups": "## Организация LPAR с помощью Host groups",
    "Host groups are helpful when you want to organize multiple LPARs connecting to a single zRemote module. An LPAR can be assigned to a host group by setting the `[HostGroup]` attribute in the `zremoteagentuserconfig.conf` file. An LPAR can belong to only one host group.": "**Host groups** полезны, когда нужно организовать несколько LPAR, подключённых к одному модулю zRemote. Чтобы назначить LPAR в Host group, задайте атрибут `[HostGroup]` в файле `zremoteagentuserconfig.conf`. LPAR может принадлежать только одной Host group.",
    "To assign an LPAR to a host group, specify the group name in between a pair of `[HostGroup]` attributes. The `[HostGroup]` attribute pair can occur anywhere in the `zremoteagentuserconfig.conf` file.": "Чтобы назначить LPAR в Host group, укажите имя группы между парой атрибутов `[HostGroup]`. Пара атрибутов `[HostGroup]` может располагаться в любом месте файла `zremoteagentuserconfig.conf`.",
    "The LPAR name is the 8 characters logical partition name defined in the `LPARNAME()` parameter in `IEASYMxx` member in z/OS.": "Имя LPAR -- это 8-символьное имя логического раздела, заданное в параметре `LPARNAME()` в элементе `IEASYMxx` в z/OS.",
    "The LPAR name is also displayed in the `Properties and tags` section on the host screen.": "Имя LPAR также отображается в разделе `Properties and tags` на экране хоста.",
    "The following requirements apply to the `<HostGroupName>` string:": "К строке `<HostGroupName>` применяются следующие требования:",
    "* Can contain only alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`)": "* Допустимы только буквенно-цифровые символы, дефисы (`-`), символы подчёркивания (`_`) и точки (`.`)",
    "* Must not start with `dt.`": "* Строка не должна начинаться с `dt.`",
    "* Maximum length is 100 characters": "* Максимальная длина: 100 символов",
    # Callout: Combining three LPARs to a single host group
    # EN line 94: "Combining three LPARs to a single host group" (callout title)
    # EN line 96: "In this example, we add three LPARs—`LPARA`, `LPARB`, and `LPARC` to a single host group `TEST_HOST`."
    # The 'â' before backtick is mojibake for '—'; _demoji converts; key uses clean em-dash form (U+2014).
    "Combining three LPARs to a single host group": "Объединение трёх LPAR в одну Host group",
    "In this example, we add three LPARs—`LPARA`, `LPARB`, and `LPARC` to a single host group `TEST_HOST`.": "В данном примере три LPAR (`LPARA`, `LPARB` и `LPARC`) добавляются в одну Host group `TEST_HOST`.",
    # Callout: Assigning three LPARs to different host groups
    "Assigning three LPARs to different host groups": "Назначение трёх LPAR в разные Host groups",
    "In this example we assign each LPAR to a separate host group.": "В данном примере каждая LPAR назначается в отдельную Host group.",
    # bullet notes after the code block
    "* In host settings, only the **General**, **Monitoring**, and **Detected processes** menus are applicable for a z/OS host group.": "* В настройках хоста для Host group z/OS применяются только меню **General**, **Monitoring** и **Detected processes**.",
    "* Store your host group settings only in the `zremoteagentuserconfig.conf` file and migrate your host group settings from the `ruxitagent.conf` file.": "* Храните настройки Host group только в файле `zremoteagentuserconfig.conf` и перенесите настройки Host group из файла `ruxitagent.conf`.",
    "* Host group settings take effect during zRemote start up. You must restart the zRemote module after defining host group in the `zremoteagentuserconfig.conf` file.": "* Настройки Host group вступают в силу при запуске zRemote. После определения Host group в файле `zremoteagentuserconfig.conf` необходимо перезапустить модуль zRemote.",
    # --- ## Fetch full SQL statements from Db2 databases ---
    "## Fetch full SQL statements from Db2 databases": "## Получение полных SQL-запросов из баз данных Db2",
    "Dynatrace can provide insight into SQL statements based on tracing of Db2 and DL/I database calls. These SQL statements are shown in Dynatrace, for example, as:": "Dynatrace предоставляет аналитику по SQL-запросам на основе трассировки обращений к базам данных Db2 и DL/I. Эти SQL-запросы отображаются в Dynatrace, например, в следующем виде:",
    "* **FETCH (PROGNAME;165;3)**": "* **FETCH (PROGNAME;165;3)**",
    "* **CLOSE (PROGNAME;441;2)**": "* **CLOSE (PROGNAME;441;2)**",
    "The string represents the program name (DBRM name), the line number, and the section number.": "Строка содержит имя программы (имя DBRM), номер строки и номер секции.",
    "Example for captured SQL statements": "Пример перехваченных SQL-запросов",
    "![zRemote SQL statement fetch off](https://dt-cdn.net/images/zremote-sql-fetch-off-1600-5beae13988.png)": "![zRemote SQL statement fetch off](https://dt-cdn.net/images/zremote-sql-fetch-off-1600-5beae13988.png)",
    "zRemote SQL statement fetch off": "zRemote SQL statement fetch off",
    "zRemote module version 1.241+ Dynatrace can provide deeper insight into Db2 database calls by fetching the full SQL statements from the Db2 catalog. With the **SQL statement fetch** feature enabled, the SQL statements are shown in Dynatrace, for example, as:": "Версия модуля zRemote 1.241+ Dynatrace предоставляет более глубокую аналитику по обращениям к базам данных Db2, получая полные SQL-запросы из каталога Db2. При включённой функции **SQL statement fetch** SQL-запросы отображаются в Dynatrace, например, в следующем виде:",
    "* **FETCH (GETTAB INTO : H , : H , : H , : H , : H)**": "* **FETCH (GETTAB INTO : H , : H , : H , : H , : H)**",
    "* **CLOSE (GETTAB)**": "* **CLOSE (GETTAB)**",
    "Example for captured SQL statements with enabled SQL statement fetch feature": "Пример перехваченных SQL-запросов с включённой функцией SQL statement fetch",
    "![zRemote SQL statement fetch on](https://dt-cdn.net/images/zremote-sql-fetch-on-1602-ff3d0f1c32.png)": "![zRemote SQL statement fetch on](https://dt-cdn.net/images/zremote-sql-fetch-on-1602-ff3d0f1c32.png)",
    "zRemote SQL statement fetch on": "zRemote SQL statement fetch on",
    # --- ### Enable SQL statement fetch ---
    "### Enable SQL statement fetch": "### Включение функции SQL statement fetch",
    "The **SQL statement fetch** feature is disabled by default. To enable it": "Функция **SQL statement fetch** отключена по умолчанию. Чтобы включить её:",
    # Step 1
    # EN line 176: link text "Linux﻿" and "Windows﻿" -- BOM is cleaned by _demoji
    "1. Install and configure the IBM Data Server Driver for ODBC and CLI software on [Linux﻿](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-linux-unix-operating-systems) or [Windows﻿](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-windows-operating-systems). Further reading: [IBM Db2 ODBC CLI driver Download and Installation information﻿](https://www.ibm.com/support/pages/db2-odbc-cli-driver-download-and-installation-information).": "1. Установите и настройте IBM Data Server Driver for ODBC and CLI на [Linux](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-linux-unix-operating-systems) или [Windows](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-windows-operating-systems). Дополнительно: [Информация по скачиванию и установке IBM Db2 ODBC CLI driver](https://www.ibm.com/support/pages/db2-odbc-cli-driver-download-and-installation-information).",
    "In the installation step take note of the location of the CLI driver library:": "На шаге установки запомните расположение библиотеки CLI driver:",
    "* `libdb2.so` for Linux": "* `libdb2.so` для Linux",
    "* `db2app64.dll` for Windows": "* `db2app64.dll` для Windows",
    "Before configuring the driver, it might be necessary to contact the DBA requesting the database connectivity information (such as database credentials, location, and IP and port). In the configuration step, take note of the Db2 aliases (or DSN).": "Перед настройкой driver может потребоваться обратиться к DBA для получения сведений о подключении к базе данных (учётных данных, местоположения, IP-адреса и порта). На шаге настройки запомните псевдонимы Db2 (или DSN).",
    "Both are required in the next steps.": "Оба значения потребуются в следующих шагах.",
    "* The zRemote module supports only 64-bit CLI driver.": "* Модуль zRemote поддерживает только 64-битный CLI driver.",
    "* We strongly recommend that you set the connection timeout for every DB alias, for example, ConnectTimeout=2": "* Настоятельно рекомендуем задавать таймаут соединения для каждого псевдонима БД, например ConnectTimeout=2",
    "for two seconds in db2cli.ini on Linux": "для двух секунд в db2cli.ini на Linux",
    "* Be sure to test the CLI driver configuration to ensure good Db2 connections, for example:": "* Обязательно протестируйте конфигурацию CLI driver для проверки подключения к Db2, например:",
    "* To configure the CLI driver, you need Db2 credentials that grant access to Db2 connections (from distributed using DDF/DRDA) and grants to select on CATALOG, specifically on SYSPACKSTMT.": "* Для настройки CLI driver необходимы учётные данные Db2 с доступом к соединениям Db2 (из распределённой среды через DDF/DRDA) и правами на SELECT по CATALOG, в частности по SYSPACKSTMT.",
    # Step 2
    "2. In the `zremoteagentuserconfig.conf` file of the zRemote module, define the CLI driver library and Db2 alias group (similar as defining host groups), for example:": "2. В файле `zremoteagentuserconfig.conf` модуля zRemote задайте библиотеку CLI driver и группу псевдонимов Db2 (аналогично определению Host groups), например:",
    "where `dbHost` is the z/OS SMF ID and `dbName` is the Db2 subsystem name. All is case sensitive.": "где `dbHost` -- это SMF ID системы z/OS, а `dbName` -- имя подсистемы Db2. Все значения чувствительны к регистру.",
    # Step 3
    "3. Optional Define `sqlStmtCacheFileName=/tmp/sqlStmtCacheFileName`, as an example, to cache the fetched SQL statements to a file and use it upon a zRemote module restart, thus reducing Db2 interactions. Be sure to use the appropriate fully qualified file name.": "3. Необязательно Задайте, например, `sqlStmtCacheFileName=/tmp/sqlStmtCacheFileName`, чтобы кэшировать полученные SQL-запросы в файл и использовать этот кэш при перезапуске модуля zRemote, сокращая тем самым число обращений к Db2. Обязательно используйте полное квалифицированное имя файла.",
    # Step 4
    "4. Restart the zRemote module.": "4. Перезапустите модуль zRemote.",
    "* The zRemote module will only enable the **SQL statement fetch** feature if the CLI driver can be loaded successfully and there is at least one DB2 alias defined.": "* Модуль zRemote включит функцию **SQL statement fetch** только в том случае, если CLI driver успешно загружен и определён хотя бы один псевдоним DB2.",
    "* If the Db2 alias is later found to be invalid, the feature is disabled.": "* Если псевдоним Db2 впоследствии окажется недействительным, функция будет отключена.",
    # --- ## Enable secure zLocal-zRemote connection ---
    "## Enable secure zLocal-zRemote connection": "## Включение защищённого соединения zLocal-zRemote",
    "zRemote module version 1.267+": "Версия модуля zRemote 1.267+",
    "By default, the zLocal and zRemote use a proprietary communication protocol via plain sockets. You can configure them to communicate via TLS by configuring AT-TLS for the zLocal and setting the SSL flags for the zRemote as shown below.": "По умолчанию zLocal и zRemote используют собственный протокол обмена данными через обычные сокеты. Их можно настроить на обмен данными через TLS: для этого задайте AT-TLS для zLocal и установите флаги SSL для zRemote, как показано ниже.",
    # --- ### AT-TLS configuration for the zLocal ---
    "### AT-TLS configuration for the zLocal": "### Конфигурация AT-TLS для zLocal",
    "Depending on your requirements, there are different ways to configure AT-TLS for zLocal. For more details, refer to [Application Transparent Transport Layer Security data protection﻿](https://www.ibm.com/docs/en/zos/2.5.0?topic=applications-application-transparent-transport-layer-security-data-protection) in IBM documentation. You can use the example AT-TLS configuration below as a template.": "В зависимости от требований существуют различные способы настройки AT-TLS для zLocal. Подробнее см. раздел [Application Transparent Transport Layer Security data protection](https://www.ibm.com/docs/en/zos/2.5.0?topic=applications-application-transparent-transport-layer-security-data-protection) в документации IBM. Приведённый ниже пример конфигурации AT-TLS можно использовать как шаблон.",
    "Example of an AT-TLS configuration": "Пример конфигурации AT-TLS",
    "Be sure the userId used in the zDC job is the same one that owns the certificate.": "Убедитесь, что userId, используемый в задаче zDC, совпадает с владельцем сертификата.",
    "Otherwise, the connection to the TSL handshake will fail (with SSL accept error -1 and code 5).": "В противном случае установление TLS-соединения завершится ошибкой (SSL accept error -1, код 5).",
    # --- ### SSL/TLS settings for the zRemote ---
    "### SSL/TLS settings for the zRemote": "### Настройки SSL/TLS для zRemote",
    "To enable SSL/TLS for the zRemote": "Чтобы включить SSL/TLS для zRemote:",
    "1. Open the `zremoteagentuserconfig.conf` file.": "1. Откройте файл `zremoteagentuserconfig.conf`.",
    "2. Set `sslEnabled` to `true`.": "2. Установите `sslEnabled` в значение `true`.",
    "3. Specify the absolute paths to your private key (`sslPrivateKey`) and certificate (`sslCertificate`) PEM files.": "3. Укажите абсолютные пути к файлам PEM вашего закрытого ключа (`sslPrivateKey`) и сертификата (`sslCertificate`).",
    "4. Optional Define specific TLS cipher suites. For information about allowed cipher suite names and their string format, refer to [OpenSSL documentation﻿](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).": "4. Необязательно Определите конкретные наборы шифров TLS. Сведения о допустимых именах наборов шифров и их строковом формате см. в [документации OpenSSL](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).",
    "Show configuration template": "Показать шаблон конфигурации",
    # --- ## Ignore invalid connection attempts ---
    "## Ignore invalid connection attempts": "## Игнорирование недействительных попыток подключения",
    "If a specific process regularly pings the zRemote module to detect its availability, and these pings reach the zRemote listener port, the zRemote module logs an invalid connection attempt. These invalid connection attempts increase the zRemote log size over time.": "Если определённый процесс регулярно отправляет ping-запросы модулю zRemote для проверки его доступности и эти запросы достигают порта прослушивания zRemote, модуль zRemote фиксирует недействительную попытку подключения. Со временем такие попытки увеличивают размер лога zRemote.",
    "To ignore connection attempts from specific processes, list their IP addresses (separated by semicolons) in the `zremoteagentuserconfig.conf` file, for example:": "Чтобы игнорировать попытки подключения от определённых процессов, перечислите их IP-адреса (через точку с запятой) в файле `zremoteagentuserconfig.conf`, например:",
    # --- ## Opt out of new IMS MPR process ID calculation ---
    "## Opt out of new IMS MPR process ID calculation": "## Отказ от нового расчёта идентификаторов процессов IMS MPR",
    "zRemote module version 1.253+": "Версия модуля zRemote 1.253+",
    # EN line 549: "we've" rendered as "wea\x80\x99ve" in scrape; _demoji fixes U+2019 -> "'"; key uses clean form
    "The IMS message processing region (MPR) process IDs could change, resulting in new process and service entities in Dynatrace. To prevent this process ID change, we’ve introduced a more stable ID calculation with the consequence that all IMS MPR process and service entities will change once but then remain stable after an update of the zRemote module with version 1.253.": "Идентификаторы процессов региона обработки сообщений IMS (MPR) могут изменяться, что приводит к появлению новых сущностей процессов и служб в Dynatrace. Чтобы исключить такое изменение идентификаторов, введён более стабильный алгоритм расчёта: все сущности процессов и служб IMS MPR изменятся один раз, после чего останутся стабильными после обновления модуля zRemote до версии 1.253.",
    "To opt out of the new IMS MPR process ID calculation, set the flag `useOldImsPgiCalc` in the `zremoteagentuserconfig.conf` file to `true`.": "Чтобы отказаться от нового алгоритма расчёта идентификаторов процессов IMS MPR, задайте флагу `useOldImsPgiCalc` значение `true` в файле `zremoteagentuserconfig.conf`.",
}

# Lines that must remain verbatim EN (config param names, paths, code-only labels)
PASS = set()

if __name__ == "__main__":
    build_one(REL, FN, TRANS, PASS)
    qa_one(REL, FN)
