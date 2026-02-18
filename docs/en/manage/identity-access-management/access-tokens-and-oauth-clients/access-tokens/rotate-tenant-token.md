---
title: Tenant token classic
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token
scraped: 2026-02-18T05:54:57.934942
---

# Tenant token classic

# Tenant token classic

* 2-min read
* Published Feb 23, 2021

This article discusses access tokens used in previous Dynatrace to authenticate to classic Configuration and Environment APIs. For the latest Dynatrace access, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") and [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

The tenant token is used by OneAgents and ActiveGates to report data to Dynatrace. Dynatrace automatically generates the tenant token and adds it to OneAgent and ActiveGate installers on download.

## Access a tenant token

To obtain a tenant token for your environment, execute the [GET connectivity information for OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") request of the Deployment API. You will find the tenant token in the `tenantToken` field of the response body. You'll need your PaaS token to authenticate the request.

## Rotate tenant token

You can change the tenant token as needed (for example, to adhere to internal security policies or respond to unintended exposure). The procedure for changing the tenant token is called *tenant token rotation*.

To rotate the token, you need to generate a new token, assign it to all OneAgents and ActiveGates that report data to the environment, and then disable the old token.

To avoid data loss, both old and new tokens are valid during the rotation process. During rotation, do not deploy any new OneAgents until all your ActiveGates are configured with the new tenant token.

1. Start the rotation and generate a new tenant token by executing the [POST start rotation request](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-start "Initiate Dynatrace tenant token rotation.").

   The request returns the new token in the **active** field of the response body.
2. Add the new token to ActiveGates. For each ActiveGate:

   1. [Stop ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
   2. In the `authorization.properties` file of [ActiveGate configuration directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."), find the entry for the required environment and specify the new token in the **tenantToken** field.
   3. Depending on your [ActiveGate purpose](/docs/ingest-from/dynatrace-activegate/capabilities "Learn the capabilities and uses of ActiveGate."):

      * [Route OneAgent traffic and monitor remote technologies](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate."): Find the entry for the required environment in the `ruxitagent.conf` and `extensions.conf` files, and specify the new token in the **tenantToken**.

        **Windows**: `%PROGRAMFILES%\dynatrace\remotepluginmodule\agent\conf`  
        **Linux**: `/opt/dynatrace/remotepluginmodule/agent/conf`
      * [Install the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring."): Find the entry for the required environment and specify the new token in the **tenantToken** field.

        **Windows**: `%PROGRAMFILES%\dynatrace\zremote\agent\conf\ruxitagent.conf`  
        **Linux**: `/opt/dynatrace/zremote/agent/conf/ruxitagent.conf`
   4. Windows only Change the value of the registry entry: `HKEY_LOCAL_MACHINE\Software\Dynatrace\Dynatrace ActiveGate\common\tenant_token`.
   5. [Start ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/stop-restart-activegate "Learn how you can start, stop and restart ActiveGate on Windows or Linux.").
3. Add the new token to OneAgents. For each OneAgent:

   1. Add the new token to the communication settings of the OneAgent.

      Use the `--set-tenant-token` command of the [OneAgent command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#change-oneagent-communication-settings "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").
   2. [Restart](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#oneagent-restart "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") OneAgent.

   You can combine both steps into one command:

   ```
   oneagentctl --restart-service --set-tenant-token={new token}
   ```
4. Finish the rotation by executing the [POST finish rotation request](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens/post-finish "Finish Dynatrace tenant token rotation."). This finishes the process and renders the old token invalid.

## Related topics

* [Tenant tokens API](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens.")
* [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")
* [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")