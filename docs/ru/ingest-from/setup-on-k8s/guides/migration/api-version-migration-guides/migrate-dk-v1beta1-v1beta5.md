---
title: Migration of DynaKube v1beta1 to v1beta5
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/migration/api-version-migration-guides/migrate-dk-v1beta1-v1beta5
scraped: 2026-02-19T21:24:57.741510
---

# Migration of DynaKube v1beta1 to v1beta5

# Migration of DynaKube v1beta1 to v1beta5

* Latest Dynatrace
* Reference
* 10-min read
* Updated on Oct 30, 2025

This guide will show you how you can manually migrate from `apiVersion: dynatrace.com/v1beta1` to `apiVersion: dynatrace.com/v1beta5` of the `DynaKube`.

## Support lifecycle

### v1beta1

**Introduced in**: Dynatrace Operator version 0.3.0

**Deprecated in**: Dynatrace Operator version 1.6.0

**Last supported in**: Dynatrace Operator version 1.6.2

### v1beta5

**Introduced in**: Dynatrace Operator version 1.6.0

## Changes

Reminder

When migrating your DynaKube, remember to update the `apiVersion` field as well as any other fields that have changed

### Prepare for v1beta1 apiVersion removal

Notice

DynaKube CRD v1beta1 apiVersion will be removed in a future release. We recommend that you prepare for this ahead of time.
User action will be required when upgrading from Dynatrace Operator version 1.1.0 and earlier.

Query the current storage version of the DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.spec.versions[?(@.storage==true)].name}'
```

Query the stored versions of the DynaKube CRD:

```
kubectl get customresourcedefinitions dynakubes.dynatrace.com -o jsonpath='{.status.storedVersions}'
```

If the **stored versions list** contains versions that will be removed with the CRD update, **user intervention is required**.

Make sure that the old apiVersion is no longer referenced by any manifest. This includes resources that load manifests from external sources, like Helm releases or ArgoCD applications.
When using GitOps, always check the source that manifests are synced from, because diffing may take conversion into account.

To ensure that the Kubernetes storage backend no longer contains outdated DynaKube objects, we recommend updating them in place.

```
for item in $(kubectl get dynakubes.dynatrace.com -A -o jsonpath='{range .items[*]}{.metadata.namespace}{"/"}{.metadata.name}{"\n"}{end}'); do



namespace=${item%/*}



name=${item#*/}



kubectl get dynakubes.dynatrace.com -n $namespace $name -o yaml | kubectl replace -f -



done
```

Do not use the command `kubectl apply`, because it only writes data when changes are detected.

Once the old apiVersion is no longer referenced, it is safe to update the CRD status.

```
kubectl patch customresourcedefinitions dynakubes.dynatrace.com --subresource status --type merge -p '{"status":{"storedVersions":["<current storage version>"]}}'
```

### Replaced feature flags

#### Dedicated `metadataEnrichment` section

The feature flag for enabling metadata enrichment (`feature.dynatrace.com/metadata-enrichment: true/false`) was moved to a dedicated field:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



enabled: true # replaces feature.dynatrace.com/metadata-enrichment: true



#...
```

#### Dedicated `dynatraceApiRequestThreshold` field

The feature flag for controlling how often Dynatrace Operator can ping the Dynatrace API (`feature.dynatrace.com/dynatrace-api-request-threshold: <number>`) was moved to a dedicated field:

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



dynatraceApiRequestThreshold: 10 # replaces feature.dynatrace.com/dynatrace-api-request-threshold: "10"



#...
```

#### Dedicated `secCompProfile` field for OneAgent

The feature flag that controls which seccomp profile the OneAgent DaemonSet uses (`feature.dynatrace.com/oneagent-seccomp-profile:example`) has been moved to a dedicated field:

Host monitoring

Classic fullstack

Cloud native fullstack

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



hostMonitoring:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



classicFullStack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



secCompProfile: example # replaces feature.dynatrace.com/oneagent-seccomp-profile: "example"



#...
```

#### New CSI mount timeout feature flag

The feature flag that controlled how many mount attempts the CSI driver would make before stopping (`feature.dynatrace.com/max-csi-mount-attempts: 5`) has been replaced with a timeout-based feature flag. This was done due to the difficulty of determining how many attempts equal a given timeout.

```
feature.dynatrace.com/max-csi-mount-timeout: "8m" # replaces feature.dynatrace.com/max-csi-mount-attempts: "10"
```

### Moved fields

#### `spec.namespaceSelector`

The `spec.namespaceSelector` field was moved to each feature subsection that it affects.

Cloud native fullstack

Application monitoring

Metadata enrichment

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullstack:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



oneAgent:



applicationMonitoring:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



metadataEnrichment:



namespaceSelector: ... # replaces spec.namespaceSelector



# ...
```

### Deprecated fields

#### OneAgent `autoUpdate`

The `spec.oneAgent.<mode>.autoUpdate: true/false` field is [deprecated](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect).") in `v1beta5`, so it shouldn't be used.

We recommend the following:

* If you want `autoUpdate: true`, do not set `image`, `codeModulesImage`, or `version`.

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack: {} # same as autoUpdate: true



  # ...
  ```
* If you want `autoUpdate: false`, set `image`, `codeModulesImage` or `version`

  ```
  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  image: ... # same effect as autoUpdate: false



  codeModulesImage: # same effect as autoUpdate: false



  # ...



  ---



  apiVersion: dynatrace.com/v1beta5



  kind: DynaKube



  metadata:



  name: example



  namespace: dynatrace



  spec:



  oneAgent:



  cloudNativeFullstack:



  version: ... # replaces autoUpdate: false



  # ...
  ```

### Removed fields

#### `spec.applicationMonitoring.useCSIDriver`

The `spec.applicationMonitoring.useCSIDriver: true/false` field has been removed.

The CSI driver is now used when installed as part of the Dynatrace Operator installation.

#### `spec.kubernetesMonitoring`

The deprecated field `spec.kubernetesMonitoring` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:

**Before**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



kubernetesMonitoring:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**After**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- kubernetes-monitoring #<-- explicitly enable Kubernetes monitoring



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

#### `spec.routing`

The deprecated field `spec.routing` was removed in favor of using the current `spec.activeGate` section. This example shows you before and after:

**Before**

```
apiVersion: dynatrace.com/v1beta1



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



routing:



enabled: true



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```

**After**

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: example



namespace: dynatrace



spec:



activeGate:



capabilities:



- routing #<-- explicitly enable routing



replicas: ...



image: ...



group: ...



customProperties: ...



resources: ...



nodeSelector: ...



tolerations: ...



labels: ...



env: ...



#...
```