---
title: Overview
source: https://docs.dynatrace.com/managed/upgrade/up-get-started
scraped: 2026-05-12T12:07:10.899832
---

# Overview

# Overview

* Published Apr 24, 2023

The purpose of this guide is to enable a self-service approach to upgrading from a Dynatrace Managed deployment to a Dynatrace SaaS deployment. We provide a proven upgrade process, along with all the instructions, tools and support resources you need to successfully run your upgrade.

This documentation is for Dynatrace platform owners, architects, and program managers who want to learn about the:

* Recommended approach to upgrading
* Phases of the migration process
* High-level integration and expansion opportunities
* Tools, capabilities, and resources that are available to you

Whether you prefer to execute your upgrade on your own, use guidance from Dynatrace, or you require full-service support, this guide has you covered. The upgrade process includes three main phases, covering planning and preparation, execution of the actual migration, and considerations for the operational phase. See the visualized process in the diagram below:

![Overview of Managed to SaaS upgrade](https://dt-cdn.net/images/upgrade-to-saas-process-overview-3452-d7dff75a18.png)

Overview of Managed to SaaS upgrade

Before you get started, be aware of the following:

* While the upgrade will update most of your Dynatrace environments, execution of the upgrade occurs independently for each environment.
* We strongly recommend that you review your existing Dynatrace Managed environments and plan for reorganization prior to upgrading to Dynatrace SaaS.

## Plan

During the planning phase, you learn about the benefits of Dynatrace SaaS and how they result in efficiencies, cloud-infrastructure cost savings, and immediate access to the latest Dynatrace innovations. By the end, you'll have a detailed plan for the upgrade and a well-prepared architecture of your Dynatrace SaaS environment.

#### Step 1 - Discover

Assess your current Dynatrace Managed deployment and the feasibility of upgrading to Dynatrace SaaS. Create a list of requirements and goals to perform a successful deployment.

#### Step 2 â Strategize

Define your approach. Based on your current usage of Dynatrace Managed, identify the scope of the upgrade, catalog and evaluate existing Dynatrace environments, and determine what must be upgraded.

#### Step 3 - Design

Review dependencies and constraints in upgrading to Dynatrace SaaS. Create a target architecture diagram.

## Upgrade

Prepare your new Dynatrace SaaS environment and migrate configuration and monitoring components. This includes adjusting integrations and all application or infrastructure monitoring sources.

#### Step 1 - Prepare

Dynatrace sets up licensing for your environments in the desired hyper-scaler region. You prepare and deploy required infrastructure components and configurations to support ActiveGates for required network flows.

#### Step 2 â Execute

During this step, you migrate the configuration, followed by redirection of monitoring traffic from the Dynatrace Managed to the Dynatrace SaaS.

#### Step 3 â Integrate

All third-party integrations with external systems previously linked to the Dynatrace Managed Cluster must be updated and validated to work with your new Dynatrace SaaS environment.

## Run

Once the configuration and monitoring have been migrated, it's time to review and refine your Dynatrace SaaS operational environment. This ensures that the observability services in your organization consistently provide maximum value to your organization. Some of the topics considered in this phase might start during the Execute phase, depending on your operational preferences and user adoption.

#### Step 1 - Enable

Set up user identity and access (IAM) for your Dynatrace SaaS environment, communicate changes, and run an enablement program to leverage maximum value from the Dynatrace platform.

#### Step 2 - Expand

Explore newly available capabilities to extend your observability services.

#### Step 3 - Optimize

Review and optimize for your use cases and internal processes. Finally, it's time to decommission your Dynatrace Managed infrastructure.

Questions?

Visit the [Upgrade to SaaS forumï»¿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.

## Related topics

* [Pre-upgrade assessment](/managed/upgrade/up-plan/feasibility-checklist "Pre-upgrade checklist to identify potential upgrade warnings or challenges.")