---
title: DDUs for Log Monitoring Classic
source: https://docs.dynatrace.com/managed/license/classic-licensing/davis-data-units/log-monitoring-consumption
---

# DDUs for Log Monitoring Classic

# DDUs for Log Monitoring Classic

* 7-min read
* Published Dec 21, 2020

## How does Dynatrace calculate DDU consumption for Log Monitoring Classic?

The Davis data units (DDUs) model counts all incoming log records (entries) from your log data. Each log record (line, message, entry) deducts `0.0005 DDU` from your available quota. For example, 1 million log records multiplied by a DDU weight of 0.0005 consumes a total of 500 DDUs.

A log record is recognized in two ways:

* Timestamp
* JSON object

### Timestamp

Dynatrace assumes that a timestamp is the beginning of a new log record.

For example, in the following log data (consumed via log file or generic ingestion), Dynatrace counts nine log records based on timestamp occurrence:

#### Log file input

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

#### Generic ingestion input

```
curl -X POST "https://my.activegate/api/v2/logs/ingest"



-H  "accept: application/json; charset=utf-8"



-H  "Content-Type: text/plain; charset=utf-8"



-d "Oct 18 05:56:11 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1Oct 18 05:56:12 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1Oct 18 05:56:13 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1551s4:Oct 18 05:56:15 INFO ip-10-176-34-132 [get_meta] Getting token for IMDSvOct 18 05:56:16 INFO ip-10-176-34-132 [get_meta] Trying to get http://169.23.2.3Oct 18 05:56:18 INFO ip-10-176-34-132 [rewrite_aliases] Rewriting aliasesOct 18 06:22:06 INFO ip-10-176-34-132 DHCPREQUEST on eth0 to 10.176.34.1 port 67Oct 18 06:22:07 INFO ip-10-176-34-132 DHCPACK from 10.176.34.1 (xid=0x3a182c8c)Oct 18 06:22:10 INFO ip-10-176-34-132 bound to 10.176.34.132 -- renewal in 1364s"
```

The DDU cost is `9` log lines/records × `0.0005` log weight = `0.0045` DDUs.

### JSON object

Dynatrace assumes that a single JSON object is a log record. A JSON file can contain multiple objects that count as a log record.

For example, in the following log data, Dynatrace counts three log records based on JSON object occurrence:

#### Log file

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

The DDU cost is `3` log lines/records × `0.0005` log weight = `0.0015` DDUs

## How Log Monitoring Classic can affect your DDU consumption

Dynatrace counts log records based on timestamp, even if the log record contains an attached stack trace.

For example, both of the following logs (Log1 and Log2) contain 14 lines of log data. Dynatrace calculates log records that consume DDUs on valid timestamp. As a result, Log1 generated a cost of `0.007` DDUs while Log2 generated a cost of `0.001` DDUs.

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

The DDU cost is `14` log records × `0.0005` log weight = `0.007` DDUs.

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

The DDU cost is `2` log records × `0.0005` log weight = `0.001` DDUs.

## FAQ

### Can I change the retention period for Log Monitoring Classic?

There is no way to change retention periods in Log Monitoring Classic. Use Log Management and Analytics in Dynatrace SaaS to manage retention periods for log files.

### Where can I check my log consumption for DDUs?

To check your DDU consumption

1. Go to [**Account Management**﻿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**.

   You need the **Manage monitoring settings** permission or an admin account to access this page.
2. On the **Davis data units (DDU)** page:

   * In the **Consumption by DDU pool** table, check the **Log Monitoring** row.
   * In the **DDU consumption details** section, check the **Log Monitoring** tab.

### What is the weight of one log record?

Each log record consumes 0.0005 DDU.

### What is the size of one log record?

Dynatrace recognizes a log record as a single log entry that contains a valid timestamp or is described in a JSON object. This log record can contain multiple lines of log data and, depending on your log verbosity, the same amount of log data may contain a different number of log records consuming DDUs.

### Are there any host-included DDUs available for Log Monitoring Classic?

No. Dynatrace only offers host-included metrics.
Log ingestion always consumes DDUs, which are deducted from your available quota.

## Related topics

* [Dynatrace pricing﻿](https://www.dynatrace.com/pricing/)
* [Log Monitoring](/managed/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")