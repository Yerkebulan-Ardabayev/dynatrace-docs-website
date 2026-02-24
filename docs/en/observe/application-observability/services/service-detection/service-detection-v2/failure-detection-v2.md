---
title: Customize failure detection in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/failure-detection-v2
scraped: 2026-02-24T21:24:19.963307
---

# Customize failure detection in Service Detection v2

# Customize failure detection in Service Detection v2

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Nov 24, 2025

Service Detection v2 (SDv2) allows you to detect failures based on the attributes of a span that is relevant to failure detection.
These relevant spans include, for example, [request](/docs/semantic-dictionary/fields#request "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") root spans.
You can use the default Dynatrace detection rules and also define your own custom rules.

## Aim and context

This page describes failure detection for SDv2, how to use default detection rules, and how to create your own custom rules.

Failure detection consists of:

* The ruleset, which is a DQL matcher that specifies the overall span and resource attributes that are evaluated.
* Failure conditions under which the span will fail.
* Custom failure rules that use DQL matchers to specify additional conditions under which the span will fail.
* Ignored exceptions, where you can force the span to succeed even in if the defined exceptions occur.

### Failure detection rulesets and rules

* Rulesets and rules are evaluated in order, from top to bottom.
* Custom rulesets are always evaluated before default rulesets.
* The first matching ruleset is applied.
* Within the applied ruleset, all rules are evaluated.

### Default failure detection rulesets and rules

Dynatrace provides default failure detection rulesets and rules.
Additionally, you can add custom rulesets and rules as described in [Create new ruleset](/docs/observe/application-observability/services/service-detection/service-detection-v2/failure-detection-v2#create-new-ruleset "Find out how to detect failed requests within services.").

A request is considered successful if no failure detection rule matches.

## Steps

Failure detection is customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Failure detection**.

To configure failure detection:

1. Create the ruleset.
2. Define the failure conditions.
3. Define the ignored exceptions. Optional
4. Define the rule(s). Optional
5. Define any HTTP or gRPC status code overrides. Optional

### Create the ruleset

1. In **Failure detection**, select **Add ruleset**.
2. Fill in the following optional and required fields:

   * **Ruleset name**: Required A user-defined name for the ruleset.
   * **Description**: Optional A human-readable description of the rule.
   * **Matching condition**: Required A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing."), which specifies the span and resource attributes that the ruleset applies to.
     If the matching condition applies, the ruleset is evaluated.
3. To save, select **Save changes**.

### Define the failure conditions

Within the ruleset, these parameters define conditions under which a span will fail.

* **HTTP status codes**: One or more HTTP status codes.
  If one of these codes is returned, the span will fail.
  By default this is set to `500-599`.
* **gRCP status codes**: One or more gRCP status codes.
  If one of these codes is returned, the span will fail.
  By default this is set to `2,4,12,13,14,15`.
* **Span status code**: If enabled: when the span's status code indicates a failure, the span will fail.
  By default, this is enabled.
* **Exceptions**: If enabled: when an unescaped exception occurs, the span will fail.
  By default, this is enabled.

### Add ignored exceptions

Optional

Within a ruleset, you can exclude specific exceptions.
If the span includes the defined exception type and message, this exception will not cause the span to fail.

Select **Add ignored exception** and enter values for both:

* **Exception type contains**.
* **Exception message contains**.

Example ignored exception

To ignore all NullPointerExceptions that contain the expected null value in their message, set the following values.

* Exception type contains: `NullPointerException`
* Exception message contains: `<Expected null value>`

### Define the custom failure rule(s)

Optional

Beyond the failure conditions that you already defined, you can define additional custom conditions under which a span will fail.
These conditions are called custom failure rules.
They are defined with any key/value pair using DQL matchers.

1. To define a rule, select **Add custom rule**.
2. Fill in the following required fields.

   * **Rule name**: A descriptive name.
   * **DQL condition**: A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.") that consists of one or more DQL functions.
     If the matching condition applies, the rule is triggered.
     If the matching condition does not apply, the rule is not triggered.

     Whether or not the condition applies, the span is evaluated against subsequent rules.

When a rule is triggered, a corresponding entry in the [`dt.failure\_detection.results array](/docs/semantic-dictionary/model/trace#failure-detection-result "Get to know the Semantic Dictionary models related to traces.") is created.

Example custom rule

This is an example custom rule to detect business logic failures.

* Rule name: `Business Transaction Failure`
* DQL matching rule: `transaction.status == "FAILED"`

### Override failure detection

Optional

Sometimes, you want a span to succeed even if it contains error indicators.
Within a ruleset, you can define certain conditions that will force success.

To do this, select  > **Override failure detection with success forcing rules**.
Then, define one or more rules.

* **HTTP status codes**: The HTTP error code(s) that will force success on the server side.
* **gRPC error codes**: The gRPC error code(s) that will force success on the server side.
* **Span status code**: If the span's status code is `OK` it will succeed, regardless of any other error indicators.
* **Force success on specific exceptions**: Specific exceptions that should force success, see [Define ignored exceptions](#ignored-exceptions).
* **Custom success forcing rules**: Custom conditions that should force success, see [Define the rule(s)](#define-rules).

Example escaped exception

To force success on an example span that contains an escaped exception, set the following values.

* Evaluated expression: `Any(span.events[][span_event.name] == "exception" and span.events[][exception.escaped] != false)`
* Failure detection result: `reason="exception", verdict="success", exception_ids`

This is useful for applications that use exceptions as part of normal control flow rather than as error indicators.

Example custom success rule

To force success for an expected business condition, set the following values.

* Rule name: `Expected Cache Miss`
* DQL matching rule: `cache.result == "MISS" and operation.type == "READ"`

This is useful for business-specific scenarios where there are expected business conditions.

### Edit custom rulesets and rules

You can re-order custom rulesets and rules to affect the order of precedence.

You can also edit custom rulesets and rules.
To do so, navigate to the ruleset or rule and select **Details** > .
Edit the field(s) as appropriate and then select **Save changes**.

### Delete custom rulesets and rules

To delete a custom ruleset or rule, navigate to the ruleset or rule and select **Delete** > .
Select **Save changes** to permanently delete the ruleset or rule, or **Discard changes** to keep the rule.

You can delete only custom rulesets and rules, not the built-in ones.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")