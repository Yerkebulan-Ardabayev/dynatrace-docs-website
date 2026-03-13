---
title: Security integrations
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-03-06T21:12:36.899894
---

# Security integrations

# Security integrations

* Latest Dynatrace
* Overview
* Updated on Jan 07, 2026

Dynatrace provides different ways to integrate external security data from multiple third-party products into [Grail](../../platform/grail.md "Insights on what and how you can query Dynatrace data.") and operationalize your data on the Dynatrace platform.

## Ingest data

For a better understanding of the integration types, see [OpenPipeline integration types for security events](concepts.md#security-ingest "Basic concepts related to Threat Observability").

See below for the supported integrations (with instructions).

* [Ingest custom security events via API](security-events-ingest/ingest-custom-data.md "Ingest security events from custom third-party products via API.")
* [Ingest Akamai security logs and events](security-events-ingest/ingest-akamai.md "Ingest Akamai security logs and events into Dynatrace as security events.")
* [Ingest Amazon ECR container vulnerability findings and scan events](security-events-ingest/ingest-aws-ecr-data.md "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.")
* [Ingest Amazon GuardDuty security findings](security-events-ingest/ingest-amazon-guardduty.md "Ingest Amazon GuardDuty security findings and analyze them in Dynatrace.")
* [Ingest AWS Security Hub security findings](security-events-ingest/ingest-aws-security-hub.md "Ingest AWS Security Hub security findings and analyze them in Dynatrace.")
* [Ingest GitHub Advanced Security security events and audit logs](security-events-ingest/ingest-github-advanced-security.md "Ingest GitHub Advanced Security audit logs and security events into Dynatrace as security events.")
* [Ingest Harbor vulnerability findings, scans, and audit logs](security-events-ingest/ingest-harbor-data.md "Ingest Harbor vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Ingest Microsoft Defender for Cloud security events](security-events-ingest/ingest-microsoft-defender.md "Ingest Microsoft Defender for Cloud security events and analyze them in Dynatrace.")
* [Ingest Microsoft Entra ID sign-in logs](security-events-ingest/ingest-microsoft-entra-id.md "Ingest Microsoft Entra ID sign-in logs and analyze them in Dynatrace.")
* [Ingest Microsoft Sentinel security events](security-events-ingest/ingest-microsoft-sentinel.md "Ingest Microsoft Sentinel security events and analyze them in Dynatrace.")
* [Ingest vulnerability findings in OCSF format](security-events-ingest/ingest-ocsf-data.md "Ingest vulnerability findings in OCSF format from any provider and analyze them on the Dynatrace platform.")
* [Ingest Qualys vulnerability findings, scan events, and audit logs](security-events-ingest/ingest-qualys.md "Ingest Qualys vulnerability findings, scan events, and audit logs into Dynatrace as security events.")
* [Ingest Runecast Analyzer compliance findings](security-events-ingest/ingest-runecast-analyzer.md "Ingest compliance findings from Runecast Analyzer and analyze them on the Dynatrace platform.")
* [Ingest Snyk vulnerability findings, scans, and audit logs](security-events-ingest/ingest-snyk-data.md "Ingest Snyk vulnerability findings, scans, and audit logs into Dynatrace as security events.")
* [Ingest SonarQube security and quality events, metrics, and audit logs](security-events-ingest/ingest-sonarqube-data.md "Ingest SonarQube security and quality events, metrics, and audit logs into Dynatrace as security events.")
* [Ingest Sonatype Lifecycle security events and audit logs](security-events-ingest/ingest-sonatype.md "Ingest Sonatype Lifecycle security events and audit logs into Dynatrace as security events.")
* [Ingest Tenable vulnerability findings, scan events, and audit logs](security-events-ingest/ingest-tenable-data.md "Ingest Tenable vulnerability findings, scan events, and audit logs into Dynatrace as security events.")

## Enrich data

Add external reputation data to observables using trusted threat intelligence sources:

* [Enrich threat observables with AbuseIPDB](security-events-ingest/abuseipdb-enrich.md "Enrich threat observables with AbuseIPDB and analyze them in Dynatrace.")
* [Enrich threat observables with VirusTotal](security-events-ingest/virustotal-enrich.md "Enrich threat observables with VirusTotal and analyze them in Dynatrace.")

After configuring enrichment sources, you can apply them to:

* Validate observables in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations/enhance-results.md#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")
* Enhance detection findings in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../threats-and-exploits/manage-results.md#enrich "Filter, format, and sort detection findings.")