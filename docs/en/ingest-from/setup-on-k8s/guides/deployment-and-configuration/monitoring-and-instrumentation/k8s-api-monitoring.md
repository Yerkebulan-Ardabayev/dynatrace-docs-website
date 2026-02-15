---
title: Kubernetes API Monitoring
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/k8s-api-monitoring
scraped: 2026-02-15T21:19:53.304303
---

# Kubernetes API Monitoring

# Kubernetes API Monitoring

* Latest Dynatrace
* 8-min read
* Updated on Dec 09, 2025

Dynatrace obtains information about Kubernetes entities and metadata by querying the Kubernetes API. This information is used for [out-of-the-box alerting for Kubernetes](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/alert-on-kubernetes-issues "Configure alerts at a Kubernetes/OpenShift cluster, node, namespace, or workload level.") and to provide all observability signals in a proper Kubernetes context within the Dynatrace platform, for example, by creating relationships among applications, (micro-)services, databases, and Kubernetes entities such as pods, namespaces, and nodes.

Dynatrace Operator manages the lifecycle of all Dynatrace components within a Kubernetes cluster and can be configured by deploying a DynaKube Custom Resource. Dynatrace ActiveGateâthe Dynatrace component required to monitor the Kubernetes APIâoffers a capability for Kubernetes API Monitoring.

Follow the steps below to enable Kubernetes API monitoring.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install Dynatrace Operator**](#install-dto)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Configure DynaKube**](#configure-dynakube)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Connect ActiveGate with Kubernetes API**](#connect-ag)

## Step 1 Install Dynatrace Operator

[Install Dynatrace Operator in any deployment mode](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes")

## Step 2 Configure DynaKube

Configure the **ActiveGate** values of the DynaKube according to the [list of parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters#ag "List the available parameters for setting up Dynatrace Operator on Kubernetes.") and add `kubernetes-monitoring` to the ActiveGate capabilities.

```
...



activeGate:



capabilities:



- routing



- kubernetes-monitoring



...
```

## Step 3 Connect ActiveGate with Kubernetes API

You have two options:

* Connect the containerized ActiveGate to a local Kubernetes API endpoint.
* Connect the containerized ActiveGate to the public Kubernetes API URL.

See below for instructions for both options.

### Connect to a local Kubernetes API endpoint

You can enable monitoring by connecting a containerized ActiveGate to a local Kubernetes API endpoint.

There are two ways to connect to the local Kubernetes API endpoint:

* Recommended [Let Dynatrace Operator automatically handle the connection](#auto)
* [Configure the connection manually](#manual)

See below for details on both methods.

Connect automatically

Connect manually

This feature flag is deprecated and enabled by default starting from Dynatrace Operator version 0.13.0.

To connect automatically to the local Kubernetes API endpoint

1. Make sure to enable the **Read entities**, **Read settings**, and **Write settings** permissions (API v2) for your access token (see [Access tokens and permissions](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster")).
2. Make sure that you have the `kubernetes-monitoring` capability enabled in your DynaKube custom resource.
3. Add the following annotation (see example below).

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



   spec:



   ...



   activeGate:



   capabilities:



   - kubernetes-monitoring
   ```

   After adding this annotation, the name of the cluster displayed in Dynatrace will be the same as the DynaKube custom resource where the annotation is configured. You can change the cluster name displayed in Dynatrace by adding the `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"` annotation as well.

   Example with custom cluster name:

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/automatic-kubernetes-api-monitoring: "true"



   feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name: "custom-cluster-name"



   spec:



   ...



   activeGate:



   capabilities:



   - kubernetes-monitoring
   ```
4. Apply your configuration.

   To disable the configuration, remove the annotation.

To connect to a local Kubernetes API endpoint manually, you only need to provide the unique Kubernetes cluster ID (the uuid of the kube-system namespace). The containerized ActiveGate then identifies the unique cluster ID and sends it over to Dynatrace.

#### Step 1 Get the Kubernetes cluster ID

Run the command below and grab the UID from the output.

Kubernetes

OpenShift

```
kubectl get namespace kube-system -o jsonpath='{.metadata.uid}'
```

```
oc get namespace kube-system -o jsonpath='{.metadata.uid}'
```

#### Step 2 Provide the Kubernetes cluster ID in Dynatrace

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Select **Connect manually**.
3. On the Kubernetes cluster connection settings page, provide a **Name**, and then turn on **Connect containerized ActiveGate to local Kubernetes API endpoint**.
4. For **Kubernetes cluster ID**, enter the UID obtained earlier.
5. Select **Save changes** to save your configuration.

   You can save your configuration even if the ActiveGate isn't ready to connect, and finish the configuration later. To verify if it's ready, select **Test configuration**.

### Connect to the public Kubernetes API

To connect to the public Kubernetes API, follow the instructions that apply to your Kubernetes version:

* [Kubernetes version 1.24+](#k8s-new)
* [Kubernetes version earlier than 1.24](#k8s-old)

#### Kubernetes version 1.24+

1. Get the Kubernetes API URL.

   Kubernetes

   OpenShift

   ```
   kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   ```
   oc config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   If you set `enableIstio` to `true` in the [DynaKube custom resourceï»¿](https://dt-url.net/dynakube-samples), use the command below to get the Kubernetes API URL:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Create a file named `token-secret.yaml` with the following content:

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: dynatrace-activegate



   annotations:



   kubernetes.io/service-account.name: "dynatrace-activegate"



   type: kubernetes.io/service-account-token
   ```
3. Apply the file to create the `dynatrace-activegate` secret.

   Kubernetes

   OpenShift

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```

   ```
   oc apply -n dynatrace -f token-secret.yaml
   ```
4. Get the bearer token.

   Kubernetes

   OpenShift

   ```
   kubectl get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret dynatrace-activegate -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```
5. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** and select **Connect manually**.
6. On the Kubernetes cluster connection settings page, provide a **Name**, the **Kubernetes API URL**, and the **Bearer token** for the Kubernetes cluster.
7. Select **Save changes**.

#### Kubernetes version earlier than 1.24

1. Get the Kubernetes API URL.

   Kubernetes

   OpenShift

   ```
   kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   ```
   oc config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```

   If you set `enableIstio` to `true` in the [DynaKube custom resourceï»¿](https://dt-url.net/dynakube-samples), use the command below to get the Kubernetes API URL:

   Kubernetes

   OpenShift

   ```
   kubectl -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```

   ```
   oc -n default get svc/kubernetes -o jsonpath='https://{.spec.clusterIP}'
   ```
2. Get the bearer token.

   Kubernetes

   OpenShift v3.x

   OpenShift v4.x

   ```
   kubectl get secret $(kubectl get sa dynatrace-activegate -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret $(oc get sa dynatrace-activegate -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   ```
   oc get secret $(oc get sa dynatrace-activegate -o jsonpath='{.secrets[1].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Special instructions for Rancher distributions to get the API URL and the bearer token

   For **Rancher distributions** of Kubernetes, you need to use the bearer token and API URL **of the Rancher server**, because this server manages and secures traffic to the Kubernetes API server. Follow the steps below.

   1. Get the **Kubernetes API URL**.

      ```
      kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
      ```
   2. Configure a user.

      In the Rancher web UI, either create a new user or use an existing user to associate with the token. We recommend creating a new user.
   3. Set permissions.

      Make sure the user has either **Owner** or **Custom** permissions to the cluster you want to monitor.

      **Recommended:** select **Custom** permissions, and be sure to select these two roles: **View all Projects** and **View Nodes**.
   4. Create an API key.

      Go to **API & Keys** and create a key either for your specific account (enter your cluster name) or for all clusters (enter **No scope**). For security reasons, we recommend selecting the first option.

      Newly created keys display four fields. Make sure to use the content of the field called **Bearer token** to set up the connection to the Kubernetes API described in the next section.
3. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic** and select **Connect manually**.
4. On the Kubernetes cluster connection settings page, provide a **Name**, the **Kubernetes API URL**, and the **Bearer token** for the Kubernetes cluster.

   For Rancher distributions, you need the bearer token that was created in the Rancher web UI, as described in **Special instructions for Rancher distributions to get the API URL and the bearer token** above.
5. Select **Save changes**.

## Other Options

* If you can't use Dynatrace Operator, you can [deploy ActiveGate directly as a StatefulSet](/docs/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.") (not recommended).
* If you want to monitor several Kubernetes clusters with one ActiveGate and don't need to separate networks for administrative or operational traffic, you can [install an ActiveGate on a virtual machine using a conventional installer](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.").

Dynatrace recommends to use the containerized ActiveGate for Kubernetes API monitoring

## FAQ

Can I change settings for Kubernetes API monitoring?

You can change Kubernetes cluster connection and monitoring settings at any time from your Kubernetes cluster details page.

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster, and then select **Actions** > **Settings**.
3. Adjust your settings, and then select **Save changes**.

How can I delete the Kubernetes Platform Monitoring configuration for a Kubernetes cluster?

To delete the connection to a local Kubernetes API endpoint

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster, and then select **Actions** > **Settings**.
3. Select **Use defaults**, and then select **Save changes**.

When does the ActiveGate get updated?

ActiveGate is updated automatically on pod restart whenever there is a new version available, unless the image version is specified in `cr.yaml`.