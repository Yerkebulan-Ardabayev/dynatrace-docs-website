---
title: Secure development controls
source: https://docs.dynatrace.com/managed/manage/data-privacy-and-security/data-security/secure-development-controls
scraped: 2026-05-12T11:08:42.517530
---

# Secure development controls

# Secure development controls

* 4-min read
* Updated on May 04, 2026

This page is an overview of all security controls that are included in the Dynatrace Security Development Lifecycle (SDL). The following sections provide more detail about these controls and practices, which are enforced by Dynatrace across all business-critical product components.

![Secure development controls overview](https://cdn.bfldr.com/B686QPH3/as/vtr987hx2ktmkf5h7gx7psh3/Secure_development_controls_-_Light_Mode?auto=webp&format=png&position=1)

Secure development controls overview

For more information about how Dynatrace secures customer data in production, see [Data security controls](/managed/manage/data-privacy-and-security/data-security/data-security-controls "Learn about data security and operational security controls.").

## Threat modeling

Security-critical application components require a threat model in the design phase. This threat model is created by product and security architects.

![Threat modeling](https://cdn.bfldr.com/B686QPH3/as/cj5mpkrv8phskt9rkmf2xbh/Threat_modeling_-_Light_Mode?auto=webp&format=png&position=1)

Threat modeling

## Evaluation of external services and libraries

Security audits are performed on all external third-party vendors and services before they're put to use by the security teams. All third-party libraries are evaluated for quality, performance, licensing, and vulnerabilities and require approval before being used.

![Evaluation of external services and libraries](https://cdn.bfldr.com/B686QPH3/as/pq9zwckn6b66vr36xc4nng6/Evaluation_of_external_services_and_libraries_-_Light_Mode?auto=webp&format=png&position=1)

Evaluation of external services and libraries

## Code reviews

Every code change is approved by a peer developer. Changes made to security-critical areas of the product have to be additionally approved by security personnel.

Changes made to the main code line require a pull request that passes through numerous automated tests, including a selected set of static code-analysis security tests.

![Code reviews](https://cdn.bfldr.com/B686QPH3/as/rthtkcpfxn9bjx74mtf4328/Code_reviews_-_Light_Mode?auto=webp&format=png&position=1)

Code reviews

## Static code analysis

Static code analysis and static application security testing (SAST) are performed daily. Rules and plugins are actively maintained by the Dynatrace code quality team comprised of software engineers and security experts.

Plugins include pre-defined and self-developed detection rules for security vulnerabilities and bugs.

![Static code analysis](https://cdn.bfldr.com/B686QPH3/as/36c74k58fvpfrtxbpzn8/Static_code_analysis_-_Light_Mode?auto=webp&format=png&position=1)

Static code analysis

## Third-party library scans

Third-party libraries are centrally managed with a software composition analysis tool (SCA). Daily scans are performed, security vulnerabilities and license risks are detected, and remediation tickets are created.

![Third-party library scans](https://cdn.bfldr.com/B686QPH3/as/9z27rnngqg8jz4wcnfvm563/Third-party_library_scans_-_Light_Mode?auto=webp&format=png&position=1)

Third-party library scans

## Automated security tests

Individual development teams implement automated security tests in the form of unit tests, integration tests, or UI tests that are executed automatically as part of the CI/CD pipeline.

![Automated security tests](https://cdn.bfldr.com/B686QPH3/as/9b4qj4rsc5j5r6crtfmk7zhk/Automated_security_tests_-_Light_Mode?auto=webp&format=png&position=1)

Automated security tests

## Code signing

Installer packages are automatically signed in the build pipeline using code signing certificates. Windows installers are signed with extended validation (EV) code-signing certificates.

Also, signature verification is performed automatically during installation and updates.

Plugins and extensions built by Dynatrace are signed, and the signature is validated when they're activated on hosts. Any change to their contents invalidates the signature and prevents activation.

![Code signing](https://cdn.bfldr.com/B686QPH3/as/6f6ttzwkwnjvr9wkp3qmxgq7/Code_Signing_-_Light_Mode?auto=webp&format=png&position=1)

Code signing

## Penetration tests

Dynatrace has a dedicated team of certified penetration testers who regularly test new and existing features using state-of-the-art penetration-testing tools.

![Penetration tests](https://cdn.bfldr.com/B686QPH3/as/5p3brjsnb9fhsnkkfn4cm/Penetration_test_-_Light_Mode?auto=webp&format=png&position=1)

Penetration tests

## Intrusion detection and incident response

All critical systems are monitored by Dynatrace and intrusion-detection systems. Critical events trigger an incident response process.

![Intrusion detection and incident response](https://cdn.bfldr.com/B686QPH3/as/43gchs247k5hjqjxmh7tf/Intrusion_detection_and_incident_response__-_Light_Mode?auto=webp&format=png&position=1)

Intrusion detection and incident response

## Web-application scans

Weekly web-application vulnerability scans are performed as dynamic application security tests (DAST).

![Web-application scans](https://cdn.bfldr.com/B686QPH3/as/gm9857j4sqx7wmp4c9x74jcs/Web-application_scans_-_Light_Mode?auto=webp&format=png&position=1)

Web-application scans

## Vulnerability scans

All public-facing and critical internal systems are scanned weekly using vulnerability-scanning tools.

![Vulnerability scans](https://cdn.bfldr.com/B686QPH3/as/jns6rqxqnw3cj3mh4rm9c3rv/Vulnerability_scans_-_Light_Mode?auto=webp&format=png&position=1)

Vulnerability scans

## Cloud security scans

All critical cloud accounts are regularly checked for security misconfigurations and non-compliant settings.

![Cloud security scan](https://cdn.bfldr.com/B686QPH3/as/xc9c589n9q5mswqz9tx7rhts/Cloud_security_scan_-_Light_Mode?auto=webp&format=png&position=1)

Cloud security scan

## External penetration testing

Annually, an extensive penetration test of all Dynatrace product components is performed by an independent security firm. Additional external penetration tests are scheduled on demand, the results of which are shared with our customers under a non-disclosure agreement (NDA).

![External penetration testing](https://cdn.bfldr.com/B686QPH3/as/53g78q24sqq8smqss2qrj5g/External_penetration_testing_-_Light_Mode?auto=webp&format=png&position=1)

External penetration testing

## Bug bounty program

Dynatrace runs a private [bug bounty program on HackerOneï»¿](https://www.dynatrace.com/news/blog/dynatrace-incorporates-hackerones-bug-bounty-program-into-their-security-playbook/).

![Bug bounty program](https://cdn.bfldr.com/B686QPH3/as/6r9rgxhx72c6kwrtfg4nqk/Bug_bounty_program_-_Light_Mode?auto=webp&format=png&position=1)

Bug bounty program

## Vulnerability tracking and KPIs

All security issues and vulnerabilities are tracked in a central ticketing system, which is also used for all other work-related tasks by other teams. The security teams categorize and rate all vulnerabilities using the Common Vulnerability Scoring System (CVSS). Remediation timelines for each vulnerability severity are defined and continuously monitored.

Central security dashboards and quarterly reports are made available to all teams. For identified hotspots, improvements are planned and implemented.

![Vulnerability tracking and KPIs](https://cdn.bfldr.com/B686QPH3/as/7m2pck8z487zpnckr53rfxv/Vulnerability_tracking_and_KPIs_-_Light_Mode?auto=webp&format=png&position=1)

Vulnerability tracking and KPIs

## Security training and onboarding programs

All Dynatrace employees are expected to attend and successfully complete annual security awareness programs, which cover our corporate and product security policies.

For new employees, the annual security awareness program and additional product security training are part of the onboarding program.

![Security training](https://cdn.bfldr.com/B686QPH3/as/nnn4f8nxsbg7s667fv4bqv2t/Security_training_and_onboarding_programs_-_Light_Mode?auto=webp&format=png&position=1)

Security training