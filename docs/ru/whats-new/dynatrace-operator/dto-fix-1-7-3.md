---
title: Примечания к выпуску Dynatrace Operator версии 1.7.3
source: https://www.dynatrace.com/docs/whats-new/dynatrace-operator/dto-fix-1-7-3
scraped: 2026-03-06T21:31:36.475717
---

**Дата выпуска:** 19 января 2025

## Исправления

### Обработка удаленных версий API при обновлении

Kubernetes не удаляет старые версии из `.status.storedVersions` CRD. В версиях Operator < 1.4 накопились `v1beta1`/`v1beta2`, что может блокировать будущие обновления.

**Решение (двухэтапное):**

1. **Хук Helm** — Job Kubernetes удаляет устаревшие версии из `status.storedVersions` перед обновлением CRD
2. **Миграция при запуске** — Operator 1.7.3 мигрирует все DynaKube на `v1beta5` и обновляет `status.storedVersions`

**Важно:**

- **Operator <= 1.2** — обновление до 1.7.3 обязательно как промежуточный шаг
- **Helm >= 1.3.0** — дополнительных действий не требуется
- **Альтернативные методы** (OperatorHub, Google Marketplace, манифесты) — обязательно через 1.7.3

**Ручная очистка CRD (альтернатива):**
```
kubectl -n dynatrace get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
storage_version=$(kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}')
kubectl get dynakube -n dynatrace -o yaml | kubectl apply -f -
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource='status' --type='merge' -p "{\"status\":{\"storedVersions\":[\"${storage_version}\"]}}"
```

## Известные проблемы (1.7.0-1.7.3)

- Объединение монтирований в `/var/lib/dynatrace` — компоненты Dynatrace не могут внедряться вместе с OneAgent
- Classic full-stack и обогащение метаданными несовместимы в одних подах

## Устаревание

- Helm-репо `dynatrace/helm-charts` устарел — обновите на `dynatrace/dynatrace-operator`
- DynaKube API: `v1beta1`/`v1beta2` удалены; `v1beta3` будет удалена в 1.8
- Поле `.autoUpdate` устарело — используйте `.version` или закрепите версию на тенанте
- CSI sidecar бинарные файлы устарели
- OpenShift 4.10/4.11 больше не поддерживаются

## Обновление с версии 1.6

DynaKube API `v1beta1`/`v1beta2` не обслуживаются. Обновите манифесты до `v1beta5` перед обновлением.
