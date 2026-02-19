---
title: Install the IMS module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-ims
scraped: 2026-02-19T21:19:12.796059
---

# Install the IMS module

# Install the IMS module

* Latest Dynatrace
* 21-min read
* Updated on Nov 18, 2025

With the IMS module, you can get observability for your IMS transactions and programs including IBM MQ and database calls.

Observability for

Including

Transactions

* IMS
* Fast Path
* [BMPï»¿](https://www.ibm.com/docs/en/ims/15.1.0?topic=bmps-batch-message-processing-transaction-oriented)

Transactions initiated using

* IBM MQ Bridge and Trigger Monitor
* IMS TM Resource Adapter, IMS SOAP Gateway, and IMS Connect
* 3270 terminal

Database calls

Database calls with their SQL statements from IMS to Db2 and IMS DB via

* the DL/I access method
* the Fast Path access methods

## Installation

The IMS module captures data on various IMS transaction processing events and forwards monitoring data to the zDC subsystem via shared buffers.

To install the Dynatrace IMS module:

1. Install the IMS module into the Control Region of each IMS DB/DC and DCCTL system that you want to monitor. This is enough to cover all message processing regions associated with the Control Region.
   Note that installing the IMS module into a DBCTL only system is not supported.
2. You need to add the Dynatrace exit to each IMS Connect that you want to monitor.
3. You need to add the [z/OS Java module](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#middleware "Set up Java monitoring on z/OS using the Java module.") to each IMS SOAP Gateway you want to monitor.

IMS restart

4. You must re-execute the injection job after each IMS restart. For more details, see the [Injection notes](#injection-notes).

### Updating a previously installed version of Dynatrace

If you have Dynatrace installed and are upgrading to a newer release, you can jump to section [Update without region restart](#update) later in this document.

### IMS Connect

Add the authorized Dynatrace dataset `<hlq>.SZDTAUTH` to the IMS Connect job STEPLIB to permit IMS Connect to load the Dynatrace exit HWSTECL0.

* If you use IMS Connect Extensions, concatenate SZDTAUTH after the IMS Connect Extensions library.
* If you use a locally developed HWSTECL0 exit, concatenate SZDTAUTH ahead of the dataset that contains the local exit.

The IMS Connect exit can be enabled to create PurePath nodes in a distributed trace. Activate the required [OneAgent feature](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.") **z/OS IMS Connect**.

* If the IMS Connect exit is configured to create PurePath nodes, the exit will connect to the default zDC subsystem name. The target zDC subsystem name can be overridden by specifying the following DDNAME and keyword parameter in the IMS Connect startup JCL:

```
//ZDTPARMS DD *



ZDCID=<zDC_Id>
```

The IMS Connect exit is required to support the IMS Connect API protocol and to support the IMS SOAP Gateway in cases when the SOAP Gateway has not been configured to insert a tracking ID using the `iogmgmt` tracking command.

### IMS Control region

You must run the Injection Utility to install the IMS module into the control region.

1. Authorize `<hlq>.SZDTAUTH` by adding it to the APF list
2. Run the ZDTINST job from the `<hlq>.SZDTSAMP` PDS.

Detail information on the parameters can also be found in the ZDTINST PDS member.

Sample JCL with positional parameters:

```
//S1       EXEC PGM=ZDTIINST,PARM='<IMS_Id>,<zDC_Id>'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

Sample JCL with keyword parameters:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=<IMS_Id>



ZDC=<zDC_Id>
```

The injection utility (ZDTIINST) supports changing the size of `pathid` tables without requiring an IMS restart and re-injection of the module. A path table size can be changed by using the `M` action code with a path table segment specification as the sixth parameter and, optionally, the target IMSID as the seventh parameter.

Below is the complete list and description of the positional parameters of the injection utility. All parameters must be upper case:

```
// ...    PARM='<IMS_Id>,<zDC_Id>,<ActionCode>|<PathTableSize>,



<WaitZdcMin>,<Y|N>,<PathTableSegm>,<PathTableIms>'
```

The injection utility parameters can be specified as either positional or keyword parameters. There are seven positional parameters. Keyword parameters must be specified in a SYSIN file. The positional parameters on the EXEC JCL statement are still valid, however any new parameters added in the future will only be added as SYSIN keyword values. If an EXEC PARM parameter value is found, no SYSIN parameters will be considered. The recommended method is to use a SYSIN file and keyword parameters.

Symbol

Position

Keyword

Description

Required

`<IMS_Id>`

1

IMSID=

The four-character IMSID of the control region.

This parameter is not needed when you're using the garbage collection function to reclaim ECSA storage that contains no longer used IMS modules.

Required

`<zDC_Id>`

2

ZDC=

The four-character zDCID used in the SUBSYSTEM\_ID() parameter of the target zDC.

This parameter is not needed when the requested target zDC is the DEFAULT zDC. In that case type in the asterisk (`*`) or omit the parameter.

Required

`<ActionCode>|<PathTableSize>`

3

ACTION= | SIZE=

The one-character action code or the value for `pathid` table size.

#### Action code

Action codes specify an action to be taken on the previously injected IMS module. An action code is not applicable to the initial injection of the IMS module and is mutually exclusive with the `pathid` table size value.

If a valid action code is specified, the injection program doesn't re-inject the IMS module and performs the specified action on the already injected module. This means that no new versions of the IMS modules will be loaded.

Action codes are:

* **E**: Enable (switch on) an injected IMS module that was previously disabled.
* **D**: Disable (switch off) an injected IMS module. The IMS module is no longer invoked. Use the `E` action code to re-enable it.
* **G**: Garbage collection. If the IMS module has been updated and injected, ECSA storage for the old (unused) load modules of the IMS module is reclaimed with this function. See the [Garbage collection notes](#gc-notes) section for more information.
* **M**: Modify the recovery option of the injected IMS module when this value is used in conjunction with the fifth parameter, `<Y|N>`.  
  Alternatively, modify the size of any previously allocated path tables, when used in conjunction with the sixth parameter `<PathTableSegm>`, and optionally the seventh parameter `<PathTableIms>`.  
  Alternatively, modify the size of any previously allocated Fast Path SMO (Shared Memory Object) when used in conjunction with the `FPATHSIZE=` statement.
* **F**: Free all resource locks and reset the `pathid` table pointers. This action code should never be used unless the `E` action has failed because a IMS module resource is locked or as directed by Dynatrace Support.

#### Table size value

The `pathid` tables size value is used for the initial IMS module injection and is mutually exclusive with actions codes. If the IMS module is already injected, the table size value is ignored.

The table size value can be expressed as SEGM=nnnn, where nnnn is up to a 4 digit number of 1-megabyte segments

The actual number of usable entries may be higher, as the storage is allocated above the specified quota. The number of entries will be adjusted upwards to use all available allocated storage.

If the parameter is omitted upon initial IMS module injection, a default of four segments (4 MB) is used. This provides space for 8,191 entries (approximately 2,048 entries per segment).

The number of allocated entries should correspond to the expected number of IMS distributed traces during any one-minute interval. When the number of traced IMS transactions exceeds the number of available table slots, new distributed traces are not recorded.

#### No third parameter specified

If no third parameter is set, the injection program injects the IMS module.

You can also use this option to update the IMS module. In that case existing table size will remain intact.

Optional

`<WaitZdcMin>`

4

ZDCWAIT=

The wait time for the target zDC to initialize, in minutes (max two digits).

The default value is 30 minutes. The target zDC must have been initialized at least once since the last system IPL before the IMS module can complete initialization.

Optional

`<Y|N>`

5

DUMP=

Indicates whether the IMS module should capture an SVC dump when ABEND recovery is driven.

This parameter can be specified during initial injection of the IMS module or in conjunction with the `M` or `E` action codes (parameter number 3) to toggle on/off the dump capture during recovery for the previously injected IMS module.

The default value is `Y`, which means dump capture is enabled.

Optional

`<PathTableSegm>`

6

SEGM=

The value that resizes `pathid` tables.

This parameter is only applicable in conjunction with the `M` action code (parameter number 3). The format of value is `SEGM=nnnn`, where `nnnn` is the number (up to 4 digits) of 1-megabyte segments.

Optional

`<PathTableIms>`

7

PATHIMS=

The value (up to 4 characters) that specifies the IMSID for which the pathid table is to be resized.

This parameter is only applicable in conjunction with the `M` action code (parameter number 3) and the `<PathTableSegm>` value (parameter number 6).

If an IMSID is specified, only the pathid table for that IMS is resized.  
If the parameter is omitted, only the `pathid` table for the local IMS (specified as parameter number 1) is resized.  
If the asterisk (`*`) is specified, the `pathid` table for the local IMS **and** `pathid` tables allocated locally for all remote IMSIDs are resized.

Optional

n/a

n/a

REMOTESEGM=

Sets the number of segments to use when allocating remote pathid tables. The format of the value is `REMOTESEGM=nnnn`, where `nnnn` is the number (up to 4 digits) of 1-megabyte segments.

The parameter is optional, valid only as a `SYSIN` parameter, and ignored when the `ACTION=` keyword is specified. When omitted, the default value of `4` megabytes is used.

This parameter doesn't change the size of any existing remote pathid tables. To change the allocation of an existing remote pathid table you must use the `ACTION=M`, `SEGM=`, and `PATHIMS=` keywords.

Optional

Example 1. Inject the IMS module into IMS IB01 for zDC ZDC1.

Accept the default `PathTableSize` and wait for up to 20 minutes for ZDC1 to initialize.

With positional parameter:

Note that the third positional parameter is not specified.

```
//S1       EXEC PGM=ZDTIINST,PARM='IB01,ZDC1,,20'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IB01



ZDC=ZDC1



ZDCWAIT=20
```

Example 2. Disable the IMS module previously injected into IMSB for zDC ZDC1.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSB,ZDC1,D'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSB



ZDC=ZDC1



ACTION=D
```

Example 3. Enable the previously injected, but disabled IMS module in IMSB for zDC ZDC1.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSB,ZDC1,E'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSB



ZDC=ZDC1



ACTION=E
```

Example 4. Inject the IMS module into IMS IMSA for zDC ZDC1.

Specify that IMS module ABEND recovery should also capture an SVC dump.

With positional parameter:

Accept the defaults for the third and fourth parameters.

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,,,Y'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



DUMP=Y
```

Example 5. Set IMS module ABEND recovery dump capture off for a previously injected IMS module.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,M,,N'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



DUMP=N
```

Example 6. Change the size of the path table for the local IMS.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,M,,,SEGM=3'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



SEGM=3
```

Example 7: Change the size of the path table for IMS IMSB which is a remote IMS to IMSA.

With positional parameter:

```
//S1       EXEC PGM=ZDTIINST,PARM='IMSA,ZDC1,M,,,SEGM=1,IMSB'



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH
```

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



SEGM=1



PATHIMS=IMSB
```

Example 8: Inject and set the remote pathid table size to 2 megabytes.

Use the `REMOTESEGM=2` parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



REMOTESEGM=2
```

### Fast Path transaction tracing

Symbol

Position

Keyword

Description

Required

n/a

n/a

FPATH=

Indicates whether to activate Fast Path transaction tracing:

* **Y**: Inject and enable Fast Path hooks. Enables hooks that are injected but disabled.
* **N** (Default): Does not inject Fast Path hooks. Disables hooks that are injected and enabled.

Valid only as a SYSIN parameter and only for IMS Version 15 or later.

If omitted or specified incorrectly, no action is taken.

Optional

n/a

n/a

FPATHSIZE=

The size of the Fast Path SMO (Shared Memory Object) for Fast Path transaction tracing, in 1 MB segments. The range is `1`-`9999`. The default is `4`.

This value can be used on the initial injection of the IMS module, or in conjunction with a modify action statement (`ACTION=M`) to resize the Fast Path SMO.

Valid only as a SYSIN parameter and only for IMS Version 15 or later.

Optional

Example 9: Inject and enable Fast Path transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



FPATH=Y
```

Example 10: Disable Fast Path transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



FPATH=N
```

Example 11: Inject and enable Fast Path transaction tracing and override the default SMO size of 4 megabytes.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



FPATH=Y



FPATHSIZE=8
```

Example 12: Change the size of the Fast Path SMO post injection.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



ACTION=M



FPATHSIZE=2
```

### BMP transaction tracing

IMS module version 1.259+

Symbol

Position

Keyword

Description

Required

n/a

n/a

BMP=

Indicates whether to activate transaction tracing for BMP regions:

* **Y**: Enables transaction tracing for BMP regions.
* **N** (Default): Disables transaction tracing for BMP regions.

Valid only as a SYSIN parameter.

If omitted or specified incorrectly, BMP transaction tracing will be disabled.

Optional

## BMP transaction tracing notes

Automatic tracking for transaction-oriented BMPs (message input is from the IMS message queues) will be the same as currently exists for MPP/IFP regions: if the input message is being tracked by a control region sensor, a path will be started for the transaction in the BMP region.
Automatic tracking for work performed by batch (non-transaction oriented) BMPs can only be done if the input message is via an MQGET (see restrictions below). Otherwise, batch BMP support means the agent performs initialization services for the BMP region (allocates work areas and places sensors) but does not start any paths.
For both transaction-oriented and batch BMPs, a path is started for the BMP region whenever the application issues an MQGET, provided all of the following are true:

1. Instrumentation is enabled for the z/OS IMS MPR MQ filter in the UI Settings.
2. Another sensor has not already started a path for the BMP region.
3. The MQ queue name for the MQGET is included or not excluded by its presence or absence from the IMS MQ filters list (**Settings** > **Mainframe** > **IBM MQ Filters**).
4. A DL/I CHKP call is made before the first MQGET. This is only required for batch-oriented BMPs.

For both transaction-oriented and batch BMPs, the SDK can be used to instrument the application to send the event messages to start and end paths.
There is no capability to limit the tracking to specific BMP job names or PSBs or to track batch work other than IMS BMPs.

Example 13: Enable BMP transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



BMP=Y
```

Example 14: Disable BMP transaction tracing.

With keyword parameter:

```
//S1       EXEC PGM=ZDTIINST



//STEPLIB  DD DISP=SHR,DSN=<hlq>.SZDTAUTH



//SYSIN DD *



IMSID=IMSA



ZDC=ZDC1



BMP=N
```

## Garbage collection notes

When updating the IMS module you can reclaim ECSA storage used by the old version of the IMS module.

After the injection job for the updated IMS module is run, IMS Message Region activity is necessary to update internal control blocks to point to the new version of the IMS module. After that, you can re-run the injection job with the `G` action code set in parameter number 3. This marks the old version of the IMS module as a candidate for deletion.

After at least 3 hours, run the injection job with the `G` action code set in parameter number 3 once again. This releases the ECSA storage containing the old version of the IMS module.

You can run the injection job with the `G` action code set in parameter number 3 repeatedly; there is no negative side effect to doing so. But in order to have the garbage collection process reclaim unused module storage, the process must be invoked at least twice after an IPL, with at least 3 hours between the first and second invocation.

## Injection notes

Start the zDC at least once after the system IPL before executing the IMS module injection job.

If the target zDC has not been up since the last IPL, the injection job waits for it to come up. The wait time defaults to 30 minutes but can be set by the `<WaitZdcMin>` parameter. If the zDC is still not up after this time then injection cannot proceed and the injection job terminates with user `ABEND` code of 100.

If the zDC has been up at least once since the last system IPL, the injection job can complete even when the zDC is not currently up. In this case warning messages are issued indicating that the zDC is not started and data collection is not available, and the injection job completes with `RC=4`.

Start and fully initialize the IMS system before you execute the IMS module injection job. If you stop and start the IMS system, the injection job must be re-run. If you start a new IMS-dependent region or stop and restart one, no action is required.

When the IMS module is updated in a previously injected IMS, re-execute the IMS module injection job to pick up the updated IMS module load modules. Do not specify an action code for the injection job in parameter number 3. The IMS **does not** require a restart after the IMS module update.

We recommend that you use an automation facility like IMS Time-Controlled Operations (TCO) to execute the IMS module injection job.

All IMS module injection messages are written to the job log. You can control the level of messages by including specific DDNAMEs in the injection job JCL. If no DDNAMEs are included, the default is level 4 for informational messages. The specific DDNAMEs and message levels are the following:

* `//DTMSGLV0 DD SYSOUT=*` For finest level 0 DEBUG messages and above
* `//DTMSGLV2 DD SYSOUT=*` For fine level 2 DEBUG messages and above
* `//DTMSGLV4 DD SYSOUT=*` For informational level 4 messages and above
* `//DTMSGLV5 DD SYSOUT=*` For warning level 5 messages and above

Injection job failures typically result in a user `ABEND` code of 100. In most cases, the cause of failure can be determined by prior diagnostic messages that have been written to SYSPRINT.

Depending on your z/OS system parameters, a symptom dump may also be written to the job log, but a dump is not captured unless one of the following DDNAMEs is included in the injection job JCL:

```
//SYSABEND DD SYSOUT=*



//SYSMDUMP DD DSN=DT.IMSAGENT.INJECT.SDUMP,DISP=(OLD,KEEP,KEEP)
```

Both sample JCL members ZDTINST (injection utility) and ZDTIDIAG (diagnostic utility) contain a final step to execute procedure ZDTZLOGC. The function of the ZDTZLOGC step is to copy the job's spool output to an HFS log file so that it will automatically be included in a support archive. There is a new JCL procedure (ZDTZLOGC), REXX program (ZDTZLOGR), and assembler program (ZDTZLOGS) included for this function. To implement it do the following:

1. Copy sample JCL member ZDTZLOGC to a PDS to contain the modified JCL. Within the JCL PROC the DSN for the DD names SYSEXEC and SZDTAUTH must be changed.  
   `//SYSEXEC DD DISP=SHR,DSN=<hlq>.SZDTSAMP` <- change `DSN` to where `REXX` exec `ZDTZLOGR` resides (see step 3)  
   `//SZDTAUTH DD DISP=SHR,DSN=<hlq>.SZDTAUTH` <- change `DSN` to where program `ZDTZLOGS` resides
2. Both sample members ZDTINST and ZDTIDIAG contain a JCLLIB statement that must be changed and the ZDTZLOGC proc step must have the `<ZDC Id>` supplied.  
   `JCLLIB ORDER=(<hlq>.SZDTSAMP)` <- change `DSN` to where the `ZDTZLOGC` JCL proc resides (see step 1)  
   `//ZDTZLOGC EXEC ZDTZLOGC,ZDC='<ZDC Id>',COND=(EVEN)` <- change ZDC Id (for example, `MEPC` or `*` for default zDC)

## Logging

There are two sets of IMS module logs.

* The first set of IMS messages comes from the IMS injection job. These are messages that occur during injection of the module into the IMS control region. These messages only appear in the job spool of the IMS module injection job.
* The second set of IMS messages comes from the IMS module as it monitors IMS activity. These messages are sent to the zDC and then are routed to the zRemote.

You can access the IMS module logs via the [zRemote logs](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#logging "Prepare and install the zRemote for z/OS monitoring.").

## Update without region restart

To update your IMS module to a newer version without restarting the region

1. [Download z/OS product datasets](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Download and install the Dynatrace product datasets for z/OS.") and [extract them](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Download and install the Dynatrace product datasets for z/OS.").
2. Update the injection job to point to the new `<hlq>.SZDTAUTH`. If you have [defined an alias](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#alias "Download and install the Dynatrace product datasets for z/OS."), redefine the alias. For example:

   ```
   DELETE 'DT.DYNTRC.SZDTAUTH' NOSCRATCH



   DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12710.SZDTAUTH'))
   ```
3. Run the injection job without the action code to pick up the updated IMS module. For more details, see the [Injection notes](#injection-notes).
4. To recover the ECSA used by the old version of the IMS module see section [Garbage collection notes](#gc-notes).

## FAQ

How can I deactivate the IMS module?

If an ABEND occurs in the IMS module, the recovery process produces ABEND diagnostics if possible, and then it disables the IMS module. The IMS system continues to function. When this occurs, a series of WTO messages are written to the system log for the IMS control region and/or IMS dependent region. A sample normal message set follows:

```
ZDTI032W Recovery routine entered.



ZDTI036W ZDTIII15 0000000 20221103 10.51 VER 1.255.0 ABEND at offset 007874.



ZDTI033W Successful ABEND recovery, agent disabled.
```

Different or additional messages might be issued if abnormal conditions are encountered by the recovery process (for example, when dynamic storage cannot be obtained, retry is not permitted, or no SDWA was passed). All of the messages related to the ABEND recovery process are documented in the [z/OS module messages](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Messages that are created by the Dynatrace z/OS modules.") section.

A Software (SFT) Error Record further describing the ABEND is usually written to the z/OS system SYS1.LOGREC data set. You should run the z/OS EREP utility program to print the Software (SFT) Error Record associated with the ABEND.

Optionally, an SVC dump might be taken during recovery, depending on the ABEND recovery option specified or defaulted to when the IMS module was injected. The default action is to capture an SVC dump when ABEND recovery is driven. This option can be specified as a parameter when the IMS module is initially injected or specified in conjunction with the Modify or Enable function parameters to toggle dump capture during recovery on or off for a previously injected IMS module.

When the IMS module is disabled as a result of the ABEND recovery process, it remains disabled until explicitly reenabled using the IMS module injection program.

How can I detect a version incompatibility?

Ensure that the IMS module version is less than or equal to zRemote module version. Don't connect newer IMS modules to older zRemote modules. Following is a sample message in the zRemote log when an IMS module version is incompatible with the zRemote version.

```
severe  [native] IMS14CR1[asid = 108] is trying to initialize with an invalid protocol version number : x.xxx.xx
```