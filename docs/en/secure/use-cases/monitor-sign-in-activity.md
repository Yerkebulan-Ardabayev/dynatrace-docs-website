---
title: Monitor suspicious sign-in activity with Dynatrace
source: https://www.dynatrace.com/docs/secure/use-cases/monitor-sign-in-activity
scraped: 2026-02-28T21:13:18.394214
---

# Monitor suspicious sign-in activity with Dynatrace

# Monitor suspicious sign-in activity with Dynatrace

* Latest Dynatrace
* Tutorial
* Updated on Jan 28, 2026

As organizations embrace cloud technologies, monitoring sign-in logs is crucial for detecting anomalies, investigating suspicious activities, and ensuring regulatory compliance. Real-time visibility into login behavior helps rapidly address security risks, protect user identities, and safeguard critical resources. It also provides actionable insights into compromised accounts, malicious insiders, and user behavior patterns, aiding strategic decisions on access management, device policies, and application usage.

While the following scenario focuses on Microsoft Entra ID logs as an example, the described approach is universally applicable to any cloud, access, or identity provider integrated with Dynatrace. This is made possible through Semantic Dictionary and the standardized data mapping to the defined [semantic model](/docs/semantic-dictionary/model/log "Get to know the Semantic Dictionary models related to Log Analytics.").

As long as sign-in logs from a supported identity provider are ingested into Dynatrace, you can follow the steps outlined below to monitor these logs effectively.

## Target audience

Security administrators and security teams responsible for safeguarding their organizationâs cloud environment and user activity.

## Scenario

Your organization relies on Microsoft Entra ID as a centralized identity provider, granting users single-sign-on (SSO) access to various company applications and services.
Microsoft Entra ID sign-in logs are forwarded to Dynatrace and stored in Grail to gain deeper visibility into user activity, creating a unified data hub for monitoring and analysis.

As a security administrator, your responsibility is to

* Safeguard user identities belonging to your organization
* Monitor user access and track patterns to spot unusual behavior quickly
* Identify and investigate potential threats or anomalous sign-in events
* Start incident response activities promptly to minimize damage if a user account gets compromised

### Goals

* Achieve comprehensive visibility over the cloud environment and user activity through a single pane of glass.
* Demonstrate how to monitor Microsoft Entra ID sign-in logs and user activity to detect potential security issues and anomalous behaviors.

## Prerequisites

* Knowledge of [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") and [how to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.").
* Send Microsoft Entra ID sign-in logs to Dynatrace. There are two options to stream logs:

  + [Azure Native Dynatrace Service](/docs/ingest-from/microsoft-azure-services/azure-platform/azure-native-integration "Set and configure your Dynatrace SaaS environment using Azure Marketplace.")
  + [Azure Log Forwarder](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")
* Follow the instructions in [Create a pipeline for processing](/docs/platform/openpipeline/use-cases/tutorial-technology-processor#pipeline "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.") to configure the OpenPipeline environment. Select **Azure Entra ID Audit Logs** as the built-in processor.

## Get started

1. Import dashboard

Use our sample dashboard to view user sign-in activities within your cloud environments.

1. Download the [sample dashboard from GitHubï»¿](https://dt-url.net/ur03wvb).
2. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time."), select ![Import](https://dt-cdn.net/images/dashboards-app-dashboards-page-import-6a06e645df.svg "Import") **Upload**, then select the downloaded file.

2. Set up filters

1. In **Product**, filter for `Azure` to display Microsoft Entra ID sign-in logs coming from the connected Azure environment.
2. Use the timeframe selector to narrow down your investigation to relevant incidents, identify trends or anomalies within that window, and efficiently monitor user activities or suspicious behavior during critical times.

   ![filtering](https://dt-cdn.net/images/2025-03-26-18-28-55-1865-3328587bcd.png)
3. To fine-tune your investigation, consider setting up additional filters. For example:

   * **User**, to analyze individual sign-in trends, devices, and locations for specific users, helping you to identify unusual access patterns or targeted attacks.
   * **User IP address**, to investigate activities from particular IP addresses, detecting repeated failed sign-ins or unusual access origins.
   * **Device OS**, to track the operating systems used during sign-ins, helping you to spot outdated or unauthorized devices.
   * **Country**, to examine sign-ins by geographic location to detect access from unexpected or restricted regions.
   * **Target service**, to identify which services or applications are being accessed, useful for monitoring sensitive resources.
   * **Result code**, to review the outcomes of sign-in attempts to detect anomalies, such as excessive failed attempts indicating potential brute-force attacks.
   * **Client application**, to determine which applications are being used to sign in, useful for identifying unauthorized or suspicious app usage.

3. Review activity and trends

In the **Sign-in activity monitoring** section, you can

* Analyze sign-in trends
* Identify peak activity periods
* Investigate access patterns by location or IP address

This enables you to gain a clear understanding of user distribution and quickly spot irregular activities from unexpected regions, helping you enhance security and respond to potential risks effectively.

![An overview dashboard example](https://dt-cdn.net/images/image-50-2540-6620ffd45d.png)

Run query

You can reproduce the **Sign-in activity outcomes over time** chart in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| makeTimeseries {



Success = countIf(audit.result=="Succeeded", default:0),



Failure = countIf(audit.result!="Succeeded", default:0)



}, time:audit.time
```

4. Drill down

In the **Top sign-in activity breakdown** section, you can explore detailed insights into user and IP-based sign-in activities.

**Example 1**: In **Top 10 sign-in users**, you can identify

* Anomalies such as account lockouts or potential brute-force attacks
* Users with the highest number of sign-in attempts, categorized by successful and failed attempts
* Users with the most failed attempts, with associated IP addresses and client applications

![sign-in users](https://dt-cdn.net/images/2025-03-26-14-46-19-1359-17c6e4d12e.png)

Run query

Top 10 sign-in users

Top 10 users by failed sign-in attempts

You can reproduce the **Top 10 sign-in users** chart in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| summarize {



Success = countIf(audit.result=="Succeeded" or isNull(result.code)),



Failure = countIf(audit.result!="Succeeded", by:{User=audit.identity



}



| sort Success+Failure desc



| limit 10
```

You can reproduce the **Top 10 users by failed sign-in attempts** table in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



and audit.result!="Succeeded"



| summarize {



Failures = count(),



`Client applications` = collectDistinct(client.app.name),



`IPs` = collectDistinct(client.ip)



}, by:{User=audit.identity}



| sort Failures desc



| limit 10
```

**Example 2**: In **Top 10 sign-in IPs**, you can

* Uncover unusual patterns which may indicate malicious activity, such as repeated failed attempts from a single IP or multiple users accessing from the same IP
* View rankings of IP addresses with the most sign-in attempts, along with those linked to multiple users or services

![sign-in-ip](https://dt-cdn.net/images/2025-03-26-17-26-56-1644-34f2135bb6.png)

Run query

Top 10 sign-in IPs

Top 10 addresses by failed sign-in attempts

You can reproduce the **Top 10 sign-in IPs** chart in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



| summarize {



Success = countIf(audit.result=="Succeeded" or isNull(result.code)),



Failure = countIf(audit.result!="Succeeded")



}, by:{IP=client.ip}



| sort Success+Failure desc



| limit 10
```

You can reproduce the **Top 10 addresses by failed sign-in attempts** table in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") with the following DQL snippet:

```
fetch logs



| filter isNotNull(audit.action) and isNotNull(authentication.is_multifactor)



and audit.result!="Succeeded"



| summarize {



Failures = count(), Users = collectDistinct(audit.identity),



`Target services` = collectDistinct(client.app.name)



}, by:{`Client IP`=client.ip, City=actor.geo.city.name}



| sort Failures desc



| limit 10
```

5. Analyze data

Dynatrace Intelligence automatically identifies anomalous trends and deviations in sign-in logs, significantly enhancing your organization's ability to detect potential threats swiftly. Dynatrace Intelligence continuously analyzes user sign-in patterns, providing proactive alerts when anomalies are detected.

To detect anomalous peaks within the observed sign-in logs with Dynatrace Intelligence

1. Select any of the time-based charts, then select **Open with**.

   ![open-with](https://dt-cdn.net/images/sssssss-1102-25711b87e5.png)
2. Select **Notebooks**.
3. In the notebook document that opens, select **Options**.
4. In the **Options** panel, select **Analyze and alert** and activate the analyzer.
5. Select an analyzer and configure its parameters.
6. Select **Run analysis**.

For example, you can select an auto-adaptive threshold to apply a dynamic approach based on the past sign-in trends.

![An example of AI data analysis in the Notebooks app.](https://dt-cdn.net/images/2025-03-27-12-52-08-1920-d8b53c4e4a-1444-3573714c33.png)

## Summary

Monitoring sign-in activities in cloud environments is essential for detecting anomalies, protecting critical resources, and ensuring compliance. Integrating sign-in logs into the Dynatrace platform centralizes visibility into user access patterns. By analyzing metrics like top users, IP addresses, client applications, and locations, security teams can swiftly identify suspicious behavior and address potential threats. The dashboardâs filtering options allow targeted investigations, enhancing threat detection and accelerating incident response.