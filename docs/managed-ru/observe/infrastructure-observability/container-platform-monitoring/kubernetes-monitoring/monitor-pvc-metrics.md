---
title: Мониторинг заявок на постоянные тома в Kubernetes/OpenShift
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-pvc-metrics
scraped: 2026-05-12T12:07:35.418094
---

# Monitor persistent volume claims on Kubernetes/OpenShift

# Мониторинг заявок на постоянные тома в Kubernetes/OpenShift

* 2-min read
* Updated on Jul 09, 2024

На этой странице описаны минимальные требования к версиям для базовых возможностей мониторинга заявок на постоянные тома.

Dynatrace version 1.294 +

ActiveGate version 1.289+

В Kubernetes постоянные данные хранятся в [заявках на постоянные тома (PVC)](https://dt-url.net/n403y11). Dynatrace предоставляет необходимые сведения об ёмкости заявок на постоянные тома.

* Dynatrace предоставляет предустановленные панели мониторинга **Kubernetes persistent volume claims**, позволяющие анализировать заявки на постоянные тома по общей ёмкости, использованию, оставшемуся свободному пространству и темпам роста.
* Шаблоны для пользовательских оповещений позволяют получать оповещения о связанных проблемах, таких как нехватка свободного пространства в PVC или необычный рост.

Чтобы начать мониторинг заявок на постоянные тома, см. ниже.

## Включение

Мониторинг PVC является встроенной функцией и не требует ручного включения.

## Разрешения

Убедитесь, что правило `get` и ресурсы `nodes/metrics` включены в ClusterRole Kubernetes. При мониторинге PVC с ActiveGate, работающим за пределами кластера, также потребуется разрешение `nodes/proxy`.

Пример:

![Example PVC permissions](https://dt-cdn.net/images/screenshot-1-1215-23c529f37c.png)

Пример разрешений PVC

## Построение панелей мониторинга

Dynatrace предоставляет предварительно настроенную панель мониторинга, охватывающую следующие сценарии использования:

* Отображение пространств имён с наибольшим / наименьшим свободным пространством
* Отображение пространств имён с наибольшим темпом роста
* Отображение топ-10 наибольших PVC
* Отображение ёмкости / использования по пространствам имён

![Example PVC dashboard](https://dt-cdn.net/images/kubernetes-persistent-volume-claims-dashboard-1357-3d62f7e8b3.png)

Пример панели мониторинга PVC

## Ограничения

Эта функция доступна только при [подключении кластера Kubernetes к локальной конечной точке Kubernetes API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring "Monitor the Kubernetes API using Dynatrace").

## Связанные темы

* [Настройка Dynatrace на Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")