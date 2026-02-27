---
title: Configure service failure detection
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection
scraped: 2026-02-27T21:15:32.630194
---

# Configure service failure detection

# Configure service failure detection

* How-to guide
* 9-min read
* Updated on Oct 01, 2025

Dynatrace failure detection automatically detects the vast majority of error conditions in your environment, including the underlying [root causes](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts."). With this approach, Dynatrace is able to provide you with answers when problems occur or when your application performance drops.

When Dynatrace detects a service error, it doesn't necessarily mean that you want to label a request as failed. If the default service-error detection settings don't meet your needs, you can configure failure detection settings as explained in this page.

By default, Dynatrace detects:

* Programming exceptions (Java, .NET, Node.js, and PHP) as the reason for failed requests when exceptions result in the abort of service calls.
* Error pages provided by many web containers for the handled exceptions.
* HTTP `500`â`599` error codes for web requests interpreted as errors on the server side.
* HTTP `400`â`599` error codes for web requests interpreted as errors on the client side.

Why does client side include 5xx codes?

The detected error codes depend on the perspective:

* From the server perspective, only a `5xx` code is an error, because a `4xx` code means a client error.
* From the client perspective, a `5xx` still means there's an error even though it's not the client's fault.

## Failure detection settings

You can configure failure detection globally or on individual services.

* When you configure failure detection settings on the service level, they override the global setup.
* Failure detection rules are evaluated from top to bottom; the first matching rule applies. If multiple failure detection rules have the same conditions, only the first matching rule applies.

The following failure detection rules don't apply to the service types:

* Span service
* Unified service

  To learn more about unified service failure detection, see [Unified services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service "Define services on observability signals ingested via Trace ingest APIs.").

Global settings

Service-level settings

To configure service failure detection globally

1. Go to **Settings** and expand **Server-side service monitoring**.
2. To add a new failure detection rule, go to **Failure detection rules** > **Add failure detection rule**.

   Each rule can have multiple conditions, based on defined failure detection parameters. You can use existing failure detection parameters for failure detection rules or create new ones.

   * To add a new failure detection parameter, go to **Failure detection parameters** > **Add failure detection parameters**. To learn more, see [Parameters](#parameters), [HTTP parameters](#http), and [General parameters](#general) below.
   * Use the **Enabled** switch to turn a rule on or off.
   * Dynatrace recalculates global rule matching every 10 minutes.

To configure service failure for a specific service

1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic** and select the service for which you need to adapt failure detection.
2. Select **More** (**â¦**) > **Settings**.
3. Select **Failure detection** and then **HTTP parameters** or **General parameters**, depending on the parameters you want to configure.
4. Turn on **Override global failure detection settings** (see **1** in the graphic).  
   If a failure detection rule applies, from here you can access both the rule (see **3** in the graphic) and the parameters (see **2** in the graphic).

## Parameters

Parameters for failure detection include HTTP-specific parameters and general parameters (related to exceptions, custom errors, and span failure detection). While you can always access general parameters both globally and on the service level, you might not see HTTP failure detection parameters on the service level, as they are visible only on specific services, such as web requests and web services. You can set them up after enabling **Override global failure detection settings** (**1** in the graphic) and even if no global rule matches the service.

![Failure detection - HTTP parameters](https://dt-cdn.net/images/failure-detection-http-parameters-1791-26675df666.png)

### HTTP parameters

* **HTTP response codes**

  `HTTP-4XX` response codes usually indicate client-side errors, not server-side errors. You can specify which missing HTTP response codes should be treated as server-side errors and which as client-side errors. You can define multiple ranges separated by commas (for example, `400-402, 405-417`).

  Depending on your application, missing response codes might indicate a "fire and forget" call that didnât return a response at all, a timeout, or an error situation. Dynatrace considers missing response codes as special cases and doesnât report them as a default behavior. You can change this by enabling **Treat missing HTTP response code as server side errors** or **Treat missing HTTP response code as client side errors**.
* **HTTP 404 - broken link configuration**

  When a web server canât find a certain page, it returns an `HTTP 404` response code. Usually, this indicates a problem on the calling side. When the calling side belongs to the same website, this would be considered a broken link.

  Because most customers don't consider broken links to be a problem on their server, Dynatrace classifies broken links as client-side problems and not automatically as failures on the server side. However, you can enable the **Consider 404 HTTP response codes as failures** switch to classify broken links as server-side failures. After doing so, you can associate additional hosts at other domains to your application by adding the name of the host under **Add other application domain**.

### General parameters

* **Success forcing exceptions**

  These exceptions indicate that a service call should not be considered as failed, for example, because the client aborted the operation. Although they are technical errors, in principle they don't count as failed requests because they aren't caused by faults with the service. If a request encounters such an exception in the root call of the service, Dynatrace considers the request to be successful, regardless of the HTTP error code or any other information. You can select **Add exception** to add exception classes that indicate such situations.
* **Ignored exceptions**

  There are situations in which your code (or third-party code that you don't control) returns exceptions that indicate a certain response and not an error. For example, the Thrift client for Cassandra returns a `NotFoundException` response when a row isnât found. This isnât an error, but simply a response code.

  You can select **Add exception** to configure Dynatrace to not consider such exceptions as failed request indicators. Additionally, you can define a string that must be found within an exception message for the exception to be ignored. If the HTTP response code for the same call shows an error, Dynatrace considers the request as failed. To consider a request successful regardless of the HTTP error code or any other information, see **Success forcing exceptions**.
* **Custom handled exceptions**

  There are situations in which application code handles exceptions gracefully in a manner that isnât automatically detected by Dynatrace. When this happens, Dynatrace doesnât detect failed requests or alert you to errors.

  You can remedy such situations by specifying an exception class that should result in a failed request. Optionally, you can define a string that must be found in the exception message. If this string isn't found, the exception won't lead to a failed request.  
  If Dynatrace finds the defined exception (and the optionally-defined exception message) on a request, Dynatrace marks the request as failed.  
  Note that this doesn't work if you exclude the exception class from capture in [Deep process monitoring settings](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#deep-monitoring "Ways to customize process-group monitoring").
* **Ignore all exceptions**

  When **Ignore all exceptions** is enabled, Dynatrace ignores **Success forcing exceptions**, **Ignored Exceptions** and **Custom handled exceptions** for the services to which the parameters applyâthe specific service if the switch is enabled on the service-level or the services that match the global rule.
  Because exceptions are still tracked, they appear in distributed traces, but you don't receive alerts for them and requests aren't labeled as failed.
* **Custom errors via request attributes**

  Custom error situations might be triggered by exceptions, but some are detectable only via a return value or other means. To support such cases, you can define a [request attribute](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") that captures the required data. You can then define a custom error rule based on the request attribute that checks the value of the request attribute to determine if the request has failed or not.

  Example: Use request attributes to detect business logic-related errors

  Requests might fail for reasons related to business logic. These situations often arenât detectable via exceptions or HTTP response codes. Nevertheless, they are indicative of problems and might be even more important than situations detected via exceptions and response codes. For example, you might have a business function in your Java code that indicates an error via a return value or you might have your own error-handling functionality that, when called, indicates a functional business error.

  Such situations can be captured via [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views."), which you can use as indicators for error situations.

  To create a custom error rule

  1. Go to ![Services Classic](https://dt-cdn.net/images/services-classic-f58502bd22.svg "Services Classic") **Services Classic**.
  2. Select the service for which you need to adapt failure detection.
  3. Select **More** (**â¦**) > **Settings**.
  4. Select **Failure detection** > **General parameters**
  5. Under **Custom error rules**, select **Add custom error rule**.
  6. Select a request attribute from the displayed list.
  7. Define a condition for the rule, such as **contains** and a value.

  In the example below, a value of `-1` in the `Amount of recommendations` attribute indicates an error. Following this rule, if Dynatrace detects such an error, it will mark the respective service request as failed and explain that the rule match is the reason for the failure.

  ![Custom error rule](https://dt-cdn.net/images/custom-error-rule-2908-978f284947.png)
* **Span failure**

  Span failure detection is specific to OpenTelemetry. Dynatrace by default detects span failures, but there are specific cases in which you might want to change these settings. To ignore span failure detection, turn on **Ignore span failure detection**.

## Schema info

On the service level, you can visualize the **Schema ID** by selecting **More** (**â¦**) > **Schema info** in the upper-right corner of the **HTTP parameters** or **General parameters** page.

## Related topics

* [Request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.")
* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.")
* [Failure detection API](/docs/dynatrace-api/configuration-api/service-api/failure-detection "Learn what the Dynatrace failure detection config API offers.")