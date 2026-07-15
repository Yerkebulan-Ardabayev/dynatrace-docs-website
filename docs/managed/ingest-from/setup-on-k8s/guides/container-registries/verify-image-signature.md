---
title: Verify Dynatrace image signatures
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature
---

# Verify Dynatrace image signatures

# Verify Dynatrace image signatures

* 4-min read
* Updated on Apr 16, 2026

In the contemporary landscape, supply chain attacks have become a prevalent threat vector. Our approach to countering this risk involves delivering immutable and signed images, which serve as the cornerstone for bolstering security measures.

This page outlines the process of verifying Dynatrace image signatures, thereby establishing authenticity and safeguarding software integrity.

## Prerequisites

Before you begin, be sure to meet the following prerequisites:

* Required [Cosign﻿](https://docs.sigstore.dev/cosign/system_config/installation/) for image signature verification
* Optional [GitHub CLI﻿](https://cli.github.com/) for SLSA provenance verification via GitHub attestation API
* Required Read access to Dynatrace image repositories when using a private registry

## Verify image signatures using Cosign

The following sections describe how Dynatrace image signatures can be verified using Cosign. For simplicity, all examples reference Dynatrace component repositories on public Amazon ECR, but are valid and applicable to any registry holding Dynatrace images.

If you are looking for alternatives to Amazon ECR, see [Supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

Image signing is only performed on Dynatrace images of supported public registries. Images on the Dynatrace built-in registry are not signed.

Dynatrace signs images with Cosign, but only signing data for Dynatrace Operator is uploaded to the public Sigstore transparency log. This allows standard verification for the Operator. For other images, the `--insecure-ignore-tlog` flag is required during verification.

### Dynatrace Operator

Dynatrace Operator is an open-source project hosted and built on GitHub. As a consequence, signing and verification slightly differs from other Dynatrace components.

Keyless verification

Public key verification

The following command shows a keyless way to verify the Dynatrace Operator image signature:

```
cosign verify --certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

The following command shows how to verify the Dynatrace Operator image signature using the public key of the respective GitHub release:

```
cosign verify --key https://github.com/Dynatrace/dynatrace-operator/releases/download/<tag>/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

### Dynatrace ActiveGate

The following command shows how to verify the Dynatrace ActiveGate image signature using the public key from `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-activegate:<tag>
```

### Dynatrace Code Modules

The following command shows how to verify the Dynatrace Code Modules image signature using the public key from `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-codemodules:<tag>
```

### Dynatrace OneAgent

The following command shows how to verify the Dynatrace OneAgent image signature using the public key from `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>
```

### Dynatrace Kubernetes Node Configuration Collector

The following command shows how to verify the Dynatrace Kubernetes Node Configuration Collector image signature using the public key from `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub \



public.ecr.aws/dynatrace/dynatrace-k8s-node-config-collector:<tag>
```

### Dynatrace EdgeConnect

The following command shows how to verify the Dynatrace EdgeConnect image signature using the public key from `ca.dynatrace.com`:

```
cosign verify --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub \



public.ecr.aws/dynatrace/edgeconnect:<tag>
```

## Verify Software Bill of Materials (SBOM) Attestation

Attestations enable users to confirm that a Software Bill of Materials (SBOM) comes from a trusted source in the software supply chain. By trusting the container image producer's declaration of the included software, users can safely integrate the SBOM into their workflows.

### Dynatrace Operator

Use the following command to verify the Software Bill of Materials (SBOM) attestation[1](#fn-1-1-def) of a Dynatrace Operator[2](#fn-1-2-def) image:

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

1

Supported from Dynatrace Operator version 0.12.0.

2

Dynatrace Operator image is available on Amazon ECR from version 1.0.0. For more information, see [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

Retrieve SBOM file from verification output

The SBOM in CycloneDX format can be extracted from the in-toto attestation by extending the command from above with `jq`[3](#fn-2-3-def) filters:

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-operator:<tag> | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

3

The [jq CLI﻿](https://jqlang.github.io/jq/) is a useful tool for working with JSON.

Executing the command creates the `sbom.json` file in the local file system, containing the SBOM of the Dynatrace Operator image.

### Dynatrace ActiveGate

ActiveGate version 1.303+

Use the following command to verify the Software Bill of Materials (SBOM) attestation of a Dynatrace ActiveGate image.
Make sure to specify the desired CPU architecture. Options are `amd64`, `arm64`, and `s390x`.

```
digest=$(docker manifest inspect public.ecr.aws/dynatrace/dynatrace-activegate:<tag> | \



jq -r '.manifests[] | select(.platform.architecture=="amd64") | .digest')



cosign verify-attestation --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub --type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-activegate@$digest
```

Retrieve SBOM file from verification output

The SBOM in CycloneDX format can be extracted from the in-toto attestation by extending the command from above with `jq`[1](#fn-3-1-def) filters:

```
cosign verify-attestation --insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign.pub --type cyclonedx \



public.ecr.aws/dynatrace/dynatrace-activegate@$digest | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

1

The [jq CLI﻿](https://jqlang.github.io/jq/) is a useful tool for working with JSON.

Executing the command creates the `sbom.json` file in the local file system, containing the SBOM of the Dynatrace ActiveGate image.

### Dynatrace EdgeConnect

EdgeConnect version 1.473+

Use the following command to verify the Software Bill of Materials (SBOM) attestation of a Dynatrace EdgeConnect image.

```
cosign verify-attestation \



--insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub --type cyclonedx \



public.ecr.aws/dynatrace/edgeconnect:<tag>
```

Retrieve SBOM file from verification output

The SBOM in CycloneDX format can be extracted from the in-toto attestation by extending the command from above with `jq`[1](#fn-4-1-def) filters:

```
cosign verify-attestation \



--insecure-ignore-tlog --key https://ca.dynatrace.com/v1/cosign-edgeconnect.pub --type cyclonedx \



public.ecr.aws/dynatrace/edgeconnect:<tag> | \



jq '.payload | @base64d | fromjson | .predicate' > sbom.json
```

1

The [jq CLI﻿](https://jqlang.github.io/jq/) is a useful tool for working with JSON.

Executing the command creates the `sbom.json` file in the local file system, containing the SBOM of the Dynatrace EdgeConnect image.

## Verify SLSA Build Provenance Attestation

[SLSA﻿](https://slsa.dev) build provenance attestations provide a verifiable record of where and how a container image was built. Verifying these attestations confirms that the image was produced by the expected source repository and build workflow, protecting against tampering in the build and distribution process.

### Dynatrace Operator

Cosign

GitHub CLI

Use the following command to verify the SLSA build provenance attestation[1](#fn-5-1-def) of a Dynatrace Operator[2](#fn-5-2-def) image:

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type slsaprovenance1 \



public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

1

Supported from Dynatrace Operator version 1.9.0.

2

Dynatrace Operator image is available on Amazon ECR from version 1.0.0. For more information, see [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

On success, Cosign confirms that the signing certificate, transparency log entry, and OIDC issuer are valid, and that the attestation was produced by a trusted Dynatrace build workflow.

Retrieve provenance details from verification output

The [SLSA Provenance v1﻿](https://slsa.dev/spec/v1.0/provenance) payload can be extracted from the in-toto attestation by extending the command from above with `jq`[3](#fn-6-3-def) filters:

```
cosign verify-attestation \



--certificate-identity-regexp 'https://github\.com/Dynatrace/dynatrace-operator/\.github/workflows/.+' \



--certificate-oidc-issuer https://token.actions.githubusercontent.com \



--type slsaprovenance1 \



public.ecr.aws/dynatrace/dynatrace-operator:<tag> | \



jq '.payload | @base64d | fromjson'
```

3

The [jq CLI﻿](https://jqlang.github.io/jq/) is a useful tool for working with JSON.

The output contains the full SLSA Provenance v1 predicate, including the source repository, build workflow, git commit, and the GitHub Actions invocation that produced the image.

Alternatively, you can use the [GitHub CLI﻿](https://cli.github.com/) to verify the attestation directly against the GitHub attestation API:

```
gh attestation verify \



--owner Dynatrace \



oci://public.ecr.aws/dynatrace/dynatrace-operator:<tag>
```

On success, the command prints `Verification succeeded!` and lists the matched attestations, including the build repository, workflow, and signer identity.

## Related topics

* [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")
* [Use a private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")
* [Store Dynatrace images in private registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")