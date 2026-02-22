---
title: Customize service detection in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2
scraped: 2026-02-22T21:24:24.318322
---

# Customize service detection in Service Detection v2

# Customize service detection in Service Detection v2

* How-to guide
* 2-min read
* Updated on Nov 24, 2025

Service Detection v2 (SDv2) allows you to define services based on span resource attributes.
You can use the default Dynatrace detection rules and also define your own custom rules.
The same rules are also applied to log and metric ingest which allows Dynatrace to link the input of all sources together.

## Aim and context

This page describes service detection for SDv2, how to use default detection rules, and how to create your own custom rules.

### Service detection rules

* Rules apply to spans, metrics, and logs.

* Rules are evaluated in order, from top to bottom.
* Custom rules are always evaluated before default rules.
* Only the first matching rule is applied.

### Default service detection rules

Dynatrace provides several default service detection rules.
Additionally, custom rules can be created as described in [Create new rule](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2#create-new-rule "Find out how to detect services based on OpenTelemetry resource attributes.").

Any future default rule changes will be opt-in: new rules will be shipped as disabled; you can choose whether to activate them.

Priority

Condition

Service name

1

`adobe.em.tier`, `adobe.em.env_type`, `adobe.em.program` attributes present

`aem-{adobe.em.tier}-{adobe.em.env_type}-{adobe.em.program}`

2

`k8s.workload.name` attribute present

`{k8s.workload.name}`

3

`dt.kubernetes.workload.name` attribute present

`{dt.kubernetes.workload.name}`

4

`istio.canonical_service` attribute present

`{istio.canonical_service}`

5

`service.name` attribute present

`{service.name}`

The service ID is a unique identifier, such as `SERVICE-649B4E44CBA804F4`, that is the result of hashing the attribute values that are used as part of the name pattern, additional service detection attributes, and [service splitting attributes](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2 "Find out how to split detected services based on resource attributes."), when applicable.

## Steps

Detection rules are customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Service detection**.

### Create new rule

1. In **Service detection**, select **Add rule**.
2. Fill in the following optional and required fields:

   * **Rule name**: Required

     A user-defined name for the rule.
   * **Description**: Optional

     A human-readable descriptor of the rule.
   * **Matching condition**: Required

     A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.
   * **Service name template**: Required

     The name that you want the service to have.
     You can use plain text, or resource attributes surrounded by curly braces (`{}`).
     For the rule to be applied, the span must contain all the specified resource attributes.
     Changing the static parts of the template or re-ordering the used attributes will not affect the service ID. Only completely removing an attribute or adding a new attribute will also change the service ID.
   * **Additional service detection attributes**: Optional

     Additional attributes used to detect and split services without affecting the generated name.
     Each attribute consists of a resource attribute specified without curly braces (for example, `service.name` or `k8s.workload.name`).
     Adding or removing attributes in this section will change the resulting service ID.

     Up to 10 additional service detection attributes can be applied.
3. Select **Save changes**.

### Edit custom rules

You can re-order custom rules.

You can also edit a custom rule.

1. Navigate to the rule and select **Details** > .
2. Edit the fields as appropriate.
3. Select **Save changes**.

### Delete custom rules

To delete a custom rule

1. Navigate to the rule and select **Delete** > .
2. Select **Save changes** to permanently delete the rule, or **Discard changes** to keep the rule.

You can delete only custom rules, not the built-in rules.

## FAQ

### How can I remove an attribute that was used as part of the service name without also changing the service ID?

To remove an attribute that was used as part of the service name without also changing the service ID

1. Remove the attribute from the **Service name template**.
2. Add the attribute to the **Additional service detection attributes** section.

This way, it will still contribute to the service ID, but it will no longer be part of the service name.

### My **Matching conditions** do match certain spans but still my rule is not applied. Why?

Verify that all the attributes used as parts of the **Service name template** and **Additional service detection attributes** also exist on the spans. The existence of those attributes is an implicit matching condition.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")