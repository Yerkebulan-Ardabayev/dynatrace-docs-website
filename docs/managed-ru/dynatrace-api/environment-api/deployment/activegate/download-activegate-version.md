---
title: Deployment API - Download ActiveGate of specific version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/download-activegate-version
---

# Deployment API - Download ActiveGate of specific version

# Deployment API - Download ActiveGate of specific version

* Справка
* Обновлено 23 июня 2026 г.

Загружает установщик ActiveGate указанной версии. Список доступных версий ActiveGate можно получить с помощью вызова [GET available versions of ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions "List available versions of ActiveGate via Dynatrace API.").

В Dynatrace Managed версии 1.344+, когда версия задана как **целевая версия** ActiveGate в [конфигурации автообновления ActiveGate](/managed/dynatrace-api/environment-api/activegates/auto-update-config "Manage auto-update configuration of your Environment ActiveGates via the Dynatrace API."), кластер сохраняет её установщик (защита build-unit). Поэтому установщик остаётся доступным для загрузки через эту конечную точку даже после того, как более старые сборки той же основной версии удаляются в ходе штатного обслуживания кластера.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/{osType}/version/{version}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/{osType}/version/{version}` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа с областью действия `InstallerDownload`.

О том, как получить и использовать его, рассказано в разделе [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| If-None-Match | string | ETag предыдущего запроса. Не загружать, если он совпадает с ETag установщика. | header | Опциональный |
| osType | string | Операционная система установщика. Элемент может принимать следующие значения * `windows` * `unix` | path | Обязательный |
| version | string | Требуемая версия установщика ActiveGate в формате `1.155.275.20181112-084458`.  Список доступных версий можно получить с помощью вызова [**GET available versions of ActiveGate**﻿](https://dt-url.net/kh43rha?dt=m). | path | Обязательный |
| networkZone | string | Сетевая зона, для которой нужно настроить результат. Указанная сетевая зона должна существовать, иначе запрос завершится ошибкой. Требует ActiveGate версии не ниже 1.247. | query | Опциональный |
| arch | string | Архитектура операционной системы:  * `all`: по умолчанию `amd64`. * `amd64`: архитектура amd64. * `s390`: архитектура S/390, поддерживается только для Linux. * `arm64`: архитектура arm64, поддерживается только для Linux. Элемент может принимать следующие значения * `all` * `amd64` * `arm64` * `s390` | query | Опциональный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | string | Успешно. Полезная нагрузка содержит файл установщика. |
| **304** | - | Не изменено. У вас уже есть актуальная версия установщика. Ответ не содержит полезной нагрузки. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | Код статуса HTTP |
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