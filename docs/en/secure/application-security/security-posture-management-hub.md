---
title: Security Posture Management
source: https://www.dynatrace.com/docs/secure/application-security/security-posture-management-hub
scraped: 2026-02-17T21:21:33.642903
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