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