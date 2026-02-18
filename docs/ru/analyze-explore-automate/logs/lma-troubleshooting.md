---
title: Troubleshooting Log Management and Analytics
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-troubleshooting
scraped: 2026-02-18T21:34:38.688131
---

# Troubleshooting Log Management and Analytics

# Troubleshooting Log Management and Analytics

* Latest Dynatrace
* Troubleshooting
* 1-min read
* Updated on Oct 15, 2025

This page explains what to do when Log Management and Analytics isn't working in your environment as expected.

## General troubleshooting

If you've encountered an issue related to Log Management and Analytics, check one of the following pages in the Dynatrace Community.

* [Why my logs are not visible in Dynatrace?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-my-logs-are-not-visible-in-Dynatrace/ta-p/242716)
* [What might prevent logs from appearing on the server?ï»¿](https://dt-url.net/lu23817)
* [I get an ingest warning about an attribute key case mismatchï»¿](https://community.dynatrace.com/t5/Troubleshooting/I-get-an-ingest-warning-about-an-attribute-key-case-mismatch/ta-p/251188)
* [I get a warning in the Log Viewer about case-sensitive queriesï»¿](https://community.dynatrace.com/t5/Troubleshooting/I-get-a-warning-in-the-Log-Viewer-about-case-sensitive-queries/ta-p/251189)
* [Syslog Ingestion via ActiveGate Troubleshooting Guideï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-via-ActiveGate-Troubleshooting-Guide/ta-p/282718)
* [Syslog Ingestion Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Syslog-Ingestion-Troubleshooting/ta-p/264112)
* [Troubleshooting log Ingestion via API - POST ingest logsï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-log-Ingestion-via-API-POST-ingest-logs/ta-p/286608)

## Technology-specific troubleshooting

* [Troubleshooting logs ingested via Fluent Bitï»¿](https://community.dynatrace.com/t5/Troubleshooting/Troubleshooting-logs-ingested-via-Fluent-Bit/ta-p/283718)
* [Azure Log Forwarder Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Azure-Log-Forwarder-Troubleshooting/ta-p/243797)
* [Google Cloud Monitor Troubleshootingï»¿](https://community.dynatrace.com/t5/Troubleshooting/Google-Cloud-Monitor-Troubleshooting/ta-p/243796)
* [Logs Ingest on K8s with Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Logs-Ingest-on-K8s-with-Dynatrace/ta-p/285827)

## Specific issues

### Ingested logs don't look as expected

For example, the content is trimmed, the timestamp is corrected, or the processing rule seems not to work.

The log ingest pipeline consists of several stages where logs are processed and checked against product characteristics and [limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics."). A particular log record contains warnings regarding issues that occurred in the log ingest and processing pipeline. Warnings are persisted and stored in `dt.ingest.warnings` attribute for each log record individually. See the list and description of all possible [log ingestion warnings](/docs/analyze-explore-automate/logs/lma-troubleshooting/lma-ingest-warnings "List of log ingestion warnings").

### OneAgent is not ingesting configured log records

If OneAgent is not ingesting log records from a log file despite a log file is configured to be ingested and either automatically detected or added as a custom log source, then Log Agent Security rules might be violated. See [Security rules](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-log-ingestion-via-oa/lma-security-rules "Configure security rules for custom log sources to ensure data protection.") for more information.