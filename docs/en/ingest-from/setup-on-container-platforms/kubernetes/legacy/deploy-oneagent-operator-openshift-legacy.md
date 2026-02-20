---
title: Deploy OneAgent Operator on OpenShift (deprecated)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-container-platforms/kubernetes/legacy/deploy-oneagent-operator-openshift-legacy
scraped: 2026-02-20T21:13:34.834622
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

## Troubleshooting

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