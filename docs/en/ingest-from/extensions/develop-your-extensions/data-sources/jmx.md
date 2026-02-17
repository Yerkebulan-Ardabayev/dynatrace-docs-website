---
title: JMX data source
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx
scraped: 2026-02-17T21:31:45.664283
---

# JMX data source

# JMX data source

* Latest Dynatrace
* Reference
* 2-min read
* Published May 15, 2023

Dynatrace provides a framework to create metrics from [JMX MBeansï»¿](https://en.wikipedia.org/wiki/Java_Management_Extensions). Every process monitored by OneAgent Java code module is capable of processing JMX 2.0 extensions.

You need to enable the **Java Metric Extensions (JMX)** [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.")

## Background

[JMXï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/package-summary.html) organizes data and functionality in an object oriented way. Every Java process has a [platform MBean serverï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/java/lang/management/ManagementFactory.html#getPlatformMBeanServer) which manages a set of monitoring objects called MBeans.

Every MBean has a unique [object nameï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html). Every object name consists of a domain name and a list of key properties. Every key property consists of a name and a (string) value.

JMX defines a standardized syntax to write those object names, for example, `java.lang:type=GarbageCollector,name=YoungGen`. Every MBean has 0 or more attributes (see [MBeanServer::getAttributeï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/MBeanServer.html#getAttribute(javax.management.ObjectName,java.lang.String))). Attributes can be of any Java type (including booleans, numbers and strings).

Numeric attributes can be directly used to produce metrics in Dynatrace. It's also possible to extract numeric values from complex attributes.

## Prerequisites

We assume the following:

* You possess sufficient JMX subject matter expertise to create an extension.
* You're familiar with [Extensions basic concepts](/docs/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.") and the general structure of the [extension YAML file](/docs/ingest-from/extensions/develop-your-extensions/extension-yaml "Learn how to create an extension YAML file using the Extensions framework.").

## Supported Dynatrace versions

* Dynatrace version 1.265+
* OneAgent version 1.265+

## JMX extension YAML file

Let's start with a minimal JMX extension:

```
# required extension metadata



name: custom:com.example.jmx



version: 1.0.0



minDynatraceVersion: 1.265.0



author:



name: John Doe



# optional metric metadata



metrics:



- key: com.example.jmx.thread_count



metadata:



displayName: Thread Count



description: Number of active Java threads



unit: Count



# defines how to create metrics from JMX MBeans



jmx:



groups:



- group: jvm



subgroups:



- subgroup: basic



query: java.lang:type=Threading



metrics:



- key: com.example.jmx.thread_count



type: gauge



value: attribute:ThreadCount
```

The first two parts should already be familiar to you, we will focus on the `jmx` section of the YAML file.

Groups and subgroups can be used to share configuration between multiple metrics. In our specific sample, we only have one group and one subgroup.

## Extract metrics from MBeans

Every subgroup has to select a set of MBeans that should contribute to a metric. This is done with the `query` field and follows the standard [JMX object name syntaxï»¿](https://docs.oracle.com/en/java/javase/17/docs/api/java.management/javax/management/ObjectName.html)

Here, the query is `java.lang:type=Threading`. This breaks down into looking for a bean in domain `java.lang` that has exactly one property with name `type` and value `Threading`.

Every subgroup also needs to define at least one metric that should be extracted from the selected MBeans. In our sample we create a Dynatrace gauge metric called `com.example.jmx.thread_count` by querying the numeric JMX attribute `ThreadCount` from the MBean `java.lang:type=Threading`.

OneAgent will automatically add the following dimensions to your metric:

* `dt.entity.process_group_instance`
* `dt.entity.process_group`
* `dt.entity.host`
* `dt.entity.container_group_instance`
* `dt.metrics.source`
* `dt.extension.config.id`

For more information, see [JMX data source reference](/docs/ingest-from/extensions/develop-your-extensions/data-sources/jmx/jmx-schema-reference "Learn about JMX extensions in the Extensions framework.").