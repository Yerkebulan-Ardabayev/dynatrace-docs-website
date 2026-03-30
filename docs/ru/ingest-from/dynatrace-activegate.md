---
title: Dynatrace ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate
scraped: 2026-03-06T21:12:45.606066
---

* Latest Dynatrace
* 3-min read

### ActiveGate действует как безопасный прокси

Dynatrace ActiveGate действует как безопасный прокси между Dynatrace OneAgent и кластерами Dynatrace или между Dynatrace OneAgent и другими ActiveGate, расположенными ближе к кластеру Dynatrace.
Он обеспечивает присутствие Dynatrace в вашей локальной сети. Таким образом, он позволяет свести взаимодействие с Dynatrace к одной точке, доступной локально. Помимо удобства, это решение оптимизирует объём трафика, снижает сложность сети и затраты. Оно также обеспечивает безопасность закрытых сетей.

### ActiveGate выполняет мониторинг

Помимо маршрутизации данных мониторинга, собранных OneAgent, Dynatrace ActiveGate также способен выполнять задачи мониторинга, используя API для запроса и мониторинга широкого спектра технологий. Список отслеживаемых технологий не ограничен и может динамически расширяться. Он включает облачные технологии и технологии центров обработки данных, например AWS, VMware, Azure, Kubernetes, OpenShift, Cloud Foundry, Google Cloud, Oracle, SNMP, WMI, Prometheus и многие другие.

###

Схема функций ActiveGate

![Функции ActiveGate](https://dt-cdn.net/images/ag-general-005-1-1048-b2d55cede0.png)

### Типы, назначения и функциональные модули ActiveGate

Вам потребуются различные типы ActiveGate — **Environment ActiveGate** или **Cluster ActiveGate** — в зависимости от решения развёртывания Dynatrace, которое вы используете, а также от назначения, для которого вы используете Dynatrace.

Если вы используете [SaaS-решение](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md#saas-scheme "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.") Dynatrace, вам нужно установить только Environment ActiveGate.

Для использования определённых функциональных возможностей ActiveGate, называемых модулями, вам необходим ActiveGate с установленными или активированными этими модулями. При установке ActiveGate вы выбираете основное назначение установки, а затем, в зависимости от назначения, можете установить или активировать различный набор функциональных модулей.

ActiveGate может быть развёрнут обычным способом — на физическом или виртуальном хосте — это **развёртывание ActiveGate на хосте**.
ActiveGate, упакованный в контейнер, называется **контейнеризированным развёртыванием ActiveGate**.

### Назначения и функциональность ActiveGate

Маршрутизация трафика OneAgent

Мониторинг облачных сред и удалённых технологий

Запуск синтетических мониторов

Маршрутизация трафика z/OS

Dynatrace API

Функциональность по типу ActiveGate

### Системные и аппаратные требования

ActiveGate для маршрутизации/мониторинга, на Linux

ActiveGate для маршрутизации/мониторинга, на Windows

ActiveGate с поддержкой синтетического мониторинга

ActiveGate для маршрутизации трафика z/OS в Dynatrace

### См. также

Схемы подключения ActiveGate

## Установка

Операционные системы

Контейнерные платформы

[Linux](dynatrace-activegate/installation/linux.md) [Windows](dynatrace-activegate/installation/windows.md)

[Kubernetes](dynatrace-activegate/activegate-in-container.md) [OpenShift](dynatrace-activegate/activegate-in-container.md)