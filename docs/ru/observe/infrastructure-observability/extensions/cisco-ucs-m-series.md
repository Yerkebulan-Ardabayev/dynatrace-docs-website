---
title: Расширение Cisco UCS M-Series
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/cisco-ucs-m-series
scraped: 2026-03-06T21:26:37.150221
---

# Расширение Cisco UCS M-Series

# Расширение Cisco UCS M-Series

* Последняя Dynatrace
* Расширение
* Опубликовано 21 февраля 2025 г.

Получите информацию о ваших устройствах Cisco UCS M-Series.

## Начало работы

### Обзор

Мониторинг устройств Cisco UCS M-Series с данными, собранными через [UCS Manager API](https://www.cisco.com/c/en/us/td/docs/unified_computing/ucs/sw/api/b_ucs_api_book/b_ucs_api_book_chapter_00.html).

Это расширение собирает метрики инфраструктуры для мониторинга состояния и производительности устройств Cisco UCS M-Series и их компонентов, включая CPU, вентиляторы, блоки питания, интерфейсы и другие.

### Сценарии использования

* Мониторинг сигналов состояния шасси и аппаратных компонентов, включая температуру/ток CPU, вентиляторы, модули вентиляторов, БП, массивы памяти, контроллеры хранения, локальные диски и свойства коммутационных плат.
* Отслеживание трафика Ethernet и счётчиков ошибок для портов UCS, включая принятые/переданные байты/пакеты, счётчики пауз/ошибок/коллизий и метрики использования/запаса.
* Наблюдение за метриками среды и системы Fabric Interconnect.
* Анализ поведения аплинков и пулов через метрики для пулов Ethernet, серверных и сетевых портов.
* Обнаружение аномалий устройств и предотвращение сбоев.

### Информация о совместимости

* Dynatrace версии 1.318+
* Устройство Cisco UCS M-Series с доступом к Cisco UCS Manager XML API.

### Требования

* Учётная запись с правами только на чтение для запросов UCS Manager XML API, предоставленная расширению в виде имени пользователя/пароля.
* Сетевой доступ от ActiveGate к конечной точке UCS.
* Возможность для настроенного пользователя выполнять API-операции: `aaaLogin`, `configResolveClass`, `aaaLogout`.
* Конкретные запрашиваемые классы зависят от включённых наборов функций:

  + M-Series CPU: `processorUnit`, `processorEnvStats`
  + M-Series Fan Module: `equipmentFanModule`, `equipmentFan`
  + M-Series Fan: `equipmentFan`
  + M-Series Local Disk: `storageLocalDisk`
  + M-Series Memory Array: `memoryArray`
  + M-Series Power Supply: `equipmentPsu`
  + M-Series Storage Controller: `storageController`
  + M-Series Ethernet Port: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series EthPortPool: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series NetworkPortPool: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series ServerPortPool: `etherPIo`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series Fabric Interconnect: `networkElement`, `swEnvStats`, `swSystemStats`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series Fabric Ethernet LAN Port Channel: `fabricEthLanPc`, `etherErrStats`, `etherLossStats`, `etherPauseStats`, `etherRxStats`, `etherTxStats`
  + M-Series Host Ethernet Interface: `adaptorHostEthIf`, `adaptorEthPortStats`, `adaptorVnicStats`
  + M-Series Organization: `orgOrg`
  + M-Series Rack Server: `computeRackUnit`
  + M-Series Service Profile: `lsServer`, `adaptorEthPortStats`, `adaptorVnicStats`
  + M-Series Switch Card: `equipmentSwitchCard`

## Активация и настройка

Активируйте расширение в вашей среде из Dynatrace Hub, настройте параметры подключения к вашей конечной точке UCS и выберите наборы функций для сбора.

## Подробности

Пакет расширения содержит:

* Обзорные панели (классическая и платформенная)
* Экраны анализа, интегрированные с ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**
* Унифицированные страницы анализа
* Пользовательские типы топологии, извлечённые из размерностей метрик:

  + Cisco UCS M-Series CPU
  + Cisco UCS M-Series Fan Module
  + Cisco UCS M-Series Fan
  + Cisco UCS M-Series Local Disk
  + Cisco UCS M-Series Memory Array
  + Cisco UCS M-Series Power Supply
  + Cisco UCS M-Series Storage Controller
  + Cisco UCS M-Series Ethernet Port
  + Cisco UCS M-Series Ethernet Port Pool
  + Cisco UCS M-Series Network Port Pool
  + Cisco UCS M-Series Server Port Pool
  + Cisco UCS M-Series Fabric Interconnect
  + Cisco UCS M-Series Fabric Ethernet LAN PC
  + Cisco UCS M-Series Host Ethernet Interface
  + Cisco UCS M-Series Organization
  + Cisco UCS M-Series Rack
  + Cisco UCS M-Series Service Profile
  + Cisco UCS M-Series Switch Card

### Лицензирование и стоимость

#### Лицензирование DPS

Потребление [лицензии DPS](/docs/license "О Dynatrace Platform Subscription (DPS) — модели лицензирования для всех возможностей Dynatrace.") основано на принимаемых точках данных метрик. Следующая формула даёт приблизительный годовой объём приёма при включении всех наборов функций и запуске расширения каждую минуту:

```
(2 * # of CPUs)



+ (1 * # of Fan Modules)



+ (1 * # of Fans)



+ (1 * # of Local Disks)



+ (1 * # of Memory Arrays)



+ (1 * # of Power Supplies)



+ (1 * # of Storage Controllers)



+ (38 * # of Ethernet Ports)



+ (12 * # of Ethernet Port Pools)



+ (12 * # of Network Port Pools)



+ (12 * # of Server Port Pools)



+ (45 * # of Fabric Interconnects)



+ (34 * # of Fabric Ethernet LAN PCs)



+ (20 * # of Host Ethernet Interfaces)



+ (1 * # of Organizations)



+ (1 * # of Racks)



+ (20 * # of Service Profiles)



+ (1 * # of Switch Cards)



* 525,600 metric data points/year
```

#### Классическое лицензирование

Для [классических лицензий Dynatrace](/docs/license/monitoring-consumption-classic "Понимание расчёта потребления мониторинга Dynatrace для классического лицензирования.") приём метрик потребляет Davis Data Units (DDU) со скоростью 0,001 DDU на точку данных метрики.
Подробнее см. [DDU для метрик](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Понимание расчёта потребления и стоимости Davis Data Units для мониторинга метрик.").

Для оценки годового потребления DDU умножьте результат формулы выше на 0,001.