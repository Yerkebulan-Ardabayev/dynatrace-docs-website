---
title: Set up agentless RUM in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring
scraped: 2026-02-21T21:19:29.423697
---

# Set up agentless RUM in the New RUM Experience

# Set up agentless RUM in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Feb 03, 2026

As covered in [Find the suitable instrumentation approach](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup#find-suitable-instrumentation-approach "Learn how to set up the New RUM Experience for web frontends."), agentless RUM is the appropriate choice for scenarios where:

* You donât have access to the web server, or your technology doesnât support automatic injection.
* You do have access to the application code.

Once youâve confirmed these conditions, follow the steps below to set up agentless RUM.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring#create-frontend "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Select and configure the snippet format**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring#select-snippet-format "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Insert the RUM JavaScript**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring#insert-rum-javascript "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Verify your setup**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring#verify-setup "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")[![Step 5](https://dt-cdn.net/images/step-5-2de312b50f.svg "Step 5")

**Keep the RUM JavaScript up-to-date**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-agentless-monitoring#keep-rum-javascript-up-to-date "Learn how to set up agentless RUM for your web frontends in the New RUM Experience.")

## Step 1 Create a frontend

To create a frontend for agentless RUM

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Frontend** to start the **Frontend creation** flow.
3. In the **Start monitoring** step, select the frontend type **Web** and provide a frontend name.
4. In the **Select instrumentation method** step, select **Agentless**.
5. Select **Create**.
6. In the **Setup** step, check under **Select capability and settings** if **RUM** is enabled. If it isnât enabled, select  **Override** and turn it on.
7. If you want to capture [user interactions](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/user-interactions "Learn how to configure and customize user interaction capturing for web frontends.") such as clicks and scrolls, enable **User Interactions**.
8. To ensure compliance with applicable data privacy regulations, configure the required settings under **End users' data privacy**. For more information about the available options, see [Configure data privacy settings for web frontends](/docs/observe/digital-experience/new-rum-experience/web-frontends/additional-configuration/data-privacy-web "Learn about the available settings that help you ensure your web frontends comply with data privacy regulations.").
9. Under **Copy JavaScript tag**, select  to copy the RUM JavaScript to the clipboard.

The provided RUM JavaScript has the [JavaScript tag snippet format](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."). This format is recommended for most scenarios because it ensures automatic updates. With this snippet, the monitoring code loads and executes synchronously.

## Step 2 optional Select and configure the snippet format Optional

The New RUM Experience provides several snippet formats to meet different requirements. For details on the available formats and their configurability, see [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."). For each snippet format, an [API endpoint](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API") is available.

To get the different snippet formats in the UI

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select the frontend you want to instrument.
4. On the **Settings** tab, select **Manual insertion**.
5. Scroll to the section for the snippet format you want to use. Then select  to copy the RUM JavaScript to the clipboard.

## Step 3 Insert the RUM JavaScript

Add the RUM JavaScript to the `<head>` element of every HTML page you want to monitor, and make sure itâs the first executable script on the page.

The example below shows a simple HTML page before and after inserting the RUM JavaScript.

Before insertion

After insertion

```
<!DOCTYPE html>



<html  lang="en">



<head>



<meta charset="UTF-8">



<title>MyApp</title>



<script type="text/javascript" src="myapp.js"></script>



</head>



<body>



<form>



Username: <input type="text" name="username"/><br/>



Password: <input type="password" name="password"/><br/>



<input type="submit" value="Login">



</form>



</body>



</html>



</html>
```

```
<!DOCTYPE html>



<html  lang="en">



<head>



<meta charset="UTF-8">



<title>MyApp</title>



<script type="text/javascript" src="https://js-cdn.dynatrace.com/jstag/145e12d594f/cg36988wxq/477g8ec68708x5c1_complete.js" crossorigin="anonymous"></script>



<script type="text/javascript" src="myapp.js"></script>



</head>



<body>



<form>



Username: <input type="text" name="username"/><br/>



Password: <input type="password" name="password"/><br/>



<input type="submit" value="Login">



</form>



</body>



</html>
```

### Use of template files

For websites that use frameworks or systems with templating, you can usually add custom JavaScript to all pages by placing it in a shared template fileâcommonly named `header.html` or similar. These files are typically included automatically in every page during server-side rendering or static site generation. If your site architecture supports centralized templates, use this approach to insert the RUM JavaScript snippet.

### Use of tag managers

When using tag managers, it can be difficult to guarantee that the RUM JavaScript is the first executable script on the page. If you cannot ensure this, you may lose informationâsuch as certain timings or user eventsâthat are only available when both the RUM monitoring code and the configuration are fully loaded and initialized.

This constraint is more pronounced if you configure the **script execution** option of the [JavaScript tag](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), [OneAgent JavaScript tag](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#oneagent-js-tag "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience."), or [OneAgent JavaScript tag with SRI](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats#oneagent-js-tag-sri "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.") to **async** or **defer**.

## Step 4 Verify your setup

If your frontend is receiving traffic, the charts in [![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals**](/docs/observe/digital-experience/new-rum-experience/experience-vitals "The Experience Vitals app provides an entry point for monitoring web and mobile frontends.") should begin showing data within ten minutes.

If no data appears yet, your environment may require further configuration steps. The guide [Finalize the initial setup for your agentless frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-agentless "Verify and complete the initial setup for your agentless frontend.") provides a series of checks to help you identify the configuration needed.

## Step 5 Keep the RUM JavaScript up-to-date



If you inserted the RUM JavaScript using the [JavaScript tag](/docs/observe/digital-experience/web-applications/initial-setup/snippet-formats#js-tag "Select a format for the RUM JavaScript snippet that best fits your specific use case") snippet format, the monitoring code and configuration update automatically. For other snippet formats, you need to update the RUM JavaScript whenever the configuration changes.

The recommended approach is to integrate the snippet insertion into your build process using the [RUM manual insertion tags API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API"). This ensures your application consistently runs with the latest configuration.

## Related topics

* [Select a snippet format in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/snippet-formats "Learn how to select the format for the RUM JavaScript snippet that best fits your specific use case in the New RUM Experience.")
* [RUM manual insertion tags API](/docs/dynatrace-api/environment-api/rum/rum-manual-insertion-tags "Learn how you can download the RUM manual insertion tags via API")
* [Finalize the initial setup for your agentless frontend](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/finalize-initial-setup-agentless "Verify and complete the initial setup for your agentless frontend.")