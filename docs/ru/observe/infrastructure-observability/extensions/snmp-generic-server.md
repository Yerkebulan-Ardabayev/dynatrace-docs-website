---
title: Расширение SNMP Generic Server
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/snmp-generic-server
scraped: 2026-03-04T21:39:18.259271
---

* Последняя Dynatrace
* Расширение

Мониторинг состояния и производительности серверной инфраструктуры с использованием протокола SNMP в средах, где невозможно развернуть OneAgent.

## Начало работы

### Обзор

Это расширение собирает общеподдерживаемые SNMP-метрики инфраструктуры для мониторинга состояния и использования ресурсов серверов. Метрики собираются через SNMP get-опрос.

### Сценарии использования

* Мониторинг серверной инфраструктуры, где установка OneAgent нецелесообразна.
* Unix-серверы: как альтернатива [Remote Unix](https://www.dynatrace.com/hub/detail/remote-unix-monitoring-20/)
* Windows-серверы: как альтернатива WMI: [Remote Windows](https://www.dynatrace.com/hub/detail/remote-windows-host-monitoring/)

### Информация о совместимости

* Любое устройство, поддерживающее SNMP-опрос и одну или несколько из следующих MIB:

  + HOST-RESOURCES-MIB
  + UCD-SNMP-MIB
  + ENTITY-SENSOR-MIB
* Unix: необходим запущенный программный агент Net-SNMP. [Пример документации Red Hat](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/deployment_guide/sect-system_monitoring_tools-net-snmp)
* Windows: необходимо включить и настроить службу SNMP. [Документация Microsoft](https://learn.microsoft.com/en-us/windows/win32/snmp/snmp-start-page)

## Активация и настройка

Просто активируйте расширение в вашей среде с помощью встроенного Hub и укажите необходимые конфигурации подключения устройств.
Это расширение использует [источник данных Dynatrace SNMP](../../../ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions.md "Узнайте, как создать SNMP-расширение с помощью фреймворка расширений.").

## Подробности

Это расширение собирает метрики SNMP OID из общеподдерживаемых MIB. Большинство наборов функций соответствуют общим записям или таблицам в файлах MIB.

* **SNMPv2-MIB**: Свойства системы, такие как `sysname`, и метрика `sysuptime`.
* **HOST-RESOURCES-MIB**: Мониторинг базовых системных ресурсов — CPU, памяти, хранилища и запущенных процессов на хосте.
* **UCD-SNMP-MIB**: Мониторинг детальных системных метрик — средних значений нагрузки, дискового ввода-вывода.
* **ENTITY-SENSOR-MIB**: Мониторинг физических датчиков — температуры, напряжения, скорости вентиляторов и других.

### Часто задаваемые вопросы

Каково использование пользовательских метрик этого расширения?

Использование пользовательских метрик можно управлять через выбор наборов функций, которые вы включаете. `sysuptime` — единственная обязательная метрика в составе набора функций 'default'. Вы также можете использовать переменные фильтрации для ограничения сбора определённых путей и типов датчиков [Фильтры размерностей](https://community.dynatrace.com/t5/Dynatrace-tips/Extensions-2-0-How-to-use-dimension-filters/m-p/230904).
Все остальные наборы функций основаны на записи объекта или таблице в SNMP MIB. Например, `hr-storage fs` = [HR hrStorageStable](https://mibs.observium.org/mib/HOST-RESOURCES-MIB/#hrStorageTable). Иногда они разделены на несколько для более детального выбора, например `ucd-system-cpu-basic`, `ucd-system-cpu-detailed` и `ucd-system-swap`, которые все относятся к: [UCD systemStats](https://mibs.observium.org/mib/UCD-SNMP-MIB/#systemStats).

Для оценки количества принимаемых метрик можно использовать формулу:

```
Scalar OIDs: 1 metric per OID


#metric_keys_in_fs


Table OIDs: 1 metric per each table entry (e.g., sensor, disk, process, file):


#metric_keys_in_fs * #entries_in_table
```