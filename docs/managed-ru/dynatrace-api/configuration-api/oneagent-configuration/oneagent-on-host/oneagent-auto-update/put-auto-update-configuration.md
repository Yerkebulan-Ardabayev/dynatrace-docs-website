---
title: OneAgent auto-update API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration
---

# OneAgent auto-update API - PUT configuration

# OneAgent auto-update API - PUT configuration

* Reference
* Опубликовано 03 февр. 2020 г.

Обновляет конфигурацию автообновления OneAgent на указанном хосте.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читайте в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace для нужного хоста. | path | Обязательный |
| body | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | Тело JSON запроса. Содержит параметры автообновления OneAgent. | body | Необязательный |

### Объекты тела запроса

#### Объект `HostAutoUpdateConfig`

Конфигурация автообновления OneAgent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| effectiveSetting | string | Фактическое состояние автообновления на хосте.  Применимо только если параметр **setting** установлен в значение `INHERITED`. В этом случае значение берётся из группы хостов или конфигурации на уровне окружения. Элемент может принимать следующие значения * `ENABLED` * `DISABLED` | Необязательный |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применимо только если параметр **setting** установлен в значение `INHERITED`, а параметр **version** установлен в `null`. В этом случае значение берётся из группы хостов или конфигурации на уровне окружения. | Необязательный |
| id | string | ID сущности Dynatrace хоста, на котором развёрнут OneAgent. | Необязательный |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные, полезные для отладки | Необязательный |
| setting | string | Состояние автообновления OneAgent на хосте:  * `ENABLED`: OneAgent автоматически обновляется до самой последней версии. * `DISABLED`: OneAgent обновляется до версии, указанной в поле **version**. * `INHERITED`: используется настройка из группы хостов (если хост входит в группу хостов) или конфигурация на уровне окружения (если хост не принадлежит группе хостов). Элемент может принимать следующие значения * `DISABLED` * `ENABLED` * `INHERITED` | Обязательный |
| targetVersion | string | Версия, до которой обновляется OneAgent при включённых автоматических обновлениях.  Поддерживает относительные версии `latest`, `previous` и `older`, а также конкретную версию в формате `<major>.<minor>` (например, `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например, `1.261.178.20230313-090930`).  Применимо только если параметр **setting** установлен в значение `ENABLED`. | Необязательный |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления | Необязательный |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>.<timestamp>` (например, `1.191.0.20200326-161115`). Список доступных версий можно получить с помощью вызова [GET available versions﻿](https://dt-url.net/fo23rb5?dt=m).  Если для указанной версии не найден подходящий инсталлятор или значение установлено в `null`, OneAgent не будет обновлён.  Применимо только если значение **effectiveSetting** равно `DISABLED`.  Если параметр **setting** установлен в значение `INHERITED`, но параметр **version** всё же задан, это приведёт к однократному обновлению: OneAgent будет обновлён до указанной версии, а значение **version** будет установлено в `null`. Для последующих обновлений будет использоваться родительская настройка. | Необязательный |

#### Объект `ConfigurationMetadata`

Метаданные, полезные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Необязательный |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Необязательный |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Необязательный |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| windows | [UpdateWindow](#openapi-definition-UpdateWindow)[] | Список окон обновления, в течение которых может начаться обновление OneAgent. Если значение отсутствует, а обновление должно быть выполнено, обновление начнётся при первой возможности. | Обязательный |

#### Объект `UpdateWindow`

Базовая информация об одном окне обслуживания

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | Идентификатор окна обслуживания | Обязательный |
| name | string | Название окна обслуживания | Необязательный |

### Модель JSON тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Успех. Конфигурация обновлена. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
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

### Модели JSON тела ответа

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

Рекомендуется проверять полезную нагрузку перед отправкой в составе реального запроса. Код ответа **204** означает, что полезная нагрузка корректна.

Запрос принимает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate/validator` |

### Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `WriteConfig`.

О том, как получить и использовать токен, читайте в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Проверено. Отправленная конфигурация корректна. Ответ не содержит тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка. Входные данные некорректны |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код состояния HTTP |
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

#### Модели JSON тела ответа

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