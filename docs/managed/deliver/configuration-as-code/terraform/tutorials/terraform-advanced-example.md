---
title: Terraform advanced example
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/tutorials/terraform-advanced-example
scraped: 2026-05-12T11:21:32.505428
---

# Terraform advanced example

# Terraform advanced example

* Tutorial
* 3-min read
* Updated on Jul 01, 2024

This section guides you through an advanced example of creating a Dynatrace configuration template for a newly deployed application with Dynatrace Configuration as Code via Terraform.

## Prerequisites

* [Terraform CLI with the Dynatrace provider installed](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.") and available under `PATH`.
* [Access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") with at least the following permissions:

  + **Read settings** (`settings.read`)
  + **Write settings** (`settings.write`)

  To create a token that works for all configurations, also include the following permissions.

  + **Read configuration** (`ReadConfig`)
  + **Write configuration** (`WriteConfig`)
  + **Create and read synthetic monitors, locations, and nodes** (`ExternalSyntheticIntegration`)
  + **Capture request data** (`CaptureRequestData`)
  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read network zones** (`networkZones.read`)
  + **Write network zones** (`networkZones.write`)

## Build configuration

In this example, we'll utilize a JSON input file to automate the creation of a management zone, alerting profile, and email notification for each defined application.

1. In your working directory, create a `main.tf` file with the following content.

   The configuration below uses a `locals` block to access the contents of `data.json` within the `resource` blocks.

   For more information on each resource, refer to the [Terraform Registryï»¿](https://dt-url.net/1ta37uo) documentation.

   ```
   locals {



   app_data = jsondecode(file("data.json"))



   }



   resource "dynatrace_management_zone_v2" "mgmz_per_app" {



   for_each = local.app_data



   name = each.key



   rules {



   rule {



   type    = "ME"



   enabled = true



   attribute_rule {



   entity_type           = "HOST"



   host_to_pgpropagation = true



   attribute_conditions {



   condition {



   case_sensitive = true



   key            = "HOST_GROUP_NAME"



   operator       = "EQUALS"



   string_value   = each.value["host-group"]



   }



   }



   }



   }



   }



   }



   resource "dynatrace_alerting" "alerting_per_app" {



   for_each = dynatrace_management_zone_v2.mgmz_per_app



   name            = each.value.name



   management_zone = each.value.legacy_id



   rules {



   rule {



   delay_in_minutes = local.app_data[each.value.name]["delay-in-minutes"]



   include_mode     = "NONE"



   severity_level   = "MONITORING_UNAVAILABLE"



   }



   }



   }



   resource "dynatrace_email_notification" "email_notification_per_app" {



   for_each = dynatrace_alerting.alerting_per_app



   name                   = each.value.name



   subject                = "{State} Problem {ProblemID}: {ImpactedEntity}"



   to                     = local.app_data[each.value.name]["notify"]



   body                   = "{ProblemDetailsHTML}"



   profile                = each.value.id



   active                 = true



   notify_closed_problems = true



   }
   ```
2. Create a `data.json` file with the following content.

   ```
   {



   "App-A": {



   "host-group": "group-a",



   "delay-in-minutes": 20,



   "notify": ["app.a.owner@dynatrace.com"]



   },



   "App-B": {



   "host-group": "group-b",



   "delay-in-minutes": 30,



   "notify": ["app.b.owner@dynatrace.com"]



   }



   }
   ```

   In the provided JSON configuration, we've defined two applications: `"App-A"` and `"App-B"`. These names will be consistently used for creating the management zone, alerting profile, and email notification. Each application is associated with the following attributes:

   * `host-group`: Refers to the [host group](/managed/observe/infrastructure-observability/hosts/configuration/organize-your-environment-using-host-groups#assign-a-host-to-a-host-group "Find out how Dynatrace enables you to organize your hosts, processes, and services using host groups.") associated with the application. Used for management zone rule.
   * `delay-in-minutes`: Specifies the duration (in minutes) that the monitoring unavailable event remains open before triggering an alert. For more information, see [alerting profile](/managed/analyze-explore-automate/notifications-and-alerting/alerting-profiles "Learn how to create and manage alerting profiles.").
   * `notify`: Lists the recipients of the [email notification](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications/email-integration "Get email whenever Dynatrace detects a problem in your environment that affects real users.").
3. Open a terminal window and set the tenant URL and API token environment variables. This is the tenant on which we want to push the configuration.

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
4. Run the `terraform apply -auto-approve` command, which displays an execution plan detailing the changes to be made.

   ```
   dynatrace_management_zone_v2.mgmz_per_app["App-A"]: Creating...



   dynatrace_management_zone_v2.mgmz_per_app["App-A"]: Creation complete after 1s [id=*************]



   dynatrace_management_zone_v2.mgmz_per_app["App-B"]: Creating...



   dynatrace_management_zone_v2.mgmz_per_app["App-B"]: Creation complete after 0s [id=*************]



   dynatrace_alerting.alerting_per_app["App-B"]: Creating...



   dynatrace_alerting.alerting_per_app["App-B"]: Creation complete after 1s [id=*************]



   dynatrace_alerting.alerting_per_app["App-A"]: Creating...



   dynatrace_alerting.alerting_per_app["App-A"]: Creation complete after 0s [id=*************]



   dynatrace_email_notification.email_notification_per_app["App-B"]: Creating...



   dynatrace_email_notification.email_notification_per_app["App-B"]: Creation complete after 1s [id=*************]



   dynatrace_email_notification.email_notification_per_app["App-A"]: Creating...



   dynatrace_email_notification.email_notification_per_app["App-A"]: Creation complete after 1s [id=*************]



   Apply complete! Resources: 6 added, 0 changed, 0 destroyed.
   ```

Upon successful execution, the management zone, alerting profile, and email notification configurations for `"App-A"` and `"App-B"` will be established in the Dynatrace environment.

To change or destroy the configuration, refer back to the examples in [Terraform basic example](/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example "Simple example of creating a management zone with Dynatrace Configuration as Code via Terraform.")

## Related topics

* [Export utility](/managed/deliver/configuration-as-code/terraform/guides/export-utility "Export existing Dynatrace configurations using Dynatrace Configuration as Code via Terraform.")