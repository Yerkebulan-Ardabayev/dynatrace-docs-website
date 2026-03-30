---
title: Миграция DynaKube v1beta4 на v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5
scraped: 2026-03-06T21:38:00.887786
---

# Миграция DynaKube с v1beta4 на v1beta5


* Latest Dynatrace
* 10-min read

В этом руководстве описано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta4` на `apiVersion: dynatrace.com/v1beta4` ресурса `DynaKube`.

## Жизненный цикл поддержки

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

### v1beta5

**Введено в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также любые другие изменённые поля.

### Переименованные поля

#### `spec.activeGate.persistentVolumeClaim`

Поле `spec.activeGate.persistentVolumeClaim` переименовано в `spec.activeGate.volumeClaimTemplate`. Функциональность остаётся прежней.

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` устарело.") в `v1beta5`, поэтому его использование не рекомендуется.

Рекомендуется следующее:

* Если вы хотите использовать `autoUpdate: true`, не задавайте `image`, `codeModulesImage` или `version`.

  ```
  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack: {} # то же самое, что autoUpdate: true


  # ...
  ```
* Если вы хотите использовать `autoUpdate: false`, задайте `image`, `codeModulesImage` или `version`.

  ```
  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack:


  image: ... # тот же эффект, что и autoUpdate: false


  codeModulesImage: # тот же эффект, что и autoUpdate: false


  # ...


  ---


  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack:


  version: ... # заменяет autoUpdate: false


  # ...
  ```
