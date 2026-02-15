---
title: Sign extensions
source: https://www.dynatrace.com/docs/ingest-from/extensions/develop-your-extensions/sign-extensions
scraped: 2026-02-15T21:24:29.478599
---

# Sign extensions

# Sign extensions

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Oct 07, 2025

Each extension uploaded to a Dynatrace environment must be signed so that Dynatrace can verify the authenticity and integrity of the extension. After you've signed your extension, each host running your extension, whether OneAgent or ActiveGate, needs to have the root certificate saved in a dedicated directory.

* In a development environment, each developer should have a unique leaf certificate. This ensures the traceability of changes.
* In a production environment, each extension must be signed with its own leaf certificate. This guarantees the authenticity of each extension.

## Sign your extension

Depending on your needs, choose one of the following methods to sign and build your extension:

* [`dt-extensions-sdk`ï»¿](https://dynatrace-extensions.github.io/dt-extensions-python-sdk/cli/sign.html) - an all-in-one CLI tool Recommended
* [VSCode Extension](/docs/ingest-from/extensions/develop-your-extensions/addon-for-vscode "Introduction to the Dynatrace Extensions add-on for VS Code") - an all-in-one editor-based tool Recommended
* [Use OpenSSL](/docs/ingest-from/extensions/develop-your-extensions/sign-extensions/manually-openssl "Sign an extension manually with OpenSSL.") - a standard crypto library for manual control

Dynatrace CLI

You can also use the Dynatrace CLI (`dt-cli`) to sign your extension. Since its features are fully contained within `dt-extensions-sdk` CLI, only use it as a lighter alternative for CI/CD environments.

Read more about [`dt-cli` on GitHubï»¿](https://github.com/dynatrace-oss/dt-cli).

## Upload your root certificate

Each host running your extension, whether OneAgent or ActiveGate, needs to have the root certificate saved in a dedicated directory. This step is required to enhance the security of the Extensions framework.

By doing this:

* You verify the authenticity of distributed extensions
* You prevent potential malicious extension distribution by an intruder who could take control of your environment

For JMX extensions, you only need to add the certificate to the Dynatrace [credential vault](/docs/manage/credential-vault "Store and manage credentials in the credential vault.").
When adding the certificate, select the **Extension validation** scope.

### Remote extensions

Upload your root certificate to each ActiveGate host within the ActiveGate group selected for running your extensions

Save the `root.pem` certificate file in the following location:

* **Linux:**  
  `<CONFIG>/remotepluginmodule/agent/conf/certificates/` (default: `/var/lib/dynatrace/remotepluginmodule/agent/conf/certificates/`)
* **Windows:**  
  `%PROGRAMDATA%\dynatrace\remotepluginmodule\agent\conf\certificates`

### Local extensions

Upload your root certificate to each OneAgent host or each OneAgent host within the host group selected for running your extensions.

Save the `root.pem` certificate file in the following location:

* **Linux:**  
  `/var/lib/dynatrace/oneagent/agent/config/certificates`
* **Windows:**  
  `%PROGRAMDATA%\dynatrace\oneagent\agent\config\certificates`