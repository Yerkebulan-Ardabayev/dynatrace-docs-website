---
title: Log ingest & process (Logs Classic)
source: https://www.dynatrace.com/docs/analyze-explore-automate/log-monitoring/acquire-log-data
scraped: 2026-02-28T21:26:40.679587
---

# Log ingest & process (Logs Classic)

# Log ingest & process (Logs Classic)

* Overview
* 2-min read
* Updated on Aug 11, 2023

Log Monitoring Classic

Dynatrace automatically collects log and event data from a vast array of technologies. With the Log ingestion API, you can stream log records to a system and have Dynatrace transform the stream into meaningful log messages.

Dynatrace supports all major third-party platforms and architectures.

## Log autodetection and custom log sources

You can rely on autodiscovered or manually added log sources for OneAgent. See [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.").

* [Automatically discover log data](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-content-auto-discovery-v2 "Learn about autodiscovery of log content and requirements for autodiscovery to occur.")
* [Manually add log files](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2 "Learn how to manually add log files for analysis.")

![LMC - OneAgent log ingestion and processing configurations at capture](https://dt-cdn.net/images/lmc-oneagent-log-ingestion-and-processing-configurations-at-capture-02-2500-c4876fc96b.png)

## Cloud providers

Log Monitoring includes native support for [Red Hat OpenShift](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes "Extend visibility into Kubernetes/OpenShift events.") and [Kubernetes logs and events](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/log-monitoring-kubernetes "Learn how to monitor logs in Kubernetes.") for Kubernetes platforms, workloads, and applications running inside Kubernetes.

Log Monitoring has native support for [multicloud environments](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/cloud-provider-log-forwarding "Learn how to configure AWS, Azure and Google Cloud log forwarding to ingest logs."), including:

* [AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Amazon Data Firehose integration allows ingest of cloud logs directly, without additional infrastructure needed, and at higher throughput.")
* [Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-guide/deploy-k8 "Set up log and metric monitoring for GCP services on a new GKE Autopilot cluster.")
* [Microsoft Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure "Use Azure log forwarding to ingest Azure logs.")

## Syslog

Syslog is a standard protocol for message logging and system logs management. Routers, printers, hosts, switches and other devices across platforms use syslog to log users' activity, system and software lifecycle events, status, or diagnostics.

Syslog logs are ingested via syslog receiver available on the Environment ActiveGate.

For more information, see [Syslog ingestion with ActiveGate (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/syslog "Ingest syslog log data to Dynatrace using ActiveGate and have Dynatrace transform it into meaningful log messages.").

## Open source

Dynatrace Log Monitoring supports open-source log data frameworks, including Fluentd and Logstash.

## Log ingestion API

With the Log ingestion API, you can stream log records to Dynatrace and have Dynatrace transform the stream into meaningful log messages. You can also use Log ingestion API to stream log records to Dynatrace using API.

* [Log ingestion API](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api "Learn how Dynatrace ingests log data and what are potential limits such ingestion.")
* [Log Monitoring API](/docs/dynatrace-api/environment-api/log-monitoring-v2 "Find out what you can do with the Log Monitoring API v2.")

![LMC - Generic log ingestion API](https://dt-cdn.net/images/lmc-generic-log-ingestion-api-2500-e9c0d3ff5f.png)

## Log processing

Dynatrace Log Monitoring incorporates reshaping the incoming log data into the form you may need for better understanding, analysis, or further processing of your log data by Dynatrace. Using Dynatrace Pattern Language (DPL), you can define patterns using matchers and create a set of rules that Log Monitoring applies to ingested log data.

* [Log processing](/docs/analyze-explore-automate/log-monitoring/log-processing "Create log processing rules that reshape your incoming log data for better analysis or further processing.")
* [Dynatrace Pattern Language](/docs/platform/grail/dynatrace-pattern-language "Use Dynatrace Pattern Language to describe patterns using matchers.")

![LMC - Log processing pipeline](https://dt-cdn.net/images/lmc-log-processing-pipeline-2500-60d2c2d7b6.png)