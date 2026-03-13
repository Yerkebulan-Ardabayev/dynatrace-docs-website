---
title: Process groups
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/process-groups
scraped: 2026-03-06T21:16:55.383877
---

# Группы процессов

# Группы процессов

* Classic
* Пояснение
* Чтение: 3 мин
* Опубликовано 08 янв. 2019

Dynatrace автоматически объединяет связанные процессы в группы процессов. Группа процессов — это логический кластер процессов, принадлежащих одному приложению или единице развёртывания и выполняющих одну и ту же функцию на нескольких хостах. Группы процессов являются ключевыми строительными блоками большинства современных веб-приложений.

Подробнее...

Dynatrace автоматически [определяет типы приложений](/docs/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "Технологии и версии, лежащие в основе процесса"), такие как Tomcat, JBoss, Apache HTTP Server, MongoDB и многие другие технологии. Для создания групп процессов Dynatrace использует определённые свойства процессов. Для Tomcat Dynatrace использует `CATALINA_HOME` и `CATALINA_BASE` для различения разных кластеров Tomcat. Для JBoss Dynatrace использует `JBOSS_HOME` и конфигурацию кластера JBoss. Для обычных Java-процессов Dynatrace использует JAR-файл или главный класс, использованный для запуска процесса. Существуют также многочисленные специализированные механизмы обнаружения. Например, Dynatrace может обнаруживать:

* Кластеры и домены IBM WebSphere
* Кластеры и домены Oracle WebLogic
* Кластеры Cassandra
* Движки Tibco BusinessWorks
* Приложения Kubernetes
* Приложения OpenShift
* Приложения Cloud Foundry
* Azure Web Apps
* И многое другое...

На странице обзора каждого процесса вы найдёте свойства, если развернёте раздел **Properties and tags**.

### Что это означает для сервисов?

Группы процессов являются основой для обнаружения сервисов, поскольку каждая группа процессов считается логическим кластером или единым развёртыванием. Когда Dynatrace обнаруживает «один и тот же» сервис в разных группах процессов, он рассматривает их как отдельные сервисы (например, один процесс может использоваться в тестовой среде, а другой — в продуктивной).

Если вы дадите Dynatrace команду объединить две отдельные группы процессов в одну, это также приведёт к объединению сервисов, работающих на этих процессах.

### Настройка групп процессов

Чтобы удовлетворить ваши потребности в мониторинге процессов, Dynatrace позволяет:

* [Настроить имена групп процессов](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Способы настройки именования групп процессов").
* [Изменить состав стандартных групп процессов](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения групп процессов").
* [Создать новые группы процессов в случаях, когда технология процессов не распознаётся Dynatrace](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения групп процессов").

## Базовые концепции

[![Технологии](https://dt-cdn.net/images/technologies-512-977161d83c.png "Технологии")

### Какие технологии лежат в основе отдельных процессов?

Технологии и версии, стоящие за процессом.](/docs/observe/infrastructure-observability/process-groups/basic-concepts/what-technologies-underlie-individual-processes "Технологии и версии, стоящие за процессом")[### Какие процессы наиболее важны?

Отображение наиболее важных процессов для мониторинга и группировки процессов.](/docs/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Отображение наиболее важных процессов для мониторинга и группировки процессов.")

## Конфигурация

[### Обнаружение облачных приложений и рабочих нагрузок

Обнаружение облачных приложений и рабочих нагрузок, а также определение правил для объединения похожих рабочих нагрузок Kubernetes в группы процессов.](/docs/observe/infrastructure-observability/process-groups/configuration/cloud-app-and-workload-detection "Обнаружение облачных приложений и рабочих нагрузок, а также определение правил для объединения похожих рабочих нагрузок Kubernetes в группы процессов.")[### Определение собственных метаданных группы процессов

Настройка собственных метаданных, связанных с процессами, на основе уникальных потребностей вашей организации или среды.](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Настройка собственных метаданных, связанных с процессами, на основе уникальных потребностей вашей организации или среды.")[### Обнаружение групп процессов

Настройка обнаружения групп процессов.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Способы настройки обнаружения групп процессов")[### Глубокий мониторинг процессов

Настройка мониторинга групп процессов.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Способы настройки мониторинга групп процессов")[### Именование групп процессов

Настройка именования групп процессов.](/docs/observe/infrastructure-observability/process-groups/configuration/pg-naming "Способы настройки именования групп процессов")

## Мониторинг

[### Анализ отзывчивости процессов

Использование отзывчивости для оценки производительности процессов.](/docs/observe/infrastructure-observability/process-groups/monitoring/analyze-process-responsiveness "Использование отзывчивости для оценки производительности процессов.")[### Анализ процессов

Анализ процессов, включая информацию о метриках процессов, уязвимостях и доступности.](/docs/observe/infrastructure-observability/process-groups/monitoring/analyze-processes "Подход Dynatrace к мониторингу и группировке процессов")[### Мониторинг сетевых подключений конкретных процессов

Анализ сетевых подключений конкретных процессов.](/docs/observe/infrastructure-observability/process-groups/monitoring/monitor-process-specific-network-connections "Анализ сетевых подключений конкретных процессов.")[### Обзор всех технологий, работающих в вашей среде

Получение сводки производительности всех технологий в вашей среде.](/docs/observe/infrastructure-observability/process-groups/monitoring/overview-of-all-technologies-running-in-my-environment "Получение сводки производительности всех технологий в вашей среде.")[### Мониторинг доступности групп процессов и оповещения

Включение мониторинга доступности групп процессов для получения оповещений, если процессы отключаются или аварийно завершаются.](/docs/observe/infrastructure-observability/process-groups/monitoring/process-group-availability-monitoring-and-alerting "Включение мониторинга доступности групп процессов для получения оповещений, если процессы отключаются или аварийно завершаются.")
