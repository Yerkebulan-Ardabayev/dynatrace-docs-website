---
title: Monaco API support and access permission handling
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/monaco/monaco-api-support-and-access-handling
scraped: 2026-02-17T05:06:15.123293
---

# Monaco API support and access permission handling

# Monaco API support and access permission handling

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 27, 2025

Dynatrace offers different options to authenticate API calls. Dynatrace Monaco supports the following authentication options:

* Platform tokens
* OAuth clients

For details about Dynatrace Identity and Access Management (including platform tokens,API tokens, and OAuth clients), see [Tokens and OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients "Tokens and OAuth clients").

## Create a platform token for the Dynatrace Monaco CLI

To create a platform token, follow the steps described in [Create a platform token for the Dynatrace Monaco CLI](/docs/deliver/configuration-as-code/monaco/guides/create-platform-token "Create a platform token for Dynatrace Configuration as Code via Monaco.").
Each available type of platform configuration requires specific [OAuth scopes](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

## Create an OAuth client for the Dynatrace Monaco CLI

To create an OAuth client, follow the steps described in [Create an OAuth2 client](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients#create-an-oauth2-client "Manage authentication and user permissions using OAuth clients.").

Each available type of platform configuration requires specific [OAuth scopes](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

To use the `automation:workflows:admin` scope, you need to do the following before creating the OAuth client.

1. Create a custom policy granting that scope.
2. Bind a group to it.
3. Assign your user to that group.

For detailed information on managing policies, see [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

To manage OpenPipeline configurations, ensure that the user belongs to a group with the policy **Data Processing and Storage** assigned to it.
Do this before creating the OAuth client.

In addition to the scopes available to the OAuth client, permissions can be further limited via policies applied to the user's groups.

When working with a service user, ensure the service user's permissions match the OAuth scopes for all environments.
For details on how permissions can be controlled, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

To use your OAuth client:

1. Follow the instructions for your operating system or CI/CD tool on how to make the client ID and secret available as environment variables.
2. Reference the environment variables you have created in the OAuth section of your manifest file
3. Dynatrace Monaco CLI will request OAuth access tokens using your client credentials to make authenticated API calls.

## API coverage

Dynatrace Monaco supports the following configuration types:

* Settings 2.0
* Configuration APIs
* Platform APIs

The specific configuration types are defined in the Monaco configuration YAML file.

### Settings 2.0

Settings 2.0 resources require a classic Dynatrace API access token or OAuth credentials.

The Dynatrace Monaco CLI provides general support for any Settings 2.0 schema available in your environment.
For information about schemas, see [Settings 2.0 - Available schemas](/docs/dynatrace-api/environment-api/settings/schemas "View the entire settings schemas table of your monitoring environment via the Dynatrace API.").

For latest Dynatrace, you will need the following OAuth scopes.

| Purpose | Scope |
| --- | --- |
| Manage Settings 2.0 objects and its all-users permission | `settings:objects:read`, `settings:objects:write` |
| View Settings 2.0 schemas | `settings:schemas:read` |

For classic Dynatrace, you will need the following OAuth scopes.

| Purpose | Scope |
| --- | --- |
| Manage Settings 2.0 objects and its all-users permission | `settings.read`, `settings.write` |

### Supported platform API types

The Dynatrace platform provides a collection of [platform servicesï»¿](https://developer.dynatrace.com/plan/platform-services/), each with a specific area of responsibility.
OAuth credentials are required to target platform APIs.

The Dynatrace Monaco CLI provides support for Dynatrace platform API types as described in the table below.

Platform service

Configuration type

Endpoint

OAuth client permissions

Monaco CLI version

Automation

`business-calendars`

`/platform/automation/v1/business-calendars`

`automation:calendars:read`, `automation:calendars:write`

2.6.0+

Automation

`scheduling-rules`

`/platform/automation/v1/scheduling-rules`

`automation:rules:read`, `automation:rules:write`

2.6.0+

Automation

`workflows`

`/platform/automation/v1/workflow`

`automation:workflows:read`, `automation:workflows:write`

2.6.0+

Grailâ-storage management

`buckets`

`/platform/storage/management/v1/bucket-definitions`

`storage:bucket-definitions:read`, `storage:bucket-definitions:write`, `storage:bucket-definitions:delete`

2.9.0+

Documents (Dashboards, Notebooks, Launchpads)

`documents`

`/platform/document/v1/documents`

`document:documents:write`, `document:documents:read`, `document:documents:delete`, `document:trash.documents:delete`

2.15.0+

OpenPipeline

`openpipelines`

`/platform/openpipeline/v1/configurations`

`openpipeline:configurations:read`, `openpipeline:configurations:write`

2.15.0+

Grail

`segment`

`/platform/storage/filter-segments/v1/filter-segments`

`storage:filter-segments:read`, `storage:filter-segments:write`, `storage:filter-segments:delete`, `storage:filter-segments:admin`

2.19.0+

SLOs

`slo-v2`

`/platform/slo/v1/slos`

`slo:slos:read`, `slo:slos:write`, `slo:objective-templates:read`

2.22.0+

### Account Management permissions

To manage account resources, such as user management or policy handling, OAuth credentials require the following permissions:

* `account-idm-read`
* `account-idm-write`
* `account-env-read`
* `account-env-write`
* `iam-policies-management`
* `iam:policies:write`
* `iam:policies:read`
* `iam:bindings:write`
* `iam:bindings:read`
* `iam:boundaries:read`
* `iam:boundaries:write`

### Supported Configuration API types

Configuration via the [Configuration API](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.") requires an API access token.
Dynatrace Monaco CLI provides support for most Configuration APIs, as described in the table below.
This table provides:

* The supported configuration types.
* Their API endpoints.
* The access token permissions that are required to interact with any endpoint.

Note that most Configuration APIs are deprecated in favor of Settings 2.0, see [Settings 2.0](/docs/dynatrace-api/configuration-api "Find out what you need to use the configuration section of the Dynatrace API.").

Configuration type

Constraints

Endpoint and access permission

**alerting-profile**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") Problem alerting profiles schema: `builtin:alerting.profile`

RUM: **allowed-beacon-origins**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**anomaly-detection-applications**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-aws**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-database-services**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-disks**

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-hosts**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-metrics**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") Metric events schema:
`builtin:anomaly-detection.metric-events`

**anomaly-detection-services**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**anomaly-detection-vmware**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Anomaly detection API](/docs/dynatrace-api/configuration-api/anomaly-detection-api "Learn what the Dynatrace anomaly detection API offers.")

**app-detection-rule**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**app-detection-rule-host**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**application-web**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**application-mobile**

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**auto-tag**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") Automatically applied tags schema: `builtin:tags.auto-tagging`

**aws-credentials**

It can't be downloaded.

[AWS credentials API](/docs/dynatrace-api/configuration-api/aws-credentials-api "Learn what the Dynatrace AWS credentials config API offers.")

**azure-credentials**

It can't be downloaded.

[Azure credentials API](/docs/dynatrace-api/configuration-api/azure-credentials-api "Learn what the Dynatrace Azure credentials config API offers.")

**calculated-metrics-application-mobile**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**calculated-metrics-application-web**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**calculated-metrics-log**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with SchemaID `builtin:logmonitoring.schemaless-log-metric`.

**calculated-metrics-service**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**calculated-metrics-synthetic**

[Special Name requirements](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#calc-metrics "This is a list of Monaco special configuration types.")

[Calculated metrics API](/docs/dynatrace-api/configuration-api/calculated-metrics "Learn what the Dynatrace calculated metrics config API offers.")

**conditional-naming-host**

[Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

**conditional-naming-processgroup**

[Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

**conditional-naming-service**

[Conditional naming API](/docs/dynatrace-api/configuration-api/conditional-naming "Learn what the Dynatrace configuration API for conditional naming offers.")

**content-resources**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**credential-vault**

It can't be downloaded.

[Credential vault API](/docs/dynatrace-api/configuration-api/credential-vault "Learn what the Dynatrace configuration API for credentials offers.")

**custom-service-java**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-dotnet**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-go**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-nodejs**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**custom-service-php**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

Dashboard Classic

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

dashboard-share-settings classic

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.") and [Scoped configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#API-type-field "This is a list of Monaco special configuration types.")

[Dashboards Classic API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.")

**data-privacy**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Data privacy API](/docs/dynatrace-api/configuration-api/data-privacy-api "Learn what the Dynatrace data privacy config API offers.")

**extension**

It can't be downloaded.

[Extensions API](/docs/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

**extension-elasticsearch**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Extensions API](/docs/dynatrace-api/configuration-api/extensions-api "Learn what the Dynatrace Extension API offers.")

**failure-detection-parametersets**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**failure-detection-rules**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**frequent-issue-detection**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with `builtin:anomaly-detection.frequent-issues` schema

**geo-ip-address-mappings**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**geo-ip-detection-headers**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**hosts-auto-update**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[OneAgent environment-wide configuration API](/docs/dynatrace-api/configuration-api/oneagent-configuration/oneagent-environment-wide "Manage environment-wide configuration of OneAgent via the Dynatrace API.")

**key-user-actions-mobile**

[Scoped configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**key-user-actions-web**

[Scoped Configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

**kubernetes-credentials**

It can't be downloaded.

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with [Settings API - Connection settings schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes "View builtin:cloud.kubernetes settings schema table of your monitoring environment via the Dynatrace API.") `builtin:cloud.kubernetes` and [Settings API - Monitoring settings schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-cloud-kubernetes-monitoring "View builtin:cloud.kubernetes.monitoring settings schema table of your monitoring environment via the Dynatrace API.") `builtin:cloud.kubernetes.monitoring` schemas

**maintenance-window**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the Maintenance windows `builtin:alerting.maintenance-window` schema

**management-zone**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the Problem notifications `builtin:problem.notifications` schema

network-zone Dynatrace Monaco CLI version 2.10.0+

[Network zones API](/docs/dynatrace-api/environment-api/network-zones "Manage network zones via the Dynatrace API.")

**notification**

[Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with Problem notifications `builtin:problem.notifications` schema

**reports**

[Reports API](/docs/dynatrace-api/configuration-api/reports-api "Manage reports via the Dynatrace configuration API.")

**request-attributes**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**request-naming-service**

[Non-Unique Name Configuration](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#non-unique-name "This is a list of Monaco special configuration types.")

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**slo classic**

[Service-level Objectives API classic](/docs/dynatrace-api/environment-api/service-level-objectives-classic "Find out what the Dynatrace SLO API classic offers.")

**service-detection-full-web-request**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-detection-full-web-service**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-detection-opaque-web-request**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-detection-opaque-web-service**

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.")

**service-resource-naming**

[Single configuration endpoint](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas#single-configuration-endpoint "This is a list of Monaco special configuration types.")

[Services configuration API](/docs/dynatrace-api/configuration-api/service-api "This is a list of services endpoints of the Dynatrace config API.") `/api/config/v1/service/resourceNaming`

**synthetic-location**

[Synthetic API v1](/docs/dynatrace-api/environment-api/synthetic "Find out what the Dynatrace Synthetic v1 API offers.")

**synthetic-monitor**

[Synthetic API v2](/docs/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers.")

**user-action-and-session-properties-mobile**

[Scoped Configuration](/docs/deliver/configuration-as-code/monaco/configuration/yaml-configuration-saas-type-fields#settings-type-field "This is a list of type fields in the Monaco configuration YAML file.")

[Real User Monitoring configuration APIs](/docs/dynatrace-api/configuration-api/rum "Find out what RUM endpoints of the Dynatrace configuration API offer.")

## Related topics

* [Monaco configuration YAML file - list of special configuration types](/docs/deliver/configuration-as-code/monaco/configuration/special-configuration-types-saas "This is a list of Monaco special configuration types.")