---
title: Создание вычисляемых метрик для мобильных приложений в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/rum-calculated-metrics-mobile
---

# Создание вычисляемых метрик для мобильных приложений в RUM Classic

# Создание вычисляемых метрик для мобильных приложений в RUM Classic

* Практическое руководство
* Чтение: 1 мин.
* Обновлено 10 мая 2024 г.

В Dynatrace можно создавать вычисляемые метрики, чтобы использовать текущий анализ для [построения графиков](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") и [использования в API](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). Вычисляемые метрики также можно применять для добавления пользовательских оповещений.

После выбора нужного приложения можно использовать **Multidimensional Analysis**, чтобы выбрать аспекты пользовательских действий и создать вычисляемую метрику. Можно разбить выбранные метрики производительности по другому измерению, например по геолокации, браузеру и типу ошибки, или использовать только отдельные измерения, например [свойства пользовательских действий](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties "Define custom string, numeric, and date properties for your monitored web applications.").

![Дашборд с пользовательскими графиками на основе вычисляемых метрик](https://dt-cdn.net/images/image-19-1916-a1098d2ab4.png)

Дашборд с пользовательскими графиками на основе вычисляемых метрик

## Создание вычисляемой метрики

Чтобы создать вычисляемую метрику из своего приложения

1. Перейдите в **Frontend** и выберите приложение, для которого нужно создать метрику.
2. В разделе **Top 3 actions** выберите **Analyze performance**.
3. Выберите нужные параметры **OS family**, **Contribution**, период времени и **Analyze by**.
4. Опционально: с помощью панели фильтров добавьте фильтры по геолокации, производителю, Apdex и другим параметрам, чтобы сфокусировать итоговую метрику на нужных данных.
5. Выберите **Create metric**.

   ![Создание метрики на странице Multidimensional analysis](https://dt-cdn.net/images/mobile-metric-create-metric-mda-1758-a913b7f692.png)

   Создание метрики на странице Multidimensional analysis
6. Опционально: измените имя и ключ метрики и включите **Split by <dimension name>**.

   Для [мобильных](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/action-and-session-properties-mobile "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/action-and-session-properties-custom "User action and session properties, which are metadata key-value pairs, provide added visibility and deeper analysis of your end users' experience. Using these properties for your applications, you can filter user sessions, add calculated metrics, create charts, and more.") нельзя разбить метрику по свойству пользовательского действия. Разбивка по свойству пользовательского действия доступна только для веб-приложений.
7. Выберите **Create metric**.

   ![Оверлей для создания метрики](https://dt-cdn.net/images/mobile-metric-create-metric-overlay-330-88ec98fac1.png)

   Оверлей для создания метрики

Используйте метрику для создания пользовательского графика или оповещения.

В вычисляемые метрики записываются только новые данные, ретроспективные данные не включаются.

На одну среду можно иметь до 500 включённых вычисляемых метрик по всем приложениям и до 100 включённых вычисляемых метрик на приложение.

### Пример

В этом примере проанализируем `Price`, это [свойство пользовательского действия](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/define-user-action-and-session-properties#custom-properties "Define custom string, numeric, and date properties for your monitored web applications."), и отфильтруем его по `Loyalty status`, это ещё одно свойство пользовательского действия.

На странице **Multidimensional analysis** выберите период времени для анализа. Чтобы отфильтровать цены, оплаченные только платиновыми клиентами, выберите `Price` в списке **Analyze by**, а затем задайте дополнительные фильтры, выбрав `String property`, `Loyalty status` и `Platinum`.

![Пример: выручка от платиновых клиентов](https://dt-cdn.net/images/loyalty-status-example-1385-0549af2191.png)

Пример: выручка от платиновых клиентов

Также можно создать метрику и построить пользовательский график.

![Пример: создание метрики](https://dt-cdn.net/images/example-create-metric-320-b73577057f.png)

Пример: создание метрики

## Создание пользовательских графиков на основе вычисляемых метрик

Создание графиков помогает анализировать сочетания метрик приложения прямо на дашборде. Можно разбивать и фильтровать доступные сущности, чтобы точно настроить измерения метрик, отображаемые на графиках, и отфильтровать сущности, которые важны именно вам.

Подробнее о создании графиков и закреплении их на дашбордах см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

## Управление метриками

После создания вычисляемой метрики можно просмотреть её свойства, удалить её, временно отключить или создать для неё график либо metric event.

После создания метрики её свойства изменить нельзя.

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Выберите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем приложения.
4. В настройках приложения выберите **Metrics**.
5. Выберите метрику, которой нужно управлять, и проверьте её свойства или выполните одно из следующих действий.

   * **Включить или отключить** ![Значок переключателя](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") метрику
   * **Скопировать** URL API для метрики
   * **Создать график** с помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.")
   * **Создать оповещение**, чтобы создать [metric event](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
   * **Удалить метрику**

## Связанные темы

* [API метрик мобильных приложений](/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Manage calculated metrics for mobile and custom apps via the Dynatrace configuration API.")