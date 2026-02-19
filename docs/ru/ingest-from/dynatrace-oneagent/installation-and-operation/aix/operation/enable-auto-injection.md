---
title: Automated injection of deep-code monitoring on AIX
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/enable-auto-injection
scraped: 2026-02-19T21:24:30.907619
---

# Automated injection of deep-code monitoring on AIX

# Automated injection of deep-code monitoring on AIX

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jun 22, 2022

On AIX, Dynatrace supports deep-code monitoring for Java, Apache, WebLogic and Websphere applications. Since OneAgent version 1.189, you only need to **Allow AIX kernel extension** on your AIX **Host settings** page in Dynatrace. For earlier releases, you need to perform some configuration on AIX, see [Install OneAgent on AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/installation/install-oneagent-on-aix "Learn how to download and install Dynatrace OneAgent on AIX.").

## Enable automated injection

To enable automated injection

1. After you install OneAgent and it successfully connects to Dynatrace, in Dynatrace, go to **Hosts** and select your AIX host.
2. On the host details page, select **More** (**â¦**) > **Settings**.
3. Select the **AIX kernel extension** tab.
4. Turn on **Allow AIX kernel extension**.  
   OneAgent will then begin collecting deep-code monitoring data.

You can use the [Settings API](/docs/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") to configure your automated injection.

1. To learn the schema, use [GET a schema](/docs/dynatrace-api/environment-api/settings/schemas/get-schema "View a settings schema via the Dynatrace API.") with `builtin:host.monitoring.aix-kernel-extension` as the schemaId.
2. Based on the `builtin:host.monitoring.aix-kernel-extension` schema, create your configuration object.
3. To create your configuration, use [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.").

## Update OneAgent version 1.187 and earlier

If you manually configured your AIX host to inject OneAgent code modules, we recommend that you clear the `LDR_PRELOAD` and the `LDR_PRELOAD64` environment variables after you enable the automated injection. This enables you to uninstall OneAgent simply using the [uninstall script](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix/operation/uninstall-oneagent-on-aix "Learn how you can remove OneAgent from your AIX-based system.") without the need to clear the environment variables.