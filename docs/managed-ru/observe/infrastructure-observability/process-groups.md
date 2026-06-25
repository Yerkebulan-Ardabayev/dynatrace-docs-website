---
title: Группы процессов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups
scraped: 2026-05-12T11:09:34.422097
---

# Process groups

# Группы процессов

* Explanation
* 3-min read
* Published Jan 08, 2019

Dynatrace автоматически объединяет связанные процессы в группы процессов. «Группа процессов» (process group) — это логический кластер процессов, принадлежащих одному приложению или единице развёртывания и выполняющих одну функцию на нескольких хостах. Группы процессов являются ключевыми строительными блоками большинства современных веб-приложений.

Dynatrace автоматически [обнаруживает типы приложений](/managed/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "The technologies and versions behind a process"), такие как Tomcat, JBoss, Apache HTTP Server, MongoDB и многие другие технологии. Для создания групп процессов Dynatrace использует конкретные свойства процессов. Для Tomcat — `CATALINA_HOME` и `CATALINA_BASE` для различения кластеров Tomcat. Для JBoss — `JBOSS_HOME` и конфигурацию кластера JBoss. Для универсальных Java-процессов — JAR-файл или главный класс, используемый для запуска процесса. Существуют также многочисленные специализированные механизмы обнаружения. Например, Dynatrace может обнаруживать:

* Кластеры и домены IBM WebSphere
* Кластеры и домены Oracle WebLogic
* Кластеры Cassandra
* Движки Tibco BusinessWorks
* Приложения Kubernetes
* Приложения OpenShift
* Приложения Cloud Foundry
* Azure Web Apps
* И другие…

На каждой странице обзора процесса свойства отображаются при раскрытии раздела **Properties and tags**.

### Влияние на сервисы

Группы процессов являются основой для обнаружения сервисов, поскольку каждая группа процессов рассматривается как логический кластер или отдельная единица развёртывания. Когда Dynatrace обнаруживает «один и тот же» сервис в разных группах процессов, он рассматривает их как отдельные сервисы (например, один процесс может использоваться в staging, другой — в production).

Если вы укажете Dynatrace объединить две отдельные группы процессов в одну, это приведёт к объединению также сервисов, работающих на этих процессах.

### Настройка групп процессов

Для удовлетворения конкретных потребностей мониторинга процессов Dynatrace позволяет:

* [Настраивать имена групп процессов](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming").
* [Изменять состав групп процессов по умолчанию](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").
* [Создавать новые группы процессов для случаев, когда технология процессов не распознаётся Dynatrace](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

## Основные концепции

[![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies")

### Какие технологии лежат в основе отдельных процессов?

Технологии и версии, лежащие в основе процесса.](/managed/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "The technologies and versions behind a process")[### Какие процессы наиболее важны?

Просмотр наиболее важных процессов для мониторинга и группировки.](/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.")

## Конфигурация

[### Обнаружение облачных приложений и рабочих нагрузок

Обнаружение облачных приложений и рабочих нагрузок, определение правил для объединения похожих нагрузок Kubernetes в группы процессов.](/managed/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection "Detect cloud applications and workloads, and define rules to merge similar Kubernetes workloads into process groups.")[### Определение пользовательских метаданных группы процессов

Настройка собственных метаданных процессов в соответствии с потребностями организации или среды.](/managed/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")[### Обнаружение групп процессов

Настройка обнаружения групп процессов.](/managed/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection")[### Глубокий мониторинг процессов

Настройка мониторинга групп процессов.](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring")[### Именование групп процессов

Настройка именования групп процессов.](/managed/observe/infrastructure-observability/process-groups/configuration/pg-naming "Ways to customize process-group naming")

## Мониторинг

[### Анализ отзывчивости процессов

Оценка производительности процессов с помощью метрики отзывчивости.](/managed/observe/infrastructure-observability/process-groups/monitoring/analyze-process-responsiveness "Use responsiveness to assess process performance.")[### Анализ процессов

Анализ процессов, включая метрики процессов, уязвимости и доступность.](/managed/observe/infrastructure-observability/process-groups/monitoring/analyze-processes "The Dynatrace approach to process monitoring and process grouping")[### Мониторинг сетевых соединений процессов

Анализ сетевых соединений конкретного процесса.](/managed/observe/infrastructure-observability/process-groups/monitoring/monitor-process-specific-network-connections "Analyze process-specific network connections.")[### Обзор всех технологий в среде

Сводка производительности всех технологий в вашей среде.](/managed/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Get a summary of the performance of all the technologies in your environment.")[### Мониторинг доступности и оповещения для групп процессов

Включение мониторинга доступности групп процессов для получения оповещений при отключении или аварийном завершении процессов.](/managed/observe/infrastructure-observability/process-groups/monitoring/process-group-availability-monitoring-and-alerting "Enable process-group availability monitoring to get alerts if processes go offline or crash.")