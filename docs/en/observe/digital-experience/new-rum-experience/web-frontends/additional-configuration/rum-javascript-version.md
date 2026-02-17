---
title: Control the RUM JavaScript version in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/rum-javascript-version
scraped: 2026-02-17T05:02:40.230348
---

# Control the RUM JavaScript version in the New RUM Experience

# Control the RUM JavaScript version in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

You can control which RUM JavaScript version is used for each of your web frontends. Available options include the **Latest stable** and **Previous stable** versions. You can also configure a [custom version](#custom-version) for your environment, which will be added to the list of selectable versions.

Depending on when your environment was created, the additional versions **Latest IE7-10 supported** and **Latest IE11 supported** may also be provided. However, these versions are not compatible with the New RUM Experience and cannot be selected when it's enabled.

## Configure the RUM JavaScript version for a frontend

To select the RUM JavaScript version

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to configure.
4. On the **Settings** tab, select ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Open in Settings**.
5. Go to **General** > **RUM JavaScript Updates**.
6. Select the required RUM JavaScript version from the dropdown list.
7. Select **Save changes**.

## Set up a custom version for your environment

To set up a custom version for your environment

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **General** > **Versions and updates** > **Custom RUM JavaScript version**.
2. Select the required version from the dropdown.
3. Select **Save changes**.

When you configure the RUM JavaScript version as described in [Configure the RUM JavaScript version for a frontend](#configure-js-version), a custom version option will now show up in the dropdown list.