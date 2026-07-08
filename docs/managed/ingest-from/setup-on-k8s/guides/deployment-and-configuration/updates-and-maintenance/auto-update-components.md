---
title: Configure auto-update for Dynatrace Operator managed components
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components
---

# Configure auto-update for Dynatrace Operator managed components

# Configure auto-update for Dynatrace Operator managed components

* 2-min read
* Updated on Sep 05, 2025

Dynatrace Operator manages the rollout and updates of the following components in Kubernetes:

* OneAgent: Configured in the DynaKube
* ActiveGate: Configured in the DynaKube
* EdgeConnect: Configured by the EdgeConnect Custom Resource (CR)

The default settings for OneAgent and ActiveGate automatically roll out updates as soon as they become available. DynaKube also defaults to update all pods when updates are detected automatically. Note that updates may take up to 15 minutes due to Dynatrace Operator checking for updates at 15-minute intervals. If you set a custom `image`, it will disable automatic updates.

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

To disable auto-update, set the `image` field in the DynaKube. Omit the field to keep auto-update enabled.

```
# Auto-update enabled (default) — omit image



spec:



oneAgent:



cloudNativeFullStack: {}



# Auto-update disabled — pin a specific image



spec:



oneAgent:



cloudNativeFullStack:



image: public.ecr.aws/dynatrace/dynatrace-oneagent:<tag>
```

## Configure code module auto-update of monitored applications

While new images are downloaded, applications are only updated when restarted. Keep in mind that autoscaling also injects the most recent CodeModule.

## Configure ActiveGate auto-update

Similar to OneAgent, the ActiveGate update can be configured in the UI, resulting in a changed ActiveGate image, visible to Dynatrace Operator.