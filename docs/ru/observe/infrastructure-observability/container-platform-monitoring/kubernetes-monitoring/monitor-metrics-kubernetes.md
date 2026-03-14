---
title: Мониторинг метрик Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-metrics-kubernetes
scraped: 2026-03-06T21:22:00.078051
---

# Мониторинг метрик Kubernetes/OpenShift


* Classic
* 2-min read
* Updated on Mar 14, 2023

Dynatrace version 1.232+

## Предварительные условия

* В Dynatrace перейдите на страницу настроек вашего кластера Kubernetes и убедитесь, что включена опция **Monitor Kubernetes namespaces, services, workloads, and pods**.

## Просмотр метрик Kubernetes

* Подробности о метриках контейнеров смотрите в разделах [Built-in metrics - Containers/CPU](../../../../analyze-explore-automate/metrics-classic/built-in-metrics.md#containers-cpu "Ознакомьтесь с полным списком встроенных метрик Dynatrace.") и [Built-in metrics - Containers/Memory](../../../../analyze-explore-automate/metrics-classic/built-in-metrics.md#containers-memory "Ознакомьтесь с полным списком встроенных метрик Dynatrace.").

* Подробности о метриках Kubernetes смотрите в разделе [Built-in metrics - Cloud/Kubernetes](../../../../analyze-explore-automate/metrics-classic/built-in-metrics.md#cloud-kubernetes "Ознакомьтесь с полным списком встроенных метрик Dynatrace.").

![K8 dash](https://dt-cdn.net/images/2021-03-12-08-54-46-1668-d24182ddd2.png)

### Метрики ресурсов рабочих нагрузок

Dynatrace version 1.264+ ActiveGate version 1.263+

Метрики ресурсов рабочих нагрузок основаны на cAdvisor, который доступен только на узлах Kubernetes под управлением POSIX. Эти метрики недоступны в Windows.

Для кластеров с более чем 50 узлами или 5000 pod потребление ресурсов ActiveGate значительно возрастает.

Функция метрик ресурсов рабочих нагрузок и узлов агрегирует метрики ресурсов контейнеров (использование CPU, дросселирование CPU и потребление памяти) до уровня рабочей нагрузки и узла. Метрики ресурсов рабочих нагрузок и узлов основаны на метриках контейнеров, предоставляемых Kubernetes cAdvisor. Для этой функции не требуется OneAgent — достаточно ActiveGate с включённым мониторингом Kubernetes API.

Чтобы включить мониторинг метрик ресурсов рабочих нагрузок и узлов:

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** и выберите имя кластера, чтобы открыть страницу обзора кластера Kubernetes.
2. В правом верхнем углу выберите **More** (**...**) > **Settings**, выберите **Monitoring settings** и включите **Monitor workload and node resource metrics**.

   Для мониторинга **метрик ресурсов узлов** требуется ActiveGate версии 1.271+.
3. Необязательно Выберите **Test connection**, чтобы убедиться, что функция успешно активирована.

Полный список доступных метрик смотрите в разделе [Workload metrics](../../../../analyze-explore-automate/metrics-classic/all-metrics.md#workload "Ознакомьтесь с полным списком метрик Dynatrace.") или [Node](../../../../analyze-explore-automate/metrics-classic/all-metrics.md#node "Ознакомьтесь с полным списком метрик Dynatrace.") для метрик ресурсов узлов.

## Связанные темы

* [Настройка Dynatrace на Kubernetes](../../../../ingest-from/setup-on-k8s.md "Способы развёртывания и настройки Dynatrace на Kubernetes.")
