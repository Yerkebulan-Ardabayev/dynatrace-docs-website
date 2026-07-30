---
title: Аппаратные и системные требования для маршрутизации/мониторинга ActiveGates на Linux
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements
---

# Аппаратные и системные требования для маршрутизации/мониторинга ActiveGates на Linux

# Аппаратные и системные требования для маршрутизации/мониторинга ActiveGates на Linux

* 4 минуты чтения
* Обновлено 07 июля 2026

### Аппаратные и системные требования: маршрутизация трафика OneAgent к Dynatrace, мониторинг облачных сред или мониторинг удалённых технологий с помощью расширений

Аппаратные и системные требования для других целей использования ActiveGate описаны в:

* [Аппаратные и системные требования для Synthetic-enabled ActiveGates](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations"), которые поддерживают подмножество операционных систем и предъявляют более высокие требования к аппаратному обеспечению и системным ресурсам, чем ActiveGates, используемые для маршрутизации и мониторинга.
* [Аппаратные и системные требования для модуля zRemote для мониторинга z/OS](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring."). ActiveGates с модулем zRemote предъявляют более высокие требования к аппаратному обеспечению и системным ресурсам, чем ActiveGates, используемые для маршрутизации и мониторинга.

Запуск ActiveGate на выделенной системе

Для оптимальной производительности и повышенной безопасности рекомендуется устанавливать и запускать ActiveGate на выделенной системе.
Использование ActiveGate на выделенной системе минимизирует риск компрометации данных аутентификации ActiveGate и снижает вероятность злонамеренной манипуляции конфигурацией.

Подробные характеристики пропускной способности журналов на Environmental Active Gate для приёма журналов API приведены на странице [Log Monitoring default limits (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.").

## Аппаратные требования

Для ActiveGate необходима выделенная машина со следующими характеристиками:

* 4 ГБ свободного места на диске для установки, настройки и журналов ActiveGate и Extensions, а также для нужд автоматического обновления.
* 4 ГБ для кэшированных установщиков и образов контейнеров ActiveGate и OneAgent, если их планируется хранить.
* Место для дамп-файлов, если их планируется хранить. Эта функция отключена по умолчанию, но её можно включить в конфигурации ActiveGate. Максимальный размер пространства для хранения [настраивается](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.") (по умолчанию 100 ГБ).
* 600 МБ + 1,5 ГБ (буфер) свободного места на диске для файла постоянного хранения повторной передачи журналов Extension Execution Controller.
* Место для загрузки расширений, в зависимости от используемых расширений.
* 2 ГБ оперативной памяти (рекомендуется 4 ГБ).
* 1 двухъядерный процессор.

В крупных средах может потребоваться машина с дополнительными ресурсами CPU и памяти.

## Требования к дисковому пространству по каталогам

**Распределение места по каталогам для нужд установки:**  
**(для более детального распределения см. [ActiveGate directories](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

| **Каталог верхнего уровня** | **Требования к дисковому пространству** |
| --- | --- |
| Исполняемые файлы, библиотеки и связанные файлы ActiveGate и модуля автообновления  по умолчанию: `/opt/dynatrace`  относительно параметра установки: `<INSTALL>` | 600 МБ |
| Конфигурация ActiveGate и связанные каталоги  Для Environment ActiveGate также содержит конфигурацию Extensions  по умолчанию: `/var/lib/dynatrace`  относительно параметра установки: `<CONFIG>` | 2 МБ |
| Только для Environment ActiveGate: исполняемые файлы, библиотеки и связанные файлы Extensions  по умолчанию: `/opt/dynatrace/remotepluginmodule`  относительно параметра установки: `<INSTALL>/remotepluginmodule` | 2 ГБ |

**Распределение места по каталогам для работы ActiveGate:**  
**(для более детального распределения см. [ActiveGate directories](/managed/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."))**

| **Каталог верхнего уровня** | **Требования к дисковому пространству** |
| --- | --- |
| Журналы ActiveGate и модуля автообновления  по умолчанию: `/var/log/dynatrace`  параметр установки: `<LOG>` | 1,2 ГБ |
| Каталог пакетов ActiveGate для загрузки установщиков автообновления  по умолчанию: `/var/lib/dynatrace/packages`  параметр установки: `<PACKAGES_DIR>` | 600 МБ |
| Временные файлы ActiveGate  по умолчанию: `/var/tmp/dynatrace/gateway`  путь относительно параметра установки TEMP: `<TEMP>/gateway` | 4 ГБ (включая 3 ГБ для кэшированных установщиков и образов контейнеров OneAgent) |
| Дамп-файлы, загруженные на ActiveGate агентом OneAgent  `/var/lib/dynatrace/gateway/dump` | Функция отключена по умолчанию, не настраивается во время установки.  После активации занимает настраиваемый максимальный объём: по умолчанию 100 ГБ. |
| Только для Environment ActiveGate: журналы, кэш и рабочая область времени выполнения Extensions  по умолчанию: `/var/lib/dynatrace/remotepluginmodule`  путь относительно параметра установки CONFIG: `<CONFIG>/remotepluginmodule` | 2 ГБ |
| Только для Environment ActiveGate: каталог загрузки расширений ActiveGate  по умолчанию: `/opt/dynatrace/remotepluginmodule/plugin_deployment`  путь относительно параметра установки INSTALL: `<INSTALL>/remotepluginmodule/plugin_deployment` | Зависит от загружаемых расширений |
| Каталог постоянного хранения для повторной передачи журналов Extension Execution Controller `/var/lib/dynatrace/remotepluginmodule/agent/runtime/extensions/persistence` | До 600 МБ по умолчанию. [1](#fn-1-1-def) |

1

Механизм надёжности не работает, если требование не выполнено. Дополнительно требуется 1,5 ГБ в качестве буфера. Подробнее см. [Подробности о постоянном хранении](#persistence).

## Подробности о постоянном хранении

Механизм надёжности обеспечивает постоянное хранение журналов Extension Execution Controller (EEC) в случае недоступности ActiveGate или OneAgent, проблем с сетью или перегрузки EEC при приёме данных. Это минимизирует пробелы в охвате журналирования.

### Общие сведения

* Для постоянного хранения данных необходимо 2136 МБ свободного места на диске:

  + 600 МБ свободного места для использования механизмом надёжности
  + 1,5 ГБ свободного места в качестве буфера
* Требование проверяется периодически; если оно не выполнено, постоянное хранение отключается и приём журналов осуществляется без механизма надёжности.
* Объём используется пропорционально нагрузке на приём журналов.
* Если требование не может быть выполнено на узле, можно изменить конфигурацию постоянного хранения журналов. Подробнее см. [Конфигурация постоянного хранения](#persistence_config).

### Конфигурация

Файл конфигурации Windows: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\extensionsuser.conf`

Файл конфигурации Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/extensionsuser.conf`

| **Переменная** | **Описание** |
| --- | --- |
| `persistence.reliable_mode` | `true` - надёжный режим включён; журналы SFM genereted, если требование к дисковому пространству не выполнено `false` - надёжный режим отключён; приём журналов осуществляется без механизма надёжности |
| `persistence.total_limit_kb` | Максимальный лимит объёма для Extensions Log Persistence в килобайтах. По умолчанию: 600 МБ. Можно изменить вручную, если требование не может быть выполнено на узле. |

## Поддерживаемые операционные системы

### Routing-monitoring ActiveGates

| Дистрибутив Linux | Версии | Архитектуры CPU |
| --- | --- | --- |
| Amazon Linux | 2, 2023[1](#fn-linux-distribution-1-def) | ARM64 (AArch64), x86-64 |
| Oracle Linux | 8.10, 9.7, 9.8, 10.1, 10.2 | ARM64 (AArch64), x86-64 |
| Red Hat Enterprise Linux | 8.10, 9.4, 9.6, 9.7, 9.8, 10.0, 10.1, 10.2 | ARM64 (AArch64), s390, x86-64 |
| Rocky Linux | 8.10, 9.7, 9.8, 10.1, 10.2 | ARM64 (AArch64), x86-64 |
| SUSE Enterprise Linux | 15.7 | ARM64 (AArch64), s390, x86-64 |
| Ubuntu | 16.04, 18.04, 20.04, 22.04, 24.04, 26.04 | x86-64 |
| Ubuntu | 20.04, 22.04, 24.04, 26.04 | ARM64 (AArch64), s390 |

1

Для запуска расширений ActiveGate на Amazon Linux 2023 версии 315 и более ранние требуют ручной установки библиотеки 'libcrypt.so.1' из пакета 'libxcrypt-compat.rpm', который не устанавливается по умолчанию.

ActiveGate, установленный на архитектуру x86-64, поддерживает весь функционал. Другие архитектуры обеспечивают лишь частичную поддержку. Подробнее см. [ActiveGate purposes and functionality](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.").

### ActiveGates, запускающие синтетические мониторы из частного местоположения

Для ActiveGates, запускающих синтетические мониторы из частного местоположения, см. [Requirements for private Synthetic location: Linux: Supported operating systems](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic#linux "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

### ActiveGates с модулем zRemote

Для ActiveGates с модулем zRemote см. [Install the zRemote module: System requirements: Supported operating systems](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#supported-operating-systems "Prepare and install the zRemote for z/OS monitoring.").

## Системные требования

* Убедитесь, что настроена корректная [конфигурация сетевых портов](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.").
* Операционная система должна поддерживать не менее 500 000 открытых файлов для пользователя `dtuserag`.  
  Чтобы просмотреть системный лимит, выполните команду:

  ```
  [user@host]# cat /proc/sys/fs/file-max
  ```

  Также возможно, что в Linux открыто слишком много файлов.
* Операционная система должна предоставлять не менее 20 000 процессов пользователю `dtuserag`.  
  Чтобы просмотреть системный лимит, выполните команду:

  ```
  [user@host]# cat /proc/sys/kernel/pid_max
  ```
* Установщик ActiveGate для Linux не поддерживает ACL (Access Control List). Правила ACL могут запрещать доступ к директориям и файлам, созданным установщиком, из-за чего ActiveGate не запустится. При использовании ACL нужно отключить правила, относящиеся к директориям установки, заданным в следующих параметрах:

  ```
  INSTALL=



  CONFIG=



  LOG=



  TEMP=



  PACKAGES_DIR=
  ```

## Руководство по выбору размера

### Выбор размера для маршрутизации трафика OneAgent

В таблице ниже приведены требования к размеру экземпляра машины в зависимости от числа OneAgent, взаимодействующих с ActiveGate. На каждом хосте OneAgent выполняет восемь задач мониторинга:

* Мониторинг инфраструктуры
* Мониторинг логов
* Полный мониторинг 3 экземпляров Apache Tomcat
* Полный мониторинг 2 экземпляров Apache HTTP Server
* Мониторинг расширений

Реальное число хостов может отличаться в зависимости от отслеживаемых технологий в вашей среде. Рекомендуется, чтобы машина, на которой работает ActiveGate, не превышала 50% CPU и 80% памяти. Также нужно учитывать, что ActiveGate могут быть недоступны во время обновлений, перезапусков или кратковременных проблем со связью. Для обеспечения высокой доступности работающие ActiveGate должны быть способны принять трафик недоступных ActiveGate.

#### Архитектура x86-64

Экземпляры машин C6i и оценочные показатели:

| Экземпляр | vCPU | Память (ГиБ) | Хранилище | Выделенная пропускная способность EBS (Мбит/с) | Производительность сети | Оценочное число хостов |
| --- | --- | --- | --- | --- | --- | --- |
| c6i.large | 2 | 3,75 | EBS-Only | 500 | Moderate | 800 |
| c6i.xlarge | 4 | 7,5 | EBS-Only | 750 | High | 1800 |
| c6i.2xlarge | 8 | 15 | EBS-Only | 1 000 | High | 2500 |

#### Архитектура ARM64 (AArch64)

Экземпляры машин C7g и оценочные показатели:

| Экземпляр | vCPU | Память (ГиБ) | Хранилище | Выделенная пропускная способность EBS (Мбит/с) | Производительность сети | Оценочное число хостов |
| --- | --- | --- | --- | --- | --- | --- |
| c7g.large | 2 | 3,75 | EBS-Only | 500 | Moderate | 1300 |
| c7g.xlarge | 4 | 7,5 | EBS-Only | 750 | High | 2700 |
| c7g.2xlarge | 8 | 15 | EBS-Only | 1 000 | High | 5500 |

#### Архитектура s390

Размеры машин и оценочные показатели:

| Размер машины | CPU | Память (ГиБ) | Оценочное число хостов |
| --- | --- | --- | --- |
| S | 2 | 4 | 800 |
| M | 4 | 8 | 1500 |

### Выбор размера только для приёма логов API

ActiveGate получает данные логов исключительно через API приёма логов.

* Устойчивый приём логов выполняется при типичном распределении размеров сообщений.
* **Размеры сообщений**: 5% очень маленькие (1,5 КБ), 20% маленькие (1,5 КБ), 50% средние (2,2 КБ), 20% большие (3 КБ), 5% очень большие (7,8 КБ)
* **Число атрибутов**: от 5 до 100 атрибутов на запись лога
* **Размеры пакетов**: от 10 до 100 сообщений на вызов API

Приведённые конфигурации ресурсов предусматривают запас для пиков трафика и переключения реплик при обновлениях.

#### Архитектура x86-64

В следующей таблице перечислены экземпляры машин C7i и оценочные показатели:

| Экземпляр | vCPU | Память (ГиБ) | Только приём логов API (МБ/мин) |
| --- | --- | --- | --- |
| c7i.large | 2 | 3,75 | 1 100 |
| c7i.xlarge | 4 | 7,5 | 2 300 |
| c7i.2xlarge | 8 | 15 | 5 100 |

#### Архитектура ARM64 (AArch64)

В следующей таблице перечислены экземпляры машин C7g и оценочные показатели:

| Экземпляр | vCPU | Память (ГиБ) | Только приём логов API (МБ/мин) |
| --- | --- | --- | --- |
| c7g.large | 2 | 3,75 | 1 000 |
| c7g.xlarge | 4 | 7,5 | 2 000 |
| c7g.2xlarge | 8 | 15 | 4 600 |

### Выбор размера для смешанной нагрузки (маршрутизация трафика OneAgent + приём логов API)

ActiveGate одновременно обрабатывает маршрутизацию трафика OneAgent и приём логов API.

* Маршрутизация трафика OneAgent составляет 50% от пропускной способности только для маршрутизации для данного размера машины (мониторинг инфраструктуры, мониторинг логов, полный мониторинг, мониторинг расширений).
* Приём логов API выполняется параллельно при типичном распределении размеров сообщений.

Реальная пропускная способность зависит от конкретной конфигурации мониторинга, объёма логов, размеров сообщений и характеристик нагрузки. Машина, на которой работает ActiveGate, не должна превышать 50% CPU и 80% памяти. ActiveGate могут быть недоступны во время обновлений, перезапусков или кратковременных проблем со связью. Для обеспечения высокой доступности оставшиеся ActiveGate должны быть способны принять трафик недоступных ActiveGate.

#### Архитектура x86-64

В следующей таблице перечислены экземпляры машин C7i и оценочные показатели:

| Экземпляр | vCPU | Память (ГиБ) | Хосты | Приём логов API (МБ/мин) |
| --- | --- | --- | --- | --- |
| c7i.large | 2 | 3,75 | 400 | 750 |
| c7i.xlarge | 4 | 7,5 | 900 | 1 500 |
| c7i.2xlarge | 8 | 15 | 1 250 | 3 300 |

#### Архитектура ARM64 (AArch64)

В следующей таблице перечислены экземпляры машин C7g и оценочные показатели:

| Экземпляр | vCPU | Память (ГиБ) | Хосты | Приём логов API (МБ/мин) |
| --- | --- | --- | --- | --- |
| c7g.large | 2 | 3,75 | 400 | 280 |
| c7g.xlarge | 4 | 7,5 | 1 350 | 560 |
| c7g.2xlarge | 8 | 15 | 2 750 | 1 650 |