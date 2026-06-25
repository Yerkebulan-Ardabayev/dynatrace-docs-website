---
title: Settings API - Network Availability monitor config schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-config
scraped: 2026-05-12T11:40:04.728920
---

# Settings API - Network Availability monitor config schema table

# Settings API - Network Availability monitor config schema table

* Published Jul 31, 2024

### Network Availability monitor config (`builtin:synthetic.multiprotocol.config)`

Network Availability monitor

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.config` | * `group:synthetic.multiprotocol` | `MULTIPROTOCOL_MONITOR` - Network availability monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.config` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.config` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.config` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor enabled `enabled` | boolean | - | Required |
| Monitor description `description` | text | - | Required |
| Steps `steps` | [Step](#Step)[] | - | Required |
| Monitor properties `properties` | Set<[Property](#Property)> | Option not supported yet | Required |

##### The `Step` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Step name `name` | text | - | Required |
| Request type `requestType` | enum | All steps in the monitor must be the same request type. Learn more about request types in [Dynatrace documentationï»¿](https://dt-url.net/0803zt8 "Visit Dynatrace documentation") The element has these enums * `ICMP` * `TCP` * `DNS` | Required |
| Target list `targetList` | set | - | Required |
| Target filter `targetFilter` | text | See syntax and examples in [Dynatrace documentationï»¿](https://dt-url.net/3443zor "Visit Dynatrace documentation") | Optional |
| Configuration properties `properties` | Set<[Property](#Property)> | See possible configuration properties in [Dynatrace documentationï»¿](https://dt-url.net/gq83z4l "Visit Dynatrace documentation") | Required |
| Step-level constraints `constraints` | Set<[Constraint](#Constraint)> | See possible step-level constraints in [Dynatrace documentationï»¿](https://dt-url.net/x3a3zev "Visit Dynatrace documentation") | Required |
| Request-level configuration `requestConfigurations` | Set<[RequestConfiguration](#RequestConfiguration)> | See possible request-level configurations in [Dynatrace documentationï»¿](https://dt-url.net/b803zmi "Visit Dynatrace documentation") | Required |
| Pre-execution script `preScript` | text | Option not supported yet | Optional |
| Post-execution script `postScript` | text | Option not supported yet | Optional |

##### The `Property` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Property key `key` | text | - | Required |
| Property value `value` | text | - | Required |

##### The `Constraint` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Constraint type `type` | text | - | Required |
| Properties `properties` | Set<[Property](#Property)> | - | Required |

##### The `RequestConfiguration` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Request constraints `constraints` | Set<[Constraint](#Constraint)> | - | Required |
| Properties `properties` | Set<[Property](#Property)> | Option not supported yet | Required |
| Pattern matcher `patternMatcher` | text | Option not supported yet | Optional |