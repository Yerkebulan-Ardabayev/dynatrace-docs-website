---
title: OneAgent environment-wide configuration API - GET auto-update configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide/get-auto-update-configuration
scraped: 2026-05-12T11:15:19.377254
---

# OneAgent environment-wide configuration API - GET auto-update configuration

# OneAgent environment-wide configuration API - GET auto-update configuration

* Reference
* Published Oct 20, 2020

Возвращает конфигурацию авто-обновления OneAgent для всего окружения.

OneAgent, подключающиеся к окружению, используют эту конфигурацию только когда их **setting** имеет значение `INHERITED`.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EnvironmentAutoUpdateConfig](#openapi-definition-EnvironmentAutoUpdateConfig) | Успех |

### Объекты тела ответа

#### Объект `EnvironmentAutoUpdateConfig`

Конфигурация авто-обновлений OneAgent для всего окружения.

Применяется ко всем OneAgent, подключающимся к окружению, если их параметр **setting** имеет значение `INHERITED`. Иначе применяется настройка уровня группы хостов или хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| setting | string | Состояние авто-обновления OneAgent, подключающихся к окружению:  * `ENABLED`: OneAgent автоматически обновляются до последней версии. * `DISABLED`: OneAgent обновляются до версии, указанной в поле **version**.  OneAgent, подключающиеся к окружению, используют эту конфигурацию только когда их параметр **setting** имеет значение `INHERITED`. Возможные значения: * `ENABLED` * `DISABLED` |
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