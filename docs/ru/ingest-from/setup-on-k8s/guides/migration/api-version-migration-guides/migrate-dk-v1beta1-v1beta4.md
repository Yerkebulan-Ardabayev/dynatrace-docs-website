---
title: Миграция DynaKube v1beta1 на v1beta4
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4
scraped: 2026-03-05T21:32:55.534393
---

# Миграция DynaKube с v1beta1 на v1beta4


* Latest Dynatrace
* Reference
* Время чтения: 10 мин
* Обновлено 22 октября 2025 г.

В этом руководстве показано, как вручную мигрировать с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta4` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta1

**Введён в**: Dynatrace Operator версии 0.3.0

**Объявлен устаревшим в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая версия**: Dynatrace Operator версии 1.6.2

### v1beta4

**Введён в**: Dynatrace Operator версии 1.5.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные изменившиеся поля.

### Заменённые флаги функций

#### Отдельная секция `metadataEnrichment`

Флаг функции для включения обогащения метаданными (`feature.dynatrace.com/metadata-enrichment: true/false`) был перенесён в отдельное поле:

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

Флаг функции для управления частотой обращений Dynatrace Operator к Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`) был перенесён в отдельное поле:

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

Флаг функции, управляющий профилем seccomp для DaemonSet OneAgent (`feature.dynatrace.com/oneagent-seccomp-profile:example`), был перенесён в отдельное поле:

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

#### Новый флаг функции для тайм-аута монтирования CSI

Флаг функции, контролировавший количество попыток монтирования CSI-драйвера перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), был заменён флагом функции на основе тайм-аута. Это было сделано из-за сложности определения того, какое количество попыток соответствует заданному тайм-ауту.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Перемещённые поля

#### `spec.namespaceSelector`

Поле `spec.namespaceSelector` было перемещено в каждую подсекцию функции, на которую оно влияет.

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

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [объявлено устаревшим](../../deployment-and-configuration/updates-and-maintenance/auto-update-components.md "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") в `v1beta5`, поэтому его не следует использовать.

Мы рекомендуем следующее:

* Если вы хотите `autoUpdate: true`, не задавайте `image`, `codeModulesImage` или `version`.

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
* Если вы хотите `autoUpdate: false`, задайте `image`, `codeModulesImage` или `version`

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

CSI-драйвер теперь используется при установке в составе установки Dynatrace Operator.

#### `spec.kubernetesMonitoring`

Устаревшее поле `spec.kubernetesMonitoring` было удалено в пользу использования текущей секции `spec.activeGate`. Этот пример показывает состояние до и после:

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

Устаревшее поле `spec.routing` было удалено в пользу использования текущей секции `spec.activeGate`. Этот пример показывает состояние до и после:

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
