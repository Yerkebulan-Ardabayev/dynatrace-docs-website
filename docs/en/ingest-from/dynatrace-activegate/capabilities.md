---
title: ActiveGate purposes and functionality
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities
scraped: 2026-02-16T21:21:17.933641
---

# ActiveGate purposes and functionality

# ActiveGate purposes and functionality

* Latest Dynatrace
* 4-min read
* Updated on May 10, 2023

An ActiveGate can be used for three different use cases, which we refer to as **purposes**:

* [Route OneAgent traffic to Dynatrace, monitor cloud environments, or monitor remote technologies using extensions](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.")
* [Run Synthetic monitors from a private location](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")
* [Install the zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose "Learn about installing the zRemote module for z/OS monitoring.")

Each purpose comes with a different subset of functional [modules](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). Modules should not be mixed between purposesâsuch re-configuration is not supported.

## Functionality available for the routing-monitoring ActiveGates

Functionality

Module name

x86-64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

s390 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

arm64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

Containerized deployment

[Message Routing](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#msg_routing "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Buffering and compression](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#buff_compr "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Authentication](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#auth "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Accessing sealed networks](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#sealed_net "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OneAgent routing

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Memory dumps](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#mem_dump "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Memory dumps

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[AWS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#aws_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

AWS

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[Cloud Foundry monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#cf_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Cloud Foundry

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Kubernetes/OpenShift monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#k8s_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Kubernetes

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Azure monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#azure_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Azure

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Monitoring using an ActiveGate extension](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#extn "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Extensions

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[Oracle database insights](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#oracle_ins "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Database insights

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Monitoring virtualized infrastructure](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#vmware "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

VMware

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Dynatrace API](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#api "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

REST API

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Log Monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#log_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Log Monitoring

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Metric ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#metric_ing "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

HTTP Metric API

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[OpenTelemetry metric ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OTLP Ingest

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[OpenTelemetry trace ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

OTLP Ingest

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[OpenTelemetry log ingestion](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#otlp_ingest "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Log Monitoring

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

[Real User Monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose#rum_mon "Learn about the routing and monitoring capabilities and uses of ActiveGate.")

Beacon forwarder

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

[Live Debugging](/docs/observe/application-observability/live-debugger "Get familiar with the Live Debugger capabilities in Dynatrace.")

Debugging

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

## Functionality available for ActiveGates running synthetic monitors from a private location

Functionality

Module name

x86-64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

s390 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

arm64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

Containerized deployment

[Execute private HTTP monitors](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

Synthetic

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")[1](#fn-1-1-def)

[Execute private browser monitors](/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose#execute-mon "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")

Synthetic

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")[1](#fn-1-1-def)

1

See [Containerized, auto-scalable private Synthetic locations on Kubernetes](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.").

## Functionality available for ActiveGates with the zRemote module

Functionality

Module name

x86-64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") and [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")

s390 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

arm64 host-based deployment on [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")

Containerized deployment

[zRemote module for z/OS monitoring](/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose#zos_mon "Learn about installing the zRemote module for z/OS monitoring.")

zRemote

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Applicable](https://dt-cdn.net/images/icon-green-check-700-c9ea81e533.svg "Applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")

![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable")