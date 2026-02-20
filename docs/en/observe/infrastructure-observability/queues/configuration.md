---
title: Configure message queue monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration
scraped: 2026-02-20T21:26:03.473951
---

# Configure message queue monitoring

# Configure message queue monitoring

* How-to guide
* 3-min read
* Updated on Dec 28, 2022

Dynatrace automatically detects how messages are processed within your environment. Under certain circumstances, however, some manual configuration is needed to allow Dynatrace to detect how messages are processed.

## Manual configuration

Review the following table to determine whether some manual configuration is needed.

If this is trueâ¦

â¦then this manual configuration is needed

The application uses non-standard or non-event-based message queue handlers.

Define a [custom messaging service](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Set up custom messaging services to trace message queues.").

You're using IBM MQ.

Define your [IBM MQ](/docs/observe/infrastructure-observability/queues/configuration/ibm-mq-tracing "Configure Dynatrace for IBM MQ tracing.") configuration in Dynatrace to get a continuous service flow.

The messaging client isn't compatible with Dynatrace, or you're using an unsupported protocol.

Extend the traces with [OpenTelemetry](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.") or [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") (see also [OneAgent SDK on GitHubï»¿](https://github.com/Dynatrace/OneAgent-SDK#trace-messaging)).

## Process group detection

OneAgent version 1.250+ Dynatrace uses the IBM MQ queue manager name to detect and group IBM MQ processes. To manage the IBM MQ process group detection

* Go to **Settings** > **Processes and containers** > **Built-in detection rules** and find **Group IBM MQ processes by queue manager name**.
* Via [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), use the `builtin:process-group.detection-flags` schema ID.

  To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

The process group detection requires a restart of the IBM MQ process.

## Related topics

* [Custom messaging services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Set up custom messaging services to trace message queues.")