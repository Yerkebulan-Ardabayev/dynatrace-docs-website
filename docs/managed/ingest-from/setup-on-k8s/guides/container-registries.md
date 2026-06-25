---
title: Container registries
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries
scraped: 2026-05-12T11:53:48.761743
---

# Container registries

# Container registries

* 2-min read
* Published Jul 28, 2023

To prioritize seamless integration with your tooling and adaptability to your needs, we offer our container images in various ways to maximize flexibility:

* Dynatrace built-in registry default
* Public registries
* Bring your own private registry Recommended

## Dynatrace built-in registry

default

As the default behavior, Dynatrace Operator retrieves images from the built-in Dynatrace registry, prioritizing convenience and minimizing configuration complexities for cloud-native monitoring setup.

Nevertheless, the concurrent retrieval of multiple images from the Dynatrace built-in registry raises the potential for rate limiting. We therefore recommend using our endorsed public registries or, ideally, establishing your private registry. Leveraging public and private registries enhances operational efficiency and performance, particularly under high-demand conditions.

## Public registries

To accommodate diverse infrastructure requirements and organizational preferences, Dynatrace images are available on [selected public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry"). These images adhere to best practices, ensuring immutability and signing for enhanced security and resilience against potential supply chain risks.

If you seek greater control over your image hosting environment, Dynatrace offers the option to replicate images and signatures to private registries.

## Bring your own private registry

Recommended

For optimal performance in high-demand and dynamic environments, we recommend using a [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry"). Furthermore, to meet security standards and ensure software integrity while mitigating supply chain risks, image scanning and [signature verification](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures") against Dynatrace images are recommended.

By replicating Dynatrace images to your private registry, you can seamlessly merge excellent delivery performance with the assurance of secure, signed, and immutable images.

## Learn more

[### Use Dynatrace public registry

Configure Dynatrace Operator and DynaKube to use images from our supported public registries.](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Use a public registry")[### Use your own private registry

Configure Dynatrace Operator and DynaKube to use images from your own private registry.](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")[### Store Dynatrace images in private registries

Learn how to replicate Dynatrace images into your private registries.](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")[### Verify Dynatrace image signatures

Verify Dynatrace image signatures to ensure integrity and secure software supply chain.](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures")