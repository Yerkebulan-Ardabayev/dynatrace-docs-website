---
title: Settings API - Attribute data masking schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-attribute-masking
---

# Settings API - Attribute data masking schema table

# Settings API - Attribute data masking schema table

* Published Dec 05, 2023

### Attribute data masking (`builtin:attribute-masking)`

Configure the visibility of stored attribute values to to meet your privacy requirements. Users with **View sensitive request data** permissions will always see the values. For further details on Dynatrace's privacy settings, visit the [Data privacy and security﻿](https://dt-url.net/bo210srx) documentation.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:attribute-masking` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-masking` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:attribute-masking` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:attribute-masking` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | If this is true, the masking of the specified key is applied. | Required |
| Attribute key `key` | text | Key of the attribute | Required |
| Masking `masking` | enum | Set a masking strategy to conceal its value from users  Choose **Mask entire value** to hide the whole value of this attribute from everyone who does not have 'View sensitive request data' permission. These attributes can't be used to define other configurations.  Choose **Mask only confidential data** to apply automatic masking strategies to your data. These strategies include, for example, credit card numbers, IBAN, IPs, email-addresses, etc. It may not be possible to recognize all sensitive data so please always make sure to verify that sensitive data is actually masked. If sensitive data is not recognized, please use **Mask entire value** instead. Users with 'View sensitive request data' permission will be able to see the entire value, others only the non-sensitive parts. These attributes can't be used to define other configurations. The element has these enums * `MASK_ONLY_CONFIDENTIAL_DATA` * `MASK_ENTIRE_VALUE` | Required |