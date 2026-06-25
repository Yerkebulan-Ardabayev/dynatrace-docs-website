---
title: Sign extensions
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/sign-extensions
scraped: 2026-05-12T12:02:17.580563
---

# Sign extensions

# Sign extensions

* How-to guide
* 2-min read
* Updated on Apr 27, 2026

Before uploading an extension to your Dynatrace environment, sign it to verify its authenticity. After signing, save the root certificate to a dedicated directory on each host running the extension, whether OneAgent or ActiveGate.

* In a development environment, each developer should have a unique leaf certificate. This ensures the traceability of changes.
* In a production environment, each extension must be signed with its own leaf certificate. This guarantees the authenticity of each extension.

## Sign your extension

Depending on your needs, choose one of the following methods to sign and build your extension:

* [`dt-extensions-sdk`ï»¿](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/cli/sign.html) - an all-in-one CLI tool Recommended
* [VSCode Extension](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Introduction to the Dynatrace Extensions add-on for VS Code") - an all-in-one editor-based tool Recommended
* [Use OpenSSL](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl "Sign an extension manually with OpenSSL.") - a standard crypto library for manual control

Dynatrace CLI

You can also use the Dynatrace CLI (`dt-cli`) to sign your extension. Since its features are fully contained within `dt-extensions-sdk` CLI, only use it as a lighter alternative for CI/CD environments.

Read more about [`dt-cli` on GitHubï»¿](https://github.com/dynatrace-oss/dt-cli).

## Upload your root certificate

Upload your root certificate to enhance the security of the Extensions framework.

By doing this, you

* Verify the authenticity of distributed extensions.
* Prevent potential malicious extension distribution by an intruder who could take control of your environment.

### Add certificate to the credential vault

Add your root certificate to the Dynatrace [credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault."). This is required before you can upload an extension ZIP file to your environment.

When adding the certificate, use the following settings:

* Credential type: `Public certificate`
* Credential scope: `Extension validation`

The [VS Code extension](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Introduction to the Dynatrace Extensions add-on for VS Code") does this automatically. If you work with multiple environments (for example, development and production), you must add the certificate to the credential vault of each environment separately.

For JMX extensions, adding the certificate to the credential vault is the only step required. You don't need to save the certificate to the host filesystem.

### Remote extensions

Upload your root certificate to each ActiveGate host within the ActiveGate group selected for running your extensions.

Save the `root.pem` certificate file in the following location:

* Linux: `/var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/`
* Windows: `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\certificates`

### Local extensions

Upload your root certificate to each OneAgent host or each OneAgent host within the host group selected for running your extensions.

Save the `root.pem` certificate file in the following location:

* Linux: `/var/lib/dynatrace/oneagent/agent/config/certificates`
* Windows: `%PROGRAMDATA%\dynatrace\oneagent\agent\config\certificates`

### Certificate file permissions

For the Extension Execution Controller to read the certificate properly, ensure the certificate file has the correct permissions:

Windows:

* OneAgent: File should be accessible to `LOCAL_SYSTEM`
* ActiveGate: File should be accessible to `LOCAL_SERVICE`

Linux:

* OneAgent: File should be accessible to `dtuser`
* ActiveGate: File should be accessible to `dtuserag`

## Upload a custom extension

After signing your extension and uploading the root certificate, you can upload the custom extension to your Dynatrace environment.

### Troubleshoot permission errors

If you encounter any permission errors when accessing the certificate file (for example, `Error opening file /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem : Permission denied`):

1. Check the file permissions:

   * Linux:

     + OneAgent: `ls -l /var/lib/dynatrace/oneagent/agent/config/certificates/root.pem`
     + ActiveGate: `ls -l /var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/root.pem`
   * Windows: Open the file properties and go to the **Security** tab.
2. Verify the permissions match those described in [Certificate file permissions](#certificate-file-permissions).
3. After correcting the file permissions, [restart the Extension Execution Controller](/managed/ingest-from/extensions/advanced-configuration/eec-custom-configuration#restart-eec "Configure the Extension Execution Controller (EEC).") if the extension continues to fail.