---
title: Настройка пользовательских оповещений на основе метрик, извлеченных из журналов
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-use-cases/lma-alert-log-based-metrics
scraped: 2026-03-06T21:33:43.409363
---

# Настройка пользовательских оповещений на основе метрик, извлечённых из логов


* Latest Dynatrace
* Руководство
* Чтение: 4 мин
* Обновлено 28 янв. 2026

Загруженные логи могут служить триггерами для создания новых проблем Davis.

Используя комбинацию метрик на основе логов и [пользовательских оповещений](../../../dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app."), вы можете применять различные анализаторы данных Dynatrace Intelligence для решения задач — от простых оповещений на основе пороговых значений до сезонных базовых линий, например:

* Оповещение, когда среднее количество совпадающих записей превышает определённое число в заданный период времени.
* Оповещение, когда значение метрики является аномальным, без установки статического порогового значения.

Следуйте этому руководству, чтобы узнать больше об оповещениях с использованием метрик на основе логов.

Если вам не нужно устанавливать пороговые значения, следуйте инструкциям в разделе [Настройка оповещений на основе событий, извлечённых из логов](lma-alert-log-based-events.md "How to create and configure Davis problems and alerts with events based on logs.").

## Предварительные требования

* Вы настроили [загрузку логов](../lma-log-ingestion.md "Stream log data to Dynatrace.").
* Вы используете OpenPipeline.
* У вас есть необходимые разрешения для настройки пользовательского оповещения в приложении [Anomaly Detection](../../../dynatrace-intelligence/anomaly-detection/anomaly-detection-app.md "Explore anomaly detection configurations using the Anomaly Detection app.").

## Шаги

В этом примере мы откроем новую проблему Davis, когда определённые записи, содержащие конкретную фразу, загружаются и превышают статическое пороговое значение.

1. Найдите логи, по которым вы хотите запускать оповещения

Вы можете найти логи, открыв ![Logs](https://dt-cdn.net/images/logs-256-ae0a9ca67f.png "Logs") **Logs** и используя следующий запрос DQL.

```
fetch logs


| filter matchesPhrase(content, "Dropping data because sending_queue is full")


| sort timestamp desc
```

Если ваш запрос DQL использует `parse`, `fieldAdd` или другие преобразования, вам следует добавить правило обработки для установки этих полей при загрузке.

2. Извлеките метрику в OpenPipeline

Добавьте конфигурацию извлечения метрик в OpenPipeline.

1. Откройте ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Logs** и выберите вкладку **Pipelines**.
2. Найдите конвейер, который вы хотите изменить, или добавьте новый конвейер.
3. Выберите  >  **Edit**.
   Откроется страница конфигурации конвейера.
4. Выберите вкладку **Metric extraction**.
5. Установите

   * Имя и идентификатор метрики.
   * [DQL-матчер](../../../platform/openpipeline/reference/dql-matcher-in-openpipeline.md "Examine specific DQL functions and logical operators for log processing.").
     Матчер задаёт условие для события, которое должно быть извлечено.
     Это подмножество условий фильтрации в одном выражении DQL.

     В поле **Matching condition** используйте матчер, как показано ниже.

     ```
     matchesPhrase(content, "Dropping data because sending_queue is full")
     ```

Если вы используете сегменты или ваши разрешения установлены на уровне записи, вам следует включить эти условия в матчер.

Бывают ситуации, когда матчер не может быть легко извлечён из выражения DQL.
В таких случаях вы можете [создать оповещения логов для события или сводки данных логов](../../../dynatrace-intelligence/use-cases/create-alert-in-logs.md "Create log alerts for a specific log event or summary of log data").

3. Добавьте измерения.
   Для большинства логов вы можете добавить автоматическую корреляцию с сущностями в анализе первопричин Dynatrace Intelligence.
   Для этого добавьте измерение `dt.source_entity` или любое другое поле, содержащее идентификатор сущности.

3. Настройте пользовательское оповещение

Перейдите в ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** и создайте новое пользовательское оповещение.

В этом разделе описывается, как создать простое пользовательское оповещение.

Если вам нужно задать дополнительные расширенные свойства и точно настроить оповещение, используйте режим **Advanced**.

1. Установите область действия для вашего оповещения.
2. Используйте синтаксис DQL, чтобы указать созданную вами метрику.
   Чтобы привязать оповещение к отслеживаемой сущности, обязательно добавьте `by: {dt.source_entity}`.
3. Определите условия оповещения, при которых будет сгенерировано новое событие Davis.
   Вы можете выбрать различные анализаторы ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.

   * Используйте **Suggest values**, чтобы найти правильное пороговое значение.
   * Используйте **Preview**, чтобы получить оценку количества оповещений, которые были бы сгенерированы за последние два часа.
4. Наконец, установите детали события, такие как заголовок и описание.

4. Открытие проблемы

Когда условия оповещения выполняются, вы увидите новую проблему в ![Problems app - new](https://dt-cdn.net/images/dynatrace-davis-new-256-340162f8c6.webp "Problems app - new") **Problems**.

## Заключение

Вот когда следует использовать пользовательское оповещение с метриками на основе логов:

* Вам нужно установить пороговые значения или использовать другие анализаторы машинного обучения для запуска оповещений.
* Когда вы хотите получать оповещения об аномалиях в значениях, поступающих из поля лога, например `http.response_time`.
* Анализаторы метрик срабатывают каждую минуту, поэтому это не метод оповещения в реальном времени.
* Измерения метрик имеют низкую кардинальность.

Обнаруженные аномалии могут запускать автоматизации с помощью простых рабочих процессов, как описано в разделе [Создание простого рабочего процесса в Dynatrace Workflows](../../workflows/simple-workflow.md "Build and run a simple workflow.").

## Связанные темы

* [Настройка оповещений на основе событий, извлечённых из логов](lma-alert-log-based-events.md "How to create and configure Davis problems and alerts with events based on logs.")
* [Метрики логов (Logs Classic)](../../log-monitoring/analyze-log-data/log-metrics.md "Learn how to create and use Dynatrace log metrics to analyze log data.")
* [События логов (Logs Classic)](../../log-monitoring/analyze-log-data/log-events.md "Learn how to create and use Dynatrace log events to analyze log data.")
* [Оповещения и уведомления](../../alerting-and-notifications.md "Utilize anomaly detection, problem detection, and workflows for external notifications to ensure that critical problems never go unnoticed.")
