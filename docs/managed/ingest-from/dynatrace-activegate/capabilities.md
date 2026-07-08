---
title: ActiveGate purposes and functionality
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-activegate/capabilities
---

# ActiveGate purposes and functionality

# ActiveGate purposes and functionality

* 4-min read
* Updated on Apr 02, 2026

An ActiveGate can be used for three different use cases, which we refer to as **purposes**:

* [Route OneAgent traffic to Dynatrace, monitor cloud environments, or monitor remote technologies using extensions](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.")
* [Run Synthetic monitors from a private location](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")
* [Install the zRemote module for z/OS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")

Each purpose comes with a different subset of functional [modules](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). Modules should not be mixed between purposes—such re-configuration is not supported.

## Functionality available for the routing-monitoring ActiveGates

| Functionality | Module name | x86-64 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.") | s390 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") | arm64 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") | Containerized deployment |
| --- | --- | --- | --- | --- | --- |
| [Message Routing](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#msg_routing "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Buffering and compression](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#buff_compr "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Authentication](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#auth "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Accessing sealed networks](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#sealed_net "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | OneAgent routing | Applicable | Applicable | Applicable | Applicable |
| [Memory dumps](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#mem_dump "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Memory dumps | Applicable | Applicable | Applicable | Not applicable |
| [AWS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#aws_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | AWS | Applicable | Applicable | Applicable | Not applicable |
| [Cloud Foundry monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#cf_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Cloud Foundry | Applicable | Applicable | Applicable | Applicable |
| [Kubernetes/OpenShift monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#k8s_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Kubernetes | Applicable | Applicable | Applicable | Applicable |
| [Azure monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#azure_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Azure | Applicable | Applicable | Applicable | Applicable |
| [Monitoring using an ActiveGate extension](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Extensions | Applicable | Not applicable | Not applicable | Not applicable |
| [Oracle database insights](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#oracle_ins "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Database insights | Applicable | Applicable | Applicable | Applicable |
| [Monitoring virtualized infrastructure](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#vmware "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | VMware | Applicable | Applicable | Applicable | Applicable |
| [Dynatrace API](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | REST API | Applicable | Applicable | Applicable | Applicable |
| [Log Monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#log_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Log Monitoring | Applicable | Applicable | Applicable | Applicable [1](#fn-1-1-def) |
| [Metric ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#metric_ing "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | HTTP Metric API | Applicable | Applicable | Applicable | Applicable |
| [OpenTelemetry metric ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | OTLP Ingest | Applicable | Applicable | Applicable | Applicable |
| [OpenTelemetry trace ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | OTLP Ingest | Applicable | Applicable | Applicable | Applicable |
| [OpenTelemetry log ingestion](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Log Monitoring | Applicable | Applicable | Applicable | Applicable [1](#fn-1-1-def) |
| [Real User Monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#rum_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.") | Beacon forwarder | Applicable | Applicable | Applicable | Applicable |

1

Log ingest API endpoint is supported on containerized ActiveGate in a number of [supported Kubernetes flavours](/managed/ingest-from/technology-support#kubernetes "Find technical details related to Dynatrace support for specific platforms and development frameworks.") when provisioned with Dynatrace Operator. Since ActiveGate uses file buffers, [persistent storage](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data.") is recommended to prevent data loss during restarts or rescheduling

2

We recommend [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.") as an alternative, as it has a [Syslog receiver﻿](https://github.com/Dynatrace/dynatrace-otel-collector?tab=readme-ov-file#receivers) provided by default.

## Functionality available for ActiveGates running synthetic monitors from a private location

| Functionality | Module name | x86-64 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.") | s390 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") | arm64 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") | Containerized deployment |
| --- | --- | --- | --- | --- | --- |
| [Execute private HTTP monitors](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations") | Synthetic | Applicable | Not applicable | Not applicable | Applicable[1](#fn-2-1-def) |
| [Execute private browser monitors](/managed/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations") | Synthetic | Applicable | Not applicable | Not applicable | Applicable[1](#fn-2-1-def) |

1

See [Containerized, auto-scalable private Synthetic locations on Kubernetes in Classic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.").

## Functionality available for ActiveGates with the zRemote module

| Functionality | Module name | x86-64 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.") | s390 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") | arm64 host-based deployment on [Linux](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") | Containerized deployment |
| --- | --- | --- | --- | --- | --- |
| [zRemote module for z/OS monitoring](/managed/ingest-from/dynatrace-activegate/capabilities/zremote-purpose#zos_mon "Learn about installing the zRemote module for z/OS monitoring.") | zRemote | Applicable | Applicable | Not applicable | Not applicable |