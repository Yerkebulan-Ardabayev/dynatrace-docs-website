---
title: Istio/Envoy proxy metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics
scraped: 2026-03-06T21:21:54.871292
---

# Метрики Istio/Envoy proxy

# Метрики Istio/Envoy proxy

* Classic
* 1-min read
* Updated on May 08, 2023

Dynatrace version 1.255+

Istio — это независимая от платформы сервисная сетка, пользующаяся большой популярностью в сообществе Kubernetes. Dynatrace OneAgent и ActiveGate могут осуществлять мониторинг Istio со следующими возможностями наблюдаемости:

* Распределённая трассировка и метрики уровня сервиса: OneAgent с [code modules](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* Метрики и топология Istio: ActiveGate
* Логи Istio: модуль логов OneAgent [log module](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa "Ingest log data to Dynatrace using OneAgent and have Dynatrace transform it into meaningful log messages.")

В качестве альтернативы, [Unified services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Define services on observability signals ingested via Trace ingest APIs.") обеспечивают безагентную поддержку сервисных сеток Istio.

## Принцип работы

ActiveGate получает метрики Istio и отправляет их в Dynatrace. Поскольку Istio предоставляет метрики через экспортеры Prometheus, вам нужно лишь [задать аннотации](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

На основе меток полученных метрик Dynatrace также определяет топологию Istio без OneAgent. Это поддерживается начиная с ActiveGate версии 1.261+.

Подробнее об активации расширения Istio в вашей среде см. [Istio Service Meshï»¿](https://www.dynatrace.com/hub/detail/istio-and-envoy-service-mesh-prometheus/) в Dynatrace Hub. Рекомендуемая версия — 1.1.0 или выше.

## Предварительные требования

### ActiveGate

* Требования к приёму данных см. в разделе [Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")
* Определение топологии: ActiveGate версии 1.261+
* Извлечение суммы и количества из гистограммных метрик: ActiveGate версии 1.261+

### Dynatrace

* Карточка метрик Istio на страницах сервисов, рабочих нагрузок и пространств имён Kubernetes: Dynatrace версии 1.255+
* Топология (вызывающие и вызываемые связанные сущности) на страницах сервисов, рабочих нагрузок и пространств имён Kubernetes: Dynatrace версии 1.263+

Мониторинг Istio через OneAgent поддерживается для классического полного стека, облачного полного стека и только-приложение [вариантов развёртывания](/docs/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.") начиная с Operator версии 0.11.0+. Более ранние версии поддерживают только классический полный стек.

## Связанные темы

* [Monitor Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")
