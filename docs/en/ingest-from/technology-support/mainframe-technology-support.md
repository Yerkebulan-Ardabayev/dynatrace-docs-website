---
title: Mainframe technology support
source: https://www.dynatrace.com/docs/ingest-from/technology-support/mainframe-technology-support
scraped: 2026-02-17T21:23:14.051650
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