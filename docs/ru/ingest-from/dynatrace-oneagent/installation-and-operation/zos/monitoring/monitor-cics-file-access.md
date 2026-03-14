---
title: Мониторинг доступа к файлам приложений CICS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access
scraped: 2026-03-05T21:29:56.255357
---

# Monitor file access of CICS applications

# Monitor file access of CICS applications

* Latest Dynatrace
* 1-min read
* Published Jan 13, 2023

С помощью Dynatrace вы можете отслеживать вызовы доступа к файлам VSAM и BDAM из ваших CICS-приложений с использованием модуля CICS. Каждый файл, к которому осуществляется доступ в регионе CICS, представлен как сервис базы данных на странице [Databases](../../../../../observe/infrastructure-observability/databases.md "Track the database performance and resources to create and maintain a high performing and available application infrastructure."), включая такие метрики, как время отклика, частота сбоев и пропускная способность.

![File access on the Database page](https://dt-cdn.net/images/file-sensor-db-3052-6d5ec51cdd.png)

На странице [Distributed traces](../../../../../observe/application-observability/distributed-traces.md "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") перечислены файловые операции и логические имена файлов, к которым осуществляется доступ на [уровне методов PurePath](../../../../../observe/application-observability/distributed-traces/use-cases/segment-request.md "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces."). Файловые операции агрегируются по логическому имени файла (например, на изображении ниже операция `READNEXT` была выполнена 21 раз для файла `EXMPCAT`).

![File access calls in the Distributed traces page](https://dt-cdn.net/images/file-sensor-pp-3142-684de155b6.png)

## Начало работы

Чтобы начать мониторинг вызовов доступа к файлам из ваших CICS-приложений

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Активируйте [функцию OneAgent](../../../oneagent-features.md "Manage OneAgent features globally and per process group.") **z/OS CICS file monitoring sensor**.
3. Перезапустите регион CICS или подождите, пока [транзакция DTAX](../operation/dtax-transaction.md "Manage the CICS module via DTAX transactions.") применит новую настройку конфигурации в течение следующего 5-минутного интервала.

## Удалённые файлы

В прикладной программе, если API управления файлами содержит предложение `SYSID` с удалённым `SYSID`, файл распознаётся как удалённый. Однако если файл определён как удалённый в определении `CEDA`, модуль CICS не распознаёт файл как удалённый.

## Отключение мониторинга доступа к файлам

Чтобы отключить мониторинг доступа к файлам, переведите датчик `z/OS CICS file monitoring` и параметр `Instrumentation enabled (change needs a process restart)` в выключенное состояние. Для вступления настроек в силу не требуется перезапускать регион CICS. Транзакция DTAX применяет изменения датчика файлов (включение/выключение) в течение 5 минут.
