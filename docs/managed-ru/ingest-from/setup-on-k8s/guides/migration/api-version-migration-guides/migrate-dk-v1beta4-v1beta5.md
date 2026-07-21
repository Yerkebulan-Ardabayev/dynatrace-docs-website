---
title: Миграция DynaKube v1beta4 на v1beta5
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5
---

# Миграция DynaKube v1beta4 на v1beta5

# Миграция DynaKube v1beta4 на v1beta5

* Справка
* 10 минут на чтение
* Обновлено 19 марта 2026 г.

Это руководство показывает, как вручную перейти с `apiVersion: dynatrace.com/v1beta4` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

**Устарело в**: Dynatrace Operator версии 1.9.0

### v1beta5

**Введено в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забыть обновить поле `apiVersion`, а также любые другие изменившиеся поля

### Переименованные поля

#### `spec.activeGate.persistentVolumeClaim`

Поле `spec.activeGate.persistentVolumeClaim` переименовано в `spec.activeGate.volumeClaimTemplate`. Функциональность осталась той же.

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") в `v1beta5`, поэтому его не следует использовать.

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