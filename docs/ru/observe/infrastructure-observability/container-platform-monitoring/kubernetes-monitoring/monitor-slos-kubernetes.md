---
title: Мониторинг целевых показателей уровня обслуживания в Kubernetes/OpenShift
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-slos-kubernetes
scraped: 2026-03-06T21:22:03.440195
---

# Мониторинг целевых показателей уровня сервиса в Kubernetes/OpenShift


* 2-min read

Вы можете отслеживать текущие целевые показатели уровня сервиса, связанные с рабочей нагрузкой Kubernetes/OpenShift, на страницах сведений о **рабочей нагрузке Kubernetes**.

* Выберите **SLOs** на панели уведомлений, чтобы отобразить панель **Service-level objectives**, которая содержит список SLO, напрямую или косвенно связанных с рабочей нагрузкой.

## Напрямую связанные SLO

* SLO напрямую связан с рабочей нагрузкой, если селектор сущности SLO соответствует следующим критериям:

  + Тип сущности установлен в `"CLOUD_APPLICATION"`.
  + Идентификатор сущности установлен в идентификатор рабочей нагрузки.
* Чтобы видеть только SLO, напрямую связанные с рабочей нагрузкой, убедитесь, что параметр **Show only directly connected SLOs** включён.

## Косвенно связанные SLO

* SLO не связан напрямую с рабочей нагрузкой, если в селекторе сущности SLO не указан идентификатор сущности.

  Пример: если указаны универсальные значения, такие как `type("CLOUD_APPLICATION"),tag("slo")`, запрос возвращает все SLO для всех рабочих нагрузок, включая текущую.
* Чтобы видеть SLO, не связанные напрямую с рабочей нагрузкой, отключите параметр **Show only directly connected SLOs**.

## Параметры

* Выберите **Details**, чтобы просмотреть график соответствующих метрик SLO.
* В разделе **Actions** выберите

  + **View in Data Explorer**, чтобы просмотреть метрики SLO в Data Explorer.
  + **Pin to Dashboard**, чтобы закрепить SLO на вашей панели мониторинга. Подробнее см. в разделе Закрепление плиток на панели мониторинга.
  + **SLO definition**, чтобы отредактировать SLO в разделе **Service-level objective definitions**.
  + **Clone**, чтобы клонировать SLO.
  + **Create alert**, чтобы создать оповещение для SLO.

## Нет SLO

Если SLO не найдены, вы можете

* Выбрать другой временной диапазон в правом верхнем углу.

  ![Timeframe selector: menu bar](https://dt-cdn.net/images/timeframe-selector-menu-bar-264-8193110c8c.png)
* Выбрать **Add SLO**, чтобы создать SLO с помощью мастера SLO.

## Пример панели SLO

![slo-card-workloads](https://dt-cdn.net/images/slo-card-754-ec31947bef.png)

## Связанные темы

* Настройка Dynatrace в Kubernetes
