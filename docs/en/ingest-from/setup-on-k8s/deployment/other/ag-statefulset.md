---
title: Manually deploy ActiveGate as a StatefulSet
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset
scraped: 2026-02-26T21:29:54.162929
---

# Manually deploy ActiveGate as a StatefulSet

# Manually deploy ActiveGate as a StatefulSet

* Latest Dynatrace
* 5-min read
* Updated on Jan 19, 2025

Dynatrace Operator manages the lifecycle of several Dynatrace components, including ActiveGate. If you can't use Dynatrace Operator, you can manually deploy ActiveGate as a StatefulSet in your Kubernetes cluster. See below for instructions.

## Prerequisites

* [Create an access token with `PaaS Integration - InstallerDownload`](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope
* [Create an authentication token](/docs/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.")
* Get your kube-system namespace UUID

  How to extract the kube-system namespace UUID

  Run the command below and save the UUID from the output for later use.

  Kubernetes

  OpenShift

  ```
  kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
  ```

  ```
  oc get namespace kube-system -o jsonpath='{.metadata.uid}'
  ```

## Deploy ActiveGate

To deploy ActiveGate, follow the steps below.

1. Create a dedicated namespace (Kubernetes)/project (OpenShift).

   Depending on your platform, select one of the options below.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Create two secrets:

   * A secret holding the environment URL and login credentials for this registry
   * A secret for the ActiveGate authentication token

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret docker-registry dynatrace-docker-registry --docker-server=<YOUR_ENVIRONMENT_URL> --docker-username=<YOUR_ENVIRONMENT_ID> --docker-password=<YOUR_PAAS_TOKEN>
   ```

   ```
   oc -n dynatrace create secret docker-registry dynatrace-docker-registry --docker-server=<YOUR_ENVIRONMENT_URL> --docker-username=<YOUR_ENVIRONMENT_ID> --docker-password=<YOUR_PAAS_TOKEN>
   ```

   where you need to replace

   * `<YOUR_ENVIRONMENT_URL>` with your environment URL (without `http`). Example: `{your-environment}.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` with the Docker account username (same as the ID in your environment URL above).
   * `<YOUR_PAAS_TOKEN>` with the PaaS token you created in [Prerequisites](#prereq)

   Create a secret that holds the authentication details to the Dynatrace server used by ActiveGate.

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

   You need to replace

   * `<YOUR_TENANT_TOKEN>` with the `tenantToken` value obtained in [Prerequisites](#prereq) from the connectivity information.
   * `<YOUR_AUTH_TOKEN>` with the individual ActiveGate token obtained in [Prerequisites](#prereq).

   To determine your environment ID, see the syntax below.  
   **SaaS:** `https://{your-environment-id}.live.dynatrace.com`  
   **Managed:** `https://{your-domain}/e/{your-environment-id}`
3. Create a service account and a cluster role.

   Create a `kubernetes-monitoring-service-account.yaml` file with the following content.

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
4. Apply the file.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f kubernetes-monitoring-service-account.yaml
   ```

   ```
   oc apply -f kubernetes-monitoring-service-account.yaml
   ```
5. Create a file named `ag-monitoring-and-routing.yaml` with the following content, making sure to replace

   * `<YOUR_ENVIRONMENT_URL>` with your value as described above.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` with the Kubernetes namespace UUID obtained in [Prerequisites](#prereq).

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

   For more information about containerized ActiveGate configuration, see [Containerized ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").

   ActiveGate limit sizing hints

   See below for a list of proposed sizes in relation to the number of Pods:

   | Number of Pods | CPU | Memory |
   | --- | --- | --- |
   | Up to 1,000 Pods | 200 millicores (mCores) | 6 gibibyte (GiB) |
   | Up to 5,000 Pods | 1,000 millicores (mCores) | 10 gibibyte (GiB) |
   | Up to 20,000 Pods | 2,000 millicores (mCores) | 12 gibibytes (GiB) |
   | Over 20,000 Pods | over 2,000 millicores (mCores)[1](#fn-1-1-def) | over 12 gibibytes (GiB)[1](#fn-1-1-def) |

   1

   Actual figures depend on your environment.

   These limits should be taken as a guideline. They're designed to prevent ActiveGate startup process slowdown and excessive node resource usage. The default values cover a large range of different cluster sizes; you can modify them according to your needs, based on the ActiveGate [self-monitoring metrics](/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.").
   For more information with regards to sizing guidelines refer to [Sizing guide for Dynatrace ActiveGate components](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "Set resource limits for Dynatrace ActiveGates")

   For PPC64le architecture, additional configuration is required. For details, see [ActiveGate container image](/docs/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Deploy a containerized ActiveGate.").
6. Deploy ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ag-monitoring-and-routing.yaml
   ```

   ```
   oc apply -f ag-monitoring-and-routing.yaml
   ```

## Connect ActiveGate with Kubernetes API

Continue with step 3 from the [guide for enabling Kubernetes API monitoring](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring#connect-ag-k8s-api "Monitor the Kubernetes API using Dynatrace")

## ActiveGate update behavior

ActiveGate is updated automatically on pod restart whenever there is a new version available, unless the image already specifies a certain version.