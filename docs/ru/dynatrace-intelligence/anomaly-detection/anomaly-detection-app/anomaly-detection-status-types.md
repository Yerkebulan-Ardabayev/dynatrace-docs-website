---
title: Anomaly Detection status types
source: https://www.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types
scraped: 2026-03-06T21:20:51.429284
---

# Типы статусов Anomaly Detection

# Типы статусов Anomaly Detection

* Последняя версия Dynatrace
* Пояснение
* Время чтения: 3 мин
* Опубликовано 20 янв. 2025 г.

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** предоставляет столбец **Status**, который отображает состояние работоспособности пользовательского оповещения и содержит информацию об успешности выполнения пользовательских оповещений в фоновом режиме за последние 24 часа. Это означает, что при возникновении ошибки или предупреждения пользовательское оповещение отправит событие предупреждения или ошибки. Эти события затем сравниваются с успешными событиями за последние 24 часа.

Статус пользовательского оповещения может измениться с предупреждения на ошибку, если успешность выполнения со временем падает ниже 95%.

Кроме того, столбец **Status** содержит информацию о недоступности данных об успешности выполнения, которая может быть разделена на три типа:

* **Pending** (Ожидание). Этот статус указывает, что пользовательское оповещение ещё не было выполнено или что запрос не содержит исполняемых событий.
* **Unavailable** (Недоступно). Этот статус указывает, что у вас могут отсутствовать необходимые разрешения для доступа к информации о статусе.
* **Inactive** (Неактивно). Этот статус указывает, что пользовательское оповещение в данный момент отключено.

## Список статусов Anomaly Detection

Пользовательское оповещение может иметь любой из следующих типов статусов:

## Устранение неполадок

Если статус пользовательского оповещения показывает ошибку, нажмите **Error** > **View more details**, чтобы просмотреть сообщение об ошибке.

Некоторые сообщения об ошибках могут быть более сложными, чем другие. Ниже приведены некоторые распространённые из них, которые помогут вам быстрее решить проблему.

* `Query failed because the response time exceeded 10000 ms`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** устанавливает 10-секундный лимит выполнения для запросов. Этот защитный лимит помогает предотвратить задержку или зависание других конфигураций пользовательских оповещений в очереди.

* `Anomaly detector failed with an unauthorized request. Fix the required permissions in the authorization settings`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** не имеет необходимых разрешений и не может читать данные от вашего имени. Для получения дополнительной информации о необходимых разрешениях и редактировании параметров авторизации см. разделы [Предварительные требования](../anomaly-detection-app.md#prerequisites "Изучите конфигурации обнаружения аномалий с помощью приложения Anomaly Detection.") и [Включение или редактирование параметров авторизации Anomaly Detection](../anomaly-detection-app.md#edit-authorization-settings "Изучите конфигурации обнаружения аномалий с помощью приложения Anomaly Detection.").
* `Query does not result in a valid timeseries: No valid time series records found. A valid time series record contains a single duration field, a single timeframe and one or multiple numeric arrays. Consider using the 'timeseries' or 'makeTimeseries' DQL command`: ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** требует временного ряда для автоматической проверки условия оповещения. Для получения дополнительной информации и примеров допустимого запроса см. раздел [Примеры ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** на Grail](../../use-cases/anomaly-detection-examples.md "Используйте возможности Grail и DQL для преобразования любых данных в временные ряды для анализаторов обнаружения аномалий.").

## Связанные темы

* [Приложение Anomaly Detection](../anomaly-detection-app.md "Изучите конфигурации обнаружения аномалий с помощью приложения Anomaly Detection.")
* [Примеры обнаружения аномалий на Grail](../../use-cases/anomaly-detection-examples.md "Используйте возможности Grail и DQL для преобразования любых данных в временные ряды для анализаторов обнаружения аномалий.")
