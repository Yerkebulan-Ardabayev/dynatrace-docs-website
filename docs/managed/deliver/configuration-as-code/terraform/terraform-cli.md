---
title: Install Terraform CLI and set up Configuration as Code via Terraform
source: https://docs.dynatrace.com/managed/deliver/configuration-as-code/terraform/terraform-cli
scraped: 2026-05-12T11:21:31.157280
---

# Install Terraform CLI and set up Configuration as Code via Terraform

# Install Terraform CLI and set up Configuration as Code via Terraform

* How-to guide
* 2-min read
* Updated on Jul 01, 2024

This guide describes how to install the Terraform CLI and set up the Dynatrace Terraform Provider.

## Install Terraform CLI

Start by installing Terraform on your system as described in the [Terraform documentationï»¿](https://dt-url.net/hd037k2).

1. Download the binary according to your operating system.
2. Set the `PATH` to ensure the Terraform binary is accessible system-wide.
3. Verify the setup by opening a new terminal session and running the following command:

   ```
   terraform version
   ```

## Set up the Dynatrace Terraform Provider

The Dynatrace Provider is available in the Terraform Registry and can be fetched automatically during the `terraform init` process.

1. Create a working directory for your Terraform configuration files.
2. Within this directory, create a `providers.tf` file. Use the configuration block below.

   ```
   terraform {



   required_providers {



   dynatrace = {



   version = "~> 1.0"



   source = "dynatrace-oss/dynatrace"



   }



   }



   }
   ```
3. Navigate to your working directory in a terminal and execute the following command.

   ```
   terraform init
   ```

   You should see output similar to:

   ```
   Initializing the backend...



   Initializing provider plugins...



   - Finding dynatrace-oss/dynatrace versions matching "x.y.z"...



   - Installing dynatrace-oss/dynatrace x.y.z...



   - Installed dynatrace-oss/dynatrace x.y.z (signed by a HashiCorp partner, key ID *************)



   ...



   Terraform has been successfully initialized!
   ```

**Next step**: [Terraform basic example](/managed/deliver/configuration-as-code/terraform/tutorials/teraform-basic-example "Simple example of creating a management zone with Dynatrace Configuration as Code via Terraform.")