---
title: Security integrations
source: https://www.dynatrace.com/docs/secure/threat-observability/security-events-ingest
scraped: 2026-03-06T21:12:36.899894
---

# Security integrations


* Latest Dynatrace
* Overview
* Updated on Jan 07, 2026

Dynatrace provides different ways to integrate external security data from multiple third-party products into Grail and operationalize your data on the Dynatrace platform.

## Ingest data

For a better understanding of the integration types, see [OpenPipeline integration types for security events](concepts.md#security-ingest "Basic concepts related to Threat Observability").

See below for the supported integrations (with instructions).

* Ingest custom security events via API
* Ingest Akamai security logs and events
* Ingest Amazon ECR container vulnerability findings and scan events
* Ingest Amazon GuardDuty security findings
* Ingest AWS Security Hub security findings
* Ingest GitHub Advanced Security security events and audit logs
* Ingest Harbor vulnerability findings, scans, and audit logs
* Ingest Microsoft Defender for Cloud security events
* Ingest Microsoft Entra ID sign-in logs
* Ingest Microsoft Sentinel security events
* Ingest vulnerability findings in OCSF format
* Ingest Qualys vulnerability findings, scan events, and audit logs
* Ingest Runecast Analyzer compliance findings
* Ingest Snyk vulnerability findings, scans, and audit logs
* Ingest SonarQube security and quality events, metrics, and audit logs
* Ingest Sonatype Lifecycle security events and audit logs
* Ingest Tenable vulnerability findings, scan events, and audit logs

## Enrich data

Add external reputation data to observables using trusted threat intelligence sources:

* Enrich threat observables with AbuseIPDB
* Enrich threat observables with VirusTotal

After configuring enrichment sources, you can apply them to:

* Validate observables in [![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations**](../investigations/enhance-results.md#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")
* Enhance detection findings in [![Threats & Exploits](https://dt-cdn.net/images/attacks-512-b922840b12.png "Threats & Exploits") **Threats & Exploits**](../threats-and-exploits/manage-results.md#enrich "Filter, format, and sort detection findings.")