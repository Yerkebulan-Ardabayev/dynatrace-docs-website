---
title: Deployment API - Download latest OneAgent
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest
---

# Deployment API - Download latest OneAgent

# Deployment API - Download latest OneAgent

* Справочник
* Опубликовано 28 авг. 2019 г.

Загружает установщик OneAgent, указанный в целевой версии в [обновлениях OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-update#configure-oneagent-updates "Узнать, как обновлять OneAgent."). Проверить номер последней версии можно с помощью вызова [GET the latest version of OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "Посмотреть последнюю версию OneAgent через Dynatrace API.").

Для типов установщика `paas` или `paas-sh` можно получить конфигурируемый установщик, передав дополнительные параметры.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/{osType}/{installerType}/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/agent/{osType}/{installerType}/latest` |

## Аутентификация

Для выполнения этого запроса нужен токен доступа со скоупом `InstallerDownload`.

Про то, как получить и использовать его, см. [Токены и аутентификация](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| If-None-Match | string | ETag предыдущего запроса. Не загружать, если он совпадает с ETag установщика. | header | Опционально |
| osType | string | Операционная система установщика. Элемент может принимать следующие значения * `windows` * `unix` * `aix` * `solaris` * `zos` | path | Обязательно |
| installerType | string | Тип установщика:  * `default`: самораспаковывающийся установщик для ручной установки. Загружает файл `.exe` для Windows или файл `.sh` для Unix. * `default-unattended`: самораспаковывающийся установщик для автоматической установки без участия пользователя. Только для Windows. Загружает архив `.zip`, содержащий установщик `.msi` и пакетный файл. Этот вариант устарел начиная с версии OneAgent 1.173 * `mainframe`: загружает все программные модули для z/OS, объединённые в один архив `*.pax`. * `paas`: установщик программных модулей. Загружает архив `*.zip`, содержащий файл `manifest.json` с метаинформацией, или файл `.jar` для z/OS. * `paas-sh`: установщик программных модулей. Загружает самораспаковывающийся shell-скрипт со встроенным архивом `tar.gz`. Элемент может принимать следующие значения * `default` * `default-unattended` * `mainframe` * `paas` * `paas-sh` | path | Обязательно |
| flavor | string | Разновидность дистрибутива Linux:  * `musl` для дистрибутивов Linux, использующих стандартную библиотеку C musl, например Alpine Linux. * `multidistro` для дистрибутивов Linux, использующих стандартные библиотеки musl C и glibc. * `default` для дистрибутивов Linux, использующих стандартную библиотеку glibc.  Применимо только к типам установщика `paas` и `paas-sh`. Элемент может принимать следующие значения * `default` * `multidistro` * `musl` | query | Опционально |
| arch | string | Архитектура вашей ОС:  * `all`: используется для AIX и z/OS. Для остальных типов ОС по умолчанию `x86`. * `x86`: архитектура x86. * `ppc`: архитектура PowerPC, поддерживается только для AIX. * `ppcle`: архитектура PowerPC Little Endian, поддерживается только для Linux. * `sparc`: архитектура Sparc, поддерживается только для Solaris. * `arm`: архитектура ARM, поддерживается только для Linux. * `s390`: архитектура S/390, поддерживается только для Linux.  Применимо только к типам установщика `paas` и `paas-sh`. Элемент может принимать следующие значения * `all` * `arm` * `ppc` * `ppcle` * `s390` * `sparc` * `x86` | query | Опционально |
| bitness | string | Разрядность вашей ОС. Должна поддерживаться ОС.  Применимо только к типам установщика `paas` и `paas-sh`. Элемент может принимать следующие значения * `32` * `64` * `all` | query | Опционально |
| include | string[] | Программные модули, которые нужно включить в установщик. Можно указать несколько модулей в следующем формате: `include=java&include=dotnet`.  Применимо только к типам установщика `paas` и `paas-sh`. Элемент может принимать следующие значения * `all` * `java` * `java-graal-native` * `apache` * `nginx` * `nodejs` * `dotnet` * `php` * `go` * `sdk` * `envoy` * `python` * `ruby` | query | Опционально |
| skipMetadata | boolean | Установите `true`, чтобы исключить из установщика информацию о подключении к OneAgent.  Применимо только к типам установщика `paas` и `paas-sh`. | query | Опционально |
| networkZone | string | Сетевая зона, с которой должен быть сконфигурирован результат. | query | Опционально |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | string | Успех. Полезная нагрузка содержит файл установщика. |
| **304** | - | Не изменено. У вас уже есть последняя версия установщика. Ответ не содержит полезной нагрузки. |
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

### JSON модели тела ответа

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