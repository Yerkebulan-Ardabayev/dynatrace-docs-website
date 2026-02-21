---
title: Create and manage teams for entity ownership
source: https://www.dynatrace.com/docs/deliver/ownership/ownership-teams
scraped: 2026-02-21T21:27:18.451744
---

# Create and manage teams for entity ownership

# Create and manage teams for entity ownership

* How-to guide
* 8-min read
* Updated on Nov 07, 2023

Ownership for monitored entities is defined within **teams**. You can set up ownership teams in the web UI, via API, and using [Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform."). Each team has a **unique identifier** that is the basis for [applying ownership to entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") by different methods (Kubernetes labels and annotations, host metadata, environment variables, or tags). Additionally, team definitions consist of names, descriptions, important routing information for notifications (via Microsoft Teams, Slack, Jira, and email), responsibilities (such as operations or security), and additional helpful links.

Team settings are based on the [Settings 2.0 framework](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework"), which defines each team configuration as a settings object based on the ownership schema, whether you use API, Configuration as Code, imported data from third-party databases, or the web UI at **Settings** > **Ownership**.

Ownership information attached to monitored entities aids in mapping your Dynatrace environment to the right teams for collaboration, issue resolution, and vulnerability escalation.

## Permissions

You need **any** of the following permissions to create, edit, or delete a team via API.

* The `settings.write` [token permission](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")
* The [IAM policy](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") `ALLOW settings:objects:write, settings:schemas:read WHERE settings:schemaId = "builtin:ownership.teams";`

You need the **Manage monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the environment or management-zone level to create teams via the web UI.

## Create a team via web UI

To create a team via the Dynatrace web UI

1. Go to **Settings** > **Ownership** > **Teams**.

   ![Ownership teams settings page](https://dt-cdn.net/images/ownership-teams-page-2212-be3abe3c7d.png)
2. Select **Add team**.
3. Required Start by providing a **Team name**.

In ownership team data [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), the `displayName` import parameter from `get_groups` is set as the **Team name**.

4. Required The **Team identifier** is auto-populated based on the team name. Use the default identifier or provide your own.

   **Requirements**

   Team identifiers are the basis of [applying ownership to entities](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags."), regardless of the method. Main team identifiers must be unique across your environment. However, you may reuse the identifier of a previously deleted team.

   * Identifiers must be unique; no two main team identifiers can be the same.
   * Identifiers must be between 1 and 100 characters long.
   * They must begin and end with a letter (`[a-zA-Z]`).
   * They can contain hyphens (`-`), underscores (`_`), and alphanumerics between the opening and closing characters. Blank spaces and other special characters are not supported.
   * Once created, a main **team identifier cannot be edited or changed**.

   In team information [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), this field is set to the corresponding group's **Object Id** in Entra ID and cannot be edited. The **External ID** of the imported ownership team in Dynatrace is also set to this value.
5. Add a **Description** that aids in differentiating the team, for example, by entities managed or by responsibility. This description is appended to the team name for display on the **Ownership teams** page.
6. Optionally, specify **Supplementary identifiers**. Select **Add supplementary identifier** to provide up to three additional identifiers, for example, to identify sub-teams. When assigning ownership to entities, you can use the main team identifier or any of the supplementary identifiers to assign an entity to the named team.

   * Supplementary identifiers must meet the same character requirements as the main team ID.
   * A supplementary identifier cannot be the same as the main identifier of the same team.
   * Within a team, supplementary identifiers must be unique.
   * A supplementary identifier can be the same as the main or supplementary identifier of another team.
   * Unlike the main team identifier, supplementary identifiers **may be edited and deleted**.

   In ownership team data [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), the `mailNickname` import parameter from `get_groups` is set as a unique, human-readable **Supplementary Identifier**.
7. Select all **Responsibilities** that apply to the team. Although optional, these toggles provide critical metadata at a glance and help you specify the appropriate contact details.

   * **Development**âTeams responsible for developing and maintaining the underlying software code
   * **Security**âTeams tasked with assessing the impact and priority of vulnerabilities and responding to them
   * **Operations**âTeams that deploy and manage software, with a focus on performance and availability
   * **Infrastructure**âTeams responsible for installing and maintaining IT hardware
   * **Line of business**âTeams responsible for meeting customer and business goals
8. Add all **Contact details** that apply to the team. You can provide specific routing information for targeted notifications via email, Jira, Microsoft Teams, and Slack.

   You can add as many entries as required. Create a separate entry for each email address, Slack channel, Microsoft team, or Jira project you want to add.

   1. Select **Add contact information**.
   2. Select an **Integration type**.
   3. Provide details as follows:

      * **Email**âProvide a single **Email** address.
      * **Jira**âEnter the Jira **Project** name, **Default assignee** Required, and project **URL**.
      * **MS Teams**âProvide the **Team** name and **URL** (you can provide the link to a team channel from MS Teams).
      * **Slack**âProvide the **Channel** name and **URL**.
9. Provide any other **Links** describing the team or its responsibilities.
10. Select **Add link**.
11. Select the link **Type**, for example, **Documentation** or **Wiki**.
12. Provide the **URL**.

    You can add as many entries as required. Create a separate entry for each link you want to add.
13. Select **Add additional information** to provide additional key-value pairs in the **Name** and **Value** fields, for example, cost center names or organizational hierarchy information. You can also provide an optional **URL**.

    Keys for additional information:

    * Must be 1â100 characters long.
    * Can contain letters, numbers, special characters, and spaces.
14. Provide an **External ID** to be used only for automation purposes such as importing or updating team information. For example, use this field to store the unique ID assigned to a team in an external system such as Active Directory.

    * An external ID can only be specified during team creation.
    * Once created, an external ID **cannot be modified**.
    * This string can begin and end with and contain special characters, blank spaces, numbers, and letters.

    * External IDs cannot be used to apply ownership information to entities in key-value pairs; use the main team ID and supplementary IDs to assign entities to team owners.

    * In team information [imported from Microsoft Entra ID](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information."), this field is set to the corresponding group's **Object Id** from Entra ID and cannot be edited. The **Team identifier** of the imported ownership team is also set to this value.
15. **Save changes**.

See [Best practices for entity ownership](/docs/deliver/ownership/best-practices "Tips and best practices to ensure that entities have adequate ownership coverage") for more information about setting up teams optimally.

## Create a team via API and Configuration as Code

Team creation via the [**Settings API**](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") requires the ownership configuration [JSON schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") (`builtin:ownership.config`) provided by Dynatrace. You can retrieve the schema using the Settings API. Provide team configuration as a JSON payload.

[Configuration as Code](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") enables you to use JSON templates and YAML files for team creation for one or multiple teams at the same time.

## Import teams via Workflows Workflows

You can import user groups from **Microsoft Entra ID** and **ServiceNow** as ownership teams within Dynatrace.
Therefore, see how to use the [`import_teams`](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information.") action and workflows for importing teams.

## Manage teams

You can manage (create, delete, edit) ownership teams via **Settings** > **Ownership** > **Teams** as well as the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

The **Ownership teams** settings page lists all teams (and their descriptions) in your environment, whether created via web UI or the API. Use the **Filter** field  to narrow this list by any string in a team name or description.

You can **Delete** a team from this view and expand **Details** to view and edit team information. You cannot, however, edit or delete the main team identifier.

### Revision history

Select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") in the upper-right corner of the **Ownership teams** page and then select **Revision history** for details of changes, including team creation, modification and deletion. Revisions are listed with **Timestamp**, the **Source** of the change (**Web UI** or **API**), and the **User** making the change.

![History of ownership teams](https://dt-cdn.net/images/ownership-teams-revisions-1462-e55719add4.png)

Expand to view the **Details** of any revision. Changes are color coded to show the **Original value** and any **New value**. The image below shows a deleted supplementary identifier.

![Revision simple view](https://dt-cdn.net/images/ownership-teams-revision1-1849-055f7f5d2e.png)

**Switch to advanced mode** and select **Show diff** to view the same changes as JSON objects. The **Key** displayed in advanced mode is a unique setting ID assigned to each team. Select the key to view the corresponding team's details.

![Revision YAML view](https://dt-cdn.net/images/ownership-teams-revision2-1848-06b3770890.png)

You can also filter revision history for a specific teamâpaste any setting ID **Key** into the **Filter** field .

### Additional team management

There are additional conveniences for team-specific management within each team.

1. Expand team details on the **Ownership teams** page.
2. Select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") in the upper-right corner of team details to access team-specific [**Revision history**](#revision-history), helpful **API** snippets for team management, and the ability to **Duplicate** team details as the basis for creating a new team.

   ![Team-management links](https://dt-cdn.net/images/ownership-team-specific-links-1462-4d8ea5d2df.png)

The API snippets for reading, creating, updating, and deleting teams are available for both Windows and Linux command line interfaces. While API snippets are team specific, you can modify them, for example, by removing the team identifier to create a new team. Be sure to provide your access token.

![Team-management API snippets](https://dt-cdn.net/images/ownership-teams-api-snippets-763-e9a0f5eb88.png)

## Related topics

* [Dynatrace settings framework](/docs/manage/settings/settings-20 "Introduction to the Settings 2.0 framework")
* [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.")
* [Configuration as Code overview](/docs/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.")