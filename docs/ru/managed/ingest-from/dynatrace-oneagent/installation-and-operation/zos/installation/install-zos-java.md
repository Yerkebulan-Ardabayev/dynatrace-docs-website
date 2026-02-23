---
title: Install the z/OS Java module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java
scraped: 2026-02-23T21:24:14.567258
---

# Install the z/OS Java module

# Install the z/OS Java module

* Latest Dynatrace
* 15-min read
* Updated on Nov 18, 2025

With the z/OS Java module, you can get observability for your Java applications including IBM MQ and database calls.

Observability for

Including

WebSphere Application Server

WebSphere Liberty

* Incoming web requests on WebSphere Application Server and Liberty
* Outgoing web requests from WebSphere Application Server and Liberty via the Apache HttpClient
* Outgoing CICS Transaction Gateway requests from WebSphere Application Server and Liberty via the CTG client
* Websphere Application Server Websphere Liberty specific metrics (PMI and JMX)
* JVM specific managed memory metrics (JMX)

z/OS Connect

* Incoming web requests on z/OS Connect
* Outgoing requests from z/OS Connect via the CICS, IMS, and IBM MQ service providers
* z/OS Connect specific metrics (JMX)
* JVM specific managed memory metrics (JMX)

CICS/IMS transactions

Transactions initiated using

* IBM MQ and JMS
* CICS SOAP and CICS Transaction Gateway
* IMS SOAP Gateway

Database calls

Database calls with their SQL statements from Java applications to Db2 via JDBC

Trace your Java applications end-to-end with Dynatrace and quickly detect any anomalies

Analyze the performance of your transactions end-to-end using the [service flow](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").

![zOS Java 1](https://dt-cdn.net/images/zos-java-1-2772-facc3b2740.png)

Use the [PurePath distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") to drill down to the code level and to optimize your programs.

![zOS Java 2](https://dt-cdn.net/images/zos-java-2-2729-43a263828d.png)

Quickly detect anomalies with the [Service response time hotspots](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.").

![zOS Java 3](https://dt-cdn.net/images/zos-java-3-2312-97d45f24a2.png)

Analyze failures and exceptions with detailed stack traces.

![zOS Java 4](https://dt-cdn.net/images/zos-java-4-2674-ebbc7f564d.png)

Understand the health and performance of your JVM with the applications deployed on it

Gain insights into your JVM with the Dynatrace managed memory metrics:

![zOS Java metrics 1](https://dt-cdn.net/images/zos-java-metrics-1-2472-ee3a4ee341.png)

Understand the health and performance of your application servers with technology-specific metrics:

![zOS Java metrics 2](https://dt-cdn.net/images/zos-java-metrics-2-2473-4cc98e9473.png)

### What JMX and PMI metrics does Dynatrace provide out of the box?

JVM specific metrics:

Metric group

Metric

Source

JVM memory

Garbage collection total activation count

JMX

JVM memory

Garbage collection total collection time

JMX

JVM memory pool

Garbage collection count

JMX

JVM memory pool

Garbage collection time

JMX

JVM memory pool

Heap memory pool maximum bytes

JMX

JVM memory pool

Heap memory pool committed bytes

JMX

JVM memory pool

Heap memory pool used bytes

JMX

JVM memory runtime

Runtime maximum memory

JMX

JVM memory runtime

Runtime total memory

JMX

JVM memory runtime

Runtime free memory

JMX

JVM threads

Thread count

JMX

JVM classes

Total number of loaded classes

JMX

JVM classes

Number of loaded classes

JMX

JVM classes

Number of unloaded classes

JMX

WebSphere Liberty and z/OS Connect specific metrics:

Metric group

Metric

Metric description

Source

JDBC connection pool

In use connections

The number of connections in use. This number might include multiple connections that are shared from a single managed connection.

JMX

JDBC connection pool

Free connections

The number of managed connections in the free pool.

JMX

JDBC connection pool

Managed connections

The total number of managed connections in the free, shared, and unshared pools.

JMX

JDBC connection pool

In use time

The average time in milliseconds that a connection is in use.

JMX

JDBC connection pool

Wait time

The average waiting time in milliseconds until a connection is granted if a connection is not currently available.

JMX

Thread pool

Pool size

The average number of threads in pool.

JMX

Thread pool

Active threads

The number of active threads that are serving requests.

JMX

Servlet

Request count

The total number of requests that a servlet processed.

JMX

Websphere Application Server specific metrics:

Metric group

Metric

Metric description

Source

JDBC connection pool

Pool size

The size of the connection pool.

PMI

JDBC connection pool

Free pool size

The number of managed connections that are in the free pool.

PMI

JDBC connection pool

Concurrent waiters

The number of threads that are currently waiting for a connection.

PMI

JDBC connection pool

Average wait time

The average waiting time in milliseconds until a connection is granted if a connection is not currently available.

PMI

JDBC connection pool

Average use time

The average time in milliseconds that a connection is in use.

PMI

JDBC connection pool

Percent used

The percent of the pool that is in use.

PMI

Thread pool

Pool size

The average number of threads in pool.

PMI

Thread pool

Active threads

The number of concurrently active threads.

PMI

Servlet

Live sessions

The number of local sessions that are currently cached in memory from the time at which this metric is enabled.

PMI

Servlet

Total requests

The total number of requests that a servlet processed.

PMI

### Can I monitor custom JMX metrics with the z/OS Java module?

Yes, you can use the z/OS Java module to monitor custom JMX metrics. For more information, see [Monitor JMX metrics on z/OS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/zos-java-custom-jmx-metrics "Learn how to set up JMX metrics monitoring for your Java applications on z/OS.").

## Prerequisite

Activate the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **Forward Tag 4 trace context extension**.

## Download

1. [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Download and install the Dynatrace product datasets for z/OS.") and extract the JAR file (`dynatrace-oneagent-zos-java.jar`).
2. Transfer the JAR file to your z/OS [Unix System Servicesï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS) environment in binary mode.
3. Create a new file with the name `dtconfig.json` in the z/OS USS folder where the module is located.

   A minimal `dtconfig.json` file contains your Dynatrace environment ID (**Tenant**), cluster ID (**ClusterID**), and the zDC subsystem name (**ZdcName**). For example:

   ```
   {



   "Tenant": "myTenant",



   "ClusterID": myCluster,



   "ZdcName": "DEFAULT"



   }
   ```

   Replace `myTenant` and `myCluster>` with your Dynatrace environment values. To find these values, in Dynatrace Hub, select **OneAgent** > **Download OneAgent** or **Set up** (latest Dynatrace) > **z/OS**.

   If the zDC name is defined as `DEFAULT`, the module will connect to the default zDC subsystem ID. To use a different zDC, replace `DEFAULT` with an alternative subsystem ID.

   You can find the zDC subsystem name in the [SYSIN parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC).") of your JCL SYSIN member `ZDCSYSIN`. The default zDC subsystem name is `MEPC`.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



   SUBSYSTEM_ID(MEPC)



   DEFAULT(YES)
   ```

   If `DEFAULT` is set to `YES` in the [SYSIN parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."), you can also use `DEFAULT` in the `dtconfig.json` file.

* EBCDIC 1047, UTF-8, and ASCII encodings are supported for the `dtconfig.json` file.
* The module automatically reads `dtconfig.json` when it's placed in the same folder as `dynatrace-oneagent-zos-java.jar`.
* If you put `dtconfig.json` in a different folder, you need to specify the path to it via the environment variable `DT_CONFIG_FILE`. The path must include the filename. You can use an absolute path or a path relative to the working folder of the process.

## Installation

### Updating a previously installed version of Dynatrace

If you have Dynatrace installed and are upgrading to a new release, you can jump to section [Update][#update]

### Application server



You need to add the z/OS Java module to the JVM arguments of each application server that you want to monitor.

WebSphere Application Server

WebSphere Liberty

WebSphere Liberty inside a CICS region

1. Open the WebSphere Application Server Admin Console and navigate to **Application servers**.
2. Select `<YOUR_SERVER>` > **Process definition** > **Servant**, and choose **Java Virtual Machine**.
3. Copy the JVM argument from your Dynatrace environment and paste it into the **Generic JVM arguments**:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Replace `PATH_TO` with the path to your JAR file.
4. Save the changes and restart your WebSphere Application Server.

* It's only necessary to add the module to the Servant processes.
* We recommend adding the module as the first JVM argument.
* The module must not be appended at the end of the command line.

1. Create the `jvm.options` file in the root folder of your WebSphere Liberty (this folder typically also contains the `server.xml` file) or edit an existing file.
2. Copy the JVM argument from your Dynatrace environment and paste it into the `jvm.options` file:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Replace `PATH_TO` with the path to your JAR file.
3. Add the `monitor-1.0` feature to your `featureManager` in the `server.xml` file to collect additional metrics like connection pools or thread pools:

   ```
   <server>



   <featureManager>



   <feature>monitor-1.0</feature>



   </featureManager>



   </server>
   ```
4. Save the changes and restart your WebSphere Liberty.

* We recommend to add the module as the first JVM argument.
* The module must not be appended at the end of the command line.
* We use the WebSphere Liberty server name as process group instance name per default. If you want to use a different process group instance name, you can override it by adding the following system property to your JVM command line: `-Dwlp.server.name=yourServerName`. Replace `yourServerName` with your individual name.

1. Create the `.jvmprofile` file in your CICS region that belongs to the CICS JVMSERVER that is executing WebSphere Liberty or edit an existing file.
2. Copy the JVM argument from your Dynatrace environment and paste it into the `.jvmprofile` file:

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Replace `PATH_TO` with the path to your JAR file.
3. Add the `monitor-1.0` feature to your `featureManager` in the `server.xml` file to collect additional metrics like connection pools or thread pools:

   ```
   <server>



   <featureManager>



   <feature>monitor-1.0</feature>



   </featureManager>



   </server>
   ```
4. Save the changes and restart your WebSphere Liberty.

* Monitoring of both the CICS region and the WebSphere Liberty that operates inside this CICS region is only supported if they report to a different zDC subsystem. If they report to different zDC subsystems, at least one of those zDCs must be started as non-default (see `SUBSYSTEM_ID` in the [zDC SYSIN parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC).")). However, both zDCs can report to the same zRemote module.

  + For the CICS module, the zDC subsystem name is defined in the [CICS SYSIN parameters](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#connect-cics-zdc "Install the Dynatrace CICS module.").
  + For the z/OS Java module, the zDC subsystem name is defined in the [`dtconfig.json` file](#download).
* OneAgent version 1.281+ Dynatrace version 1.283+ When running in a CICS region, the process group instance name will include both the CICS region name and the WebSphere Liberty server name in the `CICS region (server name)` format.

### Middleware

You need to add the z/OS Java module to each product that you want to monitor.

z/OS Connect Enterprise Edition

CICS Transaction Gateway

IMS SOAP Gateway

1. Add the module to the `JVM_OPTIONS STDENV` variable:

   ```
   JVM_OPTIONS=-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Replace `PATH_TO` with the path to your JAR file.
2. Optional Add the `monitor-1.0` feature to your `featureManager` in the `server.xml` file to collect additional metrics like connection pools or thread pools:

   ```
   <server>



   <featureManager>



   <feature>monitor-1.0</feature>



   </featureManager>



   </server>
   ```
3. Save the changes and restart your z/OS Connect Enterprise Edition.
4. For the CICS service provider, activate the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS CICS z/OS Connect**.
5. For the IMS service provider:

   1. Add the IMS module to **IMS Connect** as described in [Install the IMS module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims#install "Install the Dynatrace IMS module.").
   2. Activate the [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS IMS z/OS Connect**.
6. For the MQ service provider, no additional configuration is needed.

1. Add the module to the `CTGENV` member and to the `CTGSTART_OPTS` variable:

   ```
   -j-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar
   ```

   Replace `PATH_TO` with the path to your JAR file.
2. Save the changes and restart your CICS Transaction Gateway.

* Only the EXCI and IPIC protocols are supported.
* WAS local mode configuration of the CICS Transaction Gateway configuration is not supported.

1. Add the module as a `zDT` option to the IMS SOAP Gateway parameters:

   ```
   zDT="-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar"
   ```

   Replace `PATH_TO` with the path to your JAR file.
2. Export the defined `zDT` option so that `IBM_JAVA_OPTIONS` includes it.

   ```
   export IBM_JAVA_OPTIONS="$zDT $JAVA_OPTS"
   ```
3. Save your changes and restart the IMS SOAP Gateway.

## Logging

By default, logging is disabled for the z/OS Java module. To enable logging, add one of the following options to the JVM argument:

Option

Default value

Description

log-stdout

`false`

If `true`, write logs to the standard output stream.

log-stderr

`false`

If `true`, write logs to the standard error stream.

log-file

`false`

If `true`, write logs to a file using file rotation (persisting the file with index 0). Naming scheme: `dynatrace-oneagent-java.<PID>.<LPAR>.<INDEX>.log`.

If needed, you can log to multiple locations. For example:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=log-stdout=true,log-file=true
```

If needed, you can customize the file logging with the following options:

Option

Default value

Description

log-file-dir

`<CODEMODULE_FOLDER>/logs`

By default, write log files to the z/OS Java module folder.

It's also possible to write the log files to an absolute path (schema: `/<PATH_TO>/logs`) or to a path relative to the working folder of the process (schema: `<PATH_TO>/logs`).

By changing the default folder, ensure that the application server has appropriate write permissions for the folder in which the module should write the log files.

### OneAgent diagnostics

Dynatrace recommends to write the logs to the shared log folder of the zDC so that they are included into the [OneAgent diagnostics](/docs/ingest-from/dynatrace-oneagent/oneagent-troubleshooting/oneagent-diagnostics "Learn how to run OneAgent diagnostics") workflow. For example, if the `dtzagent` binary is located at `/u/dt/agent/lib64/dtzagent` in the z/OS USS environment, the log folder is `/u/dt/log`. Typically, a shared zDC log folder already exists and contains some zDC logs.

To enable file logging to an absolute path such as the shared zDC log folder `/u/dt/log`, specify the JVM argument as follows:

```
-javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=log-file=true,log-file-dir=/u/dt/log
```

If your zDC is installed in a different location, you must adopt the absolute path of the shared zDC log folder.

## Update

To update your z/OS Java module to a newer version

1. [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Download and install the Dynatrace product datasets for z/OS.") and transfer the JAR file (`dynatrace-oneagent-zos-java.jar`) to your z/OS USS environment in binary mode.
2. Locate your existing dtconfig.json in the z/OS USS folder where the old version of the module is located and copy it to the z/OS USS folder you used in step(1).
3. Stop your monitored application server or middleware.
4. Replace your current JAR file with the new JAR file.
5. Start your application server or middleware.

## FAQ



How can I enable program control for the z/OS Java module?

If, after starting the application server in z/OS, you may see **Not Marked Program Controlled** messages or errors with the return code 139:

```
BPXP015I HFS PROGRAM /tmp/libdynatrace-oneagent-odin-java5848811742465559217.so



IS NOT MARKED PROGRAM CONTROLLED.
```

You need to enable program control for the z/OS Java module. To do so

1. Expand `dynatrace-oneagent-zos-java.jar` that you downloaded into a program controlled folder.
2. Mark the appropriate `.so` file (31 or 64 bit) in the `lib/zos-s390/` directory as program-controlled.

   * Switch to the path that contains the `.so` files.
   * Issue the following command using the 31- or 64-bit file:

     ```
     extattr +p libdynatrace-oneagent-odin-java_64.so
     ```
3. Add `zos-native-library-override` to your JVM argument.

   ```
   -javaagent:/PATH_TO/dynatrace-oneagent-zos-java.jar=zos-native-library-override=<PATH_TO_SO>/libdynatrace-oneagent-odin-java_64.so
   ```

   Where:

   * `<PATH_TO>` is the path to your JAR file.
   * `<PATH_TO_SO>` is the absolute path to the `.so` file that you want to control.
4. Restart your application server.

Can I disable sensors of the z/OS Java module?

By default, all sensors of the z/OS Java module are enabled. In case of problems, you can disable specific sensors by setting their value to `false` in the `dtconfig.json` file.

```
{



"Sensors": {



"Enable": {



"CTG": {



"Server": "false",



"Client": "false"



},



"HttpClient": {



"Apache": "false"



},



"JDBC": "false",



"JMS": "false",



"IbmMQ": "false",



"Servlet": "false",



"ZosConnect": "false"



}



}



}
```