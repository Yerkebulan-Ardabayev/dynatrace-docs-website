---
title: ActiveGate diagnostics
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-activegate/activegate-diagnostics
scraped: 2026-02-19T21:31:37.949765
---

# ActiveGate diagnostics

# ActiveGate diagnostics

* Latest Dynatrace
* 9-min read
* Updated on Oct 20, 2025

You can run fully automated ActiveGate troubleshooting for Dynatrace SaaS and Managed environments.

The workflow enables you to:

* Automatically pinpoint an ActiveGate-related issue in highly dynamic environments, at a specific point in time
* Easily collect the diagnostic data for a specific entity, and automatically get potential solutions for detected anomalies
* Quickly resolve common issues on your own, reducing the amount of time spent on diagnosing
* Directly provide Dynatrace Support all the details they need to diagnose the issue

If ActiveGate can't connect to the Dynatrace environment or doesn't start, you might need to collect diagnostic data locally from the command line. For details, see [Collect diagnostic data with `agctl`](#collect-diagnostic-data-with-agctl).

## Requirements

* **View sensitive request data** environment permission
* For an ActiveGate configured for multi-environment support, you can run ActiveGate diagnostics only on the main environment, as defined in the [ActiveGate configuration](/docs/ingest-from/dynatrace-activegate/configuration/configure-an-environment-activegate-for-multi-environment-support "Read the step-by-step procedure for configuring a single Environment ActiveGate for multi-environment support.").

## Analyze automatically

This procedure describes the default procedure: Dynatrace collects diagnostics data for an ActiveGate and immediately analyzes it.

If you prefer to collect and review the data before manually submitting it to Dynatrace for analysis, see [Collect and review locally](#collect-and-review-locally).

1. Go to **Deployment Status** > **ActiveGates**.
2. Expand the ActiveGate entry you want to troubleshoot and select **Run ActiveGate diagnostics**.
3. On the **Run Dynatrace ActiveGate diagnostics** page, briefly describe what isnât working as expected from your point of view.
4. Optional By default, 7 days of data is collected for analysis. If you need more data, select the **Advanced options** link, change the number of days, and select **Apply**.
5. Select **Start analysis**.

### What happens next

Dynatrace does the following:

* Collects diagnostic data for the last 7 days (if you didn't change the default) of the affected ActiveGate
* Stores the collected diagnostic data
* Uploads the diagnostic data to an S3 bucket in the AWS region of your environment for further analysis

The **State** column describes the current phase of the process.

**State** does not automatically refresh. Select **Refresh** to check for a state change.

Collecting

Data collection is in progress.
While collecting data, you can:

* **Refresh** the page to update the progress.
* **Cancel** diagnostic data collection.

Collected

Dynatrace has finished collecting diagnostic data.
After collecting data, you can:

* **Analyze** to submit the collected data to Dynatrace for analysis.
* **Download** the collected data locally for your inspection.
* **Delete** the issue, including the collected diagnostic data.

Sending in progress

Diagnostic data is being transferred to Dynatrace for analysis.
While sending data, you can:

* **Refresh** the page to update the progress.
* **Download** the collected diagnostic data.
* **Delete** the issue, including the collected diagnostic data.

Sent to Dynatrace cloud

Diagnostic data has been transferred to Dynatrace for analysis.

Analyzing

Dynatrace is now analyzing the diagnostic data.  
While analyzing data, you can:

* **Refresh** the page to update the progress.
* **Download** the collected diagnostic data.
* **Delete** the issue, including the collected diagnostic data.

Analyzed

The analysis is done. The number of associated alerts is shown in parentheses.  
After an analysis, you can:

* **Download** the collected diagnostic data.
* **Delete** the issue, including the collected diagnostic data.

Delete in progress

The diagnostic data is being deleted. While deleting data, you can:

* **Refresh** the page to update the progress.

Deleted

The diagnostic data has been deleted. Dynatrace keeps only a small set of information about who, when, where, and why the diagnostic data was collected.

Canceled

The diagnostics process was canceled manually before it was finished.

### Review the Dynatrace analysis

When the analysis is complete, Dynatrace sends the results back to your environment. If a potential solution is identified, Dynatrace lists it in the **Alerts section.**

## Collect and review locally

This procedure describes how to collect diagnostics data for the ActiveGate. Use this option if you prefer to collect and review the data before manually submitting it to Dynatrace for analysis.

If you instead want to collect data and submit it to Dynatrace automatically for analysis, see [Analyze automatically](#analyze-automatically).

1. Go to **Deployment Status** > **ActiveGates**.
2. Expand the ActiveGate entry you want to troubleshoot and select **Run ActiveGate diagnostics**.
3. On the **Run Dynatrace ActiveGate diagnostics** page, briefly describe what isnât working as expected from your point of view.
4. Select the **Advanced options** link.
5. Select **and store locally**.

   * While you are here, you can also change the number of days of data to collect (default = `7 days`).
6. Select **Apply**.
7. Select **Start collection** to collect diagnostic data and store it locally.

### What happens next

Dynatrace now:

* Collects diagnostic data for the last 24 hours (if you didn't change the default) of the affected ActiveGate
* Stores the collected diagnostic data

The **State** column describes the current phase of the process.

**State** does not automatically refresh. Select **Refresh** to check for a state change.

Collecting

Data collection is in progress.
While collecting data, you can:

* **Refresh** the page to update the progress.
* **Cancel** diagnostic data collection.

Collected

Dynatrace has finished collecting diagnostic data.
After collecting data, you can:

* **Analyze** to submit the collected data to Dynatrace for analysis.
* **Download** the collected data locally for your inspection.
* **Delete** the issue, including the collected diagnostic data.

### What to do with the collected data

Now that the data is collected, you can:

* **Download** the collected data.

  + You can review the data. See [Contents of diagnostic data](#contents) for an overview of what's in the download.
  + You can add the data to your support ticket.
* **Analyze** the data.
* **Delete** the issue, including the collected diagnostic data.

### ActiveGate diagnostics in Dynatrace Managed air-gapped environments

In a Dynatrace Managed air-gapped environment:

1. Use the **Store locally** option under **Advanced options** as described above.
2. After diagnostic data is collected, you can add the data to your support ticket.
3. Dynatrace can then fetch the diagnostic data from your support ticket, analyze it, and provide automated feedback to Dynatrace Support about detected anomalies.

Stringent data privacy protections are enforced and logged throughout this process.

## Collect diagnostic data with `agctl`

ActiveGate version 1.275+

In cases where ActiveGate cannot connect to the Dynatrace environment or doesn't start, you might need to collect diagnostic data locally from the command line on the ActiveGate host. To do so, use the `agctl` command line tool to collect all the necessary data and create a package that can be analyzed later.

### Use `agctl` on Linux or Windows

Linux

Windows

#### Locations

* `agctl` is located in [ActiveGate install directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."). If you installed ActiveGate in a custom folder, the path to `agctl` will be different.
* The diagnostic package is written in the current working directory by default.

  + To change this, use the `--directory=<path>` parameter.
  + After the successful creation of a diagnostic data file, `agctl` prints the path to this file.

#### Permissions

* `agctl` must be run with [the same user as ActiveGate process](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#user-service "Learn about the command-line parameters that you can use with ActiveGate on Linux.") - by default `dtuserag`.
* Make sure that `dtuserag` has write permission for the target directory.

#### Data collected

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

#### Syntax

To collect diagnostic data, run the `agctl` script with the `create-support-archive` parameter and any optional parameters as described above.

```
sudo -u dtuserag /opt/dynatrace/gateway/agctl create-support-archive [--directory=<path> --days=<days> --modules=<modules-list>]
```

#### Locations

* `agctl.bat` is located in the [ActiveGate install directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems."). If you installed ActiveGate in a custom folder, the path to `agctl.bat` will be different.
* The diagnostic package is written in the current working directory by default.

  + To change this, use the `--directory=<path>` parameter.
  + After the successful creation of a diagnostic data file, the tool prints the path to this file.

#### Permissions

* `agctl.bat` must be run with [the same user as ActiveGate process](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate#user-service "Learn about the command-line parameters that you can use with ActiveGate on Linux.") or as administrator.

#### Data collected

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

#### Syntax

To collect diagnostic data, run the `agctl.bat` script with the `create-support-archive` parameter and any optional parameters as described above.

```
."C:\Program Files\dynatrace\gateway\agctl.bat" create-support-archive [--directory=<path> --days=<days> --modules=<modules-list>]
```

### Use `agctl` from containerized ActiveGate

ActiveGate version 1.325+

You can use `agctl` to gather diagnostic data from a containerized ActiveGate using the `--stdout` parameter, which outputs the support archive directly and allows you to redirect it to a file on your local machine.

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

Kubernetes

OpenShift

```
kubectl exec -n <namespace> <pod-name> -- /opt/dynatrace/gateway/agctl create-support-archive --stdout > ag-support-archive.zip
```

```
oc exec -n <namespace> <pod-name> [-c <container>] -- /opt/dynatrace/gateway/agctl create-support-archive --stdout > ag-support-archive.zip
```

The contents of the support archive are written to `stdout`, allowing them to be redirected to a zip file. Other output is sent to `stderr` to maintain the integrity of the archive file.

Windows PowerShell not supported

Make sure to use the command prompt (`cmd.exe`) on Windows; PowerShell currently isn't supported.

#### For ActiveGate versions before 1.325

ActiveGate version 1.275 to 1.325

For earlier versions of containerized ActiveGate, use `agctl` with the `--directory` parameter and then transfer the file using base64 encoding.

* 30 days of data is collected by default. To change this, use the `--days=<days>` parameter.
* Diagnostic data is collected from all modules by default. To change this, use the `--modules=<modules-list>` parameter with a comma-separated list of modules (for example, `--modules=zremote,synthetic`).

Kubernetes

OpenShift

1. Run the command.

   ```
   kubectl exec <pod-name> -n <namespace> -- /opt/dynatrace/gateway/agctl create-support-archive --directory=<tmp-path> [--days=<days> --modules=<modules-list>]
   ```
2. Move the created file to the host. Use base64 to create an encoded file.

   ```
   kubectl exec <pod-name> -n <namespace> -- base64 --wrap=0 <created-file-path> > <encoded-file-host-path>
   ```

1. Run the command.

   ```
   oc exec <pod-name> [-c <container>] -- /opt/dynatrace/gateway/agctl create-support-archive --directory=<tmp-path> [--days=<days> --modules=<modules-list>]
   ```
2. Move the created file to the host. Use base64 to create an encoded file.

   ```
   oc exec <pod-name> [-c <container>] -- base64 --wrap=0 <created-file-path> > <cenoded-file-host-path>
   ```

3. Decode the encoded file using the appropriate Windows or Linux command.

   Linux

   Windows

   ```
   base64 --decode -i <encoded-file-path> > <decoded-file-path>
   ```

   ```
   $base64Data = Get-Content <encoded-file-path>



   $zipBytes = [Convert]::FromBase64String($base64Data)



   Set-Content -Value $zipBytes -Encoding Byte -Path <decoded-file-path>
   ```

### What to do with the collected data

Now that the data is collected:

* You can review the data. See [Contents of diagnostic data](#contents) for an overview of what's in the download.
* You can add the data to your support ticket.

We recommend that you delete the file after use.

## Contents of diagnostic data

All the collected diagnostic data is compressed into a `SupportArchive<ID number>` (for `agctl` - `support_archive_<timestamp>`) ZIP file that includes the following folders and files:

Folder or file

Description

`details.txt` (file)

Contains general information on when and where the diagnostic data was collected and archive statistics.

`config` (folder)

Contains a snapshot of the ActiveGate [configuration directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

`debugui` (folder)

Contains a snapshot of the internal environment configuration related to the ActiveGate.

`log` (folder)

Contains a snapshot of the ActiveGate [log directory](/docs/ingest-from/dynatrace-activegate/configuration/where-can-i-find-activegate-files "Find out where ActiveGate files are stored on Windows and Linux systems.").

`autoupdater` (folder)

Contains AutoUpdater service logs and RPM, Synthetic, zRemote installer modules.

`install` (folder)

Contains ActiveGate installer logs.

`zremote` (folder)

Contains zRemote, watchdog logs and agent configuration files.

`synthetic` (folder)

Contains ActiveGate Synthetic monitors configuration files and logs.

`remotepluginmodule` (folder)

Contains logs for Extensions and agent executing them.

## Data privacy

To comply with regional data protection and privacy regulations, Dynatrace automatically deletes all diagnostic data 30 days after its collection. This applies to the data in your Dynatrace environment and on the Dynatrace Cluster.

You can choose to delete collected diagnostic data earlier. To ensure transparency, Dynatrace keeps only a small set of information about who, when, where, and why the diagnostic data was collected.

For related details on Dynatrace data privacy, see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Check retention times for various data types.").

## Troubleshooting

Analyze automatically

agctl

* [Status: 'Collecting of the diagnostic data wasnât possible within 20 minutes.'ï»¿](https://dt-url.net/zl237tu)
* ['State' appears to be frozen.ï»¿](https://dt-url.net/ua437h4)

* [Message: 'Unexpected response status code = 500, cannot create SupportArchive file.'ï»¿](https://dt-url.net/zl037au)

## FAQ

Can I access the S3 directly or use my own S3?

No, you cannot access the S3 directly or use your own.

The diagnostic data is uploaded to the Dynatrace S3 bucket that is configured for the environment/cluster by Dynatrace. The S3 bucket used depends on the location of the environment/cluster.