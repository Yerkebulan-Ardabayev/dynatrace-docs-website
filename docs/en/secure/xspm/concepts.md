---
title: Security Posture Management concepts
source: https://www.dynatrace.com/docs/secure/xspm/concepts
scraped: 2026-02-25T21:34:04.542694
---

# Security Posture Management concepts

# Security Posture Management concepts

* Latest Dynatrace
* Explanation
* Updated on Sep 23, 2025

## Results

**Results** are findings from Dynatrace in relation to your security and compliance posture, based on the rules of the [supported compliance standards](/docs/secure/application-security/spm#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

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

Results are displayed for all your monitored systems on which [Security Posture Management](/docs/secure/application-security/spm "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") is enabled.

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