---
title: Метрики хоста
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/reference/metrics
scraped: 2026-03-05T21:36:56.739400
---

# Метрики хоста

# Метрики хоста

* Classic
* Справочник
* 7 мин. чтения
* Опубликовано 4 ноября 2024 г.

Это справочный список метрик, используемых для хостов, с подробной информацией об их доступности в операционных системах Windows, Linux и AIX.

Вы также можете проверить, доступны ли метрики в режиме мониторинга Discovery. Подробнее см. [Режим Discovery](/docs/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

## Метрики CPU и памяти

Метрики, представляющие использование процессора и оперативной памяти.

### CPU

| Название метрики | Классический ключ метрики | Ключ метрики на Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Idle | builtin:host.cpu.idle | dt.host.cpu.idle |  |  |  |  |
| User | builtin:host.cpu.user | dt.host.cpu.user |  |  |  |  |
| IO wait | builtin:host.cpu.iowait | dt.host.cpu.iowait |  |  |  |  |
| Other | builtin:host.cpu.other | dt.host.cpu.other |  |  |  |  |
| Steal | builtin:host.cpu.steal | dt.host.cpu.steal |  |  |  |  |
| System | builtin:host.cpu.system | dt.host.cpu.system |  |  |  |  |
| System Load | builtin:host.cpu.load | dt.host.cpu.load |  |  |  |  |
| System load 5 minutes | builtin:host.cpu.load5m | dt.host.cpu.load5m |  |  |  |  |
| System load 15 minutes | builtin:host.cpu.load15m | dt.host.cpu.load15m |  |  |  |  |
| CPU Usage % | builtin:host.cpu.usage | dt.host.cpu.usage |  |  |  |  |
| Logical / Physical CPU cores |  |  |  |  |  |  |
| entc | builtin:host.cpu.entc | dt.host.cpu.entc |  |  |  |  |
| physc | builtin:host.cpu.physc | dt.host.cpu.physc |  |  |  |  |
| entConfigured | builtin:host.cpu.entConfig | dt.host.cpu.ent\_config |  |  |  |  |
| AIX: запущенные потоки ядра | builtin:host.kernelThreads.running | dt.host.kernel\_threads.running |  |  |  |  |
| AIX: заблокированные потоки ядра | builtin:host.kernelThreads.blocked | dt.host.kernel\_threads.blocked |  |  |  |  |
| AIX: заблокированные потоки ядра — ожидание сообщения I/O | builtin:host.kernelThreads.ioMessageWait | dt.host.kernel\_threads.io\_message\_wait |  |  |  |  |
| AIX: заблокированные потоки ядра — ожидание события I/O | builtin:host.kernelThreads.ioEventWait | dt.host.kernel\_threads.io\_event\_wait |  |  |  |  |

### Память

| Название метрики | Классический ключ метрики | Ключ метрики на Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Total | builtin:host.mem.total | Unsupported |  |  |  |  |
| Used | builtin:host.mem.used | dt.host.memory.used |  |  |  |  |
| Available | builtin:host.mem.avail.bytes | dt.host.memory.avail.bytes |  |  |  |  |
| Memory available % | builtin:host.mem.avail.pct | dt.host.memory.avail.percent |  |  |  |  |
| Memory used % | builtin:host.mem.usage | dt.host.memory.usage |  |  |  |  |
| Kernel | builtin:host.mem.kernel | dt.host.memory.kernel |  |  |  |  |
| memoryReclaimable | builtin:host.mem.recl | dt.host.memory.recl |  |  |  |  |
| Page Faults | builtin:host.mem.avail.pfps | dt.host.memory.avail.pfps |  |  |  |  |
| Swap Used | builtin:host.mem.swap.used | dt.host.memory.swap.used |  |  |  |  |
| Swap Total | builtin:host.mem.swap.total | dt.host.memory.swap.total |  |  |  |  |
| Swap Available | builtin:host.mem.swap.avail | dt.host.memory.swap.avail |  |  |  |  |

### Дескрипторы файлов / дескрипторы

| Название метрики | Классический ключ метрики | Ключ метрики на Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| File descriptors used | builtin:host.handles.fileDescriptorsUsed | dt.host.handles.file\_descriptors\_used |  |  |  |  |
| File descriptors max | builtin:host.handles.fileDescriptorsMax | dt.host.handles.file\_descriptors\_max |  |  |  |  |

## Метрики диска

Метрики, представляющие использование диска. Обратите внимание на разграничение между сетевыми и локальными дисками в Linux.

| Название метрики | Классический ключ метрики | Ключ метрики на Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Total[1](#fn-1-1-def) |  |  |  |  | [2](#fn-1-2-def) |  |
| Disk used | builtin:host.disk.used | dt.host.disk.used |  |  | [2](#fn-1-2-def) |  |
| Disk used % | builtin:host.disk.usedPct | dt.host.disk.used.percent |  |  | [2](#fn-1-2-def) |  |
| Disk available[1](#fn-1-1-def) | builtin:host.disk.avail | dt.host.disk.avail |  |  | [2](#fn-1-2-def) |  |
| Disk available %[1](#fn-1-1-def) | builtin:host.disk.free | dt.host.disk.free |  |  | [2](#fn-1-2-def) |  |
| Read (Bytes/s) | builtin:host.disk.bytesRead | dt.host.disk.bytes\_read | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Write (Bytes/s) | builtin:host.disk.bytesWritten | dt.host.disk.bytes\_written | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Inodes total | builtin:host.disk.inodesTotal | dt.host.disk.inodes\_total |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Inodes available % | builtin:host.disk.inodesAvail | dt.host.disk.inodes\_avail |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Reads (IOPS) | builtin:host.disk.readOps | dt.host.disk.read\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Writes (IOPS) | builtin:host.disk.writeOps | dt.host.disk.write\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Disk read time | builtin:host.disk.readTime | dt.host.disk.read\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Disk write time | builtin:host.disk.writeTime | dt.host.disk.write\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Disk utilization time | builtin:host.disk.utilTime | dt.host.disk.util\_time | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |
| Disk average queue length | builtin:host.disk.queueLength | dt.host.disk.queue\_length | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |

1

OneAgent версии 1.313+. Метрики доступного и общего размера диска не отправляются, если общий размер диска превышает 1024 петабайта (1024 ПБ).

2

Только локальные диски

3

Исключая GPFS

4

Начиная с OneAgent 1.307

5

Исключая CIFS

6

Только GPFS

7

Исключая CIFS/GPFS

8

Исключая NFS/CIFS/GPFS

## Сетевые метрики по сетевому интерфейсному контроллеру (NIC)

Метрики, представляющие использование сетевых интерфейсных контроллеров на хосте. Они собираются сетевым модулем OneAgent.

| Название метрики | Классический ключ метрики | Ключ метрики на Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Bytes Received / s | builtin:host.net.nic.bytesRx | dt.host.net.nic.bytes\_rx |  |  |  |  |
| Bytes Sent / s | builtin:host.net.nic.bytesTx | dt.host.net.nic.bytes\_tx |  |  |  |  |
| Packets Received / s | builtin:host.net.nic.packets.rx | dt.host.net.nic.packets.rx |  |  |  |  |
| Packets Sent / s | builtin:host.net.nic.packets.tx | dt.host.net.nic.packets.tx |  |  |  |  |
| Dropped Packets Out / s | builtin:host.net.nic.packets.droppedTx | dt.host.net.nic.packets.dropped\_tx |  |  |  |  |
| Dropped Packets In / s | builtin:host.net.nic.packets.droppedRx | dt.host.net.nic.packets.dropped\_rx |  |  |  |  |
| Errors Out / s | builtin:host.net.nic.packets.errorsTx | dt.host.net.nic.packets.errors\_tx |  |  |  |  |
| Errors In / s | builtin:host.net.nic.packets.errorsRx | dt.host.net.nic.packets.errors\_rx |  |  |  |  |
| Send Utilization | builtin:host.net.nic.linkUtilTx | dt.host.net.nic.link\_util\_tx |  |  |  |  |
| Received Utilization | builtin:host.net.nic.linkUtilRx | dt.host.net.nic.link\_util\_rx |  |  |  |  |

## Доступность

| Название метрики | Классический ключ метрики | Ключ метрики на Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Host availability | builtin:host.availability.state | dt.host.availability |  |  |  |  |
| Host uptime | builtin:host.uptime | builtin:host.uptime |  |  |  |  |

## Прочее

| Название метрики | Классический ключ метрики | Ключ метрики на Grail |
| --- | --- | --- |
| Host Time Offset | builtin:host.la.to | unsupported |
