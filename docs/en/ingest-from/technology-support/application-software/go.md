---
title: Go
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/go
scraped: 2026-02-21T21:12:51.534093
---

# Go

# Go

* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 19, 2018

Go is a programming language created by Robert Griesemer, Rob Pike, and Ken Thompson. Go is the cloud-native programming language of choice for many organizations.

Dynatrace provides extensive Go monitoring capabilities:

* Automatic injection and instrumentation of 64-bit Go executables on x86
* OneAgent version 1.323+ Automatic injection and instrumentation of Go executables on AArch64
* [Always-on 24x7 production-grade CPU profiling](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/full-code-level-visibility "Learn how Dynatrace provides full code-level visibility into the performance of your Golang-based applications without requiring any changes to either code or application.")
* [Go-specific metrics](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/analyze-go-metrics "Learn about different Go metrics and how you can analyze them with Dynatrace."):

  + Suspension
  + Committed, used, idle, and live heap memory sizes
  + Application and system Goroutines
  + Go managed memory heaps: Offheap, Stack, and overall committed or used memory
  + Allocated Go objects
  + Garbage collector invocation count
  + Go runtime system calls
  + Go to C language (cgo) calls
  + Global Goroutine run queue size
  + Parked, out of work, and overall worker threads
  + Idle scheduling context count
* [Incoming and outgoing web request monitoring](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/end-to-end-request-monitoring "Find out how Dynatrace provides request-level visibility for your Go-based applications.")
* [gRPC end-to-end service tracing](/docs/whats-new/oneagent/sprint-175#go "Release notes for Dynatrace OneAgent version 1.175")
* [Custom service monitoring](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.")
* [`database/sql`ï»¿](https://dt-url.net/database-sql) service tracing  
  For the list of supported drivers, see [Go technology support](/docs/ingest-from/technology-support#go "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-go/) for capturing traces.  
  For more information, see [Instrument your Go application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/go "Learn how to instrument your Go application using OpenTelemetry and Dynatrace.")

### Support

* [Supported Go versions](/docs/ingest-from/technology-support/application-software/go/support/supported-go-versions "Find out which Go versions are supported by Dynatrace.")
* [Known limitations for Go support](/docs/ingest-from/technology-support/application-software/go/support/go-known-limitations "Learn the limitations for Go support and their workarounds.")

### Configuration and analysis

* [Enable Go monitoring](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/enable-go-monitoring "Learn how you can enable Go monitoring in Dynatrace.")
* [Analyze Go metrics](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/analyze-go-metrics "Learn about different Go metrics and how you can analyze them with Dynatrace.")
* [End-to-end request monitoring](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/end-to-end-request-monitoring "Find out how Dynatrace provides request-level visibility for your Go-based applications.")
* [Full code-level visibility](/docs/ingest-from/technology-support/application-software/go/configuration-and-analysis/full-code-level-visibility "Learn how Dynatrace provides full code-level visibility into the performance of your Golang-based applications without requiring any changes to either code or application.")

### See also

[Blog: Introducing fully automated support for Go-based application monitoringï»¿](https://www.dynatrace.com/news/blog/introducing-fully-automated-support-for-go-based-application-monitoring/)

[Blog: End-to-end request monitoring for Go applications: No code changes requiredï»¿](https://www.dynatrace.com/news/blog/end-to-end-request-monitoring-for-go-applications-no-code-changes-required/)

[Blog: Full code-level visibility now available for Go-application monitoringï»¿](https://www.dynatrace.com/news/blog/full-code-level-visibility-now-available-for-go-application-monitoring/)

[Blog: Introducing custom services for Go applicationsï»¿](https://www.dynatrace.com/news/blog/introducing-custom-services-for-go-applications/)

[Blog: Get automatic code-level insights into your Go applications and cloud platform componentsï»¿](https://www.dynatrace.com/news/blog/automatic-code-level-insights-into-go-applications-without-code-changes/)

[Blog: Worldâs first and only fully automatic observability for Golang services now extended to statically linked Go applicationsï»¿](https://www.dynatrace.com/news/blog/worlds-first-and-only-fully-automatic-observability-for-golang-services-now-extended-to-statically-linked-go-applications/)