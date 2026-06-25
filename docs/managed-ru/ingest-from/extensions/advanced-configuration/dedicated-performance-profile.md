---
title: Настройка выделенного профиля производительности
source: https://docs.dynatrace.com/managed/ingest-from/extensions/advanced-configuration/dedicated-performance-profile
scraped: 2026-05-12T12:11:31.645859
---

# Настройка выделенного профиля производительности

# Настройка выделенного профиля производительности

* Практическое руководство
* Чтение: 1 мин
* Обновлено 28 апреля 2026 г.

Выделенный профиль производительности обеспечивает мощную оптимизацию производительности для окружения Dynatrace. С его помощью можно расширить вычислительные возможности хоста ActiveGate для улучшения возможностей мониторинга и анализа.

## Ограничения

* Выделенный профиль производительности следует использовать на мощных инстансах, например `C6i.2xlarge` (AWS), `Standard_F8s_v2` (Azure) или `c2-standard-8` (GCP).
* При использовании выделенного профиля производительности никакая другая функциональность ActiveGate не должна работать одновременно с расширениями.
* При использовании групп ActiveGate убедитесь, что ко всем ActiveGate в группе применена одинаковая пользовательская конфигурация для выбранного профиля производительности.

## Конфигурация

Настройка ActiveGate для выделенного профиля производительности

1. Ограничьте функциональность ActiveGate только расширениями.

   agctl

   custom.properties

   ActiveGate версии 1.333+

   Используйте [agctl](/managed/ingest-from/dynatrace-activegate/agctl-command-line-interface#modules "Узнайте, как использовать agctl для настройки и управления ActiveGate из командной строки") для отключения модулей:

   ```
   agctl modules disable aws_monitoring,azure_monitoring,cloudfoundry_monitoring,debugging,kubernetes_monitoring,log_analytics_collector,vmware_monitoring,dbAgent,zremote,synthetic,metrics_ingest,DumpSupported,MSGrouter,otlp_ingest
   ```

   Измените файл `custom.properties`:

   ```
   [aws_monitoring]



   aws_monitoring_enabled = false



   [azure_monitoring]



   azure_monitoring_enabled = false



   [cloudfoundry_monitoring]



   cloudfoundry_monitoring_enabled = false



   [debugging]



   debugging_enabled = false



   [kubernetes_monitoring]



   kubernetes_monitoring_enabled = false



   [log_analytics_collector]



   log_analytics_collector_enabled = false



   [vmware_monitoring]



   vmware_monitoring_enabled = false



   [dbAgent]



   dbAgent_enabled = false



   [zremote]



   zremote_enabled = false



   [synthetic]



   synthetic_enabled = false



   [metrics_ingest]



   metrics_ingest_enabled = false



   [collector]



   DumpSupported = false



   [collector]



   MSGrouter = false



   [otlp_ingest]



   otlp_ingest_enabled = false
   ```
2. Измените настройки памяти ActiveGate через файл `launcheruserconfig.conf`.

   ```
   -java.xmx.absolute_part=2000



   -java.xmx.relative_part=0
   ```
3. [Перезапустите ActiveGate](/managed/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Узнайте, как запустить, остановить и перезапустить ActiveGate на Windows или Linux.") для применения изменений конфигурации.
4. [Задайте профиль производительности ActiveGate](/managed/ingest-from/extensions/concepts#performance-profile "Подробнее о концепции Dynatrace Extensions.") как `Dedicated limits`.

## Связанные темы

* [О расширениях](/managed/ingest-from/extensions/concepts "Подробнее о концепции Dynatrace Extensions.")