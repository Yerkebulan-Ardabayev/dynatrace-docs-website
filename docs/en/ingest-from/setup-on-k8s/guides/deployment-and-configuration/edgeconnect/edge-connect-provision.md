---
title: Provision EdgeConnect for Dynatrace environment
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/edgeconnect/edge-connect-provision
scraped: 2026-02-15T21:23:58.188313
---

# Provision EdgeConnect for Dynatrace environment

# Provision EdgeConnect for Dynatrace environment

* Latest Dynatrace
* 1-min read
* Published Dec 20, 2023

EdgeConnect facilitates secure interactions between applications, workflows, and internal systems within a Kubernetes environment. This guide provides detailed steps for provisioning EdgeConnect for a Dynatrace environment.

## 1. Create OAuth client

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **Identity & access management** > **OAuth clients**.
2. Create an OAuth client with the following scopes.

   * `app-engine:edge-connects:connect`
   * `app-engine:edge-connects:write`
   * `app-engine:edge-connects:read`
   * `app-engine:edge-connects:delete`
   * `oauth2:clients:manage`
3. Save the ID, secret, and your Dynatrace account URN.

## 2. Create OAuth credentials secret

1. Create a secret with the OAuth credentials.

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

## 3. Configure EdgeConnect

1. Configure the EdgeConnect custom resource file with the `provisioner: true` and the `hostPatterns` properties. For the `resource` property, use the Dynatrace account URN that you got earlier.

   ```
   apiVersion: dynatrace.com/v1alpha2



   kind: EdgeConnect



   metadata:



   name: sample-edge-connect-name



   namespace: dynatrace



   spec:



   apiServer: "<environment-id>.apps.dynatrace.com"



   hostPatterns:



   - '*.mycompany.org'



   oauth:



   provisioner: true



   clientSecret: edgeconnect-oauth



   endpoint: https://sso.dynatrace.com/sso/oauth2/token



   resource: urn:dtaccount:<your-account-uuid>
   ```
2. Apply the EdgeConnect custom resource.

   ```
   kubectl apply -f edgeconnect.yaml
   ```

Rotating the OAuth credentials is not immediately reflected in the EdgeConnect deployment. This may lead to authentication issues until Dynatrace Operator reconciles the EdgeConnect deployment.

## Related topics

* [Configure and deploy EdgeConnect](/docs/ingest-from/edgeconnect "Use EdgeConnect to control how your apps and workflows interact with your internal systems.")