---
title: JDBC monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/jdbc-monitoring
scraped: 2026-02-17T05:11:10.224490
---

# JDBC monitoring configuration

# JDBC monitoring configuration

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Sep 19, 2024

Dynatrace Extensions SQL data source enables you to query any database allowing connections using the JDBC driver on top of all the database vendors supported by default. For such databases, some additional steps are required.

## Prerequisites

JDBC 4.0+ based drivers are supported.

## Upload JDBC driver to ActiveGate

You need to provide the driver of your selected database vendor so that the ActiveGate running the extension can connect to the database.

MariaDB example

For MariaDB, you can get the driver from the [Download MariaDBï»¿](https://mariadb.com/downloads/connectors/connectors-data-access/java8-connector) page.

Download the Java 8+, platform independent connector, that is the `mariadb-java-client-3.5.0.jar`file.

Upload the JDBC driver to an ActiveGate belonging to the group designated to run your extension:

**Windows**: `C:\ProgramData\dynatrace\remotepluginmodule\agent\conf\userdata\libs`  
**Linux**: `/var/lib/dynatrace/remotepluginmodule/agent/conf/userdata/libs/`

Make sure the `dtuserag` user has read access to driver. For example, for Linux, set `CHMOD` to `775`.

## Monitoring configuration

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data and their authentication details
* ActiveGates to execute the extension and connect to your devices. Such ActiveGates need a related [JDBC driver uploaded](#upload).

Example payload to activate the JDBC extension:

```
[



{



"value": {



"enabled": true,



"description": "My JDBC extension",



"version": "0.0.1",



"featureSets": [



"statements"



],



"jdbcRemote": {



"endpoints": [



{



"host": "193.36.194.170",



"port": 3306,



"connectionString": "jdbc:mariadb://193.36.194.170/mysql",



"authentication": {



"scheme": "basic",



"useCredentialVault": false,



"username": "user",



"password": "password"



}



}



]



}



},



"scope": "ag_group-someAgGroup"



}



]
```

Please note, that you need to provide both, the endpoint (host and port) and the related connection string.

Security controls

The SQL connection string syntax by its nature may expose sensitive information such as user credentials. If possible, avoid including any secret information in the connection string. If your connection string contains any sensitive information:

* Limit the read and write access to JDBC monitoring configuration. Make sure that only users allowed to the secret have a read and write access to the configurations.
* Unlike the authentication details, the connection string is not hashed. View and edit the configuration only in safe environment where non-authorized users cannot see it.

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

Configuration label that should provide basic insights into of the specifics of this monitoring configuration.

### Version

Version of this monitoring configuration.

### Feature sets

Add a list of feature sets you want to monitor.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `jdbcRemote` section.

```
"jdbcRemote": {



"endpoints": [



{



"host": "jdbchost",



"port": 3306,



"connectionString": "jdbc:mariadb://193.36.194.170/mysql",



"authentication": {



"scheme": "basic",



"useCredentialVault": false,



"username": "admin",



"password": "password"



}



}



]



}
```

To define the JDBS Database server, add the following details in the `endpoints` section:

* Host
* Port
* Connection string
* Authentication credentials

### Authentication

Authentication details passed to the Dynatrace API when activating monitoring configuration are obfuscated and it's impossible to retrieve them.

#### Credential vault

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

### SSL

ActiveGate version 1.295+

Enable SSL to make the data source verify the server certificate and use SSL encryption instead of native encryption.

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

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.