---
title: Serverless monitoring
source: https://docs.dynatrace.com/managed/discover-dynatrace/get-started/serverless-monitoring
---

# Serverless monitoring

# Serverless monitoring

* 3-min read
* Updated on May 15, 2026

The term **serverless** defines cloud services that share common characteristics:

* Abstracted from underlying infrastructure management
* Highly available and **scaling elastically** with your needs
* Billed on a **pay-per-use** (consumption) model

While often used as a synonym for Functions-As-A-Service (FaaS), serverless cloud services span all sorts of services. The three most important categories are:

* **Serverless compute**, including functions and containers, and managed Kubernetes
* **Serverless PaaS** such as API gateways, messaging systems, or queues
* **Serverless databases** and caches

## Observability challenges

The nature of serverless technologies creates some challenges for the effective observability of such cloud services:

* Distributed, which makes distributed tracing a critical capability.
* Sandboxed environments, with limited capabilities to modify.
* Many different ways to capture telemetry.
* Limitations of cloud provider native monitoring services

  + Gaining an understanding of system behavior can be difficult, as many data sources spread telemetry across multiple places.
  + Obtaining an end-to-end view can be difficult, especially when using hybrid or multi-cloud and third-party applications.
  + Limited capabilities, missing critical capabilities such as real user monitoring, or profiling requiring additional tools.
* New problem patterns:

  + Cold start behavior
  + Cloud service provisioning optimizations
  + Complex service limits and quotas
  + Transient faults

## Serverless observability with Dynatrace

Dynatrace integrates with the three major public cloud providers to capture metrics, metadata, events, logs, and traces. It unifies these data sources to provide end-to-end visibility and Davis AI-powered analysis.

![Unified serverless telemetry](https://dt-cdn.net/images/unified-service-descr-630-f2484fd514.png)

Unified serverless telemetry

With over [600+ integrations, extensions, and technology-specific support﻿](https://www.dynatrace.com/hub/), Dynatrace provides extensive monitoring support, including your [serverless technologies](/managed/ingest-from/technology-support/serverless-compute-services "Learn which features and capabilities Dynatrace supports for serverless compute services for functions (FaaS).") running on Amazon Web Services (AWS), Azure, or Google Cloud.

## Getting started with serverless monitoring

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Turn on cloud service monitoring**](/managed/discover-dynatrace/get-started/serverless-monitoring#services "Monitor serverless cloud services across AWS, Azure, and Google Cloud with Dynatrace for end-to-end visibility and AI-powered analysis.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Enable Dynatrace extensions on cloud services**](/managed/discover-dynatrace/get-started/serverless-monitoring#extensions "Monitor serverless cloud services across AWS, Azure, and Google Cloud with Dynatrace for end-to-end visibility and AI-powered analysis.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Advanced visibility**](/managed/discover-dynatrace/get-started/serverless-monitoring#advanced "Monitor serverless cloud services across AWS, Azure, and Google Cloud with Dynatrace for end-to-end visibility and AI-powered analysis.")

### Step 1 Turn on cloud service monitoring

With a single integration per cloud vendor, Dynatrace automatically discovers your cloud services and monitors the services to provide you with out-of-the-box service health and availability monitoring:

* [Amazon CloudWatch integration](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch.")
* [Azure Monitor integration](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide "Set up and configure Azure monitoring in Dynatrace.")
* [Google Cloud operations suite integration](/managed/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new "Monitor Google Cloud services with Dynatrace and view available metrics.")

### Step 2 Enable Dynatrace extensions on cloud services that support a native extensibility mechanism

Several cloud compute services support simple integration without the need to redeploy your service. This makes it easy to add deep service instrumentation for additional visibility.

Visit Dynatrace Hub to see all services with a [cloud-native integration﻿](https://www.dynatrace.com/hub/?query=cloud-extension).

### Step 3 Advanced visibility

For instructions on integrating Dynatrace into your container image, or using OpenTelemetry or advanced visibility to get additional details via logs and other telemetry events, see the service-specific tutorials:

* [Amazon Web Services](/managed/ingest-from/amazon-web-services "Set up and configure monitoring for Amazon Web Services.")
* [Azure Services](/managed/ingest-from/microsoft-azure-services/azure-integrations "Set up Dynatrace deep code monitoring on Azure using OneAgent or OpenTelemetry.")
* [Google Cloud Services](/managed/ingest-from/google-cloud-platform/gcp-integrations "Set up and configure Dynatrace on Google Cloud.")

Check the recommendations in the Dynatrace web UI to enable additional telemetry sources that improve the observability of your services. For example:

![Observability recommendations](https://dt-cdn.net/images/observability-hints-871-dd9d927caa.png)

Observability recommendations