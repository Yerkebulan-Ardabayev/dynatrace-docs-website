---
title: Snowflake Database monitoring configuration
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/data-sources/sql/snowflake-monitoring
scraped: 2026-02-16T21:32:19.308650
---

# Snowflake Database monitoring configuration

# Snowflake Database monitoring configuration

* Latest Dynatrace
* Reference
* 2-min read
* Published Apr 19, 2023

After you define the scope of your configuration, you need to identify the following:

* Databases from which to collect data
* ActiveGates to execute the extension and connect to your devices

## Example payload

Example payload to activate the Snowflake Database extension:

```
[



{



"value": {



"enabled": true,



"description": "My SnowFlake DB extension",



"version": "0.1.1",



"featureSets": [



"io",



"cpu",



],



"sqlSnowflakeRemote": {



"endpoints": [



{



"host": "sqlserver.org",



"port": 1521,



"databaseName":"SNOWFLAKE_SAMPLE_DATA",



"warehouse":"yourwarehouse",



"schema":"yourschema",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}



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

Human-readable description of the specifics of this monitoring configuration.

### Version

Version of this monitoring configuration. Note that a single extension can run multiple monitoring configurations.

### Feature sets

Add a list of feature sets you want to monitor. To report all feature sets, add `all`.

```
"featureSets": [



"cpu",



"io"



]
```

### Endpoints

You can define up to 20,000 endpoints in a single monitoring configuration in the `SQLSnowflakeRemote` section.

```
"sqlSnowflakeRemote": {



"endpoints": [



{



"host": "your-snowflake.com",



"port": 1521,



"databaseName":"SNOWFLAKE_SAMPLE_DATA",



"warehouse":"yourwarehouse",



"schema":"yourschema",



"authentication": {



"scheme": "basic",



"username": "admin",



"password": "password"



}



}



]



}
```

To define the Snowflake Database server, add the following details in the `endpoints` section:

* Host
* Port
* Database name
* Warehouse
* Schema
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

### Scope

Note that each ActiveGate host running your extension needs the root certificate to verify the authenticity of your extension. For more information, see [Sign extension](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension for secure distribution in your environment using the Dynatrace Extensions framework.").

The scope is an ActiveGate group that will execute the extension. Only one ActiveGate from the group will run this monitoring configuration. If you plan to use a single ActiveGate, assign it to a dedicated group. You can assign an ActiveGate to a group during or after installation. For more information, see [ActiveGate group](/docs/ingest-from/dynatrace-activegate/activegate-group "Understand the basic concepts of ActiveGate groups.").

Use the following format when defining the ActiveGate group:

```
"scope": "ag_group-<ActiveGate-group-name>",
```

Replace `<ActiveGate-group-name>` with the actual name.