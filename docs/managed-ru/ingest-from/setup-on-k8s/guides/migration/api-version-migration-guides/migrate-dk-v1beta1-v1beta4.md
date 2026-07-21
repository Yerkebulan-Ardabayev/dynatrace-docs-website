---
title: Миграция DynaKube v1beta1 на v1beta4
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4
---

# Миграция DynaKube v1beta1 на v1beta4

# Миграция DynaKube v1beta1 на v1beta4

* Справка
* Чтение: 10 мин
* Обновлено 22 октября 2025 г.

В этом руководстве показано, как вручную перейти с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta1

**Введено в**: Dynatrace Operator версии 0.3.0

**Устарело в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая версия**: Dynatrace Operator 1.6.2

### v1beta4

**Введено в**: Dynatrace Operator версии 1.5.0

**Устарело в**: Dynatrace Operator версии 1.9.0

## Изменения

Напоминание

При миграции DynaKube не забудь обновить поле `apiVersion`, а также все остальные поля, которые изменились

### Заменённые feature flag

#### Отдельный раздел `metadataEnrichment`

Feature flag для включения обогащения метаданных (`feature.dynatrace.com/metadata-enrichment: true/false`) перенесён в отдельное поле:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



enabled: true # replaces feature.dynatrace.com/metadata-enrichment: true



#...
```

#### Отдельное поле `dynatraceApiRequestThreshold`

Feature flag, управляющий тем, как часто Dynatrace Operator может обращаться к Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`), перенесён в отдельное поле:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



dynatraceApiRequestThreshold: 10 # replaces feature.dynatrace.com/dynatrace-api-request-threshold: "10"



#...
```

#### Отдельное поле `secCompProfile` для OneAgent

Feature flag, определяющий, какой seccomp-профиль использует DaemonSet OneAgent (`feature.dynatrace.com/oneagent-seccomp-profile:example`), перенесён в отдельное поле:

Host monitoring

Classic fullstack

Cloud native fullstack

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



hostMonitoring:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



classicFullStack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

#### Новый feature flag для тайм-аута монтирования CSI

Feature flag, управлявший тем, сколько попыток монтирования делает CSI-драйвер перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён на feature flag, основанный на тайм-ауте. Это сделано из-за сложности определения того, сколько попыток соответствует заданному тайм-ауту.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Перенесённые поля

#### `spec.namespaceSelector`

Поле `spec.namespaceSelector` перенесено в каждый подраздел функции, на которую оно влияет.

Cloud native fullstack

Application monitoring

Metadata enrichment

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



applicationMonitoring:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") в `v1beta5`, поэтому его не следует использовать.

Рекомендуется следующее:

* Если нужен `autoUpdate: true`, не задавай `image`, `codeModulesImage` или `version`.

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
* Если нужен `autoUpdate: false`, задай `image`, `codeModulesImage` или `version`

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

Теперь CSI-драйвер используется, когда он установлен как часть установки Dynatrace Operator.

#### `spec.kubernetesMonitoring`

Устаревшее поле `spec.kubernetesMonitoring` удалено в пользу использования текущего раздела `spec.activeGate`. Пример показывает состояние до и после:

**До**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



kubernetesMonitoring:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**После**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- kubernetes-monitoring #<-- explicitly enable Kubernetes monitoring



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

#### `spec.routing`

Устаревшее поле `spec.routing` удалено в пользу использования текущего раздела `spec.activeGate`. Пример показывает состояние до и после:

**До**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



routing:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**После**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- routing #<-- explicitly enable routing



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```