# -*- coding: utf-8 -*-
"""L4-IF.73 -- ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_AZURE_INT = "Настройка глубокого мониторинга кода в Azure с помощью OneAgent или OpenTelemetry."
TT_ENV_ID = "Узнайте, как определить идентификатор среды мониторинга и работать с ней."
TT_DDU_LOG = "Узнайте, как рассчитывается объём потребления DDU в Dynatrace Log Monitoring Classic."
TT_LOG_INGEST = "Узнайте, как Dynatrace принимает данные журналов и каковы возможные ограничения."
TT_API_TOKEN = "Узнайте о концепции токена доступа и его областях применения."
TT_SCALING = "#scalingguide"
TT_DQL_UNAVAIL = "Ваш выбор недоступен в Dynatrace Managed."
TT_DIAG = "https://dt-url.net/se83r02"
TT_AZ_CLI = "https://dt-url.net/cf63rl6"
TT_MI = "https://dt-url.net/qj23rie"
TT_GH_ARM = "https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/blob/master/deployment/dynatrace-azure-forwarder.json"
TT_GH_REL = "https://github.com/dynatrace-oss/dynatrace-azure-log-forwarder/releases"
TT_STREAM_LOGS = "https://learn.microsoft.com/en-us/azure/azure-functions/streaming-logs"
TT_FNMATCH = "https://docs.python.org/3/library/fnmatch.html"
TT_EH_SETUP = "https://dt-url.net/8w03rs3"
TT_COMMUNITY = "https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797"

TRANS = {
    # Frontmatter / titles
    "title: Azure Logs": "title: Журналы Azure",
    "# Azure Logs": "# Журналы Azure",
    "* How-to guide": "* Практическое руководство",
    "* 17-min read": "* Чтение: 17 мин",
    "* Updated on Oct 17, 2025": "* Обновлено 17 октября 2025 г.",

    # DDU callout
    "DDU consumption for Log Monitoring": "Потребление DDU для Log Monitoring",
    'DDU pricing applies to cloud Log Monitoring. See [DDUs for Log Monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.") for details.': f'Тарификация DDU распространяется на облачный Log Monitoring. Подробнее см. в разделе [DDU для Log Monitoring](/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "{TT_DDU_LOG}").',

    # Intro
    "Azure log forwarding allows you to stream Azure logs from Azure Event Hubs into Dynatrace logs via an Azure Function App instance. It supports Azure resource logs, activity logs, and Entra ID sign-in logs.": "Azure log forwarding позволяет передавать журналы Azure из Azure Event Hubs в Dynatrace через экземпляр Azure Function App. Поддерживаются журналы ресурсов Azure, журналы действий и журналы входа Entra ID.",

    # Resources to be deployed
    "## Resources to be deployed": "## Разворачиваемые ресурсы",
    "Azure log forwarding is performed directly through Cluster API. If you don't want to use direct ingest through the Cluster API, you have to use an existing ActiveGate for log ingestion.": "Azure log forwarding выполняется напрямую через Cluster API. Если прямой приём через Cluster API не нужен, для приёма журналов необходимо использовать существующий ActiveGate.",
    "Deployment of Azure log forwarder results in creating the following resources:": "Развёртывание Azure log forwarder создаёт следующие ресурсы:",
    "* Storage account (`Microsoft.Storage/storageAccounts`)": "* Storage account (`Microsoft.Storage/storageAccounts`)",
    "* Storage Account Blob Service (`Microsoft.Storage/storageAccounts/blobServices`)": "* Storage Account Blob Service (`Microsoft.Storage/storageAccounts/blobServices`)",
    "* Azure App Service plan (`Microsoft.Web/serverfarms`)": "* Azure App Service plan (`Microsoft.Web/serverfarms`)",
    "* Azure Function App (`Microsoft.Web/sites`)": "* Azure Function App (`Microsoft.Web/sites`)",
    "Azure log forwarder uses Linux based Azure function by default. Windows based function is not supported.": "Azure log forwarder по умолчанию использует Azure function на базе Linux. Функции на базе Windows не поддерживаются.",
    f'For details about the resources created, see the [Azure Resource Manager file on GitHub]({TT_GH_ARM})': f'Подробнее о создаваемых ресурсах см. в [файле Azure Resource Manager на GitHub]({TT_GH_ARM})',

    # Limitations
    "## Limitations": "## Ограничения",
    "Logs older than 24 hours are rejected (considered too old by the Dynatrace log ingest endpoint), so we recommend that you don't set a retention time of more than 24 hours for Azure Event Hubs.": "Журналы старше 24 часов отклоняются (эндпоинт приёма журналов Dynatrace считает их устаревшими), поэтому рекомендуется не устанавливать время хранения в Azure Event Hubs более 24 часов.",
    "The Azure log forwarder supports a maximum 70 MB per minute (~4 GB per hour) in the default configuration. The throughput is measured with Event Hubs metric `Outgoing Bytes` of the Event Hubs instance attached to the function. See [Scaling guide](#scalingguide) for scaling instructions.": "Azure log forwarder поддерживает максимум 70 МБ в минуту (~4 ГБ в час) в конфигурации по умолчанию. Пропускная способность измеряется метрикой Event Hubs `Outgoing Bytes` экземпляра Event Hubs, привязанного к функции. Инструкции по масштабированию см. в разделе [Руководство по масштабированию](#scalingguide).",

    # Prerequisites
    "## Prerequisites": "## Предварительные требования",
    "See below the list of requirements for setting up Azure log forwarding. Some are needed before you start deployment, others during the deployment process.": "Ниже приведён список требований для настройки Azure log forwarding. Часть из них необходима до начала развёртывания, остальные нужны в процессе.",

    # Dynatrace subsection
    "### Dynatrace": "### Dynatrace",
    "If you're using an earlier version of Dynatrace, see [Alternative deployments](#alternative) for instructions.": "Если используется более ранняя версия Dynatrace, инструкции см. в разделе [Альтернативные варианты развёртывания](#alternative).",
    "* Dynatrace version 1.217+": "* Dynatrace версии 1.217+",
    '* [Enable generic log ingestion](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")': f'* [Включите универсальный приём журналов](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "{TT_LOG_INGEST}")',
    '* [Create an API token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and enable the **Ingest logs** permission. The API token applies to both versions.': f'* [Создайте токен API](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "{TT_API_TOKEN}") и включите разрешение **Ingest logs**. Токен API применяется к обеим версиям.',

    # Azure subsection
    "### Azure": "### Azure",
    f'1. In each Azure location from where you want to pull logs [Create a resource group & Set up an Azure Event Hubs instance]({TT_EH_SETUP}).': f'1. В каждом регионе Azure, откуда требуется получать журналы, [создайте группу ресурсов и настройте экземпляр Azure Event Hubs]({TT_EH_SETUP}).',
    "To be able to send logs,": "Чтобы иметь возможность отправлять журналы,",
    "* The Event Hubs instances and the resource group in which the deployment will run need to be in the same region.": "* Экземпляры Event Hubs и группа ресурсов, в которой будет выполняться развёртывание, должны находиться в одном регионе.",
    "* make sure that in Event Hubs Namespace > Public access > Public network access, the **Disabled** option button is NOT selected. Otherwise, the logs won't be sent to Dynatrace.": "* Убедитесь, что в разделе Event Hubs Namespace > Public access > Public network access кнопка **Disabled** НЕ выбрана. В противном случае журналы не будут отправлены в Dynatrace.",
    "2. Create an authorization rule with the **listen** permission for the Event Hubs instance that is configured for receiving logs:": "2. Создайте правило авторизации с разрешением **listen** для экземпляра Event Hubs, настроенного для приёма журналов:",
    "3. Get an Event Hubs connection string for the authorization rule created above:": "3. Получите строку подключения Event Hubs для созданного выше правила авторизации:",
    f'4. Configure the [diagnostic settings]({TT_DIAG}) to stream both resource-related and Entra ID sign-in logs to the Azure Event Hub instances.': f'4. Настройте [параметры диагностики]({TT_DIAG}), чтобы передавать как журналы ресурсов, так и журналы входа Entra ID в экземпляры Azure Event Hub.',

    # CLI subsection
    "### CLI": "### CLI",
    f'You can run Azure log forwarding deployment using Azure Portal Cloud Shell (Bash) or from any machine with [Azure CLI]({TT_AZ_CLI}) and Bash shell (Linux or Windows WSL).': f'Развёртывание Azure log forwarding можно выполнить с помощью Azure Portal Cloud Shell (Bash) или с любого компьютера с установленным [Azure CLI]({TT_AZ_CLI}) и оболочкой Bash (Linux или Windows WSL).',

    # Deploy
    "## Deploy": "## Развёртывание",
    "1. Set the following environment variables, making sure to replace the placeholders (`<...>`) with your own values.": "1. Задайте следующие переменные среды, заменив заполнители (`<...>`) собственными значениями.",
    "* For `DEPLOYMENT_NAME`, enter your deployment name between 3 and 20 characters long. You can use lowercase letters and numbers.": "* Для `DEPLOYMENT_NAME` укажите имя развёртывания длиной от 3 до 20 символов. Допускаются строчные буквы и цифры.",
    "**Note:** The name needs to be globally unique—it is appended to the created Azure resources.": "**Примечание:** Имя должно быть глобально уникальным, так как оно добавляется к создаваемым ресурсам Azure.",
    '* For `TARGET_URL`, enter your environment URL: `https://{your-domain}/e/{your-environment-id}/e/{your-environment-id}/`. To learn how to determine your environment ID for the Managed deployment, see [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Для `TARGET_URL` укажите URL среды: `https://{{your-domain}}/e/{{your-environment-id}}/e/{{your-environment-id}}/`. Чтобы узнать, как определить идентификатор среды для развёртывания Managed, см. [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENV_ID}").',
    "* For `TARGET_API_TOKEN`, enter your API token. See [Dynatrace requirements](#dynatrace) for details.": "* Для `TARGET_API_TOKEN` введите токен API. Подробнее см. в разделе [Требования Dynatrace](#dynatrace).",
    "* For `RESOURCE_GROUP`, enter the name of the Azure resource group in which deployment will run. See [Azure requirements](#azure) for details.": "* Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробнее см. в разделе [Требования Azure](#azure).",
    "* For `EVENT_HUB_CONNECTION_STRING`, enter the connection string for the Azure Event Hubs instances configured for receiving logs. See [Azure requirements](#azure) for details.": "* Для `EVENT_HUB_CONNECTION_STRING` введите строку подключения для экземпляров Azure Event Hubs, настроенных для приёма журналов. Подробнее см. в разделе [Требования Azure](#azure).",
    "Optional You can enable [self-monitoring](#sfm) and/or [log filtering](#filter) during or after deployment.": "Дополнительно Можно включить [самомониторинг](#sfm) и/или [фильтрацию журналов](#filter) во время или после развёртывания.",
    "2. Download the `azure-log-forwarder-function` script and deploy the infrastructure.": "2. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.",

    # View Azure logs
    "## View Azure logs": "## Просмотр журналов Azure",
    "After deploying the script, you can view and analyze Azure logs in Dynatrace:": "После развёртывания скрипта можно просматривать и анализировать журналы Azure в Dynatrace:",
    "Go to **Logs** and, in the attributes filter, search for **Azure**.": "Откройте **Logs** и в фильтре атрибутов выполните поиск по **Azure**.",
    "* If you see logs coming in, you managed to deploy Azure log forwarder successfully.": "* Если журналы поступают, Azure log forwarder развёрнут успешно.",
    "* If there are no logs within 10 minutes checkout the **Verification** guide section of the page.": "* Если журналы не появились в течение 10 минут, обратитесь к разделу **Verification** на этой странице.",
    'You can use [DQL](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") to filter for Azure logs.': f'Для фильтрации журналов Azure можно использовать [DQL](/managed/upgrade/unavailable-in-managed "{TT_DQL_UNAVAIL}").',
    "As an example, you could add the following line to a DQL query:": "Например, в DQL-запрос можно добавить следующую строку:",
    "If you already have multiple integrations, you can additionally use the values `cloud.log_forwarder` and `dt.auth.origin` to further refine your filters.": "При наличии нескольких интеграций для уточнения фильтров можно дополнительно использовать значения `cloud.log_forwarder` и `dt.auth.origin`.",

    # Self-monitoring
    "## Self-monitoring Optional": "## Самомониторинг Дополнительно",
    "Self-monitoring allows a quick diagnosis to see if your function processes and sends logs to Dynatrace properly.": "Самомониторинг позволяет быстро диагностировать, правильно ли функция обрабатывает и отправляет журналы в Dynatrace.",
    "### Enable self-monitoring": "### Включение самомониторинга",
    "To enable self-monitoring, you have two options:": "Для включения самомониторинга существует два варианта:",
    "* **During deployment:** Set the [`--enable-self-monitoring` parameter](#par) (or the [`SFM_ENABLED` environment variable](#var)) to `true`.": "* **Во время развёртывания:** Задайте параметр [`--enable-self-monitoring`](#par) (или переменную среды [`SFM_ENABLED`](#var)) в значение `true`.",
    "* **After deployment:** In Azure Portal, go to the configuration of your deployed Function App instance and set `SELF_MONITORING_ENABLED` to `true`.": "* **После развёртывания:** В Azure Portal откройте конфигурацию развёрнутого экземпляра Function App и задайте `SELF_MONITORING_ENABLED` в значение `true`.",
    "Enable managed identity": "Включение managed identity",
    f'After enabling self-monitoring, you need to enable [managed identity]({TT_MI}) for': f'После включения самомониторинга необходимо включить [managed identity]({TT_MI}) для',
    "your Function App instance created during deployment, and configure it to allow pushing metrics to the resource.": "экземпляра Function App, созданного во время развёртывания, и настроить его для отправки метрик ресурсу.",
    "To set up managed identity": "Настройка managed identity",
    "1. In Azure Portal, go to the **Settings** of your Function App instance created during deployment, and select **Identity**.": "1. В Azure Portal откройте **Settings** экземпляра Function App, созданного во время развёртывания, и выберите **Identity**.",
    "2. Select **Yes** to **Enable system assigned managed identity**.": "2. Выберите **Yes** для **Enable system assigned managed identity**.",
    "3. Go to your resource group where Function App is deployed and select **Access control (IAM)**.": "3. Перейдите в группу ресурсов, где развёрнут Function App, и выберите **Access control (IAM)**.",
    "4. Select **Add** to add a role assignment.": "4. Нажмите **Add** для добавления назначения роли.",
    "5. Set the **Monitoring Metrics Publisher** role.": "5. Задайте роль **Monitoring Metrics Publisher**.",
    "6. Select **Save** to save your configuration.": "6. Нажмите **Save** для сохранения конфигурации.",

    # Self-monitoring metrics
    "### Self-monitoring metrics": "### Метрики самомониторинга",
    "Once you enable self-monitoring, you can view the following metrics in your `dynatrace_logs_self_monitoring` namespace of the newly deployed Function App instance.": "После включения самомониторинга в пространстве имён `dynatrace_logs_self_monitoring` нового экземпляра Function App будут доступны следующие метрики.",
    "| Metric name | Description | Dimension |": "| Название метрики | Описание | Измерение |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| `all_requests` | All requests sent to Dynatrace. |  |": "| `all_requests` | Все запросы, отправленные в Dynatrace. |  |",
    "| `dynatrace_connectivity_failures` | Reported when any Dynatrace connectivity issues occurred. | `connectivity_status` |": "| `dynatrace_connectivity_failures` | Фиксируется при возникновении проблем с подключением к Dynatrace. | `connectivity_status` |",
    "| `parsing_errors` | Reported when any parsing errors occurred during log processing. |  |": "| `parsing_errors` | Фиксируется при возникновении ошибок разбора в процессе обработки журналов. |  |",
    "| `processing_time` | Time needed to process all logs. |  |": "| `processing_time` | Время, необходимое для обработки всех журналов. |  |",
    "| `sending_time` | Time needed to send all requests. |  |": "| `sending_time` | Время, необходимое для отправки всех запросов. |  |",
    "| `too_long_content_size` | Reported when content of log is too long. The content will be trimmed. |  |": "| `too_long_content_size` | Фиксируется, когда содержимое журнала слишком велико. Содержимое будет обрезано. |  |",
    "| `too_old_records` | Reported when logs received from Event Hubs are too old. |  |": "| `too_old_records` | Фиксируется, когда журналы, полученные из Event Hubs, устарели. |  |",

    # Log filtering
    "## Log filtering Optional": "## Фильтрация журналов Дополнительно",
    "To reduce the number of logs that are sent to Dynatrace, you can apply filters.": "Чтобы сократить количество журналов, отправляемых в Dynatrace, можно применить фильтры.",
    "To apply filters you have two options:": "Для применения фильтров существует два варианта:",
    "* **During deployment:** Set the `FILTER_CONFIG` environment variable in Azure Portal Cloud Shell (Bash) before running the deployment script.": "* **Во время развёртывания:** Задайте переменную среды `FILTER_CONFIG` в Azure Portal Cloud Shell (Bash) перед запуском скрипта развёртывания.",
    "1. Add the `FILTER_CONFIG` environment variable to the list of environment variables needed for the deployment script.": "1. Добавьте переменную среды `FILTER_CONFIG` в список переменных среды, необходимых для скрипта развёртывания.",
    "Be sure to replace placeholders with your values. See [Filter options](#options) for details.": "Обязательно замените заполнители собственными значениями. Подробнее см. в разделе [Параметры фильтра](#options).",
    "2. Set the environment variables.": "2. Задайте переменные среды.",
    "3. Download the `azure-log-forwarder-function` script and deploy the infrastructure.": "3. Загрузите скрипт `azure-log-forwarder-function` и разверните инфраструктуру.",
    "* **After deployment:** Add `FILTER_CONFIG` in Azure Portal.": "* **После развёртывания:** Добавьте `FILTER_CONFIG` в Azure Portal.",
    "1. In Azure Portal, go to **Environment variables** of your deployed Function App instance.": "1. В Azure Portal откройте **Environment variables** развёрнутого экземпляра Function App.",
    "2. In **App settings**, search and select **FILTER\\_CONFIG**.": "2. В разделе **App settings** найдите и выберите **FILTER\\_CONFIG**.",
    "**FILTER\\_CONFIG** will appear in Azure after running the deployment script.": "**FILTER\\_CONFIG** появится в Azure после запуска скрипта развёртывания.",
    "3. Select **Edit** to add a **Value** for your filter.": "3. Нажмите **Edit**, чтобы задать **Value** для фильтра.",
    "Example edit": "Пример редактирования",
    "![Edit](https://dt-cdn.net/images/image-36-3759-7bc37dfe3c.png)": "![Редактирование](https://dt-cdn.net/images/image-36-3759-7bc37dfe3c.png)",
    "Edit": "Редактирование",
    "Alternatively, you can select **Advanced edit** to enter your value in the JSON.": "В качестве альтернативы можно нажать **Advanced edit** и ввести значение в формате JSON.",
    "Example advanced edit": "Пример расширенного редактирования",
    "![Advanced](https://dt-cdn.net/images/image-37-3804-dffe41ec79.png)": "![Расширенный режим](https://dt-cdn.net/images/image-37-3804-dffe41ec79.png)",
    "Advanced": "Расширенный режим",
    "4. Select **OK**.": "4. Нажмите **OK**.",
    "5. Restart your Function App instance.": "5. Перезапустите экземпляр Function App.",

    # Filter options
    "### Filter options": "### Параметры фильтра",
    "`FILTER_CONFIG` is a key-value pair variable. You can set two types of filters (`MIN_LOG_LEVEL` and/or `CONTAINS_PATTERN`) for three filter groups (`GLOBAL`, `RESOURCE_TYPE`, and/or `RESOURCE_ID`).": "`FILTER_CONFIG`: переменная в формате пар «ключ-значение». Можно задать два типа фильтров (`MIN_LOG_LEVEL` и/или `CONTAINS_PATTERN`) для трёх групп фильтров (`GLOBAL`, `RESOURCE_TYPE` и/или `RESOURCE_ID`).",
    "#### Filter type: `MIN_LOG_LEVEL`": "#### Тип фильтра: `MIN_LOG_LEVEL`",
    "This filter type allows you to filter out logs with unwanted levels. Possible log levels are:": "Данный тип фильтра позволяет исключать журналы с нежелательными уровнями. Возможные уровни журналов:",
    "* **Critical** (or `1`)": "* **Critical** (или `1`)",
    "* **Error** (or `2`)": "* **Error** (или `2`)",
    "* **Warning** (or `3`)": "* **Warning** (или `3`)",
    "* **Informational** (or `4`)": "* **Informational** (или `4`)",
    "Example:": "Пример:",
    '`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Warning"`': '`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Warning"`',
    "In the example above, **Informational** logs will be skipped, and only **Warning**, **Error**, and **Critical** logs will be sent to Dynatrace.": "В приведённом примере журналы уровня **Informational** будут пропущены, и в Dynatrace будут отправлены только журналы **Warning**, **Error** и **Critical**.",
    "Syntax options are:": "Варианты синтаксиса:",
    "* `FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>`": "* `FILTER.GLOBAL.MIN_LOG_LEVEL=<log_level>`",
    "* `FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>`": "* `FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.<resource_type>=<log_level>`",
    "* `FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>`": "* `FILTER.RESOURCE_ID.MIN_LOG_LEVEL.<resource_id>=<log_level>`",
    "You can have one global-level filter and additional filters for a particular resource type/ID.": "Можно задать один глобальный фильтр и дополнительные фильтры для конкретного типа ресурса или идентификатора ресурса.",
    '`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Error;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.MICROSOFT.WEB/SITES=Informational"`': '`FILTER_CONFIG="FILTER.GLOBAL.MIN_LOG_LEVEL=Error;FILTER.RESOURCE_TYPE.MIN_LOG_LEVEL.MICROSOFT.WEB/SITES=Informational"`',
    "In the example above, all logs from instances with resource type `MICROSOFT.WEB/SITES` will be sent to Dynatrace, while for all other resources, **Informational** and **Warning** logs will be filtered out.": "В приведённом примере все журналы от экземпляров с типом ресурса `MICROSOFT.WEB/SITES` будут отправлены в Dynatrace, а для всех остальных ресурсов журналы **Informational** и **Warning** будут отфильтрованы.",
    "#### Filter type: `CONTAINS_PATTERN`": "#### Тип фильтра: `CONTAINS_PATTERN`",
    f'This filter type allows you to collect logs containing a particular text. We use fnmatch that provides support for Unix shell–style wildcards. See [Unix filename pattern matching]({TT_FNMATCH}) for details.': f'Данный тип фильтра позволяет собирать журналы, содержащие определённый текст. Используется fnmatch с поддержкой подстановочных знаков в стиле Unix-оболочки. Подробнее см. в разделе [Сопоставление шаблонов имён файлов Unix]({TT_FNMATCH}).',
    "* `FILTER.GLOBAL.CONTAINS_PATTERN=<log_pattern>`": "* `FILTER.GLOBAL.CONTAINS_PATTERN=<log_pattern>`",
    "* `FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<log_pattern>`": "* `FILTER.RESOURCE_TYPE.CONTAINS_PATTERN.<resource_type>=<log_pattern>`",
    "* `FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<log_pattern>`": "* `FILTER.RESOURCE_ID.CONTAINS_PATTERN.<resource_id>=<log_pattern>`",
    "#### Filter group: `GLOBAL`": "#### Группа фильтров: `GLOBAL`",
    "This filter is set for all logs.": "Этот фильтр применяется ко всем журналам.",
    "#### Filter group: `RESOURCE_TYPE`": "#### Группа фильтров: `RESOURCE_TYPE`",
    "This filter is used only for logs coming from resources of the given Azure resource type, such as `Microsoft.Compute/virtualMachines`.": "Данный фильтр применяется только к журналам от ресурсов указанного типа ресурса Azure, например `Microsoft.Compute/virtualMachines`.",
    "You can find the resource type in Azure Portal, in your resource's **Properties**.": "Тип ресурса можно найти в Azure Portal в разделе **Properties** ресурса.",
    "If the **Type** field doesn't appear in **Properties**, you can extract it from the resource ID string.": "Если поле **Type** не отображается в **Properties**, его можно извлечь из строки идентификатора ресурса.",
    "Resource ID string syntax:": "Синтаксис строки идентификатора ресурса:",
    "`/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/<resourceType>/<resourceName>`": "`/subscriptions/<subscriptionId>/resourceGroups/<resourceGroupName>/providers/<resourceType>/<resourceName>`",
    "The resource type will be the part between `/providers/` and `/resourceName/`.": "Тип ресурса: часть строки между `/providers/` и `/resourceName/`.",
    "#### Filter group: `RESOURCE_ID`": "#### Группа фильтров: `RESOURCE_ID`",
    "This filter is used only for logs coming from the given resource that is identified by the Azure resource ID.": "Данный фильтр применяется только к журналам от конкретного ресурса, идентифицируемого по идентификатору ресурса Azure.",
    "You can look for the resource type in Azure Portal, in your resource's **Properties**.": "Тип ресурса можно найти в Azure Portal в разделе **Properties** ресурса.",

    # Filter rules
    "### Filter rules": "### Правила фильтрации",
    "* If you set two filter types for the same group, both conditions need to be met, so the second filter will have to match the first filter.": "* Если для одной группы заданы два типа фильтров, оба условия должны выполняться, поэтому второй фильтр должен соответствовать первому.",
    "For example, if you set `MIN_LOG_LEVEL` to **Warning** and `CONTAINS_PATTERN` to `<some_important_message>`, you will get only **Warning** logs containing `<some_important_message>`, and all other warning logs that don't contain that specific message will be filtered out.": "Например, если задать `MIN_LOG_LEVEL` равным **Warning** и `CONTAINS_PATTERN` равным `<some_important_message>`, будут получены только журналы **Warning**, содержащие `<some_important_message>`, а все прочие журналы предупреждений без этого сообщения будут отфильтрованы.",
    "* If you set one filter type for one group, and another filter type for another group, the two conditions do not overlap.": "* Если задан один тип фильтра для одной группы и другой тип для другой группы, два условия не пересекаются.",
    "For example, if you set `MIN_LOG_LEVEL` to **Warning** for `GLOBAL`, and `CONTAINS_PATTERN` to `<some_important_message>` for `RESOURCE_TYPE`, you will get all **Warning**, **Error**, and **Critical** logs from `GLOBAL`, and all logs containing `<some_important_message>` from `RESOURCE_TYPE`.": "Например, если задать `MIN_LOG_LEVEL` равным **Warning** для `GLOBAL` и `CONTAINS_PATTERN` равным `<some_important_message>` для `RESOURCE_TYPE`, будут получены все журналы **Warning**, **Error** и **Critical** из `GLOBAL`, а также все журналы из `RESOURCE_TYPE`, содержащие `<some_important_message>`.",
    "* If you set more than one pair of filter types (`MIN_LOG_LEVEL` and `CONTAINS_PATTERN`) for the same group (global or resource type/ID), only the last pair of filter types will apply; all the others will be ignored.": "* Если для одной группы (глобальной или типа/идентификатора ресурса) задано несколько пар типов фильтров (`MIN_LOG_LEVEL` и `CONTAINS_PATTERN`), применяется только последняя пара; остальные игнорируются.",

    # Update
    "## Update Azure log forwarding": "## Обновление Azure log forwarding",
    "To update Azure log forwarding": "Обновление Azure log forwarding",
    "1. You need a package that contains the source code of Azure log forwarder—download the latest Dynatrace version.": "1. Потребуется пакет с исходным кодом Azure log forwarder: загрузите последнюю версию Dynatrace.",
    "2. Deploy the new version, making sure to replace the placeholders with the required values.": "2. Разверните новую версию, заменив заполнители требуемыми значениями.",
    f'Some Azure log forwarder releases include changes that require full reinstallation. For more details, refer to the [GitHub releases page]({TT_GH_REL}).': f'Некоторые выпуски Azure log forwarder содержат изменения, требующие полной переустановки. Подробнее см. на [странице выпусков GitHub]({TT_GH_REL}).',

    # Alternative deployments
    "## Alternative deployments": "## Альтернативные варианты развёртывания",
    "### Use existing ActiveGate": "### Использование существующего ActiveGate",
    "If you don't want to use direct ingest through the Cluster API, you have to use an existing ActiveGate for log ingestion.": "Если прямой приём через Cluster API не нужен, для приёма журналов необходимо использовать существующий ActiveGate.",
    "See below for instructions.": "Инструкции приведены ниже.",
    "#### Prerequisites": "#### Предварительные требования",
    "Dynatrace version 1.217+": "Dynatrace версии 1.217+",
    "* [Dynatrace requirements](#dynatrace) listed above": "* [Требования Dynatrace](#dynatrace), перечисленные выше",
    "* [Azure requirements](#azure) listed above": "* [Требования Azure](#azure), перечисленные выше",
    "* [CLI requirements](#cli) listed above": "* [Требования CLI](#cli), перечисленные выше",
    "#### Configuration": "#### Настройка",
    "* For `DEPLOYMENT_NAME`, enter your deployment name (lowercase only).": "* Для `DEPLOYMENT_NAME` укажите имя развёртывания (только строчные буквы).",
    '* For `TARGET_URL`, enter the API URL of your ActiveGate endpoint: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. To learn how to determine your environment ID, see [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Для `TARGET_URL` введите URL API вашего эндпоинта ActiveGate: `https://<your_activegate_IP_or_hostname>:9999/e/<your_environment_ID>`. Чтобы узнать, как определить идентификатор среды, см. [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENV_ID}").',
    "* For `TARGET_API_TOKEN`, enter your API token. For details, see the prerequisites above.": "* Для `TARGET_API_TOKEN` введите токен API. Подробнее см. в предварительных требованиях выше.",
    "* For `USE_EXISTING_ACTIVE_GATE`, enter `true`.": "* Для `USE_EXISTING_ACTIVE_GATE` введите `true`.",
    "* Optional For `REQUIRE_VALID_CERTIFICATE`, enter `true` or `false`. This parameter tells the log forwarder to verify the SSL certificate of your ActiveGate. By default, certificates are validated.": "* Дополнительно Для `REQUIRE_VALID_CERTIFICATE` введите `true` или `false`. Этот параметр указывает log forwarder проверять SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются.",
    "Be sure to check whether you want to set other optional parameters as well. All parameters between brackets (`[...]`) are optional. For details, see [Deploy table](#table).": "Проверьте, нужно ли задать другие дополнительные параметры. Все параметры в скобках (`[...]`) являются необязательными. Подробнее см. в разделе [Таблица развёртывания](#table).",

    # user-assigned managed identity
    "### Use a user-assigned managed identity": "### Использование user-assigned managed identity",
    "There are two managed identity types: system-assigned and user-assigned. By default, a system-assigned managed identity is used. If you prefer to use a user-assigned managed identity, see below for instructions.": "Существует два типа managed identity: system-assigned и user-assigned. По умолчанию используется system-assigned managed identity. Если предпочтительнее использовать user-assigned managed identity, инструкции приведены ниже.",
    f'In addition to the [Azure requirements](#azure) listed above, you should also create a user-assigned managed identity in Azure Portal.': "Помимо [требований Azure](#azure), перечисленных выше, необходимо создать user-assigned managed identity в Azure Portal.",
    "Add Event Hubs roles in the user-assigned managed identity. For the event hub trigger binding, you need to assign corresponding built-in roles. The built-in roles are **Azure Event Hubs Data Receiver** and **Azure Event Hubs Data Owner**.": "Добавьте роли Event Hubs в user-assigned managed identity. Для привязки триггера концентратора событий необходимо назначить соответствующие встроенные роли: **Azure Event Hubs Data Receiver** и **Azure Event Hubs Data Owner**.",
    "* For `EVENT_HUB_NAME`, enter the name of the Azure Event Hubs instances configured for receiving logs. See [Azure requirements](#azure) for details.": "* Для `EVENT_HUB_NAME` введите имя экземпляров Azure Event Hubs, настроенных для приёма журналов. Подробнее см. в разделе [Требования Azure](#azure).",
    "* For `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY`, enter `true`. This parameter is used to determine if a user-assigned managed identity is used instead of system assigned.": "* Для `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` введите `true`. Этот параметр определяет, используется ли user-assigned managed identity вместо system-assigned.",
    "* For `EVENT_HUB_CONNECTION_CLIENT_ID`, enter the `Client ID` of the created managed identity.": "* Для `EVENT_HUB_CONNECTION_CLIENT_ID` введите `Client ID` созданного managed identity.",
    "* For `MANAGED_IDENTITY_RESOURCE_NAME`, enter the resource name of the created managed identity.": "* Для `MANAGED_IDENTITY_RESOURCE_NAME` введите имя ресурса созданного managed identity.",
    "* For `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE`, enter:": "* Для `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` введите:",
    "+ The `Host name` of the Event Hubs namespace.": "+ `Host name` пространства имён Event Hubs.",
    "+ The custom name of the default consumer group.": "+ Пользовательское имя группы потребителей по умолчанию.",
    '* For `TARGET_URL`, enter your environment URL: `https://{your-domain}/e/{your-environment-id}/e/{your-environment-id}/`. To learn how to determine your environment ID for a Managed deployment, see [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Для `TARGET_URL` укажите URL среды: `https://{{your-domain}}/e/{{your-environment-id}}/e/{{your-environment-id}}/`. Чтобы узнать, как определить идентификатор среды для развёртывания Managed, см. [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENV_ID}").',
    "* For `RESOURCE_GROUP`, enter the name of the Azure resource group in which deployment will run. See [Azure requirements](#azure) for details.": "* Для `RESOURCE_GROUP` введите имя группы ресурсов Azure, в которой будет выполняться развёртывание. Подробнее см. в разделе [Требования Azure](#azure).",
    "* Optional For `REQUIRE_VALID_CERTIFICATE`, enter `true` or `false`. This parameter tells the log forwarder to verify the SSL certificate of your ActiveGate. By default, certificates are validated.": "* Дополнительно Для `REQUIRE_VALID_CERTIFICATE` введите `true` или `false`. Этот параметр указывает log forwarder проверять SSL-сертификат вашего ActiveGate. По умолчанию сертификаты проверяются.",

    # Deploy table
    "### Deploy table": "### Таблица развёртывания",
    "For a complete list of parameters, see the deploy table below.": "Полный список параметров см. в таблице развёртывания ниже.",
    "| **Command-line parameter** | **Environment variable** | **Description** |  |": "| **Параметр командной строки** | **Переменная среды** | **Описание** |  |",
    "| --- | --- | --- | --- |": "| --- | --- | --- | --- |",
    "| `--deployment-name` | `DEPLOYMENT_NAME` | Required Your deployment name. Lowercase only. |  |": "| `--deployment-name` | `DEPLOYMENT_NAME` | Обязательно Имя развёртывания. Только строчные буквы. |  |",
    "| `--target-url` | `TARGET_URL` | Required Your Dynatrace environment where you want to set up generic log ingestion. |  |": "| `--target-url` | `TARGET_URL` | Обязательно Среда Dynatrace, в которой требуется настроить универсальный приём журналов. |  |",
    "| `--target-api-token` | `TARGET_API_TOKEN` | Required Your API token. |  |": "| `--target-api-token` | `TARGET_API_TOKEN` | Обязательно Ваш токен API. |  |",
    "| `--resource-group` | `RESOURCE_GROUP` | Required Name of the Azure resource group in which the deployment will run. |  |": "| `--resource-group` | `RESOURCE_GROUP` | Обязательно Имя группы ресурсов Azure, в которой будет выполняться развёртывание. |  |",
    "| `--event-hub-connection-string` | `EVENT_HUB_CONNECTION_STRING` | Required The connection string for the Azure Event Hubs instance configured for receiving logs. (Azure Event Hubs name that is configured for receiving logs.) |  |": "| `--event-hub-connection-string` | `EVENT_HUB_CONNECTION_STRING` | Обязательно Строка подключения для экземпляра Azure Event Hubs, настроенного для приёма журналов. (Имя Azure Event Hubs, настроенного для приёма журналов.) |  |",
    "| `--event-hub-name` | `EVENT_HUB_NAME` | Optional Optional by default. If a user-assigned managed identity is your method of authentication, then Required. |  |": "| `--event-hub-name` | `EVENT_HUB_NAME` | Дополнительно По умолчанию необязательно. Обязательно, если для аутентификации используется user-assigned managed identity. |  |",
    "| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Optional If set to `true`, the log forwarder verifies the SSL certificate of your ActiveGate. By default, certificates are validated. |  |": "| `--require-valid-certificate` | `REQUIRE_VALID_CERTIFICATE` | Дополнительно При значении `true` log forwarder проверяет SSL-сертификат ActiveGate. По умолчанию сертификаты проверяются. |  |",
    "| `--enable-self-monitoring` | `SFM_ENABLED` | Optional If set to `true`, Dynatrace sends custom metrics to Azure. See [Enable self-monitoring](#sfm) for details. By default, custom metrics aren't sent to Azure. |  |": "| `--enable-self-monitoring` | `SFM_ENABLED` | Дополнительно При значении `true` Dynatrace отправляет пользовательские метрики в Azure. Подробнее см. в разделе [Включение самомониторинга](#sfm). По умолчанию пользовательские метрики в Azure не отправляются. |  |",
    "| `--filter-config` | `FILTER_CONFIG` | Optional Apply filters to reduce the number of logs sent to Dynatrace. See [Log filtering](#filter) for details. |  |": "| `--filter-config` | `FILTER_CONFIG` | Дополнительно Применение фильтров для сокращения числа журналов, отправляемых в Dynatrace. Подробнее см. в разделе [Фильтрация журналов](#filter). |  |",
    '| `--tags` | `TAGS` | Optional Apply Azure tags to newly created resources in comma-separated key:value pair format (for example, `"tag:value,tag2:value2"`). The following characters are not supported in a tag key: `,:<>%&\\?/` |  |': '| `--tags` | `TAGS` | Дополнительно Применение тегов Azure к новым ресурсам в формате пар «ключ:значение» через запятую (например, `"tag:value,tag2:value2"`). Следующие символы не поддерживаются в ключе тега: `,:<>%&\\?/` |  |',
    "| `--enable-user-assigned-managed-identity` | `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` | Optional If set to `true`, options `--eventhub-connection-client-id`, `--managed-identity-resource-name`, `--eventhub-connection-fully-qualified-namespace`, `--event-hub-name` are Required. Enables usage of a user-assigned managed identity instead of a system-assigned managed identity. |  |": "| `--enable-user-assigned-managed-identity` | `ENABLE_USER_ASSIGNED_MANAGED_IDENTITY` | Дополнительно При значении `true` параметры `--eventhub-connection-client-id`, `--managed-identity-resource-name`, `--eventhub-connection-fully-qualified-namespace`, `--event-hub-name` становятся обязательными. Включает использование user-assigned managed identity вместо system-assigned managed identity. |  |",
    "| `--custom-consumer-group` | `CONSUMER_GROUP` | Optional If provided, this value will be used as the name of a default consumer group. Leave empty to apply the default Azure value. |  |": "| `--custom-consumer-group` | `CONSUMER_GROUP` | Дополнительно Если указано, это значение будет использоваться как имя группы потребителей по умолчанию. Оставьте пустым для применения значения Azure по умолчанию. |  |",
    "| `--eventhub-connection-client-id` | `EVENT_HUB_CONNECTION_CLIENT_ID` | Optional `Client ID` of the created managed identity. Example value: `d8916c27-4c4r-482o-895b-doe0b48c76f7` |  |": "| `--eventhub-connection-client-id` | `EVENT_HUB_CONNECTION_CLIENT_ID` | Дополнительно `Client ID` созданного managed identity. Пример значения: `d8916c27-4c4r-482o-895b-doe0b48c76f7` |  |",
    "| `--managed-identity-resource-name` | `MANAGED_IDENTITY_RESOURCE_NAME` | Optional Resource name of the created managed identity. Example value: `test-managed-identity` |  |": "| `--managed-identity-resource-name` | `MANAGED_IDENTITY_RESOURCE_NAME` | Дополнительно Имя ресурса созданного managed identity. Пример значения: `test-managed-identity` |  |",
    "| `--eventhub-connection-fully-qualified-namespace` | `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` | Optional `Host name` of the Azure Event Hubs namespace. Example value: `sample-eventhub-namespace.servicebus.windows.net` |  |": "| `--eventhub-connection-fully-qualified-namespace` | `EVENT_HUB_CONNECTION_FULLY_QUALIFIED_NAMESPACE` | Дополнительно `Host name` пространства имён Azure Event Hubs. Пример значения: `sample-eventhub-namespace.servicebus.windows.net` |  |",

    # Verification
    "## Verification": "## Проверка",
    "To verify if the deployment was successful, in Dynatrace, go to **Logs** and confirm that the following log line is present:": "Чтобы убедиться в успешном развёртывании, откройте в Dynatrace **Logs** и убедитесь, что присутствует следующая строка журнала:",
    "![Log line](https://dt-cdn.net/images/screenshot-2022-08-11-at-11-49-52-928-5957a24948.png)": "![Строка журнала](https://dt-cdn.net/images/screenshot-2022-08-11-at-11-49-52-928-5957a24948.png)",
    "Log line": "Строка журнала",
    "In around 10 minutes, further logs should start coming in. If no logs are coming in, make sure that:": "Примерно через 10 минут должны начать поступать дополнительные журналы. Если журналы не поступают, проверьте следующее:",
    "* The Event Hubs instances and the resource group in which the deployment will run are in the same region": "* Экземпляры Event Hubs и группа ресурсов, в которой выполняется развёртывание, находятся в одном регионе",
    f'* You carefully followed the steps to [Configure diagnostic settings]({TT_DIAG})': f'* Вы тщательно выполнили шаги по [настройке параметров диагностики]({TT_DIAG})',
    f'Furthermore, you can read Azure Function logs in which the Azure-log-forwarder is running. [Enable streaming execution logs in Azure Functions]({TT_STREAM_LOGS})': f'Кроме того, можно просмотреть журналы Azure Function, в которой запущен Azure-log-forwarder. [Включение потокового вывода журналов выполнения в Azure Functions]({TT_STREAM_LOGS})',
    "SNAT port exhaustion: Azure Functions have a limited number of ports that can be opened at a time (128). The number of instances, the number of worker processes, and the number of concurrent calls are the factors that contribute to the open connections. If the limit is reached, see the [scaling guide](#scalingguide) below.": "Исчерпание портов SNAT: Azure Functions имеют ограниченное количество портов, которые можно открыть одновременно (128). Число экземпляров, рабочих процессов и параллельных вызовов влияет на количество открытых соединений. При достижении лимита см. [руководство по масштабированию](#scalingguide) ниже.",

    # Check your version
    "## Check your version": "## Проверка версии",
    "To check the version of the currently deployed Azure log forwarder": "Проверка версии текущего развёрнутого Azure log forwarder",
    "1. Open Azure Portal and go to **Subscriptions**.": "1. Откройте Azure Portal и перейдите в раздел **Subscriptions**.",
    "2. Select your subscription.": "2. Выберите вашу подписку.",
    "3. Go to **Resource groups**.": "3. Перейдите в **Resource groups**.",
    "4. Choose the resource group that contains the function.": "4. Выберите группу ресурсов, содержащую функцию.",
    "5. Choose your deployed function app.": "5. Выберите развёрнутое приложение-функцию.",
    "6. Select **log\\_ingest** on the **Functions** tab.": "6. Выберите **log\\_ingest** на вкладке **Functions**.",
    "7. Select **Code + Test** from the **Developer** menu on the left.": "7. Выберите **Code + Test** в меню **Developer** слева.",
    "8. Select the dropdown file selector (`main.py` is selected by default).": "8. Откройте раскрывающийся список выбора файла (по умолчанию выбран `main.py`).",
    "9. Choose `version.txt`.": "9. Выберите `version.txt`.",
    "10. Open the file to check your currently deployed version.": "10. Откройте файл для просмотра текущей развёрнутой версии.",

    # Scaling guide
    "## Scaling guide": "## Руководство по масштабированию",
    "The recommended way of scaling up the default throughput of 70 MB/min is to upgrade the App Service plan, increase the number of App Service instances respectively, increase `FUNCTIONS_WORKER_PROCESS_COUNT` (default is 1), increase `NUMBER_OF_CONCURRENT_SEND_CALLS` (default is 2). You can add `FUNCTIONS_WORKER_PROCESS_COUNT` and `NUMBER_OF_CONCURRENT_SEND_CALLS` as **New application setting** in Azure Portal (**Azure function** > **Configuration** > **New application setting**).": "Рекомендуемый способ увеличения пропускной способности по умолчанию (70 МБ/мин): перейдите на более высокий App Service plan, увеличьте число экземпляров App Service, увеличьте `FUNCTIONS_WORKER_PROCESS_COUNT` (по умолчанию 1), увеличьте `NUMBER_OF_CONCURRENT_SEND_CALLS` (по умолчанию 2). Параметры `FUNCTIONS_WORKER_PROCESS_COUNT` и `NUMBER_OF_CONCURRENT_SEND_CALLS` можно добавить как **New application setting** в Azure Portal (**Azure function** > **Configuration** > **New application setting**).",
    "Please note that the performance of the log forwarder may vary depending on the log content (size/ processing complexity).": "Обратите внимание, что производительность log forwarder может варьироваться в зависимости от содержимого журналов (размера и сложности обработки).",
    "| **Maximum throughput** | **App Service Plan** | **Number of instances** | **Configuration** |": "| **Максимальная пропускная способность** | **App Service Plan** | **Число экземпляров** | **Конфигурация** |",
    "| up to `70 MB/minute` (up to 4 GB/hour) | `S1` | `1` | no configuration |": "| до `70 МБ/мин` (до 4 ГБ/ч) | `S1` | `1` | без конфигурации |",
    "| up to `580 MB/minute` (up to 32 GB/hour) | `P1V3` | `1` | FUNCTIONS\\_WORKER\\_PROCESS\\_COUNT: 4, NUMBER\\_OF\\_CONCURRENT\\_SEND\\_CALLS: 5 |": "| до `580 МБ/мин` (до 32 ГБ/ч) | `P1V3` | `1` | FUNCTIONS\\_WORKER\\_PROCESS\\_COUNT: 4, NUMBER\\_OF\\_CONCURRENT\\_SEND\\_CALLS: 5 |",
    "| up to `1 GB/minute` (up to 60 GB/hour) | `P2V3` | `1` | FUNCTIONS\\_WORKER\\_PROCESS\\_COUNT: 8, NUMBER\\_OF\\_CONCURRENT\\_SEND\\_CALLS: 5 |": "| до `1 ГБ/мин` (до 60 ГБ/ч) | `P2V3` | `1` | FUNCTIONS\\_WORKER\\_PROCESS\\_COUNT: 8, NUMBER\\_OF\\_CONCURRENT\\_SEND\\_CALLS: 5 |",
    "| up to `2.3 GB/minute` (up to 138 GB/hour) | `P2V3` | `3` | FUNCTIONS\\_WORKER\\_PROCESS\\_COUNT: 8, NUMBER\\_OF\\_CONCURRENT\\_SEND\\_CALLS: 5 |": "| до `2,3 ГБ/мин` (до 138 ГБ/ч) | `P2V3` | `3` | FUNCTIONS\\_WORKER\\_PROCESS\\_COUNT: 8, NUMBER\\_OF\\_CONCURRENT\\_SEND\\_CALLS: 5 |",
    "As a last resort, scale horizontally: deploy more integrations and distribute the logs' load into different Event Hubs instances.": "В крайнем случае выполните горизонтальное масштабирование: разверните дополнительные интеграции и распределите нагрузку журналов между разными экземплярами Event Hubs.",

    # Uninstall
    "## Uninstall Azure log forwarding": "## Удаление Azure log forwarding",
    "To uninstall the Dynatrace Azure log forwarder": "Удаление Dynatrace Azure log forwarder",
    "1. In Azure Portal, go to the resource group used for installation.": "1. В Azure Portal перейдите в группу ресурсов, использовавшуюся при установке.",
    "2. Filter resources by tag.": "2. Отфильтруйте ресурсы по тегу.",
    "The deployment script tags all created resources with `LogsForwarderDeployment = <your_deployment_name>`.": "Скрипт развёртывания помечает все созданные ресурсы тегом `LogsForwarderDeployment = <your_deployment_name>`.",
    "3. Delete the resources.": "3. Удалите ресурсы.",

    # Related topics
    "## Related topics": "## Связанные темы",
    '* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")': f'* [Интеграции с Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "{TT_AZURE_INT}")',
    f'* [Azure Log Forwarder Troubleshooting]({TT_COMMUNITY})': f'* [Устранение неполадок Azure Log Forwarder]({TT_COMMUNITY})',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "set-up-log-forwarder-azure.md", TRANS, PASS)
    qa_one(REL, "set-up-log-forwarder-azure.md")
