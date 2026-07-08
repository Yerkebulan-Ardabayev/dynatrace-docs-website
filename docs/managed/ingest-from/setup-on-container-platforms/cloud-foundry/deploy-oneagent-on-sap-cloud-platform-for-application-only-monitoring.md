---
title: Deploy OneAgent on SAP Business Technology Platform for application-only monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring
---

# Deploy OneAgent on SAP Business Technology Platform for application-only monitoring

# Deploy OneAgent on SAP Business Technology Platform for application-only monitoring

* 3-min read
* Published Jul 19, 2017

Applications deployed on Cloud Foundry are usually run through technology-specific buildpacks that provide framework and runtime support for applications running on the Cloud Foundry platform. For complete details, see [how buildpacks work﻿](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html).

When deployed in application-only mode, OneAgent monitors the memory, disk, CPU, and networking of processes within the container only. Host metrics aren't monitored.

The following guidelines apply to **SAP Business Technology Platform (SAP BTP)**.

## Prerequisites

Generate an [Access token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") with the following permissions:

* **Access problem and event feed, metrics, and topology**
* **PaaS integration - Installer download**

## Deploy OneAgent on SAP BTP Cloud Foundry Runtime

SAP BTP, Cloud Foundry Environment hosts [a number of buildpacks﻿](https://help.sap.com/viewer/4505d0bdaf4948449b7f7379d24d0f0d/2.0.05/en-US/684a8a79827047998b3c1e8519dec10f.html). You can use these guidelines with the following buildpack integrations:

* SAP Java Buildpack
* [Java Buildpack﻿](https://github.com/cloudfoundry/java-buildpack)
* [PHP Buildpack﻿](https://github.com/cloudfoundry/php-buildpack)
* [Staticfile Buildpack﻿](https://github.com/cloudfoundry/staticfile-buildpack)
* [Cloud Foundry Node.js Buildpack﻿](https://github.com/cloudfoundry/nodejs-buildpack).

The SAP Java Buildpack is maintained by SAP. If you experience issues with the SAP Java Buildpack, please refer to component `BC-XS-JAV` and issue a ticket at SAP Support Portal. The other buildpacks listed above are maintained by the Cloud Foundry Foundation on GitHub. If you experience issues with the integration of Dynatrace into these buildpacks, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create a user-provided service in your SAP BTP, Cloud Foundry Environment**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring#create-service "Install OneAgent on SAP Business Technology Platform.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Bind the Dynatrace service to your application**](/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring#bind-service-to-app "Install OneAgent on SAP Business Technology Platform.")

### Step 1 Create a user-provided service in your SAP BTP, Cloud Foundry Environment

Create a single service instance for Dynatrace with the name `dynatrace` as a substring (for example, `dynatraceservice`). You can use the `cf` CLI or directly create a user-provided service with the [SAP Business Technology Platform cockpit﻿](https://account.hana.ondemand.com/cockpit).

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen01-1765-0d4d1d9bf6.webp)

SAP BTB Cockpit

You need to provide a valid JSON object that contains at least the `environmentid` and `apitoken`. The API token corresponds to the PaaS token mentioned above.

For Dynatrace Managed, you also need to add the `apiurl` parameter specifying the [Dynatrace API](/managed/dynatrace-api "Find out what you need to use the Dynatrace API.") endpoint. For example:

#### Dynatrace SaaS

```
{



"environmentid": "YOUR_ENVIRONMENTID",



"apitoken": "YOUR_PAAS_TOKEN",



"tag:SAP BTB": "",



"tag:Region": "Frankfurt"



}
```

#### Dynatrace Managed

```
{



"environmentid": "YOUR_ENVIRONMENTID",



"apitoken": "YOUR_PAAS_TOKEN",



"tag:SAP BTB": "",



"tag:Region": "Frankfurt",



"apiurl": "https://<your-domain>/e/<environmentID>/api"



}
```

### Step 2 Bind the Dynatrace service to your application

You can bind the created Dynatrace service to your application in your `manifest.yml` file. If your application is already started, you need to restage it.

See the example below for pushing a Java application:

```
---



applications:



- name: spring-music



memory: 768M



instances: 1



host: spring-music-somerandomstring



path: spring-music.war



buildpack: sap_java_buildpack



services:



- dynatraceservice
```

Starting end of May 2026, libbuildpack v1.9.0 and all buildpacks that include it support [file-based VCAP services﻿](https://docs.cloudfoundry.org/devguide/services/application-binding.html#file-based-vcap-services) as an alternative to environment variable-based service credentials.

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen02-2042-7f899341e1.webp)

SAP BTB Cockpit

## Deploy OneAgent on SAP BTP Neo Runtime

SAP provides the Dynatrace Agent Activation Neo service which allows you to connect your Java applications to your Dynatrace monitoring environment.

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen03-2087-27ddc3be9f.webp)

SAP BTB Cockpit

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen04-2559-95dea005ca.webp)

SAP BTB Cockpit

Have your Dynatrace [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") and a generated [PaaS token](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") ready.

![SAP BTB Cockpit](https://dt-cdn.net/images/dynatrace-screen05-2556-57631a9d36.webp)

SAP BTB Cockpit

For Managed, enter the URL of your Cluster ActiveGate (including `/e/<environmentID>`) in the **Environment URL** field.

After restarting your Java applications deployed to SAP Business Technology Platform, you’ll receive the full range of application and service monitoring visibility that Dynatrace provides (for example, **Smartscape** and service-level insights with **Service flow**). If you experience issues with the setup of the Dynatrace Agent Activation Neo service, please refer to component `BC-NEO-MON-APM` and issue a ticket at SAP Support Portal. If you experience issues with Dynatrace, please contact a Dynatrace product expert via live chat within your Dynatrace environment.

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")