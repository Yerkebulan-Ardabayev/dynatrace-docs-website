# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide/limit-api-calls-to-azure.md"""

import os, sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide"

TRANS = {
    "title: Limit API calls to Azure": "title: Ограничение вызовов API к Azure",
    "# Limit API calls to Azure": "# Ограничение вызовов API к Azure",
    "* Explanation": "* Пояснение",
    "* 3-min read": "* Чтение: 3 мин",
    "* Updated on Oct 09, 2025": "* Обновлено 9 октября 2025 г.",
    "When monitoring large Azure environments (thousands of resources per Azure subscription), there is a risk that Dynatrace will reach Azure API throttling limits. Follow this guide to limit API calls to Azure and help to guarantee full Azure monitoring.": "При мониторинге крупных сред Azure (тысячи ресурсов на подписку Azure) существует риск достижения лимитов регулирования Azure API. Следуйте этому руководству, чтобы ограничить вызовы API к Azure и обеспечить полноценный мониторинг Azure.",
    "## Azure throttling limits": "## Лимиты регулирования Azure",
    "There are two types of Azure throttled requests that we need to take into account:": "Существует два типа регулируемых запросов Azure, которые необходимо принимать во внимание:",
    "1. [Throttled requests in Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling#subscription-and-tenant-limits)—Azure throttles subscription-level and tenant-level read operations.": "1. [Регулируемые запросы в Resource Manager](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/request-limits-and-throttling#subscription-and-tenant-limits): Azure регулирует операции чтения на уровне подписки и тенанта.",
    "* Dynatrace uses Azure Resource Manager queries to collect built-in services and metrics for all services.": "* Dynatrace использует запросы Azure Resource Manager для сбора встроенных сервисов и метрик для всех сервисов.",
    "2. [Throttled requests in Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/guidance-for-throttled-requests#understand-throttling-headers)": "2. [Регулируемые запросы в Azure Resource Graph](https://learn.microsoft.com/en-us/azure/governance/resource-graph/concepts/guidance-for-throttled-requests#understand-throttling-headers)",
    "* Dynatrace uses Azure Resource Graph queries to collect all services that are not built-in.": "* Dynatrace использует запросы Azure Resource Graph для сбора всех сервисов, не являющихся встроенными.",
    "## Dynatrace Azure anti-throttling mechanism": "## Механизм защиты Dynatrace от регулирования Azure",
    "Dynatrace collects Azure resources and metrics every 5 min by default to avoid making API calls every minute. However, the frequency of polling depends on the Azure throttling limit.": "По умолчанию Dynatrace собирает ресурсы и метрики Azure каждые 5 минут, чтобы не выполнять вызовы API ежеминутно. Частота опроса зависит от лимита регулирования Azure.",
    "Dynatrace calculates how many requests need to be sent to Azure during the upcoming hour. If the number of expected requests exceeds the configured throttling limit (12,000 requests/hour), Dynatrace changes the polling frequency to collect data with an interval of no more than 15 minutes.": "Dynatrace рассчитывает, сколько запросов необходимо отправить в Azure в течение предстоящего часа. Если ожидаемое число запросов превышает настроенный лимит регулирования (12 000 запросов/час), Dynatrace изменяет частоту опроса, чтобы собирать данные с интервалом не более 15 минут.",
    "## How to avoid Azure throttling": "## Как избежать регулирования Azure",
    "To provide full Dynatrace monitoring, it is important to avoid Azure throttling limits. To decrease API calls to Azure, you can do one of the following.": "Для обеспечения полноценного мониторинга Dynatrace важно не превышать лимиты регулирования Azure. Чтобы уменьшить количество вызовов API к Azure, можно выполнить одно из следующих действий.",
    "* Adjust the Azure service principal configuration to your environment on the Azure side.": "* Скорректировать конфигурацию Azure service principal в соответствии со своей средой на стороне Azure.",
    "* Limit the number of monitored resources using monitoring by tags on the Dynatrace side.": "* Ограничить количество отслеживаемых ресурсов с помощью мониторинга по тегам на стороне Dynatrace.",
    "See below for details.": "Подробности см. ниже.",
    "### Azure service principal configuration": "### Конфигурация Azure service principal",
    "You have three options to configure [Azure service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals), depending on your Azure environment.": "Существует три варианта настройки [Azure service principal](https://docs.microsoft.com/en-us/azure/active-directory/develop/app-objects-and-service-principals) в зависимости от среды Azure.",
    "* Recommended One Azure service principal - one Azure subscription": "* Рекомендуется: один Azure service principal - одна подписка Azure",
    "+ Throttling limit: 12,000 requests/hour per Azure subscription": "+ Лимит регулирования: 12 000 запросов/час на подписку Azure",
    "* One big Azure subscription that exceeds the throttling limit": "* Одна большая подписка Azure, превышающая лимит регулирования",
    "Split monitoring between Azure service principals:": "Распределите мониторинг между Azure service principals:",
    "+ You can create several Azure service principals for the same Azure subscription setting the `--scope` of each service principal to separate Azure resource groups.": "+ Можно создать несколько Azure service principals для одной подписки Azure, задав для каждого service principal параметр `--scope` в виде отдельных групп ресурсов Azure.",
    "Copy the following command and edit it to replace the placeholders with actual values as described below.": "Скопируйте следующую команду и отредактируйте её, заменив заполнители фактическими значениями, как описано ниже.",
    "Be sure to replace the placeholders (`<...>`) with your values:": "Обязательно замените заполнители (`<...>`) своими значениями:",
    "- `<YourServicePrincipalName>` - the name of the service principal that will be created for Dynatrace to access Azure.": "- `<YourServicePrincipalName>` - имя service principal, который будет создан для доступа Dynatrace к Azure.",
    "- `<YourSubscriptionID>`- the name of the subscription you would like to monitor.": "- `<YourSubscriptionID>` - имя подписки, которую нужно отслеживать.",
    "- `<YourResourceGroupID>` - the name of the specific resource group you would like to monitor.": "- `<YourResourceGroupID>` - имя конкретной группы ресурсов, которую нужно отслеживать.",
    "+ You can create several Azure service principals setting the `--scope` to subscription level and add multiple credentials monitoring the same Azure subscription in Dynatrace, but different services.": "+ Можно создать несколько Azure service principals, задав параметр `--scope` на уровне подписки, и добавить несколько учётных данных в Dynatrace для мониторинга одной подписки Azure, но разных сервисов.",
    "For example:": "Например:",
    "- One monitoring `Azure Virtual machines (built-in)` service": "- Один для мониторинга сервиса `Azure Virtual machines (built-in)`",
    "- Another monitoring `Azure SQL (built-in)`, `Azure Storage Blob Services`, `Azure Storage Queue Services`, `Azure Storage Table Services`, and `Azure Storage File Services`, but not monitoring `Azure Virtual machines (built-in)`.": "- Другой для мониторинга `Azure SQL (built-in)`, `Azure Storage Blob Services`, `Azure Storage Queue Services`, `Azure Storage Table Services` и `Azure Storage File Services`, но не `Azure Virtual machines (built-in)`.",
    "Remember that the scope of monitored services needs to be different for each credential and must not be left with the default configuration. Otherwise, metric values for overlapping services might be incorrect.": "Помните, что набор отслеживаемых сервисов должен быть разным для каждых учётных данных и не должен оставаться в конфигурации по умолчанию. В противном случае значения метрик для пересекающихся сервисов могут оказаться некорректными.",
    "* (not recommended) One Azure service principal - many Azure subscriptions": "* (не рекомендуется) Один Azure service principal - множество подписок Azure",
    "If the first option is not suitable in your situation, configure an Azure service principal to monitor up to twenty Azure subscriptions.": "Если первый вариант не подходит, настройте Azure service principal для мониторинга до двадцати подписок Azure.",
    "Remember that the number of API calls depends on how large your Azure subscriptions are. If you notice that the Dynatrace integration for Azure monitoring is not working correctly, consider decreasing the number of subscriptions per Azure service principal.": "Помните, что количество вызовов API зависит от размера подписок Azure. Если интеграция Dynatrace для мониторинга Azure работает некорректно, рассмотрите возможность уменьшения числа подписок на один Azure service principal.",
    "### Limit monitored resources using monitoring based on tags - Dynatrace configuration": "### Ограничение отслеживаемых ресурсов с помощью мониторинга по тегам - конфигурация Dynatrace",
    "If you don't need to monitor all Azure resources in your subscriptions, you can use monitoring by tags to decrease Azure API calls.": "Если не нужно отслеживать все ресурсы Azure в подписках, можно использовать мониторинг по тегам для уменьшения вызовов Azure API.",
    "If you have a lot of subscriptions, monitoring based on tags might not be enough to avoid throttling, and you should still prepare a proper [Azure service principal configuration](#service-principal).": "При большом количестве подписок мониторинга по тегам может быть недостаточно для предотвращения регулирования, поэтому всё равно необходимо подготовить надлежащую [конфигурацию Azure service principal](#service-principal).",
    "* Monitoring by tags mostly allows you to limit the calls for metrics and sub-resources (for example, Microsoft.ServiceBus/namespaces/queues for all resources of type Microsoft.ServiceBus/namespaces).": "* Мониторинг по тегам в основном позволяет ограничить вызовы для метрик и вложенных ресурсов (например, Microsoft.ServiceBus/namespaces/queues для всех ресурсов типа Microsoft.ServiceBus/namespaces).",
    "* Calls for top-level resources still need to be made for each subscription.": "* Вызовы для ресурсов верхнего уровня по-прежнему выполняются для каждой подписки.",
    "You can choose to monitor resources based on existing Azure tags, as Dynatrace automatically imports them from service instances.": "Можно выбрать отслеживаемые ресурсы на основе существующих тегов Azure, которые Dynatrace автоматически импортирует из экземпляров сервисов.",
    "To monitor resources based on tags": "Чтобы выполнять мониторинг ресурсов на основе тегов",
    "1. Go to **Settings** > **Cloud and virtualization** > **Azure**.": "1. Откройте **Settings** > **Cloud and virtualization** > **Azure**.",
    '2. On the Azure overview page, select the **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") icon for the Azure instance.': '2. На странице обзора Azure выберите значок **Edit** ![Edit](https://dt-cdn.net/images/edit-icon-a083c62c49.svg "Edit") для нужного экземпляра Azure.',
    "3. Set **Resources to be monitored** to **Monitor resources selected by tags**.": "3. Установите для параметра **Resources to be monitored** значение **Monitor resources selected by tags**.",
    "4. Enter key/value pairs to identify resources to exclude from monitoring or include in monitoring.": "4. Введите пары ключ/значение для определения ресурсов, которые нужно исключить из мониторинга или включить в него.",
    "You can enter multiple key/value pairs: each time you enter a pair, another empty row is displayed for you to edit as needed.": "Можно ввести несколько пар ключ/значение: каждый раз при вводе пары появляется новая пустая строка для редактирования.",
    "5. Select **Save** to save your configuration.": "5. Нажмите **Save** для сохранения конфигурации.",
    "To import the Azure tags automatically into Dynatrace, turn on **Capture Azure tags automatically**.": "Чтобы автоматически импортировать теги Azure в Dynatrace, включите **Capture Azure tags automatically**.",
    "## Related topics": "## Связанные темы",
    '* [Microsoft Azure monitoring](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")': '* [Мониторинг Microsoft Azure](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Мониторинг Azure с Dynatrace")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "limit-api-calls-to-azure.md", TRANS, PASS)
    qa_one(REL, "limit-api-calls-to-azure.md")
