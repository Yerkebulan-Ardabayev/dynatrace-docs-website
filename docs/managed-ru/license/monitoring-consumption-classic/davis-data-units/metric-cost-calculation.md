---
title: DDU для метрик
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation
scraped: 2026-05-12T11:10:21.594339
---

# DDU для метрик

# DDU для метрик

* 17-min read
* Published Mar 30, 2021

На этой странице объясняется, как рассчитываются DDU для метрик, раскрывается концепция пользовательских метрик и описываются способы оценки и отслеживания потребления DDU для метрик.

## Какие типы метрик потребляют DDU?

* Пользовательские метрики
* Некоторые встроенные метрики (см. ниже)

## Что такое пользовательская метрика?

Пользовательские метрики — это метрики, которые вы определяете или устанавливаете. Они расширяют ценность возможностей мониторинга Dynatrace, позволяя интегрировать сторонние источники данных, вычислять пользовательские метрики, импортировать метрики через API, использовать расширения и многое другое.

Ниже приведён неполный список типов пользовательских метрик:

* Все [метрики, принятые через API](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")
* Расчётные метрики сервисов, пользовательские метрики DEM и [метрики логов](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.")
  + Например, расчётные метрики сервисов, созданные на основе атрибутов запроса
* Все метрики, предоставляемые вручную установленными [расширениями Dynatrace Monitoring](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.")

Полные сведения о настройке и приёме пользовательских метрик в Dynatrace см. в [Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.").

## Какие встроенные метрики потребляют DDU?

Метрики, потребляющие DDU, включают:

* Метрики, предоставляемые некоторыми [встроенными расширениями](/managed/ingest-from/extensions#out-of-the-box "Learn how to create and manage Dynatrace Extensions."), не включёнными по умолчанию
  + Переключатели в веб-интерфейсе Dynatrace для включения/отключения этих метрик помечены соответствующим образом.
* Все метрики, принятые расширениями Public Cloud ([AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics."), [Azure](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics "Monitor Azure services with Dynatrace and view available metrics.") и [Google Cloud](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace."))
  + Например, метрики, полученные из облачных сервисов.

## Как рассчитывается потребление DDU для метрик?

Потребление происходит при приёме точек данных метрик. Точка данных метрики — единичное измеренное значение, хранящееся в Dynatrace. Значение принадлежит метрике, идентифицируемой ключом метрики, и имеет временную метку. Метрика временного ряда — это серия таких точек данных, например загрузка CPU для заданного хоста за период анализа.

Каждая принятая точка данных вычитает 0,001 DDU из доступной квоты.

Метрики, предоставляемые Dynatrace, как правило, записываются раз в минуту. Это даёт следующее типичное годовое потребление DDU для одной метрики:

`1 точка данных × 60 мин × 24 ч × 365 дней × 0,001 = 525,6 DDU на метрику/год`

### Влияние измерений метрики на потребление DDU

Точки данных метрик могут иметь связанные измерения, идентифицируемые ключами и значениями измерений. Например, при использовании синтаксиса [протокола приёма метрик](/managed/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.") два значения могут быть приняты следующим образом:

```
my_cpu_utilization,hostname=hostA 55 1609459200000
my_cpu_utilization,hostname=hostB 45 1609459200000
```

Для одной временной метки (`1609459200000`) Dynatrace сохраняет два разных измеренных значения одной метрики на двух разных хостах, используя ключ измерения `hostname` со значениями `hostA` и `hostB`. Это удваивает количество принятых точек данных и соответствующее потребление DDU.

Если добавляются дополнительные измерения и количество точек данных увеличивается, потребление DDU также растёт:

```
my_cpu_utilization,hostname=hostA,cpu=1 55 1609459200000
my_cpu_utilization,hostname=hostA,cpu=2 11 1609459200000
my_cpu_utilization,hostname=hostB,cpu=1 45 1609459200000
my_cpu_utilization,hostname=hostB,cpu=2 45 1609459200000
```

В этом примере потребляется 0,004 DDU в минуту из-за двух хостов и двух CPU.

Однако увеличение потребления обусловлено не увеличением числа измерений, а увеличением числа принятых точек данных.

Если измерения добавляются, но число точек данных остаётся прежним, потребление DDU не меняется:

```
my_cpu_utilization,hostname=hostA,host_ip="127.0.0.23" 55 1609459200000
my_cpu_utilization,hostname=hostB,host_ip="127.0.0.42" 45 1609459200000
```

Эти принятые точки данных потребляют то же количество DDU, как если бы они были отправлены без измерения `host_ip`.

### Включённые метрики на хост-единицу

При мониторинге хостов с помощью OneAgent и потреблении хост-единиц вам предоставляется количество «включённых метрик для хостов» в соответствии с потреблением хост-единиц мониторируемых хостов. Точнее, для каждой данной минуты хост, потребляющий хост-единицы, имеет бюджет включённых точек данных метрик. Одна включённая метрика определяется как одна точка данных метрики в минуту.

На каждом мониторируемом хосте (в режиме Full-Stack Monitoring) включено 1 000 метрик на хост-единицу. Эти метрики включены в ваши хост-единицы Full-Stack и не потребляют DDU.

* Каждый хост с OneAgent в режиме Full-Stack Monitoring включает 1 000 метрик на хост-единицу (см. таблицу ниже).
* Хосты с OneAgent в режиме Infrastructure Monitoring всегда включают 200 метрик, не потребляющих DDU.
* Все метрики, превышающие включённые метрики хоста, будут потреблять DDU.
* Если все DDU в пуле метрик израсходованы, включённые метрики на хост-единицу также становятся недоступны.
* Расчётные метрики сервисов, пользовательские метрики DEM и метрики логов не учитываются в включённых метриках на хост-единицу.

Обратите внимание, что включённые метрики привязаны к конкретным хостам, мониторируемым через OneAgent. Это означает, что включаются только метрики, привязанные к мониторируемому хосту или процессу мониторируемого хоста. Это также включает метрики, привязанные к сущностям Amazon EC2, Azure VM и VMware (если эти VM мониторируются OneAgent).

| Размер хоста | Full-Stack режим | Full-Stack режим | Infrastructure режим | Infrastructure режим |
| --- | --- | --- | --- | --- |
| ОЗУ (GiB) | Хост-единицы | Включённые метрики | Хост-единицы | Включённые метрики |
| 1,6 GiB | 0,1 | 200 | 0,03 | 200 |
| 4 GiB | 0,25 | 250 | 0,075 | 200 |
| 8 GiB | 0,5 | 500 | 0,15 | 200 |
| 16 GiB | 1 | 1 000 | 0,3 | 200 |
| 32 GiB | 2 | 2 000 | 0,6 | 200 |
| 48 GiB | 3 | 3 000 | 0,9 | 200 |
| 64 GiB | 4 | 4 000 | 1,0 | 200 |
| N × 16 | N | N × 1 000 (минимум 200) | 1,0 | 200 |

### Пример влияния включённых метрик на потребление DDU

Рассмотрим следующий пример:

* Хост с 16 GiB ОЗУ — то есть 1 хост-единица
* Хост мониторируется через OneAgent в режиме Full-Stack

(1 хост-единица = 1 000 включённых метрик для хостов)

* 1 500 метрик из различных расширений и локального приёма через API (например, JMX и RabbitMQ) привязаны к этому хосту с OneAgent
* 300 метрик, передаваемых через публичный API, не связанных с хостом с OneAgent

В этом сценарии 1 000 метрик/мин включены через хост-единицу, и хост передаёт избыток из 500 метрик, которые будут потреблять DDU. 300 метрик, передаваемых через API и не связанных с хостом OneAgent, также будут потреблять DDU. Итого 800 метрик/мин потребляют DDU.

| Режим | Хост-единицы | Включённых метрик | Метрик на хост | Платные метрики | DDU/мин |
| --- | --- | --- | --- | --- | --- |
| Full-Stack | 0,5 | 500 | 300 | 0 | 0 |
| Full-Stack | 1 | 1 000 | 1 500 | 500 | 0,5 |
| Full-Stack | 1 | 1 000 | 500 | 0 | 0 |
| Full-Stack | 4 | 4 000 | 5 000 | 1 000 | 1 |
| Infrastructure | 0,6 | 200 | 150 | 0 | 0 |
| Infrastructure | 1 | 200 | 1 000 | 800 | 0,8 |

## Отчётные DDU vs. потреблённые DDU

Отчётные DDU определяются как все DDU до учёта включённых метрик. Потреблённые DDU отражают суммарные «тарифицируемые» DDU, вычитаемые из баланса DDU.

Для сравнения отчётных DDU для конкретного хоста с количеством включённых метрик можно создать диаграмму в [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights."), используя следующие метрики:

* `builtin:billing.ddu.includedMetricDduPerHost` — разбивка по ID хоста. Показывает включённые DDU для хоста.
* `builtin:billing.ddu.metrics.byEntityRaw` — разбивка по мониторируемой сущности. Отражает суммарные отчётные DDU до учёта включённых метрик.
* `builtin:billing.ddu.metrics.byEntity` — разбивка по мониторируемой сущности. Отражает суммарные потреблённые DDU (то есть всё потребление выше числа включённых метрик на хост-единицу).

### Рекомендации по работе с диаграммой

![Reported vs. consumed DDU](https://dt-cdn.net/images/ddus-replacement3-1280-61229267e2.png)

Отчётные vs. потреблённые DDU

* Поскольку тарификация DDU рассчитывается с минутной детализацией, рекомендуется работать с минутным разрешением в диаграмме.
* Использование **Split by** и **Filter by** позволяет выбрать конкретный интересующий хост.

## Как оценить необходимый объём DDU для метрик

Ограниченный приём и анализ метрик предоставляется «из коробки» в форме [включённых метрик на хост-единицу](#metrics-per-host-unit). Для организации дополнительного приёма и анализа метрик [обратитесь в отдел продаж Dynatrace](https://www.dynatrace.com/contact/).

## Как отслеживать потребление DDU для метрик

### Страница обзора Davis data units

Чтобы узнать, сколько DDU потреблено в вашей среде:

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.
   Необходимо разрешение **Manage monitoring settings** или учётная запись администратора.
2. На странице **Davis data units (DDU)**:
   * В таблице **Consumption by DDU pool** проверьте строку **Metrics**.
   * В разделе **DDU consumption details** проверьте вкладку **Metrics**.

### Настраиваемые дашборды для отслеживания потребления

Investigate your total DDU consumption from metrics (Анализ суммарного потребления DDU из метрик)

![DDU chart](https://dt-cdn.net/images/image009-1379-4d81b635cd.png)

DDU chart

Investigate metric consumption per monitored entity (Анализ потребления метрик по мониторируемой сущности)

![metric consumption per monitored entity](https://dt-cdn.net/images/ddus-replacement1-1280-d87fd073c0.png)

metric consumption per monitored entity

Investigate metric consumption per monitored metric entity (Анализ потребления метрик по ключу метрики)

![metric consumption per monitored metric entity](https://dt-cdn.net/images/ddus-replacement2-1280-aef478410b.png)

metric consumption per monitored metric entity

## Потребление «Not related to a monitored entity»

Источником этого потребления является одно из следующего:

* [Приём метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") для данных без измерения `dt.entity.host`
* Расчётные метрики из пользовательских сессий для [веб](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications."), [мобильных](/managed/observe/digital-experience/mobile-applications/additional-configuration/rum-calculated-metrics-mobile "Create calculated metrics as well as custom charts based on calculated metrics for your mobile applications.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/rum-calculated-metrics-custom "Create calculated metrics as well as custom charts based on calculated metrics for your custom applications.")
* [Расчётные метрики логов v2](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-metrics "Learn how to create and use Dynatrace log metrics to analyze log data.") — в разбивке по ключам метрик имеют префикс `log.`

## Часто задаваемые вопросы

Какие метрики потребляют DDU?

Все метрики, отправляемые стандартным OneAgent (например, метрики хостов), включены бесплатно и не потребляют DDU. Метрики, принятые расширением, привязанные к конкретным хостам или процессам, сначала потребляют все доступные включённые метрики, прежде чем начнут потреблять DDU.

| Тип метрики | Потребляет DDU | Включается в хост-единицу |
| --- | --- | --- |
| Встроенные расширения | Да | Да |
| REST API | Да | Да (если привязано к хосту) |
| JMX | Да | Да |
| Python | Да | Нет |
| Расчётные метрики сервисов | Да | Нет |
| Расчётные метрики логов | Да | Нет |
| Расчётные метрики DEM | Да | Нет |
| Метрики AWS | Да | Да (если привязано к хосту с OneAgent) |
| Метрики Azure | Да | Да (если привязано к хосту с OneAgent) |
| Метрики Google Cloud | Да | Да (если привязано к хосту с OneAgent) |
| Cloud Foundry | Нет | Нет |
| Метрики кластера Kubernetes | Нет | Нет |
| Метрики VMware | Нет | Нет |

Какова стоимость (вес) одной точки данных?

Каждая точка данных потребляет `0,001 DDU`.

Сколько DDU потребляет одна метрика с частотой 1 раз в минуту в год?

`1 точка данных × 60 мин × 24 часа × 365 дней × 0,001 веса DDU = 525,6 DDU`

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
* [Расширение наблюдаемости метрик](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")