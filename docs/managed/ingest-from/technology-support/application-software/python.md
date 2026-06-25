---
title: Python
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/python
scraped: 2026-05-12T11:23:55.741326
---

# Python

# Python

* Reference
* 2-min read
* Updated on Nov 05, 2025

You can send data from your [Pythonï»¿](https://python.org) application to Dynatrace. Python is a versatile, high-level programming language known for its readability and simplicity, often used for web development, data analysis, artificial intelligence, and scientific computing due to its extensive libraries and community support.

## Capabilities

* Injects into Python processes and supported containers automatically. Injection rules enable the exclusion or inclusion of specific processes and containers.
* Tracks CPU usage, memory consumption, and responsiveness of Python processes in real time.
* Monitors Python workloads running inside containers, capturing container-specific performance metrics and metadata about the container technology and environment.
* Provides runtime metrics, including garbage collection (GC) activity, thread metrics, and loaded library versions.
* Provides remote configuration updates that allow monitoring settings to be adjusted remotely via OneAgent. Changes are applied at runtime (without requiring a process restart when possible).
* Generates diagnostic data for troubleshooting, including support archives accessible via the [OneAgent Diagnostics](/managed/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") UI.
* Comprehensive end-to-end transaction tracing for requests to web services, remote services, message queues, databases, and others. For more information, see [Services](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.").
* Third-party vulnerability detection. For more information, see [Runtime Vulnerability Analytics](/managed/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-python/) for capturing traces. For more information, see [Instrument your Python application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.").
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing.

  If you already use the [OneAgent SDK for Pythonï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Python) or [OneAgent SDK Python auto-instrumentationï»¿](https://github.com/dynatrace-oss/OneAgent-SDK-Python-AutoInstrumentation), we recommend migrating to enable auto-instrumentation using OneAgent for Python.

See our [supported technologies matrix](/managed/ingest-from/technology-support#python "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details on supported technologies used in conjunction with Python.

## Supported Python versions

| Python version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 3.14 | 2025-10-07 | 2030-10-01 | 1.329 | - | - | Supported |
| 3.13 | 2024-10-07 | 2029-10-01 | 1.309 | - | - | Supported |
| 3.12 | 2023-10-02 | 2028-10-01 | 1.309 | - | - | Supported |
| 3.11 | 2022-10-24 | 2027-10-01 | 1.309 | - | - | Supported |
| 3.10 | 2021-10-04 | 2026-10-01 | 1.309 | - | - | Supported |
| 3.9 | 2020-10-05 | 2025-10-01 | 1.309 | - | - | Supported |
| 3.8 | 2019-10-14 | 2024-10-07 | 1.309 | - | - | Supported |

For details about supported platforms, see [Technology support | Python](/managed/ingest-from/technology-support#python "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Enable Python monitoring

To activate Python monitoring

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Find **Python** in the list of supported technologies, and select  **Edit**.
3. Turn on **Monitor Python**.
4. [Create a process monitoring rule](/managed/observe/infrastructure-observability/process-groups/configuration/pg-monitoring#rules "Ways to customize process-group monitoring") to enable deep monitoring of the selected processes.

## OneAgent Python code module and OneAgent SDK for Python compatibility

The OneAgent Python code module supports applications instrumented by the OneAgent SDK for Python. Both can work together in the same application.  
The [Dynatrace OneAgent SDK for Pythonï»¿](https://github.com/Dynatrace/OneAgent-SDK-for-Python) is a wrapper of the Dynatrace OneAgent SDK for C/C++.

When the Python code module is installed, it replaces Dynatrace OneAgent SDK for C/C++ internally and collects data produced by OneAgent SDK for Python. This means that traces produced by the SDK will be linked with those produced by the Python code module itself.

## Method hotspots

The Python code module can capture Python stack traces in the background for the [method hotspots feature](/managed/observe/application-observability/profiling-and-optimization/cpu-profiling "Learn how you can use Dynatrace to perform enhanced code analysis.").

### Prerequisites for method hotspots

* Requires Python version 3.12+.
* In the following cases, the OneAgent Python code module must be switched to non-forkable mode:

  + Process-level method hotspots (all OneAgent versions)
  + Service-level method hotspots (OneAgent version 1.326 and earlier only)

  To switch to non-forkable mode, set the environment variable `DT_PYTHON_FORKABLE` to `0`. After setting the environment variable, restart the application. Also make sure to check the [limitations section below](#method-hotspot-limitations).

### Limitations for method hotspots

* After switching to non-forkable mode, the application will be multi-threaded even during forking. Ensure that forks do not execute any Python code without first invoking the `exec` system call.
* Samples are taken asynchronously and program execution is not stopped. Therefore, stacks may be incomplete or even contain incorrect call-by associations.

## Special-purpose trace linking features

Some opt-in features of the Python agent related to trace linking are designed with specific use cases in mind, and the agent doesn't automatically detect if actual usage matches those use cases.

These features are Python queue, Python threading, and Python subprocess.

### Python queue

Use this feature to trace task flow between producers and consumers using Pythonâs standard `queue.Queue` library.

Enable it if the following applies:

* You want to use `queue.Queue` to distribute tasks or similar units of work between producers and consumers.
* You want to continue a trace from the producer (where the object is inserted) to the consumer (where it is removed using `get`).

Do not enable it in case:

* The consumer performs unrelated work after retrieving the item from the queue.
* You or a library youâre using uses queues in non-standard ways.
* You use queue APIs that are not documented in the Python standard library for `queue.Queue`.

### Python threading

Use this feature to continue traces between threads in Python applications. When a new thread is started using `Thread.start`, enabling this feature creates a link from the invoking thread to the newly created one.

Enable it if the following applies:

* You want to handle a traced request and need the trace to continue into the new thread.
* You want to continue a trace to a new thread that is started as part of processing the original request.

Do not enable it in case:

* You can use alternative features like `concurrent.futures` to establish the trace link.
* The new thread performs work unrelated to the original request.

### Python subprocess

Use this feature to create a trace link between a parent process and a subprocess launched from it. This ensures that trace context is preserved when a subprocess is started during the handling of a traced request.

Enable it if the following applies:

* You want to handle a traced request in the parent process.
* You want to continue the trace into the subprocess.

Do not enable it in case:

* You can use alternative features like Python `concurrent.futures` process to establish the trace link.
* The subprocess performs work unrelated to the original request.

When the monitored application fails to meet the requirements for a feature across all usages of the respective API(s), typical problems include unrelated traces being linked together, unrelated internal background operations being associated with traces, traces becoming excessively large, or having unexpectedly long durations. Also, the OpenTelemetry or Python SDK features may unexpectedly capture or suppress certain spans.

## Limitations

* Only the standard CPython interpreter is supported (the implementation from [Python.orgï»¿](https://python.org)).
* No-GIL (nogil) builds are not supported. The binary names of the nogil version have the `t` suffix, for example, `Python3.13t`.
* [PEP 703 - Making the Global Interpreter Lock Optional in Pythonï»¿](https://peps.python.org/pep-0703/) is not supported.
* Monitoring of processes with [Geventï»¿](https://www.gevent.org/) package installed in versions lower than 20.9.0 is not supported.
* For applications creating [forkedï»¿](https://docs.python.org/3/library/os.html#os.fork) child processes: The code module uses background threads. To support applications using process forking,
  the code module usually ensures that its background threads are shut down before a fork and restarted afterwards. The following limitations apply:

  + On Python 3.12 and newer, the Python interpreter will log a warning like
    `DeprecationWarning: This process (pid=12345) is multi-threaded, use of fork() may lead to deadlocks in the child.`
    This is because after the fork and before Python checks if the process is multi-threaded, the code module already has to restart its threads.
    If the warning only appears with the Python code module and not if it is removed,
    it is a false positive and can be ignored.
    Otherwise, it may indicate a problem in application code and should be taken seriously.
  + When forking without invoking [Python fork handlersï»¿](https://docs.python.org/3/library/os.html#os.register_at_fork),
    the code module does not shut down its threads.
    This makes the parent process a multi-threaded process, with all the usual consequences this has for forking.
    For typical applications this is not relevant, but custom native extension modules calling lower-level forking APIs
    directly would be affected.