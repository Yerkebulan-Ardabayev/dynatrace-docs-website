---
title: Unavailable in Dynatrace Managed
source: https://docs.dynatrace.com/managed/upgrade/unavailable-in-managed
---

# Unavailable in Dynatrace Managed

# Unavailable in Dynatrace Managed

* Published Nov 28, 2023

The documentation you selected refers to Dynatrace functionality delivered only as a SaaS (software as a service). To learn more about Dynatrace, see [What's Dynatrace Managed](/managed/discover-dynatrace/what-is-dynatrace "Dynatrace Managed is an on-premises observability platform powered by AI. Learn how it helps you analyze, automate, and deliver more secure software faster.").

## Why only on SaaS?

Some innovations leverage the power of Grail, which is available only in Dynatrace deployed as SaaS.

Grail is the Dynatrace data lakehouse designed explicitly for observability data. It's a unified storage solution for logs, metrics, traces, events, and more. All data stored in Grail is interconnected within a real-time model that reflects the topology and dependencies within a monitored environment.

* Grail is architected as a Massively Parallel Processing (MPP) data lakehouse, scaling to thousands of nodes.
* On-premises Managed Services deployments are more frequently associated with 3, 12, or up to 30-node clusters.

At a massive scale, the underlying infrastructure attributes need to be consistently implemented, controlled, and balanced, which is not practical in physical data centers.

Grail is generally available to all Dynatrace SaaS customers deployed on AWS or Azure.

## If you're ready to upgrade to SaaS

Fantastic.

To take full advantage of the cloud with Dynatrace SaaS, start with [Upgrade from Managed to SaaS deployment](/managed/upgrade "Start your upgrade from Dynatrace Managed deployment to Dynatrace SaaS deployment.") for an overview of the migration process.

## If you're not ready to upgrade to SaaS

Don't worry.

Dynatrace Managed continues to be a market-leading option for customers with mandatory on-premises requirements.

Dynatrace is committed to supporting Managed customers and will continue to provide monthly product updates with many innovations that don't require Grail capabilities. The Managed Dynatrace roadmap doesn't include planned Grail support, as Grail was architected explicitly for SaaS and massively parallel processing.

An important action you can take now is to precisely define your organization's blockers to upgrading your Dynatrace Managed to Dynatrace SaaS.

* List all the blockers and associated applications. Maybe not all monitored entities have equal requirements. Some might be moved to SaaS earlier, some later—a temporary hybrid deployment (SaaS and Managed) might be a good solution.
* Contact us to help you go through the checklist and enable a frictionless upgrade.

## If you aren't sure

If you aren't sure whether you're ready to upgrade to SaaS, the [Dynatrace Managed to SaaS Readiness Assessment﻿](https://dt-url.net/ip038ip) will help you decide.

Questions?

Visit the [Upgrade to SaaS forum﻿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.