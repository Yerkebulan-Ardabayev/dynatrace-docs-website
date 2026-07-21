---
title: Обнаружение сервисов
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection
---

# Обнаружение сервисов

# Обнаружение сервисов

* Пояснение
* Чтение за 1 минуту
* Обновлено 25 окт. 2025 г.

Сервис в Dynatrace представляет собой логическую группировку рабочих нагрузок, обычно приложений или микросервисов, работающих в среде. Обнаружение сервисов автоматически определяет эти сервисы и включает в себя обнаружение конечных точек, обнаружение сбоев и разделение.

Dynatrace предлагает два подхода к обнаружению сервисов:

* Service Detection v2 (SDv2)
* Service Detection v1 (SDv1)

## Service Detection v2

[Service Detection v2](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.") работает по единому набору правил на основе атрибутов, встроенных и заданных пользователем, которые применяются к каждому спану трассировки.

## Service Detection v1

[Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.") это классическое обнаружение сервисов для процессов, инструментированных OneAgent. Оно обеспечивает обнаружение на основе типов сервисов, специфичных для технологии.

## Сравнение Service Detection v2 и v1

![Diagram showing the differences between Service Detection v2 and Service Detection v1](https://dt-cdn.net/images/sdv2-sdv1-1383-eb18456698.png)

Диаграмма, показывающая различия между Service Detection v2 и Service Detection v1

Как показано на диаграмме выше, Service Detection v2 обнаруживает сервисы с помощью правил, которые сопоставляют атрибуты ресурсов (например, `k8s.workload.name`) со спанами. Service Detection v1 обнаруживает сервисы на основе содержимого спанов, специфичного для технологии (например, вызываемых классов Java, таких как `BillingController`).

[### Service Detection v2

Узнайте больше о Service Detection v2.](/managed/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")[### Service Detection v1

Узнайте больше о Service Detection v1.](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")