---
title: Service Detection v1
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1
scraped: 2026-02-23T21:20:54.038815
---

# Service Detection v1

# Service Detection v1

* Overview
* 1-min read
* Updated on Aug 06, 2025

Service Detection v1 (SDv1) is a service detection mechanism for OneAgent-instrumented services in Dynatrace.

It provides detection capabilities based on technology-specific service types, each with their own detection rules and configuration options. These capabilities include:

* **Service type recognition**: Identify different service types.
* **Custom detection rules**: Fine-tunes how services are detected and grouped.
* **Request naming**: Tracks key business transactions.
* **Failure detection**: Identifies errors and problematic requests.

In addition to SDv1, you can also use [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.") (SDv2), which provides unified service detection rules across OpenTelemetry and OneAgent data sources. SDv2 is available in general availability for OpenTelemetry and in public preview for OneAgent on Kubernetes.

## Service types

SDv1 can detect the following service types:

* **Web request services**: Applications deployed via web servers or web containers.
* **Web services**: As defined by WSDL.
* **Database services**: Applications that make database requests.
* **Messaging services**: Queue and topic listeners in applications.
* **Remoting services**: RMI and RPC communications.
* **Background activity services**: Threads running in the background.
* **Custom services**: User-defined instrumentation for non-standard technologies.

## Configuration options

With SDv1, you can configure the options described below.

### Service detection rules

* Merge applications into a single service.
* Separate services based on URL patterns.
* Create rules for unmonitored hosts.
* Fix web server naming issues.

For details, see [Service detection rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.").

### Service naming

* Built-in rules define out-of-the-box naming.
* Custom service naming rules let you create your own naming standards.
* Service name formats with placeholders for consistent naming conventions.

For additional information, see [Service naming rules](/docs/observe/application-observability/services/service-detection/service-detection-v1/customize-service-naming "Use naming rules to customize and enhance the automated naming of your services.")

### Request naming

* Define how requests appear in your environment.
* Create intuitive names for business transactions.
* Track operations at a granular level.

Check out [Set up request naming](/docs/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") for details.

### Failure detection

* Configure error detection settings globally or for individual services.
* Define custom error rules.
* Handle HTTP errors and exceptions based on your needs.

See [Configure service failure detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.") for more information.

## Related topics

* [Service Detection v2](/docs/observe/application-observability/services/service-detection/service-detection-v2 "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.")
* [Service detection API](/docs/dynatrace-api/configuration-api/service-api/detection-rules "Learn what the Dynatrace service detection rules config API offers.")
* [Process group detection](/docs/observe/infrastructure-observability/process-groups/configuration/pg-detection "Ways to customize process-group detection")