---
title: Извлечение метрики из пользовательских сеансов
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-sessions
scraped: 2026-03-06T21:15:52.450536
---

# Извлечение метрики из пользовательских сессий


* Latest Dynatrace
* Tutorial
* Updated on Mar 05, 2026

OpenPipeline позволяет извлекать пользовательские метрики из [пользовательских сессий](../concepts/data-model.md#user-sessions "Ознакомьтесь с моделью данных, лежащей в основе New RUM Experience."), что обеспечивает долгосрочный анализ в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, который выходит далеко за рамки стандартного мониторинга производительности. Комбинируя эти метрики со [свойствами пользовательских сессий](../concepts/data-model.md#event-and-session-properties "Ознакомьтесь с моделью данных, лежащей в основе New RUM Experience."), вы получаете гибкость для выявления инсайтов, максимально адаптированных к вашим бизнес-целям.

Для иллюстрации этого процесса данное руководство проведёт вас через извлечение метрики конверсии клиентов из пользовательских сессий, показывая количество сессий, завершившихся конверсией клиента, в сравнении с теми, которые не завершились конверсией.

## Пример сценария

В этом руководстве мы будем использовать интернет-магазин в качестве примера. Магазин инструментирован с помощью RUM JavaScript, а собранные данные привязаны к [фронтенду](../concepts/frontends.md "Узнайте о концепции фронтенда в New RUM Experience.") с именем `webshop`.

Инструментация была настроена для отправки свойства пользовательской сессии `successful_checkout` каждый раз, когда клиент успешно завершает процесс оформления заказа. Свойство было сконфигурировано, как описано в [Захват свойств событий и сессий для веб-фронтендов](../web-frontends/additional-configuration/event-and-session-properties.md "Узнайте, как захватывать свойства событий и сессий для веб-фронтендов."), а затем отправлено через JavaScript API с помощью [`sendSessionPropertyEvent`](https://docs.dynatrace.com/javascriptapi/doc-latest/functions/Types.dynatrace.sendSessionPropertyEvent.html):

```
dynatrace.sendSessionPropertyEvent({


"session_properties.successful_checkout": true


});
```

С такой настройкой вы можете проанализировать количество сессий с конверсией и без конверсии клиента, выполнив следующий DQL-запрос:

```
fetch user.sessions


| summarize by:{session_properties.successful_checkout}, count()
```

Хотя этот запрос хорошо работает для краткосрочного анализа, он не идеален для выявления долгосрочных закономерностей, что гораздо лучше выполняется с помощью пользовательской метрики.

## Прежде чем начать

Необходимые знания

* [Dynatrace Query Language](../../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [Обработка в OpenPipeline](../../../../platform/openpipeline/concepts/processing.md "Изучите основные концепции обработки в Dynatrace OpenPipeline.")

Предварительные требования

Убедитесь, что у вас есть разрешения, описанные в [Разрешения New RUM Experience](../permissions.md "Узнайте, какие разрешения необходимы для настройки New RUM Experience.").

## Инструкция

1. Создание конвейера для извлечения метрик

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User sessions** > **Pipelines**.
2. Чтобы создать новый конвейер, выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** и введите имя (например, `Webshop`).
3. Для настройки извлечения метрик перейдите в **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Counter metric** и определите процессор, указав:

   * Описательное **Name** (имя) (например, `Conversion statistics`).
   * **Matching condition** (условие сопоставления) (`true`).
   * **Metric key** (ключ метрики) (`webshop.checkout_statistics`).
   * Измерение метрики в разделе **Dimensions**

     1. Выберите **Custom**.
     2. Введите **Field name on record** (имя поля в записи) (`session_properties.successful_checkout`).
     3. Введите **Dimension name** (имя измерения) (`successful_checkout`).
     4. Введите **Default value** (значение по умолчанию) (`false`).
4. Выберите **Add dimension**.
5. Выберите **Save**.

2. Маршрутизация данных в конвейер

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User sessions** > **Dynamic routing**.
2. Чтобы создать новый маршрут, выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** и укажите:

   * Описательное **Name** (имя) (например, `Webshop route`).
   * **Matching condition** (условие сопоставления). В нашем примере условие сопоставления:

     ```
     matchesValue(frontend.name, "webshop")
     ```
   * **Pipeline** (конвейер), содержащий инструкции обработки (`Webshop`).
3. Выберите **Save**.

## Заключение

Вы успешно извлекли пользовательскую метрику из пользовательских сессий. Теперь вы можете перейти в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и просмотреть её, например, с помощью следующего запроса:

```
timeseries sum(easytravel.checkout_statistics), by: { successful_checkout }, interval: 15m


| fieldsAdd checkout_status = if(successful_checkout == "true", "Successful Checkout", else: "No Checkout")
```

![Пользовательская метрика, извлечённая из пользовательских сессий, показывающая конверсию клиентов в интернет-магазине](https://dt-cdn.net/images/custom-metric-extraction-from-user-sessions-example-1174-7eec1c7551.png)

## Связанные темы

* [Dynatrace Query Language](../../../../platform/grail/dynatrace-query-language.md "Как использовать Dynatrace Query Language.")
* [Обработка в OpenPipeline](../../../../platform/openpipeline/concepts/processing.md "Изучите основные концепции обработки в Dynatrace OpenPipeline.")
* [Захват свойств событий и сессий для веб-фронтендов](../web-frontends/additional-configuration/event-and-session-properties.md "Узнайте, как захватывать свойства событий и сессий для веб-фронтендов.")
* [Захват свойств событий и сессий для мобильных фронтендов](../mobile-frontends/additional-configuration/event-and-session-properties.md "Узнайте, как захватывать свойства событий и сессий для мобильных фронтендов.")
