---
title: Getting started
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started
---

# Getting started

# Getting started

* How-to guide
* 5-min read
* Updated on Jul 02, 2026

This guide walks you through installing the Dynatrace Extensions add-on for Visual Studio Code, connecting to your Dynatrace environment, and publishing your first extension using the built-in VS Code workflows.

## Before you begin

### Installation

You can find **Dynatrace Extensions** in the Visual Studio Code [marketplace﻿](https://marketplace.visualstudio.com/items?itemName=DynatracePlatformExtensions.dynatrace-extensions). Install it from there or via the VS Code extension search.

### Access token

Our VS Code add-on automates many operations around extensions development by using the Dynatrace API.

To get the most out of it, create an [API Access Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") with the following scopes:

* `WriteConfig`
* `ReadConfig`
* `credentialVault.read`
* `credentialVault.write`
* `extensions.read`
* `extensions.write`
* `extensionEnvironment.write`
* `extensionEnvironment.read`
* `extensionConfigurations.read`
* `extensionConfigurations.write`
* `metrics.read`
* `entities.read`
* `settings.read`
* `settings.write`

The Dynatrace UI provides a dedicated template called **Extension Development**, which applies these exact token scopes.

### Connectivity settings

Required only if your Dynatrace environment is accessible through a dedicated URL that uses a custom-signed or a self-signed SSL certificate.

To configure the connectivity settings for your Dynatrace environment:

1. Open the **Extensions** view in Visual Studio Code, find **Dynatrace Extensions**, select the  icon, and then select **Settings**.

   For details, see [Settings in Visual Studio Code﻿](https://code.visualstudio.com/docs/getstarted/settings).
2. Search for `DynatraceExtensions tenant` in the search bar to find the **Tenant Connectivity Settings**, then select **Edit in settings.json**.
3. Register your dedicated environment URL in the file you've opened and either provide the path to your CA file or turn off SSL verification.

   For example:

   ```
   {



   "dynatraceExtensions.tenantConnectivitySettings": [



   {



   "tenantUrl": "https://my.custom.dynatrace/e/abcd-123",



   "certificatePath": "/tmp/certificates/ca.crt"



   }



   ]



   }
   ```

   For more details, see [Tenant connectivity settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#tenant-connectivity-settings "Details of settings available to configure Dynatrace Extensions").

## Connect to Dynatrace

To connect your Dynatrace environment:

1. Go to **Dynatrace Extensions** in the **Extensions** view in Visual Studio Code, then select the **Add environment** button.
2. Provide the base URL to access Dynatrace. It should follow one of these patterns:

   * `https://<Id>.live.dynatrace.com` for SaaS environments.
   * `https://<Domain>/e/<Id>` for Managed environments. Replace `<Id>` with your environment ID and `<Domain>` with your managed environment domain.
   * `https://<Id>.apps.dynatrace.com` for the latest Dynatrace Platform.
3. Provide the **API Access Token** you prepared earlier and optionally provide a label.
4. Set this as your current environment.

The add-on displays your environment in the list and uses the current environment for all API operations. Visit [Environments](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#environments "Details about the specialized activity bar views for Dynatrace Extensions") to learn more about using the **Environment** view.

## Initialize your workspace

It's time to create your first project. If you have to open a different workspace folder, select **Open folder**. Otherwise, select the **Initialize workspace** button to start.

To learn how to use the Workspaces view, visit [Extension 2.0 workspaces](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/specialized-views#extension-20-workspaces "Details about the specialized activity bar views for Dynatrace Extensions").

### 1. Schema validation

The workflow starts with your target schema version. Choose any from the list. It ensures that we can validate your extension manifest while you're writing it, allowing you to spot any issues early on.

### 2. Developer certificates

Developer certificates are used to sign and package your extension. Choose **Generate new ones** to generate a new set of certificates kept in VS Code's storage.

Check the extension's [settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings "Details of settings available to configure Dynatrace Extensions") to get the exact path to where your credentials are stored.

The workflow offers some additional convenience steps:

* Whether to use these certificates as defaults for all workspaces:

  + This will update your global settings for Dynatrace Extensions to reflect this choice.
  + As part of this guide, choose **Yes**.
* Whether to upload the new CA certificate to the Dynatrace Credentials Vault.

  + You need to provide a name and, optionally, a description.
  + As part of this guide, choose **Yes** and provide the additional details.
* Whether to upload the new CA certificate to locally installed OneAgents and ActiveGates.

  + This step only appears if a local OneAgent or ActiveGate installation is detected.
  + This step requires running VS Code with Administrator privileges.
  + As part of this guide, choose **No**.

To learn how to use your existing developer certificates, visit [Credentials](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#credentials "Details of settings available to configure Dynatrace Extensions").

### 3. Project template

The final step of the workflow is to choose the type of project you want to start. It allows the extension to generate relevant files.

Since this is your first extension, choose **Extension 2.0 ⭐** at this step.

This option is the default choice for new projects and creates the following starting setup:

* `extension` - the folder where all extension assets are placed.
* `extension/extension.yaml` - this is your extension's manifest file.

To learn more about the other types of projects, visit [Project templates](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/commands#project-templates "Overview of all the commands available within Dynatrace Extensions").

In addition, all templates also create the following folders and files:

* `.vscode` - a folder for storing workspace-specific VS Code settings.
* `dist` - a folder for storing all extension packages.
* `config` - a folder for storing your monitoring configuration files.
* `.gitignore` - a file containing useful rules for ignoring unnecessary items from your git repository.

## Make some changes to your extension

Start by opening up the extension manifest and making some changes. Give your extension a name, and add yourself as the author.

For example, update the `extension/extension.yaml` file with the following information:

```
name: custom:my.first.extension



version: "0.0.1"



minDynatraceVersion: "1.265.0"



author:



name: <Your-Name>
```

Replace `<Your-Name>` with the author's name.

## Publish your extension

Finally, perform the following steps to upload your extension to Dynatrace.

1. Select the F1 key and choose the **Dynatrace extensions: Build** command. The workflow builds your extension and creates a package inside your `dist` folder.
2. When prompted about uploading your extension to Dynatrace, choose **Yes**.
3. When prompted about activating this extension version, choose **Yes**.

Congratulations. You created, built, uploaded, and activated your first Extension 2.0. You can view this in the Dynatrace UI by navigating to Extensions.