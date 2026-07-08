---
title: Migrate OneAgent extension
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-oa-extension
---

# Migrate OneAgent extension

# Migrate OneAgent extension

* Published Dec 08, 2023

While reconfiguring or reinstalling existing OneAgents to point them to your SaaS environment, the `plugin_deployment` folder should remain intact. Hence, there is no need to redeploy the extension package in either scenario. The only required step is to upload the extension to the new SaaS environment.

## Upload a OneAgent extension

To upload a OneAgent extension

1. Go to **Settings** > **Monitoring** > **Monitored technologies**.
2. Select **Add new technology monitoring**.
3. In the **Monitor any technology** section, select **Add OneAgent extension**.
4. Upload the extension package.
5. After successful upload, you should find the extension on the **Monitored technologies** page in the Dynatrace web UI, on the **Custom extensions** tab.

   ![Extension demo upload](https://dt-cdn.net/images/demo-01-uploaded-plugin-1356-7a52b3cc3a.png)

   Extension demo upload

Note that you can automate the upload to the Dynatrace Cluster using the [Extensions SDK](/managed/ingest-from/extensions/develop-your-extensions#upload-plugin-command "Develop your own Extensions in Dynatrace.") or the [Dynatrace API](/managed/dynatrace-api/configuration-api/extensions-api/post-an-extension "Upload an extension file to your environment via the Dynatrace API.").

## Upload an Extensions 2.0 extension

To upload an Extensions 2.0 extension

1. Go to **Extensions**.
2. Scroll to the bottom of the page and select **Upload custom Extension 2.0**.
3. Select your extension archive (or drag and drop it) and upload it to Dynatrace. Dynatrace Hub verifies the extension archive and structure and automatically enables it after a successful upload.
4. Most fields are pre-filled based on the extension YAML file. You can provide release notes with information explaining the reason for migration.

## Deploy an extension from Dynatrace Hub

Many extensions are already in Dynatrace Hub. In that case, you need to install them from your SaaS environment Hub.

To install an extension from Dynatrace Hub

1. Go to **Extensions**.
2. Find the extension tile in the **Dynatrace Extensions 2.0 you can add to your environment** section.
3. Select the tile, then select **Add to environment**.