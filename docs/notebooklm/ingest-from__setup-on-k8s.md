# Dynatrace Documentation: ingest-from/setup-on-k8s

Generated: 2026-02-16

Files combined: 41

---


## Source: application-observability.md


---
title: Get started with Kubernetes platform monitoring + Application observability
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/application-observability
scraped: 2026-02-16T21:18:25.629612
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


---


## Source: eks-dto.md


---
title: Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/marketplaces/eks-dto
scraped: 2026-02-15T09:11:29.917800
---

# Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)

# Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)

* Latest Dynatrace
* 3-min read
* Published Jan 16, 2024

To use the Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS), you need to install the add-on and then connect EKS with your environment.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install Dynatrace Operator add-on EKS**](#install-dto)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Connect EKS with your environment**](#connect-eks)

## Step 1 Install Dynatrace Operator add-on for EKS

You can install the Dynatrace Operator add-on for AWS EKS through the AWS console or the CLI.

### Install through AWS console

To install the Dynatrace Operator add-on for AWS EKS through the AWS console

1. Go to your EKS cluster.
2. In the **Add-ons** section, select **Get more add-ons** > **AWS Marketplace add-ons**.
3. Filter for category **Monitoring** or search for **Dynatrace** to find the Dynatrace Operator add-on.
4. Select the checkbox in the upper-right corner of the card and then select **Next**.
5. Optional Select the version for this add-on and IAM role.
6. Select **Next** and review the configuration before applying.
7. Select **Create** and wait for the operation to finish.

   * The cluster overview page displays a confirmation banner.
   * A new `dynatrace` namespace is created
   * Several resources are automatically deployed by rendering the underlying helm chart.

### Installation through the CLI

To install the Dynatrace Operator add-on for AWS EKS through the CLI

1. Check the availability of the add-on and its versions.

   ```
   aws eks describe-addon-versions --addon-name dynatrace_dynatrace-operator
   ```
2. Deploy the add-on, specifying the version if necessary.

   ```
   aws eks create-addon --cluster-name <your_cluster_name> --addon-name dynatrace_dynatrace-operator --addon-version <version>
   ```
3. Verify the successful installation.

   ```
   aws eks describe-addon --cluster-name <your_cluster_name> --addon-name dynatrace_dynatrace-operator
   ```

## Step 2 Connect EKS with your environment

1. Create secret for access tokens.

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
2. Apply the DynaKube custom resource

   Monitoring with `cloudNativeFullStack` or `appOnly` (with CSI driver) is only supported for Dynatrace Operator version 0.15.0+.

   Download the [DynaKube custom resource sample for cloud-native full-stack mode on GitHubï»¿](https://dt-url.net/9n636jg). In addition, you can review the [available parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to-guides](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
3. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following Pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```


---


## Source: ag-in-vm.md


---
title: Deploy ActiveGate in a VM
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm
scraped: 2026-02-16T21:25:09.716059
---

# Deploy ActiveGate in a VM

# Deploy ActiveGate in a VM

* Latest Dynatrace
* 5-min read
* Updated on Jan 22, 2026

If you want to monitor several Kubernetes clusters with one ActiveGate and don't need to separate networks for administrative or operational traffic, you can install an ActiveGate on a virtual machine using a conventional installer to connect your clusters to Dynatrace as described below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Start installation**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#start-installation "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Download the installer**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#download-installer "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run the installer**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#run-installer "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Connect your Kubernetes clusters to Dynatrace**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#connect-clusters-to-dynatrace "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")

## Step 1 Start installation

1. In Dynatrace Hub, select **ActiveGate**.
2. Select **Set up**.

3. On the **Install Environment ActiveGate** page, select **Linux**.

## Step 2 Download the installer

How you download your installer depends on your setup and needs. You can choose to download an installer directly to the server where you plan to install Environment ActiveGate or you can download an installer to a different machine and then transfer the installer to the server.

1. Select [Route OneAgent traffic](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.") as an [ActiveGate purpose](/docs/ingest-from/dynatrace-activegate#purposes "Understand the basic concepts related to ActiveGate.").
2. Provide an access token with [`PaaS Integration - InstallerDownload`](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope. This token is required to download the ActiveGate installer from your environment. If you don't have an access token, you can create one right in the UI. The token is automatically appended to the download and installation commands you'll use later.
3. Select **Download installer**. There are two options:

   * Download via shell command. Copy and run the `wget` command.
   * Select the link to download the ActiveGate installer.
4. Verify the signature.
   Wait for the download to complete, and then verify the signature by copying the command from the second **Verify signature** text box and pasting the command into your terminal window.

## Step 3 Run the installer

An install parameter (determined by the ActiveGate purpose you selected) is automatically set for the command to run the installer. Make sure you use the command displayed in Dynatrace that reflects the ActiveGate purpose.
Copy the installation script command from the **Run the installer with root rights** step and paste it into your terminal.

### Add the Kubernetes CA certificate to the truststore Recommended

For instructions on how to add the certificate to the truststore file, see [Trusted root certificates for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to specify a custom truststore file that is merged with Java's root certificates and used as a default on all connections.").

### Customize installation

You can add additional [parameters](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") to the installation command to customize your installation. For example, to install ActiveGate in a different directory, use the `INSTALL=<path>` parameter:

```
[root@host]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh INSTALL=/hosted_app/dynatrace
```

### Default installation settings

For installation defaults, including default directories, see [ActiveGate default settings for Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux").

## Step 4 Connect your Kubernetes clusters to Dynatrace

To connect the Kubernetes API to Dynatrace, follow the instructions that apply to your Kubernetes version.

1. Create a service account and cluster role.

   Create a `kubernetes-monitoring-service-account.yaml` file with the following content.

   kubernetes-monitoring-service-account.yaml

   ```
   apiVersion: v1



   kind: ServiceAccount



   metadata:



   name: dynatrace-monitoring



   namespace: dynatrace



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   name: dynatrace-monitoring-cluster



   rules:



   - apiGroups:



   - ""



   resources:



   - nodes



   - pods



   - namespaces



   - replicationcontrollers



   - events



   - resourcequotas



   - pods/proxy



   - nodes/proxy



   - nodes/metrics



   - services



   - persistentvolumeclaims



   - persistentvolumes



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - batch



   resources:



   - jobs



   - cronjobs



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apps



   resources:



   - deployments



   - replicasets



   - statefulsets



   - daemonsets



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apps.openshift.io



   resources:



   - deploymentconfigs



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - config.openshift.io



   resources:



   - clusterversions



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - dynatrace.com



   resources:



   - dynakubes



   - edgeconnects



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apiextensions.k8s.io



   resources:



   - customresourcedefinitions



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - networking.k8s.io



   resources:



   - ingresses



   - networkpolicies



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - discovery.k8s.io



   resources:



   - endpointslices



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - autoscaling



   resources:



   - horizontalpodautoscalers



   verbs:



   - list



   - watch



   - get



   - nonResourceURLs:



   - /metrics



   - /version



   - /readyz



   - /livez



   verbs:



   - get



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRoleBinding



   metadata:



   name: dynatrace-monitoring-cluster



   roleRef:



   apiGroup: rbac.authorization.k8s.io



   kind: ClusterRole



   name: dynatrace-monitoring-cluster



   subjects:



   - kind: ServiceAccount



   name: dynatrace-monitoring



   namespace: dynatrace
   ```
2. Apply the file.

   ```
   kubectl apply -f kubernetes-monitoring-service-account.yaml
   ```
3. Get the Kubernetes API URL.

   ```
   $ kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```
4. Kubernetes version 1.24+ Create a file named `token-secret.yaml` with the following content.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: dynatrace-monitoring



   annotations:



   kubernetes.io/service-account.name: "dynatrace-monitoring"



   type: kubernetes.io/service-account-token
   ```
5. Kubernetes version 1.24+ Apply the file to create the `dynatrace-monitoring` secret.

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```
6. Get the bearer token.

   Kubernetes version 1.24+

   ```
   kubectl get secret dynatrace-monitoring -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Kubernetes versions 1.23 and lower

   ```
   kubectl get secret $(kubectl get sa dynatrace-monitoring -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Special instructions for Rancher distributions to get the API URL and the bearer token

   For **Rancher distributions** of Kubernetes, you need to use the bearer token and API URL **of the Rancher server**, because this server manages and secures traffic to the Kubernetes API server. Follow the steps below.

   1. Get the **Kubernetes API URL**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Configure a user.

      In the Rancher web UI, either create a new user or use an existing user to associate with the token. We recommend creating a new user.
   3. Set permissions.

      Make sure the user has either **Owner** or **Custom** permissions to the cluster you want to monitor.

      **Recommended**: select **Custom** permissions, and be sure to select these two roles: **View all Projects** and **View Nodes**.
   4. Create an API key.

      Go to **API & Keys** and create a key either for your specific account (enter your cluster name) or for all clusters (enter **No scope**). For security reasons, we recommend selecting the first option.

      Newly created keys display four fields. Make sure to use the content of the field called **Bearer token** to set up the connection to the Kubernetes API described in the next section.
7. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
8. Select **Connect manually**.
9. Provide a **Name**, the **Kubernetes API URL target**, and the **Kubernetes bearer token** for the Kubernetes cluster.
10. Make sure **Monitor events** and **Monitor Kubernetes namespaces, services, workloads, and pods** are turned on.

Disabling certificate validation isn't recommended because it imposes security risks. However, if you still want to disable certificate validation for test environments, make sure to disable **Require valid certificates for communication with the API server (recommended)** and **Verify hostname in certificate against Kubernetes API URL**.

11. Select **Save changes** to save your configuration.

To update ActiveGate, see [Update ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.").


---


## Source: ag-statefulset.md


---
title: Manually deploy ActiveGate as a StatefulSet
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset
scraped: 2026-02-16T21:32:13.917404
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


---


## Source: supported-technologies.md


---
title: Supported distributions
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/supported-technologies
scraped: 2026-02-16T21:18:24.092396
---

# Supported distributions

# Supported distributions

* Latest Dynatrace
* 6-min read
* Updated on Sep 07, 2023

This page gives an overview and documents the different configurations for all major Kubernetes distributions.

For the overall Dynatrace support lifecycle for Kubernetes and Red Hat OpenShift, including the currently supported versions, see [Dynatrace support lifecycle for Kubernetes and Red Hat OpenShift full stack Monitoring](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues").

## AWS Elastic Kubernetes Service (EKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for EKS.

Dynatrace supports a variety of different flavors of AWS EKS. For EKS on EC2 or bare metal, you can install Dynatrace in [any available deployment option](#installation-k8s) without any additional configuration changes. For EKS on Fargate, you can [install Dynatrace for App Observability](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.").

### AWS Bottlerocket OS

applicationMonitoring

Additional configuration is required for AWS Bottlerocket OS on EKS nodes.
You can deploy Dynatrace for Application Observability and configure Platform Observability via ActiveGate (Kubernetes API Monitoring). Platform Observability via Dynatrace OneAgent is not supported. Starting with Dynatrace Operator version 0.12.0 and before Dynatrace Operator version 1.7.0, the CSI driver is supported and needs to be configured in [read-only mode for Bottlerocket OS](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/advanced-security-configurations/injection-readonly-volume "Configure read-only CSI volumes for OneAgent injection to enhance data security."):

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



annotations:



feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



feature.dynatrace.com/injection-readonly-volume: "true"



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



applicationMonitoring: {}



activeGate:



capabilities:



- routing



- kubernetes-monitoring



- dynatrace-api



...
```

## Azure Kubernetes Service (AKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for AKS.

## Google Kubernetes Engine (GKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for GKE.

### GKE Standard & Anthos

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

If you deploy Dynatrace in `classicFullStack` or `hostMonitoring` without Dynatrace Operator CSI driver, additional configuration is required. Enable volume storage for the OneAgent by setting the `ONEAGENT_ENABLE_VOLUME_STORAGE` environment variable:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



...
```

### GKE Autopilot

applicationMonitoring

For GKE Autopilot, you can [install Dynatrace for App Observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"). Dynatrace Operator CSI driver is supported for all GKE Autopilot clusters running Kubernetes version 1.26+. Additionally, only images from the following repositories are supported and must be set during installation:

* `gcr.io/dynatrace-marketplace-prod/dynatrace-operator`
* `docker.io/dynatrace/dynatrace-operator`
* `public.ecr.aws/dynatrace/dynatrace-operator`

Standalone LogMonitoring on GKE Autopilot is fully supported since Dynatrace Operator version 1.4.2.

#### Allowlisting Dynatrace workloads

CSI driver Standalone LogMonitoring

Starting with GKE Autopilot version 1.32.1-gke.1376000 a `WorkloadAllowlist` explicitly permits security exceptions (for example, allowing the Dynatrace Operator CSI driver to run privileged workloads).
Dynatrace is working with Google to roll out these `WorkloadAllowlists` in a timely manner for each release.

Further details on the process can be found on the official [Google Cloud docsï»¿](https://cloud.google.com/kubernetes-engine/docs/resources/autopilot-partners).

Deploying and managing the AllowlistSynchronizer will be automated in Dynatrace Operator version 1.5.0+. For versions 1.4.1 - 1.4.X you will have to apply such manifest yourself.

##### AllowlistSynchronizer for version 1.4.2:

```
apiVersion: auto.gke.io/v1



kind: AllowlistSynchronizer



metadata:



name: allowlist-synchronizer-dynatrace



spec:



allowlistPaths:



- Dynatrace/csidriver/1.4.2/*



- Dynatrace/logmonitoring/1.4.2/*
```

Apply the `AllowlistSynchronizer`:

```
kubectl apply -f allowlist-synchronizer-dynatrace.yaml
```

v1.3.2 and earlier versions

CSI driver

Depending on the deployment option, the image can be set in different ways.

#### Helm

Set the `image` value in your helm `values.yaml` to one of the supported repositories during installation.

```
--set image=gcr.io/dynatrace-marketplace-prod/dynatrace-operator:v1.3.2
```

```
--set image=docker.io/dynatrace/dynatrace-operator:v1.3.2
```

#### Manifests

1. Instead of applying the manifest, the manifests (`kubernetes-csi.yaml`) have to be downloaded from the [release pageï»¿](https://github.com/Dynatrace/dynatrace-operator/releases).
2. Replace the value `public.ecr.aws/dynatrace/dynatrace-operator` in the image fields with `docker.io/dynatrace/dynatrace-operator`.
3. Apply the changed manifest. Use the appropriate one depending on if you want to use the CSI driver or not.

   ```
   kubectl apply -f kubernetes-csi.yaml
   ```

## Red Hat OpenShift

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

Classic full-stack is supported only on Kubernetes nodes that use Red Hat Enterprise Linux (RHEL) as their operating system.

For OpenShift, you need to [configure Security Context Constraints (SCC)](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.") for all deployments using the Dynatrace Operator CSI driver (`cloudNativeFullStack`, `applicationMonitoring`/`hostMonitoring` with CSI). In addition, starting with Openshift 4.13, you need to [configure the CSI Inline Ephemeral Volume Admissing plugin](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/openshift-configuration "Configure Dynatrace Operator in OpenShift environments.").

For managed OpenShift implementations such as AWS ROSA and Azure Red Hat OpenShift (ARO), Dynatrace supports the same features as dedicated OpenShift.

For OpenShift Dedicated, you need the [cluster-admin roleï»¿](https://dt-url.net/a2038v8).

## Rancher Kubernetes Engine 1 (RKE1)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required for RKE1.

## Rancher Kubernetes Engine 2 (RKE2)

applicationMonitoring

No specific configuration is required for RKE2 when `applicationMonitoring` mode is used. Due to SELinux policies on Red Hat Enterprise Linux derivatives, `hostMonitoring`, `cloudNativeFullStack` and `classicFullStack` modes are not supported.

## VMware Tanzu Kubernetes Grid Integrated Edition (TKGI)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

For TKGI, additional environment configurations are required for all deployment modes except `applicationMonitoring` without Dynatrace Operator CSI driver.

### `cloudNativeFullStack`, `applicationMonitoring` (with CSI driver), and `hostMonitoring`

In the `values.yaml`, additional configuration is required for these modes to configure the CSI driver:

```
csidriver:



enabled: true



kubeletPath: "/var/vcap/data/kubelet"
```

### `classicFullStack`

Requires images from the Dynatrace built-in registry and not from the public registry. Use the following configuration:

```
oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



- name: ONEAGENT_CONTAINER_STORAGE_PATH



value: /var/vcap/store
```

## IBM Kubernetes Service (IKS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

For IKS, additional environment configurations are required for all deployment modes except `applicationMonitoring` without the CSI driver.

### `cloudNativeFullStack`, `applicationMonitoring` (with CSI driver), and `hostMonitoring`

Additional configuration is required for these modes to configure the CSI driver:

```
csidriver:



enabled: true



kubeletPath: "/var/data/kubelet"
```

### `classicFullStack`

Requires images from the Dynatrace built-in registry and not from the public registry. Use the following configuration:

```
oneAgent:



classicFullStack:



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"



- name: ONEAGENT_CONTAINER_STORAGE_PATH



value: /opt
```

## SUSE Container as a Service (CaaS)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

If you deploy Dynatrace in `classicFullStack` or `hostMonitoring` without the CSI driver, be sure to configure volume storage for OneAgent:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



classicFullStack: # change to `hostMonitoring` if needed



env:



- name: ONEAGENT_ENABLE_VOLUME_STORAGE



value: "true"
```

## Nutanix Kubernetes Platform (NKP, former D2iQ Konvoy)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required.

## Oracle Kubernetes Engine (OKE)

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required.

## Mirantis Kubernetes Engine

cloudNativeFullStack classicFullStack applicationMonitoring hostMonitoring

No specific configuration is required.


---


## Source: deployment.md


---
title: Deployment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment
scraped: 2026-02-16T21:14:04.602524
---

# Deployment

# Deployment

* Latest Dynatrace
* 6-min read
* Updated on Jan 28, 2026

Dynatrace provides a flexible approach to Kubernetes observability where you can pick and choose the level of observability you need for your Kubernetes clusters. This page gives an overview and guided path on the recommended options to cover your Kubernetes observability needs.
All deployment options on this page leverage [Dynatrace Operatorï»¿](https://github.com/Dynatrace/dynatrace-operator). For dedicated documentation and options for the major Kubernetes distributions, see [Distributions](/docs/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

## Observability options

**Observability value**

**Kubernetes platform monitoring**

**Kubernetes platform monitoring**  
+ **Application observability**

**Kubernetes platform monitoring**  
+ **Full-Stack observability**

Kubernetes platform

[Kubernetes resources and topology](/docs/observe/infrastructure-observability/kubernetes-app/use-cases "Real-world scenarios and best practices for leveraging the new Dynatrace Kubernetes experience.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Kubernetes metrics (CPU, memory, network, PVCs), events, and alerts](/docs/observe/infrastructure-observability/kubernetes-app/use-cases "Real-world scenarios and best practices for leveraging the new Dynatrace Kubernetes experience.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Applications

[Automatic distributed tracing across containers](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Code-level and service insights](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") in application containers

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Profiling and thread analysis](/docs/observe/application-observability/profiling-and-optimization "Learn how to use Dynatrace diagnostic tools for crash analysis, memory dump analysis, and more.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Live debugging for cloud-native applications](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.")

opt-in

opt-in

Infrastructure

[Host and process level details](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Host network analysis and topology](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Disk analysis and alerting](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Data in context

[Data enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation "Automate and optimize your system's metadata management") for [cost allocation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") and access control

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

License

[DPS pricing/packaging](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")

by [number of Pods](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.")

by [number of Pods](/docs/license/capabilities/container-monitoring/kubernetes-platform-monitoring "Learn how your consumption of the Dynatrace Kubernetes Platform Monitoring DPS capability is billed and charged.") and [sum container memory](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")

by [sum host memory](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#gib-hour "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.")

Additional opt-in values

Log analytics

[Log collection, data filtering, masking, processing and analytics](/docs/ingest-from/setup-on-k8s/deployment/k8s-log-monitoring "Manage your Kubernetes logs with Dynatrace.")

opt-out[1](#fn-1-1-def)  
[per GiB ingested](/docs/ingest-from/setup-on-k8s/quickstart "Deploy Dynatrace Operator on Kubernetes")

opt-out[1](#fn-1-1-def)  
[per GiB ingested](/docs/ingest-from/setup-on-k8s/quickstart "Deploy Dynatrace Operator on Kubernetes")

opt-out[1](#fn-1-1-def)  
[per GiB ingested](/docs/license/capabilities/log-analytics/dps-log-ingest "Learn how your consumption of the Log Management & Analytics - Ingest & Process DPS capability is billed and charged.")

Digital experience

[Real user monitoring, synthetic checks and session replay](/docs/observe/digital-experience "Optimize end-user experience with Digital Experience Monitoring to ensure application performance and availability across all channels.")

opt-in  
For details, see [DEM](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
For details, see [DEM](/docs/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")

Application Security

[Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") and [Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

opt-in  
[by sum container memory](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
[by sum host memory](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

[Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")

opt-in  
[by host-hour](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
[by host-hour](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

opt-in  
[by host-hour](/docs/license/capabilities/application-security "Learn how Dynatrace Application Security monitoring consumption is calculated using the Dynatrace Platform Subscription model.")

1

For new users, the Dynatrace environment is preconfigured to ingest logs, and opting out is managed through [log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

Rollout and permissions overview

This table gives an overview of all the used components and required permissions for your Kubernetes observability needs. Dynatrace Operator manages the lifecycle of all observability components needed for your Kubernetes observability needs.

**Components and permissions**

**Kubernetes platform monitoring**

**Kubernetes platform monitoring**  
+ **Application observability**

**Kubernetes platform monitoring**  
+ **Full-Stack observability**

Components

Dynatrace Operator for managing observability components and lifecycle

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Dynatrace Operator webhook for auto-injection and telemetry enrichment

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Dynatrace Operator CSI driver for resource-friendly management of components

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable") (opt-out)

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Observability components

ActiveGate

ActiveGate  
Dynatrace code modules  
Dynatrace Log module (opt-in)

ActiveGate  
Dynatrace code modules  
Dynatrace host module  
Dynatrace Log module

Dynatrace OpenTelemetry collector for extensions

opt-in

opt-in

opt-in

EdgeConnect for automations

opt-in

opt-in

opt-in

Permissions

Principle of least privilege

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

Kubernetes permissions [1](#fn-2-1-def)

Kubernetes RBAC

Kubernetes RBAC  
Privileged workload (CSI driver, opt-out)

Kubernetes RBAC  
Privileged workload (CSI driver)  
OS-level permission (Dynatrace host module)

1

Please see [Dynatrace Operator security](/docs/ingest-from/setup-on-k8s/reference/security "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") for more detailed documentation.

[### Kubernetes platform monitoring

Understand and troubleshoot the health of your Kubernetes clusters.](/docs/ingest-from/setup-on-k8s/deployment/platform-observability "Deploy Dynatrace Operator for Kubernetes platform monitoring.")[### Kubernetes platform monitoring + Application observability

Ensure workload and microservice health and performance with automatic instrumentation.](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")[### Kubernetes platform monitoring + Full-Stack observability

Ensure workload, microservice and infrastructure health and performance throughout your cluster.](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes")

## Leverage the Dynatrace platform value

The Dynatrace platform offers a variety of apps, analytics and automation functionality to cover your use cases for unified observability and security. You can leverage these capabilities for all the Kubernetes observability data you collect with any of the above modes, such as the ability to:

* Explore Kubernetes health and signals in the [Kubernetes app](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads.")
* Visualize data with [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")
* Collaborate and conduct custom analysis with [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")
* Automate with [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")
* Boost productivity with [Dynatrace Intelligence](/docs/dynatrace-intelligence "Get familiar with the capabilities of Dynatrace Intelligence.") and [enerative AI](/docs/dynatrace-intelligence/copilot "Learn about Dynatrace Intelligence generative AI.")
* Forecast trends and prevent issues with [Dynatrace Intelligence predictive AI analysis](/docs/dynatrace-intelligence/reference/ai-models/forecast-analysis "Learn how Dynatrace Intelligence predictive AI generates forecasts.")
* And much moreâ¦

## Deployment from Marketplaces

Dynatrace supports deploying Dynatrace Operator from within the following Marketplaces:

* [OpenShift OperatorHub](/docs/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub "Deploy Dynatrace Operator on OpenShift via OperatorHub.")
* [AWS Marketplaceï»¿](https://aws.amazon.com/marketplace/pp/prodview-brb73nceicv7u)
* [GKE Marketplaceï»¿](https://console.cloud.google.com/marketplace/product/dynatrace-marketplace-prod/dynatrace-operator)
* [Azure Marketplaceï»¿](https://azuremarketplace.microsoft.com/en-us/marketplace/apps/dynatrace.azure-dynatrace-operator?tab=Overview)

## Learn more

[### How it works

Familiarize yourself with Dynatrace components that are deployed in your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.")[### Guides

Learn how you can configure Dynatrace Operator to support specific use cases.](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases")[### Reference

API reference and configuration options for all Dynatrace components within your Kubernetes cluster.](/docs/ingest-from/setup-on-k8s/reference "Contains a reference page with configuration options for each Dynatrace component")[### Dynatrace Operator release notes

See release notes for Dynatrace Operator.](/docs/whats-new/dynatrace-operator "Release notes for Dynatrace Operator")


---


## Source: otlp-auto-config.md


---
title: Enable automatic OpenTelemetry OTLP exporter configuration
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config
scraped: 2026-02-16T09:36:36.008067
---

# Enable automatic OpenTelemetry OTLP exporter configuration

# Enable automatic OpenTelemetry OTLP exporter configuration

* Latest Dynatrace
* Published Nov 24, 2025

Dynatrace Operator version 1.8.0+

Dynatrace Operator can automatically configure the OpenTelemetry OTLP exporter for applications instrumented with an [OpenTelemetry SDKï»¿](https://opentelemetry.io/docs/languages/). This is done by injecting environment variables into your application pods at startup, allowing telemetry data to be sent directly to Dynatrace.

## Enable OTLP auto-configuration

### Provide a data ingest token

You need to provide a [data ingest token](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Configure tokens and permissions to monitor your Kubernetes cluster") to the Dynatrace Operator. This token is passed to your application as part of the OTLP exporter configuration.

### Update your DynaKube resource

Add the `otlpExporterConfiguration` section to your DynaKube custom resource. This enables auto-configuration for all signals (metrics, traces, logs):

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



otlpExporterConfiguration:



signals:



metrics: {}



traces: {}



logs: {}
```

You can enable injection for each signal type (metrics, traces, logs) separately.

**Note**: By default, if any `OTEL_EXPORTER_OTLP_*` environment variable is already present in the container spec, Dynatrace Operator will skip the injection of endpoint configuration (aka. `OTEL_EXPORTER_OTLP_*`) âeven if the existing configuration doesn't overlap with what would be added automatically. To allow Dynatrace Operator to override the existing configuration, enable [override mode](#override). Resource attributes (`OTEL_RESOURCE_ATTRIBUTES`) are not affected by this logic and will still be set or extended.

### Verify the auto-configuration

If the OTLP auto-configuration has been injected successfully, your application pod receives the following annotation:

```
otlp-exporter-configuration.dynatrace.com/injected: "true"
```

If something goes wrong, the pod is annotated with a reason for the failure:

```
otlp-exporter-configuration.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/reason: <reason>
```

## Injected OTLP configuration

### Environment variables

The following environment variables are injected into your application containers:

| Variable | Value |
| --- | --- |
| `DT_API_TOKEN` | `dataIngestToken provided by user` |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | `https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/traces` |
| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | `authorization=Api-Token $(DT_API_TOKEN)` |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | `https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | `authorization=Api-Token $(DT_API_TOKEN)` |
| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` | `delta` |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | `https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/logs` |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | `authorization=Api-Token $(DT_API_TOKEN)` |
| `OTEL_RESOURCE_ATTRIBUTES` | `k8s.cluster.name=dynakube,k8s.container.name=app ...` |

### Resource attributes

Dynatrace Operator adds resource attributes in `OTEL_RESOURCE_ATTRIBUTES` to enrich OpenTelemetry data providing topology and additional context on data points for a rich Dynatrace experience:

* `k8s.cluster.name`
* `k8s.container.name`
* `k8s.workload.name`
* `k8s.cluster.uid`
* `k8s.pod.name`
* `k8s.pod.uid`
* `k8s.node.name`
* `k8s.namespace.name`
* `k8s.workload.kind`
* `dt.kubernetes.cluster.id`
* `dt.entity.kubernetes_cluster`

The values for those attributes are derived from the cluster and pod metadata. Additionally, the [metadata enrichment rules](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#enrichment-options "Guides for telemetry enrichment on Kubernetes") defined in your tenant are applied to further enhance the resource attributes. Furthermore, all metadata provided in the `metadata.dynatrace.com/<key>: <value>` annotations on the namespace or on the injected pod are added as resource attributes.

Any attributes you have already set in `OTEL_RESOURCE_ATTRIBUTES` are preserved, and the above attributes are appended.

Resource attributes are always injected when autoâconfiguration is enabled, regardless of existing OTLP exporter settings or whether override mode is enabled.

## Limitations

### Application pods using `envFrom`

When you populate your environment variables using `envFrom`, Dynatrace Operator is not able to discover environment variables that are already set. In this case, the injected Dynatrace OTLP exporter config takes precedence over values coming from `envFrom`, even without using the [override mode](#override).

### Hardcoded SDK configuration

* In OTel SDKs, programmatic configuration takes precedence over environment variables. Ensure the standard exporter environment variables are supported by your application.
* Dynatrace always uses protocol `http/protobuf`. If your application is restricted to gRPC, the injected protocol variable will have no effect and communication will fail.

## Route OTLP traffic via ActiveGate

If an in-cluster ActiveGate is deployed with the same DynaKube that is used for OTLP auto-configuration, the traffic is routed through this ActiveGate. Without the in-cluster ActiveGate the traffic is sent directly to your Dynatrace tenant.

## Secrets management

The following secrets are created in each injected namespace:

* `dynatrace-otlp-exporter-certs` holds the certificates required for communication with the configured endpoint, which is one of the following:

  + The TLS certificate for the ActiveGate.
  + What is set in `.spec.trustedCAs`, if the tenant API is used as an endpoint.
* `dynatrace-otlp-exporter-config` holds a copy of the data ingest token.

Secrets are updated automatically when the token or certificate changes, but only new pods will receive updated values. Restart your application pods subsequent to a change to avoid authentication or communication issues.

**Note**: If secrets are not created quickly enough, or are temporarily unavailable for other reasons, OTLP exporter configuration injection [will be skipped](#verify-config).

## Injection control

### Namespace selector

To limit auto-configuration to specific namespaces, you can use a namespace selector:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



otlpExporterConfiguration:



namespaceSelector:



matchLabels:



my.app.com/otel: "true"



signals:



metrics: {}



traces: {}



logs: {}
```

### Pod and container annotations

For fine-grained control, you can use annotations to control injection behaviour on the pods directly:

* `feature.dynatrace.com/automatic-injection: false` (on DynaKube) disables automatic injection of code modules, metadata enrichment, and OTLP exporter auto-configuration by default.
* `dynatrace.com/inject: true/false` (on pod) enables/disables injection per pod.
* `otlp-exporter-configuration.dynatrace.com/inject: true/false` (on pod) enables/disables injection per pod.
* `container.inject.dynatrace.com/<container-name>: false` (on pod or DynaKube) disables injection for specific containers.

| `feature.dynatrace.com/automatic-injection` | `dynatrace.com/inject` | `otlp-exporter-configuration.dynatrace.com/inject` | Injected |
| --- | --- | --- | --- |
| true default | true/not set | true | yes |
| true default | true/not set | false | yes |
| true default | false | true | yes |
| true default | false | false | no |
| false | true | true | yes |
| false | true | false | yes |
| false | false/not set | true | yes |
| false | false/not set | false | no |

## Enable environment variable overrides

By default, any existing configuration (for example, already set environment variables) is not altered, overwritten, or removed. This includes all environment variables matching the pattern `OTEL_EXPORTER_OTLP_*`. If any of those environment variables already exist in a container specification, no automatic configuration is made **at all**, even if the activated signal does not directly conflict with the existing configuration.

For example, if only `traces` is activated in `.spec.otlpExporterConfiguration.signals` and the container has `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` already set, `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` won't be configured on your pod.

To enable this override, you can turn on the override mode:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



otlpExporterConfiguration:



signals:



metrics: {}



overrideEnvVars: true
```

With `.spec.otlpExporterConfiguration.overrideEnvVars: true`, Dynatrace Operator will:

* Add configuration for signals not yet present (in this example, `metrics`)
* Overwrite configuration for signals already present
* Retain existing configurations if they don't conflict with the configured signals

The following examples have the above DynaKube configuration with `metrics` enabled and `overrideEnvVars` set to `true`.

### Simple override

**Before**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: grpc



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token 123456
```

**After**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://<environment-id>.live.dynatrace.com/api/v2/otlp/v1/metrics



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token $(DT_API_TOKEN)
```

### Simple addition of the new signal

**Before**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_TRACES_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_TRACES_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_TRACES_HEADERS



value: authorization=Api-Token 123456
```

**After**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_TRACES_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_TRACES_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_TRACES_HEADERS



value: authorization=Api-Token 123456



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://<environment-id>.live.dynatrace.com/api/v2/otlp/v1/metrics



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token $(DT_API_TOKEN)
```

### OTLP general configuration environment variables

A special case is the use of `OTEL_EXPORTER_OTLP_ENDPOINT` and its companion environment variables. These variables provide defaults for all signals at once. If such a variable is already set for the container, it is not removed. Instead, the signal-specific configuration is added and takes precedence.

In this example, metrics will now be sent to the Dynatrace endpoint, while traces and logs would still be reported to the previously configured endpoint.

**Before**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_HEADERS



value: authorization=Api-Token 123456
```

**After**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_HEADERS



value: authorization=Api-Token 123456



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://<environment-id>.live.dynatrace.com/api/v2/otlp/v1/metrics



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token $(DT_API_TOKEN)
```

## `NO_PROXY` support

If you choose to have an ActiveGate and a proxy configured on your application pods, the ActiveGate service is automatically added to the `NO_PROXY` environment variable. If the environment variable does not yet exist, it will be created.

You can opt-out of of this by adding the following annotation to your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/otlp-exporter-configuration-set-no-proxy: "false"
```

## Related topics

* [DynaKube parameters for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.")


---


## Source: prepare-private-registry.md


---
title: Store Dynatrace images in private registries
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry
scraped: 2026-02-16T21:26:32.072603
---

# Store Dynatrace images in private registries

# Store Dynatrace images in private registries

* Latest Dynatrace
* 7-min read
* Published Feb 29, 2024

For users seeking greater control over their image hosting environment, Dynatrace offers the option to replicate images and signatures to private registries.

We recommend using a private registry for optimal performance and no rate limiting risks in high-demand and dynamic environments. Furthermore, to meet security standards and ensure software integrity while mitigating supply chain risks, image scanning and signature verification against Dynatrace images can be applied and is recommended.

By replicating Dynatrace images to your private registry, you can seamlessly merge excellent delivery performance with the assurance of secure, signed, and immutable images. We provide multi-arch images to ensure compatibility across various platforms supporting ARM64 (AArch64) and x86-64 CPU architectures on Linux.

This page offers guidance on securely storing Dynatrace immutable images in a private registry. It includes instructions for pulling images, verifying image signatures, and pushing them to your preferred private registry.

## Prerequisites

Before you begin, be sure to meet the following prerequisites:

* Required Private registry
* Required Write access to image repositories for Dynatrace images
* Optional [Skopeoï»¿](https://github.com/containers/skopeo/blob/main/install.md) for easy copying of our multi-arch images
* Optional [Cosignï»¿](https://docs.sigstore.dev/system_config/installation/) for image signature verification

## Dynatrace container images

Dynatrace immutable and signed container images are available on various container registries. For more details on repositories and tag information, explore our [supported public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry").

We strongly recommend choosing one of our supported public registries from which to copy container images.

Please do not use the Dynatrace built-in registry for copying images to private registries.

An exception applies for the OneAgent image for Classic Full-Stack, where the respective image **must** be copied from the built-in registry to work properly.

### Observability options

Depending on the [observability options](/docs/ingest-from/setup-on-k8s/deployment#observability-options-for-kubernetes "Deploy Dynatrace Operator on Kubernetes") you choose, you might want to only copy required images. The following table outlines the relations between Dynatrace images and observability options.

Observability option

Dynatrace Operator

Dynatrace ActiveGate

Dynatrace Code Module

Dynatrace OneAgent

Full observability

(Classic Full-Stack)

required

required

-

required [1](#fn-1-1-def)

Full observability

(Cloud-Native Full-Stack)

required

required

required

required

Kubernetes Observability

required

required

-

-

Application Observability

required

required

required

-

1

Must be replicated from Dynatrace built-in registry. See [Support for Classic Full-Stack monitoring](#classic-full-stack) for further details.

### Image tags

To show how versioning directly relates to image tagging, the following table lists real examples of image tags for Dynatrace container images.

Note how Dynatrace ActiveGate, Code Modules, and OneAgent share a similar versioning approach, while Dynatrace Operator, which follows a distinct release cadence, uses a different versioning approach.

In all cases, version-based image tagging is employed with container images. Mutable image tags like 'latest' are not used.

Container image

Image tag

dynatrace-operator

`docker.io/dynatrace/dynatrace-operator:v1.5.0`

dynatrace-activegate

`public.ecr.aws/dynatrace/dynatrace-activegate:1.301.70.20241127-162512`

dynatrace-codemodules

`public.ecr.aws/dynatrace/dynatrace-codemodules:1.301.70.20241127-162512`

dynatrace-oneagent

`public.ecr.aws/dynatrace/dynatrace-oneagent:1.301.70.20241127-162512`

dynatrace-k8s-node-config-collector

`public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:1.0.0`

### Image signature verification

All of our immutable and signed container images adhere to best practices, enhancing security and shielding against supply chain attacks. To learn how to verify signatures and guarantee software integrity, see [Verify Dynatrace image signatures](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures").

## Copy Dynatrace container images

The following guide describes how to copy Dynatrace container images from public Amazon ECR to our private registry with the following example attributes.

Private container registry address

`registry.my-company.com`

Dynatrace Operator repository

`dynatrace-operator`

Dynatrace ActiveGate repository

`dynatrace-activegate`

Dynatrace Code Modules repository

`dynatrace-codemodules`

Dynatrace OneAgent repository

`dynatrace-oneagent`

Dynatrace K8s Node Config Collector repository

`dynatrace-k8s-node-config-collector`

The instructions below to copy container images to your private registry:

Skopeo (recommended)

Docker CLI

Recommended

Due to its support for easy copying of multi-arch images and signatures[1](#fn-2-1-def), we strongly recommend that you use the Skopeo CLI for copying container images. To learn more about the Skopeo CLI, see [Skopeo GitHub repositoryï»¿](https://github.com/containers/skopeo).

In the following instructions, be sure to always replace `<tag>` with an available version (see the [Supported public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry") section).

#### Copy Dynatrace Operator image

The following command shows how to copy the Dynatrace Operator image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-operator:<tag> \



docker://registry.my-company.com/dynatrace-operator:<tag>
```

#### Copy Dynatrace ActiveGate image

The following command shows how to copy the Dynatrace ActiveGate image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-activegate:<tag> \



docker://registry.my-company.com/dynatrace-activegate:<tag>
```

#### Copy Dynatrace Code Modules image

The following command shows how to copy the Dynatrace Code Modules image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-codemodules:<tag> \



docker://registry.my-company.com/dynatrace-codemodules:<tag>
```

#### Copy Dynatrace OneAgent image

The following command shows how to copy the Dynatrace OneAgent image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-oneagent:<tag> \



docker://registry.my-company.com/dynatrace-oneagent:<tag>
```

#### Copy Dynatrace K8s Node Config Collector image

The following command shows how to copy the Dynatrace K8s Node Config Collector image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag> \



docker://registry.my-company.com/dynatrace-k8s-node-config-collector:<tag>
```

1

Requires `use-sigstore-attachments` to be set to `true` in *Skopeo*'s [container registriesï»¿](https://github.com/containers/image/blob/main/docs/containers-registries.d.5.md#individual-configuration-sections) configuration.

We strongly recommend that you use the Skopeo CLI instead of Docker CLI for copying Dynatrace container images from public to private registries, as the Docker CLI does not provide an easy way to copy multi-arch images and signatures.

If you still want to use Docker CLI, please refer to the [official Docker CLI documentationï»¿](https://docs.docker.com/engine/reference/commandline/cli/).

### Support for Classic Full-Stack monitoring

[Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.") requires a pre-configured Dynatrace OneAgent image, which is available **only** via the Dynatrace built-in registry.

Consequently, the OneAgent image must be replicated via the Dynatrace built-in registry as described below.

Prerequisites

#### Before you begin

Make sure you meet the following prerequisites:

* Required Non-optional prerequisites from the top
* Required Credentials for Dynatrace built-in registry

#### Obtain Dynatrace built-in registry credentials

As the Dynatrace built-in registry requires authentication, you need to know your monitoring environment ID and provide a PaaS token for the login:

* To determine `<your-environment-id>`, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* To determine `<your-paas-token>`, see [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

Example login using *Skopeo* CLI:

```
skopeo login -u <your-environment-id> -p <your-paas-token> <your-environment-url>
```

Please note that this section only addresses configurations of Classic Full-Stack monitoring.

#### Copy Dynatrace OneAgent image for Classic Full-Stack monitoring

The Dynatrace built-in registry only supports x86-64 architectures running Linux. As a consequence, we recommend that you explicitly set/override the architecture and operating system.

How to determine OneAgent image tag

The Dynatrace built-in registry provides the following OneAgent image tag formats:

* `latest`
* `latest-raw`
* `<major>.<minor>.<revision>`
* `<major>.<minor>.<revision>-raw`

For image replication, we recommend that you copy raw images (images with the tag suffix `-raw`).

To understand which OneAgent versions are available for replication, you can use the following Deployment APIs:

* [List available versions of OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.") to get an overview of available OneAgent versions.
* [View the latest version of OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "View the latest version of OneAgent via Dynatrace API."), if you want to understand the OneAgent version behind `latest` or automate OneAgent image replication.

The following examples show how OneAgent versions translate to image tags available in the Dynatrace built-in registry:

OneAgent version

OneAgent image tag

latest

**latest-raw**

1.283.114.20240129-173640

**1.283.114-raw**

Before executing the following command, be sure to replace `<tag-with-raw-suffix>` and `<environment-id>`:

```
skopeo copy --override-arch amd64 --override-os linux



docker://<your_environment_domain_name>/linux/oneagent:<tag-with-raw-suffix> \



docker://registry.my-company.com/dynatrace-oneagent-classic:<tag-with-raw-suffix>
```

For more information on configuring a DynaKube custom resource, see our examples of how to [use private registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

## Related topics

* [Use a private registry](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Verify Dynatrace image signatures](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures")


---


## Source: cluster-role-aggregation.md


---
title: ClusterRole aggregation for Kubernetes monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation
scraped: 2026-02-15T21:25:50.877707
---

# ClusterRole aggregation for Kubernetes monitoring

# ClusterRole aggregation for Kubernetes monitoring

* Latest Dynatrace
* 2-min read
* Updated on Dec 09, 2025

Dynatrace Operator version 1.8.0+

Starting with Operator version 1.8.0, the ActiveGate component uses a service account binding the `dynatrace-kubernetes-monitoring` ClusterRole. This ClusterRole is an **aggregated role** enabling simple and flexible configuration of assigned RBAC permissions. [1](#fn-1-1-def)

1

ClusterRole aggregation is a Kubernetes RBAC feature that allows you to combine multiple ClusterRoles into a single aggregated ClusterRole. The aggregating ClusterRole uses label selectors to identify which other ClusterRoles should be included. For more information, see [ClusterRole aggregation in Kubernetes documentationï»¿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#aggregated-clusterroles).

## Default permissions

By default, the Dynatrace Operator installation creates a `dynatrace-kubernetes-monitoring-default` ClusterRole that contains the standard set of permissions required for Kubernetes platform monitoring. This ClusterRole is automatically labeled with `rbac.dynatrace.com/aggregate-to-monitoring: "true"`, so its permissions are included in the aggregated role.

The default permissions are documented in the [security reference](/docs/ingest-from/setup-on-k8s/reference/security#activegate "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require") and cover standard monitoring of:

* Pods, deployments, StatefulSets, and other workload resources.
* Services and endpoints.
* Nodes and resource metrics.
* Events and cluster information.

## Extending the ClusterRole with additional permissions

To extend the monitoring functionality beyond the default permissions, create additional ClusterRoles with the aggregation label. Any ClusterRole with the label `rbac.dynatrace.com/aggregate-to-monitoring: "true"` is automatically aggregated, and its permissions are granted to the ActiveGate service account.

### Example: Allow monitoring of sensitive data

To enable monitoring of sensitive Kubernetes objects like Secrets and ConfigMaps, create a new ClusterRole:

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRole



metadata:



name: dynatrace-kubernetes-monitoring-sensitive



labels:



rbac.dynatrace.com/aggregate-to-monitoring: "true"



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

The `rbac.dynatrace.com/aggregate-to-monitoring: "true"` label is required for your ClusterRole to be aggregated. Without this label, the permissions are not granted to the ActiveGate.

The permissions are aggregated immediately after applying the ClusterRole and take effect without requiring a restart of Operator or ActiveGate pods.


---


## Source: edge-connect-provision.md


---
title: Provision EdgeConnect for Dynatrace environment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision
scraped: 2026-02-16T09:38:13.725014
---

# Provision EdgeConnect for Dynatrace environment

# Provision EdgeConnect for Dynatrace environment

* Latest Dynatrace
* 1-min read
* Published Dec 20, 2023

EdgeConnect facilitates secure interactions between applications, workflows, and internal systems within a Kubernetes environment. This guide provides detailed steps for provisioning EdgeConnect for a Dynatrace environment.

## 1. Create OAuth client

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **OAuth clients**.
2. Create an OAuth client with the following scopes.

   * `app-engine:edge-connects:connect`
   * `app-engine:edge-connects:write`
   * `app-engine:edge-connects:read`
   * `app-engine:edge-connects:delete`
   * `oauth2:clients:manage`
3. Save the ID, secret, and your Dynatrace account URN.

## 2. Create OAuth credentials secret

1. Create a secret with the OAuth credentials.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: edgeconnect-oauth



   namespace: dynatrace



   data:



   oauth-client-id: <base64 encoded client id>



   oauth-client-secret: <base64 encoded client secret>
   ```
2. Apply the secret.

   ```
   kubectl apply -f edgeconnect-oauth-secret.yaml
   ```

## 3. Configure EdgeConnect

1. Configure the EdgeConnect custom resource file with the `provisioner: true` and the `hostPatterns` properties. For the `resource` property, use the Dynatrace account URN that you got earlier.

   ```
   apiVersion: dynatrace.com/v1alpha2



   kind: EdgeConnect



   metadata:



   name: sample-edge-connect-name



   namespace: dynatrace



   spec:



   apiServer: "<environment-id>.apps.dynatrace.com"



   hostPatterns:



   - '*.mycompany.org'



   oauth:



   provisioner: true



   clientSecret: edgeconnect-oauth



   endpoint: https://sso.dynatrace.com/sso/oauth2/token



   resource: urn:dtaccount:<your-account-uuid>
   ```
2. Apply the EdgeConnect custom resource.

   ```
   kubectl apply -f edgeconnect.yaml
   ```

Rotating the OAuth credentials is not immediately reflected in the EdgeConnect deployment. This may lead to authentication issues until Dynatrace Operator reconciles the EdgeConnect deployment.

## Related topics

* [Configure and deploy EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.")


---


## Source: edge-connect.md


---
title: Set up EdgeConnect
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect
scraped: 2026-02-15T09:07:09.645857
---

# Set up EdgeConnect

# Set up EdgeConnect

* Latest Dynatrace
* 2-min read
* Published Oct 11, 2023

EdgeConnect facilitates secure interactions between applications, workflows, and internal systems within a Kubernetes environment. This guide provides information on how to deploy and configure EdgeConnect using Dynatrace.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create EdgeConnect**](#create-edgeconnect)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create OAuth credentials secret**](#create-secret)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure EdgeConnect**](#configure-edgeconnect)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Verify that EdgeConnect is up**](#check-edgeconnect)

## Step 1 Create EdgeConnect

To create EdgeConnect, follow the instruction provided in [Create a new EdgeConnect configuration](/docs/ingest-from/edgeconnect#createconfiguration "Use EdgeConnect to control how your apps and workflows interact with your internal systems.").

## Step 2 Create OAuth credentials secret

1. Create a secret to hold your OAuth credentials. The values for the OAuth client ID and secret should be obtained from the EdgeConnect configuration created in [Create EdgeConnect](#create-edgeconnect) step.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: edgeconnect-oauth



   namespace: dynatrace



   data:



   oauth-client-id: <base64 encoded client id>



   oauth-client-secret: <base64 encoded client secret>
   ```
2. Apply the secret.

   ```
   kubectl apply -f edgeconnect-oauth-secret.yaml
   ```

## Step 3 Configure EdgeConnect

1. Before applying the configuration, ensure you have all the necessary details. See the configuration fields in [EdgeConnect parameters for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters "List of configuration parameters for EdgeConnect.").
2. Create the EdgeConnect custom resource file. Ensure the value for `metadata.name` matches the name you used when creating the EdgeConnect configuration in step 1.

   ```
   apiVersion: dynatrace.com/v1alpha2



   kind: EdgeConnect



   metadata:



   name: sample-edge-connect-name



   namespace: dynatrace



   spec:



   apiServer: "<environment-id>.apps.dynatrace.com"



   replicas: 1



   oauth:



   clientSecret: edgeconnect-oauth



   endpoint: https://sso.dynatrace.com/sso/oauth2/token



   resource: urn:dtenvironment:<tenant>
   ```
3. Apply the EdgeConnect custom resource.

   ```
   kubectl apply -f edgeconnect.yaml
   ```

## Step 4 Verify that EdgeConnect is up

After configuring EdgeConnect, use the command below to check the status of your EdgeConnect.

```
kubectl get edgeconnects -n dynatrace
```

Ensure that the status displays `Running`.

```
NAME          APISERVER                             STATUS    AGE



sample-edge-connect-name   <environment-id>.apps.dynatrace.com   Running   16m
```

## Related topics

* [Configure and deploy EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.")


---


## Source: istio-deployment.md


---
title: Deploy Dynatrace alongside Istio
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment
scraped: 2026-02-16T21:14:23.962632
---

# Deploy Dynatrace alongside Istio

# Deploy Dynatrace alongside Istio

* Latest Dynatrace
* 10-min read
* Updated on Oct 22, 2025

This guide explains how Dynatrace components can be deployed alongside Istio. A Dynatrace deployment on Kubernetes contains several components that need to communicate with each other, with the Dynatrace cluster and other external resources.

For more information on communication of Dynatrace Operator and its managed components, see the [network traffic](/docs/ingest-from/setup-on-k8s/reference/network "Network traffic requirements for the Dynatrace Operator components in a Kubernetes cluster.") reference page.

## Limitations

* Istio injection into the Dynatrace Operator namespace is not supported.
* Istio spin-offs are currently not supported (for example, Maistra or OpenShift Service Mesh).
* Istio East-West (sidecar combined with ambient) deployment is not supported.

## Setup considerations

This guide covers two predefined configurations of Istio, chosen for their simplicity and common use cases. While Istio offers extensive customization options, these configurations serve as a starting point. This section explains the configuration scenarios and provides guidance on selecting the right Dynatrace setup that best suits your needs. Note that Dynatrace does not impose any limitations on how you configure Istio.

* **Default Istio configuration** Recommended  
  This represents the default deployment of Istio, meaning no special mesh configuration. It's basically the result of following the official [Istio installation guideï»¿](https://dt-url.net/hm03u3r).
  This means Istio is installed either via Helm or `istioctl` in sidecar mode with the CNI node agent.

  Follow the [setup guide for the default Istio configuration](#setup-guide-for-default-istio-configuration) if Istio is deployed accordingly.
* **Secure Istio configuration**  
  This represents a "secure" configuration of Istio. However, this does not mean that we consider this the best practice for security configuration in Istio or that this should be seen as a guide for securing Istio. This setup is based on settings that are most likely to influence the deployed Dynatrace components and their connections. This scenario assumes that Istio is deployed with strict mTLS and `outboundTrafficPolicy` set to `REGISTRY_ONLY`. These options severely limit the incoming and outgoing connections for workloads in the mesh.

  Choose this configuration if any point below applies:

  + If you have enabled mTLS in strict mode.
  + If you have an `outboundTrafficPolicy` set to `REGISTRY_ONLY`.

  If none of the points above apply, choose [Default Istio configuration](#setup-guide-for-default-istio-configuration).  
  Follow the [setup guide for the secure Istio configuration](#setup-guide-for-secure-istio-configuration) if Istio is deployed accordingly.

### Other deployment considerations

Disable injection of CNI pods

#### Disable injection of CNI pods

This is relevant to you if all of the following applies to your deployment:

* Not supported Dynatrace Operator is deployed inside the mesh.
* Istio is deployed using sidecars.
* Istio is configured to use the CNI component.
* You have not configured any namespace selector in the DynaKube that would exclude the `istio-system` namespace.

In all scenarios, you should exclude the Istio CNI pods from being injected by the Dynatrace Operator. Otherwise, when adding a new node to the cluster, it is possible that a deadlock situation will occur.

Both the CSI driver and Istio's CNI agent are DeamonSets, and will therefore be deployed on any (new) node in the cluster.

* The CSI driver pod will be injected by Istio with an init container that waits for the correct setup of the redirection rules needed for the proxy sidecar to work.
* The CNI pod will be injected by Dynatrace to include the required OneAgent binaries for instrumentation that are provided via a volume provisioned by the CSI driver on that Node.

This leads to a situation where both pods cannot start:

* The CNI pod is waiting for the CSI driver to become ready to provide the volume.
* The CSI pod is waiting for the CNI agent to provide the redirections for the proxy.

Also all other workloads that are target of either the Istio or Dynatrace injection and get scheduled on that Node will be affected and won't be able to start.

The easiest way to exclude the CNI pods from the injection by the Dynatrace Operator is to add the annotation `oneagent.dynatrace.com/inject: "false"`. For example, for a Helm deployment of Istio, add the following to the values of the `cni` chart:

```
cni:



podAnnotations:



oneagent.dynatrace.com/inject: "false"
```

Native sidecar support

#### Native sidecar support

Istio 1.28 deployed on a compatible Kubernetes cluster (>=1.29) will use native sidecar containers. This new type of sidecar container is currently not supported by Dynatrace Operator. Disable native sidecars in your Istio deployment by adding the following environment variable to the pilot deployment.

Example values for the Istio helm chart:

```
pilot:



...



env:



ENABLE_NATIVE_SIDECARS: false



...
```

## Setup guide for default Istio configuration

Because Dynatrace supports Istio in the default configuration, you only need to enable the `enableIstio` parameter in the [DynaKube](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."). However, you don't need to set this parameter if you don't plan to use a restrictive `outboundTrafficPolicy`.

When this parameter is enabled, Dynatrace Operator will deploy `ServiceEntries` and `VirtualServices` to enable communication from inside the mesh to all relevant Dynatrace components and the Dynatrace environment. The `ServiceEntries` and `VirtualServices` work regardless of whether Dynatrace Operator's namespace itself is part of the mesh (if no `discoveryfilter` is set in Istio).

This enables all workloads and OneAgents to connect to the ActiveGate instance and all required connections to the Dynatrace environment. Therefore, all Dynatrace features are expected to work.

`ServiceEntries` result in additional DNS queries executed by each sidecar proxy. This can put additional load on your DNS server.

To minimize the number of URLs, and therefore DNS queries, make sure the network zones in your Dynatrace environment are configured correctly. For a detailed setup description, see [Kubernetes network zone docs](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones#kubernetes-cluster-with-restricted-egress "Set up and use network zones in Kubernetes environments with the Dynatrace Operator.").

If this is not possible or sufficient in your environment, see [Istio DNS proxyingï»¿](https://dt-url.net/ab23uvy) for another possible mitigation.

### How `enableIstio` works

The `enableIstio` attribute is a convenience feature that automatically creates `ServiceEntries` and `VirtualServices` for connection endpoints required by:

* Dynatrace Operator: Uses `apiUrl` defined in DynaKube.
* ActiveGate: Uses the `/v1/deployment/installer/gateway/connectioninfo` endpoint.
* OneAgent injected into user containers: Uses the `/v1/deployment/installer/agent/connectioninfo`, which respects the `networkZone` attribute for routing.

Note that `enableIstio` attribute will not consider pre-existing `ServiceEntries` and `VirtualServices`. Using this attribute prematurely might lead to conflicts in Istio configurations. In complex setups, manual configuration may yield better outcomes.

Changes to the `enableIstio` attribute require you to remove and reapply your DynaKube for the update to take effect.

Manual configuration

Manual configuration of `ServiceEntries` and `VirtualServices` may be required in the following cases:

#### ActiveGate

* **Requirement**: Necessary if the ActiveGate pod is part of the mesh.
* **Configuration**: Manually configure `ServiceEntries` and `VirtualServices` based on the output of the `/v1/deployment/installer/gateway/connectioninfo` endpoint.

#### `cloudNativeFullstack` and `applicationMonitoring`

* **Requirement**: Necessary if injected user applications are part of the mesh.
* **Configuration**: Manually configure `ServiceEntries` and `VirtualServices` based on the output of the `/v1/deployment/installer/agent/connectioninfo` endpoint.

## Setup guide for secure Istio configuration

In such a restricted environment, and depending on your required Dynatrace features and other considerations, it might be necessary to create a few additional configuration rules for Istio. There are a few things to consider regarding the Dynatrace components when deciding how to deploy Dynatrace Operator.

* Even if routing is enabled on the ActiveGate, OneAgents will fall back to directly connecting to the Dynatrace environment if the ActiveGate is not reachable (for example because it's inside the mesh). That means no monitoring data is lost if some OneAgents can't connect to the ActiveGate because of the chosen deployment strategy.
* The monitoring modes `classicFullStack` or `cloudNativeFullStack` create pods with host networking enabled. That means those pods can never be part of the mesh, as Istio does not support pods with host networking. For `classicFullStack`, those pods handle all application metrics, while for `cloudNativeFullStack`, only host monitoring is affected.
* Some features of the ActiveGate might require direct connections to pods (for example, metric scraping). With mTLS enabled in Istio, direct connections to pod IPs are not possible. For a workaround for metric scraping, see [Istio metric merging](#metric-scraping-using-istio-metric-merging).

### Deployment outside the mesh

In this scenario, the least complex deployment is outside the mesh. You still have to enable the `enableIstio` parameter in the DynaKube. The possible downsides of this deployment might include:

* Communication from inside the mesh to the ActiveGate will not be secured by mTLS. However, the communication is still encrypted via HTTPS.
* The ActiveGate is not able to connect to any pod or service inside the mesh. If metric scraping is your only concern, see the [Metric scraping using Istio metric merging](#metric-scraping-using-istio-metric-merging) workaround (not applicable for Istio ambient).

Depending on whether most of your monitored workloads are part of the mesh or most of your targets for metric scraping are inside the mesh, deploying only the ActiveGate inside the mesh can be a more suitable option.

### ActiveGate deployment inside the mesh

The most compatible deployment option is to deploy only the ActiveGate inside the mesh. This deployment option makes the most sense if most of your monitored workloads are also part of the mesh or if you need the ActiveGate to directly connect to pods inside the mesh (for example, for Prometheus scraping).

1. Make sure that the Dynatrace Operator namespace is not labeled for Istio injection (`istio-injection` or `istio.io/dataplane-mode` label is not set).
2. Label the ActiveGate pods for Istio by adding the following to your DynaKube:

   Sidecar

   Ambient

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: your-dynakube-name



   spec:



   enableIstio: true



   activeGate:



   labels:



   sidecar.istio.io/inject: "true"
   ```

   Restart your ActiveGate pods to trigger the injection.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: your-dynakube-name



   spec:



   enableIstio: true



   activeGate:



   labels:



   istio.io/dataplane-mode: "ambient"
   ```
3. Optional You can enable communication from OneAgents outside the mesh to the ActiveGate by deploying the following `PeerAuthentication` resource:

   ```
   apiVersion: security.istio.io/v1



   kind: PeerAuthentication



   metadata:



   name: ag-no-mtls # <yourname>



   namespace: dynatrace-operator # <operator namespace>



   spec:



   mtls:



   mode: PERMISSIVE



   selector:



   matchLabels:



   app.kubernetes.io/managed-by: dynatrace-operator



   app.kubernetes.io/name: activegate
   ```

All communication to the ActiveGate will still be encrypted using HTTPS.

Configure Dynatrace Operator CSI driver with Istio in registry-only mode and custom codeModulesImage

### Configure Dynatrace Operator CSI driver with Istio in registry-only mode

When using Istio configured to `REGISTRY_ONLY` mode with the `codeModulesImage` field for CSI driver, you need to apply additional configuration to ensure proper communication with the image registry.

#### Prerequisites

* Istio is installed and configured in `REGISTRY_ONLY` mode.
* Not supported Dynatrace Operator CSI driver is injected with Istio.
* `codeModulesImage` field is specified in the CSI driver configuration.

#### Configure `ServiceEntry` for CSI driver

1. Create a `ServiceEntry`.

   The `ServiceEntry` configuration allows the Dynatrace Operator CSI driver to communicate with the specified image registry. Without this configuration, the image pull process will fail. See an example of `ServiceEntry` for `docker.io` below.

   ```
   apiVersion: networking.istio.io/v1



   kind: ServiceEntry



   metadata:



   name: codemodules-docker-io



   namespace: dynatrace



   spec:



   hosts:



   - index.docker.io



   - auth.docker.io



   - production.cloudflare.docker.com



   location: MESH_EXTERNAL



   ports:



   - name: https-443



   number: 443



   protocol: HTTPS



   resolution: DNS
   ```
2. Apply the `ServiceEntry`.

   Save and apply the above configuration to a file.

   ```
   kubectl apply -f serviceentry.yaml
   ```

## Metric scraping using Istio metric merging

[Dynatrace metric scraping](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.") is done via the ActiveGate and configured via annotations. This results in the ActiveGate connecting directly to the pods on the configured endpoint to scrape the metrics. As stated earlier, this direct connection does not work with strict mTLS.

Istio ambient mode does not support metric merging as it requires a sidecar proxy. However, in ambient mode it's possible for the ActiveGate to directly connect to the pod IPs and scrape the configured targets. Depending on your mTLS policy, this might only be possible for pods inside the mesh if the ActiveGate is also part of the mesh.

Istio provides a feature called [metric mergingï»¿](https://dt-url.net/5y43ufx) that uses the (widely adopted) `prometheus.io/...` annotations to configure an additional endpoint in the sidecar proxy that serves Istio and Envoy metrics as well as the application metrics defined by the annotations. This newly created endpoint is excepted from mTLS and therefore reachable from outside the mesh despite having mTLS in strict mode.

You can now point the Dynatrace annotations to this endpoint to scrape metrics of Istio and the application. If you don't want to scrape the additional Istio and Envoy metrics, you can exclude them by using the `metrics.dynatrace.com/filter` annotation and excluding `istio_*` and `envoy_*` metrics.

This way, an ActiveGate outside (or inside) the mesh can scrape the metrics from pods inside the mesh.

Example of all required annotations:

```
apiVersion: v1



kind: Pod



metadata:



annotations:



...



metrics.dynatrace.com/path: /stats/prometheus # Endpoint created by Istio



metrics.dynatrace.com/port: "15020" # Port of the Envoy sidecar



metrics.dynatrace.com/scrape: "true"



prometheus.io/path: /metrics # Metric endpoint of the application



prometheus.io/port: "8080" # Metric port of the application



prometheus.io/scrape: "true"



...
```

Keep in mind that Istio will rewrite the `prometheus.io/...` annotations to the generated endpoint and port when applying the above pod. That means that the resulting pod in the cluster will not match the applied YAML.

## Troubleshooting

Istio service registry

You can get all services known to Istio (a service registry) by executing the following command inside the `pilot` container of the `istiod` pod.

```
curl localhost:8080/debug/registryz
```

This dumps all known services as JSON. It should contain entries for the Dynatrace tenant and ActiveGate in the cluster.

If not, check if `enableIstio` is set to `true` in the DynaKube.

## Related topics

* [Configure OpenTelemetry tracing with Istio](/docs/ingest-from/opentelemetry/integrations/istio "Learn how to configure Istio on Kubernetes to deploy pre-configured proxy services for OpenTelemetry tracing.")


---


## Source: instrument-nginx.md


---
title: Instrument ingress-nginx
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx
scraped: 2026-02-16T21:12:45.448003
---

# Instrument ingress-nginx

# Instrument ingress-nginx

* Latest Dynatrace
* 1-min read
* Published Sep 02, 2021

The instructions below are relevant only for the [official Kubernetes ingress controller implementation from Googleï»¿](https://dt-url.net/xr03xh3).

* Derivatives from the official project, such as the [Bitnami ingress controllerï»¿](https://dt-url.net/ns03xjt), are not supported. However, you may instrument them manually by using the [Manual runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") for NGINX.
* The [ingress controller implementation from F5 NGINXï»¿](https://dt-url.net/ph43xrd) can be instrumented automatically; no manual steps are required.

The NGINX process of the official Kubernetes ingress-nginx controller container image can't be instrumented automatically. To manually instrument ingress-nginx on Kubernetes, follow the instructions below.

## Prerequisites

ARM64 architecture is not supported.

* OneAgent version 1.227+
* The pod name must contain the substring `ingress-nginx-` to ensure proper instrumentation of the NGINX binary. We recommend to maintain the default pod name `ingress-nginx-controller`.

## Instrument Kubernetes ingress-nginx

To instrument ingress-nginx on Kubernetes, you need to load the NGINX module manually via a ConfigMap.

Ensure that OneAgent is running and capable of instrumenting the ingress-nginx containers when applying changes to the ingress-nginx ConfigMap. If these conditions are not met, NGINX will fail to start.

1. Edit the ConfigMap.

   ```
   kubectl edit configmap ingress-nginx-controller
   ```
2. Add the following value to the `main-snippet` key (below `data`).

   Example:

   ```
   data:



   main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

   For `cloudNativeFullStack` and `applicationMonitoring` deployments, the path becomes:

   ```
   data:



   main-snippet: load_module /opt/dynatrace/oneagent-paas/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;
   ```

## Verify your configuration

If your pod isn't up and running, make sure that it hasn't exceeded either of the following:

* Its resource quota (especially for memory).
* The initial liveness/readiness probe timeouts. You might need to increase `initialDelaySeconds` for these probes.


---


## Source: k8s-api-monitoring.md


---
title: Kubernetes API Monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring
scraped: 2026-02-16T21:17:23.705849
---

# Kubernetes API Monitoring

# Kubernetes API Monitoring

* Latest Dynatrace
* 8-min read
* Updated on Dec 09, 2025

Dynatrace obtains information about Kubernetes entities and metadata by querying the Kubernetes API. This information is used for [out-of-the-box alerting for Kubernetes](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") and to provide all observability signals in a proper Kubernetes context within the Dynatrace platform, for example, by creating relationships among applications, (micro-)services, databases, and Kubernetes entities such as pods, namespaces, and nodes.

Dynatrace Operator manages the lifecycle of all Dynatrace components within a Kubernetes cluster and can be configured by deploying a DynaKube Custom Resource. Dynatrace ActiveGateâthe Dynatrace component required to monitor the Kubernetes APIâoffers a capability for Kubernetes API Monitoring.

Follow the steps below to enable Kubernetes API monitoring.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install Dynatrace Operator**](#install-dto)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure DynaKube**](#configure-dynakube)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect ActiveGate with Kubernetes API**](#connect-ag)

## Step 1 Install Dynatrace Operator

[Install Dynatrace Operator in any deployment mode](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")

## Step 2 Configure DynaKube

Configure the **ActiveGate** values of the DynaKube according to the [list of parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#ag "List the available parameters for setting up Dynatrace Operator on Kubernetes.") and add `kubernetes-monitoring` to the ActiveGate capabilities.

```
...



activeGate:



capabilities:



- routing



- kubernetes-monitoring



...
```

## Step 3 Connect ActiveGate with Kubernetes API

You have two options:

* Connect the containerized ActiveGate to a local Kubernetes API endpoint.
* Connect the containerized ActiveGate to the public Kubernetes API URL.

See below for instructions for both options.

### Connect to a local Kubernetes API endpoint

You can enable monitoring by connecting a containerized ActiveGate to a local Kubernetes API endpoint.

There are two ways to connect to the local Kubernetes API endpoint:

* Recommended [Let Dynatrace Operator automatically handle the connection](#auto)
* [Configure the connection manually](#manual)

See below for details on both methods.

Connect automatically

Connect manually

This feature flag is deprecated and enabled by default starting from Dynatrace Operator version 0.13.0.

To connect automatically to the local Kubernetes API endpoint

1. Make sure to enable the **Read entities**, **Read settings**, and **Write settings** permissions (API v2) for your access token (see [Access tokens and permissions](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster")).
2. Make sure that you have the `kubernetes-monitoring` capability enabled in your DynaKube custom resource.
3. Add the following annotation (see example below).

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



   spec:



   ...



   activeGate:



   capabilities:



   - kubernetes-monitoring
   ```

   After adding this annotation, the name of the cluster displayed in Dynatrace will be the same as the DynaKube custom resource where the annotation is configured. You can change the cluster name displayed in Dynatrace by adding the `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"` annotation as well.

   Example with custom cluster name:

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



   feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"



   spec:



   ...



   activeGate:



   capabilities:



   - kubernetes-monitoring
   ```
4. Apply your configuration.

   To disable the configuration, remove the annotation.

To connect to a local Kubernetes API endpoint manually, you only need to provide the unique Kubernetes cluster ID (the uuid of the kube-system namespace). The containerized ActiveGate then identifies the unique cluster ID and sends it over to Dynatrace.

#### Step 1 Get the Kubernetes cluster ID

Run the command below and grab the UID from the output.

Kubernetes

OpenShift

```
kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
```

```
oc get namespace kube-system -o jsonpath='{.metadata.uid}'
```

#### Step 2 Provide the Kubernetes cluster ID in Dynatrace

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Select **Connect manually**.
3. On the Kubernetes cluster connection settings page, provide a **Name**, and then turn on **Connect containerized ActiveGate to local Kubernetes API endpoint**.
4. For **Kubernetes cluster ID**, enter the UID obtained earlier.
5. Select **Save changes** to save your configuration.

   You can save your configuration even if the ActiveGate isn't ready to connect, and finish the configuration later. To verify if it's ready, select **Test configuration**.

### Connect to the public Kubernetes API

To connect to the public Kubernetes API, follow the instructions that apply to your Kubernetes version:

* [Kubernetes version 1.24+](#k8s-new)
* [Kubernetes version earlier than 1.24](#k8s-old)

#### Kubernetes version 1.24+

1. Get the Kubernetes API URL.

   Kubernetes

   OpenShift

   ```
   kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   ```
   oc config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   If you set `enableIstio` to `true` in the [DynaKube custom resourceï»¿](https://dt-url.net/dynakube-samples), use the command below to get the Kubernetes API URL:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Create a file named `token-secret.yaml` with the following content:

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: dynatrace-activegate



   annotations:



   kubernetes.io/service-account.name: "dynatrace-activegate"



   type: kubernetes.io/service-account-token
   ```
3. Apply the file to create the `dynatrace-activegate` secret.

   Kubernetes

   OpenShift

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```

   ```
   oc apply -n dynatrace -f token-secret.yaml
   ```
4. Get the bearer token.

   Kubernetes

   OpenShift

   ```
   kubectl get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```
5. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** and select **Connect manually**.
6. On the Kubernetes cluster connection settings page, provide a **Name**, the **Kubernetes API URL**, and the **Bearer token** for the Kubernetes cluster.
7. Select **Save changes**.

#### Kubernetes version earlier than 1.24

1. Get the Kubernetes API URL.

   Kubernetes

   OpenShift

   ```
   kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   ```
   oc config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   If you set `enableIstio` to `true` in the [DynaKube custom resourceï»¿](https://dt-url.net/dynakube-samples), use the command below to get the Kubernetes API URL:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Get the bearer token.

   Kubernetes

   OpenShift v3.x

   OpenShift v4.x

   ```
   kubectl get secret $(kubectl get sa dynatrace-activegate -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret $(oc get sa dynatrace-activegate -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret $(oc get sa dynatrace-activegate -o jsonpath='{.secrets[1].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Special instructions for Rancher distributions to get the API URL and the bearer token

   For **Rancher distributions** of Kubernetes, you need to use the bearer token and API URL **of the Rancher server**, because this server manages and secures traffic to the Kubernetes API server. Follow the steps below.

   1. Get the **Kubernetes API URL**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Configure a user.

      In the Rancher web UI, either create a new user or use an existing user to associate with the token. We recommend creating a new user.
   3. Set permissions.

      Make sure the user has either **Owner** or **Custom** permissions to the cluster you want to monitor.

      **Recommended:** select **Custom** permissions, and be sure to select these two roles: **View all Projects** and **View Nodes**.
   4. Create an API key.

      Go to **API & Keys** and create a key either for your specific account (enter your cluster name) or for all clusters (enter **No scope**). For security reasons, we recommend selecting the first option.

      Newly created keys display four fields. Make sure to use the content of the field called **Bearer token** to set up the connection to the Kubernetes API described in the next section.
3. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** and select **Connect manually**.
4. On the Kubernetes cluster connection settings page, provide a **Name**, the **Kubernetes API URL**, and the **Bearer token** for the Kubernetes cluster.

   For Rancher distributions, you need the bearer token that was created in the Rancher web UI, as described in **Special instructions for Rancher distributions to get the API URL and the bearer token** above.
5. Select **Save changes**.

## Other Options

* If you can't use Dynatrace Operator, you can [deploy ActiveGate directly as a StatefulSet](/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.") (not recommended).
* If you want to monitor several Kubernetes clusters with one ActiveGate and don't need to separate networks for administrative or operational traffic, you can [install an ActiveGate on a virtual machine using a conventional installer](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.").

Dynatrace recommends to use the containerized ActiveGate for Kubernetes API monitoring

## FAQ

Can I change settings for Kubernetes API monitoring?

You can change Kubernetes cluster connection and monitoring settings at any time from your Kubernetes cluster details page.

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster, and then select **Actions** > **Settings**.
3. Adjust your settings, and then select **Save changes**.

How can I delete the Kubernetes Platform Monitoring configuration for a Kubernetes cluster?

To delete the connection to a local Kubernetes API endpoint

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster, and then select **Actions** > **Settings**.
3. Select **Use defaults**, and then select **Save changes**.

When does the ActiveGate get updated?

ActiveGate is updated automatically on pod restart whenever there is a new version available, unless the image version is specified in `cr.yaml`.


---


## Source: ag-resource-limits.md


---
title: Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits
scraped: 2026-02-16T21:31:27.043732
---

# Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case

# Sizing guide for Dynatrace ActiveGates in the Kubernetes monitoring use-case

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Jan 26, 2026

Setting appropriate resource requests (and limits, when needed) keeps Dynatrace ActiveGate instances stable and predictable. This guide details sizing methods based on scale and workload.

A stable, healthy ActiveGate ensures continuous gapâfree monitoring data.

## Understanding the sizing drivers

Actual required resources increase with:

* **Number of pods**âThe primary sizing driver is the number of monitored pods. The resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of pods primarily due to increased data processing and storage needs. As the number of monitored pods grows, the ActiveGate handles more entity data, events, and metrics, resulting in higher CPU load for ingestion and processing, as well as increased memory for caching pod-related information. This is the primary sizing driver, with consumption scaling proportionally to pod count.
* **Prometheus metrics volume**âThe number of Prometheus annotated pods directly correlates with increased resource requirements for Dynatrace ActiveGate, primarily through higher CPU consumption. As the count of annotated pods rises, the volume of scraped metrics grows, demanding more CPU cycles for collection, aggregation, and forwarding tasks. Memory impact is secondary, as metrics are forwarded to the Dynatrace tenant without long-term storage on the ActiveGate, though it scales proportionally with peak ingest rates.
* **Number of nodes**âThe resource consumption (CPU and memory) for Dynatrace ActiveGate components scales with the number of nodes primarily due to increased monitoring overhead and load from node-level system pods. As the node count grows, the ActiveGate must handle more system-level data collection, entity processing, and event ingestion, leading to higher computational demands. This is a secondary driver compared to the number of pods, but it contributes proportionally to overall resource needs, especially in larger clusters where node-level monitoring adds cumulative load.
* **Number of clusters monitored**âA single ActiveGate can monitor multiple clusters, however, this deployment pattern is **not recommended**. Monitoring multiple clusters with a single ActiveGate increases both CPU and memory requirements proportionally for each additional cluster, as the ActiveGate must handle more data processing, entity management, and event ingestion across clusters. This can lead to resource contention, higher risk of throttling or OOM restarts, and potential gaps in monitoring data.

**We recommend a setup where one containerized ActiveGate is monitoring one Kubernetes cluster.**

This ensures optimal performance and reliability. This approach simplifies troubleshooting, avoids resource contention, and ensures predictable scaling as each ActiveGate handles only one clusterâs workload.

## Signs of an unhealthy ActiveGate

These symptoms indicate exhausted resources and potential data loss.

### Gaps in monitoring data

ActiveGate collects different types of data independently (for example, Prometheus metrics, Kubernetes events, entities). If one collection task takes longer than 1 minute, only that data type experiences a gap for that window. Other collection tasks continue operating normally.

* Metrics will have missing data point for the given minute.
* Events for the given collection timeframes are not available at all.
* Entities may not reflect the latest updates or may be missing at all if short-living.

### Heavy CPU throttling

Sustained high throttling means insufficient CPU. Heavy throttling can cause gaps. Minor throttling is usually harmless.
If the throttling affects the pod serving the monitoring ActiveGate this can cause data gaps.

### Outâofâmemory restarts

If the ActiveGate is OOM-killed, data becomes unavailable until it restarts. After a restart, repeated OOM kills are likely to occur.

## Monitoring and validation

The following indicators can be tracked to understand if the ActiveGate is in a healthy operational state.

* **CPU usage vs requests**âIf CPU utilization consistently exceeds 85% increase the CPU request.
* **CPU throttling** (container\_cpu\_cfs\_throttled\_periods\_total / periods)âIf throttling exceeds 10% consistently, increase the CPU request.
* **Memory working set vs request**âIf usage consistently exceeds 80%, increase the memory request.
* **ActiveGate restart count**âAfter an OOM-based restart, promptly raise the configured memory to prevent recurrence.
* **Processing duration / cycle time** âIf the execution time of pipelines consistently exceeds 50 - 60 seconds, increase the CPU request. The pipeline execution time also depends on the amount of ingested data and other factors.
* **Garbage collection times**âIncreasing garbage collection times are a clear indicator for an under-provisioned ActiveGate.

Metrics reference

The indicators for unhealthy ActiveGates are as following:

| Indicator | Platform metrics for validation | Classic metrics for validation | Detail level |
| --- | --- | --- | --- |
| CPU usage | `dt.kubernetes.container.cpu_usage` | `builtin:kubernetes.node.cpu_usage` `builtin:kubernetes.workload.cpu_usage` | ActiveGate pod |
| CPU requests | `dt.kubernetes.resourcequota.requests_cpu` | `builtin:kubernetes.node.requests_cpu` `builtin:kubernetes.workload.requests_cpu` | ActiveGate pod |
| CPU throttling | `dt.kubernetes.container.cpu_throttled` | `builtin:kubernetes.workload.cpu_throttled` `builtin:kubernetes.node.cpu_throttled` | ActiveGate pod |
| Memory working set | `dt.kubernetes.container.memory_working_set` | `builtin:kubernetes.node.memory_working_set` `builtin:kubernetes.workload.memory_working_set` | ActiveGate pod |
| Memory requests | `dt.kubernetes.resourcequota.requests_memory` | `builtin:kubernetes.node.requests_memory` `builtin:kubernetes.workload.requests_memory` | ActiveGate pod |
| Restart count | `dt.kubernetes.container.restarts` | `builtin:kubernetes.container.restarts` | ActiveGate pod |
| OOM kills | `dt.kubernetes.container.oom_kills` | `builtin:kubernetes.container.oom_kills` | ActiveGate pod |
| Processing duration | `dt.sfm.active_gate.kubernetes.pipeline_duration` | `dsfm:active_gate.kubernetes.pipeline_duration` | ActiveGate ID |
| Garbage collection times | `dt.sfm.active_gate.jvm.gc.major_collection_time` | `dsfm:active_gate.jvm.gc.major_collection_time` | ActiveGate ID |

### Increasing resources

Start with the recommended values below.

1. Verify ActiveGate health using the monitoring indicators.
2. Adjust resources as needed:

   * Increase memory in 2Gi increments.
   * Increase CPU in 500m increments.
3. Adjust request first and in a later step adjust the limits.

   * Regarding CPU: Use limits only if required by policy.

## Using a dedicated ActiveGate for Kubernetes platform monitoring

Splitting ActiveGate responsibilities into two groups is recommended: One group handling everything related to Kubernetes platform monitoring, including KSPM, and the other managing Agent traffic routing, telemetry ingest, and extensions. This separation provides several advantages:

* **Isolation**âResource contention in one module doesn't affect the other. A spike in OneAgent traffic won't slow down Kubernetes metrics collection, and vice versa.
* **Independent scaling**âTraffic forwarding and platform monitoring have fundamentally different scaling characteristics:

  + **Kubernetes platform monitoring** can only scale vertically â when cluster size grows, you increase CPU and memory resources for the corresponding ActiveGate.
  + **OneAgent traffic routing** can be horizontally scaled â when OneAgent traffic increases, additional routing ActiveGate replicas help distribute and share the load.

  Separate ActiveGates let you scale each dimension independently without overâprovisioning resources. For example, you can add 3 more routing replicas to handle increased application traffic without unnecessarily increasing resources for platform monitoring.
* **Easier troubleshooting** â When issues occur, you can immediately identify whether they originate from platform monitoring or OneAgent traffic, reducing diagnosis time.

## Sizing ActiveGate

Scenarios are established based on the number of pods that are monitored by a single ActiveGate. The necessary resources can be taken from the following tables.

* **Scenario S**: <1000 pods
* **Scenario M**: 1000â5000 pods
* **Scenario L**: 5000â20000 pods

  This guide does not cover environments with more than 20,000 pods. Due to the many variables involved, providing precise recommendations for such large-scale setups isnât feasible. As a starting point, you can use the guidance for the L scenario and gradually increase resources until stable gap-free monitoring is established.
  For tailored advice, we recommend reaching out to Dynatrace Support to ensure the best configuration for your environment.

### Secondary factors

#### Node count

As the number of nodes in your Kubernetes cluster increases, the ActiveGate needs more CPU and memory resources to handle the extra monitoring workload. This includes processing data from node-level system components and events, which adds up proportionally.
We group node counts into these categories for sizing guidance:

* Up to 25 nodes
* Up to 100 nodes
* Up to 500 nodes

If your cluster has more than 100 nodes, you'll need to adjust the resource allocations upward to account for the additional demands, ensuring stable and gap-free monitoring. For clusters beyond 500 nodes, consult Dynatrace Support for tailored recommendations.

#### Amount of Prometheus metrics scraped

Dynatrace supports up to 1000 pod exporters, with each exporter able to provide up to 1000 metrics. If your environment approaches these limits, you'll need to increase the resources allocated to the ActiveGate to ensure reliable performance.

### ActiveGate for Kubernetes platform monitoring

All the following use cases have actually the same requirements on the ActiveGate taking over the Kubernetes platform monitoring part.

* Kubernetes platform monitoring only
* Kubernetes platform monitoring + Application observability
* Kubernetes platform monitoring + Full-stack observability

| Pod count | CPU resource | Memory resource |
| --- | --- | --- |
| < 1000 ( Small ) | requests: 200m (limits: 1000m) | requests: 6Gi limits: 6Gi |
| < 5000 ( Medium ) | requests: 1000m (limits: 2000m) | requests: 10Gi limits: 10Gi |
| < 20000 ( Large ) | requests: 2000m (limits: 4000m) | requests: 12Gi limits: 12Gi |

We recommend running ActiveGates without CPU limits.

### ActiveGate for OneAgent traffic routing and proxying

The second ActiveGate does not actively participate in Kubernetes platform monitoring but is instead used as a router/proxy on behalf of data streams originating from the OneAgent.
We recommend to use separate ActiveGates for traffic forwarding and platform monitoring. Traffic forwarding scales horizontally by adding replicas. Kubernetes monitoring itself does not scale horizontally; instead increase resources.

This setup is required in the following use-cases:

* Kubernetes platform monitoring + Application observability
* Kubernetes platform monitoring + Full-stack observability

| Pod count | CPU resource | Memory resource | replicas |
| --- | --- | --- | --- |
| < 1000 ( Small ) | requests: 250m (limits: 1000m) | requests: 2Gi limits: 2Gi | 3 |
| < 5000 ( Medium ) | requests: 500m (limits: 2000m) | requests: 4Gi limits: 4Gi | 3 |
| < 20000 ( Large ) | requests: 1000m (limits: 4000m) | requests: 6Gi limits: 6Gi | 6 |

We recommend running ActiveGates without CPU limits.

## Getting started

The following examples apply the reasoning of splitting the ActiveGates into units with separate concerns. One ActiveGate is responsible for Kubernetes platform monitoring and Kubernetes security posture management, whereas the 2nd ActiveGate is then responsible for agent traffic routing, telemetry ingest and extensions.
Adjust requests (and limits if required) to fit your environment.

### Kubernetes platform monitoring

This Dynakube resource declares the ActiveGate that is used for the Kubernetes platform monitoring.

CPU limits are commented out. We recommend defining requests only so the ActiveGate can use additional CPU when available. If limits are required, set them equal to or higher than requests.

This snippet includes configuration for Kubernetes Security Posture Management. It's a complementing, opt-in security feature next to Kubernetes platform monitoring.

DynaKube for Kubernetes platform monitoring

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: k8s-monitoring



namespace: dynatrace



annotations:



feature.dynatrace.com/k8s-app-enabled: "true"



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



tokens: <SECRET NAME>



metadataEnrichment:



enabled: true



# Link to api reference for further information: https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



activeGate:



capabilities:



- kubernetes-monitoring



resources:



requests:



cpu: 1000m



memory: 10Gi



limits:



# cpu: 2000m



memory: 10Gi



#kspm:



#mappedHostPaths:



#- /boot



#- /etc



#- /proc/sys/kernel



#- /sys/fs



#- /sys/kernel/security/apparmor



#- /usr/lib/systemd/system



#- /var/lib



#templates:



#kspmNodeConfigurationCollector:



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector



#tag: 1.5.2
```

### OneAgent, telemetry ingest and other features

This Dynakube resource declares the ActiveGate that is taking over the OneAgent traffic routing function and other features (except Kubernetes platform monitoring and KSPM).

CPU limits are commented out. We recommend defining requests only so the ActiveGate can use additional CPU when available. If limits are required, set them equal to or higher than requests.

This snippet includes configurations for log monitoring, extensions and telemetry ingest. These sections are considered optional on a per-section basis.

DynaKube for OneAgent, telemetry ingest and other features

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: agents



namespace: dynatrace



# Link to api reference for further information: https://docs.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



tokens: <SECRET NAME>



metadataEnrichment:



enabled: true



oneAgent:



applicationMonitoring: {}



activeGate:



capabilities:



- routing



- debugging



resources:



requests:



cpu: 1000m



memory: 6Gi



limits:



# cpu: 4000m



memory: 6Gi



replicas: 6



#customProperties:



#value: |



#[otlp_ingest]



#otlp_ingest_enabled = true



#logMonitoring: {}



#extensions: {}



#telemetryIngest:



#protocols:



#- jaeger



#- otlp



#- statsd



#- zipkin



#serviceName: telemetry-ingest



templates:



#logMonitoring:



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-logmodule



#tag: <>



#tolerations:



#- effect: NoSchedule



#  key: node-role.kubernetes.io/master



#  operator: Exists



#- effect: NoSchedule



#  key: node-role.kubernetes.io/control-plane



#  operator: Exists



#extensionExecutionController:



#imageRef:



#repository: <ENVIRONMENTID>/dynatrace/linux/dynatrace-eec



#tag: latest



#otelCollector:



#replicas: 1



#imageRef:



#repository: public.ecr.aws/dynatrace/dynatrace-otel-collector



#tag: <tag>
```


---


## Source: dto-auto-update.md


---
title: Auto-update for Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update
scraped: 2026-02-16T21:24:42.234335
---

# Auto-update for Dynatrace Operator

# Auto-update for Dynatrace Operator

* Latest Dynatrace
* 2-min read
* Published Mar 25, 2024

Dynatrace Operator manages and auto-updates the components it deploys. To achieve a similar effect for Dynatrace Operator itself, we recommend using GitOps and open-source tools.

## Recommended setup

* Keep the Dynatrace Operator configuration in a Git repository.
* Use [ArgoCDï»¿](https://dt-url.net/hi037z9) to deploy the configuration from the Git repository into the Kubernetes environment.
* Implement [Renovateï»¿](https://dt-url.net/vn237h6) to automatically update the Git repository with the latest Dynatrace Operator configurations.

## Automated update workflow

The workflow outlined below is a direct result of the recommended setup, ensuring that Dynatrace Operator is automatically kept up to date in your Kubernetes environment.

1. ArgoCD deploys the configuration from the Git repository into the Kubernetes environment.
2. Renovate detects a new release of Dynatrace Operator and updates the version in the Git repository.
3. ArgoCD notices the change in the Git repository and updates Dynatrace Operator in the Kubernetes environment accordingly.

### Deploy with ArgoCD

[Argoï»¿](https://dt-url.net/wt4379d) offers a suite of open-source tools for Kubernetes app deployment and management. ArgoCD, a continuous delivery tool, is used to keep the Dynatrace Operator configuration in sync with the Kubernetes cluster.

After you set up ArgoCD in your cluster, create an `ApplicationSet` YAML that specifies the source Helm chart for Dynatrace Operator, the version you want to deploy, and the target environment for the deployment.

ArgoCD ApplicationSet example

```
# For exact syntax refer to the official ArgoCD documentation



apiVersion: argoproj.io/v1alpha1



kind: ApplicationSet



metadata:



name: dynatrace-operator



spec:



generators:



...



template:



...



spec:



...



source:



repoURL: https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable



chart: dynatrace-operator



targetRevision: <version>
```

### Automate updates with Renovate

Renovate automates the updating of dependencies in Git repositories. Integrating Renovate into your workflow ensures that the Dynatrace Operator version specified in your `ApplicationSet` is always up to date. Use the [Renovate guideï»¿](https://dt-url.net/67637gq) for instructions on updating ArgoCD configurations.

## Related topics

* [Manage Dynatrace deployments using GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops "How to deploy Dynatrace Operator and DynaKube using GitOps.")


---


## Source: using-gitops.md


---
title: Manage Dynatrace deployments using GitOps
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops
scraped: 2026-02-16T21:14:17.302129
---

# Manage Dynatrace deployments using GitOps

# Manage Dynatrace deployments using GitOps

* Latest Dynatrace
* 4-min read
* Published Mar 25, 2024

With many companies today adopting GitOps for streamlined Kubernetes deployments, there's a growing interest in applying these practices to Dynatrace components. This guide focuses on deploying Dynatrace Operator with GitOps tools and setting up monitoring efficiently using the DynaKube custom resource (CR), aligning with modern deployment strategies.

## Using ArgoCD

This section discusses deploying Dynatrace Operator and applying a DynaKube CR using [ArgoCDï»¿](https://dt-url.net/hi037z9). Additionally, it outlines options and tips for flexible integration with ArgoCD.

The following three points describe Dynatrace deployment options outlined by the subsections and combinations of them.

1. Individually [Deploy Dynatrace Operator](#deploy-dynatrace-operator) and [Apply DynaKube CR](#apply-dynakube-custom-resource) via ArgoCD Applications
2. Apply ArgoCD's [App of Apps pattern](#applying-the-app-of-apps-pattern)
3. Use [multiple sources](#using-multiple-sources-for-an-argocd-application-beta-feature) for an ArgoCD Application (beta feature)

This guide was developed and tested with ArgoCD version 2.10.3.

### Deploy Dynatrace Operator

The following ArgoCD Application defines Dynatrace Operator deployment using the OCI-based Helm chart from Amazon ECR:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynatrace-operator



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



source:



repoURL: public.ecr.aws/dynatrace



chart: dynatrace-operator



targetRevision: 1.0.0



helm: {}
```

For deployment customization via Helm values, please refer to ArgoCD's [Helm user guideï»¿](https://argo-cd.readthedocs.io/en/stable/user-guide/helm/).

The Application CR can be applied in the following ways:

* Directly via *kubectl*
* By [applying the App of Apps pattern](#applying-the-app-of-apps-pattern)

#### Multi-cluster deployments via ArgoCD ApplicationSet

To use ApplicationSet CRs for multi-cluster deployments, use the Application CR from above as a template and integrate it into an ApplicationSet CR according to [ArgoCD's official documentationï»¿](https://argo-cd.readthedocs.io/en/stable/operator-manual/applicationset/#the-applicationset-resource).

### Apply DynaKube custom resource

The following ArgoCD Application references a Git repository holding a DynaKube CR under the specified filepath:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynakube



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



source:



repoURL: <git-reopository-url>



targetRevision: <revision>



path: <path-to-dynakube-dir>
```

Replace the `repoURL`, `targetRevision`, and `path` source fields with meaningful values before applying the Application CR in either of these ways:

* Directly via *kubectl*
* By [applying the App of Apps pattern](#applying-the-app-of-apps-pattern)

For details on DynaKube CR configuration, see the [deployment modes](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") documentation.

### Apply the App of Apps pattern

ArgoCD's [App Of Apps patternï»¿](https://dt-url.net/s963lbz) describes a very common approach in the ArgoCD community enabling automatic cluster bootstrapping. In combination with [Sync Phases and Wavesï»¿](https://argo-cd.readthedocs.io/en/stable/user-guide/sync-waves/), the App of Apps pattern provides sequential control over Application synchronization required for deploying Dynatrace Operator before applying a DynaKube CR [1](#fn-1-1-def).

Add the `argocd.argoproj.io/sync-wave` annotation with the respective value to the Application CRs from the above sections as illustrated in the following snippet:

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



annotations:



argocd.argoproj.io/sync-wave: "0"



name: dynatrace-operator



namespace: argocd



spec:



...



---



apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



annotations:



argocd.argoproj.io/sync-wave: "10"



name: dynakube



namespace: argocd



spec:



...
```

Both Application CRs are meant to be applied via the App of Apps pattern (which requires a parent Application CR).

1

[Creating Custom Resource Definitions (CRDs)ï»¿](https://dt-url.net/8g23lou) installed via the Helm chart can take several seconds, leading to the possibility that the initial application of the DynaKube CR will fail. To circumvent the given race condition, we recommend [configuring ArgoCD for the use of App of Appsï»¿](https://dt-url.net/ci03l8w) by changing the health assessment logic for Applications. Alternatively, automatic retries of synchronizations can be configured.

### Use multiple sources for an ArgoCD Application (beta feature)

Multiple sources for an Application is an ArgoCD beta feature and is subject to change in backwards-incompatible ways, according ArgoCD documentation.

[Multiple sources for an Applicationï»¿](https://argo-cd.readthedocs.io/en/stable/user-guide/multiple_sources/) enables you to use a single ArgoCD Application for deployment of Dynatrace Operator and DynaKube CR.
Additionally, the feature allows Helm value files to be sources from a Git repository other than the Helm chart itself, which was not possible in ArgoCD before.

```
apiVersion: argoproj.io/v1alpha1



kind: Application



metadata:



name: dynatrace



namespace: argocd



spec:



project: default



destination:



server: https://kubernetes.default.svc



namespace: dynatrace



sources:



- repoURL: public.ecr.aws/dynatrace



chart: dynatrace-operator



targetRevision: 1.0.0



helm:



valueFiles:



- $values/<path-to-dynatrace-operator-values-file>



- repoURL: <git-repository-url>



targetRevision: HEAD



ref: values



- repoURL: <git-repository-url>



targetRevision: HEAD



path: <path-to-dynakube-dir>



syncPolicy:



retry: # sample retry configuration; for details, see footnote below



limit: 5



...



...
```

Before applying, replace all placeholders with meaningful values and configure automatic retries[2](#fn-2-2-def).

2

[Creating Custom Resource Definitions (CRDs)ï»¿](https://dt-url.net/id43ley) installed via the Helm chart can take several seconds, leading to the possibility of the initial application of the DynaKube resource failing. To ensure successful deployment, you need to configure retries by specifying a sync policy.

## Auto-update for Dynatrace Operator

For configuring automatic updates for Dynatrace Operator, see [Auto-update of Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach."), which explains integrating GitOps with dependency automation tools.

## Related topics

* [Auto-update for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/dto-auto-update "Enable automatic updates of Dynatrace Operator following a GitOps approach.")


---


## Source: k8s-metadata-telemetry-enrichment.md


---
title: Metadata enrichment of all telemetry originating from Kubernetes
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment
scraped: 2026-02-16T21:13:08.637777
---

# Metadata enrichment of all telemetry originating from Kubernetes

# Metadata enrichment of all telemetry originating from Kubernetes

* Latest Dynatrace
* 7-min read
* Updated on Feb 05, 2026

## Prerequisites

* Dynatrace Operator is installed and running in your Kubernetes cluster.
* A valid DynaKube is applied to your cluster.
* [Metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") is enabled.

## Use cases

* Enhance your metrics, logs, trace data, events and entities with additional information using Kubernetes namespace annotations and labels.
* Enhance your metrics, logs, trace data, events and entities with additional information using OpenTelemetry environment variables
* Enriched data can be used for [defining access control to users](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context"), or for solving [Cost Allocation](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.") in DPS.
* Enriched data can be used for pipeline routing, bucket segmentation, segmentation, and filtering.

## Security context and Cost Allocation

In Dynatrace, you can set up [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") for fine-grained restrictions on the data level. By default, you can use `k8s.namespace.name` and `k8s.cluster.name`, but sometimes this is not enough and you need a more fine grained way to set up your boundaries.

You might already have defined such boundaries for yourself and defined them as Kubernetes labels or annotations. This feature enables you to use these at the source for your [security context](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context") in Dynatrace. If you have not done so already, we recommend to either use cluster or namespace name or set up a dedicated annotation for your Kubernetes workloads that serves as your security context.

Similarly Dynatrace provides a solution for [Cost Allocation](/docs/license/cost-allocation#assign-cost-centers-and-products-in-kubernetes-application-monitoring-deployments "Learn how to allocate costs to cost centers and products.") in DPS. You might already have the necessary data like department and product available in your existing Kubernetes labels or annotations. Even if not you might find it very convenient to setup up Cost Allocation as a Kubernetes annotation or label, which is what Dynatrace recommends. This feature then enables you to use these labels and annotations as the means to solving [Cost Allocation](/docs/license/cost-allocation#assign-cost-centers-and-products-in-kubernetes-application-monitoring-deployments "Learn how to allocate costs to cost centers and products.") in DPS.

The following attributes are supported:

* [`dt.security_context`](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")
* [`dt.cost.costcenter`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")
* [`dt.cost.product`](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.")

## Domain tags

To streamline tasks like bucket selection, segmentation, filtering, and problem routing, Dynatrace allows you to enrich your telemetry data using existing Kubernetes namespace labels or annotations. These tags are made available as domain-specific fields, such as `k8s.namespace.label.your_key` or `k8s.namespace.annotation.your_key`.

## Which data will be enriched

Data

Domain tags

Security Context

Cost Allocation

OneAgent metrics

JMX/PMI metrics collected via OneAgent

Planned

Service metrics

Kubernetes platform metrics

ActiveGate 1.331

Prometheus metrics

Planned

Planned - ActiveGate 1.333

Planned - ActiveGate 1.333

OTLP metrics

ActiveGate 1.331

Metrics collected by OpenTelemetry Collector

Logs collected by OpenTelemetry Collector

Logs collected by OneAgent log module

Logs collected by FluentBit

Smartscape Kubernetes entities

ActiveGate 1.331

Service metrics

OneAgent events

Kubernetes events

ActiveGate 1.331

## Enrichment options

Depending on the specific use case, the following enrichment options are supported:

### Use settings to use existing namespace labels and annotations (recommended)

We recommend this option, as it is the only option that enriches all signals, including Kubernetes platform metrics, events, and entitiesâunlike environment variables or manual pod annotations. Use Kubernetes enrichment rules to leverage your existing namespace labels and annotations.
The tenant configuration is applied to all Kubernetes clusters by default. However, you can override it for specific clusters if needed.

Hint: If you setup your rules before you deploy your Dynakube, you don't need to wait 45 minutes for the rules to be propagated.

1. Go to **Kubernetes App** > **Namespace** > Select your namespace to have an overview of your existing namespace labels.

   ![Namespace details opened in the K8s App, pointing to the current namespace labels](https://dt-cdn.net/images/namespace-labels-1997-2a0370e1ef.png)
2. Go to **Settings** > **Cloud and virtualization** > **Kubernetes Telemetry Enrichment**.
3. Select **Add rule**.
4. Select `Annotation` or `Label` in the **Metadata type** dropdown.
5. Enter the namespace annotation/label key in the **Source** field, following [Kubernetes conventionsï»¿](https://dt-url.net/2c02sbn):
6. To use the key of the annotation or label as field name, turn on **Enrich telemetry with label/annotation directly**.

   ![Enrich telemetry with label/annotation directly](https://dt-cdn.net/images/enrich-telemetry-with-label-annotation-directly-693-b6d33d539e.png)
7. For remapping, turn off **Enrich telemetry with label/annotation directly** and choose a value from the **Target** dropdown.

   ![Enrichment Settings for Remapping](https://dt-cdn.net/images/enrichment-settings-for-remapping-663-33a85e6613.png)
8. Select **Save changes**.
9. After creating or modifying rules, allow up to 45 minutes for the changes to take effect. Once this time has passed, restart your pods.
10. Navigate to your data and verify that the metadata is successfully enriched.

![Log details with enriched metadata](https://dt-cdn.net/images/enriched-log-652-55590251f6.png)

### Use dedicated Dynatrace metadata pod annotations

This works automatically for OneAgent and OpenTelemetry code-change scenarios.

This option is intended for scenarios where namespace labels or annotations cannot be used as a source. If both methods are present, manual annotations take precedence.

Unlike the settings-based approach, manually added pod annotations do not provide full enrichment. They will not enrich Kubernetes metrics, Kubernetes events, or entities.
For Oneagent metrics and service metrics to be enriched with these attributes, they must follow the convention `k8s.namespace.<label>/<annotation>.<key>: <value>`.

For comprehensive enrichment, the settings-based approach is recommended.

You might create the following annotations at the pod level:

```
metadata:



annotations:



metadata.dynatrace.com/dt.security_context: sre



metadata.dynatrace.com/dt.cost.costcenter: it_services



metadata.dynatrace.com/dt.cost.product: fin_app



metadata.dynatrace.com/k8s.namespace.label.domain: finance
```

The following attributes will enrich the data:

```
dt.security_context: sre



dt.cost.costcenter: it_services



dt.cost.product: fin_app



k8s.namespace.label.domain: finance
```

## OpenTelemetry setup

For OTLP setups without OneAgent, additional steps for signal enrichment are required. This can be achieved either by modifying your code to parse metadata files provided by the operator or by using environment variables.

### Enable automatic OpenTelemetry OTLP exporter configuration (recommended)

[Automatic OpenTelemetry OTLP exporter configuration](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.") is the recommended option for OTLP setups without OneAgent injection, as it provides enrichment comparable to the OneAgent case. Enable it in your DynaKube to automatically enrich your telemetry with Dynatrace metadata. This feature is available for all OpenTelemetry supported languages.

### Enrich via code changes

This option is suitable for standalone OTLP setups without OneAgent injection. For optimal results, enrich your OTLP telemetry by parsing Dynatrace metadata files and adding the metadata directly in your code, as outlined in [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."). You can find code samples in our OpenTelemetry section, like here for [Java](/docs/ingest-from/opentelemetry/walkthroughs/java/java-manual#add-telemetry-signals-manually "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.").
This approach provides enrichment comparable to the OneAgent case.

### Enrich via environment variable

If modifying your code isn't feasible, you can use the [`OTEL_RESOURCE_ATTRIBUTES`ï»¿](https://dt-url.net/ne03unx) environment variable for enrichment. However, this method has limitations: configuration can be complex, and certain properties, like k8s.container.name and tags, must be set as static strings.

1. Create a config map for cluster level attributes

1. Store DynaKube name

```
DYNAKUBE="dynakube" # set this to the name of your DynaKube / kubectl get dynakube -n dynatrace
```

2. Get `k8s.cluster.uid`

```
K8S_CLUSTER_UID="$(kubectl get dynakube -o jsonpath='{.status.kubeSystemUUID}' -n dynatrace $DYNAKUBE)"
```

3. Get `k8s.cluster.name`

```
K8S_CLUSTER_NAME="$(kubectl get dynakube -o jsonpath='{.status.kubernetesClusterName}' -n dynatrace $DYNAKUBE)"
```

4. Get Kubernetes entity `dt.entity.kubernetes_cluster`

```
DT_ENTITY_KUBERNETES_CLUSTER="$(kubectl get dynakube -o jsonpath='{.status.kubernetesClusterMEID}' -n dynatrace $DYNAKUBE)"
```

5. Create config map in the target namespace

```
kubectl create configmap dynatrace-metadata \



--from-literal K8S_CLUSTER_UID=$K8S_CLUSTER_UID \



--from-literal K8S_CLUSTER_NAME=$K8S_CLUSTER_NAME \



--from-literal DT_ENTITY_KUBERNETES_CLUSTER=$DT_ENTITY_KUBERNETES_CLUSTER \



--namespace <YOUR_NAMESPACE>
```

2. Set K8s attributes via downward API on Pod

Adapt your Kubernetes pod specification by adding the following environment variables. You can include these in your Kubernetes Deployment or Pod manifest.

Tags and `k8s.container.name` cannot be set via downward API.
It needs to be provided as a static string.

```
envFrom:



- configMapRef:



name: dynatrace-metadata



optional: false



env:



- name: K8S_CONTAINER_NAME



value: "" # replace with actual container name



- name: K8S_POD_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.name



- name: K8S_POD_UID



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.uid



- name: K8S_POD_NAMESPACE



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.namespace



- name: K8S_WORKLOAD_KIND



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/k8s.workload.kind'] # only works when metadata enrichment is enabled



- name: K8S_WORKLOAD_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/k8s.workload.name'] # only works when metadata enrichment is enabled



- name: K8S_NODE_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: spec.nodeName



- name: DT_SECURITY_CONTEXT # only works when automatic security context enrichment is configured



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/dt.security_context']



- name: DT_COST_PRODUCT # only works when automatic cost product enrichment is configured



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/dt.cost.product']



- name: DT_COST_COSTCENTER # only works when automatic cost center enrichment is configured



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.annotations['metadata.dynatrace.com/dt.cost.costcenter']
```

3. Add attributes to `OTEL_RESOURCE_ATTRIBUTES`

This example shows all our recommended attributes. Remove attributes that are not in use.

```
- name: OTEL_RESOURCE_ATTRIBUTES



value: k8s.cluster.name=$(K8S_CLUSTER_NAME),k8s.cluster.uid=$(K8S_CLUSTER_UID),k8s.node.name=$(K8S_NODE_NAME),k8s.workload.name=$(K8S_WORKLOAD_NAME),k8s.workload.kind=$(K8S_WORKLOAD_KIND),k8s.pod.name=$(K8S_POD_NAME),k8s.pod.uid=$(K8S_POD_UID),k8s.namespace.name=$(K8S_POD_NAMESPACE),k8s.container.name=$(K8S_CONTAINER_NAME),dt.entity.kubernetes_cluster=$(DT_ENTITY_KUBERNETES_CLUSTER),dt.security_context=$(DT_SECURITY_CONTEXT),dt.cost.costcenter=$(DT_COST_COSTCENTER),dt.cost.product=$(DT_COST_PRODUCT)
```

To learn how to enrich signals with release metadata using the `OTEL_RESOURCE_ATTRIBUTES` environment variable, refer to the [version detection strategies](/docs/deliver/release-monitoring/version-detection-strategies#otel_resource_attributes "Metadata for version detection in different technologies") for detailed guidance.

## Limitations

* Limit of 20 rules per configuration scope.
* After creating or modifying rules, allow up to 45 minutes for the changes to take effect. Once this time has passed, restart your pods.
* Manually set `metadata.dynatrace.com` pod annotations take precedence.
* Manually added attributes (anything other than `dt.security_context`, `dt.cost.costcenter`, or `dt.cost.product`) do not enrich any Kubernetes metrics or Kubernetes events.
* The settings-based approach does not work in conjunction with manually applied dedicated pod annotations. Using both simultaneously may cause conflicts, leading to unexpected behavior.

## Troubleshooting

### Verify the rule definition

* Confirm that each rule points to the correct **metadata type** (`label` vs. `annotation`).
* Ensure the **source key** in the rule exactly matches the key that exists on the namespace.

### Check that the source metadata really exists

* Open the namespace in the **Dynatrace Kubernetes app** and look for the expected labels/annotations.
* Alternatively, run

  ```
  kubectl get namespace <name> -o yaml
  ```

and inspect the `metadata.labels` and `metadata.annotations` sections.

### Validate that metadata enrichment is turned on

* The feature works only if `metadataEnrichment` is enabled in your **DynaKube** configuration.
* If you specify a `namespaceSelector` in the DynaKube, make sure it matches the namespace you are testing.

### Confirm that enrichment reached the pods

* Inspect any pod in the namespace:

  ```
  kubectl get pod <pod-name> -o yaml
  ```
* Look for annotations that start with `metadata.dynatrace.com/â¦`. Their presence means the metadata is enriched.

## Examples

Rules

Rules in `builtin:kubernetes.generic.metadata.enrichment`

```
"rules":



[



{



# rule #1



"type": "Annotation",



"source": "metadata.example.com/team",



"target": "dt.security_context"



},



{



# rule #2



"type": "Label",



"source": "department",



"target": "dt.cost.costcenter"



},



{



# rule #3



"type": "Label",



"source": "app/name",



"target": "dt.cost.product"



}



{



# rule #4



"type": "Label",



"source": "domain",



"primaryGrailTag": "true"



}



]
```

Namespace

Your existing namespace labels and annotations:

```
metadata:



annotations:



metadata.example.com/team: sre



labels:



department: it_services



app/name: fin_app



domain: finance
```

Pod

The Operator will create pod annotations:

```
metadata:



annotations:



metadata.dynatrace.com:|



{



"dt.security_context": "sre",



"dt.cost.costcenter": "it_services",



"dt.cost.product": "fin_app",



"k8s.namespace.label.domain": "finance"



}
```

Telemetry

The following attributes will be enriched on the data:

```
dt.security_context: sre



dt.cost.costcenter: it_services



dt.cost.product: fin_app



k8s.namespace.label.domain: finance
```

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")
* [Configure enrichment directory](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.")


---


## Source: metadata-enrichment.md


---
title: Configure enrichment directory
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
scraped: 2026-02-16T21:13:05.592514
---

# Configure enrichment directory

# Configure enrichment directory

* Latest Dynatrace
* 2-min read
* Published Jul 28, 2023

Metadata enrichment is an optional feature that enhances monitoring signals by adding supplementary metadata.

## What you will learn

This guide explains how to configure and enable metadata enrichment in the Dynatrace Operator. By following this guide, you will be able to:

* Verify the correct application of enriched metadata for various use cases.
* Associate logs and metrics with specific entities like pods, processes, etc.

## Prerequisites

* Dynatrace Operator is installed and running in your Kubernetes cluster.
* A valid DynaKube is applied to your cluster.

## Steps

1. Enable metadata enrichment

To enable metadata enrichment, modify your DynaKube YAML:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true
```

If using additional features like ActiveGate or OneAgent, your configuration may include:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true



oneAgent:



cloudNativeFullStack: (or other mode)



...



activeGate:



capabilities:



- routing



...
```

2. Use namespace selector

Optional

To limit metadata enrichment to specific namespaces, add the `namespaceSelector` field to your configuration:

```
metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



team: finance
```

This configuration applies metadata enrichment only to namespaces labeled with `team=finance`.

3. Verify enrichment directory

Confirm that the enrichment directory in injected Pods reflects the metadata attributes you've configured.

Enrichment files are stored in the following directory: `/var/lib/dynatrace/enrichment`

This directory holds the enrichment files `dt_metadata.json` and `dt_metadata.properties`

The files look like this:

1. dt\_metadata.properties

```
dt.entity.kubernetes_cluster=<kubernetes-cluster-id>



dt.kubernetes.cluster.id=<cluster-id>



dt.kubernetes.workload.kind=<workload-kind>



dt.kubernetes.workload.name=<workload-name>



k8s.cluster.name=<cluster-name>



k8s.cluster.uid=<cluster-uid>



k8s.container.name=<container-name>



k8s.namespace.name=<namespace-name>



k8s.node.name=<node-name>



k8s.pod.name=<pod-name>



k8s.pod.uid=<pod-uid>



k8s.workload.kind=<workload-kind>



k8s.workload.name=<workload-name>
```

2. dt\_metadata.json

```
{



"dt.entity.kubernetes_cluster": "<kubernetes-cluster-id>",



"dt.kubernetes.cluster.id": "<cluster-id>",



"dt.kubernetes.workload.kind": "<workload-kind>",



"dt.kubernetes.workload.name": "<workload-name>",



"k8s.cluster.name": "<cluster-name>",



"k8s.cluster.uid": "<cluster-uid>",



"k8s.container.name": "<container-name>",



"k8s.namespace.name": "<namespace-name>",



"k8s.node.name": "<node-name>",



"k8s.pod.name": "<pod-name>",



"k8s.pod.uid": "<pod-uid>",



"k8s.workload.kind": "<workload-kind>",



"k8s.workload.name": "<workload-name>"



}
```

**Please note:** The enrichment files will be used for various enrichments automatically, if there is OneAgent enabled. If there is no OneAgent enabled, the enrichment files and their content have to be used manually.

For more details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

## Learn more

* [Dynatrace documentation: metadata enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")

By following these steps, you can fully leverage metadata enrichment to enhance your Kubernetes monitoring and achieve better insights.


---


## Source: migrate-dk-v1beta1-v1beta4.md


---
title: Migration of DynaKube v1beta1 to v1beta4
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4
scraped: 2026-02-15T09:13:38.282977
---

# Migration of DynaKube v1beta1 to v1beta4

# Migration of DynaKube v1beta1 to v1beta4

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta1` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.

## Support lifecycle

### v1beta1

**Introduced in**: Dynatrace Operator version 0.3.0

**Deprecated in**: Dynatrace Operator version 1.6.0

**Last supported in**: Dynatrace Operator version 1.6.2

### v1beta4

**Introduced in**: Dynatrace Operator version 1.5.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Replaced feature flags

#### Dedicated `metadataEnrichment` section

The feature flag for enabling metadata enrichment (`feature.dynatrace.com/metadata-enrichment: true/false`) was moved to a dedicated field:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



enabled: true # replaces feature.dynatrace.com/metadata-enrichment: true



#...
```

#### Dedicated `dynatraceApiRequestThreshold` field

The feature flag for controlling how often Dynatrace Operator can ping the Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`) was moved to a dedicated field:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



dynatraceApiRequestThreshold: 10 # replaces feature.dynatrace.com/dynatrace-api-request-threshold: "10"



#...
```

#### Dedicated `secCompProfile` field for OneAgent

The feature flag that controls which seccomp profile the OneAgent DaemonSet uses (`feature.dynatrace.com/oneagent-seccomp-profile:example`) has been moved to a dedicated field:

Host monitoring

Classic fullstack

Cloud native fullstack

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



hostMonitoring:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



classicFullStack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

#### New CSI mount timeout feature flag

The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Moved fields

#### `spec.namespaceSelector`

The `spec.namespaceSelector` field was moved to each feature subsection that it affects.

Cloud native fullstack

Application monitoring

Metadata enrichment

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



applicationMonitoring:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

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
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

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

### Removed fields

#### `spec.applicationMonitoring.useCSIDriver`

The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.

The CSI driver is now used when installed as part of the Dynatrace Operator installation.

#### `spec.kubernetesMonitoring`

The deprecated field `spec.kubernetesMonitoring` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:

**Before**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



kubernetesMonitoring:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**After**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- kubernetes-monitoring #<-- explicitly enable Kubernetes monitoring



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

#### `spec.routing`

The deprecated field `spec.routing` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:

**Before**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



routing:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**After**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- routing #<-- explicitly enable routing



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```


---


## Source: migrate-dk-v1beta1-v1beta5.md


---
title: Migration of DynaKube v1beta1 to v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5
scraped: 2026-02-15T21:29:07.246476
---

# Migration of DynaKube v1beta1 to v1beta5

# Migration of DynaKube v1beta1 to v1beta5

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 30, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta1` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.

## Support lifecycle

### v1beta1

**Introduced in**: Dynatrace Operator version 0.3.0

**Deprecated in**: Dynatrace Operator version 1.6.0

**Last supported in**: Dynatrace Operator version 1.6.2

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Prepare for v1beta1 apiVersion removal

Notice

DynaKube CRD v1beta1 apiVersion will be removed in a future release. We recommend that you prepare for this ahead of time.
User action will be required when upgrading from Dynatrace Operator version 1.1.0 and earlier.

Query the current storage version of the DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Query the stored versions of the DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

If the **stored versions list** contains versions that will be removed with the CRD update, **user intervention is required**.

Make sure that the old apiVersion is no longer referenced by any manifest. This includes resources that load manifests from external sources, like Helm releases or ArgoCD applications.
When using GitOps, always check the source that manifests are synced from, because diffing may take conversion into account.

To ensure that the Kubernetes storage backend no longer contains outdated DynaKube objects, we recommend updating them in place.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do



namespace=${item%/*}



name=${item#*/}



kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -



done
```

Do not use the command `kubectl apply`, because it only writes data when changes are detected.

Once the old apiVersion is no longer referenced, it is safe to update the CRD status.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Replaced feature flags

#### Dedicated `metadataEnrichment` section

The feature flag for enabling metadata enrichment (`feature.dynatrace.com/metadata-enrichment: true/false`) was moved to a dedicated field:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



enabled: true # replaces feature.dynatrace.com/metadata-enrichment: true



#...
```

#### Dedicated `dynatraceApiRequestThreshold` field

The feature flag for controlling how often Dynatrace Operator can ping the Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`) was moved to a dedicated field:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



dynatraceApiRequestThreshold: 10 # replaces feature.dynatrace.com/dynatrace-api-request-threshold: "10"



#...
```

#### Dedicated `secCompProfile` field for OneAgent

The feature flag that controls which seccomp profile the OneAgent DaemonSet uses (`feature.dynatrace.com/oneagent-seccomp-profile:example`) has been moved to a dedicated field:

Host monitoring

Classic fullstack

Cloud native fullstack

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



hostMonitoring:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



classicFullStack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

#### New CSI mount timeout feature flag

The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Moved fields

#### `spec.namespaceSelector`

The `spec.namespaceSelector` field was moved to each feature subsection that it affects.

Cloud native fullstack

Application monitoring

Metadata enrichment

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



applicationMonitoring:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

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
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

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

### Removed fields

#### `spec.applicationMonitoring.useCSIDriver`

The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.

The CSI driver is now used when installed as part of the Dynatrace Operator installation.

#### `spec.kubernetesMonitoring`

The deprecated field `spec.kubernetesMonitoring` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:

**Before**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



kubernetesMonitoring:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**After**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- kubernetes-monitoring #<-- explicitly enable Kubernetes monitoring



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

#### `spec.routing`

The deprecated field `spec.routing` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:

**Before**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



routing:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**After**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- routing #<-- explicitly enable routing



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```


---


## Source: migrate-dk-v1beta2-v1beta4.md


---
title: Migration of DynaKube v1beta2 to v1beta4
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4
scraped: 2026-02-15T21:25:27.203240
---

# Migration of DynaKube v1beta2 to v1beta4

# Migration of DynaKube v1beta2 to v1beta4

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta2` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.

## Support lifecycle

### v1beta2

**Introduced in**: Dynatrace Operator version 1.2.0

**Deprecated in**: Dynatrace Operator version 1.6.0

**Last supported in**: Dynatrace Operator version 1.6.2

### v1beta4

**Introduced in**: Dynatrace Operator version 1.5.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Replaced feature flags

#### New CSI mount timeout feature flag

The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

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
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

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

### Removed fields

#### `spec.applicationMonitoring.useCSIDriver`

The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.

The CSI driver is now used when installed as part of the Dynatrace Operator installation.


---


## Source: migrate-dk-v1beta2-v1beta5.md


---
title: Migration of DynaKube v1beta2 to v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5
scraped: 2026-02-16T21:28:22.251881
---

# Migration of DynaKube v1beta2 to v1beta5

# Migration of DynaKube v1beta2 to v1beta5

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 30, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta2` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.

## Support lifecycle

### v1beta2

**Introduced in**: Dynatrace Operator version 1.2.0

**Deprecated in**: Dynatrace Operator version 1.6.0

**Last supported in**: Dynatrace Operator version 1.6.2

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Prepare for v1beta2 apiVersion removal

Notice

DynaKube CRD v1beta2 apiVersion will be removed in a future release. We recommend that you prepare for this ahead of time.
User action will be required when upgrading from Dynatrace Operator version 1.3.0 and earlier.

Query the current storage version of the DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Query the stored versions of the DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

If the **stored versions list** contains versions that will be removed with the CRD update, **user intervention is required**.

Make sure that the old apiVersion is no longer referenced by any manifest. This includes resources that load manifests from external sources, like Helm releases or ArgoCD applications.
When using GitOps, always check the source that manifests are synced from, because diffing may take conversion into account.

To ensure that the Kubernetes storage backend no longer contains outdated DynaKube objects, we recommend updating them in place.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do



namespace=${item%/*}



name=${item#*/}



kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -



done
```

Do not use the command `kubectl apply`, because it only writes data when changes are detected.

Once the old apiVersion is no longer referenced, it is safe to update the CRD status.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Replaced feature flags

#### New CSI mount timeout feature flag

The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

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
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

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

### Removed fields

#### `spec.applicationMonitoring.useCSIDriver`

The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.

The CSI driver is now used when installed as part of the Dynatrace Operator installation.


---


## Source: migrate-dk-v1beta3-v1beta5.md


---
title: Migration of DynaKube v1beta3 to v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5
scraped: 2026-02-16T09:38:25.570498
---

# Migration of DynaKube v1beta3 to v1beta5

# Migration of DynaKube v1beta3 to v1beta5

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta3` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.

## Support lifecycle

### v1beta3

**Introduced in**: Dynatrace Operator version 1.3.0

**Deprecated in**: Dynatrace Operator version 1.6.0

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

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
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

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


---


## Source: migrate-dk-v1beta4-v1beta5.md


---
title: Migration of DynaKube v1beta4 to v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5
scraped: 2026-02-16T21:27:31.288039
---

# Migration of DynaKube v1beta4 to v1beta5

# Migration of DynaKube v1beta4 to v1beta5

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 22, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta4` to `apiVersion: dynatrace.com/v1beta4` of the `DynaKube`.

## Support lifecycle

### v1beta4

**Introduced in**: Dynatrace Operator version 1.5.0

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Renamed fields

#### `spec.activeGate.persistentVolumeClaim`

The `spec.activeGate.persistentVolumeClaim` field has been renamed to `spec.activeGate.volumeClaimTemplate`. The functionality remains the same.

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

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
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

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


---


## Source: migrate-dk-v1beta5-v1beta6.md


---
title: Migration of DynaKube v1beta5 to v1beta6
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6
scraped: 2026-02-15T21:29:13.428580
---

# Migration of DynaKube v1beta5 to v1beta6

# Migration of DynaKube v1beta5 to v1beta6

* Latest Dynatrace
* Reference
* 5-min read
* Published Jan 20, 2026

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta5` to `apiVersion: dynatrace.com/v1beta6` of the DynaKube.

## Support lifecycle

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

### v1beta6

**Introduced in**: Dynatrace Operator version 1.8.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Moved fields

#### `spec.extensions`

The `spec.extensions` field was moved to `spec.extensions.prometheus` to accommodate the new `spec.extensions.databases` field. The functionality remains the same.


---


## Source: classic-to-app-monitoring.md


---
title: Migrate from classic full-stack to application monitoring mode
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring
scraped: 2026-02-16T21:25:27.670767
---

# Migrate from classic full-stack to application monitoring mode

# Migrate from classic full-stack to application monitoring mode

* Latest Dynatrace
* 3-min read
* Updated on Sep 05, 2025

Dynatrace Operator version 1.0.0+

This guide describes the steps required to migrate your Dynatrace deployment from classic full-stack monitoring to [application monitoring mode](/docs/ingest-from/setup-on-k8s/how-it-works#auto "In-depth description on how the deployment on Kubernetes works.").

## Advantages

To only monitor selected applications on Kubernetes, application monitoring offers a flexible approach with the following benefits:

* The application monitoring mode, similar to the cloud native full stack mode, prevents race conditions that can occur when OneAgent DaemonSet pods and monitored application pods start simultaneously.
* By leveraging Kubernetes concepts such as admission webhooks and CSI driver for Code Module injection, application monitoring mode reduces the required privileges for OneAgent.

### Considerations and implications

* When switching to application monitoring, previously deployed OneAgents will get deactivated and deep monitoring of applications will stop. Consequently, restarting all application pods that require deep monitoring becomes mandatory. Restarting these pods ensures that applications are reinjected, allowing deep monitoring to resume.
* In application monitoring mode, container monitoring rules are ignored. Instead, [label selectors](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") should be employed to precisely manage OneAgent injection.
* Log monitoring requires [additional setup](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.").

## Migrate to application monitoring mode

This section provides all the information needed to migrate from classic to application monitoring mode.

Using CRI-O container runtime

The standard migration procedure described below requires OneAgent version 1.281 or higher for Kubernetes clusters using CRI-O as their container runtime, so you need to upgrade OneAgents accordingly before continuing with the steps below.

If that upgrade cannot be performed, follow the [Running CRI-O with OneAgent versions 1.279 or earlier](#running-crio) procedure for an alternative migration flow, and then return to step 1 of this procedure.

1. Recommended

   Update installation with CSI driver included:

   Helm

   Manifest

   ```
   helm upgrade dynatrace-operator oci://docker.io/dynatrace/dynatrace-operator \



   --atomic \



   --csidriver.enabled="true" \ # By default CSI driver is enabled



   --namespace dynatrace
   ```

   **Kubernetes**

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes-csi.yaml
   ```

   **OpenShift**

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/openshift-csi.yaml
   ```
2. Reconfigure (existing) DynaKube for application monitoring mode:

   The following side-by-side comparison outlines how to reconfigure a DynaKube CR from classic full-stack to application monitoring:

   Classic full-stack monitoring

   Application monitoring

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   classicFullStack:



   args:



   - "--set-host-group=<host-group>"



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   For further information on how to configure DynaKube for application monitoring mode, visit the [deployment guide](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") or [DynaKube parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "List the available parameters for setting up Dynatrace Operator on Kubernetes."). Alternatively, download the [DynaKube custom resource sampleï»¿](https://dt-url.net/0w036dz) for application monitoring from GitHub and adapt the DynaKube custom resource according to your requirements.
3. Apply the DynaKube custom resource:

   Run the command below to apply the DynaKube custom resource. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f dynakube.yaml
   ```

   This action will lead to the removal of OneAgents in classic full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter.
4. Wait for code modules to become ready:

   Dynatrace Operator picks up the changes in the DynaKube custom resource and ensures code modules are available on each node.

   The CSI driver emits Kubernetes events attached to the DynaKube custom resource when the code modules are ready and available on each node. Wait until an event has been logged for each node before proceeding with the next step.
5. Restart application workloads:

   Restart all application workloads promptly to trigger code module injection and enable deep monitoring minimizing monitoring outages.

#### Running CRI-O with OneAgent versions 1.279 or earlier

This section outlines the migration procedure for Kubernetes clusters utilizing a CRI-O container runtime and running OneAgent version 279 or earlier.

It is necessary to remove CRI-O hooks installed and utilized for OneAgent injection in classic full-stack mode. For additional details on CRI-O hooks, refer to this [Red Hat blog postï»¿](https://dt-url.net/fq039v2).

Show step-by-step instructions

Follow these instructions to successfully migrate from classic full-stack mode:

1. Delete DynaKube custom resource:

   Delete the DynaKube configured in classic full-stack mode by running the following command:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   This action will lead to the removal of OneAgents in classic full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter. Additionally, if Kubernetes monitoring is configured in the DynaKube custom resource, Kubernetes monitoring will stop instantly with the removal of the ActiveGate.
2. Wait for the OneAgent pods to terminate.
3. Follow the instructions in the [Cleanup nodes](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Upgrade and uninstallation procedures for Dynatrace Operator") section to remove Dynatrace CRI-O hooks from all Linux nodes.
4. Continue with step 1 of the [standard migration procedure](#migrate).

## Changes in Kubernetes resources

The migration impacts several Kubernetes resources, altering their functions or introducing new components to support the application monitoring mode. Key changes include:

Component

classic full-stack

Application monitoring

Dynatrace Oneagent

* Deployed as a DaemonSet
* Collect host metrics on nodes
* Inject code modules into application pods

* Not present

Dynatrace Webhook Server

* Validates DynaKube definitions

* Validates DynaKube definitions
* Inject code modules into application pods by modifying pod definitions

[Dynatrace Operator CSI driver](/docs/ingest-from/setup-on-k8s/how-it-works#csi-driver "In-depth description on how the deployment on Kubernetes works.")

Optional

* Not present

* Deployed as a DaemonSet
* Optimizes the download of code modules to speed up pod injection and reduce storage consumption


---


## Source: classic-to-cloud-native.md


---
title: Migrate from classic full-stack to cloud-native full-stack mode
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native
scraped: 2026-02-16T21:28:08.735169
---

# Migrate from classic full-stack to cloud-native full-stack mode

# Migrate from classic full-stack to cloud-native full-stack mode

* Latest Dynatrace
* 4-min read
* Updated on Sep 05, 2025

Dynatrace Operator version 1.0.0+

This guide describes the steps required to migrate your Dynatrace deployment from classic full-stack to the [cloud-native full-stack mode](/docs/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.").

## Advantages

The cloud-native full-stack deployment mode represents a major advancement in security, utilizing cloud native methods for OneAgent injection. This approach addresses two key limitations found in the traditional full stack mode:

* The cloud-native full-stack mode prevents race conditions that can occur when OneAgent DaemonSet pods and monitored application pods start simultaneously.
* By leveraging Kubernetes concepts such as admission webhooks and CSI driver for Code Module injection, cloud-native full-stack monitoring reduces the required privileges for OneAgent.

### Considerations and implications

* When switching to cloud-native full-stack monitoring, previously deployed OneAgents will get deactivated and deep monitoring of applications will stop. Consequently, the restart of all application pods requiring deep monitoring becomes mandatory. Restarting these pods will ensure that applications are reinjected, allowing deep monitoring to resume.
* In cloud-native full-stack mode, Host IDs are determined differently, leading to the temporary presence of both new and old hosts in the host list screens. Old host entities and their associated data follow the data retention policy defined by Dynatrace, remaining accessible for the specified duration.
* In cloud-native full-stack mode, container monitoring rules are ignored. Instead, [label selectors](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") should be employed to precisely manage OneAgent injection.

## Migrate to cloud-native full-stack

This section provides all the information needed to migrate from classic to cloud-native full-stack mode.

Using CRI-O container runtime

The standard migration procedure described below requires OneAgent version 1.281 or higher for Kubernetes clusters using CRI-O as their container runtime, so you need to upgrade OneAgents accordingly before continuing with the steps below.

If that upgrade cannot be performed, follow the [Running CRI-O with OneAgent versions 1.279 or earlier](#running-crio) procedure for an alternative migration flow, and then return to step 1 of this procedure.

1. Update installation with CSI driver included:

   Helm

   Manifest

   ```
   helm upgrade dynatrace-operator oci://docker.io/dynatrace/dynatrace-operator \



   --atomic \



   --csidriver.enabled="true" \ # By default CSI driver is enabled



   --namespace dynatrace
   ```

   **Kubernetes**

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/kubernetes-csi.yaml
   ```

   **OpenShift**

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.8.1/openshift-csi.yaml
   ```
2. Reconfigure (existing) DynaKube for cloud-native full-stack mode:

   The following side-by-side comparison outlines how to reconfigure a DynaKube CR from classic full-stack to cloud-native full-stack monitoring:

   Classic full-stack monitoring

   Cloud-native full-stack monitoring

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   classicFullStack: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   cloudNativeFullStack: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   For further information on how to configure DynaKube for cloud-native full-stack mode, see the comparison below, visit the [deployment guide](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes") or [DynaKube parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-cloudnativefullstack "List the available parameters for setting up Dynatrace Operator on Kubernetes."). Alternatively, download the [DynaKube custom resource sampleï»¿](https://dt-url.net/9n636jg) for cloud-native full-stack from GitHub and adapt the DynaKube custom resource according to your requirements.
3. Apply the DynaKube custom resource:

   Run the command below to apply the DynaKube custom resource. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f dynakube.yaml
   ```

   This action will lead to the removal of OneAgents in classic full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter.
4. Wait for OneAgents to become ready:

   The Dynatrace Operator will pick up the changes in the DynaKube custom resource and ensure new OneAgents are available on each node.
5. Restart application workloads:

   Restart all application workloads promptly to trigger OneAgent injection and enable deep monitoring preventing/minimizing monitoring outages.

#### Running CRI-O with OneAgent versions 1.279 or earlier

This section outlines the migration procedure for Kubernetes clusters utilizing a CRI-O container runtime and running OneAgent version 279 or earlier.

It is necessary to remove CRI-O hooks installed and utilized for OneAgent injection in classic full-stack mode. For additional details on CRI-O hooks, refer to this [Red Hat blog postï»¿](https://dt-url.net/fq039v2).

Show step-by-step instructions

Follow these instructions to successfully migrate from classic full-stack mode:

1. Delete DynaKube custom resource:

   Delete the DynaKube configured in classic full-stack mode by running the following command:

   ```
   kubectl delete dynakube -n dynatrace <dynakube-name>
   ```

   This action will lead to the removal of OneAgents in classic full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter. Additionally, if Kubernetes monitoring is configured in the DynaKube custom resource, Kubernetes monitoring will stop instantly with the removal of the ActiveGate.
2. Wait for the OneAgent pods to terminate.
3. Follow the instructions in the [Cleanup nodes](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Upgrade and uninstallation procedures for Dynatrace Operator") section to remove Dynatrace CRI-O hooks from all Linux nodes.
4. Continue with step 1 of the [standard migration procedure](#migrate).

## Changes in Kubernetes resources

This migration impacts several Kubernetes resources, altering their functions or introducing new components to support cloud-native injection mode. Key changes include:

Component

classic full-stack

cloud-native full-stack

OneAgent

* Deployed as a DaemonSet
* Collect host metrics on nodes
* Inject code modules into application pods

* Deployed as a DaemonSet
* Collect host metrics on nodes

Dynatrace Webhook Server

* Validates DynaKube definitions

* Validates DynaKube definitions
* Inject code modules into application pods by modifying pod definitions

[Dynatrace Operator CSI driver](/docs/ingest-from/setup-on-k8s/how-it-works#csi-driver "In-depth description on how the deployment on Kubernetes works.")

Required

* Not present

* Deployed as a DaemonSet
* Optimizes the download of code modules to speed up pod injection and reduce storage consumption


---


## Source: cloud-native-to-app-monitoring.md


---
title: Migrate from cloud-native full-stack to application monitoring mode
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring
scraped: 2026-02-15T21:23:44.135577
---

# Migrate from cloud-native full-stack to application monitoring mode

# Migrate from cloud-native full-stack to application monitoring mode

* Latest Dynatrace
* 2-min read
* Published Apr 09, 2024

Dynatrace Operator version 1.0.0+

This guide describes the steps required to migrate your Dynatrace deployment from cloud-native full-stack to the [application monitoring mode](/docs/ingest-from/setup-on-k8s/how-it-works#auto "In-depth description on how the deployment on Kubernetes works.").

## Advantages

To only monitor selected applications on Kubernetes, application monitoring offers a flexible approach with the following benefits:

* The application monitoring mode, similar to the cloud native full stack mode, prevents race conditions that can occur when OneAgent DaemonSet pods and monitored application pods start simultaneously.
* By leveraging Kubernetes concepts such as admission webhooks and CSI driver for Code Module injection, application monitoring mode reduces the required privileges for OneAgent.

### Considerations and implications

* When switching to application monitoring, previously deployed OneAgents will get deactivated and deep monitoring of applications will stop. Consequently, restarting all application pods that require deep monitoring becomes mandatory. Restarting these pods ensures that applications are reinjected, allowing deep monitoring to resume.
* In application monitoring mode, container monitoring rules are ignored. Instead, [label selectors](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") should be employed to precisely manage OneAgent injection.
* Log monitoring requires [additional setup](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-fluent-bit-logs-k8s "Integrate Fluent Bit in Kubernetes to stream logs to Dynatrace.").

## Migrate to application monitoring mode

This section provides all the information needed to perform the migration from cloud-native full-stack to application monitoring mode.

1. Reconfigure (existing) DynaKube for application monitoring mode:

   The following side-by-side comparison outlines how to reconfigure a DynaKube CR from cloud-native full-stack to application monitoring:

   Cloud-native full-stack monitoring

   Application monitoring

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   cloudNativeFullStack:



   args:



   - "--set-host-group=<host-group>"



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<environment-id>.live.dynatrace.com/api



   networkZone: <network-zone>



   oneAgent:



   hostGroup: <host-group>



   applicationMonitoring: {}



   activeGate:



   capabilities:



   - routing



   - kubernetes-monitoring



   - dynatrace-api
   ```

   For further information on how to configure DynaKube for application monitoring mode, visit the [deployment guide](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") or [DynaKube parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#spec-oneagent-applicationmonitoring "List the available parameters for setting up Dynatrace Operator on Kubernetes."). Alternatively, download the [DynaKube custom resource sampleï»¿](https://dt-url.net/0w036dz) for application monitoring from GitHub and adapt the DynaKube custom resource according to your requirements.
2. Apply the DynaKube custom resource:

   Run the command below to apply the DynaKube custom resource. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f dynakube.yaml
   ```

   This action will lead to the removal of OneAgents in cloud-native full-stack mode and subsequently result in the termination of deep monitoring for application pods shortly thereafter.
3. Restart application workloads:

   Restart all application workloads promptly to trigger OneAgent injection and enable deep monitoring minimizing monitoring outages.

## Changes in Kubernetes resources

The migration impacts several Kubernetes resources, altering their functions or introducing new components to support the application monitoring monitoring mode. Key changes include:

Component

cloud-native full-stack

Application monitoring

Dynatrace OneAgent

* Deployed as a DaemonSet
* Collect host metrics on nodes

* Not present

Dynatrace Webhook Server

* Validates DynaKube definitions
* Inject code modules into application pods by modifying pod definitions

* Validates DynaKube definitions
* Inject code modules into application pods by modifying pod definitions

[Dynatrace Operator CSI driver](/docs/ingest-from/setup-on-k8s/how-it-works#csi-driver "In-depth description on how the deployment on Kubernetes works.")

Required

* Deployed as a DaemonSet
* Provides volume storage for OneAgents
* Manages and provides code modules used for pod injection and optimizes storage consumption

Optional

* Deployed as a DaemonSet
* Manages and provides code modules used for pod injection and optimizes storage consumption


---


## Source: dynakube.md


---
title: Migration guide for DynaKube API versions
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/dynakube
scraped: 2026-02-15T21:23:32.205216
---

# Migration guide for DynaKube API versions

# Migration guide for DynaKube API versions

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Jan 22, 2026

## Overview

Depending on your Dynatrace Operator Version, different `apiVersion`'s of the `DynaKube` are supported. This page collects the migration guides for each `apiVersion` considering the version of the Operator.

Starting with Dynatrace Operator version 1.8.0+, Dynatrace Operator emits a Kubernetes warning event if the installed DynaKube CRD version doesnât match the version expected by this Operator release.

### API Version Overview

| DynaKube API version | Introduced | Deprecated | Removed [1](#fn-1-1-def) | Migration guides |
| --- | --- | --- | --- | --- |
| v1beta5 | 1.6.0 |  |  |  |
| v1beta4 | 1.5.0 |  |  | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Migrate your v1beta4 DynaKube CR to the v1beta5 apiVersions.") |
| v1beta3 | 1.3.0 | 1.7.0 |  | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Migrate your v1beta3 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Migrate your v1beta3 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Migrate your v1beta2 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Migrate your v1beta2 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | [to v1beta5](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Migrate your v1beta1 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Migrate your v1beta1 DynaKube CR to the v1beta4 apiVersions.") |

1

The respective API version is no longer served with the stated Dynatrace Operator version. It will get deleted from the CRD in a subsequent version.

## Conversion strategies

### Automatic conversion

Each version of the Dynatrace Operator converts the deployed `DynaKubes` with an older `apiVersion` to the latest `apiVersion` supported by that Dynatrace Operator version.

* Example: Dynatrace Operator v1.6.x will always convert `DynaKubes` to `v1beta5`.

So when you are checking, using `kubectl` what `apiVersion` you are using, you will always see the latest `apiVersion` that is supported by that Dynatrace Operator version. You can facilitate this mechanism instead of doing a manual conversion.

1. Download the converted version of your DynaKube. The following command will give you the DynaKube converted to the latest supported `apiVersion`:

   ```
   kubectl get dynakubes -n <namespace> <dynakube-name> -o yaml
   ```
2. Cleanup the downloaded DynaKube, only keep this sections

   * relevant parts of `.metadata` section
   * complete `.spec` section

### Manual conversion

1. First, check the version of the Operator that is currently deployed. If you don't know which version you're running, here are some ways to find out.

   Using Helm:

   * Use the `helm list` command, the `APP VERSION` field tells you the version of the installed Dynatrace Operator.

     + Example:

   ```
   > helm list -n dynatrace -o json | jq -r '.[].app_version'`



   1.6.2
   ```

   Using `kubectl`:

   * There is an `app.kubernetes.io/version` label on the Dynatrace Operator Deployment that shows the version used.

     + Example:

   ```
   > kubectl get deployment dynatrace-operator -n dynatrace -o jsonpath='{.metadata.labels.app\.kubernetes\.io/version}'



   1.6.2
   ```
2. Then check the `apiVersion` of the `DynaKube` used and follow the matching migration guide in the [overview above](#overview).

## Removal process

The Dynatrace Operator follows a structured deprecation process that follows the [official Kubernetes guidanceï»¿](https://kubernetes.io/docs/tasks/extend-kubernetes/custom-resources/custom-resource-definition-versioning) to ensure smooth transitions between DynaKube API versions while providing adequate time for migration.

### Phase 1: Deprecation announcement

**Pre-deprecation notice**: An announcement is made in the release notes at least one Dynatrace Operator release before the deprecation takes effect.

**Deprecation marking**: The API version is officially marked as deprecated in the subsequent release, but remains fully functional and supported.

### Phase 2: Supported deprecation period

**Continued support**: The deprecated API version continues to be fully supported and functional during the deprecation period.

**Migration encouragement**: Users are strongly encouraged to migrate to the newer API version during this time using the provided migration guides.

**Automatic conversion**: The Operator automatically converts deprecated API versions to the latest supported version in the background, ensuring compatibility.

### Phase 3: Removal preparation

**API serving disabled**: After the support period ends, the deprecated API version is marked as `served: false` in the Custom Resource Definition (CRD).

**Conversion-only mode**: The API version schema is retained in the CRD for conversion purposes only, allowing existing resources to be read and converted.

**Migration deadline**: Users must complete their migration to the newer API version before this phase to ensure continued functionality of their DynaKube resources.

### Phase 4: Complete removal

**Schema removal**: The deprecated API version schema is completely removed from the CRD in a future Operator release.

**No conversion support**: After removal, no conversion or compatibility support is available for the deprecated API version.

### Migration timeline recommendations

* **Immediate action**: Plan your migration as soon as a deprecation notice is announced
* **Testing period**: Use the deprecation period to test the migration in non-production environments
* **Production migration**: Complete production migration well before the API serving is disabled
* **Validation**: Verify that all DynaKube resources are using the current API version after migration


---


## Source: migrate-dto-to-tenant.md


---
title: Migrate Dynatrace Operator to a new environment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant
scraped: 2026-02-16T21:30:14.612503
---

# Migrate Dynatrace Operator to a new environment

# Migrate Dynatrace Operator to a new environment

* Latest Dynatrace
* 2-min read
* Updated on Sep 05, 2025

If you're currently monitoring your Kubernetes cluster with a Dynatrace OneAgent rolled out through the Dynatrace Operator and you need to migrate to a different Dynatrace environment, select one of the following options, based on your deployment method.

Kubernetes

OpenShift

1. Delete the existing DynaKube (starting with Dynatrace Operator version 1.3.0, editing `spec.apiUrl` is not allowed).

   ```
   kubectl delete dynakube dynakube -n dynatrace
   ```
2. Delete the existing secret that holds the Dynatrace Operator and Data Ingest tokens for authenticating to the Dynatrace Cluster.

   ```
   kubectl delete secret dynakube -n dynatrace
   ```
3. Create a new secret based on new tokens from your new environment.

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Apply the new DynaKube with the updated `spec.apiUrl`.

   ```
   kubectl apply -f dynakube.yaml
   ```
5. Restart your applications.

1. Delete the existing DynaKube (starting with Dynatrace Operator version 1.3.0, editing `spec.apiUrl` is not allowed).

   ```
   oc delete dynakube dynakube -n dynatrace
   ```
2. Delete the existing secret that holds the Dynatrace Operator and Data Ingest tokens for authenticating to the Dynatrace Cluster.

   ```
   oc delete secret dynakube -n dynatrace
   ```
3. Create a new secret based on new tokens from your new environment.

   ```
   oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
4. Apply the new DynaKube with the updated `spec.apiUrl`.

   ```
   oc apply -f dynakube.yaml
   ```
5. Restart your applications.


---


## Source: migrate-to-dto.md


---
title: Migrate from OneAgent Operator to Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto
scraped: 2026-02-16T09:38:22.271974
---

# Migrate from OneAgent Operator to Dynatrace Operator

# Migrate from OneAgent Operator to Dynatrace Operator

* Latest Dynatrace
* 5-min read
* Published Apr 01, 2021

## Understand and configure the DynaKube custom resource

The DynaKube custom resource (CR) replaces the OneAgent custom resource. The DynaKube CR follows the "don't repeat yourself" (DRY) principle to deploy a number of different components to your Kubernetes cluster.

Each section includes an illustration of the differences between the two custom resources, what changes from the old custom resource to the new one (marked with green), and what stays the same in both custom resource (marked with blue).

Changing operators will change the host ID calculations for monitored hosts, which will lead to monitoring anomalies in the Dynatrace UI.

### Classic full-stack migration

Follow the instructions below to migrate from OneAgent Operator to Dynatrace Operator for classic full-stack injection.

![Migration of properties](https://dt-cdn.net/images/classicfullstackmigration-600-fb8529d001.png)

What stays the same

What changes

**Global parameters (`spec`)**  
The following settings are global, shared by every component, and located under `spec`.

* `apiUrl`
* `tokens`[1](#fn-1-1-def)
* `skipCertCheck`
* `proxy`
* `trustedCAs`
* `networkZone`
* `customPullSecret`
* `enableIstio`

1

**Tokens must point to an existing secret.**

**ClassicFullStack parameters (`.spec.oneAgent.classicFullStack`)**  
A new section for the full-stack OneAgent is located at `.spec.oneAgent.classicFullStack`:

* `image`
* ~~`autoUpdate`~~[1](#fn-2-1-def)
* `version`[2](#fn-2-2-def)

1

Previously, this was `disableAgentUpdate` in the OneAgent CR.  
The `autoUpdate` field has been removed. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).").  
Auto-update is disabled when either the `version` or `image` fields are set.

2

This was `agentVersion` in the OneAgent CR.

All the other OneAgent parameters (such as tolerations, arguments, DNS, and resource settings) are also located in the `.spec.oneAgent.classicFullStack` section and are unique to the full-stack installation.

### Application-only migration

Follow the instructions below to migrate from OneAgent Operator to Dynatrace Operator for automatic application-only injection.

![Cloud native app only](https://dt-cdn.net/images/cloudnativeappo-600-de0c984048.png)

What stays the same

What changes

**Global parameters (`spec`)**  
The following settings are global, shared by every component, and located under `spec`.

* `apiUrl`
* `tokens`[1](#fn-3-1-def)
* `skipCertCheck`
* `proxy`
* `trustedCAs`
* `networkZone`
* `customPullSecret`
* `enableIstio`

1

**Tokens must point to an existing secret.**

**ApplicationMonitoring parameters (`.spec.oneAgent.applicationMonitoring`)**  
A new section for the full-stack OneAgent is located at `.spec.oneAgent.applicationMonitoring`:

* `version`[1](#fn-4-1-def)
* `useCSIDriver`[2](#fn-4-2-def)

1

This was `agentVersion` in the OneAgent CR.

2

This new parameter will deliver binaries to pods automatically and eliminate storage requirements on pods. This is in preview only and defaults to `false`.

The `image` parameter is no longer available. The functionality will be reintroduced in future. For now, all pods download from the API URL.

## Migrate from OneAgent Operator to Dynatrace Operator

You can migrate from the deprecated OneAgent Operator to the new Dynatrace Operator that manages the lifecycle of several Dynatrace components such as OneAgent, routing, and Kubernetes API Monitor. Additional components will be added as new observability features become available.

Select **one of the following options**, depending on your deployment methods.

[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Migrate manifests

Kubernetes

OpenShift

1. Delete OneAgent Operator and the `dynatrace` namespace/project.

   ```
   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/kubernetes.yaml



   kubectl delete namespace dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

1. Delete OneAgent Operator and the `dynatrace` namespace/project.

   ```
   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/<version>/openshift.yaml



   oc delete project dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

### Migrate with Helm

Kubernetes

OpenShift

1. Remove OneAgent Operator, the Helm repository, and the `dynatrace` namespace/project.

   ```
   helm uninstall dynatrace-oneagent-operator



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   kubectl delete namespace dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

1. Remove OneAgent Operator, the Helm repository, and the `dynatrace` namespace/project.

   ```
   helm uninstall dynatrace-oneagent-operator



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagentapms.yaml



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/download/v0.10.2/dynatrace.com_oneagents.yaml



   helm repo remove dynatrace



   oc delete project dynatrace
   ```
2. [Set up monitoring with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").


---


## Source: migration.md


---
title: Migration guides
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration
scraped: 2026-02-15T09:13:35.951687
---

# Migration guides

# Migration guides

* Latest Dynatrace
* 1-min read
* Updated on Sep 05, 2025

Explore step-by-step migration guides to help you transition between different Dynatrace monitoring setups.

[### Migrate from classic full-stack to cloud-native full-stack

Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack deployment.](/docs/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.")[### Migrate from classic full-stack to application monitoring mode

Migrate your Dynatrace deployment from classic full-stack to application monitoring mode.](/docs/ingest-from/setup-on-k8s/guides/migration/classic-to-app-monitoring "Migrate your Dynatrace deployment from classic full-stack to application monitoring mode.")[### Migrate from cloud-native full-stack to application monitoring mode

Migrate your Dynatrace deployment from cloud-native full-stack to application monitoring mode.](/docs/ingest-from/setup-on-k8s/guides/migration/cloud-native-to-app-monitoring "Migrate your Dynatrace deployment from cloud-native full-stack to application monitoring mode.")[### Migrate Dynatrace Operator to a new environment

Migrate monitoring to a new Dynatrace environment on Kubernetes clusters.](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant "Migrate monitoring to a new Dynatrace environment on Kubernetes clusters.")[### Migrate from OneAgent Operator to Dynatrace Operator

Migrate from deprecated OneAgent Operator to Dynatrace Operator.](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Detailed instructions how to migrate from deprecated OneAgent Operator to Dynatrace Operator using kubectl/oc")[### Migrate from manifests to Helm

Migrate from manifests to Helm for Dynatrace Operator installation.](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-helm "Migrate from manifests to Helm for Dynatrace Operator installation.")[### Migrate DynaKube to newer apiVersion

Migrate from your old `DynaKube` with an older `apiVersion` to the newest supported for a given Dynatrace Operator version.](/docs/ingest-from/setup-on-k8s/guides/migration/dynakube "Migrate your DynaKube CR to newer apiVersions based on the Operator Version you are using.")


---


## Source: network-configurations.md


---
title: Network configurations
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations
scraped: 2026-02-15T21:27:57.886040
---

# Network configurations

# Network configurations

* Latest Dynatrace
* 4-min read
* Published Mar 25, 2024

Configure Dynatrace in network-restricted environments with network configurations, proxy settings, and URL exclusions.

Network zones

For details on setting up and managing network zones, initial endpoint setup, and advanced configurations in restricted environments, see [Using network zones in Kubernetes](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations/network-zones "Set up and use network zones in Kubernetes environments with the Dynatrace Operator.").

## Configure proxy

For Kubernetes Platform Monitoring with Dynatrace, you might need to configure a proxy, which facilitates all outgoing connections for Dynatrace Operator components (such as `csi-driver` and `operator`), OneAgent, and ActiveGate.

Depending on your proxy configuration, especially regarding credentials, there are two options for configuring your proxy in a DynaKube:

Without proxy credentials

With proxy credentials

HTTPS proxies are supported for ActiveGate since version 1.289.  
HTTPS proxies are supported for OneAgent since version 1.311.

For proxies without credential requirements, provide your proxy URL in the `value` field:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



proxy:



value: http://<my-super-proxy>
```

For proxies requiring credentials.

1. Create a Kubernetes secret containing your encrypted proxy URL, including the credentials.

   Kubernetes

   OpenShift

   ```
   kubectl -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   ```
   oc -n dynatrace create secret generic my-proxy-secret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
   ```

   Rules for the proxy password

   Ensure the proxy password meets the following criteria:

   | Requirements | Corresponding characters |
   | --- | --- |
   | Characters allowed | [A-Za-z0-9] ! " # $ ( ) \* - . / : ; < > ? @ [ ] ^ \_ { | } |
   | Characters not allowed | blank space ' ` , & = + % \ |

   The password in the custom resource or proxy secret must be URL-encoded. For example, `password!"#$()*-./:;<>?@[]^_{|}~` becomes `password!%22%23%24()*-.%2F%3A%3B%3C%3E%3F%40%5B%5D%5E_%7B%7C%7D~`.
2. Provide the name of the secret in the `valueFrom` section.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



   proxy:



   valueFrom: my-proxy-secret
   ```

Dynatrace Operator version 1.0.0+

The connection between OneAgent and Dynatrace code modules with ActiveGate will always bypass the proxy, ensuring direct communication for these components.

If you need to bypass the proxy for other reasons, see the next section.

### Exclude selected URLs from proxy configuration

To set the list of URLs to exclude from the proxy configuration, add the following annotation to the DynaKube custom resource.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/no-proxy: "some.url.com,other.url.com"
```

Dynatrace Operator then excludes the listed URLs from the proxy settings. This exclusion applies specifically to Dynatrace Operator and the CSI driver. It doesn't affect the proxy settings for other components managed by Dynatrace Operator, such as OneAgent or ActiveGate.

## Add trusted CA certificates

### ActiveGate, OneAgent and Dynatrace Operator components

To add trusted CA certificates to ActiveGate, OneAgent and/or Dynatrace Operator, the certificates must be provided via a Kubernetes ConfigMap referenced in your DynaKube configuration.

1. Create a ConfigMap (replace `<ca-certificates>` with the CA certificates to be trusted).

   ```
   apiVersion: v1



   kind: ConfigMap



   metadata:



   name: mycaconfigmap



   namespace: dynatrace



   data:



   certs: |



   <ca-certificates>
   ```

   For example:

   ```
   data:



   certs: |



   -----BEGIN CERTIFICATE-----



   MIIFmTCCA4GgAwIBAgIUNGBlRh1tuDIqr25rjNfMtvzfkRUwDQYJKoZIhvcNAQEL



   BQAwXDELMAkGA1UEBhMCUEwxDDAKBgNVBAgMA1BPTTELMAkGA1UEBwwCR0QxHDAa



   BgNVBAoME0RlZmF1bHQgQ29tcGFueSBMdGQxFDASBgNVBAMMC3NxdWlkLnByb3h5



   MB4XDTI0MDYxODExNTU0OVoXDTI1MDYxODExNTU0OVowXDELMAkGA1UEBhMCUEwx



   DDAKBgNVBAgMA1BPTTELMAkGA1UEBwwCR0QxHDAaBgNVBAoME0RlZmF1bHQgQ29t



   cGFueSBMdGQxFDASBgNVBAMMC3NxdWlkLnByb3h5MIICIjANBgkqhkiG9w0BAQEF



   AAOCAg8AMIICCgKCAgEA3oM7eX/p68jIjqOcRnUUOoLz14s4rEdGr44j7W0Kkm3O



   +zzy5xEDh3lz8Wt5MGfkGYzuo9yxdmt6gCRSzOER6Af/uaALk5gO1I4wdgsRG7vA



   i5GcS4oWqrOAVgbNNtVRd3g5+ouWH1wx4hhu1w/XYIiQOiraCINiFLpxJ2OmcBB1



   CPR3DfwoB39tN/aqf0W7tWwG7kf3aabQ4giCFsoadV/h4pEXNx7sFS5rNSXBlajl



   zfau1O/QYdhzBEdeF7pNwG1EDfa66+Frb/luVjuea0c5UABV9xTiLSb3evFAx9w6



   n4dN3T2V9uBlhvKRAkqKuh70uTW1NlsNdo6xVBvl9ivPcqtM/p5nHgqTlX+UIbAu



   SmTOF5NB90EqHnb/BjPYUtaIWE6Zj8BkhEVbPejipsBBqci1iCnUFBGD1U8TNZGg



   2ySy5GH6Q6RIJ6JFOYtaHqYQg/VsLT55uRJzqgVNaOjDffYlaoNBdiBaQfzt+Nxk



   rF8p9un8hBb0CX2iwpyX5vy2HIXNtJrHOi1CcBMLYuxCyFrQChanB2NwQ1l1BIM6



   zDoHZh2CaPJTE/g0152dgvl0Xs1MtrQ/6Dmwodmitse/oWAO9CZBg6ELGZyjOKQn



   yvQbxMf3H9vOrddPQFEuhaErJNJUGDtvAH4i/CfmTyYSc61k+AwXLB39hrz7rMUC



   AwEAAaNTMFEwHQYDVR0OBBYEFPQEwTqk6OjBWqyNAFKD8FGetZd8MB8GA1UdIwQY



   MBaAFPQEwTqk6OjBWqyNAFKD8FGetZd8MA8GA1UdEwEB/wQFMAMBAf8wDQYJKoZI



   hvcNAQELBQADggIBAGpfz5NM4nlcA88FfG22Re7osKkBaP+GZBujpwRHGNYgJQ1T



   5yjrNSzGfI2kNz7m/SuauUQN8ehS57t9kvQHOru4Y0A5oxnRh+1jMSVX5Ri8o6ZD



   ObQ4J99YriGZVfOyiahQ41ekRprvLBALmfLjFsQKMWGy4B2p7YsTpQdK9Nl7TXub



   6Y6ZGousk5Kf/cKX3xxyHWbWsLqOwxfcpBGbi9AHZjBZX2utLq1sxQHg4/ma1fR0



   MXX49kXoJDCWZkd2qumwT7rpibp2KGul5jQ8gmUSO25T3r9xfygnzBk0obneya/J



   NW06SWHgmT+z5pWly6/9Y8hBtD8GD4AY7GgjmojF3ziDtddFhbPd1C2S8xdvFYiu



   qkjlLRuqRPyF3zwUiiFw8/D03Sc8hIR14XCGVexRgOzqUi1TrZ4Glb2uLF/vdLhz



   Loi9xjUSETsVvVuxAbGlU7pVLQJWElTETmdgYqzOPGE0m3ROSQxkSDLKe+7k9xZL



   PQSICKQYuD2dzttjx99cVZMLgiuaH2APsv1eIggf5tAC/LVyKZOf/QedG5o1Bb2T



   goCos2lkkJcV/LDBNE2X5+IS/3q3v0Esq90prl9wXH83CVtG4lJVpm42TccCwRID



   j4xHGOuWrdmKRafgeohGIsH1ZhckkPc4Vcri2232dRPUAXziS+Yp3Ef9xdov



   -----END CERTIFICATE-----
   ```
2. Apply the ConfigMap to your cluster.

   ```
   kubectl apply -f my-ca-configmap.yaml
   ```
3. In your DynaKube, reference the ConfigMap in the `trustedCAs` field.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



   trustedCAs: mycaconfigmap
   ```
4. Apply the DynaKube configuration to your cluster.

   ```
   kubectl apply -f dynakube-config.yaml
   ```

### Use `skipCertCheck` to bypass certificate verification

To ignore certificate verification for Dynatrace Operator components (`operator` and `csi-driver`), set `skipCertCheck` in your DynaKube configuration. This setting should only be used if the custom certificate authority is unknown or can't be provided to Dynatrace Operator via the `trustedCAs` field.

In Dynatrace Operator version 1.0.0 and earlier, the `skipCertCheck` setting was not applied during the image pulling process.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<activegate-host>:9999/e/<environment-id>/api



skipCertCheck: true
```

## Configure a server TLS certificate for ActiveGate

By default, ActiveGate uses a self-signed certificate, which can be replaced by a self-managed certificate as described in [Custom SSL certificate for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

To configure a server TLS certificate for the ActiveGate:

1. Create the [Kubernetes Opaque secretï»¿](https://dt-url.net/zm03qza) holding the ActiveGate certificate(s) and ActiveGate private key.

   ```
   kubectl -n dynatrace create secret generic mytlssecret --from-file=server.p12=<myag.p12> --from-file=server.crt=<myag.crt> --from-literal=password=<mypassword>
   ```

   Where:

   * `server.crt`âDynatrace Operator propagates ActiveGate certificate(s) from the file to OneAgents.
   * `server.p12`âActiveGate certificate(s) and ActiveGate private key, ActiveGate reads the file and configures itself to use the provided private key and certificates.
   * `password`âActiveGate reads it and uses it to decrypt the `server.p12` file.

   `server.12` and `server.crt` files should contain the same certificate(s).
2. Provide the name of the secret via the `tlsSecretName` field.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   spec:



   ...



   activeGate:



   tlsSecretName: <mytlssecret>



   ...
   ```


---


## Source: guides.md


---
title: Guides
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides
scraped: 2026-02-16T09:34:48.808356
---

# Guides

# Guides

* Latest Dynatrace
* 3-min read
* Published Jul 28, 2023

After you have installed Dynatrace Operator for Kubernetes, you might have specific use-cases and requirements to fulfill. This section contains guided content for a set of specific use-cases.

[### Migration

Guides on how to migrate between different monitoring environments.](/docs/ingest-from/setup-on-k8s/guides/migration "Guides on how to migrate between different monitoring environments.")[### Deployment and configuration

Guides and procedures for various operational tasks.](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration "Guides and procedures for various operational tasks")[### Network and security configurations

Explore various aspects of networking and security in your environment.](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance "Explore various aspects of networking, security, and compliance in your environment.")[### Container registries

Manage container registries with Dynatrace.](/docs/ingest-from/setup-on-k8s/guides/container-registries "Manage container registries with Dynatrace")[### High availability

Ensure high availability of your Dynatrace deployment.](/docs/ingest-from/setup-on-k8s/guides/high-availability "Ensure high availability of your Dynatrace deployment")[### Metadata and automation

Automate and optimize your system's metadata management.](/docs/ingest-from/setup-on-k8s/guides/metadata-automation "Automate and optimize your system's metadata management")


---


## Source: cloud-native-fullstack.md


---
title: Full-stack observability
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack
scraped: 2026-02-16T21:18:12.777972
---

# Full-stack observability

# Full-stack observability

* Latest Dynatrace
* 3-min read
* Published Oct 31, 2024

Full-stack observability combines infrastructure and application monitoring in Kubernetes environments. This setup includes the injection of Dynatrace OneAgent and provides insights into both cluster performance and application behavior.

See the [`.spec.oneAgent.cloudNativeFullStack`](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Capabilities

* Offers similar functionality to the classic full-stack injection.
* Uses mutating webhooks to inject code modules into application Pods.
* Enables data enrichment for Kubernetes environments via [enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-kubernetes-operator "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

### Current limitations

* Diagnostic files (support archives) for application Pods aren't yet supported.
* Container monitoring rules aren't supported (the DynaKube label selector parameter provides similar functionality).
* [Go static monitoring](/docs/ingest-from/technology-support/application-software/go/support/go-known-limitations#static-monitoring "Learn the limitations for Go support and their workarounds.") is partially supported.
* OneAgent support archives, such as code module logs, can be gathered from the monitored process/Pod using the **Run OneAgent Diagnostics** menu option on the process-specific page. If no OneAgent support archive is available, it means one of the following:

  + No code module has been injected into the application Pod.
  + There is an issue with OneAgent creating the support archive.

## Deployed resources

### Dynatrace Operator components

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.
* [Dynatrace Operator CSI Driver](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") deployed as a DaemonSet, provides writable volume storage for OneAgent binaries to minimize network and storage usage.

### Operator-managed components

The following components are deployed by applying a DynaKube with full-stack observability:

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") collects host metrics from Kubernetes nodes.
* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster and monitors the Kubernetes API.
* Dynatrace code modules are injected into your application to enable deep monitoring and observability.

![cloud-native](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-40-02-pm-2352-4cba84df51.png)


---


## Source: classic-fullstack.md


---
title: Classic Full-Stack monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack
scraped: 2026-02-16T21:17:38.530885
---

# Classic Full-Stack monitoring

# Classic Full-Stack monitoring

* Latest Dynatrace
* 2-min read
* Published Oct 31, 2024

Classic Full-Stack monitoring integrates host and application monitoring for Kubernetes environments. Instrumented Pods maintain their relationship with hosts, enabling the collection of host metrics.

See [`.spec.oneAgent.classicFullStack`](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") section of DynaKube for additional information.

## Capabilities

* Instrumented Pods maintain their taxonomic relationship with hosts and host metrics. OneAgent complements code modules with OOM detection, disk and storage monitoring, network monitoring, and more.
* This all-in-one approach includes Kubernetes cluster monitoring, distributed tracing, fault domain isolation, and deep code-level insights using a single deployment configuration across your clusters.

## Limitations

Thereâs a startup dependency between the container where OneAgent is deployed and the application container to be instrumented (for example, containers with deep process monitoring enabled). The OneAgent container must be started, and the `oneagenthelper` process must be running before the application container is launched to ensure proper instrumentation.

## Deployed resources

### Dynatrace Operator components

The following components are deployed via Helm/Manifests as part of the core installation. For more information, go to their respective sections:

* [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#operator "Components of Dynatrace Operator") manages the automated rollout, configuration, and lifecycle of Dynatrace components in your Kubernetes environment.
* [Dynatrace Operator webhook](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#webhook "Components of Dynatrace Operator") validates DynaKube definitions, converts definitions with older API versions, and injects configurations into Pods.

### Operator-managed components

The following components are deployed by applying a DynaKube with full-stack observability:

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") collects host metrics from Kubernetes nodes.
* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") routes observability data to the Dynatrace cluster and monitors the Kubernetes API.

![classic-full-stack](https://dt-cdn.net/images/screenshot-2024-01-31-at-2-37-54-pm-2354-6d55b949e0.png)

Classic full-stack injection requires *write access* from the OneAgent Pod to the Kubernetes node file system to detect and inject into newly deployed containers.


---


## Source: how-it-works.md


---
title: How it works
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/how-it-works
scraped: 2026-02-16T21:30:07.817516
---

# How it works

# How it works

* Latest Dynatrace
* 1-min read
* Published May 10, 2022

This section provides an in-depth look at how Dynatrace components are deployed and how they interact with Kubernetes clusters and entities.

## Deployment modes

[#### Kubernetes platform monitoring

In-depth description of Kubernetes platform monitoring using Dynatrace Operator.

Kubernetes platform monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/kubernetes-monitoring)[#### Application observability

In-depth description of Application observability using the Dynatrace Operator.

Application observability](/docs/ingest-from/setup-on-k8s/how-it-works/application-monitoring)[#### Full-stack observability

In-depth description of full-stack observability using Dynatrace Operator.

Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack)

### Other

[#### Classic Full-Stack monitoring

In-depth description of Classic Full-Stack monitoring using Dynatrace Operator.

Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack)[#### Host monitoring

In-depth description of Host monitoring using Dynatrace Operator.

Host monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/host-monitoring)

## Components

[#### Dynatrace Operator

Components of Dynatrace Operator

Dynatrace Operator](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator)


---


## Source: dynakube-parameters.md


---
title: DynaKube parameters for Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters
scraped: 2026-02-16T09:38:08.852569
---

# DynaKube parameters for Dynatrace Operator

# DynaKube parameters for Dynatrace Operator

* Latest Dynatrace
* 57-min read
* Updated on Jan 02, 2026

This page will help you to understand and configure the DynaKube [Kubernetes Custom Resourceï»¿](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), enabling you to optimize your Dynatrace Operator setup according to your specific requirements.

The table below specifies the required Dynatrace Operator versions corresponding to each DynaKube API version.

| DynaKube API version | Minimum Dynatrace Operator version | Maximum Dynatrace Operator version [1](#fn-1-1-def) |
| --- | --- | --- |
| `v1beta6` | 1.8 |  |
| `v1beta5` | 1.6 |  |
| `v1beta4` | 1.5 |  |
| `v1beta3` | 1.4 | 1.7 |
| `v1beta2` | 1.2 | 1.6 |
| `v1beta1` | All versions | 1.6 |

1

The corresponding DynaKube API versions will be removed from the Dynatrace Operator in the subsequent minor or major release.

See the DynaKube YAML samples on [GitHubï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.5.0/assets/samples/dynakube).

v1beta6

v1beta5

v1beta4

v1beta3

v1beta2

v1beta1

Dynatrace Operator version 1.8.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified in an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-2-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-2-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `terminationGracePeriodSeconds` | Configures the terminationGracePeriodSeconds parameter of the ActiveGate pod. Kubernetes defaults and rules apply. | Not applicable | int |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |
| `volumeClaimTemplate` | Describes the common attributes of storage devices and allows a Source for provider-specific attributes. | Not applicable | corev1.PersistentVolumeClaimSpec |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `prometheus` | Enables prometheus extension. | Not applicable |  |
| `databases` | List of database extensions. | Not applicable | [[]DatabaseSpec](#extensions-databases) |

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.extensions.databases`

Available with a future Dynatrace version.

* All parameters besides `id` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `id` | Unique Kubernetes object name. | Not applicable | string |
| `replicas` | Number of SQL Extension Executor replicas. | 1 | int32 |
| `volumes` | Volumes for file-based authentication. | Not applicable | []Volume |
| `volumeMounts` | Volume mounts for file-based authentication. | Not applicable | []VolumeMount |
| `serviceAccountName` | ServiceAccount for IAM-based authentication. | Not applicable | string |
| `labels` | SQL Extension Executor labels. | Not applicable | []Label |
| `annotations` | SQL Extension Executor annotations. | Not applicable | []Annotation |
| `affinity` | SQL Extension Executor affinities. | Not applicable | []Affinity |
| `resources` | SQL Extension Executor resources. | Not applicable | ResourcesSpec |
| `nodeSelector` | SQL Extension Executor node selector. | Not applicable | NodeSelectorSpec |
| `topologySpreadConstraints` | SQL Extension Executor topology spread constraints. | Not applicable | TopologySpreadConstraints |

On OpenShift, using volumes of type `hostPath` is prohibited by default SCC and will cause failures. If `hostPath` is required, create a role with sufficient privileges and bind it to the respective service account. In this example, the created role is bound to a service account named `custom-sql-extension-executor-sa`:

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-sa



namespace: dynatrace



---



apiVersion: rbac.authorization.k8s.io/v1



kind: Role



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-role



namespace: dynatrace



rules:



- apiGroups:



- ""



resources:



- pods



verbs:



- list



- apiGroups:



- security.openshift.io



resourceNames:



- nonroot-v2



resources:



- securitycontextconstraints



verbs:



- use



---



kind: RoleBinding



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-rolebinding



namespace: dynatrace



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: Role



name: custom-sql-extension-executor-role



subjects:



- kind: ServiceAccount



name: custom-sql-extension-executor-sa



namespace: dynatrace



---



kind: Dynakube



spec:



extensions:



databases:



- id: my-sql-db



serviceAccountName: custom-sql-extension-executor-sa
```

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.kspm` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Specifies the host paths that are mounted to the NCC container. | Not applicable | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring:

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator version 1.6.0+

Enable additional [telemetry ingest endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest using 3rd-party protocols. Adding this section deploys the Dynatrace Collector workload to the cluster.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `protocols` | Specifies the protocols that will be ingested by the Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Specifies the name of the service to be used. If not specified the serviceName is set to a default. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret containing a TLS certificate used by telemetryIngest. | Not applicable | string |

## `.spec.otlpExporterConfiguration`

Dynatrace Operator version 1.8.0+

Enable automatic [OTLP exporter configuration](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.") for application pods that are already instrumented with OpenTelemetry SDK.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `signals` | The OpenTelemetry signals that will be automatically ingested into Dynatrace. | Not applicable | [signalConfiguration](#otlp-exporter-signals) |
| `namespaceSelector` | The namespaces where OTLP exporter configuration will be injected. For more information, see [Configure monitoring for namespaces and pods](/docs/ingest-from/setup-on-k8s/guides#annotate "Detailed description of installation and configuration options for specific use-cases") | Not applicable | LabelSelector |
| `overrideEnvVars` | Enable overriding of existing configuration environment variables of the OTLP exporter. | false | boolean |

## `.spec.otlpExporterConfiguration.signals`

Dynatrace Operator version 1.8.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `logs` | Enables the automatic OTLP exporter configuration for logs. See [endpoint urls for otlphttpï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | - | object |
| `metrics` | Enables the automatic OTLP exporter configuration for metrics. See [endpoint urls for otlphttpï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | - | object |
| `traces` | Enables the automatic OTLP exporter configuration for traces. See [endpoint urls for otlphttpï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp) | - | object |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Node Configuration Collector image. | Not applicable | string |
| `tag` | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `tolerations` | Set tolerations for the LogMonitoring pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring main container. | Not applicable | []string |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified, a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Labels applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller pod. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | Not applicable | string |
| `tag` | Tag for Dynatrace Collector image. | Not applicable | string |

## `.spec.templates.sqlExtensionExecutor`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for SQL Extension Executor. | Not applicable | [imageRef](#extensions-sql-extension-executor-image-ref) |
| `tolerations` | Tolerations for SQL Extension Executor pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |

## `.spec.templates.sqlExtensionExecutor.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of SQL Extension Executor image. | Not applicable | string |
| `tag` | Tag for SQL Extension Executor image. | Not applicable | string |

Dynatrace Operator version 1.6.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified in an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-3-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-3-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `terminationGracePeriodSeconds` | Configures the terminationGracePeriodSeconds parameter of the ActiveGate pod. Kubernetes defaults and rules apply. | Not applicable | int |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |
| `volumeClaimTemplate` | Describes the common attributes of storage devices and allows a Source for provider-specific attributes. | Not applicable | corev1.PersistentVolumeClaimSpec |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

Adding this section enables extension support in Kubernetes. To use extensions

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.kspm` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Specifies the host paths that are mounted to the NCC container. | Not applicable | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator version 1.6.0+

Enable Dynatrace [telemetry endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest. Adding this section deploys the Dynatrace Collector by Dynatrace Operator.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `protocols` | Specifies the protocols that will be ingested by the Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Specifies the name of the service to be used. If not specified the serviceName is set to a default. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret containing a TLS certificate used by telemetryIngest. | Not applicable | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Node Configuration Collector image. | Not applicable | string |
| `tag` | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `tolerations` | Set tolerations for the LogMonitoring pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring main container. | Not applicable | []string |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified, a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Labels applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller pod. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Tag for Dynatrace Collector image. | `latest` | string |

Dynatrace Operator version 1.5.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified in an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.5.0/assets/samples/dynakube). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-4-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-4-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `terminationGracePeriodSeconds` | Configures the terminationGracePeriodSeconds parameter of the ActiveGate pod. Kubernetes defaults and rules apply. | Not applicable | int |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |
| `persistentVolumeClaim` | Describes the common attributes of storage devices and allows a Source for provider-specific attributes. | Not applicable | corev1.PersistentVolumeClaimSpec |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

Adding this section enables extension support in Kubernetes. To use extensions

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator version 1.6.0+

Adding this section deploys the Dynatrace Collector by the Operator.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `protocols` | Specifies the protocols that will be ingested by the Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Specifies the name of the service to be used. If not specified the serviceName is set to a default. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret containing a TLS certificate used by telemetryIngest. | Not applicable | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Node Configuration Collector image. | Not applicable | string |
| `tag` | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring Pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring Pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring Pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring Pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring Pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `tolerations` | Set tolerations for the LogMonitoring Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring main container. | Not applicable | []string |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Lables applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller Pod. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector Pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Tag for Dynatrace Collector image. | `latest` | string |

Dynatrace Operator version 1.4.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified on an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-5-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-5-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

Adding this section enables extension support in Kubernetes. To use extensions

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| repository | URL of Node Configuration Collector image. | Not applicable | string |
| tag | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring Pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring Pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring Pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring Pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring Pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the NodeConfigurationCollector | Not applicable | corev1.NodeAffinity |
| `tolerations` | Set tolerations for the LogMonitoring Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring main container. | Not applicable | []string |
| `updateStrategy` | Define the NodeConfigurationCollector daemonSet updateStrategy. | Not applicable | appsv1.DaemonSetUpdateStrategy |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Lables applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller Pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Available with a future Dynatrace version.

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector Pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Tag for Dynatrace Collector image. | `latest` | string |

Dynatrace Operator version 1.2.0 - 1.6.0

Deprecation notice

DynaKube API version `v1beta2` is no longer available with Dynatrace Operator version 1.7.0+.

## `.spec`

* `apiUrl` parameter is Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `useCSIDriver` | Set if you want to use the CSIDriver. Don't enable it if you do not have access to Kubernetes nodes or if you lack privileges. | `false` | boolean |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-6-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-6-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

See [Configure enrichment directory](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") for additional information

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `true` by default. | `true` | boolean |

DynaKube API version `v1beta1` is no longer available with Dynatrace Operator version 1.6.0+.
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") | LabelSelector |

Dynatrace Operator version <=1.6.0

Deprecation notice

DynaKube API version `v1beta1` is no longer available with Dynatrace Operator version 1.7.0+.

## `.spec`

* `apiUrl` parameter is Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). | Not applicable | string |
| `tokens` | Name of the secret holding the tokens. | Name of custom resource (`.metadata.name`) if unset | string |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | `false` | boolean |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | Not applicable | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. Put the certificate under `certs` within your configmap. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | Not applicable | string |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | Not applicable | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | Not applicable | string |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | `false` | boolean |
| `namespaceSelector` | Applicable only for `applicationMonitoring` or `cloudNativeFullStack` configuration types. The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |
| `useCSIDriver` | Set if you want to use the CSI driver. Don't enable it if you do not have access to Kubernetes nodes or if you lack privileges. | `false` | boolean |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-7-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-7-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.


---


## Source: edgeconnect-parameters.md


---
title: EdgeConnect parameters for Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters
scraped: 2026-02-16T21:28:34.864329
---

# EdgeConnect parameters for Dynatrace Operator

# EdgeConnect parameters for Dynatrace Operator

* Latest Dynatrace
* 7-min read
* Updated on Dec 22, 2025

[EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.") enables Dynatrace apps and workflows to interact securely with your systems. EdgeConnect is available as a Docker container and can run in any container runtime environment. This reference guide provides detailed information on how to configure the EdgeConnect [custom resourceï»¿](https://dt-url.net/b60397m) within your Kubernetes environment.

The following table lists the minimum required Dynatrace Operator versions for each EdgeConnect API version.

| DynaKube API version | Minimum Dynatrace Operator version |
| --- | --- |
| `v1alpha2` | 1.3.0+ |
| `v1alpha1` | All versions |

v1alpha1

v1alpha2

## `.spec`

* The `apiServer` and `oauth` parameters are Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiServer` | Location of the hostname of the Dynatrace API to connect to, including your specific environment UUID. Example: `ENVIRONMENT_ID.live.dynatrace.com` | Not applicable | string |
| `annotations` | Adds annotations to the EdgeConnect Pods. | Not applicable | map[string] string |
| `autoUpdate` | Enables automatic restarts of EdgeConnect Pods when a new version becomes available. | `true` | boolean |
| `customPullSecret` | Pull secret for your private registry. | Not applicable | string |
| `env` | Adds environment variables to the EdgeConnect Pods. | Not applicable | []EnvVar |
| `hostRestrictions` | Restricts outgoing HTTP requests from your internal resources to specified hosts. Comma-separated list. | Not applicable | string |
| `imageRef` | Overrides the default image. | Not applicable | Object |
| `labels` | Adds labels to the EdgeConnect Pods. | Not applicable | map[string]string |
| `nodeSelector` | Node selector to control the selection of nodes for the EdgeConnect Pods. | Not applicable | map[string]string |
| `oauth` | EdgeConnect uses the OAuth client to authenticate itself with the Dynatrace platform. | Not applicable | Object |
| `replicas` | Number of replicas for your EdgeConnect. | 1 | int |
| `resources` | Defines resource requests and limits for single Pods. | Not applicable | ResourceRequirements |
| `tolerations` | Specifies tolerations for your EdgeConnect. | Not applicable | []Toleration |
| `topologySpreadConstraints` | Sets topology spread constraints for the EdgeConnect Pods. | Not applicable | []TopologySpreadConstraint |
| `hostPatterns` | Specifies a list of host patterns for requests to be managed by the EdgeConnect instance. This field mandatory and only used when `.spec.oauth.provisioner` is set to `true`. | empty | []string |
| `caCertsRef` | Adds custom root certificate from a ConfigMap. Ensure the certificate is located under the `certs` directory within your ConfigMap. | empty | string |

## `.spec.oauth`

* `resource`, `endpoint`, `clientSecret` parameters are Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `clientSecret` | Name of the secret containing the OAuth client ID/secret. | Not applicable | string |
| `endpoint` | Token endpoint URL of Dynatrace SSO. | Not applicable | string |
| `resource` | URN identifying your account. The URN is provided when creating the OAuth client. | Not applicable | string |
| `provisioner` | Enables EdgeConnect provisioning. This requires the `.spec.hostPatterns` field to be configured. | `false` | bool |

## `.spec.imageRef`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `repository` | Custom EdgeConnect image repository. | `docker.io/dynatrace/edgeconnect` | string |
| `tag` | Specifies version of the EdgeConnect image to use. | `latest` | string |

## `.spec.proxy`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `authRef` | Secret name containing the username and password used for authentication with the proxy, using the basic HTTP authentication scheme. | empty | string |
| `host` | Server address (hostname or IP address) of the proxy. | empty | string |
| `noProxy` | Represents the `NO_PROXY` or `no_proxy` environment variable. It specifies a string containing comma-separated values specifying hosts that should be excluded from proxying. | empty | string |
| `port` | Port of the proxy. | empty | integer |

## `.spec`

* The `apiServer` and `oauth` parameters are Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiServer` | Location of the hostname of the Dynatrace API to connect to, including your specific environment UUID. Example: `ENVIRONMENT_ID.live.dynatrace.com` | Not applicable | string |
| `annotations` | Adds annotations to the EdgeConnect Pods. | Not applicable | map[string] string |
| `autoUpdate` | Enables automatic restarts of EdgeConnect Pods when a new version becomes available. | `true` | boolean |
| `customPullSecret` | Pull secret for your private registry. | Not applicable | string |
| `env` | Adds environment variables to the EdgeConnect Pods. | Not applicable | []EnvVar |
| `hostRestrictions` | Restricts outgoing HTTP requests from your internal resources to specified hosts. | Not applicable | []string |
| `imageRef` | Overrides the default image. | Not applicable | Object |
| `labels` | Adds labels to the EdgeConnect Pods. | Not applicable | map[string]string |
| `nodeSelector` | Node selector to control the selection of nodes for the EdgeConnect Pods. | Not applicable | map[string]string |
| `oauth` | EdgeConnect uses the OAuth client to authenticate itself with the Dynatrace platform. | Not applicable | Object |
| `replicas` | Number of replicas for your EdgeConnect. | 1 | int |
| `resources` | Defines resource requests and limits for single Pods. | Not applicable | ResourceRequirements |
| `tolerations` | Specifies tolerations for your EdgeConnect. | Not applicable | []Toleration |
| `topologySpreadConstraints` | Sets topology spread constraints for the EdgeConnect Pods. | Not applicable | []TopologySpreadConstraint |
| `hostPatterns` | Specifies a list of host patterns for requests to be managed by the EdgeConnect instance. This field mandatory and only used when `.spec.oauth.provisioner` is set to `true`. | empty | []string |
| `caCertsRef` | Adds custom root certificate from a ConfigMap. Ensure the certificate is located under the `certs` directory within your ConfigMap. | empty | string |
| `serviceAccountName` | Name of Kubernetes `ServiceAccount` that allows EdgeConnect to access the Kubernetes API. | `dynatrace-edgeconnect` | string |
| `kubernetesAutomation` | Configures Kubernetes Automation. | Not applicable | Object |

## `.spec.oauth`

* `resource`, `endpoint`, `clientSecret` parameters are Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `clientSecret` | Name of the secret containing the OAuth client ID/secret. | Not applicable | string |
| `endpoint` | Token endpoint URL of Dynatrace SSO. | Not applicable | string |
| `resource` | URN identifying your account. The URN is provided when creating the OAuth client. | Not applicable | string |
| `provisioner` | Enables EdgeConnect provisioning. This requires the `.spec.hostPatterns` field to be configured. | `false` | bool |

## `.spec.imageRef`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `repository` | Custom EdgeConnect image repository. | `docker.io/dynatrace/edgeconnect` | string |
| `tag` | Specifies version of the EdgeConnect image to use. | `latest` | string |

## `.spec.proxy`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `authRef` | Secret name containing the username and password used for authentication with the proxy, using the basic HTTP authentication scheme. | empty | string |
| `host` | Server address (hostname or IP address) of the proxy. | empty | string |
| `noProxy` | Represents the `NO_PROXY` or `no_proxy` environment variable. It specifies a string containing comma-separated values specifying hosts that should be excluded from proxying. | empty | string |
| `port` | Port of the proxy. | empty | integer |

## `.spec.kubernetesApiAutomation`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `enabled` | Enables Kubernetes Automation. | `false` | bool |


---


## Source: security.md


---
title: Dynatrace Operator security
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/security
scraped: 2026-02-16T09:39:00.739725
---

# Dynatrace Operator security

# Dynatrace Operator security

* Latest Dynatrace
* 16-min read
* Updated on Jan 16, 2026

Kubernetes observability relies on components with different purposes, default configurations, and permissions. These different components need permissions to perform and maintain operational function of Dynatrace within your cluster.

While Dynatrace permissions adhere to the principle of least privilege, make sure to secure the `dynatrace` namespace and limit access to a closed group of administrators and operators.

## Permission list

### Dynatrace Operator

**Purpose:** Maintains the lifecycle of Dynatrace components. Replaces OneAgent Operator.

**Default configuration:** `1-replica-per-cluster`

**RBAC objects**:

* Service Account `dynatrace-operator`
* Cluster-Role `dynatrace-operator`
* Role `dynatrace-operator`

#### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `nodes` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/Update/Delete/List | `dynatrace-dynakube-config` `dynatrace-bootstrapper-config` `dynatrace-bootstrapper-certs` `dynatrace-metadata-enrichment-endpoint` `dynatrace-otlp-exporter-config` `dynatrace-otlp-exporter-certs` |
| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `edgeconnects/finalizers` | `dynatrace.com` | Update |  |
| `dynakubes/status` | `dynatrace.com` | Update |  |
| `edgeconnects/status` | `dynatrace.com` | Update |  |
| `statefulsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `daemonsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `replicasets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `deployments` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `deployments/finalizers` | `apps` | Update |  |
| `configmaps` | `""` | Get/List/Watch/Create/Update/Delete |  |
| `pods` | `""` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch/Create/Update/Delete |  |
| `events` | `""` | Create/Get/List/Patch |  |
| `services` | `""` | Create/Update/Delete/Get/List/Watch |  |
| `serviceentries` | `networking.istio.io` | Get/List/Create/Update/Delete |  |
| `virtualservices` | `networking.istio.io` | Get/List/Create/Update/Delete |  |
| `leases` | `coordination.k8s.io` | Get/Update/Create |  |

### Dynatrace Operator Webhook Server

**Purposes**:

* Modifies pod definitions to include Dynatrace code modules for application observability
* Validates DynaKube custom resources
* Handles the DynaKube conversion between versions

**Default configuration**: `1-replica-per-cluster`, can be scaled

**RBAC objects**:

* Service Account `dynatrace-webhook`
* Cluster-Role `dynatrace-webhook`
* Role `dynatrace-webhook`

#### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/List/Watch/Update | `dynatrace-dynakube-config` `dynatrace-bootstrapper-config` `dynatrace-bootstrapper-certs` `dynatrace-metadata-enrichment-endpoint` `dynatrace-otlp-exporter-config` `dynatrace-otlp-exporter-certs` |
| `replicationcontrollers` | `""` | Get |  |
| `replicasets` | `apps` | Get |  |
| `statefulsets` | `apps` | Get |  |
| `daemonsets` | `apps` | Get |  |
| `deployments` | `apps` | Get |  |
| `jobs` | `batch` | Get |  |
| `cronjobs` | `batch` | Get |  |
| `deploymentconfigs` | `apps.openshift.io` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `events` | `""` | Create/Patch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `pods` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |

### Dynatrace Operator CSI driver

**Purpose**:

* For `applicationMonitoring` configurations, it provides the necessary OneAgent binary for application monitoring to the pods on each node.
* For `hostMonitoring` configurations, it provides a writable folder for the OneAgent configurations when a read-only host file system is used.
* For `cloudNativeFullStack`, it provides both of the above.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-oneagent-csi-driver`
* Cluster-Role `dynatrace-oneagent-csi-driver`
* Role `dynatrace-oneagent-csi-driver`

#### Cluster-wide permission

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `jobs` | `batch` | Get/List/Create/Delete/Watch |  |
| `events` | `""` | Create/Patch |  |

### ActiveGate

#### Kubernetes Platform Monitoring

**Purpose**: collects cluster and workload metrics, events, and status from the Kubernetes API.

**Default configuration**: `1-replica-per-cluster`, can be scaled

**RBAC objects**:

* Service Account: `dynatrace-kubernetes`
* Cluster-Roles:

  + `dynatrace-kubernetes-monitoring`

    - Used to aggregate all ClusterRoles with the label `rbac.dynatrace.com/aggregate-to-monitoring: "true"`
  + `dynatrace-kubernetes-monitoring-default`

    - Aggregated by `dynatrace-kubernetes-monitoring`, more details can be found in the [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.")

##### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `nodes` | `""` | List/Watch/Get |  |
| `pods` | `""` | List/Watch/Get |  |
| `namespaces` | `""` | List/Watch/Get |  |
| `replicationcontrollers` | `""` | List/Watch/Get |  |
| `events` | `""` | List/Watch/Get |  |
| `resourcequotas` | `""` | List/Watch/Get |  |
| `pods/proxy` | `""` | List/Watch/Get |  |
| `nodes/proxy` | `""` | List/Watch/Get |  |
| `nodes/metrics` | `""` | List/Watch/Get |  |
| `services` | `""` | List/Watch/Get |  |
| `persistentvolumeclaims` | `""` | List/Watch/Get |  |
| `persistentvolumes` | `""` | List/Watch/Get |  |
| `jobs` | `batch` | List/Watch/Get |  |
| `cronjobs` | `batch` | List/Watch/Get |  |
| `deployments` | `apps` | List/Watch/Get |  |
| `replicasets` | `apps` | List/Watch/Get |  |
| `statefulsets` | `apps` | List/Watch/Get |  |
| `daemonsets` | `apps` | List/Watch/Get |  |
| `deploymentconfigs` | `apps.openshift.io` | List/Watch/Get |  |
| `clusterversions` | `config.openshift.io` | List/Watch/Get |  |
| `dynakubes` | `dynatrace.com` | List/Watch/Get |  |
| `edgeconnects` | `dynatrace.com` | List/Watch/Get |  |
| `customresourcedefinitions` | `apiextensions.k8s.io` | List/Watch/Get |  |
| `ingresses` | `networking.k8s.io` | List/Watch/Get |  |
| `networkpolicies` | `networking.k8s.io` | List/Watch/Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Dynatrace Kubernetes Security Posture Management (KSPM)

**Purposes**: [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.") detects, analyzes, and continuously watches for
misconfigurations, security hardening guidelines, and potential compliance violations in Kubernetes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-node-config-collector`
* Cluster-Role `dynatrace-kubernetes-monitoring-kspm`

  + Aggregated by the `dynatrace-kubernetes-monitoring` ClusterRole, more details can be found in the [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.")

##### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch |  |
| `nodes` | `""` | Get/List/Watch |  |
| `pods` | `""` | Get/List/Watch |  |
| `replicationcontrollers` | `""` | Get/List/Watch |  |
| `serviceaccounts` | `""` | Get/List/Watch |  |
| `services` | `""` | Get/List/Watch |  |
| `cronjobs` | `batch` | Get/List/Watch |  |
| `jobs` | `batch` | Get/List/Watch |  |
| `daemonsets` | `apps` | Get/List/Watch |  |
| `deployments` | `apps` | Get/List/Watch |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `statefulsets` | `apps` | Get/List/Watch |  |
| `networkpolicies` | `networking.k8s.io` | Get/List/Watch |  |
| `clusterrolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `clusterroles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `rolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `roles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |

### OneAgent

**Purposes**:

* Collects host metrics from Kubernetes nodes.
* Detects new containers and injects Dynatrace code modules into application pods using classic full-stack injection. Optional
* Collects container logs from Kubernetes nodes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-logmonitoring`

**Policy settings**: Allows **HostNetwork**, **HostPID**, to use any volume types.

**Necessary capabilities**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, `FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, `SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`

#### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `nodes/proxy` | `""` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Dynatrace Log Module

**Purposes**:

* Collects container logs from Kubernetes nodes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-logmonitoring`
* Cluster-Role `dynatrace-logmonitoring`

#### Cluster-wide permissions

Log monitoring requires [the same cluster-wide permissions as OneAgent](#oneagent-permissions).

### Dynatrace telemetry ingest

**Purposes**:

* Enable [Dynatrace telemetry endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest

  + Ingest data via [OTLPï»¿](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaegerï»¿](https://www.jaegertracing.io/), [StatsDï»¿](https://github.com/statsd/statsd) or [Zipkinï»¿](https://zipkin.io/) endpoints
* Analyze context-rich data with built-in apps, DQL, Notebooks and Dashboards

**RBAC objects**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-telemetry-ingest`

#### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | Get/Watch/List |  |
| `namespaces` | `""` | Get/Watch/List |  |
| `nodes` | `""` | Get/Watch/List |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Extensions

**Purposes**:

* Extensions extend Dynatrace analytics capabilities by ingesting data from various sources, such as third-party applications, services, and custom metrics. See [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") for more information.

**Default configuration**:

The following components are required, regardless of which extensions are used:

* Extension Execution Controller (EEC): `1-replica-per-cluster`

**RBAC objects**:

Depending on the used extension, the following RBAC objects are required.

* Service Accounts

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`
* Roles

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`

##### Namespace `dynatrace` permissions

*Prometheus extension*

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

*Database extension*

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Prometheus extension

**Purpose**:

* Collects metrics from Prometheus endpoints in your cluster.

**Default configuration**:

* Prometheus datasource: `replicas-set-in-dynakube` (no default, replicas set in the DynaKube)

**RBAC objects**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-extensions-prometheus`

##### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch |  |
| `endpoints` | `""` | Get/List/Watch |  |
| `services` | `""` | Get/List/Watch |  |
| `nodes` | `""` | Get/List/Watch |  |
| `nodes/metrics` | `""` | Get/List/Watch |  |
| `deployments` | `apps` | Get/List/Watch |  |
| `daemonsets` | `apps` | Get/List/Watch |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `statefulsets` | `apps` | Get/List/Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Database extension

**Purpose**:

* Collects metrics from database endpoints in your cluster.

**Default configuration**:

* SQL Extension Executor: `replicas-set-in-dynakube` (no default, replicas set in the DynaKube)

**RBAC objects**:

* Service Accounts

  + `dynatrace-sql-ext-exec`
* Roles

  + `dynatrace-sql-ext-exec`

##### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |

### Dynatrace Operator supportability

**Purposes**:

* Allow Dynatrace Operator to execute [the support-archive command](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components."). Necessary for troubleshooting Operator related issues.

**RBAC objects**:

* Role `dynatrace-operator-supportability`

**Opt-out**:

* You can opt out of this feature by setting the Dynatrace Operator Helm chart value `rbac.supportability` to `false`.

Disabling this feature will make it harder to provide the necessary information when opening support cases regarding Dynatrace Operator.

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods/log` | `""` | Get |  |
| `pods/exec` | `""` | Create |  |
| `jobs` | `batch` | Get/List |  |

### Dynatrace Operator API upgrade support

**Purposes**:

* Start `dynatrace-operator-crd-storage-migration` Job for automatic cleanup of removed Dynakube API versions in `pre-upgrade` Helm hook.

**RBAC objects**:

* ClusterRole `dynatrace-crd-storage-migration`
* Role `dynatrace-crd-storage-migration`
* ServiceAccount `dynatrace-crd-storage-migration`

**Opt-in**:

* You can opt-out of this feature by setting the Dynatrace Operator Helm chart value `crdStorageMigrationJob` to `false`.

#### Cluster wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |

## Security Controls of Dynatrace Operator components

The following table presents a detailed analysis of the security controls for Kubernetes components: Dynatrace Operator, Dynatrace Operator webhook, and Dynatrace Operator CSI driver. This report is based on:

* [CIS Benchmarkï»¿](https://dt-url.net/zd0368p), a globally recognized standard for securing Kubernetes deployments.
* [POD Security Standard policiesï»¿](https://dt-url.net/mp0345l).
* Best practices.

| Security Control | Standard (\*) | Operator | Webhook | CSI driver | OneAgent | Extensions Controller | Dynatrace Collector | ActiveGate | EdgeConnect | KSPM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Disallow privileged containers | CIS [1](#fn-1-1-def) 5.2.2 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [5](#fn-1-5-def) | Required [10](#fn-1-10-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow privilege escalation | CIS [1](#fn-1-1-def) 5.2.6 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Required [5](#fn-1-5-def) | Required [11](#fn-1-11-def) | Satisfied | Required [16](#fn-1-16-def) | Satisfied | Satisfied | Satisfied |
| Disallow containers running as root | CIS [1](#fn-1-1-def) 5.2.7 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Required [6](#fn-1-6-def) | Required [10](#fn-1-10-def) | Satisfied | Required [16](#fn-1-16-def) | Required [18](#fn-1-18-def) | Satisfied | Required [19](#fn-1-19-def) |
| Disallow use of too many or insecure capabilities | CIS [1](#fn-1-1-def) 5.2.8 / 5.2.9 / 5.2.10 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Satisfied | Required [12](#fn-1-12-def) | Satisfied | Satisfied | Required [18](#fn-1-18-def) | Satisfied | Required [24](#fn-1-24-def) |
| Limit access to secrets (RBAC) | CIS [1](#fn-1-1-def) 5.1.4 | Planned improvement [22](#fn-1-22-def) | Planned improvement [22](#fn-1-22-def) | Planned improvement [22](#fn-1-22-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow use of HostPath volumes | CIS [1](#fn-1-1-def) 5.2.12 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [7](#fn-1-7-def) | Required [10](#fn-1-10-def) | Satisfied | Satisfied | Satisfied | Satisfied | Required [20](#fn-1-20-def) |
| Disallow use of HostPorts | CIS [1](#fn-1-1-def) 5.2.13 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow access to host network | CIS [1](#fn-1-1-def) 5.2.5 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Required [13](#fn-1-13-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow use of host PID | CIS [1](#fn-1-1-def) 5.2.3 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Required [14](#fn-1-14-def) | Satisfied | Satisfied | Satisfied | Satisfied | Required [23](#fn-1-23-def) |
| Disallow use of host IPC | CIS [1](#fn-1-1-def) 5.2.4 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Require Resource limits | Best practice | Satisfied | Satisfied | Satisfied [9](#fn-1-9-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Demand seccomp to be used (at least default/runtime) | CIS [1](#fn-1-1-def) 5.7.2 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Satisfied | Required [15](#fn-1-15-def) | Satisfied | Satisfied | Required [18](#fn-1-18-def) | Required [21](#fn-1-21-def) | Required [19](#fn-1-19-def) |
| Disallow Secrets mounted as env variable | CIS [1](#fn-1-1-def) 5.4.1 | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Planned improvement [17](#fn-1-17-def) | Satisfied | Satisfied | Satisfied |
| Restrict sysctls | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict AppArmor | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow SELinux | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [8](#fn-1-8-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict automounting of service account token | CIS [1](#fn-1-1-def) 5.1.6 | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) |
| /proc Mount Type | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |

**Standard**:

1

[Center for Internet Security (CIS) Kubernetes benchmarkï»¿](https://dt-url.net/zd0368p).

2

[POD Security Standards Baseline profileï»¿](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).

3

[POD Security Standards Restricted profileï»¿](https://dt-url.net/ut4387d).

**General**:

4

Component needs to communicate with the Kubernetes API.

**CSI**:

5

CSI driver requires elevated permissions to create and manage mounts on the host system. For more details, see [CSI driver privileges](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "Components of Dynatrace Operator").

6

CSI driver communicates with kubelet using a socket on the host, to access this socket the CSI driver needs to run as root.

7

CSI driver stores/caches the OneAgent binaries on the host's filesystem, in order to do that it needs a hostVolume mount.

8

CSI driver needs seLinux level s0 for the application pods to see files from the volume created by the CSI driver.

9

CSI driver provisioner has no resources limits by default in order to provide the best [performance during provisioning](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "Set resource limits for Dynatrace Operator components."); limits can be set via Helm chart values.

**OneAgent**:

10

OneAgent DaemonSet runs with host-level privileges for full-stack visibility (network, processes, file system).

11

Required for init containers that instrument processes before startup.

12

Requires limited Linux capabilities (e.g., NET\_RAW) for network observability.

13

Uses host network namespace to monitor network traffic.

14

Uses host PID namespace to correlate process metrics.

15

Uses default runtime seccomp profile; explicit setting planned.

**Extension Execution Controller / Dynatrace Collector**:

16

Dynatrace Collector and Extensions controller may require root or elevated privileges for metrics collection and sidecar operations.

17

Dynatrace Collector currently uses environment variables for tokens; migrating to secret files is planned.

**ActiveGate / EdgeConnect / KSPM**:

18

ActiveGate runs with minimal elevated privileges to manage inbound connections.

19

KSPM mounts the host root filesystem `/` to perform configuration and security scans; hostPath restriction evaluation is planned.

20

KSPM mounts the entire host filesystem for node-level scanning; improvement under review to restrict mounted paths.

21

EdgeConnect currently lacks an explicit seccomp profile; addition is planned in future releases. This control is being addressed in upcoming releases.

22

Namespace-scoped Roles for the Operator, Webhook, and CSI driver currently allow access to all secrets within their namespace. Improvement planned to restrict these Roles to specific secret names, consistent with ClusterRole configuration.

23

KSPM requires host PID namespace access for the node collector to gather process-level data. This requirement will be documented.

24

KSPM requires specific Linux capabilities to scan and collect system configuration and security data; this is by design and cannot be removed.

## Security Controls of components managed by Dynatrace Operator

The following table presents a detailed analysis of the security controls for Kubernetes components managed by Dynatrace Operator: ActiveGate, [OneAgent (CloudNative)](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator."), LogAgent. This report is based on:

* [CIS Benchmarkï»¿](https://dt-url.net/zd0368p), a globally recognized standard for securing Kubernetes deployments.
* [POD Security Standard policiesï»¿](https://dt-url.net/mp0345l).
* Best practices.

| Security Control | Standard (\*) | ActiveGate | OneAgent CloudNative | OneAgent Log Module |
| --- | --- | --- | --- | --- |
| Disallow privileged containers | CIS [1](#fn-2-1-def) 5.2.2 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Required [15](#fn-2-15-def) |
| Disallow privilege escalation | CIS [1](#fn-2-1-def) 5.2.6 / PSSR [3](#fn-2-3-def) | Satisfied | Required [6](#fn-2-6-def) | Required [16](#fn-2-16-def) |
| Disallow containers running as root | CIS [1](#fn-2-1-def) 5.2.7 / PSSR [3](#fn-2-3-def) | Satisfied | Satisfied | Satisfied |
| Disallow usage of too many or insecure capabilities | CIS [1](#fn-2-1-def) 5.2.8 / 5.2.9 / 5.2.10 / PSSR [3](#fn-2-3-def) | Satisfied | Required [7](#fn-2-7-def) | Required [17](#fn-2-17-def) |
| Disallow usage of HostPath volumes | CIS [1](#fn-2-1-def) 5.2.12 / PSSB [2](#fn-2-2-def) | Satisfied | Required [8](#fn-2-8-def) | Required [18](#fn-2-18-def) |
| Disallow usage of HostPorts | CIS [1](#fn-2-1-def) 5.2.13 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Disallow access to host network | CIS [1](#fn-2-1-def) 5.2.5 / PSSB [2](#fn-2-2-def) | Satisfied | Required [9](#fn-2-9-def) | Satisfied |
| Disallow usage of host PID | CIS [1](#fn-2-1-def) 5.2.3 / PSSB [2](#fn-2-2-def) | Satisfied | Required [10](#fn-2-10-def) | Satisfied |
| Disallow usage of host IPC | CIS [1](#fn-2-1-def) 5.2.4 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | Satisfied |
| Require Resource limits | Best practice | Configurable [5](#fn-2-5-def) | Configurable [11](#fn-2-11-def) | Configurable [19](#fn-2-19-def) |
| Demand seccomp to be used (at least default/runtime) | CIS [1](#fn-2-1-def) 5.7.2 / PSSR [3](#fn-2-3-def) | Satisfied | Required [12](#fn-2-12-def) | Required [20](#fn-2-20-def) |
| Disallow Secrets mounted as env variable | CIS [1](#fn-2-1-def) 5.4.1 | Satisfied | Satisfied | Satisfied |
| Restrict sysctls | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Restrict AppArmor | PSSB [2](#fn-2-2-def) | Satisfied | Required [13](#fn-2-13-def) | Satisfied |
| Disallow SELinux | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Restrict automounting of service account token | CIS [1](#fn-2-1-def) 5.1.6 | Required [4](#fn-2-4-def) | Configurable [14](#fn-2-14-def) | Required [4](#fn-2-4-def) |
| /proc Mount Type | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |

**Standard**:

1

[Center for Internet Security (CIS) Kubernetes benchmarkï»¿](https://dt-url.net/zd0368p).

2

[POD Security Standards Baseline profileï»¿](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).

3

[POD Security Standards Restricted profileï»¿](https://dt-url.net/ut4387d).

**General**:

4

Component needs to communicate with the Kubernetes API.

**ActiveGate**

5

The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

**OneAgent**

6

Privilege escalation is needed for processes inside OneAgent container to get Linux capabilities.

7

[Monitoring actions](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#operation "Learn about Dynatrace OneAgent security and modifications to your Linux-based system") executed by OneAgent processes need the following [capabilities](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#linux-system-capabilities "Find out when Dynatrace OneAgent requires root privileges on Linux.").

8

Mounted host's root filesystem is accessed by all OneAgent modules and allows for log files access, disk metrics, and other host and process monitoring capabilities.

9

OneAgent needs access to host network namespace to provide host-level and process-level network health monitoring.

10

OneAgent needs access to host process table to collect performance metrics for all processes running on the host.

11

The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

12

OneAgent needs access to kernel syscalls beyond the RuntimeDefault set for monitoring purposes.

13

OneAgent needs access to the mount command which is blocked by the default AppArmor profile.

14

OneAgent component needs to communicate with the kubelet `/pods` endpoint. The K8s token is not mounted to the Pod if LogMonitoring is turned off via Helm values.

**OneAgent Log Module**:

15

LogAgent needs to run as privileged container on OCP cluster to access its persistent storage. [OCP persistent storage using hostPathï»¿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).

16

AllowPrivilegeEscalation is always true when the container is run as privileged. [Configure a Security Context for a Pod or Containerï»¿](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

17

LogAgent needs additional capability to get access to all monitored log files.

18

Needs access to log files on the host's filesystem.

19

The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

20

The seccomp profile can be set via DynaKube in order to run in secure computing mode.

## Pod security policies

These permissions used to be managed using a **PodSecurityPolicy** (PSP), but [in Kubernetes version 1.25 PSPs will be removedï»¿](https://dt-url.net/2403pxy) from the following components:

* [Dynatrace Operatorï»¿](https://dt-url.net/d7034gj) version 0.2.2
* **LEGACY** [Dynatrace OneAgent Operatorï»¿](https://dt-url.net/3023pvs) version 0.11.0
* [Corresponding Helm chartsï»¿](https://dt-url.net/rp43pl1)

**Dynatrace Operator version 0.2.1** is the last version in which PSPs are applied by default, so it's up to you to enforce these rules. As PSP alternatives, you can use other policy enforcement tools such as:

* [k-railï»¿](https://dt-url.net/qx63p3n)
* [Kyvernoï»¿](https://dt-url.net/6m83ppk)
* [Gatekeeperï»¿](https://dt-url.net/aha3ps4)

If you choose to use a PSP alternative, be sure to provide the necessary permissions to the Dynatrace components.

## Dynatrace Operator security context constraints

Dynatrace Operator version 0.12.0+

Starting with Dynatrace Operator version 0.12.0, the built-in creation of custom security context constraints (SCCs) has been removed for Dynatrace Operator and Dynatrace Operatorâmanaged components. This change was made to reduce complications caused by custom SCCs in unique OpenShift setups.

Despite this update, the components maintain the same permissions and security requirements as before.

The following tables show the SCCs used in different versions of Dynatrace Operator and OpenShift.

| Resources accessed | Custom SCC used in Dynatrace Operator versions earlier than 0.12.0 | SCC in Dynatrace Operator version 0.12.0+ and OpenShift earlier than 4.11 |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

| Resources accessed | Custom SCC used in Dynatrace Operator versions earlier than 0.12.0 | SCC in Dynatrace Operator version 0.12.0+ and OpenShift 4.11+ |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `nonroot-v2` |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

1

This SCC is the only built-in OpenShift SCC that allows usage of seccomp, which our components have set by default, and also the usage of CSI volumes.

It is still possible to create your own more permissive or restrictive SCCs that take your specific setup into consideration. You can safely remove the old SCCs that were created by a previous Dynatrace Operator version.

To remove the old SCCs, use the following command:

```
oc delete scc <scc-name>
```


---
