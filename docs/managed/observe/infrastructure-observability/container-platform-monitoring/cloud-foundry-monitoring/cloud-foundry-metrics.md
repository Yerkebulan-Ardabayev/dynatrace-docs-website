---
title: Cloud Foundry metrics overview
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring/cloud-foundry-metrics
scraped: 2026-05-12T11:37:33.432161
---

# Cloud Foundry metrics overview

# Cloud Foundry metrics overview

* Reference
* 2-min read
* Published Apr 27, 2020

The Cloud Foundry overview page complements the Cloud Foundry metrics that are collected by Dynatrace OneAgent at the process and host levels with additional metadata and metrics that are pulled via the Cloud Foundry API.

![Cloud Foundry overview page](https://dt-cdn.net/images/cf-screen-165-166-1920-78d87ab14f.png)

Cloud Foundry overview page

## BOSH-managed VMs

Dynatrace automatically detects the metadata of your Cloud Foundry VMs. This metadata is displayed on the Host overview page of your BOSH-managed VM:

![Bosh-managed VMs](https://dt-cdn.net/images/download-1689-14a9ebfb79.png)

Bosh-managed VMs

You can make use of the automatically discovered Cloud Foundry specific metadata to manage large Cloud Foundry environments in several ways. For instance, auto-tagging rules allow you to group all entities that belong to the same BOSH deployment. Metadata like `Technology type: Diego cell` or `Technology type: BOSH` as well as `Cloud platform type: Cloud Foundry foundation` are also available for filtering your host list.

## Gorouters

The **Gorouters** tile offers:

* Traffic flow based on total requests gathered across all Gorouters
* Detection of repeatedly crashing applications resulting from `HTTP 5xx` or `HTTP 502` responses
* Gorouter HTTP metrics

Gorouter HTTP metrics are also available on Gorouter process group instance pages.

## Auctioneers

The **Auctioneers** tile offers:

* Auctioneer distribution of applications and tasks for Diego cells
* Failed application instance placements and failed task placements

## Diego cells

The **Diego cells** tile offers standard performance metrics such as memory usage, CPU usage, and disk space usage.

## Organizations, spaces, applications

The Cloud Foundry overview page also includes Cloud Foundry concepts like **organizations** and **spaces** for holding your applications.
We recommend using the concept of [Management zonesï»¿](https://www.dynatrace.com/news/blog/organize-your-cloud-foundry-foundations-with-management-zones-beta/) for organizing Cloud Foundry organizations, spaces, and applications.  
See [process group metadata for Cloud Foundry applicationsï»¿](https://www.dynatrace.com/news/blog/define-process-group-metadata-for-cloud-foundry-applications/) for information about auto-detection of these and other tags.

## Properties

The Cloud Foundry overview page provides an expandable **Properties and tags** section (see above) where youâll find the Cloud Foundry API version as well as the Cloud Foundry Build version (which represents the Cloud Foundry foundation version). These properties are gathered from the Cloud Foundry API endpoint.

## Limitations

If you monitor multiple Cloud Foundry foundations with the same BOSH deployment ID (for example, 'cf') that are managed by different BOSH directors, Dynatrace merges them into the same Cloud Foundry foundation in your Dynatrace environment. You'll need to set up different BOSH deployment IDs in your deployment YAML files to also separate them in Dynatrace.

## Related topics

* [Set up Dynatrace on Cloud Foundry](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.")