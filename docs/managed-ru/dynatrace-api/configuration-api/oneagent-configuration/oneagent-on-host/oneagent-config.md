---
title: OneAgent on a host API - OneAgent configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-config
---

# OneAgent on a host API - OneAgent configuration

# OneAgent on a host API - OneAgent configuration

* Справка
* Опубликовано 03 февраля 2020 г.

Получает конфигурацию OneAgent на указанном хосте. Позднее конфигурацию автообновления и мониторинга можно изменить одним из следующих запросов:

* [PUT конфигурация автообновления](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration "Изменение конфигурации автообновления экземпляра OneAgent через Dynatrace API.")
* [PUT конфигурация мониторинга](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Обновление конфигурации мониторинга экземпляра OneAgent через Dynatrace API.")

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace для Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace нужного хоста. | путь | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostConfig](#openapi-definition-HostConfig) | Успех |

### Объекты тела ответа

#### Объект `HostConfig`

Конфигурация OneAgent на хосте.

| Элемент | Тип | Описание |
| --- | --- | --- |
| autoUpdateConfig | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | Конфигурация автообновления OneAgent. |
| id | string | ID сущности Dynatrace хоста, на котором развёрнут OneAgent. |
| monitoringConfig | [MonitoringConfig](#openapi-definition-MonitoringConfig) | Конфигурация мониторинга OneAgent. |
| techMonitoringConfigList | [TechMonitoringConfigList](#openapi-definition-TechMonitoringConfigList) | Список конфигураций мониторинга технологий. |

#### Объект `HostAutoUpdateConfig`

Конфигурация автообновления OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления на хосте.  Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из группы хостов или конфигурации на уровне окружения. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применимо только если параметр **setting** установлен в `INHERITED`, а параметр **version** установлен в `null`. В этом случае значение берётся из группы хостов или конфигурации на уровне окружения. |
| id | string | ID сущности Dynatrace хоста, на котором развёрнут OneAgent. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| setting | string | Состояние автообновления OneAgent на хосте:  * `ENABLED`: OneAgent автоматически обновляется до самой актуальной версии. * `DISABLED`: OneAgent обновляется до версии, указанной в поле **version**. * `INHERITED`: используется настройка группы хостов (если хост входит в группу хостов) или конфигурации на уровне окружения (если хост не принадлежит группе хостов). Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Версия, до которой обновляется OneAgent, если включены автоматические обновления.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например `1.261.178.20230313-090930`).  Применимо только если параметр **setting** установлен в `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>.<timestamp>` (например `1.191.0.20200326-161115`). Список доступных версий можно получить вызовом [GET доступные версии﻿](https://dt-url.net/fo23rb5?dt=m).  Если для указанной версии не найдено подходящего установщика или значение установлено в `null`, OneAgent не будет обновлён.  Применимо только если значение **effectiveSetting** равно `DISABLED`.  Если параметр **setting** установлен в `INHERITED`, но **version** всё же задан, это приведёт к разовому обновлению: OneAgent будет обновлён до указанной версии, а значение **version** будет установлено в `null`. Для дальнейших обновлений будет использоваться родительская настройка. |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание |
| --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в которые может начаться обновление OneAgent. Если значение не задано, а обновление должно быть выполнено, обновление начнётся при первой возможности. |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор окна обслуживания |
| name | string | Название окна обслуживания |

#### Объект `MonitoringConfig`

Конфигурация мониторинга OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| autoInjectionEnabled | boolean | Если эта настройка включена, модули кода будут автоматически внедряться в отслеживаемые приложения. Эта настройка не применяется, если автовнедрение отключено через oneagentctl (см. https://dt-url.net/oneagentctl?dt=m). |
| id | string | ID сущности Dynatrace хоста, на котором развёрнут OneAgent. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| monitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`). |
| monitoringMode | string | Режим мониторинга хоста: полный стек или только инфраструктура. Элемент может принимать следующие значения * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |

#### Объект `TechMonitoringConfigList`

Список конфигураций мониторинга технологий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| technologies | [Technology](#openapi-definition-Technology)[] | Список конфигураций мониторинга технологий. |

#### Объект `Technology`

Конфигурация мониторинга технологии.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoringEnabled | boolean | Мониторинг технологии включён (`true`) или отключён (`false`). |
| scope | string | Область действия конфигурации:  * `HOST`: настройка действует только для OneAgent на хосте. Другие OneAgent, подключённые к тому же серверу Dynatrace, могут иметь другую настройку. * `ENVIRONMENT`: настройка действует для всех OneAgent, подключённых к серверу Dynatrace. Элемент может принимать следующие значения * `ENVIRONMENT` * `HOST` |
| type | string | Тип технологии. Элемент может принимать следующие значения * `AIX_KERNEL_EXT` * `APACHE` * `CIM_V2` * `DOCKER` * `DOCKER_WIN` * `DOT_NET` * `DOT_NET_CORE` * `EXTENSIONS` * `EXTENSIONS_DS_GENERIC` * `EXTENSIONS_STATSD` * `GARDEN` * `GO` * `GO_STATIC` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PHP_81` * `PHP_CGI` * `PHP_CLI` * `PHP_CLI_SERVER` * `PHP_WIN` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `VARNISH` * `Z_OS` |

### Модели тела ответа JSON

```
{



"autoUpdateConfig": {



"effectiveSetting": "DISABLED",



"effectiveVersion": "1.191.0.20200326-161115",



"id": "HOST-0123456789ABCDE",



"metadata": {



"clusterVersion": "1.192.1",



"configurationVersions": [



4,



2



],



"currentConfigurationVersions": [



"1.0.4",



"1.23"



]



},



"setting": "DISABLED",



"targetVersion": "latest",



"updateWindows": {



"windows": [



{



"id": "vu9U3hXa3q0AAAABADdkeW5hdHJhY2Uuc2V0dGluZ3MuZGVwbG95bWVudC5tYW5h",



"name": "Daily maintenance window"



}



]



},



"version": "1.191.0.20200326-161115"



},



"id": "HOST-0123456789ABCDE",



"monitoringConfig": {



"autoInjectionEnabled": true,



"id": "HOST-0123456789ABCDE",



"metadata": {},



"monitoringEnabled": true,



"monitoringMode": "FULL_STACK"



},



"techMonitoringConfigList": {



"metadata": {},



"technologies": [



{



"monitoringEnabled": true,



"scope": "ENVIRONMENT",



"type": "JAVA"



}



]



}



}
```