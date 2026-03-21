---
title: Microsoft Azure Arc-enabled servers
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-arc-enabled-servers
scraped: 2026-03-06T21:25:35.037946
---

# Серверы с поддержкой Microsoft Azure Arc


* Latest Dynatrace

## Возможности

* Полностековый мониторинг на базе OneAgent
* [Расширения для простого развертывания OneAgent](#installation)
* [Интеграция с Azure Monitor](../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")
* Расширенная поддержка метаданных виртуальных машин Azure, таких как регионы Azure, масштабируемые наборы и т. д.
* Поддерживаются также [классические виртуальные машины](azure-vm/monitor-azure-virtual-machines-classic.md "Мониторинг классических виртуальных машин Azure и просмотр доступных метрик.")

## Предварительные требования

* Создайте [PaaS-токен](../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте о концепции токена доступа и его областях действия.").
* Определите ваш [идентификатор среды](../../../discover-dynatrace/get-started/monitoring-environment.md "Изучите работу со средами мониторинга.").
* При необходимости определите URL-адрес сервера.

  URL-адрес сервера требуется только при использовании ActiveGate для конечной точки Dynatrace SaaS. URL-адрес автоматически генерируется из идентификатора среды.

  + **URL-адрес сервера ActiveGate:**
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (порт ActiveGate настраивается)

## Установка расширения Dynatrace OneAgent VM

Существует несколько способов установки расширения Dynatrace OneAgent VM: через портал Azure, Azure CLI или PowerShell, а также с помощью шаблона ARM. Следуйте приведенным ниже инструкциям.

Портал Azure

Azure CLI 2.0

Шаблон ARM

### Добавление расширения к существующей виртуальной машине

1. На портале Azure перейдите к существующему ресурсу Azure Arc Machine.
2. В левом меню перейдите в **Settings** > **Extensions**.
3. Выберите **Add**.
4. В списке расширений выберите **Dynatrace OneAgent**.
5. Выберите **Next** для добавления расширения.
6. На странице **Configure Dynatrace OneAgent Extension** введите ваш **Environment ID**, **API Token** и **Server URL**. Подробности см. в разделе [Предварительные требования](#prerequisites).
7. Необязательно: определите дополнительные параметры OneAgent (например, прокси, порт).
8. Выберите **Review + create**.
9. Чтобы проверить статус развертывания, в вашей среде Dynatrace перейдите в **Deployment Status**.

```
az connectedmachine extension create


--publisher "Dynatrace.Ruxit"


--type "<Extension-Type>"


--name "<Extension-Type>"


--resource-group "<Resource-Group>"


--machine-name "<Azure Arc Server Name>"


--location <Azure Region>


--settings "{\"tenantId\":\"<Environment-ID>\",\"token\":\"<API-Token>\", \"server\":\"<Server-Url>\", \"enableLogAnalytics\":\"yes\", \"hostGroup\":\"<Host-Group>\"}"
```

| Параметр | Обязательность | Описание |
| --- | --- | --- |
| Resource-Group | Обязательный | Имя группы ресурсов, в которой развернута виртуальная машина. |
| Azure Arc Server Name | Обязательный | Имя расширения машины. |
| Extension-Type | Обязательный | Для виртуальных машин на базе Windows используйте `oneAgentWindows`. Для виртуальных машин на базе Linux используйте `oneAgentLinux`. |
| Extension-name | Обязательный | Для виртуальных машин на базе Windows используйте `oneAgentWindows`. Для виртуальных машин на базе Linux используйте `oneAgentLinux`. |
| Azure Region | Обязательный | Регион Azure ресурса |
| tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS-токен, описанный в разделе [Предварительные требования](#prerequisites). |
| server | Необязательный | URL-адрес сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в разделе [Предварительные требования](#prerequisites). |
| enableLogsAnalytics | Необязательный | Установите `yes`, если хотите включить мониторинг журналов. |
| hostGroup | Необязательный | Определите [группу хостов](../../../observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups.md "Узнайте, как Dynatrace позволяет организовать хосты, процессы и сервисы с помощью групп хостов."), к которой принадлежит виртуальная машина. |

В качестве альтернативы основным методам установки вы можете включить расширение Dynatrace VM в шаблоны ARM.

[JSON-файл](https://dt-url.net/9f03wr8) для расширения виртуальной машины может быть вложен в ресурс виртуальной машины или размещен на корневом или верхнем уровне JSON-шаблона Resource Manager. Размещение JSON-файла влияет на значение имени и типа ресурса.

Пример

В следующем примере предполагается, что расширение OneAgent вложено в ресурс виртуальной машины. При вложении ресурса расширения JSON-файл размещается в объекте `"resources": []` виртуальной машины.

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

| Параметр | Обязательность | Описание |
| --- | --- | --- |
| Parent-Arc Machine-Resource | Обязательный | Имя ресурса Azure Arc Machine, на котором вы хотите установить расширение. Не применяется при использовании вложенного ресурса. |
| Arc Machine Name | Обязательный | Имя Azure Arc Machine, на которой вы хотите установить расширение. |
| Extension-Type | Обязательный | Для виртуальных машин на базе Windows используйте `oneAgentWindows`. Для виртуальных машин на базе Linux используйте `oneAgentLinux`. |
| tenantId | Обязательный | Идентификатор среды, описанный в разделе [Предварительные требования](#prerequisites). |
| token | Обязательный | PaaS-токен, описанный в разделе [Предварительные требования](#prerequisites). Начиная с версии Microsoft Azure Arc 2.200.0.0 рекомендуется передавать его в `protectedSettings`. |
| server | Необязательный | URL-адрес сервера, если вы хотите настроить альтернативную конечную точку связи, как описано в разделе [Предварительные требования](#prerequisites). |

Чтобы проверить статус развертывания, в вашей среде Dynatrace перейдите в **Manage** > **Deployment status**.

После завершения установки OneAgent начнет мониторинг.
