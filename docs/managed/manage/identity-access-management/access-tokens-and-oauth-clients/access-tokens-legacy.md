---
title: Access tokens
source: https://docs.dynatrace.com/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens-legacy
scraped: 2026-05-12T12:01:26.665309
---

# Access tokens

# Access tokens

* Reference
* 3-min read
* Published Nov 03, 2018

All external access to your Dynatrace monitoring environment relies on two pieces of information: the [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") and an *access token*.

Dynatrace uses several types of tokens:

* API tokens and personal access tokens grant access to the [Dynatrace API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API.")
* PaaS tokens allow download of OneAgent and ActiveGate installers
* Tenant tokens allow OneAgent to report data to Dynatrace
* Module tokens grant access to module integrations.

## Token format

Dynatrace uses a unique token format consisting of three components separated by dots (`.`).

### Token example

`dt0s01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM`

### Token components

| Component name | Component description |
| --- | --- |
| prefix | The **prefix** identifies the token type.  In our example: `dt0s01`  See [Token prefixes](#token-format-prefixes) below for a table of standard prefixes. |
| public portion | The **public portion** of the token is a 24-character public identifier.  In our example: `ST2EY72KQINMH574WMNVI7YN` |
| token identifier | The **token identifier** is the combination of the **prefix** and the **public portion**. A token identifier can be safely displayed in the UI and can be used for logging purposes.  In our example: `dt0s01.ST2EY72KQINMH574WMNVI7YN` |
| secret portion | The **secret portion** of the token is a 64-character string that should be treated like a password:  * Don't display it * Don't store it in log files * Rotate it instantly if it's leaked  In our example: `G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM` |

### Token prefixes

| Prefix | Description |
| --- | --- |
| `dt0s01` | This is an API token. It's used as an authorization method: a valid token allows the user to make changes within the Dynatrace account through SCIM.  * It is generated once. * Do not reveal the secret portion of a `dt0s01` token. * The public portion is used for identification in the web UI, but you generally should not reveal it (or any portion of this token). * This token remains in effect until invalidated by the customer, so you must rotate it instantly if it is ever leaked. |
| `dt0s02` | OAuth2 Clients created by users through Account Management to be used with Dynatrace Apps and Account Management API. |
| `dt0s03` | OAuth2 Clients for internal and external services and integrations. |
| `dt0s04` | Chat and identity linking. |
| `dt0s06` | This is an OAuth2 Refresh Token, which is used to retrieve a new Access Token and generally changes frequently (typically every 5 to 15 minutes). |
| `dt0s08` | OAuth2 Clients for internal and external services and integrations. |
| `dt0s09` | Chat and identity linking. |
| `dt0s16` | Platform Token enabling programmatic access to Dynatrace platform services. |

The predictable format gives you several advantages, such as:

* Using Git pre-commit hooks to avoid pushing tokens to source code repositories (for example, using tools like [git-secretsï»¿](https://github.com/awslabs/git-secrets))
* Defining masking rules to obfuscate the secret portions of tokens when writing log files
* Detecting tokens in internal files or communications
* Enabling the [GitHub secret scanning serviceï»¿](https://docs.github.com/en/free-pro-team@latest/github/administering-a-repository/about-secret-scanning#about-secret-scanning-for-public-repositories) to identify any token pushed to a public GitHub repository

Use this regular expression to look for tokens:

```
dt0[a-zA-Z]{1}[0-9]{2}\.[A-Z0-9]{24}\.[A-Z0-9]{64}
```

With the rollout of Dynatrace version 1.210, this format is enabled by default (all newly generated tokens will use the new format).

All existing tokens of the old format remain valid.

### Disable the new format

For a limited time, you have the option to opt out of using the new token format. To find the setting, in the CMC web UI, go to **Settings > API tokens**.

## API token

API tokens are used by Dynatrace API to authenticate various [API calls](/managed/dynatrace-api "Find out what you need to use the Dynatrace API."). API tokens have fine-grained scopes to limit access to specific product functionality for security reasons.

### Token scopes

View available scopes

### OpenPipeline

| Name | API value | Description |
| --- | --- | --- |
| OpenPipeline - Ingest Events | `openpipeline.events` | Grants access to [POST Built-in generic events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") request of the OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle | `openpipeline.events_sdlc` | Grants access to [POST Built-in SLDC events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") request of the OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events, Software Development Lifecycle (Custom) | `openpipeline.events_sdlc.custom` | Grants access to [POST Custom SLDC events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") request of the OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Built-in) | `openpipeline.events_security` | Grants access to [POST Built-in security events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") request of the OpenPipeline Ingest API. |
| OpenPipeline - Ingest Security Events (Custom) | `openpipeline.events_security.custom` | Grants access to [POST Custom security events](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") request of the OpenPipeline Ingest API. |
| OpenPipeline - Ingest Events (Custom) | `openpipeline.events.custom` | Grants access to [POST Custom generic event endpoint](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") request of the OpenPipeline Ingest API. |

### API v2

| Name | API value | Description |
| --- | --- | --- |
| Read ActiveGates | `activeGates.read` | Grants access to GET requests of the [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers."). |
| Write ActiveGates | `activeGates.write` | Grants access to POST and DELETE requests of the [ActiveGates API](/managed/dynatrace-api/environment-api/activegates "Learn what the Dynatrace ActiveGate API offers."). |
| Create ActiveGate tokens | `activeGateTokenManagement.create` | Grants access to the POST request of the ActiveGate tokens API. |
| Read ActiveGate tokens | `activeGateTokenManagement.read` | Grants access to GET requests of the ActiveGate tokens API. |
| Write ActiveGate tokens | `activeGateTokenManagement.write` | Grants access to POST and DELETE requests of the ActiveGate tokens API. |
| Read API tokens | `apiTokens.read` | Grants access to GET requests of the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Write API tokens | `apiTokens.write` | Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Read attacks | `attacks.read` | Grants access to GET requests of the Attacks API and the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`). |
| Write Application Protection settings | `attacks.write` | Grants access to POST, PUT, and DELETE requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") for Application Protection (`builtin:appsec.attack-protection-settings`, `builtin:appsec.attack-protection-advanced-config`, and `builtin:appsec.attack-protection-allowlist-config schemas`). |
| Read audit logs | `auditLogs.read` | Grants access to the [audit log](/managed/manage/data-privacy-and-security/configuration/audit-logs-api "Learn how to manage audit logs using an API."). |
| Read credential vault entries | `credentialVault.read` | Grants access to GET requests of the [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers."). |
| Write credential vault entries | `credentialVault.write` | Grants access to POST, PUT, and DELETE requests of the [Credential vault API](/managed/dynatrace-api/environment-api/credential-vault "Learn what the Dynatrace API for credentials offers."). |
| Read entities | `entities.read` | Grants access to GET requests of the [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs. |
| Write entities | `entities.write` | Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs. |
| Ingest events | `events.ingest` | Grants access to POST request of the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). |
| Read events | `events.read` | Grants access to GET requests of the [Events API v2](/managed/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2."). |
| Read extensions monitoring configuration | `extensionConfigurations.read` | Grants access to GET requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions monitoring configuration | `extensionConfigurations.write` | Grants access to POST, PUT, and DELETE requests from the **Extensions monitoring configuration** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read extensions environment configuration | `extensionEnvironment.read` | Grants access to GET requests from the **Extensions environment configuration** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions environment configuration | `extensionEnvironment.write` | Grants access to POST, PUT, and DELETE requests from the **Extensions environment configuration** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read extensions | `extensions.read` | Grants access to GET requests from the **Extensions** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Write extensions | `extensions.write` | Grants access to POST, PUT, and DELETE requests from the **Extensions** section of the [Extensions 2.0 API](/managed/dynatrace-api/environment-api/extensions-20 "Learn how to manage extensions with the Dynatrace Extensions 2.0 API."). |
| Read Geographic regions | `geographicRegions.read` | Grants access to the [Geographic regions API](/managed/dynatrace-api/environment-api/rum/geographic-regions "View requests available through the Dynatrace Geographic regions API."). |
| Install and update Hub items | `hub.install` | Grants permission to install and update extensions via the [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Read Hub related data | `hub.read` | Grants access to GET requests of the [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Manage metadata of Hub items | `hub.write` | Grants permission to manage metadata of Hub items via the [Hub items API](/managed/dynatrace-api/environment-api/hub "Learn how to access Dynatrace Hub features via the Hub items API."). |
| Read JavaScript mapping files | `javaScriptMappingFiles.read` |  |
| Write JavaScript mapping files | `javaScriptMappingFiles.write` |  |
| Ingest logs | `logs.ingest` | Grants access to the [POST ingest logs](/managed/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs "Push custom logs to Dynatrace via the Log Monitoring API v2.") request of the Log Monitoring API v2 as well as the [OpenTelemetry log ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). |
| Read logs | `logs.read` | Grants access to the GET requests of the [Log Monitoring API v2](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.") |
| Ingest metrics | `metrics.ingest` | Grants access to the [POST ingest data points](/managed/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.") request of the Metrics v2 API as well as the [OpenTelemetry metrics ingest API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). |
| Read metrics | `metrics.read` | Grants access to GET requests of the [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). |
| Write metrics | `metrics.write` | Grants access to the [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2. |
| Read network zones | `networkZones.read` | Grants access to GET requests of the [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Write network zones | `networkZones.write` | Grants access to POST, PUT, and DELETE requests of the [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Read OneAgents | `oneAgents.read` | Grants access to GET requests of the [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API."). |
| Write OneAgents | `oneAgents.write` | Grants access to POST and DELETE requests of the [OneAgents API](/managed/dynatrace-api/environment-api/oneagent-on-a-host/get-all-hosts-with-oneagents "Check the configuration of OneAgent instances on your hosts via Dynatrace API."). |
| Ingest OpenTelemetry traces | `openTelemetryTrace.ingest` | Grants permission to [ingest OpenTelemetry traces](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."). |
| Read problems | `problems.read` | Grants access to GET requests of the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Write problems | `problems.write` | Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Read releases | `releases.read` | Grants access to the [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers."). |
| Read security problems | `securityProblems.read` | Grants access to GET requests of the [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Write security problems | `securityProblems.write` | Grants access to POST requests of the [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Read settings | `settings.read` | Grants access to GET requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Write settings | `settings.write` | Grants access to POST and DELETE requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Read SLO | `slo.read` | Grants access to GET requests of the [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Write SLO | `slo.write` | Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Read synthetic monitor execution results | `syntheticExecutions.read` | Grants access to GET requests of the `/synthetic/executions` API. |
| Write synthetic monitor execution results | `syntheticExecutions.write` | Grants access to POST request of `/synthetic/executions` API. |
| Read synthetic locations | `syntheticLocations.read` | Grants access to GET requests of the [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API."). |
| Write synthetic locations | `syntheticLocations.write` | Grants access to POST, PUT, and DELETE requests of the [Synthetic locations API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.") and [Synthetic nodes API v2](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-nodes-v2 "Manage synthetic nodes via the Synthetic v2 API."). |
| Tenant token rotation | `tenantTokenRotation.write` | Grants access to the [Tenant tokens API](/managed/dynatrace-api/environment-api/tokens-v2/tenant-tokens "Rotate Dynatrace tenant tokens."). |
| Look up a single trace | `traces.lookup` | Checks for the presence of a trace in cross-environment tracing. |
| Read Unified Analysis page | `unifiedAnalysis.read` | Grants access to the Unified analysis schema in the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |

### API v1

| Name | API value | Description |
| --- | --- | --- |
| Access problems and event feed, metrics, and topology | `DataExport` | Grants access to various calls of [Environment API](/managed/dynatrace-api/environment-api "Find out what you need to use the environment section of the Dynatrace API."). |
| Create and read synthetic monitors, locations, and nodes | `ExternalSyntheticIntegration` | Grants access to the [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers."). |
| Read synthetic monitors, locations, and nodes | `ReadSyntheticData` | Grants access to GET requests of [Synthetic API](/managed/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers."). |
| Read configuration | `ReadConfig` | Grants access to GET calls of [Configuration API](/managed/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API."). |
| Write configuration | `WriteConfig` | Grants access to POST, PUT, and DELETE calls of [Configuration API](/managed/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API."). |
| Change data privacy settings | `DataPrivacy` | Grants access to [Data privacy API](/managed/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.") and data privacy calls of [Web application configuration API](/managed/dynatrace-api/configuration-api/rum/web-application-configuration-api "Learn what the Dynatrace web application config API offers."). |
| User sessions | `DTAQLAccess` | Grants access to [User sessions API](/managed/dynatrace-api/environment-api/rum/user-sessions "Learn what the Dynatrace User Sessions Query language API offers."). |
| Anonymize user sessions for data privacy reasons | `UserSessionAnonymization` | Grants access to [Anonymization API](/managed/dynatrace-api/environment-api/anonymization "Find out how fulfill GDPR requirements by using the Dynatrace API to remove user data."). |
| Mobile symbol file management | `DssFileManagement` | Grants access to [Mobile symbolication API](/managed/dynatrace-api/configuration-api/mobile-symbolication-api "Manage mobile symbol files via the Dynatrace API."). |
| Real User Monitoring JavaScript tag management | `RumJavaScriptTagManagement` | Grants access to [Real User Monitoring JavaScript API](/managed/dynatrace-api/environment-api/rum/real-user-monitoring-javascript-code "Learn how you can use the Dynatrace API to set up and maintain your manually injected applications using the Real User Monitoring JavaScript API."). |
| ActiveGate certificate management | `ActiveGateCertManagement` | Grants permission to [configure certificate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.") on private ActiveGates. |
| Fetch data from a remote environment | `RestRequestForwarding` | Grants permission to fetch data from [remote Dynatrace environments](/managed/dynatrace-api/configuration-api/remote-environments "Manage configurations of remote Dynatrace environments via the Dynatrace configuration API.") for multi-environment dashboarding. |
| Capture request data | `CaptureRequestData` | Grants access to [Request attributes API](/managed/dynatrace-api/configuration-api/service-api/request-attributes-api "Learn what the Dynatrace request attribute config API offers."). |
| Read log content | `LogExport` | Grants access to [Log Monitoring API](/managed/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2."). |

### PaaS

| Name | API value | Description |
| --- | --- | --- |
| Download OneAgent and ActiveGate installers | `InstallerDownload` | Allows download of installers via [Deployment API](/managed/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API."). |
| Create support alerts | `SupportAlert` | Allows creation of [support alerts](/managed/observe/application-observability/profiling-and-optimization/crash-analysis#support-alert "Learn how Dynatrace can help you gain insight into process crashes.") for crash analysis. |

### Other

| Name | API value | Description |
| --- | --- | --- |
| Upload plugins using the command line | `PluginUpload` | Grants permission to upload OneAgent extensions via [Extension SDK](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace."). |

### Create an API token

To generate an API token

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Find and select the required permissions for the token in the scopes list.
5. Select **Generate token**.
6. Select **Copy** to copy the generated token to the clipboard. Store the token in a password manager for future use.

You can assign multiple permissions to a single token, or you can generate several tokens, each with different access levels and use them accordinglyâcheck your organization's security policies for the best practice.

Alternatively, you can use the [POST a token](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token "Create an access token via Dynatrace API.") call of the **Access tokens** API to generate a token.

Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.

## PaaS token

PaaS tokens are used to download OneAgent and ActiveGate installers. To generate a PaaS token

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.
4. Find and select the required permissions for the token in the scopes list.
5. Select **Generate token**.
6. Select **Copy** to copy the generated token to the clipboard. Store the token in a password manager for future use.

Alternatively, you can use the [POST a new token](/managed/dynatrace-api/environment-api/tokens-v1/post-new-token "Learn how to use the Dynatrace API to create a new Dynatrace API authentication token.") API call to generate a token with the `InstallerDownload` and `SupportAlert` permissions.

## Tenant token

The tenant token is used by OneAgents and ActiveGates to report data to Dynatrace. Dynatrace automatically generates the tenant token and adds it to OneAgent and ActiveGate installers on download.

### Access a tenant token

To obtain a tenant token for your environment, execute the [GET connectivity information for OneAgent](/managed/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") request of the Deployment API. You will find the tenant token in the `tenantToken` field of the response body. You'll need your PaaS token to authenticate the request.

### Rotate tenant token

You can change the tenant token as needed (for example, to adhere to internal security policies or respond to unintended exposure). The procedure for changing the tenant token is called *tenant token rotation*. To learn how to rotate tenant tokens, see [Tenant token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/rotate-tenant-token "Learn what a tenant token is and how to change it.").

## Personal access token

All the above-mentioned tokens require admin rights to generate. With **personal access tokens**, you can generate a token for API usage without admin rights. Available scopes are bound to your permissions, meaning that you can only use the API counterparts of features you're already authorized to use. You're also limited to the data from management zones you have access to.

A personal access token is bound to you. You can't generate a personal access token for another user.

### Enable personal access tokens

Admin rights are required to enable this feature. After it's enabled, any user can generate a personal access token.

To enable personal access tokens

1. Go to **Settings** and select **Integration** > **Token settings**.
2. Turn on **Enable personal access tokens**.

### Generate personal access tokens

To generate a personal access token

1. Go to **Personal Access Tokens** (accessible via the [user menu](/managed/discover-dynatrace/get-started/dynatrace-ui#user-menu-previous-dynatrace "Navigate the Dynatrace Managed platform") in the previous Dynatrace).
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the required scopes for the token.
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

### Token scopes

View available scopes

Dynatrace provides the following permissions for personal access tokens. You can set them in the web UI as described above or via the [**Access tokens** API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.").

| Name | API value | Description |
| --- | --- | --- |
| Read API tokens | `apiTokens.read` | Grants access to GET requests of the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Write API tokens | `apiTokens.write` | Grants access to POST, PUT, and DELETE requests of the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens."). |
| Read entities | `entities.read` | Grants access to GET requests of the [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs. |
| Write entities | `entities.write` | Grants access to POST, PUT, and DELETE requests of the [Monitored entities](/managed/dynatrace-api/environment-api/entity-v2 "Learn about the Dynatrace Monitored entities API.") and [Custom tags](/managed/dynatrace-api/environment-api/custom-tags "Manage custom tags of the monitored entities via the Dynatrace API.") APIs. |
| Read metrics | `metrics.read` | Grants access to GET requests of the [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). |
| Write metrics | `metrics.write` | Grants access to the [DELETE a custom metric](/managed/dynatrace-api/environment-api/metric-v2/delete-metric "Delete a metric ingested via Metrics v2 API.") request of the Metrics API v2. |
| Read network zones | `networkZones.read` | Grants access to GET requests of the [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Write network zones | `networkZones.write` | Grants access to POST, PUT, and DELETE requests of the [Network zones API](/managed/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API."). |
| Read problems | `problems.read` | Grants access to GET requests of the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Write problems | `problems.write` | Grants access to POST, PUT, and DELETE requests of the [Problems API v2](/managed/dynatrace-api/environment-api/problems-v2 "Find out what the Dynatrace Problems v2 API offers."). |
| Read releases | `releases.read` | Grants access to the [Releases API](/managed/dynatrace-api/environment-api/releaseapi "Find out what the Dynatrace Releases API offers."). |
| Read security problems | `securityProblems.read` | Grants access to GET requests of the [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Write security problems | `securityProblems.write` | Grants access to POST requests of the [Security problems API](/managed/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers."). |
| Read settings | `settings.read` | Grants access to GET requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Write settings | `settings.write` | Grants access to POST and DELETE requests of the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."). |
| Read SLO | `slo.read` | Grants access to GET requests of the [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |
| Write SLO | `slo.write` | Grants access to POST, PUT, and DELETE requests of the [Service-level objectives API](/managed/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers."). |