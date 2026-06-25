---
title: Анализ процессов
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/process-groups/monitoring/analyze-processes
scraped: 2026-05-12T11:37:53.360299
---

# Analyze processes

# Анализ процессов

* How-to guide
* 6-min read
* Updated on Jul 30, 2024

На любой странице **Host** можно просмотреть список процессов, вносящих вклад в каждую метрику работоспособности хоста (например, **Memory** на рисунке ниже).

![Host with consuming processes](https://dt-cdn.net/images/processes-new-810-08dd1cb78f.png)

Host with consuming processes

Нажмите кнопку **Consuming processes** для просмотра списка процессов, вносящих вклад в выбранную метрику работоспособности.

![Processes table](https://dt-cdn.net/images/processes-new-2-1173-baad2315da.png)

Processes table

Отобразив список участвующих процессов, нажмите на любой процесс для его детального изучения на отдельной странице **Process**. На каждой странице процесса вы найдёте статистику потребления CPU, памяти, сетевых ресурсов (см. рисунок ниже) и другие [метрики инфраструктуры](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace."). Там же вы найдёте сведения о связанных событиях, проблемах и зависимостях.

![Host detail - process details](https://dt-cdn.net/images/hostprocesses2-1225-b7b9608767.png)

Host detail - process details

## Уязвимости

Раздел **Vulnerabilities** на странице деталей процесса показывает пять наиболее серьёзных [уязвимостей сторонних компонентов](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.") и [уязвимостей на уровне кода](/managed/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/manage-code-level-vulnerabilities "Monitor the code-level vulnerabilities in your environment."), связанных с данным процессом.

Для просмотра этого раздела необходимо [активировать и включить Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.").

Если у вас недостаточно [прав безопасности](/managed/secure/application-security#permissions "Access the Dynatrace Application Security functionalities.") для зоны управления, в которую включён процесс, данный раздел не отображается.

* Выберите уязвимость для просмотра подробностей и оценки её серьёзности и влияния на вашу среду.
* Для просмотра полного списка обнаруженных уязвимостей, затрагивающих данный процесс, выберите **Show all third-party vulnerabilities** / **Show all code-level vulnerabilities**.

Пример уязвимостей сторонних компонентов:

![Process overview: TPV](https://dt-cdn.net/images/process-tpv-775-92fe606d07.png)

Process overview: TPV

Пример уязвимостей на уровне кода:

![Process overview: CLV](https://dt-cdn.net/images/process-clv-774-d460fb39ba.png)

Process overview: CLV

## Доступность процессов

Помимо записи [типов событий](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories "Learn about different categories of events and supported event types, along with their severity levels, and the logic behind raising them."), таких как завершение и перезапуск процессов, Dynatrace также отображает [аварийные завершения процессов](/managed/observe/application-observability/profiling-and-optimization/crash-analysis "Learn how Dynatrace can help you gain insight into process crashes."). Это особенно важно для мониторинга доступности сервисов. Сервисы наследуют доступность от процессов, на которых работают. Dynatrace считает сервис недоступным, когда вся группа процессов, на которой он работает, становится недоступной. Это может произойти при завершении или аварийном завершении процесса (см. рисунок ниже).

![Process crashed](https://dt-cdn.net/images/process-crashed-877-1cbf72dbbc.png)

Process crashed

Dynatrace позволяет различать сервисы, доступные, но не получающие трафика, и сервисы, недоступные из-за остановки или аварийного завершения базовых процессов. В случае аварийного завершения процесса Dynatrace фиксирует сбой и информирует о его влиянии на сервисы и приложения (см. рисунок ниже).

![Root cause crashed process](https://dt-cdn.net/images/root-cause-crashed-process-634-b3ccae5e57.png)

Root cause crashed process

## Доступность экземпляров групп процессов

OneAgent version 1.291+

Доступность экземпляров групп процессов (PGI) можно отслеживать с помощью метрики `builtin:pgi.availability.state` (`dt.process.availability` в Grail).

Состояние обозначается одним из следующих значений:

* **Available** — экземпляр группы процессов доступен и передаёт данные.
* **Unavailable** — экземпляр группы процессов недоступен и не передаёт данные.
* **Unimportant** — экземпляр группы процессов доступен, но не передаётся в кластер, поскольку стал неважным. Подробнее см. в разделе [Which are the most important processes?](/managed/observe/infrastructure-observability/process-groups/basic-concepts/which-are-the-most-important-processes "Display the most important processes for monitoring and process grouping.").

Значения метрики опрашиваются OneAgent:

* Если состояние `available` — каждую минуту.
* Если состояние `unavailable` или `unimportant` — однократно. После отправки выборки с этим состоянием OneAgent прекращает передавать метрику для данного экземпляра группы процессов.