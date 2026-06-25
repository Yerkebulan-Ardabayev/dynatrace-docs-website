---
title: Migrate OneAgent
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-oa
scraped: 2026-05-12T12:14:00.644731
---

# Migrate OneAgent

# Migrate OneAgent

* Published Apr 24, 2023

To start collecting data in the target SaaS environment and completing configuration migration, you need to migrate OneAgents from your Managed environment.

There are several different ways to do this. Choose the method that works best for your situation.

* Recommended Remote bulk migration with remote configuration management
* Local migration with `oneagentctl`
* Using [OneAgent deployment orchestration](/managed/ingest-from/dynatrace-oneagent/deployment-orchestration "Learn how to deploy OneAgent using deployment orchestration")
* Uninstallation of existing OneAgent and installation from the SaaS environment

## Remote bulk migration with remote configuration management

Recommended

You can use [remote configuration management](/managed/ingest-from/bulk-configuration#bulk-configuration-oa-communication-settings "Perform OneAgent and ActiveGate configuration on hosts from the Deployment status page or at scale using the Dynatrace API.") to modify the communication settings of OneAgents from the same environment in bulk mode. The action is still performed on the respective hosts when using remote configuration management, but you trigger it and control it centrally from **Deployment Status** in the Dynatrace web UI.

To start, go to your Dynatrace Managed environment and select **Deployment Status** from the Dynatrace menu.

## Local migration with oneagentctl

Use the `oneagentctl` command-line interface to perform OneAgent reconfiguration at the individual host level. You'll need to update multiple OneAgent communication configuration settings:

* Set OneAgent communication settings
* Set environment ID
* Set environment token
* Set proxy configuration or unset proxy configuration. For details, [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

### How to use oneagentctl

Requirements:

* curl installed on a host

Specifying a wrong `--set-server` will lead to OneAgent losing communication with both the previous and the new environment.

There are two scenarios, depending on how OneAgent connects to your Dynatrace Managed environment currently:

1. Standalone OneAgent directly connects to your cluster nodes
   In this case, your SaaS environment's URL is the communication address for your OneAgent instances. You don't need to install anything additionally beforehand.
2. Standalone OneAgent uses a Cluster ActiveGate or Environment ActiveGate
   In this case, you need to [install a new Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") for your target environment. In the procedure below, use ActiveGate's address as a communication address.

To reconfigure OneAgent in place, follow the procedure below:

In your target environment:

1. Create an [access token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") â scope **PaaS integration - Installer download**.
2. From the user menu on the right, open the interactive REST API client for **Environment API v1**.
3. Run [Deployment API - View connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") using the generated token as an authentication.
4. Save the response from the API call. You'll need data from it in the next step.
5. Sign in to your target host and use the following command to reroute OneAgent to your new Dynatrace environment:

   * Linux or AIX:  
     `./oneagentctl --set-server=https://abc123456.live.dynatrace:443 --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`
   * Windows:  
     `.\oneagentctl.exe --set-server=https://abc123456.live.dynatrace.com:443 --set-tenant=abc123456 --set-tenant-token=abcdefg123456790 --set-proxy=my-proxy.com`

   The `--set-server` parameter sets a OneAgent communication endpoint. Use the IP address or name. Depending on your deployment, it can be an environment's or ActiveGate's URL. You can use `formattedCommunicationEndpoints` value from the API's response.

   The `--set-tenant` parameter sets an environment ID. You can use `tenantUUID` value from the API's response.

   The `--set-tenant-token` parameter sets the environment token, which is used to authenticate communication with the defined endpoint. You can use `tenantToken` value from the API's response.

   After the successful reconfiguration, the OneAgent will be restarted. For other operation options, see [OneAgent configuration via command-line interface](/managed/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").
6. After reconfiguring the OneAgent, you need to restart all the applications monitored with deep code modules.
7. Go to **Deployment Status** and select **OneAgents** to check if your OneAgent appears and if monitored applications are monitored successfully. In case of an error, repeat these steps to reroute the OneAgent to the Managed environment.

Questions?

Visit the [Upgrade to SaaS forumï»¿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.