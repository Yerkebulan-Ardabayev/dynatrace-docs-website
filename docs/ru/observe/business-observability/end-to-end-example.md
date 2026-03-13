---
title: Business events end-to-end example
source: https://www.dynatrace.com/docs/observe/business-observability/end-to-end-example
scraped: 2026-03-06T21:14:48.552772
---

# Сквозной пример бизнес-событий

# Сквозной пример бизнес-событий

* Latest Dynatrace
* Tutorial
* 7-min read
* Updated on Jan 28, 2026

Этот сценарий использования показывает, как можно захватить данные, настроить правило обработки и как эти данные можно далее анализировать и визуализировать.

## Целевая аудитория

Эта статья предназначена для бизнес-аналитиков и менеджеров процессов, которые хотят понимать эффективность своего бизнеса в реальном времени и стремятся к оптимальному выполнению бизнес-процессов. Вы должны обладать базовыми знаниями о том, как захватываются бизнес-события, и определённым пониманием предметной области бизнеса, которую вы анализируете.

## Сценарий

EasyTrade — это симулированное торговое приложение со следующими сценариями использования:

* Внесение и снятие денежных средств
* Транзакции покупки и продажи активов
* Базовые дашборды для вашей торговой деятельности
* Заказ кредитной карты

В данном сценарии предположим, что вам нужно рассчитать общую сумму депозитов для каждого счёта, общий и максимальный долларовый объём торгов по счёту в EasyTrade, а также общую сумму транзакций покупки активов по счёту в операциях быстрой покупки.

## Перед началом работы

Вам необходимо определить:

* Логику и правила обработки
* Необходимые поля данных

Поскольку вам нужно рассчитать долларовый объём торгов, ваше правило обработки должно умножить цену на количество и добавить результат как новое поле события:

**Dollar Trading Volume** = **Price** \* **Amount**

Вам также нужно определить элементы данных запроса быстрой покупки актива. Например:

```
{



"accountId":6,



"amount":10,



"instrumentId":1,



"price":157.025



}
```

## Шаги

1. Создание правила захвата

1. Перейдите в приложение ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. Выберите **Collect and capture** > **Business Events** > **Incoming**.
3. Выберите **Add new capture rule** и задайте **Rule name** как `easyTrade- /v1/trade/buy`.
4. Выберите **Add trigger** и в разделе **Summary** задайте следующее:

   * **Data source**: `Request - Path`
   * **Operator**: `starts with`
   * **Value**: `- /v1/trade/buy`
5. Снова выберите **Add trigger** и в разделе **Summary** задайте следующее:

   * **Data source**: `Request — HTTP Method`
   * **Operator**: `equals`
   * **Value**: `POST`
6. Определите **Event provider**:

   * **Data source**: `Fixed value`
   * **Fixed value**: `www.easytrade.com`
7. Определите **Event type**:

   * **Data source**: `Fixed value`
   * **Fixed value**: `com.easytrade.quick-buy`

     Если вам нужно добавить дополнительные типы событий, выберите **Event type** отдельно для каждого типа. В данном случае типами событий также будут `com.easytrade.` и `com.easytrade.deposit`.
8. Определите **Event category:**

   * **Data source**: `Fixed value`
   * Необязательное **Fixed value:** в данном случае можно оставить пустым.
9. В разделе **Event data** необходимо добавить четыре поля данных.

   Для каждого поля данных:

   1. Выберите **Add data field**.
   2. Задайте значения **Field name**, **Source** и **Path** согласно следующей таблице:
10. Выберите **Save changes**.

2. Добавление полей

Для создания правила обработки данных:

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**.
2. Выберите **Business Events** > вкладку **Pipelines**.
3. Для создания нового конвейера выберите  **Pipeline** и введите имя — `Process EasyTrade data`.
4. На вкладке **Processing** выберите  **Processor** > **DQL** и назовите процессор `EasyTrade trade volume`.
5. Задайте **Matching condition** вашего правила как следующий [DQL-запрос для matcher](../../platform/openpipeline/reference/dql-matcher-in-openpipeline.md "Examine specific DQL functions and logical operators for log processing."):

   ```
   matchesValue(event.provider, "www.easytrade.com")
   ```

   1. Подробности

   * Если вам нужно добавить только один тип события (например, `com.easytrade.buy-assets`), matcher будет следующим:

     ```
     matchesValue(event.type, "com.easytrade.buy-assets")
     ```
   * Для двух типов событий в рамках одного поставщика событий matcher будет следующим:

     ```
     matchesValue(event.type, "com.easytrade.buy-assets") or matchesValue(event.type, "com.easytrade.sell-assets")
     ```
   * Однако в данном сценарии вам нужно охватить все типы событий поставщика EasyTrade, поэтому достаточно использовать:

     ```
     matchesValue(event.provider, "www.easytrade.com")
     ```
6. В поле **DQL processor definition** добавьте:

   ```
   fieldsAdd trade_volume=amount*price
   ```
7. Выберите **Save**.
8. Для создания нового маршрута перейдите на вкладку **Dynamic routing** >  **Dynamic route** и укажите:

   * Описательное имя для вашего нового динамического маршрута
   * **Matching condition**:

     ```
     matchesValue(event.provider, "www.easytrade.com")
     ```
9. Выберите конвейер `Process EasyTrade data`, в который будут направляться бизнес-события.
10. Выберите **Add**, затем **Save**.
    Примечание: любое правило, добавленное в раздел **Dynamic routing** конвейера `Process EasyTrade data`, будет обрабатывать данные в рамках того же условия сопоставления.

3. Извлечение метрики бизнес-события

Для добавления метрики бизнес-события:

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**.
2. Выберите **Business Events** > вкладку **Pipelines**.
3. Выберите ранее созданный конвейер `Process EasyTrade data`.
4. Перейдите на вкладку **Metric Extraction**.
5. Выберите  **Processor** > **Value metric** и назовите его `bizevents.EasyTrade.TradingVolume`.
6. Добавьте **Matching condition** к вашему правилу, вставив [DQL-запрос для matcher](../../platform/openpipeline/reference/dql-matcher-in-openpipeline.md "Examine specific DQL functions and logical operators for log processing."):

   ```
   matchesValue(event.type, "com.easyTrade.quick-buy")
   ```
7. Выберите **Field extraction**, на основе которого будет строиться метрика — добавьте `trading_volume`.
8. В поле **Metric key** назовите метрику `bizevents.EasyTrade.TradingVolume`.
9. Вы также можете выбрать **Dimensions**: либо **Pre-defined**, например `dt.entity.host`, либо **Custom**.
10. Выберите **Save**.

Для отображения метрик:

1. Перейдите в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
2. Выберите  **Notebook** и назовите его `Notebook for business analytics metrics`.
3. Для открытия конструктора запросов метрик добавьте новый раздел и выберите  **Metrics**.
4. Найдите свою метрику в окне поиска, выберите **Run** и отобразите результаты.

   Вы также можете:

   * Закрепить метрику на дашборде
   * Экспортировать данные в CSV-файл
   * Поделиться ссылкой
   * Скопировать DQL-запрос
   * Использовать Dynatrace Intelligence для анализа временных рядов, обнаружения аномалий или прогнозирования

4. Выбор периода хранения

Если вам нужно хранить данные в течение одного года, например для целей налогового учёта, сначала необходимо создать корзину для bizevents с периодом хранения один год.

1. Перейдите в приложение ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**.
2. Выберите **Storage management** > **Bucket storage management**.
3. Выберите  **Bucket** и назовите корзину уникальным идентификатором — `easytrade-bizevents`.
4. Добавьте **Display name** `EasyTrade bizevents`.
5. Определите период хранения — 365 дней.
6. Для **Bucket table type** выберите `bizevents`.
7. Выберите **Create**.

После создания корзины необходимо определить правила для хранения входящих bizevents в этой корзине.

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline**.
2. Выберите **Business Events** > вкладку **Pipelines**.
3. Выберите `Process Easytrade data` из списка конвейеров.
4. Перейдите на вкладку **Storage**, выберите  **Processor** > **Bucket assignment**.
5. Назовите его `Easytrade data bucket assignment`.
6. Определите **Matching condition** как `true` (так как все маршрутизированные bizevents принадлежат данным `EasyTrade data`).
7. Задайте **Storage** как `EasyTrade bizevents`.
8. Выберите **Save**.

5. Проверка результатов

Чтобы убедиться, что данные захвачены корректно:

1. Выберите **Run in Playground** под этим запросом:

   ```
   fetch bizevents



   | filter event.provider == "www.easytrade.com"



   | filter event.type == "com.easytrade.quick-buy" OR event.type == "com.easytrade.deposit" OR event.type == "com.easytrade.quick-sell"



   | sort timestamp desc
   ```

   Run in Playground
2. Выберите **New notebook**, и запрос выполнится автоматически.

   Вы должны получить результаты, подобные следующим:

   ![Analyze your data with DQL](https://dt-cdn.net/images/analyze-your-data-with-dql-blurred-2634-444ada5143.png)

6. Анализ данных с помощью DQL

На этом этапе вы можете начать создание [DQL](../../platform/grail/dynatrace-query-language.md "How to use Dynatrace Query Language.")-запросов для анализа загруженных данных, определения метрик и создания графиков и дашбордов.

Вам необходимо рассчитать:

* Общую сумму депозитов по каждому счёту за последние 30 дней
* Общую сумму транзакций покупки активов по каждому счёту за последние 30 дней
* Общий и максимальный долларовый объём торгов по каждому счёту за последние 30 дней

Для анализа данных с помощью DQL выберите **Run in Playground** под этим запросом:

```
fetch bizevents, from:now()-30d, to:now()



| filter event.provider == "www.easytrade.com" and (event.type == "com.easytrade.quick-buy" OR event.type == "com.easytrade.deposit" OR event.type == "com.easytrade.quick-sell")



| fieldsAdd moneyTransfered = if(event.type == "com.easytrade.deposit", toDouble(amount)),



buyAssets = if(event.type == "com.easytrade.quick-buy", toDouble(amount)),



trading_volume= if(event.type == "com.easytrade.quick-sell",(amount*price))



| summarize sum(moneyTransfered), sum(buyAssets), sum(trading_volume), max(trading_volume), by:accountId
```

Run in Playground

Таблица результатов:

7. Отображение результатов

Вы можете отобразить результаты несколькими способами, включая следующие варианты.

* В виде столбчатой диаграммы в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ограничив результат топ-10 с максимальным переводом средств.

  1. Выберите  Options.
  2. На панели справа выберите тип визуализации **Bar**.
* На плитке дашборда

  Чтобы закрепить результаты на дашборде в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**:

  1. Выберите  >  **Open with**.
  2. Выберите ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
  3. Решите, хотите ли вы открыть его в новом дашборде или в существующем.