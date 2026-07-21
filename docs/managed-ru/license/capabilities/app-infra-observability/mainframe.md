---
title: Как понять и управлять потреблением Mainframe Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/mainframe
---

# Как понять и управлять потреблением Mainframe Monitoring (DPS)

# Как понять и управлять потреблением Mainframe Monitoring (DPS)

* Пояснение
* 1 минута на чтение
* Обновлено 10 дек. 2025 г.

Dynatrace Mainframe Monitoring обеспечивает автоматический сквозной мониторинг производительности приложений для транзакций, регионов и приложений, развёрнутых на IBM z/OS.
Он включает распределённую трассировку, метрики, топологию и анализ на уровне кода для [более 30 поддерживаемых технологий](/managed/ingest-from/technology-support/mainframe-technology-support "Узнать, какие технологии поддерживает Dynatrace для мониторинга Mainframe.").

С возможностью DPS для Mainframe Monitoring:

* Появляется гибкость лицензирования для поэтапного развёртывания мониторинга (например, можно начать с малого и постепенно расширять охват).
* Оплата взимается только за период активного мониторинга (например, простои не тарифицируются).
* Появляется прозрачность затрат и управление бюджетом в Account Management.
* Использование ![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing** и **Services** включено в Dynatrace.
  Эти приложения не создают расход запросов.

Технические предварительные условия для DPS:

* Dynatrace Cluster версии 1.279+
* [модуль zRemote](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовить и установить zRemote для мониторинга z/OS.") версии 1.265+
* [подсистема zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Настроить подсистему сбора данных z/OS (zDC).") версии 1.247+

Отслеживаемый логический раздел (Logical Partition, LPAR) представлен в Dynatrace как хост.
Тарификация мониторинга LPAR зависит от значения Million Service Unit (MSU) раздела и продолжительности мониторинга Dynatrace.
MSU, это единица измерения IBM объёма вычислительной работы, которую мейнфрейм IBM Z может выполнить за один час.

### Часы MSU

Единица измерения для Mainframe Monitoring, это час MSU.
Потребление Mainframe Monitoring рассчитывает часы MSU на основе решения по учёту потребления ПО [IBM Tailored Fit Pricing﻿](https://www.ibm.com/support/z-content-solutions/tailored-fit-pricing/), получаемого по каждому LPAR из [записей SMF типа 70, подтипа 1﻿](https://www.ibm.com/docs/en/zos/2.5.0?topic=conditions-cpu-activity-smf-record-type-70-1) (фактическое количество потреблённых MSU).

Чем больше MSU у LPAR и чем дольше Dynatrace его отслеживает, тем выше потребление в MSU-часах.

### Гранулярность тарификации потребления MSU-часов

Гранулярность тарификации потребления MSU-часов рассчитывается по четырём 15-минутным интервалам в час.
Если LPAR отслеживается менее 15 минут в интервале, потребление MSU-часов округляется до 15 минут перед расчётом потребления.
Сумма MSU-часов всех отслеживаемых LPAR составляет общее потребление.

### Распределённая трассировка

Mainframe Monitoring включает [распределённую трассировку](/managed/observe/application-observability/distributed-traces "Получить наблюдаемость высокораспределённых, облачно-нативных архитектур для эффективной трассировки и анализа транзакций в реальном времени.").

### Метрики

Mainframe Monitoring включает мониторинг производительности приложений и связанные встроенные метрики.
Например, [пользовательские метрики JMX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Узнать, как настроить мониторинг метрик JMX для приложений Java на z/OS.") расходуют точки данных метрик.

## Детали потребления: Mainframe

Dynatrace предоставляет метрику использования, которая помогает понять и проанализировать потребление MSU-часов.
Чтобы использовать эту метрику, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите следующий ключ или имя метрики в поле **Search**.

Также эту метрику можно запросить через [Environment API - Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получить информацию о метриках через Metrics v2 API.").

(DPS) Mainframe Monitoring billing usage
:   Ключ: `builtin:billing.mainframe_monitoring.usage`

    Измерение: Host (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: Общее количество отслеженных MSU-часов, подсчитанное в 15-минутных интервалах.

Потребление MSU-часов можно разложить по каждому LPAR.
В примере ниже показаны все LPAR, которые внесли вклад в потребление, в часовых интервалах за последние 24 часа.

![DPS Mainframe Monitoring billing metric](https://dt-cdn.net/images/billing-metric-1559-0f648884c8.png)

Метрика тарификации DPS Mainframe Monitoring

Метрику использования также можно посмотреть в Account Management.
Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выбрать возможность **Mainframe Monitoring**.

![MSU Usage Summary](https://dt-cdn.net/images/msu-usage-summary-1505-3ab6abffd5.png)

Сводка использования MSU

## Оценка потребления: Mainframe

Чтобы оценить требуемое годовое потребление MSU-часов, использовать отчёт [IBM Sub-Capacity Reporting Tool (SCRT)﻿](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting).

1. В разделе **C5** проверить **Reporting Period** отчёта SCRT.
   Обычно он содержит данные за один месяц.
2. В разделе **N7** сложить значение **Total MSU Consumed** для каждого отслеживаемого LPAR.
3. Если отчётный период составляет один месяц, умножить **Total MSU Consumed** на 12 месяцев, чтобы получить годовое потребление.

![SCRT report example](https://dt-cdn.net/images/scrt-report-example-936-7ea2942e4f.png)

Пример отчёта SCRT

В этом примере три LPAR (S1LP01, S2LP02 и TF1LP1) потребили 99 000 MSU-часов в сентябре 2023 года.

Умноженное на 12 месяцев, это составляет 1 188 000 MSU-часов в год.

Примечания:

* Такой подход может не учитывать сезонные колебания нагрузки, что может приводить к отклонениям в фактическом потреблении.
* Раздел **N7** доступен начиная с IBM SCRT версии 25.2.
  IBM выпустила её в декабре 2017 года.

Мониторы Network availability monitoring (NAM) не имеют отдельной строки в прайс-листе Dynatrace. Вместо этого тарификация основана на [количестве точек данных метрик](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."), создаваемых при каждом выполнении теста NAM. За дополнительной информацией обратиться к менеджеру по работе с клиентами Dynatrace.

Расчёт точек данных метрик

Для точек данных метрик применяются следующие детали:

* Точки данных метрик, связанные с выполнением монитора и шага, не тарифицируются.
* На тарификацию влияет только потребление метрик, создаваемых на уровне запроса.
* Каждое выполнение запроса в ping-тестах создаёт 6 точек данных метрик.

  + Количество пакетов, используемых в ping-тесте, не влияет на количество создаваемых метрик или на тарификацию.
  + Количество пакетов не влияет на цену.
* Каждое выполнение запроса в TCP/DNS-тестах создаёт 3 точки данных метрик.
* Цена остаётся одинаковой независимо от того, создаётся ли несколько тестов с одним запросом в каждом, или один тест с многочисленными запросами для одного и того же набора хостов или устройств.

## Похожие темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Узнать о важных концепциях, связанных с OneAgent, а также как устанавливать и эксплуатировать OneAgent на разных платформах.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Узнать о разных вариантах Application & Infrastructure Observability, доступных с лицензией Dynatrace Platform Subscription (DPS).")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)