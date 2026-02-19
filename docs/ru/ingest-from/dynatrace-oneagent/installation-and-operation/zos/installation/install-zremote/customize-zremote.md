---
title: Customize the zRemote module
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos/installation/install-zremote/customize-zremote
scraped: 2026-02-19T21:20:47.503437
---

# Customize the zRemote module

# Customize the zRemote module

* Latest Dynatrace
* 9-min read
* Updated on Aug 11, 2022

You can customize the zRemote module to enable optional features and optimize its performance.

## User configuration files

The following configuration files are retained in the event of a zRemote update or uninstallation. You can make changes here.

You must restart the zRemote service to apply new settings.

### zRemote module user configuration

The zRemote module user configuration file (`zremoteagentuserconfig.conf`) allows you to override the default configuration defined in `ruxitagent.conf`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/zremoteagentuserconfig.conf`

### Watchdog user configuration

Dynatrace version 1.277+ The watchdog user configuration file (`watchdoguserconfig.conf`) allows you to override the default configuration defined in `oneagentzwatchdog.ini`.

Linux

Windows

`/var/lib/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

`C:/ProgramData/dynatrace/zremote/agent/conf/watchdoguserconfig.conf`

Available parameters for configuration:

Parameter

Unit

Default value

Description

-healthcheck.heartbeat.timeout

Seconds

900

The connection timeout between the zRemote service and your Dynatrace environment

-healthcheck.memory.limit\_absolute

MiB

500

Absolute input for the memory calculation limit of the child process

-healthcheck.memory.limit\_percentage

%

20

Percentage input for the memory calculation limit of the child process

Effective memory limit calculation

Effective limit = percentage limit Ã available physical memory on the system + absolute limit

For example:

0.2 Ã 5 GiB + 500 MiB = 1.5 GiB effective memory limit

## Organize LPARs with host groups

Host groups are helpful when you want to organize multiple LPARs connecting to a single zRemote module. An LPAR can be assigned to a host group by setting the `[HostGroup]` attribute in the `zremoteagentuserconfig.conf` file. An LPAR can belong to only one host group.

To assign an LPAR to a host group, specify the group name in between a pair of `[HostGroup]` attributes. The `[HostGroup]` attribute pair can occur anywhere in the `zremoteagentuserconfig.conf` file.

```
[HostGroup]



<LPAR_Name1>=<HostGroupName>



<LPAR_Name2>=<HostGroupName>



[HostGroup]
```

The LPAR name is the 8 characters logical partition name defined in the `LPARNAME()` parameter in `IEASYMxx` member in z/OS.

The LPAR name is also displayed in the `Properties and tags` section on the host screen.

The following requirements apply to the `<HostGroupName>` string:

* Can contain only alphanumeric characters, hyphens (`-`), underscores (`_`), and dots (`.`)
* Must not start with `dt.`
* Maximum length is 100 characters

Combining three LPARs to a single host group

In this example, we add three LPARsâ`LPARA`, `LPARB`, and `LPARC` to a single host group `TEST_HOST`.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=TEST_HOST



LPARC=TEST_HOST



[HostGroup]
```

Assigning three LPARs to different host groups

In this example we assign each LPAR to a separate host group.

```
[HostGroup]



LPARA=TEST_HOST



LPARB=PROD_HOST



LPARC=PERF_HOST



[HostGroup]
```

* In host settings, only the **General**, **Monitoring**, and **Detected processes** menus are applicable for a z/OS host group.
* Store your host group settings only in the `zremoteagentuserconfig.conf` file and migrate your host group settings from the `ruxitagent.conf` file.
* Host group settings take effect during zRemote start up. You must restart the zRemote module after defining host group in the `zremoteagentuserconfig.conf` file.

## Fetch full SQL statements from Db2 databases

Dynatrace can provide insight into SQL statements based on tracing of Db2 and DL/I database calls. These SQL statements are shown in Dynatrace, for example, as:

* **FETCH (PROGNAME;165;3)**
* **CLOSE (PROGNAME;441;2)**

The string represents the program name (DBRM name), the line number, and the section number.

Example for captured SQL statements

![zRemote SQL statement fetch off](https://dt-cdn.net/images/zremote-sql-fetch-off-1600-5beae13988.png)

zRemote module version 1.241+ Dynatrace can provide deeper insight into Db2 database calls by fetching the full SQL statements from the Db2 catalog. With the **SQL statement fetch** feature enabled, the SQL statements are shown in Dynatrace, for example, as:

* **FETCH (GETTAB INTO : H , : H , : H , : H , : H)**
* **CLOSE (GETTAB)**

Example for captured SQL statements with enabled SQL statement fetch feature

![zRemote SQL statement fetch on](https://dt-cdn.net/images/zremote-sql-fetch-on-1602-ff3d0f1c32.png)

### Enable SQL statement fetch

The **SQL statement fetch** feature is disabled by default. To enable it

1. Install and configure the IBM Data Server Driver for ODBC and CLI software on [Linuxï»¿](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-linux-unix-operating-systems) or [Windowsï»¿](https://www.ibm.com/docs/en/db2/11.5?topic=dsd-installing-data-server-driver-odbc-cli-software-windows-operating-systems). Further reading: [IBM Db2 ODBC CLI driver Download and Installation informationï»¿](https://www.ibm.com/support/pages/db2-odbc-cli-driver-download-and-installation-information).

   In the installation step take note of the location of the CLI driver library:

   * `libdb2.so` for Linux
   * `db2app64.dll` for Windows

   Before configuring the driver, it might be necessary to contact the DBA requesting the database connectivity information (such as database credentials, location, and IP and port). In the configuration step, take note of the Db2 aliases (or DSN).

   Both are required in the next steps.

   * The zRemote module supports only 64-bit CLI driver.
   * We strongly recommend that you set the connection timeout for every DB alias, for example, ConnectTimeout=2
     for two seconds in db2cli.ini on Linux
   * Be sure to test the CLI driver configuration to ensure good Db2 connections, for example:

     ```
     \<cli-driver-path\>/bin/db2cli validate -connect -database \<db-location\>:\<ip\>:\<port\> -user \<id\> -passwd \<pw\>



     \<cli-driver-path\>/bin/db2cli validate -connect -dsn \<db-alias\>
     ```
   * To configure the CLI driver, you need Db2 credentials that grant access to Db2 connections (from distributed using DDF/DRDA) and grants to select on CATALOG, specifically on SYSPACKSTMT.
2. In the `zremoteagentuserconfig.conf` file of the zRemote module, define the CLI driver library and Db2 alias group (similar as defining host groups), for example:

   ```
   # Linux



   cli_driver_lib=/opt/IBM/CLIDRIVER/lib/libdb2.so



   # ... or Windows



   cli_driver_lib=C:/IBM/CLIDRIVER/bin/db2app64.dll



   [DbAlias]



   dbHost1.dbName1=alias1



   dbHost2.dbName2=alias2



   dbHostN.dbNameN=aliasN



   [DbAlias]



   # Beginning with zRemote 1.279 it is possible to set the new flag sqlStmtExtended, if



   # true the full (fetched) SQL statement is appended with its old (unfetched) format,



   # for example, from an example above "FETCH (GETTAB INTO : H , : H , : H , : H , : H)"



   # would be shown as "FETCH (GETTAB INTO : H , : H , : H , : H , : H) (PROGNAME;165;3)".



   # The default is false. Note: if enabled this setting would affect the aggregation count.



   sqlStmtExtended=false
   ```

   where `dbHost` is the z/OS SMF ID and `dbName` is the Db2 subsystem name. All is case sensitive.
3. Optional Define `sqlStmtCacheFileName=/tmp/sqlStmtCacheFileName`, as an example, to cache the fetched SQL statements to a file and use it upon a zRemote module restart, thus reducing Db2 interactions. Be sure to use the appropriate fully qualified file name.
4. Restart the zRemote module.

   * The zRemote module will only enable the **SQL statement fetch** feature if the CLI driver can be loaded successfully and there is at least one DB2 alias defined.
   * If the Db2 alias is later found to be invalid, the feature is disabled.

## Enable secure zLocal-zRemote connection

zRemote module version 1.267+

By default, the zLocal and zRemote use a proprietary communication protocol via plain sockets. You can configure them to communicate via TLS by configuring AT-TLS for the zLocal and setting the SSL flags for the zRemote as shown below.

### AT-TLS configuration for the zLocal

Depending on your requirements, there are different ways to configure AT-TLS for zLocal. For more details, refer to [Application Transparent Transport Layer Security data protectionï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=applications-application-transparent-transport-layer-security-data-protection) in IBM documentation. You can use the example AT-TLS configuration below as a template.

Example of an AT-TLS configuration

```
TTLSRule                       <client-rule>



{



RemoteAddr                 <ALL | specific-ip-addr>



RemotePortRange            <zdclistenerport>



Direction                  Outbound



TTLSGroupActionRef         <group-action>



TTLSEnvironmentActionRef   <environment-action>



TTLSConnectionActionRef    <connection-action>



}



TTLSGroupAction                <group-action>



{



TTLSEnabled                On



Trace                       <trace-level>



}



TTLSEnvironmentAction          <environment-action>



{



HandshakeRole              Client



TTLSKeyringParmsRef        <keyring-parms>



TTLSCipherParmsRef         <cipher-parms>



}



TTLSKeyringParms               <keyring-parms>



{



#   A certificate matches that of the zRemote's certificate





#   must be loaded into RACF and connected to the Keyring here.



Keyring                    <pub-key-or-certificate>



}



TTLSCipherParms                <cipher-parms>



{



...



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256



V3CipherSuites             TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384



...



}



TTLSConnectionAction           <connection-action>



{



TTLSConnectionAdvancedParmsRef  <connection-advanced-parms>



}



TTLSConnectionAdvancedParms    <connection-advanced-parms>



{



SSLv2                      Off



SSLv3                      Off



TLSv1                      Off



TLSv1.1                    Off



TLSv1.2                    On



TLSv1.3                    On



}
```

Be sure the userId used in the zDC job is the same one that owns the certificate.
Otherwise, the connection to the TSL handshake will fail (with SSL accept error -1 and code 5).

### SSL/TLS settings for the zRemote

To enable SSL/TLS for the zRemote

1. Open the `zremoteagentuserconfig.conf` file.
2. Set `sslEnabled` to `true`.
3. Specify the absolute paths to your private key (`sslPrivateKey`) and certificate (`sslCertificate`) PEM files.
4. Optional Define specific TLS cipher suites. For information about allowed cipher suite names and their string format, refer to [OpenSSL documentationï»¿](https://www.openssl.org/docs/man1.1.1/man1/ciphers.html).

Show configuration template

```
# Must be true to enable secure connection; all other SSL settings are ignored if false



sslEnabled=true



# Absolute paths to your private key (with the pass-phrase stripped) and certificate PEM files.



# Beginning with zRemote module version 1.301.0, multiple private-key/certificate pairs delimited



# by a semicolon can be specified. For example:



# sslPrivateKey=<private-key-1.pem; private-key-2.pem; ...; private-key-n.pem>



# sslCertificate=<certificate-1.pem; certificate-2.pem; ...; certificate-n.pem>



sslPrivateKey=<private-key.pem>



sslCertificate=<certificate.pem>



# Optional: TLS cipher suites allowed according to OpenSSL



# Example: sslCiphers=ECDHE-RSA-AES128-SHA256:ECDHE-RSA-AES256-SHA384:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384



sslCiphers=<cipher-suites>
```

## Ignore invalid connection attempts

If a specific process regularly pings the zRemote module to detect its availability, and these pings reach the zRemote listener port, the zRemote module logs an invalid connection attempt. These invalid connection attempts increase the zRemote log size over time.

To ignore connection attempts from specific processes, list their IP addresses (separated by semicolons) in the `zremoteagentuserconfig.conf` file, for example:

```
ignoreHandshakeEndpoints=192.168.0.1;10.0.0.2
```

## Opt out of new IMS MPR process ID calculation

zRemote module version 1.253+

The IMS message processing region (MPR) process IDs could change, resulting in new process and service entities in Dynatrace. To prevent this process ID change, weâve introduced a more stable ID calculation with the consequence that all IMS MPR process and service entities will change once but then remain stable after an update of the zRemote module with version 1.253.

To opt out of the new IMS MPR process ID calculation, set the flag `useOldImsPgiCalc` in the `zremoteagentuserconfig.conf` file to `true`.

```
useOldImsPgiCalc=true
```