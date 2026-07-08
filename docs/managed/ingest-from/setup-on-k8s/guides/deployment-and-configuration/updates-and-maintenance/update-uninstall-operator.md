---
title: Update or uninstall Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator
---

# Update or uninstall Dynatrace Operator

# Update or uninstall Dynatrace Operator

* 12-min read
* Updated on May 05, 2026

This page provides detailed instructions on how to update or uninstall Dynatrace Operator in Kubernetes and OpenShift environments.

Dynatrace Operator manages the deployment and lifecycle of all Dynatrace components in your Kubernetes clusters (for example, OneAgent, ActiveGate, and code modules). Dynatrace Operator itself needs to be updated either by applying new manifests or by using Helm charts.

We recommend using an up-to-date Dynatrace Operator version (at least version n-2) and always using the latest patch version (for example, 1.7.3 instead of 1.7.0).

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

   Note that the `helm repo` command does not support OCI registries. You can only use the `helm pull`, `helm show`, `helm install`, and `helm upgrade` commands with OCI.

   Upgrade from the Helm repository

   To upgrade to the latest release from the Helm repository, run the following command.

   ```
   helm upgrade dynatrace-operator dynatrace/dynatrace-operator \



   --namespace dynatrace \



   --atomic \



   -f values.yaml
   ```

   Migrate from the legacy Helm repository

   The legacy `dynatrace/helm-charts` repository is deprecated. If you're still using it, update before your next upgrade.

   Remove the old repository and add the current one:

   ```
   helm repo remove dynatrace



   helm repo add dynatrace https://raw.githubusercontent.com/Dynatrace/dynatrace-operator/main/config/helm/repos/stable
   ```

   Switch to using the OCI registry:

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --version <version> \



   --namespace dynatrace \



   --install
   ```

   Manually managing CRDs

   By default, the Helm chart manages the custom resource definition (CRD) automatically (`installCRD: true` in your `values.yaml`). If you've set `installCRD: false`, you must upgrade the CRD manually before running `helm upgrade`.

   The commands for the latest version are the following.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.9.0/dynatrace-operator-crd.yaml
   ```

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

**Find current tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#find-token "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Delete your secret**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-old-secret "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Create new tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-token "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Create a new secret with updated tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#create-new-secret "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Delete the old tokens**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#delete-token "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")

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

**Remove Dynatrace Operator–managed components**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator-components "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

Optional **Restart your monitored applications**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#restart-apps "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Remove Dynatrace Operator**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#remove-operator "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

Optional **Cleanup nodes**](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/update-uninstall-operator#cleanup-nodes "Upgrade paths, update procedures, and uninstallation guide for Dynatrace Operator.")

**Important for CRI-O Runtime users with classicFullStack**

OneAgent version 1.279 and below

If you're using CRI-O as your cluster's container runtime with `classicFullStack`, complete the steps outlined in [Migrate from classic full-stack to cloud-native full-stack mode](/managed/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") as part of the uninstallation process.

### Step 1 Remove Dynatrace Operator–managed components

Delete DynaKube custom resources to allow Dynatrace Operator to fully delete all related Dynatrace Operator–managed components from your Kubernetes cluster. Wait for those components to be removed to make sure the cleanup is completed successfully.

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

After all Dynatrace Operator–managed components have been successfully removed, you can safely uninstall Dynatrace Operator.

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

## Upgrade from older versions

If you have **ever run a Dynatrace Operator version older than 1.4** in your cluster - regardless of which version you're on today - you must upgrade to version **1.7.3 first** before going to the latest release. From 1.7.3, the Operator handles the necessary DynaKube conversion and CRD cleanup automatically.

To find out whether you're affected and if a version jump is possible, see [Check your current versions](#check-versions).

### Check your current versions

Check your current Dynatrace Operator version.

Helm

kubectl

```
helm list -n dynatrace -o json | jq -r '.[].app_version'
```

```
kubectl get deployment dynatrace-operator -n dynatrace \



-o jsonpath='{.metadata.labels.app\.kubernetes\.io/version}'
```

Check your current DynaKube API version:

```
kubectl get dynakubes -n dynatrace -o custom-columns='NAME:.metadata.name,API VERSION:.apiVersion'
```

Check which API versions have ever been used to store DynaKubes in this cluster:

```
kubectl get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

Every API version listed in `.status.storedVersions` must still be served by the Dynatrace Operator version you're upgrading to. If an entry is no longer served, you must first upgrade to an intermediate Operator version that still supports it so the stored resources can be converted and the obsolete entry removed.

`v1beta1` and `v1beta2` are a special exception: if the output contains either of them, **only Dynatrace Operator 1.7.3** can convert these resources and remove the entries. No other version will fix it - see [Upgrade steps](#upgrade-steps).

### DynaKube API version overview

| DynaKube API version | Introduced | Deprecated | Not served [1](#fn-1-1-def) | Removed | Migration guides |
| --- | --- | --- | --- | --- | --- |
| v1beta6 | 1.8.0 |  |  |  |  |
| v1beta5 | 1.6.0 |  |  |  | [to v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta5-v1beta6 "Migrate your v1beta5 DynaKube CR to the v1beta6 apiVersions.") |
| v1beta4 | 1.5.0 | 1.9.0 |  |  | [to v1beta6](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta6 "Migrate your v1beta4 DynaKube CR to the v1beta6 apiVersions."), [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta4-v1beta5 "Migrate your v1beta4 DynaKube CR to the v1beta5 apiVersions.") |
| v1beta3 | 1.4.0 | 1.7.0 | 1.8.0 | 1.9.0 | [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta5 "Migrate your v1beta3 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta3-v1beta4 "Migrate your v1beta3 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta2 | 1.2.0 | 1.6.0 | 1.7.0 | 1.8.0 | [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta5 "Migrate your v1beta2 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta2-v1beta4 "Migrate your v1beta2 DynaKube CR to the v1beta4 apiVersions.") |
| v1beta1 | 0.3.0 | 1.6.0 | 1.7.0 | 1.8.0 | [to v1beta5](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5 "Migrate your v1beta1 DynaKube CR to the v1beta5 apiVersions."), [to v1beta4](/managed/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta4 "Migrate your v1beta1 DynaKube CR to the v1beta4 apiVersions.") |

1

The stated Dynatrace Operator version no longer serves this API version. You can't apply new resources using it. The schema is retained in the CRD for automatic conversion only and will be removed in a subsequent release. For more details, see [Removal process](#deprecation).

### Upgrade steps

Dynatrace Operator versions **older than 1.4** stored DynaKube as `v1beta1` or `v1beta2`. These API versions are removed in 1.8.0, and **1.7.3 is the last and only release that can migrate them**.

What matters is your cluster's history, not your current version: if your DynaKube was *ever* stored as `v1beta1` or `v1beta2` (anywhere along the upgrade path), you must pass through 1.7.3 before going to 1.8.0 or later - even if you've upgraded the Operator several times since. Skipping this step blocks both the operator and CRD upgrade.

You can confirm this by checking the CRD's `.status.storedVersions` - see [Check your current versions](#check-versions).

1. **Upgrade to version 1.7.3**

   This step automatically converts your DynaKube to a supported API version.

   Helm

   Manifest

   Do not use `--reuse-values` when upgrading across major Dynatrace Operator versions. New chart versions introduce fields that have no defaults in older values files, which causes nil pointer errors during templating. Pass only the values you need explicitly with `--set` or `-f values.yaml`.

   ```
   helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



   --version 1.7.3 \



   --namespace dynatrace
   ```

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-operator/releases/download/v1.7.3/kubernetes-csi.yaml
   ```

   Wait for the Operator pod to restart and give it roughly 10 minutes to ensure a healthy reconciliation.
2. **Upgrade to the latest version**

   To upgrade, follow [Update Dynatrace Operator](#update).

   The upgrade automatically cleans up obsolete CRD entries and migrates your DynaKube to the current API version (`v1beta6`).

   When installing with manifests, make sure to provide the right RBAC permissions for the cleanup job, see [Dynatrace Operator security and RBAC](/managed/ingest-from/setup-on-k8s/reference/security#upgrade-support "This page provides an overview of the Dynatrace components, their default configurations, and the permissions they require").
3. **Verify the upgrade**

   Check that the Dynatrace Operator is healthy, your DynaKube is on `v1beta6`, and `.status.storedVersions` is clean:

   ```
   kubectl get pods -n dynatrace



   kubectl get dynakubes -n dynatrace -o custom-columns='NAME:.metadata.name,API VERSION:.apiVersion'



   kubectl get crd dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
   ```

   The expected output is `dynatrace.com/v1beta6` and `["v1beta6"]`. Update your stored manifests to reflect the new `apiVersion` so they remain your source of truth.

   Check for warning events about outdated CRD versions:

   ```
   kubectl get events -n dynatrace --field-selector reason=Warning
   ```

### What happens during the upgrade to 1.7.3

When you follow the steps above, the Dynatrace Operator takes care of two concerns automatically:

* **DynaKube custom resource conversion** to a supported API version. The Operator auto-converts DynaKubes only while the source version is still served by the CRD. Once a version is removed, conversion is no longer possible - this is why version 1.7.3 is mandatory for resources on `v1beta1` or `v1beta2`.
* **`.status.storedVersions` cleanup** on the CRD. Kubernetes tracks every API version that has ever been used to store data. Entries that remain listed there but no longer exist in the schema block any further CRD update. From 1.7.3 onward, the Dynatrace Operator removes obsolete entries automatically - either via a Helm pre-upgrade hook (for Helm-based installations) or an Operator init container (for manifest-based installations). Because this cleanup logic was introduced in 1.7.3 and does not exist in earlier releases, **1.7.3 is the mandatory entry point** for clusters that still carry `v1beta1` or `v1beta2` in `storedVersions`.