---
title: Хосты
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/hosts
scraped: 2026-05-12T12:03:14.492484
---

# Hosts

# Хосты

* Explanation
* 3-min read
* Published Sep 25, 2018

Производительность хостов отслеживается на нескольких страницах Dynatrace — от высокоуровневых метрик работоспособности на плитках панели мониторинга до специальных страниц для каждого хоста. Полностековый мониторинг инфраструктуры начинается автоматически, как только Dynatrace OneAgent запускается и начинает сбор информации о производительности и событиях на ваших хостах.

## Обзор

### Группы хостов

По мере роста и усложнения сред, отслеживаемых Dynatrace, охватывающих разные центры обработки данных и множество приложений, [группы хостов](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") приобретают всё большее значение. Группы хостов позволяют настраивать хосты по группам, избирательно развёртывать версии OneAgent и по-разному отслеживать метрики сервисов в зависимости от платформы, на которой они работают.

### Анализ производительности виртуализации

Dynatrace показывает, как виртуальные машины в вашей среде влияют на производительность приложений и сервисов. После включения виртуализации в мониторинг производительности Dynatrace вы получаете полное представление о стеке инфраструктуры и его поведении.

### Теги в конфигурационном файле на основе хостов

В динамических или крупных средах ручная расстановка тегов хостов может быть непрактичной. Для динамических развёртываний с часто меняющимися экземплярами и именами хостов (например, AWS или MS Azure) можно [использовать специальный конфигурационный файл для программного применения тегов к хостам](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.").

### Пользовательские имена хостов

Dynatrace, как правило, присваивает обнаруженным хостам имена на основе их DNS-имён, точно так, как они определяются OneAgent. Для улучшения читаемости можно [создать пользовательские имена хостов](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name."), которые будут отображаться вместо обнаруженных.

## Конфигурация

[### Режимы мониторинга OneAgent

Узнайте, что входит в режимы Infrastructure и Discovery мониторинга и как их включить.](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.")[### Обнаружение аномалий хостов

Настройте обнаружение аномалий хостов, включая пороги проблем и событий.](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection "Configure host anomaly detection, including problem and event thresholds.")[### Определение тегов и метаданных для хостов

Расставьте теги и задайте дополнительные свойства для отслеживаемого хоста.](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")[### Исключение дисков и сетевого трафика из мониторинга хостов

Исключите выбранные диски и сетевой трафик из мониторинга хостов.](/managed/observe/infrastructure-observability/hosts/configuration/exclude-disks-and-network-traffic "Learn how to exclude selected disks and network traffic from host monitoring.")[### Организация среды с помощью групп хостов

Узнайте, как Dynatrace позволяет организовывать хосты, процессы и сервисы с помощью групп хостов.](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.")[### Задание пользовательских имён хостов

Измените имя отслеживаемого хоста.](/managed/observe/infrastructure-observability/hosts/configuration/set-custom-host-names-in-dynamic-environments "Learn how to change a monitored host name.")

## Мониторинг

[### Режимы мониторинга

Изучите режимы мониторинга в Dynatrace.](/managed/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.")[### Мониторинг хостов с помощью Dynatrace

Отслеживайте хосты с помощью Dynatrace.](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.")[### Мониторинг служб ОС

Улучшите видимость инфраструктуры за счёт мониторинга доступности служб операционной системы.](/managed/observe/infrastructure-observability/hosts/monitoring/os-services "Improve the visibility of your infrastructure by monitoring the availability of operating system services.")[### Классический мониторинг служб Windows

Улучшите видимость инфраструктуры за счёт мониторинга доступности служб Windows.](/managed/observe/infrastructure-observability/hosts/monitoring/windows-services "Learn how to improve the visibility of your infrastructure by monitoring the availability of Windows services.")[### Доступность процессов

Отслеживайте доступность и производительность ключевых процессов на хостах.](/managed/observe/infrastructure-observability/hosts/monitoring/process-availability "Monitor availability and performance of the key processes on your hosts.")

## Диагностика

[![OneAgent](https://cdn.bfldr.com/B686QPH3/at/g8mmkkpfmgwbxcjz54pvfsx/OneAgent.svg?auto=webp&width=72&height=72 "OneAgent")

### Диагностика OneAgent

Узнайте, как запустить диагностику OneAgent.](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics")