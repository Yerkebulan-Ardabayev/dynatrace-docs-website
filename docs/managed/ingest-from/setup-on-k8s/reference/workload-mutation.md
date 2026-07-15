---
title: Dynatrace pod mutations for application workloads
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/workload-mutation
---

# Dynatrace pod mutations for application workloads

# Dynatrace pod mutations for application workloads

* 3-min read
* Updated on Dec 04, 2025

When you enable metadata enrichment or OneAgent for application pods, Dynatrace Operator uses a webhook to intercept workload creation events and applies mutations to the resulting pods. These mutations modify the pod specification to enable monitoring capabilities.

## Common components

Starting with Operator v1.7, the injection mechanisms have been unified to improve efficiency by reducing volume mounts and moving away from environment variables in favor of an improved init-container approach.

### `annotations`

These `annotations` are relevant for all types of Dynatrace webhook injections.

| Name | Example Values | Description |
| --- | --- | --- |
| `dynakube.dynatrace.com/injected` | `true` | Indicates that the webhook has processed the pod and either injected it or skipped injection |
| `dynakube.dynatrace.com/reason` | `"NoBootstrapperConfig"` | Only present when `dynakube.dynatrace.com/injected: false`, provides additional information about why injection was skipped |

Possible values for `dynakube.dynatrace.com/reason`:

* `NoBootstrapperConfig`: Dynatrace Operator needs to provide configuration to every monitored namespace through secrets called `dynatrace-bootstrapper-config` and `dynatrace-bootstrapper-certs`. If the application is scheduled before these secrets are created, the webhook must skip injection.
* `NoMutationNeeded`: [There are several ways users can opt a pod out of injection in an otherwise monitored namespace.](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods") For such pods, this value is set as the `reason` for no injection.

### `volumes`

These `volumes` are relevant for all types of Dynatrace Webhook injections.

| `name` | `type` |
| --- | --- |
| `dynatrace-input` | `projected` with `dynatrace-bootstrapper-config`(required `Secret`) and `dynatrace-bootstrapper-certs`(optional `Secret`) |
| `dynatrace-config` | `emptyDir` |

The `dynatrace-input` volume is used exclusively by the injected init-container and contains:

* Configuration necessary for the injection within the `dynatrace-bootstrapper-config` secret
* Necessary certificates within the `dynatrace-bootstrapper-certs` secret

  + The exact content of the secrets depends on what is configured in the `DynaKube`
  + A `projected` volume is used to avoid hitting the size limit of secrets when users provide a large number of certificates

The `dynatrace-config` volume contains all the necessary configuration for the injection after setup by the init-container.

### `volumeMounts`

Every user container, independent of injection type, will have this volume mount.

| `mountPath` | `name` | `subPath` |
| --- | --- | --- |
| `/var/lib/dynatrace` | `dynatrace-config` | `<container-name>` |

The `dynatrace-config` volume, after setup by the init-container, contains all the necessary file-based configurations to enable monitoring capabilities. The OneAgent also uses this volume for storage.

#### `volumeMounts` in `split-mounts` mode

Starting with Operator version 1.8.0, an optional annotation `dynatrace.com/split-mounts` can be applied to a pod to enable `split-mounts` mode.

| Name | Example Values | Description |
| --- | --- | --- |
| `dynatrace.com/split-mounts` | `true` | allows to inject into Dynatrace workloads (like ActiveGate) |

There are four mount paths used when `split-mounts` mode is enabled instead of `/var/lib/dynatrace`. This prevents conflicts between Dynatrace application images and injected `/var/lib/dynatrace` volumeMount.

In case of ActiveGate `/var/lib/dynatrace/gateway/config_template`, the subdirectory becomes inaccessible when `/var/lib/dynatrace` mount path is used.

| `mountPath` | `name` | `subPath` |
| --- | --- | --- |
| `/var/lib/dynatrace/oneagent` | `dynatrace-config` | `<container-name>/oneagent` |
| `/var/lib/dynatrace/enrichment/dt_metadata.json` | `dynatrace-config` | `<container-name>/enrichment/dt_metadata.json` |
| `/var/lib/dynatrace/enrichment/dt_metadata.properties` | `dynatrace-config` | `<container-name>/enrichment/dt_metadata.properties` |
| `/var/lib/dynatrace/enrichment/endpoint` | `dynatrace-config` | `<container-name>/enrichment/endpoint` |

The `split-mounts` mode is always enabled for ActiveGates that are managed by Dynatrace Operator.

### `initContainers`

An init container named `dynatrace-operator` is added to enrich the container with metadata and/or inject the OneAgent.

* Uses pod and cluster configuration (including pod name, UID, and cluster ID) as part of its config.
* Uses a default security context, or copies the securityContext of the Pod.
* Uses resource limits depending on the type of injection:

  + (standalone) Metadata: defaults are set
  + OneAgent: can be configured in the `DynaKube`, otherwise

    - without CSI: no defaults
    - with CSI: defaults are set

Example YAML

This example shows both OneAgent injection and metadata enrichment enabled:

```
initContainers:



- args:



- bootstrap



- --config-directory=/mnt/config



- --input-directory=/mnt/input



- --source=/opt/dynatrace/oneagent



- --target=/mnt/bin



- --install-path=/opt/dynatrace/oneagent-paas



- --technology=php



- --attribute=k8s.workload.kind=deployment



- --attribute=k8s.workload.name=csi-scenario



- --attribute=k8s.namespace.annotation.operator-demo=example



- --attribute=prop=example



- --metadata-enrichment



- --attribute-container={"container_image.registry":"docker.io","container_image.repository":"php","container_image.tags":"fpm-stretch","k8s.container.name":"app"}



- --attribute=k8s.pod.uid=$(K8S_PODUID)



- --attribute=k8s.node.name=$(K8S_NODE_NAME)



- --attribute=k8s.namespace.name=demo



- --attribute=k8s.cluster.uid=84793b4d-9046-45f9-99da-cf3595cc4440



- --attribute=k8s.cluster.name=zib50933zib50933zib50933zib50933zib5093



- --attribute=dt.entity.kubernetes_cluster=KUBERNETES_CLUSTER-D3946527FEB7CAAF



- --attribute=k8s.pod.name=$(K8S_PODNAME)



env:



- name: K8S_PODNAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.name



- name: K8S_PODUID



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.uid



- name: K8S_NODE_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: spec.nodeName



image: public.ecr.aws/dynatrace/dynatrace-operator:v1.7.2



imagePullPolicy: IfNotPresent



name: dynatrace-operator



resources: {}



securityContext:



allowPrivilegeEscalation: false



capabilities:



drop:



- ALL



privileged: false



readOnlyRootFilesystem: true



runAsGroup: 1001



runAsNonRoot: true



runAsUser: 1001



terminationMessagePath: /dev/termination-log



terminationMessagePolicy: File



volumeMounts:



- mountPath: /mnt/bin



name: oneagent-bin



readOnly: true



- mountPath: /mnt/config



name: dynatrace-config



- mountPath: /mnt/input



name: dynatrace-input



readOnly: true



- mountPath: /var/run/secrets/kubernetes.io/serviceaccount



name: kube-api-access-jtkxm



readOnly: true
```

## Workload mutation in OneAgent injection mode

In OneAgent injection mode, the mutations focus on enabling full-stack monitoring capabilities. This mode injects the OneAgent into your application pods to provide comprehensive application monitoring and deep visibility.

OneAgent injection specific arguments for the init-container

* `--source=/opt/dynatrace/oneagent`: (Only relevant for [node-image-pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.")) Source path for copying OneAgent binaries
* `--target=/mnt/bin`: Destination path for copying OneAgent binaries
* `--install-path=/opt/dynatrace/oneagent-paas`: Installation path where OneAgent binaries will be mounted in the user container (used for configuring the `ld.so.preload` file)
* `--technology=...`: (Only relevant for [node-image-pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") or when init-container downloads OneAgent) Specifies the OneAgent type to download/copy for reducing binary size (configured via pod or DynaKube annotations)
* `--flavor=...`: (Only relevant when init-container downloads OneAgent) Specifies the OneAgent flavor to download/copy for reducing binary size (configured via pod annotations)

### `annotations`

| Name | Example Values |
| --- | --- |
| `oneagent.dynatrace.com/injected` | `true` |

### `env`

| Name | Example Values | Description |
| --- | --- | --- |
| `DT_DEPLOYMENT_METADATA` | `orchestration_tech=Operator-cloud_native_fullstack;script_version=snapshot;orchestrator_id=b9c38fb3-6c0f-45f6-8c25-9eb3b4b5af2a` | Contains deployment metadata for OneAgent |
| `LD_PRELOAD` | `/opt/dynatrace/oneagent-paas/agent/lib64/liboneagentproc.so` | Preloads the OneAgent library for monitoring |

### `volumes`

These `volumes` are relevant for the OneAgent injection.

| `name` | `type` | Description |
| --- | --- | --- |
| `oneagent-bin` | `csi` or `emptyDir` | Contains OneAgent binaries |

The `csi` mount uses the `csi.oneagent.dynatrace.com` driver and is always read-only.

### `volumeMounts`

These `volumeMounts` are relevant for the OneAgent injection.

| `mountPath` | `name` | `subPath` | `readOnly` | Description |
| --- | --- | --- | --- | --- |
| `/opt/dynatrace/oneagent-paas` | `oneagent-bin` |  | `true` | OneAgent installation directory |
| `/etc/ld.so.preload` | `dynatrace-config` | `oneagent/ld.so.preload` | `false` | Library preload configuration |

## Pod mutation for metadata enrichment

Starting with Dynatrace Operator version 1.9.0, the `metadataEnrichment` feature is automatically enabled for namespaces with OneAgent injection, even if the `enabled` parameter in `.spec.metadataEnrichment` is set to `false`.

These metadata enrichment–specific mutations are therefore applied to pods in namespaces with OneAgent injection, even without explicitly enabling `metadataEnrichment` in the `DynaKube`. Explicitly disabling metadata enrichment on the pod level via the `metadata-enrichment.dynatrace.com/inject: false` annotation will also have no effect.

In metadata-enrichment mode, Dynatrace Operator enhances pods with additional metadata.

Metadata enrichment–specific arguments for the init-container

* `--metadata-enrichment`: Instructs the init-container to perform metadata enrichment
* `--attribute=k8s.workload.kind=...`: The webhook determines this by following the `OwnerReferences` of the pod
* `--attribute=k8s.workload.name=...`: The webhook determines this by following the `OwnerReferences` of the pod
* `--attribute=...`: Metadata propagated from the annotations of the pod's namespace appears as attributes

### `annotations`

| Name | Example Values |
| --- | --- |
| `metadata.dynatrace.com/k8s.workload.kind` | `deployment` |
| `metadata.dynatrace.com/k8s.workload.name` | `example-app` |
| `metadata-enrichment.dynatrace.com/injected` | `true` |

## Pod mutation for OneAgent injection with node-image-pull

In OneAgent injection mode with [node-image-pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download."), the Dynatrace Operator combines full-stack monitoring with metadata enrichment capabilities.

### `initContainers`

The key difference from other injection modes is that the `image` of the init-container is **not** the same as the `image` of the Operator/Webhook. Instead, it uses the `codeModulesImage` defined in the `DynaKube`.

Example YAML

Due to not using the `image` of the Operator/Webhook, the `bootstrap` argument is not present in the init-container, as it is not needed.

```
initContainers:



- args:



- --config-directory=/mnt/config



- --input-directory=/mnt/input



- --suppress-error



- --attribute-container={"container_image.registry":"registry.k8s.io","container_image.repository":"ingress-nginx/controller","container_image.tags":"v1.12.1","container_image.digest":"sha256:d2fbc4ec70d8aa2050dd91a91506e998765



e86c96f32cffb56c503c9c34eed5b","k8s.container.name":"controller"}



- --source=/opt/dynatrace/oneagent



- --target=/mnt/bin



- --install-path=/opt/dynatrace/oneagent-paas



- --fullstack



- --tenant=zib50933



- --technology=nginx



- --attribute=k8s.pod.uid=$(K8S_PODUID)



- --attribute=k8s.workload.name=ingress-nginx-controller



- --attribute=k8s.cluster.uid=84793b4d-9046-45f9-99da-cf3595cc4440



- --attribute=k8s.cluster.name=example



- --attribute=dt.entity.kubernetes_cluster=KUBERNETES_CLUSTER-D3946527FEB7CAAF



- --attribute=k8s.pod.name=$(K8S_PODNAME)



- --attribute=k8s.node.name=$(K8S_NODE_NAME)



- --attribute=k8s.namespace.name=ingress-nginx



- --attribute=k8s.workload.kind=deployment



env:



- name: K8S_PODNAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.name



- name: K8S_PODUID



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: metadata.uid



- name: K8S_NODE_NAME



valueFrom:



fieldRef:



apiVersion: v1



fieldPath: spec.nodeName



image: public.ecr.aws/dynatrace/dynatrace-codemodules:1.315.62.20250613-075406



imagePullPolicy: IfNotPresent



name: dynatrace-operator



resources: {}



securityContext:



allowPrivilegeEscalation: false



capabilities:



drop:



- ALL



privileged: false



readOnlyRootFilesystem: true



runAsGroup: 1001



runAsNonRoot: true



runAsUser: 1001



terminationMessagePath: /dev/termination-log



terminationMessagePolicy: File



volumeMounts:



- mountPath: /mnt/bin



name: oneagent-bin



- mountPath: /mnt/config



name: dynatrace-config



- mountPath: /mnt/input



name: dynatrace-input



readOnly: true



- mountPath: /var/run/secrets/kubernetes.io/serviceaccount



name: kube-api-access-p5css



readOnly: true
```