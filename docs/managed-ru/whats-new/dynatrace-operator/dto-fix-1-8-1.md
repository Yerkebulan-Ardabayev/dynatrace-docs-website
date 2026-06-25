---
title: Заметки о выпуске Dynatrace Operator версии 1.8.1
source: https://docs.dynatrace.com/managed/whats-new/dynatrace-operator/dto-fix-1-8-1
scraped: 2026-05-12T12:13:31.434897
---

# Заметки о выпуске Dynatrace Operator версии 1.8.1

# Заметки о выпуске Dynatrace Operator версии 1.8.1

* Заметки о выпуске
* Updated on Apr 09, 2026

Дата выпуска: February 9th, 2026

На этой странице представлен обзор исправлений, включённых в Dynatrace Operator версии 1.8.1. Подробную информацию о новых функциях и других улучшениях см. в [заметках о выпуске версии 1.8](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Release notes for Dynatrace Operator, version 1.8.0").

## Исправленные ошибки

* Разрешения ActiveGate на маркетплейсе OperatorHub

  Dynatrace Operator 1.8.1 теперь включает ресурсы RBAC, которые ранее отсутствовали при установке на основе ClusterServiceVersion (CSV). Процесс сборки бандла Dynatrace Operator изменён для преодоления ограничений CSV, касающихся агрегированных ролей, которые вызывали данную проблему.

  **Ограничение:** ClusterRoleBinding, включённый в это исправление, жёстко привязан к ServiceAccount `dynatrace-activegate` в пространстве имён `dynatrace`. Если вы развёртываете Dynatrace Operator в другом пространстве имён, необходимые разрешения для мониторинга Kubernetes не будут предоставлены, что приведёт к тому же поведению, что и в версии 1.8.0.

* Список разрешённых источников (allowlist) мониторинга логов на GKE Autopilot

  Исправлена проблема с мониторингом логов на GKE Autopilot, при которой суффикс тенанта, добавляемый к HostPath для поддержки RKE, вызывал сбои валидации.

## Известные ошибки

* RBAC для мониторинга Kubernetes требует повышенных разрешений для развёртывания агрегированного ClusterRole. Это затрагивает инструменты, например ArgoCD, управляющие рабочими нагрузками без разрешений cluster-admin.

## Уведомления об удалении и прекращении поддержки (deprecation)

* Удалена поддержка Rancher Kubernetes Engine 1 (RKE1) из поддерживаемых дистрибутивов.

* Helm-репозиторий по адресу `dynatrace/helm-charts` объявлен устаревшим и прекратит получать обновления в будущем выпуске. Обновите URL следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

## Обновление с Dynatrace Operator версии 1.7

* Указание образа в `.spec.templates.otelCollector.imageRef` теперь обязательно при включённом приёме телеметрии.
* Устаревшие версии API DynaKube `v1beta1` и `v1beta2` удалены из схемы CRD DynaKube.
* Версия API DynaKube `v1beta3` больше не обслуживается и будет удалена в будущем выпуске Dynatrace Operator.
* Обновление Dynatrace Operator может привести к перезапуску ActiveGate, DaemonSet OneAgent и DaemonSet Log Monitoring.
* Если вы отслеживаете Kubernetes через публичный Kubernetes API изнутри внутрикластерного ActiveGate, необходимо пересоздать токен-носитель, так как имя ServiceAccount изменилось с `dynatrace-kubernetes-monitoring` на `dynatrace-activegate`. Следуйте инструкциям в разделе [Подключение к публичному Kubernetes API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Monitor the Kubernetes API using Dynatrace").
* В связи с изменениями объектов RBAC ActiveGate установка `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`. **Перед обновлением обязательно скорректируйте значения Helm, если это применимо.**