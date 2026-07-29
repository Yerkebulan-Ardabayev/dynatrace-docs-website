---
title: Dynatrace support model for Broadcom Elastic Application Runtime
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/support-model-for-pivotal-platform
---

# Dynatrace support model for Broadcom Elastic Application Runtime

# Dynatrace support model for Broadcom Elastic Application Runtime

* 5-min read
* Updated on Jul 23, 2026

Broadcom supports N, N-1, and N-2 releases of Elastic Application Runtime (EAR). You can find further details in the [Broadcom support policy﻿](https://support.broadcom.com/group/ecx/productlifecycle).

Dynatrace follows the same [support model﻿](https://d1fto35gcfffzn.cloudfront.net/support/PivotalLifecycleMatrix.pdf) as Broadcom, ensuring a consistent upgrade cadence. However, OneAgent and [Dynatrace Service Broker](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile "Install and configure the Dynatrace Service Broker for VMware Tanzu Platform dashboard tile.") support for Elastic Application Runtime may trail behind Broadcom releases to allow for adequate testing.

For details, see [end of support announcements](/managed/whats-new/technology/end-of-support-news "End of support announcements for technologies supported by Dynatrace.") for OneAgent.

| EAR version[1](#fn-1-1-def) | EAR release | End of support[2](#fn-1-2-def) |
| --- | --- | --- |
| 10.4.x (+ Windows) | 2026-06-18 | 2028-04-30 |
| 10.3.x (+ Windows) | 2025-10-28 | 2026-10-31 |
| 10.2.x (+ Windows) | 2025-06-17 | 2027-06-30 |

## Version matrix

The support for a specific EAR version depends on the Go version used by the Cloud Foundry Gorouter supported by the OneAgent. The following table gives you detailed information about which OneAgent version is compatible with which EAR version.

|  |  |
| --- | --- |
| Future**Future** | Technology support will be added in a future OneAgent version |

### Version 10.4.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 10.4.3 | 2026-07-21 | 1.26.5 | 1.335.0 |

### Version 10.3.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 10.3.8 | 2026-06-16 | 1.25.11 | 1.327.0 |
| 10.3.7 | 2026-04-22 | 1.25.9 | 1.327.0 |
| 10.3.6 | 2026-03-17 | 1.25.8 | 1.327.0 |
| 10.3.5 | 2026-02-20 | 1.25.7 | 1.327.0 |
| 10.3.4 | 2026-01-20 | 1.25.5 | 1.327.0 |
| 10.3.2 | 2025-12-16 | 1.25.5 | 1.327.0 |
| 10.3.1 | 2025-11-18 | 1.25.3 | 1.327.0 |
| 10.3.0 | 2025-10-28 | 1.25.3 | 1.327.0 |

### Version 10.2.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 10.2.13 | 2026-07-21 | 1.26.5 | 1.335.0 |
| 10.2.12 | 2026-06-18 | 1.25.11 | 1.327.0 |
| 10.2.11 | 2026-05-19 | 1.25.9 | 1.327.0 |
| 10.2.10 | 2026-04-22 | 1.25.9 | 1.327.0 |
| 10.2.9 | 2026-03-17 | 1.25.8 | 1.327.0 |
| 10.2.8 | 2026-02-20 | 1.25.7 | 1.327.0 |
| 10.2.7 | 2026-01-20 | 1.25.5 | 1.327.0 |
| 10.2.6 | 2025-12-16 | 1.25.5 | 1.327.0 |
| 10.2.5 | 2025-11-18 | 1.25.3 | 1.327.0 |
| 10.2.4 | 2025-10-28 | 1.25.3 | 1.327.0 |
| 10.2.3 | 2025-09-16 | 1.24.7 | 1.321.0 |
| 10.2.2 | 2025-08-19 | 1.24.6 | 1.321.0 |
| 10.2.1 | 2025-07-22 | 1.24.4 | 1.321.0 |
| 10.2.0 | 2025-06-17 | 1.24.4 | 1.321.0 |

There are two flavors of the [Dynatrace OneAgent BOSH Release﻿](https://github.com/Dynatrace/bosh-oneagent-release). The full BOSH OneAgent release doesn't contain the OneAgent installer. Instead, the installer is downloaded from your Dynatrace environment during the release deployment. We recommend that you use the latest release of the Dynatrace OneAgent BOSH add-on because it contains the latest improvements. However, we've also listed the minimum required BOSH Release versions per VMware Tanzu application service version above.

1

All of the above-listed versions have been verified with multiple OneAgent versions.

2

Prior to May 2020 (pre 1.191) Dynatrace offered a three-month upgrade grace period for Cloud Foundry distributions due to the offset between delivery schedules. As of May 2020, Dynatrace has accelerated its testing cycle. Thus our support model no longer requires the three-month grace period. For all OneAgent releases prior to May 2020 (earlier than OneAgent version 1.191), Dynatrace will extend support by three months to honor pre-existing OneAgent installations based on the previous support model.

3

There are two versioning schemes. The immutable OneAgent BOSH release is versioned the same as OneAgent. The immutable OneAgent BOSH release is the recommended method of deploying OneAgent. Previous versions used a lightweight approach, available on GitHub, and use GitHub's version scheme.