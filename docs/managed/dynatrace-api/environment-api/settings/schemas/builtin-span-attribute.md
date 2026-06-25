---
title: Settings API - Span attributes schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-span-attribute
scraped: 2026-05-12T11:42:35.879025
---

# Settings API - Span attributes schema table

# Settings API - Span attributes schema table

* Published Dec 05, 2023

### Span attributes (`builtin:span-attribute)`

We replaced this setting with Allowed attributes (`<your-dynatrace-url>/builtin:attribute-allow-list`) and Attribute data masking (`<your-dynatrace-url>/builtin:attribute-masking`) and migrated your data. This setting will be removed soon.

Changes in this setting will still be migrated to the new ones, but please be aware that we are not able to migrate certain changes such as attribute deletions.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:span-attribute` | * `group:service-monitoring` * `group:service-monitoring.spans` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-attribute` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:span-attribute` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:span-attribute` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key `key` | text | Key of the span attribute to store | Required |
| Masking `masking` | enum | If this attribute contains confidential data, turn on masking to conceal its value from users  Introduce more granular control over the visibility of attribute values.  Choose **Do not mask** to allow every user to see the actual value and use it in defining other configurations.  Choose **Mask entire value** to hide the whole value of this attribute from everyone who does not have 'View sensitive request data' permission. These attributes can't be used to define other configurations. Choose **Mask only confidential data** to apply automatic masking strategies to your data. These strategies include, for example, credit card numbers, IBAN, IPs, email-addresses, etc. It may not be possible to recognize all sensitive data so please always make sure to verify that sensitive data is actually masked. If sensitive data is not recognized, please use **Mask entire value** instead. Users with 'View sensitive request data' permission will be able to see the entire value, others only the non-sensitive parts. These attributes can't be used to define other configurations. The element has these enums * `NOT_MASKED` * `MASK_ONLY_CONFIDENTIAL_DATA` * `MASK_ENTIRE_VALUE` | Required |