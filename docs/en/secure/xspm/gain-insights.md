---
title: Gain insights
source: https://www.dynatrace.com/docs/secure/xspm/gain-insights
scraped: 2026-02-25T21:32:37.456271
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