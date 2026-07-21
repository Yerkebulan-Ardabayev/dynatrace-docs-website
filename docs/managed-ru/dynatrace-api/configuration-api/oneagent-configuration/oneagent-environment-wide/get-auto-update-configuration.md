---
title: OneAgent environment-wide configuration API - GET auto-update configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide/get-auto-update-configuration
---

# OneAgent environment-wide configuration API - GET auto-update configuration

# OneAgent environment-wide configuration API - GET auto-update configuration

* Справка
* Опубликовано 20 октября 2020 г.

Получение конфигурации автообновления OneAgent на уровне окружения.

OneAgent, подключающиеся к окружению, используют эту конфигурацию только когда их параметр **setting** установлен в `INHERITED`.

Запрос возвращает содержимое типа `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/autoupdate` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `ReadConfig`.

Подробнее о том, как получить и использовать токен, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Запрос не предусматривает настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [EnvironmentAutoUpdateConfig](#openapi-definition-EnvironmentAutoUpdateConfig) | Успешно |

### Объекты тела ответа

#### Объект `EnvironmentAutoUpdateConfig`

Конфигурация автообновлений OneAgent на уровне Environment.

Применяется ко всем OneAgent, подключающимся к окружению, если их параметр **setting** установлен в `INHERITED`. В противном случае применяется настройка на уровне группы хостов или хоста.

| Элемент | Тип | Описание |
| --- | --- | --- |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки |
| setting | string | Состояние автообновления OneAgent, подключающихся к окружению:  * `ENABLED`: OneAgent автоматически обновляются до самой актуальной версии. * `DISABLED`: OneAgent обновляются до версии, указанной в поле **version**.  OneAgent, подключающиеся к окружению, используют эту конфигурацию только когда их параметр **setting** установлен в `INHERITED`. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` |
| targetVersion | string | Версия, до которой обновляется OneAgent при включённых автоматических обновлениях.  Поддерживаются относительные версии `latest`, `previous` и `older`, а также конкретная версия в формате `<major>.<minor>` (например, `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например, `1.261.178.20230313-090930`).  Применимо только когда параметр **setting** установлен в `ENABLED`. |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Указывается в формате `<major>.<minor>.<revision>` (например, `1.181.0`) или `<major>.<minor>` (например, `1.181`). Список доступных версий можно получить с помощью вызова [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m). Если для указанной версии не найден подходящий установщик или значение установлено в `null`, OneAgent не будет обновлён.  Применимо только когда параметр **setting** установлен в `DISABLED`. |

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

### Модели JSON тела ответа

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