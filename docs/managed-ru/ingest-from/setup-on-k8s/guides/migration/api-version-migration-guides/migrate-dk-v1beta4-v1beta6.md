---
title: Миграция DynaKube v1beta4 на v1beta6
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6
---

# Миграция DynaKube v1beta4 на v1beta6

# Миграция DynaKube v1beta4 на v1beta6

* Справочник
* Чтение 5 мин.
* Обновлено 19 марта 2026 г.

В этом руководстве показано, как вручную перейти с `apiVersion: dynatrace.com/v1beta4` на `apiVersion: dynatrace.com/v1beta6` DynaKube.

## Жизненный цикл поддержки

### v1beta4

**Введена в**: Dynatrace Operator версии 1.5.0

**Устарела в**: Dynatrace Operator версии 1.9.0

### v1beta6

**Введена в**: Dynatrace Operator версии 1.8.0

## Изменения

Напоминание

При миграции DynaKube не забыть обновить поле `apiVersion`, а также любые другие поля, которые изменились

### Переименованные поля

#### `spec.activeGate.persistentVolumeClaim`

Поле `spec.activeGate.persistentVolumeClaim` переименовано в `spec.activeGate.volumeClaimTemplate`. Функциональность остаётся прежней.

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") в `v1beta5`, поэтому использовать его не следует.

Рекомендуется следующее:

* Если нужен `autoUpdate: true`, не задавать `image`, `codeModulesImage` или `version`.

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack: {} # same as autoUpdate: true



  # ...
  ```
* Если нужен `autoUpdate: false`, задать `image`, `codeModulesImage` или `version`

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  image: ... # same effect as autoUpdate: false



  codeModulesImage: # same effect as autoUpdate: false



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



  version: ... # replaces autoUpdate: false



  # ...
  ```

### Перемещённые поля

#### `spec.extensions`

Поле `spec.extensions` перемещено в `spec.extensions.prometheus`, чтобы освободить место для нового поля `spec.extensions.databases`. Функциональность остаётся прежней.