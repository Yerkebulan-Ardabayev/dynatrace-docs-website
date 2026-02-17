# Dynatrace Documentation: license/cost-allocation.md

Generated: 2026-02-17

Files combined: 1

---


## Source: cost-allocation.md


---
title: Allocate your DPS costs
source: https://www.dynatrace.com/docs/license/cost-allocation
scraped: 2026-02-17T21:16:29.343199
---

# Allocate your DPS costs

# Allocate your DPS costs

* Latest Dynatrace
* How-to guide
* 16-min read
* Updated on Feb 09, 2026

Cost Allocation is exclusively available for Dynatrace SaaS environments with a Dynatrace Platform Subscription (DPS) licensing agreement that was signed after April 2023.

Dynatrace Cost Allocation lets you allocate Dynatrace DPS usage to customer-defined cost centers, products, or both.
This gives you a transparent and detailed account of each cost centerâs Dynatrace expenditures, helping your organization optimize its budgets.

You can customize the use of these fields to fit your company's organizational framework:

* Data is collected from all OneAgents deployed on hosts or Kubernetes pods.
* Additionally, ingested telemetry data (traces and logs) can be collected in certain infrastructure setups (e.g., via Logs API or Kubernetes metadata enrichment).
* Costs can be allocated to customer-defined cost centers, products, or both.
* Data can be

  + Analyzed in Dynatrace via DQL, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, or ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
  + Exported for viewing and editing in separate tools such as Excel and Power BI.

The figure below shows how different components in a given Dynatrace environment can be assigned to different cost centers and products.

![Cost Allocation overview showing assignment of cost centers and products](https://dt-cdn.net/images/cost-allocation-overview-image-3989-d9453baaa2-3989-249b38f43f.png)

## Concepts

Cost center
:   A specific cost center within your organization.
    This is defined according to your organizational structure.
    Costs in Dynatrace can be allocated to specific cost centers.

Host tag
:   The parameter that assigns a host to a specific cost center or product.
    For more information, see [Define tags and metadata for hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.").

Host property
:   Sometimes used as a synonym for "host tag."
    For more information, see [Define tags and metadata for hosts](/docs/observe/infrastructure-observability/hosts/configuration/define-tags-and-metadata-for-hosts "Learn how to tag and set additional properties for a monitored host.").

Product
:   A single product, or group of products, offered by your organization.
    Costs in Dynatrace can be allocated to specific products.

Telemetry data
:   Generic term to refer to any single data point that is one of the following: log, trace, metric, or event.

## Required permissions

To view or edit Cost Allocation information, your Dynatrace account needs at least one of the permissions as indicated in the table below.
More information about these permissions is available at [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions#permissions-account "Role-based permissions").

### Account Management permissions

| What you want to do | View account | View and manage account and billing information |
| --- | --- | --- |
| View Cost Allocation Allow List |  |  |
| Edit Cost Allocation Allow List |  |  |
| View usage/costs extract in Account Management |  |  |

### Environment-level permissions

The default policy "Read System Events" needs to be assigned to the relevant user group.
The actual policy statement is provided in the code block below.

```
//Grail read data



ALLOW storage:buckets:read WHERE storage:table-name = "dt.system.events";



ALLOW storage:system:read;
```

If you will be using lookup tables to access Grail data, you will additionally need the permissions described in [Lookup data in Grail](/docs/platform/grail/lookup-data#permissions "Learn about lookup data in Grail.").

## Supported capabilities

The table below describes the [rate card capabilitiesï»¿](https://www.dynatrace.com/pricing/) for which Cost Allocation is available.

In the case that Cost Allocation isn't available for the given capability, an alternative best practice is recommended.

Category

Capability

DPS Cost Allocation

Alternative best practice

Application & Infrastructure Observability

Full-Stack Monitoring

â

Infrastructure Monitoring

â

Foundation & Discovery

â

Mainframe Monitoring

Classic metrics

Container Observability

Kubernetes Monitoring

Classic metrics

Application Security Protection

Runtime Vulnerability Analytics

â

Runtime Application Protection

â

Security Posture Management

Notebook available via Account Management

Digital Experience Monitoring

Real User Monitoring

Classic metrics

Real User Monitoring with Session Replay

Classic metrics

Real User Monitoring Property

Classic metrics

Browser Monitor or Clickpath

Classic metrics

Third-Party Synthetic API Ingestion

Classic metrics

HTTP Monitor

Classic metrics

Metrics powered by Grail

Metrics - Ingest

Notebook available via Account Management

Metrics - Retain

Notebook available via Account Management

Metrics - Query

Notebook available via Account Management

Log Analytics

Log - Ingest

â

Log - Retain

â

Logs - Retain with Included Queries

â

Log - Query

See [Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions](#user-based).

Traces powered by Grail

Traces - Ingest

â

Traces - Retain

Notebook available via Account Management

Traces - Query

See [Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions](#user-based).

Events powered by Grail

Events - Ingest

Notebook available via Account Management

Events - Retain

Notebook available via Account Management

Events - Query

See [Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions](#user-based).

AppEngine Functions

AppEngine Functions - Small

See [Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions](#user-based).

Automation

AutomationWorkflow

See [Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions](#user-based).

Platform extensions

Custom Metrics Classic

Please switch to [Metrics powered by Grail](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

Log Monitoring Classic

Please switch to [Log Analytics](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")

Custom Traces Classic

Please switch to [Traces powered by Grail](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")

Custom Events Classic

Please switch to [Events powered by Grail](/docs/license/capabilities/events "Learn how Dynatrace Events powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")

Serverless Functions Classic

Please switch to [AppEngine Functions](/docs/license/capabilities/appengine-functions "Learn how AppEngine Function consumption is calculated using the Dynatrace Platform Subscription model.")

We're continuously extending Cost Allocation support to cover additional Dynatrace capabilities.
For complete details regarding your licensing agreement, please contact your Dynatrace account manager.
For more details about specific capabilities, see [Monitoring consumption per capability](/docs/license#monitoring-consumption-per-dynatrace-capability "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

## Set up Cost Allocation

This section describes how to set up Cost Allocation in your Dynatrace environment.

For tips on how to allocate shared costs, where a single host is used by multiple cost centers or products, see [Handling shared costs](#cost-allocation-shared-costs).

### Identify allowed cost centers and products

To configure Cost Allocation you need to explicitly define the cost centers and products to which costs are allocated.
Up to 250 cost centers and 250 products can be defined.

The definitions are managed in two separate allow lists: the **Cost center allow list** and the **Product allow list**.
You can configure these either via **Account Management** or via the Dynatrace API, as described below.

Changes to the allow lists are not applied retroactively.
If you remove a cost center or product from its allow list, historical reports will still show the usage and costs associated with the value before it was removed.

#### Via Account Management

To find the two allow lists, go to **Account Management** > **Subscription** > **Cost management**.
The allow lists are visible in the **Cost center allow list** and **Product allow list** sections.

To add a new cost center or product, select  **Cost center** and follow the steps.

![Account management cost center allow list for Cost Allocation host tags](https://dt-cdn.net/images/image-1-1631-55a21c8e2a.png)

#### Via the API

Both the cost center and product allow lists can be configured via the Account Management API as described in [Dynatrace Platform Subscription API - manage cost allocation](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/manage-cost-allocation "Manage Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.").

### Configure Cost Allocation for host-based deployments

To set up Cost Allocation in a host-based deployment, configure OneAgent according to the steps in [Set up Cost Allocation for OneAgent deployments](/docs/ingest-from/dynatrace-oneagent/oneagent-cost-allocation "Learn how to allocate costs from OneAgent to cost centers and products.").

Cost Allocation is configured at the host level.
One host can be allocated to a maximum of one cost center and one product.

### Configure Cost Allocation for Kubernetes deployments

To set up Cost Allocation in a Kubernetes-based deployment, configure Kubernetes according to the steps in [Set up Cost Allocation for Kubernetes deployments](/docs/ingest-from/setup-on-k8s/kubernetes-cost-allocation "Learn how to allocate costs from Kubernetes deployments to cost centers and products.").

Cost Allocation is supported for different [Kubernetes deployment models](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

### Configure Cost Allocation for telemetry ingest

With Dynatrace, you can enrich telemetry data with Cost Allocation attributes (`dt.cost.costcenter`, `dt.cost.product`) as metadata.
Telemetry enrichment with Cost Allocation attributes is possible for all supported ingest methodsâwhether logs, traces, metrics, or events.

For ingested logs, Cost Allocation is also available for retained data ([Log - Retain](/docs/license/capabilities/log-analytics/dps-log-retain "Learn how your consumption of the Log Management & Analytics - Retain DPS capability is billed and charged.") and [Log - Retain with Included Queries](/docs/license/capabilities/log-analytics/dps-log-retain-included "Learn how your consumption of the Log Management & Analytics - Retain with Included Queries DPS capability is billed and charged.")).
Both retain models use the settings that you already set up for ingest, so you don't need to do any additional configuration.

You can use these attributes to allocate usage to your user-defined products and cost centers.

* They're stored in Grail and are available through ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, **Account Management**, and the [Dynatrace API](/docs/dynatrace-api "Find out what you need to use the Dynatrace API.").
* They're defined in the Dynatrace [Semantic Dictionary](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

For more information on how to enrich telemetry data according to your use case, see [Ingest data](/docs/ingest-from "Learn how to install and configure ActiveGate and OneAgent on various platforms.").

#### How to get started

No matter which method you use to ingest data, here's how to get going with Cost Allocation telemetry enhancement:

1. Get an inventory of your ingest channels.
   List all the ways your organization sends logs and traces into Dynatrace.
   This could be via OneAgent, the log ingest API, cloud forwarders, log shippers, OpenTelemetry, or any one of the supported ingest methods.
2. Review the documentation for your ingest method.
   Check the official Dynatrace documentation to find method-specific configuration and enrichment options.
3. Map metadata opportunities: Identify your specific cost centers and products and then explicitly define them in **Account Management**. For more information, see [Identify allowed cost centers and products](#cost-allocation-allowlist).

#### Integrate Cost Allocation metadata

Donât worry about perfection on day one.
Start tagging now, even if it's just for one ingest channel.
You can refine and expand to other ingest channels and telemetry types as your FinOps maturity grows.

Our available dashboard [Cost Allocation pre-made dashboard](#cost-allocation-dashboard) can help you identify other ingest channels that you could consider enhancing with Cost Allocation data.

1. For each ingest channel:

   * Review how metadata can be added.
     Depending on your ingest method, this could be via OneAgent configuration, API payload, cloud tag mapping, Kubernetes annotations, etc.
   * Implement tagging in your pipelines, scripts, or agent settings.
2. Test your setup:

   * Send sample data and verify that cost allocation tags are present in Grail.
   * Use the pre-made dashboard to confirm that these tags are visible.

     Usage tracking for logs and traces is written every 15 minutes.
     So, it might take up to 15 minutes until you will see any results.
3. Document your approach: Record which channels and tagging methods you use.
   This will help with future audits and troubleshooting.

### Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions

This section describes how to configure Cost Allocation for queries, workflows, and functions.
The relevant rate card categories are

* [Log Analytics - Query](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.")
* [Traces - Query](/docs/license/capabilities/traces/dps-traces-query "Learn how your consumption of the Traces - Query DPS capability is billed and charged.")
* [Events - Query](/docs/license/capabilities/events/dps-events-query "Learn how your consumption of the Events powered by Grail - Query DPS capability is billed and charged.")
* [Automation Workflow](/docs/license/capabilities/automation "Learn how Dynatrace Automation Workflow consumption is calculated using the Dynatrace Platform Subscription model.")
* [AppEngine Functions](/docs/license/capabilities/appengine-functions "Learn how AppEngine Function consumption is calculated using the Dynatrace Platform Subscription model.")

Cost Allocation for queries, workflows, and functions is currently only supported at the environment level.
Because of this, related data isn't included in [exported data](#cost-allocation-export).

Consumption related to each of these categories is triggered by a specific Dynatrace user.
Therefore, to allocate costs related to these categories, you'll map the user to the relevant Cost Allocation attributes (whether `dt.cost.costcenter` or `dt.cost.product`).
To do this, follow the steps below.

1. Prerequisites

Make sure that you have the following permissions:

* To set up this configuration: You need read, write, and delete permissions for Grail lookup tables.
  For more information, see [Lookup data in Grail](/docs/platform/grail/lookup-data#permissions "Learn about lookup data in Grail.").
* To use the dashboard: You need read permissions for Grail lookup tables.

2. Get the notebook and dashboard

Upload the following notebook and dashboard to your Dynatrace environment.

1. Copy the JSON contents from the code blocks below.
2. Save them as individual files in a text editor.
3. Import/upload the files to your environment, see [Import a notebook](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks#notebook-import "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") and [Upload a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboard-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

Cost Allocation with extended lookup tables notebook: JSON contents

```
{



"version": "7",



"defaultTimeframe": { "from": "now()-30d", "to": "now()" },



"defaultSegments": [],



"sections": [



{



"id": "1dc2b5b1-b459-404f-8397-dbde36b18576",



"type": "markdown",



"markdown": "Changelog:\n* v1.0: Initial setup including user details for query and function workaround.\n* v2.0: Add user ID to the user details and to enable workflow workarounds and put rate card into lookup tables\n* v2.1: Adding documentation and reorder cards for better understanding\n* v3.0: Sync with Dashboard needs"



},



{



"id": "7d8c034c-5957-4184-9158-2d6226b94ffe",



"type": "markdown",



"markdown": "## Documentation\n1. Ensure your user has the **CREATE Grail Lookup table permissions** [Lookup Documentation](https://docs.dynatrace.com/docs/discover-dynatrace/platform/grail/lookup-data#permissions)\n2. Ensure all Dashboard **users have the READ Grail Lookup table permission**\n3. Create a **list of users** with: user.email, user.id, dt.cost.costcenter, dt.cost.product (e.g. by using one of the helpful cards further down \"Retrieve a list of active Dynatrace users\")\n4. transform this list **into JSON** \n    AI can transform from CSV/Excel to JSON with the following AI prompt (please keep in mind our and your customer's AI policies)\n    > Please convert the attached CSV into a downloadable JSON based on this JSON example:\n    > {\"user.email\":\"abc@de.fg\",\n    > \"user.id\":\"00000000-0000-0000-0000-000000000000\",\n    > \"dt.cost.costcenter\":\"a\",\n    > \"dt.cost.product\":\"1\"}\n    \n5. **Copy the JSON** into the *\"Store user mapping within lookup table\"* card & execute (you might need to click \"show input\")\n6. **Adjust the prices** in the *\"Store rate card within lookup table\"* card & execute (you might need to click \"show input\")\n7. Check the Dashboard :-)\n\n\nYou will find some helpful cards further down:\n* Fetch already used cost centers or products\n* Retrieve a list of active Dynatrace users\n* See lookup rate card and user data content\n* See all existing lookup tables\n* Delete a lookup table\n"



},



{



"id": "417233f0-8ee3-4460-b8a5-9e3aea6a55ec",



"type": "function",



"title": "Store user mapping within lookup table",



"showTitle": false,



"drilldownPath": [],



"height": 100,



"showInput": false,



"state": {



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "export default async function () {\n  const form = new FormData();\n\n  form.append('request', JSON.stringify({\n    filePath: '/lookups/CA/userdata',   //please use this path to match the dashboard requirements\n    parsePattern: `JSON:json`,   \n    overwrite: true,\n    lookupField: 'user.email'  \n  }));\n\n// your custom JSON goes here - as shown in the example\nconst jsonContent = `[\n{\"user.email\":\"abc@de.fg\",\n    \"user.id\":\"00000000-0000-0000-0000-000000000000\",\n    \"dt.cost.costcenter\":\"a\",\n    \"dt.cost.product\":\"1\"}\n  ]`;\nconst jsonBlob = new Blob([jsonContent], { type: 'application/json' });\nform.append('content', jsonBlob, 'content.json');\n\n  const response = await fetch('/platform/storage/resource-store/v1/files/tabular/lookup:upload', {\n    method: 'POST',\n    body: form,\n    // No headers needed â fetch will set them correctly\n  });\n\n  if (!response.ok) {\n    const errorText = await response.text();\n    return 'Upload failed: ' + errorText;\n  } else {\n    const result = await response.text();\n    return 'Upload successful';\n  }\n}"



},



"visualizationSettings": { "thresholds": [], "chartSettings": {} },



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"state": "success",



"result": {



"code": 200,



"value": "Upload successful",



"notifications": [],



"logs": "",



"dateTime": "2025-09-25T13:41:04.413Z",



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "export default async function () {\n  const form = new FormData();\n\n  form.append('request', JSON.stringify({\n    filePath: '/lookups/CA/userdatax',   //please use this path to match the dashboard requirements\n    parsePattern: `JSON:json`,   \n    overwrite: true,\n    lookupField: 'user.email'  \n  }));\n\n// your custom JSON goes here vvv - please remove the surrounding [] if needed - as shown in the example\nconst jsonContent = `[\n{\"user.email\":\"abc@de.fg\",\n    \"user.id\":\"00000000-0000-0000-0000-000000000000\",\n    \"dt.cost.costcenter\":\"a\",\n    \"dt.cost.product\":\"1\"}\n  ]`;\nconst jsonBlob = new Blob([jsonContent], { type: 'application/json' });\nform.append('content', jsonBlob, 'content.json');\n\n  const response = await fetch('/platform/storage/resource-store/v1/files/tabular/lookup:upload', {\n    method: 'POST',\n    body: form,\n    // No headers needed â fetch will set them correctly\n  });\n\n  if (!response.ok) {\n    const errorText = await response.text();\n    return 'Upload failed: ' + errorText;\n  } else {\n    const result = await response.text();\n    return 'Upload successful';\n  }\n}"



}



},



"visualization": "table"



}



},



{



"id": "1b475125-118b-4a93-a8d1-541c0259ca2f",



"type": "function",



"title": "Store rate card within lookup table - ADJUST PRICES",



"showTitle": false,



"drilldownPath": [],



"showInput": false,



"height": 156,



"state": {



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "export default async function () {\n  const form = new FormData();\n\n  form.append('request', JSON.stringify({\n    filePath: '/lookups/CA/ratecard',   //please use this path to match the dashboard requirements\n    parsePattern: `JSON:json`,   \n    overwrite: true,\n    lookupField: 'key'     \n  }));\n\n// Hardcoded payload instead of fetching from URL\nconst jsonContent = `{\n        \"key\": \"AUTOMATIONS\",\n        \"name\": \"Automation Workflow\",\n        \"price\": \"0.13\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"BUSINESS_EVENTS_ANALYZE\",\n        \"name\": \"Events - Query\",\n        \"price\": \"0.0035\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"BUSINESS_EVENTS_INGEST\",\n        \"name\": \"Events - Ingest & Process\",\n        \"price\": \"0.2\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"BUSINESS_EVENTS_RETAIN\",\n        \"name\": \"Events - Retain\",\n        \"price\": \"0.0007\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"COMPUTE\",\n        \"name\": \"AppEngine Functions - Small\",\n        \"price\": \"0.001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"EVENTS\",\n        \"name\": \"Custom Events Classic\",\n        \"price\": \"0.000002\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"FOUNDATION_AND_DISCOVERY\",\n        \"name\": \"Foundation & Discovery\",\n        \"price\": \"0.01\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"FULLSTACK_MONITORING\",\n        \"name\": \"Full-Stack Monitoring\",\n        \"price\": \"0.01\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"INFRASTRUCTURE_MONITORING\",\n        \"name\": \"Infrastructure Monitoring\",\n        \"price\": \"0.04\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"KUBERNETES_OPERATIONS\",\n        \"name\": \"Kubernetes Platform Monitoring\",\n        \"price\": \"0.002\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOG_MANAGEMENT_ANALYZE\",\n        \"name\": \"Log Management & Analytics - Query\",\n        \"price\": \"0.0035\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOG_MANAGEMENT_INGEST\",\n        \"name\": \"Log Management & Analytics - Ingest & Process\",\n        \"price\": \"0.2\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOG_MANAGEMENT_RETAIN\",\n        \"name\": \"Log Management & Analytics - Retain\",\n        \"price\": \"0.0007\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOGS\",\n        \"name\": \"Log Monitoring Classic\",\n        \"price\": \"0.000001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"MAINFRAME_MONITORING\",\n        \"name\": \"Mainframe Monitoring\",\n        \"price\": \"0.1\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"METRICS\",\n        \"name\": \"Custom Metrics Classic\",\n        \"price\": \"0.000002\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"RUNTIME_APPLICATION_PROTECTION\",\n        \"name\": \"Runtime Application Protection\",\n        \"price\": \"0.00225\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"RUNTIME_VULNERABILITY_ANALYTICS\",\n        \"name\": \"Runtime Vulnerability Analytics\",\n        \"price\": \"0.00225\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SECURITY_POSTURE_MANAGEMENT\",\n        \"name\": \"Security Posture Management\",\n        \"price\": \"0\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SERVERLESS\",\n        \"name\": \"Serverless Functions Classic\",\n        \"price\": \"0.000004\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SYNTHETIC_MONITORING_BROWSER\",\n        \"name\": \"Browser Monitor or Clickpath\",\n        \"price\": \"0.009\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SYNTHETIC_MONITORING_HTTP\",\n        \"name\": \"HTTP Monitor\",\n        \"price\": \"0.001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SYNTHETIC_MONITORING_THIRD_PARTY\",\n        \"name\": \"Third-Party Synthetic API Ingestion\",\n        \"price\": \"0.001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACE_INGEST\",\n        \"name\": \"Traces - Ingest & Process\",\n        \"price\": \"0.2\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACE_QUERY\",\n        \"name\": \"Traces - Query\",\n        \"price\": \"0.0035\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACE_RETAIN\",\n        \"name\": \"Traces - Retain\",\n        \"price\": \"0.0007\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACES\",\n        \"name\": \"Custom Traces Classic\",\n        \"price\": \"0.0000014\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"USER_SESSION_PROPERTIES\",\n        \"name\": \"Real User Monitoring Property\",\n        \"price\": \"0.0001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"USER_SESSION_REPLAYS\",\n        \"name\": \"Real User Monitoring with Session Replay\",\n        \"price\": \"0.009\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"USER_SESSIONS\",\n        \"name\": \"Real User Monitoring\",\n        \"price\": \"0.00225\",\n        \"currencyCode\": \"USD\"\n    }`;\nconst jsonBlob = new Blob([jsonContent], { type: 'application/json' });\nform.append('content', jsonBlob, 'content.json');\n\n  const response = await fetch('/platform/storage/resource-store/v1/files/tabular/lookup:upload', {\n    method: 'POST',\n    body: form,\n    // No headers needed â fetch will set them correctly\n  });\n\n  if (!response.ok) {\n    const errorText = await response.text();\n    return 'Upload failed: ' + errorText;\n  } else {\n    const result = await response.text();\n    return 'Upload successful';\n  }\n}"



},



"visualizationSettings": { "thresholds": [], "chartSettings": {} },



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"state": "success",



"result": {



"code": 200,



"value": "Upload successful",



"notifications": [],



"logs": "",



"dateTime": "2025-09-25T13:35:51.117Z",



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "export default async function () {\n  const form = new FormData();\n\n  form.append('request', JSON.stringify({\n    filePath: '/lookups/CA/ratecard',   //please use this path to match the dashboard requirements\n    parsePattern: `JSON:json`,   \n    overwrite: true,\n    lookupField: 'key'     \n  }));\n\n// Hardcoded payload instead of fetching from URL\nconst jsonContent = `{\n        \"key\": \"AUTOMATIONS\",\n        \"name\": \"Automation Workflow\",\n        \"price\": \"0.13\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"BUSINESS_EVENTS_ANALYZE\",\n        \"name\": \"Events - Query\",\n        \"price\": \"0.0035\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"BUSINESS_EVENTS_INGEST\",\n        \"name\": \"Events - Ingest & Process\",\n        \"price\": \"0.2\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"BUSINESS_EVENTS_RETAIN\",\n        \"name\": \"Events - Retain\",\n        \"price\": \"0.0007\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"COMPUTE\",\n        \"name\": \"AppEngine Functions - Small\",\n        \"price\": \"0.001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"EVENTS\",\n        \"name\": \"Custom Events Classic\",\n        \"price\": \"0.000002\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"FOUNDATION_AND_DISCOVERY\",\n        \"name\": \"Foundation & Discovery\",\n        \"price\": \"0.01\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"FULLSTACK_MONITORING\",\n        \"name\": \"Full-Stack Monitoring\",\n        \"price\": \"0.01\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"INFRASTRUCTURE_MONITORING\",\n        \"name\": \"Infrastructure Monitoring\",\n        \"price\": \"0.04\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"KUBERNETES_OPERATIONS\",\n        \"name\": \"Kubernetes Platform Monitoring\",\n        \"price\": \"0.002\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOG_MANAGEMENT_ANALYZE\",\n        \"name\": \"Log Management & Analytics - Query\",\n        \"price\": \"0.0035\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOG_MANAGEMENT_INGEST\",\n        \"name\": \"Log Management & Analytics - Ingest & Process\",\n        \"price\": \"0.2\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOG_MANAGEMENT_RETAIN\",\n        \"name\": \"Log Management & Analytics - Retain\",\n        \"price\": \"0.0007\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"LOGS\",\n        \"name\": \"Log Monitoring Classic\",\n        \"price\": \"0.000001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"MAINFRAME_MONITORING\",\n        \"name\": \"Mainframe Monitoring\",\n        \"price\": \"0.1\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"METRICS\",\n        \"name\": \"Custom Metrics Classic\",\n        \"price\": \"0.000002\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"RUNTIME_APPLICATION_PROTECTION\",\n        \"name\": \"Runtime Application Protection\",\n        \"price\": \"0.00225\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"RUNTIME_VULNERABILITY_ANALYTICS\",\n        \"name\": \"Runtime Vulnerability Analytics\",\n        \"price\": \"0.00225\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SECURITY_POSTURE_MANAGEMENT\",\n        \"name\": \"Security Posture Management\",\n        \"price\": \"0\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SERVERLESS\",\n        \"name\": \"Serverless Functions Classic\",\n        \"price\": \"0.000004\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SYNTHETIC_MONITORING_BROWSER\",\n        \"name\": \"Browser Monitor or Clickpath\",\n        \"price\": \"0.009\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SYNTHETIC_MONITORING_HTTP\",\n        \"name\": \"HTTP Monitor\",\n        \"price\": \"0.001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"SYNTHETIC_MONITORING_THIRD_PARTY\",\n        \"name\": \"Third-Party Synthetic API Ingestion\",\n        \"price\": \"0.001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACE_INGEST\",\n        \"name\": \"Traces - Ingest & Process\",\n        \"price\": \"0.2\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACE_QUERY\",\n        \"name\": \"Traces - Query\",\n        \"price\": \"0.0035\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACE_RETAIN\",\n        \"name\": \"Traces - Retain\",\n        \"price\": \"0.0007\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"TRACES\",\n        \"name\": \"Custom Traces Classic\",\n        \"price\": \"0.0000014\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"USER_SESSION_PROPERTIES\",\n        \"name\": \"Real User Monitoring Property\",\n        \"price\": \"0.0001\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"USER_SESSION_REPLAYS\",\n        \"name\": \"Real User Monitoring with Session Replay\",\n        \"price\": \"0.009\",\n        \"currencyCode\": \"USD\"\n    },\n    {\n        \"key\": \"USER_SESSIONS\",\n        \"name\": \"Real User Monitoring\",\n        \"price\": \"0.00225\",\n        \"currencyCode\": \"USD\"\n    }`;\nconst jsonBlob = new Blob([jsonContent], { type: 'application/json' });\nform.append('content', jsonBlob, 'content.json');\n\n  const response = await fetch('/platform/storage/resource-store/v1/files/tabular/lookup:upload', {\n    method: 'POST',\n    body: form,\n    // No headers needed â fetch will set them correctly\n  });\n\n  if (!response.ok) {\n    const errorText = await response.text();\n    return 'Upload failed: ' + errorText;\n  } else {\n    const result = await response.text();\n    return 'Upload successful';\n  }\n}"



}



},



"visualization": "table"



}



},



{



"id": "fddbfef3-a99c-47ff-bf5c-5649d1256570",



"type": "markdown",



"markdown": "## some helpful cards"



},



{



"id": "98bba782-3b1d-48b5-9985-f345a2bb2e03",



"type": "dql",



"title": "Fetch already used cost centers",



"filterSegments": [],



"drilldownPath": [],



"previousFilterSegments": [],



"height": 199,



"state": {



"input": {



"timeframe": { "from": "now()-30d", "to": "now()" },



"value": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| summarize count(), by: {dt.cost.costcenter}\n| fieldsKeep dt.cost.costcenter"



},



"visualizationSettings": { "thresholds": [], "chartSettings": {} },



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"visualization": "table",



"result": {



"code": 200,



"value": {



"records": [



{ "dt.cost.costcenter": "business-intelligence/BI" },



{ "dt.cost.costcenter": "cybersecurity" },



{ "dt.cost.costcenter": "it-support-services/IT" },



{ "dt.cost.costcenter": "not-allowlisted" },



{ "dt.cost.costcenter": "quality-assurance/QA" },



{ "dt.cost.costcenter": "research-and-development/RnD" },



{ "dt.cost.costcenter": null }



],



"types": [



{ "indexRange": [0, 6], "mappings": { "dt.cost.costcenter": { "type": "string" } } }



],



"metadata": {



"grail": {



"canonicalQuery": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| summarize by:{dt.cost.costcenter}, count()\n| fieldsKeep dt.cost.costcenter",



"timezone": "Europe/Berlin",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n// | lookup [\n//    load \"/lookups/CA/userdata\"\n// ], sourceField:user.email, lookupField:user.email\n// | fieldsAdd dt.cost.costcenter = coalesce(dt.cost.costcenter, lookup.dt.cost.costcenter, \"unassigned\")\n| summarize count(), by: {dt.cost.costcenter}\n| fieldsKeep dt.cost.costcenter",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"scannedDataPoints": 0,



"analysisTimeframe": {



"start": "2025-07-20T15:44:57.099000000Z",



"end": "2025-08-19T15:44:57.099000000Z"



},



"locale": "en-US",



"executionTimeMilliseconds": 290,



"notifications": [],



"queryId": "6133276c-8e9c-419d-b1a2-c681a1b03bd8",



"sampled": false



}



}



},



"notifications": [],



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"dateTime": "2025-08-19T15:44:58.580Z",



"input": {



"timeframe": { "from": "now()-30d", "to": "now()" },



"value": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n// | lookup [\n//    load \"/lookups/CA/userdata\"\n// ], sourceField:user.email, lookupField:user.email\n// | fieldsAdd dt.cost.costcenter = coalesce(dt.cost.costcenter, lookup.dt.cost.costcenter, \"unassigned\")\n| summarize count(), by: {dt.cost.costcenter}\n| fieldsKeep dt.cost.costcenter"



}



},



"state": "success",



"davis": { "includeLogs": true, "davisVisualization": { "isAvailable": true } }



}



},



{



"id": "ce726004-77c1-45c1-931b-5b3f71ba2bd8",



"type": "dql",



"title": "Fetch already used products",



"filterSegments": [],



"drilldownPath": [],



"previousFilterSegments": [],



"height": 248,



"state": {



"input": {



"timeframe": { "from": "now()-30d", "to": "now()" },



"value": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| summarize count(), by: {dt.cost.product}\n| fieldsKeep dt.cost.product"



},



"visualizationSettings": {



"table": { "columnOrder": ["[\"dt.cost.product\"]"] },



"thresholds": [],



"chartSettings": {}



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"visualization": "table",



"result": {



"code": 200,



"value": {



"records": [



{ "dt.cost.product": "appsec" },



{ "dt.cost.product": "easytravel-AWS" },



{ "dt.cost.product": "easytravel-GCP" },



{ "dt.cost.product": "easytravel-VMware" },



{ "dt.cost.product": "fin-ops-application" },



{ "dt.cost.product": "not-allowlisted" },



{ "dt.cost.product": "stock-market-application" },



{ "dt.cost.product": "warehouse-wizard" },



{ "dt.cost.product": null }



],



"types": [



{ "indexRange": [0, 8], "mappings": { "dt.cost.product": { "type": "string" } } }



],



"metadata": {



"grail": {



"canonicalQuery": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| summarize by:{dt.cost.product}, count()\n| fieldsKeep dt.cost.product",



"timezone": "Europe/Berlin",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n// | lookup [\n//    load \"/lookups/CA/userdata\"\n// ], sourceField:user.email, lookupField:user.email\n// | fieldsAdd dt.cost.costcenter = coalesce(dt.cost.costcenter, lookup.dt.cost.costcenter, \"unassigned\")\n| summarize count(), by: {dt.cost.product}\n| fieldsKeep dt.cost.product",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"scannedDataPoints": 0,



"analysisTimeframe": {



"start": "2025-07-20T15:45:52.799000000Z",



"end": "2025-08-19T15:45:52.800000000Z"



},



"locale": "en-US",



"executionTimeMilliseconds": 296,



"notifications": [],



"queryId": "4f80c384-7d7d-4352-99e3-3c003d7d4101",



"sampled": false



}



}



},



"notifications": [],



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"dateTime": "2025-08-19T15:45:54.133Z",



"input": {



"timeframe": { "from": "now()-30d", "to": "now()" },



"value": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n// | lookup [\n//    load \"/lookups/CA/userdata\"\n// ], sourceField:user.email, lookupField:user.email\n// | fieldsAdd dt.cost.costcenter = coalesce(dt.cost.costcenter, lookup.dt.cost.costcenter, \"unassigned\")\n| summarize count(), by: {dt.cost.product}\n| fieldsKeep dt.cost.product"



}



},



"state": "success",



"davis": { "includeLogs": true, "davisVisualization": { "isAvailable": true } }



}



},



{



"id": "12525576-a233-4c08-8953-c624e01befe0",



"type": "dql",



"title": "Quickstart: Retrieve a list of active Dynatrace users",



"filterSegments": [],



"drilldownPath": [],



"previousFilterSegments": [],



"showInput": true,



"height": 155,



"state": {



"input": {



"timeframe": { "from": "now()-30d", "to": "now()" },



"value": "  fetch dt.system.events\n  |filter event.kind == \"BILLING_USAGE_EVENT\"\n  |fields user.email, user.id\n  |dedup user.email\n  |filter endsWith(user.email,\"dynatrace.com\")\n  | append [ \n    fetch dt.system.events\n    |filter event.kind == \"QUERY_EXECUTION_EVENT\"\n    |fields user.email, user.id\n    |dedup user.email\n    |filter endsWith(user.email,\"dynatrace.com\")\n  ]"



},



"visualizationSettings": {



"table": { "columnOrder": ["[\"user.email\"]", "[\"user.id\"]"] },



"thresholds": [],



"chartSettings": {}



},



"querySettings": {



"maxResultRecords": 5000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"visualization": "table",



"result": {



"code": 200,



"value": {



"records": [],



"types": [



{



"indexRange": [0, 1562],



"mappings": { "user.email": { "type": "string" }, "user.id": { "type": "string" } }



}



],



"metadata": {



"grail": {



"canonicalQuery": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| fields user.email, user.id\n| dedup user.email\n| filter endsWith(user.email, \"dynatrace.com\")\n| append \n\t[\n\t\tfetch dt.system.events\n\t\t| filter event.kind == \"QUERY_EXECUTION_EVENT\"\n\t\t| fields user.email, user.id\n\t\t| dedup user.email\n\t\t| filter endsWith(user.email, \"dynatrace.com\")\n\t]",



"timezone": "Europe/Berlin",



"query": "  fetch dt.system.events\n  |filter event.kind == \"BILLING_USAGE_EVENT\"\n  |fields user.email, user.id\n  |dedup user.email\n  |filter endsWith(user.email,\"dynatrace.com\")\n  | append [ \n    fetch dt.system.events\n    |filter event.kind == \"QUERY_EXECUTION_EVENT\"\n    |fields user.email, user.id\n    |dedup user.email\n    |filter endsWith(user.email,\"dynatrace.com\")\n  ]",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"scannedDataPoints": 0,



"analysisTimeframe": {



"start": "2025-08-19T09:33:28.471000000Z",



"end": "2025-09-18T09:33:28.471000000Z"



},



"locale": "en-US",



"executionTimeMilliseconds": 309,



"notifications": [],



"queryId": "8a1873d6-8983-474a-93f4-e6490bde84ab",



"sampled": false



}



}



},



"notifications": [],



"querySettings": {



"maxResultRecords": 5000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"dateTime": "2025-09-18T09:33:30.382Z",



"input": {



"timeframe": { "from": "now()-30d", "to": "now()" },



"value": "  fetch dt.system.events\n  |filter event.kind == \"BILLING_USAGE_EVENT\"\n  |fields user.email, user.id\n  |dedup user.email\n  |filter endsWith(user.email,\"dynatrace.com\")\n  | append [ \n    fetch dt.system.events\n    |filter event.kind == \"QUERY_EXECUTION_EVENT\"\n    |fields user.email, user.id\n    |dedup user.email\n    |filter endsWith(user.email,\"dynatrace.com\")\n  ]"



}



},



"state": "success",



"davis": { "includeLogs": true, "davisVisualization": { "isAvailable": true } }



}



},



{



"id": "563d3d6f-48d5-4a35-b3ca-99825a891347",



"type": "dql",



"filterSegments": [],



"drilldownPath": [],



"previousFilterSegments": [],



"showInput": true,



"height": 159,



"title": "See lookup userdata content",



"state": {



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "load \"/lookups/CA/userdata\""



},



"visualizationSettings": {



"table": {



"columnOrder": [



"[\"user.id\"]",



"[\"dt.cost.costcenter\"]",



"[\"dt.cost.product\"]",



"[\"user.email\"]"



]



},



"thresholds": [],



"chartSettings": {}



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"visualization": "table",



"result": {



"code": 200,



"value": {



"records": [



{



"user.id": "00000000-0000-0000-0000-000000000000",



"dt.cost.costcenter": "a",



"dt.cost.product": "1",



"user.email": "abc@de.fg"



}



],



"types": [



{



"indexRange": [0, 0],



"mappings": {



"user.id": { "type": "string" },



"dt.cost.costcenter": { "type": "string" },



"dt.cost.product": { "type": "string" },



"user.email": { "type": "string" }



}



}



],



"metadata": {



"grail": {



"canonicalQuery": "load \"/lookups/CA/userdatax\"",



"timezone": "Europe/Berlin",



"query": "load \"/lookups/CA/userdatax\"",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"scannedDataPoints": 0,



"locale": "de-DE",



"executionTimeMilliseconds": 193,



"notifications": [],



"queryId": "621d4d8d-8124-4701-bbce-65af846e091e",



"sampled": false



}



}



},



"notifications": [],



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"dateTime": "2025-09-25T13:41:27.640Z",



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "load \"/lookups/CA/userdatax\""



}



},



"state": "success",



"davis": { "includeLogs": true, "davisVisualization": { "isAvailable": true } }



}



},



{



"id": "8de1173f-a897-499f-8aba-9aa4821db646",



"type": "dql",



"filterSegments": [],



"drilldownPath": [],



"previousFilterSegments": [],



"showInput": true,



"height": 159,



"title": "See lookup ratecard content",



"state": {



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "load \"/lookups/CA/ratecard\""



},



"visualizationSettings": {



"table": {



"columnOrder": ["[\"name\"]", "[\"price\"]", "[\"currencyCode\"]", "[\"key\"]"]



},



"thresholds": [],



"chartSettings": {}



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"visualization": "table",



"result": {



"code": 200,



"value": {



"records": [



{



"name": "Automation Workflow",



"price": "0.13",



"currencyCode": "USD",



"key": "AUTOMATIONS"



},



{



"name": "Events - Query",



"price": "0.0035",



"currencyCode": "USD",



"key": "BUSINESS_EVENTS_ANALYZE"



},



{



"name": "Events - Ingest & Process",



"price": "0.2",



"currencyCode": "USD",



"key": "BUSINESS_EVENTS_INGEST"



},



{



"name": "Events - Retain",



"price": "0.0007",



"currencyCode": "USD",



"key": "BUSINESS_EVENTS_RETAIN"



},



{



"name": "AppEngine Functions - Small",



"price": "0.001",



"currencyCode": "USD",



"key": "COMPUTE"



},



{



"name": "Custom Events Classic",



"price": "0.000002",



"currencyCode": "USD",



"key": "EVENTS"



},



{



"name": "Foundation & Discovery",



"price": "0.01",



"currencyCode": "USD",



"key": "FOUNDATION_AND_DISCOVERY"



},



{



"name": "Full-Stack Monitoring",



"price": "0.01",



"currencyCode": "USD",



"key": "FULLSTACK_MONITORING"



},



{



"name": "Infrastructure Monitoring",



"price": "0.04",



"currencyCode": "USD",



"key": "INFRASTRUCTURE_MONITORING"



},



{



"name": "Kubernetes Platform Monitoring",



"price": "0.002",



"currencyCode": "USD",



"key": "KUBERNETES_OPERATIONS"



},



{



"name": "Log Monitoring Classic",



"price": "0.000001",



"currencyCode": "USD",



"key": "LOGS"



},



{



"name": "Log Management & Analytics - Query",



"price": "0.0035",



"currencyCode": "USD",



"key": "LOG_MANAGEMENT_ANALYZE"



},



{



"name": "Log Management & Analytics - Ingest & Process",



"price": "0.2",



"currencyCode": "USD",



"key": "LOG_MANAGEMENT_INGEST"



},



{



"name": "Log Management & Analytics - Retain",



"price": "0.0007",



"currencyCode": "USD",



"key": "LOG_MANAGEMENT_RETAIN"



},



{



"name": "Mainframe Monitoring",



"price": "0.1",



"currencyCode": "USD",



"key": "MAINFRAME_MONITORING"



},



{



"name": "Custom Metrics Classic",



"price": "0.000002",



"currencyCode": "USD",



"key": "METRICS"



},



{



"name": "Runtime Application Protection",



"price": "0.00225",



"currencyCode": "USD",



"key": "RUNTIME_APPLICATION_PROTECTION"



},



{



"name": "Runtime Vulnerability Analytics",



"price": "0.00225",



"currencyCode": "USD",



"key": "RUNTIME_VULNERABILITY_ANALYTICS"



},



{



"name": "Security Posture Management",



"price": "0",



"currencyCode": "USD",



"key": "SECURITY_POSTURE_MANAGEMENT"



},



{



"name": "Serverless Functions Classic",



"price": "0.000004",



"currencyCode": "USD",



"key": "SERVERLESS"



},



{



"name": "Browser Monitor or Clickpath",



"price": "0.009",



"currencyCode": "USD",



"key": "SYNTHETIC_MONITORING_BROWSER"



},



{



"name": "HTTP Monitor",



"price": "0.001",



"currencyCode": "USD",



"key": "SYNTHETIC_MONITORING_HTTP"



},



{



"name": "Third-Party Synthetic API Ingestion",



"price": "0.001",



"currencyCode": "USD",



"key": "SYNTHETIC_MONITORING_THIRD_PARTY"



},



{



"name": "Custom Traces Classic",



"price": "0.0000014",



"currencyCode": "USD",



"key": "TRACES"



},



{



"name": "Traces - Ingest & Process",



"price": "0",



"currencyCode": "USD",



"key": "TRACE_INGEST"



},



{



"name": "Traces - Query",



"price": "0",



"currencyCode": "USD",



"key": "TRACE_QUERY"



},



{



"name": "Traces - Retain",



"price": "0",



"currencyCode": "USD",



"key": "TRACE_RETAIN"



},



{



"name": "Real User Monitoring",



"price": "0.00225",



"currencyCode": "USD",



"key": "USER_SESSIONS"



},



{



"name": "Real User Monitoring Property",



"price": "0.0001",



"currencyCode": "USD",



"key": "USER_SESSION_PROPERTIES"



},



{



"name": "Real User Monitoring with Session Replay",



"price": "0.009",



"currencyCode": "USD",



"key": "USER_SESSION_REPLAYS"



}



],



"types": [



{



"indexRange": [0, 29],



"mappings": {



"name": { "type": "string" },



"price": { "type": "string" },



"currencyCode": { "type": "string" },



"key": { "type": "string" }



}



}



],



"metadata": {



"grail": {



"canonicalQuery": "load \"/lookups/CA/ratecard\"",



"timezone": "Europe/Berlin",



"query": "load \"/lookups/CA/ratecard\"",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"scannedDataPoints": 0,



"locale": "en-US",



"executionTimeMilliseconds": 227,



"notifications": [],



"queryId": "8249960d-76d2-42be-ad48-95fdaaf2af15",



"sampled": false



}



}



},



"notifications": [],



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"dateTime": "2025-08-26T15:02:53.423Z",



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "load \"/lookups/CA/ratecard\""



}



},



"state": "success",



"davis": { "includeLogs": true, "davisVisualization": { "isAvailable": true } }



}



},



{



"id": "39cf3e30-3400-41b4-9071-b6594821ae3c",



"type": "dql",



"title": "check existing Cost Allocation lookup tables",



"filterSegments": [],



"drilldownPath": [],



"previousFilterSegments": [],



"showInput": true,



"height": 115,



"state": {



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "fetch dt.system.files\n| filter startsWith(name,\"/lookups/CA\")"



},



"visualizationSettings": { "thresholds": [], "chartSettings": {} },



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"visualization": "table",



"result": {



"code": 200,



"value": {



"records": [],



"types": [],



"metadata": {



"grail": {



"canonicalQuery": "fetch dt.system.files\n| filter startsWith(name, \"/lookups/CAx\")",



"timezone": "Europe/Berlin",



"query": "fetch dt.system.files\n| filter startsWith(name,\"/lookups/CAx\")",



"scannedRecords": 0,



"dqlVersion": "V1_0",



"scannedBytes": 0,



"scannedDataPoints": 0,



"analysisTimeframe": {



"start": "2025-08-08T08:25:55.722000000Z",



"end": "2025-08-08T10:25:55.722000000Z"



},



"locale": "en-US",



"executionTimeMilliseconds": 30,



"notifications": [],



"queryId": "b61580ac-b62c-43c0-a167-19757fe498ac",



"sampled": false



}



}



},



"notifications": [],



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"dateTime": "2025-08-08T10:25:56.067Z",



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "fetch dt.system.files\n| filter startsWith(name,\"/lookups/CAx\")"



}



},



"state": "success",



"davis": { "includeLogs": true, "davisVisualization": { "isAvailable": true } }



}



},



{



"id": "2636c224-47d6-44c1-9584-7bd71ed0f24d",



"type": "function",



"title": "DELETE a lookup table",



"showTitle": false,



"drilldownPath": [],



"showInput": true,



"height": 246,



"state": {



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "export default async function () {\n  const form = new FormData();\n\n  const response = await fetch('/platform/storage/resource-store/v1/files:delete', {\n    method: 'POST',\n    headers: {\n        \"Content-Type\": \"application/json\",\n        Accept: \"application/json\"\n      },\n    body: JSON.stringify({\n        filePath: '/lookups/CA/delete_me'\n      }),\n  });\n\n  if (!response.ok) {\n    const errorText = await response.text();\n    return 'Delete failed: ' + errorText;\n  } else {\n    const result = await response.text();\n    return 'Delete successful';\n  }\n}"



},



"visualizationSettings": { "thresholds": [], "chartSettings": {} },



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"state": "success",



"result": {



"code": 200,



"value": "Delete failed: {\"error\":{\"message\":\"Resource with name: '/lookups/CAtest/ratecard' not found for tenantId 'gmg80500'.\",\"code\":404}}",



"notifications": [],



"logs": "",



"dateTime": "2025-08-07T14:53:14.081Z",



"input": {



"timeframe": { "from": "now()-2h", "to": "now()" },



"value": "export default async function () {\n  const form = new FormData();\n\n  const response = await fetch('/platform/storage/resource-store/v1/files:delete', {\n    method: 'POST',\n    headers: {\n        \"Content-Type\": \"application/json\",\n        Accept: \"application/json\"\n      },\n    body: JSON.stringify({\n        filePath: '/lookups/CAtest/ratecard'\n      }),\n  });\n\n  if (!response.ok) {\n    const errorText = await response.text();\n    return 'Delete failed: ' + errorText;\n  } else {\n    const result = await response.text();\n    return 'Delete successful';\n  }\n}"



}



},



"visualization": "table"



}



}



]



}
```

Cost Allocation with extended lookup tables dashboard: JSON contents

```
{



"version": 20,



"variables": [



{



"version": 2,



"key": "CostAllocation",



"type": "csv",



"visible": true,



"editable": true,



"input": "costcenter,product",



"multiple": false,



"defaultValue": "costcenter"



},



{



"version": 2,



"key": "Filter",



"type": "query",



"visible": true,



"editable": true,



"input": "fetch dt.system.events\n| filter $CostAllocation == \"costcenter\"\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| fieldsAdd value = coalesce(dt.cost.costcenter, $unassigned)\n| summarize count(), by: {value}\n| fieldsKeep value\n| append [\n  fetch dt.system.events\n  | filter $CostAllocation == \"product\"\n  | filter event.kind == \"BILLING_USAGE_EVENT\"\n  | fieldsAdd value = coalesce(dt.cost.product, $unassigned)\n  | summarize count(), by: {value}\n  | fieldsKeep value\n]",



"multiple": true,



"defaultValue": ["3420b2ac-f1cf-4b24-b62d-61ba1ba8ed05*"]



},



{



"key": "Capability",



"visible": true,



"type": "query",



"version": 2,



"editable": true,



"input": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| expand dt.cost.costcenter\n| fieldsAdd dt.cost.costcenter = coalesce(dt.cost.costcenter[key], dt.cost.costcenter)\n| expand dt.cost.product\n| fieldsAdd dt.cost.product = coalesce(dt.cost.product[key], dt.cost.product)\n| filter $SupportedCapabilitiesOnly == \"no\" OR isNotNull(dt.cost.costcenter) OR isNotNull(dt.cost.product)\n| fields event.type\n| dedup event.type",



"multiple": true



},



{



"version": 2,



"key": "unassigned",



"type": "text",



"visible": false,



"editable": true,



"defaultValue": "unassigned"



},



{



"version": 2,



"key": "SupportedCapabilitiesOnly",



"type": "csv",



"visible": true,



"editable": true,



"input": "yes,no",



"multiple": false,



"defaultValue": "yes"



},



{



"version": 2,



"key": "ratecard_data",



"type": "code",



"visible": false,



"editable": true,



"input": "/*\n* This will run JavaScript in the DYNATRACE\n* serverless environment.\n* To generate variable options return string array.\n*/\nexport default async function () {\n  return `[\n  {\"key\":\"AUTOMATIONS\",\"name\":\"Automation Workflow\",\"price\":\"0.13\",\"currencyCode\":\"USD\"},\n  {\"key\":\"BUSINESS_EVENTS_ANALYZE\",\"name\":\"Events - Query\",\"price\":\"0.0035\",\"currencyCode\":\"USD\"},\n  {\"key\":\"BUSINESS_EVENTS_INGEST\",\"name\":\"Events - Ingest & Process\",\"price\":\"0.2\",\"currencyCode\":\"USD\"},\n  {\"key\":\"BUSINESS_EVENTS_RETAIN\",\"name\":\"Events - Retain\",\"price\":\"0.0007\",\"currencyCode\":\"USD\"},\n  {\"key\":\"CODE_MONITORING\",\"name\":\"Code Monitoring\",\"price\":\"0.005\",\"currencyCode\":\"USD\"},\n  {\"key\":\"COMPUTE\",\"name\":\"AppEngine Functions - Small\",\"price\":\"0.001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"EVENTS\",\"name\":\"Custom Events Classic\",\"price\":\"0.000002\",\"currencyCode\":\"USD\"},\n  {\"key\":\"FOUNDATION_AND_DISCOVERY\",\"name\":\"Foundation & Discovery\",\"price\":\"0.01\",\"currencyCode\":\"USD\"},\n  {\"key\":\"FULLSTACK_MONITORING\",\"name\":\"Full-Stack Monitoring\",\"price\":\"0.01\",\"currencyCode\":\"USD\"},\n  {\"key\":\"INFRASTRUCTURE_MONITORING\",\"name\":\"Infrastructure Monitoring\",\"price\":\"0.04\",\"currencyCode\":\"USD\"},\n  {\"key\":\"KUBERNETES_OPERATIONS\",\"name\":\"Kubernetes Platform Monitoring\",\"price\":\"0.002\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOG_MANAGEMENT_ANALYZE\",\"name\":\"Log Management & Analytics - Query\",\"price\":\"0.0035\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOG_MANAGEMENT_INGEST\",\"name\":\"Log Management & Analytics - Ingest & Process\",\"price\":\"0.2\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOG_MANAGEMENT_RETAIN\",\"name\":\"Log Management & Analytics - Retain\",\"price\":\"0.0007\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOGS\",\"name\":\"Log Monitoring Classic\",\"price\":\"0.000001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"MAINFRAME_MONITORING\",\"name\":\"Mainframe Monitoring\",\"price\":\"0.1\",\"currencyCode\":\"USD\"},\n  {\"key\":\"METRICS\",\"name\":\"Custom Metrics Classic\",\"price\":\"0.000002\",\"currencyCode\":\"USD\"},\n  {\"key\":\"RUNTIME_APPLICATION_PROTECTION\",\"name\":\"Runtime Application Protection\",\"price\":\"0.00225\",\"currencyCode\":\"USD\"},\n  {\"key\":\"RUNTIME_VULNERABILITY_ANALYTICS\",\"name\":\"Runtime Vulnerability Analytics\",\"price\":\"0.00225\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SECURITY_POSTURE_MANAGEMENT\",\"name\":\"Security Posture Management\",\"price\":\"0\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SERVERLESS\",\"name\":\"Serverless Functions Classic\",\"price\":\"0.000004\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SYNTHETIC_MONITORING_BROWSER\",\"name\":\"Browser Monitor or Clickpath\",\"price\":\"0.009\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SYNTHETIC_MONITORING_HTTP\",\"name\":\"HTTP Monitor\",\"price\":\"0.001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SYNTHETIC_MONITORING_THIRD_PARTY\",\"name\":\"Third-Party Synthetic API Ingestion\",\"price\":\"0.001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACE_INGEST\",\"name\":\"Traces - Ingest \\& Process\",\"price\":\"0.2\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACE_QUERY\",\"name\":\"Traces - Query\",\"price\":\"0.0035\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACE_RETAIN\",\"name\":\"Traces - Retain\",\"price\":\"0.0007\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACES\",\"name\":\"Custom Traces Classic\",\"price\":\"0.0000014\",\"currencyCode\":\"USD\"},\n  {\"key\":\"USER_SESSION_PROPERTIES\",\"name\":\"Real User Monitoring Property\",\"price\":\"0.0001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"USER_SESSION_REPLAYS\",\"name\":\"Real User Monitoring with Session Replay\",\"price\":\"0.009\",\"currencyCode\":\"USD\"},\n  {\"key\":\"USER_SESSIONS\",\"name\":\"Real User Monitoring\",\"price\":\"0.00225\",\"currencyCode\":\"USD\"}\n]`\n}",



"multiple": false



}



],



"tiles": {



"33": {



"type": "markdown",



"content": "## Disclaimer\n* ensure to adopt the ratecard_data variable\n* Usage of the Dashboard is free of charge"



},



"36": {



"title": "Capability / Cost center Heatmap",



"description": "",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {sum(usage), sum(cost)}, by:{event.type, filter}",



"visualization": "heatmap",



"visualizationSettings": {



"dataMapping": { "xAxis": "filter", "yAxis": "event.type", "bucketValue": "sum(cost)" },



"axes": { "yAxis": { "showLabel": true } },



"legend": { "ratio": 5 },



"unitsOverrides": [



{



"identifier": "sum(cost)",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": false,



"added": 1753286738031



}



],



"thresholds": []



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"38": {



"title": "",



"type": "data",



"query": "fetch dt.system.events\n\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd entityName(dt.entity.host)\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsAdd usage = toDouble(ingested_bytes) / (1024*1024*1024)\n]\n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd cost = if(event.type == \"Traces - Ingest & Process\", \"not applicable*\", else:usage * toDouble(ratecard.price))\n| fieldsRename currency = ratecard.currencyCode, capability = event.type, price = ratecard.price\n| fieldsKeep usage.start, usage.end, capability, filter, usage, cost, price, currency, dt.entity.host.name, billed_bytes, application_only_type, dt.openpipeline.pipelines, dt.entity.host, billed_container_hours, dt.openpipeline.source, billed_gibibyte_hours, k8s.cluster.uid, k8s.namespace.name, ingested_bytes, ingested_spans, licensing_type\n| sort filter, usage.start, capability\n",



"visualization": "table",



"visualizationSettings": {



"table": {



"hiddenColumns": [["event.version"]],



"hideColumnsForLargeResults": false,



"sortBy": [{ "columnId": "[\"billed_gibibyte_hours\"]", "direction": "descending" }],



"columnOrder": [



"[\"usage.start\"]",



"[\"usage.end\"]",



"[\"capability\"]",



"[\"filter\"]",



"[\"usage\"]",



"[\"cost\"]",



"[\"currency\"]",



"[\"dt.entity.host.name\"]",



"[\"billed_bytes\"]",



"[\"application_only_type\"]",



"[\"dt.openpipeline.pipelines\"]",



"[\"dt.entity.host\"]",



"[\"billed_container_hours\"]",



"[\"dt.openpipeline.source\"]",



"[\"billed_gibibyte_hours\"]",



"[\"k8s.cluster.uid\"]",



"[\"k8s.namespace.name\"]",



"[\"ingested_bytes\"]",



"[\"ingested_spans\"]",



"[\"licensing_type\"]",



"[\"price\"]"



]



},



"thresholds": []



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"40": {



"title": "Estimated Costs per capability and $CostAllocation",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price) \n\n//  | summarize {\n//         total_usage = sum(usage[]),\n//         total_cost = sum(cost[])},\n//         by: { timeframe, interval, event.type, filter }\n// | sort event.type",



"visualization": "lineChart",



"visualizationSettings": {



"chartSettings": {



"xAxisScaling": "analyzedTimeframe",



"fieldMapping": { "leftAxisValues": ["cost"] },



"gapPolicy": "connect"



},



"dataMapping": { "displayedFields": ["filter", "event.type"] },



"autoSelectVisualization": false,



"thresholds": [],



"unitsOverrides": [



{



"identifier": "total_usage",



"unitCategory": "amount",



"baseUnit": "one",



"displayUnit": null,



"decimals": 0,



"suffix": "",



"delimiter": false,



"added": 1754648177039



},



{



"identifier": "total_cost",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": true,



"added": 1754648199722



}



]



},



"querySettings": {



"maxResultRecords": 10000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 5,



"defaultSamplingRatio": 10,



"enableSampling": true



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"44": { "type": "markdown", "content": "## Estimated costs per $CostAllocation" },



"47": {



"title": "Estimated Costs per capability",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price) \n\n | summarize {\n        total_usage = sum(usage[]),\n        total_cost = sum(cost[])},\n        by: { timeframe, interval, event.type }\n| sort event.type",



"visualization": "lineChart",



"visualizationSettings": {



"chartSettings": {



"xAxisScaling": "analyzedTimeframe",



"fieldMapping": { "leftAxisValues": ["total_cost"] },



"gapPolicy": "connect"



},



"dataMapping": { "displayedFields": ["event.type"] },



"autoSelectVisualization": false,



"thresholds": [],



"unitsOverrides": [



{



"identifier": "usage",



"unitCategory": "amount",



"baseUnit": "one",



"displayUnit": null,



"decimals": 0,



"suffix": "",



"delimiter": false,



"added": 1754648177039



},



{



"identifier": "cost",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": true,



"added": 1754648199722



}



]



},



"querySettings": {



"maxResultRecords": 5000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"48": { "type": "markdown", "content": "## Historical view of capabilities" },



"50": {



"title": "Estimated cost distribution per Capability",



"description": "",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start,nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}, by:{capability=event.type}\n",



"visualization": "pieChart",



"visualizationSettings": {



"autoSelectVisualization": false,



"chartSettings": {



"legend": { "position": "right" },



"categoricalBarChartSettings": {



"valueAxis": "total_cost",



"valueAxisLabel": "total_cost",



"categoryAxis": ["capability"],



"categoryAxisLabel": "capability"



},



"circleChartSettings": {



"valueType": "relative",



"groupingThresholdType": "number-of-slices",



"groupingThresholdValue": 20,



"groupingName": "Other"



}



},



"legend": { "ratio": 52 },



"thresholds": [],



"unitsOverrides": [



{



"identifier": "total_usage",



"unitCategory": "amount",



"baseUnit": "one",



"displayUnit": null,



"decimals": 0,



"suffix": "",



"delimiter": false,



"added": 1754648177039



},



{



"identifier": "total_cost",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": true,



"added": 1754648199722



}



]



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"52": {



"title": "List of usage and estimated costs per Capability and Cost Center",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}, by:{capability=event.type,filter}\n| sort total_cost desc",



"visualization": "table",



"visualizationSettings": {



"table": {



"sortBy": [{ "columnId": "[\"capability\"]", "direction": "descending" }],



"columnWidths": { "[\"event.type\"]": 312, "[\"total_cost\"]": 88 },



"columnOrder": [



"[\"capability\"]",



"[\"filter\"]",



"[\"total_usage\"]",



"[\"total_cost\"]"



]



},



"thresholds": [],



"unitsOverrides": [



{



"identifier": "total_usage",



"unitCategory": "amount",



"baseUnit": "one",



"displayUnit": null,



"decimals": 0,



"suffix": "",



"delimiter": false,



"added": 1754648177039



},



{



"identifier": "total_cost",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": true,



"added": 1754648199722



}



]



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"56": {



"type": "markdown",



"content": "## Change Log\n* v 3: Branched a version w/o lookup tables to ensure no related costs\n* v 3.1: dedup events \n* v 3.2: fixed some overlooked lookup table references\n* v 3.3: Adjusted for Log Retain/RwiQ & Fixed Trace Ingest billed usage"



},



"57": {



"title": "Estimated cost distribution per cost center",



"description": "Showing only values above 5% of total costs",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}, by:{filter}\n| sort total_cost desc",



"visualization": "pieChart",



"visualizationSettings": {



"chartSettings": {



"legend": { "position": "right" },



"colorPalette": "fireplace-inverted",



"categoricalBarChartSettings": {



"categoryAxis": ["capability", "filter"],



"categoryAxisLabel": "capability,filter",



"valueAxis": "total_cost",



"valueAxisLabel": "total_cost"



},



"circleChartSettings": {



"valueType": "relative",



"groupingThresholdType": "number-of-slices",



"groupingThresholdValue": 10,



"groupingName": "Other"



}



},



"legend": { "ratio": 52 },



"autoSelectVisualization": false,



"thresholds": [],



"unitsOverrides": [



{



"identifier": "total_usage",



"unitCategory": "amount",



"baseUnit": "one",



"displayUnit": null,



"decimals": 0,



"suffix": "",



"delimiter": false,



"added": 1754648177039



},



{



"identifier": "total_cost",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": true,



"added": 1754648199722



}



]



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"58": {



"title": "Used Ratecard (can be changed by editing the ratecard_data variable <---)",



"type": "data",



"query": "data json:$ratecard_data",



"visualization": "table",



"visualizationSettings": {



"autoSelectVisualization": true,



"table": { "sortBy": [{ "columnId": "[\"key\"]", "direction": "ascending" }] }



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"60": {



"title": "Estimated cost distribution per Capability",



"description": "",



"type": "data",



"query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}\n",



"visualization": "singleValue",



"visualizationSettings": {



"singleValue": { "label": "total costs", "recordField": "total_cost" },



"autoSelectVisualization": false,



"thresholds": [],



"unitsOverrides": [



{



"identifier": "total_usage",



"unitCategory": "amount",



"baseUnit": "one",



"displayUnit": null,



"decimals": 0,



"suffix": "",



"delimiter": false,



"added": 1754648177039



},



{



"identifier": "total_cost",



"unitCategory": "currency",



"baseUnit": "usd",



"displayUnit": null,



"decimals": 2,



"suffix": "",



"delimiter": true,



"added": 1754648199722



}



]



},



"querySettings": {



"maxResultRecords": 1000,



"defaultScanLimitGbytes": 500,



"maxResultMegaBytes": 1,



"defaultSamplingRatio": 10,



"enableSampling": false



},



"davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



},



"61": {



"type": "markdown",



"content": "*shown trace usage also includes included, non billable usage. The calculation for billable Traces cannot be done on record level. Therefore costs cannot be calculated within this table. For the Trace Ingest usage and costs which is billable - check the other tiles please."



},



"62": { "type": "markdown", "content": "## Maximum detail level for usage" }



},



"layouts": {



"33": { "x": 0, "y": 0, "w": 12, "h": 2 },



"36": { "x": 0, "y": 23, "w": 12, "h": 4 },



"38": { "x": 0, "y": 35, "w": 24, "h": 10 },



"40": { "x": 12, "y": 29, "w": 12, "h": 5 },



"44": { "x": 0, "y": 14, "w": 24, "h": 2 },



"47": { "x": 0, "y": 29, "w": 12, "h": 5 },



"48": { "x": 0, "y": 27, "w": 24, "h": 2 },



"50": { "x": 0, "y": 7, "w": 12, "h": 7 },



"52": { "x": 12, "y": 16, "w": 12, "h": 11 },



"56": { "x": 0, "y": 2, "w": 12, "h": 5 },



"57": { "x": 0, "y": 16, "w": 12, "h": 7 },



"58": { "x": 12, "y": 0, "w": 12, "h": 7 },



"60": { "x": 12, "y": 7, "w": 12, "h": 7 },



"61": { "x": 0, "y": 45, "w": 24, "h": 1 },



"62": { "x": 0, "y": 34, "w": 24, "h": 1 }



},



"importedWithCode": true,



"settings": {}



}
```

3. Map users to Cost Allocation metadata

In the notebook that you imported, set up the mapping between users and attributes.

1. Create a list of users whose account activity you want to map to a given cost center or product.

   The **Quickstart: Retrieve a list of active Dynatrace users** card provides a list of all users who are active in the relevant environment.

   Each user is identified with an email and a unique user ID.
2. Create a list of all cost centers and products that costs should be allocated to.

   The **Fetch already used cost centers** and **Fetch already used products** cards provide a list of all tags that are configured in your environment.
3. For each user, create a JSON object that defines the `user.email`, `user.id`, `dt.cost.costcenter`, and `dt.cost.product`.
   Make sure that this object matches the JSON syntax shown in the code block below.

   ```
   {



   "user.email": "abc@de.fg",



   "user.id": "00000000-0000-0000-0000-000000000000",



   "dt.cost.costcenter": "a",



   "dt.cost.product": "1"



   }
   ```
4. Once you've created JSON objects for each user, paste these into the **Store user mapping within lookup table** card.
   Note that you may need to select  **Show input** to enter the JSON contents.
5. Once you've entered all relevant JSON objects, select  **Run** to upload the lookup table to your environment.

4. Update the prices according to your rate card

In the notebook you imported, set your prices for all the relevant rate card capabilities.

1. In the **Store rate card within lookup table - ADJUST PRICES** card, enter your rate-card prices for all the relevant capabilities.
   An example for the Automation Workflow capability is shown below.

   ```
   {



   "key": "AUTOMATIONS",



   "name": "Automation Workflow",



   "price": "0.13",



   "currencyCode": "USD"



   }
   ```

   Note that you may need to select  **Show input** to enter the JSON.
2. Once you've updated the relevant prices, select  **Run** to upload the lookup table to your environment.

5. Use the dashboard

Once you've configured the user mappings and the rate card prices, you can use the **Cost Allocation with extended lookup tables** dashboard to see costs related to queries, workflows, and functions.

To access the dashboard, go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and find the dashboard you uploaded.

If you see a `The tabular file <file> doesn't exist.` error message in your dashboard, the `userdata` or `ratecard` lookup tables are improperly configured.
Repeat the steps in [Map users to Cost Allocation metadata](#map-user-accounts) or [Update the prices according to your rate card](#update-rate-card) as appropriate.

## Best practices

This section provides best practices for setting up Cost Allocation.

### Cost center and product names

How you name your cost centers and products is up to you.
We recommend:

* For cost centers: Use the organizational level to which the costs belong.
* For products: Use the application or product group to which the costs belong.

Values can be provided as text or numerical strings.
If you have both, we recommend to use both the text-based name and the ID, separated by a comma (`,`) or slash (`/`).
This lets you separate the name and ID after a data export.

Examples:

Host

Cost center

Product

Host 1

`dt.cost.costcenter=BusinessUnit1/Bu1`

`dt.cost.product=AppName/AppID`

Host 2

`dt.cost.costcenter=BusinessUnit2/Bu2`

`dt.cost.product=AppName/AppID`

Host 3

`dt.cost.costcenter=BusinessUnit2/Bu2`

`dt.cost.product=AppName/AppID`

### Handling shared costs

If your host shares services, Cost Allocation doesn't support costs billed to separate cost centers or products.
However, you can create a cost center or product for that host and then allocate its costs outside of Dynatrace.

1. Create a cost center or product for both entities, such as `dt.cost.product="Webpage_MobileApp"` for a host that should be allocated to both the webpage product and the mobile app product.
2. When you want to analyze past data, retrieve the data from Account Management and import them into an Excel or Power BI board.
3. You can take the host's total costs and split them according to your requirements.

DPS licensing consumption and related costs are based on 15-minute increments.
Reports are generated daily, so you won't be able to see usage accrued in the previous <24 hours.

## Analyze Cost Allocation data

To analyze Cost Allocation data, you can

* Use Dynatrace environment-specific dashboards, notebooks, or DQL, as described in [Analyze in Dynatrace](#analyze-in-dynatrace).
* Export data to an external tool, as described in [Export Cost Allocation data via Account Management](#cost-allocation-export).

### Analyze in Dynatrace

Cost Allocation data is stored in [Dynatrace Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more.") as billing usage events.
These events can be analyzed

* In ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** and ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
  Dynatrace provides a built-in Dashboard, **DPS Cost Allocation usage & costs**.
  Examples from this dashboard are provided below.
* Via [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") queries.
  Example DQL queries are provided below.

Visit the [Dynatrace DPS Cost Allocation communityï»¿](https://dt-url.net/30a0fb7) to see how other Dynatracers analyze their Cost Allocation data.

#### Analyze in Dashboards and Notebooks

To analyze Cost Allocation data, you can use the pre-made dashboard.

The pre-made dashboard is enough to get you going right away, but it is really intended as just a starting point.
Please adapt the dashboard to fit to your needs and use-case scenarios.

Known limitations

The dashboard does not automatically account for [included trace amounts](/docs/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.").
Therefore, the costs shown are actually higher than what you will be billed for.

This will be updated in a future release of the dashboard.

The dashboard is available:

* In the built-in environment.
* As a JSON file, which you can upload to any other Dynatrace environment (see [Upload a dashboard](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new#dashboards-upload "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.")).

  1. Copy the JSON contents from the code block below and save them to a file on your computer.

     Cost Allocation pre-made dashboard JSON contents

     ```
     {



     "version": 20,



     "variables": [



     {



     "version": 2,



     "key": "CostAllocation",



     "type": "csv",



     "visible": true,



     "editable": true,



     "input": "costcenter,product",



     "multiple": false,



     "defaultValue": "costcenter"



     },



     {



     "version": 2,



     "key": "Filter",



     "type": "query",



     "visible": true,



     "editable": true,



     "input": "fetch dt.system.events\n| filter $CostAllocation == \"costcenter\"\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| fieldsAdd value = coalesce(dt.cost.costcenter, $unassigned)\n| summarize count(), by: {value}\n| fieldsKeep value\n| append [\n  fetch dt.system.events\n  | filter $CostAllocation == \"product\"\n  | filter event.kind == \"BILLING_USAGE_EVENT\"\n  | fieldsAdd value = coalesce(dt.cost.product, $unassigned)\n  | summarize count(), by: {value}\n  | fieldsKeep value\n]",



     "multiple": true,



     "defaultValue": ["3420b2ac-f1cf-4b24-b62d-61ba1ba8ed05*"]



     },



     {



     "version": 2,



     "key": "Capability",



     "type": "query",



     "visible": true,



     "editable": true,



     "input": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| expand dt.cost.costcenter\n| fieldsAdd dt.cost.costcenter = coalesce(dt.cost.costcenter[key], dt.cost.costcenter)\n| expand dt.cost.product\n| fieldsAdd dt.cost.product = coalesce(dt.cost.product[key], dt.cost.product)\n| filter $SupportedCapabilitiesOnly == \"no\" OR isNotNull(dt.cost.costcenter) OR isNotNull(dt.cost.product)\n| fields event.type\n| dedup event.type",



     "multiple": true



     },



     {



     "version": 2,



     "key": "unassigned",



     "type": "text",



     "visible": false,



     "editable": true,



     "defaultValue": "unassigned"



     },



     {



     "version": 2,



     "key": "SupportedCapabilitiesOnly",



     "type": "csv",



     "visible": true,



     "editable": true,



     "input": "yes,no",



     "multiple": false,



     "defaultValue": "yes"



     },



     {



     "version": 2,



     "key": "ratecard_data",



     "type": "code",



     "visible": false,



     "editable": true,



     "input": "/*\n* This will run JavaScript in the DYNATRACE\n* serverless environment.\n* To generate variable options return string array.\n*/\nexport default async function () {\n  return `[\n  {\"key\":\"AUTOMATIONS\",\"name\":\"Automation Workflow\",\"price\":\"0.13\",\"currencyCode\":\"USD\"},\n  {\"key\":\"BUSINESS_EVENTS_ANALYZE\",\"name\":\"Events - Query\",\"price\":\"0.0035\",\"currencyCode\":\"USD\"},\n  {\"key\":\"BUSINESS_EVENTS_INGEST\",\"name\":\"Events - Ingest & Process\",\"price\":\"0.2\",\"currencyCode\":\"USD\"},\n  {\"key\":\"BUSINESS_EVENTS_RETAIN\",\"name\":\"Events - Retain\",\"price\":\"0.0007\",\"currencyCode\":\"USD\"},\n  {\"key\":\"CODE_MONITORING\",\"name\":\"Code Monitoring\",\"price\":\"0.005\",\"currencyCode\":\"USD\"},\n  {\"key\":\"COMPUTE\",\"name\":\"AppEngine Functions - Small\",\"price\":\"0.001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"EVENTS\",\"name\":\"Custom Events Classic\",\"price\":\"0.000002\",\"currencyCode\":\"USD\"},\n  {\"key\":\"FOUNDATION_AND_DISCOVERY\",\"name\":\"Foundation & Discovery\",\"price\":\"0.01\",\"currencyCode\":\"USD\"},\n  {\"key\":\"FULLSTACK_MONITORING\",\"name\":\"Full-Stack Monitoring\",\"price\":\"0.01\",\"currencyCode\":\"USD\"},\n  {\"key\":\"INFRASTRUCTURE_MONITORING\",\"name\":\"Infrastructure Monitoring\",\"price\":\"0.04\",\"currencyCode\":\"USD\"},\n  {\"key\":\"KUBERNETES_OPERATIONS\",\"name\":\"Kubernetes Platform Monitoring\",\"price\":\"0.002\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOG_MANAGEMENT_ANALYZE\",\"name\":\"Log Management & Analytics - Query\",\"price\":\"0.0035\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOG_MANAGEMENT_INGEST\",\"name\":\"Log Management & Analytics - Ingest & Process\",\"price\":\"0.2\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOG_MANAGEMENT_RETAIN\",\"name\":\"Log Management & Analytics - Retain\",\"price\":\"0.0007\",\"currencyCode\":\"USD\"},\n  {\"key\":\"LOGS\",\"name\":\"Log Monitoring Classic\",\"price\":\"0.000001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"MAINFRAME_MONITORING\",\"name\":\"Mainframe Monitoring\",\"price\":\"0.1\",\"currencyCode\":\"USD\"},\n  {\"key\":\"METRICS\",\"name\":\"Custom Metrics Classic\",\"price\":\"0.000002\",\"currencyCode\":\"USD\"},\n  {\"key\":\"RUNTIME_APPLICATION_PROTECTION\",\"name\":\"Runtime Application Protection\",\"price\":\"0.00225\",\"currencyCode\":\"USD\"},\n  {\"key\":\"RUNTIME_VULNERABILITY_ANALYTICS\",\"name\":\"Runtime Vulnerability Analytics\",\"price\":\"0.00225\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SECURITY_POSTURE_MANAGEMENT\",\"name\":\"Security Posture Management\",\"price\":\"0\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SERVERLESS\",\"name\":\"Serverless Functions Classic\",\"price\":\"0.000004\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SYNTHETIC_MONITORING_BROWSER\",\"name\":\"Browser Monitor or Clickpath\",\"price\":\"0.009\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SYNTHETIC_MONITORING_HTTP\",\"name\":\"HTTP Monitor\",\"price\":\"0.001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"SYNTHETIC_MONITORING_THIRD_PARTY\",\"name\":\"Third-Party Synthetic API Ingestion\",\"price\":\"0.001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACE_INGEST\",\"name\":\"Traces - Ingest \\& Process\",\"price\":\"0.2\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACE_QUERY\",\"name\":\"Traces - Query\",\"price\":\"0.0035\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACE_RETAIN\",\"name\":\"Traces - Retain\",\"price\":\"0.0007\",\"currencyCode\":\"USD\"},\n  {\"key\":\"TRACES\",\"name\":\"Custom Traces Classic\",\"price\":\"0.0000014\",\"currencyCode\":\"USD\"},\n  {\"key\":\"USER_SESSION_PROPERTIES\",\"name\":\"Real User Monitoring Property\",\"price\":\"0.0001\",\"currencyCode\":\"USD\"},\n  {\"key\":\"USER_SESSION_REPLAYS\",\"name\":\"Real User Monitoring with Session Replay\",\"price\":\"0.009\",\"currencyCode\":\"USD\"},\n  {\"key\":\"USER_SESSIONS\",\"name\":\"Real User Monitoring\",\"price\":\"0.00225\",\"currencyCode\":\"USD\"}\n]`\n}",



     "multiple": false



     }



     ],



     "tiles": {



     "33": {



     "type": "markdown",



     "content": "## Disclaimer\n* ensure to adopt the ratecard_data variable\n* Usage of the Dashboard is free of charge"



     },



     "36": {



     "title": "Capability / Cost center Heatmap",



     "description": "",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {sum(usage), sum(cost)}, by:{event.type, filter}",



     "visualization": "heatmap",



     "visualizationSettings": {



     "dataMapping": { "xAxis": "filter", "yAxis": "event.type", "bucketValue": "sum(cost)" },



     "axes": { "yAxis": { "showLabel": true } },



     "legend": { "ratio": 5 },



     "unitsOverrides": [



     {



     "identifier": "sum(cost)",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": false,



     "added": 1753286738031



     }



     ],



     "thresholds": []



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "38": {



     "title": "",



     "type": "data",



     "query": "fetch dt.system.events\n\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd entityName(dt.entity.host)\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsAdd usage = toDouble(ingested_bytes) / (1024*1024*1024)\n]\n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd cost = if(event.type == \"Traces - Ingest & Process\", \"not applicable*\", else:usage * toDouble(ratecard.price))\n| fieldsRename currency = ratecard.currencyCode, capability = event.type, price = ratecard.price\n| fieldsKeep usage.start, usage.end, capability, filter, usage, cost, price, currency, dt.entity.host.name, billed_bytes, application_only_type, dt.openpipeline.pipelines, dt.entity.host, billed_container_hours, dt.openpipeline.source, billed_gibibyte_hours, k8s.cluster.uid, k8s.namespace.name, ingested_bytes, ingested_spans, licensing_type\n| sort filter, usage.start, capability\n",



     "visualization": "table",



     "visualizationSettings": {



     "table": {



     "hiddenColumns": [["event.version"]],



     "hideColumnsForLargeResults": false,



     "sortBy": [{ "columnId": "[\"billed_gibibyte_hours\"]", "direction": "descending" }],



     "columnOrder": [



     "[\"usage.start\"]",



     "[\"usage.end\"]",



     "[\"capability\"]",



     "[\"filter\"]",



     "[\"usage\"]",



     "[\"cost\"]",



     "[\"currency\"]",



     "[\"dt.entity.host.name\"]",



     "[\"billed_bytes\"]",



     "[\"price\"]",



     "[\"ingested_bytes\"]",



     "[\"ingested_spans\"]",



     "[\"licensing_type\"]"



     ]



     },



     "thresholds": []



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "40": {



     "title": "Estimated Costs per capability and $CostAllocation",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price) \n\n\n//  | summarize {\n//         total_usage = sum(usage[]),\n//         total_cost = sum(cost[])},\n//         by: { timeframe, interval, event.type, filter }\n// | sort event.type",



     "visualization": "lineChart",



     "visualizationSettings": {



     "chartSettings": {



     "xAxisScaling": "analyzedTimeframe",



     "fieldMapping": { "leftAxisValues": ["cost"] },



     "gapPolicy": "connect"



     },



     "dataMapping": { "displayedFields": ["filter", "event.type"] },



     "autoSelectVisualization": false,



     "thresholds": [],



     "unitsOverrides": [



     {



     "identifier": "total_usage",



     "unitCategory": "amount",



     "baseUnit": "one",



     "displayUnit": null,



     "decimals": 0,



     "suffix": "",



     "delimiter": false,



     "added": 1754648177039



     },



     {



     "identifier": "total_cost",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": true,



     "added": 1754648199722



     }



     ]



     },



     "querySettings": {



     "maxResultRecords": 10000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 5,



     "defaultSamplingRatio": 10,



     "enableSampling": true



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "44": { "type": "markdown", "content": "## Estimated costs per $CostAllocation" },



     "47": {



     "title": "Estimated Costs per capability",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price) \n\n | summarize {\n        total_usage = sum(usage[]),\n        total_cost = sum(cost[])},\n        by: { timeframe, interval, event.type }\n| sort event.type",



     "visualization": "lineChart",



     "visualizationSettings": {



     "chartSettings": {



     "xAxisScaling": "analyzedTimeframe",



     "fieldMapping": { "leftAxisValues": ["total_cost"] },



     "gapPolicy": "connect"



     },



     "dataMapping": { "displayedFields": ["event.type"] },



     "autoSelectVisualization": false,



     "thresholds": [],



     "unitsOverrides": [



     {



     "identifier": "usage",



     "unitCategory": "amount",



     "baseUnit": "one",



     "displayUnit": null,



     "decimals": 0,



     "suffix": "",



     "delimiter": false,



     "added": 1754648177039



     },



     {



     "identifier": "cost",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": true,



     "added": 1754648199722



     }



     ]



     },



     "querySettings": {



     "maxResultRecords": 5000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "48": { "type": "markdown", "content": "## Historical view of capabilities" },



     "50": {



     "title": "Estimated cost distribution per Capability",



     "description": "",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start,nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}, by:{capability=event.type}\n",



     "visualization": "pieChart",



     "visualizationSettings": {



     "chartSettings": {



     "legend": { "position": "right" },



     "categoricalBarChartSettings": {



     "valueAxis": "total_cost",



     "valueAxisLabel": "total_cost",



     "categoryAxis": ["capability"],



     "categoryAxisLabel": "capability"



     },



     "circleChartSettings": {



     "valueType": "relative",



     "groupingThresholdType": "number-of-slices",



     "groupingThresholdValue": 20,



     "groupingName": "Other"



     }



     },



     "legend": { "ratio": 33 },



     "autoSelectVisualization": false,



     "thresholds": [],



     "unitsOverrides": [



     {



     "identifier": "total_usage",



     "unitCategory": "amount",



     "baseUnit": "one",



     "displayUnit": null,



     "decimals": 0,



     "suffix": "",



     "delimiter": false,



     "added": 1754648177039



     },



     {



     "identifier": "total_cost",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": true,



     "added": 1754648199722



     }



     ]



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "52": {



     "title": "List of usage and estimated costs per Capability and Cost Center",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}, by:{capability=event.type,filter}\n| sort total_cost desc",



     "visualization": "table",



     "visualizationSettings": {



     "table": {



     "sortBy": [{ "columnId": "[\"capability\"]", "direction": "descending" }],



     "columnWidths": { "[\"event.type\"]": 312, "[\"total_cost\"]": 88 },



     "columnOrder": [



     "[\"capability\"]",



     "[\"filter\"]",



     "[\"total_usage\"]",



     "[\"total_cost\"]"



     ]



     },



     "thresholds": [],



     "unitsOverrides": [



     {



     "identifier": "total_usage",



     "unitCategory": "amount",



     "baseUnit": "one",



     "displayUnit": null,



     "decimals": 0,



     "suffix": "",



     "delimiter": false,



     "added": 1754648177039



     },



     {



     "identifier": "total_cost",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": true,



     "added": 1754648199722



     }



     ]



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "56": {



     "type": "markdown",



     "content": "## Change Log\n* v 3: Branched a version w/o lookup tables to ensure no related costs\n* v 3.1: dedup events \n* v 3.2: fixed some overlooked lookup table references\n* v 3.3: Adjusted for Log Retain/RwiQ & Fixed Trace Ingest billed usage"



     },



     "57": {



     "title": "Estimated cost distribution per cost center",



     "description": "Showing only values above 5% of total costs",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}, by:{filter}\n| sort total_cost desc",



     "visualization": "pieChart",



     "visualizationSettings": {



     "chartSettings": {



     "legend": { "position": "right" },



     "colorPalette": "fireplace-inverted",



     "categoricalBarChartSettings": {



     "valueAxis": "total_cost",



     "valueAxisLabel": "total_cost",



     "categoryAxis": ["capability", "filter"],



     "categoryAxisLabel": "capability,filter"



     },



     "circleChartSettings": {



     "valueType": "relative",



     "groupingThresholdType": "number-of-slices",



     "groupingThresholdValue": 10,



     "groupingName": "Other"



     }



     },



     "legend": { "ratio": 33 },



     "autoSelectVisualization": false,



     "thresholds": [],



     "unitsOverrides": [



     {



     "identifier": "total_usage",



     "unitCategory": "amount",



     "baseUnit": "one",



     "displayUnit": null,



     "decimals": 0,



     "suffix": "",



     "delimiter": false,



     "added": 1754648177039



     },



     {



     "identifier": "total_cost",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": true,



     "added": 1754648199722



     }



     ]



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "58": {



     "title": "Used Ratecard (can be changed by editing the ratecard_data variable <---)",



     "type": "data",



     "query": "data json:$ratecard_data",



     "visualization": "table",



     "visualizationSettings": {



     "autoSelectVisualization": true,



     "table": { "sortBy": [{ "columnId": "[\"key\"]", "direction": "ascending" }] }



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "60": {



     "title": "Estimated cost distribution per Capability",



     "description": "",



     "type": "data",



     "query": "fetch dt.system.events\n| filter event.kind == \"BILLING_USAGE_EVENT\"\n| filterOut event.type ==\"Traces - Ingest & Process\" //traces need special handling\n| dedup event.id\n| filter in(event.type, {$Capability})\n| fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n| fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n| fieldsRemove dt.cost.costcenter, dt.cost.product\n| expand costallocation\n| fieldsAdd filter = coalesce(costallocation[key], costallocation)\n| filter in(filter, {$Filter})\n| fieldsAdd billed_bytes = coalesce(costallocation[billed_bytes], billed_bytes)\n| fieldsAdd usage = coalesce(\n    billed_host_hours, //Infra, F&D\n    billed_gibibyte_hours, //Fullstack, Runtime Application Protection, Runtime Vulnerability Analytics\n    toDouble(billed_bytes) / (1024*1024*1024), //ALL I/R/Q\n    billed_invocations, //AppEngine\n    ingested_bytes,\n    1 //workflow count\n    )\n| fieldsAdd usage.start = if(isNull(usage.start), timestamp, else: usage.start)\n| makeTimeseries interval: 15m, time: usage.start, nonempty:false, by:{filter, event.type },{\n  usage = sum(usage)\n}\n| append [\n// THIS IS JUST FOR TRACES INGEST NORMALIZATION ----->\n\n\n      FETCH dt.system.events\n      | filter event.kind == \"BILLING_USAGE_EVENT\" and event.type == \"Traces - Ingest & Process\"\n      | filter in(event.type, {$Capability})\n      | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n      | fieldsRemove dt.cost.costcenter, dt.cost.product\n      | fieldsAdd filter = costallocation\n      | filter in(filter, {$Filter})\n      | fieldsKeep usage.start, licensing_type, ingested_bytes, costallocation, event.id\n      | dedup event.id\n      | fieldsAdd licensing_type = if(in(licensing_type, {\n        \"otlp-trace-ingest\", \"serverless\"}), \"other\", else: licensing_type)\n      \n      | fieldsAdd adaptive_volume = if(licensing_type == \"fullstack-adaptive\", ingested_bytes)\n      | fieldsAdd fixed_rate_volume = if(licensing_type == \"fullstack-fixed-rate\", ingested_bytes)\n      | fieldsAdd other_volume = if(licensing_type == \"other\", ingested_bytes)\n    \n      | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      \n      | makeTimeseries interval: 15m, time: usage.start, by: {\n        costallocation}, nonempty: true, {\n        adaptive_volume = sum(adaptive_volume, default: 0),\n        fixed_rate_volume = sum(fixed_rate_volume, default: 0),\n        other_volume = sum(other_volume, default: 0)\n      }\n      \n        // calculate included volume per costcenter and join with trace-ingest usage\n      | join [\n          FETCH dt.system.events\n          | filter event.kind == \"BILLING_USAGE_EVENT\"\n          | filter event.type == \"Full-Stack Monitoring\"\n          | fieldsAdd costallocation = if($CostAllocation==\"costcenter\",dt.cost.costcenter, else: dt.cost.product)\n          | fieldsRemove dt.cost.costcenter, dt.cost.product\n          | fieldsKeep usage.start, billed_gibibyte_hours, costallocation, event.id\n          | dedup event.id\n          | makeTimeseries {\n            billed = sum(billed_gibibyte_hours) }, by: {\n            costallocation }, time: usage.start, interval: 15m\n          | summarize by: {\n            timeframe, interval }, {\n            total = sum(billed[]), r = collectArray(record(costallocation, billed)) }\n          | expand r\n          | fieldsFlatten r, fields: {\n            costallocation, billed }\n          | fieldsAdd ratio = billed[] / total[]\n          | fields timeframe, interval, costallocation, ratio\n          | join [\n              timeseries interval: 15m, union: true, nonempty: true, {\n                included_volume = max(dt.billing.traces.maximum_included_fullstack_volume_per_minute, default: null),\n                configured_volume = max(dt.billing.traces.maximum_configured_fullstack_volume_per_minute, default: null)\n              }\n              | fieldsAdd interval_in_minutes = toLong(interval) / 60000000000\n              | fieldsAdd extra_ingest_on = configured_volume[] > included_volume[]\n              | fieldsAdd included_volume = interval_in_minutes * if(isNull(configured_volume[]), null, else: included_volume[])\n          ], on: {\n            timeframe, interval }, fields: {\n            included_volume, extra_ingest_on }\n          | fieldsAdd included_volume_costallocation = included_volume[] * ratio[]\n          | fieldsAdd costallocation = if(isNull(costallocation), $unassigned, else: costallocation)\n      ], on: {\n        timeframe, interval, costallocation }, kind: outer, prefix: \"included.\"\n      \n      | fieldsAdd timeframe = coalesce(timeframe, included.timeframe)\n      | fieldsAdd interval = coalesce(interval, included.interval)\n      | fieldsAdd costallocation = coalesce(costallocation, included.costallocation)\n      | fieldsAdd\n          extra_ingest_on =\n              if(exists(included.extra_ingest_on) and isNotNull(included.extra_ingest_on), included.extra_ingest_on,\n                else: array(false, false, false, false))\n      \n      | fieldsAdd included_volume_costallocation = included.included_volume_costallocation\n        // replace nulls with 0\n      | fieldsAdd adaptive_volume = iCollectArray(coalesce(adaptive_volume[], 0))\n      | fieldsAdd fixed_rate_volume = iCollectArray(coalesce(fixed_rate_volume[], 0))\n      | fieldsAdd other_volume = iCollectArray(coalesce(other_volume[], 0))\n      \n      | fieldsKeep timeframe, interval, costallocation, adaptive_volume, fixed_rate_volume, other_volume,\n          included_volume_costallocation, extra_ingest_on\n      \n        // calculate fullstack trace-ingest usage per costcenter\n      | fieldsAdd license_remaining = included_volume_costallocation[] - adaptive_volume[]\n      | fieldsAdd license_remaining = if(license_remaining[] > 0, license_remaining[], else: 0)\n      \n      | fieldsAdd\n          billable_fullstack =\n              if(isNull(included_volume_costallocation[]), 0,\n                else: if(extra_ingest_on[], adaptive_volume[] + fixed_rate_volume[] - included_volume_costallocation[],\n                  else: fixed_rate_volume[] - license_remaining[]))\n      \n      | fieldsAdd billable_fullstack = if(billable_fullstack[] > 0, billable_fullstack[], else: 0)\n      \n      | summarize {\n        total_included = sum(included_volume_costallocation[]),\n        total_adaptive = sum(adaptive_volume[]),\n        total_fixed_rate = sum(fixed_rate_volume[]),\n        total_fullstack_to_allocate = sum(billable_fullstack[]),\n        per_costallocation = collectArray(record(extra_ingest_on, billable_fullstack, billable_other = other_volume, costallocation, included_volume_costallocation))}, \n        by: { timeframe, interval }\n      | expand per_costallocation\n      | fieldsFlatten per_costallocation\n      | fieldsRemove per_costallocation\n      \n      | fieldsAdd total_license_remaining = total_included[] - total_adaptive[]\n      | fieldsAdd total_license_remaining = if(total_license_remaining[] > 0, total_license_remaining[], else: 0)\n      | fieldsAdd\n          total_applicable_fullstack =\n              if(isNull(per_costallocation.included_volume_costallocation), 0,\n                else: if(per_costallocation.extra_ingest_on[], total_adaptive[] + total_fixed_rate[] - total_included[],\n                  else: total_fixed_rate[] - total_license_remaining[]))\n      | fieldsAdd total_billable_fullstack = if(total_applicable_fullstack[] > 0, total_applicable_fullstack[], else: 0)\n      \n      | fieldsAdd\n          distributed_fullstack =\n              if(total_fullstack_to_allocate[] <= 0, 0,\n                else: per_costallocation.billable_fullstack[] / total_fullstack_to_allocate[] * total_billable_fullstack[])\n      // filter out  entry if the included was not fetched\n      | fieldsAdd\n          adjusted_billable_total_per_costallocation =\n              per_costallocation.billable_other[] + if(total_included[] == 0, null, else: toDouble(distributed_fullstack[]))\n      | filterOut isNull(adjusted_billable_total_per_costallocation)\n      \n      | fields timeframe, interval, costallocation = per_costallocation.costallocation, adjusted_billable_total_per_costallocation\n      | fieldsAdd event.type =\"Traces - Ingest & Process\"\n      | fieldsAdd filter = costallocation\n]\n| fieldsAdd traces_usage = adjusted_billable_total_per_costallocation[] / (1024*1024*1024)\n// <---------THIS IS JUST FOR TRACES INGEST NORMALIZATION \n\n| lookup [\n   data json:$ratecard_data\n], sourceField:event.type, lookupField:name, prefix: \"ratecard.\"\n| fieldsAdd isnull = isNull(adjusted_billable_total_per_costallocation)\n| fieldsAdd usage = if(isnull, usage, else: traces_usage)\n| fieldsKeep timeframe, interval, costallocation, event.type, usage,ratecard.price, filter\n| fieldsAdd cost = usage[] * toDouble(ratecard.price)\n| fieldsAdd cost = arraySum(cost)\n| fieldsAdd usage = arraySum(usage)\n| summarize {total_usage=sum(usage), total_cost=sum(cost)}\n",



     "visualization": "singleValue",



     "visualizationSettings": {



     "singleValue": { "label": "total costs", "recordField": "total_cost" },



     "autoSelectVisualization": false,



     "thresholds": [],



     "unitsOverrides": [



     {



     "identifier": "total_usage",



     "unitCategory": "amount",



     "baseUnit": "one",



     "displayUnit": null,



     "decimals": 0,



     "suffix": "",



     "delimiter": false,



     "added": 1754648177039



     },



     {



     "identifier": "total_cost",



     "unitCategory": "currency",



     "baseUnit": "usd",



     "displayUnit": null,



     "decimals": 2,



     "suffix": "",



     "delimiter": true,



     "added": 1754648199722



     }



     ]



     },



     "querySettings": {



     "maxResultRecords": 1000,



     "defaultScanLimitGbytes": 500,



     "maxResultMegaBytes": 1,



     "defaultSamplingRatio": 10,



     "enableSampling": false



     },



     "davis": { "enabled": false, "davisVisualization": { "isAvailable": true } }



     },



     "61": {



     "type": "markdown",



     "content": "*shown trace usage also includes included, non billable usage. The calculation for billable Traces cannot be done on record level. Therefore costs cannot be calculated within this table. For the Trace Ingest usage and costs which is billable - check the other tiles please."



     },



     "62": { "type": "markdown", "content": "## Maximum detail level for usage" }



     },



     "layouts": {



     "33": { "x": 0, "y": 0, "w": 12, "h": 2 },



     "36": { "x": 0, "y": 20, "w": 12, "h": 4 },



     "38": { "x": 0, "y": 32, "w": 24, "h": 10 },



     "40": { "x": 12, "y": 26, "w": 12, "h": 5 },



     "44": { "x": 0, "y": 12, "w": 24, "h": 1 },



     "47": { "x": 0, "y": 26, "w": 12, "h": 5 },



     "48": { "x": 0, "y": 24, "w": 24, "h": 2 },



     "50": { "x": 0, "y": 5, "w": 12, "h": 7 },



     "52": { "x": 12, "y": 13, "w": 12, "h": 11 },



     "56": { "x": 0, "y": 2, "w": 12, "h": 3 },



     "57": { "x": 0, "y": 13, "w": 12, "h": 7 },



     "58": { "x": 12, "y": 0, "w": 12, "h": 5 },



     "60": { "x": 12, "y": 5, "w": 12, "h": 7 },



     "61": { "x": 0, "y": 42, "w": 24, "h": 1 },



     "62": { "x": 0, "y": 31, "w": 24, "h": 1 }



     },



     "importedWithCode": true,



     "settings": {}



     }
     ```

     This dashboard currently does not display costs related to queries, Automation Workflows, and AppEngine Function invocations.
     To view Cost Allocation data for these DPS capabilities, see [Configure user-based Cost Allocation for queries, Automation Workflow, and AppEngine Functions](#user-based).
  2. In Dynatrace, go to the target environment and open ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
  3. Select ![Upload](https://dt-cdn.net/images/upload-8349cb825b.svg "Upload") **Upload** and use the file browser to locate the JSON file that you just saved.
  4. The pre-made dashboard is now visible in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

The costs shown in the demo dashboard are based on manual cost assignments as provided in the DQL query.
They're not automatically cross-checked with your rate card.

#### Use DQL queries

This section provides various DQL queries that you can use to achieve specific use cases.

Fetch all Billing Usage Events in full detail (including Cost Allocation fields)

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"
```

Fetch all Billing Usage Events for all supported host-related capabilities and show only their capability, Host ID, and Cost Allocation fields

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| fieldsKeep event.type, dt.entitiy.host, dt.cost.costcenter, dt.cost.product
```

Check if any Cost Allocation fields are already configured

```
fetch dt.system.events



| filter event.kind == "BILLING_USAGE_EVENT"



| summarize count = count(), by:{event.type,dt.cost.costcenter}
```

### Export Cost Allocation data

If you want to view Cost Allocation data in a separate tool, such as Excel or Power BI, you can export the data.

You can export Cost Allocation data via **Account Management** or the API.

DPS licensing consumption and related costs are based on 15-minute increments.
Reports are generated daily, so you won't be able to see usage accrued in the previous <24 hours.

#### Export Cost Allocation data via Account Management

In Account Management, you can download some or all Cost Allocation data from your current DPS subscription.

1. Go to **Account Management**.
2. Select **License** > **Cost Management** > **Cost Allocation** > **Download cost allocation report**.
3. Select the **Commitment period** for the relevant subscription.
4. Select the timeframe from which data should be exported: enter the appropriate dates for **From** and **To**.
5. Select  **Request download**.
6. An email will be sent to the email account of the logged-in user.
   The email is sent from **noreply@dynatrace.com**, so you might want to check your whitelist to make sure that you can receive emails from this account.
   It contains a download link for the CSV file, which is valid for 24 hours.

#### Export Cost Allocation data via the API

All Cost Allocation data can be retrieved via the API.

Before using the API, you need to generate an Account Management API Token as described in [Authentication for the Account Management API](/docs/manage/account-management/identity-access-management/oauth "Manage authentication and user permissions for the Account Management API.").
Additionally, your user will need the permission **View usage and consumption: account-uac-read**.

Use the following API call to retrieve Cost Allocation data.
Parameters are described in [Dynatrace Platform Subscription API - GET cost allocation](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation "See how Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.").

`GET /v1/subscriptions/{subscription-uuid}/cost-allocation?field={field}\&environment-id={environment-id}`

An example response is provided in the code block below.

```
{



"records": [



{ "date": "2024-04-01", "capability": "FULLSTACK_MONITORING","key": "department-A", "costs": 10, "usage": 2000 },



{ "date": "2024-04-01", "capability": "FULLSTACK_MONITORING","key": "department-B", "costs": 40, "usage": 8000 },



{ "date": "2024-04-01", "capability": "LOGS", "key": "department-A", "costs": 70, "usage": 700 },



{ "date": "2024-04-01", "capability": "LOGS", "key": "department-B", "costs": 20, "usage": 200 },



{ "date": "2024-04-01", "capability": "FULLSTACK_MONITORING", "key": "department-E", "costs": 10, "usage": 2000 },



{ "date": "2024-04-01", "capability": "FULLSTACK_MONITORING", "key": "department-F", "costs": 50, "usage": 10000 },



{ "date": "2024-04-01", "capability": "FULLSTACK_MONITORING", "key": null, "costs": 60, "usage": 12000 },



{ "date": "2024-04-01", "capability": "LOGS", "key": null, "costs": 10, "usage": 100 },



{ "date": "2024-04-02", "capability": "FULLSTACK_MONITORING", "key": "department-A", "costs": 10, "usage": 2000 },



{ "date": "2024-04-02", "capability": "FULLSTACK_MONITORING", "key": "department-B", "costs": 40, "usage": 8000 },



{ "date": "2024-04-02", "capability": "FULLSTACK_MONITORING", "key": "department-C", "costs": 70, "usage": 14000 },



{ "date": "2024-04-02", "capability": "LOGS", "key": null, "costs": 500, "usage": 5000 }



// more daily records



],



"nextPageKey": "...",



"environmentId": "tenant-A",



"field": "COSTCENTER"



}
```

## Troubleshooting

If you can't find Cost Allocation data:

* Make sure you have a Dynatrace Platform Service (DPS) SaaS license.
* Check your OneAgent version.
  Cost Allocation is supported for versions 1.291+.
* Confirm that host tags are in the allow list.

  + Are all tag names correct?
  + Are all tags in ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations** also in the allow list?
  + If any used tags are not in the allow list, add them as described in [Add host tags](#add-host-tags).
    Make sure that they're set on the OneAgent directly (i.e., via the command line), and not in the browser.
* Did you perform a restart?
  When in doubt, restart OneAgent or your Kubernetes pod(s).
  Then wait up to 30 minutes and try again.

## Related topics

* [Account Management](/docs/manage/account-management "Manage your Dynatrace license, subscriptions, and platform adoption and environment health.")
* [Set up Cost Allocation for OneAgent deployments](/docs/ingest-from/dynatrace-oneagent/oneagent-cost-allocation "Learn how to allocate costs from OneAgent to cost centers and products.")
* [Set up Cost Allocation for Kubernetes deployments](/docs/ingest-from/setup-on-k8s/kubernetes-cost-allocation "Learn how to allocate costs from Kubernetes deployments to cost centers and products.")
* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)


---
