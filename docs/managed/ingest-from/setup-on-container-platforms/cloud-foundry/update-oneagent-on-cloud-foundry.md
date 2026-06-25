---
title: Update OneAgent on Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/update-oneagent-on-cloud-foundry
scraped: 2026-05-12T11:09:22.027268
---

# Update OneAgent on Cloud Foundry

# Update OneAgent on Cloud Foundry

* 1-min read
* Published Apr 17, 2020

Find out below how to update OneAgent according to your particular deployment strategy. For a clear view of all the deployment alternatives, see [Cloud Foundry deployment strategies](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.").

## Update OneAgent BOSH lightweight release

For Cloud Foundry VMs, the [auto-update mechanism](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.") is built into Dynatrace OneAgent. This means you don't have to worry about manually updating the OneAgents running on your Cloud Foundry VMs.

Following any auto-update you must manually restart the platform processes and the Cloud Foundry processes/applications so that they are monitored with the latest version of Dynatrace OneAgent.

```
cf restart <app_name>
```

## Update OneAgent BOSH immutable release

To update the immutable BOSH release, follow the [Deploy instructions](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#immutable "Install OneAgent on Cloud Foundry with BOSH.") for downloading the latest release, uploading it to your BOSH blobstore, and changing the versions in the runtime configuration.

## Update OneAgent for application-only monitoring

When a new version of Dynatrace OneAgent becomes available, you must restage your Cloud Foundry application.

```
cf restage <app_name>
```

The Cloud Foundry buildpack will automatically fetch the latest version of Dynatrace OneAgent. After the restage, your Cloud Foundry applications will be monitored with the latest version of Dynatrace OneAgent.

If you've specified a default Dynatrace OneAgent installation version for new hosts and applications in your [Dynatrace OneAgent updates settings](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), the Cloud Foundry buildpack will automatically fetch the defined default version of Dynatrace OneAgent.

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")