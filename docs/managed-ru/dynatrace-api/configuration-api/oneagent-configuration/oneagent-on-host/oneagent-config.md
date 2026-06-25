---
title: OneAgent on a host API - OneAgent configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-config
scraped: 2026-05-12T11:21:20.541269
---

# OneAgent on a host API - OneAgent configuration

# OneAgent on a host API - OneAgent configuration

* Reference
* Published Feb 03, 2020

Возвращает конфигурацию OneAgent на указанном хосте. Изменить конфигурацию авто-обновления и мониторинга можно позже одним из следующих запросов:

* [PUT auto-update configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration "Редактирование конфигурации авто-обновления OneAgent-инстанса через Dynatrace API.")
* [PUT monitoring configuration](/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-monitoring/put-monitoring-configuration "Обновление конфигурации мониторинга OneAgent-инстанса через Dynatrace API.")

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace требуемого хоста. | path | Required |

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
| autoUpdateConfig | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | Конфигурация авто-обновления OneAgent. |
| id | string | ID сущности Dynatrace хоста, где развёрнут OneAgent. |
| monitoringConfig | [MonitoringConfig](#openapi-definition-MonitoringConfig) | Конфигурация мониторинга OneAgent. |
| techMonitoringConfigList | [TechMonitoringConfigList](#openapi-definition-TechMonitoringConfigList) | Список конфигураций мониторинга технологий. |

#### Объект `HostAutoUpdateConfig`

Конфигурация авто-обновления OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние авто-обновления на хосте.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из конфигурации группы хостов или для всего окружения. Возможные значения: * `ENABLED` * `DISABLED` |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применяется только если параметр **setting** имеет значение `INHERITED`, а параметр **version** имеет значение `null`. В этом случае значение берётся из конфигурации группы хостов или для всего окружения. |
| id | string | ID сущности Dynatrace хоста, где развёрнут OneAgent. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| setting | string | Состояние авто-обновления OneAgent на хосте:  * `ENABLED`: OneAgent автоматически обновляется до последней версии. * `DISABLED`: OneAgent обновляется до версии, указанной в поле **version**. * `INHERITED`: используется настройка из группы хостов (если хост входит в группу хостов) или конфигурации для всего окружения (если хост не принадлежит группе хостов). Возможные значения: * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Версия, до которой обновлять OneAgent при включённых автоматических обновлениях.  Поддерживаются относительные версии `latest`, `previous` и `older`, а также конкретная версия в формате `<major>.<minor>` (например `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например `1.261.178.20230313-090930`).  Применяется только когда параметр **setting** имеет значение `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>.<timestamp>` (например `1.191.0.20200326-161115`). Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5).  Если для указанной версии не найден подходящий установщик или значение равно `null`, OneAgent не будет обновлён.  Применяется только когда значение **effectiveSetting** равно `DISABLED`.  Если параметр **setting** имеет значение `INHERITED`, но **version** всё ещё задан, это приведёт к разовому обновлению: OneAgent будет обновлён до указанной версии, а значение **version** будет установлено в `null`. Для дальнейших обновлений будет использоваться родительская настройка. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание |
| --- | --- | --- |
| windows | [UpdateWindow[]](#openapi-definition-UpdateWindow) | Список окон обновления, когда может начаться обновление OneAgent. Если значение отсутствует, а обновление должно быть выполнено, оно начнётся при первой возможности. |

#### Объект `UpdateWindow`

Базовая информация об одном maintenance window

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор maintenance window |
| name | string | Имя maintenance window |

#### Объект `MonitoringConfig`

Конфигурация мониторинга OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| autoInjectionEnabled | boolean | Кодовые модули будут автоматически внедряться в отслеживаемые приложения, если эта настройка включена. Эта настройка не применяется, если авто-внедрение отключено через oneagentctl (см. https://dt-url.net/oneagentctl). |
| id | string | ID сущности Dynatrace хоста, где развёрнут OneAgent. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| monitoringEnabled | boolean | Мониторинг включён (`true`) или отключён (`false`). |
| monitoringMode | string | Режим мониторинга хоста: полный стек или только инфраструктура. Возможные значения: * `CLOUD_INFRASTRUCTURE` * `DISCOVERY` * `FULL_STACK` |

#### Объект `TechMonitoringConfigList`

Список конфигураций мониторинга технологий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| technologies | [Technology[]](#openapi-definition-Technology) | Список конфигураций мониторинга технологий. |

#### Объект `Technology`

Конфигурация мониторинга технологий.

| Элемент | Тип | Описание |
| --- | --- | --- |
| monitoringEnabled | boolean | Мониторинг технологии включён (`true`) или отключён (`false`). |
| scope | string | Валидность конфигурации:  * `HOST`: настройка действует только для OneAgent на хосте. Другие OneAgent, подключённые к тому же серверу Dynatrace, могут иметь другую настройку. * `ENVIRONMENT`: настройка действует для всех OneAgent, подключённых к серверу Dynatrace. Возможные значения: * `ENVIRONMENT` * `HOST` |
| type | string | Тип технологии. Возможные значения: * `AIX_KERNEL_EXT` * `APACHE` * `CIM_V2` * `DOCKER` * `DOCKER_WIN` * `DOT_NET` * `DOT_NET_CORE` * `EXTENSIONS` * `EXTENSIONS_DS_GENERIC` * `EXTENSIONS_STATSD` * `GARDEN` * `GO` * `GO_STATIC` * `IBM_INTEGRATION_BUS` * `IIS` * `JAVA` * `LOG_ANALYTICS` * `NETTRACER` * `NETWORK` * `NGINX` * `NODE_JS` * `OPENTRACINGNATIVE` * `PHP` * `PHP_81` * `PHP_CGI` * `PHP_CLI` * `PHP_CLI_SERVER` * `PHP_WIN` * `PROCESS` * `PYTHON` * `RUBY` * `SDK` * `VARNISH` * `Z_OS` |

### JSON-модели тела ответа

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