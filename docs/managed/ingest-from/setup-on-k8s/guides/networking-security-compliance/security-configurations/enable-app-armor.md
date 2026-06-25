---
title: Enable AppArmor for enhanced security
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor
scraped: 2026-05-12T12:14:30.813706
---

# Enable AppArmor for enhanced security

# Enable AppArmor for enhanced security

* 2-min read
* Updated on Mar 09, 2026

You can make Dynatrace Operator more secure by enabling [AppArmorï»¿](https://dt-url.net/3403y6b).

## Enable AppArmor for Dynatrace Operator, Webhook, and CSI driver

Depending on whether you deployed Dynatrace Operator using **Helm** or by directly applying **YAML manifests**.

Helm

Manifest

AppArmor configuration changes in Kubernetes 1.31+

Starting with Kubernetes version 1.31, AppArmor profiles are configured using `securityContext.appArmorProfile` instead of pod annotations. The previous `operator.apparmor`, `webhook.apparmor`, and `csidriver.apparmor` Helm values are deprecated. Use the `appArmorProfile` values shown below instead. The deprecated values are supported until Kubernetes 1.30 and OpenShift 4.17 reach end of support (July 2027).

Add the `appArmorProfile` field to `podSecurityContext` in your `values.yaml` to enable AppArmor for Dynatrace Operator and Webhook:

```
operator:



podSecurityContext:



appArmorProfile:



type: RuntimeDefault



webhook:



podSecurityContext:



appArmorProfile:



type: RuntimeDefault
```

For the **CSI driver**, set `appArmorProfile` on each container's `securityContext` individually:

```
csidriver:



csiInit:



securityContext:



appArmorProfile:



type: RuntimeDefault



server:



securityContext:



appArmorProfile:



type: RuntimeDefault



provisioner:



securityContext:



appArmorProfile:



type: RuntimeDefault



registrar:



securityContext:



appArmorProfile:



type: RuntimeDefault



livenessprobe:



securityContext:



appArmorProfile:



type: RuntimeDefault
```

On Kubernetes version 1.31+, AppArmor profiles are configured using `securityContext.appArmorProfile` instead of pod annotations.

AppArmor pod annotation deprecation

On Kubernetes version 1.30 and earlier, AppArmor was configured using the `container.apparmor.security.beta.kubernetes.io/<container-name>: runtime/default` pod annotation. This approach is deprecated. Instead, use `securityContext.appArmorProfile`, which is natively supported on Kubernetes version 1.31+.

* **Dynatrace Operator and Webhook** require updating the `securityContext` in the deployment YAML:

  ```
  kind: Deployment



  metadata:



  name: dynatrace-webhook



  spec:



  template:



  spec:



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  kind: Deployment



  metadata:



  name: dynatrace-operator



  spec:



  template:



  spec:



  securityContext:



  appArmorProfile:



  type: RuntimeDefault
  ```
* **CSI driver** requires setting `appArmorProfile` on each container's `securityContext` in the DaemonSet:

  ```
  kind: DaemonSet



  metadata:



  name: dynatrace-oneagent-csi-driver



  spec:



  template:



  spec:



  initContainers:



  - name: csi-init



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  containers:



  - name: server



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  - name: provisioner



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  - name: registrar



  securityContext:



  appArmorProfile:



  type: RuntimeDefault



  - name: liveness-probe



  securityContext:



  appArmorProfile:



  type: RuntimeDefault
  ```

## Enable AppArmor for operator-deployed components

To enable AppArmor for components that are deployed by the Dynatrace Operator into monitored clusters, you need to opt in for each component separately.

### ActiveGate

On Kubernetes 1.31+, AppArmor is configured via `securityContext`. On older clusters, an annotation is used instead. The Operator automatically selects the appropriate method based on the cluster version. To opt in, add the following annotation to your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/activegate-apparmor: true
```

### OneAgent

On Kubernetes 1.31+, the Operator automatically applies AppArmor via `securityContext` â no user action is required. On Kubernetes 1.30 and earlier, AppArmor for OneAgent is not automatically applied. To use a custom AppArmor profile on older clusters, see [Enable a custom AppArmor profile for OneAgent](#custom-apparmor).

### EdgeConnect

To enable AppArmor for EdgeConnect, add the AppArmor annotation via the DynaKube `spec.edgeConnect.annotations` field:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



edgeConnect:



annotations:



container.apparmor.security.beta.kubernetes.io/edge-connect: runtime/default
```

The `container.apparmor.security.beta.kubernetes.io` annotation was deprecated in Kubernetes 1.30 and removed in Kubernetes 1.31. On Kubernetes 1.31+, the annotation has no effect for EdgeConnect. `securityContext`-based AppArmor configuration for EdgeConnect is not yet supported.

### Enable a custom AppArmor profile for OneAgent

You can restrict the OneAgent access to a desired set of features. See below for how to enable a custom AppArmor profile and apply it to the OneAgent pods.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a custom OneAgent AppArmor profile**](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#create-profile "Apply AppArmor profiles on Dynatrace components for enhanced security.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Install the profile on all worker nodes**](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#install-profile "Apply AppArmor profiles on Dynatrace components for enhanced security.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Enforce the profile on all OneAgent pods**](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/enable-app-armor#enforce-profile "Apply AppArmor profiles on Dynatrace components for enhanced security.")

#### Step 1 Create a custom OneAgent AppArmor profile

See [Run OneAgent as a Docker container](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#with-apparmor "Install and update Dynatrace OneAgent as a Docker container.") for details on how to create a custom AppArmor profile.

#### Step 2 Install the profile on all worker nodes

OneAgent is deployed as a daemonset by default, which means pods that use the AppArmor profile will be used on every node. You therefore need to install the OneAgent AppArmor profile **on all nodes**.

Depending on the environment, this can be done in several ways, such as by using the [kube-apparmor-managerï»¿](https://dt-url.net/5g034s7) or the [security-profiles-operatorï»¿](https://dt-url.net/uz23475). Please refer to the official documentation of these tools on how to apply them in your cluster.

#### Step 3 Enforce the profile on all OneAgent pods

To enable AppArmor for all the OneAgent pods, add the `container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent: localhost/oneagent` annotation to one of the following fields, depending on your deployment:

* `oneAgent.classicFullStack.annotations`
* `oneAgent.cloudNativeFullStack.annotations`
* `oneAgent.hostMonitoring.annotations`

Example for `cloudNativeFullStack` deployment:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



cloudNativeFullStack:



annotations:



container.apparmor.security.beta.kubernetes.io/dynatrace-oneagent: localhost/oneagent
```