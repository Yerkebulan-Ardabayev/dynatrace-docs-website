---
title: Business events security context
source: https://www.dynatrace.com/docs/observe/business-observability/bo-event-processing/bo-security-context
scraped: 2026-02-17T21:24:48.862245
---

# Business events security context

# Business events security context

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up security context

Dynatrace allows you to tweak your ingested business events data by adding a `dt.security_context` attribute to specific business events records. This enables you to set additional options, for example, permissions for individual records. See, [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

You can set those permissions for individual records on specific attribute values or automatically enriched entities in a business event (hosts, process groups, process group instances) when OneAgent captures data.

For basic use cases, it's best to have the permission boundaries following the deployment of your organization lines around hosts and process groups, or other attributes that can define such boundaries, such as the geographical location of the data.

To create a security context adjustment to your ingested business events data, you need to create rules that:

1. Filter the records that have the `dt.security_context` attribute added to them.  
   Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and create a DQL query using a [business events processing function](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline ."). For example:

   ```
   fetch bizevents



   | filter matchesValue(geo.city.name, "Brussels")
   ```

   This allows you to filter the business events records to which you will want to add the `dt.security_context` attribute. Once satisfied with the query result, copy the business events processing function of the DQL query: `matchesValue(geo.city.name, "Brussels")`.
2. Define the business events security context rule using that function and specify the value of the `dt.security_context` attribute.
   The value of the `dt.security_context` attribute can be a literal value that you provide, or you can specify the name of another attribute of which the value will be used as the value of `dt.security_context`.

### Leverage existing tags at the source

You can define the security context at the source via [OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-security-context "Learn how to set up Grail permissions for OneAgent."), [OpenTelemetry](/docs/ingest-from/opentelemetry/opentelemetry-security-context "Set up Grail permissions for OpenTelemetry."), or [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes"). This allows you to use your existing labels and tags to facilitate permissions in Dynatrace.

## Create a business events security context rule via OpenPipeline

Recommended optional

Business event security context is based on rules that contain a matcher and the `dt.security_context` attribute definition, and they're set as a processor in OpenPipeline. The matcher narrows down the available business event records for executing this specific rule, while the value source type specifies the value of the `dt.security_context` attribute.

For more information, read about [OpenPipeline processors](/docs/platform/openpipeline/concepts/processing#processor "Learn the core concepts of Dynatrace OpenPipeline processing.").

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **Business events**.
2. Go to the **Pipelines** tab and select an existing pipeline or create a new one with an existing dynamic route that would apply on the incoming business event.
3. Select the **Permission** tab to view business events processing security processors that are in effect on that pipeline, reorder the existing processors, and create new processors.
   Processors are executed in the order in which they're listed, from top to bottom. This order is critical because the first user-defined processor that matches is executed. A business events security processor consists of the following:

   * **Name**: The name of the processor.
   * **Matching condition**: A business events processing function that narrows down the available business events data for executing this specific processor.
   * **Security context value**

     + **Field name**: The value will be copied from the field.
     + **Static string**: A constant literal will be used as value.
     + **Static array**: An array literal will be used as value.
   * **Security context field value**: The value of the security context, depending on the selected type.
4. To add a new security context processor, go to the **Permission** tab and select  **Processor** > **Set security context** within the chosen pipeline.
5. Add a matching condition to your processor by pasting the business events processing function from your DQL query.
6. Choose the **Security context value** and provide the **Security context field value**:

   * If you selected **Field**, the value should be the name of the field used as a source to copy the value to the `dt.security_context` attribute.
   * If you selected **Literal**, the value should be the constant literal that will be used as the value in the `dt.security_context` attribute.

### OpenPipeline example

Your business events records contain attribute `geo.city.name` with a value of `Brussels`. Only users in the `team_EU` user group should have access to them and you want to create a business events security context rule that:

* Filters all records that contain `Brussels` as a value of the `geo.city.name` attribute.
* Adds a `dt.security_context` attribute with the `team_EU` value to all filtered business events records.

To create a new rule

1. Go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and execute a DQL query using a [business events processing function](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline ."):

   ```
   fetch bizevents



   | filter matchesValue(geo.city.name, "Brussels")
   ```
2. Copy the business events processing function of the DQL query: `matchesValue(geo.city.name, "Brussels")`.
3. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** and navigate to the pipeline where you want to add the processor.
4. Select the **Permission** tab, and select  **Processor** > **Set security context**.
5. Define your new processor:

   * **Name**: `team_EU - Brussels`
   * **Matching condition**: `matchesValue(geo.city.name, "Brussels")`
   * **Security context value**: select **Static string**
   * **Security context field value**: `team_EU`
6. Select **Save**.

## Create a business events security context rule via the classic pipeline

optional

If you havenât upgraded to Grail and OpenPipeline yet, follow this section for processing via the classic pipeline.

Business event security context is based on rules that contain a matcher and the `dt.security_context` attribute definition.

* The matcher narrows down the available business events records for executing this specific rule.
* Value source type specifies the value of the `dt.security_context` attribute.

Go to **Settings** > **Business Observability** > **Security context** to view business events processing security rules that are in effect, reorder the existing rules, and create new rules. Rules are executed in the order in which they're listed, from top to bottom. This order is critical because the first user-defined rule that matches is executed.

Expand **Details** to examine a rule definition. A business events processing security rule consists of the following:

* **Rule name**: The name for the rule.
* **Matcher**: A business events processing function that narrows down the available business events data for executing this specific rule.
* **Select value source type**

  + **Field**: Value will be copied from field.
  + **Literal**: Constant literal will be used as value.
* **Value**: Value of the source type.

To add a business events security context rule:

1. Select **Add rule** on the **Business event security context** page.
2. Add a **Matcher** to your rule by pasting the [business events processing function](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline .") from your DQL query.
3. Select value source type.
4. Provide the **Value** for the source type.

   * If you selected **Field**, the value should be the name of the field used as a source to copy the value to the `dt.security_context` attribute.
   * If you selected **Literal**, the value should be the constant literal that will be used as the value in the `dt.security_context` attribute.

### Classic processing example

Your business events records contain the attribute `geo.city.name` with the value `Brussels`. Only users in the `team_EU` user group should have access to them and you want to create a business events security context rule that:

* Filters all records that contain `Brussels` as a value of the `geo.city.name` attribute.
* Adds a `dt.security_context` attribute with the `team_EU` value to all filtered business events records.

1. Go to the **Logs and events** page and execute a DQL query using a [business events processing function](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline ."):

   ```
   fetch bizevents



   | filter matchesValue(geo.city.name, "Brussels")
   ```
2. Copy the business events processing function of the DQL query: `matchesValue(geo.city.name, "Brussels")`.
3. Go to **Settings** > **Business Analytics** > **Security context** and select **Add rule** on the **Business event security context** page.
4. Define your new rule:

   * **Rule name**: `team_EU - Brussels`
   * **Matcher**: `matchesValue(geo.city.name, "Brussels")`
   * **Select value source type**: select **Literal**
   * **Value**: `team_EU`
5. Select **Save changes**.

## Check security context

optional

Once new business events data arrives, it's processed by business event security context rules or a processor (depending on the availability of OpenPipeline). A new `dt.security_context` attribute is added with a value of `team_EU`. You can go to ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** and check that new business events records are processed by your `team_EU - Brussels` business events security context rule. Use the DQL to view all business events records containing the `team_EU` value in the `dt.security_context` attribute:

```
fetch bizevents



| filter matchesValue(dt.security_context, "team_EU")
```

Based on this attribute, you can now create security-related user and group policies. See, [Permissions in Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail.").

## Related topics

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [DQL matcher in business event in the classic pipeline](/docs/observe/business-observability/bo-event-processing/bo-events-processing-matcher "This is the DQL matcher in events in the classic pipeline .")