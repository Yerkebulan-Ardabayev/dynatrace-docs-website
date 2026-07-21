---
title: Миграция DynaKube с v1beta2 на v1beta4
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4
---

# Миграция DynaKube с v1beta2 на v1beta4

# Миграция DynaKube с v1beta2 на v1beta4

* Справочник
* Чтение 10 минут
* Обновлено 22 окт. 2025 г.

Это руководство показывает, как вручную перейти с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta2

**Введено в**: Dynatrace Operator версии 1.2.0

**Устарело в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая версия**: Dynatrace Operator 1.6.2

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

**Устарело в**: Dynatrace Operator версии 1.9.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также любые другие поля, которые были изменены

### Заменённые feature flags

#### Новый feature flag таймаута монтирования CSI

Feature flag, который управлял тем, сколько попыток монтирования делает CSI driver перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён на feature flag на основе таймаута. Это сделано из-за сложности определения того, сколько попыток соответствует заданному таймауту.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

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

### Удалённые поля

#### `spec.applicationMonitoring.useCSIDriver`

Поле `spec.applicationMonitoring.useCSIDriver: true/false` удалено.

CSI driver теперь используется, если он установлен как часть установки Dynatrace Operator.