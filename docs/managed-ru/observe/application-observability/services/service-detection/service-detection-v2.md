---
title: Обнаружение сервисов v2
source: https://docs.dynatrace.com/managed/observe/application-observability/services/service-detection/service-detection-v2
---

# Обнаружение сервисов v2

# Обнаружение сервисов v2

* Обзор
* 1 мин на чтение
* Обновлено 14 июля 2026 г.

Версия кластера 1.318+

Service Detection v2 (SDv2) работает по единому набору правил, основанных на атрибутах. Сюда входят правила по умолчанию, а также можно дополнительно определять собственные пользовательские правила. Правила SDv2 применяются только к сервисам OpenTelemetry и Adobe Experience Manager.

SDv2 обеспечивает:

* Обнаружение и именование сервисов на основе атрибутов ресурсов и условий.
* Обнаружение конечных точек на основе атрибутов спанов и ресурсов.
* Разделение сервисов на основе атрибутов ресурсов.
* Обнаружение сбоев по кодам HTTP или gRPC, а также по другим атрибутам спанов и ресурсов.

Настроить SDv2 можно через:

* веб-интерфейс Dynatrace, как описано на страницах этого раздела.
* [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

## Связанные темы

* [Service Detection v1](/managed/observe/application-observability/services/service-detection/service-detection-v1 "Find out how Dynatrace Service Detection v1 detects and names different types of services.")