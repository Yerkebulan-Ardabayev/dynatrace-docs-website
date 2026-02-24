---
title: Containerized, auto-scalable private Synthetic locations on Kubernetes
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations
scraped: 2026-02-24T21:23:34.979106
---

# Containerized, auto-scalable private Synthetic locations on Kubernetes

# Containerized, auto-scalable private Synthetic locations on Kubernetes

* How-to guide
* 26-min read
* Updated on Feb 11, 2026

Dynatrace version 1.264+

**Containerized, auto-scalable private Synthetic locations on Kubernetes and its commercial distribution OpenShift** are an alternative to deploying Synthetic-enabled ActiveGates on separate hosts or virtual machines and then assigning them to private locations for the execution of synthetic monitors.

Unlike individual Synthetic-enabled ActiveGates that are deployed and assigned to private locations (and then tracked via utilization metrics) **containerized locations are deployed as a whole**, with a minimum and maximum number of ActiveGates as the necessary input parameters.

Kubernetes and OpenShift aren't just additional supported ActiveGate platforms along with Windows and Linux; with this offering, containerized private Synthetic locations:

* Are auto-scalable (based on utilization metrics and the maximum/minimum number of ActiveGates specified).

* Are easy to manage and maintain.
* Support the synthetic monitoring of cloud-native solutions that require container-based application development.
* Can be deployed faster while minimizing downtime.
* Are automatically tracked for resource utilization as a part of auto-scaling operations.

You can execute scheduled as well as [on-demand](/docs/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Execute synthetic monitors on demand from public or private locations") executions of all [types of synthetic monitors](/docs/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Learn about Dynatrace synthetic monitor types.") on containerized locations.

You can manage Kubernetes/OpenShift locations via the Dynatrace web UI and the existing [Synthetic - Locations, nodes, and configuration API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API."). Additional Early Adopter endpoints in this API facilitate the deployment of Kubernetes locations; the new endpoints help you generate the commands that need to be executed on the Kubernetes cluster.

## Architecture

Containerized private Synthetic locations are deployed as a whole.

* Each location has multiple Synthetic-enabled **ActiveGates** configured as **pods**. You specify a minimum and maximum number of ActiveGates when [setting up a location](#initial-setup).
* The **StatefulSet** is considered as the **location**.

  You can have one or more locations per namespace. See [Requirements](#requirements) and [Recommendations and caveats](#recommend) below.

  You can have one or more auto-scalable locations per Kubernetes cluster.

Locations are scaled automatically by adjusting the number of ActiveGates per location by the following additional parts of the containerized location architecture.

* The **Synthetic metric adapter** requests and receives [utilization metrics](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#location-details "Analyze and manage capacity usage at your private Synthetic locations.") for the containerized ActiveGates from the Dynatrace Cluster.

  There is one Synthetic metric adapter per Kubernetes cluster.

  The metric adapter is configured to communicate with a single Dynatrace environment.

  Installing a Synthetic metric adapter requires [super-user roles in Kubernetesï»¿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles)âsee [Install a containerized location](#install) below.
* The **horizontal pod auto-scaler** scales a location by adjusting the number of ActiveGates based on the utilization data it receives from the Synthetic metric adapter.

  There is one horizontal pod auto-scaler per location.

![Containerized locations for synthetic monitoring](https://dt-cdn.net/images/k8s-synthetic-locations-1769-41775c85f2.jpg)

## Requirements

Containerized private Synthetic locations are supported with Dynatrace version 1.264+ on **Kubernetes 1.22â1.25** with persistent volume and `kubectl` support.

* Additional support for **Kubernetes 1.26+** is available in the [installation workflow](#install).
* All kinds of Kubernetes implementations are supported, whether cloud or local (for example, Amazon EKS or Minikube).
* OpenShift versions compatible with the supported Kubernetes versions are supported.

Internet connectivity is required to access the public repositories where Docker images for the Synthetic-enabled ActiveGate and Synthetic metric adapter are available. These image locations are referenced in the respective template filesâsee [Install a containerized location](#install) and [Update a containerized location](#update) below.

### Sizing guide

The **ActiveGate hardware requirements** below are listed by size.

* CPU and RAM requests refer to the resources reserved by pods upon creation.
* CPU and RAM limits refer to the maximum resource consumption per pod.
* If the location is monitored by [OneAgent](/docs/ingest-from/dynatrace-oneagent/oa-requirements "OneAgent code module requirements") or another deep monitoring solution, memory (RAM) requirements will increase.
* Browserless pod in FIPS mode has the same requirements as ordinary browserless pod.

XS node

S node

M node

|  | Browser-supporting pod | Browserless pod | Browser-supporting pod in FIPS mode | Browser-supporting pod in FIPS mode with corporate proxy |  | ActiveGate | Synthetic Engine | Browser worker | FIPS proxy | FIPS peer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Containers | 4 | 2 | 5 | 6 |  | 1 | 1 | 2 | 1 | 1 |
| CPU requests | 1.4 vCPU | 0.4 vCPU | 1.9 vCPU | 2.05 vCPU |  | 0.3 vCPU | 0.25 vCPU | 2 Ã 0.5 vCPU | 0.5 vCPU | 0.15 vCPU |
| CPU limits | 3.8 vCPU | 0.8 vCPU | 5.3 vCPU | 5.6 vCPU |  | 0.3 vCPU | 0.5 vCPU | 2 Ã 1.5 vCPU | 1.5 vCPU | 0.3 vCPU |
| RAM requests | 3.25 GiB | 1.25 GiB | 3.5 GiB | 3.75 GiB |  | 0.25 GiB | 1 GiB | 2 Ã 1 GiB | 0.25 GiB | 0.25 GiB |
| RAM limits | 7 GiB | 3 GiB | 7.5 GiB | 8 GiB |  | 1 GiB | 2 GiB | 2 Ã 2 GiB | 0.5 GiB | 0.5 GiB |
| Ephemeral storage | 1.5 GiB | 1.3 GiB | 1.6 GiB | 1.7 GiB |  | 1.2 GiB | 0.1 GiB | 2 Ã 0.1 GiB | 0.1 GiB | 0.1 GiB |
| Persistent storage | 3 GiB | 3 GiB | 3 GiB | 3 GiB |  |  |  |  |  |  |
| RAM disk | 1 GiB | - | 1 GiB | 1 GiB |  |  |  |  |  |  |

|  | Browser-supporting pod | Browserless pod | Browser-supporting pod in FIPS mode | Browser-supporting pod in FIPS mode with corporate proxy |  | ActiveGate | Synthetic Engine | Browser worker | FIPS proxy | FIPS peer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Containers | 6 | 2 | 7 | 8 |  | 1 | 1 | 4 | 1 | 1 |
| CPU requests | 2.65 vCPU | 0.65 vCPU | 3.15 vCPU | 3.3 vCPU |  | 0.3 vCPU | 0.5 vCPU | 4 Ã 0.5 vCPU | 0.5 vCPU | 0.15 vCPU |
| CPU limits | 7.3 vCPU | 1.3 vCPU | 8.8 vCPU | 9.1 vCPU |  | 0.3 vCPU | 1 vCPU | 4 Ã 1.5 vCPU | 1.5 vCPU | 0.3 vCPU |
| RAM requests | 5.75 GiB | 1.75 GiB | 6 GiB | 6.25 GiB |  | 0.25 GiB | 1.5 GiB | 4 Ã 1 GiB | 0.25 GiB | 0.25 GiB |
| RAM limits | 12 GiB | 4 GiB | 12.5 GiB | 13 GiB |  | 1 GiB | 3 GiB | 4 Ã 2 GiB | 0.5 GiB | 0.5 GiB |
| Ephemeral storage | 1.7 GiB | 1.3 GiB | 1.8 GiB | 1.9 GiB |  | 1.2 GiB | 0.1 GiB | 4 Ã 0.1 GiB | 0.1 GiB | 0.1 GiB |
| Persistent storage | 6 GiB | 6 GiB | 6 GiB | 6 GiB |  |  |  |  |  |  |
| RAM disk | 2 GiB | - | 2 GiB | 2 GiB |  |  |  |  |  |  |

|  | Browser-supporting pod | Browserless pod | Browser-supporting pod in FIPS mode | Browser-supporting pod in FIPS mode with corporate proxy |  | ActiveGate | Synthetic Engine | Browser worker | FIPS proxy | FIPS peer |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Containers | 14 | 2 | 15 | 16 |  | 1 | 1 | 12 | 1 | 1 |
| CPU requests | 7.15 vCPU | 1.15 vCPU | 7.65 vCPU | 7.8 vCPU |  | 0.3 vCPU | 1 vCPU | 12 Ã 0.5 vCPU | 0.5 vCPU | 0.15 vCPU |
| CPU limits | 20.3 vCPU | 2.3 vCPU | 21.8 vCPU | 22.1 vCPU |  | 0.3 vCPU | 2 vCPU | 12 Ã 1.5 vCPU | 1.5 vCPU | 0.3 vCPU |
| RAM requests | 14.25 GiB | 2.25 GiB | 14.5 GiB | 14.75 GiB |  | 0.25 GiB | 2 GiB | 12 Ã 1 GiB | 0.25 GiB | 0.25 GiB |
| RAM limits | 29 GiB | 5 GiB | 29.5 GiB | 30 GiB |  | 1 GiB | 4 GiB | 12 Ã 2 GiB | 0.5 GiB | 0.5 GiB |
| Ephemeral storage | 2.5 GiB | 1.3 GiB | 2.6 GiB | 2.7 GiB |  | 1.2 GiB | 0.1 GiB | 12 Ã 0.1 GiB | 0.1 GiB | 0.1 GiB |
| Persistent storage | 12 GiB | 12 GiB | 12 GiB | 12 GiB |  |  |  |  |  |  |
| RAM disk | 4 GiB | - | 4 GiB | 4 GiB |  |  |  |  |  |  |

### Best practices and caveats

**ActiveGates**

* We recommend the **S** ActiveGate size and a minimum of two ActiveGates per location.
* When considering node size, keep in mind the possible limitations specific to the Kubernetes service you will be relying on.
* All ActiveGates within a location are always the same size.
* Once specified, ActiveGate size for a location can't be changed because persistent storage can't be resized.
* Kubernetes locations follow the same rules as other locations in that an ActiveGate can't be added to multiple locations simultaneously.
* You cannot combine containerized and non-containerized ActiveGates in the same location.
* The image for Synthetic-enabled ActiveGate is in a public registry; this image location is referenced by the template file.

**Locations**

* We recommend installing each location in its own namespace.
* If deploying more than one location per namespace, use different names for the respective ActiveGate resourcesâsee [Install a containerized location](#install) below.
* Locations that share a single Kubernetes namespace must be connected to the same Dynatrace environment as the Synthetic metric adapter in order to be auto-scalable. For example, assume that Location A and the metric adapter are configured for Environment X. However, Location A shares a namespace with Location B, which is configured for Environment Y. In such a case, Location A is auto-scalable; Location B is not auto-scalable.
* If you want to install a location in the same namespace as other Dynatrace resources such as [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits "Set resource limits for Dynatrace Operator components."), be aware of the more demanding [hardware and system requirements](#requirements) for containerized Synthetic-enabled ActiveGates.

**Synthetic metric adapter**

* The best practice is to deploy the Synthetic metric adapter in its own namespace per Kubernetes cluster. The Synthetic metric adapter can share a namespace with a location. However, deploying the metric adapter in its own namespace ensures that it isn't deleted when a location is taken down.
* The metric adapter can only communicate with a single Dynatrace environment, so location auto-scaling works just for that environment.
* The image for the Synthetic metric adapter is in a public registry; this image location is referenced by the template file.

### Auto-scaling specifics

For auto-scaling purposes, the Synthetic metric adapter needs access to and extends the Kubernetes API by specifying a new API serviceâ`v1beta1.external.metrics.k8s.io`.

This API service is defined in the Synthetic metric adapter templateâsee <#install> below.

API service definition in the metric adapter template

```
apiVersion: apiregistration.k8s.io/v1



kind: APIService



metadata:



name: v1beta1.external.metrics.k8s.io



spec:



service:



name: dynatrace-metrics-apiserver



namespace: {{adapterNamespace}}



group: external.metrics.k8s.io



version: v1beta1



insecureSkipTLSVerify: true



groupPriorityMinimum: 100



versionPriority: 100
```

The Synthetic metric adapter also modifies an existing resource in its templateâthe `horizontal-pod-autoscaler` ServiceAccount in `kube-system` namespace.

Existing resource modification in the metric adapter template

```
apiVersion: rbac.authorization.k8s.io/v1



kind: ClusterRoleBinding



metadata:



name: hpa-controller-dynatrace-metrics



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: ClusterRole



name: dynatrace-metrics-server-resources



subjects:



- kind: ServiceAccount



name: horizontal-pod-autoscaler



namespace: kube-system
```

#### Limitations

Note that only one external metric server is allowed in the Kubernetes cluster. Because of this, other components that serve as a metric server (such as the KEDA add-on or the Prometheus adapter) cannot be used along with the Synthetic metric adapter.

## Install a containerized location

You can install a containerized location only in the previous Dynatrace. In the latest Dynatrace, the containerized locations are available only in view mode.

Set up and manage a containerized location in the Dynatrace web UI at **Settings** > **Web and Mobile monitoring** > **Private Synthetic locations**.

### 1. Initial setup for a Kubernetes/OpenShift location

1. Select **Add Kubernetes location** or **Add OpenShift location** on the **Private Synthetic locations** page.
2. Provide a **Location name** of your choice.
3. Select a **Geographic location**, for example, `San Francisco, California, United States`. (Note that you cannot **Save changes** until you've specified a name and location.)
4. In the **ActiveGates** section:

   1. Specify a **Minimum** and **Maximum number of ActiveGates** for your location. These settings are the auto-scaling parameters that the [horizontal pod auto-scaler](#architecture) uses.
   2. Select an ActiveGate **Node size** (`XS`, `S`, or `M`). See also [Requirements](#requirements) and [Best practices and caveats](#recommend).
   3. The **Deployment platform** is preselected based on your selection of Kubernetes or OpenShift.
5. Kubernetes only If your Kubernetes implementation is based on a later release than 1.21â1.25, turn on **Use Kubernetes version 1.26+**. See also [Requirements](#requirements) and [Best practices and caveats](#recommend).

   If you change this setting after downloading the location template, you need to repeat the deployment procedure.
6. Optional You can turn off support for browser monitors. If you do so, the ActiveGate node will be treated as [browserless](#browserless).
7. Optional Turn on [problem generation if all ActiveGates go offline](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations#outage-handling "Analyze and manage capacity usage at your private Synthetic locations.").
8. **Save changes** before proceeding with deploying the [location](#deploy-location) and [metric adapter](#deploy-adapter).

Your named location is displayed on the **Private Synthetic locations** page with the Kubernetes or OpenShift logo. Note that no ActiveGates are assigned to the location at this point.

![Empty location](https://dt-cdn.net/images/containerized-empty-location-1351-ef0b3700e2.png)

### 2. Deploy the location

Select your location in **Private Synthetic locations** to download the location template and generate the commands that need to be executed on the Kubernetes cluster.

1. In the **Deployment** section, create a **PaaS token** (**Create token**) or paste an existing token. The PaaS token is required to generate ActiveGate connection tokens for communication with your Dynatrace environment.

   Existing tokens are listed on the **Access tokens** page. Note that a PaaS token is only displayed once upon creation, after which it's stored encrypted and can't be revealed. We recommend storing your PaaS token in a password manager so that you can reuse it for creating additional private locations within your Kubernetes cluster.
2. Provide an **ActiveGate name** or use the default. This name is used as the prefix for ActiveGates deployed as part of the location. The first ActiveGate is named `<prefix>-0`, the second ActiveGate `<prefix>-1`, and so on. This name is also used as the StatefulSet name.
3. Provide a **Location namespace** name or use the default. (Leave the **Metric adapter namespace** as is. This field is only necessary for generating the [template for the Synthetic metric adapter](#deploy-adapter).)

   The **Download synthetic.yaml** button is enabled after you provide a PaaS token, ActiveGate name, and location namespace name.

   The values of fields in the **Deployment** section are not persistent. If you navigate away from the page, you need to re-enter the values.

   ![Required fields for the location template](https://dt-cdn.net/images/k8s-location-tokens-namespace-1242-d9a86d7dce.png)
4. Select **Download synthetic.yaml**. This is the location template file. You can rename the file to match your location for easy identification.
5. Copy the downloaded location template over to your Kubernetes cluster.
6. Copy and execute the generated commands on your Kubernetes cluster. Your PaaS token is automatically appended to the commands displayed.

   Execute the commands from the same location as the template file.

   If you've renamed the template file, use the new filename in the commands.

   ![Commands to create the location namespace](https://dt-cdn.net/images/k8s-location-commands-1106-4b8fac8db7.png)
7. Optional Run the following command to list all pods in a given namespace (`dynatrace` in the sample below) and verify their deployment.

   ```
   kubectl get pod -n dynatrace
   ```

   You can also view pods on the **Deployment Status** > **ActiveGates** page by filtering with the key-value pairs `Running in container: True` and `With modules: Synthetic`.

   ![ActiveGate deployment status filters](https://dt-cdn.net/images/k8s-location-deployment-status-1109-28df0f6a0c.png)

### 3. Deploy the Synthetic metric adapter

This procedure generates a separate template for the Synthetic metric adapter. You then execute generated commands on your Kubernetes cluster to deploy the metric adapter.

* You need to deploy the Synthetic metric adapter just once per Kubernetes cluster.
* Installing a Synthetic metric adapter requires a [Kubernetes super-user roleï»¿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#user-facing-roles) to create ClusterRoles and ClusterRoleBindings.

1. In the **Deployment** section, create a **Metrics token** (**Create token**) or paste an existing token. The metric token is an [access token](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.") for fetching utilization data from Dynatrace. Existing tokens are listed on the **Access tokens** page.
2. Provide a **Metric adapter namespace** name or use the default. (Leave the **Location namespace** and **ActiveGate name** as is. These fields are only necessary for generating the [template for the location](#deploy-location).)

   The **Download synthetic-adapter.yaml** button is enabled after you provide a metric token and metric adapter namespace name.

   The values of fields in the **Deployment** section are not persistent. If you navigate away from the page, you need to re-enter the values.

   ![Required fields for the adapter template](https://dt-cdn.net/images/k8s-location-tokens-adapter-1213-fc6df4117a.png)
3. Select **Download synthetic-adapter.yaml**. This is the template file for the Synthetic metric adapter.
4. Copy the downloaded metric adapter template over to your Kubernetes cluster.
5. Copy and execute the generated commands on your Kubernetes cluster. Your metric token is automatically appended to the commands displayed.

   Execute the commands from the same location as the template file.

   If you've renamed the template file, use the new filename in the commands.

   ![Commands to create the metric adapter namespace](https://dt-cdn.net/images/k8s-location-adapter-commands-1167-f2c11204cc.png)

## Install FIPS-enabled containerized location

1. Set location to FIPS mode

   Currently this is only possible using the [REST API](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API."), by setting the `fipsMode` property in the request JSON.

   * To create a new location, use a [POST location](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location "Create a private synthetic location via the Synthetic v2 API.") call
   * To update an existing location, use a [PUT location](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/put-a-location "Update a private synthetic location via the Synthetic v2 API.") call
2. Perform additional configuration

   Browser-supporting

   Browser-supporting with corporate proxy

   Browserless

   Provide a certificate for re-signing HTTPS requests (explained in [FIPS mode](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")):

   ```
   kubectl -n $NAMESPACE create secret tls synthetic-fips-proxy-cert --cert=squid.crt --key=squid.key
   ```

   1. Provide a certificate for re-signing HTTPS requests (explained in [FIPS mode](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-proxy "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")):

      ```
      kubectl -n $NAMESPACE create secret tls synthetic-fips-proxy-cert --cert=squid.crt --key=squid.key
      ```
   2. Provide configuration of corporate proxy to Squid (explained in [FIPS mode with corporate proxy](/docs/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic#fips-corporate-proxy "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")):

      ```
      kubectl -n $NAMESPACE create secret generic synthetic-fips-proxy-peer --from-literal='peer.conf=cache_peer proxy.example.com parent 443 0 default no-digest proxy-only login=proxyuser:proxypass tls tls-min-version=1.2 tls-options=NO_SSLv3'
      ```
   3. Provide configuration of corporate proxy to ActiveGate:

      * see [Proxy configuration](#proxy)

   No additional configuration is needed.
3. Continue to download and deploy the YAML template as described in the [Installation](#deploy-location) section.

## Update a containerized location or its ActiveGates

You can update a containerized location or its ActiveGates only in the previous Dynatrace. In the latest Dynatrace, the containerized locations are available only in view mode.

Any updates to a location require that you download the location template file again and apply the changes via kubectl.

**To update ActiveGate versions**

1. Download the location template file.

   1. Select your location in **Private Synthetic locations**.
   2. In the **Deployment** section, re-enter the **PaaS token**, **ActiveGate name**, and **Location namespace** name that you provided during [location deployment](#deploy-location). The **Download synthetic.yaml** button is then enabled.
   3. Select **Download synthetic.yml** to download a new location template file.
   4. Rename the file to match your location for easy identification.
   5. Copy the template file over to your Kubernetes cluster.
2. Execute the following command to apply the changes on your Kubernetes cluster. Be sure to use your location template filename in place of `synthetic.yaml`. Execute this command from the same location as the template file.

   ```
   kubectl apply -f ./synthetic.yaml
   ```

Any update redeploys ActiveGates in the reverse order of their deployment. For example, if your location contains the ActiveGates `activegate-name-0` and `activegate-name-1`, `activegate-name-1` is stopped and redeployed first.

The redeployed ActiveGate pod uses the same persistent volume deployed for log continuity.

## Delete a location or metric adapter on Kubernetes

The snippets for deleting a location or a metric adapter on Kubernetes can be generated only in the previous Dynatrace.

The commands generated when [deploying a location](#deploy-location) and [the Synthetic metric adapter](#deploy-adapter) also include code snippets for deleting them on Kubernetes. You may copy and store these commands for future reference.

At any point, you can regenerate the commands for the respective namespaces.

* If you've renamed a template file, use the new filename in the commands.
* The cleanup commands shown below don't delete the respective namespaces.

**Location**

1. Select your location in **Private Synthetic locations**.
2. Re-enter the **Paas token**, **ActiveGate name**, and **Location namespace** name.
3. **Copy** and use the location **Cleanup** commands.

   ![Delete location resources](https://dt-cdn.net/images/k8s-location-delete-1111-8927775af1.png)

Note that this procedure only deletes Kubernetes resources; it doesn't delete the [location you initially set up in Dynatrace](#initial-setup).

**Synthetic metric adapter**

1. Select your location in **Private Synthetic locations**.
2. Re-enter the **Metrics token** and **Metric adapter namespace** name.
3. **Copy** and use the metric adapter **Cleanup** command.

   ![Delete the metric adapter](https://dt-cdn.net/images/k8s-location-adapter-delete-1098-fe02e0d2db.png)

If the [Synthetic metric adapter](#deploy-adapter) is deleted or stops working, horizontal pod auto-scalers can no longer receive utilization data from Dynatrace, and your containerized locations become [non-scalable](#non-scalable).

## Multi-AZ PVC access on cloud clusters

Using a multi-availability zone (multi-AZ) cluster with deployments utilizing PVC can result in pods being stuck in a pending state upon recreation. This happens because the storage volumes like EBS are not replicated between zones.

PVC is only shared between nodes located in the same availability zone. When you use a multi-AZ cluster and a node tries to access PVC from a different availability zone, it will become stuck in pending state and display an error message.

Currently, there are two possible solutions for multi-AZ Kubernetes deployments:

* Use node affinity to limit pods to a specific zone
* Use shared storage systems like EFS

### Use node affinity to limit pods to a specific zone

You can configure node affinities to use only specific zones for a deployment.

To set node affinity

1. Use the following command to find the zone each node is deployed on:

   ```
   kubectl get nodes --show-labels
   ```
2. Look for a label `failure-domain.beta.kubernetes.io/zone`, for example, `failure-domain.beta.kubernetes.io/zone=us-east-1a`.
3. Use the kubectl label command to set a custom label for a node:

   ```
   kubectl label nodes node name label=value
   ```

   Example

   ```
   kubectl label nodes ip-10-179-202-73.ec2.internal zone=us-east-1a
   ```
4. Add the custom node label to the `nodeSelector` section of the Synthetic deployment template. For example:

   ```
   spec:



   nodeSelector:



   zone: us-east-1a
   ```
5. Save your changes.
6. Apply the template.

Nodes with the same zone label will be deployed in the same availability zone and you'll be able to share PVC between them without causing an error.

### Use shared storage systems

Each cloud service provides its own shared storage systems options. To explain how to use shared storage systems, we will use AWS EFS as the example. For information about storage systems used by other cloud storage providers, see:

* Google Cloud: [About Filestore support for Google Kubernetes Engineï»¿](https://cloud.google.com/kubernetes-engine/docs/concepts/filestore-for-gke)
* Azure Storage: [What is Azure Files?ï»¿](https://learn.microsoft.com/en-us/azure/storage/files/storage-files-introduction)

  The standard SMB/CIFS driver is not supported for Azure Files. For details, see [Pod crashes when modifying file permissions when backed by Azure Files storageï»¿](https://access.redhat.com/solutions/7078656).

We assume that you already have EFS that you can use. If you don't, see [Getting started with Amazon EFSï»¿](https://dt-url.net/vq02epe) to learn how to set up EFS.

Be aware that EFS may be more expensive than EBS. Check pricing.

To use storage class with EFS

1. Complete the Synthetic deployment template similar to the example below:

   ```
   kind: StorageClass



   apiVersion: storage.k8s.io/v1



   metadata:



   name: efs-test



   provisioner: efs.csi.aws.com



   parameters:



   fileSystemId: fs-0c155dcd8425aa39d



   provisioningMode: efs-ap



   directoryPerms: "700"



   basePath: "/"
   ```
2. Modify the **volumeClaimTemplates** section of the template similar to the example below:

   ```
   volumeClaimTemplates:



   - metadata:



   name: persistent-storage



   spec:



   storageClassName: efs-test



   accessModes:



   - ReadWriteMany



   resources:



   requests:



   storage: 3Gi
   ```
3. Save your changes.
4. Apply the template.

Now, if the pod is redeployed on a node in a different zone, the PVC should be automatically bound to the new deployment zone.

## NAM monitors on containerized locations

Network availability monitors are supported on containerized Synthetic-enabled ActiveGate deployments, but additional permissions are required for ICMP tests.

To enable ICMP request type for NAM execution

1. In Dynatrace Hub ![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub"), search for **Settings**.
2. In **Settings**, search for **Private Synthetic Locations** and select it.
3. Select **Add Kubernetes location**.
4. Configure your location and make sure to turn on **Enable ICMP request type for Network Availability Monitors execution**.

* ICMP monitors use the `ping` executable, which requires the `CAP_NET_RAW` capability set for the container executing the requests (`synthetic-vuc`).
* The `allowPrivilegeEscalation` property of `securityContext` for this container has to be set to `true`, because the process that launches the `ping` executable doesn't have the required privileges set by default.

The entire `securityContext` for the `synthetic-vuc` container with enabled network availability monitors should look as follows.

```
securityContext:



readOnlyRootFilesystem: true



privileged: false



allowPrivilegeEscalation: true



runAsNonRoot: true



capabilities:



drop: ["all"]



add: ["NET_RAW"]
```

### OpenShift

OpenShift uses Security Context Constraint for limiting capabilities used by the pods.
By default, deployed pods will use the `restricted-v2` SCC, which does not allow any additional capabilities.
The recommended solution is to prepare a custom Security Context Constraint.

1. Create a dedicated Service Account Optional

   * If the custom SCC is used just by the synthetic deployment, it's recommended to create a dedicated Service Account.

     ```
     oc -n $NAMESPACE create sa sa-dt-synthetic



     oc -n $NAMESPACE adm policy add-role-to-user edit system:serviceaccount:$NAMESPACE:sa-dt-synthetic
     ```
2. Create a custom Security Context Constraint

   * scc-dt-synthetic.yaml

     ```
     apiVersion: security.openshift.io/v1



     kind: SecurityContextConstraints



     metadata:



     name: scc-dt-synthetic



     allowPrivilegedContainer: false



     allowHostDirVolumePlugin: false



     allowHostIPC: false



     allowHostNetwork: false



     allowHostPID: false



     allowHostPorts: false



     runAsUser:



     type: MustRunAsRange



     seccompProfiles:



     - runtime/default



     seLinuxContext:



     type: MustRunAs



     fsGroup:



     type: MustRunAs



     supplementalGroups:



     type: MustRunAs



     volumes:



     - configMap



     - downwardAPI



     - emptyDir



     - persistentVolumeClaim



     - projected



     - secret



     users: []



     groups: []



     priority: null



     readOnlyRootFilesystem: true



     requiredDropCapabilities:



     - ALL



     defaultAddCapabilities: null



     allowedCapabilities:



     - NET_RAW



     allowPrivilegeEscalation: true
     ```
   * `priority` can be set to any number between 1 and 9. If there are two or more SCCs that fulfill the requirements, the one with higher priority is selected.

     ```
     oc create -f scc-dt-synthetic.yaml
     ```
3. Add the new SCC to the Service Account used for synthetic deployment

   ```
   oc -n $NAMESPACE adm policy add-scc-to-user scc-dt-synthetic system:serviceaccount:$NAMESPACE:default
   ```

   * If the `sa-dt-synthetic` SA was created, substitute it in place of `default`.

     ```
     oc -n $NAMESPACE adm policy add-scc-to-user scc-dt-synthetic system:serviceaccount:$NAMESPACE:sa-dt-synthetic
     ```

### Azure RedHat OpenShift (ARO)

If the OpenShift cluster is deployed as an Azure Red Hat OpenShift (ARO) resource, by default, the Network Security Group won't allow ICMP traffic outside the cluster.

The AROs Network Security Group is not modifiable, but a custom NSG can be created and imported during the ARO cluster creation.
To learn more about it, see [Bring your own Network Security Group (NSG) to an Azure Red Hat OpenShift (ARO) clusterï»¿](https://learn.microsoft.com/en-us/azure/openshift/howto-bring-nsg).

Running the cluster with default settings will only allow for using ICMP NAM monitors for resources inside the OpenShift cluster. Any requests going outside the cluster will fail.

## Proxy configuration

Add the following code at the top of your [location template file](#deploy-location) to insert a ConfigMap resource containing your proxy server information.

In the code sample below:

* The proxy server is used for connections to the Dynatrace Cluster and tested resources.
* The namespace (`namespace: dynatrace`) must be the location namespace.

```
kind: ConfigMap



apiVersion: v1



data:



custom.properties: |-



[http.client]



proxy-server = 10.102.43.210



proxy-port = 3128



proxy-user = proxyuser



proxy-password = proxypass



metadata:



name: ag-custom-configmap



namespace: dynatrace



---
```

Add the following code at `spec.template.spec.volumes:`.

```
- name: ag-custom-volume



configMap:



name: ag-custom-configmap



items:



- key: custom.properties



path: custom.properties
```

Add the following code to the ActiveGate container configuration under `volumeMounts:`.

```
- name: ag-custom-volume



mountPath: /var/lib/dynatrace/gateway/config_template/custom.properties



subPath: custom.properties
```

## Browserless private Synthetic locations

In general, we recommend the deployment of complete synthetic private locations to support the execution of all types synthetic monitors (HTTP, browser, NAM).

If you don't need to run browser monitors, consider deploying your location in browserless mode. This mode deploys the location (or ActiveGate belonging to it) without a browser, reducing hardware requirements. However, browser monitors can't run on a browserless location.

Consider browserless locations as an alternative to synthetic private locations with browser monitor support when youâre focused purely on:

* Network and infrastructure use cases (using NAM monitors)
* API monitoring (using HTTP monitors)

Compared to the regular template, following changes are introduced:

1. `browser` value is set for `DT_SYNTHETIC_UNSUPPORTED_MONITORING_MODULES` environment variable in `synthetic-vuc` container under `env:`

   ```
   - name: DT_SYNTHETIC_UNSUPPORTED_MONITORING_MODULES



   value: "browser"
   ```
2. No `synthetic-vuc-worker` containers are included
3. No `chromium-cache` volume is specified or mounted

## Kerberos authentication configuration

Add the following code at the top of your [location template file](#deploy-location) to insert a ConfigMap resource containing your Kerberos server information.

In the code sample below:

* The `EXAMPLE.COM` realm is used in Kerberos authentication.
* The `example.com` domain is used in Kerberos authentication.
* The `kerberos.example.com` is the hostname of Key Distribution Center.
* The namespace (`namespace: dynatrace`) must be the location namespace.

```
kind: ConfigMap



apiVersion: v1



data:



krb5.conf: |-



[libdefaults]



dns_lookup_realm = false



ticket_lifetime = 24h



renew_lifetime = 7d



forwardable = true



rdns = false



pkinit_anchors = FILE:/etc/pki/tls/certs/ca-bundle.crt



spake_preauth_groups = edwards25519



dns_canonicalize_hostname = fallback



qualify_shortname = ""



default_realm = EXAMPLE.COM



default_ccache_name = /tmp/krb5cc_%{uid}



[realms]



EXAMPLE.COM = {



kdc = kerberos.example.com



admin_server = kerberos.example.com



}



[domain_realm]



.example.com = EXAMPLE.COM



example.com = EXAMPLE.COM



metadata:



name: krb-map



namespace: dynatrace



---
```

Add the following code at `spec.template.spec.volumes:`.

```
- name: krb5-conf



configMap:



name: krb-map



items:



- key: krb5.conf



path: krb5.conf
```

Add the following code to every `synthetic-vuc-worker` container configuration under `volumeMounts:`.

```
- name: krb5-conf



mountPath: /etc/krb5.conf



subPath: krb5.conf
```

## Synthetic metric adapter

### Disable domain certificate validation

Add the following code to Synthetic metric adapter template under `env:`

```
- name: TLS_SECURE



value: "false"
```

This disables certificate validation for the Synthetic metric adapter connection to the Dynatrace Cluster (by default, it is enabled).

### Proxy configuration

Add the following code to Synthetic metric adapter template under `env:`

```
- name: HTTPS_PROXY



value: "http://proxyuser:proxypass@10.102.43.210:3128"



- name: NO_PROXY



value: "172.20.0.0/16"  # do not proxy internal calls to Kubernetes cluster
```

For more details about these environment variables see [Go httpproxy package documentationï»¿](https://pkg.go.dev/golang.org/x/net/http/httpproxy#Config).

The way of obtaining Service CIDR depends on Kubernetes distribution, for example for AWS EKS the following command can be used:

```
aws eks describe-cluster --name my-cluster --query 'cluster.kubernetesNetworkConfig'
```

## Non-scalable containerized locations

Auto-scalable locations become non-scalable for any of the following reasons.

* The location reaches its maximum number of pods in the StatefulSet, and location utilization is over the threshold of 80%. No new ActiveGate pods are created until the maximum number of ActiveGates is increased.
* The [Synthetic metric adapter](#deploy-adapter) stops working, and the location horizontal pod auto-scalers don't receive the metrics required for auto-scaling.

  You can run the following command to verify the state of a pod auto-scaler. In the example below, `dynatrace` is the location namespace.

  ```
  kubectl describe hpa -n dynatrace
  ```

  If `ScalingActive` is set to `False` in the output, the auto-scaler isn't receiving metric data.

## API: Synthetic - Locations, nodes, and configuration API v2

You can automate the deployment of and manage containerized locations via the existing [Synthetic - Locations, nodes, and configuration API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API."). Early Adopter endpoints added to this API to facilitate the deployment of Kubernetes locations. The new endpoints help generate the commands you need to execute on the Kubernetes cluster.

![New endpoints for Kubernetes location deployment](https://dt-cdn.net/images/k8s-locations-endpoints-3168-a8f5b7f158.png)

* The GET location YAML endpoint (`/synthetic/locations/{LocationId}/yaml`) fetches the [location template file](#deploy-location) based on the location ID of the [location you initially set up](#initial-setup) for containerized deployment.
* The GET apply commands endpoint (`synthetic/locations/commands/apply`) fetches the list of commands to [deploy a location](#deploy-location) on Kubernetes/Openshift.
* The GET delete commands endpoint (`synthetic/locations/{LocationId}/commands/delete`)fetches the commands to delete a containerized location.

## Related topics

* [Synthetic locations API v2](/docs/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2 "Manage synthetic locations via the Synthetic v2 API.")
* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")
* [Kubernetes Classic](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring "Monitor Kubernetes/OpenShift with Dynatrace.")