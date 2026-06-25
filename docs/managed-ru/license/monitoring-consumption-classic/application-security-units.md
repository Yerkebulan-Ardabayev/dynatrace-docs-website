---
title: Мониторинг Application Security (единицы ASU)
source: https://docs.dynatrace.com/managed/license/monitoring-consumption-classic/application-security-units
scraped: 2026-05-12T11:37:20.427652
---

# Мониторинг Application Security (единицы ASU)

# Мониторинг Application Security (единицы ASU)

* 6-min read
* Published Nov 30, 2021

## Application Security

[Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.") помогает визуализировать, анализировать и отслеживать уязвимости безопасности в вашей среде, связанные со сторонними библиотеками в режиме реального времени.

### Единицы Application Security

Лицензирование Dynatrace Application Security основано на потреблении единиц Application Security (ASU). Количество потребляемых ASU зависит от серверов, на которых запущены приложения, мониторируемые с помощью Application Security.

На потребление ASU влияет несколько факторов:

* Объём ОЗУ мониторируемого сервера (см. таблицу весов ниже)
* Количество часов работы сервера
* Возможности Application Security, включённые на сервере

### Возможности Application Security

В настоящее время Application Security предоставляет две возможности:

* Runtime Vulnerability Analytics
* Runtime Application Protection

### Влияние возможностей на потребление мониторинга

Каждая возможность потребляет 1 ASU в час, умноженный на весовой коэффициент ОЗУ (подробнее см. таблицу весов).

Runtime Application Protection (RAP) использует Runtime Vulnerability Assessment (RVA) для оценки уязвимости, на которой основана атака. Поэтому сервер с включённым Runtime Application Protection всегда потребляет ASU как для RVA, так и для RAP.

| Размер хоста (на основе ОЗУ GiB) | Runtime Vulnerability Analytics (единиц Application Security в час) | Runtime Vulnerability Analytics & Runtime Application Protection (единиц Application Security в час) |
| --- | --- | --- |
| 1,6 GiB | 0,10 | 0,20 |
| 4 GiB | 0,25 | 0,50 |
| 8 GiB | 0,50 | 1 |
| 16 GiB | 1 | 2 |
| 32 GiB | 2 | 4 |
| 48 GiB | 3 | 6 |
| 64 GiB | 4 | 8 |
| 80 GiB | 5 | 10 |
| N × 16 | N | N × 2 |

#### Пример

Предположим, что среда состоит из:

* 1 сервера с 32 GiB ОЗУ, работающего с RVA и RAP
* 1 сервера с 32 GiB ОЗУ, работающего только с RVA
* 1 сервера с 4 GiB ОЗУ, работающего только с RVA
* 1 сервера с 32 GiB ОЗУ для обработки всплесков нагрузки, работающего с RVA и RAP

Если первые три сервера работают 24×7, они потребляют 54 750 единиц Application Security в год. Когда среда перестаёт справляться с нагрузкой, дополнительный сервер с 32 GiB ОЗУ запускается для обработки всплесков. Этот сервер работает 250 часов в год, добавляя 1 000 ASU к потреблению.

Расчёт:

* Один сервер с 32 GiB ОЗУ с RVA и RAP потребляет 35 040 ASU в год.
  `4 ASU для RVA и RAP для 32 GiB хоста × 24 (часа) × 365 (дней)`
* Другой сервер с 32 GiB ОЗУ только с RVA потребляет 17 520 ASU в год.
  `2 ASU для RVA для 32 GiB хоста × 24 (часа) × 365 (дней)`
* Сервер с 4 GiB ОЗУ только с RVA потребляет 2 190 ASU в год.
  `0,25 ASU для RVA для 4 GiB хоста × 24 (часа) × 365 (дней)`
* Дополнительный сервер с 32 GiB ОЗУ с RVA и RAP работает всего 250 часов в год, добавляя 1 000 ASU.
  `4 ASU для RVA и RAP для 32 GiB хоста × 250 (часов)`

### Совместное использование мониторинга Application Security с Full-Stack и Infrastructure Monitoring

Единицы Application Security потребляются параллельно с хост-единицами как для Full-Stack, так и для Infrastructure Monitoring. Например, можно мониторировать безопасность хоста с сервером Tomcat в режиме Dynatrace Infrastructure Monitoring, а не Full-Stack Monitoring. Этот подход даёт аналитику Dynatrace Application Security, но без улучшенной приоритизации на основе топологии и более глубоких аналитических данных о производительности, предоставляемых режимом Full-Stack Monitoring.

Аллокация единиц Application Security применяется только к хостам, на которых работают поддерживаемые технологии. Для получения дополнительных сведений свяжитесь с экспертом Dynatrace через чат.

## Runecast Security Posture Management (SPM)

Лицензии, перечисленные здесь, не связаны с ASU мониторинга Application Security; для потребления Security Posture Management (SPM) не требуется лицензирование ASU мониторинга Application Security. Подробнее о DPS-ценообразовании SPM см. в [Application Security (DPS)](/managed/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.").

Runecast® Security Posture Management (SPM) обеспечивает непрерывный мониторинг и автоматизированную оценку для VMware® и облачных сред. Благодаря аналитике конфигураций, проблем соответствия требованиям и оценке рисков клиенты могут поддерживать высокий уровень защищённости.

### Возможности Runecast Security Posture Management (SPM)

Runecast Security Posture Management (SPM) предоставляет следующие возможности:

* VMware SPM (VSPM)
* Cloud SPM (CSPM)

### Единицы измерения Runecast Security Posture Management (SPM)

Лицензирование Runecast Security Posture Management (SPM) основано на SKU. Количество потребляемых SKU зависит от следующих единиц измерения:

* Единица измерения для VSPM — сокет CPU в год (сокеты CPU лицензированных хостов VMware® ESXi), независимо от числа ядер или виртуальных машин.
* Единица измерения для CSPM — хосты в год, где хост в контексте CSPM применяется для ресурсов вычислений, баз данных и функций. CSPM можно включать на уровне облачного аккаунта.

Лицензии структурированы как параллельные годовые единицы. Неиспользованные лицензии не переносятся на последующие периоды. Для расширения лицензированных сокетов CPU и/или хостов необходимо приобрести дополнительные лицензии.

#### Пример расчёта VSPM

Предположим, вы приобрели лицензию на 20 сокетов CPU с 1 января. Проверки VSPM инициированы и выполняются непрерывно. Через шесть месяцев вы добавляете 10 сокетов CPU и приобретаете дополнительную лицензию на них с началом с 1 июля.

Первоначальная лицензия на 20 сокетов CPU истекает 31 декабря того же года.

* 20 сокетов CPU оказываются без лицензии и не могут проверяться до продления.
* Вторая лицензия продолжает охватывать оставшиеся 10 сокетов CPU до истечения 30 июня следующего года.

#### Пример расчёта CSPM

Предположим, вы приобрели подписку на 20 тарифицируемых ресурсов AWS (EC2-инстансы и Lambda-функции) с 1 января. Проверки CSPM инициированы и выполняются непрерывно.
Через шесть месяцев вы решаете добавить 10 хостов и приобретаете дополнительную лицензию на них с началом 1 июля.
В этом случае необходимо применить новую лицензию на 30 тарифицируемых ресурсов, заменив текущую подписку.

Лицензия на первоначальные 20 хостов истекает 31 декабря.

* 20 хостов оказываются без лицензии и не могут проверяться до продления.
* Вторая лицензия продолжает охватывать оставшиеся 10 хостов до истечения 30 июня следующего года.

![cspm](https://dt-cdn.net/images/20250417-112010-1102-2d970d5643.png)

cspm

### Просмотр лицензии

Просмотреть сведения о текущих, истёкших и предстоящих лицензиях можно на [портале лицензирования](https://dt-url.net/bj03ua2) (после входа в систему лицензии отображаются в левом меню).

![view your licenses](https://dt-cdn.net/images/20250417-112053-1648-8c741dda54.png)

view your licenses

## Связанные темы

* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)
* [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.")