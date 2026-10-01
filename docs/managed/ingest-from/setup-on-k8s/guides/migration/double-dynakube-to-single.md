---
title: Consolidate Kubernetes monitoring into a single DynaKube
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/migration/double-dynakube-to-single
---

# Consolidate Kubernetes monitoring into a single DynaKube

# Consolidate Kubernetes monitoring into a single DynaKube

* How-to guide
* 5-min read
* Published Sep 30, 2026

Dynatrace Operator version 1.11.0+

Consolidate the `kubernetes-monitoring` ActiveGate capability into the DynaKube that configures your routing ActiveGate and OneAgent monitoring, using `spec.kubernetesMonitoring`. This simplifies cluster configuration and reduces the number of DynaKube resources to maintain.

Starting with Dynatrace Operator version 1.11.0, `spec.kubernetesMonitoring` lets you configure Kubernetes monitoring alongside routing and OneAgent in a single DynaKube. The underlying functionality is unchanged; only the configuration moves.

Before: two DynaKubes

After: single DynaKube

```
# DynaKube 1: Kubernetes monitoring



apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



activeGate:



capabilities:



- kubernetes-monitoring



resources:



requests:



cpu: 1000m



memory: 10Gi



limits:



cpu: 2000m



memory: 10Gi



replicas: 1



kspm:



mappedHostPaths:



- /boot



- /etc



- /proc/sys/kernel



- /sys/fs



- /sys/kernel/security/apparmor



- /usr/lib/systemd/system



- /var/lib



---



# DynaKube 2: OneAgent + routing ActiveGate



apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: k8s-agents



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullStack:



tolerations:



- effect: NoSchedule



key: node-role.kubernetes.io/master



operator: Exists



- effect: NoSchedule



key: node-role.kubernetes.io/control-plane



operator: Exists



activeGate:



capabilities:



- routing



- debugging



resources:



requests:



cpu: 500m



memory: 4Gi



limits:



cpu: 2000m



memory: 4Gi



replicas: 3



logMonitoring: {}



telemetryIngest:



protocols:



- jaeger



- otlp



- statsd



- zipkin



serviceName: telemetry-ingest
```

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: k8s-agents



namespace: dynatrace



spec:



oneAgent:



cloudNativeFullStack:



tolerations:



- effect: NoSchedule



key: node-role.kubernetes.io/master



operator: Exists



- effect: NoSchedule



key: node-role.kubernetes.io/control-plane



operator: Exists



activeGate:



capabilities:



- routing



- debugging



resources:



requests:



cpu: 500m



memory: 4Gi



limits:



cpu: 2000m



memory: 4Gi



replicas: 3



kubernetesMonitoring:



replicas: 1



registration: {}



resources:



requests:



cpu: 1000m



memory: 10Gi



limits:



cpu: 2000m



memory: 10Gi



kspm:



mappedHostPaths:



- /boot



- /etc



- /proc/sys/kernel



- /sys/fs



- /sys/kernel/security/apparmor



- /usr/lib/systemd/system



- /var/lib



logMonitoring: {}



telemetryIngest:



protocols:



- jaeger



- otlp



- statsd



- zipkin



serviceName: telemetry-ingest
```

## Prerequisites

* Dynatrace Operator version 1.11.0+
* An existing two-DynaKube setup with one DynaKube using `capabilities: [kubernetes-monitoring]` and another using `capabilities: [routing]`
* `kubectl` CLI access to the cluster

## Migrate to a single DynaKube

Migration order matters

Do not create a new DynaKube resource while your existing DynaKubes are still running. Dynatrace Operator rejects a DynaKube that conflicts with another one over OneAgent node assignment, namespace injection, or telemetry ingest service names.

Always add `spec.kubernetesMonitoring` to the DynaKube that configures your routing ActiveGate and OneAgent monitoring first, then delete the dedicated Kubernetes monitoring DynaKube.

1. Edit the DynaKube that does not have the `kubernetes-monitoring` capability and add `spec.kubernetesMonitoring`.

   Transfer the `spec.activeGate` settings from your Kubernetes monitoring DynaKube into `spec.kubernetesMonitoring`, and move over any other top-level sections (such as `spec.kspm`). Most `spec.activeGate` fields map directly: `image`, `imagePullPolicy`, `nodeSelector`, `tolerations`, `env`, `labels`, `annotations`, `customProperties`, and `group`.

   If you use [`spec.kspm`](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), `spec.kubernetesMonitoring` must have `registration` configured, and `replicas` cannot exceed `1`. Dynatrace Operator rejects higher values when KSPM is configured.

   ```
   spec:



   activeGate:



   capabilities:



   - routing       # your existing capabilities stay unchanged



   kubernetesMonitoring:



   replicas: 1



   registration: {}



   resources:



   requests:



   cpu: 1000m



   memory: 10Gi



   limits:



   cpu: 2000m



   memory: 10Gi
   ```

   With `spec.kubernetesMonitoring`, cluster registration is not configured automatically. Add `registration: {}` to keep your cluster registered in Dynatrace. The DynaKube name change does not create a duplicate cluster. Dynatrace identifies your cluster independently of the DynaKube name.

   If you set a custom cluster name using the `automatic-kubernetes-api-monitoring-cluster-name` [feature flag annotation](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes."), move that value to `kubernetesMonitoring.registration.clusterName`. Dynatrace Operator does not migrate annotation values automatically.

   For all available `spec.kubernetesMonitoring` parameters, see [DynaKube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
2. Apply the updated DynaKube:

   ```
   kubectl apply -f dynakube.yaml
   ```
3. Wait for the new Kubernetes monitoring StatefulSet to become ready before deleting the old DynaKube. The two StatefulSets overlap briefly, which is expected. Deleting the old DynaKube early causes a monitoring gap.

   ```
   kubectl rollout status statefulset/<dynakube-name>-kubemon -n dynatrace
   ```

   Check the `KubernetesMonitoringAvailable` condition on your DynaKube:

   ```
   kubectl get dynakube <dynakube-name> -n dynatrace \



   -o jsonpath='{.status.conditions[?(@.type=="KubernetesMonitoringAvailable")].status}'
   ```

   The condition returns `True` when all Kubernetes monitoring resources are ready. While it reconciles, it returns `False` with reason `Reconciling`. On failure, it returns `False` with reason `Error`.
4. Delete the Kubernetes monitoring DynaKube:

   ```
   kubectl delete dynakube <k8s-monitoring-dynakube-name> -n dynatrace
   ```

## Verify the migration

Confirm the new StatefulSet is present and the old one is gone:

```
kubectl get statefulsets -n dynatrace
```

A StatefulSet named `<dynakube-name>-kubemon` appears. No StatefulSet from the deleted DynaKube remains.

In the Dynatrace UI, go to **Infrastructure** > **Kubernetes** to confirm your cluster is visible and receiving data. The existing cluster entity and its data are preserved. No duplicate cluster is created.

## Next steps

* Review all available `spec.kubernetesMonitoring` parameters in [DynaKube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").
* To monitor cluster security posture, see [Security Posture Management](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").