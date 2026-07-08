---
title: Configuration as Code overview
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code
---

# Configuration as Code overview

# Configuration as Code overview

* Overview
* 2-min read
* Updated on Jul 27, 2025

![Configuration as Code](https://dt-cdn.net/images/configuration-as-code-highresolution-1025-29c909e912.png "Configuration as Code") Configuration as Code (CaC) provides Observability as Code and Security as Code to fully automate the configuration of the Dynatrace platform at any scale for:

* Automating and standardizing your observability configurations.
* Adding observability to your software delivery process.
* Ensuring standards while democratizing observability.
* Security-as-code compliance in your service and application onboarding flow.

![Set up Open Pipeline configurations via Terraform](https://cdn.hub.central.dynatrace.com/hub/Terraform-screenshot-intro.png)![Automate the service monitoring configuration via Monaco CLI](https://cdn.hub.central.dynatrace.com/hub/Monaco-Screenshot-Intro.png)

1 of 2Set up Open Pipeline configurations via Terraform

## Use cases

Manage any Dynatrace configuration side-by-side with any source code, from within YAML files organized in Git repositories.

For example:

* IAM resources
* Service monitoring / service onboarding
* SLO dashboards

You can manage any Dynatrace configuration side-by-side with any source code, from within YAML files organized in Git repositories.
Check out our [samples on GitHub﻿](https://github.com/Dynatrace/dynatrace-configuration-as-code-samples).

## Concepts

The Dynatrace CaC approach allows you to manage your Dynatrace environment observability tasks through configuration files instead of via a GUI.

A CaC self-service model allows development teams to set up quickly and efficiently, even for large-scale applications:

* Monitoring
* Observability
* Security policies

It eliminates the need to build custom solutions and reduces the manual work of observability teams.

CaC can:

* Create configuration templates for multiple environments.
* Manage interdependencies between configurations without the need to retain unique identifiers.
* Apply the same configuration to hundreds of Dynatrace environments and be able to update all of them at the same time.
* Promote application-specific configurations across environments after deployments at each stage.
* Support all mechanisms and best practices of git-based workflows such as pull requests, merging, and approvals.
* Commit your configuration to version control and collaborate on changes.

## Why use configuration as code

The reason to use CaC is to have configuration files that allow you to

* Create,
* Update, and
* Manage your observability configurations safely, consistently, and repeatedly.

They can be reused, versioned, and shared with your team.

A standardized approach to configuring Dynatrace as code has many benefits.
In addition to all the advantages a Git approach brings, such as

* Version control
* Reproducibility

Applying CaC allows

* Self-service observability configurations
* Streamlining and standardizing onboarding processes
* Keeping configurations in sync across different environments

## Use observability-driven development within developer platform

* Reduce deployment time by integrating CaC to streamline your application onboarding process via Golden Paths.
* Introduce observability and security standards in your environment by integrating them into your CI/CD pipelines, for example, via container images, and ensuring consistency in all your stages.
* Provide self-service possibilities, integrating observability, automation, and quality gates into your SDLC.
  For more information, see [Platform Engineering](/managed/discover-dynatrace/get-started/platform-engineering "Use observability and security to drive analytics and automation at scale.").

## Tools

To set up and manage Dynatrace with CaC you have two tool options:

* [Terraform](/managed/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform."), the industry-standard CaC software tool.
* [Monaco](/managed/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco."), the Dynatrace-proprietary CaC CLI tool.

Deciding what to use depends on the tool stack and requirements.

We recommend Terraform with the Dynatrace Terraform provider if:

* You're already familiar with Terraform and feel comfortable working with it.
* You want to manage the infrastructure and configuration of multiple providers in a single workspace.
* You want to benefit from external state management, highlighting gaps between the plan and reality, and collaborating via remote state backends like GitHub.
* You plan to use dynamic configurations, leveraging calculations and conditional logic supported by HCL (Hashicorp Configuration Language) expressions.

If you don't want to or can't use Terraform, we offer the Dynatrace-proprietary CaC CLI tool, Monaco.
Monaco provides a third-party independent solution, operating in standalone mode, that uses native JSON to describe the Dynatrace configurations.

## Related topics

* [Configuration as Code via Terraform overview](/managed/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform.")
* [Configuration as Code via Monaco overview](/managed/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.")
* [[Blog] Automated observability, security, and reliability at scale﻿](https://www.dynatrace.com/news/blog/automated-observability-security-and-reliability-at-scale/)