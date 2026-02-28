---
title: Install the zRemote module for z/OS monitoring
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/capabilities/zremote-purpose
scraped: 2026-02-28T21:18:51.771113
---

# Install the zRemote module for z/OS monitoring

# Install the zRemote module for z/OS monitoring

* Latest Dynatrace
* 1-min read
* Updated on Jul 25, 2020

The zRemote module processes binary data received from the [zLocal](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.") and routes that data, compressed and encrypted, via its local ActiveGate to Dynatrace. Hence, the zRemote module offloads much of the processing work from the [CICS, IMS, and z/OS Java code modules](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.") incurred in instrumenting subsystems and applications to an open system.

## zRemote functionality and module

If the [zRemote module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#zos_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.") is enabled on an ActiveGate, no other functional module can be enabled. Note that the zRemote module is more demanding in terms of [hardware and system requirements](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#sizing "Prepare and install the zRemote for z/OS monitoring.").

## z/OS monitoring

To monitor a z/OS LPAR, including technologies such as CICS, IMS, and Java, you need an ActiveGate with the zRemote module enabled. You can install this ActiveGate on any [Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.") or [Windows](/docs/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.") operating system that is supported by ActiveGate.

We recommend installing the zRemote module on an IBM Z or LinuxONE mainframe, on an supported [Linux operating system](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#supported-operating-systems "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes."), to avoid performance or security issues in z/OS monitoring.

For more details and configuration options, see [Install the zRemote module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring.").