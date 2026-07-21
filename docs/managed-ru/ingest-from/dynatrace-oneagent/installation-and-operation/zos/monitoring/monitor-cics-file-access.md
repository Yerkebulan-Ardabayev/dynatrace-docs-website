---
title: Мониторинг файлового доступа приложений CICS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access
---

# Мониторинг файлового доступа приложений CICS

# Мониторинг файлового доступа приложений CICS

* 1 мин чтения
* Опубликовано 13 января 2023 г.

С Dynatrace можно отслеживать вызовы доступа к файлам VSAM и BDAM из приложений CICS с помощью модуля CICS. Каждый файл, к которому обращаются в регионе CICS, представлен как служба базы данных на странице [Databases Services](/managed/observe/infrastructure-observability/databases "Learn how to automatically detect database services, how to analyze database services, and more."), включая такие метрики, как время отклика, частота сбоев и пропускная способность.

![File access on the Database page](https://dt-cdn.net/images/file-sensor-db-3052-6d5ec51cdd.png)

Доступ к файлам на странице Database

Страница [Distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") показывает файловые операции и логические имена файлов, к которым выполняется обращение, на уровне метода [PurePath](/managed/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces."). Файловые операции агрегируются по логическому имени файла (например, на изображении ниже операция `READNEXT` была выполнена 21 раз для файла `EXMPCAT`).

![File access calls in the Distributed traces page](https://dt-cdn.net/images/file-sensor-pp-3142-684de155b6.png)

Вызовы доступа к файлам на странице Distributed traces

## Начало работы

Чтобы начать мониторинг вызовов доступа к файлам из приложений CICS

1. Перейти в **Settings** > **Preferences** > **OneAgent features**.
2. Активировать [функцию OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS CICS file monitoring sensor**.
3. Перезапустить регион CICS или дождаться, пока [транзакция DTAX](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") подхватит новую настройку конфигурации в течение следующего 5-минутного интервала.

## Удалённые файлы

Если в прикладной программе блок управления файлом API содержит предложение `SYSID` с удалённым `SYSID`, файл распознаётся как удалённый. Однако если файл определён как удалённый в определении `CEDA`, модуль CICS не распознаёт файл как удалённый.

## Отключение мониторинга доступа к файлам

Чтобы отключить мониторинг доступа к файлам, нужно выключить сенсор `z/OS CICS file monitoring` и переключатель `Instrumentation enabled (change needs a process restart)`. Перезапускать регион CICS для вступления настроек в силу не требуется. Транзакция DTAX подхватывает изменения файлового сенсора (вкл/выкл) в течение 5 минут.