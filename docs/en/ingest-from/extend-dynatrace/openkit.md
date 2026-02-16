---
title: Extend user experience and behavior data
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/openkit
scraped: 2026-02-16T21:22:07.477918
---

# Extend user experience and behavior data

# Extend user experience and behavior data

* Latest Dynatrace
* 2-min read
* Updated on May 30, 2022

There are many ways your business can interact with your customers in the digital world. Monitoring user experience and behavior in your web and mobile applications is a great way to get started with digital experience monitoring; Dynatrace easily detects and automatically monitors all application touchpoints using OneAgent. However, your business likely has many other digital touchpoints outside of your applications where your customers interact with your brand that are also key to the success of your business. With Dynatrace OpenKit, you get a set of open source libraries that enable you to instrument all other digital touchpoints in your environment, whether or not theyâre traditional rich client applications, smart IoT applications, or even Alexa skills.

Dynatrace OpenKit is a set of open source libraries that provides an easy, lightweight means of instrumenting the source code of your custom applications so that you can monitor their performance with Dynatrace. Dynatrace OpenKit is best suited for client/server applications that communicate via HTTPâfor example, rich client applications, embedded devices, and terminals.

The main advantages of OpenKit are:

* Ease of use
* No OneAgent library dependencies
* Ease of portability to other languages and platforms

With Dynatrace OpenKit, you can:

* Track [user sessions](/docs/observe/digital-experience/rum-concepts/user-session "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.") and [user actions](/docs/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.")
* Report events, errors, and crashes
* Trace web requests to [server-side distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")
* Tag user sessions with user tags
* Maintain compatibility with Dynatrace

With Dynatrace OpenKit, you can't:

* Create server-side distributed traces. This functionality is provided by the Dynatrace OneAgent SDK.
* Create metrics. However, you can use the [Topology and Smartscape API](/docs/dynatrace-api/environment-api/topology-and-smartscape/custom-device-api/report-custom-device-metric-via-rest-api "Learn how you can use the Dynatrace API to send a custom metric data point to a custom device.") and [Metrics API](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.") to report metrics.

As of April 2022, Dynatrace no longer supports TLS 1.0 and TLS 1.1 for Dynatrace SaaS Real User Monitoring (RUM) data. Now Dynatrace SaaS only supports TLS 1.2+. For this reason, using a .NET Framework version lower than 4.7 might require [additional configurationï»¿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/tls#if-your-app-targets-a-net-framework-version-earlier-than-47).