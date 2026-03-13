---
title: Service-Level Objectives Classic
source: https://www.dynatrace.com/docs/deliver/service-level-objectives-classic
scraped: 2026-03-04T21:33:40.088795
---

# Service-Level Objectives Classic

# Service-Level Objectives Classic

* Classic
* Overview
* 1-min read
* Published Sep 14, 2020

Dynatrace поставляется с встроенной поддержкой мониторинга [целевых показателей уровня обслуживания (SLO)](/docs/deliver/service-level-objectives-classic/slo-basics "Basic terminology related to service-level objectives") в соответствии с [основами Site Reliability Engineering (SRE), опубликованными Google](https://dt-url.net/cv030av).

## Обзор SLO

На странице обзора **SLOs** вы можете просматривать текущее состояние работоспособности, бюджеты ошибок, целевые и предупредительные значения, а также временной период для всех ваших SLO.

## Определение и настройка

* Вы можете [определять SLO на основе предварительно настроенных шаблонов Dynatrace или создавать и настраивать собственные определения SLO](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#config "Create, configure, and monitor service-level objectives with Dynatrace."). Для лучшего понимания настройки готовых SLO см. [Примеры настройки определений целевых показателей уровня обслуживания](/docs/deliver/service-level-objectives-classic/slo-definition-configuration-examples "Explore the out-of-the-box service-level objective definitions by way of examples.").
* Вы можете [управлять доступом к SLO в вашей среде на основе разрешений зон управления](/docs/deliver/service-level-objectives-classic/slo-mz-permissions "Permissions required at the environment and management-zone level to manage service-level objectives.").

## Визуализация

Вы можете:

* [Закрепить плитки SLO на вашей панели мониторинга](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.") для отображения их текущего состояния и оставшихся бюджетов ошибок.
* [Запрашивать и строить графики метрик в Data Explorer](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
* Просматривать список текущих SLO на страницах с подробностями [**Hosts**](/docs/observe/infrastructure-observability/hosts/monitoring/host-monitoring#slo "Monitor hosts with Dynatrace."), **Services** и [**Kubernetes workload**](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes "Keep track of SLOs for Kubernetes/OpenShift.").

## Оповещения

Вы получаете [поддержку Davis](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#davis-support "Create, configure, and monitor service-level objectives with Dynatrace.") для определения нарушений SLO до того, как программное обеспечение попадёт в производственную среду, а также для проведения анализа первопричин.
