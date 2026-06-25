---
title: OneAgent in a host group API - GET auto-update configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group/get-auto-update-configuration
scraped: 2026-05-12T11:17:35.337036
---

# OneAgent in a host group API - GET auto-update configuration

# OneAgent in a host group API - GET auto-update configuration

* Reference
* Published Oct 20, 2020

Возвращает конфигурацию авто-обновления OneAgent в указанной группе хостов.

OneAgent, установленные на хостах группы хостов, используют эту конфигурацию только когда их **setting** имеет значение `INHERITED`.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace требуемой группы хостов. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostGroupAutoUpdateConfig](#openapi-definition-HostGroupAutoUpdateConfig) | Успех |

### Объекты тела ответа

#### Объект `HostGroupAutoUpdateConfig`

Конфигурация авто-обновления OneAgent в группе хостов.

Применяется ко всем OneAgent, установленным на хостах группы хостов, если их параметр **setting** имеет значение `INHERITED`. Иначе применяется настройка уровня хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние авто-обновления на хостах группы хостов.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из настройки для всего окружения. Возможные значения: * `ENABLED` * `DISABLED` |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из настройки для всего окружения. |
| id | string | ID сущности Dynatrace группы хостов. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| setting | string | Состояние авто-обновления OneAgent в группе хостов:  * `ENABLED`: OneAgent автоматически обновляются до последней версии. * `DISABLED`: OneAgent обновляются до версии, указанной в поле **version**. * `INHERITED`: используется настройка из конфигурации для всего окружения.  OneAgent, установленные на хостах группы хостов, используют эту конфигурацию только когда их параметр **setting** имеет значение `INHERITED`. Возможные значения: * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Версия, до которой обновлять OneAgent при включённых автоматических обновлениях.  Поддерживаются относительные версии `latest`, `previous` и `older`, а также конкретная версия в формате `<major>.<minor>` (например `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например `1.261.178.20230313-090930`).  Применяется только когда параметр **setting** имеет значение `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>` (например `1.181.0`) или `<major>.<minor>` (например `1.181`). Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5). Если для указанной версии не найден подходящий установщик или значение равно `null`, OneAgent не будет обновлён.  Применяется только когда параметр **setting** имеет значение `DISABLED`. |

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

### JSON-модели тела ответа

```
{



"effectiveSetting": "DISABLED",



"effectiveVersion": "1.181.0",



"id": "HOST_GROUP-0123456789ABCDE",



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



"version": "1.181.0"



}
```