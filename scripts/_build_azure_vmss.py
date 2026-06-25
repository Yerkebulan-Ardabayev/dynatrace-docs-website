# -*- coding: utf-8 -*-
"""L4-IF.73 — ingest-from/microsoft-azure-services/azure-integrations/azure-vmss.md"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _zos_canon_l4if71 import build_one, qa_one

REL = "ingest-from/microsoft-azure-services/azure-integrations"

TT_AZURE = "Настройка и конфигурирование мониторинга для Microsoft Azure."
TT_PAAS = "Узнайте о концепции токена доступа и его областях действия."
TT_ENVID = "Ознакомьтесь с мониторинговыми средами и узнайте, как с ними работать."
TT_ACTIVEGATE = "Ознакомьтесь с базовыми концепциями ActiveGate."
TT_HOSTGROUP = "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."
TT_PLATFORM = "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах."

TRANS = {
    "title: Monitor Azure Virtual Machine Scale Set (VMSS)": "title: Мониторинг Azure Virtual Machine Scale Set (VMSS)",
    "# Monitor Azure Virtual Machine Scale Set (VMSS)": "# Мониторинг Azure Virtual Machine Scale Set (VMSS)",
    "* How-to guide": "* Практическое руководство",
    "* 6-min read": "* Чтение: 6 мин",
    "* Published Jul 19, 2017": "* Опубликовано 19 июля 2017 г.",
    "## Capabilities": "## Возможности",
    "* Full-stack monitoring powered OneAgent": "* Мониторинг полного стека на базе OneAgent",
    f"* [Extensions for easy deployment of OneAgent](#installation)": "* [Расширения для простого развёртывания OneAgent](#installation)",
    f'* [Integration with Azure Monitor](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    "* Enhanced support for Azure VM Metadata such as Azure regions, AutoScale detection, and more": "* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, обнаружение AutoScale и другое",
    "Dynatrace provides a VM extension to install OneAgent on Azure Virtual Machine Scale Set (VMSS). The extension doesn't include the OneAgent installer. Instead, it uses the Dynatrace REST API to download the latest version from the cluster, unless a [default OneAgent version](https://www.dynatrace.com/news/blog/define-default-version-oneagent-new-installations/) is configured. OneAgent updates are provided automatically.": "Dynatrace предоставляет VM extension для установки OneAgent на Azure Virtual Machine Scale Set (VMSS). Расширение не включает установщик OneAgent. Вместо этого оно использует Dynatrace REST API для загрузки последней версии с кластера, если только не задана [версия OneAgent по умолчанию](https://www.dynatrace.com/news/blog/define-default-version-oneagent-new-installations/). Обновления OneAgent применяются автоматически.",
    "## Prerequisites": "## Предварительные требования",
    f'* Create a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").': f'* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "{TT_PAAS}").',
    f'* Determine your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").': f'* Определите свой [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "{TT_ENVID}").',
    "* Determine your server URL if required.": "* При необходимости определите URL сервера.",
    "The server URL is required only if you use either of the following:": "URL сервера требуется только в следующих случаях:",
    "+ a Dynatrace Managed endpoint": "+ эндпоинт Dynatrace Managed",
    "+ an ActiveGate for a Dynatrace Managed or Dynatrace SaaS endpoint": "+ ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS",
    "(For Dynatrace SaaS, the URL is automatically generated from the environment ID.)": "(Для Dynatrace SaaS URL формируется автоматически на основе идентификатора среды.)",
    "+ **ActiveGate server URL:**": "+ **URL сервера ActiveGate:**",
    "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)": "`https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)",
    "+ **Dynatrace Managed server URL:**": "+ **URL сервера Dynatrace Managed:**",
    "`https://{your-domain}/e/{your-environment-id}/api`": "`https://{your-domain}/e/{your-environment-id}/api`",
    f'If you\'re using Dynatrace Managed, or if your cluster traffic should be routed through an [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), you need to configure the API endpoint used by the extension for downloading OneAgent.': f'Если используется Dynatrace Managed или трафик кластера должен маршрутизироваться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "{TT_ACTIVEGATE}"), необходимо настроить API-эндпоинт, используемый расширением для загрузки OneAgent.',
    "## Installation": "## Установка",
    "The Dynatrace VM extension is available for Windows and Linux in all public Azure regions.": "VM extension Dynatrace доступно для Windows и Linux во всех публичных регионах Azure.",
    "Azure CLI 2.0": "Azure CLI 2.0",
    "PowerShell": "PowerShell",
    "1. Run the command below.": "1. Выполните приведённую ниже команду.",
    "Replace all values marked with `<...>` with your actual values.": "Замените все значения, отмеченные `<...>`, на фактические.",
    "When using the Azure CLI within PowerShell, you need to format the settings as a [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).": "При использовании Azure CLI в PowerShell необходимо форматировать параметры как [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).",
    "| Parameter | Required | Description |": "| Параметр | Обязательный | Описание |",
    "| --- | --- | --- |": "| --- | --- | --- |",
    "| Resource-Group | Required | Name of the resource group on which the VM is deployed. |": "| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута ВМ. |",
    "| VMSS-Name | Required | Name of the VMSS where you want to install the extension. |": "| VMSS-Name | Обязательный | Имя VMSS, на котором нужно установить расширение. |",
    "| Extension-Type | Required | For Windows-based VMs, use `oneAgentWindows`. For Linux-based VMs, use `oneAgentLinux`. |": "| Extension-Type | Обязательный | Для ВМ на базе Windows используйте `oneAgentWindows`. Для ВМ на базе Linux используйте `oneAgentLinux`. |",
    "| tenantId | Required | The environment ID as described in [Prerequisites](#prerequisites). |": "| tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| token | Required | The PaaS token as described in [Prerequisites](#prerequisites). |": "| token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |",
    "| server | Optional | The server URL, if you want to configure an alternative communication endpoint as described in [Prerequisites](#prerequisites). |": "| server | Необязательный | URL сервера для настройки альтернативного эндпоинта связи, описанного в разделе [Предварительные требования](#prerequisites). |",
    "| enableLogAnalytics | Optional | Set to `yes` if you want to enable Log Monitoring. |": "| enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг журналов. |",
    f'| hostGroup | Optional | Define the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") to which the VM belongs. |': f'| hostGroup | Необязательный | Определите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "{TT_HOSTGROUP}"), к которой принадлежит ВМ. |',
    "2. Update the VMSS virtual machines.": "2. Обновите виртуальные машины VMSS.",
    "3. To check the deployment status, go to **Deployment Status**.": "3. Чтобы проверить статус развёртывания, откройте **Deployment Status**.",
    "After installation is complete, restart your applications on the VMs. Immediately after restart, OneAgent will begin monitoring them.": "После завершения установки перезапустите приложения на ВМ. Сразу после перезапуска OneAgent начнёт их мониторинг.",
    "1. Run the command below to apply the extension to the VMSS definition.": "1. Выполните приведённую ниже команду, чтобы применить расширение к определению VMSS.",
    "2. Update the VMSS virtual machines with the new definition.": "2. Обновите виртуальные машины VMSS с новым определением.",
    "| Resource-Group | Required | Name of the resource group on which the VM is deployed. |": "| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута ВМ. |",
    "After installation is complete, restart your applications on the VM. Immediately after restart, OneAgent will begin monitoring them.": "После завершения установки перезапустите приложения на ВМ. Сразу после перезапуска OneAgent начнёт их мониторинг.",
    "## Install Dynatrace OneAgent VM extension via an ARM template": "## Установка VM extension Dynatrace OneAgent через шаблон ARM",
    "Alternatively to the main installation methods, you can make the Dynatrace site extension part of your ARM templates.": "В дополнение к основным методам установки можно включить site extension Dynatrace в шаблоны ARM.",
    "1. Place the JSON configuration for a virtual machine extension in the VMSS resource, under `extensions` in `extensionProfile`.": "1. Поместите конфигурацию JSON для расширения виртуальной машины в ресурс VMSS в раздел `extensions` внутри `extensionProfile`.",
    "Example:": "Пример:",
    "2. Configure the JSON file.": "2. Настройте JSON-файл.",
    "| Extension-Version | Optional | Required version[1](#fn-1-1-def) of the extension. |": "| Extension-Version | Необязательный | Требуемая версия[1](#fn-1-1-def) расширения. |",
    "1": "1",
    "o fetch the list of extension versions, run": "Чтобы получить список версий расширений, выполните",
    "## Troubleshooting": "## Устранение неполадок",
    "VMSS nodes not showing up in Dynatrace": "Узлы VMSS не отображаются в Dynatrace",
    "Restart the VMSS nodes via PowerShell, replacing all values marked with `<...>` with your actual values:": "Перезапустите узлы VMSS через PowerShell, заменив все значения, отмеченные `<...>`, на фактические:",
    "| Resource-Group | Required | Name of the resource group on which the Virtual Machine is deployed |": "| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута виртуальная машина |",
    "## Related topics": "## Связанные темы",
    f'* [Set up Dynatrace on Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")': f'* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "{TT_AZURE}")',
    f'* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")': f'* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "{TT_PLATFORM}")',
}

PASS = set()

if __name__ == "__main__":
    build_one(REL, "azure-vmss.md", TRANS, PASS)
    qa_one(REL, "azure-vmss.md")
