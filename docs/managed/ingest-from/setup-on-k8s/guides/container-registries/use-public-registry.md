---
title: Use a public registry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry
---

# Use a public registry

# Use a public registry

* 6-min read
* Updated on Jul 01, 2026

To accommodate diverse infrastructure requirements and organizational preferences, Dynatrace images are available on selected public registries. These images adhere to best practices, ensuring immutability and signing for enhanced security and resilience against potential supply chain risks.

Explore our supported public registries with multi-arch Dynatrace container images supporting ARM64 (AArch64), x86-64, s390x, and PPC64le CPU architectures on Linux, ensuring compatibility across various platforms.

This page provides instructions for using Dynatrace signed and immutable container images hosted on supported public registries.

Start using these fortified images today for a safer and more efficient containerized monitoring experience:

* [Resolve public registry images automatically](#automatic-public-registry) for Dynatrace Operator managed components
* [Deploy Dynatrace Operator](#deploy-dynatrace-operator-with-images-from-public-registry) with container images from a public registry
* [Configure DynaKube](#configure-dynakube-to-use-images-from-public-registry) to use container images from a public registry for monitoring components

## Prerequisites

Before you begin, be sure to meet the following prerequisites:

* Dynatrace SaaS version 1.343+
* Dynatrace Operator version 0.11+
* Target CPU architectures are ARM64 (AArch64), x86-64, s390x, and/or ppc64le
* Allow egress traffic to public registry

### Limitations

Note that the following configurations are not supported in combination with public registries:

* Classic Full-Stack monitoring

## Supported public registries

Dynatrace publishes its container images to [Amazon ECR Public﻿](https://gallery.ecr.aws/dynatrace) and [Docker Hub﻿](https://hub.docker.com/u/dynatrace). When using [automatic image resolution](#automatic-public-registry), set `spec.publicRegistryOverride` to `public.ecr.aws` for Amazon ECR Public or `registry-1.docker.io` for Docker Hub to request images from a specific registry.

| Amazon ECR Public | Docker Hub |
| --- | --- |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-activegate | registry-1.docker.io/dynatrace/dynatrace-activegate |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-codemodules | registry-1.docker.io/dynatrace/dynatrace-codemodules |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-eec | registry-1.docker.io/dynatrace/dynatrace-eec |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-k8s-node-config-collector | registry-1.docker.io/dynatrace/dynatrace-k8s-node-config-collector |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-logmodule | registry-1.docker.io/dynatrace/dynatrace-logmodule |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-oneagent | registry-1.docker.io/dynatrace/dynatrace-oneagent |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-operator | registry-1.docker.io/dynatrace/dynatrace-operator |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-otel-collector | registry-1.docker.io/dynatrace/dynatrace-otel-collector |
| public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-sql-extension-executor | registry-1.docker.io/dynatrace/dynatrace-sql-extension-executor |
| public.ecr.aws/registry-1.docker.io/dynatrace/edgeconnect | registry-1.docker.io/dynatrace/edgeconnect |

Rate limiting

Be aware that, when accessing public registries, there is a potential risk of encountering rate limiting. To ensure a smoother experience and reduce this risk, we recommend using a private registry.

Image tagging

Dynatrace employs version-based image tagging for its container images and does **not** use mutable image tags like `latest`. For more information on tags, please visit the respective public registry repository.

## Automatic Image Resolution with Dynatrace Operator

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

* **Component images**: Dynatrace Operator resolves image references from your Dynatrace environment for OneAgent, ActiveGate, and CodeModules. Components without a default image source (Extension Execution Controller, Standalone Log Module, SQL Extension Executor) always require a custom image in the respective `spec.templates` field.
* **Pod restarts**: All managed component pods restart when the feature is first enabled.
* **Application injection**: The init container image injected into application pods changes on the pod's next restart, if you are not using the CSI driver or if you use [node image pull via ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."). In both cases the webhook switches from ZIP-download mode to self-extracting mode using the CodeModules image.

### Verify

After enabling, confirm that Dynatrace Operator is resolving images from the public registry:

```
kubectl get dynakube <dynakube-name> -n dynatrace -o jsonpath='{.status.activeGate.source}'
```

A value of `public-registry` confirms the ActiveGate image was resolved from the public registry. Check `status.oneAgent.source` and `status.codeModules.source` similarly for OneAgent and CodeModules.

## Deploy Dynatrace Operator with images from public registry

The Dynatrace Operator Helm chart is available as an OCI artifact from both Amazon ECR and Docker Hub.
Regardless of which registry you use to pull the chart, container image references default to Amazon ECR. If you install the chart from Docker Hub and want all images pulled from Docker Hub as well, you can use `--set imageRef.repository=docker.io/registry-1.docker.io/dynatrace/dynatrace-operator` with your `helm install` or `helm upgrade` command.

Dynatrace Operator consists of multiple components (operator, webhook, CSI driver), all of which use the same `dynatrace-operator` image with specific deployment configurations per component.

Helm

Kustomize

Manifest

If you are using Helm version 4.0+, you must use `--rollback-on-failure` instead of the `--atomic` flag.

The following command installs Dynatrace Operator and configures container images to be pulled from a public registry:

```
helm install dynatrace-operator oci://public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic
```

Alternatively, an existing installation can be upgraded as follows:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-operator \



--reset-then-reuse-values \



--atomic \



--namespace dynatrace
```

Use the following kustomization to conveniently install or update Dynatrace Operator by applying the necessary manifests.

```
apiVersion: kustomize.config.k8s.io/v1beta1



kind: Kustomization



namespace: Dynatrace



resources:



- namespace.yaml # can be created by `kubectl create namespace dynatrace --dry-run=client -oyaml > namespace.yaml`



- https://github.com/Dynatrace/dynatrace-operator/releases/download/<version>/kubernetes-csi.yaml
```

To avoid tedious and error-prone editing of large YAML files, we recommend using either Helm or Kustomize for manifest manipulation.

If you prefer to make your modifications directly, however, be sure to adjust the `image` fields on all containers and pods where the `dynatrace-operator` image occurs.

## Configure DynaKube to use images from public registry

**Classic Full-Stack** monitoring is not supported in combination with a public registry.

For PPC64le architecture, additional configuration is required. For details, see [ActiveGate container image](/managed/ingest-from/dynatrace-activegate/activegate-in-container#additional-configuration "Deploy a containerized ActiveGate.").

To use images from a public registry, configure the respective `image` fields in the DynaKube custom resource. Dynatrace Operator then deploys the configured images to your Kubernetes cluster to set up monitoring components. Alternatively, Dynatrace Operator can [resolve public image references automatically](#automatic-public-registry) from your Dynatrace environment, without manual configuration.

The following DynaKube snippet demonstrates how to configure [Cloud-Native Full-Stack monitoring setup](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.") leveraging the public Amazon ECR registry.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



oneAgent:



cloudNativeFullstack:



...



image: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-oneagent:<tag>



codeModulesImage: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect - see note below



...



activeGate:



...



image: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-activegate:<tag>



...
```

Note that the `version` field has no effect when the `image` and/or `codeModulesImage` fields are set.

After configuring the required fields, the DynaKube custom resource must be applied to the Kubernetes cluster.

Looking for more examples?

#### Application and Kubernetes Observability with Amazon ECR

The following custom resource describes how to configure DynaKube for [Application Observability and Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"):

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



oneAgent:



applicationMonitoring:



...



codeModulesImage: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect



...



activeGate:



...



image: public.ecr.aws/registry-1.docker.io/dynatrace/dynatrace-activegate:<tag>



...
```

## Verify image signature

All of our immutable and signed container images adhere to best practices, enhancing security and shielding against supply chain attacks. To learn how to verify signatures and guarantee software integrity, see [Verify Dynatrace image signatures](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures").

## Related topics

* [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")
* [DynaKube feature flags for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.")
* [Configure auto-update for Dynatrace Operator managed components](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for all components managed by Dynatrace Operator")