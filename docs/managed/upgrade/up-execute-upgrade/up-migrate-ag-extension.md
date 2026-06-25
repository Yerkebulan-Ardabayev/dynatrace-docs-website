---
title: Migrate ActiveGate extension
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension
scraped: 2026-05-12T12:13:58.722587
---

# Migrate ActiveGate extension

# Migrate ActiveGate extension

* Published Dec 08, 2023

If you have an ActiveGate Extensions 1.0 or Extensions 2.0 extension in your Dynatrace Managed environment and you need to migrate it to your SaaS environment, you might need to deploy it again, review and adjust the ActiveGate's configuration, and upload it to the SaaS environment.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Deploy the extension package**](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension#deploy-extension "Migrate your ActiveGate extension to SaaS.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Review the ActiveGate properties**](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension#review-properties-new-host "Migrate your ActiveGate extension to SaaS.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Upload the extension**](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension#upload-extension-new-host "Migrate your ActiveGate extension to SaaS.")

## Step 1 Deploy the extension package

The steps for migrating ActiveGate extensions depend on the selected method of ActiveGate migration.

* If you don't change the ActiveGate's host during migration, the `plugin_deployment` directory should remain intact, and there's no need to redeploy the extension package.
* If you change the ActiveGate's host, copy the extension package to the ActiveGate deployment directory (`%PROGRAMFILES%\dynatrace\remotepluginmodule\plugin_deployment` or `/opt/dynatrace/remotepluginmodule/plugin_deployment`).

## Step 2 Review the ActiveGate properties

In **Deployment Status** > **ActiveGates**, filter by ActiveGate group, ensure that the extension modules are enabled, and restart the ActiveGate and Extensions Execution Controller (EEC) services if needed. You can find the names of properties for **Module: Extension 1.0** and **Module: Extension 2.0** in [configuration properties and parameters](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate "Learn which ActiveGate properties you can configure based on your needs and requirements.").

## Step 3 Upload the extension

### Extensions 1.0 extension

To upload an Extensions 1.0 extension in the new SaaS environment

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Select **Add new technology monitoring**.
3. In the **Monitor remote technologies** section, select **Add ActiveGate extension**.
4. Upload the extension package.
5. After successful upload, you should find the extension on the **Monitored technologies** page in the Dynatrace web UI, on the **Custom extensions** tab.

   ![Extension demo upload](https://dt-cdn.net/images/demo-01-uploaded-plugin-1356-7a52b3cc3a.png)

   Extension demo upload

Note that you can automate the upload to the Dynatrace Cluster using the [Extensions SDK](/managed/ingest-from/extensions/develop-your-extensions#upload-plugin-command "Develop your own Extensions in Dynatrace.") or the [Dynatrace API](/managed/dynatrace-api/configuration-api/extensions-api/post-an-extension "Upload an extension file to your environment via the Dynatrace API.").

### Extensions 2.0 extension

To upload an Extensions 2.0 extension in the new SaaS environment

1. Go to **Extensions**.
2. Scroll to the bottom of the page and select **Upload custom Extension 2.0**.
3. Select your extension archive (or drag and drop it) and upload it to Dynatrace.

   Dynatrace Hub verifies the extension archive and structure and automatically enables it after a successful upload.
4. Most fields are pre-filled based on the extension YAML file. You can provide release notes with information explaining the reason for migration.

## Deploy extension from Dynatrace Hub

Many extensions are already in Dynatrace Hub. In that case, you need to install them from Dynatrace Hub in your SaaS environment.

To deploy an extension from Dynatrace Hub in your SaaS environment

1. Go to **Extensions**.
2. Find the extension tile in the **Dynatrace Extensions 2.0 you can add to your environment** section.
3. Select the tile, then select **Add to environment**.