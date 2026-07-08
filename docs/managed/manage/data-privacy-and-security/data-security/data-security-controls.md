---
title: Data security controls
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-security/data-security-controls
---

# Data security controls

# Data security controls

* 10-min read
* Updated on May 04, 2026

## Data storage

Your monitoring data remains in your own on-premise data center.

Also see [Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Review default and configurable retention periods for service, RUM Classic, synthetic, Log Monitoring, metric, diagnostic, and security data in Dynatrace Managed.").

## Dynatrace components

[Dynatrace OneAgent](/managed/platform/oneagent "Learn the monitoring capabilities of OneAgent.") collects all monitoring data within your monitored environment. Optionally, all data collected by OneAgent can be routed through a [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), which works as a proxy between Dynatrace OneAgent and the Dynatrace Cluster. In the absence of an ActiveGate, data collected by OneAgent is sent directly to the Dynatrace Cluster.

Dynatrace Managed clusters periodically exchange information, such as license and consumption data, with [Dynatrace Mission Control](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category.").

![Dynatrace Managed components](https://dt-cdn.net/images/dynatrace-data-security-managed-components-2-2690-71d9d32760.png)

Dynatrace Managed components

## Data segregation between customer environments

Dynatrace Managed allocates one cluster per customer account.

## Data encryption at rest

You should configure your own hard disk encryption and manage encryption keys on your own.

## Data encryption in transit

All data exchanged between OneAgent, ActiveGate, and Dynatrace Cluster is encrypted in transit. Data is serialized and deserialized using Google Protocol Buffers.

You can configure TLS versions as well as cipher suites, and you can use your own [SSL certificates](/managed/managed-cluster/installation/ssl-certificate-managed-cluster "Configure your own SSL certificate for a Managed Cluster instead of using the built-in Dynatrace-managed certificate automation.").

![Data encryption in transit](https://dt-cdn.net/images/dynatrace-data-security-managed-data-in-transit-2676-fee13f7c58.png)

Data encryption in transit

## User authentication

Users are managed by [configuring user groups](/managed/manage/identity-access-management/user-and-group-management/user-groups-and-permissions "Learn about the supported permissions and policies, how you can assign them to groups, and how you can manage your users and groups."), [SAML](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-saml "Learn how to connect your Dynatrace Server to a SAML server to import user groups or accounts that need access to your Dynatrace Managed environment."), [OpenID](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-openid "Learn how to use OpenID as an SSO IdP for the management of users and groups."), and [LDAP](/managed/manage/identity-access-management/user-and-group-management/manage-users-and-groups-with-ldap "Learn how to connect your Dynatrace Server to an LDAP server to import user groups or accounts that need access to your Dynatrace Managed environment.").

![User authentication](https://dt-cdn.net/images/dynatrace-data-security-managed-user-authentication-2525-25b24aca80.png)

User authentication

## Integrity verification of Dynatrace components

Dynatrace components are signed using code signing certificates within the continuous delivery and integration (CI/CD) pipeline.

Code signing certificates are stored on hardware tokens with Extended Validation (EV) code signing certificates for Windows. Signature verification is performed automatically before an update or installation. When installing a component for the first time, signature verification must be conducted manually.

![Integrity verification of Dynatrace components](https://cdn.bfldr.com/B686QPH3/as/sjrcqtck3j773vsf95tsmfrk/Data_security_controls-_Integrity_verification_-_Light_Mode?auto=webp&format=png&position=1)

Integrity verification of Dynatrace components

## Business continuity and high availability

A high-availability setup can be achieved by setting up multiple cluster nodes. The Dynatrace Mission Control team monitors the service quality and hardware utilization of Dynatrace Managed clusters. It uses high-availability multi-node setup and sends alerts when additional hardware is required for monitoring the environment. For more details, download the [Managed SLA﻿](https://www.dynatrace.com/company/trust-center/sla/managed/).

## Data backups and disaster recovery

Dynatrace Managed offers a built-in [backup mechanism](/managed/managed-cluster/operation/back-up-and-restore-a-cluster "Understand the steps and commands required to restore a Dynatrace Managed cluster.") that you must configure.

## Infrastructure monitoring

Dynatrace Managed clusters send regular health checks to Dynatrace Mission Control. Optionally, Managed clusters can be monitored by the Dynatrace self-monitoring cluster.

![Infrastructure monitoring](https://dt-cdn.net/images/dynatrace-data-security-managed-infrastructure-monitoring-2539-ba851e65a0.png)

Infrastructure monitoring

## Rollout of updates and hot fixes

Using a fully automated CI/CD pipeline, Dynatrace is able to roll out updates and hot fixes within a few hours. The Dynatrace architecture allows for zero-downtime upgrades of clusters.

Updates are delivered via Dynatrace Mission Control. New features are delivered every 4 weeks. Upgrades of the cluster, OneAgents, and ActiveGates can be performed automatically or manually.

![Rollout of updates and hot fixes](https://dt-cdn.net/images/dynatrace-data-security-managed-updates-3029-959588547a.png)

Rollout of updates and hot fixes

## Data access for Dynatrace Support

You have complete control over the [remote access](/managed/managed-cluster/configuration/configure-cluster-remote-access "Configure remote access permissions for your Managed Cluster, including scope options and role assignments for Dynatrace product experts.") to your cluster in case support is required. You can turn off remote access or configure it to require approval before access is granted. Dynatrace Support has access to Dynatrace Managed software (application-level) only, not to your underlying infrastructure or the system level.

Remote access is established by Dynatrace Mission Control, which is only accessible from within the Dynatrace corporate network. Remote access by Dynatrace Mission Control requires multi-factor authentication. Each access and any changes made are audit-logged and fully accessible.

![Data access for Dynatrace Support](https://dt-cdn.net/images/dynatrace-data-security-managed-support-access-2979-a5672b06a1.png)

Data access for Dynatrace Support

## Dynatrace secret leak prevention

Dynatrace can detect and prevent the leakage of Dynatrace secrets in source code repositories on GitHub. These secrets may include platform or API tokens that were inadvertently pushed to a source code repository. If a secret leak is detected, we will reach out to you and aid with remediation measures.

For details on reporting a security issue, see [Report a security-related concern](/managed/manage/data-privacy-and-security/data-security/report-a-security-related-concern "Find out how to report vulnerabilities and whom to contact in case of security concerns.").

![Secret leak prevention](https://cdn.bfldr.com/B686QPH3/as/g36rffwrskqsrjkb47ghr2w/Data_security_controls_-_Secret_leak_prevention_-_Light_Mode?auto=webp&format=png&position=1)

Secret leak prevention

## Compliance, certifications, and audits

Dynatrace undergoes annual, independent third-party audits and conducts penetration tests and red team assessments with independent security firms.

Having achieved several global and local certifications and accreditations demonstrates that we adhere to the most recognized international standards for security management.

Dynatrace also benefits from secure Amazon, Azure, and Google data centers that are certified for ISO 27001, PCI-DSS Level 1, and SOC 1/SSAE-16.

For the full list of certifications, see [Trust Center﻿](https://www.dynatrace.com/company/trust-center/).