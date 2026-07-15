---
title: Migrate to public registry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/migrate-to-public-registry
---

# Migrate to public registry

# Migrate to public registry

* How-to guide
* 3-min read
* Published Jul 01, 2026

To switch an existing Dynatrace Operator installation to automatic public registry image resolution, see [Automatic Image Resolution with Dynatrace Operator](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#automatic-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

## Prerequisites

* Dynatrace Operator version 1.10.0 or later
* Access to a [supported public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* Dynatrace SaaS 1.343 or later

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

* **Component images**: Dynatrace Operator resolves image references from your Dynatrace environment for OneAgent, ActiveGate, and CodeModules. Components without a default image source (Extension Execution Controller, Standalone Log Module, SQL Extension Executor) always require a custom image in the respective `spec.templates` field.
* **Pod restarts**: All managed component pods restart when the feature is first enabled.
* **Application injection**: The init container image injected into application pods changes on the pod's next restart, if you are not using the CSI driver or if you use [node image pull via ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). In both cases the webhook switches from ZIP-download mode to self-extracting mode using the CodeModules image.

### Verify

After enabling, confirm that Dynatrace Operator is resolving images from the public registry:

```
kubectl get dynakube <dynakube-name> -n dynatrace -o jsonpath='{.status.activeGate.source}'
```

A value of `public-registry` confirms the ActiveGate image was resolved from the public registry. Check `status.oneAgent.source` and `status.codeModules.source` similarly for OneAgent and CodeModules.

## Related topics

* [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* [Configure auto-update for Dynatrace Operator managed components](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator")