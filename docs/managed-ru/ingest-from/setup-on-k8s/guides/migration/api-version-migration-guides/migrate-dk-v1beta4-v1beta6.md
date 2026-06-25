---
title: Миграция DynaKube с v1beta4 на v1beta6
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6
scraped: 2026-05-12T12:14:44.324340
---

# Миграция DynaKube с v1beta4 на v1beta6

# Миграция DynaKube с v1beta4 на v1beta6

* Справочник
* Чтение: 5 мин
* Обновлено 19 марта 2026 г.

В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta4` на `apiVersion: dynatrace.com/v1beta6` для DynaKube.

## Жизненный цикл поддержки

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

**Устарело в**: Dynatrace Operator версии 1.9.0

### v1beta6

**Введено в**: Dynatrace Operator версии 1.8.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились

### Переименованные поля

#### `spec.activeGate.persistentVolumeClaim`

Поле `spec.activeGate.persistentVolumeClaim` было переименовано в `spec.activeGate.volumeClaimTemplate`. Функциональность осталась прежней.

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Настройка автообновлений для компонентов, управляемых Dynatrace Operator (OneAgent, ActiveGate и EdgeConnect).") в `v1beta5`, поэтому его не следует использовать.

Рекомендуем следующее:

* Если вам нужно `autoUpdate: true`, не задавайте `image`, `codeModulesImage` или `version`.

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
* Если вам нужно `autoUpdate: false`, задайте `image`, `codeModulesImage` или `version`

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

Поле `spec.extensions` было перемещено в `spec.extensions.prometheus` для поддержки нового поля `spec.extensions.databases`. Функциональность осталась прежней.