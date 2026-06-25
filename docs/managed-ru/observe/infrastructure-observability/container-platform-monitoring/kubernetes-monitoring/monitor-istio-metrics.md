---
title: Метрики Istio/Envoy proxy
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics
scraped: 2026-05-12T12:03:06.469368
---

# Istio/Envoy proxy metrics

# Метрики Istio/Envoy proxy

* 1-min read
* Updated on May 08, 2023

Dynatrace version 1.255+

Istio — это независимая от платформы сервисная сеть, широко используемая в сообществе Kubernetes. Dynatrace OneAgent и ActiveGate могут отслеживать Istio со следующими вариантами наблюдаемости:

* Распределённая трассировка и метрики уровня сервиса: OneAgent с [кодовыми модулями](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* Метрики и топология Istio: ActiveGate
* Журналы Istio: [модуль журналов](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") OneAgent

Кроме того, [Unified services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Define services on observability signals ingested via Trace ingest APIs.") обеспечивают поддержку сервисных сетей Istio без агента.

## Принцип работы

ActiveGate принимает метрики Istio и отправляет их в Dynatrace. Поскольку Istio предоставляет метрики как Prometheus-экспортёры, достаточно [указать аннотации](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

На основе меток принятых метрик Dynatrace также обнаруживает топологию Istio без OneAgent. Поддерживается начиная с ActiveGate версии 1.261+.

Подробнее об активации расширения Istio в вашей среде см. в разделе [Istio Service Mesh](https://www.dynatrace.com/hub/detail/istio-and-envoy-service-mesh-prometheus/) в Dynatrace Hub. Рекомендуемая версия — 1.1.0 и выше.

## Предварительные требования

### ActiveGate

* Предварительные требования для приёма данных см. в разделе [Метрики Prometheus](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")
* Обнаружение топологии: ActiveGate version 1.261+
* Извлечение суммы и счётчика из метрик гистограмм: ActiveGate version 1.261+

### Dynatrace

* Карточка метрик Istio на страницах сервисов, нагрузок и пространств имён Kubernetes: Dynatrace version 1.255+
* Топология (вызывающие и вызываемые связанные сущности) на страницах сервисов, нагрузок и пространств имён Kubernetes: Dynatrace version 1.263+

Мониторинг Istio с помощью OneAgent поддерживается для вариантов развёртывания [classic full-stack, cloud-native full-stack и application-only](/managed/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.") начиная с версии Operator 0.11.0+. Более ранние версии поддерживают только classic full-stack.

## Связанные темы

* [Мониторинг метрик Prometheus](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.")