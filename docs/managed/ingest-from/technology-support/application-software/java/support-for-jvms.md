---
title: Support for JVMs
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/support-for-jvms
scraped: 2026-05-12T12:04:24.423848
---

# Support for JVMs

# Support for JVMs

* 3-min read
* Updated on Feb 10, 2026

Dynatrace offers support for the major JVMs and JDKs.

## Oracle HotSpot VM

[Oracle support matrixï»¿](https://www.oracle.com/technetwork/java/eol-135779.html)

JVM versions 6, 7, and 8 are receiving indefinite sustained support by Oracle. Dynatrace support for these versions is currently open-ended as well.

Versions 9 and 10 are non-LTS versions and will be end of life in 2018. Dynatrace will support them until end of 2019.
Version 11 is an LTS and its support is currently open-ended.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | 2026-03-17 | - | 1.335 | - | - | Supported[1](#fn-oracle-hotspot-vm-1-def) |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 22 | - | - | 1.285 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-30 | - | 1.225 | - | - | Supported |
| 11 LTS | 2018-09-30 | 2023-09-30 | 1.155 | - | - | Supported |
| 8 LTS | 2014-03-31 | 2025-03-31 | - | - | - | Supported |
| 7 | 2011-07-31 | 2022-07-31 | - | - | - | Supported |
| 6 | 2006-09-30 | 2018-12-31 | - | - | - | Supported |

1

Alpine-based Linux systems are not supported.

Learn about [known problems and solutions to the Oracle Java HotSpot](/managed/ingest-from/technology-support/known-solutions-and-workarounds#java-oracle-hotspotopenjdk "Check the solutions for reported problems regarding various technologies.").

## OpenJDK

The OpenJDK is open source but officially supported by RedHat. See the [support lifecycleï»¿](https://access.redhat.com/articles/1299013).

Dynatraces currently provides open-ended support for versions 6, 7, and 8.

Versions 9 and 10 are non-LTS versions. Dynatrace will support these until end of 2019.
Version 11 is an LTS and its support is currently open-ended.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | 2026-03-17 | - | 1.335 | - | - | Supported[1](#fn-openjdk-1-def) |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 22 | - | - | 1.285 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-30 | - | 1.225 | - | - | Supported |
| 11 LTS | 2018-09-30 | 2024-10-30 | 1.155 | - | - | Supported |
| 8 LTS | 2014-03-31 | 2023-06-30 | - | - | - | Supported |
| 7 | 2011-07-31 | 2020-06-30 | - | - | - | Supported |
| 6 | 2006-12-31 | 2016-12-31 | - | - | - | Supported |

1

Alpine-based Linux systems are not supported.

Learn about [known problems and solutions to OpenJDK JVM](/managed/ingest-from/technology-support/known-solutions-and-workarounds#java-oracle-hotspotopenjdk "Check the solutions for reported problems regarding various technologies.").

## SapMachine

The SapMachine is a Java distribution of the OpenJDK maintained by SAP. See [SapMachine.ioï»¿](https://sapmachine.io/)

SAP JVM is the discontinued product line of Java distributions maintained by SAP.

SAP JVM 6 was discontinued at the end of 2017 and is no longer available.
Dynatrace currently provides open-ended support for versions 7 and 8.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | - | - | 1.335 | - | - | Supported[1](#fn-sapmachine-1-def) |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-18 | - | 1.299 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | - | - | 1.225 | - | - | Supported |
| 11 LTS | - | - | 1.199 | - | - | Supported |
| 8 LTS | - | - | - | - | - | Supported |
| 7 | - | - | - | - | - | Supported |

1

Alpine-based Linux systems are not supported.

## IBM JVM

The IBM JVM has its own [support timelineï»¿](https://developer.ibm.com/javasdk/support/lifecycle/) but actual support is based on support of other IBM products. For Dynatrace, the most important product here is WebSphere Application Server (see the [support timelineï»¿](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)).

WebSphere Application Server is on the [Enhanced Lifecycle policyï»¿](https://www-01.ibm.com/software/support/lifecycle/lc-policy.html). This means that although [WebSphere 8ï»¿](https://www-01.ibm.com/software/support/lifecycleapp/PLCDetail.wss?q45=D704800I08089R72) is EOS as of April 2018, IBM will continue to support it until 2021.

Dynatrace will support WebSphere and the underlying JVM versions as long as they are supported by IBM. See our [supported technologies matrix](/managed/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for details.

This means that, at the moment, IBM JVM 6,7, and 8 have open-ended support.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 8 LTS | 2015-02-28 | 2022-04-30 | - | - | - | Supported |
| 7 | 2011-09-30 | 2019-09-30 | - | - | - | Supported |
| 6 | 2007-11-30 | 2017-09-30 | - | - | - | Supported |

Memory dumps require IBM JVM 7 or higher.  
Learn more about [known problems and solutions to the IBM JVM](/managed/ingest-from/technology-support/known-solutions-and-workarounds#java-ibm-j9 "Check the solutions for reported problems regarding various technologies.").

## OpenJ9

The [Eclipse OpenJ9 JVMï»¿](https://www.eclipse.org/openj9/) is a JVM that is embedded in the OpenJDK JDK.
Each OpenJ9 release supports multiple JDK versions. See [release and support policiesï»¿](https://www.eclipse.org/openj9/docs/openj9_support/) and
[AdoptOpenJDK supportï»¿](https://adoptopenjdk.net/support.html?jvmVariant=openj9).

| OpenJ9 version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 0.11 | 2018-09-30 | - | 1.165 | - | - | Supported[1](#fn-openj9-1-def) |
| 0.10 | 2018-09-30 | - | 1.165 | - | - | Supported[2](#fn-openj9-2-def) |
| 0.9 | 2018-08-31 | - | 1.145 | - | - | Supported[3](#fn-openj9-3-def) |
| 0.8 | 2018-03-31 | - | 1.145 | - | - | Supported[4](#fn-openj9-4-def) |

1

JDK8, JDK11

2

JDK 11

3

JDK8, JDK10

4

JDK8

## Amazon Corretto

The [Amazon Correttoï»¿](https://aws.amazon.com/corretto/) JVM is based on OpenJDK. Amazon has its own LTS support for this JVM. See the [Amazon FAQï»¿](https://aws.amazon.com/corretto/faqs/) for details.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | - | - | 1.335 | - | - | Supported[1](#fn-amazon-corretto-1-def) |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 22 | - | - | 1.285 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-14 | - | 1.225 | - | - | Supported |
| 11 LTS | 2019-02-12 | 2024-08-31 | 1.165 | - | - | Supported |
| 8 LTS | 2018-11-14 | 2023-06-30 | 1.165 | - | - | Supported |

1

Alpine-based Linux systems are not supported.

## Azul

Dynatrace also supports the two proprietary JVMs from Azul Zulu and Zing. Details can be found in [our supported technologies matrix](/managed/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Azul has its own [support timelineï»¿](https://www.azul.com/products/azul_support_roadmap/)

### Azul Zing

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 11 LTS | 2018-09-30 | 2026-09-30 | - | - | - | Limited[1](#fn-azul-platform-prime-zing-1-def) |
| 8 LTS | 2015-03-31 | 2025-03-31 | - | - | - | Limited[1](#fn-azul-platform-prime-zing-1-def) |
| 7 | 2011-07-31 | 2021-12-31 | - | - | - | Limited[1](#fn-azul-platform-prime-zing-1-def) |
| 6 | 2006-12-31 | 2017-04-30 | - | - | - | Limited[1](#fn-azul-platform-prime-zing-1-def) |

1

[Limited support](#limited-support): Dynatrace can only provide support for problems that can be reproduced on other JVMs.

### Azul Zulu

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | - | - | 1.335 | - | - | Supported[1](#fn-azul-platform-core-zulu-1-def) |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 22 | - | - | 1.285 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-13 | 2030-09-30 | 1.225 | - | - | Supported |
| 11 LTS | 2018-09-30 | 2027-09-30 | 1.173 | - | - | Supported |
| 8 LTS | 2015-03-31 | 2026-03-31 | - | - | - | Supported |
| 7 | 2011-07-31 | 2023-07-31 | - | - | - | Supported |

1

Alpine-based Linux systems are not supported.

## Support and Desupport

JVMs have different support timelines, based on their vendors. Dynatrace is committed to supporting each JVM and version for at least as long as its vendor does and in most cases at least 1 year longer.

See [our supported technologies matrix](/managed/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for more details about the supported JVMs.