---
title: Configuration as Code via Terraform overview
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform
---

# Configuration as Code via Terraform overview

# Configuration as Code via Terraform overview

* Explanation
* 2-min read
* Updated on Jul 01, 2024

Dynatrace offers a dedicated [Terraform provider﻿](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest) to manage your monitoring environment.

## Terraform overview

[Terraform﻿](https://developer.hashicorp.com/terraform), by HashiCorp, is a widely adopted Infrastructure-as-Code (IaC) tool.

The Dynatrace Terraform provider is a library that allows you to use the Terraform syntax and functionalities to create a custom configuration (resource), such as a Dynatrace dashboard, workflow, or custom alert.

Additionally, it provides data sources such as the entity ID of a service detected by Dynatrace.
The Dynatrace Terraform provider allows you to pull information from these data sources into Dynatrace.

## Advantages of using the Dynatrace Terraform Provider

* No manual edits in production.
* Scale configs via teams and stages.
* Keep configs or environments in sync.
* Recreate configs (e.g., for purposes of disaster recovery).
* Elevate Terraform features such as loops.
* Group components in modules for reusability.
* Team onboarding for building new apps and templating.

## Steps

* To install Terraform CLI, see [Install Terraform CLI and set up Configuration as Code via Terraform](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.").

* Check the [Terraform basic example](/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example "Simple example of creating a management zone with Dynatrace Configuration as Code via Terraform.").
* Check the [Terraform advanced example](/managed/deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example "Advanced example of creating a management zone with Dynatrace Configuration as Code via Terraform.").

## Learn more

Official Terraform documentation:

* [Terraform Documentation﻿](https://developer.hashicorp.com/terraform/docs)
* [Terraform Tutorials﻿](https://developer.hashicorp.com/terraform/tutorials)

Further Dynatrace documentation and material:

* [GitHub Repository: `terraform-provider-dynatrace`﻿](https://github.com/dynatrace-oss/terraform-provider-dynatrace)
* [Terraform Registry: Dynatrace Terraform Provider﻿](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs)

Getting Started with Dynatrace Terraform