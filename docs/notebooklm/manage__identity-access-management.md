# Dynatrace Documentation: manage/identity-access-management

Generated: 2026-02-18

Files combined: 18

---


## Source: rotate-tenant-token.md


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


---


## Source: access-tokens.md


---
title: Access tokens classic
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
scraped: 2026-02-18T05:52:57.700545
---

# Access tokens classic

# Access tokens classic

* Reference
* 2-min read
* Updated on Oct 25, 2023

This article discusses access tokens used in previous Dynatrace to authenticate to classic Configuration and Environment APIs. For the latest Dynatrace access, see [Platform tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.") and [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

All external access to your Dynatrace monitoring environment relies on two pieces of information: the [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") and an *access token*.

Dynatrace uses several types of tokens:

* Access tokens and personal access tokens grant access to:

  + [Dynatrace API](/docs/dynatrace-api "Find out what you need to use the Dynatrace API.")
  + Download of OneAgent and ActiveGate installers
* [Personal access tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.") grant access to some endpoints of Dynatrace API
* [Tenant tokens](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.") allow OneAgent to report data to Dynatrace

## Token format

Dynatrace uses a unique token format consisting of three components separated by dots (`.`).

### Token example

`<DYNATRACE_TOKEN_PLACEHOLDER>`

### Token components

Component name

Component description

prefix

The **prefix** identifies the token type.

In our example: `dt0s01`

See [Token prefixes](#token-format-prefixes) below for a table of standard prefixes.

public portion

The **public portion** of the token is a 24-character public identifier.

In our example: `ST2EY72KQINMH574WMNVI7YN`

token identifier

The **token identifier** is the combination of the **prefix** and the **public portion**. A token identifier can be safely displayed in the UI and can be used for logging purposes.

In our example: `<DYNATRACE_TOKEN_PLACEHOLDER>`

secret portion

The **secret portion** of the token is a 64-character string that should be treated like a password:

* Don't display it
* Don't store it in log files
* Rotate it instantly if it's leaked

In our example: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Token prefixes

Prefix

Description

`dt0s01`

This is an API token. It's used as an authorization method: a valid token allows the user to make changes within the Dynatrace account through SCIM.

* It is generated once.
* Do not reveal the secret portion of a `dt0s01` token.
* The public portion is used for identification in the web UI, but you generally should not reveal it (or any portion of this token).
* This token remains in effect until invalidated by the customer, so you must rotate it instantly if it is ever leaked.

`dt0s02`

OAuth2 Clients created by users through Account Management to be used with Dynatrace Apps and Account Management API.

`dt0s03`

OAuth2 Clients for internal and external services and integrations.

`dt0s04`

Chat and identity linking.

`dt0s06`

This is an OAuth2 Refresh Token, which is used to retrieve a new Access Token and generally changes frequently (typically every 5 to 15 minutes).

`dt0s08`

OAuth2 Clients for internal and external services and integrations.

`dt0s09`

Chat and identity linking.

`dt0s16`

Platform Token enabling programmatic access to Dynatrace platform services.

This predictable format offers you several capabilities:

* Use Git pre-commit hooks to avoid pushing tokens to source code repositories (for example, using tools like [git-secretsï»¿](https://github.com/awslabs/git-secrets))
* Define masking rules to obfuscate the secret portions of tokens when writing log files
* Detect tokens in internal files or communications
* Enable the [GitHub secret scanning serviceï»¿](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning#about-secret-scanning-for-public-repositories) to identify any token pushed to a public GitHub repository

Use this regular expression to look for tokens:

```
dt0[a-zA-Z]{1}[0-9]{2}\.[A-Z0-9]{24}\.[A-Z0-9]{64}
```

With the rollout of Dynatrace version 1.210, this format is enabled by default (all newly generated tokens will use the new format).

All existing tokens of the old format remain valid.

### Disable the new format

For a limited time, you can opt out of using the new token format:

1. Go to **Settings > Integration > Token settings**.
2. Turn off **Create Dynatrace API tokens in the new format**.

## Generate an access token

To generate an access token:

1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

## Token scopes

Access tokens have fine-grained scopes to limit access to specific product functionality for security reasons.

### OpenPipeline

Name

API value

Description

OpenPipeline - Ingest Events

`openpipeline.events`

Grants access to [POST Built-in generic events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-builtin "Ingest generic events from built-in endpoints via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events, Software Development Lifecycle

`openpipeline.events_sdlc`

Grants access to [POST Built-in SLDC events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-builtin "Ingest SDLC events from built-in endpoints via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events, Software Development Lifecycle (Custom)

`openpipeline.events_sdlc.custom`

Grants access to [POST Custom SLDC events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/sdlc-events/events-sdlc-custom-endpoint "Configure a custom SDLC event endpoint via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Security Events (Built-in)

`openpipeline.events_security`

Grants access to [POST Built-in security events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-builtin "Ingest security events from built-in endpoints via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Security Events (Custom)

`openpipeline.events_security.custom`

Grants access to [POST Custom security events](/docs/platform/openpipeline/reference/openpipeline-ingest-api/security-events/events-security-custom-endpoint "Configure a custom security event endpoint via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events (Custom)

`openpipeline.events.custom`

Grants access to [POST Custom generic event endpoint](/docs/platform/openpipeline/reference/openpipeline-ingest-api/generic-events/events-generic-custom-endpoint "Configure a custom generic event endpoint via OpenPipeline Ingest API.") request of the OpenPipeline Ingest API.

### API v2

Name

API value

Description

Read ActiveGates

`activeGates.read`

Grants access to GET requests of the [ActiveGates API](/docs/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers.").

Write ActiveGates

`activeGates.write`

Grants access to POST and DELETE requests of the [ActiveGates API](/docs/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers.").

Create ActiveGate tokens

`activeGateTokenManagement.create`

Grants access to the POST request of the ActiveGate tokens API.

Read ActiveGate tokens

`activeGateTokenManagement.read`

Grants access to GET requests of the ActiveGate tokens API.

Write ActiveGate tokens

`activeGateTokenManagement.write`

Grants access to POST and DELETE requests of the ActiveGate tokens API.

Read API tokens

`apiTokens.read`

Grants access to GET requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Write API tokens

`apiTokens.write`

Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/docs/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

Read attacks

`attacks.read`

Grants access to GET requests of the Attacks API and the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`).

Write Application Protection settings

`attacks.write`

Grants access to POST, PUT, and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`).

Read audit logs

`auditLogs.read`

Grants access to the [audit log](/docs/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API.").

Read credential vault entries

`credentialVault.read`

Grants access to GET requests of the [Credential vault API](/docs/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.").

Write credential vault entries

`credentialVault.write`

Grants access to POST, PUT, and DELETE requests of the [Credential vault API](/docs/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers.").

Read entities

`entities.read`

Grants access to GET requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Write entities

`entities.write`

Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/docs/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs.

Ingest events

`events.ingest`

Grants access to POST request of the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

Read events

`events.read`

Grants access to GET requests of the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

Read extensions monitoring configuration

`extensionConfigurations.read`

Grants access to GET requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Write extensions monitoring configuration

`extensionConfigurations.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Read extensions environment configuration

`extensionEnvironment.read`

Grants access to GET requests from the **Extensions environment configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Write extensions environment configuration

`extensionEnvironment.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions environment configuration** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Read extensions

`extensions.read`

Grants access to GET requests from the **Extensions** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Write extensions

`extensions.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions** section of the [Extensions 2.0 API](/docs/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API.").

Read Geographic regions

`geographicRegions.read`

Grants access to the [Geographic regions API](/docs/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API.").

Install and update Hub items

`hub.install`

Grants permission to install and update extensions via the [Hub items API](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.").

Read Hub related data

`hub.read`

Grants access to GET requests of the [Hub items API](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.").

Manage metadata of Hub items

`hub.write`

Grants permission to manage metadata of Hub items via the [Hub items API](/docs/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API.").

Read JavaScript mapping files

`javaScriptMappingFiles.read`

Write JavaScript mapping files

`javaScriptMappingFiles.write`

Ingest logs

`logs.ingest`

Grants access to the [POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") request of the Log Monitoring API v2 as well as the [OpenTelemetry log ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Read logs

`logs.read`

Grants access to the GET requests of the [Log Monitoring API v2](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

Ingest metrics

`metrics.ingest`

Grants access to the [POST ingest data points](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") request of the Metrics v2 API as well as the [OpenTelemetry metrics ingest API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Read metrics

`metrics.read`

Grants access to GET requests of the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

Write metrics

`metrics.write`

Grants access to the [DELETE a custom metric](/docs/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2.

Read network zones

`networkZones.read`

Grants access to GET requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Write network zones

`networkZones.write`

Grants access to POST, PUT, and DELETE requests of the [Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.").

Read OneAgents

`oneAgents.read`

Grants access to GET requests of the [OneAgents API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Write OneAgents

`oneAgents.write`

Grants access to POST and DELETE requests of the [OneAgents API](/docs/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API.").

Ingest OpenTelemetry traces

`openTelemetryTrace.ingest`

Grants permission to [ingest OpenTelemetry traces](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

Read problems

`problems.read`

Grants access to GET requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Write problems

`problems.write`

Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/docs/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers.").

Read releases

`releases.read`

Grants access to the [Releases API](/docs/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers.").

Read security problems

`securityProblems.read`

Grants access to GET requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Write security problems

`securityProblems.write`

Grants access to POST requests of the [Security problems API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.").

Read settings

`settings.read`

Grants access to GET requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Write settings

`settings.write`

Grants access to POST and DELETE requests of the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

Read SLO

`slo.read`

Grants access to GET requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.").

Read synthetic monitor execution results

`syntheticExecutions.read`

Grants access to GET requests of the `/synthetic/executions` API.

Write synthetic monitor execution results

`syntheticExecutions.write`

Grants access to POST request of `/synthetic/executions` API.

Read synthetic locations

`syntheticLocations.read`

Grants access to GET requests of the [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.").

Write synthetic locations

`syntheticLocations.write`

Grants access to POST, PUT, and DELETE requests of the [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API.").

Tenant token rotation

`tenantTokenRotation.write`

Grants access to the [Tenant tokens API](/docs/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens.").

Look up a single trace

`traces.lookup`

Checks for the presence of a trace in cross-environment tracing.

Read Unified Analysis page

`unifiedAnalysis.read`

Grants access to the Unified analysis schema in the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.").

### API v1

Name

API value

Description

Access problems and event feed, metrics, and topology

`DataExport`

Grants access to various calls of [Environment API](/docs/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API.").

Create and read synthetic monitors, locations, and nodes

`ExternalSyntheticIntegration`

Grants access to the [Synthetic API](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.").

Read synthetic monitors, locations, and nodes

`ReadSyntheticData`

Grants access to GET requests of [Synthetic API](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.").

Read configuration

`ReadConfig`

Grants access to GET calls of [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Write configuration

`WriteConfig`

Grants access to POST, PUT, and DELETE calls of [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Change data privacy settings

`DataPrivacy`

Grants access to [Data privacy API](/docs/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.") and data privacy calls of [Web application configuration API](/docs/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers.").

User sessions

`DTAQLAccess`

Grants access to [User sessions API](/docs/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers.").

Anonymize user sessions for data privacy reasons

`UserSessionAnonymization`

Grants access to [Anonymization API](/docs/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data.").

Mobile symbol file management

`DssFileManagement`

Grants access to [Mobile symbolication API](/docs/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API.").

Real User Monitoring JavaScript tag management

`RumJavaScriptTagManagement`

Grants access to [Real User Monitoring JavaScript API](/docs/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API.").

ActiveGate certificate management

`ActiveGateCertManagement`

Grants permission to [configure certificate](/docs/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.") on private ActiveGates.

Fetch data from a remote environment

`RestRequestForwarding`

Grants permission to fetch data from [remote Dynatrace environments](/docs/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.") for multi-environment dashboarding.

Capture request data

`CaptureRequestData`

Grants access to [Request attributes API](/docs/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers.").

Read log content

`LogExport`

Grants access to [Log Monitoring API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.").

### PaaS

Name

API value

Description

Download OneAgent and ActiveGate installers

`InstallerDownload`

Allows download of installers via [Deployment API](/docs/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API.").

Create support alerts

`SupportAlert`

Allows creation of [support alerts](/docs/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Learn how Dynatrace can help you gain insight into process crashes.") for crash analysis.

### Other

Name

API value

Description

Upload plugins using the command line

`PluginUpload`

Grants permission to upload OneAgent extensions via [Extension SDK](/docs/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.").

## Related topics

* [Tokens API v1](/docs/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")


---


## Source: platform-tokens.md


---
title: Platform tokens
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens
scraped: 2026-02-18T05:55:56.715982
---

# Platform tokens

# Platform tokens

* Latest Dynatrace
* Reference
* 8-min read
* Published Jul 23, 2024

Platform tokens are long-lived access tokens enabling programmatic access to Dynatrace platform services. They can be created by regular users and work within the bounds of the assigned user permissions.

Platform tokens are a user-friendly alternative to OAuth clients and are suited for processes and applications that integrate directly with the Dynatrace API. They can be assigned to the user creating them or to a service user that the creating user has access to.

Platform tokens can be set to expire after a period of time or never expire.

These properties make platform tokens a good candidate for all sorts of integrations with the Dynatrace platform, such as:

* Running a scheduled Grail query for data export and ETL
* Ingesting business metrics and events via the API
* A script that keeps Dashboards in sync across multiple environments

## How to use a platform token

Platform tokens are directly usable with the APIs offered by the Dynatrace platform services. To use a platform token please provide the token in the Authorization header:

`Authorization: Bearer <platformtoken>`

To get an overview of all the services supporting platform tokens, go to the Dynatrace API explorer. In Dynatrace, search for **Dynatrace API** and select the result.

You can also directly put the platform token into the Authorization field in the Dynatrace API explorer for quick experimentation and try-out.

## My platform tokens

This feature is available for regular users. Every user can create platform tokens in all the accounts of which they are a member.

The platform token management operations listed below are all performed using the **Account Management** pages.

1. Go to [My platform tokensï»¿](https://myaccount.dynatrace.com/platformTokens).

   This opens `https://myaccount.dynatrace.com/platformTokens`, which you can bookmark for easy access to platform tokens Management.
2. You are presented with a table that list all your platform tokens.

This page lists all of your platform tokens and enables you to create, delete, or disable your tokens.

### Create a new platform token

Every user is able to create up to 10 platform tokens in a given account.

1. Select  \*\*platform token \*\* and specify:

   * **Token Name**
   * **Expiration date**
   * **Account**
   * **Apply to account**
   * **Environments**.

     + If **apply to account** has been selected, this is not available.
2. Choose if the new token will be generated for you (default) or a service user you have access to.
3. Select token scopes in the table below

   * The table provides you with a list of scopes that map to the individual endpoints on the API.
   * Go to the Dynatrace API explorer, to see the mapping between token scopes and API endpoints.
   * **IMPORTANT**: A platform token will only work within the limits of the assigned user's permissions. This means that a selected scope is only granting access if that user has the respective permissions.
4. Select **Generate** to generate the platform token.
5. The created token will only be shown once, so make sure you copy it into a secure location.
6. After you have saved the token, select **Finish and exit** to return to the list of platform tokens.

### Disable a platform token

1. Find the platform token that you want to disable in the list overview.
2. In the **Actions** column, select  > **Disable**.
3. Select **Cancel** to cancel or **Disable** to confirm.

   * The dialog shows the ID of the token for confirmation.

A disabled token can not be used on the API but can later on be re-enabled to continue using it.
This is handy if you want to temporary block a token.

Disabling a platform token is immediate, but it may take up to five minutes for the change to propagate.

### Delete a platform token

1. Find the platform token that you want to delete in the list overview
2. In the **Actions** column, select  > **Delete**.
3. Select **Cancel** to cancel or **Disable** to confirm.

   * The dialog shows the ID of the token for confirmation.

### Duplicate a platform token

1. Find the platform token that you want to duplicate in the list overview.
2. In the **Actions** column, select  > **Duplicate**.
3. The creation process is triggered with an exact copy of the properties of the original token and the name "Duplicate of:" `<token-name>`.
4. Adjust the properties to your liking and select **Generate**.
5. After you duplicate the token, it's the only time you can preview it and copy to store for later use.
6. After you have stored the token, select **Finish and exit** to return to the list of platform tokens.

### Rotate a platform token

It's a security best practice to regularly rotate your tokens.

To rotate an active token

1. Find the platform token that you want to rotate in the list overview.
2. In the **Actions** column, select  > **Rotate**.
3. Choose when to expire the old token

   * You may choose to expire immediately or defer to a later time so that you allow some overlap between the two tokens.
4. Choose a name.

   * To differentiate the rotated token from the original, you can add the current date in the token name.  
     old: `K8s operator`  
     new: `K8s operator 10.09.2024`
5. Either accept the proposed expiry time or change it.
6. Select **Rotate**.

   * Do not forget to replace the old token with the new one, in all places you are using it.

### Expired tokens

Expired tokens will continue to show in the list overview until you or the account admin decides to delete them.

## Manage users tokens

Account admins can disable or delete platform tokens created by all users under their account. The Account Management UI management actions are performed in a similar way to the ones listed above for regular users.

### Disable platform token creation for an entire account

Account admins have the ability to enable or disable creation of new platform tokens for a given account.

1. In Account Management, go to **Identity & access management** > **Platform tokens**.
2. Turn off **Allow to manage platform tokens** and confirm the dialog with **Deny**.
3. Optional To disable existing platform tokens use, select specific or all tokens with the checkboxes on the left and select **Disable** at the top of the list.
4. Optional To delete existing platform tokens use, select specific or all tokens with the checkboxes on the left and select **Delete** at the top of the list.

To re-enable the creation of new platform tokens, turn on **Allow to manage platform tokens** and confirm the dialog with **Allow**.

### Allow users to generate platform tokens against service users

To allow users to generate platform tokens against existing service users, the account admin needs to assign `iam:service-users:use` permissions, and optionally conditionalize it with `iam:service-user-email` to one or more groups. An example policy could look like this:

```
ALLOW iam:service-users:use



WHERE iam:service-user-email IN ("abc@service.sso.dynatrace.com", "def@service.sso.dynatrace.com");
```

## Platform tokens requirements

* A maximum of 10 platform tokens can be generated by a user for a given account.
* A platform token is scoped to only one account and cannot be used to access other accounts.
* A platform token can be further reduced in scope to only target one or many environments within the account the token is being issued against.
* A platform token name can't exceed 255 characters.
* Using expired platform tokens to access Dynatrace will return an HTTP error 403 response.

## Available services for platform tokens

The following services are covered by platform tokens:

* `app-engine`
* `automation`
* `notification`
* `davis`
* `davis-copilot`
* `document`
* `email`
* `iam`
* `platform-management`
* `storage`
* `settings`
* `app-settings`
* `state`
* `state-management`


---


## Source: iam-concepts.md


---
title: Overview of Dynatrace IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/iam-concepts
scraped: 2026-02-18T05:46:36.613895
---

# Overview of Dynatrace IAM

# Overview of Dynatrace IAM

* Latest Dynatrace
* Overview
* 2-min read
* Updated on Jun 18, 2025

This guide outlines the key Identity and Access Management (IAM) components in Dynatrace, covering user and group management, access models, identity providers, access policies, and access tokens. These components ensure secure interactions, enable effective automation, and support seamless integration within the platform.

## Identity management

Manage user and group lifecycle operations and implement automated authentication with identity providers (IdPs).

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover the IAM user types, identity federation, and user repositories.](/docs/manage/identity-access-management/user-and-group-management/identity-concepts "Understand the key identity concepts in Dynatrace IAM")[### Local users

Dynatrace serves as your identity store.](/docs/manage/identity-access-management/user-and-group-management/identity-concepts#users "Understand the key identity concepts in Dynatrace IAM")[### Service users

Non-human identities interacting with services and resources.](/docs/manage/identity-access-management/user-and-group-management/identity-concepts#service-users "Understand the key identity concepts in Dynatrace IAM")[### SAML federation

Delegate authentication through your IdP.](/docs/manage/identity-access-management/user-and-group-management/access-saml "SAML")[### SCIM

Keep your identity repositories in sync.](/docs/manage/identity-access-management/user-and-group-management/access-scim "SCIM")

## Access management

Define granular user access in Dynatrace, controlling permissions to safeguard sensitive data and resources.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover how Dynatrace manages groups and policies.](/docs/manage/identity-access-management/permission-management/access-concepts "Understand the key access concepts in Dynatrace IAM")[### Groups

Collectively manage your access configurations.](/docs/manage/identity-access-management/permission-management/access-concepts#groups "Understand the key access concepts in Dynatrace IAM")[### Policies

Define tailored permissions to access resources.](/docs/manage/identity-access-management/permission-management/access-concepts#policies "Understand the key access concepts in Dynatrace IAM")[### Policy boundaries

Scale, refine, and simplify access permissions.](/docs/manage/identity-access-management/permission-management/access-concepts#policy-boundaries "Understand the key access concepts in Dynatrace IAM")[### Policy templates

Reusable policies to regulate access control.](/docs/manage/identity-access-management/permission-management/access-concepts#policy-templates "Understand the key access concepts in Dynatrace IAM")[### Default policies

Get started with Dynatrace default policies.](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference")[### Default groups

Get started with Dynatrace default groups.](/docs/manage/identity-access-management/user-and-group-management/default-groups "Dynatrace default groups reference")

## Tokens and OAuth clients

Externalize and automate the access to Dynatrace using secure tokens.

[![Concepts](https://dt-cdn.net/images/concept-6e215a8350.svg "Concepts")

### Concepts

Discover how Dynatrace handles API tokens and access automation.](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/token-concepts "Understand the key API access and automation in Dynatrace IAM")[### Platform tokens

Allow interactions with the Dynatrace platform.](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/platform-tokens "Create personalised platform tokens to access Dynatrace services via the API in your user context.")[### OAuth tokens

Access Dynatrace through OAuth clients.](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.")


---


## Source: iam-limits.md


---
title: Identity and Access Management limits
source: https://www.dynatrace.com/docs/manage/identity-access-management/iam-limits
scraped: 2026-02-17T21:29:21.553191
---

# Identity and Access Management limits

# Identity and Access Management limits

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Nov 12, 2025

The following table indicates the current default IAM resource limits.

About Adjustable column

Limits marked as 'Adjustable' can only be modified through contacting our customer support. Please note that we will validate every request before considering a change.

Recommended

| Resource | Level | Default limit | Adjustable |
| --- | --- | --- | --- |
| Users | Account | 10,000 | Yes |
| Groups | Account | 5,000 | Yes |
| Groups | User | 8,000 | Yes |
| Permissions | Group | 1,000 | Yes |
| OAuth clients | Account | 200 | No |
| SCIM tokens | Account | 10 | No |
| Policies | Account | 200 | No |
| Policy statements | Policy | 100 | No |
| Groups-to-policy bindings | Account or Environment | 30,000 | No |
| Policy boundaries | Account | 2,000 | No |
| Policy boundary restrictions | Boundary | 10 | No |


---


## Source: iam-policystatements.md


---
title: IAM policy reference
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements
scraped: 2026-02-18T05:52:16.038063
---

# IAM policy reference

# IAM policy reference

* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 25, 2021

The following is a complete reference of IAM permissions and corresponding conditions applicable to Dynatrace services. Refer to it when you need to define access policies based on a fine-grained set of permissions and conditions that can be enforced per service.

## ai

AI exposes generative AI capabilities in Dynatrace

### ai:operator:execute

Grants permission to interact with the AI conversational interface

## app-engine

AppEngine

### app-engine:apps:install

Grants permission to install and update apps

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - The ID of the user that installed the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:apps:run

Grants permission to list and run apps and gives basic access to the Launcher

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - The ID of the user that installed the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:apps:delete

Grants permission to uninstall apps

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`
* `app-engine:app-installer` - The ID of the user that installed the app.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT IN`, `NOT startsWith`

### app-engine:functions:run

Grants permission to use the function-executor

### app-engine:edge-connects:read

Grants permission to read EdgeConnects

### app-engine:edge-connects:write

Grants permission to write EdgeConnects

### app-engine:edge-connects:delete

Grants permission to delete EdgeConnects

### app-engine:certificates:create

Grants permission to create short-living certificates for app releases

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `=`, `IN`, `startsWith`

## app-settings

App Settings service

### app-settings:objects:read

Grants permission to read app settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single app settings schema. The identifier of a schema can be found in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### app-settings:objects:write

Grants permission to write settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can be found in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### app-settings:objects:admin

Enables using admin-mode to access, change ownership and share permissions of any object. Admin-mode only bypasses the ownership check - so to do anything useful, app-settings:objects:read and/or app-settings:objects:write are needed as well.

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single app settings schema. The identifier of a schema can be found in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## automation

Automation Server

### automation:workflows:read

Grants permission to read workflows

### automation:workflows:write

Grants permission to write workflows

#### conditions:

* `automation:workflow-type` - A string that identifies a workflow type either SIMPLE or STANDARD  
  operators: `IN`, `=`

### automation:workflows:run

Grants permission to execute workflows

### automation:workflows:admin

Grant admin permissions for workflows.

### automation:rules:read

Grants permission to read scheduling rules

### automation:rules:write

Grants permission to write scheduling rules

### automation:calendars:read

Grants permission to read business calendars

### automation:calendars:write

Grants permission to write business calendars

## business-analytics

Platform Business Analytics Service

### business-analytics:business-flows:write

Grants permission to write business-flows

### business-analytics:business-flows:read

Grants permission to read business-flows

## data-acquisition

Data Acquisition Ingest

### data-acquisition:logs:ingest

Grants permission to ingest logs from Data Acquisition supported sources

### data-acquisition:metrics:ingest

Grants permission to ingest metrics from Data Acquisition supported sources

### data-acquisition:events:ingest

Grants permission to ingest events from Data Acquisition supported sources

## davis

Davis service

### davis:analyzers:read

Grants permission to view Davis analyzers

### davis:analyzers:execute

Grants permission to execute Davis analyzers

## davis-copilot

Davis CoPilot exposes generative AI capabilities in Dynatrace

### davis-copilot:conversations:execute

Grants permission to interact with the Davis CoPilot conversational interface

### davis-copilot:nl2dql:execute

Grants permission to execute the Natural Language to DQL generative AI capability

### davis-copilot:dql2nl:execute

Grants permission to execute the CoPilot skill 'Summarize DQL'

### davis-copilot:document-search:execute

Grants permission to execute the CoPilot skill 'Document Search'

## deployment

Deployment service

### deployment:activegates.network-zones:write

Grants permission to write ActiveGate network zones

### deployment:activegates.groups:write

Grants permission to write ActiveGate groups

### deployment:oneagents.network-zones:write

Grants permission to write OneAgent network zones

### deployment:oneagents.host-groups:write

Grants permission to write OneAgent host groups

### deployment:oneagents.host-tags:write

Grants permission to write OneAgent host tags

### deployment:oneagents.host-properties:write

Grants permission to write OneAgent host properties

### deployment:oneagents.communication-settings:write

Grants permission to write OneAgent communication settings

## dev-obs

Developer Observability

### dev-obs:breakpoint:set

Grants permission to set breakpoint using DevObs live debugger

#### conditions:

* `dev-obs:k8s.namespace.name` - Kubernetes namespaces of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.entity.process_group` - Dynatrace entity process group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.process_group.detected_name` - Dynatrace process group detected name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:k8s.cluster.name` - Cluster name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.group` - Host group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.name` - Host name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`

### dev-obs:breakpoints:set

Grants permission to set breakpoint using DevObs live debugger

#### conditions:

* `dev-obs:k8s.namespace.name` - Kubernetes namespaces of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.entity.process_group` - Dynatrace entity process group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:dt.process_group.detected_name` - Dynatrace process group detected name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:k8s.cluster.name` - Cluster name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.group` - Host group of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`
* `dev-obs:host.name` - Host name of the agents where the user is allowed to set breakpoints  
  operators: `=`, `IN`, `startsWith`, `!=`, `NOT IN`, `NOT startsWith`

### dev-obs:breakpoint:manage

Grants permission to manage breakpoints set in DevObs live debugger

### dev-obs:breakpoints:manage

Grants permission to manage breakpoints set in DevObs live debugger

## document

Document service

### document:documents:write

Grants permission to create and update documents of the document service

### document:documents:read

Grants permission to read documents of the document service

### document:documents:delete

Grants permission to delete documents of the document service

### document:documents:admin

Grants admin permissions for documents of the document service

### document:environment-shares:read

Grants permission to read environment shares of the document service

### document:environment-shares:write

Grants permission to create and update environment shares of the document service

### document:environment-shares:claim

Grants permission to claim environment shares of the document service

### document:environment-shares:delete

Grants permission to delete environment shares of the document service

### document:direct-shares:delete

Grants permission to delete direct shares of the document service

### document:direct-shares:read

Grants permission to read direct shares of the document service

### document:direct-shares:write

Grants permission to create and update direct shares of the document service

### document:trash.documents:read

Grants permission to read deleted documents of the document service

### document:trash.documents:delete

Grants permission to remove deleted documents from the trash of the document service

### document:trash.documents:restore

Grants permission to restore deleted documents from the trash of the document service

## email

API for sending emails

### email:emails:send

Grants permission to send emails from @apps.dynatrace.com with send email API

## environment

Environment and management zone user permissions. See [Migrate role-based permissions to Dynatrace IAMï»¿](https://dt-url.net/3s23539) for more information.

Role IAM permissions work the same way as classic roles do, which means that the `environment:roles:viewer` permission is a part of any other role permission. For example, a policy granting `environment:roles:manage-settings` permission also allows a user to access the web UI.

### environment:roles:viewer

Grants user the **Access environment** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on the management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-settings

Grants user the **Change monitoring settings** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:agent-install

Grants user the **Download/install OneAgent** permission. Users who have this permission assigned are also able to view monitoring data for all management zones.

### environment:roles:view-sensitive-request-data

Grants user the **View sensitive request data** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:configure-request-capture-data

Grants user the **Configure capture of sensitive data** permission. Users who have this permission assigned are also able to view monitoring data for all management zones.

### environment:roles:replay-sessions-without-masking

Grants user the **Replay session data without masking** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:replay-sessions-with-masking

Grants user the **Replay session data** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:manage-security-problems

Grants user the **Manage security problems** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:view-security-problems

Grants user the **View security problems** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

### environment:roles:logviewer

Grants user the **View logs** permission.

#### conditions:

* `environment:management-zone` - A string that uniquely identifies a management zone. Applies the permission on management zone level for the specified management zone.  
  operators: `IN`, `startsWith`, `NOT startsWith`, `=`, `!=`, `MATCH`

## extensions

Extensions service

### extensions:definitions:read

Grants permission to read extension and environment configurations

#### conditions:

* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:definitions:write

Grants permission to write (update/create/delete) extension and environment configurations

#### conditions:

* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:read

Grants permission to read extension monitoring configurations

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configurations:write

Grants permission to write (update/create/delete) extension monitoring configurations

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:configuration.actions:write

Grants permission to execute actions for extension

#### conditions:

* `extensions:host` - A string that uniquely identifies a single host for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:host-group` - A string that uniquely identifies a single host group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:ag-group` - A string that uniquely identifies a single ActiveGate group for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:management-zone` - A string that uniquely identifies a single management zone for monitoring configuration assignment  
  operators: `IN`, `=`
* `extensions:extension-name` - A string that uniquely identifies a single extension  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `!=`, `=`

### extensions:discovery.jmx:read

Grants permission to discover running Java processes via JMX and read their data through extensions

## geolocation

Geolocation Service

### geolocation:locations:lookup

Grants permission to lookup geolocations for IP adresses.

## hub

Hub provides catalog content, such as Dynatrace Apps, Extensions, and Technologies, in the context of the environment.

### hub:catalog:read

Grants permission to read the hub catalog content.

## hyperscaler-authentication

Hyperscaler authentication service

### hyperscaler-authentication:aws:authenticate

Grants permission to authenticate against AWS.

### hyperscaler-authentication:azure:authenticate

Grants permission to authenticate against Azure.

## iam

Identity and Access Management Framework.

### iam:service-users:use

Grants permission to use all or specified service users

#### conditions:

* `iam:service-user-email` - Service users emails  
  operators: `IN`, `=`

### iam:service-users:create

Grants permission to create a service user in the environment

### iam:bindings:read

Grants permission to read bindings

#### conditions:

* `iam:policyUuid` - Policy uuid in the URI.  
  operators: `=`, `IN`
* `iam:levelType` - Level type in the URI.  
  operators: `=`, `IN`
* `iam:boundGroup` - Group uuid in the URI.  
  operators: `=`, `IN`

### iam:bindings:write

Grants permission to create bindings

#### conditions:

* `iam:policyUuid` - Policy uuid in the URI.  
  operators: `=`, `IN`
* `iam:levelType` - Level type in the URI.  
  operators: `=`, `IN`
* `iam:boundGroup` - Group uuid in the URI.  
  operators: `=`, `IN`

### iam:policies:read

Grants permission to read policies

### iam:policies:write

Grants permission to create policies

### iam:boundaries:read

Grants permission to read boundaries

### iam:boundaries:write

Grants permission to create boundaries

### iam:effective-permissions:read

Grants permission to read effective permissions

#### conditions:

* `iam-param:entity-type` - Entity type in the query parameters. Allowed values: `group`, `user`.  
  operators: `=`
* `iam-param:entity-id` - Entity id of given entity-type in the query parameters.  
  operators: `=`, `IN`

### iam:limits:read

Grants permission to read limits

## insights

Business Insights Service

### insights:opportunities:read

Grants permission to read data from the Opportunity Insights API

### insights:moments:read

Grants permission to query value moments and related data

## mcp-gateway

MCP Gateway exposes MCP server capabilities in Dynatrace

### mcp-gateway:servers:invoke

Grants permission to invoke the MCP Gateway API

### mcp-gateway:servers:read

Grants permission to list the available MCP servers

## notification

API for sending notifications

### notification:self-notifications:read

Grants permission to read self notifications.

### notification:self-notifications:write

Grants permission to write self notifications.

### notification:notifications:read

Grants permission to read notification configurations.

### notification:notifications:write

Grants permission to write notification configurations.

## oauth2

Authorization of OAuth token issuing actions (token exchange)

### oauth2:clients:manage

Allows management of light OAuth clients

#### conditions:

* `oauth2:scopes` - Requested scopes for the generated OAuth clients  
  operators: `=`, `NOT IN`

## openpipeline

OpenPipeline

### openpipeline:configurations:read

Grants permission to read the OpenPipeline configuration

### openpipeline:configurations:write

Grants permission to write the OpenPipeline configuration

### openpipeline:events:ingest

Grants permission to ingest events into OpenPipeline

### openpipeline:events.custom:ingest

Grants permission to ingest events into custom endpoints of OpenPipeline

### openpipeline:security.events:ingest

Grants permission to ingest security events into OpenPipeline

### openpipeline:security.events.custom:ingest

Grants permission to ingest security events into custom endpoints of OpenPipeline

### openpipeline:events.sdlc:ingest

Grants permission to ingest software development lifecycle events into OpenPipeline

### openpipeline:events.sdlc.custom:ingest

Grants permission to ingest software development lifecycle events into custom endpoints of OpenPipeline

## platform-token

Permissions for platform-tokens

### platform-token:tokens:write

Enables write user's platform tokens.

## security-intelligence

Provides APIs for security intelligence (enrichment and contextualization)

### security-intelligence:enrichments:run

Allows execution of enrichments and discovery of integration apps.

## session-replay

Session Replay

### session-replay:resources:read

Grants permission to retrieve a session replay resource

## settings

Settings service

### settings:objects:read

Enables reading of settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.  
  operators: `IN`, `=`
* `settings:entity.hostGroup` - The host group attribute of an entity for which a setting is stored. This is e.g. useful to grant access to settings scopes of all hosts which belong to the same host group.  
  operators: `IN`, `=`, `!=`
* `settings:scope` - The exact scope identifier a setting object has or will have. This condition allows to grant access to the scope of e.g., an individual host. In this case the scope equals the entity identifier, e.g. HOST-48B8F52F33098830.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - The name of a management zone. This condition is applicable to either: any settings object that is allowed on the scope of an entity that can be matched into a management zone or settings objects of the schemas builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo and builtin:problem.notifications.  
  operators: `IN`, `=`, `startsWith`, `MATCH`
* `settings:dt.security_context` - The name of a security context. This condition is applicable to any settings object that is allowed on the scope of an entity that can have a security context assigned.  
  operators: `IN`, `=`, `startsWith`

### settings:objects:write

Enables writing of settings objects belonging to the schema

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.  
  operators: `IN`, `=`
* `settings:entity.hostGroup` - The host group attribute of an entity for which a setting is stored. This is e.g. useful to grant access to settings scopes of all hosts which belong to the same host group.  
  operators: `IN`, `=`, `!=`
* `settings:scope` - The exact scope identifier a setting object has or will have. This condition allows to grant access to the scope of e.g., an individual host. In this case the scope equals the entity identifier, e.g. HOST-48B8F52F33098830.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `environment:management-zone` - The name of a management zone. This condition is applicable to either: any settings object that is allowed on the scope of an entity that can be matched into a management zone or settings objects of the schemas builtin:alerting.maintenance-window, builtin:alerting.profile, builtin:anomaly-detection.metric-events, builtin:monitoring.slo and builtin:problem.notifications.  
  operators: `IN`, `=`, `startsWith`, `MATCH`
* `settings:dt.security_context` - The name of a security context. This condition is applicable to any settings object that is allowed on the scope of an entity that can have a security context assigned.  
  operators: `IN`, `=`, `startsWith`

### settings:schemas:read

Enables reading settings schemas

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema's schemaId property of the schema matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema's schemaId property of the schema matches.  
  operators: `IN`, `=`

### settings:objects:admin

Enables using admin-mode to access, change ownership and share permissions of any object. Admin-mode only bypasses the ownership check - so to do anything useful, settings:objects:read and/or settings:objects:write are needed as well.

#### conditions:

* `settings:schemaId` - A string that uniquely identifies a single settings schema. The identifier of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the object's schemaId property matches.  
  operators: `IN`, `=`, `!=`, `startsWith`, `NOT startsWith`
* `shared:app-id` - A string that matches an app identifier. Only applicable to objects of schemas that have been added via apps. The condition will match if the object's app-id property matches.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`
* `settings:schemaGroup` - A schema group that allows to address multiple individual schemas at once. The group of a schema can either be found via the dedicated schema endpoint in the Dynatrace Environment API or in the info box of a settings screen. The condition will match if the schema of the object has a schemaGroup property that matches.  
  operators: `IN`, `=`

## slo

SLO service

### slo:slos:read

Grants permission to read Service-Level Objectives

### slo:slos:write

Grants permission to write Service-Level Objectives

### slo:objective-templates:read

Grants permission to read Service-Level Objectives Templates

## state

Platform State Service

### state:app-states:read

Grants permission to read app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:app-states:write

Grants permission to write app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:app-states:delete

Grants permission to delete app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:read

Grants permission to read user-app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:write

Grants permission to write user-app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state:user-app-states:delete

Grants permission to delete user-app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## state-management

State Management - Clear app-states and user-app-states of specific apps.

### state-management:app-states:delete

Grants permission to delete all app-states

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state-management:user-app-states:delete

Grants permission to delete user-app-states of the current user

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

### state-management:user-app-states:delete-all

Grants permission to delete user-app-states of all users

#### conditions:

* `shared:app-id` - The ID of the app.  
  operators: `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `=`, `!=`

## storage

Grail

### storage:events:read

Grants permission to read records from the events-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:events:write

Grants permission to write events to Grail

### storage:metrics:read

Grants permission to read timeseries from the metrics-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:metric.key` - The identifier of a metric, grouping numeric measurements that share the same measurement semantics (i.e. were measured "the same way".)  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:metrics:write

Grants permissions to write metrics from Dynatrace classic to latest Dynatrace and vice versa

### storage:logs:read

Grants permission to read records from the logs-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:log.source` - The location where the log comes from.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:logs:write

Grants permission to write logs to Grail

### storage:entities:read

Grants permission to read records from entities

#### conditions:

* `storage:entity.type` - The type of the entity.  
  operators: `=`, `IN`, `startsWith`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`

### storage:spans:read

Grants permission to read records from the spans-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:bizevents:read

Grants permission to read records from the bizevents-table

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:smartscape:read

Grants permission to read smartscape nodes and edges from Grail

#### conditions:

* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:system:read

Grants permission to read records from all system tables (for example, `dt.system.events`).

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:buckets:read

Grants permission to read records from Grail buckets. Required additionally to a table permission.

#### conditions:

* `storage:table-name` - Table name of the bucket that can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:bucket-name` - Name of the bucket that can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:query-consumption` - If it is set to `INCLUDED`, the query returns data only from the configured included timeframe of buckets. If set to `ON_DEMAND`, it returns data from the entire timeframe. For any other value, the IAM statement is ignored. The included timeframe must be configured per bucket via the Storage Management API.  
  operators: `=`

### storage:fieldsets:read

Read data from fieldsets

#### conditions:

* `storage:table-name` - Name of the table from which fieldset(s) can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:bucket-name` - Name of the bucket from which fieldset(s) can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:fieldset-name` - Name of the fieldset(s) which can be accessed.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`

### storage:bucket-definitions:read

Grants permission to read bucket definitions from Grail

### storage:bucket-definitions:write

Grants permission to write bucket definitions to Grail

### storage:bucket-definitions:delete

Grants permission to delete bucket definitions from Grail

### storage:bucket-definitions:truncate

Grants permission to delete all records from a bucket (not delete the bucket itself) in Grail.

### storage:records:delete

Delete records in grail

### storage:files:read

Read data from files.

#### conditions:

* `storage:file-path` - Path of the file which can be accessed.  
  operators: `=`, `startsWith`, `IN`

### storage:files:write

Ingest data via REST API

#### conditions:

* `storage:file-path` - Path of the file which can be accessed.  
  operators: `=`, `startsWith`, `IN`

### storage:files:delete

Delete data via REST API

#### conditions:

* `storage:file-path` - Path of the file which can be accessed.  
  operators: `=`, `startsWith`, `IN`

### storage:filter-segments:read

Read filter-segments from grail

### storage:filter-segments:write

Write filter-segments in grail

### storage:filter-segments:share

Share filter-segments in grail

### storage:filter-segments:delete

Delete own filter-segments in grail

### storage:filter-segments:admin

Write and delete all filter-segments in grail

### storage:fieldset-definitions:read

Read fieldset definitions from grail

### storage:fieldset-definitions:write

Write and delete fieldset definitions in grail

### storage:application.snapshots:read

Read application.snapshots from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`

### storage:user.events:read

Read user.events from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:frontend.name` - The name of the frontend.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:user.sessions:read

Read user.sessions from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:frontend.name` - The name of the frontend.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:user.replays:read

Read user.replays from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

### storage:security.events:read

Read security.events from grail

#### conditions:

* `storage:bucket-name` - This condition reduces the effect of the record-level permission to a defined list of buckets.  
  operators: `=`, `!=`, `IN`, `NOT IN`, `startsWith`, `NOT startsWith`, `MATCH`
* `storage:event.kind` - Gives high-level information about what kind of information the event contains, without being specific to the contents of the event. Helps to determine the record type of a raw event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.type` - The unique type identifier of a given event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:event.provider` - Source of the event, for example the name of the component or system that generated the event.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.namespace.name` - The name of the namespace that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:k8s.cluster.name` - The name of the cluster that the pod is running in.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:host.name` - Name of the host.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.host_group.id` - Id of the host group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:dt.security_context` - Custom field for security context.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:gcp.project.id` - Google Cloud Platform Project ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:aws.account.id` - Amazon Web Services Account ID.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.subscription` - Azure subscription.  
  operators: `=`, `IN`, `startsWith`, `MATCH`
* `storage:azure.resource.group` - Azure resource group.  
  operators: `=`, `IN`, `startsWith`, `MATCH`

## unified-analysis

Unified analysis

### unified-analysis:screen-definition:read

Grants permission to read the screen definition of a unified analysis screen

## upgrade-assistant

SaaS Upgrade Assistant service

### upgrade-assistant:environments:write

Grants permission to use the SaaS Upgrade Assistant app

## vulnerability-service

Provides APIs to access vulnerabilities that are affecting customer environments

### vulnerability-service:vulnerabilities:read

Allows viewing vulnerabilities

### vulnerability-service:vulnerabilities:write

Allows modifying vulnerability related information

## Related topics

* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [IAM policy statement syntax and examples](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")
* [Grant access to Settings](/docs/manage/identity-access-management/use-cases/access-settings "Grant access to Settings")
* [Account Management API](/docs/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.")


---


## Source: migrate-roles.md


---
title: Upgrade role-based permissions to Dynatrace IAM policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles
scraped: 2026-02-18T05:55:59.557615
---

# Upgrade role-based permissions to Dynatrace IAM policies

# Upgrade role-based permissions to Dynatrace IAM policies

* Latest Dynatrace
* 11-min read
* Updated on Aug 20, 2025

Dynatrace version 1.266+

This guide defines and compares role-based access control (RBAC) and attribute-based access control (ABAC), and provides guidelines and recommendations to consider when planning your upgrade from RBAC to ABAC. Upgrade in this context means expressing classic RBAC permissions targeting the previous Dynatrace as statements within IAM policies. As is explained later, upgrading offers you multiple benefits.

The guide is primarily intended for use by account administrators wanting to take advantage of the power of the ABAC framework within the previous Dynatrace.

## What is ABAC?

ABAC is the preferred industry-wide access management framework because of its business-oriented and modern approach to defining security policies through logical, plain language.

It defines access to secure resources based on a combination of user, resource, action, and contextual attributes. It uses security policies as a mechanism to define access rules for resources.

### Understanding the Difference: RBAC vs ABAC

RBAC roles are typically created to map work functions, such as department, seniority, or work assignment. RBAC permissions typically grant all-or-nothing access to resources based on pre-defined static roles.

For example, assigning "View Logs" permission to a group in Dynatrace grants users in that group the ability to view all captured logs. There is no ability to further refine their access to the logs.

* Various user, resource, and contextual information is not considered in classic RBAC.
* RBAC roles do not adapt well to changing access permission requirements and the dynamic nature of the attributes of the resources being secured.

ABAC, on the other hand, determines user access by evaluating resource, data, user, and contextual attributes, along with the specific user action being requested. This provides for a flexible permissions framework that handles changes in access requirements in a more dynamic way, rather than relying on static RBAC roles. Furthermore, the access control granularity offered makes it possible to design common or complex access requirements.

Dynatraceâs IAM permissions framework uses these core ABAC principles and further enhances them with features like [policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating"), [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users."), and [default policies](/docs/manage/identity-access-management/permission-management/default-policies#default-policies "Dynatrace default policies reference") to make our implementation of ABAC more flexible and user friendly.

### ABAC implementation in your Dynatrace

The Dynatrace IAM permissions framework currently supports the classic RBAC as well as the newer, ABAC, which leverages security policies to define permissions. Security policies are stand-alone components of the ABAC framework that allow combining one or many policy statements to define conditional access to your Dynatrace resources.

The access permissions defined in a security policy take effect when that policy is bound to a group, thus directly controlling the permissions of the users of that group. For simplicity, we will refer to security policies as simply policies for the remainder of this guide.

The following diagram captures the relationship between users, groups, policies, and policy boundaries.

![Users-Groups-Policies-Boundaries](https://dt-cdn.net/images/user-group-policy-boundary-812-75ea55d16b.png)

[Policies](/docs/manage/identity-access-management/permission-management "Permission management") leverage user, resource, data, and contextual attribution to enable you to configure access to your Dynatrace secure resources. You can secure individual data resources, apps, and services while optionally specifying business-specific access control conditions through the expressiveness of the [policy statements syntax](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.").

One or many policy statements can be combined into one policy. The policy can then be bound to one or many user groups, ultimately granting the users of those group the resource access defined by the policy.

For example, the Dynatrace ABAC policy below grants the ability to install or delete (action) custom apps (resource) where (condition) app identifier (resource attribute) is prefixed with "custom" (attribute value):

```
ALLOW app-engine:apps:install, app-engine:apps:delete WHERE shared:app-id startsWith âcustomâ;
```

The next example leverages additional contextual information (the time of the day) to restrict the ability to run apps only within business working hours.

```
ALLOW app-engine:apps:run WHERE shared:app-id = "dynatrace.automations" and global:time-of-day > "09:00+01:00" AND global:time-of-day < "17:00+01:00";
```

Classic RBAC roles can also be expressed in policies. For example, the policy statement below grants environment access but only for a specific management zone.

```
ALLOW environment:roles:viewer WHERE environment:management-zone=âmgmt-euâ
```

The ability to include classic RBAC roles in your policy statements is a very important feature of ABAC policies to help you transition from RBAC.

The true power of the Dynatrace ABAC framework lies in its ability to dynamically target individual or groups of platform resources, while optionally combining available attributes to further narrow down access parameters using the expressive nature of policy statement syntax.

### Benefits of upgrading to ABAC

Dynatraceâs ABAC permissions framework offers the following advantages:

#### Security and compliance

* Policies enable admins to adopt the [principle of least privilegeï»¿](https://en.wikipedia.org/wiki/Principle_of_least_privilege)
* Policies provide a better framework to adhere to your IT compliance standards

#### Flexibility

* Policies are built to be adaptable to changes and future platform services
* [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") are managed by Dynatrace and automatically adapt to future platform changes
* Multiple policy statements can be combined to form one policy, allowing administrators to build policies that align with their access control business requirement

#### Scalability

* Policies allow for a concise expression of complex permissions
* Policy boundaries offer further policy optimization and generalization
* [Policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating") enables parameterization of policies through binding parameters

#### Granularity

* Each policy statement can target one or many platform resources
* `WHERE` conditions can be appended to statements to further limit access

#### Usability

[Policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") can be re-used in multiple policies.

* Default policies give a great starting point for common access scenarios

#### Futureproofing

* ABAC is here to stay and will continue to be developed and extended.

## RBAC to ABAC upgrade planning

The following upgrade guide recommends a strategy and best practices to consider when planning and executing your upgrade from RBAC to ABAC.

If you use management zones for access control, this guide offers examples of how to refer to management zones within policies so that you can remove the corresponding RBAC assignments. This guide does not cover how to migrate your use of management zones into Grail permissions.

### Upgrade guidelines

The upgrade strategy you choose will depend on your current Dynatrace configuration.

The general strategy is to:

1. Identify RBAC permissions that you have currently configured with your groups.
2. Define a mapping on how those RBAC permissions map to ABAC permissions that can be implemented in policies.

   * You can repeat doing this in batches until you cover all your groups.
   * Where appropriate, consider using [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") rather than building custom policies.

You can use these sample [Dynatrace Notebook or this PowerShellï»¿](https://community.dynatrace.com/t5/Dynatrace-tips/RBAC-to-ABAC-migration-helper-scripts-Notebook-and-PowerShell/m-p/257807#M1447) scripts to give you an initial assessment and some recommendations to get you started. We will use the script output from our sample Dynatrace environment to illustrate some important concepts and best practices you should consider as you plan your RBAC upgrade to ABAC.

Note that any automation scripts that you might have built that use RBAC permissions will also have to be reviewed for potential changes in the event that you transition to solely using ABAC for your access control.

### Your Dynatrace RBAC assessment

An upgrade plan should start with an assessment of your current RBAC configuration. This means identifying existing RBAC roles assigned to your groups. We are interested in RBAC role assignments that are scoped to target environments or management zones.

Consider the steps below to conduct an initial assessment. You can use the Account Management portal to complete the steps or [import](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and use the provided notebook to help you. Alternatively, you can also use the provided PowerShell script.

1. Create the required OAuth client in the [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.") portal with permissions as instructed in the notebook.
2. Import the provided **RBAC Assessment** notebook into your Dynatrace or, if itâs more convenient for you, use the provided PowerShell script.
3. Run the script.
4. The output will be a table like the example below:

| permissionName | scope | scopeType | mgmtzone\_name | group\_name | abacRole | recommended\_policy |
| --- | --- | --- | --- | --- | --- | --- |
| tenant-replay-session-with-masking | xyz:mgmt\_na\_east | management-zone | mgmt\_na\_east | group\_na\_supp | `environment:roles:replay-sessions-with-masking` | Dynatrace Professional |
| tenant-replay-session-without-masking | xyz:mgmt\_na\_east | management-zone | mgmt\_na\_east | group\_na\_supp | `environment:roles:replay-sessions-without-masking` | Dynatrace Professional |
| tenant-manage-settings | xyz:mgmt\_na\_east | management-zone | mgmt\_na\_east | group\_na\_supp | `environment:roles:manage-settings` | Dynatrace Professional |
| â¦ | â¦ | â¦ | â¦ | â¦ | â¦ | â¦ |
| tenant-replay-session-with-masking | xyz:mgmt\_na\_west | management-zone | mgmt\_na\_west | group\_na\_supp | `environment:roles:replay-sessions-with-masking` | Dynatrace Professional |
| tenant-replay-session-without-masking | xyz:mgmt\_na\_west | management-zone | mgmt\_na\_west | group\_na\_supp | `environment:roles:replay-sessions-without-masking` | Dynatrace Professional |
| tenant-manage-settings | xyz:mgmt\_na\_west | management-zone | mgmt\_na\_west | group\_na\_supp | `environment:roles:manage-settings` | Dynatrace Professional |
| â¦ | â¦ | â¦ | â¦ | â¦ | â¦ | â¦ |

### Upgrade to ABAC

With the inventory of assigned RBAC permissions already created, you can now map RBAC permissions to ABAC ones. You should give priority to existing [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") whenever possible, as opposed to building your own custom policies.

We will use âgroup\_na\_suppâ to help us illustrate some key best practices you should consider for your ABAC configuration.

This group currently has the following RBAC permissions scoped to two management zones âmgmt\_na\_eastâ and âmgmt-na\_westâ:

| RBAC Role Name | ABAC role name |
| --- | --- |
| tenant-replay-session-with-masking | `environment:roles:replay-sessions-with-masking` |
| tenant-replay-session-without-masking | `environment:roles:replay-sessions-without-masking` |
| tenant-manage-settings | `environment:roles:manage-settings` |
| tenant-view-sensitive-request-data | `environment:roles:view-sensitive-request-data` |
| tenant-view-security-problems | `environment:roles:view-security-problems` |
| tenant-manage-security-problems | `environment:roles:manage-security-problems` |
| tenant-log-viewer | `environment:roles:logviewer` |

If we were to create a new custom policy to assign those permissions, we could write the following policy statement:

```
ALLOW  environment:roles:replay-sessions-with-masking, environment:roles:replay-sessions-without-masking, environment:roles:manage-settings, environment:roles:view-sensitive-request-data , environment:roles:manage-security-problems, environment:roles:logviewer



WHERE environment:management-zone startsWith "mgmt_na";
```

We could then bind this policy to the `group_na_supp` group and remove the old RBAC role assignment from the group. To further optimize our new ABAC permission, we could use **Dynatrace Professional** rather than building a custom policy. Because [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") are read-only, we would need a mechanism to append our `WHERE` condition above.

This is where [policy boundaries](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.") come into play. We can store the condition `environment:management-zone startsWith "mgmt\_na";` in a policy boundary and then use it with our group, as we bind the group to the **Dynatrace Professional** policy, thus further restricting this permission assignment using the boundary we created.

First, letâs create the policy boundary. In [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health."), under **Identity & Access management** > **Policy management**, we can create a policy boundary specific to North America management zones.

![Boundaries](https://dt-cdn.net/images/boundaries-468-08355e2a83.png)

Next, we assign the default policy **Dynatrace Professional** to the `group_na_supp` and apply the boundary we just created.

![Permission Assign](https://dt-cdn.net/images/permissionassign-936-e6e96537be.png)

As may be obvious from this example, policy boundaries make it possible to extract your business-specific access requirements out of the policy and into a standalone unit that can be re-applied over and over across multiple policies. Policy boundaries can be assigned to one or many group-to-policy bindings, making them reusable. The combination of default policies with policy boundaries has the potential to further simplify your permissions configuration.

Best practice

Make use of [default policies](/docs/manage/identity-access-management/permission-management/default-policies "Dynatrace default policies reference") whenever possible and define your business-specific access conditions in policy boundaries.

### When should you create custom policies

Rather than creating new custom policies, administrators are strongly encouraged to primarily leverage default policies, which are built and managed by Dynatrace and already encapsulate the necessary policy statements for typical access scenarios. When assigning these default policies to groups, you can then further restrict the permissions by using policy boundaries.

In cases where default policies do not meet your specific permission requirements, or when you might want to restrict them with some specific `DENY` statements, you can then build custom policies.

Best practice

Build your own custom policies only when provided default policies don't fit your requirements or when you want to further limit default policies.

### Testing and validation

We recommend mocking up groups and users and testing separately, ideally in a sandboxed environment if possible.

Also, Dynatraceâs Enterprise API could be used to provide useful permissions information for specific users or groups. For example, the following GET request to `https://api.dynatrace.com` will return current permissions for a specific user:

```
`https://api.dynatrace.com/iam/v1/resolutionaccount/:accountIdHere/effectivepermissions?entityType=user\&entityId=:userIdHere`
```

### Deployment

Deploy policies in a phased approach to minimize user access disruptions. You may choose to do these in batches of groups or some other way more appropriate to your setup.

Best practice

Consider deploying your changes in batches rather than all at once.

### Monitoring and tuning

Monitor your ABAC permissions over time to see if they have adversely affected user access and adjust accordingly.

### Upgrade support

Refer to our online documentation and Dynatrace Community forums for additional help during your upgrade from RBAC to ABAC. Additionally, make use of Dynatraceâs support channels for more targeted help.

### Final checklist

1. Compile your existing RBAC roles and group assignments

   * Identify and plan to replace any custom automation still relying on RBAC
2. Design your ABAC policies:

   * Use default policies whenever suitable
   * Create policy boundaries to capture your specific business logic
3. Decide on an upgrade strategy

   * Consider a phased rather than a big-bang approach by introducing changes in multiple batches
4. Test your upgrade

   * Use a sandbox environment if available to test the effects of your new ABAC-only configuration
   * Try upgrading a select set of groups first
5. Monitor the effects of your upgrade to catch and correct any misconfigurations

## Related topics

* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")
* [IAM policy statement syntax and examples](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")


---


## Source: iam-policy-boundaries.md


---
title: Policy boundaries
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries
scraped: 2026-02-18T05:43:50.167415
---

# Policy boundaries

# Policy boundaries

* Latest Dynatrace
* 6-min read
* Published Sep 01, 2024

With policy boundaries, you can assign permissions with fine-granular restrictions on the data level.

Policy boundaries enable to restrict user permissions on the record and resource level and are intended to work very well with the Dynatrace default policies.

## What are policy boundaries?

Policy boundaries allow you to bundle restrictions on the record and/or resource level together for usage in your permission assignments. This allows for easier management of partitions on the data level and enables re-usability. Boundaries alone don't restrict anything, they are always used together with policies in the process of assigning policies to your user groups.

Whenever a boundary is selected in combination with a security policy, it further restricts the existing policy, which can also result in no access for the user.

Policy boundaries support all conditions that are available in the [IAM reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Boundaries and default policies

**Use case**:

As an account admin I would like to restrict the **Read logs** default policy for 20 user groups to logs from K8s development namespace.

**Solution**:

1. Create a boundary **K8s DEV** with the following content:

   * `storage:k8s.namespace.name = "DEVELOPMENT";`
2. Select the boundary when you assign the **Read Logs** default policy to your user groups.

   * The boundary is automatically applied to all permissions where it fits and therefore restricts log access.

If you ever want to adopt the boundary because your access requirements have changed, for example you introduce another stage in your development process, you just need to change the boundary like so:

`storage:k8s.namespace.name IN ("DEVELOPMENT","HARDENING");`

### Technical details about boundaries

Boundaries allow you to decouple the "What" and "Where" of a policy.

In other words, enable you to externalize the conditions to a separate object for easier management and re-usability.

`ALLOW <permissions> WHERE <conditions>`

* **What** being the permissions part of the policy that defines which APIs you are allowed to use
* **Where** being the service related fine granular permissions on record/resource-level expressed by the policy conditions.

This mechanism is extremely useful in combination with the [default policies](/docs/manage/identity-access-management/permission-management/default-policies#default-policies "Dynatrace default policies reference").

The default policies define a set of permissions to access features and data. As they are generic, they don't restrict the access to a specific records and resources.

**Example**:

The `storage:k8s.namespace.name IN ("DEV","PREPROD")` is a recurring pattern in your policies and can be externalized into a policy boundary.

```
ALLOW storage:logs:read WHERE storage:k8s.namespace.name IN ("DEV","PREPROD");



ALLOW storage:metrics:read WHERE storage:k8s.namespace.name IN ("DEV","PREPROD");
```

Boundary **K8s-dev-preprod**:

`storage:k8s.namespace.name IN ("DEV","PREPROD");`

Of course, this is a basic example and your boundary could consist of more statements that exactly define to what records and resources your users have access.

## Working with policy boundaries

The boundary management operations listed below are all performed using the **Account Management** pages.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.

   This opens `https://myaccount.dynatrace.com/`, which you can bookmark for easy access to Account Management.
2. Go to **Identity & access management** > **Policy management**.
3. On the policy management screen you find two tabs for **Policies** and **Boundaries** on top.
4. Select **Boundaries** to open the boundary management screen.

### Create a new policy boundary

1. Select  **Boundary** and specify:

   * **Boundary Name**
   * **Boundary query**

     + Here you provide your conditions in textual format. One line per condition, no logical operators allowed.
2. Select **Save** to create your boundary.

### Edit a policy boundary

1. Find the policy boundary that you want to edit in the list overview.
2. In the Actions column, select  > **Edit boundary**.
3. Adopt the boundary to your requirements and click **Save**.

   * A change in the boundary will have an immediate effect on the user permissions that are assigned with this boundary.

### Delete a policy boundary

1. Find the policy boundary that you want to edit in the list overview.
2. In Actions column, select  > **Delete boundary**.
3. In the Confirmation dialog click **Cancel** to abort or **Delete** to confirm.

Deletion of used boundaries

A boundary that is used in policy bindings can not be deleted. Before you can delete the boundary you have to adjust or remove all bindings where the boundary is used.

### Assignment of a policy boundaries during permission assignment

1. To assign a boundary please configure your group permissions as described in [Group management](/docs/manage/identity-access-management/user-and-group-management/access-group-management#manage-group-permissions "Manage Dynatrace groups and their permissions.").
2. Select one or multiple boundaries that should be applied to your permission assignment.

   * To learn about how boundaries are applied to your policy permissions, see the [How are policy boundaries applied?](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries#apply-boundary "Restrict security policies with policy boundaries to provide tailored access to your users.") section below.

Boundaries assignment

Policy boundaries can only be assigned to policies, they are not compatible with role-based permissions.

## How are policy boundaries applied?

Boundaries work for all services that are covered with the security policies and which are documented in the [IAM Policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

When a policy binding contains boundaries the effective policy is calculated according to the following rules:

* Only conditions added to service configuration will be applied to relative permissions. This rule doesn't apply to global conditions. Global conditions will be applied to all permissions
* When a boundary contains repeated condition names, then each policy statement is multiplied by such conditions. Each of the repeated conditions appears separately in each applicable statement.
* When more than one boundary applies to a policy, then effective statements are calculated for each boundary separately

In certain configurations this may cause unintended unconditional access. For example when this policy:

```
"ALLOW storage:logs:read, storage:entities:read;"
```

is bound to boundary one:

```
storage:host.name="myHost"
```

and boundary two:

```
storage:dt.security_context="mySC"
```

will produce:

```
ALLOW storage:entities:read;



ALLOW storage:entities:read WHERE storage:dt.security_context = "mySC";



ALLOW storage:logs:read WHERE storage:host.name = "myHost";



ALLOW storage:logs:read WHERE storage:dt.security_context = "mySC" `
```

which would effectively grant unconditional read access to storage entities, as boundary one's condition of `storage:host.name="myHost"`does not apply to permission `storage:entities:read`.

* When a policy statement contains multiple permissions, then such a statement will be split into single permission statements
* Boundaries are applied to policy statements without evaluating the statement's condition. Boundary will be applied no matter if the statement already contains the same condition
* Boundaries don't apply to `DENY` statements

## Expressing management zones inside of policy boundaries

To use your management zones inside of boundaries you just need to reference them as a condition in your policy boundary.

Boundary **Kubernetes**:

```
environment:management-zone startsWith "[Kubernetes]";



storage:k8s.namespace.name IN ("DEV","PREPROD");
```

This boundary includes all management zones that start with `[Kubernetes]`, as well as all the records stored in Grail for the `DEV` and `PREPROD` K8s namespaces.

Be aware that the management zones referenced in your boundaries only apply to policy statements that support management zones.

Grail does not support management zones but uses the `storage:` fields for record level access control. For more details see [What is the difference between management zones and new IAM policies?](/docs/platform/upgrade#access-control "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.")

## Restrictions and limits of policy boundaries

* Only 10 restrictions per boundary, to keep them manageable. If you need more restrictions for your use case, create more boundaries and [assign multiple boundaries](/docs/manage/identity-access-management/iam-limits "IAM limits for Dynatrace SaaS") to the policy.
* Boundaries are only compatible with security policies. No role-based support.
* Boundaries don't support the AND operator, every line of a boundary can only consist of one condition.

  + If you need logical operators and also want to re-use your policy definitions please take a look into [policy templating](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policy-templating "Policy templating").


---


## Source: iam-policy-mgt.md


---
title: Manage IAM policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt
scraped: 2026-02-18T05:41:59.539386
---

# Manage IAM policies

# Manage IAM policies

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Aug 20, 2025

Use these procedures in the Dynatrace web UI to manage Dynatrace [IAM](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") policies.

API alternative

To instead use the API to manage IAM policies, go to [Dynatrace Account Management API 1.0ï»¿](https://dt-url.net/vr03thr).

## List IAM policies

To list configured IAM policies

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Review the table of all existing policies that you can bind to user groups.

   * **Name**âthe name of the policy
   * **Description**âa brief description of the policy
   * **Source**â`global`, `account`, or `environment`
   * **Actions**âview, edit, or delete that row's policy (actions available to you depend on your permission level)

### Default policies

To let you use policies right away, Dynatrace IAM is shipped with built-in global policies.

* On the **Policies** page, in the **Source** column, they're all set to `Dynatrace`
* They're predefined and managed by Dynatrace
* You can apply a built-in policy by [assigning it to a group](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies") for the whole account or to any environment.
* You can inspect themâselect **View policy** in the **Actions** columnâbut you can't edit them

## Create a policy

To create a policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Select **Create policy**.
3. Enter the following information.

   Element

   Description

   Name

   The name of the policy.

   Description

   A brief description of the policy.

   Organization level

   Each policy has a level that determines its scope:

   * `global`: These policies are predefined and managed by Dynatrace, and they apply to all accounts and environments. They cannot be edited.
   * `account`: These policies apply to all environments under that account (customer). Use them to set company-wide policies.
   * `environment`: These policies apply only to a single customer environment.

   Organization levels are restricted in the UI to the `account` level (other levels are still available via API).
   Restriction in UI was provided to avoid confusion between *creating* and *binding*.
   Commonly creating multiple identical policies on the `environment` levels can be achieved in a more efficient way by defining one policy on the `account` level and binding it to `environment` levels.

   Policy statement

   A statement specifying exactly what this policy allows.

   Example: Policy for Settings 2.0 Write

   ```
   ALLOW settings:objects:read;



   ALLOW settings:objects:write;



   ALLOW settings:schemas:read;
   ```

   You can combine multiple permissions in a single statement. Here is the same example combined into a single statement:

   ```
   ALLOW settings:objects:read, settings:objects:write, settings:schemas:read;
   ```

   Combining statements is particularly useful for managing policies with complicated conditions.

### Services

For a complete and up-to-date list of Dynatrace services that support permission management via IAM policies, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Edit a policy

To edit an existing policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Find the policy you want to edit.  
   You can filter and sort the table.
3. Select **Actions** > **Edit policy**.
4. Make your changes and select **Save**.

## Delete a policy

To delete a policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Find the policy you want to delete.  
   You can filter and sort the table.
3. Select **Actions** > **Delete** for the policy.

## Copy a policy

To copy an existing policy

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Policy management**.
2. Find the policy you want to copy.  
   You can filter and sort the table.
3. Select the **Edit** button for the policy.
4. Copy the contents of **Policy statement** to the clipboard.
5. Go back to the **Policies** page.
6. Select **Create policy**.
7. Paste the copied policy statements into **Policy statement**.
8. Fill in the **Name** and optional **Description**.
9. Select **Create policy**.

## Apply a policy to a group

To apply a policy to a group, you need to bind the policy to the group. For details on managing group permissions with IAM, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").


---


## Source: manage-user-permissions-policies.md


---
title: Working with policies
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies
scraped: 2026-02-18T05:43:03.622573
---

# Working with policies

# Working with policies

* Latest Dynatrace
* Explanation
* 9-min read
* Updated on Aug 20, 2025

Use Dynatrace identity and access management (IAM) to manage user access to Dynatrace features.

With the IAM framework, you can define policies that clearly specify whether an action in Dynatrace is allowed. When policies are bound to user groups, they describe an access pattern for the group that is enforced at runtime. This gives you much more fine-grained control over how your users interact with Dynatrace.

## Basic

[### Manage IAM policies

List, create, delete, and copy policies using the Account Management.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-mgt "Create, edit, copy, and delete IAM policies for managing Dynatrace user permissions.")[### Create your policies

Learn the policy statement syntax and see the example custom policies.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policystatement-syntax "IAM policy statement syntax.")[### Policy boundaries

Boundaries allow you to further restrict policies.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries "Restrict security policies with policy boundaries to provide tailored access to your users.")

## Advanced

[### Global conditions

You can apply global conditions to any policy statement because they are not service-specific.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-conditions "Policy global conditions")[### Global attributes

Apply attributes to certain global conditions, usable in the policy syntax without extra configuration.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-global-attributes "Policy global attributes")[### Migrate role-based permissions

Dynatrace security policies now support the classic role-based permissions, learn how to migrate them.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/migrate-roles "Manage access to a Dynatrace environment using security policies.")

## Reference

[### IAM permissions reference

A complete list of all supported IAM permissions across all Dynatrace services.](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")[### Policy management API

Manage the policies at scale using the policy management API.](/docs/dynatrace-api/account-management-api/policy-management-api/policies "Manage access policies in your Dynatrace account via the Policy management API.")


---


## Source: management-zone-rules.md


---
title: Management-zone rules
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules
scraped: 2026-02-16T21:25:22.167738
---

# Management-zone rules

# Management-zone rules

* How-to guide
* 16-min read
* Updated on Oct 03, 2025

Management zones comprise one or more rules that define and limit the entities or dimensional data (such as logs and metrics) that can be accessed within the management zone.

When you select a management zone in **Settings** > **Preferences** > **Management zones**, all configured rules are displayed. You can **Disable/Enable** individual rules.

![Management zone rules](https://dt-cdn.net/images/mz-rules-1a-1227-bcb209a202.png)

Read more about:

* How log data can be ingested and automatically assigned to management zones in [Management zones and ingested log data (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.").
* How to [add a service-level objective to a management zone](/docs/deliver/service-level-objectives-classic/configure-and-monitor-slo#mz "Create, configure, and monitor service-level objectives with Dynatrace.") so users with access to the management zone can view SLO status and error budget in the **Service-level objectives** page.

## Rule types

Management zones offer **UI-based rule definition** for:

* [Monitored entities](#ui)
* [Dimensional data (logs and metrics)](#logs-metrics)

You can select the type of rule, and then create rule conditions based on entity/data properties, operators, and values where relevant.

When creating rules for some entities, you can propagate access to related topological entities without creating an extra rule. See [How management-zone rules are applied](#rules-apply) below.

For UI-based rules for dimensional log and metric data, you can define conditions based on the log file name, metric keys and dimension keys and values. Built-in, calculated, and ingested metrics are supported.

More information on the Metrics API v2

Use the powerful [metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.") of the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") for metric and dimension keys and values:

* [GET a list of all available metrics](/docs/dynatrace-api/environment-api/metric-v2/get-all-metrics "List all metrics available in your monitoring environment via Metrics v2 API.") in your environment.
* [GET the details of a specified metric](/docs/dynatrace-api/environment-api/metric-v2/get-descriptor "View the descriptor of a metric via Metrics v2 API.") to check dimension keys.
* [GET a list of data points](/docs/dynatrace-api/environment-api/metric-v2/get-data-points "Read data points of one or multiple metrics via Metrics v2 API.") to check dimension values.

Note that users automatically get access to logs and metrics associated with entities that are included within their assigned management zones.

**[Text-based rules](#text)** leverage the powerful [entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") for v2 Environment APIs to define entities. Text-based rules enable you to define entity access based on all the entity types, properties, values, and relationships exposed by the [Monitored entities API v2](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.").

There are several advantages of text-based rules.

* You can provide granular and focused entity definitions without having to review the subset of choices available in the UI.
* While UI-based rules allow for some relationship-based [propagation of entity access](#rules-apply), with text-based rules, you can explicitly use relationships to filter your entity selection. You have the flexibility to decide exactly which relationships you want to use to filter entities.
* You can define text-based rules for including your own custom entity types, attributes, and relationships in management zones.

Per monitoring environment, you can add:

* 5,000 management zones by default. For any questions, contact a Dynatrace product expert via live chat.
* 300 UI-based management-zone rules for entities (150 for Dynatrace versions 1.323 and earlier).
* 300 UI-based management-zone rules for dimensional data (150 for Dynatrace versions 1.323 and earlier).
* 300 text-based entity selector rules for management zones (150 for Dynatrace versions 1.323 and earlier).
* 100,000 conditions for all management-zone rules taken together (does not apply to [entity selector rules](/docs/manage/identity-access-management/permission-management/management-zones/management-zone-rules#text "Define rules to limit the entities accessible within a management zone.")).
* Any individual entity to a maximum of 200 management zones (run the [GET an entity](/docs/dynatrace-api/environment-api/entity-v2/get-entity "View parameters of a monitored entity via Dynatrace API.") API call to see an entity's management zones).

Check our documentation on [how to optimize management-zone rule performance at scale](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.").

### Add a UI-based rule for entities

See [Examples](#examples) for different rule types and implementations.

1. [Select/create a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") and then select **Add a new rule**.
2. Select **Monitored entity** as the **Rule type**. (See also information on [rules for dimensional data](#logs-metrics) and [text-based rule definition](#text) via the **Entity selector**.)
3. Select the entity type to which the rule should apply (**Rule applies to**), for example, **Web applications**.

   ![Select an entity type](https://dt-cdn.net/images/mz-rules-entity-type-571-8a758524db.png)
4. Each entity can be defined and limited by several different conditions. Select **Add condition**.
5. Choose the condition **Property**, **Operator**, and **Value** (where relevant). For example, you can specify that the **Web application name begins with** a specified string. You can enter up to 80 characters; wildcard characters are not allowed; regular expressions are allowed in the **contains regex** and **does not contain regex** condition operators.
6. If you enter a text string, specify whether it is **Case sensitive**.

   ![Rule conditions](https://dt-cdn.net/images/mz-rules-3a-958-3a6e99d6a0.png)
7. For some entities, you can propagate access to related topological entities without creating an extra rule. For example, turn on the appropriate toggles to include underlying hosts and process groups when defining a management-zone rule for **Services**.

   ![Include related entities](https://dt-cdn.net/images/mz-rules-4a-879-f4b10ae36b.png)
8. Select **Add condition** to add another condition (or **Remove condition** to remove a condition) as required.

   * You need to define at least one condition per rule.
   * Conditions are applied using the `AND` logicâall conditions need to be met for the rule to apply to an entity.
   * There's no limit on the number of conditions per rule. However, there's a limit of 100,000 conditions for all rules taken together per environment.
9. Select **Preview** to see entities matching the rule that were active and online in the last 72 hours. Of course, when you actually apply the management zone, all entities matching the rules for the given timeframe will be displayed. Note that **Preview** is only available for entity-based rules.

   ![Rule preview](https://dt-cdn.net/images/mz-rules-5a-957-2b8d1b7d14.png)
10. **Save changes**.

### Add a UI-based rule for dimensional data

See [Examples](#examples) for different rule types and implementations.

1. [Select/create a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") and then select **Add a new rule**.
2. Select **Dimensional data** for **Rule type**. (See also information on [rules for entities](#ui) and [text-based rule definition](#text) via the **Entity selector**.)
3. Select the data **Type** to which the rule should apply.

   * For a UI-based rule for a built-in, calculated, or ingested metric, select **METRIC**.
   * For a UI-based rule for logs, select **LOG**.
4. Each rule can be defined and limited by several different conditions. Select **Add condition**.
5. Choose the condition **Type**, **Key** (where appropriate), **Operator**, and **Value**. You can enter up to 80 characters in any text field; wildcard characters are not allowed.

   Condition types are:

   * For a log attribute or metric dimension, **DIMENSION**.

     ![Log attribute or metric dimension condition](https://dt-cdn.net/images/mz-rules-data-dimension-580-3843630e79.png)
   * For a log filename, **LOG\_FILE\_NAME**. The log filename should match the attribute `log.source`.

     ![Log filename condition](https://dt-cdn.net/images/mz-rules-log-filename-580-7f89e2cbd4.png)
   * For a metric key, **METRIC\_KEY**.

     ![Metric key condition](https://dt-cdn.net/images/mz-rules-metric-key-580-fac4735560.png)
   * For a combined log or metric condition, **ANY**.

   Allowed operators are **begins with** and **equals**.
6. Select **Add condition** to add another condition (or **Remove condition** to remove a condition) as required.

   * You need to define at least one condition per rule.
   * Conditions are applied using the `AND` logicâall conditions need to be met for the rule to apply to an entity.
   * There's no limit on the number of conditions per rule. However, there's a limit of 100,000 conditions for all rules taken together per environment.
   * **Preview** is not available for dimensional-data rules.
7. **Save changes**.

### Add a text-based entity selector rule

1. [Select/create a management zone](/docs/manage/identity-access-management/permission-management/management-zones/set-up-management-zones "Create and assign access rights to management zones.") and then select **Add a new rule**.
2. In **Rule type**, select **Entity selector**.
3. To fill out the **Entity Selector** text string, you might need to run [Monitored entities API v2 calls](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") to fetch entity types, properties, values, and relationships. Consult [entity selector documentation](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.") for details on how to construct an entity definition. See [Examples](#examples) for different rule types and implementations.

   **Important parts of the entity selector string**

   * `type(<entityType>)` defines the type of entity that is subject to the rule. For example, the entity type for hosts is `host` and for process groups is `process_group`. The entity type is not case sensitive. You can only provide a single entry in `<entityType>`.

     Run the [GET all entity types](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") API call for a list of all entity types in your environment (including custom entities) and their properties.

     Alternatively, you can specify multiple individual entity IDs with the `entityId` criterion. You can run the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") API call for a list of actual entities in your environment and their properties.
   * Entity properties and values filter the entity list that your rule applies to. For example:

     + `entityName.startsWith("Book")` filters for entities whose name starts with `Book`.
     + `serviceType(WEB_REQUEST_SERVICE)` filters for web request services.

     You can run the [GET entity type API call](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") for any entity type (for example, `service`) to get a list of all its properties (for example, `serviceType`). You can also run the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") API call for a list of actual entities in your environment with their property values (for example, `WEB_REQUEST_SERVICE`).
   * Relationships further refine entity selection by defining an entity in terms of its relationship to another. Relationships are of two kinds.

     + A `fromRelationship` implies that the direction of the relationship is **from the given entity** (that is, the entity being queried) to a related entity. When you query all the services that service A calls, this is a relationship âfrom (service A)â to other services.
     + A `toRelationship` implies that the direction of the relationship is from a related entity **to the given entity** (that is, the entity being queried). When you query all the services that call service A, this relationship is âto (service A).â

     You can run the [GET entity type API call](/docs/dynatrace-api/environment-api/entity-v2/get-entity-type "View the details of a monitored entity type via Dynatrace API.") on any entity type to get a list of the entity's from/to relationships and the related entity types. You can also run the [GET entities list](/docs/dynatrace-api/environment-api/entity-v2/get-entities-list "View a list of monitored entities via Dynatrace API.") API call to get a list of the actual entities in your environment along with their relationship values (for example, a `service` entity type can have a `calls` "from relationship" to another `service`).
4. Select **Preview** to see entities matching the rule that were active and online in the last 72 hours. (Of course, when you actually apply the management zone, all entities matching the rules for the given timeframe will be displayed.)

   ![Entity-selector rule preview](https://dt-cdn.net/images/mz-rules-6a-998-ebeb2f11bd.png)
5. **Save changes**.

## How management-zone rules are applied

* Conditions are applied using the `AND` logicâall conditions within a rule need to be met for the rule to apply to an entity.
* Rules are applied using the `OR` logicâany rule must apply for an entity to be included in a management zone.
* When creating rules for some entities, you can propagate access to related topological entities without creating an extra rule. For example, when creating a rule for services, you can opt to add underlying hosts and process groups. See [Add a UI-based rule](#ui) above.

  In other cases, the propagation of access to related topological entities is implicit. For example, when you grant access to a host in a management zone, any custom metrics ingested via that host are also accessible within the management zone. Note that this does not automatically include all measurements of those custom metrics but only those measurements that were sent in for your host.

  In cases where such propagation isn't available, you need to explicitly create rules for the entities you wish to add to a management zone. For example, a management-zone rule that applies to **Host groups** does not automatically grant access to the hosts within those groups; you need to explicitly add rules for the **Hosts** you wish to include in the management zone, as shown in [Examples](#examples) below.

  Management zones are always implicitly propagated to the following related entities. However, this does not apply to entity selector based rules.

  From

  To

  Process Group

  Process Group Instance, Container Group, Container Group Instance

  Hypervisor

  VCenter

  Host

  EC2 Instance, Container Group Instance

  AWS Credentials

  AWS availability zone, AWS lambda function, AWS application load balancer, AWS network load balancer, EC2 instance, Custom device, Custom device group, Auto scaling group, Relational database service

  Synthetic Test

  Application
* When you add an entity using tags to a management zone as part of entity creation via API, there might be a delay in management-zone assignment depending on the number and complexity of your tagging rules. See [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.") for best practices to speed up the time taken to assign tags and management zones within your monitoring environments.
* You cannot define management-zone rules where the entity selector for one management zone filters by another management zone. Management zone predicates such as `mzID` or `mzName` are not allowed in entity selector strings. This means, for example, that you cannot define management zone A as containing hosts belonging to management zone B. Management-zone rules based on other management zones increase the number of runs made by the conditional decision engine and can greatly delay management-zone assignment. See also [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.") for related information.

  As a workaround, use the same entity selector string in both management zones. For example, consider that:

  + Management zone A has the rule `type(SERVICE),entityName.startsWith("myService"),tag("my:tag")`.
  + Management zone B is required to include services that call services in Management zone A. To do so, define the rule `type(SERVICE),fromRelationships.calls(type(SERVICE),entityName.startsWith("myService"),tag("my:tag"))`.

## Examples

Example 1: Management-zone rules providing access to hosts of specific host groups; users assigned to the zone can filter by accessible host groups.

1. Set up a rule for hosts.

   1. Select **Monitored entity** as the **Rule type**.
   2. Select **Hosts** as the entity that the **Rule applies to**.
   3. Add a condition.
   4. Select **Host group** as the **Property**.
   5. Select or search for a host group in the **Value** field.
   6. **Preview** the list of matching entities.

      ![Preview the rule for hosts](https://dt-cdn.net/images/mz-sample-1-1a-1026-c1e2a8cd09.png)
   7. **Save changes**.

   Add a rule in this way for each set of hosts per host group.
2. Set up a rule for host groups.

   In order for users to have visibility into host groups containing the hosts in the management zone, you need to set up host group rulesâone per host group you wish to include. This ensures that users can filter by the host groups on the **Hosts** page.

   1. Select **Monitored entity** as the **Rule type**.
   2. Choose **Host groups** as the entity that the **Rule applies to**.
   3. Add a condition.
   4. Select **Host group name** as the **Property**.
   5. Define the condition for the host group name, for example, a text string contained in the host group's name.
   6. **Preview** the list of matching host groups.

      ![Rule for a host group](https://dt-cdn.net/images/mz-sample-1-2a-1025-fd96aea449.png)
   7. **Save changes**.

   Add a rule in this way for each host group you wish to include in the management zone. Host group names are shown in the filter on the **Hosts** page only if a corresponding management-zone rule is defined for them. Generally, you would grant access to the same host groups that the hosts in your management zone belong to.

When the management zone is applied, the user can see only the assigned hosts and can filter the **Hosts** page by **Host group**. The host groups are those defined in your management-zone rules.

![Host groups filter](https://dt-cdn.net/images/mz-sample-1-3-1612-2b773ed1d7.png)

Example 2: Management-zone rules providing access to all synthetic monitors

Management-zone rules can be defined for three types of synthetic entities:

* Browser monitors
* HTTP monitors
* Third-party monitors

To provide access to all synthetic monitors, you need to define rules to cover all monitors per monitor type.

![Management zones: synthetic entities](https://dt-cdn.net/images/mz-sample-2-1a-823-7985b67d21.png)

To set up a rule to cover all **Browser monitors**, for example:

Specify that the **Browser monitor name exists**. **Preview** the rule to see the matching entities.

![Browser-monitor rule](https://dt-cdn.net/images/mz-sample-2-2a-1119-c1287aafd6.png)

Additionally, set up similar rules for HTTP and third-party monitors to cover all synthetic monitors in your environment.

If you'd like your user to be able to create or edit synthetic monitors in a management zone, you need to provide the **Manage monitoring settings** [permission](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") at the management-zone or environment level.

Example 3: Management-zone rules providing access to specific measurements of specific ingested metrics

You can provide access to an ingested metric, filtered by a dimension value so that only specific measurements of the given metric are accessible within the management zone (for charting and analysis, for example).

1. Select the **Dimensional data** entity of type **METRIC**.
2. Fill out the condition for the metric name (**METRIC\_KEY**). You can provide access to a specific metric by providing the entire name or a set of metrics by specifying the opening string (for example, `business.revenue`).

   ![Management-zone rule for custom metric name](https://dt-cdn.net/images/mz-sample-3-1-955-64a30c6239.png)
3. To filter for specific measurements of the metrics, you need to add a condition for the metric dimension. Select **DIMENSION** and provide the dimension name (**Key**) and (**Value**). For example, to filter your business metrics for the US eastern region, you would specify the dimension name `region` and value `useast`.

   ![Dimensional metric data in a management zone](https://dt-cdn.net/images/mz-sample-3-2-937-3087a6c4e0.png)
4. **Save changes**.

If your management zone already provides access to the host through which a custom metric and its measurements are ingested, you automatically provide access to that custom metric; you don't need to set up an explicit rule for the custom metric. Note that this doesnât include all measurements of that custom metric but only those measurements that were sent in for your host.

Example 4: Management-zone rules providing access to specific measurements of specific ingested logs

You can provide access to logs filtered by a log attribute value (as an alternative to filtering logs by entities).

1. Select **Dimensional data** in the **Rule type** field.
2. Select **LOG** in the **Type** field.
3. Add a condition for logs.

   1. Select **DIMENSION** for condition type.
   2. Provide the log attribute name in the **Key** field. You can list only one attribute value.
   3. Add the phrase to search for in the **Value** field.
   4. You can also set the **Operator** as `begins with` or `equals` for the **Value** entered. For example, to filter your logs for a specific Kubernetes deployment name, specify the `k8s.deployment.name` key and `begins with` `automation-server` as the value.
4. **Save changes**.

![Example management-zone rule for logs](https://dt-cdn.net/images/mz-log-example-726-67634de796.png)

If your management zone already provides access to the host through which logs are ingested, you automatically provide access to those logs. This means that you don't need to set up an explicit dimensional rule for such logs.

Example 5: Entity selector rule based on entity relationships

In order to filter for services that directly call a service with the name `JourneyService`, you can run the [GET all entity types](/docs/dynatrace-api/environment-api/entity-v2/get-all-entity-types "View all types of monitored entities in your environment via Dynatrace API.") API call to check the entity type and relationships for services.

From the information gathered, you can now construct an entity-selector rule for the entity type `service` that has a `calls` "from relationship" to the entity type `service` with the name `JourneyService`:

`type(SERVICE),fromRelationship.calls(type(SERVICE),entityName(JourneyService))`

This can also be written as `type(SERVICE),fromRelationship.calls(type(SERVICE) AND entityName.equals(JourneyService))`.

![Entity-selector rule based on relationships](https://dt-cdn.net/images/mz-sample-4-1-954-606bb32f43.png)

## Related topics

* [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.")
* [Environment API v2 - Entity selector](/docs/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.")
* [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.")
* [Metrics API - Metric selector](/docs/dynatrace-api/environment-api/metric-v2/metric-selector "Configure the metric selector for the Metric v2 API.")
* [Management zones and ingested log data (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/management-zones-and-log-monitoring "Find out how ingested log data is assigned to management zones.")
* [Best practices for scaling tagging and management-zone rules](/docs/manage/tags-and-metadata/basic-concepts/best-practice-tagging-at-scale "Optimize auto-tagging and management-zone rules to speed up the automatic assignment process.")


---


## Source: access-security-context.md


---
title: Grant access to entities with security context
source: https://www.dynatrace.com/docs/manage/identity-access-management/use-cases/access-security-context
scraped: 2026-02-17T21:25:03.991881
---

# Grant access to entities with security context

# Grant access to entities with security context

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Sep 17, 2025

This article shows you how to set the security context and grant access to the monitored entities using policies.

Don't mistake IAM policies with management zones. Unlike management zones, an IAM policy that is set up to filter entities (`allow storage:entities:read`) will not filter related metrics, logs, or traces.
These entity filters only control which entities can be queried via DQL.
To control access to logs, metrics, and spans, you need to use the corresponding permissions, such as `allow storage:logs:read`.

## Who this is for

This is for Dynatrace account administrators who are responsible for creating policies to grant users access to monitored entities such as hosts, through [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

## What you'll learn

In this article, you'll learn:

* How to set the security context on monitored entities.
* How to create policies to grant access to monitoring data stored in Grail in the context of monitored entities.
* How to use the security context in combination with IAM security policies to provide granular access to your entities.

## Before you begin

Prior knowledge

* [Identity and access management (IAM)](/docs/manage/identity-access-management "Configure users, groups and permissions.")
* [Grant access to Dynatrace](/docs/manage/identity-access-management/use-cases/access-platform "Grant access to Dynatrace")
* [User permissions in default groups](/docs/manage/identity-access-management/user-and-group-management/default-groups "Dynatrace default groups reference")

Prerequisites

* A Dynatrace account with administrative privileges.
* Set up the required users, federations, and user groups in advance.

Key terms

Security context
:   Defines the scope of access for a user or group

Management zone
:   Information-partitioning mechanism that promotes collaboration and the sharing of relevant data in your Dynatrace environment

## Steps

Letâs start by setting up the security context, then learn how to create the policies to grant access to data on entities.

1. Set the security context for monitored entities

To set the security context for entities, you can choose one of the following options,

#### Option 1: Use an already existing property of the entity

If you have already set up management zones, it's possible to map the management zones into the security context, depending on its type.

1. Go to **Settings** > **Topology model** > **Grail Security Context**.
2. Expand the relevant entity type
3. In the **Destination property** section, choose the field that should map into the security context. It can be either `managementZones`, `entity.detected_name`, or `dt.security_context` itself.

   ![Grail Security Context ](https://dt-cdn.net/images/123-1532-c8aa238683.webp)

`managementZones` is the default value for the majority of entity types. With this option, the security context of entities is mapped from classic management zones.
Logs, spans, metrics, and events powered by Grail that are sent from an entity do not inherit the management zones of that entity.
This means [access controls](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.") on logs, spans, metrics and events powered by Grail must be handled separately.
This option is useful if you have management zones already in place and you want to re-use those to control access on entities.

#### Option 2: Host tags and properties

You can set the security context using the `dt.security_context` host property set using automated rules or host properties set using [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

After you set the security context on a host, it will be used to automatically determine the security context for all logs, spans, metrics, and events that are sent from this host.

Additionally, it will set the security context for host-related entities reported from this host, such as process group instances and disks.

With this option, ensure the security context is mapped using the `dt.security_context` field for the entity types of interest, as described in Option 1 above.

To set a security context using `oneagentctl`:

```
./oneagentctl --set-host-property=dt.security_context=my-security-context
```

#### Option 3: Define an extraction rule for generic types

For [generic entity types](/docs/ingest-from/extend-dynatrace/extend-topology/events-entity-extraction#extract-map "Extract generic entities from event metadata and map events to them."), you can add an extraction rule for `dt.security_context` and derive the security context from any detail on the data source.
This is particularly useful for extensions where you can set the `dt.security_context` per extension configuration.

Let's use the PostgreSQL extension with a simplified example, assuming a configuration with `dt.security_context` set to `TeamA`.
For that configuration, the extension sends metric data points using the Metrics API such as:

```
postgres.activity.idle,port=5432,dt.security_context="TeamA",dt.entity.sql:postgres_instance="CUSTOM_DEVICE-..." 42



postgres.activity.idle,port=5432,dt.security_context="TeamA",dt.entity.sql:postgres_instance="CUSTOM_DEVICE-..." 45



postgres.activity.idle,port=5432,dt.security_context="TeamA",dt.entity.sql:postgres_instance="CUSTOM_DEVICE-..." 43
```

Based on this, you can add an extraction rule to the existing PostgreSQL extension extraction rules that sets the `dt.security_context`
to the value of the `dt.security_context` dimension in the metric data points (`TeamA`).

As with option 2, ensure the security context is mapped using the `dt.security_context` field for the entity types of interest.
If the entity types are not listed, we recommend creating those entity types.

#### Option 4: Dynatrace API

This API is deprecated.

Set the security context via the [Monitored entities API](/docs/dynatrace-api/environment-api/entity-v2/security-context "Create or delete security context via Dynatrace API.").

2. Create the policy

Entity permissions allow you to define policies that control data access on entities. In contrast to monitoring data, entity permissions only allow filtering for the `dt.security_context` field.

Access to all entities is configured via the `storage:entities:read` permission, which supports the following conditions

* `storage:entity.type`

  the entity type in upper snake case (for example `PROCESS_GROUP_INSTANCE`)
* `storage:dt.security_context`

  the security context of this entity. Can be a multi-value field and `startsWith` will evaluate for any matching value.

For example, the following policy grants access to data with the security context set to `mySecurityContext`.

```
ALLOW



storage:entities:read



WHERE



storage:dt.security_context = "mySecurityContext";
```

## Related topics

* [Monitored entities API - security context](/docs/dynatrace-api/environment-api/entity-v2/security-context "Create or delete security context via Dynatrace API.")
* [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.")
* [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies")


---


## Source: user-mfa.md


---
title: Enhance your account security with MFA TOTP
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-mfa/user-mfa
scraped: 2026-02-18T05:57:57.268158
---

# Enhance your account security with MFA TOTP

# Enhance your account security with MFA TOTP

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Dec 05, 2025

**Non-federated users** can choose to increase their user account security by enabling MFA Time-based One-Time Password (TOTP) with their preferred authenticator app. When enabled, they will be prompted to enter the verification code from their registered authenticator app every time they access any environment.

Federated Users

**Federated users** are not required to register or apply MFA, even if MFA is enabled on their environment. Instead, their login is verified by their Identity Provider (IdP) during the login process.

### Enable MFA TOTP for your user account

To enable MFA TOTP

1. Go to the [Account Managementï»¿](https://myaccount.dynatrace.com/accounts) **My profile** > **Security options** tab and select **Add authenticator app**.
2. Enter the verification code sent to your registered email address.
3. Scan the QR code using your phone's camera in your preferred authenticator app. Optionally, you can enter the code by selecting **Can't scan the QR code?**.
4. Enter the code generated into the **One-Time Password** field and select **Add**.

Verification code prompt frequency

Verification code prompts display once during a user login session. To further reduce code verification requests on trusted devices, use the **Remember Me** option on the login screen to instruct the system to remember you on that web browser.

To remove MFA TOTP

1. Go to the [Account Managementï»¿](https://myaccount.dynatrace.com/accounts) **My profile** > **Security options** tab and select **Add authenticator app**.
2. Open the  menu and select **Delete**.
3. Enter the code generated into the **One-Time Password** field and select **Delete**.

## FAQ

While signing up for MFA TOTP, I did not receive a one-time password via email.

Please wait 30 seconds and check your junk email folder.

I signed up for MFA TOTP, but the verification code does not work.

Ensure that you're using the correct code from the Dynatrace entry in your authenticator app and that the code has not timed out.

Can I register another Authenticator app?

Currently, only one authenticator app can be registered at a time. If you want to switch to another authenticator app, do not delete the old app yet. First, remove MFA TOTP by deleting it from [Dynatrace accountï»¿](https://myaccount.dynatrace.com/accounts), and then enable it again with the new authenticator app.

I signed up for MFA TOTP, but Iâm not prompted for a verification code.

Common reasons why you might not be prompted for MFA when accessing Dynatrace:

* You're a federated user, logging in through your federated identity provider (such as Azure AD or Okta). In this case, MFA should be handled by your IdP.
* You're a non-federated user, but you're in the same login session and have previously provided an MFA code.
* You're a non-federated user but have previously chosen the **Remember me** option on the login window and are using the same web browser.


---


## Source: access-saml.md


---
title: SAML
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-saml
scraped: 2026-02-18T05:44:00.059398
---

# SAML

# SAML

* Latest Dynatrace
* Reference
* 13-min read
* Updated on Aug 20, 2025

Dynatrace SaaS enables authentication through your organization's identity provider (IdP). If you want to use your organization's corporate credentials for authentication in Dynatrace, you can set up SAML to delegate authentication to your IdP.

* For definitions of unfamiliar terms, see the [glossary](#glossary).
* For background information such as an overview of federation types, use cases, and algorithms, see [Federation concepts](/docs/manage/identity-access-management/user-and-group-management/access-saml/federation-concepts "Federation concepts").

## Requirements and specifications

### Identity Provider (IdP)

Your IdP needs to follow some basic SAML specification and security requirements to be compliant with Dynatrace SSO:

* The entire SAML message must be signed (signing only SAML assertions is insufficient and generates a `400 Bad Request` response).
* The SAML protocol version is `urn:oasis:names:tc:SAML:2.0:protocol`.
* The `NameID` format is `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.
* IdP response `NotBefore` and `NotOnOrAfter` assertion timestamps must consider system clock skew and must be set to at least 1 minute before and 1 minute after the current time (this particularly concerns AD FS default settings).
* The IdP response status code must be `urn:oasis:names:tc:SAML:2.0:status:Success`.
* The `SignatureMethod` algorithm is `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`.
* The `DigestMethod` algorithm is `http://www.w3.org/2001/04/xmlenc#sha256`.
* The X509Certificate appended to federation metadata needs to be signed using one of the following algorithms: SHA256withRSA, SHA384withRSA, or SHA512withRSA
* No assertion encryption.

### Service Provider (SP) - Dynatrace SSO

* `Just-in-Time` provisioning is supported.
* Session timeout is `1` hour and is not configurable.

## SSO metadata

* For global federation, Dynatrace SSO SP metadata is provided at [https://sso.dynatrace.com/sso/metadataï»¿](https://sso.dynatrace.com/sso/metadata). If your IdP requires manual configuration and you don't have any XML parser extensions installed in your Chrome browser, we recommend that you view the metadata in Firefox.
* For account or environment federation, you download unique SP metadata during SAML configuration as described below.

Depending on the IdP type, these endpoints need to be configured as follows.

### Global federation

* `https://sso.dynatrace.com:443/saml2/login` for Entity ID (Audience Restriction).
* `https://sso.dynatrace.com:443/saml2/sp/consumer` for Single Sign On URL, Destination URL, Recipient URL.
* `https://sso.dynatrace.com:443/saml2/sp/logout` for Single Logout Service URL.

If your IdP configuration screen contains the option to set SAML bindings for sign-in or sign-out, set it to `urn:oasis:names:tc:SAML:2.0:bindings:HTTP-POST`.

### Account or environment federation

* `https://sso.dynatrace.com/identity-federation/federation/<configuration-UUID>` for Entity ID.

  In the XML metadata file, look for `md:EntityDescriptor` and find the value of `entityID`.
* `https://sso.dynatrace.com/identity-federation/sp/consumer/account/<account-UUID>/federation/<configuration-UUID>` for Assertion Consumer Service (ACS).

  In the XML metadata file, look for `md:AssertionConsumerService` and find the value of `Location`.
* `https://sso.dynatrace.com/identity-federation/sp/logout/account/<account-UUID>/federation/<configuration-UUID>` for Logout URL.

  In the XML metadata file, look for `md:SingleLogoutService` and find the value of `Location`.

## SAML federated IdP configuration

To set up SAML for your domain

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a fallback user account**](#create-fallback)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Verify your ownership of the domain**](#verify-ownership)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure SAML**](#configure-saml)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Test your configuration**](#test-configuration)

### Step 1 Create a fallback user account

Your fallback account must be a non-federated user account belonging to a group that has **View and manage users and groups** permission and isn't covered by the federated sign-in.

* For global federation, when a user signs in, Dynatrace checks the domain part of your corporate email address to determine whether SAML was configured for that domain. If there's a match, the sign-in is redirected to your companyâs IdP for authentication. For a fallback, you need an email address that won't be redirected like this.

  If you are using global federation, you must create a fallback user account so you won't be locked out if you have configuration troubles.
* To sign in without using Account or Environment federation, open `https://sso.dynatrace.com` in incognito mode and sign in using credentials. (If you sign in using credentials, however, you won't have any SAML group assigned in your session.)

  If the user belongs to any global federation, however, they are redirected to the global federation IdP, not signed in using their credentials.

To create a fallback account

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > your account > **Identity & access management** > **User management** and select **Invite user**.
2. In the **User email** step, enter a non-federated email address (an email address with a different domain from the one for which you are setting up SAML) and then select **Next**.
3. In the **Add to groups** step, add the user to a group that has **View and manage users and groups** permission and then select **Next**.
4. In the **Confirm permissions** step, confirm that you have added the correct permissions and then select **Invite**.

### Step 2 Verify your ownership of the domain

Before you can configure the domain for which you want to set up SAML, you need to prove ownership of the domain.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > your account > **Identity & access management** > **Domain verification**.
2. In the **Add domain** section, enter the domain (for example, `mycompanyname.com`) for which you want to set up SAML and select **Add** to add it to the **Pending domains** table.

   If users in your organization use more than one domain to sign in (for example, `@mycompanyname.com` and `@uk.mycompanyname.com`), you can add additional domains in additional rows and start verifying them all in parallel. Enter each domain in a different row.
3. For each domain you are verifying, in the **Pending domains** table, select **Copy** (in the **Value** column) and add the copied TXT resource record to your domainâs DNS configuration.
4. For each domain you are verifying, in the **Pending domains** table, select **Actions** > **Verify** so that Dynatrace can verify that the record was added to your domainâs DNS.

   It typically takes a few minutes for a record to propagate through the DNS system and the value to become available for Dynatrace to verify. In some cases, it may take up to 24 hours.
5. Each verified domain is added to the **Verified domains** table.

### Step 3 Configure SAML

Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > your account > **Identity & access management** > **SAML configuration** to list all SAML configurations for the selected account. This is your starting point for managing SAML configurations.

What can I do from the SAML configuration page?

Action

How to do it

Find

To find a SAML configuration, use the filter controls above the table. You can filter by **Search table** (text), **Scope**, and **Domain**.

Create

To create a new SAML configuration, select the **New configuration** button above the table.

Edit

To edit an existing SAML configuration, find the configuration in the table and, in the **Actions** column, select  > **Edit configuration**. The steps are the same as for creating a new configuration.

Disable

To disable an existing SAML configuration, find the configuration in the table and, in the **Actions** column, select  > **Disable configuration**.

Delete

To delete an existing SAML configuration, find the configuration in the table and, in the **Actions** column, select  > **Delete configuration**.

After you [create a fallback user account](#create-fallback) and [verify your ownership of the domain](#verify-ownership), go to **Identity & access management** > **SAML configuration** and select **New configuration** to create a new SAML configuration.

1. **Federation type**: select one of the three federation types and then select **Next**.

   After a SAML configuration is created:

   * You can't change the type from Global to Account or Environment, or from Account or Environment to Global.
   * You can change the type from Account to Environment, or from Environment to Account.

   Account federation - description

   Account-specific federation federates your user's identity based on the domain part of the email address. The scope is limited by your account. Your configuration does not impact any other accounts from your company using the same domain. It's valid only within the boundaries of your account and environment.

   Environment federation - description

   Environment-specific federation also federates your user's identity based on the domain part of the email, but the scope is limited to one or more environments. You can, for instance, enable identity federation for your dev monitoring environment using your dev IdP instance.

   Global federation - description

   Global cross-account federation also federates your user's identity based on the domain part of the email address. Its scope is global: it affects all other accounts in Dynatrace sharing the same domain part of the user's email. If your company has several Dynatrace accounts and you are using the same domain to sign in for all of your accounts, then the other accounts inherit the federation configuration automatically and use your identity provider for authentication.

   For details, see [Federation types](/docs/manage/identity-access-management/user-and-group-management/access-saml/federation-concepts#federation-types "Federation concepts").
2. **SAML metadata**: configure the SAML metadata and then select **Next**.

   * **Name or description for configuration**

     Enter the name for your configuration that you want to display in the **Configurations** table on the **SAML configuration** page.
   * **Dynatrace service provider metadata**:

     If you're creating an Account or Environment type federation, the **Generate SP metadata** button in this step creates a disabled, blank configuration in the account that's needed to register a new virtual Service Provider instance, which is required for generating the SP metadata. If you select **Generate SP metadata** and then you want to abandon the configuration, be sure to delete the blank SAML configuration.

     Select **Download SP metadata** to download the service provider (SP) metadata from Dynatrace.

     This gets the metadata from Dynatrace that you need to use on the IdP end of this configuration.

     + Register this data at your IdP.
     + From your IdP, get the metadata of your IdP in XML format.

       You need this file in the **Identity provider metadata** section below.

     Exact details of the activities involved in this step depend on your IdP's interface and requirements.

     IdP-specific instructions

     Dynatrace supports all IdPs that support the SAML 2.0 standard. For frequently used IdPs,
     we have IdP-specific instructions for registering the SP data at your IdP and getting the IdP metadata. These examples were correct at the time of writing, but Dynatrace has no control over changes that may be made by your IdP.

     + [AD FS instructions](/docs/manage/identity-access-management/user-and-group-management/access-saml/idp-specific/saml-ad-fs "Learn how to configure Dynatrace SSO in Active Directory Federation Services (AD FS).")
     + [Azure instructions](/docs/manage/identity-access-management/user-and-group-management/access-saml/idp-specific/saml-azure "Learn how to configure Dynatrace SSO in Azure.")
     + [Google Workspace instructions](/docs/manage/identity-access-management/user-and-group-management/access-saml/idp-specific/saml-google-workspace "Learn how to configure Dynatrace SSO in Google Workspace.")
     + [Okta instructions](/docs/manage/identity-access-management/user-and-group-management/access-saml/idp-specific/saml-okta "Learn how to configure Dynatrace SSO in Okta.")

     As mentioned in the IdP requirements section of this page, the `X509Certificate` appended to metadata needs to be signed using one of the following algorithms: `SHA256withRSA`, `SHA384withRSA`, or `SHA512withRSA`.
   * **Identity provider metadata**

     Select **Choose file** to specify the metadata file you received from your IdP.
   * **Attribute mapping** Optional

     Specify where to get the attribute values when Dynatrace reads SAML payloads.

     What attribute mapping values can I use here?

     | Attribute | Location |
     | --- | --- |
     | Firstname | For Microsoft Azure: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname` |
     | Lastname | For Microsoft Azure: `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname` |
     | Federated | The groups/roles of a user from your IdP. You need this value if you want to use [SAML authorization](#saml-authorization). |

     Example SAML response and how to set fields based on it

     In this example:

     + First Name: `Sandy`
     + Last Name: `McSample`
     + Federated attribute: `http://schemas.microsoft.com/ws/2008/06/identity/claims/groups`
     + Group Claims: `5ab67c8d-9e0f-1ghi-23j4-56klmn7o8p9q`, etc.

     ```
     <AttributeStatement>



     <Attribute Name="http://schemas.microsoft.com/identity/claims/tenantid">



     <AttributeValue>70ebe3a3-5b30-435d-9d67-7716d74ca190</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.microsoft.com/identity/claims/objectidentifier">



     <AttributeValue>c72581d1-f178-4a50-9816-504ee495bc15</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.microsoft.com/identity/claims/displayname">



     <AttributeValue>McSample, Sandy</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/groups">



     <AttributeValue>5ab67c8d-9e0f-1ghi-23j4-56klmn7o8p9q</AttributeValue>



     (...)



     <AttributeValue>5ba67c8d-9e0f-1ghi-23j4-56klmn7o8p9q</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.microsoft.com/identity/claims/identityprovider">



     <AttributeValue>https://sts.windows.net/70ebe3a3-5b30-435d-9d67-7716d74ca190/</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.microsoft.com/claims/authnmethodsreferences">



     <AttributeValue>http://schemas.microsoft.com/ws/2008/06/identity/authenticationmethod/password</AttributeValue>



     <AttributeValue>http://schemas.microsoft.com/claims/multipleauthn</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname">



     <AttributeValue>Sandy</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname">



     <AttributeValue>McSample</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress">



     <AttributeValue>Sandy.McSample@dynatrace.com</AttributeValue>



     </Attribute>



     <Attribute Name="http://schemas.xmlsoap.org/ws/2005/05/identity/claims/name">



     <AttributeValue>Sandy.McSample@dynatrace.com</AttributeValue>



     </Attribute>



     </AttributeStatement>
     ```
3. **Validation**: validate your configuration and then select **Next**.

   Validation starts automatically when you move to the validation step. If you select **Previous** to go back and change settings, validation will restart when you select **Next** to return to the validation step.

   During validation, you are redirected to the federated IdP for sign-in, and then sign-in results are displayed for you to review. The configuration passes validation when you sign in through the federated IdP and Dynatrace resolves the user sign-in from the SAML message.

   The validation step prevents any misconfiguration that could result in account lock-out and ensures that users can sign in.
4. **Scope assignment**: assign scopes and then select **Next**.

   Account federation

   Account-specific federation federates your user's identity based on the domain part of the email address. The scope is limited by your account and your configuration will not impact any other accounts from your company using the same domain. It is only valid within the boundaries of your account and environment.

   Verify the federation type you have selected. If you need to change it, use **Previous** to go back to the **Federation type** step and then use **Next** to return to this step.

   Then specify one of the following:

   Select domains for configuration

   Select this option to specify each of the domains from which you want to allow authentication.

   When this is selected:

   * If you have selected **Allow users from all other domains to authenticate via your IdP**, it is now cleared.
   * Only users whose email address matches one of the selected domains will be authenticated via your IdP.

   Allow users from all other domains to authenticate via your IdP

   Select this option if you want to authenticate users from domains other than the domains you chose in **Select domains for configuration**.

   When this is selected:

   * Any selection you have made in **Select domains for configuration** is cleared.
   * All users that sign in to your account or environment will always be authenticated via your IdP, regardless of the domain in their email address. This can be useful, for example, if you manage external contractors in your identity provider who don't have a selected email address for signing in.

   Environment federation

   Environment-specific federation also federates your user's identity based on the domain part of the email, but the scope is limited to one or more environments. You can, for instance, enable the identity federation for your dev monitoring environment using your dev IDP instance.

   For each environment federation you want to add

   1. Select **Add federation**.
   2. Define the federation.

      * **Select environment**: Select the environment
      * **Select domains**: Select one or more domains
5. **Activation**: activate your configuration.

   Turn on **Enable SSO** and select **Complete configuration**.

### Step 4 Test your configuration

To test your configuration

1. Open a new browser instance and a new incognito window.
2. Sign in to one of your Dynatrace environments.

   To test an Account or Environment federation, go to the tenant URL first, because that's how Dynatrace SSO gets the context (for example, from `https://abc12345.live.dynatrace.com`).

Troubleshooting:

* If you experience trouble, use the [fallback user account](#create-fallback) you created earlier to sign in and change the configuration or disable federation.
* See [FAQ](#faq) below for answers to common questions.

## SAML authorization

It is possible to automatically synchronize the group membership between your IdP and Dynatrace. For this, you need to define a mapping between locally-defined Dynatrace groups and incoming group claims from your IdP. These mappings are later used during user sign in to establish user's membership on the matching groups.

To create a mapping, you need to specify the SAML Group Attribute Value in the [attribute mapping configuration](#configure-metadata) that contains the groups/roles of a user from your IdP, and then map groups from your IdP to groups in Dynatrace.

In Dynatrace, all user group permissions are joined together. The user will be granted permissions from all group types: `LOCAL`, `SAML`, and `SCIM`. It is the Account Manager's responsibility to decide if and how user permissions are isolated.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > your account > **Identity & access management** > **Group management** and add a new group or find an existing group you want to map. You can filter the list by name and permissions.

   **Important**

   * We **strongly recommend** that you first create a new group (select **Create group**) to test whether SAML authorization works for that group.
   * Switching a `LOCAL` group to `SAML` removes all user assignments to that group.
   * Make sure you have a non-federated user with **manage groups** permission as discussed [earlier](#create-fallback).
2. Expand the **Edit** pane of the group to set up a mapping.

   * **Group name**âMake sure it matches the group you intend to edit.
   * **SAML Group Attribute Value**âA list of one or more federated group names returned by your IdP and mapped to this Dynatrace group.  
     Select \*\* +SAML Group Attribute Value\*\* if you need to match to an incoming SAML group claim.  
     This typically isn't a group display name. It can be, for example, an LDAP ID.

     Note that when adding SAML Group Attribute Values to a local group:

     + **All existing users from that group are removed**.
     + The group's source is changed to SAML, which means that assignment of users to that group is automatically handled via the corect mapping of the incoming **SAML group claims** to the defined SAML Group Attribute Values.
   * **Account permissions**  
     Account-related permissions for members of this group.
   * **Environment permissions**  
     Environment-related permissions for members of this group.
   * **Management zone permissions**  
     [Management zone](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")ârelated permissions for members of this group.
3. Select **Save**.  
   **Note**: Don't sign out of Dynatrace yet.
4. Open a new browser instance and a new incognito window and sign in.
5. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) and verify that you can still see **Identity & and access management** > **User management** and **Identity & and access management** > **Group management**.  
   If you can't see them, you've lost your Dynatrace admin permissions. Use the non-federated user account to change the configuration if you've run into any issues.
6. Upon a federated user's successful login, Dynatrace checks incoming **group claims** against **SAML Group Attribute Values** defined throughout all SAML groups. When there is a match, the user is added to the corresponding Dynatrace group.

**Note**:

* When using SAML authentication, you don't have to invite users to Dynatrace. During sign-in, a user that doesn't already exist in Dynatrace is created automatically.

## FAQ

### SAML configuration and attributes

How can I resolve a Missing Destination Attribute error when configuring PingFederate?

If you are using PingFederate as an IdP and you get a Missing Destination Attribute value error

1. Go to PingFederate and select **Identity Provider** in the left sidebar.
2. Select the **Signature Policy** tab.
3. Clear the **ALWAYS SIGN ASSERTION** checkbox as in the following example.

![Clear the ALWAYS SIGN ASSERTION checkbox](https://dt-cdn.net/images/pingfed-2125-8866bd36e1.png)

Whatâs the proper NameIdFormat?

The `NameIdFormat` must be `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`.

What claim rules do I need in AD FS on the Dynatrace relying party?

You need two issuance transform rules, in this order:

* The first one uses the `Send LDAP Attributes as Claims` rule template and creates an outgoing claim type named `E-Mail Address` from an LDAP attribute in your attribute store containing the Dynatrace username (the userâs domain email address).
* The second one uses the `Transform an Incoming Claim` rule template and creates an outgoing claim type `Name ID` and outgoing name ID format `Email` with the `Pass through all claim values` option enabled.

Does Dynatrace support Just-in-Time creation of users upon sign-in?

Yes, Dynatrace supports JIT creation of users when using SAML federation. Federated users are created or updated on the fly after successful authentication.

Is the domain verification TXT resource record needed permanently?

No, it can be removed after Dynatrace has successfully validated ownership of the domain.

Is sending a full DN allowed in a group attribute?

No, a full DN contains commas, and this is recognized as independent group names. The IdP should send the group name or group ID.

Can a specific Dynatrace environment URL be configured as the default destination URL?

Yes. When a Dynatrace environment URL is sent in the `RelayState` parameter, the user is redirected to the specified URL upon signing in. When the `RelayState` value is missing, the user is redirected to the last accessed Dynatrace tenant or account page.

Depending on the IdP, setting `RelayState` in an IdP SAML configuration usually affects all IdP users. Dynatrace SSO does not support a default destination per user.

Can the Group SAML attribute value contain a comma-separated list of groups?

Yes. If the value of the Group SAML attribute contains a comma-separated list of groups, the value will be split by comma and interpreted as a list of groups.

If a SAML group in Dynatrace is assigned multiple group claims, does a user need all of them to get assigned to the group upon SAML login?

No, a user needs only one of the security group claims to get assigned to the group.

Are nested LDAP groups (such as 'CN=Admin,OU=SSO Team,DC=dynatrace,DC=com') supported?

Yes. For example, if your IdP returned groups as the LDAP path:  
`CN=Admin,OU=SSO Team,DC=dynatrace,DC=com`  
Dynatrace would interpret this as a comma-separated list of four groups:  
`CN=Admin`, `OU=SSO Team`, `DC=dynatrace`, and `DC=com`  
In group mapping, you should use one of these values.

In the validation step, I get an "All certificates from SAML metadata are expired or not yet valid" error, but my metadata didn't change.

The signing certificate inside the IdP metadata has expired since you set up the SAML configuration. The metadata is always validated at the beginning of the verification process.

To solve this, you need to rotate the signing certificate on your IdP side, save (or copy) the updated IdP metadata, and upload it to your federation configuration in Dynatrace.

### Authentication and logout

Why am I signed out from my services when I've requested a sign-out from Dynatrace?

Upon sign-out, a global sign-out is triggered, including for your IdP, which then cascades to other services. Otherwise, you would be signed out from Dynatrace, but it would be sufficient to just enter your email to re-authenticate.

If you want to disable it (not a good idea from a security standpoint), edit your metadata, remove all `SingleLogoutService` tags, and upload the updated metadata.

Are multiple domains and subdomains supported for authentication?

Yes, but you need to perform domain verification and create a configuration for each domain separately. Each domain configuration can use the same IdP metadata and settings.

Is IdP-initiated sign-in or RelayState supported?

Yes, both IdP-initiated sign-in and `RelayState` are supported.

How can I configure Break Glass access to an account when SAML federation is active?

If your security policy requires emergency access to Dynatrace in case of problems with your IdP, we recommend that you invite a non-federated user to the environment with **Account manager** permissions and use that as your Break Glass account.

* If this is not an option, you can configure an additional federated domain to a different IdP and use it for backup sign-on in case of problems with your regular IdP.
* Configuring multi-factor authentication (MFA) is not supported by Dynatrace. You can configure authentication and MFA through your organization's IdP.

How can I configure multi-factor authentication (MFA)?

Configuring multi-factor authentication (MFA) is not supported by Dynatrace. You can configure authentication and MFA through your organization's IdP.

### Signatures and certificates

What needs to be signed in SAML?

Whole messages need to be signed, including sign-out requests and responses. It isn't sufficient to sign just the assertion part.

Can metadata contain multiple signing certificates?

Yes, customer IdP metadata can contain multiple signing certificates. Dynatrace SSO validates that SAML messages from the customer IdP are signed by one of them.

How can I rotate my IdP SAML certificates in Dynatrace?

SAML metadata can contain more than one certificate, not all of which need to be valid. This is very useful when you want to rotate your certificates because the current one is going to expire.

To switch certificates

1. Create a new certificate that meets our [requirements.](#idp-requirements)

   Caution

   Don't change it on your IdP side yet! If you do so, you will cut access to the Dynatrace environment.

   Caution

   If your IdP is Azure Entra ID, note that a new inactive certificate will automatically be used immediately after the old one expires. Source: [Tutorial: Manage certificates for federated single sign-onï»¿](https://dt-url.net/ez23wla).
2. Append the new certificate to your metadata in Dynatrace.

   * If your IdP allows you to include more than one certificate, you can add the certificate in the IdP and then upload to Dynatrace the entire updated metadata generated by your IdP.

     To maintain uninterrupted access to Dynatrace during certificate rotation, look at the entries between the `<KeyDescriptor>` tags to verify that the XML metadata contains two different certificates, as shown in the example below.

     ```
     <KeyDescriptor use="signing">



     <KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">



     <X509Data>



     <X509Certificate>(...) Certificate 1 (...)</X509Certificate>



     </X509Data>



     </KeyInfo>



     </KeyDescriptor>



     <KeyDescriptor use="signing">



     <KeyInfo xmlns="http://www.w3.org/2000/09/xmldsig#">



     <X509Data>



     <X509Certificate>(...) Certificate 2 (...)</X509Certificate>



     </X509Data>



     </KeyInfo>



     </KeyDescriptor>
     ```

     Be aware that Azure XML metadata might not contain the new certificate immediately after it is created. If you notice that the certificate is missing, wait a few minutes to allow Azure to process the new certificate and then download the XML metadata again.
   * Otherwise, copy the full `<KeyDescriptor use="signing"> (...) </KeyDescriptor>` element in metadata, paste it under the current one, and, in the copy, replace the certificate value with your new certificate value, which is located between the `<ds:X509Certificate>` and `</ds:X509Certificate>` tags in the `<KeyDescriptor>` element you just pasted.
3. Update the metadata on the Dynatrace side only.
4. [Test your configuration.](#test-configuration)
5. If the verification process completes without issues, you can update the certificate on your IdP side.
6. Run the [configuration test](#test-configuration) again.
7. Optional To double-check your configuration, sign out and in again.  
   If you have problems, you can switch back to the older certificate in your IdP and try again.
8. Optional Remove the older certificate from your IdP metadata in Dynatrace.

### Troubleshooting

What are the possible causes of the Dynatrace technical difficulties page?

If, after you authenticate with your IdP, you are redirected to a Dynatrace page such as **Weâve run into technical difficultiesâ¦** or **400 Bad Request**, it's likely that there's a problem with the configuration.

The most common causes of this are:

* Your IdP doesnât accept an `authN` request using our `NameId` format and returns an error response with the status code `InvalidNameIdPolicy`. The `NameIdFormat` must be `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`. You might also need a rule to create a `NameId` using our format.
* You're using a `<saml:Attribute/>` to return the Dynatrace username but the attribute wasn't recognized by Dynatrace; alternatively, we couldn't find it using `NameID` as we didn't recognize its format. See the previous question (`What claim rules do I need in AD FS on the Dynatrace relying party?`) for the proper format.
* Dynatrace didn't trust your IdP SAML signing certificate. The IdP SAML metadata you uploaded did not contain a certificate for signing that matches the certificate in the assertion sent by your IdP. Verify that the certificate is in the metadata XML file that was uploaded to Dynatrace. If you're using a URL to upload the metadata, look at the contents generated by the URL. In some organizations, the SAML signing certificate must be requested separately and manually inserted into the metadata by saving the URL contents to a file, adding the signing certificate to the file, and then uploading the file to us.
* The response from the IdP isn't fully signed (the assertion signature might be present, but it isn't sufficient).
* Your IdP doesn't accept some SAML objects or attributes that the SAML 2.0 specification describes as optionalâcontact a Dynatrace product expert via live chat.

How can I resolve Error AADSTS50105 in an Azure configuration?

If `Error AADSTS50105 - The signed in user is not assigned to a role for the application` occurs during federated authentication with Microsoft Entra ID, it indicates that the user hasn't been granted access to the application in Entra ID.

For details, see the Microsoft documentation:

* [Error AADSTS50105 - The signed in user is not assigned to a role for the applicationï»¿](https://dt-url.net/iz034ci)
* [Quickstart: Create and assign a user accountï»¿](https://dt-url.net/0a234sy)

How can I resolve Error AADSTS76026 in an Azure configuration?

If `Error AADSTS50105 - The request has expired. Try to submit new request.` occurs during federated authentication with Microsoft Entra ID, contrary to the error description, it indicates that the user tried to sign in to Dynatrace by IdP-initiated login (via M365 app launcher) while the Azure application had Signature Verification enabled. This is a limitation of Entra ID, as per [SAML Request Signature Verificationï»¿](https://dt-url.net/0602ymq) in the Microsoft documentation:

*Enabling `Require Verification certificates` will not allow IDP-initiated authentication requests (like SSO testing feature, MyApps or M365 app launcher) to be validated as the IDP would not possess the same private keys as the registered application.*

To resolve this issue, choose one of the following approaches:

* Users need to use the Dynatrace environment URL to sign in to Dynatrace
* Signature Verification needs to be disabled

For details, see the [Microsoft documentationï»¿](https://dt-url.net/0602ymq).

## Glossary

**Term**

**Definition**

**account**

In the account scope, a customer can manage their federations, account verified domains, federated domains, and account default federation. An account is identified by UUID, which is typical for all Dynatrace applications.

**account domain**

When the customer confirms their ownership of a given domain in the process of domain verification in the account, this domain becomes an account verified domain. An account can own multiple verified domains, and multiple accounts can own the same verified domain.

**account default federation**

The default federation for a user who doesn't belong to any of the account federated domains. It's used in [federation discovery](#sp-initiated-authentication-federation-discovery).

**account federated guest**

An account federated guest is created whenever a user logs in through account/environment-specific federation, but does not belong to any verified domain within the account. In this case, SSO creates a new user with a very specific identifier to make sure that this user is tied to a single account and does not interfere with the global user, who may freely be assigned to multiple accounts.

The username of an account federated guest is remapped on the fly as follows:

`<login_part>_<domain_part>@a.<account_uuid>.sso.dynatrace.com`

For example, user `mary.smith@example.com`, in an account with IDM UUID `7f5bab5a-9620-11ee-960a-2fcdafd38a3b`, would become the following account federated guest:

`mary.smith_example.com@a.7f5bab5a-9620-11ee-960a-2fcdafd38a3b.sso.dynatrace.com`

The mapping from the original login to the account federated guest stamp is automatic.

* The user is free to use either their regular or mapped email in the login field.
* In the Account Management **People** list, however, account federated guests are displayed with the mapped value.
* The account UUID, which is part of the mapped login, is not parsed and does not influence the process of environment discovery.

**environment**

Identified by ID, which is unique across Dynatrace (usually called tenantId). The environment belongs to one account. The environment defines how users sign into it. It can have a user-friendly alias. The alias is unique and the environment can have at least one alias.

**environment discovery**

The process used to resolve the environment from the sign-in context. For details, see the [Environment resolution](#sp-initiated-authentication-environment-discovery) section.

**federated domain**

Association between domain and federation. When a user signs in to the account and belongs to a federated domain, they are redirected to federated domain's federation. It can be set on the account or environment scope. It's used in [federation discovery](#sp-initiated-authentication-federation-discovery).

**federation**

Defines Dynatrace as a Service Provider (SP), which delegates sign-in, manages sessions, and manages user groups to the customer's Identity Provider (IdP). This configuration enables linking identities (users) to Dynatrace SSO. It has a unique UUID. The federation IdP ID corresponds to the entity ID from the SAML 2.0 specification. Federation belongs to the account.

**federation discovery**

The process used to choose the federation for signing in users in the SP-initiated authentication. For details, see the [Federation discovery](#sp-initiated-authentication-federation-discovery) section.

**global federation**

Bound to the account verified domain and shared between all accounts having this domain.

**global user**

The user for which, in the current setup, the username, login, and email are synonymous.

**IdP-initiated authentication**

Sign-in process initiated by the federated IDP. For example, when the user wants to open Dynatrace application in the Azure Portal. For details, see the [IdP-initiated authentication](#idp-initiated-authentication) section.

**last used environment cookie**

An optional cookie that contains the environment ID. For details, see the [Environment discovery](#sp-initiated-authentication-environment-discovery)

**SP-initiated authentication**

Sign-in process initiated by Dynatrace. For example, when the user wants to sign into the environment. For details, see the [SP-initiated authentication](#sp-initiated-authentication) section.

**username**

The user enters their username on the SSO sign-in page to sign in. It's in email address format.


---


## Source: scim-azure.md


---
title: Azure SCIM configuration for Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure
scraped: 2026-02-17T21:28:56.636566
---

# Azure SCIM configuration for Dynatrace

# Azure SCIM configuration for Dynatrace

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Aug 06, 2024

This page describes the IdP (**Azure**) end of your **SCIM** SSO configuration, not the Dynatrace end. Use it as part of the entire [SCIM configuration procedure](/docs/manage/identity-access-management/user-and-group-management/access-scim "SCIM") for Dynatrace SaaS if you're using Azure.

While we do our best to provide you with current information, Dynatrace has no control over changes that may be made by third-party providers. Always refer to official third-party documentation from your IdP as your primary source of information for third-party products.

To set up SCIM for your domain

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create SCIM application in Azure**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#create-scim-app "Learn how to configure Dynatrace SCIM in Azure.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure provisioning**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#provisioning "Learn how to configure Dynatrace SCIM in Azure.")[![Step 3 optional](https://dt-cdn.net/images/dotted-step-3-e2082c1921.svg "Step 3 optional")

**Configure group mappings**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#configure-group-mappings "Learn how to configure Dynatrace SCIM in Azure.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Configure user mappings**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#configure-user-mappings "Learn how to configure Dynatrace SCIM in Azure.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Assign users and groups**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#assign-users-and-groups "Learn how to configure Dynatrace SCIM in Azure.")[![Step 6](https://dt-cdn.net/images/step-6-f906c6c957.svg "Step 6")

**Enable SCIM**](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure#enable-scim "Learn how to configure Dynatrace SCIM in Azure.")

## Step 1 Create SCIM application in Azure

In **Microsoft Entra ID**

1. From the leftmost menu, select **Manage** > **Enterprise applications**.
2. Select **New application** > **Create your own application**.
3. In the pop-up window on the right, enter an **Input name** for your app.

   Make sure that you have selected **Integrate any other application you don't find in the gallery (Non-gallery)**.
4. Select **Create**.

## Step 2 Configure provisioning

To configure provisioning in Azure, you need the Dynatrace SCIM base URL and a secret token you got in the [Get Dynatrace SCIM endpoint and create secret token](/docs/manage/identity-access-management/user-and-group-management/access-scim#scim-endpoint-secret-token "SCIM") procedure.

In **Microsoft Entra ID** with your application selected

1. If you're already on the application **Overview** page, select **3. Provision User Accounts** in the **Getting Started** section.

   Alternatively, from the leftmost menu, select **Manage** > **Provisioning**.
2. If you're doing this for the first time, select **Get started**.
3. In **Provisioning Mode**, select **Automatic**.
4. Expand **Admin Credentials**.
5. Enter your admin credentials:

   * **Tenant URL**  
     Example: `https://api.sso.dynatrace.com/idm/public/scim/<YOUR_ACCOUNT_ID>/v2`
   * **Secret Token**  
     You got this token from Dynatrace.
6. Select **Test Connection** to validate the endpoint and credentials.
7. If the test succeeds, select **Save** in the upper-left corner of the page to generate mappings.

   If the test fails, verify your settings:

   * **Tenant URL**  
     Example: `https://api.sso.dynatrace.com/idm/public/scim/<YOUR_ACCOUNT_ID>/v2`
   * **Secret Token**  
     You created this earlier in the [Get a secret token](/docs/manage/identity-access-management/user-and-group-management/access-scim#scim-endpoint-secret-token "SCIM") procedure.

## Step 3 optional Configure group mappings Optional

Do this if you need to provision only certain groups in Dynatrace.

In **Microsoft Entra ID** with your application selected

1. On the **Provisioning** page, expand **Mappings**.
2. Select **Synchronize Azure Active Directory Groups to customappsso**.

   Make sure that the **Enabled** toggle is set to **Yes**.
3. In **Source Object Scope**, select **All records**.
4. Select **Add new filter group**.
5. Fill in the fields.
6. Select **Apply** in the lower-left corner.
7. You can leave all **Target Object Actions** selected.  
   Dynatrace SCIM supports all of these actions.
8. Set **Attribute Mappings** as follows:

   Microsoft Entra ID Attribute

   customappsso Attribute

   `displayName`

   `displayName`

   `objectId`

   `externalId`

   `members`

   `members`
9. Select **Save** on the **Attribute Mapping** page.

## Step 4 Configure user mappings

You need to limit the scope of users that are provisioned by SCIM to those with matching email domains to prevent your SCIM requests from being rejected.

To create a filtering rule for users

1. On the **Provisioning** page, expand **Mappings**.
2. Select **Synchronize Azure Active Directory Users to customappsso**.
3. Select your **Source Object Scope**.
4. Select **Add new filter group**.
5. On **Add Scoping Filter**, fill in the fields as follows:

   * Source Attribute: `mail`
   * Operator: `ENDS_WITH`
   * Clause value: `@<YOUR_DOMAIN>` (for example, `@example.com`)

   Keep in mind that subdomains should be verified for the account separately. Therefore, the `@` in the domain string is required and will guarantee that your requests won't be rejected due to an invalid user domain.
6. Select **Apply** in the lower-left corner.
7. You can leave all **Target Object Actions** selected.  
   Dynatrace SCIM supports all of these actions.
8. Limit **Attribute Mappings** to the following:

   Microsoft Entra ID Attribute

   customappsso Attribute

   `userPrincipalName`

   `userName`

   `Switch([IsSoftDeleted],,"False","True","True","False")`

   `active`

   `displayName`

   `displayName`

   `givenName`

   `name.givenName`

   `surname`

   `name.familyName`
9. Select **Show advanced options** in **Attribute Mappings**, and select **Edit attribute list for customappsso**.
10. Make sure the following checkboxes are selected.

    * For **id**âselect **Primary Key?** and **Required?**
    * For **userName**âselect **Required?**
11. Select **Save** on the **Edit Attribute List** page.
12. Select **Save** on the **Attribute Mapping** page.

## Step 5 Assign users and groups

To assign users or groups to your application and send them via SCIM to Dynatrace, in **Microsoft Entra ID**

1. If you're already on the application **Overview** page, select **1. Assign users and groups** in the **Getting Started** section.

   Alternatively, from the leftmost menu, select **Manage** > **Users**.
2. Select **Add user/group**.
3. Select the **Users and groups** you want to sync.
4. Select **Assign**.

## Step 6 Enable SCIM

To enable SCIM provisioning

1. Go to the **Provisioning** page and expand **Settings**.
2. In **Scope** list, select **Sync only assigned users and groups**.
3. Turn **Provisioning Status** on.

In Azure, the initial sync takes longer than subsequent syncs, which occur approximately every 40 minutes as long as the service is running.

## Troubleshooting

I have accidentally deleted a SCIM synchronized user in Dynatrace my account. Is it possible to re-synchronize the user via SCIM in Azure?

Yes, you can restart SCIM synchronization. To do this, go to the SCIM application's **Overview** tab and select **Restart provisioning**.


---


## Source: scim-okta.md


---
title: Okta SCIM configuration for Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-okta
scraped: 2026-02-17T05:07:48.277977
---

# Okta SCIM configuration for Dynatrace

# Okta SCIM configuration for Dynatrace

* Latest Dynatrace
* How-to guide
* 1-min read
* Published May 14, 2020

This page describes the IdP (**Okta**) end of your **SCIM** SSO configuration, not the Dynatrace end. Use it as part of the entire [SCIM configuration procedure](/docs/manage/identity-access-management/user-and-group-management/access-scim "SCIM") for Dynatrace SaaS if you're using Okta.

While we do our best to provide you with current information, Dynatrace has no control over changes that may be made by third-party providers. Always refer to official third-party documentation from your IdP as your primary source of information for third-party products.

To integrate Dynatrace SCIM in Okta, you will need the Dynatrace SCIM Base URL and a secret token you got in the [Get Dynatrace SCIM endpoint and create secret token](/docs/manage/identity-access-management/user-and-group-management/access-scim#scim-endpoint-secret-token "SCIM") procedure.

Okta provides two possibilities of SCIM integration:

1. [Add SCIM provisioning to already integrated Okta app with Dynatrace SSOï»¿](https://help.okta.com/en/prod/Content/Topics/Apps/Apps_App_Integration_Wizard_SCIM.htm)
2. [Integrate Dynatrace SCIM in separate SCIM Okta Appï»¿](https://developer.okta.com/docs/guides/build-provisioning-integration/prepare-app/)

   * You can use either [SCIM 2.0 Test App (Header Auth)ï»¿](https://www.okta.com/integrations/scim-2-0-test-app-header-auth) or [SCIM 2.0 Test App (OAuth Bearer Token)ï»¿](https://www.okta.com/integrations/scim-2-0-test-app-oauth-bearer-token)

Dynatrace SCIM supports only bearer token authentication. Depending on the Okta application type, while configuring API Credentials the token should be provided with the **Bearer** prefix.


---


## Source: access-scim.md


---
title: SCIM
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim
scraped: 2026-02-17T21:25:28.647320
---

# SCIM

# SCIM

* Latest Dynatrace
* Reference
* 6-min read
* Updated on Jun 30, 2025

System for Cross-domain Identity Management (SCIM) is an open standard for automating the exchange of user identity information between identity domains or IT systems. You can configure Dynatrace SaaS to be provided with user identity information automatically from your organization's identity provider (IdP) through SCIM.

## Benefits of using SCIM with Dynatrace SSO

* Users in your IdP will automatically be synchronized with Dynatrace, so there is no need to invite them manually

  + if a user is disabled or removed from the IdP, it will also disable the user in Dynatrace
* Groups in your IdP will automatically be synchronized with Dynatrace

  + All groups created by SCIM will be of type `SCIM` in Account Management
* Users will be assigned to groups in Dynatrace mirroring the relationship within the IdP

## SCIM notice and limitations

* SCIM synchronization is one-way from the IdP to Dynatrace. This is because technically the IdP is the owner of both the users and groups and changes in Dynatrace will never transpire to the IdP.
* Dynatrace will only accept users with domains, which were verified within the account
* Groups of type `SCIM` are managed by SCIM only and cannot be removed or modified through Account Management
* Permissions to SCIM groups still have to be assigned manually in Dynatrace

  + It is possible to use [Account Management API](/docs/dynatrace-api/account-management-api "Explore endpoints of the Account Management API.") to manage the permissions programmatically
* If your SCIM client does not support dynamic external id changes, email/login change will cause SCIM integration to stop working for such users. Requests will be rejected due to invalid username (in SCIM it is email)
* The scope of users and groups synchronized into Dynatrace with SCIM can be narrowed within the SCIM application in your IdP
* Users in SCIM groups are not listed in the web UI for sharing a document (dashboard or notebook) to specific users or groups unless you add those users to local Dynatrace groups.
* A user cannot be assigned to an account if the account has already reached its [maximum number of assigned users](/docs/manage/identity-access-management/iam-limits "IAM limits for Dynatrace SaaS").
* A user cannot be added to a group if they have already reached the [maximum number of groups they can be assigned to](/docs/manage/identity-access-management/iam-limits "IAM limits for Dynatrace SaaS").

## SCIM requirements and supported features

* Dynatrace supports **SCIM 2.0** and **GET**, **POST**, **PATCH**, **PUT**, and **DELETE** operations for both **User** and **Group** resources.
* For authentication, SCIM requires **Bearer token** in **Authorization header**.
* SCIM is configured for the account and domain scopes. At least one domain ownership verification is required for the account.
* Only users whose email domains have been verified for ownership can be synchronized with Dynatrace via SCIM.
* Required and supported SCIM attributes:

  | SCIM Attribute | Type |
  | --- | --- |
  | userName | email format |
  | name.givenName | string |
  | name.familyName | string |
  | active | boolean |
* **userName** must be persistent. Dynatrace does not support user email change.

## Verify your ownership of the domain

Before you can proceed with SCIM configuration, you need to prove ownership of the domain. Verification is based on a DNS TXT Record check.

For the account, it is sufficient to verify the domain once. If a domain has been verified for SAML, it will be valid for SCIM as well.

To verify ownership of a domain

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Domain verification**.
3. In the **Add domain** section, enter the domain (for example, `mycompanyname.com`) for which you want to set up SCIM and select **Add** to add it to the **Pending domains** table.

   Multiple domains

   If users in your organization use more than one domain to sign in (for example, `@mycompanyname.com` and `@uk.mycompanyname.com`), you can add additional domains in additional rows and start verifying them all in parallel. Enter each domain in a different row.
4. For each domain you are verifying, in the **Pending domains** table, select **Copy** (in the **Value** column) and add the copied TXT resource record to your domainâs DNS configuration.
5. For each domain you are verifying, in the **Pending domains** table, select **Actions** > **Verify** so that Dynatrace can verify that the record was added to your domainâs DNS.

   Propagation time

   It typically takes a few minutes for a record to propagate through the DNS system and the value to become available for Dynatrace to verify. In some cases, it may take up to 24 hours.
6. Each verified domain is added to the **Verified domains** table.

## Get Dynatrace SCIM endpoint and create secret token

Use this procedure to get the Dynatrace SCIM Base URL for your account and create a secret token.

The token is revealed only once during generation time. Copy and paste it into a secure location. If you lose it, you have to generate a new one and replace it in your application.

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **SCIM configuration**.
2. In the **Generate new token** section, optionally enter a token **Description** (or you can add a description for the token later).
3. Select **Generate token**
4. Next to **Token value**, select **Copy** to copy the token to your clipboard, and then paste it into a secure location for later use.

   Dynatrace SCIM supports Bearer Token Authentication only. Example:

   | Header | Value |
   | --- | --- |
   | Authorization | Bearer <DYNATRACE_TOKEN_PLACEHOLDER> |

The SCIM endpoint required for SCIM configuration in your application is added to the **List of tokens**.

## Example IdP-specific instructions

To continue integrating Dynatrace SCIM with your IdP, select the procedure appropriate for your IdP:

* [Azure](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure "Learn how to configure Dynatrace SCIM in Azure.")
* [Okta](/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-okta "Learn how to configure Dynatrace SCIM in Okta.")

## FAQ

Is a change of email address supported?

No, an email address can't be changed by SCIM. Any requests to update an email address are ignored.

How many SCIM authentication tokens can I generate?

You can generate up to 10 SCIM authentication tokens. For security reasons, we strongly recommend that you delete all unused tokens.

Can I provision users from different email domains?

Yes, you can provision as many users from different email domains as you need, as long as all of their domains have been verified. You can verify multiple domains for a single account.

It is possible to create more than one group with the same name?

No, some IdPs, like Azure AD, allow multiple groups with the same name in a single account. For Dynatrace SSO, however, each group name in an account must be unique.

Is it possible to set group `description` during provisioning?

No, we're limited by the SCIM protocol specification, so additional fields, such as `description`, can't be set during provisioning.

### Azure

I have accidentally deleted a SCIM synchronized user in Dynatrace my account. Is it possible to re-synchronize the user via SCIM in Azure?

Yes, you can restart SCIM synchronization. To do this, go to the SCIM application's **Overview** tab and select **Restart provisioning**.


---


## Source: access-service-users.md


---
title: Service users
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-service-users
scraped: 2026-02-17T21:32:15.403490
---

# Service users

# Service users

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Dec 05, 2025

An administrator or a user belonging to a group with `View and manage users and groups` permission can perform the service user management activities listed here.

## What's a service user?

A service user is a non-interactive user: it can't sign in to Dynatrace and it isn't related to any real person. It has its own identity and access management permissions assigned directly.

You can select a service user as the actor of a [workflow](/docs/analyze-explore-automate/workflows/security#service-users "Guide on security aspects of workflow automation in Dynatrace Workflows") or [custom alert](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app#service-user "Explore anomaly detection configurations using the Anomaly Detection app.").

## Use case

When workflows and custom alerts are executed in the context of a service user, it makes them independent of the status of the user who maintains them. This makes it a good fit for a department or production use cases, or any collaborative efforts where a dependency on an actual user could hinder your work. Using a service user also strengthens the security of the actions executed by the actor.

## List and edit service users

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/). If you have more than one account, select the account you want to manage.
2. Go to **Identity & access management** > **Service users**.

   A table lists the defined service users.
3. In the **Actions** column for the user you want to edit, select  >  **Edit**.
4. In the **Edit service user** page, you can:

   * Change the **Name**
   * Change the **Description**

**Note**: You can't change the service user email address. It's the identifier used in policy statements. See [Create policies based on a service user](#policy).

5. On the **Select group** section, you can add or remove the selected groups. Service users get permissions via the selected groups.
6. Select **Save**.

## Create service user

1. On the **Service users** page, select  **Add service user**.
2. On the **Create service user** page, enter the following service user details.

   * **Name**
   * Optional **Description**

     **Tip**: Make sure they're both meaningful for environment admins so that they understand the purpose of the service user.
     The service user's email address is created automatically and can't be modified. It's the identifier used in the [policy statements](#policy).
3. In the **Assign permissions** section, select whether to assign permissions **Through existing groups** or **Directly**.

   * **Through existing groups**: Select one or more existing groups whose permissions you want to assign to this service user.
   * **Directly**: Make your own custom selection of permissions. A new group will be automatically created.

     1. On the **Assign permissions** tab, select a **Permission**, **Scope**, and **Boundaries** to assign to this service user.
     2. On the **View permissions** tab, verify the details of the selected permission.
4. Select **Create**.

## User permissions to use service users as actors

A user who wants to use a service user as an actor of a workflow or custom alert must be granted the `iam:service-users:use` permission.

That permission is granted with the following default policies:

* [Dynatrace Pro User](/docs/manage/identity-access-management/permission-management/default-policies#DynatraceAccessProUser "Dynatrace default policies reference")
* [Dynatrace Admin User](/docs/manage/identity-access-management/permission-management/default-policies#DynatraceAccessAdminUser "Dynatrace default policies reference")

## Create policies based on a service user

To control the use of service users even further, you can create a policy allowing users to use only specific service users as workflows or custom alerts actors.

To do that, create a policy with `iam:service-users:use` set to the `iam:service-user-email` condition

For example:

```
ALLOW iam:service-users:use



WHERE iam:service-user-email IN ("be820735-3114-4d40-9c44-dfa18fa62be9@service.sso.dynatrace.com");
```

Such policies are secure. You can't modify the service user identifier or assign a custom email address to a service user.


---
