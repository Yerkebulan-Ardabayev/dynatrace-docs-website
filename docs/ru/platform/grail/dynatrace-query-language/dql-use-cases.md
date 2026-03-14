---
title: Варианты использования DQL
source: https://www.dynatrace.com/docs/platform/grail/dynatrace-query-language/dql-use-cases
scraped: 2026-03-02T21:25:43.385489
---

# Сценарии использования DQL


* Последняя версия Dynatrace
* Справочник
* Опубликовано 16 января 2023 г.

Следующие сценарии использования демонстрируют некоторые способы применения Dynatrace Query Language для работы с данными, принятыми в Grail.

### Разбор JSON-данных и агрегирование записей

В данном сценарии предположим, что необходимо проверить, сколько транзакций было проведено каждым провайдером платёжных услуг, а также долю каждого провайдера в общем количестве транзакций.

Поле `content` для каждой записи выглядит следующим образом:

```
{


"country_code":"US",


"session_id":"6a6c6b6d6a7c7b7f7a7c7b7a7f7",


"invoicing_data":null,


"bill_to":{


"first_name":"John",


"last_name":"Doe",


"email":"john.doe@gmail.com",


"phone":null


},


"payment_provider":"paypal"


}
```

Можно использовать команду `parse` в сочетании с [Dynatrace Pattern Language](../dynatrace-pattern-language.md "Используйте Dynatrace Pattern Language для описания шаблонов с помощью матчеров.") для разбора JSON-объектов. Запрос извлекает поле `payment_provider` из JSON-данных и группирует количество транзакций по каждому провайдеру с помощью команды `summarize`, а также вычисляет общее количество транзакций. Доля отображается в отдельном столбце рядом с количеством транзакций каждого провайдера.

```
fetch logs


| parse content, "JSON:json"


| fields payment = json[payment_provider]


| summarize


bank_card=countIf(payment=="bank_card"), bank_cardPer=toDouble(countIf(payment=="bank_card"))/toDouble(count()),


apple_pay=countIf(payment=="apple_pay"),apple_payPerc=toDouble(countIf(payment=="apple_pay"))/toDouble(count()),


paypal=countIf(payment=="paypal"),paypalPerc=toDouble(countIf(payment=="paypal"))/toDouble(count()),


google_pay=countIf(payment=="google_pay"),google_payPerc=toDouble(countIf(payment=="google_pay"))/toDouble(count()),


unpaid_booking=countIf(payment=="unpaid_booking"),unpaid_bookingPerc=toDouble(countIf(payment=="unpaid_booking"))/toDouble(count()),


total=count()
```

Результаты:

### Извлечение первых n символов из поля

В этом примере есть поле `kiosk`, из которого нужно извлечь первые три символа для определения сокращения местонахождения киоска.

```
{


"kiosk": "LAOBAUA729"


}
```

```
...


| parse kiosk, "DATA{3}:kioskLoc"


| fields kiosk, kioskLoc
```

Результаты:

### Извлечение информации из XML-элемента

В данном сценарии API-шлюз создаёт журналы в формате XML, и из них нужно извлечь некоторую информацию.

Поле XML для каждой записи выглядит следующим образом:

```
<log-entry serial='1467' domain='bca_icas_soa'>


<date>Fri Sep 21 2023</date>


<time utc='1380295304719'>11:21:44</time>


<date-time>2012-09-21T11:21:44</date-time>


<type>xmlfirewall</type>


<class>xmlfirewall</class>


<object>example-Firewall</object>


<level num='3'>error</level>


<transaction-type>error</transaction-type>


<transaction>6187</transaction>


<client>127.0.0.1</client>


<code>0x01130007</code>


<file></file>


<message>Failed to establish backend connection</message>


</log-entry>
```

В DQL-запросе необходимо использовать [матчер DPL](../dynatrace-pattern-language/dpl-xml.md "Узнайте, как использовать XML-матчеры с DPL.") для извлечения всего XML-элемента:

```
...


| parse content, "XML(excludeRoot=true):xml"


| fields domain = xml[`@domain`],


serial = toLong(xml[`@serial`]),


object = xml[object],


transaction = xml[transaction],


code = xml[code]
```

Результаты:

### Расследование инцидентов безопасности в кластерах Kubernetes. Поиск угроз

Application Security

В данном сценарии выполняются запросы с помощью [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../../../secure/investigations.md "Объединение возможностей Grail для расследований на основе доказательств: разрешение инцидентов, анализ первопричин и поиск угроз.") для анализа несанкционированных запросов в журналах аудита Kubernetes. Следуйте различным путям расследования, перемещайтесь между выполненными запросами и получайте подробный обзор результатов в исходном формате.

* [Поиск угроз и форензика](../../../secure/use-cases/threat-hunting.md "Сценарий использования для поиска угроз и форензики с помощью Investigations.")

## Связанные темы

* [Dynatrace Query Language](../dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [Использование DQL-запросов](dql-guide.md "Узнайте, как работает DQL и каковы ключевые концепции DQL.")
* [DQL в сравнении с SQL и другими языками](dql-comparison.md "Сравнение DQL с другими языками запросов.")
* [Справочник по языку DQL](dql-reference.md "Справочник синтаксиса Dynatrace Query Language.")
* [Команды DQL](commands.md "Список команд DQL.")
* [Функции DQL](functions.md "Список функций DQL.")
* [Операторы DQL](operators.md "Список операторов DQL.")
* [Типы данных DQL](data-types.md "Список типов данных DQL.")
