---
title: Plugins API - GET a plugin
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/plugins-api/get-a-plugin
scraped: 2026-05-12T11:20:53.014711
---

# Plugins API - GET a plugin

# Plugins API - GET a plugin

* Reference
* Published Jun 07, 2019

Выводит свойства указанного плагина.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/plugins/{id}` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| id | string | ID требуемого плагина. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [Plugin](#openapi-definition-Plugin) | Успех |

### Объекты тела ответа

#### Объект `Plugin`

Общая конфигурация плагина.

| Элемент | Тип | Описание |
| --- | --- | --- |
| id | string | ID плагина, например `custom.remote.python.demo`. |
| metadata | [ConfigurationMetadata](#openapi-definition-ConfigurationMetadata) | Метаданные для отладки |
| metricGroup | string | Группа метрик плагина. Все метрики, собираемые плагином, являются потомками этой группы. |
| name | string | Имя плагина, отображаемое в Dynatrace. |
| properties | [PluginProperty[]](#openapi-definition-PluginProperty) | Список свойств плагина. |
| type | string | Тип плагина. Указывает среду выполнения плагина (например, ActiveGate). Возможные значения: * `ActiveGate` * `JMX` * `OneAgent` * `PMI` |
| version | string | Версия плагина, отображаемая в Dynatrace. |

#### Объект `ConfigurationMetadata`

Метаданные для отладки

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterVersion | string | Версия Dynatrace. |
| configurationVersions | integer[] | Отсортированный список номеров версий конфигурации. |
| currentConfigurationVersions | string[] | Отсортированный список номеров версий конфигурации. |

#### Объект `PluginProperty`

Свойство плагина.

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



"metricGroup": "custom.demo_metrics",



"name": "ActiveGate demo plugin",



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

## Пример

В этом примере запрос запрашивает параметры **SAP plugin** с ID **custom.remote.python.sap**.

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/plugins/custom.remote.python.sap
```

#### Тело ответа

```
{



"metadata": {



"configurationVersions": [



0



],



"clusterVersion": "1.173.0.20190611-111714"



},



"id": "custom.remote.python.sap",



"name": "SAP plugin",



"type": "ActiveGate",



"properties": [



{



"key": "password",



"type": "PASSWORD",



"defaultValue": ""



},



{



"key": "instance",



"type": "STRING",



"defaultValue": ""



},



{



"key": "serverIp",



"type": "TEXTAREA",



"defaultValue": ""



},



{



"key": "clientno",



"type": "STRING",



"defaultValue": ""



},



{



"key": "username",



"type": "STRING",



"defaultValue": ""



}



]



}
```

#### Код ответа

200