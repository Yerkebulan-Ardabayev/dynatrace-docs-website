---
title: Dynatrace ActiveGate
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate
scraped: 2026-03-06T21:12:45.606066
---

# Dynatrace ActiveGate

# Dynatrace ActiveGate

* Latest Dynatrace
* 3-min read
* Published Jul 23, 2018

### ActiveGate действует как безопасный прокси

Dynatrace ActiveGate действует как безопасный прокси между Dynatrace OneAgent и кластерами Dynatrace или между Dynatrace OneAgent и другими ActiveGate, расположенными ближе к кластеру Dynatrace.
Он обеспечивает присутствие Dynatrace в вашей локальной сети. Таким образом, он позволяет свести взаимодействие с Dynatrace к одной точке, доступной локально. Помимо удобства, это решение оптимизирует объём трафика, снижает сложность сети и затраты. Оно также обеспечивает безопасность закрытых сетей.

### ActiveGate выполняет мониторинг

Помимо маршрутизации данных мониторинга, собранных OneAgent, Dynatrace ActiveGate также способен выполнять задачи мониторинга, используя API для запроса и мониторинга широкого спектра технологий. Список отслеживаемых технологий не ограничен и может динамически расширяться. Он включает облачные технологии и технологии центров обработки данных, например AWS, VMware, Azure, Kubernetes, OpenShift, Cloud Foundry, Google Cloud, Oracle, SNMP, WMI, Prometheus и многие другие.

###

Схема функций ActiveGate

![Функции ActiveGate](https://dt-cdn.net/images/ag-general-005-1-1048-b2d55cede0.png)

### Типы, назначения и функциональные модули ActiveGate

Вам потребуются различные типы ActiveGate — **Environment ActiveGate** или **Cluster ActiveGate** — в зависимости от [решения развёртывания](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.") Dynatrace, которое вы используете, а также от [назначения](/docs/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применениях ActiveGate."), для которого вы используете Dynatrace.

Если вы используете [SaaS-решение](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#saas-scheme "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.") Dynatrace, вам нужно установить только Environment ActiveGate.

Для использования определённых функциональных возможностей ActiveGate, называемых [модулями](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований."), вам необходим ActiveGate с установленными или активированными этими модулями. При установке ActiveGate вы выбираете основное [назначение](/docs/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применениях ActiveGate.") установки, а затем, в зависимости от назначения, можете установить или активировать различный набор функциональных [модулей](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований.").

ActiveGate может быть развёрнут обычным способом — на физическом или виртуальном хосте — это **развёртывание ActiveGate на хосте**.
ActiveGate, упакованный в контейнер, называется **контейнеризированным развёртыванием ActiveGate**.

### Назначения и функциональность ActiveGate

[Маршрутизация трафика OneAgent](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#route "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Мониторинг облачных сред и удалённых технологий](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#monitor "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Запуск синтетических мониторов](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из приватных синтетических локаций")

[Маршрутизация трафика z/OS](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS.")

[Dynatrace API](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Функциональность по типу ActiveGate](/docs/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и применениях ActiveGate.")

### Системные и аппаратные требования

[ActiveGate для маршрутизации/мониторинга, на Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Узнайте, какие аппаратные требования и требования к операционной системе необходимо учитывать перед установкой ActiveGate на Linux для маршрутизации и мониторинга.")

[ActiveGate для маршрутизации/мониторинга, на Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Узнайте, какие аппаратные требования и требования к операционной системе необходимо учитывать перед установкой ActiveGate на Windows для маршрутизации и мониторинга.")

[ActiveGate с поддержкой синтетического мониторинга](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из приватных локаций")

[ActiveGate для маршрутизации трафика z/OS в Dynatrace](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.")

### См. также

[Схемы подключения ActiveGate](/docs/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.")

## Установка

Операционные системы

Контейнерные платформы

[Linux](/docs/ingest-from/dynatrace-activegate/installation/linux) [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows)

[Kubernetes](/docs/ingest-from/dynatrace-activegate/activegate-in-container) [OpenShift](/docs/ingest-from/dynatrace-activegate/activegate-in-container)