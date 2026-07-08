---
title: CPU profiling
source: https://docs.dynatrace.com/managed/observe/application-observability/profiling-and-optimization/cpu-profiling
---

# CPU profiling

# CPU profiling

* How-to guide
* 2-min read
* Published Nov 22, 2018

Dynatrace offers the following capabilities that allow you to perform enhanced code-level CPU analysis:

* Gain insights into processes and process group hotspots
* Access background activity, service activity, single request executions, and specific requests
* Break down and filter data by code execution, network I/O, disk I/O, lock time, and wait times over times
* Break down and filter data by API over time
* View forward stack traces and hotspots with reverse stack traces
* Gain support for Java, .NET, PHP, Node.js, and Golang

To perform code-level CPU analysis:

1. Go to **Profiling & Optimization** and select **Continuous CPU profiling**.
2. Select the process group that contains the process that you want to analyze.
3. Find the process you want to analyze and, in the **Actions** column, select the corresponding **Method hotspots** icon to view the **Method hotspots** page.

![Select method hotspots for process](https://dt-cdn.net/images/select-method-hotspots-for-process-1642-febf8aa198.png)

Select method hotspots for process

## Analysis options

To analyze a process group, remove the filters.

The color coding of the pie chart, the area chart, and the bars in the code-level stack facilitate code-level diagnostics.

To access the breakdown of processes, select the **Top APIs** tab. You can [configure the list of APIs](/managed/observe/application-observability/services/customize-api-definitions "Set detection rules to customize APIs in your environment.").

![Top APIs tab in CPU profiling](https://dt-cdn.net/images/cpu-analysis-top-apis-1861-9b7ace016f.png)

Top APIs tab in CPU profiling

To view the forward stack trace, select the **Call hierarchy** tab. Each listed method is tagged with the name and color of the API.

![Call hierarchy tab](https://dt-cdn.net/images/tab-call-hierarchy-1599-8547c4ef49.png)

Call hierarchy tab

Select the **Hotspots** tab to view the top three hotspots with reverse stack traces.

![Hotspots tab](https://dt-cdn.net/images/tab-hotspots-1603-29f5680bb8.png)

Hotspots tab

## Filter

When you filter the execution times and top APIs, the **Call hierarchy** and **Hotspots** views inherit the defined filters.

In the following example, filtering by code execution and Built-In JRE (by selecting **Code execution** under the **Execution time** tab and selecting **Built-In JRE** under the **Top APIs** tab) reveals in the **Hotspots** tab that most of the built-in JRE API execution time is within the `ConcurrentLinkedQueue.iterator` call. When you open the stack frames, you can identify the culprit.

![Filter CPU analysis contribution breakdown](https://dt-cdn.net/images/cpu-analysis-breakdown-filter-1863-8fa231eaaf.png)

Filter CPU analysis contribution breakdown

## Download code

Prerequisites

Ensure you have the **View sensitive request data** [permission](/managed/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions") in your environment.

Limitations

Downloading the code is supported for Java, .NET, and Node.js.

To download the code for an execution,

1. Go to **Actions** and select  > **Source code**.
2. Choose the process from which you want to download the code.
3. Select **Download** for the execution you're interested in.
4. Open the source code.

   Node.js

   Java

   .NET

   The source code is directly visible in Dynatrace.

   Required To convert the code into source code, use an external decompiler, such as [Bytecode Viewer﻿](https://bytecodeviewer.com).

   Choose the decompiler most suited to the specific Java version you’re working with.

   Required To convert the code into source code, use an external decompiler, such as [dotPeak﻿](https://www.jetbrains.com/decompiler/).

   Choose the decompiler most suited to the specific .NET version you’re working with.