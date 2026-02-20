---
title: Check application detection rules
source: https://www.dynatrace.com/docs/observe/digital-experience/web-applications/additional-configuration/application-detection-rules
scraped: 2026-02-20T21:28:52.824734
---

# Check application detection rules

# Check application detection rules

* Explanation
* 1-min read
* Published Apr 03, 2020

With application detection rules, you can define the transactions that can compromise your RUM applications. User actions detected by Dynatrace are grouped together to represent your application from the user perspective, thereby enabling standalone monitoring and analysis in Dynatrace.

You can now check if the defined detection rules are detecting traffic from the correct URLs and accurately reflecting the applications that theyâre designed to detect. By checking the URL of any auto-injected RUM application, you can:

* See exactly which detection rules match the entered URL
* Confirm that RUM is enabled for your monitored application
* Quickly access detection rule configuration by selecting the rule's **Edit** button
* Gain control over the setup and testing of your application detection rules

To better understand the defined application detection rules and their impact on your application

1. Go to **Settings** > **Web and mobile monitoring** > **Application detection**.
2. Under **Check your existing detection rules**, enter the URL, and select **Check URL**.

You can create up to 1,000 application detection rules per environment.

![Application detection rules](https://dt-cdn.net/images/application-detection-rules-2187-0b3847405f.png)