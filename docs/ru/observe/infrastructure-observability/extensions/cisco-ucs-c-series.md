---
title: Расширение Cisco UCS C-Series
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/cisco-ucs-c-series
scraped: 2026-03-06T21:36:04.473139
---

* Последняя Dynatrace
* Расширение

Получите информацию о ваших устройствах Cisco UCS C-Series.

## Начало работы

### Обзор

Мониторинг устройств Cisco UCS C-Series с данными, собранными через [UCS Manager XML API](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/api/b_ucs_api_book/b_ucs_api_book_chapter_00.html).

Это расширение собирает метрики инфраструктуры и события для аппаратных компонентов Cisco UCS C-Series, включая CPU, модули вентиляторов, вентиляторы, память, хранилище, блоки питания, сетевые адаптеры и интерфейсы VIC.

### Сценарии использования

* Мониторинг сигналов состояния аппаратных компонентов — CPU, модулей вентиляторов/вентиляторов, массивов/модулей памяти, контроллеров хранения, локальных дисков, батарей RAID, блоков питания и виртуальных дисков.
* Наблюдение за подключением и состоянием адаптеров, внешних интерфейсов, vHBA и vNIC.
* Обнаружение сбоев UCS и создание событий ошибок Dynatrace для ускоренной сортировки проблем.

### Информация о совместимости

* Dynatrace версии 1.318+
* Устройство Cisco UCS C-Series с доступом к Cisco UCS Manager XML API.

### Требования

* Учётная запись с правами только на чтение для запросов UCS Manager XML API, предоставленная расширению в виде имени пользователя/пароля.
* Сетевой доступ от ActiveGate к конечной точке UCS.
* Возможность для настроенного пользователя выполнять API-операции: `aaaLogin`, `configResolveClass`, `aaaLogout`.
* Конкретные запрашиваемые классы зависят от включённых наборов функций:

  + C-Series Faults: `faultInst`
  + C-Series CPU: `processorUnit`
  + C-Series External Interface: `networkAdapterEthIf`
  + C-Series Fan Module / C-Series Fan Module (voltage): `equipmentFanModule`
  + C-Series Fan / C-Series Fan (voltage): `equipmentFan`
  + C-Series Local Disk / C-Series Local Disk (predictive failure count): `storageLocalDisk`
  + C-Series Memory Array: `memoryArray`
  + C-Series Memory Unit: `memoryUnit`
  + C-Series Network Adapter: `networkAdapterUnit`
  + C-Series Power Supply / C-Series Power Supply (voltage): `equipmentPsu`
  + C-Series Raid Battery: `storageRaidBattery`
  + C-Series Storage Controller: `storageController`
  + C-Series VIC Adapter: `adaptorUnit`
  + C-Series VIC External Interface: `adaptorExtEthIf`
  + C-Series VIC vHBA: `adaptorHostFcIf`
  + C-Series VIC vNIC: `adaptorHostEthIf`
  + C-Series Virtual Drive: `storageVirtualDrive`

## Активация и настройка

Активируйте расширение в вашей среде из Dynatrace Hub, настройте параметры подключения к вашей конечной точке UCS и выберите наборы функций для сбора.

## Подробности

Пакет расширения содержит:

* Обзорные панели (классическая и платформенная)
* Экраны анализа, интегрированные с ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**
* Унифицированные страницы анализа
* Пользовательские типы топологии, извлечённые из размерностей метрик:

  + Cisco UCS C-Series CPU
  + Cisco UCS C-Series External Interface
  + Cisco UCS C-Series Fan Module
  + Cisco UCS C-Series Fan
  + Cisco UCS C-Series Local Disk
  + Cisco UCS C-Series Memory Array
  + Cisco UCS C-Series Memory Unit
  + Cisco UCS C-Series Network Adapter
  + Cisco UCS C-Series Power Supply
  + Cisco UCS C-Series Raid Battery
  + Cisco UCS C-Series Storage Controller
  + Cisco UCS C-Series VIC Adapter
  + Cisco UCS C-Series VIC External Interface
  + Cisco UCS C-Series VIC vHBA
  + Cisco UCS C-Series VIC vNIC
  + Cisco UCS C-Series Virtual Drive
  + Cisco UCS C-Series Rack

### Лицензирование и стоимость

#### Лицензирование DPS

Потребление [лицензии DPS](../../../license.md "О Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace.") основано на принимаемых точках данных метрик. Следующая формула даёт приблизительный годовой объём приёма при включении всех наборов функций и запуске расширения каждую минуту:

```
((2 * # of CPUs)


+ (1 * # of External Interfaces)


+ (5 * # of Fan Modules)


+ (5 * # of Fans)


+ (5 * # of Local Disks)


+ (4 * # of Memory Arrays)


+ (2 * # of Memory Units)


+ (1 * # of Network Adapters)


+ (5 * # of Power Supplies)


+ (4 * # of Raid Batteries)


+ (1 * # of Storage Controllers)


+ (1 * # of VIC Adapters)


+ (1 * # of VIC External Interfaces)


+ (1 * # of VIC vHBAs)


+ (1 * # of VIC vNICs)


+ (2 * # of Virtual Drives))


* 525,600 metric data points/year
```

#### Классическое лицензирование

Для [классических лицензий Dynatrace](../../../license/monitoring-consumption-classic.md "Понимание расчёта потребления мониторинга Dynatrace для классического лицензирования.") приём метрик потребляет Davis Data Units (DDU) со скоростью 0,001 DDU на точку данных метрики.
Подробнее см. [DDU для метрик](../../../license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation.md "Понимание расчёта потребления и стоимости Davis Data Units для мониторинга метрик.").

Для оценки годового потребления DDU умножьте результат формулы выше на 0,001.