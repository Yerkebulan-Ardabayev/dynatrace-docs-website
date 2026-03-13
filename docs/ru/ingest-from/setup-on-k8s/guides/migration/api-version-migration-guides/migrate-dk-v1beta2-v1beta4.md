---
title: Migration of DynaKube v1beta2 to v1beta4
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4
scraped: 2026-03-05T21:36:05.242871
---

# Migration of DynaKube v1beta2 to v1beta4

# Миграция DynaKube с v1beta2 на v1beta4

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

Данное руководство покажет, как выполнить ручную миграцию с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta2

**Введена в**: Dynatrace Operator версии 1.2.0

**Устарела в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая в**: Dynatrace Operator версии 1.6.2

### v1beta4

**Введена в**: Dynatrace Operator версии 1.5.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также любые другие поля, которые изменились.

### Замена флагов функций

#### Новый флаг функции таймаута монтирования CSI

Флаг функции, управлявший количеством попыток монтирования CSI-драйвера перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), был заменён флагом функции на основе таймаута. Это было сделано из-за сложности определения того, сколько попыток соответствует заданному таймауту.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # заменяет feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](../../deployment-and-configuration/updates-and-maintenance/auto-update-components.md "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") в `v1beta5` и не должно использоваться.

Рекомендуется следующее:

* Если вы хотите использовать `autoUpdate: true`, не устанавливайте `image`, `codeModulesImage` или `version`.

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
* Если вы хотите использовать `autoUpdate: false`, установите `image`, `codeModulesImage` или `version`

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  image: ... # тот же эффект, что autoUpdate: false



  codeModulesImage: # тот же эффект, что autoUpdate: false



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

### Удалённые поля

#### `spec.applicationMonitoring.useCSIDriver`

Поле `spec.applicationMonitoring.useCSIDriver: true/false` было удалено.

CSI-драйвер теперь используется при установке в рамках установки Dynatrace Operator.
