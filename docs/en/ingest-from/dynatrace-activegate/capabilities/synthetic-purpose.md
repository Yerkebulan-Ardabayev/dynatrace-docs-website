---
title: Execute synthetic monitors from private locations
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities/synthetic-purpose
scraped: 2026-02-18T05:35:27.365369
---

# Execute synthetic monitors from private locations

# Execute synthetic monitors from private locations

* Latest Dynatrace
* 2-min read
* Updated on Jun 01, 2022

**Synthetic-enabled ActiveGates** enable you to set up private Synthetic locations from which you can execute synthetic monitors to monitor your internal as well as external resources.

## Private synthetic monitoring functionality and Synthetic module

(module: [Synthetic](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements."))

ActiveGates purposed for Dynatrace Synthetic Monitoring have the [Synthetic module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#synth_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") enabled.

Synthetic-enabled ActiveGates, along with the [Synthetic engine and Chromium](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."), are elements of private Synthetic locations, which are locations in your private network infrastructure.

A private location may consist of one or more Synthetic-enabled ActiveGates. See the [requirements](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations") and [process](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for setting up private locations. Once set up, you can use the Dynatrace-based [management interface for private locations and monitors](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Analyze and manage capacity usage at your private Synthetic locations.").

### Important hardware and software notes

Synthetic-enabled ActiveGates are more demanding in terms of hardware requirements. See [Requirements for private Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations").

**If an ActiveGate runs the Synthetic module, it cannot have any other functional modules enabled**. If you were to run any other modules on the same ActiveGate, you might run into a situation where synthetic monitors are executed but other processes overloading the machine have a significant impact on monitor performance metrics, setting off false-positive alerts about performance degradation.

## Execute monitors

Any Synthetic-enabled ActiveGate is able to execute **both [browser as well as HTTP monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.")**.

Additionally on private locations, capacity usage is tracked separately for high-resource HTTP monitorsâthese monitors have special resource-intensive features.

To run browser monitors from a private location, you must first satisfy the engine dependencies before you install the Environment or Cluster ActiveGate. See [Create a private Synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.") for detailed instructions.

### Use cases

Private locations enable you to run monitors in your internal network when you cannot use Dynatrace [public Synthetic locations](/docs/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Learn about all currently available public Synthetic Monitoring locations.") for synthetic monitoring. With private locations you can:

* Measure internal web page performance and availability.
* Measure complex internal applications with browser clickpath monitors.

Additionally, you can also:

* Measure external resources with synthetic monitors run from internal locations.
* Monitor APIs, both internal and external.