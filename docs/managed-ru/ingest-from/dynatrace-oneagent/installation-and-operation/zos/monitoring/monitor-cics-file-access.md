---
title: Мониторинг доступа к файлам в приложениях CICS
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access
scraped: 2026-05-12T12:04:56.828972
---

# Мониторинг доступа к файлам в приложениях CICS

# Мониторинг доступа к файлам в приложениях CICS

* Чтение: 1 мин
* Опубликовано 13 января 2023 г.

С Dynatrace можно мониторить вызовы доступа к файлам VSAM и BDAM из ваших приложений CICS через модуль CICS. Каждый файл, к которому обращаются в регионе CICS, представлен как сервис базы данных на странице [Databases](/managed/observe/infrastructure-observability/databases "Отслеживайте производительность и ресурсы базы данных, чтобы создавать и поддерживать высокопроизводительную и доступную инфраструктуру приложений."), вместе с такими метриками, как время отклика, частота отказов и пропускная способность.

![Доступ к файлам на странице Database](https://dt-cdn.net/images/file-sensor-db-3052-6d5ec51cdd.png)

Доступ к файлам на странице Database

Страница [Distributed traces](/managed/observe/application-observability/distributed-traces "Получите наблюдаемость в высоко распределённых, облачно-нативных архитектурах, чтобы эффективно трассировать и анализировать транзакции в реальном времени.") отображает операции с файлами и логические имена файлов, к которым обращаются на [уровне методов PurePath](/managed/observe/application-observability/distributed-traces/use-cases/segment-request "Повышайте производительность распределённой системы, сегментируя запросы с медленным временем отклика через Service flow и анализируя их распределённые трассировки."). Операции с файлами агрегируются по логическому имени файла (например, на изображении ниже операция `READNEXT` была выполнена 21 раз над файлом `EXMPCAT`).

![Вызовы доступа к файлам на странице Distributed traces](https://dt-cdn.net/images/file-sensor-pp-3142-684de155b6.png)

Вызовы доступа к файлам на странице Distributed traces

## Начало работы

Чтобы начать мониторинг вызовов доступа к файлам из ваших приложений CICS

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Активируйте [возможность OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управление возможностями OneAgent глобально и для каждой группы процессов.") **z/OS CICS file monitoring sensor**.
3. Перезапустите регион CICS или позвольте [DTAX-транзакции](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Управление модулем CICS через DTAX-транзакции.") подхватить новые настройки конфигурации в следующем 5-минутном интервале.

## Удалённые файлы

В прикладной программе, если file control API содержит выражение `SYSID` с удалённым `SYSID`, файл распознаётся как удалённый. Однако, если файл определён как удалённый в определении `CEDA`, модуль CICS не распознаёт файл как удалённый.

## Отключение мониторинга доступа к файлам

Чтобы отключить мониторинг доступа к файлам, переключите сенсор `z/OS CICS file monitoring` и `Instrumentation enabled (change needs a process restart)` в положение off. Регион CICS перезапускать не требуется, чтобы настройки вступили в силу. DTAX-транзакция подхватывает изменения file sensor (вкл/выкл) в течение 5 минут.