---
title: Развернуть ActiveGate как StatefulSet вручную
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset
---

# Развернуть ActiveGate как StatefulSet вручную

# Развернуть ActiveGate как StatefulSet вручную

* 5 минут чтения
* Обновлено 19 янв. 2025

Dynatrace Operator управляет жизненным циклом нескольких компонентов Dynatrace, включая ActiveGate. Если использовать Dynatrace Operator невозможно, можно развернуть ActiveGate как StatefulSet в кластере Kubernetes вручную. Инструкции приведены ниже.

## Предварительные требования

* [Создайте токен доступа с областью действия `PaaS Integration - InstallerDownload`](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Узнайте о концепции токена доступа и его областях действия.")
* [Создайте токен аутентификации](/managed/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Защитите ActiveGate с помощью отдельных токенов.")
* Получите UUID пространства имён kube-system

  Как извлечь UUID пространства имён kube-system

  Выполните команду ниже и сохраните UUID из вывода для дальнейшего использования.

  Kubernetes

  OpenShift

  ```
  kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
  ```

  ```
  oc get namespace kube-system -o jsonpath='{.metadata.uid}'
  ```

## Развёртывание ActiveGate


Чтобы развернуть ActiveGate, выполни шаги ниже.


1. Создай выделенный namespace (Kubernetes) / project (OpenShift).


   В зависимости от платформы выбери один из вариантов ниже.


   Kubernetes


   OpenShift


   ```
   kubectl create namespace dynatrace
   ```


   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Создай два секрета:


   * Секрет с URL окружения и учётными данными для входа в этот реестр
   * Секрет с токеном аутентификации ActiveGate


   Kubernetes


   OpenShift


   ```
   kubectl -n dynatrace create secret docker-registry dynatrace-docker-registry --docker-server=<YOUR_ENVIRONMENT_URL> --docker-username=<YOUR_ENVIRONMENT_ID> --docker-password=<YOUR_PAAS_TOKEN>
   ```


   ```
   oc -n dynatrace create secret docker-registry dynatrace-docker-registry --docker-server=<YOUR_ENVIRONMENT_URL> --docker-username=<YOUR_ENVIRONMENT_ID> --docker-password=<YOUR_PAAS_TOKEN>
   ```


   где нужно заменить


   * `<YOUR_ENVIRONMENT_URL>` на URL своего окружения (без `http`). Пример: `{your-environment}.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` на имя пользователя учётной записи Docker (совпадает с ID в URL окружения выше).
   * `<YOUR_PAAS_TOKEN>` на PaaS-токен, созданный в разделе [Prerequisites](#prereq)


   Создай секрет с данными аутентификации для сервера Dynatrace, используемого ActiveGate.


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


   Чтобы узнать ID окружения, используй синтаксис ниже.  
   **SaaS:** `https://{your-environment-id}.live.dynatrace.com`  
   **Managed:** `https://{your-domain}/e/{your-environment-id}`
3. Создай сервисный аккаунт и роль кластера.


   Создай файл `kubernetes-monitoring-service-account.yaml` со следующим содержимым.


   kubernetes-monitoring-service-account.yaml


   ```
   apiVersion: v1



   kind: ServiceAccount



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   name: dynatrace-activegate



   rules:



   - apiGroups:



   - ""



   - batch



   - apps



   - apps.openshift.io



   resources:



   - nodes



   - nodes/metrics



   - pods



   - namespaces



   - deployments



   - replicasets



   - deploymentconfigs



   - replicationcontrollers



   - jobs



   - cronjobs



   - statefulsets



   - daemonsets



   - events



   - resourcequotas



   - pods/proxy



   - services



   verbs:



   - list



   - watch



   - get



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRoleBinding



   metadata:



   name: dynatrace-activegate



   roleRef:



   apiGroup: rbac.authorization.k8s.io



   kind: ClusterRole



   name: dynatrace-activegate



   subjects:



   - kind: ServiceAccount



   name: dynatrace-activegate



   namespace: dynatrace
   ```
4. Примени файл.


   Kubernetes


   OpenShift


   ```
   kubectl apply -f kubernetes-monitoring-service-account.yaml
   ```


   ```
   oc apply -f kubernetes-monitoring-service-account.yaml
   ```
5. Создай файл с именем `ag-monitoring-and-routing.yaml` со следующим содержимым, заменив


   * `<YOUR_ENVIRONMENT_URL>` на своё значение, как описано выше.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` на UUID namespace Kubernetes, полученный в разделе [Prerequisites](#prereq).


   kubernetes-monitoring-and-routing.yaml


   ```
   apiVersion: v1



   kind: Service



   metadata:



   name: dynatrace-activegate



   namespace: dynatrace



   spec:



   type: ClusterIP



   selector:



   activegate: kubernetes-monitoring-and-routing



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



   activegate: kubernetes-monitoring-and-routing



   spec:



   serviceName: ""



   selector:



   matchLabels:



   activegate: kubernetes-monitoring-and-routing



   template:



   metadata:



   #     Uncomment the lines below to enable AppArmor



   #     annotations:



   #  container.apparmor.security.beta.kubernetes.io/activegate: runtime/default



   labels:



   activegate: kubernetes-monitoring-and-routing



   spec:



   serviceAccountName: dynatrace-activegate



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



   image: <YOUR_ENVIRONMENT_URL>/linux/activegate



   imagePullPolicy: Always



   ports:



   - name: ag-https



   containerPort: 9999



   env:



   - name: DT_ID_SEED_NAMESPACE



   value: dynatrace



   - name: DT_ID_SEED_K8S_CLUSTER_ID



   value: <YOUR_KUBE-SYSTEM_NAMESPACE_UUID>



   - name: DT_CAPABILITIES



   value: kubernetes_monitoring,MSGrouter,restInterface



   # - name: DT_NETWORK_ZONE



   #   value: <CUSTOM_NZ>



   - name: DT_DNS_ENTRY_POINT



   value: https://$(DYNATRACE_ACTIVEGATE_SERVICE_HOST):$(DYNATRACE_ACTIVEGATE_SERVICE_PORT)/communication



   volumeMounts:



   - name: dynatrace-tokens



   mountPath: /var/lib/dynatrace/secrets/tokens



   - name: truststore-volume



   mountPath: /opt/dynatrace/gateway/jre/lib/security/cacerts



   readOnly: true



   subPath: k8s-local.jks



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



   cpu: 250m



   memory: 512Mi



   limits:



   cpu: 250m



   memory: 512Mi



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



   image: <YOUR_ENVIRONMENT_URL>/linux/activegate



   workingDir: /var/lib/dynatrace/gateway



   command: ['/bin/bash']



   args: ['-c', '/opt/dynatrace/gateway/k8scrt2jks.sh']



   volumeMounts:



   - mountPath: /var/lib/dynatrace/gateway/ssl



   name: truststore-volume



   imagePullSecrets:



   - name: dynatrace-docker-registry



   volumes:



   - name: dynatrace-tokens



   secret:



   secretName: dynatrace-tokens



   - name: truststore-volume



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


   Подробнее о конфигурации контейнеризованного ActiveGate см. в разделе [Конфигурация контейнеризованного ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Узнайте, как настроить контейнеризованный ActiveGate.").


   Рекомендации по ограничению ресурсов ActiveGate


   Ниже приведены предлагаемые размеры в зависимости от количества Pod:


   | Количество Pod | CPU | Память |
   | --- | --- | --- |
   | До 1 000 Pod | 200 миллиядер (mCores) | 6 гибибайт (GiB) |
   | До 5 000 Pod | 1 000 миллиядер (mCores) | 10 гибибайт (GiB) |
   | До 20 000 Pod | 2 000 миллиядер (mCores) | 12 гибибайт (GiB) |
   | Более 20 000 Pod | более 2 000 миллиядер (mCores)[1](#fn-1-1-def) | более 12 гибибайт (GiB)[1](#fn-1-1-def) |


   1


   Фактические значения зависят от окружения.


   Эти ограничения носят рекомендательный характер. Они призваны предотвратить замедление процесса запуска ActiveGate и избыточное потребление ресурсов узла. Значения по умолчанию покрывают широкий диапазон размеров кластеров; их можно изменить под свои нужды, опираясь на [метрики самомониторинга](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Просмотрите полный список метрик самомониторинга Dynatrace.") ActiveGate.
   Подробнее о рекомендациях по размерам см. в разделе [Руководство по размерам компонентов Dynatrace ActiveGate](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "Рекомендации по ресурсам CPU и памяти для Dynatrace ActiveGate, развёрнутых в Kubernetes, с учётом масштаба кластера и типа нагрузки.")

   Для архитектуры PPC64le требуется дополнительная настройка. Подробности см. в разделе [Образ контейнера ActiveGate](/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Развёртывание контейнеризованного ActiveGate.").
6. Разверни ActiveGate.


   Kubernetes


   OpenShift


   ```
   kubectl apply -f ag-monitoring-and-routing.yaml
   ```


   ```
   oc apply -f ag-monitoring-and-routing.yaml
   ```
## Подключение ActiveGate к Kubernetes API

Перейди к шагу 3 из [руководства по включению мониторинга Kubernetes API](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect-ag-k8s-api "Мониторинг Kubernetes API с помощью Dynatrace")

## Поведение ActiveGate при обновлении

ActiveGate обновляется автоматически при перезапуске пода, если доступна новая версия, при условии что в образе не указана конкретная версия.