---
title: Метрики хостов
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/hosts/reference/metrics
scraped: 2026-03-05T21:36:56.739400
---

# Метрики хостов


* Classic
* Справочник
* Чтение: 7 мин
* Опубликовано 4 ноября 2024 г.

Это справочный список метрик, используемых для хостов, с информацией об их доступности в операционных системах Windows, Linux и AIX.

Вы также можете проверить, доступны ли метрики в режиме мониторинга Discovery. Подробнее см. в разделе [Режим Discovery](../../../../platform/oneagent/monitoring-modes/monitoring-modes.md#discovery "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

## Метрики процессора и памяти

Метрики, отражающие использование процессора и оперативной памяти.

### Процессор

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Простой | builtin:host.cpu.idle | dt.host.cpu.idle |  |  |  |  |
| Пользовательский | builtin:host.cpu.user | dt.host.cpu.user |  |  |  |  |
| Ожидание ввода-вывода | builtin:host.cpu.iowait | dt.host.cpu.iowait |  |  |  |  |
| Прочее | builtin:host.cpu.other | dt.host.cpu.other |  |  |  |  |
| Steal | builtin:host.cpu.steal | dt.host.cpu.steal |  |  |  |  |
| Системный | builtin:host.cpu.system | dt.host.cpu.system |  |  |  |  |
| Системная нагрузка | builtin:host.cpu.load | dt.host.cpu.load |  |  |  |  |
| Системная нагрузка за 5 минут | builtin:host.cpu.load5m | dt.host.cpu.load5m |  |  |  |  |
| Системная нагрузка за 15 минут | builtin:host.cpu.load15m | dt.host.cpu.load15m |  |  |  |  |
| Использование процессора % | builtin:host.cpu.usage | dt.host.cpu.usage |  |  |  |  |
| Логические / физические ядра процессора |  |  |  |  |  |  |
| entc | builtin:host.cpu.entc | dt.host.cpu.entc |  |  |  |  |
| physc | builtin:host.cpu.physc | dt.host.cpu.physc |  |  |  |  |
| entConfigured | builtin:host.cpu.entConfig | dt.host.cpu.ent\_config |  |  |  |  |
| Потоки ядра AIX: выполняющиеся | builtin:host.kernelThreads.running | dt.host.kernel\_threads.running |  |  |  |  |
| Потоки ядра AIX: заблокированные | builtin:host.kernelThreads.blocked | dt.host.kernel\_threads.blocked |  |  |  |  |
| Потоки ядра AIX: ожидание сообщения ввода-вывода | builtin:host.kernelThreads.ioMessageWait | dt.host.kernel\_threads.io\_message\_wait |  |  |  |  |
| Потоки ядра AIX: ожидание события ввода-вывода | builtin:host.kernelThreads.ioEventWait | dt.host.kernel\_threads.io\_event\_wait |  |  |  |  |

### Память

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Всего | builtin:host.mem.total | Unsupported |  |  |  |  |
| Использовано | builtin:host.mem.used | dt.host.memory.used |  |  |  |  |
| Доступно | builtin:host.mem.avail.bytes | dt.host.memory.avail.bytes |  |  |  |  |
| Доступная память % | builtin:host.mem.avail.pct | dt.host.memory.avail.percent |  |  |  |  |
| Использованная память % | builtin:host.mem.usage | dt.host.memory.usage |  |  |  |  |
| Ядро | builtin:host.mem.kernel | dt.host.memory.kernel |  |  |  |  |
| Освобождаемая память | builtin:host.mem.recl | dt.host.memory.recl |  |  |  |  |
| Ошибки страниц | builtin:host.mem.avail.pfps | dt.host.memory.avail.pfps |  |  |  |  |
| Использованный swap | builtin:host.mem.swap.used | dt.host.memory.swap.used |  |  |  |  |
| Всего swap | builtin:host.mem.swap.total | dt.host.memory.swap.total |  |  |  |  |
| Доступный swap | builtin:host.mem.swap.avail | dt.host.memory.swap.avail |  |  |  |  |

### Файловые дескрипторы/дескрипторы

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Использовано файловых дескрипторов | builtin:host.handles.fileDescriptorsUsed | dt.host.handles.file\_descriptors\_used |  |  |  |  |
| Максимум файловых дескрипторов | builtin:host.handles.fileDescriptorsMax | dt.host.handles.file\_descriptors\_max |  |  |  |  |

## Метрики дисков

Метрики, отражающие использование дисков. Обратите внимание, что на Linux существует разделение между сетевыми и локальными дисками.

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Всего[1](#fn-1-1-def) |  |  |  |  | [2](#fn-1-2-def) |  |
| Использовано | builtin:host.disk.used | dt.host.disk.used |  |  | [2](#fn-1-2-def) |  |
| Использовано % | builtin:host.disk.usedPct | dt.host.disk.used.percent |  |  | [2](#fn-1-2-def) |  |
| Доступно[1](#fn-1-1-def) | builtin:host.disk.avail | dt.host.disk.avail |  |  | [2](#fn-1-2-def) |  |
| Доступно %[1](#fn-1-1-def) | builtin:host.disk.free | dt.host.disk.free |  |  | [2](#fn-1-2-def) |  |
| Чтение (байт/с) | builtin:host.disk.bytesRead | dt.host.disk.bytes\_read | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Запись (байт/с) | builtin:host.disk.bytesWritten | dt.host.disk.bytes\_written | [3](#fn-1-3-def) |  | [2](#fn-1-2-def) | [4](#fn-1-4-def) |
| Всего inode | builtin:host.disk.inodesTotal | dt.host.disk.inodes\_total |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Доступно inode % | builtin:host.disk.inodesAvail | dt.host.disk.inodes\_avail |  | [5](#fn-1-5-def) | [2](#fn-1-2-def) |  |
| Чтений (IOPS) | builtin:host.disk.readOps | dt.host.disk.read\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Записей (IOPS) | builtin:host.disk.writeOps | dt.host.disk.write\_ops | [3](#fn-1-3-def) |  | [6](#fn-1-6-def) |  |
| Время чтения диска | builtin:host.disk.readTime | dt.host.disk.read\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Время записи диска | builtin:host.disk.writeTime | dt.host.disk.write\_time | [3](#fn-1-3-def) | [7](#fn-1-7-def) |  |  |
| Время использования диска | builtin:host.disk.utilTime | dt.host.disk.util\_time | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |
| Средняя длина очереди диска | builtin:host.disk.queueLength | dt.host.disk.queue\_length | [3](#fn-1-3-def) | [8](#fn-1-8-def) |  |  |

1

OneAgent версии 1.313+ Метрики доступного и общего объёма диска не отправляются, если общий размер диска превышает 1024 петабайта (1024 ПБ).

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

## Сетевые метрики по сетевому интерфейсу (NIC)

Метрики, отражающие использование сетевых интерфейсов на хосте. Они собираются сетевым модулем OneAgent.

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Принято байт/с | builtin:host.net.nic.bytesRx | dt.host.net.nic.bytes\_rx |  |  |  |  |
| Отправлено байт/с | builtin:host.net.nic.bytesTx | dt.host.net.nic.bytes\_tx |  |  |  |  |
| Принято пакетов/с | builtin:host.net.nic.packets.rx | dt.host.net.nic.packets.rx |  |  |  |  |
| Отправлено пакетов/с | builtin:host.net.nic.packets.tx | dt.host.net.nic.packets.tx |  |  |  |  |
| Потеряно исходящих пакетов/с | builtin:host.net.nic.packets.droppedTx | dt.host.net.nic.packets.dropped\_tx |  |  |  |  |
| Потеряно входящих пакетов/с | builtin:host.net.nic.packets.droppedRx | dt.host.net.nic.packets.dropped\_rx |  |  |  |  |
| Исходящих ошибок/с | builtin:host.net.nic.packets.errorsTx | dt.host.net.nic.packets.errors\_tx |  |  |  |  |
| Входящих ошибок/с | builtin:host.net.nic.packets.errorsRx | dt.host.net.nic.packets.errors\_rx |  |  |  |  |
| Утилизация отправки | builtin:host.net.nic.linkUtilTx | dt.host.net.nic.link\_util\_tx |  |  |  |  |
| Утилизация приёма | builtin:host.net.nic.linkUtilRx | dt.host.net.nic.link\_util\_rx |  |  |  |  |

## Доступность

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail | Windows | Linux | AIX | Режим Discovery |
| --- | --- | --- | --- | --- | --- | --- |
| Доступность хоста | builtin:host.availability.state | dt.host.availability |  |  |  |  |
| Время работы хоста | builtin:host.uptime | builtin:host.uptime |  |  |  |  |

## Прочее

| Название метрики | Ключ Metrics classic | Ключ Metrics on Grail |
| --- | --- | --- |
| Смещение времени хоста | builtin:host.la.to | unsupported |
