---
title: Deployment API - GET доступные версии ActiveGate
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-versions
scraped: 2026-05-12T11:56:48.102976
---

# Deployment API - GET доступные версии ActiveGate

# Deployment API - GET доступные версии ActiveGate

* Справочник
* Опубликовано 02 июля 2020 г.

Перечисляет все доступные версии инсталлятора ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/versions/{osType}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/deployment/installer/gateway/versions/{osType}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `InstallerDownload`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| osType | string | Операционная система инсталлятора. Поле может принимать значения: * `windows` * `unix` | path | Обязательный |
| arch | string | Архитектура вашей ОС:  * `all`: по умолчанию `amd64`. * `amd64`: архитектура amd64. * `s390`: архитектура S/390, поддерживается только для Linux. * `arm64`: архитектура arm64, поддерживается только для Linux. Поле может принимать значения: * `all` * `amd64` * `arm64` * `s390` | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ActiveGateInstallerVersions](#openapi-definition-ActiveGateInstallerVersions) | Успех. Payload содержит доступные версии. |
| **404** | - | Не найдено. Подробности смотрите в теле ответа. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ActiveGateInstallerVersions`

Список доступных версий инсталлятора ActiveGate.

| Поле | Тип | Описание |
| --- | --- | --- |
| availableVersions | string[] | Доступные версии. |

### JSON-модели тела ответа

```
{



"availableVersions": [



"string"



]



}
```