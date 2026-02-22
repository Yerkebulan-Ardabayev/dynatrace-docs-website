---
title: Distribute custom dashboards with your extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/custom-dashboards
scraped: 2026-02-22T21:27:09.343443
---

# Distribute custom dashboards with your extensions

# Distribute custom dashboards with your extensions

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Aug 07, 2025

After your extension starts sending data to Dynatrace, you can create a custom dashboard, export its definition to a JSON file, and add the JSON to your extension archive.

## Dashboards **Dashboards**

If you're using [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."), follow these procedures.

You can export a dashboard definition through the Dynatrace web UI.

### Export dashboard JSON

To download (export) a dashboard from the ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** side panel

1. Go to ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.
2. In **Last opened by you**, hover over the name of the dashboard you want to export and select  **Download** from the  menu. The dashboard is downloaded to a local JSON file that you can upload.

   If your dashboard isn't listed in **Last opened by you**, select  **All dashboards** to display a table of all dashboards that you can access (your dashboards or dashboards shared with you). From there, you can find the dashboard and select  **Download** from the  menu.

To download (export) the currently displayed dashboard as JSON

1. At the top of the dashboard, open the  menu to the right of the dashboard name.
2. Select  **Download** from the menu.

   The definition of the current dashboard is downloaded to a local JSON file.

### Add your dashboard to the extension package

After you create a dashboard that uses your extension data, and you export the dashboard JSON as described earlier, you can add the dashboard to your extension package.

1. Rename the dashboard JSON file to match the pattern `<string>.dashboard.json`. For example, `device-health.dashboard.json`.
2. Add the JSON to the [extension package](/docs/ingest-from/extensions/concepts#package "Learn more about the concept of Dynatrace Extensions.").

   For example,

   ```
   extension.zip



   â   extension.yaml



   â



   ââââdocuments



   â   device-health.dashboard.json
   ```
3. Declare the JSON in the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

   For example,

   ```
   documents:



   dashboards:



   - displayName: "My Dashboard"



   path: "documents/device-health.dashboard.json"
   ```
4. Upload the extension to the Dynatrace environment.

   Your dashboard is now available in ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

You can also access the dashboard from ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**.

1. Go to ![Extensions](https://dt-cdn.net/images/dynatrace-extensions-256-9cb05e0f55.png "Extensions") **Extensions**.
2. Select your extension.
3. On the **Configure** tab, select **Extension content**.

   * Your dashboard is listed as type `DOCUMENT_DASHBOARD`.
   * You can set **Filter By Type** to `DOCUMENT_DASHBOARD` to list only dashboards.

## Dashboards Classic

If you're using [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic."), follow these procedures.

After your extension starts sending data to Dynatrace, you can [create a custom dashboard](/docs/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.") and then export its definition to a JSON file and add it to your extension archive. You can export a dashboard definition through the Dynatrace web UI or Dynatrace API.

### Export dashboard JSON in web UI

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. In the row for the dashboard you want to export, select **More** (**â¦**) > **Export**.  
   A JSON file with the dashboard's name is downloaded to your local machine.
   For more information, see [Edit Dynatrace dashboard JSON](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.").

### Export dashboard JSON using API

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and display the dashboard.
2. In the dashboard URL, find the `id` parameter (for example, `id=d996b25e-593c-4213-8ad3-c87319a8830a`) and save the parameter value.
3. Use the [Get a dashboard](/docs/dynatrace-api/configuration-api/dashboards-api/get-dashboard "View a dashboard via the Dynatrace Classic API.") API endpoint to get the dashboard JSON definition.
   Run the following command to get the dashboard definition. For this example, we use the Dynatrace SaaS URL:

   ```
   curl -X GET "https://{env-id}.live.dynatrace.com/api/config/v1/dashboards/{dashboard-id}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token `{api-token}"
   ```

   Replace:

   * `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](/docs/ingest-from/extensions/manage-extensions#permissions "Learn how to manage extensions.").
   * `{dashboard-id}` with the dashboard identifier you determined in the previous step.
4. The call returns the JSON payload containing the dashboard definition. Save it as a JSON file.

### Add your dashboard to the extension package

Add your dashboard JSON file to your extension package and reference it in your extension YAML file.

For the following package structure:

```
extension.zip



â   extension.yaml



â



ââââalerts



â   |   alert.json



â



ââââdashboards



â   dashboard.json
```

Use the following reference in the top level of your [YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework."):

```
dashboards:



- path: dashboards/dashboard.json



alerts:



- path: alerts/alert.json
```