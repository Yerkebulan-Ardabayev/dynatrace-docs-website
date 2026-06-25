---
title: Cluster event notifications
source: https://docs.dynatrace.com/managed/managed-cluster/configuration/cluster-event-notifications
scraped: 2026-05-12T11:53:00.554794
---

# Cluster event notifications

# Cluster event notifications

* Updated on Oct 07, 2025

You can manage the following notifications in a Dynatrace Managed cluster:

* **Insufficient disk space on a cluster node**  
  Triggered when a disk partition on a cluster node has less disk space than required for a given storage type. In that case, you need to extend your disk or review cluster settings. Otherwise, data retention might be reduced.
* **Insufficient hardware on a cluster node**  
  Triggered when a cluster node doesn't have enough CPU cores and RAM to meet recommended requirements. For details, see [Hardware requirements](/managed/managed-cluster/installation/managed-hardware-requirements "Review the hardware sizing, storage, and multi-node cluster requirements before installing Dynatrace Managed on your infrastructure.").
* **Metrics storage exceeds supported size (4TiB)**  
  Triggered when metrics storage for a cluster node is too high. In that case, you need to review your monitoring settings or add additional nodes to the cluster.
* **Transaction storage retention period truncation**  
  Triggered when data retention has been automatically reduced to store new data. In that case, we recommend that you adjust the target retention time, review monitoring settings, or extend a disk.
* **Adaptive Load Reduction activity**  
  Triggered when a cluster node is considered overloaded and unable to keep up with processing incoming requests. In that case, you need to review monitoring settings or increase CPU cores and RAM on the cluster node. For details, see [Adaptive Traffic Management for Dynatrace Managed](/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed#alr "Improve your Dynatrace Managed environment health and performance with the adaptive features of traffic management, load reduction, and capture control.").
  To configure cluster event notifications settings

In order to interact with the [Cluster API v2](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2.") and manage cluster event notifications, follow the procedure below:

* [Authentication](#authentication-token-authentication)
* [Configure email notifications](#configure-email-notifications-config-emails)
* [Read configuration schema](#read-configuration-schema-read-config-schema)
* [Read current configuration](#read-current-configuration-read-current-config)
* [Create notification settings object](#create-notification-settings-object-create-settings-object)
* [Update notification settings](#update-notification-settings-update-settings-object)
* [Delete notification settings](#delete-notification-settings-delete-settings-object)
* [Cluster events and email notifications](#cluster-events-and-email-notifications-cluster-notifications-reference)

## Authentication

To generate a cluster token with the **Write settings** and **Read settings** scopes

1. Go to **Settings** > **API tokens**.
2. In the **Cluster tokens** section, select **Generate token**.
3. Enter a name for your token and define the **Write settings** and **Read settings** access scopes of your cluster API token.
4. **Save** and then **Copy** the token to a secure location.

## Configure email notifications

To send your configuration as a JSON payload, use the [POST an object](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint with a cluster token that has the appropriate [access scopes](#token-authentication):

```
[



{



"schemaId": "builtin:cluster-events-notification-settings",



"scope": "cluster",



"value": {



"insufficientDiskSpace": {



"sendEmail": true



},



"insufficientHardware": {



"sendEmail": true



},



"insufficientMetricStorage": {



"sendEmail": false



},



"transactionStorageTruncation": {



"sendEmail": false



},



"adaptiveLoadReductionActivated": {



"sendEmail": false



}



}



}



]
```

## Read configuration schema

To learn the JSON format required to post your configuration, use the [GET a schema](/managed/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") endpoint with a cluster token that has the appropriate [access scopes](#token-authentication). The configuration schema identifier (`schemaId`) is `builtin:cluster-events-notification-settings`.

Response schema details

```
{



"dynatrace": "1",



"schemaId": "builtin:cluster-events-notification-settings",



"displayName": "Cluster events notification settings",



"description": "Configuration of emails notifications for cluster events.",



"documentation": "Email notifications are sent to recipients defined in Settings - Emails - Email notifications.",



"version": "0",



"multiObject": false,



"maxObjects": 1,



"allowedScopes": [



"cluster"



],



"enums": {},



"types": {



"SingleEventSettings": {



"version": "0",



"versionInfo": "",



"displayName": "Single event settings",



"summaryPattern": "",



"description": "Settings for a single cluster event",



"documentation": "",



"properties": {



"sendEmail": {



"displayName": "Send email",



"description": "",



"documentation": "",



"type": "boolean",



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT",



"default": true



}



},



"type": "object"



}



},



"properties": {



"insufficientDiskSpace": {



"displayName": "Insufficient disk space on a cluster node",



"description": "Triggered when a disk partition on a cluster node has less disk space than required for a given storage type. In that case, you need to extend your disk or review cluster settings. Otherwise, data retention might be reduced.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"insufficientHardware": {



"displayName": "Insufficient hardware on a cluster node",



"description": "Triggered when a cluster node doesn't have enough CPU cores and RAM to meet recommended requirements.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"insufficientMetricStorage": {



"displayName": "Metrics storage exceeds supported size (4TiB)",



"description": "Triggered when Metrics storage a cluster node is too high. In that case, you need to review your monitoring settings or add additional nodes to the cluster.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"transactionStorageTruncation": {



"displayName": "Transaction storage retention period truncation",



"description": "Triggered when data retention has been automatically reduced to store new data. In that case, it is recommended to adjust target retention time, review monitoring settings or extend a disk.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



},



"adaptiveLoadReductionActivated": {



"displayName": "Adaptive Load Reduction activity",



"description": "Triggered when a cluster node has been considered as overloaded and not able to keep up with processing incoming requests. In that case, you need to review monitoring settings or increase CPU cores and RAM on the cluster node.",



"documentation": "",



"type": {



"$ref": "#/types/SingleEventSettings"



},



"nullable": false,



"maxObjects": 1,



"modificationPolicy": "DEFAULT"



}



}



}
```

## Read current configuration

To check the current configuration, use the [GET objects](/managed/dynatrace-api/environment-api/settings/objects/get-objects "View multiple settings objects via the Dynatrace API.") endpoint (`/api/cluster/v2/settings/objects?schemaIds=builtin:cluster-events-notification-settings&scopes=cluster`) with a cluster token that has the appropriate [access scopes](#token-authentication).

* If these settings have been previously changed, the items list contains a single object. Use the `objectId` from the list in making subsequent updates.
* If the items list is empty, the default value is used (not visible in Dynatrace API):

  ```
  {



  "value": {



  "insufficientDiskSpace": {



  "sendEmail": true



  },



  "insufficientHardware": {



  "sendEmail": true



  },



  "insufficientMetricStorage": {



  "sendEmail": true



  },



  "transactionStorageTruncation": {



  "sendEmail": false



  },



  "adaptiveLoadReductionActivated": {



  "sendEmail": false



  }



  }



  }
  ```

## Create notification settings object

To create a cluster event notification settings object, use the [POST objects](/managed/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") endpoint with a cluster token that has the appropriate [access scopes](#token-authentication). Use the ID of the newly created object (event notification settings) for later notification settings updates.

Example of creating notification settings object

In this example, using a `POST` API call to the `/api/cluster/v2/settings/objects` endpoint and `builtin:cluster-events-notification-settings` schema, you create a notification settings object in your cluster settings:

```
[



{



"schemaId": "builtin:cluster-events-notification-settings",



"scope": "cluster",



"value": {



"insufficientDiskSpace": {



"sendEmail": true



},



"insufficientHardware": {



"sendEmail": true



},



"insufficientMetricStorage": {



"sendEmail": false



},



"transactionStorageTruncation": {



"sendEmail": false



},



"adaptiveLoadReductionActivated": {



"sendEmail": false



}



}



}



]
```

## Update notification settings

There are two methods you can use to update cluster events notification settings once the notification settings object is created. In either case, make sure you have a cluster token that has the appropriate [access scopes](#token-authentication).

* You can use the same `POST` method that you used to create the settings object ([Create notification settings object](#create-settings-object)). The schema doesn't allow duplicate settings objects, so if you attempt to create another settings object, you will overwrite the existing one.
* You can modify an existing settings object by making a `PUT` API call to the `/api/cluster/v2/settings/objects/<objectId>` endpoint and providing the `objectId` obtained when creating the initial event notification settings object.

  Example of updating the event notification settings object

  Make the `PUT` API call to the `/api/cluster/v2/settings/objects/<objectId>`

  ```
  {



  "value": {



  "insufficientDiskSpace": {



  "sendEmail": true



  },



  "insufficientHardware": {



  "sendEmail": true



  },



  "insufficientMetricStorage": {



  "sendEmail": false



  },



  "transactionStorageTruncation": {



  "sendEmail": false



  },



  "adaptiveLoadReductionActivated": {



  "sendEmail": false



  }



  }



  }
  ```

## Delete notification settings

You can delete an existing notification settings object by making a [`DELETE`](/managed/dynatrace-api/environment-api/settings/objects/del-object "Delete a settings object via the Dynatrace API.") API call to the `/api/cluster/v2/settings/objects/<objectId>` endpoint (with a cluster token that has the appropriate [access scopes](#token-authentication)) and providing the `objectId` obtained when creating the initial event notification settings object. After the object is deleted, notification behavior falls back to the default: all notifications trigger an email to configured recipients.

## Cluster events and email notifications

Below, you can find a table describing the cluster event types, their associated severity levels, and whether notifications are triggeredâeither via email or directly to Mission Control.

| Type | Severity | Summary | Email notification | MC notification |
| --- | --- | --- | --- | --- |
| `ACTIVE_GATE_TOKENS` | WARNING | "ActiveGate Token(s) will expire soon." | Yes | No |
| `CASSANDRA` | WARNING | "Cassandra node connection lost (`%d` times in the last hour)." | No | Yes |
|  | WARNING / INFO | "Cassandra node connection `ADDED/LOST/REACTIVATED`, host ." | No | Yes |
|  | INFO | "Cassandra node connection added (`%d` times in the last hour)." | No | Yes |
|  | INFO | "Cassandra node connection reestablished (`%d` times in the last hour)." | No | Yes |
| `CLUSTER_LIFECYCLE` | SEVERE | "License `'%s'` will expire within one day." | Yes | Yes |
|  | SEVERE | "License `'%s'` has expired." | Yes | Yes |
|  | SEVERE | "Your Dynatrace Managed cluster node `{0}` is undersized!" | Configurable [1](#fn-1-1-def) | Yes |
|  | SEVERE | "Storage volume for Dynatrace Managed log files is running out of space on `{0}`." | Yes | Yes |
|  | SEVERE | "Your Dynatrace Managed cluster should be scaled-out!" | Yes | Yes |
|  | SEVERE | "Could not detect `%s` activity on `%s%s`." | No | Yes |
|  | SEVERE | "Insufficient system privileges on `%s`." | No | Yes |
|  | SEVERE | "Update your Cluster `ActiveGate{0}` immediately. You're using `{1}` `ActiveGate{0}` that `{2}` no longer supported!" | Yes | Yes |
|  | SEVERE | "Post-Update data migration failed, please contact Dynatrace Support." | No | Yes |
|  | SEVERE | "Dynatrace update `%s` download failed." | No | Yes |
|  | SEVERE | "Cassandra backup problem." | No | Yes |
|  | SEVERE | "Dynatrace Managed has stopped collecting monitored dataâ¦" | No | Yes |
|  | SEVERE | "SSL certificate expired." | No | Yes |
|  | SEVERE | "License `'%s'` is inactive. Until it is done, you cannot set up any monitoring. Activate your license on Licensing page." | No | Yes |
|  | SEVERE | "Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security." | No | Yes |
|  | SEVERE | "Failed to import metadata file `%s`." | No | Yes |
|  | SEVERE | "Default cluster features were changed for non-gov license." | No | Yes |
|  | SEVERE | âCluster traffic control: OneAgent monitoring was disabled on recently connected hosts to avoid cluster overload." | No | Yes |
|  | WARNING / SEVERE | "Host is down." | Yes | Yes |
|  | WARNING / SEVERE | "ElasticSearch backup problem." | No | Yes |
|  | WARNING / SEVERE | "Cluster `'%s'` (`'%s'`) update failed." | No | Yes |
|  | WARNING | "WebUI nodes settings change failed." | No | Yes |
|  | WARNING | "LDAP connection error." | Yes | Yes |
|  | WARNING | "Upcoming update to version `%s` is suspended for the cluster `'%s'` (`'%s'`)." | Yes | Yes |
|  | WARNING | "Node is down - `%s`." | Yes, if happened outside of the upgrade procedure | Yes |
|  | WARNING | âThere is lack of connection to Dynatrace Mission Control." | Yes | Yes |
|  | WARNING | "Backup has been disabled because the configuration is no longer supported." | Yes | Yes |
|  | WARNING | "Fetching OAuth client credentials failed with status code `{0}`." | No | Yes |
|  | WARNING | "Cluster `'%s'` (`'%s'`) failed to determine update status." | No | Yes |
|  | WARNING | "Self monitoring download failed on cluster `'%s'`." | No | Yes |
|  | WARNING | "License check error." | No | Yes |
|  | WARNING | "SSL certificate (`%s`) refresh failed." | No | Yes |
|  | WARNING | "Login failed." | No | Yes |
|  | WARNING | "Not all tenants from MultiTenant-ActiveGate `%s` are configured with AuthTokens." | No | Yes |
|  | WARNING | "Let's Encrypt SSL certificate fetching failure." | No | Yes |
|  | WARNING | "Your SSL certificate will expire soon." | No | Yes |
|  | WARNING | "Login failed." | No | Yes |
|  | WARNING | "User welcome e-mail was not sent." | No | Yes |
|  | WARNING | "The Snyk vulnerability feed import failed." | No | Yes |
|  | WARNING | "The NVD CVE vulnerability feed import failed." | No | Yes |
|  | WARNING | âLDAP connection problems.â | No | Yes |
|  | WARNING / INFO | "Oidc signature check." | No | Yes |
|  | WARNING / INFO | "Billing archive has been successfully downloaded/downloaded with warning/failed." | No | Yes |
|  | INFO | "WebUI nodes settings changed successfully." | No | Yes |
|  | INFO | "Scheduled update has been resumed for the cluster `'%s'` (`'%s'`)." | Yes | Yes |
|  | INFO | "Hardware recommendation are fulfilled on `{0}`." | Configurable [1](#fn-1-1-def) | Yes |
|  | INFO | "Storage space for Dynatrace Managed log files is sufficient on `{0}`." | Yes | Yes |
|  | INFO | "Cluster meets the minimum requirement for the number of nodes." | Yes | Yes |
|  | INFO | "Node is up - `%s`." | Yes | Yes |
|  | INFO | "Host is up." | Yes | Yes |
|  | INFO | "Connection to Dynatrace Mission Control is back again." | Yes | Yes |
|  | INFO | "`<processName>` is up on `<hostName>`." | No | Yes |
|  | INFO | "Node was restored on ." | No | Yes |
|  | INFO | "Dynatrace update `%s` was successfully downloaded." | No | Yes |
|  | INFO | "Cluster `'%s'` (`'%s'`) started updating." | No | Yes |
|  | INFO | "Cluster update download finished." | No | Yes |
|  | INFO | "Cluster `'%s'` update to version `%s` finished." | No | Yes |
|  | INFO | "Request for remote access." | No | Yes |
|  | INFO | "Successful login to DebugUI." | No | Yes |
|  | INFO | "SSL certificate (`%s`) refresh succeeded." | No | Yes |
|  | INFO | "Let's Encrypt SSL certificate fetching succeeded." | No | Yes |
|  | INFO | "Cluster `'%s'` configuration database initialized successfully." | No | Yes |
|  | INFO | "Server `%d` joined cluster `'%s'` (`'%s'`)." | No | Yes |
|  | INFO | "Server `%d` left cluster `'%s'` (`'%s'`)." | No | Yes |
|  | INFO | "Server `%d` joined cluster `'%s'` (`'%s'`) `%d` times last hour." | No | Yes |
|  | INFO | "Server `%d` left cluster `'%s'` (`'%s'`) `%d` times last hour." | No | Yes |
|  | INFO | "Successful login." | No | Yes |
|  | INFO | "The third-party vulnerability feeds version `%s` were successfully imported into the cluster's Dynatrace Application Security." | No | Yes |
|  | INFO | "Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security." | No | Yes |
| `CLUSTER_RUNTIME_SETTING` | SEVERE | "Responsibility cluster nodes override set on node: `%d`." | No | Yes |
| `CONFIGURATION_AUDIT` | INFO | "Min Agent Version updated to `%d` by Session Replay." | No | Yes |
|  | INFO | "Session State Version updated to `v%d` by Session Replay." | No | Yes |
| `ELASTICSEARCH` | INFO | "Elasticsearch storage service on your Dynatrace Managed cluster might be overloaded!" | No | Yes |
| `ERROR` | WARNING | "ElasticSearch update transient settings failed." | No | Yes |
|  | INFO | "ElasticSearch update transient settings succeeded." | No | Yes |
| `LOG_EVENT_DROP` | WARNING | "Ingested log data is trimmed." | No | Yes |
|  | WARNING | "Log ingest queue is full." | No | Yes |
|  | WARNING | "Elasticsearch log queue is full." | No | Yes |
|  | WARNING | "Elasticsearch log storing failed." | No | Yes |
| `MANAGED_INTERNAL` | INFO | "Internal: Cassandra has old files." | No | Yes |
| `MANAGED_NODE_ADD` | WARNING | "Adding new node is taking more than expected." | No | Yes |
|  | INFO | "Adding new node operation has been started." | No | Yes |
|  | INFO | "Adding new node precondition check status." | No | Yes |
|  | INFO | "Adding new node finished successfully." | No | Yes |
|  | WARNING | "Adding new node failure." | No | Yes |
| `MANAGED_NODE_REMOVAL` | WARNING | "Node removal finished with error `%s` (id=`%d`)." | No | Yes |
|  | INFO | "Node removal operation is not allowed `%s` (id=`%d`)." | No | Yes |
|  | INFO | "Node removal process started successfully `%s` (id=`%d`)." | No | Yes |
|  | INFO | "Node removal process started successfully `%s`." | No | Yes |
|  | INFO | "Node removal finished successfully." | No | Yes |
|  | INFO | "Node removal failure." | No | Yes |
| `SECURITY_GATEWAY_LIFECYCLE` | INFO | "ActiveGate (host=`%s`) registered on cluster." | No | Yes |
|  | INFO | "ActiveGate (host=`%s`) unregistered on cluster." | No | Yes |
|  | INFO | "ActiveGate (host=`%s`) lost connection to cluster." | No | Yes |
|  | INFO | "ActiveGate (environment=`%s`, host=`%s`) registered on cluster." | No | Yes |
|  | INFO | "ActiveGate (environment=`%s`, host=`%s`) unregistered on cluster." | No | Yes |
|  | INFO | "ActiveGate (environment=`%s`, host=`%s`) lost connection to cluster." | No | Yes |
| `SERVER_LIFECYCLE` | SEVERE | "Transaction storage retention period truncated." | Configurable [1](#fn-1-1-def) | Yes |
|  | SEVERE | "Insufficient disk space on `%s` on `%s`." | Configurable [1](#fn-1-1-def) | Yes |
|  | SEVERE | "Long-term Metrics Store size exceeds the maximum acceptable 4 TB on `%s`." | Configurable [1](#fn-1-1-def) | Yes |
|  | SEVERE | "`<component name>` is down." | No | Yes |
|  | SEVERE | "Heap memory: Server `%d` started memory emergency mode." | No | Yes |
|  | SEVERE | "Heap memory: Server `%d` triggered a hard memory cleanup action." | No | Yes |
|  | SEVERE | "A cluster node can't receive OneAgent traffic." | No | Yes |
|  | WARNING | "Server `%d` activated Adaptive Load Reduction." | Configurable [1](#fn-1-1-def) | Yes |
|  | WARNING | "Long-term Metrics Store size exceeds recommended 2 TB on `%s`." | No | Yes |
|  | WARNING | "Node cannot read and write to directory: `'%s'`." | No | Yes |
|  | WARNING | "Heap memory: Server `%d` triggered a soft memory cleanup action." | No | Yes |
|  | WARNING / INFO | "Disabling OneAgent traffic at " | No | Yes |
|  | WARNING / INFO | "Enabling OneAgent traffic at " | No | Yes |
|  | INFO | "Failed to import the third-party vulnerability feeds version `%s` into the cluster's Dynatrace Application Security." | Configurable [1](#fn-1-1-def) | Yes |
|  | INFO | "Server `%d` deactivated Adaptive Load Reduction." | Configurable [1](#fn-1-1-def) | Yes |
|  | INFO | "Server `%d` shutdown initiated." | No | Yes |
|  | INFO | "`<component name>` is up." | No | Yes |
|  | INFO | "Server `%d` startup completed. (Version: `%s`)." | No | Yes |
|  | INFO | "Heap memory: Server `%d` ended memory emergency mode." | No | Yes |
|  | ? | "Server time of server `%d` is out of sync. Time difference `%d` milliseconds. Please enable NTP on all cluster nodes." | No | Yes |
| `TENANT_LIFECYCLE` | SEVERE | "Trial environment expired." | No | Yes |
|  | SEVERE | "The node with id `%s` is not properly configured." | No | Yes |
|  | SEVERE | "Environment `'%s'` with id `%s` failed to start on server `%d`. See server logs for details." | No | Yes |
|  | INFO | "Environment `'%s'` with id `%s` created." | No | Yes |
|  | INFO | "Environment `'%s'` with id `%s` updated." | No | Yes |
|  | INFO | "Environment `'%s'` with id `%s` removed." | No | Yes |

1

Configurable means that you can configure the notifications via Settings API. Setting id: `builtin:cluster-events-notification-settings`. In order to use this REST API, you need to authorize with settings-specific token with `settings.read` and `settings.write` permissions.