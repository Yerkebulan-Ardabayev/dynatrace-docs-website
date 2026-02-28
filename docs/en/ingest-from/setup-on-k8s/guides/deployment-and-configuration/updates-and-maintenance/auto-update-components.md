---
title: Configure auto-update for Dynatrace Operator managed components
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components
scraped: 2026-02-28T21:23:39.711249
---

# Configure auto-update for Dynatrace Operator managed components

# Configure auto-update for Dynatrace Operator managed components

* Latest Dynatrace
* 2-min read
* Updated on Sep 05, 2025

Dynatrace Operator manages the rollout and updates of the following components in Kubernetes:

* OneAgent: Configured in the DynaKube
* ActiveGate: Configured in the DynaKube
* EdgeConnect: Configured by the EdgeConnect Custom Resource (CR)

The default settings for OneAgent and ActiveGate automatically roll out updates as soon as they become available. DynaKube also defaults to update all pods when updates are detected automatically. Note that updates may take up to 15 minutes due to Dynatrace Operator checking for updates at 15-minute intervals. If you set a custom `image` or `version`, it will disable automatic updates.

## Configure OneAgent auto-update

Set the target version on the Dynatrace Server to a relative version, for example, `Latest stable version`. Dynatrace Operator will periodically check for updates and propagate them to the Kubernetes environment. An update of the OneAgent version will always cause restart of the OneAgent pods.

Minimal DynaKube configuration that uses auto-update:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://ENVIRONMENTID.live.dynatrace.com/api



oneAgent:



cloudNativeFullStack: {}
```

Update windows currently do not apply in Kubernetes environments.

If `autoUpdate` is set to `false` in the DynaKube, the OneAgents will not get version updates based on the target version of the Dynatrace environment after the initial deployment of the OneAgents.

We do not recommend setting `autoUpdate: false` directly. To control OneAgent version updates, we recommend doing one of the following:

* Set `autoUpdate: true` and set the target version in the Dynatrace environment's web UI
* Configure the `image` field in the DynaKube
* Configure the `version` field in the DynaKube

## Configure code module auto-update of monitored applications

While new images are downloaded, applications are only updated when restarted. Keep in mind that autoscaling also injects the most recent CodeModule.

## Configure ActiveGate auto-update

Similar to OneAgent, the ActiveGate update can be configured in the UI, resulting in a changed ActiveGate image, visible to Dynatrace Operator.

## Configure EdgeConnect auto-update

Dynatrace Operator can be configured to disable auto-updates by setting the `autoUpdate` field in the [EdgeConnect spec](/docs/ingest-from/setup-on-k8s/reference/edgeconnect-parameters#spec "List of configuration parameters for EdgeConnect.") section to `false`.

```
apiVersion: dynatrace.com/v1alpha2



kind: EdgeConnect



metadata:



name: edgeconnect



namespace: dynatrace



spec:



autoUpdate: false
```