---
title: Set up OpenShift monitoring via OperatorHub
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/other/ocp-operator-hub
scraped: 2026-02-17T04:57:52.026277
---

# Set up OpenShift monitoring via OperatorHub

# Set up OpenShift monitoring via OperatorHub

* Latest Dynatrace
* 2-min read
* Published Jun 15, 2020

The OperatorHub is the interface that cluster administrators use to discover and install operators and is available via the OpenShift Container Platform web console.

## Prerequisites for OpenShift Dedicated

* A dedicated-admin user for the OpenShift Dedicated cluster

How to add a user to a dedicated-admin role

1. Sign in to the [Red Hat OpenShift Cluster Managerï»¿](https://cloud.redhat.com/openshift) with your Red Hat account.
2. Select the OpenShift Dedicated cluster and go to **Access control** > **Cluster administrative users** > **Add user**.
3. Add the userid of the user who will have dedicated-admin access.

The dedicated-admin user must be added before the OneAgent Operator is visible in the OperatorHub UI.

## Limitations

Deployment options that can be installed from OperatorHub:

* [Kubernetes platform monitoring](/docs/ingest-from/setup-on-k8s/deployment/platform-observability "Deploy Dynatrace Operator for Kubernetes platform monitoring.")
* [Classic Full-Stack monitoring](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")
* [Application observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") without CSI driver

Deployment options that **can't** be installed from OperatorHub (they require Helm or manifest installation approaches):

* [Full-Stack observability](/docs/ingest-from/setup-on-k8s/deployment/full-stack-observability "Deploy Dynatrace Operator in cloud-native full-stack mode to Kubernetes")
* [Application observability](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes") with CSI driver
* [Host monitoring](/docs/ingest-from/setup-on-k8s/deployment/other/host-monitoring "Deploy Dynatrace Operator in host monitoring mode to Kubernetes")

## Installation

To install Dynatrace Operator on OpenShift via OperatorHub

1. On the OpenShift Container Platform dashboard, select **Operators** > **OperatorHub** from the side menu.
2. Select **Dynatrace Operator** > **Install**.
3. Enter the necessary information about the Operator subscription.
4. In **Installation Mode**, select **All namespaces**.
5. Keep the default values of the other settings and select **Subscribe**.
6. Go to **Operators** > **Installed Operators** and wait until you see **Install Succeeded**.
7. Go to **Workloads** > **Secrets** and create a new key named `dynakube` with two values:

   * `apiToken` equal to your cluster's [Dynatrace Operator token](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
   * `dataIngestToken` equal to your cluster's [Data Ingest token](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").
8. Go to **Operators** > **Installed Operators** from the side menu and select **Dynatrace Operator**.
9. Select **Create instance**.
10. Make the following changes:

    * Replace `apiURL` value according to your deployment:

      Dynatrace SaaS

      ```
      spec:



      apiURL: 'https://ENVIRONMENTID.live.dynatrace.com/api'
      ```

      Replace `ENVIRONMENTID` with your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
    * Set `classicFullStack.enabled` to `true`.
    * If you're using a custom resource file, set `namespace` to the namespace where you installed Dynatrace Operator.
11. Select **Create**.