# -*- coding: utf-8 -*-
"""L4-IF.73 -- ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_PAAS = "Узнайте о концепции токена доступа и его областях действия."
TT_ENVID = "Понимание окружений мониторинга и работа с ними."
TT_ONEAGENT_UPD = "Узнайте, как обновить OneAgent."
TT_ACTIVEGATE = "Познакомьтесь с базовыми концепциями ActiveGate."
TT_HOSTGROUP = "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."
TT_NETZONES = "Узнайте, как работают сетевые зоны в Dynatrace."
TT_OAP = "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."
TT_CLASSIC = "Мониторинг Azure Virtual Machines (classic) и просмотр доступных метрик."
TT_VMSS = "Узнайте, как установить, настроить и устранять неполадки OneAgent для мониторинга Azure VM Scale Set через VM extension."

TRANS = {
    "title: Monitor Azure Virtual Machines": "title: Мониторинг Azure Virtual Machines",
    "# Monitor Azure Virtual Machines": "# Мониторинг Azure Virtual Machines",
    "* How-to guide": "* Практическое руководство",
    "* 8-min read": "* Чтение: 8 мин",
    "* Published Jul 19, 2017": "* Опубликовано 19 июля 2017 г.",
    f"Dynatrace provides a [VM Extension](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/overview) to install OneAgent on Azure Virtual Machines. This enables you to leverage the native deployment automation features using Azure Resource Manager (ARM). The Dynatrace VM extension is available for Windows and Linux in all public Azure regions (including support for Classic Virtual Machines).": f"Dynatrace предоставляет [VM Extension](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/overview) для установки OneAgent на Azure Virtual Machines. Это позволяет использовать встроенные возможности автоматизации развёртывания через Azure Resource Manager (ARM). Dynatrace VM extension доступен для Windows и Linux во всех публичных регионах Azure (включая поддержку Classic Virtual Machines).",
    f'The Dynatrace OneAgent site extension doesn\'t include the OneAgent installer. Instead, the extension uses the Dynatrace REST API to download the installer from the cluster in the target version as set in [OneAgent updates](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Learn how to update OneAgent.").': f'Site extension Dynatrace OneAgent не включает установщик OneAgent. Вместо этого расширение использует Dynatrace REST API для загрузки установщика из кластера в целевой версии, заданной в разделе [Обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "{TT_ONEAGENT_UPD}").',
    "## Capabilities": "## Возможности",
    "* Full-stack monitoring powered by OneAgent": "* Мониторинг полного стека на базе OneAgent",
    "* [Extensions for easy deployment of OneAgent](#installation)": "* [Расширения для простого развёртывания OneAgent](#installation)",
    f'* [Integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    "* Enhanced support for Azure VM metadata such as Azure regions, scale sets and more": "* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, масштабируемые наборы и другое",
    f'* [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Monitor Azure Virtual Machines (classic) and view available metrics.") are also supported': f'* Поддерживаются также [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "{TT_CLASSIC}")',
    "## Prerequisites": "## Предварительные требования",
    f'* Create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").': f'* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "{TT_PAAS}").',
    f'* Determine your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Определите ваш [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENVID}").',
    "* Determine your server URL if required.": "* При необходимости определите URL сервера.",
    "The server URL is required only if you use either of the following:": "URL сервера требуется только в следующих случаях:",
    "+ a Dynatrace Managed endpoint": "+ эндпоинт Dynatrace Managed",
    f"+ an ActiveGate for a Dynatrace Managed or Dynatrace SaaS endpoint": f"+ ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS",
    "(For Dynatrace SaaS, the URL is automatically generated from the environment ID.)": "(Для Dynatrace SaaS URL формируется автоматически на основе идентификатора окружения.)",
    "+ **ActiveGate server URL:**": "+ **ActiveGate server URL:**",
    "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)": "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)",
    "+ **Dynatrace Managed server URL:**": "+ **Dynatrace Managed server URL:**",
    "`https://{your-domain}/e/{your-environment-id}/api`": "`https://{your-domain}/e/{your-environment-id}/api`",
    f'If you\'re using Dynatrace Managed, or if your cluster traffic should be routed through an [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), you need to configure the API endpoint used by the extension for downloading OneAgent.': f'При использовании Dynatrace Managed или если трафик кластера должен направляться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "{TT_ACTIVEGATE}"), необходимо настроить API-эндпоинт, используемый расширением для загрузки OneAgent.',
    "## Install Dynatrace OneAgent VM extension": "## Установка VM extension Dynatrace OneAgent",
    "There are several ways to install the Dynatrace OneAgent VM extension: through Azure Portal, Azure CLI, or PowerShell, or by using an ARM template. Follow the steps below for instructions.": "Dynatrace OneAgent VM extension можно установить несколькими способами: через Azure Portal, Azure CLI, PowerShell или с помощью ARM-шаблона. Следуйте инструкциям ниже.",
    "Azure Portal": "Azure Portal",
    "Azure CLI 2.0": "Azure CLI 2.0",
    "PowerShell": "PowerShell",
    "### Add the extension to an existing VM": "### Добавление расширения к существующей VM",
    "1. In Azure Portal, go to an existing virtual machine where you want to add the OneAgent extension.": "1. В Azure Portal перейдите к существующей виртуальной машине, на которую нужно добавить расширение OneAgent.",
    "2. In the left menu, go to **Settings** and select **Extensions**.": "2. В левом меню откройте **Settings** и выберите **Extensions**.",
    "3. Select **Add**.": "3. Выберите **Add**.",
    "4. Select **Choose extension**.": "4. Выберите **Choose extension**.",
    "5. From the list of extensions, select **Dynatrace OneAgent**.": "5. В списке расширений выберите **Dynatrace OneAgent**.",
    "6. Select **Create** to add the extension.": "6. Нажмите **Create** для добавления расширения.",
    "7. On the **Install extension** page, enter your **environment ID**, your **API token**, and your **server URL**. See [Prerequisites](#prerequisites) for details.": "7. На странице **Install extension** введите **environment ID**, **API token** и **server URL**. Подробнее см. в разделе [Предварительные требования](#prerequisites).",
    "8. Select whether you want to enable Log Monitoring.": "8. Укажите, нужно ли включить Log Monitoring.",
    f'9. Optional Define the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs.': f'9. Необязательно: укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "{TT_HOSTGROUP}"), к которой принадлежит VM.',
    "10. Select **OK**.": "10. Нажмите **OK**.",
    "11. To check the deployment status, go to **Deployment Status**.": "11. Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.",
    "After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.": "После завершения установки перезапустите приложения на VM. Сразу после перезапуска OneAgent начнёт их мониторинг.",
    "### Add the extension to a new VM": "### Добавление расширения к новой VM",
    "1. During the creation of a new VM in the deployment wizard, in **Advanced**, select **Select an extension**.": "1. При создании новой VM в мастере развёртывания в разделе **Advanced** выберите **Select an extension**.",
    "2. Select **Dynatrace OneAgent**.": "2. Выберите **Dynatrace OneAgent**.",
    "3. Select **Create**.": "3. Нажмите **Create**.",
    "4. On the **Install extension** page, enter your **environment ID**, your **API token**, and your **server URL**. See [Prerequisites](#prerequisites) for details.": "4. На странице **Install extension** введите **environment ID**, **API token** и **server URL**. Подробнее см. в разделе [Предварительные требования](#prerequisites).",
    "5. Select whether you want to enable Log Monitoring.": "5. Укажите, нужно ли включить Log Monitoring.",
    f'6. Optional Define the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs.': f'6. Необязательно: укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "{TT_HOSTGROUP}"), к которой принадлежит VM.',
    "7. Select **OK**.": "7. Нажмите **OK**.",
    "8. Continue VM configuration in the deployment wizard.": "8. Продолжите настройку VM в мастере развёртывания.",
    "9. Select **Review and create**.": "9. Нажмите **Review and create**.",
    "10. To check the deployment status, go to **Deployment Status**.": "10. Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.",
    "Replace all values marked with `<...>` with your actual values.": "Замените все значения, отмеченные как `<...>`, реальными значениями.",
    "When using the Azure CLI within PowerShell, the settings have to be formatted as a [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).": "При использовании Azure CLI в PowerShell параметры settings необходимо оформить в виде [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).",
    "| Parameter | Required | Description |": "| Параметр | Обязательный | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| Resource-Group | Required | Name of the resource group on which the VM is deployed. |": "| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |",
    "| VM-Name | Required | Name of the VM where you want to install the extension. |": "| VM-Name | Обязательный | Имя VM, на которую нужно установить расширение. |",
    "| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |": "| Extension-Type | Обязательный | Для Windows-based VM используйте `oneAgentWindows`. Для Linux-based VM используйте `oneAgentLinux`. |",
    "| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |": "| tenantId | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |": "| token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |": "| server | Необязательный | URL сервера, если нужно настроить альтернативный коммуникационный эндпоинт, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |": "| enableLogsAnalytics | Необязательный | Установите `yes`, чтобы включить Log Monitoring. |",
    f'| hostGroup | Optional | Define the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |': f'| hostGroup | Необязательный | Укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "{TT_HOSTGROUP}"), к которой принадлежит VM. |',
    '| overrideDefaults [1](#fn-1-1-def) | Optional | Override the default value of the timeout—120 seconds. For example, if you want to set the timeout to 600 seconds, add `\\"overrideDefaults\\": {\\"downloadInstallerRequestTimeoutInSeconds\\": 600}` to the `-Settings` string, you can also leave it empty `\\"overrideDefaults\\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |': '| overrideDefaults [1](#fn-1-1-def) | Необязательный | Переопределяет значение таймаута по умолчанию (120 секунд). Например, чтобы задать таймаут 600 секунд, добавьте `\\"overrideDefaults\\": {\\"downloadInstallerRequestTimeoutInSeconds\\": 600}` в строку `-Settings`; можно также оставить пустым `\\"overrideDefaults\\": {}` или `null`. В этих случаях применяется значение по умолчанию 120 секунд. |',
    "1": "1",
    "Available from VM extension version 2.201.1.0.": "Доступно начиная с версии VM extension 2.201.1.0.",
    "To check the deployment status, go to **Deployment Status**.": "Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.",
    "| Location | Required | Location where the VM is deployed. |": "| Location | Обязательный | Расположение, в котором развёрнута VM. |",
    "| Extension-Version | Optional | Required version of the extension. |": "| Extension-Version | Необязательный | Требуемая версия расширения. |",
    '| overrideDefaults [1](#fn-2-1-def) | Optional | Override the default value of the timeout—120 seconds. For example, if you want to set the timeout to 600 seconds, add `\\"overrideDefaults\\": {\\"downloadInstallerRequestTimeoutInSeconds\\": 600}` to the `-Settings` string, you can also leave it empty `\\"overrideDefaults\\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |': '| overrideDefaults [1](#fn-2-1-def) | Необязательный | Переопределяет значение таймаута по умолчанию (120 секунд). Например, чтобы задать таймаут 600 секунд, добавьте `\\"overrideDefaults\\": {\\"downloadInstallerRequestTimeoutInSeconds\\": 600}` в строку `-Settings`; можно также оставить пустым `\\"overrideDefaults\\": {}` или `null`. В этих случаях применяется значение по умолчанию 120 секунд. |',
    "VM extension version 2.201.1.0+": "VM extension версии 2.201.1.0+",
    "With the VM extension 2.201.1.0 release, you can set the `overrideDefaults` parameter via CLI and PowerShell [installation](#installation) and via [ARM template](#arm-template).": "В версии VM extension 2.201.1.0 стало доступно задание параметра `overrideDefaults` через CLI, PowerShell [установку](#installation) и [ARM-шаблон](#arm-template).",
    "* You can set the custom timeout (`overrideDefaults`) for the Azure VM Extension download, which is helpful in environments with a suboptimal internet connection or smaller network throughput (bandwidth).": "* Теперь можно задать пользовательский таймаут (`overrideDefaults`) для загрузки Azure VM Extension, что полезно в окружениях с нестабильным интернет-соединением или низкой пропускной способностью сети.",
    "* Your error messages became more informative, which is helpful in automated systems.": "* Сообщения об ошибках стали более информативными, что упрощает работу в автоматизированных системах.",
    "* Updating the Azure VM Extension on Windows can now be done without uninstalling it first. If the version of OneAgent changes on the tenant, you just need to install the Azure VM Extension again to install this new version.": "* Обновление Azure VM Extension на Windows теперь не требует предварительной деинсталляции. Если версия OneAgent изменилась в тенанте, достаточно повторно установить Azure VM Extension для перехода на новую версию.",
    "## Install Dynatrace OneAgent VM extension via an ARM template": "## Установка VM extension Dynatrace OneAgent через ARM-шаблон",
    "Alternatively to the main installation methods, you can make the Dynatrace VM extension part of your ARM templates.": "В дополнение к основным методам установки можно включить Dynatrace VM extension в состав ARM-шаблонов.",
    "The JSON file for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a resource manager JSON template. [The placement of the JSON file affects the value of the resource name and type](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-templates-resources#child-resources).": "JSON-файл расширения виртуальной машины можно вложить внутрь ресурса виртуальной машины или разместить в корне JSON-шаблона Resource Manager. [Расположение JSON-файла влияет на значение имени и типа ресурса](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-templates-resources#child-resources).",
    '* The following example assumes the OneAgent extension is nested inside the virtual machine resource. When nesting the extension resource, the JSON file is placed in the "resources": [] object of the virtual machine.': '* В следующем примере расширение OneAgent вложено внутрь ресурса виртуальной машины. При вложении ресурса расширения JSON-файл размещается в объекте "resources": [] виртуальной машины.',
    "* When placing the extension JSON at the root of the template, the resource name includes a reference to the parent virtual machine, and the type reflects the nested configuration.": "* При размещении JSON расширения в корне шаблона имя ресурса содержит ссылку на родительскую виртуальную машину, а тип отражает вложенную конфигурацию.",
    "| Parent-VM-Resource | Required | Name of the parent VM resource where you want to install the extension. Not applicable when using nested resource. |": "| Parent-VM-Resource | Обязательный | Имя родительского ресурса VM, на который нужно установить расширение. Не применяется при использовании вложенного ресурса. |",
    "| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). From `2.200.0.0` version, it's recommended to pass it in `protectedSettings`. |": "| token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). Начиная с версии `2.200.0.0` рекомендуется передавать его в `protectedSettings`. |",
    '| overrideDefaults [1](#fn-3-1-def) | Optional | Override the default value of the timeout—120 seconds. For example, if you want to set the timeout to 600 seconds, add `\\"overrideDefaults\\": {\\"downloadInstallerRequestTimeoutInSeconds\\": 600}` to the ARM template in the `settings` object, you can also leave it empty `\\"overrideDefaults\\": {}`, or `null`. In such cases, the 120 seconds default value will apply. |': '| overrideDefaults [1](#fn-3-1-def) | Необязательный | Переопределяет значение таймаута по умолчанию (120 секунд). Например, чтобы задать таймаут 600 секунд, добавьте `\\"overrideDefaults\\": {\\"downloadInstallerRequestTimeoutInSeconds\\": 600}` в объект `settings` ARM-шаблона; можно также оставить пустым `\\"overrideDefaults\\": {}` или `null`. В этих случаях применяется значение по умолчанию 120 секунд. |',
    "## Configure network zones Optional": "## Настройка сетевых зон (необязательно)",
    "To configure network zones, use the installer arguments below.": "Для настройки сетевых зон используйте приведённые ниже аргументы установщика.",
    f'See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.': f'Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "{TT_NETZONES}").',
    "## Related topics": "## Связанные темы",
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    f'* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': f'* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "{TT_OAP}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-vm.md", TRANS, PASS)
    qa_one(REL, "azure-vm.md")
