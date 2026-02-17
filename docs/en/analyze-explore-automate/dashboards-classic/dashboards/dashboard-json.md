---
title: Edit Dynatrace dashboard JSON
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json
scraped: 2026-02-17T05:04:44.644071
---

# Edit Dynatrace dashboard JSON

# Edit Dynatrace dashboard JSON

* How-to guide
* 3-min read
* Published Sep 24, 2020

[Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")

The dashboards discussed here are classic dashboards created using the dashboarding functionality integrated with previous Dynatrace.

* For more about classic dashboards, see [Dashboards Classic](/docs/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.").
* For more about dashboards created with the Dashboards app in the latest Dynatrace, see [Dashboards](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").
* To improve your dashboard experience, you can [upgrade existing dashboards](/docs/analyze-explore-automate/dashboards-classic/dashboards-upgrade-classic-to-latest "Upgrade classic dashboards created in the previous Dynatrace to the Dashboards app in the latest Dynatrace.") from Dashboards Classic to the Dashboards app in the latest Dynatrace.

You can edit the JSON definition of your dashboard offline or, for small changes, edit the JSON directly in Dynatrace.

API alternative

To manage dashboard JSON at scale, you need the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.").

## Edit offline

Use this procedure to download a dashboard's JSON definition, edit it offline, and upload it back to Dynatrace.

When you upload a dashboard using this procedure, you overwrite the dashboard whose definition you originally downloaded. If you want to upload a dashboard definition to a new dashboard, see [Import dashboard](#import-dashboard) below.

1. Display the dashboard.
2. Select **Edit**.
3. Switch to the **Settings** tab and then select **Configure more**.
4. Select **Dashboard JSON**.
5. On the **Dashboard JSON** page, select **Download**.  
   A JSON file with the dashboard's name is downloaded to your local machine.
6. Edit the JSON in your preferred development environment.  
   For JSON syntax details, see the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") Documentation.
7. On the **Dashboard JSON** page, select **Upload**, browse for the edited JSON file, and upload it to Dynatrace.  
   The uploaded JSON is displayed on the **Dashboard JSON** page.
8. Select **Save changes** to replace the old JSON with your edited JSON.
9. Display the dashboard to verify your changes.

## Edit in Dynatrace

1. Display the dashboard.
2. Select **Edit**.
3. Switch to the **Settings** tab and then select **Configure more**.
4. Select **Dashboard JSON**.
5. On the **Dashboard JSON** page, the dashboard JSON is displayed in an edit window.
6. Click in the displayed JSON and start editing.

   * You can work directly in the edit window or copy and paste back and forth from another editor.
   * The **You have unsaved changes** message in the lower left of the page will remind you that you have work in progress. Be sure to save before you navigate away from the page.
   * Syntax is checked each time you save. You can work incrementally and use **Save changes** to verify that it still parses.
   * For JSON syntax details, see the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") Documentation.
7. When you are finished, display the dashboard to verify your changes.

## Import dashboard

Use this procedure to import a dashboard definition as a new dashboard.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Export the dashboard**](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json#step-1 "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Edit the dashboard JSON file**](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json#step-2 "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Import the dashboard**](/docs/analyze-explore-automate/dashboards-classic/dashboards/dashboard-json#step-3 "Learn how to export, edit, and import the JSON for a Dynatrace dashboard.")

When you import a dashboard using this procedure, you add a new dashboard to Dynatrace. If you want to overwrite an existing dashboard, see [Edit offline](#edit-offline) above.

### Step 1 Export the dashboard

If you want to start from an existing dashboard definition

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. In the table of dashboards, select **More** (**â¦**) > **Export** for the dashboard you want to export.  
   The dashboard definition is exported as a JSON file to your computer.

### Step 2 Edit the dashboard JSON file

Edit the dashboard JSON in your preferred development environment. For JSON syntax details, see the [Dashboards API](/docs/dynatrace-api/configuration-api/dashboards-api "Find out how to manage dashboard configuration via Dynatrace Classic configuration API.") Documentation.

### Step 3 Import the dashboard

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic**.
2. Select **Import dashboard**.
3. Select the JSON file for the dashboard you want to import.  
   The imported dashboard opens in edit mode.