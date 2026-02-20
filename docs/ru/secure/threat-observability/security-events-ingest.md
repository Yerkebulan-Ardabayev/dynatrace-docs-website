---
title: Security integrations
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-02-20T21:08:55.080282
---

# Security integrations

# Security integrations

* Latest Dynatrace
* Overview
* Updated on Jan 07, 2026

Dynatrace provides different ways to integrate external security data from multiple third-party products into [Grail](/docs/platform/grail "Insights on what and how you can query Dynatrace data.") and operationalize your data on the Dynatrace platform.

## Ingest data

For a better understanding of the integration types, see [OpenPipeline integration types for security events](/docs/secure/threat-observability/concepts#security-ingest "Basic concepts related to Threat Observability").

See below for the supported integrations (with instructions).

* [Ingest custom security events via API](/docs/secure/threat-observability/security-events-ingest/ingest-custom-data "Ingest security events from custom third-party products via API.")
* [Ingest Akamai security logs and events](/docs/secure/threat-observability/security-events-ingest/ingest-akamai "Ingest Akamai security logs and events into Dynatrace as security events.")
* [Ingest Amazon ECR container vulnerability findings and scan events](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.")
* [Ingest Amazon GuardDuty security findings](/docs/secure/threat-observability/security-events-ingest/ingest-amazon-guardduty "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.")
* [Ingest AWS Security Hub security findings](/docs/secure/threat-observability/security-events-ingest/ingest-aws-security-hub "Ingest AWS Security Hub security findings and analyze them in Dynatrace.")
* [Ingest GitHub Advanced Security security events and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-github-advanced-security "Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.")
* [Ingest Harbor vulnerability findings, scans, and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-harbor-data "Ingest Harbor vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Ingest Microsoft Defender for Cloud security events](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-defender "Ingest Microsoft Defender for Cloud security events and analyze them in Dynatrace.")
* [Ingest Microsoft Entra ID sign-in logs](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-entra-id "Ingest Microsoft Entra ID sign-in logs and analyze them in Dynatrace.")
* [Ingest Microsoft Sentinel security events](/docs/secure/threat-observability/security-events-ingest/ingest-microsoft-sentinel "Ingest Microsoft Sentinel security events and analyze them in Dynatrace.")
* [Ingest vulnerability findings in OCSF format](/docs/secure/threat-observability/security-events-ingest/ingest-ocsf-data "Ingest vulnerability findings in OCSF format from any provider and analyze them on the Dynatrace platform.")
* [Ingest Qualys vulnerability findings, scan events, and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-qualys "Ingest Qualys vulnerability findings, scan events, and audit logs into Dynatrace as security events.")
* [Ingest Runecast Analyzer compliance findings](/docs/secure/threat-observability/security-events-ingest/ingest-runecast-analyzer "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.")
* [Ingest Snyk vulnerability findings, scans, and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-snyk-data "Ingest Snyk vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Ingest SonarQube security and quality events, metrics, and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-sonarqube-data "Ingest SonarQube security and quality events, metrics, and audit logs into Dynatrace as security events.")
* [Ingest Sonatype Lifecycle security events and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-sonatype "Ingest Sonatype Lifecycle security events and audit logs into Dynatrace as security events.")
* [Ingest Tenable vulnerability findings, scan events, and audit logs](/docs/secure/threat-observability/security-events-ingest/ingest-tenable-data "Ingest Tenable vulnerability findings, scan events, and audit logs into Dynatrace as security events.")

## Enrich data

Add external reputation data to observables using trusted threat intelligence sources:

* [Enrich threat observables with AbuseIPDB](/docs/secure/threat-observability/security-events-ingest/abuseipdb-enrich "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.")
* [Enrich threat observables with VirusTotal](/docs/secure/threat-observability/security-events-ingest/virustotal-enrich "Enrich threat observables with VirusTotal and analyze them in Dynatrace.")

After configuring enrichment sources, you can apply them to:

* Validate observables in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](/docs/secure/investigations/enhance-results#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")
* Enhance detection findings in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](/docs/secure/threats-and-exploits/manage-results#enrich "Filter, format, and sort detection findings.")