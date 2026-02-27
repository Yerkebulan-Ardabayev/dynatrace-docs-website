---
title: ActiveGate container image
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-in-container
scraped: 2026-02-27T21:18:42.909311
---

# ActiveGate container image

# ActiveGate container image

* Latest Dynatrace
* 2-min read
* Updated on May 09, 2025

Dynatrace supports running ActiveGate in a container. As an example of a container-based deployment, this page describes how to deploy container-based ActiveGate using a StatefulSet on Kubernetes/OpenShift.

## Prerequisites

1. [Create an access token with `InstallerDownload`](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope
2. [Create an authentication token](/docs/ingest-from/dynatrace-activegate/activegate-security#generate-individual "Secure ActiveGates with dedicated tokens.")
3. Determine the ActiveGate communication endpoints and authentication. Use the [GET connectivity information for ActiveGate](/docs/dynatrace-api/environment-api/deployment/activegate/get-activegate-connectivity "View the connectivity information for ActiveGate via Dynatrace API.") API.
4. Get your kube-system namespace UUID
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

## System requirements

A Dynatrace ActiveGate image is supported on a variety of Kubernetes and OpenShift versions. For a complete list, see [Technology support - Kubernetes](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

Images are available for the following architectures:

* x86-64
* ARM64 (AArch64)
* s390x
* PPC64le

## Container registries

To prioritize seamless integration with your tooling and adaptability to your needs, we offer our container images in various ways to maximize flexibility:

* [Dynatrace built-in registry](/docs/ingest-from/setup-on-k8s/guides/container-registries#default "Manage container registries with Dynatrace") default
* [Public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry")
* [Bring your own private registry](/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries") Recommended

Please note that multi-arch Dynatrace container images, ensuring compatibility across various platforms are available from [public registries only](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry"). Dynatrace built-in registry provides only x86-64 images.

## Deployment

Dynatrace provides signed container images to ensure authenticity and integrity, along with SBOMs that list all included software components.
Verifying the signatures and reviewing the SBOMs enables effective vulnerability management and risk mitigation.
For verification details, see [Verify Software Bill of Materials (SBOM) Attestation](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature#sbom-attestation-verification "Verify Dynatrace image signatures").

Private or public registry

Dynatrace built-in registry

1. Create a dedicated namespace.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Create a secret that holds the authentication details to the Dynatrace server used by ActiveGate.

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
3. Create an `ag-deployment-example.yaml` file with the following content:

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
4. Modify your deployment YAML file.

   Add environment configuration details to the `ag-deployment-example.yaml` file, making sure to replace:

   * `CPU_ARCHITECTURE` with your CPU architecture. Possible values are `amd64`, `arm64`, `s390x`, and `ppcle64`
   * `<REPOSITORY_URL>` with one of the [supported registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry")
   * `<IMAGE_TAG>` with correct image tag ([examples](/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#image-tags "Store Dynatrace images in private registries"))
   * `<YOUR_ENVIRONMENT_ID>` with your environment ID

     To determine your environment ID, see the syntax below.

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` with the value of `communicationEndpoints` obtained in [Prerequisites](#prereq) from the connectivity information

     The list of server communication endpoints (`communicationEndpoints`) may change over time.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` with the kube-system namespace UUID obtained in [Prerequisites](#prereq)

     For PPC64le architecture, additional configuration is required. For details, see [ActiveGate container image](/docs/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Deploy a containerized ActiveGate.").

   Options:

   * Optional Enable AppArmor if available.

     AppArmor profile

     To maintain compatibility with a wider array of Kubernetes clusters, the AppArmor profile is not specified in `ag-deployment-example.yaml`. If AppArmor is available on your Kubernetes cluster, we recommend that you additionally annotate StatefulSet with a `runtime/default` profile.

     ```
     spec:



     template:



     metadata:



     annotations:



     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Optional Apply resource limits according to sizing hints.

     K8S monitoring and agent routing sizing hints

     The table below lists suggested ActiveGate CPU and memory sizes according to the number of pods:

     | Number of pods | CPU | Memory |
     | --- | --- | --- |
     | Up to 100 pods | 500 millicores (mCores) | 512 mebibytes (MiB) |
     | Up to 1,000 pods | 1,000 millicores (mCores) | 1 gibibyte (GiB) |
     | Up to 5,000 pods | 1,500 millicores (mCores) | 2 gibibytes (GiB) |
     | Over 5,000 pods | over 1,500 millicores (mCores)[1](#fn-1-1-def) | over 2 gibibytes (GiB)[1](#fn-1-1-def) |

     1

     Actual figures depend on your environment.

     These limits should be taken as a guideline. They're designed to prevent ActiveGate startup process slowdown and excessive node resource usage. The default values cover a large range of different cluster sizes; you can modify them according to your needs, based on the ActiveGate [self-monitoring metrics](/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.").

   For additional configuration options, see [Containerized ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").
5. Deploy ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
6. To verify that ActiveGate has successfully connected to the Dynatrace server, go to **Deployment Status** > **ActiveGates**.

1. Create a dedicated namespace.

   Kubernetes

   OpenShift

   ```
   kubectl create namespace dynatrace
   ```

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Create a secret that holds the environment URL and authentication details for this registry.

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

   You need to replace

   * `<YOUR_ENVIRONMENT_URL>` with your environment URL (without `https://`). Example: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` with the Docker account username (the same as the ID in your environment URL above).

     To determine your environment ID, see the syntax below.

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_INSTALLER_DOWNLOAD_TOKEN>` with the access token with `InstallerDownload` scope you created in [Prerequisites](#prereq)
3. Create a secret that holds the authentication details to the Dynatrace server used by ActiveGate.

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
4. Create an `ag-deployment-example.yaml` file with the following content:

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
5. Modify your deployment YAML file.

   Add environment configuration details to the `ag-deployment-example.yaml` file, making sure to replace:

   * `<YOUR_ENVIRONMENT_URL>` with your environment URL (without `https://`). Example: `abc12345.live.dynatrace.com`
   * `<YOUR_ENVIRONMENT_ID>` with the Docker account username (the same as the ID in your environment URL above)

     To determine your environment ID, see the syntax below.

     + **SaaS:** `https://{your-environment-id}.live.dynatrace.com`
     + **Managed:** `https://{your-domain}/e/{your-environment-id}`
   * `<YOUR_COMMUNICATION_ENDPOINTS>` with the value of `communicationEndpoints` obtained in [Prerequisites](#prereq) from the connectivity information

     The list of server communication endpoints (`communicationEndpoints`) may change over time.
   * `<YOUR_KUBE-SYSTEM_NAMESPACE_UUID>` with the kube-system namespace UUID obtained in [Prerequisites](#prereq)

   Options:

   * Optional You can change the image version by using different version tag
     Versions

     + `raw`âThe latest available image
     + `1.sprint.patchlevel-raw`âAn image for a particular ActiveGate version (for example, `1.297.0-raw`)

   * Optional Enable AppArmor if available.

     AppArmor profile

     To maintain compatibility with a wider array of Kubernetes clusters, the AppArmor profile is not specified in `ag-deployment-example.yaml`. If AppArmor is available on your Kubernetes cluster, we recommend that you additionally annotate StatefulSet with a `runtime/default` profile.

     ```
     spec:



     template:



     metadata:



     annotations:



     container.apparmor.security.beta.kubernetes.io/activegate: runtime/default
     ```
   * Optional Apply resource limits according to sizing hints.

     K8S monitoring and agent routing sizing hints

     The table below lists suggested ActiveGate CPU and memory sizes according to the number of pods:

     | Number of pods | CPU | Memory |
     | --- | --- | --- |
     | Up to 100 pods | 500 millicores (mCores) | 512 mebibytes (MiB) |
     | Up to 1,000 pods | 1,000 millicores (mCores) | 1 gibibyte (GiB) |
     | Up to 5,000 pods | 1,500 millicores (mCores) | 2 gibibytes (GiB) |
     | Over 5,000 pods | over 1,500 millicores (mCores)[1](#fn-2-1-def) | over 2 gibibytes (GiB)[1](#fn-2-1-def) |

     1

     Actual figures depend on your environment.

     These limits should be taken as a guideline. They're designed to prevent ActiveGate startup process slowdown and excessive node resource usage. The default values cover a large range of different cluster sizes; you can modify them according to your needs, based on the ActiveGate [self-monitoring metrics](/docs/analyze-explore-automate/metrics-classic/self-monitoring-metrics#activegate-insights "Explore the complete list of self-monitoring Dynatrace metrics.").

   For additional configuration options, see [Containerized ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration "Learn how to configure containerized ActiveGate.").
6. Deploy ActiveGate.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f ./ag-deployment-example.yaml
   ```

   ```
   oc apply -f ./ag-deployment-example.yaml
   ```
7. To verify that ActiveGate has successfully connected to the Dynatrace server, go to **Deployment Status** > **ActiveGates**.



### Additional configuration for PPC64le architecture

To finish setup of containerized ActiveGate on PPC64le architecture, two more steps are needed:

1. Increase the number of CPU cores: To match the performance of the x86-64 architecture, the CPU core count should be increased by a factor of four.
2. Reduce the number of ActiveGate threads:

   * Create custom properties as described in [Advanced configuration](/docs/ingest-from/dynatrace-activegate/activegate-in-container/configuration#advanced-configuration "Learn how to configure containerized ActiveGate.")
   * Add the following lines to custom.properties:

     ```
     [com.compuware.apm.webserver]



     threadpool-max-size=30



     async-worker-pool-coresize=60
     ```

To achieve better performance, we highly recommend applying the steps above.

## Dedicated deployments

* To monitor Kubernetes/Openshift, select one of the following:

  + Use [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")
  + Deploy [ActiveGate directly as a StatefulSet](/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.")
* To collect logs from Kubernetes, use [Log Monitoring](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-logs-from-kubernetes "Dynatrace supports collecting log data from Kubernetes container orchestration systems via OneAgent Log Module or Kubernetes Log Module.").

## FIPS-compliant images

ActiveGate version 1.315+

There is a dedicated, FIPS-compliant ActiveGate image available. See [ActiveGate FIPS compliance](/docs/ingest-from/dynatrace-activegate/activegate-fips-compliance "Learn about ActiveGate FIPS compliance") for information on requirements, limitations, where to get the image, and how to verify the deployment.