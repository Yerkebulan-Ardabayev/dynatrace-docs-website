---
title: Мониторинг Azure Virtual Machine Scale Set (VMSS)
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss
scraped: 2026-05-12T11:22:58.327127
---

# Мониторинг Azure Virtual Machine Scale Set (VMSS)

# Мониторинг Azure Virtual Machine Scale Set (VMSS)

* Практическое руководство
* Чтение: 6 мин
* Опубликовано 19 июля 2017 г.

## Возможности

* Мониторинг полного стека на базе OneAgent
* [Расширения для простого развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, обнаружение AutoScale и другое

Dynatrace предоставляет VM extension для установки OneAgent на Azure Virtual Machine Scale Set (VMSS). Расширение не включает установщик OneAgent. Вместо этого оно использует Dynatrace REST API для загрузки последней версии с кластера, если только не задана [версия OneAgent по умолчанию](https://www.dynatrace.com/news/blog/define-default-version-oneagent-new-installations/). Обновления OneAgent применяются автоматически.

## Предварительные требования

* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Определите свой [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Ознакомьтесь с мониторинговыми средами и узнайте, как с ними работать.").
* При необходимости определите URL сервера.

  URL сервера требуется только в следующих случаях:

  + эндпоинт Dynatrace Managed
  + ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS

  (Для Dynatrace SaaS URL формируется автоматически на основе идентификатора среды.)

  + **URL сервера ActiveGate:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)
  + **URL сервера Dynatrace Managed:**
    `https://{your-domain}/e/{your-environment-id}/api`

  Если используется Dynatrace Managed или трафик кластера должен маршрутизироваться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "Ознакомьтесь с базовыми концепциями ActiveGate."), необходимо настроить API-эндпоинт, используемый расширением для загрузки OneAgent.

## Установка

VM extension Dynatrace доступно для Windows и Linux во всех публичных регионах Azure.

Azure CLI 2.0

PowerShell

1. Выполните приведённую ниже команду.

   Замените все значения, отмеченные `<...>`, на фактические.

   ```
   az vmss extension set



   --publisher dynatrace.ruxit



   -n "<Extension-Type>"



   -g "<Resource-Group>"



   --vmss-name "<VMSS-Name>"



   --settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
   ```

   При использовании Azure CLI в PowerShell необходимо форматировать параметры как [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

   ```
   --settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
   ```

   | Параметр | Обязательный | Описание |
   | --- | --- | --- |
   | Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута ВМ. |
   | VMSS-Name | Обязательный | Имя VMSS, на котором нужно установить расширение. |
   | Extension-Type | Обязательный | Для ВМ на базе Windows используйте `oneAgentWindows`. Для ВМ на базе Linux используйте `oneAgentLinux`. |
   | tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные требования](#prerequisites). |
   | token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
   | server | Необязательный | URL сервера для настройки альтернативного эндпоинта связи, описанного в разделе [Предварительные требования](#prerequisites). |
   | enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг журналов. |
   | hostGroup | Необязательный | Определите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит ВМ. |
2. Обновите виртуальные машины VMSS.

   ```
   az vmss update-instances --instance-ids '*' --resource-group $CLUSTER_RESOURCE_GROUP --name $SCALE_SET_NAME
   ```
3. Чтобы проверить статус развёртывания, откройте **Deployment Status**.

   После завершения установки перезапустите приложения на ВМ. Сразу после перезапуска OneAgent начнёт их мониторинг.

1. Выполните приведённую ниже команду, чтобы применить расширение к определению VMSS.

   Замените все значения, отмеченные `<...>`, на фактические.

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
   | Extension-Type | Обязательный | Для ВМ на базе Windows используйте `oneAgentWindows`. Для ВМ на базе Linux используйте `oneAgentLinux`. |
   | tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные требования](#prerequisites). |
   | token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
   | server | Необязательный | URL сервера для настройки альтернативного эндпоинта связи, описанного в разделе [Предварительные требования](#prerequisites). |
   | enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг журналов. |
   | hostGroup | Необязательный | Определите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит ВМ. |
2. Обновите виртуальные машины VMSS с новым определением.

   ```
   Update-AzVmss



   -ResourceGroupName "<Resource-Group>"



   -Name "<VMSS-Name>"



   -VirtualMachineScaleSet $vmss
   ```

   | Параметр | Обязательный | Описание |
   | --- | --- | --- |
   | Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута ВМ. |
   | VMSS-Name | Обязательный | Имя VMSS, на котором нужно установить расширение. |
3. Чтобы проверить статус развёртывания, откройте **Deployment Status**.

   После завершения установки перезапустите приложения на ВМ. Сразу после перезапуска OneAgent начнёт их мониторинг.

## Установка VM extension Dynatrace OneAgent через шаблон ARM

В дополнение к основным методам установки можно включить site extension Dynatrace в шаблоны ARM.

1. Поместите конфигурацию JSON для расширения виртуальной машины в ресурс VMSS в раздел `extensions` внутри `extensionProfile`.

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
   | Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута ВМ. |
   | VMSS-Name | Обязательный | Имя VMSS, на котором нужно установить расширение. |
   | Extension-Type | Обязательный | Для ВМ на базе Windows используйте `oneAgentWindows`. Для ВМ на базе Linux используйте `oneAgentLinux`. |
   | tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные требования](#prerequisites). |
   | token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
   | Extension-Version | Необязательный | Требуемая версия[1](#fn-1-1-def) расширения. |
   | server | Необязательный | URL сервера для настройки альтернативного эндпоинта связи, описанного в разделе [Предварительные требования](#prerequisites). |
   | enableLogAnalytics | Необязательный | Установите значение `yes`, чтобы включить мониторинг журналов. |
   | hostGroup | Необязательный | Определите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит ВМ. |

   1

   Чтобы получить список версий расширений, выполните

   ```
   az vm extension image list --name oneAgentLinux --publisher dynatrace.ruxit
   ```
3. Чтобы проверить статус развёртывания, откройте **Deployment Status**.

   После завершения установки перезапустите приложения на ВМ. Сразу после перезапуска OneAgent начнёт их мониторинг.

## Устранение неполадок

Узлы VMSS не отображаются в Dynatrace

Перезапустите узлы VMSS через PowerShell, заменив все значения, отмеченные `<...>`, на фактические:

```
Restart-AzureRmVmss -ResourceGroupName "<Resource-Group>" -VMScaleSetName "<VMSS-Name>"
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута виртуальная машина |
| VMSS-Name | Обязательный | Имя VMSS, на котором нужно установить расширение. |

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")