---
title: Pre-upgrade information
source: https://docs.dynatrace.com/managed/upgrade/up-information
scraped: 2026-05-12T12:07:03.311056
---

# Pre-upgrade information

# Pre-upgrade information

* Published Apr 24, 2023

This pre-upgrade information helps you understand what changes to expect while upgrading from Dynatrace Managed to SaaS deployment and to plan accordingly. This page helps you to understand the most important differences that you need to consider before you start the upgrade.

## Reasons to upgrade

Preparation and planning of the migration to SaaS start with understanding the benefits of migration. A key reason why many organizations are upgrading to SaaS deployments is to access SaaS-only technologies and Dynatrace capabilities like Grail, AppEngine, and AutomationEngine.

Grail is architected as a Massively Parallel Processing (MPP) data lakehouse, scaling to thousands of nodes. At a massive scale, the underlying infrastructure attributes must be consistently implemented, controlled, and balanced, which is not practical in physical data centers.

Additionally, with the SaaS deployment model, Dynatrace operates your environment holistically, providing a secure environment certified to comply with ISO 27001 and [other standardsï»¿](https://www.dynatrace.com/company/trust-center/#security), configurable privacy features to enable customers to meet their compliance obligations, and stringent Dynatrace uptime SLAs. This reduces your total cost of ownership and provides users with faster and more resilient access to the Dynatrace environment.

## Data retention periods and limits

An overview of the current data retention periods and how they differ in Dynatrace Managed and SaaS can be found in [Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types."). If a retention limit was increased in your Dynatrace Managed environment, you need to review it to determine if it's still feasible for your new Dynatrace SaaS environment. The [Pre-upgrade assessment](/managed/upgrade/up-plan/feasibility-checklist "Pre-upgrade checklist to identify potential upgrade warnings or challenges.") can help you understand the important differences and limits.

## Business continuity

Every Dynatrace Cluster is deployed in three data centers within a hyperscaler region, assuring failover and providing continuous operation in the case of the loss of one data center until the lost data center is available again.

AWS, Azure, and Google protect and monitor physical equipment from security threats and environmental hazards. Dynatrace implements the following means for assuring business continuity in the event of an emergency:

* Datacenter failover within a region
* Backup

### Datacenter failover within a region

Dynatrace uses a clustered architecture and a high availability setup within each region, where three data centers are utilized to allow the failover of data centers within a region:

* Each cluster uses multiple data centers (AWS availability zones, Azure availability zones, or Google Zones) for redundancy within the same geographical region.
* For each Dynatrace Cluster, the required resources are over-provisioned.
* If a Dynatrace cluster fails, another cluster in the same or a different data center can take over, while the fail-over process recreates the failed instance. Data is replicated in other data centers. The architecture allows for the failure of an entire data center. Fail-over is handled automatically.

See also [Business continuity and high-availability](/managed/manage/data-privacy-and-security/data-security/data-security-controls#business-continuity-and-high-availability "Learn about data security and operational security controls.").

### Backup

Dynatrace product data is backed up to a dedicated storage account on the respective cloud provider. For details, see [Data backups and disaster recovery](/managed/manage/data-privacy-and-security/data-security/data-security-controls#data-backups-and-disaster-recovery "Learn about data security and operational security controls.").

## Dynatrace availability regions

Dynatrace provisions and manages the cloud provider infrastructure and operates the Dynatrace platform on clusters deployed in different regions of the hyperscalers. See [Data storage](/managed/manage/data-privacy-and-security/data-security/data-security-controls#data-storage "Learn about data security and operational security controls.") section to learn what regions are currently available.

## SaaS versus Managed deployment

This page provides an overview of the differences between Dynatrace Managed and Dynatrace SaaS. If you have more detailed questions when upgrading to SaaS, contact a Dynatrace product expert via live chat within your Dynatrace environment.

| Topic | Managed | SaaS | Considerations for Upgrade |
| --- | --- | --- | --- |
| Access to Grail, AppEngine, and AutomationEngine | No | Yes | Only available in selected AWS/Azure regions. Some of the platform features may still be available in the preview. To get preview features enabled, contact a Dynatrace product expert via live chat within your environment. Learn more about [Upgrade to Dynatrace SaaSï»¿](https://docs.dynatrace.com/docs/shortlink/up-upgrade). |
| Logs monitoring capabilities | [Log Monitoring Classic](/managed/analyze-explore-automate/log-monitoring#log-monitoring-classic "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.") | [Log Management and Analytics powered by Grailï»¿](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics) | Only available in selected AWS Regions. Some of the platform features might still be available in the preview. To get preview features enabled, contact a Dynatrace product expert via live chat within your environment. |
| Dynatrace Hub | Yes (except Managed Offline) | Yes |  |
| [Application Security](/managed/secure/application-security "Access the Dynatrace Application Security functionalities.") | Yes | Yes |  |
| Multi-environment private synthetic location | Yes, via Cluster ActiveGate | Not supported |  |
| Deployment location and region | Customer preference defined based on data center location. | AWS/Azure/GCP on supported regions. For details, see [Data storage](/managed/manage/data-privacy-and-security/data-security/data-security-controls#data-storage "Learn about data security and operational security controls."). | Plan and decide on the best hyper scaler/region for your SaaS environments. As Dynatrace creates your SaaS environments, this information is needed in advance. |
| Multiple availability zone deployment | Customers need to take care. | Always in 3 availability zones with failover (overcomes outage of one availability zone) |  |
| Native Service Integration with hyper scalers | No | Yes, for Dynatrace deployed on Microsoft Azure. | Deploying your Dynatrace SaaS environment integrated with Microsoft Azure requires provisioning the Dynatrace SaaS environment via the Azure Marketplace. For further information, see [Azure Native Dynatrace Service](/managed/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.") or contact a Dynatrace product expert via live chat within your Dynatrace environment. |
| API Call Limits | API rate and volume are dependent on hardware and Managed configuration. | Scalable on SaaS. | For high-volume use cases, contact a Dynatrace product expert via live chat for details and further support. |
| Storage and compute | Customers need to buy, provision, and support at capacity based on needs. | Dynatrace manages and takes care of proper sizing. | If you plan to significantly increase your usage of Dynatrace SaaS (for example, onboard a very large number of OneAgent instances), contact a Dynatrace product expert via live chat in advance. |
| Data retention policy | Custom, based on allocated storage. | Scalable retention periods. Some data retention periods may be extendable at additional cost. | Read more about differences in [Data retention periods](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types."). |
| Distributed traces retention | 10 days, configurable with maximum 365 days | 10 days, increase scalable with the license | If you have special needs, contact a Dynatrace product expert via live chatâthe limit of 10 days in SaaS may be extendable incurring additional costs. |
| RUM user sessions, Session Replay retention | 35 days | 35 days | - |
| Trace volume capture | Capped by process | Auto adapted per process and balanced across host units | For details, see [Adaptive Traffic Management for Dynatrace Managed](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control."). |
| Capture rate | Limited by customer's hardware and process; limits. | 250 full-service calls / min / active host unit. | Can potentially be increased at additional cost. |
| SSO and LDAP | SSO with SAML/OIDC; LDAP | SSO with SAML/SCIM; LDAP via SCIM |  |
| Web UI domain and SSL management | Automatic domain and SSL certificate provisioned by Dynatrace via Let's Encrypt. Custom certificates are possible. | Automatic domain and SSL certificate provisioned by Dynatrace. Custom certificates and domain names can be implemented with organizational proxy configurations. |  |
| Email notifications | SMTP or via Dynatrace email service | Only Dynatrace email service | Let know email recipients about a change of "from" e-mail address |
| Problem notifications | Network configuration must be established and maintained by the customer. | Customer must configure network connection so that on-premises services are reachable from Dynatrace SaaS. |  |
| SQL bind variables | Available | Available [depending on licensingï»¿](https://docs.dynatrace.com/docs/shortlink/sql-bind-variables#faq). |  |
| Configuration change control | Configuration can be changed by the Mission Control team and customer; option to restrict/prevent changes done by Dynatrace/Mission Control. | Cluster/System changes only by Dynatrace ACE team; environment configuration by Dynatrace and customer. |  |
| Audit log | Cluster Audit Change log in CMC UI and audit log files. Changes in environments are available additionally via REST API. | Audit log available via REST API for environment configuration changes; Cluster/infra changes on demand via CSM. |  |
| License management | All options available, except Application Security and Cloud Automation; Ability to control environment license utilization; Export of data available but only in raw format. | Charts available; control of utilization only in Dynatrace Platform Subscription (DPS); data export available. |  |
| Dynatrace Cluster infrastructure | Cluster Node Hosts procured, provisioned and managed by the customer. | No hardware required. All are hosted by Dynatrace. |  |
| Cluster upgrades and OS patches | Automatic upgrades every 4 weeks; OS Patches by Customer | Automatic upgrades every 2 weeks; OS Security patches by Dynatrace ACE team. Advanced notifications are available. |  |
| OneAgent maintenance | Upgrades can be centrally scheduled, controlled by customer. | Upgrades can be centrally scheduled, controlled by customer. |  |
| Cross-regional data replication | Additionally paid via Premium High Availability | Cross availability zones within a single cloud region data replication |  |
| Backup/restore | On customer's provided additional NFS storage; Elasticsearch snapshots every 2 days; Cassandra once a day; RPO = 24h; RTO = 24h. | Automatic by Dynatrace ACE team; no additional storage required; RPO = 24h; RTO = 24h. |  |
| Self-monitoring | Local self-monitoring environment, dashboard, and metrics available. | Selected self-monitoring metrics available within the Dynatrace environment. | For details, see [Self-monitoring metrics](/managed/analyze-explore-automate/metrics-classic/self-monitoring-metrics "Explore the complete list of self-monitoring Dynatrace metrics."). |
| Security and privacy | Data located on-premises (for example, log analytics). | Data located in SaaS (logs, transaction data, password vault). |  |

Questions?

Visit the [Upgrade to SaaS forumï»¿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.