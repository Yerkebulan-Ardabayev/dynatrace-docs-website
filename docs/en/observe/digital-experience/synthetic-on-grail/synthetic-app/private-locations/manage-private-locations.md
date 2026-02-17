---
title: Manage private locations
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/private-locations/manage-private-locations
scraped: 2026-02-17T05:04:43.059388
---

# Manage private locations

# Manage private locations

* Latest Dynatrace
* How-to guide
* Updated on Dec 12, 2025

To view and manage private locations, go to the **Private locations** tab in ![Synthetic](https://dt-cdn.net/images/synthetic-new-256-1ddb35ac79.png "Synthetic") **Synthetic**.

## Health status

In the **Health status** column of the **Private Synthetic locations** list, you can see ActiveGates health status for each private location in your environment. The column has three sub-columns:

* **Health alerts**âthe alerts display reasons behind ActiveGates health issues. The alerts are also highlighted with colored indicators depending on issues severity:

  + Yellow:

    - Capacityâthe capacity usage of a least one monitor type is more than 80%.
    - No redundancyâthere is only one ActiveGate assigned to the location. No backup in case the ActiveGate is down.
    - Compatibilityâat least one ActiveGate doesn't support at least one monitor type assigned to the location. For details, point to the  (**Warning**) in the **Assigned monitors** column.
  + Red:

    - Capacityâthe capacity usage of at least one monitor type is greater than 90%.
    - Offline AGâat least one ActiveGate is down.
    - Offline locationâthe private location is down. It happens when no ActiveGates are assigned to the private location.
    - Discardedâthere is at least one discarded monitor execution in the last 30 minutes.
* **ActiveGates**ânumber of ActiveGates assigned to a location by their health status. Health status is indicated by one of the following colors:

  + Greenâno ActiveGates with issues.
  + Yellowâone or more ActiveGates experience issues that are still not serious but might require attention.
  + Redâone or more ActiveGates experience serious issues that require immediate attention.
* **Assigned monitors**âthe type and number of Synthetic monitors assigned to the location. The number of HTTP monitors also includes HTTP High Resource monitors.

![ActiveGates health status](https://dt-cdn.net/images/screenshot-2025-12-08-163344-1471-088b434222.png)

## See location details and edit location

Select a location to see its details and edit it. For classic locations, you can see ActiveGates assigned to the locations. They are listed and displayed in red when a Synthetic engine or an ActiveGate itself is offline; the **Status** column shows a corresponding message.

You can see the **ActiveGate ID** in the column that is hidden by default. To display it, select the columns  icon > **ActiveGate ID** > **Apply**.

You can add or delete ActiveGates from the location details page. You can also make other changes and select **Save** to save them.

### Diagnostics

The **Diagnostics** card displays the health status for each monitor type.

* **Capacity usage**âthe capacity usage for a monitor type. If the capacity usage is less than 80%, `OK` is displayed in the column, and if there is no data, `0` is displayed.
* **Compatibility**âthe number of ActiveGates that support a monitor type. For example, if there are three ActiveGates assigned to the location, but only two of them support the monitor type, you will see `2/3`.
* **Monitors**âthe number of monitors by type assigned to the location.
* **Executions/hour**âthe number of executions per hour for a monitor type.
* **ActiveGates**âthe number of ActiveGates assigned to the location. This also includes the number of those ActiveGates that are offline. For example, if there are three ActiveGates assigned to the location, but one of them is offline, you will see `1/3`.

For **Capacity usage**, **Compatibility**, and **ActiveGates**, the health status is additionally indicated by one of the following colors:

* Greenâno issues.
* Yellowâthere are issues that are not yet serious but might require attention.
* Redâthere are serious issues that require immediate attention.

### Metrics for health status

Metrics for the health status of each monitor type are available for charting and alerting. Metrics for charting and alerting on the health status of each monitor type are available in [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace."). For example, you can choose the following metrics for charting and alerting:

* Synthetic - HTTP - Engine Utilization
* Synthetic - HTTP High Resource - Engine Utilization
* Synthetic - Browser - Engine Utilization

We strongly recommend splitting these metrics by location to get an accurate view of location health.

![Metric_for_private_location](https://dt-cdn.net/images/screenshot-2025-07-02-201338-1377-bb0711152b.png)

## Location outage handling

For each location, enable the corresponding switches to generate problems when a location or any of its ActiveGate engines are unavailable. The following switches are currently available:

* You can generate a problem when the entire private location is unavailable (all ActiveGates are offline), or if the location lacks the capability required for the monitor type to be executed.
* You can generate a problem when a single ActiveGate at this location is offline.

For example, suppose your location has two ActiveGates, and you enable both problem switches. You will see three problems when your location is unavailableâone for the entire location and one for each ActiveGate that's offline.

Containerized locations

For containerized locations, you can only generate a problem when the entire private location is unavailable (all ActiveGates are offline), or if the location lacks the capability required for the monitor type to be executed.