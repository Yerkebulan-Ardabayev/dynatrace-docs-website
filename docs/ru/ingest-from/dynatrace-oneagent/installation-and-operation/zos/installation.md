---
title: z/OS installation overview
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation
scraped: 2026-02-18T21:28:32.379507
---

# z/OS installation overview

# z/OS installation overview

* Latest Dynatrace
* 1-min read
* Published Jul 22, 2016

Since the z/OS modules require multiple components in both the mainframe environment and open systems, the installation process is more complex than the standard OneAgent installation. However, with a bit of planning and coordination with the varied architecture groups, the installation of the code modules can go smoothly.

Efficient z/OS module installation is typically a team effort involving the following:

* **Open Systems Administrator**âInstalls the zRemote module.
* **Mainframe Systems Programmer**âDownloads and installs the Dynatrace product datasets for z/OS.
* **Mainframe Security Administrator**âSets up security for the zDC subsystem.
* **Mainframe Systems Programmer**âInstalls the modules on each technology you want to monitor.

Depending on your team, a single individual may be able to administer more than one of the required tasks.

![z/OS monitoring architecture](https://dt-cdn.net/images/zos-architecture-1745-8d165d1510.png)

## Related topics

* [Technology support](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.")