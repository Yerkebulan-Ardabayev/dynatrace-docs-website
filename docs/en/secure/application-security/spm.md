---
title: Security Posture Management
source: https://www.dynatrace.com/docs/secure/application-security/spm
scraped: 2026-02-27T21:12:36.887933
---

# Security Posture Management

# Security Posture Management

* Latest Dynatrace
* How-to guide
* Updated on Feb 23, 2026

What youâll find on this page

* [Explore Security Posture Management capabilities](#capabilities)
* [How SPM evaluates and analyzes your posture](#mechanism)
* [Check supported standards and technologies](#support)
* [How to get started with SPM](#start)
* [What you can do with SPM next](#next)
* [Review common use cases](#use-cases)
* [Frequently asked questions](#faq)

Dynatrace Security Posture Management (SPM) enables you to assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.

## Capabilities

Security Posture Management provides comprehensive visibility into the security posture of your Kubernetes, cloud, and VMware environments. Depending on your infrastructure, the following flavors are available:

* **Dynatrace Kubernetes Security Posture Management (KSPM)**: Enables you to detect, analyze, and monitor misconfigurations, security hardening guidelines, and potential compliance violations across your Kubernetes deployments.
* **Runecast Cloud Security Posture Management (CSPM)**: Provides inâdepth insights into the security posture of your AWS, Azure, and GCP environments.
* **Runecast VMware Security Posture Management (VSPM)**: Provides inâdepth insights into the security posture of your VMware environments, including vCenter and NSXâT.

Across these flavors, SPM delivers a consistent set of core capabilities:

* Automated assessments against [supported compliance standards](#support), enabling you to manage and report on the most critical findings.
* Continuous analysis and evidence creation for internal and external auditing purposes.
* Actionable findings that help you to

  + Prioritize compliance efforts
  + Create audit evidence and reporting for auditors and internal security and compliance teams

## How it works

Security Posture Management continuously evaluates your environment for misconfigurations, policy violations, and compliance risks. Dynatrace collects configuration data from your infrastructure and cloud platforms, streams it into Grail, and normalizes it into security events. These are then evaluated against hardening guidelines and compliance standards. Results update in real time as your environment changes, helping you stay secure and audit-ready.

For a quick walkthrough, see [Dynatrace Cloud Security Posture Management elevates cloud security with real-time compliance across hyperscalersï»¿](https://www.dynatrace.com/news/blog/elevate-cloud-security-with-real-time-compliance-across-hyperscalers/).

## Support matrix

Security Posture Management supports a range of compliance standards through two types of coverage: Dynatrace native support and Runecastâintegrated support. Native standards are maintained directly by Dynatrace and kept up to date.

The table below shows which standards are supported and how each one is provided.

For detailed explanations of each compliance standard and how Dynatrace supports them, see [Security Posture Management compliance standards](/docs/secure/application-security/spm/compliance-standards "Technical details about the supported compliance standards.").

| **Compliance standards** | **Kubernetes[1](#fn-1-1-def)** | **AWS** | **Azure** | **GCP** | **vSphere[2](#fn-1-2-def)** | **NSX-T[3](#fn-1-3-def)** |
| --- | --- | --- | --- | --- | --- | --- |
| [BSI C5](/docs/secure/application-security/spm/compliance-standards#bsic5 "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [BSI IT-Grundschutz](/docs/secure/application-security/spm/compliance-standards#bsi-it "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [CIS](/docs/secure/application-security/spm/compliance-standards#cis "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [Cyber Essentials](/docs/secure/application-security/spm/compliance-standards#cyber "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [DISA STIG](/docs/secure/application-security/spm/compliance-standards#stig "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [DORA](/docs/secure/application-security/spm/compliance-standards#dora "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [Essential Eight](/docs/secure/application-security/spm/compliance-standards#essential "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [GDPR](/docs/secure/application-security/spm/compliance-standards#gdpr "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [HIPAA](/docs/secure/application-security/spm/compliance-standards#hipaa "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [ISO 27001](/docs/secure/application-security/spm/compliance-standards#iso "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [KVKK](/docs/secure/application-security/spm/compliance-standards#kvkk "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [NIST](/docs/secure/application-security/spm/compliance-standards#nist "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [PCI DSS](/docs/secure/application-security/spm/compliance-standards#pci "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [TISAX](/docs/secure/application-security/spm/compliance-standards#tisax "Technical details about the supported compliance standards.") |  |  |  |  |  |  |
| [VMware SCG](/docs/secure/application-security/spm/compliance-standards#vmware "Technical details about the supported compliance standards.") |  |  |  |  |  |  |

1

Support includes upstream Kubernetes, Amazon EKS, and Azure AKS. Compatibility is limited to x86-64 CPU architectures and requires Kubernetes version according to Dynatrace support lifecycle (unless defined otherwise in the specific standard).

2

Supported versions are VMware ESXi 8.0 v1.1.0, VMware ESXi 7.0 v1.4.0, VMware ESXi 6.7 v1.2.0, and VMware ESXi 6.5 v1.0.0.

3

NSX-T support is limited to version 3.2 and later.

## Get started

* To get started with Kubernetes Security Posture Management, see [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.").

* To get started with Cloud Security Posture Management and/or VMware Security Posture Management, see [Ingest Runecast Analyzer compliance findings](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").

## What's next

### Next with KSPM

Once you set up Kubernetes Security Posture Management, you can

* Detect, manage, and take action on security and compliance findings with [![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management**](/docs/secure/xspm "Detect, manage, and take action on security and compliance findings.")
* Query [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.")

  + For a list of DQL examples based on compliance events that you can use for further investigation or reporting, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

Try ![xSPM](https://dt-cdn.net/images/security-posture-management-highresolution-1024-83a748ecdd.png "xSPM") **Security Posture Management** and [share your feedbackï»¿](https://dt-url.net/1m03u6q) to help us improve.

### Next with CSPM/VSPM

Once you set up CSPM/VSPM, you can

* Visualize data with our **Security Posture Overview** dashboard. For details, see [Next steps](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer#next "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.").
* Query [compliance events](/docs/semantic-dictionary/model/security-events#compliance-finding-events "Get to know the Semantic Dictionary models related to security events.") with [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations "Combine Grail functionalities for evidence-driven investigations, including incident resolution, root cause analysis, and threat hunting.") or [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.").

  + For a list of DQL examples based on compliance events that you can use for further investigation or reporting, see [Query compliance events](/docs/secure/threat-observability/dql-examples#compliance "DQL examples for security data powered by Grail.").

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

Resources on your system are assessed as `Failed` (not compliant) according to rules specified in the [supported standards](/docs/secure/application-security/spm#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

* To better understand resource configuration and review the source of the rule, see [Gain insights](/docs/secure/xspm/gain-insights "Drill into results that can help you fix misconfigurations and noncompliance.").
* To better understand result types, see [Concepts: Results](/docs/secure/xspm/concepts#concept-results "Concepts that are specific to the Dynatrace Security Posture Management app.").

### What happens if I don't fix my system based on the findings?

Maintaining your security posture is fundamental to your overall security strategy. Think of it as basic security hygieneâwithout it, all other security measures you implement will be significantly less effective. On the compliance side, not addressing these findings means you won't be able to identify, assess, and fix potential issues that could lead to audit failures.

Manually handling the numerous checks required for audits quickly becomes an overwhelming task, consuming countless hours. With our Security Posture Management solution, this entire process is automated, ensuring both security and compliance are effectively managed.

Ignoring compliance issues presents potential exposure risk or compliance failure risk.

### How to fix the problems detected in my environment?

For guidelines on how to fix findings, see [Stay compliant with Security Posture Management](/docs/secure/use-cases/stay-compliant "Stay on top of your security measures, policies, and practices.").

### What environments can be monitored with Security Posture Management?

For a list of supported systems and their versions and distributions, see [Security Posture Management](/docs/secure/application-security/spm#support "Assess, manage, and take action on misconfigurations and violations against security hardening guidelines and regulatory compliance standards.").

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