---
title: Microsoft Entra ID Connector
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows/actions/microsoft-entra-id
scraped: 2026-02-18T05:44:10.939539
---

# Microsoft Entra ID Connector

# Microsoft Entra ID Connector

* Latest Dynatrace
* 5-min read
* Updated on Jun 18, 2025

Your Dynatrace environment can integrate with Microsoft Entra ID (formerly Azure Active Directory) in automation [workflows](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.").
Microsoft Entra ID Connector ![Azure Connector](https://dt-cdn.net/images/azure-for-workflows-lcgzeur-256-0e765fdb69.png "Azure Connector") enables you to use prebuilt actions in Workflows ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") to automate importing teams from Entra ID (based on various triggers) for defining entity ownership and other use cases in Dynatrace.
Microsoft Entra ID Connector connects to the Azure Cloud via the [Microsoft Graph APIï»¿](https://developer.microsoft.com/en-us/graph).

## Setup

1. Allow External Requests

External requests enable outbound network connections from your Dynatrace environment to external services. They allow you to control access to public endpoints from the AppEngine with app functions and functions in Dashboards, Notebooks, and Automations.

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** >  **General** > **External requests**.
2. Select  **New host pattern**.
3. Add the domain names.
4. Select **Add**.

This way you can granularly control the web services your functions can connect to.

You need to add these domain names `login.microsoftonline.com` and `graph.microsoft.com`.

2. Grant permissions to Workflows

Workflows requires some permissions to run actions on your behalf. Actions that come bundled with the Connector require other permissions.

To fine-tune permissions granted to Workflows

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and go to **Settings** > **Authorization settings**.
2. Select the following permissions besides the general Workflows permission.

   * `app-settings:objects:read`

For more on general Workflows user permissions, see [User permissions for workflows](/docs/analyze-explore-automate/workflows/security#user-permission "Guide on security aspects of workflow automation in Dynatrace Workflows").

3. Set up integration with Dynatrace

Configure your Microsoft Azure tenant to establish a connection with your Dynatrace environment.

1. Open `portal.azure.com` to access your Microsoft Azure tenant.
2. Navigate to **App registrations** to set up a new application.

   For the necessary setup steps, see [Register a client application in Azure Active Directoryï»¿](https://dt-url.net/3w239qt).
3. Grant your newly created Azure application the `Group.Read.All` permission.

   For more information, see [API Permissionsï»¿](https://dt-url.net/v8439p2) and [Introduction to permissions and consentï»¿](https://dt-url.net/7g639wa).
4. After registering the app, create a new client secret. For details, see [Certificates & secretsï»¿](https://dt-url.net/bt839gp).

   * To create a client secret, make sure that you either have admin permissions or are part of the app owners.
   * Make sure you store the client secret **Value** (not the **Secret ID**) after creation for establishing the connection to your Dynatrace environment later.

4. Authorize connection

Microsoft Entra ID Connector requires a client secret from Microsoft Azure for authorization.

1. Get the following credentials from your application registration in your Microsoft Azure tenant on `portal.azure.com`.

   * Directory (tenant) ID: Available in the **Overview** menu
   * Application (client) ID: Available in the **Overview** menu
   * Client secret: The **Value** (not the **Secret ID**) of the client secret from the preceding [Set up Microsoft Azure for integration with Dynatrace](#set-up-azure) section
2. Return to Dynatrace, go to **Settings** ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") > **Connections** > **Microsoft Entra ID**.
3. Select **Add item** and provide the following information.

   * **Connection name**: Needs to be unique. It will be listed and selectable in the connection field in Microsoft Entra ID Connector.
   * **Directory (tenant) ID**
   * **Application (client) ID**
   * **Type**: `Client secret`
   * **Client Secret**: This is the **Value** of the client secret from the [Set up Microsoft Azure for integration with Dynatrace](#set-up-azure) section.
4. Select **Create**.

#### Additional notes

* To add connection settings, you need the following permissions.

  ```
  ALLOW settings:objects:read, settings:objects:write, settings:schemas:read WHERE settings:schemaId = "app:dynatrace.azure.connector:microsoft-entra-identity-developer-connection"
  ```

  For details, see [Permissions and access](/docs/manage/settings/settings-20#permissions-and-access "Introduction to the Settings 2.0 framework").

## Get groups from Entra ID in automation workflows

1. Go to **Workflows** ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") and select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Workflow** in the upper-right corner of the page.
2. In the side panel, select the trigger best suited to your needs.
3. On the trigger node, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") to browse available actions.
4. In the **Choose action** side panel, search for **Microsoft Entra ID** and select **Get groups**.
5. In the action **Input**, you can target specific groups in **$filter** if you wish to filter your results. Likewise, in **$select**, specify which fields you wish to get from Entra ID. The syntax is based on [Entra ID API documentationï»¿](https://dt-url.net/azure-api-docs).

   Important for importing Entra ID groups as [ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership."):

   * You always need to include `id` and `displayName` in `$select`; these fields are mapped to the imported ownership team's **Team identifier** and **Team name**, respectively.
   * We recommend that you always include the `mailNickname` parameter in `get_groups`. This field has unique values in Entra ID and is set as a unique, human-readable **Supplementary Identifier** for your imported ownership team within Dynatrace.
   * The **Object Id** from Entra ID, imported via the `id` parameter, is set as the unique **Team identifier** as well as the **External ID** of the imported ownership team.
   * The `mail` parameter is set as the **Email** of the imported ownership team.

   ![Get groups input fields](https://dt-cdn.net/images/azure-connector-get-groups-input-698-0609c7d9dc.webp)
6. Optionally, insert the **Import teams** action (provided by the [Ownership app](/docs/deliver/ownership-app#import-teams "It provides custom actions to define workflows integrating entity owners and their contact information.") ![Ownership](https://dt-cdn.net/images/ownership-w-background-512-99cc966544.webp "Ownership")) to store Entra ID group information as [ownership teams](/docs/deliver/ownership/ownership-teams "Define teams with team identifiers, descriptions, responsibilities, and routing information for entity ownership.") within Dynatrace **Settings**. You can then [assign these imported teams as owners](/docs/deliver/ownership/assign-ownership "Assign owners to entities using entity metadata like labels, environment variables, and tags.") to any monitored entity in Dynatrace.
7. To test your workflow, select **Run**.

### Action result

The result of `get_groups` is a JSON array with each record consisting of a single user group. If **$count** is set to `true` when configuring the action, the **Results** panel shows a count of imported groups.

The `directory_id` displayed in the results is the Azure tenant ID.

The log of a successful run is shown below.

```
[INFO]    Successfully retrieved connection settings.



[INFO]    Successfully fetched authentication token.



[INFO]    Calling Entra-ID groups endpoint with the following query params: $filter=startswith(displayName, 'team-deco')&$select=id,displayName,description,mail,mailNickname&$count=true&$top=999



[INFO]    Successfully fetched Groups from Entra-ID.
```