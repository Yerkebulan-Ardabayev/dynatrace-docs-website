---
title: Миграция DynaKube с v1beta1 на v1beta5
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5
scraped: 2026-05-12T12:14:50.289595
---

# Миграция DynaKube с v1beta1 на v1beta5

# Миграция DynaKube с v1beta1 на v1beta5

* Справочник
* Чтение: 10 мин
* Обновлено 30 октября 2025 г.

В этом руководстве показано, как вручную выполнить миграцию с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta1

**Введено в**: Dynatrace Operator версии 0.3.0

**Устарело в**: Dynatrace Operator версии 1.6.0

**Последняя поддержка в**: Dynatrace Operator версии 1.6.2

### v1beta5

**Введено в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились

### Подготовка к удалению apiVersion v1beta1

Примечание

apiVersion v1beta1 в DynaKube CRD будет удалён в будущем выпуске. Рекомендуем подготовиться к этому заранее.
Действие пользователя потребуется при обновлении с Dynatrace Operator версии 1.1.0 и более ранних.

Запросите текущую версию хранилища DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Запросите сохранённые версии DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Если **список сохранённых версий** содержит версии, которые будут удалены при обновлении CRD, **требуется вмешательство пользователя**.

Убедитесь, что старый apiVersion больше не используется ни в одном манифесте. Это включает ресурсы, которые загружают манифесты из внешних источников, такие как релизы Helm или приложения ArgoCD.
При использовании GitOps всегда проверяйте источник, из которого синхронизируются манифесты, поскольку при вычислении различий может учитываться преобразование.

Чтобы убедиться, что бэкенд хранилища Kubernetes больше не содержит устаревших объектов DynaKube, рекомендуем обновить их на месте.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do



namespace=${item%/*}



name=${item#*/}



kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -



done
```

Не используйте команду `kubectl apply`, поскольку она записывает данные только при обнаружении изменений.

Как только старый apiVersion больше не используется, можно безопасно обновить статус CRD.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Заменённые флаги функций

#### Выделенный раздел `metadataEnrichment`

Флаг функции для включения обогащения метаданными (`feature.dynatrace.com/metadata-enrichment: true/false`) был перемещён в выделенное поле:

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

Флаг функции для управления тем, как часто Dynatrace Operator может обращаться к Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`), был перемещён в выделенное поле:

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

Флаг функции, который управляет тем, какой профиль seccomp использует OneAgent DaemonSet (`feature.dynatrace.com/oneagent-seccomp-profile:example`), был перемещён в выделенное поле:

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

#### Новый флаг функции тайм-аута монтирования CSI

Флаг функции, который определял, сколько попыток монтирования делает CSI driver перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён флагом функции на основе тайм-аута. Это сделано из-за сложности определения того, скольким попыткам соответствует заданный тайм-аут.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Перемещённые поля

#### `spec.namespaceSelector`

Поле `spec.namespaceSelector` было перемещено в каждый подраздел функции, на который оно влияет.

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

#### `spec.kubernetesMonitoring`

Устаревшее поле `spec.kubernetesMonitoring` было удалено в пользу использования текущего раздела `spec.activeGate`. В этом примере показано до и после:

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

Устаревшее поле `spec.routing` было удалено в пользу использования текущего раздела `spec.activeGate`. В этом примере показано до и после:

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