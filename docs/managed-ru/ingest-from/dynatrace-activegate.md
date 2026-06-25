---
title: Dynatrace ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate
scraped: 2026-05-12T11:03:19.492044
---

# Dynatrace ActiveGate

# Dynatrace ActiveGate

* 3-min read
* Published Jul 23, 2018

### ActiveGate выступает в роли безопасного прокси

Dynatrace ActiveGate выступает в роли безопасного прокси между Dynatrace OneAgent и кластерами Dynatrace или между Dynatrace OneAgent и другими ActiveGate, расположенными ближе к кластеру Dynatrace. Он обеспечивает присутствие Dynatrace в вашей локальной сети. Таким образом, все взаимодействия с Dynatrace сводятся к одной точке, доступной локально. Помимо удобства, такое решение оптимизирует объём трафика, снижает сложность сети и затраты, а также обеспечивает безопасность изолированных сетей.

### ActiveGate выполняет мониторинг

В дополнение к маршрутизации данных мониторинга, собранных OneAgent, Dynatrace ActiveGate также способен выполнять задачи мониторинга с использованием API для запросов и мониторинга широкого спектра технологий. Список отслеживаемых технологий не ограничен и может динамически расширяться. В него входят облачные и датацентровые технологии, например AWS, VMware, Azure, Kubernetes, OpenShift, Cloud Foundry, Google Cloud, Oracle, SNMP, WMI, Prometheus и многие другие.

### 

Схема функций ActiveGate

![Функции ActiveGate](https://dt-cdn.net/images/ag-general-005-1-1048-b2d55cede0.png)

Функции ActiveGate

### Типы, назначение и функциональные модули ActiveGate

В зависимости от используемого [решения развёртывания](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также между ActiveGate и OneAgent.") Dynatrace и [назначения](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и вариантах использования ActiveGate.") вам потребуются различные типы ActiveGate: **Environment ActiveGate** или **Cluster ActiveGate**.

Для [развёртываний Dynatrace Managed](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#managed-scheme "Узнайте о приоритетах подключения между типами ActiveGate, а также между ActiveGate и OneAgent.") обычно требуются оба типа ActiveGate, хотя наиболее важным для Dynatrace Managed является [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Установка Cluster ActiveGate на Linux или Windows для маршрутизации трафика OneAgent или запуска Synthetic-мониторов с подключением к Managed Cluster.").

Для использования определённых функциональных возможностей ActiveGate, называемых [модулями](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями."), необходим ActiveGate с установленными или активированными этими модулями. При установке ActiveGate вы выбираете основное [назначение](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и вариантах использования ActiveGate.") установки, а затем, в зависимости от назначения, можете установить или активировать различные функциональные [модули](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Узнайте, какие свойства ActiveGate можно настроить в соответствии с вашими потребностями и требованиями.").

ActiveGate может быть развёрнут обычным способом на физическом или виртуальном хосте — это **развёртывание ActiveGate на хосте**. ActiveGate, упакованный в контейнер, называется **контейнеризованным развёртыванием ActiveGate**.

### Назначение и функциональность ActiveGate

[Маршрутизация трафика OneAgent](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#route "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Мониторинг облачных сред и удалённых технологий](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#monitor "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Запуск Synthetic-мониторов](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGate для Synthetic-мониторинга внутренних и внешних ресурсов из частных Synthetic-локаций")

[Маршрутизация трафика z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Узнайте об установке модуля zRemote для мониторинга z/OS.")

[API Dynatrace](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Узнайте о возможностях маршрутизации и мониторинга ActiveGate.")

[Функциональность по типу ActiveGate](/managed/ingest-from/dynatrace-activegate/capabilities "Узнайте о возможностях и вариантах использования ActiveGate.")

### Системные и аппаратные требования

[ActiveGate для маршрутизации/мониторинга, на Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Узнайте о требованиях к аппаратному обеспечению и операционной системе перед установкой ActiveGate на Linux для маршрутизации и мониторинга.")

[ActiveGate для маршрутизации/мониторинга, на Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Узнайте о требованиях к аппаратному обеспечению и операционной системе перед установкой ActiveGate на Windows для маршрутизации и мониторинга.")

[ActiveGate с поддержкой Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к аппаратному обеспечению для запуска Synthetic-мониторов из частных локаций")

[ActiveGate для маршрутизации трафика z/OS в Dynatrace](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Подготовка и установка zRemote для мониторинга z/OS.")

### Смотрите также

[Схемы подключения ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Узнайте о приоритетах подключения между типами ActiveGate, а также между ActiveGate и OneAgent.")

## Установка

Операционные системы

Контейнерные платформы

[Linux](/managed/ingest-from/dynatrace-activegate/installation/linux) [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows)

[Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container) [OpenShift](/managed/ingest-from/dynatrace-activegate/activegate-in-container)