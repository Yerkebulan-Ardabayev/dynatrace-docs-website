---
title: Support for JVMs
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/support-for-jvms
---

# Support for JVMs

# Support for JVMs

* 3-min read
* Updated on Jun 09, 2026

Dynatrace offers support for the major JVMs and JDKs.

## Oracle HotSpot VM

[Oracle support matrix﻿](https://www.oracle.com/technetwork/java/eol-135779.html)

JVM versions 6, 7, and 8 are receiving indefinite sustained support by Oracle. Dynatrace support for these versions is currently open-ended as well.

Versions 9 and 10 are non-LTS versions and will be end of life in 2018. Dynatrace will support them until end of 2019.
Version 11 is an LTS and its support is currently open-ended.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | 2026-03-17 | - | 1.335 | - | - | Supported |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-30 | - | 1.225 | - | - | Supported |
| 11 LTS | 2018-09-30 | 2023-09-30 | 1.155 | - | - | Supported |
| 8 LTS | 2014-03-31 | 2025-03-31 | - | - | - | Supported |
| 7 | 2011-07-31 | 2022-07-31 | - | - | - | Supported |
| 6 | 2006-09-30 | 2018-12-31 | - | - | - | Supported |

Learn about [known problems and solutions to the Oracle Java HotSpot](/managed/ingest-from/technology-support/known-solutions-and-workarounds#java-oracle-hotspotopenjdk "Check the solutions for reported problems regarding various technologies.").

## OpenJDK

The OpenJDK is open source but officially supported by RedHat. See the [support lifecycle﻿](https://access.redhat.com/articles/1299013).

Dynatraces currently provides open-ended support for versions 6, 7, and 8.

Versions 9 and 10 are non-LTS versions. Dynatrace will support these until end of 2019.
Version 11 is an LTS and its support is currently open-ended.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | 2026-03-17 | - | 1.335 | - | - | Supported |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 22 | - | - | 1.285 | 1.333 | 2026-05-31 | Not supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 20 | 2023-03-20 | - | 1.263 | 1.307 | 2025-03-11 | Not supported |
| 19 | 2022-09-20 | - | 1.251 | 1.297 | 2023-09-30 | Not supported |
| 18 | 2022-03-15 | - | 1.241 | 1.261 | 2023-03-31 | Not supported |
| 17 LTS | 2021-09-30 | - | 1.225 | - | - | Supported |
| 16 | 2021-03-15 | 2021-09-30 | 1.217 | 1.239 | 2022-03-31 | Not supported |
| 15 | 2020-09-15 | 2021-03-30 | 1.203 | 1.223 | 2021-09-30 | Not supported |
| 14 | 2020-03-17 | 2020-09-30 | 1.189 | 1.215 | 2021-03-30 | Not supported |
| 13 | 2019-09-17 | 2020-03-30 | 1.179 | 1.201 | 2020-09-30 | Not supported |
| 12 | 2019-03-31 | 2019-09-30 | 1.169 | 1.197 | 2020-03-31 | Not supported |
| 11 LTS | 2018-09-30 | 2024-10-30 | 1.155 | - | - | Supported |
| 10 | 2018-03-31 | 2018-09-30 | - | 1.167 | 2019-06-30 | Not supported |
| 9 | 2017-09-30 | 2018-03-31 | - | 1.163 | 2019-03-31 | Not supported |
| 8 LTS | 2014-03-31 | 2023-06-30 | - | - | - | Supported |
| 7 | 2011-07-31 | 2020-06-30 | - | - | - | Supported |
| 6 | 2006-12-31 | 2016-12-31 | - | - | - | Supported |

Learn about [known problems and solutions to OpenJDK JVM](/managed/ingest-from/technology-support/known-solutions-and-workarounds#java-oracle-hotspotopenjdk "Check the solutions for reported problems regarding various technologies.").

## SapMachine

The SapMachine is a Java distribution of the OpenJDK maintained by SAP. See [SapMachine.io﻿](https://sapmachine.io/)

SAP JVM is the discontinued product line of Java distributions maintained by SAP.

SAP JVM 6 was discontinued at the end of 2017 and is no longer available.
Dynatrace currently provides open-ended support for versions 7 and 8.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | - | - | 1.335 | - | - | Supported |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-18 | - | 1.299 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | - | - | 1.225 | - | - | Supported |
| 11 LTS | - | - | 1.199 | - | - | Supported |
| 8 LTS | - | - | - | - | - | Supported |
| 7 | - | - | - | - | - | Supported |

## IBM JVM

The IBM JVM has its own support timeline, but actual support is based on support of other IBM products. For Dynatrace, the most important product here is WebSphere Application Server (see the [WebSphere Application Server on Wikipedia﻿](https://en.wikipedia.org/wiki/IBM_WebSphere_Application_Server)). IBM is committed to supporting WebSphere Platform. For WebSphere Application Server versions 8.5.5 and 9.0.5, there is no planned end-of-support published (see [WebSphere Application Server - Support FYI﻿](https://www.ibm.com/support/pages/websphere-application-server-support-fyi)).

IBM SDK, Java Technology Edition, Version 8 was released in February 2015 and will continue to receive security updates from IBM until December 31, 2030 (see [Java SDK lifecycle dates﻿](https://www.ibm.com/support/pages/java-sdk-lifecycle-dates)). Java 11 and later releases are succeeded by [IBM Semeru Runtimes](#ibm-semeru).

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 8 LTS | 2015-02-28 | 2022-04-30 | - | - | - | Supported |
| 7 | 2011-09-30 | 2019-09-30 | - | - | - | Supported |
| 6 | 2007-11-30 | 2017-09-30 | - | - | - | Supported |

Memory dumps require IBM JVM 7 or higher.  
Learn more about [known problems and solutions to the IBM JVM](/managed/ingest-from/technology-support/known-solutions-and-workarounds#java-ibm-j9 "Check the solutions for reported problems regarding various technologies.").

## IBM Semeru

[IBM Semeru Runtimes﻿](https://developer.ibm.com/languages/java/semeru-runtimes/) is IBM's supported distribution of OpenJDK paired with the [Eclipse OpenJ9 JVM﻿](https://eclipse.dev/openj9/). It succeeds IBM JVM for Java 11 and later versions.

[Eclipse OpenJ9﻿](https://eclipse.dev/openj9/) is an open-source JVM that powers IBM Semeru Runtimes. Each Semeru release pairs an OpenJDK update with a specific OpenJ9 build. Eclipse OpenJ9 does not publish standalone OpenJDK distributions — IBM Semeru Runtimes is the IBM-supported way to run workloads on OpenJ9. Dynatrace supports Eclipse OpenJ9 as part of IBM Semeru Runtimes support.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 25 LTS | 2025-09-25 | - | 1.321 | - | - | Supported |
| 21 LTS | 2024-02-05 | - | 1.275 | - | - | Supported |
| 17 LTS | 2022-01-28 | - | 1.229 | - | - | Supported |
| 11 LTS | 2021-07-30 | - | 1.229 | - | - | Supported |
| 8 LTS | 2021-07-30 | - | 1.229 | - | - | Supported |

## Amazon Corretto

The [Amazon Corretto﻿](https://aws.amazon.com/corretto/) JVM is based on OpenJDK. Amazon has its own LTS support for this JVM. See the [Amazon FAQ﻿](https://aws.amazon.com/corretto/faqs/) for details.

| Java version | Vendor released | Vendor End of life | First supported Dynatrace OneAgent version | Last supported Dynatrace OneAgent version | Dynatrace support until | [Dynatrace support level](/managed/ingest-from/technology-support#support-levels) |
| --- | --- | --- | --- | --- | --- | --- |
| 26 | - | - | 1.335 | - | - | Supported |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-14 | - | 1.225 | - | - | Supported |
| 11 LTS | 2019-02-12 | 2024-08-31 | 1.165 | - | - | Supported |
| 8 LTS | 2018-11-14 | 2023-06-30 | 1.165 | - | - | Supported |

## Azul

Dynatrace also supports the two proprietary JVMs from Azul Zulu and Zing. Details can be found in [our supported technologies matrix](/managed/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

Azul has its own [support timeline﻿](https://www.azul.com/products/azul_support_roadmap/)

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
| 26 | - | - | 1.335 | - | - | Supported |
| 25 LTS | 2025-09-16 | - | 1.321 | - | - | Supported |
| 24 | 2025-03-18 | - | 1.309 | - | - | Supported |
| 23 | 2024-09-17 | - | 1.299 | - | - | Supported |
| 21 LTS | 2023-09-19 | - | 1.275 | - | - | Supported |
| 17 LTS | 2021-09-13 | 2030-09-30 | 1.225 | - | - | Supported |
| 11 LTS | 2018-09-30 | 2027-09-30 | 1.173 | - | - | Supported |
| 8 LTS | 2015-03-31 | 2026-03-31 | - | - | - | Supported |
| 7 | 2011-07-31 | 2023-07-31 | - | - | - | Supported |

## Support and Desupport

JVMs have different support timelines, based on their vendors. Dynatrace is committed to supporting each JVM and version for at least as long as its vendor does and in most cases at least 1 year longer.

See [our supported technologies matrix](/managed/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.") for more details about the supported JVMs.