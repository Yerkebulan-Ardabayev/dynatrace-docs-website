---
title: Set up EdgeConnect
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect
scraped: 2026-02-27T21:26:20.647426
---

# Set up EdgeConnect

# Set up EdgeConnect

* Latest Dynatrace
* 2-min read
* Published Oct 11, 2023

EdgeConnect facilitates secure interactions between applications, workflows, and internal systems within a Kubernetes environment. This guide provides information on how to deploy and configure EdgeConnect using Dynatrace.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Create EdgeConnect**](#create-edgeconnect)[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Create OAuth credentials secret**](#create-secret)[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Configure EdgeConnect**](#configure-edgeconnect)[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Verify that EdgeConnect is up**](#check-edgeconnect)

## Step 1 Create EdgeConnect

To create EdgeConnect, follow the instruction provided in [Create a new EdgeConnect configuration](/docs/ingest-from/edgeconnect#createconfiguration "Use EdgeConnect to control how your apps and workflows interact with your internal systems.").

## Step 2 Create OAuth credentials secret

1. Create a secret to hold your OAuth credentials. The values for the OAuth client ID and secret should be obtained from the EdgeConnect configuration created in [Create EdgeConnect](#create-edgeconnect) step.

   ```
   apiVersion: v1



   kind: Secret



   metadata:



   name: edgeconnect-oauth



   namespace: dynatrace



   data:



   oauth-client-id: <base64 encoded client id>



   oauth-client-secret: <base64 encoded client secret>
   ```
2. Apply the secret.

   ```
   kubectl apply -f edgeconnect-oauth-secret.yaml
   ```

## Step 3 Configure EdgeConnect

1. Before applying the configuration, ensure you have all the necessary details. See the configuration fields in [EdgeConnect parameters for Dynatrace Operator](/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters "List of configuration parameters for EdgeConnect.").
2. Create the EdgeConnect custom resource file. Ensure the value for `metadata.name` matches the name you used when creating the EdgeConnect configuration in step 1.

   ```
   apiVersion: dynatrace.com/v1alpha2



   kind: EdgeConnect



   metadata:



   name: sample-edge-connect-name



   namespace: dynatrace



   spec:



   apiServer: "<environment-id>.apps.dynatrace.com"



   replicas: 1



   oauth:



   clientSecret: edgeconnect-oauth



   endpoint: https://sso.dynatrace.com/sso/oauth2/token



   resource: urn:dtenvironment:<tenant>
   ```
3. Apply the EdgeConnect custom resource.

   ```
   kubectl apply -f edgeconnect.yaml
   ```

## Step 4 Verify that EdgeConnect is up

After configuring EdgeConnect, use the command below to check the status of your EdgeConnect.

```
kubectl get edgeconnects -n dynatrace
```

Ensure that the status displays `Running`.

```
NAME          APISERVER                             STATUS    AGE



sample-edge-connect-name   <environment-id>.apps.dynatrace.com   Running   16m
```

## Related topics

* [Configure and deploy EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.")