---
title: Миграция DynaKube v1beta2 на v1beta5
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5
---

# Миграция DynaKube v1beta2 на v1beta5

# Миграция DynaKube v1beta2 на v1beta5

* Справочник
* Чтение занимает 10 мин.
* Обновлено 30 октября 2025 г.

Это руководство показывает, как вручную перейти с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta2

**Введено в**: Dynatrace Operator версии 1.2.0

**Признано устаревшим в**: Dynatrace Operator версии 1.6.0

**Последняя версия с поддержкой**: Dynatrace Operator версии 1.6.2

### v1beta5

**Введено в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забыть обновить поле `apiVersion`, а также все остальные изменившиеся поля

### Подготовка к удалению apiVersion v1beta2

Уведомление

apiVersion v1beta2 CRD DynaKube будет удалён в одном из следующих релизов. Рекомендуется подготовиться к этому заранее.
Потребуется вмешательство пользователя при обновлении с Dynatrace Operator версии 1.3.0 и более ранних.

Запрос текущей версии хранения CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Запрос сохранённых версий CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Если **список сохранённых версий** содержит версии, которые будут удалены при обновлении CRD, **требуется вмешательство пользователя**.

Нужно убедиться, что на старый apiVersion больше не ссылается ни один манифест. Это касается и ресурсов, загружающих манифесты из внешних источников, например релизов Helm или приложений ArgoCD.
При использовании GitOps всегда нужно проверять источник, из которого синхронизируются манифесты, потому что при сравнении diff может учитываться конвертация.

Чтобы в бэкенде хранения Kubernetes больше не оставалось устаревших объектов DynaKube, рекомендуется обновить их на месте.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do



namespace=${item%/*}



name=${item#*/}



kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -



done
```

Не использовать команду `kubectl apply`, так как она записывает данные только при обнаружении изменений.

После того как на старый apiVersion больше нет ссылок, можно безопасно обновить статус CRD.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Заменённые feature flag

#### Новый feature flag таймаута монтирования CSI

Feature flag, управлявший количеством попыток монтирования, которые CSI driver выполнял перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён на feature flag, основанный на таймауте. Это сделано из-за сложности определения, скольким попыткам соответствует заданный таймаут.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # заменяет feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Устаревшие поля

#### OneAgent `autoUpdate`

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [признано устаревшим](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator") в `v1beta5`, поэтому его использовать не следует.

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

CSI driver теперь используется, когда он установлен как часть установки Dynatrace Operator.