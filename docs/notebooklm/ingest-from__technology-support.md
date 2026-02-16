# Dynatrace Documentation: ingest-from/technology-support

Generated: 2026-02-16

Files combined: 22

---


## Source: cpp.md


---
title: C++
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/cpp
scraped: 2026-02-16T09:21:52.079873
---

# C++

# C++

* Latest Dynatrace
* Reference
* 1-min read
* Published Dec 20, 2022

You can send data from your C++ application to Dynatrace via OpenTelemetry. See also

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-cpp) for capturing traces.

  + [Instrument your C++ application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/cpp "Learn how to instrument your C++ application using OpenTelemetry and Dynatrace.")
* [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing


---


## Source: dotnet.md


---
title: .NET
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/dotnet
scraped: 2026-02-16T09:21:40.340415
---

# .NET

# .NET

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Oct 23, 2025

Dynatrace OneAgent instruments your .NET applications by placing trace statements at strategic locations in your code for code tracing, performance metrics, error detection, dependency tracking, and more.

Not every detected .NET application is instrumented by default. Dynatrace maintains a set of rules to instrument specific processes (for example, IIS application-pools, which you can extend with our own rules). To learn the basics about process group monitoring setup (automatic deep monitoring, custom monitoring rules, and built-in monitoring rules), see [Set up process group monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Capabilities

Dynatrace provides extensive .NET monitoring capabilities:

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-dotnet) for capturing traces and ingesting metrics.  
  For more information, see [Instrument your .NET application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/dotnet "Learn how to instrument your .NET application using OpenTelemetry and Dynatrace.")
* End-to-end transaction tracing of requests to web services, remoting services, queues, and databases. [Learn more about services](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.")
* [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing
* Garbage collection, process metrics, and much more
* [Always-on 24x7 production grade CPU profilingï»¿](https://www.dynatrace.com/news/blog/analyze-cpu-consumption-background-threads/)

See our [supported technologies matrix](/docs/ingest-from/technology-support#net "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details on supported frameworks.

## Supported .NET versions

Version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

10

2025-11-11

-

1.325

-

-

Supported

9

2024-11-12

-

1.305

-

-

Supported

8

2023-11-14

-

1.277

-

-

Supported

7

2022-11-08

-

1.263

-

-

Supported

6

2021-11-08

-

1.229

-

-

Supported

5

2020-11-10

-

1.203

-

-

Supported

Core 3.1

2019-12-03

-

1.183

-

-

Supported

Core 3.0

2019-09-23

-

1.177

-

-

Supported

Core 2.2

-

2019-12-23

-

-

-

Supported

Core 2.1

-

-

-

-

-

Supported

Core 2.0

-

2018-10-01

-

1.297

2024-08-31

Limited[1](#fn-net-and-net-core-1-def)

Core 1.1

-

2019-06-27

-

1.177

2019-12-01

Not supported

Core 1.0

-

2019-06-27

-

1.177

2019-12-01

Not supported

1

Limited support: Dynatrace can only solve problems that can be reproduced on supported versions.

## Supported .NET Framework versions

Version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

4.5.2 - 4.8

-

-

-

-

-

Supported

4.5.1

-

2016-01-12

-

-

-

Limited[1](#fn-net-framework-1-def)

4.5

-

2016-01-12

-

-

-

Limited[1](#fn-net-framework-1-def)

4

-

2016-01-12

-

-

-

Limited[1](#fn-net-framework-1-def)

3.5 SP1

-

-

-

-

-

Supported

1

Limited support: Dynatrace can only solve problems that can be reproduced on supported versions.

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

## Support lifecycle

Dynatrace is committed to support each version according to its support lifetime:

* See [Microsoft support lifecycle for .NET and .NET Coreï»¿](https://docs.microsoft.com/en-us/lifecycle/products/microsoft-net-and-net-core).
* See [Microsoft support lifecycle for .NET Frameworkï»¿](https://docs.microsoft.com/en-us/lifecycle/products/microsoft-net-framework).

## Limitations

### Method hotspots on Linux

The .NET code module uses POSIX signals to capture stack traces for the method hotspots feature.

Because those signals can interrupt the application at arbitrary times, certain applications/libraries (in particular, .NET libraries with native dependencies) might not work correctly with method hotspots features enabled.

An affected application might show symptoms such as:

* Connectivity problems
* Mangled text data
* Kubernetes readiness and liveness probes failing

The only current solution is to disable the corresponding OneAgent features for the affected process group:

* Capture method hotspot information in PurePaths
* Capture background CPU method hotspot information
* .NET Async Method Hotspots

Method hotspots might not be able to correctly capture stack traces on musl-libc based operating systems such as Alpine. This is because certain debug information is removed by the musl-libc library. Moving to a glibc-based operating system (Debian/Ubuntu) can mitigate this specific issue.

* .NET method hotspots are not available for Linux on ARM64 (AArch64).

### Trimming

The optional .NET feature [trimmed self-contained deployments and executablesï»¿](https://docs.microsoft.com/en-us/dotnet/core/deploying/trim-self-contained) was introduced to optimize the size of packaged applications.
Trimmed applications are not supported by OneAgent therefore this option must be turned off. [UiPathï»¿](https://www.uipath.com/), for example, uses trimming, which makes it impossible to instrument with OneAgent.

### Single-file applications

The .NET SDK supports building your application as a [single fileï»¿](https://learn.microsoft.com/en-us/dotnet/core/deploying/single-file/overview?tabs=cli) that bundles all dependencies into one platform-dependent executable.

Depending on whether you use [framework-dependent deploymentï»¿](https://learn.microsoft.com/en-us/dotnet/core/deploying/#publish-framework-dependent) or [self-contained applicationsï»¿](https://learn.microsoft.com/en-us/dotnet/core/deploying/#publish-self-contained), the runtime will also be bundled into the executable.

Consider also the following information:

* OneAgent doesn't support the instrumentation of modules bundled into the executable, which results in applications built as single files and self-contained not being supported at all.
* Applications built as single file and framework-dependent can be partly instrumented.
* .NET assemblies bundled into the single-file executable can't be instrumented (tracing logic can't be placed for those assemblies).


---


## Source: erlang-elixir.md


---
title: Erlang/Elixir
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/erlang-elixir
scraped: 2026-02-16T09:20:50.416764
---

# Erlang/Elixir

# Erlang/Elixir

* Latest Dynatrace
* Reference
* 1-min read
* Published Dec 20, 2022

You can send data from your Erlang/Elixir application to Dynatrace via OpenTelemetry. See also

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-erlang-contrib) for capturing traces.

  + [Instrument your Erlang application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/erlang "Learn how to instrument your Erlang application using OpenTelemetry and Dynatrace.")
  + [Instrument your Elixir application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/elixir "Learn how to instrument your Elixir application using OpenTelemetry and Dynatrace.")


---


## Source: supported-go-versions.md


---
title: Supported Go versions
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/go/support/supported-go-versions
scraped: 2026-02-16T09:21:18.438662
---

# Supported Go versions

# Supported Go versions

* Latest Dynatrace
* 7-min read
* Updated on Feb 06, 2026

Whenever a new Go major version is released, Dynatrace adds support for that version. Support for each minor version is
added tooâsee [Version matrix](#go-version-matrix) for more details.

The [Go release policyï»¿](https://dt-url.net/uos3rmi) supports the last two major Go versions. However, Dynatrace decided
to support each Go version at least half a year longer so that you have enough time for upgrades.

### Official [Golang toolchainï»¿](https://dt-url.net/go)

Go version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

1.25

2025-08-12

2026-08-12

1.325

-

2027-08-12

Supported

1.24

2025-02-11

2026-02-11

1.311

-

2027-02-11

Supported

1.23

2024-08-13

2025-08-13

1.301

-

2026-08-13

Supported

1.22

2024-02-06

2025-02-06

1.287

-

2026-02-28

Supported

### Golang toolchain with FIPS ([openssl-fipsï»¿](https://dt-url.net/golang-fips)) modifications

Prerequisites

* **Go FIPS** OneAgent feature.

  To enable the feature, go to **Settings** > **Preferences** > **OneAgent features** and turn on **Go FIPS**.

Go version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

1.25.3

2025-08-12

2026-08-12

1.331

-

2027-08-12

Supported

1.24.6

2025-02-11

2026-02-11

1.325

-

2027-02-11

Supported

1.24.4

2025-02-11

2026-02-11

1.323

-

2027-02-11

Supported

1.23.9

2024-08-13

2025-08-13

1.323

-

2026-08-13

Supported

1.23.6

2024-08-13

2025-08-13

1.315

-

2026-08-13

Supported

1.22.9

2024-02-06

2025-02-06

1.309

-

2026-02-28

Supported

1.22.7

2024-02-06

2025-02-06

1.307

-

2026-02-28

Supported

## Version matrix

Each version range defines Go versions for which OneAgent has built-in support. The upper bound in parentheses specifies
the latest version that may be supported via [external metadata](#external-metadata).

| OneAgent versions | Go 1.22 | Go 1.23 | Go 1.24 | Go 1.25 |
| --- | --- | --- | --- | --- |
| v1.287 | 1.22.0 (1.22.5) |  |  |  |
| v1.289 | 1.22.0 - 1.22.1 (1.22.6) |  |  |  |
| v1.291 | 1.22.0 - 1.22.2 (1.22.6) |  |  |  |
| v1.293 | 1.22.0 - 1.22.3 (1.22.8) |  |  |  |
| v1.295 | 1.22.0 - 1.22.4 (1.22.8) |  |  |  |
| v1.297 | 1.22.0 - 1.22.5 (1.22.10) |  |  |  |
| v1.299 | 1.22.0 - 1.22.5 (1.22.12) |  |  |  |
| v1.301 | 1.22.0 - 1.22.6 (1.22.12) | 1.23.0 (1.23.6) |  |  |
| v1.303 | 1.22.0 - 1.22.8 (1.22.12) | 1.23.0 - 1.23.2 (1.23.8) |  |  |
| v1.305 | 1.22.0 - 1.22.8 (1.22.12) | 1.23.0 - 1.23.2 (1.23.8) |  |  |
| v1.307 | 1.22.0 - 1.22.10 (1.22.12) | 1.23.0 - 1.23.4 (1.23.9) |  |  |
| v1.309 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.6 (1.23.10) |  |  |
| v1.311 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.6 (1.23.11) | 1.24.0 (1.24.5) |  |
| v1.313 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.8 (1.23.12) | 1.24.0 - 1.24.2 (1.24.6) |  |
| v1.315 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.8 (1.23.12) | 1.24.0 - 1.24.2 (1.24.7) |  |
| v1.317 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.9 (1.23.12) | 1.24.0 - 1.24.3 (1.24.9) |  |
| v1.319 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.10 (1.23.12) | 1.24.0 - 1.24.4 (1.24.10) |  |
| v1.321 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.11 (1.23.12) | 1.24.0 - 1.24.5 (1.24.11) |  |
| v1.323 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.6 (1.24.12) |  |
| v1.325 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.7 (1.24.13) | 1.25.0 - 1.25.1 (1.25.7) |
| v1.327 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.9 (1.24.13) | 1.25.0 - 1.25.3 (1.25.7) |
| v1.329 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.10 (1.24.13) | 1.25.0 - 1.25.4 (1.25.7) |
| v1.331 | 1.22.0 - 1.22.12 | 1.23.0 - 1.23.12 | 1.24.0 - 1.24.11 (1.24.13) | 1.25.0 - 1.25.5 (1.25.7) |

### Older versions

| OneAgent versions | Go 1.18 | Go 1.19 | Go 1.20 | Go 1.21 |
| --- | --- | --- | --- | --- |
| v1.239 | 1.18.0 (1.18.5) |  |  |  |
| v1.241 | 1.18.0 - 1.18.1 (1.18.5) |  |  |  |
| v1.243 | 1.18.0 - 1.18.2 (1.18.7) |  |  |  |
| v1.245 | 1.18.0 - 1.18.3 (1.18.8) |  |  |  |
| v1.247 | 1.18.0 - 1.18.3 (1.18.10) |  |  |  |
| v1.249 | 1.18.0 - 1.18.5 (1.18.10) | 1.19.0 (1.19.5) |  |  |
| v1.251 | 1.18.0 - 1.18.5 (1.18.10) | 1.19.0 (1.19.5) |  |  |
| v1.253 | 1.18.0 - 1.18.7 (1.18.10) | 1.19.0 - 1.19.2 (1.19.7) |  |  |
| v1.255 | 1.18.0 - 1.18.7 (1.18.10) | 1.19.0 - 1.19.2 (1.19.7) |  |  |
| v1.257 | 1.18.0 - 1.18.8 (1.18.10) | 1.19.0 - 1.19.3 (1.19.8) |  |  |
| v1.259 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.5 (1.19.9) |  |  |
| v1.261 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.5 (1.19.10) |  |  |
| v1.263 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.7 (1.19.11) | 1.20.0 - 1.20.2 (1.20.6) |  |
| v1.265 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.7 (1.19.12) | 1.20.0 - 1.20.2 (1.20.7) |  |
| v1.267 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.8 (1.19.13) | 1.20.0 - 1.20.3 (1.20.8) |  |
| v1.269 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.9 (1.19.13) | 1.20.0 - 1.20.4 (1.20.10) |  |
| v1.271 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.10 (1.19.13) | 1.20.0 - 1.20.5 (1.20.11) |  |
| v1.273 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.11 (1.19.13) | 1.20.0 - 1.20.6 (1.20.12) |  |
| v1.275 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.12 (1.19.13) | 1.20.0 - 1.20.7 (1.20.13) |  |
| v1.277 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.8 (1.20.14) | 1.21.0 - 1.21.1 (1.21.7) |
| v1.279 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.10 (1.20.14) | 1.21.0 - 1.21.3 (1.21.8) |
| v1.281 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.11 (1.20.14) | 1.21.0 - 1.21.4 (1.21.9) |
| v1.283 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.12 (1.20.14) | 1.21.0 - 1.21.5 (1.21.10) |
| v1.285 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.13 (1.20.14) | 1.21.0 - 1.21.6 (1.21.11) |
| v1.287 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.7 (1.21.12) |
| v1.289 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.8 (1.21.13) |
| v1.291 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.9 (1.21.13) |
| v1.293 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.10 (1.21.13) |
| v1.295 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.11 (1.21.13) |
| v1.297 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.12 (1.21.13) |
| v1.299 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.12 (1.21.13) |
| from v1.301 | 1.18.0 - 1.18.10 | 1.19.0 - 1.19.13 | 1.20.0 - 1.20.14 | 1.21.0 - 1.21.13 |

## External metadata

OneAgent can support newer Go versions by requesting external metadata from the Dynatrace Cluster. After OneAgent has
received the external metadata, it can instrument an application that is based on a Go version for which OneAgent
doesn't have built-in support. A restart of the Go process is required.

The [version matrix](#go-version-matrix), therefore, has two different upper bounds in each version range. The built-in
Go versions are always supported, while the upper bound in parentheses may be supported if OneAgent can get the required
external metadata from the Dynatrace Cluster.

External metadata is published independently of the OneAgent release cycle and OneAgent will always receive the latest
available external metadata from the Dynatrace Cluster. This also means that in a staged environment, applications may
be instrumented in a later stage that were not instrumented in an earlier stage, because new metadata became available
in the meantime. If this behavior is undesirable, disable the OneAgent feature **Go external metadata** so that external
metadata is not used. You can find OneAgent features at **Settings** > **Preferences** > **OneAgent features**.


---


## Source: go.md


---
title: Go
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/go
scraped: 2026-02-16T09:21:43.526167
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


---


## Source: graalvm-native-image.md


---
title: GraalVM Native Image
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/graalvm-native-image
scraped: 2026-02-16T09:21:35.446372
---

# GraalVM Native Image

# GraalVM Native Image

* Latest Dynatrace
* 8-min read
* Published Jul 02, 2024

OneAgent version 1.295+ Dynatrace version 1.295+

[GraalVM Native Imageï»¿](https://www.graalvm.org/latest/docs/getting-started/) is designed to achieve high performance when running applications written in Java and other languages by pre-compiling Java code into native images. AOT-compiled native images contain only the Java code required at runtime and exclude everything else from the libraries and frameworks.

Dynatrace provides end-to-end distributed tracing for your native Java applications pre-compiled as GraalVM Native Image running in virtualized, containerized, and K8s environments. Dynatrace automatically discovers your native Java apps' services and visualizes their dependencies from the website to containers, infrastructure, and the cloud. It diagnoses anomalies in real-time using AI and determines the root cause down to the broken code. Performance metrics give you insight into memory usage, garbage collection, and threads.

For the supported distributed tracing technologies, see [Java Native Image](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Dynatrace GraalVM Native Image observability requires a [Full-Stack Monitoring](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") license.

## Get started

The Dynatrace GraalVM Native Image module consists of a **build-time module** and a **runtime module**. The build-time module must be present during Native Image build-time. The runtime module must be present when the Native Image is executed to capture telemetry data.

* Both modules must be of the same version for compatibility reasons.
* The Dynatrace environment version must be equal to or later than the version of the GraalVM Native modules.
* No changes to your application code are required.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Integrate Dynatrace in your project**](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#integration "Install, configure, and manage Dynatrace GraalVM Native Image module.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Activate Dynatrace observability**](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#activate "Install, configure, and manage Dynatrace GraalVM Native Image module.")

### Step 1 Integrate Dynatrace in your project

#### Maven projects

To integrate Dynatrace in a Maven project

1. Add the following to your `pom.xml` file:

   ```
   <profile>



   <id>dynatrace-native</id>



   <build>



   <plugins>



   <plugin>



   <groupId>com.dynatrace.buildtools.graalnative</groupId>



   <artifactId>dynatrace-native-maven-plugin</artifactId>



   <version>2.1.0</version>



   <executions>



   <execution>



   <goals>



   <goal>setup-build-agent</goal>



   <goal>copy-runtime-agent</goal>



   </goals>



   <configuration>



   <agentDownload>



   <environmentUrl>ENVIRONMENT_URL</environmentUrl>



   <apiToken>API_TOKEN</apiToken>



   </agentDownload>



   </configuration>



   </execution>



   </executions>



   <extensions>true</extensions>



   </plugin>



   </plugins>



   </build>



   </profile>
   ```

   Replace `ENVIRONMENT_URL` and `API_TOKEN` according to your Dynatrace environment:

   * `ENVIRONMENT_URL` is the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * `API_TOKEN` is your access token and can, for example, be provided with an environment variable by using `<apiToken>${env.DT_API_TOKEN}</apiToken>`. This access token requires the **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").

   This will automatically download and use the latest GraalVM Native Image module version available in your environment. To use a specific GraalVM Native Image module version, add `<agentVersion>AGENT_VERSION</agentVersion>` to the `agentDownload` configuration.

   Alternatively, you can also [manually download the GraalVM Native Image module](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#manual-agent-download "Install, configure, and manage Dynatrace GraalVM Native Image module.") and use

   ```
   <configuration>



   <agentZip>PATH_TO_DOWNLOADED_ZIP</agentZip>



   </configuration>
   ```

   to configure the Dynatrace plugin. Replace `PATH_TO_DOWNLOADED_ZIP` with the absolute or relative path to the downloaded ZIP file.
2. Run `mvnw package -Pnative -Pdynatrace-native`. This will generate a Native Image, including Dynatrace. The `native` profile adds the [Maven plugin for GraalVM Native image buildingï»¿](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-registering-plugin).

   Typically, the resulting Native Image will be available in the `target` folder. In addition to the Native Image, there will be a `dynatrace` folder. It is required for monitoring at runtime. If you want to run the Native Image on another machine, copy the `dynatrace` folder along with the Native Image.

#### Gradle projects

Prerequisites

* Gradle 8.4+ runs on a supported [JVM](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") or [Native Image](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.") of Java version 17+.
* Gradle plugin `org.graalvm.buildtools:native-gradle-plugin` with version 0.10+ is applied to your project.

To integrate Dynatrace in a Gradle project

1. Add the following code to `settings.gradle`:

   ```
   pluginManagement {



   repositories {



   mavenCentral()



   }



   }
   ```
2. Add the following code to `build.gradle`:

   ```
   plugins {



   id 'com.dynatrace.buildtools.graalnative' version '2.1.0'



   }



   dynatrace {



   agentDownload {



   environmentUrl = "ENVIRONMENT_URL"



   apiToken = "API_TOKEN"



   }



   }
   ```

   Replace `ENVIRONMENT_URL` and `API_TOKEN` according to your Dynatrace environment:

   * `ENVIRONMENT_URL` is the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
   * `API_TOKEN` is your access token and can, for example, be provided with an environment variable by using `System.getenv("DT_API_TOKEN")`. This access token requires the **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").

   This will automatically download and use the latest GraalVM Native Image module version available in your environment. To use a specific GraalVM Native Image module version, add `agentVersion = "AGENT_VERSION"` to the `agentDownload` configuration.

   Alternatively, you can also [manually download the GraalVM Native Image module](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image#manual-agent-download "Install, configure, and manage Dynatrace GraalVM Native Image module.") and use

   ```
   dynatrace {



   agentZip = "PATH_TO_DOWNLOADED_ZIP"



   }
   ```

   to configure the Dynatrace plugin. Replace `PATH_TO_DOWNLOADED_ZIP` with the absolute or relative path to the downloaded ZIP file.
3. Run `gradlew dynatraceNativeCompile` to generate a Native Image, including Dynatrace.

   Typically, the resulting Native Image is available in the folder `build/native/nativeCompile`. In addition to the Native Image, the folder contains a `dynatrace` folder. It is required for monitoring at runtime. If you want to run the Native Image on another machine, copy the `dynatrace` folder along with the Native Image.

#### Manually downloading the GraalVM Native Image module

You can also manually download the GraalVM Native Image module from [Dynatrace OneAgent Deployment API](/docs/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.") for your target platform.

An example API call using `curl`:

```
curl -X GET "$DT_TENANT_URL/api/v1/deployment/installer/agent/$OS_TYPE/paas/latest?flavor=default&arch=$ARCH&bitness=64&include=java-graal-native&skipMetadata=true" -H "accept: application/octet-stream"  -H "Authorization: Api-Token $DT_API_TOKEN" -o agent.zip
```

Replace `$DT_TENANT_URL`, `$OS_TYPE`, `$ARCH`, and `$DT_API_TOKEN` with your Dynatrace environment values.

* `$DT_TENANT_URL` is your Dynatrace environment URL.
* `$OS_TYPE` can be `unix` or `windows`.
* `$ARCH` can be `x86` or `arm`, while `arm` is only available for the OS type `unix`.
* `$DT_API_TOKEN` is your access token with the **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").

### Step 2 optional Activate Dynatrace observability

If you already have OneAgent installed or use Dynatrace Operator for Kubernetes, the Dynatrace connection details are automatically applied and GraalVM Native Image observability activated.

To activate Dynatrace observability at runtime, define your Dynatrace connection details using the environment variables `DT_TENANT`, `DT_TENANTTOKEN`, and `DT_CONNECTION_POINT`. An example for Dynatrace SaaS:

```
export DT_TENANT=$DT_TENANT_ID



export DT_TENANTTOKEN=$DT_TENANTTOKEN



export DT_CONNECTION_POINT=$DT_CONNECTION_POINT



./$YOUR_APP_NAME
```

Replace `$DT_TENANT_ID`, `$DT_TENANTTOKEN`, and `$DT_CONNECTION_POINT` with your Dynatrace connection details. Replace `$YOUR_APP_NAME` with your application name.

You can retrieve your connection details via [View connectivity information for OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-connectivity-info "View the connectivity information of OneAgent via Dynatrace API.") API call. You need the following fields of the response:

* **tenantUUID** for `$DT_TENANT_ID`
* **tenantToken** for `$DT_TENANTTOKEN`
* **communicationEndpoints** for `$DT_CONNECTION_POINT`

## Plugin configuration

### Maven plugin

The Maven plugin is configured via the `dynatrace-native` profile in the `pom.xml` file. For example:

```
<configuration>



<agentDownload>



<environmentUrl>${env.DT_TENANT_URL}</environmentUrl>



<apiToken>${env.DT_API_TOKEN}</apiToken>



</agentDownload>



<agentOptions>loglevelcon=info</agentOptions>



</configuration>
```

You can configure the following properties:

* `agentDownload` is used to configure the automatic GraalVM Native Image module download:

  + `environmentUrl` specifies the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
  + `apiToken` specifies the access token with **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").
  + `agentVersion` specifies the GraalVM Native Image module version. If not set, the latest GraalVM Native Image module version is used.
* `agentZip` sets the absolute or relative path to the manually downloaded ZIP file.
* `agentOptions` defines the options for the Dynatrace build-time module (optional).

The following `agentOptions` are available:

* `loglevelcon` sets the console logging level. Possible values: `off` (default), `severe`, `warning`, and `info`.
* `agentconfigpath` sets the absolute path to a JSON configuration file (see the next section).

### Gradle plugin

The Gradle plugin is configured via a `dynatrace` block in `build.gradle`. For example:

```
dynatrace {



agentDownload {



environmentUrl = System.getenv("DT_TENANT_URL")



apiToken = System.getenv("DT_API_TOKEN")



}



agentOptions="loglevelcon=info"



}
```

You can configure the following properties:

* `agentDownload` is used to configure the automatic GraalVM Native Image module download:

  + `environmentUrl` specifies the Dynatrace environment URL of your [monitoring environment](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
  + `apiToken` specifies the access token with **PaaS integration - Installer download** scope. To learn how to generate the token, see [Generate access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.").
  + `agentVersion` specifies the GraalVM Native Image module version. If not set, the latest GraalVM Native Image module version is used.
* `agentZip` sets the absolute or relative path to the manually downloaded ZIP file.
* `agentOptions` defines the options for the Dynatrace build-time module (optional).

The following `agentOptions` are available:

* `loglevelcon` sets the console logging level. Possible values: `off` (default), `severe`, `warning`, and `info`.
* `agentconfigpath` sets the absolute path to a JSON configuration file (see the next section).

## GraalVM Native Image module configuration

### Build-time module

The Dynatrace build-time module is preconfigured with recommended settings. If needed, you can override the defaults via a JSON configuration file at build time. For example:

```
{



"enabledSensors": [



"servlet"



]



}
```

The following `enabledSensors` (instrumentation points) are available:

* `servlet`: Incoming HTTP requests via Servlet API
* `netty`: Incoming HTTP requests via Netty
* `httpclient`: Outgoing HTTP requests
* `threading`: Context propagation for threads and executors
* `mongo`: MongoDB database calls

Remove a sensor from the `enabledSensors` list to deactivate it.

### Runtime module

#### FIPS mode

FIPS mode is disabled by default. To enable FIPS mode for the runtime module, delete the `agent/dt_fips_disabled.flag` file in the `dynatrace` folder next to the Native Image.

## Known limitations

### Limited GraalVM Native Image module feature set

The GraalVM Native Image module does not have all the features of the regular Java module. The technologies supported by the GraalVM Native Image module can be found in the [Java Native Image](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.") section of the technology support page.

Furthermore, the GraalVM Native Image module currently does not support:

* Application Security, including runtime vulnerability analytics, and runtime application protection
* Real-time updates for Java services
* CPU profiling
* Memory profiling
* Memory dump analysis
* Built-in metricsâlimited support; suspension time metrics are not reported

### Spring RestTemplate

This is expected to be no longer necessary in GraalVM versions 17.0.12+, 21.0.4+, and 22.0.2+.

If you are using Spring RestTemplate and get unconnected traces, please try the following workaround.

#### Maven projects

Configure in your `pom.xml` file:

```
<jvmArgs>



<arg>--add-opens=java.base/sun.net.www.protocol.http=ALL-UNNAMED</arg>



<arg>--add-opens=java.base/java.net=ALL-UNNAMED</arg>



<arg>--add-exports=java.base/sun.net.www=ALL-UNNAMED</arg>



</jvmArgs>
```

For reference, see [Maven plugin for GraalVM Native Image buildingï»¿](https://graalvm.github.io/native-build-tools/latest/maven-plugin.html#configuration-options).

#### Gradle projects

Configure in your `build.gradle` file:

```
graalvmNative {



binaries {



main {



jvmArgs.addAll(



'--add-opens', 'java.base/sun.net.www.protocol.http=ALL-UNNAMED',



'--add-opens', 'java.base/java.net=ALL-UNNAMED',



'--add-exports', 'java.base/sun.net.www=ALL-UNNAMED'



)



}



}



}
```


---


## Source: set-up-event-and-memory-alerting.md


---
title: Out-of-memory (OOM) and out-of-threads (OOT) events and alerting
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting
scraped: 2026-02-16T09:39:59.510741
---

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting

* Latest Dynatrace
* 2-min read
* Updated on Jan 10, 2024

To set up out-of-memory (OOM) and out-of-threads (OOT) events for standalone/PaaS scenarios and cloud-native Full-Stack injections, follow the instructions below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Enable the OneAgent feature**](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#enable-feature "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create metric events**](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#create-metrics "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")

## Step 1 Enable the OneAgent feature

To enable out-of-memory (OOM) and out-of-threads (OOT) detection

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Find and turn on **Enable Out-Of-Memory and Out-Of-Thread Detection for Kubernetes and PaaS installations**.
3. Select **Save changes**.

## Step 2 Set up high GC activity alerts

If you've already set up alerts for [high GC activity](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection#hosts "Configure host anomaly detection, including problem and event thresholds.") in your environment, alerts are automatically created for standalone/PaaS scenarios and cloud-native Full-Stack injections.

To verify your setup

1. Go to **Settings** > **Anomaly detection** and select **Hosts**.
2. Make sure that **Detect high GC activity** is turned on.

   If you're using a customized setup for [long garbage-collection times alerts](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events#long-garbage-collection-time "Learn more about resource events and the logic behind raising them."), note that, for standalone/PaaS scenarios and cloud-native Full-Stack injections, data collected in 10-second observation intervals is adjusted to one-minute observation intervals.

Alternatively, you can create alerts only for specific metric events.

1. Go to **Settings** > **Anomaly detection** and select **Metric events**.
2. Select **Add metric event**.
3. Define the following two events.

   Metric event

   Metric key

   Threshold

   Violating samples

   Sliding window

   Dealerting samples

   High GC suspension time

   `builtin:tech.jvm.memory.gc.suspensionTime`

   25 %

   3

   5

   4

   High GC total collection time

   `builtin:tech.jvm.memory.gc.collectionTime`

   24 s

   3

   5

   4
4. Select **Save changes**.

## Related topics

* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
* [Static thresholds for infrastructure monitoring](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure "Learn about the fixed thresholds used by Dynatrace to determine when a detected slowdown or error-rate increase justifies the generation of a new problem event.")


---


## Source: java.md


---
title: Java
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java
scraped: 2026-02-16T09:21:26.738874
---

# Java

# Java

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 23, 2025

Incompatibility alert

Using both the [SAP Introscope Agentï»¿](https://dt-url.net/ut039c3) and Dynatrace OneAgent on the same JVM is not supported. Dynatrace OneAgent, when active on the same host, can silently block the Introscope Agent, preventing it from operating as expected.

Dynatrace fully supports Java as well as all major JVMs and JDKs, providing extensive Java monitoring capabilities:

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-java/) for capturing traces and ingesting metrics.  
  For more information, see [Instrument your Java application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/java "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")
* End-to-end [transaction tracing](/docs/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") of requests to web services, remoting services, JMS, and RabbitMQ
* [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing
* Insight into SQL databases (via JDBC) and NoSQL databases such as MongoDB, Cassandra, and Redis
* Heap, garbage collection, thread, JMX, process metrics, and much more
* Memory dump analysisâDynatrace supports [memory dumps](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.") for the Oracle JVM, OpenJDK, and IBM JVM
* Always-on, 24/7, production-grade CPU profiling (including support for virtual threads)
* [Continuous thread analysis](/docs/observe/application-observability/profiling-and-optimization/continuous-thread-analysis "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") for application, JVM, and agent threads (JVM thread analysis limited to Java 8 and Java 17+)

Dynatrace also supports GraalVM Native Images, providing extensive Java monitoring capabilities:

* End-to-end distributed tracing for HTTP requests all the way to databases.
* Code-level visibility for your applications to troubleshoot issues.
* Resource contention analysis with garbage collection and thread metrics.

See our supported technologies matrix for details about the supported [JVMs](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Native Images](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Topics

* [Support for JVMs](/docs/ingest-from/technology-support/application-software/java/support-for-jvms "Find out the major JVMs and JDKs that are supported by Dynatrace.")
* [G1 Garbage Collector â Java 9](/docs/ingest-from/technology-support/application-software/java/g1-garbage-collector-java-9 "Learn how the G1 works compared to other collectors and why it can easily outperform other state-of-the-art garbage collectors on large heaps.")
* [Top Java memory problems](/docs/ingest-from/technology-support/application-software/java/top-java-memory-problems "Learn about Java memory issues such as memory leaks, high memory usage, class loader problems, and GC configuration.")
* [Out-of-memory (OOM) and out-of-threads (OOT) events and alerting](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")
* [GraalVM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.")
* [Red Hat Quarkus native applications monitoring](/docs/ingest-from/technology-support/application-software/java/quarkus "Monitor Red Hat Quarkus native applications with Dynatrace on hosts that are monitored by OneAgent.")


---


## Source: kong-gateway.md


---
title: Kong Gateway monitoring
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nginx/kong-gateway
scraped: 2026-02-16T09:20:13.796904
---

# Kong Gateway monitoring

# Kong Gateway monitoring

* Latest Dynatrace
* 4-min read
* Updated on Sep 04, 2024

To enable Kong Observability in Dynatrace, you have the following options.

* Recommended Enable OneAgent for Gateway logs, traces, and process monitoring. This should be combined with Dynatrace Prometheus scraping to monitor Kong Gateway metrics.
* Monitor Kong using a combination of OpenTelemetry for traces and Prometheus for Kong Gateway metrics.

OneAgent

OpenTelemetry

## Kong Gateway process and logs

OneAgent automatically monitors the Kong Gateway process and logs.

### Prerequisites

* Kong Gateway version 2.8+
* OneAgent or Dynatrace Operator is installed and available for monitoring your Kong Gateway.

The required installation depends on your application:

| If your application is running | See the instruction for |
| --- | --- |
| on a virtual machine or bare-metal | [OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation "Install OneAgent on a server for the very first time.") |
| as workload in Kubernetes or OpenShift | [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") |

## Application traces

In addition to process and logs, OneAgent also provides Kong Gateway application traces. See [Manual runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") for NGINX.

## Step 1 Configure Kong Gateway

### Prerequisites

* Kong Gateway version 3.8+

Kong Gateway requires the configuration of two settings.

* `tracing_instrumentations = all`
* `tracing_sampling_rate = 1.0`

For further details and option, see the [Kong Gateway documentationï»¿](https://dt-url.net/2m03q66).

## Step 2 Configure OpenTelemetry plugin

1. Evaluate support for logging and tracing according to the [OpenTelemetry plugin versionï»¿](https://dt-url.net/1423wjw) installed in your environment.
2. Send the following POST request (example assumes Kong Gateway 3.8+) by replacing `{HOST}`, `{PLUGIN-INSTANCE_NAME}` and `{OPENTELEMETRY_COLLECTOR}` with proper values:

```
curl -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "opentelemetry",



"instance_name": "{PLUGIN-INSTANCE_NAME}",



"config": {



"traces_endpoint": "http://{OPENTELEMETRY_COLLECTOR}:4318/v1/traces",



"logs_endpoint": "http://{OPENTELEMETRY_COLLECTOR}:4318/v1/logs",



"resource_attributes": {



"service.name": "kong-dev"



}



}



}'
```

## Step 3 Configure OpenTelemetry Collector

Configure your OpenTelemetry Collector to send data to your Dynatrace environment. The example below shows how to export traces and logs.

```
receivers:



otlp:



protocols:



http:



endpoint: 0.0.0.0:4318



exporters:



otlp_http:



endpoint: "${env:DT_BASEURL}/api/v2/otlp"



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

## Step 3 Export Application Span Metrics

To include span metrics for application traces, configure the collector exporters section of the OpenTelemetry Collector configuration.

```
connectors:



spanmetrics:



dimensions:



- name: http.method



default: GET



- name: http.status_code



- name: http.route



exclude_dimensions:



- status.code



metrics_flush_interval: 15s



histogram:



disable: false



service:



pipelines:



traces:



receivers: [otlp]



processors: []



exporters: [spanmetrics]



metrics:



receivers: [spanmetrics]



processors: []



exporters: [otlp_http]
```

## Metrics

Kongâs Prometheus plugin is a convenient way to collect Kong Gateway metrics. Dynatrace can collect these metrics directly from the Gateway produced by the Kong plugin. The default port and endpoint is `8001/metrics`.

For more information and a list of available metrics, see the [Kong Prometheus plugin documentationï»¿](https://dt-url.net/gp23qq7).

## Step 1 Enable Kong Prometheus plugin

### Basic configuration

To enable basic configuration of the Kong Prometheus plugin send a POST request replacing `{HOST}` with the host name value.

```
curl -s -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "prometheus"



}'
```

### Additional plugin metrics

To enable additional metrics produced by the Kong Gateway Prometheus plugin, send a POST request replacing `{HOST}` and `{PLUGIN-INSTANCE_NAME}` with proper values:

```
curl -s -X POST http://{HOST}:8001/plugins \



-H 'Content-Type: application/json' \



-d '{



"name": "prometheus",



"instance_name": "{PLUGIN-INSTANCE_NAME}",



"config": {



"per_consumer": true,



"status_code_metrics": true,



"latency_metrics": true,



"bandwidth_metrics": true,



"upstream_health_metrics": true



}



}'
```

To check available Kong metrics, query the `/metrics` endpoint:

```
curl -i http://{HOST}:8001/metrics
```

## Step 2 Collect Prometheus metrics

After configuring [Kong Gateway's Prometheus pluginï»¿](https://dt-url.net/gp23qq7), metrics can be collected using the Dynatrace ActiveGate (recommended) or the OpenTelemetry Collector.

ActiveGate

OpenTelemetry Collector

### Scrape metrics using ActiveGate

In Kubernetes, Dynatrace supports scraping of Prometheus endpoints using special annotations.

To learn how to collect Prometheus metrics in Kubernetes, see [Monitor Prometheus metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.").

### Scrape metrics using OpenTelemetry Collector

You can also use the OpenTelemetry Collectorâs Prometheus receiver to collect metrics from the Kong Gateway. To learn how to scrape Prometheus data using an OpenTelemetry collector, see [Scrape Promethus metrics with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.").

If you're running on Kubernetes, you can enrich traces, metrics, and logs using the Collector's Kubernetes attribute processor. This allows Dynatrace to map the telemetry data to the correct toplogy. To learn how to enable enrichment in the OpenTelemetry Collector, see [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.").


---


## Source: manual-runtime-instrumentation.md


---
title: Runtime instrumentation
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation
scraped: 2026-02-16T09:20:28.971206
---

# Runtime instrumentation

# Runtime instrumentation

* Latest Dynatrace
* 2-min read
* Updated on Oct 26, 2022

The NGINX code module relies on ahead-of-time assumptions about the internal NGINX data structure declarations and their layout in the memory during its automatic instrumentation. If the underlying data structure declarations are patched (meaning the source code defining these structures has been modified) and hence the ahead-of-time assumptions are invalid, the automatic instrumentation done by the code module may cause problems on NGINX due to reading from, or writing to, wrong parts of the memory.

To avoid such a scenario, the NGINX code module tries to detect patched NGINX data structure declarations. If a patched declaration is detected, the code module disables its automatic instrumentation and shows the following note on the process page in the web UI:

Notification

* Incompatible NGINX modules were detected in this process. Automatic instrumentation was disabled. To force instrumenting NGINX, see [Runtime instrumentation](/docs/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.").

## Instrument a patched NGINX

NGNIX Code Module can instrument a patched NGINX for [supported versions](/docs/ingest-from/technology-support/application-software/nginx#nginx-versions "Learn the details of Dynatrace support for NGINX.") by inspecting internal NGINX data structure declarations on startup (during runtime), instead of relying on ahead-of-time assumptions.

An example of a patched NGINX is the NGINX binary distributed with the Kong Gateway.

As patches can significantly alter the internal workings of NGINX, there is no guarantee that NGINX instrumented with runtime instrumentation will work as expected. Consider the following limitations.

Runtime instrumentation limitations

* The runtime instrumentation depends on debug symbols being available for the NGINX binary, which is not always the case.
* The runtime instrumentation adds a notable startup delay (10 seconds or more) to NGINX.
* The runtime instrumentation on Linux ARM64 requires OneAgent version 1.313+.

  My NGINX or Kong Pod in Kubernetes is not starting up due to a timeout

  In cloud deployments, adjust your Pod or container startup timeouts to prevent NGINX from running into a timeout when starting up.

  If an NGINX or Kong pod in Kubernetes is not starting up, look for a mention of failing liveness or readiness probes in the logs, and adjust the initial delay, timeout, and failure threshold values of these probes to high enough values. The exact configuration depends on the deployment.
* The runtime instrumentation requires more memory during the startup of NGINX. This higher peak memory consumption can lead to Pods being killed by Kubernetes (or other container runtimes) in case of strict memory limits. Please adjust your memory limits to accommodate runtime instrumentation.

To force instrumenting a patched NGINX during runtime

1. Add the environment variable `DT_NGINX_FORCE_RUNTIME_INSTRUMENTATION` to your NGINX:

```
DT_NGINX_FORCE_RUNTIME_INSTRUMENTATION=on
```

2. Restart your NGINX to pick up the environment variable.


---


## Source: nginx.md


---
title: NGINX
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nginx
scraped: 2026-02-16T09:21:08.397789
---

# NGINX

# NGINX

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Oct 23, 2025

With the NGINX code module of OneAgent, you can get observability for your NGINX instances and processed web requests.

Observability for

Including

Incoming web requests

All incoming web requests to NGINX

Outgoing web requests

Outgoing web requests originating from a [supported module of NGINX](#nginx-supported-modules)

NGINX HTTP connection metrics

* Traffic and requests
* Response sizes
* Accepted, active, and dropped connections

NGINX Plus metrics

Server zones

* Traffic and requests per server zone

Upstreams

* Traffic and requests
* Upstream health

Caches

* Cache performance
* Cache usage

Support on Windows

NGINX deep monitoring is currently not supported on Windows.

See [OneAgent support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#os-code-modules "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") for more details.

Which modules of NGINX are supported for outgoing web requests?

| Modules of NGINX | Versions |
| --- | --- |
| ngx\_http\_fastcgi\_module (fastcgi\_pass) | All versions supported |
| ngx\_http\_grpc\_module (grpc\_pass) | All versions supported |
| ngx\_http\_memcached\_module (memcached\_pass) | All versions supported |
| ngx\_http\_proxy\_module (proxy\_pass) | All versions supported |
| ngx\_http\_scgi\_module (scgi\_pass) | All versions supported |
| ngx\_http\_uwsgi\_module (uwsgi\_pass) | All versions supported |

## Support lifecycle

Dynatrace supports a variety of NGINX, NGINX Plus, OpenResty, and Tengine versions, see the tables below. A notification appears on the NGINX process page in the Dynatrace web UI if an attempt is made to instrument an unsupported version.

If your OneAgent build date is newer than a specific NGINX release date, the NGINX code module may be able to instrument your NGINX release even if it's not listed in the supported version tables.

Where I can find the OneAgent build date?

The OneAgent build date is part of the OneAgent intaller version, for example 1.254.0.**20221012-201831**.

### Support for NGINX

Support for the latest NGINX release is typically included in the next subsequent OneAgent releases.

NGINX version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

1.29.4

2025-12-09

-

1.331

-

-

Supported

1.29.3

2025-10-28

-

1.329

-

-

Supported

1.29.2

2025-10-07

-

1.327

-

-

Supported

1.29.1

2025-08-13

-

1.325

-

-

Supported

1.29.0

2025-06-24

-

1.321

-

-

Supported

1.28.1

2025-12-23

-

1.333

-

-

Not supported

1.28.0

2025-04-23

-

1.315

-

-

Supported

1.27.5

2025-04-16

-

1.313

-

-

Supported

1.27.4

2025-02-05

-

1.309

-

-

Supported

1.27.3

2024-11-26

-

1.307

-

-

Supported

1.27.2

2024-10-02

-

1.305

-

-

Supported

1.27.1

2024-08-14

-

1.297

-

-

Supported

1.27.0

2024-05-29

-

1.297

-

-

Supported

1.26.3

2025-02-05

-

1.309

-

-

Supported

1.26.2

2024-08-14

-

1.297

-

-

Supported

1.26.1

2024-05-29

-

1.297

-

-

Supported

1.26.0

2024-04-23

-

1.293

-

-

Supported

1.25.5

2024-04-16

-

1.293

-

-

Supported

1.25.4

2024-02-14

-

1.289

-

-

Supported

1.25.3

2023-10-25

-

1.277

-

-

Supported

1.25.2

2023-08-15

-

1.277

-

-

Supported

1.25.1

2023-06-13

-

1.271

-

-

Supported

1.25.0

2023-05-23

-

1.271

-

-

Supported

1.24.0

2023-04-11

-

1.265

-

-

Supported

1.23.4

2023-03-28

-

1.265

-

-

Supported

1.23.3

2022-12-13

-

1.259

-

-

Supported

1.23.2

2022-10-19

-

1.255

-

-

Supported

1.23.1

2022-07-19

-

1.249

-

-

Supported

1.23.0

2022-06-21

-

1.247

-

-

Supported

1.22.1

2022-10-19

-

1.255

-

-

Supported

1.22.0

2022-05-24

-

1.245

-

-

Supported

1.21.6

2022-01-25

-

1.237

-

-

Supported

1.21.5

2021-12-28

-

1.235

-

-

Supported

1.21.4

2021-11-02

-

1.233

-

-

Supported

1.21.3

2021-09-07

-

1.229

-

-

Supported

1.21.2

2021-08-31

-

1.229

-

-

Supported

1.21.1

2021-06-06

-

1.225

-

-

Supported

1.21.0

2021-05-25

-

1.221

-

-

Supported

1.20.2

2021-11-16

-

1.233

-

-

Supported

1.20.1

2021-05-25

-

1.221

-

-

Supported

1.20.0

2021-04-20

-

1.215

-

-

Supported

1.19.10

2021-04-10

-

1.215

-

-

Supported

1.19.9

2021-03-30

-

1.215

-

-

Supported

1.19.8

2021-03-09

-

1.213

-

-

Supported

1.19.7

2021-02-16

-

1.211

-

-

Supported

1.19.6

2020-12-15

-

1.209

-

-

Supported

1.19.5

2020-11-24

-

1.207

-

-

Supported

1.19.4

2020-10-27

-

1.205

-

-

Supported

1.19.3

2020-09-29

-

1.203

-

-

Supported

1.19.2

2020-08-11

-

1.199

-

-

Supported

1.19.1

2020-07-07

-

1.197

-

-

Supported

1.19.0

2020-05-26

-

1.193

-

-

Supported

1.17.10 - 1.18.0

2020-04-14

-

1.191

-

-

Supported

1.17.9

2020-03-03

-

1.189

-

-

Supported[1](#fn-nginx-1-def)

1.17.8

2020-01-21

-

1.183

-

-

Supported[1](#fn-nginx-1-def)

1.17.7

2019-12-24

-

1.181

-

-

Supported[1](#fn-nginx-1-def)

1.17.4 - 1.17.6

2019-09-24

-

1.175

-

-

Supported[1](#fn-nginx-1-def)

1.16.1 - 1.17.3

2019-08-13

-

1.173

-

-

Supported[1](#fn-nginx-1-def)

1.15.11 - 1.16.0

2019-04-09

-

1.163

-

-

Supported[1](#fn-nginx-1-def)

1.15.9 - 1.15.10

2019-02-26

-

1.161

-

-

Supported[1](#fn-nginx-1-def)

1.14.1 - 1.15.8

2018-11-06

-

1.159

-

-

Supported[1](#fn-nginx-1-def)

1.13.9 - 1.14.0

2018-02-20

-

1.143

-

-

Supported[1](#fn-nginx-1-def)

1.11.5 - 1.13.8

2016-10-11

-

1.137

-

-

Supported[1](#fn-nginx-1-def)

1.4 - 1.11.4

2013-04-24

-

-

-

2023-03-31

Not supported[2](#fn-nginx-2-def)

1

Support for the CPU architecture PPCLE was added with OneAgent version 1.169 and ARM64 (AArch64) with OneAgent version 1.189.

2

Supported if the used binary is in the list of [supported binaries](/docs/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries "Learn the details of Dynatrace support for NGINX.") or the corresponding debug information is available locally.

Support details for NGINX versions 1.4 - 1.11.4

The NGINX code module uses debug information from the NGINX packages for instrumenting NGINX. Standard NGINX package sources are regularly discovered by Dynatrace to support new binaries. If you use other binaries (for example, custom builds), you need to provide their debug packages locally.

The following image can help you to determine if a NGINX release is qualified for support:

![NGINX supported versions](https://dt-cdn.net/images/nginx-instrumentation-simplified-1800-9148ec25fc.png)

Supported binaries for which Dynatrace has debug information available

##### http://archive.ubuntu.com/ubuntu/pool/main/n/nginx

* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.0-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.1-0ubuntu5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.2-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.2-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.04.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.10.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu0.16.10.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.10.3-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.6\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.6\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.9\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3.9\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.4.6-1ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.6.2-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.6.2-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.6.2-5ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.6.2-5ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.6.2-5ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.6.2-5ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.10-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.10-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.11-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.11-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.12-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.12-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.13-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.13-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.14-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.14-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.15-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.15-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.3-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.3-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.3-1ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.3-1ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.3-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.3-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.9-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.9-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.9-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/main/n/nginx/nginx-core\_1.9.9-1ubuntu1\_i386.deb

##### http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx

* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.1.19-1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.1.19-1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.1.19-1ubuntu0.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.1.19-1ubuntu0.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.1.19-1ubuntu0.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.1.19-1ubuntu0.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.0-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.1-0ubuntu5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.2-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.2-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.04.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.10.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu0.16.10.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.10.3-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.6\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.6\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.9\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3.9\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.4.6-1ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.6.2-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.6.2-5ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.6.2-5ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.6.2-5ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.6.2-5ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.10-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.10-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.11-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.11-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.12-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.12-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.13-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.13-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.14-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.14-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.15-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.15-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.3-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.3-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.3-1ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.3-1ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.3-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.3-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.9-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.9-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.9-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-extras\_1.9.9-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.1.19-1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.1.19-1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.1.19-1ubuntu0.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.1.19-1ubuntu0.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.1.19-1ubuntu0.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.1.19-1ubuntu0.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.0-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.1-0ubuntu5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.2-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.2-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.04.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.10.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu0.16.10.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.10.3-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.6\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.6\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.9\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3.9\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.4.6-1ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.6.2-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.6.2-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.6.2-5ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.6.2-5ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.6.2-5ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.6.2-5ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.10-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.10-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.11-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.11-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.12-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.12-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.13-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.13-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.14-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.14-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.15-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.15-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.3-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.3-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.3-1ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.3-1ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.3-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.3-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.9-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.9-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.9-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-full\_1.9.9-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.1.19-1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.1.19-1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.1.19-1ubuntu0.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.1.19-1ubuntu0.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.1.19-1ubuntu0.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.1.19-1ubuntu0.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.0-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.1-0ubuntu5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.2-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.2-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.04.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.10.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu0.16.10.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.10.3-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.6\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.6\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.9\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3.9\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.4.6-1ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.6.2-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.6.2-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.6.2-5ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.6.2-5ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.6.2-5ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.6.2-5ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.10-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.10-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.11-0ubuntu2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.11-0ubuntu2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.12-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.12-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.13-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.13-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.14-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.14-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.15-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.15-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.3-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.3-1ubuntu1.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.3-1ubuntu1.2\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.3-1ubuntu1.2\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.3-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.3-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.9-0ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.9-0ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.9-1ubuntu1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-light\_1.9.9-1ubuntu1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.1.19-1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.1.19-1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.1.19-1ubuntu0.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.1.19-1ubuntu0.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.1.19-1ubuntu0.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.1.19-1ubuntu0.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.1\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.4\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.4\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.5\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.5\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.6\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.6\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.7\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.7\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.8\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.8\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.9\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3.9\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.4.6-1ubuntu3\_i386.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.6.2-1ubuntu1.1\_amd64.deb
* http://archive.ubuntu.com/ubuntu/pool/universe/n/nginx/nginx-naxsi\_1.6.2-1ubuntu1.1\_i386.deb

##### http://archive.webtatic.com/yum/el6-archive/x86\_64

* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx16-1.6.0-1.w6.x86\_64.rpm
* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx16-1.6.0-2.w6.x86\_64.rpm
* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx16-1.6.1-1.w6.x86\_64.rpm
* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx16-1.6.2-1.w6.x86\_64.rpm
* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx16-1.6.3-1.w6.x86\_64.rpm
* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx18-1.8.0-1.w6.x86\_64.rpm
* http://archive.webtatic.com/yum/el6-archive/x86\_64/nginx18-1.8.1-1.w6.x86\_64.rpm

##### http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS

* http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS/nginx16-1.6.0-2.w7.x86\_64.rpm
* http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS/nginx16-1.6.1-1.w7.x86\_64.rpm
* http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS/nginx16-1.6.2-1.w7.x86\_64.rpm
* http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS/nginx16-1.6.3-1.w7.x86\_64.rpm
* http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS/nginx18-1.8.0-1.w7.x86\_64.rpm
* http://archive.webtatic.com/yum/el7-archive/x86\_64/RPMS/nginx18-1.8.1-1.w7.x86\_64.rpm

##### http://dl.fedoraproject.org/pub/epel/6/i386

* http://dl.fedoraproject.org/pub/epel/6/i386/nginx-1.0.15-12.el6.i686.rpm
* http://dl.fedoraproject.org/pub/epel/6/i386/nginx-1.10.1-1.el6.i686.rpm
* http://dl.fedoraproject.org/pub/epel/6/i386/nginx-1.10.2-1.el6.i686.rpm

##### http://dl.fedoraproject.org/pub/epel/6/x86\_64

* http://dl.fedoraproject.org/pub/epel/6/x86\_64/nginx-1.0.15-12.el6.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/6/x86\_64/nginx-1.10.1-1.el6.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/6/x86\_64/nginx-1.10.2-1.el6.x86\_64.rpm

##### http://dl.fedoraproject.org/pub/epel/7/x86\_64/Packages/n

* http://dl.fedoraproject.org/pub/epel/7/x86\_64/Packages/n/nginx-1.10.2-2.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/Packages/n/nginx-1.12.2-1.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/Packages/n/nginx-1.12.2-2.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/Packages/n/nginx-1.12.2-3.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/Packages/n/nginx-1.16.1-1.el7.x86\_64.rpm

##### http://dl.fedoraproject.org/pub/epel/7/x86\_64/n

* http://dl.fedoraproject.org/pub/epel/7/x86\_64/n/nginx-1.10.1-1.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/n/nginx-1.10.2-1.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/n/nginx-1.6.3-6.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/n/nginx-1.6.3-7.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/n/nginx-1.6.3-8.el7.x86\_64.rpm
* http://dl.fedoraproject.org/pub/epel/7/x86\_64/n/nginx-1.6.3-9.el7.x86\_64.rpm

##### http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64

* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.10.0-1ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.10.0-2\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.10.0-3\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.10.3-10ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.10.3-8ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.14.0-1ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.8.0-8ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.8.0-9ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/Debian\_8.0/amd64/nginx-custom\_1.8.1-1ppa\_amd64.deb

##### http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64

* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.10.0-1ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.10.0-2\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.10.0-3\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.10.3-10ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.10.3-8ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.14.0-1ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.8.0-8ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.8.0-9ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.04/amd64/nginx-custom\_1.8.1-1ppa\_amd64.deb

##### http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64

* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.10.0-1ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.10.0-2\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.10.0-3\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.10.3-10ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.10.3-8ppa~stable\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.8.0-8ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.8.0-9ppa\_amd64.deb
* http://download.opensuse.org/repositories/home:/rtCamp:/EasyEngine/xUbuntu\_14.10/amd64/nginx-custom\_1.8.1-1ppa\_amd64.deb

##### http://download.opensuse.org/repositories/openSUSE:/Backports:/SLE-12/standard/x86\_64

* http://download.opensuse.org/repositories/openSUSE:/Backports:/SLE-12/standard/x86\_64/nginx-1.13.9-12.1.x86\_64.rpm
* http://download.opensuse.org/repositories/openSUSE:/Backports:/SLE-12/standard/x86\_64/nginx-1.14.2-16.1.x86\_64.rpm
* http://download.opensuse.org/repositories/openSUSE:/Backports:/SLE-12/standard/x86\_64/nginx-1.8.1-5.1.x86\_64.rpm
* http://download.opensuse.org/repositories/openSUSE:/Backports:/SLE-12/standard/x86\_64/nginx-1.8.1-9.1.x86\_64.rpm

##### http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586

* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.10.0-55.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.10.1-58.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.11.2-62.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.11.4-63.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.11.4-64.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.11.8-68.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.8.0-46.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.8.0-49.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/i586/nginx-1.8.1-52.1.i586.rpm

##### http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64

* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.10.0-55.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.10.1-58.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.11.2-62.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.11.4-63.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.11.4-64.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.11.8-68.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.8.0-46.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.8.0-49.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.1/x86\_64/nginx-1.8.1-52.1.x86\_64.rpm

##### http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586

* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.10.0-55.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.10.1-58.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.11.2-62.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.11.4-63.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.11.4-64.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.11.8-68.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.8.0-1.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.8.0-49.1.i586.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/i586/nginx-1.8.1-52.1.i586.rpm

##### http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64

* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.10.0-55.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.10.1-58.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.11.2-62.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.11.4-63.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.11.4-64.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.11.8-68.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.8.0-1.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.8.0-49.1.x86\_64.rpm
* http://download.opensuse.org/repositories/server:/http/openSUSE\_13.2/x86\_64/nginx-1.8.1-52.1.x86\_64.rpm

##### http://download.opensuse.org/tumbleweed/repo/oss/i586

* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.13.11-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.13.9-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.13.9-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-3.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-3.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-3.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-3.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.14.0-3.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.1-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.10-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.10-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.2-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.2-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.2-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.2-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.2-1.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.3-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.3-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.3-2.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.3-2.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.3-2.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.3-2.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.5-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.6-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.6-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.6-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.7-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.6.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.15.8-1.7.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.16.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.16.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.0-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.0-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.0-1.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.10-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.10-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.2-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.2-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.3-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.3-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.3-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.4-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.5-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.5-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.5-2.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.6-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.6-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.7-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.7-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.7-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.7-2.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.8-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.8-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.8-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.9-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.9-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.17.9-2.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.18.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.18.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.18.0-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.18.0-2.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.0-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.1-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.2-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.2-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.2-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.2-1.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.2-1.7.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.3-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.3-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.3-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.4-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.4-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.5-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.5-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.5-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.5-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.6-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.6-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.6-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.6-1.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.7-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.7-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.8-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.19.9-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.20.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.20.0-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/i586/nginx-1.20.0-2.3.i586.rpm

##### http://download.opensuse.org/tumbleweed/repo/oss/suse/i586

* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.10.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.10.1-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.10.1-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.10-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.12-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.2-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.2-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.4-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.4-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.4-2.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.4-2.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.4-2.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.8-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.8-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.9-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.9-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.11.9-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.12.0-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.12.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.12.0-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.12.0-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.1-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.1-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.3-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.3-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.3-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.3-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.5-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.6-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.6-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.6-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.6-1.4.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.7-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.7-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.7-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.7-1.5.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.7-2.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.9-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.9-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.13.9-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.8.0-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.8.0-1.3.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.8.1-1.1.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.8.1-1.2.i586.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/i586/nginx-1.8.1-1.3.i586.rpm

##### http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64

* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.10.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.10.1-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.10.1-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.10-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.12-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.2-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.2-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.4-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.4-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.4-2.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.4-2.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.4-2.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.8-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.8-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.9-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.9-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.11.9-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.12.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.12.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.12.0-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.12.0-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.1-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.1-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.3-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.3-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.3-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.3-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.5-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.5-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.6-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.6-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.6-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.6-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.7-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.7-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.7-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.7-1.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.7-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.9-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.9-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.13.9-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.8.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.8.0-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.8.1-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.8.1-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/suse/x86\_64/nginx-1.8.1-1.3.x86\_64.rpm

##### http://download.opensuse.org/tumbleweed/repo/oss/x86\_64

* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.13.11-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.13.9-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.13.9-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-3.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-3.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-3.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-3.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.14.0-3.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.1-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.10-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.10-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.2-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.2-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.2-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.2-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.2-1.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.3-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.3-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.3-2.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.3-2.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.3-2.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.3-2.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.5-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.6-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.6-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.6-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.7-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.6.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.15.8-1.7.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.16.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.16.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.0-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.0-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.0-1.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.10-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.10-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.2-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.2-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.3-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.3-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.3-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.4-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.5-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.5-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.5-2.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.6-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.6-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.7-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.7-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.7-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.7-2.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.8-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.8-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.8-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.9-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.9-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.17.9-2.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.18.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.18.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.18.0-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.18.0-2.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.0-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.0-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.1-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.2-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.2-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.2-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.2-1.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.2-1.7.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.3-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.3-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.3-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.4-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.4-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.5-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.5-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.5-1.3.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.5-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.6-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.6-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.6-1.4.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.6-1.5.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.7-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.7-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.8-1.2.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.19.9-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.20.0-1.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.20.0-2.1.x86\_64.rpm
* http://download.opensuse.org/tumbleweed/repo/oss/x86\_64/nginx-1.20.0-2.3.x86\_64.rpm

##### http://ftp.debian.org/debian/pool/main/n/nginx

* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.10.0-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.10.0-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.10.1-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.10.1-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.10.1-2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.10.1-2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.2-1~exp1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.2-1~exp1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.3-1~exp1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.3-1~exp1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.3-1~exp2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.3-1~exp2+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.3-1~exp2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.11.3-1~exp2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.2.1-2.2+wheezy3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.2.1-2.2+wheezy3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.2.1-2.2+wheezy4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.2.1-2.2+wheezy4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u1~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u1~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u2~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u2~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u5\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5+deb8u5\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.6.2-5~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.10-1~bpo8+4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.14-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.14-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.3-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.3-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.4-1+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.4-1+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.4-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.4-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.4-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.4-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.6-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.6-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.6-2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.6-2+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.6-2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.6-2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.9-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-extras\_1.9.9-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.10.0-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.10.0-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.10.1-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.10.1-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.10.1-2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.10.1-2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.2-1~exp1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.2-1~exp1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.3-1~exp1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.3-1~exp1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.3-1~exp2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.3-1~exp2+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.3-1~exp2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.11.3-1~exp2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.2.1-2.2+wheezy3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.2.1-2.2+wheezy3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.2.1-2.2+wheezy4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.2.1-2.2+wheezy4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u1~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u1~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u2~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u2~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u5\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5+deb8u5\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.6.2-5~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.10-1~bpo8+4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.14-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.14-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.3-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.3-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.4-1+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.4-1+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.4-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.4-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.4-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.4-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.6-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.6-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.6-2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.6-2+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.6-2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.6-2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.9-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-full\_1.9.9-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.10.0-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.10.0-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.10.1-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.10.1-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.10.1-2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.10.1-2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.2-1~exp1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.2-1~exp1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.3-1~exp1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.3-1~exp1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.3-1~exp2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.3-1~exp2+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.3-1~exp2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.11.3-1~exp2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.2.1-2.2+wheezy3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.2.1-2.2+wheezy3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.2.1-2.2+wheezy4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.2.1-2.2+wheezy4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u1~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u1~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u2~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u2~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u5\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5+deb8u5\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5~bpo70+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.6.2-5~bpo70+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.10-1~bpo8+4\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.14-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.14-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.3-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.3-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.4-1+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.4-1+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.4-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.4-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.4-1~bpo8+1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.4-1~bpo8+1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.6-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.6-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.6-2+b1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.6-2+b1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.6-2\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.6-2\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.9-1\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-light\_1.9.9-1\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-naxsi\_1.2.1-2.2+wheezy3\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-naxsi\_1.2.1-2.2+wheezy3\_i386.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-naxsi\_1.2.1-2.2+wheezy4\_amd64.deb
* http://ftp.debian.org/debian/pool/main/n/nginx/nginx-naxsi\_1.2.1-2.2+wheezy4\_i386.deb

##### http://nginx.org/packages/debian/pool/nginx/n/nginx

* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~squeeze\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~squeeze\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.0-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.0-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.0-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.1-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.1-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.1-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.2-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.2-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.2-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.2-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.3-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.3-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.3-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.10.3-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.0-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.0-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.0-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.0-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.0-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.1-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.1-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.1-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.1-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.1-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.2-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.2-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.2-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.12.2-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.0-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.0-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.0-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.0-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.1-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.1-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.1-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.1-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.2-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.2-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.2-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.14.2-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.16.0-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.16.0-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.16.0-1~stretch\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.16.0-1~stretch\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.0-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.0-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.0-1~squeeze\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.0-1~squeeze\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.0-1~wheezy\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.1-1~jessie\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.1-1~jessie\_i386.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/debian/pool/nginx/n/nginx/nginx\_1.8.1-1~wheezy\_i386.deb

##### http://nginx.org/packages/mainline/centos/5/i386/RPMS

* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.10-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.11-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.12-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.8-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.11.9-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.10-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.11-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.12-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.13-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.14-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.15-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.8-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-1.9.9-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/mainline/centos/5/i386/RPMS/nginx-debug-1.9.7-1.el5.ngx.i386.rpm

##### http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS

* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.10-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.11-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.12-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.8-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.11.9-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.10-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.11-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.12-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.13-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.14-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.15-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.8-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-1.9.9-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/5/x86\_64/RPMS/nginx-debug-1.9.7-1.el5.ngx.x86\_64.rpm

##### http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS

* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.10-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.11-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.12-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.13-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.7-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.8-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.11.9-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.10-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.11-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.12-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.6-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.7-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.8-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.13.9-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.0-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.1-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.10-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.11-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.12-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.2-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.3-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.4-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.5-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.6-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.7-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.8-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.15.9-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.10-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.7-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.8-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.17.9-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.10-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.7-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.8-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.19.9-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.21.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.10-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.11-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.12-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.13-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.14-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.15-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.7-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.8-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-1.9.9-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/centos/7/x86\_64/RPMS/nginx-debug-1.9.7-1.el7.ngx.x86\_64.rpm

##### http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx

* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~squeeze\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~squeeze\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~squeeze\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~squeeze\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~squeeze\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~squeeze\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.0-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.0-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.0-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.1-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.1-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.1-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.10-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.10-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.10-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.10-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.11-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.11-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.11-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.11-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.12-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.12-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.12-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.12-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.13-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.13-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.13-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.13-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.13-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.13-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.2-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.2-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.2-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.2-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.3-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.3-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.3-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.3-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.4-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.4-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.4-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.4-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.5-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.5-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.5-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.5-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.6-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.6-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.6-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.6-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.7-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.7-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.7-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.7-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.8-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.8-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.8-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.8-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.9-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.9-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.9-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.11.9-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.0-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.0-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.0-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.0-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.0-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.1-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.1-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.1-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.1-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.1-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.10-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.10-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.10-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.10-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.11-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.11-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.11-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.11-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.12-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.12-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.12-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.12-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.2-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.2-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.2-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.2-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.2-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.2-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.3-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.3-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.3-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.3-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.3-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.3-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.4-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.4-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.4-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.4-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.4-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.4-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-2~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-2~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-2~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.5-2~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.6-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.6-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.6-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.6-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.7-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.7-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.7-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.7-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.8-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.8-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.8-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.8-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.9-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.9-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.9-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.13.9-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.0-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.0-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.0-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.0-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.1-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.1-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.1-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.1-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.10-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.10-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.10-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.10-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.11-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.11-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.11-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.11-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.12-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.12-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.12-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.12-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.2-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.2-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.2-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.2-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.3-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.3-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.3-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.3-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.4-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.4-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.4-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.4-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.5-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.5-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.5-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.5-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.6-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.6-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.6-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.6-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.7-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.7-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.7-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.7-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.8-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.8-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.8-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.8-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.9-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.9-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.9-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.15.9-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.17.0-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.17.0-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.17.1-1~stretch\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.17.1-1~stretch\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.0-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.0-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.0-1~squeeze\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.0-1~squeeze\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.0-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.0-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.1-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.1-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.1-1~squeeze\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.1-1~squeeze\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.1-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.1-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.10-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.10-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.10-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.10-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.11-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.11-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.11-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.11-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.12-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.12-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.12-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.12-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.13-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.13-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.13-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.13-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.14-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.14-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.14-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.14-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.15-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.15-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.15-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.15-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.2-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.2-1~squeeze\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.2-1~squeeze\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.2-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.2-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.3-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.3-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.3-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.3-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.4-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.4-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.4-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.4-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.5-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.5-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.5-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.5-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.6-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.6-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.6-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.6-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.7-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.7-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.7-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.7-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.8-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.8-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.8-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.8-1~wheezy\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.9-1~jessie\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.9-1~jessie\_i386.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.9-1~wheezy\_amd64.deb
* http://nginx.org/packages/mainline/debian/pool/nginx/n/nginx/nginx\_1.9.9-1~wheezy\_i386.deb

##### http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS

* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.3.15-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.3.16-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.0-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.1-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.10-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.11-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.12-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.13-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.2-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.3-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.6-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.7-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.8-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.5.9-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.0-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.1-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.2-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.3-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.4-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.5-1opensuse12.1.ngx.i586.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/i586/RPMS/nginx-debug-1.7.6-1opensuse12.1.ngx.i586.rpm

##### http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS

* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.3.15-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.3.16-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.0-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.1-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.10-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.11-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.12-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.13-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.2-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.3-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.5-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.6-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.7-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.8-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.5.9-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.0-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.1-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.2-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.3-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.4-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.5-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.7.6-1opensuse12.1.ngx.x86\_64.rpm

##### http://nginx.org/packages/mainline/rhel/6/i386/RPMS

* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.10-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.11-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.12-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.13-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.11.9-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.13.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.10-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.11-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.12-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.13-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.14-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.15-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-1.9.9-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/mainline/rhel/6/i386/RPMS/nginx-debug-1.9.7-1.el6.ngx.i386.rpm

##### http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS

* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.13-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.11.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.13.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.15.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.17.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.19.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.19.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.19.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.19.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.19.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.19.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.13-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.14-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.15-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-1.9.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/rhel/6/x86\_64/RPMS/nginx-debug-1.9.7-1.el6.ngx.x86\_64.rpm

##### http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS

* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.10-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.11-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.12-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.13-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.7-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.8-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.11.9-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.10-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.11-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.12-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.7-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.8-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.13.9-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.10-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.11-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.12-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.7-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.8-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.15.9-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.10-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.7-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.8-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.17.9-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.10-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.7-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.8-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.19.9-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.21.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.10-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.11-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.12-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.13-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.14-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.15-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.7-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.8-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-1.9.9-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.4-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.5-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.6-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/mainline/sles/12/x86\_64/RPMS/nginx-debug-1.9.7-1.sles12.ngx.x86\_64.rpm

##### http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx

* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.5.12-1~raring\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.5.12-1~raring\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.5.7-1~oneiric\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.5.7-1~oneiric\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.7.2-1~quantal\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.7.2-1~quantal\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.7.3-1~saucy\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.7.3-1~saucy\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~lucid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~lucid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.0-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~lucid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~lucid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.1-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~lucid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~lucid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.2-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.3-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.4-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.5-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.6-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.9.7-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.0-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.1-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.10-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.11-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.12-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.13-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.2-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.3-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.4-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.4-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.4-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.4-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.4-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.4-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.5-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.5-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.5-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.5-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.5-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.5-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.6-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.7-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.8-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.11.9-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.0-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.1-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.10-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.10-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.10-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.10-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.10-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.10-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.11-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.11-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.11-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.11-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.11-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.11-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.12-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.2-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.3-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~yakkety\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~yakkety\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.4-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-2~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-2~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-2~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-2~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-2~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.5-2~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.6-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.6-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.6-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.6-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.6-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.6-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.7-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~zesty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.8-1~zesty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.9-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.9-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.9-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.9-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.9-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.13.9-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.0-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.1-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.10-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.10-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.10-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.10-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.10-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.10-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.11-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.11-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.11-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.11-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.11-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.11-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.12-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.12-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.12-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.12-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.12-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.12-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~artful\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~artful\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.2-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.3-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.3-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.3-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.3-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.3-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.4-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.4-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.4-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.4-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.4-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.5-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.5-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.5-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.5-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.5-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.6-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.6-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.6-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.6-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.6-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.6-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.7-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.7-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.7-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.7-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.7-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.7-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.8-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.8-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.8-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.8-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.8-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.8-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.9-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.9-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.9-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.9-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.9-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.15.9-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.0-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.0-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.0-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.0-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.1-1~bionic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.1-1~cosmic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.1-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.17.1-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~lucid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~lucid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.0-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~lucid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~lucid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.1-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.10-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.11-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.12-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.13-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.13-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.13-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.13-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.13-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.13-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.14-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.14-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.14-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.14-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.14-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.14-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~xenial\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.15-1~xenial\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~lucid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~lucid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.2-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~utopic\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~utopic\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.3-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.4-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.4-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.4-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.4-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.4-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.4-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.5-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.5-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.5-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.5-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.5-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.5-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.6-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.7-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.8-1~wily\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~precise\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~precise\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~trusty\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~trusty\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~vivid\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~vivid\_i386.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~wily\_amd64.deb
* http://nginx.org/packages/mainline/ubuntu/pool/nginx/n/nginx/nginx\_1.9.9-1~wily\_i386.deb

##### http://nginx.org/packages/old/centos/5/i386

* http://nginx.org/packages/old/centos/5/i386/nginx-1.6.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.6.0-2.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.6.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.6.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.6.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.10-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.11-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.12-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.8-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-1.7.9-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.2.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.2.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.2.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.2.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.2.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.2.8-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.3.15-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.3.16-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.4.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.10-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.11-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.12-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.13-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.8-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.5.9-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.6.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.6.0-2.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.6.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.6.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.6.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.10-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.11-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.12-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.4-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.5-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.6-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.7-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.8-1.el5.ngx.i386.rpm
* http://nginx.org/packages/old/centos/5/i386/nginx-debug-1.7.9-1.el5.ngx.i386.rpm

##### http://nginx.org/packages/old/centos/5/x86\_64

* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.6.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.6.0-2.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.6.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.6.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.6.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.10-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.11-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.12-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.8-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-1.7.9-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.2.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.2.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.2.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.2.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.2.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.2.8-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.3.15-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.3.16-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.4.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.10-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.11-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.12-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.13-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.8-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.5.9-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.6.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.6.0-2.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.6.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.6.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.6.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.10-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.11-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.12-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.4-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.5-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.6-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.7-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.8-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/5/x86\_64/nginx-debug-1.7.9-1.el5.ngx.x86\_64.rpm

##### http://nginx.org/packages/old/centos/6/i386

* http://nginx.org/packages/old/centos/6/i386/nginx-1.6.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.6.0-2.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.6.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.6.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.6.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.10-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.11-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.12-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-1.7.9-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.2.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.2.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.2.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.2.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.2.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.2.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.3.15-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.3.16-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.4.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.10-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.11-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.12-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.13-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.5.9-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.6.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.6.0-2.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.6.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.6.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.6.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.10-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.11-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.12-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.4-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.5-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.6-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.7-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.8-1.el6.ngx.i386.rpm
* http://nginx.org/packages/old/centos/6/i386/nginx-debug-1.7.9-1.el6.ngx.i386.rpm

##### http://nginx.org/packages/old/centos/6/x86\_64

* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.6.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.6.0-2.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.6.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.6.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.6.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-1.7.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.2.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.2.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.2.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.2.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.2.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.2.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.3.15-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.3.16-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.4.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.13-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.5.9-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.6.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.6.0-2.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.6.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.6.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.6.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.10-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.11-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.12-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.4-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.5-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.6-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.7-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.8-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/6/x86\_64/nginx-debug-1.7.9-1.el6.ngx.x86\_64.rpm

##### http://nginx.org/packages/old/centos/7/x86\_64

* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.6.0-2.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.6.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.6.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.6.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.10-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.11-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.12-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.7-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.8-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-1.7.9-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.6.0-2.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.6.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.6.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.6.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.10-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.11-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.12-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.4-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.5-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.6-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.7-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.8-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/old/centos/7/x86\_64/nginx-debug-1.7.9-1.el7.ngx.x86\_64.rpm

##### http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS

* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.0.14-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.0.15-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.0-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.1-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.2-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.4-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.5-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.6-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.2.8-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.0-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.2-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.3-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.4-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.5-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.6-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.4.7-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.6.0-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.6.0-2opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.6.1-1opensuse12.1.ngx.x86\_64.rpm
* http://nginx.org/packages/opensuse/12.1/x86\_64/RPMS/nginx-debug-1.6.2-1opensuse12.1.ngx.x86\_64.rpm

##### http://nginx.org/packages/rhel/5/i386/RPMS

* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-1.10.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-1.10.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-1.10.2-1.el5.ngx.i386.rpm
* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-1.10.3-1.el5.ngx.i386.rpm
* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-1.8.0-1.el5.ngx.i386.rpm
* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-1.8.1-1.el5.ngx.i386.rpm
* http://nginx.org/packages/rhel/5/i386/RPMS/nginx-debug-1.8.0-1.el5.ngx.i386.rpm

##### http://nginx.org/packages/rhel/5/x86\_64/RPMS

* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-1.10.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-1.10.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-1.10.2-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-1.10.3-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-1.8.0-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-1.8.1-1.el5.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/5/x86\_64/RPMS/nginx-debug-1.8.0-1.el5.ngx.x86\_64.rpm

##### http://nginx.org/packages/rhel/6/i386/RPMS

* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.10.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.10.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.10.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.10.3-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.12.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.12.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.12.2-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.8.0-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-1.8.1-1.el6.ngx.i386.rpm
* http://nginx.org/packages/rhel/6/i386/RPMS/nginx-debug-1.8.0-1.el6.ngx.i386.rpm

##### http://nginx.org/packages/rhel/6/x86\_64/RPMS

* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.10.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.10.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.10.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.10.3-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.12.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.12.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.12.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.14.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.14.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.14.2-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.16.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.16.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.18.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.18.0-2.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.8.0-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-1.8.1-1.el6.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/6/x86\_64/RPMS/nginx-debug-1.8.0-1.el6.ngx.x86\_64.rpm

##### http://nginx.org/packages/rhel/7/x86\_64/RPMS

* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.10.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.10.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.10.2-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.10.3-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.12.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.12.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.12.2-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.14.0-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.14.1-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.14.2-1.el7\_4.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.16.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.16.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.18.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.18.0-2.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.20.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.20.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.8.0-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-1.8.1-1.el7.ngx.x86\_64.rpm
* http://nginx.org/packages/rhel/7/x86\_64/RPMS/nginx-debug-1.8.0-1.el7.ngx.x86\_64.rpm

##### http://nginx.org/packages/sles/12/x86\_64/RPMS

* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.10.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.10.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.10.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.10.3-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.12.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.12.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.12.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.14.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.14.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.14.2-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.16.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.16.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.18.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.18.0-2.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.20.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.20.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.8.0-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-1.8.1-1.sles12.ngx.x86\_64.rpm
* http://nginx.org/packages/sles/12/x86\_64/RPMS/nginx-debug-1.8.0-1.sles12.ngx.x86\_64.rpm

##### http://nginx.org/packages/ubuntu/pool/nginx/n/nginx

* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~vivid\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~vivid\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~wily\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx-debug\_1.8.0-1~wily\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~wily\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~wily\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.0-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~wily\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~wily\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.1-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.2-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.2-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.2-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.2-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.2-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.2-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~yakkety\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.10.3-1~yakkety\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~yakkety\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.0-1~yakkety\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~yakkety\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~yakkety\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~zesty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.1-1~zesty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.2-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.2-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.2-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.2-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.2-1~zesty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.12.2-1~zesty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~artful\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~artful\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~bionic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.0-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.1-1~bionic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.1-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.1-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.1-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.1-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.1-2~cosmic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.2-1~bionic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.2-1~cosmic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.2-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.2-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.2-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.14.2-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.16.0-1~bionic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.16.0-1~cosmic\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.16.0-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.16.0-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.16.0-1~xenial\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.16.0-1~xenial\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~lucid\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~lucid\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~utopic\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~vivid\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~vivid\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~wily\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.0-1~wily\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~precise\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~precise\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~trusty\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~trusty\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~vivid\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~vivid\_i386.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~wily\_amd64.deb
* http://nginx.org/packages/ubuntu/pool/nginx/n/nginx/nginx\_1.8.1-1~wily\_i386.deb

##### http://packages.eu-central-1.amazonaws.com/2017.09/main/154a6dd467e2/x86\_64/Packages

* http://packages.eu-central-1.amazonaws.com/2017.09/main/154a6dd467e2/x86\_64/Packages/nginx-1.12.1-1.33.amzn1.x86\_64.rpm

##### http://packages.eu-west-1.amazonaws.com/2015.09/main/201509419456/x86\_64/Packages

* http://packages.eu-west-1.amazonaws.com/2015.09/main/201509419456/x86\_64/Packages/nginx-1.8.0-10.25.amzn1.x86\_64.rpm

##### http://packages.eu-west-1.amazonaws.com/2015.09/updates/7258b711f970/x86\_64/Packages

* http://packages.eu-west-1.amazonaws.com/2015.09/updates/7258b711f970/x86\_64/Packages/nginx-1.8.1-1.26.amzn1.x86\_64.rpm

##### http://packages.eu-west-1.amazonaws.com/2016.03/updates/0f1bdc3765e6/x86\_64/Packages

* http://packages.eu-west-1.amazonaws.com/2016.03/updates/0f1bdc3765e6/x86\_64/Packages/nginx-1.8.1-3.27.amzn1.x86\_64.rpm

##### http://packages.eu-west-1.amazonaws.com/2016.09/main/4c53375a3f86/x86\_64/Packages

* http://packages.eu-west-1.amazonaws.com/2016.09/main/4c53375a3f86/x86\_64/Packages/nginx-1.10.1-1.28.amzn1.x86\_64.rpm

##### http://packages.eu-west-1.amazonaws.com/2017.03/main/201703c0ffee/x86\_64/Packages

* http://packages.eu-west-1.amazonaws.com/2017.03/main/201703c0ffee/x86\_64/Packages/nginx-1.10.2-1.30.amzn1.x86\_64.rpm

##### http://packages.us-west-2.amazonaws.com/2017.03/updates/1f71589089f2/x86\_64/Packages

* http://packages.us-west-2.amazonaws.com/2017.03/updates/1f71589089f2/x86\_64/Packages/nginx-1.10.3-1.31.amzn1.x86\_64.rpm
* http://packages.us-west-2.amazonaws.com/2017.03/updates/1f71589089f2/x86\_64/Packages/nginx-1.12.1-1.32.amzn1.x86\_64.rpm

##### http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx

* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.1-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.2-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.11.3-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.3.12-0ubuntu0ppa2~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.3.12-0ubuntu0ppa2~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.5.0-1~ppa1~natty\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.5.0-1~ppa1~natty\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.5.0-1~ppa1~oneiric\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.5.0-1~ppa1~oneiric\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.5.9-1~raring0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.5.9-1~raring0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.7.0-1+quantal0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.7.0-1+quantal0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.7.1-1+saucy0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.7.1-1+saucy0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.10-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.11-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+xenial1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.12-0+xenial1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.13-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.14-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+utopic0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+utopic0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.3-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.4-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+precise1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+precise2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+precise2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+trusty1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+trusty2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+trusty2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+vivid1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+vivid1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+vivid2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+vivid2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+wily1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+wily1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+wily2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+wily2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+xenial2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.6-1+xenial2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.7-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-extras\_1.9.9-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.1-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.2-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.11.3-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.3.12-0ubuntu0ppa2~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.3.12-0ubuntu0ppa2~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.5.0-1~ppa1~natty\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.5.0-1~ppa1~natty\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.5.0-1~ppa1~oneiric\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.5.0-1~ppa1~oneiric\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.5.9-1~raring0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.5.9-1~raring0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.7.0-1+quantal0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.7.0-1+quantal0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.7.1-1+saucy0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.7.1-1+saucy0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.10-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.11-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+xenial1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.12-0+xenial1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.13-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.14-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+utopic0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+utopic0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.3-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.4-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+precise1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+precise2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+precise2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+trusty1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+trusty2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+trusty2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+vivid1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+vivid1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+vivid2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+vivid2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+wily1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+wily1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+wily2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+wily2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+xenial2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.6-1+xenial2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.7-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-full\_1.9.9-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.1-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.2-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.11.3-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.3.12-0ubuntu0ppa2~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.3.12-0ubuntu0ppa2~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.5.0-1~ppa1~natty\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.5.0-1~ppa1~natty\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.5.0-1~ppa1~oneiric\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.5.0-1~ppa1~oneiric\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.5.9-1~raring0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.5.9-1~raring0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.7.0-1+quantal0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.7.0-1+quantal0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.7.1-1+saucy0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.7.1-1+saucy0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.10-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.11-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+xenial1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.12-0+xenial1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.13-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.14-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+utopic0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+utopic0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.3-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.4-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+precise1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+precise2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+precise2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+trusty1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+trusty2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+trusty2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+vivid1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+vivid1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+vivid2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+vivid2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+wily1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+wily1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+wily2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+wily2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+xenial2\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.6-1+xenial2\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.7-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-light\_1.9.9-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.3.12-0ubuntu0ppa2~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.3.12-0ubuntu0ppa2~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.5.0-1~ppa1~natty\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.5.0-1~ppa1~natty\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.5.0-1~ppa1~oneiric\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.5.0-1~ppa1~oneiric\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.5.9-1~raring0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.5.9-1~raring0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.0-1+quantal0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.0-1+quantal0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.1-1+saucy0\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.1-1+saucy0\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.5-1+precise1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.5-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.5-1+trusty1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.5-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.5-1+utopic1.1\_amd64.deb
* http://ppa.launchpad.net/nginx/development/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.7.5-1+utopic1.1\_i386.deb

##### http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx

* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.0-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.10.1-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.2.7-0ubuntu0ppa1~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.2.7-0ubuntu0ppa1~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.0-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.0-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.0-1+utopic1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.0-1+vivid1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-extras\_1.8.1-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.0-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.10.1-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.2.7-0ubuntu0ppa1~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.2.7-0ubuntu0ppa1~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.4.1-1ppa1~natty\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.4.1-1ppa1~oneiric\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.4.1-1ppa1~oneiric\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.4.4-4~raring\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.4.4-4~raring\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.6.0-1+quantal0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.6.0-1+quantal0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.6.0-1+saucy0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.6.0-1+saucy0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+precise1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+trusty1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+utopic1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+utopic1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+vivid1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.0-1+vivid1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-full\_1.8.1-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.0-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+yakkety0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.10.1-0+yakkety0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.2.7-0ubuntu0ppa1~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.2.7-0ubuntu0ppa1~maverick\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.4.1-1ppa1~natty\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.4.1-1ppa1~natty\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.4.1-1ppa1~oneiric\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.4.1-1ppa1~oneiric\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.4.4-4~raring\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.4.4-4~raring\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.6.0-1+quantal0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.6.0-1+quantal0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.6.0-1+saucy0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.6.0-1+saucy0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+precise1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+precise1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+trusty1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+trusty1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+utopic1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+utopic1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+vivid1\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.0-1+vivid1\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+precise0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+precise0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+trusty0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+trusty0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+vivid0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+vivid0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+wily0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+wily0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+xenial0\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-light\_1.8.1-1+xenial0\_i386.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.2.7-0ubuntu0ppa1~maverick\_amd64.deb
* http://ppa.launchpad.net/nginx/stable/ubuntu/pool/main/n/nginx/nginx-naxsi\_1.2.7-0ubuntu0ppa1~maverick\_i386.deb

##### http://security.debian.org/debian-security/pool/updates/main/n/nginx

* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.2.1-2.2+wheezy4+deb7u1\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.2.1-2.2+wheezy4+deb7u1\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.6.2-5+deb8u2\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.6.2-5+deb8u3\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.6.2-5+deb8u3\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.6.2-5+deb8u6\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-extras\_1.6.2-5+deb8u6\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.2.1-2.2+wheezy4+deb7u1\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.2.1-2.2+wheezy4+deb7u1\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.6.2-5+deb8u2\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.6.2-5+deb8u3\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.6.2-5+deb8u3\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.6.2-5+deb8u6\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-full\_1.6.2-5+deb8u6\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.2.1-2.2+wheezy4+deb7u1\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.2.1-2.2+wheezy4+deb7u1\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.6.2-5+deb8u2\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.6.2-5+deb8u3\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.6.2-5+deb8u3\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.6.2-5+deb8u6\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-light\_1.6.2-5+deb8u6\_i386.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-naxsi\_1.2.1-2.2+wheezy4+deb7u1\_amd64.deb
* http://security.debian.org/debian-security/pool/updates/main/n/nginx/nginx-naxsi\_1.2.1-2.2+wheezy4+deb7u1\_i386.deb

##### http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS

* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.13.12-4187.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.13.12-4308.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.13.5-2194.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.13.5-2195.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.13.6-2582.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.13.8-3124.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.14.0-4591.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.14.0-4597.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.6.0-21.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.6.1-22.el6.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/6/x86\_64/RPMS/nginx-1.6.2-23.el6.art.x86\_64.rpm

##### http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS

* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.13.12-4187.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.13.12-4308.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.13.5-2194.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.13.5-2195.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.13.6-2582.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.13.8-3124.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.14.0-4591.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.14.0-4597.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.6.1-22.el7.art.x86\_64.rpm
* http://www.atomicorp.com/channels/atomic/centos/7/x86\_64/RPMS/nginx-1.6.2-23.el7.art.x86\_64.rpm

##### https://archives.dotdeb.org/dists/wheezy/nginx/1.6.2/binary-amd64

* https://archives.dotdeb.org/dists/wheezy/nginx/1.6.2/binary-amd64/nginx-extras\_1.6.2-1~dotdeb.1\_amd64.deb
* https://archives.dotdeb.org/dists/wheezy/nginx/1.6.2/binary-amd64/nginx-full\_1.6.2-1~dotdeb.1\_amd64.deb
* https://archives.dotdeb.org/dists/wheezy/nginx/1.6.2/binary-amd64/nginx-light\_1.6.2-1~dotdeb.1\_amd64.deb
* https://archives.dotdeb.org/dists/wheezy/nginx/1.6.2/binary-amd64/nginx-naxsi\_1.6.2-1~dotdeb.1\_amd64.deb

##### https://buildpacks.cloudfoundry.org/dependencies/nginx-static

* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.0-linux-x64-7d0e1375.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.0-linux-x64-cflinuxfs2-5142f2b2.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.0-linux-x64-cflinuxfs3-23553dd2.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.1-linux-x64-cflinuxfs2-a0f93eda.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.1-linux-x64-cflinuxfs3-a90e99a5.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.2-linux-x64-cflinuxfs2-eb8c0353.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.14.2-linux-x64-cflinuxfs3-bae9b9ac.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.0-linux-x64-64919fa9.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.1-linux-x64-1166715b.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.10-linux-x64-cflinuxfs2-6247377a.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.10-linux-x64-cflinuxfs3-6439e95b.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.11-linux-x64-cflinuxfs2-03f76271.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.11-linux-x64-cflinuxfs3-1b53d732.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.12-linux-x64-cflinuxfs2-4d0440ef.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.12-linux-x64-cflinuxfs2-eb4e6044.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.12-linux-x64-cflinuxfs3-27bb34e1.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.12-linux-x64-cflinuxfs3-4b82e605.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.2-linux-x64-cflinuxfs2-535a2646.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.2-linux-x64-cflinuxfs3-d57d6220.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.3-linux-x64-cflinuxfs2-a466977f.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.3-linux-x64-cflinuxfs3-c27042f7.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.5-linux-x64-cflinuxfs2-df8b02ea.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.5-linux-x64-cflinuxfs3-798caddc.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.6-linux-x64-cflinuxfs2-d8a2c4eb.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.6-linux-x64-cflinuxfs3-2746e45a.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.7-linux-x64-cflinuxfs2-79867cf4.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.7-linux-x64-cflinuxfs3-72da3615.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.8-linux-x64-cflinuxfs2-48b8f057.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.8-linux-x64-cflinuxfs3-6f865593.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.9-linux-x64-cflinuxfs2-ba737288.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.15.9-linux-x64-cflinuxfs3-52f983b1.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.16.0-linux-x64-cflinuxfs2-0979f6dd.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.16.0-linux-x64-cflinuxfs2-715f5fcc.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.16.0-linux-x64-cflinuxfs3-4bca85aa.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.16.0-linux-x64-cflinuxfs3-8e2471f5.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.16.1-linux-x64-cflinuxfs2-000976a8.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.16.1-linux-x64-cflinuxfs3-4917bf93.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.0-linux-x64-cflinuxfs2-f35aff96.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.0-linux-x64-cflinuxfs3-10287b21.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.2-linux-x64-cflinuxfs2-e09a4a0d.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.2-linux-x64-cflinuxfs3-ce201882.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.3-linux-x64-cflinuxfs2-c8f18d90.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.3-linux-x64-cflinuxfs3-3f6db241.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.4-linux-x64-cflinuxfs3-ed4aa971.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx-static/nginx-1.17.5-linux-x64-cflinuxfs3-a25b6e9a.tgz

##### https://buildpacks.cloudfoundry.org/dependencies/nginx

* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.12.1-linux-x64-e824b7e3.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.12.2-linux-x64-60e5d131.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.0-linux-x64-4debb822.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.1-linux-x64-6178c85f.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.12-linux-x64-d1593c9d.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.2-linux-x64-1c2d589d.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.3-linux-x64-53917f43.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.4-linux-x64-3b4180ad.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.5-linux-x64-1dda12b3.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.6-linux-x64-b624d604.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.7-linux-x64-95aff9ab.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.8-linux-x64-9585c5f4.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.13.9-linux-x64-21ff4d0f.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.14.0-linux-x64-22d73813.tgz
* https://buildpacks.cloudfoundry.org/dependencies/nginx/nginx-1.15.0-linux-x64-fcf8f112.tgz

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-5-x86\_64/00446691-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-5-x86\_64/00446691-openresty/openresty-1.11.2.1-3.el5.centos.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-5-x86\_64/00492544-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-5-x86\_64/00492544-openresty/openresty-1.11.2.2-8.el5.centos.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00446691-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00446691-openresty/openresty-1.11.2.1-3.el6.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00492544-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00492544-openresty/openresty-1.11.2.2-8.el6.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00542405-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00542405-openresty/openresty-1.11.2.3-1.el6.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00543810-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00543810-openresty/openresty-1.11.2.3-9.el6.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00910061-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-6-x86\_64/00910061-openresty/openresty-1.15.8.1-1.el6.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00446691-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00446691-openresty/openresty-1.11.2.1-3.el7.centos.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00492544-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00492544-openresty/openresty-1.11.2.2-8.el7.centos.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00542405-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00542405-openresty/openresty-1.11.2.3-1.el7.centos.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00543810-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00543810-openresty/openresty-1.11.2.3-9.el7.centos.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00910061-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/epel-7-x86\_64/00910061-openresty/openresty-1.15.8.1-1.el7.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00446691-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00446691-openresty/openresty-1.11.2.1-3.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00492544-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00492544-openresty/openresty-1.11.2.2-8.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00543810-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00543810-openresty/openresty-1.11.2.3-9.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00554953-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00554953-openresty/openresty-1.11.2.3-10.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00557048-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00557048-openresty/openresty-1.11.2.3-12.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00557423-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00557423-openresty/openresty-1.11.2.3-13.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00557540-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00557540-openresty/openresty-1.11.2.3-14.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00559824-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00559824-openresty/openresty-1.11.2.3-15.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00578156-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00578156-openresty/openresty-1.11.2.4-1.fc24.x86\_64.rpm

##### https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00591457-openresty

* https://copr-be.cloud.fedoraproject.org/results/openresty/openresty/fedora-24-x86\_64/00591457-openresty/openresty-1.11.2.5-1.fc24.x86\_64.rpm

##### https://oss-binaries.phusionpassenger.com/apt/passenger/pool/lucid/main/n/nginx

* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/lucid/main/n/nginx/nginx-extras\_1.6.3-8.5.0.7~lucid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/lucid/main/n/nginx/nginx-extras\_1.6.3-8.5.0.7~lucid1\_i386.deb

##### https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx

* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.0-8.5.0.28~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.0-8.5.0.28~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.1-8.5.0.29~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.1-8.5.0.29~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.1-8.5.0.30~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.1-8.5.0.30~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.2-8.5.1.0~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.2-8.5.1.0~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.2-8.5.1.1~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.2-8.5.1.1~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.2-8.5.1.2~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.2-8.5.1.2~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.3~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.3~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.4~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.4~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.5~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.5~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.6~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.6~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.7~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.10.3-8.5.1.7~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.12.1-8.5.1.10~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.12.1-8.5.1.10~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.12.1-8.5.1.8~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.12.1-8.5.1.8~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.12.1-8.5.1.9~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.12.1-8.5.1.9~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.6.3-8.5.0.7~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.6.3-8.5.0.7~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.6.3-8.5.0.8~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.6.3-8.5.0.8~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.10~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.10~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.11~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.11~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.13~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.13~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.14~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.14~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.15~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.15~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.16~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.16~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.18~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.18~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.19~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.19~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.20~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.20~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.21~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.21~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.22~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.22~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.23~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.23~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.9~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.0-8.5.0.9~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.24~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.24~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.25~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.25~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.26~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.26~precise1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.27~precise1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/precise/main/n/nginx/nginx-extras\_1.8.1-8.5.0.27~precise1\_i386.deb

##### https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx

* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.0-8.5.0.28~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.0-8.5.0.28~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.1-8.5.0.29~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.1-8.5.0.29~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.1-8.5.0.30~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.1-8.5.0.30~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.2-8.5.1.0~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.2-8.5.1.0~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.2-8.5.1.1~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.2-8.5.1.1~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.2-8.5.1.2~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.2-8.5.1.2~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.3~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.3~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.4~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.4~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.5~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.5~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.6~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.6~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.7~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.10.3-8.5.1.7~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.10~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.10~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.11~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.11~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.8~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.8~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.9~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.1-8.5.1.9~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.2-8.5.1.12~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.2-8.5.1.12~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.2-8.5.2.0~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.2-8.5.2.1~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.2-8.5.2.2~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.12.2-8.5.2.3~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.0~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.1~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.2~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.3~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.4~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.5~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.6~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.14.0-8.5.3.7~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.15.7-8.6.0.0~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.15.8-8.6.0.1~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.15.8-8.6.0.2~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.6.3-8.5.0.7~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.6.3-8.5.0.7~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.6.3-8.5.0.8~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.6.3-8.5.0.8~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.10~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.10~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.11~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.11~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.13~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.13~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.14~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.14~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.15~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.15~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.16~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.16~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.18~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.18~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.19~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.19~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.20~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.20~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.21~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.21~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.22~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.22~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.23~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.23~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.9~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.0-8.5.0.9~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.24~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.24~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.25~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.25~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.26~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.26~trusty1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.27~trusty1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/trusty/main/n/nginx/nginx-extras\_1.8.1-8.5.0.27~trusty1\_i386.deb

##### https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx

* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.6.3-8.5.0.8~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.6.3-8.5.0.8~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.10~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.10~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.11~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.11~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.13~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.13~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.14~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.14~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.15~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.15~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.16~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.16~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.18~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.18~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.19~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.19~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.20~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.20~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.21~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.21~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.22~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.22~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.23~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.23~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.9~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.0-8.5.0.9~vivid1\_i386.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.1-8.5.0.24~vivid1\_amd64.deb
* https://oss-binaries.phusionpassenger.com/apt/passenger/pool/vivid/main/n/nginx/nginx-extras\_1.8.1-8.5.0.24~vivid1\_i386.deb

##### https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386

* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.0-8.p5.0.28.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.1-8.p5.0.29.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.1-8.p5.0.30.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.2-1.p5.1.0.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.2-1.p5.1.1.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.2-1.p5.1.2.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.3-1.p5.1.3.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.3-1.p5.1.4.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.10.3-1.p5.1.5.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.1-1.p5.1.10.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.1-1.p5.1.11.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.1-1.p5.1.6.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.1-1.p5.1.7.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.1-1.p5.1.8.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.1-1.p5.1.9.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.2-1.p5.1.12.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.2-1.p5.2.0.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.2-1.p5.2.1.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.2-1.p5.2.2.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.12.2-1.p5.2.3.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.0.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.1.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.2.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.3.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.4.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.5.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.6.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.14.0-1.p5.3.7.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.15.7-1.p6.0.0.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.15.8-1.p6.0.1.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.15.8-1.p6.0.2.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.17.3-1.p6.0.3.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.17.3-1.p6.0.4.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.6.3-8.p5.0.8.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.10.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.11.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.13.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.14.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.15.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.16.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.17.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.18.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.19.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.20.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.21.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.22.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.23.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.0-8.p5.0.9.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.1-8.p5.0.24.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.1-8.p5.0.25.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.1-8.p5.0.26.el6.i686.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/i386/nginx-1.8.1-8.p5.0.27.el6.i686.rpm

##### https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64

* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.0-8.p5.0.28.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.1-8.p5.0.29.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.1-8.p5.0.30.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.2-1.p5.1.0.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.2-1.p5.1.1.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.2-1.p5.1.2.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.3-1.p5.1.3.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.3-1.p5.1.4.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.10.3-1.p5.1.5.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.1-1.p5.1.10.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.1-1.p5.1.11.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.1-1.p5.1.6.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.1-1.p5.1.7.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.1-1.p5.1.8.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.1-1.p5.1.9.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.2-1.p5.1.12.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.2-1.p5.2.0.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.2-1.p5.2.1.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.2-1.p5.2.2.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.12.2-1.p5.2.3.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.0.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.1.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.2.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.3.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.4.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.5.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.6.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.14.0-1.p5.3.7.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.15.7-1.p6.0.0.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.15.8-1.p6.0.1.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.15.8-1.p6.0.2.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.17.3-1.p6.0.3.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.17.3-1.p6.0.4.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.6.3-8.p5.0.8.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.10.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.11.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.13.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.14.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.15.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.16.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.17.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.18.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.19.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.20.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.21.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.22.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.23.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.0-8.p5.0.9.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.1-8.p5.0.24.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.1-8.p5.0.25.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.1-8.p5.0.26.el6.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/6/x86\_64/nginx-1.8.1-8.p5.0.27.el6.x86\_64.rpm

##### https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64

* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.0-8.p5.0.28.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.1-8.p5.0.29.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.1-8.p5.0.30.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.2-1.p5.1.0.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.2-1.p5.1.1.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.2-1.p5.1.2.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.3-1.p5.1.3.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.3-1.p5.1.4.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.10.3-1.p5.1.5.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.1-1.p5.1.10.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.1-1.p5.1.11.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.1-1.p5.1.6.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.1-1.p5.1.7.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.1-1.p5.1.8.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.1-1.p5.1.9.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.2-1.p5.1.12.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.2-1.p5.2.0.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.2-1.p5.2.1.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.2-1.p5.2.2.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.12.2-1.p5.2.3.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.0.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.1.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.2.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.3.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.4.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.5.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.6.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.14.0-1.p5.3.7.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.15.7-1.p6.0.0.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.15.8-1.p6.0.1.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.15.8-1.p6.0.2.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.17.3-1.p6.0.3.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.17.3-1.p6.0.4.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.6.3-8.p5.0.8.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.10.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.11.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.13.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.14.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.15.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.16.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.17.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.18.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.19.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.20.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.21.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.22.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.23.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.0-8.p5.0.9.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.1-8.p5.0.24.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.1-8.p5.0.25.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.1-8.p5.0.26.el7.x86\_64.rpm
* https://oss-binaries.phusionpassenger.com/yum/passenger/el/7/x86\_64/nginx-1.8.1-8.p5.0.27.el7.x86\_64.rpm

##### https://packages.dotdeb.org/pool/all/n/nginx

* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B7.3\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B7.3\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.1-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2Bhttp2%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.2-2~dotdeb%2Bhttp2%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.3-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.3-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.3-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.3-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.3-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.10.3-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.0-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.0-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.1-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.1-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.12.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.1-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.1-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.14.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.0-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.1-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.1-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-extras\_1.8.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B7.3\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B7.3\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.1-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2Bhttp2%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.2-2~dotdeb%2Bhttp2%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.3-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.3-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.3-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.3-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.3-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.10.3-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.0-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.0-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.1-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.1-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.12.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.1-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.1-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.14.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.0-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.1-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.1-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-full\_1.8.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B7.3\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B7.3\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.1-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2Bhttp2%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.2-2~dotdeb%2Bhttp2%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.3-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.3-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.3-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.3-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.3-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.10.3-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.0-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.0-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.1-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.1-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.12.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.1-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.1-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.2-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.2-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.2-1~dotdeb%2Bhttp2%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.14.2-1~dotdeb%2Bhttp2%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.0-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.1-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.1-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-light\_1.8.1-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B7.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B7.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B8.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B8.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.0-1~dotdeb%2B8.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.1-1~dotdeb%2B6.2\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.1-1~dotdeb%2B6.2\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.1-1~dotdeb%2B7.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.1-1~dotdeb%2B7.1\_i386.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.1-1~dotdeb%2B8.1\_amd64.deb
* https://packages.dotdeb.org/pool/all/n/nginx/nginx-naxsi\_1.8.1-1~dotdeb%2B8.1\_i386.deb

##### https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce

* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.0~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.0~omnibus.1-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.0~omnibus.2-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.0~omnibus.3-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.0~omnibus.4-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.1~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.1~omnibus.2-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.4~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.4~omnibus.1-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.10.5~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.11.0~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.11.0~omnibus.1-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.11.1~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.11.2~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.11.3~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.11.4~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.12.0~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.12.0~omnibus.1-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.12.1~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.12.1~omnibus.1-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.12.2~omnibus-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.12.2~omnibus.1-1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.13.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.13.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.13.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.13.3-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.13.4-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.13.5-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.14.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.14.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.14.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.14.2-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.14.3-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_7.14.3-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.1-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.2-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.3-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.4-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.0.5-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.0-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.1-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.3-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.1.4-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.2.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.2.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.2.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.2.3-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.3.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.3.1-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.3.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.3.3-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.3.3-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.3.4-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.4.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.4.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.4.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.4.3-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.4.4-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.4.5-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.5.0-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.5.0-ce.1\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.5.1-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.5.2-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.5.3-ce.0\_amd64.deb
* https://packages.gitlab.com/gitlab/gitlab-ce/ubuntu/pool/trusty/main/g/gitlab-ce/gitlab-ce\_8.5.4-ce.0\_amd64.deb

##### https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS

* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.11.10-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.11.10-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.11.10-3.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.11.10-4.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.11.3-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.11.5-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.13.4-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.13.7-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.13.7-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.9.13-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.9.13-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.9.9-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.9.9-3.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-1.9.9-4.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-15-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-15-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-15-3.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-16-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-16-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-17-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-18-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-extras-1.11.3-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-extras-1.9.13-1.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-extras-1.9.13-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-extras-1.9.9-2.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-extras-1.9.9-3.amzn1.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/amzn/2017.03/x86\_64/RPMS/nginx-plus-extras-1.9.9-4.amzn1.ngx.x86\_64.rpm

##### https://plus-pkgs.nginx.com/centos/5/i386/RPMS

* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.11.10-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.11.10-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.11.10-3.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.11.10-4.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.11.3-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.11.5-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.11-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.11-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.3-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.3-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.7-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.7-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.7-3.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.7.7-4.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.13-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.13-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.4-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.4-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.4-3.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.9-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.9-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.9-3.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-1.9.9-4.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.12-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.3-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.3-4.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.3-5.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.7-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.7-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.7-3.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.5.7-4.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.11-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.11-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.3-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.3-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.7-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.7-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.7-3.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.7.7-4.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.9.4-1.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.9.4-2.el5.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/5/i386/RPMS/nginx-plus-debug-1.9.4-3.el5.ngx.i386.rpm

##### https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS

* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.11.10-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.11.10-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.11.10-3.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.11.10-4.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.11.3-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.11.5-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.11-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.11-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.3-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.3-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.7-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.7-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.7-3.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.7.7-4.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.13-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.13-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.4-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.4-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.4-3.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.9-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.9-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.9-3.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-1.9.9-4.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.0-2.ngx.el5.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.12-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.3-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.3-4.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.3-5.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.7-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.7-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.7-3.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.5.7-4.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.11-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.11-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.3-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.3-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.7-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.7-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.7-3.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.7.7-4.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.9.4-1.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.9.4-2.el5.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/5/x86\_64/RPMS/nginx-plus-debug-1.9.4-3.el5.ngx.x86\_64.rpm

##### https://plus-pkgs.nginx.com/centos/6/i386/RPMS

* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.11.10-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.11.10-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.11.10-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.11.10-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.11.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.11.5-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.13.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.13.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.13.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.11-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.11-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.7.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.13-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.13-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.9-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.9-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.9-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-1.9.9-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.12-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.3-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.3-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.3-5.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.5.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.11-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.11-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.7.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-debug-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.11.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.5.12-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.11-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.11-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.7.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.13-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.13-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.9-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.9-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.9-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-1.9.9-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.5.12-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.11-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.11-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.7.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-extras-debug-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-http2-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-http2-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-http2-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-http2-debug-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-http2-debug-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-http2-debug-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.11-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.11-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.7.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-1.9.4-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.5.12-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.5.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.5.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.5.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.5.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.11-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.11-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.3-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.3-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.7-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.7-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.7-3.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.7.7-4.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.9.4-1.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.9.4-2.el6.ngx.i386.rpm
* https://plus-pkgs.nginx.com/centos/6/i386/RPMS/nginx-plus-lua-debug-1.9.4-3.el6.ngx.i386.rpm

##### https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS

* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.11.10-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.11.10-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.11.10-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.11.10-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.11.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.11.5-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.13.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.13.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.13.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.11-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.11-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.7.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.13-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.13-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.9-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.9-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.9-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-1.9.9-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-15-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-15-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-15-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-16-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-16-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-17-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-18-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.0-2.ngx.el6.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.12-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.3-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.3-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.3-5.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.5.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.11-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.11-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.7.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-debug-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.11.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.5.12-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.11-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.11-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.7.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.13-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.13-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.9-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.9-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.9-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-1.9.9-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.5.12-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.11-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.11-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-http2-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-http2-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-http2-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.11-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.11-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.7.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-1.9.4-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.5.12-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.5.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.5.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.5.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.5.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.11-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.11-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.3-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.3-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-3.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-4.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-1.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-2.el6.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/6/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-3.el6.ngx.x86\_64.rpm

##### https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS

* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.11.10-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.11.10-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.11.10-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.11.10-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.11.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.11.5-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.13.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.13.4-1.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.13.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.13.7-1.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.13.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.13.7-2.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.11-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.11-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.3-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.7-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.7.7-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.13-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.13-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.9-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.9-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.9-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-1.9.9-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-15-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-15-1.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-15-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-15-2.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-15-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-15-3.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-16-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-16-1.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-16-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-16-2.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-17-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-17-1.el7\_4.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-18-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.11-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.11-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.3-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.7-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.7.7-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-debug-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.11.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.11-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.11-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.3-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.7-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.7.7-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.13-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.13-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.9-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.9-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.9-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-1.9.9-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.11-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.11-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.3-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-http2-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-http2-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-http2-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.11-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.11-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.3-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.7-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.7.7-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-1.9.4-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.11-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.11-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.3-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.3-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-3.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-4.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-1.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-2.el7.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/centos/7/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-3.el7.ngx.x86\_64.rpm

##### https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus

* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-5~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-5~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-5~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-5~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~squeeze\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~squeeze\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~wheezy\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~wheezy\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~jessie\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~jessie\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_19-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_19-1~stretch\_i386.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_20-1~stretch\_amd64.deb
* https://plus-pkgs.nginx.com/debian/pool/nginx-plus/n/nginx-plus/nginx-plus\_20-1~stretch\_i386.deb

##### https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS

* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.11.10-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.11.10-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.11.10-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.11.10-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.11.3-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.11.5-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.13.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.13.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.13.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.7.11-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.7.11-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.7.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.7.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.7.7-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.7.7-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.13-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.13-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.9-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.9-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.9-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-1.9.9-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-15-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-15-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-15-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-16-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-16-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-17-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-18-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.7.11-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.7.11-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.7.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.7.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.7.7-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.7.7-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-debug-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.11.3-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.7.11-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.7.11-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.7.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.7.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.7.7-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.7.7-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.13-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.13-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.9-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.9-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.9-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-1.9.9-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.7.11-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.7.11-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.7.7-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-extras-debug-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-http2-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-http2-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-http2-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-http2-debug-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.7.11-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.7.11-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.7.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.7.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.7.7-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.7.7-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-1.9.4-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.7.11-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.7.11-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-3.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.7.7-4.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-1.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-2.sles12.ngx.x86\_64.rpm
* https://plus-pkgs.nginx.com/sles/12/x86\_64/RPMS/nginx-plus-lua-debug-1.9.4-3.sles12.ngx.x86\_64.rpm

##### https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus

* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.12-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-5~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.3-5~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-1~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-2~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-3~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.5.7-4~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.11-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.3-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-3~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.7.7-4~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-debug\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.5.12-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.11-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.3-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-3~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.7.7-4~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras-debug\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.11.3-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.11-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-3~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.7.7-4~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.13-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-2~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-3~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-extras\_1.9.9-4~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2-debug\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-http2\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.12-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-3~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~quantal\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~quantal\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~raring\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~raring\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~saucy\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.5.7-4~saucy\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.11-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.3-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-3~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.7.7-4~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua-debug\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.11-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-3~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.7.7-4~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus-lua\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~yakkety\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-1~yakkety\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~yakkety\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-2~yakkety\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~yakkety\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-3~yakkety\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~yakkety\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~yakkety\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~zesty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.10-4~zesty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.3-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~yakkety\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.11.5-1~yakkety\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~zesty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.4-1~zesty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~artful\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~artful\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~zesty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-1~zesty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~artful\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~artful\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~zesty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.13.7-2~zesty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.11-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-1~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-2~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-3~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~lucid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~lucid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~utopic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.7.7-4~utopic\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.13-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.4-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-1~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-2~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-3~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~precise\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~precise\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~vivid\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~vivid\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~wily\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_1.9.9-4~wily\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~artful\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~artful\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~artful\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~artful\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_15-3~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_16-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_17-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~trusty\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~trusty\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_18-2~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_19-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_19-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_19-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_20-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_20-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_20-1~xenial\_i386.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_21-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_21-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_22-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_22-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_23-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_23-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_23-2~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_23-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_24-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_24-1~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_24-2~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_24-2~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_24-3~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_24-3~xenial\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_25-1~bionic\_amd64.deb
* https://plus-pkgs.nginx.com/ubuntu/pool/nginx-plus/n/nginx-plus/nginx-plus\_25-2~bionic\_amd64.deb

##### https://pulp.inuits.eu/passenger/rhel/7/x86\_64

* https://pulp.inuits.eu/passenger/rhel/7/x86\_64/passenger-5.0.10-8.el7.x86\_64.rpm
* https://pulp.inuits.eu/passenger/rhel/7/x86\_64/passenger-5.0.11-8.el7.x86\_64.rpm
* https://pulp.inuits.eu/passenger/rhel/7/x86\_64/passenger-5.0.8-8.el7.x86\_64.rpm
* https://pulp.inuits.eu/passenger/rhel/7/x86\_64/passenger-5.0.9-8.el7.x86\_64.rpm

##### k8s.gcr.io\_ingress-nginx\_controller:v0.34.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.34.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.34.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.34.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.34.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.34.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.35.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.35.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.35.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.40.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.40.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.40.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.40.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.40.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.40.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.40.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.40.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.40.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.41.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.41.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.41.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.41.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.41.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.41.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.41.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.41.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.41.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.42.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.42.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.42.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.43.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.43.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.43.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.44.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.44.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.44.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.45.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.45.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.45.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.46.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.46.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.46.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.47.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.47.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.47.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.48.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.48.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.48.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.49.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.49.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.49.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.49.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.49.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.49.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.49.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.49.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.49.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.49.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.49.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.49.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v0.51.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v0.51.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v0.51.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-alpha.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-alpha.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-alpha.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-beta.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-beta.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-beta.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-beta.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-beta.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.0-beta.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.0.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.0.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.0.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.1.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.1.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.1.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.1.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.1.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.1.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.1.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.1.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.1.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.1.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.1.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.1.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.10.6.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.10.6.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.10.6.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.6.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.6.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.6.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.7.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.7.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.7.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.11.8.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.11.8.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.11.8.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.0-beta.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.0-beta.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.0-beta.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.6.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.6.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.6.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.7.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.7.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.7.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.12.8.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.12.8.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.12.8.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.6.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.6.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.6.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.13.7.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.13.7.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.13.7.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.14.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.14.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.14.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.14.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.14.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.14.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.14.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.14.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.14.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.14.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.14.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.14.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.2.0-beta.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.2.0-beta.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.2.0-beta.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.2.0-beta.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.2.0-beta.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.2.0-beta.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.2.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.2.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.2.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.2.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.2.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.2.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.3.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.3.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.3.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.3.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.3.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.3.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.4.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.4.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.4.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.5.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.5.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.5.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.5.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.5.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.5.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.6.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.6.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.6.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.6.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.6.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.6.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.6.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.6.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.6.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.6.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.6.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.6.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.6.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.6.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.6.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.7.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.7.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.7.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.7.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.7.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.7.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.8.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.8.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.8.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.8.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.8.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.8.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.8.2.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.8.2.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.8.2.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.8.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.8.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.8.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.8.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.8.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.8.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.0-beta.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.0-beta.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.0-beta.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.0.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.0.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.0.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.1.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.1.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.1.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.3.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.3.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.3.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.4.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.4.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.4.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.5.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.5.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.5.tgz

##### k8s.gcr.io\_ingress-nginx\_controller:v1.9.6.tgz

* k8s.gcr.io\_ingress-nginx\_controller:v1.9.6.tgz/k8s.gcr.io\_ingress-nginx\_controller:v1.9.6.tgz

### Support for NGINX Plus

Support for the latest NGINX Plus release may differ from the NGINX support lifecycle, but we aim to stay current.

NGINX Plus version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

R36

2025-12-01

2027-11-30

1.329

-

-

Supported

R35

2025-08-13

2027-08-13

1.321

-

-

Supported

R34

2025-04-01

2027-04-01

1.313

-

-

Supported

R33

2024-11-19

2026-11-19

1.305

-

-

Supported

R32

2024-05-29

2026-05-29

1.293

-

-

Supported

R31

2023-12-19

2025-12-19

1.281

-

-

Supported

R30

2023-08-15

2025-08-15

1.271

-

-

Supported

R29

2023-05-23

2025-05-23

1.265

-

-

Supported

R28

2022-11-29

2024-11-29

1.255

-

-

Supported

R27

2022-06-28

2024-06-28

1.236

-

-

Supported

R26

2021-02-15

2023-02-15

1.234

-

-

Supported

R25

2021-09-28

2023-09-28

1.228

-

-

Supported

R24

2021-04-27

2023-04-27

1.215

-

-

Supported

R23

2020-12-08

2022-12-08

1.207

-

-

Supported

R22

2020-06-09

2022-06-09

1.193

-

-

Supported

R21

2020-04-07

2022-04-07

1.189

-

-

Supported[1](#fn-nginx-plus-1-def)

R20

2019-12-03

2021-12-03

1.175

-

-

Supported[1](#fn-nginx-plus-1-def)

R19

2019-08-13

2021-08-13

1.173

-

-

Supported[1](#fn-nginx-plus-1-def)

R18

2019-04-09

2021-04-09

1.161

-

-

Supported[1](#fn-nginx-plus-1-def)

R16 - R17

2018-09-05

2020-12-11

1.159

-

-

Supported[1](#fn-nginx-plus-1-def)

R15

2018-04-10

2020-04-10

1.143

-

-

Supported[1](#fn-nginx-plus-1-def)

R11 - R14

2016-10-25

2019-12-12

1.137

-

-

Supported[1](#fn-nginx-plus-1-def)

R1 - R10

2013-08-22

2018-08-23

-

-

2023-03-31

Not supported[2](#fn-nginx-plus-2-def)

1

Support for the CPU architecture PPCLE was added with OneAgent version 1.169 and ARM64 (AArch64) with OneAgent version 1.189.

2

Supported if the used binary is either in the list of [supported binaries](/docs/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries "Learn the details of Dynatrace support for NGINX.") or the corresponding debug information is available locally.

### Supported for OpenResty

Support for the latest OpenResty release may differ from the NGINX support lifecycle, but we aim to stay current.

OpenResty version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

1.27.1.2

2025-03-14

-

1.311

-

-

Supported

1.27.1.1

2024-10-16

-

1.305

-

-

Supported

1.25.3.2

2024-07-19

-

1.295

-

-

Supported

1.25.3.1

2024-01-04

-

1.283

-

-

Supported

1.21.4.3

2023-11-07

-

1.279

-

-

Supported

1.21.4.2

2023-09-19

-

1.273

-

-

Supported

1.21.4.1

2022-05-08

-

1.243

-

-

Supported

1.19.9

2021-08-06

-

1.223

-

-

Supported

1.19.3

2020-11-06

-

1.207

-

-

Supported

1.17.8

2020-07-04

-

1.199

-

-

Supported

1.15.8

2019-05-16

-

1.169

-

-

Supported

1.13.6

2017-11-13

-

1.145

-

-

Supported

1.11.2

2016-08-24

-

1.107

-

2023-03-31

Limited[1](#fn-openresty-1-def)

1

Supported if the used binary is in the list of [supported binaries](/docs/ingest-from/technology-support/application-software/nginx#nginx-supported-binaries "Learn the details of Dynatrace support for NGINX.").

### Support for Tengine

Support for the latest Tengine release may differ from the NGINX support lifecycle, but we aim to stay current.

Tengine version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

2.4.1

-

-

1.269

-

-

Supported

2.4.0

-

-

1.261

-

-

Supported

2.3.4

-

-

1.255

-

-

Supported

2.3.0 - 2.3.3

-

-

1.237

-

-

Supported

1.4.2 - 2.2.3

-

-

1.173

-

-

Supported

## NGINX HTTP connection metrics

The NGINX module captures HTTP connection metrics if you build your NGINX with [http\_stub\_status\_moduleï»¿](https://nginx.org/en/docs/http/ngx_http_stub_status_module.html).

How to build NGINX with http\_stub\_status\_module

Use the `--with-http_stub_status_module` configuration parameter.

How to check if an NGINX binary was built with http\_stub\_status\_module

Invoke `nginx -V` on your command line. This will return the NGINX configuration parameters.
Make sure that the output contains the `--with-http_stub_status_module` parameter.

## NGINX Plus metrics

The NGINX module captures NGINX Plus metrics from [NGINX Plus Status API (up to R15) or NGINX Plus API (R16+)ï»¿](https://www.nginx.com/blog/transitioning-to-nginx-plus-api-configuration-monitoring/).

The API needs to be turned on and accessible by the NGINX module. If the API is protected by NGINX authentication, ensure it's accessible from localhost for HTTP GET requests. The Nginx module requires the API configuration to be available from the start (adding the configuration during Nginx runtime and reloading it is not supported).

A notification appears on the NGINX process page in Dynatrace if the API for extended NGINX Plus metrics is not accessible.

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").


---


## Source: nodejs.md


---
title: Node.js
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/nodejs
scraped: 2026-02-16T09:21:38.685222
---

# Node.js

# Node.js

* Latest Dynatrace
* Reference
* 4-min read
* Updated on Nov 21, 2025

[Node.jsï»¿](https://nodejs.org) is a server-side framework based on the [V8 JavaScript engineï»¿](https://developers.google.com/v8/) by Google. Node.js has an asynchronous execution model and is frequently used for gluing or as a proxy tier within enterprise environments.

## Capabilities

Dynatrace provides extensive Node.js monitoring capabilities:

* Heap and process metrics
* Heap dumps
* CPU sampling
* Event loop metrics
* Insights into inbound and outbound HTTP calls
* Dedicated support for a variety of databases (includes query capture)
* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-js-api/) for capturing traces and ingesting metrics.  
  For more information, see [Instrument your JavaScript application on Node.js with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/nodejs "Learn how to instrument your JavaScript application on Node.js using OpenTelemetry and Dynatrace.")
* [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing
* [Continuous thread analysis for worker threads](#worker-threads)

See [our supported technologies matrix](/docs/ingest-from/technology-support#nodejs "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details about supported technologies that will be used in conjunction with Node.js.

## Support & desupport

Node.js follows an [LTS release modelï»¿](https://github.com/nodejs/Release).

Each odd-numbered version reaches EOL shortly after each new even-numbered version is released. Each even-numbered version eventually becomes an LTS release. For enterprise production environments, we recommend that you stick to LTS releases.

Whenever a new Node.js major version (even or uneven) is released, we add support for that version.

Dynatrace will follow this support model, but will support each Node.js version at least half a year longer to give our customers time for upgrades.

Node.js version

Vendor released

Vendor End of life

First supported Dynatrace OneAgent version

Last supported Dynatrace OneAgent version

Dynatrace support until

[Dynatrace support level](/docs/ingest-from/technology-support#support-levels)

25

2025-10-15

2026-06-01

1.333

-

2026-12-01

Not supported

24

2025-05-06

2028-04-30

1.329

-

2029-04-30

Supported

23

2024-10-16

2025-06-01

1.305

1.329

2025-12-01

Not supported

22

2024-04-23

2027-04-30

1.295

-

2028-04-30

Supported

21

2023-10-17

2024-06-01

1.281

1.303

2024-12-01

Not supported

20

2023-04-18

2026-04-30

1.271

-

2027-04-30

Supported

19

2022-10-18

2023-06-01

1.257

1.285

2023-12-01

Not supported

18

2022-04-19

2025-04-30

1.243

-

2026-04-30

Supported

17

2021-10-19

2022-06-01

1.235

1.265

2022-12-01

Not supported

16

2021-04-20

2023-09-11

1.219

-

2024-09-11

Limited[1](#fn-node-js-1-def)

15

2020-10-20

2021-06-01

1.207

1.233

2021-12-01

Not supported

14

2020-04-21

2023-04-30

1.195

-

2024-04-30

Limited[1](#fn-node-js-1-def)

13

2019-10-22

2020-06-01

1.183

1.205

2020-12-01

Not supported

12

2019-04-23

2022-04-30

1.171

-

2023-04-30

Limited[1](#fn-node-js-1-def)

11

2018-10-23

2019-06-30

1.159

1.181

2019-12-31

Not supported

10

2015-04-24

2021-04-30

1.147

1.329

2022-04-30

Not supported[2](#fn-node-js-2-def)

9

2017-10-01

2018-06-30

-

1.157

2018-12-31

Not supported

8

2017-05-30

2019-12-31

-

1.239

2020-12-31

Not supported

1

Limited support: Dynatrace can only solve problems that can be reproduced on supported versions.

2

Not supported: Instrumentation is deprecated off by default on OneAgent version >=1.321 and <=1.329. Define DT\_SUPPORT\_DEPRECATED\_NODE\_VERSIONS environment variable to opt in on these OA versions.

## Continuous thread analysis for worker threads

Node.js version 12+ OneAgent version 1.251+ Dynatrace version 1.256+

[Continuous thread analysis](/docs/observe/application-observability/profiling-and-optimization/continuous-thread-analysis "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") for [worker threadsï»¿](https://nodejs.org/api/worker_threads.html#worker-thread) can automatically identify CPU-intensive threads and pinpoint scalability issues when work is distributed across many threads so that you can solve performance bottlenecks before your end users are impacted.

Continuous thread analysis in action

Statistics about the `main` and `worker` threads:

![Node.js worker thread stats](https://dt-cdn.net/images/worker-thread-stats-1815-5a10cfd6f5.png)

CPU time consumed by the various `worker` threads:

![Node.js worker thread CPU times](https://dt-cdn.net/images/worker-thread-cpu-times-1815-7223ec5892.png)

To get started with the continuous thread analysis for worker threads, activate the [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Node.js worker threads monitoring** and **Node.js code module preloading**.

Limitations

Node.js specific metrics (for example, memory, garbage collection, and event-loops) are only reported for the `main` thread.

Class browsing (required for the custom messaging services of kafkajs) is limited to the `main` thread.

There is no automatic transaction tracing in place between the `main` and `worker` threads. For tracing transactions across threads, you can either use [OpenTelemetry tracing](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.") or the [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.").

## Known limitations

* Due to platform limitations of JavaScript and Node.js, code-level visibility is limited compared to .NET or Java.
* In conjunction with unsupported third-party modules, context can be lost in asynchronous callbacks. In such cases, please contact a Dynatrace product expert via live chat within your Dynatrace environment.
* OneAgent version 1.279+ CPU times are not reported for Node.js services. These numbers were misleading, since by design a major part of any operation is handled asynchronously inside the Node.js runtime without the possibility to correlate the actual CPU time to a specific service.
* Web Streams, WebSocket Client are not supported.
* Node.js features marked as 'experimental' are not supported.
* Using the NPM module [esmï»¿](https://github.com/standard-things/esm) in [variant 1 for packagesï»¿](https://github.com/standard-things/esm/tree/3.2.25#getting-started) might result in reduced visibility (especially if used for the main application script). It's preferable to use variant 2 to preload `esm` via the `-r` command line option.
* There is currently only limited support for [ECMAScript modulesï»¿](https://nodejs.org/api/esm.html) (aka "ES6 modules"):

  + If the main script file itself is an ECMAScript module OneAgent version 1.219+ with [Agent preloading](/docs/whats-new/preview-releases#oneagent-1-219-nodejs-agent-preloading "Learn about our Preview releases and how you can participate in them.") enabled is needed for the OneAgent to be injected into the Node.js process.
  + Instrumentation of ECMAScript modules is currently not available. This limits support for `kafkajs` in case the user defined entrypoint for the KafkaJs sensor is inside an ECMAScript module.
* **Webpack** bundles all modules into a single file by default. OneAgent is unable to instrument bundled modules. To work around this limitation, all modules that need to be instrumented by OneAgent (such as `express`, `mongodb`, and `pg`) need to be externalized in the webpack configuration. For details, see the [webpack externalsï»¿](https://webpack.js.org/configuration/externals/) documentation.
* Using **Webpack** or other bundlers might also have an impact on automatic vulnerability detection. This is because the software components cannot be detected, as they are hidden behind the bundler configuration and not available at runtime. Only packages that are deployed as external packages can be detected and reported.

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Monitoring

* [How do I monitor Cloud Foundry applications?](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")

### See also

* [Blog: Understanding Garbage Collection and hunting Memory Leaks in Node.jsï»¿](https://www.dynatrace.com/news/blog/understanding-garbage-collection-and-hunting-memory-leaks-in-node-js/)
* [Blog: How to track down CPU issues in Node.jsï»¿](https://www.dynatrace.com/news/blog/how-to-track-down-cpu-issues-in-node-js/)
* [Blog: All you need to know to really understand the Node.js Event Loop and its Metricsï»¿](https://www.dynatrace.com/news/blog/all-you-need-to-know-to-really-understand-the-node-js-event-loop-and-its-metrics/)


---


## Source: php.md


---
title: PHP
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/php
scraped: 2026-02-16T09:20:48.818384
---

# PHP

# PHP

* Latest Dynatrace
* Reference
* 1-min read
* Published Jul 09, 2018

PHP is a server-side scripting language particularly well-suited for web development but also popular in general-purpose programming. Originally created by Rasmus Lerdorf in 1994, new versions are now produced by The PHP Group.

PHP is processed by a PHP interpreter that's implemented in Apache HTTP Server, the Common Gateway Interface (CGI) executable, and command-line interface (CLI).

Dynatrace provides extensive PHP monitoring capabilities:

* All database statements and SQL metrics
* Compilation, execution, and response time analysis
* Supported caching technologies: Redis (php-redis and predis PHP libraries) and Memcached (memcached PHP extension)
* Detailed request and response metrics
* Information about restarts, crashes, and deployment changes
* Insight into stack issues (like Stack Overflow)
* Automatically collected PHP-FPM metrics
* Location of hotspots at the code level
* Analysis of requests to external services via CURL, SOAP interfaces, and other remote interfaces, such as `fopen` or `get_file_contents`
* [OneAgent SDK](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing

See [the environments and versions that Dynatrace supports](/docs/ingest-from/technology-support#php "Find technical details related to Dynatrace support for specific platforms and development frameworks.") in conjunction with PHP.

### Topics

* [Supported PHP versions](/docs/ingest-from/technology-support/application-software/php/php-supported-versions "Find out the support timeline for all PHP versions.")
* [Full-stack PHP monitoring](/docs/ingest-from/technology-support/application-software/php/full-stack-monitoring "Find out how Dynatrace supports full-stack monitoring for PHP.")
* [Code-level visibility for PHP](/docs/ingest-from/technology-support/application-software/php/code-level-visibility "Learn how Dynatrace offers code-level visibility for its PHP deep-monitoring support.")
* [PHP-FPM monitoring](/docs/ingest-from/technology-support/application-software/php/php-fpm "Learn how Dynatrace PHP-FPM monitoring provides information about connections, slow requests, and processes.")

### See also

[Dynatrace Open Q&A: What is the desupport policy for PHP?ï»¿](https://community.dynatrace.com/t5/Dynatrace-Open-Q-A/What-is-the-desupport-policy-for-PHP/m-p/42853)

[Blog: Monitor PHP in Windows environmentsï»¿](https://www.dynatrace.com/news/blog/monitor-php-in-windows-environments-beta/)

[Blog: General availability of PHP deep monitoringï»¿](https://www.dynatrace.com/news/blog/general-availability-of-php-deep-monitoring/)

[Blog: New response time analysis views!ï»¿](https://www.dynatrace.com/news/blog/new-response-time-analysis-views/)


---


## Source: ruby.md


---
title: Ruby
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/ruby
scraped: 2026-02-16T09:21:55.338732
---

# Ruby

# Ruby

* Latest Dynatrace
* Reference
* 1-min read
* Published Feb 01, 2022

You can send data from your Ruby application to Dynatrace via OpenTelemetry. See also

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-ruby/) for capturing traces.

  + [Instrument your Ruby application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/ruby "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.")


---


## Source: rust.md


---
title: Rust
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/rust
scraped: 2026-02-16T09:21:30.452808
---

# Rust

# Rust

* Latest Dynatrace
* Reference
* 1-min read
* Published Dec 20, 2022

You can send data from your Rust application to Dynatrace via OpenTelemetry. See also

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-rust) for capturing traces.

  + [Instrument your Rust application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/rust "Learn how to instrument your Rust application using OpenTelemetry and Dynatrace.")


---


## Source: application-software.md


---
title: Runtimes
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software
scraped: 2026-02-15T09:05:52.340712
---

# Runtimes

# Runtimes

* Latest Dynatrace
* 1-min read
* Published Mar 29, 2019

The following runtimes can be monitored within Dynatrace.

[### C++](/docs/ingest-from/technology-support/application-software/cpp "Learn how to instrument your C++ application with OpenTelemetry as a data source for Dynatrace.")[![Elixir](https://dt-cdn.net/images/elixir-logo-180-b773ecbdae.png "Elixir")

### Elixir](/docs/ingest-from/technology-support/application-software/erlang-elixir "Learn how to instrument your Erlang/Elixir application with OpenTelemetry as a data source for Dynatrace.")[### Erlang](/docs/ingest-from/technology-support/application-software/erlang-elixir "Learn how to instrument your Erlang/Elixir application with OpenTelemetry as a data source for Dynatrace.")[### Go](/docs/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.")[### Java](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.")[### .NET](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.")[### NGINX](/docs/ingest-from/technology-support/application-software/nginx "Learn the details of Dynatrace support for NGINX.")[### NodeJS](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.")[### PHP](/docs/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.")[### Python](/docs/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.")[### Ruby](/docs/ingest-from/technology-support/application-software/ruby "Learn how to instrument your Ruby application with OpenTelemetry as a data source for Dynatrace.")[![Rust](https://dt-cdn.net/images/rust-logo-gray-8d1a6c296b.svg "Rust")

### Rust](/docs/ingest-from/technology-support/application-software/rust "Learn how to instrument your Rust application with OpenTelemetry as a data source for Dynatrace monitoring.")


---


## Source: known-solutions-and-workarounds.md


---
title: Known solutions and workarounds
source: https://www.dynatrace.com/docs/ingest-from/technology-support/known-solutions-and-workarounds
scraped: 2026-02-16T09:20:59.118263
---

# Known solutions and workarounds

# Known solutions and workarounds

* Latest Dynatrace
* 14-min read
* Updated on Feb 26, 2024

This page details a number of resolved issues and solutions to issues that have been reported to the Dynatrace Support team.

## OneAgent prevents startup of Elasticsearch 8.18+

**Issue:**

OneAgent prevents startup of Elasticsearch 8.18+

**Solution:**

For more information, kindly visit [this pageï»¿](https://community.dynatrace.com/t5/Heads-up-from-Dynatrace/OneAgent-prevents-startup-of-Elasticsearch-8-18/ta-p/278744)

## OneAgent on a SAP HANA host

**Issue:**

OneAgent installed on a HANA host may interfere with database updates if it has automatic process injection enabled (default).

**Solution:**

Disable process auto-injection for a OneAgent installed on a SAP HANA host.

### Disable auto-injection at installation time

To install OneAgent with the parameters to enable Infrastructure Monitoring mode and disable process injection, run the command below:

```
/bin/sh Dynatrace-OneAgent-Linux-<version>.sh --set-monitoring-mode=infra-only --set-auto-injection-enabled=false
```

### Disable auto-injection after OneAgent installation

To disable auto-injection after OneAgent is installed

1. Open a terminal on your HANA host.
2. Run the `oneagentctl` command-line tool with the following parameters to enable Infrastructure Monitoring mode and disable process injection. The command will also restart the OneAgent service to automatically apply your changes.

```
./oneagentctl --set-monitoring-mode=infra-only --set-auto-injection-enabled=false --restart-service
```

For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

#### Dynatrace web UI

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find your HANA host and select it.
3. Select **More** (**â¦**) > **Settings** > **Monitoring**.
4. Turn off **Full-stack monitoring** and **Auto-injection**.

## Alpine Linux/musl-libc, Memory allocation

**Issue:**

On musl-libc-based Alpine Linux systems, each executable has its memory limits which are controlled via the `MPROTECT` parameter. When monitoring an musl-libc-based Alpine Linux application with Dynatrace OneAgent, your process (for example, a Java process) may exceed the specified memory limit. When this is the case, the subsequent memory allocation will fail with a message like `There is insufficient memory for the Java Runtime Environment to continue.`

**Solution:**

To overcome such issues, it's recommended that you ignore the memory protection parameter for executables that you plan to monitor with Dynatrace OneAgent. To do this, you must install the paxctl tool using:

`apk add paxctl`

You can then remove the memory check, for example

`paxctl -m /usr/lib/jvm/java-1.8-openjdk/jre/bin/java`

For 3rd-party executables not shipped by Alpine, you'll be notified that

`<file> does not have a PT_PAX_FLAGS program`

In such instances, convert your file beforehand, for example

`paxctl -C /usr/lib/jvm/java-1.8-openjdk/jre/bin/java`

## Alpine Linux/musl-libc, GNU C Library (glibc) compatibility packages

**Issue:**

Binaries built against GNU C Library (glibc) running on Alpine based Linux systems via **gcompat (GNU C Library compatibility layer for musl)** package or **libc6-compat (compatibility libraries for glibc)** package are not supported.

**Solution:**

Please migrate your build pipeline to natively compile and package against the Alpine based Linux.

## PHP running in Apache on Windows, Stack size

**Issue:**

The default stack size of Apache on Windows is 1 MB, which is rather low compared to other platforms. Therefore, the additional memory footprint involved in enabling Dynatrace monitoring for PHP can lead to stack overflows.

**Solution:**

This problem can be solved by changing the stack size to 8 MB, which is the default on Linux.

```
<IfModule mpm_winnt_module>



ThreadStackSize 8388608



</IfModule>
```

## Cloud Foundry, IBM WebSphere Liberty buildpack

**Issue:**

The recommended version of IBM WebSphere Liberty buildpack changed from `v3.7-20170118-2046` to `v3.9-20170419-1403` due to known issues related to a limitation of the JVM command line to 512 characters and an issue with trailing slashes.

**Solution:**  
Please use IBM WebSphere Liberty buildpack version v3.9-20170419-1403+

## Host, Ubuntu 16.10

**Issue:**

Due to compile optimization changes in the C runtime packages provided with Ubuntu 16.10, new stack-alignment requirements have been introduced. OneAgent versions earlier than 1.103.237 don't yet fulfill these requirements. Using versions of OneAgent earlier than 1.103.237 may lead to process crashes during dynamic symbol resolution (`dlsym`) calls in the C runtime.

**Solution:**

Update to OneAgent version 1.103.237 or higher. This version of OneAgent will be available to all Dynatrace environments by October 20th, 2016. Here are the instructions for upgrading OneAgent:

1. Go to **Settings** > **Preferences** (only visible to environment admins).
2. Ensure that the **Automatically update OneAgent instances** setting is enabled. OneAgent version 1.103.237 will be automatically deployed once itâs available on your environment.
   If **Automatically update One Agent instances** is disabled, select **OneAgent version 1.103.237 or higher** and click **Update now**.

## Java, IBM J9

**Issue:**

In rare situations, when implementing a try-catch-finally block and catching a multi-type exception with Java 7, the exception is caught, but the source code in the finally block doesn't execute. This issue has been fixed since IBM J9.

**Solution:**

Fixed since IBM J9

* 7 R1 SR2 FP11 (7.1.3.0)
* 7 SR9 (7.0.9.0)
* 8 SR1 (8.0.1.0)

**Source:**

* [IBM 1IV68110ï»¿](https://www-01.ibm.com/support/docview.wss?uid=swg1IV68110)

## Java, WebSphere MQ , JMS

**Issue:**

When using WebSphere MQ via JMS, Dynatrace isn't always able to determine the queue name and may report the queue name as 'unavailable'. This happens when MQ messages have not been properly mapped to JMS.

**Solution:**

Follow the IBM documentation for [mapping JMS messages onto IBM MQ messagesï»¿](https://www.ibm.com/support/knowledgecenter/SSFKSJ_8.0.0/com.ibm.mq.dev.doc/q031990_.htm). Once the `MQRFH2` header has been properly mapped, Dynatrace will pick up the correct queue name.

## Java, Oracle HotSpot/OpenJDK

**Issue:**

A known issue in Oracle HotSpot and OpenJDK can lead to a JVM deadlock in `ThreadTimesClosure` or incomplete CPU timings of background activities. Be sure to update to Oracle HotSpot 6u38/7u40 or OpenJDK 7u45 and higher to benefit from this solution.

**Solution:**

Fixed in Oracle HotSpot 6u38/7u40 and OpenJDK 7u45

**Source:**

* [Source Oracle HotSpot 6 (bug 7196045))ï»¿](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=7196045)
* [Source Oracle HotSpot 7 (bug 8005479)ï»¿](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=8005479)
* [Source OpenJDK (JDK-7196045)ï»¿](https://bugs.openjdk.java.net/browse/JDK-7196045)

**Issue:**

A known issue in Oracle HotSpot and OpenJDK can lead to a JVM crash when a JVMTI agent is loaded, [class data sharingï»¿](https://docs.oracle.com/en/java/javase/11/vm/class-data-sharing.html#GUID-7EAA3411-8CF0-4D19-BD05-DF5E1780AA91) is turned on, and the `classes.jsa` file exists. This is not normally the case, but it does occur in Docker environments, especially with Java 11 where class data sharing is set to `auto`.

**Solution:**

Change the java command line to turn off class data sharing via -Xshare:off.

**Source:**

* [Source OpenJDK (JDK-8212200)ï»¿](https://bugs.openjdk.java.net/browse/JDK-8212200)

## Java, Spring, AspectJ

**Issue:**

Some customers have reported the following `NullPointerException` during startup of their Java Spring or AspectJ applications. AspectJ has resolved this issue in version 1.6+. Ensure that the classpath is updated to use AspectJ 1.6+.

Message: `NullPointerException at`

```
`org.aspectj.weaver.reflect.Java15AnnotationFindergetAnnotations



(Java15AnnotationFinder.java:109)`
```

**Solution:**

Fixed since Spring 2.5.4/AspectJ 1.6

**Source:**

* [SPR-4390ï»¿](https://jira.spring.io/browse/SPR-4390)

## Java/Real User Monitoring/Apigee

**Issue:**

Real User Monitoring of Java applications may trigger a `ClassCastException` error upon a type cast to the implemented `HttpServletRequest` interface because Dynatrace replaces the original `HttpServletRequest` implementation with a `RequestWrapper` for automatic RUM JavaScript injection.

This crash also occurs for customers using [Apigeeï»¿](https://apigee.com).

**Solution:**

You have a few options:

1. Change your source code so that it doesn't expect a specific implementation of the `HttpServletRequest` interface.
2. If you're using a 3rd party framework, you can reach out to your framework vendor.
3. For Apigee, we've disabled Real User Monitoring auto-injection. Manual Real User Monitoring injection isn't affected and can be used as a workaround.
4. You can use a web server in front of Javaâthe web server will auto-inject the Real User Monitoring JavaScript and thereby avoid the crash.

**Source:**  
n/a

## Java CPU overhead

**Issue:**

Periodically, spikes of CPU usage or overall CPU usage occur when instrumenting Preview for JBoss. Querying JMX measures cause these spikes. JMX calls done in 10 sec intervals lead to a CPU spike on certain versions affected by this JBoss bug. Versions 6.4.x are considered to be problematic.

**Solution:**

Solution is to upgrade to Preview for JBoss and/or contact RedHat.

**Source:**

* [Bug 1367784ï»¿](https://bugzilla.redhat.com/show_bug.cgi?id=1367784)

## UI/Docker

**Issue:**

With Docker versions 1.10.3 - 1.11, CPU, memory, and network container statistics are missing from the UI because data requests sent to containers via `docker stats` time out. Restarting Docker addresses this issue temporarily.

**Solution:**

Fixed since Docker 1.12. Upgrade to Docker 1.12.

**Source:**

* [Issue 22655ï»¿](https://github.com/docker/docker/issues/22655)

## UI/IIS

**Issue:**

Due to a lack of Windows Performance Counters, the **Further details** tab may be not visible in the UI for IIS processes, even following IIS restart. No errors are raised during OneAgent injection.

**Solution:**

This can occur if there is a problem with the Performance Counter Library in the Windows Registry. To check this:

Using a Windows command, verify that the metrics are not retrievable from the Windows Registry:
typeperf `"\Process(w3wp*)\ID Process" -sc 15`
Alternatively, use `Perfmon.exe` to see if data is available for the counters or to confirm that the counters don't exist.

Consult Microsoft technical documentation to rebuild the performance libraries in the registry.

**Source:**

* [KB 00956ï»¿](https://support.microsoft.com/en-us/kb/300956)

## .NET, IIS

**Issue:**

If IIS monitoring is enabled for an ASP.NET application using .NET >= 4.5 and < 4.6, in rare circumstances the application could fail with an unhandled `NullReferenceException`.

Message: `System.NullReferenceException at`

```
`System.Web.Security.Roles.IsUserInRole(String username, String roleName)`
```

**Solution:**

Fixed since .NET 4.6.

* [Sourceï»¿](https://connect.microsoft.com/VisualStudio/feedbackdetail/view/967133/roles-getrolesforuser-throw-a-nullreferenceexception-in-a-wcf-service-which-is-hosted-in-asp-net-with-the-aspnetcompatibilityenabled-define-to-false)

## .NET, Cassette

**Issue:**

Customers reported a crash when using the Cassette web asset management library.

Message: Crash at

```
`[TinyIoCResolutionException: Unable to resolve type: Cassette.Views.BundlesDocumentationer]`
```

**Solution:**

As a workaround, you can use the file system as Cassette's cache by specifying a directory in your `web.config` file as follows:

```
`<cassette cacheDirectory="App_Data\Cassette" />`
```

Potentially fixed in v2.4.1

**Source:**

* [Pull 441ï»¿](https://github.com/andrewdavey/cassette/pull/441)

## .NET, ConfuserEx

**Issue:**

Using the assembly-obfuscation tool ConfuserEx can sometimes crash .NET applications because the ConfuserEx assembly doesn't allow "profilers" like Dynatrace.

Message: Crash at

```
`System.Environment.FailFast(System.String)`
```

**Solution:**

Disable ConfuserEx obfuscation or disable Dynatrace monitoring at the process level.

**Source:**

* [Sourceï»¿](https://github.com/yck1509/ConfuserEx/blob/816172adcb1ea2a6c74a964274373987fc2e9fe5/Confuser.Runtime/AntiDebug.Antinet.cs)

## Real User Monitoring, Chrome

**Issue:**

Real User Monitoring analysis with Google Chrome can lead to browser crashes when some resources can't be loaded.

Message: Crash at

```
`window.performance.getEntriesByType('resource')`
```

**Solution:**

Until Chrome provides a fix for this issue, make sure that all resources are loaded successfully (no 301 responses) or disable **W3C resource timing for third party/CDN**.

To disable W3C resource timing for third party/CDN:

1. Go to **Frontend**.
2. Select the application you want to edit.
3. Click the **More** (**â¦**) button.
4. Click **Edit**.
5. Click **Content capture**.
6. Set the **W3C resource timing for third party/CDN** switch to **Off**.

**Source:**

* [Issue 586443ï»¿](https://bugs.chromium.org/p/chromium/issues/detail?id=586443)

## Agentless Real User Monitoring, Chrome

**Issue:**

Users may see a browser warning in Chrome's Developer Console if they are on slow connections such as 2G networks.

Message:
`A Parser-blocking, cross-origin script, https://js-cdn.dynatrace.com/jstag/148709fdc4b/ruxitagent_2fgjqrx_10111170210093847.js, is invoked via document.write. This may be blocked by the browser if the device has poor network connectivity. See https://www.chromestatus.com/feature/5718547946799104 for more details.`

**Solution:**

1. Go to **Frontend**.
2. Select the application you want to configure.
3. Click the **Browse (â¦)** button and select **Edit**.
4. In the **Setup** section, select **Agentless monitoring setup**.
5. Disable the **Easy monitoring** switch.

The only downside of this change is that every time you make a configuration change you have to copy and re-inject the Real User Monitoring JavaScript again. Therefore, it's better to use the REST API to get the updated tag.

**Source:**

* [Update 2016/08ï»¿](https://developers.google.com/web/updates/2016/08/removing-document-write)

## Real User Monitoring, jQuery

**Issue:**

In the course of Real User Monitoring, failing asynchronous JQuery user actions lead to action timeouts after 180 seconds, but no error is reported. This is caused by a known jQuery limitation.

**Solution:**

JQuery has not provided a fix for this problem. To resolve this issue, fix the failing jQuery call on your end (for example, an AJAX request to a missing resource) or disable jQuery in XHR (Ajax) detection settings and enable basic XHR detection.

To disable JQuery detection and enable basic XHR detection:

1. Go to **Frontend**.
2. Select the application you want to edit.
3. Click the **More** (**â¦**) button.
4. Click **Edit**.
5. Click **XHR (Ajax)** detection.
6. Set the **JQuery, Backbone.js** switch to **Off**.
7. Set the **Basic XHR detection** switch to **On**.

**Source:**

* [Ticket 9613ï»¿](https://bugs.jquery.com/ticket/9613)

## Real User Monitoring, Ext JS

**Issue:**

In large, complex Ext JS applications customers experienced client side response time degradation like a web browser notification about an unresponsive script. Due to the internal event handling mechanism of Ext JS the application can be running slow if too many events are triggered which are captured by the RUM JavaScript.

**Solution:**

Turn off extended Ext JS event capturing in Real User Monitoring settings.

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Capturing** > **Custom configuration properties**.
5. Select **Add a custom configuration property** and enter `exteventsoff=1`.

If certain user actions are not captured afterwards, use the JavaScript API to trigger actions manually.

## Real User Monitoring, Salesforce

**Issue:**
When [injecting RUM](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications") into Salesforce, you may experience the application stuck in "loading" when viewing records from a search result. When this happens, browser debugging displays the JavaScript error: `Wrong number of arguments or invalid property assignment on b.b.open,arguments,b.b`.

This occurs when the RUM JavaScript is not the first JavaScript loaded on the page. There can be JavaScript code loading in the heading that has a negative impact on the RUM JavaScript.

**Solution:**
Shifting the RUM JavaScript to load before any JavaScript resolves this issue.

**Issue:**
Dynatrace RUM isn't working for Salesforce applications based on the [Lightning Component Frameworkï»¿](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm).

The reason for this is that many Salesforce applications and offerings are based on [Lightning Component Frameworkï»¿](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/intro_framework.htm). This framework has a security architecture called [Lightning Lockerï»¿](https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/security_code.htm), which restricts access to DOM elements and therefore influences the Dynatrace RUM JavaScript. Whenever the Locker code is loaded and executed before the Dynatrace RUM JavaScript, monitoring won't work, independently of whether you add the [RUM JavaScript](/docs/observe/digital-experience/web-applications/initial-setup/rum-injection "Configure automatic injection of the RUM JavaScript into the pages of your applications").

**Solution:**
There is currently no solution from the Dynatrace side. Please contact Salesforce support. Perhaps there is a way to allow the Dynatrace RUM JavaScript.

## Real User Monitoring, Salesforce Commerce

**Issue:**

There is currently an incompatibility between Dynatrace Agentless RUM and Salesforce Commerce. This is due to a reserved character within the Salesforce compiler.

**Solution:**

Replace `#` with `${'#'}` in the Dynatrace RUM JavaScript.

## Real User Monitoring, Visually complete, Internet Explorer 11

**Issue:**

Enabling the [**Visually complete**](/docs/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Learn how to use 'Visually complete' and 'Speed index' metrics.") application setting while using Dynatrace with Internet Explorer 11 can lead to a complete page crash or hanging in cases where heavy `<table>` or table-like (using the style attribute `display:table`) DOM mutations occur. This tends to be more common with single-page applications. Simply monitoring mutations with the MutationObserver, as is done for Visually complete, can crash the page once it's loaded. Here is a [simple reproduction of the issueï»¿](https://jsfiddle.net/gd88q1n3/2/) with a table-like element mutation crash.

#### More information on Visually complete and Speed index

Speed index and Visually complete metrics are only available on browsers that support [`mutationobservers`ï»¿](https://developers.google.com/web/updates/2012/02/Detect-DOM-changes-with-Mutation-Observers). This includes the following browsers:

* Microsoft Internet Explorer 11
* Microsoft Edge 15 or later
* Firefox 57 or later
* Google Chrome 61 or later

Speed index is available only for load actions. Visually complete is available for all actions, including load actions, but not for AJAX requests that don't affect the DOM.

**Solution:**

Microsoft fixed the bulk of this issue for `<table>` element mutations in a [recent updateï»¿](https://support.microsoft.com/en-za/help/4025252/cumulative-security-update-for-internet-explorer-july-11-2017). Update Internet Explorer 11 to this version to fix this issue in most cases.

Elements with the style attribute `display:table` still run into this problem following update of Internet Explorer 11. For this reason, we've created a feature flag you can use to disable Visually complete within Internet Explorer 11 only. To enable this feature flag, Please contact a Dynatrace product expert via live chat within your environment..

## Redhat Enterprise Linux 7.4

**Issue:**

RHEL v7.4 (upgraded from v7.3 or fresh install) comes with the stix-fonts package. When this package is installed, the default font changes from `Utopia` to `STIX`. As a result, Java default fonts are mapped to `STIX`, including the `sans-serif` font family. However, the `STIX` fonts don't seem to be compatible with Java (OpenJDK + IBM JDK) and cause exceptions and bad calculated artefacts when using `java.awt`, which is the case with `JasperReports`.

For Dynatrace Managed, which is based on Java, this issue was experienced as a problem in Smartscape. More specifically, selecting any item in Smartscape shows an unspecific error message that something went wrong.

**Solution:**

Create a file `/etc/fonts/local.conf` with the content shown below to explicitly make `Utopia` the default font again.

```
<?xml version='1.0'?>



<!DOCTYPE fontconfig SYSTEM 'fonts.dtd'>



<fontconfig>



<alias>



<family>serif</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>sans-serif</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>monospace</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>dialog</family>



<prefer><family>Utopia</family></prefer>



</alias>



<alias>



<family>dialoginput</family>



<prefer><family>Utopia</family></prefer>



</alias>



</fontconfig>
```

**Source:**

* [Bug 1484079ï»¿](https://bugzilla.redhat.com/show_bug.cgi?id=1484079#c8)

## IBM HTTP Server (IHS) 8.5

**Issue:**

IHS 8.5 on Linux crashes with segmentation fault.

**Solution:**

Disable prelink on IHS server.

**Source:**

* [Sourceï»¿](https://www.google.at/search?q=prelink+crash)

## Adobe Dispatcher

**Issue:**

When using Adobe Dispatcher with a web server monitored by Dynatrace OneAgent, the RUM JavaScript agent tag is injected twice into the HTML page. As a consequence, the RUM JavaScript agent will be executed twice at the browser, producing unnecessary load (e.g. the beacons will be sent twice, etc.).

The reason for this is that Adobe Dispatcher doesn't cache HTTP response headers by default and so the header X-OneAgent-JS-Injection "gets lost" for already injected sites, which are served from the cache. If this header is not present, the webserver agent injects (another) RUM JavaScript agent tag, even if it's already present in the cached content.

**Solution:**

The dispatcher needs to be configured to cache the response header "X-OneAgent-JS-Injection". To avoid double injection of the RUM JavaScript agent tag when using Adobe Dispatcher with a web server monitored by Dynatrace OneAgent, add "X-OneAgent-JS-Injection" to the `/cache/headers` section of the Adobe Dispatcher configuration:

```
/cache



{



# Cache configuration



# <existing configuration>



# ...



/headers



{



"X-OneAgent-JS-Injection"



}



}
```


---


## Source: mainframe-technology-support.md


---
title: Mainframe technology support
source: https://www.dynatrace.com/docs/ingest-from/technology-support/mainframe-technology-support
scraped: 2026-02-16T09:20:55.739935
---

# Mainframe technology support

# Mainframe technology support

* Latest Dynatrace
* 3-min read
* Published Mar 19, 2023

Dynatrace supports monitoring of the technologies and versions listed below on IBM z/OS.

For the supported operating systems of the zRemote module, see [System requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#system-requirements "Prepare and install the zRemote for z/OS monitoring.").

Technology support version schema

Definition of the technology support version schema with examples:

* **Major version 5 is supported**

  + Major version 5 is supported, including all of its minor versions like 5.1 and 5.2
  + Other major versions are not supported like 6 and 7
* **Minor version 5.1 is supported**

  + Minor version 5.1 is supported, including all of its patch versions like 5.1.1 and 5.1.2
  + Other minor versions are not supported like 5.2 and 5.3
* **Patch version 5.1.1 is supported**

  + Patch version 5.1.1 is supported
  + Other patch versions are not supported like 5.1.2 and 5.1.3
* **Version range 5.1 â 5.3 is supported**

  + Minor versions 5.1, 5.2, and 5.3 are supported, including all of their patch versions like 5.1.1, 5.2.1, and 5.3.1
  + Other minor versions are not supported like 5.0 and 5.4
* **The minimum required version is 5+**

  + All major, minor, and patch versions starting from version 5 are supported, like 5, 5.1, 5.1.1, and 6

## IBM z/OS

To get started with monitoring, see [Dynatrace for z/OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.").

| Operating system | Versions |
| --- | --- |
| IBM z/OS | 2.3, 2.4, 2.5, 3.1, 3.2 |

## IBM CICS

To get started with monitoring, see [Install the CICS module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics "Install the Dynatrace CICS module.").

| IBM CICS | Versions |
| --- | --- |
| CICS Transaction Server | 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 6.1, 6.2 |
| CICS MQ Bridge |  |
| CICS MQ Trigger Monitor |  |
| CICS HTTP/S |  |
| CICS JSON (non-Java JSON pipeline) |  |
| CICS SOAP (over HTTP) |  |
| CICS file access[1](#fn-1-1-def) |  |

1

The CICS file access methods VSAM and BDAM are supported.

| Database client | Versions |
| --- | --- |
| IBM Db2 | 11, 12, 13 |
| IBM IMS DB[1](#fn-2-1-def) |  |

1

The database access method DL/I is supported.

| Messaging client | Versions |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2, 9.3 |

## IBM IMS

To get started with monitoring, see [Install the IMS module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims "Install the Dynatrace IMS module.").

| IBM IMS | Versions |
| --- | --- |
| IMS [1](#fn-3-1-def)[2](#fn-3-2-def) | 13, 14, 15 |
| IMS TM Resource Adapter | 13, 14, 15 |
| IMS MQ Bridge[1](#fn-3-1-def) |  |
| IMS MQ Trigger Monitor |  |
| IMS Connect API[1](#fn-3-1-def) | 3.2 |

1

Only inbound tracing is supported.

2

Fast Path and BMP transaction tracing is only supported for IMS 15.

| Database client | Versions |
| --- | --- |
| IBM Db2 | 11, 12, 13 |
| IBM IMS DB[1](#fn-4-1-def) |  |

1

The database access methods DL/I and Fast Path are supported.

| Messaging client | Versions |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2, 9.3 |

## z/OS Java

To get started with monitoring, see [Install the z/OS Java module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java "Set up Java monitoring on z/OS using the Java module.").

| Java Runtime | Versions |
| --- | --- |
| IBM JVM for z/OS | 8 |
| IBM Semeru for z/OS | 11 |
| IBM Semeru for z/OS | 17 |
| IBM Semeru for z/OS[1](#fn-5-1-def) | 21 |

1

Virtual Threads are currently not supported

The technologies listed below are supported only when used with a supported Java runtime.
In some cases, a manual Java runtime upgrade may be required to remain supported
(for example, the IBM CICS Transaction Gateway earlier than 9.2).

| Technology | Versions |
| --- | --- |
| IBM WebSphere Application Server | 8.5.5, 9.0 |
| IBM WebSphere Liberty | 18, 19, 20, 21, 22, 23, 24, 25 |
| IBM z/OS Connect [1](#fn-6-1-def)[2](#fn-6-2-def) | 3.0.30+ |
| IBM CICS Transaction Gateway [3](#fn-6-3-def)[4](#fn-6-4-def) | 9.0, 9.1, 9.2, 9.3 |
| IBM IMS SOAP Gateway [5](#fn-6-5-def) | 3.2 |
| Apache HttpClient | 3.1, 4 |

1

Only the z/OS Connect standalone configuration is supported.

2

Only the CICS, IMS, and IBM MQ service providers are supported.

3

Only EXCI and IPIC protocols are supported.

4

WAS local mode configuration is not supported.

5

Only inbound tracing is supported.

| Database framework | Versions |
| --- | --- |
| JDBC [1](#fn-7-1-def) | 3, 4 |

1

Only the [Db2 JDBC driver typesï»¿](https://www.ibm.com/docs/en/sdi/7.2.0.3?topic=drivers-connecting-db2) 2 and 4 are supported.

| Messaging client | Versions |
| --- | --- |
| IBM MQ | 8.0, 9.0, 9.1, 9.2 |
| JMS | 1.1 |

| Monitoring framework | Versions |
| --- | --- |
| [JMX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.") | 1.0+ |


---


## Source: oneagent-platform-and-capability-support-matrix.md


---
title: OneAgent platform and capability support matrix
source: https://www.dynatrace.com/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix
scraped: 2026-02-16T09:21:10.342234
---

# OneAgent platform and capability support matrix

# OneAgent platform and capability support matrix

* Latest Dynatrace
* 13-min read
* Updated on Oct 15, 2025

This page describes which capabilities are supported by OneAgent on different operating systems and platforms.

|  |  |
| --- | --- |
| **GA** | Generally available and fully supported. |
| **Preview** | These features are in the final stages of development and are ready to be previewed. Preview features aren't production-ready and they aren't officially supported. |
| **Future** | A feature or technology support that is either on the roadmap or may be considered on-demand. |
| **Not planned** | A feature or technology support that Dynatrace does not currently plan to pursue. |
| n/a | Not applicable |

## Operating systems

The tables below contain information about the supported OneAgent capabilities for various supported operating systems. Note that Alpine Linux is supported in containers only, see [Alpine Linux (musl libc) based containers](#musl).

### Code modules

| Code module | [Windows](/docs/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [AIX PPC](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  |  |
| [.NET and .NET Core](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| [.NET Framework](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |
| [Node.js](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| Python | n/a |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| PHP |  |  |  | [1](#fn-1-1-def) | n/a | n/a | n/a | n/a | n/a |
| [Go](/docs/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.") |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Apache, IHS |  |  |  | [1](#fn-1-1-def) |  |  | [2](#fn-1-2-def) |  | n/a |
| NGINX |  |  |  | [1](#fn-1-1-def) | n/a | n/a |  | n/a | n/a |
| Microsoft IIS |  | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

1

[Classic full-stack mode](/docs/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.") is not supported for [Alpine Linux (musl libc) based containers](#musl). Please [migrate](/docs/ingest-from/setup-on-k8s/guides/migration/classic-to-cloud-native "Migrate your Dynatrace deployment from classic full-stack to cloud-native full-stack mode.") to the [Cloud-native full-stack](/docs/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.").

2

[Alpine Linux (musl libc) based containers](#musl) are not supported.

### IBM technologies

| Code module | [Windows](/docs/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| IBM App Connect Enterprise |  |  | n/a | n/a |  |  |  |  |  |
| IBM Integration Bus |  |  | n/a | n/a |  |  |  |  |  |
| IBM CICS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |
| IBM IMS | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |  |

### OneAgent SDK

| OneAgent SDK | [Windows](/docs/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [AIX PPC](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK for C/C++ |  |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) |  |  |  |  |
| OneAgent SDK for Java |  |  |  |  |  |  |  |  |  |
| OneAgent SDK for .NET |  |  |  |  | n/a | n/a | n/a | n/a | n/a |
| OneAgent SDK for Node.js |  |  |  |  |  |  |  | n/a | n/a |
| OneAgent SDK for Python |  |  | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | [1](#fn-2-1-def) | n/a | n/a |

1

We added support for Python, C++, and other runtimes via [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") instead of the Dynatrace SDK (which is Dynatrace-proprietary). This is available on any platform.

### Other modules

| Module | [Windows](/docs/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | [Linux ARM64 (AArch64)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [AIX PPC](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| OS module[1](#fn-3-1-def) |  |  | n/a |  |  |  |  |  |  |
| Network module |  |  | n/a |  |  |  |  |  |  |
| Log module |  |  | n/a |  | [2](#fn-3-2-def) |  |  |  |  |
| JMX extensions |  |  |  |  |  |  |  |  |  |
| Extensions |  |  |  |  |  |  |  |  |  |
| Live Debugger [3](#fn-3-3-def) |  |  |  |  |  |  |  |  | n/a |

1

OS module is required for out-of-the-box infrastructure alerting capabilities.

2

Log module support is limited to custom log sources, no log auto-detection is performed.

3

Supported for Java versions 8-23. Node.js version 22 is supported starting OneAgent version 1.313+.

### Features

| Feature | [Windows](/docs/ingest-from/technology-support#windows "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux x64](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Alpine Linux x64](#musl) | Linux ARM64 (AArch64) | [AIX PPC](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Solaris SPARC/x86](/docs/ingest-from/technology-support#unix "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux PPC-LE (64bit)](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [Linux s390x](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") | [z/OS](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Auto-update of all modules |  |  | n/a |  |  |  |  |  |  |
| [Auto-injection](#auto-injection) of code modules |  |  |  |  | n/a[1](#fn-4-1-def) |  |  |  |  |
| [Universal injection](#universal-injection) of code modules |  |  |  |  |  |  |  |  |  |
| [Auto-injection](#auto-injection) for containers |  |  | n/a |  |  |  |  |  |  |
| Non-privileged |  |  | n/a |  |  |  |  |  | n/a |

1

Global auto-injection isn't possible for AIX. Instead, use the [universal injection](#universal-injection) approach, as described on the [AIX OneAgent installation page](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Learn how to download and install Dynatrace OneAgent on AIX.").

## Enterprise cloud platforms

The tables below contain information about the supported OneAgent capabilities for various supported Cloud platforms.

Cloud Foundry application-only also applies to [SAP Cloud](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Install OneAgent on SAP Business Technology Platform.").

OneAgent deployment via container (OneAgent Operator) on OpenShift and Kubernetes has some [limitations](#agent-container) compared to standard OneAgent installation.

### Code modules

| Code module[1](#fn-5-1-def) | [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") | [OpenShift](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") |  |  |  |  |  |  |  |
| [.NET and .NET Core](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) | [1](#fn-5-1-def) |
| [.NET Framework](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  | n/a | n/a | n/a | n/a | n/a |  |
| [Node.js](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") |  |  |  |  |  |  |  |
| [Python](/docs/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.") | n/a | n/a |  |  |  |  | n/a |
| PHP |  |  |  |  |  |  |  |
| [Go](/docs/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.") |  |  |  | [1](#fn-5-1-def) |  | [1](#fn-5-1-def) |  |
| Apache, IHS |  |  |  |  |  |  | [2](#fn-5-2-def) |
| NGINX |  |  |  |  |  |  | [2](#fn-5-2-def) |

1

Out-of-the-box infrastructure alerting capabilities are not supported for application-only code modules.

2

[Alpine Linux (musl libc) based containers](#musl) are not supported.

### OneAgent SDK

| OneAgent SDK | [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") | [OpenShift](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OneAgent SDK for C/C++ |  |  |  |  |  |  |  |
| OneAgent SDK for Python |  |  |  |  |  |  |  |

### Other modules

| Module | [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") | [OpenShift](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| OS module |  | n/a |  | n/a |  | n/a |  |
| Network module |  | n/a |  | n/a |  | n/a |  |
| Log module |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  | [1](#fn-6-1-def) |  |
| Extension module |  | n/a | n/a | n/a | n/a | n/a |  |
| Live Debugger |  |  |  |  |  |  |  |

1

This is supported via the [FluentD integration](/docs/analyze-explore-automate/log-monitoring/acquire-log-data "Learn how to acquire log data in Dynatrace Log Monitoring.") available in Dynatrace

### Features

| Feature | [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH.") | [Cloud Foundry application-only](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") | [OpenShift](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [OpenShift application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | [Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | [Kubernetes application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") | Azure ServiceFabric |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Auto-update of all modules |  | n/a |  | n/a |  | n/a |  |
| [Auto-injection](#auto-injection) of code modules |  | n/a |  | n/a |  | n/a |  |
| [Universal injection](#universal-injection) of code modules |  |  |  |  |  |  |  |
| [Auto-injection](#auto-injection) for containers |  | n/a |  | n/a |  | n/a |  |
| Non-privileged | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

## Cloud application platforms

The tables below contain information about the supported OneAgent capabilities for supported Cloud application platforms.

### Code modules

| Code module | AWS Lambda | [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.") | [Azure App services](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace") | [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.") | [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.") | [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.") | [Google Cloud Run Managed](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun "Monitor Java application deployed on Google Cloud Run managed.") |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [Java](/docs/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| [.NET and .NET Core](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") |  |  |  |  |  | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| [.NET Framework](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | n/a |  |  |  | n/a | n/a | n/a |  |
| [Node.js](/docs/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") | [1](#fn-7-1-def) |  |  |  |  |  |  | [2](#fn-7-2-def) |
| Python | [1](#fn-7-1-def) |  |  |  |  |  |  |  |
| PHP |  |  |  |  |  |  |  |  |
| [Go](/docs/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.") |  | n/a |  | n/a | [3](#fn-7-3-def) | [3](#fn-7-3-def) | [3](#fn-7-3-def) |  |
| Microsoft IIS | n/a | n/a |  |  |  |  |  |  |

1

Both 64-bit ARM ([AWS Graviton2 processorsï»¿](https://aws.amazon.com/ec2/graviton/)) and 64-bit x86 architectures are supported.

2

Both Google Cloud Run execution environments are supported, with some restrictions.

3

[Alpine Linux (musl libc) based containers](#musl) are not supported.

### Features

| Feature | AWS Lambda | [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.") | [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring "Learn how to configure OneAgent for monitoring Azure Spring Apps.") | [Azure App services](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace") | [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.") | [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.") | [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.") |
| --- | --- | --- | --- | --- | --- | --- | --- |
| [Universal injection](#universal-injection) of code modules | n/a |  | n/a |  |  |  |  |

## Auto-injection of code modules

Auto-injection automatically injects code modules into monitored applications in a completely transparent and automatic fashion that requires no manual configuration or intervention. This approach to deep monitoring is supported for Windows (Docker only) and Linux. Among other things, auto-injection also automatically injects code modules into Docker, containerd, CRI-O, and Cloud Foundry Garden containers. This means that you don't have to change any container images on monitored platforms to gain full insights.

## Universal injection of code modules

Universal injection allows Dynatrace to inject code modules into applications in a unified way across multiple platforms, in situations where auto-injection isn't available. This applies to AIX and Solaris as well as to Cloud Foundry application-only, OpenShift application-only, Kubernetes application-only, Heroku, Google App Engine, AWS Fargate, and AWS App Runner.

The feature is described on the [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Learn how to download and install Dynatrace OneAgent on AIX.")/[Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris/install-oneagent-on-solaris "Find out how to configure Dynatrace to monitor applications of different technologies that run on Solaris (x86 and SPARC).") OneAgent installation page. It is also part of the [OpenShift application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")/[Kubernetes application-only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") integration and the container platforms [Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine "Install OneAgent on Google App Engine clusters for application-only monitoring.") and [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.").

Outside of these specific use cases, this feature isn't to be used directly!

The [Cloud Foundry buildpack](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") integrations and [Dynatrace Heroku](/docs/ingest-from/setup-on-container-platforms/heroku "Install OneAgent to monitor applications running on Heroku.") buildpack use this transparently under the hood without any need for manual intervention or configuration.

Any form of undocumented injection (for example, older forms of manual injection) aren't supported.

## Alpine Linux (musl libc) based containers

Dynatrace supports [Alpine Linux (musl libc) based containers](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.") on monitored Linux x86\_64 hosts. This includes OpenShift, Kubernetes and Cloud Foundry installations and all forms of Docker environments. In these environments Dynatrace OneAgent [automatically injects](#auto-injection) the code modules into the applications running inside the container.

Alpine Linux is also supported in [OpenShift application only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") and [Kubernetes application only](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") integrations as well as when pushing Docker images to Cloud Foundry and Heroku. This happens via the [universal injection](#universal-injection).

Dynatrace OneAgent doesn't support direct installation in Alpine based Linux systems.

Dynatrace OneAgent doesn't support monitoring binaries built against GNU C Library (glibc) running on Alpine based Linux systems using a GNU C Library (glibc) compatibility package like gcompat (GNU C Library compatibility layer for musl) or libc6-compat (compatibility libraries for glibc).

## OneAgent deployment via Dynatrace Operator

Dynatrace Operator deploys the OneAgent to Kubernetes or OpenShift clusters through a containerized approach. There are some [limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.") associated with deploying OneAgent via Dynatrace Operator. These include:

* The auto-update mechanism of modules is disabled for container rollouts. However, Dynatrace Operator ensures the restart of OneAgent pods to receive OneAgent updates.
* Auto-injection of code-modules is disabled for native (i.e., non-containerized) processes.
* JMX extensions aren't supported for technologies outside of containers

For a detailed overview of limitations, see [Set up Dynatrace OneAgent as a Docker container](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.").

## Related topics

* [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Known solutions and workarounds](/docs/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.")


---


## Source: serverless-compute-services.md


---
title: Serverless compute support matrix
source: https://www.dynatrace.com/docs/ingest-from/technology-support/serverless-compute-services
scraped: 2026-02-16T09:22:00.699766
---

# Serverless compute support matrix

# Serverless compute support matrix

* Latest Dynatrace
* 13-min read
* Published Jan 27, 2022

This page describes which features and capabilities are available across the various flavors of serverless compute services for functions (FaaS).

Key to columns and cells

#### Columns

| Heading | Description |
| --- | --- |
| Cloud platform metrics and metadata | Dynatrace has an integration with the cloud provider to capture platform-level metrics and metadata. |
| Logs | Dynatrace captures resource and/or application logs. |
| Distributed tracing | Dynatrace supports distributed tracing for these services, either providing a dedicated integration or via OpenTelemetry. |
| Automatic tracing | Dynatrace provides automatic out-of-the-box tracing without code changes. |
| OpenTelemetry/Extend tracing | Dynatrace provides the ability to enhance tracing via [OpenTelemetry](/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace."), its own [SDKs](/docs/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available."), and [custom services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols."). |
| Custom metrics | Dynatrace provides the ability to add custom metrics via [API](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace."), [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."), [Spring Micrometerï»¿](https://micrometer.io/docs/registry/dynatrace), and many other means. |
| Automatic RUM | Dynatrace provides out-of-the-box real user monitoring with no code changes required. |
| Agentless RUM | Dynatrace provides an [agentless integration](/docs/observe/digital-experience/web-applications/initial-setup/set-up-agentless-real-user-monitoring "Set up agentless monitoring for your web applications.") for real user monitoring. |

#### Cells

| Icon | Release | Description |
| --- | --- | --- |
| GA | **GA** | Generally available and fully supported. |
|  | **Preview** | These features are in the final stages of development and are ready to be previewed. Preview features aren't production-ready and they aren't officially supported. |
| Future | **Future** | A feature or technology support that is either on the roadmap or may be considered on-demand. |
| Not planned | **Not planned** | A feature or technology support that Dynatrace does not currently plan to pursue. |
| n/a |  | Not applicable |

### AWS Lambda

#### Classic deployment

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

Language

[Cloud platform metrics and metadata](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")

[Logs](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")

Distributed tracing

Automatic tracing

OpenTelemetry  
Extend tracing

Custom metrics

Automatic RUM

Agentless RUM

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

n/a

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

n/a

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-1-1-def)

n/a

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

GoLang

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

#### Container images

Both 64-bit ARM (AWS Graviton2 processors) and 64-bit x86 architectures are supported

Language

[Cloud platform metrics and metadata](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")

[Logs](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")

Distributed tracing

Automatic tracing

OpenTelemetry  
Extend tracing

Custom metrics

Automatic RUM

Agentless RUM

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

n/a

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

n/a

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-1-2-def)

n/a

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[3](#fn-1-3-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

GoLang

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

[Requires integration of Dynatrace extension via Dynatrace Lambda Layer](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java."). To learn which runtimes are supported, see [Support lifecycle](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "AWS Lambda capabilities and integration options").

2

[Requires integration of Dynatrace extension on container image](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension/deploy-oneagent-on-lambda-container-images "Deploy Dynatrace Lambda Layers when deployed via a container image.")

3

[Trace AWS Lambda .Net Core](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")

### Azure Functions

#### Windows-based AppService plan or App Service Environment

Language

[Cloud platform metrics and metadata](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")

[Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

Distributed tracing

Automatic tracing

OpenTelemetry  
extend tracing

Custom metrics

Automatic RUM

Agentless RUM

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-2-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

Requires integration of OneAgent via [Dynatrace Site-Extension for Azure App Services](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace")

#### Linux-based App Service plan or App Service Environment

Language

[Cloud platform metrics and metadata](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")

[Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

Distributed tracing

Automatic tracing

OpenTelemetry  
extend tracing

Custom metrics

Automatic RUM

Agentless RUM

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-3-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

Requires integration of [OneAgent on AppServices for Linux and Containers](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice/integrate-oneagent-on-web-app-for-containers "Learn how to install, configure, update, and uninstall OneAgent in containerized applications on Linux.")

#### Consumption or Premium plan

Language

[Cloud platform metrics and metadata](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")

[Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

Distributed tracing

Automatic tracing

OpenTelemetry  
extend tracing

Custom metrics

Automatic RUM

Agentless RUM

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-4-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

[Trace Azure Functions on Azure Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans")

### Runtime v1

Language

Distributed tracing

Automatic tracing

All languages

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Not planned](https://dt-cdn.net/images/icon-not-planned-172a321f5d.svg "Not planned")

### Runtime v2

Language

Distributed tracing

Automatic tracing

.NET Core[1](#fn-5-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-5-2-def)

Other languages

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

1

Functions written in [C# (class libaries), C# script (.csx) and F# (.fsx)ï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details) which are executed in the [in-process modelï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Limited to functions deployed on on AppService-Plan / Appservice-Environment or Kubernetes

### Runtime v3-v4

Language

Distributed tracing

Automatic tracing

.NET Core[1](#fn-6-1-def)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[2](#fn-6-2-def)

[.Net Core, Isolated-Processï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide)

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

Other languages

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

1

Functions written in [C# (class libaries), C# script (.csx) and F# (.fsx)ï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/supported-languages#language-support-details) which are executed in the [in-process modelï»¿](https://docs.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#differences-with-net-class-library-functions)

2

Limited to functions deployed on on AppService-Plan / Appservice-Environment or Kubernetes

### Frameworks

#### Durable Functions

Language

Distributed tracing

Automatic tracing

.NET Core

[1](#fn-7-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

Other languages

n/a[1](#fn-7-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

1

Durable Functions SDK has [preview support for distributed tracingï»¿](https://dt-url.net/qj03vf2) for .NET Core using Application-Insights.

### Google Cloud Functions

Language

[Cloud platform metrics and metadata](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")

[Logs](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")

[Distributed tracing](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.")

Automatic tracing

OpenTelemetry  
Extend tracing

Custom metrics

Automatic RUM

Agentless RUM

Python

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

GoLang

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

.NET Core

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Java

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

Node.js

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")[1](#fn-8-1-def)

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

![Future](https://dt-cdn.net/images/icon-future-blue-700-7ce07301ea.svg "Future")

![GA](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "GA")

1

[Trace Google Functions written in Node.js](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs "Monitor Google Cloud Functions with OpenTelemetry for Node.js and Dynatrace.")

## Related topics

* [Serverless monitoring](/docs/discover-dynatrace/get-started/serverless-monitoring "Serverless observability with Dynatrace")
* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")
* [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")
* [Known solutions and workarounds](/docs/ingest-from/technology-support/known-solutions-and-workarounds "Check the solutions for reported problems regarding various technologies.")


---


## Source: support-model-and-issues.md


---
title: Dynatrace Operator support and known issues
source: https://www.dynatrace.com/docs/ingest-from/technology-support/support-model-and-issues
scraped: 2026-02-16T09:20:34.079944
---

# Dynatrace Operator support and known issues

# Dynatrace Operator support and known issues

* Latest Dynatrace
* 5-min read
* Updated on Feb 10, 2026

Dynatrace offers support for Kubernetes shortly after a new Kubernetes or OpenShift release. Once the new Kubernetes/OpenShift release candidate versions are available, Dynatrace tests these versions, including the latest OneAgent, ActiveGate, and Dynatrace Operator versions.

The table below lists the verified and tested release versions:

| Kubernetes upstream version | OpenShift version | Minimum OneAgent version | Minimum ActiveGate version | Minimum Dynatrace Operator version | Recommended Dynatrace Operator version | End of support (Kubernetes) | End of support (OpenShift) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.35 |  | 1.329 | 1.329 | v1.1.x | v1.8.0+ | Apr 1, 2028 |  |
| 1.34 | 4.21[4](#fn-1-4-def) | 1.321 | 1.321 | v1.1.x | v1.7.0+ | Nov 1, 2027 | Oct 1, 2028 |
| 1.33 | 4.20[4](#fn-1-4-def) | 1.319 | 1.319 | v1.1.x | v1.7.0+ | Jul 1, 2027 | Mar 1, 2028 |
| 1.32 | 4.19[4](#fn-1-4-def) | 1.309 | 1.309 | v1.1.x | v1.7.0+ | Mar 1, 2027 | Mar 1, 2028 |
| 1.31 | 4.18[3](#fn-1-3-def) | 1.297 | 1.297 | v1.1.x | v1.7.0+ | Jan 1, 2027 | Aug 1, 2028 |
| 1.30 | 4.17[3](#fn-1-3-def) | 1.291 | 1.291 | v1.1.x | v1.7.0+ | Aug 1, 2026 | Jul 1, 2027 |
| 1.29 | 4.16[3](#fn-1-3-def) | 1.281 | 1.281 | v0.14.x | v1.7.0+ | Mar 1, 2026 | Sep 1, 2027 |
| 1.28 | 4.15 | 1.275 | 1.275 | v0.12.x | v1.7.0+ | Nov 1, 2025 | Nov 1, 2026 |
| 1.27 | 4.14 | 1.269 | 1.269 | v0.10.x | v1.7.0+ | Jul 1, 2025 | Nov 1, 2026 |
| 1.26 | 4.13 | 1.259 | 1.257 | v0.10.x | v1.7.0+ | Mar 1, 2025 | Feb 1, 2026 |
| 1.25 | 4.12 | 1.249 | 1.251 | v0.8.x | v1.4.2+ | Nov 1, 2024 | Feb 1, 2026 |
| 1.24 | 4.11 | 1.241 | 1.243 | v0.7.x | v1.3.2+ | Aug 1, 2024 | Mar 1, 2025 |
| 1.23 | 4.10 | 1.233 | 1.233 | v0.4.x | v1.0.1[2](#fn-1-2-def) | Apr 1, 2024 | Mar 1, 2025 |
| 1.22 | 4.9 | 1.227 | 1.223 | v0.3.x | v1.0.1[2](#fn-1-2-def) | Jan 1, 2024 | May 1, 2024 |
| 1.21 | 4.8 | 1.217 | 1.215 | v0.3.x | v0.12.1[1](#fn-1-1-def) | Nov 1, 2023 | May 1, 2024 |
| 1.20 | 4.7 | 1.207 | 1.211 | v0.3.x | v0.6.0 | Aug 1, 2023 | Aug 1, 2023 |
| 1.19 | 4.6 | 1.199 | 1.205 | v0.3.x | v0.6.0 | Aug 1, 2023 | Aug 1, 2023 |
|  | 3.11 |  |  | v0.2.2 | v0.2.2 | Aug 1, 2023 | Aug 1, 2023 |

1

A new Go version used in Dynatrace Operator is incompatible with the CRI-O version of OpenShift 4.8 and Kubernetes 1.21. See the required manual workaround in [Dynatrace Operator release notes version 0.13.0](/docs/whats-new/dynatrace-operator/dto-fix-0-13-0 "Release notes for Dynatrace Operator, version 0.13.0").

2

Dynatrace Operator version 1.0.1 is recommended for Kubernetes 1.22 and 1.23. Upgrading to version 1.1.0+ is suggested for OpenShift 4.8 and above.

3

[Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/how-it-works/other-deployment-modes/classic-fullstack "In-depth description of Classic Full-Stack monitoring using Dynatrace Operator.") is supported only on worker nodes that run Red Hat Enterprise Linux. If worker nodes run Red Hat Enterprise Linux CoreOS instead, only [Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") is supported.

4

Only [Application observability](/docs/ingest-from/setup-on-k8s/how-it-works/application-monitoring "In-depth description of Application observability using the Dynatrace Operator.") and [Full-stack observability](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator.") are supported. This is because worker nodes can run only Red Hat Enterprise Linux CoreOS. To learn more, see [Red Hat release notes (1.5.13.2)ï»¿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.19/html/release_notes/ocp-4-19-release-notes#ocp-4-19-rhel-worker-nodes-removed_release-notes).

Full support is provided until a Kubernetes or OpenShift version reaches end of life. After that, Dynatrace provides maintenance support for approximately one year. End-of-support dates are announced in [End-of-support announcements](/docs/whats-new/technology/end-of-support-news#dto "End of support announcements for technologies supported by Dynatrace.").

The main distinction between full support and maintenance support is that Dynatrace reduces the daily testing activities during the maintenance support period.

During the full support and maintenance support periods, each encountered bug undergoes a backport assessment. Depending on the severity and change risk, the fix is either backported and released with a patch version or fixed in the next version. For details, refer to the relevant [Dynatrace release notes](/docs/whats-new "Read the product news and the release notes and find out which Documentation topics are new.").

## Dynatrace Operator support

The Dynatrace Operator is available on the following architectures:

* x86
* ARM
* ppc64le
* s390x [1](#fn-2-1-def)

1

Only the [cloud native full stack deployment](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes"), [application monitoring](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), and [host monitoring](/docs/ingest-from/setup-on-k8s/deployment/other/host-monitoring "Deploy Dynatrace Operator in host monitoring mode to Kubernetes") are supported.

In cases where issues related to the Dynatrace Operator cannot be replicated by Dynatrace on x86 or ARM architectures and are identified as specific to ppc64le, you need to reach out to `dt-operator@ibm.com` for further support. Additional information can be found in the associated open-source pull request for the Dynatrace Operator on [GitHubï»¿](https://dt-url.net/ev034k3).

Dynatrace Operator is responsible for rollout and lifecycle management of various Dynatrace components in Kubernetes and OpenShift (including ActiveGate and OneAgent). Dynatrace Operator is an open-source project maintained on [GitHubï»¿](https://dt-url.net/d7034gj). It follows the `major.minor.patch` [semantic versioningï»¿](https://semver.org/) schema, with a release cadence of minor versions being released roughly every 2â3 months.

The three latest Dynatrace Operator versions are tested with the latest Kubernetes and OpenShift versions. Additionally, we perform a backport assessment for any bug or vulnerability to analyze the severity and change risk of the fix. We recommend that you use the latest patch version, as the newly implemented features increment the minor version. For details, see the [Dynatrace Operator release notes](/docs/whats-new/dynatrace-operator "Release notes for Dynatrace Operator").

All Dynatrace Operator versions that are not considered end-of-life are treated as being in maintenance mode, which includes our regular customer support processes. Versions in maintenance mode do not receive bug fixes and vulnerability backports. See end-of-support announcements on [End-of-support announcements](/docs/whats-new/technology/end-of-support-news#dto "End of support announcements for technologies supported by Dynatrace.").

## Known issues and resolutions

A list of known issues for Dynatrace Operator versions and how they affect various components. These issues are present in released versions of the Dynatrace Operator and may require a minor version upgrade to resolve them!

### Dynatrace component injection

Dynatrace Operator version 1.7.0 Dynatrace Operator version 1.7.1 Dynatrace Operator version 1.7.2

#### Issue

* Due to optimization of the injected mounts (combining them under `/var/lib/dynatrace`), Dynatrace components can no longer be injected with the OneAgent.

* Dynatrace components contain configuration in `/var/lib/dynatrace` that is hidden by mounts added by the Webhook injection.

By default, monitoring for the Dynatrace Operator namespace (and therefore Dynatrace components) is not enabled. The issue can surface if the `feature.dynatrace.com/ignored-namespaces` feature flag is used to override ignored namespaces to include the Dynatrace Operator namespace.

#### Resolution

Configure the `dynatrace.com/split-mounts` pod annotation (requires Dynatrace Operator version 1.8.0+) on affected pods.

### Classic full-stack with metadata enrichment

Dynatrace Operator version 1.7.0 Dynatrace Operator version 1.7.1 Dynatrace Operator version 1.7.2

#### Issue

* Classic full-stack and metadata enrichment are not compatible and cannot be used to inject the same application pods.

Both OneAgent and Webhook injection attempt to add a mount to the `/var/lib/dynatrace` directory in the application pod. These mounts are incompatible and cannot coexist.

#### Resolution

If using Dynatrace Operator versions below 1.7.0:

* With OneAgent version 1.333, no changes are required.
* With OneAgent version 1.331 or earlier, the `remountOperatorEnrichment` debug flag needs to be configured for the OneAgent.

Upgrade to Dynatrace Operator version 1.8.0 (when available).

### Host availability detection

Dynatrace Operator version 1.6.0 Dynatrace Operator version 1.6.1 Dynatrace Operator version 1.6.2 Dynatrace Operator version 1.7.0 Dynatrace Operator version 1.7.1

#### Issue

* In Kubernetes environments â especially those utilizing auto-scalers â there are challenges in reliably determining whether a node was intentionally removed or has failed unexpectedly. This ambiguity can lead to a high number of false-positive âHost is unavailableâ alerts, impacting monitoring accuracy and alerting quality.

#### Resolution

Upgrade to Dynatrace Operator version 1.7.2+ or 1.6.3.

### Switch to Node image pull with Code modules image

Dynatrace Operator version 1.5.0 Dynatrace Operator version 1.5.1 Dynatrace Operator version 1.6.0 Dynatrace Operator version 1.6.1 Dynatrace Operator version 1.6.2

#### Issue

When switching from using the CSI driver without `codeModulesImage` to using it with [node image pull](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"), ensure that the CSI driverâs filesystem does not contain a code module for the specified DynaKube. If it does, the CSI driver will fail and require manual intervention to recover.

* If this issue is encountered, reverting back to not using the `codeModulesImage` will make the CSI driver operational again.
* You can use the `find` command to check for the downloaded code module for a DynaKube in the filesystem of the CSI `server` container:

  ```
  > find /data -name latest-codemodule



  /data/_dynakubes/my-dynakube-1/latest-codemodule



  /data/_dynakubes/my-dynakube-2/latest-codemodule
  ```

#### Resolution

* Upgrade to Dynatrace Operator version 1.7.0+.

Other ways to solve the problem:

* Delete the DynaKube and recreate it. This will cause monitoring gaps.

### Incompatibilities with specific component versions

Dynatrace Operator version 1.5.0+

The automatic TLS certificate feature requires ActiveGate version 1.307.35+.

* If you prefer to disable this feature, set the feature flag `feature.dynatrace.com/automatic-tls-certificate: false` in your DynaKube configuration.


---


## Source: support-model-for-pivotal-platform.md


---
title: Dynatrace support model for VMware Tanzu Application Service
source: https://www.dynatrace.com/docs/ingest-from/technology-support/support-model-for-pivotal-platform
scraped: 2026-02-16T09:20:45.621889
---

# Dynatrace support model for VMware Tanzu Application Service

# Dynatrace support model for VMware Tanzu Application Service

* Latest Dynatrace
* 5-min read
* Updated on May 10, 2024

VMware supports N, N-1, and N-2 releases of Tanzu Application Service. You can find further details in the VMware [support policyï»¿](https://tanzu.vmware.com/support/lifecycle_policy).

Dynatrace follows the same [support modelï»¿](https://d1fto35gcfffzn.cloudfront.net/support/PivotalLifecycleMatrix.pdf) as VMware, ensuring a consistent upgrade cadence. However, OneAgent and [Dynatrace Service Broker](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile "Install and configure the Dynatrace Service Broker for VMware Tanzu Platform dashboard tile.") support for Tanzu may trail behind VMware releases to allow for adequate testing.

For details, see [end of support announcements](/docs/whats-new/technology/end-of-support-news "End of support announcements for technologies supported by Dynatrace.") for OneAgent.

| TAS version[1](#fn-1-1-def) | TAS release | End of support[2](#fn-1-2-def) |
| --- | --- | --- |
| 2.11.x (+ Windows) | 2021-03-30 | 2024-04-30 |
| 2.13.x (+ Windows) | 2022-03-29 | 2024-03-31 |
| 3.0.x (+ Windows) | 2022-10-06 | 2023-10-31 |
| 4.0.x (+ Windows) | 2023-04-18 | 2025-04-30 |
| 5.0.x (+ Windows) | 2023-10-17 | 2025-10-31 |
| 6.0.x (+ Windows) | 2024-04-10 | 2026-04-30 |

## Version matrix

The support for a specific TAS version depends on the Go version used by the Cloud Foundry Gorouter supported by the OneAgent. The following table gives you detailed information about which OneAgent version is compatible with which TAS version.

|  |  |
| --- | --- |
| Future **Future** | Technology support will be added in a future OneAgent version |

### Version 6.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 6.0.11+LTS-T | 2025-01-09 | 1.22.7 | 1.287.0 |
| 6.0.10+LTS-T | 2024-11-19 | 1.22.7 | 1.287.0 |
| 6.0.9+LTS-T | 2024-10-07 | 1.22.7 | 1.287.0 |
| 6.0.8+LTS-T | 2024-09-27 | 1.22.7 | 1.287.0 |
| 6.0.7+LTS-T | 2024-08-22 | 1.22.6 | 1.287.0 |
| 6.0.6+LTS-T | 2024-07-29 | 1.22.4 | 1.287.0 |
| 6.0.5+LTS-T | 2024-07-08 | 1.22.4 | 1.287.0 |
| 6.0.4+LTS-T | 2024-05-29 | 1.22.3 | 1.287.0 |
| 6.0.3+LTS-T | 2024-05-03 | 1.22.2 | 1.287.0 |
| 6.0.2+LTS-T | 2024-05-02 | 1.22.2 | 1.287.0 |
| 6.0.1+LTS-T | 2024-04-10 | 1.21.9 | 1.281.0 |
| 6.0.0+LTS-T | 2024-04-18 | 1.21.9 | 1.281.0 |

### Version 5.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 5.0.0 | 2023-10-17 | 1.21.3 | 1.279.0 |

### Version 4.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 4.0.4 | 2023-06-26 | 1.20.5 | 1.263.0 |
| 4.0.3 | 2023-06-02 | 1.20.4 | 1.263.0 |
| 4.0.2 | 2023-05-25 | 1.20.4 | 1.263.0 |
| 4.0.1+LTS-T | 2023-05-17 | 1.20.4 | 1.263.0 |
| 4.0.0+LTS-T | 2023-04-18 | 1.20.2 | 1.263.0 |

### Version 3.0.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 3.0.3 | 2022-12-15 | 1.19.4 | 1.257.0 |
| 3.0.2 | 2022-12-02 | 1.19.2 | 1.253.0 |
| 3.0.1 | 2022-11-15 | 1.19.2 | 1.253.0 |
| 3.0.0 | 2022-10-06 | 1.18.6 | 1.253.0 |

### Version 2.13.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 2.13.8 | 2022-08-10 | 1.17.12 | 1.249.0 |
| 2.13.7 | 2022-07-19 | 1.17.11 | 1.245.0 |
| 2.13.6 | 2022-06-24 | 1.17.10 | 1.243.0 |
| 2.13.5 | 2022-06-09 | 1.17.8 | 1.239.0 |
| 2.13.4 | 2022-04-21 | 1.17.8 | 1.239.0 |
| 2.13.3 | 2022-04-20 | 1.17.8 | 1.239.0 |
| 2.13.2 | 2022-04-06 | 1.17.8 | 1.239.0 |
| 2.13.1 | 2022-03-31 | 1.17.8 | 1.239.0 |
| 2.13.0 | 2022-03-29 | 1.17.8 | 1.239.0 |

### Version 2.11.x

| TAS version | Release date | Go version | Minimum OneAgent version [3](#fn-1-3-def) |
| --- | --- | --- | --- |
| 2.11.14 | 2022-02-07 | 1.16.12 | 1.233.0 |
| 2.11.13 | 2021-12-22 | 1.16.10 | 1.233.0 |
| 2.11.12 | 2021-12-16 | 1.16.10 | 1.233.0 |
| 2.11.11 | 2021-12-15 | 1.16.10 | 1.233.0 |
| 2.11.10 | 2021-12-13 | 1.16.10 | 1.233.0 |
| 2.11.9 | 2021-11-23 | 1.16.9 | 1.231.0 |
| 2.11.8 | 2021-10-19 | 1.16.7 | 1.227.0 |
| 2.11.7 | 2021-09-30 | 1.16.7 | 1.227.0 |
| 2.11.6 | 2021-09-16 | 1.16.7 | 1.227.0 |
| 2.11.5 | 2021-09-09 | 1.16.7 | 1.227.0 |
| 2.11.4 | 2021-07-20 | 1.16.5 | 1.221.0 |
| 2.11.3 | 2021-07-15 | 1.16.5 | 1.221.0 |
| 2.11.2 | 2021-06-22 | 1.15.8 | 1.213.0 |
| 2.11.1 | 2021-05-27 | 1.15.8 | 1.213.0 |
| 2.11.0 | 2021-03-30 | 1.15.6 | 1.213.0 |

There are two flavors of the [Dynatrace OneAgent BOSH Releaseï»¿](https://github.com/Dynatrace/bosh-oneagent-release). The full BOSH OneAgent release doesn't contain the OneAgent installer. Instead, the installer is downloaded from your Dynatrace environment during the release deployment. We recommend that you use the latest release of the Dynatrace OneAgent BOSH add-on because it contains the latest improvements. However, we've also listed the minimum required BOSH Release versions per VMware Tanzu application service version above.

1

All of the above-listed versions have been verified with multiple OneAgent versions.

2

Prior to May 2020 (pre 1.191) Dynatrace offered a three-month upgrade grace period for Cloud Foundry distributions due to the offset between delivery schedules. As of May 2020, Dynatrace has accelerated its testing cycle. Thus our support model no longer requires the three-month grace period. For all OneAgent releases prior to May 2020 (earlier than OneAgent version 1.191), Dynatrace will extend support by three months to honor pre-existing OneAgent installations based on the previous support model.

3

There are two versioning schemes. The immutable OneAgent BOSH release is versioned the same as OneAgent. The immutable OneAgent BOSH release is the recommended method of deploying OneAgent. Previous versions used a lightweight approach, available on GitHub, and use GitHub's version scheme.


---
