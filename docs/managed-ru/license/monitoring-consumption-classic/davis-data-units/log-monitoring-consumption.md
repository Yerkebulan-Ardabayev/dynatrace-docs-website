---
title: DDU для Log Monitoring Classic
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption
scraped: 2026-05-12T11:13:29.437524
---

# DDU для Log Monitoring Classic

# DDU для Log Monitoring Classic

* 7-min read
* Published Dec 21, 2020

## Как Dynatrace рассчитывает потребление DDU для Log Monitoring Classic?

Модель Davis data units (DDU) подсчитывает все входящие записи лога (entries) из ваших данных логов. Каждая запись лога (строка, сообщение, запись) вычитает `0,0005 DDU` из доступной квоты. Например, 1 миллион записей лога, умноженный на вес DDU 0,0005, потребляет суммарно 500 DDU.

Запись лога распознаётся двумя способами:

* Временная метка (timestamp)
* JSON-объект

### Временная метка

Dynatrace считает временную метку началом новой записи лога.

Например, в следующих данных лога (принятых через лог-файл или универсальный приём) Dynatrace подсчитывает девять записей лога по числу временных меток:

#### Входные данные лог-файла

```
1: Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1
2: Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1
3: Oct 18 05:56:13 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1551s4:
4: Oct 18 05:56:15 INFO ip-10-176-34-132 [get_meta] Getting token for IMDSv
5: Oct 18 05:56:16 INFO ip-10-176-34-132 [get_meta] Trying to get http://169.23.2.3
6: Oct 18 05:56:18 INFO ip-10-176-34-132 [rewrite_aliases] Rewriting aliases
7: Oct 18 06:22:06 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1 port 67
8: Oct 18 06:22:07 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1 (xid=0x3a182c8c)
9: Oct 18 06:22:10 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1364s
```

#### Универсальный приём

```
curl -X POST "https://my.activegate/api/v2/logs/ingest"
-H  "accept: application/json; charset=utf-8"
-H  "Content-Type: text/plain; charset=utf-8"
-d "Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1..."
```

Стоимость в DDU: `9` записей лога × `0,0005` веса лога = `0,0045` DDU.

### JSON-объект

Dynatrace считает единственный JSON-объект записью лога. Файл JSON может содержать несколько объектов, каждый из которых считается записью лога.

Например, в следующих данных лога Dynatrace подсчитывает три записи лога по числу JSON-объектов:

#### Лог-файл

```json
[
  {
    "timestamp": "2021-07-29T10:54:40.962165022Z",
    "level": "error",
    "log.source": "/var/log/syslog",
    "application.id": "PaymentService-Prod",
    "content": "DHCPREQUEST on eth0 to 10.176.34.1"
  },
  {
    "log.source": "/var/log/syslog",
    "content": "[get_meta] Getting token for IMDSv"
  },
  {
    "content": "DHCPACK from 10.176.34.1 (xid=0x3a182c8c)"
  }
]
```

Стоимость в DDU: `3` записи лога × `0,0005` веса лога = `0,0015` DDU.

## Влияние Log Monitoring Classic на потребление DDU

Dynatrace подсчитывает записи лога по временным меткам, даже если запись лога содержит прикреплённый стек вызовов.

Например, оба следующих лога (Log1 и Log2) содержат 14 строк данных. Dynatrace рассчитывает записи лога, потребляющие DDU, по действительным временным меткам. В результате Log1 стоил `0,007` DDU, а Log2 — `0,001` DDU.

#### Log1

```
1:  Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1
2:  Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1
3:  Oct 18 05:56:13 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1551s4:
...
14: Oct 18 16:52:10 ERROR ip-10-176-34-32 classOne: Index out of range
```

Стоимость в DDU: `14` записей лога × `0,0005` веса лога = `0,007` DDU.

#### Log2

```
1: Oct 18 14:51:22 ERROR ip-10-176-34-32 classOne: Index out of range
2:     java.lang.StringIndexOutOfBoundsException: String index out of range: 18
...
8: Oct 18 16:52:10 ERROR ip-10-176-34-32 classOne: Index out of range
...
14:    at sun.reflect.NativeMethodAccessorImpl.invoke0(NativeMethodAccessorImpl.java:62)
```

Стоимость в DDU: `2` записи лога × `0,0005` веса лога = `0,001` DDU.

## Часто задаваемые вопросы

### Можно ли изменить период хранения для Log Monitoring Classic?

Изменить периоды хранения в Log Monitoring Classic невозможно. Для управления периодами хранения лог-файлов используйте Log Management and Analytics в Dynatrace SaaS.

### Где можно проверить потребление логов для DDU?

Для проверки потребления DDU:

1. Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.
   Необходимо разрешение **Manage monitoring settings** или учётная запись администратора.
2. На странице **Davis data units (DDU)**:
   * В таблице **Consumption by DDU pool** проверьте строку **Log Monitoring**.
   * В разделе **DDU consumption details** проверьте вкладку **Log Monitoring**.

### Каков вес одной записи лога?

Каждая запись лога потребляет 0,0005 DDU.

### Каков размер одной записи лога?

Dynatrace распознаёт запись лога как единичную запись, содержащую действительную временную метку или описанную в JSON-объекте. Эта запись может содержать несколько строк данных, и в зависимости от детализации логов один и тот же объём данных может содержать разное количество записей, потребляющих DDU.

### Есть ли включённые DDU для хостов в Log Monitoring Classic?

Нет. Dynatrace предлагает только включённые метрики для хостов.
Приём логов всегда потребляет DDU, вычитаемые из доступной квоты.

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
* [Мониторинг логов](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")