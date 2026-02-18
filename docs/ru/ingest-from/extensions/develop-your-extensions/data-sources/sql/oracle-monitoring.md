---
title: Oracle Database monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/oracle-monitoring
scraped: 2026-02-18T21:32:31.017453
---

# Oracle Database monitoring configuration

# Oracle Database monitoring configuration

* Latest Dynatrace
* Reference
* 5-min read
* Published Apr 11, 2022

After you define the scope of your configuration, you need to identify the databases you'd like to collect data from and identify the ActiveGates that will execute the extension and connect to your devices.

Make sure that all the ActiveGates from the ActiveGate group you'll define as the scope can connect to a respective data source. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

The monitoring configuration is a JSON payload defining the connection details, credentials, and feature sets that you want to monitor. For details, see [Start monitoring](/docs/ingest-from/extensions/manage-extensions#start-monitoring "Learn how to manage extensions.").

Example payload to activate an Oracle SQL extension:

```
[



{



"value": {



"enabled": true,



"description": "My Oracle SQL extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlOracleRemote": {



"licenseAccepted": true,



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseIdentifier": "serviceName",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"serviceName": "some-serviceName"



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

When you have your initial extension YAML ready, package it, sign it, and upload it to your Dynatrace environment. For details, see [Manage extension lifecyle](/docs/ingest-from/extensions/manage-extensions "Learn how to manage extensions.").

The Dynatrace Hub-based extension activation wizard contains a dynamically updated JSON payload with your monitoring configuration

You can also use the Dynatrace API to download the schema for your extension that will help you create the JSON payload for your monitoring configuration.

Use the [GET an extension schema](/docs/dynatrace-api/environment-api/extensions-20/extensions/get-schema "View the schema of an extension the Dynatrace Extensions 2.0 API.") endpoint.

Issue the following request:

```
curl -X GET "{env-id}.live.dynatrace.com/api/v2/extensions/{extension-name}/{extension-version}/schema" \



-H "accept: application/json; charset=utf-8" \



-H "Authorization: Api-Token {api-token}"
```

Make sure to replace `{extension-name}` and `{extension-version}` with values from your extension YAML file. A successful call returns the JSON schema.

## Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.

## Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

## Description

Human-readable description of the specifics of this monitoring configuration.

## Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

## Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `SQLOracleRemote` section.

```
"sqlOracleRemote": {



"licenseAccepted": true,



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseIdentifier": "serviceName",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"serviceName": "some-serviceName"



"ssl": false



}



]



}



}
```

### Oracle JDBC Driver

The Oracle SQL data source requires the Oracle JDBC driver distributed by Dynatrace. By setting the `licenceAccepted` property to `true`, you indicate that you have read and accepted the [Dynatrace redistribution license agreement for Oracle JDBC Driverï»¿](https://dt-url.net/0s1n0pw9).

To define an Oracle Database server, add the following details in the `endpoints` section:

* Host
* Port
* Database identifier, either `serviceName` or `sid`.
* Authentication credentials

The Oracle JDBC driver version shipped with the Extension Framework is `ojdbc11`.

## Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

### Credential vault

The credential vault authentication type provides a more secure approach to using extensions by securely storing and managing user credentials. To use this, you must be the owner of the credentials and have a credential vault that meets the following criteria:

* **Credential type**âUser and password
* **Credential scope**âSynthetic (in case of external vault usage) and Extension authentication scopes enabled
* **Owner access only** is enabled only for credential owners

```
"authentication": {



"scheme": "basic",



"useCredentialVault": true,



"credentialVaultId": "some-credential-vault-id"



}
```

## Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### TopN

The feature set `topN` enables monitoring of the most resource-intensive queries. Enabled by default.

```
"featureSets": [



"topN"



]
```

This groups topN queries by an entity. The queries are displayed on the event page and on a unified analysis page for the Oracle server entity.

### Multitenancy

The feature set `multitenancy` enhances the monitoring capabilities by querying and retrieving information about Container Databases (CDBs), Pluggable Databases (PDBs), and the services associated with the specified database in the monitoring configuration.

```
"featureSets": [



"multitenancy"



]
```

Example navigation

To navigate through the structure of Oracle entities

1. Go to ![Dashboards Classic](https://dt-cdn.net/images/dashboards-classic-512-15764940e8.png "Dashboards Classic") **Dashboards Classic** and open the **Oracle Database Overview** dashboard.
2. In the **Hosts** section of the dashboard, select the host from the **Oracle DB host** column.
3. On the **Oracle DB server** page, select a CDB.

   ![Oracle Database multitenancy: CDBs](https://dt-cdn.net/images/cbds-1640-8c7671e235.png)
4. On the **CDB** page, select a pluggable database.

   ![Oracle Database multitenancy: Pluggable databases](https://dt-cdn.net/images/pluggable-databases-1611-2ce2521bef.png)
5. The **PDB** page lists services.

   ![Oracle Database multitenancy: Services](https://dt-cdn.net/images/services-1621-d3ca42e060.png)

## Heavy query timeout

ActiveGate version 1.275+

Add the `long-running-query-timeout` parameter to configure the timeout duration for long-running SQL queries. This parameter is optional, and if not set, the default timeout of 10 seconds is applied.

```
"vars": {



"long-running-query-timeout": null



}
```

## SSL

ActiveGate version 1.251+

Enable SSL to force the data source to verify the server certificate and use SSL encryption instead of native encryption.

```
"ssl": true
```

#### Enable SSL without a local truststore

When SSL is enabled and the server's certificate chain is publicly verifiable (for example, issued by Azure or other well-known CAs), there's no need to manually create a truststore. The system will automatically trust the server's certificate based on the trusted CAs in the environment.

However, if you need to use a local truststore for certificates not globally recognized or for additional security measures

1. In the `userdata` directory on the ActiveGates running the SQL data source, manually create a PKCS12 truststore with the name `sqlds_truststore` and password `sqlds_truststore`.

   Command to create a truststore with keytool:

   ```
   keytool -genkey -keystore sqlds_truststore -storepass sqlds_truststore -keyalg DSA
   ```

   Location of `userdata` directory:

   * Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\userdata`
   * Unix: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata`
2. Add the server's certificate to it.

   Command to import a certificate with keytool:

   ```
   keytool -import -keystore sqlds_truststore -file .\ora.crt -alias oracle
   ```

#### Validate SSL certificates

ActiveGate version 1.269+

The certificate is additionally validated with hostname, which means that the domain from the certificate must match the one from the endpoint passed in the monitoring configuration.

Enable this option when connecting to databases using custom certificates.

```
"validateCertificates": true
```

## Resource consumption



Resource consumption depends on the number of Oracle endpoints. The first endpoint consumes 110 MB of RAM and 0.1%â0.5% of CPU. Every following endpoint consumes 0.5â1.0 MB of RAM and ~0.01% of CPU.

Endpoints

Average CPU

Max CPU

RAM (MB)

Host (EC2 instance type)

100

0.6%

0.6% (spike at beginning)

160

XS (`c5.large`)

1

0.1%

0.5% (spike at beginning)

110

XS (`c5.large`)