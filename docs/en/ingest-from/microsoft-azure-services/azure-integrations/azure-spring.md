---
title: Monitor Azure Spring Apps
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring
scraped: 2026-03-01T21:28:20.090844
---

# Monitor Azure Spring Apps

# Monitor Azure Spring Apps

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Jul 16, 2021

## Capabilities

* Full-stack java monitoring powered by OneAgent
* Integration with [Azure Monitor](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Monitor Azure Spring Apps and view available metrics.")
* Automatic service detection of services running in Azure Spring Apps

Since Azure Spring Apps is a fully managed hosting platform, applications are deployed into a sandboxed environment that doesn't allow direct access to the underlying operating system.

See below how you can integrate OneAgent with your Azure Spring Apps application to monitor your Spring Apps workloads with Dynatrace.

## Prerequisites

* Create a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.")
* [Install the Azure CLIï»¿](https://dt-url.net/cf63rl6)

## Set up integration

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Prepare your environment in Azure**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#prepare-env "Learn how to configure OneAgent for monitoring Azure Spring Apps.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Determine the values for the required environment variables**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#envvar "Learn how to configure OneAgent for monitoring Azure Spring Apps.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Add the environment variables to your application**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring#add-variables "Learn how to configure OneAgent for monitoring Azure Spring Apps.")

### Step 1 Prepare your environment in Azure

1. In Azure Portal, create an Azure Spring Apps instance.
2. In the new Azure Spring Apps instance, create an application that you want to report to Dynatrace by running the command below.

   Be sure to replace the placeholders (`<...>`) with your own values.

   ```
   az spring app create --name <your-application-name> --is-public true -s <your-resource-name> -g <your-resource-group-name>
   ```

### Step 2 Determine the values for the required environment variables

To set up OneAgent integration with your Azure Spring Apps instance, you need to configure three environment variables:

* `DT_TENANT`
* `DT_TENANTTOKEN`
* `DT_CONNECTION_POINT`.

Before you begin, collect the following information:

* Your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
* Authentication

  + **PaaS token** authenticates you as a Dynatrace user and is required to determine the tenant token.
  + **Tenant token** allows OneAgent to report data to Dynatrace.
    For more information on tokens, see [Access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.").

1. The value for `DT_TENANT`is your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
2. To determine the values for `DT_TENANTTOKEN` and `DT_CONNECTION_POINT`, make an API request to the [Deployment API - GET connectivity information for OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") endpoint. The values you need are returned as `tenantToken` and `communicationEndpoints`.

   You can submit the call to your environment URL (SaaS or Managed) or an Environment ActiveGate URL.

   * **Dynatrace SaaS**:

     ```
     curl https://<your-environment-id>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Replace:

     + `<your-environment-id>` with your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
     + `<your_PaaS_token>` with your [PaaS token](#prerequisites)
   * **Dynatrace Managed**:

     ```
     curl https://<your-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Replace:

     + `<your-domain>` with your Managed deployment domain
     + `<your-environment-id>` with your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
     + `<your_PaaS_token>` with your [PaaS token](#prerequisites)
   * **Environment ActiveGate**:

     ```
     curl https://<your-activegate-domain>/e/<your-environment-id>/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<your_PaaS_token>
     ```

     Replace

     + `<your-activegate-domain>` with your ActiveGate domain
     + `<your-environment-id>` with your [Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.")
     + `<your_PaaS_token>` with your [PaaS token](#prerequisites)

### Step 3 Add the environment variables to your application

Once you have the values for the environment variables required for OneAgent integration, you can add the respective key/value pairs to your application either on Azure Portal, or in the Azure CLI. See the instructions below for each of these options.

In the Azure CLI

In Azure Portal

Run the command below, making sure to replace the placeholders (`<...>`) with your own values determined in the previous steps.

```
az spring app deploy --name <your-application-name> --jar-path app.jar \



-s <your-resource-name> -g <your-resource-group-name> --env DT_TENANT=<your-environment-ID> \



DT_TENANTTOKEN=<your-tenant-token> DT_CONNECTION_POINT=<your-communication-endpoint>
```

1. Go to your Azure Spring Apps instance and select the resource group where Dynatrace will be deployed.
2. Select the application for which you want Dynatrace to report data.
3. Select **Configuration** and enter the following environment variables key/value pairs.

   | Key | Value |
   | --- | --- |
   | `DT_TENANT` | [Your Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") |
   | `DT_TENANTTOKEN` | Your tenant token. See [Determine the values for the required environment variables](#envvar) for details. |
   | `DT_CONNECTION_POINT` | Your communication endpoint. See [Determine the values for the required environment variables](#envvar) for details. |
4. [Create a buildpack bindingï»¿](https://dt-url.net/nu036u6) for Dynatrace using the PaaS token (API token) and API url as properties.

   | Property | Value |
   | --- | --- |
   | `api-url` | [Your Dynatrace environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") |
   | `api-token` | [PaaS token](#prerequisites) |

Optionally, you can customize the built-in rules for process group detection by setting another environment variable, `DT_CLUSTER_ID`. The value can be the name of the process group you want to see in Dynatrace. See [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection") for details.

## View data in Dynatrace

Once you add the environment variables to your application, Dynatrace starts collecting data from it. To view data for your Azure Spring Apps application, go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select your application.

Example service flow:

![AppFlow](https://dt-cdn.net/images/1-1721-67868203e3.png)

Example CPU consumption:

![Diagnostic cpu](https://dt-cdn.net/images/diagnostic-cpu-1565-a403ae7a02.png)

Example response time analysis:

![Resposetime](https://dt-cdn.net/images/f-1486-bd826153cb.png)

## OneAgent updates

OneAgent updates are performed automatically with the JDK.

Following a OneAgent update, you need to restart or redeploy your applications for them to be monitored with a new OneAgent version. This is because some components of OneAgent keep running in processes that are monitored by Dynatrace.

* Before restart, these processes will continue to be monitored with the previous version of OneAgent.
* After restart, these processes will be monitored with the latest version of OneAgent.

## Related topics

* [Monitor Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring/monitor-azure-spring-apps "Monitor Azure Spring Apps and view available metrics.")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")