---
title: Mission Control data exchange
source: https://docs.dynatrace.com/managed/managed-cluster/basics/mission-control-data-exchange
---

# Mission Control data exchange

# Mission Control data exchange

* Reference
* 5-min read
* Updated on May 19, 2026

Managed Clusters exchange data with Mission Control at least once or periodically. You can customize data exchange with Mission Control via [Configure cluster preferences](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences to manage proactive support reporting, remote access, data privacy, domain name, and community settings for your Managed Cluster.") to suit your organization's needs and data protection regulations.

To ensure compliance with data protection regulations:

* Review [what personal data is captured by Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.").
* [Configure Dynatrace to protect personal data](/managed/manage/data-privacy-and-security/configuration/configure-global-privacy-settings "Learn how to set up data privacy masking for end user IP addresses, geolocations, and user action names.").

## Data exchange with Mission Control

The following table documents the data that a Managed Cluster exchanges with Mission Control. All communication between a Managed Cluster and Mission Control is encrypted and initiated only by the Cluster. Certain data can be excluded from communication, such as Dynatrace's proactive access to your Clusters. However, some data is essential for Dynatrace and can't be disabled (for example, license data).

| Type | Frequency | Managed Cluster request | Mission Control response | Opt out |
| --- | --- | --- | --- | --- |
| Installation | Once during installation  With each update | License key | License name, account name, OneAgent download URL, OneAgent installation flag, OneAgent validation flag | No |
| Registration | Once after first startup | Cluster ID, license key | Registration status, username, password | No |
| License check | Once every 5 minutes | Cluster ID | Cluster ID, license key, license name, license type, license status, license details, account name, license creation date, license expiration date, license units limits, license units overage limits, pricing model, remote access flag, trial environment flag, country code, monitored host categories | No |
| License data | Once each hour | Cluster ID, start timeframe, end timeframe, *environments* license data  Per *environment*, see [Export license data](/managed/managed-cluster/operation/export-license-data "Learn how to export license data from the Cluster Management Console.") | License status, license key, license units usages, license units overages, remaining license units, *environments* license data  Per *environment*: environment UUID, license units usages, license units overages, remaining license units | No |
| Health check | Once every 2 minutes | Cluster ID, Cluster version, auto update flag, events reporting flag, remote access flag, time zone, traffic volume, admin email address, *Managed Cluster nodes*, *Cluster ActiveGates*, maintenance windows  Per *Cluster node*: node ID, node IP address, node state, server state, node startup timestamp, OS name, OS version, JVM info, CPU statistics, memory statistics, storage statistics, Cassandra version, Cassandra data files, Cassandra partitions, certificate type, custom settings  Per *Cluster ActiveGate*: ActiveGate ID, ActiveGate IP address, ActiveGate type, ActiveGate state, OS name, OS version, certificate type | Health status, health status description, minimum Cluster nodes, minimum CPU cores, minimum memory | No |
| Heartbeat | 20 requests every 10 minutes  12 requests every 10 minutes if remote access is disabled | Cluster ID, Cluster node ID, source type | Remote access flag, WebSocket URLs | No |
| Environment synchronization | Synchronization difference every 10 minutes  Full synchronization once a day | Environment UUID, environment name | – | No |
| Updates | Once each hour | – | Installation package label, installation package type, installation package version, minimum required version, *files*  Per *file*: file type, file size, download URL | No |
| Dynatrace Hub | Every 30 to 60 minutes | – | Images and text describing the capabilities and extensions available in Dynatrace Hub | No |
| [Application Security vulnerability feeds](/managed/secure/application-security#vulnerability-feeds "Access the Dynatrace Application Security functionalities.") | When updates are available | Vulnerability feed data | Vulnerability feed data | No |
| Cluster and OneAgent events (proactive support) | When events are available | – | Event type, event severity level, event timestamp, event description | Yes |

The following table documents the data that Nodekeeper exchanges with Mission Control. All communication between Nodekeeper and Mission Control is encrypted.

| Type | Frequency | Nodekeeper request | Mission Control response | Opt out |
| --- | --- | --- | --- | --- |
| Health check | Once per minute for each Cluster node | Nodekeeper IP address, master node flag, Cluster node state, server state, OneAgent traffic enabled flag, web UI traffic enabled flag, *component versions*, *component statuses*, Cluster multi-DC migration state, Cluster state, Cassandra PHA repair status, Cassandra repair state, *Cluster node directory statuses*, *Cluster node connectivity metrics*, maintenance mode  Per *component versions*: component name, component version  Per *component status*: component name, component status, component status description, result code  Per *Cluster node directory status*: Cluster node ID, directory path, directory status, directory status details, result code  Per *Cluster node connectivity metric*: node ID, server connected flag, server latency, host connected flag, host latency, Cassandra connected flag, Cassandra hints | Responsibility Cluster node IDs, Cluster status, Cluster status description, Cassandra quorum override flag, PHA downtime longer than 72h flag, PHA failover remediation flag, *Cluster node* statuses, *component* statuses  Per *Cluster node*: Cluster node ID, Cluster node status  Per *component*: component name, component status, Cluster node ID | No |

## Monitored technologies and product adoption

Dynatrace may retrieve information about the monitored technologies and product adoption in Managed Clusters, including the entities listed below, to inform you about incompatibilities and technology-specific risks associated with your Cluster.

Dynatrace companies (Dynatrace LLC and subsidiaries) [operate globally﻿](https://www.dynatrace.com/company/locations). Data may be transferred to, and processed by cloud services in the United States and other locations. For details, see [Data privacy and security](/managed/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

Relevant logs are accessible on each Managed Cluster node at `<datastore_dir>/log/server/audit.rest.proxy.log`. Dynatrace doesn't send host names or any information that could compromise your Cluster's security.

| Type | Data |
| --- | --- |
| ActiveGate | ActiveGate type, build version, operating system, supported capabilities, update status |
| Application configs | Configurations on application level covering aspects of cost control, key user actions, and synthetic checks |
| Dashboard configs | Configurations on dashboard level including basic sharing settings and tile types used |
| Digital Experience | Real User Monitoring user sessions, including mobile user sessions and Session Replay usage, and diagnostic metrics |
| Distributed traces | Diagnostic data on distributed traces and code-level insight storage |
| Dynatrace API | Aggregated statistics on Dynatrace API endpoints, including number of calls and response times |
| JavaScript framework | Aggregated statistics on JavaScript frameworks seen in monitoring |
| Log Monitoring | Aggregate statistics on log usage and indices |
| Monitored entities | Aggregated statistics on monitored processes, hosts, services, applications, and other related entities |
| Network zones | Aggregated statistics on network zones on cluster and environment-level, including OneAgent and ActiveGate counts |
| Requests | Aggregated statistics on key requests and request attributes |
| RUM | RUM JavaScript version used for mobile monitoring and metadata about monitored OS versions and agent crashes |
| OneAgent | Connected OneAgents with installer version, operating system, injection information, process and host technology, and host memory metrics |
| Extension | Active extensions with extension type, version, size, status, extension metrics, and host relationship information |
| Problem detection | Problems with status, severity, impact level, affected entity IDs, and problem event details |
| Security | Technical security problem and vulnerability metadata |
| Synthetic monitors | Active synthetic monitor configurations with monitor type, ID, and location name (for custom locations, the location name isn't sent) |
| Tags | Aggregated statistics of tag counts by tag type and entity type |

| Setting | Data |
| --- | --- |
| Alerting profile | Alerting profile configurations |
| API token permissions | Aggregated statistics on API tokens by permission level |
| Conditional procedures | Aggregated statistics on rules for management zones and automatically applied tags |
| Deep monitoring | OneAgent Early Access release and troubleshooting feature settings |
| Environmental configs | Aggregated statistics on preference settings and advanced environment configurations |
| Feature flags | Settings for environment features that are set to non-default |
| Integrations | Integration settings including problem notifications, Dynatrace API, Dynatrace modules, user session export and release issue tracker integrations |
| Maintenance windows | Aggregated statistics on configured monitoring windows and their settings such as maintenance type, provided text length, schedule, filters |
| Metric events | Aggregated statistics on configuration count, model and filter types |
| Metrics | Environmental metrics metadata, configured metric data types, metric usage statistics |
| Preferences | Settings for OneAgent updates and data privacy |
| Service Level Objectives | Aggregate statistics on Service Level Objectives usage |
| Tile filters | Aggregated statistics on tile filters that can optimize scalability |
| Virtualization | Configured virtualization types such as AWS, Azure, and VMware |

## Related topics

* [Configure Cluster preferences](/managed/managed-cluster/configuration/configure-cluster-preferences "Configure cluster preferences to manage proactive support reporting, remote access, data privacy, domain name, and community settings for your Managed Cluster.")