---
title: Поддержка технологий мейнфрейма
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/mainframe-technology-support
---

# Поддержка технологий мейнфрейма

# Поддержка технологий мейнфрейма

* Чтение за 3 минуты
* Обновлено 14 июля 2026 г.

Dynatrace поддерживает мониторинг технологий и версий, перечисленных ниже, на IBM z/OS.

Поддерживаемые операционные системы для модуля zRemote указаны в разделе [Системные требования](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#system-requirements "Prepare and install the zRemote for z/OS monitoring.").

Схема версий поддержки технологий

Определение схемы версий поддержки технологий с примерами:

* **Поддерживается мажорная версия 5**

  + Мажорная версия 5 поддерживается, включая все её минорные версии, например 5.1 и 5.2
  + Другие мажорные версии не поддерживаются, например 6 и 7
* **Поддерживается минорная версия 5.1**

  + Минорная версия 5.1 поддерживается, включая все её патч-версии, например 5.1.1 и 5.1.2
  + Другие минорные версии не поддерживаются, например 5.2 и 5.3
* **Поддерживается патч-версия 5.1.1**

  + Патч-версия 5.1.1 поддерживается
  + Другие патч-версии не поддерживаются, например 5.1.2 и 5.1.3
* **Поддерживается диапазон версий 5.1 – 5.3**

  + Минорные версии 5.1, 5.2 и 5.3 поддерживаются, включая все их патч-версии, например 5.1.1, 5.2.1 и 5.3.1
  + Другие минорные версии не поддерживаются, например 5.0 и 5.4
* **Минимально необходимая версия 5+**

  + Все мажорные, минорные и патч-версии начиная с версии 5 поддерживаются, например 5, 5.1, 5.1.1 и 6

## IBM z/OS

Чтобы начать работу с мониторингом, см. [Dynatrace для z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.").

| Операционная система | Версии |
| --- | --- |
| IBM z/OS | 2.3, 2.4, 2.5, 3.1, 3.2 |

## IBM CICS

Чтобы начать работу с мониторингом, см. [Установка модуля CICS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics "Install the Dynatrace CICS module.").

| IBM CICS | Версии |
| --- | --- |
| CICS Transaction Server | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3 |
| CICS MQ Bridge |  |
| CICS MQ Trigger Monitor |  |
| CICS HTTP/S |  |
| CICS JSON (не-Java пайплайн JSON) |  |
| CICS SOAP (через HTTP) |  |
| Доступ к файлам CICS[1](#fn-1-1-def) |  |

1

Поддерживаются методы доступа к файлам CICS VSAM и BDAM.

| Клиент базы данных | Версии |
| --- | --- |
| IBM Db2 | 11, 12, 13 |
| IBM IMS DB[1](#fn-2-1-def) |  |

1

Поддерживается метод доступа к базе данных DL/I.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2, 9.3, 9.4, 10 |

## IBM IMS

Чтобы начать работу с мониторингом, см. [Установка модуля IMS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims "Install the Dynatrace IMS module.").

| IBM IMS | Версии |
| --- | --- |
| IMS [1](#fn-3-1-def)[2](#fn-3-2-def) | 13, 14, 15 |
| IMS TM Resource Adapter | 13, 14, 15 |
| IMS MQ Bridge[1](#fn-3-1-def) |  |
| IMS MQ Trigger Monitor |  |
| IMS Connect API[1](#fn-3-1-def) | 3.2 |

1

Поддерживается только входящая трассировка.

2

Трассировка транзакций Fast Path и BMP поддерживается только для IMS 15.

| Клиент базы данных | Версии |
| --- | --- |
| IBM Db2 | 11, 12, 13 |
| IBM IMS DB[1](#fn-4-1-def) |  |

1

Поддерживаются методы доступа к базе данных DL/I и Fast Path.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2, 9.3, 9.4, 10 |

## z/OS Java

Чтобы начать работу с мониторингом, см. [Установка модуля z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.").

| Среда выполнения Java | Версии |
| --- | --- |
| IBM JVM для z/OS | 8 |
| IBM Semeru для z/OS | 11 |
| IBM Semeru для z/OS | 17 |
| IBM Semeru для z/OS[1](#fn-5-1-def) | 21 |

1

Virtual Threads в настоящее время не поддерживаются

Перечисленные ниже технологии поддерживаются только при использовании с поддерживаемой средой выполнения Java.
В некоторых случаях для сохранения поддержки может потребоваться ручное обновление среды выполнения Java
(например, для IBM CICS Transaction Gateway версии ниже 9.2).

| Технология | Версии |
| --- | --- |
| IBM WebSphere Application Server | 8.5.5, 9.0 |
| IBM WebSphere Liberty | 18, 19, 20, 21, 22, 23, 24, 25, 26 |
| IBM z/OS Connect [1](#fn-6-1-def)[2](#fn-6-2-def) | 3.0.30+ |
| IBM CICS Transaction Gateway [3](#fn-6-3-def)[4](#fn-6-4-def) | 9.0, 9.1, 9.2, 9.3, 10.1 |
| IBM IMS SOAP Gateway [5](#fn-6-5-def) | 3.2 |
| Apache HttpClient | 3.1, 4, 5 |

1

Поддерживается только автономная конфигурация z/OS Connect.

2

Поддерживаются только провайдеры служб CICS, IMS и IBM MQ.

3

Поддерживаются только протоколы EXCI и IPIC.

4

Конфигурация локального режима WAS не поддерживается.

5

Поддерживается только входящая трассировка.

| Фреймворк базы данных | Версии |
| --- | --- |
| JDBC [1](#fn-7-1-def) | 3, 4 |

1

Поддерживаются только [драйверы Db2 JDBC типов﻿](https://www.ibm.com/docs/en/sdi/7.2.0.3?topic=drivers-connecting-db2) 2 и 4.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2 |
| JMS | 1.1 |

| Фреймворк мониторинга | Версии |
| --- | --- |
| [JMX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.") | 1.0+ |