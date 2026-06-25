---
title: OneAgent auto-update API - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/oneagent-configuration/oneagent-on-host/oneagent-auto-update/put-auto-update-configuration
scraped: 2026-05-12T11:21:17.209085
---

# OneAgent auto-update API - PUT configuration

# OneAgent auto-update API - PUT configuration

* Reference
* Published Feb 03, 2020

Обновляет конфигурацию авто-обновления OneAgent на указанном хосте.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID сущности Dynatrace требуемого хоста. | path | Required |
| body | [HostAutoUpdateConfig](#openapi-definition-HostAutoUpdateConfig) | JSON-тело запроса. Содержит параметры авто-обновления OneAgent. | body | Optional |

### Объекты тела запроса

#### Объект `HostAutoUpdateConfig`

Конфигурация авто-обновления OneAgent.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| effectiveSetting | string | Фактическое состояние авто-обновления на хосте.  Применяется только если параметр **setting** имеет значение `INHERITED`. В этом случае значение берётся из конфигурации группы хостов или для всего окружения. Возможные значения: * `ENABLED` * `DISABLED` | Optional |
| effectiveVersion | string | Фактическая версия, до которой должен быть обновлён OneAgent.  Применяется только если параметр **setting** имеет значение `INHERITED`, а параметр **version** имеет значение `null`. В этом случае значение берётся из конфигурации группы хостов или для всего окружения. | Optional |
| id | string | ID сущности Dynatrace хоста, где развёрнут OneAgent. | Optional |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки | Optional |
| setting | string | Состояние авто-обновления OneAgent на хосте:  * `ENABLED`: OneAgent автоматически обновляется до последней версии. * `DISABLED`: OneAgent обновляется до версии, указанной в поле **version**. * `INHERITED`: используется настройка из группы хостов (если хост входит в группу хостов) или конфигурации для всего окружения (если хост не принадлежит группе хостов). Возможные значения: * `DISABLED` * `ENABLED` * `INHERITED` | Required |
| targetVersion | string | Версия, до которой обновлять OneAgent при включённых автоматических обновлениях.  Поддерживаются относительные версии `latest`, `previous` и `older`, а также конкретная версия в формате `<major>.<minor>` (например `1.261`) или `<major>.<minor>.<revision>.<timestamp>` (например `1.261.178.20230313-090930`).  Применяется только когда параметр **setting** имеет значение `ENABLED`. | Optional |
| updateWindows | [UpdateWindowsConfig](#openapi-definition-UpdateWindowsConfig) | Базовая информация обо всех настроенных окнах обновления | Optional |
| version | string | Версия, до которой должен быть обновлён OneAgent.  Укажите версию в формате `<major>.<minor>.<revision>.<timestamp>` (например `1.191.0.20200326-161115`). Список доступных версий можно получить вызовом [GET available versions](https://dt-url.net/fo23rb5).  Если для указанной версии не найден подходящий установщик или значение равно `null`, OneAgent не будет обновлён.  Применяется только когда значение **effectiveSetting** равно `DISABLED`.  Если параметр **setting** имеет значение `INHERITED`, но **version** всё ещё задан, это приведёт к разовому обновлению: OneAgent будет обновлён до указанной версии, а значение **version** будет установлено в `null`. Для дальнейших обновлений будет использоваться родительская настройка. | Optional |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. | Optional |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. | Optional |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. | Optional |

#### Объект `UpdateWindowsConfig`

Базовая информация обо всех настроенных окнах обновления

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| windows | [UpdateWindow[]](#openapi-definition-UpdateWindow) | Список окон обновления, когда может начаться обновление OneAgent. Если значение отсутствует, а обновление должно быть выполнено, оно начнётся при первой возможности. | Required |

#### Объект `UpdateWindow`

Базовая информация об одном maintenance window

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| id | string | Идентификатор maintenance window | Required |
| name | string | Имя maintenance window | Optional |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно адаптировать под реальный запрос.

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
| **204** | - | Успех. Конфигурация обновлена. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

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

## Validate payload

Рекомендуется валидировать payload перед отправкой реального запроса. Код ответа **204** означает валидный payload.

Запрос принимает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/hosts/{id}/autoupdate/validator` |

### Аутентификация

Для выполнения этого запроса нужен access token со scope `WriteConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Ответ

#### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **204** | - | Validated. Переданная конфигурация валидна. Ответ без тела. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Сбой. Невалидный ввод |

#### Объекты тела ответа

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код статуса |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Возможные значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### JSON-модели тела ответа

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