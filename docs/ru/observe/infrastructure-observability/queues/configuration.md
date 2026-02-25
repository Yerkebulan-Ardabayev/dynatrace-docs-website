---
title: Configure message queue monitoring
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/queues/configuration
scraped: 2026-02-25T21:28:37.060477
---

# Configure message queue monitoring

# Configure message queue monitoring

* How-to guide
* 3-min read
* Updated on Dec 28, 2022

Dynatrace automatically detects how messages are processed within your environment. Under certain circumstances, however, some manual configuration is needed to allow Dynatrace to detect how messages are processed.

## Manual configuration

Review the following table to determine whether some manual configuration is needed.

## Process group detection

OneAgent version 1.250+ Dynatrace uses the IBM MQ queue manager name to detect and group IBM MQ processes. To manage the IBM MQ process group detection

* Go to **Settings** > **Processes and containers** > **Built-in detection rules** and find **Group IBM MQ processes by queue manager name**.
* Via [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers."), use the `builtin:process-group.detection-flags` schema ID.

  To be able to use the API you need an access token with **Read settings** (`settings.read`) and **Write settings** (`settings.write`) scopes. To learn how to obtain it, see [Create an access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.").

The process group detection requires a restart of the IBM MQ process.

## Related topics

* [Custom messaging services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/define-messaging-services "Set up custom messaging services to trace message queues.")