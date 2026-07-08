---
title: Settings API - Salesforce Insights schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-biz-salesforce-insights-biz-salesforce-insights-settings
---

# Settings API - Salesforce Insights schema table

# Settings API - Salesforce Insights schema table

* Published Dec 05, 2023

### Salesforce Insights (`app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings)`

Settings for the Salesforce Insights AppEngine application

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.biz.salesforce.insights:biz-salesforce-insights-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | Configuration Name | Required |
| URL `url` | text | URL of salesforce instance | Required |
| Event Types `eventTypes` | Set<[EEventTypes](#EEventTypes)> | The element has these enums * `LoginEvent` * `SessionHijackingEventStore` * `ReportAnomalyEventStore` * `ReportEvent` * `ApiAnomalyEventStore` * `LightningUriEvent` * `ListViewEvent` * `OpportunityFieldHistory` * `UriEvent` | Required |
| Workflow ID `workflowId` | text | Changing this will break the app | Optional |
| Grant type `grant_type` | enum | The element has these enums * `client_credentials` * `password` | Required |
| Client Id `client_id` | secret | - | Required |
| Client secret `client_secret` | secret | - | Required |
| Username `username` | text | - | Required |
| Password `password` | secret | - | Required |