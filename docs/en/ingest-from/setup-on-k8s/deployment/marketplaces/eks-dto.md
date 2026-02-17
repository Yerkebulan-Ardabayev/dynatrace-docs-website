---
title: Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/deployment/marketplaces/eks-dto
scraped: 2026-02-17T05:01:01.552864
---

# Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)

# Install Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS)

* Latest Dynatrace
* 3-min read
* Published Jan 16, 2024

To use the Dynatrace Operator add-on for AWS Elastic Kubernetes Service (AWS EKS), you need to install the add-on and then connect EKS with your environment.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Install Dynatrace Operator add-on EKS**](#install-dto)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Connect EKS with your environment**](#connect-eks)

## Step 1 Install Dynatrace Operator add-on for EKS

You can install the Dynatrace Operator add-on for AWS EKS through the AWS console or the CLI.

### Install through AWS console

To install the Dynatrace Operator add-on for AWS EKS through the AWS console

1. Go to your EKS cluster.
2. In the **Add-ons** section, select **Get more add-ons** > **AWS Marketplace add-ons**.
3. Filter for category **Monitoring** or search for **Dynatrace** to find the Dynatrace Operator add-on.
4. Select the checkbox in the upper-right corner of the card and then select **Next**.
5. Optional Select the version for this add-on and IAM role.
6. Select **Next** and review the configuration before applying.
7. Select **Create** and wait for the operation to finish.

   * The cluster overview page displays a confirmation banner.
   * A new `dynatrace` namespace is created
   * Several resources are automatically deployed by rendering the underlying helm chart.

### Installation through the CLI

To install the Dynatrace Operator add-on for AWS EKS through the CLI

1. Check the availability of the add-on and its versions.

   ```
   aws eks describe-addon-versions --addon-name dynatrace_dynatrace-operator
   ```
2. Deploy the add-on, specifying the version if necessary.

   ```
   aws eks create-addon --cluster-name <your_cluster_name> --addon-name dynatrace_dynatrace-operator --addon-version <version>
   ```
3. Verify the successful installation.

   ```
   aws eks describe-addon --cluster-name <your_cluster_name> --addon-name dynatrace_dynatrace-operator
   ```

## Step 2 Connect EKS with your environment

1. Create secret for access tokens.

   Create a secret named `dynakube` for the Dynatrace Operator token and data ingest token obtained in [Tokens and permissions required](/docs/ingest-from/setup-on-k8s/deployment/tokens-permissions "Configure tokens and permissions to monitor your Kubernetes cluster").

   ```
   kubectl -n dynatrace create secret generic dynakube --from-literal="apiToken=<OPERATOR_TOKEN>" --from-literal="dataIngestToken=<DATA_INGEST_TOKEN>"
   ```
2. Apply the DynaKube custom resource

   Monitoring with `cloudNativeFullStack` or `appOnly` (with CSI driver) is only supported for Dynatrace Operator version 0.15.0+.

   Download the [DynaKube custom resource sample for cloud-native full-stack mode on GitHubï»¿](https://dt-url.net/9n636jg). In addition, you can review the [available parameters](/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") or [how-to-guides](/docs/ingest-from/setup-on-k8s/guides "Detailed description of installation and configuration options for specific use-cases"), and adapt the DynaKube custom resource according to your requirements.

   Run the command below to apply the DynaKube custom resource, making sure to replace `<your-DynaKube-CR>` with your actual DynaKube custom resource file name. A validation webhook will provide helpful error messages if there's a problem.

   ```
   kubectl apply -f <your-DynaKube-CR>.yaml
   ```
3. Optional Verify deployment

   Verify that your DynaKube is running and all Pods in your Dynatrace namespace are running and ready.

   ```
   > kubectl get dynakube -n dynatrace



   NAME         APIURL                                          STATUS     AGE



   dynakube     https://<ENVIRONMENTID>.live.dynatrace.com/api  Running    45s
   ```

   In a default DynaKube configuration, you should see the following Pods:

   ```
   > kubectl get pods -n dynatrace



   NAME                                  READY   STATUS    RESTARTS        AGE



   dynakube-activegate-0                 1/1     Running   0               50s



   dynakube-oneagent-b88rn               1/1     Running   0               50s



   dynakube-oneagent-m5jm4               1/1     Running   0               50s



   dynakube-oneagent-qhd9u               1/1     Running   0               50s



   dynatrace-oneagent-csi-driver-qxfwx   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-xk5c4   4/4     Running   0               2m49s



   dynatrace-oneagent-csi-driver-mz6ch   4/4     Running   0               2m49s



   dynatrace-operator-7dc8dc7d8c-wmh4z   1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-l8fsq    1/1     Running   0               2m59s



   dynatrace-webhook-7bb6957fb5-rqnqk    1/1     Running   0               2m59s
   ```