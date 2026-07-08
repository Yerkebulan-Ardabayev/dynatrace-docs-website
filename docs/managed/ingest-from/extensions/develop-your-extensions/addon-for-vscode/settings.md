---
title: Settings
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings
---

# Settings

# Settings

* Reference
* 4-min read
* Updated on Mar 23, 2026

You can define all settings either globally or for each workspace.

You can learn more about accessing these settings in Visual Studio Code's [official documentation﻿](https://code.visualstudio.com/docs/getstarted/settings).

## Credentials

**Dynatrace Extensions** can either generate all the credentials required for Extension 2.0 development or allow you to bring your own credential files.

### When using your credentials

You need to provide your files by using these settings:

| Setting | Description |
| --- | --- |
| `dynatraceExtensions.developerCertkeyLocation` | This is the path to your [developer credential](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions#cert "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.") file. |
| `dynatraceExtensions.rootOrCaCertificateLocation` | is the path to your root (CA) certificate. |

Example usage:

```
{



"dynatraceExtensions.developerCertkeyLocation": "C:\\Temp\\certificates\\dev.pem",



"dynatraceExtensions.rootOrCaCertificateLocation": "C:\\Temp\\certificates\\ca.pem"



}
```

### When generating credentials

You can customize the details that are embedded into the generated certificates by using these settings:

| Setting | Default value | Description |
| --- | --- | --- |
| `dynatraceExtensions.certificateCommonName` | Extension Developer | The certificate's common name (CN) attribute. |
| `dynatraceExtensions.certificateOrganization` |  | The certificate's organization (O) attribute. |
| `dynatraceExtensions.certificateOrganizationUnit` |  | The certificate's organization unit (OU) attribute. |
| `dynatraceExtensions.certificateStateOrProvince` |  | The certificate's state or province (ST) attribute. |
| `dynatraceExtensions.certificateCountryCode` |  | The certificate's country code (C) attribute. |

## Behavior

The add-on aims to allow users to customize their extension development experience as much as possible. The following settings allow turning various features on or off on demand.

### Features

| Setting | Default value | Description |
| --- | --- | --- |
| `dynatraceExtensions.metricSelectorsCodeLens` | true | [Metric selector code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#metric-selectors "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.entitySelectorsCodeLens` | true | [Entity selector code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#entity-selectors "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.fastDevelopmentMode` | false | [Fast development mode](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#fast-development-mode "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.wmiCodeLens` | true | [WMI queries code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#windows-management-interface-wmi-queries "Overview of all Dynatrace Extensions features to help you develop apps") |
| `dynatraceExtensions.screenCodeLens` | true | [Unified analysis screen code lens](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#unified-analysis-screens "Overview of all Dynatrace Extensions features to help you develop apps") |

### Logging

| Setting | Default value | Description |
| --- | --- | --- |
| `dynatraceExtensions.logging.level` | `INFO` | The minimum level of log messages |
| `dynatraceExtensions.logging.maxFiles` | 10 | The maximum number of log files (by age) kept on disk. |
| `dynatraceExtensions.logging.maxFileSize` | 10 | The maximum size of a single log file (in MB). |

### Tenant Connectivity Settings

The add-on always performs web requests to your Dynatrace environment over HTTPS. In specific scenarios—for example, in Dynatrace Managed—your environment may be accessible through a dedicated endpoint that uses either a custom-signed or a self-signed SSL certificate. While valid for encryption, most frameworks and browsers don't recognize these certificates as trusted, which causes requests to fail.

The `dynatraceExtensions.tenantConnectivitySettings` setting is only available from your `settings.json` file and represents an array of environment endpoints that require special settings for HTTPS connectivity. Each entry in the array is an object with the following details:

| Attribute | Default value | Description |
| --- | --- | --- |
| `tenantUrl` | "" | The base URL to your Dynatrace environment. The add-on will use the URL to decide when to apply special connectivity settings on web requests. |
| `certificatePath` | "" | The path on disk to a Root/CA file in `.pem` or `.crt` format. The add-on will load this file and add it to the list of trusted CAs for the given `tenantUrl`. |
| `disableSSLVerification` | `false` | When enabled, the add-on ignores SSL certificates for the given `tenantUrl`. Enable this only when using self-signed certificates on your Dynatrace endpoint. |

Example:

* Adding a custom certificate to the trusted CAs:

  ```
  "dynatraceExtensions.tenantConnectivitySettings": [



  {



  "tenantUrl": "https://10.0.0.1:5555/e/my-tenant",



  "certificatePath": "C:\\Temp\\my_custom.crt"



  }



  ]
  ```
* Using a self-signed certificate on an endpoint:

  ```
  "dynatraceExtensions.tenantConnectivitySettings": [



  {



  "tenantUrl": "https://my.custom.endpoint/e/my-other-tenant",



  "disableSSLVerification": true



  }



  ]
  ```

## Diagnostics

| Setting | Default value | Description |
| --- | --- | --- |
| `dynatraceExtensions.diagnostics.all` | true | All diagnostics |
| `dynatraceExtensions.diagnostics.extensionName` | true | The name of the extension |
| `dynatraceExtensions.diagnostics.metricKeys` | true | Keys used for metric definitions |
| `dynatraceExtensions.diagnostics.cardKeys` | true | Keys of cards referenced/defined in the screens section |
| `dynatraceExtensions.diagnostics.snmp` | true | SNMP data source, especially the use of OIDs |

Learn more about Dynatrace Extensions [custom diagnostics.](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/development-assistance#diagnostics "Overview of all Dynatrace Extensions features to help you develop apps")

## Python environment

The settings in this section allow you to customize the details of your virtual environment when working with Python extensions.

| Setting | Default value | Description |
| --- | --- | --- |
| `dynatraceExtensions.pythonExtraPlatforms` | `[ "linux_x86_64", "win_amd64" ]` | A list of platforms to build Python packages for. |
| `dynatraceExtensions.pythonExtraPlatformsOnly` | false | When enabled, the `Dynatrace extensions: Build` command builds only for the platforms specified above. |
| `dynatraceExtensions.pythonBuildVersion` | `3.10 + 3.14` | Options are `3.10 + 3.14`, `3.10`, or `3.14`. Select `3.10` to roll back for EEC versions earlier than `1.333.x`. |