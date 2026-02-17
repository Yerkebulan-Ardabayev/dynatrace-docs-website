---
title: Troubleshooting OneAgent deep-monitoring issues
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/troubleshoot-oneagent-deep-monitoring-issues
scraped: 2026-02-17T21:23:58.585430
---

# Troubleshooting OneAgent deep-monitoring issues

# Troubleshooting OneAgent deep-monitoring issues

* Latest Dynatrace
* 3-min read
* Published Jul 16, 2018

Dynatrace OneAgent is supported on many [platforms](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") and offers deep monitoring for many [technologies and frameworks](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks."). The Dynatrace team tests all possible deep-monitoring scenarios, but to streamline our supportability in situations in which deep monitoring might not work as planned, you can leverage the [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") page.

## Use cases

Settings on the **OneAgent features** page make it possible to disable certain OneAgent functionality at a fine-grained level to facilitate issue resolution. This can be useful for identifying the root cause of a problem, all the way down to a specific feature.

These settings also make it possible to temporarily disable certain features that might lead to problems while retaining all other functionality. At the same time, the Dynatrace Support team can work on a permanent fix.

Before deactivating OneAgent settings

We don't recommended deactivating OneAgent feature settings without first consulting Dynatrace Support. When you disable a specific OneAgent feature in your environment, OneAgent stops capturing observability data for this feature, so you might miss important information.

## Settings

Each feature on the **OneAgent features** page can be turned off for the entire environment, a specific process group, or a single process.

### Environment settings

To turn a feature on or off for the entire environment

1. Go to **Settings**.
2. Select **Preferences** > **OneAgent features**.
3. Find the feature. You can enter a filter string above the table.
4. Expand the entry to:

   * Optional Review the feature description
   * Optional Review metadata
   * Optional Follow a link to relevant release notes
5. Change the **Enabled** setting as needed.

All instrumentation features can be enabled or disabled by the main toggle, and some of them have two additional options:

* **Activate this feature also in OneAgents only fulfilling the minimum Opt-In version**  
  This setting activates a feature with a minimum opt-in version when first released. Usually, you can activate a feature if it fulfills the minimum OneAgent version, but some of them are first released as opt-in features with a minimum opt-in version. This is useful when a General Availability (GA) OneAgent feature is greater than a minimum opt-in version. If you already enabled the feature during opt-in, you can still use the OneAgent without upgrading to the new GA version.
* **Instrumentation enabled**  
  This setting has an immediate effect. However, upon restart/startup of a process, the feature won't be added to your application. This means that the feature will have no impact on your application. The downside is that, if you re-enable the feature later, you'll need to restart the affected processes.

### Process-specific settings

If a specific feature is problematic only in the context of a specific process group, you can disable the feature for just that process group and leave the rest of your environment untouched.

To turn a feature on or off for a particular process or group of processes

1. Go to **Smartscape Topology**.
2. Select **Processes**.
3. On the topology map, hover over the process and select the link icon to go to the process details page. For example:

   ![Link from Smartscape topology to process details page](https://dt-cdn.net/images/link-to-process-page-377-da0282e435.png)
4. On the process details page, select **More** (**â¦**) > **Settings** and then select the **OneAgent features** tab.
5. Select **Add override** to add a process-specific setting that overrides the environment setting.
6. Type a search string in the **Feature** box to find and select the feature.
7. Set the switches as needed for the override and then select **Save changes**.