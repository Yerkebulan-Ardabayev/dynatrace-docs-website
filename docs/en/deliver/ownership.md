---
title: Ownership Classic
source: https://www.dynatrace.com/docs/deliver/ownership
scraped: 2026-03-06T21:28:42.755901
---

# Ownership Classic


* Classic
* Overview
* 2-min read
* Updated on Nov 07, 2023

Assigning team owners to monitored entities in Dynatrace drives effective DevSecOps collaboration and swift, smart resolution of incidents and service degradations.

Ownership metadata attached to entities feeds your BizDevSecOps workflows, ensuring that the right people from among your security, operations, infrastructure, line of business, and development teams are brought together with the right information in context.

Knowledge about the ownership of an entity enables additional automation, such as:

* Notification of relevant teams of production issues that need their attention.
* Creation of IT service management tickets (for example, in Jira and ServiceNow) and assignment to the right teams.
* Assignment of vulnerabilities to the responsible team members.
* Provision of information to all relevant stakeholders.

You can create ownership information in the web UI, via API, and using Configuration as Code. You can also import ownership teams from third-party directory services (Microsoft Entra ID) via Workflows. For scalability and complete coverage, assign ownership as part of deployment metadata. You can also use the settings and entity web interfaces for these purposes.

1. Create and maintain ownership teams with unique IDs and associated contact information to make problem routing easier. See also Best practices for entity ownership.

   ![Ownership teams settings page](https://dt-cdn.net/images/ownership-teams-page-2212-be3abe3c7d.png)
2. Assign teams to Dynatrace-monitored entities via host metadata, Kubernetes labels and annotations, environment variables, and tags. See also Best practices for entity ownership.
3. View ownership information with routing details as part of Dynatrace entity details pages.

   ![Owner of a Kubernetes workload](https://dt-cdn.net/images/ownership-k8s-workload-2213-2217e57297.png)

### Basics

* Create and manage teams for entity ownership
* Assign ownership teams to monitored entities
* Best practices for entity ownership

### Additional

Define tags and metadata for hosts

Define your own process group metadata

Configuration as Code overview

Microsoft Entra ID Connector

### API

Settings API (retrieve schema and create teams)

Monitored entities - Custom tags API