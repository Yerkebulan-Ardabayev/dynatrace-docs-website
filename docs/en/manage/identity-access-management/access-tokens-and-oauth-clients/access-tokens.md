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