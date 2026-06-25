---
title: Update or uninstall Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator
scraped: 2026-05-12T12:03:28.374389
---

# Update or uninstall Dynatrace Operator

# Update or uninstall Dynatrace Operator

* 9-min read
* Updated on Jan 02, 2026

This page provides detailed instructions on how to update or uninstall Dynatrace Operator in Kubernetes and OpenShift environments.

Dynatrace Operator manages the deployment and lifecycle of all Dynatrace components in your Kubernetes clusters (for example, OneAgent, ActiveGate, and code modules). This includes, depending on the configuration, automatic updates for these components. Dynatrace Operator itself needs to be updated either by applying new manifests or by using helm charts.

We recommend using an up-to-date Operator version (at least version n-2) and always using the latest patch version of that Operator version (for example, 0.10.4 instead of 0.10.0).

## Update Dynatrace Operator

To update Dynatrace Operator, select **one of the following options**, depending on your deployment approach:

[**Manifest**](#manifest)[![Helm](https://dt-cdn.net/images/helm-1-f86d0c89ed.svg "Helm")

**Helm**](#helm)

### Manifest

For `classicFullStack`, `applicationMonitoring`, or `hostMonitoring` without CSI driver execute the following command.

Kubernetes

OpenShift

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
```

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
```

Starting with Dynatrace Operator version 1.4.0, the `kubernetes-csi.yaml` includes all Dynatrace Operator components. For more details, see [Dynatrace Operator release notes version 1.4.0](/managed/whats-new/dynatrace-operator/dto-fix-1-4-0#upgrade-from-dynatrace-operator-version-1-3-0 "Release notes for Dynatrace Operator, version 1.4.0").

If you're using the CSI driver, use this command instead:

Kubernetes

OpenShift

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
```

```
oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
```

### Helm

1. Upgrade the Helm chart.

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   The `values.yaml` file may have changed in newer versions. If existing values are no longer valid, they will be silently ignored as there's no validation for this.

   Upgrade from the OCI registry

   To upgrade to the latest release from the OCI registry, run the following command.

   ```
   helm upgrade dynatrace-operator dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Note that the `helm repo` command does not support OCI registries. You can only use the `helm pull`, `helm show`, `helm install`, and `helm upgrade` commands with OCI.

   Upgrade from a Dynatrace Operator version < 0.8.0

   ### Upgrade from old Dynatrace Operator versions with Helm

   If you use a Dynatrace Operator version earlier than v0.8.0 in a Helm deployment, follow the steps below to migrate to the latest Dynatrace Operator version with Helm.

   #### Step 1 Upgrade the custom resource definition

   According to your [configuration of the `values.yaml` fileï»¿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml), select one of the options below.

   * If `installCRD` is set to `true`, the custom resource definition will be automatically upgraded and managed by Helm.
   * If `installCRD` is set to `false`, you need to upgrade the custom resource definition manually before starting the Helm installation:

     Kubernetes

     OpenShift

     ```
     kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
     ```

     ```
     oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
     ```

   #### Step 2 Upgrade the Helm chart

   Delete the CRD section and the secrets from your existing values.yaml file or use and customize the [`values.yaml` sample from GitHubï»¿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.9.0/config/helm/chart/default/values.yaml). Upgrade the helm chart:

   ```
   helm upgrade dynatrace-operator dynatrace/dynatrace-operator -f values.yaml --atomic -n dynatrace
   ```

   The above changes make your old values unusable, therefore setting the `--reuse-values` flag isn't possible for migration.

   On certain Dynatrace Operator versions, a failed upgrade can break Helm rollback, resulting in a non-functional setup. This is due to the DynaKube stored `apiVersions`. For more information, see [Update or uninstall Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator "Upgrade and uninstallation procedures for Dynatrace Operator").

   ```
   Error: UPGRADE FAILED: release dynatrace-operator failed, and has been rolled back due to atomic being set: cannot patch "dynakubes.dynatrace.com" with kind CustomResourceDefinition: CustomResourceDefinition.apiextensions.k8s.io "dynakubes.dynatrace.com" is invalid: status.storedVersions[1]: Invalid value: "v1beta5": missing from spec.versions; v1beta5 was previously a storage version, and must remain in spec.versions until a storage migration ensures no data remains persisted in v1beta5 and removes v1beta5 from status.storedVersions
   ```

   If this error occurs

   1. [Uninstall Dynatrace Operator](#uninstall-dynatrace-operator).
   2. Delete the DynaKube custom resource definition.

      ```
      kubectl delete crd dynakubes.dynatrace.com
      ```
   3. [Install the desired Dynatrace Operator version](#update).
   4. Restart application workloads as needed.

## Update ActiveGate pods

Typically, ActiveGate pods are updated automatically on pod restart whenever there is a new version available (unless the image already specifies a certain version). However, if you need to manually restart ActiveGate pods, run the command below.

Kubernetes

OpenShift

```
kubectl -n dynatrace rollout restart statefulset/<ACTIVEGATE-STATEFULSET-NAME>
```

```
oc -n dynatrace rollout restart statefulset/<ACTIVEGATE-STATEFULSET-NAME>
```

## Update Access tokens

If you need to update your Dynatrace access tokens, follow the steps below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Find current tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#find-token "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Delete your secret**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-old-secret "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Create new tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-token "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Create a new secret with updated tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-secret "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Delete the old tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-token "Upgrade and uninstallation procedures for Dynatrace Operator")

### Step 1 Find current access tokens

Find and save your currently used tokens.

After generating new tokens, you'll need to [delete the old ones](#delete-token).

Kubernetes

OpenShift

```
kubectl -n dynatrace get secrets <dynakube-name> -o yaml | yq '.data.apiToken' | base64 -d
```

```
oc -n dynatrace get secrets <dynakube-name> -o yaml | yq '.data.apiToken' | base64 -d
```

### Step 2 Delete your secret

To delete the secret, run one of the commands below.

In Kubernetes, used tokens are stored in a secret named `dynakube` by default. If the DynaKube custom resource has a different name, or the `tokens` field in DynaKube is set, make sure that the new secret has the same name as defined there.

Kubernetes

OpenShift

```
kubectl -n dynatrace delete secret dynakube
```

```
oc -n dynatrace delete secret dynakube
```

### Step 3 Create new access tokens

For instructions on how to create the tokens, see [Access tokens and permissions](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

### Step 4 Create a new secret with updated access tokens

To create a new secret with the updated tokens, run one of the commands below, making sure to replace the placeholders with the new tokens.

Kubernetes

OpenShift

* For Dynatrace Operator token:

  ```
  kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
  ```
* For Dynatrace Operator and Data Ingest token:

  ```
  kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA-INGEST-TOKEN>"
  ```

* For Dynatrace Operator token:

  ```
  oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>"
  ```
* For Dynatrace Operator and Data Ingest token:

  ```
  oc -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA-INGEST-TOKEN>"
  ```

Dynatrace Operator picks up the updated secrets in approximately five minutes. Removing DynaKube and reapplying it forces an instant reconciliation.

### Step 5 Delete the old access token

After the new tokens are in place, delete the old ones.

1. In Dynatrace, go to **Access Tokens** and look for the [old token](#find-token).
2. Select **Delete**.

## Uninstall Dynatrace Operator

The following guide outlines the recommended steps for a clean uninstallation of Dynatrace Operator.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Remove Dynatrace Operatorâmanaged components**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator-components "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

Optional **Restart your monitored applications**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#restart-apps "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Remove Dynatrace Operator**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator "Upgrade and uninstallation procedures for Dynatrace Operator")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

Optional **Cleanup nodes**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Upgrade and uninstallation procedures for Dynatrace Operator")

**Important for CRI-O Runtime users with classicFullStack**

OneAgent version 1.279 and below

If you're using CRI-O as your cluster's container runtime with `classicFullStack`, complete the steps outlined in [Migrate from classic full-stack to cloud-native full-stack mode](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") as part of the uninstallation process.

### Step 1 Remove Dynatrace Operatorâmanaged components

Delete DynaKube custom resources to allow Dynatrace Operator to fully delete all related Dynatrace Operatorâmanaged components from your Kubernetes cluster. Wait for those components to be removed to make sure the cleanup is completed successfully.

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

Why is additional cleanup necessary?

Most resources related to a DynaKube are cleaned up automatically through the Kubernetes ownership system: when you delete a DynaKube, Kubernetes automatically removes all resources that have an `OwnerReference` pointing to that DynaKube.

However, some resources require additional cleanup steps due to Kubernetes limitations:

* **CSI driver dependencies**: Applications using the CSI driver must shut down before the CSI driver can be safely removed. This prevents potential data corruption or mounting issues.
* **Cross-namespace resources**: Kubernetes `OwnerReferences` only work within the same namespace. Because Dynatrace Operator creates resources such as `Secrets` in your application namespaces, it must clean these up separately.

### Step 2 optional Optional **If you used the CSI driver**: Restart your monitored applications

To ensure that CSI volumes are properly unmounted and disconnected from the CSI driver before proceeding with the uninstallation, use the following command to identify applications that use the CSI driver and need to be restarted.

The output will show a list of pods in the format `namespace pod` for each application that uses the CSI driver.

Kubernetes

OpenShift

```
kubectl get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

```
oc get pods --all-namespaces -o jsonpath='{range .items[?(@.spec.volumes[*].csi.driver=="csi.oneagent.dynatrace.com")]}{.metadata.namespace}{"\t"}{.metadata.name}{"\n"}{end}'
```

### Step 3 Remove Dynatrace Operator

After all Dynatrace Operatorâmanaged components have been successfully removed, you can safely uninstall Dynatrace Operator.

1. Delete Dynatrace Operator.

   Helm

   Kubernetes

   Openshift

   ```
   helm uninstall dynatrace-operator -n dynatrace
   ```

   * If the CSI driver was **not** installed (you used `kubernetes.yaml` during installation):

     ```
     kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes.yaml
     ```
   * If the CSI driver **was** installed (you used `kubernetes-csi.yaml` during installation):

     ```
     kubectl delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/kubernetes-csi.yaml
     ```

   * If the CSI driver was **not** installed (you used `openshift.yaml` during installation):

     ```
     oc delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift.yaml
     ```
   * If the CSI driver **was** installed (you used `openshift-csi.yaml` during installation):

     ```
     oc delete -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/openshift-csi.yaml
     ```
2. Delete the namespace.

   Kubernetes

   OpenShift

   ```
   kubectl delete namespace dynatrace
   ```

   ```
   oc delete namespace dynatrace
   ```

### Step 4 optional Clean up nodes

Depending on the monitoring mode, OneAgent and CSI driver data might remain on the node. To ensure a clean state, use a cleanup script to remove unnecessary data.

The script deploys a DaemonSet that runs a cleanup procedure on all Linux nodes in the cluster (amd64, arm64, ppc64le, s390x).

Before running the node cleanup, ensure that no DynaKube is deployed and all monitored pods have been restarted.

1. Download the script.

```
curl -O https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/refs/tags/v1.9.0/hack/cluster/cleanup-node-fs.sh
```

2. Make the script executable.

```
chmod +x cleanup-node-fs.sh
```

3. Run the script.

```
./cleanup-node-fs.sh
```

By default, the script uses the `dynatrace` namespace. To specify a different namespace, pass it as an argument:

```
./cleanup-node-fs.sh <namespace>
```

The script performs the following actions:

* Executes the OneAgent uninstall script, if present.
* Removes OneAgent directories (`/var/lib/dynatrace`, `/opt/dynatrace`, `/var/log/dynatrace`).
* Removes the CSI driver data directory.
* Reports the cleanup status for each node.

After all cleanup pods complete successfully, the DaemonSet is automatically deleted. If any cleanup fails, the DaemonSet remains for investigation.