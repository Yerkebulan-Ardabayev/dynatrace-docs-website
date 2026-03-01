---
title: Store Dynatrace images in private registries
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry
scraped: 2026-03-01T21:28:29.223775
---

# Store Dynatrace images in private registries

# Store Dynatrace images in private registries

* Latest Dynatrace
* 7-min read
* Published Feb 29, 2024

For users seeking greater control over their image hosting environment, Dynatrace offers the option to replicate images and signatures to private registries.

We recommend using a private registry for optimal performance and no rate limiting risks in high-demand and dynamic environments. Furthermore, to meet security standards and ensure software integrity while mitigating supply chain risks, image scanning and signature verification against Dynatrace images can be applied and is recommended.

By replicating Dynatrace images to your private registry, you can seamlessly merge excellent delivery performance with the assurance of secure, signed, and immutable images. We provide multi-arch images to ensure compatibility across various platforms supporting ARM64 (AArch64) and x86-64 CPU architectures on Linux.

This page offers guidance on securely storing Dynatrace immutable images in a private registry. It includes instructions for pulling images, verifying image signatures, and pushing them to your preferred private registry.

## Prerequisites

Before you begin, be sure to meet the following prerequisites:

* Required Private registry
* Required Write access to image repositories for Dynatrace images
* Optional [Skopeoï»¿](https://github.com/containers/skopeo/blob/main/install.md) for easy copying of our multi-arch images
* Optional [Cosignï»¿](https://docs.sigstore.dev/system_config/installation/) for image signature verification

## Dynatrace container images

Dynatrace immutable and signed container images are available on various container registries. For more details on repositories and tag information, explore our [supported public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry").

We strongly recommend choosing one of our supported public registries from which to copy container images.

Please do not use the Dynatrace built-in registry for copying images to private registries.

An exception applies for the OneAgent image for Classic Full-Stack, where the respective image **must** be copied from the built-in registry to work properly.

### Observability options

Depending on the [observability options](/docs/ingest-from/setup-on-k8s/deployment#observability-options-for-kubernetes "Deploy Dynatrace Operator on Kubernetes") you choose, you might want to only copy required images. The following table outlines the relations between Dynatrace images and observability options.

1

Must be replicated from Dynatrace built-in registry. See [Support for Classic Full-Stack monitoring](#classic-full-stack) for further details.

### Image tags

To show how versioning directly relates to image tagging, the following table lists real examples of image tags for Dynatrace container images.

Note how Dynatrace ActiveGate, Code Modules, and OneAgent share a similar versioning approach, while Dynatrace Operator, which follows a distinct release cadence, uses a different versioning approach.

In all cases, version-based image tagging is employed with container images. Mutable image tags like 'latest' are not used.

### Image signature verification

All of our immutable and signed container images adhere to best practices, enhancing security and shielding against supply chain attacks. To learn how to verify signatures and guarantee software integrity, see [Verify Dynatrace image signatures](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures").

## Copy Dynatrace container images

The following guide describes how to copy Dynatrace container images from public Amazon ECR to our private registry with the following example attributes.

The instructions below to copy container images to your private registry:

Skopeo (recommended)

Docker CLI

Recommended

Due to its support for easy copying of multi-arch images and signatures[1](#fn-2-1-def), we strongly recommend that you use the Skopeo CLI for copying container images. To learn more about the Skopeo CLI, see [Skopeo GitHub repositoryï»¿](https://github.com/containers/skopeo).

In the following instructions, be sure to always replace `<tag>` with an available version (see the [Supported public registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry") section).

#### Copy Dynatrace Operator image

The following command shows how to copy the Dynatrace Operator image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-operator:<tag> \



docker://registry.my-company.com/dynatrace-operator:<tag>
```

#### Copy Dynatrace ActiveGate image

The following command shows how to copy the Dynatrace ActiveGate image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-activegate:<tag> \



docker://registry.my-company.com/dynatrace-activegate:<tag>
```

#### Copy Dynatrace Code Modules image

The following command shows how to copy the Dynatrace Code Modules image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-codemodules:<tag> \



docker://registry.my-company.com/dynatrace-codemodules:<tag>
```

#### Copy Dynatrace OneAgent image

The following command shows how to copy the Dynatrace OneAgent image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-oneagent:<tag> \



docker://registry.my-company.com/dynatrace-oneagent:<tag>
```

#### Copy Dynatrace K8s Node Config Collector image

The following command shows how to copy the Dynatrace K8s Node Config Collector image to our private registry:

```
skopeo copy --all docker://public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag> \



docker://registry.my-company.com/dynatrace-k8s-node-config-collector:<tag>
```

1

Requires `use-sigstore-attachments` to be set to `true` in *Skopeo*'s [container registriesï»¿](https://github.com/containers/image/blob/main/docs/containers-registries.d.5.md#individual-configuration-sections) configuration.

We strongly recommend that you use the Skopeo CLI instead of Docker CLI for copying Dynatrace container images from public to private registries, as the Docker CLI does not provide an easy way to copy multi-arch images and signatures.

If you still want to use Docker CLI, please refer to the [official Docker CLI documentationï»¿](https://docs.docker.com/engine/reference/commandline/cli/).

### Support for Classic Full-Stack monitoring

[Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.") requires a pre-configured Dynatrace OneAgent image, which is available **only** via the Dynatrace built-in registry.

Consequently, the OneAgent image must be replicated via the Dynatrace built-in registry as described below.

Prerequisites

#### Before you begin

Make sure you meet the following prerequisites:

* Required Non-optional prerequisites from the top
* Required Credentials for Dynatrace built-in registry

#### Obtain Dynatrace built-in registry credentials

As the Dynatrace built-in registry requires authentication, you need to know your monitoring environment ID and provide a PaaS token for the login:

* To determine `<your-environment-id>`, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
* To determine `<your-paas-token>`, see [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

Example login using *Skopeo* CLI:

```
skopeo login -u <your-environment-id> -p <your-paas-token> <your-environment-url>
```

Please note that this section only addresses configurations of Classic Full-Stack monitoring.

#### Copy Dynatrace OneAgent image for Classic Full-Stack monitoring

The Dynatrace built-in registry only supports x86-64 architectures running Linux. As a consequence, we recommend that you explicitly set/override the architecture and operating system.

How to determine OneAgent image tag

The Dynatrace built-in registry provides the following OneAgent image tag formats:

* `latest`
* `latest-raw`
* `<major>.<minor>.<revision>`
* `<major>.<minor>.<revision>-raw`

For image replication, we recommend that you copy raw images (images with the tag suffix `-raw`).

To understand which OneAgent versions are available for replication, you can use the following Deployment APIs:

* [List available versions of OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.") to get an overview of available OneAgent versions.
* [View the latest version of OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-version-latest "View the latest version of OneAgent via Dynatrace API."), if you want to understand the OneAgent version behind `latest` or automate OneAgent image replication.

The following examples show how OneAgent versions translate to image tags available in the Dynatrace built-in registry:

Before executing the following command, be sure to replace `<tag-with-raw-suffix>` and `<environment-id>`:

```
skopeo copy --override-arch amd64 --override-os linux



docker://<your_environment_domain_name>/linux/oneagent:<tag-with-raw-suffix> \



docker://registry.my-company.com/dynatrace-oneagent-classic:<tag-with-raw-suffix>
```

For more information on configuring a DynaKube custom resource, see our examples of how to [use private registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

## Related topics

* [Use a private registry](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Verify Dynatrace image signatures](/docs/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures")