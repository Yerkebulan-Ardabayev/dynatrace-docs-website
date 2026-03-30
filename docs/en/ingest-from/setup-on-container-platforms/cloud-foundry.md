---
title: Set up Dynatrace on Cloud Foundry
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/cloud-foundry
scraped: 2026-03-06T21:15:45.746356
---

# Set up Dynatrace on Cloud Foundry


* Latest Dynatrace
* 1-min read
* Published Aug 03, 2018

Dynatrace supports full-stack monitoring for Cloud Foundry through the Dynatrace OneAgent BOSH Release, which allows you to deploy OneAgent to your Cloud Foundry cluster VMs, including Diego cells, Cloud Controller, router, and others.

## Integrations

There are two approaches in deploying the OneAgent BOSH release, immutable and lightweight. The differences between these approaches are described below.

Immutable release

Lightweight release

The immutable OneAgent BOSH release is downloaded using the Dynatrace Environment API. This release contains complete packages, binaries, and installation files in the same archive. This fully contained approach is immutable because it gives operators full control over what is deployed and when.

![Immutable release](https://dt-cdn.net/images/bosh-cludfoundry-immutable-500-fbf72def36.png)

The lightweight OneAgent BOSH release downloads and installs a pre-configured OneAgent at deployment time, which guarantees the latest OneAgent binaries and allows for fully automated OneAgent-controlled version updates.

![Lightweight release](https://dt-cdn.net/images/bosh-cloudfoundry-lightweight-500-4ff8ba068b.png)

If you don't have access to BOSH, Dynatrace provides two different approaches for application-only monitoring:

* OneAgent on Cloud Foundry
* OneAgent on SAP Business Technology Platform

## Configuration

Connect your Cloud Foundry clusters with Dynatrace

Install the Dynatrace Service Broker for Cloud Foundry dashboard tile

## Maintenance

Update OneAgent on Cloud Foundry

Uninstall OneAgent from Cloud Foundry.

## Troubleshooting

Troubleshoot OneAgent deployment issues on Cloud Foundry

## Related topics

* [Cloud Foundry monitoringï»¿](https://www.dynatrace.com/technologies/cloud-foundry-monitoring/)
* Cloud Foundry monitoring