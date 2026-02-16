# Dynatrace Documentation: manage/identity-access-management

Generated: 2026-02-16

Files combined: 13

---


## Source: access-tokens.md


---
title: Access tokens classic
source: https://www.dynatrace.com/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens
scraped: 2026-02-16T09:22:07.175320
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


## Source: iam-concepts.md


---
title: Overview of Dynatrace IAM
source: https://www.dynatrace.com/docs/manage/identity-access-management/iam-concepts
scraped: 2026-02-15T09:06:25.796733
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
scraped: 2026-02-16T09:28:48.694109
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


## Source: iam-policy-boundaries.md


---
title: Policy boundaries
source: https://www.dynatrace.com/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/iam-policy-boundaries
scraped: 2026-02-16T09:28:15.568879
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
scraped: 2026-02-16T09:26:42.704801
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
scraped: 2026-02-15T21:20:10.171652
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
scraped: 2026-02-16T09:34:41.855356
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
scraped: 2026-02-15T09:13:15.888833
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
scraped: 2026-02-15T21:22:42.442272
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


## Source: scim-azure.md


---
title: Azure SCIM configuration for Dynatrace
source: https://www.dynatrace.com/docs/manage/identity-access-management/user-and-group-management/access-scim/scim-azure
scraped: 2026-02-15T21:27:14.155315
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
scraped: 2026-02-16T09:29:36.576899
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
scraped: 2026-02-16T09:36:52.684026
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
scraped: 2026-02-16T09:30:03.994665
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
