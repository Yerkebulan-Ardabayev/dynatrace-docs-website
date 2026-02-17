---
title: Deploy ActiveGate in a VM
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm
scraped: 2026-02-17T05:08:47.258365
---

# Deploy ActiveGate in a VM

# Deploy ActiveGate in a VM

* Latest Dynatrace
* 5-min read
* Updated on Jan 22, 2026

If you want to monitor several Kubernetes clusters with one ActiveGate and don't need to separate networks for administrative or operational traffic, you can install an ActiveGate on a virtual machine using a conventional installer to connect your clusters to Dynatrace as described below.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Start installation**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#start-installation "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Download the installer**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#download-installer "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Run the installer**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#run-installer "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Connect your Kubernetes clusters to Dynatrace**](/docs/ingest-from/setup-on-k8s/deployment/other/ag-in-vm#connect-clusters-to-dynatrace "Set up and configure an ActiveGate for Kubernetes platform monitoring in a virtual machine.")

## Step 1 Start installation

1. In Dynatrace Hub, select **ActiveGate**.
2. Select **Set up**.

3. On the **Install Environment ActiveGate** page, select **Linux**.

## Step 2 Download the installer

How you download your installer depends on your setup and needs. You can choose to download an installer directly to the server where you plan to install Environment ActiveGate or you can download an installer to a different machine and then transfer the installer to the server.

1. Select [Route OneAgent traffic](/docs/ingest-from/dynatrace-activegate/capabilities/routing-monitoring-purpose "Learn about the routing and monitoring capabilities and uses of ActiveGate.") as an [ActiveGate purpose](/docs/ingest-from/dynatrace-activegate#purposes "Understand the basic concepts related to ActiveGate.").
2. Provide an access token with [`PaaS Integration - InstallerDownload`](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.") scope. This token is required to download the ActiveGate installer from your environment. If you don't have an access token, you can create one right in the UI. The token is automatically appended to the download and installation commands you'll use later.
3. Select **Download installer**. There are two options:

   * Download via shell command. Copy and run the `wget` command.
   * Select the link to download the ActiveGate installer.
4. Verify the signature.
   Wait for the download to complete, and then verify the signature by copying the command from the second **Verify signature** text box and pasting the command into your terminal window.

## Step 3 Run the installer

An install parameter (determined by the ActiveGate purpose you selected) is automatically set for the command to run the installer. Make sure you use the command displayed in Dynatrace that reflects the ActiveGate purpose.
Copy the installation script command from the **Run the installer with root rights** step and paste it into your terminal.

### Add the Kubernetes CA certificate to the truststore Recommended

For instructions on how to add the certificate to the truststore file, see [Trusted root certificates for ActiveGate](/docs/ingest-from/dynatrace-activegate/configuration/configure-trusted-root-certificates-on-activegate "Learn how to specify a custom truststore file that is merged with Java's root certificates and used as a default on all connections.").

### Customize installation

You can add additional [parameters](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-customize-installation-for-activegate "Learn about the command-line parameters that you can use with ActiveGate on Linux.") to the installation command to customize your installation. For example, to install ActiveGate in a different directory, use the `INSTALL=<path>` parameter:

```
[root@host]# /bin/bash Dynatrace-ActiveGate-Linux-x86-1.0.0.sh INSTALL=/hosted_app/dynatrace
```

### Default installation settings

For installation defaults, including default directories, see [ActiveGate default settings for Linux](/docs/ingest-from/dynatrace-activegate/installation/linux/linux-default-settings "Learn about the default settings with which ActiveGate is installed on Linux").

## Step 4 Connect your Kubernetes clusters to Dynatrace

To connect the Kubernetes API to Dynatrace, follow the instructions that apply to your Kubernetes version.

1. Create a service account and cluster role.

   Create a `kubernetes-monitoring-service-account.yaml` file with the following content.

   kubernetes-monitoring-service-account.yaml

   ```
   apiVersion: v1



   kind: ServiceAccount



   metadata:



   name: dynatrace-monitoring



   namespace: dynatrace



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRole



   metadata:



   name: dynatrace-monitoring-cluster



   rules:



   - apiGroups:



   - ""



   resources:



   - nodes



   - pods



   - namespaces



   - replicationcontrollers



   - events



   - resourcequotas



   - pods/proxy



   - nodes/proxy



   - nodes/metrics



   - services



   - persistentvolumeclaims



   - persistentvolumes



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - batch



   resources:



   - jobs



   - cronjobs



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apps



   resources:



   - deployments



   - replicasets



   - statefulsets



   - daemonsets



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apps.openshift.io



   resources:



   - deploymentconfigs



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - config.openshift.io



   resources:



   - clusterversions



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - dynatrace.com



   resources:



   - dynakubes



   - edgeconnects



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - apiextensions.k8s.io



   resources:



   - customresourcedefinitions



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - networking.k8s.io



   resources:



   - ingresses



   - networkpolicies



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - discovery.k8s.io



   resources:



   - endpointslices



   verbs:



   - list



   - watch



   - get



   - apiGroups:



   - autoscaling



   resources:



   - horizontalpodautoscalers



   verbs:



   - list



   - watch



   - get



   - nonResourceURLs:



   - /metrics



   - /version



   - /readyz



   - /livez



   verbs:



   - get



   ---



   apiVersion: rbac.authorization.k8s.io/v1



   kind: ClusterRoleBinding



   metadata:



   name: dynatrace-monitoring-cluster



   roleRef:



   apiGroup: rbac.authorization.k8s.io



   kind: ClusterRole



   name: dynatrace-monitoring-cluster



   subjects:



   - kind: ServiceAccount



   name: dynatrace-monitoring



   namespace: dynatrace
   ```
2. Apply the file.

   ```
   kubectl apply -f kubernetes-monitoring-service-account.yaml
   ```
3. Get the Kubernetes API URL.

   ```
   $ kubectl config view --minify -o jsonpath='{.clusters[0].cluster.server}'
   ```
4. Kubernetes version 1.24+ Create a file named `token-secret.yaml` with the following content.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: dynatrace-monitoring



   annotations:



   kubernetes.io/service-account.name: "dynatrace-monitoring"



   type: kubernetes.io/service-account-token
   ```
5. Kubernetes version 1.24+ Apply the file to create the `dynatrace-monitoring` secret.

   ```
   kubectl apply -n dynatrace -f token-secret.yaml
   ```
6. Get the bearer token.

   Kubernetes version 1.24+

   ```
   kubectl get secret dynatrace-monitoring -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
   ```

   Kubernetes versions 1.23 and lower

   ```
   kubectl get secret $(kubectl get sa dynatrace-monitoring -o jsonpath='{.secrets[0].name}' -n dynatrace) -o jsonpath='{.data.token}' -n dynatrace | base64 --decode
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

      **Recommended**: select **Custom** permissions, and be sure to select these two roles: **View all Projects** and **View Nodes**.
   4. Create an API key.

      Go to **API & Keys** and create a key either for your specific account (enter your cluster name) or for all clusters (enter **No scope**). For security reasons, we recommend selecting the first option.

      Newly created keys display four fields. Make sure to use the content of the field called **Bearer token** to set up the connection to the Kubernetes API described in the next section.
7. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
8. Select **Connect manually**.
9. Provide a **Name**, the **Kubernetes API URL target**, and the **Kubernetes bearer token** for the Kubernetes cluster.
10. Make sure **Monitor events** and **Monitor Kubernetes namespaces, services, workloads, and pods** are turned on.

Disabling certificate validation isn't recommended because it imposes security risks. However, if you still want to disable certificate validation for test environments, make sure to disable **Require valid certificates for communication with the API server (recommended)** and **Verify hostname in certificate against Kubernetes API URL**.

11. Select **Save changes** to save your configuration.

To update ActiveGate, see [Update ActiveGate](/docs/ingest-from/dynatrace-activegate/operation/update-activegate "Learn how to find out which version of ActiveGate you have installed and how you can download and install the latest version.").