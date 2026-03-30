---
title: Java
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java
scraped: 2026-03-05T21:26:24.102960
---

# Java


* Latest Dynatrace
* Reference
* 1-min read
* Updated on Oct 23, 2025

Incompatibility alert

Using both the [SAP Introscope Agentï»¿](https://dt-url.net/ut039c3) and Dynatrace OneAgent on the same JVM is not supported. Dynatrace OneAgent, when active on the same host, can silently block the Introscope Agent, preventing it from operating as expected.

Dynatrace fully supports Java as well as all major JVMs and JDKs, providing extensive Java monitoring capabilities:

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-java/) for capturing traces and ingesting metrics.  
  For more information, see Instrument your Java application with OpenTelemetry
* End-to-end transaction tracing of requests to web services, remoting services, JMS, and RabbitMQ
* OneAgent SDK for custom tracing
* Insight into SQL databases (via JDBC) and NoSQL databases such as MongoDB, Cassandra, and Redis
* Heap, garbage collection, thread, JMX, process metrics, and much more
* Memory dump analysisâDynatrace supports memory dumps for the Oracle JVM, OpenJDK, and IBM JVM
* Always-on, 24/7, production-grade CPU profiling (including support for virtual threads)
* Continuous thread analysis for application, JVM, and agent threads (JVM thread analysis limited to Java 8 and Java 17+)

Dynatrace also supports GraalVM Native Images, providing extensive Java monitoring capabilities:

* End-to-end distributed tracing for HTTP requests all the way to databases.
* Code-level visibility for your applications to troubleshoot issues.
* Resource contention analysis with garbage collection and thread metrics.

See our supported technologies matrix for details about the supported [JVMs](../../technology-support.md#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Native Images](../../technology-support.md#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see Process logs with technology bundle parsers.

### Topics

* Support for JVMs
* G1 Garbage Collector â Java 9
* Top Java memory problems
* Out-of-memory (OOM) and out-of-threads (OOT) events and alerting and out-of-threads (OOT) events and alerting in Dynatrace.")
* GraalVM Native Image
* Red Hat Quarkus native applications monitoring