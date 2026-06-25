---
title: z/OS module messages - zDC system messages
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages/zdc-system-messages
scraped: 2026-05-12T12:13:15.748925
---

# z/OS module messages - zDC system messages

# z/OS module messages - zDC system messages

* 63-min read
* Updated on Feb 10, 2026

## ZDC000I

* **Full message** - ZDC000I INITIALIZATION @@ FOR zDC @@ VER @@.@@.@@
* **Explanation** - This informational message indicates that the initialization of the zDC has started or ended. The subsystem ID and the version of the product are displayed.
* **System action** - Processing continues.
* **User response** - None

## ZDC001E

* **Full message** - ZDC001E AN ERROR HAS OCCURRED DURING LOAD FOR MODULE @@
* **Explanation** - At zDC system startup the was an attempt to load all the processing modules into storage. This load was unsuccessful for the module named (`@@`) in this message.
* **System action** - zDC terminates.
* **User response** - Ensure that the `//STEPLIB` or `//JOBLIB DD` statements in the JCL executing zDC point to the correct data sets and that these data sets contain the correct release of the zDC.

## ZDC002E

* **Full message** - ZDC002E MODULE=@@ R15=@@ R1=@@
* **Explanation** - This message follows `ZDC001` and gives the module name as well as the contents of `R15` and `R1` at the completion of the LPAD operation.
* **System action** - zDC terminates.
* **User response** - Save the information in this message if you need to contact your systems programmer or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC003E

* **Full message** - ZDC003E COMMON AREA STORAGE NOT AVAILABLE FOR MODULE @@
* **Explanation** - This message indicates that the attempt to load the module named in the message into extended common storage has failed because there is not enough available storage to hold the module.
* **System action** - zDC terminates.
* **User response** - Increase the amount of common storage, specifically subpool 241, and start zDC again.

## ZDC004E

* **Full message** - ZDC004E AN ERROR HAS OCCURRED DURING BLDL FOR MODULE @@
* **Explanation** - At zDC system startup there was an attempt to load all the processing modules into storage. The `BLDL` for this load was unsuccessful for the module named in the message.
* **System action** - zDC terminates.
* **User response** - Ensure that the `//STEPLIB` or `//JOBLIB DD` statements in the JCL executing zDC point to the correct data sets and that these data sets contain the correct release of the zDC.

## ZDC005E

* **Full message** - ZDC005E MODULE=@@ R15=@@ R1=@@
* **Explanation** - This message follows `ZDC004` and gives the module name, and the contents of `R15` and `R1` at the completion of the `BLDL` operation.
* **System action** - zDC terminates.
* **User response** - Save the information in this message if you have to contact your systems programmer or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC006E

* **Full message** - ZDC006E SUBSYSTEM @@ ALREADY EXISTS AND IS ACTIVE
* **Explanation** - This message indicates that the 4-character subsystem ID you specified in the `//SYSIN DD` parameter data set already exists in your system and it is an active zDC subsystem.
* **System action** - zDC terminates.
* **User response** - Ensure that the subsystem ID you have specified is unique in your system. Then restart zDC or stop the instance of the zDC that holds this name.

## ZDC007E

* **Full message** - ZDC007E ECSA STORAGE NOT AVAILABLE FOR SUBSYSTEM @@, R15=@@
* **Explanation** - This message indicates that the attempt to obtain storage for the subsystem control block has failed. There is not enough storage above the line in extended CSA sub-pool 241 for these blocks.
* **System action** - zDC terminates.
* **User response** - Increase the amount of extended CSA subpool 241 storage and restart the zDC.

## ZDC008I

* **Full message** - ZDC008I MODULE P/T DATE TIME VERSION ADDRESS LENGTH
* **Explanation** - This message is displayed only at zDC startup. It names the columns shown below in multiple message numbers `ZDC009`. The module name, highest problem tracking number, the date and time the module was last assembled, the version of the module and the main storage address where it is loaded are shown.
* **System action** - Processing continues.
* **User response** - None

## ZDC009I

* **Full message** - ZDC009I @@ @@ @@ @@ @@ @@ @@
* **Explanation** - This message lists one module loaded by zDC. See the `ZDC008` message for a description of the columns.
* **System action** - Processing continues.
* **User response** - None

## ZDC010E

* **Full message** - ZDC010E SDUMPX TAKEN SUCCESSFULLY FOR zDC @@ ABEND
* **Explanation** - This message is displayed on the system console by the zDC dump routines. It names the abend code.
* **System action** - Execution terminates.
* **User response** - Prepare the dump for examination by your systems staff or for transmission to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.

## ZDC011E

* **Full message** - ZDC011E SDUMPX FAILED FOR zDC @@ ABEND. RETCODE=@@/@@
* **Explanation** - This message is displayed on the system console by the zDC dump routines. It indicates that the attempt to obtain a system dump has failed. The return and reason code for the failure are shown in the message.
* **System action** - Execution terminates.
* **User response** - Examine the return and reason codes or supply this message to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.

## ZDC012E

* **Full message** - ZDC012E @@ ABEND DUMP IN DYNATRACE zDC @@
* **Explanation** - This message is the title for all SDUMPX macros issued by zDC. This title indicates the abend code that caused the dump to be taken.
* **System action** - Execution terminates.
* **User response** - Ensure that the dump is preserved and can be given to your systems programming staff or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.

## ZDC014E

* **Full message** - ZDC014E ZDCLOGER VSAM @@ ERROR
* **Explanation** - This message indicates that a non-zero return code has resulted from a VSAM zDC log request. The name of the request is contained in the message.
* **System action** - The log task terminates but the execution of the zDC continues.
* **User response** - Examine the subsequent messages, which contain detailed information about the nature of the error. Keep this information for your systems programming staff or for a Dynatrace product expert via live chat. Try to and re-attach and re-open the log (MVS command: `Modify ZdcStcName,LOG OPEN`). Please contact a Dynatrace product expert via live chat within your environment.

## ZDC015E

* **Full message** - ZDC015E ZDCLOGER VSAM RPL FEEDBACK WORD @@
* **Explanation** - This message contains the value of the VSAM RPL feedback word following a VSAM PUT to the log data set.
* **System action** - The log task terminates but execution of the zDC continues.
* **User response** - Examine the subsequent messages, which contain detailed information about the nature of the error. Keep this information for your systems programming staff or for a Dynatrace product expert via live chat. Try to re-attach and re-open the log (MVS command: `Modify ZdcStcName,LOG OPEN`). Please contact a Dynatrace product expert via live chat within your environment.

## ZDC016E

* **Full message** - ZDC016E ZDCLOGER VSAM ACB ERROR FLAG @@
* **Explanation** - This message contains the value of the VSAM ACB error flag following a VSAM OPEN or CLOSE of the log data set.
* **System action** - The log task terminates but execution of the zDC continues.
* **User response** - Examine the subsequent messages, which contain detailed information about the nature of the error. Keep this information for your systems programming staff or for a Dynatrace product expert via live chat. Enter the ISPF zDC control system. Then re-attach and re-open the log. Please contact a Dynatrace product expert via live chat within your environment..

## ZDC017E

* **Full message** - ZDC017E SRB ABEND @@ AT DISPLACEMENT @@ INTO ZDCSRBRT
* **Explanation** - This message indicates that an abend has occurred at the displacement shown into the SRB routine named `ZDCSRBRT`.
* **System action** - Execution terminates.
* **User response** - If a dump is produced, save it for your systems staff or for transmission to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment. re-execute the zDC.

## ZDC018E

* **Full message** - ZDC018E EXTENDED CSA STORAGE NOT AVAILABLE FOR SRB ROUTINE
* **Explanation** - This message indicates that a `STORAGE OBTAIN` has failed to report that extended CSA storage from subpool 241 is not available.
* **System action** - Execution terminates.
* **User response** - Report this condition to your systems programmer who may want to increase the amount of extended CSA storage in the system.

## ZDC019E

* **Full message** - ZDC019E zDC INITIALIZATION FAILED. RETCODE=@@/@@
* **Explanation** - This message indicates that the initialization routines have failed. It also shows the return and reason codes describing this failure.
* **System action** - zDC execution terminates.
* **User response** - Examine the SYSPRINT data set for any other messages that may be relevant to the failure. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC026I

* **Full message** - ZDC026I STOP COMMAND ACCEPTED
* **Explanation** - This message confirms that the STOP command entered by an operator has been accepted by zDC and end of job processing has commenced.
* **System action** - Execution terminates.
* **User response** - None

## ZDC027I

* **Full message** - ZDC027I MODIFY COMMAND RECEIVED
* **Explanation** - This message confirms that the MODIFY command entered by an operator has been received by zDC and is processing. Any errors encountered during parsing or execution of the command are indicated later.
* **System action** - Execution continues.
* **User response** - None

## ZDC028I

* **Full message** - ZDC028I @@
* **Explanation** - This message contains a copy of the entire command entered by the operator in the console. Only the first 120 bytes of the command are displayed.
* **System action** - Execution continues.
* **User response** - None

## ZDC029E

* **Full message** - ZDC029E TCPSP subtask unavailable to process shutdown request
* **Explanation** - This message indicates that the ECB for TCPSP subtask is busy and unavailable to receive the shutdown request.
* **System action** - Execution terminates.
* **User response** - If a dump is produced, save it for your systems staff or for transmission to a Dynatrace product expert via live chat. Re-execute the zDC. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC033E

* **Full message** - ZDC033E INVALID COMMAND. PLEASE REENTER
* **Explanation** - The command you just entered in the operator console was invalid and wasn't processed.
* **System action** - The command is ignored and processing continues.
* **User response** - Re-enter a valid command if possible. If the command was valid, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC035I

* **Full message** - ZDC035I @@ ARMED FOR AUTOMATIC RESTART
* **Explanation** - This message indicates that you have selected ARM processing and this is the first time the element named in this message has been armed. This means the execution is not due to an automatic restart.
* **System action** - Processing continues.
* **User response** - None

## ZDC036I

* **Full message** - ZDC036I @@ RESTARTED DUE TO PREVIOUS ABEND. RSNCD=@@
* **Explanation** - This message indicates that this zDC has been automatically restarted by the system. The reason code indicates whether the JCL or START command has been changed (RSNCD=108) or has not been changed (RSNCD=104).
* **System action** - Processing continues.
* **User response** - None

## ZDC037E

* **Full message** - ZDC037E @@ IXCARM REGISTER FAILURE. RETCD=@@. RSNCD=@@
* **Explanation** - An attempt to issue IXCARM macro has resulted in a return code greater than 4. This indicates that the request did not complete. The actual return and reason codes are shown in this message.
* **System action** - Processing continues but without ARM support.
* **User response** - See the **z/OS MVS Sysplex Services Reference** for a complete list of the possible return and reason codes. Correct any environmental errors or report this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC038E

* **Full message** - ZDC038E @@ IXCARM READY FAILURE. RETCD=@@. RSNCD=@@
* **Explanation** - An attempt to issue `IXCARM` macro has resulted in a return code greater than 4. This indicates that the request did not complete. The actual return and reason codes are shown in this message.
* **System action** - Processing continues but without ARM support.
* **User response** - See the **z/OS MVS Sysplex Services Reference** for a complete list of the possible return and reason codes. Correct any environmental errors or report this problem to a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDC039I

* **Full message** - ZDC039I @@ AUTOMATIC RESTART NOT SUPORTED ON THIS SYSTEM
* **Explanation** - An attempt to issue IXCARM macro has resulted in a return code indicating that ARM support is not available on this system, or it may be available but stopped.
* **System action** - Processing continues but without ARM support.
* **User response** - See the **z/OS MVS Sysplex Services Reference** for a complete list of the possible return and reason codes. You might need to issue the operator command `SETXCF START,POLICY,TYPE=ARM` to activate ARM processing.

## ZDC040I

* **Full message** - ZDC040I @@ DEREGISTERED FOR AUTOMATIC RESTART
* **Explanation** - This message indicates that an `IXCARM` has been issued in order for the server to go to a normal end of job.
* **System action** - Processing continues.
* **User response** - None

## ZDC048I

* **Full message** - ZDC048I THE FOLLOWING MODULES ARE LOADED INTO ECSA
* **Explanation** - This message is printed in the `SYSPRINT` data set and indicates that all modules named next via `ZDC009I` messages were loaded into ECSA.
* **System action** - Processing continues.
* **User response** - None

## ZDC049I

* **Full message** - ZDC049I THE FOLLOWING MODULES ARE LOADED INTO PRIVATE STORAGE
* **Explanation** - This message is printed in the `SYSPRINT` data set and indicates that all modules named next via `ZDC009I` messages were loaded into the private area of the zDC.
* **System action** - Processing continues.
* **User response** - None

## ZDC052I

* **Full message** - ZDC052I zDC IS RUNNING ON @@ RELEASE @@
* **Explanation** - This informational message indicates the name and release level on which this zDC is running.
* **System action** - Processing continues.
* **User response** - None

## ZDC053I

* **Full message** - ZDC053I LPAR NAME @@ CVTSNAME @@
* **Explanation** - This informational message indicates the name of the LPAR on which this zDC is running and the name of the operating system on which this zDC is running.
* **System action** - Processing continues.
* **User response** - None

## ZDC054E

* **Full message** - ZDC054E zDC ACTIVE SUBSYSTEM @@ ALREADY MARKED AS DEFAULT
* **Explanation** - This message indicates that during the process of establishing a new zDC subsystem on this LPAR, a previous subsystem named in the message was already active and marked as the default subsystem.
* **System action** - zDC execution ends.
* **User response** - Only one zDC subsystem at a time can be marked as the default. Change the parameter specification of this zDC to indicate `DEFAULT(NO)` and re-execute the zDC. You can also stop the zDC job with the named subsystem, which allows another subsystem to specify it as the default one. Note, that if the zDC instance with the subsystem named is unable to be cancelled or if it has been cancelled and its subsystem remains active, then you can specify `DEFAULT(YES,FORCE)`. The existing subsystem is marked as not the default and the new one is marked as the default.

## ZDC055I

* **Full message** - ZDC055I LPAR CPU capacity MSUs per hour:@@. If z/VM guest, capacity:@@
* **Explanation** - This informational message indicates the MSU capacity on which this zDC is running. If running as z/VM guest, shows guest MSU capacity.
* **System action** - Processing continues.
* **User response** - None

## ZDC056I

* **Full message** - ZDC056I LPAR General Processors:@@, ZIIPs:@@
* **Explanation** - This informational message indicates the processors vailable to LPAR and how many of them are ZIIP speciality processors.
* **System action** - Processing continues.
* **User response** - None

## ZDC057I

* **Full message** - ZDC057I LPAR Facility Indicators in hexdump format:
* **Explanation** - Facilities installed in the configuration. Hex dump of the area to assist issue diagnosis. See STORE FACILITY LIST EXTENDED (STFLE) instruction
* **System action** - Processing continues.
* **User response** - None

## ZDC059I

* **Full message** - ZDC059I zDC NOW EXECUTING UNDER USERID @@
* **Explanation** - This message is written to SYSPRINT indicating that the user ID you specified in `TCPIP_USERID` is now in control of the main task of the zDC.
* **System action** - Processing continues.
* **User response** - None

## ZDC060I

* **Full message** - ZDC060I LOG @@ @@ SUCCESSFULLY
* **Explanation** - This message is written to `SYSPRINT` indicating that the action you requested in a `LOG` command has been successfully executed.
* **System action** - Processing continues.
* **User response** - None

## ZDC061E

* **Full message** - ZDC061E INSUFFICIENT ACCESS TO LOG DATA SET. SEE JOBLOG
* **Explanation** - This message is written to `SYSPRINT` indicating that the `USERID`under which zDC is running does not have the necessary security access to the log data set. This access must be `ACCESS(ALTER)` in order that the log data set can be created and/or extended and be available.
* **System action** - Processing continues but without the log.
* **User response** - Either grant the user ID under which zDC is running ACCESS(ALTER) to the log data set or supply a user ID that has this access level. Note that the log data set must be defined as a generic entity in order to pass the RACROUTE used in zDC.

## ZDC062E

* **Full message** - ZDC062E LOG TASK INITIALIZATION FAILURE RC=@@/@@
* **Explanation** - This message is written to `SYSPRINT` indicating that the log subtask has failed to initialize.
* **System action** - zDC processing continues but without the log.
* **User response** - Scan the system console and the JES job log for messages relating to this problem. Look carefully for any system access `(RACF, ACF/2, TOPSECRET)` messages relating to the log data set.

## ZDC064E

* **Full message** - ZDC064E QUEUE TASK INITIALIZATION FAILURE
* **Explanation** - This message is written to `SYSPRINT` indicating that the queue subtask has failed to initialize.
* **System action** - zDC terminates.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDC065I

* **Full message** - ZDC065I zDC INITIALIZATION SUCCESSFUL. RETCODE=00/00 @@
* **Explanation** - This message is written to SYSPRINT indicating that initialization of the zDC has been successful.
* **System action** - Processing continues.
* **User response** - None

## ZDC066E

* **Full message** - ZDC066E QUEUE TASK FAILURE RETCODE=@@/@@
* **Explanation** - This message is written to `SYSPRINT` indicating that the queue subtask has failed. Return and reason codes are contained in this message.
* **System action** - zDC terminates.
* **User response** - If `"QUEUE"=DtAgt`, in the message, review the following: \* The zDC task tries to connect to the zRemote. One of the first things it does is bootstrap the zLocal from the server using the zRemote. If the bootstrapping fails, meaning that the zLocal can't be loaded, the zDC task tries three times then issues a user abend. The fallback is that if this happens, the zDC tries to load the most recently bootstrapped zLocal. If it is the first time the zDC has been started in a new work area on the OMVS filesystem, and there is no previously downloaded zLocal, then this user abend is issued. \* Check that the zRemote code module parameter in the zDC `//SYSIN` is correct. This needs to point to the zRemote instance, which needs to be up and running, and connected to a server, so that the zLocal bootstrapping can happen. \* Review the zDC spool output for bootstrap messages. If `"QUEUE"=QUEUE`, in the message, report this message to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC067E

* **Full message** - ZDC067E LOG TASK FAILURE RETCODE=@@/@@
* **Explanation** - This message is written to `SYSPRINT` indicating that the log subtask has failed. Return and reason codes are contained in this message.
* **System action** - Processing continues but without the log.
* **User response** - Scan the system console and the JES job log for messages relating to this problem. Look carefully for any system access `(RACF, ACF/2, TOPSECRET)` messages relating to the log data set.

## ZDC069W

* **Full message** - ZDC069W zDC QUEUE IS AT @@% OF CAPACITY
* **Explanation** - This message indicates that the queue is filling. New internal events are not accepted once the queue reaches 100%. This message first displays when the queue reaches 75% and it re-displays at each 5% interval. When the queue drops below 75%, this message is no longer displayed. This message appears on the system console as well as in the SYSPRINT data set.
* **System action** - Execution continues.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDC071W

* **Full message** - ZDC071W UNABLE TO CONSTRUCT SDUMPX SYMREC RETCODE=@@/@@
* **Explanation** - This message indicates that the `ZDCSDUMP` module could not create a symptom record to be included in the `SDUMP` that it was about to write.
* **System action** - The dump is created but without a symptom record.
* **User response** - None

## ZDC072W

* **Full message** - ZDC072W WLM ENCLAVE CREATION FAILED. @@ @@/@@
* **Explanation** - This message indicates that the process to create an WLM enclave has not been successful. The function name is shown in the message along with the return and reason codes from execution of this function. This is a warning message only because execution of the zDC continues. See below.
* **System action** - zDC execution continues but all processing is performed in task mode and the enclave SRB is not dispatched. Hence there is no execution on any zIIP.
* **User response** - Report this message to your systems programmer who might need to contact a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC073I

* **Full message** - ZDC073I WLM ENCLAVE @@ CREATED SUCCESSFULLY
* **Explanation** - This message indicates that the process to create an WLM enclave has been successful and zDC is a member of the enclave named in the message.
* **System action** - Processing continues.
* **User response** - None

## ZDC074E

* **Full message** - ZDC074E WLM ENCLAVE DELETION FAILED. @@ @@/@@
* **Explanation** - This message indicates that the process to delete a WLM enclave has not been successful. The function name is shown in the message along with the return and reason codes from the execution of this function.
* **System action** - zDC execution ends.
* **User response** - Report this message to your systems programmer who might need to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC076E

* **Full message** - ZDC076E WLM ENCLAVE SRB EXECUTION FAILED. RETCODE=@@
* **Explanation** - This message indicates that the enclave SRB has failed to execute correctly. If the RETCODE in this message is `1C`, then message `ZDC077` is written next with the details concerning the failure.
* **System action** - zDC execution ends.
* **User response** - Report this message to your systems programmer who might need to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC077E

* **Full message** - ZDC077E WLM ENCLAVE SRB REASON CODES=@@ @@ @@
* **Explanation** - The three codes in this message correspond to the `IEAMSCHD` `SYNCHCOMPADDR`, `SYNCHCODEADDR` and `SYNCHRSNADDR` values.
* **System action** - zDC execution ends.
* **User response** - Report this message to your systems programmer who might need to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC078W

* **Full message** - ZDC078W QUERT.STAWXXX UNEXPECTED @@ DISPATCH DELAY @@ @@ @@ @@
* **Explanation** - This message is written to `SYSPRINT` indicating that the zDC appears to be getting insufficient processor service to handle messages in a timely fashion.
* **System action** - Processing continues.
* **User response** - There are 2 formats of the message followed by 4 hex words: \* {QueRt.StaWDGp Unexpected GP dispatch delay} \* {QueRt.StaWZSp Unexpected ZIIP dispatch delay} GP is general processor delay, while ZIIP is IBM's Systems Integrated Information Processor. The first 2 hex words are a 64bit number in STCK format with the sum of the unexpected delays. (Convert to decimal and divide by 4096 to getmicro-seconds) The 3rd and 4th word are a count of unexpected delays and a count of how may times the delay has been evaluated. The average unexpected delay is the 64bit sum divided by the unexpected delay count. For example: `ZDC078W QueRt.StaWDGp Unexpected GP dispatch` delay 00000000 F7E0822C 00000003 000019E2. xF7E0822C/x00000003=1.015sec/3=.338sec average unexpected delay base on x19E2/6,626 observations. By default, he message will display at most once every 10 minutes. An unexpected delay defaults to .25 sec. That is, a task goes into a wait for 2 seconds and gets control back after over 2.25 seconds. zDC parm: `ZDCDISPATCHDELAYWARN(25)` sets delay threshold in .01 second units e.g. 25=250 milli-sec. zDC parm: `ZDCDISPATCHDELAYRPTM(10)` sets reporting interval in minutes. Generally, use your performance tools to look for workflow delays in the 10 minute window before the warning message (for example, IBM's RMF monitor III). Also, check PARMLIB member `IEAOPTxx` parameter: `IIPHONORPRIORITY=NO`. NO can cause ZIIP eligible work to be delayed if GP processors are available.

## ZDC079W

* **Full message** - ZDC079W IEAVRLS ERROR, RETURN CODE @@
* **Explanation** - This message indicates that and internal release function didn't complete properly.
* **System action** - Processing continues.
* **User response** - If the issue persists, save the information in this message and contact your systems programmer or a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC083E

* **Full message** - ZDC083E SUBSYSTEM @@ ALREADY EXISTS BUT IS NOT A zDC SUBSYSTEM
* **Explanation** - This message indicates that the 4-character subsystem ID you specified in the `//SYSIN DD` parameter data set already exists on your system but is used by some other program that is not Dynatrace zDC.
* **System action** - zDC terminates.
* **User response** - Ensure that the subsystem ID you have specified is unique on your system then restart zDC.

## ZDC100I

* **Full message** - ZDC100I SYSIN PARAMETER LISTING
* **Explanation** - This message indicates that the `//SYSIN` parameters specified by the customer are listed next.
* **System action** - Processing continues.
* **User response** - None

## ZDC101I

* **Full message** - ZDC101I END OF SYSIN PARAMETER LISTING TRANBUF-Megabytes=@@
* **Explanation** - This message indicates that the `//SYSIN` parameters specified by the customer have all been previously listed.
* **System action** - Processing continues.
* **User response** - None

## ZDC102E

* **Full message** - ZDC102E SYSTEM VARIABLE SUBSTITUTION FAILED. @@
* **Explanation** - During the parsing of the `//SYSIN DD` data, the z/OS system variable substitution routine is called for each parameter. A non-zero return code resulted from one of these calls.
* **System action** - zDC execution ends.
* **User response** - Correct the parameter in error and re-execute the zDC.

## ZDC103E

* **Full message** - ZDC103E UNABLE TO OPEN //SYSIN DATA SET
* **Explanation** - The attempt to open the `SYSIN` data set failed. There is no return code associated with this error but a message may be displayed in the job log that better explains the error.
* **System action** - zDC execution ends.
* **User response** - Ensure that the `//SYSIN DD` statement exists in the JCL used to invoke zDC and ensure that it points to a data set with DCB characteristics of `LRECL=80`.

## ZDC105E

* **Full message** - ZDC105E ILLOGICAL SEQUENCE OF COMMENT CONTROL CHARACTERS
* **Explanation** - Comment control characters are "/*" to begin a comment and "*/" to end a comment. These must be paired; one of each. All statements between this pair are treated as a comment. This message indicates that the pairing of these control sequences is not correct.
* **System action** - zDC execution ends.
* **User response** - Correct the comment pairing error and re-execute the zDC.

## ZDC106E

* **Full message** - ZDC106E UNKNOWN SYSIN KEYWORD @@
* **Explanation** - The `SYSIN` keyword shown in the message text is not one of the valid keywords.
* **System action** - zDC execution ends.
* **User response** - Correct the keyword in the `SYSIN` data set and re-execute the zDC.

## ZDC107E

* **Full message** - ZDC107E SUBSYSTEM\_ID PARAMETER MISSING
* **Explanation** - The `SUBSYSTEM_ID` parameter names a unique 4-character name for this zDC instance. This name must not be duplicated on this LPAR, and must NOT be defined in the `SYS1.PARMLIB IEFSSNxx` member.
* **System action** - zDC execution ends.
* **User response** - Add the SUBSYSTEM\_ID parameter to the `//SYSIN` data set and re-execute the zDC. This 4-character name must be unique across all subsystems running on this LPAR but may be the same on different LPARs. You may name all your zDC subsystems with the same name on each LPA. But on any one LPAR this name must be unique. Do not define this name in the `IEFSSNxx SYS1.PARMLIB` member.

## ZDC110E

* **Full message** - ZDC110E NAME PARAMETER MISSING
* **Explanation** - The `NAME` parameter is required and must specify a name for this zDC that is meaningful to personnel in your enterprise who may see messages from this zDC. The value you specify in the `NAME` parameter is not used for any purpose except to uniquely identify this instance of the zDC.
* **System action** - zDC execution ends.
* **User response** - Add the `NAME` parameter and re-execute the zDC.

## ZDC116E

* **Full message** - ZDC116E AUTOMATIC RESTART MANAGEMENT NAME MISSING
* **Explanation** - You have specified `ARM(YES)` but have not specified the name to be used for Automatic Restart Management. This name must be from 1 to 16 bytes long. zDC registers with the z/OS automatic restart management and is then eligible for this facility. This name can consist of uppercase letters, numbers, and the following special characters: underscore (`_`), dollar sign (`$`), pound sign(`#`), or At sign (`@`). The first character cannot be numeric.
* **System action** - zDC execution ends.
* **User response** - See *z/OS V1Rn.0 MVS Setting Up a Sysplex* for a complete discussion of how an installation invokes this facility. When all of the steps outlined in this manual have been followed, then add the `ARM_NAME` parameter and re-execute the zDC. In the meantime, specify `ARM(NO)` or omit the parameter.

## ZDC121E

* **Full message** - ZDC121E SUBSYSTEM\_ID PARAMETER INVALID
* **Explanation** - The SUBSYSTEM\_ID parameter has been specified but is not valid. The value for this parameter must be 4 bytes long consisting only of uppercase letters and numbers and dollar sign (`$`), pound sign(`#`), or At sign (`@`). The first character must be a letter.
* **System action** - zDC execution ends.
* **User response** - Correct the `SUBSYSTEM_ID` parameter and re-execute the zDC.

## ZDC122E

* **Full message** - ZDC122E DISPLAY\_NAME PARAMETER INVALID
* **Explanation** - The `DISPLAY_NAME` parameter has been specified, but is not valid. The value for this parameter must be from 1 to 40 bytes long. Any displayable characters are valid.
* **System action** - zDC execution ends.
* **User response** - Correct the `DISPLAY_NAME` parameter and re-execute the zDC.

## ZDC123E

* **Full message** - ZDC123E DEFAULT PARAMETER INVALID
* **Explanation** - The `DEFAULT` parameter has been specified, but is not valid. Only two values are allowed: `YES` or `NO`. Only one zDC instance in a given LPAR may specify that it is the default; all others must specify NO.
* **System action** - zDC execution ends.
* **User response** - Correct the `DEFAULT` parameter and re-execute the zDC.

## ZDC125E

* **Full message** - ZDC125E EVENT\_WAIT PARAMETER INVALID
* **Explanation** - The EVENT\_WAIT parameter can only specify `YES` or `NO`. If this parameter is omitted `YES` is assumed. An EVENT\_WAIT specified as `YES` or allowed to default to `YES` indicates that when events are processed, programs are kept from continuing their execution until the event has been successfully processed by the zDC address space. In most cases this is the desirable option. If it is determined that too much time is lost while zDC is processing the event, then specify `NO` to this parameter. The liability is that events may be lost if zDC terminates abnormally.
* **System action** - zDC execution ends.
* **User response** - Correct the `EVENT_WAIT` parameter and re-execute the zDC.

## ZDC126E

* **Full message** - ZDC126E TCPIP\_USERID PARAMETER INVALID
* **Explanation** - The `TCPIP_USERID` parameter must specify a 1- to 8-character valid user ID. You may omit this parameter in which case the user ID under which zDC was submitted is used.
* **System action** - zDC execution ends.
* **User response** - Either correct the user ID parameter or omit it entirely. re-execute the zDC.

## ZDC127E

* **Full message** - ZDC127E LOG\_INITIAL PARAMETER INVALID
* **Explanation** - The `LOG_INITIAL` parameter must specify either `(OPEN)` `(CLOSED)` or `()`. Any other values are invalid. If you omit this parameter or specify `()`, the default is`LOG_INITIAL(CLOSED)`. Specify all the other parameters for logging that are applicable to your SMS environment, and also specify `LOG_INITIAL(CLOSED)`. You can dynamically start logging using the specified parameters if the need arises. With the log in a `CLOSED` state no system resources are consumed.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_INITIAL` parameter and re-execute the zDC.

## ZDC128E

* **Full message** - ZDC128E LOG\_DSNAME PARAMETER IS INVALID
* **Explanation** - The `LOG_DSNAME` parameter must specify a 1 to 35- character data set name for the optional logging. Be sure you haven't specified more than 35 characters because `IDCAMS` appends a `.DATA` and a `.INDEX` to this name when the cluster is defined.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_DSNAME` and re-execute the zDC.

## ZDC130E

* **Full message** - ZDC130E LOG\_VOLSER PARAMETER IS INVALID
* **Explanation** - The `LOG_VOLSER` parameter must specify a 6-character volume serial number for the volume on which the log is to be defined. You must specify this parameter only if your SMS environment dictates it, else you may omit this parameter and take your system defaults.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_VOLSER` and re-execute the zDC.

## ZDC131E

* **Full message** - ZDC131E LOG\_TRKS PARAMETER IS INVALID
* **Explanation** - The `LOG_TRKS` parameter must specify a 1 to 8-digit number representing the number of tracks you want defined in the primary and secondary extents of the log data set. The maximum value for this parameter is `65535` and the minimum value is 1.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_TRKS` and re-execute the zDC.

## ZDC132E

* **Full message** - ZDC132E LOG\_CYLS PARAMETER IS INVALID
* **Explanation** - The `LOG_CYLS` parameter must specify a 1 to 8-digit number representing the number of cylinders you want defined in the primary and secondary extents of the log data set. The maximum value for this parameter is `65535` and the minimum value is 1.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_CYLS` and re-execute the zDC.

## ZDC133E

* **Full message** - ZDC133E LOG\_MGMTCLASS PARAMETER IS INVALID
* **Explanation** - The `LOG_MGMTCLASS` parameter must specify a 1- to 8-character name for the management class SMS parameter that is defined in your installation for the log data set.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_MGMTCLASS` parameter and re-execute the zDC.

## ZDC134E

* **Full message** - ZDC134E LOG\_DATACLASS PARAMETER IS INVALID
* **Explanation** - The `LOG_DATACLASS` parameter must specify a 1- to 8-character name for the data class SMS parameter that is defined in your installation for the log data set.
* **System action** - zDC execution ends.

## ZDC135E

* **Full message** - ZDC135E LOG\_STORCLASS PARAMETER IS INVALID
* **Explanation** - The `LOG_STORCLASS` parameter must specify a 1- to 8-character name for the storage class SMS parameter that is defined in your installation for the log data set.
* **System action** - zDC execution ends.
* **User response** - Correct the `LOG_STORCLASS` parameter and re-execute the zDC.

## ZDC155E

* **Full message** - ZDC155E ARM PARAMETER INVALID
* **Explanation** - The `ARM` parameter must specify either `ARM(YES)`, if you want Automatic Restart Management to restart this zDC in case of abnormal termination, or `ARM(NO)`, if you do not want the zDC restarted. Initially you should specify `ARM(NO)` until you have assured yourself that the zDC is working correctly under normal circumstances. When this is the case you can request `ARM` support.
* **System action** - zDC execution ends.
* **User response** - Correct the `ARM` parameter and re-execute the zDC

## ZDC156E

* **Full message** - ZDC156E ARM\_ELEMENT\_NAME PARAMETER INVALID
* **Explanation** - The `ARM_ELEMENT_NAME` parameter specifies a 1- to 16- character name to be used by z/OS in identifying this program to the Automatic Restart Management system. Only letters and numbers and the special characters `_`, `$`, `#` and `@` are valid. In addition, the first byte must not be numeric.
* **System action** - zDC execution ends.
* **User response** - Correct the `ARM_ELEMENT_NAME` parameter and re-execute the zDC.

## ZDC185E

* **Full message** - ZDC185E PROTECT PARAMETER INVALID
* **Explanation** - The `PROTECT` parameter must specify `PROTECT(YES)` if pages in extended common storage are to be protected from inadvertent alteration by other programs running in the `LPAR` or `PROTECT(NO)` if this protection is not to occur. If this parameter is omitted then no protection exists. Any program running in key 0 can alter this storage.
* **System action** - zDC execution ends.
* **User response** - Correct the `PROTECT` parameter and re-execute the zDC.

## ZDC187E

* **Full message** - ZDC187E DEFAULT PARAMETER MISSING
* **Explanation** - The `DEFAULT` parameter is required as either `DEFAULT(YES)` or `DEFAULT(NO)`. Only one zDC subsystem in the LPAR can specify `DEFAULT(YES)`. All others must specify `DEFAULT(NO)`.
* **System action** - zDC execution ends.
* **User response** - Add the `DEFAULT` parameter and re-execute the zDC.

## ZDC189E

* **Full message** - ZDC189E OPERATING\_SYSTEM PARAMETER INVALID
* **Explanation** - The `OPERATING_SYSTEM` parameter should never be specified at a customer parameter. Its use is only for emulating releases of z/OS earlier than the current one.
* **System action** - zDC ends.
* **User response** - Remove this parameter from the `SYSIN` data set.

## ZDC193E

* **Full message** - ZDC193E TCPIP\_INTF PARAMETER INVALID
* **Explanation** - The TCPIP\_INTF parameter specifies the TCPIP interface name or IPV4 address. It has a maximum length of 16 characters.
* **System action** - zDC ends.
* **User response** - Correct the TCPIP\_INTF parameter and resubmit zDC.

## ZDC194E

* **Full message** - ZDC194E zIIP\_ENABLE PARAMETER INVALID
* **Explanation** - The `zIIP_ENABLE` parameter can specify `YES` or `NO`. If `zIIP_ENABLE(YES)` is specified, then the SRB under which all XML creation and TCP/IP SOCKET(SEND) routines run is zIIP enabled. This SRB is not run on your zIIP if set to NO.
* **System action** - zDC execution ends.
* **User response** - Correct the `zIIP_ENABLE` parameter and resubmit zDC.

## ZDC196E

* **Full message** - ZDC196E DTMSG\_QSIZE PARAMETER IS INVALID
* **Explanation** - The `DTMSG_QSIZE` parameter specifies a Data Space size in Kilobyte. The default is 1024 (1024K). This Data Space is used to queue messages from the CICS code module of OneAgent to the zLocal. The minimum value is 8 and the maximum is 262144K (256Megabytes).
* **System action** - zDC execution ends.
* **User response** - Specify a value in the range given.

## ZDC197E

* **Full message** - ZDC197E DTMSG\_SMOSIZE PARAMETER IS INVALID
* **Explanation** - The `DTMSG_SMOSIZE` parameter specifies a 64-bit SMO size in MB. The default is 1 MB. This 64-bit SMO is used to queue messages from the CICS code module to the zLocal. The minimum value is 1 and the maximum is 256 MB. (256 Megabytes).
* **System action** - zDC execution ends.
* **User response** - Choose a correct value for `SMOSIZE` and then resubmit zDC.

## ZDC198E

* **Full message** - ZDC198E DT\_UMASK PARAMETER IS INVALID
* **Explanation** - The `DT_UMASK` parameter specifies user file-creation mask. The default is 0022(octal) and corresponds to rwxr-xr-x permission for new files. Error is generated if the parameter is over 3 characters, or contain non-octal characters (o:7).
* **System action** - zDC execution ends.
* **User response** - Choose a correct value for `DT_UMASK` and then resubmit zDC.

## ZDC199E

* **Full message** - ZDC199E DTMSG\_TBCSIZE PARAMETER IS INVALID
* **Explanation** - The `DTMSG_TBCSIZE` parameter specifies a 64-bit Transaction buffer total size in MB and either a 2K or 4K buffer size. The default is `(1,2)`, which stands for 1MB and 2K buffer. This 64-bit SMO is used to buffer messages related to a transaction before being sent to OneAgent. The minimum value is 1 and the maximum is 256 MB (256Megabytes).
* **System action** - zDC execution ends.
* **User response** - Choose a correct value for `TBCSIZE` and then resubmit zDC.

## ZDC200I

* **Full message** - ZDC200I DTMSG\_QSIZE PARAMETER IS DEPRECATED
* **Explanation** - The `DTMSG_QSIZE` parameter specified DataSpace size in Kilobytes It is replace by `DTMSG_SMOSIZE(Megabytes)` The parameter has been converted to Megabytes and used to set the SMO size.
* **System action** - zDC execution continues.
* **User response** - Use `DTMSG_SMOSIZE` in the future.

## ZDC201E

* **Full message** - ZDC201E ZDCLOGBUFFERSIZE PARAMETER IS INVALID
* **Explanation** - `ZDCLOGBUFFERSIZE` specifies a log buffer in kilobytes. It is a SMO memory are areas to buffer the zDC `.log` file. The zDC .log file in the same directory as the ZLocal code module `.log` files. The default is (64) - 64K. The minimum is 16K, the maximum is 10240K =10M.
* **System action** - zDC execution ends.
* **User response** - Correct value for `ZDCLOGBUFFERSIZE` and resubmit.

## ZDC202E

* **Full message** - ZDC202E ZDCMAXLOGFILESIZE PARAMETER IS INVALID
* **Explanation** - `ZDCMAXLOGFILESIZE` specifies the log file size limit. It is used to rotate to a new log file when exceeded. The ZDClogfile pattern: `.._ZDCID_PID_.#.log`, for example: `dt_DTV1ZDC4_MEPC_33620088.1.log`. The default is (10240) =10M. The minimum is 10K; the maximum is 1048576K =1G.
* **System action** - zDC execution ends.
* **User response** - Correct value for `ZDCMAXLOGFILESIZE` and resubmit.

## ZDC203E

* **Full message** - ZDC203E ZDCDISPATCHDELAYWARN PARAMETER IS INVALID
* **Explanation** - `ZDCDISPATCHDELAYWARN` specifies an unexpected dispatch delay threshold in units of .01sec. For example, `ZDCDISPATCHDELAYWARN(100)` specifies 1sec. The default is (25) =.25sec. The minimum non-zero valuse is 10 =.1sec. The maximum is (32000) =320sec. Disable delay checking: `ZDCDISPATCHDELAYWARN(0)`
* **System action** - zDC execution ends.
* **User response** - Correct value for `ZDCDISPATCHDELAYWARN` and resubmit.

## ZDC204E

* **Full message** - ZDC204E ZDCDISPATCHDELAYRPTM PARAMETER IS INVALID
* **Explanation** - `ZDCDISPATCHDELAYRPTM` specifies a minimum report interval for unexpected dispatch delay in minutes. If no exceptions occur, no warning is reported. For example, `ZDCDISPATCHDELAYRPTM(15)` reports delays at most every 15 minutes. The default is (10) =10Minutes The minimum is (1) (not recommended, small) The maximum is (32000) (over 533Hours)
* **System action** - zDC execution ends.
* **User response** - Correct value for `ZDCDISPATCHDELAYRPTM` and resubmit.

## ZDC205E

* **Full message** - ZDC205E ZEDC\_COMPRESS PARAMETER IS INVALID
* **Explanation** - The `ZEDC_COMPRESS` parameter may specify a 1- or 2-digit number representing the minimum size for a data block to be eligible for zEDC hardware assisted data compression. Smaller blocks will be sent without compression. A null argument may be specified to enable hardware data compression using the 8K default minimum block size.
* **System action** - zDC execution ends.
* **User response** - Correct the ZEDC\_COMPRESS parameter and re-execute the zDC.

## ZDC206E

* **Full message** - ZDC206E TCP\_BUFFER PARAMETER IS INVALID
* **Explanation** - The `TCP_BUFFER` parameter specifies a 1- to 4-digit number representing the size of the buffer that is used to pass OneAgent data to TCP/IP.
* **System action** - zDC execution ends.
* **User response** - Correct the `TCP_BUFFER` parameter and re-execute the zDC.

## ZDC207E

* **Full message** - ZDC207E ZEDC\_COMPRESS MUST BE SMALLER THAN TCP\_BUFFER
* **Explanation** - The minimum compression threshold must be smaller than the size of the TCP/IP buffer.
* **System action** - zDC execution ends.
* **User response** - Correct one of the parameters and re-execute the zDC.

## ZDC208I

* **Full message** - ZDC208I METRIC\_INTERVAL PARAMETER IS INVALID
* **Explanation** - \* The minimum interval is 10 seconds. \* The maximum interval is 600 seconds. Specify a zero value to disable metrics processing.
* **System action** - Processing continues.
* **User response** - Correct the parameter and re-execute the zDC.

## ZDC209I

* **Full message** - ZDC209I DISPLAY\_INTERVAL PARAMETER IS INVALID
* **Explanation** - \* The minimum interval is 10 seconds. \* The maximum interval is 600 (seconds). \* Specify a zero value to disable AutoDisplay processing.
* **System action** - Processing continues.
* **User response** - Correct the parameter and re-execute the zDC.

## ZDC210I

* **Full message** - ZDC210I zDC NO LONGER LINKED TO TCP/IP
* **Explanation** - This informational message indicates that the TERMAPI macro was successfully executed to terminate TCP/IP communications.
* **System action** - Processing continues.
* **User response** - None

## ZDC211E

* **Full message** - ZDC211E DTMSG\_TRANBUFSIZE PARAMETER IS INVALID
* **Explanation** - The `DTMSG_TRANBUFSIZE` parameter specifies a Transaction buffer total size in thousands of buffers and either a 2K or 4K buffer size. The default is `(1,2)`, which stands for 1 thousand 2K buffers. This 64-bit SMO is used to buffer messages related to a transaction before being sent to the zLocal. The minimum value is `(1,2)`, maximum is `(126,4)` or `(248,2)` (512Megabytes).
* **System action** - zDC execution ends.
* **User response** - Choose a correct value for `DTMSG_TRANBUFSIZE` and resubmit.

## ZDC212E

* **Full message** - ZDC212E zremote= IS REQUIRED IN DTAGTCMD
* **Explanation** - A zRemote code module parameter is required. The zRemote code module properties such as host and port are not specified in the `DTAGTCMD` parameter.
* **System action** - zDC is terminated.
* **User response** - Add `zremote=` to `DTAGTCMD` resubmit zDC.

## ZDC213W

* **Full message** - ZDC213W TCP\_BUFFER PARAMETER IS OUT OF RANGE, SETTING 8K or 256K
* **Explanation** - The TCP\_BUFFER parameter must be in range from 8k to 256k. If less than 8k is specified, 8k is used. If more than 256k is specified, 256k is used.
* **System action** - Processing continues.
* **User response** - Correct the TCP\_BUFFER parameter for next ZDC execution.

## ZDC215I

* **Full message** - ZDC215I TERMINATION STARTED FOR zDC @@
* **Explanation** - This informational message indicates that termination processing has started for this zDC.
* **System action** - Termination processing continues.
* **User response** - None

## ZDC217I

* **Full message** - ZDC217I LONG TERM STORAGE STATISTICS FOLLOW
* **Explanation** - This informational message is followed by messages that show the number of bytes of storage allocated in each of the designated areas. These numbers may only be approximate as dynamic storage areas are not included in them.
* **System action** - Processing continues.
* **User response** - None

## ZDC218I

* **Full message** - ZDC218I PAGEABLE PRIVATE STORAGE @@
* **Explanation** - The number of bytes of private zDC storage that is allocated long term is shown in this message. This number may only be approximate as dynamic storage areas are not included. Storage allocated both over and under the 16M line are included in this number.
* **System action** - Processing continues.
* **User response** - None

## ZDC219I

* **Full message** - ZDC219I PAGEABLE COMMON STORAGE - CSA: @@ ECSA: @@
* **Explanation** - The number of bytes of subpool 241 (pageable common) storage that has been allocated for the duration of the zDC execution.
* **System action** - Processing continues.
* **User response** - None

## ZDC220I

* **Full message** - ZDC220I FIXED COMMON STORAGE - SQA: @@ ESQA: @@
* **Explanation** - The number of bytes of subpool 245 (fixed common) storage that has been allocated for the duration of the zDC execution.
* **System action** - Processing continues.
* **User response** - None

## ZDC221I

* **Full message** - ZDC221I NUMBER SP 241 PAGES PROTECTED: @@
* **Explanation** - The number of pages in subpool 241 that have had the PGSER PROTECT macro issued against them. This message displays only if you have specified `PROTECT(YES)` in the SYSIN parameter data set.
* **System action** - Processing continues.
* **User response** - None

## ZDC302E

* **Full message** - ZDC302E Message @@ - BAD REC ADDRESS PASSED
* **Explanation** - Validation routines invoked to ensure that each message to the zLocal is valid has detected an error in the data.
* **System action** - If logging is active, the event is logged. This message is written to the user's JOBLOG and the event is discarded.
* **User response** - Please contact a Dynatrace product expert via live chat within your environment.

## ZDC666W

* **Full message** - ZDC666W List of possible zDC CPU contenders
* **Explanation** - This informational message warns that the zDC might be contenting with other work for access to the processors. Up to 6 Job names are shown.
* **System action** - Processing continues. Check with the system performance group about adjusting the zDC priority.
* **User response** - None.

## ZDC667E

* **Full message** - ZDC667E SMF70 host metrics not sent in last SMF INTVAL?
* **Explanation** - This error message warns that the zDC has not seen any SMF Type 70 metric records in the last hour (approximately). Check SMFPRMxx to ensure exits SYS.IEFU86 and SUBSYS.IEFU86 process TYPE 70 records.
* **System action** - Processing continues.
* **User response** - None.

## ZDC668W

* **Full message** - ZDC668W Db2 Stats and Accounting records missing for ~8 hours
* **Explanation** - This error message warns that the zDC has not seen Db2 SMF Type 100/101 records in the last hour (approximately). Check SMFPRMxx to ensure exits SYS.IEFU86 and SUBSYS.IEFU86 process TYPE 70 records.
* **System action** - Processing continues.
* **User response** - None.

## ZDC669E

* **Full message** - ZDC669E Abend S202 detected, zDC must be restarted
* **Explanation** - This error message notifies the operator that the zDC has encountered an S202 abend.
  The zDC is unable to recover and will be shut down automatically. The operator must manually restart
  the zDC.
* **System action** - zDC terminates
* **User response** - Restart zDC.

## ZDC8XXW

* **Full message** - ZDC8XXW INTERNAL MESSAGES FROM TCP MODULE ZDCTCPSP
* **Explanation** - Generally, these are internal diagnostic messages issued when the `DTLOGLEVEL` 2 or less (fine). They may be requested by Dynatrace software support to diagnose an issue.
* **System action** - Processing continues.
* **User response** - None

## ZDC950E

* **Full message** - ZDC950E DT PARAMETER INVALID
* **Explanation** - The parameters `DTPIPEPATH`, `DTCHDIR`, `DTAGTCMD`, or `DTLOG` are invalid. See comments in the supplied sample config member for a description of these parameters.
* **System action** - zDC execution ends.
* **User response** - Correct the parameter and re-execute the zDC.

## ZDC951I

* **Full message** - ZDC951I CICS property update too frequent, under 30sec., discarded
* **Explanation** - There is a limit on how frequently the internal tables that contain CICS properties can be updated. The current limit is 30 seconds.
* **System action** - Informational, processing continues.
* **User response** - Re-apply the update later.

## ZDC952W

* **Full message** - ZDC952W zDC zLocalâ¦ {BufferâType} is at @@% of capacity
* **Explanation** - This message indicates that the queue is filling and you should be aware that, if it reaches 100%, new messages won't be sent to the zLocal, possibly causing distribute trace corruption. This message first displays when the queue reaches 70% and re-displays at five percent increments. When utilization drops below 70%, this message no longer displays. Note that this message appears on the system console as well as in the `SYSPRINT` data set.
* **System action** - Execution continues.
* **User response** - Monitor these messages carefully. \* If the **{BufferâType};** is `Trans Buffer Que`, consider increasing zDC parameter: `DTMSG_TRANBUFSIZE()`. \* If the **{BufferâType};** is `SMO Buffer Space`, consider increasing zDC parameter: `DTMSG_SMOSIZE()`.

## ZDC953I

* **Full message** - ZDC953I ZIIP\_ENABLE requires zremote=, ZIIP\_ENABLE NO forced
* **Explanation** - ZIIP enablement requires remote agent option.
* **System action** - Informational, processing continues.
* **User response** - ZIIP enablement requires both the zremote= in the DTABGCMT command line and ZIIP\_ENABLE(YES) in the zDC SYSIN parameters.

## ZDC954W

* **Full message** - ZDC954W DT PARAMETER SYSLOG INVALID
* **Explanation** - Dynatrace parameter `SYSLOG` is invalid. Only `CONNECTSTATUS` or `()` to disable the option are allowed.
* **System action** - Informational, processing continues.
* **User response** - Remove the parameter or code allowed values.

## ZDC955L

* **Full message** - ZDC955L Dynatrace connection being processed ZDC-Job/ID: @@/@@
* **Explanation** - zLocal code module has connected though the zRemote code module to the Dynatrace server.
* **System action** - Informational, processing continues.
* **User response** - None

## ZDC956E

* **Full message** - ZDC956E Dynatrace zLocal agent disconnected from Dynatrace Server ZDC-Job/ID:@@/@@
* **Explanation** - zLocal code module has disconnected from the Dynatrace server.
* **System action** - Informational, processing continues.
* **User response** - If this is not planned, investigate the outage.

## ZDC957I

* **Full message** - ZDC957I Dynatrace Check Agent Mapping. Capture Events disabled for xxxx iAdk. Diag:xxxxxxxx
* **Explanation** - Ignore if expected, otherwise check **Settings** > **Server-side service monitoring** > **Deep monitoring** > **Troubleshooting**.
* **System action** - Informational, processing continues.
* **User response** - None

## ZDC958I

* **Full message** - ZDC958I Dynatrace INIT completed, ZDC AgentId received ZDC-Job/ID:@@/@@
* **Explanation** - ZDC has completed sending INIT msg and received an AgentId response.
* **System action** - Informational, processing continues.
* **User response** - None

## ZDC959I

* **Full message** - ZDC959I The ZDC could not locate the IP in the SMO
* **Explanation** - ZDC could not find the V4 IP address in the SMO. Verify your zLocal is current.
* **System action** - Informational, processing continues.
* **User response** - Confirm zLocal version is current.

## ZDC960L

* **Full message** - ZDC960L The ZDC could not locate the IP using EZA macros @@
* **Explanation** - ZDC could not find the V4 IP address using the IBM EZA tcpip macros.
* **System action** - Processing continues with zero IP address.
* **User response** - If this repeats, please contact Dynatrace support.

## ZDC961L

* **Full message** - ZDC961L Not found TCPIP\_INTF @@, using TCPIP\_USE\_PRIMARY
* **Explanation** - ZDC could not find the V4 IP address using the IBM EZA tcpip macros.
* **System action** - Processing continues with TCPIP\_USE\_PRIMARY value.
* **User response** - If this repeats, please contact Dynatrace support.

## ZDC974E

* **Full message** - ZDC974E Unexpected failure checking agent executable, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. Check that the agent file exists and is executable. See `DTAGTCMD()` parameter.
* **System action** - Processing terminates.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC975E

* **Full message** - ZDC975E zLocal attach failed, Abort
* **Explanation** - This message is written to the SYSPRINT and Oper. Check that the DTAGTCMD parameter references an accessible and executable OneAgent.
* **System action** - Processing terminates.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC976E

* **Full message** - ZDC976E Unexpected failure during change directory, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. Check that the zDC has read+write access to the `DTCHDIR` directory.
* **System action** - Processing terminates.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC977E

* **Full message** - ZDC977E Unexpected failure during z/OS Unix API, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. Check that the user ID that is running the zDC is defined to the security product. The userid is either the normally assigned ID, or overriden by the `TCPIP_USERID` parameter.
* **System action** - Processing terminates.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDC978E

* **Full message** - ZDC978E Failed ZDC.FML Name/Token operation, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. The MVS Name/Token is used for internal processing. The operation failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC979E

* **Full message** - ZDC979E Waiting for Que Data Space failed, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. The Data Space used to pass messages to the ZDC has not initialized.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat within your Dynatrace environment.

## ZDC980E

* **Full message** - ZDC980E Waiting for OMVS failed, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. The OMVS kernel is not ready.
* **System action** - Processing terminates with a dump.
* **User response** - Check why the OMVS address space is not operational. Restart OMVS or delay zDC startup until OMVS is ready.

## ZDC981E

* **Full message** - ZDC981E DtmD.FlagBad internal error, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A critical Data Space process has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC982E

* **Full message** - ZDC982E DtmD.LenBad internal error, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A critical Data Space process has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC983E

* **Full message** - ZDC983E Timer routine critical error, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A critical timer wait function has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC984E

* **Full message** - ZDC984E Critical error in Wait routine, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A Unix wait to check zLocal status has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC985E

* **Full message** - ZDC985E Poll for data failed, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A Unix poll for zLocal messages has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC986E

* **Full message** - ZDC986E Unnamed pipe required, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A Unix unnamed pipe is needed for zLocal communication.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC987E

* **Full message** - ZDC987E Internal error unknown ECB, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A critial internal call function has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC988E

* **Full message** - ZDC988E Unexpected PC return, Abort
* **Explanation** - This message is written to the `SYSPRINT` and Oper. A critial internal call function has failed.
* **System action** - Processing terminates with a dump.
* **User response** - Check job log for additional error messages, correct them if possible. If still unresolved, refer this problem to a Dynatrace product expert via live chat. Please contact a Dynatrace product expert via live chat within your environment.

## ZDC989E

* **Full message** - ZDC989E \*Dbg\*Developer build test message
* **Explanation** - This message is written to the `SYSPRINT` and Oper. It is intended for internal diagnostic for Dynatrace loglevel:finer(1).
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC990I

* **Full message** - ZDC990I Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal diagnostic for `loglevel:finest(0)`.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC991I

* **Full message** - ZDC991I Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:finer(1)`.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC992I

* **Full message** - ZDC992I Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:fine(2)`.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC993I

* **Full message** - ZDC993I Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:config(3)`.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC994I

* **Full message** - ZDC994I Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:info(4)`
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC995W

* **Full message** - ZDC995W Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:warn(5)`.
* **System action** - Informational, processing continues.
* **User response** - If a connection issue, investigate the status of the zRemote code module. Otherwise, informational, processing continues.

## ZDC996E

* **Full message** - ZDC996E Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:severe(6)`.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC997I

* **Full message** - ZDC997I Internal DynaDiag
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic for Dynatrace `loglevel:debug(7)`.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC998I

* **Full message** - ZDC998I @@ @@ @@ @@
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace. Dynatrace product experts might ask that system parameters be changed to cause these messages.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## ZDC999I

* **Full message** - ZDC999I Internal DynaDiag: @@ @@ @@ @@
* **Explanation** - This message is written to the `SYSPRINT`. It is intended for internal Dynatrace diagnostic and shouldn't appear under normal operation. Dynatrace product experts might ask that system parameters be changed to cause these messages.
* **System action** - Informational, processing continues.
* **User response** - Informational, processing continues.

## Related topics

* [Install the zDC subsystem](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zdc "Set up the z/OS Data Collection subsystem (zDC).")