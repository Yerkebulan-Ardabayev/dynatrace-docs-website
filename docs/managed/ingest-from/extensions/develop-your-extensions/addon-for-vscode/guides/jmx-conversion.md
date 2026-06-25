---
title: Migrate JMX extensions
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/guides/jmx-conversion
scraped: 2026-05-12T12:35:19.832387
---

# Migrate JMX extensions

# Migrate JMX extensions

* How-to guide
* 3-min read
* Published Jun 16, 2025

The [Extensions Framework](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") for JMX has been available since version 1.213 and brings you new possibilities for visualizing and querying your data. Follow this guide to learn how to leverage Visual Studio Code to convert your 1.0 extensions to the new format automatically.

## Prerequisites

1. Complete the first-time setup for your editor

   For simplicity, this guide will assume you have already configured your editor for first-time use. If you haven't used Dynatrace Extensions for VS Code before, follow our [Getting started guide](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes.") to complete your first-time setup.

   This guide assumes you have access to developer credentials. If you followed the [Getting started](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/getting-started "Set up your Visual Studio Code editor and get your first extension built and uploaded to Dynatrace in 5 minutes.") guide, store the generated credentials in VS Code's global settings. An example is shown the [Settings](/managed/ingest-from/extensions/develop-your-extensions/addon-for-vscode/settings#when-using-your-credentials "Details of settings available to configure Dynatrace Extensions") page.
2. Enable JMX 2.0 extensions in your environment

   Go to **Settings > Preferences > OneAgent features** and enable **Java Metric Extensions (JMX)**, then restart your monitored Java processes.

## Convert a JMX Extension as a new project

### Initialize your workspace

1. Create a new folder on your computer and open it in VS Code.
2. Press F1 then select the command **Dynatrace extensions: Initialize workspace**
3. Next, choose schema version **1.275.0** from the list
4. When prompted about certificates, choose **Use existing**
5. When prompted about project type, choose **JMX 1.0 Conversion**

Your workspace has been initialized, and you're ready to convert your old extension.

### Convert your extension

1. You need to load the JMX 1.0 Extension for conversion. You can browse your local filesystem for a `.zip` or `plugin.json` file or browse your connected Dynatrace environment. As part of this guide, we'll do the latter. Choose to load it **Remotely**.
2. You are now presented with a list of extensions from your tenant. Choose which one you want to convert.

   After selecting an extension, you may be prompted for a new extension name if your old one is too long.
3. Next, you should select a technology so that Process pages can be configured automatically. Choose one that applies to your Java process. Otherwise, choose **All other**.
4. Optionally, we can also show the data on your Host's page. To follow along with this guide, select **Yes**.

The conversion will generate your new extension manifest at `extension/extension.yaml`.

## Convert a JMX Extension standalone

If you don't want to initialize a new workspace for your project or you're already working within a registered workspace, you can run our automation as a standalone command.

Press F1 and select the command **Dynatrace Extensions: Convert JMX**. This workflow starts by first prompting you to load the extension and follows the same steps as mentioned above.

At the end, your new manifest will be placed in `extension/extension.yaml`, or you'll be prompted for a save destination if this folder doesn't exist in the currently opened workspace.

## Deploy and configure your new extension

### Build and upload to Dynatrace

1. Build the extension by pressing F1 then clicking the command **Dynatrace extensions: Build**.
2. Then, choose to upload it to Dynatrace by clicking **Yes**.
3. Next, activate this extension by clicking **Yes**.

### Add a monitoring configuration

1. Open your extension either from the prompt or from the Extensions menu in Dynatrace.
2. Add a monitoring configuration by clicking the button.
3. Select a Host running your Java process, then click **Next step**.
4. On the next page click **Next step** once again, then add a description and click **Activate**.

Once your monitoring configuration is activated, data collection starts automatically.

## Find your extension's data

Open the details page of one of the hosts running your monitored Java process. You should see a card (towards the bottom) with a title starting with **JMX Metrics**.

From that card, select any of the processes listed. Then click `...` and choose **Metrics and logs analysis**.

On the page that opens, you'll have multiple cards from your extension.

The cards on the Process page are only added if you selected a technology during the conversion.