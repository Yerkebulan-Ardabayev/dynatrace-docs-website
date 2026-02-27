---
title: Security Posture Management compliance standards
source: https://www.dynatrace.com/docs/secure/application-security/spm/compliance-standards
scraped: 2026-02-27T21:21:32.688433
---

# Security Posture Management compliance standards

# Security Posture Management compliance standards

* Latest Dynatrace
* How-to guide
* Published Feb 23, 2026

A compliance standard groups together security, configuration, and process requirements that follow established ICT security guidelines and best practices. Adhering to these standards helps organizations maintain required levels of security hardening and reduce exposure to risk.

In the following, youâll find detailed descriptions of each standard and how Dynatrace supports it.

## BSI C5

C5, also known as the [Cloud Computing Compliance Criteria Catalogueï»¿](https://www.bsi.bund.de/EN/Themen/Unternehmen-und-Organisationen/Informationen-und-Empfehlungen/Empfehlungen-nach-Angriffszielen/Cloud-Computing/Kriterienkatalog-C5/kriterienkatalog-c5_node.html), developed by the German Federal Office for Information Security (BSI), outlines the basic requirements for secure cloud computing. It's primarily designed to provide a high level of assurance in the security of cloud services. While based on international standards such as ISO 27001, C5 goes further by incorporating additional controls tailored explicitly to cloud environments.

### BSI C5 version support

Supported version is C5:2020.

## BSI IT-Grundschutz

The [German IT Baseline Protection (IT- Grundschutz)ï»¿](https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html) standard was established by the German Federal Office for Information Security (BSI) as a sound and sustainable information security management system (ISMS). IT-Grundschutz covers technical, organizational, infrastructural, and personnel aspects equally. With its broad foundation, IT-Grundschutz offers a systematic information security approach compatible with ISO/IEC 27001.

### BSI IT-Grundschutz version support

Supported editions are 2022 and 2023.

## CIS

The [Center for Internet Security (CIS)ï»¿](https://dt-url.net/cm03uso) publishes the CIS Critical Security Controls (CSC) to help organizations achieve greater overall cybersecurity defense. These controls are a recommended set of actions for cyber defense that provide specific and actionable ways to stop todayâs most pervasive and dangerous attacks. A principal benefit of the controls is that they prioritize and focus a smaller number of actions with high pay-off results.

### CIS benchmark support

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

## Cyber Essentials

Cyber Essentials is a United Kingdom security standard aiming to demonstrate that an organization has implemented minimum cybersecurity protections through annual assessments. It comprises fundamental technical controls to help organizations safeguard against common online security threats. [The Cyber Essentials schemeï»¿](https://www.ncsc.gov.uk/files/Cyber-Essentials-Requirements-for-Infrastructure-v3-1-January-2023.pdf) is a government-backed framework supported by the National Cyber Security Centre (NCSC).

### Cyber Essentials version support

Supported version for Cyber Essentials: Requirements for IT infrastructure is v3.1.

## DISA STIG

[Security Technical Implementation Guides (STIGs)ï»¿](https://dt-url.net/cmc3uif) are based on the standards of the Department of Defense (DoD). DISA STIG guidelines are often used as a baseline in other sectors or segments to ensure compliance with the standards and access to the DoD networks. All organizations must meet the DISA STIG security standards before accessing and operating on DoD networks.

### DISA STIG support

| **STIG** | **Supported versions** |
| --- | --- |
| Kubernetes STIG - Ver 2, Rel 4 | Upstream Kubernetes, Amazon EKS, Azure AKS |
| VMware vSphere 8.0 STIG | VMware vCenter 8.0.x, VMware ESXi 8.0.x |
| VMware vSphere 7.0 STIG | VMware vCenter 7.0.x, VMware ESXi 7.0.x |
| VMware vSphere 6.7 STIG | VMware vCenter 6.7.x, VMware ESXi 6.7.x |
| VMware vSphere 6.5 STIG | VMware vCenter 6.5.x, VMware ESXi 6.5.x |
| VMware NSX 4.x STIG | NSX 4.x |
| VMware NSX-T Data Center STIG | NSX 3.x |

## DORA

[Digital Operational Resilience Act (DORA)ï»¿](https://dt-url.net/xp43uj2) is a major piece of European Union legislation (Regulation (EU) 2022/2554). DORA aims to enhance the resilience of digital operations and protect the integrity of the financial market infrastructure in the European Union. Compliance with DORA is a pathway to creating a more secure and reliable digital environment within financial institutions. The act impacts day-to-day operations, security protocols, and compliance measures. DORA takes effect on January 17, 2025.

## Essential Eight

The Essential Eight standard is built on [eight prioritized mitigation strategiesï»¿](https://www.cyber.gov.au/resources-business-and-government/essential-cybersecurity/essential-eight) designed to assist cybersecurity professionals in mitigating incidents caused by various cyber threats. Developed by the Australian Cyber Security Centre (ACSC), it's mandatory for all Australian non-corporate (federal) Commonwealth entities and highly recommended for other business organizations.

## GDPR

General Data Protection Regulation (GDPR) is a European privacy law designed to harmonize data protection regulations across the European Union (EU) by establishing a single, binding framework for all EU member states. [**GDPR.eu**ï»¿](https://gdpr.eu/) offers a comprehensive library of resources to assist organizations in achieving GDPR compliance.

## HIPAA

The 1996 Health Insurance Portability and Accountability Act (HIPAA) mandated that the Secretary of the U.S. Department of Health and Human Services (HHS) establish regulations aimed at safeguarding the privacy and security of specific health information. In response, HHS introduced the [HIPAA Privacy Rule and the HIPAA Security Ruleï»¿](https://www.hhs.gov/hipaa/for-professionals/security/guidance/index.html), which are now widely recognized standards.

### HIPAA version support

Supported version is 5/2005: rev. 3/2007.

## ISO 27001

[ISO 27001ï»¿](https://www.iso.org/standard/27001) is one of the most globally recognized standards, offering a comprehensive Information Security Management Systems (ISMS) framework. It helps organizations align their security practices with international best practices and business, legal, and regulatory requirements. The standard encompasses all aspects of information risk management, from risk assessment to risk treatment, making it an essential tool in today's ever-changing cybersecurity landscape.

### ISO 27001 version support

Supported version is ISO 27001/2022.

## KVKK

The [Personal Data Protection Lawï»¿](https://www.kvkk.gov.tr/en/) (Turkish: KiÅisel Verilerin KorunmasÄ± Kanunu, KVKK) is a Turkish regulation that governs personal data protection and defines the legal obligations of entities and individuals handling personal data. This law ensures compliance with technical requirements for Data Protection, Data Access, and Audit readiness, modeled after the European Unionâs General Data Protection Regulation (GDPR).

## NIST

The [National Institute of Standards and Technology (NIST)ï»¿](https://dt-url.net/5p23u79) publishes the NIST SP 800-53, which offers security and privacy controls for information systems and organizations. Per the Office of Management and Budget (OMB), the NIST standards and policies are mandatory for all non-national security systems run by federal agencies in the USA.

### NIST revision support

| **Revision** | **Cloud provider/Server software** |
| --- | --- |
| SP 800-53 Rev. 5.1.1 | Upstream Kubernetes, Amazon EKS, Azure AKS |
| SP 800-53 Rev. 5 | AWS, Azure |
| SP 800-53 Rev. 5.1 | VMware vSphere |

## PCI DSS

[Payment Card Industry Data Security Standard (PCI DSS)ï»¿](https://www.pcisecuritystandards.org/document_library/) is a set of requirements to ensure that companies that process, store, or transmit credit card information operate in a secure environment. Developed to address the increasing risk of data breaches in payment card systems, PCI DSS is crucial for any business accepting, handling, or storing payment card information.

### PCI DSS version support

Supported version is PCI DSS v4.0.

## TISAX

The Trusted Information Security Assessment Exchange (TISAX) is a prominent information security standard in the automotive industry, developed by the German Association of the Automotive Industry (VDA). TISAX requirements are outlined in the [Information Security Assessment (ISA) catalogï»¿](https://enx.com/en-US/TISAX/downloads/), which is managed by the ENX Association. These requirements are based on the international ISO/IEC 27001 standard for information security management, with additional provisions explicitly tailored to the automotive sector.

### TISAX version support

Supported version is VDA ISA 5.1.

## VMware SCG

VMware Security Configuration Guides provides guidance on how to deploy and operate VMware products in a secure manner based on the [VMware Security Configuration Guideï»¿](https://www.vmware.com/solutions/security/hardening-guides).

### VMware SCG version support

Supported version is vCenter Server 8.0 Update 3.

## Related topics

* [Security Posture Management](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")