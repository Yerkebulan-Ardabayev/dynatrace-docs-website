---
title: Radware Alteon Load Balancer extension
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/extensions/radware-alteon-load-balancer
scraped: 2026-03-06T21:31:00.869391
---

# Расширение Radware Alteon Load Balancer

# Расширение Radware Alteon Load Balancer

* Latest Dynatrace
* Extension
* Updated on Feb 25, 2026

Мониторинг устройств и интерфейсов балансировщика нагрузки Radware Alteon через SNMP.

## Начало работы

### Обзор

Это расширение собирает метрики инфраструктуры для мониторинга состояния и производительности устройств Radware Alteon Load Balancer.

![radware-1](https://dt-cdn.net/images/radware-dashboard-resized-2107-7e41f877d2.png)

![radware-2](https://dt-cdn.net/images/radware-device-resized-2085-dbb5255a5b.png)

### Сценарии использования

* Мониторинг важных метрик устройства, таких как время безотказной работы, использование CPU и памяти, а также дополнительных метрик состояния оборудования — температуры, вентиляторов и блоков питания.
* Мониторинг интерфейсов устройства с отчётами по метрикам, включая байты, отбрасывания пакетов, а также входящие и исходящие ошибки.
* Сбор дополнительных данных об устройстве, включая использование виртуальных серверов, статистику HTTP и SSL, пропускную способность и количество сеансов. Полный список отслеживаемых метрик доступен в разделе **Feature Sets**.
* Обнаружение аномалий устройства и предотвращение сбоев.

### Информация о совместимости

* SNMP v2c или SNMP v3
* Dynatrace версии 1.318+

## Активация и настройка

Активируйте расширение в вашей среде через встроенный Hub, укажите необходимую конфигурацию устройства, и настройка завершена.

Подробнее см. [документацию по источнику данных расширения SNMP](/docs/ingest-from/extensions/develop-your-extensions/data-sources/snmp-extensions "Learn how to create an SNMP extension using the Extensions framework.").

## Подробности

Пакет расширения содержит:

* Конфигурацию источника данных SNMP
* Обзорный дашборд (Classic и Platform)
* Унифицированные экраны анализа
* Пользовательские типы топологии, извлечённые из измерений метрик:

  + Radware Alteon Device
  + Radware Alteon Interface
* Файлы SNMP MIB, используемые для мониторинга:

  + IF-MIB
  + ALTEON-CHEETAH-LAYER4-MIB
  + ALTEON-CHEETAH-NETWORK-MIB
  + ALTEON-CHEETAH-SWITCH-MIB
  + ALTEON-ROOT-MIB

### Лицензирование и стоимость

Расчёты основаны на предположении, что вы отслеживаете все метрики для каждого набора функций каждую минуту:

DDU: `(60 + (8 * Interfaces)) * 525.6 DDUs/year, per device`

DPS (точки данных метрик): `(60 + (8 * Interfaces)) * 525,600 metric data points/year, per device`

## Наборы функций

Backend\_Server\_Utilization\_Virtual

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Real-server current sessions | radware\_alteon.slbstat.enh.rserver.currsessions | Текущие сеансы реального сервера. |
| Real-server total sessions | radware\_alteon.slbstat.enh.rserver.totalsessions | Общее количество сеансов реального сервера. |
| Real-server highest sessions | radware\_alteon.slbstat.enh.rserver.highestsessions | Максимальное количество сеансов реального сервера. |
| Real-server total rx/tx octets | radware\_alteon.slbstat.enh.rserver.hc.octets | Общее количество принятых/переданных октетов реального сервера. |
| Real server max concurrent connections | radware\_alteon.slbcur.cfg.realserver.maxconns | Максимально допустимое количество одновременных подключений к реальному серверу в конфигурации. |
| SP current memory | radware\_alteon.spmemusagestats.currentmemory | Текущая память SP в килобайтах. |
| Real-server group current sessions | radware\_alteon.slbstat.enh.group.currsessions | Количество сеансов, обрабатываемых группой реальных серверов в данный момент. |
| Real-server group total sessions | radware\_alteon.slbstat.enh.group.totalsessions | Общее количество сеансов, обработанных группой реальных серверов. |
| Real-server group highest sessions | radware\_alteon.slbstat.enh.group.highestsessions | Максимальное количество сеансов, обработанных группой реальных серверов. |

Throughput\_Physical\_Virtual

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Peak throughput of ports | radware\_alteon.peakthroughputusage.count | Пиковая пропускная способность портов в битах в секунду. |
| Current throughput of ports | radware\_alteon.curthroughputusage.count | Текущая пропускная способность портов в битах в секунду. |

default

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| — | com.dynatrace.extension.network\_device.sysuptime | — |
| — | com.dynatrace.extension.network\_device.cpu\_usage | — |
| — | com.dynatrace.extension.network\_device.memory\_total | — |
| — | com.dynatrace.extension.network\_device.memory\_free | — |
| — | com.dynatrace.extension.network\_device.memory\_used | — |
| — | com.dynatrace.extension.network\_device.if.status | — |
| — | com.dynatrace.extension.network\_device.if.bytes\_in.count | — |
| — | com.dynatrace.extension.network\_device.if.bytes\_out.count | — |
| — | com.dynatrace.extension.network\_device.if.in.discards.count | — |
| — | com.dynatrace.extension.network\_device.if.out.discards.count | — |
| — | com.dynatrace.extension.network\_device.if.in.errors.count | — |
| — | com.dynatrace.extension.network\_device.if.out.errors.count | — |

Session\_Table\_Utilization\_Virtual

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Session table maximum entries | radware\_alteon.slbstat.maint.maximumsessions | Максимальное количество записей в таблице сеансов. |
| Ipv6 session count | radware\_alteon.slbstat.maint.ip6currsessions.count | Количество сеансов для IPv6. |
| Curent sessions in session table | radware\_alteon.slbstat.maint.curbindings | Текущее количество сеансов в таблице сеансов. |

Hardware\_Status\_Physical

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Temperature sensor status | radware\_alteon.temperature.status | Состояние датчика температуры. ok(1), exceed(2) |
| Temperature warning threshold | radware\_alteon.temperature.threshold.warning | Порог предупреждения по температуре |
| Temperature shutdown threshold | radware\_alteon.temperature.threshold.shutdown | Порог выключения по температуре |
| Hardware fan status | radware\_alteon.fan.status | Состояние вентилятора. ok(1), fail(2), unplug(3) |
| Powersupply status | radware\_alteon.powersupply.status | Состояние блока питания. singlePowerSupplyOk(1), firstPowerSupplyFailed(2), secondPowerSupplyFailed(3), doublePowerSupplyOk(4), unknownPowerSupplyFailed(5) |

SSL\_Statistics\_Virtual

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| TCP sessions using SSL service | radware\_alteon.sslslbstat.cursessions | Текущее количество различных TCP-сеансов, использующих службу SSL. |
| Total TCP sessions using SSL service | radware\_alteon.sslslbstat.totalsessions.count | Общее количество различных TCP-сеансов, использующих службу SSL. |
| TCP sessions using SSL service high water mark | radware\_alteon.sslslbstat.highestsessions.count | Максимальное значение текущих сеансов различных TCP-сеансов, использующих службу SSL. |
| SSL handshakes between clients and AAS per second | radware\_alteon.ssloff.newhandShake | Новые SSL-рукопожатия между клиентами и AAS в секунду. |
| New SSL handshakes between Clients and AAS per second (sslOffPerEnhServNewhandShake) | radware\_alteon.ssloffper.enh.serv.newhandshake | Количество новых SSL-рукопожатий между клиентами и AAS в секунду для данной виртуальной службы. |
| Number of expired SSL certificates per second for virtual service (sslOffPerEnhServExpiredCertificates) | radware\_alteon.ssloffper.enh.serv.expiredcertificates | Количество просроченных SSL-сертификатов в секунду для виртуальной службы. |

Advanced interfaces

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| — | com.dynatrace.extension.network\_device.if.lastchange | — |

High\_Availability\_Physical

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| High availability (HA) service group state | radware\_alteon.ha.group.state | Состояние группы служб высокой доступности (HA) |
| High availability (HA) switch state | radware\_alteon.ha.switch.state | Состояние коммутатора высокой доступности (HA) |
| High availability (HA) mode | radware\_alteon.ha.curcfg.mode | Режим высокой доступности (HA) |

Per\_Device\_HTTP\_Statistics\_Virtual

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| HTTP 2.0 connection count | radware\_alteon.httpstatsumm.http20connection.count | Количество подключений HTTP 2.0. |
| HTTP 1.1 connection count | radware\_alteon.httpstatsumm.http11connection.count | Количество подключений HTTP 1.1. |
| HTTP 1.0 connection count | radware\_alteon.httpstatsumm.http10connection.count | Количество подключений HTTP 1.0. |
| HTTP 2.0 connection peak count | radware\_alteon.httpstatsumm.http20connection.peak.count | Пиковое количество подключений HTTP 2.0. |
| HTTP 1.1 connection peak count | radware\_alteon.httpstatsumm.http11connection.peak.count | Пиковое количество подключений HTTP 1.1. |
| HTTP 1.0 connection peak count | radware\_alteon.httpstatsumm.http10connection.peak.count | Пиковое количество подключений HTTP 1.0. |
| HTTP 2.0 request count | radware\_alteon.httpstatsumm.http20connection.request.count | Количество запросов HTTP 2.0. |
| HTTP 1.1 request count | radware\_alteon.httpstatsumm.http11connection.request.count | Количество запросов HTTP 1.1. |
| HTTP 1.0 request count | radware\_alteon.httpstatsumm.http10connection.request.count | Количество запросов HTTP 1.0. |
| HTTP transactions per second | radware\_alteon.httptranssumm.trans.rate | HTTP-транзакций в секунду. |

Software\_Status\_SP

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| SP CPU utilization | com.dynatrace.extension.network\_device.sp.cpu\_usage | Утилизация CPU SP |

Virtual\_Server\_Utilization\_Virtual

| Название метрики | Ключ метрики | Описание |
| --- | --- | --- |
| Virtual server current sessions | radware\_alteon.slbstat.enh.vserver.currsessions | Количество сеансов, обрабатываемых виртуальным сервером в данный момент. |
| Virtual server total sessions | radware\_alteon.slbstat.enh.vserver.totalsessions | Общее количество сеансов, обработанных виртуальным сервером. |
| Virtual server highest sessions handled | radware\_alteon.slbstat.enh.vserver.highestsessions | Максимальное количество сеансов, обработанных виртуальным сервером. |
| Total octets received and transmitted by the virtual server | radware\_alteon.slbstat.enh.vserver.hc.octets | Общее количество октетов, принятых и переданных виртуальным сервером. |
| Sessions handled by the virtual server | radware\_alteon.slbstat.enh.vserver.sessions | Количество сеансов, обработанных виртуальным сервером в секунду. |
| Real server runtime status per virtual server | radware\_alteon.slbstat.enh.vserver.real.status | Состояние реального сервера во время выполнения для виртуальной службы. (0)Up, (1)Down, (2)Admin-Down, (3)Warning, (4)Shutdown, (5)Error |
| Backend server concurrent connections for virtual service | radware\_alteon.commng.enh.perservstats.servconn | Количество одновременных подключений к серверному серверу для виртуальной службы. |
| Virtual service client requests passed to AX | radware\_alteon.commng.enh.perservstats.clireq | Количество клиентских запросов, переданных в AX для виртуальной службы. |
| Virtual service security policy peak bandwidth (secPolPerServBwPeak) | radware\_alteon.secpol.perserv.bw.peak | Статистика политики безопасности виртуальной службы — пиковое значение пропускной способности. |
| Virtual service security policy bandwidth ( secPolPerServBwCurVal) | radware\_alteon.secpol.perserv.bw.curval | Статистика политики безопасности виртуальной службы — текущее значение пропускной способности. |
| Virtual service security policy PPS current (secPolPerServPPSCurVal) | radware\_alteon.secpol.perserv.pps.curval | Статистика политики безопасности виртуальной службы — текущее значение PPS. |
| Virtual service security policy PPS peak (secPolPerServPPSPeak) | radware\_alteon.secpol.perserv.pps.peak | Статистика политики безопасности виртуальной службы — пиковое значение PPS. |
| Virtual service security policy CPS current (secPolPerServCPSCurVal) | radware\_alteon.secpol.perserv.cps.curval | Статистика политики безопасности виртуальной службы — текущее значение CPS. |
| Virtual service security policy CPS peak (secPolPerServCPSPeak) | radware\_alteon.secpol.perserv.cps.peak | Статистика политики безопасности виртуальной службы — пиковое значение CPS. |
| Virtual service security policy latency current (secPolPerServLatencyCurVal) | radware\_alteon.secpol.perserv.latency.curval | Статистика политики безопасности виртуальной службы — текущее значение задержки. |
| Virtual service security policy latency peak (secPolPerServLatencyPeak) | radware\_alteon.secpol.perserv.latency.peak | Статистика политики безопасности виртуальной службы — пиковое значение задержки. |

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Обзор в Dynatrace Hub

Мониторинг балансировщиков нагрузки Radware Alteon через SNMP.](https://www.dynatrace.com/hub/detail/radware-alteon-load-balancer/)
