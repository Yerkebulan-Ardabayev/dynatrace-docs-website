---
title: Install the zDC subsystem
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc
---

# Install the zDC subsystem

# Install the zDC subsystem

* 18-min read
* Updated on Feb 03, 2026

The z/OS Data Collection (zDC) subsystem interacts with the CICS, IMS, and z/OS Java modules via shared memory object (SMO) on a LPAR. The zDC subsystem maintains this SMO, and the modules write their monitoring data to it.

The zLocal (`libdtzagent.so`), hosted in the z/OS [Unix System Services﻿](https://www.ibm.com/docs/en/zos/2.5.0?topic=zos-unix-system-services) (USS) environment, runs as part of the zDC. It manages the TCP/IP socket connection to the zRemote module, reads monitoring data from SMO, and transfers these data to the zRemote.

The bootstrapper (`dtzagent`), hosted in the z/OS USS environment, runs as part of the zDC. It manages the update process of the zLocal.

When the zDC initializes (system startup or manual start), it starts the bootstrapper, and the bootstrapper starts the zLocal. When the zDC terminates, the zLocal and the bootstrapper are stopped.

## System security

The zDC (zLocal) uses TCP/IP socket connections, so it may be necessary to update your security system's access rules if they are configured to deny TCP/IP access by default.

The zDC doesn't limit which user IDs can enter operator commands.

You can control permissions assigned to files created by the zLocal and bootstrapper by setting `DT_UMASK`. The default is `umask(022)`.

## Installation

The zDC runs as an authorized z/OS process (typically as a system task). This means the programs must reside in an authorized library. It is intended to start automatically as a started task at a system IPL. This gives the zDC continuous availability to collect monitoring data from modules.

The zDC can also be run as a batch job. The service class of the zDC must be high enough so that it is always available for keep-alive messages from the zRemote. The zDC should have a priority higher than the monitored CICS and IMS regions.

A zDC subsystem must be installed on each LPAR you want to monitor.

1. [Download z/OS product datasets](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Download and install the Dynatrace product datasets for z/OS."). Make a note of the high-level qualifier used in the download procedure.
2. Create the RACF user ID for the zDC process. This ID must have a z/OS USS segment. The recommended home directory name is `/u/dt`.

   If a home directory other than `/u/dt` is set, change in step 8 the path to the bootstrapper, which defaults to `/u/dt/agent/lib64/dtzagent`. The path names below the home directory can't be changed.

   The home directory or the high-level qualifier that replaces it must be writeable by the zDC process.

   * It writes the zLocal binary to `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so`, where `a.b.c.d` is the version of the zLocal (i.e. 1.0.1.0).
   * It writes the zDC and zLocal logs to `/u/dt/log/dtxxx.log`.

   If write fails, the zDC processes use the directory `/tmp/dynaTrace`.

   If the zDC is run as a started task, the ID must be capable of representing the zDC started task and have access to the USS path above.
3. Change the dataset high-level qualifier represented by <hlq> in member `COPYAGNT` of `SZDTSAMP` to the value you used in the [Download z/OS product datasets](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Download and install the Dynatrace product datasets for z/OS.") procedure.
4. Run the `COPYAGNT` job to create the required z/OS USS subdirectories under the home directory of the zDC started task.
5. Copy the `dtzagent` binary from `SZDTSAMP` and set it to be executable.

   If you're using the default home directory of `/u/dt`, the resulting path is `/u/dt/agent/lib64/dtzagent`.

   If a home directory other than `/u/dt` is used, the path in this job must be changed accordingly. File and directory names are case-sensitive. The path names below the home directory can't be changed.

   The `COPYAGNT` job should run under the user ID that was created for the zDC process, so that user ID owns the `dtzagent` binary. If this is inconvenient, you can also use the `chown` and `chgrp` commands to reset the owning user and group for the `dtzagent` binary after running `COPYAGNT`.
6. Authorize `<hlq>.SZDTAUTH` where `<hlq>` is the high-level qualifier value you used in the [Download z/OS product datasets](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets "Download and install the Dynatrace product datasets for z/OS.") procedure.

   For example, create a member named `SYS1.PARMLIB(PROGDT)` containing:

   ```
   APF FORMAT(DYNAMIC)



   APF ADD DSNAME(<hlq>.SZDTAUTH) VOLUME(XXXXXX)
   ```

   Then issue the console command:

   ```
   SET PROG=DT
   ```
7. Copy the `ZDCMEPC` sample zDC started task PROC from `SZDTSAMP` to a system PROCLIB used for started tasks.

   The default name for the PROC is `MEPC`. Customize it as necessary for local standards. If a different subsystem name is chosen, change the `SUBSYSTEM_ID()` parameter in the [SYSIN parameters](#sysin-parameters) to match.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



   SUBSYSTEM_ID(MEPC)
   ```

   The PROC and the two JCL SYSIN members `ZDCSYSIN` and `ZDCMEPCA` that it uses contain dataset names that must be edited to replace `<hlq>.` with the appropriate high-level qualifiers.
8. Update the `DTAGTCMD()` parameter in the [SYSIN parameter](#sysin-parameters) to reflect your definitions.

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



   DTAGTCMD(/u/dt/agent/lib64/dtzagent



   nobootstrap=false



   zremote=<ipaddress>[:port])
   ```

   * `/u/dt/agent/lib64/dtzagent` sets the path to the bootstrapper. The default home directory name is `/u/dt`. If you have set a different home directory in step 2, change it accordingly.
   * `nobootstrap=false` enables the bootstrapper to automatically update the zLocal once a newer version is available. Per default, the zLocal receives automatic updates. Set `true` to disable automatic updates and [manually update the zLocal](#update-zlocal).
   * `zremote=<ipaddress>[:port]` set the IP address and port of a [installed zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring."). The IP address is required, the port is optional and defaults to 8898.
9. Verify that the appropriate exit is active, according to the OneAgent version.

   | OneAgent version | Exit(s) | Additional notes |
   | --- | --- | --- |
   | OneAgent version 1.300+ | U86 | * Required You need to be running z/OS 2.3 or later. * Required The U86 exit is required to report LPAR usage for DPS metrics and billing. + OneAgent version 1.300—OneAgent version 1.314: Dynatrace may suspend tracing without DPS metrics.   + OneAgent version 1.315+: Tracing will be automatically suspended if a `host.zos.msu_hours` metric is not received for 12 consecutive hours.  When this occurs, the following message is recorded in the zRemote log:  `Tracing has been disabled. The LPAR[LPAR] has not sent valid billing metrics.`  Tracing will be automatically re-enabled once valid `host.zos.msu_hours` metrics are received again. |
   | OneAgent version 1.300 and earlier | U83 |  |

   To verify that SMF exit U86 is active, run the following command:

   ```
   D SMF,O
   ```

   Look in the command output for `SUBSYS(STC,EXITS(IEFU83))` and `SYS(EXITS(IEFU83))`, or `SUBSYS(STC,EXITS(IEFU86))` and `SYS(EXITS(IEFU86))`.

   * If you find this, the SMF U83 and/or U86 exit is active. Go to the next step.
   * If you don't find this, you need to add it to your SMFPRMxx parmlib member.

     + U83:

       ```
       SUBSYS(STC,EXITS(IEFU83)
       ```
     + U86:

       ```
       SUBSYS(STC,EXITS(IEFU86)
       ```

     Then enable it.

     + U83:

       ```
       D PROG,EXIT,EN=SYS.IEFU83,DIAG
       ```
     + U86:

       ```
       D PROG,EXIT,EN=SYS.IEFU86,DIAG
       ```
10. Optional Add a command to your system startup to automatically start the zDC subsystem at IPL.
11. Use the `ZDCIVP` PROC in `SZDTSAMP` to verify the zDC installation and the zRemote connectivity.

    Good test for the zRemote connectivity returns `Connection timeout`, as the zRemote does not support FTP protocol. If a zRemote connectivity problem exist, it is indicated by `EDC8128I Connection refused`. This implies that the zRemote is not listening on the expected port.

    Step ZDCXVER - expect JOBLOG messages::

    ```
    JOBnnnnn  IEA630I  OPERATOR ZDCXVER  NOW ACTIVE,   SYSTEM=ZZZZ    , LU=



    JOBnnnnn  D SMF,O



    JOBnnnnn  IEA631I  OPERATOR ZDCXVER  NOW INACTIVE, SYSTEM=ZZZZ    , LU=



    JOBnnnnn  IEA630I  OPERATOR ZDCXVER  NOW ACTIVE,   SYSTEM=ZZZZ    , LU=



    JOBnnnnn  D PROG,EXIT,EXITNAME=SYS.IEFU86,DIAG



    JOBnnnnn  IEA631I  OPERATOR ZDCXVER  NOW INACTIVE, SYSTEM=ZZZZ    , LU=



    JOBnnnnn  IEA630I  OPERATOR ZDCXVER  NOW ACTIVE,   SYSTEM=ZZZZ    , LU=



    JOBnnnnn  D PROG,EXIT,EXITNAME=SYSSTC.IEFU86,DIAG
    ```

    Step ZDCXVER //SYSTSPRT spool - note special chars are for TSO 3270 formatting

    ```
    <3270> <Current Date/Time>



    <3270> Beginning of IEFU86 exit analysis......



    <3270> This routine inspects SMFPRMxx for active exits



    <3270> Also displays active ZDC information and release



    <3270> The status display should be all 'OK' for SM70(ZOSMETRICS) and DB2 performance metrics



    <3270> SYS.IEFU86 exit is active in SMFPRMxx



    <3270> STCSYS.IEFU86 exit is active in SMFPRMxx



    <3270> OK    ZDC Version is 1.vvv.0 ZDCSUBS(ZDTSMEPC)



    <3270> OK    SYS.EXIT(IEFU86) is active and is loaded at address: <hex>



    Note: Repeated for other zDCs
    ```

    Step SHOWIP //SYSTSPRT spool - Note: sample output

    ```
    Interface            Domain Port IP_ADDRESS



    OSA1I                AF_INET 0   172.23.243.82



    OSA2I                AF_INET 0   172.23.243.142



    IQDF0                AF_INET 0   10.250.250.82



    Interface Index  Interface



    65538            LOOPBACK



    65545            OSA1I



    65659            OSA2I



    65661            IQDF0



    Note: In this case, zDC PARM TCPIP_INTF() could specify OSA1I or OSA2I to set the LPARs IP address. This is usually used when a common VIPA address is used for the Sysplex. Without this parameter, the Dynatrace Hosts page may show multiple LPARs with the same IP address.
    ```

## Verify installation

After the installation is complete, verify its correctness.

### Verify the zDC started correctly

Verify that the zDC has started the correct version, initialized successfully, and has started the zLocal. Look for the following messages in `zDC SYSPRINT DD`.

```
ZDC000I INITIALIZATION STARTED FOR zDC  VER 1.195.00



ZDC052I zDC IS RUNNING ON Z/OS RELEASE 02.02.00



ZDC053I LPAR NAME IBMSYS1    CVTSNAME S0W1



.



.



.



.



ZDC955L Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021



ZDC958L Dynatrace INIT completed, ZDC AgentId received ZDC-Job/ID:AFVBZ021/Z021



ZDC993I Opn1RFD:0008  /u/labuser/adcdk/ci/7.2build/log/dt_Z021_Z021_33620108.0.log



ZDC955I Dynatrace connection being processed ZDC-Job/ID:AFVBZ021/Z021
```

If the following message appears in the zDC job log (your subsystem name might be different than `MEPC`), [restart the zDC](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#terminate-zdc "Customize the zDC subsystem.") with a different `SUBSYSTEM_ID` in the [SYSIN parameters](#sysin-parameters).

```
11:55:30.419083 ZDC006E SUBSYSTEM MEPC ALREADY EXISTS AND IS ACTIVE
```

### Verify the zLocal started correctly and connected to the zRemote

The zLocal writes log messages to the zDC SYSPRINT DD in addition to `/u/dt/log` in the z/OS USS environment. The zLocal log contains information relating to zLocal startup, versioning, and connectivity to the zRemote.

To verify that all the channels in zLocal are connected to the zRemote, look for the following messages in the SYSPRINT:

```
info    [native] dynaTrace z Remote Agent data channel connected successfully, performing handshake.



info    [native] dynaTrace z Remote Agent client handshake performed.



info    [native] dynaTrace z Remote Agent data channel handshake successful, version[rr.rr.rr.bbbb].



info    [native] dynaTrace z Remote Agent control channel connected successfully, performing handshake



info    [native] dynaTrace z Remote Agent handshakes are complete, all channels are fully operational.
```

Use the [z/OS MODIFY command](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#Thezos-modify-cmd "Customize the zDC subsystem.") below to instruct the zDC to display the zLocal status and to locate the log file paths of zLocal and zRemote.

```
MODIFY <zdc-jobname>,DT1 STDO
```

Once the zLocal log file is located, you can access it using the standard techniques. Use OMVS, ssh/telnet, or view it in the Dynatrace web UI like a regular OneAgent log file.

Also, look for the following messages in the corresponding zRemote log file (the values inside the bracket should reflect your live data).

```
info    [native] dynaTrace z Local Agent handshakes are complete, all channels are fully operational, version[rr.rr.rr.bbbb].



info    [native] Data client socket listener thread started



info    [native] ASID[48], smfID[S0W1], sysid[Z208], jobName[AF71Z208], subagentid[da57ff16] smfID.JobID[S0W1    .JOB92014], zDC release 65 was successfully initialized with protocol version=6.5.0



info    [native] zDC[Z208] SMO is initialized with size=10M.



info    [native] Registering the zdc[48]
```

### Check maintenance level of the zLocal load module

Browse the install library `<hlq>.R1nnnxx.SZDTAUTH`, where `<hlq>` is the high-level qualifier of the product dataset, to find the `ZDCDTAGT` load module for the zLocal.

In the header example below, you can see `1.nnn.00`, which indicates this is the version of the load module without any maintenance. When service is applied, the field contains a subversion number like `1.nnn.01`. The dates vary over time.

```
ZDCDTAGT 00000000 YYYYMMDD HH.MM VER 1.nnn.00 COPYRIGHT (C)...
```

The `ZDCDTAGT` load module can produce diagnostic messages in the following format:

```
ZDC99<n><i>
```

Where `n` is the log level, and `i` is the severity.

### Insufficient access authority message when starting the zDC

If the following messages (or something similar) appear in the zDC job log:

```
H408I USER(xxxxxxxx) GROUP(xxxx) NAME(STARTED TASK )



BPX.FILEATTR.PROGCTL CL(FACILITY)



INSUFFICIENT ACCESS AUTHORITY



ACCESS INTENT(READ ) ACCESS ALLOWED(NONE )
```

And the associated messages appear in the zLocal log file:

```
JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Server requests us to use Agent



dTMajor.dTMinorVersion.0.dTBuild with a hash of 0317af199c1ab1a03dda2cee90c2ea61



JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Requesting Agent library from Server



JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Error setting Agent library program



controlled: EDC5139I Operation not permitted.



JJJJ-MM-DD HH:MM:SS  3f8bbe02¨ info  native¨ Loading Agent



/dt/dynatrace-<dTMajor.dTMinorVersion.0>/agent/downloads/<dTMajor.dTMinorVersion.0.dTBuild>



/native/zos-s390-64/libdtzagent.so
```

These can be safely ignored.

After the initial download of the zLocal, the operating system tries to set a flag for the downloaded library that is needed in certain circumstances. The flag is not set during the second run because the library will not be downloaded anymore if it already exists.

## SYSIN dataset

All values that tailor the execution of the zDC reside in the dataset pointed to by `DDNAME SYSIN`. The sample started task PROC `ZDCMEPC` refers to the JCL SYSIN member `ZDCSYSIN` of `SZDTSAMP` as shown below:

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)
```

The dataset must contain 80 character records, blocked to a multiple of 80 bytes.

When you make any change to the SYSIN dataset, you must restart the zDC process for the change to take effect.

### SYSIN parameters

Positions 1 through 71 of each statement can contain parameter values. Positions 72 through 80 are ignored and can optionally contain a sequence number.

Each parameter uses `KEYWORD(value)` format. Each keyword and the requirements for the values associated with it are documented in the JCL SYSIN member `ZDCSYSIN` of `SZDTSAMP`.

If a parameter value spans multiple lines, specify the value through position 71 and continue the value on the next statement starting in position 1.

How can I add a comment to a statement?

If you want to use a comment, specify it by placing an asterisk in position 1 of a statement. The entire statement is considered part of the comment.

A comment can be enclosed between a slash-asterisk and an asterisk-slash.

```
/* This is a comment. */
```

Multiple lines can be contained within comments of this type.

| Parameter(default value) | Description |
| --- | --- |
| DTAGTCMD(/u/dt/agent/lib64/dtzagent) | Sets the path to the bootstrapper `dtzagent`.  Additional parameters:  * `nobootstrap=false` enables the bootstrapper to automatically update the zLocal once a newer version is available. Set `true` to disable automatic updates. * `zremote=<ipaddress>[:port]` sets the IP address and port of the [installed zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote "Prepare and install the zRemote for z/OS monitoring."). The IP address is required, the port is optional and defaults to 8898. * `name=zlocal_<lpar>` defines the name of the zLocal for log files. The name should reflect that this is a zLocal. It could include the SMF ID of the LPAR that it services. * `loglevel=<value>` sets the log level of the zLocal. Log level values include `FINEST`, `FINER`, `FINE`, `CONFIG`, `INFO`, `WARNING`, `SEVERE`, `DEBUG`, `NONE`). No default value. |
| SUBSYSTEM\_ID(MEPC) | Defines the name of the zDC subsystem. It must be four non-blank characters:  * The first character must be upper case alpha (A:Z). * The last three characters upper case alphanumeric (#,$,@,A:Z,0-9). |
| DEFAULT(YES) | Defines a zDC subsystem as default. Monitoring data is collected by the default zDC subsystem that defines `DEFAULT(YES)`. If you run multiple zDC subsystems on a single LPAR, you need to specify `DEFAULT(NO)` for each additional zDC, otherwise, they fail to initialize. |
| DISPLAY\_NAME() | Defines a display name for this zDC subsystem to identify it in certain log messages. |
| DTLOGLEVEL(3) | Sets the log level of the zDC. Log level values range from `0` to `8`. Set the value to `4` to suppress informational messages. Values lower than `3` should be only used for diagnostic debugging. |
| DTMSG\_SMOSIZE(1) | Sets the maximum amount of storage (MB) for messages that can be queued in the zDC shared memory object while awaiting writing to the z/OS modules. The default of 1 MB should be adequate in most cases when transaction buffering is enabled. When transaction buffering is disabled (not recommended), set the SMO size to 10 MB if very high volumes of transactions are traced. |
| DTCHDIR(/u/dt) | Changes the z/OS USS current directory where the bootstrapper `dtzagent` creates temporary files for `stdin`, `stdout`, and `stderr`. It defaults to the home directory of the associated user ID. |
| DTMSG\_TRANBUFSIZE(n,m) | Overrides the default number and size of transaction buffers. Transaction buffers offer better performance for CICS and IMS modules by placing event messages related to each distributed trace into dedicated buffers. Rather than send individual event messages for each distributed trace as they occur, they are blocked into one or more buffers and sent together. Additionally, the buffer of related messages is processed more efficiently by the zRemote.  The `n` parameter is the number of buffers in thousands. For example, 2 = 2,000 buffers. A zero value disables transaction buffers. The `m` parameter must be either `2` or `4` to specify a 2 K or 4 K buffer size. We recommend the 4 K buffer size, unless storage consumption is a significant concern. The minimum non-disabled value is `1,2`. The maximum is `126,4` or `248,2`, corresponding to a total size of 512 MB. An upper bound for the number of buffers that may be required is one for each IMS message region and MAXTASK times the number of CICS regions, but actual requirements are likely to be considerably smaller. |

## Logging

The log level of the zDC is set with the `DTLOGLEVEL()` parameter in the [SYSIN parameters](#sysin-parameters). You can change this log level dynamically by issuing a [z/OS MODIFY command](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#Thezos-modify-cmd "Customize the zDC subsystem.").

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



DTLOGLEVEL(3)



MODIFY <jobName>,DT1 LOG=1
```

View log message output in the zDC job spool. The job spool helps determine errors that may occur during the zDC startup or when connecting with the zRemote. Once the zDC successfully connects to the zRemote, error messages from the zDC subsystem and the CICS and IMS modules are routed to the zRemote.

The log level of the zLocal is set with the `DTAGTCMD(loglevel=INFO)` parameter in the [SYSIN parameters](#sysin-parameters). You can change this log level dynamically by issuing a [z/OS MODIFY command](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc#Thezos-modify-cmd "Customize the zDC subsystem."). The `DTAGTCMD(name=zlocal_<lpar>)` defines the name of the zLocal for log files. The name should reflect that this is a zLocal. It could include the SMF ID of the LPAR that it services.

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN)



DTAGTCMD(loglevel=INFO name=zlocal_<lpar>)



MODIFY <jobname>,DT1 ZLALOGLEVEL=FINE
```

There are two sets of logs created for the zLocal. Both are created in the OMVS file system. One set is a temporary set of logs only valid for the current execution of the zDC, and the location of these logs defaults to the home directory of the zDC user ID. You can override the location by using the `DTCHDIR()` parameter in the [SYSIN parameters](#sysin-parameters).

The zLocal also creates a standard set of logs, one for the bootstrapper, and one for the zLocal itself. These logs are in the standard Dynatrace log locations on the OMVS file system.

## Update and maintenance

1. [Download z/OS product datasets](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#download-pax "Download and install the Dynatrace product datasets for z/OS.") and [extract them](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#extract-datasets "Download and install the Dynatrace product datasets for z/OS.").
2. Update the zDC job to point to the new `<hlq>.SZDTAUTH`. If you have [defined an alias](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets#alias "Download and install the Dynatrace product datasets for z/OS."), redefine the alias. For example:

   ```
   DELETE 'DT.DYNTRC.SZDTAUTH' NOSCRATCH



   DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12710.SZDTAUTH'))
   ```

Updating the zDC subsystem from version 1.211 or earlier

A special handling is required to avoid abends in CICS regions that you're monitoring when updating the zDC subsystem from a version 1.211 or earlier.

1. Stop the zDC.
2. Wait for **15 minutes** for the CICS module to reset and clean up the control blocks.
3. Update the zDC to the newer version.
4. Start the zDC.

### zLocal

By default, the zLocal receives automatic updates if `DTAGTCMD(nobootstrap=false)` is set in the [SYSIN parameters](#sysin-parameters). At every start of the zDC, the bootstrapper queries the zRemote module for available updates. The latest zLocal is installed as part of the zRemote installation. If an update is available, the zLocal will be automatically downloaded from the zRemote and updated.

Log message examples in the zDC job output in case of automatic updates

```
info    (native) The bootstrap channel connected successfully, requesting version: a.b.c.d



info    (native) Interprocess lock acquired for /u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so



info    (native) Fetching agent binary succeeded for /u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so
```

### Manually update the zLocal

* Don't use the manual update process for the zLocal when connecting the first time to your Dynatrace environment because the zDC won't start successfully.
* The zRemote module must be running when starting the zDC for the first time to avoid a `U103` [user abend](#user-abends).

Suppose you don't want to receive automatic updates for the zLocal, set `DTAGTCMD(nobootstrap=true)` in the [SYSIN parameters](#sysin-parameters). For the manual update process, the zLocal binary `libdtzagent.so` must be present on the LPAR in the `/u/dt/agent/lib64` directory.

To accomplish this

1. Run the bootstrapper `dtzagent` at least once in either a production LPAR or non-production LPAR.
2. Copy the zLocal binary to the target LPAR. In the `SZDTSAMP` dataset, the member `OCOPYAGT` is a job that copies the zLocal binary `libdtzagent.so` to the `/u/dt/agent/lib64` directory.
3. Complete the instructions to start the zDC and connect it to your Dynatrace environment.
4. If the zDC successfully connects to Dynatrace, `libdtzagent.so` is copied to the `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64/libdtzagent.so` directory, where `a.b.c.d` is the version of the zLocal (i.e. 1.0.1.0)

Log message examples in the zDC job output in case of manual updates

```
info    (native) Configured to not download module - loading local module



info    (native) Start loading local agent binary



info    (native) Successfully loaded agent binary /u/dt/agent/lib64/libdtzagent.so
```

## zDC user abends

A zDC may terminate with a user abend due to internal errors and initialization failures. All user abends, except for `U103` and `U106`, create a dump file. See the list of possible user abends below.

| Abend | Description |
| --- | --- |
| U100 | An internal error occurred due to zDC initialization failure. |
| U101 | zDC initialization failed and is unable to display the failure message. |
| U102 | ECSA storage is not available for the zDC. |
| U103 | A problem occurred during a RETRY operation from a recovery exit routine. |
| U104 | A queue task ended abnormally. This abend is accompanied by a `ZDC066E` message in the SYSLOG. |
| U105 | A queue task ended abnormally while shutdown was NOT in progress. |
| U106 | A fatal error occurred in TCPSP routine. |
| U110 | This abend might occur for various internal error reasons. It is accompanied by one of the following zDC error messages in the SYSLOG:  * `ZDC988E` * `ZDC987E` * `ZDC985E` * `ZDC984E` * `ZDC983E` * `ZDC982E` * `ZDC981E` * `ZDC988E` * `ZDC982E` * `ZDC981E` * `ZDC979E` * `ZDC978E` |
| U111 | An internal error occurred in one of the zDC modules. The abend is accompanied by one of the following error messages in the SYSLOG:  * `AgtSt:DqrIErr-Get Token/Name for FML failed` * `AgtSt:DqrILod LOAD failed` * `AgtSt:Waiting for Que Data Space failed-Abort` |
| U205 | The zDC is unable to open SYSPRINT or SYSPRIN3 DD for displaying log messages. |
| U222 | An internal error occurred in one of the zDC modules. The abend is accompanied by one of the following messages in the SYSLOG:  * `066E IEAVRLS Error limit!` * `066E Freed dead TBC Error-Abend222` |

## Troubleshooting

* [zDC subsystem troubleshooting﻿](https://dt-url.net/al03k4i)