---
title: "Application Security"
source: https://docs.dynatrace.com/managed/secure/application-security
updated: 2026-02-09
---

* How-to guide

Dynatrace Application Security delivers real-time protection and deep visibility into your application landscape. By combining automated vulnerability detection, runtime threat prevention, and posture management, it empowers teams to secure modern cloud-native environments with precision and scale. Explore the feature overviews, configuration steps, operational modes, and usage guidance.

## Get started

To get started with Dynatrace Application Security, follow the instructions below.

Activate Application Security

To activate Application Security, contact a Dynatrace product expert via live chat.

Set up Application Security capabilities

Dynatrace provides the following integrated Application Security capabilities to help secure your applications. Select one to get started.

* **Dynatrace Runtime Vulnerability Analytics (RVA)**: Identify critical vulnerabilities instantly with automated risk and impact assessments, thanks to in-depth analysis of data access paths and production execution.
* **Dynatrace Runtime Application Protection (RAP)**: Defend your applications in real time by detecting and blocking attacks through advanced code-level insights and transaction analysis.

## Monitoring modes coverage

The effectiveness and depth of Application Security insights depend on the deployed monitoring mode. This section explains how each mode impacts data collection and analysis.

### Support overview

| Capability | Full-Stack | Infrastructure | Discovery |
| --- | --- | --- | --- |
| [Third-party vulnerability detection](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") | Green background check mark | [limited](#tpv-infra) | [limited](#clv-infra) |
| [Code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.") | Green background check mark | [limited](#tpv-disco) | [limited](#clv-disco) |
| Runtime Application Protection | Green background check mark | Green background check mark | Green background check mark |

Public internet exposure

On Linux hosts, if there's no information, which can happen in different monitoring modes or because something went wrong, public internet exposure is detected via eBPF. Potential states are `Public network` and `Not detected`. Davis Security Score isn't influenced by either of these states.

### Full-Stack Monitoring mode

Recommended

Full-Stack Monitoring mode provides complete application performance monitoring, code-level visibility, deep process monitoring, and Infrastructure Monitoring (including PaaS platforms).

### Infrastructure Monitoring mode

Infrastructure Monitoring mode, where OneAgent is configured to provide physical and virtual infrastructure-centric monitoring, provides less complete monitoring than the Full-Stack Monitoring mode. The following functionalities are provided:

* System metrics (CPU usage, memory usage, disk usage)
* [Third-party vulnerability detection](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Runtime Application Protection

#### Characteristics

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

* In an Infrastructure Monitoring deployment, DavisÂ® AI cannot adapt the Davis Security Score. In this case, the vulnerability's risk value can't be reevaluated, as this can only happen based on the topology information extracted from your environment, and the DSS will be the same as the CVSS base score.
* Infrastructure Monitoring mode lacks environmental information, such as reachable data assets or public internet exposure, and limits information on related entities, such as databases and services. A full assessment can be performed only on vulnerabilities that have all related hosts under Full-Stack Monitoring.

  + If related hosts are running in Infrastructure Monitoring mode, there's not enough data sent by OneAgents to examine whether there's exposure or sensitive data affected, therefore the values for **public internet exposure** and **reachable data assets** are set to `Not available`.
  + If all related hosts are running in Full-Stack Monitoring mode except one, which runs in Infrastructure Monitoring mode, and the vulnerability isn't exposed or affected (based on the hosts in Full-Stack mode), the values for **public internet exposure** and **reachable data assets** are set to `Not available`. However, if at least one related host is running in Full-Stack Monitoring mode and the vulnerability is exposed or affected, the **public internet exposure** and **reachable data assets** features are displayed.
* In Infrastructure Monitoring mode, vulnerable function information is supported.

Infrastructure Monitoring mode lacks environmental information, such as reachable data assets or public internet exposure, and limits information on related entities, such as databases and services. A full assessment can be performed only on vulnerabilities that have all related hosts under Full-Stack Monitoring.

* If related hosts are running in Infrastructure Monitoring mode, there's not enough data sent by OneAgents to examine whether there's exposure or sensitive data affected, therefore the values for **public internet exposure** and **reachable data assets** are set to `Not available`.
* If all related hosts are running in Full-Stack mode except one, which runs in Infrastructure Monitoring mode, and the vulnerability isn't exposed or affected (based on the hosts in Full-Stack mode), the values for **public internet exposure** and **reachable data assets** are set to `Not available`. However, if at least one related host is running in Full-Stack mode and the vulnerability is exposed or affected, the **public internet exposure** and **reachable data assets** features are displayed.

Same capabilities as Full-Stack Monitoring mode.

#### Consumption

* If you're using the Dynatrace Platform Subscription (DPS) licensing model, the licensing model for all Dynatrace capabilities."), see Host monitoring (DPS): Infrastructure Monitoring.
* If you're using the Dynatrace classic licensing, see Application and Infrastructure Monitoring (Host Units).

### Discovery mode

Discovery mode is a lightweight monitoring mode that provides basic monitoring. The following functionalities are provided:

* System metrics (CPU usage, memory usage, disk usage)
* [Third-party vulnerability detection](/managed/secure/application-security/vulnerability-analytics#tpv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* [Code-level vulnerability detection](/managed/secure/application-security/vulnerability-analytics#clv-detection "Monitor, visualize, analyze, and remediate third-party and code-level vulnerabilities, track the remediation progress, and create monitoring rules.")
* Runtime Application Protection

For Application Security to work in Discovery mode, after enabling Discovery mode, you also need to enable code-module injection.

#### Characteristics

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

Third-party vulnerabilities

Code-level vulnerabilities

Attacks

* In a Discovery mode deployment, Davis AI cannot adapt the Davis Security Score. In this case, the vulnerability's risk value can't be reevaluated, as this can only happen based on the topology information extracted from your environment, and the DSS will be the same as the CVSS base score.
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

Discovery mode is only available for the Dynatrace Platform Subscription (DPS) licensing model, the licensing model for all Dynatrace capabilities.").

For monitoring consumption information, see Host monitoring (DPS): Foundation & Discovery.

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

* [Introduction to Application Security concepts](https://university.dynatrace.com/learn/courses/313/introduction-to-appsec)
* [Dynatrace Application Security overview](https://university.dynatrace.com/learn/courses/85/introduction/lessons/484/dynatrace-application-security)
* [Activate Application Security](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/382/activating-application-security)
* [Enable Runtime Vulnerability Analytics](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/384/enabling-runtime-vulnerability-analytics)
* [Automate and simplify Application Security with Dynatrace](https://university.dynatrace.com/learn/courses/259/automate-amp-simplify-application-security-with-dynatrace)
* [Configure security notifications](https://university.dynatrace.com/learn/courses/88/configuring-application-security/lessons/378/configuring-security-notifications)
* [Runtime Application Protection](https://university.dynatrace.com/learn/courses/89/runtime-application-protection/lessons/365/runtime-application-protection)
* [Manage code-level vulnerabilities](https://university.dynatrace.com/learn/courses/86/runtime-vulnerability-analytics/lessons/479/managing-code-level-vulnerabilities)
* [Application Security case study: log4j](https://university.dynatrace.com/learn/courses/87/case-studies/lessons/478/application-security-case-study-log4j)

* [Remediating CVE-2025-3248: How Dynatrace Application Security protects Agentic AI applications](https://www.dynatrace.com/news/blog/remediating-cve-2025-3248-how-dynatrace-application-security-protects-agentic-ai-applications/)
* [Supply chain security: How to detect malicious software packages with Dynatrace](https://www.dynatrace.com/news/blog/supply-chain-security-how-to-detect-malicious-software-packages-with-dynatrace/)
* [Kubernetes security essentials: Container misconfigurations â From theory to exploitation](https://www.dynatrace.com/news/blog/kubernetes-security-essentials-container-misconfigurations-from-theory-to-exploitation/)
* [Dynatrace 3rd-generation platform: Built for the world of Autonomous Intelligence](https://www.dynatrace.com/news/blog/dynatrace-3rd-gen-platform/)
* [Revolutionizing cloud security with observability context: Dynatrace Cloud Security addressing CADR](https://www.dynatrace.com/news/blog/revolutionizing-cloud-security-observability-cadr/)
* [Empowering SREs with runtime vulnerability analytics and security posture management](https://www.dynatrace.com/news/blog/empowering-sres-with-runtime-vulnerability-analytics-and-security-posture-management/)
* [Dynatrace launches Python Vulnerability Monitoring for enhanced customer security](https://www.dynatrace.com/news/blog/dynatrace-launches-python-vulnerability-monitoring-for-enhanced-customer-security/)
* [Snyk integration for Dynatrace: Bridging development and runtime with actionable security notifications](https://www.dynatrace.com/news/blog/snyk-dynatrace-integration-actionable-notifications/)
* [Threat detection in cloud native environments: Detecting suspicious Kubernetes service account behavior](https://www.dynatrace.com/news/blog/threat-detection-cloud-native-kubernetes/)
* [Threat detection in cloud native environments (part 2): How to automate threat management using workflows](https://www.dynatrace.com/news/blog/threat-detection-automate-using-workflows/)
* [Revisiting Spring4Shell: How Cloud Application Detection and Response (CADR) offers multi-layer protection](https://www.dynatrace.com/news/blog/spring4shell-cadr-multi-layer-protection/)
* [Kubernetes security essentials: Kubernetes misconfiguration attack paths and mitigation strategies](https://www.dynatrace.com/news/blog/kubernetes-misconfiguration-attack-paths-and-mitigation/)
* [Kubernetes security essentials: Understanding Kubernetes security misconfigurations](https://www.dynatrace.com/news/blog/understanding-kubernetes-security-misconfigurations/)
* [Balancing security and performance with business goals through observability](https://www.dynatrace.com/news/blog/balancing-security-and-performance-with-business-goals-through-observability/)
* [Announcing Java SSRF protection in Dynatrace Application Security](https://dt-url.net/cn03zlo)
* [NGINX vulnerability: Quickly detect and mitigate IngressNightmare vulnerabilities with Dynatrace](https://www.dynatrace.com/news/blog/nginx-vulnerability-mitigate-ingressnightmare-with-dynatrace/)
* [Discover the new Dynatrace Runtime Vulnerability Analytics experience](https://www.dynatrace.com/news/blog/discover-the-new-dynatrace-runtime-vulnerability-analytics-experience/)
* [New continuous compliance requirements drive the need to converge observability and security](https://www.dynatrace.com/news/blog/dynatrace-for-executives-security-compliance/)
* [What is application security monitoring](https://www.dynatrace.com/news/blog/what-is-application-security-monitoring/)
* [Security incident response with Dynatrace automations](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [DevSecOps automation improves application security in multicloud environments](https://www.dynatrace.com/news/blog/devsecops-automation-improves-application-security/)
* [Exposure management vs. vulnerability management: Preventing attacks with a robust cybersecurity strategy](https://www.dynatrace.com/news/blog/exposure-management-vs-vulnerability-management/)
* [Context-aware security incident response with Dynatrace Automations and Tetragon](https://www.dynatrace.com/news/blog/context-aware-security-incident-response/)
* [Best practices for building a strong DevSecOps maturity model](https://www.dynatrace.com/news/blog/devsecops-maturity-model-best-practices/)
* [Protect your organization from zero-day vulnerabilities](https://www.dynatrace.com/news/blog/protect-against-zero-day-vulnerabilities/)
* [Find vulnerabilities in your codeâdonât wait for someone to exploit them](https://www.dynatrace.com/news/blog/code-level-vulnerability-detection/)
* [Dynatrace DevSecOps Lifecycle Coverage with Snyk eliminates security coverage blind spots](https://www.dynatrace.com/news/blog/dynatrace-and-snyk-to-unify-security-insights/)
* [Davis Security Advisor extends Application Security](https://www.dynatrace.com/news/blog/davis-security-advisor-extends-dynatrace-application-security/)

Application Security FAQ

For troubleshooting articles related to Application Security, visit [Dynatrace Community](https://dt-url.net/dy122xtf).

## Related topics

* [Application Security](https://www.dynatrace.com/platform/application-security/)
* [Cloud Application Security eBook](https://www.dynatrace.com/resources/ebooks/cloud-application-security/)
