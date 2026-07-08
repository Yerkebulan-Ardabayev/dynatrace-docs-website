---
title: Set up Kubernetes platform monitoring with DaemonSet
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/oneagent-daemonset
---

# Set up Kubernetes platform monitoring with DaemonSet

# Set up Kubernetes platform monitoring with DaemonSet

* 4-min read
* Published Jan 21, 2020

Deprecated

Manually configuring a daemonset to rollout OneAgent on a Kubernetes cluster is deprecated.

We recommend that you leverage Dynatrace Operator and benefit from automated lifecycle management and metadata enrichment. For a clear view of all the deployment strategies, see [How it works](/managed/ingest-from/setup-on-k8s/how-it-works "In-depth description on how the deployment on Kubernetes works.").

This page describes how you can set up OneAgent on Kubernetes using the OneAgent DaemonSet. DaemonSet is a feature that makes sure that if a copy of a Pod on a node dies, the copy is recreated, and if nodes are added to the cluster, copies of the Pod are added as well.

## Prerequisites

* Pods must allow egress to your Dynatrace environment or to your Environment ActiveGate in order for metric routing to work properly.
* Locate the `ONEAGENT_INSTALLER_SCRIPT_URL`. This information is shared during Dynatrace OneAgent installation.

How to locate your installer URL

To get your `ONEAGENT_INSTALLER_SCRIPT_URL`

1. Go to **Deploy Dynatrace**.
2. Select **Start installation** > **Linux**.

3. Determine the installer script URL and token from the UI-provided `wget` command:

OneAgent container image version 1.39.1000+

OneAgent container image version 1.38.1000 and earlier

This is the URL:

![OneAgent URL](https://dt-cdn.net/images/oneagent-url-570-2bbd3eb216.png)

OneAgent URL

* Replace the value of `arch` parameter with `<arch>`. Ignore the `flavor=default` parameter.
* For the `API-Token` value, you need a [PaaS token](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens#paas-token "Learn the concept of an access token and its scopes.").

Your URL should look like this:
`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=<arch>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

This your URL and API token.

![OneAgent installation page with URL to be modified](https://dt-cdn.net/images/oneagent-linux-install-url-734-22e9ac9a69.png)

OneAgent installation page with URL to be modified

Append the API token to the URL using the `API-Token` parameter. Your URL should look like this:

`https://host.domain.com/api/v1/deployment/installer/agent/unix/default/latest?arch=x86&flavor=default&Api-Token=<token>`

This is your `ONEAGENT_INSTALLER_SCRIPT_URL`.

## Install DaemonSet

1. Download or copy the `dynatrace-oneagent.yml` Kubernetes template.

   dynatrace-oneagent.yml

   ```
   apiVersion: apps/v1



   kind: DaemonSet



   metadata:



   name: dynatrace-oneagent



   spec:



   selector:



   matchLabels:



   name: dynatrace-oneagent



   template:



   metadata:



   labels:



   name: dynatrace-oneagent



   spec:



   hostPID: true



   hostIPC: true



   hostNetwork: true



   nodeSelector:



   beta.kubernetes.io/os: linux



   volumes:



   - name: host-root



   hostPath:



   path: /



   containers:



   - name: dynatrace-oneagent



   image: dynatrace/oneagent



   env:



   - name: ONEAGENT_INSTALLER_SCRIPT_URL



   value: your_URL



   - name: ONEAGENT_INSTALLER_SKIP_CERT_CHECK



   value: 'false'



   - name: ONEAGENT_INSTALLER_DOWNLOAD_TOKEN



   value: '<API-Token>'



   args:



   - '--set-network-zone=<your.network.zone>'



   volumeMounts:



   - name: host-root



   mountPath: /mnt/root



   securityContext:



   privileged: true
   ```

   * `ONEAGENT_INSTALLER_DOWNLOAD_TOKEN` is only needed for OneAgent container image versions 1.39+ and is ignored for earlier versions.
   * The `--set-app-log-content-access` parameter is passed to the OneAgent installer and, when set to `true` (or `1`), allows OneAgent to access log files for the purpose of log monitoring. For more about this and other parameters, see [Customize OneAgent installation on Linux](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters.").
   * You can configure network zones by setting the `--set-network-zone=<your.network.zone>` parameter. See [network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.") for more information.
2. Deploy Dynatrace OneAgent using the created file `dynatrace-oneagent.yml`.

   Kubernetes

   OpenShift

   ```
   kubectl apply -f dynatrace-oneagent.yml --namespace=kube-system



   daemonset "dynatrace-oneagent" created
   ```

   ```
   oc apply -f dynatrace-oneagent.yml --namespace=kube-system



   daemonset "dynatrace-oneagent" created
   ```
3. Verify that the `dynatrace-oneagent` DaemonSet has deployed Pods to the cluster nodes successfully:

   Kubernetes

   OpenShift

   ```
   kubectl get pods --namespace=kube-system



   NAME                       READY     STATUS              RESTARTS   AGE



   dynatrace-oneagent-abcde   1/1       Running             0          1m
   ```

   ```
   oc get pods --namespace=kube-system



   NAME                       READY     STATUS              RESTARTS   AGE



   dynatrace-oneagent-abcde   1/1       Running             0          1m
   ```

   Kubernetes

   OpenShift

   ```
   kubectl logs -f dynatrace-oneagent-abcde



   09:46:18 Using volume-based storage



   09:46:18 Started agent deployment as a Docker container, PID 1234.



   09:46:18 Downloading agent to /tmp/Dynatrace-OneAgent-Linux.sh via https://EnvironmentID.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=***&arch=x86&flavor=default



   09:46:21 Download complete



   09:46:21 Downloaded version: 1.x



   09:46:21 Validating downloaded agent installer



   09:46:23 Verification successful



   ...
   ```

   ```
   oc logs -f dynatrace-oneagent-abcde



   09:46:18 Using volume-based storage



   09:46:18 Started agent deployment as a Docker container, PID 1234.



   09:46:18 Downloading agent to /tmp/Dynatrace-OneAgent-Linux.sh via https://EnvironmentID.live.dynatrace.com/api/v1/deployment/installer/agent/unix/default/latest?Api-Token=***&arch=x86&flavor=default



   09:46:21 Download complete



   09:46:21 Downloaded version: 1.x



   09:46:21 Validating downloaded agent installer



   09:46:23 Verification successful



   ...
   ```

## Limitations

* When you set up Kubernetes/OpenShift monitoring with DaemonSet, the shutdown state of the host is not detected. For details, see [Host availability states](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring/host-availability#states "Check host availability, interpret host availability states, and see how maintenance windows are reflected in host availability charts.").
* See [Docker limitations](/managed/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container.").

## Connect your Kubernetes clusters to Dynatrace

Now that you have OneAgent running on your Kubernetes nodes, you're able to monitor those nodes and the applications running in Kubernetes. The next step is to connect the Kubernetes API to Dynatrace in order to get native Kubernetes metrics, like request limits, and differences in Pods requested vs running Pods.  
For further instructions, see [Connect your Kubernetes clusters to Dynatrace](/managed/ingest-from/setup-on-k8s/deployment/other/ag-statefulset "Install and configure ActiveGate in Kubernetes as a StatefulSet.").

## Update OneAgent DaemonSet

Whenever a new version of OneAgent becomes available in Dynatrace, you can redeploy OneAgent as explained in the steps below. The `dynatrace-oneagent` container will automatically fetch the latest version of Dynatrace OneAgent.

If you've specified a default OneAgent installation version for new hosts and applications in your [OneAgent updates settings](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/update-oneagent-on-linux "Learn about the different ways to update OneAgent on Linux."), the `dynatrace-oneagent` container will automatically fetch the defined default version of OneAgent.

1. Delete the `dynatrace-oneagent` DaemonSet.

   Kubernetes

   OpenShift

   ```
   kubectl delete ds/dynatrace-oneagent
   ```

   ```
   oc delete ds/dynatrace-oneagent
   ```
2. Deploy Dynatrace OneAgent using the `dynatrace-oneagent.yml` [DaemonSet file](#install).

   Kubernetes

   OpenShift

   ```
   kubectl apply -f dynatrace-oneagent.yml --namespace=kube-system
   ```

   ```
   oc apply -f dynatrace-oneagent.yml --namespace=kube-system
   ```

## Uninstall OneAgent DaemonSet

1. Delete the `dynatrace-oneagent` DaemonSet.

   Kubernetes

   OpenShift

   ```
   kubectl delete ds/dynatrace-oneagent
   ```

   ```
   oc delete ds/dynatrace-oneagent
   ```
2. Optional After deleting the `dynatrace-oneagent` DaemonSet, the OneAgent binary remains on the node in an inactive state. To uninstall it completely, run the `uninstall.sh` script and delete logs and configuration files.  
   See [Linux related information](/managed/ingest-from/dynatrace-oneagent/installation-and-operation/linux/operation/uninstall-oneagent-on-linux "Learn how you can remove OneAgent from your Linux-based system.").