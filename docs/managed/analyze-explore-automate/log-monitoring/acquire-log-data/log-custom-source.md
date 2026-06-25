---
title: Custom log source (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-custom-source
scraped: 2026-05-12T12:00:15.173962
---

# Custom log source (Logs Classic)

# Custom log source (Logs Classic)

* Tutorial
* 14-min read
* Updated on Nov 19, 2024

Log Monitoring Classic

OneAgent version 1.251+ Dynatrace Cluster version 1.254+

In OneAgent version 1.249 and earlier, you need to [add log files manually](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Learn how to manually add log files for analysis.").

Custom log source configuration enables you to manually add log sources that have not been autodetected.

* Autodiscovery might not identify a log source if a log file is not kept open for writing during a process.
* It might also fail to find log sources that are not part of any processes or are part of short-lived processes.

In such cases, you can define, configure, and customize log sources to your needs.

* Starting from OneAgent version 1.251, you can switch to the improved version of manual addition, which is the custom log source configuration. You can opt-in by selecting a banner on the [Custom log source configuration page](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-custom-source#mainclscuipage "Configure custom log sources that have not been autodetected.").

The entire process consists of two parts:

1. Source definition (custom log source configuration), which is described on this page.
2. Log acquisition (adding logs to storage), which is described on [Log ingest rules](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.").

If you need to store your custom logs, you need to complete both steps.

## Advantages of custom log source configuration

Compared to the log addition in earlier versions of OneAgent versions, the process now has several improvements.

Custom log source configuration enables you to:

* Define log sources without the process group context (adding a process group is optional). You can add up to three process groups to a log source.
* Define rules within all three scopes (host, host group, environment).
* Change security rules through files placed on the host.
* Add a rule with multiple paths within one process group.
* Use wildcards in directories.
* Use a dedicated API.

Automatically migrate your legacy custom log source configuration: each of your existing rules is migrated to the environment scope with the corresponding process group context set accordingly. The names of migrated rules have the `auto-migrated` prefix.

## Supported scopes

Three hierarchy scopes are supported: host, host group, and environment. The narrower a given scope, the higher its priority.

* Log source rules configured for a host take precedence over log source rules configured for a host group.
* Log source rules configured for a host group take precedence over log source rules configured for a Dynatrace environment.

### Hosts

To configure custom log sources at the host level

1. Go to **Hosts**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. From the host settings, go to **Log Monitoring** > **Custom log sources**.

### Host groups

To configure custom log sources at the host group level

1. Go to **Hosts** and select the host that interests you.
2. On the host overview page, select **Properties and tags**.
3. On the **Properties and tags** panel, find the **Host group** property to see the name of the host group to which the selected host belongs.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name to list all hosts in that host group. This displays the **OneAgent deployment** page filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.
5. Select the host group name in any row.

6. In the host group settings, select **Log Monitoring** > **Custom log sources**

### Environment

To configure custom log sources at the environment level

1. Go to **Settings** > **Log Monitoring** > **Custom log sources**.

## Configure log source

1. Go to the **Custom log sources** page at the host, host group, or environment level as described above.
2. Select **Add custom log source** and add **Rule name**.
3. Optional Bind your rule to a process group by selecting the process group name from the dropdown menu.

Any rules assigned to process groups that are not present on a given host will be ignored for that host.

4. In the **Custom log source paths** section, select **Log source type**. There are two source types available:

   * **Log path**
   * **Windows Event Log**
     Each rule is applied to one log source type. You can select either **Log path** or **Windows Event Log**.
5. To define a full path to the log file, select **Add custom log source path**, enter your complete path (for example, `/var/lib/*.log` or `/var/log/sys.bin`), and select **Add Path**. You can add up to 100 values per log source. If you selected **Windows Event Log**, refer to [Windows event example](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2#Windoweventlog "Learn how to manually add log files for analysis.") to add a proper log path.

Sometimes, OneAgent can't detect the monitored file's encoding method. This may be due to the lack of a BOM marker that defines the encoding method or the use of a specific encoding for diacritical characters. Currently supported encodings are UTF-8, UTF-16 Little and Big Endian, Shift\_JIS, EUC\_JP (Japanese language), and EUC\_KR (Korean language).

6. Optional Select **Show advanced** to expand the panel that lets you define the list of attributes which will enrich each log record from the defined log sources. Enter the attribute key or select it from the list, and then enter the attribute value. This is available only if you have selected the **Log source type** as Log Path.

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

   You can define up to 100 attributes per log path. The minimum required version is OneAgent version 1.285.
7. Select **Save changes**.
8. To activate your rule, turn on the **Active** toggle.

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

## Log file matching

When configuring a custom log source, follow these rules:

* Custom log paths must be absolute; relative paths are rejected. An absolute path has the following pattern:

  + For Windows: `any letter:\`
  + For Linux: Starts with `/`
  + For NFS: Starts with `//hostname/`
* A Windows Event Log path in Windows Event System must be a relative path.
* Custom log sources can contain wildcards:

  + `#` replaces a string of numbers or a hash `#`. It can only be used in file names.
  + `*` substitutes a string of any characters including the asterisk `*`. It does not substitute the slash (`/`) or backslash (`\`). `*` can be used both in file names and directories.

Additionally, each custom log source path you add needs to be validated by OneAgent and abide by its security rules (file matching rules). The following security rules are applied on the OneAgent side:

## Security rules

Dynatrace defines security rules for custom log sources. These rules manage OneAgent access to log sources, which defends against unauthorized access and data misuse. You can add or override these predefined security rules in the configuration file on the host where OneAgent is installed, allowing flexibility in adapting to specific security needs.

The rules prohibit log paths in critical system directories (such as `/etc`, `/boot`, `/proc`, and several others), paths containing `.ssh`, paths with the `.pem` extension, and paths in directories starting with a dot (indicating hidden directories). Additionally, acceptable log paths must either have a log extension, with certain separators, be located within the first or second level of a `log` or `logs` directory, be situated at any level of the `/var/log` directory, or have the filename `catalina.out`.

The rules take into account the resolved paths of symbolic links for security matching, emphasizing the importance of the actual file location over the symlink path.

* A log path is not in any of the following: `/etc`, `/boot`, `/proc`, `/dev`, `/bin`, `/sbin`, `/usr`, `WindowsRoot:\windows`, or `WindowsRoot:\winnt`. However, `Windows|winnt\system32\winevt\Logs` is accepted AND
* A log path does not contain `.ssh` AND
* A log path does not have the `.pem` extension AND
* A log path is not located in a directory whose name starts with `.` (for example, `/.hidden`) AND
* A log path must have the `log` extension separated by `.`, `-`, or `_` (it can be followed by another extension with the same separator set) OR

  + A log path must be located on the first or second level of the `log` or `logs` directory OR
  + A log path must be located on any level of the `/var/log directory` OR
  + A log path must have the file name `catalina.out`.

Files with paths that do not fulfill one or more criteria are not accepted.
Once the conditions above are met, log file matching takes place. Check the [log file matching](#log-file-matching) rules.

If the log file you've configured for ingestion is a symlink, Dynatrace will verify its log path (the path obtained after following the symlink) against security rules.

### Override security rules

You can add or override predefined security rules only in the configuration file on the host where OneAgent is installed.

* Save your changes as a separate file placed in the OneAgent persistent configuration directory.

  + `/var/lib/dynatrace/oneagent/agent/config/logmodule` on Linux and UNIX
  + `%PROGRAMDATA%\dynatrace\oneagent\agent\config\logmodule` on Windows

    Any log file with the `.json` suffix is allowed in the above directories.
* Do not edit the file that contains predefined rules:

  + `/opt/dynatrace/oneagent/agent/conf` on Linux and UNIX
  + `%PROGRAMFILES%\dynatrace\oneagent\agent\conf` on Windows
* Rules defined by you under the custom configuration take precedence over the default rules. Additionally, the first matching rule determines whether a path passes the security test. The override configuration file (the one that you save in the persistent configuration directory) format needs to be the same as the format for a file with predefined rules.

### Override configuration file

* There is a predefined directory pattern that is executed from right to left. For example, `/log/` will match `/log/file` and `/var/log/file` but not `/log/dir/file`
* Only one directory is matched. For example, `/log/*/` will match `/log/dir/file` but not `/log/dir/dir2/file`
* The `[-.\\_]` expression in a pattern means that one of the characters provided in the square brackets must be present for a match to occur.

### Example override configuration file

The following structure is given in the file:

* `allowed-log-paths-configuration`: Marks the array of the rules.

Each rule consists of three key-value pairs, with the following mandatory keys:

* `directory-pattern`
* `file-pattern`
* `action`

The description of the keys is given below:

* `directory-pattern`: This object specifies the pattern for matching directories. The directory pattern is executed from right to left, for example: `/log/` will match `/log/file.txt` and `/var/log/file.txt` but not `/log/dir/file.txt`. The following rules apply:

  + A directory is matched by a wildcard `*`. For example, `/log/*/` will match `/log/dir/file.txt` but not `/log/dir/dir2/file.txt`.
  + `**` matches any number of subdirectories. For example, the pattern `/log/dir/**/file.txt` will match `/log/dir/dir1/dir2/dir3/file.txt`.
  + `^` matches the start of the path. It anchors the pattern to the beginning of the examined path For example, `^/usr/*/` matches paths starting with `/usr/`, such as `/usr/log/file.txt` and `/usr/local/file.txt`, but will not match `/some/usr/log/file.txt`.
    For Windows paths, the anchor can also skip the drive letter. For example, the pattern `^/Users/Public/` would match the actual path `C:\Users\Public\file.txt`. JSON treats \ as an escape character, so when specifying Windows paths, you can use either `C:\\Users\\Public` or `C:/Users/Public` but not `C:\Users\Public`.

  You can combine special characters such as `*`, `**`, and `^` within a single directory pattern to create more complex matching rules. For example, the pattern `^/log/**/dir/*/*/` will match the path `/log/some/deep/dir/and/deeper/file.txt`.
* `file-pattern`: This object specifies the pattern for matching files within the directories matched by the `directory pattern`. This pattern is applied using full match. This means that a pattern such as `*.txt` will match `error.txt` but not `error.txt.1`.
  To properly detect files that follow rotation patterns, the file pattern must include a wildcard at the end. For example, to match files that rotate from error.txt to error.txt.1, the file pattern should be constructed as `*.txt*`.
* `action`: This object specifies the action to be taken for the matched file. In this case, `EXCLUDE` or `INCLUDE`.

The `[-.\\_]` expression in square brackets means that one of the characters provided in the square brackets must be present for a match to occur.

An example override configuration file is given below:

```
{



"allowed-log-paths-configuration":[



{



"directory-pattern":"/",



"file-pattern":"*.pem",



"action":"EXCLUDE" // or INCLUDE



},



... your rules ...



]



}
```

## Examples of OneAgent security rules

Each custom log source path you add needs to be validated by OneAgent and abide by its security rules (file matching rules). Some predefined security rules are applied on the OneAgent side. Examples of exclude and include rules for UNIX, Linux, and Windows are listed in the table below.

| Operating system | Directory pattern | File pattern | Action |
| --- | --- | --- | --- |
| UNIX | `/` | `*.pem` | EXCLUDE |
| UNIX | `/` | `*[-.\\_]log[-.\\_]*` | INCLUDE |
| Linux | `/.ssh/` | \* | EXCLUDE |
| Linux | `/` | `*[-.\\_]log` | INCLUDE |
| Windows | `/.*/` | \* | EXCLUDE |
| Windows | `/windows/system32/winevt/Logs/` | \* | INCLUDE |

### Security rule lists for UNIX, Linux, and Windows

Security rules for UNIX

The full list of security rules for UNIX:

```
{



"allowed-log-paths-configuration": [



{



"directory-pattern":"/",



"file-pattern":"*.pem",



"action":"EXCLUDE"



},



{



"directory-pattern":"/.ssh/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/.*/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/",



"file-pattern":".*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/etc/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/boot/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/proc/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/dev/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/bin/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/sbin/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/usr/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern": "/",



"file-pattern": "*[-.\\_]log[-.\\_]*",



"action": "INCLUDE"



},



{



"directory-pattern": "/",



"file-pattern": "*[-.\\_]log",



"action": "INCLUDE"



},



{



"directory-pattern": "/",



"file-pattern": "catalina.out*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/*/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/*/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "^/var/lib/docker/containers/*/",



"file-pattern": "*.log",



"action": "INCLUDE"



},



{



"directory-pattern": "^/var/log/**/",



"file-pattern": "*",



"action": "INCLUDE"



}



]



}
```

Security rules for Linux

The full list of security rules for Linux:

```
{



"allowed-log-paths-configuration": [



{



"directory-pattern":"/",



"file-pattern":"*.pem",



"action":"EXCLUDE"



},



{



"directory-pattern":"/.ssh/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/.*/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/",



"file-pattern":".*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/etc/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/boot/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/proc/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/dev/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/bin/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/sbin/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/usr/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern": "/",



"file-pattern": "*[-.\\_]log[-.\\_]*",



"action": "INCLUDE"



},



{



"directory-pattern": "/",



"file-pattern": "*[-.\\_]log",



"action": "INCLUDE"



},



{



"directory-pattern": "/",



"file-pattern": "catalina.out*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/*/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/*/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "^/var/lib/docker/containers/*/",



"file-pattern": "*.log",



"action": "INCLUDE"



},



{



"directory-pattern": "^/var/log/**/",



"file-pattern": "*",



"action": "INCLUDE"



}



]



}
```

Security rules for Windows

The full list of security rules for Windows:

```
{



"allowed-log-paths-configuration":[



{



"directory-pattern":"/",



"file-pattern":"*.pem",



"action":"EXCLUDE"



},



{



"directory-pattern":"/.ssh/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/.*/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/",



"file-pattern":".*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/windows/system32/winevt/Logs/",



"file-pattern":"*",



"action":"INCLUDE"



},



{



"directory-pattern":"/winnt/system32/winevt/Logs/",



"file-pattern":"*",



"action":"INCLUDE"



},



{



"directory-pattern":"^/windows/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"^/winnt/**/",



"file-pattern":"*",



"action":"EXCLUDE"



},



{



"directory-pattern":"/",



"file-pattern":"*[-.\\_]log[-.\\_]*",



"action":"INCLUDE"



},



{



"directory-pattern":"/",



"file-pattern":"*[-.\\_]log",



"action":"INCLUDE"



},



{



"directory-pattern":"/",



"file-pattern":"catalina.out*",



"action":"INCLUDE"



},



{



"directory-pattern": "/log/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/log/*/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/*/",



"file-pattern": "*",



"action": "INCLUDE"



},



{



"directory-pattern": "/logs/*/*/",



"file-pattern": "*",



"action": "INCLUDE"



}



]



}
```