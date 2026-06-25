---
title: Требования к оборудованию и системе для ActiveGate (маршрутизация/мониторинг) на Windows
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements
scraped: 2026-05-12T11:08:08.991629
---

# Требования к оборудованию и системе для ActiveGate (маршрутизация/мониторинг) на Windows

# Требования к оборудованию и системе для ActiveGate (маршрутизация/мониторинг) на Windows

* 2-min read
* Published Oct 09, 2018

### Требования к оборудованию и системе: маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных окружений или удалённых технологий с помощью расширений

Требования к оборудованию и системе для других назначений ActiveGate:

* [Требования к оборудованию и системе для Synthetic-enabled ActiveGate](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений"), которые поддерживают подмножество операционных систем и предъявляют более высокие требования к оборудованию, чем ActiveGate для маршрутизации и мониторинга.
* [Требования к оборудованию и системе для модуля zRemote (мониторинг z/OS)](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Подготовка и установка zRemote для мониторинга z/OS."). ActiveGate с модулем zRemote предъявляют более высокие требования к оборудованию, чем ActiveGate для маршрутизации и мониторинга.

Запускайте ActiveGate на выделенной системе

Для оптимальной производительности и повышенной безопасности рекомендуется устанавливать и запускать ActiveGate на выделенной системе.
Использование выделенной системы минимизирует риск компрометации данных аутентификации ActiveGate и снижает вероятность злонамеренной манипуляции с конфигурацией.

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
| ActiveGate and autoupdater executable files, libraries, and related files  `%PROGRAMFILES%\dynatrace\gateway`  relative to installation parameter: `<INSTALL>\gateway`  also configurable in GUI during installation | 300 MB |
| ActiveGate configuration and related directories  For Environment ActiveGate, it also contains Extensions configuration  `%PROGRAMDATA%\dynatrace` | 2 MB |
| For Environment ActiveGate only: Extensions executable files, libraries, and related files `%PROGRAMFILES%\dynatrace\remotepluginmodule`  relative to installation parameter: `<INSTALL>\remotepluginmodule`  also configurable in GUI during installation | 850 MB |

**Распределение пространства по директориям для работы ActiveGate:**
**(более детальное распределение см. в [Директориях ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Узнайте, где хранятся файлы ActiveGate на Windows и Linux."))**

> _Reference-таблица ниже на английском._

| **Top-level directory** | **Disk space requirements** |
| --- | --- |
| ActiveGate and autoupdater logs  ActiveGate packages directory for auto-update installer downloads  `%PROGRAMDATA%\dynatrace` | 1.2 GB |
| ActiveGate temporary files  `%PROGRAMDATA%\dynatrace\gateway\tmp` | 4 GB (including 3 GB for cached OneAgent installers and container images) |
| Dump files uploaded to ActiveGate by OneAgent  `%PROGRAMDATA%\dynatrace\gateway\dump` | Functionality off by default. When activated, can take configurable maximum size: default 100 GB. |
| For Environment ActiveGate only: ActiveGate Extensions logs, cache, run-time work area  `%PROGRAMDATA%\dynatrace\remotepluginmodule` | 2 GB |
| For Environment ActiveGate only: ActiveGate extensions upload directory  `%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment` | Depending on uploaded extensions |
| Extension Execution Controller logs retransmission persistence directory `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\runtime\extensions\persistence` | Up to 600 MB by default. [1](#fn-1-1-def) |

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

Поддерживаемые операционные системы:

| Операционная система Windows | Версии | Архитектуры CPU |
| --- | --- | --- |
| Windows | 11 | x86-64 |
| Windows Server | 2016, 2019, 2022, 2025 | x86-64 |

## Системные требования

* ActiveGate поддерживает только операционные системы на архитектуре x86-64 (64-разрядный Intel/AMD).
* Убедитесь в наличии правильной [конфигурации сетевых портов](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate и между ActiveGate и OneAgent.").
* Установка ActiveGate не поддерживается на Windows с отключённой учётной записью `NT AUTHORITY\LocalService`.

## Руководство по выбору размера системы AWS

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