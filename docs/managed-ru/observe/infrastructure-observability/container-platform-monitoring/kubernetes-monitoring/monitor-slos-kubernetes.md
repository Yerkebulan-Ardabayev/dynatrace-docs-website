---
title: Мониторинг целевых показателей уровня обслуживания в Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes
scraped: 2026-05-12T11:38:29.021248
---

# Monitor service-level objectives in Kubernetes/OpenShift

# Мониторинг целевых показателей уровня обслуживания в Kubernetes/OpenShift

* 2-min read
* Published Jan 19, 2023

Отслеживать текущие [целевые показатели уровня обслуживания (SLO)](/managed/deliver/service-level-objectives-classic "Monitor and alert on service-level objectives with Dynatrace in Service-Level Objectives Classic."), связанные с нагрузкой Kubernetes/OpenShift, можно на страницах сведений о **нагрузках Kubernetes**.

* Выберите **SLOs** на панели уведомлений для отображения панели **Service-level objectives**, содержащей список SLO, непосредственно или косвенно связанных с нагрузкой.

## Непосредственно связанные SLO

* SLO непосредственно связан с нагрузкой, когда [селектор сущностей](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") SLO соответствует следующим критериям:

  + Тип сущности задан как `"CLOUD_APPLICATION"`.
  + Идентификатор сущности задан равным идентификатору нагрузки.
* Чтобы отображались только SLO, непосредственно связанные с нагрузкой, убедитесь, что параметр **Show only directly connected SLOs** включён.

## Косвенно связанные SLO

* SLO не является непосредственно связанным с нагрузкой, когда в [селекторе сущностей](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") SLO не указан идентификатор сущности.

  Пример: при использовании общих значений, таких как `type("CLOUD_APPLICATION"),tag("slo")`, запрос возвращает все SLO для всех нагрузок, включая текущую.
* Чтобы отобразить SLO, не связанные непосредственно с нагрузкой, отключите **Show only directly connected SLOs**.

## Действия

* Выберите **Details** для просмотра диаграммы соответствующих метрик SLO.
* В разделе **Actions** выберите:

  + **View in Data Explorer** для [просмотра метрик SLO в Data Explorer](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#explorer "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Pin to Dashboard** для [закрепления SLO на панели мониторинга](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#dash "Create, configure, and monitor service-level objectives with Dynatrace."). Подробнее см. в разделе [Закрепление плиток на панели мониторинга](/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/pin-tiles-to-your-dashboard "Learn to pin tiles to your dashboards.").
  + **SLO definition** для редактирования SLO в **Service-level objective definitions**.
  + **Clone** для [клонирования SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#clone "Create, configure, and monitor service-level objectives with Dynatrace.").
  + **Create alert** для [создания оповещения для SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#alerts "Create, configure, and monitor service-level objectives with Dynatrace.").

## Нет SLO

Если SLO не найдены, можно:

* Выбрать другой временной диапазон в правом верхнем углу.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)

  Временной диапазон: панель меню
* Нажать **Add SLO** для создания SLO в [мастере SLO](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo#wizard "Create, configure, and monitor service-level objectives with Dynatrace.").

## Пример панели SLO

![slo-card-workloads](https://dt-cdn.net/images/slo-card-754-ec31947bef.png)

slo-card-workloads

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")