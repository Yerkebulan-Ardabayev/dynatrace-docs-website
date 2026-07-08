---
title: Settings API - Configure ownership schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ownership-config
---

# Settings API - Configure ownership schema table

# Settings API - Configure ownership schema table

* Published Dec 05, 2023

### Configure ownership (`builtin:ownership.config)`

Configure keys for ownership metadata and tags. [See documentation﻿](https://dt-url.net/ownership-custom-keys)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ownership.config` | * `group:ownership` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.config` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ownership.config` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ownership.config` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Keys for ownership metadata and tags `ownershipIdentifiers` | [OwnershipIdentifier](#OwnershipIdentifier)[] | Tags and metadata are key-value pairs. Define keys for tags and metadata that are considered for ownership. If a tag or any metadata starts with a key defined below, the value of the tag or metadata is considered a team identifier. | Required |

##### The `OwnershipIdentifier` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Key for ownership metadata and tags `key` | text | - | Required |