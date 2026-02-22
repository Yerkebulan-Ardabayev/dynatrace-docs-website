---
title: Log sources and storage (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2
scraped: 2026-02-22T21:25:43.477285
---

# Log sources and storage (Logs Classic)

# Log sources and storage (Logs Classic)

* 2-min read
* Updated on Jan 18, 2023

Log Monitoring Classic

Starting with OneAgent version 1.243 and Dynatrace Cluster version 1.252, we strongly encourage you to switch to [Log Storage](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-storage "Configure storage of log files that are already known to OneAgent.").

With the release of Dynatrace version 1.285 (March 2024), Dynatrace will automatically convert your [log source](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-files-manually "Learn how to manually add log files for analysis.") and [log storage](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-add-log-file-sources "Learn how to include and exclude log sources for analysis.") configurations to the latest version.

You can also upgrade to the new configuration by selecting **Upgrade configuration**. All of your current settings will be fully upgraded.

The upgraded configuration (see [Log ingest rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-storage-configuration "Include and exclude specific log sources already known to OneAgent for storage and analysis.")) defined on the **Custom log source configuration** and **Log sources and storage** pages will give you:

* Greater flexibility in defining log sources (for example, log path, log level, Kubernetes namespace, Kubernetes deployment)
* Flexibility in defining log sources (using environment, host group, and host scopes)
* Granularity in managing log source access rights
* Use of the REST API for managing log sources
* Ability to filter and mask log data at capture

To include or exclude specific log sources from storage

1. Go to **Settings** > **Log Monitoring** > **Log sources and storage**.
2. Select **Include all logs**, **Include the following logs**, or **Exclude the following logs** from the list.
3. Switch between tabs to select logs from **Hosts perspective** or from **Process groups perspective**.

Switching tabs

Only log sources in the currently active (selected) tab will be saved. Log sources marked in the other tab will be ignored.

4. Select **Save changes**.

## Migration to the new storage configuration

After you go to **Settings** > **Log Monitoring** > **Log storage**, automatic migration from the old storage configuration format to the new one takes place. The following changes will occur in your current configuration:

* **Host perspective**  
  All items configured on the **Hosts perspective** are migrated as a set of matchers to the corresponding host scope.
* **Process groups perspective**  
  Only the rules that are applied to a whole process group are migrated to the tenant scope. If a process group is enabled only for a subset of hosts, the relevant rules must be created on the host level.

After your configuration of log sources is successfully migrated, you can use new configuration items and add your matchers.

## FAQ

Is this change reversible?

No. After the change, all old configurations are wiped out, so be sure before you make this change.