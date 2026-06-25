---
title: Агрегация ClusterRole для мониторинга Kubernetes
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation
scraped: 2026-05-12T12:09:08.953469
---

# Агрегация ClusterRole для мониторинга Kubernetes

# Агрегация ClusterRole для мониторинга Kubernetes

* Чтение: 2 мин
* Обновлено 9 декабря 2025 г.

Dynatrace Operator версия 1.8.0

Начиная с Dynatrace Operator версии 1.9.0, агрегированные ClusterRole больше не используются. В развёртывании Dynatrace Operator теперь используются исключительно стандартные ClusterRole. Эта страница относится только к Operator версии 1.8. Причины этого изменения см. в [примечаниях к выпуску 1.9.0](/managed/whats-new/dynatrace-operator/dto-fix-1-9-0 "Примечания к выпуску Dynatrace Operator, версия 1.9.0").

В Dynatrace Operator версии 1.8.0 компонент ActiveGate использует ServiceAccount, привязывающий ClusterRole `dynatrace-kubernetes-monitoring`. Этот ClusterRole является **агрегированной ролью**, обеспечивающей простую и гибкую настройку назначенных разрешений RBAC. [1](#fn-1-1-def)

1

Агрегация ClusterRole, это функция Kubernetes RBAC, которая позволяет объединять несколько ClusterRole в один агрегированный ClusterRole. Агрегирующий ClusterRole использует селекторы меток для определения того, какие другие ClusterRole следует включить. Подробнее см. [агрегация ClusterRole в документации Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).

## Разрешения по умолчанию

По умолчанию при установке Dynatrace Operator создаётся ClusterRole `dynatrace-kubernetes-monitoring-default`, который содержит стандартный набор разрешений, необходимых для мониторинга платформы Kubernetes. Этому ClusterRole автоматически присваивается метка `rbac.dynatrace.com/aggregate-to-monitoring: "true"`, поэтому его разрешения включаются в агрегированную роль.

Разрешения по умолчанию описаны в [справочнике по безопасности](/managed/ingest-from/setup-on-k8s/reference/security#activegate "На этой странице приведён обзор компонентов Dynatrace, их конфигураций по умолчанию и требуемых им разрешений") и охватывают стандартный мониторинг:

* Подов, деплойментов, StatefulSet и других ресурсов рабочих нагрузок.
* Сервисов и эндпоинтов.
* Узлов и метрик ресурсов.
* Событий и информации о кластере.

## Расширение ClusterRole дополнительными разрешениями

Чтобы расширить функциональность мониторинга за пределы разрешений по умолчанию, создайте дополнительные ClusterRole с меткой агрегации. Любой ClusterRole с меткой `rbac.dynatrace.com/aggregate-to-monitoring: "true"` автоматически агрегируется, и его разрешения предоставляются ServiceAccount ActiveGate.

### Пример: разрешение мониторинга конфиденциальных данных

Чтобы включить мониторинг конфиденциальных объектов Kubernetes, таких как Secret и ConfigMap, создайте новый ClusterRole:

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

Метка `rbac.dynatrace.com/aggregate-to-monitoring: "true"` необходима, чтобы ваш ClusterRole был агрегирован. Без этой метки разрешения не предоставляются ActiveGate.

Разрешения агрегируются сразу после применения ClusterRole и вступают в силу без необходимости перезапуска подов Operator или ActiveGate.