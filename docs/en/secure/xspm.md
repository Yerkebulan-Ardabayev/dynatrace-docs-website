---
title: Security Posture Management
source: https://www.dynatrace.com/docs/secure/xspm
scraped: 2026-02-17T04:56:49.671867
---

# Security Posture Management

# Security Posture Management

* Latest Dynatrace
* App
* Updated on Jan 13, 2026

About the app

### What you'll learn

* Review the Security Posture Management coverage of your systems at a glance.
* Search for relevant information to resolve security and compliance findings efficiently.
* Drill into results for insights on how to fix misconfigurations and noncompliance.
* Convert results into a DQL query or download them as CSV and share them with others.

### Target audience

![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** is dedicated to Security Ops Engineers, DevOps, DevSecOps, and Site Reliability Engineers (SREs).

Key use cases include:

* Gaining immediate insight into the overall security posture of your monitored environment
* Detecting and addressing security issues and misconfigurations easily
* Receiving actionable guidance for findings
* Ensuring your environment is configured securely and efficiently
* Enhancing the overall system reliability
* Maintaining continuous compliance with security standards

Prerequisites

* Review the [supported compliance standards and technologies](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").
* To take full advantage of the [Security Posture Management functionality](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards."), you need to [deploy Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.").
* Permissions: For a list of permissions required, go to  **Hub**, select ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**, and display **Technical information**.
* Prior knowledge: Understand Kubernetes.

## Get started

![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** is designed to empower organizations with visibility, control, and compliance over their environment. It provides a high-level report on the compliance posture across the selected compliance standards.

![The Overview page shows a high-level information about the security compliance state in your environment.](https://dt-cdn.net/images/overview-4008-06620e65ce.png)![The Assessment results page provides a compliance view of all evaluated rules from the supported security standards. The available filters allow for a quick selection based on environment, result state, severity, and others.](https://dt-cdn.net/images/assessment-4008-8563f10902.png)![Assessed resources from your environment are marked as 'Passed' when no misconfigurations are discovered in the context of a given rule.](https://dt-cdn.net/images/passed-rules-4008-eccb9b527d.png)![Assessed resources from your environment are marked as 'Failed' when misconfigurations are discovered in the context of a given rule. The Rule assessment section contains details about the relevant configuration properties.](https://dt-cdn.net/images/failed-rules-4008-e7eb504699.png)

1 of 4

To get started, follow the steps below.

### 1. Install app

1. In Dynatrace, open  [**Hub**](/docs/manage/hub "See the information about Dynatrace Hub.").
2. Look for ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** and select **Install**.

### 2. Configure SPM coverage

Optional

You can configure which of your systems (or clusters, in the case of [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")) monitored by Dynatrace is covered by [Security Posture Management](/docs/secure/application-security/security-posture-management-hub "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

1. Open ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**.
2. On the **Overview** page, in the **My systems** table, enable or disable the desired systems.

   Systems that aren't covered by Security Posture Management are labeled `Not enabled`.

   Enable systems

   Disable systems

   To enable coverage for a system

   1. For the desired system, select **Enable SPM**.
   2. On the **Settings** page that opens, turn on **Enable Security Posture Management**.

   To disable coverage for a system

   1. For the desired system, select **Settings** .
   2. On the **Settings** page that opens, turn off **Enable Security Posture Management**.

### 3. Configure assessment scope

Optional

Kubernetes Security Posture Management (KSPM)

The **CIS** standard is enabled by default in the assessment of your Kubernetes environment and cannot be disabled.
However, you can configure which of the other supported compliance standards (**DORA**, **NIST**, and **DISA STIG**) are to be included in future assessments.

To configure the assessment scope

1. Open the  settings menu on the upper-right corner of ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**.
2. Enable or disable the desired standards.

Alternatively, you can enable or disable standards directly from ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings**:

1. Go to **Settings** > **Analyze and alert** > **Application Security** > **Security Posture Management**.
2. Enable or disable the desired standards.

Dynatrace assesses data received from your systems and searches for misconfigurations against the [supported compliance standards](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards."). Results are reported in the app.

Try ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** and [share your feedbackï»¿](https://dt-url.net/1m03u6q) to help us improve.

## Learning modules

[01Security Posture Management concepts

* Explanation
* Concepts that are specific to the Dynatrace Security Posture Management app.](/docs/secure/xspm/concepts)[02Assess coverage

* How-to guide
* Review the Security Posture Management coverage of your systems at a glance.](/docs/secure/xspm/assess-coverage)[03Review findings

* How-to guide
* Search for relevant information to analyze security and compliance findings efficiently.](/docs/secure/xspm/review-findings)[04Gain insights

* How-to guide
* Drill into results that can help you fix misconfigurations and noncompliance.](/docs/secure/xspm/gain-insights)[05Collaborate with apps and share findings

* How-to guide
* Interact with other apps for further insights and share results with stakeholders.](/docs/secure/xspm/share-findings)

Use cases

FAQ

Related blogs

[Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.")

For a list of frequently asked questions regarding Security Posture Management, see [FAQ](/docs/secure/application-security/security-posture-management-hub#faq "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

* [Kubernetes security essentials: Container misconfigurations â From theory to exploitationï»¿](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADRï»¿](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Which IT security solution is right for your organization? CSPM vs. KSPM vs. CNAPPï»¿](https://dt-url.net/az03zj0)
* [Extend the Dynatrace platform with CSPM and VSPMï»¿](https://www.dynatrace.com/news/blog/extend-the-dynatrace-platform-with-cspm-and-vspm/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protectionï»¿](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [What is Kubernetes security posture management? Driving business security with KSPMï»¿](https://www.dynatrace.com/news/blog/kubernetes-security-posture-management-kspm/)
* [Empowering SREs with runtime vulnerability analytics and security posture managementï»¿](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace KSPM: Transforming Kubernetes security and complianceï»¿](https://www.dynatrace.com/news/blog/dynatrace-kspm-transforming-kubernetes-security-and-compliance/)
* [Dynatrace Cloud Security Posture Management elevates cloud security with real-time compliance across hyperscalersï»¿](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/)

## Related topics

* [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.")