---
title: Мониторинг использования кластера Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-cluster-utilization-kubernetes
scraped: 2026-02-06T16:26:39.711082
---

# Monitor Kubernetes/OpenShift cluster utilization

# Monitor Kubernetes/OpenShift cluster utilization

* 2-min read
* Updated on Apr 29, 2024

Dynatrace version 1.232+

## Предварительные требования

* В Dynatrace перейдите на страницу настроек кластера Kubernetes и убедитесь, что параметр **Monitor Kubernetes namespaces, services, workloads, and pods** включён.

## Страница Kubernetes

После включения доступа к странице обзора Kubernetes для конкретного кластера Kubernetes этот кластер появится на странице **Kubernetes**. Страница Kubernetes предоставляет обзор всех кластеров Kubernetes, отображая данные мониторинга, такие как размеры и утилизация кластеров.
Для доступа к этой странице перейдите в **Kubernetes** (предыдущий Dynatrace) или ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.

![Cluster utilization](https://dt-cdn.net/images/cluster-list-3710-4c21475cfb.png)

## Утилизация ресурсов кластера во времени

Поскольку Kubernetes может выполнять любые контейнеризированные рабочие нагрузки и поддерживает горизонтальное автомасштабирование подов, фактическая утилизация ресурсов кластера, вероятно, будет очень волатильной. Именно поэтому Dynatrace предлагает единую панель управления для наиболее важных метрик утилизации и производительности на уровне кластера. К этим метрикам относятся:

* Процент использованных ресурсов CPU от общего объёма выделяемых ресурсов CPU.
* Процент запрошенных/ограниченных ресурсов CPU от общего объёма выделяемых ресурсов CPU.
* Процент запрошенных/использованных ресурсов памяти от общего объёма выделяемых ресурсов памяти.
* Процент ограниченных ресурсов памяти от общего объёма выделяемых ресурсов памяти.
* Общее использование CPU/памяти.
* Запрошенные/ограниченные ресурсы CPU/памяти.
* Ресурсы CPU/памяти, выделяемые подам.
* Общее количество запущенных/выделяемых подов на узлах кластера.
* Количество перезапусков контейнеров.

![Monitor k8](https://dt-cdn.net/images/cluster-1-3700-55f0edc5fe.png)

## Просмотр доступных ресурсов на узлах Kubernetes

Вы можете получить детальную информацию о метриках узлов Kubernetes на уровне каждого узла, чтобы понять, как используются отдельные узлы. Страница **Node analysis** также предоставляет информацию о том, сколько рабочей нагрузки ещё можно развернуть на узлах.

![View resource k8](https://dt-cdn.net/images/cluster-2-3700-209833d1e0.png)

Выбрав конкретный узел, вы можете получить доступ к сведениям о хосте в верхней части страницы обзора узла. Оттуда вы можете углубиться в аналитику на уровне кода для развёрнутых в данный момент контейнеров, а также в соответствующие облачные свойства хоста и метки узлов Kubernetes.

![View host k8](https://dt-cdn.net/images/cluster-3-3700-0d7e54a3e8.png)

## Связанные темы

* [Настройка Dynatrace на Kubernetes](../../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes")
