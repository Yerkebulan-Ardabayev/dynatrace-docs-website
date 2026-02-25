---
title: Ownership Classic
source: https://www.dynatrace.com/docs/deliver/ownership
scraped: 2026-02-25T21:34:33.752818
---

# Ownership Classic

# Ownership Classic

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

You can [create ownership](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") information in the web UI, via API, and using [Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform."). You can also import ownership teams from third-party directory services ([Microsoft Entra ID](/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id "Set up Microsoft Entra ID Connector to automate importing teams from Microsoft Entra ID via Workflows.")) via [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."). For scalability and complete coverage, [assign ownership](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") as part of deployment metadata. You can also use the settings and entity web interfaces for these purposes.

1. [Create and maintain ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") with unique IDs and associated contact information to make problem routing easier. See also [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").

   ![Ownership teams settings page](https://dt-cdn.net/images/ownership-teams-page-2212-be3abe3c7d.png)
2. [Assign teams to Dynatrace-monitored entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") via host metadata, Kubernetes labels and annotations, environment variables, and tags. See also [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage").
3. View ownership information with routing details as part of Dynatrace entity details pages.

   ![Owner of a Kubernetes workload](https://dt-cdn.net/images/ownership-k8s-workload-2213-2217e57297.png)

### Basics

* [Create and manage teams for entity ownership](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.")
* [Assign ownership teams to monitored entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.")
* [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage")

### Additional

[Define tags and metadata for hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.")

[Define your own process group metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata "Configure your own process-related metadata based on the unique needs of your organization or environment.")

[Configuration as Code overview](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.")

[Microsoft Entra ID Connector](/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id "Set up Microsoft Entra ID Connector to automate importing teams from Microsoft Entra ID via Workflows.")

### API

[Settings API (retrieve schema and create teams)](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")

[Monitored entities - Custom tags API](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.")