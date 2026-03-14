---
title: Миграция DynaKube v1beta1 на v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5
scraped: 2026-03-05T21:36:12.229894
---

# Миграция DynaKube с v1beta1 на v1beta5


* Latest Dynatrace
* Справочник
* 10 мин чтения
* Обновлено 30 октября 2025

Это руководство покажет вам, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta1

**Представлено в**: Dynatrace Operator версии 0.3.0

**Устарело в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая версия**: Dynatrace Operator версии 1.6.2

### v1beta5

**Представлено в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все другие изменившиеся поля

### Подготовка к удалению apiVersion v1beta1

Уведомление

Версия apiVersion v1beta1 CRD DynaKube будет удалена в будущем релизе. Рекомендуем подготовиться к этому заранее.
При обновлении с Dynatrace Operator версии 1.1.0 и более ранних потребуются действия пользователя.

Запросите текущую версию хранилища CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Запросите сохранённые версии CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Если **список сохранённых версий** содержит версии, которые будут удалены при обновлении CRD, **требуется вмешательство пользователя**.

Убедитесь, что старая версия apiVersion больше не используется ни в одном манифесте. Это включает ресурсы, загружающие манифесты из внешних источников, таких как Helm-релизы или приложения ArgoCD.
При использовании GitOps всегда проверяйте источник, из которого синхронизируются манифесты, поскольку сравнение может учитывать конверсию.

Чтобы гарантировать, что серверная часть хранилища Kubernetes больше не содержит устаревших объектов DynaKube, рекомендуем обновить их на месте.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do


namespace=${item%/*}


name=${item#*/}


kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -


done
```

Не используйте команду `kubectl apply`, так как она записывает данные только при обнаружении изменений.

После того как старая версия apiVersion больше не используется, можно безопасно обновить статус CRD.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Заменённые флаги функций

#### Выделенная секция `metadataEnrichment`

Флаг функции для включения обогащения метаданных (`feature.dynatrace.com/metadata-enrichment: true/false`) был перенесён в выделенное поле:

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

#### Выделенное поле `dynatraceApiRequestThreshold`

Флаг функции для управления частотой обращений Dynatrace Operator к Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`) был перенесён в выделенное поле:

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

#### Выделенное поле `secCompProfile` для OneAgent

Флаг функции, управляющий тем, какой профиль seccomp использует DaemonSet OneAgent (`feature.dynatrace.com/oneagent-seccomp-profile:example`), был перенесён в выделенное поле:

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

#### Новый флаг функции для таймаута монтирования CSI

Флаг функции, который контролировал количество попыток монтирования CSI-драйвера до остановки (`feature.dynatrace.com/max-csi-mount-attempts: 5`), был заменён флагом на основе таймаута. Это было сделано из-за сложности определения того, сколько попыток соответствует заданному таймауту.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Перемещённые поля

#### `spec.namespaceSelector`

Поле `spec.namespaceSelector` было перемещено в каждую подсекцию функций, на которую оно влияет.

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

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](../../deployment-and-configuration/updates-and-maintenance/auto-update-components.md "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") в `v1beta5`, поэтому его не следует использовать.

Мы рекомендуем следующее:

* Если вы хотите `autoUpdate: true`, не устанавливайте `image`, `codeModulesImage` или `version`.

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
* Если вы хотите `autoUpdate: false`, установите `image`, `codeModulesImage` или `version`

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

CSI-драйвер теперь используется, когда он установлен в рамках установки Dynatrace Operator.

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