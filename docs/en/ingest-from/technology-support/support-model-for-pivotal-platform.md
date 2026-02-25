---
title: Dynatrace support model for VMware Tanzu Application Service
source: https://www.dynatrace.com/docs/ingest-from/technology-support/support-model-for-pivotal-platform
scraped: 2026-02-25T21:21:08.262731
---

# Dynatrace support model for VMware Tanzu Application Service

# Dynatrace support model for VMware Tanzu Application Service

* Latest Dynatrace
* 5-min read
* Updated on May 10, 2024

VMware supports N, N-1, and N-2 releases of Tanzu Application Service. You can find further details in the VMware [support policyï»¿](https://tanzu.vmware.com/support/lifecycle_policy).

Dynatrace follows the same [support modelï»¿](https://d1fto35gcfffzn.cloudfront.net/support/PivotalLifecycleMatrix.pdf) as VMware, ensuring a consistent upgrade cadence. However, OneAgent and [Dynatrace Service Broker](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile "Install and configure the Dynatrace Service Broker for VMware Tanzu Platform dashboard tile.") support for Tanzu may trail behind VMware releases to allow for adequate testing.

For details, see [end of support announcements](/docs/whats-new/technology/end-of-support-news "End of support announcements for technologies supported by Dynatrace.") for OneAgent.

| TAS version[1](#fn-1-1-def) | TAS release | End of support[2](#fn-1-2-def) |
| --- | --- | --- |
| 2.11.x (+ Windows) | 2021-03-30 | 2024-04-30 |
| 2.13.x (+ Windows) | 2022-03-29 | 2024-03-31 |
| 3.0.x (+ Windows) | 2022-10-06 | 2023-10-31 |
| 4.0.x (+ Windows) | 2023-04-18 | 2025-04-30 |
| 5.0.x (+ Windows) | 2023-10-17 | 2025-10-31 |
| 6.0.x (+ Windows) | 2024-04-10 | 2026-04-30 |

## Version matrix

The support for a specific TAS version depends on the Go version used by the Cloud Foundry Gorouter supported by the OneAgent. The following table gives you detailed information about which OneAgent version is compatible with which TAS version.

|  |  |
| --- | --- |
| Future **Future** | Technology support will be added in a future OneAgent version |

### Version 6.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 6.0.11+LTS-T | 2025-01-09 | 1.22.7 | 1.287.0 |
| 6.0.10+LTS-T | 2024-11-19 | 1.22.7 | 1.287.0 |
| 6.0.9+LTS-T | 2024-10-07 | 1.22.7 | 1.287.0 |
| 6.0.8+LTS-T | 2024-09-27 | 1.22.7 | 1.287.0 |
| 6.0.7+LTS-T | 2024-08-22 | 1.22.6 | 1.287.0 |
| 6.0.6+LTS-T | 2024-07-29 | 1.22.4 | 1.287.0 |
| 6.0.5+LTS-T | 2024-07-08 | 1.22.4 | 1.287.0 |
| 6.0.4+LTS-T | 2024-05-29 | 1.22.3 | 1.287.0 |
| 6.0.3+LTS-T | 2024-05-03 | 1.22.2 | 1.287.0 |
| 6.0.2+LTS-T | 2024-05-02 | 1.22.2 | 1.287.0 |
| 6.0.1+LTS-T | 2024-04-10 | 1.21.9 | 1.281.0 |
| 6.0.0+LTS-T | 2024-04-18 | 1.21.9 | 1.281.0 |

### Version 5.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 5.0.0 | 2023-10-17 | 1.21.3 | 1.279.0 |

### Version 4.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 4.0.4 | 2023-06-26 | 1.20.5 | 1.263.0 |
| 4.0.3 | 2023-06-02 | 1.20.4 | 1.263.0 |
| 4.0.2 | 2023-05-25 | 1.20.4 | 1.263.0 |
| 4.0.1+LTS-T | 2023-05-17 | 1.20.4 | 1.263.0 |
| 4.0.0+LTS-T | 2023-04-18 | 1.20.2 | 1.263.0 |

### Version 3.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 3.0.3 | 2022-12-15 | 1.19.4 | 1.257.0 |
| 3.0.2 | 2022-12-02 | 1.19.2 | 1.253.0 |
| 3.0.1 | 2022-11-15 | 1.19.2 | 1.253.0 |
| 3.0.0 | 2022-10-06 | 1.18.6 | 1.253.0 |

### Version 2.13.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 2.13.8 | 2022-08-10 | 1.17.12 | 1.249.0 |
| 2.13.7 | 2022-07-19 | 1.17.11 | 1.245.0 |
| 2.13.6 | 2022-06-24 | 1.17.10 | 1.243.0 |
| 2.13.5 | 2022-06-09 | 1.17.8 | 1.239.0 |
| 2.13.4 | 2022-04-21 | 1.17.8 | 1.239.0 |
| 2.13.3 | 2022-04-20 | 1.17.8 | 1.239.0 |
| 2.13.2 | 2022-04-06 | 1.17.8 | 1.239.0 |
| 2.13.1 | 2022-03-31 | 1.17.8 | 1.239.0 |
| 2.13.0 | 2022-03-29 | 1.17.8 | 1.239.0 |

### Version 2.11.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 2.11.14 | 2022-02-07 | 1.16.12 | 1.233.0 |
| 2.11.13 | 2021-12-22 | 1.16.10 | 1.233.0 |
| 2.11.12 | 2021-12-16 | 1.16.10 | 1.233.0 |
| 2.11.11 | 2021-12-15 | 1.16.10 | 1.233.0 |
| 2.11.10 | 2021-12-13 | 1.16.10 | 1.233.0 |
| 2.11.9 | 2021-11-23 | 1.16.9 | 1.231.0 |
| 2.11.8 | 2021-10-19 | 1.16.7 | 1.227.0 |
| 2.11.7 | 2021-09-30 | 1.16.7 | 1.227.0 |
| 2.11.6 | 2021-09-16 | 1.16.7 | 1.227.0 |
| 2.11.5 | 2021-09-09 | 1.16.7 | 1.227.0 |
| 2.11.4 | 2021-07-20 | 1.16.5 | 1.221.0 |
| 2.11.3 | 2021-07-15 | 1.16.5 | 1.221.0 |
| 2.11.2 | 2021-06-22 | 1.15.8 | 1.213.0 |
| 2.11.1 | 2021-05-27 | 1.15.8 | 1.213.0 |
| 2.11.0 | 2021-03-30 | 1.15.6 | 1.213.0 |

There are two flavors of the [Dynatrace OneAgent BOSH Releaseï»¿](https://github.com/Dynatrace/bosh-oneagent-release). The full BOSH OneAgent release doesn't contain the OneAgent installer. Instead, the installer is downloaded from your Dynatrace environment during the release deployment. We recommend that you use the latest release of the Dynatrace OneAgent BOSH add-on because it contains the latest improvements. However, we've also listed the minimum required BOSH Release versions per VMware Tanzu application service version above.

1

All of the above-listed versions have been verified with multiple OneAgent versions.

2

Prior to May 2020 (pre 1.191) Dynatrace offered a three-month upgrade grace period for Cloud Foundry distributions due to the offset between delivery schedules. As of May 2020, Dynatrace has accelerated its testing cycle. Thus our support model no longer requires the three-month grace period. For all OneAgent releases prior to May 2020 (earlier than OneAgent version 1.191), Dynatrace will extend support by three months to honor pre-existing OneAgent installations based on the previous support model.

3

There are two versioning schemes. The immutable OneAgent BOSH release is versioned the same as OneAgent. The immutable OneAgent BOSH release is the recommended method of deploying OneAgent. Previous versions used a lightweight approach, available on GitHub, and use GitHub's version scheme.