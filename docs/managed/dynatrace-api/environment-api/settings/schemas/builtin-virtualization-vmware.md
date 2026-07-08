---
title: Settings API - VMware schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-virtualization-vmware
---

# Settings API - VMware schema table

# Settings API - VMware schema table

* Published Dec 05, 2023

### VMware (`builtin:virtualization.vmware)`

Use this page to connect your VMware vCenter, standalone ESXi hosts to Dynatrace for monitoring. For VMware instances, connect all vCenter servers that manage virtual machines where Dynatrace OneAgent is installed. You don't need to add ESXi hosts if they are managed by a vCenter server that is connected to Dynatrace.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:virtualization.vmware` | * `group:cloud-and-virtualization` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:virtualization.vmware` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:virtualization.vmware` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:virtualization.vmware` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Name this connection `label` | text | - | Required |
| Specify the IP address or name of the vCenter or standalone ESXi host: `ipaddress` | text | - | Required |
| Provide user credentials for the vCenter or standalone ESXi host: `username` | text | - | Required |
| `password` | secret | - | Required |
| Specify filter condition to limit the number of monitored clusters: `filter` | text | This string should have one of the following formats:  * $prefix(parameter) - property value starting with 'parameter' * $eq(parameter) - property value exactly matching 'parameter' * $suffix(parameter) - property value ends with 'parameter' * $contains(parameter) - property value contains 'parameter' | Optional |