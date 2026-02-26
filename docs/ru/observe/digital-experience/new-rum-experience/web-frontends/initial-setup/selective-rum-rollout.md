---
title: Roll out RUM selectively for your frontends in the New RUM Experience
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout
scraped: 2026-02-26T21:20:38.329654
---

# Roll out RUM selectively for your frontends in the New RUM Experience

# Roll out RUM selectively for your frontends in the New RUM Experience

* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

The following instructions use the RUM enablement setting at the frontend level. While the [RUM enablement setting at the process group level](/docs/observe/digital-experience/web-applications/additional-configuration/rum-for-process-groups "Learn how to configure Real User Monitoring for process groups."), in principle, also allows for implementing a selective RUM rollout approach, this tends to be complex and error-proneâparticularly in multi-tier environments. For this reason, we recommend using the frontend-level setting instead.

After deploying OneAgent in full-stack monitoring mode on a host, web applications running on that host are, by default, automatically monitored using RUM. This means that the RUM JavaScript is injected into web pages, and RUM-specific headers and cookies are added to both HTTP requests and responses. Unless you've already defined frontend detection rules that apply to these web applications, the captured RUM data is associated with a catch-all frontend that, by default, has the name **My web application**.

However, there may be cases where you prefer to roll out RUM in a more selective or phased manner after deploying OneAgent. The steps for doing this depend on whether your environment has already captured RUM data or not. The following sections guide you through both scenarios.

## If your environment has already captured RUM data

If your environment has already captured RUM dataâeven if itâs exclusively RUM Classic so farâperform the following actions to implement a selective RUM rollout.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Identify your catch-all frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout#method-1-identify-your-catch-all-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Move relevant traffic out of your catch-all frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout#method-1-move-relevant-data-out-of-your-catch-all-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")

[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Disable RUM in advance before you deploy OneAgent**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout#method-1-disable-rum-before-deploying-oneagent "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")[![Step 4 optional](https://dt-cdn.net/images/dotted-step-4-2b9147df5b.svg "Step 4 optional")

**Roll out RUM for a frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout#method-1-roll-out-rum-for-a-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")

### Step 1 Identify your catch-all frontend

To identify your catch-all frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. In the frontend list, look for **My web application**, which is the default name for the catch-all frontend.
4. If you can't find it, someone might have renamed it. To locate it, enter the ID `EA7C4B59F27D43EB` in the  **Search frontends** field.

### Step 2 Move relevant traffic out of your catch-all frontend

To implement a phased RUM rollout, it's essential that your catch-all frontend does not contain any relevant traffic and disabling it is safe. You can achieve this by moving any relevant traffic into one or more dedicated frontends, as described in [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience."). If you haven't enabled the New RUM Experience for your catch-all frontend yet, examine the captured data in RUM Classic.

Ensure that your frontend detection rules use patterns that are specific enough to distinguish between frontends. For example, if you create a detection rule for `www.example.com`, using a broader pattern like `example.com` may be too generalâespecially if all your companyâs application domains end with `example.com`. In this case, `www.example.com` would be a more precise and appropriate choice.

### Step 3 Disable RUM in advance before you deploy OneAgent

To disable RUM in advance for all web applications running on hosts where OneAgent has not yet been deployed

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select your catch-all application.
4. On the **Settings** tab, select **Enablement and cost control**.
5. Turn off **RUM Classic**. This disables both RUM Classic and the New RUM Experience.
6. Select **Save**.

### Step 4 optional Roll out RUM for a frontend Optional

When you are ready to roll out RUM for a frontend, define a new RUM frontend and frontend detection rules, as described in [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience."). As already recommended in step 2, choose patterns that are specific enough to distinguish between frontends.

## If your environment has not captured RUM data yet

If your environment has not captured RUM data yet, perform the following actions to implement a selective RUM rollout.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Disable RUM in advance before you deploy OneAgent**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout#method-2-disable-rum-before-deploying-oneagent "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")[![Step 2 optional](https://dt-cdn.net/images/dotted-step-2-8ae6982454.svg "Step 2 optional")

**Roll out RUM for a frontend**](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/selective-rum-rollout#method-2-roll-out-rum-for-a-frontend "Learn how to roll out RUM selectively for your frontends after installing OneAgent on your hosts.")

### Step 1 Disable RUM in advance before you deploy OneAgent

To disable RUM in advance for all web applications running on hosts where OneAgent has not yet been deployed

1. Go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **Real User Monitoring** > **Traffic and cost control** > **Web frontends**.
2. Turn off **Enable Real User Monitoring Classic**. This disables both RUM Classic and the New RUM Experience.
3. Select **Save changes**.

### Step 2 optional Roll out RUM for a frontend Optional

When you are ready to roll out RUM for a frontend, define a new frontend and frontend detection rules, as described in [Set up an auto-injected frontend in the New RUM Experience](/docs/observe/digital-experience/new-rum-experience/web-frontends/initial-setup/set-up-auto-injected-frontend "Learn how to set up an auto-injected web frontend in the New RUM Experience.").

Ensure that your frontend detection rules use patterns that are specific enough to distinguish between frontends. For example, if you create a detection rule for `www.example.com`, using a broader pattern like `example.com` may be too generalâespecially if all your companyâs application domains end with `example.com`. In this case, `www.example.com` would be a more precise and appropriate choice.

To enable RUM for your newly created frontend

1. Go to ![Experience Vitals](https://dt-cdn.net/images/experience-vitals-256-9999590b55.png "Experience Vitals") **Experience Vitals** > **Overview**.
2. Select  **Web** to view all web frontends.
3. Select your catch-all application.
4. On the **Settings** tab, select **Enablement and cost control**.
5. Turn on **RUM Classic** and **RUM**.
6. Select **Save**.