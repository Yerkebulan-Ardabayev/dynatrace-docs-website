---
title: Customize service splitting in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2
scraped: 2026-02-18T05:59:03.439391
---

# Customize service splitting in Service Detection v2

# Customize service splitting in Service Detection v2

* How-to guide
* 2-min read
* Updated on Nov 24, 2025

Service Detection v2 (SDv2) lets you split your [detected services](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-detection-v2 "Find out how to detect services based on OpenTelemetry resource attributes.") based on resource attributes.
You can use the default Dynatrace detection rules and also define your own custom rules.
These rules are applied globally to all detected services.

## Aim and context

This page describes service splitting for SDv2, how to use default splitting rules, and how to create your own custom rules.

Service splitting is particularly useful when:

* You need to compare the same service across different environments.
* You want to isolate performance issues to specific deployment regions.
* You need to track behavior differences between service versions.
* You're troubleshooting environment-specific issues.

### Service splitting rules

* Rules are evaluated in order, from top to bottom.
* Custom rules are always evaluated before default rules.
* Only the first matching rule is applied.

### Default splitting rules

Dynatrace provides default service splitting rules as described in the table below.
Additionally, custom rules can be created as described in [Create new rule](/docs/observe/application-observability/services/service-detection/service-detection-v2/service-splitting-v2#create-new-rule "Find out how to split detected services based on resource attributes.").

Priority

Rule name

Condition

Splitting attributes

Status

1

Split Adobe Experience Manager (AEM) services by process group

`adobe.em.tier` + `adobe.em.env_type` + `adobe.em.program`

`dt.entity.process_group`

Enabled

2

Split services by k8s cluster and namespace

None (applies to all)

`k8s.namespace.name` + `k8s.cluster.uid`

Enabled[1](#fn-1-1-def)

3

Split services by k8s namespace Deprecated

None (applies to all)

`k8s.namespace.name`

Disabled[2](#fn-1-2-def)

1

If you began using Dynatrace before Dynatrace version 1.317, this is disabled.

2

If you began using Dynatrace before Dynatrace version 1.317, this is enabled.

## Steps

Service splitting rules are customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Service splitting**.

### Create new rule

1. In **Service splitting**, select **Add rule**.
2. Fill in the following optional and required fields:

   * **Rule name**: Required A user-defined name for the rule.
   * **Description**: Optional A human-readable description of the rule.
   * **Matching condition**: Required A[DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.
   * **Split service by resource attribute**: Optional Spans will be separated into services according to the resource attribute(s) defined here.
     Consists of one or more resource attributes specified without curly braces, e.g. `dt.entity.process_group` or `k8s.namespace.name`.

     To add a resource attribute, select **Add item** and enter the **Attribute key**.

     Up to 10 resource attributes can be configured.
3. To save, select **Save changes**.

### Edit custom rules

You can re-order custom rules to affect the order of precedence.

You can also edit a custom rule.

1. Navigate to the rule and select **Details** > .
2. Edit the field(s) as appropriate.
3. Select **Save changes**.

It's not possible to re-order or edit built-in rules.

### Delete custom rules

You can delete a custom rule.

1. Navigate to the rule and select **Delete** > .
2. Select **Save changes** to permanently delete the rule, or **Discard changes** to keep the rule.

It's not possible to delete built-in rules, however you can deactivate built-in rules.

## Best practices for splitting services

* Start with broader splitting rules before adding more specific ones.
* Don't over-split services as this can cause you to receive the same alert spread across many different services.
* Choose attributes that provide meaningful insights for your specific use case.
* Regularly review splitting rules as your application architecture evolves.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")