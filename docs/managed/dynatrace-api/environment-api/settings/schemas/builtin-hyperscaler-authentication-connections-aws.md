---
title: Settings API - Connections to AWS environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hyperscaler-authentication-connections-aws
scraped: 2026-05-12T11:40:20.576212
---

# Settings API - Connections to AWS environments schema table

# Settings API - Connections to AWS environments schema table

* Published Sep 25, 2025

### Connections to AWS environments (`builtin:hyperscaler-authentication.connections.aws)`

Connections to AWS for Dynatrace integrations

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hyperscaler-authentication.connections.aws` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.aws` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.aws` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.aws` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | The name of the connection | Required |
| Connection Type `type` | enum | AWS Authentication mechanism to be used by the connection The element has these enums * `awsRoleBasedAuthentication` * `awsWebIdentity` | Required |
| `awsRoleBasedAuthentication` | [AwsRoleBasedAuthenticationConfig](#AwsRoleBasedAuthenticationConfig) | - | Required |
| `awsWebIdentity` | [AwsWebIdentity](#AwsWebIdentity) | - | Required |

##### The `AwsRoleBasedAuthenticationConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| AWS IAM Role ARN `roleArn` | text | The ARN of the AWS role that should be assumed | Required |
| Consumers `consumers` | [ConsumersOfAwsRoleBasedAuthentication](#ConsumersOfAwsRoleBasedAuthentication)[] | Dynatrace integrations that can use this connection The element has these enums * `DA` * `SVC:com.dynatrace.da` * `APP:dynatrace.biz.carbon` * `SVC:com.dynatrace.bo` * `SVC:com.dynatrace.openpipeline` * `SVC:com.dynatrace.grail` * `NONE` | Required |

##### The `AwsWebIdentity` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| AWS IAM Role ARN `roleArn` | text | The ARN of the AWS role that should be assumed | Required |
| Consumers `consumers` | [ConsumersOfAwsWebIdentity](#ConsumersOfAwsWebIdentity)[] | Dynatrace integrations that can use this connection The element has these enums * `APP:dynatrace.aws.connector` * `APP:dynatrace.biz.carbon` | Required |