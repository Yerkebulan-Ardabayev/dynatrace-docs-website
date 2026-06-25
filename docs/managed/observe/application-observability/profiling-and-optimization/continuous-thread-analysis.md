---
title: Continuous thread analysis
source: https://docs.dynatrace.com/managed/observe/application-observability/profiling-and-optimization/continuous-thread-analysis
scraped: 2026-05-12T12:02:48.541969
---

# Continuous thread analysis

# Continuous thread analysis

* How-to guide
* 5-min read
* Published Aug 30, 2019

Multiple-thread architectures can easily scale, as the distribution of work allows CPUs to remain active and continue running code. However, when systems need to coordinate work across multiple threads, locks increase and reductions in code run might occur.

In Dynatrace, such behavior is automatically and continuously detected by OneAgent. With continuous thread analysis, data is continuously available, with historical context, and doesnât need to be triggered if a problem occurs. You can receive alerts on trends, analyze thread dumps, and directly start improving code, when and where it's needed, to prevent bottlenecks.

## Before you begin

To start using continuous thread analysis

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Find and turn on the following OneAgent features for the technology you want to monitor:

   | Technology to monitor | OneAgent features to turn on |
   | --- | --- |
   | Java | **Continuous thread analysis** |
   | Node.js | * **Node.js worker threads monitoring** * **Node.js code module preloading** |

Supported Java versions

Due to a known issue with Java 11, continuous thread analysis of JVM threads is only available for Java 8 and Java 17+ (based on the [supported versions](/managed/ingest-from/technology-support/application-software/java/support-for-jvms "Find out the major JVMs and JDKs that are supported by Dynatrace.")). Application and agent threads remain unaffected.

## Thread analysis

To start analyzing thread dumps

1. Go to **Profiling & Optimization** > **Continuous CPU profiling**.
2. For the process group that you want to analyze, select **More** (**â¦**) > **Threads**.
3. On the **Thread analysis** page, you can:

   * Analyze the thread breakdown by thread states or by estimated CPU time.
   * Include or exclude data on waiting threads at any time, by selecting the related checkbox.
   * Filter the data

     + By request type.  
       Select **Filter requests** > **Type** and choose an option.
     + By request thread-group name.  
       Select the thread-group name. The segmentation of thread groups takes into account the fact that they typically run different functionalities, and gives you quick means to identify CPU consumers.
   * Analyze the method hotspots of a thread group.  
     In the thread group **Actions** column, select **More** (**â¦**) > **Method hotspots**.

## Use cases

Threads are a source of scalability, as they enable your applications to carry out multiple tasks at once. In certain situations, this can become a source of performance bottlenecks. For example:

* High-load systems might experience thread-locking issues, which [prevent the application from scaling](#scalability).
* If the number of active threads is too high, [CPU resources can be wasted](#cpu) due to over-utilization or to operating systems being forced to schedule thousands of threads on a limited set of cores.

Example: Locks prevent application scalability

### Identify scalability issues

In this example, the process group `idea*.exe` shows a spike in CPU consumption. We investigate the problem in its **Thread analysis** page, starting by filtering the thread group list by the **Locking** thread state.

![Locking time in Java process group](https://dt-cdn.net/images/locking-usercase-thread-analysis-1-1565-1d59eb7299.png)

Locking time in Java process group

We see that the system is not in bad shape, but there is still locking behavior affecting `23` thread groups. We select the first and most affected thread group, `JobScheduler FJ pool`, to continue our analysis.

![Analysis of locking time in Java process group](https://dt-cdn.net/images/locking-usercase-thread-analysis-2-1562-55c0abba1f.png)

Analysis of locking time in Java process group

For the thread group `JobScheduler FJ pool`, a considerable amount of time (almost half: `46.1%`) is continuously spent in locking, and it's distributed across `15` threads. This indicates a general lock affecting all of those threads. We want to avoid this behavior because it limits both speed and the ability to increase throughput by adding resources. Ultimately, it can lead to a state where the system wonât be able to process more data even if we add more hardware.

To get to the root cause, we select **More** (**â¦**) > **Method hotspots**.

![Method hotspost analysis for locking time in Java process group](https://dt-cdn.net/images/locking-usercase-thread-analysis-3-1158-1e89cbdec0.png)

Method hotspost analysis for locking time in Java process group

Based on the retrieved information, we can locate the problem of locking and test different ways to write the code to increase its performance.

Example: High number of threads causes over-utilization of resources

### Identify CPU-intensive thread groups

In this example, the process group `doaks-prod1-eastus-cassandra` spends `9.97%` of the time in **Code execution**.

![Cassandra process group spends a considerable amount of time in code execution](https://dt-cdn.net/images/cassandra-process-group-code-execution-3401-524ea5b6f1.png)

Cassandra process group spends a considerable amount of time in code execution

We select **CPU time** to understand how the behavior is affecting CPU consumption. From the chart, we can see that the thread group `MutationStage` is the biggest contributor. From the table below, we learn that it's spending `1.6 d` in **Estimated CPU time** and `3.55%` of the **Overall execution breakdown** in code execution.

![Cassandra process group - CPU consumption](https://dt-cdn.net/images/cassandra-process-group-cpu-consumption-3393-ffd2f798b4.png)

Cassandra process group - CPU consumption

We want to identify which code is executed and how it impacts CPU consumption. After selecting the thread group name (`MutationStage`), the first thread in the list at the bottom of the page is the highest contributor (`MutationStage-2`).

![Thread analysis drill down - Cassandra](https://dt-cdn.net/images/cassandra-thread-analysis-3403-ffbcde45a2.png)

Thread analysis drill down - Cassandra

To see a list of hotspots, we select **More** (**â¦**) > **Method hotspots** for `MutationStage-2`.

![Hotspots - Cassandra thread group](https://dt-cdn.net/images/cassandra-thread-analysis-3815-8e250538fe.png)

Hotspots - Cassandra thread group

We now see that `Unsafe.unpark` contributes `30.1%` to code execution and is a good candidate for optimization.

## FAQ

Is the retention period for continuous thread analysis related to the code-level retention period?

Yes, the data retention period for continuous thread analysis is the same as for [distributed traces, code-level insights, and errors](/managed/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.").