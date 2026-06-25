---
title: Log Monitoring Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/log-monitoring-classic
scraped: 2026-05-12T12:13:11.406817
---

# Log Monitoring Classic (DPS)

# Log Monitoring Classic (DPS)

* 16-min read
* Updated on Jan 12, 2026

На этой странице описано, как потребляется и тарифицируется DPS-возможность Log Monitoring Classic.
Обзор возможности и основных функций см. в [Log Monitoring Classic](/managed/license/capabilities/platform-extensions#logs "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: записи лога

Единица измерения для Log Monitoring Classic — одна запись лога.

* Каждая временная метка считается новой записью лога.
* Каждый JSON-объект считается записью лога. Файл JSON может содержать несколько объектов, каждый из которых считается записью лога.

### Временные метки

Например, в следующих данных лога (принятых через лог-файл или универсальный приём) Dynatrace подсчитывает девять записей лога по числу временных меток:

1. `Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1`
2. `Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1`
3. `Oct 18 05:56:13 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1551s4:`
4. `Oct 18 05:56:13 INFO ip-10-176-34-132 [get\_meta] Getting token for IMDSv`
5. `Oct 18 05:56:16 INFO ip-10-176-34-132 [get\_meta] Trying to get http://169.23.2.3`
6. `Oct 18 05:56:18 INFO ip-10-176-34-132 [rewrite\_aliases] Rewriting aliases`
7. `Oct 18 06:22:06 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1 port 67`
8. `Oct 18 06:22:07 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1 (xid=0x3a182c8c)`
9. `Oct 18 06:22:10 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1364s`

### JSON-объекты

Например, в следующих данных лога Dynatrace подсчитывает три записи лога по числу JSON-объектов:

```
{
  "timestamp": "2021-07-29T10:54:40.962165022Z",
  "level": "error",
  "log.source": "/var/log/syslog",
  "application.id": "PaymentService-Prod",
  "content": "DHCPREQUEST on eth0 to 10.176.34.1"
},
{
  "log.source": "/var/log/syslog",
  "content": "[get\_meta] Getting token for IMDSv"
},
{
  "content": "DHCPACK from 10.176.34.1 (xid=0x3a182c8c)"
}
```

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Log Monitoring Classic в вашей организации.

Для использования в Data Explorer введите DPS в поле **Search**.
Эти метрики также доступны через Environment API и связаны в Account Management (**Usage summary** > **Log Monitoring Classic** > **Actions** > **View details**).
В таблице ниже перечислены метрики для мониторинга деталей потребления Log Monitoring Classic.

(DPS) Total Log Monitoring Classic billing usage
:   Ключ: `builtin:billing.log_monitoring_classic.usage`

    Измерение: count

    Разрешение: 1 мин

    Описание: Количество принятых записей лога, агрегированных по всем мониторируемым сущностям.

(DPS) Log Monitoring Classic billing usage by monitored entity
:   Ключ: `builtin:billing.log_monitoring_classic.usage_by_entity`

    Измерение: `dt.entity.monitored_entity\[ME:MONITORED_ENTITY]`

    Разрешение: 1 мин

    Описание: Количество принятых записей лога с разбивкой по мониторируемой сущности.

(DPS) Log Monitoring Classic billing usage by log path
:   Ключ: `builtin:billing.log_monitoring_classic.usage_by_log_path`

    Измерение: `log_path\[STRING]`

    Разрешение: 1 мин

    Описание: Количество принятых записей лога с разбивкой по пути лога.

Суммарное количество тарифицируемых записей лога за различные интервалы (15 мин, час, день или неделя) в любом выбранном периоде можно отслеживать с помощью метрики «(DPS) Total Log Monitoring Classic billing usage».
В примере ниже показано потребление, агрегированное в 1-часовых интервалах.

![Log Monitoring Classic (DPS)](https://dt-cdn.net/images/image050-793-028075d0da.png)

Log Monitoring Classic (DPS)

Потребление записей лога по любой отфильтрованной сущности можно отслеживать с помощью метрики «(DPS) Log Monitoring Classic billing usage by monitored entity».
В примере ниже показано количество тарифицируемых записей лога, поступивших с указанного хоста.

![Log Monitoring Classic (DPS)](https://dt-cdn.net/images/image052-784-fdeaf93f29.png)

Log Monitoring Classic (DPS)

Потребление записей лога по любому отфильтрованному пути лога можно отслеживать с помощью метрики «(DPS) Log Monitoring Classic billing usage by log path».
В примере ниже показано количество тарифицируемых записей лога, поступивших из OneAgent и API.

![Log Monitoring Classic (DPS)](https://dt-cdn.net/images/image054-787-fae2c8abd8.png)

Log Monitoring Classic (DPS)

## Связанные темы

* [Обзор расширений платформы (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)