---
title: Требования к оборудованию и системе для ActiveGate (маршрутизация/мониторинг) на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements
scraped: 2026-05-12T11:08:20.855981
---

# Требования к оборудованию и системе для ActiveGate (маршрутизация/мониторинг) на Linux

# Требования к оборудованию и системе для ActiveGate (маршрутизация/мониторинг) на Linux

* 4-min read
* Updated on Nov 20, 2025

### Требования к оборудованию и системе: маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных окружений или удалённых технологий с помощью расширений

Требования к оборудованию и системе для других назначений ActiveGate:

* [Требования к оборудованию и системе для Synthetic-enabled ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений"), которые поддерживают подмножество операционных систем и предъявляют более высокие требования к оборудованию, чем ActiveGate для маршрутизации и мониторинга.
* [Требования к оборудованию и системе для модуля zRemote (мониторинг z/OS)](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Подготовка и установка zRemote для мониторинга z/OS."). ActiveGate с модулем zRemote предъявляют более высокие требования к оборудованию, чем ActiveGate для маршрутизации и мониторинга.

Запускайте ActiveGate на выделенной системе

Для оптимальной производительности и повышенной безопасности рекомендуется устанавливать и запускать ActiveGate на выделенной системе.
Использование выделенной системы минимизирует риск компрометации данных аутентификации ActiveGate и снижает вероятность злонамеренной манипуляции с конфигурацией.

Для получения информации о пропускной способности журналов на Environment ActiveGate для API приёма журналов обратитесь к странице [Ограничения Log Monitoring по умолчанию (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Ограничения по умолчанию для последней версии Dynatrace Log Monitoring.").

## Требования к оборудованию

Необходима машина, выделенная для ActiveGate, со следующими характеристиками:

* 4 ГБ свободного дискового пространства для установки ActiveGate и Extensions, конфигурации и журналов для целей автообновления.
* 4 ГБ для кэшированных установщиков OneAgent и образов контейнеров ActiveGate (если они должны храниться).
* Пространство для дамп-файлов (если они должны храниться). Эта функция отключена по умолчанию, но может быть включена в конфигурации ActiveGate. Максимальный размер хранилища [настраивается](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Узнайте, как включить хранение дампов памяти на ActiveGate."), по умолчанию 100 ГБ.
* 600 МБ + 1,5 ГБ (буфер) свободного дискового пространства для файла персистентности повторной передачи журналов Extension Execution Controller.
* Пространство для загружаемых расширений (зависит от используемых расширений).
* 2 ГБ ОЗУ (рекомендуется 4 ГБ).
* 1 двухъядерный процессор.

Для крупных окружений может потребоваться машина с дополнительными CPU и памятью.

## Требования к дисковому пространству по директориям

**Распределение пространства по директориям для целей установки:**
**(более детальное распределение см. в [Директориях ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux."))**

> _Reference-таблица ниже на английском._

| **Top-level directory** | **Disk space requirements** |
| --- | --- |
| ActiveGate and autoupdater executable files, libraries, and related files  default: `/opt/dynatrace`  relative to installation parameter: `<INSTALL>` | 300 MB |
| ActiveGate configuration and related directories  For Environment ActiveGate, it also contains Extensions configuration  default: `/var/lib/dynatrace`  relative to installation parameter: `<CONFIG>` | 2 MB |
| For Environment ActiveGate only: Extensions executable files, libraries, and related files default: `/opt/dynatrace/remotepluginmodule`  relative to installation parameter: `<INSTALL>/remotepluginmodule` | 1.2 GB |

**Распределение пространства по директориям для работы ActiveGate:**
**(более детальное распределение см. в [Директориях ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux."))**

> _Reference-таблица ниже на английском._

| **Top-level directory** | **Disk space requirements** |
| --- | --- |
| ActiveGate and autoupdater logs  default: `/var/log/dynatrace`  installation parameter: `<LOG>` | 700 MB |
| ActiveGate packages directory for auto-update installer downloads  default: `/var/lib/dynatrace/packages`  installation parameter: `<PACKAGES_DIR>` | 500 MB |
| ActiveGate temporary files  default: `/var/tmp/dynatrace/gateway`  path relative to installation parameter TEMP: `<TEMP>/gateway` | 4 GB (including 3 GB for cached OneAgent installers and container images) |
| Dump files uploaded to ActiveGate by OneAgent  `/var/lib/dynatrace/gateway/dump` | Functionality off by default, not configurable at installation time.  When activated, can take configurable maximum size: default 100 GB. |
| For Environment ActiveGate only: ActiveGate Extensions logs, cache, run-time work area  default: `/var/lib/dynatrace/remotepluginmodule`  path relative to installation parameter CONFIG: `<CONFIG>/remotepluginmodule` | 2 GB |
| For Environment ActiveGate only: ActiveGate extensions upload directory  default: `/opt/dynatrace/remotepluginmodule/plugin_deployment`  path relative to installation parameter INSTALL: `<INSTALL>/remotepluginmodule/plugin_deployment` | Depending on uploaded extensions |
| Extension Execution Controller logs retransmission persistence directory `/var/lib/dynatrace/remotepluginmodule/agent/runtime/extensions/persistence` | Up to 600 MB by default. [1](#fn-1-1-def) |

1

Механизм надёжности не работает при невыполнении требования. Требуется дополнительно 1,5 ГБ в качестве буфера. Подробнее см. [Детали персистентности](#persistence).

## Детали персистентности

Механизм надёжности обеспечивает персистентность журналов Extension Execution Controller (EEC) в случае недоступности ActiveGate или OneAgent, проблем с сетью или перегрузки EEC при приёме данных. Это минимизирует пробелы в покрытии журналов.

### Общая информация

* Для персистентного хранения данных требуется 2136 МБ свободного дискового пространства:

  + 600 МБ свободного дискового пространства для механизма надёжности
  + 1,5 ГБ свободного дискового пространства в качестве буфера
* Требование проверяется периодически; при его невыполнении персистентность будет отключена и приём журналов будет осуществляться без механизма надёжности.
* Объём используется пропорционально нагрузке на приём журналов.
* Если требование не может быть выполнено на хосте, можно изменить конфигурацию персистентности журналов. Подробнее см. [Конфигурация персистентности](#persistence_config).

### Конфигурация

Файл конфигурации Windows: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Файл конфигурации Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

| **Переменная** | **Описание** |
| --- | --- |
| `persistence.reliable_mode` | `true` — надёжный режим включён; SFM-журналы генерируются при невыполнении требования к пространству. `false` — надёжный режим выключен; приём журналов осуществляется без механизма надёжности. |
| `persistence.total_limit_kb` | Максимальный лимит объёма для персистентности журналов Extensions в килобайтах. По умолчанию: 600 МБ. Может быть изменён вручную при невозможности выполнить требование на хосте. |

## Поддерживаемые операционные системы

### ActiveGate для маршрутизации и мониторинга

> _Reference-таблица ниже на английском._

| Linux distribution | Versions | CPU architectures |
| --- | --- | --- |
| Amazon Linux | 2, 2023[1](#fn-linux-distribution-1-def) | ARM64 (AArch64), x86-64 |
| Oracle Linux | 8.10, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), s390, x86-64 |
| Rocky Linux | 8.10, 9.6, 9.7, 10.0, 10.1 | ARM64 (AArch64), x86-64 |
| SUSE Enterprise Linux | 15.6, 15.7 | ARM64 (AArch64), s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04 | ARM64 (AArch64), s390 |

1

Для запуска расширений ActiveGate на Amazon Linux 2023 версии 315 и ранее требуется ручная установка библиотеки `libcrypt.so.1` из пакета `libxcrypt-compat.rpm`, который не устанавливается по умолчанию.

ActiveGate, установленный на архитектуре x86-64, поддерживает все функции. Другие архитектуры обеспечивают только частичную поддержку. Подробнее см. [Назначения и функции ActiveGate](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применении ActiveGate.").

### ActiveGate для запуска синтетических мониторов из частных расположений

Для ActiveGate, запускающего синтетические мониторы из частного расположения, см. [Требования для частного расположения Synthetic: Linux: Поддерживаемые операционные системы](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#linux "Поддерживаемые ОС, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений").

### ActiveGate с модулем zRemote

Для ActiveGate с модулем zRemote см. [Установка модуля zRemote: Системные требования: Поддерживаемые операционные системы](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#supported-operating-systems "Подготовка и установка zRemote для мониторинга z/OS.").

## Системные требования

* Убедитесь в наличии правильной [конфигурации сетевых портов](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate и между ActiveGate и OneAgent.").
* Операционная система должна обрабатывать не менее 500 000 открытых файлов для пользователя `dtuserag`.
  Для просмотра системного лимита выполните команду:

  ```
  [user@host]# cat /proc/sys/fs/file-max
  ```

  Также может возникнуть ситуация [слишком большого количества открытых файлов в Linux](/managed/ingest-from/dynatrace-activegate#too-many-open-files-in-linux "Понять основные концепции ActiveGate.").
* Операционная система должна предоставлять не менее 20 000 процессов пользователю `dtuserag`.
  Для просмотра системного лимита выполните команду:

  ```
  [user@host]# cat /proc/sys/kernel/pid_max
  ```
* Установщик ActiveGate для Linux не поддерживает ACL (Access Control List). Правила ACL могут запрещать доступ к директориям и файлам, созданным установщиком, что приведёт к сбою запуска ActiveGate. При использовании ACL правила, связанные с директориями установки, определёнными в следующих параметрах, должны быть отключены:

  ```
  INSTALL=



  CONFIG=



  LOG=



  TEMP=



  PACKAGES_DIR=
  ```

## Руководство по выбору размера системы

Следующая таблица представляет требования к размеру экземпляра машины в зависимости от количества OneAgent, взаимодействующих с ActiveGate. На каждом хосте OneAgent выполняет восемь задач мониторинга:

* Мониторинг инфраструктуры
* Мониторинг журналов
* Full-stack мониторинг 3 экземпляров Apache Tomcat
* Full-stack мониторинг 2 экземпляров Apache HTTP Server
* Мониторинг расширений

Реальное количество хостов может отличаться в зависимости от мониторируемых технологий в вашем окружении. Рекомендуется, чтобы машина, на которой запущен ActiveGate, не превышала 50% CPU и 80% памяти. Кроме того, необходимо учитывать, что ActiveGate могут быть неработоспособны во время обновлений, перезапусков или кратковременных проблем со связью. Для обеспечения высокой доступности работающие ActiveGate должны быть способны принять трафик недоступных ActiveGate.

### Архитектура x86-64

Экземпляры машин C6i и оценки:

> _Reference-таблица ниже на английском._

| Instance | vCPU | Mem (GiB) | Storage | Dedicated EBS bandwidth (Mbps) | Network performance | Estimated number of hosts |
| --- | --- | --- | --- | --- | --- | --- |
| c6i.large | 2 | 3.75 | EBS-Only | 500 | Moderate | 800 |
| c6i.xlarge | 4 | 7.5 | EBS-Only | 750 | High | 1800 |
| c6i.2xlarge | 8 | 15 | EBS-Only | 1,000 | High | 2500 |

### Архитектура ARM64 (AArch64)

Экземпляры машин C7g и оценки:

> _Reference-таблица ниже на английском._

| Instance | vCPU | Mem (GiB) | Storage | Dedicated EBS bandwidth (Mbps) | Network performance | Estimated number of hosts |
| --- | --- | --- | --- | --- | --- | --- |
| c7g.large | 2 | 3.75 | EBS-Only | 500 | Moderate | 1300 |
| c7g.xlarge | 4 | 7.5 | EBS-Only | 750 | High | 2700 |
| c7g.2xlarge | 8 | 15 | EBS-Only | 1,000 | High | 5500 |

### Архитектура s390

Размеры машин и оценки:

| Размер машины | CPU | Mem (GiB) | Оценочное количество хостов |
| --- | --- | --- | --- |
| S | 2 | 4 | 800 |
| M | 4 | 8 | 1500 |