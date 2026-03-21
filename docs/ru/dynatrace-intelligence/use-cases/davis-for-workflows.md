---
title: AI в Workflows - Прогностическое обслуживание облачных дисков
source: https://www.dynatrace.com/docs/dynatrace-intelligence/use-cases/davis-for-workflows
scraped: 2026-03-03T21:23:38.569179
---

# ИИ в Workflows — Предиктивное обслуживание облачных дисков


* Latest Dynatrace
* Учебное руководство

Анализаторы данных Dynatrace Intelligence предлагают широкий спектр универсальных функций искусственного интеллекта и машинного обучения (ИИ/МО), таких как обучение и прогнозирование временных рядов, обнаружение аномалий или выявление изменений в поведении метрик во временных рядах. Dynatrace Intelligence позволяет бесшовно интегрировать эти анализаторы в ваши пользовательские рабочие процессы. Пример использования — полностью автоматизированная задача прогнозирования и устранения будущих потребностей в ёмкости. Она помогает избежать критических сбоев, уведомляя вас за несколько дней до возникновения инцидентов.

## Установка Dynatrace Intelligence (Preview)

Для использования действий Dynatrace Intelligence сначала необходимо установить **Dynatrace Intelligence (Preview)** из Dynatrace Hub.

1. В Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") найдите **Dynatrace Intelligence (Preview)**.
2. Выберите **Dynatrace Intelligence (Preview)** и нажмите **Install**.

После установки действия Dynatrace Intelligence автоматически появятся в разделе **Choose action** приложения [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.").

## Пример использования

Этот сценарий использования демонстрирует, как можно использовать предиктивный ИИ-анализатор Dynatrace Intelligence для прогнозирования будущих потребностей в дисковой ёмкости и генерации предиктивных оповещений за несколько недель до наступления критических инцидентов.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

Предоставление необходимых разрешений](davis-for-workflows.md#permissions "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

Изучение показателей ёмкости](davis-for-workflows.md#explore "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

Определение расписания запуска](davis-for-workflows.md#schedule "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")[![Шаг 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Шаг 4")

Настройка прогноза](davis-for-workflows.md#forecast "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")[![Шаг 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Шаг 5")

Оценка результата](davis-for-workflows.md#evaluate "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")[![Шаг 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Шаг 6")

Устранение до возникновения проблемы](davis-for-workflows.md#remediate "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")[![Шаг 7](https://dt-cdn.net/images/step-7-35139ef2d6.svg "Шаг 7")

Просмотр созданных проблем](davis-for-workflows.md#problems "Автоматизация предиктивного обслуживания облачных ресурсов с помощью Dynatrace Intelligence в AutomationEngine.")

### Шаг 1. Предоставление необходимых разрешений

Для успешного анализа Dynatrace Intelligence требуются соответствующие права доступа.

1. В ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** перейдите в **Settings** > **Authorization settings**.
2. Предоставьте следующее основное разрешение.

   ```
   app-engine:functions:run
   ```
3. Предоставьте следующие дополнительные разрешения.

   ```
   davis:analyzers:read


   davis:analyzers:execute


   storage:bizevents:read


   storage:buckets:read


   storage:events:read


   storage:logs:read


   storage:metrics:read


   storage:spans:read


   storage:system:read
   ```
4. В правом верхнем углу нажмите **Save**.

### Шаг 2. Изучение показателей ёмкости в Notebook

Предиктивное управление ёмкостью начинается в [**Notebooks**](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве."), где необходимо настроить показатели ёмкости. На изображении ниже показан пример индикатора процента свободного дискового пространства для операционной команды.

![Пример прогноза анализа данных ИИ.](https://dt-cdn.net/images/notebooks-data-analyzer-forecast-1891-28bee08431.png)

Когда у вас есть необходимые индикаторы, пора построить рабочий процесс, который запускает прогноз через регулярные интервалы.

### Шаг 3. Определение расписания запуска

В ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows** настройте необходимое расписание для запуска прогноза. Чтобы узнать, как это сделать, см. [Триггер расписания рабочего процесса](../../analyze-explore-automate/workflows/trigger/schedules.md "Руководство по созданию триггеров расписания для автоматизации рабочих процессов в Dynatrace Workflows."). На изображении ниже показан рабочий процесс, который запускается в 8:00 для прогнозирования всех дисков, которые с высокой вероятностью исчерпают свободное пространство в течение следующей недели.

![Пример триггера Dynatrace Intelligence в приложении Workflows.](https://dt-cdn.net/images/workflows-forecast-trigger-1920-652d16e024.png)

### Шаг 4. Настройка прогноза

Для запуска прогноза из рабочего процесса необходимо действие **Analyze data**. Действие использует прогнозный анализ и набор данных для прогноза. Вы можете использовать любые данные временных рядов для прогноза. Всё, что нужно — это получить их из Grail с помощью DQL-запроса. Здесь мы определяем набор дисков, для которых хотим спрогнозировать ёмкость. Мы используем метрику `dt.host.disk.free`, но вы можете использовать любую метрику ёмкости — ЦП хоста, память, сетевую нагрузку. Вы даже можете извлечь значение из строки лога.

Наш прогноз обучается на относительном временном диапазоне за последние семь дней, указанном в DQL-запросе. Он предсказывает 100 точек данных; то есть исходные 120 точек, полученных из Grail, расширяются прогнозируемыми 100 точками данных, охватывающими приблизительно одну неделю в будущее. См. DQL-запрос ниже.

Действие возвращает все спрогнозированные временные ряды, которых может быть сотни или тысячи отдельных прогнозов по дискам.

Для настройки прогноза в действии

1. Добавьте новое действие **Analyze data**.
2. Задайте имя действия как `predict_disk_capacity`.
3. Выберите **Generic Forecast Analysis** в качестве анализатора.
4. В поле **Time series data** укажите следующий DQL-запрос:

   ```
   timeseries avg(dt.host.disk.free), by:{dt.entity.host, dt.entity.disk}, bins: 120, from:now()-7d, to:now()
   ```
5. Установите **Data points to predict** равным `100`.

![Прогноз Dynatrace Intelligence для рабочих процессов в приложении Workflows.](https://dt-cdn.net/images/dynatrace-intelligence-forecast-for-workflows-1920-de2e97e37b.png)

### Шаг 5. Оценка результата

Следующее действие рабочего процесса проверяет каждый прогноз, чтобы определить, исчерпает ли диск свободное пространство в течение следующей недели. Это действие **Run JavaScript**, выполняющее пользовательский TypeScript-код, проверяющий нарушения порогов и передающий все нарушения следующему действию. Оно возвращает пользовательский объект с булевым флагом (`violation`) и массивом, содержащим подробности нарушений (`violations`).

1. Добавьте новое действие **Run JavaScript**.
2. Задайте имя действия как `check_prediction`.
3. Используйте следующий исходный код.

   ```
   import { execution } from '@dynatrace-sdk/automation-utils';


   const THRESHOLD = 15;


   const TASK_ID = 'predict_disk_capacity';


   export default async function () {


   const exe = await execution();


   const predResult = await exe.result(TASK_ID);


   const result = predResult['result'];


   const predictionSummary = { violation: false, violations: new Array<Record<string, string>>() };


   console.log("Total number of predicted lines: " + result.output.length);


   // Check if prediction was successful.


   if (result && result.executionStatus == 'COMPLETED') {


   console.log('Prediction was successful.')


   // Check each predicted result, if it violates the threshold.


   for (let i = 0; i < result.output.length; i++) {


   const prediction = result.output[i];


   // Check if the prediction result is considered valid


   if (prediction.analysisStatus == 'OK' && prediction.forecastQualityAssessment == 'VALID') {


   const lowerPredictions = prediction.timeSeriesDataWithPredictions.records[0]['dt.davis.forecast:lower'];


   const lastValue = lowerPredictions[lowerPredictions.length-1];


   // check against the threshold


   if (lastValue < THRESHOLD) {


   predictionSummary.violation = true;


   // we need to remember all metric properties in the result,


   // to inform the next actions which disk ran out of space


   predictionSummary.violations.push(prediction.timeSeriesDataWithPredictions.records[0]);


   }


   }


   }


   console.log(predictionSummary.violations.length == 0 ? 'No violations found :)' : '' + predictionSummary.violations.length + ' capacity shortages were found!')


   return predictionSummary;


   } else {


   console.log('Prediction run failed!');


   }


   }
   ```

### Шаг 6. Устранение до возникновения проблемы

У вас есть множество вариантов действий по устранению прогнозируемого дефицита ёмкости. В нашем примере рабочий процесс создаёт проблему Davis и отправляет сообщение в Slack для каждого потенциального дефицита. Оба действия являются условными и срабатывают только если прогноз предсказывает нехватку дискового пространства.

Каждая созданная проблема Davis содержит пользовательские свойства, которые дают представление о ситуации и помогают идентифицировать проблемный диск.

![Пример условного действия Dynatrace Intelligence.](https://dt-cdn.net/images/workflows-forecast-conditional-action-1920-8dbefdfc44.png)

Для отправки сообщения

1. Добавьте новое действие **Send message**.
2. Задайте имя действия как `send_message`.
3. Настройте сообщение. Чтобы узнать, как это сделать, см. [Коннектор Slack](../../analyze-explore-automate/workflows/actions/slack.md "Отправка сообщений в рабочие пространства Slack").
4. Откройте вкладку **Conditions**.
5. Выберите условие `success` для действия **check\_prediction**.
6. Добавьте следующее пользовательское условие:

   ```
   {{ result('check_prediction').violation }}
   ```

Для создания проблемы Davis

1. Добавьте новое действие **Run JavaScript**.
2. Задайте имя действия как `raise_violation_events`.
3. Используйте следующий исходный код.

   ```
   import { eventsClient, EventIngestEventType } from "@dynatrace-sdk/client-classic-environment-v2";


   import { execution } from '@dynatrace-sdk/automation-utils';


   export default async function () {


   const exe = await execution();


   const checkResult = await exe.result('check_prediction');


   const violations = await checkResult.violations;


   // Raise an event for each violation


   violations.forEach(function (violation) {


   eventsClient.createEvent({


   body : {


   eventType: EventIngestEventType.ResourceContentionEvent,


   title: 'Predicted Disk Capacity Alarm',


   entitySelector: 'type(DISK),entityId("' + violation['dt.entity.disk'] + '")',


   properties: {


   'dt.entity.host' : violation['dt.entity.host']


   }


   }


   });


   });


   };
   ```
4. Откройте вкладку **Conditions**.
5. Выберите условие `success` для действия **check\_prediction**.
6. Добавьте следующее пользовательское условие.

   ```
   {{ result('check_prediction').violation }}
   ```

### Шаг 7. Просмотр всех проблем прогнозируемой ёмкости Dynatrace Intelligence

В Dynatrace операционная команда может просмотреть все прогнозируемые дефициты ёмкости в ленте проблем Dynatrace Intelligence.

Создание проблемы — это необязательный шаг устранения, который можно полностью пропустить, ограничившись уведомлениями ответственных команд. В данном примере он иллюстрирует гибкость и мощь AutomationEngine в сочетании с аналитическими возможностями Dynatrace Intelligence и Grail.

![Пример предиктивного прогнозирования ёмкости и предиктивных оповещений Dynatrace Intelligence.](https://dt-cdn.net/images/problems-predictive-capacity-alert-3600-89a8dfa6a9.png)

## Связанные темы

* [Workflows](../../analyze-explore-automate/workflows.md "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.")
* [Notebooks](../../analyze-explore-automate/dashboards-and-notebooks/notebooks.md "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном настраиваемом рабочем пространстве.")
