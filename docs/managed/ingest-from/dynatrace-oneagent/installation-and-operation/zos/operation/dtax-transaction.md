---
title: Manage the CICS module via DTAX transactions
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction
scraped: 2026-05-12T12:04:54.968352
---

# Manage the CICS module via DTAX transactions

# Manage the CICS module via DTAX transactions

* 4-min read
* Published Jul 22, 2016

These functions are primarily intended to be used for troubleshooting purposes. None of them are required for normal operation, but you may wish to automate CICS module enablement by submitting `DTAX ENABLE` and `DTAX DISABLE` transactions through an operations automation system like CAFC or z/OS modify commands. CICS modify commands for DTAX return messages to CSMT TD queue and to the z/OS system log. A `DTAX STATUS` modify command is available to see if the Dynatrace CICS HOOKS/EXITS are enabled. This command outputs a `ZDTP030I` message to the z/OS console. See [z/OS module messages](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Messages that are created by the Dynatrace z/OS modules.") for a full description of the output.

The DTAX transaction runs automatically every 5 minutes. It initializes the CICS module connection to a newly started or restarted zDC at that time. Because data is only collected while the zDC is active, it should be running prior to CICS or IMS region initialization. In addition, data may be lost for up to 5 minutes after the zDC is restarted or when the zDC is initially started after the CICS region initializes. Optionally, the reconnection process can be completed immediately by manually entering the DTAX transaction and performing the `DISABLE` function followed by the `ENABLE` function after reinitializing the zDC. Use the `ENABLE` function alone if the CICS region had not been connected to a zDC and thus shows a `DISABLED` status.

The DTAX transaction also provides a UI to access basic functionality of the CICS module. Logon to CICS and issue the DTAX transaction without parameters for a brief description of its functions and current module status.

![DTAX main menu](https://dt-cdn.net/images/dtax-panel-dt-3199-cf520f3ba8.png)

DTAX main menu

## Change the log level

The log level of the CICS module is set to **Info** and, unlike the other modules, it cannot be changed within Dynatrace. It can, however, be changed using the DTAX transaction. Set the cursor to the upper right corner and type one of the following log levels: **Severe**, **Warning**, **Info**(Default) or **Fine**.

## Send a ping message

You can use the ping message functionality to verify the connectivity between the CICS module and the zRemote module.

Execute the DTAX transaction with the parameter `PING`.

```
DTAX Ping
```

Verify that the `PING` traveled from CICS to zDC to zRemote and returned.

The ping message generates the following DTAX output:

![DTAXPing](https://dt-cdn.net/images/dtaxping-1042-cb46eb515d.png)

DTAXPing

On success, this also generates a log entry zRemote log, such as:

```
info    [native] ASID[53], smfID[S0W1], sysid[C449], jobName[H71AC449] Ping data=asid=53, CFDE33C15E800000
```

## Enable or disable the Dynatrace data capture

These functions enable or disable all the exits used by the CICS module. The `ENABLE` command also starts the DTAX five (5) minute restart cycle if one was not in progress. Likewise, the `DISABLE` command terminates any active DTAX five (5) minute restart cycle.

### Enable the CICS module

`DTAX Enable` should generate the following DTAX output:

![DTAXEna](https://dt-cdn.net/images/dtaxena-1040-c3d45ff65b.png)

DTAXEna

Enable should also register this CICS address space with Dynatrace. Below are the sample messages in the zRemote log following a successful `DTAX Enable`:

```
info    [native] Registering a pgi for the job: HVEAC727[C727], snaId[NETD    .HVEAC727], asid=51, CICS, protocol version=7.3.0, host=xx.xx.xxx.xx, groupId=16db6009dd8ec573, pgir.groupInstanceID=9b720782ca4a076, hostID=ed11bc0b5ee8f53a, nodeID=9b720782ca4a076, groupName=HVEAC727, hostGroup=, processGroupType=28



info    [native] Registered SubAgent[C727,51,6df4c9acf8f61ef5] with zDC[Z727,148], Software Release=54 rc=true
```

### Disable the CICS module

`DTAX Disable` should generate the following DTAX output:

![DTAXDis](https://dt-cdn.net/images/dtaxdis-1048-2f658f2d3e.png)

DTAXDis

Disable should also un-register this address space from Dynatrace. Message from the zRemote logs:

```
info    [native] UnregisterSubAgentRunner: starting to unregister 1 subagents
```

### Enable DTAX Language Environment sensor

Dynatrace provides a sensor into the Language Environment runtime to provide events for dynamic linkage requests from COBOL programs and FETCH verbs from PL/I programs. The Language Environment sensor only traces calls to programs that are linked into a separate load module, it does not trace calls to programs within the same load module. The `DTAX LEENAB` command enables the Language Environment sensor to capture these events. By default, the Language Environment sensor is enabled for 5 minutes, then disabled.

To enable the Language Environment sensor for a custom time interval, use the `LEENAB=<time>` command, where `<time>` is in the range of `1` to `1000` minutes.

![DTAXLEE](https://dt-cdn.net/images/leenab-953-df6ab6d3f3.png)

DTAXLEE

Enabling Language Environment sensor might increase CPU time overhead within the CICS region.

### Disable DTAX Language Environment sensor

`DTAX LEDIS` disables the Dynatrace Language Environment sensor within CICS.

## DTAX messages

To find the description of all DTAX messages, see [z/OS module messages](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages "Messages that are created by the Dynatrace z/OS modules.").