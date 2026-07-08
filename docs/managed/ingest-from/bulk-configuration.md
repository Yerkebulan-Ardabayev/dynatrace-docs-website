---
title: Remote configuration management of OneAgents and ActiveGates
source: https://docs.dynatrace.com/managed/ingest-from/bulk-configuration
---

# Remote configuration management of OneAgents and ActiveGates

# Remote configuration management of OneAgents and ActiveGates

* How-to guide
* 9-min read
* Published May 31, 2022

Use remote configuration management to help you organize multiple OneAgents or ActiveGates with a single command instead of performing the same actions one by one (whether during installation, by editing configuration files, or by using the `oneagentctl` command-line tool).

When using remote configuration management, the action is still performed on the respective hosts, but you trigger it and control it centrally from **Deployment Status** in the Dynatrace web UI or via the Dynatrace API.

Before you start, review the [capabilities](#capabilities) and [limitations](#limitations) to make sure remote configuration management is suitable for your needs and your deployment.

## Capabilities

With remote configuration management, you can use a single command to carry out any of the following actions on multiple OneAgents or ActiveGates that meet the version requirements.

### OneAgent

| Action | Required Dynatrace version | Required OneAgent version |
| --- | --- | --- |
| [Host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") assignment | 1.252+ | 1.237+ |
| [Network zone](/managed/manage/network-zones/oneagent-connectivity "Find out how network zones prioritize ActiveGates for OneAgent connectivity.") assignment | 1.252+ | 1.237+ |
| [Tag](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#tags "Learn how to tag and set additional properties for a monitored host.") assignment | 1.268+ | 1.263+ |
| [Property](/managed/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts#host-metadata "Learn how to tag and set additional properties for a monitored host.") assignment | 1.268+ | 1.263+ |
| Communication settings assignment | 1.294+ | 1.285+ |

### ActiveGate

| Action | Required Dynatrace version | Required ActiveGate version |
| --- | --- | --- |
| [ActiveGate group](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#group "Learn which ActiveGate properties you can configure based on your needs and requirements.") assignment | 1.252+ | 1.237+ |
| [Network zone](/managed/manage/network-zones/activegate-connectivity "Find out how network zones prioritize ActiveGates for Environment ActiveGate connectivity.") assignment | 1.252+ | 1.237+ |

Remote configuration management works for OneAgents in Full-Stack and Infrastructure Monitoring mode and for host-based ActiveGates. OneAgent and ActiveGate must be communicating with your environment.

## Limitations

Remote configuration management does NOT work with:

* OneAgent deployed with Dynatrace Operator
* Application-only OneAgents
* OneAgents on Solaris
* Containerized ActiveGates

Communication settings assignment can be performed only via the web UI.

## Permissions

We recommend that you limit the number of users permitted to use remote configuration management. Multiple users performing configuration at the same time might not be aware of one another's actions. This applies to both the web UI and the API. The IAM permissions give you very granular control, so you can avoid having your users run into conflicts.

### IAM permissions

Users performing remote configuration management need to belong to a group bound to a policy with the following IAM permissions:

* `deployment:oneagents.network-zones:write`
* `deployment:oneagents.host-groups:write`
* `deployment:oneagents.host-tags:write`
* `deployment:oneagents.host-properties:write`

* `deployment:oneagents.communication-settings:write`

* `deployment:activegates.network-zones:write`
* `deployment:activegates.groups:write`

With IAM permissions, you can limit a user's activities down to a single configuration action, such as changing only the OneAgent host group assignment.

For more information on Dynatrace IAM permissions, see [Working with policies](/managed/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

### Access tokens

To make configuration changes using the Dynatrace API, you need an [access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") with the following scopes:

* **Write OneAgents** (`oneAgents.write`)—to validate the payload, generate a preview, and trigger a configuration change for OneAgents
* **Write ActiveGates** (`activeGates.write`)—to validate the payload, generate a preview, and trigger a configuration change for ActiveGates

### Cluster administrators

Communication settings assignment for OneAgent can be performed out of the box by the Dynatrace Managed cluster administrators.

## Web UI procedures

The Dynatrace web UI remote configuration workflow is similar for OneAgents and ActiveGates.

### Configure OneAgents

You can assign the following to multiple OneAgents:

* Host group
* Network zone
* Tags
* Properties

To update multiple OneAgents for any of the above

1. Go to **Deployment Status** > **OneAgents**.
2. Filter for and select the OneAgents you want to configure. You can use the select ![Checkbox](https://dt-cdn.net/images/box-bb39d78028.svg "Checkbox") box in the table header to select all filtered OneAgents or you can select OneAgents individually.

   After you select OneAgents, an edit pane appears at the bottom of the page.
3. Select the configuration change you want to perform.

   * modify host group
   * modify network zone
   * modify host tags
   * modify host properties
4. Select **Run action**.

   This starts the **Remote configuration management** wizard to carry out a configuration change on the selected OneAgents. It does not commit any changes until you select **Apply changes** and you confirm any required restarts. Before then, you will be able to change or cancel the action.
5. Specify the change you want to make to all the selected OneAgents. Depending on the action you selected, you can:

   * Add or remove the host group assignment
   * Add or remove the network zone assignment
   * Add or remove host tags
   * Add or remove host properties
6. Select **Next**.
7. Review your changes.
8. Select **Apply changes**.
9. Select **Continue** to start the bulk action.

   * OneAgents will be restarted to apply changes to network zone assignments, host group assignments, and Dynatrace version 1.308+ tags and properties.
   * If you change the host group assignment, you need to restart OneAgent-injected processes manually. Restarting the injected processes isn't necessary when changing the network zone assignment.
10. While the bulk action is being run, the status bar at the top of the **Deployment status** page informs you about the bulk action's progress. You can't start another bulk action until the current one is finished.

Changing network zones and host groups may require up to 10 minutes to take effect. Removing host properties and tags may require up to seven hours to take effect.

### Configure OneAgent communication settings

The cluster version of the target environment must be newer than or equal to the OneAgent version.

To update the communication settings of multiple OneAgents

1. Go to **Deployment Status** > **OneAgents**.
2. Filter for and select the OneAgents you want to configure. You can use the select ![Checkbox](https://dt-cdn.net/images/box-bb39d78028.svg "Checkbox") box in the table header to select all filtered OneAgents or you can select OneAgents individually.

   After you select OneAgents, an edit pane appears at the bottom of the page.
3. Select **modify communication settings**.
4. Select **Run action**.

   This starts the **Remote configuration management** wizard to carry out a configuration change on the selected OneAgents. It doesn't commit any changes until you select **Apply changes** and you confirm any required restarts. Before then, you'll be able to change or cancel the action.
5. Select **target environment**.
6. Specify a target environment URL.
7. Select **Next**.
8. Specify communication settings properties:

   * **Tenant token**
   * **Communication endpoints**
9. Select **Next**.
10. Run **Connection test**. You can review selected OneAgents versions, network zones, and ActiveGates they are using. After a connection test is started, the status for each OneAgent is shown in the table. You can proceed to the next step after the connection test is finished.Only those OneAgents that successfully tested the new connection settings can be updated.
11. Select **Next**.
12. Select **Apply changes**.
13. While the bulk action is being run, the status bar at the top of the **Deployment status** page informs you about the bulk action's progress. You can't start another bulk action until the current one is finished.

Updated OneAgents will restart automatically and be available in the target environment within up to 10 minutes. After reconfiguration, they will stop reporting to the source environment. However, it may take up to 10 minutes for them to be considered disconnected.

To re-enable full-stack monitoring for your monitored processes, you need to restart them manually.

### Configure ActiveGates

You can assign the following to multiple ActiveGates:

* ActiveGate group
* Network zone

To update multiple ActiveGates for either of the above

1. Go to **Deployment Status** > **ActiveGates**.
2. Filter for and select the ActiveGates you want to configure. You can use the select box ![Checkbox](https://dt-cdn.net/images/box-bb39d78028.svg "Checkbox") in the table header to select all filtered ActiveGates or you can select ActiveGates individually.
3. After you select ActiveGates, an edit pane appears at the bottom of the page.
4. Select the configuration change you want to perform.

   * modify ActiveGate group
   * modify network zone
5. Select the configuration you want to perform and then select **Run action**.

   This starts the **Remote configuration management** wizard to carry out a configuration change on the ActiveGates you have selected. It does not commit any changes until you select **Apply changes** and you confirm any required restarts. Before then, you will be able to change or cancel the action.
6. Specify the change you want to make to all the selected ActiveGates. Depending on the action you selected, you can:

   * Add or remove the ActiveGate group assignment
   * Add or remove the network zone assignment
7. Select **Next**.
8. Review your changes.
9. Select **Apply changes** to run the bulk action.
10. While the bulk action is being run, the bar at the top of the **Deployment status** page informs you about the bulk action's progress. Don't start another bulk action until the current one is finished. ActiveGate restart isn't necessary to apply changes.

Your changes may require up to 10 minutes to take effect.

## API procedures

The Dynatrace API has a set of endpoints that let you manage the configuration remotely in a safe and controlled manner.

See the [Remote configuration management API](/managed/dynatrace-api/environment-api/remote-configuration "Find out what the Remote configuration management API offers.") for more information.

### OneAgent configuration management example

The following is an example of how to assign multiple OneAgents to a host group using the Dynatrace API.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Filter OneAgents to configure**](/managed/ingest-from/bulk-configuration#step-1 "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create payload**](/managed/ingest-from/bulk-configuration#step-2 "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Validate payload**](/managed/ingest-from/bulk-configuration#step-3 "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Generate preview**](/managed/ingest-from/bulk-configuration#step-4 "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Run bulk configuration**](/managed/ingest-from/bulk-configuration#step-5 "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.")

### Step 1 Filter OneAgents to configure

Use the [OneAgent on a host API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") endpoint to specify the list of OneAgents for which you want to modify the host assignment.

You can use any of the available OneAgent properties as filtering criteria. For example, to list all OneAgents installed on Windows, issue the following request.

```
curl --request GET \



--url 'https://myenvironment.com/api/v2/oneagents?osType=WINDOWS \



--header 'Authorization: Api-Token <token>'
```

### Step 2 Create payload

The payload lists OneAgents for which you'll perform the bulk action and the details of the action itself. The example payload below will result in changing the host group assignment to `some-host-group` for the three listed OneAgents identified by their host IDs.

```
{



"entities": ["HOST-0000000000000001", "HOST-0000000000000002", "HOST-0000000000000003"],



"operations": [



{



"operation": "SET",



"attribute": "hostGroup",



"value": "some-host-group"



}



]



}
```

### Step 3 Validate payload

Before you run your configuration job, you can validate the payload you created by issuing the following request. In the example below, the payload is passed to the request as the `payload.json` file.

```
curl --request POST \



--url https://myenvironment.com/api/v2/oneagents/remoteConfigurationManagement/validator \



--header 'Authorization: Api-Token <token>' \



--header 'Content-Type: application/json' \



--data @payload.json
```

A valid payload returns the `HTTP 204` response. An invalid payload returns a response indicating details of the violation.

### Step 4 Generate preview

You can generate a preview before performing the actual configuration change. The preview provides information on how many entities are currently configured as described in the payload and how many will be configured this way when the reconfiguration request is sent.

The preview step is not supported for tags and properties.

To run a preview, issue the following request:

```
curl --request POST \



--url https://myenvironment.com/api/v2/oneagents/remoteConfigurationManagement/preview \



--header 'Authorization: Api-Token <token>' \



--header 'Content-Type: application/json' \



--data @payload.json
```

The response contains information on how many OneAgents are assigned to the host group and how many will be assigned to the host group after the configuration is complete.

```
{



"previews": [



{



"operation": "SET",



"attribute": "hostgroup",



"existingEntitiesCount": 3,



"targetEntitiesCount": 6



}



]



}
```

### Step 5 Run bulk configuration

To run the bulk configuration, issue the following request:

```
curl --request POST \



--url https://myenvironment.com/api/v2/oneagents/remoteConfigurationManagement \



--header 'Authorization: Api-Token <token>' \



--header 'Content-Type: application/json' \



--data @payload.json
```

A successful request returns the `HTTP 201` response. It means that the configuration job started. The change isn't applied instantly. Each OneAgent first performs the configuration on its own and then sends the information to your environment, and then the Dynatrace cluster updates the host group assignment. It may take up to 10 minutes for the change to be reflected in your environment.

You can validate the change by running the [OneAgent on a host API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") request filtered to the host group to which you just assigned your hosts.

```
curl --request GET \



--url 'https://myenvironment.com/api/v2/oneagents?hostGroupName=some-host-group \



--header 'Authorization: Api-Token <token>'
```

The response should contain the three host IDs you added to your configuration job.

### Configure OneAgent communication settings

The cluster version of the target environment must be newer than or equal to the OneAgent version.

To modify a host assignment for OneAgents

1. Execute an [API call](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.") to filter OneAgents for which you want to modify the host assignment.
2. Execute an [API call](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") to obtain the following target environment parameters:

   * tenantUUID
   * tenantToken
   * formattedCommunicationEndpoints
3. Execute the following [API call](/managed/dynatrace-api/environment-api/remote-configuration/oneagent/post-dry-run "Verify if hosts are able to communicate with a target environment.") to verify if the hosts are able to communicate with the target environment:

   Required token scope : `oneAgents.write`.

   ```
   POST https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/managedRemoteCommunicationSettings/dryRun



   accept: application/json; charset=utf-8



   Authorization: Api-Token <TOKEN>



   Content-Type: application/json



   {



   "additionalCommunicationAddresses": "<formattedCommunicationEndpoints>",



   "entities": [



   "<HOST-1>",



   "<HOST-2>"



   ],



   "environmentId": "<tenantUUID>",



   "proxy": "{optional proxy parameter}",



   "tenantToken": "<tenantToken>"



   }
   ```

   If `processedEntitiesCount` is less than `totalEntitiesCount`, execute the following API call to check the task status:

   ```
   GET https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/remoteConfigurationManagement/<task-id>



   Authorization: Api-Token <TOKEN>
   ```

   Repeat until it returns an error or `processedEntitiesCount` = `totalEntitiesCount`. The response format is the same as for the dry run. Required token scope: `oneAgents.read`.
4. Execute the following [API call](/managed/dynatrace-api/environment-api/remote-configuration/oneagent/execute-migration "Migrate hosts to a target environment.") to finalize migration:

   Execute the call if only the dry run was successful. Required token scope: `oneAgents.write`.

   ```
   POST https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/managedRemoteCommunicationSettings/execute



   accept: application/json; charset=utf-8



   Authorization: Api-Token <TOKEN>



   Content-Type: application/json



   {



   ... same payload like for dryRun



   }
   ```

   The response format is the same as for the dry run.

   Updated OneAgents will restart automatically and be available in the target environment within up to 10 minutes. After reconfiguration, they will stop reporting to the source environment. However, it may take up to 10 minutes for them to be considered disconnected.

   Execute the following API call to check the task status and make sure the migration is complete:

   ```
   GET https://<your-domain>/e/<your-environment-id>/api/v2/oneagents/remoteConfigurationManagement/<task-id>



   Authorization: Api-Token <TOKEN>
   ```