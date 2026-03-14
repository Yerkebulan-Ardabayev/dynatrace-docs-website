---
title: ActiveGate purposes and functionality
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities
scraped: 2026-03-06T21:25:12.561851
---

# ActiveGate purposes and functionality


* Latest Dynatrace
* 4-min read
* Updated on May 10, 2023

An ActiveGate can be used for three different use cases, which we refer to as **purposes**:

* [Route OneAgent traffic to Dynatrace, monitor cloud environments, or monitor remote technologies using extensions](capabilities/routing-monitoring-purpose.md "Learn about the routing and monitoring capabilities and uses of ActiveGate.")
* [Run Synthetic monitors from a private location](capabilities/synthetic-purpose.md "ActiveGates purposed for synthetic monitoring of internal and external resources from private Synthetic locations")
* [Install the zRemote module for z/OS monitoring](capabilities/zremote-purpose.md "Learn about installing the zRemote module for z/OS monitoring.")

Each purpose comes with a different subset of functional [modules](configuration/configure-activegate.md#modules "Learn which ActiveGate properties you can configure based on your needs and requirements."). Modules should not be mixed between purposesâsuch re-configuration is not supported.

## Functionality available for the routing-monitoring ActiveGates

1

Log ingest API endpoint is supported on containerized ActiveGate in a number of [supported Kubernetes flavours](../technology-support.md#kubernetes "Find technical details related to Dynatrace support for specific platforms and development frameworks.") when provisioned with Dynatrace Operator. Since ActiveGate uses file buffers, [persistent storage](../setup-on-k8s/guides/deployment-and-configuration/activegate-pvc.md "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data.") is recommended to prevent data loss during restarts or rescheduling

## Functionality available for ActiveGates running synthetic monitors from a private location

1

See [Containerized, auto-scalable private Synthetic locations on Kubernetes](../../observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations.md "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.").

## Functionality available for ActiveGates with the zRemote module