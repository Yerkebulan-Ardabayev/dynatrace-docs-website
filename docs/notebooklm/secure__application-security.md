# Dynatrace Documentation: secure/application-security

Generated: 2026-02-16

Files combined: 18

---


## Source: application-protection-rules.md


---
title: Runtime Application Protection monitoring rules
source: https://www.dynatrace.com/docs/secure/application-security/application-protection/application-protection-rules
scraped: 2026-02-15T21:26:50.425428
---

# Runtime Application Protection monitoring rules

# Runtime Application Protection monitoring rules

* Latest Dynatrace
* How-to guide
* Updated on Jul 25, 2025

Dynatrace Runtime Application Protection rules allow you to

* [Set up fine-grained monitoring rules to block, monitor, or ignore future attacks](#handling-rules), based on [resource attributes](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."), and define multiple conditions for one rule. When creating a rule, you can check if conditions apply and how many process groups are affected.
  The rules you create override the global attack control settings for the selected technology.
* [Add attacks that you don't consider harmful to the allowlist](#exception-rules), by source IPs or attack patterns.

## Define specific attack control rules

To create an attack rule

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New)**.
2. On the **Monitoring rules** tab, select  **Add new rule**.
3. Define the rule:

   * **Rule name**: The name under which your rule will be listed.
   * **Attack control**: Specify how to control an attack that matches the rule criteria:

     + `Off; incoming attacks NOT detected or blocked.`
     + `Monitor; incoming attacks detected only.`
     + `Block; incoming attacks detected and blocked.`
   * **Attack type**: Select the attack type to which current configuration applies.
   * Optional **Specify where the rule is applied**: If you want the rule to apply only to a subset of your environment, select  **Add condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").
4. Select **Create**.
5. Restart processes.

You can edit, disable, enable, or remove rules at any time.

## Define exception (allowlist) rules

Based on specific criteria, you can create an exception monitoring rule for the attack.

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New)**.
2. On the **Allowlist rules** tab, select  **Add new rule**.
3. Define the exception rule:

   * **Attack control**: Select one of the options below:

     + `Off; incoming attacks NOT detected or blocked` to ignore the attacks based on the subsequently defined criteria
     + `Monitor; incoming attacks detected only` to monitor the attacks based on the subsequently defined criteria, but not block them
   * **Define the rule**: Select  **Add condition** to set up fine-grain conditions that need to be met to allow an attack.

     Most key/matcher combinations available in the drop-down list require OneAgent version 1.309+.

     For OneAgent versions earlier than 1.309, the only available options are:

     + key: `entry_point.payload`, matcher: `contains`
     + key: `actor.ip`, matcher: `is part of IP CIDR`

     To fully benefit from this functionality, make sure you're using the latest OneAgent version.
   * Optional **Specify where the rule is applied**: If you want the rule to apply only to a subset of your environment, select  **Add condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").
4. Select **Create**.

You can edit, disable, enable, or remove rules at any time.

## FAQ

* [How does Dynatrace actually block attacks?](/docs/secure/faq#block-attacks "Frequently asked questions about Dynatrace Application Security.")
* [How is an attacker's IP determined?](/docs/secure/faq#attacker "Frequently asked questions about Dynatrace Application Security.")

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: application-protection.md


---
title: Runtime Application Protection
source: https://www.dynatrace.com/docs/secure/application-security/application-protection
scraped: 2026-02-15T21:13:25.969512
---

# Runtime Application Protection

# Runtime Application Protection

* Latest Dynatrace
* How-to guide
* Updated on Nov 03, 2025

Dynatrace Runtime Application Protection leverages code-level insights and transaction analysis to detect and block exploitation attempts on your applications automatically and in real time.

## Capabilities

* Detection of SQL injection, JNDI injection, command injection, and SSRF attacks
* Code-level visibility provided by OneAgent
* Production-ready performance footprint
* Configurable automatic blocking of detected attacks
* Protection of web applications and APIs
* High alert precision with rich context to optimize your team's performance and make every minute count

## How it works

[Runtime Application Protection (RAP)](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.") uses runtime instrumentation to detect and optionally block exploit attempts. When your application receives a web request, [Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") tracks user input and analyzes how it interacts with sensitive code paths, such as SQL queries, OS commands, or JNDI lookups. If the behavior matches a known attack pattern, Dynatrace reports it as a security finding. If attack blocking is enabled, OneAgent throws an exception to stop the malicious request before it executes. RAP is lightweight and safe for use in production environments.

## Prerequisites

Before you begin, ensure your environment meets the necessary requirements:

* You're using a supported version of Dynatrace. Review the [release notes](/docs/whats-new "Read the product news and the release notes and find out which Documentation topics are new.") for currently supported versions.
* For Runtime Application Protection to work properly, make sure deep monitoring is enabled in **Settings** > **Processes and containers** > **Process group monitoring**.

  For .NET, Go, and Python technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Supported technologies

Dynatrace detects SQL injection, JNDI injection, command injection, and SSRF attacks in the following technologies.

| Technology | Minimum OneAgent version | SQL injection | Command injection | JNDI injection | SSRF |
| --- | --- | --- | --- | --- | --- |
| Java 8 or higher[1](#fn-1-1-def) | 1.241 |  |  |  |  |
| .NET[2](#fn-1-2-def)'[3](#fn-1-3-def) | 1.289 |  |  |  |  |
| Go[3](#fn-1-3-def) | 1.311 |  |  |  |  |

1

Only supported on Windows x86 and Linux x86 systems.

2

Only .NET Framework 4.5, .NET Core 3.0 or higher, and 64-bit processes are supported.

3

For .NET and Go technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Get started

To set up Runtime Application Protection, follow the instructions below.

To use preview features, please contact a Dynatrace product expert via live chat to **activate Runtime Application Protection** before continuing.

Enable Runtime Application Protection

To enable Runtime Application Protection globally on your environment

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New**).
2. Enable Runtime Application Protection.
3. Select **Enable**.
4. Restart your processes.

Define the global attack control

To define the global attack control for all process groups

1. Go to **Settings (New)** > **Analyze and alert** > **Application security** > **Application protection (New)** > **Monitoring rules** > **Default rules**.
2. Edit the attack control per technology:

* **Off; incoming attacks NOT detected or blocked.**âMonitoring is disabled; no attacks in the selected technology are reported.
* **Monitor; incoming attacks detected only.**âMonitoring is enabled; no attacks in the selected technology are blocked.
* **Block; incoming attacks detected and blocked.**âMonitoring is enabled; attacks in the selected technology are blocked at runtime.

If you define [custom monitoring rules](/docs/secure/application-security/application-protection/application-protection-rules#handling-rules "Create, modify, and delete rules for specific attacks.") based on certain process groups or vulnerability types, the custom rules override the global attack control for the selected technology, and Runtime Application Protection continues to monitor the attacks based on your rules.

3. Select **Save**.
4. Restart your processes.

Enable OneAgent monitoring

1. Go to **Settings (New)** and select **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Filter by `code-level attack evaluation` and enable the feature for the technologies you want to monitor.
3. Select **Save changes**.
4. Restart your processes.

OneAgent version 1.309 To detect SSRF attacks, you also need to enable SSRF attack evaluation. See below for instructions.

1. Go to **Settings (New)** and select **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Find and enable `Java SSRF code-level vulnerability and attack evaluation`.
3. Select **Save changes**.
4. Restart your processes.

## What's next

After you set up Runtime Application Protection, you can

* Evaluate, triage, and investigate findings with [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.").
* [Set up Runtime Application Protection monitoring rules](/docs/secure/application-security/application-protection/application-protection-rules "Create, modify, and delete rules for specific attacks.").

## Consumption

Runtime Application Protection is licensed based on the consumption of [GiB-hours](/docs/license/capabilities/application-security/runtime-application-protection "Learn how how your consumption of the Runtime Application Protection (RAP) DPS capability is billed and charged.") if you're using the [Dynatrace Platform Subscription (DPS) licensing model](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), or [Application Security units (ASUs)](/docs/license/monitoring-consumption-classic/application-security-units "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.") if you're using the [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: security-posture-management-hub.md


---
title: Security Posture Management
source: https://www.dynatrace.com/docs/secure/application-security/security-posture-management-hub
scraped: 2026-02-15T21:13:31.085106
---

# Security Posture Management

# Security Posture Management

* Latest Dynatrace
* How-to guide
* Updated on Jan 13, 2026

Dynatrace Security Posture Management (SPM) enables you to assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.

The following Security Posture Management flavors are available.

* **Dynatrace Kubernetes Security Posture Management (KSPM)**: Enables you to detect, analyze, and monitor misconfigurations, security hardening guidelines, and potential compliance violations across your Kubernetes deployment.
* **Runecast Cloud Security Posture Management (CSPM)**: Provides in-depth insights into the security posture of your cloud environments (AWS, Azure, and GCP).
* **Runecast VMware Security Posture Management (VSPM)**: Provides in-depth insights into the security posture of your VMware environments (vCenter and NSX-T).

## Capabilities

* Automated assessments against [supported compliance standards](#support), allowing you to manage and report on the most critical findings.
* Continuous analysis and evidence creation for internal and external auditing purposes.
* Actionable findings that allow you to

  + Prioritize compliance efforts
  + Create audit evidence and reporting for auditors and internal security and compliance teams

## How it works

Security Posture Management (SPM) continuously evaluates your environment for misconfigurations, policy violations, and compliance risks. Dynatrace collects configuration data from your infrastructure and cloud platforms, streams it into Grail, and normalizes it into security events. These are then evaluated against hardening guidelines and compliance standards. Results update in real time as your environment changes, helping you stay secure and audit-ready.

For a quick walkthrough, see [Dynatrace Cloud Security Posture Management elevates cloud security with real-time compliance across hyperscalersï»¿](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/). For technical details, see [SPM concepts](/docs/secure/xspm/concepts "Concepts that are specific to the Dynatrace Security Posture Management app.").

## Support matrix

A compliance standard groups together security, configuration, and process requirements often following already established ICT Security guidelines and best practices. Adhering to these can help organizations maintain regulatory required levels of security hardening and minimize the risk of exposure across the organization.

These standards are supported either natively or through Dynatrace integration with Runecast Analyzer. Native standards are always kept up to date. Dynatrace Security Posture Management supports the following standards and technologies.

| **Compliance standards** | **Kubernetes[1](#fn-1-1-def)** | **AWS** | **Azure** | **GCP** | **vSphere[2](#fn-1-2-def)** | **NSX-T[3](#fn-1-3-def)** |
| --- | --- | --- | --- | --- | --- | --- |
| [BSI C5](#bsic5) |  |  |  |  |  |  |
| [BSI IT-Grundschutz](#bsi-it) |  |  |  |  |  |  |
| [CIS](#cis) |  |  |  |  |  |  |
| [Cyber Essentials](#cyber) |  |  |  |  |  |  |
| [DISA STIG](#stig) |  |  |  |  |  |  |
| [DORA](#dora) |  |  |  |  |  |  |
| [Essential Eight](#essential) |  |  |  |  |  |  |
| [GDPR](#gdpr) |  |  |  |  |  |  |
| [HIPAA](#hipaa) |  |  |  |  |  |  |
| [ISO 27001](#iso) |  |  |  |  |  |  |
| [KVKK](#kvkk) |  |  |  |  |  |  |
| [NIST](#nist) |  |  |  |  |  |  |
| [PCI DSS](#pci) |  |  |  |  |  |  |
| [TISAX](#tisax) |  |  |  |  |  |  |
| [VMware SCG](#vmware) |  |  |  |  |  |  |

1

Support includes upstream Kubernetes, Amazon EKS, and Azure AKS. Compatibility is limited to x86-64 CPU architectures and requires Kubernetes version according to Dynatrace support lifecycle (unless defined otherwise in the specific standard).

2

Supported versions are VMware ESXi 8.0 v1.1.0, VMware ESXi 7.0 v1.4.0, VMware ESXi 6.7 v1.2.0, and VMware ESXi 6.5 v1.0.0.

3

NSX-T support is limited to version 3.2 and later.

## Compliance standards

BSI C5

C5, also known as the [Cloud Computing Compliance Criteria Catalogueï»¿](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html), developed by the German Federal Office for Information Security (BSI), outlines the basic requirements for secure cloud computing. It's primarily designed to provide a high level of assurance in the security of cloud services. While based on international standards such as ISO 27001, C5 goes further by incorporating additional controls tailored explicitly to cloud environments.

#### BSI C5 version support

Supported version is C5:2020.

BSI IT-Grundschutz

The [German IT Baseline Protection (IT- Grundschutz)ï»¿](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html) standard was established by the German Federal Office for Information Security (BSI) as a sound and sustainable information security management system (ISMS). IT-Grundschutz covers technical, organizational, infrastructural, and personnel aspects equally. With its broad foundation, IT-Grundschutz offers a systematic information security approach compatible with ISO/IEC 27001.

#### BSI IT-Grundschutz version support

Supported editions are 2022 and 2023.

### Center for Internet Security (CIS)

The [Center for Internet Security (CIS)ï»¿](https://dt-url.net/cm03uso) publishes the CIS Critical Security Controls (CSC) to help organizations achieve greater overall cybersecurity defense. These controls are a recommended set of actions for cyber defense that provide specific and actionable ways to stop todayâs most pervasive and dangerous attacks. A principal benefit of the controls is that they prioritize and focus a smaller number of actions with high pay-off results.

#### CIS benchmark support

| **Benchmark** | **Cloud provider/Server software** | **Supported versions** |
| --- | --- | --- |
| CIS Kubernetes v1.12.0 | Upstream Kubernetes | 1.32, 1.33, 1.34 |
| CIS Kubernetes v1.11.1 | Upstream Kubernetes | 1.29, 1.30, 1.31, 1.32 |
| CIS Amazon Elastic Kubernetes Service (EKS) Benchmark v1.7.0 | Amazon EKS | 1.30, 1.31, 1.32 |
| CIS Azure Kubernetes Service (AKS) Benchmark v1.8.0 | Azure AKS | 1.32, 1.33, 1.34 |
| CIS Amazon Web Services Foundations Benchmark v3.0.0 | AWS | â |
| CIS Microsoft Azure Foundations Benchmark v5.0.0 | Azure | â |
| CIS Google Cloud Platform Foundation Benchmark v1.3.0 | GCP | â |
| CIS VMware ESXi 8.0 Benchmark v1.2.0 | VMware | VMware ESXi 8.0 |
| CIS VMware ESXi 7.0 Benchmark v1.4.0 | VMware | VMware ESXi 7.0 |
| CIS VMware ESXi 6.7 Benchmark v1.2.0 | VMware | VMware ESXi 6.7 |
| CIS VMware ESXi 6.5 Benchmark v1.0.0 | VMware | VMware ESXi 6.5 |

Cyber Essentials

Cyber Essentials is a United Kingdom security standard aiming to demonstrate that an organization has implemented minimum cybersecurity protections through annual assessments. It comprises fundamental technical controls to help organizations safeguard against common online security threats. [The Cyber Essentials schemeï»¿](https://www.ncsc.gov.uk/files/Cyber-Essentials-Requirements-for-Infrastructure-v3-1-January-2023.pdf) is a government-backed framework supported by the National Cyber Security Centre (NCSC).

#### Cyber Essentials version support

Supported version for Cyber Essentials: Requirements for IT infrastructure is v3.1.

DISA STIG

[Security Technical Implementation Guides (STIGs)ï»¿](https://dt-url.net/cmc3uif) are based on the standards of the Department of Defense (DoD). DISA STIG guidelines are often used as a baseline in other sectors or segments to ensure compliance with the standards and access to the DoD networks. All organizations must meet the DISA STIG security standards before accessing and operating on DoD networks.

#### DISA STIG support

| **STIG** | **Supported versions** |
| --- | --- |
| Kubernetes STIG - Ver 2, Rel 4 | Upstream Kubernetes, Amazon EKS, Azure AKS |
| VMware vSphere 8.0 STIG | VMware vCenter 8.0.x, VMware ESXi 8.0.x |
| VMware vSphere 7.0 STIG | VMware vCenter 7.0.x, VMware ESXi 7.0.x |
| VMware vSphere 6.7 STIG | VMware vCenter 6.7.x, VMware ESXi 6.7.x |
| VMware vSphere 6.5 STIG | VMware vCenter 6.5.x, VMware ESXi 6.5.x |
| VMware NSX 4.x STIG | NSX 4.x |
| VMware NSX-T Data Center STIG | NSX 3.x |

DORA

[Digital Operational Resilience Act (DORA)ï»¿](https://dt-url.net/xp43uj2) is a major piece of European Union legislation (Regulation (EU) 2022/2554). DORA aims to enhance the resilience of digital operations and protect the integrity of the financial market infrastructure in the European Union. Compliance with DORA is a pathway to creating a more secure and reliable digital environment within financial institutions. The act impacts day-to-day operations, security protocols, and compliance measures. DORA takes effect on January 17, 2025.

Essential Eight

The Essential Eight standard is built on [eight prioritized mitigation strategiesï»¿](https://www.cyber.gov.au/resources-business-and-government/essential-cybersecurity/essential-eight) designed to assist cybersecurity professionals in mitigating incidents caused by various cyber threats. Developed by the Australian Cyber Security Centre (ACSC), it's mandatory for all Australian non-corporate (federal) Commonwealth entities and highly recommended for other business organizations.

GDPR

General Data Protection Regulation (GDPR) is a European privacy law designed to harmonize data protection regulations across the European Union (EU) by establishing a single, binding framework for all EU member states. [**GDPR.eu**ï»¿](https://gdpr.eu/) offers a comprehensive library of resources to assist organizations in achieving GDPR compliance.

HIPAA

The 1996 Health Insurance Portability and Accountability Act (HIPAA) mandated that the Secretary of the U.S. Department of Health and Human Services (HHS) establish regulations aimed at safeguarding the privacy and security of specific health information. In response, HHS introduced the [HIPAA Privacy Rule and the HIPAA Security Ruleï»¿](https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html), which are now widely recognized standards.

#### HIPAA version support

Supported version is 5/2005: rev. 3/2007.

ISO 27001

[ISO 27001ï»¿](https://www.iso.org/standard/27001) is one of the most globally recognized standards, offering a comprehensive Information Security Management Systems (ISMS) framework. It helps organizations align their security practices with international best practices and business, legal, and regulatory requirements. The standard encompasses all aspects of information risk management, from risk assessment to risk treatment, making it an essential tool in today's ever-changing cybersecurity landscape.

#### ISO 27001 version support

Supported version is ISO 27001/2022.

KVKK

The [Personal Data Protection Lawï»¿](https://www.kvkk.gov.tr/en/) (Turkish: KiÅisel Verilerin KorunmasÄ± Kanunu, KVKK) is a Turkish regulation that governs personal data protection and defines the legal obligations of entities and individuals handling personal data. This law ensures compliance with technical requirements for Data Protection, Data Access, and Audit readiness, modeled after the European Unionâs General Data Protection Regulation (GDPR).

NIST

The [National Institute of Standards and Technology (NIST)ï»¿](https://dt-url.net/5p23u79) publishes the NIST SP 800-53, which offers security and privacy controls for information systems and organizations. Per the Office of Management and Budget (OMB), the NIST standards and policies are mandatory for all non-national security systems run by federal agencies in the USA.

#### NIST revision support

| **Revision** | **Cloud provider/Server software** |
| --- | --- |
| SP 800-53 Rev. 5.1.1 | Upstream Kubernetes, Amazon EKS, Azure AKS |
| SP 800-53 Rev. 5 | AWS, Azure |
| SP 800-53 Rev. 5.1 | VMware vSphere |

PCI DSS

[Payment Card Industry Data Security Standard (PCI DSS)ï»¿](https://www.pcisecuritystandards.org/document_library/) is a set of requirements to ensure that companies that process, store, or transmit credit card information operate in a secure environment. Developed to address the increasing risk of data breaches in payment card systems, PCI DSS is crucial for any business accepting, handling, or storing payment card information.

#### PCI DSS version support

Supported version is PCI DSS v4.0.

TISAX

The Trusted Information Security Assessment Exchange (TISAX) is a prominent information security standard in the automotive industry, developed by the German Association of the Automotive Industry (VDA). TISAX requirements are outlined in the [Information Security Assessment (ISA) catalogï»¿](https://enx.com/en-US/TISAX/downloads/), which is managed by the ENX Association. These requirements are based on the international ISO/IEC 27001 standard for information security management, with additional provisions explicitly tailored to the automotive sector.

#### TISAX version support

Supported version is VDA ISA 5.1.

VMware SCG

VMware Security Configuration Guides provides guidance on how to deploy and operate VMware products in a secure manner based on the [VMware Security Configuration Guideï»¿](https://www.vmware.com/solutions/security/hardening-guides).

#### VMware SCG version support

Supported version is vCenter Server 8.0 Update 3.

## Get started

* To get started with Kubernetes Security Posture Management, see [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.").

* To get started with Cloud Security Posture Management and/or VMware Security Posture Management, see [Ingest Runecast Analyzer compliance findings](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").

## What's next

* Once you set up Kubernetes Security Posture Management, you can

  + Detect, manage, and take action on security and compliance findings with [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")
  + Query [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")

    - For a list of DQL examples based on compliance events that you can use for further investigation or reporting, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

  Try ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** and [share your feedbackï»¿](https://dt-url.net/1m03u6q) to help us improve.
* Once you set up CSPM/VSPM, you can

  + Visualize data with our **Security Posture Overview** dashboard. For details, see [Next steps](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer#next "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").
  + Query [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

    - For a list of DQL examples based on compliance events that you can use for further investigation or reporting, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

## Use cases

[Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.")

## FAQ

### How can I check my Kubernetes cluster against security compliance standards?

* To review the compliance status of your cluster, see [Review compliance status per system](/docs/secure/xspm/assess-coverage#systems "Review the Security Posture Management coverage of your systems at a glance.").
* To review findings on your cluster, you can [filter and sort results](/docs/secure/xspm/review-findings "Search for relevant information to analyze security and compliance findings efficiently.").
* For contextual information that can help you fix findings on your cluster, see [Gain insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").

### Can I enable or disable compliance standards?

* For [Dynatrace Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."), you can manage compliance standards in the Dynatrace **Settings**, see [Configure assessment scope](/docs/secure/xspm#configure-assessment "Detect, manage, and take action on security and compliance findings.").
* For Runecast Cloud Security Posture Management (CSPM) and Runecast VMware Security Posture Management (VSPM), adjust standard selection directly in the [Runecast Analyzerï»¿](https://www.dynatrace.com/platform/runecast-analyzer/).

### What can I do with the findings generated by Dynatrace?

For an overview of how to use compliance findings, see [Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### How can I be compliant with the high-severity findings generated by Dynatrace?

For guidelines on how to increase compliance, see [Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### How can I improve Security Posture Management coverage?

For instructions, see [Improve coverage](/docs/secure/xspm/assess-coverage#improve "Review the Security Posture Management coverage of your systems at a glance.").

### Why am I getting failed results on my system?

Resources on your system are assessed as `Failed` (not compliant) according to rules specified in the [supported standards](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

* To better understand resource configuration and review the source of the rule, see [Gain insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").
* To better understand result types, see [Concepts: Results](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.").

### What happens if I don't fix my system based on the findings?

Maintaining your security posture is fundamental to your overall security strategy. Think of it as basic security hygieneâwithout it, all other security measures you implement will be significantly less effective. On the compliance side, not addressing these findings means you won't be able to identify, assess, and fix potential issues that could lead to audit failures.

Manually handling the numerous checks required for audits quickly becomes an overwhelming task, consuming countless hours. With our Security Posture Management solution, this entire process is automated, ensuring both security and compliance are effectively managed.

Ignoring compliance issues presents potential exposure risk or compliance failure risk.

### How to fix the problems detected in my environment?

For guidelines on how to fix findings, see [Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### What environments can be monitored with Security Posture Management?

For a list of supported systems and their versions and distributions, see [Security Posture Management](/docs/secure/application-security/security-posture-management-hub#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

### In what monitoring modes can I deploy Security Posture Management on Kubernetes?

Running Security Posture Management on Kubernetes is entirely independent of OneAgent and thus independent of the [Monitoring modes](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
Analyzed data originates from the Kubernetes API Server and the Kubernetes Node Configuration Collector via ActiveGate.
Therefore, you can use ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** with [Kubernetes Platform Monitoring](/docs/ingest-from/setup-on-k8s/deployment/platform-observability "Deploy Dynatrace Operator for Kubernetes platform monitoring."), where OneAgent isn't deployed.

### How can I set up Security Posture Management for cloud environments?

Set up the Dynatrace [integration with Runecast Analyzer](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").

## Further resources

* [Kubernetes security essentials: Container misconfigurations â From theory to exploitationï»¿](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADRï»¿](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture managementï»¿](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Extend the Dynatrace platform with CSPM and VSPMï»¿](https://www.dynatrace.com/news/blog/extend-the-dynatrace-platform-with-cspm-and-vspm/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protectionï»¿](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [What is Kubernetes security posture management? Driving business security with KSPMï»¿](https://www.dynatrace.com/news/blog/kubernetes-security-posture-management-kspm/)
* [Which IT security solution is right for your organization? CSPM vs. KSPM vs. CNAPPï»¿](https://dt-url.net/az03zj0)
* [Dynatrace KSPM: Transforming Kubernetes security and complianceï»¿](https://www.dynatrace.com/news/blog/dynatrace-kspm-transforming-kubernetes-security-and-compliance/)
* [Dynatrace Cloud Security Posture Management elevates cloud security with real-time compliance across hyperscalersï»¿](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/)

## Related topics

* [Security Posture Management](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")


---


## Source: app-sec-metrics.md


---
title: Metrics Classic for Dynatrace Runtime Vulnerability Analytics
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/app-sec-metrics
scraped: 2026-02-15T21:29:54.069550
---

# Metrics Classic for Dynatrace Runtime Vulnerability Analytics

# Metrics Classic for Dynatrace Runtime Vulnerability Analytics

* Reference
* Updated on Nov 06, 2025

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** and ![Code Level Vulnerabilities](https://dt-cdn.net/images/code-level-vulnerabilities-512-49803cb5cf.png "Code Level Vulnerabilities") **Code-Level Vulnerabilities** apps, which are deprecated. If you're currently using these apps, we recommend transitioning to the unified [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Upgrade to the latest Dynatrace](/docs/platform/upgrade "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.").

## Available metrics

The following Application Security metrics are available for Runtime Vulnerability Analytics.

### Vulnerabilities

Metric name

Dynatrace version

Description

Open security problems (global)

1.225+

Number of currently open vulnerabilities seen within the last minute. The metric value is independent of any configured management zone (and thus global).

New open security problems (global)

1.222+

Number of vulnerabilities that were recently created. The metric value is independent of any configured management zone (and thus global).

New muted security problems (global)

1.222+

Number of vulnerabilities that were recently muted. The metric value is independent of any configured management zone (and thus global).

Open security problems (split by management zone)

1.231+

Number of currently open vulnerabilities seen within the last minute. The metric value is split by management zone.

New open security problems (split by management zone)

1.231+

Number of vulnerabilities that were recently created. The metric value is split by management zone.

New resolved security problems (global)

1.222+

Number of vulnerabilities that were recently resolved. The metric value is independent of any configured management zone (and thus global).

#### Dimensions used in vulnerability metrics

* Risk level (`Critical`, `High`, `Medium`, `Low`, `None`)
* Type (`Third-party vulnerability`, `Code-level vulnerability`)
* Management zone name â only for split-by-zone metrics
* Vulnerable component type (`Library`, `Runtime`) â only available for third-party vulnerabilities
* Public internet exposure (`Public internet exposure`, `No public internet exposure`, `Public internet exposure not available`)
* Reachable data assets (`Reachable data assets`, `No reachable data assets`, `Reachable data assets not available`)
* Vulnerable functions (`Vulnerable functions in use`, `No vulnerable functions in use`, `Vulnerable functions not available`)
* Assessment accuracy (`Full accuracy`, `Reduced accuracy`, `Accuracy not available`)
* Public exploit (`Public exploit published`, `No public exploit published`)

### Affected entities

Metric name

Dynatrace version

Description

Vulnerabilities - affected entities count

1.251+

Total number of unique affected entities across all open vulnerabilities. The metric supports the management zone selector.

#### Dimensions used in affected entities metrics

* Security problem ID
* External vulnerability ID
* Title
* Vulnerable component (Package name or `Not available`)
* CVE (All related CVE IDs or `Not available`)
* Risk level (`CRITICAL`, `HIGH`, `MEDIUM`, `LOW`, `NONE`)
* Technology (`Java`, `.NET`, `Node.js`, `PHP`, `GO`)
* Type (`Third-party vulnerability`, `Code-level vulnerability`)

## View

To view Application Security metrics

1. Go to **Metrics**.
2. Filter for the category of metrics you want, for example `affected process groups`.

   * If you don't see results, turn off **Only show metrics reported after the start of the selected timeframe**.
   * You can add more filters (`Tag`, `Unit`, `Favorites`). See [Filter and sort the table](/docs/analyze-explore-automate/dashboards-classic/metrics-browser#filter "Browse metrics with the Dynatrace metrics browser.") for details.
3. Expand **Details** for any metric to see metric details and a chart of the metric over the selected timeframe. For more information, see [Metrics browser](/docs/analyze-explore-automate/dashboards-classic/metrics-browser "Browse metrics with the Dynatrace metrics browser.").

   Example metric details:

   ![Metric example appsec](https://dt-cdn.net/images/2021-08-11-11-01-04-1505-deabc3769d.png)

## Usage

You can use Application Security metrics to

* [Create charts and pin them to your dashboards](/docs/analyze-explore-automate/dashboards-classic/metrics-browser#pin "Browse metrics with the Dynatrace metrics browser.")
* [Query data in Data Explorer](/docs/analyze-explore-automate/explorer#query-components-and-concepts "Query for metrics and transform results to gain desired insights.")

### Example

To view the current status of affected entities in your environment and see how the process of remediating vulnerabilities is developing, create a chart for the `Vulnerabilities - affected entities count` metric and pin it to your dashboard.

## Export and share

Once you run a query in Data Explorer, you can

* [Share metrics results](/docs/analyze-explore-automate/explorer#share "Query for metrics and transform results to gain desired insights.")
* [Export metric results](/docs/analyze-explore-automate/explorer#csv "Query for metrics and transform results to gain desired insights.")
* [Use metric results in API requests](/docs/analyze-explore-automate/explorer#api "Query for metrics and transform results to gain desired insights.")

## Related topics

* [Threats & Exploits](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.")
* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: application-security-overview.md


---
title: Application Security overview
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/application-security-overview
scraped: 2026-02-15T21:26:23.302362
---

# Application Security overview

# Application Security overview

* Explanation
* Updated on Jun 17, 2025

This page refers to the classic ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview** app, which is deprecated.  
For the latest Dynatrace experience, use the readyâmade [**Vulnerability coverage** dashboard](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.") to stay ahead of your vulnerability posture. It provides insights into process and host coverage, scan activity, and the evolution of vulnerability findings.

After you [set up Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), Dynatrace starts monitoring your applications to detect vulnerabilities. Go to ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview** for an overview of vulnerabilities in your global environment.

For security reasons, access to this page is restricted to users who are part of the **Security admin** group for the whole environment, not just for a selected set of management zones.

The **Application Security overview** page displays the following information.

* [A count of vulnerabilities in your environment](#info)
* [A chart of vulnerabilities by risk level](#risk-level)
* [A chart of vulnerabilities by status](#status)
* [A host coverage chart](#host-coverage)
* [Top five affected process groups](#affected-pg)
* [Technology coverage](#tech-coverage)

## Vulnerability count

![infographic of vulnerabilities in your environment](https://dt-cdn.net/images/2023-03-15-10-06-59-606-8f8cdf178c.png)

The infographic at the top of the page is based on calculations that take place every 15 minutes and shows

* In the foreground, the total count of the most severe open vulnerabilities in your environment (`26 critical` in the example above).
* **Third-party vulnerabilities:** The number of the most severe open critical third-party vulnerabilities (`21 critical` in the example above). Select it to go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** filtered by the highest risk level and the open status.

  This feature isn't displayed if [third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.
* **Code-level vulnerabilities:**

  + The number of open code-level vulnerabilities (`5 critical` in the example above). Select it to go to ![Code Level Vulnerabilities](https://dt-cdn.net/images/code-level-vulnerabilities-512-49803cb5cf.png "Code Level Vulnerabilities") **Code-Level Vulnerabilities** filtered by the open status.

    This feature isn't displayed if [code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.
  + The total number of attacksâexploited, blocked, and allowlisted (`2,765 attacks` in the example above)âthat occurred over the last 30 days. Select it to go to the unfiltered ![Attacks](https://dt-cdn.net/hub/logos/attack-protection.png "Attacks") **Attacks**.

    This feature isn't displayed if [Application Protection](/docs/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.") isn't activated and enabled.

## Risk level

Third-party vulnerabilities

Code-level vulnerabilities

![risk-level-card-security-overview](https://dt-cdn.net/images/2023-03-14-09-42-28-779-dff88cf5dc.png)

The **Risk level** section shows a chart of third-party vulnerabilities by risk level (`critical`, `high`, `medium`, `low`).

This section isn't displayed if [third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

Two perspectives are displayed:

* **Currently open vulnerabilities:** The number of third-party vulnerabilities currently open, grouped by risk level (`21 Critical`, `151 High`, `247 Medium`, `53 Low` in the example above). Select any group to go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** filtered by the respective risk level and open state.
* **Vulnerability evolution over time:** The maximum value of the day for vulnerabilities in your global environment, over the last 30 days, split by risk level. To refine the chart by risk level, select chart legend entries.

  Vulnerabilities are constantly reassessed and may change their risk level over time. For details, see [FAQ](#faq).

Select **View all third-party vulnerabilities** to go to the unfiltered list of third-party vulnerabilities in your environment.

![clvs-risk-level](https://dt-cdn.net/images/2023-03-14-10-04-31-772-302bdac8df.png)

The **Risk level** section shows a chart of code-level vulnerabilities by risk level (`critical`).

This section isn't displayed if [code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

Two perspectives are displayed:

* **Currently open vulnerabilities:** The number of critical code-level vulnerabilities currently open, grouped by risk level (`5 Critical` in the example above).
* **Vulnerability evolution over time:** The maximum value of the day for vulnerabilities in your global environment, over the last 30 days.

Select **View all code-level vulnerabilities** to go to the unfiltered list of code-level vulnerabilities in your environment.

## Vulnerabilities

Third-party vulnerabilities

Code-level vulnerabilities

![vuln-chart-tpv](https://dt-cdn.net/images/2023-05-17-16-46-45-805-9963c32d08.png)

The **Vulnerabilities** section shows a chart of third-party vulnerabilities in your global environment by status (`resolved`, `open`, `muted(open)`), over the last 30 days. You can see when a vulnerability was opened, reopened, resolved, or muted. To refine the chart by risk level, select chart legend entries.

This section isn't displayed if [third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

Select **View all third-party vulnerabilities** to go to the unfiltered list of third-party vulnerabilities in your environment.

![clv-status-chart](https://dt-cdn.net/images/clv-status-chart-778-36cddd9069.png)

The **Vulnerabilities** section shows a chart of code-level vulnerabilities in your global environment by status (`resolved`, `open`, `muted(open)`), over the last 30 days. You can see when a vulnerability was opened, reopened, resolved, or muted. To refine the chart by risk level, select chart legend entries.

This section isn't displayed if [code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

Select **View all code-level vulnerabilities** to go to the unfiltered list of code-level vulnerabilities in your environment.

## Host coverage

The **Host coverage** section shows the coverage of hosts on which vulnerability detection is enabled, based on your settings. This helps you determine where there are coverage gaps and how this can relate to the current number of open vulnerabilities in your environment.

Third-party vulnerabilities

Code-level vulnerabilities

![Host coverage example for third-party vulnerabilities](https://dt-cdn.net/images/2023-06-12-13-23-33-803-6b5f8a2414.png)

This section isn't displayed if [third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

The following information is provided.

* The number and percentage of supported hosts from the total number of hosts in your environment. For example, if the total number of hosts is 1,755 hosts, and, from this amount, only 1,398 hosts are supported, then the remaining 357 hosts belong to technologies that are not supported by Dynatrace.
* In the foreground, the number of hosts that are excluded from monitoring by monitoring rules. To improve the coverage gaps, you need to decrease this number. For details, see [How to increase host coverage](#increase).
* **Supported hosts:** All hosts with [supported technologies](/docs/secure/application-security#tech "Access the Dynatrace Application Security functionalities.") in your environment, regardless of their monitoring status (comprises the monitored and excludes hosts). Select **Supported hosts** to go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered by supported hosts.
* **Monitored hosts:** The supported hosts in your environment on which [Third-Party Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is enabled, and that are not excluded from monitoring by [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."). Also displayed is the percentage of monitored hosts from the total number of supported hosts. Select **Monitored hosts** to go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered to display only the hosts covered by your [active monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#active "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.").
* **Excluded hosts:** The number of supported hosts on which [Third-Party Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is enabled, but that are excluded from monitoring by [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") or by having a relevant technology disabled. Also displayed is the percentage of excluded hosts from the total of supported hosts. Select **Excluded hosts** to go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered by excluded hosts.

![host-coverage-clv](https://dt-cdn.net/images/image-8-1077-ac55d59678.png)

This section isn't displayed if [code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

The following information is provided.

* The number and percentage of supported hosts from the total number of hosts in your environment. For example, if the total number of hosts is 65 hosts, and, from this amount, only 24 hosts are supported, then the remaining 41 hosts belong to technologies that are not supported by Dynatrace.
* In the foreground, the number of hosts that are excluded from monitoring by monitoring rules. To improve the coverage gaps, you need to decrease this number. For details, see [How to increase host coverage](#increase).
* **Supported hosts:** All hosts with [supported technologies](/docs/secure/application-security#tech-clv "Access the Dynatrace Application Security functionalities.") in your environment, regardless of their monitoring status (comprises the monitored and excludes hosts). Select **Supported hosts** to go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered by supported hosts.
* **Monitored hosts:** The supported hosts in your environment on which [Code-level Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-clva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is enabled and the [global code-level vulnerability detection control](/docs/secure/application-security/vulnerability-analytics#config "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is set to `Monitor` for at least one supported technology, and that are not excluded from monitoring by [monitoring rules](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups"). Also displayed is the percentage of monitored hosts from the total of supported hosts. Select **Monitored hosts** to go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered by monitored hosts.
* **Excluded hosts:** The number of supported hosts on which [Code-level Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-clva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is enabled but that are excluded from monitoring by [monitoring rules](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups") or by having the [global code-level vulnerability detection control](/docs/secure/application-security/vulnerability-analytics#config "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") set to `Do not monitor` for all supported technologies. Also displayed is the percentage of excluded hosts from the total of supported hosts. Select **Excluded hosts** to go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered by excluded hosts.

### How host coverage is calculated

Host coverage is calculated based on the last 70 minutes and uses all hosts in your environment that run a supported technology.
See below the calculation mechanism for third-party and code-level vulnerabilities.

Third-party vulnerabilities

Code-level vulnerabilities

1. **Collect:** Dynatrace first collects all monitored hosts.
2. **Filter:** All monitored hosts collected are then filtered based on your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."). If there are hosts that are excluded by monitoring rules, host coverage decreases.

* If there's a decrease in coverage, it can take up to 70 minutes until changes are displayed.
* If there's an increase in coverage, it can take up to 10 minutes until changes are displayed.

Dynatrace collects hosts based on the processes that are configured to report code-level vulnerabilities.
If at least one process is able to report code-level vulnerabilities, then its host is covered.

A process is able to report code-level vulnerabilities when

* [Code-level Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-clva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is globally enabled
* [OneAgent monitoring is enabled](/docs/secure/application-security/vulnerability-analytics#enable-oneagent "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* The [global code-level vulnerability detection control](/docs/secure/application-security/vulnerability-analytics#config "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is set to `Monitor` for the technology of the given process.
* No [monitoring rules](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups") exclude the process group of the respective process from monitoring
* The process is restarted after a change in configuration

* If there's a decrease in coverage, it can take up to 70 minutes until changes are displayed.
* If there's an increase in coverage, it can take up to 10 minutes until changes are displayed.

### How to increase host coverage

To increase the host coverage for third-party and code-level vulnerabilities, follow the instructions below.

Third-party vulnerabilities

Code-level vulnerabilities

1. [Enable Third-party Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") globally.
2. Enable all the [supported technologies](/docs/secure/application-security/vulnerability-analytics#tech-tpv "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") that you want Dynatrace to cover. Note that only hosts running technologies that are listed and enabled can be collected.
3. In your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."), look for hosts that are excluded from monitoring, and adapt these rules if you want the respective hosts to be collected.

1. [Enable Code-level Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-clva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") globally.
2. [Enable OneAgent monitoring](/docs/secure/application-security/vulnerability-analytics#enable-oneagent "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
3. Set the [global code-level vulnerability detection control](/docs/secure/application-security/vulnerability-analytics#config "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") to `Monitor` for all supported technologies.
4. In your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups"), look for process groups that are excluded from monitoring, and adapt these rules. Note that a host is monitored when one of its processes is monitored with Application Security.
5. Restart the process.

It can take up to 10 minutes until any change is displayed.

## Affected process groups

![affected-pg-security-overview](https://dt-cdn.net/images/2022-11-10-12-26-56-763-e4e8d7444e.png)

The **Affected process groups** section shows the top five process groups affected by third-party vulnerabilities, sorted by

1. The severity of the vulnerabilities affecting the process group.
2. The number of vulnerabilities affecting the process group.

This section isn't displayed if [third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

The following information is provided.

* The name of the process group with a link to the associated process group details page.
* The corresponding technology.
* The number of vulnerabilities affecting that process group out of the total number of vulnerabilities related to it.

For deeper insights, see [Manage third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.").

## Technology coverage

Third-party vulnerabilities

Code-level vulnerabilities

![Technology coverage for third-party vulnerabilities](https://dt-cdn.net/images/2023-05-31-09-47-29-802-e9b9030cd7.png)

**Use case:** Gain an overview of the third-party vulnerability coverage by technology to determine which technologies have the most affected entities and which process groups or nodes (in the case of Kubernetes vulnerabilities) are the most vulnerable.

This section isn't displayed if [third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

The following information is displayed.

* A table listing the [supported technologies](/docs/secure/application-security#tech "Access the Dynatrace Application Security functionalities.") for third-party vulnerabilities, their monitoring status (enabled or disabled), the monitored entities (process groups or, in the case of Kubernetes vulnerabilities, nodes), and the number and percentage of affected entities from the total number of monitored entities.
* A chart of the affected entity evolution by technology over the last 30 days. Hover over the data for details. To refine the chart by technology, select chart legend entries.

To increase technology coverage for third-party vulnerabilities

1. Enable all the [supported technologies](/docs/secure/application-security/vulnerability-analytics#tech-tpv "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") that you want Dynatrace to cover.
2. In your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes."), look for entities that are excluded from monitoring and adapt these rules if you want the respective entities to be monitored.

![Technology coverage for code-level vulnerabilities](https://dt-cdn.net/images/2023-05-31-11-44-28-797-e09685a824.png)

**Use case:** Gain an overview of the code-level vulnerability coverage by technology to determine which technologies have the most affected entities and which process groups are the most vulnerable.

This section isn't displayed if [code-level vulnerability detection](/docs/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is disabled.

The following information is displayed.

* A table listing the [supported technologies](/docs/secure/application-security#tech-clv "Access the Dynatrace Application Security functionalities.") for code-level vulnerabilities, their monitoring status (enabled or disabled), the monitored entities (process groups), and the number and percentage of affected entities from the total number of monitored entities.
* A chart of the affected entity evolution by technology over the last 30 days. Hover over the data for details.

To increase technology coverage for code-level vulnerabilities

1. Set the [global code-level vulnerability detection control](/docs/secure/application-security/vulnerability-analytics#config "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") to `Monitor` for at least one supported technology.
2. In your [monitoring rules](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups"), look for process groups that are excluded from monitoring and adapt these rules.

## FAQ

### Why isn't the host coverage increasing?

If you have followed the steps to [increase the Application Security host coverage](#increase), yet the number of covered hosts stays the same, follow the instructions below.

Third-party vulnerabilities

Code-level vulnerabilities

Make sure that

1. Your OneAgent version is compatible with the [supported technologies](/docs/secure/application-security#tech "Access the Dynatrace Application Security functionalities.").
2. **(â¦) software component reporting** OneAgent features are enabled for all technologies (go to **Settings** > **Preferences** > **OneAgent features** and search for **(â¦) software component reporting**).
3. There are no OneAgent features configured at the process-group level overriding the global OneAgent configuration. For details, see [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.").
4. You restart processes after each change in configuration.

Make sure that

1. Your OneAgent version is compatible with the [supported technologies](/docs/secure/application-security#tech-clv "Access the Dynatrace Application Security functionalities.").
2. There are no OneAgent features configured at the process-group level overriding the global OneAgent configuration. For details, see [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.").

### Why doesn't the number of covered hosts match?

If you [define tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.") for hosts covered by Application Security and you notice that the number of hosts on ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** filtered by your Application Security tags is different from the number of hosts displayed in ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview** under [**Host coverage**](/docs/secure/application-security/vulnerability-analytics/application-security-overview#host-coverage "Get an overview of the security issues of your third-party libraries."), follow the instructions below.

Third-party vulnerabilities

Code-level vulnerabilities

1. Make sure that your OneAgent version is compatible with the [supported technologies](/docs/secure/application-security#tech "Access the Dynatrace Application Security functionalities.").
2. Enable **(â¦) software component reporting** OneAgent features for all technologies (go to **Settings** > **Preferences** > **OneAgent features**, and search for **(â¦) software component reporting**).
3. Make sure that there are no OneAgent features configured at the process-group level overriding the global OneAgent configuration. For details, see [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.").
4. Enable all supported technologies (go to **Settings** > **Application Security** > **Vulnerability Analytics** > **General settings** and select **Third-party Vulnerability Analytics**). For details, see [Control by technology](/docs/secure/application-security/vulnerability-analytics#technology "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

1. Make sure that your OneAgent version is compatible with the [supported technologies](/docs/secure/application-security#tech-clv "Access the Dynatrace Application Security functionalities.").
2. Make sure that there are no OneAgent features configured at the process-group level overriding the global OneAgent configuration. For details, see [OneAgent features](/docs/ingest-from/dynatrace-oneagent/oneagent-features "Manage OneAgent features globally and per process group.").

### How many TPVs are counted if their risk level changes?

*On the risk-level chart, how many third-party vulnerabilities are counted in one day if their risk level changes several times that day (for example, from `Medium` to `High`, and back to `Medium` again)?*

In this case, the vulnerability is counted twice, once for `Medium` and once for `High`.

### How many TPVs are counted if affected process is restarted?

*On the risk-level chart, how many third-party vulnerabilities are counted in one day if the affected process is restarted several times that day, but the vulnerability risk level stays the same (for example, `Medium`)?*

In this case, the vulnerability is counted one time, as `Medium`.

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: define-monitoring-rules-clv.md


---
title: Monitoring rules - Code-level Vulnerability Analytics
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv
scraped: 2026-02-15T21:25:00.783318
---

# Monitoring rules - Code-level Vulnerability Analytics

# Monitoring rules - Code-level Vulnerability Analytics

* Latest Dynatrace
* How-to guide
* Updated on Dec 18, 2025

You can create your own fine-grained monitoring rules for code-level vulnerabilities based on [resource attributes](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."), and define multiple conditions for one rule. When creating a rule, you can check if conditions apply and how many process groups are affected.
The rules you create override the global code-level vulnerability detection control for the selected technology.

## Prerequisites

[Enable Code-level Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-clva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

## Create custom monitoring rules

1. Go to **Settings** and select **Application security** > **Vulnerability Analytics** > **Monitoring rules: Code-level**.
2. Select **Add new rule**.
3. Optional Name your rule (if not, a name will be assigned to it automatically once you create the rule, based on your criteria).
4. For **Code-level vulnerability control**, specify how to control a vulnerability that matches the rule criteria:

   * **Do not monitor** â Code-level vulnerabilities for the selected conditions are ignored.
   * **Monitor** â Code-level vulnerabilities for the selected selected conditions are reported.
5. Optional If you want the rule to apply only to a subset of your environment, for **Specify where the rule is applied**, select **Add new condition** and provide the resource attributes that should be used to identify that part of the environment (for example, `dt.entity.process_group`, `aws.region`). For details, see [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").
6. Optional To check if a rule applies, select **Preview matching process group instances**. This lists process group instances that currently match the criteria.
7. Select **Save changes**.
8. Restart your processes.

You can edit, disable, enable, or remove rules at any time.

Monitoring rules are ordered; the first matching rule applies.

## Coverage impact

Monitoring rules directly influence host and process coverage. If a host or process group is excluded by a rule, it won't be monitored for vulnerabilities.

To review how your monitoring rules affect overall coverage, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

## FAQ

* What happens if I change the order of the rules?

  + The first matching rule applies.
* What happens if a **Do not monitor** rule that applies gets added?

  + New vulnerabilities for the processes that match the rule won't be created.
  + Existing vulnerabilities that only relate to matching processes are resolved.
* What happens if a **Do not monitor** rule is deleted or doesn't apply anymore?

  + New vulnerabilities for the processes that match the rule will be created.
  + Related resolved vulnerabilities are reopened.

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: email-integration.md


---
title: Email integration for security notifications
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration
scraped: 2026-02-15T09:13:26.867695
---

# Email integration for security notifications

# Email integration for security notifications

* How-to guide
* Updated on Apr 25, 2023

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** and ![Code Level Vulnerabilities](https://dt-cdn.net/images/code-level-vulnerabilities-512-49803cb5cf.png "Code Level Vulnerabilities") **Code-Level Vulnerabilities** apps, which are deprecated. If you're currently using these apps, we recommend transitioning to the unified [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Upgrade to the latest Dynatrace](/docs/platform/upgrade "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.").

Integrate security notifications with Dynatrace to pass security issues and/or attacks to your email account for alerting and remediation purposes.

To integrate security notifications via email, follow the instructions below.

## Set up notifications for vulnerabilities

To set up notifications for vulnerabilities

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an alerting profile**](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration#profile-create "Integrate security notifications for vulnerabilities via email.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Link the alerting profile**](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/email-integration#profile-link "Integrate security notifications for vulnerabilities via email.")

### Step 1 Create an alerting profile

Create an alerting profile that allows you to set up alert-filtering rules that are based on the risk level of detected vulnerabilities.

1. Go to **Settings** and select **Alerting** > **Vulnerability alerting profiles**.
2. Select **Add alerting profile**.
3. Enter a **Name** for the profile on which you want to receive security notifications.
4. Under **Alert for the following events**, select at least one event type for which you want to receive notifications.

   * If **Vulnerability (re)opened** is turned on and **New management zone affected** is turned off, you are notified when a vulnerability is opened or reopened.
   * If **New management zone affected** is turned on and **Vulnerability (re)opened** is turned off, you are notified when an already open vulnerability starts affecting a management zone in your environment that wasn't previously affected.
   * If both **Vulnerability (re)opened** and **New management zone affected** are turned on, you are notified when a vulnerability is opened or reopened, or when an open vulnerability starts affecting a new management zone.
5. Optional To restrict alerts to one management zone, under **Alert only if the following management zone is affected (optional)**, select the desired management zone from the dropdown list. This way, you are alerted only when the selected management zone is affected by the selected event types. For example, for the **New management zone affected** event type, you are notified when an open vulnerability that hasn't previously affected your selected management zone starts affecting it.

   Only one management zone can be selected per alerting profile.
6. Turn on each risk level for which you want to receive notifications. You can select more than one.
7. Select **Save changes** to save your configuration.

### Step 2 Link the alerting profile to an email security notifications integration

Link the alerting profile to a security notifications integration via email. You can define the email integration and configure the payload (in the form of a message template) that you want to receive with your security notifications.

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Add integration** and enter the following information.

   * **Security alert type:** Select **Vulnerability alert**.
   * **Notification type:** Select **Email**.
   * **Display name:** Enter a name for the email integration. This name will be displayed on **Settings** > **Integration** > **Security notifications** after you save this configuration.
   * Select **Add recipient** to add the email address of the recipient (required), carbon copy recipient (optional), and blind carbon copy recipient (optional). The total number of email addresses mustn't exceed 50.
   * **Subject:** Enter the title of the vulnerability.
   * **Body:** Enter the vulnerability description. HTML formatting is supported.

   Besides plain text, your vulnerability description can include placeholders. Select the **Info** icon for a list of **Available placeholders** that you can use for this integration. Placeholders are automatically replaced with information related to the vulnerability when the notification is generated.

   **Example body:**

   ```
   <h3>



   Vulnerability {SecurityProblemId}: {Title}



   </h3>



   <br>



   Severity: <b>{Severity}</b><br>



   Davis Security Score: <b>{DavisSecurityScore}</b><br>



   <hr>



   <br>



   {Description}



   <br>



   <br>



   {Tags}



   <br>



   {Tags[Host Name]}



   <br>



   {ManagementZones}



   <br>
   ```

* **Alerting profile:** Select the [alerting profile](#profile-create) on which you want to receive security notifications.
* Optional To verify your configuration, select **Send test notification**. If your configuration is correct:

  + You should receive a test email on your desired email account
  + The following info message should be displayed on the Dynatrace settings page: `Test notification sent successfully`.
* **Save changes**.

**Example email reporting**

![Example email reporting](https://dt-cdn.net/images/image-7-1199-b6406026cc.png)

## Verify your configuration

To verify that your integration is set up correctly

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Details** for the integration you want to check.
3. Select **Send test notification**. If your configuration is incorrect and the test notification hasn't been sent via email, you'll receive an error message that will help you identify the problem.

## Related topics

* [Threats & Exploits](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.")
* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: jira-integration.md


---
title: Jira integration for security notifications
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration
scraped: 2026-02-15T09:10:01.276976
---

# Jira integration for security notifications

# Jira integration for security notifications

* How-to guide
* Updated on Apr 25, 2023

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** and ![Code Level Vulnerabilities](https://dt-cdn.net/images/code-level-vulnerabilities-512-49803cb5cf.png "Code Level Vulnerabilities") **Code-Level Vulnerabilities** apps, which are deprecated. If you're currently using these apps, we recommend transitioning to the unified [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Upgrade to the latest Dynatrace](/docs/platform/upgrade "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.").

With Dynatrace Jira integration, issue tickets are generated automatically for all new vulnerabilities in your Dynatrace environments. Direct integration of Dynatrace and Atlassian Jira saves you a lot of manual work and completely automates the reporting of Dynatrace-detected vulnerabilities in your monitored environments into your organization's Jira project.

To integrate security notifications with Jira, follow the instructions below.

## Set up notifications for vulnerabilities

To set up notifications for vulnerabilities

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an alerting profile**](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration#profile-create "Integrate security notifications for vulnerabilities and/or attacks using Jira.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Link the alerting profile**](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/jira-integration#profile-link "Integrate security notifications for vulnerabilities and/or attacks using Jira.")

### Step 1 Create an alerting profile

Create an alerting profile, which allows you to set up alert-filtering rules that are based on the risk level of detected vulnerabilities.

1. Go to **Settings** and select **Alerting** > **Vulnerability alerting profiles**.
2. Select **Add alerting profile**.
3. Enter a **Name** for the profile on which you want to receive security notifications.
4. Under **Alert for the following events**, select at least one event type for which you want to receive notifications.

   * If **Vulnerability (re)opened** is turned on and **New management zone affected** is turned off, you are notified when a vulnerability is opened or reopened.
   * If **New management zone affected** is turned on and **Vulnerability (re)opened** is turned off, you are notified when an already open vulnerability starts affecting a management zone in your environment that wasn't previously affected.
   * If both **Vulnerability (re)opened** and **New management zone affected** are turned on, you are notified when a vulnerability is opened or reopened, or when an open vulnerability starts affecting a new management zone.
5. Optional To restrict alerts to one management zone, under **Alert only if the following management zone is affected (optional)**, select the desired management zone from the dropdown list. This way, you are alerted only when the selected management zone is affected by the selected event types. For example, for the **New management zone affected** event type, you are notified when an open vulnerability that hasn't previously affected your selected management zone starts affecting it.

   Only one management zone can be selected per alerting profile.
6. Turn on each risk level for which you want to receive notifications. You can select more than one.
7. Select **Save changes** to save your configuration.

### Step 2 Link the alerting profile to a Jira security notifications integration

Link the alerting profile to a security notifications integration with Jira. You can define the Jira integration and configure the payload (in the form of a message template) that you want to receive with your security notifications.

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Add integration** and enter the following information.

   * **Security alert type:** Select **Vulnerability alert**.
   * **Notification type:** Select **Jira**.
   * **Display name:** Enter a name for the Jira integration. This name will be displayed on **Settings** > **Integration** > **Security notifications** after you save this configuration.
   * **Jira endpoint URL:** Enter the URL of the Jira API endpoint using the following syntax: `https://{instancename}.atlassian.net/rest/api/2`. Be sure to replace `{instancename}` with your Atlassian instance.
   * **Username:** Enter the username of the Jira profile.
   * **API token:** Enter the Jira API token for the Jira profile. To create an API token, in your Jira account, go to **API tokens** and select **Create API token**.
   * **Project key:** Enter the key of the Jira project where new issues are to be created and tracked. To find the project key, in your Jira account, go to **Project settings** > **Details**.
   * **Issue type:** Enter the issue type, such as `task` or `story`, that should be used for issues detected by Dynatrace. Be sure to specify an issue type that's already been set up in Jira. To find all available issue types or create a new one, in your Jira account, go to **Project settings** > **Issue types**.
   * **Summary:** Enter a brief summary of the issue.
   * **Issue description:** Enter details of the issue.

   Besides plain text, your summary and issue description can both include placeholders. Select the **Info** icon for a list of **Available placeholders** that you can use for this integration. Placeholders are automatically replaced with information related to the vulnerability when the notification is generated.

   **Example issue description:**

   ```
   Severity: {Severity}



   Davis Security Score: {DavisSecurityScore}



   {Description}



   {Tags}



   {Tags[Host Name]}



   {ManagementZones}
   ```

   * **Alerting profile:** Select the [alerting profile](#profile-create) on which you want to receive security notifications.
3. Optional To verify your configuration, select **Send test notification**. If your configuration is correct:

   * A test story should be created in Jira
   * The following info message should be displayed on the Dynatrace settings page: `Test notification sent successfully`.
4. **Save changes**.

**Example reporting to a Jira ticket**

![Example reporting to a Jira ticket](https://dt-cdn.net/images/image-5-886-71f6b5cf8d.png)

Dynatrace doesn't automatically close resolved issues. You need to close Jira issues manually.

## Verify your configuration

To verify that your integration is set up correctly

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Details** for the integration you want to check.
3. Select **Send test notification**. If your configuration is incorrect and the test notification hasn't been sent to Jira, you'll receive an error message that will help you identify the problem.

## Related topics

* [Threats & Exploits](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.")
* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: webhook-integration.md


---
title: Webhook integration for security notifications
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration
scraped: 2026-02-15T09:13:40.608927
---

# Webhook integration for security notifications

# Webhook integration for security notifications

* How-to guide
* Updated on Apr 25, 2023

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** and ![Code Level Vulnerabilities](https://dt-cdn.net/images/code-level-vulnerabilities-512-49803cb5cf.png "Code Level Vulnerabilities") **Code-Level Vulnerabilities** apps, which are deprecated. If you're currently using these apps, we recommend transitioning to the unified [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Upgrade to the latest Dynatrace](/docs/platform/upgrade "Use the power of Grail, AppEngine, and AutomationEngine to take advantage of improvements in storing and analyzing observability and security data.").

Integrate security notifications with Dynatrace to pass security issues and/or attacks to your teams for alerting and remediation purposes.

To integrate security notifications using webhooks, follow the instructions below.

## Set up notifications for vulnerabilities

To set up notifications for vulnerabilities

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create an alerting profile**](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration#profile-create "Integrate security notifications for vulnerabilities and/or attacks using webhooks.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Link the alerting profile**](/docs/secure/application-security/vulnerability-analytics/security-notifications-rva/webhook-integration#profile-link "Integrate security notifications for vulnerabilities and/or attacks using webhooks.")

### Step 1 Create an alerting profile

Create an alerting profile, which allows you to set up alert-filtering rules that are based on the risk level of detected vulnerabilities.

1. Go to **Settings** and select **Alerting** > **Vulnerability alerting profiles**.
2. Select **Add alerting profile**.
3. Enter a **Name** for the profile on which you want to receive security notifications.
4. Under **Alert for the following events**, select at least one event type for which you want to receive notifications.

   * If **Vulnerability (re)opened** is turned on and **New management zone affected** is turned off, you are notified when a vulnerability is opened or reopened.
   * If **New management zone affected** is turned on and **Vulnerability (re)opened** is turned off, you are notified when an already open vulnerability starts affecting a management zone in your environment that wasn't previously affected.
   * If both **Vulnerability (re)opened** and **New management zone affected** are turned on, you are notified when a vulnerability is opened or reopened, or when an open vulnerability starts affecting a new management zone.
5. Optional To restrict alerts to one management zone, under **Alert only if the following management zone is affected (optional)**, select the desired management zone from the dropdown list. This way, you are alerted only when the selected management zone is affected by the selected event types. For example, for the **New management zone affected** event type, you are notified when an open vulnerability that hasn't previously affected your selected management zone starts affecting it.

   Only one management zone can be selected per alerting profile.
6. Turn on each risk level for which you want to receive notifications. You can select more than one.
7. Select **Save changes** to save your configuration.

### Step 2 Link the alerting profile to a webhook security notifications integration

Link the alerting profile to a security notifications integration using webhooks. You can define the webhook integration and configure the payload (in the form of a message template) that you want to receive with your security notifications.

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Add integration** and enter the following information.

   * **Security alert type:** Select **Vulnerability alert**.
   * **Notification type:** Select **Custom integration**.
   * **Display name:** Enter a name for the webhook integration. This name will be displayed on **Settings** > **Integration** > **Security notifications** after you save this configuration.
   * **Webhook endpoint URL:** Enter the URL of the webhook API endpoint.
3. Optional Choose whether you want to accept any SSL certificate.

   * **On** = Accept any SSL certificate (including self-signed and invalid certificates)
   * **Off** = Dynatrace verifies the SSL certificate of the URL. (Recommended)
4. Select **Add HTTP header** to specify additional HTTP header fields, such as `Content-Type` or `Authorization`. These custom HTTP header fields can be used if the target endpoint needs an authentication token within the HTTP header or if you would like to send different content types such as `application/json`, `application/xml`, `text/plain`.

   The **Content-Type** field is required, others are optional.
5. In the **Custom payload** field, customize your notification format and content. Once a vulnerability is detected or resolved, this customizable payload is pushed through an **HTTP POST** to the target system. Select the **Info** icon for a list of **Available placeholders** that you can use for this integration. Placeholders are automatically replaced with information related to the vulnerability when the notification is generated.

**Example message template:**

```
{



"text": "New management zone is affected for *{SecurityProblemId}* and *{Severity} {DavisSecurityScore}* (CVSS: {CvssScore}). \nTitle: *{Title}*\n```{Description}```\n{SecurityProblemUrl}\n* Public exploit: {ExploitAvailable}, \n* public exposure: {Exposed}, \n* sensitive data exposure: {SensitiveDataReachable}. \nTags[Host Name]: ```{Tags[Host Name]}``` ManagementZones: ```{ManagementZones} ```\n\n *from test system* :dynatrace: (triggered by 'all risk levels' rule)."



}
```

6. From the **Alerting profile** list, select the [alerting profile](#profile-create) on which you want to receive security notifications.
7. Optional To verify your configuration, select **Send test notification**. If your configuration is correct:

   * You should receive a notification on your organization's endpoint.
   * The following info message should be displayed on the Dynatrace settings page: `Test notification sent successfully`.
8. **Save changes**.

**Example payload:**

![Example payload webhook](https://dt-cdn.net/images/image-4-836-a601108485.png)

## Verify your configuration

To verify that your integration is set up correctly

1. Go to **Settings** and select **Integration** > **Security notifications**.
2. Select **Details** for the integration you want to check.
3. Select **Send test notification**. If your configuration is incorrect and the test notification hasn't been sent to your organization's selected endpoint, you'll receive an error message that will help you identify the problem.

## Related topics

* [Threats & Exploits](/docs/secure/threats-and-exploits "Understand, triage, and investigate detection findings and alerts.")
* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: davis-security-advisor.md


---
title: Davis Security Advisor calculations
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor
scraped: 2026-02-15T21:21:17.890395
---

# Davis Security Advisor calculations

# Davis Security Advisor calculations

* Explanation
* Published Dec 20, 2022

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated. If you're currently using this app, we recommend transitioning to the corresponding [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Vulnerabilities upgrade guide](/docs/secure/application-security/vulnerability-analytics/vulnerabilities-upgrade-classic-to-latest "Upgrade from the classic Thirdâparty and Codeâlevel vulnerabilities apps to the Vulnerabilities app in the latest Dynatrace.").

The Davis Security Advisor is displayed in ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** above the vulnerability list on the **Third-party vulnerabilities** page. It recommends the fixes that would most improve the overall security of your environment.

![dsa-tpv](https://dt-cdn.net/images/2023-03-14-09-18-22-1575-8bbc0c397f.png)

Each recommendation contains

* The library that needs to be updated (for example, `jackson-mapper-asl`)
* The library technology logo (for example, )
* The number of the most severe vulnerabilities that will be fixed after updating the library (for example, `Solves 1 critical`)
* The total number of vulnerabilities that will be fixed (for example, `4 vulnerabilities total`).

### Basis for calculation

To calculate recommended fixes, Davis Security Advisor takes into consideration all third-party vulnerabilities that are currently open and not muted; resolved or muted vulnerabilities aren't taken into account. Fixes are tailored to your environment and ranked based on how much they improve the overall security of your environment.

### Grouping

DSA groups specific libraries that trigger vulnerabilities to simplify remediation efforts.
When calculating the advice, Davis Security Advisor ignores the specific version of the library. All shown libraries contain known vulnerabilities and should be updated to the latest version.

### Advice ranking

Advice is ranked based on the severity of the third-party vulnerabilities. Advice regarding a critical vulnerability, for example, is ranked higher than advice for a high-severity vulnerability.

The severity of a vulnerability is calculated based on [Davis Security Score](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI."), so you can focus on fixing vulnerabilities that are relevant in your environment, instead of on those that have only a theoretical impact.

### Filtering

To filter by recommended fixes, see [Filter third-party vulnerabilities by recommended fixes with Davis Security Advisor](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#dsa-filter "Organize third-party vulnerabilities for easy management and to prioritize issues.").

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: davis-security-score.md


---
title: Davis Security Score calculations
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score
scraped: 2026-02-15T21:21:20.413861
---

# Davis Security Score calculations

# Davis Security Score calculations

* Explanation
* Updated on Mar 13, 2024

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated. If you're currently using this app, we recommend transitioning to the corresponding [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Vulnerabilities upgrade guide](/docs/secure/application-security/vulnerability-analytics/vulnerabilities-upgrade-classic-to-latest "Upgrade from the classic Thirdâparty and Codeâlevel vulnerabilities apps to the Vulnerabilities app in the latest Dynatrace.").

Davis Security Score (DSS) is an enhanced risk-calculation score based on the industry-standard [Common Vulnerability Scoring System (CVSS)ï»¿](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System). Davis AI is designed to provide a more precise risk-assessment score by considering additional parameters such as public internet exposure and whether or not data assets are reachable from an affected entity.

## How DSS is better than CVSS

Virtually all security products use the CVSS Base Score to set the severity of security vulnerabilities. CVSS was designed to be risk-averse, which means that, for any given vulnerability, the assigned score assumes the worst-case scenario. The CVSS specification does allow for some modifications based on environmental influences, but this is usually not factored into the risk score calculation, which leads to many high or critical vulnerability scores that the user needs to handle.

**DSS is more accurate:** Davis doesn't assume the worst-case scenario. Instead, Davis adapts the characteristics of the vulnerability to your particular environment, taking into consideration its structure and topology, and advises you as to which elements are at risk and how to handle security issues. With Davis AI, you can find out if the affected entity is reachable from the internet and if there is any data storage in reach of an affected entity.

**DSS makes you more efficient:** By including additional parameters in its analysis, Davis is designed to leverage data to more precisely calculate the security score and predict the potential risk of a vulnerability to your environment. By reducing the score of vulnerabilities that are considered less relevant for your environment, you gain time to focus on the most critical issues and fix them faster.

## Davis Security Score scale

The DSS scale ranges between 0.1 (lowest risk) and 10.0 (most critical risk):

* **Low risk:** Vulnerabilities are indicated with blue and range between 0.1 and 3.9
* **Medium risk:** Vulnerabilities are indicated with yellow and range between 4.0 and 6.9
* **High risk:** Vulnerabilities are indicated with red and range between 7.0 and 8.9
* **Critical risk:** Vulnerabilities are indicated with red and range between 9.0 and 10.0

## Calculation process

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**CVSS Base**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#step-1 "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Davis adds context to public internet exposure**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#step-2 "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Davis adds context to reachable data assets**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#step-3 "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Final score**](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#step-4 "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.")

### Step 1 CVSS Base

Davis calculation starts from the base [CVSS Scoreï»¿](https://dt-url.net/2e03r7g)[1](#fn-1-1-def), and takes into consideration metrics pertaining to

* Public internet exposure: **Attack vector (AV)**
* Reachable data assets: **Confidentiality (C)** and **Integrity (I)**

1

CVSS v2 is [deprecatedï»¿](https://dt-url.net/f6k3wfz). For vulnerabilities relying on this data, Davis Security Score can't be assessed.

### Step 2 Davis adds context to public internet exposure

To influence the security score of a third-party vulnerability based on the public internet exposure, Davis uses the **Modified Attack Vector (MAV)** metric. This metric reflects the context by which vulnerability exploitation is possible.

### Result

* If the original AV value shows exploitation is possible via network access, but, based on the topology information extracted from your environment, the service isn't actually exposed, Davis lowers the MAV value.
* In all other cases, the MAV value doesn't differ from the original AV value.

### Step 3 Davis adds context to reachable data assets

To influence the security score of a third-party vulnerability based on reachable data assets, Davis uses the **Modified Confidentiality (MC)** and **Modified Integrity (MI)** metrics. These metrics reflect the actual accessibility of a reachable data asset to an affected service.

### Result

* If the original C and I values show that data exposure or manipulation are possible, but, based on Davis' evaluation, there aren't any reachable data assets accessible by the affected service, Davis lowers the corresponding MC and MI values.
* In all other cases, the MC and MI values don't differ from the original C and I values.

### Step 4 Final score

The final score is calculated based on the previous two results.

**Example:**

In this example, the evaluation of public internet exposure and reachable data assets lowers the score by 23 percent, from **high** to **medium**.

![DSS lowering score example](https://dt-cdn.net/images/2024-02-14-14-18-35-775-6949cd30d4.png)

## FAQ

* How is the score calculated if a third-party vulnerability has more affected services?

  + Davis modifies the scores on the service level. If a vulnerability has more than one affected service, Davis uses the highest score.
* In which cases does Davis raise the final score?

  + Davis never raises DSS higher than the base CVSS. The values for public internet exposure and reachable data assets can only lower the score or leave it unchanged.
* [Why does my vulnerability have a different risk assessment and Davis Security Score than its affected entities?](/docs/secure/faq#risk-assessment-affected-entities "Frequently asked questions about Dynatrace Application Security.")

## Limitations

The DSS calculation currently differs in Grail-powered apps (such as ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**, ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**, ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**) from third-party vulnerabilities pages:

* On third-party vulnerabilities pages, DSS is assessed based on the remediable entities within the selected scope.
* In Grail-powered apps, DSS is assessed based on the DSS of the remediable entities within the selected scope.

Thus, the DSS (score and risk level) for vulnerabilities on Grail-powered apps can be lower than on the vulnerabilities pages.


---


## Source: define-monitoring-rules-tpv.md


---
title: Monitoring rules - Third-party Vulnerability Analytics
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv
scraped: 2026-02-15T21:21:21.938531
---

# Monitoring rules - Third-party Vulnerability Analytics

# Monitoring rules - Third-party Vulnerability Analytics

* Latest Dynatrace
* How-to guide
* Updated on Jan 07, 2026

To include or exclude specific entities from being monitored by Runtime Vulnerability Analytics, you can set up fine-grained monitoring rules for third-party vulnerabilities based on different [criteria](#criteria).

If you define custom monitoring rules, the [global third-party vulnerability detection control mode](/docs/secure/application-security/vulnerability-analytics#config-tpv "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") applies to all entities that are not matched by a rule.

## Monitoring criteria

There are currently two ways to set up monitoring rules:

* **Based on resource attributes and Kubernetes labels** Recommended

  + For details, see [New monitoring rules](#new).
* **Based on process group tag, host tag, and management zones**

  + For details, see [Classic monitoring rules](#classic).

To start monitoring based on your rules, you need to [activate](#activate) the corresponding monitoring criteria. The two criteria cannot be in place at the same time. When one is activated, the other one is deactivated. You can switch between them at any time.

For environments created on Dynatrace version 1.313+, classic monitoring rules based on process group tag, host tag, and management zones aren't available; you can [set up monitoring rules based on resource attributes and Kubernetes labels](#setup-new).

### Activate the preferred monitoring criteria

To activate your preferred way to define monitoring

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics**.
2. Make one of the following changes:

   * To activate the [new rules](#new), turn on **Enable new monitoring rules**.
   * To activate the [classic rules](#classic), turn off **Enable new monitoring rules**.

Your setting will persist until you change it again.

For environments created on Dynatrace version 1.313+, new monitoring rules are activated by default (no action is required from your side).

## New monitoring rules

Recommended

With the new monitoring rules, you can define which processes and Kubernetes nodes and hosts should be monitored.

* Process rules are based on [resource attributes](/docs/platform/oneagent/resource-attributes "Any signal that uses a given resource, such as host or process group, is enriched with certain attributes coming from the resource.").
* Kubernetes node and host rules are based on [Kubernetes labelsï»¿](https://dt-url.net/g442yn5).

Kubernetesârelated resource attributes (for example, `k8s.cluster.uid`) apply to **process groups**, not Kubernetes nodes. To include or exclude Kubernetes nodes or hosts from monitoring, you must define Kubernetes label rules. If you only configure resource attribute rules, Kubernetes nodes may continue to be monitored and generate usage even when the related process groups are excluded.

### Define rules

You can define new monitoring rules through the [Dynatrace web UI](#new-ui) or the [Settings API](#new-api).

#### In Dynatrace

Process rules

Kubernetes node and host rules

1. In Dynatrace, go to **Settings** > **Application Security** > **New monitoring rules: Third-party**.
2. In the **Resource attribute monitoring rules (â¦)** tab, select **Add new rule**.
3. Follow the on-screen instructions.

   A condition's key and value fields are **free text fields**. On-screen suggestions aren't mandatory.
4. Select **Preview matching process group instances** to verify if the condition matches the expected processes.

   All conditions of a rule must match for the rule to apply.
5. Select **Save changes**.

1. In Dynatrace, go to **Settings** > **Application Security** > **New monitoring rules: Third-party**.
2. In the **Kubernetes monitoring rules (â¦)** tab, select **Add new rule**.
3. Follow the on-screen instructions.

   A condition's key and value fields are **free text fields**. On-screen suggestions aren't mandatory.
4. Select **Preview matching Kubernetes nodes and hosts** to verify if the condition matches the expected Kubernetes nodes and hosts.

   All conditions of a rule must match for the rule to apply.
5. Select **Save changes**.

To start monitoring based on your preferred monitoring criterion, make sure it's [activated](#activate).

You can edit, disable, enable, or remove rules at any time.

#### Via Settings API

You can read or modify the rules using the Settings API.

Process rules

Kubernetes node and host rules

* To view a monitoring rule, use the [GET an object](/docs/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.") request. Set the following parameters:

  + `schemaIds=builtin:appsec.third-party-vulnerability-rule-settings`
  + `scopes=tenant`

  Example JSON response

  ```
  {



  "items": [



  {



  "objectId": "vu9U3hXa3q0AAAABADZidWlsdGluOmFwcHNlYy50aGlyZC1wYXJ0eS12dWxuZXJhYmlsaXR5LXJ1bGUtc2V0dGluZ3MABnRlbmFudAAGdGVuYW50ACQ1YWYzOWNiZC0xM2I0LTNlZmItYTViYi1iYzljNTgyOTQxNze-71TeFdrerQ",



  "value": {



  "enabled": true,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_OFF"



  },



  "resourceAttributeConditions": [



  {



  "resourceAttributeKey": "dt.entity.host",



  "matcher": "EQUALS",



  "resourceAttributeValue": "HOST-ABD42981B3D483AC"



  }



  ],



  "metadata": {



  "comment": ""



  }



  }



  },



  {



  "objectId": "vu9U3hXa3q0AAAABADZidWlsdGluOmFwcHNlYy50aGlyZC1wYXJ0eS12dWxuZXJhYmlsaXR5LXJ1bGUtc2V0dGluZ3MABnRlbmFudAAGdGVuYW50ACQ4NDQ1OGRjNC1lM2Q2LTM2MGYtOWQyYy1lNmYwMTY1MzAwMza-71TeFdrerQ",



  "value": {



  "enabled": false,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_ON"



  },



  "resourceAttributeConditions": [



  {



  "resourceAttributeKey": "attribute_2",



  "matcher": "EXISTS"



  }



  ],



  "metadata": {



  "comment": ""



  }



  }



  },



  {



  "objectId": "vu9U3hXa3q0AAAABADZidWlsdGluOmFwcHNlYy50aGlyZC1wYXJ0eS12dWxuZXJhYmlsaXR5LXJ1bGUtc2V0dGluZ3MABnRlbmFudAAGdGVuYW50ACRjNzk3M2I4YS1kYmFjLTMxMzAtYjdjMy0zYjYxNGMxOWU1NzK-71TeFdrerQ",



  "value": {



  "enabled": false,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_OFF"



  },



  "resourceAttributeConditions": [



  {



  "resourceAttributeKey": "my.app.name",



  "matcher": "EQUALS",



  "resourceAttributeValue": "cool-app"



  }



  ],



  "metadata": {



  "comment": ""



  }



  }



  }



  ],



  "totalCount": 3,



  "pageSize": 100



  }
  ```
* To modify a monitoring rule, use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request.

  Example JSON body

  ```
  [



  {



  "value": {



  "enabled": true,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_OFF"



  },



  "resourceAttributeConditions": [



  {



  "resourceAttributeKey": "dt.entity.host",



  "matcher": "EQUALS",



  "resourceAttributeValue": "HOST-ABD42981B3D483AC"



  }



  ],



  "metadata": { "comment": "" }



  },



  "schemaId": "builtin:appsec.third-party-vulnerability-rule-settings",



  "scope": "tenant"



  },



  {



  "value": {



  "enabled": false,



  "vulnerabilityDetectionControl": { "monitoringMode": "MONITORING_ON" },



  "resourceAttributeConditions": [



  {



  "resourceAttributeKey": "attribute_2",



  "matcher": "EXISTS"



  }



  ],



  "metadata": { "comment": "" }



  },



  "schemaId": "builtin:appsec.third-party-vulnerability-rule-settings",



  "scope": "tenant"



  },



  {



  "value": {



  "enabled": false,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_OFF"



  },



  "resourceAttributeConditions": [



  {



  "resourceAttributeKey": "my.app.name",



  "matcher": "EQUALS",



  "resourceAttributeValue": "cool-app"



  }



  ],



  "metadata": {



  "comment": ""



  }



  },



  "schemaId": "builtin:appsec.third-party-vulnerability-rule-settings",



  "scope": "tenant"



  }



  ]
  ```

* To view a monitoring rule, use the [GET an object](/docs/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.") request. Set the following parameters:

  + `schemaIds=builtin:appsec.third-party-vulnerability-kubernetes-label-rule-settings`
  + `scopes=tenant`

  Example JSON response

  ```
  {



  "items": [



  {



  "objectId": "vu9U3hXa3q0AAAABAEdidWlsdGluOmFwcHNlYy50aGlyZC1wYXJ0eS12dWxuZXJhYmlsaXR5LWt1YmVybmV0ZXMtbGFiZWwtcnVsZS1zZXR0aW5ncwAGdGVuYW50AAZ0ZW5hbnQAJDBhZDRhNTRjLWY3MDMtM2M2OC1iOTQ5LTkxNTA2YTc2Mzc5Zr7vVN4V2t6t",



  "value": {



  "enabled": true,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_ON"



  },



  "kubernetesLabelConditions": [



  {



  "kubernetesLabelKey": "dummy-label",



  "matcher": "CONTAINS",



  "kubernetesLabelValue": "HOST"



  },



  {



  "kubernetesLabelKey": "dummy-label",



  "matcher": "STARTS_WITH",



  "kubernetesLabelValue": "value:"



  },



  {



  "kubernetesLabelKey": "dummy-label",



  "matcher": "EQUALS",



  "kubernetesLabelValue": "HOST-1C2B7B7A2613CBFD"



  }



  ],



  "metadata": {



  "comment": ""



  }



  }



  }



  ],



  "totalCount": 1,



  "pageSize": 100



  }
  ```
* To modify a monitoring rule, use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request.

  Example JSON body

  ```
  [



  {



  "value": {



  "enabled": true,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_OFF"



  },



  "kubernetesLabelConditions": [



  {



  "kubernetesLabelKey": "kubernetes.io/os",



  "matcher": "EQUALS",



  "kubernetesLabelValue": "linux"



  }



  ],



  "metadata": {



  "comment": ""



  }



  },



  "schemaId": "builtin:appsec.third-party-vulnerability-kubernetes-label-rule-settings",



  "scope": "tenant"



  },



  {



  "value": {



  "enabled": true,



  "vulnerabilityDetectionControl": {



  "monitoringMode": "MONITORING_OFF"



  },



  "kubernetesLabelConditions": [



  {



  "kubernetesLabelKey": "dummy-label",



  "matcher": "CONTAINS",



  "kubernetesLabelValue": "HOST"



  },



  {



  "kubernetesLabelKey": "dummy-label",



  "matcher": "STARTS_WITH",



  "kubernetesLabelValue": "value:"



  },



  {



  "kubernetesLabelKey": "dummy-label",



  "matcher": "EQUALS",



  "kubernetesLabelValue": "HOST-1C2B7B7A2613CBFD"



  }



  ],



  "metadata": {



  "comment": ""



  }



  },



  "schemaId": "builtin:appsec.third-party-vulnerability-kubernetes-label-rule-settings",



  "scope": "tenant"



  }



  ]
  ```

### Monitoring rules evaluation

After you add, edit, or remove a rule, it can take up to 10 minutes for changes to take effect throughout the system. The configured monitoring rules are evaluated periodically (on internal worker runs) and on-demand (through calls to the REST API).

**Exception**: After an entity that was previously monitored is excluded from monitoring, it can take up to 70 minutes for changes to take effect throughout the system. For details, see [How host coverage is calculated](/docs/secure/application-security/vulnerability-analytics/application-security-overview#calculation "Get an overview of the security issues of your third-party libraries.").

Regardless of the calling context, the rule evaluation stays the same: given a set of entities, the algorithm decides whether a specific entity should be monitored. The rules are processed in order until the first match.

* If a rule matches a specific entity, the configured mode (**Monitor** or **Do not monitor**) is used and subsequent rules aren't evaluated for this particular entity.
* If no rule matches a specific entity, the configured default mode (**Monitor** or **Do not monitor**) is used.

### Use cases

For some common scenarios for defining monitoring rules, see [Use cases for monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/use-cases-monitoring-rules "Common scenarios for defining monitoring rules for vulnerabilities based on resource attributes and Kubernetes labels.").

## Classic monitoring rules

Although classic rules based on management zones and tags still work, they are scheduled for deprecation. We strongly recommend migrating to the [new rules based on resource attributes or Kubernetes labels](#new). Automatic migration isn't possible; for details, see [FAQ](#migrate).

Classic monitoring rules are based on process group tag, host tag, and management zones.

### Define rules

You can define classic monitoring rules through the [Dynatrace web UI](#classic-ui) or the [Settings API](#classic-api).

#### In Dynatrace

To add a new rule

1. Go to **Settings** > **Application Security** > **Vulnerability Analytics** > **Monitoring rules: Third-party**.
2. Select **Add new rule** to add a new rule.
3. Enter the requested information (mode, property, condition operator, and condition value).

   The `Process tag` property applies to process groups, not processes.
4. Select **Save changes**.

You can edit, disable, enable, or remove rules at any time.

#### Via Settings API

You can read or modify the rules using the Settings API.

* To view a monitoring rule, use the [GET an object](/docs/dynatrace-api/environment-api/settings/objects/get-object "View a settings object via the Dynatrace API.") request. Set the following parameters:

  + `schemaIds=builtin:appsec.rule-settings`
  + `scopes=tenant`

  Example JSON response

  ```
  {



  "items": [



  {



  "objectId": "vu9U3hXa3q0AAAABABxidWlsdGluOmFwcHNlYy5ydWxlLXNldHRpbmdzAAZ0ZW5hbnQABnRlbmFudAAkYTc4NjY0NGItZmVjNC0zNzliLWI0MWItNThmYzgzOWZmYWY5vu9U3hXa3q0",



  "value": {



  "enabled": true,



  "mode": "MONITORING_OFF",



  "property": "PROCESS_TAG",



  "operator": "EQUALS",



  "value": "super secret process"



  }



  },



  {



  "objectId": "vu9U3hXa3q0AAAABABxidWlsdGluOmFwcHNlYy5ydWxlLXNldHRpbmdzAAZ0ZW5hbnQABnRlbmFudAAkNDhkZGYxNDMtYzc2Mi0zYzIwLWI1ODAtNTNhODEwOGZlMDBivu9U3hXa3q0",



  "value": {



  "enabled": true,



  "mode": "MONITORING_ON",



  "property": "HOST_TAG",



  "operator": "NOT_EQUALS",



  "value": "Test"



  }



  },



  {



  "objectId": "vu9U3hXa3q0AAAABABxidWlsdGluOmFwcHNlYy5ydWxlLXNldHRpbmdzAAZ0ZW5hbnQABnRlbmFudAAkNmY1NjZkNmItYWMyNy0zOTg2LWE1OGItNTU2ZTI1NTE5NTcyvu9U3hXa3q0",



  "value": {



  "enabled": false,



  "mode": "MONITORING_ON",



  "property": "MANAGEMENT_ZONE",



  "operator": "EQUALS",



  "value": "Monitorme"



  }



  }



  ],



  "totalCount": 3,



  "pageSize": 100



  }
  ```
* To modify a monitoring rule, use the [POST an object](/docs/dynatrace-api/environment-api/settings/objects/post-object "Create or validate a settings object via the Dynatrace API.") request.

  Example JSON body

  ```
  [



  {



  "value": {



  "enabled": true,



  "mode": "MONITORING_ON",



  "property": "HOST_TAG",



  "operator": "EQUALS",



  "value": "REST"



  },



  "scope": "tenant",



  "schemaId": "builtin:appsec.rule-settings"



  },



  {



  "value": {



  "enabled": true,



  "mode": "MONITORING_OFF",



  "property": "PROCESS_TAG",



  "operator": "NOT_EQUALS",



  "value": "Test-Process"



  },



  "scope": "tenant",



  "schemaId": "builtin:appsec.rule-settings"



  }



  ]
  ```

For Kubernetes environments, you need to add tags both on the host and on the Kubernetes node.

### Monitoring rules evaluation

* After you add, edit, or remove a rule, it can take up to 15 minutes for changes to take effect throughout the system. The configured monitoring rules are evaluated periodically (on internal worker runs) and on-demand (through calls to the REST API).

  Regardless of the calling context, the rule evaluation stays the same: given a set of entities, the algorithm decides whether a specific entity should be monitored. The rules are processed in order until the first match. Note that each rule must be unique.
* When you have a rule in place for a management zone or tag, and you add an entity to the same management zone or add the same tag to an entity, it can take up to 15 minutes until the change is reflected in your monitoring rule.

  For example, if you have a `Do not monitor if host tag equals 'testsystem'` rule, and you add the tag `testsystem` to a host, it can take up to 15 minutes until the newly tagged host stops being monitored.
* If a rule matches a specific entity, the configured mode (`Monitor`, `Do not monitor`) is used and subsequent rules are not evaluated for this particular entity.
* If no rule matches a specific entity, the [global third-party vulnerability detection control mode](/docs/secure/application-security/vulnerability-analytics#config-tpv "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") is used.

## Coverage impact

Monitoring rules directly influence host and process coverage. If a host or process group is excluded by a rule, it won't be monitored for vulnerabilities.

To review how your monitoring rules affect overall coverage, see [Assess coverage](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

## FAQ

### Does the order of the rules matter?

The order of the monitoring rules is important: As soon as a rule matches an entity, the entity won't be considered by any of the later rules. Consequently, **specific rules should come before general rules.**

### Can existing classic monitoring rules be automatically migrated to the new ones?

Automatic migration from the classic to the new monitoring rules isn't possible. You need to recreate the rules, or you can [create new rules](#setup-new) from scratch.

### Is process restart required after enabling or disabling a monitoring rule?

Classic monitoring rules

No restart is required. For more information, see [FAQ: Is restart required after enabling or disabling an Application Security feature or functionality?](/docs/secure/faq#restart-requirements "Frequently asked questions about Dynatrace Application Security.")

### What happens if a **Do not monitor** rule that applies gets added?

New monitoring rules Classic monitoring rules

* New vulnerabilities for the processes that match the rule won't be created.
* Existing vulnerabilities that only relate to matching processes are resolved.

### What happens if a **Do not monitor** rule is deleted or doesn't apply anymore?

New monitoring rules Classic monitoring rules

* New vulnerabilities for the processes that match the rule will be created.
* Related resolved vulnerabilities are reopened.

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: filter-third-party-vulnerabilities.md


---
title: Filter or change status of third-party vulnerabilities
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities
scraped: 2026-02-15T21:21:25.909284
---

# Filter or change status of third-party vulnerabilities

# Filter or change status of third-party vulnerabilities

* Explanation
* Updated on Jun 03, 2023

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated. If you're currently using this app, we recommend transitioning to the corresponding [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Vulnerabilities upgrade guide](/docs/secure/application-security/vulnerability-analytics/vulnerabilities-upgrade-classic-to-latest "Upgrade from the classic Thirdâparty and Codeâlevel vulnerabilities apps to the Vulnerabilities app in the latest Dynatrace.").

Once you [enable third-party vulnerability detection](/docs/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") and see the [list of third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#list "Monitor the security issues of your third-party libraries.") appear in ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**, there are several ways you can organize them for easy management and to prioritize issues:

## Filter vulnerabilities

You can filter vulnerabilities by

* [Recommended fixes](#dsa)
* [Vulnerability details](#details), [global timeframe](#timeframe), and [management zone](#management-zones) (you can combine any of these filters)

### Filter by recommended fixes with Davis Security Advisor

To filter by recommended fixes, on the **Third-party vulnerabilities** page, select an upgrade and then select **Add as filter**.

* After adding a recommended fix as a filter, you can extend filtering by [vulnerability details](#details).
* You can add multiple filters for recommended fixes all at once. In this case, you get a cumulated list of vulnerabilities based on the selected fixes.
* If you use the management zones filter, you'll get a list of third-party vulnerabilities that affect the selected management zone.

You won't receive recommendations for

* Muted vulnerabilities
* Vulnerabilities filtered by the global filter in a past timeframe
* Resolved vulnerabilities

For more information about Davis Security Advisor, see [Davis Security Advisor calculations](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.").

### Filter by vulnerability details

In the filter bar, the following filters are available.

You can combine any of the filters, but you cannot use the same filter more than once per search.

* **Risk assessment**:

  + `Public internet exposure`: Displays vulnerabilities that affect at least one process that is exposed to the internet.

    This filter isn't available for vulnerabilities in the Kubernetes technology.
  + `Reachable data assets`: Displays vulnerabilities that affect at least one process that has database access.

    This filter isn't available for vulnerabilities in the Kubernetes technology.
  + `Public exploit published`: Displays vulnerabilities that are exploited by known malicious code.
  + `Vulnerable functions in use`: Displays vulnerabilities that have any vulnerable functions in use by a process (this might indicate a higher exploitation risk).
  + `Reduced accuracy`: Displays vulnerabilities that have related hosts running in Infrastructure Monitoring mode or OneAgent Discovery mode. For details, see [Monitoring modes](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
* **Risk level**: Displays vulnerabilities based on their severity (`Critical`, `High`, `Medium`, `Low`, `None`).

For details about risk levels, see [Davis Security Score calculations](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.").

* **Snyk/CVE ID**: Displays a particular vulnerability based on

  + The Snyk ID (for example, `SNYK-JAVA-ORGAPACHEXMLBEANS-1060048`), for Snyk-based vulnerabilities.
  + The CVE ID (for example, `CVE-2017-5645`), for NVD-based vulnerabilities.
* **Status**:

  + `Open`: Displays active vulnerabilities.
  + `Resolved`: Displays vulnerabilities that have been closed automatically because the root cause (for example, loading a vulnerable library) is no longer present. For more information, see [Vulnerability evaluation: Resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").
  + `Muted`: Displays the active and resolved vulnerabilities that have been silenced by request.
* **Technology**: Displays vulnerabilities in one of the supported technologies (`Kubernetes`, `Node.js`,`Java`, `.NET`, `PHP`, `Python`, `Go`).
* **Technology runtimes**: Displays only library-based (`only vulnerable libraries`) or runtime-based (`only vulnerable runtimes`) vulnerabilities.
* **Vulnerable component**: Displays vulnerabilities based on part of a vulnerable component name.
* **Vulnerability ID**: Displays a particular vulnerability by selecting its Dynatrace-provided ID (for example, `S-4423`).
* **Affected or related entity**: Displays vulnerabilities that affect or relate to specific entities. Select and enter any combination of the following: `Process group name`, `Host name`, `Kubernetes workload name`, `Kubernetes cluster name`, `Tag`. For `Tag`, you can use tags on a host, process, and process group, with the syntax `key:value` or `key`. For more information about tagging, see [Define and apply tags](/docs/manage/tags-and-metadata/setup/how-to-define-tags "Find out how to define and apply tags manually and automatically.").

  If a vulnerability affects more than 5,000 processes, the **Affected or related entity** filter may not be able to find all vulnerabilities impacted by the entered entity.

### Filter by global timeframe

You can use the global timeframe selector to filter third-party vulnerabilities on the following pages:

* On the **Third-party vulnerabilities** page, it displays vulnerabilities that were open within the selected global timeframe. However, the data displayed about an entry reflects the current status of the entry, not the historical status.
* On the vulnerability details page, it displays entities that were affected and libraries that were vulnerable during the selected global timeframe. An affected entity or a vulnerable component is shown:

  + If it was already affected or vulnerable during the selected timeframe.
  + If it's still affected or vulnerable.

### Filter by management zone

You can use the management zones filter on the **Third-party vulnerabilities** list and details pages.

#### How the filter applies

For each case, the filter applies to different components:

* On the **Third-party vulnerabilities** page

  + Filtering by management zone applies only to the **Vulnerability** field.
  + Data in all the other vulnerability fields is based on the whole environment.
* On the third-party vulnerability details page

  + Filtering by management zone applies only to the **Vulnerable components** and **Related entities** sections.
  + Data in all the other sections is based on the whole environment.

#### How management zones are calculated

Management zone calculation is based on processes (or Kubernetes node, in the case of Kubernetes vulnerabilities). Management zones are calculated when a vulnerability is opened and every 15 minutes after that until the vulnerability is resolved. A management zone is affected by a vulnerability if a process (or Kubernetes node, in the case of Kubernetes vulnerabilities) of the management zone uses a vulnerable component that has the reported vulnerability.

#### How resolved vulnerabilities behave

* When a vulnerability stops affecting a management zone, it won't show up when you filter for that management zone.
* When a vulnerability is resolved (when it has stopped affecting the whole environment), it shows up regardless of the selected management zone.

#### Management zone limitations

A maximum of 1,000 management zones are stored for a vulnerability. If a vulnerability affects more than 1,000 management zones, you are only able to filter for the 1,000 management zones that are stored with the vulnerability.

## Change vulnerability status

### Options to change status

You can:

* **Mute** (silence) vulnerabilities that are

  + Open, if you don't consider them important
  + Resolved, if you don't want to deal with them if they are reopened
* **Unmute** vulnerabilities that are muted, if you consider them important.
* **Change the vulnerability status** by selecting a new reason for the current status or adding more information to the current status.

* Muted vulnerabilities don't appear on the list of vulnerabilities unless you filter for `Status: muted`.
* Unmuting an open vulnerability makes it active againâits status changes back to `Open`, and the vulnerability shows up again in the list of vulnerabilities.
* Unmuting a resolved vulnerability changes its status back to `Resolved`, and the vulnerability shows up again in the list of vulnerabilities when you filter for `Resolved` vulnerabilities.

### Ways to change status

You can change the vulnerability status individually or in bulk:

* **Individually** (one vulnerability at a time). You have two options:

  + On the **Third-party vulnerabilities** page, under the **Details** for the selected vulnerability, select **Change status**, select the new status, enter any additional information, and then select **Save**.
  + On the third-party vulnerability details page, in the upper-right corner of the page, select **Change status**, select the new status, enter any additional information, and then select **Save**.
* **In bulk** (for multiple vulnerabilities at once, for example based on specific [filters](#details)). On the **Third-party vulnerabilities** page, you have two options:

  + Select multiple vulnerabilities that are displayed on one page (select the vulnerabilities you want, then select **Yes, change status**, select the new status, enter any additional information, and then select **Save**).
  + Select all vulnerabilities that are displayed on one page (select the **Vulnerability** column in the vulnerabilities list, then select **Yes, change status**, select the new status, enter any additional information, and then select **Save**).

  The option to perform bulk changes isn't available to users with view-only access. The **Manage security problems** permission is required. For details on permission management, see [Fine-tune permissions](/docs/secure/application-security#restrict-permissions "Access the Dynatrace Application Security functionalities.").

You need to wait up to a minute for the changes to take effect. Refresh the page to see your changes.

### Show status changes

The last five status changes of the vulnerability are logged in the **Vulnerability evolution** section of a vulnerability details page.

* Select **Show more** for the next five status changes.
* Select **Details** to see who changed the status of the vulnerability, the reason for changing the status, and any additional comments.

## Related topics

* [Vulnerabilities API](/docs/dynatrace-api/environment-api/application-security/vulnerabilities "Find out what the vulnerabilities API offers.")
* [Davis Security Advisor API](/docs/dynatrace-api/environment-api/application-security/davis-security-advice "View the Davis Security Advisor recommendations via Dynatrace API.")
* [Management zones](/docs/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.")
* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: manage-third-party-vulnerabilities.md


---
title: Manage third-party vulnerabilities
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities
scraped: 2026-02-15T21:21:23.422505
---

# Manage third-party vulnerabilities

# Manage third-party vulnerabilities

* Explanation
* Updated on Sep 10, 2025

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated. If you're currently using this app, we recommend transitioning to the corresponding [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Vulnerabilities upgrade guide](/docs/secure/application-security/vulnerability-analytics/vulnerabilities-upgrade-classic-to-latest "Upgrade from the classic Thirdâparty and Codeâlevel vulnerabilities apps to the Vulnerabilities app in the latest Dynatrace.").

A third-party vulnerability is a security problem detected in the third-party libraries loaded in your environment. After you [enable and configure Dynatrace Runtime Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), Dynatrace starts monitoring your applications to detect vulnerabilities in third-party libraries.

## Third-party vulnerabilities list

To see a list of all detected third-party vulnerabilities in your environment, go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.
The following information is displayed.

### General overview of the key features

![key-feat-tpv](https://dt-cdn.net/images/2023-03-14-09-14-17-1579-32c8119346.png)

The numeric values displayed are management-zone aware.

* The number of open vulnerabilities (and the muted ones). Select it to display the vulnerabilities filtered by `Status: Open`.
* The number of critical and high vulnerabilities. Select it to display the open vulnerabilities filtered by `Risk level: Critical` or `Risk level: High`.
* The number of monitored technologies out of the total number of supported technologies. Select **Monitored technologies** to view and [edit your settings](/docs/secure/application-security/vulnerability-analytics#technology "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").
* A visual representation of each technology.

### Davis Security Advisor

![dsa-tpv](https://dt-cdn.net/images/2023-03-14-09-18-22-1575-8bbc0c397f.png)

The Davis Security Advisor recommends the fixes that would most improve the overall security of your environment. For details, see [Davis Security Advisor calculations](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.").

### Vulnerabilities detected

![Third-party vulnerability list](https://dt-cdn.net/images/2024-02-14-09-27-51-1575-70c71f9742.png)

A list of all detected third-party vulnerabilities in your environment.
For optimized performance, a maximum of 500 vulnerabilities are displayed at a time. You can narrow down the results by applying [filters](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#filter "Organize third-party vulnerabilities for easy management and to prioritize issues.").
To sort the list by any item, select the corresponding column heading. To add or remove column headings, select **Format table**.

#### Vulnerability

* The vulnerability ID provided by Dynatrace (example: `S-3440`)
* Depending on the vulnerability feed:

  + For [Snykï»¿](https://snyk.io) vulnerabilities, the Snyk name (example: `Denial of Service (DoS)`)
  + For [NVDï»¿](https://nvd.nist.gov/vuln) vulnerabilities, the [CVEï»¿](https://cve.mitre.org/) ID (example: `CVE-2020-2805`), or the [CWEï»¿](https://cwe.mitre.org/) name, if available (example: `Deserialization of Untrusted Data`)

    - One vulnerability in Dynatrace can have multiple CVEs (for example, if different vendors release their own CVEs).
    - There can be different vulnerabilities for one component (library).
    - One security problem can generate multiple Dynatrace vulnerabilities, one for each affected technology.
* The vulnerable component (the software component (library) or runtime component (for example, a Kubernetes package) that has a vulnerable function causing a vulnerability):

  + For Snyk-based vulnerabilities, the package name (example: `org.apache.tomcat:tomcat-coyote`)
  + For NVD-based vulnerabilities, the runtime technology (examples: `Java runtime`, `Node.js runtime`)

To find out how Dynatrace evaluates components, see [How vulnerabilities are evaluated: Third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

#### Davis Security Score

* The Davis Security Score risk level (`Critical`, `High`, `Medium`, `Low`, `None`) of the vulnerability, based on the [Common Vulnerability Scoring System (CVSS) scoreï»¿](https://en.wikipedia.org/wiki/Common_Vulnerability_Scoring_System) of the vulnerability and AI-enhanced to take public internet exposure and reachable data assets into consideration. If a vulnerability has been resolved, the symbol color is green.
* The overall risk assessment (the [final score](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.")).
* If there is any **public internet exposure** (the vulnerability affects at least one process that is exposed to the internet). To find out how Dynatrace determines public internet exposure, see [FAQ: How is public internet exposure determined?](/docs/secure/faq#internet-exposure "Frequently asked questions about Dynatrace Application Security.").
  If the symbol is grayed out and crossed out, no public internet exposure was found. If the symbol isn't present, no data is available.
* If there are any **reachable data assets** (the vulnerability affects a process that has database access, based on the [Dynatrace entity model (Smartscape)](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.")). If the symbol is grayed out and crossed out, there are no reachable data assets within range. If the symbol isn't present, no data is available.
* If there is any **vulnerable function** in use by a process, which allows the vulnerability to be exploited. If the symbol is grayed out and crossed out, there's no vulnerable function in use. If the symbol isn't present, no data is available.
* If there is any **public exploit** (a known malicious code that exploits this vulnerability). If the symbol is grayed out and crossed out, there's no public exploit. If the symbol isn't present, no data is available.

#### CVSS score

The base CVSS score of the vulnerability. This column is hidden by default and can be enabled via **Format table**.

#### Status

* **Open:** The vulnerability is active.
* **Resolved:** The vulnerability has been closed automatically because the root cause (for example, loading a vulnerable library) is no longer present. For more information, see [Vulnerability evaluation: Resolution](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#tpv-resolution "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").
* **Muted - Open:** The vulnerability is active but has been silenced by request.
* **Muted - Resolved:** The silenced active vulnerability has been closed automatically because the root cause (for example, loading a vulnerable library) is no longer present.

  A muted vulnerability that has been closed automatically doesn't change its status to `Resolved`, but to `Muted - Resolved`.

#### Affected entities

The entities (process groups, Kubernetes nodes) that are affected by the identified third-party vulnerability.

#### Technology

The technology of the process affected by the vulnerability.

To display this column, select **Format table** and add **Technology** to the list.

#### First detected

When Dynatrace first detected the third-party vulnerability.

#### Last update

Timestamp of the last status change of the third-party vulnerability. A status change can be when:

* The vulnerability is resolved or reopened
* The vulnerability is muted or unmuted
* The number of affected process groups has decreased or increased
* The risk assessment has changed
* The Davis Security Score has changed
* A new software component is detected

For details, see [FAQ: What does "last update" refer to?](/docs/secure/faq#last-update "Frequently asked questions about Dynatrace Application Security.").

To display this column, select **Format table** and add **Last update** to the list.

#### Details

Expand ![Expand row](https://dt-cdn.net/images/expand-row-icon-9c4950fc2e.svg "Expand row") vulnerability rows for details, or to perform the following actions:

* Select **Change status** to mute, unmute, or mute again a vulnerability with a different reason or comment.
* Select **View process group overview** to navigate to the overview page of the process groups related to a vulnerability.
* Select **View vulnerability details** to navigate to the details page of a vulnerability.

## Third-party vulnerability details

To see details about a third-party vulnerability, go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** and select a vulnerability.
The following information is displayed.

### Vulnerability title

* Software components use the Snyk feed. In this case, the vulnerability title displays the Snyk name and ID, the `third-party vulnerability` attribute, and when the vulnerability was first detected.

  Example

  ![Example title third-party vulnerability from Snyk feed](https://dt-cdn.net/images/2022-11-10-15-14-25-757-52f792fe88.png)
* Runtime components use the NVD feed[1](#fn-1-1-def). In this case, the vulnerability title displays one of the following.

  + The CWE name and CVE ID, the `runtime vulnerability` attribute, and when the vulnerability was first detected.

  Example

  ![Example title runtime vulnerability from NVD feed (1)](https://dt-cdn.net/images/2023-03-16-11-05-48-600-64b719a6b0.png)

  + The CVE ID, the `runtime vulnerability` attribute, and when the vulnerability was first detected.

  Example

  ![Example title runtime vulnerability from NVD feed (2)](https://dt-cdn.net/images/2023-03-16-09-57-39-609-c1b0c63b4a.png)

  1

  With the exception of Kubernetes runtime components, which use the Snyk feed. For details, see [Third-party vulnerability feeds](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#vulnerability-feeds "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

### Shortcut to main topics

![shortcut-vuln-evolution](https://dt-cdn.net/images/shortcut-vuln-evolution-383-d999d9ffc9.png)

Expand the button next to **Settings** on the upper-left side of the vulnerability details page to select one of the topics below.

* **Vulnerability details**
* **Related entities**
* **Vulnerability evolution**
* **Vulnerable components**

Select **Settings** to navigate to **Vulnerability Analytics: General settings**. For details, see [Get started with Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

### Infographic of the key features

![Infographic of the key features](https://dt-cdn.net/images/2024-02-14-13-36-38-1333-f22b2ab724.png)

Select any of these features to jump to the corresponding section on the page.

* [**Risk level:**](#dss) Davis Security Score risk level (`Critical`, `High`, `Medium`, `Low`, `None`).
* **Public internet exposure:** If there's any public internet exposure. Possible states are:

  + **Public network:** There is public internet exposure.
  + **Not detected:** No public internet exposure was found.
  + **Not available:** Data isn't available, because the related hosts are running in Infrastructure Monitoring mode. For details, see [Monitoring modes](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
* [**Reachable data assets:**](#data-assets) If there are any reachable data assets affected. Possible states are:

  + **Within range:** There are reachable data assets affected.
  + **None within range:** There are no reachable data assets within range.
  + **Not available:** Data isn't available, because the related hosts are running in Infrastructure Monitoring mode. For details, see [Monitoring modes](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").
* [**Vulnerable functions:**](#vulnerability-details) If there are any vulnerable functions in use. Possible states are:

  + **In use:** There are vulnerable functions in use.
  + **Not in use:** No vulnerable functions in use were found.
  + **Not available:** Data isn't available. For a list of potential reasons, see [FAQ](#faq).
* **Exploit:** If there's any malicious code that exploits the third-party vulnerability. Possible states are:

  + **Public exploit published:** A publicly known exploit for this vulnerability is available.
  + **No public exploit published:** No publicly known exploit for this vulnerability is available.
* [**Process groups:**](#pg) How many process groups are affected
* [**Vulnerable component:**](#components) The name of the vulnerable component

If you want to [change the status of a vulnerability](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities#mute "Organize third-party vulnerabilities for easy management and to prioritize issues."), select **Change status** in the upper-right corner of the page.

### Vulnerability details

![vuln-details-snyk-feed](https://dt-cdn.net/images/2022-11-11-8-59-22-910-e337d9f503.png)

* The name and description of the affected package (example: `com.fasterxml.jackson.core:jackson-databind`), the associated technology (example: `Java`), and links to the Snyk/CVE/CWE/OWASP IDs for further information.

#### Fix recommendation

For vulnerabilities based on the [Snykï»¿](https://snyk.io/) feed, a fix recommendation is displayed if one is available. It consists of a library upgrade suggestion to solve the vulnerability.

![fix recommendation from snyk](https://dt-cdn.net/images/2024-05-17-07-34-40-800-7bdff77acd.png)

Make sure to restart processes after upgrading a library.

#### Vulnerable functions

The exact classes (example: `com.fasterxml.jackson.databind.jsontype.impl.SubTypeValidator`) and functions (example: `validateSubType`) causing the vulnerability, and the affected process groups based on the function usage.

This section is not displayed

* If no vulnerable function information is provided by Snyk or the Dynatrace security research team.
* For runtime vulnerabilities, which are based on the NVD feed.

**Function usage** shows whether the vulnerable function is being used by your application. Based on whether your application uses the vulnerable function, you can assess the impact on your environment. The usage of a vulnerable function is calculated on the process level and is aggregated to the process group level, which results in a count of affected process groups per function.

* **In use:** A count of the related process groups that are affected by the vulnerability (use at least one vulnerable function). Select the number of affected process groups to navigate to [remediation tracking](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.").
* **Not in use:** A count of related process groups that don't use any vulnerable function.
* **Not available:** A count of related process groups for which the vulnerable function usage could not be determined. For a list of potential reasons, see [FAQ](#faq).

  The information is based on management zones, not on the timeframe.

#### How it works

* If Snyk or the Dynatrace security research team provides information about the vulnerable function, and OneAgent monitoring for Java vulnerable functions is enabled, OneAgent determines whether the vulnerable function is in use.

  Example:

  ![usage-oa-enabled](https://dt-cdn.net/images/usage-oa-enabled-916-5b2cbd3f7d.png)
* If Snyk or the Dynatrace security research team provides information about the vulnerable function, but the OneAgent feature is disabled, the number of vulnerable functions is displayed as **Not available**.

  Example:

  ![usage-oa-disabled](https://dt-cdn.net/images/usage-oa-disabled-1008-0ff9e7d45b.png)

For instructions on how to enable OneAgent monitoring, see [Enable OneAgent monitoring for Java vulnerable functions](/docs/secure/application-security/vulnerability-analytics#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

Restart required

If information about vulnerable functions is outdated, you are prompted to restart processes so that OneAgent can pick up and use the new data. The following message is displayed: `Restart required: Restart the process(es) for updated vulnerable function data.`

Example:

![Restart required on vulnerability details page](https://dt-cdn.net/images/2023-12-18-09-34-40-778-11c7311d23.png)

For more information, such as how determine which processes you need to restart, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

### Davis Security Score

![Davis Security Score](https://dt-cdn.net/images/2024-02-14-13-41-24-780-f51f2513e9.png)

A detailed view of [how the Davis Security Score for the opened vulnerability is calculated](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI."): starting from the CVSS from Snyk, Davis checks whether there is public internet exposure or reachable data affected and, if so, to what extent. The score is then adjusted as applicable based on the [Davis AI calculations](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.").

### Reachable data assets

![reachable-assets-tpv-details](https://dt-cdn.net/images/2022-11-11-10-52-09-767-41a1d8055c.png)

The last five database services accessed by affected processes containing the identified vulnerability, based on the last hour. Select **View all** to navigate to **Databases**. For information on how to monitor your database performance, see [Databases](/docs/observe/infrastructure-observability/databases "Track the database performance and resources to create and maintain a high performing and available application infrastructure.").

### Vulnerability evolution

**Use case**: Have a better understanding of the evolution of a vulnerability over time.

The **Vulnerability evolution** section displays the following information.

#### Status

The current status of the vulnerability.

* For open vulnerabilities:

  + The current risk level and score (for example, `Critical risk vulnerability: 10.0`) and the time when the vulnerability was open (for example, `Opened 121 d 22 h ago (December 12 14:38)`).
  + The Davis Security Score compared to the base score (CVSS).
  + The current risk assessment (for example, `Public internet exposure detected`).
  + The number of affected processes (for example, `1 affected process (in 168 process groups)`) or, in the case of Kubernetes vulnerabilities, of affected nodes (for example, `1 affected node`).

  Example:

  ![Example status](https://dt-cdn.net/images/2024-02-14-13-46-42-781-2859677977.png)
* For resolved vulnerabilities, the current status and the time when the vulnerability was resolved.

  Example:

  ![Vulnerability evolution - Status for resolved vunerabilities](https://dt-cdn.net/images/2023-06-01-10-04-09-790-2333f1d4b5.png)

#### Latest events

The last 10 vulnerability status changes over the last 365 days.

If there are no status change events for over 365 days, this section is empty.

Possible status change events:

* A vulnerability is open, resolved or reopened. Displays the status change and the time when the change happened. For reopened vulnerabilities, select **Details** to see the risk assessment.

  Example events:

  ![Event change: Vulnerability resolved and reopened](https://dt-cdn.net/images/2024-02-14-13-51-21-780-a39fcba471.png)
* A vulnerability is muted or unmuted. Displays the user who performed the change, the reason for the change, any comments, and the time when the change was performed.

  Example event:

  ![Vulnerability status event change](https://dt-cdn.net/images/2023-06-01-09-48-47-781-8d47c443d9.png)
* The vulnerability risk assessment has changed. Displays the time when the change happened. Select **Details** to see the risk change. You can find out, for example, when a vulnerability that used to be exposed to the public internet is no longer exposed.

  Example event:

  ![Risk assessment change event](https://dt-cdn.net/images/2024-02-14-13-54-30-754-9d8d1bd7ed.png)
* The number of affected process groups or nodes, in the case of Kubernetes vulnerabilities, increased or decreased. Displays the number by which the affected process groups or nodes increased or decreased, the total number of affected process groups or nodes resulting from this change, and the time when this change happened. You can find out, for example, if you need to take action (if the number of affected entities is increasing) or if the vulnerability is being fixed (if the number of affected entities is decreasing).

  Example events for Kubernetes vulnerabilities:

  ![Event change in the number of nodes](https://dt-cdn.net/images/2023-06-01-08-00-01-783-4146d7278a.png)

  Example events for non-Kubernetes vulnerabilities:

  ![Event change in the number of process groups](https://dt-cdn.net/images/2023-06-01-08-06-56-787-7ba0129fde.png)
* Davis Security Score increased or lowered. Displays the new value and the time when this change happened.

  Example event:

  ![Davis Security Score event change](https://dt-cdn.net/images/2023-06-01-08-51-49-789-453e59edb5.png)
* CVSS increased or lowered. Displays the new value and the time when this change happened.

  Example event:

  ![CVSS score change event](https://dt-cdn.net/images/2023-06-01-15-07-48-916-4702d7421a.png)

### Related entities

![related-entities-tpv-details](https://dt-cdn.net/images/2022-11-11-11-01-23-773-87c1a45bfd.png)

The number of entities (applications, services, hosts, databases, Kubernetes workloads, or Kubernetes clusters) that are somehow connected to the identified vulnerability, based on the last hour, with links to the details page of the related entities:

* **Applications:** Applications that call a vulnerable service, or applications that call a non-vulnerable service that calls a vulnerable service.

  + Limitations: When determining related applications, the Dynatrace PurePathÂ® distributed traces are not analyzed.
* **Services:** Services that directly run on a vulnerable process group instance.
* **Hosts:** Hosts on which the vulnerable process runs.
* **Databases:** Databases that run on the vulnerable process.
* **Kubernetes workloads:** In Kubernetes environments, the workloads to which the vulnerable process belongs.
* **Kubernetes clusters:** In Kubernetes environments, the clusters to which the vulnerable process belongs.

The Kubernetes workloads and Kubernetes clusters sections are displayed only if Kubernetes workloads or clusters are detected.

The related entities displayed may be impacted by

* Security-monitoring rules
* Management zones
* Timeframe

### Vulnerable components

![vulnerable-components-tpv-details](https://dt-cdn.net/images/2022-11-11-11-14-51-775-93c7cf8329.png)

The name and description of the libraries containing the identified vulnerability, and the number of affected processes, based on the last hour.

### Related container image

![related-container-image-tpv-details](https://dt-cdn.net/images/2022-11-11-11-53-23-766-051380027a.png)

The top five related container images (image name and ID), based on the last hour, sorted by the number of affected processes.

This information is displayed only if containers are detected.

### Process group overview

![pg-overview-tpv-details](https://dt-cdn.net/images/2022-11-11-11-58-16-770-1240069b87.png)

Displays the following information, based on the last hour:

#### Process groups

* **Process groups in total:** The total number of process groups that are related (affected, resolved, and muted) to the identified vulnerability. It links to the overview page of the related process groups.
* **Affected process groups:** The number of affected process groups and the percentage of affected process groups out of the total number of related process groups. It links to the overview page of related process groups filtered by `Status: Affected`.

  + An affected process group is a process group that contains a vulnerable library or runtime.
  + The number of affected process groups matches the total count only if all functions in all used software component versions are vulnerable.

  Example

  A software component `A` is vulnerable to a vulnerability `X` in versions `1` and `2`.

  The function `f1` is only vulnerable in version `1`.

  There are two process groups:

  + Process group `PG1` uses the software component `A.1`, which includes the vulnerable function `f1`.
  + Process group `PG2` uses the software component `A.2`, which doesn't include any vulnerable function.

  The **Process groups overview** section on the details page of a vulnerability will show the vulnerable function `f1` with one process group (`PG1`) `In use` and `Not in use`. `PG2` is not considered because there is no vulnerable function in version `2`.
* **Resolved process groups:** The number of affected process groups that have been resolved and the percentage of resolved process groups out of the total number of related process groups. It links to the overview page of related process groups filtered by `Status: Resolved`.
* **Muted process groups:** The number of affected process groups that have been muted and the percentage of muted process groups out of the total number of related process groups. It links to the overview page of related process groups filtered by `Status: Muted`.
* A graph displaying the affected, resolved, and muted process groups, marked with different colors.

#### Processes

* **Processes total:** The total number of processes (affected and unaffected) out of the process groups where at least one process is affected.
* **Affected processes:** The number of affected processes.

  An affected process is a process that contains a vulnerable library or runtime. It can be exposed to the public internet or not.
* **Exposed:** The number of affected processes that are exposed to the public internet and the percentage of exposed processes out of the total number of affected processes.

#### Most affected process groups

Lists and links to the top five process groups, sorted by status (`Affected`, then `Resolved`, and then `Muted`) and amount of affected processes out of the total processes in the respective process group, and indicates if there is any public internet exposure, or if there are any reachable data assets. Select **View all process groups** to navigate to the overview page of the process groups related to a vulnerability.

## FAQ

* Why is there no data available for vulnerable functions?

  + See below for potential reasons why, on the **Third-party vulnerability** details page, in the [infographic of the key features](#key-features) and the [Vulnerability details section](#vulnerability-details), the **Not available** status is displayed for vulnerable functions.

    - Once you [enable Third-party Vulnerability Analytics](/docs/secure/application-security/vulnerability-analytics#enable-tpva "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."), it will take some time (one hour at the most) until data about vulnerable functions is displayed.
    - OneAgent monitoring for Java vulnerable functions is disabled. To enable it, see [Enable OneAgent monitoring for Java vulnerable functions](/docs/secure/application-security/vulnerability-analytics#vulnerable-function "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.").

      The OneAgent feature must be enabled for all processes affected by the vulnerability.
    - No vulnerable functions of the vulnerability are contained in the release version of the third-party libraries (software components) in use.
    - No vulnerable functions are provided by Snyk or the Dynatrace security research team.
    - You need to restart the processes affected by the vulnerability for updated information. For details, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: remediation-tracking.md


---
title: Remediation tracking
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking
scraped: 2026-02-15T21:21:19.238081
---

# Remediation tracking

# Remediation tracking

* Explanation
* Updated on Jan 14, 2025

This page refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** app, which is deprecated. If you're currently using this app, we recommend transitioning to the corresponding [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.") in the latest Dynatrace experience, which offers enhanced functionality and ongoing support. For details, see [Vulnerabilities upgrade guide](/docs/secure/application-security/vulnerability-analytics/vulnerabilities-upgrade-classic-to-latest "Upgrade from the classic Thirdâparty and Codeâlevel vulnerabilities apps to the Vulnerabilities app in the latest Dynatrace.").

Remediation tracking allows you to track the remediation progress of individual entities ([process groups](#pg), [processes](#process), or [Kubernetes nodes](#k8s)) that are affected by a third-party vulnerability.

For process groups and Kubernetes nodes, you can control which of these entities you want to track and which you want to discard. For instance, if you think an entity isn't relevant or is a false positive, you can mute it. By muting an entity, you hide third-party vulnerabilities for certain process groups or Kubernetes nodes.

* Muted entities aren't taken into consideration in any context, such as Davis Security Score or Application Security metrics.
* To ensure proper handling of newly affected entities, muting all entities doesn't mute the vulnerability itself. Other affected entities may exist that aren't visible to a particular user due to permission restrictions or the selected management zone.

## Remediation tracking for process groups

![Process group overview related to a vulnerability](https://dt-cdn.net/images/2024-02-14-15-17-20-1599-a5f27c81bb.png)

### Access remediation tracking for process groups

To access remediation tracking for process groups that are related to a vulnerability

1. Go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.
2. Select **Details** for the vulnerability you want.
3. Select **View all process groups**.

On the **Process group overview** page, you can

* [Filter for process groups](#filter-pg)
* [Track remediation progress for process groups](#track-pg)
* [Change vulnerability status of process groups](#status-pg)

### Filter for process groups

You can filter for process groups by

* **Entity name**: Full or partial name.
* **Status**: `Affected`, `Resolved`, or `Muted`.
* **Tracking link**: Full or partial title of a tracking link that has already been set up. For details, see [tracking link](#tracking-link-pg).
* **Public internet exposure**: `Public network` or `Not detected`.
* **Reachable data assets**: `Within range` or `None within range`.
* **Name of vulnerable function in use**: You can use two colons in your search term (`<class>::<function>`) to specify the function and/or class name you're looking for:

  + `<class>::` to filter by a specific class name.
  + `<class>::<function>` to filter for a specific function in a specific class.
  + `<function>` to filter for a specific function name in any class.

  Example how to filter by name of vulnerable function in use

  You can find the class and function names in the **Vulnerable functions** section on the details page of a vulnerability.

  ![Class and function attributes of a vulnerable function](https://dt-cdn.net/images/2024-01-04-16-16-20-800-c09240a325.png)

  This section is not displayed

  + If no vulnerable function information is provided by Snyk or the Dynatrace security research team.
  + For runtime vulnerabilities, which are based on the NVD feed.

  In the example above, the class is `org.apache.http.client.utils.URIUtils`, and the function is `extractHost`. On the remediation tracking page of process groups related to a vulnerability, you can use the following syntax to filter

  + By class: `org.apache.http.client.utils.URIUtils::`
  + By function: `extractHost`
  + By the function in the class: `org.apache.http.client.utils.URIUtils::extractHost`

  Example result of filtering by class:

  ![Example filtering by class on the remediation tracking for process groups](https://dt-cdn.net/images/2024-02-14-15-26-12-1649-c4932e535d.png)
* **Vulnerable functions usage**: `In use`, `Not in use`, or `Restart required`.

  For more information about `Restart required`, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").
* **Assessment accuracy**:

  + `Full` filters for related process groups that run in Full-Stack Monitoring mode.
  + `Reduced` filters for related process groups that run in Infrastructure Monitoring mode or OneAgent Discovery mode.

  For details, see [Monitoring modes](/docs/secure/application-security#monitoring-modes "Access the Dynatrace Application Security functionalities.").

### Track remediation progress for process groups

The process group list provides the following information.

#### Process group

* The name of the related process group with a link to the process group details page.
* The number of currently affected processes out of the total number of processes in that process group, indicating the remediation progress.

#### Risk assessment

* If the vulnerability affects a process group that, based on the [Dynatrace entity model (Smartscape)](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment."), is exposed to the internet, the public internet exposure symbol is displayed.
* If the vulnerability affects a process group that, based on the Dynatrace entity model, has database access, the reachable data symbol is displayed.

#### Status

* Current status of the related process group (`Affected`, `Resolved`, or `Muted`).

#### Tracking link

To track a vulnerability's remediation progress, you can add links to tickets created in your own issue tracking system for the affected entity. Once you add a tracking link, select it to navigate to the associated URL, which opens in a new page. You can easily check, for example, if someone is already working on fixing the vulnerability.

![tracking-link](https://dt-cdn.net/images/2023-09-13-17-53-50-337-77c482d850.png)

You can add, update, and delete a tracking link [individually](#link-pg) (for one process group at a time) or [in bulk](#link-pgs) (for several process groups at the same time).

Individually

In bulk

* To add a tracking link

  1. On the overview page of process groups related to a vulnerability, under **Tracking link**, select **Set link** for the desired process group.
  2. Enter a title (for example, the ticket number) and the URL (link to your ticket).
  3. Select **Save**.
* To update or delete a tracking link

  1. On the overview page of process groups related to a vulnerability, under **Tracking link**, select **More** (**â¦**) for the desired process group.
  2. Select **Edit** to update the link or **Delete** to remove it, then select **Save**.

* To add a tracking link

  1. On the overview page of process groups related to a vulnerability, under **Tracking link**, select the process groups you want from those displayed on the page, then select **Set tracking links**.
  2. Enter a title (for example, the ticket number) and the URL (link to your ticket).
  3. Select **Save**.
* To update a tracking link

  1. On the overview page of process groups related to a vulnerability, under **Tracking link**, select the process groups you want from those displayed on the page, then select **Change tracking links**.
  2. Enter the new values, then select **Save**.
* To delete a tracking link

  1. On the overview page of process groups related to a vulnerability, under **Tracking link**, select the process groups you want from those displayed on the page, then select **Delete tracking links**.
  2. Select **Delete**.

#### First detected

A timestamp showing when the related process group was first detected.

#### Last update

A timestamp showing when the status of the related process group was last updated.

#### Details

Detailed information about the selected process group.

![Details of a process group related to a vulnerability](https://dt-cdn.net/images/2023-09-14-09-58-01-1760-3350043753.png)

The process group details section provides the following information:

* **Details**:

  + **Process group name**: The name of the affected process group (for example, `IIS app pool dotNetBackend_easyTravel_x64`) with a link to the process group details page.
  + **Processes**: The number of currently affected processes out of the total number of processes in that process group, indicating the remediation progress. (for example, `2/10 processes affected`).
  + **Status**: The current status of the affected process group (`Affected`, `Resolved`, or `Muted`).
  + **Tracking link**: Existing tracking links appear here. If no tracking link has been added, you can select **Set link** to add one.
  + **First detected**: A timestamp showing when the related process group was first detected.
  + **Last update**: A timestamp showing when the status of the affected process group was last updated.
  + **Vulnerable component**: The name of the vulnerable component (for example, `.NET 3.5.1.0 .NET Framework`).

    - **Loaded from**: The origin of the vulnerable component; shows where the vulnerable component was loaded from (for example, `jar:file:/app/app.jar!/BOOT-INF/lib/spring-web-5.2.2.RELEASE.jar!/`).

    This feature is displayed for vulnerable Java, .NET, Node.js, Python, and Go software components.

    Note that to display the origin of .NET software components, the minimum OneAgent version required is OneAgent version 1.301+.
* **Status**: The latest status change.

  + If the status has changed, Dynatrace displays when the change occurred and who performed the change (if applicable).
  + If the status hasn't changed, **No status changes yet** is displayed.
* **Risk assessment**:

  + If there's any public internet exposure.

    If the symbol is grayed out and crossed out, no public internet exposure was found. If the symbol isn't present, there's no data available.
  + If there are any reachable data assets affected.

    If the symbol is grayed out and crossed out, there aren't any reachable data assets. If the symbol isn't present, there's no data available.
  + If there are any vulnerable functions in use by a process.

    If the symbol is grayed out and crossed out, there's no vulnerable function in use. If the symbol isn't present, there's no data available. For details, see [FAQ: Why is there no data available for vulnerable functions?](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#faq "Monitor the security issues of your third-party libraries.").
  + If process restart is required, with a link to the specific processes that need to be restarted.

    ![Restart required on the remediation tracking page of a process group](https://dt-cdn.net/images/2023-12-18-10-14-37-545-4c6e2f7f34.png)

    For more information, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

### Change vulnerability status of process groups

To change the vulnerability status of

* One affected process group:

  1. On **Process group overview**, go to **Details** of the process group and select **Change status**.
  2. Select the new status and enter any additional information, and then select **Save**.
* Multiple affected process groups:

  1. On **Process group overview**, select the process groups you want from those displayed on the page and then select **Yes, change status**.
  2. Select the new status, enter any additional information, and then select **Save**.

  The option to perform bulk changes isn't available to users with view-only access. The **Manage security problems** permission is required. For details on permission management, see [Fine-tune permissions](/docs/secure/application-security#restrict-permissions "Access the Dynatrace Application Security functionalities.").

## Remediation tracking for processes

![Processes affected by a vulnerability](https://dt-cdn.net/images/2023-09-14-10-04-54-1802-0be01945c8.png)

### Access remediation tracking for processes

To access remediation tracking for processes that are related to a vulnerability

1. Go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.
2. Select **Details** for the vulnerability you want.
3. Select **View all process groups**.
4. In the **Process group** column, under the name of the process group you want, select one of the two numbers to view:

   * The affected processes

     ![example-affected-process-click](https://dt-cdn.net/images/2023-03-13-13-40-45-371-591b997ace.png)
   * The related processes (`Affected` and `Resolved`)

     ![example-related-process-click](https://dt-cdn.net/images/2023-03-13-16-34-25-314-1e97d41a3d.png)

On the **Process overview** page, you can

* [Filter for processes](#filter-process)
* [Track remediation progress for processes](#track-process)

### Filter for processes

You can filter for processes by

* **Entity name**: Full or partial name.
* **Status**: `Affected` or `Resolved`.
* **Name of vulnerable function in use**: You can use two colons in your search term (`<class>::<function>`) to specify the function and/or class name you are looking for:

  + `<class>::` to filter by a specific class name.
  + `<class>::<function>` to filter for a specific function in a specific class.
  + `<function>` to filter for a specific function name in any class.

  Example how to filter by name of vulnerable function in use

  You can find the class and function names in the **Vulnerable functions** section on the details page of a vulnerability.

  ![Class and function attributes of a vulnerable function](https://dt-cdn.net/images/2024-01-04-16-16-20-800-c09240a325.png)

  This section is not displayed

  + If no vulnerable function information is provided by Snyk or the Dynatrace security research team.
  + For runtime vulnerabilities, which are based on the NVD feed.

  In the example above, the class is `org.apache.http.client.utils.URIUtils`, and the function is `extractHost`. On the remediation tracking page for processes related to a vulnerability, you can use the following syntax to filter

  + By class: `org.apache.http.client.utils.URIUtils::`
  + By function: `extractHost`
  + By the function in the class: `org.apache.http.client.utils.URIUtils::extractHost`

  Example result of filtering by function:

  ![Example filtering by function on the remediation tracking for processes](https://dt-cdn.net/images/2024-01-04-16-29-44-1650-cdde650b78.png)
* **Vulnerable functions usage**: `In use`, `Not in use`, or `Restart required`.

  For more information about `Restart required`, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

### Track remediation progress for processes

The process list provides the following information.

#### Process

* The name of the related process (for example, `KpiTomcatFrontEnd-CWS-2-IG-51-HG`) with a link to the process details page.
* The Dynatrace ID of the related process (for example, `PROCESS_GROUP_INSTANCE-B63193A779301A0E`), to distinguish it from other processes with the same name.

#### Vulnerable functions

* If there are any vulnerable functions in use by the process, the vulnerable function symbol is displayed.

  If the symbol is grayed out and crossed out, there's no vulnerable function in use. If the symbol isn't present, there's no data available. For details, see [FAQ: Why is there no data available for vulnerable functions?](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#faq "Monitor the security issues of your third-party libraries.").
* If information about vulnerable functions is outdated, the restart symbol is displayed.

  ![Restart required symbol on process list related to a vulnerability](https://dt-cdn.net/images/2023-12-18-14-47-28-1604-7d119a3d3f.png)

  For more information, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

##### Status

The current status of the related process (`Affected` or `Resolved`).

#### First detected

A timestamp showing when the related process was first detected.

##### Details

Detailed information about the selected process.

![Details of a process affected by a vulnerability](https://dt-cdn.net/images/2023-09-14-10-09-27-1773-7a28354bf1.png)

The process details section provides the following information:

* **Details**:

  + **Process group name**: The name of the related process group (for example, `IIS app pool dotNetBackend_easyTravel_x64`) with a link to the process group details page.
  + **Status**: The current status of the related process (`Affected` or `Resolved`).
  + **First detected**: A timestamp showing when the related process was first detected.
  + **Vulnerable component**: The name of the vulnerable component (for example, `.com.fasterxml.jackson.core:jackson-databind:2.9.9`).

    - **Loaded from**: The origin of the vulnerable component; shows where the vulnerable component was loaded from (for example, `jar:file:/app/app.jar!/BOOT-INF/lib/spring-web-5.2.2.RELEASE.jar!/`).

    This feature is displayed for vulnerable Java, .NET, Node.js, Python, and Go software components.

    Note that to display the origin of .NET software components, the minimum OneAgent version required is OneAgent version 1.301+.
* **Risk assessment**: Presence of vulnerable functions in use by the process.

  + If there are any vulnerable functions in use by the process, the vulnerable function symbol is displayed.
  + If the symbol is grayed out and crossed out, there's no vulnerable function in use.
  + If the symbol isn't present, there's no data available. For details, see [FAQ: Why is there no data available for vulnerable functions?](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#faq "Monitor the security issues of your third-party libraries.").
  + If information about vulnerable functions is outdated, you are prompted to restart the process.

    ![Restart required for remediation entities (processes)](https://dt-cdn.net/images/2023-12-18-10-31-24-460-e8459c9e11.png)

    For more information, see [FAQ: How can I know if information about vulnerable functions is outdated and what can I do about it?](/docs/secure/faq#outdated-vulnerable-functions "Frequently asked questions about Dynatrace Application Security.").

## Remediation tracking for Kubernetes nodes

![Kubernetes nodes related to a vulnerability](https://dt-cdn.net/images/2023-09-14-10-24-11-1807-580be862e7.png)

### Access remediation tracking for nodes

To access remediation tracking for Kubernetes nodes that are related to a vulnerability

1. Go to ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities**.
2. Select **Details** for the vulnerability you want.
3. Select **View all Kubernetes nodes**.

On the **Kubernetes node overview** page you can

* [Filter for nodes](#filter-node)
* [Track remediation progress for nodes](#track-node)
* [Change vulnerability status of nodes](#status-node)

### Filter for nodes

You can filter for nodes by

* **Entity name**: Full or partial name.
* **Status**: `Affected`, `Resolved`, or `Muted`.
* **Tracking link**: Full or partial title of a tracking link that has already been set up. For details, see [tracking link](#tracking-link-nodes).

### Track remediation progress for nodes

The Kubernetes node list provides the following information.

#### Node

The name of the affected node with a link to the host details page.

#### Status

The current status of the affected node (`Affected`, `Resolved`, or `Muted`).

#### Tracking link

To keep track of a vulnerability's remediation progress you can add links to tickets created in your own issue tracking system for the affected entity. Once you add a tracking link, select it to navigate to the associated URL, which opens in a new page. You can easily check, for example, if someone is already working on fixing the vulnerability.

![tracking-link](https://dt-cdn.net/images/2023-09-13-17-53-50-337-77c482d850.png)

You can add, update, and delete a tracking link [individually](#link-node) (for one node at a time) or [in bulk](#link-nodes) (for several nodes at the same time).

Individually

In bulk

* To add a tracking link

  1. On the overview page of nodes related to a vulnerability, under **Tracking link**, select **Set link** for the desired node.
  2. Enter a title (for example, the ticket number) and the URL (link to your ticket).
  3. Select **Save**.
* To update or delete a tracking link

  1. On the overview page of nodes related to a vulnerability, under **Tracking link**, select **More** (**â¦**) for the desired node.
  2. Select **Edit** to update the link or **Delete** to remove it, then select **Save**.

* To add a tracking link

  1. On the overview page of nodes related to a vulnerability, under **Tracking link**, select the nodes you want from those displayed on the page, then select **Set tracking links**.
  2. Enter a title (for example, the ticket number) and the URL (link to your ticket).
  3. Select **Save**.
* To update a tracking link

  1. On the overview page of nodes related to a vulnerability, under **Tracking link**, select the nodes you want from those displayed on the page, then select **Change tracking links**.
  2. Enter the new values, then select **Save**.
* To delete a tracking link

  1. On the overview page of nodes related to a vulnerability, under **Tracking link**, select the nodes you want from those displayed on the page, then select **Delete tracking links**.
  2. Select **Delete**.

#### First detected

A timestamp showing when the affected node was first detected.

#### Last update

A timestamp showing when the status of the affected node was last updated.

#### Details

Detailed information about the selected node.

![Details of a Kubernetes node affected by a vulnerability](https://dt-cdn.net/images/2023-09-14-10-26-51-1755-203155638d.png)

The Kubernetes node details section provides the following information:

* **Details**:

  + **Node name**: The name of the Kubernetes node (for example, `deb-10-k3s-oi-01`).
  + **Status**: The current status of the affected node (`Affected`, `Resolved`, or `Muted`).
  + **Tracking link**: Existing tracking links appear here. If no tracking link has been added, you can select **Set link** to add one.
  + **First detected**: A timestamp showing when the affected node was first detected.
  + **Last update**: A timestamp showing when the status of the affected node was last updated.
  + **Vulnerable component**: The name of the vulnerable component (for example, `Kubernetes v1.21.9+k3s1 master`).
* **Status**:

  + If the status hasn't changed, **No status changes yet** is displayed.
  + If the status has changed, Dynatrace displays when the change occurred and who performed the change (if applicable).

### Change vulnerability status of nodes

To change the vulnerability status of

* One affected node:

  1. Go to **Details** of the Kubernetes node you want, and then select **Change status**.
  2. Select the new status and enter any additional information, and then select **Save**.
* Multiple affected nodes:

  1. Select the nodes you want from those displayed on the page and then select **Yes, change status**.
  2. Select the new status, enter any additional information, and then select **Save**.


---


## Source: use-cases-monitoring-rules.md


---
title: Use cases for monitoring rules
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/use-cases-monitoring-rules
scraped: 2026-02-15T09:06:17.520813
---

# Use cases for monitoring rules

# Use cases for monitoring rules

* Latest Dynatrace
* Tutorial
* Published Apr 22, 2025

Below are some common scenarios for defining [monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") for third-party vulnerabilities [based on resource attributes and Kubernetes labels](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv#new "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.").

## Monitor only the processes on specific hosts

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Find the host on which you want to monitor processes (for example, via [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")).
3. Copy the hostname (for example, `exchange.mycompany.local`) from the overview.
4. Add a new resource attribute monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * Select **Add new condition** and enter the following data:

     + **Resource attribute key**: `host.name`
     + **Matcher**: `equals`
     + **Resource attribute value**: hostname from step 3.
   * Check the preview to see if the condition matches the expected processes.
   * Save the rule.

## Monitor only the Java processes on specific hosts

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Find the host on which you want to monitor processes (for example, via [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")).
3. Copy the hostname (for example, `exchange.mycompany.local`) from the overview.
4. Add a new resource attribute monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * To create a condition that matches the host, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `host.name`
     + **Matcher**: `equals`
     + **Resource attribute value**: hostname from step 3.
   * To create a condition that matches the technology, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `java.main.class`
     + **Matcher**: `exists`
   * Check the preview to see if the conditions match the expected processes.
   * Save the rule.

## Exclude .NET processes of specific hosts from monitoring

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Monitor**.
2. Find the host on which you want to monitor processes (for example, via [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")).
3. Copy the hostname (for example, `exchange.mycompany.local`) from the overview.
4. Add a new resource attribute monitoring rule:

   * Set **Third-party vulnerability control** to `Do not monitor`.
   * To create a condition that matches the host, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `host.name`
     + **Matcher**: `equals`
     + **Resource attribute value**: hostname from step 3.
   * To create a condition that matches the technology, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `dotnet.dll.file`
     + **Matcher**: `exists`
   * Check the preview to see if the conditions match the expected processes.
   * Save the rule.

## Monitor only processes with a custom resource attribute

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Add a [custom resource attributes](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") (for example, `{"stage":"production"}`) to your entities.
3. Add a new resource attribute monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * Select **Add new condition** and enter the following data:

     + **Resource attribute key**: key of the custom resource attribute from step 2 (for example, `stage`)
     + **Matcher**: `equals`
     + **Resource attribute value**: value of the custom resource attribute from step 2 (for example, `production`)
   * Check the preview to see if the condition matches the expected processes.
   * Save the rule.

## Monitor only processes of a specific process group

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Find the process group on which you want to monitor processes (for example, via the **Technologies & Processes Classic** app).
3. Copy the process group ID (for example, `PROCESS_GROUP-0123456789ABCDEF`) from the URL.
4. Add a new resource attribute monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * Select **Add new condition** and enter the following data:

     + **Resource attribute key**: `dt.entity.process_group`
     + **Matcher**: `equals`
     + **Resource attribute value**: ID of the process group from step 3.
   * Check the preview to see if the condition matches the expected processes.
   * Save the rule.

## Monitor only processes running in a specific Kubernetes namespace

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Add a new resource attribute monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * Select **Add new condition** and enter the following data:

     + **Resource attribute key**: `k8s.namespace.name`
     + **Matcher**: `equals`
     + **Resource attribute value**: namespace name that should be monitored
   * Check the preview to see if the condition matches the expected processes.
   * Save the rule.

## Monitor only Kubernetes nodes and hosts running a Linux-based OS for Kubernetes vulnerabilities

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Add a new Kubernetes monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * Select **Add new condition** and enter the following data:

     + **Kubernetes label key**: `kubernetes.io/os`
     + **Matcher**: `equals`
     + **Kubernetes label value**: `linux`
   * Check the preview to see if the condition matches the expected Kubernetes nodes.
   * Save the rule.

## Monitor only EC2 instances for Kubernetes vulnerabilities

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Add a new Kubernetes monitoring rule:

   * Set **Third-party vulnerability control** to `Monitor`.
   * Select **Add new condition** and enter the following data:

     + **Kubernetes label key**: `kubernetes.io/hostname`
     + **Matcher**: `ends with`
     + **Kubernetes label value**: `.ec2.internal`
   * Check the preview to see if the condition matches the expected Kubernetes nodes.
   * Save the rule.

## Exclude ARM-based nodes from monitoring of Kubernetes vulnerabilities

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Monitor**.
2. Add a new Kubernetes monitoring rule:

   * Set **Third-party vulnerability control** to `Do not monitor`.
   * Select **Add new condition** and enter the following data:

     + **Kubernetes label key**: `kubernetes.io/arch`
     + **Matcher**: `contains`
     + **Kubernetes label value**: `arm`
   * Check the preview to see if the condition matches the expected Kubernetes nodes.
   * Save the rule.

## Monitor all Java processes except the Java demo application process on the development hosts

1. In Dynatrace, go to **Settings** > **Application Security** > **General settings** > **Third-party Vulnerability Analytics** and set **Global third-party vulnerability detection control** to **Do not monitor**.
2. Copy the fully qualified name (FQN) of the Java main class of your demo application (for example, `com.example.my.DemoMain`).
3. Find the development host on which you don't want to monitor the demo application process (for example, via [![Infrastructure & Operations](https://dt-cdn.net/images/infrasctucture-operations-highresolution-1025-07d1bc45b5.png "Infrastructure & Operations") **Infrastructure & Operations**](/docs/observe/infrastructure-observability/infrastructure-and-operations "Monitor hosts, VMs, processes, and networks to detect issues and improve infrastructure performance.")).
4. Copy the hostname (for example, `exchange.mycompany.local`) from the overview.
5. Add a new resource attribute monitoring rule to exclude the demo application process on the development host:

   * Set **Third-party vulnerability control** to `Do not monitor`.
   * To create a condition that matches the development host, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `host.name`
     + **Matcher**: `equals`
     + **Resource attribute value**: hostname from step 4.
   * To create a condition that matches the demo application process, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `java.main.class`
     + **Matcher**: `equals`
     + **Resource attribute value**: main class from step 2.
   * Check the preview to see if the conditions match the expected processes.
   * Save the rule.
6. Add a new resource attribute monitoring rule to monitor all remaining Java processes:

   * Set **Third-party vulnerability control** to `Monitor`.
   * To create a condition that matches the technology, select **Add new condition** and enter the following data:

     + **Resource attribute key**: `java.main.class`
     + **Matcher**: `exists`
   * Check the preview to see if the condition matches the expected processes.
   * Save the rule.

The order of the monitoring rules is important: As soon as a rule matches an entity, the entity won't be considered by any of the later rules. Consequently, **specific rules should come before general rules.**

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: third-party-vulnerabilities.md


---
title: Third-party vulnerabilities
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities
scraped: 2026-02-15T21:10:35.279436
---

# Third-party vulnerabilities

# Third-party vulnerabilities

* Latest Dynatrace
* Overview
* Published Feb 13, 2023

[![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities")

Latest Dynatrace

Try out ![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** to improve your environment's security by quickly addressing vulnerabilities and remediation actions.](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.")

[### Manage third-party vulnerabilities

Monitor third-party vulnerabilities and get precise answers about their source, nature, and severity.](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities "Monitor the security issues of your third-party libraries.")[### Filter or mute vulnerabilities

Prioritize and organize third-party vulnerabilities for easy management.](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/filter-third-party-vulnerabilities "Organize third-party vulnerabilities for easy management and to prioritize issues.")[### Davis Security Advisor

Get recommendations for security fixes from Davis Security Advisor.](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-advisor "Get recommendations for security fixes from Davis Security Advisor.")[### Davis Security Score

Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI.")[### Remediation tracking

Track the remediation progress of individual entities that are affected by a third-party vulnerability.](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/remediation-tracking "Track the remediation progress of vulnerabilities.")[### Monitoring rules

Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.")

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---


## Source: vulnerability-analytics.md


---
title: Runtime Vulnerability Analytics
source: https://www.dynatrace.com/docs/secure/application-security/vulnerability-analytics
scraped: 2026-02-15T21:13:29.733620
---

# Runtime Vulnerability Analytics

# Runtime Vulnerability Analytics

* Latest Dynatrace
* How-to guide
* Updated on Dec 18, 2025

Dynatrace Runtime Vulnerability Analytics enables you to detect, visualize, analyze, monitor, and remediate open-source and third-party vulnerabilities, as well as the security vulnerabilities in libraries and first-party code in production and pre-production environments at runtime.

## Capabilities

* Automatic and continuous protection. Dynatrace continuously watches production and pre-production environments to identify any changes in application environments (such as container dynamics, elastic scaling, multi-version deployments, runtime container updates, rollbacks, A/B tests, or blue/green deployments) and provide precise answers about the source, nature, and severity of vulnerabilities as they arise in real time. Dynatrace automatically analyzes and prioritizes alerts.
* Continuous analysis of attack vectors to automatically track if vulnerable libraries are called and used at runtime. Dynatrace Application Security is designed to allow you to identify the most relevant vulnerabilities and reduce false positives with [Smartscape real-time topology mapping](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") and distributed tracing with [PurePathÂ® code-level analysis](/docs/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").
* Runtime introspection approach in combination with [Snykï»¿](https://security.snyk.io/) and [NVDï»¿](https://nvd.nist.gov/vuln), for automatic vulnerability detection at runtime. Even if security checks aren't integrated into the pipelines across all teams, or if they're deliberately bypassed, Dynatrace can detect whatâs running and pinpoint vulnerabilities instantly by automatically opening a vulnerability when one is detected, and close it when the root cause (for example, loading a vulnerable library) is no longer present.
* Full coverage across production rollbacks and outdated releases, feature flags, and deployment patterns (canary, blue/green).
* Efficient management of vulnerabilities where a fix hasn't been effective, such as if a vulnerability is accidentally reintroduced during a rollback, or if updates haven't been applied correctly.
* Precise and automatic [risk and impact assessment](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation#risk-asses "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace."), with risks prioritized by data access path and actual production execution. From hundreds or thousands of open vulnerabilities, Dynatrace Application Security is designed to pinpoint those that need immediate investigation. It automatically analyzes data access paths and production execution to provide a more precise risk and impact assessment.

## How it works

[Runtime Vulnerability Analytics (RVA)](/docs/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") detects and evaluates vulnerabilities in your environment based on what's actually running, not just what's deployed. [Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") monitors loaded libraries, runtime components, and data flows in real time. Vulnerabilities are only reported when affected components are actively used, reducing noise and false positives.

* For third-party vulnerabilities, Dynatrace:

  + Detects libraries and runtime components as they are loaded by processes.
  + Matches component names and versions against trusted vulnerability feeds.
  + Issues a vulnerability only when the component is in use.
* For code-level vulnerabilities, Dynatrace:

  + Analyzes how user input flows through the application.
  + Identifies insecure code paths that could be exploited.
  + Assesses risk based on exposure to the public internet and access to sensitive data assets.

Vulnerabilities are automatically resolved when the root cause is no longer present; for example, if a vulnerable library is removed or a process is stopped. RVA continuously adapts to topology changes and dynamic environments.

For technical details, see [Vulnerability evaluation](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace."). For a quick walkthrough, see [Discover the new Dynatrace Runtime Vulnerability Analytics experienceï»¿](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/).

## Prerequisites

Before you begin, ensure your environment meets the necessary requirements:

* You're using a supported version of Dynatrace. Review the [release notes](/docs/whats-new "Read the product news and the release notes and find out which Documentation topics are new.") for currently supported versions.
* For Runtime Vulnerability Analytics to work properly, make sure deep monitoring is enabled in **Settings** > **Processes and containers** > **Process group monitoring**.

  For .NET, Go, and Python technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

## Permissions

This permissions section refers to the classic ![Third Party Vulnerabilities](https://dt-cdn.net/images/third-party-vulnerabilities-512-1b375181bf.png "Third Party Vulnerabilities") **Third-Party Vulnerabilities** and ![Security Overview](https://dt-cdn.net/images/security-overview-512-a310b17025.png "Security Overview") **Security Overview** apps, which are deprecated. If you're using the latest Dynatrace experience, refer to the [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities** requirements](/docs/secure/vulnerabilities#permissions "Prioritize and efficiently manage vulnerabilities in your monitored environments.") instead.

For details, see [Vulnerabilities upgrade guide](/docs/secure/application-security/vulnerability-analytics/vulnerabilities-upgrade-classic-to-latest "Upgrade from the classic Thirdâparty and Codeâlevel vulnerabilities apps to the Vulnerabilities app in the latest Dynatrace.").

You need to assign specific permissions and optionally fine-tune them based on your access needs.

1. Set up required permissions

Assign the **Security admin** group to users who will be allowed to view and manage vulnerabilities.

To assign **Security admin** permission

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **People**. You have the following options.

Add an existing user

Add a new user

Add an existing user

Add a new user

To add an existing user to the group

2. Under **Actions**, select  > **Edit user** for the user you want to add.
3. Select **Security admin**, then select **Save**.

To add a new user to the group

2. Select **Invite user**.
3. Enter the required details, then select **Next**.
4. Select **Security admin**, then select **Next** > **Invite**.

For more information on user permissions, see [Manage user groups and permissions](/docs/manage/identity-access-management/permission-management/role-based-permissions#users "Role-based permissions").

2. Customize access

Optional

By default, once you enable the **Security admin** group, users can both view and manage vulnerabilities. To restrict the access level to view-only for specific users, so they can view vulnerabilities but not manage them (cannot change their status), you have two options:

Restrict access to an existing group

Create a new group with restricted access

Restrict access to an existing group

Create a new group with restricted access

To restrict the access of an existing group at the environment or management zone level

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Group management**.
2. Filter for **Security admin** and then, under **Actions**, select  > **View group**.
3. For the **Permissions** section, select **Edit**. You have the following options.

1. Configure per environment

4. Select **Environment permissions**.
5. Select your environment, then clear **Manage security problems** and select **View security problems**.
6. Select **Save**.

2. Configure per management zone

4. Select **Management zone permissions**.
5. Filter for and select the management zone you want.
6. Clear **Manage security problems** and select **View security problems**.
7. Select **Save**.

To create a new group with restricted access at the environment or management zone level

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **Group management**.
2. Select **Create group**.
3. Enter a name and a description for the group, and then select **Next**. You have the following options.

1. Configure per environment

4. Select **Environment permissions**.
5. Select your environment, then select **View security problems**.
6. Select **Next** > **Next** and then select **Create group**.

2. Configure per management zone

4. Select **Management zone permissions**.
5. Filter for and select the management zone you want, and then select **View security problems**.
6. Select **Next** > **Next** and then select **Create group**.

## Supported technologies

Third-party vulnerability detection

Code-level vulnerability detection

Dynatrace detects third-party vulnerabilities in the following technologies.

| Technology | Minimum OneAgent version |
| --- | --- |
| Go[1](#fn-1-1-def) | 1.245 |
| Java[2](#fn-1-2-def) | 1.221 |
| Java runtimes | 1.253 |
| Kubernetes | 1.219 |
| .NET[1](#fn-1-1-def) | 1.233 |
| .NET runtimes | 1.255 |
| Node.js[3](#fn-1-3-def) | 1.231 |
| Node.js runtimes | 1.253 |
| PHP | 1.231 |
| Python[1](#fn-1-1-def)'[4](#fn-1-4-def) | 1.309 |
| Python runtimes | 1.309 |

1

For .NET, Go, and Python technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

2

Java on z/OS is currently not supported.

3

Using **Webpack** or other bundlers might have an impact on automatic vulnerability detection. This is because the software components cannot be detected, as they are hidden behind the bundler configuration and not available at runtime. Only packages that are deployed as external packages can be detected and reported. For details, see [Node.js: Limitations](/docs/ingest-from/technology-support/application-software/nodejs#limitations "Read about Dynatrace support for Node.js applications.").

4

For Python vulnerabilities, Dynatrace currently supports only two states for reachable data assets: **Within range** and **Not available**.

Dynatrace detects code-level vulnerabilities in the following technologies.

| Technology | Minimum OneAgent version |
| --- | --- |
| Java 8 or higher[1](#fn-2-1-def) | 1.259 |
| .NET[2](#fn-2-2-def)'[3](#fn-2-3-def) | 1.289 |
| Go[3](#fn-2-3-def) | 1.311 |

1

Only supported on Windows x86 and Linux x86 systems.

2

Only .NET Framework 4.5, .NET Core 3.0 or higher, and 64-bit processes are supported.

3

For .NET and Go technologies, for which automatic deep monitoring is disabled, you need to manually enable deep monitoring on each host. For more information, see [Process deep monitoring](/docs/observe/infrastructure-observability/process-groups/configuration/pg-monitoring "Ways to customize process-group monitoring").

Code-level vulnerability detection for backends that use database ORMs is also supported.

## Get started

* Third-party vulnerability detection helps you identify open-source and third-party vulnerabilities in production and pre-production environments at runtime. To monitor third-party vulnerabilities, [enable third-party vulnerability detection](#tpv-detection).
* Code-level vulnerability detection leverages code inspection at runtime to identify vulnerabilities in libraries and first-party code. To monitor code-level vulnerabilities, [enable code-level vulnerability detection](#clv-detection).

Enable third-party vulnerability detection

Enable code-level vulnerability detection

OneAgent version 1.239+

1. Enable Third-party Vulnerability Analytics

1. Go to **Settings** and select **Application Security** > **Vulnerability Analytics** > **General settings**.
2. Under **Third-party Vulnerability Analytics**, select **Enable Third-party Vulnerability Analytics**.

2. Configure the global third-party vulnerability detection control

To define the default third-party vulnerability detection control for all processes and Kubernetes nodes

1. Go to **Settings** and select **Application Security** > **Vulnerability Analytics** > **General settings**.
2. Under **Third-party vulnerability Analytics**, select one of the **Global third-party vulnerability detection control** modes:

   * **Monitor**âThird-party vulnerabilities are reported.
   * **Do not monitor**âThird-party vulnerabilities are ignored.

You can also define [custom monitoring rules](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") based on certain criteria. In this case, the default monitoring mode applies to all processes and Kubernetes nodes that are not matched by a rule.

3. Control by technology

Optional

After you enable Third-party Vulnerability Analytics, Dynatrace starts generating vulnerabilities for all [supported technologies](/docs/secure/application-security/vulnerability-analytics#tech-tpv "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") by default. To control which of these technologies should receive vulnerabilities

1. Go to **Settings** and select **Application Security** > **Vulnerability Analytics** > **General settings**.
2. Under **Third-party Vulnerability Analytics**, enable or disable technologies as needed.

   Runtime technologies (for example, Java, Node.js, and .NET runtimes) are tied to the corresponding main technology (for example, Java and Node.js). If the main technology is disabled, the corresponding runtime technology is automatically disabled. If you enable the main technology, enabling the corresponding runtime technology is optional.
3. Select **Save changes**.

4. Enable monitoring for Python

This step is required only to monitor vulnerabilities in Python technology.

1. Enable Dynatrace monitoring for Python: In **Monitoring** > **Monitoring technologies**, find **Python** and enable **Monitor Python**.
2. Enable OneAgent monitoring: In **Preferences** > **OneAgent features**, find and enable **Python software component reporting**, then restart your processes.

5. Enable OneAgent monitoring for Java vulnerable functions

Optional

To enable OneAgent monitoring for Java vulnerable functions

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Find and enable **Java vulnerable function reporting**.
3. Select **Save changes**.
4. Restart your processes.

For more information about function usage, see [Vulnerable functions](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/manage-third-party-vulnerabilities#vuln-functions "Monitor the security issues of your third-party libraries.").

OneAgent version 1.259+

1. Enable Code-level Vulnerability Analytics

1. Go to **Settings** and select **Application Security** > **Vulnerability Analytics** > **General settings**.
2. Under **Code-level Vulnerability Analytics**, select **Enable Code-level Vulnerability Analytics**.
3. Restart your processes.

Code-level Vulnerability Analytics is designed to carry a production-ready performance footprint. The overhead depends on your application but should be negligible in most cases.

2. Configure the global code-level vulnerability detection control

To define the default code-level vulnerability detection control for all process groups

1. Go to **Settings** and select **Application Security** > **Vulnerability Analytics** > **General settings**.
2. Under **Code-level Vulnerability Analytics**, select the global code-level vulnerability detection control per technology:

   * **Monitor** â Code-level vulnerabilities in the selected technology are reported.
   * **Do not monitor** â Code-level vulnerabilities in the selected technology are ignored.

You can also define [custom monitoring rules](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups") based on certain process groups. In this case, custom rules override the global detection control for the selected technology, and Runtime Vulnerability Analytics continues to monitor the code-level vulnerabilities based on your rules.

3. Select **Save changes**.
4. Restart your processes.

3. Enable OneAgent monitoring

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Filter by `code-level vulnerability evaluation` and enable the feature for the technologies you want to monitor.
3. Select **Save changes**.
4. Restart your processes.

OneAgent version 1.309 To detect SSRF code-level vulnerabilities, you also need to enable SSRF code-level vulnerability evaluation. See below for instructions.

1. Go to **Settings** and select **Preferences** > **OneAgent features**.
2. Find and enable `Java SSRF code-level vulnerability and attack evaluation`.
3. Select **Save changes**.
4. Restart your processes.

## What's next

After you enable third-party and code-level vulnerability detection, you can

* Improve your environment's security by quickly addressing vulnerabilities and remediation actions with [![Vulnerabilities](https://dt-cdn.net/images/vulnerabilities-highresolution-1025-9279da9743.png "Vulnerabilities") **Vulnerabilities**](/docs/secure/vulnerabilities "Prioritize and efficiently manage vulnerabilities in your monitored environments.").
* Set up monitoring rules for [third-party vulnerabilities](/docs/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/define-monitoring-rules-tpv "Create, modify, and delete custom monitoring rules for Dynatrace-monitored processes.") and [code-level vulnerabilities](/docs/secure/application-security/vulnerability-analytics/code-level-vulnerabilities/define-monitoring-rules-clv "Define rules based on specific process groups").
* Verify monitoring scope and exposure trends with the [**Vulnerability coverage** dashboard](/docs/secure/vulnerabilities/assess-coverage "Evaluate your environment's RVA process and host coverage with the Vulnerability coverage dashboard.").

For details on how Dynatrace evaluates third-party and code-level vulnerabilities, see [Vulnerability evaluation](/docs/secure/application-security/vulnerability-analytics/vulnerability-evaluation "Explore the mechanism for generating third-party and code-level vulnerabilities in Dynatrace.").

## Consumption

Runtime Vulnerability Analytics is licensed based on the consumption of [GiB-hours](/docs/license/capabilities/application-security/runtime-vulnerability-analytics "Learn how your consumption of the Dynatrace Runtime Vulnerability Analytics (RVA) DPS capability is billed and charged.") if you're using the [Dynatrace Platform Subscription (DPS) licensing model](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), or [Application Security units (ASUs)](/docs/license/monitoring-consumption-classic/application-security-units "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.") if you're using the [Dynatrace classic licensing](/docs/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

## Related topics

* [Application Security FAQ](/docs/secure/faq "Frequently asked questions about Dynatrace Application Security.")


---
