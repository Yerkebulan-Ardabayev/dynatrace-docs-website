---
title: Сети
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/networks
scraped: 2026-05-12T11:22:19.511310
---

# Сети

# Сети

* Explanation
* 2-min read
* Updated on Apr 19, 2022

Мониторинг инфраструктуры Dynatrace выходит за рамки хостов и процессов и включает сетевые коммуникации. Он обеспечивает понимание качества взаимодействия процессов, доступа к необходимым ресурсам и использования полосы пропускания сети. Это помогает обнаруживать проблемы, вызванные не ограничениями ресурсов или медленным временем ответа, а плохой связностью или нерациональным использованием сетевых ресурсов. Мониторинг пакетов данных, передаваемых между процессами и хостами, обеспечивает более глубокую видимость производительности и надёжности всей среды.

## Накладные расходы на мониторинг сети

Мониторинг сети в Dynatrace создаёт минимальные накладные расходы, величина которых зависит от объёма трафика. Dynatrace автоматически отслеживает эти накладные расходы и применяет ограничение, если они превышают 5% доступного CPU. При срабатывании ограничения сетевой модуль приостанавливается менее чем на 3 минуты. Если после повторного включения порог по-прежнему превышен, продолжительность паузы каждый раз удваивается — вплоть до максимума в 45 минут — до тех пор, пока использование ресурсов не вернётся к приемлемому уровню.

## Конфиденциальность данных

* Dynatrace анализирует сетевые пакеты в памяти в режиме реального времени.
* Dynatrace не сохраняет пакеты на диск ни на мониторируемых хостах, ни в кластере Dynatrace.
* Dynatrace анализирует только заголовки пакетов, но не их содержимое.

[#### Мониторинг сетевых коммуникаций

Изучите основы мониторинга сети Dynatrace, включая способы анализа работоспособности сети и распознавания распространённых сетевых проблем.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/how-to-monitor-network-communication)[#### Обнаружение сетевых ошибок

Узнайте, как ошибки, например потеря пакетов и повторные передачи на сетевом уровне, могут влиять на производительность и связность сервисов.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/detect-network-errors)[#### Расширенный мониторинг сети

Расширение мониторинга сети с помощью метрик сетевого трафика на контейнеризованных хостах Linux с использованием NetTracer.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/network-monitoring-with-nettracer)[#### Устранение неполадок мониторинга сети

Подробнее об устранении неполадок мониторинга сети.

* Troubleshooting

Read this troubleshooting guide](/managed/observe/infrastructure-observability/networks-classic/troubleshoot-network-monitoring)[#### Приём записей NetFlow в Dynatrace

Узнайте, как принимать записи NetFlow в Dynatrace.

* How-to guide

Read this guide](/managed/observe/infrastructure-observability/networks-classic/ingest-netflow-records)

## Связанные темы

* [Мониторинг сети](https://www.dynatrace.com/platform/network-monitoring/)