---
title: Microsoft SQL Server monitoring configuration
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/sql/microsoft-sql-monitoring
scraped: 2026-05-12T12:08:26.392671
---

# Microsoft SQL Server monitoring configuration

# Microsoft SQL Server monitoring configuration

* Reference
* 3-min read
* Updated on Apr 09, 2026

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data
* ActiveGates to execute the extension and connect to your devices

## Example payload

Example payload to activate a Microsoft SQL extension:

```
{



"value": {



"enabled": true,



"description": "My Microsoft SQL extension",



"version": "1.0.1",



"sqlServerRemote": {



"endpoints": [



{



"host": "localhost",



"port": 1521,



"instanceName": "some-instanceName",



"databaseName": "some-databaseName",



"authentication": {



"scheme": "basic",



"username": "username",



"password": "password"



},



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}
```

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

A human-readable description of the specifics of this monitoring configuration.

### Version

The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlServerRemote` section.

```
"sqlServerRemote": {



"endpoints": [



{



"host": "sqlserver.org",



"port": 1433,



"instanceName": "instance",



"databaseName": "database",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}



}



]



}
```

To define a Microsoft SQL Server, add the following details in the `endpoints` section:

* Host
* Port
* Instance name
* Database name
* Authentication credentials

### Authentication

Authentication details passed to the Dynatrace API when activating a monitoring configuration are obfuscated and it's impossible to retrieve them.

#### Basic

Basic authentication requires only a username and password.

```
"authentication": {



"scheme": "basic",



"username": "username",



"password": "password",



}
```

#### Kerberos

Requires Active Directory domain set up. Allows you to connect to a database by providing a domain username, password, Key Distribution Center (KDC), and realm.

```
"authentication": {



"scheme": "kerberos",



"username": "username",



"password": "password",



"realm": "realm",



"kdc": "kdc"



}
```

#### NTLM

Windows only

Requires Active Directory domain set up. Allows you to connect to a database by providing a domain username, a domain password, and, optionally, the domain.

```
"authentication": {



"scheme": "ntlm",



"username": "username",



"password": "password",



"domain": "some-domain-name"



}
```

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

ActiveGate version 1.251+

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

Client certificates are not supported for SQL data sources. To authenticate securely, use basic authentication with SSL enabled. For details, see [Authentication](#authentication).

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/managed/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.