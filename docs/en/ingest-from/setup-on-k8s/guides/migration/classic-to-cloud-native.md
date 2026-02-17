---
title: Migrate from classic full-stack to cloud-native full-stack mode
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native
scraped: 2026-02-17T05:02:12.035415
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