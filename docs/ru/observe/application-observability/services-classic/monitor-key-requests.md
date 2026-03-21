---
title: Мониторинг ключевых запросов
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/monitor-key-requests
scraped: 2026-03-06T21:17:32.546778
---

Переход на Enhanced endpoints для SDv1

Настройка ключевых запросов недоступна для сред, созданных в Dynatrace версии 1.330+.

Вместо определения ключевых запросов, как описано на этой странице, мы настоятельно рекомендуем включить [функцию **Enhanced endpoints for SDv1**](../services/service-detection/service-detection-v1/enhanced-endpoints-sdv1.md "Utilize the Enhanced endpoints for SDv1 feature to gain deeper insights into your application's performance and improve your ability to monitor and troubleshoot service interactions."), которая позволяет отображать все конечные точки в [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](../services/services-app.md "Maintain centralized control over service health, performance, and resources with the Services app."), а не только ключевые запросы.

*Ключевые запросы* — это запросы, требующие особого внимания, либо потому что они являются критическим показателем успеха вашего бизнеса (например, запрос на вход или запрос на оформление заказа в корзине), либо потому что они обеспечивают жизненно важную техническую функциональность, от которой зависит ваше приложение.

* Ключевые запросы имеют [выделенные метрики](../../../analyze-explore-automate/metrics-classic/built-in-metrics.md#key-requests "Explore the complete list of built-in Dynatrace metrics."), которыми можно управлять через веб-интерфейс или [API](#manage-api). Вы можете создавать специальные плитки дашборда для отображения ключевых запросов с прямым доступом с дашборда и анализировать долгосрочную историю метрик ключевых запросов в [графиках запросов](../services-classic.md#request-charting "Learn about Dynatrace's classic service monitoring").
* Оповещения всегда включены для ключевых запросов, даже когда они составляют менее 1% от пропускной способности. Они также предоставляют пользовательские пороговые значения.
* Периоды хранения данных ключевых запросов поддерживаются следующим образом:

Ключевые запросы выделены в разделе **Key requests/endpoints** на странице обзора каждого сервиса. Такая видимость особенно ценна для низкообъёмных, но высокоприоритетных запросов, которые в противном случае оказались бы внизу списка **Top requests**.

Количество ключевых запросов ограничено:

* 500 ключевых запросов на среду по всем сервисам.
* 100 ключевых запросов на сервис.

Когда вы достигаете этого лимита, рассмотрите использование [вычисляемых метрик сервисов](../services/calculated-service-metric.md "Learn how to create a calculated metric based on web requests."), которые предлагают более гибкий подход.

## Создание ключевого запроса (через веб-интерфейс)

Чтобы отметить конкретный запрос как ключевой

1. Перейдите в ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Выберите нужный сервис из списка.
3. На странице обзора сервиса нажмите кнопку **View** (например, **View requests**, **View dynamic requests** или **View resource requests**).
4. Прокрутите вниз до **Top requests** и выберите запрос, который хотите отметить как ключевой.
5. На странице обзора запроса нажмите **More** (**...**) > **Mark as key request** или **Pin to dashboard**.

   ![Set key request](https://dt-cdn.net/images/key-request-1000-c04070fc96.png)

После ручной пометки ключевого запроса его линии тренда сохраняются бессрочно.

## Отображение ключевых запросов на дашборде

Чтобы создать плитку дашборда для конкретного запроса

1. Перейдите в ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
2. Выберите нужный сервис из списка.
3. На странице обзора сервиса нажмите **View** (**View requests**, **View dynamic requests** или **View resource requests**).
4. Прокрутите вниз до **Key requests/endpoints** и выберите запрос, который хотите отобразить на дашборде.
5. На странице обзора запроса нажмите **More** (**...**) > **Pin to dashboard**.
   На ваш дашборд будет добавлена новая плитка, специфичная для запроса, показывающая наиболее важные метрики для этого конкретного запроса.

Плитки дашборда содержат только данные, собранные после того, как запрос был отмечен как ключевой.

## Переименование ключевых запросов

Определение ключевых запросов основано на именах. Когда вы применяете [правило именования запросов](../services/service-detection/service-detection-v1/set-up-request-naming.md "Adjust request naming and define the operations your services offer."), это может повлиять на ключевые запросы. Если вы хотите, чтобы Dynatrace продолжал определять переименованные запросы как ключевые, вам нужно добавить новое имя в список имён ключевых запросов.

1. Перейдите в ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** и выберите сервис, который хотите настроить.
2. Нажмите **More** (**...**) > **Settings**.
3. На странице **Service settings** перейдите на вкладку **Key requests** и нажмите **Add item**, чтобы добавить имя, к которому применяются правила именования запросов.

## Обнаружение аномалий с ключевыми запросами

Dynatrace предполагает, что низкообъёмные запросы менее важны, чем высокообъёмные и ключевые запросы. Это означает, что запросы, составляющие менее 1% от общей нагрузки сервиса, не будут вызывать оповещения, если их влияние не настолько значительно, что затрагивает общее время отклика или частоту ошибок сервиса. Поскольку такой подход по умолчанию не подходит для всех низкообъёмных запросов, вам следует вручную пометить любые важные низкообъёмные запросы как ключевые, чтобы обеспечить для них стандартные пороговые значения оповещений.

### Пороговые значения оповещений для конкретных запросов

Поскольку определённые запросы могут иметь специфические паттерны времени отклика и частоты ошибок, в то время как другие могут иметь строгие пороговые значения SLA, Dynatrace позволяет определять пользовательские пороговые значения оповещений при обнаружении аномалий, связанных с производительностью ключевых запросов. Если установлены, пороговые значения на уровне ключевых запросов переопределяют пороговые значения на уровне сервиса. Чтобы узнать, как установить пороговые значения на уровне запросов, см. [**Пороговые значения для конкретного веб-запроса**](../../../dynatrace-intelligence/anomaly-detection/adjust-sensitivity-anomaly-detection/adjust-sensitivity-services.md#key-request "Learn how to adapt the sensitivity of problem detection for services.").

## Вычисляемая метрика сервиса

В качестве альтернативного способа фокусировки на определённых запросах вы можете создать [вычисляемую метрику сервиса](../services/calculated-service-metric.md "Learn how to create a calculated metric based on web requests.") на основе нужных запросов. Этот подход обеспечивает большую гибкость с оповещениями — вы можете использовать вычисляемую метрику так же, как любую встроенную метрику Dynatrace.

## Управление ключевыми запросами через Settings API

Вы можете управлять конфигурациями ключевых запросов через [Settings API](../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.").

Для использования API вам необходим токен доступа с областями действия **Read settings** (`settings.read`) и **Write settings** (`settings.write`). Чтобы узнать, как его получить, см. [Создание токена доступа](../../../dynatrace-api/basics/dynatrace-api-authentication.md#create-token "Find out how to get authenticated to use the Dynatrace API.").

### Создание конфигурации ключевого запроса

Выполните следующие шаги для создания новой конфигурации ключевого запроса. Обратите внимание, что эта процедура перезаписывает любую существующую конфигурацию. Если вы хотите изменить существующую конфигурацию, см. раздел [**Обновление конфигурации ключевого запроса**](#update-api) ниже.

1. Чтобы узнать формат объекта настроек, запросите его схему через вызов [GET a schema](../../../dynatrace-api/environment-api/settings/schemas/get-schema.md "View a settings schema via the Dynatrace API."). Идентификатор схемы ключевого запроса — `builtin:settings.subscriptions.service`.
2. Создайте JSON-объект для ваших настроек.
   Обратите внимание, что область действия ключевого запроса — всегда сервис. Вы должны указать сервис по его идентификатору сущности Dynatrace. Чтобы узнать идентификатор сущности вашего сервиса, используйте запрос [GET entities list](../../../dynatrace-api/environment-api/entity-v2/get-entities-list.md "View a list of monitored entities via Dynatrace API.").
   Пример JSON

   ```
   [


   {


   "schemaId": "builtin:settings.subscriptions.service",


   "scope": "SERVICE-123456789",


   "value": {


   "keyRequestNames": [


   "/cart/checkout"


   ]


   }


   }


   ]
   ```
3. Используйте конечную точку [POST an object](../../../dynatrace-api/environment-api/settings/objects/post-object.md "Create or validate a settings object via the Dynatrace API.") для отправки вашей конфигурации.

### Обновление конфигурации ключевого запроса

1. Чтобы узнать формат объекта настроек, запросите его схему через вызов [GET a schema](../../../dynatrace-api/environment-api/settings/schemas/get-schema.md "View a settings schema via the Dynatrace API."). Идентификатор схемы ключевого запроса — `builtin:settings.subscriptions.service`.
   Обратите внимание, что область действия ключевого запроса — всегда сервис. Вы должны указать сервис по его идентификатору сущности Dynatrace. Чтобы узнать идентификатор сущности вашего сервиса, используйте запрос [GET entities list](../../../dynatrace-api/environment-api/entity-v2/get-entities-list.md "View a list of monitored entities via Dynatrace API.").
2. Запросите текущую конфигурацию через вызов [GET objects](../../../dynatrace-api/environment-api/settings/objects/get-objects.md "View multiple settings objects via the Dynatrace API.").
3. Создайте JSON для обновления.

   1. Используйте значение **updateToken** из предыдущего шага.
   2. Измените список запросов в массиве **keyRequestNames** по необходимости.
      Пример JSON

      ```
      {


      "updateToken": "vu9U3hXY3q0ATAAkMG",


      "value": {


      "keyRequestNames": [


      "/cart/checkout",


      "/cart"


      ]


      }


      }
      ```
4. Используйте конечную точку [PUT an object](../../../dynatrace-api/environment-api/settings/objects/put-object.md "Edit a settings object via the Dynatrace API.") для отправки вашей конфигурации.

## Связанные темы

* [Анализ таймингов сервисов](service-analysis-timing.md "Find out what each time in service analysis means.")
* [Вычисляемые метрики для сервисов](../services/calculated-service-metric.md "Learn how to create a calculated metric based on web requests.")
* [Отключение мониторинга запросов сервисов](../services/service-detection/service-detection-v1/service-monitoring-mute.md "Mute the monitoring of certain service requests so that you can focus on the performance of requests that affect your customers.")
