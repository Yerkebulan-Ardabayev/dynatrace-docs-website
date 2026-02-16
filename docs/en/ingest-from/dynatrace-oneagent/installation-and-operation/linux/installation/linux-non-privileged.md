---
title: OneAgent non-privileged mode on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged
scraped: 2026-02-16T21:16:00.820470
---

# OneAgent non-privileged mode on Linux

# OneAgent non-privileged mode on Linux

* Latest Dynatrace
* 7-min read
* Published Jul 19, 2017

By default, OneAgent is installed in the non-privileged mode, in which superuser privileges are used once to initiate the installation process.

OneAgent is then run under an unprivileged user, retaining the complete set of functionalities.

## System requirements

To install OneAgent in non-privileged mode, your system must meet the following requirements:

* The filesystem must support [extended attributesï»¿](https://man7.org/linux/man-pages/man7/xattr.7.html).
* The system must have `libcap2` installed. For example, the default Red Hat Enterprise Linux 5 installation doesn't have `libcap2`.
* The filesystem must not be mounted as `noexec` or `nosuid`.
* Linux Filesystem Capabilities must be enabled. For example, SUSE Linux Enterprise Server 11 has Linux Filesystem Capabilities disabled by default. For more information, see [Non-privileged mode and Linux Filesystem Capabilities](#cap) below.

See [OneAgent security on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#permissions "Learn about Dynatrace OneAgent security and modifications to your Linux-based system") to learn about monitoring actions executed by OneAgent that require privileged access.

## Privileges during installation

When run in non-privileged mode, the OneAgent installer requires superuser privileges to:

* Set file capabilities for OneAgent binaries located at `/opt/dynatrace/oneagent/agent/lib[64]/*`.
* Invoke the `oneagent` service script to start `oneagentwatchdog`.
* On systems with systemd, communicate with systemd daemon via d-bus to run the following commands:

  + `systemctl <start|stop|enable|disable> oneagent.service`
  + `systemctl daemon-reload`
* On systems with SysV, execute `/sbin/chkconfig` to add the `oneagent` service script to autostart or to remove it.
* Write to `/proc/sys/kernel/core_pattern`.

Superuser privileges are dropped when the Dynatrace OneAgent service script is executed:

* On systems with systemd, the unprivileged user is included in the service definition (unit file). The systemd daemon thus runs the OneAgent service script in unprivileged mode.
* On systems with SysV, the privileges are dropped in the script when starting the OneAgent Watchdog process.

## Linux System Capabilities

Dynatrace OneAgent Watchdog starts and runs all other processes under an unprivileged user without superuser access. OneAgent binaries leverage the following Linux System Capabilities.

| Binary | Linux System Capabilities |
| --- | --- |
| oneagentwatchdog | `cap_sys_resource`[1](#fn-1-1-def)- for setting [system resource limitsï»¿](https://man7.org/linux/man-pages/man3/getrlimit.3p.html) when starting OneAgent processes |
| oneagentos | `cap_dac_override`[2](#fn-1-2-def) - for filesystem access `cap_chown`[2](#fn-1-2-def) [3](#fn-1-3-def) - for setting ownership of files replaced in the filesystem (e.g., `runc` binary) `cap_fowner` [2](#fn-1-2-def) - for setting ownership of files replaced in the filesystem `cap_sys_ptrace` - for reading data from `/proc` pseudo-filesystem and tracing processes `cap_sys_resource`[3](#fn-1-3-def) - for reading processes resource limits `cap_setuid`[4](#fn-1-4-def) - for temporary elevation of privileges to execute certain operations; for details, see [Automatic updates and operation](#autoupdate) `cap_kill` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) `cap_setfcap` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) `cap_fsetid` [3](#fn-1-3-def) [5](#fn-1-5-def) [6](#fn-1-6-def) |
| oneagentnettracer | `cap_bpf` (kernel >=5.8)[7](#fn-1-7-def) `cap_perfmon` (kernel >=5.8)[7](#fn-1-7-def) `cap_sys_admin` (kernel <5.8, or when `cap_bpf` is explicitly blocked)[7](#fn-1-7-def) `cap_dac_override` `cap_sys_ptrace` `cap_sys_resource` |
| oneagentnetwork | `cap_net_raw` - for opening raw sockets `cap_net_admin`[8](#fn-1-8-def)- for reading network interface information |
| oneagentloganalytics | `cap_dac_read_search` - for access to all logs stored on host `cap_sys_ptrace` - for reading data from `/proc` pseudo-filesystem |
| oneagentplugin | `cap_set_gid`[1](#fn-1-1-def)- for adding docker to the process supplementary groups list, which allows for the container data to be retrieved |
| oneagenthelper[9](#fn-1-9-def) | `cap_sys_admin` - for `mount()` syscall `cap_dac_override` - for inspection and modification of filesystems of the running containers `cap_sys_ptrace` - for tracing the `Docker` daemon `cap_sys_chroot` - for `chroot()` syscall `cap_fowner` - for changing ownership and permissions of files within container filesystem `cap_fsetid` - for changing ownership and permissions of files within container filesystem |
| OneAgent Installer executed during auto-update | `cap_dac_override` - for filesystem access `cap_chown` - for filesystem access `cap_fowner` - for filesystem access `cap_fsetid` - for filesystem access `cap_kill` - to be able to signal all the running processes, e.g. stopped orphaned OneAgent processes `cap_setfcap` - for setting Linux Filesystem capabilities file capabilities on agent binaries during the installation |
| oneagentosconfig | `cap_setuid`[6](#fn-1-6-def)- for execution of privileged operations during the installation process `cap_setgid`[6](#fn-1-6-def)- for setting group ownership of files during the installation process |
| oneagenteventstracer | `cap_sys_admin` - for `perf_event_open()` syscall `cap_dac_override` - for access to `/sys/kernel/debug/tracing` |
| oneagentdmidecode | `cap_dac_override` - for filesystem access |
| oneagentmntconstat | `cap_dac_read_search` - for retrieving disk occupation stats with `statvfs64()` `cap_sys_chroot` - for `setns()` syscall `cap_sys_admin` - for `setns()` syscall `cap_sys_ptrace` - for accessing `/proc/1/ns` |
| oneagentebpfdiscovery | `cap_bpf` (kernel >=5.8)[7](#fn-1-7-def) `cap_perfmon` (kernel >=5.8)[7](#fn-1-7-def) `cap_sys_admin` (kernel <5.8, or when `cap_bpf` is explicitly blocked)[7](#fn-1-7-def) `cap_dac_override` - for write access to /sys/kernel/debug/tracing `cap_sys_resource` - for removing memory usage limitation of the bpf program |

1

Required only during initialization phase and is unconditionally dropped afterwards.

2

Not used if [auto-updates](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#enable-or-disable-auto-update "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") and [automatic injection](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") are disabled.

3

Kept in permitted set only and raised to the effective set when needed.

4

Only if ambient capabilities aren't supported.

5

Not used if [auto-updates](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#enable-or-disable-auto-update "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") are disabled.

6

Only if ambient capabilities are supported.

7

Only for kernels 5.8 and newer, unless usage of unprivileged `cap_bpf` is [blocked by the OSï»¿](https://ubuntu.com/blog/whats-new-in-security-for-ubuntu-21-10), then it fallbacks to `cap_sys_admin`. For older kernel versions, `cap_sys_admin` is enabled instead.

8

Only on kernels older than 2.6.33.

9

Not started if [automatic injection](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#injection-toggle "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.") is disabled.

Enable Linux Filesystem Capabilities

Linux Filesystem Capabilities are required to install OneAgent in non-privileged mode. SUSE Linux Enterprise Server 11 has Linux Filesystem Capabilities disabled by default. These capabilities might also be disabled in other supported Linux distributions or as the result of a custom configuration. The OneAgent installer prints the following message if Linux Filesystem Capabilities are disabled:

```
Warning: Failed to enable non-privileged mode, kernel does not support file capabilities.
```

You can also check the kernel boot options to see if Linux Filesystem Capabilities are enabled. Run the following command to check your kernel boot options.

```
cat /proc/cmdline
```

If you find `file_caps=1` in the output, your setup is fine.

To enable Linux Filesystem Capabilities, add `file_caps=1` to your kernel boot options. For example, on SUSE Linux Enterprise Server 11, use [YaSTï»¿](https://doc.opensuse.org/documentation/leap/reference/html/book-reference/cha-grub2.html#sec-grub2-yast2-config), edit kernel boot options, add `file_caps=1`, and reboot the machine.

## Privileges during automatic updates and operation

The scope of privileges required by OneAgent depends on whether the kernel supports Linux ambient capabilities. As a general rule, kernel 4.3+ supports ambient capabilities. However, in the case of Red Hat Enterprise Linux, these may be supported in older kernel versions because of the Red Hat policy to backport patches. This makes ambient capabilities supported by kernel versions as old as 3.10.x.

Kernels with ambient capabilities (version 4.3+)

Kernels without ambient capabilities (version 2.6.26 to 4.3)

During an automatic update, the installer starts under an unprivileged `dtuser` with proper ambient capabilities set. OneAgent doesn't require root access to perform an automatic update.

Red Hat Enterprise Linux 7 has a too low `systemd` (v219 instead of the required v221), and to be able to run automatic updates in non-privileged mode, we're temporarily elevating the privileges to run `systemctl <start|stop|enable|disable> oneagent.service`.

OneAgent will work under the non-privileged `dtuser` in the majority of cases. When the kernel doesn't provide ambient capabilities, it automatically elevates its privileges to the superuser level using `setuid(0)` in the following cases:

* OneAgent automatic updates
* Host OSI ID generation on Azure hosts
* Docker containers properties detection
* Self-diagnostics

If you don't want to grant the superuser permission level to OneAgent, you can disable it by adding the `DISABLE_ROOT_FALLBACK=1` parameter to the OneAgent installation command. For example:

`sudo /bin/sh Dynatrace-OneAgent-Linux-1.0.0.sh NON_ROOT_MODE=1 DISABLE_ROOT_FALLBACK=1`

In such cases, you must perform [manual updates on individual hosts](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux#manual-update "Learn about the different ways to update OneAgent on Linux."). We don't recommend using the `DISABLE_ROOT_FALLBACK=1` parameter for OneAgents on Azure or Docker containers.

## How do I know if OneAgent operates in non-privileged mode?

The installer prints a message at the end of OneAgent installation. Depending on the kernel version and its support for ambient capabilities, you will see one of the following messages:

* `Non-privileged mode is enabled`  
  The kernel supports ambient capabilities, the root access is not used for updates or operation.
* `Enabled non-privileged mode, but ambient capabilities are not supported by kernel`  
  The kernel is within the minimum supported version, but due to non-supported ambient capabilities, OneAgent needs to elevate privileges in select cases, see above.
* `Failed to enable non-privileged mode`  
  The kernel doesn't meet the minimum version requirements to enable non-privileged mode.