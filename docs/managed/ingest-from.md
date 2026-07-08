---
title: Ingest data into Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from
---

# Ingest data into Dynatrace

# Ingest data into Dynatrace

* Explanation
* 2-min read
* Updated on Jun 22, 2026

Dynatrace needs data to work. Before you can analyze performance, detect anomalies, trace requests, or trigger automation, your environment needs to send telemetry to Dynatrace. That process is ingestion: getting your data from wherever it originates into the platform.

This section covers every supported ingestion approach: which one fits your environment, how to set it up, and what happens to your data once it arrives.

## Where ingestion fits in the Dynatrace journey

Data doesn't go directly from your environment into dashboards: it passes through a processing layer that shapes how it lands in storage and becomes available for analysis and action. Ingestion is the first step in a sequence.

| Stage | What happens | Where to learn more |
| --- | --- | --- |
| **Ingest** | Data leaves your environment via agents, SDKs, or API integrations and arrives at Dynatrace | This section |
| **Process** | OpenPipeline routes, filters, enriches, and transforms your data before it reaches storage | [Process your data with OpenPipeline](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") |
| **Store** | Processed data lands in Dynatrace for querying, alerting, and analysis | Automatic: no configuration required to get started |
| **Analyze and act** | Data becomes insights, alerts, dashboards, and automated responses | Dynatrace platform |

You don't need to configure every stage before you start. Default pipelines handle your data automatically once it's flowing. Configure OpenPipeline later, after ingestion is working, when you need to shape how your data lands.

## What determines the right approach

Several factors determine the right data ingestion approach for your environment, including:

* Your infrastructure type
* Whether you can install software on it
* What monitoring tools you already use
* How you prefer to instrument

## Select your environment

| Section | Best for |
| --- | --- |
| [Servers and VMs](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") | Linux, Windows, AIX, Solaris, z/OS: physical or virtual machines you manage |
| [Kubernetes](/managed/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes") | Orchestrated containers on a K8s cluster, any cloud provider or self-managed |
| [Containers and PaaS](/managed/ingest-from/setup-on-container-platforms "Deploy Dynatrace on various container and PaaS platforms.") | Docker on a host, Cloud Foundry, Heroku, Azure App Service: non-K8s containers and PaaS platforms |
| [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options") | AWS serverless functions: monitored using the Dynatrace Lambda extension or OpenTelemetry |
| [Azure Functions](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions "Monitor Azure Functions") | Azure serverless functions: monitored using OpenTelemetry SDKs |
| [Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.") | Azure managed services: Azure SQL, Blob Storage, and Azure Monitor metrics |
| [Google Cloud Platform](/managed/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.") | GCP managed services: Cloud SQL, Cloud Storage, and GCP Operations metrics |
| [OpenTelemetry](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") | Existing OTel instrumentation, or a preference for open-standard SDK-based instrumentation regardless of environment |
| [Extend and customize](/managed/ingest-from/extend-dynatrace "Learn what extension mechanisms are offered by Dynatrace.") | Custom data sources, unsupported technologies, or direct API ingestion |

## Infrastructure prerequisites

Some ingestion setups require connectivity infrastructure before data can flow, such as proxies, routing components, or network configuration for environments that can't reach Dynatrace directly. If a setup guide in this section tells you that you need an ActiveGate or specific network configuration, [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") covers what to deploy and how.