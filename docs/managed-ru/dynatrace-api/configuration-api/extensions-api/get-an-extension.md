---
title: Extensions API - GET an extension
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/get-an-extension
scraped: 2026-05-12T11:19:51.968621
---

# Extensions API - GET an extension

# Extensions API - GET an extension

* Reference
* Published Mar 06, 2020

Выводит свойства указанного расширения.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого расширения. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Extension](#openapi-definition-Extension) | Успех |

### Объекты тела ответа

#### Объект `Extension`

Общая конфигурация расширения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID расширения, например `custom.remote.python.demo`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| metricGroup | string | metricGroup расширения, используемый для группировки кастомных метрик в иерархическое пространство имён. |
| name | string | Имя расширения, отображаемое в Dynatrace. |
| properties | [ExtensionProperty[]](#openapi-definition-ExtensionProperty) | Список свойств расширения. |
| type | string | Тип расширения. Указывает среду выполнения расширения (например, ACTIVEGATE). Возможные значения: * `ACTIVEGATE` * `CODEMODULE` * `JMX` * `ONEAGENT` * `PMI` * `UNKNOWN` |
| version | string | Версия расширения, отображаемая в Dynatrace. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `ExtensionProperty`

Свойство расширения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| defaultValue | string | Значение свойства по умолчанию. |
| dropdownValues | string[] | Список возможных значений свойства.  Если такой список задан, свойству можно присвоить только значения из этого списка. |
| key | string | Ключ свойства. |
| type | string | Тип свойства. |

### JSON-модели тела ответа

```
{



"id": "custom.remote.python.demo",



"metadata": {



"clusterVersion": "1.186.0.20200109-094111",



"configurationVersions": [



7



]



},



"metricGroup": "custom.demo_metrics",



"name": "ActiveGate demo extension",



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



],



"type": "ActiveGate",



"version": "1.01"



}
```

## Связанные темы

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Разработка собственных Extensions в Dynatrace.")