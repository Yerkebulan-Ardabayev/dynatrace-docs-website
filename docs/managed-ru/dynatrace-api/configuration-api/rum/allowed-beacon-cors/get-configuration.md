---
title: Allowed beacon domains API - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/allowed-beacon-cors/get-configuration
scraped: 2026-05-12T11:19:45.152693
---

# Allowed beacon domains API - GET configuration

# Allowed beacon domains API - GET configuration

* Reference
* Published Sep 23, 2020

Возвращает конфигурацию разрешённых beacon origins для запросов Cross Origin Resource Sharing (CORS).

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/allowedBeaconOriginsForCors` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [AllowedBeaconOrigins](#openapi-definition-AllowedBeaconOrigins) | Успех |

### Объекты тела ответа

#### Объект `AllowedBeaconOrigins`

Конфигурация разрешённых beacon origins для запросов CORS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| allowedBeaconOrigins | [BeaconDomainPattern[]](#openapi-definition-BeaconDomainPattern) | Список разрешённых beacon origins для запросов CORS. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| rejectBeaconsWithoutOriginHeader | boolean | Отбрасывать (`true`) или сохранять (`false`) beacon'ы без HTTP-заголовка **Origin** на BeaconForwarder.  Если не задано, используется `false`. |

#### Объект `BeaconDomainPattern`

Разрешённый beacon origin для запросов CORS.

| Элемент | Тип | Описание |
| --- | --- | --- |
| domainNameMatcher | string | Операция сопоставления для **domainNamePattern**. Возможные значения: * `CONTAINS` * `ENDS_WITH` * `EQUALS` * `STARTS_WITH` |
| domainNamePattern | string | Шаблон разрешённого доменного имени. |

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



"allowedBeaconOrigins": [



{



"domainNameMatcher": "EQUALS",



"domainNamePattern": "dynatrace.com"



}



],



"metadata": {



"clusterVersion": "Mock version",



"configurationVersions": [



4,



2



]



}



}
```