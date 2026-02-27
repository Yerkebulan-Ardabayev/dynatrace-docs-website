---
title: Log events (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events
scraped: 2026-02-27T21:18:33.293795
---

# Log events (Logs Classic)

# Log events (Logs Classic)

* Tutorial
* 5-min read
* Updated on Oct 08, 2025

Log Monitoring Classic

Dynatrace Log Monitoring gives you the ability to create log events based on log data and use them in problem detection.

Log event pricing is based on the Davis data units (DDUs) model. Check [DDUs for custom Davis events](/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.") to find out how you can estimate and track DDU consumption for log events.

When Dynatrace ingests log data, it applies the query specified in the log event definition. Every matched occurrence triggers a log event that can be configured to individually create a problem for each triggered log event or can be merged into one problem.

## Create a log event

1. Go to **Settings** > **Log Monitoring** > **Events extraction** and select **Add log event**.
2. Enter the **Summary**.  
   The summary acts as the display name of the log event configuration. The summary must be unique for all configurations.
3. Enter the **Matcher**.  
   Enter the Log Monitoring query to filter the log data for your log event. For details, see [Log viewer](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer#query-syntax "Learn how to use Dynatrace log viewer to analyze log data.").

   I switched to Grail

   If you switched to [Dynatrace Grail](/docs/platform/grail/dynatrace-grail "Grail is the Dynatrace data lakehouse that's designed explicitly for observability and security data and acts as single unified storage for logs, metrics, traces, events, and more."), you may begin using the [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") functions in your Log Monitoring queries. For details, see [Log processing with classic pipeline](/docs/analyze-explore-automate/logs/lma-classic-log-processing#dql-functions "Utilize log processing rules to reshape incoming log data for better understanding, analysis, or further transformation.").
4. Configure the **Event template**.

   * Provide the **Title** of the event to trigger. If this log event triggers a problem, this title will also be the title of the problem.
   * Provide the **Description** of the event. Note that you can have one or more placeholders in the description (see [Placeholders](#placeholders) below for details).
   * Select the **Event Type**. Event types indicate the severity of the event. See [Settings API - Log events schema table](/docs/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events "View builtin:logmonitoring.log-events settings schema table of your monitoring environment via the Dynatrace API.").
5. Choose whether to **Allow merge**.  
   If two or more events are triggered, Dynatrace could merge these events into a single problem. This option lets you choose to disable this behavior, which can result in more reported problems.

   The `dt.event.allow_davis_merge` property does **not** split problems for the same log event configuration. It only prevents merging with problems from other log event configurations or other problem domains (such as custom alerts).  
   If you want to split problems for the same log event configuration, the `event.unique_identifier` property must be **present in the actual log data**. You can then use a placeholder in your log event configuration to reference this property.  
   For example, to create a separate problem for each log line message, use `event.unique_identifier={content}`.
6. Add **Properties**.
   A property is a key/value pair that is set on every triggered event. You can have one or more placeholders as a value that will be extracted from the log data. For example, a property with **Key** set to `PGI` and a **Value** of placeholder `{dt.entity.process_group_instance}` will extract the process group instance value from log data once the event is triggered. If the placeholder substitution fails, both the key and the value will not be available.  
   To see how to get the full list of properties, go to [Events API v2 - GET all event properties](/docs/dynatrace-api/environment-api/events-v2/get-event-properties "List all event properties via the Dynatrace API."). The `description` field in the API response body explains how each property works. For [example](/docs/dynatrace-api/environment-api/events-v2/get-event-properties#exampledesc "List all event properties via the Dynatrace API."): In the `dt.event.allow_davis_merge`, the description says :`"Allow Davis AI to merge this event into existing problems (true) or force creating a new problem (false)"`.

### Set a timeout for a log event

Log events have a default timeout of 15 minutes. The timeout defines how frequently the event source must refresh the log event to keep it active. The maximum time allowed for a log event is six hours.

* A log event is kept active if the event source sends a refresh before the event times out (default: `15` minutes).
* An event automatically closes if no refresh is sent within the timeout period.
* You can customize the timeout.

To set a custom timeout

1. When you create or edit a log event, select **Add property**.
2. Set **Key** to `dt.event.timeout`.
3. Set **Value** to the number of minutes (for example, `12`).

To verify that a custom timeout was added for an event triggered on the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select the host name.
2. Scroll down to **Events** and expand **Details** for the event.

### Placeholders

Placeholders are log entry attributes that can be used to extract the actual value from the log data.

* You can use any attribute listed in the log viewer for a given log entry as a placeholder to extract that attribute value.
* You can use additional log entry attributes in the log viewer as placeholders for the values they represent in the log data. Enclose placeholder values in brackets (for example, `{dt.process.name}`).

Log viewer showing additional log entry attributes

![Additional event attributes in log viewer.](https://dt-cdn.net/images/screenshot-log-viewer-attributes-903-2a2d4d157f.png)

## Example

In this example, we create a log event based on ingested log data. This log event will be triggered when the ingested log entry matches the input from the **Matcher** field. The matcher will search for status `error` on the `555f5555-555a-5dd5-55f555a5b55d` host. We add log event properties (attributes) that will extract values from the log data and include it in the problem summary.

1. Go to **Settings** > **Log Monitoring** > **Events extraction** and select **Add log event**.
2. Set the following:

   * **Summary:** `syslog-agent log event`
   * **Matcher:** `status="error" AND host.name="555f5555-555a-5dd5-55f555a5b55d"`
   * **Event template** - **Title:** `[Log] log events demo`
   * **Event template** - **Description:** `{content}`
   * **Event template** - **Event type:** `Custom alert`
3. Turn off **Allow merge**.
4. For **Properties**, add the following two properties:

   * Key `K8 Id` with value `{dt.kubernetes.config.id}`
   * Key `Process Name` with value `The process name is -> {dt.process.name}`
5. Save your changes and wait for log data to be ingested.

Log events example page

![Settings screen for configuring log events.](https://dt-cdn.net/images/screenshot-log-events-settings-641-583e83f210.png)

Logs can have attributes with long values, up to 32kB. Such attribute can be added as part of the **Event template** section. In such case, the events are created, but those values are trimmed to 4096.

If a match is found, this log event will create a problem with each triggered log event.

![Problem created by defined log events.](https://dt-cdn.net/images/screenshot-log-events-problem-845-dc714350b6.png)

The problem created as a result of a triggered log event will contain the information mapped from your log event configuration. The problem title is the **Event title** and the impact section reflects your **Event type** settings and additional information you configured in the description and properties of the log event.

Note that, in this example, while we have configured two properties (`K8 Id` and `Process Name`), only one appears on the problem page. This is because only the `{dt.process.name}` placeholder had a value in the ingested log data. The `{dt.kubernetes.config.id}` value was not found in that particular log entry and the defined property was ignored.