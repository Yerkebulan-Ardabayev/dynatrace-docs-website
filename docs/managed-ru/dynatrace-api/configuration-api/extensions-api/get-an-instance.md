---
title: Extensions API - GET an extension's instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-an-instance
scraped: 2026-05-12T11:19:48.007949
---

# Extensions API - GET an extension's instance

# Extensions API - GET an extension's instance

* Reference
* Published Mar 06, 2020

Выводит свойства указанного экземпляра расширения ActiveGate.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения. | path | Required |
| configurationId | string | ID конфигурации. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [ExtensionConfigurationDto](#openapi-definition-ExtensionConfigurationDto) | Успех |

### Объекты тела ответа

#### Объект `ExtensionConfigurationDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| activeGate | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Краткое представление сущности Dynatrace. |
| enabled | boolean | Расширение включено (`true`) или отключено (`false`). |
| endpointId | string | ID эндпоинта. |
| endpointName | string | Имя эндпоинта, отображаемое в Dynatrace. |
| extensionId | string | ID расширения. |
| hostId | string | ID хоста, на котором работает расширение. |
| properties | object | Список параметров расширения.  Каждый параметр представляет собой пару «ключ-значение». |
| useGlobal | boolean | Позволяет пропустить текущую конфигурацию и использовать глобальную. |

#### Объект `EntityShortRepresentation`

Краткое представление сущности Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| description | string | Краткое описание сущности Dynatrace. |
| id | string | ID сущности Dynatrace. |
| name | string | Имя сущности Dynatrace. |

### JSON-модели тела ответа

```
{



"activeGate": {



"id": "7835970235169136995",



"name": "ActiveGate Host Name"



},



"enabled": true,



"hostId": "HOST-01A7DEFA5340A86D",



"id": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "three",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



},



"useGlobal": false



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")