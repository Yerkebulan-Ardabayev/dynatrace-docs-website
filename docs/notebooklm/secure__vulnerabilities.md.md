# Dynatrace Documentation: secure/vulnerabilities.md

Generated: 2026-02-17

Files combined: 1

---


## Source: vulnerabilities.md


---
title: Vulnerabilities
source: https://www.dynatrace.com/docs/secure/vulnerabilities
scraped: 2026-02-17T04:49:38.140019
---

# Vulnerabilities

# Vulnerabilities

* Latest Dynatrace
* App
* Updated on Feb 04, 2026

About the app

### What you'll learn

* Filter, format, and sort to find relevant vulnerability information.
* Prioritize vulnerabilities based on Dynatrace Security Score, Dynatrace Assessment, affected and related entities, historical context, CISA KEV catalog.
* Apply fixes, track remediation, drill down to the source of vulnerabilities, change the mute status of affected entities.
* Interact with other apps and download results to share with others.
* Gain insights into monitoring coverage and exposure trends with the [**Vulnerability coverage** dashboard](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

### Target audience

![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** is dedicated to devsecops engineers.

Prerequisites

* Review the [supported technologies](/docs/secure/application-security#rva-tech "Access the Dynatrace Application Security functionalities.").
* [Set up Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#start "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

Permissions

An [admin user](/docs/manage/identity-access-management/permission-management/default-policies#access "Dynatrace default policies reference") needs to assign the following IAM policies to the group of users that will access the [`vulnerability-service`](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements#vulnerability-service "Complete reference of IAM policies and corresponding conditions across all Dynatrace services."):

* `Read Entities`
* `Read Security Events`
* One of the following user policies: `Admin User`, `Pro User`, `Standard User` (for details, see [Default policies](/docs/manage/identity-access-management/permission-management/default-policies#default-policies "Dynatrace default policies reference")).

See below for instructions.

1. Create a group

1. In **Account Management**, select **Identity & access management** > **Group management**.
2. Select  **Group** to create the group.

   ![add a group](https://dt-cdn.net/images/2024-12-05-15-57-23-1895-68ceeae80a.png)
3. Enter a name (for example, `vulnerability-service`) and a description (for example, `vulnerability-service group`), then select **Create**.

2. Assign policies to the group

Once the group is created, you can view details and assign policies.

1. Select  **Permission**.

   ![assign policies](https://dt-cdn.net/images/2024-12-05-14-52-36-1902-2b2ef3db6a.png)
2. In the drop-down menu of **Permission name**, select and save the three required policies, one at a time.

Once added, the three policies should be displayed in your list of permissions.

![required policies](https://dt-cdn.net/images/2024-12-09-19-34-41-1908-a1b779b33e.png)

3. Add users to the group

1. In **Account Management**, select **Identity & access management** > **People**.
2. Select **Invite user** to invite users to the newly created group.

For details on IAM policies, see [Working with policies](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies "Working with policies").

Get started

Related blogs

![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** detects if the applications in your Dynatrace environment use vulnerable libraries at runtime or vulnerable runtime to execute your code. It helps you prioritize based on context and impact, efficiently addressing remediation actions.

For additional visibility into monitoring coverage and exposure, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

![Vulnerability results table on the Prioritization page](https://dt-cdn.net/images/one-1920-3b90d3d40b.png)![Vulnerability details](https://dt-cdn.net/images/two-1920-2dec9771f5.png)![Process group overview related to a vulnerability](https://dt-cdn.net/images/three-1920-6b45726007.png)![Details of an affected process group](https://dt-cdn.net/images/four-1920-f0bf314049.png)![Findings overview page](https://dt-cdn.net/images/2025-12-17-14-29-30-1920-06cddbfea0.png)![Finding details](https://dt-cdn.net/images/2025-12-17-14-37-49-1920-1ecd920899.png)

1 of 6

Try ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** and [share your feedbackï»¿](https://dt-url.net/up03ph5) to help us improve.

## Learning modules

[01Vulnerabilities concepts

* Explanation
* Concepts that are specific to the Dynatrace Vulnerabilities app.](/docs/secure/vulnerabilities/concepts)[02Manage results

* How-to guide
* Filter, format, and sort to find relevant vulnerability information.](/docs/secure/vulnerabilities/manage-results)[03Address remediation

* How-to guide
* Address remediation and optimize remediation activities.](/docs/secure/vulnerabilities/address-remediation)[04Prioritize vulnerabilities

* How-to guide
* Prioritize third-party, code-level, and runtime vulnerabilities.](/docs/secure/vulnerabilities/prioritize)[05Explore findings

* How-to guide
* View, filter, and analyze vulnerability findings from Dynatrace and external security tools.](/docs/secure/vulnerabilities/explore-findings)[06Assess coverage

* Explanation
* Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.](/docs/secure/vulnerabilities/assess-coverage)[07Integrate vulnerability insights across Dynatrace and external apps

* How-to guide
* Navigate between Dynatrace apps, share vulnerability data externally, and automate remediation workflows.](/docs/secure/vulnerabilities/collaborate-with-apps)

* [Introducing the Dynatrace Vulnerability feed: Accurate, transparent, and threat-awareï»¿](https://www.dynatrace.com/news/blog/introducing-the-dynatrace-vulnerability-feed-accurate-transparent-and-threat-aware/)
* [Introducing findings in the Vulnerabilities app: Unified, granular insights for smarter securityï»¿](https://www.dynatrace.com/news/blog/introducing-findings-in-the-vulnerabilities-app-unified-granular-insights-for-smarter-security/)
* [CVE-2025-55182: React2Shell Critical Vulnerability â what it is and what to doï»¿](https://www.dynatrace.com/news/blog/cve-2025-55182-react2shell-critical-vulnerability-what-it-is-and-what-to-do/)
* [Supply chain security: How to detect malicious software packages with Dynatraceï»¿](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Prioritize vulnerabilities based on the CISA Known Exploited Vulnerabilities Catalogï»¿](https://www.dynatrace.com/news/blog/prioritize-vulnerabilities-based-on-the-cisa-known-exploited-vulnerabilities-catalog/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADRï»¿](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture managementï»¿](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace launches Python Vulnerability Monitoring for enhanced customer securityï»¿](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Snyk integration for Dynatrace: Bridging development and runtime with actionable security notificationsï»¿](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protectionï»¿](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Discover the new Dynatrace Runtime Vulnerability Analytics experienceï»¿](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [The anatomy of broken Apache Struts 2: A technical deep dive into CVE-2024-53677ï»¿](https://www.dynatrace.com/news/blog/the-anatomy-of-broken-apache-struts-2-a-technical-deep-dive-into-cve-2024-53677/)


---
