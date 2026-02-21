---
title: Ownership
source: https://www.dynatrace.com/docs/deliver/ownership-app
scraped: 2026-02-21T21:19:47.460483
---

# Ownership

# Ownership

* Latest Dynatrace
* App
* 7-min read
* Updated on Feb 10, 2025

Prerequisites

### Permissions

The following table describes the required permissions.

Additionally, you require the following primary permissions in Workflows (go to **Workflows** > **Settings** > **Authorization Settings**).

* `app-engine:apps:run`âEnables listing and running apps; provides basic access to the Launcher.
* `app-engine:functions:run`âEnables use of the function executor.

Alternatively, you can set up users with the [AppEngine user policyï»¿](https://www.dynatrace.com/news/blog/tailored-access-management-part-2-onboard-users-to-grail-and-appengine/).

Permission

Description

settings:objects:read

Read settings 2.0

settings:objects:write

Write settings 2.0 schemas

10

rows per page

Page

1

of 1

## Installation

Make sure the app is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

Get started

Use cases

![Ownership](https://dt-cdn.net/images/ownership-w-background-512-99cc966544.webp "Ownership") **Ownership** provides actions for building a workflow querying for an entity's ownership team and related contact information. With these actions, you can extract ownership data about an entity and integrate it with other apps, for example, to send Slack notifications or Jira updates to entity owners based on different triggers.

Furthermore, the ![Ownership](https://dt-cdn.net/images/ownership-w-background-512-99cc966544.webp "Ownership") **Ownership** enables you to import teams from the following sources using [automation workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services."):

* Groups from [Microsoft Entra ID](/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id "Set up Microsoft Entra ID Connector to automate importing teams from Microsoft Entra ID via Workflows.")
* Groups from [ServiceNow](/docs/analyze-explore-automate/workflows/actions/service-now "Automate creation of incidents in ServiceNow based on your monitoring data and events.")
* Any data source using JSON structure

See [Actions for Ownership](/docs/deliver/ownership-app/ownership-actions "Combine Ownership actions with other tasks and actions to create workflows for team import, notifications, task assignments, and other use cases.") for details.

![Retrieving the ownership team information from selected entities is handled by the "get_owners" workflow action.
One entity ID or a list of entity IDs can be used directly or via expression to use the result from previously executed workflow action to retrieve the ownership team information.
If contact details are set within ownership teams settings, the returned information can be used with notification workflow actions, such as Slack, MS Teams, E-Mail, or JIRA.](https://dt-cdn.net/hub/img_getOwners_workflow_5dy7rv6.png)![The import_teams workflow action simplifies the import and auto-sync of external ownership team data.
It supports ownership team information in a JSON format and complies with the ownership schema.
Additionally, it automatically accepts information retrieved from 3rd party tools such as ServiceNow and Microsoft Entra ID (formerly Azure Active Directory).](https://dt-cdn.net/hub/img_importTeams_workflow_6d1QAAy.png)![Web-UI view example: Associated Ownership Teams with a selected entity](https://dt-cdn.net/hub/ownershipInContext_2.png)![Ownership teams management UI within Settings: List of created Ownership-Teams in Settings with the possibility to create, edit, and delete ownership teams and their attributes.](https://dt-cdn.net/hub/img_ownershipSettings_vZ6SsxZ.png)

1 of 4Retrieving the ownership team information from selected entities is handled by the "get\_owners" workflow action.
One entity ID or a list of entity IDs can be used directly or via expression to use the result from previously executed workflow action to retrieve the ownership team information.
If contact details are set within ownership teams settings, the returned information can be used with notification workflow actions, such as Slack, MS Teams, E-Mail, or JIRA.

* Providing contact information at the entity level to enhance automated remediation actions, such as targeted notifications via, for example, Workflows
* Enabling team and dependency transparency
* Reducing mean time to recovery (MTTR) to automatically inform the right teams about new incidents.
* Automatically import and store ownership-team information to keep the information always in sync and up-to-date.

## Related topics

* [Actions for Ownership](/docs/deliver/ownership-app/ownership-actions "Combine Ownership actions with other tasks and actions to create workflows for team import, notifications, task assignments, and other use cases.")
* [Workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.")