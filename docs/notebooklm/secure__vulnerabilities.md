# Dynatrace Documentation: secure/vulnerabilities

Generated: 2026-02-17

Files combined: 6

---


## Source: address-remediation.md


---
title: Address remediation
source: https://www.dynatrace.com/docs/secure/vulnerabilities/address-remediation
scraped: 2026-02-17T05:02:32.005669
---

# Address remediation

# Address remediation

* Latest Dynatrace
* How-to guide
* Updated on Jan 28, 2026

In the following, you'll learn how to manage remediation of entities affected by or related to a vulnerability. You can

* [Apply fix recommendations from Snyk](#snyk) Third-party vulnerabilities
* [Apply fixes from Security Advisor](#dsa) Third-party vulnerabilities
* [Connect affected entities to your ticketing system and track the remediation progress](#remediation-tracking)
* [Drill down into the source of vulnerabilities](#source)
* [Change the mute status of affected entities](#mute-entities)
* [Initiate deeper analysis with Dynatrace Intelligence generative AI](#explain)

## Apply fix recommendations from Snyk

Third-party vulnerabilities

For vulnerabilities based on the [Snykï»¿](https://snyk.io/) feed, a fix recommendation is displayed if one is available. It consists of a library upgrade suggestion to solve the vulnerability.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Details** and look for **Fix recommendation**.

Make sure to restart processes after upgrading a library.

## Apply fixes from Security Advisor

Third-party vulnerabilities

With Security Advisor, you can determine

* Which patches and upgrades in the monitored technologies to apply for maximum remediation impact
* How many vulnerabilities you can solve by updating a specific library
* How many of the total solvable vulnerabilities are the most severe

To filter by Security Advisor fixes

1. On the **Prioritization** page, on the upper-left of the vulnerabilities table, select **Security Advisor**. This opens a side window with a list of fixes.
2. Select ![Filter for](https://dt-cdn.net/images/filter-for-efd104354d.svg "Filter for") for the desired library. This filters the vulnerabilities table by the total number of vulnerabilities for a selected library that would be fixed by upgrading the library.

Make sure to restart processes after upgrading a library.

* You can add as many Security Advisor filters as you want.
* To remove a filter, select  next to the desired library.
* To remove all filters, select **Clear all**.

### Further reading

To learn more about Security Advisor, see [Concepts: Security Advisor](/docs/secure/vulnerabilities/concepts#dsa "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Track remediation progress

You can add links to tickets created in your issue tracking system for [affected entities](/docs/secure/vulnerabilities/concepts#affected "Concepts that are specific to the Dynatrace Vulnerabilities app.").

Adding a tracking link allows you to

* Navigate to the associated URL
* Track the remediation progress of the selected entities

You can easily check, for example, if someone is already working on fixing the vulnerability.

### Set up tracking links

You can add, edit, or delete tracking links individually or in bulk.

Individually

In bulk

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities**.
3. Select **View all process groups** (**View all Kubernetes nodes**) to navigate to the process group (or Kubernetes node) overview page related to the vulnerability.
4. You have the following options:

   * To add a tracking link, in the **Tracking link** column, select **Set link** for the desired entity.
   * To edit or delete a link, in the **Tracking link** column, select ![More actions](https://dt-cdn.net/images/dashboards-app-menu-kebab-c39eda426b.svg "More actions") next to the tracking link for the desired entity, and then select **Edit tracking link** or **Delete tracking link**.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities**.
3. Select **View all process groups** (**View all Kubernetes nodes**) to navigate to the process group (or Kubernetes node) overview page related to the vulnerability.
4. You have the following options:

   * To add a tracking link, select the desired entities, and then select **Set tracking links**.
   * To edit or delete a tracking link, select the desired entities, and then select **Change tracking links** > **Edit tracking links** or **Delete tracking links**.

## Drill down into the source of vulnerabilities

To fix vulnerabilities you need to find the root cause. You can examine

* [Vulnerable components](#vulnerable-component) Third-party vulnerabilities
* [Entry points](#entry-points) Code-level vulnerabilities
* [Code location](#code-location) Code-level vulnerabilities

### Examine vulnerable components

Third-party vulnerabilities

Identify which libraries contain the vulnerability and how many affected process groups (or Kubernetes nodes) are impacted.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities** and look for **Vulnerable components**.

You can also view vulnerable components on the overview page of process groups or Kubernetes nodes:

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities**.
3. Under **Process group overview** (or **Kubernetes node overview**), either select a specific process group (or Kubernetes node), or select **View all process groups** (**View all Kubernetes nodes**) to open the related overview page.
4. From there, select an affected entity to view details, including the name of the vulnerable component.

**Further reading**

* [FAQ: Why is a fixed vulnerability still showing as open?](/docs/secure/faq#open "Frequently asked questions about Dynatrace Application Security.")
* [Concepts: Vulnerable component](/docs/secure/vulnerabilities/concepts#vulnerable-component "Concepts that are specific to the Dynatrace Vulnerabilities app.")
* [Vulnerability evaluation: Third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.")

### Examine entry points

Code-level vulnerabilities

Analyze entry points to determine how the vulnerability could be exploited and identify potential attack paths.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Details** and look for **Entry points**.

If the same vulnerability is reachable by multiple HTTP paths, multiple entry point entries are listed. To save memory and network traffic, a limited number of entries is displayed.

If a code-level vulnerability is resolved or is about to be resolved in the next 30 minutes, the entry points are no longer open (vulnerable).

**Further reading**

* [Concepts: Entry points](/docs/secure/vulnerabilities/concepts#entry-points "Concepts that are specific to the Dynatrace Vulnerabilities app.")

### Examine code location

Code-level vulnerabilities

View the source of the vulnerable function call to quickly assess its impact and origin.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Details** and look for **Code location**.

## Change the mute status of affected entities

You can change the mute status of [affected entities](/docs/secure/vulnerabilities/concepts#affected "Concepts that are specific to the Dynatrace Vulnerabilities app.") according to your findings and needs. For example, you can set the status of an affected entity to `Muted (...)` **if you wish to ignore the vulnerability for this particular entity**:

* It could be a false flag, meeting some additional conditions that make the vulnerability irrelevant.
* Or maybe there's no remediation available and a workaround has been applied.

Muting all affected entities of a vulnerability sets the vulnerability status to `Muted`. For details, see [Vulnerability status](/docs/secure/vulnerabilities/concepts#status "Concepts that are specific to the Dynatrace Vulnerabilities app.").

You can change the status of affected entities individually or in bulk.

Individually

In bulk

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities**.
3. Select **View all process groups** (**View all Kubernetes nodes**) to navigate to the process group (or Kubernetes node) overview page related to the vulnerability.
4. In the **Mute status** column, select the current value for the desired entity.
5. Enter the new status and select **Save**.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities**.
3. Select **View all process groups** (**View all Kubernetes nodes**) to navigate to the process group (or Kubernetes node) overview page related to the vulnerability.
4. Select the desired entities.
5. Select **Change status**.
6. Enter the new status and select **Save**.

Mute status and remediation decisions depend on vulnerability monitoring scope. Vulnerabilities on hosts or processes excluded from monitoring rules won't appear here.  
For visibility into overall monitoring coverage and exposure trends, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

## Initiate deeper analysis with Dynatrace Intelligence generative AI

To use this generative AI functionality, ensure the following:

* Dynatrace Intelligence generative AI has been enabled at the environment level. For details, see [Enable Dynatrace Intelligence generative AI on your environment](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Learn how to set up Dynatrace Intelligence generative AI.").
* You have permissions to access it. For details, see [User permissions](/docs/dynatrace-intelligence/copilot/copilot-getting-started#davis-copilot-user-permissions "Learn how to set up Dynatrace Intelligence generative AI.").

Dynatrace Intelligence generative AI can provide contextual, plain-language explanations of vulnerabilities to accelerate understanding and remediation.

To access the functionality

1. In [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), select a vulnerability.
2. In the upper-right corner of the vulnerability details pane, select  **Explain vulnerability**.

When selected, Dynatrace Intelligence generative AI analyzes the technical details of a vulnerability and generates a structured summary that may include:

* **What the vulnerability means**: Explains the nature of the issue (for example, SQL injection in application code, CCS Injection in OpenSSL, insecure configuration) and how it arises in thirdâparty libraries, dependencies, or code.
* **Why it matters**: Highlights severity levels and risk scores, and describes potential implications including unauthorized data access, session hijacking, manâinâtheâmiddle attacks, or system compromise.
* **What to investigate**: Points to affected functions, entry points, components, or libraries. Suggests reviewing exposure (for example, whether entities are accessible via public networks), reachable data assets, exploit availability (public or private), and whether vulnerable thirdâparty libraries (such as outdated OpenSSL or Node.js builds) are in use.
* **How to respond**: Recommends remediation steps such as patching code, upgrading dependencies or runtimes, restricting access, monitoring suspicious activity, and reviewing other applications that may rely on vulnerable components.

The structure and depth of generative AI's explanation may vary depending on the vulnerability type and available context. While Dynatrace Intelligence generative AI aims to provide detailed insights, not all vulnerabilities will include every element listed above.

Dynatrace Intelligence generative AI explanations are tailored to the nature of each vulnerabilityâwhether it's cross-site scripting, denial-of-service, remote code execution, or similar security weaknessesâproviding relevant, actionable insights that accelerate triage and support informed decision-making, even for users without deep security expertise.


---


## Source: assess-coverage.md


---
title: Assess coverage
source: https://www.dynatrace.com/docs/secure/vulnerabilities/assess-coverage
scraped: 2026-02-17T05:09:25.590609
---

# Assess coverage

# Assess coverage

* Latest Dynatrace
* Explanation
* Published Dec 18, 2025

To gain insights into your environment's [Runtime Vulnerability Analytics (RVA)](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") coverage and pinpoint areas of exposure, you can use the readyâmade **Vulnerability coverage** dashboard.

The dashboard currently addresses library vulnerability coverage in runtime. Support for additional types, such as codeâlevel vulnerabilities, Kubernetes, and runtime coverage, is planned for upcoming releases.

## Overview

The **Vulnerability coverage** dashboard supports your workflows for managing results and prioritizing remediation by providing a clear overview of vulnerability concentration and how coverage evolves over time. It helps you

* Highlight monitoring gaps by showing processes not monitored, aggregated to the host level.
* Surface the most affected entities to support prioritization.
* Track trends in findings and scans over time.

Dashboard example

![Vulnerability coverage](https://dt-cdn.net/images/2025-12-04-15-16-56-1920-49c53cbfda.png)

### Prerequisites

Before using the dashboard, ensure the following prerequisites are met:

* Review the [supported technologies](/docs/secure/application-security#rva-tech "Access the Dynatrace Application Security functionalities.").
* [Set up Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#start "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* [Set up the required permissions](/docs/secure/vulnerabilities#permissions "Prioritize and efficiently manage vulnerabilities in your monitored environments.").

### Access the dashboard

You can open the dashboard either from ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** or ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**.

* From ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**:

  1. In the ![Help](https://dt-cdn.net/images/image-6c69427243.svg "Help") help menu on the upper-right of the **Prioritization** page, select **About this app**.
  2. Go to the **Contents** tab and select **Vulnerability coverage**.
* From ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**:

  1. On the **Dashboards** page, select ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Ready-made**.
  2. Search for and open **Vulnerability coverage**.

### Host coverage calculation

Host coverage is derived from process monitoring. A host is considered covered if at least one of its processes is monitored.

The following explains how host coverage is determined for library vulnerabilities.

1. Dynatrace first collects all monitored processes.
2. Monitoring rules are applied to processes. If a process is excluded by your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."), the corresponding host is not considered covered, which decreases overall host coverage.

### Improve host coverage

To increase host coverage for thirdâparty vulnerabilities, focus on ensuring that processes are monitored.

Steps to improve coverage:

1. [Enable Third-party Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") globally.
2. Enable all the [supported technologies](/docs/secure/application-security/vulnerability-analytics#tech-tpv "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") you want Dynatrace to monitor. Only hosts running processes on listed and enabled technologies are reflected in coverage.
3. Adjust your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") to include the processes you want monitored. Excluding processes reduces host coverage.

## Use cases

With the **Vulnerability coverage** dashboard, you can accomplish various use cases, such as:

* **Validate monitoring coverage**: Ensure critical processes are monitored and reflected at the host level.
* **Support prioritization**: Identify the most affected processes and their corresponding hosts before deciding remediation steps.
* **Track exposure trends**: Monitor how vulnerability findings evolve and whether scans are keeping pace.
* **Communicate risk**: Share highâlevel coverage and severity insights with stakeholders.


---


## Source: collaborate-with-apps.md


---
title: Integrate vulnerability insights across Dynatrace and external apps
source: https://www.dynatrace.com/docs/secure/vulnerabilities/collaborate-with-apps
scraped: 2026-02-16T09:36:44.209210
---

# Integrate vulnerability insights across Dynatrace and external apps

# Integrate vulnerability insights across Dynatrace and external apps

* Latest Dynatrace
* How-to guide
* Updated on Sep 09, 2025

Dynatrace doesn't just detect vulnerabilities; it helps you act on them. You can navigate across Dynatrace apps for deeper context, share findings with external tools, and automate remediation workflows to accelerate response and reduce risk.

## Cross-app navigation

Clickable elements in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, such as related entities, affected process groups, Kubernetes nodes, or reachable data assets, serve as entry points into other Dynatrace apps, allowing you to explore related context and take informed action.

* **Examples**:

  + When viewing the **Exploit attempts** section of a code-level vulnerability in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, you can either select an individual exploit attempt or use the **View all related exploit attempts** button to access detailed information in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts."). This enables you to investigate technical details, correlate runtime evidence, and determine whether the vulnerability is being actively targeted, helping you prioritize remediation based on actual risk.
  + When viewing a vulnerability tied to a Kubernetes node in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, you can select the affected node from the Kubernetes node overview to jump directly into [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads."), where you can assess its health, dependencies, and workload impact.

Navigation also works in reverse. When exploring entities in other Dynatrace apps, such as ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** or ![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**, you may encounter vulnerability indicators or links that guide you directly to ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** for deeper analysis.

* **Examples**:

  + From [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/docs/observe/infrastructure-observability/kubernetes-app "Monitor and optimize Kubernetes with Dynatrace. Get real-time insights and health for clusters and workloads."), selecting a vulnerability in the **Vulnerabilities** section of a node or workload opens ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, pre-filtered to that specific vulnerability.
  + From [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance."), selecting the vulnerability indicator in the upper-right corner of the page opens ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, filtered by that host.

This bidirectional navigation ensures you're always one click away from full security context.

## Share and automate with external apps

Use [Workflow connectors](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.") to share vulnerability data with external platforms and automate remediation tasks.

* **Examples**:

  + Automatically create Jira issues when new vulnerabilities are detected or when thresholds are breached using [Jira Connector](/docs/analyze-explore-automate/workflows/actions/jira "Automate creating, transitioning, commenting, and assigning Jira issues on the events and schedules defined for your workflows.").
  + Send real-time alerts to specific channels or people using [Slack Connector](/docs/analyze-explore-automate/workflows/actions/slack "Send messages to Slack Workspaces") or [Microsoft Teams Connector](/docs/analyze-explore-automate/workflows/actions/microsoft-teams "Send messages to Microsoft Teams").
  + Trigger remediation workflows using [Red Hat Ansible Connector](/docs/analyze-explore-automate/workflows/actions/red-hat/redhat-ansible "Automate running of Ansible jobs based on your monitoring data and events.") or [Jenkins Connector](/docs/analyze-explore-automate/workflows/actions/jenkins "Automate pipelines in Jenkins.").

These integrations help ensure that the right teams receive timely, actionable information, without manual effort.

## Automate remediation workflows

Use the [![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**](/docs/analyze-explore-automate/workflows "Automate IT processes with Dynatrace Workflowsâreact to events, schedule tasks, and connect services.") app to automate actions based on vulnerability severity, type, or affected entities.

* **Examples**:

  + Auto-assign remediation tasks in Jira.
  + Send alerts to specific channels in Slack.
  + Launch custom scripts or CI/CD jobs using connectors like Ansible or Jenkins.

This enables proactive, scalable vulnerability management across your environment.

## Download vulnerability data as CSV

You can download data in the vulnerabilities table as a CSV file for external analysis or reporting.

To download:

1. On the **Prioritization** page, apply any filters to narrow down the results.
2. Select ![Download table](https://dt-cdn.net/images/download-table-data-ebb09d49cd.svg "Download table") to save the current view as a CSV file.

The downloaded file reflects the filters applied at the time of download.


---


## Source: concepts.md


---
title: Vulnerabilities concepts
source: https://www.dynatrace.com/docs/secure/vulnerabilities/concepts
scraped: 2026-02-17T05:05:26.046862
---

# Vulnerabilities concepts

# Vulnerabilities concepts

* Latest Dynatrace
* Explanation
* Updated on Dec 18, 2025

Understand essential concepts and key terms for ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**.

## How Dynatrace uses CVSS

Third-party vulnerabilities

Dynatrace uses the [Common Vulnerability Scoring System (CVSS)ï»¿](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System) to assess and contextualize vulnerabilities. CVSS provides a standardized framework for describing the severity, exploitability, and impact of vulnerabilities using structured vector strings and numerical scores.
This scoring system forms the foundation for the Dynatrace Security Score (DSS), which adds environmental context to help prioritize remediation.

### CVSS data source

CVSS vector data is sourced from the Snyk vulnerability feed, which includes both CVSS v3 and CVSS v4 vectors when available.

### Scoring logic

Dynatrace supports both CVSS v3 and CVSS v4 for vulnerability scoring. CVSS vector data is sourced from both the Snyk vulnerability feed and the National Vulnerability Database (NVD). When CVSS v4 vectors are available in the Snyk feed, they are used to calculate the [Dynatrace Security Score (DSS)](#dss). If CVSS v4 is not available, CVSS v3 vectors are used as a fallback.

CVSS v4 is currently supported only for vulnerabilities sourced from Snyk, not from NVD.

Scoring is based on the official [CVSS v4 calculatorï»¿](https://github.com/FIRSTdotorg/cvss-v4-calculator/blob/main/cvss_score.js) provided by [FIRST.orgï»¿](https://www.first.org/).

### CVSS vectors

In ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, each vulnerability displays two types of CVSS vectors:

* **CVSS Base Vector**: Describes the vulnerability's inherent characteristics, such as its attack vector, required privileges, user interaction, and impact on confidentiality, integrity, and availability. These traits are static and don't change across environments.
* **CVSS Modified Vector**: Adjusts the base metrics to reflect your specific environment. This includes factors like asset exposure and reachability. Modified vectors provide a more accurate reflection of risk in your context.

  + For **CVSS v3**, modified impact metrics are labeled as `MC` (Confidentiality), `MI` (Integrity), and `MA` (Availability).
  + For **CVSS v4**, these are updated to `MVC`, `MVI`, and `MVA`, where the "V" stands for **Vulnerable System Impact Metrics**, reflecting the impact on the vulnerable system itself.

Both vectors are visible on the **Prioritization** page:

* In the vulnerabilities table (go to the [column settings](/docs/secure/vulnerabilities/manage-results#format "Filter, format, and sort to find relevant vulnerability information.") ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column") and select **CVSS Base Vector** and **CVSS Modified Vector**).
* In the details of a vulnerability (in the side panel that opens when you select a vulnerability, go to **Overview** and look for **Dynatrace Security Score calculation**).

This visibility helps you understand how the CVSS score was derived and compare raw versus contextualized risk.

Dynatrace supports filtering by CVSS vector components for advanced triage. For practical examples and usage, see [Filter by CVSS vectors](/docs/secure/vulnerabilities/manage-results#cvss-filter "Filter, format, and sort to find relevant vulnerability information.").

## Dynatrace Security Score

Dynatrace calculates the severity of a vulnerability based on Dynatrace Security Score (DSS), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact.

DSS
:   An enhanced risk-calculation score based on the industry-standard [Common Vulnerability Scoring System (CVSS)ï»¿](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System). Dynatrace Security Score is designed to provide a more precise risk-assessment score by considering additional parameters such as public internet exposure and whether or not data assets are reachable from an affected entity.

**Risk-averse**: Virtually all security products use the CVSS Base Score to set the severity of security vulnerabilities. CVSS was designed to be risk-averse, which means that, for any given vulnerability, the assigned score assumes the worst-case scenario. The CVSS specification does allow for some modifications based on environmental influences, but this is usually not factored into the risk score calculation, which leads to many high or critical vulnerability scores that the user needs to handle.

**Accurate**: Dynatrace Security Score doesn't assume the worst-case scenario. Instead, it adapts the characteristics of the vulnerability to your particular environment, taking into consideration its structure and topology, and advises you as to which elements are at risk and how to handle security issues. With Dynatrace Security Score, you can find out if the affected entity is reachable from the internet and if there is any data storage in reach of an affected entity.

**Efficient**: By including additional parameters in its analysis, Dynatrace Security Score is designed to leverage data to more precisely calculate the security score and predict the potential risk of a vulnerability to your environment. By reducing the score of vulnerabilities that are considered less relevant for your environment, you gain time to focus on the most critical issues and fix them faster.

### Vulnerability score calculation

Third-party vulnerabilities

Code-level vulnerabilities

Dynatrace determines the Dynatrace Security Score for third-party vulnerabilities through a combination of CVSS data and environmental context:

1. Gather CVSS vector data

Vectors are pulled from both the Snyk vulnerability feed and the National Vulnerability Database (NVD).

* CVSS v4 is currently supported *only* for vulnerabilities from Snyk.
* CVSS v2 is [deprecatedï»¿](https://dt-url.net/f6k3wfz). For vulnerabilities relying on this data, Dynatrace Security Score can't be assessed. For the supported CVSS versions, see [How Dynatrace uses CVSS](#cvss).

2. Determine applicable CVSS version

If CVSS v4 vectors are available, theyâre used to calculate DSS. Otherwise, Dynatrace falls back to CVSS v3.

3. Incorporate environmental context

DSS adjusts the CVSS Base Score using modifiers that reflect your environment:

* **For CVSS v3**:

  + `MC` â Modified Confidentiality
  + `MI` â Modified Integrity
* **For CVSS v4**:

  + `MVC` â Modified Vulnerable Confidentiality
  + `MVI` â Modified Vulnerable Integrity

    These belong to the **Vulnerable System Impact Metrics** group in CVSS v4.

4. Calculate DSS for each affected entity

DSS is calculated individually for each affected entity. If multiple entities are impacted, the highest DSS score is used.

DSS never exceeds the original CVSS Base Score; environmental modifiers can only reduce or maintain the score.

The score of a code-level vulnerability is always `10` and the risk always `Critical` because it's considered to be exploitable at any time.

For example, on a login page where the password hasn't been sanitized before sending it to the database, thus allowing an SQL injection, it's only a matter of time until an attacker finds this vulnerability and exploits it.

### Dynatrace Risk Levels

The DSS scale ranges between 0.1 (lowest risk) and 10.0 (most critical risk):

| **Dynatrace Risk Level** | **Vulnerability score range** |
| --- | --- |
| Low risk Low | Vulnerabilities ranging between 0.1 and 3.9 |
| Medium risk Medium | Vulnerabilities ranging between 4.0 and 6.9 |
| High risk High | Vulnerabilities ranging between 7.0 and 8.9 |
| Critical risk Critical | Vulnerabilities ranging between 9.0 and 10.0 |

### Calculation differences

The Dynatrace Security Score (DSS) calculation differs between ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** and ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.

| **App** | **DSS assessment** |
| --- | --- |
| Third Party Vulnerabilities **Third-Party Vulnerabilities** | DSS is assessed based on aggregating the scores of affected entities within the selected management zone. |
| Vulnerabilities **Vulnerabilities** | DSS is assessed based on the DSS of the affected entities within the selected segment. |

Thus, the DSS (score and risk level) for vulnerabilities in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** can be lower than in ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.

#### Example

A vulnerability with `Critical` severity affects two processes, `Process_1` and `Process_2`.

1. Evaluation of risk assessment

* `Process_1` is exposed to the public internet but has no reachable data assets => DSS lowers the severity to `High`.
* `Process_2` isn't exposed to the public internet but has reachable data assets => DSS lowers the severity to `High`.

2. Final score

* In ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, DSS aggregates the risk factors of the affected entities (the vulnerability is both exposed to the public internet and has reachable data assets), thus the severity remains `Critical`.
* In ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, the score is determined by the affected entity with the highest DSS score. So if both affected entities have `High` severity, the severity is lowered from the initial `Critical` to `High`.

How to use: You can [prioritize vulnerabilities based on DSS](/docs/secure/vulnerabilities/prioritize#dss "Prioritize third-party, code-level, and runtime vulnerabilities.").

## Coverage

Coverage refers to the extent to which your environment's processes are monitored by Runtime Vulnerability Analytics (RVA). This processâlevel information is aggregated to the host level. Coverage determines whether vulnerabilities can be detected and reported for the monitored processes and their corresponding hosts.

Coverage:

* Highlights monitoring gaps where vulnerabilities may go undetected.
* Identifies the most affected processes with the corresponding hosts.
* Provides trends in findings and scans over time.

For practical guidance on how to visualize coverage, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

## Security Advisor

Security Advisor recommends the fixes that would most improve the overall security of your environment.

### Basis for calculation

To calculate recommended fixes, Security Advisor takes into consideration all third-party vulnerabilities that are currently open and not muted; resolved or muted vulnerabilities aren't taken into account. Fixes are tailored to your environment and ranked based on how much they improve the overall security of your environment.

### Grouping

Security Advisor groups specific libraries that trigger vulnerabilities to simplify remediation efforts.
When calculating the advice, Security Advisor ignores the specific version of the library. All shown libraries contain known vulnerabilities and should be updated to the latest version.

### Advice ranking

Advice is ranked based on the severity of the third-party vulnerabilities. Advice regarding a critical vulnerability, for example, is ranked higher than advice for a high-severity vulnerability.

The severity of a vulnerability is calculated based on [Dynatrace Security Score (DSS)](#dss), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact.

## Dynatrace Assessment

Understand the risk factors and assessment modes considered when assessing a vulnerability.

* [Public internet exposure](#internet-exposure)
* [Reachable data assets](#data-assets)
* [Vulnerable functions](#vulnerable-functions) Third-party vulnerabilities
* [Public exploit](#public-exploit) Third-party vulnerabilities
* [Assessment mode](#assessment-mode)

### Public internet exposure

Public internet exposure
:   One of the risk factors taken into consideration when determining the [Dynatrace Security Score](#dss). If there is public internet exposure, it means that vulnerabilities affect at least one process that is exposed to the internet.

#### States

| **State** | **Description** |
| --- | --- |
| Public network | There is public internet exposure. |
| Not detected | No public internet exposure was found. |
| Not available | Data isn't available, because the related hosts aren't running in Full-Stack Monitoring mode. For details, see [Monitoring modes](/docs/secure/application-security "Access the Dynatrace Application Security functionalities."). |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Public internet exposure`.

Further reading: [How is public internet exposure determined?](/docs/secure/faq#internet-exposure "Frequently asked questions about Dynatrace Application Security.")

### Reachable data assets

Reachable data assets
:   One of the risk factors taken to consideration when determining the [Dynatrace Security Score](#dss). If there are any reachable data assets affected it means that vulnerabilities affect at least one process that has database access (runs a database service).

#### States

| **State** | **Description** |
| --- | --- |
| Within range | There are reachable data assets affected. |
| None within range | There are no reachable data assets within range. |
| Not available | Data isn't available, because the related hosts aren't running in Full-Stack Monitoring mode. For details, see [Monitoring modes](/docs/secure/application-security "Access the Dynatrace Application Security functionalities."). |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Reachable data assets`.

### Vulnerable functions

Third-party vulnerabilities

Vulnerable function
:   One of the risk factors to consider when evaluating a vulnerability (yet they are not considered for the DSS calculation). If there are any vulnerable functions in use, there is at least one process using a vulnerable function (this might indicate a higher exploitation risk).

Class
:   The class that contains the vulnerable function related to the vulnerability.

    * Example: `org.apache.http.client.utils.URIUtils`

Function usage
:   Shows whether the vulnerable function is being used by your application. Based on whether your application uses the vulnerable function, you can assess the impact on your environment. The usage of a vulnerable function is calculated on the process level and is aggregated to the process group level, which results in a count of affected process groups per function.

    * Examples: `In use`, `Not in use`, `Not available`

#### States

| **State** | **Description** |
| --- | --- |
| In use | There are vulnerable functions in use. |
| Not in use | No vulnerable functions in use were found. |
| Not available | Data isn't available. For details, see [FAQ: Why is there no data available for vulnerable function?](/docs/secure/faq#vuln-funct-no-info-available "Frequently asked questions about Dynatrace Application Security."). |

How to use: You can

* [Filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Vulnerable functions in use`
* [Prioritize vulnerabilities based on vulnerable functions](/docs/secure/vulnerabilities/prioritize#details-functions "Prioritize third-party, code-level, and runtime vulnerabilities.")

Further reading:

* [How are vulnerable functions determined?](/docs/secure/faq#vuln-function-calculation "Frequently asked questions about Dynatrace Application Security.")
* [Why is there no information on vulnerable functions?](/docs/secure/faq#vuln-function-no-info-available "Frequently asked questions about Dynatrace Application Security.")
* [Why is there no data available for vulnerable functions?](/docs/secure/faq#vuln-function-no-data-available "Frequently asked questions about Dynatrace Application Security.")

### Public exploit

Third-party vulnerabilities

Public exploit
:   One of the risk factors to be considered when assessing a vulnerability. If there is any public exploit published, it means that malicious code to exploit this vulnerability is available on the internet.

#### States

| **State** | **Description** |
| --- | --- |
| Public exploit published | A publicly known exploit for this vulnerability is available. |
| No public exploit published | No publicly known exploit for this vulnerability is available. |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Public exploit published`.

### Assessment mode

Assessment mode
:   Determines whether detailed analysis is possible based on your monitoring mode.

#### States

| **State** | **Description** |
| --- | --- |
| Full | All process group instances are monitored in [Full-stack monitoring mode](/docs/secure/application-security#fullstack "Access the Dynatrace Application Security functionalities."). |
| Reduced | Detailed assessment isn't possible because at least one process group instance isn't monitored in Full-stack monitoring mode. |
| Not available | The vulnerability is resolved. |

How to use: You can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.") vulnerabilities by **Dynatrace Assessment** > `Assessment mode`.

#### How reduced accuracy affects the DSS calculation

The context of internet exposure or reachable data assets cannot be examined due to the lack of information, thus the DSS score can't be lowered.

## Affected and related entities

Learn about the entities affected by and related to vulnerabilities in your environment.

### Affected entities

Affected entities
:   Entities (process groups, processes, and Kubernetes nodes) for which a vulnerability was detected, and are therefore directly affected by the vulnerability.

Affected process
:   A process that contains a vulnerable library or runtime.

How to use: You can [prioritize vulnerabilities by affected entities](/docs/secure/vulnerabilities/prioritize#affected-related "Prioritize third-party, code-level, and runtime vulnerabilities.").

### Related entities

Related entities
:   Entities that are connected to one of the affected entities and, thus, indirectly affected by the vulnerability.

Related application
:   An application associated with the affected processes.

Related service
:   A service that runs directly on a vulnerable process group instance.

Related host
:   A host on which the vulnerable process runs.

Related database
:   A database that is accessed by the vulnerable process or reachable from it. It can be reached via multiple hops.

Related Kubernetes workload/cluster
:   In Kubernetes environments, the workload or cluster to which the vulnerable process belongs.

Related container image
:   In Kubernetes environments, the container image used by the affected processes.

How to use: You can [prioritize vulnerabilities by related entities](/docs/secure/vulnerabilities/prioritize#affected-related "Prioritize third-party, code-level, and runtime vulnerabilities.").

## Vulnerability source

Drill down into the source of vulnerabilities for the [vulnerable component](#vulnerable-component), [entry point](#entry-points), and [code location](#code-location).

### Vulnerable component

Third-party vulnerabilities

Vulnerable component
:   A software component (library) or runtime component (for example, a Kubernetes package) that has a vulnerable function causing a vulnerability:

    * For Snyk-based vulnerabilities, the package name (example: `org.apache.tomcat:tomcat-coyote`)

    * For NVD-based vulnerabilities, the runtime technology (examples: `Java runtime`, `Node.js runtime`)

How to use: You can [drill down and explore vulnerable components](/docs/secure/vulnerabilities/address-remediation#vulnerable-component "Address remediation and optimize remediation activities.").

Further reading: [Why is a fixed vulnerability still showing as open?](/docs/secure/faq#open "Frequently asked questions about Dynatrace Application Security.")

### Entry point

Code-level vulnerabilities

Entry point
:   A point in the code where an attacker could enter the application, for example, by passing user input fields to the application (such as a login form or search bar).

URL path
:   The path used in the HTTP request to reach and potentially exploit the vulnerability.

    * Example: `/user/1218/bio`

Untrusted input
:   The input that is passed to the vulnerable function.

Payloads
:   The user-controlled inputs that could be used to exploit the vulnerability. This may be the part of the SQL statement (for SQL injection), the command (for command injection), the JNDI lookup name (for improper input validation), or the request URL (for SSRF).
    The userâcontrolled input is highlighted. If the payload has an associated key (for example, an HTTP parameter name or an HTTP header name), it's shown after a colon.

    * Example: `HTTP parameter value: bioText`

How to use: You can [drill down and explore entry points](/docs/secure/vulnerabilities/address-remediation#entry-points "Address remediation and optimize remediation activities.").

### Code location

Code-level vulnerabilities

Code location
:   Shows where the actual vulnerability is in the code (the location where the vulnerable function is called from).

    * Example: `SQL injection at DatabaseManager.updateBio():82`

How to use: You can [drill down and explore code location](/docs/secure/vulnerabilities/address-remediation#code-location "Address remediation and optimize remediation activities.").

## Vulnerability status

Learn about the resolution and mute status of a vulnerability or [affected entity](#affected).

### States for vulnerabilities

| **State** | **Description** |
| --- | --- |
| Open | The vulnerability is active. |
| Resolved | The vulnerability was closed automatically because the root cause is no longer present. For details, see [Vulnerability evaluation: Resolution](/docs/secure/application-security "Access the Dynatrace Application Security functionalities."). |
| Muted (Open) | The vulnerability is active but all its affected entities were muted by request. |

How to use: On the **Prioritization** page, you can [filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.")

* By **Status** to see `Open` and `Resolved` vulnerabilities
* By **Mute: Status** to see `Muted (Open)` vulnerabilities

  Resolved vulnerabilities are displayed only once (at the resolution time). Extend the timeframe to include more results. For details, see [Timeframe filter](/docs/secure/vulnerabilities/manage-results#timeframe "Filter, format, and sort to find relevant vulnerability information.").

### States for affected entities

| **State** | **Description** |
| --- | --- |
| Affected | The entity is affected by the vulnerability. |
| Resolved | The entity was closed automatically because the root cause is no longer present. |
| Muted (Affected) | The entity is affected by the vulnerability but was silenced by request. |
| Muted (Resolved) | The silenced vulnerability was closed automatically because the root cause is no longer present. |

A muted entity that was closed automatically doesn't change its status to `Resolved`, but to `Muted (Resolved)`.

How to use: On the overview page of affected process groups or Kubernetes nodes, you can

* [Filter](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.")

  + By **Status** to see the affected entities that are `Affected` or `Resolved`
  + By **Mute** > **Mute: Status** to see affected entities that are `Muted (Affected)` or `Muted (Resolved)`
* [Format](/docs/secure/vulnerabilities/manage-results#format "Filter, format, and sort to find relevant vulnerability information.") affected entities table by **Status**
* [Change the mute status of affected entities](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.")

Further reference: [Can a vulnerability be resolved while there are still affected entities?](/docs/secure/faq#resolution-affected-entities "Frequently asked questions about Dynatrace Application Security.")

## Third-party library events

Third-party libraries

Prerequisite: [Enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

To help you monitor and analyze **third-party libraries** in your applications, Dynatrace provides detailed event data that captures how external libraries are assessed for security risks.

This data is represented through two types of security events:

* `VULNERABILITY_FINDING`: Represents a single vulnerability identified in a specific process at a given time.

  + For details, see [Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").
* `VULNERABILITY_SCAN`: Represents the analysis of detected packages within a specific process at a given time.

  + For details, see [Semantic Dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-scan-events "Get to know the Semantic Dictionary models related to security events.").

Both types are stored in the `security.events` table and can be queried using [DQL](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.").

As Dynatrace analyzes the libraries used by your application, it continuously generates vulnerability findings. These raw events reflect the same underlying vulnerability data shown in [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments."), but in a more granular form.

The table below highlights the core differences between the granular finding events and the aggregated view in the app and entity events:

| **Granular view (DQL)** | **Aggregated view (Vulnerabilities **Vulnerabilities**)** |
| --- | --- |
| Continuously generated by Dynatrace during library analysis | Aggregated from entity state events |
| Unaggregated event data: `VULNERABILITY_FINDING` and `VULNERABILITY_SCAN` | Vulnerability-based view with comprehensive summaries |
| Not influenced by user actions | Includes [states](#status) (open/resolved) and user-controlled input like [mute states](/docs/secure/vulnerabilities/address-remediation#mute-entities "Address remediation and optimize remediation activities.") and [tracking links](/docs/secure/vulnerabilities/address-remediation#remediation-tracking "Address remediation and optimize remediation activities.") |
| Queried using DQL | Accessed via the app interface or via DQL by querying entity state events |
| Offers deeper investigative context for custom analysis | Designed for high-level overview and vulnerability management |

Both views reflect the same underlying data and are complementaryâuse DQL for deep dives and ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** for concise overviews and comprehensive risk analysis.

Here's an example DQL query to retrieve vulnerability findings and scans:

```
fetch security.events



| filter event.provider == "Dynatrace"



| filter event.type == "VULNERABILITY_FINDING" OR event.type == "VULNERABILITY_SCAN"
```

## Ingested vulnerability findings

In addition to findings generated by Dynatrace through [thirdâparty library detection](#tpv-events) and code-level vulnerability detection, vulnerability findings can also be ingested from external security tools. These originate outside Dynatrace and are brought in via [security events ingest](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail."). For details, see [Vulnerability findings](/docs/secure/threat-observability/concepts#vuln-findings "Basic concepts related to Threat Observability").

Ingested findings represent individual vulnerabilities reported by thirdâparty products. They are stored in the `security.events` table and available in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** on the [**Findings** page](/docs/secure/vulnerabilities/explore-findings "View, filter, and analyze vulnerability findings from Dynatrace and external security tools."), where you can filter, sort, remove duplicates, and analyze them alongside Dynatraceâgenerated findings.

### Severity normalization mapping

To ensure consistency across sources, severity and risk scores from external tools are normalized to the Dynatrace unified risk scale.

Severity normalization follows this mapping:

| Reported severity | Normalized score |
| --- | --- |
| Critical | 10.0 |
| High | 8.9 |
| Medium | 6.9 |
| Low | 3.9 |
| Other/unknown | 0.0 |

For details on how normalization works, see [Severity and score normalization](/docs/secure/threat-observability/concepts#normalization "Basic concepts related to Threat Observability").


---


## Source: explore-findings.md


---
title: Explore findings
source: https://www.dynatrace.com/docs/secure/vulnerabilities/explore-findings
scraped: 2026-02-17T05:08:36.941328
---

# Explore findings

# Explore findings

* Latest Dynatrace
* How-to guide
* Updated on Jan 08, 2026

The **Findings** page, accessible by selecting the **Findings** tab in ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**, consolidates [vulnerability findings](/docs/secure/threat-observability/concepts#vuln-findings "Basic concepts related to Threat Observability") from Dynatrace and integrated external security tools into a single, actionable view. It helps reduce noise from multiple scanners (network, web app, cloud, container, SAST), providing developers and security teams with a holistic view of vulnerabilities across assets and layers of their environments.

By default, the **Findings** page displays Dynatraceâgenerated results (thirdâparty and codeâlevel). To extend it with external findings, set up integrations via [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline."). For the list of supported integrations and setup instructions, see [Security events ingest](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.").

## Manage results

In the findings table available on the **Findings** page, you can explore and refine vulnerability finding data:

* [**Filter and sort**](#filter-sort) findings by severity, product, timeframe, segments, or any available column.
* [**Format table**](#format) to switch perspectives between basic and detailed information.
* [**Show only unique IDs**](#deduplicate) to remove recurring findings.
* [**Visualize results**](#visualize) in a chart.

### Filter and sort

You have several options to filter and sort findings:

* **Filter by timeframe**: Define the period from which your data is being queried. If you don't specify the timeframe, the default `Last 30 minutes` is applied, meaning that the data being fetched is from the last thirty minutes.

  Show me how

  1. In the timeframe section, select one of the preset options or select the calendar for customization.
  2. Select **Apply**.
* **Filter by segments**: Segments provide quick access to predefined logical filters. The segment selector allows you to filter results based on these predefined logical filters.

  Show me how

  1. Open the segment selector .
  2. In **Filter by segments**, select a segment.
  3. Optional To add more segments, select  **Segments**; if available, you can select a value for the selected segment.
  4. When you're happy with the selection, select **Apply**.

  Selecting one or multiple segments results in fewer findings.

  For more information on segments and how they work, see [Segments](/docs/manage/segments "Segments logically structure monitoring data in Grail and function as convenient filters for data that users are allowed to access based on permissions.").
* **Filter by expressions**: In the filter field, you can use complex filter expressions to select which information is to be displayed, such as:

  + Add multiple filters on the same filter key
  + Use `AND` and `OR` operators
  + Use the wildcard (`*`) to search for patterns
  + Filter numbers with `>` and `<`

  Show me how

  To filter by expressions, you have two options:

  + **Option 1**: Manually type the expression in the filter field.
  + **Option 2**: Filter by field values in the results table (hover over a cell and select a filter from the context menu ).

  To reset the filters to the default mode, select ![Close tab](https://dt-cdn.net/images/xmark-d8bb8b39d8.svg "Close tab") on the right of the filter field.

  If the selected filter doesn't show in the table, go to the ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column") column settings and make sure to add the corresponding column to the table.

* **Sort columns**: You can sort the order of columns and of results.

  Show me how to sort the order of columns

  To select the order of columns, you have two options:

  + **Option 1**: From the column settings (select the column settings ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column"), then use the up and down arrows and select **Confirm**).
  + **Option 2**: From the results table (select a column title, then select  **Move left** or  **Move right**).

  Show me how to sort the order of results

  To select the order in which results in a column should be displayed:

  1. Select a column title.
  2. Select  **Sort ascending** or  **Sort descending**.

  If more than 100,000 findings are displayed, sorting isn't available. This limitation prevents performance issues with very large result sets.  
  To enable sorting, narrow your scope by applying filters.

### Format table

In the upper-left corner of the table, you can choose between two preset views of the results:

* Select **Overview** to display basic information about the findings.
* Select **Detailed** to include more detailed information.

You can easily switch between the two views and customize them (add or remove columns) according to your needs.

### Remove duplicates

Many vulnerability findings are cyclical, reappearing in every scan if the environment or feed hasn't changed. This can create noise.

To reduce this noise, ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** removes duplicates: only the latest event of a finding with the same ID is displayed.

Two findings are considered duplicates (same finding ID) if all of the following fields match:

* `object.id`
* `vulnerability.id`
* `component.name`
* `component.version`
* `product.name`
* `product.vendor`

For details on these fields, see the [Dynatrace semantic dictionary](/docs/semantic-dictionary/model/security-events#vulnerability-finding-events "Get to know the Semantic Dictionary models related to security events.").

To drill into an issue or specific affected object and observe the full historyâeven if it contains periodic identical findingsâturn off **Show unique findings** at the top of the table.

### Visualize results

The chart on the **Findings** page allows you to visualize results based on your selected criteria.

![findings chart](https://dt-cdn.net/images/2025-12-17-14-39-12-1856-e9a22b8ff8.png)

* The X-axis displays the time when the findings were detected.
* The Y-axis displays the count of the detected findings.

Select different dimensions using the **Split by** options in the drop-down list:

* **Severity**: Shows the distribution of findings by severity level (for example, Critical, High, Medium, Low).
* **Affected object**: Groups findings by the impacted Dynatrace entity (such as process, service, or host).
* **Provider**: Separates findings based on the source that reported them (for example, Dynatrace Runtime Vulnerability Analytics or an external security tool).

These options help you quickly identify trends and concentrations across different dimensions, reducing noise and highlighting where attention is most needed.

## Gain insights

Selecting a finding in the **Findings** table opens the details pane, which provides full context about the vulnerability. This view helps you quickly assess severity, trace affected components, and connect findings to remediation workflows.

The details pane includes:

* **Detection details**: When the finding was detected and its unique event ID.
* **Identifiers**: Related CVEs and linked security problems.
* **Severity & scores**: Severity level, CVSS score, and risk scores (ingested or calculated).
* **Affected object**: Name, type, and ID of the impacted Dynatrace entity, with links to its page.
* **Component metadata**: Component name, version, and package URL.
* **Source & product**: Which feature or product reported the finding (for example, Runtime Vulnerability Analytics).
* **Scan information**: Scan ID and related ingestion details.

Select the **Source** tab for a complete list of information available from the ingested finding.

## Collaborate with other apps

You can extend your analysis beyond ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** by sharing or reusing findings in other Dynatrace apps:

* **Download findings data as CSV** for offline analysis.

  1. Optional On the **Findings** page, apply any filters to narrow down the results.
  2. Select ![Download table](https://dt-cdn.net/images/download-table-data-ebb09d49cd.svg "Download table") to save the current view as a CSV file.
* **Open findings in other apps** using the  menu in the details pane next to the finding name (for example, you can send a finding to the ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** app with a preset DQL query scoped to that event).
* **Open values** from the **Source** tab of a finding's details pane directly in another app for deeper analysis.

## Further resources

* [Introducing findings in the Vulnerabilities app: Unified, granular insights for smarter securityï»¿](https://www.dynatrace.com/news/blog/introducing-findings-in-the-vulnerabilities-app-unified-granular-insights-for-smarter-security/)


---


## Source: prioritize.md


---
title: Prioritize vulnerabilities
source: https://www.dynatrace.com/docs/secure/vulnerabilities/prioritize
scraped: 2026-02-17T05:09:37.830415
---

# Prioritize vulnerabilities

# Prioritize vulnerabilities

* Latest Dynatrace
* How-to guide
* Updated on Dec 18, 2025

In the following, you'll learn to prioritize third-party, code-level, and runtime vulnerabilities based on

* [Dynatrace Security Score](#dss)
* [Dynatrace Assessment](#risk-factors)
* [What is at risk (affected and related entities)](#affected-related)
* [Exploit attempts](#exploit)
* [Vulnerability evolution](#evolution)
* [CISA KEV catalog](#cisa-kev)
* [Coverage](#coverage)

## Prioritize by Dynatrace Security Score

Third-party vulnerabilities

The risk level (severity) of a vulnerability is calculated based on Dynatrace Security Score (DSS), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact. See below for your options.

### Filter by DSS

Use Dynatrace Security Score filters to focus on vulnerabilities based on their severity and risk classification.

On the **Prioritization** page, in the filter field, you can filter by

* The DSS score (select **Dynatrace Security Score** and then enter a score)
* The risk level (select **Dynatrace Risk Level** and then select a severity)

For details, see [Filter expressions](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.").

### Get details about DSS calculation

View how the Dynatrace Security Score is calculated for individual vulnerabilities.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Overview** and look for **Dynatrace Security Score calculation**.

### FAQ

* [Why does my vulnerability have a different risk assessment and Dynatrace Security Score than its affected entities?](/docs/secure/faq#risk-assessment-affected-entities "Frequently asked questions about Dynatrace Application Security.")

### Further reading

To learn more about DSS, see [Concepts: Dynatrace Security Score](/docs/secure/vulnerabilities/concepts#dss "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Prioritize by Dynatrace Assessment

Prioritize vulnerabilities by analyzing the [risk factors and assessment modes taken into consideration when determining the Dynatrace Security Score](/docs/secure/vulnerabilities/concepts#assessment "Concepts that are specific to the Dynatrace Vulnerabilities app."). By understanding the assessment modes behind the Dynatrace Security Score, you can make smarter remediation decisions, tailor your response to business impact, and stay ahead of emerging threats. See below for your options.

### Filter by risk factors and assessment modes

Use filters to narrow down vulnerabilities based on Dynatrace Security Score assessment modes and associated risk factors.

1. On the **Prioritization** page, in the filter field, select **Dynatrace Assessment**.
2. Select the options you're interested in.

For details, see [Filter expressions](/docs/secure/vulnerabilities/manage-results#expressions "Filter, format, and sort to find relevant vulnerability information.").

### Review reachable data assets

Investigate which database services are impacted by the vulnerability and trace direct connections to affected assets.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities** and look for **Reachable data assets**.

### Review vulnerable functions

Third-party vulnerabilities

Identify which functions are affected by the vulnerability and assess their usage within your application.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Details** and look for **Vulnerable functions**.

### Further reading

To learn more about the risk factors, see [Concepts: Risk factors](/docs/secure/vulnerabilities/concepts#assessment "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Prioritize by related and affected entities

Identify whatâs at risk by examining the entities connected to each vulnerability. See below for your options.

### Review related and affected process groups or Kubernetes nodes

Understand how a vulnerability affects process groups or Kubernetes nodesâsee how many are affected, resolved, or muted, and what percentage they represent. Track remediation progress, exposure level, and overall impact.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Affected entities** and look for **Process group overview** or **Kubernetes node overview**.

### Review other related entities

Explore entities connected to affected process groups or Kubernetes nodes to uncover indirect exposure, trace root causes, and assess the broader impact of vulnerabilities. Open these entities in compatible apps to investigate further and take targeted action.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Related entities**.

### Further reading

To learn more about affected and related entities, see [Concepts: Affected and related entities](/docs/secure/vulnerabilities/concepts#entities "Concepts that are specific to the Dynatrace Vulnerabilities app.").

## Prioritize by exploit attempts

Code-level vulnerabilities

Prioritize vulnerabilities based on observed exploit activity to better understand exposure and response patterns. View how frequently a vulnerability has been targeted, what actions were taken in response, and key details from recent attempts to help guide your remediation efforts. Adjust [timeframe](/docs/secure/vulnerabilities/manage-results#timeframe "Filter, format, and sort to find relevant vulnerability information.") and [segments](/docs/secure/vulnerabilities/manage-results#segments "Filter, format, and sort to find relevant vulnerability information.") and open exploits in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.") for further insights.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Exploit attempts**.

To detect exploit attempts you need to [set up Runtime Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.").

## Prioritize by vulnerability evolution

Track vulnerability evolution to understand severity changes over time and prioritize response accordingly.

Historical context helps clarify whether a vulnerability has always been critical or recently escalated. For example, if a `Medium` severity issue becomes `Critical`, you'll know it wasn't neglectedâit simply evolved and now demands attention. Without this timeline, a newly critical vulnerability might appear to have been overlooked for longer than it actually has.

1. On the **Prioritization** page, select a vulnerability.
2. In the side panel, go to **Vulnerability evolution**.

Events are stored for one year and can only be queried up to the timestamp of when the vulnerability was first detected.

## Prioritize by CISA KEV catalog

Third-party vulnerabilities

Leverage the [CISA KEV catalogï»¿](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) to prioritize vulnerabilities based on known exploit activity and remediation deadlinesâso you can focus on threats with real-world impact and regulatory urgency. See below for your options.

### Filter by CISA KEV

On the **Prioritization** page, use the [filter](/docs/secure/vulnerabilities/manage-results#filter "Filter, format, and sort to find relevant vulnerability information.") field to

* Show whether a vulnerability appears in the CISA KEV catalog (`CISA KEV` > `CISA KEV - In catalog` > `Yes`/`No`)
* View when a CISA KEV-listed vulnerability is due (`CISA KEV` > `CISA KEV - Due date`, then enter the target date, in `YYYY-MM-DD` format)

### Sort by CISA KEV

1. On the **Prioritization** page, go to the column settings ![Column](https://dt-cdn.net/images/column-settings-dfb41f159c.svg "Column") and select `CISA KEV` to add the **CISA KEV** column to the results table.
2. Select the **CISA KEV** column header, then select **Sort ascending** or **Sort descending**.

### Understand remediation deadlines

Vulnerabilities with missed remediation deadlines are labeled **Overdue**.

For GCP deployments, data may lag behind the CISA KEV catalog by approximately two to four weeks.

## Prioritize by coverage

Coverage of library vulnerabilities shows how well your environment's processes and hosts are monitored by Runtime Vulnerability Analytics (RVA). By reviewing coverage, you can identify monitoring gaps, understand which entities are most affected in runtime, and track exposure trends over time. This context helps you prioritize remediation where it matters most.

For details, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").


---
