---
title: Мониторинг Azure Virtual Machines
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm
scraped: 2026-03-06T21:17:59.893176
---

# Мониторинг виртуальных машин Azure


* Latest Dynatrace
* 8 мин. чтения

Dynatrace предоставляет [расширение VM](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/overview) для установки OneAgent на виртуальные машины Azure. Это позволяет использовать встроенные средства автоматизации развертывания с помощью Azure Resource Manager (ARM). Расширение Dynatrace VM доступно для Windows и Linux во всех публичных регионах Azure (включая поддержку классических виртуальных машин).

Расширение сайта Dynatrace OneAgent не включает программу установки OneAgent. Вместо этого расширение использует REST API Dynatrace для загрузки программы установки из кластера в целевой версии, установленной в обновлениях OneAgent.

## Возможности

* Полностековый мониторинг на основе OneAgent
* [Расширения для простого развертывания OneAgent](#installation)
* Интеграция с Azure Monitor
* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, наборы масштабирования и другие
* Классические виртуальные машины также поддерживаются

## Предварительные требования

* Создайте [PaaS-токен](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Определите ваш идентификатор среды.
* При необходимости определите URL сервера.

  URL сервера требуется только при использовании ActiveGate для конечной точки Dynatrace. URL автоматически генерируется на основе идентификатора среды.

  + **URL сервера ActiveGate:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)

## Установка расширения Dynatrace OneAgent VM

Существует несколько способов установки расширения Dynatrace OneAgent VM: через портал Azure, Azure CLI или PowerShell, а также с помощью ARM-шаблона. Следуйте приведенным ниже инструкциям.

Портал Azure

Azure CLI 2.0

PowerShell

### Добавление расширения к существующей VM

1. В портале Azure перейдите к существующей виртуальной машине, на которую вы хотите добавить расширение OneAgent.
2. В левом меню перейдите в **Settings** и выберите **Extensions**.
3. Выберите **Add**.
4. Выберите **Choose extension**.
5. Из списка расширений выберите **Dynatrace OneAgent**.
6. Выберите **Create**, чтобы добавить расширение.
7. На странице **Install extension** введите ваш **environment ID**, ваш **API token** и ваш **server URL**. Подробности см. в разделе [Предварительные требования](#prerequisites).
8. Выберите, хотите ли вы включить мониторинг логов.
9. Необязательно: Определите группу хостов, к которой принадлежит VM.
10. Выберите **OK**.
11. Для проверки статуса развертывания перейдите в **Deployment Status**.

После завершения установки перезапустите ваши приложения на VM. Сразу после перезапуска OneAgent начнет их мониторинг.

### Добавление расширения к новой VM

1. При создании новой VM в мастере развертывания, в разделе **Advanced**, выберите **Select an extension**.
2. Выберите **Dynatrace OneAgent**.
3. Выберите **Create**.
4. На странице **Install extension** введите ваш **environment ID**, ваш **API token** и ваш **server URL**. Подробности см. в разделе [Предварительные требования](#prerequisites).
5. Выберите, хотите ли вы включить мониторинг логов.
6. Необязательно: Определите группу хостов, к которой принадлежит VM.
7. Выберите **OK**.
8. Продолжите настройку VM в мастере развертывания.
9. Выберите **Review and create**.
10. Для проверки статуса развертывания перейдите в **Deployment Status**.

После завершения установки перезапустите ваши приложения на VM. Сразу после перезапуска OneAgent начнет их мониторинг.

Замените все значения, отмеченные `<...>`, вашими реальными значениями.

```
az vm extension set


--publisher dynatrace.ruxit


-n "<Extension-Type>"


-g "<Resource-Group>"


--vm-name "<VM-Name>"


--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

При использовании Azure CLI внутри PowerShell настройки должны быть отформатированы как [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

```
--settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развернута VM. |
| VM-Name | Обязательный | Имя VM, на которую вы хотите установить расширение. |
| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS-токен, как описано в разделе [Предварительные требования](#prerequisites). |
| server | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите значение `yes`, если вы хотите включить мониторинг логов. |
| hostGroup | Необязательный | Определите группу хостов, к которой принадлежит VM. |
| overrideDefaults [1](#fn-1-1-def) | Необязательный | Переопределение значения таймаута по умолчанию --- 120 секунд. Например, если вы хотите установить таймаут в 600 секунд, добавьте `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` в строку `-Settings`, также можно оставить пустым `\"overrideDefaults\": {}` или `null`. В таких случаях будет применяться значение по умолчанию --- 120 секунд. |

1

Доступно начиная с версии расширения VM 2.201.1.0.

Для проверки статуса развертывания перейдите в **Deployment Status**.

После завершения установки перезапустите ваши приложения на VM. Сразу после перезапуска OneAgent начнет их мониторинг.

Замените все значения, отмеченные `<...>`, вашими реальными значениями.

```
Set-AzureRmVmExtension


-Name Dynatrace


-Publisher dynatrace.ruxit


-ResourceGroupName "<Resource-Group>"


-Location "<Location>"


-VMName "<VM-Name>"


-ExtensionType "<Extension-Type>"


-TypeHandlerVersion "<Extension-Version>"


-Settings @{ "tenantId"="<Environment-ID>"; "token"="<API Token>";"server"="<Server-Url>"; "enableLogAnalytics"="yes"; "hostGroup"="<Host-Group>"; }
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развернута VM. |
| Location | Обязательный | Расположение, в котором развернута VM. |
| VM-Name | Обязательный | Имя VM, на которую вы хотите установить расширение. |
| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS-токен, как описано в разделе [Предварительные требования](#prerequisites). |
| Extension-Version | Необязательный | Требуемая версия расширения. |
| server | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите значение `yes`, если вы хотите включить мониторинг логов. |
| hostGroup | Необязательный | Определите группу хостов, к которой принадлежит VM. |
| overrideDefaults [1](#fn-2-1-def) | Необязательный | Переопределение значения таймаута по умолчанию --- 120 секунд. Например, если вы хотите установить таймаут в 600 секунд, добавьте `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` в строку `-Settings`, также можно оставить пустым `\"overrideDefaults\": {}` или `null`. В таких случаях будет применяться значение по умолчанию --- 120 секунд. |

1

Доступно начиная с версии расширения VM 2.201.1.0.

Для проверки статуса развертывания перейдите в **Deployment Status**.

После завершения установки перезапустите ваши приложения на VM. Сразу после перезапуска OneAgent начнет их мониторинг.

Версия расширения VM 2.201.1.0+

Начиная с версии расширения VM 2.201.1.0, вы можете задать параметр `overrideDefaults` через CLI и PowerShell при [установке](#installation) и через [ARM-шаблон](#arm-template).

* Вы можете задать пользовательский таймаут (`overrideDefaults`) для загрузки расширения Azure VM, что полезно в средах с неоптимальным интернет-соединением или ограниченной пропускной способностью сети.
* Сообщения об ошибках стали более информативными, что полезно в автоматизированных системах.
* Обновление расширения Azure VM на Windows теперь можно выполнять без предварительного удаления. Если версия OneAgent изменяется на тенанте, достаточно заново установить расширение Azure VM для установки новой версии.

## Установка расширения Dynatrace OneAgent VM через ARM-шаблон

В качестве альтернативы основным методам установки вы можете включить расширение Dynatrace VM в ваши ARM-шаблоны.
JSON-файл для расширения виртуальной машины может быть вложен в ресурс виртуальной машины или размещен на корневом или верхнем уровне JSON-шаблона Resource Manager. [Размещение JSON-файла влияет на значение имени и типа ресурса](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-templates-resources#child-resources).

* В следующем примере предполагается, что расширение OneAgent вложено в ресурс виртуальной машины. При вложении ресурса расширения JSON-файл помещается в объект "resources": [] виртуальной машины.

  ```
  {


  "type": "extensions",


  "name": "dynatrace",


  "apiVersion": "2018-06-01",


  "location": "[resourceGroup().location]",


  "dependsOn": [


  "[concat('Microsoft.Compute/virtualMachines/', <VM-Name>)]"


  ],


  "properties": {


  "publisher": "dynatrace.ruxit",


  "type": "<Extension-Type>",


  "typeHandlerVersion": "<Extension-Version>",


  "autoUpgradeMinorVersion": true,


  "settings": {


  "tenantId": "<Environment-ID>",


  "token": "<API-Token>",


  "server": "<Server-Url>",


  "enableLogAnalytics": "yes",


  "hostGroup": "<Host-Group>"


  },


  }


  }
  ```
* При размещении JSON расширения на корневом уровне шаблона имя ресурса включает ссылку на родительскую виртуальную машину, а тип отражает вложенную конфигурацию.

  ```
  {


  "type": "Microsoft.Compute/virtualMachines/extensions",


  "name": "<Parent-VM-Resource>/dynatrace",


  "apiVersion": "2018-06-01",


  "location": "[resourceGroup().location]",


  "dependsOn": [


  "[concat('Microsoft.Compute/virtualMachines/', <VM-Name>)]"


  ],


  "properties": {


  "publisher": "dynatrace.ruxit",


  "type": "<Extension-Type>",


  "typeHandlerVersion": "<Extension-Version>",


  "autoUpgradeMinorVersion": true,


  "settings": {


  "tenantId": "<Environment-ID>",


  "token": "<API-Token>",


  "server": "<Server-Url>",


  "enableLogAnalytics": "yes",


  "hostGroup": "<Host-Group>"


  }


  }


  }
  ```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Parent-VM-Resource | Обязательный | Имя родительского ресурса VM, на который вы хотите установить расширение. Не применяется при использовании вложенного ресурса. |
| VM-Name | Обязательный | Имя VM, на которую вы хотите установить расширение. |
| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS-токен, как описано в разделе [Предварительные требования](#prerequisites). Начиная с версии `2.200.0.0`, рекомендуется передавать его в `protectedSettings`. |
| Extension-Version | Необязательный | Требуемая версия расширения. |
| server | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите значение `yes`, если вы хотите включить мониторинг логов. |
| hostGroup | Необязательный | Определите группу хостов, к которой принадлежит VM. |
| overrideDefaults [1](#fn-3-1-def) | Необязательный | Переопределение значения таймаута по умолчанию --- 120 секунд. Например, если вы хотите установить таймаут в 600 секунд, добавьте `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` в объект `settings` ARM-шаблона, также можно оставить пустым `\"overrideDefaults\": {}` или `null`. В таких случаях будет применяться значение по умолчанию --- 120 секунд. |

1

Доступно начиная с версии расширения VM 2.201.1.0.

Для проверки статуса развертывания перейдите в **Deployment Status**.

После завершения установки перезапустите ваши приложения на VM. Сразу после перезапуска OneAgent начнет их мониторинг.

## Настройка сетевых зон (необязательно)

Для настройки сетевых зон используйте приведенные ниже аргументы установщика.

```
az vm extension set


--publisher dynatrace.ruxit


-n "oneAgentLinux"


-g "yourresourcegroup"


--vm-name "awesome-vm"


--settings "{\"tenantId\":\"myawesometenant\",\"token\":\"nope123\", \"installerArguments\":\"--set-host-group=example_hostgroup --set-monitoring-mode=fullstack --set-network-zone=<your.network.zone>\"}"
```

Дополнительную информацию см. в разделе Сетевые зоны.

## Связанные темы

* Настройка Dynatrace в Microsoft Azure
* Матрица поддержки платформ и возможностей OneAgent
