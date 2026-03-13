---
title: Dynatrace Operator release notes version 1.8.1
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-8-1
scraped: 2026-03-06T21:37:12.752343
---

# Примечания к выпуску Dynatrace Operator версии 1.8.1

# Примечания к выпуску Dynatrace Operator версии 1.8.1

* Latest Dynatrace
* Release notes
* Updated on Feb 09, 2026

Дата выпуска: 9 февраля 2026 года

Данная страница содержит обзор патчей, включённых в Dynatrace Operator версии 1.8.1. Подробную информацию о новых функциях и других улучшениях см. в [примечаниях к выпуску версии 1.8](/docs/whats-new/dynatrace-operator/dto-fix-1-8-0 "Примечания к выпуску Dynatrace Operator, версия 1.8.0.").

## Исправленные проблемы

* Разрешения ActiveGate в маркетплейсе OperatorHub

  Dynatrace Operator 1.8.1 теперь включает RBAC-ресурсы, которые ранее отсутствовали для установок на основе ClusterServiceVersion (CSV). Процесс сборки бандла Dynatrace Operator был изменён для преодоления ограничений CSV в отношении агрегированных ролей, которые вызывали данную проблему.

* Список разрешённых адресов для мониторинга логов в GKE Autopilot

  Исправлена проблема с мониторингом логов в GKE Autopilot, при которой суффикс тенанта, добавляемый к HostPath для поддержки RKE, приводил к ошибкам валидации.

## Уведомления об удалении и устаревании

* Репозиторий Helm, расположенный по адресу `dynatrace/helm-charts`, является устаревшим и в будущем выпуске прекратит получать обновления. Если вы всё ещё используете его,
  обновите URL до `dynatrace/dynatrace-operator` или перейдите на подход с использованием реестра OCI. Обновите URL репозитория Helm следующими командами:

  ```
  helm repo remove dynatrace



  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```

* Во избежание возможных сбоев настоятельно рекомендуется поддерживать версию DynaKube API в актуальном состоянии. После того как версия будет признана устаревшей и удалена, обновления могут стать значительно более сложными и требовательными по времени.

  + Подробнее о процессе устаревания версий DynaKube API можно узнать в [руководстве по миграции](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Перенесите ваш DynaKube CR на более новые версии apiVersion в соответствии с используемой версией Operator.").

## Обновление с Dynatrace Operator версии 1.7

* Указание образа в `.spec.templates.otelCollector.imageRef` теперь является обязательным при включённом [получении телеметрии](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Включите конечные точки получения телеметрии Dynatrace в Kubernetes для локального приёма данных в кластере.").
* Устаревшие версии DynaKube API `v1beta1` и `v1beta2` были удалены из схемы CRD DynaKube.
* Версия DynaKube API `v1beta3` больше не обслуживается и будет удалена в будущем выпуске Dynatrace Operator. См.: [Руководство по миграции версий DynaKube API](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube#deprecation "Перенесите ваш DynaKube CR на более новые версии apiVersion в соответствии с используемой версией Operator.")
* Обновление Dynatrace Operator может перезапустить ActiveGate, DaemonSet OneAgent (хостовый агент) и DaemonSet мониторинга логов.
* Если вы осуществляете мониторинг Kubernetes через публичный Kubernetes API с использованием внутрикластерного ActiveGate, вам потребуется воссоздать bearer-токен, поскольку имя используемого ServiceAccount изменилось с `dynatrace-kubernetes-monitoring` на `dynatrace-activegate`. Следуйте инструкциям в разделе [Подключение к публичному Kubernetes API](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect "Мониторинг Kubernetes API с помощью Dynatrace").
* В связи с вышеупомянутыми изменениями в объектах RBAC ActiveGate, установка `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`. **Обязательно скорректируйте значения Helm при необходимости перед обновлением.**
