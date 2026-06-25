---
title: Add log files manually (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2
scraped: 2026-05-12T11:13:15.972124
---

# Add log files manually (Logs Classic)

# Add log files manually (Logs Classic)

* 7-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Starting with OneAgent version 1.251 and Dynatrace Cluster version 1.254, we strongly encourage you to switch to [Custom log source configuration](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-custom-source "Configure custom log sources that have not been autodetected."), which has many [advantages](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/log-custom-source#clscadvantages "Configure custom log sources that have not been autodetected.") over manual log file addition.

Dynatrace allows you to add specific log files manually in instances where the files aren't discovered automatically. You only need to add one log path at the process-group level to cover all processes within the group across all monitored hosts.

### Adding log file to process group

To manually add a log file to a process group

1. In Dynatrace, go to **Technologies & Processes** and select a process group.
2. From the process group page, select the process instance for which you want to add a new log file.
3. In the **Log files** section of the page, select the **Configure more log files** link.  
   Alternatively, look for the **No log sources detected** section if no log files are associated with the process.
4. On the **Process group settings** page, select the **Log monitoring** tab.
5. Select **Add new log for monitoring**.
6. Type the file path of the log file to be associated with this process group. Only absolute paths are allowed.

   * Check out the requirements to the [logs paths](#considerations-for-adding-text-log-files-manually) to make sure they are supported.
   * Make sure you [enable monitoring](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 "Learn how to include and exclude log sources for analysis.") of the added log file(s).
7. Select **Save**.

### Windows event logs

Standard Windows event logs are already automatically detected, so you don't have to manually add the following:

* `Windows Security Log`
* `Windows Application Log`
* `Windows System Log`
* `IIS Event Logs`

To manually add a custom Windows event log file to a process

1. In Dynatrace, go to **Hosts**.
2. Select the host that contains the Windows event log file.
3. From the **Processes** section of the overview of the host page, select the process for which you want to add a new log file.  
   Optionally, go to **Technologies & Processes**, select a process group, and then, from the process group page, select the process instance for which you want to add a new log file.
4. In the **Log files** section, select **Add more**.
5. On the **Manually added process logs** page, select **Add new log for monitoring**
6. Provide the log name.  
   You can use the built-in Windows **Event Viewer** to find the custom log name. Make sure that you provide the full name as shown in the below example.

   Get the full name of a Windows event log.

   As in the following example, you can display the log name by right-clicking on the chosen event log and selecting **Properties**:

   ![Windows event viewer properties screen.](https://dt-cdn.net/images/windows-event-viewer-properties1-547-41612bfc3c.png)

   Windows event viewer properties screen.

   Copy the **Full Name**:

   ![Windows viewer log properties.](https://dt-cdn.net/images/windows-event-viewer-properties2-1261-03ad4741e4.png)

   Windows viewer log properties.
7. Select **Save**.

### Set up permissions on Network File System (NFS)

When handling logs on NFS, access permissions are strictly enforced. This is true despite the increased capabilities of OneAgent, which allow it to access local files without having to read permissions for the `dtuser` user.

To allow OneAgent to process and ingest NFS-mounted resources:

* Every non-local directory along the path needs to have at least the `read` and `execute` permissions set.
* Every log file needs to have the `read` permission set.

Example log file to add:

`/mnt/nfs/logs/app1/test.log`  
where `/mnt/nfs` is mounted to an external NFS resource.

In this scenario, both `/mnt/nfs/logs` and `/mnt/nfs/logs/app1` need `r-x`permissions for 'others', and every `test.log.*` file needs `r--` permissions for 'others' as shown below:

```
$ ls -l /mnt/nfs



drwxr-xr-x 3 1001 1002 4096 Sep 8 17:11 logs
```

```
$ ls -l /mnt/nfs/log



drwxr-xr-x 3 1001 1002 4096 Sep 8 17:11 app1
```

```
$ ls -l /mnt/nfs/logs/app1



-rw-rw-r-- 3 1001 1002 100 Jul 19 14:22 test.log



-rw-rw-r-- 3 1001 1002 100 Jul 19 14:23 test.log.1



-rw-rw-r-- 3 1001 1002 100 Jul 19 14:24 test.log.2
```

### Considerations for adding text log files manually

Dynatrace supports log files that were updated (written to) in the last 7 days **AND** contain a full path name **AND** meet **at least one of the additional criteria**:

* Files are located in a directory called `log` or `logs` (up to 2 levels) or `/var/log/`.  
  **OK (level 1):**  
  `c:\...\logs\custom.txt`  
  `c:\...\log\custom.txt`

  **OK (level 2):**  
  `c:\...\logs\app1\custom.txt`  
  `c:\...\log\app2\custom.txt`

  **NOT OK (level 3 and above):**  
  `c:\...\logs\app1\app11\custom.txt`  
  `c:\...\log\app2\app22\custom.txt`
* Custom log path must specify files, not a directory:  
  **NOT OK:**  
  `/var/log/customdir/`
* Files have the extension `.log`, `-log`, `_log` (for example, `apache.log`, `apache.myapp-log`, `apache.myapp_log`)
* Every file that has other extension, such as `.txt`, is supported if its names contains the `.log`, `-log`, or `_log` prefix that is preceded by at least one character or symbol (for example, `apache.log.txt`, `apache-log.txt`, or `apache_log.txt`)

  The `log.txt` alone file is not accepted (unless placed in the `log` or `logs` directory).
* File name is `catalina.out`

Only file names that contain a full path are correct. Therefore, `AlertServiceLog.log` is rejected despite meeting other criteria, but `c:\customdir\AlertServiceLog.log` is accepted.

Additionally:

* Custom log paths files can start or end with a wildcard ( \* ).
  **OK:**  
  `/var/log/customdir/*`  
  `/var/log/customdir/file*`  
  `/var/log/customdir/*.log`
* You can add a group of logs (a fileset) by using the asterisk character (**\***) within the file name.  
  For example, `/var/log/error-*.log` will match `error-1.log`, `error-some-ID.log`, etc., and report the fileset as a single `error-*.log`  file.

Custom log paths

Make sure the log files are added to log storage after you configure custom log paths. See [Log sources and storage (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 "Learn how to include and exclude log sources for analysis.")

Example:  
If you have a file named `AlertServiceLog.txt`, the above scenarios apply as shown in the table:

| File | Accepted? | Reason |
| --- | --- | --- |
| AlertServiceLog.txt | NOT OK | Does not contain a full path. |
| c:\customdir\AlertServiceLog.txt | NOT OK | Contains a full path, but no additional requirement met. |
| c:â¦\log\AlertServiceLog.txt | OK | 1st level requirement met. |
| c:â¦\log\app2\AlertServiceLog.txt | OK | 2nd level requirement met. |
| c:â¦\log\app2\app22\AlertServiceLog.txt | NOT OK | level > 2 |
| c:\customdir\file.log | OK | `.log` extension |
| c:\customdir\file-log | OK | `-log` extension |
| /var/log/customdir/AlertServiceLog\_log\* | OK | Wild card is accepted (if at least one additional criterion is met, here: `_log` extension). |
| c:\customdir\AlertServiceLog.log.txt | OK | .log present in a file with `.txt` extension |
| c:\customdir\AlertServiceLog\_log.txt | OK | \_log present in a file with `.txt` extension |
| c:\customdir\AlertServiceLog-log.txt | OK | -log present in a file with `.txt` extension |

### Additionally:

* Only absolute file paths are supported:

  + **Unix:** Path must begin with `/`.  
    Paths within the following folders are not supported:

  ```
  etc



  boot



  proc



  dev



  bin



  sbin



  lib



  usr



  .ssh
  ```

  + **Windows:** Path must begin with drive letter (for example, `C:\` ).  
    Paths within the following folders are not supported:

  ```
  windows



  winnt
  ```
* Manually added log files affect all processes on all hosts belonging to the configured process group.
* To add log files located in a container:

1. Configure the container so that the log file within the container is written to a disk.
2. Point the OneAgent to this location by defining the absolute path to where the container is to write the log files.

* You can add numbered rotating-log filesets by using the hash character (**#**).  
  For example, `/var/log/error-#.log` will match `error-1.log`, `error-2.log`, etc., and report the fileset as a single `error-#.log` file.
* You can globally disable the option to configure custom log files by setting:  
  `AppLogRemoteConfiguration = false`

  **On Linux**:  
  `/var/lib/dynatrace/oneagent/agent/config/ruxitagentloganalytics.conf`

  **On Windows**:  
  `%PROGRAMDATA%\dynatrace\oneagent\agent\config\ruxitagentloganalytics.conf`

Use template

If your OneAgent installation, freshly installed or upgraded, does not have the `ruxitagentloganalytics.conf` file, use `ruxitagentloganalytics.conf.template` as a template and create your own `ruxitagentloganalytics.conf` file. Next, copy the `ruxitagentloganalytics.conf` file to the following directory:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\`