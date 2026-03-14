---
title: Передача журналов в Dynatrace с помощью Fluentd на Kubernetes
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s
scraped: 2026-03-06T21:16:24.238689
---

# Потоковая передача журналов в Dynatrace с помощью Fluentd на Kubernetes


* Latest Dynatrace
* Explanation
* Чтение займёт 1 минуту
* Опубликовано 02 декабря 2021 г.

[Управление журналами и аналитика Dynatrace](../../logs.md "Log Management and Analytics обеспечивает единый подход к управлению и изучению данных журналов в Dynatrace.") использует DaemonSet OneAgent, включающий модуль журналов. Это рекомендуемый способ потоковой передачи журналов с узлов и подов в Dynatrace.

В качестве альтернативы вы можете использовать [плагин Dynatrace Fluentd](https://dt-url.net/gb23475) — модуль с открытым исходным кодом — для потоковой передачи журналов.

Архитектура показана ниже.

![fluentd](https://dt-cdn.net/images/image-2022-03-04-09-25-59-449-925-faa9522baf.png)

## Возможности

* Поддерживает потоковую передачу журналов в разные среды Dynatrace из одного кластера Kubernetes. Например, можно отправлять журналы подов приложений в среду, отличную от среды для журналов узлов Kubernetes.
* Поддерживает потоковую передачу журналов для [интеграций только с приложениями](../../../ingest-from/setup-on-k8s/deployment/application-observability.md "Разверните Dynatrace Operator в режиме мониторинга приложений на Kubernetes").
* Можно настроить для прямой потоковой передачи журналов в Dynatrace.

## Ограничения

Журналы, поступающие из Fluentd, не связаны с рабочими нагрузками Kubernetes. Следовательно, вы не сможете искать журналы по рабочей нагрузке Kubernetes на странице **Просмотр журналов** в Dynatrace. Однако журналы по-прежнему можно просматривать на соответствующих страницах **Рабочих нагрузок Kubernetes**.

## Развёртывание интеграции

Инструкции по развёртыванию интеграции Fluentd см. в [документации на GitHub](https://github.com/dynatrace-oss/fluent-plugin-dynatrace/tree/main/example).

## Связанные темы

* [Kubernetes Classic](../../../observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring.md "Мониторинг Kubernetes/OpenShift с помощью Dynatrace.")
