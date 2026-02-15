---
title: Dynatrace for z/OS
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos
scraped: 2026-02-15T21:10:10.433172
---

# Dynatrace for z/OS

# Dynatrace for z/OS

* Latest Dynatrace
* 8-min read
* Updated on Nov 15, 2022

With Dynatrace, you can get complete transactional insights into your workloads from the mobile frontend down to mainframe programs and everything in between so that you can troubleshoot anomalies on the code level. Furthermore, Dynatrace can accompany you in your hybrid cloud journey with end-to-end observability from the mainframe to the cloud.

Learn how Dynatrace addresses the most typical mainframe challenges:

Is the mainframe part of the problem?

The AI-powered fault domain isolation pinpoints the root-cause of problems and assesses their user impact so that you can prioritize mitigation strategies and reduce the mean-time to repair.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-4-2556-d7363d4d4a.png)

All monitored LPARs, regions, and applications are contributing to this fault domain isolation.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-5-2556-eaa580abc1.png)

Who is calling the mainframe and how often?

Backtrace transactions using the [Service backtrace](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.") to understand your mainframe workloads and benefit from potential IBM discounts (see for example the IBM [mobileï»¿](https://www.ibm.com/common/ssi/ShowDoc.wss?docURL=/common/ssi/rep_ca/0/877/ENUSZP14-0280/index.html&lang=en&request_locale=en) and [public cloudï»¿](https://www.ibm.com/common/ssi/cgi-bin/ssialias?htmlfid=897/ENUS216-319&infotype=AN&subtype=CA) workload discounts to lower your monthly peak rolling 4-hour average MSU value).

The Service backtrace below shows how a CICS transaction interactions with both a mobile application and a web application. You can clearly see how often these applications call the CICS transaction, and also which of their requests failed.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-3-2554-c2353b4392.png)

What transactions are expensive or slow?

Analyze the performance of your transactions using via the [service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") to verify if they fulfill the defined SLOs with service-level metrics. The request count for example can indicate when a transaction is called too often from an open-system, which could result in additional costs.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-1-2558-21736786aa.png)

Use the [PurePath distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") code-level insights to optimize your programs.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-6-2072-233541ed1b.png)

Modernize programs on z/OS for hybrid cloud?

Use Dynatrace to ensure business continuity for traditional environments by monitoring middleware technologies like enterprise service buses or message queues. While transforming your mainframe programs to make them accessible for cloud functions with z/OS Connect EE, monitored by Dynatrace.

See the end-to-end trace from z/OS Connect EE down to an IMS DL/I database below.

![z/OS use case](https://dt-cdn.net/images/zos-usecase-2-2557-a3531aae62.png)

## Set up monitoring

Dynatrace provides code modules for CICS, IMS, and z/OS Java technologies so that you can achieve seamless observability with trace and metric insights. To learn more about the supported technologies, see [Mainframe technology support](/docs/ingest-from/technology-support/mainframe-technology-support "Learn which technologies Dynatrace supports for Mainframe monitoring.").

![z/OS monitoring architecture](https://dt-cdn.net/images/zos-architecture-1745-8d165d1510.png)

The CICS, IMS, and z/OS Java modules interact with the Dynatrace z/OS Data Collection (zDC) subsystem via a shared memory object (SMO) within an LPAR. The zDC subsystem manages this SMO, to which the modules write their monitoring data.

The zLocal, hosted in the z/OS [Unix System Servicesï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS) environment, runs as part of the zDC. It manages the TCP/IP connection to the zRemote module, reads monitoring data from SMO, and transfers these data to the zRemote.

The zRemote module processes monitoring data received from the zLocal and routes that data, compressed and encrypted, via its local ActiveGate to Dynatrace. Hence, the zRemote module offloads much of the processing work from the modules incurred in instrumenting subsystems and applications to an open system.

To get started, see [z/OS installation overview](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation "Installation overview of Dynatrace z/OS modules.").

## Licensing

Monitoring of the CICS, IMS, and z/OS Java modules are consumed based on million service units (MSUs).

Dynatrace Platform Subscription, see [Mainframe Monitoring](/docs/license/capabilities/app-infra-observability/mainframe "Learn how your consumption of the Dynatrace Mainframe Monitoring DPS capability is billed and charged.").

Dynatrace classic licensing, see [Mainframe Monitoring on IBM z/OS](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring#mainframe-msu "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

## FAQ

Who needs to be involved in a typical Dynatrace for z/OS installation?

To find the procedure and the people involved people, see [z/OS installation overview](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation "Installation overview of Dynatrace z/OS modules.").

Can I use host groups to organize multiple LPARs?

Yes, you can organize multiple LPARs using host groups. For more information, see [Define host groups to organize multiple LPARs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote#host-groups "Customize the zRemote module for your needs.").

What does a volatile service mean and how can I solve related problems?

A **volatile CICS** or **volatile IMS** is created automatically by Dynatrace when the maximum number of service IDs that can be generated per region (process) is exceeded. To increase the limit of service IDs that can be generated, contact a Dynatrace product expert via live chat within your Dynatrace environment.

### CICS and IMS modules

How does the CICS and IMS modules instrumentation work?

The CICS module uses hooks to instrument CICS terminal and application owning regions, creating events of interest.

The IMS module uses the logging facility to instrument IMS control and message processing regions, creating events of interest from parsing binary logs.

Both modules use hooks to instrument IBM MQ, Db2, and DL/I.

No byte code instrumentation is used by the CICS and IMS modules.

### How much GCP time do the CICS and IMS modules consume while instrumenting applications?

The CICS and IMS consume some general-purpose central processor (GCP) time while instrumenting applications on IBM Z, but this overhead is typically very low (in the range of 1%-2%, depending on the type of monitored transactions). See the examples below.

| Industry of customer | Country | Code module | Measured in year | Measurement method | GCP time overhead |
| --- | --- | --- | --- | --- | --- |
| Financial (Bank) | Italy | CICS | 2023 | HIS profiling[1](#fn-1-1-def) | < 1.9 % |
| Financial (Bank) | Spain | CICS | 2020 | HIS profiling[1](#fn-1-1-def) | < 1.0 % |
| Insurance | Germany | CICS | 2020 | ran their own tests | < 1.0 % |
| Insurance | Germany | IMS | 2020 | HIS profiling[1](#fn-1-1-def) | < 1.0 % |
| Financial (Bank) | Germany | CICS | 2019 | ran their own tests | < 1.0 % |
| Insurance | Germany | IMS | 2017 | HIS profiling[1](#fn-1-1-def) | < 1.61 % |
| Insurance | Germany | IMS | 2017 | HIS profiling[1](#fn-1-1-def) | < 0.33 % |
| Financial (Bank) | Austria | CICS | 2015 | HIS profiling[1](#fn-1-1-def) | < 2.04 % |

1

Using the [Hardware Instrumentation Servicesï»¿](https://www.ibm.com/docs/en/zos/2.1.0?topic=aids-hardware-instrumentation-services) from IBM.

* The GCP time overhead numbers are calculated relatively to the address spaces in which the modules are running. When you compare the GCP time overhead relatively to the LPAR, then these numbers are even lower.
* For example, 2% GCP time overhead in CICS address spaces represents only 1% GCP time overhead per LPAR if the CICS workloads consume only 50% of the total GCP time on a given LPAR compared to other workloads (such as jobs and system tasks).

Can the CICS and IMS modules capture dynamic SQL statements?

No, the CICS and IMS modules can only capture static SQL statements.

### z/OS Java module

Can I monitor the Servants of my WebSphere Application Server with the z/OS Java module?

The WebSphere Application Server on z/OS allows you to spin up [Servantsï»¿](https://www.ibm.com/docs/en/was-zos/9.0.5?topic=zos-websphere-application-server-terminology) dynamically depending on the workload.

In Dynatrace, you can use the **process identifier** on each metric to distinguish between different Servants, as shown in the image below.

![Metrics process identifier](https://dt-cdn.net/images/was-process-id-1607-06f91781b9.png)

However, Servants can't be incorporated into the WebSphere Application Server process group detection because whenever you spin up a new Servant, a new process entity is created, and the current monitoring context is lost.

Which attributes are evaluated for WebSphere Application Server process group detection?

Dynatrace uses the following attributes to detect and create WebSphere Application Server process entities:

* Server name
* Node name
* Cell name

Dynatrace groups all process entities belonging to the same WebSphere Application Server cluster name into a process group.

Can I merge process groups created by the z/OS Java module into a single process group?

No, process groups created by the z/OS Java module can't be modified or merged.

As an alternative you can organize your process groups by [defining metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") or [defining tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") based on environmental variables. Both concepts apply to z/OS Java as well. Note that you can define environment variables only on the process level, not on the host level.

Can I tag processes created by the z/OS Java module?

Yes. You can tag processes created by the z/OS Java module by [defining metadata](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment.") or [defining tags](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables "Find out how Dynatrace enables you to define tags based on environment variables.") based on environmental variables. Note that you can define environment variables only on the process level, not on the host level.

Can I define custom services using the z/OS Java module?

The z/OS Java module does not support custom services purely via configuration. Instead, you can create custom traces using the z/OS Java module's [OpenTelemetry interoperability](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry "Use OpenTelemetry to close observability gaps in your Java applications on z/OS.").

Can I use span attributes captured by the z/OS Java module as a request attribute?

Yes. To learn how to set up a request attribute for any captured span attribute, see [Define a request attribute for span attributes](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-opentelemetry#request-attribute "Use OpenTelemetry to close observability gaps in your Java applications on z/OS.").

## Linux on Z

With Dynatrace, you can get [Full-Stack Monitoring with Host monitoring (DPS)](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") for Linux on Z using [OneAgent on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more."). To learn more about the supported technologies on the s390 architecture, see [Technology support](/docs/ingest-from/technology-support#linux "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Related topics

* [[Blog] Eliminate inefficiencies and innovate faster on IBM Zï»¿](https://www.dynatrace.com/news/blog/eliminate-inefficiencies-and-innovate-faster-by-optimizing-hybrid-mainframe-environments-on-ibm-z/ "Eliminate inefficiencies and innovate faster by optimizing hybrid mainframe environments on IBM Z.")
* [[Blog] Transform z/OS Java applicationsï»¿](https://www.dynatrace.com/news/blog/transform-mainframe-applications-into-z-os-java-services-with-end-to-end-transaction-visibility-and-anomaly-detection-preview/ "Transform z/OS Java applications into microservices with end-to-end transaction visibility and anomaly detection.")
* [[Blog] Managing hybrid cloud infrastructureï»¿](https://www.dynatrace.com/news/blog/managing-hybrid-cloud-infrastructure-with-an-observability-platform/ "Managing a mainframe-powered hybrid cloud infrastructure with Dynatrace as an observability platform.")
* [[Video] Get insights for z/OS Connect apps with Dynatraceï»¿](https://www.youtube.com/watch?v=6WuHzvQV7yk "Learn how to modernize for hybrid cloud with the Dynatrace z/OS Connect end-to-end observability.")
* [[Video] Extend the Dynatrace value for z/OS ï»¿](https://www.youtube.com/watch?v=XUw7YmpBx4E "Learn how to capture additional monitoring data of your z/OS business applications using the CICS/IMS SDK.")