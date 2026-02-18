---
title: Address remediation
source: https://www.dynatrace.com/docs/secure/vulnerabilities/address-remediation
scraped: 2026-02-18T21:33:23.794684
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