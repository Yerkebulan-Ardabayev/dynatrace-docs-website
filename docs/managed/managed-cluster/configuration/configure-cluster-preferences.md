---
title: Cluster preferences
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/configure-cluster-preferences
scraped: 2026-05-12T11:36:49.300927
---

# Cluster preferences

# Cluster preferences

* Published Nov 16, 2022

All cluster preferences settings are turned on by default. Proper configuration of these settings depends on the unique needs of your organization. In addition to pro-active support settings, you'll also find settings related to new Community-user setup and domain name management. Please see below for details on the available controls.

To configure data privacy settings within your Managed environment, go to **Settings** > **Preferences**. You can also manage them using [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") and [Cluster API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1 "Find out about API for managing environments, network zones, synthetic locations, nodes, and tokens.").

You must have cluster administrator privileges to access the **Preferences** page.

## Pro-active support

### Dynatrace Managed Mission Control Support Services

Dynatrace Managed provides fully automated self-management capabilities that keep your system secure, reliable, and up-to-date. To achieve this, Dynatrace needs to send certain information to the Dynatrace Mission Control. You can adjust these settings by modifying below UI options.

* **Report usage and billing information**

  Each Dynatrace Managed cluster reports license-relevant consumption data such as number of host units, custom metrics or log monitoring for each environment. This setting is reflected by the **Report usage and billing information** UI label and cannot be changed to ensure proper billing and license verification of your deployment.
* **Report Dynatrace cluster health**

  Dynatrace clusters send status information, including cluster IDs, privacy flags, time zones, traffic levels, and maintenance windows. Server state, including number of CPU cores, CPU load, and used/free storage are reported on a per-cluster basis. This setting is reflected by the **Report Dynatrace cluster health** UI label and cannot be changed to ensure our support of your deployment.
* **Report cluster and OneAgent events to Dynatrace Mission Control**

  For each event, clusters send type, severity level, timestamp, and description detail so that Dynatrace product experts can remotely analyze and address problems or incompatibilities in your environment. When disabled, your organization is responsible for monitoring system events and collecting log files necessary for problem resolution prior to contacting Dynatrace product experts. This setting is controlled by the **Report cluster and OneAgent events to Dynatrace Managed Mission Control Support Services** UI option.
* **Dynatrace deployment health and user behavior monitoring**

  Dynatrace Managed installations include Dynatrace OneAgent, which provides self-monitoring of cluster health. Monitoring is enabled in Full-Stack Monitoring mode. In addition to infrastructure and Dynatrace service metrics, the following information is captured.

  + User information such as IP address
  + Geolocation of users
  + Browser or device type
  + User-action details within Dynatrace Managed such as clicks or page loads
  + Dynatrace Managed processes logs

  This setting is controlled by the **Dynatrace deployment health monitoring** UI option.

## Remote access

* Allow Dynatrace product experts remote access to environment monitoring settings.

  In the case of detected events, Dynatrace product experts can remotely check the monitoring settings of your cluster configuration. To configure this setting, go to **Settings** > **Remote access permissions** > **SMTP server**. This setting is controlled by the **Remote access permissions** - **Allow Dynatrace Support employees remote access to this cluster's monitoring settings** UI option.
* Allow Dynatrace product experts to change your configuration.

  When enabled, Dynatrace product experts can remotely optimize your environment's monitoring settings to ensure optimum performance and stability. This setting is controlled by the **Remote access permissions** - **Allow `option` Dynatrace employees who have appropriate permissions to access this cluster for purposes of pro-active support** UI option.

## Privacy

* Report information about monitored technologies and feature usage.

  Dynatrace proactively sends alerts for incompatibilities or technology-specific risks related to your environment. Dynatrace can report information about installed OneAgent versions, process technologies, hosts, ActiveGates, and other related entities and configurations. The retrieved information may be used for support and to improve Dynatrace offerings. Dynatrace may use this data (if aggregated and it can't be used to identify end users) for industry analyses, benchmarking, and analytics. Learn more about how Dynatrace [sends information about monitored technologies in your environment](/managed/managed-cluster/basics/mission-control-data-exchange "Review the data your Managed Cluster exchanges with Mission Control and the available opt-out options for each data category."). This setting is controlled by the **Send information about monitored technologies and feature usage** UI option.
* Use Mission Control as email notifications sender.

  Enable your own SMTP server to determine how Dynatrace delivers email notifications, reports, and other communications to users and administrators. To configure your own SMTP server, go to **Settings** > **Emails** > **SMTP server**. You can find more information on configuring your SMTP server in [Configure an SMTP server connection](/managed/managed-cluster/configuration/configure-smtp-server-connection "Learn how to configure an SMTP server connection and why this is recommended.").

## Dynatrace Community

The Dynatrace Community provides an Internet forum for customers and digital performance experts to connect with each other and share ideas. Registered users can ask questions and view answers in the [Dynatrace Communityï»¿](https://community.dynatrace.com/) and create support tickets. Before allowing your users access to the Dynatrace Community, please ensure that your users have a valid email address set.

To create a Dynatrace Community user account upon login

1. Log in as an admin to your Cluster Management Console.
2. Go to **Settings** > **Preferences**.
3. Enable **Send users invitation to create a Dynatrace account on first login**.

New and existing users of your cluster will receive an email with instructions on how to create a Dynatrace Community user account. New users will get the email after the first successful login to the cluster whereas existing users will get the email a few moments after you've enabled it.

This setting is controlled by the **Send users invitation to create a Dynatrace account on first login**. With an account, users will have access to the Dynatrace Community, Dynatrace University, and support tickets. For a better self-service support experience, we recommend turning this on. If you turn this off, you can still manually send users an invitation to create an account from each user's details page.

## Manage domain name & SSL certificates

### Domain name and SSL certificates management

This preference is controlled by **Enable management of domain name and SSL certificates** option.

Enable this setting to generate a domain name (a subdomain of `dynatrace-managed.com`) with a trusted certificate for your Dynatrace Managed cluster. All users in your environment can then access Dynatrace at `<prefix>.dynatrace-managed.com`. The Certificate Authority (CA) is [Let's Encryptï»¿](https://letsencrypt.org/). Certificates are downloaded by HTTPS (REST API) via Mission Control.

**Enable management of domain name and SSL certificates**

Note that this process may take a few minutes. Once complete, you'll be able to access the new URL. Disabling this option results in SSL certificates and the cluster URL being rolled back to the previous version. Remember to update your SSO IdP settings with this URL.

## Managing cluster preferences via REST API

To manage most cluster preferences, you can use the [Cluster API v1](/managed/dynatrace-api/cluster-api/cluster-api-v1 "Find out about API for managing environments, network zones, synthetic locations, nodes, and tokens."). To change the value of `Synchronize users' e-mail addresses, first and last name, and assigned permissions`, you need to use [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") and follow the procedure below.

* [Authentication](#token-authentication)
* [Configure synchronization of users and permissions](#config-users-and-permissions-sync)
* [Read configuration schema](#read-config-schema)
* [Read current configuration](#read-current-config)
* [Create cluster privacy settings object](#create-settings-object)
* [Update cluster privacy settings](#update-settings-object)
* [Delete cluster privacy settings](#delete-settings-object)

## Authentication

To generate a cluster token with the **Write settings** and **Read settings** scopes

1. Go to **Settings** > **API tokens**.
2. In the **Cluster tokens** section, select **Generate token**.
3. Enter a name for your token and define the **Write settings** and **Read settings** access scopes of your cluster API token.
4. **Save** and then **Copy** the token to a secure location.

## Configure synchronization of users and permissions

To send your configuration as a JSON payload, use the [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint with a cluster token that has the appropriate [access scopes](#token-authentication). An example below disables the synchronization:

```
[



{



"schemaId": "builtin:cluster-privacy-settings",



"scope": "cluster",



"value": {



"syncUsersAndPermissionsWithinSupportResources": false



}



}



]
```

## Read configuration schema

To learn the JSON format required to post your configuration, use the [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint with a cluster token that has the appropriate [access scopes](#token-authentication). The configuration schema identifier (`schemaId`) is `builtin:cluster-privacy-settings`.

Response schema details

```
{



{



"dynatrace": "1",



"schemaId": "builtin:cluster-privacy-settings",



"displayName": "Data exchange settings",



"description": "A Dynatrace Managed cluster exchange information with Dynatrace Mission Control, at least once, or periodically. You may want to opt-out of certain communications, such as allowing Dynatrace to proactively access your clusters and environments. However, some messages are mandatory and can't be switched off.",



"documentation": "Check data privacy and exchange in Dynatrace Managed deployments here: https://dt-url.net/5i035v7",



"version": "0",



"multiObject": false,



"maxObjects": 1,



"allowedScopes": [



"cluster"



],



"enums": {},



"types": {},



"properties": {



"syncUsersAndPermissionsWithinSupportResources": {



"displayName": "Synchronize users' email addresses, first and last names and assigned permissions within support resources with Mission Control",



"description": "Dispatched Dynatrace support resources will contain users' email addresses, first and last names, and assigned permissions.",



"documentation": "",



"type": "boolean",



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT",



"default": true



}



}



}
```

## Read current configuration

To check the current configuration, use the [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") endpoint (`/api/cluster/v2/settings/objects?schemaIds=builtin:cluster-privacy-settings&scopes=cluster`) with a cluster token that has the appropriate [access scopes](#token-authentication).

* If these settings have been previously changed, the items list contains a single object. Use the `objectId` from the list in making subsequent updates.
* If the items list is empty, the default value is used (not visible in Dynatrace API):

  ```
  {



  "value": {



  "syncUsersAndPermissionsWithinSupportResources": true



  }



  }
  ```

## Create cluster privacy settings object

To create a cluster privacy settings object, use the [POST objects](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint with a cluster token that has the appropriate [access scopes](#token-authentication). Use the ID of the newly created object for later settings updates.

Example of cluster privacy settings object

In this example, using a `POST` API call to the `/api/cluster/v2/settings/objects` endpoint and `builtin:cluster-privacy-settings` schema, you create a cluster privacy settings object in your cluster settings:

```
[



{



"schemaId": "builtin:cluster-privacy-settings",



"scope": "cluster",



"value": {



"syncUsersAndPermissionsWithinSupportResources": true



}



}



]
```

## Update cluster privacy settings

There are two methods you can use to update cluster privacy settings once the cluster privacy settings object is created. In either case, make sure you have a cluster token that has the appropriate [access scopes](#token-authentication).

* You can use the same `POST` method that you used to create the settings object ([Create cluster privacy settings object](#create-settings-object)). The schema doesn't allow duplicate settings objects, so if you attempt to create another settings object, you will overwrite the existing one.
* You can modify an existing settings object by making a `PUT` API call to the `/api/cluster/v2/settings/objects/<objectId>` endpoint and providing the `objectId` obtained when creating the initial cluster privacy settings object.

  Example of updating the cluster privacy settings object

  Make the `PUT` API call to the `/api/cluster/v2/settings/objects/<objectId>`

  ```
  {



  "value": {



  "syncUsersAndPermissionsWithinSupportResources": true



  }



  }
  ```

## Delete cluster privacy settings

You can delete an existing cluster privacy settings object by making a [`DELETE`](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") API call to the `/api/cluster/v2/settings/objects/<objectId>` endpoint (with a cluster token that has the appropriate [access scopes](#token-authentication)) and providing the `objectId` obtained when creating the initial cluster privacy settings object. After the object is deleted, cluster privacy behavior falls back to the default: synchronization of users and permissions is turned on.