---
title: OneAgent in a host group API - PUT auto-update configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-in-host-group/put-auto-update-configuration
---

# OneAgent in a host group API - PUT auto-update configuration

# OneAgent in a host group API - PUT auto-update configuration

* Справка
* Опубликовано 20 октября 2020 г.

Обновляет конфигурацию автообновления OneAgent в указанной группе хостов.

OneAgentы, установленные на хостах группы хостов, используют эту конфигурацию только когда их **setting** установлен в `INHERITED`.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace для нужной группы хостов. | path | Обязательный |
| body | [HostGroupAutoUpdateConfig](#openapi-definition-HostGroupAutoUpdateConfig) | Тело JSON запроса. Содержит параметры автообновления OneAgent. | body | Опциональный |

### Объекты тела запроса

#### Объект `HostGroupAutoUpdateConfig`

Конфигурация автообновления OneAgent в группе хостов.

Применяется ко всем OneAgentам, установленным на хостах группы хостов, если их параметр **setting** установлен в `INHERITED`. Иначе применяется настройка на уровне хоста.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления на хостах в группе хостов.  Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из настройки на уровне окружения. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` | Опциональный |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применимо только если параметр **setting** установлен в `INHERITED`. В этом случае значение берётся из настройки на уровне окружения. | Опциональный |
| id | string | ID сущности Dynatrace группы хостов. | Опциональный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Опциональный |
| setting | string | Состояние автообновления OneAgentов в группе хостов:  * `ENABLED`: OneAgentы автоматически обновляются до самой новой версии. * `DISABLED`: OneAgentы обновляются до версии, указанной в поле **version**. * `INHERITED`: используется настройка из конфигурации на уровне окружения.  OneAgentы, установленные на хостах группы хостов, используют эту конфигурацию только когда их параметр **setting** установлен в `INHERITED`. Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` | Обязательный |
| targetVersion | string | Версия, до которой обновляется OneAgent при включённых автоматических обновлениях.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например, `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например, `1.261.178.20230313-090930`).  Применимо только когда параметр **setting** установлен в `ENABLED`. | Опциональный |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления | Опциональный |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажи версию в формате `<major>.<minor>.<revision>` (например, `1.181.0`) или `<major>.<minor>` (например, `1.181`). Список доступных версий можно получить вызовом [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m). Если для указанной версии не найдено подходящего установщика или значение установлено в `null`, OneAgent не будет обновлён.  Применимо только когда параметр **setting** установлен в `DISABLED`. | Опциональный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Опциональный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Опциональный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Опциональный |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, когда может начаться обновление OneAgent. Если значение отсутствует и обновление должно быть выполнено, обновление начнётся при первой возможности. | Обязательный |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | Идентификатор окна обслуживания | Обязательный |
| name | string | Название окна обслуживания | Опциональный |

### Модель тела JSON запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Модели тела JSON ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Проверка полезной нагрузки

Рекомендуется проверять полезную нагрузку перед отправкой её с реальным запросом. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает полезную нагрузку `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hostgroups/{id}/autoupdate/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читай в разделе [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны. |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать следующие значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Модели тела JSON ответа

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```