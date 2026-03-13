---
title: Monitor service-level objectives in Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes
scraped: 2026-03-06T21:22:03.440195
---

# Мониторинг целевых показателей уровня сервиса в Kubernetes/OpenShift

# Мониторинг целевых показателей уровня сервиса в Kubernetes/OpenShift

* Classic
* 2-min read
* Published Jan 19, 2023

Вы можете отслеживать текущие [целевые показатели уровня сервиса](../../../../deliver/service-level-objectives-classic.md "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic."), связанные с рабочей нагрузкой Kubernetes/OpenShift, на страницах сведений о **рабочей нагрузке Kubernetes**.

* Выберите **SLOs** на панели уведомлений, чтобы отобразить панель **Service-level objectives**, которая содержит список SLO, напрямую или косвенно связанных с рабочей нагрузкой.

## Напрямую связанные SLO

* SLO напрямую связан с рабочей нагрузкой, если [селектор сущности](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md "Configure the entity selector for Environment API endpoints.") SLO соответствует следующим критериям:

  + Тип сущности установлен в `"CLOUD_APPLICATION"`.
  + Идентификатор сущности установлен в идентификатор рабочей нагрузки.
* Чтобы видеть только SLO, напрямую связанные с рабочей нагрузкой, убедитесь, что параметр **Show only directly connected SLOs** включён.

## Косвенно связанные SLO

* SLO не связан напрямую с рабочей нагрузкой, если в [селекторе сущности](../../../../dynatrace-api/environment-api/entity-v2/entity-selector.md "Configure the entity selector for Environment API endpoints.") SLO не указан идентификатор сущности.

  Пример: если указаны универсальные значения, такие как `type("CLOUD_APPLICATION"),tag("slo")`, запрос возвращает все SLO для всех рабочих нагрузок, включая текущую.
* Чтобы видеть SLO, не связанные напрямую с рабочей нагрузкой, отключите параметр **Show only directly connected SLOs**.

## Параметры

* Выберите **Details**, чтобы просмотреть график соответствующих метрик SLO.
* В разделе **Actions** выберите

  + **View in Data Explorer**, чтобы [просмотреть метрики SLO в Data Explorer](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard**, чтобы [закрепить SLO на вашей панели мониторинга](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#dash "Create, configure, and monitor service-level objectives with Dynatrace."). Подробнее см. в разделе [Закрепление плиток на панели мониторинга](../../../../analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard.md "Learn to pin tiles to your dashboards.").
  + **SLO definition**, чтобы отредактировать SLO в разделе **Service-level objective definitions**.
  + **Clone**, чтобы [клонировать SLO](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert**, чтобы [создать оповещение для SLO](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

## Нет SLO

Если SLO не найдены, вы можете

* Выбрать другой временной диапазон в правом верхнем углу.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Выбрать **Add SLO**, чтобы создать SLO с помощью [мастера SLO](../../../../deliver/service-level-objectives-classic/configure-and-monitor-slo.md#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

## Пример панели SLO

![slo-card-workloads](https://dt-cdn.net/images/slo-card-754-ec31947bef.png)

## Связанные темы

* [Настройка Dynatrace в Kubernetes](../../../../ingest-from/setup-on-k8s.md "Ways to deploy and configure Dynatrace on Kubernetes")
