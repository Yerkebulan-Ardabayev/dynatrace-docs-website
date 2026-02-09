---
title: "Configure an advanced custom alert"
source: https://docs.dynatrace.com/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/configure-an-advanced-ad
updated: 2026-02-09
---

# Configure an advanced custom alert

# Configure an advanced custom alert

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Jan 28, 2026

![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** allows you to create custom alerts, set up customized alerts, and transform metric events configuration. You can also save time and create a custom alert in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** while using the app.

## Prerequisites

To use the latest version of ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**, you need to have appropriate permissions. For more information, see [![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** overview](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.").

## Create or edit an advanced custom alert

To manually create an advanced custom alert configuration

1. Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Create your own custom alert** to create a new alert. To edit an existing custom alert, select any custom alert from the list.
3. Go to the **Advanced** tab and expand **Set scope**.
4. Optional In **Segments**, choose one or more segments you want to filter by.
5. In **Query**, provide the [DQL query](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") to fetch your data.

   We recommend that you use the `interval: 1m` parameter to ensure proper data resolution for the analysis.
6. Set **Actor** to a service user or regular user.

   By default, after editing the custom alert's configuration, the actor changes to the user who updated it. You will get a warning message confirming whether you want to overwrite the existing configuration or make a copy of the custom alert with your changes.

   If the custom alert was created with a service user and you have permission to use the service user, you can update the configuration without overwriting the service user actor; otherwise, you'll get a warning about restricted service user access.
7. Expand **Define alert condition**.
8. In **Select use case**, select the analyzer.
9. In **Set a condition**, set the analyzer parameters. For details, see [Analyzer type and parameters](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#analyzer "How to set up an alert for missing measurements.").
10. Optional Select **Preview** to see a demonstration of your alert condition.
11. Expand **Add details**.
12. In **General information**, set a **Title** and **Description** for your custom alert. You can use Markdown in your custom alert description.
13. In **Create event template**, configure the event triggered by the configuration. For details, see [Event template](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#event-template "How to set up an alert for missing measurements.").
14. Select **Create** to create a simple custom alert or select **Save** to update your configuration.

Whenever you **Create** or **Save** your custom alert, its configuration gets automatically validated. If the there's no errors present in your configuration, you'll be able to save or update your configuration. If there are any errors, the section will be highlighted with red and marked with `Error` message under the section title.

Check the **Status** of the new configuration shortly after creation to ensure there are no errors in the execution.

## Create an advanced custom alert in Notebooks

With Dynatrace Intelligence for Notebooks, you can preview your custom alert configuration and evaluate its effectiveness. This option takes you to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, where you configure the query and monitoring strategy, and then back to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection** to create an event template.

1. Go to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
2. Select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **New alert** > **Open a custom alert in Notebooks**.
3. Select a notebook in which you want to preview your configuration.  
   This action takes you to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**.
4. Add a new **DQL** or **Metrics** section and query the data you're interested in.

   For a DQL query, we recommend that you use the `interval: 1m` parameter to ensure proper data resolution for the analysis.
5. Optional Select , then select one or multiple segments you want to filter by.
6. Select **Options** > **Analyze and alert**.
7. Activate the analyzer.
8. Select the required analyzer and configure it. For details, see [Anomaly detection configuration](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration "How to set up an alert for missing measurements.").
9. Select **Run analysis**.
10. Once you're satisfied with the result, select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") > ![Open with](https://dt-cdn.net/images/open-with-003fc82dcd.svg "Open with") **Open with** and select **Anomaly Detection**.  
    This action takes you back to ![Anomaly Detection - new](https://dt-cdn.net/images/davis-anomalydetection-256-105da91594.png "Anomaly Detection - new") **Anomaly Detection**.
11. Go to the **Advanced** tab and expand **Add details**.
12. In **General information**, set a **Title** and **Description** for your custom alert. You can use Markdown for the description.
13. In **Create event template**, configure the event triggered by the configuration. For details, see [Event template](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-configuration#event-template "How to set up an alert for missing measurements.").
14. Select **Create**.

    Check the **Status** of the new configuration shortly after creation to ensure there are no errors in the execution.

## Related topics

* [Anomaly Detection app](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app "Explore anomaly detection configurations using the Anomaly Detection app.")
* [Anomaly Detection status types](/docs/dynatrace-intelligence/anomaly-detection/anomaly-detection-app/anomaly-detection-status-types "An explanation of Anomaly Detection status types")
* [[Video] Elevating Security with Anomaly Detectionï»¿](https://www.youtube.com/watch?v=WDZUus-VxCE)
* [[Video] Anomaly Detection and Data Observabilityï»¿](https://www.youtube.com/watch?v=HPQi63mQg3w)
