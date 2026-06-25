---
title: Цели уровня обслуживания (SLO)
source: https://docs.dynatrace.com/managed/deliver/service-level-objectives-classic
scraped: 2026-05-12T11:09:54.409008
---

# Service-Level Objectives

# Service-Level Objectives

* Overview
* 1-min read
* Published Sep 14, 2020

Dynatrace обеспечивает нативную поддержку мониторинга [целей уровня обслуживания (SLO)](/managed/deliver/service-level-objectives-classic/slo-basics "Basic terminology related to service-level objectives") в соответствии с [основами Site Reliability Engineering (SRE), опубликованными Google](https://dt-url.net/cv030av).

## Обзор SLO

На странице обзора **SLOs** можно просмотреть текущий статус работоспособности, бюджеты ошибок, целевые и предупредительные значения, а также временной диапазон для всех ваших SLO.

## Определение и настройка

* Вы можете [определять SLO на основе преднастроенных шаблонов, предоставляемых Dynatrace, либо создавать и настраивать собственные определения SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#config "Create, configure, and monitor service-level objectives with Dynatrace."). Для лучшего понимания того, как настраивать готовые SLO, см. раздел [Примеры конфигурации определений целей уровня обслуживания](/managed/deliver/service-level-objectives-classic/slo-definition-configuration-examples "Explore the out-of-the-box service-level objective definitions by way of examples.").
* Вы можете [управлять доступом к SLO в вашем окружении на основе разрешений зон управления](/managed/deliver/service-level-objectives-classic/slo-mz-permissions "Permissions required at the environment and management-zone level to manage service-level objectives.").

## Визуализация

Вы можете:

* [Закреплять плитки SLO на дашборде](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace.") для визуализации их текущего состояния и оставшихся бюджетов ошибок.
* [Запрашивать и строить графики метрик в Data Explorer](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
* Просматривать список текущих SLO на страницах сведений [**Hosts**](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring#slo "Monitor hosts with Dynatrace."), **Services** и [**Kubernetes workload**](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes "Keep track of SLOs for Kubernetes/OpenShift.").

## Оповещения

Вы получаете [поддержку Davis](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#davis-support "Create, configure, and monitor service-level objectives with Dynatrace.") для определения нарушений SLO до выхода ПО в производство и для проведения анализа первопричин.