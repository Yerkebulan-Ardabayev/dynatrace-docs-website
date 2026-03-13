---
title: Extend metric observability
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics
scraped: 2026-03-06T21:29:17.802394
---

# Расширение наблюдаемости метрик

# Расширение наблюдаемости метрик

* Последняя версия Dynatrace
* Чтение: 4 мин
* Опубликовано 4 февраля 2022 г.

Вы можете расширить данные, собираемые по умолчанию, данными, предоставляемыми следующими фреймворками и стандартами:

[![OpenTelemetry](https://dt-cdn.net/images/techn-icon-opentelemetry-345d0f8b0e.svg "OpenTelemetry")

### OpenTelemetry

Отправка метрик OpenTelemetry в Dynatrace](/docs/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.")[![Micrometer](https://dt-cdn.net/images/mircrometer-d91d5ac640.svg "Micrometer")

### Micrometer

Сбор метрик Micrometer из приложений JVM](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Узнайте, как отправлять метрики Micrometer в Dynatrace.")[![Prometheus](https://dt-cdn.net/images/prometheus-b1fab729ac.svg "Prometheus")

### Prometheus

Отправка метрик Prometheus в Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Узнайте, как расширить наблюдаемость в Dynatrace с помощью метрик Prometheus.")[![StatsD](https://dt-cdn.net/images/statsd-icon-bigger-800-72b34b3823.png "StatsD")

### StatsD

Отправка метрик StatsD в Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/statsd "Приём метрик в Dynatrace с использованием клиента StatsD через OneAgent и ActiveGate.")[![Telegraf](https://dt-cdn.net/images/techn-icon-telegraf-ba9e70e8d6.svg "Telegraf")

### Telegraf

Отправка метрик Telegraf в Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/telegraf "Приём метрик Telegraf в Dynatrace.")[### Oracle Database

Расширение наблюдаемости приложений за счёт данных, получаемых непосредственно из слоя Oracle Database.](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/oraclesql "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик, получаемых из Oracle Database.")[![Microsoft SQL Server](https://dt-cdn.net/images/techn-icon-microsoft-sqlserver-60740bd3fa.svg "Microsoft SQL Server")

### Microsoft SQL Server Database

Расширение наблюдаемости приложений за счёт данных, получаемых непосредственно из слоя Microsoft SQL Server.](/docs/ingest-from/extensions/supported-extensions/data-sources/sql/microsoft-sql "Расширение наблюдаемости в Dynatrace с помощью декларативных метрик, получаемых из Microsoft SQL Server.")[![SNMP](https://dt-cdn.net/images/techn-icon-snmp-43de4f1139.svg "SNMP")

### SNMP

Узнайте, как мониторить сетевые устройства с помощью SNMP.](/docs/ingest-from/extensions/supported-extensions/data-sources/snmp "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативных метрик и приёма событий SNMP.")[![WMI](https://dt-cdn.net/images/techn-icon-microsoft-e15d516aaf.svg "WMI")

### WMI

Узнайте, как мониторить устройства с помощью WMI (Windows Management Instrumentation).](/docs/ingest-from/extensions/supported-extensions/data-sources/wmi "Узнайте, как расширить наблюдаемость в Dynatrace с помощью декларативного приёма метрик WMI.")[![JMX](https://dt-cdn.net/images/techn-icon-java-3016283f6a.svg "JMX")

### JMX

Расширение наблюдаемости Java-приложений с помощью метрик JMX.](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/jmx-extensions "Узнайте, как расширить мониторинг Dynatrace, включив приложения, инструментированные с помощью JMX.")[### Скриптовая интеграция

Расширение наблюдаемости метрик через скриптовую интеграцию Dynatrace.](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-pipe "Узнайте, как принимать метрики с помощью локальной скриптовой интеграции.")[### API приёма метрик

Расширение наблюдаемости метрик через открытые API метрик Dynatrace.](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте API Dynatrace для получения метрик отслеживаемых сущностей.")

## Доступ к принятым метрикам

Вы можете получить доступ к принятым метрикам через Metric API v2 и в Data Explorer для построения пользовательских графиков.

### Metrics API

Используйте вызов [GET metric data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Чтение точек данных одной или нескольких метрик через Metrics v2 API.") из Metrics API v2 для получения принятых точек данных.

### Data Explorer

Выберите **Create custom chart**, а затем **Try it out** в верхнем баннере. Подробнее см. в разделе [Data Explorer](/docs/analyze-explore-automate/explorer "Запрос метрик и преобразование результатов для получения нужных данных.").

Вы можете искать ключи всех доступных метрик, выбирать метрики для отображения на графике, определять способ их анализа и визуализации, а затем закреплять графики на панели мониторинга.

## События

Канал приёма пользовательских метрик позволяет принимать все типы измерений метрик, независимо от количества сущностей, к которым они относятся. Способ создания события зависит от того, нет ли сущности, есть одна или несколько сущностей, назначенных пользовательской метрике. Подробнее см. в разделе [Топологическая осведомлённость](/docs/dynatrace-intelligence/anomaly-detection/metric-events#topology "Узнайте о событиях метрик в Dynatrace").

## Оповещения по метрикам

Вы также можете создавать пользовательские оповещения на основе принятых метрик. Перейдите в **Settings** > **Anomaly detection** > **Metric events** и выберите **Add metric event**. На странице **Add metric event** найдите метрику по её ключу и определите параметры оповещения. Подробнее см. в разделе [События метрик для оповещений](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о событиях метрик в Dynatrace").

## Приём пользовательских метрик влияет на потребление DDU

Только ограниченный приём и анализ пользовательских метрик включён в стандартную поддержку технологий Dynatrace. Пользовательские метрики обычно потребляют единицы данных Davis (DDU), но пользовательские метрики с хостов, отслеживаемых OneAgent, сначала вычитаются из вашей квоты [включённых метрик на единицу хоста](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Узнайте, как рассчитать потребление единиц данных Davis и затраты, связанные с мониторингом метрик."), поэтому они не обязательно потребляют DDU. Это относится к метрикам, которые привязаны к хосту автоматически или путём добавления измерения `dt.entity.host`.

Подробнее см. в разделе [DDU для пользовательских метрик](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Узнайте, как рассчитать потребление единиц данных Davis и затраты, связанные с мониторингом метрик.").

* Каждая принятая метрика, подлежащая потреблению DDU (то есть не привязанная к хосту), генерирует одну или несколько **точек данных метрик**. Эти точки данных потребляют DDU с весом 0,001. Таким образом, простая метрика, отправляемая раз в минуту в течение всего года, потребит 526 DDU (`525 600 минут x 0,001 = 526 DDU`).
* Чтобы проверить потребление DDU среды, перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

### Измерения метрик также влияют на потребление DDU

При определении того, какие принятые метрики будут потреблять DDU и когда, необходимо учитывать два дополнительных фактора:

* **Кортежи**: уникальные комбинации пар метрика-измерение (см. примеры ниже).

  + Метрики (классическая модель)
    Каждая среда может поддерживать максимум 50 000 000 уникальных кортежей в месяц.

  + Метрики на базе Grail
    Каждый кортеж учитывается в [лимите кардинальности](/docs/analyze-explore-automate/metrics/limits "Справочник по метрикам на базе Grail") вашей среды.
* **Временные рамки**: когда одна и та же метрика принимается с уникальными кортежами измерений **в пределах 1-минутного интервала, каждый дополнительный кортеж приводит к потреблению ещё одной точки данных метрики.**

#### Примеры

В следующих примерах предполагается, что все метрики принимаются один раз в минуту.

* В первом примере один и тот же кортеж измерений отправляется дважды в пределах одноминутного интервала. Поэтому потребляется только одна (агрегированная) точка данных (`1 точка данных x 0,001 DDU`).

  ```
  cpu.temp,cpu=cpu1,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu1,cpu_type="INTEL" 75
  ```
* Здесь две различные пары измерений отправляются в пределах одноминутного интервала. Поэтому потребляются две точки данных (`2 x 0,001 DDU`). С точки зрения потребления это фактически две различные метрики. Кортеж с двумя измерениями потребляет `526 x 2 = 1 052` DDU в год.

  ```
  cpu.temp,cpu=cpu1,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu2,cpu_type="INTEL" 75
  ```
* Здесь четыре различные пары измерений отправляются в пределах одноминутного интервала. Поэтому потребляются четыре точки данных (`4 x 0,001 DDU`). С точки зрения потребления это фактически четыре различные метрики. Кортеж с четырьмя измерениями потребляет `526 x 4 = 2 104` DDU в год.

  ```
  cpu.temp,cpu=cpu1,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu2,cpu_type="INTEL" 75



  cpu.temp,cpu=cpu3,cpu_type="INTEL" 55



  cpu.temp,cpu=cpu4,cpu_type="INTEL" 75
  ```

Каждое значение измерения (в данном примере — каждая сетевая карта) генерирует отдельный временной ряд в графике. Поэтому при [расчёте потребления пользовательских метрик](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Узнайте, как рассчитать потребление единиц данных Davis и затраты, связанные с мониторингом метрик.") каждое значение измерения учитывается как отдельная пользовательская метрика.

## Лимиты

Следующие лимиты применяются к приёму метрик через общий канал приёма. Для метрик, принятых через API, при превышении любого лимита вызов API возвращает код ответа **400** с подробностями в теле ответа.

| Сущность | Лимит | Описание |
| --- | --- | --- |
| Длина ключа метрики, символов | 250 | Общая длина ключа метрики, включая префикс. |
| Длина ключа измерения, символов | 100 | Общая длина ключа измерения. |
| Длина значения измерения, символов | 250 | Общая длина значения измерения. |
| Количество измерений в строке | 50 | Количество измерений в одной строке полезной нагрузки. |
| Общее количество возможных ключей метрик на среду | 100 000 | Максимальное количество ключей метрик, которые могут быть зарегистрированы в Dynatrace. |
| Количество кортежей в месяц на метрику | 1 000 000 | Максимальное количество кортежей (уникальных комбинаций ключ метрики-ключ измерения-значение измерения-тип полезной нагрузки) для каждого ключа метрики за последние 30 дней. |
| Количество кортежей в месяц для всех пользовательских метрик | 50 000 000 | Максимальное количество кортежей (уникальных комбинаций ключ метрики-ключ измерения-значение измерения-тип полезной нагрузки) для всех пользовательских метрик за последние 30 дней. |
| Длина строки, символов | 50 000 | Максимальная длина одной строки полезной нагрузки. |

Также существует лимит на количество метрик, которые Dynatrace может принять.