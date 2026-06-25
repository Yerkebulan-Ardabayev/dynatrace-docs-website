---
title: Run after deployment upgrade
source: https://docs.dynatrace.com/managed/upgrade/up-post-upgrade
scraped: 2026-05-12T12:07:07.254893
---

# Run after deployment upgrade

# Run after deployment upgrade

* Published Apr 24, 2023

![Actions after upgrading Managed to SaaS](https://dt-cdn.net/images/upgrade-to-saas-process-run-3454-7c363359e8.png)

Actions after upgrading Managed to SaaS

As the monitoring is moved to a new SaaS environment, a review and refinement of the use of Dynatrace in the customer environment ensure that the observability services in your organization remain optimal, consistently providing maximum value to your organization and leading to further exploration of the use of observability in the customer organization. This eventually allows leveraging resources freed up through the move of an on-premises service operated on customer infrastructure to a fully Cloud hosted service operated by Dynatrace.

This page describes three steps to consider when running Dynatrace SaaS after the upgrade from Dynatrace Managed.

## Step 1 - Enable

Main objectives of this step:

* Invite users to new SaaS environments
* Set up user permissions
* Communicate the update to Dynatrace SaaS to your users
* Train your users on a new platform

### On-board users

Dynatrace allows you to manage user permissions based on user account membership in user groups. You can manage these accounts and groups locally or through an Identity Provider of your choice via [SAML 2.0ï»¿](https://docs.dynatrace.com/docs/shortlink/access-saml) or [SCIMï»¿](https://docs.dynatrace.com/docs/shortlink/access-scim) protocol. When your first SaaS environment is provisioned, you'll get access to the Account Management service. Then, you can start configuring your access management settings and setting up user permissions manually or automatically with [Account Management API](/managed/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.").

Communicate any operational differences which may impact service design for Dynatrace users. For most users, there should be no noticeable difference in transitioning from Dynatrace Managed to SaaS.

### Revisit roles and access control

Reassess the roles of Dynatrace administrators, users, and stakeholders and identify opportunities to optimize interactions and processes further. Determine if role access needs to be revised and implement new access policies to maximize the reach and value which Dynatrace can bring.

Review access control structure, policies, and procedures, considering any adjustments needed due to management of Data Security and Privacy, and access to the SaaS platform. Employ SSO to integrate and automate access procedures, advancing your Monitoring-as-a-Service practice as much as possible.

## Step 2 - Expand

Main objectives of this step:

* Learn how to leverage new Dynatrace capabilities
* Optimize your Dynatrace experiences

### Extend your observability services

We recommend that you review [Grailï»¿](https://docs.dynatrace.com/docs/shortlink/grail). It's a database designed explicitly for observability data. It acts as a single unified storage solution for logs, metrics, traces, events, and more. All data stored in Grail is interconnected within a real-time model that reflects the topology and dependencies within a monitored environment. Plan how to apply the following capabilities:

* [Log Management and Analyticsï»¿](https://docs.dynatrace.com/docs/shortlink/log-management-and-analytics)
* [Business Observabilityï»¿](https://docs.dynatrace.com/docs/shortlink/business-observability-hub)

## Step 3 - Optimize

Main objectives of this step:

* Review and optimize your internal processes
* Decommission your old Managed infrastructure

### Review and optimize your internal processes

Moving from Dynatrace Managed to SaaS reduces the burden of infrastructure maintenance for organizations, however, this also necessitates adjusted operational procedures. Review and synchronize organizational operational procedures about the Dynatrace release schedules, notifications, and high availability.

### Scale-In Dynatrace Managed

Once all monitoring sources have been migrated to the SaaS platform, the remaining Dynatrace Managed components may be decommissioned.

The following types of Dynatrace components may be left over from your Dynatrace Managed deployment:

#### Decommission ActiveGates

The general recommendation for an upgrade is to deploy new ActiveGates for the new Dynatrace SaaS environment and later decommission unused ActiveGates once the upgrade is complete.

#### Decommission Dynatrace Managed cluster nodes

Cluster Nodes provide the compute capacity and data storage for Dynatrace Managed. These nodes can be maintained temporarily to access legacy Managed data and configuration. Once they are no longer required, these should be decommissioned. For more information regarding the parallel operation of Dynatrace Managed and SaaS, please contact your Dynatrace Sales team.

We recommend creating a Dynatrace Managed infrastructure decommissioning plan. As an example, we provide you with a sample plan aligned to hypothetical requirements:

* At the start, the Dynatrace Managed cluster was sized with 12 nodes
* Monitored traffic is continuously switched to the target SaaS environment for the whole upgrade duration
* Halfway, the Dynatrace Managed cluster is scaled-in to half of the initial size
* We keep 3 nodes to ensure high availability during the validation phase
* We keep 1 cluster node to comply with our data retention policy. After it ends, we decommission the cluster completely.

![Dynatrace Managed infrastructure decommissioning plan](https://dt-cdn.net/images/managed-decomissioning-plan-3064-efaffd379b.png)

Dynatrace Managed infrastructure decommissioning plan

Questions?

Visit the [Upgrade to SaaS forumï»¿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.