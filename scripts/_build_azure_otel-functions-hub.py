# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans"

TT_HUB = "Мониторинг плана Consumption для Azure Functions с OpenTelemetry и Dynatrace."
TT_DOTNET = "Мониторинг Azure Functions с OpenTelemetry для .NET и Dynatrace."
TT_NODEJS = "Мониторинг Azure Functions с OpenTelemetry для Node.js и Dynatrace."
TT_PYTHON = "Мониторинг Azure Functions с OpenTelemetry для Python и Dynatrace."
TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_OAMATRIX = "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."
TT_SITE_EXT = "Узнайте, как установить, настроить, обновить и удалить OneAgent для мониторинга Azure Functions через расширение Azure site extension."

TRANS = {
    "title: Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan": "title: Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption",
    "# Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan": "# Настройка мониторинга OpenTelemetry для Azure Functions на плане Consumption",
    "* How-to guide": "* Практическое руководство",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Mar 31, 2025": "* Обновлено 31 марта 2025 г.",
    "Dynatrace version 1.240+ OneAgent version 1.193+": "Dynatrace версии 1.240+ OneAgent версии 1.193+",
    f"Dynatrace uses [OpenTelemetry](https://dt-url.net/y903u4j) to monitor Azure Functions invocations.": "Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов Azure Functions.",
    f'For that purpose, Dynatrace provides language-specific packages, such as [`Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` for .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace."), that can be used in combination with default OpenTelemetry SDKs and APIs.': f'Для этого Dynatrace предоставляет пакеты для конкретных языков, например [`Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` для .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "{TT_DOTNET}"), которые можно использовать совместно со стандартными SDK и API OpenTelemetry.',
    "## Installation": "## Установка",
    f'[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': f'[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    f'**Activate the OneAgent feature**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#oneagent-feature "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': f'**Активация функции OneAgent**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#oneagent-feature "{TT_HUB}")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    f'**Select a configuration method**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#choose-config-method "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")': f'**Выбор метода настройки**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#choose-config-method "{TT_HUB}")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")',
    f'**Specify a Dynatrace API endpoint**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#specify-endpoint "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")': f'**Указание эндпоинта Dynatrace API**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#specify-endpoint "{TT_HUB}")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")',
    f'**Apply the configuration to your function app**](#apply-config)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")': f'**Применение настроек к приложению функции**](#apply-config)[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")',
    f'**Instrument the function code**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#instrument-code "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.")': f'**Инструментирование кода функции**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions#instrument-code "{TT_HUB}")',
    "### Step 1 Activate the OneAgent feature": "### Шаг 1. Активация функции OneAgent",
    "Go to **Settings** > **Preferences** > **OneAgent features** and activate the **Forward Tag 4 trace context extension** OneAgent feature.": "Откройте **Settings** > **Preferences** > **OneAgent features** и активируйте функцию OneAgent **Forward Tag 4 trace context extension**.",
    "### Step 2 Select a configuration method": "### Шаг 2. Выбор метода настройки",
    "1. In Dynatrace,  **Search** for **Deploy OneAgent** app and select it.": "1. В Dynatrace введите **Deploy OneAgent** в строке **Search** и выберите приложение.",
    "2. Under **Download Dynatrace OneAgent**, select **Set up** > **Azure Functions**.": "2. В разделе **Download Dynatrace OneAgent** выберите **Set up** > **Azure Functions**.",
    "3. On the **Enable Monitoring for Azure Functions** page, under **How will you configure your Azure Functions?**, select your preferred configuration method from the dropdown menu.": "3. На странице **Enable Monitoring for Azure Functions** в разделе **How will you configure your Azure Functions?** выберите нужный метод настройки из выпадающего меню.",
    "### Step 3 optional Specify a Dynatrace API endpoint Optional": "### Шаг 3 (необязательно). Указание эндпоинта Dynatrace API",
    "If you don't want to use the default public Dynatrace endpoint, specify a custom Dynatrace API endpoint where you want to receive monitoring data.": "Если не нужно использовать стандартный публичный эндпоинт Dynatrace, укажите пользовательский эндпоинт Dynatrace API для получения данных мониторинга.",
    "To reduce network latency, you typically deploy a Dynatrace ActiveGate close to (in the same region as) the Azure Function that you want to monitor.": "Для снижения сетевой задержки рекомендуется развернуть Dynatrace ActiveGate рядом с монитируемой Azure Function (в том же регионе).",
    "### Step 4 Apply the configuration to your function app": "### Шаг 4. Применение настроек к приложению функции",
    "To apply the configuration, select one of the options below, depending on your configuration method.": "Чтобы применить настройки, выберите один из вариантов ниже в зависимости от метода настройки.",
    "Configure with JSON file": "Настройка с помощью файла JSON",
    "Configure with environment variables": "Настройка с помощью переменных окружения",
    "Copy the JSON snippet into a file named `dtconfig.json` located in the root folder of your Azure Functions deployment.": "Скопируйте фрагмент JSON в файл `dtconfig.json`, расположенный в корневой папке развёртывания Azure Functions.",
    "On **Enable Monitoring for Azure Functions**, under **Use the following values to configure your monitored Azure Functions**, there's a snippet with all required environment variables. Be sure to add these environment variables and their values to your function app configuration:": "На странице **Enable Monitoring for Azure Functions** в разделе **Use the following values to configure your monitored Azure Functions** содержится фрагмент со всеми необходимыми переменными окружения. Добавьте эти переменные и их значения в настройки приложения функции:",
    "1. In Azure Portal, go to your function app.": "1. В Azure Portal перейдите к приложению функции.",
    "2. In **Settings**, select **Configuration**.": "2. В **Settings** выберите **Configuration**.",
    "3. Edit any existing environment variables so that the names and values match those in [Dynatrace](#variables-dynatrace), or, if your function app doesn't have any existing variables, select **New application setting** and add the names and values for all the variables in [Dynatrace](#variables-dynatrace).": "3. Отредактируйте существующие переменные окружения, чтобы их имена и значения совпадали с указанными в [Dynatrace](#variables-dynatrace), или, если в приложении функции нет существующих переменных, выберите **New application setting** и добавьте имена и значения всех переменных из [Dynatrace](#variables-dynatrace).",
    "Leave the settings not listed by Dynatrace unchanged.": "Настройки, не указанные в Dynatrace, оставьте без изменений.",
    "### Step 5 Instrument the function code": "### Шаг 5. Инструментирование кода функции",
    "Adding the required API calls to monitor function invocations via OpenTelemetry is specific to languages and their respective OpenTelemetry distribution:": "Добавление необходимых вызовов API для мониторинга вызовов функций через OpenTelemetry зависит от используемого языка и соответствующего дистрибутива OpenTelemetry:",
    f'* **.NET (C#):** [Trace Azure Functions written in .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "Monitor Azure Functions with OpenTelemetry for .NET and Dynatrace.")': f'* **.NET (C#):** [Трассировка Azure Functions на .NET](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet "{TT_DOTNET}")',
    f'* **Node.js (Javascript):** [Trace Azure Functions written in Node.js](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "Monitor Azure Functions with OpenTelemetry for Node.js and Dynatrace.")': f'* **Node.js (Javascript):** [Трассировка Azure Functions на Node.js](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs "{TT_NODEJS}")',
    f'* **Python:** [Trace Azure Functions written in Python](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "Monitor Azure Functions with OpenTelemetry for Python and Dynatrace.")': f'* **Python:** [Трассировка Azure Functions на Python](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-python "{TT_PYTHON}")',
    "## Known limitations": "## Известные ограничения",
    "The Dynatrace Azure Functions integration doesn't capture the IP addresses of outgoing HTTP requests. If the called service isn't monitored with Dynatrace OneAgent, this results in **unmonitored hosts**.": "Интеграция Dynatrace с Azure Functions не захватывает IP-адреса исходящих HTTP-запросов. Если вызываемый сервис не отслеживается через Dynatrace OneAgent, это приводит к появлению **неотслеживаемых хостов**.",
    "## Related topics": "## Связанные темы",
    f'* [Monitor Azure Functions on App Service Plan for Windows](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.")': f'* [Мониторинг Azure Functions на App Service Plan для Windows](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "{TT_SITE_EXT}")',
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    f'* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': f'* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "{TT_OAMATRIX}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "opentelemetry-on-azure-functions.md", TRANS, PASS)
    qa_one(REL, "opentelemetry-on-azure-functions.md")
