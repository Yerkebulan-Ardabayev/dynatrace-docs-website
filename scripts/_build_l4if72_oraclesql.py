# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/supported-extensions/data-sources/sql"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Published Apr 11, 2022": "* Опубликовано 11 апреля 2022 г.",
    "Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Oracle Database layer, so that you can monitor how database server tasks impact your app.": "Dynatrace предоставляет платформу для расширения наблюдаемости приложений за счёт данных, получаемых непосредственно с уровня Oracle Database, что позволяет отслеживать влияние задач сервера баз данных на приложение.",
    'To get started, check [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=oracle+sql) to see if the Dynatrace-provided Oracle Database extension satisfies your requirements. If this is not the case, you can build your own [Dynatrace Oracle Database extension](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Learn how to create an SQL data source-based extension using the Extensions framework.").': 'Для начала проверьте в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=oracle+sql), соответствует ли предоставляемое Dynatrace расширение Oracle Database вашим требованиям. Если нет, создайте собственное [расширение Dynatrace Oracle Database](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql "Узнайте, как создать расширение на основе источника данных SQL с помощью платформы Extensions framework.").',
    "## Before you begin": "## Перед началом работы",
    "1. Decide which Oracle Database server you want to monitor. The Oracle Database extension supports Oracle Database versions 12.2+ with the following setups:": "1. Определите, какой сервер Oracle Database нужно отслеживать. Расширение Oracle Database поддерживает Oracle Database версии 12.2+ со следующими конфигурациями:",
    "* Oracle standalone servers": "* Автономные серверы Oracle",
    "* Oracle Multitenant (CDB/PDB)": "* Oracle Multitenant (CDB/PDB)",
    "* Oracle RAC": "* Oracle RAC",
    "* Oracle AWS RDS": "* Oracle AWS RDS",
    "2. Designate an ActiveGate group or groups that will remotely connect to your Oracle Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Oracle Database server.": "2. Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к серверу Oracle Database для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключаться к серверу Oracle Database.",
    "3. Create a dedicated user account for monitoring and grant it permissions as in the [Oracle Databaseï»¿](https://dt-url.net/7f03qwp) extension description under the **Get started with Oracle Database servers** section.": "3. Создайте выделенную учётную запись для мониторинга и предоставьте ей разрешения согласно описанию расширения [Oracle Database](https://dt-url.net/7f03qwp) в разделе **Get started with Oracle Database servers**.",
    "## Manage Oracle SQL extensions": "## Управление расширениями Oracle SQL",
    "Dynatrace Hub provides a unified workflow to enable and manage extensions that will ingest Oracle Database data into your Dynatrace environment.": "Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими с целью приёма данных Oracle Database в среду Dynatrace.",
    "Required permission: **Change monitoring settings**": "Необходимое разрешение: **Change monitoring settings**",
    '1. In Dynatrace Hub, select and install the **Oracle Database** extension. (You can use "Oracle SQL" to filter search results.) This enables the extension in your environment.': '1. В Dynatrace Hub выберите и установите расширение **Oracle Database**. (Для фильтрации результатов поиска используйте "Oracle SQL".) Это включает расширение в среде.',
    "2. Add a monitoring configuration so that the extension can begin collecting data.": "2. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.",
    "Next, perform the following steps.": "Затем выполните следующие шаги.",
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    '**Accept Oracle JDBC driver redistribution license**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-1 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': '**Принятие лицензии на распространение драйвера Oracle JDBC**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-1 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    '**Define endpoints**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-2 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': '**Определение эндпоинтов**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-2 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
    '**ActiveGate group**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-3 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")': '**Группа ActiveGate**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-3 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")',
    '**Activate extension**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-4 "Learn how to extend observability in Dynatrace with declarative metrics ingested from Oracle Database.")': '**Активация расширения**](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql#step-4 "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Oracle Database.")',
    "### Step 1 Accept Oracle JDBC driver redistribution license": "### Шаг 1. Принятие лицензии на распространение драйвера Oracle JDBC",
    "An Oracle Database extension requires that you accept the [Dynatrace redistribution license agreement for Oracle JDBC Driverï»¿](https://dt-url.net/0s1n0pw9).": "Расширение Oracle Database требует принятия [лицензионного соглашения Dynatrace на распространение драйвера Oracle JDBC](https://dt-url.net/0s1n0pw9).",
    "### Step 2 Define endpoints": "### Шаг 2. Определение эндпоинтов",
    "Select **Add Oracle endpoint** to define the Oracle Database servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:": "Нажмите **Add Oracle endpoint**, чтобы определить серверы Oracle Database, с которых нужно получать данные. Можно определить до 100 эндпоинтов. Укажите следующие сведения для подключения:",
    "* Host": "* Хост",
    "* Port": "* Порт",
    "* Database identifier, either **Service Name** or **SID**.": "* Идентификатор базы данных: **Service Name** или **SID**.",
    "* Authentication credentials. Note that only basic authentication is supported. Authentication details passed to Dynatrace when activating monitoring configuration are obfuscated and it's impossible to retrieve them.": "* Учётные данные аутентификации. Поддерживается только базовая аутентификация. Данные аутентификации, передаваемые в Dynatrace при активации конфигурации мониторинга, скрываются и не могут быть получены.",
    '+ You can [use credential vault](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring#credential-vault "Create and activate a monitoring configuration for an SQL data source based extension for Oracle Database.") to provide a more secure approach of storing and managing user credentials.': '+ Для более безопасного хранения учётных данных пользователя и управления ими можно [использовать хранилище учётных данных](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring#credential-vault "Создайте и активируйте конфигурацию мониторинга для расширения на основе источника данных SQL для Oracle Database.").',
    "When done, select **Next step**": "После этого нажмите **Next step**.",
    "### Step 3 ActiveGate group": "### Шаг 3. Группа ActiveGate",
    "Select the ActiveGate group to determine which ActiveGates will run the extension. When done, select **Next step**.": "Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение. После этого нажмите **Next step**.",
    "### Step 4 Activate extension": "### Шаг 4. Активация расширения",
    "Provide final configuration details.": "Укажите финальные сведения о конфигурации.",
    "* **Description**": "* **Description**  ",
    "Text explaining details of this particular monitoring configuration. When troubleshooting monitoring, this can give your teams details of this particular monitoring configuration.": "Текст с описанием данной конфигурации мониторинга. При устранении неполадок он поможет вашей команде получить подробные сведения о конкретной конфигурации.",
    "* **Feature sets**": "* **Feature sets**  ",
    "In highly segmented networks, feature sets can reflect the segments of your environment. You can use them to limit your monitoring to particular segments. Feature sets are predefined for each extension.": "В сильно сегментированных сетях наборы функций могут отражать сегменты среды. Их можно использовать для ограничения мониторинга определёнными сегментами. Наборы функций предопределены для каждого расширения.",
    "When done, select **Activate**.": "После этого нажмите **Activate**.",
    "## Monitoring configuration as JSON": "## Конфигурация мониторинга в формате JSON",
    'The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. See [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") to learn how to use it to activate an extension using the Dynatrace API.': 'Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. О том, как использовать их для активации расширения через Dynatrace API, см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.").',
    "## Related topics": "## Связанные разделы",
    '* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")': '* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")',
}

PASS = {
    "title: Manage Oracle Database extensions",
    "source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql",
    "scraped: 2026-05-12T11:10:30.584363",
    "# Manage Oracle Database extensions",
}

if __name__ == "__main__":
    build_one(REL, "oraclesql.md", TRANS, PASS)
    qa_one(REL, "oraclesql.md")
