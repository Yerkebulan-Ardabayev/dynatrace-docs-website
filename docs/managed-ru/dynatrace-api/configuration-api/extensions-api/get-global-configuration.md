---
title: Extensions API - GET global configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-global-configuration
scraped: 2026-05-12T11:19:54.729089
---

# Extensions API - GET global configuration

# Extensions API - GET global configuration

* Reference
* Published Mar 06, 2020

Возвращает глобальную конфигурацию указанного расширения OneAgent или JMX.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/global` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/global` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID расширения, которое нужно обновить. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [GlobalExtensionConfiguration](#openapi-definition-GlobalExtensionConfiguration) | Глобальная конфигурация указанного расширения. |

### Объекты тела ответа

#### Объект `GlobalExtensionConfiguration`

Глобальная конфигурация расширения OneAgent и JMX

| Элемент | Тип | Описание |
| --- | --- | --- |
| enabled | boolean | Расширение включено (`true`) или отключено (`false`). |
| extensionId | string | ID расширения. |
| infraOnlyEnabled | boolean | Плагин включён (`true`) или отключён (`false`) глобально для хостов в режиме мониторинга только инфраструктуры |
| properties | object | Список параметров конфигурации.  Каждый параметр представляет собой пару «ключ-значение». |

### JSON-модели тела ответа

```
{



"id": "custom.remote.python.demo",



"properties": [



{



"defaultValue": "127.0.0.1",



"key": "serverIp",



"type": "STRING"



},



{



"defaultValue": "",



"key": "password",



"type": "PASSWORD"



},



{



"defaultValue": "dynatrace",



"key": "username",



"type": "STRING"



},



{



"defaultValue": "one",



"dropdownValues": [



"one",



"two",



"three"



],



"key": "dropdownProperty",



"type": "DROPDOWN"



}



]



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")