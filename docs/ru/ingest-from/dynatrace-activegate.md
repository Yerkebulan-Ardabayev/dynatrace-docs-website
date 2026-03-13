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

Вам потребуются различные типы ActiveGate — **Environment ActiveGate** или **Cluster ActiveGate** — в зависимости от [решения развёртывания](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.") Dynatrace, которое вы используете, а также от [назначения](dynatrace-activegate/capabilities.md "Узнайте о возможностях и применениях ActiveGate."), для которого вы используете Dynatrace.

Если вы используете [SaaS-решение](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md#saas-scheme "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.") Dynatrace, вам нужно установить только Environment ActiveGate.

Для использования определённых функциональных возможностей ActiveGate, называемых [модулями](dynatrace-activegate/configuration/configure-activegate.md#modules "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований."), вам необходим ActiveGate с установленными или активированными этими модулями. При установке ActiveGate вы выбираете основное [назначение](dynatrace-activegate/capabilities.md "Узнайте о возможностях и применениях ActiveGate.") установки, а затем, в зависимости от назначения, можете установить или активировать различный набор функциональных [модулей](dynatrace-activegate/configuration/configure-activegate.md#modules "Узнайте, какие свойства ActiveGate можно настроить в зависимости от ваших потребностей и требований.").

ActiveGate может быть развёрнут обычным способом — на физическом или виртуальном хосте — это **развёртывание ActiveGate на хосте**.
ActiveGate, упакованный в контейнер, называется **контейнеризированным развёртыванием ActiveGate**.

### Назначения и функциональность ActiveGate

[Маршрутизация трафика OneAgent](dynatrace-activegate/capabilities/routing-monitoring-purpose.md#route "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Мониторинг облачных сред и удалённых технологий](dynatrace-activegate/capabilities/routing-monitoring-purpose.md#monitor "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Запуск синтетических мониторов](dynatrace-activegate/capabilities/synthetic-purpose.md "ActiveGate для синтетического мониторинга внутренних и внешних ресурсов из приватных синтетических локаций")

[Маршрутизация трафика z/OS](dynatrace-activegate/capabilities/zremote-purpose.md "Узнайте об установке модуля zRemote для мониторинга z/OS.")

[Dynatrace API](dynatrace-activegate/capabilities/routing-monitoring-purpose.md#api "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Функциональность по типу ActiveGate](dynatrace-activegate/capabilities.md "Узнайте о возможностях и применениях ActiveGate.")

### Системные и аппаратные требования

[ActiveGate для маршрутизации/мониторинга, на Linux](dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements.md "Узнайте, какие аппаратные требования и требования к операционной системе необходимо учитывать перед установкой ActiveGate на Linux для маршрутизации и мониторинга.")

[ActiveGate для маршрутизации/мониторинга, на Windows](dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements.md "Узнайте, какие аппаратные требования и требования к операционной системе необходимо учитывать перед установкой ActiveGate на Windows для маршрутизации и мониторинга.")

[ActiveGate с поддержкой синтетического мониторинга](../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md "Поддерживаемые операционные системы, версии Chromium и аппаратные требования для запуска синтетических мониторов из приватных локаций")

[ActiveGate для маршрутизации трафика z/OS в Dynatrace](dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote.md "Подготовка и установка zRemote для мониторинга z/OS.")

### См. также

[Схемы подключения ActiveGate](dynatrace-activegate/supported-connectivity-schemes-for-activegates.md "Узнайте о приоритетах подключения между типами ActiveGate, а также о приоритетах между ActiveGate и OneAgent.")

## Установка

Операционные системы

Контейнерные платформы

[Linux](dynatrace-activegate/installation/linux.md) [Windows](dynatrace-activegate/installation/windows.md)

[Kubernetes](dynatrace-activegate/activegate-in-container.md) [OpenShift](dynatrace-activegate/activegate-in-container.md)