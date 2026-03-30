---
title: Go
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/go
scraped: 2026-03-05T21:25:20.925617
---

# Go


* Latest Dynatrace
* Reference
* 1-min read
* Published Mar 19, 2018

Go is a programming language created by Robert Griesemer, Rob Pike, and Ken Thompson. Go is the cloud-native programming language of choice for many organizations.

Dynatrace provides extensive Go monitoring capabilities:

* Automatic injection and instrumentation of 64-bit Go executables on x86
* OneAgent version 1.323+ Automatic injection and instrumentation of Go executables on AArch64
* Always-on 24x7 production-grade CPU profiling
* Go-specific metrics:

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
* Incoming and outgoing web request monitoring
* gRPC end-to-end service tracing
* Custom service monitoring for custom services that don't use standard protocols.")
* [`database/sql`ï»¿](https://dt-url.net/database-sql) service tracing  
  For the list of supported drivers, see [Go technology support](../../technology-support.md#go "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-go/) for capturing traces.  
  For more information, see Instrument your Go application with OpenTelemetry

### Support

* Supported Go versions
* Known limitations for Go support

### Configuration and analysis

* Enable Go monitoring
* Analyze Go metrics
* End-to-end request monitoring
* Full code-level visibility

### See also

[Blog: Introducing fully automated support for Go-based application monitoringï»¿](https://www.dynatrace.com/news/blog/introducing-fully-automated-support-for-go-based-application-monitoring/)

[Blog: End-to-end request monitoring for Go applications: No code changes requiredï»¿](https://www.dynatrace.com/news/blog/end-to-end-request-monitoring-for-go-applications-no-code-changes-required/)

[Blog: Full code-level visibility now available for Go-application monitoringï»¿](https://www.dynatrace.com/news/blog/full-code-level-visibility-now-available-for-go-application-monitoring/)

[Blog: Introducing custom services for Go applicationsï»¿](https://www.dynatrace.com/news/blog/introducing-custom-services-for-go-applications/)

[Blog: Get automatic code-level insights into your Go applications and cloud platform componentsï»¿](https://www.dynatrace.com/news/blog/automatic-code-level-insights-into-go-applications-without-code-changes/)

[Blog: Worldâs first and only fully automatic observability for Golang services now extended to statically linked Go applicationsï»¿](https://www.dynatrace.com/news/blog/worlds-first-and-only-fully-automatic-observability-for-golang-services-now-extended-to-statically-linked-go-applications/)