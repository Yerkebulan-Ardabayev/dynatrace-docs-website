---
title: Customize the zDC subsystem
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc/customize-zdc
scraped: 2026-05-12T12:30:54.783659
---

# Customize the zDC subsystem

# Customize the zDC subsystem

* 8-min read
* Published Jul 22, 2016

Learn how to customize the zDC subsystem depending on your needs.

## z/OS MODIFY commands

The format of the [z/OS MODIFY commandï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=reference-modify-command) is defined as follows:

```
MODIFY <jobName or stcProcName>,DT1 <command>
```

The zDC subsystem supports the following z/OS MODIFY commands.

| Command | Description |
| --- | --- |
| DISPLAY | Displays Dynatrace subtask processor stats. |
| DTM%V | Forces display (ZDC952) of the utilization of the zLocal message queue. |
| LOG=? | Queries the log level of the zDC. |
| LOG=3 | Sets the log level of the zDC. Log level values range from `0` to `8`. The default value is `3`. Set the value to `4` to suppress informational messages. Values lower than `3` should be only used for diagnostic debugging. |
| START | Starts the zLocal. |
| STDO | Appends previously unreported lines from zLocal `stdo.log` to `SYSPRINT`. |
| STOP | Stops the zLocal. |
| ZLALOGLEVEL=INFO | Sets the log level of the zLocal. Log level values include `FINEST`, `FINER`, `FINE`, `CONFIG`, `INFO`, `WARNING`, `SEVERE`, `DEBUG`, and `NONE`. No default value. |

The `DISPLAY` command skips most rows with zero counters if the log level is at or higher than the default level of 3. To list the complete set of counters, you need to increase the log level to 1.

```
MODIFY MEPx,DT1 LOG=1



MODIFY MEPx,DT1 DISPLAY
```

A zDC sample output from `DISPLAY` with `LOG=1`.

```
14:13:33.854126 ZDC027I MODIFY COMMAND RECEIVED



14:13:33.857174 ZDC028I DT1 DISPLAY



14:13:33-977432 ZDC994I ShoS Counters



35:Msgs sent from MAgent to zDC using unnamed pipe



1:QUEUE_MAX_EVENTS(EQH)High watermark elements used



128:EQH queue elements defined



128:EQH elements currently free



0:Internal Performance:XmPosts avoided



0:Internal Performance:XmPost Skip DupSrbs



1,758:zDC Elapsed time (approx sec)



0: Bytes read from DTM Msgs



49:SMO Msgs written



34:Internal:Redundant Post bypassed



15:Internal:Attempt Rd=Wr cursor for vStorage Perf.



15:z/OS Unix has no ready Msgs, waiting for work



48:z/OS Unix Msgs read



3,808: Bytes read from SMO Msgs



2,267:TBC Total Transactional Buffers



2,267:TBC number in Free queue



25:TBC Msgs written



25:TBC Msgs read



10:TBC TBCs written



10:TBC TBCs read



10:TBC Post bypass



41:TBC No Ready Q



1,905:TBC Bytes written



1,905:TBC Bytes read



2:TBC Age<=PingDelay*.5



2:TBC Age<=PingDelay*.75



2:TBC Age<=PingDelay*1



2:TBC Age<=PingDelay*1.25



2:TBC Age>=PingDelay*1.25



10,485,760:DTMSG_SMOSIZE Bytes allocated



9,248:DTMSG_SMOSIZE Bytes used



14:13:36-712702 ZDC995W  DispTcb:     009D1438                0.900sec



14:13:36-712792 ZDC995W  DispTcb:     009BBAD0                0.577sec



14:13:36-712832 ZDC995W  DispTcb:     009BBCF0                0.013sec



14:13:36-712882 ZDC995W  DispTcb:     009BBE88                0.012sec



14:13:36-714022 ZDC995W  DispTcb:     009BE170                0.924sec



14:13:36-714062 ZDC995W  DispTcb:     009BE390                0.590sec



14:13:36-714112 ZDC995W  DispTcb:     009BE528                0.251sec
```

Rows that end with an exclamation mark (`!`) should have zero counts.

## Multiple TCP/IP stacks on a LPAR

An LPAR with multiple TCP/IP stacks requires an additional configuration step in the `ZDCMEPC` started task PROC from `SZDTSAMP`.

The `BPXTCAFF` program associates a specific TCP/IP stack with the current address space.

The `PARM` value is the job name that starts the desired TCP/IP stack.

```
//MEPC     PROC



...



//STEP0 EXEC PGM=BPXTCAFF,PARM='TCPIP_stack_name'



//*



//ZDCMAIN EXEC PGM=ZDCMAIN,REGION=0M,PARM='LANGUAGE=EN'



//STEPLIB   DD DISP=SHR,DSN=hlq.SZDTAUTH



//* Notes:



//* SYSPRINT is required in all cases.



//* SYSPRINT must be allocated to spool, not disk, on JES2 systems.



//* SYSPRIN3 is required on JES3 systems only.



//SYSPRINT  DD SYSOUT=*



//SYSPRIN3  DD SYSOUT=*



//SYSIN     DD DISP=SHR,DSN=hlq.SZDTSAMP(ZDCSYSIN)
```

## Multiple zDC/zRemote pairs on an LPAR

A zDC/zRemote pair connects the modules on a LPAR to a single Dynatrace environment. For example, it may be necessary to configure multiple zDC/zRemote pairs on an LPAR

* When you want to maintain different application groups in different Dynatrace environments.
* When you want to optimize your monitoring performance with high transaction volumes.

### Install an additional zDC/zRemote pair

1. Install an additional [zRemote module](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote#installation "Prepare and install the zRemote for z/OS monitoring.").
2. On your LPAR, copy the current JCL SYSIN member `ZDCSYSIN` to another name (for example, `ZDCSYSI2`).
3. Edit the new JCL SYSIN member by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



   DTAGTCMD(zremote=<ipaddress>[:port]



   name=zlocal_<lpar>)



   SUBSYSTEM_ID(<subsystem>)



   DEFAULT(NO)
   ```

   * Point `zremote=<ipaddress>[:port]` to the IP address and port of the new zRemote module.
   * Change `name=<zlocal_<lpar>>` to a new zLocal name.
   * Change `<subsystem>` to a new name.
   * Change `DEFAULT(YES)` to `DEFAULT(NO)`. The first zDC is designated as the default. Only one zDC per LPAR can specify `DEFAULT(YES)`. Additional zDCs fail to initialize unless they specify `DEFAULT(NO)`.
4. Make a copy of the current started task PROC and change the JCL SYSIN member to point to the new SYSIN member.
5. Start the new zDC and check if it connects to the new zRemote.

### Connect the modules to the new zDC

CICS module

IMS module

z/OS Java module

Create an `INITPARM` parameter override in the CICS system initialization to target the new zDC subsystem.

See [Connect CICS module to a zDC subsystem](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-cics#connect-cics-zdc "Install the Dynatrace CICS module.").

Change the `ZDC=` parameter in the injection utility parameters to target the new zDC subsystem.

See injection utility of [IMS control region](#install-ims-control-region).

Change the `ZdcName` parameter in the `dtconfig.json` file to target the new zDC subsystem.

See the [Download](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zos-java#download "Set up Java monitoring on z/OS using the Java module.") procedure of the z/OS Java module.

## Failover processing for zDC/zRemote

This is not load balancing.

The zDC subsystem can automatically switch to the next active zRemote module if a problem occurs with the primary zRemote.

zLocal version 1.1.0+ zRemote module version 1.261+ Once failover happens, and the secondary zRemote is connected, the zDC checks every 5 minutes to see if the primary zRemote is available. If not, the secondary zRemote connection remains intact, and the cycle starts anew. If the primary zRemote is available, the secondary zRemote is disconnected, and an immediate reconnect is attempted to the primary zRemote.

zLocal versions older than 1.1.0

Once failover happens, the ZDC remains connected to this next zRemote until this connection is broken. At that time, if the original zRemote is back online, a connection attempt will be made to it from the zDC. If the zDC is restarted, the original zRemote will be the initial connect attempt.

To use this behavior also for newer zLocal versions, set `zlaDisablePrimaryReconnect=true` in the `DTAGTCMD` SYSIN parameter.

The list of zRemote addresses used for failover processing is maintained in the JCL SYSIN member `ZDCSYSIN`. Edit it by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):

```
//SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



DTAGTCMD(zremote=<ipaddress>[:port];<ipaddress>[:port];<ipaddress>[:port]



nobootstrap=true)
```

* Set `zremote=<ipaddress>[:port]` to include a list of zRemote addresses.
* Set `nobootstrap=true` to disable automatic updates for the zLocal; they're not supported during failover processing.

  zLocal error message when attempting to update during failover processing

  ```
  severe  [native] Connection error (connect()/apr_sockaddr_info_get(), EDC9501I The name does not resolve for the supplied parameters.) while trying to bootstrap the zLocal.
  ```

### Update zLocal during failover processing

To update the zLocal during failover processing

1. Edit the JCL SYSIN member `ZDCSYSIN` by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



   DTAGTCMD(zremote=<ipaddress>[:port]



   nobootstrap=false)
   ```

   * Set `zremote=<ipaddress>[:port]` to the primary zRemote module.
   * Set `nobootstrap=false` to enable automatic updates for the zLocal.
2. Start the zDC. The bootstrapper `dtzagent` downloads the latest zLocal binary `libdtzagent.so` to the `/u/dt/agent/downloads/native/a.b.c.d/zos-s390-64` directory.
3. Copy the zLocal binary `libdtzagent.so` to the `/u/dt/agent/lib64` directory. Now the zDC is ready for failover processing with the latest zLocal binary.
4. Edit the JCL SYSIN member `ZDCSYSIN` by changing the following [SYSIN parameters](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#sysin-params "Set up the z/OS Data Collection subsystem (zDC)."):

   ```
   //SYSIN DD DISP=SHR,DSN=<hlq>.SZDTSAMP(ZDCSYSIN2)



   DTAGTCMD(zremote=<ipaddress>[:port];<ipaddress>[:port];<ipaddress>[:port]



   nobootstrap=true)
   ```

   * Set `zremote=<ipaddress>[:port]` to include a list of zRemote addresses.
   * Set `nobootstrap=true` to disable automatic updates for the zLocal.
5. Restart the zDC.

## Terminate the zDC

The zDC typically releases system resources (especially common storage) when it terminates due to a shutdown command or abnormal due to a cancel command or a program abend. Recovery (ESTAEX) routines are always in effect to trap abnormal terminations and to free all system resources.

However, there may be a situation where zDC can't be canceled due to a z/OS anomaly or failure, which precludes the functioning of the cancel command. If you want to terminate the zDC, try the commands below in the specified order until the zDC terminates. Go on to step 2 only if step 1 is unsuccessful, go on to step 3 only if step 2 is unsuccessful, and so on.

To avoid manually cleaning up system resources using the `ZDCDELET` process below, wait a short while between commands to permit dumps to be taken and system resources to be freed.

1. Issue the `STOP jobname` command.
2. Issue the `MODIFY jobname,SHUTDOWN IMMED` command.
3. Issue the `CANCEL jobname` command.
4. Issue the `FORCE jobname` command.

Attempt to restart the zDC. If the restart is successful, you can continue to run this job. If the restart is not successful and zDC indicates that it can't continue, you can execute the emergency zDC cleanup program named `ZDCDELET`.

`ZDCDELET` is a stand-alone job that attempts to terminate a specified zDC job and release all system resources held by a zDC process. The JCL to execute `ZDCDELET` is shown below:

```
//*



//* PLACE YOUR JOB STATEMENT HERE



//*



//DELETE EXEC PGM=ZDCDELET,PARM=xxxx



//STEPLIB DD DISP=SHR,DSN=<hlq>.R1nnnxx.SZDTAUTH
```

The `PARM=` on the `EXEC` statement must specify the 4-character subsystem name of the zDC process you want to terminate.

* User abends `100` and `101` may occur and messages describing the abends are written to the job log.
* User abend `100` indicates that the `PARM=` is not exactly 4 bytes long.
* User abend `101` indicates that the subsystem name specified on the `PARM=` operand can't be found in the system.
* Messages `ZDC400` through `ZDC403` may be written to the job log.

Refer to the [zDC user abends](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc#user-abends "Set up the z/OS Data Collection subsystem (zDC).") and [z/OS module messages](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Messages that are created by the Dynatrace z/OS modules.") for a list of all zDC messages.