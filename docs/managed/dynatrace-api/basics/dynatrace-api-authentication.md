---
title: "Dynatrace API - Tokens and authentication"
source: https://docs.dynatrace.com/managed/dynatrace-api/basics/dynatrace-api-authentication
updated: 2026-02-09
---

To be authenticated to use the Dynatrace API, you need a valid access token or a valid personal access token. Access to the API is fine-grained, meaning that you also need the proper scopes assigned to the token. See the description of each request to find out which scopes are required to use it.

For details on OAuth clients, see OAuth clients.

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

## Generate a token

Access token

Personal access token

To generate an access token:

1. Go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

To generate a personal access token

1. Go to **Personal Access Tokens** (accessible via the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform") in the previous Dynatrace).
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

You can assign multiple scopes to a single token, or you can generate several tokens, each with different access levels and use them accordinglyâcheck your organization's security policies for the best practice.

To change the scope of an existing token, use the PUT a token call of the Access tokens API. Note that you need to submit the existing scopes if you want to keep them. Any existing scope missing in the payload is removed.

Alternatively, you can use the POST a token call to generate a token.

## Token scopes

Access token

Personal access token

### OpenPipeline

Name

API value

Description

OpenPipeline - Ingest Events

`openpipeline.events`

Grants access to POST Built-in generic events request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events, Software Development Lifecycle

`openpipeline.events_sdlc`

Grants access to POST Built-in SLDC events request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events, Software Development Lifecycle (Custom)

`openpipeline.events_sdlc.custom`

Grants access to POST Custom SLDC events request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Security Events (Built-in)

`openpipeline.events_security`

Grants access to POST Built-in security events request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Security Events (Custom)

`openpipeline.events_security.custom`

Grants access to POST Custom security events request of the OpenPipeline Ingest API.

OpenPipeline - Ingest Events (Custom)

`openpipeline.events.custom`

Grants access to POST Custom generic event endpoint request of the OpenPipeline Ingest API.

### API v2

Name

API value

Description

Read ActiveGates

`activeGates.read`

Grants access to GET requests of the ActiveGates API.

Write ActiveGates

`activeGates.write`

Grants access to POST and DELETE requests of the ActiveGates API.

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

Grants access to GET requests of the Access tokens API.

Write API tokens

`apiTokens.write`

Grants access to POST, PUT, and DELETE requests of the Access tokens API.

Read attacks

`attacks.read`

Grants access to GET requests of the Attacks API and the Settings API for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`).

Write Application Protection settings

`attacks.write`

Grants access to POST, PUT, and DELETE requests of the Settings API for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`).

Read audit logs

`auditLogs.read`

Grants access to the audit log.

Read credential vault entries

`credentialVault.read`

Grants access to GET requests of the Credential vault API.

Write credential vault entries

`credentialVault.write`

Grants access to POST, PUT, and DELETE requests of the Credential vault API.

Read entities

`entities.read`

Grants access to GET requests of the Monitored entities and Custom tags APIs.

Write entities

`entities.write`

Grants access to POST, PUT, and DELETE requests of the Monitored entities and Custom tags APIs.

Ingest events

`events.ingest`

Grants access to POST request of the Events API v2.

Read events

`events.read`

Grants access to GET requests of the Events API v2.

Read extensions monitoring configuration

`extensionConfigurations.read`

Grants access to GET requests from the **Extensions monitoring configuration** section of the Extensions 2.0 API.

Write extensions monitoring configuration

`extensionConfigurations.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions monitoring configuration** section of the Extensions 2.0 API.

Read extensions environment configuration

`extensionEnvironment.read`

Grants access to GET requests from the **Extensions environment configuration** section of the Extensions 2.0 API.

Write extensions environment configuration

`extensionEnvironment.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions environment configuration** section of the Extensions 2.0 API.

Read extensions

`extensions.read`

Grants access to GET requests from the **Extensions** section of the Extensions 2.0 API.

Write extensions

`extensions.write`

Grants access to POST, PUT, and DELETE requests from the **Extensions** section of the Extensions 2.0 API.

Read Geographic regions

`geographicRegions.read`

Grants access to the Geographic regions API.

Install and update Hub items

`hub.install`

Grants permission to install and update extensions via the Hub items API.

Read Hub related data

`hub.read`

Grants access to GET requests of the Hub items API.

Manage metadata of Hub items

`hub.write`

Grants permission to manage metadata of Hub items via the Hub items API.

Read JavaScript mapping files

`javaScriptMappingFiles.read`

Write JavaScript mapping files

`javaScriptMappingFiles.write`

Ingest logs

`logs.ingest`

Grants access to the POST ingest logs request of the Log Monitoring API v2 as well as the OpenTelemetry log ingest API.

Read logs

`logs.read`

Grants access to the GET requests of the Log Monitoring API v2

Ingest metrics

`metrics.ingest`

Grants access to the POST ingest data points request of the Metrics v2 API as well as the OpenTelemetry metrics ingest API.

Read metrics

`metrics.read`

Grants access to GET requests of the Metrics API v2.

Write metrics

`metrics.write`

Grants access to the DELETE a custom metric request of the Metrics API v2.

Read network zones

`networkZones.read`

Grants access to GET requests of the Network zones API.

Write network zones

`networkZones.write`

Grants access to POST, PUT, and DELETE requests of the Network zones API.

Read OneAgents

`oneAgents.read`

Grants access to GET requests of the OneAgents API.

Write OneAgents

`oneAgents.write`

Grants access to POST and DELETE requests of the OneAgents API.

Ingest OpenTelemetry traces

`openTelemetryTrace.ingest`

Grants permission to ingest OpenTelemetry traces into Dynatrace.").

Read problems

`problems.read`

Grants access to GET requests of the Problems API v2.

Write problems

`problems.write`

Grants access to POST, PUT, and DELETE requests of the Problems API v2.

Read releases

`releases.read`

Grants access to the Releases API.

Read security problems

`securityProblems.read`

Grants access to GET requests of the Security problems API.

Write security problems

`securityProblems.write`

Grants access to POST requests of the Security problems API.

Read settings

`settings.read`

Grants access to GET requests of the Settings API.

Write settings

`settings.write`

Grants access to POST and DELETE requests of the Settings API.

Read SLO

`slo.read`

Grants access to GET requests of the Service-level objectives API.

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the Service-level objectives API.

Read synthetic monitor execution results

`syntheticExecutions.read`

Grants access to GET requests of the `/synthetic/executions` API.

Write synthetic monitor execution results

`syntheticExecutions.write`

Grants access to POST request of `/synthetic/executions` API.

Read synthetic locations

`syntheticLocations.read`

Grants access to GET requests of the Synthetic locations API v2 and Synthetic nodes API v2.

Write synthetic locations

`syntheticLocations.write`

Grants access to POST, PUT, and DELETE requests of the Synthetic locations API v2 and Synthetic nodes API v2.

Tenant token rotation

`tenantTokenRotation.write`

Grants access to the Tenant tokens API.

Look up a single trace

`traces.lookup`

Checks for the presence of a trace in cross-environment tracing.

Read Unified Analysis page

`unifiedAnalysis.read`

Grants access to the Unified analysis schema in the Settings API.

### API v1

Name

API value

Description

Access problems and event feed, metrics, and topology

`DataExport`

Grants access to various calls of Environment API.

Create and read synthetic monitors, locations, and nodes

`ExternalSyntheticIntegration`

Grants access to the Synthetic API.

Read synthetic monitors, locations, and nodes

`ReadSyntheticData`

Grants access to GET requests of Synthetic API.

Read configuration

`ReadConfig`

Grants access to GET calls of Configuration API.

Write configuration

`WriteConfig`

Grants access to POST, PUT, and DELETE calls of Configuration API.

Change data privacy settings

`DataPrivacy`

Grants access to Data privacy API and data privacy calls of Web application configuration API.

User sessions

`DTAQLAccess`

Grants access to User sessions API.

Anonymize user sessions for data privacy reasons

`UserSessionAnonymization`

Grants access to Anonymization API.

Mobile symbol file management

`DssFileManagement`

Grants access to Mobile symbolication API.

Real User Monitoring JavaScript tag management

`RumJavaScriptTagManagement`

Grants access to Real User Monitoring JavaScript API.

ActiveGate certificate management

`ActiveGateCertManagement`

Grants permission to configure certificate on private ActiveGates.

Fetch data from a remote environment

`RestRequestForwarding`

Grants permission to fetch data from remote Dynatrace environments for multi-environment dashboarding.

Capture request data

`CaptureRequestData`

Grants access to Request attributes API.

Read log content

`LogExport`

Grants access to Log Monitoring API.

### PaaS

Name

API value

Description

Download OneAgent and ActiveGate installers

`InstallerDownload`

Allows download of installers via Deployment API.

Create support alerts

`SupportAlert`

Allows creation of support alerts for crash analysis.

### Other

Name

API value

Description

Upload plugins using the command line

`PluginUpload`

Grants permission to upload OneAgent extensions via Extension SDK.

Dynatrace provides the following permissions for personal access tokens. You can set them in the web UI as described above or via the **Access tokens** API.

Name

API value

Description

Read API tokens

`apiTokens.read`

Grants access to GET requests of the Access tokens API.

Write API tokens

`apiTokens.write`

Grants access to POST, PUT, and DELETE requests of the Access tokens API.

Read entities

`entities.read`

Grants access to GET requests of the Monitored entities and Custom tags APIs.

Write entities

`entities.write`

Grants access to POST, PUT, and DELETE requests of the Monitored entities and Custom tags APIs.

Read metrics

`metrics.read`

Grants access to GET requests of the Metrics API v2.

Write metrics

`metrics.write`

Grants access to the DELETE a custom metric request of the Metrics API v2.

Read network zones

`networkZones.read`

Grants access to GET requests of the Network zones API.

Write network zones

`networkZones.write`

Grants access to POST, PUT, and DELETE requests of the Network zones API.

Read problems

`problems.read`

Grants access to GET requests of the Problems API v2.

Write problems

`problems.write`

Grants access to POST, PUT, and DELETE requests of the Problems API v2.

Read releases

`releases.read`

Grants access to the Releases API.

Read security problems

`securityProblems.read`

Grants access to GET requests of the Security problems API.

Write security problems

`securityProblems.write`

Grants access to POST requests of the Security problems API.

Read settings

`settings.read`

Grants access to GET requests of the Settings API.

Write settings

`settings.write`

Grants access to POST and DELETE requests of the Settings API.

Read SLO

`slo.read`

Grants access to GET requests of the Service-level objectives API.

Write SLO

`slo.write`

Grants access to POST, PUT, and DELETE requests of the Service-level objectives API.

## Authenticate

You have two options to pass your API token: in the **Authorization** HTTP header or in the **api-token** query parameter.

We recommend that you use the **Authorization** header, as URLs (along with tokens passed within them) might be logged in various locations. Users might also bookmark the URLs or share them in plain text. Therefore, placing authentication tokens into the URL increases the risk that they will be captured by an attacker.

HTTP header

Query parameter

You can authenticate by attaching the token to the **Authorization** HTTP header preceding the **Api-Token** realm.

```
--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

The following example shows authentication via HTTP header.

```
curl --request GET \


--url https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion \


--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

You can authenticate by adding the token as the value of the **api-token** query parameter.

```
curl --request GET \


--url 'https://mySampleEnv.live.dynatrace.com/api/v1/config/clusterversion?api-token=abcdefjhij1234567890' \
```

### Authentication in the API Explorer

Select the lock ![Lock](https://dt-cdn.net/images/blue-lock-icon-77090b9928.svg "Lock") icon next to any end point to display information about the OAuth 2.0 tokens that secure that endpoint. Each endpoint requires a specific token type.

You can also unlock all endpoints by selecting **Authorize**. In the displayed dialog, you can then see which token permissions are necessary for each API endpoint. By entering your OAuth 2.0 token into the global **Available authorizations** dialog, you can unlock all related API endpoints.

## Related topics

* Access tokens
