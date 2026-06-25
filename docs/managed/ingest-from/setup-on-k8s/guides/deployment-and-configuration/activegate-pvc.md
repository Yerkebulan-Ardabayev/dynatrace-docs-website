---
title: Configure persistent storage for the ActiveGate
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc
scraped: 2026-05-12T11:36:21.361977
---

# Configure persistent storage for the ActiveGate

# Configure persistent storage for the ActiveGate

* 1-min read
* Updated on Feb 04, 2026

The [`log_analytics_collector`](/managed/ingest-from/dynatrace-activegate/configuration/configure-activegate#logdiskbuffer "Learn which ActiveGate properties you can configure based on your needs and requirements.") ActiveGate module utilizes disk buffers to temporarily store data. To avoid data loss across ActiveGate restarts, we recommend attaching a [PersistentVolumeClaimï»¿](https://kubernetes.io/docs/concepts/storage/persistent-volumes) (PVC) to the ActiveGate.

## Adding a PersistentVolumeClaim

The following snippet shows how you can attach the PersistentVolumeClaim to the ActiveGate in the DynaKube.

v1beta5

v1beta4

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



volumeClaimTemplate:



accessModes:



- ReadWriteOnce



resources:



requests:



storage: 1Gi
```

```
apiVersion: dynatrace.com/v1beta4



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



persistentVolumeClaim:



accessModes:



- ReadWriteOnce



resources:



requests:



storage: 1Gi
```

Kubernetes environments without a default StorageClass require you to set `storageClassName` field. Without it, the ActiveGate pod may fail to schedule with the error: `pod has unbound immediate PersistentVolumeClaims`. This requirement also applies to EEC (Extensions Execution Controller) deployments.

Ensure that the `storageClassName` value corresponds to a valid StorageClass in your cluster:

```
persistentVolumeClaim:



storageClassName: fast-ssd
```

## Adjusting ActiveGate shutdown grace period

When the ActiveGate performs a graceful shutdown (for example, in a scale-in scenario), it needs to flush buffers to avoid data loss. In large environments, this can take longer than the default grace period of Kubernetes, which is 30s. To avoid this, setting a longer `terminationGracePeriodSeconds` on the ActiveGate pods can be helpful. You can change it as shown in the following snippet.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



terminationGracePeriodSeconds: 120s
```