---
title: Requirements for private Synthetic locations
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic
scraped: 2026-02-18T05:35:18.909123
---

# Requirements for private Synthetic locations

# Requirements for private Synthetic locations

* Reference
* 15-min read
* Updated on Jan 13, 2026

Ensure that the host you want to use for your private location complies with the following requirements.

End-of-support information

* There are no new versions of Chromium for Red Hat/Oracle Linux/Rocky Linux 8 beyond version 133.
  For important security and stability reasons, we've decided to discontinue our support for installing **Synthetic-enabled** ActiveGate on Red Hat/Oracle Linux/Rocky Linux 8 after ActiveGate version 1.325.
  ActiveGate version 1.325 is **the last Synthetic-enabled** ActiveGate supported on Red Hat/Oracle Linux/Rocky Linux 8.
  Additionally, with Dynatrace version 1.326, we plan to introduce mechanisms preventing Synthetic-enabled ActiveGates on Red Hat/Oracle Linux/Rocky Linux 8 from being updated beyond version 1.325.
* Chromium development for Amazon Linux 2 stopped at version 126.
  For important security and stability reasons, we've decided to discontinue our support for installing Synthetic-enabled ActiveGate on Amazon Linux 2 after ActiveGate version 1.307.
  ActiveGate version 1.307 is the last Synthetic-enabled ActiveGate to support Amazon Linux 2.
  Additionally, with Dynatrace version 1.308, we have introduced mechanisms preventing Synthetic-enabled ActiveGates on Amazon Linux 2 from being updated beyond version 1.307.
* Chromium development for Red Hat/CentOS 7 stopped at version 126.
  For important security and stability reasons, we've decided to discontinue our support for installing Synthetic-enabled ActiveGate on Red Hat/CentOS 7 after ActiveGate version 1.305.
  ActiveGate version 1.305 is the last Synthetic-enabled ActiveGate to support Red Hat/CentOS 7.
  Additionally, with Dynatrace version 1.306, we have introduced mechanisms preventing Synthetic-enabled ActiveGates on Red Hat/CentOS 7 from being updated beyond version 1.305.

  + Since Red Hat Enterprise Linux 7 reached [End of Maintenanceï»¿](https://dt-url.net/af03uea) support on June 30, 2024, all of its packages have been archived. This means that it may not be possible to find the required dependencies for update. For more details, see the [Red Hat Enterprise Linux 7 statusï»¿](https://dt-url.net/e623zr1)
* Check the latest [ActiveGate release notes](/docs/whats-new/activegate "Release notes for Dynatrace ActiveGate") for the oldest supported ActiveGate versions.

## Operating system requirements

Antivirus and Anti-Malware software

Antivirus and anti-malware software can adversely affect Dynatrace Synthetic monitoring capabilities. The antivirus or anti-malware software might block the Chromium browser or Dynatrace processes responsible for executing synthetic monitors, cause Synthetic-enabled ActiveGate installation failures, interfere with network communication, and impact the reliability of measurements.

Please also note

To ensure proper stability and performance, consider adding the following directories and processes to the allowed list or excluding them from the policy:

**Directories:**

* All directories with `synthetic` in their path. For an overview of directories in use, see [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files#default-activegate-directories--windows "Find out where ActiveGate files are stored on Windows and Linux systems.").

**Processes:**

* chrome
* vucwrapper
* java

This is the minimal list of processes and directories required for Dynatrace Synthetic to operate. It's not guaranteed that the service will function correctly with only these exclusions. Collaborate with your vendor to appropriately allow expected behaviors from Dynatrace.

Prior to contacting Dynatrace support to troubleshoot issues with your private synthetic locations make sure that antivirus or anti-malware software was excluded as a source of problems.

A freshly installed ActiveGate can run your private synthetic monitors (both HTTP and browser monitors) on the following operating systems.

### Windows

#### Supported operating systems

| Windows OS | Versions |
| --- | --- |
| Windows Server | 2016, 2019, 2022 |

#### Chromium version on Windows

On Windows, the ActiveGate installer package includes the Chromium browser used to run browser monitors. The table below shows the Chromium versions that are bundled with the respective ActiveGate versions.

| ActiveGate version | Included Chromium version |
| --- | --- |
| 1.329 | 142 |
| 1.327 | 141 |
| 1.325 | 140 |
| 1.323 | 139 |
| 1.321 | 138 |
| 1.319 | 138 |
| 1.317 | 137 |
| 1.315 | 136 |
| 1.313 | 135 |
| 1.311 | 134 |
| 1.309 | 133 |
| 1.307 | 132 |
| 1.305 | 130 |
| 1.303 | 129 |

#### Unsupported Windows versions for testing purposes only

If you only want to test private Synthetic locations on a non-production host, for example, your own desktop, you can install a Synthetic-enabled ActiveGate on unsupported Windows versions such as Windows 10 or Windows 11.

As of ActiveGate version 1.263+, Synthetic-enabled ActiveGate no longer works on Windows Server 2012 for testing purposes. [Google has dropped support for Windows 2012 Server with Chromium 110ï»¿](https://dt-url.net/e2026id), which is bundled with the [ActiveGate version 1.263 installation package](#chromium-windows).

### Linux

#### Supported operating systems

| Linux distribution | Versions |
| --- | --- |
| Red Hat Enterprise Linux[1](#fn-1-1-def) | 9.2, 9.4, 9.6 |
| Ubuntu | 20.04, 22.04, 24.04 |
| Amazon Linux | 2023 |
| Oracle Linux[1](#fn-1-1-def) | 9.5 |
| Rocky Linux[2](#fn-1-2-def) | 9.7 |

1

The Synthetic installer can be installed on all minor releases of Oracle Linux 9. However, we recommend using the latest currently supported versions according to documentation for [Oracle Linux 9ï»¿](https://docs.oracle.com/en/operating-systems/oracle-linux/9/).

2

The Synthetic installer can be installed on all minor releases of Rocky Linux 9. However, we recommend using the latest currently supported versions according to [Rocky Linux Release and Version Guideï»¿](https://wiki.rockylinux.org/rocky/version/#current-supported-releases).

#### Deprecated operating systems

| Linux distribution | Versions |
| --- | --- |
| Red Hat Enterprise Linux | 7.9[1](#fn-2-1-def) |
| CentOS | 7.9[1](#fn-2-1-def) |
| Amazon Linux | 2[2](#fn-2-2-def) |
| Red Hat Enterprise Linux | 8.8[3](#fn-2-3-def) |
| Red Hat Enterprise Linux | 8.10[3](#fn-2-3-def) |
| Oracle Linux | 8.10[3](#fn-2-3-def) |
| Rocky Linux | 8.10[3](#fn-2-3-def) |

1

ActiveGate version 1.305 is the last Synthetic-enabled ActiveGate to support Red Hat/CentOS 7.

2

ActiveGate version 1.307 is the last Synthetic-enabled ActiveGate to support Amazon Linux 2.

3

ActiveGate version 1.325 is the last Synthetic-enabled ActiveGate to support Red Hat/Oracle Linux/Rocky Linux 8.

#### Chromium versions on Linux

We strongly recommend that you keep your Linux-based Synthetic-enabled ActiveGates and Chromium versions updatedâDynatrace supports Chromium versions that are no more than two versions behind the latest Dynatrace-supported version for a specific ActiveGate release. For example, if the latest supported Chromium version is 103, Dynatrace supports up to Chromium version 101. If the provided Chromium version is significantly older for a specific OS, we support only the provided version. See information on updating Chromium [automatically](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#chromium "Analyze and manage capacity usage at your private Synthetic locations.") and [manually](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#chromium-manual "Analyze and manage capacity usage at your private Synthetic locations.").

On Linux, the ActiveGate installer downloads the Chromium dependencies that are required by the Synthetic engine. On Red Hat and Rocky, you need to enable particular repositories from which the installer downloads the dependencies. The Dynatrace web UI provides you with all the required commands. For detailed instructions, see [Create a private synthetic location](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

When [installing ActiveGate and Chromium from a custom, local repository](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location#custom-repo "Learn how to create a private location for synthetic monitoring."), you need to resolve all dependencies and enable repositories as required; the custom repository can be used only for Chromium packages, not their dependencies. Place the Chromium package archive and the signature file in the custom repository for installation. If your package archive file is `https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-107.0.5304.87-2168.tgz` (Chromium 107 for Ubuntu 20 and 22 on ActiveGate version 1.255), you can find the signature file by appending `.sig` to the URL: `https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-107.0.5304.87-2168.tgz.sig`.

* Chromium development for Red Hat/CentOS 7 and Amazon Linux 2 stopped at version 126.

  + Since Red Hat Enterprise Linux 7 reached [End of Maintenanceï»¿](https://dt-url.net/af03uea) support on June 30, 2024, all of its packages have been archived. This means that it may not be possible to find the required dependencies for update. For more details, see the [Red Hat Enterprise Linux 7 statusï»¿](https://dt-url.net/e623zr1)

Due to changes in `libdav1d.so.6` packet availability Chromium versions older than 130 cannot be installed on Red Hat/Rocky Linux 9.
Please refer to [troubleshooting guideï»¿](https://dt-url.net/x303x5f) for details.

| ActiveGate version | Latest supported Chromium version Red Hat, CentOS, Oracle Linux 8 | Latest supported Chromium version Ubuntu | Latest supported Chrome for Testing version Amazon Linux 2023, Ubuntu 24, Oracle Linux 9 |
| --- | --- | --- | --- |
| 1.329 | 142 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-142.0.7444.175-2.el9.tgz) | 142 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-142.0.7444.175-3313.tgz) | [142ï»¿](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-142.0.7444.175.zip) |
| 1.327 | 141 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-141.0.7390.122-1.el9.tgz) | 141 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-141.0.7390.122-3285.tgz) | [141ï»¿](https://synthetic-packages.s3.amazonaws.com/Chrome/chrome-for-testing-linux64/chrome-for-testing-linux64-141.0.7390.122.zip) |
| 1.325 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 140 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-140.0.7339.185-1.el9.tgz) | 140 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-140.0.7339.185-3251.tgz) | 140 |
| 1.323 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 139 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-139.0.7258.138-1.el9.tgz) | 139 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-139.0.7258.138-3235.tgz) | 139 |
| 1.321 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 138 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.157-1.el9.tgz) | 138 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.157-3203.tgz) | 138 |
| 1.319 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 138 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-138.0.7204.100-1.el9.tgz) | 138 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-138.0.7204.100-3199.tgz) | 138 |
| 1.317 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 137 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-137.0.7151.103-1.el9.tgz) | 137 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-137.0.7151.103-3169.tgz) | 137 |
| 1.315 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 136 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-136.0.7103.59-1.el9.tgz) | 136 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-136.0.7103.59-3121.tgz) | 136 |
| 1.313[2](#fn-3-2-def) | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 135 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-135.0.7049.95-1.el9.tgz) | 135 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-135.0.7049.95-3110.tgz) | 135 |
| 1.311 | 133 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-133.0.6943.141-1.el8.tgz), 134 [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-134.0.6998.35-1.el9.tgz) | 134 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-134.0.6998.35-3060.tgz) | 134 |
| 1.309 | 132 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-132.0.6834.159-1.el8.tgz), [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-132.0.6834.159-1.el9.tgz) | 132 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-132.0.6834.159-3036.tgz) | 133 |
| 1.307[1](#fn-3-1-def) | 126 [Amazon Linux 2ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz), 131 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-131.0.6778.204-1.el8.tgz), [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-131.0.6778.204-1.el9.tgz) | 131 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-131.0.6778.85-3002.tgz) | 131 |
| 1.305 | 126 [Red Hat/CentOS 7 and Amazon Linux 2ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz), 130 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-130.0.6723.69-1.el8.tgz), [Red Hat/Rocky Linux 9ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-130.0.6723.116-1.el9.tgz) | 130 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-130.0.6723.69-2985.tgz) | 130 |
| 1.303 | 126 [Red Hat/CentOS 7 and Amazon Linux 2ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-126.0.6478.114-1.el7.tgz), 129 [Red Hat/Oracle/Rocky Linux 8ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/rpm/chromium-129.0.6668.89-1.el8.tgz), Red Hat/Rocky Linux 9 requires chromium 130 | 129 [Ubuntu 20.04 and 22.04ï»¿](https://synthetic-packages.s3.amazonaws.com/Chromium/snap/chromium-129.0.6668.89-2965.tgz) | 129 |

1

Introduced support for Ubuntu 24.

2

Introduced support for Oracle Linux 9.

#### File Access Policy Daemon framework (`fapolicyd`)

If not configured correctly, the File Access Policy Daemon (`fapolicyd`) can potentially affect Dynatrace Synthetic monitoring capabilities. Similarly to antivirus or anti-malware software, `fapolicyd` might block the Chromium browser or Dynatrace processes responsible for executing synthetic monitors.

To ensure proper stability and performance, consider adding directories and processes to the allowed list or excluding them from the policy. For more detailed information, refer to the [Red Hat documentation on fapolicydï»¿](https://dt-url.net/tn1v0z1x). Prior to contacting Dynatrace support to troubleshoot issues with your private synthetic locations, make sure that `fapolicyd` was excluded as a source of problems.

File Access Policy Daemon framework can be run in debug mode where all denials are logged, making tracking down missing rules and troubleshooting issues easier. For more detailed information about its debug mode, refer to the [documentation on troubleshooting problems related to fapolicydï»¿](https://dt-url.net/e943wcc)

## Hardware requirements

### General considerations

* Note that a Synthetic-enabled ActiveGate has more demanding hardware and system requirements than a regular Environment or Cluster ActiveGate. We strongly recommend using a Synthetic-enabled ActiveGate exclusively for synthetic monitoring purposes.
* Any additional component running on the host should be taken into account when planning resources provisioning. For instance, if the location is monitored by [OneAgent](/docs/ingest-from/dynatrace-oneagent/oa-requirements "OneAgent code module requirements") or another deep monitoring solution, memory (RAM) requirements will increase.
* You need to uninstall and reinstall your Synthetic-enabled ActiveGate to change its size, for example, after increasing the resources of your S-sized ActiveGate to meet the requirements for a size M. Reinstallation is required before you can make use of the updated resources for synthetic monitoring; otherwise, your ActiveGate will continue to show up as size S (**Synthetic Node size**) in **Deployment Status** and will be subject to the execution limits of size S.

### Sizing guide

Based on the number of tests executed per hour, Synthetic-enabled ActiveGates need to meet the following hardware requirements.

Limit values

The estimated limits listed in the table below were determined in our internal tests. The actual values might vary depending on the complexity of your monitors.

XS node

S node

M node

L node

XS node

While XS nodes can be used on Windows Server-based ActiveGates, they may not be the best fit due to the higher hardware demands of Chromium. For optimal performance and to prepare for future enhancements, we recommend having at least 8 GB of RAM and 25 GB of free disk space.

On Linux systems with only 4 GB of RAM, the increasing resource requirements of Chrome (or Chromium), combined with the installation of third-party tools on the host, may lead to occasional memory shortages. Upgrading to 8 GB of RAM is strongly recommended to help ensure a smoother and more reliable experience.

|  | Node with browser monitor support | Browserless node |
| --- | --- | --- |
| Minimum CPUs | 2 vCPU | 1 vCPU |
| Minimum free disk space | 20 GB | 17 GB |
| Minimum RAM | 4 GB | 4 GB |
| Minimum free RAM | 3 GB | 2,7 GB |
| Minimum disk IOPS (Windows) | 100 | 100 |
| Estimated maximum number of HTTP monitor executions/h[1](#fn-4-1-def) | 300k | 300k |
| Estimated maximum number of high-resource HTTP monitor[2](#fn-4-2-def) executions/h | 10k | 10k |
| Estimated maximum number of browser monitor executions/h | 300 | - |
| Estimated maximum number of NAM ICMP monitor packets/h[3](#fn-4-3-def) [5](#fn-4-5-def) | 500k | 500k |
| Estimated maximum number of NAM TCP monitor requests/h[4](#fn-4-4-def) [6](#fn-4-6-def) | 1M | 1M |
| Estimated maximum number of NAM DNS monitor request/h[4](#fn-4-4-def) [7](#fn-4-7-def) | 100k | 100k |

Footnotes

1

Calculated as 5000 monitor executions (maximum for a single environment) run once every minute (maximum frequency).

2

These are HTTP monitors on private locations with any of: pre- or post-execution scripts, OAuth2 authorization, Kerberos authentication.

3

For NAM monitors using ICMP request type, capacity is related to number of ICMP echo requests (packets) that are being sent during monitors execution. As this number of packets-to-be-sent may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

4

For NAM monitors using TCP and DNS request types, capacity is related to the number of network connections (requests) that are being sent during monitors execution. As this number of requests may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

5

During load tests that helped to establish capacity limits, NAM ICMP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings and single packet per-request) and were scheduled every 1 minute.
There were multiple target hosts used during tests; all of them were responding properly with average RTT around 200ms.

6

During load tests that helped to establish capacity limits, NAM TCP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings) and were scheduled every 1 minute.
There were multiple target hosts and ports used during tests; all of them were responding properly with average TCP connection time around 200ms.

7

During load tests that helped to establish capacity limits, NAM DNS monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time). Please note that DNS server used during resolution should be able to handle incoming requests and may not consider the incoming traffic as a subject to throttling or rejection (for example, due to detection as bot-originated).
Monitors were using default settings (including default timeouts settings and UDP as a transport) and were scheduled every 1 minute.
There were multiple resolution targets used during tests; all of them were resolved properly with average DNS resolution time around 10ms.
Publicly available DNS servers were used: Google (8.8.8.8 and 8.8.4.4) and Cloudflare (1.1.1.1 and 1.1.1.2)

|  | Node with browser monitor support | Browserless node |
| --- | --- | --- |
| Minimum CPUs | 4 vCPU | 2 vCPU |
| Minimum free disk space | 25 GB | 22 GB |
| Minimum RAM | 8 GB | 8 GB |
| Minimum free RAM | 5 GB | 4 GB |
| Minimum disk IOPS (Windows) | 200 | 200 |
| Estimated maximum number of HTTP monitor executions/h[1](#fn-5-1-def) | 300k | 300k |
| Estimated maximum number of high-resource HTTP monitor[2](#fn-5-2-def) executions/h | 20k | 20k |
| Estimated maximum number of browser monitor executions/h | 650 | - |
| Estimated maximum number of NAM ICMP monitor packets/h[3](#fn-5-3-def) [5](#fn-5-5-def) | 1M | 1M |
| Estimated maximum number of NAM TCP monitor requests/h[4](#fn-5-4-def) [6](#fn-5-6-def) | 2M | 2M |
| Estimated maximum number of NAM DNS monitor request/h[4](#fn-5-4-def) [7](#fn-5-7-def) | 200k | 200k |

Footnotes

1

Calculated as 5000 monitor executions (maximum for a single environment) run once every minute (maximum frequency).

2

These are HTTP monitors on private locations with any of: pre- or post-execution scripts, OAuth2 authorization, Kerberos authentication.

3

For NAM monitors using ICMP request type, capacity is related to number of ICMP echo requests (packets) that are being sent during monitors execution. As this number of packets-to-be-sent may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

4

For NAM monitors using TCP and DNS request types, capacity is related to the number of network connections (requests) that are being sent during monitors execution. As this number of requests may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

5

During load tests that helped to establish capacity limits, NAM ICMP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings and single packet per-request) and were scheduled every 1 minute.
There were multiple target hosts used during tests; all of them were responding properly with average RTT around 200ms.

6

During load tests that helped to establish capacity limits, NAM TCP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings) and were scheduled every 1 minute.
There were multiple target hosts and ports used during tests; all of them were responding properly with average TCP connection time around 200ms.

7

During load tests that helped to establish capacity limits, NAM DNS monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time). Please note that DNS server used during resolution should be able to handle incoming requests and may not consider the incoming traffic as a subject to throttling or rejection (for example, due to detection as bot-originated).
Monitors were using default settings (including default timeouts settings and UDP as a transport) and were scheduled every 1 minute.
There were multiple resolution targets used during tests; all of them were resolved properly with average DNS resolution time around 10ms.
Publicly available DNS servers were used: Google (8.8.8.8 and 8.8.4.4) and Cloudflare (1.1.1.1 and 1.1.1.2)

|  | Node with browser monitor support | Browserless node |
| --- | --- | --- |
| Minimum CPUs | 8 vCPU | 4 vCPU |
| Minimum free disk space | 30 GB | 23 GB |
| Minimum RAM | 16 GB | 16 GB |
| Minimum free RAM | 8 GB | 6,5 GB |
| Minimum disk IOPS (Windows) | 400 | 400 |
| Estimated maximum number of HTTP monitor executions/h[1](#fn-6-1-def) | 300k | 300k |
| Estimated maximum number of high-resource HTTP monitor[2](#fn-6-2-def) executions/h | 60k | 60k |
| Estimated maximum number of browser monitor executions/h | 1200 | - |
| Estimated maximum number of NAM ICMP monitor packets/h[3](#fn-6-3-def) [5](#fn-6-5-def) | 1.5M | 1.5M |
| Estimated maximum number of NAM TCP monitor requests/h[4](#fn-6-4-def) [6](#fn-6-6-def) | 3M | 3M |
| Estimated maximum number of NAM DNS monitor request/h[4](#fn-6-4-def) [7](#fn-6-7-def) | 300k | 300k |

Footnotes

1

Calculated as 5000 monitor executions (maximum for a single environment) run once every minute (maximum frequency).

2

These are HTTP monitors on private locations with any of: pre- or post-execution scripts, OAuth2 authorization, Kerberos authentication.

3

For NAM monitors using ICMP request type, capacity is related to number of ICMP echo requests (packets) that are being sent during monitors execution. As this number of packets-to-be-sent may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

4

For NAM monitors using TCP and DNS request types, capacity is related to the number of network connections (requests) that are being sent during monitors execution. As this number of requests may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

5

During load tests that helped to establish capacity limits, NAM ICMP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings and single packet per-request) and were scheduled every 1 minute.
There were multiple target hosts used during tests; all of them were responding properly with average RTT around 200ms.

6

During load tests that helped to establish capacity limits, NAM TCP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings) and were scheduled every 1 minute.
There were multiple target hosts and ports used during tests; all of them were responding properly with average TCP connection time around 200ms.

7

During load tests that helped to establish capacity limits, NAM DNS monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time). Please note that DNS server used during resolution should be able to handle incoming requests and may not consider the incoming traffic as a subject to throttling or rejection (for example, due to detection as bot-originated).
Monitors were using default settings (including default timeouts settings and UDP as a transport) and were scheduled every 1 minute.
There were multiple resolution targets used during tests; all of them were resolved properly with average DNS resolution time around 10ms.
Publicly available DNS servers were used: Google (8.8.8.8 and 8.8.4.4) and Cloudflare (1.1.1.1 and 1.1.1.2)

|  | Node with browser monitor support | Browserless node |
| --- | --- | --- |
| Minimum CPUs | 16 vCPU | 8 vCPU |
| Minimum free disk space | 40 GB | 25 GB |
| Minimum RAM | 32 GB | 32 GB |
| Minimum free RAM | 12 GB | 10 GB |
| Minimum disk IOPS (Windows) | 750 | 750 |
| Estimated maximum number of HTTP monitor executions/h[1](#fn-7-1-def) | 300k | 300k |
| Estimated maximum number of high-resource HTTP monitor[2](#fn-7-2-def) executions/h | 100k | 100k |
| Estimated maximum number of browser monitor executions/h | 2200 | - |
| Estimated maximum number of NAM ICMP monitor packets/h[3](#fn-7-3-def) [5](#fn-7-5-def) | 2M | 2M |
| Estimated maximum number of NAM TCP monitor requests/h[4](#fn-7-4-def) [6](#fn-7-6-def) | 4M | 4M |
| Estimated maximum number of NAM DNS monitor request/h[4](#fn-7-4-def) [7](#fn-7-7-def) | 400k | 400k |

Footnotes

1

Calculated as 5000 monitor executions (maximum for a single environment) run once every minute (maximum frequency).

2

These are HTTP monitors on private locations with any of: pre- or post-execution scripts, OAuth2 authorization, Kerberos authentication.

3

For NAM monitors using ICMP request type, capacity is related to number of ICMP echo requests (packets) that are being sent during monitors execution. As this number of packets-to-be-sent may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

4

For NAM monitors using TCP and DNS request types, capacity is related to the number of network connections (requests) that are being sent during monitors execution. As this number of requests may significantly vary among defined monitors, using the number of monitor executions as a capacity limit would be inaccurate.

5

During load tests that helped to establish capacity limits, NAM ICMP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings and single packet per-request) and were scheduled every 1 minute.
There were multiple target hosts used during tests; all of them were responding properly with average RTT around 200ms.

6

During load tests that helped to establish capacity limits, NAM TCP monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time).
Monitors were using default settings (including default timeouts settings) and were scheduled every 1 minute.
There were multiple target hosts and ports used during tests; all of them were responding properly with average TCP connection time around 200ms.

7

During load tests that helped to establish capacity limits, NAM DNS monitors were exclusively scheduled on location; monitors had the following characteristic. Actual capacity may be different for other environments (for example, those where monitored targets respond slower or are failing to provide a response within timeout limit or other type of monitors are executed at the same time). Please note that DNS server used during resolution should be able to handle incoming requests and may not consider the incoming traffic as a subject to throttling or rejection (for example, due to detection as bot-originated).
Monitors were using default settings (including default timeouts settings and UDP as a transport) and were scheduled every 1 minute.
There were multiple resolution targets used during tests; all of them were resolved properly with average DNS resolution time around 10ms.
Publicly available DNS servers were used: Google (8.8.8.8 and 8.8.4.4) and Cloudflare (1.1.1.1 and 1.1.1.2)

### Storage and file system permissions

The table below shows the default installation locations (Linux and Windows) of various ActiveGate directories and the minimum size requirements. This information is compiled from details in [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

Installation parameter

Default path

Min. size

Notes

`<INSTALL>`

* `/opt/dynatrace/`
* `%PROGRAMFILES%\dynatrace`

600 MB

For executable files, libraries, and related files

* 300 MB for ActiveGate
* 270 MB for Private Synthetic files

`<LOGS>`

* `/var/log/dynatrace`
* `%PROGRAMDATA%\dynatrace`

1.7 GB

* 500 MB for ActiveGate logs
* 1 GB for Private Synthetic logs
* 200 MB for autoupdater logs

`<CONFIG>`

* `/var/lib/dynatrace`
* `%PROGRAMDATA%\dynatrace`

1 MB

`<TEMP>`

* `/var/tmp/dynatrace`
* `%PROGRAMDATA%\dynatrace`

21 GB[1](#fn-8-1-def)

* 1 GB for ActiveGate temporary files (without cached OneAgent installers and container images)
* 20 GB for Private Synthetic temporary files (including execution logs, cache, and screenshots)

1

For an XS ActiveGateâmore space is required for execution logs on larger ActiveGates.

#### Permissions for `/tmp`

Synthetic-enabled ActiveGate requires write access to the `/tmp` directory during runtime. Its dependencies, including xvfb, utilize `/tmp` for storing temporary files and runtime data.
Lack of write permissions to this directory may result in unexpected failures or degraded functionality.
Ensure that the host environment provides sufficient access rights and available space in `/tmp` to support these operations reliably.

## Related topics

* [ActiveGate directories](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.")