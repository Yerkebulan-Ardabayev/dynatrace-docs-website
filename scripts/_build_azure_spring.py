# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_SPRING_APPS = "Мониторинг Azure Spring Apps и просмотр доступных метрик."
TT_SPRING = "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps."
TT_ENV = "Изучите концепцию токена доступа и его области."
TT_MONITORING = "Общие сведения о мониторинговых окружениях и работа с ними."
TT_ONEAGENT_MATRIX = "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."
TT_DEPLOY_API = "Просмотр сведений о подключении OneAgent через Dynatrace API."
TT_PG = "Способы настройки обнаружения группы процессов"

TRANS = {
    "title: Monitor Azure Spring Apps": "title: Мониторинг Azure Spring Apps",
    "# Monitor Azure Spring Apps": "# Мониторинг Azure Spring Apps",
    "* How-to guide": "* Практическое руководство",
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Jul 16, 2021": "* Опубликовано 16 июля 2021 г.",
    "## Capabilities": "## Возможности",
    "* Full-stack java monitoring powered by OneAgent": "* Мониторинг полного стека Java на базе OneAgent",
    f'* Integration with [Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Monitor Azure Spring Apps and view available metrics.")': f'* Интеграция с [Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "{TT_SPRING_APPS}")',
    "* Automatic service detection of services running in Azure Spring Apps": "* Автоматическое обнаружение сервисов, работающих в Azure Spring Apps",
    "Since Azure Spring Apps is a fully managed hosting platform, applications are deployed into a sandboxed environment that doesn't allow direct access to the underlying operating system.": "Azure Spring Apps, являясь полностью управляемой платформой хостинга, разворачивает приложения в изолированной среде, которая не допускает прямого доступа к базовой операционной системе.",
    "See below how you can integrate OneAgent with your Azure Spring Apps application to monitor your Spring Apps workloads with Dynatrace.": "Ниже описано, как интегрировать OneAgent с приложением Azure Spring Apps для мониторинга рабочих нагрузок Spring Apps с помощью Dynatrace.",
    "## Prerequisites": "## Предварительные требования",
    f'* Create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.")': f'* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "{TT_ENV}")',
    "* [Install the Azure CLI](https://dt-url.net/cf63rl6)": "* [Установите Azure CLI](https://dt-url.net/cf63rl6)",
    "## Set up integration": "## Настройка интеграции",
    f'[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': f'[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    f'**Prepare your environment in Azure**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#prepare-env "Learn how to configure OneAgent for monitoring Azure Spring Apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': f'**Подготовьте окружение в Azure**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#prepare-env "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    f'**Determine the values for the required environment variables**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#envvar "Learn how to configure OneAgent for monitoring Azure Spring Apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': f'**Определите значения необходимых переменных окружения**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#envvar "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
    f'**Add the environment variables to your application**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#add-variables "Learn how to configure OneAgent for monitoring Azure Spring Apps.")': f'**Добавьте переменные окружения в приложение**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#add-variables "Узнайте, как настроить OneAgent для мониторинга Azure Spring Apps.")',
    "### Step 1 Prepare your environment in Azure": "### Шаг 1. Подготовьте окружение в Azure",
    "1. In Azure Portal, create an Azure Spring Apps instance.": "1. В Azure Portal создайте экземпляр Azure Spring Apps.",
    "2. In the new Azure Spring Apps instance, create an application that you want to report to Dynatrace by running the command below.": "2. В новом экземпляре Azure Spring Apps создайте приложение, данные которого нужно передавать в Dynatrace, выполнив приведённую ниже команду.",
    "Be sure to replace the placeholders (`<...>`) with your own values.": "Обязательно замените заполнители (`<...>`) собственными значениями.",
    "### Step 2 Determine the values for the required environment variables": "### Шаг 2. Определите значения необходимых переменных окружения",
    "To set up OneAgent integration with your Azure Spring Apps instance, you need to configure three environment variables:": "Чтобы настроить интеграцию OneAgent с экземпляром Azure Spring Apps, необходимо задать три переменные окружения:",
    "* `DT_TENANT`": "* `DT_TENANT`",
    "* `DT_TENANTTOKEN`": "* `DT_TENANTTOKEN`",
    "* `DT_CONNECTION_POINT`.": "* `DT_CONNECTION_POINT`.",
    "Before you begin, collect the following information:": "Прежде чем начать, соберите следующие сведения:",
    f'* Your [Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")': f'* [Идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}")',
    "* Authentication": "* Аутентификация",
    "+ **PaaS token** authenticates you as a Dynatrace user and is required to determine the tenant token.": "+ **PaaS token** аутентифицирует вас как пользователя Dynatrace и необходим для определения tenant token.",
    "+ **Tenant token** allows OneAgent to report data to Dynatrace.": "+ **Tenant token** позволяет OneAgent передавать данные в Dynatrace.",
    f'For more information on tokens, see [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").': f'Подробнее о токенах см. в разделе [Токены доступа](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "{TT_ENV}").',
    f'1. The value for `DT_TENANT`is your [Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'1. Значение `DT_TENANT` совпадает с [идентификатором окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}").',
    f'2. To determine the values for `DT_TENANTTOKEN` and `DT_CONNECTION_POINT`, make an API request to the [Deployment API - GET connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") endpoint. The values you need are returned as `tenantToken` and `communicationEndpoints`.': f'2. Чтобы определить значения `DT_TENANTTOKEN` и `DT_CONNECTION_POINT`, выполните API-запрос к эндпоинту [Deployment API - GET connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "{TT_DEPLOY_API}"). Нужные значения возвращаются как `tenantToken` и `communicationEndpoints`.',
    "You can submit the call to your environment URL (SaaS or Managed) or an Environment ActiveGate URL.": "Запрос можно отправить на URL вашего окружения (SaaS или Managed) либо на URL Environment ActiveGate.",
    "* **Dynatrace SaaS**:": "* **Dynatrace SaaS**:",
    "Replace:": "Замените:",
    f'+ `<your-environment-id>` with your [Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")': f'+ `<your-environment-id>` на [идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}")',
    "+ `<your_PaaS_token>` with your [PaaS token](#prerequisites)": "+ `<your_PaaS_token>` на [PaaS token](#prerequisites)",
    "* **Dynatrace Managed**:": "* **Dynatrace Managed**:",
    f"+ `<your-domain>` with your Managed deployment domain": f"+ `<your-domain>` на домен вашего Managed-развёртывания",
    f'+ `<your-environment-id>` with your [Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") (2)': f'+ `<your-environment-id>` на [идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}") (2)',
    "+ `<your_PaaS_token>` with your [PaaS token](#prerequisites) (2)": "+ `<your_PaaS_token>` на [PaaS token](#prerequisites) (2)",
    "* **Environment ActiveGate**:": "* **Environment ActiveGate**:",
    "Replace": "Замените",
    "+ `<your-activegate-domain>` with your ActiveGate domain": "+ `<your-activegate-domain>` на домен вашего ActiveGate",
    f'+ `<your-environment-id>` with your [Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") (3)': f'+ `<your-environment-id>` на [идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}") (3)',
    "+ `<your_PaaS_token>` with your [PaaS token](#prerequisites) (3)": "+ `<your_PaaS_token>` на [PaaS token](#prerequisites) (3)",
    "### Step 3 Add the environment variables to your application": "### Шаг 3. Добавьте переменные окружения в приложение",
    "Once you have the values for the environment variables required for OneAgent integration, you can add the respective key/value pairs to your application either on Azure Portal, or in the Azure CLI. See the instructions below for each of these options.": "Получив значения переменных окружения, необходимых для интеграции OneAgent, можно добавить соответствующие пары «ключ/значение» в приложение через Azure Portal или Azure CLI. Инструкции для каждого из вариантов приведены ниже.",
    "In the Azure CLI": "В Azure CLI",
    "In Azure Portal": "В Azure Portal",
    "Run the command below, making sure to replace the placeholders (`<...>`) with your own values determined in the previous steps.": "Выполните приведённую ниже команду, заменив заполнители (`<...>`) собственными значениями, определёнными на предыдущих шагах.",
    "1. Go to your Azure Spring Apps instance and select the resource group where Dynatrace will be deployed.": "1. Откройте экземпляр Azure Spring Apps и выберите группу ресурсов, в которой будет развёрнут Dynatrace.",
    "2. Select the application for which you want Dynatrace to report data.": "2. Выберите приложение, данные которого нужно передавать в Dynatrace.",
    "3. Select **Configuration** and enter the following environment variables key/value pairs.": "3. Выберите **Configuration** и введите следующие пары «ключ/значение» для переменных окружения.",
    "| Key | Value |": "| Ключ | Значение |",
    "| --- | --- |": "| --- | --- |",
    f'| `DT_TENANT` | [Your Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") |': f'| `DT_TENANT` | [Идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}") |',
    "| `DT_TENANTTOKEN` | Your tenant token. See [Determine the values for the required environment variables](#envvar) for details. |": "| `DT_TENANTTOKEN` | Ваш tenant token. Подробнее см. в разделе [Определение значений необходимых переменных окружения](#envvar). |",
    "| `DT_CONNECTION_POINT` | Your communication endpoint. See [Determine the values for the required environment variables](#envvar) for details. |": "| `DT_CONNECTION_POINT` | Ваш communication endpoint. Подробнее см. в разделе [Определение значений необходимых переменных окружения](#envvar). |",
    f"4. [Create a buildpack binding](https://dt-url.net/nu036u6) for Dynatrace using the PaaS token (API token) and API url as properties.": f"4. [Создайте buildpack binding](https://dt-url.net/nu036u6) для Dynatrace, указав PaaS token (API token) и API url в качестве свойств.",
    "| Property | Value |": "| Свойство | Значение |",
    f'| `api-url` | [Your Dynatrace environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") |': f'| `api-url` | [Идентификатор окружения Dynatrace](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_MONITORING}") |',
    "| `api-token` | [PaaS token](#prerequisites) |": "| `api-token` | [PaaS token](#prerequisites) |",
    f'Optionally, you can customize the built-in rules for process group detection by setting another environment variable, `DT_CLUSTER_ID`. The value can be the name of the process group you want to see in Dynatrace. See [Process group detection](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") for details.': f'При необходимости можно настроить встроенные правила обнаружения группы процессов, задав дополнительную переменную окружения `DT_CLUSTER_ID`. В качестве значения укажите имя группы процессов, которое должно отображаться в Dynatrace. Подробнее см. в разделе [Обнаружение группы процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "{TT_PG}").',
    "## View data in Dynatrace": "## Просмотр данных в Dynatrace",
    "Once you add the environment variables to your application, Dynatrace starts collecting data from it. To view data for your Azure Spring Apps application, go to **Services** and select your application.": "После добавления переменных окружения в приложение Dynatrace начнёт собирать из него данные. Чтобы просмотреть данные приложения Azure Spring Apps, откройте **Services** и выберите нужное приложение.",
    "Example service flow:": "Пример потока сервиса:",
    "![AppFlow](https://dt-cdn.net/images/1-1721-67868203e3.png)": "![AppFlow](https://dt-cdn.net/images/1-1721-67868203e3.png)",
    "AppFlow": "AppFlow",
    "Example CPU consumption:": "Пример потребления CPU:",
    "![Diagnostic cpu](https://dt-cdn.net/images/diagnostic-cpu-1565-a403ae7a02.png)": "![Diagnostic cpu](https://dt-cdn.net/images/diagnostic-cpu-1565-a403ae7a02.png)",
    "Diagnostic cpu": "Diagnostic cpu",
    "Example response time analysis:": "Пример анализа времени отклика:",
    "![Resposetime](https://dt-cdn.net/images/f-1486-bd826153cb.png)": "![Resposetime](https://dt-cdn.net/images/f-1486-bd826153cb.png)",
    "Resposetime": "Resposetime",
    "## OneAgent updates": "## Обновления OneAgent",
    "OneAgent updates are performed automatically with the JDK.": "Обновления OneAgent выполняются автоматически вместе с JDK.",
    "Following a OneAgent update, you need to restart or redeploy your applications for them to be monitored with a new OneAgent version. This is because some components of OneAgent keep running in processes that are monitored by Dynatrace.": "После обновления OneAgent необходимо перезапустить или повторно развернуть приложения, чтобы они отслеживались новой версией OneAgent. Это обусловлено тем, что некоторые компоненты OneAgent продолжают работать в процессах, отслеживаемых Dynatrace.",
    "* Before restart, these processes will continue to be monitored with the previous version of OneAgent.": "* До перезапуска эти процессы будут по-прежнему отслеживаться с предыдущей версией OneAgent.",
    "* After restart, these processes will be monitored with the latest version of OneAgent.": "* После перезапуска эти процессы будут отслеживаться с последней версией OneAgent.",
    "## Related topics": "## Связанные темы",
    f'* [Monitor Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Monitor Azure Spring Apps and view available metrics.")': f'* [Мониторинг Azure Spring Apps](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "{TT_SPRING_APPS}")',
    f'* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': f'* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "{TT_ONEAGENT_MATRIX}")',
}

# Lines that appear multiple times with identical stripped text but different context
# The engine matches by norm'd content; duplicated keys need disambiguation.
# azure-spring.md has two DT_MANAGED and two DT_SAAS replacement blocks —
# each block's Replace: line differs only by presence (line 80 vs 89 vs 101).
# The lines whose stripped content is IDENTICAL across occurrences are covered by
# a single dict entry — the engine applies the same RU to each matching line.

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-spring.md", TRANS, PASS)
    qa_one(REL, "azure-spring.md")
