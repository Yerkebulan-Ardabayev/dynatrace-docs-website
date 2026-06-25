---
title: Обновление или удаление Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator
scraped: 2026-05-12T12:03:28.374389
---

# Обновление или удаление Dynatrace Operator

# Обновление или удаление Dynatrace Operator

* Чтение: 9 мин
* Обновлено 02 января 2026 г.

На этой странице приведены подробные инструкции по обновлению или удалению Dynatrace Operator в окружениях Kubernetes и OpenShift.

Dynatrace Operator управляет развёртыванием и жизненным циклом всех компонентов Dynatrace в ваших кластерах Kubernetes (например, OneAgent, ActiveGate и модулей кода). В зависимости от конфигурации это включает автоматические обновления этих компонентов. Сам Dynatrace Operator необходимо обновлять либо применением новых манифестов, либо с помощью helm chart.

Рекомендуется использовать актуальную версию Operator (не ниже версии n-2) и всегда использовать последнюю патч-версию этой версии Operator (например, 0.10.4 вместо 0.10.0).

## Обновление Dynatrace Operator

Чтобы обновить Dynatrace Operator, выберите **один из следующих вариантов** в зависимости от вашего подхода к развёртыванию:

[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Manifest

Для `classicFullStack`, `applicationMonitoring` или `hostMonitoring` без CSI driver выполните следующую команду.

Kubernetes

OpenShift

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
```

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
```

Начиная с версии Dynatrace Operator 1.4.0, `kubernetes-csi.yaml` включает все компоненты Dynatrace Operator. Подробнее см. [примечания к выпуску Dynatrace Operator версии 1.4.0](/managed/whats-new/dynatrace-operator/dto-fix-1-4-0#upgrade-from-dynatrace-operator-version-1-3-0 "Примечания к выпуску Dynatrace Operator, версия 1.4.0").

Если вы используете CSI driver, используйте вместо этого следующую команду:

Kubernetes

OpenShift

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
```

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
```

### Helm

1. Обновите Helm chart.

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Файл `values.yaml` мог измениться в более новых версиях. Если существующие значения больше не действительны, они будут молча проигнорированы, так как проверка для этого отсутствует.

   Обновление из реестра OCI

   Чтобы обновиться до последнего выпуска из реестра OCI, выполните следующую команду.

   ```
   helm upgrade dynatrace-operator dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Обратите внимание, что команда `helm repo` не поддерживает реестры OCI. С OCI можно использовать только команды `helm pull`, `helm show`, `helm install` и `helm upgrade`.

   Обновление с версии Dynatrace Operator < 0.8.0

   ### Обновление со старых версий Dynatrace Operator с помощью Helm

   Если вы используете версию Dynatrace Operator ранее v0.8.0 в развёртывании Helm, выполните приведённые ниже шаги для перехода на последнюю версию Dynatrace Operator с помощью Helm.

   #### Шаг 1 Обновите определение пользовательского ресурса

   В соответствии с вашей [конфигурацией файла `values.yaml`](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml) выберите один из вариантов ниже.

   * Если для `installCRD` задано значение `true`, определение пользовательского ресурса будет автоматически обновлено и управляться Helm.
   * Если для `installCRD` задано значение `false`, необходимо обновить определение пользовательского ресурса вручную перед запуском установки Helm:

     Kubernetes

     OpenShift

     ```
     kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
     ```

     ```
     oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
     ```

   #### Шаг 2 Обновите Helm chart

   Удалите раздел CRD и секреты из существующего файла values.yaml либо используйте и настройте [пример `values.yaml` из GitHub](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml). Обновите helm chart:

   ```
   helm upgrade dynatrace-operator dynatrace/dynatrace-operator -f values.yaml --atomic -n dynatrace
   ```

   Указанные выше изменения делают ваши старые значения непригодными, поэтому задать флаг `--reuse-values` для миграции невозможно.

   На некоторых версиях Dynatrace Operator неудачное обновление может нарушить откат Helm, что приводит к нерабочей установке. Это связано с хранимыми DynaKube `apiVersions`. Подробнее см. [Обновление или удаление Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "Процедуры обновления и удаления Dynatrace Operator").

   ```
   Error: UPGRADE FAILED: release dynatrace-operator failed, and has been rolled back due to atomic being set: cannot patch "dynakubes.dynatrace.com" with kind CustomResourceDefinition: CustomResourceDefinition.apiextensions.k8s.io "dynakubes.dynatrace.com" is invalid: status.storedVersions[1]: Invalid value: "v1beta5": missing from spec.versions; v1beta5 was previously a storage version, and must remain in spec.versions until a storage migration ensures no data remains persisted in v1beta5 and removes v1beta5 from status.storedVersions
   ```

   Если возникает эта ошибка

   1. [Удалите Dynatrace Operator](#uninstall-dynatrace-operator).
   2. Удалите определение пользовательского ресурса DynaKube.

      ```
      kubectl delete crd dynakubes.dynatrace.com
      ```
   3. [Установите нужную версию Dynatrace Operator](#update).
   4. При необходимости перезапустите рабочие нагрузки приложений.

## Обновление подов ActiveGate

Обычно поды ActiveGate обновляются автоматически при перезапуске пода, когда доступна новая версия (если только образ уже не задаёт определённую версию). Однако если вам нужно вручную перезапустить поды ActiveGate, выполните приведённую ниже команду.

Kubernetes

OpenShift

```
kubectl -n dynatrace rollout restart statefulset/<ACTIVEGATE-STATEFULSET-NAME>
```

```
oc -n dynatrace rollout restart statefulset/<ACTIVEGATE-STATEFULSET-NAME>
```

## Обновление токенов доступа

Если вам нужно обновить токены доступа Dynatrace, выполните приведённые ниже шаги.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Найдите текущие токены**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#find-token "Процедуры обновления и удаления Dynatrace Operator")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Удалите ваш секрет**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-old-secret "Процедуры обновления и удаления Dynatrace Operator")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Создайте новые токены**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-token "Процедуры обновления и удаления Dynatrace Operator")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Создайте новый секрет с обновлёнными токенами**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-secret "Процедуры обновления и удаления Dynatrace Operator")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Удалите старые токены**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-token "Процедуры обновления и удаления Dynatrace Operator")

### Шаг 1 Найдите текущие токены доступа

Найдите и сохраните используемые в настоящее время токены.

После генерации новых токенов вам нужно будет [удалить старые](#delete-token).

Kubernetes

OpenShift

```
kubectl -n dynatrace get secrets <dynakube-name> -o yaml | yq '.data.apiToken' | base64 -d
```

```
oc -n dynatrace get secrets <dynakube-name> -o yaml | yq '.data.apiToken' | base64 -d
```

### Шаг 2 Удалите ваш секрет

Чтобы удалить секрет, выполните одну из приведённых ниже команд.

В Kubernetes используемые токены по умолчанию хранятся в секрете с именем `dynakube`. Если пользовательский ресурс DynaKube имеет другое имя или задано поле `tokens` в DynaKube, убедитесь, что новый секрет имеет то же имя, что определено там.

Kubernetes

OpenShift

```
kubectl -n dynatrace delete secret dynakube
```

```
oc -n dynatrace delete secret dynakube
```

### Шаг 3 Создайте новые токены доступа

Инструкции по созданию токенов см. в разделе [Токены доступа и разрешения](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes").

### Шаг 4 Создайте новый секрет с обновлёнными токенами доступа

Чтобы создать новый секрет с обновлёнными токенами, выполните одну из приведённых ниже команд, обязательно заменив подстановочные значения новыми токенами.

Kubernetes

OpenShift

* Для токена Dynatrace Operator:

  ```
  kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
  ```
* Для токена Dynatrace Operator и Data Ingest:

  ```
  kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA-INGEST-TOKEN>"
  ```

* Для токена Dynatrace Operator:

  ```
  oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
  ```
* Для токена Dynatrace Operator и Data Ingest:

  ```
  oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA-INGEST-TOKEN>"
  ```

Dynatrace Operator подхватывает обновлённые секреты примерно за пять минут. Удаление DynaKube и его повторное применение принудительно запускает мгновенную сверку.

### Шаг 5 Удалите старый токен доступа

После того как новые токены установлены, удалите старые.

1. В Dynatrace перейдите в **Access Tokens** и найдите [старый токен](#find-token).
2. Выберите **Delete**.

## Удаление Dynatrace Operator

В следующем руководстве описаны рекомендуемые шаги для чистого удаления Dynatrace Operator.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Удалите компоненты, управляемые Dynatrace Operator**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator-components "Процедуры обновления и удаления Dynatrace Operator")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

Необязательно **Перезапустите отслеживаемые приложения**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#restart-apps "Процедуры обновления и удаления Dynatrace Operator")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Удалите Dynatrace Operator**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator "Процедуры обновления и удаления Dynatrace Operator")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

Необязательно **Очистите узлы**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Процедуры обновления и удаления Dynatrace Operator")

**Важно для пользователей среды выполнения CRI-O с classicFullStack**

OneAgent версии 1.279 и ниже

Если вы используете CRI-O в качестве среды выполнения контейнеров вашего кластера с `classicFullStack`, выполните шаги, описанные в разделе [Миграция из режима classic full-stack в режим cloud-native full-stack](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Перенесите ваше развёртывание Dynatrace из режима classic full-stack в режим cloud-native full-stack.") в рамках процесса удаления.

### Шаг 1 Удалите компоненты, управляемые Dynatrace Operator

Удалите пользовательские ресурсы DynaKube, чтобы позволить Dynatrace Operator полностью удалить все связанные компоненты, управляемые Dynatrace Operator, из вашего кластера Kubernetes. Дождитесь удаления этих компонентов, чтобы убедиться, что очистка завершена успешно.

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

Зачем нужна дополнительная очистка?

Большинство ресурсов, связанных с DynaKube, очищаются автоматически через систему владения Kubernetes: когда вы удаляете DynaKube, Kubernetes автоматически удаляет все ресурсы, имеющие `OwnerReference`, указывающую на этот DynaKube.

Однако некоторые ресурсы требуют дополнительных шагов очистки из-за ограничений Kubernetes:

* **Зависимости CSI driver**: приложения, использующие CSI driver, должны быть остановлены, прежде чем CSI driver можно будет безопасно удалить. Это предотвращает возможное повреждение данных или проблемы с монтированием.
* **Межпространственные ресурсы**: `OwnerReferences` в Kubernetes работают только в пределах одного пространства имён. Поскольку Dynatrace Operator создаёт ресурсы, такие как `Secrets`, в пространствах имён ваших приложений, он должен очищать их отдельно.

### Шаг 2 необязательно Необязательно **Если вы использовали CSI driver**: перезапустите отслеживаемые приложения

Чтобы убедиться, что тома CSI правильно отмонтированы и отключены от CSI driver перед продолжением удаления, используйте следующую команду для определения приложений, которые используют CSI driver и требуют перезапуска.

Вывод покажет список подов в формате `namespace pod` для каждого приложения, которое использует CSI driver.

Kubernetes

OpenShift

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

```
oc get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

### Шаг 3 Удалите Dynatrace Operator

После того как все компоненты, управляемые Dynatrace Operator, успешно удалены, можно безопасно удалить Dynatrace Operator.

1. Удалите Dynatrace Operator.

   Helm

   Kubernetes

   Openshift

   ```
   helm uninstall dynatrace-operator -n dynatrace
   ```

   * Если CSI driver **не** был установлен (вы использовали `kubernetes.yaml` при установке):

     ```
     kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
     ```
   * Если CSI driver **был** установлен (вы использовали `kubernetes-csi.yaml` при установке):

     ```
     kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
     ```

   * Если CSI driver **не** был установлен (вы использовали `openshift.yaml` при установке):

     ```
     oc delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
     ```
   * Если CSI driver **был** установлен (вы использовали `openshift-csi.yaml` при установке):

     ```
     oc delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
     ```
2. Удалите пространство имён.

   Kubernetes

   OpenShift

   ```
   kubectl delete namespace dynatrace
   ```

   ```
   oc delete namespace dynatrace
   ```

### Шаг 4 необязательно Очистите узлы

В зависимости от режима мониторинга данные OneAgent и CSI driver могут оставаться на узле. Чтобы обеспечить чистое состояние, используйте скрипт очистки для удаления ненужных данных.

Скрипт развёртывает DaemonSet, который выполняет процедуру очистки на всех узлах Linux в кластере (amd64, arm64, ppc64le, s390x).

Перед запуском очистки узлов убедитесь, что ни один DynaKube не развёрнут и все отслеживаемые поды перезапущены.

1. Загрузите скрипт.

```
curl -O https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/refs/tags/v1.9.0/hack/cluster/cleanup-node-fs.sh
```

2. Сделайте скрипт исполняемым.

```
chmod +x cleanup-node-fs.sh
```

3. Запустите скрипт.

```
./cleanup-node-fs.sh
```

По умолчанию скрипт использует пространство имён `dynatrace`. Чтобы указать другое пространство имён, передайте его в качестве аргумента:

```
./cleanup-node-fs.sh <namespace>
```

Скрипт выполняет следующие действия:

* Выполняет скрипт удаления OneAgent, если он присутствует.
* Удаляет каталоги OneAgent (`/var/lib/dynatrace`, `/opt/dynatrace`, `/var/log/dynatrace`).
* Удаляет каталог данных CSI driver.
* Сообщает о статусе очистки для каждого узла.

После успешного завершения всех подов очистки DaemonSet удаляется автоматически. Если какая-либо очистка завершается неудачей, DaemonSet остаётся для исследования.