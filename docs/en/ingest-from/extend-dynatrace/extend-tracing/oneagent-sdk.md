---
title: OneAgent SDK
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk
scraped: 2026-02-17T04:50:14.494901
---

# OneAgent SDK

# OneAgent SDK

* Latest Dynatrace
* 2-min read
* Published Mar 01, 2018

Dynatrace provides extensive monitoring capabilities for nearly all popular languages and technologies, including Java, .NET, Node.js, PHP, and Golang. See our [our supported technologies page](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details about all supported technologies.

The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module available yet. With the SDK, you get full access to all analysis and monitoring functionality, including auto-baselining and AI-based root cause analysis.

The Dynatrace OneAgent SDK is available in GitHub. Feedback and feature requests can be filed directly in GitHub.

## What you can do with Dynatrace OneAgent SDK

With the Dynatrace OneAgent SDK, you can:

* Trace incoming and outgoing remote calls
* Trace database requests
* Trace incoming and outgoing web requests
* Trace in-process asynchronous execution
* Trace queues and messages
* Capture request attributes

More functionality will be added to the OneAgent SDK over time. The feature sets differ slightly with each language implementation.

## What you can't do with Dynatrace OneAgent SDK

With the Dynatrace OneAgent SDK, you can't:

* Create user sessions and user actions: This functionality is provided by [Dynatrace OpenKit](/docs/ingest-from/extend-dynatrace/openkit "Learn how you can instrument your application using OpenKit, how you can use Dynatrace OpenKit API methods, and more.")

## How to use the Dynatrace OneAgent SDK

As the OneAgent SDK works hand-in-hand with Dynatrace OneAgent, no additional configuration is required.

The main requirements for using the OneAgent SDK are:

* Access to the source code of the application (and willingness to change the code)
* As the OneAgent SDK communicates directly with OneAgent, OneAgent (minimum required OneAgent version depends on the SDK version) needs to be installed and running on the host that runs the application. Container environments are supported.
* OneAgent in full-stack monitoring mode.

OneAgent automatically detects that your application is instrumented with the OneAgent SDK and immediately begins monitoring it. A restart of the application is required following OneAgent installation on the host.

## OneAgent SDK on GitHub

The Dynatrace OneAgent SDK is published directly to GitHub together with the technical documentation. To get a detailed overview of the current features of the OneAgent SDK, check out the following links:

* [Language independent documentation of the SDK's APIs and conceptsï»¿](https://github.com/Dynatrace/OneAgent-SDK)
* [OneAgent SDK for Javaï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Java)
* [OneAgent SDK for C/C++ï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-C)
* [OneAgent SDK for Node.jsï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-NodeJs)
* [OneAgent SDK for .NETï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet)
* [OneAgent SDK for Pythonï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Python)
* [OneAgent SDK for PHPï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-PHP)

## Further reading

* [Blog: Extend AI-based root cause analysis with OneAgent SDKï»¿](https://www.dynatrace.com/news/blog/extend-ai-based-root-cause-analysis-with-oneagent-sdk)

## Related topics

* [Instrumentation via OneAgent SDK for Android](/docs/observe/digital-experience/mobile-applications/instrument-android-app/instrumentation-via-oneagent-sdk/oneagent-sdk-for-android "Learn how to enrich mobile user experience monitoring in Android using OneAgent SDK.")
* [OneAgent SDK for iOS](/docs/observe/digital-experience/mobile-applications/instrument-ios-app/customization/oneagent-sdk-for-ios "Enrich mobile user experience monitoring using OneAgent SDK for iOS.")
* [OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.")
* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")