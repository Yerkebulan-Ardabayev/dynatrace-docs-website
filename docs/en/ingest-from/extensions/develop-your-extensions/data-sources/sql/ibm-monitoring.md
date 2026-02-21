---
title: IBM Database monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/ibm-monitoring
scraped: 2026-02-21T21:18:49.170584
---

# IBM Database monitoring configuration

# IBM Database monitoring configuration

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 19, 2023

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data
* ActiveGates to execute the extension and connect to your devices

## Example payload

Example payload to activate an IBM DB2 extension:

```
[



{



"value": {



"enabled": true,



"description": "My IBM extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlDb2Remote": {



"endpoints": [



{



"host": "db2host",



"port": 1521,



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



},



"databaseName": "dbname",



"ssl": false



}



]



}



},



"scope": "ag_group-default"



}



]
```

## Parameters

### Enabled

If set to `true`, the configuration is active and Dynatrace starts monitoring immediately.

### Description

A human-readable description of the specifics of this monitoring configuration.

### Version

The version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `sqlDb2Remote` section.

```
"sqlDb2Remote": {



"endpoints": [



{



"host": "db2host",



"port": 1433,



"authentication": {



"scheme": "basic",



"username": "user",



"password": "password"



},



"databaseName": "dbname",



}



]



}
```

To define an IBM Database server, add the following details in the `endpoints` section:

* Host
* Port
* Authentication credentials
* Database name

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

ActiveGate version 1.269+

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