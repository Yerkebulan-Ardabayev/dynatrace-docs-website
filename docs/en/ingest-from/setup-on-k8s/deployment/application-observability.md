---
title: Get started with Kubernetes platform monitoring + Application observability
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/application-observability
scraped: 2026-02-16T09:21:58.837734
---

# Get started with Kubernetes platform monitoring + Application observability

# Get started with Kubernetes platform monitoring + Application observability

* Latest Dynatrace
* 7-min read
* Updated on Dec 09, 2025

This page provides instructions for deploying Dynatrace Operator to enable Kubernetes platform monitoring and Application observability. This configuration is ideal for monitoring Kubernetes environments and containerized applications.

## Use cases

* [Assess and troubleshoot Kubernetes cluster and workload health](/docs/observe/infrastructure-observability/kubernetes-app/use-cases/cluster-health "Understand and manage the health of your Kubernetes clusters with Dynatrace.")
* [Optimize Kubernetes workload resource usage](/docs/observe/infrastructure-observability/kubernetes-app/use-cases/resource-optimization "Efficiently utilize your cluster's resources by identifying workloads that don't fully utilize their allocated resources.")
* [Receive alerts and events to detect and respond to cluster anomalies](/docs/observe/infrastructure-observability/kubernetes-app/use-cases/alert-use-case "Proactively address Kubernetes issues using out-of-the-box alerting mechanisms.")
* [Explore metrics, events, and logs your Pods and nodes in a single interface](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")
* [Troubleshoot common health problems of Kubernetes workloads](/docs/observe/infrastructure-observability/kubernetes-app/use-cases/troubleshoot-health-problems "Identify and resolve health problems in Kubernetes workloads.")
* [Automatic distributed tracing across containers](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.")
* [Code-level and service insights](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") in application containers
* [Profiling and thread analysis](/docs/observe/application-observability/profiling-and-optimization "Learn how to use Dynatrace diagnostic tools for crash analysis, memory dump analysis, and more.")

If youâre looking to gain a complete view of your Kubernetes environment, check out the [deployment overview](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") to learn about [Full-Stack observability](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes"). You can further expand your Kubernetes observability on [Log Analytics](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace."), [Digital Experience](/docs/observe/digital-experience "Optimize end-user experience with Digital Experience Monitoring to ensure application performance and availability across all channels."), and [Application Security](/docs/secure/application-security "Access the Dynatrace Application Security functionalities.").

Prerequisites

### Before you begin

Before installing Dynatrace on your Kubernetes cluster, ensure that you meet the following requirements:

* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to monitor.
* You have sufficient privileges on the monitored cluster to run `kubectl` or `oc` commands.

### Cluster setup and configuration

* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to your Dynatrace environment URL.
* For OpenShift Dedicated, you need the [cluster-admin roleï»¿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Helm installation Use [Helm version 3ï»¿](https://dt-url.net/n5036j1).

### Supported versions

See supported Kubernetes/OpenShift [platform versions](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") and [distributions](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

[Configuring SCC](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.") is required for OpenShift for `cloudNativeFullStack` and `applicationMonitoring` with Dynatrace Operator CSI driver deployments.

The combination of `hostMonitoring` and `applicationMonitoring` in a Kubernetes cluster in the same environment is not supported.

## Installation options

Choose **one of the installation methods** that best suits your needs.

[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)[**Manifest**](#manifest)

## Helm

Dynatrace Operator version 0.8.0+

New Helm installation and upgrade instructions use our Helm chart available from an OCI registry. Therefore, if the Dynatrace repository is currently added to your local Helm repositories, it can be safely removed.

```
helm repo remove dynatrace
```

The installation process is independent of whether you are using Kubernetes or OpenShift. The platform is auto-detected during the installation.

1. Install Dynatrace Operator

   You have two options:

   Default installation / OCI registry installation

   The following command works for both default installations and installations using an OCI registry.

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic
   ```

   Installation with additional configuration of the Helm chart

   Edit the [`values.yaml`ï»¿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.8.1/config/helm/chart/default/values.yaml) sample from GitHub, and then run the install command, passing the YAML file as an argument:

   ```
   helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --create-namespace \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   If `installCRD` is set to `false`, you need to create the custom resource definition manually before starting the Helm installation:

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/dynatrace-operator-crd.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) and IBM Kubernetes Service (IKS) require [additional configuration](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").
2. Create secret for access tokens

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
3. Create your DynaKube custom resource YAML file.

   DynaKube custom resource sample for application monitoring

   You can review the [available parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/k8s-app-enabled: "true"



   feature.dynatrace.com/injection-readonly-volume: "true"



   spec:



   # For detailed instructions on DynaKube parameters in the spec section, visit https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



   # Dynatrace apiUrl including the /api path at the end.



   # Replace 'ENVIRONMENTID' with your environment ID.



   # For instructions on how to determine the environment ID and how to configure the apiUrl address, see https://www.dynatrace.com/support/help/reference/dynatrace-concepts/environment-id/.



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   metadataEnrichment:



   enabled: true



   oneAgent:



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi
   ```
4. Optional Monitor potentially sensitive data

   To monitor potentially sensitive data such as Secrets (values are masked before ingest) and ConfigMaps, you need to create a ClusterRole that allows access to these resources. Add the following snippet at the end of your DynaKube custom resource YAML file.

   Installation with sensitive data monitoring

   ```
   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   labels:



   rbac.dynatrace.com/aggregate-to-monitoring: "true"



   name: dynatrace-kubernetes-monitoring-sensitive



   rules:



   - apiGroups:



   - ""



   resources:



   - configmaps



   - secrets



   verbs:



   - list



   - watch



   - get
   ```

   The role will be automatically bound to the `dynatrace-kubernetes-monitoring` ClusterRole via aggregation rules. For more information about ClusterRole aggregation, see [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
5. Apply the DynaKube custom resource

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
6. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration with CSI driver, you should see the following Pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI driver is optional (see Step 2). If enabled, it gets deployed as DaemonSet and results in a CSI driver Pod on each node.

## Manifest

Kubernetes

OpenShift

1. Create a `dynatrace` namespace

   ```
   kubectl create namespace dynatrace
   ```
2. Install Dynatrace Operator

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes-csi.yaml
   ```

   Without CSI driver

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes.yaml
   ```

   VMware Tanzu Kubernetes (TKGI) and IBM Kubernetes Service (IKS) require [additional configuration](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

   Run the following command to see when Dynatrace Operator components finish initialization:

   ```
   kubectl -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Create secret for Access tokens

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Create your DynaKube custom resource YAML file.

   DynaKube custom resource sample for application monitoring

   You can review the [available parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/k8s-app-enabled: "true"



   feature.dynatrace.com/injection-readonly-volume: "true"



   spec:



   # For detailed instructions on DynaKube parameters in the spec section, visit https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



   # Dynatrace apiUrl including the /api path at the end.



   # Replace 'ENVIRONMENTID' with your environment ID.



   # For instructions on how to determine the environment ID and how to configure the apiUrl address, see https://www.dynatrace.com/support/help/reference/dynatrace-concepts/environment-id/.



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   metadataEnrichment:



   enabled: true



   oneAgent:



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi
   ```
5. Optional Monitor potentially sensitive data

   To monitor potentially sensitive data such as Secrets (values are masked before ingest) and ConfigMaps, you need to create a ClusterRole that allows access to these resources. Add the following snippet at the end of your DynaKube custom resource YAML file.

   Installation with sensitive data monitoring

   ```
   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   labels:



   rbac.dynatrace.com/aggregate-to-monitoring: "true"



   name: dynatrace-kubernetes-monitoring-sensitive



   rules:



   - apiGroups:



   - ""



   resources:



   - configmaps



   - secrets



   verbs:



   - list



   - watch



   - get
   ```

   The role will be automatically bound to the `dynatrace-kubernetes-monitoring` ClusterRole via aggregation rules. For more information about ClusterRole aggregation, see [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
6. Apply the DynaKube custom resource

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
7. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration with CSI driver, you should see the following Pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI driver is optional (see Step 2). If enabled, it gets deployed as DaemonSet and results in a CSI driver Pod on each node.

1. Add a `dynatrace` project

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Install Dynatrace Operator

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/openshift-csi.yaml
   ```

   Without CSI driver

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/openshift.yaml
   ```

   Run the following command to see when Dynatrace Operator components finish initialization:

   ```
   oc -n dynatrace wait pod --for=condition=ready --selector=app.kubernetes.io/name=dynatrace-operator,app.kubernetes.io/component=webhook --timeout=300s
   ```
3. Create secret for Access tokens

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Create your DynaKube custom resource YAML file.

   DynaKube custom resource sample for application monitoring

   You can review the [available parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to guides](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/k8s-app-enabled: "true"



   feature.dynatrace.com/injection-readonly-volume: "true"



   spec:



   # For detailed instructions on DynaKube parameters in the spec section, visit https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



   # Dynatrace apiUrl including the /api path at the end.



   # Replace 'ENVIRONMENTID' with your environment ID.



   # For instructions on how to determine the environment ID and how to configure the apiUrl address, see https://www.dynatrace.com/support/help/reference/dynatrace-concepts/environment-id/.



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   metadataEnrichment:



   enabled: true



   oneAgent:



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   resources:



   requests:



   cpu: 500m



   memory: 512Mi



   limits:



   cpu: 1000m



   memory: 1.5Gi
   ```
5. Optional Monitor potentially sensitive data

   To monitor potentially sensitive data such as Secrets (values are masked before ingest) and ConfigMaps, you need to create a ClusterRole that allows access to these resources. Add the following snippet at the end of your DynaKube custom resource YAML file.

   Installation with sensitive data monitoring

   ```
   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   labels:



   rbac.dynatrace.com/aggregate-to-monitoring: "true"



   name: dynatrace-kubernetes-monitoring-sensitive



   rules:



   - apiGroups:



   - ""



   resources:



   - configmaps



   - secrets



   verbs:



   - list



   - watch



   - get
   ```

   The role will be automatically bound to the `dynatrace-kubernetes-monitoring` ClusterRole via aggregation rules. For more information about ClusterRole aggregation, see [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").
6. Apply the DynaKube custom resource
   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   oc apply -f <your-DynaKube-CR>.yaml
   ```
7. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > oc get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration with CSI driver, you should see the following Pods:

   ```
   > oc get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```

   CSI driver is optional (see Step 2). If enabled, it gets deployed as DaemonSet and results in a CSI driver Pod on each node.

## Licensing

Kubernetes platform monitoring + Application observability requires [Dynatrace Platform Subscription (DPS)](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."). Kubernetes platform monitoring is licensed by number of Pods per hour ([pod-hours](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.")) and Application observability by the sum of container memory ([GiB-hours](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")).

## Learn more

After you've successfully installed the Dynatrace Operator, you may find the following resources helpful for further learning and troubleshooting.

[### Get actionable answers

Start to analyze your Kubernetes clusters and containerized Apps with Dynatrace and benefit from actionable answers.](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")[### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases")[### Troubleshooting

Troubleshoot any challenges you may encounter while working with the Dynatrace Operator and its various components.](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.")

[### How it works

Want to learn more about the Dynatrace components in your Kubernetes cluster?](/docs/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.")[### Reference

API reference and configuration options for all Dynatrace components within your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/reference "Contains a reference page with configuration options for each Dynatrace component")[### Dynatrace Operator release notes

See release notes for Dynatrace Operator.](/docs/whats-new/dynatrace-operator "Release notes for Dynatrace Operator")[### Update or uninstall

This page provides a detailed instructions on how to update and uninstall Dynatrace Operator.](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "Upgrade and uninstallation procedures for Dynatrace Operator")[### Dynatrace ActiveGate sizing guide

Sizing guide for Dynatrace ActiveGate components](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "Set resource limits for Dynatrace ActiveGates")

## Related topics

* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")