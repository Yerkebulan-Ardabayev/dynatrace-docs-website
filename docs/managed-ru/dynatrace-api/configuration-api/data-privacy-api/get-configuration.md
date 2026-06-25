---
title: Data privacy API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/data-privacy-api/get-configuration
scraped: 2026-05-12T11:17:39.954620
---

# Data privacy API - GET configuration

# Data privacy API - GET configuration

* Reference
* Published Sep 02, 2019

Возвращает глобальную конфигурацию data privacy, влияющую на все ваши приложения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dataPrivacy` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [DataPrivacyAndSecurity](#openapi-definition-DataPrivacyAndSecurity) | Успех |

### Объекты тела ответа

#### Объект `DataPrivacyAndSecurity`

Глобальная конфигурация data privacy и security.

| Элемент | Тип | Описание |
| --- | --- | --- |
| logAuditEvents | boolean | Audit logging включён (`true`) или выключен (`false`). |
| maskIpAddressesAndGpsCoordinates | boolean | Маскирование IP-адресов и GPS-координат включено (`true`) или выключено (`false`). |
| maskPersonalDataInUris | boolean | Маскирование персональных данных в URI включено (`true`) или выключено (`false`). |
| maskUserActionNames | boolean | Маскирование имён user actions включено (`true`) или выключено (`false`).  Это маскирование доступно только для web applications. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

### JSON-модели тела ответа

```
{



"logAuditEvents": true,



"maskIpAddressesAndGpsCoordinates": true,



"maskPersonalDataInUris": true,



"maskUserActionNames": true,



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



}



}
```

## Пример

В этом примере запрос возвращает текущую конфигурацию data privacy.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dataPrivacy
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



17,



17



],



"clusterVersion": "1.211.2.20210129-043235"



},



"maskIpAddressesAndGpsCoordinates": true,



"maskUserActionNames": false,



"maskPersonalDataInUris": false,



"logAuditEvents": true



}
```

## Связанные темы

* [Data privacy and security](/managed/manage/data-privacy-and-security "Узнайте, как Dynatrace применяет меры безопасности для защиты приватных данных.")