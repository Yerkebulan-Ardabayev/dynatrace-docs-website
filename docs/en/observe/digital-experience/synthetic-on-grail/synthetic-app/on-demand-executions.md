---
title: On-demand monitor executions
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/on-demand-executions
scraped: 2026-03-01T21:10:13.285484
---

# On-demand monitor executions

# On-demand monitor executions

* Latest Dynatrace
* How-to guide
* 15-min read
* Updated on Jun 23, 2025

To trigger an execution via the web UI

1. In the upper-right corner of the monitor's details page, select **On-demand execution**.
2. From the **Locations** list, select the locations for which you want to trigger on-demand execution.

   Note that you can select a combination of **Assigned locations** and **Unassigned public locations** for this execution.
3. Select a **Processing mode**âthis applies to all selected locations for this execution.

   * **Standard** (default)âthe executions contribute to problem detection and availability and performance statistics. You can access execution results when you [**Analyze executions**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/browser-monitors-results-reporting#analyze-executions "Learn about the Browser details page for Browser monitors.").
   * **Disable problem detection**âthe executions contribute to availability and performance statistics but not to problem detection. You can view execution results when you [**Analyze executions**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/browser-monitors-results-reporting#analyze-executions "Learn about the Browser details page for Browser monitors.").
   * **Execution details only**âthe executions do not contribute to availability and performance statistics or to problem detection. You can still access results when you [**Analyze executions**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/browser-monitors-results-reporting#analyze-executions "Learn about the Browser details page for Browser monitors.").

   Note that for all processing modes, executions are visible in the list of on-demand executions in the web UI and retrieved via the [on-demand executions API](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions#api "Execute synthetic monitors on demand from public or private locations").
4. **Fail on performance threshold violation**âby default, on-demand executions fail when they violate a performance threshold, given that their main purpose is to validate new software versions in your CI/CD pipeline. However, you can disable this setting so that on-demand executions behave like regularly scheduled executions (performance threshold violation does not cause this execution to fail but contributes to triggering the performance problem.).
5. **Trigger screenshot** (for browser monitors only)âfor a successful execution, the system takes a screenshot. To see the screenshot, go to [**Analyze executions**](/docs/observe/digital-experience/synthetic-on-grail/synthetic-app/browser-monitors-results-reporting#analyze-executions "Learn about the Browser details page for Browser monitors.").

   **SSL issue handling** (for HTTP monitors only)âfail the monitor if one or more of its requests encounters an expired, missing, or expiring SSL certificate.
6. Select  **Trigger now**âsee a summary dialog listing the execution locations; the execution list displays new entries for the triggered executions. The **Execution stage** initially is `Triggered`.

   Any change you make to monitor script (configuration) is immediately available for on-demand executions on public or private locations.

   Note that executions might not all begin at the same time from different locationsâexecutions might take longer to begin from public locations than from private locations. See additional information on [throttling](#throttling) below.

#### Throttling and limits

* There is a mandatory gap per user of 60 seconds between consecutive on-demand executions of a monitor from the same location (whether triggered via the web UI or API).

  Examples of throttling

  All these examples assume execution from the same location.

  + User A triggers a monitor via API within 60 seconds of triggering the same monitor via UIâthrottled.
  + User B triggers a monitor via API within 60 seconds of user A triggering the same monitor via UIâno throttling.
  + User B triggers a monitor via UI within 60 seconds of user A triggering the same monitor via UIâno throttling.
  + User B triggers a monitor via API within 60 seconds of user A triggering the same monitor via APIâno throttling.
* When triggering multiple on-demand executions via the [API](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions#api "Execute synthetic monitors on demand from public or private locations"), there is a limit of 100 executions per batch.
* + There's a limit of 5,000 on-demand executions per minute for a Dynatrace environment.
* You can define up to 64 key-value pairs of metadata per batch, where keys and values can each be up to 1,024 characters.

#### Failure to be triggered

On-demand executions might not be successfully triggered for various reasons, for example, when a monitor is disabled, a location is down, or when throttling is in effect for a monitor on a given location.

Additional reasons that on-demand executions might not be successfully triggered via the [API](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions#api "Execute synthetic monitors on demand from public or private locations"): monitor deletion, incorrect specification of monitor or location IDs, incorrect specification of related service or application IDs, location deletion, problems with the public Synthetic infrastructure, or problems with your Dynatrace monitoring environment.

If an execution can't be successfully triggered via the web UI, the reasons are shown in the **Triggering status summary** after you select  **Trigger now**. The **Execution stage** in the execution list is `Not triggered`. Details of executions not triggered via the [API](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions#api "Execute synthetic monitors on demand from public or private locations") are returned in the `triggeringProblemsCount` and `triggeringProblemsDetails` response parameters for the POST request.

Executions that can't be triggered are different from executions that are triggered but can't be executed. For details, see the [API](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions#api "Execute synthetic monitors on demand from public or private locations") section.

#### List of executions

The list of executions shows all on-demand executions (triggered by any user via the web UI or API) for a given monitor within the selected time frame.

You need the DPS license to see the list of executions.

* **Execution ID** is a unique ID assigned to each execution; if you trigger executions from all locations, each location's execution has a different ID.
* **Triggered** shows the start time of the execution in the logged-in user's time zone.
* **Source** shows whether the execution was triggered via the web `UI` or the `API`.
* **User** is the Dynatrace user ID of the user who triggered the execution.
* **Location** is the name of the public or private location from which the monitor was executed.
* **Execution stage** identifies the different stages of the on-demand execution. The initial value is `Triggered` or `Not triggered`. When execution is complete, the value changes to `Executed`. Basic results such as duration and status code are available at this stage. The progress spinner continues to be displayed at the `Executed` stage until detailed results are available and the value changes to `Data retrieved`. If multiple sequential executions are triggered per location, the first execution is marked `Triggered`; the remaining executions are marked `Waiting`.
* **Result** indicates whether the execution was a `Success` or `Failure` (with an accompanying **Failure reason**).
* To view execution details, select the expand icon  in the first column.