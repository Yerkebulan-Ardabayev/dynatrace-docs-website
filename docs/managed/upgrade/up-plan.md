---
title: Plan deployment upgrade
source: https://docs.dynatrace.com/managed/upgrade/up-plan
---

# Plan deployment upgrade

# Plan deployment upgrade

* Published Apr 24, 2023

During the Plan phase you collect requirements, adjust to differences, create a scope, and decide on the approach to upgrading to SaaS. The Plan phase should result in a detailed plan for performing the upgrade to SaaS deployment and a well-prepared architecture of the target solution within the Dynatrace platform.

![Planning of Managed to SaaS upgrade](https://dt-cdn.net/images/upgrade-to-saas-plan-3452-4791b81b19.png)

Planning of Managed to SaaS upgrade

## Step 1 - Discover

Main objectives of this step:

* Assess your current situation
* Identify your challenges and collect requirements
* Consider your requirements for data security, privacy, and compliance
* Assess the feasibility of upgrading to SaaS

The following topics should be considered in support of the above objectives:

### Assess your current needs

As outlined in [Pre-upgrade information](/managed/upgrade/up-information "Get essential information about upgrading to Dynatrace SaaS and related concepts."), you need to be aware of the [differences between SaaS and Managed](/managed/upgrade/up-information#saas-versus-managed-differences "Get essential information about upgrading to Dynatrace SaaS and related concepts.") before you upgrade to SaaS deployment. For each difference that you need to act on additionally, create an action item in the Upgrade Plan document.

### Review your requirements for data security, privacy, and compliance

To provide value to its customers, Dynatrace collects large amounts of data, often also including confidential and personal user information. Dynatrace is aware of the risks associated with data security and privacy, and can summarize our approach as follows:

#### Data security

A use-case-centric approach enables you to configure Dynatrace to your specific needs and compliance requirements, including GDPR and CCPA compliance. You may exclude confidential data, including personal data, at capture with ease of configuration and strong defaults to automatically exclude data, including IBANs and payment card numbers for PCI-DSS compliance.

You may instead choose to process confidential data on the cluster to benefit from the initial analysis of the data, without storing the data on the cluster—the data is excluded at storage, with easy configuration and helpful defaults.

Additionally, you have fine-grained control over access to your data and the ability to automate transparency into access events via an audit log API that enables you to integrate audit log events with your internal SIEM (security information and event management) solutions and a permission management API to automate restrictions in access in response to SIEM.

To explore details, please review the following pages:

* [Data security controls](/managed/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.")
* [Secure development controls](/managed/manage/data-privacy-and-security/data-security/secure-development-controls "Learn how we ensure complete security for all Dynatrace software components and development practices.")

#### Data privacy

Strong privacy-by-design and privacy-by-default enable you to configure Dynatrace to maximize value while complying with your legal requirements. Investigate and list actions you need to undertake to cover the following aspects:

* Data privacy
* Data privacy APIs
* Environment-wide settings
* Session Replay
* Real User Monitoring

Information about each of these topics can be found at the [Dynatrace Trust Center﻿](https://www.dynatrace.com/company/trust-center/). In particular, please review these topics:

* [Personal data captured by Dynatrace](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")
* [Levels of data protection](/managed/manage/data-privacy-and-security/data-privacy/levels-of-data-protection "Learn how Dynatrace protects end-user information by applying situation-dependent levels of protection.")

#### Data retention periods

Dynatrace Managed deployment provides the flexibility to set retention periods at the cost of corresponding infrastructure. With Dynatrace SaaS, default retention safeguards are optimized and applied however each can be adjustable, based on individual considerations.

### Platform safeguards

If limits have been increased previously in your Dynatrace Managed environment, an in-depth review of retention periods and limits will help you to identify safeguards that might exceed default settings in your Dynatrace SaaS environment.

For each safeguard, Dynatrace defines a default and a hard limit. On SaaS, settings may be increased above the default limit, up to the hard limit, however, such increases may incur additional licensing costs due to higher storage or compute utilization.

If data retention limits need to be increased above the default SaaS limit, we recommend that you verify increased limit requirements with your Dynatrace team ahead of the planned upgrade and clarify any potential implications due to requesting limit increases.

Limits generally cannot be increased above the hard limit and if there is a requirement to exceed a hard limit, please reach out to [Dynatrace Support﻿](https://www.dynatrace.com/services-support/).

### SQL bind variables

Bind variables generate high network and storage demands, so the capture of SQL bind variables is not enabled by default. To learn Dynatrace SaaS deployment availability conditions and how to get started, see [Support for SQL bind variables](/managed/observe/infrastructure-observability/database-services-classic/support-for-sql-bind-variables "Learn how you can enable Dynatrace OneAgent to capture the values of bind variables.").

### API limits

You can use the Dynatrace API to automate your monitoring tasks and export different types of data into your third-party reporting and analysis tools. There are no differences in handling API request limits between Dynatrace Managed and SaaS. See [Dynatrace API - Access limit](/managed/dynatrace-api/basics/access-limit "Find out about payload limits and request throttling that may affect your use of the Dynatrace API."). If API request throttling is identified as critical, or if your Dynatrace Managed Cluster has been explicitly sized or specified to handle high volumes of API calls, contact your Dynatrace team.

### Dynatrace software updates

In Dynatrace SaaS, all cluster software upgrades are managed by Dynatrace, automatically ensuring the most secure and optimized version of Dynatrace, as well as access to all of the latest advances, including Early Access features. SaaS updates take place automatically with no interruptions or downtime to monitoring and have been designed to be seamless. Dynatrace SaaS clusters are upgraded approximately once every two weeks. While the cluster will be automatically updated, you retain full control over [OneAgent update](/managed/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.") and [ActiveGate update settings](/managed/ingest-from/dynatrace-activegate/operation/update-activegate "Configure Environment ActiveGate automatic updates---update mode, target version, and update windows---and download or install manually.").

### Adaptive Traffic Management

One of the core capabilities of Dynatrace is the automatic capture of distributed traces. Dynatrace protects the performance and availability of the platform by proactively managing the rate of traffic capture. The method of Adaptive Traffic Management on Dynatrace SaaS is different from Dynatrace Managed: Automatically adapted and tuned with less dependency on the individual monitored application architecture. Safeguards are applied to the overall volume sent to the Dynatrace environment, enabling limits to scale with licensing and allowing high-volume entry points to send more traffic. For in-depth information, read [Upgrade to Dynatrace SaaS﻿](https://docs.dynatrace.com/docs/shortlink/up-upgrade) and note the specified limits.

### RUM overload prevention

You can control the count of captured web, mobile, and OpenKit app user actions by setting the maximum user actions per minute limit. Once this limit is reached, Dynatrace automatically throttles the number of user sessions captured until the number of user actions returns to within licensed limits. Plan to set up RUM overload prevention to match your requirements in your Dynatrace SaaS environment. For details, see [RUM: What does a 'Max. user actions per minute exceeded' message mean?﻿](https://dt-url.net/h92389d) in the Dynatrace Community.

If any additional information is needed to ensure that data security, privacy, compliance and governance concerns have been addressed, please contact your Dynatrace Sales team.

## Step 2 - Strategize

Main objectives of this step:

* Assess the scope of upgrading to Dynatrace SaaS
* Understand the effort required for upgrading to Dynatrace SaaS
* Assess your capacity and capabilities
* Decide on a self-service upgrade or assisted approach with Dynatrace ACE Services
* Create a plan for upgrading to Dynatrace SaaS

The following topics should be considered during this step and support the process of achieving the above objectives:

### Data migration

Dynatrace stores three essential data types

* Configuration data
* User accounts and permissions
* Historical monitoring data

Migrating configuration data such as dashboards, applications, and tags is important to preparing your new SaaS environment for receiving monitoring data from all the sources previously reporting into your Dynatrace Managed cluster. No matter if you migrate your configuration or start from scratch, you need to set up new user accounts and permissions to the SaaS environment. The effort and scope depend on how many users, groups, management zones and IAM policies you plan to migrate.

Due to technical constraints, it's not possible to move any historical monitoring data (such as metrics, traces, problems, events, and logs) from one environment to another environment. However, data can still be accessed in your Dynatrace Managed Cluster. Dynatrace Managed Clusters can be operated in parallel if access to historical data is required. This may require running dual Dynatrace Managed and SaaS licenses.

You may also find it helpful to set up [Set up cross-environment tracing](/managed/observe/application-observability/distributed-traces/analysis/connect-environments "Analyze requests across environment boundaries.") and [Create remote/multi-environment Dynatrace dashboards](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.") to connect your Dynatrace Managed and SaaS environments for data access.

### Running concurrent Dynatrace Managed and SaaS licenses

Dynatrace may provide, upon request, additional licenses for Dynatrace SaaS that can be used at no charge during your upgrade process. This provides you with a sufficient timeframe to collect longer trending data on your SaaS environment, in addition to ensuring that the destination SaaS environment is operational before switching over. SaaS licenses can only be used for the workloads and settings that are being migrated and are provided only during the period of the upgrade, up to six months. Upon the completion of the upgrade process, Dynatrace Managed licenses will be deactivated, and you'll be billed for the SaaS licenses. Please contact your Dynatrace sales team for more details.

### Estimate the effort and select the right approach

Estimate the effort, skills, and resources needed to execute the upgrade. Start with cataloging, evaluating the environment, and identifying the configuration items that must be migrated. Next, catalog and review OneAgent and ActiveGate instances deployed across your environment. This will help you determine the preferred approach in upgrading to SaaS.

#### What upgrade approach options do I have?

Each organization has unique needs. Dynatrace presents two distinct upgrade approaches:

* The Big Bang approach  
  Recommended for customers with a highly interconnected and interdependent infrastructure landscape.
* The Phased approach  
  Recommended for organizations with siloed teams and infrastructure entities.

Each method comes with its advantages and considerations. Choose the strategy that aligns best with your organizational goals and operational preferences.

#### Big Bang approach

The Big Bang approach offers a comprehensive migration in a single instance. This strategy is ideal for organizations aiming for a quick and decisive transition.

Advantages:

* A highly connected and interdependent monitoring setup is maintained
* Everything is moved at once with minimal risk of monitoring downtime
* It is a time and cost-efficient upgrade process

Disadvantages:

* There is a high coordination and communication effort
* We recommend tests in smaller sandbox or pre-production environments

#### Phased approach

The Phased approach involves a gradual transition, allowing you to migrate specific components or user groups over time. It provides flexibility and minimizes potential disruptions to your operations.

Advantages:

* Siloed infrastructure and organizational setups can be migrated one-by-one.
* Trial and error migrations with quick feedback and learning on how to setup new SaaS tenant
* No downtime due to the temporary hybrid setup

Disadvantages:

* Temporary hybrid model can result in a disconnect of Full-Stack Monitoring and a disruption in Real User Monitoring
* Extended upgrade timeline and higher costs due to longer periods of duplicated deployments (hardware & cloud)
* Dynatrace web UI differences between Dynatrace Managed and Dynatrace SaaS

#### Catalog and evaluate the environment

Start with a review of which configuration items need to be migrated and determine if they can be migrated using an automated utility or will require manual effort. This is an opportunity to perform environment clean-up and apply best practices and standards. Excessive or legacy configuration items can be left behind. Most configuration items such as tags or management zones are usually migrated in full, while others such as dashboards, can be reviewed and migrated selectively.

Here is a list of configurations that are commonly migrated:

* Network zones
* Management zones
* Custom services
* Synthetics
* Application definitions
* Anomaly detection
* Notifications and integrations
* API tokens
* OpenTelemetry

* User groups
* Tagging rules
* Services configuration
* Cloud automation
* Deep monitoring settings
* Alerting profiles
* Maintenance windows
* Credentials vault
* Cloud platform integrations

* SSO setup
* Naming rules
* Extensions
* Process group detection
* Log monitoring
* Dashboards
* SLI/SLOs
* Mainframe volumes
* Custom metrics

#### Catalog and evaluate deployed Dynatrace components

Following the documentation of the Dynatrace configuration that has to be applied to the Dynatrace environment, it is helpful to catalog and review the components configured or deployed across your environment and determine the preferred approach to moving them to Dynatrace SaaS. The component versions will impact the capabilities of your deployed OneAgents to connect to the Dynatrace platform, as well as affect the methods available for the upgrade.

Update

We strongly recommend that you update Dynatrace monitoring components to the latest versions and apply standardized configurations and best practices.

Dynatrace components that must be moved to the new Dynatrace environment are:

* OneAgent instances (such as hosts, PaaS, and Kubernetes/Openshift)
* ActiveGate extensions
* OneAgent extensions
* External or custom sources
* ActiveGate instances (routing traffic, monitoring cloud environments, monitoring remote technologies with extensions, synthetic monitors, zRemote modules)

For each monitoring item, identify the OneAgent or extension version and determine the necessary updates required from both a technical and process perspective.

* Newer versions of OneAgents provide more configuration abilities and the version of deployed OneAgents dictates whether your OneAgents need to be updated or reinstalled entirely.
* Support for OneAgent versions is 9-12 months; review the oldest supported versions to validate support.
* Migrating RUM applications from Dynatrace Managed to Dynatrace SaaS without side effects on either environment requires OneAgent version 1.289+; update your OneAgents before moving them to Dynatrace SaaS.
* A restart of applications using Full-Stack Monitoring is required and should be incorporated into the upgrade plan.

OneAgent update

* For more information regarding OneAgent capabilities, see [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.").
* For information regarding OneAgent update capabilities and approaches, see [OneAgent Update](/managed/ingest-from/dynatrace-oneagent/oneagent-update "Learn how to update OneAgent.").
* For more information regarding the latest supported versions, see the oldest supported version in the latest release notes at [OneAgent Release Notes](/managed/whats-new/oneagent "Release notes for Dynatrace OneAgent").

#### Decide on the migration approach: self-service or with Dynatrace ACE Services

Dynatrace offers different levels of [ACE service﻿](https://www.dynatrace.com/services-support/ace-services/) engagements. If you want assistance from Dynatrace experts for upgrading to SaaS, please reach out to your Sales representative.

### Create an upgrade plan

Creating a feasible plan to upgrade to SaaS is essential to maximizing the operation's success. We recommend start planning and preparing at least 2-3 months in advance of the actual migration phase. In previous steps, you should've listed action items that solve differences between the two deployment models and clarify the scope. Now, it's time to list all actions required in the execution phase. Following are the details and aspects that should be considered when creating the plan for your upgrade to SaaS.

#### User management

Define users, groups, and permissions for Dynatrace

* User groups
* Users
* Permission mapping - environment
* Permission mapping - management zone

#### Configuration inventory

A review of the existing Dynatrace Managed configuration results in a list of configurations that need to be applied to your new Dynatrace SaaS environment. To run a pre-upgrade checklist, go to [Pre-upgrade assessment](/managed/upgrade/up-plan/feasibility-checklist "Pre-upgrade checklist to identify potential upgrade warnings or challenges.").

#### Pre-upgrade activities

If you are using manual tagging in your Managed environment, convert those rules to automatic tagging rules. To complete the documentation of the existing Dynatrace Managed environment, the following should be identified and securely documented:

* Review the API and PaaS tokens used and identify the purposes.
* Securely document credentials for cloud and container platforms such as AWS, Azure, and Kubernetes.
* Coordinate with and onboard all teams that are affected or have ownership for parts of the migration.
* Your platform teams should plan deployment file updates and restarts for all their infrastructure and services.
* Your network team should assist beforehand to replicate all firewall rules from previous environment to new environment. They should also have to be on hand during migration in case of issues.
* Plan communication channels and messages that must be sent out to applicatino teams. Get required approvals from the team leads and managers on a date when it is feasible to restart your applications and services.
* Create a tracking lists. For example, a spreadsheet with each application team's main contact that will be on call during the weekend to restart their applicatino.
* Ensure the environment is properly sized ahead of time. Contact your Dynatrace team at least 1 week in advance for notice of migrating more than 5,000 OneAgents.

#### Configuration migration

The goal is to apply the same configuration in your Dynatrace Managed environment to your new Dynatrace SaaS environment. This is ideally done automatically where possible with the support of tools such as Dynatrace Configuration-as-code.

#### Monitoring inventory

As outlined earlier ([Catalog and evaluate the Dynatrace components deployed](#catalog-and-evaluate-dynatrace-components)) this results in a list of the Dynatrace components currently deployed in your Dynatrace Managed environment.

#### Monitoring migration

All Dynatrace components in the Managed environment must be re-configured to report to the new Dynatrace environment. This might also result in replacing existing deployed components with newly deployed components for Dynatrace, such as ActiveGates. For details, see [Upgrade your deployment](/managed/upgrade/up-execute-upgrade "Execute specific steps to migrate your Managed configurations to Dynatrace.").

#### Operationalization

Adjust existing processes and workflows, including any integrations with ITOM/ITSM and update any references to the Dynatrace Managed environment to the new Dynatrace environment.

#### Firewall constraints for RUM

The configuration of your firewalls, proxies, and web servers will require adjustment since cookie names have environment specific suffixes. For details, see [Infrastructure pass-through requirements for RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/infrastructure-pass-through-requirements-classic#cookies-web "Learn which requests, headers, and cookies must pass through your infrastructure for RUM to work as expected.").

## Step 3 - Design

During this step, the target design for the Dynatrace SaaS platform is created. In addition to establishing a new Dynatrace SaaS environment, the surrounding technical architecture, (for example, network design, capacity and operational impact) also need to be considered and specified to enable the provisioning and deployment steps in subsequent phases.

Main objectives of this step are to

* Review dependencies that might impact the upgrade
* Review constraints that might impact the upgrade
* Define the target architecture

The output of this step might be a single diagram, a high- or low-level architectural design document, or a written specification summary—depending on governance, processes, and your requirements.

During the Design step, the following considerations should be covered:

### Consolidated SaaS environment

In Dynatrace Managed, you have control to create environments as required. However, in Dynatrace SaaS, it's important to establish a target design of environments. The sizing and configuration of environments will be required input when the SaaS environment is provisioned—this will be valuable input when considering configuration optimizations. You can also opt to consolidate multiple Dynatrace Clusters into a single tenant which provides benefits but also a few considerations:

* A single source for configuration, dashboards, and maintenance windows greatly reduces administrative overhead.
* A single fault domain allows Dynatrace Davis AI to provide a more complete analysis, as well as have a single place to view complete traces from multi-region applications.
* More applications, services, processes, and hosts to manage all in one place. Metadata, tagging, management zones, network zones, and naming best practices will become more critical to ensure correct entity and data grouping, as well as access controls.

Please note that consolidation of environments may require additional vetting of SaaS limits to ensure that the new, consolidated environment remains within platform safeguard limits.

#### Dynatrace environment consolidation architecture example

Here is an example of what an environment consolidation plan can look like.

* 14 Dynatrace Managed environments, on two clusters were consolidated into three 3 SaaS environments
* Environments grouped in SaaS by stage instead by application
* Reduced complexity of integrations, configuration, and user access to data
* Full end-to-end transaction tracing without cross-environment configuration

![Dynatrace environment consolidation architecture example](https://dt-cdn.net/images/saas-upgrade-env-consolidation-example2-2698-07f638fff7.png)

Dynatrace environment consolidation architecture example

### Network zones

Dynatrace allows the definition of network zones that represent the architecture of your network. Network zones are used to route telemetry data from OneAgent to your Dynatrace Cluster in an optimized way and avoid unnecessary network traffic across data centers and network regions. For more information, see [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.").

For information regarding ActiveGate considerations, see [Dynatrace ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.").

### ActiveGate deployment and sizing

ActiveGate allows you to optimize and minimize bandwidth usage by deploying the correct number of ActiveGate instances in each data center and enforcing the use of network zones. New ActiveGate instances should be provisioned for the migration, and existing ActiveGate instances should be decommissioned after the migration is complete. This ensures that your Dynatrace monitoring is uninterrupted. This includes considering how to deploy/configure:

* Environment ActiveGates - OneAgent traffic (SSL Certificate)
* Environment ActiveGates - Cloud & Virtualization
* Environment ActiveGates - Synthetics
* Environment ActiveGates - Extensions
* Environment ActiveGates - Log Ingest (SSL Certificate)
* Environment ActiveGates - z/OS Mainframe

When sizing the ActiveGates, please ensure that you have sufficient capacity for failure events. Dynatrace best practices dictate at least two ActiveGates per data center, with additional instances added based on capacity requirements.

### Review dependencies and constraints that might impact the upgrade

Moving from Dynatrace Managed to a SaaS deployment might require changes to your networking setup, as well as a re-examination and reconfiguration of external systems integrated with Dynatrace (for example, for problem notifications, see [Problem notifications](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.")). Reviewing the current networking setup and the integrated systems forms the basis for further architecture considerations; review and design your Dynatrace components (ActiveGate) using network zones.

### Define the target architecture

The target design for the Dynatrace platform is created. In addition to configuring and setting up a new Dynatrace environment, the surrounding technical architecture—for example, network design, capacity, and operational impact—needs to be considered and specified to enable the provisioning and deployment steps in subsequent phases.

The output of the design phase may be a single diagram, a high-level or low-level architectural design document, or a written specification summary, depending on your governance, processes, and requirements. You can find a sample target architecture diagram for a basic Dynatrace Managed deployment below. We've used the following assumptions:

* A single Dynatrace Managed Cluster in DC-1 is migrated to a single SaaS environment (ID: vre43162)
* OneAgents and external automation leverage a single Environment ActiveGate to report data from/to the cluster
* Agentless, Mobile RUM, Synthetic and OneAgents outside of DC-1 leverage a Cluster ActiveGate to report data to the cluster
* A corporate firewall prevents direct network access to Dynatrace SaaS.
* Green arrows and components represent needed adjustments during the upgrade

![Sample upgrade architecture diagram - basic](https://dt-cdn.net/images/saas-architecture-basic-3234-10abf03beb.png)

Sample upgrade architecture diagram - basic

Planning the upgrade results in a plan tailored to the needs of your organization and your target SaaS architecture. Starting with understanding how your organization can benefit from Dynatrace and learning how vital aspects such as security are improved with Dynatrace, a review of your current Dynatrace Managed landscape will provide a solid basis for executing a smooth upgrade.

Please see the other topics in this guide for a more detailed overview of essential aspects that should be known when considering/preparing for an upgrade to Dynatrace SaaS.

Learn more about the following aspects that should be taken care of when upgrading to Dynatrace SaaS:

* Dynatrace software upgrades
* Adaptive Traffic Management in Dynatrace
* Self-monitoring in Dynatrace
* Infrastructure operated and managed by Dynatrace
* SLAs of Dynatrace

Questions?

Visit the [Upgrade to SaaS forum﻿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.

## Related topics

* [Pre-upgrade assessment](/managed/upgrade/up-plan/feasibility-checklist "Pre-upgrade checklist to identify potential upgrade warnings or challenges.")