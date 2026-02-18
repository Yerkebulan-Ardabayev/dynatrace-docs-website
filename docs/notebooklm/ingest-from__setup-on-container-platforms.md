# Dynatrace Documentation: ingest-from/setup-on-container-platforms

Generated: 2026-02-18

Files combined: 7

---


## Source: cloud-foundry.md


---
title: Set up Dynatrace on Cloud Foundry
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/cloud-foundry
scraped: 2026-02-18T05:38:39.662455
---

# Set up Dynatrace on Cloud Foundry

# Set up Dynatrace on Cloud Foundry

* Latest Dynatrace
* 1-min read
* Published Aug 03, 2018

Dynatrace supports full-stack monitoring for Cloud Foundry through the Dynatrace OneAgent BOSH Release, which allows you to deploy OneAgent to your Cloud Foundry cluster VMs, including Diego cells, Cloud Controller, router, and others.

## Integrations

There are two approaches in deploying the OneAgent BOSH release, [immutable](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#immutable "Install OneAgent on Cloud Foundry with BOSH.") and [lightweight](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry#lightweight "Install OneAgent on Cloud Foundry with BOSH."). The differences between these approaches are described below.

Immutable release

Lightweight release

The immutable OneAgent BOSH release is downloaded using the Dynatrace Environment API. This release contains complete packages, binaries, and installation files in the same archive. This fully contained approach is immutable because it gives operators full control over what is deployed and when.

![Immutable release](https://dt-cdn.net/images/bosh-cludfoundry-immutable-500-fbf72def36.png)

The lightweight OneAgent BOSH release downloads and installs a pre-configured OneAgent at deployment time, which guarantees the latest OneAgent binaries and allows for fully automated OneAgent-controlled version updates.

![Lightweight release](https://dt-cdn.net/images/bosh-cloudfoundry-lightweight-500-4ff8ba068b.png)

If you don't have access to BOSH, Dynatrace provides two different approaches for application-only monitoring:

* [OneAgent on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")
* [OneAgent on SAP Business Technology Platform](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-sap-cloud-platform-for-application-only-monitoring "Install OneAgent on SAP Business Technology Platform.")

## Configuration

[Connect your Cloud Foundry clusters with Dynatrace](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/connect-your-cloud-foundry-foundations-to-dynatrace "Enable monitoring on your Cloud Foundry foundations.")

[Install the Dynatrace Service Broker for Cloud Foundry dashboard tile](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/install-the-service-broker-for-cloud-foundry-dashboard-tile "Install and configure the Dynatrace Service Broker for VMware Tanzu Platform dashboard tile.")

## Maintenance

[Update OneAgent on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/update-oneagent-on-cloud-foundry "Update OneAgent on Cloud Foundry based on different deployment strategies.")

[Uninstall OneAgent from Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/uninstall-oneagent-from-cloud-foundry "Uninstall OneAgent from Cloud Foundry for BOSH add-ons.").

## Troubleshooting

[Troubleshoot OneAgent deployment issues on Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/troubleshoot-cf "Troubleshoot deployment problems on Cloud Foundry.")

## Related topics

* [Cloud Foundry monitoringï»¿](https://www.dynatrace.com/technologies/cloud-foundry-monitoring/)
* [Cloud Foundry monitoring](/docs/observe/infrastructure-observability/container-platform-monitoring/cloud-foundry-monitoring "Monitor Cloud Foundry with Dynatrace.")


---


## Source: deploy-dynatrace-oneagent-on-mesos-marathon.md


---
title: Deploy OneAgent on Mesos/Marathon
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/deploy-dynatrace-oneagent-on-mesos-marathon
scraped: 2026-02-18T05:38:46.547917
---

# Deploy OneAgent on Mesos/Marathon

# Deploy OneAgent on Mesos/Marathon

* Latest Dynatrace
* 2-min read
* Published May 21, 2020

Mesos is a generic cluster resource manager which can be used together with the Marathon framework to run containers in distributed environments.

To monitor applications running in [Mesos clustersï»¿](https://www.dynatrace.com/technologies/mesos-monitoring/), we recommend that you deploy OneAgent on all Mesos agent nodes by means of a Marathon application deployment. Following this, install OneAgent on the Mesos master nodes, as explained on this page.

## Locate your OneAgent installer URL

The first step is to obtain the location for `ONEAGENT_INSTALLER_SCRIPT_URL`. This information is presented to you during OneAgent installation.

To get your `ONEAGENT_INSTALLER_SCRIPT_URL`

1. In Dynatrace Hub, select **OneAgent**.
2. Select **Set up** > **Linux**.

3. Determine the installer script URL and token from the UI-provided `wget` command:

OneAgent container image version 1.39.1000+

OneAgent container image version 1.38.1000 and earlier

This is the URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

* Replace the value of `arch` parameter with `<arch>`. Ignore the `flavor=default` parameter.
* For the `API-Token` value, you need a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

Your URL should look like this:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

This your URL and API token.

![OneAgent installation page with URL to be modified](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

Append the API token to the URL using the `API-Token` parameter. Your URL should look like this:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Install OneAgent

1. Deploy OneAgent on Mesos agent nodes.

   If you use DC/OS

   If you don't use DC/OS

   If you're using [DC/OSï»¿](https://www.dynatrace.com/technologies/dcos-monitoring/) to manage your Mesos cluster, you can take advantage of the Dynatrace package in the DC/OS universe. The universe package will automatically deploy Dynatrace to all your Mesos agent nodes.

   If you're not using [DC/OSï»¿](https://www.dynatrace.com/technologies/dcos-monitoring), you can run OneAgent as a Marathon application by following this example.

   * Use the `cat` command to create the `dynatrace-oneagent.json` file. Before you run it, edit the JSON part from the example below and replace the two placeholders with your Mesos cluster specific data:

     + `REPLACE_WITH_YOUR_URL` is the location for `ONEAGENT_INSTALLER_SCRIPT_URL` you determined earlier.
     + `REPLACE_WITH_NUMBER_OF_NODES` is the integer representing the number of nodes in your Mesos cluster.

   ```
   cat <<- EOF > dynatrace-oneagent.json



   {



   "id": "dynatrace-oneagent",



   "cpus": 0.1,



   "mem": 256,



   "instances": REPLACE_WITH_NUMBER_OF_NODES,



   "constraints": [["hostname", "UNIQUE"], ["hostname", "GROUP_BY"]],



   "container": {



   "type": "DOCKER",



   "volumes": [



   {



   "containerPath": "/mnt/root",



   "hostPath": "/",



   "mode": "RW"



   }



   ],



   "docker": {



   "image": "dynatrace/oneagent",



   "forcePullImage": true,



   "network": "HOST",



   "privileged": true,



   "parameters": [



   { "key": "pid", "value": "host" },



   { "key": "ipc", "value": "host" },



   { "key": "env", "value": "ONEAGENT_INSTALLER_SCRIPT_URL=REPLACE_WITH_YOUR_URL" },



   { "key": "env", "value": "ONEAGENT_INSTALLER_SKIP_CERT_CHECK=false "}



   ]



   }



   },



   "args": [



   ]



   }



   EOF
   ```

   * After you created the `dynatrace-oneagent.json` file, send an HTTP POST request to the Mesos master leader to deploy the Marathon application with OneAgent.

   ```
   curl -X POST -H "Content-Type: application/json" http://your-mesos-master:8080/v2/apps -d@dynatrace-oneagent.json
   ```
2. Deploy OneAgent on Mesos master nodes.

   Marathon doesn't allow you to deploy applications to master nodes (except for nodes that are tagged as both master and agent). This is why you must manually install OneAgent on all Mesos master nodes that aren't additionally configured as Mesos agents. For this, use the default [Linux installer](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.").

## Related topics

* [OneAgent platform and capability support matrix](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix "Learn which capabilities are supported by OneAgent on different operating systems and platforms.")


---


## Source: docker.md


---
title: Set up Dynatrace on Docker
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/docker
scraped: 2026-02-18T05:38:58.114992
---

# Set up Dynatrace on Docker

# Set up Dynatrace on Docker

* Latest Dynatrace
* 1-min read
* Published Jun 25, 2021

Dynatrace offers full-featured Docker monitoring, as well as generic container monitoring for containerd and CRI-O, giving you all the same deep monitoring capabilities for containerized applications that are available for non-containerized applications.

## Integrations

If you want to use Docker outside a container platform, there are two methods to monitor applications using OneAgent:

* [Set up OneAgent for application-only](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.")
* [Set up Dynatrace as a Docker container](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.")

In a typical scenario, container orchestration and management tools such as Kubernetes, OpenShift, and Cloud Foundry use Docker, containerd, or CRI-O as a container runtime. If you're running one of these platforms, follow the appropriate deployment instructions: [Kubernetes](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), [OpenShift](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"), [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry "Install OneAgent on Cloud Foundry with BOSH."), or [Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate."). Any platform that uses containers can also be monitored using the [application-only approach](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.").

## Related topics

* [Monitor container groups](/docs/observe/infrastructure-observability/container-platform-monitoring/container-groups "Overview on container groups monitoring")


---


## Source: heroku.md


---
title: Set up Dynatrace on Heroku
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/heroku
scraped: 2026-02-18T05:38:44.770512
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


---


## Source: deploy-oneagent-operator-k8s-legacy.md


---
title: Deploy OneAgent Operator on Kubernetes (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-k8s-legacy
scraped: 2026-02-18T05:43:20.465269
---

# Deploy OneAgent Operator on Kubernetes (deprecated)

# Deploy OneAgent Operator on Kubernetes (deprecated)

* Latest Dynatrace
* 10-min read
* Published May 26, 2020

This procedure is deprecated.

* If you are making a fresh installation, you should [set up Kubernetes monitoring using Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").
* If you already have OneAgent installed using OneAgent Operator, please see the [instructions for migrating to Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Detailed instructions how to migrate from deprecated OneAgent Operator to Dynatrace Operator using kubectl/oc").

## Installation

Find out below how to install and configure OneAgent.

Deploy with kubectl

Deploy with Helm

Prerequisites

* Generate an [API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment.

  Make sure you have the **Access problem and event feed, metrics, and topology** setting enabled for the API token.
* Pods must allow egress to your Dynatrace environment or to your Environment ActiveGate in order for metric routing to work properly.
* See [Support lifecycle](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") for supported Kubernetes versions.

1. Create the necessary objects for OneAgent Operator.

   OneAgent Operator acts on its separate namespace `dynatrace`. It holds the operator deployment and all dependent objects like permissions, custom resources and the corresponding DaemonSet. You can also observe the logs of OneAgent Operator.

   ```
   kubectl create namespace dynatrace
   ```

   ```
   kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
   ```

   ```
   kubectl -n dynatrace logs -f deployment/dynatrace-oneagent-operator
   ```
2. Create the secret holding API and PaaS tokens for authentication to the Dynatrace Cluster.

   The name of the secret is important in a later step when you configure the custom resource (`.spec.tokens`). In the following code-snippet the name is `oneagent`. Be sure to replace `API_TOKEN` and `PAAS_TOKEN` with the values explained in the prerequisites.

   ```
   kubectl -n dynatrace create secret generic oneagent --from-literal="apiToken=API_TOKEN" --from-literal="paasToken=PAAS_TOKEN"
   ```
3. Save custom resource.

   The rollout of Dynatrace OneAgent is governed by a custom resource of type `OneAgent`. Retrieve the `cr.yaml` file from the GitHub repository.

   ```
   curl -o cr.yaml https://raw.githubusercontent.com/Dynatrace/dynatrace-oneagent-operator/master/deploy/cr.yaml
   ```
4. Adapt the values of the custom resource as indicated below.

   If you want to revert an argument, you need to **set it to empty** instead of removing it from the custom resource.  
   Example:

   ```
   args:



   - "--set-proxy="
   ```

   ### Parameters

   | **Parameter** | **Description** | **Default value** |
   | --- | --- | --- |
   | `apiUrl` | Required For **Dynatrace SaaS**, where OneAgent can connect to the internet, replace the Dynatrace `ENVIRONMENTID` in `https://ENVIRONMENTID.live.dynatrace.com/api`. For **Environment ActiveGates** (SaaS or Managed), use the following to download the OneAgent, as well as to communicate OneAgent traffic through the ActiveGate: `https://YourActiveGateIP` or `FQDN:9999/e/<ENVIRONMENTID>/api`. |  |
   | `useUnprivilegedMode` | Optional Set to `false` if you want to mark the pod as privileged. Defaults to using [Linux capabilities for the OneAgent pod](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.") | `true` |
   | `tokens` | Optional Name of the secret that holds the API and PaaS tokens from above. | Name of custom resource (`.metadata.name`) if unset |
   | `useImmutableImage` | Optional Set to `true` if you want to pull a OneAgent Docker image from your Dynatrace environment. Use this parameter together with the `agentVersion` parameter to control the version of OneAgent. | `false` |
   | `agentVersion` | Optional Set this value to the OneAgent version using semantic versioning (`major.minor.patch`). Example: `1.203.0` | latest version |
   | `args` | Optional Parameters to be passed to the OneAgent installer. All the [command line parameters of the installer](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") are supported, with the exception of `INSTALL_PATH`. |  |
   | `env` | Optional Environment variables for OneAgent container. |  |
   | `skipCertCheck` | Optional Disable certificate validation checks for installer download and API communication. Set to `true` if you want to skip any certification validation checks. | `false` |
   | `nodeSelector` | Optional Keep empty default value. If you want to roll out OneAgent to specific nodes only, provide the `nodeSelectors` here. Refer to [Kubernetes docsï»¿](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) for details. |  |
   | `tolerations` | Optional Keep default value to also roll out the OneAgent to primary nodes if possible. If you want to apply additional tolerations to OneAgent pods for tainted nodes, provide them here. Refer to [Kubernetes docsï»¿](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) for details. |  |
   | `image` | Optional Define the OneAgent image to be taken. Defaults to the publicly available OneAgent image on [Docker Hubï»¿](https://hub.docker.com/r/dynatrace/oneagent/). In order to use the certified [OneAgent imageï»¿](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) from [Red Hat Container Catalogï»¿](https://access.redhat.com/containers/) you need to set `.spec.image` to `registry.connect.redhat.com/dynatrace/oneagent` in the custom resource and provide image pull secrets as shown in the next step. | `docker.io/dynatrace/oneagent:latest` if unset |
   | `resources` | Optional Resource requests/limits for the OneAgent pods. These settings heavily depend on size of worker nodes and workloads. Please adjust to fit your needs. |  |
   | `priorityClassName` | Optional Priority class for OneAgent pod. Refer to [Kubernetes docsï»¿](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/). |  |
   | `disableAgentUpdate` | Optional Disable the Operator's auto-update feature for OneAgent pods. | `false` |
   | `enableIstio` | Optional Enable management of Istio service entries and virtual services for Dynatrace endpoints to allow for OneAgent monitoring egress traffic to your Dynatrace environment | `false` |
   | `trustedCAs` | Optional Adds the provided CA certificates to the Operator and the OneAgent; provide the name of the configmap which holds your PEM in a field called `certs`. | If not set, the default embedded certificates on the images will be used. |

   Configuration for Anthos, SUSE CaaS, GKE, IKS, and TKGI

   For Anthos, SUSE CaaS, Google Kubernetes Engine, and VMware Tanzu Kubernetes Grid Integrated Edition (formerly PKE), you must add the following additional parameters to the `env` section in the `cr.yaml` file:

   Anthos and GKE

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"
   ```

   TKGI

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /var/vcap/store
   ```

   IKS

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /opt
   ```

   SUSE CaaS

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"
   ```
5. Create the custom resource.

   ```
   kubectl apply -f cr.yaml
   ```
6. Optional Configure proxy.

   * You can configure optional parameters like proxy settings in the `cr.yaml` file in order to

     + download the OneAgent installer
     + ensure the communication between the OneAgent and your Dynatrace environment
     + ensure the communication between the Dynatrace OneAgent Operator and the Dynatrace API.

   There are two ways to provide the proxy, depending on whether or not your proxy uses credentials.

   No credentials

   If you have a proxy that doesn't use credentials, enter your proxy URL directly in the `value` field for the proxy.

   **Example**

   ```
   apiVersion: dynatrace.com/v1alpha1



   kind: OneAgent



   metadata:



   name: oneagent



   namespace: dynatrace



   spec:



   apiUrl: https://environmentid.dynatrace.com/api



   tolerations:



   - effect: NoSchedule



   key: node-role.kubernetes.io/master



   operator: Exists



   args: []



   enableIstio: true



   proxy:



   value: http://mysuperproxy
   ```

   With credentials

   If your proxy uses credentials

   1. Create a secret with a field called `proxy` which holds your encrypted proxy URL with the credentials.  
      Example.

      ```
      kubectl -n dynatrace create secret generic myproxysecret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
      ```
   2. Provide the name of the secret in the `valueFrom` section.  
      Example.

      ```
      apiVersion: dynatrace.com/v1alpha1



      kind: OneAgent



      metadata:



      name: oneagent



      namespace: dynatrace



      spec:



      apiUrl: https://environmentid.dynatrace.com/api



      tolerations:



      - effect: NoSchedule



      key: node-role.kubernetes.io/master



      operator: Exists



      args: []



      enableIstio: true



      proxy:



      valueFrom: myproxysecret
      ```
7. Optional Configure network zones.

   You can configure network zones by setting the following argument:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

Prerequisites

* Generate an [API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment.

  Make sure you have the **Access problem and event feed, metrics, and topology** setting enabled for the API token.
* Pods must allow egress to your Dynatrace environment or to your Environment ActiveGate in order for metric routing to work properly.
* See [Support lifecycle](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") for supported Kubernetes versions.
* [Install Helm version 3ï»¿](https://helm.sh/docs/intro/install/).

1. Add the Dynatrace OneAgent Helm repository.

   ```
   helm repo add dynatrace \



   https://raw.githubusercontent.com/Dynatrace/helm-charts/master/repos/stable
   ```
2. Create a Dynatrace namespace.

   The Dynatrace OneAgent Operator acts on its separate namespace called **dynatrace**, which holds the operator deployment and all dependent objects like permissions, custom resources, and corresponding DaemonSets.

   ```
   kubectl create namespace dynatrace
   ```
3. Create the custom resource definitions.

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagents.yaml



kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagentapms.yaml
```

4. Create a `values.yaml` file with the following content.

   ```
   platform: "kubernetes"



   operator:



   image: ""



   oneagent:



   name: "oneagent"



   apiUrl: "https://ENVIRONMENTID.live.dynatrace.com/api"



   image: ""



   args: {}



   env: {}



   nodeSelector: {}



   labels: {}



   skipCertCheck: false



   disableAgentUpdate: false



   enableIstio: false



   dnsPolicy: ""



   resources: {}



   waitReadySeconds: null



   priorityClassName: ""



   serviceAccountName: ""



   proxy: ""



   trustedCAs: ""



   secret:



   apiToken: "DYNATRACE_API_TOKEN"



   paasToken: "PLATFORM_AS_A_SERVICE_TOKEN"
   ```

   The OneAgent proxy setting is used by both the Operator and the OneAgent containers when communicating to the Dynatrace environment.

   Configuration for Anthos, SUSE CaaS, GKE, IKS, and TKGI

   For Anthos, SUSE CaaS, Google Kubernetes Engine, and VMware Tanzu Kubernetes Grid Integrated Edition (formerly PKE), you must add the following additional parameters to the `env` section in the `values.yaml` file:

   Anthos, SUSE CaaS, and GKE

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"
   ```

   TKGI

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /var/vcap/store
   ```

   IKS

   ```
   env:



   - name: ONEAGENT_ENABLE_VOLUME_STORAGE



   value: "true"



   - name: ONEAGENT_CONTAINER_STORAGE_PATH



   value: /opt
   ```
5. Optional Configure network zones.

   You can configure network zones by setting the following argument:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.
6. To apply the YAML parameters, run the following command:

   ```
   helm install dynatrace-oneagent-operator \



   dynatrace/dynatrace-oneagent-operator -n\



   dynatrace --values values.yaml
   ```

After deployment, you need to restart your pods so OneAgent can inject into them.

## Cluster-wide permissions

The following table shows the permissions needed for OneAgent Operator.

| **Resources accessed** | **APIs used** | **Resource names** |
| --- | --- | --- |
| `Nodes` | Get/List/Watch | - |
| `Namespaces` | Get/List/Watch | - |
| `Secrets` | Create | - |
| `Secrets` | Get/Update/Delete | `dynatrace-oneagent-config`, `dynatrace-oneagent-pull-secret` |

## Limitations

See [Docker limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container.") for details.

## Troubleshoot

Find out how to [troubleshoot issues](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting#deploy "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.") that you may encounter when deploying OneAgent on Kubernetes.

## Deploy an ActiveGate and connect your Kubernetes API to Dynatrace

Now that you have OneAgent running on your Kubernetes nodes, you're able to monitor those nodes, and the applications running in Kubernetes. The next step is to deploy an ActiveGate and connect your Kubernetes API to Dynatrace in order to get native Kubernetes metrics, like request limits, and differences in pods requested vs. running pods.  
For further instructions see [Deploy ActiveGate in Kubernetes as a StatefulSet](/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.").

## Update OneAgent Operator with kubectl

OneAgent Operator (for Kubernetes version 1.9+) automatically takes care of the lifecycle of the deployed OneAgents, so you don't need to update OneAgent pods yourself.

Review the [release notesï»¿](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases) of the Operator for any breaking changes on the custom resource.

If the custom resource of the new version is compatible with the already deployed version, you can simply set the OneAgent Operator image to the new tagged version. Be sure to replace `vX.Y.Z` with the new version in the following command:

```
kubectl -n dynatrace set image deployment \



dynatrace-oneagent-operator *=quay.io/dynatrace/\



dynatrace-oneagent-operator:vX.Y.Z
```

The image version of the OneAgent Operator is independent from the OneAgent version. To check the available versions for the Operator, see the [OneAgent Operator releasesï»¿](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases).

To update OneAgent Operator, run the following command:

```
kubectl apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
```

## Update OneAgent Operator with Helm

1. Update your Helm repositories.

   ```
   helm repo update
   ```

   Another method of updating the Dynatrace OneAgent Helm repository is adding it again, which overwrites the older version.
2. Update OneAgent to the latest version.

   Don't omit the `--reuse-values` flag in the command in order to keep your configuration.

   ```
   helm upgrade dynatrace-oneagent-operator dynatrace/\



   dynatrace-oneagent-operator -n dynatrace --reuse-values
   ```

## Uninstall OneAgent Operator

Uninstall with kubectl

Uninstall with Helm

To uninstall OneAgent Operator from Kubernetes version 1.9+

1. Remove OneAgent custom resources and clean up all remaining OneAgent Operatorâspecific objects.

   ```
   kubectl delete -n dynatrace oneagent --all



   kubectl delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/kubernetes.yaml
   ```
2. Optional After deleting OneAgent Operator, the OneAgent binary remains on the node in an inactive state. To uninstall it completely, run the `uninstall.sh` script and delete logs and configuration files.  
   See [Linux related information](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").

Remove OneAgent custom resources and clean up all remaining OneAgent Operatorâspecific objects:

```
helm uninstall dynatrace-oneagent-operator -n dynatrace
```

## Related topics

* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")
* [Store Dynatrace images in private registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")
* [Migrate Dynatrace Operator to a new environment](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant "Migrate monitoring to a new Dynatrace environment on Kubernetes clusters.")


---


## Source: deploy-oneagent-operator-openshift-legacy.md


---
title: Deploy OneAgent Operator on OpenShift (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy
scraped: 2026-02-17T21:33:23.058485
---

# Deploy OneAgent Operator on OpenShift (deprecated)

# Deploy OneAgent Operator on OpenShift (deprecated)

* Latest Dynatrace
* 10-min read
* Published May 26, 2020

This procedure is deprecated.

* If you are making a fresh installation, you should [set up OpenShift monitoring using Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").
* If you already have OneAgent installed using OneAgent Operator, please see the [instructions for migrating to Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-to-dto "Detailed instructions how to migrate from deprecated OneAgent Operator to Dynatrace Operator using kubectl/oc").

The instructions below apply to **OpenShift Dedicated** as well. For OpenShift Dedicated, you need [cluster-admin privilegesï»¿](https://docs.openshift.com/dedicated/4/administering_a_cluster/cluster-admin-role.html).

## Installation

Find out below how to install and configure OneAgent.

Deploy with oc

Deploy with Helm

Prerequisites

* Generate an [API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment.

  Make sure you have the **Access problem and event feed, metrics, and topology** setting enabled for the API token.
* Pods must allow egress to your Dynatrace environment or to your Environment ActiveGate in order for metric routing to work properly.
* See [Support lifecycle](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") for supported OpenShift versions.

1. Add a new project.

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. OCP version 3.11 Provide image pull secrets.  
   Skip this step if you're using a later version.  
   In order to use the certified [OneAgent Operatorï»¿](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/dynatrace-oneagent-operator) and [OneAgentï»¿](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) images from [Red Hat Container Catalogï»¿](https://access.redhat.com/containers/) (RHCC), you need to [provide image pull secretsï»¿](https://access.redhat.com/documentation/en-us/openshift_container_platform/3.9/html/developer_guide/dev-guide-managing-images#pulling-private-registries-delegated-auth). The Service Accounts on the `openshift.yaml` manifest already have links to the secrets to be created below.

   ```
   # For OCP 3.11



   oc -n dynatrace create secret docker-registry redhat-connect --docker-server=registry.connect.redhat.com --docker-username=REDHAT_CONNECT_USERNAME --docker-password=REDHAT_CONNECT_PASSWORD --docker-email=unused



   oc -n dynatrace create secret docker-registry redhat-connect-sso --docker-server=sso.redhat.com --docker-username=REDHAT_CONNECT_USERNAME --docker-password=REDHAT_CONNECT_PASSWORD --docker-email=unused
   ```
3. OCP version 4.x OCP version 3.11 Apply the `openshift.yaml` manifest to deploy the OneAgent Operator.

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/openshift.yaml



   oc -n dynatrace logs -f deployment/dynatrace-oneagent-operator
   ```

   For OpenShift versions **earlier than 3.11.188** you need to **delete the** `type: object` **line beneath the required spec validation in** `openshift.yaml` **before deploying the** `CustomResourceDefinition` ([OpenShift known bugï»¿](https://github.com/openshift/origin/pull/24540)).

   ```
   required:



   -  spec



   type: object  # delete this line, which is a validation rule
   ```
4. Create the secret that holds the API and PaaS tokens for authenticating to the Dynatrace Cluster.  
   The name of the secret will be important in a later step when you configure the custom resource (`.spec.tokens`). In the following code-snippet the name is `oneagent`. Be sure to replace `API_TOKEN` and `PAAS_TOKEN` with the values mentioned in prerequisites.

   ```
   oc -n dynatrace create secret generic oneagent --from-literal="apiToken=API_TOKEN" --from-literal="paasToken=PAAS_TOKEN"
   ```
5. Save the custom resource.  
   The rollout of Dynatrace OneAgent is governed by a custom resource of type `OneAgent`. Retrieve the `cr.yaml` file from the GitHub repository.

   ```
   curl -o cr.yaml https://raw.githubusercontent.com/Dynatrace/dynatrace-oneagent-operator/master/deploy/cr.yaml
   ```
6. Adapt the custom resource.

   If you want to revert an argument, you need to **set it to empty** instead of removing it from the custom resource.
   Example:

   ```
   args:



   - "--set-proxy="
   ```

### Parameters

| **Parameter** | **Description** | **Default value** |
| --- | --- | --- |
| `apiUrl` | Required For **Dynatrace SaaS**, where OneAgent can connect to the internet, replace the Dynatrace `ENVIRONMENTID` in `https://ENVIRONMENTID.live.dynatrace.com/api`. For **Environment ActiveGates** (SaaS or Managed), use the following to download the OneAgent, as well as to communicate OneAgent traffic through the ActiveGate: `https://YourActiveGateIP` or `FQDN:9999/e/<ENVIRONMENTID>/api`. |  |
| `useUnprivilegedMode` | Optional Set to `false` if you want to mark the pod as privileged. Defaults to using [Linux capabilities for the OneAgent pod](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged "Find out when Dynatrace OneAgent requires root privileges on Linux.") | `true` |
| `tokens` | Optional Name of the secret that holds the API and PaaS tokens from above. | Name of custom resource (`.metadata.name`) if unset |
| `useImmutableImage` | Optional Set to `true` if you want to pull a OneAgent Docker image from your Dynatrace environment. Use this parameter together with the `agentVersion` parameter to control the version of OneAgent. | `false` |
| `agentVersion` | Optional Set this value to the OneAgent version using semantic versioning (`major.minor.patch`). Example: `1.203.0` | latest version |
| `args` | Optional Parameters to be passed to the OneAgent installer. All the [command line parameters of the installer](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.") are supported, with the exception of `INSTALL_PATH`. |  |
| `env` | Optional Environment variables for OneAgent container. |  |
| `skipCertCheck` | Optional Disable certificate validation checks for installer download and API communication. Set to `true` if you want to skip any certification validation checks. | `false` |
| `nodeSelector` | Optional Keep empty default value. If you want to roll out OneAgent to specific nodes only, provide the `nodeSelectors` here. Refer to [Kubernetes docsï»¿](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#nodeselector) for details. |  |
| `tolerations` | Optional Keep default value to also roll out the OneAgent to master nodes if possible. If you want to apply additional tolerations to OneAgent pods for tainted nodes, provide them here. Refer to [Kubernetes docsï»¿](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/) for details. |  |
| `image` | Optional Define the OneAgent image to be taken. Defaults to the publicly available OneAgent image on [Docker Hubï»¿](https://hub.docker.com/r/dynatrace/oneagent/). In order to use the certified [OneAgent imageï»¿](https://access.redhat.com/containers/#/registry.connect.redhat.com/dynatrace/oneagent) from [Red Hat Container Catalogï»¿](https://access.redhat.com/containers/) you need to set `.spec.image` to `registry.connect.redhat.com/dynatrace/oneagent` in the custom resource and provide image pull secrets as shown in the next step. | `docker.io/dynatrace/oneagent:latest` if unset |
| `resources` | Optional Resource requests/limits for the OneAgent pods. These settings heavily depend on size of worker nodes and workloads. Please adjust to fit your needs. |  |
| `priorityClassName` | Optional Priority class for OneAgent pod. Refer to [Kubernetes docsï»¿](https://kubernetes.io/docs/concepts/configuration/pod-priority-preemption/). |  |
| `disableAgentUpdate` | Optional Disable the Operator's auto-update feature for OneAgent pods. | `false` |
| `enableIstio` | Optional Enable management of Istio service entries and virtual services for Dynatrace endpoints to allow for OneAgent monitoring egress traffic to your Dynatrace environment | `false` |
| `trustedCAs` | Optional Name of the ConfigMap containing the custom CA certificates. The ConfigMap must have a field called `certs` with the content of the PEM bundle. These custom certificates will be used by both the OneAgent Operator and the OneAgent. | If not set, the default embedded certificates on the images will be used. |

7. Create the custom resource.

   ```
   oc apply -f cr.yaml
   ```
8. Optional Configure proxy.

   * You can configure optional parameters like proxy settings in the `cr.yaml` file in order to

     + download the OneAgent installer
     + ensure the communication between the OneAgent and your Dynatrace environment
     + ensure the communication between the Dynatrace OneAgent Operator and the Dynatrace API.

   There are two ways to provide the proxy, depending on whether or not your proxy uses credentials.

   No credentials

   If you have a proxy that doesn't use credentials, enter your proxy URL directly in the `value` field for the proxy.

   **Example**

   ```
   apiVersion: dynatrace.com/v1alpha1



   kind: OneAgent



   metadata:



   name: oneagent



   namespace: dynatrace



   spec:



   apiUrl: https://environmentid.dynatrace.com/api



   tolerations:



   - effect: NoSchedule



   key: node-role.kubernetes.io/master



   operator: Exists



   args: []



   enableIstio: true



   proxy:



   value: http://mysuperproxy
   ```

   With credentials

   If your proxy uses credentials

   1. Create a secret with a field called `proxy` which holds your encrypted proxy URL with the credentials.  
      Example.

      ```
      oc -n dynatrace create secret generic myproxysecret --from-literal="proxy=http://<user>:<password>@<IP>:<PORT>"
      ```
   2. Provide the name of the secret in the `valueFrom` section.  
      Example.

      ```
      apiVersion: dynatrace.com/v1alpha1



      kind: OneAgent



      metadata:



      name: oneagent



      namespace: dynatrace



      spec:



      apiUrl: https://environmentid.dynatrace.com/api



      tolerations:



      - effect: NoSchedule



      key: node-role.kubernetes.io/master



      operator: Exists



      args: []



      enableIstio: true



      proxy:



      valueFrom: myproxysecret
      ```
9. Optional Configure network zones.

   You can configure network zones by setting the following argument:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

Prerequisites

* Generate an [API token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#create-api-token "Learn the concept of an access token and its scopes.") and a [PaaS token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") in your Dynatrace environment.

  Make sure you have the **Access problem and event feed, metrics, and topology** setting enabled for the API token.
* Pods must allow egress to your Dynatrace environment or to your Environment ActiveGate in order for metric routing to work properly.
* See [Support lifecycle](/docs/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") for supported OpenShift versions.
* [Install Helm version 3ï»¿](https://helm.sh/docs/intro/install/).
* We recommend installing a **recent version** of the Helm chart.

1. Add a new project called `dynatrace`.

   ```
   oc adm new-project --node-selector="" dynatrace
   ```
2. Add the Dynatrace OneAgent Helm repository.

   ```
   helm repo add dynatrace \



   https://raw.githubusercontent.com/Dynatrace/helm-charts/master/repos/stable
   ```
3. Create the custom resource definitions.

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagents.yaml



   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagentapms.yaml
   ```

   For OCP version 3.11, run the commands below.

   ```
   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagents-v1beta1.yaml



   oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/dynatrace.com_oneagentapms-v1beta1.yaml
   ```
4. Create a `values.yaml` file with the following content.

   ```
   platform: "openshift"



   operator:



   image: ""



   oneagent:



   name: "oneagent"



   apiUrl: "https://ENVIRONMENTID.live.dynatrace.com/api"



   image: ""



   args: []



   env: []



   nodeSelector: []



   labels: []



   skipCertCheck: false



   disableAgentUpdate: false



   enableIstio: false



   dnsPolicy: ""



   resources: []



   waitReadySeconds: null



   priorityClassName: ""



   serviceAccountName: ""



   proxy: ""



   trustedCAs: ""



   secret:



   apiToken: "DYNATRACE_API_TOKEN"



   paasToken: "PLATFORM_AS_A_SERVICE_TOKEN"
   ```
5. Optional Configure network zones.

   You can configure network zones by setting the following argument:

   ```
   args:



   - --set-network-zone=<your.network.zone>
   ```

   See [network zones](/docs/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.

   For OpenShift versions **earlier than 3.11.188** you need to **delete the** `type: object` **line beneath the required spec validation in** `openshift.yaml` **before deploying the** `CustomResourceDefinition` ([OpenShift known bugï»¿](https://github.com/openshift/origin/pull/24540)).

   ```
   required:



   -  spec



   type: object  # delete this line, which is a validation rule
   ```
6. To apply the YAML parameters, run the following command:

   ```
   helm install dynatrace-oneagent-operator \



   dynatrace/dynatrace-oneagent-operator -n\



   dynatrace --disable-openapi-validation --values values.yaml
   ```

After deployment, you need to restart your pods so OneAgent can inject into them.

## Cluster-wide permissions

The following table shows the permissions needed for OneAgent Operator.

| **Resources accessed** | **APIs used** | **Resource names** |
| --- | --- | --- |
| `Nodes` | Get/List/Watch | - |
| `Namespaces` | Get/List/Watch | - |
| `Secrets` | Create | - |
| `Secrets` | Get/Update/Delete | `dynatrace-oneagent-config`, `dynatrace-oneagent-pull-secret` |

## Limitations

See [Docker limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container.") for details.

## Troubleshoot

Find out how to [troubleshoot issues](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting#deploy "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components.") that you may encounter when deploying OneAgent on OpenShift.

## Deploy an ActiveGate and connect your Kubernetes API to Dynatrace

Now that you have OneAgent running on your OpenShift nodes, you're able to monitor those nodes, and the applications running in OpenShift. The next step is to deploy an ActiveGate and connect your Kubernetes API to Dynatrace in order to get native Kubernetes metrics, like request limits, and differences in pods requested vs. running pods.  
For further instructions see [Deploy ActiveGate in OpenShift as a StatefulSet](/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.").

## Update OneAgent Operator with oc

OneAgent Operator for OpenShift version 3.9+ automatically takes care of the lifecycle of the deployed OneAgents, so you don't need to update OneAgent pods yourself.

Review the [release notesï»¿](https://github.com/Dynatrace/dynatrace-oneagent-operator/releases) of the Operator for any breaking changes of the custom resource.

To update OneAgent Operator, run the following command:

```
oc apply -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/openshift.yaml
```

## Update OneAgent Operator with Helm

1. Update your Helm repositories.

   ```
   helm repo update
   ```

   Alternative method: add it again. This will overwrite the older version.
2. Update OneAgent to the latest version.

   Don't omit the `--reuse-values` flag in the command in order to keep your configuration.

   ```
   helm upgrade dynatrace-oneagent-operator dynatrace/\



   dynatrace-oneagent-operator -n dynatrace --reuse-values
   ```

## Uninstall OneAgent Operator

Uninstall with kubectl

Uninstall with Helm

To uninstall OneAgent Operator from OpenShift version 3.9+

1. Remove OneAgent custom resources and clean up all remaining OneAgent Operatorâspecific objects.

   ```
   oc delete -n dynatrace oneagent --all



   oc delete -f https://github.com/Dynatrace/dynatrace-oneagent-operator/releases/latest/download/openshift.yaml
   ```
2. Optional After you delete OneAgent Operator, the OneAgent binary remains on the node in an inactive state. To uninstall it completely, run the `uninstall.sh` script and delete logs and configuration files.  
   See [Linux related information](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").

Remove OneAgent custom resources and clean up all remaining OneAgent Operatorâspecific objects:

```
helm uninstall dynatrace-oneagent-operator -n dynatrace
```

## Related topics

* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")
* [Store Dynatrace images in private registries](/docs/ingest-from/setup-on-k8s/guides/container-registries/prepare-private-registry "Store Dynatrace images in private registries")
* [Migrate Dynatrace Operator to a new environment](/docs/ingest-from/setup-on-k8s/guides/migration/migrate-dto-to-tenant "Migrate monitoring to a new Dynatrace environment on Kubernetes clusters.")


---


## Source: oneagent-privileges.md


---
title: OneAgent privileges for container monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/oneagent-privileges
scraped: 2026-02-17T21:30:50.247397
---

# OneAgent privileges for container monitoring

# OneAgent privileges for container monitoring

* Latest Dynatrace
* 2-min read
* Published Mar 08, 2023

Dynatrace supports Full-Stack Monitoring for container platforms, from the application down to the infrastructure layer. This requires elevated privileges to get container-level metrics and perform deep-code host monitoring, including OneAgent injection into processes.

However, if you don't want to grant elevated privileges to OneAgent, or you don't have access to the infrastructure layer, you can go with application-only monitoring.

For Kubernetes, Dynatrace Operatorâbased application-only monitoring still provides you with a good scope of data, such as node-level insights (basic metrics and alerting) based on data retrieved by the ActiveGate from Kubernetes API, or Prometheus metrics.

## Full-stack injection

The OneAgent container and underlying host share selected Linux namespaces for OneAgent to be able to access data required for full-stack monitoring:

* Shared network namespace enables processes running inside the container to directly access host network interfaces.
* Shared PID namespace enables processes running inside the container to see and work with all the processes from the host process table.
* Mounted host's root filesystem is accessed by all OneAgent modules and allows for log files access, disk metrics, and other full-stack monitoring capabilities.

During monitoring, the scope of required permissions for each process is limited using specific [Linux System Capabilities](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#linux-system-capabilities "Find out when Dynatrace OneAgent requires root privileges on Linux.").

You can achieve full-stack injection using the following deployment modes:

* Dynatrace Operator on Kubernetes/OpenShift

  + [Cloud-native full-stack mode](/docs/ingest-from/setup-on-k8s/how-it-works#cloud-native "In-depth description on how the deployment on Kubernetes works.")
  + [Classic full-stack mode](/docs/ingest-from/setup-on-k8s/how-it-works#classic "In-depth description on how the deployment on Kubernetes works.")
* Docker outside a container platform

  + [OneAgent as a Docker container](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container "Install and update Dynatrace OneAgent as a Docker container.")

### OneAgent on Docker host

Alternatively, you can also deploy OneAgent on the Docker host on Linux. In this scenario, OneAgent does not run in a container but directly on the host, so there is no Linux namespace isolation. For more information, see [OneAgent on Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux "Learn how to install OneAgent on Linux, how to customize installation, and more.").

## Application-only injection

OneAgent deployed in application-only mode doesn't run as a privileged container.

For more information, see:

* [Get started with Kubernetes platform monitoring + Application observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")
* [Deploy OneAgent on Cloud Foundry for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")
* [Set up OneAgent on containers for application-only monitoring](/docs/ingest-from/setup-on-container-platforms/docker/set-up-oneagent-on-containers-for-application-only-monitoring "Install, update, and uninstall OneAgent on containers for application-only monitoring.")


---
