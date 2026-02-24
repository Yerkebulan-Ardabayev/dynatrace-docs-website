---
title: Control the RUM JavaScript version
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/rum-javascript-version
scraped: 2026-02-24T21:24:50.241523
---

# Control the RUM JavaScript version

# Control the RUM JavaScript version

* How-to guide
* Published Jul 01, 2025

You can control which RUM JavaScript version is used for each of your web applications. Available options include at least the **Latest stable** and **Previous stable** versions. Depending on when your environment was created, additional versions for Internet Explorer may also be provided; for details, see [RUM JavaScript for Internet Explorer](#rum-javascript-for-ie). You can also configure a [custom version](#custom-version) for your environment, which will be added to the list of selectable versions.

## Configure the RUM JavaScript version for an application

To select the RUM JavaScript version

1. Go to **Web**.
2. Select the application that you want to configure.
3. In the upper-right corner of the application overview page, select **More** (**â¦**) > **Edit**.
4. From the application settings, select **Injection** > **RUM JavaScript updates**.
5. Select the required RUM JavaScript version from the dropdown list.
6. Select **Save changes**.

## Set up a custom version for your environment

To set up a custom version for your environment

1. Go to **Settings** > **Web and mobile monitoring** > **Custom RUM JavaScript version**.
2. Select the required version from the dropdown.
3. Select **Save changes**.

When you configure the RUM JavaScript version as described in [Configure the RUM JavaScript version for an application](#configure-js-version), a custom version option will now show up in the dropdown list.

## RUM JavaScript for Internet Explorer

* We ended support for Internet Explorer 7â10 starting with RUM JavaScript version 1.265.
* We ended support for Internet Explorer 11 starting with RUM JavaScript version 1.293.

As a result, starting with these versions, the RUM JavaScript can't initialize on these browsers and, therefore, can't send any RUM data to Dynatrace. The browser console will show a message stating that the RUM JavaScript is disabled or that the browser can't parse the RUM JavaScript.

Depending on when your environment was created, specific RUM JavaScript versions are available that ensure compatibility with Internet Explorer 7â10 and Internet Explorer 11, respectively.

RUM JavaScript version 1.263 is the last version that is compatible with Internet Explorer 7â10, and RUM JavaScript version 1.291 is the last version that is compatible with Internet Explorer 11. These versions are provided as is and will not receive any more updates.

### Internet Explorer 7â10

* **Environments created in Dynatrace version 1.266+**: You can't use the RUM JavaScript version that is compatible with Internet Explorer 7â10.
* **Environments created before Dynatrace version 1.266**: You can choose a version of the RUM JavaScript that is compatible with Internet Explorer 7â10. Select the **Latest IE7-10 supported** option in step 5 of the instructions in [Configure the RUM JavaScript version for an application](#configure-js-version).

### Internet Explorer 11

* **Environments created in Dynatrace version 1.294+**: You can't use the RUM JavaScript version that is compatible with Internet Explorer 11.
* **Environments created before Dynatrace version 1.294**: You can choose a version of the RUM JavaScript that is compatible with Internet Explorer 11. Select the **Latest IE11 supported** option in step 5 of the instructions in [Configure the RUM JavaScript version for an application](#configure-js-version).

### Internet Explorer 11 with Compatibility View

If your application might be viewed via Internet Explorer 11 with Compatibility View enabled, use the **Latest IE7-10 supported** version, not the **Latest IE11 supported** version. If you choose the **Latest IE11 supported** version, the RUM JavaScript won't initialize, and the browser console will display the following message:

```
Unsupported Internet Explorer version detected. Only version 11 (without Compatibility View) is supported!
```