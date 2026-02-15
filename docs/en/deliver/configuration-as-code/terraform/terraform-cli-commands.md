---
title: Terraform CLI commands
source: https://www.dynatrace.com/docs/deliver/configuration-as-code/terraform/terraform-cli-commands
scraped: 2026-02-15T21:28:02.843972
---

# Terraform CLI commands

# Terraform CLI commands

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Nov 10, 2025

Terraform CLI offers a wide variety of commands to manage your resources. In this section, we provide a high-level outline of the main commands. As these commands are not Terraform-related and not specifically for the Dynatrace Terraform provider, you can find details in the [Terraform documentationï»¿](https://developer.hashicorp.com/terraform/docs).

## Main Terraform commands

You can use the following native commands with the Dynatrace Terraform provider:

* `init`: Prepares your working directory for other commands.
* `validate`: Checks whether the configuration is valid.
* `plan`: Shows changes required by the current configuration.
* `apply`: Creates or updates the infrastructure.
* `destroy`: Destroys the previously created infrastructure.

Additionally, Dynatrace implements the following command specifically for the Dynatrace Terraform provider:

* `export`: Exports the existing Dynatrace resources from a given Dynatrace environment.
  [Terraform CLI examples](/docs/deliver/configuration-as-code/terraform/terraform-cli-commands#terraform-cli-examples "This is a list of Terraform CLI commands.") provides examples of how to use the `export` command.

## Export configuration from a Dynatrace environment using the Dynatrace Terraform Provider

In addition to Terraform's out-of-the-box functionality, the Dynatrace Terraform Provider can be executed as a standalone executable to export an existing configuration from a Dynatrace environment. This functionality provides an alternative to manually creating a Terraform configuration and an easy way to create templates based on an existing configuration.

When exporting resources, consider appropriate permission scopes for fetching the desired configuration items.

### Prerequisites

* [Install Terraform CLI and set up Configuration as Code via Terraform](/docs/deliver/configuration-as-code/terraform/terraform-cli "Install the Terraform CLI and set up Dynatrace Configuration as Code via Terraform.") and make it available in your `PATH`.
* Create a [platform token or OAuth client](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.") with the correct access permissions.
  The correct permissions depends on which APIs you use.
  For more info, see the API documentation or [IAM policy reference](/docs/manage/identity-access-management/permission-management/manage-user-permissions-policies/advanced/iam-policystatements "Complete reference of IAM policies and corresponding conditions across all Dynatrace services.").

### Using the export utility

1. Define the environment variables to identify the Dynatrace tenant for configuration retrieval, according to the [API support and access permission handling](/docs/deliver/configuration-as-code/terraform/terraform-api-support-access-permission-handling "Outlines the different options the Terraform provider can use to authenticate Dynatrace API calls.").

   Optionally, set the environment variable `DYNATRACE_TARGET_FOLDER` to designate an output directory (export folder). If not set, the default directory `.configuration` is used.
2. Go to the Terraform Dynatrace Provider executable in the terminal. This executable isn't generic, such as `terraform.exe` or `./terraform`.

   Typically, you can find it in the `.terraform/providers/registry.terraform.io/dynatrace-oss/dynatrace/{provider_version}/{os_version}/terraform-provider-dynatrace_x.y.z/` directory.
3. Directly invoke the executable with the options you need. The export is an additional functionality; invoking the plugin directly is OK, and you can ignore the warning.

   Windows

   Linux

   ```
   terraform-provider-dynatrace.exe -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]'
   ```

   ```
   ./terraform-provider-dynatrace -export [-ref] [-migrate] [-import-state] [-id] [-flat] [-exclude] [<resourcename>[=<id>]]'
   ```

### Commands

The `list-exclusions` command provides an overview of resources that won't get exported unless explicitly specified.
This does not perform an export.
It isn't intended to be used in conjunction with other options.

Windows

Linux

```
terraform-provider-dynatrace.exe -export -list-exclusions
```

```
./terraform-provider-dynatrace -export -list-exclusions
```

By default, ![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards** (`dynatrace_json_dashboard`) and other resources are excluded from the export unless the resource is directly specified. Use the `-list-exclusions` command for a complete list of the excluded resources.

### Options and flags

* `-ref`: Enable resources with data sources and dependencies.
* `-migrate`: Enable resources with dependencies, excluding data sources.
* `-import-state`: Initialize Terraform modules and import resources into the state.
* `-id`: Display commented id output in resource files.
* `-flat`: Store all resources directly within the target folder without a module structure.
* `-exclude`: Exclude specified resources from export.

## Example usage

The table below describes various use cases for the Dynatrace-specific `export` command, as well example commands to achieve the desired outcome.
For simplicity, only Linux examples are provided.

Use case

Example

Export all configurations without data sources/dependencies.

```
./terraform-provider-dynatrace -export
```

Export all configurations with data sources/dependencies and include commented IDs.

```
./terraform-provider-dynatrace -export -ref -id
```

Export all configurations with data sources/dependencies including specified resources in the exclusion list.

```
./terraform-provider-dynatrace -export -ref * dynatrace_document dynatrace_platform_slo
```

Export specific configuration.

```
./terraform-provider-dynatrace -export dynatrace_document dynatrace_platform_slo
```

Export specific configurations and their dependencies.

```
./terraform-provider-dynatrace -export -ref dynatrace_platform_slo dynatrace_automation_workflow
```

Export specific alerting profiles by their IDs.

```
./terraform-provider-dynatrace -export -ref dynatrace_automation_workflow=4f5942d4-3450-40a8-818f-c5faeb3563d0 dynatrace_automation_workflow=9c4b75f1-9a64-4b44-a8e4-149154fd5325
```

Export multiple resources including dependencies.

```
./terraform-provider-dynatrace -export -ref dynatrace_document dynatrace_automation_workflow=4f5942d4-3450-40a8-818f-c5faeb3563d0
```

Export all configurations and import them into the state.

```
./terraform-provider-dynatrace -export -import-state
```

Export all service-level objectives and import them into the state.

```
./terraform-provider-dynatrace -export -import-state dynatrace_platform_slo
```

Export all configurations except specified resources.

```
./terraform-provider-dynatrace -export -ref -exclude dynatrace_platform_slo dynatrace_automation_workflow
```

## Additional information

During a Terraform export, it's possible that certain files cannot be processed correctly.
These files are moved to the following directories in the export folder, see [Using the export utility](/docs/deliver/configuration-as-code/terraform/terraform-cli-commands#export "This is a list of Terraform CLI commands.").
The reasons are added as comments at the beginning of each file.

* `.flawed`: The files in this directory are either deprecated or require modifications.
* `.required_attention`: The files in this directory lack essential information for a Terraform to be applied.
  This may be due to sensitive data or instances where the files require additional attention.
  (For example, `dynatrace_credentials` confidential strings are not available via the API.)