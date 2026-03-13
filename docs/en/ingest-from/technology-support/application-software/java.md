---
title: Java
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java
scraped: 2026-03-05T21:26:24.102960
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
  For more information, see [Instrument your Java application with OpenTelemetry](../../opentelemetry/walkthroughs/java.md "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")
* End-to-end [transaction tracing](../../../observe/application-observability/services.md "Learn how to monitor and analyze your services, define and use request attributes, and more.") of requests to web services, remoting services, JMS, and RabbitMQ
* [OneAgent SDK](../../extend-dynatrace/extend-tracing/oneagent-sdk.md "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing
* Insight into SQL databases (via JDBC) and NoSQL databases such as MongoDB, Cassandra, and Redis
* Heap, garbage collection, thread, JMX, process metrics, and much more
* Memory dump analysisâDynatrace supports [memory dumps](../../../observe/application-observability/profiling-and-optimization/memory-dump-analysis.md "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.") for the Oracle JVM, OpenJDK, and IBM JVM
* Always-on, 24/7, production-grade CPU profiling (including support for virtual threads)
* [Continuous thread analysis](../../../observe/application-observability/profiling-and-optimization/continuous-thread-analysis.md "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") for application, JVM, and agent threads (JVM thread analysis limited to Java 8 and Java 17+)

Dynatrace also supports GraalVM Native Images, providing extensive Java monitoring capabilities:

* End-to-end distributed tracing for HTTP requests all the way to databases.
* Code-level visibility for your applications to troubleshoot issues.
* Resource contention analysis with garbage collection and thread metrics.

See our supported technologies matrix for details about the supported [JVMs](../../technology-support.md#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Native Images](../../technology-support.md#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](../../../platform/openpipeline/use-cases/tutorial-technology-processor.md "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Topics

* [Support for JVMs](java/support-for-jvms.md "Find out the major JVMs and JDKs that are supported by Dynatrace.")
* [G1 Garbage Collector â Java 9](java/g1-garbage-collector-java-9.md "Learn how the G1 works compared to other collectors and why it can easily outperform other state-of-the-art garbage collectors on large heaps.")
* [Top Java memory problems](java/top-java-memory-problems.md "Learn about Java memory issues such as memory leaks, high memory usage, class loader problems, and GC configuration.")
* [Out-of-memory (OOM) and out-of-threads (OOT) events and alerting](java/set-up-event-and-memory-alerting.md "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")
* [GraalVM Native Image](java/graalvm-native-image.md "Install, configure, and manage Dynatrace GraalVM Native Image module.")
* [Red Hat Quarkus native applications monitoring](java/quarkus.md "Monitor Red Hat Quarkus native applications with Dynatrace on hosts that are monitored by OneAgent.")