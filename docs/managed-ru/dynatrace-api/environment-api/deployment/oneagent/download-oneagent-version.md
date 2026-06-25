---
title: Deployment API - Download OneAgent of specific version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version
scraped: 2026-05-12T11:58:17.787179
---

# Deployment API - Download OneAgent of specific version

# Deployment API - Download OneAgent of specific version

* Справочник
* Опубликовано 28 августа 2019 г.

Скачивает инсталлятор OneAgent указанной версии. Список доступных версий можно получить вызовом [GET available versions of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "Список доступных версий OneAgent через Dynatrace API.").

Для типов инсталлятора `paas` или `paas-sh` можно получить конфигурирующий инсталлятор, передав дополнительные параметры.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/{osType}/{installerType}/version/{version}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/{osType}/{installerType}/version/{version}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| If-None-Match | string | ETag предыдущего запроса. Не скачивайте, если он совпадает с ETag инсталлятора. | header | Необязательный |
| osType | string | Операционная система инсталлятора. Поле может принимать значения: * `windows` * `unix` * `aix` * `solaris` * `zos` | path | Обязательный |
| installerType | string | Тип инсталлятора:  * `default`: самораспаковывающийся инсталлятор для ручной установки. Скачивает файл `.exe` для Windows или файл `.sh` для Unix. * `default-unattended`: самораспаковывающийся инсталлятор для автоматической установки. Только Windows. Скачивает архив `.zip`, содержащий инсталлятор `.msi` и пакетный файл. Эта опция устарела начиная с OneAgent версии 1.173 * `mainframe`: скачивает все code modules для z/OS, объединённые в один архив `*.pax`. * `paas`: инсталлятор code modules. Скачивает архив `*.zip`, содержащий файл `manifest.json` с метаинформацией или файл `.jar` для z/OS. * `paas-sh`: инсталлятор code modules. Скачивает самораспаковывающийся shell-скрипт со встроенным архивом `tar.gz`. Поле может принимать значения: * `default` * `default-unattended` * `mainframe` * `paas` * `paas-sh` | path | Обязательный |
| version | string | Требуемая версия OneAgent в формате `1.155.275.20181112-084458`.  Список доступных версий можно получить вызовом [**GET available versions of OneAgent**](https://dt-url.net/fo23rb5). | path | Обязательный |
| flavor | string | Вариант вашего дистрибутива Linux:  * `musl` для дистрибутивов Linux, использующих стандартную библиотеку C musl, например Alpine Linux. * `multidistro` для дистрибутивов Linux, использующих стандартные библиотеки musl C и glibc. * `default` для дистрибутивов Linux, использующих стандартную библиотеку glibc.  Применимо только к типам инсталлятора `paas` и `paas-sh`. Поле может принимать значения: * `default` * `multidistro` * `musl` | query | Необязательный |
| arch | string | Архитектура вашей ОС:  * `all`: используйте это значение для AIX и z/OS. По умолчанию `x86` для остальных типов ОС. * `x86`: архитектура x86. * `ppc`: архитектура PowerPC, поддерживается только для AIX. * `ppcle`: архитектура PowerPC Little Endian, поддерживается только для Linux. * `sparc`: архитектура Sparc, поддерживается только для Solaris. * `arm`: архитектура ARM, поддерживается только для Linux. * `s390`: архитектура S/390, поддерживается только для Linux.  Применимо только к типам инсталлятора `paas` и `paas-sh`. Поле может принимать значения: * `all` * `arm` * `ppc` * `ppcle` * `s390` * `sparc` * `x86` | query | Необязательный |
| bitness | string | Разрядность вашей ОС. Должна поддерживаться ОС.  Применимо только к типам инсталлятора `paas` и `paas-sh`. Поле может принимать значения: * `32` * `64` * `all` | query | Необязательный |
| include | string[] | Code modules, которые нужно включить в инсталлятор. Можно указать несколько модулей в формате: `include=java&include=dotnet`.  Применимо только к типам инсталлятора `paas` и `paas-sh`. Поле может принимать значения: * `all` * `java` * `java-graal-native` * `apache` * `nginx` * `nodejs` * `dotnet` * `php` * `go` * `sdk` * `envoy` * `python` | query | Необязательный |
| skipMetadata | boolean | Установите `true`, чтобы исключить сведения о подключении OneAgent из инсталлятора.  Применимо только к типам инсталлятора `paas` и `paas-sh`. | query | Необязательный |
| networkZone | string | Сетевая зона, с которой должен быть сконфигурирован результат. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | string | Успех. Payload содержит файл инсталлятора. |
| **304** | - | Не изменено. У вас уже есть последняя версия инсталлятора. Ответ не содержит payload. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

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