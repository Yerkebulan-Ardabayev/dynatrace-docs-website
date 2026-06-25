---
title: Deployment API - List available versions of OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions
scraped: 2026-05-12T11:58:31.687130
---

# Deployment API - List available versions of OneAgent

# Deployment API - List available versions of OneAgent

* Справочник
* Опубликовано 28 августа 2019 г.

Перечисляет все доступные версии инсталлятора OneAgent.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/{osType}/{installerType}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/versions/{osType}/{installerType}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| osType | string | Операционная система инсталлятора. Поле может принимать значения: * `windows` * `unix` * `aix` * `solaris` * `zos` | path | Обязательный |
| installerType | string | Тип инсталлятора:  * `default`: самораспаковывающийся инсталлятор для ручной установки. Скачивает файл `.exe` для Windows или файл `.sh` для Unix. * `default-unattended`: самораспаковывающийся инсталлятор для автоматической установки. Только Windows. Скачивает архив `.zip`, содержащий инсталлятор `.msi` и пакетный файл. Эта опция устарела начиная с OneAgent версии 1.173 * `mainframe`: скачивает все code modules для z/OS, объединённые в один архив `*.pax`. * `paas`: инсталлятор code modules. Скачивает архив `*.zip`, содержащий файл `manifest.json` с метаинформацией или файл `.jar` для z/OS. * `paas-sh`: инсталлятор code modules. Скачивает самораспаковывающийся shell-скрипт со встроенным архивом `tar.gz`. Поле может принимать значения: * `default` * `default-unattended` * `mainframe` * `paas` * `paas-sh` | path | Обязательный |
| flavor | string | Вариант вашего дистрибутива Linux:  * `musl` для дистрибутивов Linux, использующих стандартную библиотеку C musl, например Alpine Linux. * `multidistro` для дистрибутивов Linux, использующих стандартные библиотеки musl C и glibc. * `default` для дистрибутивов Linux, использующих стандартную библиотеку glibc.  Применимо только к типам инсталлятора `paas` и `paas-sh`. Поле может принимать значения: * `default` * `multidistro` * `musl` | query | Необязательный |
| arch | string | Архитектура вашей ОС:  * `all`: используйте это значение для AIX и z/OS. По умолчанию `x86` для остальных типов ОС. * `x86`: архитектура x86. * `ppc`: архитектура PowerPC, поддерживается только для AIX. * `ppcle`: архитектура PowerPC Little Endian, поддерживается только для Linux. * `sparc`: архитектура Sparc, поддерживается только для Solaris. * `arm`: архитектура ARM, поддерживается только для Linux. * `s390`: архитектура S/390, поддерживается только для Linux.  Применимо только к типам инсталлятора `paas` и `paas-sh`. Поле может принимать значения: * `all` * `arm` * `ppc` * `ppcle` * `s390` * `sparc` * `x86` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AgentInstallerVersions](#openapi-definition-AgentInstallerVersions) | Успех. Payload содержит доступные версии. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `AgentInstallerVersions`

Список доступных версий инсталлятора OneAgent.

| Поле | Тип | Описание |
| --- | --- | --- |
| availableVersions | string[] | Список доступных версий инсталлятора OneAgent. |

#### Объект `ErrorEnvelope`

| Поле | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Поле | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Поле | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Поле может принимать значения: * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"availableVersions": [



"string"



]



}
```

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