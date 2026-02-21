---
title: Analyze memory dumps
source: https://www.dynatrace.com/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis
scraped: 2026-02-21T21:20:45.749066
---

# Analyze memory dumps

# Analyze memory dumps

* How-to guide
* 5-min read
* Updated on Jan 19, 2026

Dynatrace can store and analyze memory dumps for Java, .NET, and Node.js applications.

Memory dumps are stored by OneAgent locally for a limited time on the disk of the monitored application-server machine.

If an ActiveGate is configured, then OneAgent automatically uploads the memory dumps to the ActiveGate, which acts as a long-term storage center for memory dumps. This approach ensures that memory dumps are available only to users who have access to the network location of your ActiveGate. This precaution provides an additional security layer to ensure that no personal data leaves your data center unless you configure it that way.

![Memory dump page](https://dt-cdn.net/images/memory-dumps-1181-d3e7b9b87e.png)

## Before you begin

* To trigger memory dumps, you need the [**View sensitive request data**](/docs/manage/identity-access-management/permission-management/role-based-permissions#environment "Role-based permissions") user permission.
* To store memory dumps, your application server must have adequate space.
* To access persisted memory dumps via Dynatrace web UI, [configure an ActiveGate to store memory dumps in a centralized location](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate."). To learn more about memory dump retention time, see [Data retention periods](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#memory-dumps "Check retention times for various data types.").

## Trigger memory dumps

To trigger a memory dump

1. Navigate to the **Memory dumps** page:

   * On the page of the entity that you want to analyze, select **More** (**â¦**) > **Memory dump details**.
   * Go to ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization** > **Memory dumps**.
2. Select the process you want to analyze and select **Trigger new dump** to generate a new memory dump.  
   It takes a few minutes to generate a memory dump. The time required varies widely based on application type. Java applications that have multiple GBs of heap memory may take several minutes; smaller dumps are available almost immediately.

   Java

   Dynatrace uses the [JVM Tool Interface (JVM TI)ï»¿](https://docs.oracle.com/javase/8/docs/platform/jvmti/jvmti.html) to generate memory dumps. For this reason, your JVM may stall during memory-dump generation. Please restart your Java-based application following trigger of a memory dump.
3. After a few minutes, refresh the page. The newly created dump now appears in the list.

## Download and view memory dumps

To download memory dumps

1. Navigate to the **Memory dumps** page:

   * On the page of the entity that you want to analyze, select **More** (**â¦**) > **Memory dump details**.
   * Go to ![Profiling & Optimization](https://dt-cdn.net/hub/logos/profiling-optimization.png "Profiling & Optimization") **Profiling & Optimization** > **Memory dumps**.
2. Expand your memory dump record.
3. From the **Download link** list, select the ActiveGate from where you want to download the memory dump, and select **Download**.

   If you can't download the memory dump via UI, download the file manually at local path indicated in the web UI. Note that memory dumps that are stored by OneAgent locally are available for a limited time; when OneAgent periodically empties the directory, the file size could be 0 bytes.

In the case of Java applications, the download provides the memory dump in [hprofï»¿](https://dt-url.net/kh03s1r) format, which can be analyzed using a number of tools, including [Eclipse Memory analyzerï»¿](https://dt-url.net/uq23syk) and [VisualVMï»¿](https://dt-url.net/mz43sws). The IBM JVM doesn't support hprof, but its own format called IBM Portable Heap Dump (PHD). This can also be analyzed by the Eclipse Memory analyzer.

Node.js memory dumps can be opened in Google Chrome's integrated memory heap snapshot analysis tool.

.NET memory dumps can be opened in [PerfViewï»¿](https://dt-url.net/fb03syb) or Visual Studio.

## Limitations

* .NET memory dumps are not supported in Alpine Linux based containers.
* Memory dump uploads are not supported for both [Kubernetes Applicationâonly monitoring](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") and [Kubernetes Cloud Native Full Stack monitoring](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes").

  This is because OneAgent runs in a container with a readâonly filesystem (OneAgent binary directory `/opt/dynatrace/oneagent-paas` is mounted as readâonly), so Dynatrace cannot write the memory dump files it needs. At the same time, the `DATA_STORAGE` installer parameter used to override the dump directory is [not supported in containerâbased deployments](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). Therefore, it's not possible to change the dump location to a writable path. As a result, memory dump collection is not possible in Kubernetes environments monitored with Applicationâonly monitoring or Cloud Native Full Stack.

## FAQ

If I enable memory dump analysis on multiple ActiveGates, which ActiveGate will perform the memory dump?

ActiveGates have an automatically assigned priority. If more than one ActiveGate has the same priority, an endpoint is selected randomly.

What happens if a file transfer to an ActiveGate fails?

OneAgent attempts to send the dump list to all available endpoints until it finds one that works. This process is retried until it's successful or until the dumps are deleted by aging tasks (for example, if there are too many or if they are too old).

What happens if ActiveGate runs out of space for memory dumps?

ActiveGate first deletes outdated dumps. If there are no outdated dumps, ActiveGate deletes the oldest dumps first.

Can I configure where OneAgent stores memory dumps?

Yes. OneAgent stores memory dumps locally and ensures that dumps do not leave your local network. You can [customize the location of the memory dumps](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux#data-storage "Learn how to use the Linux installer with command line parameters.").

The end user can't access any of ActiveGate endpoints. Can I still provide access to the memory dump file?

Yes. Because from time to time an ActiveGate endpoint might not be accessible to the end user, ActiveGates can have multiple IP addresses, and so multiple endpoints. If all of the existing endpoints are not accessible to the end user at the same time, you can still provide access to the memory dump file.

* You can enable remote access to the ActiveGate by changing the public endpoints.  
  To learn how to configure a new endpoint, see:

  + [Enable the memory dump module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#mem_dump_mod "Learn which ActiveGate properties you can configure based on your needs and requirements.")
  + [Configure ActiveGate for memory dump storage](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage "Learn how to enable storage of memory dumps on an ActiveGate.")
* If remote access to the ActiveGate is not possible, you can download the memory dump file manually from the ActiveGate host.

  + To access the ActiveGate host, use a protocol that allows you to transfer files (such as sFTP or SSH).
  + To download the memory dump file, you need to [learn the location of the file](/docs/observe/application-observability/profiling-and-optimization/memory-dump-analysis/configure-an-activegate-for-memory-dump-storage#specify-dedicated-dump-directory "Learn how to enable storage of memory dumps on an ActiveGate.").
  + To be able to identify the memory dump, unzip its file via a protocol that includes a `summary.json` (such as sFTP or SSH).

## Related topics

* [Dynatrace ActiveGate](/docs/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.")
* [Role-based permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions "Role-based permissions")