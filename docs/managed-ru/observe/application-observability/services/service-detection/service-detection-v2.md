---
title: Service Detection v2
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v2
scraped: 2026-05-12T11:35:34.236259
---

# Service Detection v2

# Service Detection v2

* Overview
* 1-min read
* Updated on Feb 04, 2026

Cluster версии 1.318+

Service Detection v2 (SDv2) работает на основе единого набора правил, основанных на атрибутах. Сюда входят правила по умолчанию, а также возможность определения собственных пользовательских правил. Правила SDv2 применяются только к сервисам OpenTelemetry и Adobe Experience Manager.

SDv2 обеспечивает:

* Обнаружение и именование сервисов на основе атрибутов ресурсов и условий.
* Обнаружение конечных точек на основе атрибутов spans и ресурсов.
* Разделение сервисов на основе атрибутов ресурсов.
* Обнаружение сбоев на основе HTTP- или gRPC-кодов либо других атрибутов spans и ресурсов.

SDv2 можно настроить через:

* Веб-интерфейс Dynatrace, как описано на страницах данного раздела.
* [Settings API](/managed/dynatrace-api/environment-api/settings "Узнайте, что предлагает Dynatrace Settings API.").

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")