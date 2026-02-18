---
title: Customize endpoint detection in Service Detection v2
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v2/endpoint-detection-v2
scraped: 2026-02-18T21:33:01.390665
---

# Customize endpoint detection in Service Detection v2

# Customize endpoint detection in Service Detection v2

* How-to guide
* 2-min read
* Updated on Feb 04, 2026

Service Detection v2 (SDv2) allows you to identify specific endpoints into your services.
You can use the default Dynatrace detection rules and also define your own custom rules.

If you have existing OpenTelemetry endpoints created before August 2025, you are currently using [hard-coded endpoint detection rules](#legacy-default-endpoint-rules). You can opt in to the [new improved rules](#default-endpoint-rules), which are now configurable and provide better service health monitoring via [settings](#new-default-endpoint-rules-opt-in), but this will cause breaking changes to your endpoints. See the [community postï»¿](https://dt-url.net/lv031sg) for comparison dashboards before opting in.

## Aim and context

This page describes endpoint detection for SDv2, how to use default detection rules, and how to create your own custom rules.

SDv2 treats the following span types as endpoints:

* Standard HTTP and gRPC endpoints (`span.kind == server`).
  These are treated as web-based entry points into a service and represent incoming HTTP or gRPC requests handled by the service.
* Message consumption endpoints (`span.kind == consumer`).
  These are treated as entry points into a service for messages from queue systems like RabbitMQ, ActiveMQ, and Kafka and represent messages consumed by the service.

## Endpoint detection rules

* Rules are evaluated in order, from top to bottom.
* Custom rules are always evaluated before default rules.
* Only the first matching rule is applied.

### New endpoint detection opt-in

Opting in will enable the creation of [custom rules](#create-new-rule) and the use of the new [default rule set](#default-endpoint-rules), but will break existing endpoints. See the [community postï»¿](https://dt-url.net/lv031sg) for comparison dashboards before opting in.

You can find the setting to opt in to the new way of endpoint detection in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Enable endpoint detection**.

If this setting is not available, you are already using the new configurable endpoint detection rules. This can happen if we didn't find any SDv2-related data in your tenant during the update to Dynatrace version 1.321, or if your tenant was created using Dynatrace version 1.321 or later.

### Default rules

These rules focus on actual service health by considering only service entry points (server and consumer spans), excluding outbound calls to other services. This provides more accurate service health monitoring by distinguishing service problems from external dependency issues.

* The default endpoint detection rules can be activated or deactivated.
* You can add custom endpoint detection rules as described in [Create new rule](#create-new-rule).

Any tenant created with Dynatrace version 1.330+ uses these configurable rules. Older tenants can be opted in to the configurable rule set; see the [New endpoint detection opt-in](#new-default-endpoint-rules-opt-in) section.

Priority

Condition

Endpoint

1

`span.kind == "server"` + `rpc.service` + `rpc.method`

`{rpc.service}.{rpc.method}`

2

`span.kind == "server"` + `rpc.method`

`{rpc.method}`

3[1](#fn-1-1-def)

`span.kind == "server"` + `http.request.method` + `url.path.pattern`

`{http.request.method} {url.path.pattern}`

4

`span.kind == "server"` + `http.request.method` + `url.truncated_path`

`{http.request.method} {url.truncated_path}`

5

`span.kind == "server"` + `http.request.method` + `http.route`

`{http.request.method} {http.route}`

6

`span.kind == "server"` + `http.request.method`

`{http.request.method} /*`

7

`span.kind == "server"` + `span.name`

`{span.name}`

8

`span.kind == "consumer"` + `span.name`

`{span.name}`

1

Rule available with Dynatrace SaaS version 1.330+. See [Configure URL path pattern matching in Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2/url-pattern-matching-v2 "Find out how to get better endpoint names for frameworks without route templates by setting up URL pattern matching rules.") for details.

### Legacy default rules

Legacy endpoint detection rules apply also to all trace root spans (span without a parent span)âwhether client, consumer, internal, or producer span. This broad approach captured comprehensive system activity but created noise in service health monitoring, since outbound call failures typically indicate problems with the called service rather than the calling service.
However, you can still add custom endpoint rules to the new endpoint detection to restore exactly this behavior.

Priority

Condition

Endpoint name

1

`service.name` starts with `istio-`

`/`

2

`rpc.service` + `rpc.method` + `span.kind` is `server`

`<rpc.method>.<rpc.service>` or `<rpc.method>`

3

`adobe.em.env_type` + `url.truncated_path` + `span.kind` is `server`

`<url.truncated_path>`

4

`adobe.em.env_type` + `url.path` is `/system/probes/health` OR `http.request.method` is `HEAD`

`Health Check`

5

`http.route` + `span.kind` is `server`

`<http.route>`

6

`http.method` + `span.kind` is `server` + `telemetry.sdk.language` is `apache`, `cpp`, or `nginx`

`/`

7

`faas.name`

`invoke`

8

`code.namespace` + `code.function`

`<code.namespace>.<code.function>` or `<code.function>` or `<code.namespace>`

9

`span.name`

`<span.name>`

## Steps

Endpoint detection is customized in ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **Services** > **Endpoint detection**.

### Create new rule

1. In **Endpoint detection**, select **Add rule**.
2. Fill in the following optional and required fields:

   * **Rule name**: Required A user-defined name for the rule.
   * **Description**: Optional A human-readable description of the rule.
   * **Matching condition**: Required A [DQL matcher](/docs/platform/openpipeline/reference/dql-matcher-in-openpipeline "Examine specific DQL functions and logical operators for log processing.").
     If the matching condition applies, the rule is evaluated.

     Keep in mind that the rules are applied on spans with span kind `span.kind == server` or `span.kind == consumer`, as well as on trace root spans (spans without a parent span) regardless of the span kind.

     To avoid unexpected behavior, we recommend adding the span kind explicitly to the condition. For example, `span.kind == server` for HTTP endpoints or `span.kind == consumer` for message consumption endpoints.

   * **If condition matches**: Required The action that will be taken.
     Options are either

     + **Detect request on endpoint**: The endpoint is detected and named.
     + **Suppress request**: The endpoint will not be detected by this or any subsequent rule.
   * **Endpoint name template**: The name that you want the endpoint to have.
     You can use plain text, or span and resource attributes surrounded by curly braces (`{}`).
     For the rule to be applied, the span must contain all the specified resource attributes.
3. Select **Save changes**.

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

## Best practices when creating new rules

* Keep the number of custom rules manageable to maintain performance.
  For many environments, the default rules will be enough.
* Start by creating endpoint rules for the most critical endpoints.
* Use consistent naming conventions for your endpoints.
* Regularly review your custom endpoint rules to ensure that they still match your application architecture.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")