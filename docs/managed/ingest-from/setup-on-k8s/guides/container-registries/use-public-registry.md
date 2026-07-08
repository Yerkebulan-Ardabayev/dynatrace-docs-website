---
title: Use a public registry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry
---

# Use a public registry

# Use a public registry

* 5-min read
* Updated on Sep 05, 2025

To accommodate diverse infrastructure requirements and organizational preferences, Dynatrace images are available on selected public registries. These images adhere to best practices, ensuring immutability and signing for enhanced security and resilience against potential supply chain risks.

Explore our supported public registries with multi-arch Dynatrace container images supporting ARM64 (AArch64), x86-64, s390x, and PPC64le CPU architectures on Linux, ensuring compatibility across various platforms.

This page provides instructions for using Dynatrace signed and immutable container images hosted on supported public registries.

## Prerequisites

Before you begin, be sure to meet the following prerequisites:

* Required Dynatrace Operator version is v0.11 or later
* Required Target CPU architectures are ARM64 (AArch64), x86-64, s390x, and/or ppc64le
* Required Allow egress traffic to public registry

#### Limitations

Note that the following configurations are not supported in combination with public registries:

* Application monitoring without CSI driver
* Host monitoring without CSI driver
* Classic Full-Stack monitoring - Alternatively, use a private registry for [Classic Full-Stack monitoring](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry#classic-full-stack "Store Dynatrace images in private registries")

Start using these fortified images today for a safer and more efficient containerized monitoring experience:

* [Deploy Dynatrace Operator](#deploy-dynatrace-operator-with-images-from-public-registry) with container images from a public registry
* [Configure DynaKube](#configure-dynakube-to-use-images-from-public-registry) to use container images from a public registry for monitoring components

## Supported public registries

Dynatrace publishes its container images to [Amazon ECR﻿](https://gallery.ecr.aws/dynatrace) and [Docker Hub﻿](https://hub.docker.com/u/dynatrace):

| Amazon ECR | Docker Hub |
| --- | --- |
| public.ecr.aws/dynatrace/dynatrace-activegate | dynatrace/dynatrace-activegate |
| public.ecr.aws/dynatrace/dynatrace-codemodules | dynatrace/dynatrace-codemodules |
| public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector | dynatrace/dynatrace-k8s-node-config-collector |
| public.ecr.aws/dynatrace/dynatrace-logmodule | dynatrace/dynatrace-logmodule |
| public.ecr.aws/dynatrace/dynatrace-oneagent | dynatrace/dynatrace-oneagent |
| public.ecr.aws/dynatrace/dynatrace-operator[1](#fn-1-1-def) | dynatrace/dynatrace-operator |
| public.ecr.aws/dynatrace/dynatrace-otel-collector | dynatrace/dynatrace-otel-collector |
| public.ecr.aws/dynatrace/edgeconnect | dynatrace/edgeconnect |

1

Available from Dynatrace Operator version 1.0.0

Rate limiting

Be aware that, when accessing public registries, there is a potential risk of encountering rate limiting. To ensure a smoother experience and reduce this risk, we recommend using a private registry or authenticating against the respective registry.

Image tagging

Dynatrace employs version-based image tagging for its container images and does **not** use mutable image tags like `latest`. For more information on tags, please visit the respective public registry repository.

## Deploy Dynatrace Operator with images from public registry

By default, the Dynatrace Operator image `dynatrace/dynatrace-operator` is served by the public registry on AWS ECR.

Dynatrace Operator consists of multiple components (operator, webhook, CSI driver), all of which use the same `dynatrace-operator` image with specific deployment configurations per component.

Helm

Kustomize

Manifest

If you are using Helm version 4.0+, you must use `--rollback-on-failure` instead of the `--atomic` flag.

The following command installs Dynatrace Operator and configures container images to be pulled from a public registry:

```
helm install dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--create-namespace \



--namespace dynatrace \



--atomic \
```

Alternatively, an existing installation can be upgraded as follows:

```
helm upgrade dynatrace-operator oci://public.ecr.aws/dynatrace/dynatrace-operator \



--reuse-values \



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

The Dynatrace Operator can easily be instructed to use images from a public registry by configuring the respective `image` fields in the DynaKube custom resource. The configured images will be deployed to your Kubernetes cluster to set up monitoring components.

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



image: public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>



codeModulesImage: public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect - see note below



...



activeGate:



...



image: public.ecr.aws/dynatrace/dynatrace-activegate:<tag>



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



codeModulesImage: public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>



# version:         # has no effect



...



activeGate:



...



image: public.ecr.aws/dynatrace/dynatrace-activegate:<tag>



...
```

## Verify image signature

All of our immutable and signed container images adhere to best practices, enhancing security and shielding against supply chain attacks. To learn how to verify signatures and guarantee software integrity, see [Verify Dynatrace image signatures](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures").

## Related topics

* [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")