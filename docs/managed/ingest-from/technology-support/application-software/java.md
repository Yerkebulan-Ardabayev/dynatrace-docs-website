---
title: Java
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java
scraped: 2026-05-12T11:23:13.810332
---

# Java

# Java

* Reference
* 1-min read
* Updated on Oct 23, 2025

Incompatibility alert

Using both the [SAP Introscope Agentï»¿](https://dt-url.net/ut039c3) and Dynatrace OneAgent on the same JVM is not supported. Dynatrace OneAgent, when active on the same host, can silently block the Introscope Agent, preventing it from operating as expected.

Dynatrace fully supports Java as well as all major JVMs and JDKs, providing extensive Java monitoring capabilities:

* [OpenTelemetry supportï»¿](https://github.com/open-telemetry/opentelemetry-java/) for capturing traces and ingesting metrics.  
  For more information, see [Instrument your Java application with OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/java "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")
* End-to-end [transaction tracing](/managed/observe/application-observability/services "Learn how to monitor and analyze your services, define and use request attributes, and more.") of requests to web services, remoting services, JMS, and RabbitMQ
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "The Dynatrace OneAgent SDK enables you to instrument your application manually to extend end-to-end visibility for frameworks and technologies for which there is no code module yet available.") for custom tracing
* Insight into SQL databases (via JDBC) and NoSQL databases such as MongoDB, Cassandra, and Redis
* Heap, garbage collection, thread, JMX, process metrics, and much more
* Memory dump analysisâDynatrace supports [memory dumps](/managed/observe/application-observability/profiling-and-optimization/memory-dump-analysis "Learn how Dynatrace enables you to trigger, download and analyze memory dumps for Java and Node.js.") for the Oracle JVM, OpenJDK, and IBM JVM
* Always-on, 24/7, production-grade CPU profiling (including support for virtual threads)
* [Continuous thread analysis](/managed/observe/application-observability/profiling-and-optimization/continuous-thread-analysis "Continuously analyze the state of your threads and their development to quickly identify and solve performance issues in Java and Node.js processes.") for application, JVM, and agent threads (JVM thread analysis limited to Java 8 and Java 17+)

Dynatrace also supports GraalVM Native Images, providing extensive Java monitoring capabilities:

* End-to-end distributed tracing for HTTP requests all the way to databases.
* Code-level visibility for your applications to troubleshoot issues.
* Resource contention analysis with garbage collection and thread metrics.

See our supported technologies matrix for details about the supported [JVMs](/managed/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") and [Native Images](/managed/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

### Topics

* [Support for JVMs](/managed/ingest-from/technology-support/application-software/java/support-for-jvms "Find out the major JVMs and JDKs that are supported by Dynatrace.")
* [G1 Garbage Collector â Java 9](/managed/ingest-from/technology-support/application-software/java/g1-garbage-collector-java-9 "Learn how the G1 works compared to other collectors and why it can easily outperform other state-of-the-art garbage collectors on large heaps.")
* [Top Java memory problems](/managed/ingest-from/technology-support/application-software/java/top-java-memory-problems "Learn about Java memory issues such as memory leaks, high memory usage, class loader problems, and GC configuration.")
* [Out-of-memory (OOM) and out-of-threads (OOT) events and alerting](/managed/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")
* [GraalVM Native Image](/managed/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.")
* [Red Hat Quarkus native applications monitoring](/managed/ingest-from/technology-support/application-software/java/quarkus "Monitor Red Hat Quarkus native applications with Dynatrace on hosts that are monitored by OneAgent.")