---
title: Расчёт потребления Mainframe Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/mainframe
scraped: 2026-05-12T11:06:22.190749
---

# Расчёт потребления Mainframe Monitoring (DPS)

# Расчёт потребления Mainframe Monitoring (DPS)

* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace Mainframe Monitoring обеспечивает автоматический сквозной мониторинг производительности приложений для транзакций, регионов и приложений, развёрнутых на IBM z/OS.
Включает распределённую трассировку, метрики, топологию и анализ на уровне кода для [30+ поддерживаемых технологий](/managed/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.").

DPS-возможности Mainframe Monitoring предоставляют:

* гибкость лицензирования для постепенного расширения мониторинга (например, начать с небольшого масштаба и постепенно увеличивать охват);
* оплату только за активный период мониторинга (например, время простоя не тарифицируется);
* прозрачность затрат и управление бюджетом в Account Management;
* использование ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** и **Services** включено в Dynatrace — запросы этих приложений не потребляют дополнительный ресурс.

Технические предварительные требования для DPS:

* Dynatrace Cluster версии 1.279+
* Модуль [zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.") версии 1.265+
* Подсистема [zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).") версии 1.247+

Мониторируемый логический раздел (LPAR) представлен в Dynatrace как хост.
Тарификация мониторинга LPAR зависит от значения Million Service Unit (MSU) раздела и длительности мониторинга Dynatrace.
MSU — это единица измерения IBM, отражающая объём вычислительной работы, который IBM Z mainframe может выполнить за один час.

### MSU-часы

Единица измерения для Mainframe Monitoring — MSU-час.
Потребление MSU-часов в Mainframe Monitoring рассчитывается на основе решения [IBM Tailored Fit Pricing](https://www.ibm.com/support/z-content-solutions/tailored-fit-pricing/), получаемого на LPAR из [записей SMF типа 70 подтипа 1](https://www.ibm.com/docs/en/zos/2.5.0?topic=conditions-cpu-activity-smf-record-type-70-1) (фактическое количество потреблённых MSU).

Чем больше MSU у LPAR и чем дольше его мониторирует Dynatrace, тем выше потребление MSU-часов.

### Детализация тарификации потребления MSU-часов

Детализация тарификации потребления MSU-часов рассчитывается в четырёх 15-минутных интервалах в час.
Если LPAR мониторируется менее 15 минут в интервале, потребление MSU-часов округляется до 15 минут перед расчётом.
Сумма MSU-часов всех мониторируемых LPAR составляет общее потребление.

### Распределённая трассировка

Mainframe Monitoring включает [распределённую трассировку](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.").

### Метрики

Mainframe Monitoring включает мониторинг производительности приложений и связанные встроенные метрики.
Например, [пользовательские метрики JMX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.") потребляют точки данных метрик.

## Детали потребления: Mainframe

Dynatrace предоставляет метрику использования, помогающую понять и анализировать потребление MSU-часов.
Чтобы использовать эту метрику, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите ключ или название метрики в поле **Search**.

Кроме того, эту метрику можно запросить через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

(DPS) Mainframe Monitoring billing usage
:   Ключ: `builtin:billing.mainframe_monitoring.usage`

    Измерение: Хост (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: Общее число MSU-часов под мониторингом, подсчитанных в 15-минутных интервалах.

Можно детализировать потребление MSU-часов по LPAR.
Пример ниже показывает все LPAR, участвовавшие в потреблении, в 1-часовых интервалах за последние 24 часа.

![DPS Mainframe Monitoring billing metric](https://dt-cdn.net/images/billing-metric-1559-0f648884c8.png)

DPS Mainframe Monitoring billing metric

Метрику использования можно также просмотреть в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Mainframe Monitoring**.

![MSU Usage Summary](https://dt-cdn.net/images/msu-usage-summary-1505-3ab6abffd5.png)

MSU Usage Summary

## Оценка потребления: Mainframe

Для оценки необходимого потребления MSU-часов в год используйте [отчёт IBM Sub-Capacity Reporting Tool (SCRT)](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting).

1. В разделе **C5** проверьте **Reporting Period** отчёта SCRT. Обычно он содержит данные за один месяц.
2. В разделе **N7** суммируйте значение **Total MSU Consumed** для каждого LPAR, который планируется мониторировать.
3. Если период отчёта равен одному месяцу, умножьте **Total MSU Consumed** на 12 месяцев для получения годового потребления.

![SCRT report example](https://dt-cdn.net/images/scrt-report-example-936-7ea2942e4f.png)

SCRT report example

В этом примере три LPAR (S1LP01, S2LP02 и TF1LP1) потребили 99 000 MSU-часов в сентябре 2023 года.

Умножение на 12 месяцев даёт 1 188 000 MSU-часов в год.

Примечания:

* Этот подход может не учитывать сезонные колебания нагрузки, что может приводить к отклонениям фактического потребления.
* Раздел **N7** доступен начиная с версии IBM SCRT 25.2, выпущенной IBM в декабре 2017 года.

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)