---
title: Migrate Dynatrace Operator
source: https://docs.dynatrace.com/managed/upgrade/up-execute-upgrade/up-migrate-dto
scraped: 2026-05-12T12:14:02.572684
---

# Migrate Dynatrace Operator

# Migrate Dynatrace Operator

* Published Aug 02, 2023

If you deployed Dynatrace Operator to a Kubernetes cluster, the easiest way to migrate Kubernetes monitoring from your Managed cluster to your SaaS environment is to reconfigure the Dynatrace Operator deployment. You'll need to update a single configuration to perform Dynatrace Operator reconfiguration at the environment level.

Prerequisites

Before installing Dynatrace on your Kubernetes cluster, ensure that you meet the following requirements:

* Your `kubectl` CLI is connected to the Kubernetes cluster that you want to monitor.
* You have sufficient privileges on the monitored cluster to run `kubectl` or `oc` commands.

### Cluster setup and configuration

* You must allow egress for Dynatrace pods (default: Dynatrace namespace) to your Dynatrace environment URL.

  + For Dynatrace Managed, you can optionally use a Cluster ActiveGate URL.
* For OpenShift Dedicated, you need the [cluster-admin roleï»¿](https://docs.openshift.com/dedicated/osd_cluster_admin/osd-admin-roles.html).
* Helm installation Use [Helm version 3ï»¿](https://dt-url.net/n5036j1).

### Supported versions

See supported Kubernetes/OpenShift [platform versions](/managed/ingest-from/technology-support/support-model-and-issues "How Dynatrace supports Kubernetes and Red Hat OpenShift versions and known issues") and [distributions](/managed/ingest-from/setup-on-k8s/deployment/supported-technologies "Overview of different configurations for all major Kubernetes distributions.").

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Generate a token**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#generate-token "Migrate your Dynatrace Operator configuration to SaaS.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create a new secret**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#secret "Migrate your Dynatrace Operator configuration to SaaS.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Update DynaKube custom resource file**](/managed/upgrade/up-execute-upgrade/up-migrate-dto#update-custom-resource "Migrate your Dynatrace Operator configuration to SaaS.")

## Step 1 Generate a token

To generate an access token in the target SaaS environment,

1. Go to **Access Tokens**.
2. Select **Generate new token**.
3. Enter a name for your token.  
   Dynatrace doesn't enforce unique token names. You can create multiple tokens with the same name. Be sure to provide a meaningful name for each token you generate. Proper naming helps you to efficiently manage your tokens and perhaps delete them when they're no longer needed.
4. Select the template **Kubernetes: Dynatrace Operator**.  
   This will automatically add the required scopes (see [Operator token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#operator-token "Configure tokens and permissions to monitor your Kubernetes cluster")).
5. Select **Generate token**.
6. Copy the generated token to the clipboard. Store the token in a password manager for future use.

   You can only access your token once upon creation. You can't reveal it afterward.

Generating a token in the target SaaS environment won't affect your Kubernetes cluster nor your Managed cluster.

## Step 2 Create a new secret

To create a new secret (`saasdynakube`) holding the new token in the Kubernetes cluster, replace the placeholders in the code sample below (`saasdynakube` and `<API-TOKEN>`) with your own values, then run the command.

Kubernetes

OpenShift

```
kubectl -n dynatrace create secret generic saasdynakube --from-literal="apiToken=<API-TOKEN>"
```

```
oc -n dynatrace create secret generic saasdynakube --from-literal="apiToken=<API-TOKEN>"
```

Your Kubernetes cluster will then contain the new secret `saasdynakube` holding the new token.

## Step 3 Update DynaKube custom resource file

To update an existing [DynaKube custom resource file](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") with the new secret,

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) to find your SaaS [Environment ID].
2. To start modifying `dynakube` custom resource file, run the command below

   Kubernetes

   OpenShift

   ```
   kubectl edit dynakube dynakube -n dynatrace
   ```

   ```
   oc edit dynakube dynakube -n dynatrace
   ```
3. Update the configuration parameter values as follows, making sure to replace the placeholders (`{your-saas-environment-id}` and `saasdynakube`) with your own values

   | Parameter | Updated value |
   | --- | --- |
   | apiUrl | `https://{your-saas-environment-id}.live.dynatrace.com/api` |
   | token | `saasdynakube` |

   Your existing DynaKube custom resource file will then be updated to reference the new secret `saasdynakube` and the SaaS environment.
4. Restart your applications.  
   Your OneAgents will then point to the SaaS environment. Because existing connections to the Dynatrace Managed cluster will no longer be active, we recommend deleting any existing secret that is no longer used for this connection.