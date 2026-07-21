---
title: Миграция DynaKube с v1beta3 на v1beta4
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4
---

# Миграция DynaKube с v1beta3 на v1beta4

# Миграция DynaKube с v1beta3 на v1beta4

* Справка
* Чтение: 10 мин
* Обновлено 19 марта 2026 г.

В этом руководстве показано, как вручную мигрировать `DynaKube` с `apiVersion: dynatrace.com/v1beta3` на `apiVersion: dynatrace.com/v1beta4`.

## Жизненный цикл поддержки

### v1beta3

**Введена в**: Dynatrace Operator версии 1.4.0

**Устарела в**: Dynatrace Operator версии 1.6.0

### v1beta4

**Введена в**: Dynatrace Operator версии 1.5.0

**Устарела в**: Dynatrace Operator версии 1.9.0

## Изменения

Напоминание

При миграции DynaKube не забыть обновить поле `apiVersion`, а также все прочие изменённые поля

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") в `v1beta5`, поэтому использовать его не стоит.

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