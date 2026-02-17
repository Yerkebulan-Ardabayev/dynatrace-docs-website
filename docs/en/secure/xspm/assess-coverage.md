---
title: Assess coverage
source: https://www.dynatrace.com/docs/secure/xspm/assess-coverage
scraped: 2026-02-17T21:29:07.120978
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