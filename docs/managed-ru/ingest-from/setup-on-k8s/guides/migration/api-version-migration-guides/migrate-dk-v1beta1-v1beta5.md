---
title: Миграция DynaKube с v1beta1 на v1beta5
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5
---

# Миграция DynaKube с v1beta1 на v1beta5

# Миграция DynaKube с v1beta1 на v1beta5

* Справочник
* Чтение: 10 минут
* Обновлено 30 октября 2025 г.

Это руководство показывает, как вручную перейти с `apiVersion: dynatrace.com/v1beta1` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta1

**Введена в**: Dynatrace Operator версии 0.3.0

**Устарела в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая версия**: Dynatrace Operator версии 1.6.2

### v1beta5

**Введена в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все остальные поля, которые изменились

### Подготовка к удалению apiVersion v1beta1

Уведомление

apiVersion v1beta1 CRD DynaKube будет удалён в одном из следующих релизов. Рекомендуется подготовиться к этому заранее.
Действия пользователя потребуются при обновлении с Dynatrace Operator версии 1.1.0 и более ранних.

Запрос текущей версии хранения CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Запрос сохранённых версий CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Если **список сохранённых версий** содержит версии, которые будут удалены при обновлении CRD, **требуется вмешательство пользователя**.

Нужно убедиться, что старый apiVersion больше нигде не упоминается ни в одном манифесте. Это касается и ресурсов, которые загружают манифесты из внешних источников, например релизов Helm или приложений ArgoCD.
При использовании GitOps всегда нужно проверять источник, из которого синхронизируются манифесты, так как при формировании diff может учитываться преобразование версий.

Чтобы убедиться, что бэкенд хранения Kubernetes больше не содержит устаревших объектов DynaKube, рекомендуется обновить их на месте.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do



namespace=${item%/*}



name=${item#*/}



kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -



done
```

Не используйте команду `kubectl apply`, так как она записывает данные, только если обнаружены изменения.

После того как старый apiVersion больше нигде не упоминается, можно безопасно обновить статус CRD.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Заменённые feature flags

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



enabled: true # заменяет feature.dynatrace.com/metadata-enrichment: true



#...
```

#### Отдельное поле `dynatraceApiRequestThreshold`

Feature flag, управляющий тем, как часто Dynatrace Operator может опрашивать Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`), перенесён в отдельное поле:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



dynatraceApiRequestThreshold: 10 # заменяет feature.dynatrace.com/dynatrace-api-request-threshold: "10"



#...
```

#### Отдельное поле `secCompProfile` для OneAgent

Feature flag, управляющий тем, какой seccomp-профиль использует DaemonSet OneAgent (`feature.dynatrace.com/oneagent-seccomp-profile:example`), перенесён в отдельное поле:

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



secCompProfile: example # заменяет feature.dynatrace.com/oneagent-seccomp-profile: "example"



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



secCompProfile: example # заменяет feature.dynatrace.com/oneagent-seccomp-profile: "example"



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



secCompProfile: example # заменяет feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

#### Новый feature flag тайм-аута монтирования CSI

Feature flag, контролировавший, сколько попыток монтирования выполнит CSI-драйвер перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён на feature flag на основе тайм-аута. Это сделано из-за сложности определения того, скольким попыткам соответствует тот или иной тайм-аут.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # заменяет feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Перемещённые поля

#### `spec.namespaceSelector`

Поле `spec.namespaceSelector` перенесено в каждый подраздел функции, на который оно влияет.

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



namespaceSelector: ... # заменяет spec.namespaceSelector



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



namespaceSelector: ... # заменяет spec.namespaceSelector



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



namespaceSelector: ... # заменяет spec.namespaceSelector



# ...
```

### Устаревшие поля

#### `autoUpdate` для OneAgent

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [устарело](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") в `v1beta5`, поэтому его не следует использовать.

Рекомендуется следующее:

* Если нужен `autoUpdate: true`, не задавайте `image`, `codeModulesImage` или `version`.

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
* Если нужен `autoUpdate: false`, задайте `image`, `codeModulesImage` или `version`

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  image: ... # даёт тот же эффект, что и autoUpdate: false



  codeModulesImage: # даёт тот же эффект, что и autoUpdate: false



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

Поле `spec.applicationMonitoring.useCSIDriver: true/false` удалено.

CSI-драйвер теперь используется, когда он установлен как часть установки Dynatrace Operator.

#### `spec.kubernetesMonitoring`

Устаревшее поле `spec.kubernetesMonitoring` удалено в пользу использования текущего раздела `spec.activeGate`. В этом примере показано состояние до и после:

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



- kubernetes-monitoring #<-- явно включить мониторинг Kubernetes



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

Устаревшее поле `spec.routing` удалено в пользу использования текущего раздела `spec.activeGate`. В этом примере показано состояние до и после:

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



- routing #<-- явно включить routing



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