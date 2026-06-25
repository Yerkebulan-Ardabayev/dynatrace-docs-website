---
title: Settings API - Transaction start filters schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mainframe-txstartfilters
scraped: 2026-05-12T11:45:22.964327
---

# Settings API - Transaction start filters schema table

# Settings API - Transaction start filters schema table

* Published Dec 05, 2023

### Transaction start filters (`builtin:mainframe.txstartfilters)`

Dynatrace automatically traces CICS and IMS transactions when monitored services call them. Transactions that originate on the mainframe, on a terminal, or are called by unmonitored services must be explicitly listed to be monitored.

Add CICS and IMS transactions originating on a terminal (e.g., IBM 3270 green screen terminal) to the terminal transaction start filter. Add all other transactions to the transaction start filters.

Note that traces started using the transaction filters will never be linked to a previous trace, regardless of how the transaction was initiated.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mainframe.txstartfilters` | * `group:mainframe` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txstartfilters` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mainframe.txstartfilters` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mainframe.txstartfilters` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| CICS terminal transaction start filter `includedCicsTerminalTransactionIds` | set | You can use \* as wildcard. For example use A\* to trace all transaction IDs that start with A. | Required |
| CICS transaction start filter `includedCicsTransactionIds` | set | You can use \* as wildcard. For example use A\* to trace all transaction IDs that start with A. | Required |
| IMS terminal transaction start filter `includedImsTerminalTransactionIds` | set | You can use \* as wildcard. For example use A\* to trace all transaction IDs that start with A. | Required |
| IMS transaction start filter `includedImsTransactionIds` | set | You can use \* as wildcard. For example use A\* to trace all transaction IDs that start with A. | Required |