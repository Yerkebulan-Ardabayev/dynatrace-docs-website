---
title: Custom log source
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-custom-log-source
scraped: 2026-02-17T04:53:35.576938
---

# Custom log source

# Custom log source

* Latest Dynatrace
* Tutorial
* 6-min read
* Updated on Jul 07, 2025

Custom log source configuration enables you to manually add log sources that have not been autodetected. If you want to ingest them, you still need to configure it using the [log ingest configuration](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.") The use cases when you need to use custom log sources include:

* Autodiscovery might not identify a log source if a log file is not kept open for writing during a process.
* It might also fail to find log sources that are not part of any processes or are part of short-lived processes.

The entire process consists of two parts:

1. Source definition (custom log source configuration), which is described on this page.
2. Log acquisition (adding logs to storage), which is described on [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.").

If you need to store your custom logs, you need to complete both steps.

Each custom log source path you add needs to be validated by OneAgent and abide by its security rules. See [Security rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-security-rules "Configure security rules for custom log sources to ensure data protection.") for configuration files and examples.

### Hosts

To configure custom log sources at the host level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your host.
2. Select **More** (**â¦**) > **Settings** to open the **Host settings** page (available only on hosts assigned to a host group).
3. On the **Host settings** page, select **Log Monitoring** > **Custom log sources**.

### Host groups

To configure custom log sources at the host group level

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your host.
2. Expand the **Properties and tags** section and select the **Host group** (available only on hosts assigned to a host group).
3. On the **Host group settings** page, select **Log Monitoring** > **Custom log sources**.

### Environment

To configure custom log sources at the environment level

1. Go to **Settings**.
2. Select **Log Monitoring** > **Custom log sources**.

## Configure custom log source

1. Go to the **Custom log sources** page at the host, host group, or environment level as described above.
2. Select **Add custom log source** and add **Rule name**.
3. Optional Bind your rule to a process group by selecting the process group name from the dropdown menu.

Any rules assigned to process groups that are not present on a given host will be ignored for that host.

4. In the **Custom log source paths** section, select **Log source type**. There are two source types available:

   * **Log path**
   * **Windows Event Log**
5. Select **Allow binary content** to enable ingesting content from files containing binary data. Non-text data will be escaped. This is useful in cases when a file consisting mostly of text log records also contains some binary data.
6. Optional Select the encoding method of the monitored file from the **Encoding** drop-down.

Sometimes OneAgent can't detect the monitored file's encoding method. This may be due to the lack of a BOM marker that defines the encoding method or the use of a specific encoding for diacritical characters. Currently supported encodings are UTF-8, UTF-16 Little and Big Endian, Shift\_JIS, EUC\_JP (Japanese language), and EUC\_KR (Korean language).

7. Define a full path to the log file by selecting **Add custom log source path**, enter your complete path (for example, `/var/lib/*.log` or `/var/log/sys.bin`), and select **Add Path**. You can add up to 100 log paths per a single custom log source rule. You can provide custom Windows event logs.
   When configuring a custom log source, follow these rules:

   If you selected Windows Event Log, add the Full Name.

   As in the following example, you can display the log name by right-clicking on the chosen event log and selecting **Properties**:

   ![Windows event viewer properties screen.](https://dt-cdn.net/images/windows-event-viewer-properties1-547-41612bfc3c.png)

   ![Windows viewer log properties.](https://dt-cdn.net/images/windows-event-viewer-properties2-1261-03ad4741e4.png)
8. Optional Select **Show advanced** to expand the panel that lets you define the list of attributes which will enrich each log record from the defined log sources. Enter the attribute key or select it from the list, and then enter the attribute value. This is available only if you have selected the **Log source type** as Log Path.

   Enrich the logs with custom attributes.

   When using wildcards in the log path, you may want to distinguish the paths matched by the wildcards. In such cases, you can define attributes that use the whole file path or a part of the path matched by the wildcards.

   To define such an attribute, follow the steps below:

   1. Enter the key or select it from the list.
   2. In the Attribute value field, use the `${N}` token, where `N` denotes the index of the wildcard you refer to, starting from 1. `${0}` has a special meaning and expands to the full log file path.

   You can use multiple `${N}` tokens in a single attribute and combine them with other characters. For example, `worker:${1}-${2}`.

   If the `${N}` token refers to a wildcard index higher than the number of wildcards in the log path, it won't be replaced, and `${N}` will remain in the attribute value. The attribute key must contain only Latin alphanumeric characters (upper or lower case), dots (`.`), underscores (`_`), hyphens (`-`), or colons (`:`). It must not start with the `dt.` prefix and must not be any of the following:

   ```
   process.technology, log.source, log.content, timestamp, container.name, winlog.level, winlog.eventid, winlog.provider, winlog.opcode, winlog.task, winlog.keywords, winlog.username, k8s.namespace.name, k8s.container.name, k8s.deployment.name
   ```
9. Select **Save changes**.
10. Turn on the **Active** toggle to activate your rule.

## Log file permissions requirements

In order for OneAgent to ingest a log file, it needs read permissions for that file.

How you grant these permissions depends on the OS where OneAgent is deployed.

OneAgent supports three operating systems:

* Linux
* Windows
* AIX

At a glance, when you need to actively grant permissions:

| Drives | Linux | Windows | AIX |
| --- | --- | --- | --- |
| Local drives | No action required | Action might be required | No action required |
| Remote drives | Action might be required | Action might be required | No action required |

### Linux

* Log files on local drives: no action needed.
  By default, OneAgent has the appropriate [Linux capabilitiesï»¿](https://man7.org/linux/man-pages/man7/capabilities.7.html) to read these files.
* Log files on a remote drive: you need to grant the following permissions for the account that OneAgent operates on (by default, this account is `dtuser`):

  + Read and execute `(r+x)` permissions for each directory in the log file path.
  + Read `(r)` for the log file itself - for the account OneAgent operates on, which is `dtuser` on default settings.

    Log files on remote drive

    The lack of permissions rights is one of the most typical root causes for the lack of log ingestion for remote drives on Linux.

    If you have access to the monitored host, you can quickly check if the lack of permission rights is the issue.
    Do this by executing the `sudo âu dtuser cat /path/to/file.log` command, with the proper full path, of course, assuming `dtuser` is the account the OneAgent works on.

### Windows

OneAgent operates on the `LocalSystem` account.

The following permissions are typically granted automatically for log files on local drives:

* Read permission for each log file.
* Read and execute permissions for directories in the path, for this account.

For remote drives, it might not be set. You need to check if they're set and grant the permissions.
For more information, see [https://www.ntfs.com/ntfs-permissions-setting.htmï»¿](https://www.ntfs.com/ntfs-permissions-setting.htm).

OneAgent cannot access files that require authorization via additional UI dialogs, for example a Windows Explorer pop-up.

### AIX

By default, OneAgent has the appropriate root permissions to read these files.

### Configuration limits

You can add a maximum of 1000 custom log source rules per scope, with a maximum of 100 paths for each.

## Log file matching

When configuring a custom log source, follow these rules:

* Custom log paths must be absolute; relative paths are rejected. An absolute path has the following pattern:

  + For Windows: `any letter:\`
  + For Linux: Starts with `/`
  + For NFS: Starts with `//hostname/`
* A Windows Event Log path in Windows Event System must be a relative path.
* Custom log sources can contain wildcards: `#` replaces a string of numbers, while `*` substitutes a string of any characters except for slash (`/`) or backslash (`\`). While `*` can be used both in file names and directories, `#` can be used only in file names.

There is no need to use a sequence of wildcard characters instead of a single one. For example:

* You can replace `/path/to/test###.log` with `/path/to/test#.log`
* You can replace `/path/to/test#*.log` with `/path/to/test*.log`
* You can replace `/path/to/test#-#-#-#.log` with `/path/to/test*.log`, unless you want to enrich the logs with custom attributes using the numbers separated by dashes individually.

Using wildcards in directories can hinder OneAgent performance.

If you selected Windows Event Log, add the Full Name.

As in the following example, you can display the log name by right-clicking on the chosen event log and selecting **Properties**:

![Windows event viewer properties screen.](https://dt-cdn.net/images/windows-event-viewer-properties1-547-41612bfc3c.png)

![Windows viewer log properties.](https://dt-cdn.net/images/windows-event-viewer-properties2-1261-03ad4741e4.png)

11. Optional Select **Show advanced** to expand the panel that lets you define the list of attributes which will enrich each log record from the defined log sources. Enter the attribute key or select it from the list, and then enter the attribute value. This is available only if you have selected the **Log source type** as Log Path.

Enrich the logs with custom attributes.

When using wildcards in the log path, you may want to distinguish the paths matched by the wildcards. In such cases, you can define attributes that use the whole file path or a part of the path matched by the wildcards.

To define such an attribute, follow the steps below:

1. Enter the key or select it from the list.
2. In the Attribute value field, use the `${N}` token, where `N` denotes the index of the wildcard you refer to, starting from 1. `${0}` has a special meaning and expands to the full log file path.

You can use multiple `${N}` tokens in a single attribute and combine them with other characters. For example, `worker:${1}-${2}`.

If the `${N}` token refers to a wildcard index higher than the number of wildcards in the log path, it won't be replaced, and `${N}` will remain in the attribute value. The attribute key must contain only Latin alphanumeric characters (upper or lower case), dots (`.`), underscores (`_`), hyphens (`-`), or colons (`:`). It must not start with the `dt.` prefix and must not be any of the following:

```
process.technology, log.source, log.content, timestamp, container.name, winlog.level, winlog.eventid, winlog.provider, winlog.opcode, winlog.task, winlog.keywords, winlog.username, k8s.namespace.name, k8s.container.name, k8s.deployment.name
```

9. Select **Save changes**.
10. Turn on the **Active** toggle to activate your rule.

## Supported scopes

Three hierarchy scopes are supported: host, host group, and environment. The narrower a given scope, the higher its priority.

* Log source rules configured for a host take precedence over log source rules configured for a host group.
* Log source rules configured for a host group take precedence over log source rules configured for a Dynatrace environment.