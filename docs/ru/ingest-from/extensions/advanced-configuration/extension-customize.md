---
title: Customize data with extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/advanced-configuration/extension-customize
scraped: 2026-03-01T21:25:04.282922
---

# Customize data with extensions

# Customize data with extensions

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Oct 28, 2025

You can tailor various aspects of Dynatrace to the specifics of data acquired by your extension. You can also use the extension to introduce a new configuration in your environment (for example, organize data in dashboards, create new alerts, or introduce complex metrics).

## Custom Dynatrace UI

The Extensions 2.0 framework enables you to tailor the Dynatrace UI for the specific needs of the data ingested by your extension. You can add customized dashboards or specialized unified analysis pages to your extension.

For more information, see [Extend Dynatrace with domain-specific web UI](/docs/ingest-from/extend-dynatrace/extend-ui "Extend the Dynatrace web UI using entity-tailored unified analysis pages.").

## Custom metric events

You can create custom metric events based on the metrics extracted by your extension and add the exported definitions to your extension archive. This way, you can distribute the custom metric events among Dynatrace environments.

Export custom event for alerting definition

1. Go to **Settings** > **Anomaly detection** > **Metric events**.
2. Expand the event of your choice.
3. Scroll to the bottom of the definition where you'll find the `Config id` parameter (for example, `id=1be8d58d-71a7-4566-9058-754d635363ab`) and save the parameter value.
4. Run the following command to get the definition of the custom metric event. For this example, we use the Dynatrace SaaS URL:

   ```
   curl -X GET "https://{env-id}.live.dynatrace.com/api/config/v1/anomalyDetection/metricEvents/{custom-event-id}" \



   -H "accept: application/json; charset=utf-8" \



   -H "Authorization: Api-Token `{api-token}"
   ```

   Replace:

   * `{env-id}` with your [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * `{api-token}` with an [API token](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") that has the required [permissions](/docs/ingest-from/extensions/manage-extensions#permissions "Learn how to manage extensions.").
   * `{custom-event-id}` with the custom metric event identifier you determined in the previous step.
5. The call returns the JSON payload containing a custom metric event definition. Save it as a JSON file.
6. Declare the exported JSON files in your `extension.yaml` file and add them to your extension package.

For more information, see [Extensions 2.0 hands-on excercise](/docs/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial "Learn about WMI extensions in the Extensions framework.").

After you upload or update an extension containing custom metric events, make sure you enable the events you'd like to use. The extension-imported events are disabled by default after each upload and activation, inluding an update. To enable metric events, go to **Settings** > **Anomaly detection** > **Metric events**.

## Custom topology

After you start to send in your own data via an extension, you might be interested in extending the built-in topology model by adding your own domain-related entity types and relationships.

For more information, see [Custom topology model](/docs/ingest-from/extend-dynatrace/extend-topology "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to.").

## Custom metric metadata

To add more context to data points and their dimensions ingested by your extension, your custom metric can carry additional useful information, such as the unit of measurement, display name, and value ranges.

You can provide such information via custom metric metadata. Metadata is stored independently from data points and tied together by the metric key. You can push data points and set metadata in any order.

For more information, see [Custom metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.").

### Data filtering

Extensions also allow you to filter data based on specific criteria. This filtering capability is particularly useful for SNMP extensions, where you might want to limit the data that is ingested by the extension

Filters match entity names to include/exclude certain configurations from monitoring. This makes the data more relevant and saves unnecessary license consumption. Filters work with a specific entity type and support the following syntax:

| Expression | Description |
| --- | --- |
| `$eq(<str>)` | Checks if `<str>` matches what you're filtering |
| `$prefix(...)` | Begins with â¦ |
| `$suffix(...)` | Ends with â¦ |
| `$contains(...)` | Contains â¦ |
| `$and(<expr1>, <expr2>)` | Chains two or more of the above expressions with the AND operator |
| `$or(<expr1>, <expr2>)` | Chains two or more of the above expressions with the OR operator |
| `$not(<expr>)` | Negates an expression. For example, to exclude all Pools from the Common partition, you can add the `$not($prefix(/Common/))` filter. |

## Custom process group detection rules

Dynatrace detects which processes are part of the same [process groups](/docs/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring.") by means of a default set of detection rules. However, you can add your own process detection rules suited to the data retrieved by your extension.

For more information, see [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection").

## Custom security context attribute

You can add a security context attribute to Dynatrace-provided and custom extensions. You can do this as part of the extension's activation, individually per each configuration, or you can edit the settings later.

You need to have a monitoring configuration for the selected extension. For more details on setting up a monitoring configuration via API, see [Extensions 2.0 API - POST a monitoring configuration](/docs/dynatrace-api/environment-api/extensions-20/monitoring-configurations/post-monitoring-configuration "Create a monitoring configuration of an extension via the Dynatrace Extensions 2.0 API.").

You can add security context from the **Monitoring configurations** tab of the chosen extension by selecting **Edit** from the **Actions** column. Then, select **Next** to go to the **Attributes** page.

The attribute is applied to all metrics, logs, and events produced by the configuration.

An API can also be used to set up a security context. For details, see [Monitored entities API - security context](/docs/dynatrace-api/environment-api/entity-v2/security-context "Create or delete security context via Dynatrace API.").

To avoid vulnerabilities, such as unauthorized access or data leakage, configure the security context for extensions according to our [recommended practices](/docs/manage/identity-access-management/use-cases/access-security-context "Grant access to entities with security context").

## Custom cost center and cost product attributes

You can add a cost center and a cost product attribute to Dynatrace-provided and custom extensions. You can do this as part of the extension's activation, individually per each configuration, or you can edit the settings later.

The fields are based on the following attributes:

* `dt.cost.costcenter` assigns usage to a specific cost center.
* `dt.cost.product` assigns usage to a product or application ID.

To learn more about the field syntax, see [Global field reference](/docs/semantic-dictionary/fields#dynatrace "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.").

To add cost center and cost product attributes to your extension, you need to have a monitoring configuration for the selected extension. For more details on setting up a monitoring configuration via API, see [Extensions 2.0 API - POST a monitoring configuration](/docs/dynatrace-api/environment-api/extensions-20/monitoring-configurations/post-monitoring-configuration "Create a monitoring configuration of an extension via the Dynatrace Extensions 2.0 API.").

You can add security context from the **Monitoring configurations** tab of the chosen extension by selecting **Edit** from the **Actions** column. Then, select **Next** to go to the **Attributes** page.

The attributes are applied to all metrics, logs, and events produced by the configuration.

## Log metrics, events, and processing rules



After you enable [log ingestion](/docs/analyze-explore-automate/logs "Log Management and Analytics provides a unified approach to controlling and studying your log data in Dynatrace.") into Dynatrace you can define the log metrics, events, and add your own log processing rules to be shipped with your extension.

For general information, on your logs configuration, see

* [Log events](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-events "Create log events based on log data and use them in problem detection.")
* [Log metrics](/docs/analyze-explore-automate/logs/lma-log-processing/lma-log-metrics "Create metrics based on log data and use them throughout Dynatrace like any other metric.")
* [Log processing](/docs/analyze-explore-automate/logs/lma-log-processing "Use Dynatrace powered by Grail and DQL to reshape incoming log data for better understanding, analysis, or further processing.")

The Extensions YAML file supports the same fields as the Settings 2.0 schemas:

* [Log metrics](/docs/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-schemaless-log-metric "View builtin:logmonitoring.schemaless-log-metric settings schema table of your monitoring environment via the Dynatrace API.")
* [Log events](/docs/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-events "View builtin:logmonitoring.log-events settings schema table of your monitoring environment via the Dynatrace API.")
* [Processing](/docs/dynatrace-api/environment-api/settings/schemas/builtin-logmonitoring-log-dpp-rules "View builtin:logmonitoring.log-dpp-rules settings schema table of your monitoring environment via the Dynatrace API.")

You define your custom log configuration in the Extensions YAML file, starting with the following nodes in the root of the file

* `logMetrics`
* `logEvents`
* `logProcessingRules`

To learn the structure of the definition, check the Extensions schemas:

* `log.events.schema.json`
* `log.metrics.schema.json`
* `log.processing.rule.schema.dql.json`
* `log.processing.rule.schema.json`
* `log.processing.rule.schema.lql.json`

See [Extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml#schemas "Learn how to create an extension YAML file using the Extensions framework.") to learn how to get the schema JSON files.

Check the examples below on how to define your log metrics, events, and processing rules in the extension YAML file.

Log metrics

```
name: custom:dynatrace.logmetric.test.extension



version: 1.0.0



minDynatraceVersion: "1.281.0"



author:



name: "John Doe"



logMetrics:



- key: log.test.extension.occurrence



query: content="AllProcessed"



enabled: true



measure: OCCURRENCE



- key: log.test.extension.attribute



query: content="AllProcessed"



enabled: true



measure: ATTRIBUTE



measureAttribute: dt.os.type



- key: log.test.extension.dimensions



query: content="AllProcessed"



enabled: true



measure: OCCURRENCE



dimensions: [



dimension1,



dimension2



]
```

Log events

```
ame: custom:dynatrace.logevent.test.extension2



version: 1.0.0



minDynatraceVersion: "1.281.0"



author:



name: "John Doe"



logEvents:



- query: content="a"



enabled: true



summary: abc



eventTemplate:



title: log_event_a



description: ''



eventType: CUSTOM_ALERT



davisMerge: false



- query: content="a"



enabled: true



summary: abd



eventTemplate:



title: abd



description: My custom log event description :)



eventType: CUSTOM_ALERT



davisMerge: false
```

Log processing rule

With this definition, you use the `RAPLACE_PATTERN` to mask sensitive data retrieved using the SQL data source.

```
logProcessingRules:



- ruleName: TopN statements masking



query: event.group="query_performance"



enabled: true



ProcessorDefinition:



rule: |



USING(INOUT content) | FIELDS_ADD(content: REPLACE_PATTERN(content, "(\"'\"):p1 (LD):p2 (\"'\"):p3", "${p1}${p2|sha1}${p3}"))



RuleTesting:



sampleLog: |



{



"event.group": "query_performance",



"content": "/*dt:ownQuery*/SELECT DECODE(name, 'sessions', value) AS sessions_limit, DECODE(name, 'processes', value) AS processes_limit FROM v$parameter WHERE name IN('sessions', 'processes')"



}
```