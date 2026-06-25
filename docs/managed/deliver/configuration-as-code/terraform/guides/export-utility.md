---
title: Export utility
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/guides/export-utility
scraped: 2026-05-12T12:02:50.498896
---

# Export utility

# Export utility

* How-to guide
* 4-min read
* Updated on Jul 01, 2024

In addition to the out-of-the-box functionality of Terraform, the provider has the ability to be executed as a standalone executable to export an existing configuration from a Dynatrace environment. This functionality provides an alternative to manually creating a Terraform configuration and provides an easy way to create templates based on an existing configuration.

## Prerequisites

* [Terraform CLI with the Dynatrace provider installed](/managed/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.") and available under `PATH`.
* [Access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") with at least the following permissions:

  + **Read settings** (`settings.read`)
  + **Write settings** (`settings.write`)
  + **Read configuration** (`ReadConfig`)
  + **Write configuration** (`WriteConfig`)
  + **Create and read synthetic monitors, locations, and nodes** (`ExternalSyntheticIntegration`)
  + **Capture request data** (`CaptureRequestData`)
  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read network zones** (`networkZones.read`)
  + **Write network zones** (`networkZones.write`)

## Export guide

1. Define the environment URL and API token in a terminal window. This identifies the Dynatrace tenant for configuration retrieval.

   Windows

   Linux

   ```
   set DYNATRACE_ENV_URL=https://<dynatrace-host>/e/########



   set DYNATRACE_API_TOKEN=dt0c01.########.########
   ```

   ```
   export DYNATRACE_ENV_URL=https://<dynatrace-host>/e/########



   export DYNATRACE_API_TOKEN=dt0c01.########.########
   ```

Optionally, set `DYNATRACE_TARGET_FOLDER` to designate an output directory. If not set, the default `./configuration` is used.

1. Go to the Terraform Dynatrace Provider executable in the terminal. This isn't the generic executable, such as `terraform.exe` or `./terraform`. Typically, it's found in `.terraform/providers/registry.terraform.io/dynatrace-oss/dynatrace/{provider_version}/{os_version}/terraform-provider-dynatrace_x.y.z`.
2. Directly invoke the executable with any needed options. Because export is additional functionality, it's OK to invoke the plugin directly, and the warning can be safely ignored. For examples, see the [Usage examples](#usage-examples) section below.

   **Windows**: `terraform-provider-dynatrace.exe -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]`

   **Linux**: `./terraform-provider-dynatrace -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]`

### Options

* `-ref`: Enable resources with data sources and dependencies.
* `-migrate`: Enable resources with dependencies, excluding data sources. See more in the [Migration guide](/managed/deliver/configuration-as-code/terraform/guides/migration "Migrate configurations between Dynatrace environments using Dynatrace Configuration as Code via Terraform.").
* `-import-state`: Initialize terraform modules and import resources into the state.
* `-id`: Display commented id output in resource files.
* `-flat`: Store all resources directly within the target folder without a module structure.
* `-exclude`: Exclude specified resources from export.
* `-list-exclusions`: Prints an overview of resources that will not get exported unless explicitly specified.

By default, dashboards (`dynatrace_json_dashboard`) and various other resources are excluded from the export unless the resource is directly specified. Use the option `-list-exclusions` for a full list of the excluded resources.

### Usage examples

The following examples demonstrate various ways to use the export utility.

* Export all configurations without data sources/dependencies:

  ```
  ./terraform-provider-dynatrace -export
  ```
* Export all configurations with data sources/dependencies and include commented IDs:

  ```
  ./terraform-provider-dynatrace -export -ref -id
  ```
* Export all configurations with data sources/dependencies including specified resources in the exclusion list:

  ```
  ./terraform-provider-dynatrace -export -ref * dynatrace_json_dashboard dynatrace_document
  ```
* Export specific configuration:

  ```
  ./terraform-provider-dynatrace -export dynatrace_json_dashboard dynatrace_document
  ```
* Export specific configurations and their dependencies:

  ```
  ./terraform-provider-dynatrace -export -ref dynatrace_json_dashboard dynatrace_web_application
  ```
* Export specific alerting profiles by their IDs:

  ```
  ./terraform-provider-dynatrace -export -ref dynatrace_alerting=4f5942d4-3450-40a8-818f-c5faeb3563d0 dynatrace_alerting=9c4b75f1-9a64-4b44-a8e4-149154fd5325
  ```
* Export multiple resources including dependencies:

  ```
  ./terraform-provider-dynatrace -export -ref dynatrace_calculated_service_metric dynatrace_alerting=4f5942d4-3450-40a8-818f-c5faeb3563d0
  ```
* Export all configurations and import them into the state:

  ```
  ./terraform-provider-dynatrace -export -import-state
  ```
* Export specific web applications and import them into the state:

  ```
  ./terraform-provider-dynatrace -export -import-state dynatrace_web_application
  ```
* Export all configurations except specified resources:

  ```
  ./terraform-provider-dynatrace -export -ref -exclude dynatrace_calculated_service_metric dynatrace_alerting
  ```

### Additional information

* Some exported configurations might be deprecated or require modifications. Such files are moved to the `.flawed` directory in the output folder, with reasons provided as comments at the beginning of the file.
* Some configurations might lack essential information for a `terraform apply` due to sensitive data or instances where the files require additional attention. These files are moved to `.requires_attention`, with explanations provided as comments at the beginning of the file.

  For example, `dynatrace_credentials` confidential strings are not available via the API.