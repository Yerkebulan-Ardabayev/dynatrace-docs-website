---
title: SaaS Upgrade Assistant
source: https://docs.dynatrace.com/managed/upgrade/saas-upgrade-assistant
scraped: 2026-05-12T12:16:04.575549
---

# SaaS Upgrade Assistant

# SaaS Upgrade Assistant

* Updated on Dec 13, 2024

Latest Dynatrace

![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** imports your Dynatrace Managed environment configuration and enables Dynatrace Managed cluster administrators to navigate through a frictionless upgrade from their Dynatrace Managed on-premises deployment to the SaaS deployment model. A cluster administrator can import the configuration to the target SaaS environment and update it to align with SaaS environment requirements. The app ensures a faster migration and minimizes disruption to Dynatrace users by incorrect environment configuration. Automation eliminates time-consuming manual tasks, such as updating dashboard ownership or adjusting entity IDs that have changed between environments.

## What can SaaS Upgrade Assistant SaaS Upgrade Assistant do?

Currently, with ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** you can

* Track configuration migration progress.
* Browse imported configurations and review failed configurations marked in red.
* Troubleshoot failed and skipped configurations with ease thanks to error messages.
* Fix a single configuration with an edit form or update hundreds of configurations at a time using bulk mode. You can leverage preview changes to make sure the update is correct.
* Choose which configurations you want to migrate and run partial deployment.
* [Automatically update dashboard owners](/managed/upgrade/saas-upgrade-assistant/sua-update-dashboard-owners "Update dashboard owners automatically with SaaS Upgrade Assistant.").

## How to export the configuration from Dynatrace Managed?

1. Sign in the Dynatrace Managed **Cluster Management Console**.
2. Go to **Environments**.
3. Select an environment that you want to migrate from.
4. Select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Export configuration**.
5. Confirm the operation and navigate to your target local directory to store the archive.

For more information, see [Update configuration in SaaS Upgrade Assistant](/managed/upgrade/saas-upgrade-assistant/sua-update-config "Learn how to update configuration in SaaS Upgrade Assistant.").

## How to install, update, or uninstall SaaS Upgrade Assistant SaaS Upgrade Assistant?

To install, update, or uninstall the SaaS Upgrade Assistant, in [Dynatrace Hubï»¿](https://docs.dynatrace.com/docs/shortlink/hub), select ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**. Then select either **Install**, **Update**, or **Uninstall** to perform this action in your environment.

If you want to uninstall ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant**, note that

* The upgrade status and any uploaded configurations will be deleted after 30 days of inactivity. You can reinstall the app during this time and your data will still be there, or you can keep the app but the data will still be deleted after 30 days if you don't use it.
* Configurations that have already been deployed by ![SaaS Upgrade Assistant](https://dt-cdn.net/images/saas-upgrade-assistant-61dc5b83c0.svg "SaaS Upgrade Assistant") **SaaS Upgrade Assistant** will persist.

## What versions are SaaS Upgrade Assistant SaaS Upgrade Assistant compatible with?

We recommend working on a configuration exported from the same major version of the Dynatrace Managed cluster and SaaS environment to avoid unnecessary false-positive failed configuration migrations. For example, your Dynatrace Managed cluster should be in version 1.284.123, and your SaaS environment should be in 1.284.89.