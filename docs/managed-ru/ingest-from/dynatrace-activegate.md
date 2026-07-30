---
title: Dynatrace ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate
---

# Dynatrace ActiveGate

# Dynatrace ActiveGate

* Чтение займёт 3 минуты
* Обновлено 09 июля 2026 г.

### ActiveGate выступает в роли защищённого прокси

Dynatrace ActiveGate выступает в роли защищённого прокси между Dynatrace OneAgents и кластерами Dynatrace либо между Dynatrace OneAgents и другими ActiveGates, расположенными ближе к кластеру Dynatrace.
Он создаёт присутствие Dynatrace в локальной сети. Это позволяет свести взаимодействие с Dynatrace к единой точке, доступной локально. Помимо удобства, такое решение оптимизирует объём трафика, снижает сложность сети и сопутствующие расходы. Кроме того, оно обеспечивает безопасность изолированных сетей.

### ActiveGate выполняет мониторинг

Помимо маршрутизации данных мониторинга, собранных OneAgents, Dynatrace ActiveGate также способен выполнять задачи мониторинга: для этого используется API, позволяющий запрашивать и контролировать широкий спектр технологий. Список отслеживаемых технологий не ограничен и может расширяться динамически. В него входят облачные и дата-центровые технологии, например AWS, VMware, Azure, Kubernetes, OpenShift, Cloud Foundry, Google Cloud, Oracle, SNMP, WMI, Prometheus и многие другие.

### 

Диаграмма функций ActiveGate

![Functions of an ActiveGate](https://cdn.bfldr.com/B686QPH3/as/t4j8ggtv98xv8v8pccpvwf27/ActiveGate-ActiveGate_performance_monitoring-Light_Mode?auto=webp&format=png&position=1)

Функции ActiveGate

### Типы, назначение и функциональные модули ActiveGate

В зависимости от используемого [варианта развёртывания](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") Dynatrace и [целей](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate."), для которых применяется Dynatrace, потребуются разные типы ActiveGates: **Environment ActiveGates** или **Cluster ActiveGates**.

Для [развёртываний Dynatrace Managed](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates#managed-scheme "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.") как правило нужны оба типа ActiveGate, однако наиболее важным для Dynatrace Managed является [Cluster ActiveGate](/managed/managed-cluster/installation/install-cluster-activegate "Install a Cluster ActiveGate on Linux or Windows to route OneAgent traffic or run Synthetic monitors, and connect it to your Managed Cluster.").

Чтобы использовать конкретные функциональные возможности ActiveGate, называемые [модулями](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."), нужен ActiveGate с установленными или активированными соответствующими модулями. При установке ActiveGate выбирается основное [назначение](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.") инсталляции, после чего, в зависимости от назначения, можно установить или активировать различные наборы функциональных [модулей](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements.").

ActiveGate можно развернуть традиционным способом, на физическом или виртуальном хосте: это **развёртывание ActiveGate на базе хоста**.
ActiveGate, упакованный в контейнер, называется **контейнеризованным развёртыванием ActiveGate**.

### Назначение и функциональность ActiveGate

[Маршрутизация трафика OneAgent](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#route "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Мониторинг облачных сред и удалённых технологий](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#monitor "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Запуск синтетических мониторов](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

[Маршрутизация трафика z/OS](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")

[Dynatrace API](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

[Функциональность по типу ActiveGate](/managed/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate.")

### Системные и аппаратные требования

[ActiveGate для маршрутизации/мониторинга, Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

[ActiveGate для маршрутизации/мониторинга, Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

[ActiveGate с поддержкой Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations")

[ActiveGate для маршрутизации трафика z/OS в Dynatrace](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.")

### См. также

[Схемы подключения ActiveGate](/managed/ingest-from/dynatrace-activegate/supported-connectivity-schemes-for-activegates "Learn about the connectivity priorities between ActiveGate types as well as the priorities between ActiveGates and OneAgents.")

## Установка

Операционные системы

Контейнерные платформы

[Linux](/managed/ingest-from/dynatrace-activegate/installation/linux) [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows)

[Kubernetes](/managed/ingest-from/dynatrace-activegate/activegate-in-container) [OpenShift](/managed/ingest-from/dynatrace-activegate/activegate-in-container)