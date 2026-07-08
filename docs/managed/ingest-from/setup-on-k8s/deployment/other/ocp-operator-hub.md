---
title: Set up OpenShift monitoring via OperatorHub
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub
---

# Set up OpenShift monitoring via OperatorHub

# Set up OpenShift monitoring via OperatorHub

* 2-min read
* Updated on Mar 20, 2026

The OperatorHub is the interface that cluster administrators use to discover and install operators and is available via the OpenShift Container Platform web console.

## Prerequisites for OpenShift Dedicated

* A dedicated-admin user for the OpenShift Dedicated cluster

How to add a user to a dedicated-admin role

1. Sign in to the [Red Hat OpenShift Cluster Manager﻿](https://cloud.redhat.com/openshift) with your Red Hat account.
2. Select the OpenShift Dedicated cluster and go to **Access control** > **Cluster administrative users** > **Add user**.
3. Add the userid of the user who will have dedicated-admin access.

The dedicated-admin user must be added before the OneAgent Operator is visible in the OperatorHub UI.

## Limitations

Deployment options that can be installed from OperatorHub:

* [Kubernetes platform monitoring﻿](https://docs.dynatrace.com/docs/shortlink/installation-k8s-platform-only)
* [Classic Full-Stack monitoring﻿](https://docs.dynatrace.com/docs/shortlink/installation-k8s-classic-fs)
* [Application observability﻿](https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-monitoring) without CSI driver
* [Full-Stack observability﻿](https://docs.dynatrace.com/docs/shortlink/node-image-pull) without CSI driver

Deployment options that **can't** be installed from OperatorHub (they require Helm or manifest installation approaches):

* [Full-Stack observability﻿](https://docs.dynatrace.com/docs/shortlink/installation-k8s-cloud-native-fs) with CSI driver
* [Application observability﻿](https://docs.dynatrace.com/docs/shortlink/installation-k8s-automated-app-monitoring) with CSI driver
* [Host monitoring﻿](https://docs.dynatrace.com/docs/shortlink/k8s-host-monitoring)

## Installation

To install Dynatrace Operator on OpenShift via OperatorHub

1. On the OpenShift Container Platform dashboard, select **Operators** > **OperatorHub** from the side menu.
2. Select **Dynatrace Operator** > **Install**.
3. Enter the necessary information about the Operator subscription.
4. In **Installation Mode**, select **All namespaces**.
5. Keep the default values of the other settings and select **Subscribe**.
6. Go to **Operators** > **Installed Operators** and wait until you see **Install Succeeded**.
7. Go to **Workloads** > **Secrets** and create a new key named `dynakube` with two values:

   * `apiToken` equal to your cluster's [Dynatrace Operator token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
   * `dataIngestToken` equal to your cluster's [Data Ingest token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
8. Go to **Operators** > **Installed Operators** from the side menu and select **Dynatrace Operator**.
9. Select **Create instance**.
10. Make the following changes:

    * Replace `apiURL` value according to your deployment:

      Dynatrace SaaS

      ```
      spec:



      apiURL: 'https://ENVIRONMENTID.live.dynatrace.com/api'
      ```

      Replace `ENVIRONMENTID` with your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").

      Dynatrace Managed

      ```
      spec:



      apiURL: 'https://<YourDynatraceServerURL>/e/<ENVIRONMENTID>/api'
      ```

      Replace `YourDynatraceServerURL` with the address of your Dynatrace Managed Cluster and `ENVIRONMENTID` with your [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.").
    * Set `classicFullStack.enabled` to `true`.
    * If you're using a custom resource file, set `namespace` to the namespace where you installed Dynatrace Operator.
11. Select **Create**.