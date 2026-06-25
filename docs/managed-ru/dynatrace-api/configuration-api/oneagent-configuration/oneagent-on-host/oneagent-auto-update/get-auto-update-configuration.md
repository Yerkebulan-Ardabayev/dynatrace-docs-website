---
title: OneAgent auto-update API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/get-auto-update-configuration
scraped: 2026-05-12T11:21:18.649214
---

# OneAgent auto-update API - GET configuration

# OneAgent auto-update API - GET configuration

* Reference
* Published Feb 03, 2020

Возвращает конфигурацию авто-обновления OneAgent на указанном хосте.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |

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
| **200** | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | Успех |

### Объекты тела ответа

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

### JSON-модели тела ответа

```
{



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



}
```