---
title: Extend user experience and behavior data
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/openkit
scraped: 2026-03-06T21:16:33.806116
---

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

* Track user sessions and user actions
* Report events, errors, and crashes
* Trace web requests to server-side distributed traces
* Tag user sessions with user tags
* Maintain compatibility with Dynatrace

With Dynatrace OpenKit, you can't:

* Create server-side distributed traces. This functionality is provided by the Dynatrace OneAgent SDK.
* Create metrics. However, you can use the Topology and Smartscape API and Metrics API to report metrics.

As of April 2022, Dynatrace no longer supports TLS 1.0 and TLS 1.1 for Dynatrace SaaS Real User Monitoring (RUM) data. Now Dynatrace SaaS only supports TLS 1.2+. For this reason, using a .NET Framework version lower than 4.7 might require [additional configurationï»¿](https://docs.microsoft.com/en-us/dotnet/framework/network-programming/tls#if-your-app-targets-a-net-framework-version-earlier-than-47).