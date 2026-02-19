---
title: Install the CICS module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics
scraped: 2026-02-19T21:19:19.778450
---

# Install the CICS module

# Install the CICS module

* Latest Dynatrace
* 14-min read
* Updated on Jan 28, 2026

With the CICS module, you can get observability for your CICS transactions and programs including DB2, DLI, and VSAM calls.

Observability for

Including

CICS transactions

Transactions initiated using

* IBM MQ Bridge and Trigger Monitor
* CICS Transaction Gateway, HTTP/S, SOAP over HTTP/S, JSON using non-Java JSON pipeline
* 3270 terminal

CICS programs

* Programs invoked using CICS LINK
* Transaction details for DPL LINK and START TRANSACTION requests in a distributed trace

Database calls

Database calls with their SQL statements from CICS to Db2 and IMS DB via the DL/I access method

File access

[File access](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/monitoring/monitor-cics-file-access "File access monitoring of CICS applications using the CICS module.") from CICS via the VSAM and BDAM access methods.

Trace your CICS transactions end-to-end with Dynatrace

Analyze the performance of your transactions end-to-end using the [Service flow](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").

![CICS service flow](https://dt-cdn.net/images/cics-trace-2357-0a7717e199.png)

Use the [PurePath distributed traces](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.") to drill down to the code level and to optimize your programs.

![CICS code-level](https://dt-cdn.net/images/cics-code-level-1984-d6aeff52fb.png)

Understand exceptions in the context of your transactions down to the Db2 database layer.

![CICS distributed trace with exception](https://dt-cdn.net/images/cics-distributed-trace-1986-97b2240549.png)

Detect CICS anomalies and isolate fault domains with Dynatrace

Dynatrace Intelligence automatically pinpoints the root cause of problems and assesses their user impact so that you can prioritize mitigation strategies and reduce the mean time to repair.

![CICS automatic fault domain isolation](https://dt-cdn.net/images/cics-problem-1985-100d80f55c.png)

Analyze failures with exception details in the context of transactions.

![CICS failure analysis](https://dt-cdn.net/images/cics-exceptions-1985-478b6f8ba6.png)

## Installation

The CICS module includes a PLT program that initiates at CICS startup. This program uses hooks to instrument CICS terminal and application owning regions, creating events of interest. It forwards monitoring data to the zDC subsystem via shared buffers.

You need to install the CICS module in every CICS region you want to monitor. If Dynatrace is already installed on a CICS and you want to update your CICS module without restarting the CICS region, see [Update the CICS module without region restart](#cics-update).

You need to add the [z/OS Java module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#middleware "Set up Java monitoring on z/OS using the Java module.") to each CICS Transaction Gateway you want to monitor.

### CTS 6.2 support

Beginning with OneAgent version 1.299, we are providing support for CTS 6.2, which is a major change and follows the latest security enhancements for the CICS subsystem.

CTS 6.2 support requires the `DFHBPZDT` load module that is supplied in the `SZDTAUTH` to be available at CICS region startup.
Recommended installation procedure:

Add a line similar to the example below to a PROGxx parmlib member. Note that the `SZDTAUTH` should be APF authorized.

```
LPA ADD MODNAME(DFHBPZDT) DSNAME(<hlq>.SZDTAUTH)
```

To add the module to LPA immediately, enter a console command similar to the below example.

```
SETPROG LPA,ADD,MODNAME=DFHBPZDT,DSNAME=<hlq>.SZDTAUTH
```

Alternatively, it is also possible to add `DFHBPZDT` to the `STEPLIB` of the CICS 6.2 regions where the Dynatrace agent is installed.
However, we do not recommend adding the entire `SZDTAUTH` to the CICS STEPLIB.

To verify the installation, CTS 6.2 prints the following mesage:

```
DFHKE0010  HVPAC449 Vendor table DFHBPZDT for product ID ZDT has been loaded
```

### CICS library definition

You can dynamically add the load library as a CICS library definition in the CSD. The CEDA definition is in `SZDTSAMP` member `CICRDO`. You can find it in the example in the next section.

If you don't want to use the CICS Library definition, you need to add the following PDS (or its contents) to the DFHRPL concatenation:

```
// DD DISP=SHR,DSN=<hlq>.SZDTLOAD
```

Regardless of which option you decide to use, you need to tailor the DSN by replacing `<hlq>` with the high-level qualifier you set during [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Download and install the Dynatrace product datasets for z/OS.").

### Dynatrace CICS programs and transaction

The CICS resource definitions for the Dynatrace CICS module can be found in `SZDTSAMP` member `CICRDO`, which is provided for use with the batch `RDO` utility `DFHCSDUP`.

We recommend to use these transaction and group names, but you can change them in accordance with your installation policies. Coordinate the group name and group list name with your CICS administrator. Replace `XYZLIST` with the name of your group list (`GRPLIST`).

While we recommend to use the default transaction ID `DTAX` for `ZDTPLT`, you can also use a custom transaction ID instead of `DTAX` in your definitions if you have conflicting transaction definitions.

### CICS startup program list table

Add the CICS startup program (`ZDTPLT`) after the `DFHDELIM` entry in your PLTPI source code and assemble the table.

This step is optional for test installations because the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") can be used instead to enable the module after CICS initialization. We recommend that you place the `ZDTPLT` entry immediately before the `TYPE=FINAL` specification.

The JCL procedure `DFHAUPLE` in `CICSHLQ.SDFHINST(DFHAUPLE)` can be used to build the PLTPI table.

An example of the PLTPI table that contains the CICS startup program

```
*



* PLT USED TO SUPPORT DYNATRACE CODE MODULE INITIALIZATION



*



DFHPLT TYPE=INITIAL,SUFFIX=SI



DFHPLT TYPE=ENTRY,PROGRAM=DFHDELIM



* Other PLT startup programs here...



DFHPLT TYPE=ENTRY,PROGRAM=ZDTPLT



DFHPLT TYPE=FINAL



END
```

Compuware Xpediter Global storage protection users

The PLT startup program (`ZDTPLT`) initializes the CICS module's exit work area, which CICS obtains on its behalf. Products such as Compuware Xpediter/CICS may be configured to enforce strict storage access controls and may abend `ZDTPLT` and prevent the CICS module from starting unless it is excluded from these controls. If you use the Xpediter/CICS global storage protection feature, add a `monitor exceptions` entry to the XDDBPINP DD in the CICS region JCL to exclude `ZDTPLT*`. For example:

```
DBPA 17.02 TRAN=*,PROGRAM=ZDTPLT*,CSECT=*
```

### CICS shutdown program list table

Add the CICS shutdown program (`ZDTPLTSD`) before the `DFHDELIM` entry in your PLTSD source code and assemble the table.

We recommend to place the `ZDTPLTSD` entry immediately after the `TYPE=INITIAL` specification.

The JCL procedure `DFHAUPLE` in `CICSHLQ.SDFHINST(DFHAUPLE)` can be used to build the PLTSD table.

An example of the PLTSD table that contains the CICS shutdown program

```
*



* PLT USED TO SUPPORT DYNATRACE CODE MODULE SHUTDOWN



*



DFHPLT TYPE=INITIAL,SUFFIX=SD



DFHPLT TYPE=ENTRY,PROGRAM=ZDTPLTSD



* Other PLT shutdown programs here...



DFHPLT TYPE=ENTRY,PROGRAM=DFHDELIM



DFHPLT TYPE=FINAL



END
```

### Connect the CICS module to a zDC subsystem

The PLT startup program (`ZDTPLT`) automatically connects to the default zDC subsystem at CICS region initialization.

If multiple zDCs subsystems are running, it connects to the zDC that specifies `DEFAULT(YES)`, unless an `INITPARM` override parameter in the CICS SYSIN parameters specifies that it must connect to a zDC with a particular name:

```
INITPARM=(ZDTPLT='MEPC,<option>'),
```

`<option>` sets the log level for the CICS module; see [Logging](#logging).

To verify the connectivity between the CICS module and the zDC subsystem, [send a ping message](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction#ping "Manage the CICS module via DTAX transactions.").

## Customization

### CICSPlex name grouping

You can group CICS regions belonging to the same CICSPlex into a single process group. To do so

1. Go to **Settings** > **Mainframe** > **Transaction monitoring**.
2. Turn on **Group CICS regions that belong to the same CICSPlex**.
3. Add `MASPLTWAIT(YES)` to your LMAS parameter. It instructs the CICS region to wait for the CICSPlex to become available before proceeding. If the CICSPlex isn't available, the module can't consider it.
4. Optional The `MASINITTIME(10)` timeout interal defaults to 10 minutes. You can customize it in the range of 5 minutes to 59 minutes.

If you enabled CICSPlex name grouping **after** the CICS region is up, you need to run the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") `DTAX DISABLE` and `DTAX ENABLE`.

### CICS web services support

The CICS module can trace the CICS web services invoked through a SOAP request or a JSON request (non-Java JSON pipeline). You need OneAgent version 1.257 or later to trace JSON requests.

To trace the CICS web service provider programs that are invoked by handler programs from CICS SOAP pipelines or from CICS non-Java JSON pipelines, update the provider pipeline config (`.xml`) file with `ZDTSOAPH` as shown below.

Only pipelines using the standard terminal handler are supported by Dynatrace. If you are running a non-standard terminal handler, it can be instrumented via the CICS and IMS SDK. As a starting point, you can use the following code samples:

* [ADKJSONAï»¿](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsona.txt)âCICS assembler example of starting paths for JSON requests in a user-written apphandler.
* [ADKJSONCï»¿](https://assets.dynatrace.com/global/doc/appmon/integrations-and-extensions/development-kits/agent-development-kit-adk/cics-and-ims-adk/adkjsonc.txt)âCICS COBOL example of starting paths for JSON requests in a user-written apphandler.

#### CICS SOAP pipeline

`DFHPITP` is the app handler program used in the CICS SOAP pipeline config that invokes the service provider programs. In addition to the `DFHPITP` in the pipeline, the CICS code module also supports user-written terminal programs.

Update your pipeline config file to include `ZDTSOAPH` in the `<headerprogram>` stanza under the SOAP handler element. Note that all SOAP pipelines have the SOAP handler element `<cics_soap_1.1_handler>` or `<cics_soap_1.2_handler>` where `ZDTSOAPH` is added. Below is a sample CICS SOAP provider pipeline updated with `ZDTSOAPH`.

To trace outbound SOAP requests that originate within CICS transactions that are traced by a CICS module, add the `<headerprogram>` stanza to the service requester pipeline definitions of those SOAP services that should be traced. Outbound SOAP requests that occur within CICS transactions that aren't traced are ignored. However, tracing isn't limited to requests from SOAP programs that act as CICS SOAP service providers.

```
<?xml version="1.0" encoding="EBCDIC-CP-US"?>



<provider_pipeline



xmlns="http://www.ibm.com/software/htp/cics/pipeline"



xmlns:xsi="http://www.w3.org/2001/XMLSchemainstance"



xsi:schemaLocation="http://www.ibm.com/software/htp/



cics/pipeline/provider.xsd ">



<service>



<terminal_handler>



<cics_soap_1.1_handler>



<headerprogram>



<program_name>ZDTSOAPH</program_name>



<namespace>*</namespace>



<localname>*</localname>



<mandatory>true</mandatory>



</headerprogram>



</cics_soap_1.1_handler>



</terminal_handler>



</service>



<apphandler>DFHPITP</apphandler>



</provider_pipeline>
```

#### OneAgent version 1.257+ CICS non-Java JSON pipeline

`DFHPIJT` is the terminal handler program used in the CICS non-Java JSON pipeline that invokes the service provider programs. To trace the CICS web service provider invoked through the non-Java JSON pipeline, update your pipeline config file to include `ZDTSOAPH` in the `<handler>` stanza under the `<default_http_transport_handler_list>` xml tags. Below is a sample CICS non-Java JSON provider pipeline updated with `ZDTSOAPH`.

```
<?xml version="1.0" encoding="EBCDIC-CP-US"?>



<provider_pipeline xmlns="http://www.ibm.com/software/htp/cics/pipeline">



<transport>



<default_http_transport_handler_list>



<handler>



<program>ZDTSOAPH</program><handler_parameter_list/>



</handler>



</default_http_transport_handler_list>



</transport>



<service>



<terminal_handler>



<handler>



<program>DFHPIJT</program><handler_parameter_list/>



</handler>



</terminal_handler>



</service>



</provider_pipeline>
```

### Route DTAX messages using TDQueue

Optional To route DTAX messages to the Dynatrace TDQueue (Transient Data Queue), use the `ZDTQ` resource definition provided above in your `CICRDO` member.

DTAX messages will only be written to the ZDTQ TDQueue if the queue is open. If you use the supplied resource definition, the queue remains closed due to the `OPENTIME(DEFERRED)` attribute. You can manually open it by using the `CEMT INQUIRE|SET TDQUEUE` command or you can set up the queue to open at initialization time, by modifying the TDQUEUE definition for ZDTQ to use the `OPENTIME(INITIAL)` attribute.

## Logging

You can control the CICS module log level either by using the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") or by specifying an optional `INITPARM` at CICS region startup.

```
INITPARM=(ZDTPLT='MEPC,<Option>'),
```

`<Option>` sets the logging level for CICS module. Accepted values are:

1. `FINE` | `F` for fine logging. We recommend to enable it only when the CICS module has difficulties during startup.
2. `INFO` | `I` for info logging. This is the default.
3. `WARNING` | `W` for warning messages logging.
4. `SEVERE` | `S` for severe messages logging.

```
Example:



INITPARM=(ZDTPLT='MEPC,SEVERE'),
```

There are two different sets of CICS logs:

* One set of messages occurs when the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") issues the `DISABLE` and `ENABLE` commands. These messages are written to the CICS CSMT Transient Data Queue(usually written to MSGUSR). View these messages in the CICS job spool. DTAX also writes a set of messages to the CEEOUT SYSOUT statement when errors occur in the connection between the zDC and the DTAX transaction. View these messages in the CICS Job spool. As long as the DTAX transaction can connect to the zDC, it logs its messages to the zRemote.
* The CICS module monitoring transaction activity routes its log messages to the zDC, and subsequently to the zRemote. The log shows if any corrupted distributed traces, timeouts, or other errors occurred. You may also see some statistical information in these logs.

You can access the CICS logs via the [zRemote logs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#logging "Prepare and install the zRemote for z/OS monitoring.").

## Update without region restart

To update your CICS module to a newer version without restarting the region

1. [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Download and install the Dynatrace product datasets for z/OS.") and [extract them](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Download and install the Dynatrace product datasets for z/OS.").
2. Use the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") to disable the CICS module in the CICS region with the `DISABLE` command.
3. Copy the CICS modules in the `SZDTLOAD` dataset into the Dynatrace `DFHRPL` dataset defined to your CICS region.
4. Use the CICS command `CEMT I PROG(ZDT*)` to display the CICS modules. Use the `SET PROG(ZDT*) NEWCOPY` command to tell CICS a new version of each program will be used.
5. Use the DTAX transaction to enable the CICS module with the `ENABLE` command. Verify that the new CICS module version is displayed on the DTAX panel.

## FAQ

How can I verify whether the CICS module and resources are installed correctly?

The group name might be different, as well as the two-character suffix representing the CICS release of the module (for example, CTS52 uses 69).

From the CICS region, look for these messages to validate the CICS module resources have been defined:

```
CICSAPPL Install for group XXXX has completed successfully.



CICSAPPL OWNER CSSY Resource definition for ZDTAGT72 has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTDC2 has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTDC2A has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTPLT has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTPLTSD has been added.



CICSAPPL OWNER CSSY Resource definition for ZDTSOAPH has been added.



CICSAPPL OWNER CSSY TRANSACTION definition entry for DTAX has been added.
```

How can I verify whether the CICS module PLT program is invoked?

The CICS module logs initialization messages to the zRemote log.

The zRemote log can be accessed from within Dynatrace, in the same manner as all the other module log files. Look for log entries similar to the following:

```
2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registering a pgi for the job: HVBAC021, host=10.30.220.41, groupId= f39f4801966aa7c7, pgir.groupInstanceID= fad6dee63cfd1522, hostID= 95c0bb0371704b8c, nodeID= fad6dee63cfd1522, groupName=HVBAC021, hostGroup=, processGroupType= 28



2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] Registered SubAgent[C021,51,32aa8d038887d1c9] with zDC[Z021,52], rc=true



2019-05-09 20:19:11.789 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021], subagentid[32aa8d038887d1c9] snaId[NETD    .HVBAC021], CICS release 54 was successfully registered with zdc[52] using protocol version=7.2.0, allocator=pooled.



2019-05-09 20:19:13.789 UTC [d37f9842] info    [native] ASID[52], smfID[S0W1], sysid[Z021], jobName[AFVBZ021] - ZDC955I  - Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021.



2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP008I - ZDTP008I ZDTAGT71.



2019-05-09 20:19:13.790 UTC [d37f9842] info    [native] ASID[51], smfID[S0W1], sysid[C021], jobName[HVBAC021] - ZDTP020I - ZDTP020I Active Sensors: MQ DB2 DB2R SOAP CTG DB2Fetch DLI DLIR HTTP .
```

What should I do if a CICS region cannot connect to the zDC?

Check the job log of the affected CICS regions for the following message, where `yyyy` is the subsystem ID of the zDC that the CICS region is trying to connect to. It might be blank if the CICS region is trying to connect to the default subsystem that is configured with the DEFAULT(YES) parameter. We recommend to simply search for the error message code.

```
ZDTP004W zDC yyyy unavailable
```

Verify that the zDC with that subsystem ID is started. If so, try to issue the [DTAX transaction](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.") command `ENABLE` to re-enable the connections.

How can I detect a version incompatibility?

Ensure that the CICS module version is less than or equal to zRemote module version. Don't connect newer CICS modules to older zRemote modules. Following is a sample message in the zRemote log when an CICS module version is incompatible with the zRemote version.

```
severe  [native] CICS14CR1[asid = 108] is trying to initialize with an invalid protocol version number : x.xxx.xx
```