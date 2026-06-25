---
title: z/OS module messages - IMS module system messages
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/zos-code-module-messages/ims-messages
scraped: 2026-05-12T12:13:13.386138
---

# z/OS module messages - IMS module system messages

# z/OS module messages - IMS module system messages

* 3-min read
* Published Mar 22, 2019

### ZDTI032W

|  |  |
| --- | --- |
| Full message | ZDTI032W Recovery routine entered. |
| Explanation | The IMS code module's ABEND recovery routine was invoked by RTM. |
| System action | The ABEND recovery process continues. |
| User response | Please contact a Dynatrace product expert via live chat within your environment. |

### ZDTI033W

|  |  |
| --- | --- |
| Full message | ZDTI033W Successful ABEND recovery, agent disabled. |
| Explanation | The IMS code module's ABEND recovery process was successful. |
| System action | The IMS code module is disabled and the IMS system continues to function. |
| User response | Please contact a Dynatrace product expert via live chat within your environment. |

### ZDTI034E

|  |  |
| --- | --- |
| Full message | ZDTI034E Unable to obtain dynamic storage. |
| Explanation | The IMS code module's ABEND recovery routine was unable to obtain the dynamic storage required to produce ABEND diagnostics. |
| System action | The ABEND recovery process continues but some diagnostic information may not be available. A Software (`SFT`) Error Record further describing the ABEND is written to the z/OS system SYS1.LOGREC data set. |
| User response | Run the z/OS EREP utility program to print the Software (`SFT`) Error Record associated with the ABEND. Please contact a Dynatrace product expert via live chat within your environment. |

### ZDTI035W

|  |  |
| --- | --- |
| Full message | ZDTI035W Retry not permitted, must percolate. |
| Explanation | The z/OS system doesn't allow the IMS code module's ABEND recovery process to continue. |
| System action | The recovery process terminates and percolates (returns control to RTM). |
| User response | Please contact a Dynatrace product expert via live chat within your environment. |

### ZDTI036W

|  |  |
| --- | --- |
| Full message | ZDTI036W ZDTIIInn zzzzzzzz yyyymmdd hh.mm VER vv.rr.mm ABEND at offset xxxxxx. |
| Explanation | An ABEND occurred at offset `xxxxxx` in the `ZDTIIInn` module of the IMS code module, where `nn` corresponds to the IMS version (for example, 12). The remaining fields describe the maintenance level of the IMS code module. |
| System action | A Software (`SFT`) Error Record further describing the ABEND is written to the z/OS system SYS1.LOGREC data set. Optionally, an SVC dump may be taken. The ABEND recovery process continues. |
| User response | Run the z/OS EREP utility program to print the Software (SFT) Error Record associated with the ABEND. Please contact a Dynatrace product expert via live chat within your environment. |

### ZDTI037W

|  |  |
| --- | --- |
| Full message | ZDTI037W ZDTIIInn zzzzzzzz yyyymmdd hh.mm VER vv.rr.mm ABEND offset N/A, no SDWA provided. |
| Explanation | An ABEND occurred in the `ZDTIIInn` module of the IMS code module, where `nn` corresponds to the IMS version (for example, 12). The remaining fields describe the maintenance level of the IMS code module. The ABEND offset could not be determined because no SDWA was provided by RTM. |
| System action | The recovery process terminates and percolates (returns control to RTM). |
| User response | Please contact a Dynatrace product expert via live chat within your environment. |

### ZDTI038W

|  |  |
| --- | --- |
| Full message | ZDTI038W Recovery routine of recovery routine entered. |
| Explanation | While recovering from an ABEND in the IMS code module, the recovery routine encountered an ABEND. |
| System action | The ABEND recovery process continues but does not attempt to produce further diagnostics. The IMS code module is disabled and the IMS system continues to function. |
| User response | Please contact a Dynatrace product expert via live chat within your environment. |

## Related topics

* [Customize CICS and IMS monitoring](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/zos/operation/cics-ims-monitoring "Customize the Dynatrace CICS and IMS monitoring on z/OS.")