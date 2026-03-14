---
title: Передача журналов в Dynatrace с помощью Fluentd на Kubernetes (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-fluentd-k8s
scraped: 2026-03-06T21:26:03.242201
---

# Потоковая передача логов в Dynatrace с помощью Fluentd в Kubernetes (Logs Classic)

# Потоковая передача логов в Dynatrace с помощью Fluentd в Kubernetes (Logs Classic)

* Classic
* Explanation
* 1-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Для новейшей версии Dynatrace см. [Потоковая передача логов в Dynatrace с помощью Fluentd в Kubernetes](../../logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s.md "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.").

Рекомендуемый способ потоковой передачи логов из узлов и подов Kubernetes в Dynatrace описан в разделе [Log Monitoring в Kubernetes (Logs Classic)](log-monitoring-kubernetes.md "Learn how to monitor logs in Kubernetes.").

В качестве альтернативы вы можете использовать [плагин Dynatrace Fluentdï»¿](https://dt-url.net/gb23475) — модуль с открытым исходным кодом — для потоковой передачи логов.

Архитектура показана ниже.

![fluentd](https://dt-cdn.net/images/image-2022-03-04-09-25-59-449-925-faa9522baf.png)

## Возможности

* Поддерживает потоковую передачу логов в разные среды Dynatrace из одного кластера Kubernetes. Например, логи подов приложений можно отправлять в другую среду, отличную от среды логов узлов Kubernetes.
* Поддерживает потоковую передачу логов для [интеграций только с приложениями](../../../ingest-from/setup-on-k8s/deployment/application-observability.md "Deploy Dynatrace Operator in application monitoring mode to Kubernetes").
* Может быть настроен для прямой потоковой передачи логов в Dynatrace.

## Ограничения

Логи, поступающие из Fluentd, не связаны с рабочими нагрузками Kubernetes. Следовательно, на странице **Log viewer** в Dynatrace нельзя выполнять поиск логов по рабочей нагрузке Kubernetes. Однако логи по-прежнему можно просматривать на соответствующих страницах **Kubernetes workloads**.

## Развёртывание интеграции

Инструкции по развёртыванию интеграции Fluentd см. в [документации на GitHubï»¿](https://github.com/dynatrace-oss/fluent-plugin-dynatrace/tree/main/example).

## Связанные темы

* [Kubernetes Classic](../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring.md "Monitor Kubernetes/OpenShift with Dynatrace.")
