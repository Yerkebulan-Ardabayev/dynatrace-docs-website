---
title: Потоковая передача журналов в Dynatrace с помощью Fluentd в Kubernetes (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/stream-logs-fluentd-k8s
scraped: 2026-05-12T11:53:57.480452
---

# Потоковая передача журналов в Dynatrace с помощью Fluentd в Kubernetes (Logs Classic)

# Потоковая передача журналов в Dynatrace с помощью Fluentd в Kubernetes (Logs Classic)

* Пояснение
* Чтение: 1 мин
* Обновлено 18 января 2023 г.

Log Monitoring Classic

Рекомендуемый способ потоковой передачи журналов из узлов и подов Kubernetes в Dynatrace описан в разделе [Мониторинг журналов в Kubernetes (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Узнайте, как осуществлять мониторинг журналов в Kubernetes.").

В качестве альтернативы можно использовать [плагин Dynatrace для Fluentd](https://dt-url.net/gb23475) — модуль с открытым исходным кодом — для потоковой передачи журналов.

Архитектура представлена на схеме ниже.

![fluentd](https://dt-cdn.net/images/image-2022-03-04-09-25-59-449-925-faa9522baf.png)

fluentd

## Возможности

* Поддерживает потоковую передачу журналов в различные окружения Dynatrace из одного кластера Kubernetes. Например, можно отправлять журналы прикладных подов в другое окружение, нежели журналы узлов Kubernetes.
* Поддерживает потоковую передачу журналов для [интеграций только для приложений](/managed/ingest-from/setup-on-k8s/deployment/app-obs-managed "Развёртывание Dynatrace Operator в режиме мониторинга приложений в Kubernetes").
* Может быть настроен для прямой передачи журналов в Dynatrace.

## Ограничения

Журналы, поступающие от Fluentd, не связываются с рабочими нагрузками Kubernetes. Следовательно, поиск журналов по рабочей нагрузке Kubernetes на странице **Log viewer** в Dynatrace недоступен. Однако журналы по-прежнему отображаются на соответствующих страницах **Kubernetes workloads**.

## Развёртывание интеграции

Инструкции по развёртыванию интеграции Fluentd: [документация на GitHub](https://github.com/dynatrace-oss/fluent-plugin-dynatrace/tree/main/example).

## Связанные темы

* [Kubernetes](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")