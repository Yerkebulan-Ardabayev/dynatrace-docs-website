---
title: Deploy OneAgent on Cloud Foundry for application-only monitoring
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring
---

# Deploy OneAgent on Cloud Foundry for application-only monitoring

# Deploy OneAgent on Cloud Foundry for application-only monitoring

* 2-min read
* Published Jul 19, 2017

Applications deployed on Cloud Foundry are usually run through technology-specific buildpacks that provide framework and runtime support for applications running on the Cloud Foundry platform. For complete details, see [how buildpacks work﻿](https://docs.cloudfoundry.org/buildpacks/understand-buildpacks.html).

When deployed in application-only mode, OneAgent monitors the memory, disk, CPU, and networking of processes within the container only. Host metrics aren't monitored.

## Prerequisites

* Create a [PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
* Review the [supported applications and versions](/managed/ingest-from/technology-support#applications-services-and-databases "Find technical details related to Dynatrace support for specific platforms and development frameworks.").

## Deploy OneAgent

1. Create a Dynatrace service in your Cloud Foundry environment.  
   There are two ways of defining a service instance, choose one:

   Option 1: Create a user-provided service

   Create a single service instance for Dynatrace with the name `dynatrace` as a substring, like in the example below. You will then be prompted for your environment ID and API token. The API token corresponds to the token mentioned above.

   ```
   cf cups dynatrace-service -p "environmentid, apitoken, apiurl"
   ```

   The `apiurl` parameter specifies the API endpoint of your Dynatrace Cluster and needs to be set to `https://<YourDynatraceClusterURL>/e/<environmentID>/api`. This parameter is optional. If not provided, the default SaaS endpoint will be used. In case there is no direct connection to the SaaS endpoint, the ActiveGate one might be used: `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/`.

   Option 2: Create a service instance via service broker

   If you want to maintain Dynatrace credentials in a central location, use a service broker. For details, visit [GitHub﻿](https://github.com/dynatrace-innovationlab/dynatrace-service-broker).
   You need to configure and run the broker as an application, add the service broker to Cloud Foundry, enable service access to users, and finally, create the service instance.
2. Bind Dynatrace service to your application.

   You can bind the created Dynatrace service to your application in your `manifest.yml` file. If your application is already started, you need to restage it.

   ```
   ---



   applications:



   - name: demo-helloworld



   path: target/JavaHelloWorldApp.war



   buildpack: https://github.com/cloudfoundry/java-buildpack.git



   memory: 512M



   instances: 1



   host: hello-world-${random-word}



   disk_quota: 1024M



   services:



   - dynatrace-service
   ```

   Starting end of May 2026, libbuildpack v1.9.0 and all buildpacks that include it support [file-based VCAP services﻿](https://docs.cloudfoundry.org/devguide/services/application-binding.html#file-based-vcap-services) as an alternative to environment variable-based service credentials.
3. Optional Configure the default OneAgent log stream for Cloud Foundry.

   By default, OneAgent logs are written to the Cloud Foundry standard error stream. All you have to do is set the environment variable `DT_LOGSTREAM` to either `stdout` or `stderr`.

   For example:

   ```
   cf set-env APP_NAME DT_LOGSTREAM stdout
   ```
4. Optional Configure a proxy address.

   If your environment uses a proxy, you need to set the `DT_PROXY` environment variable to pass the proxy credentials to OneAgent as shown below.

   ```
   cf set-env <application> DT_PROXY <proxy address>
   ```
5. Optional Configure network zones.

   You can configure network zones in two ways.

   * Via `UserProvidedService`:

   ```
   cf cups dynatrace-service -p "environmentid, apitoken, networkzone"
   ```

   * As an environment variable per application:

   ```
   cf set-env <application> DT_NETWORK_ZONE <your_network_zone>
   ```

   See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.
6. Optional Configure additional code modules

   You can configure additional code modules via `UserProvidedService`:

   ```
   cf cups dynatrace-service -p "environmentid, apitoken, addtechnologies"
   ```

   The `addtechnologies` parameter accepts a comma-separated list (without whitespaces).
   See supported values [supported values](/managed/dynatrace-api/environment-api/deployment/oneagent/download-oneagent-version#parameters "Download the OneAgent installer of the specific version via Dynatrace API.")
   in the "include" row.

   This is required to monitor additional technologies in multi-buildpack and sidecar deployment scenarios with Cloud Foundry.

   **Important**:

   * Setting unsupported values will break the deployment, since this directly affects the download instructions.
   * Adding code modules will increase the disk space requirements.

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")