---
title: Выделенная конфигурация профиля производительности
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/dedicated-performance-profile
scraped: 2026-03-06T21:29:41.296118
---

# Dedicated performance profile configuration


Выделенный профиль производительности предлагает мощную оптимизацию производительности для вашей среды Dynatrace. С выделенным профилем вы можете расширить вычислительные возможности хоста ActiveGate для улучшения возможностей мониторинга и анализа.

## Ограничения

* Выделенный профиль производительности следует использовать на мощных экземплярах, таких как `C6i.2xlarge`.
* При использовании выделенного профиля производительности никакие другие функции ActiveGate не должны работать одновременно с расширениями.
* Если вы используете группы ActiveGate, убедитесь, что ко всем ActiveGate в группе применена одинаковая пользовательская конфигурация для выбранного профиля производительности.

## Конфигурация

Для настройки ActiveGate для выделенного профиля производительности:

1. Измените файл `custom.properties`, чтобы ограничить функциональность ActiveGate только расширениями Extensions 2.0.

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


   [beacon_forwarder]


   beacon_forwarder_enabled = false


   [metrics_ingest]


   metrics_ingest_enabled = false


   [collector]


   DumpSupported = false


   [collector]


   MSGrouter = false


   [otlp_ingest]


   otlp_ingest_enabled = false


   [collector]


   restInterface = false
   ```
2. Измените настройки памяти ActiveGate с помощью файла `launcheruserconfig.conf`.

   ```
   -java.xmx.absolute_part=2000


   -java.xmx.relative_part=0
   ```
3. [Перезапустите ActiveGate](../../dynatrace-activegate/operation/stop-restart-activegate.md "Узнайте, как запустить, остановить и перезапустить ActiveGate в Windows или Linux."), чтобы применить изменения конфигурации.
4. [Задайте профиль производительности ActiveGate](../concepts.md#performance-profile "Узнайте больше о концепции расширений Dynatrace.") на `Dedicated limits`.

## Связанные темы

* [О расширениях](../concepts.md "Узнайте больше о концепции расширений Dynatrace.")
