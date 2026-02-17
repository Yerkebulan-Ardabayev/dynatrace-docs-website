---
title: Set up Dynatrace on Cloud Foundry
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/cloud-foundry
scraped: 2026-02-17T21:20:56.414348
---

# Set up Dynatrace on Cloud Foundry

# Set up Dynatrace on Cloud Foundry

* Latest Dynatrace
* 1-min read
* Published Aug 03, 2018

Dynatrace supports full-stack monitoring for Cloud Foundry through the Dynatrace OneAgent BOSH Release, which allows you to deploy OneAgent to your Cloud Foundry cluster VMs, including Diego cells, Cloud Controller, router, and others.

## Integrations

There are two approaches in deploying the OneAgent BOSH release, [immutable](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#immutable "Install OneAgent on Cloud Foundry with BOSH.") and [lightweight](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#lightweight "Install OneAgent on Cloud Foundry with BOSH."). The differences between these approaches are described below.

Immutable release

Lightweight release

The immutable OneAgent BOSH release is downloaded using the Dynatrace Environment API. This release contains complete packages, binaries, and installation files in the same archive. This fully contained approach is immutable because it gives operators full control over what is deployed and when.

![Immutable release](https://dt-cdn.net/images/bosh-cludfoundry-immutable-500-fbf72def36.png)

The lightweight OneAgent BOSH release downloads and installs a pre-configured OneAgent at deployment time, which guarantees the latest OneAgent binaries and allows for fully automated OneAgent-controlled version updates.

![Lightweight release](https://dt-cdn.net/images/bosh-cloudfoundry-lightweight-500-4ff8ba068b.png)

If you don't have access to BOSH, Dynatrace provides two different approaches for application-only monitoring:

* [OneAgent on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")
* [OneAgent on SAP Business Technology Platform](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Install OneAgent on SAP Business Technology Platform.")

## Configuration

[Connect your Cloud Foundry clusters with Dynatrace](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.")

[Install the Dynatrace Service Broker for Cloud Foundry dashboard tile](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile "Install and configure the Dynatrace Service Broker for VMware Tanzu Platform dashboard tile.")

## Maintenance

[Update OneAgent on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/update-oneagent-on-cloud-foundry "Update OneAgent on Cloud Foundry based on different deployment strategies.")

[Uninstall OneAgent from Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/uninstall-oneagent-from-cloud-foundry "Uninstall OneAgent from Cloud Foundry for BOSH add-ons.").

## Troubleshooting

[Troubleshoot OneAgent deployment issues on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/troubleshoot-cf "Troubleshoot deployment problems on Cloud Foundry.")

## Related topics

* [Cloud Foundry monitoringï»¿](https://www.dynatrace.com/technologies/cloud-foundry-monitoring/)
* [Cloud Foundry monitoring](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")