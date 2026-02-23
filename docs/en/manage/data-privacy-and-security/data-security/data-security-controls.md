---
title: Data security controls
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-security/data-security-controls
scraped: 2026-02-23T21:27:28.383730
---

# Data security controls

# Data security controls

* Latest Dynatrace
* 10-min read
* Updated on Sep 29, 2025

## Overview of data security controls

![data-security-overview-saas-v2](https://dt-cdn.net/images/data-security-overview-saas-v2-3982-b71494b7fa.png)

## Data storage

Data is stored in Amazon Web Services (AWS), Microsoft Azure, or Google Cloud data centers. The available regions are listed below.

#### AWS Regions

* US East (N. Virginia)
* US West (Oregon)
* Europe (Ireland)
* Asia Pacific (Sydney)
* Europe (London)[1](#fn-1-1-def)
* Europe (Frankfurt)[1](#fn-1-1-def)
* Canada (Central)[1](#fn-1-1-def)
* South America (SÃ£o Paulo)[1](#fn-1-1-def)
* Asia Pacific (Singapore)[1](#fn-1-1-def)
* Asia Pacific (Mumbai)[1](#fn-1-1-def)
* Asia Pacific (Tokyo)[1](#fn-1-1-def)
* Middle East (Tel Aviv)[1](#fn-1-1-def)

1

Available on request. Talk to your Dynatrace sales contact.

#### Azure regions[1](#fn-2-1-def)

* East US (Virginia)
* West US 3 (Arizona)
* West Europe (Netherlands)
* Canada Central (Toronto)
* UAE (Dubai)
* Switzerland North (Zurich)
* Australia East (Sydney)

1

Available on request. Talk to your Dynatrace sales contact.

#### Google Cloud regions[1](#fn-3-1-def)

* us-east4 (N. Virginia)
* europe-west3 (Frankfurt)

1

Available on request. Talk to your Dynatrace sales contact.

Also see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").

## Dynatrace components

[Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") collects all monitoring data within your monitored environment. Optionally, all data collected by OneAgent can be routed through a [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), which works as a proxy between Dynatrace OneAgent and the Dynatrace Cluster. In the absence of an ActiveGate, data collected by OneAgent is sent directly to the Dynatrace Cluster.

![saas-dynatrace-components](https://dt-cdn.net/images/saas-dynatrace-components-2690-a37591adb1.png)

## Data segregation between customer environments

Dynatrace SaaS uses a multi-tenant, high-availability architecture. Dynatrace allocates a tenant, a so-called Dynatrace environment, to each customer. Customers can also manage multiple environments within the Dynatrace account management system. Each environment gets its own individual domain.

With the latest Dynatrace, all Dynatrace platform data at rest, including data from Grail, AppEngine, and AutomationEngine, is stored in a separate, dedicated storage space. One single Dynatrace SaaS environment hosted on AWS uses a dedicated AWS S3 bucket as storage space. Environments hosted on Azure use dedicated Azure storage accounts. Other data, such as [Dynatrace Credential vault data](/docs/manage/credential-vault "Store and manage credentials in the credential vault.") or [Dynatrace account data](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health."), is stored in databases using logical data separation.

The application layer, in which the data is processed before it is stored at rest, is hosted on a highly scalable shared cloud infrastructure.

Separate storage space is currently available for Dynatrace SaaS on AWS and Azure. Support for Dynatrace SaaS on Google Cloud is planned.

![Data separation on the Dynatrace platform](https://dt-cdn.net/images/dynatrace-platform-data-separation-doc-2662-d52d653a45.png)

## Data encryption at rest

All Dynatrace SaaS monitoring data is encrypted at rest using AES-256. With the latest Dynatrace, all Dynatrace platform data, including data from Grail, AppEngine, and AutomationEngine, is stored in a separate, dedicated storage space. Each storage space is encrypted with a unique encryption key, which is rotated every 365 days. Dynatrace manages the encryption keys.

Separate data storage and unique encryption keys are currently available for Dynatrace SaaS on AWS and Azure. Support for Dynatrace SaaS on Google Cloud is planned.

![Dynatrace SaaS platform data encryption at rest](https://dt-cdn.net/images/dynatrace-platform-data-encryption-doc-2772-2da248ac18.png)

## Data encryption in transit

All data exchanged between OneAgent, ActiveGate, and Dynatrace Cluster is encrypted in transit. Data is serialized and deserialized using Google Protocol Buffers.

Dynatrace SaaS supports TLS 1.2 and TLS 1.3 (SSL Labs Grade A+).

![dynatrace-data-security-encryption-in-transit](https://dt-cdn.net/images/dynatrace-data-security-encryption-in-transit-2690-c09d771883.png)

## User authentication

You can manage your users by setting up [user groups and permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") and [SAML](/docs/manage/identity-access-management/user-and-group-management/access-saml "SAML").

![dynatrace-data-security-user-authentication](https://dt-cdn.net/images/dynatrace-data-security-user-authentication-2690-9a645c42f8.png)

## Integrity verification of Dynatrace components

Dynatrace components are signed using code signing certificates within the continuous delivery and integration (CI/CD) pipeline.

Code signing certificates are stored on hardware tokens with Extended Validation (EV) code signing certificates for Windows. Signature verification is performed automatically before an update or installation. When installing a component for the first time, signature verification must be conducted manually.

![dynatrace-data-security-integrity-verification](https://dt-cdn.net/images/dynatrace-data-security-integrity-verification-2905-53a43d8705.png)

## Business continuity and high-availability

Dynatrace SaaS uses a clustered architecture, multiple availability zones (data centers), and automatic fail-over mechanisms to ensure high availability ([99.5% availability SLAï»¿](https://www.dynatrace.com/company/trust-center/sla/saas/)).

![dynatrace-data-security-high-availability](https://dt-cdn.net/images/dynatrace-data-security-high-availability-2772-a154b24478.png)

## Data backups and disaster recovery

* **AWS:** Every 24 hours, Dynatrace SaaS on AWS performs data backups to a different AWS account in the same AWS region. The backup includes the data captured for at least the last 30 days. The maximum recovery point objective (RPO) for a full cluster is 24 hours. The recovery time objective (RTO) takes up to 24 hours, depending on the size of the cluster.
* **Azure:** Every 24 hours, Dynatrace SaaS on Azure performs data backups to a different Azure subscription in the same Azure region. The backup includes the data captured for at least the last 30 days. The maximum recovery point objective (RPO) for a full cluster is 24 hours. The recovery time objective (RTO) takes up to 24 hours, depending on the size of the cluster.
* **Google Cloud:** Every 24 hours, Dynatrace SaaS on Google Cloud performs data backups to a different Google Cloud project in the same Google Cloud region. The backup includes the data captured for at least the last 30 days. The maximum recovery point objective (RPO) for a full cluster is 24 hours. The recovery time objective (RTO) takes up to 24 hours, depending on the size of the cluster.

![dynatrace-data-security-backup](https://dt-cdn.net/images/dynatrace-data-security-backup-2690-e30ecd18aa.png)

## Infrastructure monitoring

A dedicated Dynatrace self-monitoring cluster monitors availability, performance, and security of all SaaS clusters. If a problem is detected, the Dynatrace ACE (Autonomous Cloud Enablement) team, which operates on a 24/7 basis, is notified immediately. Operational status and incidents are always available at [dynatrace.status.ioï»¿](https://dynatrace.status.io/).

![dynatrace-data-security-infrastructure-monitoring](https://dt-cdn.net/images/dynatrace-data-security-infrastructure-monitoring-2612-10a1faea42.png)

## Roll out of updates and hot fixes

Using a fully automated CI/CD pipeline, Dynatrace is able to roll out updates and hot fixes within a few hours. The Dynatrace architecture allows for zero-downtime upgrades of clusters.

New features are delivered every two weeks. Updates of Dynatrace ActiveGates and OneAgents can be performed automatically or manually.

![dynatrace-data-security-rollout-updates](https://dt-cdn.net/images/dynatrace-data-security-rollout-updates-2892-9efe1ac573.png)

## Audit logs

Dynatrace logs security-relevant events such as configuration changes and access to the environment. You can view these audit logs in [Dynatrace](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.") or download them for further use via the [GET audit log](/docs/dynatrace-api/environment-api/audit-logs/get-log "View full audit log via Dynatrace API.") API call.

![dynatrace-data-security-audit-logs](https://dt-cdn.net/images/dynatrace-data-security-audit-logs-2635-7349637e51.png)

## Data access for Dynatrace support

Access to Dynatrace SaaS environments is role-based. Role changes require justification and approval by the Dynatrace ACE (Autonomous Cloud Enablement) team. Access is restricted to the Dynatrace corporate network and requires multi-factor authentication when accessed remotely. Every access and all changes are [audit logged](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.") and fully accessible.

![dynatrace-data-security-data-access-support](https://dt-cdn.net/images/dynatrace-data-security-data-access-support-2791-ebcc4e889e.png)

## Dynatrace secret leak prevention

Dynatrace can detect and prevent the leakage of Dynatrace secrets in source code repositories on GitHub. These secrets may include platform or API tokens that were inadvertently pushed to a source code repository. If a secret leak is detected, we will reach out to you and aid with remediation measures.

For details on reporting a security issue, see [Report a security-related concern](/docs/manage/data-privacy-and-security/data-security/report-a-security-related-concern "Find out how to report vulnerabilities and whom to contact in case of security concerns.").

![dynatrace-data-security-secret-leak-prevention](https://dt-cdn.net/images/dynatrace-data-security-secret-leak-prevention-2575-f100e468bf.png)

## Compliance, certifications, and audits

Dynatrace undergoes annual, independent third-party audits and conducts penetration tests and red team assessments with independent security firms.

Having achieved several global and local certifications and accreditations demonstrates that we adhere to the most recognized international standards for security management.

Dynatrace also benefits from secure Amazon, Azure, and Google data centers that are certified for ISO 27001, PCI-DSS Level 1, and SOC 1/SSAE-16.

For the full list of certifications, see [Trust Centerï»¿](https://www.dynatrace.com/company/trust-center/).

## Runtime protection

Dynatrace SaaS is protected using [Dynatrace Application Securityï»¿](https://www.dynatrace.com/platform/application-security/).

Malicious activity is blocked using Dynatrace's [Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.") feature.

Third party and code level vulnerabilities are [detected in real time and automatically reported](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") to the Dynatrace Security team.

![Data security Dynatrace protection](https://dt-cdn.net/images/data-security-dynatrace-protection-1915-5d93f4245d.png)