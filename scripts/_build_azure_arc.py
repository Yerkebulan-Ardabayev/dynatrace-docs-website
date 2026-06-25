# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_CLASSIC_VM = (
    "Мониторинг Azure Virtual Machines (classic) и просмотр доступных метрик."
)
TT_PAAS = "Изучите концепцию токена доступа и его области действия."
TT_ENV_ID = "Понять и научиться работать со средами мониторинга."
TT_AG = "Основные концепции, связанные с ActiveGate."
TT_HOST_GROUPS = "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."
TT_JSON = "Файл JSON для расширения виртуальной машины."

TRANS = {
    "title: Microsoft Azure Arc-enabled servers": "title: Microsoft Azure Arc-enabled servers",
    "# Microsoft Azure Arc-enabled servers": "# Microsoft Azure Arc-enabled servers",
    "* How-to guide": "* Практическое руководство",
    "* 4-min read": "* Чтение: 4 мин",
    "* Published Dec 10, 2024": "* Опубликовано 10 декабря 2024 г.",
    "## Capabilities": "## Возможности",
    "* Full-stack monitoring powered by OneAgent": "* Мониторинг полного стека на базе OneAgent",
    "* [Extensions for easy deployment of OneAgent](#installation)": "* [Расширения для простого развёртывания OneAgent](#installation)",
    f'* [Integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    "* Enhanced support for Azure VM metadata such as Azure regions, scale sets and more": "* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, масштабируемые наборы и другое",
    f'* [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Monitor Azure Virtual Machines (classic) and view available metrics.") are also supported': f'* Также поддерживаются [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "{TT_CLASSIC_VM}")',
    "## Prerequisites": "## Предварительные требования",
    f'* Create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").': f'* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "{TT_PAAS}").',
    f'* Determine your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Определите [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENV_ID}").',
    "* Determine your server URL if required.": "* При необходимости определите URL сервера.",
    "The server URL is required only if you use either of the following:": "URL сервера требуется только при использовании одного из следующих вариантов:",
    "+ a Dynatrace Managed endpoint": "+ эндпоинт Dynatrace Managed",
    "+ an ActiveGate for a Dynatrace Managed or Dynatrace SaaS endpoint": "+ ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS",
    "(For Dynatrace SaaS, the URL is automatically generated from the environment ID.)": "(Для Dynatrace SaaS URL генерируется автоматически на основе идентификатора среды.)",
    "+ **ActiveGate server URL:**": "+ **ActiveGate server URL:**  ",
    "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)": "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate можно настраивать)",
    "+ **Dynatrace Managed server URL:**": "+ **Dynatrace Managed server URL:**  ",
    "`https://{your-domain}/e/{your-environment-id}/api`": "`https://{your-domain}/e/{your-environment-id}/api`",
    f'If you\'re using Dynatrace Managed, or if your cluster traffic should be routed through an [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), you need to configure the API endpoint used by the extension for downloading OneAgent.': f'При использовании Dynatrace Managed или если трафик кластера должен маршрутизироваться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "{TT_AG}"), необходимо настроить эндпоинт API, используемый расширением для загрузки OneAgent.',
    "## Install Dynatrace OneAgent VM extension": "## Установка VM extension Dynatrace OneAgent",
    "There are several ways to install the Dynatrace OneAgent VM extension: through Azure Portal, Azure CLI, or PowerShell, or by using an ARM template. Follow the steps below for instructions.": "VM extension Dynatrace OneAgent можно установить несколькими способами: через Azure Portal, Azure CLI, PowerShell или с помощью шаблона ARM. Следуйте инструкциям ниже.",
    "Azure Portal": "Azure Portal",
    "Azure CLI 2.0": "Azure CLI 2.0",
    "ARM template": "ARM template",
    "### Add the extension to an existing VM": "### Добавление расширения к существующей VM",
    "1. In Azure Portal, go to an existing Azure Arc Machine resource.": "1. В Azure Portal перейдите к существующему ресурсу Azure Arc Machine.",
    "2. In the left menu, go to **Settings** > **Extensions**.": "2. В левом меню откройте **Settings** > **Extensions**.",
    "3. Select **Add**.": "3. Выберите **Add**.",
    "4. From the list of extensions, select **Dynatrace OneAgent**.": "4. В списке расширений выберите **Dynatrace OneAgent**.",
    "5. Select **Next** to add the extension.": "5. Выберите **Next** для добавления расширения.",
    "6. On the **Configure Dynatrace OneAgent Extension** page, enter your **Environment ID**, your **API Token**, and your **Server URL**. See [Prerequisites](#prerequisites) for details.": "6. На странице **Configure Dynatrace OneAgent Extension** введите **Environment ID**, **API Token** и **Server URL**. Подробнее см. в разделе [Предварительные требования](#prerequisites).",
    "7. Optional Define additional OneAgent settings (such as proxy, port).": "7. Необязательно: задайте дополнительные настройки OneAgent (например, прокси, порт).",
    "8. Select **Review + create**.": "8. Выберите **Review + create**.",
    "9. To check the deployment status, in your Dynatrace environment, go to **Deployment Status**.": "9. Чтобы проверить статус развёртывания, в среде Dynatrace откройте **Deployment Status**.",
    "| Parameter | Required | Description |": "| Параметр | Обязательный | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| Resource-Group | Required | Name of the resource group on which the VM is deployed. |": "| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |",
    "| Azure Arc Server Name | Required | Name of the machine extension. |": "| Azure Arc Server Name | Обязательный | Имя расширения машины. |",
    "| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |": "| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |",
    "| Extension-name | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |": "| Extension-name | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |",
    "| Azure Region | Required | Azure Region of the resource |": "| Azure Region | Обязательный | Регион Azure ресурса. |",
    "| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |": "| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |",
    "| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |": "| token | Обязательный | PaaS token, как описано в разделе [Предварительные требования](#prerequisites). |",
    "| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |": "| server | Необязательный | URL сервера, если нужно настроить альтернативный эндпоинт связи, как описано в разделе [Предварительные требования](#prerequisites). |",
    "| enableLogsAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |": "| enableLogsAnalytics | Необязательный | Установите значение `yes`, чтобы включить Log Monitoring. |",
    f'| hostGroup | Optional | Define the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |': f'| hostGroup | Необязательный | Укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "{TT_HOST_GROUPS}"), к которой принадлежит VM. |',
    "Alternatively to the main installation methods, you can make the Dynatrace VM extension part of your ARM templates.": "Помимо основных способов установки, VM extension Dynatrace можно включить в шаблоны ARM.",
    f"The [JSON fileï»¿](https://dt-url.net/9f03wr8) for a virtual machine extension can be nested inside the virtual machine resource, or placed at the root or top level of a resource manager JSON template. The placement of the JSON file affects the value of the resource name and type.": f"[Файл JSON](https://dt-url.net/9f03wr8) для расширения виртуальной машины можно вложить в ресурс виртуальной машины или разместить на корневом уровне шаблона JSON диспетчера ресурсов. Расположение файла JSON влияет на значения имени и типа ресурса.",
    "Example": "Пример",
    'The following example assumes the OneAgent extension is nested inside the virtual machine resource. When nesting the extension resource, the JSON file is placed in the `"resources": []` object of the virtual machine.\'': 'В следующем примере расширение OneAgent вложено в ресурс виртуальной машины. При вложении ресурса расширения файл JSON размещается в объекте `"resources": []` виртуальной машины.',
    "| Parent-Arc Machine-Resource | Required | Name of the Azure Arc Machine resource where you want to install the extension. Not applicable when using nested resource. |": "| Parent-Arc Machine-Resource | Обязательный | Имя ресурса Azure Arc Machine, на котором нужно установить расширение. Неприменимо при использовании вложенного ресурса. |",
    "| Arc Machine Name | Required | Name of the Azure Arc Machine where you want to install the extension. |": "| Arc Machine Name | Обязательный | Имя Azure Arc Machine, на котором нужно установить расширение. |",
    "| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |": "| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |",
    "| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |": "| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |",
    "| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). From Microsoft Azure Arc version 2.200.0.0, it's recommended to pass it in `protectedSettings`. |": "| token | Обязательный | PaaS token, как описано в разделе [Предварительные требования](#prerequisites). Начиная с версии Microsoft Azure Arc 2.200.0.0, рекомендуется передавать его в `protectedSettings`. |",
    "| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |": "| server | Необязательный | URL сервера, если нужно настроить альтернативный эндпоинт связи, как описано в разделе [Предварительные требования](#prerequisites). |",
    "To check the deployment status, in your Dynatrace environment, go to **Manage** > **Deployment status**.": "Чтобы проверить статус развёртывания, в среде Dynatrace откройте **Manage** > **Deployment status**.",
    "After installation is complete, OneAgent will begin monitoring.": "После завершения установки OneAgent начнёт мониторинг.",
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-arc-enabled-servers.md", TRANS, PASS)
    qa_one(REL, "azure-arc-enabled-servers.md")
