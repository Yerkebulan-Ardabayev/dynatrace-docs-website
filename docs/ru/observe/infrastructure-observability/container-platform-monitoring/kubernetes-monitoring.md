---
title: Kubernetes Классический
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring
scraped: 2026-03-06T21:11:55.255187
---

# Kubernetes Classic


* Classic
* 1 мин. чтения
* Обновлено 28 сентября 2022 г.

Dynatrace обеспечивает полностековый мониторинг Kubernetes, охватывая все уровни от приложений до инфраструктуры.

## Предварительные требования

1. [Настройте и сконфигурируйте интеграцию Dynatrace в Kubernetes](../../../ingest-from/setup-on-k8s/deployment.md "Deploy Dynatrace Operator on Kubernetes")
2. [Подключите кластер к Dynatrace](../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring.md "Monitor the Kubernetes API using Dynatrace")

Дополнительные параметры и подробности см. в разделе [Настройка Dynatrace в Kubernetes](../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes").

## Функции мониторинга по умолчанию

Чтобы узнать, как настроить функции мониторинга по умолчанию для кластеров Kubernetes/OpenShift, см. [Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift](kubernetes-monitoring/default-monitoring-settings.md "Configure default monitoring settings for all new Kubernetes/OpenShift clusters in your environment.")

## Просмотр результатов мониторинга

Чтобы узнать, как анализировать результаты мониторинга в Dynatrace, см.:

* [Мониторинг использования кластера Kubernetes/OpenShift](kubernetes-monitoring/monitor-cluster-utilization-kubernetes.md "Monitor the health and utilization of your Kubernetes/OpenShift cluster resources.")
* [Мониторинг событий Kubernetes/OpenShift](kubernetes-monitoring/monitor-events-kubernetes.md "Extend visibility into Kubernetes/OpenShift events.")
* [Мониторинг рабочих нагрузок Kubernetes/OpenShift](kubernetes-monitoring/monitor-workloads-kubernetes.md "Enable Kubernetes/OpenShift workloads integration for Dynatrace monitoring.")
* [Мониторинг сервисов Kubernetes/OpenShift](kubernetes-monitoring/monitor-services-kubernetes.md "Enable Kubernetes/OpenShift service integration for Dynatrace monitoring.")
* [Мониторинг метрик Kubernetes/OpenShift](kubernetes-monitoring/monitor-metrics-kubernetes.md "Available metrics for monitoring Kubernetes/OpenShift clusters")
* [Мониторинг метрик Prometheus](kubernetes-monitoring/monitor-prometheus-metrics.md "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")
* [Организация развертываний Kubernetes/OpenShift с помощью тегов](kubernetes-monitoring/leverage-tags-defined-in-kubernetes-deployments.md "Organize and filter your monitored applications by importing labels and annotations from your Kubernetes/OpenShift environment.")
* [Мониторинг заявок на постоянные тома в Kubernetes/OpenShift](kubernetes-monitoring/monitor-pvc-metrics.md "Enable Kubernetes/OpenShift monitoring for persistent volume claims metrics.")
* [Оповещения о распространенных проблемах Kubernetes/OpenShift](kubernetes-monitoring/alert-on-kubernetes-issues.md "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.")
* [Мониторинг уязвимостей в Kubernetes/OpenShift](kubernetes-monitoring/monitor-vulnerabilities-kubernetes.md "Keep track of vulnerabilities in Kubernetes/OpenShift.")
* [Мониторинг целей уровня обслуживания в Kubernetes/OpenShift](kubernetes-monitoring/monitor-slos-kubernetes.md "Keep track of SLOs for Kubernetes/OpenShift.")
* [Метрики Istio/Envoy proxy](kubernetes-monitoring/monitor-istio-metrics.md "Istio metric ingestion and topology detection")
* [Глобальные настройки мониторинга по умолчанию для Kubernetes/OpenShift](kubernetes-monitoring/default-monitoring-settings.md "Configure default monitoring settings for all new Kubernetes/OpenShift clusters in your environment.")

## Связанные темы

* [Настройка Dynatrace в Kubernetes](../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes")
