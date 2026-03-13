---
title: ClusterRole aggregation for Kubernetes monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation
scraped: 2026-03-05T21:35:12.026761
---

# ClusterRole aggregation for Kubernetes monitoring

# ClusterRole aggregation for Kubernetes monitoring

* Latest Dynatrace
* 2-min read
* Updated on Dec 09, 2025

Dynatrace Operator версии 1.8.0+

Начиная с версии Operator 1.8.0, компонент ActiveGate использует сервисный аккаунт, привязанный к ClusterRole `dynatrace-kubernetes-monitoring`. Эта ClusterRole является **агрегированной ролью**, обеспечивающей простую и гибкую настройку назначенных разрешений RBAC. [1](#fn-1-1-def)

1

Агрегация ClusterRole — это функция Kubernetes RBAC, позволяющая объединять несколько ClusterRole в одну агрегированную ClusterRole. Агрегирующая ClusterRole использует селекторы меток для определения того, какие другие ClusterRole должны быть включены. Подробнее см. в разделе [ClusterRole aggregation в документации Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).

## Разрешения по умолчанию

По умолчанию установка Dynatrace Operator создаёт ClusterRole `dynatrace-kubernetes-monitoring-default`, содержащую стандартный набор разрешений, необходимых для мониторинга платформы Kubernetes. Эта ClusterRole автоматически помечается меткой `rbac.dynatrace.com/aggregate-to-monitoring: "true"`, поэтому её разрешения включаются в агрегированную роль.

Разрешения по умолчанию задокументированы в [справочнике по безопасности](../../reference/security.md#activegate "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") и охватывают стандартный мониторинг:

* подов, развёртываний, StatefulSet и других ресурсов рабочих нагрузок;
* сервисов и конечных точек;
* узлов и метрик ресурсов;
* событий и информации о кластере.

## Расширение ClusterRole дополнительными разрешениями

Чтобы расширить функциональность мониторинга за пределы разрешений по умолчанию, создайте дополнительные ClusterRole с меткой агрегации. Любая ClusterRole с меткой `rbac.dynatrace.com/aggregate-to-monitoring: "true"` автоматически агрегируется, и её разрешения предоставляются сервисному аккаунту ActiveGate.

### Пример: разрешить мониторинг конфиденциальных данных

Чтобы включить мониторинг конфиденциальных объектов Kubernetes, таких как Secrets и ConfigMaps, создайте новую ClusterRole:

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



labels:



rbac.dynatrace.com/aggregate-to-monitoring: "true"



rules:



- apiGroups:



- ""



resources:



- configmaps



- secrets



verbs:



- list



- watch



- get
```

Метка `rbac.dynatrace.com/aggregate-to-monitoring: "true"` обязательна для агрегации вашей ClusterRole. Без этой метки разрешения не будут предоставлены ActiveGate.

Разрешения агрегируются сразу после применения ClusterRole и вступают в силу без перезапуска подов Operator или ActiveGate.
