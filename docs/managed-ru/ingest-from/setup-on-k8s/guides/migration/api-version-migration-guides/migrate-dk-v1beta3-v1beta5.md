---
title: Миграция DynaKube с v1beta3 на v1beta5
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5
---

# Миграция DynaKube с v1beta3 на v1beta5

# Миграция DynaKube с v1beta3 на v1beta5

* Справочник
* Чтение 10 мин.
* Обновлено 22 янв. 2026 г.

Это руководство показывает, как вручную выполнить миграцию `DynaKube` с `apiVersion: dynatrace.com/v1beta3` на `apiVersion: dynatrace.com/v1beta5`.

## Жизненный цикл поддержки

### v1beta3

**Введена в**: Dynatrace Operator версии 1.4.0

**Устарела в**: Dynatrace Operator версии 1.6.0

### v1beta5

**Введена в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились

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