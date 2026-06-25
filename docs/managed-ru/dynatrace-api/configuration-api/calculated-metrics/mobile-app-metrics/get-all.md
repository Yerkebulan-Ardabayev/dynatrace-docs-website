---
title: Mobile app metrics API - GET all metrics
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics/get-all
scraped: 2026-05-12T11:17:32.139031
---

# Mobile app metrics API - GET all metrics

# Mobile app metrics API - GET all metrics

* Reference
* Published Apr 16, 2020

Выводит список всех вычисляемых метрик мобильных приложений.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/calculatedMetrics/mobile` |

## Аутентификация

Для выполнения этого запроса нужен access token со scope `ReadConfig`.

Как его получить и использовать, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

В запросе нет настраиваемых параметров.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Успех |

### Объекты тела ответа

#### Объект `StubList`

Упорядоченный список кратких представлений сущностей Dynatrace.

| Элемент | Тип | Описание |
| --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | Упорядоченный список кратких представлений сущностей Dynatrace. |

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



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Связанные темы

* [Создание вычисленных метрик для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших мобильных приложений.")
* [Создание вычисляемых метрик для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Создание вычисляемых метрик, а также пользовательских графиков на основе вычисляемых метрик для ваших пользовательских приложений.")