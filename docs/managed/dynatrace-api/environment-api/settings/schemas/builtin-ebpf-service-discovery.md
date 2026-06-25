---
title: Settings API - eBPF Service Discovery schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-ebpf-service-discovery
scraped: 2026-05-12T11:43:11.470017
---

# Settings API - eBPF Service Discovery schema table

# Settings API - eBPF Service Discovery schema table

* Published Feb 26, 2024

### eBPF Service Discovery (`builtin:ebpf.service.discovery)`

This OneAgent module enables the discovery of active services on the network. It is a very low-overhead, safe way of identifying services that need to be monitored.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:ebpf.service.discovery` | * `group:network-and-discovery` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ebpf.service.discovery` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:ebpf.service.discovery` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:ebpf.service.discovery` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable service discovery `ebpf` | boolean | When disabled, Dynatrace can only detect services in Full stack mode. | Required |