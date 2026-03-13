---
title: Calculate your consumption of Mainframe Monitoring (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/mainframe
scraped: 2026-03-06T21:19:44.937750
---

# Расчёт потребления Mainframe Monitoring (DPS)

# Расчёт потребления Mainframe Monitoring (DPS)

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace Mainframe Monitoring обеспечивает автоматический сквозной мониторинг производительности приложений для транзакций, регионов и приложений, развёрнутых на IBM z/OS.
Он включает распределённую трассировку, метрики, топологию и анализ на уровне кода для [более чем 30 поддерживаемых технологий](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.").

С возможностью DPS для Mainframe Monitoring:

* Вы получаете гибкость лицензирования для поэтапного внедрения мониторинга (например, можно начать с малого и расширять покрытие со временем).
* Вы платите только за период активного мониторинга (например, простои не тарифицируются).
* Вы получаете прозрачность затрат и управление бюджетом в Account Management.
* Использование ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** и ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** включено в Dynatrace.
  Эти приложения не генерируют потребление запросов.

Технические предварительные требования для DPS:

* Dynatrace Cluster версии 1.279+
* Модуль [zRemote](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.") версии 1.265+
* Подсистема [zDC](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).") версии 1.247+

Мониторируемый логический раздел (LPAR) представляется как хост в Dynatrace.
Стоимость мониторинга LPAR зависит от значения Million Service Unit (MSU) раздела и продолжительности мониторинга Dynatrace.
MSU -- это единица измерения IBM для объёма вычислительной работы, которую мейнфрейм IBM Z может выполнить за один час.

### MSU-часы

Единицей измерения для Mainframe Monitoring является MSU-час.
Потребление Mainframe Monitoring рассчитывает MSU-часы на основе решения [IBM Tailored Fit Pricing](https://www.ibm.com/support/z-content-solutions/tailored-fit-pricing/) для учёта потребления программного обеспечения, получаемого по каждому LPAR из [записей SMF type 70 subtype 1](https://www.ibm.com/docs/en/zos/2.5.0?topic=conditions-cpu-activity-smf-record-type-70-1) (фактическое количество потреблённых MSU).

Чем больше MSU у LPAR и чем дольше Dynatrace его мониторит, тем выше потребление MSU-часов.

### Детализация тарификации для потребления MSU-часов

Детализация тарификации для потребления MSU-часов рассчитывается в четырёх 15-минутных интервалах в час.
Если LPAR мониторится менее 15 минут в интервале, потребление MSU-часов округляется до 15 минут перед расчётом.
Сумма MSU-часов всех мониторируемых LPAR представляет общее потребление.

### Распределённая трассировка

### Включённое и расширенное хранение трассировок

Dynatrace [хранит общий объём принятых трассировок](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.") из вашей среды в течение 10 дней.

Dynatrace предоставляет возможность выборочного продления хранения трассировок на срок до 10 лет.
Это достигается путём [создания пользовательских бакетов](/docs/platform/grail/organize-data "Insights on the Grail data model consisting of buckets, tables, and views.") в Grail.
Первые 10 дней хранения всегда включены.
Любые данные трассировок, хранящиеся дольше 10 дней, тарифицируются на основе гибибайт как [Trace Retain](/docs/license/capabilities/traces#trace-retain-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

### Метрики

Mainframe Monitoring включает мониторинг производительности приложений и связанные встроенные метрики, за исключением пользовательских метрик, которые измеряются в точках данных метрик и тарифицируются как [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").
Например, [пользовательские JMX-метрики](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.") потребляют точки данных метрик.

Как тарифицируются метрики в DPS до появления Metrics powered by Grail

Если [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") отсутствует в вашем тарифном плане, точки данных метрик тарифицируются как [Custom Metrics Classic](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

## Детали потребления: Mainframe

Dynatrace предоставляет метрику использования, которая помогает понять и проанализировать потребление MSU-часов.
Для использования этой метрики в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите следующий ключ или название метрики в поле **Search**.

Кроме того, вы можете запрашивать эту метрику через [Environment API - Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

(DPS) Mainframe Monitoring billing usage
:   Key: `builtin:billing.mainframe_monitoring.usage`

    Dimension: Host (`dt.entity.host`)

    Resolution: 15 min

    Description: Общее количество мониторируемых MSU-часов, подсчитываемых в 15-минутных интервалах.

Вы можете детализировать потребление MSU-часов по каждому LPAR.
Пример ниже показывает все LPAR, которые внесли вклад в потребление за 1-часовые интервалы в течение последних 24 часов.

![DPS Mainframe Monitoring billing metric](https://dt-cdn.net/images/billing-metric-1559-0f648884c8.png)

Вы также можете просматривать метрику использования в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Mainframe Monitoring**.

![MSU Usage Summary](https://dt-cdn.net/images/msu-usage-summary-1505-3ab6abffd5.png)

## Оценка потребления: Mainframe

Используйте [отчёт IBM Sub-Capacity Reporting Tool (SCRT)](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting) для оценки требуемого потребления MSU-часов в год.

1. В разделе **C5** проверьте **Reporting Period** отчёта SCRT.
   Как правило, он содержит данные за один месяц.
2. В разделе **N7** суммируйте значение **Total MSU Consumed** для каждого мониторируемого LPAR.
3. Если отчётный период составляет один месяц, умножьте **Total MSU Consumed** на 12 месяцев для получения годового потребления.

![SCRT report example](https://dt-cdn.net/images/scrt-report-example-936-7ea2942e4f.png)

В этом примере три LPAR (S1LP01, S2LP02 и TF1LP1) потребили 99 000 MSU-часов в сентябре 2023 года.

Умноженное на 12 месяцев, это составляет 1 188 000 MSU-часов в год.

Примечания:

* Этот подход может не учитывать сезонные колебания нагрузки, что может привести к отклонениям в фактическом потреблении.
* Раздел **N7** доступен начиная с версии IBM SCRT 25.2.
  Он был выпущен IBM в декабре 2017 года.

Мониторы сетевой доступности (NAM) не имеют отдельной строки в тарифном плане Dynatrace. Вместо этого тарификация основана на [количестве точек данных метрик](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model."), генерируемых при каждом выполнении теста NAM. Для получения дополнительной информации обратитесь к вашему менеджеру по работе с клиентами Dynatrace.

Расчёт точек данных метрик

Следующие детали относятся к точкам данных метрик:

* Точки данных метрик, связанные с выполнением монитора и шага, не тарифицируются.
* Только потребление метрик, создаваемых на уровне запроса, влияет на вашу тарификацию.
* Каждое выполнение запроса в тестах ping генерирует 6 точек данных метрик.

  + Количество пакетов, используемых в тесте ping, не влияет на количество создаваемых метрик или вашу тарификацию.
  + Количество пакетов не влияет на цену.
* Каждое выполнение запроса в тестах TCP/DNS генерирует 3 точки данных метрик.
* Цена остаётся одинаковой вне зависимости от того, создаёте ли вы несколько тестов с одним запросом или один тест с множеством запросов для одного и того же набора хостов или устройств.

## Связанные темы

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Обзор Application & Infrastructure Observability (DPS)](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Тарификация Dynatrace](https://www.dynatrace.com/pricing/)
