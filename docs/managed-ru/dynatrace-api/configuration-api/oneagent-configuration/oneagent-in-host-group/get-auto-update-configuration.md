---
title: OneAgent in a host group API - GET auto-update configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group/get-auto-update-configuration
---

# OneAgent in a host group API - GET auto-update configuration

# OneAgent in a host group API - GET auto-update configuration

* Справка
* Опубликовано 20 окт. 2020 г.

Возвращает конфигурацию автообновления OneAgent в указанной host group.

OneAgentы, установленные на хостах host group, используют эту конфигурацию только если их **setting** установлен в `INHERITED`.

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace требуемой host group. | path | Обязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [HostGroupAutoUpdateConfig](#openapi-definition-HostGroupAutoUpdateConfig) | Успех |

### Объекты тела ответа

#### Объект `HostGroupAutoUpdateConfig`

Конфигурация автообновления OneAgent в host group.

Применяется ко всем OneAgentам, установленным на хостах host group, если их параметр **setting** установлен в `INHERITED`. В противном случае применяется настройка уровня хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления на хостах в host group.  Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из настройки на уровне окружения. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из настройки на уровне окружения. |
| id | string | ID сущности Dynatrace host group. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| setting | string | Состояние автообновления OneAgentов в host group:  * `ENABLED`: OneAgentы автоматически обновляются до самой актуальной версии. * `DISABLED`: OneAgentы обновляются до версии, указанной в поле **version**. * `INHERITED`: используется настройка из конфигурации на уровне окружения.  OneAgentы, установленные на хостах host group, используют эту конфигурацию только если их параметр **setting** установлен в `INHERITED`. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` |
| targetVersion | string | Версия, до которой обновляется OneAgent при включённых автоматических обновлениях.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например, `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например, `1.261.178.20230313-090930`).  Применимо только если параметр **setting** установлен в `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажи версию в формате `<major>.<minor>.<revision>` (например, `1.181.0`) или `<major>.<minor>` (например, `1.181`). Список доступных версий можно получить с помощью вызова [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m). Если для указанной версии не найден подходящий установщик или значение установлено в `null`, OneAgent не будет обновлён.  Применимо только если параметр **setting** установлен в `DISABLED`. |

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
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в которые может начаться обновление OneAgent. Если значение отсутствует и обновление должно быть выполнено, оно начнётся при первой возможности. |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | Идентификатор окна обслуживания |
| name | string | Название окна обслуживания |

### JSON модели тела ответа

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