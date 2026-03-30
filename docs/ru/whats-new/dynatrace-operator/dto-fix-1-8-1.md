---
title: Примечания к выпуску Dynatrace Operator версии 1.8.1
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-8-1
scraped: 2026-03-06T21:37:12.752343
---

**Дата выпуска:** 9 февраля 2026

Патч-релиз. Новые функции см. в примечаниях к версии 1.8.

## Исправления

- **RBAC для ActiveGate в OperatorHub** — добавлены отсутствовавшие RBAC-ресурсы для CSV-установок. Изменен процесс сборки бандла для обхода ограничений CSV с агрегированными ролями.
- **Мониторинг логов в GKE Autopilot** — исправлена ошибка валидации HostPath из-за суффикса тенанта для RKE.

## Устаревание

- Helm-репозиторий `dynatrace/helm-charts` устарел. Обновите URL:
  ```
  helm repo remove dynatrace
  helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
  ```
- Поддерживайте версию DynaKube API в актуальном состоянии. См. [руководство по миграции](../../ingest-from/setup-on-k8s/guides/migration/dynakube.md#deprecation).

## Обновление с версии 1.7

- `.spec.templates.otelCollector.imageRef` теперь обязателен при включенном приеме телеметрии
- Удалены DynaKube API `v1beta1` и `v1beta2`; `v1beta3` устарела
- Обновление может перезапустить ActiveGate, OneAgent DaemonSet и LogMonitoring DaemonSet
- При мониторинге через публичный K8s API — пересоздайте bearer-токен (ServiceAccount изменен на `dynatrace-activegate`)
- `rbac.kspm.create: true` теперь требует `rbac.activeGate.create: true` и `rbac.kubernetesMonitoring.create: true`
