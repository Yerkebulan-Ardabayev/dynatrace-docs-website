---
title: Upgrade your deployment
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade
scraped: 2026-05-12T12:07:09.123083
---

# Upgrade your deployment

# Upgrade your deployment

* Updated on Aug 03, 2023

![Executing Managed to SaaS upgrade](https://dt-cdn.net/images/upgrade-to-saas-upgrade-3454-35eeb82133.png)

Executing Managed to SaaS upgrade

During this phase, the platform, infrastructure, and monitoring components are migrated. This includes licensing, SaaS environments, infrastructure, Dynatrace configurations, integrations and all application or infrastructure monitoring sources.

First, the new Dynatrace SaaS platform and accompanying infrastructure should be prepared. Next, the configuration, integrations, and applications should be systematically migrated.

## Step 1 - Prepare

Main objectives of this step:

* Clarify potential changes in licensing
* Provision Dynatrace environment
* Deploy necessary infrastructure

This step focuses on preparing the new Dynatrace platform (including the SaaS environment), all supporting infrastructure components and configurations to support ActiveGates, and required network flows.

### Request the provisioning of Dynatrace environments

Dynatrace provisions new SaaS environments in your account for you in the available hyper scaler and region. This requires the setup of proper licensing for your SaaS environments and includes the dual running of the Managed cluster. Share information on the planned migration timeline and expected growth.

### Pre-configure new environments

After the SaaS environment is provisioned, environment pre-configuration is addressed. This includes:

* Configuring your accountâSSO, users, and permissions
* Configuring proxy, DNS, and corporate firewalls if needed
* Checking with the Dynatrace Support team if custom feature flags have to be set
* Validating that licensing is correctly set up for all of your environments

## Step 2 - Execute

Main objectives of this step:

* Migrate configurations
* Migrate ActiveGates
* Migrate OneAgents

In this step, all monitoring configuration is applied to the Dynatrace environment. Furthermore, the below actions are advised:

### Migrate configuration

A Dynatrace environment may contain many individual configuration items. Manual migration may cause delays in the project and increase the likelihood of errors. Follow the procedure described in [Migrate configuration](/managed/upgrade/up-execute-upgrade/up-migrate-cfg "Migrate your Dynatrace Managed environment configuration using Monaco.") to migrate the configuration most efficiently.

#### Validate configuration

Once configurations have been transferred, it is important to validate that all the relevant configurations have been migrated successfully. This will ensure that the environment has all the necessary configurations to continue processing data once the OneAgents are switched over to the SaaS platform and provides a seamless cutover for Dynatrace users.

For the most critical configurations, review them manually by comparing your environments. You can also use a JSON `diff` combined with the Dynatrace REST API.

Once the migrated configuration has been validated, the Dynatrace SaaS environment is ready to start receiving OneAgent traffic.

### Migrate ActiveGates

ActiveGate's primary purpose is to route OneAgent traffic to Dynatrace, monitor cloud environments, or monitor remote technologies using extensions. Therefore, before migrating OneAgents, ensure they can securely and successfully connect to the Dynatrace environment by [migrating your ActiveGate](/managed/upgrade/up-execute-upgrade/up-migrate-ag "Migrate your ActiveGate configuration to SaaS.") instances. In the second step, migrate ActiveGates responsible for Synthetic and z/OS monitoring.

### Migrate OneAgents

The OneAgent migration involves the reconfiguration or reinstallation of all OneAgents from the Dynatrace Managed, to the new SaaS environment. This step requires careful planning and coordination. Take into consideration the deployment and maintenance procedures of the wider application environment.

OneAgents should be migrated as soon as the configuration migration has been completed. This will minimize the delta between the environments and will provide for the smoothest transition to the new platform.

A series of steps is repeated for every application to be migrated. Using the priority-based plan, migrate each application with the steps described below.

#### Reconfigure the OneAgent to the SaaS environment

All OneAgents deployed in the customer environment must be reconfigured to point to the new Dynatrace environment. OneAgent may be deployed on cloud platforms, container platforms, or operating systems.

There are two approaches for redirecting OneAgents to the new SaaS environment:

* Update and reconfigure OneAgent in place (recommended) - for details, see [Migrate OneAgent](/managed/upgrade/up-execute-upgrade/up-migrate-oa "Migrate your OneAgent configuration to SaaS.")
* Reinstall OneAgent

We recommend that you use the automated solution. Also ensure that Host Group, Network Zone, and Custom Metadata are set correctly during installation, as per the architectural design created in the upgrade guide.

#### Restart application processes and make sure the applications are observed in the Dynatrace environment

OneAgent injection into monitored processes only happens during application startup, and until the application processes are restarted, the OneAgent will continue to point to the Dynatrace Managed environment. After the OneAgents have been reconfigured, you must restart all application processes where OneAgent is configured in the full stack for deep application monitoring.

### Validate monitoring

As the last step of the migration, validate that the application data is flowing seamlessly into the new environment, hosts, processes, services, and applications appear as expected, custom settings are in place and alerting/notifications are configured the same.

Review data in the SaaS environment to ensure everything looks correct and data and metrics are flowing as expected.

We recommend regularly validating the state of the upgrade by:

* Cross-checking configuration in the old environment and new environments, assure that integrations work and that ActiveGates is configured the right way
* Engaging with your teams using Dynatrace and letting them check that all monitoring is set up in the way they expect

### Migrate Dynatrace Operator

If you deployed Dynatrace Operator to a Kubernetes cluster, you can [migrate Kubernetes monitoring from your Managed cluster to your SaaS environment](/managed/upgrade/up-execute-upgrade/up-migrate-dto "Migrate your Dynatrace Operator configuration to SaaS.") by reconfiguring the Dynatrace Operator deployment.

### Migrate Dynatrace extensions

If you extend Dynatrace observability with extensions, you need to perform additional steps to gather data from them in the SaaS environment. The migration steps to migrate extensions vary depending on the extension type and version.

* [Migrate OneAgent extension](/managed/upgrade/up-execute-upgrade/up-migrate-oa-extension "Migrate your OneAgent extension to SaaS.")
* [Migrate ActiveGate extension](/managed/upgrade/up-execute-upgrade/up-migrate-ag-extension "Migrate your ActiveGate extension to SaaS.")

## Step 3 - Integrate

Main objectives of this step:

* Update external integrations to communicate with SaaS environments
* Ensure your monitoring and alerting landscape is re-integrated after migration

All third-party integrations previously used with the Dynatrace Managed cluster need to be updated and validated. Configure and review all integrations and ensure that end-to-end workflows are operational. Examples include service management platforms, automation platforms for automated remediation, CI/CD pipelines, and reporting systems.

### Update automation that uses Dynatrace API

Any API access should be updated to use the new environment. This requires the generation of new API tokens, as existing tokens canât be migrated due to security reasons.

Questions?

Visit the [Upgrade to SaaS forumï»¿](https://community.dynatrace.com/t5/Upgrade-to-SaaS/bd-p/upgrade_to_saas) to ask questions, get answers, and share what you've learned with others.