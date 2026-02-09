---
title: "Application Security"
source: https://docs.dynatrace.com/managed/secure/application-security
updated: 2026-02-09
---

# Application Security

# Application Security

* How-to guide
* Updated on Nov 03, 2025

Dynatrace Application Security delivers real-time protection and deep visibility into your application landscape. By combining automated vulnerability detection, runtime threat prevention, and posture management, it empowers teams to secure modern cloud-native environments with precision and scale. Explore the feature overviews, configuration steps, operational modes, and usage guidance.

## Get started

To get started with Dynatrace Application Security, follow the instructions below.

Activate Application Security

To activate Application Security, contact a Dynatrace product expert via live chat.

Set up Application Security capabilities

Dynatrace provides the following integrated Application Security capabilities to help secure your applications. Select one to get started.

* [**Dynatrace Runtime Vulnerability Analytics (RVA)**](/managed/secure/application-security/vulnerability-analytics "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules."): Identify critical vulnerabilities instantly with automated risk and impact assessments, thanks to in-depth analysis of data access paths and production execution.
* [**Dynatrace Runtime Application Protection (RAP)**](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities."): Defend your applications in real time by detecting and blocking attacks through advanced code-level insights and transaction analysis.

## Monitoring modes coverage

The effectiveness and depth of Application Security insights depend on the deployed monitoring mode. This section explains how each mode impacts data collection and analysis.

### Support overview

| Capability | Full-Stack | Infrastructure | Discovery |
| --- | --- | --- | --- |
| [Third-party vulnerability detection](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") | Green background check mark | [limited](#tpv-infra) | [limited](#clv-infra) |
| [Code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") | Green background check mark | [limited](#tpv-disco) | [limited](#clv-disco) |
| [Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.") | Green background check mark | Green background check mark | Green background check mark |

Public internet exposure

On Linux hosts, if there's no information, which can happen in different monitoring modes or because something went wrong, public internet exposure is detected via eBPF. Potential states are `Public network` and `Not detected`. Davis Security Score isn't influenced by either of these states.

### Full-Stack Monitoring mode

Recommended

Full-Stack Monitoring mode provides complete application performance monitoring, code-level visibility, deep process monitoring, and Infrastructure Monitoring (including PaaS platforms).

### Infrastructure Monitoring mode

[Infrastructure Monitoring mode](/managed/platform/oneagent/monitoring-modes/monitoring-modes#infrastructure-only "Find out more about the available monitoring modes when using OneAgent."), where OneAgent is configured to provide physical and virtual infrastructure-centric monitoring, provides less complete monitoring than the Full-Stack Monitoring mode. The following functionalities are provided:

* System metrics (CPU usage, memory usage, disk usage)
* [Third-party vulnerability detection](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

#### Characteristics

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

* In an Infrastructure Monitoring deployment, DavisÂ® AI cannot [adapt the Davis Security Score](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI."). In this case, the vulnerability's risk value can't be reevaluated, as this can only happen based on the topology information extracted from your environment, and the DSS will be the same as the CVSS base score.
* Infrastructure Monitoring mode lacks environmental information, such as reachable data assets or public internet exposure, and limits information on related entities, such as databases and services. A full assessment can be performed only on vulnerabilities that have all related hosts under Full-Stack Monitoring.

  + If related hosts are running in Infrastructure Monitoring mode, there's not enough data sent by OneAgents to examine whether there's exposure or sensitive data affected, therefore the values for **public internet exposure** and **reachable data assets** are set to `Not available`.
  + If all related hosts are running in Full-Stack Monitoring mode except one, which runs in Infrastructure Monitoring mode, and the vulnerability isn't exposed or affected (based on the hosts in Full-Stack mode), the values for **public internet exposure** and **reachable data assets** are set to `Not available`. However, if at least one related host is running in Full-Stack Monitoring mode and the vulnerability is exposed or affected, the **public internet exposure** and **reachable data assets** features are displayed.
* In Infrastructure Monitoring mode, vulnerable function information is supported.

Infrastructure Monitoring mode lacks environmental information, such as reachable data assets or public internet exposure, and limits information on related entities, such as databases and services. A full assessment can be performed only on vulnerabilities that have all related hosts under Full-Stack Monitoring.

* If related hosts are running in Infrastructure Monitoring mode, there's not enough data sent by OneAgents to examine whether there's exposure or sensitive data affected, therefore the values for **public internet exposure** and **reachable data assets** are set to `Not available`.
* If all related hosts are running in Full-Stack mode except one, which runs in Infrastructure Monitoring mode, and the vulnerability isn't exposed or affected (based on the hosts in Full-Stack mode), the values for **public internet exposure** and **reachable data assets** are set to `Not available`. However, if at least one related host is running in Full-Stack mode and the vulnerability is exposed or affected, the **public internet exposure** and **reachable data assets** features are displayed.

Same capabilities as Full-Stack Monitoring mode.

#### Consumption

* If you're using the [Dynatrace Platform Subscription (DPS) licensing model](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities."), see [Host monitoring (DPS): Infrastructure Monitoring](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring "Learn how your consumption of the Dynatrace Infrastructure Monitoring DPS capability is billed and charged.").
* If you're using the [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing."), see [Application and Infrastructure Monitoring (Host Units)](/managed/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").

### Discovery mode

[Discovery mode](/managed/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.") is a lightweight monitoring mode that provides basic monitoring. The following functionalities are provided:

* System metrics (CPU usage, memory usage, disk usage)
* [Third-party vulnerability detection](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Runtime Application Protection](/managed/secure/application-security/application-protection "Set up and configure Dynatrace Runtime Application Protection to monitor attacks and attack-generated code-level vulnerabilities.")

For Application Security to work in Discovery mode, after [enabling Discovery mode](/managed/platform/oneagent/monitoring-modes/monitoring-modes#enable-discovery-mode "Find out more about the available monitoring modes when using OneAgent."), you also need to [enable code-module injection](/managed/platform/oneagent/monitoring-modes/monitoring-modes#code-module-injection "Find out more about the available monitoring modes when using OneAgent.").

#### Characteristics

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

* In a Discovery mode deployment, Davis AI cannot [adapt the Davis Security Score](/managed/secure/application-security/vulnerability-analytics/third-party-vulnerabilities/davis-security-score#score "Calculate the Davis Security Score and predict potential vulnerability risks with Davis AI."). In this case, the vulnerability's risk value can't be reevaluated, as this can only happen based on the topology information extracted from your environment, and the DSS will be the same as the CVSS base score.
* Discovery mode lacks environmental information, such as reachable data assets or public internet exposure, and limits information on related entities, such as databases and services. A full assessment can be performed only on vulnerabilities that have all related hosts under Full-Stack Monitoring.

  + If related hosts are running in Discovery mode, not enough data is sent by OneAgents to examine whether there's exposure or sensitive data affected, so the values for **public internet exposure** and **reachable data assets** are set to `Not available`.
  + If all related hosts are running in Full-Stack Monitoring mode except one, which runs in Discovery mode, and the vulnerability isn't exposed or affected (based on the hosts in Full-Stack Monitoring mode), the values for **public internet exposure** and **reachable data assets** are set to `Not available`. However, if at least one related host is running in Full-Stack Monitoring mode and the vulnerability is exposed or affected, the **public internet exposure** and **reachable data assets** features are displayed.

  Exception

  Public internet exposure is detected on Linux hosts running in Discovery mode via eBPF. Potential states are `Public network` and `Not detected`. Davis Security Score isn't influenced by either of these states.
* In Discovery mode, vulnerable function information is supported.

Discovery mode lacks environmental information, such as reachable data assets or public internet exposure, and limits information on related entities, such as databases and services. A full assessment can be performed only on vulnerabilities that have all related hosts under Full-Stack Monitoring.

* If related hosts are running in Discovery mode, not enough data is sent by OneAgents to examine whether there's exposure or sensitive data affected, so the values for **public internet exposure** and **reachable data assets** are set to `Not available`.
* If all related hosts are running in Full-Stack Monitoring mode except one, which runs in Discovery mode, and the vulnerability isn't exposed or affected (based on the hosts in Full-Stack Monitoring mode), the values for **public internet exposure** and **reachable data assets** are set to `Not available`. However, if at least one related host is running in Full-Stack Monitoring mode and the vulnerability is exposed or affected, the **public internet exposure** and **reachable data assets** features are displayed.

Exception

Public internet exposure is detected on Linux hosts running in Discovery mode via eBPF. Potential states are `Public network` and `Not detected`. Davis Security Score isn't influenced by either of these states.

Same capabilities as Full-Stack Monitoring mode.

#### Consumption

Discovery mode is only available for the [Dynatrace Platform Subscription (DPS) licensing model](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

For monitoring consumption information, see [Host monitoring (DPS): Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Learn how your consumption of the Dynatrace Foundation & Discovery DPS capability is billed and charged.").

## Further resources

Explore additional documentation to deepen your understanding and make the most of Dynatrace Application Security.

Videos

Dynatrace University tutorials

Blogs

FAQ

Videos

Dynatrace University tutorials

Blogs

FAQ

* What is Dynatrace and how to get started:

  What is Dynatrace and how to get started
* Elevate security with Dynatrace Davis Anomaly Detection:

  Elevating Security with Dynatrace Davis Anomaly Detection
* Unguard - An open source application security playground:

  Unguard: An open source application security playground
* Vulnerability detection and automated risk assessment with Dynatrace Application Security:

  Vulnerability Detection and Automated Risk Assessment with Dynatrace AppSec
* Remediate vulnerabilities like Log4Shell with Dynatrace:

  Remediate Vulnerabilities like Log4Shell with Dynatrace
* Protect your applications against attacks:

  Protecting your applications against attacks
* How to achieve cloud native hyperscale security with Dynatrace:

  How to achieve cloud native hyperscale security with Dynatrace

* [Introduction to Application Security conceptsï»¿](https://university.dynatrace.com/learn/courses/313/introduction-to-appsec)
* [Dynatrace Application Security overviewï»¿](https://university.dynatrace.com/learn/courses/85/introduction/lessons/484/dynatrace-application-security)
* [Activate Application Securityï»¿](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/382/activating-application-security)
* [Enable Runtime Vulnerability Analyticsï»¿](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/384/enabling-runtime-vulnerability-analytics)
* [Automate and simplify Application Security with Dynatraceï»¿](https://university.dynatrace.com/learn/courses/259/automate-amp-simplify-application-security-with-dynatrace)
* [Configure security notificationsï»¿](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/378/configuring-security-notifications)
* [Runtime Application Protectionï»¿](https://university.dynatrace.com/learn/courses/89/runtime-application-protection/lessons/365/runtime-application-protection)
* [Manage code-level vulnerabilitiesï»¿](https://university.dynatrace.com/learn/courses/86/runtime-vulnerability-analytics/lessons/479/managing-code-level-vulnerabilities)
* [Application Security case study: log4jï»¿](https://university.dynatrace.com/learn/courses/87/case-studies/lessons/478/application-security-case-study-log4j)

* [Remediating CVE-2025-3248: How Dynatrace Application Security protects Agentic AI applicationsï»¿](https://www.dynatrace.com/news/blog/remediating-cve-2025-3248-how-dynatrace-application-security-protects-agentic-ai-applications/)
* [Supply chain security: How to detect malicious software packages with Dynatraceï»¿](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Kubernetes security essentials: Container misconfigurations â From theory to exploitationï»¿](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Dynatrace 3rd-generation platform: Built for the world of Autonomous Intelligenceï»¿](https://www.dynatrace.com/news/blog/dynatrace-3rd-gen-platform/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADRï»¿](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture managementï»¿](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace launches Python Vulnerability Monitoring for enhanced customer securityï»¿](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Snyk integration for Dynatrace: Bridging development and runtime with actionable security notificationsï»¿](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Threat detection in cloud native environments: Detecting suspicious Kubernetes service account behaviorï»¿](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Threat detection in cloud native environments (part 2): How to automate threat management using workflowsï»¿](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protectionï»¿](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Kubernetes security essentials: Kubernetes misconfiguration attack paths and mitigation strategiesï»¿](https://www.dynatrace.com/news/blog/kubernetes-misconfiguration-attack-paths-and-mitigation/)
* [Kubernetes security essentials: Understanding Kubernetes security misconfigurationsï»¿](https://www.dynatrace.com/news/blog/understanding-kubernetes-security-misconfigurations/)
* [Balancing security and performance with business goals through observabilityï»¿](https://www.dynatrace.com/news/blog/balancing-security-and-performance-with-business-goals-through-observability/)
* [Announcing Java SSRF protection in Dynatrace Application Securityï»¿](https://dt-url.net/cn03zlo)
* [NGINX vulnerability: Quickly detect and mitigate IngressNightmare vulnerabilities with Dynatraceï»¿](https://www.dynatrace.com/news/blog/nginx-vulnerability-mitigate-ingressnightmare-with-dynatrace/)
* [Discover the new Dynatrace Runtime Vulnerability Analytics experienceï»¿](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [New continuous compliance requirements drive the need to converge observability and securityï»¿](https://www.dynatrace.com/news/blog/dynatrace-for-executives-security-compliance/)
* [What is application security monitoringï»¿](https://www.dynatrace.com/news/blog/what-is-application-security-monitoring/)
* [Security incident response with Dynatrace automationsï»¿](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [DevSecOps automation improves application security in multicloud environmentsï»¿](https://www.dynatrace.com/news/blog/devsecops-automation-improves-application-security/)
* [Exposure management vs. vulnerability management: Preventing attacks with a robust cybersecurity strategyï»¿](https://www.dynatrace.com/news/blog/exposure-management-vs-vulnerability-management/)
* [Context-aware security incident response with Dynatrace Automations and Tetragonï»¿](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [Best practices for building a strong DevSecOps maturity modelï»¿](https://www.dynatrace.com/news/blog/devsecops-maturity-model-best-practices/)
* [Protect your organization from zero-day vulnerabilitiesï»¿](https://www.dynatrace.com/news/blog/protect-against-zero-day-vulnerabilities/)
* [Find vulnerabilities in your codeâdonât wait for someone to exploit themï»¿](https://www.dynatrace.com/news/blog/code-level-vulnerability-detection/)
* [Dynatrace DevSecOps Lifecycle Coverage with Snyk eliminates security coverage blind spotsï»¿](https://www.dynatrace.com/news/blog/dynatrace-and-snyk-to-unify-security-insights/)
* [Davis Security Advisor extends Application Securityï»¿](https://www.dynatrace.com/news/blog/davis-security-advisor-extends-dynatrace-application-security/)

[Application Security FAQ](/managed/secure/faq "Frequently asked questions about Dynatrace Application Security.")

For troubleshooting articles related to Application Security, visit [Dynatrace Communityï»¿](https://dt-url.net/dy122xtf).

## Related topics

* [Application Securityï»¿](https://www.dynatrace.com/platform/application-security/)
* [Cloud Application Security eBookï»¿](https://www.dynatrace.com/resources/ebooks/cloud-application-security/)
