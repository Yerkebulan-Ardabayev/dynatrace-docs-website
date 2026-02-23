---
title: Set up Dynatrace on Heroku
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/heroku
scraped: 2026-02-23T21:23:08.304957
---

# Set up Dynatrace on Heroku

# Set up Dynatrace on Heroku

* Latest Dynatrace
* 6-min read
* Updated on Jun 23, 2023

Heroku is a cloud Platform as a Service (PaaS) that enables you to build and run applications in the cloud. Applications deployed to Heroku are usually run through one or more buildpacks that provide framework and runtime support.

## Capabilities

The Heroku buildpack for Dynatrace OneAgent is language independent and can be used with any [Dynatrace supported language](/docs/ingest-from/technology-support#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks."), including Node.js-based applications. If youâve used the [Dynatrace NPM module for PaaS moduleï»¿](https://www.npmjs.com/package/@dynatrace/oneagent), you can remove it from your dependencies as the buildpack discovers and instruments your Node.js applications automatically.

You also no longer need to rely on releases of the Dynatrace OneAgent dependencies for NPM. The Heroku buildpack for Dynatrace OneAgent automatically fetches the latest version of Dynatrace OneAgent so that you can receive potential fixes as quickly and easily as possible. If youâve specified [a default OneAgent installation version for new hosts and applications in your OneAgent update settings](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), the Heroku buildpack for Dynatrace OneAgent will download the defined default version of Dynatrace OneAgent.

The following guidelines explain how to enable Dynatrace monitoring for your [Herokuï»¿](https://www.dynatrace.com/technologies/heroku-monitoring/) applications by adding a [Dynatrace Heroku buildpackï»¿](https://github.com/Dynatrace/heroku-buildpack-dynatrace) to the Heroku configuration of your application.

The Dynatrace Heroku buildpack enables you to monitor all [supported languages on Linux systems](/docs/ingest-from/technology-support#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Prerequisites

* Create a [PaaS Token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Review the list of [supported applications and versions](/docs/ingest-from/technology-support "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* The [OneAgent code module memory requirement](/docs/ingest-from/dynatrace-oneagent/oa-requirements#oneagent-code-module-memory-requirement "OneAgent code module requirements") is 200 MB of your [slug sizeï»¿](https://devcenter.heroku.com/articles/slug-compiler#slug-size).

## Installation

These guidelines explain how to integrate Dynatrace OneAgent into your Heroku dynos and begin monitoring your Heroku applications.

### Get the Heroku CLI

To configure Heroku applications to use the Dynatrace Heroku buildpack, you can either use the [Heroku CLIï»¿](https://devcenter.heroku.com/articles/heroku-cli) or you can configure your applications using the [Heroku dashboardï»¿](https://dashboard.heroku.com).

### Add the Dynatrace Heroku buildpack

To integrate Dynatrace OneAgent into your existing application, you need to add the Dynatrace Heroku buildpack to your application buildpacks and set your Dynatrace environment ID and PaaS token using the commands below.

```
# Add the Dynatrace buildpack



heroku buildpacks:add https://github.com/Dynatrace/heroku-buildpack-dynatrace.git#<version>



# Set required credentials to your Dynatrace environment



heroku config:set DT_TENANT=<environmentID>



heroku config:set DT_API_TOKEN=<token>



# Deploy to Heroku



git push heroku master
```

Once you push these changes, the buildpack installs Dynatrace OneAgent to automatically monitor your application.

### Additional configuration

The Dynatrace Heroku buildpack supports the following configurations:

| Environment variable | Description |
| --- | --- |
| DT\_TENANT | Your Dynatrace environment ID **Note:** For details on how to determine your environment ID, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). |
| DT\_API\_TOKEN | The PaaS token for integrating your Dynatrace environment with Heroku. |
| DT\_API\_URL | - For Dynatrace SaaS, where OneAgent can connect to the internet: `https://<your-environment-ID>.live.dynatrace.com/api` - For Dynatrace Managed: `https://<your-managed-cluster-domain>/e/<your-environment-ID>/api` - For environment ActiveGates (SaaS or Managed), use the following to download the OneAgent, as well as to communicate OneAgent traffic through the ActiveGate: `https://<your-ActiveGate-IP-or-FQDN>:9999/e/<your-environment-ID>/api` **Note:** For details on how to determine your environment ID, see [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). |
| DT\_DOWNLOAD\_URL | Optional A direct download URL for Dynatrace OneAgent. If this environment variable is set, the buildpack will download OneAgent from this location |
| SSL\_MODE | Optional Set to `all` if you want to accept all self-signed SSL. certificates |
| DT\_TAGS | not recommended The tags you want to add to the monitored. applications |
| DT\_CUSTOM\_PROP | not recommended Apply if you want to split by the component and/or environment. |
| SKIP\_ERRORS | Optional If set to `1`, application deployment won't fail on OneAgent installer download errors |

We recommend creating environment variables specific to process detection. Environment variables that serve other scopes, such as [`DT_TAGS`](/docs/manage/tags-and-metadata/setup/define-tags-based-on-environment-variables#variables "Find out how Dynatrace enables you to define tags based on environment variables.") or [`DT_CUSTOM_PROP`](/docs/observe/infrastructure-observability/process-groups/configuration/define-your-own-process-group-metadata#variables "Configure your own process-related metadata based on the unique needs of your organization or environment."), might cause incorrect or unintentional splits because all values of environment variables are evaluated for process-group detection.

How to use the Heroku buildpack for Dynatrace OneAgent in place of the Dynatrace NPM module for PaaS

The Heroku buildpack for Dynatrace OneAgent requires no changes to your application source code:

You no longer need to install a dependency on `@dynatrace/oneagent` in the project directory of your Node.js application.
Also, youâre no longer required to add the following statement as the first statement of your Node.js application:

```
try {



require('@dynatrace/oneagent')();



} catch(err) {



console.log(err.toString());



}
```

Because of these advantages, the Heroku buildpack for Dynatrace OneAgent supersedes the Dynatrace NPM module for PaaS and requires OneAgent version 1.141+.

If youâre eager to start using the Heroku buildpack for Dynatrace OneAgent instead of the Dynatrace NPM module for PaaS, weâve got you covered. All you have to do is remove the dependency on `@dynatrace/oneagent` in your `package.json` file:

```
$ npm uninstall --save @dynatrace/oneagent
```

Further, you can also remove the `require` statement mentioned above from your Heroku application.

You can use a different Dynatrace environment for Heroku applications that are enriched with OneAgent.

How to use a different Dynatrace environment for Heroku applications enriched with OneAgent

For OneAgent version 1.139+, if you have an existing Heroku application where you have already added the OneAgent code modules for a specific Dynatrace environment, you can have the OneAgent report to another Dynatrace environment.

To do this you need to make a call to the REST endpoint of your second Dynatrace environment. Don't forget to adapt the respective placeholders `<environmentID>` and `<token>`.

```
curl "https://<environmentID>.live.dynatrace.com/api/v1/deployment/installer/agent/connectioninfo?Api-Token=<token>"
```

In return, you get a JSON object that covers the required information that needs to be passed as an environment variable to the application container. Make sure you set the environment variables of your Heroku application as described below:

* `DT_TENANT`: equals `tenantUUID`
* `DT_TENANTTOKEN`: equals `tenantToken`
* `DT_CONNECTION_POINT`: semi-colon separated list of `communicationEndpoints`

### Configure network zones Optional

You can configure network zones via an environment variable:

```
heroku config:set DT_NETWORK_ZONE=<your.network.zone>
```

See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

## Update OneAgent

When a new version of OneAgent becomes available, you need to trigger a rerun of the buildpack in Heroku. The Dynatrace buildpack will automatically fetch the latest version of OneAgent.

If you've specified a default OneAgent install version for new hosts and applications in your [OneAgent updates settings](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), the Heroku buildpack will automatically fetch the defined default version of OneAgent.

## Related topics



* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")