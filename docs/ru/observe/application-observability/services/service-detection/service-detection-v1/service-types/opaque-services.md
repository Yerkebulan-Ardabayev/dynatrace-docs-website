---
title: Opaque services
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/opaque-services
scraped: 2026-02-18T21:17:05.094725
---

# Opaque services

# Opaque services

* How-to guide
* 3-min read
* Published Oct 04, 2017

Opaque services are services that are detected on the calling side by Dynatrace for which code-level visibility isn't available. Dynatrace can detect requests to opaque services and identify which processes they are processed by, but Dynatrace can't monitor these services directly.

Code-level visibility isn't possible if:

* A service is of a technology type for which deep monitoring isn't supported.
* A service is of an unrecognized or unsupported technology.

## No deep monitoring support

Code-level visibility might not be available for some technologies, even though the technology is supported by Dynatrace.

Nevertheless, Dynatrace can detect all requests to such services that are sent by services with full visibility. Dynatrace calculates response times and failure rates and generates appropriate alerts.

Thanks to artificial intelligence, Dynatrace understands the impact that host and process performance problems can have on services. This is why Dynatrace correlates host and process issues with corresponding slow-downs in service requests. For example, if a service without code-level visibility crashes, Dynatrace will interpret the crash as the root cause of any increased failure rate in calls to this service.

## Unrecognized or unsupported technologies

When a service is of an unrecognized technology or a technology that is recognized but not currently supported by Dynatrace, the service is considered to be opaque.

Although deep monitoring isn't supported for such services, Dynatrace can still detect all requests to this service that are sent by fully visible services and, for example, calculate the relevant response times and failure rate.

Opaque services of unrecognized or unsupported technologies are included in Smartscape. This ensures a complete representation of your infrastructureâs topology, even when your environment includes opaque services.

The [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") enables you to instrument your application manually to extend end-to-end visibility for unrecognized or unsupported technologies.

## Other reasons services may be classified as opaque

There can be cases where a service is considered opaque even when the service is recognized and of a supported technology. This can occur for the multiple reasons, such as:

* A process is offline but a service still makes calls to it. These opaque services are used to visualize dependencies in the context of availability problems.
* A process never started processing a request (the calling service receives an error or timeout) and therefore Dynatrace can't track the request in the process.
* A process hasn't completely restarted following OneAgent installation. By the time the process restarts, it should no longer appear as opaque.
* The framework processing the request at the specific port is not currently supported by OneAgent. If this is important to you, please suggest a product idea for the specific framework and version in [Dynatrace Community product ideasï»¿](https://community.dynatrace.com/t5/Product-ideas/idb-p/DynatraceProductIdeas) (Community sign-in required).
* The framework is supported, but OneAgent has run into a technical problem. In such a case, please [submit a Support ticketï»¿](https://www.dynatrace.com/support/contact-support/). Describe the issue as best you can and include all details regarding your underlying framework, technologies, and versions.