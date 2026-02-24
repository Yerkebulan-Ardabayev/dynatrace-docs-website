---
title: Download z/OS product datasets
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/zosmf-installer/download-zos-datasets
scraped: 2026-02-24T21:35:42.008594
---

# Download z/OS product datasets

# Download z/OS product datasets

* Latest Dynatrace
* 5-min read
* Updated on Nov 03, 2023

You can download the PAX file containing the CICS, IMS, z/OS Java, and zDC modules in two ways:

* Dynatrace version 1.272+ Download via [Deployment API](#using-deploymentapi).
* Dynatrace version 1.276+ Download via [web UI](#using-webui).

Starting with OneAgent release 1.275, the PAX file will no longer be published on our FTP server.

## Download the PAX file

You can download the latest or a specific PAX file version via web UI or the [Deployment API](/docs/dynatrace-api/environment-api/deployment/oneagent "Download OneAgent installers via Dynatrace API.") of OneAgent.

The PAX file version must be less than or equal to the zRemote module version.

### Download latest version via web UI

1. Search for **Deploy OneAgent**
2. Select **z/OS** and **Download z/OS product datasets** to download the latest PAX file version.

The file name `dynatrace-zos-1.nnn.m.pax` includes the major release version `nnn` and `m` minor.

### Download a specific version via web UI

You can download a specific PAX file version via web UI as follows:

1. Go to **Settings** > **Monitoring** > **Monitoring overview**.
2. Select **Download Dynatrace OneAgent or ActiveGate installer** and define your preferred version:

   1. Installer: `OneAgent - z/OS`
   2. Build: Select your preferred major version
   3. Revision: Select your preferred minor version

   ![zos monitoring overview](https://dt-cdn.net/images/zos-monitoring-overview-1289-aa537f3578.png)
3. Select **Continue** and **Download z/OS product datasets** to download your defined PAX file version.

   The file name `dynatrace-zos-1.nnn.m.pax` includes the major release version `nnn` and `m` minor.

### Download latest version via Deployment API

You can download the latest PAX file version via Deployment API as follows:

1. Generate an [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the scope **PaaS integration - Installer download** (`InstallerDownload`).
2. Download the latest PAX file via [Deployment API - Download latest OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-latest "Download the latest OneAgent installer via Dynatrace API."):

   Below is a sample `curl` command for a SaaS environment that uses the Deployment API to download the latest PAX file version:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/latest" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Replace `<environment>` with your Dynatrace environment ID and `<accessToken>` with your generated access token.

### Download a specific version via Deployment API

You can download a specific PAX file version via Deployment API as follows:

1. Generate an [Access token](/docs/dynatrace-api/basics/dynatrace-api-authentication#create-token "Find out how to get authenticated to use the Dynatrace API.") with the scope **PaaS integration - Installer download** (`InstallerDownload`).
2. List all available PAX file versions via [Deployment API - List available versions of OneAgent](/docs/dynatrace-api/environment-api/deployment/oneagent/get-available-versions "List available versions of OneAgent via Dynatrace API.").

   Below is a sample `curl` command for a SaaS environment that uses the Deployment API to list all available PAX file versions:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/versions/zos/mainframe" -H "accept: */*" -H "Authorization: Api-Token <accessToken>"
   ```

   Replace `<environment>` with your Dynatrace environment ID and `<accessToken>` with your generated access token.
3. Download a specific PAX file version via [Deployment API - Download OneAgent of specific version](/docs/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version "Download the OneAgent installer of the specific version via Dynatrace API."):

   Below is a sample `curl` command for a SaaS environment that uses the Deployment API to download a specific PAX file version:

   ```
   curl -X GET "https://<environment>.live.dynatrace.com/api/v1/deployment/installer/agent/zos/mainframe/version/<version>" -H "accept: */*" -H "Authorization: Api-Token <accessToken>" --output dynatrace-zos.pax
   ```

   Replace `<environment>` with your Dynatrace environment ID, `<version>` with your selected PAX file version, and `<accessToken>` with your generated access token.

## Extract product datasets

You can extract the product datasets from the PAX file as follows:

1. Transfer the PAX file to your z/OS USS directory in binary mode.
2. Rename the PAX file from `dynatrace-zos-1.nnn.m.pax` to `dynatrace-zos.pax`.
3. Use the `EXTRACT` job below to extract the product datasets from the installation files. Before running the job, modify the following:

   1. Determine the desired high-level qualifier for the install dataset names and set the `HLQ` variable accordingly.
   2. Set `MYUSS` to the z/OS USS directory path where you placed the `dynatrace-zos.pax` file. If the directory path exceeds 42 characters, it might result in an error in the `STEP3` of the job. In such case, you need to modify the JCL to accommodate the continuation character.
   3. Change the volume serial number `VOLSER` to match site standards.

   EXTRACT job

   ```
   //EXTRACT JOB ('ACCTINFO'),'User name or comment',NOTIFY=&SYSUID,



   //             MSGLEVEL=(1,1),CLASS=A,MSGCLASS=X,REGION=0M,



   //             COND=(0,NE)



   //*



   //* !!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



   //*



   //* When upgrading the zDC to version 1.213+ while



   //* the CICS code module is enabled, it is important to follow



   //* the below steps in the given sequence.



   //*



   //* 1. Stop the zDC



   //* 2. Wait for 15 minutes for the CICS code module to



   //*    reset/cleanup the control blocks



   //* 3. Upgrade the zDC to newer version



   //* 4. Start the zDC



   //*



   //* !!!!!!!! IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



   //*



   //* This job extracts the product installation datasets from



   //* the installation files at <MYUSS>/GIMZIP to



   //* <hlq>.<rel>.SZDT* libraries.



   //*



   //* Change the JOB card and the SET statements below to meet



   //* site standards.



   //*



   //* Verify if the SMPCPATH and SMPJHOME DD below points to the



   //* correct PATH to meet site standards.



   //*



   //* WARNING!



   //* This JCL must be in mixed case and sequence numbers are not allowed



   //*



   // EXPORT SYMLIST=*



   // SET HLQ='DT'             <== HLQ of the target PDS datasets



   // SET REL='R12770'         <== Release number



   // SET VOLSER='NSM001'      <== Volume of the target PDS datasets



   // SET MYUSS='/u/dt'        <== USS work directory



   //*



   //*



   //STEP1   EXEC PGM=IKJEFT01,DYNAMNBR=10



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH rm -Rf &MYUSS/GIMZIP



   BPXBATCH SH cd &MYUSS &&  +



   pax -rvf dynatrace-zos.pax GIMZIP



   //*



   //*



   //STEP2    EXEC PGM=GIMUNZIP,PARM='HASH=YES'



   //SMPDIR   DD PATH='&MYUSS/GIMZIP/',PATHDISP=KEEP



   //SMPCPATH DD PATH='/usr/lpp/smp/classes/',PATHDISP=KEEP



   //SMPJHOME DD PATH='/usr/lpp/java/J8.0/',PATHDISP=KEEP



   //SMPOUT   DD SYSOUT=*



   //SYSPRINT DD SYSOUT=*



   //SYSUT3   DD UNIT=SYSALLDA,SPACE=(CYL,(25,5))



   //SYSUT4   DD UNIT=SYSALLDA,SPACE=(CYL,(25,5))



   //SYSIN    DD *,SYMBOLS=EXECSYS



   <GIMUNZIP>



   <ARCHDEF archid="AUTHLIB"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTAUTH">



   </ARCHDEF>



   <ARCHDEF archid="LOAD"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTLOAD">



   </ARCHDEF>



   <ARCHDEF archid="SAMPLE"



   replace="YES"



   volume="&VOLSER"



   newname="&HLQ..&REL..SZDTSAMP">



   </ARCHDEF>



   </GIMUNZIP>



   /*



   //*



   //STEP3   EXEC PGM=IKJEFT01,DYNAMNBR=10



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH export ussdir=&MYUSS &&+



   cp ${ussdir}/GIMZIP/dynatrace-oneagent-zos-java.jar +



   ${ussdir}/dynatrace-oneagent-zos-java.jar



   //*



   //*



   //STEP4   EXEC PGM=IKJEFT01,DYNAMNBR=55



   //SYSPRINT DD SYSOUT=*



   //SYSTSPRT DD SYSOUT=*



   //STDOUT   DD SYSOUT=*



   //STDERR   DD SYSOUT=*



   //SYSIN    DD DUMMY



   //SYSTSIN  DD *,SYMBOLS=EXECSYS



   BPXBATCH SH rm -Rf &MYUSS/GIMZIP



   //
   ```

   If the job ends with a return code of `0`, the extraction was successful.

   Optional Delete `dynatrace-zos.pax` and `dynatrace-oneagent-zos-java.jar` (if it is not needed) to free up disk space.

### Product datasets

The extraction process creates the following product datasets (the names are provided for the default high-level qualifier and the `R1nnnx` release version):

* `DT.R1nnnx.SZDTAUTH`: Contains the zDC subsystem and the IMS module including IMS Connect
* `DT.R1nnnx.SZDTLOAD`: Contains the CICS module
* `DT.R1nnnx.SZDTSAMP`: Includes sample JCL and CICS RDO definitions

Disk space usage of the product datasets

On an average, the product datasets and installation files in the z/OS USS directory use the following disk space:

```
Dsname                Tracks(3390) %Used



---------------------------------------



DT.R1nnnm.SZDTAUTH      893          5



DT.R1nnnm.SZDTLOAD       61         27



DT.R1nnnm.SZDTSAMP     1221         24
```

```
./GIMZIP/                      8K



./dynatrace-zos-1.nnn.m.pax    5M
```

### Define aliases

We recommend defining an `ALIAS` without the version number for the product datasets. Use these `ALIAS` in the zDC, CICS, and IMS module injection jobs. You can then perform maintenance without updating the jobs.

For example:

```
DEFINE ALIAS(NAME('DT.DYNTRC.SZDTAUTH') RELATE('DT.R12770.SZDTAUTH'))



DEFINE ALIAS(NAME('DT.DYNTRC.SZDTLOAD') RELATE('DT.R12770.SZDTLOAD'))
```