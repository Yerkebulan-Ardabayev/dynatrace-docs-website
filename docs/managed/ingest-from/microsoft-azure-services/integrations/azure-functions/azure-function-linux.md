---
title: Monitor Azure Functions on Linux plans
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/azure-function-linux
---

# Monitor Azure Functions on Linux plans

# Monitor Azure Functions on Linux plans

* How-to guide
* 3-min read
* Published Jul 29, 2026

## Prerequisites

* Create a token to download and setup OneAgent:

  + [Platform tokens](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). Use Platform tokens to access the for following services:

    - fleet-management:oneagents:download
    - fleet-management:cluster-id:read
    - fleet-management:oneagent.tokens:read
  + [API Tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas "Learn the concept of an access token and its scopes.")
* Determine your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
* Determine your server URL if required.

  The server URL is required only if you use either of the following:

  + a Dynatrace Managed endpoint
  + an ActiveGate for a Dynatrace Managed or Dynatrace SaaS endpoint

  (For Dynatrace SaaS, the URL is automatically generated from the environment ID.)

  + **ActiveGate server URL:**  
    `https://<your-active-gate-IP-or-hostname>:9999/e/<your-environment-id>/api` (the ActiveGate port is configurable)
  + **Dynatrace Managed server URL:**  
    `https://{your-domain}/e/{your-environment-id}/api`

  If you're using Dynatrace Managed, or if your cluster traffic should be routed through an [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate."), you need to configure the API endpoint used by the extension for downloading OneAgent.

## Set up monitoring

Because Azure Functions on Linux has no native extension point, OneAgent is packaged as a runtime-specific deployment dependency. Dynatrace provides packages for all supported runtimes, meaning no changes to your function code are required.

Use the setup wizard in Dynatrace to generate configuration values tailored to your runtime and Dynatrace environment.

### Step 1: Open the setup wizard

Open the deployment wizard from one of these entry points:

* In ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub") **Dynatrace Hub**, select **Azure Functions** > **Set up**.
* On the onboarding page of ![Discovery & Coverage](https://dt-cdn.net/images/discovery-coverage-256-a20d5afa78.png "Discovery & Coverage") **Discovery & Coverage**,  **Services**, ![Distributed Traces](https://dt-cdn.net/images/distributed-traces-512-156c05158c.png "Distributed Traces") **Distributed Tracing**, or ![Fleet Management](https://dt-cdn.net/images/fleet-management-highresolution-1024-314b8c84b3.png "Fleet Management") **Fleet Management**, select **Azure Functions**.

Then complete the wizard:

1. Select your **runtime** (Python, Node.js, or .NET).
2. Select your **Azure Functions hosting option** (for example, Linux Flex Consumption).

The wizard generates:

* The environment variables (set via Azure Function Application Settings) to configure your function app.
* The exact package version to install.

### Step 2: Apply environment variables

Add the environment variables from the wizard to your function app's Application Settings. You can do this in the Azure portal under **Settings** > **Configuration** > **Application Settings**, or use the Azure CLI snippet the wizard provides.

The variables configure:

* Dynatrace connection.

  Variables: `DT_TENANT`, `DT_CLUSTER`, `DT_CONNECTION_BASE_URL`, `DT_CONNECTION_AUTH_TOKEN`.

  These variables identify your Dynatrace environment and authenticate OneAgent.
* Runtime startup hook.

  Variable: `languageWorkers__python__arguments` for Python, with an equivalent for each runtime.

  This variable registers OneAgent with the language runtime before your function executes. It enables automatic instrumentation at runtime, so you don't need to modify your function code.

Store `DT_CONNECTION_AUTH_TOKEN` as an [Azure Key Vault secret﻿](https://learn.microsoft.com/en-us/azure/app-service/app-service-key-vault-references) and reference it in your Application Settings rather than pasting the token value directly. This reduces the risk of unintentionally leaking the token.

### Step 3: Add the OneAgent package and redeploy

Add the runtime-specific OneAgent package as a dependency in your project using the version the wizard specifies. For example, for Python:

```
pip install dynatrace-oneagentpython==<version>



pip freeze > requirements.txt
```

Redeploy your function app. Azure Functions installs the package automatically during deployment, and OneAgent starts monitoring from the first invocation.

## Related topics

* [Monitor Azure Functions on Plans for Windows](/managed/ingest-from/microsoft-azure-services/integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.")
* [Serverless compute support matrix](/managed/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS).")