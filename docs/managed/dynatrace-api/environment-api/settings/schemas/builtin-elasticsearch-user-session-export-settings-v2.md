---
title: Settings API - User session exports schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-elasticsearch-user-session-export-settings-v2
scraped: 2026-05-12T11:48:24.723456
---

# Settings API - User session exports schema table

# Settings API - User session exports schema table

* Published Dec 05, 2023

### User session exports (`builtin:elasticsearch.user-session-export-settings-v2)`

A user session export enables you to stream real user monitoring data from Dynatrace to an external data source where it can be leveraged as input for big data analytics, or for extending data retention.

Streamed data includes all user sessions, user actions, events, and high-level timing and error data.

Use your existing analytics infrastructure to perform ad-hoc analysis on large numbers of user sessions, and combine this data with data mined from other sources.

Once enabled, user session export automatically sends JSON data for all monitored user sessions in your environment to the configured HTTPS endpoint.

You can also filter on a management zone per user session export.
You can define up to three user session exports to send specific data to different endpoints.

For complete details, visit [Configure user session exportsï»¿](https://dt-url.net/user-session-exports).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:elasticsearch.user-session-export-settings-v2` | * `group:integration.external` * `group:integration` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:elasticsearch.user-session-export-settings-v2` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:elasticsearch.user-session-export-settings-v2` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:elasticsearch.user-session-export-settings-v2` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Define your endpoint `endpointDefinition` | [EndpointDefinition](#EndpointDefinition) | Dynatrace will send JSON data periodically to this endpoint. You can also pause and disable an endpoint to stop the data stream from Dynatrace to your endpoint. | Required |
| Authentication `authentication` | [Authentication](#Authentication) | Dynatrace can automatically send bulk data to Elasticsearch. You can use an SSL certificate, basic authentication or OAuth 2.0 to secure access. For Dynatrace SaaS installations, the Elasticsearch instance must be publicly reachable by the Dynatrace Cluster. | Required |
| Send data directly to Elasticsearch `sendDirect` | [SendDirect](#SendDirect) | Activate this if you want to export user session data to your own Elasticsearch cluster. If you run Elasticsearch 7, make sure to enter \_doc as the type. For Elasticsearch 8 omit the type. If you really want to use a type, then you have to add include\_type\_name=true when creating your Elasticsearch index. See more information in the Dynatrace help. | Required |
| Export scope, alerting, and advanced configuration `exportBehavior` | [ExportBehavior](#ExportBehavior) | Define the scope of your export by using a specific management zone. You can also disable UI notifications for failing exports, or add special settings provided by Dynatrace support for troubleshooting. | Required |

##### The `EndpointDefinition` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Endpoint URL `endpointUrl` | text | - | Required |
| Enable user session export `enableUserSessionExport` | boolean | - | Required |
| Content type `contentType` | text | - | Required |
| Use POST method (instead of PUT) `usePost` | boolean | - | Required |

##### The `Authentication` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Activate `active` | boolean | - | Required |
| Authentication type `authType` | enum | The element has these enums * `basic` * `oauth2` | Required |
| Basic authentication `basicAuth` | [BasicAuth](#BasicAuth) | - | Required |
| OAuth 2.0 (Early Adopter) `oAuth2` | [OAuth2](#OAuth2) | - | Required |

##### The `SendDirect` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Activate `active` | boolean | - | Required |
| Name of the index where data is sent `indexName` | text | - | Required |
| Type of documents in the Elasticsearch index `docType` | text | - | Optional |

##### The `ExportBehavior` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Management zone `managementZone` | setting | Restrict exported sessions to management zone | Optional |
| Disable notification `disableNotification` | boolean | - | Required |
| Custom configuration properties `customConfiguration` | text | Here you can set additional properties for this export configuration. Changing these values might only be necessary in some rare cases. Please contact support before changing this field. | Optional |

##### The `BasicAuth` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| User name `username` | text | - | Required |
| Password `password` | secret | - | Required |

##### The `OAuth2` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Grant type `grantType` | enum | The element has these enums * `clientCredentials` | Required |
| Access token URL `accessTokenUrl` | text | - | Required |
| Client ID `clientId` | text | - | Required |
| Client secret `clientSecret` | secret | - | Required |
| Scope `scope` | text | The scope of access you are requesting | Optional |
| Send credentials `sendCredentials` | enum | The element has these enums * `header` | Required |