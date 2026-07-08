---
title: Terraform basic example
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example
---

# Terraform basic example

# Terraform basic example

* Tutorial
* 4-min read
* Updated on Jul 01, 2024

To get you started with managing configurations, this section guides you through a simple example of creating a management zone with Dynatrace Configuration as Code via Terraform. You will learn how to create, update, and destroy a configuration.

## Prerequisites

* [Terraform CLI with the Dynatrace provider installed](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.") and available under `PATH`.
* [Access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") with at least the following permissions:

  + **Read configuration** (`ReadConfig`)
  + **Write configuration** (`WriteConfig`)
  + **Read settings** (`settings.read`)
  + **Write settings** (`settings.write`)

  To create a token that works for all configurations, also include the following permissions.

  + **Create and read synthetic monitors, locations, and nodes** (`ExternalSyntheticIntegration`)
  + **Capture request data** (`CaptureRequestData`)
  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read network zones** (`networkZones.read`)
  + **Write network zones** (`networkZones.write`)

## Build a configuration

Create a management zone for a web application using Terraform.

1. Inside your working directory, create a `main.tf` file with the following content.

   This file contains the Terraform configuration—a set of resource blocks that define the configuration. For more information on management zone resource, refer to the [Terraform Registry﻿](https://registry.terraform.io/providers/dynatrace-oss/dynatrace/latest/docs/resources/management_zone_v2) documentation.

   Consider using the export utility to export existing configurations from the environment.

   ```
   resource "dynatrace_management_zone_v2" "TerraformExample" {



   name = "Terraform Example"



   rules {



   rule {



   type    = "ME"



   enabled = true



   attribute_rule {



   entity_type = "WEB_APPLICATION"



   attribute_conditions {



   condition {



   case_sensitive = true



   key            = "WEB_APPLICATION_NAME"



   operator       = "EQUALS"



   string_value   = "easyTravel"



   }



   }



   }



   }



   }



   }
   ```
2. Open a terminal and set the environment variables for your environment URL and API token. This identifies which tenant you'll be pushing configurations to.

   SaaS

   Managed

   ```
   set DYNATRACE_ENV_URL=https://########.live.dynatrace.com



   set DYNATRACE_API_TOKEN=dt0c01.########.########
   ```

   ```
   set DYNATRACE_ENV_URL=https://<dynatrace-host>/e/########



   set DYNATRACE_API_TOKEN=dt0c01.########.########
   ```
3. In your working directory, run `terraform plan` to generate an execution plan that provides a preview of the changes Terraform intends to make.

   ```
   Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:



   + create



   Terraform will perform the following actions:



   # dynatrace_management_zone_v2.TerraformExample will be created



   + resource "dynatrace_management_zone_v2" "TerraformExample" {



   + id        = (known after apply)



   + legacy_id = (known after apply)



   + name      = "Terraform Example"



   + rules {



   + rule {



   + enabled = true



   + type    = "ME"



   + attribute_rule {



   + entity_type = "WEB_APPLICATION"



   + attribute_conditions {



   + condition {



   + case_sensitive = true



   + key            = "WEB_APPLICATION_NAME"



   + operator       = "EQUALS"



   + string_value   = "easyTravel"



   }



   }



   }



   }



   }



   }



   Plan: 1 to add, 0 to change, 0 to destroy.
   ```
4. After verifying the plan, execute `terraform apply` to implement the proposed changes (in this case, pushing the management zone configuration to the environment).

   ```
   dynatrace_management_zone_v2.TerraformExample: Creating...



   dynatrace_management_zone_v2.TerraformExample: Creation complete after 1s [id=*************)]



   Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
   ```

   After the `apply` command, you'll notice a `terraform.tfstate` file. This is the Terraform state file that is automatically generated to keep track of the resources that Terraform is currently managing. It's crucial for subsequent Terraform operations.

## Modify your configuration

1. Execute `terraform plan`, which should indicate that no changes are needed.

   ```
   dynatrace_management_zone_v2.easyTravel: Refreshing state... [id=*************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. To make a change, edit the `main.tf` file. For instance, you can modify the `string_value` from `"easyTravel"` to `"Terraform"`.

   ```
   resource "dynatrace_management_zone_v2" "TerraformExample" {



   name = "Terraform Example"



   rules {



   rule {



   type    = "ME"



   enabled = true



   attribute_rule {



   entity_type = "WEB_APPLICATION"



   attribute_conditions {



   condition {



   case_sensitive = true



   key            = "WEB_APPLICATION_NAME"



   operator       = "EQUALS"



   string_value   = "Terraform"



   }



   }



   }



   }



   }



   }
   ```
3. After making your changes, execute `terraform apply` that will update the management zone configuration in Dynatrace and adjust the Terraform state file accordingly.

   ```
   dynatrace_management_zone_v2.easyTravel: Modifying... [id=*************]



   dynatrace_management_zone_v2.easyTravel: Modifications complete after 0s [id=*************]



   Apply complete! Resources: 0 added, 1 changed, 0 destroyed.
   ```

## Delete the configuration

1. To remove a configuration, run `terraform plan` to confirm no changes are pending.

   ```
   dynatrace_management_zone_v2.easyTravel: Refreshing state... [id=*************]



   No changes. Your infrastructure matches the configuration.



   Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
   ```
2. To delete the management zone, execute `terraform destroy`.

   ```
   dynatrace_management_zone_v2.easyTravel: Destroying... [id=*************]



   dynatrace_management_zone_v2.easyTravel: Destruction complete after 0s



   Destroy complete! Resources: 1 destroyed.
   ```

The management zone configuration in the Dynatrace environment has been destroyed and the Terraform state file is now empty.

**Next step**: [Terraform advanced example](/managed/deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example "Advanced example of creating a management zone with Dynatrace Configuration as Code via Terraform.")