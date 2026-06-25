---
title: Режимы мониторинга OneAgent
source: https://docs.dynatrace.com/managed/platform/oneagent/monitoring-modes/monitoring-modes
scraped: 2026-05-12T11:07:15.600496
---

# Режимы мониторинга OneAgent

# Режимы мониторинга OneAgent

* Explanation
* 5-min read
* Updated on Nov 26, 2025

Использование [OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") для сбора данных о производительности и работоспособности вашей среды обеспечивает глубокую наблюдаемость приложений, сервисов и инфраструктуры. Для поддержки различных сценариев использования и требований к ресурсам OneAgent поддерживает несколько режимов мониторинга.

Если вам не нужен полный мониторинг стека, вы можете выбрать один из двух облегчённых режимов, ориентированных на основные метрики инфраструктуры:

* Режим мониторинга инфраструктуры
* Режим обнаружения

Ниже приведён обзор доступных параметров мониторинга для каждого режима.

| Компонент | Full stack | Infrastructure | Discovery |
| --- | --- | --- | --- |
| Обнаружение топологии (гибридное облако и Smartscape) | GA | GA | GA |
| Критичность хоста (обнаружение внешних сервисов и зависимостей приложений) | GA | GA | GA |
| Базовый мониторинг (работоспособность хоста, файловая система, службы ОС) | GA | GA | GA |
| Детали процессов хоста | GA | GA |  |
| Детальный анализ дисков | GA | GA |  |
| Анализ сети | GA | GA |  |
| Анализ памяти | GA | GA |  |
| Расширения | opt-in | opt-in |  |
| Пользовательские метрики | 15 / 256 MiB | 100 / host |  |
| Log Management | opt-in | opt-in | opt-in |
| Трассировка и профилирование | GA |  |  |
| Внедрение в процессы | GA | opt-out |  |
| Application Security[1](#fn-1-1-def) | opt-in | opt-in | opt-in |
| Live Debugger | opt-in | opt-in | opt-in |

1

Подробнее о режимах Infrastructure и Discovery для Application Security см. в разделе [Режимы мониторинга для Application Security](/managed/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").

## Режим мониторинга инфраструктуры

Автоматическое внедрение OneAgent

OneAgent в режиме мониторинга инфраструктуры автоматически внедряется в процессы, чтобы обеспечить мониторинг вспомогательных сервисов на Java и метрики выполнения для поддерживаемых языков. Узнайте, как [отключить автоматическое внедрение](/managed/platform/oneagent/monitoring-modes/enable-monitoring-modes#disable-auto-injection "Learn how to enable monitoring modes when using OneAgent.").

Режим мониторинга Full-Stack обеспечивает комплексный мониторинг производительности приложений, включая видимость на уровне кода, углублённый мониторинг процессов и мониторинг инфраструктуры (в том числе платформ PaaS). Однако если вас больше интересует работоспособность инфраструктуры, а не углублённый анализ приложений, вы можете настроить OneAgent для использования режима мониторинга инфраструктуры, который фокусируется на физической и виртуальной инфраструктуре, мониторинге журналов и возможностях AIOps.

Подробнее см. в разделе [Включение режима мониторинга инфраструктуры](/managed/platform/oneagent/monitoring-modes/enable-monitoring-modes#enable-infrastructure-monitoring-mode "Learn how to enable monitoring modes when using OneAgent.").

## Режим обнаружения

OneAgent версии 1.281+

Режим обнаружения предоставляет базовые метрики, позволяющие обнаруживать хосты и процессы и оценивать возможности для расширения мониторинга.

Мы рекомендуем развёртывать OneAgent в режиме Full-Stack для мониторинга критически важных бизнес-приложений. Аналогично рекомендуется отслеживать критически важную инфраструктуру — базы данных, очереди и системы обмена сообщениями — с помощью Infrastructure Observability. OneAgent в режиме обнаружения может быть развёрнут на остальной инфраструктуре для обеспечения полной видимости благодаря относительно низкой стоимости.

Режим обнаружения доступен только при использовании модели подписки Dynatrace Platform Subscription. Потребление лицензий осуществляется через возможность **Foundation & Discovery**. Подробнее см. в разделе [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability#discovery "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").

Подробнее см. в разделе [Включение режима обнаружения](/managed/platform/oneagent/monitoring-modes/enable-monitoring-modes#enable-discovery-mode "Learn how to enable monitoring modes when using OneAgent.").

В режиме обнаружения доступны следующие встроенные метрики:

CPU

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.cpu.entConfig | AIX Entitlement configured Выделенная ёмкость — это количество виртуальных процессоров, назначенных разделу AIX. Измеряется в долях процессора, равных 0.1 или 0.01. Подробнее о выделении ресурсов см. в официальной документации IBM [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz). | Ratio | autoavgmaxmin |
| builtin:host.cpu.entc | AIX Entitlement used Процент использованного выделения. Выделенная ёмкость — это количество виртуальных ядер, назначенных разделу AIX. Подробнее см. в официальной документации IBM [Assigning the appropriate processor entitled capacity](https://dt-url.net/3n234vz). | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.idle | CPU idle Среднее время ЦП, когда ЦП не выполнял никаких задач | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.iowait | CPU I/O wait Процент времени, когда ЦП был простаивающим во время ожидания операции ввода-вывода. Недоступно в Windows. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.load | System load Среднее количество процессов, выполняемых или ожидающих выполнения ЦП за последнюю минуту | Ratio | autoavgmaxmin |
| builtin:host.cpu.load15m | System load15m Среднее количество процессов, выполняемых или ожидающих выполнения ЦП за последние 15 минут | Ratio | autoavgmaxmin |
| builtin:host.cpu.load5m | System load5m Среднее количество процессов, выполняемых или ожидающих выполнения ЦП за последние 5 минут | Ratio | autoavgmaxmin |
| builtin:host.cpu.other | CPU other Среднее время ЦП, затраченное на другие задачи: обработку запросов прерываний (IRQ), запуск виртуальных машин под управлением ядра хоста (хост является гипервизором для ВМ). Доступно только для хостов Linux. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.physc | AIX Physical consumed Общее количество процессорных ресурсов, потреблённых разделом AIX | Ratio | autoavgmaxmin |
| builtin:host.cpu.steal | CPU steal Среднее время ЦП, когда виртуальная машина ожидает получения циклов ЦП от гипервизора. В виртуализированной среде циклы ЦП распределяются между виртуальными машинами на сервере гипервизора. Высокое значение CPU steal может указывать на перегруженный гипервизор. Доступно только для хостов Linux. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.system | CPU system Среднее время ЦП при работе в режиме ядра | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.usage | CPU usage % Процент времени использования ЦП. Значение, близкое к 100%, означает, что большинство ресурсов обработки хоста задействованы. | Percent (%) | autoavgmaxmin |
| builtin:host.cpu.user | CPU user Среднее время ЦП при работе в пользовательском режиме | Percent (%) | autoavgmaxmin |
| builtin:host.kernelThreads.blocked | AIX Kernel threads blocked Длина очереди подкачки. | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioEventWait | AIX Kernel threads I/O event wait Количество потоков, ожидающих прямых (cio) операций файловой системы + количество процессов, ожидающих буферизованных операций ввода-вывода | Count | autoavgmaxmin |
| builtin:host.kernelThreads.ioMessageWait | AIX Kernel threads I/O message wait Количество потоков, находящихся в спящем режиме и ожидающих выполнения операций сырого ввода-вывода | Count | autoavgmaxmin |
| builtin:host.kernelThreads.running | AIX Kernel threads runnable Количество выполняемых потоков (запущенных или ожидающих времени выполнения) | Count | autoavgmaxmin |

Memory

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.mem.avail.bytes | Memory available Объём доступной памяти (ОЗУ) на хосте. | Byte | autoavgmaxmin |
| builtin:host.mem.avail.pct | Memory available % Процент доступной памяти (ОЗУ) на хосте. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.kernel | Kernel memory Память, используемая ядром системы. | Byte | autoavgmaxmin |
| builtin:host.mem.recl | Memory reclaimable Использование памяти для конкретных целей. Возвращаемая память рассчитывается как доступная память минус свободная память. | Byte | autoavgmaxmin |
| builtin:host.mem.total | Memory total Объём установленной памяти (ОЗУ) в системе. | Byte | autovalue |
| builtin:host.mem.usage | Memory used % Процент используемой памяти. Рассчитывается как: использовано = всего − доступно. | Percent (%) | autoavgmaxmin |
| builtin:host.mem.used | Memory used Используемая память рассчитывается как: использовано = всего − доступно. | Byte | autoavgmaxmin |

Availability

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.availability.state | Host availability Метрика состояния доступности хоста с интервалом 1 минута | Count | autovalue |
| builtin:host.uptime | Host uptime Время с момента последней перезагрузки хоста. Требуется OneAgent 1.259+. | Second | autoavgmaxmin |

Disk

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.disk.avail | Disk available Объём свободного места, доступного пользователю в файловой системе. | Byte | autoavgmaxmin |
| builtin:host.disk.bytesRead | Disk read bytes per second Скорость чтения из файловой системы в байтах в секунду | Byte/second | autoavgmaxmin |
| builtin:host.disk.bytesWritten | Disk write bytes per second Скорость записи в файловую систему в байтах в секунду | Byte/second | autoavgmaxmin |
| builtin:host.disk.free | Disk available % Процент свободного места, доступного пользователю в файловой системе. | Percent (%) | autoavgmaxmin |
| builtin:host.disk.used | Disk used Объём использованного пространства в файловой системе | Byte | autoavgmaxmin |

Network

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:host.net.nic.bytesRx | NIC bytes received Байты, полученные сетевым интерфейсом на хосте | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.bytesTx | NIC bytes sent on host Байты, отправленные сетевым интерфейсом на хосте | Byte/second | autoavgmaxmin |
| builtin:host.net.nic.linkUtilRx | NIC receive link utilization Использование канала приёма сетевого интерфейса на хосте | Percent (%) | autoavgmaxmin |
| builtin:host.net.nic.linkUtilTx | NIC transmit link utilization Использование канала передачи сетевого интерфейса на хосте | Percent (%) | autoavgmaxmin |

## Мониторинг виртуализации

Dynatrace поддерживает [мониторинг виртуализации](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace."). Для мониторинга виртуальных компонентов вашей среды необходимо выполнить дополнительный шаг после начальной настройки. Подробнее см. в разделе [Настройка мониторинга виртуализации](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.").

## Часто задаваемые вопросы

Что происходит при внедрении OneAgent в отслеживаемую технологию?

При внедрении внедряемый модуль становится динамически связанным с отслеживаемой технологией. Следовательно, он становится неотъемлемой частью отслеживаемого процесса и может быть удалён только при перезапуске процесса. В зависимости от ОС (Windows/Linux/AIX) внедрение выполняется несколько по-разному, но результат схож.

Я отключил внедрение, но вижу, что модули глубокого кода Dynatrace всё ещё внедрены в отслеживаемые технологии.

Правила внедрения действуют в момент запуска процесса поддерживаемой технологии. После запуска модуль глубокого мониторинга кода OneAgent остаётся динамически связанным с отслеживаемой технологией и может быть выгружен только путём перезапуска отслеживаемого процесса.

Я перезапустил/отключил/остановил OneAgent, но внедрённые модули остаются активными.

При внедрении внедряемый модуль становится динамически связанным с отслеживаемой технологией. Следовательно, он становится неотъемлемой частью отслеживаемого процесса и может быть удалён только путём перезапуска отслеживаемого процесса.

Как OneAgent отслеживает процессы?

OneAgent внедряется в процесс каждый раз, когда в системе запускается новый процесс. OneAgent идентифицирует запущенный процесс (по имени, местоположению, пространству пользователя и т. д.) и, если он поддерживается для внедрения и правила внедрения не исключают его, устанавливает динамическую связь между отслеживаемым процессом и одним из модулей глубокого мониторинга кода OneAgent.

Я отключил OneAgent в веб-интерфейсе, но процесс всё ещё активен на хосте и сетевой трафик между OneAgent и кластером Dynatrace продолжается.

Отключённые OneAgents фактически прекращают мониторинг вашей среды. Однако ядро OneAgent, отвечающее за связь с кластером Dynatrace, остаётся активным. Поскольку связь между OneAgent и кластерами Dynatrace всегда инициируется со стороны OneAgent, он должен продолжать отправлять своё состояние и запрашивать у кластера, нужно ли возобновить мониторинг.