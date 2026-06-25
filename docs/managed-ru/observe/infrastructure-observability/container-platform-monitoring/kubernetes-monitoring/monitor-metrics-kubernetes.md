---
title: Мониторинг метрик Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-metrics-kubernetes
scraped: 2026-05-12T12:07:31.611820
---

# Monitor Kubernetes/OpenShift metrics

# Мониторинг метрик Kubernetes/OpenShift

* 2-min read
* Updated on Mar 14, 2023

Dynatrace version 1.232+

## Предварительные требования

* В Dynatrace перейдите на страницу настроек кластера Kubernetes и убедитесь, что параметр **Monitor Kubernetes namespaces, services, workloads, and pods** включён.

## Просмотр метрик Kubernetes

* Подробнее о метриках контейнеров см. в разделах [Built-in metrics - Containers/CPU](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#containers-cpu "Explore the complete list of built-in Dynatrace metrics.") и [Built-in metrics - Containers/Memory](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#containers-memory "Explore the complete list of built-in Dynatrace metrics.").

* Подробнее о метриках Kubernetes см. в разделе [Built-in metrics - Cloud/Kubernetes](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#cloud-kubernetes "Explore the complete list of built-in Dynatrace metrics.").

![K8 dash](https://dt-cdn.net/images/2021-03-12-08-54-46-1668-d24182ddd2.png)

K8 dash

### Метрики ресурсов нагрузок

Dynatrace version 1.264+ ActiveGate version 1.263+

Метрики ресурсов нагрузок используют cAdvisor, доступный только на узлах Kubernetes под управлением POSIX. Эти метрики недоступны в Windows.

Для кластеров с более чем 50 узлами или 5000 подов потребление ресурсов ActiveGate существенно возрастает.

Функция метрик ресурсов нагрузок и узлов агрегирует метрики ресурсов контейнеров (использование CPU, тротлинг CPU и потребление памяти) до уровня нагрузок и узлов. Метрики ресурсов нагрузок и узлов основаны на метриках контейнеров, предоставляемых Kubernetes cAdvisor. Для работы этой функции не требуется OneAgent — достаточно ActiveGate с включённым мониторингом Kubernetes API.

Чтобы включить мониторинг метрик ресурсов нагрузок и узлов:

1. Перейдите в раздел **Kubernetes** и выберите имя кластера, чтобы открыть страницу обзора кластера Kubernetes.
2. В правом верхнем углу выберите **More** (**…**) > **Settings**, затем **Monitoring settings** и включите **Monitor workload and node resource metrics**.

   Для мониторинга **node resource metrics** требуется ActiveGate version 1.271+.
3. Необязательно: выберите **Test connection**, чтобы убедиться, что функция успешно активирована.

Список всех доступных метрик см. в разделе [Workload metrics](/managed/analyze-explore-automate/metrics-classic/all-metrics#workload "Explore the complete list of Dynatrace metrics.") или [Node](/managed/analyze-explore-automate/metrics-classic/all-metrics#node "Explore the complete list of Dynatrace metrics.") для метрик ресурсов узлов.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")