---
title: Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2
scraped: 2026-03-06T21:22:31.186176
---

# Service Detection v2

# Service Detection v2

* Classic
* Обзор
* Чтение: 1 мин
* Обновлено 04 февраля 2026 г.

Service Detection v2 (SDv2) работает на основе единого набора правил, основанных на атрибутах. Это включает правила по умолчанию, а также возможность определять собственные пользовательские правила. Правила SDv2 общедоступны для сервисов OpenTelemetry; для сервисов, работающих в Kubernetes и отслеживаемых OneAgent, правила SDv2 доступны в рамках предварительного выпуска (Preview).

Предварительный выпуск для сервисов Kubernetes, инструментированных OneAgent

SDv2 доступен в качестве предварительного выпуска (Preview) для сервисов, работающих в Kubernetes и отслеживаемых OneAgent. Вы можете присоединиться к этому предварительному выпуску через страницу настроек **Service Detection v2 for OneAgent**.

1. Перейдите в ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Найдите и выберите ваш кластер Kubernetes. При необходимости также выберите пространство имён (namespace).
3. В правом верхнем углу страницы обзора кластера или пространства имён выберите **More** (**…**) > **Settings**.
4. Перейдите в **Service detection** > **Service Detection v2 for OneAgent**.
5. Включите **Enable Service detection v2 for Kubernetes workloads**.

В рамках предварительного выпуска вы можете использовать следующие атрибуты для дополнительного ограничения области применения новых правил SDv2.

* `dt.agent.module.type`
* `k8s.cluster.name`
* `k8s.namespace.name`
* `k8s.workload.name`
* `dt.host_group.id`

Эти параметры настраиваются в настройках вашего пространства имён или кластера Kubernetes.

В настоящее время поддерживается только Java, и необходимо сохранить условие сопоставления по умолчанию `dt.agent.module.type == "java"`. Поддержка дополнительных языков запланирована и будет объявлена в примечаниях к выпускам.

SDv2 обеспечивает:

* Обнаружение и именование сервисов на основе атрибутов ресурсов и условий.
* Обнаружение конечных точек (endpoint) на основе атрибутов спанов и ресурсов.
* Разделение сервисов на основе атрибутов ресурсов.
* Обнаружение сбоев на основе кодов HTTP или gRPC либо других атрибутов спанов и ресурсов.

Поведение SDv2 можно настроить через:

* Веб-интерфейс Dynatrace, как описано на страницах данного раздела.
* [Settings API](../../../../dynatrace-api/environment-api/settings.md "Find out what the Dynatrace Settings API offers.").

## Связанные темы

* [Service Detection v1](service-detection-v1.md "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
