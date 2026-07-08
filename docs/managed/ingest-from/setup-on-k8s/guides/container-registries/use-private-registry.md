---
title: Use a private registry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry
---

# Use a private registry

# Use a private registry

* 5-min read
* Updated on Jun 19, 2026

For users seeking greater control over their image hosting environment, Dynatrace offers the option to replicate images and signatures to private registries.

We recommend using a private registry for optimal performance and no rate limiting risks in high-demand and dynamic environments. Furthermore, to meet security standards and ensure software integrity while mitigating supply chain risks, image scanning and signature verification against Dynatrace images can be applied and is recommended.

By replicating Dynatrace images to your private registry, you can seamlessly merge excellent delivery performance with the assurance of secure, signed, and immutable images. Additionally, we provide multi-arch images to ensure compatibility across various platforms supporting ARM64 (AArch64) and x86-64 CPU architectures on Linux.

This page provides instructions for using Dynatrace signed and immutable container images hosted on a private registry.

## Prerequisites

Before you begin, be sure to meet the following prerequisites:

* Required Dynatrace Operator version is v0.11 or later
* Required Target CPU architectures are ARM64 (AArch64) and/or x86-64
* Required Allow egress traffic to public registry
* Required Private registry with Dynatrace images stored

For guidance on storing Dynatrace images in your private registry, see [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries").

## Create a pull secret

When Dynatrace container images are served by a private registry requiring authentication, a pull secret is **required** if node image pull is not used and any of the following conditions apply:

* DynaKube configured for Full Observability ([Cloud-Native Full-Stack](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.") monitoring)
* DynaKube configured for Application Observability ([Application-Only](/managed/ingest-from/setup-on-k8s/how-it-works#auto "In-depth description on how the deployment on Kubernetes works.") monitoring) **with** CSI driver enabled

Since Dynatrace Operator version 0.14.0, `customPullSecret` field is required unless [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") feature is used.

The pull secret (the `customPullSecret` field in a DynaKube configuration) is generally used for authenticating against the private registry and accessing its artifacts (images). The following points describe the requirements for a pull secret in more detail:

* When Cloud-Native Full-Stack or Application-Only monitoring with the CSI driver is configured, the CSI driver requires a pull secret to access the private registry as it attempts to directly download the Dynatrace Code Modules image from the private registry.
* When using the [node image pull feature](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, the `customPullSecret` field only affects components managed by Dynatrace Operator (in the `dynatrace` namespace). For injected application pods, you must manually configure pull secrets at the node, namespace, or pod level. For details, see [node image pull prerequisites](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull").

To create a pull secret, follow this [Kubernetes documentation﻿](https://dt-url.net/p403yu6) on how to create a Kubernetes secret based on existing credentials or by providing credentials on the command line.

## Deploy Dynatrace Operator with images from private registry

This section guides you through deploying Dynatrace Operator with its container image coming from a private registry.

Dynatrace Operator consists of multiple components (operator, webhook, CSI driver), all of which use the same `dynatrace-operator` image with specific deployment configurations per component.

Helm

Manifest

The following command installs Dynatrace Operator and configures container images to be pulled from a private registry (for example, "registry.my-company.com") by setting the `imageRef.repository`, `imageRef.tag`, and `customPullSecret` (is propagated into `imagePullSecrets` of PodSpecs) values:

If you are using Helm version 4.0+, you must use `--rollback-on-failure` instead of the `--atomic` flag.

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "imageRef.repository=<your-private-registry>/dynatrace-operator" \



--set "imageRef.tag=<tag>" \



--set "customPullSecret=<secretName>" \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Alternatively, an already existing installation can be upgraded as follows:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--set "imageRef.repository=<your-private-registry>/dynatrace-operator" \



--set "imageRef.tag=<tag>" \



--set "customPullSecret=<secretName>" \



--namespace dynatrace \



--reuse-values



--atomic \
```

To avoid tedious and error-prone editing of large YAML files, we recommend using Helm for manifest generation via `helm template`.

If you prefer to make your modifications directly, however, be sure to adjust the `image` and `imagePullSecrets` fields on all containers and pods where the `dynatrace-operator` image occurs.

## Configure DynaKube to use images from private registry

To instruct Dynatrace Operator to use container images from a private registry, just configure a pull secret via the `customPullSecret` field for registry authentification and respective `image` fields in the DynaKube custom resource. The configured images will be deployed to your Kubernetes cluster to set up monitoring components.

The following DynaKube snippet demonstrates how to configure [Cloud-Native Full-Stack monitoring setup](/managed/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.") using Dynatrace container images from a private registry.

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



customPullSecret: <secretName>



oneAgent:



cloudNativeFullstack:



...



image: <your-private-registry>/dynatrace-oneagent:<tag>



codeModulesImage: <your-private-registry>/dynatrace-codemodules:<tag>



...



activeGate:



...



image: <your-private-registry>/dynatrace-activegate:<tag>



...
```

After configuring the required fields, the DynaKube custom resource must be applied to the Kubernetes cluster.

If the [`KubeletEnsureSecretPulledImages`﻿](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification) feature gate is enabled on your Kubernetes cluster, you may need to ensure that all nodes are authenticated to access the registry.
For security reasons, Dynatrace Operator does not replicate provided pull secrets into application namespaces or mount them to pods outside of Dynatrace Operator's control. Instead, you must manually configure pull secrets at one of the following levels:

* **Node level**: Configure registry authentication directly on each node.
* **Namespace level**: Add the pull secret to the namespace where application pods are deployed.
* **Pod level**: Configure the pull secret via the `imagePullSecrets` field in the pod specification of your application pods.

For more information on manual pull secret configuration, see [Kubernetes documentation on pulling images from private registries﻿](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).

For additional information regarding `customPullSecret` field, `image` fields, or the DynaKube custom resource, see further examples below or go to the [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") reference page.

Looking for more examples?

#### Application and Kubernetes Observability

The following custom resource snippet describes how to configure DynaKube for [Application Observability and Kubernetes observability](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") with container images from your private registry:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



...



customPullSecret: <secretName>



oneAgent:



applicationMonitoring:



...



codeModulesImage: <your-private-registry>/dynatrace-codemodules:<tag>



...



activeGate:



...



image: <your-private-registry>/dynatrace-activegate:<tag>



...
```

## Verify image signature

All of our immutable and signed container images adhere to best practices, enhancing security and shielding against supply chain attacks. To learn how to verify signatures and guarantee software integrity, see [Verify Dynatrace image signatures](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures").

## Related topics

* [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")
* [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Use a public registry")