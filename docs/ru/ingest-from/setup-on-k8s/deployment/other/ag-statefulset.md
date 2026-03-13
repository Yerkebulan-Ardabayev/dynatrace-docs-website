---
title: Manually deploy ActiveGate as a StatefulSet
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset
scraped: 2026-03-06T21:33:13.482217
---

# Ручное развёртывание ActiveGate как StatefulSet

# Ручное развёртывание ActiveGate как StatefulSet

* Latest Dynatrace
* Чтение: 5 мин
* Обновлено 19 января 2025 г.

Dynatrace Operator управляет жизненным циклом нескольких компонентов Dynatrace, включая ActiveGate. Если вы не можете использовать Dynatrace Operator, вы можете вручную развернуть ActiveGate как StatefulSet в вашем кластере Kubernetes. Ниже приведены инструкции.

## Предварительные требования

* [Создайте токен доступа с областью `PaaS Integration - InstallerDownload`](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens.md#paas-token "Узнайте концепцию токена доступа и его областей.")
* [Создайте токен аутентификации](../../../dynatrace-activegate/activegate-security.md#generate-individual "Защитите ActiveGate с помощью выделенных токенов.")
* Получите UUID пространства имён kube-system

  Как извлечь UUID пространства имён kube-system

  Выполните приведённую ниже команду и сохраните UUID из вывода для дальнейшего использования.

  Kubernetes

  OpenShift

  ```
  kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
  ```

  ```
  oc get namespace kube-system -o jsonpath='{.metadata.uid}'
  ```

## Развёртывание ActiveGate

Для развёртывания ActiveGate выполните следующие шаги.

1. Создайте выделенное пространство имён (Kubernetes) / проект (OpenShift).

   В зависимости от вашей платформы выберите один из вариантов ниже.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Создайте два секрета:

   * Секрет, содержащий URL среды и учётные данные для входа в этот реестр
   * Секрет для токена аутентификации ActiveGate

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret docker-registry dynatrace-docker-registry --docker-server=<YOUR_ENVIRONMENT_URL> --docker-username=<YOUR_ENVIRONMENT_ID> --docker-password=<YOUR_PAAS_TOKEN>
   ```

   ```
   oc -n dynatrace create secret docker-registry dynatrace-docker-registry --docker-server=<YOUR_ENVIRONMENT_URL> --docker-username=<YOUR_ENVIRONMENT_ID> --docker-password=<YOUR_PAAS_TOKEN>
   ```

   где необходимо заменить

   * `<YOUR_ENVIRONMENT_URL>` на URL вашей среды (без `http`). Пример: `{your-environment}.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` на имя пользователя учётной записи Docker (совпадает с ID в URL вашей среды выше).
   * `<YOUR_PAAS_TOKEN>` на PaaS-токен, созданный в разделе [Предварительные требования](#prereq)

   Создайте секрет, содержащий данные аутентификации для сервера Dynatrace, используемого ActiveGate.

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

   Необходимо заменить

   * `<YOUR_TENANT_TOKEN>` на значение `tenantToken`, полученное в разделе [Предварительные требования](#prereq) из информации о подключении.
   * `<YOUR_AUTH_TOKEN>` на индивидуальный токен ActiveGate, полученный в разделе [Предварительные требования](#prereq).

   Чтобы определить ID вашей среды, см. синтаксис ниже.
   **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
   **Managed:** `https://{your-domain}/e/{your-environment-id}`
3. Создайте сервисный аккаунт и кластерную роль.

   Создайте файл `kubernetes-monitoring-service-account.yaml` со следующим содержимым.

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
4. Примените файл.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f kubernetes-monitoring-service-account.yaml
   ```

   ```
   oc apply -f kubernetes-monitoring-service-account.yaml
   ```
5. Создайте файл с именем `ag-monitoring-and-routing.yaml` со следующим содержимым, обязательно заменив

   * `<YOUR_ENVIRONMENT_URL>` на ваше значение, как описано выше.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` на UUID пространства имён Kubernetes, полученный в разделе [Предварительные требования](#prereq).

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

   Для получения дополнительной информации о конфигурации контейнеризированного ActiveGate см. [Конфигурация контейнеризированного ActiveGate](../../../dynatrace-activegate/activegate-in-container/configuration.md "Узнайте, как настроить контейнеризированный ActiveGate.").

   Рекомендации по ограничениям ресурсов ActiveGate

   Ниже приведён список предлагаемых размеров в зависимости от количества подов:

   | Количество подов | CPU | Память |
   | --- | --- | --- |
   | До 1 000 подов | 200 миллиядер (mCores) | 6 гибибайт (GiB) |
   | До 5 000 подов | 1 000 миллиядер (mCores) | 10 гибибайт (GiB) |
   | До 20 000 подов | 2 000 миллиядер (mCores) | 12 гибибайт (GiB) |
   | Более 20 000 подов | более 2 000 миллиядер (mCores)[1](#fn-1-1-def) | более 12 гибибайт (GiB)[1](#fn-1-1-def) |

   1

   Фактические значения зависят от вашей среды.

   Эти ограничения следует рассматривать как рекомендации. Они предназначены для предотвращения замедления процесса запуска ActiveGate и чрезмерного использования ресурсов узлов. Значения по умолчанию охватывают широкий диапазон различных размеров кластеров; вы можете изменить их в соответствии с вашими потребностями на основе [метрик самомониторинга](../../../../analyze-explore-automate/metrics-classic/self-monitoring-metrics.md#activegate-insights "Ознакомьтесь с полным списком метрик самомониторинга Dynatrace.") ActiveGate.
   Для получения дополнительной информации о рекомендациях по размерам обратитесь к [Руководству по размерам для компонентов Dynatrace ActiveGate](../../guides/deployment-and-configuration/resource-management/ag-resource-limits.md "Установите ограничения ресурсов для Dynatrace ActiveGate")

   Для архитектуры PPC64le требуется дополнительная конфигурация. Подробнее см. [Образ контейнера ActiveGate](../../../dynatrace-activegate/activegate-in-container.md#additional-configuration "Развертывание контейнеризированного ActiveGate.").
6. Разверните ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ag-monitoring-and-routing.yaml
   ```

   ```
   oc apply -f ag-monitoring-and-routing.yaml
   ```

## Подключение ActiveGate к Kubernetes API

Продолжите с шага 3 из [руководства по включению мониторинга Kubernetes API](../../guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring.md#connect-ag-k8s-api "Мониторинг Kubernetes API с помощью Dynatrace")

## Поведение обновления ActiveGate

ActiveGate обновляется автоматически при перезапуске пода, когда доступна новая версия, если только в образе не указана определённая версия.
