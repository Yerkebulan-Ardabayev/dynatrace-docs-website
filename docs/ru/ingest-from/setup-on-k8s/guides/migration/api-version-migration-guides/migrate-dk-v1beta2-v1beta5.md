---
title: Миграция DynaKube v1beta2 на v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5
scraped: 2026-03-06T21:32:59.327256
---

# Миграция DynaKube с v1beta2 на v1beta5


* Latest Dynatrace
* 10-min read

Данное руководство покажет, как выполнить ручную миграцию с `apiVersion: dynatrace.com/v1beta2` на `apiVersion: dynatrace.com/v1beta5` для `DynaKube`.

## Жизненный цикл поддержки

### v1beta2

**Введена в**: Dynatrace Operator версии 1.2.0

**Объявлена устаревшей в**: Dynatrace Operator версии 1.6.0

**Последняя поддерживаемая в**: Dynatrace Operator версии 1.6.2

### v1beta5

**Введена в**: Dynatrace Operator версии 1.6.0

## Изменения

Напоминание

При миграции DynaKube не забудьте обновить поле `apiVersion`, а также все другие изменившиеся поля.

### Подготовка к удалению apiVersion v1beta2

Уведомление

Версия apiVersion v1beta2 CRD DynaKube будет удалена в будущем выпуске. Рекомендуется подготовиться к этому заблаговременно.
Действия пользователя потребуются при обновлении с Dynatrace Operator версии 1.3.0 и более ранних версий.

Запросите текущую версию хранилища CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Запросите сохранённые версии CRD DynaKube:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Если **список сохранённых версий** содержит версии, которые будут удалены при обновлении CRD, **требуется вмешательство пользователя**.

Убедитесь, что старая версия apiVersion больше не упоминается ни в одном манифесте. Это касается ресурсов, которые загружают манифесты из внешних источников, таких как релизы Helm или приложения ArgoCD.
При использовании GitOps всегда проверяйте источник, из которого синхронизируются манифесты, поскольку сравнение может учитывать преобразование.

Чтобы убедиться, что бэкенд хранилища Kubernetes больше не содержит устаревших объектов DynaKube, рекомендуется обновить их на месте.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do


namespace=${item%/*}


name=${item#*/}


kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -


done
```

Не используйте команду `kubectl apply`, поскольку она записывает данные только при обнаружении изменений.

После того как старая версия apiVersion больше не упоминается, можно безопасно обновить статус CRD.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Замененные флаги функций

#### Новый флаг функции тайм-аута монтирования CSI

Флаг функции, который контролировал количество попыток монтирования драйвера CSI перед остановкой (`feature.dynatrace.com/max-csi-mount-attempts: 5`), заменён флагом функции на основе тайм-аута. Это было сделано из-за сложности определения, сколько попыток соответствует заданному тайм-ауту.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # заменяет feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Устаревшие поля

#### `autoUpdate` для OneAgent

Поле `spec.oneAgent.<mode>.autoUpdate: true/false` [объявлено устаревшим](../../deployment-and-configuration/updates-and-maintenance/auto-update-components.md "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") в `v1beta5` и не должно использоваться.

Рекомендуем следующее:

* Если вы хотите `autoUpdate: true`, не задавайте `image`, `codeModulesImage` или `version`.

  ```
  apiVersion: dynatrace.com/v1beta5


  kind: DynaKube


  metadata:


  name: example


  namespace: dynatrace


  spec:


  oneAgent:


  cloudNativeFullstack: {} # аналогично autoUpdate: true


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


  image: ... # аналогичный эффект как autoUpdate: false


  codeModulesImage: # аналогичный эффект как autoUpdate: false


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

Теперь драйвер CSI используется, когда он установлен в составе установки Dynatrace Operator.
