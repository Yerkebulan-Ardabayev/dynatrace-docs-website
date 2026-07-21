---
title: OneAgent auto-update API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/get-auto-update-configuration
---

# OneAgent auto-update API - GET configuration

# OneAgent auto-update API - GET configuration

* Справочник
* Опубликовано 03 февраля 2020 г.

Получает конфигурацию автообновления OneAgent на указанном хосте.

Запрос формирует полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace нужного хоста. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | Успех |

### Объекты тела ответа

#### Объект `HostAutoUpdateConfig`

Конфигурация автообновления OneAgent.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления на хосте.  Применимо, только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из группы хостов или общей конфигурации окружения. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применимо, только если параметр **setting** имеет значение `INHERITED`, а параметр **version** имеет значение `null`. В этом случае значение берётся из группы хостов или общей конфигурации окружения. |
| id | string | ID сущности Dynatrace хоста, на котором развёрнут OneAgent. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| setting | string | Состояние автообновления OneAgent на хосте:  * `ENABLED`: OneAgent автоматически обновляется до самой свежей версии. * `DISABLED`: OneAgent обновляется до версии, указанной в поле **version**. * `INHERITED`: используется настройка из группы хостов (если хост входит в группу хостов) или общая конфигурация окружения (если хост не принадлежит группе хостов). Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Версия, до которой обновляется OneAgent при включённом автообновлении.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например, `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например, `1.261.178.20230313-090930`).  Применимо, только если параметр **setting** имеет значение `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажи версию в формате `<major>.<minor>.<revision>.<timestamp>` (например, `1.191.0.20200326-161115`). Список доступных версий можно получить вызовом [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m).  Если подходящий инсталлятор для указанной версии не найден или значение установлено в `null`, OneAgent не будет обновлён.  Применимо, только если значение **effectiveSetting** равно `DISABLED`.  Если параметр **setting** имеет значение `INHERITED`, но при этом задан параметр **version**, это приведёт к разовому обновлению: OneAgent будет обновлён до указанной версии, после чего значение **version** будет установлено в `null`. Для последующих обновлений будет использоваться родительская настройка. |

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
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в которые может начаться обновление OneAgent. Если значение отсутствует, а обновление должно быть выполнено, оно начнётся при первой возможности. |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор окна обслуживания |
| name | string | Название окна обслуживания |

### Примеры моделей тела ответа JSON

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