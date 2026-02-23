---
title: Assess coverage
source: https://www.dynatrace.com/docs/secure/vulnerabilities/assess-coverage
scraped: 2026-02-23T21:34:48.461622
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