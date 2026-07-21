---
title: DDU для Log Monitoring Classic
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units/log-monitoring-consumption
---

# DDU для Log Monitoring Classic

# DDU для Log Monitoring Classic

* 7 минут чтения
* Опубликовано 21 дек. 2020 г.

## Как Dynatrace рассчитывает потребление DDU для Log Monitoring Classic?

Модель Davis data units (DDU) учитывает все входящие записи логов (записи) из логовых данных. Каждая запись лога (строка, сообщение, запись) списывает `0.0005 DDU` из доступной квоты. Например, 1 миллион записей лога, умноженный на вес DDU 0.0005, потребляет в сумме 500 DDU.

Запись лога распознаётся двумя способами:

* По временной метке
* По объекту JSON

### Временная метка

Dynatrace считает, что временная метка, это начало новой записи лога.

Например, в следующих логовых данных (полученных через файл лога или generic ingestion) Dynatrace насчитывает девять записей лога на основе появления временных меток:

#### Ввод из файла лога

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

#### Ввод через generic ingestion

```
curl -X POST "https://my.activegate/api/v2/logs/ingest"



-H  "accept: application/json; charset=utf-8"



-H  "Content-Type: text/plain; charset=utf-8"



-d "Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1Oct 18 05:56:13 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1551s4:Oct 18 05:56:15 INFO ip-10-176-34-132 [get_meta] Getting token for IMDSvOct 18 05:56:16 INFO ip-10-176-34-132 [get_meta] Trying to get http://169.23.2.3Oct 18 05:56:18 INFO ip-10-176-34-132 [rewrite_aliases] Rewriting aliasesOct 18 06:22:06 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1 port 67Oct 18 06:22:07 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1 (xid=0x3a182c8c)Oct 18 06:22:10 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1364s"
```

Стоимость DDU: `9` строк/записей лога × `0.0005` вес лога = `0.0045` DDU.

### Объект JSON

Dynatrace считает, что один объект JSON, это одна запись лога. Файл JSON может содержать несколько объектов, каждый из которых засчитывается как отдельная запись лога.

Например, в следующих логовых данных Dynatrace насчитывает три записи лога на основе появления объектов JSON:

#### Файл лога

```
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

#### Generic Ingestion

```
curl -X POST "https://my.activegate/api/v2/logs/ingest"



-H  "accept: application/json; charset=utf-8"



-H  "Content-Type: application/json; charset=utf-8"



-d "[{\"timestamp\":\"2021-07-29T10:54:40.962165022Z\",\"level\":\"error\",\"log.source\":\"/var/log/syslog\",\"application.id\":\"PaymentService-Prod\",\"content\":\"DHCPREQUEST on eth0 to 10.176.34.1\"},{\"log.source\":\"/var/log/syslog\",\"content\":\"[get_meta] Getting token for IMDSv\"},{\"content\":\"DHCPACK from 10.176.34.1 (xid=0x3a182c8c)\"}]"
```

Стоимость DDU: `3` строки/записи лога × `0.0005` вес лога = `0.0015` DDU

## Как Log Monitoring Classic может влиять на потребление DDU

Dynatrace считает записи лога на основе временной метки, даже если запись лога содержит прикреплённый stack trace.

Например, оба следующих лога (Log1 и Log2) содержат по 14 строк логовых данных. Dynatrace рассчитывает записи лога, потребляющие DDU, по действительной временной метке. В результате Log1 сгенерировал стоимость `0.007` DDU, а Log2 сгенерировал стоимость `0.001` DDU.

#### Log1

```
1:  Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1



2:  Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1



3:  Oct 18 05:56:13 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1551s4:



4:  Oct 18 05:56:15 INFO ip-10-176-34-132 [get_meta] Getting token for IMDSv



5:  Oct 18 05:56:16 INFO ip-10-176-34-132 [get_meta] Trying to get http://169.23.2.3



6:  Oct 18 05:56:15 INFO ip-10-176-34-132 [get_meta] Getting token for IMDSv



7:  Oct 18 06:16:16 INFO ip-10-176-34-132 [get_meta] Trying to get http://169.23.2.3



8:  Oct 18 06:16:18 INFO ip-10-176-34-132 [rewrite_aliases] Rewriting aliases



9:  Oct 18 06:21:26 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1 port 67



10: Oct 18 06:22:06 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1 port 67



11: Oct 18 06:22:07 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1 (xid=0x3a182c8c)



12: Oct 18 06:22:10 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1364s



13: Oct 18 14:51:22 ERROR ip-10-176-34-32 classOne: Index out of range



14: Oct 18 16:52:10 ERROR ip-10-176-34-32 classOne: Index out of range
```

Стоимость DDU: `14` записей лога × `0.0005` вес лога = `0.007` DDU.

#### Log2

```
1: Oct 18 14:51:22 ERROR ip-10-176-34-32 classOne: Index out of range



2:     java.lang.StringIndexOutOfBoundsException: String index out of range: 18



3:     at java.lang.String.charAt(String.java:658)



4:     at com.example.app.loggingApp.classOne.getResult(classOne.java:15)



5:     at com.example.app.loggingApp.AppController.tester(AppController.java:27)



6:     at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)



7:     at sun.reflect.NativeMethodAccessorImpl.invoke0(NativeMethodAccessorImpl.java:62)



8: Oct 18 16:52:10 ERROR ip-10-176-34-32 classOne: Index out of range



9:     java.lang.StringIndexOutOfBoundsException: String index out of range: 18



10:    at java.lang.String.charAt(String.java:658)



11:    at com.example.app.loggingApp.classOne.getResult(classOne.java:15)



12:    at com.example.app.loggingApp.AppController.tester(AppController.java:27)



13:    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)



14:    at sun.reflect.NativeMethodAccessorImpl.invoke0(NativeMethodAccessorImpl.java:62)
```

Стоимость DDU: `2` записи лога × `0.0005` вес лога = `0.001` DDU.

## FAQ

### Можно ли изменить период хранения для Log Monitoring Classic?

Изменить периоды хранения в Log Monitoring Classic нельзя. Используй Log Management and Analytics в Dynatrace SaaS для управления периодами хранения файлов логов.

### Где можно проверить потребление логов по DDU?

Чтобы проверить потребление DDU

1. Перейди в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

   Для доступа к этой странице нужны разрешение **Manage monitoring settings** или учётная запись администратора.
2. На странице **Davis data units (DDU)**:

   * В таблице **Consumption by DDU pool** проверь строку **Log Monitoring**.
   * В разделе **DDU consumption details** проверь вкладку **Log Monitoring**.

### Каков вес одной записи лога?

Каждая запись лога потребляет 0.0005 DDU.

### Каков размер одной записи лога?

Dynatrace распознаёт запись лога как одну запись логов, которая содержит действительную временную метку или описана в объекте JSON. Такая запись лога может содержать несколько строк логовых данных, и в зависимости от уровня детализации логов один и тот же объём логовых данных может содержать разное количество записей лога, потребляющих DDU.

### Есть ли для Log Monitoring Classic бесплатные DDU, включённые в хост?

Нет. Dynatrace предлагает только метрики, включённые в хост.
Приём логов всегда потребляет DDU, которые списываются с доступной квоты.

## Похожие темы

* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)
* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Узнай, как включить Log Monitoring, какие данные предоставляет Log Monitoring, и многое другое.")