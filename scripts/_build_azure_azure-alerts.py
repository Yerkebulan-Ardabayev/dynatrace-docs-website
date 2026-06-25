# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide"

# Curly apostrophe (U+2019) and em-dash (U+2014) — formatter strips them from string
# literals, so build the two affected norm-keys programmatically.
_CURL = "’"  # '
_EMDASH = "—"  # —
_K_AG = (
    "The ActiveGate designated to consume Azure Monitor alerts doesn"
    + _CURL
    + "t have to be the same ActiveGate that runs the Azure Monitor integration."
    " It can be any other [Azure monitoring-enabled ActiveGate]"
    "(/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod"
    ' "Learn which ActiveGate properties you can configure based on your needs and requirements.")'
    "."
)
_K_DDU = (
    "Currently, the events/alerts ingested via Azure Monitor alerts webhook don"
    + _CURL
    + "t consume DDUs"
    + _EMDASH
    + "although, it might change in the future."
)


TT_AZMON = "Настройка и конфигурирование мониторинга Azure в Dynatrace."
TT_STEP = (
    "Интеграция с Azure Monitor alerts и поддерживаемые типы оповещений Azure Monitor"
)
TT_AG = "Узнайте, какие свойства ActiveGate можно настроить в зависимости от потребностей и требований."
_V_AG = (
    "ActiveGate, выделенный для приёма Azure Monitor alerts, не обязан совпадать"
    " с ActiveGate, выполняющим интеграцию с Azure Monitor. Это может быть любой"
    " другой [ActiveGate с поддержкой мониторинга Azure]"
    "(/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#azure_mod"
    ' "{ag}").'
).format(ag=TT_AG)
TT_SSL = "Узнайте, как настроить SSL-сертификат на ActiveGate."
TT_AZINT = "Настройка глубокого мониторинга кода Dynatrace в Azure с помощью OneAgent или OpenTelemetry."
TT_EVENTS = "Узнайте о различных категориях событий и поддерживаемых типах событий, их уровнях серьёзности и логике их возникновения."

TRANS = {
    "title: Set up monitoring notifications with Azure Monitor alerts": "title: Настройка уведомлений мониторинга с Azure Monitor alerts",
    "# Set up monitoring notifications with Azure Monitor alerts": "# Настройка уведомлений мониторинга с Azure Monitor alerts",
    "* How-to guide": "* Практическое руководство",
    "* 5-min read": "* Чтение: 5 мин",
    "* Updated on Jan 28, 2026": "* Обновлено 28 января 2026 г.",
    f'After [setting up Azure Monitor integration](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace."), you can start setting up monitoring notifications with Azure Monitor alerts.': f'После [настройки интеграции с Azure Monitor](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "{TT_AZMON}") можно приступить к настройке уведомлений мониторинга с Azure Monitor alerts.',
    "Azure Monitor alerts is a unified notification hub for all types of important conditions found in Azure monitoring data. The integration of Azure Monitor alerts enables you to consume alerts, which are automatically transformed into events that are leveraged by Davis AI for deeper insights.": "Azure Monitor alerts, единый центр уведомлений для всех типов важных условий, обнаруженных в данных мониторинга Azure. Интеграция Azure Monitor alerts позволяет принимать оповещения, которые автоматически преобразуются в события, используемые Davis AI для более глубокого анализа.",
    "To set up monitoring notifications with Azure Monitor alerts, complete the following steps.": "Чтобы настроить уведомления мониторинга с Azure Monitor alerts, выполните следующие шаги.",
    f'[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")': f'[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")',
    f'**Create an API token**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-1 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")': f'**Создание API-токена**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-1 "{TT_STEP}")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")',
    f'**Configure one or more designated ActiveGates**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-2 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")': f'**Настройка одного или нескольких выделенных ActiveGates**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-2 "{TT_STEP}")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")',
    f'**Configure Azure Monitor alerts via webhook**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-3 "Integration with Azure Monitor alerts and supported Azure Monitor alerts types")': f'**Настройка Azure Monitor alerts через webhook**](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/set-up-monitoring-with-azure-alerts#step-3 "{TT_STEP}")',
    "## Step 1 Create an API token": "## Шаг 1. Создание API-токена",
    "To generate an API token": "Чтобы создать API-токен",
    "1. Go to **Access Tokens**.": "1. Откройте **Access Tokens**.",
    "2. Select **Generate new token**.": "2. Нажмите **Generate new token**.",
    "3. Enter a name for your token.": "3. Введите имя для токена.",
    "4. Find and select the **Ingest metrics** scope.": "4. Найдите и выберите область **Ingest metrics**.",
    "5. Select **Generate token**.": "5. Нажмите **Generate token**.",
    "6. Select **Copy** to copy the generated token to the clipboard. Store the token in a password manager for future use.": "6. Нажмите **Copy**, чтобы скопировать созданный токен в буфер обмена. Сохраните токен в менеджере паролей для дальнейшего использования.",
    "You can assign multiple permissions to a single token, or you can generate several tokens, each with different access levels, and use them accordingly. Check your organization's security policies for best practices.": "Одному токену можно назначить несколько разрешений или создать несколько токенов с разными уровнями доступа и использовать их соответствующим образом. Ознакомьтесь с политиками безопасности своей организации для получения рекомендаций.",
    "## Step 2 Configure one or more designated ActiveGates": "## Шаг 2. Настройка одного или нескольких выделенных ActiveGates",
    _K_AG: _V_AG,
    "To configure a designated ActiveGate to consume Azure Monitor alerts:": "Чтобы настроить выделенный ActiveGate для приёма Azure Monitor alerts:",
    f'1. Configure a valid TLS certificate (not a self-signed certificate) for the ActiveGate to communicate via HTTPS. Ensure that the root certificate is accepted by Azure. For details, see [how to configure custom SSL certificate for an ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").': f'1. Настройте действительный TLS-сертификат (не самоподписанный) для ActiveGate для обмена данными по HTTPS. Убедитесь, что корневой сертификат принят Azure. Подробнее см. в разделе [о настройке пользовательского SSL-сертификата для ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "{TT_SSL}").',
    "2. Add the following lines to your ActiveGate `custom.properties` file and restart the ActiveGate after applying the configuration.": "2. Добавьте следующие строки в файл `custom.properties` своего ActiveGate и перезапустите ActiveGate после применения конфигурации.",
    "3. Give access to ActiveGate for Azure Monitor alerts source IP addresses.": "3. Предоставьте ActiveGate доступ к IP-адресам источника Azure Monitor alerts.",
    f"For more details, see [source IP address ranges](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook) in Azure documentation.": f"Подробнее см. в разделе [диапазоны IP-адресов источника](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook) в документации Azure.",
    "## Step 3 Configure Azure Monitor alerts via webhook": "## Шаг 3. Настройка Azure Monitor alerts через webhook",
    _K_DDU: "В настоящее время события/оповещения, поступающие через webhook Azure Monitor alerts, не потребляют DDU, хотя в будущем это может измениться.",
    "Azure Monitor alerts consumed via webhooks are configured in your Azure Alert Rules.": "Azure Monitor alerts, принимаемые через webhooks, настраиваются в правилах оповещений Azure.",
    "The alerts are mapped to the closest known matching entity. This means that they either map to their related Azure resource entity or, as a fallback, to the Azure subscription of the resource.": "Оповещения сопоставляются с наиболее близкой известной сущностью. Это означает, что они либо сопоставляются с соответствующей сущностью ресурса Azure, либо, в качестве запасного варианта, с подпиской Azure для данного ресурса.",
    "To configure Azure Monitor alerts via webhook, you need to create an alert rule and an action group that will trigger a webhook.": "Чтобы настроить Azure Monitor alerts через webhook, нужно создать правило оповещения и группу действий, которая будет запускать webhook.",
    "1. In Azure Portal, go to **Home** > **Monitor** > **Alerts** > **Create** > **Alert rule**.": "1. В Azure Portal откройте **Home** > **Monitor** > **Alerts** > **Create** > **Alert rule**.",
    "2. Select **Scope** > **Select scope**.": "2. Выберите **Scope** > **Select scope**.",
    "3. Filter for and select the resource you want to monitor, and then select **Done**.": "3. Отфильтруйте и выберите ресурс для мониторинга, затем нажмите **Done**.",
    "4. Select **Condition** > **Add condition**.": "4. Выберите **Condition** > **Add condition**.",
    "5. Filter for, select, and customize the signal type that will trigger your alert.": "5. Отфильтруйте, выберите и настройте тип сигнала, который будет запускать оповещение.",
    "6. Select **Next: Actions** > **Create action group**.": "6. Выберите **Next: Actions** > **Create action group**.",
    "7. Enter the **subscription** that will manage the deployed resources and costs, the **resource group** to which the subscription belongs, and the name (and display name) for the **action group**.": "7. Введите **subscription**, которая будет управлять развёрнутыми ресурсами и расходами, **resource group**, к которой относится подписка, а также имя (и отображаемое имя) для **action group**.",
    "8. Select **Actions** and enter the following values:": "8. Выберите **Actions** и введите следующие значения:",
    "* For **Action type**, select **Webhook** and enter a name.": "* Для **Action type** выберите **Webhook** и введите имя.",
    "* For **URI**, enter `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/modules/azure_monitoring/alerts_webhook?token=<YOUR_API_TOKEN>`, making sure to replace `<YOUR_ACTIVEGATE_ADDRESS>` and `<YOUR_API_TOKEN>` with your own values.": "* Для **URI** введите `https://<YOUR_ACTIVEGATE_ADDRESS>:9999/modules/azure_monitoring/alerts_webhook?token=<YOUR_API_TOKEN>`, заменив `<YOUR_ACTIVEGATE_ADDRESS>` и `<YOUR_API_TOKEN>` своими значениями.",
    "9. Leave the common alert schema disabled, and then select **OK**.": "9. Оставьте общую схему оповещений отключённой и нажмите **OK**.",
    "The common alert schema is not supported.": "Общая схема оповещений не поддерживается.",
    "10. Select **Review and create** > **Create**.": "10. Нажмите **Review and create** > **Create**.",
    "After the action group is created, you can view and edit it in **Alerts** > **Action groups**.": "После создания группы действий её можно просмотреть и изменить в **Alerts** > **Action groups**.",
    f"For more information, see [Webhook rules in Azure documentation](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook).": f"Подробнее см. в разделе [Правила Webhook в документации Azure](https://docs.microsoft.com/en-us/azure/azure-monitor/platform/action-groups#webhook).",
    "## Alert types": "## Типы оповещений",
    "The following alert types are supported.": "Поддерживаются следующие типы оповещений.",
    "### Metric alerts": "### Метрические оповещения",
    "Metric alerts are complementary to Dynatrace integration of Azure Monitor metrics.": "Метрические оповещения дополняют интеграцию Dynatrace с метриками Azure Monitor.",
    "Metric alerts enable you to retrieve metric-based events without the need to push the metrics to Dynatrace. This is helpful in reducing API and network pressure, especially in cases where you might not need the metric (for example, for charting purposes).": "Метрические оповещения позволяют получать события на основе метрик без необходимости передавать метрики в Dynatrace. Это помогает снизить нагрузку на API и сеть, особенно в случаях, когда метрика не нужна (например, для построения графиков).",
    "The event type is defined based on alert **Severity**:": "Тип события определяется на основе **Severity** оповещения:",
    "* **Sev-0 (Critical)**: `ERROR_EVENT`": "* **Sev-0 (Critical)**: `ERROR_EVENT`",
    "* **Sev-1 (Error)**: `PERFORMANCE_EVENT`": "* **Sev-1 (Error)**: `PERFORMANCE_EVENT`",
    "* **Sev-2 (Warning)**: `RESOURCE_CONTENTION_EVENT`": "* **Sev-2 (Warning)**: `RESOURCE_CONTENTION_EVENT`",
    "* **Default (Informational)**: `CUSTOM_ANNOTATION`": "* **Default (Informational)**: `CUSTOM_ANNOTATION`",
    "### Activity log alerts": "### Оповещения журнала активности",
    "Dynatrace supports three types of activity notifications.": "Dynatrace поддерживает три типа уведомлений об активности.",
    "#### Activity log resource health": "#### Работоспособность ресурса в журнале активности",
    "The event type is defined based on severity **Level**:": "Тип события определяется на основе **Level** серьёзности:",
    "* **Critical**: `AVAILABILITY_EVENT`": "* **Critical**: `AVAILABILITY_EVENT`",
    "* **Error**: `AVAILABILITY_EVENT`": "* **Error**: `AVAILABILITY_EVENT`",
    "* **Default**: `CUSTOM_ANNOTATION`": "* **Default**: `CUSTOM_ANNOTATION`",
    f"See [Configure resource health alerts using Azure portal](https://docs.microsoft.com/en-us/azure/service-health/resource-health-alert-monitor-guide) in Azure documentation for more information.": f"Подробнее см. в разделе [Настройка оповещений о работоспособности ресурса с помощью портала Azure](https://docs.microsoft.com/en-us/azure/service-health/resource-health-alert-monitor-guide) в документации Azure.",
    "#### Activity log service health": "#### Работоспособность сервиса в журнале активности",
    "The event type is defined based on **IncidentType**": "Тип события определяется на основе **IncidentType**",
    "* Case **ActionRequired**: `ERROR_EVENT`": "* Case **ActionRequired**: `ERROR_EVENT`",
    "* Case **Incident** or **Security**:": "* Case **Incident** or **Security**:",
    "+ Level **Error**: `ERROR_EVENT`": "+ Level **Error**: `ERROR_EVENT`",
    "+ Level **Info** or **Warning**: `CUSTOM_ANNOTATION`": "+ Level **Info** or **Warning**: `CUSTOM_ANNOTATION`",
    "* Case **Maintenance** or **Information**: `CUSTOM_ANNOTATION`": "* Case **Maintenance** or **Information**: `CUSTOM_ANNOTATION`",
    "Root cause analysis": "Анализ первопричины",
    "Events with `Properties.stage=RCA` are skipped. We don't support stage RCA for service health.": "События с `Properties.stage=RCA` пропускаются. Стадия RCA для работоспособности сервиса не поддерживается.",
    f"See [Create activity log alerts on service notifications using the Azure portal](https://docs.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal) in Azure documentation for more information.": f"Подробнее см. в разделе [Создание оповещений журнала активности об уведомлениях сервиса с помощью портала Azure](https://docs.microsoft.com/en-us/azure/service-health/alerts-activity-log-service-notifications-portal) в документации Azure.",
    "#### Activity log administrative": "#### Административные записи журнала активности",
    "## Related topics": "## Связанные темы",
    f'* [Microsoft Azure Integrations](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")': f'* [Интеграции с Microsoft Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations "{TT_AZINT}")',
    f'* [Event categories](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them.")': f'* [Категории событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "{TT_EVENTS}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "set-up-monitoring-with-azure-alerts.md", TRANS, PASS)
    qa_one(REL, "set-up-monitoring-with-azure-alerts.md")
