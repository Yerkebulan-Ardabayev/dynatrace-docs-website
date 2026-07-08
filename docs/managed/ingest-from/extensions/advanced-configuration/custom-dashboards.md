---
title: Distribute custom dashboards with your extensions
source: https://docs.dynatrace.com/managed/ingest-from/extensions/advanced-configuration/custom-dashboards
---

# Distribute custom dashboards with your extensions

# Distribute custom dashboards with your extensions

* How-to guide
* 3-min read
* Updated on Aug 07, 2025

After your extension starts sending data to Dynatrace, you can create a custom dashboard, export its definition to a JSON file, and add the JSON to your extension archive.

## Dashboards Classic

If you're using [Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic."), follow these procedures.

After your extension starts sending data to Dynatrace, you can [create a custom dashboard](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.") and then export its definition to a JSON file and add it to your extension archive. You can export a dashboard definition through the Dynatrace web UI or Dynatrace API.

### Export dashboard JSON in web UI

1. Go to **Dashboards**.
2. In the row for the dashboard you want to export, select **More** (**…**) > **Export**.  
   A JSON file with the dashboard's name is downloaded to your local machine.
   For more information, see [Edit Dynatrace dashboard JSON](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.").

### Export dashboard JSON using API

1. Go to **Dashboards** and display the dashboard.
2. In the dashboard URL, find the `id` parameter (for example, `id=d996b25e-593c-4213-8ad3-c87319a8830a`) and save the parameter value.
3. Use the [Get a dashboard](/managed/dynatrace-api/configuration-api/dashboards-api/get-dashboard "View a dashboard via the Dynatrace Classic API.") API endpoint to get the dashboard JSON definition.
   Run the following command to get the dashboard definition. For this example, we use the Dynatrace SaaS URL:

   ```
   curl -X GET "https://{env-id}.live.dynatrace.com/api/config/v1/dashboards/{dashboard-id}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token `{api-token}"
   ```

   Replace:

   * `{env-id}` with your [Environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
   * `{api-token}` with an [API token](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").
   * `{dashboard-id}` with the dashboard identifier you determined in the previous step.
4. The call returns the JSON payload containing the dashboard definition. Save it as a JSON file.

### Add your dashboard to the extension package

Add your dashboard JSON file to your extension package and reference it in your extension YAML file.

For the following package structure:

```
extension.zip



│   extension.yaml



│



└───alerts



│   |   alert.json



│



└───dashboards



│   dashboard.json
```

Use the following reference in the top level of your [YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework."):

```
dashboards:



- path: dashboards/dashboard.json



alerts:



- path: alerts/alert.json
```