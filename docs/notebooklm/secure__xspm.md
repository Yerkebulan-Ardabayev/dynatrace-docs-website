# Dynatrace Documentation: secure/xspm

Generated: 2026-02-16

Files combined: 5

---


## Source: assess-coverage.md


---
title: Assess coverage
source: https://www.dynatrace.com/docs/secure/xspm/assess-coverage
scraped: 2026-02-16T09:39:10.473294
---

# Assess coverage

# Assess coverage

* Latest Dynatrace
* How-to guide
* Updated on Jan 13, 2026

The following options to assess coverage are available.

## Review system coverage

On the **Overview** page, the **System coverage** donut chart helps you determine the percentage of monitored systems on which [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") is enabled.

![system coverage](https://dt-cdn.net/images/2024-11-08-08-15-45-387-114cb209db.png)

Enabling Security Posture Management on your systems allows you to view results in the app and take full advantage of its [capabilities](/docs/secure/xspm#about "Detect, manage, and take action on security and compliance findings.").

If you later on disable Security Posture Management on your system, you keep the access to previously created assessment results and you can query for [compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.") from that system in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") and [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

### Improve system coverage

To improve [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") coverage on your systems

1. On the **Overview** page, in the **My systems** table, search for systems labeled `Not enabled`.
2. For each system you want to cover, select **Enable SPM**.
3. On the **Settings** page that opens, turn on **Enable Security Posture Management**.

## Review compliance status per environment

On the **Overview** page, the compliance standard cards help you determine your compliance status per environment for each [supported compliance standard](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards."). You can view

* The percentage of passed rules
* The total number of rules and how many of them are [passed, manual, and failed](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.")
* The number of rules by [severity](/docs/secure/xspm/concepts#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.") (critical, high, medium, and low)

![compliance status](https://dt-cdn.net/images/2024-11-04-21-06-16-1477-6f03aab3d1.png)

Select a card to navigate to the **Assessment results** page and view results filtered by the respective standard.

### Improve compliance coverage

Kubernetes Security Posture Management (KSPM)

You can improve compliance coverage for each environment by enabling the relevant standards.

1. Open the  settings menu on the upper-right corner of ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**.
2. On the **Settings** page that opens, enable the desired standards.

   The CIS standard is enabled by default and can't be disabled.

Alternatively, you can enable standards directly from **Settings**.

1. Go to **Settings** > **Analyze and alert** > **Application Security** > **Security Posture Management**.
2. Enable the desired standards.

Any configuration changes take effect after the next compliance analysis.

## Review compliance status per system

On the **Overview** page, the **My systems** table helps you review the results and compliance status for each of your monitored systems. You can view

* The total number of [failed, manual, and passed rules](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.")
* The total number of failed rules based on [severity](/docs/secure/xspm/concepts#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.")
* The compliance status
* The time when the latest assessment was completed

![system list](https://dt-cdn.net/images/2024-11-04-22-02-43-1839-4166f65292.png)

Select a system to navigate to the **Assessment results** page and view results filtered by that system. If a system has [no results](#no-results), navigation isn't possible.

## FAQ

### Why are there no results for my system?

See below for the potential reasons why, on the **Overview** page, in **My systems** table, there are no results displayed for a system.

* Security Posture Management isn't enabled on that system. In this case, the system is labeled `Not enabled`. Select **Enable SPM** to navigate to the Settings page of that system and enable Security Posture Management.

* The initial assessment is still in progress. In this case, the system is labeled `No data`. Please allow around one hour for the assessment to finish. For details of the assessment mechanism, see [How it works](/docs/secure/application-security/security-posture-management-hub#mechanism "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")


---


## Source: concepts.md


---
title: Security Posture Management concepts
source: https://www.dynatrace.com/docs/secure/xspm/concepts
scraped: 2026-02-16T09:27:32.979457
---

# Security Posture Management concepts

# Security Posture Management concepts

* Latest Dynatrace
* Explanation
* Updated on Sep 23, 2025

## Results

**Results** are findings from Dynatrace in relation to your security and compliance posture, based on the rules of the [supported compliance standards](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

**Rules** are specific configuration and other process requirements defined in the compliance standards.

Results consist of

* Rules that were assessed automatically (labeled `Failed`, `Passed`, and `Not relevant`)
* Rules that couldn't be assessed automatically (labeled `Manual`)

Learn below about each result type.

| **Result type** | **Definition** |
| --- | --- |
| Failed | The assessed resource doesn't follow the recommendations specified in the rule. In this case, a reason for failure is provided, based on which you can fix the issue. For details, see [Gain insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance."). |
| Passed | The assessed resource follows the recommendations specified in the rule (there are no misconfigurations violating the specified recommendations). |
| Manual[1](#fn-1-1-def) | The resource cannot be automatically assessed, as Dynatrace can't determine whether the resource is compliant (for example, when, due to physical security, Dynatrace can't get the configuration data from the clusters and nodes). |
| Not relevant | The assessed resource doesn't meet a specific criteria for assessment, such as a specific version. These results can be skipped. |

1

Manual results aren't currently actionable.

To increase the number of results based on automatic assessment, we recommend that you [deploy Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.").

### View

Results are displayed for all your monitored systems on which [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") is enabled.

* The **Overview** page shows the total number of failed, manual, and passed rules per monitored system.
* The **Assessment results** page shows a table with all results, sorted automatically in descending order, starting from the ones deserving the most attention (failed rules with critical severity) to those less important (not relevant rules with low severity).

See below the result calculation based on the aggregation of finding events into rules.

| **Rule result** | **Aggregation of resource states** |
| --- | --- |
| Failed | At least one assessed resource has a `Failed` result. |
| Passed | At least one assessed resource has a `Passed` result, but none `Failed` nor `Manual`. |
| Manual | At least one assessed resource has a `Manual` result, but none `Failed`. |
| Not relevant | All assessed resources have a `Not relevant` result. |

### Categorize assessment results

You can filter and sort results based on different criteria of interest. For details, see [Review findings](/docs/secure/xspm/review-findings "Search for relevant information to analyze security and compliance findings efficiently.").

### Explore

To view result details

1. Go to the **Assessment results** page.
2. Select a rule.

   This opens a side window with more information that can help you understand the context and fix potential issues. For details, see [Gain insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").

## Severity

Information regarding severity is provided by the compliance standards and mapped to Dynatrace as `Critical`, `High`, `Medium`, and `Low`, following the compliance standard recommendations.

### View

* The **Overview** page shows

  + The total number of rules per compliance standard and how many of them are passed, manual, and failed (see the compliance standard cards)
  + The total number of failed rules per system based on severity (see **My systems** table)
* The **Assessment results** page shows a table with all results and the associated severity, sorted automatically in descending order, starting from the ones deserving the most attention (failed rules with critical severity) to those less important (not relevant rules with low severity).

### Categorize assessment results

You can filter and sort results based on severity. For details, see [Review findings](/docs/secure/xspm/review-findings "Search for relevant information to analyze security and compliance findings efficiently.").


---


## Source: gain-insights.md


---
title: Gain insights
source: https://www.dynatrace.com/docs/secure/xspm/gain-insights
scraped: 2026-02-16T09:35:37.484000
---

# Gain insights

# Gain insights

* Latest Dynatrace
* How-to guide
* Updated on Jan 28, 2026

On the **Assessment results** page, selecting a rule opens a side window that enables you to:

**Review key information:**

* [The rule](#rule)
* [Related system resources](#resources)
* [Resource configuration](#configuration)

**Initiate deeper analysis:**

* [Explain assessment](#explain)

This context can help you fix issues on your system.

## Insights about the rule

On the **Rule details** tab, you can

* View relevant details about the rule such as

  + Rule version used for assessment
  + Rule severity
  + Compliance standard issuing the rule
* Navigate to the original documentation resource for the full description of the rule

  ![Insights about the rule](https://dt-cdn.net/images/2024-11-17-18-05-08-896-899014266d.png)

## Insights about resources

On the **Assessed resources** tab, you can examine the resources that must comply to the rule. This can help you identify the resources affected by a compliance violation or by security relevant misconfiguration.

Assessed resources with `Not relevant` status are filtered out by default.

You can

* View the system on which the rule applies together with all the system resources
* Use the filter bar to filter for resources that

  + Require your attention (`Failed`)
  + Are compliant (`Passed`)
  + Can't be automatically assessed (`Manual`)
  + Don't meet a specific criteria for the rule assessment (`Not relevant`)
* Use the search bar to search for a specific resource (full or partial match)
* Hover over the system chart bar to see the compliance status of the system resources

  ![compliance node status](https://dt-cdn.net/images/2024-11-13-06-06-14-471-e22dd6056b.png)
* Identify the resource type and last assessment date in **Rule assessment** > **Resource**

  ![resource type](https://dt-cdn.net/images/2024-11-17-18-13-15-537-4dcd8fcd4b.png)

## Insights about configuration

On the **Assessed resources** tab, go to **Rule assessment** > **Relevant configuration properties** for information about resource configuration.

This can help you identify the current misconfiguration for a selected resource that is contributing to a rule violation.

* **Example**: A `Failed` rule `1.2.19 Ensure that the --audit-log-maxsize argument is set to 100 or as appropriate` reports that a node on the control plane doesn't have `--audit-log-maxsize` configured. This means that, in case security investigation would be needed, it's not guaranteed that there will be enough logs to carry out investigation due to this misconfiguration.

  ![rule example 1](https://dt-cdn.net/images/2024-11-17-18-32-42-446-e03c9462e5.png)

For `Manual` rules, where automatic assessment isn't possible, hints are provided about what information is needed to complete the assessment.

For details about `manual` rules, see [Results](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.").

* **Example**: A `Manual` rule `The Kubernetes kubelet staticPodPath must not enable static pods` reports that Dynatrace can't check configuration because Kubernetes Node Configuration Collector is missing.

  ![ncc missing example](https://dt-cdn.net/images/2024-11-17-19-11-42-473-231173eb9b.png)

## Explain assessment

To use this generative AI feature, make sure:

* Dynatrace Intelligence generative AI is enabled for your environment. See [Enable Dynatrace Intelligence generative AI](/docs/dynatrace-intelligence/copilot/copilot-getting-started#enable-davis-copilot "Learn how to set up Dynatrace Intelligence generative AI.").
* You have permission to use it. See [User permissions](/docs/dynatrace-intelligence/copilot/copilot-getting-started#davis-copilot-user-permissions "Learn how to set up Dynatrace Intelligence generative AI.").

Dynatrace Intelligence generative AI can provide contextual, plain-language explanations of rule assessments to accelerate understanding and remediation.

To access the functionality

1. In [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings."), on the **Assessment results** page, select a rule.
2. On the **Assessed resources** tab, select  **Explain assessment**.

When selected, Dynatrace Intelligence generative AI analyzes the technical details of a rule assessment and generates a structured summary that may include:

* **What the assessment means**: Explains the compliance rule (for example, CIS Kubernetes Benchmark requirements) and its purpose in securing environments.
* **Why it matters**: Highlights severity levels and priority, and describes potential implications such as misconfigurations leading to unauthorized access, privilege escalation, or cluster compromise.
* **How to remediate**: Where applicable, recommends remediation steps such as updating file permissions, applying configuration fixes, restarting services, or enabling continuous monitoring across clusters and cloud accounts.

The structure and depth of generative AI's explanation may vary depending on the rule type and available context. While Dynatrace Intelligence generative AI aims to provide detailed insights, not all assessments will include every element listed above.

Dynatrace Intelligence generative AI explanations are tailored to the nature of each rule assessment, providing relevant, actionable insights that accelerate triage and support informed decision-making, even for users without deep security expertise.

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")


---


## Source: review-findings.md


---
title: Review findings
source: https://www.dynatrace.com/docs/secure/xspm/review-findings
scraped: 2026-02-16T21:31:37.992400
---

# Review findings

# Review findings

* Latest Dynatrace
* How-to guide
* Updated on Oct 13, 2025

To efficiently manage and analyze security and compliance findings, you can [filter](#filter) and [sort](#sort) results to prioritize the most relevant findings.

## Filter

Select which information is to be displayed.

### Filter by standard

You have two options:

From Overview

From Assessment results

1. Go to the **Overview** page.
2. From the list of available compliance standard cards, select the one you're interested in. This will navigate you to the **Assessment results** page, filtered by the respective standard.

![filter by standard](https://dt-cdn.net/images/2024-11-10-11-32-31-1491-79379f31bf.png)

1. Go to the **Assessment results** page.
2. In the filter bar, select a **Standard** (short form) and/or a **Standard name** (full name of the standard) to focus your results.

![filter by standard](https://dt-cdn.net/images/2025-10-13-15-28-08-1920-94cd4524a0.png)

### Filter by system

You have two options:

From Overview

From Assessment results

1. Go to the **Overview** page.
2. In the **My systems** table, look for and select the system you're interested in. This will navigate you to the **Assessment results** page, filtered by the respective system.

![filter by system](https://dt-cdn.net/images/2024-11-10-12-06-27-860-9e7c4d01d1.png)

Only systems on which Security Posture Management is enabled can be selected.

1. Go to the **Assessment results** page.
2. In the **System** filter, select the system you're interested in.

   ![filter by system](https://dt-cdn.net/images/2025-10-13-15-34-33-1357-5c705ed4d4.png)

   Only systems on which Security Posture Management is enabled are displayed.
3. Select **Update** next to the systems filter bar to update results based on your selection.

### Filter by assessment view

On the **Assessment results** page, use the **Assessment view** filter to control the scope of displayed rules:

* **Complete results**: Displays all rules assessed for the selected systems, including those marked `Not relevant`.
* **Recommended**: Displays only the results which are relevant to your environment: `Failed`, `Manual`, or `Passed`.

![assessment view filter](https://dt-cdn.net/images/2025-10-13-14-37-49-1920-1a11441c0c.png)

### Filter by results, severity and rule

On the **Assessment results** page, filter for the options you're interested in:

* [Result](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.") (`Failed`, `Manual`, `Passed`, `Not relevant`)
* [Severity](/docs/secure/xspm/concepts#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.") (`Critical`, `High`, `Medium`, `Low`)
* Rule (full or partial match of the rule name)

Filters can be combined.

![combined filters](https://dt-cdn.net/images/2025-10-13-15-38-12-1920-a0e9d073f1.png)

## Sort

On the **Overview** and the **Assessment results** pages, select any of the columns with a sorter symbol  to change the order of results to ascending or descending based on that criteria.

![sorting](https://dt-cdn.net/images/2024-11-10-11-16-35-579-3bd762be27.png)

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")


---


## Source: share-findings.md


---
title: Collaborate with apps and share findings
source: https://www.dynatrace.com/docs/secure/xspm/share-findings
scraped: 2026-02-15T21:27:41.500681
---

# Collaborate with apps and share findings

# Collaborate with apps and share findings

* Latest Dynatrace
* How-to guide
* Updated on Sep 23, 2025

Dynatrace offers you the flexibility to

* Interact with other apps: You can either [convert results into DQL queries](#dql) or [run DQL queries for compliance events in your favorite app](#run)
* Share insights with stakeholders: You can [share the results URL](#url) or [download results as a CSV file](#dwld)

See below for details.

## Convert results into DQL queries

You can convert app results into [DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") and open them in other Dynatrace apps to continue investigation from there.

1. On the **Assessment results** page, select a rule.
2. In **Assessed resources**, you have two options:

   * **Option 1**: Select **Open in Notebooks** to open a new document in ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**
   * **Option 2**: In the  menu, select  **Open with** and select an app from the available options

     ![open with](https://dt-cdn.net/images/2025-02-12-17-23-12-511-fac7e1d101.png)

## Run DQL queries for compliance events

You can run [DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.") for [compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.") in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") for further insights or to share results with others.

* For guidance on how to use DQL, see [How to use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.").
* For a list of DQL query examples based on compliance events, see [DQL examples for security data](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").
* For a list of compliance event fields mapped to Grail, see [Dynatrace Semantic Dictionary](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.").

## Share URL

You can forward the URL of your filtered results or specific rules to team members.

To view results, users need to have the required permissions enabled. For details, see [Prerequisites](/docs/secure/xspm#prereq "Detect, manage, and take action on security and compliance findings.").

## Download as CSV

You can download results as a CSV file to share it with others.

1. On the **Assessment results** page, use the filter bar to select which results you want to display.
2. On the upper-right of the vulnerabilities table, select  > **Download as CSV** > **All**.

   ![download as csv](https://dt-cdn.net/images/2024-11-17-12-40-34-1865-7ac81cfa63.png)

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")


---
