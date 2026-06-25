---
title: Personal access token
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token
scraped: 2026-05-12T11:14:04.904893
---

# Personal access token

# Personal access token

* 6-min read
* Published Sep 15, 2021

Normally, access tokens require admin rights to generate. With *personal access tokens*, however, you can generate a token for API usage without admin rights. Available scopes are not pre-filtered based on your user permissions. Instead, your permissions are checked whenever you use your personal access token to authorize a request. You're also limited to the data from management zones you have access to.

A personal access token is bound to you. You can't generate a personal access token for another user.

## Enable personal access tokens

Admin rights are required to enable this feature. After it's enabled, any user can generate a personal access token.

To enable personal access tokens

1. Go to **Settings** and select **Integration** > **Access tokens**.
2. Turn on **Enable personal access tokens**.

## Generate personal access tokens

To generate a personal access token

1. Go to **Personal Access Tokens** (accessible via the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform") in the previous Dynatrace).
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

## Available scopes

| Name | API value | Description |
| --- | --- | --- |
| Read ActiveGates | `activeGates.read` | Grants access to GET requests of the [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers."). |
| Write ActiveGates | `activeGates.write` | Grants access to POST and DELETE requests of the [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers."). |
| Read analyzers | `analyzers.read` |  |
| Write and execute analyzers | `analyzers.write` |  |
| Read API tokens | `apiTokens.read` | Grants access to GET requests of the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Write API tokens | `apiTokens.write` | Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Read attacks | `attacks.read` | Grants access to GET requests of the Attacks API and attack-related schemas in the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Write Application Protection settings | `attacks.write` | Grants access to POST, PUT, and DELETE requests of the Settings API for Application Protection. |
| Read entities | `entities.read` | Grants access to GET requests of the [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs. |
| Write entities | `entities.write` | Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs. |
| Ingest events | `events.ingest` | Grants access to POST request of the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). |
| Read events | `events.read` | Grants access to GET requests of the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). |
| Actions for extension monitoring configurations | `extensionConfigurationActions.write` |  |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Grants access to GET requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Grants access to POST, PUT, and DELETE requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read extensions | `extensions.read` | Grants access to GET requests from the **Extensions** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions | `extensions.write` | Grants access to POST, PUT, and DELETE requests from the **Extensions** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read Geographic regions | `geographicRegions.read` | Grants access to GET requests of the Geographic regions API. |
| Install and update Hub items | `hub.install` | Grants permission to install and update extensions via the [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Read Hub-related data | `hub.read` | Grants access to GET requests of the [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Grants permission to manage metadata of [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` | Grants access to GET requests of the JavaScript mapping files API. |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` | Grants access to PUT and DELETE requests of the JavaScript mapping files API. |
| Read metrics | `metrics.read` | Grants access to GET requests of the [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). |
| Write metrics | `metrics.write` | Grants access to the [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2. |
| Read network zones | `networkZones.read` | Grants access to GET requests of the [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Write network zones | `networkZones.write` | Grants access to POST, PUT, and DELETE requests of the [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Read OneAgents | `oneAgents.read` | Grants access to GET requests of the [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Grants access to POST and DELETE requests of the [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API."). |
| Read problems | `problems.read` | Grants access to GET requests of the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Write problems | `problems.write` | Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Read releases | `releases.read` | Grants access to the [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers."). |
| Read RUM cookie names | `rumCookieNames.read` |  |
| Read security problems | `securityProblems.read` | Grants access to GET requests of the [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Write security problems | `securityProblems.write` | Grants access to POST requests of the [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Read settings | `settings.read` | Grants access to GET requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Write settings | `settings.write` | Grants access to POST and DELETE requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Read SLOs | `slo.read` | Grants access to GET requests of the [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Write SLOs | `slo.write` | Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Look up a single trace | `traces.lookup` | Check whether a trace is present. This is required to use cross-environment tracing. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Grants access to the Unified analysis schema in the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |

## Related topics

* [Tokens API v1](/managed/dynatrace-api/environment-api/tokens-v1 "Learn how to manage Dynatrace API authentication tokens in your environment.")