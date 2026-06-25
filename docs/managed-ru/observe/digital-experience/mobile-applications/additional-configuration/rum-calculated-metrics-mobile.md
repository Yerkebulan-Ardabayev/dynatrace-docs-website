---
title: Создание вычисленных метрик для мобильных приложений
source: https://docs.dynatrace.com/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile
scraped: 2026-05-12T11:07:00.377874
---

# Создание вычисленных метрик для мобильных приложений

# Создание вычисленных метрик для мобильных приложений

* How-to guide
* 1-min read
* Updated on May 10, 2024

В Dynatrace вы можете создавать вычисленные метрики для использования текущего анализа в [графиках](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.") и [API](/managed/dynatrace-api/environment-api/metric-v2 "Получайте информацию о метриках через Metrics v2 API."). Также вы можете использовать вычисленные метрики для добавления пользовательских оповещений.

Выбрав интересующее вас приложение, вы можете использовать **Multidimensional Analysis** для выбора аспектов пользовательских действий и создания вычисленной метрики. Вы можете разбить выбранные метрики производительности по другому измерению, например по геолокации, браузеру и типу ошибки, или использовать только одно измерение, например [свойства пользовательских действий](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties "Определяйте пользовательские строковые, числовые и датовые свойства для отслеживаемых веб-приложений.").

![Dashboard with custom charts based on calculated metrics](https://dt-cdn.net/images/image-19-1916-a1098d2ab4.png)

Dashboard with custom charts based on calculated metrics

## Создание вычисленной метрики

Чтобы создать вычисленную метрику из приложения:

1. Перейдите в **Frontend** и выберите приложение, для которого нужно создать метрику.
2. В разделе **Top 3 actions** нажмите **Analyze performance**.
3. Выберите нужные параметры **OS family**, **Contribution**, временной диапазон и **Analyze by**.
4. Необязательно: используйте строку фильтра, чтобы добавить фильтры по геолокации, производителю, Apdex и другим параметрам для уточнения результирующей метрики.
5. Нажмите **Create metric**.

   ![Creating a metric on the Multidimensional analysis page](https://dt-cdn.net/images/mobile-metric-create-metric-mda-1758-a913b7f692.png)

   Creating a metric on the Multidimensional analysis page
6. Необязательно: измените имя и ключ метрики, включите **Split by <dimension name>**.

   Для [мобильных](/managed/observe/digital-experience/mobile-applications/analyze-and-use/action-and-session-properties-mobile "Свойства пользовательских действий и сессий — пары ключ-значение метаданных.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/analyze-and-use/action-and-session-properties-custom "Свойства пользовательских действий и сессий — пары ключ-значение метаданных.") разбивка метрики по свойству пользовательского действия недоступна. Разбивка по свойству пользовательского действия доступна только для веб-приложений.
7. Нажмите **Create metric**.

   ![Overlay for creating a metric](https://dt-cdn.net/images/mobile-metric-create-metric-overlay-330-88ec98fac1.png)

   Overlay for creating a metric

Используйте метрику для создания пользовательского графика или оповещения.

В вычисленные метрики записываются только новые данные; ретроспективные данные не включаются.

На одно окружение можно иметь до 500 включённых вычисленных метрик во всех приложениях и до 100 включённых вычисленных метрик на приложение.

### Пример

В этом примере проанализируем `Price` — [свойство пользовательского действия](/managed/observe/digital-experience/web-applications/additional-configuration/define-user-action-and-session-properties#custom-properties "Определяйте пользовательские строковые, числовые и датовые свойства для отслеживаемых веб-приложений.") — и отфильтруем его по `Loyalty status`, которое является ещё одним свойством пользовательского действия.

На странице **Multidimensional analysis** выберите временной диапазон анализа. Чтобы отфильтровать цены, оплаченные только клиентами уровня platinum, выберите `Price` в списке **Analyze by**, а затем установите дополнительные фильтры, выбрав `String property`, `Loyalty status` и `Platinum`.

![Example - Revenue by platinum customers](https://dt-cdn.net/images/loyalty-status-example-1385-0549af2191.png)

Example - Revenue by platinum customers

Также вы можете создать метрику и сформировать пользовательский график.

![Example - Create a metric](https://dt-cdn.net/images/example-create-metric-320-b73577057f.png)

Example - Create a metric

## Создание пользовательских графиков на основе вычисленных метрик

Создание графиков помогает анализировать комбинации метрик приложения непосредственно на панели мониторинга. Вы можете разбивать и фильтровать доступные сущности для точной настройки измерений метрики в графиках.

Подробнее о создании графиков и их закреплении на панелях мониторинга см. в разделе [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.").

## Управление метриками

После создания вычисленной метрики вы можете просматривать её свойства, удалять, временно отключать или создавать для неё график или метрическое событие.

После создания метрики изменить её свойства нельзя.

1. Перейдите в **Frontend**.
2. Выберите приложение, которое нужно настроить.
3. Нажмите **More** (**…**) > **Edit** в правом верхнем углу плитки с именем вашего приложения.
4. В настройках приложения выберите **Metrics**.
5. Выберите метрику, которой нужно управлять, и проверьте её свойства или выполните одно из следующих действий.

   * **Enable or disable** ![Toggle icon](https://dt-cdn.net/images/icon-toggle-barista-701-35879d6adf.png "Toggle icon") — включить или отключить метрику
   * **Copy** — скопировать URL API для метрики
   * **Create a chart** с помощью [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразовывайте результаты для получения нужных аналитических данных.")
   * **Create alert** — создать [метрическое событие](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace")
   * **Delete metric** — удалить метрику

## Связанные темы

* [Mobile app metrics API](/managed/dynatrace-api/configuration-api/calculated-metrics/mobile-app-metrics "Управляйте вычисленными метриками для мобильных и пользовательских приложений через API конфигурации Dynatrace.")