---
title: OneAgent security on Linux
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux
scraped: 2026-02-18T21:28:15.992838
---

# OneAgent security on Linux

# OneAgent security on Linux

* Latest Dynatrace
* 5-min read
* Published Nov 11, 2020

To fully automate the monitoring of your operating systems, processes, and network interfaces, OneAgent performs the following changes to your system.

OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Permissions

By default, OneAgent is installed in non-privileged mode, in which superuser privileges are used once to initiate the installation process. OneAgent is then run under an unprivileged user, retaining the complete set of functionalities. For details and system requirements, see [OneAgent non-privileged mode on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.")

### Operation

OneAgent performs the following privileged operations. Depending on whether OneAgent runs in non-privileged or privileged mode, the scope of operations is the same, only the underlying mechanism differs. In privileged mode, OneAgent runs as root, while non-privileged mode utilizes the Linux System Capabilities.

* Access the list of open sockets for each process.
* Access the list of libraries loaded for each process.
* Access the name and path of the executable file for each process.
* Access command-line parameters for each process.
* Monitor network traffic.
* Read application configuration files.
* Parse executables for Go Discovery.
* Gather monitoring data related to Docker containers.

If you have Log Monitoring enabled, root privileges are also required for:

* Accessing system logs: `/var/log/syslog` and `/var/log/messages`.
* Accessing the list of open file handlers for each process (`/proc` file system).
* Accessing the log file for each process.

## Operating system changes

The OneAgent installer performs the following changes to your system:

* The `dtuser` user is created. You can change the default name using the `USER` [installation parameter](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#user "Learn how to use the Linux installer with command line parameters.").
* The `oneagent` service is registered in the system init.
* `ABRT` (Red Hat) and `Apport` (Debian) services are stopped and disabled.
* A custom SELinux module is installed on systems with SELinux enabled. The sources of the SELinux module installed by the OneAgent installer are available under `{install-dir}/agent/SELinuxPolicy`, `/opt/dynatrace/oneagent/agent/SELinuxPolicy` by default.
* Installs OneAgent components in the system library directories.
* Sets up `/etc/ld.so.preload` to automatically monitor processes.

## Files modified

### Installation

The OneAgent installer modifies the following system files:

* `/proc/sys/kernel/core_pattern` and `/etc/sysctl.conf` are modified to enable core dump processing by `oneagentdumpproc`. The original `core_pattern` configuration will still work following installation and will be preserved in `/opt/dynatrace/oneagent/agent/conf/original_core_pattern`, where you can define your own core settings using the format as specified in [Linux Programmer's Manualï»¿](https://man7.org/linux/man-pages/man5/core.5.html). See [Linux core dump handling](/docs/observe/application-observability/profiling-and-optimization/crash-analysis#linux-core-dump-handling "Learn how Dynatrace can help you gain insight into process crashes.") for more information.
* `/etc/ld.so.preload` is modified to enable auto-injection into processes.

### Operation

OneAgent modifies the following files during its operation:

* The OneAgent wrapper overwrites the `/var/vcap/packages/runc/bin/runc` file (Garden runc) to allow injection. This happens periodically during runtime. The original file is stored as `runc-original` and is restored by the [uninstall script](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").
* On [CRI-Oï»¿](https://cri-o.io/) hosts (OCI-based implementation of Kubernetes Container Runtime Interface), the crio hook (`oneagent_crio_injection-0.1.0.json`) is copied to the path specified in the `hooks_dir` parameter of the CRI-O configuration file (`/etc/crio/crio.conf`). If the `hooks_dir` parameter is not set, one of the default paths is used, either `/etc/containers/oci/hooks.d/` or `/usr/share/containers/oci/hooks.d/`. The hook is removed by the uninstall script.

## Files added

### Installation

The OneAgent installer adds the following files to your system:

* OneAgent binaries and configuration files are saved in `/opt/dynatrace/oneagent`. Note that you can change the location using the [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#installation-path "Learn how to use the Linux installer with command line parameters.") parameter.
* Startup scripts are copied to `/etc/init.d` on systems with SystemV and to `/etc/systemd/system` on systems with systemd.
* `liboneagentproc.so` is placed in the system library directories, which vary depending on a distribution. For example,

  + Ubuntu 14.04 (with 32-bit libraries installed): `/lib32` and `/lib/x86_64-linux-gnu`
  + Fedora 25: `/lib64`
  + OpenSUSE 42.2: `/lib` and `/lib64`
  + CentOS 7.3 and Red Hat Enterprise Linux 6: `/lib` and `/lib64`

### Operation

* OneAgent temporary files and runtime configuration are saved in `/var/lib/dynatrace/oneagent/runtime`.
* OneAgent persistent configuration is saved in `/var/lib/dynatrace/oneagent/agent/config`.
* Large runtime data, such as memory dumps, is saved in `/var/lib/dynatrace/oneagent/datastorage`. Note that you can change the location of large runtime data using the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters.") parameter.

## System logs downloaded by OneAgent

OneAgent downloads certain system logs so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or automatic updates.

* `/var/log/boot.log`
* `/var/log/dmesg`
* `/var/log/dpkg.log`
* `/var/log/kern.log`
* `/var/log/messages`
* `/var/log/syslog`
* `/var/log/yum.log`
* `/var/log/audit/audit.log`
* `/var/log/zypper.log`
* `/etc/nsswitch.conf`
* Output of `/usr/sbin/apparmor_status` command
* Output of `/bin/journalctl --utc -a -n 10000` command

Revoking access to system logs

To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.  
For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Globally writable directories

The [OneAgent directory structure](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/disk-space-requirements-for-oneagent-installation-and-update-on-linux "Learn the OneAgent directory structure and disk space requirements for OneAgent installation on Linux.") contains globally writable directories (`1777` permissions). Changing these permissions by users is not supported.

### OneAgent injection mechanism

Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.

Similarly, certain log files require global write permissions (`666`) to allow applications running under various users to write to them.

### System security

We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.

* We keep the number of globally writable directories as limited as possible.
* All these directories have a sticky bit set (actual permissions are `1777`). Only the file's owner, the directory's owner, or the root user can modify the files in the directory. This is standard practice that makes the permissions more robust. It's also used for the Linux `/tmp` directory to prevent ordinary users from deleting or moving other users' files.