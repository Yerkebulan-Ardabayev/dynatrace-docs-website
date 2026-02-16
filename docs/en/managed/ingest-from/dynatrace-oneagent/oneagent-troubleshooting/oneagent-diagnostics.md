---
title: OneAgent diagnostics
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics
scraped: 2026-02-16T09:39:44.099443
---

# OneAgent diagnostics

# OneAgent diagnostics

* Latest Dynatrace
* 7-min read
* Published Oct 22, 2020

You can run fully automated OneAgent troubleshooting for Dynatrace SaaS and Managed environments starting with Dynatrace version 1.208.

The workflow enables you to:

* Automatically pinpoint a OneAgent-related issue in highly dynamic environments, at a specific point in time
* Easily collect the diagnostic data for a specific entity, and automatically get potential solutions for detected anomalies
* Quickly resolve common issues on your own, reducing the amount of time spent on diagnosing
* Directly provide Dynatrace Support all the details they need to diagnose the issue

Command-line diagnostics

If you don't have access to Dynatrace or you would like to script diagnostic data collection, you can use the `oneagentctl` command to collect a subset of full diagnostics data right on the host where OneAgent is installed. For more information, see [Create support archive](/docs/ingest-from/dynatrace-oneagent/oneagent-configuration-via-command-line-interface#create-support-archive "Learn how to perform some OneAgent configuration tasks without the need to reinstall OneAgent.").

## Requirements

* Dynatrace SaaS environment: Dynatrace version 1.202+
* Dynatrace Managed environment: Dynatrace version 1.208+
* **View sensitive request data** environment permission

## Analyze automatically

This procedure describes the default procedure: Dynatrace collects diagnostics data for a host or process and immediately analyzes it.

If you prefer to collect and review the data before manually submitting it to Dynatrace for analysis, see [Collect and review locally](#collect-and-review-locally).

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Select the host you want to troubleshoot.
3. Run diagnostics on the host or process level.

   * Host level: on the host page, open the browse menu (**â¦**) and select **Run OneAgent diagnostics**.
     Example menu selection

     ![OneAgent diagnostics: menu item](https://dt-cdn.net/images/diagnostics-menu-item2-950-0243641987.png)
   * Process level: on the host page, open a process page, and then select **Run OneAgent diagnostics** from the browse menu (**â¦**) on the process page.
4. On the **Run Dynatrace OneAgent diagnostics** page, briefly describe what isnât working as expected from your point of view.

   Example OneAgent diagnostics page

   ![OneAgent diagnostics: run](https://dt-cdn.net/images/run-diagnostics-1548-2f9988d21a.png)
5. Optional By default, 24 hours (1 day) of data is collected for analysis. If you need more data, select the **Advanced options** link, change the number of days, and select **Apply**.
6. Select **Start analysis**.

### What happens next

Dynatrace does the following:

* Collects diagnostic data for the last 24 hours (if you didn't change the default) of the affected host or process
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

Example

![OneAgent diagnostics: alerts](https://dt-cdn.net/images/public-alerts-1-1783-14caea955d.png)

In this example, you can see that the fully automated OneAgent troubleshooting workflow has detected that this OneAgent was mounted on a network file system (NFS), which isnât supported. Instructions for resolving the issue are included.

## Collect and review locally

This procedure describes how to collect diagnostics data for a host or process locally. Use this option if you prefer to collect and review the data before manually submitting it to Dynatrace for analysis.

If you instead want to collect data and submit it to Dynatrace automatically for analysis, see [Analyze automatically](#analyze-automatically).

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Select the host you want to troubleshoot.
3. Run diagnostics on the host or process level.

   * Host level: on the host page, open the browse menu (**â¦**) and select **Run OneAgent diagnostics**.
     Example

     ![OneAgent diagnostics: menu item](https://dt-cdn.net/images/diagnostics-menu-item2-950-0243641987.png)
   * Process level: on the host page, open a process page, and then select **Run OneAgent diagnostics** from the browse menu (**â¦**) on the process page.
4. On the **Run Dynatrace OneAgent diagnostics** page, briefly describe what isnât working as expected from your point of view.

   Example OneAgent diagnostics page

   ![OneAgent diagnostics: run](https://dt-cdn.net/images/run-diagnostics-1548-2f9988d21a.png)
5. Select the **Advanced options** link.
6. Select **and store locally**.

   * While you are here, you can also change the number of days of data to collect (default = `1 day`).
7. Select **Apply**.
8. Select **Start collection** to collect diagnostic data and store it locally.

### What happens next

Dynatrace now:

* Collects diagnostic data for the last 24 hours (if you didn't change the default) of the affected host or process
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

### OneAgent troubleshooting in Dynatrace Managed air-gapped environments

In a Dynatrace Managed air-gapped environment:

1. Use the **Store locally** option under **Advanced options** as described above.
2. After diagnostic data is collected, you can add the data to your support ticket.
3. Dynatrace can then fetch the diagnostic data from your support ticket, analyze it, and provide automated feedback to Dynatrace Support about detected anomalies.

Stringent data privacy protections are enforced and logged throughout this process.

## OneAgent diagnostics overview

For an overview of all OneAgent troubleshooting runs in your environment

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Open the browse (**â¦**) menu and select **OneAgent diagnostics overview**.

The **Dynatrace OneAgent diagnostics overview** page lists all OneAgent diagnostics activity in your environment. Expand any entry to see details. If the data has not been deleted (all diagnostic data is deleted automatically after 30 days), you can download it or delete it.

## Contents of diagnostic data

All the collected diagnostic data is compressed into a `SupportArchive<ID number>` ZIP file that includes the following folders and files:

Folder or file

Description

`host` (folder)

Contains a snapshot of the topology information of the host entity including any relationships to other hosts.

`monitored_entities` (folder)

Contains a snapshot of the topology information of all involved process groups, process group instances, services, and service instances.

`agent_registration_entries` (JSON)

Contains information about which OneAgent code modules are connected to Dynatrace.

`archive` (JSON)

Contains information about who, when, where, and why the diagnostic data was collected.

`monitoring_state` (JSON)

Contains information about the monitoring state of processes and related problems.

`support_archive` (ZIP)

Contains the local configuration of the OneAgent installed on the host or process where youâve run the troubleshooting, as well as the OneAgent-related log files.

`diagnostic_files` ZIP

Contains information about the process group detection, auto-injection problems, and extension configuration.

## Data privacy

To comply with regional data protection and privacy regulations, Dynatrace does the following:

* Masks some personal data before storing a support archive in Cassandra and uploading it to an AWS S3 bucket. For example, IBANs and URI credentials are replaced with `<masked>`. However, some personal data may not be masked.
* Writes audit log messages when support archives are created, analyzed, accessed, and deleted to ensure transparency in the use of support archives.
* Provides access to OneAgent support archives only to users that have the **View sensitive request data** [environment permission](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions").
* Automatically deletes all diagnostic data 30 days after its collection.

  This applies to the data in your Dynatrace environment. You can also choose to delete collected diagnostic data earlier.

For related details on OneAgent diagnostics, check the following pages:

* [Personal data captured by Dynatrace](/docs/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#oneagent-diagnostics "Find out what types of end-user data may be captured during Dynatrace monitoring and the methods that are available for masking personal end-user data.")
* [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#diagnostics "Check retention times for various data types.")

## Troubleshooting

Status: `Collecting of the diagnostic data wasnât possible within 20 minutes.`

* If Dynatrace cannot collect diagnostic data within 20 minutes, it automatically tries again.
* If the retry fails as well, we suggest that you contact a Dynatrace product expert via live chat.

`State` appears to be frozen.

**State** does not automatically refresh. Select **Refresh** to check for a state change.

## FAQ

Can I access the S3 directly or use my own S3?

No, you cannot access the S3 directly or use your own.

OneAgent diagnostics uploads the diagnostic data to the Dynatrace S3 bucket that is configured for the environment/cluster by Dynatrace. The S3 bucket used depends on the location of the environment/cluster.