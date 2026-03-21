---
title: Мониторинг Azure Virtual Machine Scale Set (VMSS)
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss
scraped: 2026-03-06T21:17:37.851510
---

* Latest Dynatrace

## Возможности

* Полный мониторинг стека на базе OneAgent
* [Расширения для простого развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных Azure VM: регионы Azure, обнаружение автомасштабирования и многое другое

Dynatrace предоставляет расширение VM для установки OneAgent на Azure Virtual Machine Scale Set (VMSS). Расширение не включает установщик OneAgent. Вместо этого оно использует Dynatrace REST API для скачивания последней версии из кластера, если не настроена [версия OneAgent по умолчанию](https://www.dynatrace.com/news/blog/define-default-version-oneagent-new-installations/). Обновления OneAgent предоставляются автоматически.

## Предварительные условия

* Создайте [PaaS-токен](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Определите ваш [идентификатор среды](../../../discover-dynatrace/get-started/monitoring-environment.md "Понимание и работа со средами мониторинга.").
* При необходимости определите URL сервера.

  URL сервера необходим только если вы используете ActiveGate для конечной точки Dynatrace SaaS. URL автоматически генерируется из идентификатора среды.

  + **URL сервера ActiveGate:**
    `https://<IP-адрес-или-имя-хоста-вашего-ActiveGate>:9999/e/<идентификатор-вашей-среды>/api` (порт ActiveGate настраивается)

## Установка

Расширение VM Dynatrace доступно для Windows и Linux во всех публичных регионах Azure.

Azure CLI 2.0

PowerShell

1. Выполните приведённую ниже команду.

   Замените все значения, обозначенные `<...>`, на ваши реальные значения.

   ```
   az vmss extension set


   --publisher dynatrace.ruxit


   -n "<Extension-Type>"


   -g "<Resource-Group>"


   --vmss-name "<VMSS-Name>"


   --settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
   ```

   При использовании Azure CLI в PowerShell необходимо форматировать настройки как [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

   ```
   --settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
   ```

   | Параметр | Обязательный | Описание |
   | --- | --- | --- |
   | Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |
   | VMSS-Name | Обязательный | Имя VMSS, в который вы хотите установить расширение. |
   | Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
   | tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные условия](#prerequisites). |
   | token | Обязательный | PaaS-токен, описанный в разделе [Предварительные условия](#prerequisites). |
   | server | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, описанную в разделе [Предварительные условия](#prerequisites). |
   | enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг логов. |
   | hostGroup | Необязательный | Определите [группу хостов](../../../observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups.md "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |
2. Обновите виртуальные машины VMSS.

   ```
   az vmss update-instances --instance-ids '*' --resource-group $CLUSTER_RESOURCE_GROUP --name $SCALE_SET_NAME
   ```
3. Для проверки статуса развёртывания перейдите в **Deployment Status**.

   После завершения установки перезапустите ваши приложения на виртуальных машинах. Сразу после перезапуска OneAgent начнёт их мониторинг.

1. Выполните приведённую ниже команду для применения расширения к определению VMSS.

   Замените все значения, обозначенные `<...>`, на ваши реальные значения.

   ```
   $vmss = Get-AzVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"


   $vmss = Add-AzVmssExtension


   -VirtualMachineScaleSet $vmss


   -Name "dynatrace"


   -Publisher "dynatrace.ruxit"


   -Type "<Extension-Type>"


   -TypeHandlerVersion "2.300"


   -Setting @{ "tenantId"="<Environment-ID>"; "token"="<API Token>";"server"="<Server-Url>"; "enableLogAnalytics"="yes"; "hostGroup"="<Host-Group>"; }
   ```

   | Параметр | Обязательный | Описание |
   | --- | --- | --- |
   | Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
   | tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные условия](#prerequisites). |
   | token | Обязательный | PaaS-токен, описанный в разделе [Предварительные условия](#prerequisites). |
   | server | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, описанную в разделе [Предварительные условия](#prerequisites). |
   | enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг логов. |
   | hostGroup | Необязательный | Определите [группу хостов](../../../observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups.md "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |
2. Обновите виртуальные машины VMSS с новым определением.

   ```
   Update-AzVmss


   -ResourceGroupName "<Resource-Group>"


   -Name "<VMSS-Name>"


   -VirtualMachineScaleSet $vmss
   ```

   | Параметр | Обязательный | Описание |
   | --- | --- | --- |
   | Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |
   | VMSS-Name | Обязательный | Имя VMSS, в который вы хотите установить расширение. |
3. Для проверки статуса развёртывания перейдите в **Deployment Status**.

   После завершения установки перезапустите ваши приложения на виртуальной машине. Сразу после перезапуска OneAgent начнёт их мониторинг.

## Установка расширения VM Dynatrace OneAgent через шаблон ARM

В качестве альтернативы основным методам установки вы можете включить расширение Dynatrace в ваши шаблоны ARM.

1. Поместите JSON-конфигурацию расширения виртуальной машины в ресурс VMSS, в раздел `extensions` внутри `extensionProfile`.

   Пример:

   ```
   {


   "type": "Microsoft.Compute/virtualMachineScaleSets",


   "sku": {...},


   "name": "<VMSS-Name>",


   "apiVersion": "2018-06-01",


   "location": "centralus",


   "properties": {


   "upgradePolicy": {...},


   "virtualMachineProfile": {


   "osProfile": {...},


   "storageProfile": {...},


   "networkProfile": {...},


   "extensionProfile": {


   "extensions": [


   {


   "name": "dynatrace",


   "properties": {


   "publisher": "dynatrace.ruxit",


   "type": "<Extension-Type>",


   "typeHandlerVersion": "<Extension-Version>",


   "autoUpgradeMinorVersion": true,


   "settings": {


   "tenantId": "<Environment-ID>",


   "token": "<API-Token>",


   "enableLogAnalytics": "yes"


   }


   }


   }


   ]


   }


   }


   }


   }
   ```
2. Настройте JSON-файл.

   ```
   {


   "name": "dynatrace",


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

   | Параметр | Обязательный | Описание |
   | --- | --- | --- |
   | Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |
   | VMSS-Name | Обязательный | Имя VMSS, в который вы хотите установить расширение. |
   | Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
   | tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные условия](#prerequisites). |
   | token | Обязательный | PaaS-токен, описанный в разделе [Предварительные условия](#prerequisites). |
   | Extension-Version | Необязательный | Необходимая версия[1](#fn-1-1-def) расширения. |
   | server | Необязательный | URL сервера, если вы хотите настроить альтернативную конечную точку связи, описанную в разделе [Предварительные условия](#prerequisites). |
   | enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг логов. |
   | hostGroup | Необязательный | Определите [группу хостов](../../../observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups.md "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |

   1

   Чтобы получить список версий расширения, выполните команду

   ```
   az vm extension image list --name oneAgentLinux --publisher dynatrace.ruxit
   ```
3. Для проверки статуса развёртывания перейдите в **Deployment Status**.

   После завершения установки перезапустите ваши приложения на виртуальной машине. Сразу после перезапуска OneAgent начнёт их мониторинг.

## Устранение неполадок

Узлы VMSS не отображаются в Dynatrace

Перезапустите узлы VMSS через PowerShell, заменив все значения, обозначенные `<...>`, на ваши реальные значения:

```
Restart-AzureRmVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута виртуальная машина |
| VMSS-Name | Обязательный | Имя VMSS, в который вы хотите установить расширение. |

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](../../technology-support/oneagent-platform-and-capability-support-matrix.md "Узнайте, какие возможности поддерживаются OneAgent на различных операционных системах и платформах.")
