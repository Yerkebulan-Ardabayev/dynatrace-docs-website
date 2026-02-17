---
title: OneAgent requirements
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oa-requirements
scraped: 2026-02-17T21:24:46.256267
---

# OneAgent requirements

# OneAgent requirements

* Latest Dynatrace
* 3-min read
* Updated on Jul 02, 2025

## OneAgent CPU requirements for the x86-64 architecture

This section outlines the CPU specifications to run Dynatrace OneAgent. Ensuring your system meets these requirements is essential for reliable and efficient operation.

### Minimum Supported Microarchitecture Level: **x86-64-v2**

The binary deliverables of the Dynatrace OneAgent rely on the support of the instructions included in the x86-64-v2 microarchitecture level[1](#fn-1-1-def).

1

The Dynatrace OneAgent version where this is enforced is will be announced in a future release.

#### Intel

Nehalem was the first Intel architecture to fully support the x86-64-v2 baseline. Please consult the [Intel product specificationï»¿](https://www.intel.com/content/www/us/en/products/overview.html) for further information.

**Example Intel CPUs:**

* **Intel Core i7-920** â Desktop (LGA 1366)
* **Intel Xeon X5550** â Server (LGA 1366)
* **Intel Core i5-750** â Mainstream desktop (LGA 1156)
* **Intel Xeon L5520** â Low-power server CPU

#### AMD

Bulldozer and its successors support the x86-64-v2 baseline. For some CPUs, support was added at a specific stepping. Please consult the [AMD product specificationï»¿](https://www.amd.com/en/products/specifications.html) for further information.

**Example AMD CPUs:**

* **AMD FX-4100** â Desktop (AM3+)
* **AMD Opteron 6200 Series** â Server (Socket G34)
* **AMD A8-3870K** â APU (FM1)
* **AMD FX-8350** â High-performance desktop (AM3+)

* **x86-64-v2** is a baseline that includes support for SSE3, SSSE3, SSE4.1, SSE4.2, POPCNT, and CMPXCHG16B instructions.
* Systems not meeting the x86-64-v2 baseline will not be able to run the Dynatrace OneAgent.
* Virtualized environments should ensure CPU feature passthrough is enabled to meet the microarchitecture requirements.

## OneAgent memory requirements

Deep monitoring an application with Dynatrace OneAgent implies an increase of per-application memory demand compared to execution without Dynatrace OneAgent. In addition to the memory required to load the OneAgent code module binary code into the application process, memory is also utilized to maintain monitored application state information, communication buffers, etc.

Memory demand isn't a constant number or proportion of application memory requirements, but depends on technology, monitoring configurations, application properties, and the executed load. See [About memory demand variance](#about-memory-demand-variance) below for further insights on memory demand.

### OneAgent code module memory requirement

As outlined above, monitoring memory demand depends on multiple factors. To facilitate straight forward resource planning, we recommend that you account for an additional **200MB** memory budget for monitored application processes. This number will suffice monitoring of a vast number of applications. Empirical observations show memory demand well below **100MB** for most applications.

The monitoring memory demand refers to resident set size (RSS) or equivalent quantification on non Linux operating systems. RSS is a key quantifier for applying memory limits to processes.

#### Cloud platform memory limits

Kubernetes and other cloud platforms feature definition of memory limits for workloads. The defined limits apply (roughly spoken) to RSS and workloads are automatically terminated once they exceed the defined memory limit.

As Dynatrace OneAgent code modules increase memory demand of monitored applications, memory limits must be adjusted accordingly.

### About memory demand variance

OneAgent code module deep monitoring memory demand can't be expressed exactly as a constant number or proportion of memory consumed by the application process. It's the sum of memory required for basic OneAgent code module operation (for example, communication buffers) and dynamic monitoring data gathered by OneAgent code modules. Dynamic monitoring data memory demand depends on configuration settings, application base technology, and the application itself.

#### Application dependent memory demand

Code level visibility and hotspot analysis mandate the recording of function execution time and frequency. Therefore, the number of functions in the application and their execution defines the number data items and ultimately the memory footprint needed to measure function performance. The same applies to distributed traces informationâthe memory demand for gathering distributed traces information depends on the number of concurrent requests processed by the application and the complexity (i.e., the length of the PurePath) of the executions triggered by these requests.

#### Configuration dependent memory demand

Custom service monitoring is an example for monitoring configuration dependent memory demand. The definition of a custom service increases base memory budget for selected function instrumentation and dynamical memory budget for the increased number of distributed traces data collected for custom service calls. In .NET technology, instrumentation of additional assemblies for the custom service can significantly increase startup memory demand (see below).

#### Technology dependent memory demand

OneAgent code modules are optimized to efficiently use memory and to free resources when they're no longer needed, to burden application execution as little as possible. So, memory demand might vary over application execution time.

Dependent on OneAgent code module, memory demand might peak at application startup. This is especially true for .NET technology. Preparing .NET assemblies for monitoring causes memory footprint to spike, as assembly code temporarily resides twice in memory. Once the injection process is completed, the .NET runtime retains both the original assemblies and the instrumented versions of the application logic in memory. This is a known issue of Microsoft .NET technology and can't be mitigated by the Dynatrace OneAgent.