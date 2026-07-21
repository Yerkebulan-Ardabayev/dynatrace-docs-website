---
title: Образ контейнера ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/activegate-in-container
---

# Образ контейнера ActiveGate

# Образ контейнера ActiveGate

* Чтение: 2 мин
* Обновлено 09 мая 2025

Dynatrace поддерживает запуск ActiveGate в контейнере. В качестве примера развёртывания на основе контейнеров эта страница описывает, как развернуть контейнерный ActiveGate с помощью StatefulSet на Kubernetes/OpenShift.

## Предварительные требования

1. [Создать токен доступа со скоупом `InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.")
2. [Создать токен аутентификации](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.")
3. Определить конечные точки связи ActiveGate и аутентификацию. Использовать API [GET connectivity information for ActiveGate](/managed/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.").
4. Получить UUID пространства имён kube-system
   Как извлечь UUID пространства имён kube-system

   Выполнить команду ниже и сохранить UUID из вывода для дальнейшего использования.

   Kubernetes

   OpenShift

   ```
   kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

   ```
   oc get namespace kube-system -o jsonpath='{.metadata.uid}'
   ```

## Системные требования

Образ ActiveGate Dynatrace поддерживается на различных версиях Kubernetes и OpenShift. Полный список см. в [Technology support - Kubernetes](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

Образы доступны для следующих архитектур:

* x86-64
* ARM64 (AArch64)
* s390x
* PPC64le

## Реестры контейнеров

Чтобы обеспечить бесшовную интеграцию с инструментарием и адаптируемость под потребности, образы контейнеров предлагаются несколькими способами для максимальной гибкости:

* [Встроенный реестр Dynatrace](/managed/ingest-from/setup-on-k8s/guides/container-registries#default "Manage container registries with Dynatrace") по умолчанию
* [Публичные реестры](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* [Использование собственного приватного реестра](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries") рекомендуется

Обратите внимание, что мультиархитектурные образы контейнеров Dynatrace, обеспечивающие совместимость с различными платформами, доступны [только из публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). Встроенный реестр Dynatrace предоставляет только образы x86-64.

## Развёртывание


Dynatrace предоставляет подписанные образы контейнеров для обеспечения подлинности и целостности, а также SBOM, в которых перечислены все включённые программные компоненты.
Проверка подписей и просмотр SBOM позволяет эффективно управлять уязвимостями и снижать риски.
Подробнее о проверке см. [Verify Software Bill of Materials (SBOM) Attestation](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature#sbom-attestation-verification "Verify Dynatrace image signatures").


Частный или публичный реестр


Встроенный реестр Dynatrace


1. Создать выделенное пространство имён.


   Kubernetes


   OpenShift


   ```
   kubectl create namespace dynatrace
   ```


   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Создать секрет, содержащий данные аутентификации на сервере Dynatrace, который использует ActiveGate.


   Kubernetes


   OpenShift


   ```
   kubectl -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```


   ```
   oc -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```


   Нужно заменить


   * `<YOUR_TENANT_TOKEN>` на значение `tenantToken`, полученное в разделе [Prerequisites](#prereq) из информации о подключении.
   * `<YOUR_AUTH_TOKEN>` на отдельный токен ActiveGate, полученный в разделе [Prerequisites](#prereq).
3. Создать файл `ag-deployment-example.yaml` со следующим содержимым:


   ag-deployment-example.yaml


   ```
   apiVersion: v1



   kind: Service



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   spec:



   type: ClusterIP



   selector:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   ports:



   - protocol: TCP



   port: 443



   targetPort: ag-https



   ---



   apiVersion: apps/v1



   kind: StatefulSet



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   podManagementPolicy: Parallel



   serviceName: ""



   selector:



   matchLabels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   template:



   metadata:



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   affinity:



   nodeAffinity:



   requiredDuringSchedulingIgnoredDuringExecution:



   nodeSelectorTerms:



   - matchExpressions:



   - key: kubernetes.io/arch



   operator: In



   values:



   - <CPU_ARCHITECTURE>



   - key: kubernetes.io/os



   operator: In



   values:



   - linux



   containers:



   - name: activegate



   image: <REPOSITORY_URL>/dynatrace-activegate:<IMAGE_TAG>



   imagePullPolicy: Always



   ports:



   - containerPort: 9999



   name: ag-https



   protocol: TCP



   env:



   - name: DT_TENANT



   value: <YOUR_ENVIRONMENT_ID>



   - name: DT_SERVER



   value: <YOUR_COMMUNICATION_ENDPOINTS>



   - name: DT_ID_SEED_NAMESPACE



   value: dynatrace



   - name: DT_ID_SEED_K8S_CLUSTER_ID



   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>



   - name: DT_CAPABILITIES



   value: restInterface,kubernetes_monitoring,MSGrouter,metrics_ingest



   - name: DT_DEPLOYMENT_METADATA



   value: orchestration_tech=handcrated-ag-sts;script_version=none;orchestrator_id=none



   - name: DT_DNS_ENTRY_POINT



   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication



   volumeMounts:



   - name: dynatrace-tokens



   mountPath: /var/lib/dynatrace/secrets/tokens



   - name: truststore-volume



   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts



   readOnly: true



   subPath: k8s-local.jks



   - name: server-certs-storage



   mountPath: /var/lib/dynatrace/gateway/ssl



   - name: ag-lib-gateway-config



   mountPath: /var/lib/dynatrace/gateway/config



   - name: ag-lib-gateway-temp



   mountPath: /var/lib/dynatrace/gateway/temp



   - name: ag-lib-gateway-data



   mountPath: /var/lib/dynatrace/gateway/data



   - name: ag-log-gateway



   mountPath: /var/log/dynatrace/gateway



   - name: ag-tmp-gateway



   mountPath: /var/tmp/dynatrace/gateway



   livenessProbe:



   failureThreshold: 2



   httpGet:



   path: /rest/state



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 30



   successThreshold: 1



   timeoutSeconds: 1



   readinessProbe:



   failureThreshold: 3



   httpGet:



   path: /rest/health



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 15



   successThreshold: 1



   timeoutSeconds: 1



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi



   securityContext:



   allowPrivilegeEscalation: false



   capabilities:



   drop:



   - all



   privileged: false



   readOnlyRootFilesystem: true



   runAsNonRoot: true



   seccompProfile:



   type: RuntimeDefault



   initContainers:



   - name: certificate-loader



   image: <REPOSITORY_URL>/dynatrace-activegate:<IMAGE_TAG>



   workingDir: /var/lib/dynatrace/gateway



   command: ['/bin/bash']



   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']



   volumeMounts:



   - mountPath: /var/lib/dynatrace/gateway/ssl



   name: truststore-volume



   volumes:



   - name: truststore-volume



   emptyDir: {}



   - name: dynatrace-tokens



   secret:



   secretName: dynatrace-tokens



   - name: server-certs-storage



   emptyDir: {}



   - name: ag-lib-gateway-config



   emptyDir: {}



   - name: ag-lib-gateway-temp



   emptyDir: {}



   - name: ag-lib-gateway-data



   emptyDir: {}



   - name: ag-log-gateway



   emptyDir: {}



   - name: ag-tmp-gateway



   emptyDir: {}



   updateStrategy:



   type: RollingUpdate
   ```
4. Изменить файл развёртывания YAML.


   Добавить в файл `ag-deployment-example.yaml` данные конфигурации окружения, обязательно заменив:


   * `CPU_ARCHITECTURE` на архитектуру процессора. Возможные значения: `amd64`, `arm64`, `s390x` и `ppcle64`
   * `<REPOSITORY_URL>` на один из [поддерживаемых реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
   * `<IMAGE_TAG>` на корректный тег образа ([примеры](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#image-tags "Store Dynatrace images in private registries"))
   * `<YOUR_ENVIRONMENT_ID>` на идентификатор своего окружения


     Чтобы определить идентификатор окружения, см. синтаксис ниже.


     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` на значение `communicationEndpoints`, полученное в разделе [Prerequisites](#prereq) из информации о подключении


     Список конечных точек связи с сервером (`communicationEndpoints`) со временем может меняться.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` на UUID пространства имён kube-system, полученный в разделе [Prerequisites](#prereq)


     Для архитектуры PPC64le требуется дополнительная настройка. Подробнее см. [образ контейнера ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Deploy a containerized ActiveGate.").


   Опции:


   * Опционально включить AppArmor, если он доступен.


     Профиль AppArmor


     Для сохранения совместимости с более широким набором кластеров Kubernetes профиль AppArmor не указан в `ag-deployment-example.yaml`. Если AppArmor доступен в кластере Kubernetes, рекомендуется дополнительно снабдить StatefulSet аннотацией с профилем `runtime/default`.


     ```
     spec:



     template:



     metadata:



     annotations:



     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Опционально применить лимиты ресурсов согласно рекомендациям по размеру.


     Рекомендации по размеру для K8S monitoring и agent routing


     В таблице ниже приведены рекомендуемые значения CPU и памяти для ActiveGate в зависимости от количества подов:


     | Количество подов | CPU | Память |
     | --- | --- | --- |
     | До 100 подов | 500 миллиядер (mCores) | 512 мебибайт (MiB) |
     | До 1000 подов | 1000 миллиядер (mCores) | 1 гибибайт (GiB) |
     | До 5000 подов | 1500 миллиядер (mCores) | 2 гибибайта (GiB) |
     | Более 5000 подов | более 1500 миллиядер (mCores)[1](#fn-1-1-def) | более 2 гибибайт (GiB)[1](#fn-1-1-def) |


     1


     Фактические значения зависят от конкретного окружения.


     Эти лимиты следует рассматривать как ориентир. Они предназначены для предотвращения замедления процесса запуска ActiveGate и чрезмерного использования ресурсов узла. Значения по умолчанию охватывают широкий диапазон размеров кластеров, их можно изменить в соответствии со своими потребностями на основе [метрик самомониторинга](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.") ActiveGate.


   Дополнительные варианты настройки см. в разделе [Настройка контейнеризованного ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").
5. Развернуть ActiveGate.


   Kubernetes


   OpenShift


   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

```
oc apply -f ./ag-deployment-example.yaml
```
6. Чтобы убедиться, что ActiveGate успешно подключился к серверу Dynatrace, перейти в **Deployment Status** > **ActiveGates**.


1. Создать выделенный namespace.


   Kubernetes


   OpenShift


   ```
   kubectl create namespace dynatrace
   ```


   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Создать секрет, который хранит URL окружения и данные аутентификации для этого реестра.


   Kubernetes


   OpenShift


   ```
   kubectl -n dynatrace create secret docker-registry dynatrace-docker-registry \



   --docker-server=<YOUR_ENVIRONMENT_URL> \



   --docker-username=<YOUR_ENVIRONMENT_ID> \



   --docker-password=<YOUR_INSTALLER_DOWNLOAD_TOKEN>
   ```


   ```
   oc -n dynatrace create secret docker-registry dynatrace-docker-registry \



   --docker-server=<YOUR_ENVIRONMENT_URL> \



   --docker-username=<YOUR_ENVIRONMENT_ID> \



   --docker-password=<YOUR_INSTALLER_DOWNLOAD_TOKEN> -n dynatrace
   ```


   Нужно заменить


   * `<YOUR_ENVIRONMENT_URL>` на URL окружения (без `https://`). Пример: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` на имя пользователя учётной записи Docker (совпадает с ID в URL окружения выше).


     Чтобы определить ID окружения, см. синтаксис ниже.


     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_INSTALLER_DOWNLOAD_TOKEN>` на токен доступа с областью действия `InstallerDownload`, созданный в разделе [Prerequisites](#prereq)
3. Создать секрет, который хранит данные аутентификации для сервера Dynatrace, используемого ActiveGate.


   Kubernetes


   OpenShift


   ```
   kubectl -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```


   ```
   oc -n dynatrace create secret generic dynatrace-tokens \



   --from-literal=tenant-token=<YOUR_TENANT_TOKEN> \



   --from-literal=auth-token=<YOUR_AUTH_TOKEN>
   ```


   Нужно заменить


   * `<YOUR_TENANT_TOKEN>` на значение `tenantToken`, полученное в разделе [Prerequisites](#prereq) из информации о подключении.
   * `<YOUR_AUTH_TOKEN>` на индивидуальный токен ActiveGate, полученный в разделе [Prerequisites](#prereq).
4. Создать файл `ag-deployment-example.yaml` со следующим содержимым:


   ag-deployment-example.yaml


   ```
   apiVersion: v1



   kind: Service



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   spec:



   type: ClusterIP



   selector:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   ports:



   - protocol: TCP



   port: 443



   targetPort: ag-https



   ---



   apiVersion: apps/v1



   kind: StatefulSet



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   podManagementPolicy: Parallel



   serviceName: ""



   selector:



   matchLabels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   template:



   metadata:



   labels:



   app.kubernetes.io/component: activegate



   component.dynatrace.com/feature: activegate



   spec:



   affinity:



   nodeAffinity:



   requiredDuringSchedulingIgnoredDuringExecution:



   nodeSelectorTerms:



   - matchExpressions:



   - key: kubernetes.io/arch



   operator: In



   values:



   - amd64



   - key: kubernetes.io/os



   operator: In



   values:



   - linux



   containers:



   - name: activegate



   image: <YOUR_ENVIRONMENT_URL>/linux/activegate:raw



   imagePullPolicy: Always



   ports:



   - containerPort: 9999



   name: ag-https



   protocol: TCP



   env:



   - name: DT_TENANT



   value: <YOUR_ENVIRONMENT_ID>



   - name: DT_SERVER



   value: <YOUR_COMMUNICATION_ENDPOINTS>



   - name: DT_ID_SEED_NAMESPACE



   value: dynatrace



   - name: DT_ID_SEED_K8S_CLUSTER_ID



   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>



   - name: DT_CAPABILITIES



   value: restInterface,kubernetes_monitoring,MSGrouter,metrics_ingest



   - name: DT_DEPLOYMENT_METADATA



   value: orchestration_tech=handcrated-ag-sts;script_version=none;orchestrator_id=none



   - name: DT_DNS_ENTRY_POINT



   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication



   volumeMounts:



   - name: dynatrace-tokens



   mountPath: /var/lib/dynatrace/secrets/tokens



   - name: truststore-volume



   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts



   readOnly: true



   subPath: k8s-local.jks



   - name: server-certs-storage



   mountPath: /var/lib/dynatrace/gateway/ssl



   - name: ag-lib-gateway-config



   mountPath: /var/lib/dynatrace/gateway/config



   - name: ag-lib-gateway-temp



   mountPath: /var/lib/dynatrace/gateway/temp



   - name: ag-lib-gateway-data



   mountPath: /var/lib/dynatrace/gateway/data



   - name: ag-log-gateway



   mountPath: /var/log/dynatrace/gateway



   - name: ag-tmp-gateway



   mountPath: /var/tmp/dynatrace/gateway



   livenessProbe:



   failureThreshold: 2



   httpGet:



   path: /rest/state



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 30



   successThreshold: 1



   timeoutSeconds: 1



   readinessProbe:



   failureThreshold: 3



   httpGet:



   path: /rest/health



   port: ag-https



   scheme: HTTPS



   initialDelaySeconds: 30



   periodSeconds: 15



   successThreshold: 1



   timeoutSeconds: 1



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi



   securityContext:



   allowPrivilegeEscalation: false



   capabilities:



   drop:



   - all



   privileged: false



   readOnlyRootFilesystem: true



   runAsNonRoot: true



   seccompProfile:



   type: RuntimeDefault



   initContainers:



   - name: certificate-loader



   image: <YOUR_ENVIRONMENT_URL>/linux/activegate:raw



   workingDir: /var/lib/dynatrace/gateway



   command: ['/bin/bash']



   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']



   volumeMounts:



   - mountPath: /var/lib/dynatrace/gateway/ssl



   name: truststore-volume



   imagePullSecrets:



   - name: dynatrace-docker-registry



   volumes:



   - name: truststore-volume



   emptyDir: {}



   - name: dynatrace-tokens



   secret:



   secretName: dynatrace-tokens



   - name: server-certs-storage



   emptyDir: {}



   - name: ag-lib-gateway-config



   emptyDir: {}



   - name: ag-lib-gateway-temp



   emptyDir: {}



   - name: ag-lib-gateway-data



   emptyDir: {}



   - name: ag-log-gateway



   emptyDir: {}



   - name: ag-tmp-gateway



   emptyDir: {}



   updateStrategy:



   type: RollingUpdate
   ```
5. Изменить файл YAML развёртывания.


   Добавить в файл `ag-deployment-example.yaml` данные конфигурации окружения, обязательно заменив:


   * `<YOUR_ENVIRONMENT_URL>` на URL окружения (без `https://`). Пример: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` на имя пользователя учётной записи Docker (совпадает с ID в URL окружения выше)


     Чтобы определить ID окружения, см. синтаксис ниже.


     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` на значение `communicationEndpoints`, полученное в разделе [Prerequisites](#prereq) из информации о подключении


     Список конечных точек подключения к серверу (`communicationEndpoints`) со временем может меняться.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` на UUID namespace kube-system, полученный в разделе [Prerequisites](#prereq)


   Параметры:


   * Опционально Можно изменить версию образа, используя другой тег версии
     Версии


     + `raw`, последний доступный образ
     + `1.sprint.patchlevel-raw`, образ для конкретной версии ActiveGate (например, `1.297.0-raw`)


   * Опционально Включить AppArmor, если доступен.


     Профиль AppArmor


     Для сохранения совместимости с более широким набором кластеров Kubernetes профиль AppArmor не указан в `ag-deployment-example.yaml`. Если AppArmor доступен в кластере Kubernetes, рекомендуется дополнительно аннотировать StatefulSet профилем `runtime/default`.


     ```
     spec:



     template:



     metadata:



     annotations:



     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Опционально Применить ограничения ресурсов согласно рекомендациям по объёму.


     Рекомендации по объёму для K8S monitoring и маршрутизации агентов


     В таблице ниже приведены рекомендуемые значения CPU и памяти для ActiveGate в зависимости от количества pod:


     | Количество pod | CPU | Память |
     | --- | --- | --- |
     | До 100 pod | 500 миллиядер (mCores) | 512 мебибайт (MiB) |
     | До 1000 pod | 1000 миллиядер (mCores) | 1 гибибайт (GiB) |
     | До 5000 pod | 1500 миллиядер (mCores) | 2 гибибайта (GiB) |
     | Свыше 5000 pod | свыше 1500 миллиядер (mCores)[1](#fn-2-1-def) | свыше 2 гибибайт (GiB)[1](#fn-2-1-def) |


     1


     Фактические значения зависят от вашего окружения.


     Эти ограничения следует рассматривать как рекомендацию. Они предназначены для предотвращения замедления процесса запуска ActiveGate и чрезмерного использования ресурсов узла. Значения по умолчанию покрывают широкий диапазон размеров кластеров, их можно изменять в соответствии со своими потребностями, опираясь на [метрики самомониторинга](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.") ActiveGate.

Дополнительные параметры конфигурации см. в разделе [Настройка контейнеризированного ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").
6. Разверните ActiveGate.


   Kubernetes


   OpenShift


   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```


   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
7. Чтобы убедиться, что ActiveGate успешно подключился к серверу Dynatrace, перейдите в **Deployment Status** > **ActiveGates**.

### Дополнительная настройка для архитектуры PPC64le

Чтобы завершить настройку контейнеризированного ActiveGate на архитектуре PPC64le, нужно выполнить ещё два шага:

1. Увеличить количество ядер CPU: чтобы соответствовать производительности архитектуры x86-64, количество ядер CPU нужно увеличить в четыре раза.
2. Уменьшить количество потоков ActiveGate:

   * Создать пользовательские свойства, как описано в разделе [Расширенная настройка](/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration#advanced-configuration "Узнайте, как настроить контейнеризированный ActiveGate.")
   * Добавить следующие строки в custom.properties:

     ```
     [com.compuware.apm.webserver]



     threadpool-max-size=30



     async-worker-pool-coresize=60
     ```

Для достижения лучшей производительности настоятельно рекомендуется выполнить описанные выше шаги.

## Выделенные развёртывания

* Для мониторинга Kubernetes/Openshift выбрать один из вариантов:

  + Использовать [Оператор Dynatrace](/managed/ingest-from/setup-on-k8s/deployment "Разверните оператор Dynatrace в Kubernetes")
  + Развернуть [ActiveGate напрямую как StatefulSet](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Установка и настройка ActiveGate в Kubernetes как StatefulSet.")
* Для сбора логов из Kubernetes использовать [Log Monitoring](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

## FIPS-совместимые образы

ActiveGate версии 1.315+

Доступен отдельный, FIPS-совместимый образ ActiveGate. Информацию о требованиях, ограничениях, месте получения образа и способе проверки развёртывания см. в разделе [Соответствие ActiveGate требованиям FIPS](/managed/ingest-from/dynatrace-activegate/activegate-fips-compliance "Узнайте о соответствии ActiveGate требованиям FIPS").