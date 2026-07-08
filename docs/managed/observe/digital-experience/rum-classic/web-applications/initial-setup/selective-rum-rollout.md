---
title: Roll out RUM Classic selectively for your applications
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout
---

# Roll out RUM Classic selectively for your applications

# Roll out RUM Classic selectively for your applications

* How-to guide
* Published Mar 04, 2025

The following instructions use the RUM enablement setting at the application level. While the [RUM enablement setting at the process group level](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-for-process-groups "Learn how to configure Real User Monitoring Classic for process groups."), in principle, also allows for implementing a selective RUM rollout approach, this tends to be complex and error-prone—particularly in multi-tier environments. For this reason, we recommend using the application-level setting instead.

After deploying OneAgent in full-stack monitoring mode on a host, web applications running on that host are, by default, automatically monitored using RUM. This means that the RUM JavaScript is injected into web pages, and RUM-specific headers and cookies are added to both HTTP requests and responses. Unless you've already defined application detection rules that apply to these web applications, the captured RUM data is associated with a catch-all application that, by default, has the name "My web application".

However, there may be cases where you prefer to roll out RUM in a more selective or phased manner after deploying OneAgent. The steps for doing this depend on whether your environment has already captured RUM data or not. The following sections guide you through both scenarios.

## If your environment has already captured RUM data

If your environment has already captured RUM data, perform the following actions to implement a selective RUM rollout.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Identify your catch-all application**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-identify-your-catch-all-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Move relevant traffic out of your catch-all application**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-move-relevant-data-out-of-your-catch-all-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Disable RUM in advance before you deploy OneAgent**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-disable-rum-before-deploying-oneagent "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Roll out RUM for an application**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-1-roll-out-rum-for-an-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Step 1 Identify your catch-all application

To identify your catch-all application

1. Go to **Web**.
2. In the application list, look for **My web application**, which is the default name for the catch-all application.
3. If you can't find it, someone might have renamed it. To locate it, open any other application and replace the application ID in the URL with `EA7C4B59F27D43EB`. You'll be redirected to your catch-all application.

### Step 2 Move relevant traffic out of your catch-all application

To implement a phased RUM rollout, it's essential that your catch-all application does not contain any relevant traffic and disabling it is safe. You can achieve this by moving any relevant traffic into one or more dedicated applications, as described in [Define applications for Real User Monitoring | Suggested approach](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#automated-approach "Learn how to define your applications following the suggested, manual, or application detection rules approach.") or [Define applications for Real User Monitoring | Application detection rules approach](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

Ensure that your application detection rules use patterns that are specific enough to distinguish between applications. For example, if you create a detection rule for `www.example.com`, using a broader pattern like `example.com` may be too general—especially if all your company’s application domains end with `example.com`. In this case, `www.example.com` would be a more precise and appropriate choice.

### Step 3 Disable RUM in advance before you deploy OneAgent

To disable RUM in advance for all web applications running on hosts where OneAgent has not yet been deployed

1. Go to **Web**.
2. Select your catch-all application.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Enablement and cost control**.
5. Turn off **Enable Real User Monitoring**.

### Step 4 optional Roll out RUM for an application Optional

When you are ready to roll out RUM for an application, define a new RUM application, as described in [Define applications for Real User Monitoring | Application detection rules approach](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach."). As already recommended in step 2, choose patterns that are specific enough to distinguish between applications.

## If your environment has not captured RUM data yet

If your environment has not captured RUM data yet, perform the following actions to implement a selective RUM rollout.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Disable RUM in advance before you deploy OneAgent**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-2-disable-rum-before-deploying-oneagent "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Roll out RUM for an application**](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/selective-rum-rollout#method-2-roll-out-rum-for-an-application "Roll out RUM selectively after installing OneAgent in full-stack monitoring mode on your hosts")

### Step 1 Disable RUM in advance before you deploy OneAgent

To disable RUM in advance for all web applications running on hosts where OneAgent has not yet been deployed

1. Go to **Settings**.
2. From the settings, select **Web and mobile monitoring** > **Enablement and cost control**.
3. Turn off **Enable Real User Monitoring**.

### Step 2 optional Roll out RUM for an application Optional

When you are ready to roll out RUM for an application, define a new RUM application, as described in [Define applications for Real User Monitoring | Application detection rules approach](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder#application-detection-rules "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

Ensure that your application detection rules use patterns that are specific enough to distinguish between applications. For example, if you create a detection rule for `www.example.com`, using a broader pattern like `example.com` may be too general—especially if all your company’s application domains end with `example.com`. In this case, `www.example.com` would be a more precise and appropriate choice.

To enable RUM for your newly created application

1. Go to **Web**.
2. Select your application.
3. In the upper-right corner of the application overview page, select **More** (**…**) > **Edit**.
4. From the application settings, select **General settings** > **Enablement and cost control**.
5. Turn on **Enable Real User Monitoring**.