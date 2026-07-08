---
title: z/OS module messages - DTAX messages
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages/dtax-messages
---

# z/OS module messages - DTAX messages

# z/OS module messages - DTAX messages

* 43-min read
* Published Mar 22, 2019

## ZDTP001S

* **Full message** - ZDTP001S Persistent Storage allocation failed.
* **Explanation** - The CICS PLT program was unable to allocate a required persistent storage area.
* **System action** - The PLT program terminates and the CICS code module is not enabled.
* **User response** - Determine why the CICS region is unable to provide storage for the DTAX transaction.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP002S

* **Full message** - ZDTP002S Message Block allocation failed.
* **Explanation** - The PLT program was unable to allocate a required Message block storage area.
* **System action** - The PLT program terminates and the CICS code module is disabled.
* **User response** - Determine why the CICS region is unable to provide storage for the PLT program.

## ZDTP003S

* **Full message** - ZDTP003S ZDTSOAPH Load failed. Disabling Dynatrace CICS code module.
* **Explanation** - CICS could not load `ZDTSOAPH`.
* **System action** - The PLT program terminates and the CICS code module is disabled.
* **User response** - Determine why the CICS region is unable to load one of the DTAX modules - ZDTSOAPH.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP004S

* **Full message** - ZDTP004S ZDTDCCAL final block send failed. rc:<xx>.
* **Explanation** - Message transfer from CICS code module to zDC has failed.
* **System action** - CICS code module operation continues but with missing nodes in the distributed trace.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP005S

* **Full message** - ZDTP005S START DTAX ICE failed.
* **Explanation** - The `EXEC CICS START` command used to initiate the `DTAX ICE` transaction in 5 minutes interval has failed.
* **System action** - None
* **User response** - Examine the more detailed message in the appropriate CICS job log to look at the precise EIBRESP code that indicates why this EXEC CICS START command failed.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP006S

* **Full message** - ZDTP006S Inquire MQCONN <QMGR Name> returned with resp:<xx> resp2:<xx>.
* **Explanation** - `EXEC CICS INQUIRE` for MQ Connection information has failed.
* **System action** - Missing MQ Queue manager name in CICS attachment details.
* **User response** - With the help of `resp` and `resp2` codes, determine why INQUIRE MQCONN failed.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP007S

* **Full message** - ZDTP007S Enable of temporary Language Environment sensor failed no zDC.
* **Explanation** - Indicates that the Language Environment sensor could not be enabled because zDC is unavailable.
* **System action** - Language Environment sensor is not enabled. CICS code module doesn't monitor LE dynamic calls.
* **User response** - Start the zDC for CICS code module to reconnect.

## ZDTP008S

* **Full message** - ZDTP008S GETMAIN PLT Workarea failed.
* **Explanation** - Storage allocation for PLT work area failed.
* **System action** - The PLT program terminates and the CICS code module is disabled.
* **User response** - Determine why the CICS region is unable to provide storage for the PLT program.

## ZDTP009S

* **Full message** - ZDTP009S PLT Name/Token storage not found rc: <xx>.
* **Explanation** - Persistent storage for PLT program is not found.
* **System action** - The PLT program terminates and the CICS code module is disabled.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP010S

* **Full message** - ZDTP010S Turn ON RMI Hook failed with rc: <xx>.
* **Explanation** - RMI hook initialization failed.
* **System action** - CICS code module not initialized successfully.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP011S

* **Full message** - ZDTP011S Turn OFF RMI Hook failed with rc: <xx>.
* **Explanation** - Disabling RMI hook failed.
* **System action** - CICS code module not disabled successfully.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP012S

* **Full message** - ZDTP012S GWA Storage unavailable.
* **Explanation** - Global work area storage for PLT program is unavailable.
* **System action** - Hooks don't initialize successfully.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP013S

* **Full message** - ZDTP013S SOAP hook <nn> failed with rc: <xx>.
* **Explanation** - SOAP hook enable/disable has failed.
* **System action** - Hook operation fails.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP014S

* **Full message** - ZDTP014S Language Environment sensor <nn> failed with rc: <xx>.
* **Explanation** - Language Environment sensor enable/disable has failed.
* **System action** - Hook operation fails.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP015S

* **Full message** - ZDTP015S MRO hook <nn> failed with rc: <xx>.
* **Explanation** - MRO hook enable/disable has failed.
* **System action** - Hook operation fails.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP016S

* **Full message** - ZDTP016S ZDTHKIDR failed with rc: <xx>.
* **Explanation** - Hook operation has failed.
* **System action** - CICS code module don't initialize successfully.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP018S

* **Full message** - ZDTP018S CONF block allocation failed.
* **Explanation** - Storage allocation for config block has failed.
* **System action** - CICS code module doesn't initialize successfully.
* **User response** - Determine why the CICS region is unable to provide storage for the DTAX transaction.

## ZDTP019S

* **Full message** - ZDTP019S Message buffer allocation failed.
* **Explanation** - Storage allocation for message buffer has failed.
* **System action** - CICS code module doesn't initialize successfully.
* **User response** - Determine why the CICS region is unable to provide storage for the DTAX transaction.

## ZDTP020S

* **Full message** - ZDTP020S Get CICS Applid failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS ASSIGN` for APPLID retrieval has failed.
* **System action** - CICS Applid is not displayed in DTAX screen and in log messages.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

## ZDTP021S

* **Full message** - ZDTP021S Get STARTCODE failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS ASSIGN` for program start code retrieval has failed.
* **System action** - CICS code module doesn't initialize successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

## ZDTP022S

* **Full message** - ZDTP022S CICS DELAY failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS DELAY` has failed.
* **System action** - None
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

## ZDTP023S

* **Full message** - ZDTP023S Inquire DB2Entry failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS INQUIRE DB2ENTRY` has failed.
* **System action** - CICS code module operation continues.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP024S

* **Full message** - ZDTP024S CICS code module could not locate a valid AgentId. Possibly a misconfigured or disconnected zRemote. Please check the zRemote log.
* **Explanation** - CICS code module didn't get a valid AgentId after initialization.
* **System action** - CICS code module is disabled.
* **User response** - Check for error messages in zRemote log. If the zRemote service is not running, start it.

## ZDTP025S

* **Full message** - ZDTP025S Inquire System failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS INQUIRE SYSTEM` for CICS version retrieval has failed.
* **System action** - By default CICS code module for CICS Version 4.2 is loaded.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP026S

* **Full message** - ZDTP026S Inquire Program failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS INQUIRE PROGRAM` has failed.
* **System action** - CICS code module operation continues.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP027S

* **Full message** - ZDTP027S Disable Exit program failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS DISABLE PROGRAM` for all exits has failed.
* **System action** - CICS code module is not disabled successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP028S

* **Full message** - ZDTP028S Disable RMI Exit failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS DISABLE PROGRAM` for RMI exit has failed.
* **System action** - RMI exit is not disabled successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP029S

* **Full message** - ZDTP029S START Exit failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS ENABLE START` for `XPCREQC/XRMIIN/XRMIOUT` exit has failed.
* **System action** - Exits are not started successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP030S

* **Full message** - ZDTP030S FREEMAIN failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS FREEMAIN` has failed.
* **System action** - Global Work Area for PLT program FREEMAIN fails.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP031S

* **Full message** - ZDTP031S Enable Exit failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS ENABLE PROGRAM` for enabling exits failed.
* **System action** - CICS code module exits are not enabled successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP032S

* **Full message** - ZDTP032S STOP Exit failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS DISABLE` stop for exits failed.
* **System action** - CICS code module exits are not stopped successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP033S

* **Full message** - ZDTP033S Cancel ReqID failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS CANCEL REQID` has failed.
* **System action** - `DTAX ICE` transaction is not cancelled.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP034S

* **Full message** - ZDTP034S Inquire ReqID failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS INQUIRE REQID` has failed.
* **System action** - `DTAX ICE` transaction is not started successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP035S

* **Full message** - ZDTP035S GETMAIN failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS GETMAIN` for Global Work Area has failed.
* **System action** - Global Work Area for PLT program is not allocated. CICS code module doesn't initialize successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP036S

* **Full message** - ZDTP036S START DTAX ICE failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS START` has failed.
* **System action** - DTAX Interval control transaction is not started every 5 minutes.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP037S

* **Full message** - ZDTP037S LOAD Agent failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS LOAD PROGRAM` for `ZDTAGTxx` module has failed.
* **System action** - `ZDTAGTxx` PTF and build date is not printed in the log messages.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP038S

* **Full message** - ZDTP038S LOAD ZDTSOAPH failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS LOAD PROGRAM` for `ZDTSOAPH` module has failed.
* **System action** - `ZDTSOAPH` build date and version information are not printed in the log messages.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP039S

* **Full message** - ZDTP039S Release agent failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - `EXEC CICS RELEASE PROGRAM` for `ZDTAGTxx/ZDTSOAPH` module has failed.
* **System action** - CICS code module operation continues.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP040S

* **Full message** - ZDTP040S CICS Receive failed. resp:<xx>, resp2:<xx>.
* **Explanation** - `EXEC CICS RECEIVE DATA` has failed.
* **System action** - User command for `DTAX` transaction is not received and hence is not processed successfully.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP041S

* **Full message** - ZDTP041S zOS SMFid unavailable.
* **Explanation** - Error retrieving zOS SMFid.
* **System action** - CICS code module doesn't initialize.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP042S

* **Full message** - ZDTP042S ZDTDCCAL INIT message send failed. rc: <xx>.
* **Explanation** - CICS code module initialization has failed.
* **System action** - CICS code module doesn't initialize.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP043S

* **Full message** - ZDTP043S Unknown AUTHTYPE:<xx>.
* **Explanation** - `EXEC CICS INQUIRE DB2CONN` retreives an `AUTHTYPE` that is not one of `GROUP, TERM, TX, OPID, USERID`.
* **System action** - Authtype not specified in DB2 attachment data in distributed trace.
* **User response** - Contact your Db2 administrator.

## ZDTP044S

* **Full message** - ZDTP044S ZDTDCCAL Register Connection pool failed. rc:<xx>.
* **Explanation** - Sending Db2 connection pool information from CICS code module to zDC has failed.
* **System action** - Db2 attachment details in distributed trace is empty.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP045S

* **Full message** - ZDTP045S ZDTDCCAL Register DLI Connection pool failed. rc:<xx>.
* **Explanation** - Sending DL1 connection pool information from CICS code module to zDC has failed.
* **System action** - DLI attachment details in distributed trace is empty.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP046S

* **Full message** - ZDTP046S ZDTDCCAL Message send failed. rc:<xx>.
* **Explanation** - CICS code module could not send message to zDC.
* **System action** - No data passes from CICS to zDC.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP047S

* **Full message** - ZDTP047S DTAX Transaction definition not found. Disabling dynatrace agent.
* **Explanation** - The RDO definition for DTAX transaction is not found.
* **System action** - CICS code module not enabled and the PLT program execution terminates.
* **User response** - Define DTAX transaction for the PLT program. Refer to CICRDO member in SZDTSAMP installation library for sample definition.

## ZDTP048S

* **Full message** - ZDTP048S Config block retrieval failed. rc:<xx>.
* **Explanation** - CICS code module could not find the configuration data with sensor settings.
* **System action** - CICS code module doesn't initialize.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP049S

* **Full message** - ZDTP049S Config block not found.
* **Explanation** - CICS code module could not find the config block with CICS sensor settings.
* **System action** - CICS code module is disabled.
* **User response** - Check if the CICS Transaction Server sensor is placed in the CICS code module Mapping.

## ZDTP050S

* **Full message** - ZDTP050S DTAX Enable failed. rc:<xx>.
* **Explanation** - Couldn't enable CICS code module.
* **System action** - CICS code module doesn't initialize successfully.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP051S

* **Full message** - ZDTP051S ZDTAGT Copyright Info not found.
* **Explanation** - Could not find the Copyright block in ZDTAGTxx module.
* **System action** - CICS code module continues. No PTF/Build date is printed in the zRemote log.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP052S

* **Full message** - ZDTP052S Check Agent Mapping if the CICS Transaction Server sensor is placed.
* **Explanation** - Configuration block with the CICS sensor information is not found.
* **System action** - CICS code module is disabled.
* **User response** - Check if the CICS transaction server sensor is placed in the CICS code module mapping.

## ZDTP053S

* **Full message** - ZDTP053S Disabling CICS code module.
* **Explanation** - This message is an extension of `ZDTP052S`.
* **System action** - CICS code module is disabled.
* **User response** - Follow `ZDTP052S`.

## ZDTP054S

* **Full message** - ZDTP054S Turn ON Trace Hooks failed with rc: @@
* **Explanation** - Couldn't enable Trace hook.
* **System action** - Trace hook is not installed.
* **User response** - Look in CICS log for problems. If you don't find anything, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP055S

* **Full message** - ZDTP055S Turn OFF Trace Hooks failed with rc: @@
* **Explanation** - Couldn't disable trace hook.
* **System action** - Trace hook is not installed.
* **User response** - Look in CICS log for problems. If you don't find anything, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP056S

* **Full message** - ZDTP056S DSASTK address is not NULL -logic error
* **Explanation** - Bad address for DSA storage
* **System action** - Dynatrace hooks are not enabled.
* **User response** - CICS getmain failed. Check CICS logs and correct problem.

## ZDTP057S

* **Full message** - ZDTP057S Getmain failed for DSA area
* **Explanation** - Storage allocation for DSA area has failed.
* **System action** - Dynatrace hooks are not enabled.
* **User response** - Check CICS log and correct the problem.

## ZDTP058S

* **Full message** - ZDTP058S DSASTK address is Zero can not free GWA: @@
* **Explanation** - Bad address for DSA storage free
* **System action** - No attempt to free main storage.
* **User response** - This is usually not a problem as Dynatrace code module usually just didn't get any storage for this configuration.

## ZDTP059S

* **Full message** - ZDTP059S Freemain failed for DSA area @@
* **Explanation** - Bad address for DSA storage free from CICS chain.
* **System action** - No attempt to free main storage.
* **User response** - The storage chain is broken or corrupt.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP060S

* **Full message** - ZDTP060S Invalid ICE value, resetting to 5
* **Explanation** - DTAX time value was not in the range from 1 to 5.
* **System action** - The value is reset to 5.
* **User response** - If you are changing ICE values in the DTAX transaction make sure it is value from 1 to 5.

## ZDTP061S

* **Full message** - ZDTP061S This upgrade requires a CICS restart
* **Explanation** - CICS code module has been updated. A CICS restart is required to run the new code.
* **System action** - None
* **User response** - Restart CICS when you can to pick up new code module versions.

## ZDTP062S

* **Full message** - ZDTP062S No CICSplex name, CPSM API error <xx> occurred
* **Explanation** - CICSPlex name not found for the CICS region due to an unexpected error indicated by the error code “xx”
* **System action** - CICS code module continues initialization.
* **User response** - None

## ZDTP063S

* **Full message** - ZDTP063S Turn OFF Language Environment sensor failed with rc: <xx>
* **Explanation** - Couldn't disable Language Environment sensor.
* **System action** - Language Environment sensor is not turned off, CICS code module continues to monitor LE events.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP064S

* **Full message** - ZDTP064S Turn ON Language Environment sensor failed with rc: <xx>
* **Explanation** - Couldn't enable Language Environment sensor.
* **System action** - CICS code module doesn't monitor LE events.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP065S

* **Full message** - ZDTP065S Disable EXITALL failed
* **Explanation** - Couldn't disable the TRUE and GLUE exits after two consecutive attempts.
* **System action** - CICS code module might cause an `AKEA` abend.
* **User response** - Examine CICS log for `DISABLE EXITALL` failure. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP066S

* **Full message** - ZDTP066S CICS version <Cics Version> unsupported. Disabling Dynatrace CICS code module.
* **Explanation** - CICS code module has detected an unsupported version of CICS.
* **System action** - CICS code module is disabled.
* **User response** - Upgrade your CICS region to a version supported by Dynatrace.

## ZDTP067S

* **Full message** - ZDTP067S <ZDTAGTxx> Load failed. Disabling Dynatrace CICS code module.
* **Explanation** - Loading of the CICS code module has failed.
* **System action** - CICS code module is disabled.
* **User response** - Examine the CICS job output for any other messages that may be relevant to the failure. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP068S

* **Full message** - ZDTP068S Exec CICS Retrieve failed. resp:<xx>, resp2:<xx>, rcode:<xx>
* **Explanation** - The `EXEC CICS RETRIEVE` command used to control the Language Environment sensor interval has failed.
* **System action** - None
* **User response** - Examine the more detailed message in the appropriate CICS job log to look at the precise EIBRESP code that indicates why this EXEC CICS RETRIEVE command failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP069S

* **Full message** - ZDTP069S START LE ICE failed. resp:<xx>, resp2:<xx>, rcode:<xx>
* **Explanation** - The `EXEC CICS START` command used to initiate the Language Environment sensor interval has failed.
* **System action** - None
* **User response** - Examine the more detailed message in the appropriate CICS job log to look at the precise EIBRESP code that indicates why this EXEC CICS START command failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP070S

* **Full message** - ZDTP070S Agent program ZDTAGTnn not marked ThreadSafe - check CSD definition
* **Explanation** - During CICS startup or DTAX command processing, the Agent program was not marked ThreadSafe. ThreadSafe is required for CICS performance.
* **System action** - Processing is terminated and the CICS region is not setup to run Dynatrace.
* **User response** - Check that the Dynatrace CICS resource definitions has been added to the CICS region. Sample resource definitions can be found in installation sample dataset member(CICRDO). Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP072S

* **Full message** - ZDTP072S Hook installation failed.
* **Explanation** - DTAX transaction could not update the sensor hook settings in the GWA.
* **System action** - If this happens during DTAX initialization, DTAX is disabled. If this happens during the ICE interval, the new sensor changes will not take effect.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP001W

* **Full message** - ZDTP001W Please update PLT, INITPARM, and RDO to ZDTPLT.
* **Explanation** - RDO definition for `ZDTPLT` with suffix (67/68/69/70/71/72/73) found.
* **System action** - Execution continues.
* **User response** - Update the RDO definitions for `ZDTPLTxx` and DTAX to refer to `ZDTPLT` without suffix. Refer to CICRDO member in `SZDTSAMP` installation library for sample RDO definitions.

## ZDTP002W

* **Full message** - ZDTP002W Extract Exit failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - There was a problem in retrieving the Global Work Area storage for exit program. `EXEC CICS EXTRACT EXIT` operation failed. This is also possible when an attempt was made to look up `DTAX CONF` when the CICS code module is disabled.
* **System action** - None
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP004W

* **Full message** - ZDTP004W zDC <zDC Name> unavailable, no active SSCT found.
* **Explanation** - There was no zDC available for CICS code module to connect to.
* **System action** - CICS code module is disabled.
* **User response** - Start zDC and check if the zDC connects successfully to zRA. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP005W

* **Full message** - ZDTP005W Config block retrieval failed. Attempt re-retrieval during ICE.
* **Explanation** - CICS code module could not retrieve CICS Sensor configuration block.
* **System action** - DTAX transaction attempts to retrieve CICS Sensor configuration block in the next 5 minutes interval.
* **User response** - Check if the CICS code module is successfully enabled in the next 5 minutes interval. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP006W

* **Full message** - ZDTP006W DTAX ICE is out of range 1 - 5 minutes. Forcing ICE to 5 minutes.
* **Explanation** - `DTAX ICE` command was issued with an invalid value.
* **System action** - DTAX transaction sets the ICE value to the default 5 minutes.
* **User response** - If you want to change the default DTAX ICE value, enter a value between 1 to 5.

## ZDTP007W

* **Full message** - ZDTP007W No CICSplex name, CPSM API not available.
* **Explanation** - No CICSplex name is available for the CICS region.
* **System action** - CICS code module continues initialization.
* **User response** - None

## ZDTP008W

* **Full message** - ZDTP008W Too many configuration parameters to display.
* **Explanation** - `DTAX CONF` option couldn't display all the configuration settings in the DTAX panel, because there's not enough screen area for the display.
* **System action** - Configuration settings are truncated in the DTAX display
* **User response** - None

## ZDTP009W

* **Full message** - ZDTP009W Refer to Deep monitoring section in the UI for all the parameters.
* **Explanation** - Check all CICS code module configuration parameters in Dynatrace UI.
* **System action** - None
* **User response** - To view all the CICS code module configuration settings, go to **Settings** > **Server-side service monitoring** > **Deep monitoring** > **CICS, IMS and MQ monitoring**.

## ZDTP010W

* **Full message** - ZDTP010W Temporary Language Environment sensor enable failed
* **Explanation** - Couldn't enable Language Environment sensor.
* **System action** - CICS code module doesn't monitor Language Environment events.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP011W

* **Full message** - ZDTP011W Temporary Language Environment sensor disable failed
* **Explanation** - Couldn't disable Language Environment sensor.
* **System action** - CICS code module continues to monitor Language Environment events which might cause overhead.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP012W

* **Full message** - ZDTP012W CICSPlex name not known due to CPSM security
* **Explanation** - Dynatrace does not have permission to issue EXEC CPSM comands.
* **System action** - CICS code module continues but the plex name is blank or invalid.
* **User response** - Contact system security and authorize Dynatrace to access CPSM.

## ZDTP013W

* **Full message** - ZDTP013W PLT version <plt version> and CICS Agent version <zdtagt version> does not match
* **Explanation** - Dynatrace CICS code module versions are different.
* **System action** - None
* **User response** - Perform `CEMT SET NEWCOPY` for the version that is older. For example: If PLT is older `CEMT SET PROG(ZDTPLT) NEWCOPY` If CICS code module version is older (`zz` is the CTS version) `CEMT SET PROG(ZDTAGTzz) NEWCOPY`

## ZDTP014W

* **Full message** - ZDTP014W Invalid time interval entered for Language Environment sensor.
* **Explanation** - Invalid minute value entered for the Language Environment sensor.
* **System action** - None
* **User response** - Enter a valid interval, between 1-1000 minutes, to enable the Language Environment sensor.

## ZDTP015W

* **Full message** - ZDTP015W Language Environment sensor time interval out of range (1-1000).
* **Explanation** - The Language Environment sensor interval value entered is out of range.
* **System action** - None
* **User response** - Enter a valid interval value between 1-1000 minutes to enable the Language Environment sensor.

## ZDTP016W

* **Full message** - ZDTP016W zDC <zdcName> INIT Failed.
* **Explanation** - The PLT program is unable to connect to the collection system.
* **System action** - Execution continues. The PLT program tries to reconnect with the collection system during the next 5 minute window.
* **User response** - Check if the zRemote code module is up and running and connected to Dynatrace. If not, start the service that is down.

  If the problem persists, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDTP017W

* **Full message** - ZDTP017W Agent ID is zero, using zDC ZDC-NAME
* **Explanation** - During CICS startup or DTAX command processing, the Agent program is not registered to the zDC.
* **System action** - Hooks and exits are not installed.
* **User response** - Make sure the zDC is started and connected to a zRemote. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP001I

* **Full message** - ZDTP001I DTAX User Command: PING.
* **Explanation** - User issued a `DTAX PING` command.
* **System action** - Check if the connection exists between the z/OS CICS code module and the zRemote code module.
* **User response** - None

## ZDTP002I

* **Full message** - ZDTP002I DTAX User Command: DISABLE.
* **Explanation** - User issued a `DTAX DISABLE` command.
* **System action** - Disable all the exits used by CICS code module and terminate the 5 minutes DTAX cycle.
* **User response** - None

## ZDTP004I

* **Full message** - ZDTP004I DTAX User Command: CONF.
* **Explanation** - User issued a `DTAX CONF` command.
* **System action** - Display the active CICS Sensor configuration in the DTAX panel.
* **User response** - None

## ZDTP005I

* **Full message** - ZDTP005I DTAX User Command: ENABLE.
* **Explanation** - User issued a `DTAX ENABLE` command.
* **System action** - CICS code module registers with the collection system. On successful connection, respective EXITs and Hooks are enabled.
* **User response** - None

## ZDTP006I

* **Full message** - ZDTP006I ZDTPLT[<call type>] Compiled on mm dd yyyy hh:mm:ss.
* **Explanation** - This message is displayed in the zRemote log file when DTAX initializes successfully. The call type indicates the time when DTAX initalizes. Possible call types are, CPLT - DTAX initialized during CICS startup; USER - DTAX initialized due to user command `DTAX EN`. ICE - DTAX initialized during the ICE interval. This message gives ZDTPLT compilation and version information.
* **System action** - None
* **User response** - None

## ZDTP007I

* **Full message** - ZDTP007I ZDTAGT <PTF> <Build Date> <Build Time> VER <Product Release> <CICS Version>.
* **Explanation** - This message is logged in the zRemote log file when DTAX initializes successfully. This message gives CICS code module module (ZDTAGT) compilation and version information.
* **System action** - None
* **User response** - None

## ZDTP008I

* **Full message** - ZDTP008I ZDTSOAPH <PTF> <Build Date> <Build Time> VER <Product Release>.
* **Explanation** - This message is logged in the zRemote log file when DTAX initializes successfully. This message gives ZDTSOAPH compilation and version information.
* **System action** - None
* **User response** - None

## ZDTP009I

* **Full message** - ZDTP009I INIT failed during PLT. Trying to reconnect…
* **Explanation** - The PLT program is unable to establish connection with the zRemote code module during PLT time.
* **System action** - Reconnect attempted during the next DTAX cycle, which starts immediately after the CICS region comes up.
* **User response** - None

## ZDTP010I

* **Full message** - ZDTP010I Screen size unavailable.
* **Explanation** - There was a problem in retrieving the screen attributes.
* **System action** - Screen attributes are defaulted to `Screen Width=80` and `Screen Height=24`.
* **User response** - None

## ZDTP011I

* **Full message** - ZDTP011I DISABLE TRUE(ZDTAGTxx) with ENTRYNAME(ZDTAGENT).
* **Explanation** - The exit program `ZDTAGTxx` associated with entryname `ZDTAGENT` is disabled. `xx` represents the CTS version.
* **System action** - None
* **User response** - None

## ZDTP012I

* **Full message** - ZDTP012I ENABLE TRUE(ZDTAGTxx) with ENTRYNAME(ZDTAGENT).
* **Explanation** - The exit program ZDTAGTxx associated with entryname ZDTAGENT is enabled. `xx` represents the CTS version.
* **System action** - None
* **User response** - None

## ZDTP013I

* **Full message** - ZDTP013I ENABLE Exit program(ZDTAGTxx) with Exit([exit name]).
* **Explanation** - Enable the global exit point specified by `[exit name]` associated with the ZDTAGTxx exit.
* **System action** - None
* **User response** - None

## ZDTP014I

* **Full message** - ZDTP014I START TRUE(ZDTAGTxx) with ENTRYNAME(ZDTAGENT).
* **Explanation** - Start the user exit `ZDTAGENT` associated with the exit program `ZDTAGTxx`.
* **System action** - None
* **User response** - None

## ZDTP015I

* **Full message** - ZDTP015I START Exit program(ZDTAGTxx) with Exit([exit name]).
* **Explanation** - Start the global exit point specified by `[exit name]` associated with the exit program `ZDTAGTxx`.
* **System action** - None
* **User response** - None

## ZDTP016I

* **Full message** - ZDTP016I STOP Exit program(program name) and all associated exits
* **Explanation** - Stop and disable all the exit points associated with the exit `ZDTAGTxx`.
* **System action** - None
* **User response** - None

## ZDTP017I

* **Full message** - ZDTP017I DISABLE Exit program(ZDTAGTxx) with Exit([exit name]).
* **Explanation** - Disable the global exit point `[exit name]` associated with the exit ZDTAGTxx.
* **System action** - None
* **User response** - None

## ZDTP019I

* **Full message** - ZDTP019I Config block retrieved successfully.
* **Explanation** - Indicates that CICS sensor configuration has been retrieved successfully after there was a problem in configuration block access. This message follows after ZDTP049S when the CICS transaction server sensor has been placed.
* **System action** - CICS code module is initialized.
* **User response** - None

## ZDTP020I

* **Full message** - ZDTP020I Active Sensors: <TX | MQ | DB2 | DB2R | SOAP | CTG | DB2Fetch | DLI | DLIR | LE | File | HTTP | ZCON | TTX | CTGA>.
* **Explanation** - Indicates the CICS Sensors that are placed and active.
* **System action** - None
* **User response** - None

## ZDTP021I

* **Full message** - ZDTP021I CICS Sensors updated.
* **Explanation** - Indicates that the CICS Sensors have been updated and the CICS code module honored the changes during DTAX 5 minutes cycle.
* **System action** - None
* **User response** - None

## ZDTP022I

* **Full message** - ZDTP022I Inquire DB2Conn failed. resp:<xx>, resp2:<xx>, rcode:<xx>.
* **Explanation** - EXEC CICS INQUIRE DB2CONN has failed.
* **System action** - CICS code module operation continues. No DB2 attachment details provided in the distributed trace.
* **User response** - Determine the cause of the problem from `resp` and `resp2` codes. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP023I

* **Full message** - ZDTP023I DTAX ICE interval set to: @@ minute(s).
* **Explanation** - `DTAX ICE` value was changed.
* **System action** - None.
* **User response** - None

## ZDTP024I

* **Full message** - ZDTP024I Trace Hook is being enabled
* **Explanation** - Indicates that the Trace hook is being turned on in the CICS code module.
* **System action** - None.
* **User response** - None

## ZDTP025I

* **Full message** - ZDTP025I Trace Hook is being disabled
* **Explanation** - Indicates that the Trace hook is being turned off in the CICS code module.
* **System action** - None.
* **User response** - None

## ZDTP026I

* **Full message** - ZDTP026I Temporary Language Environment sensor is enabled for @@@@ minute(s).
* **Explanation** - Indicates that the Language Environment sensor has been turned on for the current DTAX ICE interval. Note that the Language Environment sensor will be automatically turned off during the following DTAX ICE cycle.
* **System action** - None.
* **User response** - None

## ZDTP027I

* **Full message** - ZDTP027I Turn off Language Environment sensor because ICE timer expired
* **Explanation** - Indicates that the Language Environment sensor has been automatically turned off at the end of the current ICE interval.
* **System action** - None.
* **User response** - None

## ZDTP028I

* **Full message** - ZDTP028I TX code : xxxx xxxx xxxx .
* **Explanation** - Displays the Start TX sensor setting in Deep Monitoring in the web UI for the CICS regions.
* **System action** - None.
* **User response** - None

## ZDTP029I

* **Full message** - ZDTP029I DTAX User Command: LEENAB
* **Explanation** - User issued a `DTAX LEENAB` command to turn on the Language Environment sensor.
* **System action** - Language Environment sensor is turned on temporarily. CICS code module starts monitoring LE dynamic calls.
* **User response** - None

## ZDTP030I

* **Full message** - ZDTP030I DTAX Status:V.R PLT-PTF AGT-PTF TRUE-STS XP RMI-STS ZDC-NAME AGT-ID ).
* **Explanation** - DTAX STATUS console command was issued. This can be used for Automated Operations to see if Dynatrace Hooks/Exits are enabled. Field descriptions: \* `V.R`: DT Version \* `PLT-PTF`: PLT PTF \* `AGT-PTF`: Agent PTF \* `TRUE-STS`: TRUE Status \* `XPC-STS`: XPCREQ/C Status \* `RMI-STS`: RMIIN/R \* `ZDC-NAME`: zDC Name \* `AGT-ID`: Agent ID
* **System action** - None, this is informational only.
* **User response** - None

## ZDTP031I

* **Full message** - ZDTP031I DSA Freed at location : <addr>
* **Explanation** - Indicates that the DSA at location `addr`, used by CICS code module, has been freed.
* **System action** - DSA memory is freed.
* **User response** - None

## ZDTP032I

* **Full message** - ZDTP032I DTAX Modify Command: LOG accepted.
* **Explanation** - DTAX received the LOG level update from MODIFY command.
* **System action** - None.
* **User response** - None. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP033I

* **Full message** - ZDTP033I DTAX using TD Queue ZDTQ DD for messages.
* **Explanation** - DTAX is now using ZDTQ DD for messages instead of the default MSGUSR.
* **System action** - None.
* **User response** - None. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP034I

* **Full message** - ZDTP034I Terminal TX code : xxxx
* **Explanation** - This message is displayed with user specified Terminal transaction code, in the zRemote log during DTAX initialization.
* **System action** - CICS code module stops monitoring MRO events if the MRO hook has been removed successfully.
* **User response** - If the Return code is a non-zero value, MRO hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP035I

* **Full message** - ZDTP035I Language Environment sensor has been disabled successfully.
* **Explanation** - The Language Environment sensor has been disabled. The CICS agent will stop monitoring LE programs.
* **System action** - None.
* **User response** - None. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP036I

* **Full message** - ZDTP036I Language Environment is already disabled.
* **Explanation** - Language Environment sensor is already disabled, no action taken.
* **System action** - None
* **User response** - None. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP131I

* **Full message** - ZDTP131I Install of Soap Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed installing SOAP hook for SOAP request monitoring. Return code 0 indicates successful SOAP hook installation.
* **System action** - CICS code module is ready to monitor SOAP events with successful SOAP hook installation.
* **User response** - If the Return code is a non-zero value, SOAP hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP132I

* **Full message** - ZDTP132I Removal of SOAP Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed removing SOAP hook. Return code 0 indicates successful SOAP hook removal.
* **System action** - CICS code module stops monitoring SOAP events if the SOAP hook has been removed successfully.
* **User response** - If the Return code is a non-zero value, SOAP hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP133I

* **Full message** - ZDTP133I Install of MRO Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed installing MRO hook for multi region call monitoring. Return code 0 indicates successful MRO hook installation.
* **System action** - CICS code module is ready to monitor MRO events with the successful MRO hook installation.
* **User response** - If the Return code is a non-zero value, MRO hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP134I

* **Full message** - ZDTP134I Removal of MRO Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed removing MRO hook. Return code 0 indicates successful MRO hook removal.
* **System action** - CICS code module stops monitoring MRO events if the MRO hook has been removed successfully.
* **User response** - If the Return code is a non-zero value, MRO hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP135I

* **Full message** - ZDTP135I Install of ERM Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed installing ERM hook for DB2 call monitoring. Return code 0 indicates successful ERM hook installation.
* **System action** - CICS code module is ready to monitor DB2 calls from the CICS region with the successful ERM hook installation.
* **User response** - If the Return code is a non-zero value, ERM hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP136I

* **Full message** - ZDTP136I Removal of ERM Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed removing ERM hook. Return code 0 indicates successful ERM hook removal.
* **System action** - CICS code module stops monitoring DB2 calls if the ERM hook has been removed successfully.
* **User response** - If the Return code is a non-zero value, ERM hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP137I

* **Full message** - ZDTP137I Install of PL1 Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed installing PL1 hook for monitoring PL1 dynamic calls. Return code 0 indicates successful PL1 hook installation.
* **System action** - CICS code module is ready to monitor PL1 dynamic calls with the successful PL1 hook installation.
* **User response** - If the Return code is a non-zero value, PL1 hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP138I

* **Full message** - ZDTP138I Removal of PL1 Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed removing PL1 hook. Return code 0 indicates successful PL1 hook removal.
* **System action** - CICS code module stops monitoring PL1 dynamic calls if the PL1 hook has been removed successfully.
* **User response** - If the Return code is a non-zero value, PL1 hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP139I

* **Full message** - ZDTP139I Install of <COBOL routine> Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed installing COBOL hooks IGZCFCC, IGZCLNK and IGZXFCAL (indicated by “COBOL routine”) for monitoring COBOL dynamic calls. Return code 0 indicates successful COBOL hooks installation.
* **System action** - CICS code module is ready to monitor COBOL dynamic calls with the successful COBOL hooks installation.
* **User response** - If the Return code is a non-zero value, COBOL hook installation has failed. Please contact a Dynatrace product expert via live chat within your environment.

## ZDTP140I

* **Full message** - ZDTP140I Removal of COBOL Hook Completed Return Code: xxxx
* **Explanation** - CICS code module has completed removing COBOL hook. Return code 0 indicates successful COBOL hook removal.
* **System action** - CICS code module stops monitoring COBOL dynamic calls if the COBOL hook has been removed successfully.
* **User response** - If the Return code is a non-zero value, COBOL hook removal has failed. Please contact a Dynatrace product expert via live chat within your environment.

## Related topics

* [Manage the CICS module via DTAX transactions](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/dtax-transaction "Manage the CICS module via DTAX transactions.")