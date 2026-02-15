---
title: Flatcar support on SELinux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/flatcar-os
scraped: 2026-02-15T21:18:52.122719
---

# Flatcar support on SELinux

# Flatcar support on SELinux

* Latest Dynatrace
* 1-min read
* Published May 30, 2023

OneAgent can now be deployed on [Flatcarï»¿](https://dt-url.net/u5034bo). However, due to certain limitations with how SELinux operates on this operating system, you need to address the following configuration constraints:

* Flatcar operates on a read-only filesystem. As a result, if you intend to use SELinux with OneAgent, it requires a specific configuration. For more information about container compatibility with SELinux policy, see the following Flatcar documentation: [Check a containerâs compatibility with SELinux policyï»¿](https://dt-url.net/ns0342m).
* Use a default path to install OneAgent with SELinux enabled.

* By default, Flatcar uses the Multi-Category Security (MCS) policy. To ensure compatibility, you need to change this setting to the `targeted` policy in the `/etc/selinux/config` file.

  ```
  SELINUXTYPE=targeted
  ```