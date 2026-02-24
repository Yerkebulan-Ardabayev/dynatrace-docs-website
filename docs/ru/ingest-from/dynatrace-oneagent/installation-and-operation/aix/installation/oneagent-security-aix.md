---
title: OneAgent security on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/oneagent-security-aix
scraped: 2026-02-24T21:25:40.312725
---

# OneAgent security on AIX

# OneAgent security on AIX

* Latest Dynatrace
* Reference
* 3-min read
* Published Nov 12, 2020

To fully automate the monitoring of your operating systems, processes, and network interfaces, Dynatrace requires privileged access to your operating system during both installation and operation.

OneAgent is tested extensively to ensure that it has minimal performance impact on your system and [conforms to the highest security standards](/docs/manage/data-privacy-and-security "Learn how Dynatrace applies various security measures required to protect private data.").

## Permissions

### Installation

OneAgent installer requires admin privileges to:

* Add an entry for OneAgent to `/etc/rc.shutdown`
* Register OneAgent service in the system's init via the `mkitab` command

### Operation

The OneAgent requires admin privileges to:

* Access the list of open sockets for each process.
* Access the list of libraries loaded for each process.
* Access the name and path of the executable file for each process.
* Access command line parameters for each process.
* Monitor network traffic.
* Read application configuration files.
* Load `oneagentkmod`  kernel extension to enable automatic injection into processes

## Operating system changes

* The `oneagentkmod` kernel extension is loaded upon OneAgent service startup.

## Files modified

* `/etc/rc.shutdown` and `/etc/inittab` have an entry added for `oneagent` service.

## Files added

### Installation

The OneAgents installer adds the following files to your system:

* OneAgent binaries and configuration files are saved in `/opt/dynatrace/oneagent`. Note that you can change the location using [INSTALL\_PATH](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#installation-path "Learn how you can use AIX installer with command line parameters.") parameter.

### Operation

OneAgent adds the following files to your system:

* OneAgent temporary files and runtime configuration are saved in `/var/lib/dynatrace/oneagent/runtime`.
* OneAgent persistent configuration is saved in `/var/lib/dynatrace/oneagent/config`.
* Large runtime data, such as memory dumps, is saved in `/var/lib/dynatrace/oneagent/datastorage`. Note that you can change the location of large runtime data using the [DATA\_STORAGE](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#data-storage "Learn how you can use AIX installer with command line parameters.") parameter.

## System logs downloaded by OneAgent

OneAgent downloads certain system logs so that Dynatrace can diagnose issues that may be caused by conditions in your environment. Most often such issues are related to deep monitoring or installations run as automatic updates.
System logs downloaded by OneAgent on AIX are:

* `/etc/security/limits`
* `/var/adm/ras/errlog`
* `/var/log/kern`
* `/var/log/syslog`

Revoking access to system logs

To revoke access to system logs, use the `oneagentctl` command with the `--set-system-logs-access-enabled` parameter set to `false`.  
For more information, see [OneAgent configuration via command-line interface](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.")

## Globally writable directories

The OneAgent directory structure contains globally writable directories (`1777` permissions). Changing these permissions by users is not supported.

### OneAgent injection mechanism

Such permissions on the selected set of directories are necessary for successful OneAgent injection into the processes on the monitored hosts. When OneAgent injects into a process, the code module responsible for injection runs in the context of the original injected process. Consequently, the users under which these processes are run need to be permitted to write into the OneAgent directory structure, which is the reason for the global write permissions that allow that.

Similarly, certain log files require global write permissions (`666`) to allow applications running under various users to write to them.

### System security

We're aware that global read and write permissions on OneAgent directories get flagged by security scan heuristics, but we can assure you that they're fully secure.

* We keep the number of globally writable directories as limited as possible.
* All these directories have a sticky bit set (actual permissions are `1777`). Only the file's owner, the directory's owner, or the root user can modify the files in the directory. This is standard practice that makes the permissions more robust. It's also used for the `/tmp` directory to prevent ordinary users from deleting or moving other users' files.