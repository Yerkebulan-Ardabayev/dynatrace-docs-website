---
title: Мониторинг Azure Virtual Machines
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm
scraped: 2026-05-12T11:22:41.250664
---

# Мониторинг Azure Virtual Machines

# Мониторинг Azure Virtual Machines

* Практическое руководство
* Чтение: 8 мин
* Опубликовано 19 июля 2017 г.

Dynatrace предоставляет [VM Extension](https://docs.microsoft.com/en-us/azure/virtual-machines/extensions/overview) для установки OneAgent на Azure Virtual Machines. Это позволяет использовать встроенные возможности автоматизации развёртывания через Azure Resource Manager (ARM). Dynatrace VM extension доступен для Windows и Linux во всех публичных регионах Azure (включая поддержку Classic Virtual Machines).

Site extension Dynatrace OneAgent не включает установщик OneAgent. Вместо этого расширение использует Dynatrace REST API для загрузки установщика из кластера в целевой версии, заданной в разделе [Обновления OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Узнайте, как обновить OneAgent.").

## Возможности

* Мониторинг полного стека на базе OneAgent
* [Расширения для простого развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, масштабируемые наборы и другое
* Поддерживаются также [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Мониторинг Azure Virtual Machines (classic) и просмотр доступных метрик.")

## Предварительные требования

* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Определите ваш [идентификатор окружения](/managed/discover-dynatrace/get-started/monitoring-environment "Понимание окружений мониторинга и работа с ними.").
* При необходимости определите URL сервера.

  URL сервера требуется только в следующих случаях:

  + эндпоинт Dynatrace Managed
  + ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS

  (Для Dynatrace SaaS URL формируется автоматически на основе идентификатора окружения.)

  + **ActiveGate server URL:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)
  + **Dynatrace Managed server URL:**
    `https://{your-domain}/e/{your-environment-id}/api`

  При использовании Dynatrace Managed или если трафик кластера должен направляться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "Познакомьтесь с базовыми концепциями ActiveGate."), необходимо настроить API-эндпоинт, используемый расширением для загрузки OneAgent.

## Установка VM extension Dynatrace OneAgent

Dynatrace OneAgent VM extension можно установить несколькими способами: через Azure Portal, Azure CLI, PowerShell или с помощью ARM-шаблона. Следуйте инструкциям ниже.

Azure Portal

Azure CLI 2.0

PowerShell

### Добавление расширения к существующей VM

1. В Azure Portal перейдите к существующей виртуальной машине, на которую нужно добавить расширение OneAgent.
2. В левом меню откройте **Settings** и выберите **Extensions**.
3. Выберите **Add**.
4. Выберите **Choose extension**.
5. В списке расширений выберите **Dynatrace OneAgent**.
6. Нажмите **Create** для добавления расширения.
7. На странице **Install extension** введите **environment ID**, **API token** и **server URL**. Подробнее см. в разделе [Предварительные требования](#prerequisites).
8. Укажите, нужно ли включить Log Monitoring.
9. Необязательно: укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM.
10. Нажмите **OK**.
11. Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.

После завершения установки перезапустите приложения на VM. Сразу после перезапуска OneAgent начнёт их мониторинг.

### Добавление расширения к новой VM

1. При создании новой VM в мастере развёртывания в разделе **Advanced** выберите **Select an extension**.
2. Выберите **Dynatrace OneAgent**.
3. Нажмите **Create**.
4. На странице **Install extension** введите **environment ID**, **API token** и **server URL**. Подробнее см. в разделе [Предварительные требования](#prerequisites).
5. Укажите, нужно ли включить Log Monitoring.
6. Необязательно: укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM.
7. Нажмите **OK**.
8. Продолжите настройку VM в мастере развёртывания.
9. Нажмите **Review and create**.
10. Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.

После завершения установки перезапустите приложения на VM. Сразу после перезапуска OneAgent начнёт их мониторинг.

Замените все значения, отмеченные как `<...>`, реальными значениями.

```
az vm extension set



--publisher dynatrace.ruxit



-n "<Extension-Type>"



-g "<Resource-Group>"



--vm-name "<VM-Name>"



--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

При использовании Azure CLI в PowerShell параметры settings необходимо оформить в виде [here-string](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_quoting_rules?view=powershell-6#here-strings).

```
--settings @'"{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\"}"'@
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |
| VM-Name | Обязательный | Имя VM, на которую нужно установить расширение. |
| Extension-Type | Обязательный | Для Windows-based VM используйте `oneAgentWindows`. Для Linux-based VM используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
| server | Необязательный | URL сервера, если нужно настроить альтернативный коммуникационный эндпоинт, описанный в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите `yes`, чтобы включить Log Monitoring. |
| hostGroup | Необязательный | Укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |
| overrideDefaults [1](#fn-1-1-def) | Необязательный | Переопределяет значение таймаута по умолчанию (120 секунд). Например, чтобы задать таймаут 600 секунд, добавьте `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` в строку `-Settings`; можно также оставить пустым `\"overrideDefaults\": {}` или `null`. В этих случаях применяется значение по умолчанию 120 секунд. |

1

Доступно начиная с версии VM extension 2.201.1.0.

Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.

После завершения установки перезапустите приложения на VM. Сразу после перезапуска OneAgent начнёт их мониторинг.

Замените все значения, отмеченные как `<...>`, реальными значениями.

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
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |
| Location | Обязательный | Расположение, в котором развёрнута VM. |
| VM-Name | Обязательный | Имя VM, на которую нужно установить расширение. |
| Extension-Type | Обязательный | Для Windows-based VM используйте `oneAgentWindows`. Для Linux-based VM используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). |
| Extension-Version | Необязательный | Требуемая версия расширения. |
| server | Необязательный | URL сервера, если нужно настроить альтернативный коммуникационный эндпоинт, описанный в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите `yes`, чтобы включить Log Monitoring. |
| hostGroup | Необязательный | Укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |
| overrideDefaults [1](#fn-2-1-def) | Необязательный | Переопределяет значение таймаута по умолчанию (120 секунд). Например, чтобы задать таймаут 600 секунд, добавьте `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` в строку `-Settings`; можно также оставить пустым `\"overrideDefaults\": {}` или `null`. В этих случаях применяется значение по умолчанию 120 секунд. |

1

Доступно начиная с версии VM extension 2.201.1.0.

Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.

После завершения установки перезапустите приложения на VM. Сразу после перезапуска OneAgent начнёт их мониторинг.

VM extension версии 2.201.1.0+

В версии VM extension 2.201.1.0 стало доступно задание параметра `overrideDefaults` через CLI, PowerShell [установку](#installation) и [ARM-шаблон](#arm-template).

* Теперь можно задать пользовательский таймаут (`overrideDefaults`) для загрузки Azure VM Extension, что полезно в окружениях с нестабильным интернет-соединением или низкой пропускной способностью сети.
* Сообщения об ошибках стали более информативными, что упрощает работу в автоматизированных системах.
* Обновление Azure VM Extension на Windows теперь не требует предварительной деинсталляции. Если версия OneAgent изменилась в тенанте, достаточно повторно установить Azure VM Extension для перехода на новую версию.

## Установка VM extension Dynatrace OneAgent через ARM-шаблон

В дополнение к основным методам установки можно включить Dynatrace VM extension в состав ARM-шаблонов.
JSON-файл расширения виртуальной машины можно вложить внутрь ресурса виртуальной машины или разместить в корне JSON-шаблона Resource Manager. [Расположение JSON-файла влияет на значение имени и типа ресурса](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-manager-templates-resources#child-resources).

* В следующем примере расширение OneAgent вложено внутрь ресурса виртуальной машины. При вложении ресурса расширения JSON-файл размещается в объекте "resources": [] виртуальной машины.

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
* При размещении JSON расширения в корне шаблона имя ресурса содержит ссылку на родительскую виртуальную машину, а тип отражает вложенную конфигурацию.

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
| Parent-VM-Resource | Обязательный | Имя родительского ресурса VM, на который нужно установить расширение. Не применяется при использовании вложенного ресурса. |
| VM-Name | Обязательный | Имя VM, на которую нужно установить расширение. |
| Extension-Type | Обязательный | Для Windows-based VM используйте `oneAgentWindows`. Для Linux-based VM используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор окружения, описанный в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS token, описанный в разделе [Предварительные требования](#prerequisites). Начиная с версии `2.200.0.0` рекомендуется передавать его в `protectedSettings`. |
| Extension-Version | Необязательный | Требуемая версия расширения. |
| server | Необязательный | URL сервера, если нужно настроить альтернативный коммуникационный эндпоинт, описанный в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите `yes`, чтобы включить Log Monitoring. |
| hostGroup | Необязательный | Укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |
| overrideDefaults [1](#fn-3-1-def) | Необязательный | Переопределяет значение таймаута по умолчанию (120 секунд). Например, чтобы задать таймаут 600 секунд, добавьте `\"overrideDefaults\": {\"downloadInstallerRequestTimeoutInSeconds\": 600}` в объект `settings` ARM-шаблона; можно также оставить пустым `\"overrideDefaults\": {}` или `null`. В этих случаях применяется значение по умолчанию 120 секунд. |

1

Доступно начиная с версии VM extension 2.201.1.0.

Чтобы проверить статус развёртывания, перейдите в **Deployment Status**.

После завершения установки перезапустите приложения на VM. Сразу после перезапуска OneAgent начнёт их мониторинг.

## Настройка сетевых зон (необязательно)

Для настройки сетевых зон используйте приведённые ниже аргументы установщика.

```
az vm extension set



--publisher dynatrace.ruxit



-n "oneAgentLinux"



-g "yourresourcegroup"



--vm-name "awesome-vm"



--settings "{\"tenantId\":\"myawesometenant\",\"token\":\"nope123\", \"installerArguments\":\"--set-host-group=example_hostgroup --set-monitoring-mode=fullstack --set-network-zone=<your.network.zone>\"}"
```

Подробнее см. в разделе [сетевые зоны](/managed/manage/network-zones "Узнайте, как работают сетевые зоны в Dynatrace.").

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* [Матрица поддержки платформ и возможностей OneAgent](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Узнайте, какие возможности поддерживаются OneAgent в различных операционных системах и на разных платформах.")