---
title: Серверы Microsoft Azure с поддержкой Azure Arc
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers
scraped: 2026-05-12T11:38:12.172038
---

# Серверы Microsoft Azure с поддержкой Azure Arc

# Серверы Microsoft Azure с поддержкой Azure Arc

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 10 декабря 2024 г.

## Возможности

* Мониторинг полного стека на базе OneAgent
* [Расширения для простого развёртывания OneAgent](#installation)
* [Интеграция с Azure Monitor](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных Azure VM, таких как регионы Azure, масштабируемые наборы и другое
* Также поддерживаются [Classic Virtual Machines](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-vm/monitor-azure-virtual-machines-classic "Мониторинг Azure Virtual Machines (classic) и просмотр доступных метрик.")

## Предварительные требования

* Создайте [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Изучите концепцию токена доступа и его области действия.").
* Определите [идентификатор среды](/managed/discover-dynatrace/get-started/monitoring-environment "Понять и научиться работать со средами мониторинга.").
* При необходимости определите URL сервера.

  URL сервера требуется только при использовании одного из следующих вариантов:

  + эндпоинт Dynatrace Managed
  + ActiveGate для эндпоинта Dynatrace Managed или Dynatrace SaaS

  (Для Dynatrace SaaS URL генерируется автоматически на основе идентификатора среды.)

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate можно настраивать)
  + **Dynatrace Managed server URL:**  
    `https://{your-domain}/e/{your-environment-id}/api`

  При использовании Dynatrace Managed или если трафик кластера должен маршрутизироваться через [ActiveGate](/managed/ingest-from/dynatrace-activegate "Основные концепции, связанные с ActiveGate."), необходимо настроить эндпоинт API, используемый расширением для загрузки OneAgent.

## Установка VM extension Dynatrace OneAgent

VM extension Dynatrace OneAgent можно установить несколькими способами: через Azure Portal, Azure CLI, PowerShell или с помощью шаблона ARM. Следуйте инструкциям ниже.

Azure Portal

Azure CLI 2.0

ARM template

### Добавление расширения к существующей VM

1. В Azure Portal перейдите к существующему ресурсу Azure Arc Machine.
2. В левом меню откройте **Settings** > **Extensions**.
3. Выберите **Add**.
4. В списке расширений выберите **Dynatrace OneAgent**.
5. Выберите **Next** для добавления расширения.
6. На странице **Configure Dynatrace OneAgent Extension** введите **Environment ID**, **API Token** и **Server URL**. Подробнее см. в разделе [Предварительные требования](#prerequisites).
7. Необязательно: задайте дополнительные настройки OneAgent (например, прокси, порт).
8. Выберите **Review + create**.
9. Чтобы проверить статус развёртывания, в среде Dynatrace откройте **Deployment Status**.

```
az connectedmachine extension create



--publisher "Dynatrace.Ruxit"



--type "<Extension-Type>"



--name “<Extension-Type>”



--resource-group "<Resource-Group>"



--machine-name "<Azure Arc Server Name>"



--location <Azure Region>



--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развёрнута VM. |
| Azure Arc Server Name | Обязательный | Имя расширения машины. |
| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
| Extension-name | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
| Azure Region | Обязательный | Регион Azure ресурса. |
| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS token, как описано в разделе [Предварительные требования](#prerequisites). |
| server | Необязательный | URL сервера, если нужно настроить альтернативный эндпоинт связи, как описано в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите значение `yes`, чтобы включить Log Monitoring. |
| hostGroup | Необязательный | Укажите [группу хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит VM. |

Помимо основных способов установки, VM extension Dynatrace можно включить в шаблоны ARM.

[Файл JSON](https://dt-url.net/9f03wr8) для расширения виртуальной машины можно вложить в ресурс виртуальной машины или разместить на корневом уровне шаблона JSON диспетчера ресурсов. Расположение файла JSON влияет на значения имени и типа ресурса.

Пример

В следующем примере расширение OneAgent вложено в ресурс виртуальной машины. При вложении ресурса расширения файл JSON размещается в объекте `"resources": []` виртуальной машины.

```
{



    "$schema": "https://schema.management.azure.com/schemas/2019-04-01/deploymentTemplate.json#",



    "contentVersion": "1.0.0.0",



    "parameters": {



        "vmName": {



            "type": "string"



        },



        "location": {



            "type": "string"



        },



        "tenant": {



            "type": "string"



        },



        "token": {



            "type": "securestring"



        },



        "server": {



            "type": "string",



            "defaultValue": ""



        }



    },



    "resources": [



        {



            "name": "[concat(parameters('vmName'),'/<Extension-Type>')]",



            "type": "Microsoft.HybridCompute/machines/extensions",



            "location": "[parameters('location')]",



            "apiVersion": "2022-03-10",



            "properties": {



                "publisher": "dynatrace.ruxit",



                "type": " <Extension-Type>",



                "autoUpgradeMinorVersion": true,



                "settings": {



                    "tenantId": "[parameters('tenant')]",



                    "server": "[parameters('server')]"



                },



                "protectedSettings": {



                    "token": "[parameters('token')]"



                }



            }



        }



    ]



}
```

| Параметр | Обязательный | Описание |
| --- | --- | --- |
| Parent-Arc Machine-Resource | Обязательный | Имя ресурса Azure Arc Machine, на котором нужно установить расширение. Неприменимо при использовании вложенного ресурса. |
| Arc Machine Name | Обязательный | Имя Azure Arc Machine, на котором нужно установить расширение. |
| Extension-Type | Обязательный | Для VM на базе Windows используйте `oneAgentWindows`. Для VM на базе Linux используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор среды, как описано в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS token, как описано в разделе [Предварительные требования](#prerequisites). Начиная с версии Microsoft Azure Arc 2.200.0.0, рекомендуется передавать его в `protectedSettings`. |
| server | Необязательный | URL сервера, если нужно настроить альтернативный эндпоинт связи, как описано в разделе [Предварительные требования](#prerequisites). |

Чтобы проверить статус развёртывания, в среде Dynatrace откройте **Manage** > **Deployment status**.

После завершения установки OneAgent начнёт мониторинг.