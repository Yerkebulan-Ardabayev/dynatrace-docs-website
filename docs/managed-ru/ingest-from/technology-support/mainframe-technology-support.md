---
title: Поддержка технологий мейнфрейма
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/mainframe-technology-support
scraped: 2026-05-12T11:06:28.120870
---

# Поддержка технологий мейнфрейма

# Поддержка технологий мейнфрейма

* Чтение: 3 мин
* Обновлено 7 апреля 2026 г.

Dynatrace поддерживает мониторинг перечисленных ниже технологий и версий на IBM z/OS.

Поддерживаемые операционные системы модуля zRemote перечислены в разделе [Системные требования](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#system-requirements "Подготовка и установка zRemote для мониторинга z/OS.").

Схема версий поддержки технологий

Определение схемы версий поддержки технологий с примерами:

* **Поддерживается мажорная версия 5**

  + Поддерживается мажорная версия 5, включая все её минорные версии, такие как 5.1 и 5.2
  + Другие мажорные версии не поддерживаются, например 6 и 7
* **Поддерживается минорная версия 5.1**

  + Поддерживается минорная версия 5.1, включая все её патч-версии, такие как 5.1.1 и 5.1.2
  + Другие минорные версии не поддерживаются, например 5.2 и 5.3
* **Поддерживается патч-версия 5.1.1**

  + Поддерживается патч-версия 5.1.1
  + Другие патч-версии не поддерживаются, например 5.1.2 и 5.1.3
* **Поддерживается диапазон версий 5.1 – 5.3**

  + Поддерживаются минорные версии 5.1, 5.2 и 5.3, включая все их патч-версии, такие как 5.1.1, 5.2.1 и 5.3.1
  + Другие минорные версии не поддерживаются, например 5.0 и 5.4
* **Минимально требуемая версия: 5+**

  + Поддерживаются все мажорные, минорные и патч-версии начиная с версии 5, такие как 5, 5.1, 5.1.1 и 6

## IBM z/OS

Чтобы начать мониторинг, см. [Dynatrace для z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Установка, настройка и управление модулями Dynatrace на z/OS.").

| Операционная система | Версии |
| --- | --- |
| IBM z/OS | 2.3, 2.4, 2.5, 3.1, 3.2 |

## IBM CICS

Чтобы начать мониторинг, см. [Установка модуля CICS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics "Установка модуля Dynatrace CICS.").

| IBM CICS | Версии |
| --- | --- |
| CICS Transaction Server | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2, 6.3 |
| CICS MQ Bridge |  |
| CICS MQ Trigger Monitor |  |
| CICS HTTP/S |  |
| CICS JSON (non-Java JSON pipeline) |  |
| CICS SOAP (over HTTP) |  |
| CICS file access[1](#fn-1-1-def) |  |

1

Поддерживаются методы доступа к файлам CICS: VSAM и BDAM.

| Клиент базы данных | Версии |
| --- | --- |
| IBM Db2 | 11, 12, 13 |
| IBM IMS DB[1](#fn-2-1-def) |  |

1

Поддерживается метод доступа к базе данных DL/I.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2, 9.3 |

## IBM IMS

Чтобы начать мониторинг, см. [Установка модуля IMS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims "Установка модуля Dynatrace IMS.").

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
| IBM MQ | 8.0, 9.0, 9.1, 9.2, 9.3 |

## z/OS Java

Чтобы начать мониторинг, см. [Установка модуля z/OS Java](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Настройка мониторинга Java на z/OS с помощью модуля Java.").

| Среда выполнения Java | Версии |
| --- | --- |
| IBM JVM for z/OS | 8 |
| IBM Semeru for z/OS | 11 |
| IBM Semeru for z/OS | 17 |
| IBM Semeru for z/OS[1](#fn-5-1-def) | 21 |

1

Virtual Threads в настоящее время не поддерживаются

Перечисленные ниже технологии поддерживаются только при использовании с поддерживаемой средой выполнения Java.
В некоторых случаях для сохранения поддержки может потребоваться ручное обновление среды выполнения Java
(например, IBM CICS Transaction Gateway версии ниже 9.2).

| Технология | Версии |
| --- | --- |
| IBM WebSphere Application Server | 8.5.5, 9.0 |
| IBM WebSphere Liberty | 18, 19, 20, 21, 22, 23, 24, 25, 26 |
| IBM z/OS Connect [1](#fn-6-1-def)[2](#fn-6-2-def) | 3.0.30+ |
| IBM CICS Transaction Gateway [3](#fn-6-3-def)[4](#fn-6-4-def) | 9.0, 9.1, 9.2, 9.3 |
| IBM IMS SOAP Gateway [5](#fn-6-5-def) | 3.2 |
| Apache HttpClient | 3.1, 4, 5 |

1

Поддерживается только автономная конфигурация z/OS Connect.

2

Поддерживаются только поставщики услуг CICS, IMS и IBM MQ.

3

Поддерживаются только протоколы EXCI и IPIC.

4

Конфигурация WAS в локальном режиме не поддерживается.

5

Поддерживается только входящая трассировка.

| Фреймворк базы данных | Версии |
| --- | --- |
| JDBC [1](#fn-7-1-def) | 3, 4 |

1

Поддерживаются только [типы драйверов Db2 JDBC](https://www.ibm.com/docs/en/sdi/7.2.0.3?topic=drivers-connecting-db2) 2 и 4.

| Клиент обмена сообщениями | Версии |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2 |
| JMS | 1.1 |

| Фреймворк мониторинга | Версии |
| --- | --- |
| [JMX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Узнайте, как настроить мониторинг метрик JMX для ваших Java-приложений на z/OS.") | 1.0+ |