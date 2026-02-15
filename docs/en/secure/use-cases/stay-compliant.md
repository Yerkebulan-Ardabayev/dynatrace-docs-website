---
title: Stay compliant with Security Posture Management
source: https://www.dynatrace.com/docs/secure/use-cases/stay-compliant
scraped: 2026-02-15T21:24:42.657302
---

# Stay compliant with Security Posture Management

# Stay compliant with Security Posture Management

* Latest Dynatrace
* Tutorial
* Published Dec 02, 2024

Early Adopter

In this tutorial you will learn how [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.") can help you stay compliant with the [security hardening guidelines and regulatory compliance standards](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

## Target audience

This tutorial is dedicated to Security Ops Engineers, DevOps, DevSecOps, and Site Reliability Engineers (SREs).

## Scenario

* Your organization requires following Industry best practices or regulatory requirements.
* New workloads are constantly added or removed from your environment.

## Goal

* Gain immediate insight into the overall security posture of your monitored environment.
* Detect and address security issues and misconfigurations easily.
* Ensure your environment is configured securely and efficiently.
* Enhance the overall system reliability.
* Stay compliant with security standards.

## Result

* Kubernetes clusters are actively assessed through Kubernetes Security Posture Management against regulatory compliance standards and security best practices.
* Misconfigurations and violations against standards are continuously discovered.

## Prerequisites

* [Deploy Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")
* Install ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**

  1. Show me how

  1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
  2. Look for ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** and select **Install**.

## Get started

1. Review results

Open [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.") ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") and review

* The [Assessment results](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.")
* The compliance status

  + [For the whole environment](/docs/secure/xspm/assess-coverage#standards "Review the Security Posture Management coverage of your systems at a glance.")
  + [For specific systems](/docs/secure/xspm/assess-coverage#systems "Review the Security Posture Management coverage of your systems at a glance.")

2. Search for relevant information

Use the [filtering and sorting](/docs/secure/xspm/review-findings "Search for relevant information to analyze security and compliance findings efficiently.") options to gather insights about problems in your environment.

3. Gather insights

Define which rules are relevant [based on contextual insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").

4. Define compliance strategy

1. Fix configuration issues for [rules with the highest priority](/docs/secure/xspm/concepts#concept-severity "Concepts that are specific to the Dynatrace Security Posture Management app.") in a narrow context (for example, on a single cluster).
2. Monitor compliance and operation for a while.
3. If everything works fine, roll out the fix to other environments.

5. Define monitoring for compliance

There are two ways:

In the app

Via DQL queries

Use ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** to monitor that

1. The [compliance standard percentage](/docs/secure/xspm/assess-coverage#standards "Review the Security Posture Management coverage of your systems at a glance.") is increasing.
2. The total number of assessed resources with the `Passed` result is increasing.

For easy management and to compare results, you can [download results as a CSV file](/docs/secure/xspm/share-findings#dwld "Interact with other apps for further insights and share results with stakeholders.").

Use [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") to monitor

1. The history of results per standard or rule, per cluster or environment.
2. That the resource assessment result for a specific set of rules remains `Passed`.

   For a list of DQL examples based on compliance events that you can use, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

6. Create notifications

[Create a workflow](/docs/analyze-explore-automate/workflows/actions "Use Dynatrace ready-made actions for your workflows and integrate Dynatrace with third-party systems.") to send an alert on your desired channel if the previously `Passed` rule turns into `Failed`.

## Further resources

[Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.")

[Security Posture Management](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")

## Related topics

* [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.")