---
title: Settings API - AWS Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hyperscaler-authentication-aws-connection
---

# Settings API - AWS Connections schema table

# Settings API - AWS Connections schema table

* Published Oct 14, 2024

### AWS Connections (`builtin:hyperscaler-authentication.aws.connection)`

Available connections for [AWS for Workflows﻿](https://dt-url.net/s803q9r). A connection is used to authenticate against your AWS account. The retrieved, temporary AWS credentials are used to execute the AWS workflow actions.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hyperscaler-authentication.aws.connection` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.aws.connection` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hyperscaler-authentication.aws.connection` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.aws.connection` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Credential Type `type` | enum | The element has these enums * `webIdentity` | Required |
| `webIdentity` | [WebIdentity](#WebIdentity) | - | Required |

##### The `WebIdentity` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Role ARN `roleArn` | secret | The ARN of the AWS role that should be assumed | Required |
| Policy ARNs `policyArns` | list | An optional list of policies that can be used to restrict the AWS role | Required |