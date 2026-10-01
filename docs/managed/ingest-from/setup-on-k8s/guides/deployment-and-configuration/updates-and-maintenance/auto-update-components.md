---
title: Configure auto-update for Dynatrace Operator managed components
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components
---

# Configure auto-update for Dynatrace Operator managed components

# Configure auto-update for Dynatrace Operator managed components

* How-to guide
* 2-min read
* Updated on Sep 08, 2026

Dynatrace Operator manages the rollout and updates of the following components in Kubernetes:

* OneAgent
* ActiveGate
* CodeModules
* Extension Execution Controller (EEC)
* Standalone Log Module
* SQL Extension Executor
* EdgeConnect (configured via the EdgeConnect Custom Resource)

The default settings for OneAgent and ActiveGate automatically roll out updates as soon as they become available. DynaKube also updates all pods automatically when it detects updates. Note that updates may take up to 15 minutes due to Dynatrace Operator checking for updates at 15-minute intervals. Setting a custom `image` disables automatic updates.

Update windows do not apply in Kubernetes environments.

## Automatic updates with public registry images

Dynatrace Operator version 1.10.0+

Dynatrace Operator can automatically resolve the latest public image URIs for managed components from your Dynatrace environment, without manual `image` field configuration.

When this feature is active, Dynatrace Operator periodically syncs the image references for each component from your Dynatrace environment and applies them automatically.

### Enable automatic image resolution

1. Remove the `image` and `codeModulesImage` fields from your DynaKube if set — their values take precedence over automatically resolved images for the affected component.
2. Set the `feature.dynatrace.com/use-public-registry` annotation on your DynaKube:

   ```
   apiVersion: dynatrace.com/v1beta6



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/use-public-registry: "true"



   spec:



   apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



   ...
   ```

Enable automatically with a platform token

When your DynaKube uses a platform token, Dynatrace Operator enables public registry resolution automatically. No annotation is required. You can set `spec.publicRegistryOverride` to use a specific supported public registry.

Override the registry host

To request images from a specific supported public registry, set `spec.publicRegistryOverride` to one of the registry hosts listed in [Supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.") — for example, `public.ecr.aws` for Amazon ECR Public or `registry-1.docker.io` for Docker Hub. Dynatrace Operator forwards the host to your Dynatrace environment when resolving image URIs.

### What changes when the feature is enabled

* **Component images**: Dynatrace Operator resolves image references from your Dynatrace environment.

  + Container images for Extension Execution Controller, Dynatrace Log Module and the SQL Extension Executor are supported from Dynatrace SaaS 1.350 and Dynatrace Operator 1.11. In older versions, these components always require a image specified in the respective `spec.templates` field.
* **Pod restarts**: All managed component pods restart when the feature is first enabled.
* **Application injection**: The init container image injected into application pods changes on the pod's next restart, if you are not using the CSI driver or if you use [node image pull via ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). In both cases the webhook switches from ZIP-download mode to self-extracting mode using the CodeModules image.

### Verify

After enabling, confirm that Dynatrace Operator is resolving images from the public registry:

```
kubectl get dynakube <dynakube-name> -n dynatrace -o jsonpath='{.status.activeGate.source}'
```

A value of `public-registry` confirms the ActiveGate image was resolved from the public registry. Check `status.oneAgent.source` and `status.codeModules.source` similarly for OneAgent and CodeModules.

## Automatic updates with image from the Dynatrace built-in registry

### Configure OneAgent auto-update

Set the target version on the Dynatrace Server to a relative version, for example, `Latest stable version`. Dynatrace Operator will periodically check for updates and propagate them to the Kubernetes environment. Updating the OneAgent version always restarts the OneAgent pods.

Minimal DynaKube configuration that uses auto-update:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



cloudNativeFullStack: {}
```

To disable auto-update, set the `image` field in the DynaKube. Omit the field to keep auto-update enabled.

```
# Auto-update enabled (default) — omit image



spec:



oneAgent:



cloudNativeFullStack: {}



# Auto-update disabled — pin a specific image



spec:



oneAgent:



cloudNativeFullStack:



image: public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>
```

For CodeModules, while Dynatrace Operator downloads new images, applications update only when they restart. Keep in mind that autoscaling also injects the most recent CodeModule.

### Configure ActiveGate auto-update

The ActiveGate target version configured in Dynatrace determines the image used by Dynatrace Operator. Dynatrace Operator periodically checks for updates and applies them automatically.

Minimal DynaKube configuration that uses auto-update:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



activeGate:



capabilities:



- kubernetes-monitoring
```

To disable auto-update, set the `image` field in the DynaKube. Omit the field to keep auto-update enabled.

```
# Auto-update enabled (default) — omit image



spec:



activeGate:



capabilities:



- kubernetes-monitoring



# Auto-update disabled — pin a specific image



spec:



activeGate:



capabilities:



- kubernetes-monitoring



image: public.ecr.aws/dynatrace/dynatrace-activegate:<tag>
```