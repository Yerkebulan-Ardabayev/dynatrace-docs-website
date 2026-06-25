# -*- coding: utf-8 -*-
"""L4-IF.72 — ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/extensions/supported-extensions/data-sources/sql"

TRANS = {
    "* How-to guide": "* Практическое руководство",
    "* 2-min read": "* Чтение: 2 мин",
    "* Published Sep 05, 2022": "* Опубликовано 5 сентября 2022 г.",
    "Dynatrace provides you with a framework that you can use to extend your application observability into data acquired directly from your Microsoft SQL Database layer, so that you can monitor how database server tasks impact your app.": "Dynatrace предоставляет платформу для расширения наблюдаемости приложений за счёт данных, получаемых непосредственно с уровня Microsoft SQL Database, что позволяет отслеживать влияние задач сервера баз данных на приложение.",
    'Start by checking [Dynatrace Hubï»¿](https://www.dynatrace.com/hub/?query=microsoft+sql) to see if the Dynatrace-provided Microsoft SQL Server extension satisfies your requirements. If you need something different, you can build your own [Microsoft SQL Server extension](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Learn how to create an SQL data source-based extension using the Extensions framework.").': 'Для начала проверьте в [Dynatrace Hub](https://www.dynatrace.com/hub/?query=microsoft+sql), соответствует ли предоставляемое Dynatrace расширение Microsoft SQL Server вашим требованиям. Если нет, создайте собственное [расширение Microsoft SQL Server](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql#microsoft-sql-monitoring "Узнайте, как создать расширение на основе источника данных SQL с помощью платформы Extensions framework.").',
    "## Before you begin": "## Перед началом работы",
    "Designate an ActiveGate group or groups that will remotely connect to your Microsoft SQL Database server to pull data. All ActiveGates in each designated group need to be able to connect to your Microsoft SQL Database server.": "Назначьте группу или группы ActiveGate, которые будут удалённо подключаться к серверу Microsoft SQL Database для получения данных. Все ActiveGate в каждой назначенной группе должны иметь возможность подключаться к серверу Microsoft SQL Database.",
    "## Manage Microsoft SQL extensions": "## Управление расширениями Microsoft SQL",
    "Dynatrace Hub provides a unified workflow to enable and manage extensions that ingest Microsoft SQL Server data into your Dynatrace environment.": "Dynatrace Hub предоставляет единый рабочий процесс для включения расширений и управления ими с целью приёма данных Microsoft SQL Server в среду Dynatrace.",
    "Required permission: **Change monitoring settings**": "Необходимое разрешение: **Change monitoring settings**",
    "1. In Dynatrace Hub, select and install the **Microsoft SQL Server** extension. This enables the extension in your environment.": "1. В Dynatrace Hub выберите и установите расширение **Microsoft SQL Server**. Это включает расширение в среде.",
    "2. Add a monitoring configuration so that the extension can begin collecting data.": "2. Добавьте конфигурацию мониторинга, чтобы расширение начало сбор данных.",
    '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': '[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    'Define endpoints](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': 'Определение эндпоинтов](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#define-endpoints "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Microsoft SQL Server.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    'Select ActiveGates](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': 'Выбор ActiveGates](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activegate-group "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Microsoft SQL Server.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
    'Activate the extension](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Extend observability in Dynatrace with declarative metrics ingested from Microsoft SQL Server.")': 'Активация расширения](/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql#activate-extension "Расширьте наблюдаемость в Dynatrace с помощью декларативных метрик, поступающих из Microsoft SQL Server.")',
    "### Step 1 Define endpoints": "### Шаг 1. Определение эндпоинтов",
    "1. Select **Add Sql Server endpoint** to define the servers from which you want to pull data. You can define up to 100 endpoints. Provide the following connection details:": "1. Нажмите **Add Sql Server endpoint**, чтобы определить серверы, с которых нужно получать данные. Можно определить до 100 эндпоинтов. Укажите следующие сведения для подключения:",
    "* Host": "* Хост",
    "* Optional Port": "* Порт (необязательно)",
    "* Optional Instance name": "* Имя экземпляра (необязательно)",
    "* Optional Database name": "* Имя базы данных (необязательно)",
    '* Authentication scheme. You can choose from the following [authentication schemes](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Microsoft SQL extensions in the Extensions framework."):': '* Схема аутентификации. Доступны следующие [схемы аутентификации](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#authentication "Расширения Microsoft SQL в платформе Extensions framework."):',
    "+ Basic authentication": "+ Базовая аутентификация",
    "+ Kerberos authentication": "+ Аутентификация Kerberos",
    "+ NTLM authentication": "+ Аутентификация NTLM",
    '* You can [enable SSL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Microsoft SQL extensions in the Extensions framework.") to establish a secure connection for your configuration.': '* Для установки защищённого соединения в конфигурации можно [включить SSL](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#ssl "Расширения Microsoft SQL в платформе Extensions framework.").',
    '* You can [use credential vault](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Microsoft SQL extensions in the Extensions framework.") to provide a more secure approach of storing and managing user credentials.': '* Для более безопасного хранения учётных данных пользователя и управления ими можно [использовать хранилище учётных данных](/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring#credential-vault "Расширения Microsoft SQL в платформе Extensions framework.").',
    "2. Select **Next step**.": "2. Нажмите **Next step**.",
    "### Step 2 Select ActiveGates": "### Шаг 2. Выбор ActiveGates",
    "1. Select the ActiveGate group to determine which ActiveGates will run the extension.": "1. Выберите группу ActiveGate, чтобы определить, какие ActiveGate будут запускать расширение.",
    "### Step 3 Activate the extension": "### Шаг 3. Активация расширения",
    "1. Give your monitoring configuration a distinctive label in **Description**.": "1. Укажите отличительную метку конфигурации мониторинга в поле **Description**.",
    "2. Select **Activate**.": "2. Нажмите **Activate**.",
    "## Monitoring configuration as JSON": "## Конфигурация мониторинга в формате JSON",
    'The extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration. To learn how to use it to activate an extension using the Dynatrace API, see [Unavailable in Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").': 'Мастер активации расширения содержит динамически обновляемые JSON-данные с конфигурацией мониторинга. О том, как использовать их для активации расширения через Dynatrace API, см. в разделе [Недоступно в Dynatrace Managed](/managed/upgrade/unavailable-in-managed "Выбранная функция недоступна в Dynatrace Managed.").',
    "## Related topics": "## Связанные разделы",
    '* [Troubleshooting extensionsï»¿](https://dt-url.net/6303zdg "Learn how to troubleshoot Dynatrace Extensions")': '* [Устранение неполадок расширений](https://dt-url.net/6303zdg "Узнайте, как устранять неполадки с расширениями Dynatrace")',
}

PASS = {
    "title: Manage Microsoft SQL Server extensions",
    "source: https://docs.dynatrace.com/managed/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql",
    "scraped: 2026-05-12T11:10:29.358444",
    "# Manage Microsoft SQL Server extensions",
}

if __name__ == "__main__":
    build_one(REL, "microsoft-sql.md", TRANS, PASS)
    qa_one(REL, "microsoft-sql.md")
