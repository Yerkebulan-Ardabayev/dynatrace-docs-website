---
title: Расширенный мониторинг сети
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/networks-classic/network-monitoring-with-nettracer
scraped: 2026-05-12T12:03:18.394064
---

# Расширенный мониторинг сети

# Расширенный мониторинг сети

* How-to guide
* 5-min read
* Updated on Oct 03, 2025

Расширение мониторинга сети с помощью метрик сетевого трафика на контейнеризованных хостах Linux.

С добавлением сетевых метрик к контейнеризованным хостам анализ первопричин Davis® будет их использовать и расширит анализ для обеспечения видимости проблем, связанных с сетью. Интенсивный сетевой трафик на конкретных узлах является признаком того, что следует рассмотреть масштабирование кластера.

## NetTracer

NetTracer — это инструмент с открытым исходным кодом для отслеживания TCP-событий и сбора метрик сетевых соединений в Linux. Он состоит из двух частей:

* программа BPF для сбора данных
* бинарный файл, представляющий данные в структурированном или полуструктурированном формате

Преимущества:

* Может отслеживать TCP-события: **connect**, **accept** и **close**
* Может собирать метрики для каждого отслеженного соединения
* Высокопроизводительное приложение (написано на C и C++)
* Независимо от версии и конфигурации ядра (Linux kernel 4.15 и выше)
* Проект с открытым исходным кодом ([NetTracer](https://github.com/dynatrace-oss/nettracer-bpf))

NetTracer определяет TCP-соединение IPv4 и IPv6 по адресу и порту источника, адресу и порту назначения, PID взаимодействующего процесса и сетевому пространству имён.

Используя это определение TCP-соединения, он собирает следующие метрики:

* Отправленные байты
* Полученные байты
* Отправленные пакеты
* Полученные пакеты
* Повторно переданные пакеты
* Время прохождения туда-обратно (RTT, в микросекундах)
* Дисперсия RTT (не используется в анализе Dynatrace)

По умолчанию NetTracer включён в виде бинарного файла `oneagentnettracer` с каждой установкой OneAgent и может быть включён через веб-интерфейс Dynatrace.

## Поддерживаемые платформы NetTracer

NetTracer официально поддерживает версии ядра Linux 4.15 и выше, однако другие компоненты Dynatrace, сосуществующие с NetTracer на конкретном хосте, имеют специфические требования и поддерживаются на конкретных дистрибутивах Linux. В следующей таблице перечислены протестированные и наиболее безопасные дистрибутивы Linux для использования с NetTracer и Dynatrace.

| Дистрибутив | Архитектура | Версия |
| --- | --- | --- |
| RedHat Enterprise Linux | x86\_64 | 8.0 и выше |
| CentOS | x86\_64 | 8.0 и выше |
| Ubuntu | x86\_64 | 18.04 LTS и выше |

## Включение NetTracer

При включении OneAgent будет использовать NetTracer для сбора сетевых данных из контейнеров, но только для хостов Linux.

Для включения NetTracer на конкретном хосте Linux:

1. Перейдите в **Hosts** и выберите хост Linux.
2. На странице обзора хоста выберите **More** (**…**) > **Settings** в правом верхнем углу страницы.
3. На странице **Host settings** выберите **NetTracer traffic** и включите **Enable NetTracer traffic network monitoring**.

Для глобального включения NetTracer на всех хостах Linux:

1. Перейдите в **Settings** > **Network & Discovery** > **NetTracer traffic**.
2. Включите **Enable NetTracer traffic network monitoring**.

Для корректной работы NetTracer OneAgent должен быть установлен в режиме мониторинга Full-Stack или Infrastructure, поскольку эти режимы включают функцию мониторинга сети. При установке OneAgent в ограниченном режиме (например, режиме мониторинга Discovery) NetTracer может не работать должным образом. Подробности см. в разделе [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Подробнее о доступных режимах мониторинга при использовании OneAgent.").

## Встроенные метрики NetTracer

| Ключ метрики | Название и описание | Единица | Агрегации |
| --- | --- | --- | --- |
| builtin:tech.nettracer.bytes\_rx | Полученные байты. Количество полученных байт | Байт | autoavgcountmaxminsum |
| builtin:tech.nettracer.bytes\_tx | Переданные байты. Количество переданных байт | Байт | autoavgcountmaxminsum |
| builtin:tech.nettracer.pkts\_retr | Повторно переданные пакеты. Количество повторно переданных пакетов | Количество | autovalue |
| builtin:tech.nettracer.pkts\_rx | Полученные пакеты. Количество полученных пакетов | Количество | autovalue |
| builtin:tech.nettracer.pkts\_tx | Переданные пакеты. Количество переданных пакетов | Количество | autovalue |
| builtin:tech.nettracer.retr\_percentage | Процент повторных передач. Процент повторно переданных пакетов | Процент (%) | autoavgmaxmin |
| builtin:tech.nettracer.rtt | Время прохождения туда-обратно (RTT). RTT в миллисекундах. Агрегирует данные активных сессий | Миллисекунда | autoavgcountmaxminsum |
| builtin:tech.nettracer.traffic | Сетевой трафик. Суммарный входящий и исходящий сетевой трафик в битах в секунду | бит/с | autovalue |
| builtin:tech.nettracer.traffic\_rx | Входящий трафик. Входящий сетевой трафик в битах в секунду | бит/с | autovalue |
| builtin:tech.nettracer.traffic\_tx | Исходящий трафик. Исходящий сетевой трафик в битах в секунду | бит/с | autovalue |

### Вычисляемые метрики NetTracer

Следующие метрики, доступные для NetTracer, являются вычисляемыми:

* `builtin:tech.nettracer.retr_percentage` (Повторные передачи)

  Повторные передачи = повторно переданные пакеты / (повторно переданные пакеты + переданные пакеты) × 100
* `builtin:tech.nettracer.traffic_rx` (Входящий трафик)

  Входящий трафик = (сумма полученных байт × 8) в секунду
* `builtin:tech.nettracer.traffic_tx` (Исходящий трафик)

  Исходящий трафик = (сумма переданных байт:sum × 8) в секунду
* `builtin:tech.nettracer.traffic` (Сетевой трафик)

  Сетевой трафик = ((сумма полученных байт + сумма переданных байт) × 8) в секунду

## Измерения NetTracer

| Ключ метрики | Измерение | Значение | Единица |
| --- | --- | --- | --- |
| `builtin:tech.nettracer.bytes_rx` | `dt.entity.process_group_instance`  `dt.entity.process_group`  `dt.entity.host` | Gauge, где:  sum = количество байт из всех сессий за данный временной интервал  avg/min/max = среднее/минимальное/максимальное количество байт на сессию за данный временной интервал  count = количество сессий за данный временной интервал | Байты |
| `builtin:tech.nettracer.bytes_tx` | `dt.entity.process_group_instance`  `dt.entity.process_group`  `dt.entity.host` | Gauge, где:  sum = количество байт из всех сессий за данный временной интервал  avg/min/max = среднее/минимальное/максимальное количество байт на сессию за данный временной интервал  count = количество сессий за данный временной интервал | Байты |
| `builtin:tech.nettracer.pkts_rx` | `dt.entity.process_group_instance`  `dt.entity.process_group`  `dt.entity.host` | Счётчик, отправляющий дельты/сбрасывающий счётчик | Количество |
| `builtin:tech.nettracer.pkts_tx` | `dt.entity.process_group_instance`  `dt.entity.process_group`  `dt.entity.host` | Счётчик, отправляющий дельты/сбрасывающий счётчик | Количество |
| `builtin:tech.nettracer.pkts_retr` | `dt.entity.process_group_instance`  `dt.entity.process_group`  `dt.entity.host` | Счётчик, отправляющий дельты/сбрасывающий счётчик | Количество |
| `builtin:tech.nettracer.rtt` | `dt.entity.process_group_instance`  `dt.entity.process_group`  `dt.entity.host` | Gauge | Миллисекунды |

### Измерения контейнеров для NetTracer

Если процесс выполняется в контейнере, добавляются следующие измерения:

* `dt.entity.container_group_instance`
* `dt.entity.container_group`

В зависимости от типа развёртывания добавляются дополнительные измерения контейнера.

| Kubernetes | Docker (без Kubernetes) |
| --- | --- |
| `container.image.name` (если доступно)  `k8s.container.name`  `k8s.namespace.name`  `k8s.pod.name`  `k8s.pod.uid` | `container.image.name`  `container.name` |

## Где можно увидеть данные NetTracer?

После сбора данные NetTracer доступны в виде метрик в Dynatrace.

* **Data Explorer**: метрики можно использовать в [Data Explorer](/managed/analyze-explore-automate/explorer "Запрашивайте метрики и преобразуйте результаты для получения нужных аналитических данных.") для создания графиков и дашбордов с интересующими данными.
* **Страница экземпляра группы процессов**: перейдите на страницу экземпляра группы процессов и выберите вкладку **Networking**.

  ![Страница экземпляра группы процессов — сведения о сети](https://dt-cdn.net/images/pgi-page-networking-details-2172-bcb6d64191.png)

  Страница экземпляра группы процессов — сведения о сети
* **Обзор хоста**: перейдите на страницу обзора хоста и прокрутите вниз до раздела **Network analysis**.

  ![Анализ сети](https://dt-cdn.net/images/lde68092-dev-apps-dynatracelabs-com-ui-apps-dynatrace-classic-hosts-ui-entity-host-b8ec70b7dc022ec8-gtf-2h-gf-all-sessionid-4aquod8c7d1hqbf8-2-2913-bca5600276.png)

  Анализ сети

Разделы **Networking** и **Network analysis** содержат данные NetTracer в сочетании с другими сетевыми данными, анализируемыми для данного хоста. NetTracer собирает данные для контейнеризованных процессов, тогда как Network Agent — для нативных (то есть неконтейнеризованных) процессов.

## Характеристики NetTracer

* Из модуля `ebpf` NetTracer отслеживается только 4096 TCP-соединений.
* Информация о портах прослушивания требует активного TCP-соединения.