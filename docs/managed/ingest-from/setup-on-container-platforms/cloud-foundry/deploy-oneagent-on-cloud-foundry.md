---
title: Deploy BOSH release for Full-Stack monitoring on Cloud Foundry
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry
scraped: 2026-05-12T11:11:01.027325
---

# Deploy BOSH release for Full-Stack monitoring on Cloud Foundry

# Deploy BOSH release for Full-Stack monitoring on Cloud Foundry

* 6-min read
* Updated on Oct 12, 2022

The following guidelines apply to the deployment of Dynatrace OneAgent to Cloud Foundry VMs, including Cloud Foundry components, Diego cells, and Windows Diego cells.

There are two approaches for the deployment of the OneAgent BOSH release: immutable and lightweight. See the [deployment strategies](/managed/ingest-from/setup-on-container-platforms/cloud-foundry "Set up and configure Dynatrace on Cloud Foundry.") to decide which approach suits your needs.

Immutable release

Lightweight release

1. [Create a PaaS Token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").
2. [Deploy an Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") (SaaS customers only).
3. Locate the download URLsâcheck documentation for the [Deployment API](/managed/dynatrace-api/environment-api/deployment "Download OneAgent and ActiveGate installers via Dynatrace API."), which is part of the Environment API v1.
4. Get the latest versions of the BOSH release.

   ```
   curl -X GET https://{api-url}/api/v1/deployment/boshrelease/versions/unix -H /



   'Authorization: Api-Token {paas-token}'
   ```
5. Download the BOSH release.

   For Dynatrace SaaS, replace `{api-url}` with the address of the environment ActiveGate.

   ```
   wget  -O dynatrace-release.tgz --header="Authorization: Api-Token {paas-token}" /



   https://{api-url}/api/v1/deployment/boshrelease/agent/unix/version/{version}?skipMetadata=true
   ```

   Download Windows BOSH release

   ```
   wget  -O dynatrace-release.tgz --header="Authorization: Api-Token {paas-token}" /



   https://{api-url}/api/v1/deployment/boshrelease/agent/windows/version/{version}?skipMetadata=true
   ```
6. Confirm the checksum of the release.

   For Dynatrace SaaS, replace `{api-url}` with the address of the environment ActiveGate.

   ```
   curl -H "Authorization: Api-Token {paas-token}"  /



   https://{api-url}/api/v1/deployment/boshrelease/agent/windows/version/{version}/checksum?skipeMetadata=true



   # this results in a response as follows (example):



   {"sha256":"13658655d922aedc93951b545e8b881b76a77545ba6f8442828cfed53ffac3a8"}



   # use the sha256 value to check against the file:



   echo "13658655d922aedc93951b545e8b881b76a77545ba6f8442828cfed53ffac3a8 dynatrace-release.tgz" | sha256sum -c



   # if the checksum matches the response is:



   dynatrace-release.tgz: OK



   # if the checksum doesn't match:



   # dynatrace-release.tgz FAILED



   # sha256sum: WARNING: 1 computed checksum did NOT match
   ```
7. Ensure that your BOSH CLI is successfully connected to the BOSH Director. For details, see the Cloud Foundry or VMware Tanzu documentation.
8. Upload the BOSH release of OneAgent to the BOSH Director.

   ```
   bosh -e my-env upload-release PATH-TO-BINARY/dynatrace-release.tgz
   ```
9. Create a runtime configuration named `runtime-config-dynatrace.yml` and adapt the settings according to your environment:

   * The `apiurl` key:

   For Dynatrace SaaS, where OneAgent can connect to the internet

   Replace the Dynatrace `ENVIRONMENTID` in `https://ENVIRONMENTID.live.dynatrace.com/api` with your own environment ID.

   For Dynatrace SaaS, where OneAgent can't connect to the internet

   Use `https://YourActiveGateIP` or `FQDN:9999/e/<ENVIRONMENTID>/api` to download the OneAgent, as well as to communicate OneAgent traffic through the ActiveGate.

   We recommend that you use an ActiveGate as a connection endpoint. By default, ActiveGates have a self-signed certificate. However, if you prefer to use a trusted CA rather than the self-signed certificate, or if you're getting SSL errors during install after switching to the ActiveGate endpoint, follow the [instructions on how to properly set up your ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

   For Dynatrace Managed

   Use `https://YourActiveGateIP`, or `FQDN/e/<ENVIRONMENTID>/api`, or the server IP address of your ActiveGate to connect to your server directly.  
   Depending on your settings, you may need the port as well.

   We recommend that you use an ActiveGate as a connection endpoint. By default, ActiveGates have a self-signed certificate. However, if you prefer to use a trusted CA rather than the self-signed certificate, or if you're getting SSL errors during install after switching to the ActiveGate endpoint, follow the [instructions on how to properly set up your ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

   * Optional Configure network zones:  
     To configure network zones, use the following installer argument: `--set-network-zone=<your.network.zone>`.  
     See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

   ```
   releases:



   - name: dynatrace-oneagent



   version: 1.187.100.20200217-114813



   addons:



   - name: dynatrace-oneagent-addon



   jobs:



   - name: dynatrace-oneagent



   release: dynatrace-oneagent



   properties:



   dynatrace:



   environmentid: <environmentId>



   # The following keys are required for 1.177+ immutable OneAgent release



   apitoken: <paas-token>



   ###



   # optional properties below



   ###



   # Replace with your Dynatrace Managed URL, including the environment ID.



   # An example URL might look like the following



   apiurl: https://{your-managed-cluster.com}/e/{environmentid}/api



   # Set to 'all' if you want to accept all self-signed SSL certificates.



   sslmode: all



   # Specify the proxy to be used for communication. This setting is for BOSH only.



   # If you're using a proxy from an ActiveGate, leave this option commented out.



   proxy: https://your-proxy-url



   # Specify in which hostgroup the VMs in this deployments belong



   hostgroup: example_hostgroup



   # Define host tags for the VMs in this deployment



   hosttags: landscape=production team=my_team



   # Define custom properties for the VMs in this deployment



   hostprops: Department=Acceptance Stage=Sprint



   # Enable cloud infrastructure monitoring mode.



   # Set this to 1 to activate it



   infraonly: 0



   # Enable validation of the download via certificate



   # Set this to true to active it



   validatedownload: false



   # Hand over any installer argumentâ



   # Use either this OR the hostgroup, hosttags, infraonly, proxy properties.â



   # Usage of 'installerargs' will overwrite the others!â



   # (Linux only) Usage of USER= and GROUP= arguments will change user and group for plugin and network agents



   installerargs: USER=vcap GROUP=vcap --set-network-zone=<your.network.zone>



   include:



   deployments:



   - name-of-your-deployment



   stemcell:



   - os: ubuntu-xenial



   exclude:



   lifecycle: errand
   ```
10. Update the BOSH Director runtime configuration.

    Replace `PATH` with the path to the `runtime-config-dynatrace.yml` file.

    ```
    bosh -e my-env update-runtime-config PATH/runtime-config-dynatrace.yml
    ```

    This runtime configuration applies to all new BOSH deployments going forward.

    If you have multiple BOSH runtime configurations with different OneAgent versions, you must delete the older ones using `bosh delete-config`.
11. Deploy your changes.

    Since existing BOSH deployments wonât be automatically updated with the jobs specified in the runtime configuration, you need to redeploy them so that BOSH rolls out the OneAgent.

    ```
    bosh -e my-env -d deployment deploy
    ```

This version isn't recommended for controlled production environments as it automatically downloads the latest OneAgent release with each `bosh deploy`.

The latest OneAgent release can be controlled in the [OneAgent updates](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux.") section of your Dynatrace environment.

1. Download the lightweight OneAgent BOSH release from the Dynatrace [Github repositoryï»¿](https://github.com/Dynatrace/bosh-oneagent-release)
2. Ensure that your BOSH CLI is successfully connected to the BOSH Director. For details, see the Cloud Foundry or VMware Tanzu documentation.
3. Upload the BOSH release of OneAgent to the BOSH Director.

   ```
   bosh -e my-env upload-release PATH-TO-BINARY/dynatrace-release.tgz
   ```
4. Create a runtime configuration named `runtime-config-dynatrace.yml` and adapt the settings according to your environment:

   * The `apiurl` key:

   For Dynatrace SaaS, where OneAgent can connect to the internet

   Replace the Dynatrace `ENVIRONMENTID` in `https://ENVIRONMENTID.live.dynatrace.com/api` with your own environment ID.

   For Dynatrace SaaS, where OneAgent can't connect to the internet

   Use `https://YourActiveGateIP` or `FQDN:9999/e/<ENVIRONMENTID>/api` to download the OneAgent, as well as to communicate OneAgent traffic through the ActiveGate.

   We recommend that you use an ActiveGate as a connection endpoint. By default, ActiveGates have a self-signed certificate. However, if you prefer to use a trusted CA rather than the self-signed certificate, or if you're getting SSL errors during install after switching to the ActiveGate endpoint, follow the [instructions on how to properly set up your ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

   For Dynatrace Managed

   Use `https://YourActiveGateIP`, or `FQDN/e/<ENVIRONMENTID>/api`, or the server IP address of your ActiveGate to connect to your server directly.  
   Depending on your settings, you may need the port as well.

   We recommend that you use an ActiveGate as a connection endpoint. By default, ActiveGates have a self-signed certificate. However, if you prefer to use a trusted CA rather than the self-signed certificate, or if you're getting SSL errors during install after switching to the ActiveGate endpoint, follow the [instructions on how to properly set up your ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

   * Optional Configure network zones:  
     To configure network zones, use the following installer argument: `--set-network-zone=<your.network.zone>`.  
     See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

   ```
   releases:



   - name: dynatrace-oneagent



   version: 1.3.2



   addons:



   - name: dynatrace-oneagent-addon



   jobs:



   - name: dynatrace-oneagent



   release: dynatrace-oneagent



   properties:



   dynatrace:



   environmentid: <environmentId>



   # The following keys are required for 1.177+ immutable OneAgent release



   apitoken: <paas-token>



   ###



   # optional properties below



   ###



   # Replace with your Dynatrace Managed URL, including the environment ID.



   # An example URL might look like the following



   apiurl: https://{your-managed-cluster.com}/e/{environmentid}/api



   # Set to 'all' if you want to accept all self-signed SSL certificates.



   sslmode: all



   # Specify a direct download URL for Dynatrace OneAgent.



   # If this propery is set, BOSH will download OneAgent from this location.



   downloadurl: https://direct-download-url-for-agent



   # Specify the proxy to be used for communication. This setting is for BOSH only.



   # If you're using a proxy from an ActiveGate, leave this option commented out.



   proxy: https://your-proxy-url



   # Specify in which hostgroup the VMs in this deployments belong



   hostgroup: example_hostgroup



   # Define host tags for the VMs in this deployment



   hosttags: landscape=production team=my_team



   # Define custom properties for the VMs in this deployment



   hostprops: Department=Acceptance Stage=Sprint



   # Enable cloud infrastructure monitoring mode.



   # Set this to 1 to activate it



   infraonly: 0



   # Enable validation of the download via certificate



   # Set this to true to active it



   validatedownload: false



   # Hand over any installer argumentâ



   # Use either this OR the hostgroup, hosttags, infraonly, proxy properties.â



   # Usage of 'installerargs' will overwrite the others!â



   # (Linux only) Usage of USER= and GROUP= arguments will change user and group for plugin and network agents



   installerargs: USER=vcap GROUP=vcap --set-network-zone=<your.network.zone>



   include:



   deployments:



   - name-of-your-deployment



   stemcell:



   - os: ubuntu-xenial



   exclude:



   lifecycle: errand



   # optional: extra addon configuration for Windows cells



   - name: dynatrace-oneagent-windows-addon



   jobs:



   - name: dynatrace-oneagent-windows



   release: dynatrace-oneagent



   properties:



   dynatrace:



   environmentid: <environmentId>



   apitoken: <paas-token>



   # All of the optional properties for the Linux addon shown above (for example, apiurl, hostgroup) can also be used here.



   include:



   deployments:



   - name-of-your-deployment



   stemcell:



   - os: windows1803



   exclude:



   lifecycle: errand
   ```
5. Update the BOSH Director runtime configuration.

   Replace `PATH` with the path to the `runtime-config-dynatrace.yml` file.

   ```
   bosh -e my-env update-runtime-config PATH/runtime-config-dynatrace.yml
   ```

   This runtime configuration applies to all new BOSH deployments going forward.

   If you have multiple BOSH runtime configurations with different OneAgent versions, you must delete the older ones using `bosh delete-config`.
6. Deploy your changes.

   Since existing BOSH deployments wonât be automatically updated with the jobs specified in the runtime configuration, you need to redeploy them so that BOSH rolls out the OneAgent.

   ```
   bosh -e my-env -d deployment deploy
   ```

## Related topics

* [Cloud Foundry monitoring](/managed/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")
* [OneAgent platform and capability support matrix](/managed/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")