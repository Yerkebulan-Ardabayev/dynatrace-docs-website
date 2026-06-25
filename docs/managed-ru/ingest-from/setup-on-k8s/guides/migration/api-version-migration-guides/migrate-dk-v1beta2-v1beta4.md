---
title: Миграция DynaKube с v1beta2 на v1beta4
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4
scraped: 2026-05-12T12:14:34.613150
---

# Миграция DynaKube с v1beta2 на v1beta4

# Миграция DynaKube с v1beta2 на v1beta4

* Справочник
* Чтение: 10 мин
* Обновлено 22 октября 2025 г.

В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta2

**Введено в**: Dynatrace Operator версии 1.2.0

**Устарело в**: Dynatrace Operator версии 1.6.0

**Последняя поддержка в**: Dynatrace Operator версии 1.6.2

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

**Устарело в**: Dynatrace Operator версии 1.9.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились

### Заменённые флаги функций

#### Новый флаг функции тайм-аута монтирования CSI

Флаг функции, который определял, сколько попыток монтирования делает CSI driver перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён флагом функции на основе тайм-аута. Это сделано из-за сложности определения того, скольким попыткам соответствует заданный тайм-аут.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

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

### Удалённые поля

#### `spec.applicationMonitoring.useCSIDriver`

Поле `spec.applicationMonitoring.useCSIDriver: true/false` было удалено.

CSI driver теперь используется, если он установлен в составе Dynatrace Operator.