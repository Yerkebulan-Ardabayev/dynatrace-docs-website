---
title: Обновление или удаление Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator
---

# Обновление или удаление Dynatrace Operator

# Обновление или удаление Dynatrace Operator

* 12 мин чтения
* Обновлено 05 мая 2026 г.

На странице приведены подробные инструкции по обновлению и удалению Dynatrace Operator в средах Kubernetes и OpenShift.

Dynatrace Operator управляет развёртыванием и жизненным циклом всех компонентов Dynatrace в кластерах Kubernetes (например, OneAgent, ActiveGate и code modules). Сам Dynatrace Operator нужно обновлять, применяя новые манифесты или используя чарты Helm.

Рекомендуется использовать актуальную версию Dynatrace Operator (не ниже n-2) и всегда применять последний патч-релиз (например, 1.7.3 вместо 1.7.0).

## Обновление Dynatrace Operator

Чтобы обновить Dynatrace Operator, выберите **один из следующих вариантов** в зависимости от подхода к развёртыванию:

[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Manifest

Для `classicFullStack`, `applicationMonitoring` или `hostMonitoring` без CSI driver выполните следующую команду.

Kubernetes

OpenShift

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes.yaml
```

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift.yaml
```

Начиная с Dynatrace Operator версии 1.4.0, файл `kubernetes-csi.yaml` включает все компоненты Dynatrace Operator. Подробнее см. в [примечаниях к выпуску Dynatrace Operator версии 1.4.0](/managed/whats-new/dynatrace-operator/dto-fix-1-4-0#upgrade-from-dynatrace-operator-version-1-3-0 "Release notes for Dynatrace Operator, version 1.4.0").

Если используется CSI driver, вместо этого выполните:

Kubernetes

OpenShift

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes-csi.yaml
```

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift-csi.yaml
```

### Helm

1. Обновите чарт Helm.

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --reset-then-reuse-values \



   --atomic \



   -f values.yaml
   ```

   Файл `values.yaml` в новых версиях мог измениться. Если существующие значения больше не действительны, они будут молча проигнорированы, поскольку валидация для этого не предусмотрена.

   Команда `helm repo` не поддерживает OCI-реестры. С OCI можно использовать только команды `helm pull`, `helm show`, `helm install` и `helm upgrade`.

   Обновление из репозитория Helm

   Чтобы обновиться до последнего релиза из репозитория Helm, выполните следующую команду.

   ```
   helm upgrade dynatrace-operator dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --reset-then-reuse-values \



   --atomic \



   -f values.yaml
   ```

   Миграция из устаревшего репозитория Helm

   Репозиторий `dynatrace/helm-charts` устарел. Если он ещё используется, обновите его перед следующим апгрейдом.

   Удалите старый репозиторий и добавьте актуальный:

   ```
   helm repo remove dynatrace



   helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
   ```

   Перейдите на использование OCI-реестра:

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --version <version> \



   --namespace dynatrace \



   --reset-then-reuse-values \



   --install
   ```

   Управление CRD вручную

   По умолчанию чарт Helm управляет custom resource definition (CRD) автоматически (`installCRD: true` в `values.yaml`). Если задано `installCRD: false`, нужно обновить CRD вручную перед запуском `helm upgrade`.

   Команды для последней версии:

   Kubernetes

   OpenShift

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/dynatrace-operator-crd.yaml
   ```

## Обновление подов ActiveGate

Как правило, поды ActiveGate обновляются автоматически при перезапуске, если доступна новая версия (если только в образе не указана конкретная версия). Если требуется перезапустить поды ActiveGate вручную, выполните команду ниже.

Kubernetes

OpenShift

```
kubectl -n dynatrace rollout restart statefulset/<ACTIVEGATE-STATEFULSET-NAME>
```

```
oc -n dynatrace rollout restart statefulset/<ACTIVEGATE-STATEFULSET-NAME>
```

## Обновление токенов доступа

Чтобы обновить токены доступа Dynatrace, выполните следующие шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Найти текущие токены**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#find-token "Пути обновления, процедуры апгрейда и руководство по удалению Dynatrace Operator.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Удалить секрет**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-old-secret "Пути обновления, процедуры апгрейда и руководство по удалению Dynatrace Operator.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создать новые токены**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-token "Пути обновления, процедуры апгрейда и руководство по удалению Dynatrace Operator.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Создать новый секрет с обновлёнными токенами**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-secret "Пути обновления, процедуры апгрейда и руководство по удалению Dynatrace Operator.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Удалить старые токены**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-token "Пути обновления, процедуры апгрейда и руководство по удалению Dynatrace Operator.")

### Шаг 1. Найти текущие токены доступа

Найдите и сохраните текущие токены.

После создания новых токенов нужно [удалить старые](#delete-token).

Kubernetes

OpenShift

```
kubectl -n dynatrace get secrets <dynakube-name> -o yaml | yq '.data.apiToken' | base64 -d
```

```
oc -n dynatrace get secrets <dynakube-name> -o yaml | yq '.data.apiToken' | base64 -d
```

### Шаг 2. Удалить секрет

Чтобы удалить секрет, выполните одну из команд ниже.

В Kubernetes используемые токены хранятся по умолчанию в секрете с именем `dynakube`. Если custom resource DynaKube имеет другое имя или в DynaKube задано поле `tokens`, убедитесь, что новый секрет имеет то же имя, что указано там.

Kubernetes

OpenShift

```
kubectl -n dynatrace delete secret dynakube
```

```
oc -n dynatrace delete secret dynakube
```

### Шаг 3. Создать новые токены доступа

Инструкции по созданию токенов см. в разделе [Access tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

### Шаг 4. Создать новый секрет с обновлёнными токенами доступа

Чтобы создать новый секрет с обновлёнными токенами, выполните одну из команд ниже, заменив плейсхолдеры на новые токены.

Kubernetes

OpenShift

* Для токена Dynatrace Operator:

  ```
  kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
  ```
* Для токенов Dynatrace Operator и Data Ingest:

  ```
  kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA-INGEST-TOKEN>"
  ```

* Для токена Dynatrace Operator:

  ```
  oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
  ```
* Для токенов Dynatrace Operator и Data Ingest:

  ```
  oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA-INGEST-TOKEN>"
  ```

Dynatrace Operator применяет обновлённые секреты примерно через пять минут. Удаление DynaKube и его повторное применение принудительно запускает немедленную reconciliation.

### Шаг 5. Удалить старый токен доступа

После того как новые токены активированы, удалите старые.

1. В Dynatrace перейдите в **Access Tokens** и найдите [старый токен](#find-token).
2. Нажмите **Delete**.

## Удаление Dynatrace Operator

Следующее руководство описывает рекомендуемые шаги для чистого удаления Dynatrace Operator.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Удалить компоненты, управляемые Dynatrace Operator**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator-components "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

Опционально **Перезапустить отслеживаемые приложения**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#restart-apps "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Удалить Dynatrace Operator**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

Опционально **Очистить узлы**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")

**Важно для пользователей CRI-O Runtime с classicFullStack**

OneAgent версия 1.279 и ниже

Если в качестве container runtime кластера используется CRI-O вместе с `classicFullStack`, выполните шаги из раздела [Migrate from classic full-stack to cloud-native full-stack mode](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") в рамках процесса удаления.

### Step 1 Удалить компоненты, управляемые Dynatrace Operator

Удалите custom resources DynaKube, чтобы Dynatrace Operator полностью удалил все связанные компоненты из кластера Kubernetes. Дождитесь удаления этих компонентов, чтобы убедиться в успешном завершении очистки.

Kubernetes

OpenShift

```
kubectl delete dynakube -n dynatrace --all



kubectl delete edgeconnect -n dynatrace --all



kubectl -n dynatrace wait pod --for=delete -l app.kubernetes.io/managed-by=dynatrace-operator --timeout=300s



kubectl -n dynatrace wait edgeconnect --for=delete --all --timeout=300s
```

```
oc delete dynakube -n dynatrace --all



oc delete edgeconnect -n dynatrace --all



oc -n dynatrace wait pod --for=delete -l app.kubernetes.io/managed-by=dynatrace-operator --timeout=300s



oc -n dynatrace wait edgeconnect --for=delete --all --timeout=300s
```

Почему требуется дополнительная очистка?

Большинство ресурсов, связанных с DynaKube, удаляются автоматически через систему владения Kubernetes: при удалении DynaKube Kubernetes автоматически удаляет все ресурсы, у которых есть `OwnerReference`, указывающий на этот DynaKube.

Однако некоторые ресурсы требуют дополнительных шагов очистки из-за ограничений Kubernetes:

* **Зависимости CSI driver**: приложения, использующие CSI driver, должны завершить работу до того, как CSI driver можно будет безопасно удалить. Это предотвращает возможное повреждение данных или проблемы с монтированием.
* **Ресурсы в других namespace**: `OwnerReferences` в Kubernetes работают только в пределах одного namespace. Поскольку Dynatrace Operator создаёт ресурсы, например `Secrets`, в namespace приложений, их нужно удалять отдельно.

### Step 2 optional Опционально **Если использовался CSI driver**: перезапустить отслеживаемые приложения

Чтобы перед продолжением удаления CSI volumes были корректно размонтированы и отключены от CSI driver, используйте следующую команду для определения приложений, которые используют CSI driver и нуждаются в перезапуске.

В результате будет выведен список подов в формате `namespace pod` для каждого приложения, использующего CSI driver.

Kubernetes

OpenShift

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

```
oc get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

### Step 3 Удалить Dynatrace Operator

После того как все компоненты, управляемые Dynatrace Operator, успешно удалены, можно безопасно деинсталлировать Dynatrace Operator.

1. Удалите Dynatrace Operator.

   Helm

   Kubernetes

   Openshift

   ```
   helm uninstall dynatrace-operator -n dynatrace
   ```

   * Если CSI driver **не** был установлен (при установке использовался `kubernetes.yaml`):

     ```
     kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes.yaml
     ```
   * Если CSI driver **был** установлен (при установке использовался `kubernetes-csi.yaml`):

     ```
     kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/kubernetes-csi.yaml
     ```

   * Если CSI driver **не** был установлен (при установке использовался `openshift.yaml`):

     ```
     oc delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift.yaml
     ```
   * Если CSI driver **был** установлен (при установке использовался `openshift-csi.yaml`):

     ```
     oc delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.10.1/openshift-csi.yaml
     ```
2. Удалите namespace.

   Kubernetes

   OpenShift

   ```
   kubectl delete namespace dynatrace
   ```

   ```
   oc delete namespace dynatrace
   ```

### Step 4 optional Очистить узлы

В зависимости от режима мониторинга данные OneAgent и CSI driver могут остаться на узле. Для обеспечения чистого состояния используйте скрипт очистки для удаления ненужных данных.

Скрипт разворачивает DaemonSet, который выполняет процедуру очистки на всех Linux-узлах кластера (amd64, arm64, ppc64le, s390x).

Перед запуском очистки узлов убедитесь, что ни один DynaKube не развёрнут и все отслеживаемые поды перезапущены.

1. Загрузите скрипт.

```
curl -O https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/refs/tags/v1.10.1/hack/cluster/cleanup-node-fs.sh
```

2. Сделайте скрипт исполняемым.

```
chmod +x cleanup-node-fs.sh
```

3. Запустите скрипт.

```
./cleanup-node-fs.sh
```

По умолчанию скрипт использует namespace `dynatrace`. Чтобы указать другой namespace, передайте его как аргумент:

```
./cleanup-node-fs.sh <namespace>
```

Скрипт выполняет следующие действия:

* Запускает скрипт удаления OneAgent, если он присутствует.
* Удаляет директории OneAgent (`/var/lib/dynatrace`, `/opt/dynatrace`, `/var/log/dynatrace`).
* Удаляет директорию данных CSI driver.
* Сообщает о статусе очистки для каждого узла.

После успешного завершения работы всех подов очистки DaemonSet удаляется автоматически. Если какая-либо очистка завершится неудачно, DaemonSet остаётся для расследования.

## Обновление со старых версий

Если в кластере **когда-либо использовалась версия Dynatrace Operator старше 1.4**, независимо от текущей версии, необходимо сначала обновиться до версии **1.7.3**, и только потом переходить к последнему релизу. Начиная с версии 1.7.3, Operator автоматически выполняет необходимую конвертацию DynaKube и очистку CRD.

Чтобы узнать, затронута ли ваша установка и возможен ли прыжок версий, см. [Check your current versions](#check-versions).

### Check your current versions

Проверьте текущую версию Dynatrace Operator.

Helm

kubectl

```
helm list -n dynatrace -o json | jq -r '.[].app_version'
```

```
kubectl get deployment dynatrace-operator -n dynatrace \



-o jsonpath='{.metadata.labels.app\.kubernetes\.io/version}'
```

Проверьте текущую версию API DynaKube:

```
kubectl get dynakubes -n dynatrace -o custom-columns='NAME:.metadata.name,API VERSION:.apiVersion'
```

Проверьте, какие версии API когда-либо использовались для хранения DynaKubes в этом кластере:

```
kubectl get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Каждая версия API, указанная в `.status.storedVersions`, должна по-прежнему поддерживаться той версией Dynatrace Operator, до которой выполняется обновление. Если какая-либо запись больше не обслуживается, нужно сначала обновиться до промежуточной версии Operator, которая её ещё поддерживает, чтобы хранимые ресурсы были конвертированы и устаревшая запись удалена.

`v1beta1` и `v1beta2` являются особым исключением: если в выводе присутствует любая из них, конвертировать эти ресурсы и удалить записи способен **только Dynatrace Operator 1.7.3**. Никакая другая версия это не исправит, см. [Upgrade steps](#upgrade-steps).

### Обзор версий API для DynaKube

| Версия API DynaKube | Введена | Устарела | Не обслуживается [1](#fn-1-1-def) | Удалена | Руководства по миграции |
| --- | --- | --- | --- | --- | --- |
| v1beta6 | 1.8.0 |  |  |  |  |
| v1beta5 | 1.6.0 | 1.10.0 |  |  | [в v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6 "Migrate your v1beta5 DynaKube CR to the v1beta6 apiVersions.") |
| v1beta4 | 1.5.0 | 1.9.0 | 1.10.0 |  | [в v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6 "Migrate your v1beta4 DynaKube CR to the v1beta6 apiVersions."), [в v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Migrate your v1beta4 DynaKube CR to the v1beta5 apiVersions.") |
| v1beta3 | 1.4.0 | 1.7.0 | 1.8.0 | 1.9.0 | [в v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Migrate your v1beta3 DynaKube CR to the v1beta5 apiVersions."), [в v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Migrate your v1beta3 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | 1.8.0 | [в v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Migrate your v1beta2 DynaKube CR to the v1beta5 apiVersions."), [в v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Migrate your v1beta2 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | 1.8.0 | [в v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Migrate your v1beta1 DynaKube CR to the v1beta5 apiVersions."), [в v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Migrate your v1beta1 DynaKube CR to the v1beta4 apiVersions.") |

1

Указанная версия Dynatrace Operator больше не обслуживает эту версию API. С её помощью нельзя применять новые ресурсы. Схема сохраняется в CRD только для автоматического преобразования и будет удалена в одном из последующих релизов. Подробнее см. [Процесс удаления](#deprecation).

### Шаги обновления

Версии Dynatrace Operator **старше 1.4** хранили DynaKube как `v1beta1` или `v1beta2`. Эти версии API удалены в 1.8.0, и **1.7.3, это последний и единственный релиз, способный их мигрировать**.

Важна история кластера, а не текущая версия: если DynaKube *когда-либо* хранился как `v1beta1` или `v1beta2` (в любой точке пути обновления), нужно пройти через 1.7.3 перед переходом на 1.8.0 или более позднюю версию, даже если Operator с тех пор обновлялся несколько раз. Пропуск этого шага блокирует обновление и оператора, и CRD.

Убедиться в этом можно, проверив `.status.storedVersions` у CRD, см. [Проверка текущих версий](#check-versions).

1. **Обновление до версии 1.7.3**

   Этот шаг автоматически преобразует DynaKube в поддерживаемую версию API.

   Helm

   Manifest

   Не использовать `--reuse-values` при обновлении между major-версиями Dynatrace Operator. Новые версии chart вводят поля, для которых нет значений по умолчанию в старых values-файлах, что вызывает ошибки nil pointer при шаблонизации. Передавать только нужные значения явно через `--set` или `-f values.yaml`.

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --version 1.7.3 \



   --namespace dynatrace
   ```

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.7.3/kubernetes-csi.yaml
   ```

   Дождаться перезапуска пода Operator и дать примерно 10 минут на успешную сверку (reconciliation).
2. **Обновление до последней версии**

   Для обновления нужно следовать инструкции [Обновление Dynatrace Operator](#update).

   Обновление автоматически удаляет устаревшие записи CRD и мигрирует DynaKube на текущую версию API (`v1beta6`).

   При установке через манифесты нужно предоставить правильные права RBAC для задания очистки, см. [Безопасность и RBAC Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/security#upgrade-support "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require").
3. **Проверка обновления**

   Проверить, что Dynatrace Operator работает исправно, DynaKube на `v1beta6`, а `.status.storedVersions` чистый:

   ```
   kubectl get pods -n dynatrace



   kubectl get dynakubes -n dynatrace -o custom-columns='NAME:.metadata.name,API VERSION:.apiVersion'



   kubectl get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
   ```

   Ожидаемый результат: `dynatrace.com/v1beta6` и `["v1beta6"]`. Нужно обновить сохранённые манифесты, отразив в них новый `apiVersion`, чтобы они оставались источником истины.

   Проверить наличие предупреждающих событий об устаревших версиях CRD:

   ```
   kubectl get events -n dynatrace --field-selector reason=Warning
   ```

### Что происходит при обновлении до 1.7.3

При выполнении шагов выше Dynatrace Operator автоматически решает две задачи:

* **Преобразование пользовательского ресурса DynaKube** в поддерживаемую версию API. Operator автоматически преобразует DynaKube только пока исходная версия ещё обслуживается CRD. После удаления версии преобразование становится невозможным, именно поэтому версия 1.7.3 обязательна для ресурсов на `v1beta1` или `v1beta2`.
* **Очистка `.status.storedVersions`** у CRD. Kubernetes отслеживает каждую версию API, которая когда-либо использовалась для хранения данных. Записи, которые остаются в списке, но больше не существуют в схеме, блокируют любое дальнейшее обновление CRD. Начиная с 1.7.3, Dynatrace Operator автоматически удаляет устаревшие записи, либо через pre-upgrade hook Helm (для установок на основе Helm), либо через init-контейнер Operator (для установок на основе манифестов). Поскольку эта логика очистки появилась в 1.7.3 и отсутствует в более ранних релизах, **1.7.3 обязательна как точка входа** для кластеров, у которых в `storedVersions` всё ещё числятся `v1beta1` или `v1beta2`.