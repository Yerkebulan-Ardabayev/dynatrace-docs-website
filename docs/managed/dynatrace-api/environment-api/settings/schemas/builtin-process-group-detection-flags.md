---
title: Settings API - Built-in detection rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-process-group-detection-flags
---

# Settings API - Built-in detection rules schema table

# Settings API - Built-in detection rules schema table

* Published Dec 05, 2023

### Built-in detection rules (`builtin:process-group.detection-flags)`

Enable or disable process group detection flags

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:process-group.detection-flags` | * `group:processes-and-containers.processes` * `group:processes-and-containers` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.detection-flags` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:process-group.detection-flags` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:process-group.detection-flags` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ignore versions, builds, dates, and GUIDs in process directory names `ignoreUniqueIdentifiers` | boolean | To determine the unique identity of each detected process, and to generate a unique name for each detected process, Dynatrace evaluates the name of the directory that each process binary is contained within. For application containers like Tomcat and JBoss, Dynatrace evaluates important directories like CATALINA\_HOME and JBOSS\_HOME for this information. In some automated deployment scenarios such directory names are updated automatically with new version numbers, build numbers, dates, or GUIDs. Enable this setting to ensure that automated directory name changes don't result in Dynatrace registering pre-existing processes as new processes. | Required |
| Use CATALINA\_BASE to identify Tomcat cluster nodes `useCatalinaBase` | boolean | By default, Tomcat clusters are identified and named based on the CATALINA\_HOME directory name. This setting results in the use of the CATALINA\_BASE directory name to identify multiple Tomcat nodes within each Tomcat cluster. If this setting is not enabled, each CATALINA\_HOME+CATALINA\_BASE combination will be considered a separate Tomcat cluster. In other words, Tomcat clusters can't have multiple nodes on a single host. | Required |
| Use Docker container name to distinguish multiple containers `useDockerContainerName` | boolean | **For Docker outside container platforms only.** By default, Dynatrace uses image names as identifiers for individual process groups, with one process-group instance per host. Normally Docker container names can't serve as stable identifiers of process group instances because they are variable and auto-generated. You can however manually assign proper container names to their Docker instances. Such manually-assigned container names can serve as reliable process-group instance identifiers. This flag instructs Dynatrace to use Docker-provided names to distinguish between multiple instances of the same image. If this flag is not applied and you run multiple containers of the same image on the same host, the resulting processes will be consolidated into a single process view. **Use this flag with caution!** | Required |
| Automatically detect Cassandra clusters `autoDetectCassandraClusters` | boolean | Enabling this flag will detect separate Cassandra process groups based on the configured Cassandra cluster name. | Required |
| Use Node.js script name to distinguish processes started from same directory in addition to application id. `addNodeJsScriptName` | boolean | In older versions, Node.js applications were distinguished based on their directory name, omitting the script name. Changing this setting may change the general handling of Node.js process groups. Leave unchanged if in doubt. | Required |
| Automatically detect TIBCO BusinessWorks engines `autoDetectTibcoEngines` | boolean | Enabling this flag will detect separate TIBCO BusinessWorks process groups per engine property file. | Required |
| Identify and name JBoss servers based on system property jboss.server.name `identifyJbossServerBySystemProperty` | boolean | Enabling this flag will detect the JBoss server name from the system property jboss.server.name=, only if -D[Server:] is not set. | Required |
| Automatically detect webMethods Integration Server `autoDetectWebMethodsIntegrationServer` | boolean | Enabling this flag will detect webMethods Integration Server including specific properties like install root and product name. | Required |
| Automatically detect Spring Boot applications `autoDetectSpringBoot` | boolean | Enabling this flag will detect Spring Boot process groups based on command line and applications' configuration files. | Required |
| Automatically detect TIBCO BusinessWorks Container Edition engines `autoDetectTibcoContainerEditionEngines` | boolean | Enabling this flag will detect separate TIBCO BusinessWorks process groups per engine property file. | Required |
| Group Oracle database processes by SID `splitOracleDatabasePG` | boolean | Enable to group and separately analyze the processes of each Oracle DB. Each process group receives a unique name based on the Oracle DB SID. | Required |
| Group Oracle listener processes by name `splitOracleListenerPG` | boolean | Enable to group and separately analyze the processes of each Oracle Listener. Each process group receives a unique name based on the Oracle Listener name. On Windows, this option supports listeners launched manually or running on a Windows virtual account. | Required |
| Automatically detect WebSphere Liberty application `autoDetectWebSphereLibertyApplication` | boolean | Enabling this flag will detect separate WebSphere Liberty process groups based on java command line. | Required |
| Monitor short lived processes `shortLivedProcessesMonitoring` | boolean | Enable to monitor CPU and memory usage of short lived processes, otherwise being lost by traditional monitoring. | Required |
| Group IBM MQ processes by queue manager name `groupIBMMQbyInstanceName` | boolean | Enable to group and separately analyze the processes of each IBM MQ Queue manager instance. Each process group receives a unique name based on the queue manager instance name. | Required |
| Automatically detect security software `securitySoftwareDetectionEnabled` | boolean | This flag enables the detection of security software, such as anti-malware protection. The currently detected utilities are Carbon Black EDR (on Windows only), CrowdStrike Falcon XDR and Trellix Endpoint Security (former McAfee). | Required |
| Group DB2 database processes by DB2 Instances `splitDb2GroupingByInstances` | boolean | Enable to group and separately analyze the processes of each DB2 Instance. Each process receives a unique name based on the DB2 Instance name. | Required |