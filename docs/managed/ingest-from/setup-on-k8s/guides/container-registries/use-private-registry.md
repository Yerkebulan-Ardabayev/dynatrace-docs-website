---
title: Use a private registry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry
---

# Use a private registry

# Use a private registry

* 5-min read
* Updated on Jul 10, 2026

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

When your private registry requires authentication, Dynatrace Operator needs credentials to pull the images. You provide these credentials as a Kubernetes pull secret.

The `customPullSecret` field in a DynaKube configuration authenticates **only the components that Dynatrace Operator manages in the `dynatrace` namespace**.

Dynatrace Operator does **not** copy this pull secret into your application namespaces or add it to your injected application pods. Following the principle of least privilege, and to limit the security exposure of your registry credentials, Dynatrace Operator does not replicate the pull secret outside the `dynatrace` namespace. Injected pods require the pull secret because of the added init container, so it needs to be distributed to either the node, serviceAccount or pod directly.

### Where the pull secret applies

The following table shows which image the Kubernetes node pulls in each scenario, whether the DynaKube `customPullSecret` covers it, and what you need to configure.

| Scenario | Image the node pulls for the pod | Is `customPullSecret` enough? | What you need to configure |
| --- | --- | --- | --- |
| Operator-managed components in the `dynatrace` namespace | Dynatrace Operator image | Yes | Set `customPullSecret` in the DynaKube. |
| Injected application pods with node image pull ([ephemeral volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") or [via CSI volume](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-node-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.")) | OneAgent code modules image (init container) | No | Distribute a pull secret to your application namespace, node, or pod. See [Provide pull secrets for injected workloads](#injected-workloads). |
| Injected application pods with [CSI driver image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."), [CSI driver ZIP download](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-zip "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."), or [ZIP download](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#zip-download "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") | Dynatrace Operator image (init container) | No | Distribute a pull secret to your application namespace, node, or pod. See [Provide pull secrets for injected workloads](#injected-workloads). |

For [CSI driver image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#csi-image-pull "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."), `customPullSecret` additionally covers the OneAgent code modules image, which the CSI driver pulls in the `dynatrace` namespace. The injected pods still need their own pull secret for the init container image.

### Create the pull secret

To create a pull secret for the operator-managed components, follow this [Kubernetes documentation﻿](https://dt-url.net/p403yu6) on how to create a Kubernetes secret based on existing credentials or by providing credentials on the command line. Reference it through the `customPullSecret` field in your DynaKube, as shown in [Configure DynaKube to use images from private registry](#configure-dynakube).

### Provide pull secrets for injected workloads

Injected pods run a Dynatrace init container whose image the Kubernetes node must pull. Because Dynatrace Operator does not distribute the `customPullSecret` outside the `dynatrace` namespace, you must provide these credentials yourself at one of the following levels:

* **Node level**: Configure registry authentication directly on each node.
* **Namespace level**: Add the pull secret to every namespace and the respective serviceAccounts where injected application pods run. Pull secrets are only valid in their own namespace, so repeat this for each application namespace.
* **Pod level**: Configure the pull secret through the `imagePullSecrets` field in the pod specification of your application pods.

For details, see the [Kubernetes documentation on pulling images from private registries﻿](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).

Previously, an application pod could reuse an image that another pod had already pulled onto the same node, even without its own credentials. Since Kubernetes 1.35, the [`KubeletEnsureSecretPulledImages`﻿](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification) feature gate is enabled by default and the kubelet verifies pull credentials per pod, even for images already cached on the node. If you don't distribute pull secrets as described above, injected pods fail with `ImagePullBackOff`.

## Deploy Dynatrace Operator with images from private registry

This section guides you through deploying Dynatrace Operator with its container image coming from a private registry.

Dynatrace Operator consists of multiple components, all of which use the same `dynatrace-operator` image with specific deployment configurations per component.

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



--reset-then-reuse-values \



--atomic \
```

To avoid tedious and error-prone editing of large YAML files, we recommend using Helm for manifest generation via `helm template`.

If you prefer to make your modifications directly, however, be sure to adjust the `image` and `imagePullSecrets` fields on all containers and pods where the `dynatrace-operator` image occurs.

## Configure DynaKube to use images from private registry

To instruct Dynatrace Operator to use container images from a private registry, configure the respective `image` fields in the DynaKube custom resource. The configured images will be deployed to your Kubernetes cluster to set up monitoring components.

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

The `customPullSecret` field authenticates only the operator-managed components in the `dynatrace` namespace. If the Kubernetes node pulls the OneAgent code modules image for your injected application pods, you must provide the pull secret yourself. For details, see [Provide pull secrets for injected workloads](#injected-workloads).

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
* [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")