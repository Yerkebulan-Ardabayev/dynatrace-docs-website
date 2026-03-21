---
title: Анализ и примеры бизнес-событий
source: https://www.dynatrace.com/docs/observe/business-observability/bo-analysis
scraped: 2026-03-06T21:14:29.180885
---

# Анализ бизнес-событий и примеры


* Latest Dynatrace
* 9 мин. чтения

После сохранения в Grail вы можете интерактивно запрашивать данные бизнес-событий и анализировать их с помощью [DQL](../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language."). DQL является отправной точкой для анализа, независимо от того, используете ли вы [Notebooks](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь аналитическими данными наблюдаемости --- в едином совместном настраиваемом рабочем пространстве."), [Dashboards](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени.") или DQL Query API (latest Dynatrace). Вы можете использовать результаты запросов интерактивно или закрепить их на дашборде в виде графиков, плиток или таблиц.

## Запрос и анализ ваших данных

1. Выберите **Notebooks** ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") или **Dashboards** ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards").
2. Создайте и выполните ваш запрос.

   Вы можете использовать запросы для создания метрик и графиков для дашбордов. Вы также можете выполнять запросы через API для использования данных во внешних системах.

## Примеры метрик в Notebooks

С помощью DQL вы можете создавать метрики на постоянной основе из любых числовых данных, собранных как бизнес-события. Существует множество вариантов отображения результатов в Notebooks ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") с предложениями, оптимизированными для ваших данных метрик.

### Средний объем торговых операций в долларах: Одно значение

Этот пример рассчитывает средний общий объем торговых операций в долларах, сгенерированный EasyTrade за последние 24 часа.

* Покупки активов через EasyTrade фиксируются типами событий `com.easytrade.quick-buy` и `com.easytrade.long-buy`.
* Общий объем торговых операций в долларах рассчитывается как количество купленных активов, умноженное на цену актива.

Метрика ниже дает одно числовое значение, отображаемое как **Record list** в Notebooks.

```
fetch bizevents, from:now()-24h, to:now()


| filter event.type == "com.easytrade.quick-buy" or event.type == "com.easytrade.long-buy"


| summarize dollar_volume = avg(amount*price)
```

![Средний объем в долларах --- одно значение](https://dt-cdn.net/images/ba-dollar-volume-single-value-1229-3145c15ba2.webp)

### Общий объем торговых операций в долларах по временным интервалам: Линейный график

Вы можете создавать метрики на основе интервалов. Этот пример запрашивает общий объем торговых операций в долларах за последние 24 часа с интервалом в пять минут. В этом примере используется команда DQL [makeTimeseries](../../platform/grail/dynatrace-query-language/commands/aggregation-commands.md#makeTimeseries "Команды агрегации DQL") для построения временного ряда из меры (суммы объема в долларах), который затем можно использовать для визуализации в Notebooks или Dashboards.

* Продажи активов через EasyTrade фиксируются типом события `com.easytrade.nginx.quick-sell`.
* Объем торговых операций в долларах рассчитывается как количество проданных активов, умноженное на их цену.
* Этот запрос возвращает значение, представляющее объем в долларах с интервалом в пять минут.

```
fetch bizevents, from:now()-24h, to:now()


| filter event.type == "com.easytrade.nginx.quick-sell"


| makeTimeseries dollar_volume= sum (amount*price), interval: 5m
```

На изображении ниже показан **линейный график** для результатов запроса в Notebooks.

![Объем в долларах по временным интервалам --- линейный график](https://dt-cdn.net/images/ba-dollar-volume-time-intervals-line-chart-1316-2a2ac3dd06.webp)

### Средняя цена актива

Этот пример извлекает среднюю цену актива для ордеров на покупку и продажу через EasyTrade.

* Активы можно покупать и продавать через EasyTrade, что фиксируется, например, типами событий `com.easytrade.quick-buy` и `com.easytrade.nginx.quick-sell`.
* Без фильтрации по `event.type` этот запрос возвращает среднюю цену актива для ордеров как на покупку, так и на продажу.

```
fetch bizevents


| filter event.provider == "www.easytrade.com"


| filter isNotNull(price)


| summarize average_price_assets = avg(price)
```

Этот запрос лучше всего отображается как **Single value** (показано ниже) или **Record list**.

![Средняя цена актива покупка+продажа](https://dt-cdn.net/images/ba-avg-asset-price-single-value-1320-26c917a897.webp)

### Ежедневная сумма депозитов за последние 30 дней

Узнайте, сколько средств было переведено на счета EasyTrade в день за последние 30 дней.

* Переводы средств в EasyTrade фиксируются типом события `com.easytrade.deposit`.
* Логика запроса включает:

  + Суммирование суммы каждого события для получения общей суммы переведенных средств в EasyTrade.
  + Разбивку этой суммы по дням.

```
fetch bizevents, from: now()-30d, to: now()-1d


| filter event.type == "com.easytrade.deposit"


| makeTimeseries moneyTransfered= sum(amount), interval: 1d
```

На изображениях ниже показаны результаты в виде развернутого **Record list** и **линейного графика**.

![Ежедневные депозиты --- список записей](https://dt-cdn.net/images/ba-daily-deposits-record-list-1319-eba4e7d2e9.webp)

![Ежедневные депозиты --- линейный график](https://dt-cdn.net/images/ba-daily-deposits-line-chart-1315-561171007e.webp)

### Распределение сделок по группам по 2000 акций

Этот запрос показывает, сколько акций было продано в EasyTrade за последние 24 часа.

* Этот запрос показывает распределение сделок (или количество сделок) по группам по 2000 затронутых акций, чтобы увидеть, сколько сделок затрагивают 0--2000 акций, 2001--4000 акций и т.д.
* **Categorical chart** --- лучший выбор для отображения этих данных в столбцах, показывающих количество сделок для каждой группы.

```
fetch bizevents, from:now()-1d, to:now()


| filter event.provider == "www.easytrade.com"


| filter event.type == "com.easytrade.nginx.long-sell" OR event.type == "com.easytrade.nginx.long-buy"


| summarize numberOfTrades = count(), by:{sharesAffected=bin(amount, 2000)}


| fields sharesAffected = concat(toString(toLong(sharesAffected)+1), " - ", toString(toLong(sharesAffected +2000))), numberOfTrades


| limit 10
```

![Распределение сделок по группам](https://dt-cdn.net/images/ba-trades-by-buckets-categorical-chart-1316-464499d8c1.webp)

### Время между событиями

Вам нужно узнать, сколько времени занимает торговля у клиента, то есть как долго деньги клиента находятся на платформе перед выводом. Для этого необходимо определить время между связанными событиями, а именно: первым депозитом средств в EasyTrade и первым выводом активов.

```
fetch bizevents, from:now()-30d, to:now()


| filter event.provider == "www.easytrade.com"


| sort timestamp, direction:"descending"


| filter event.type == "com.easytrade.deposit" OR event.type == "com.easytrade.withdraw"


| fieldsAdd deposit_ts = if(event.type == "com.easytrade.deposit", timestamp)


| fieldsAdd withdraw_ts = if(event.type == "com.easytrade.withdraw", timestamp)


| summarize {first_deposit_ts = takeFirst(deposit_ts), first_withdraw_ts = takeFirst(withdraw_ts)}, by:{`accountId`}


| fieldsAdd timeDepositToDeposit= (first_withdraw_ts - first_deposit_ts) /(1000000000.0)


| filter timeDepositToDeposit > duration(0,unit:"ns")


| fields `accountId`, `Seconds From Deposit To Deposit`= timeDepositToDeposit
```

На изображении ниже показаны результаты запроса в виде **таблицы** в Notebooks.

![Время между событиями --- табличные данные](https://dt-cdn.net/images/ba-time-between-events-table-758-6610577a8d.webp)

#### Пошаговое объяснение запроса

* **Строка 1**

  ```
  fetch bizevents, from:now()-30d, to:now()
  ```

  Извлекает таблицу бизнес-событий. Кроме того, необязательный параметр `from:` задает начальную временную метку запроса.
* **Строка 2**

  ```
  | filter event.provider == "www.easytrade.com"
  ```

  Команда [`filter`](../../platform/grail/dynatrace-query-language/commands/filtering-commands.md#filter "Команды фильтрации и поиска DQL") предоставляет записи бизнес-событий на основе определенного [провайдера событий](bo-events-capturing.md#configure-sources "Сбор бизнес-событий для Dynatrace Business Observability.").
* **Строка 3**

  ```
  | sort timestamp, direction:"descending"
  ```

  Чтобы получить самые последние события первыми, вы можете отсортировать результаты по самой последней временной метке.
* **Строка 4**

  ```
  | filter event.type == "com.easytrade.deposit" OR event.type == "com.easytrade.withdraw"
  ```

  Новый фильтр объединяет два различных типа событий: депозит средств в EasyTrade и вывод средств с торговой платформы.
* **Строка 5**

  ```
  | fieldsAdd deposit_ts = if(event.type == "com.easytrade.deposit", timestamp)
  ```

  Команда [`fieldsAdd`](../../platform/grail/dynatrace-query-language/commands.md#fields-add "Список команд DQL.") создает новое поле: временную метку. Это временная метка депозита.
* **Строка 6**

  ```
  | fieldsAdd withdraw_ts = if(event.type == "com.easytrade.withdraw", timestamp)
  ```

  Команда [`fieldsAdd`](../../platform/grail/dynatrace-query-language/commands.md#fields-add "Список команд DQL.") создает новое поле: временную метку. Это временная метка вывода средств.
* **Строка 7**

  ```
  | summarize {first_deposit_ts = takeFirst(deposit_ts), first_withdraw_ts = takeFirst(withdraw_ts)}, by:{`accountId`}
  ```

  Команда [`summarize`](../../platform/grail/dynatrace-query-language/commands/aggregation-commands.md#summarize "Команды агрегации DQL") группирует по аккаунту:

  + Первую временную метку события депозита.
  + Первую временную метку события вывода средств.
* **Строка 8**

  ```
  | fieldsAdd timeDepositToDeposit= (first_withdraw_ts - first_deposit_ts) /(1000000000.0)
  ```

  Создает новое поле для вычисления разницы между двумя временными метками для расчета времени между первым депозитом и первым выводом средств по аккаунту (в секундах).
* **Строка 9**

  ```
  | filter timeDepositToDeposit > duration(0,unit:"ns")
  ```

  Эта команда filter удаляет все нулевые и отрицательные значения, поэтому любой вывод средств, произошедший до депозита, исключается из результатов.
* **Строка 10**

  ```
  | fields `accountId`, `Seconds From Deposit To Deposit`= timeDepositToDeposit
  ```

  Команда [`fields`](../../platform/grail/dynatrace-query-language/commands/selection-and-modification-commands.md#fields "Команды выборки и модификации DQL") ограничивает вывод идентификатором аккаунта и временем между первым депозитом и первым выводом средств.

### Бизнес-события в рабочие часы

Чтобы получить бизнес-события (в данном примере --- транзакции по кредитным картам), происходящие только в рабочие часы, выберите рабочие часы для мониторинга, а затем исключите нерабочие дни (например, субботу и воскресенье) и нерабочие часы (например, с 17:00 до 6:00).

Учитывайте часовой пояс: если вы находитесь в Великобритании и анализируете события в рабочие часы компании в Сингапуре, временные метки необходимо скорректировать.

```
fetch bizevents


| filter event.provider == "www.easytrade.com"


| filter isNotNull(`cardType`)


| fieldsAdd hour = getHour(timestamp), day_of_week = getDayOfWeek(timestamp)


| filterOut day_of_week == "Sat" or day_of_week == "Sun" // Исключить выходные дни


| filterOut hour <= 6 or hour >= 17 // Исключить часы вне диапазона 6:00--17:00


| fields `Account ID`, event.type, amount, cardType, event.kind
```

На изображении ниже показаны результаты запроса в виде **Record list**.

![События в рабочие часы --- список записей](https://dt-cdn.net/images/ba-events-during-office-hours-record-list-1300-850c8b417e.webp)

### Топ-5 аккаунтов с наибольшим снижением стоимости

Чтобы найти топ-5 аккаунтов с наибольшим снижением стоимости за последние 24 часа, этот запрос сравнивает общую сумму депозитов с общей суммой выводов.

```
fetch bizevents, from:now()-1d, to:now()


| filter event.provider == "www.easytrade.com"


| filter event.type == "com.easytrade.withdraw" or event.type == "com.easytrade.deposit"


| fieldsAdd amount_withdrawal = if(event.type=="com.easytrade.withdraw", amount, else:0)


| fieldsAdd amount_deposit = if(event.type=="com.easytrade.deposit", amount, else:0)


| summarize {total_withdrawals = sum(amount_withdrawal), total_deposits = sum(amount_deposit)}, by:{accountId}


| fieldsAdd balance_change = total_deposits - total_withdrawals


| sort balance_change, direction:"ascending"


| filter balance_change < 0


| fields accountId, balance_change


| sort balance_change, direction:"ascending"


| limit 5
```

На изображении ниже показаны результаты запроса в виде **Record list**.

![Снижение стоимости аккаунта --- список записей](https://dt-cdn.net/images/ba-decrease-in-account-value-record-list-1296-e854ca9c29.webp)

### Пропущенные транзакции

Розничная компания гарантирует доставку в тот же день, принимая заказы с 8:00 до 17:00. Они отслеживают размещение заказов, подтверждение оплаты и закрытие заказов. Доставка завершается к 21:00 каждый день, и к этому моменту количество событий, зарегистрированных для каждого типа событий, должно быть одинаковым; любые расхождения помечаются как аномалия для расследования. Они запускают этот запрос в 21:00 каждый день.

* Важные типы событий для этого запроса: `com.acme.order_confirmed`, `com.acme.payment_confirmed` и `com.acme.close_order`.
* Запрос генерирует серию подсчетов из трех типов событий.
* Запрос создает новое поле с условием, которое в норме должно быть `fulfilled` (выполнено). В частности, условие выполнено, когда подсчеты для всех трех типов событий одинаковы.

```
`fetch bizevents, from:now()-24h, to:now()


| filter event.provider == "www.acme.com"


| summarize {A_place_order = countIf(event.type=="com.acme.order_confirmed"), B_payment_confirmed = countIf(event.type=="com.acme.payment_confirmed"), C_order_confirmed = countIf(event.type=="com.acme.close_order")},by:{order_id}


| fieldsAdd fulfilled = (A_place_order == B_payment_confirmed and A_place_order == C_order_confirmed)


| filter A_place_order==1
```

Результаты в виде **таблицы** показывают, какие идентификаторы заказов не выполнены (`false`) в тот же день.

![Пропущенные транзакции --- таблица](https://dt-cdn.net/images/ba-missing-transactions-table-1301-f64b4fbd01.webp)

## Дашборды

Вы также можете использовать Dashboards ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") для простой реализации всех [примеров метрик в Notebooks](#notebooks), описанных выше. На изображении ниже показан дашборд, содержащий плитки для некоторых DQL-запросов, описанных выше, и некоторых других запросов, которые являются простыми модификациями или вариациями приведенных примеров.

Выберите любую плитку, а затем выберите [**Open with** ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with")](../../analyze-explore-automate/dashboards-and-notebooks/dashboards-new.md#dashboards-open-with "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в реальном времени."), чтобы повторно использовать содержимое из Dashboards в другом приложении, например в Notebooks.

![Дашборд бизнес-аналитики для метрик](https://dt-cdn.net/images/ba-dashboard-examples-2393-86077d7d44.webp)
