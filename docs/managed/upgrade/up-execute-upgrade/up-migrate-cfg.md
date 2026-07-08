---
title: Migrate configuration
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-cfg
---

# Migrate configuration

# Migrate configuration

* Updated on May 29, 2026

Dynatrace offers several tools to help you successfully migrate your configuration from a Dynatrace Managed environment to the SaaS environment. The table below will help you select the appropriate tool for your environment, your configuration experience, and the [upgrade approach](/managed/upgrade/up-plan#which-approach "A detailed overview of what you need to plan, prepare, and consider before upgrading to Dynatrace SaaS.") you intend to follow.

To avoid configuration compatibility issues, update your Dynatrace Managed deployment to the latest version. The best practice is to update Dynatrace Managed to the same version as your SaaS environment.

## Select a tool

| Tool name | Should I use it? |
| --- | --- |
| [SaaS Upgrade Assistant](/managed/upgrade/saas-upgrade-assistant "Import your Dynatrace Managed environment configuration to SaaS.")  Recommended | The SaaS Upgrade Assistant lets you easily import your Dynatrace Managed configuration to your SaaS environment and edit it in simple UI. |
| [Configuration as Code overview](/managed/deliver/configuration-as-code "Use Dynatrace configuration as code via Monaco or Terraform.") | If you already use [Configuration as Code via Monaco overview](/managed/deliver/configuration-as-code/monaco "Manage your Dynatrace environment using Dynatrace Configuration as Code via Monaco.") or [Configuration as Code via Terraform overview](/managed/deliver/configuration-as-code/terraform "Manage your Dynatrace environment using Dynatrace Configuration as Code via Terraform."), you can repoint the target to your SaaS environment. |

## Get started

Use one of the following migration procedures, depending on your selected tool.

### Migrate using SaaS Upgrade Assistant

Recommended

To migrate your configuration using the SaaS Upgrade Assistant, see [SaaS Upgrade Assistant](/managed/upgrade/saas-upgrade-assistant "Import your Dynatrace Managed environment configuration to SaaS.").

With this approach, you export the Dynatrace Managed environment's configuration in the Cluster Management Console and upload it to the app.

### Migrate using Monaco

To migrate your configuration using Monaco

1. [Install Dynatrace Configuration as Code via Monaco](/managed/deliver/configuration-as-code/monaco/installation "Download and install Dynatrace Configuration as Code via Monaco.") on a host with network access to your Dynatrace Managed cluster (for example, to the cluster node itself).
2. Create a deployment [manifest](/managed/deliver/configuration-as-code/monaco/configuration "Manage the Dynatrace configuration files using Monaco with a set of projects and a deployment manifest."): `manifest.yaml`
3. For each environment that you want to migrate, add a configuration:

   * In the environment’s web UI, go to **Access tokens** and select **Generate new token**.
   * Type a token name and set a feasible expiration date.
   * Select the scopes below:

     + **Read configuration**
     + **Read settings**
     + **Read SLO**
     + **Access problem and event feed, metrics, and topology**
     + **Create and read synthetic monitors, locations, and nodes**
   * Store the token in a secret place. For example, use a password manager.
   * Create an operating system environment variable with the token value. For example, on Linux systems:

     ```
     export ENV_TOKEN_PRODUCTION_FIN= dt0c01.abc123.abcdefjhij1234567890
     ```
   * Add the environment data to the `manifest.yaml`:

     + Add the name to the `projects` field
     + In the **managed** environmentGroup, input the URL with a token

     Example `manifest.yaml`:

     ```
     manifestVersion: 1.0



     projects:



     - name: production-fin



     - name: production-logistics



     environmentGroups:



     - name: managed



     environments:



     - name: production-fin



     url:



     value: https://foo123.dynatrace-managed.com/e/1231aaa1-1111-434e-8111-11abcd1234a1



     token:



     name: MIGRATION_TOKEN_PROD_FIN



     - name: production-logistics



     url:



     value: https://foo123.dynatrace-managed.com/e/2345bbb3-3333-456b-1566622abcd3456a1



     token:



     name: MIGRATION_TOKEN_PROD_LOGISTICS
     ```
4. Run Monaco using the download command:  
   `monaco download manifest manifest.yaml`

5. Create your SaaS environment configuration. Apply the steps described in step 3 above, but set the token scope as follows:

   * **Read Configuration**
   * **Write Configuration**
   * **Read settings**
   * **Write settings**
   * **Read SLO**
   * **Write SLO**
   * **Access problem and event feed, metrics, and topology**
   * **Create and read synthetic monitors, locations, and nodes**
     Store the token in a secure place (for example, use a password manager).
6. Change data privacy settings.

   Example:

   ```
   environmentGroups:



   - name: saas



   environments:



   - name: abc1234456



   url:



   value: https://abc1234456.live.dynatrace.com



   token:



   name: ENV_TOKEN_SAAS
   ```
7. Run Monaco using the deploy command:
   `monaco deploy -e saas`
8. Resolve problems and conflicts as stated in the output log.
   Use `skipDeployment: "true"` for unsupported or duplicated configurations and recreate them manually.

Now your configuration should be replicated in your new SaaS environment.

### Migrate using Terraform

To migrate your configuration using Configuration as Code via Terraform, follow the [migration guide](/managed/deliver/configuration-as-code/terraform/guides/migration "Migrate configurations between Dynatrace environments using Dynatrace Configuration as Code via Terraform.").

## Settings that require manual migration

The SaaS Upgrade Assistant is based on the Dynatrace Configuration as Code implementation, which does not support all of the settings that you may use. To ensure a complete configuration migration, you need to check and manually migrate the additional settings listed below.

See the [supported configuration API types](/managed/deliver/configuration-as-code/monaco/reference/supported-configuration#configs "Configuration types and access permissions for Dynatrace Configuration as Code via Monaco") of Dynatrace Configuration as Code.

* [Extensions 1.0](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.") and [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") configuration, including endpoint credentials
* [AWS](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Monitor AWS with Dynatrace") credentials
* [Azure](/managed/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace") credentials
* [GCP](/managed/observe/infrastructure-observability/cloud-platform-monitoring/gcp-monitoring "Monitor Google Cloud with Dynatrace") monitoring
* [Cloud Foundry](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.") credentials
* [Kubernetes/Openshift](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.") credentials
* [Heroku monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/heroku "Monitor Heroku with Dynatrace.")
* [VMware platform](/managed/observe/infrastructure-observability/vmware-vsphere-monitoring "Monitor VMware vSphere with Dynatrace.") monitoring
* [Credential vault](/managed/manage/credential-vault "Store and manage credentials in the credential vault.")
* Access [tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") and [personal access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens/personal-access-token "Learn the concept of a personal access token and its scopes.")
* [Problem notifications](/managed/analyze-explore-automate/notifications-and-alerting/problem-notifications "Learn how to integrate third-party problem notification systems with Dynatrace.") integration, such as Jira, OpsGenie, PagerDuty, Trello, VictorOps, and xMatters
* [Push notifications](/managed/analyze-explore-automate/notifications-and-alerting/push-notifications-via-the-dynatrace-mobile-app "Learn how you can connect your Dynatrace environments with the Dynatrace mobile app to receive problem alerts.") via the Dynatrace mobile app
* [Metrics](/managed/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.") not linked to instances
* Web application usability analytics - [rage clicks](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#rage-event "Learn about user and error events and the types of user and error events captured by Dynatrace.")
* [JavaScript errors](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors#configure-javascript-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.")
* [Mobile symbolication](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")
* [Request naming](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming "Adjust request naming and define the operations your services offer.") order
* [Merged services](/managed/observe/application-observability/services/service-detection/service-detection-v1/service-types/merged-services "Consolidate multiple web-request services of the same process group into one service.")
* Key requests and their references
* Server-side service deep monitoring settings: Real-time updates to Java and PHP services
* Server-side service deep monitoring settings: Exclude noisy exceptions
* Server-side service deep monitoring settings: Exclude incoming web request URLs
* Server-side service deep monitoring settings: Capture SQL bind variables
* [Multi-dimensional analysis](/managed/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.") saved views
* [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") saved queries
* [Custom service rules](/managed/observe/application-observability/services/service-detection/service-detection-v1/customize-service-detection "Use detection rules to customize and enhance the automated detection of your services.") order
* [Remote environments](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboards-multi-environment "Create dashboards that display data from multiple Dynatrace environments.")
* [Account management](/managed/manage/account-management "Manage your Dynatrace license, accounts, platform adoption, and environment health.") - users, groups, permissions, and IAM policies
* Custom devices
* Tags manually applied to entities
* Custom entity names and descriptions (e.g., [process groups](/managed/observe/infrastructure-observability/process-groups "Analyze process groups and customize process group naming, detection, and monitoring."))

  Migrate process groups before upgrading

  If you have simple detection rules, advanced detection rules, or declarative process grouping rules on Dynatrace Managed, you need to migrate them to [Process Grouping Rules](/managed/observe/infrastructure-observability/process-groups/configuration/unified-process-grouping/process-grouping-rules-migration "Learn how to migrate your process groups and process group instances to process grouping rules.") before upgrading to SaaS.

Questions?

Visit the [Upgrade to SaaS forum﻿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.