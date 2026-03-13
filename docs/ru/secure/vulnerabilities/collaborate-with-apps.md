---
title: Integrate vulnerability insights across Dynatrace and external apps
source: https://www.dynatrace.com/docs/secure/vulnerabilities/collaborate-with-apps
scraped: 2026-03-01T21:19:36.163432
---

# Интеграция аналитики уязвимостей между Dynatrace и внешними приложениями

# Интеграция аналитики уязвимостей между Dynatrace и внешними приложениями

* Последняя версия Dynatrace
* Практическое руководство
* Обновлено 9 сент. 2025

Dynatrace не просто обнаруживает уязвимости — он помогает вам действовать. Вы можете переходить между приложениями Dynatrace для получения более глубокого контекста, делиться результатами с внешними инструментами и автоматизировать рабочие процессы устранения для ускорения реагирования и снижения рисков.

## Навигация между приложениями

Интерактивные элементы в ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, такие как связанные сущности, затронутые группы процессов, узлы Kubernetes или доступные ресурсы данных, служат точками входа в другие приложения Dynatrace, позволяя изучать связанный контекст и принимать обоснованные решения.

* **Примеры**:

  + При просмотре раздела **Exploit attempts** уязвимости на уровне кода в ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** вы можете либо выбрать отдельную попытку эксплуатации, либо использовать кнопку **View all related exploit attempts** для доступа к подробной информации в [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Понимание, сортировка и расследование обнаруженных угроз и оповещений."). Это позволяет исследовать технические детали, сопоставлять доказательства из среды выполнения и определять, является ли уязвимость объектом активной атаки, что помогает расставлять приоритеты устранения на основе реального риска.
  + При просмотре уязвимости, связанной с узлом Kubernetes, в ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** вы можете выбрать затронутый узел из обзора узлов Kubernetes, чтобы перейти непосредственно в [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/docs/observe/infrastructure-observability/kubernetes-app "Мониторинг и оптимизация Kubernetes с помощью Dynatrace. Получайте данные в реальном времени о состоянии кластеров и рабочих нагрузок."), где вы можете оценить его состояние, зависимости и влияние на рабочие нагрузки.

Навигация также работает в обратном направлении. При изучении сущностей в других приложениях Dynatrace, таких как ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** или ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, вы можете встретить индикаторы уязвимостей или ссылки, которые направят вас непосредственно в ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** для более глубокого анализа.

* **Примеры**:

  + Из [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/docs/observe/infrastructure-observability/kubernetes-app "Мониторинг и оптимизация Kubernetes с помощью Dynatrace. Получайте данные в реальном времени о состоянии кластеров и рабочих нагрузок."), при выборе уязвимости в разделе **Vulnerabilities** узла или рабочей нагрузки открывается ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** с предварительно применённым фильтром для этой конкретной уязвимости.
  + Из [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Мониторинг хостов, ВМ, процессов и сетей для обнаружения проблем и повышения производительности инфраструктуры."), при выборе индикатора уязвимости в правом верхнем углу страницы открывается ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** с фильтрацией по этому хосту.

Эта двунаправленная навигация гарантирует, что вы всегда находитесь в одном клике от полного контекста безопасности.

## Обмен данными и автоматизация с внешними приложениями

Используйте [коннекторы Workflows](/docs/analyze-explore-automate/workflows/actions "Используйте готовые действия Dynatrace для ваших рабочих процессов и интегрируйте Dynatrace со сторонними системами.") для обмена данными об уязвимостях с внешними платформами и автоматизации задач по устранению.

* **Примеры**:

  + Автоматическое создание задач в Jira при обнаружении новых уязвимостей или превышении пороговых значений с помощью [коннектора Jira](/docs/analyze-explore-automate/workflows/actions/jira "Автоматизируйте создание, переход, комментирование и назначение задач Jira на основе событий и расписаний ваших рабочих процессов.").
  + Отправка оповещений в реальном времени в определённые каналы или людям с помощью [коннектора Slack](/docs/analyze-explore-automate/workflows/actions/slack "Отправка сообщений в рабочие пространства Slack") или [коннектора Microsoft Teams](/docs/analyze-explore-automate/workflows/actions/microsoft-teams "Отправка сообщений в Microsoft Teams").
  + Запуск рабочих процессов устранения с помощью [коннектора Red Hat Ansible](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible "Автоматизируйте выполнение заданий Ansible на основе данных мониторинга и событий.") или [коннектора Jenkins](/docs/analyze-explore-automate/workflows/actions/jenkins "Автоматизируйте конвейеры в Jenkins.").

Эти интеграции помогают обеспечить своевременное получение нужными командами актуальной и полезной информации без ручных усилий.

## Автоматизация рабочих процессов устранения

Используйте приложение [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Автоматизируйте ИТ-процессы с помощью Dynatrace Workflows — реагируйте на события, планируйте задачи и подключайте сервисы.") для автоматизации действий на основе серьёзности, типа уязвимости или затронутых сущностей.

* **Примеры**:

  + Автоматическое назначение задач по устранению в Jira.
  + Отправка оповещений в определённые каналы в Slack.
  + Запуск пользовательских скриптов или заданий CI/CD с помощью коннекторов, таких как Ansible или Jenkins.

Это обеспечивает проактивное и масштабируемое управление уязвимостями во всей вашей среде.

## Скачивание данных об уязвимостях в формате CSV

Вы можете скачать данные из таблицы уязвимостей в виде файла CSV для внешнего анализа или отчётности.

Для скачивания:

1. На странице **Prioritization** примените фильтры для сужения результатов.
2. Выберите ![Download table](https://dt-cdn.net/images/download-table-data-ebb09d49cd.svg "Download table"), чтобы сохранить текущее представление в виде файла CSV.

Скачанный файл отражает фильтры, применённые на момент скачивания.
