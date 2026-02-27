---
title: Secure development controls
source: https://www.dynatrace.com/docs/manage/data-privacy-and-security/data-security/secure-development-controls
scraped: 2026-02-27T21:20:35.063593
---

# Secure development controls

# Secure development controls

* Latest Dynatrace
* 4-min read
* Published Jun 04, 2020

This page is an overview of all security controls that are included in the Dynatrace Security Development Lifecycle (SDL). The following sections provide more detail about these controls and practices, which are enforced by Dynatrace across all business-critical product components.

![secure-development-controls-overview](https://dt-cdn.net/images/secure-development-controls-overview-3982-7ad21ab60f.png)

For more information about how Dynatrace secures customer data in production, see [Data security controls](/docs/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.").

## Threat modeling

Security-critical application components require a threat model in the design phase. This threat model is created by product and security architects.

![Threat modeling](https://dt-cdn.net/images/threat-modeling-816b44cd90.svg)

## Evaluation of external services and libraries

Security audits are performed on all external third-party vendors and services before they're put to use by the security teams. All third-party libraries are evaluated for quality, performance, licensing, and vulnerabilities and require approval before being used.

![Evaluating external services and libraries](https://dt-cdn.net/images/evaluating-external-services-and-libraries-37cd7a926f.svg)

## Code reviews

Every code change is approved by a peer developer. Changes made to security-critical areas of the product have to be additionally approved by security personnel.

Changes made to the main code line require a pull request that passes through numerous automated tests, including a selected set of static code-analysis security tests.

![Code reviews](https://dt-cdn.net/images/code-reviews-44e39d181b.svg)

## Static code analysis

Static code analysis and static application security testing (SAST) are performed daily. Rules and plugins are actively maintained by the Dynatrace code quality team comprised of software engineers and security experts.

Plugins include pre-defined and self-developed detection rules for security vulnerabilities and bugs.

![Static code analysis](https://dt-cdn.net/images/static-code-analysis-f3bc613a7e.svg)

## Third-party library scans

Third-party libraries are centrally managed with a software composition analysis tool (SCA). Daily scans are performed, security vulnerabilities and license risks are detected, and remediation tickets are created.

![Third-party scans](https://dt-cdn.net/images/third-party-scans-27165fd909.svg)

## Automated security tests

Individual development teams implement automated security tests in the form of unit tests, integration tests, or UI tests that are executed automatically as part of the CI/CD pipeline.

![Security tests](https://dt-cdn.net/images/security-tests-7fbf27eb8b.svg)

## Code signing

Installer packages are automatically signed in the build pipeline using code signing certificates. Windows installers are signed with extended validation (EV) code-signing certificates.

Also, signature verification is performed automatically during installation and updates.

Plugins and extensions built by Dynatrace are signed, and the signature is validated when they're activated on hosts. Any change to their contents invalidates the signature and prevents activation.

![Code signing](https://dt-cdn.net/images/code-signing-d324fdc18a.svg)

## Penetration tests

Dynatrace has a dedicated team of certified penetration testers who regularly test new and existing features using state-of-the-art penetration-testing tools.

![Penetration testing](https://dt-cdn.net/images/penetration-testing-89250f38c6.svg)

## Intrusion detection and incident response

All critical systems are monitored by Dynatrace and intrusion-detection systems. Critical events trigger an incident response process.

![Intrusion detection and incident response](https://dt-cdn.net/images/intrusion-detection-and-incident-response-9847021c64.svg)

## Web-application scans

Weekly web-application vulnerability scans are performed as dynamic application security tests (DAST).

![Web scans](https://dt-cdn.net/images/web-scans-db5c35afb5.svg)

## Vulnerability scans

All public-facing and critical internal systems are scanned weekly using vulnerability-scanning tools.

![Vulnerability scan](https://dt-cdn.net/images/vulnerability-scan-f268ce5b9c.svg)

## Cloud security scans

All critical cloud accounts are regularly checked for security misconfigurations and non-compliant settings.

![Cloud scans](https://dt-cdn.net/images/cloud-scans-3cbd78a229.svg)

## External penetration testing

Annually, an extensive penetration test of all Dynatrace product components is performed by an independent security firm. Additional external penetration tests are scheduled on demand, the results of which are shared with our customers under a non-disclosure agreement (NDA).

![External penetration testing](https://dt-cdn.net/images/external-pen-testing-51ab8c744f.svg)

## Bug bounty program

Dynatrace runs a private [bug bounty program on HackerOneï»¿](https://www.dynatrace.com/news/blog/dynatrace-incorporates-hackerones-bug-bounty-program-into-their-security-playbook/).

![Bug bounty program](https://dt-cdn.net/images/bug-bounty-4eea6046c7.svg)

## Vulnerability tracking and KPIs

All security issues and vulnerabilities are tracked in a central ticketing system, which is also used for all other work-related tasks by other teams. The security teams categorize and rate all vulnerabilities using the Common Vulnerability Scoring System (CVSS). Remediation timelines for each vulnerability severity are defined and continuously monitored.

Central security dashboards and quarterly reports are made available to all teams. For identified hotspots, improvements are planned and implemented.

![Vulnerability tracking and KPIs](https://dt-cdn.net/images/vulnerability-tracking-f59e2fbfc3.svg)

## Security training and onboarding programs

All Dynatrace employees are expected to attend and successfully complete annual security awareness programs, which cover our corporate and product security policies.

For new employees, the annual security awareness program and additional product security training are part of the onboarding program.

![Security training](https://dt-cdn.net/images/security-training-8b0ececa60.svg)