---
title: DQL в сравнении с SQL и другими
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-comparison
scraped: 2026-03-06T21:20:41.784151
---

# Сравнение DQL с SQL и другими языками


* Последняя версия Dynatrace
* Справочник
* Опубликовано 17 октября 2022 г.

На этой странице сравниваются наиболее распространённые сценарии использования DQL и других устоявшихся языков запросов и обработки данных, таких как SQL, Splunk SPL и Microsoft Kusto Query Language.

### Загрузка данных для запросов

#### Dynatrace Query Language (DQL)

```
fetch events
```

#### Structured Query Language (SQL)

```
SELECT * FROM events
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*
```

#### Kusto Query Language (KQL)

```
events
```

### Фильтрация

Сужает количество записей на основе выражения фильтра. В этом примере мы ищем события оплаты.

#### Dynatrace Query Language (DQL)

```
fetch events


| filter event.type == "travel.funnel.booking-payment"
```

#### Structured Query Language (SQL)

```
SELECT * FROM events WHERE 'event.type'="travel.funnel.booking-payment"
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event* | where event.type = "travel.funnel.booking-payment"
```

#### Kusto Query Language (KQL)

```
events


| where ['event.type'] == "travel.funnel.booking-payment"
```

Мы можем добавить в конвейер столько фильтров, сколько необходимо. Например, мы можем искать бронирования, сделанные клиентами с высоким уровнем лояльности, путешествующими с детьми.

#### Dynatrace Query Language (DQL)

```
fetch events


| filter event.type == "travel.funnel.booking-payment" and loyaltyStatus == "Platinum" and childrenTravelers > 0
```

#### Structured Query Language (SQL)

```
SELECT * FROM events WHERE 'event.type'="travel.funnel.booking-payment" AND loyaltyStatus = "Platinum" AND childrenTravelers > 0
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*


| where event.type = "travel.funnel.booking-payment" AND loyaltyStatus = "Platinum" AND childrenTravelers > 0
```

#### Kusto Query Language (KQL)

```
events


| where ['event.type'] == "travel.funnel.booking-payment" and loyaltyStatus == "Platinum" and childrenTravelers > 0
```

### Выбор полей

Выбор только нужных полей может быть выполнен на любом этапе конвейера. В этом примере мы выберем только продукт успешных бронирований.

#### Dynatrace Query Language (DQL)

```
fetch events


| filter event.type == "travel.funnel.booking-payment"


| fields product
```

#### Structured Query Language (SQL)

```
SELECT product FROM events WHERE 'event.type'="travel.funnel.booking-payment"
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*


| where event.type = "travel.funnel.booking-payment"


| fields product
```

#### Kusto Query Language (KQL)

```
event


| where ['event.type'] == "travel.funnel.booking-payment"


| project product
```

### Вычисления и сортировка

Мы можем преобразовывать выбранные записи в конвейерах. Например, мы выберем продолжительность забронированных поездок в днях и пересчитаем её в недели.

#### Dynatrace Query Language (DQL)

```
fetch event


| filter event.type == "travel.funnel.booking-payment"


| fieldsAdd journeyWeeks = journeyDuration/7


| sort journeyWeeks desc
```

#### Structured Query Language (SQL)

```
SELECT journeyDuration/7 AS journeyWeeks FROM events WHERE 'event.type'="travel.funnel.booking-payment" ORDER BY journeyWeeks DESC
```

#### Splunk Search Processing language (SPL)

```
sourcetype = event*


| where event.type = "travel.funnel.booking-payment"


| eval journeyweeks = journeyDuration/7


| sort -journeyweeks
```

#### Kusto Query Language (KQL)

```
event


| where ['event.type'] == "travel.funnel.booking-payment"


| project journeyWeeks = journeyDuration/7


| sort journeyweeks desc
```

### Группировка

Если нас интересуют только уникальные значения ключа, мы можем дедуплицировать результаты путём группировки.

#### Dynatrace Query Language (DQL)

```
fetch events


| summarize count(), by:event.type


| fields event.type
```

#### Structured Query Language (SQL)

```
SELECT DISTINCT 'event.type' FROM events
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*


| stats count by event.type
```

#### Kusto Query Language (KQL)

```
events


| summarize by event.type
```

### Агрегация

После группировки выбранных записей по полю мы можем агрегировать результаты в новый вывод.

#### Dynatrace Query Language (DQL)

```
fetch events


| filter event.type == "travel.funnel.booking-payment"


| summarize sum = sum(amount), by:travelAgency
```

#### Structured Query Language (SQL)

```
SELECT sum(amount) AS sum FROM events GROUP BY sum, travelAgency WHERE 'event.type' == "travel.funnel.booking-payment"
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*


| where event.type = "travel.funnel.booking-payment"


| stats sum(amount) as total_amount by travelAgency
```

#### Kusto Query Language (KQL)

```
event


| filter event.type == "travel.funnel.booking-payment"


| summarize sum = sum(amount) by travelAgency
```

Рассмотрим более сложный сценарий, в котором мы хотим добавить новое поле, основанное на математическом выражении, в нашу таблицу результатов.

#### Dynatrace Query Language (DQL)

```
fetch events


| filter event.type == "travel.funnel.booking-payment"


| summarize sum = sum(amount), by:{travelAgency, travelers}


| fieldsAdd has_more_than_2 = travelers > 2
```

#### Structured Query Language (SQL)

```
SELECT sum(amount) AS sum, travelers > 2  AS has_more_than_2 FROM events  GROUP BY sum, has_more_than_2, travelAgency, travelers WHERE 'event.type' == "travel.funnel.booking-payment"
```

#### Splunk Search Processing Language (SPL)

```
sourcetype = event*


| where event.type = "travel.funnel.booking-payment"


| stats sum(amount) as total_amount by travelAgency, travelers


| eval has_more_than_2 = travelers > 2
```

#### Kusto Query Language (KQL)

```
events


| where ['event.type'] == "travel.funnel.booking-payment"


| summarize sumBytes = sum(amount) by travelAgency, travelers


| project has_more_than_2 = travelers > 2
```

## Связанные темы

* [Dynatrace Query Language](../dynatrace-query-language.md "Использование Dynatrace Query Language.")
* [Использование запросов DQL](dql-guide.md "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
* [Справочник по языку DQL](dql-reference.md "Справочник по синтаксису Dynatrace Query Language.")
* [Команды DQL](commands.md "Список команд DQL.")
* [Функции DQL](functions.md "Список функций DQL.")
* [Операторы DQL](operators.md "Список операторов DQL.")
* [Типы данных DQL](data-types.md "Список типов данных DQL.")
* [Лучшие практики DQL](dql-best-practices.md "Лучшие практики использования Dynatrace Query Language.")
