---
title: Real User Monitoring Classic for process groups
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-for-process-groups
---

# Real User Monitoring Classic for process groups

# Real User Monitoring Classic for process groups

* How-to guide
* 2-min read
* Updated on Apr 01, 2026

By default, RUM is enabled for all process groups. For the technologies listed in [Technology support - Real User Monitoring - Web servers and applications](/managed/ingest-from/technology-support#rum-auto-injection "Find technical details related to Dynatrace support for specific platforms and development frameworks."), this allows OneAgent to do the following:

* Automatically inject the RUM JavaScript into each page delivered by this process group
* Provide the necessary information to link user actions with [server-side distributed traces](/managed/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* Deliver the RUM JavaScript
* Forward beacons to the Dynatrace Cluster

You can disable RUM for a process group. For example, you can do that to exclude servers that do not require RUM monitoring. Furthermore, disabling RUM for a process group can serve as a workaround for resolving issues with your applications. However, we recommend that you contact a Dynatrace product expert via live chat to help you determine the root cause of the issue.

## Disable RUM for a process group

If you disable RUM for a process group, the entire RUM functionality listed above is turned off.

To manually disable RUM for a process group

1. Go to **Technologies & Processes**.
2. Select the technology tile that includes the process group where the RUM JavaScript is to be injected.
   The matching process groups are displayed further down the page.
3. Scroll down, and select the required process group.
4. Select **Settings** in the upper-right corner of the page.
5. In the process group settings, select **Real User Monitoring**.
6. Turn off **Enable Real User Monitoring**.

## Important considerations

* If you prefer to insert the RUM JavaScript manually, do not suppress the injection by disabling Real User Monitoring for your process groups. This suppresses not only the injection but also the linking of user actions and distributed traces. Instead, use a custom injection rule as described in [Configure automatic injection in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/rum-injection#manual-insertion-using-oneagent "Configure automatic injection of the RUM JavaScript into the pages of your applications").
* If you want to roll out RUM in a selective manner after deploying OneAgent on your hosts, we recommend using the approach described in [Roll out RUM Classic selectively for your applications](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts"). In principle, the RUM enablement setting at the process-group level also allows for a selective rollout, but this tends to be complex and error-prone.
* If your application consists of multiple tiers, enable RUM at least on OneAgent that instruments the first tier (that is the tier nearest to the browser), which captures the root of the distributed trace.  
  For example, consider an Apache HTTP server as a proxy and a Java app server as a backend. Even though Dynatrace injects the RUM JavaScript on the process group of the Java backend, disabling RUM for the process group of the Apache HTTP server would cause issues. In particular, it would be impossible to link user actions and distributed traces.