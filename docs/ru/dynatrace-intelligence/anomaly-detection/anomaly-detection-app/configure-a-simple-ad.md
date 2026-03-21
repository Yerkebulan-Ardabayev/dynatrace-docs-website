---
title: Настройка простого пользовательского оповещения
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-a-simple-ad
scraped: 2026-03-06T21:35:01.911530
---

* Latest Dynatrace
* How-to guide
* 4-min read

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** позволяет создавать пользовательские оповещения, настраивать индивидуальные оповещения и преобразовывать конфигурации событий метрик. Вы также можете сэкономить время и создать пользовательское оповещение в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** непосредственно во время работы с приложением.

## Предварительные требования

Для использования последней версии ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** вам необходимы соответствующие разрешения. Для получения дополнительной информации см. [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") обзор **Anomaly Detection**](../anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app.").

## Создание или редактирование простого пользовательского оповещения

Чтобы вручную создать конфигурацию простого пользовательского оповещения

1. Перейдите в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Create your own custom alert** для создания нового оповещения. Для редактирования существующего пользовательского оповещения выберите любое пользовательское оповещение из списка.
3. На вкладке **Simple** разверните **Set scope**.
4. Необязательно: в **Segments** выберите один или несколько сегментов для фильтрации.
5. В **Query** укажите [DQL-запрос](../../../platform/grail/dynatrace-query-language/dql-guide.md "Find out how DQL works and what are DQL key concepts.") для получения данных.

   Мы рекомендуем использовать параметр `interval: 1m` для обеспечения надлежащего разрешения данных при анализе.
6. Разверните **Define alert condition**.
7. В **Select use case** выберите предпочтительный анализатор. Подробности см. в разделе [Тип и параметры анализатора](../anomaly-detection-configuration.md#analyzer "How to set up an alert for missing measurements.").
8. В **Set a condition** > **Threshold** выберите **Suggest values**, если хотите, чтобы Dynatrace Intelligence автоматически предложила значение на основе последнего поведения ваших данных. Вы также можете выбрать желаемое пороговое значение и **Unit** (единицу измерения) вручную.
9. Необязательно: в **Set a condition** > **Alert condition** выберите:

   * **Alert if metric is above** — для получения оповещений, когда значение превышает пороговое.
   * **Alert if metric is below** — для получения оповещений, когда значение ниже порогового.
10. Необязательно: выберите **Preview** для просмотра демонстрации вашего условия оповещения.
11. Разверните **Add details**.
12. Установите **Title** для присвоения имени вашему пользовательскому оповещению.
13. Установите **Event name** — любое имя по вашему выбору. **Event name** будет отображаться как заголовок событий, генерируемых этим пользовательским оповещением.

    Вы можете ввести `{`, чтобы Dynatrace Intelligence предложила вам имена-заполнители с нужными значениями (например, `{alert_condition}`). Для получения дополнительной информации см. [Шаблон события](../anomaly-detection-configuration.md#event-template "How to set up an alert for missing measurements.").
14. Выберите **Create** для создания простого пользовательского оповещения или **Save** для обновления вашей конфигурации.

При каждом нажатии **Create** или **Save** конфигурация пользовательского оповещения автоматически проходит валидацию. Если в конфигурации нет ошибок, вы сможете сохранить или обновить конфигурацию. При наличии ошибок соответствующий раздел будет выделен красным цветом и помечен сообщением `Error` под заголовком раздела.

Проверьте **Status** новой конфигурации вскоре после создания, чтобы убедиться в отсутствии ошибок при выполнении.

## Создание простого пользовательского оповещения в Notebooks

С помощью Dynatrace Intelligence для Notebooks вы можете предварительно просмотреть конфигурацию пользовательского оповещения и оценить её эффективность. Этот вариант перенаправляет вас в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, где вы настраиваете запрос и стратегию мониторинга, а затем обратно в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** для создания шаблона события.

1. Перейдите в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Open a custom alert in Notebooks**.
3. Выберите notebook, в котором вы хотите предварительно просмотреть конфигурацию.
   Это действие перенаправит вас в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
4. Добавьте новый раздел **DQL** или **Metrics** и выполните запрос к интересующим вас данным.

   Для DQL-запроса мы рекомендуем использовать параметр `interval: 1m` для обеспечения надлежащего разрешения данных при анализе.
5. Необязательно: выберите , затем выберите один или несколько сегментов для фильтрации.
6. Выберите **Options** > **Analyze and alert**.
7. Активируйте анализатор.
8. Выберите необходимый анализатор и настройте его. Подробности см. в разделе [Конфигурация обнаружения аномалий](../anomaly-detection-configuration.md "How to set up an alert for missing measurements.").
9. Выберите **Run analysis**.
10. Когда вы будете удовлетворены результатом, выберите ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with") **Open with** и выберите **Anomaly Detection**.
    Это действие перенаправит вас обратно в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
11. Разверните **Add details** и установите **Title** — любое имя по вашему выбору.
12. Установите **Event name** — любое имя по вашему выбору. **Event name** будет отображаться как заголовок событий, генерируемых этим пользовательским оповещением.
13. Выберите **Create**.

    Проверьте **Status** новой конфигурации вскоре после создания, чтобы убедиться в отсутствии ошибок при выполнении.

## Преобразование конфигурации события метрики

[События метрик](../metric-events.md "Learn about metric events in Dynatrace") расширяют возможности обнаружения аномалий, выходя за рамки стандартных сценариев использования и охватывая события на основе метрик. С помощью DQL вы можете расширить эти возможности ещё больше.

Чтобы преобразовать событие метрики в конфигурацию пользовательского оповещения

1. Перейдите в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Improve metric events with DQL**.
3. Выберите необходимое событие метрики и нажмите **Transform**.
4. Для настройки адаптивного порога и сезонной базовой линии адаптируйте запрос к разрешению в 1 минуту.

   1. Для вновь созданной конфигурации выберите преобразованное пользовательское оповещение из списка.
   2. Разверните **Set scope**.
   3. Добавьте параметр `interval:1m` к запросу.
   4. Выберите **Save** для сохранения изменений.
5. Преобразованное событие метрики автоматически отключается, и вместо него активируется вновь созданная конфигурация.

   Проверьте **Status** новой конфигурации вскоре после создания, чтобы убедиться в отсутствии ошибок при выполнении.

## Связанные темы

* [Приложение Anomaly Detection](../anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Настройка расширенного пользовательского оповещения](../../../../common/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-an-advanced-ad.md "Learn how to create and edit advanced custom alerts in the Anomaly Detection app")
* [Типы статусов Anomaly Detection](anomaly-detection-status-types.md "An explanation of Anomaly Detection status types")
* [[Видео] Повышение безопасности с помощью Anomaly Detection](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Видео] Anomaly Detection и наблюдаемость данных](https://www.youtube.com/watch?v=HPQi63mQg3w)