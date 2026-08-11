---
title: Container registries
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/container-registries
---

# Container registries

# Container registries

* 2-min read
* Updated on Aug 03, 2026

To prioritize seamless integration with your tooling and adaptability to your needs, we offer our container images in various ways to maximize flexibility:

* Dynatrace built-in registry default
* Public registries
* Bring your own private registry Recommended

## Dynatrace built-in registry

default

As the default behavior, Dynatrace Operator retrieves images from the built-in Dynatrace registry, prioritizing convenience and minimizing configuration complexities for cloud-native monitoring setup.

Nevertheless, the concurrent retrieval of multiple images from the Dynatrace built-in registry raises the potential for rate limiting. We therefore recommend using our endorsed public registries or, ideally, establishing your private registry. Leveraging public and private registries enhances operational efficiency and performance, particularly under high-demand conditions.

The built-in cluster container registry will be shut down on January 1, 2028, and will no longer function. Migrate to Amazon ECR or Docker Hub.

* For the full schedule, see [End-of-life announcements](/managed/whats-new/technology/end-of-life-announcements#built-in-cluster-container-registry "Information about technologies, features, or integrations scheduled for end of life (EOL) in Dynatrace, including upcoming and recently retired items.").
* For the image paths to use after you migrate, see [Use a public registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.").

## Public registries

To accommodate diverse infrastructure requirements and organizational preferences, Dynatrace images are available on [selected public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."). These images adhere to best practices, ensuring immutability and signing for enhanced security and resilience against potential supply chain risks.

If you seek greater control over your image hosting environment, Dynatrace offers the option to replicate images and signatures to private registries.

## Bring your own private registry

Recommended

For optimal performance in high-demand and dynamic environments, we recommend using a [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry"). Furthermore, to meet security standards and ensure software integrity while mitigating supply chain risks, image scanning and [signature verification](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures") against Dynatrace images are recommended.

By replicating Dynatrace images to your private registry, you can seamlessly merge excellent delivery performance with the assurance of secure, signed, and immutable images.

## Learn more

[### Use Dynatrace public registry

Configure Dynatrace Operator and DynaKube to use images from our supported public registries.](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment.")[### Use your own private registry

Configure Dynatrace Operator and DynaKube to use images from your own private registry.](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry")[### Store Dynatrace images in private registries

Learn how to replicate Dynatrace images into your private registries.](/managed/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")[### Verify Dynatrace image signatures

Verify Dynatrace image signatures to ensure integrity and secure software supply chain.](/managed/ingest-from/setup-on-k8s/guides/container-registries/verify-image-signature "Verify Dynatrace image signatures")