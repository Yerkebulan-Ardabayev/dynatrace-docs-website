---
title: OneAgent file aging mechanism
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism
scraped: 2026-02-24T21:33:36.930749
---

# OneAgent file aging mechanism

# OneAgent file aging mechanism

* Latest Dynatrace
* 6-min read
* Updated on Feb 19, 2026

OneAgent in the installer-based deployment uses a built-in aging mechanism that makes sure the OneAgent files are kept within a reasonable size.

Aging mechanism is not used in the application-only mode.

Optimal OneAgent disk usage is determined based on the following limits:

* The minimum required space is 200 MB \* 3 = 600 MB (logs, alerts, crash reports).
* The default required space is 1 GB \* 3 = 3 GB (logs, alerts, crash reports).

The two type of files that contribute most to OneAgent disk space usage during its operation are OneAgent log files and runtime data such as crash and memory dumps.

## Log files

The maximum disk space occupied by OneAgent log files is very well managed by the OneAgent aging mechanism. Logs grow in size slowly and steadily. A continuous cleanup process that runs every minute keeps the log size within reasonable constraints. We designed the log aging mechanism with inside knowledge on how OneAgent-related events are logged, so log file aging doesn't require additional configuration.

## Runtime data

Unlike log files, large runtime data files such as crash and memory dumps are generated ad hoc and can cause rapid spikes in disk usage. To mitigate this, use the `DATA_STORAGE` installation parameter to specify a custom directory for large runtime data. Locate the custom directory on a resource where tight disk size constraints are not as critical as they are on the disk where OneAgent is installed.

For more information on customizing OneAgent installation, see the OS-specific help: [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters."), [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows/installation/customize-oneagent-installation-on-windows#data-storage "Learn how to use the OneAgent installer for Windows."), or [AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/customize-oneagent-installation-on-aix#data-storage "Learn how you can use AIX installer with command line parameters.").

## Emergency cleanup

In an emergency situation, when free disk space reaches `3%` threshold, OneAgent cleans all the files from directories managed by the aging mechanism except the latest installer logs and OneAgent OS module log

## OneAgent aging mechanism rules

The OneAgent aging mechanism ensures that the disk space used by OneAgent is constantly within predefined limits. To do that, a number of rules are applied to OneAgent directories. If necessary, you can contact a Dynatrace product expert via live chat to modify some of the aging rules.

### Log directory

* Linux/AIX `/var/log/dynatrace/oneagent`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\log`

The file aging mechanism checks the files and subdirectories in the main log directory and removes the oldest files when:

* The total directory size is above 1 GB
* Any file in this directory is older than 14 days

Files are removed from any subdirectory that contains more than 1000 files (newest files are preserved; oldest files are removed).

There are additional rules for subdirectories:

* `{log-dir}/process`  
  Files are removed when any of these conditions are true:

  + The files in this directory use more than 300 MB in total
  + Any file in this directory is older than 14 days
* `{log-dir}/installer`  
  Files are removed when any of these conditions are true:

  + The files in this directory use more than 30 MB in total
  + Any file in this directory is older than 180 days
    On Windows, the `driver.log` file is preserved.
* `{log-dir}/dumpproc`  
  Files are removed when any of these conditions are true:

  + The files in this directory use more than 100 MB in total
  + Any file in this directory is older than 14 days

### Data storage directory

* Linux/AIX `/var/lib/dynatrace/oneagent/datastorage`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\datastorage`
* `{data_storage_dir}/supportalerts`  
  Files are removed when any of these conditions are true:

  + This directory contains more than 10 files
  + The files in this directory use more than 1 GB in total
  + Any of the files in this directory is older than 7 days
* `{data_storage_dir}/memorydump`  
  Files are removed when any of these conditions are true:

  + Any of the files in this directory is older than 2 hours
  + The files in this directory use more than 20 GB in total
* `{data_storage_dir}/crashreports`  
  Files are removed when any of these conditions are true:

  + They have already been reported to Dynatrace
  + This directory contains more than 100 files
  + The files in this directory use more than 1 GB in total
  + Any of the files in this directory is older than 3 days

### Runtime directory

* Linux/AIX `/var/lib/dynatrace/oneagent/agent/runtime`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\agent\runtime`

The OneAgent file aging mechanism checks the subdirectories starting with `0x`. Checks are performed recursively.

* If the `0x*` directory contains a dump subdirectory and all the files in it are older than 3 days, then the dump subdirectory is removed.
* If all the files and directories in the `0x*` directory are older than 7 days, the whole directory is removed.
* This directory is also fully cleaned up during OneAgent update.

### Installation bin directory

* Linux/AIX `/opt/dynatrace/oneagent/bin`
* Windows `%PROGRAMFILES%\dynatrace\oneagent\bin`
* `{install-dir}/bin`  
  OneAgent deploys a number of file artifacts during the update process, specifically in cases of injectable technology modules. All injectable module files are stored in versioned folders. When OneAgent is active, it performs file cleanup according to the following criteria:

  + The currently used version is always preserved.
  + OneAgent scans all the monitored processes and determines which libraries are used.
  + The library list is compared to the contents of the bin directory. Unused binaries from the 32-bit and 64-bit directories are removed, regardless of whether Host monitoring is enabled or disabled. For binaries in the `any` directory, cleanup occurs only if Host monitoring is enabled. The OneAgent aging mechanism retains the current version and the 10 most recent previous versions, keeping a total of 11 versions.

## Aging mechanism for OneAgent in application-only monitoring mode

If you don't have access to the infrastructure layer, Dynatrace also provides the option of application-only monitoring for [Kubernetes](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), [OpenShift](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes"), [CloudFoundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.") or [SAP Business Technology Platform](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Install OneAgent on SAP Business Technology Platform.").

The aging mechanism in application-only monitoring mode manages the logs of the OneAgent modules. All of them are located in the respective subdirectories of the default OneAgent log directory:

* Linux/AIX `/var/log/dynatrace/oneagent`
* Windows `%PROGRAMDATA%\dynatrace\oneagent\log`

### Log rotation

Each OneAgent module limits its number of logs to 5. Each of these 5 files is limited to 10 MB.

### Log aging

OneAgent purges the log files at startup when:

* A log file is older than 14 days
* The combined size of all log files exceeds 300 MB
* There are more than 1,000 log files

To prevent unnecessary delays in your application's startup, the OneAgent bulk purge limit is set to delete a maximum of 50 of the oldest files.