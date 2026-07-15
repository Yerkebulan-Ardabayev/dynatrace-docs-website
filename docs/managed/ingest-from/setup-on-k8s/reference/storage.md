---
title: Storage requirements
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/storage
---

# Storage requirements

# Storage requirements

* 5-min read
* Updated on Jan 02, 2026

This guide describes how the different storage volumes are used by Dynatrace Operator.

## Overview

The following table shows the storage requirements of Dynatrace Operator deployment modes.

| Deployment type | CSI driver disabled | CSI driver enabled |
| --- | --- | --- |
| `classicFullStack` | 2 GB for OneAgent configuration and binaries on the node root filesystem | N/A |
| `hostMonitoring` | 2 GB for OneAgent configuration and binaries on the node root filesystem | 2 GB for OneAgent configuration and binaries in the kubelet root directory |
| `applicationMonitoring` | 1 GB per monitored pod from local ephemeral storage (for example, kubelet root directory) | 1 GB per tenant and running OneAgent version in the kubelet root directory  0.1 GB per injected pod from local ephemeral storage (for example, kubelet root directory) |
| `cloudNativeFullStack` | Combination of `hostMonitoring` and `applicationMonitoring` | Combination of `hostMonitoring` and `applicationMonitoring` |

## CSI driver volumes

The `kubelet` root directory is the central storage location for all directories required by the CSI driver. Allocate approximately 30 GB for the `kubelet` directory to cover all Dynatrace-related storage requirements.

These numbers should be increased for volatile environments and can be decreased for environments with disk space monitoring.

### Host volumes

Depending on your setup, the `kubelet` root directory might not be located in `/var/lib/kubelet`.

| **Volume name** | **Path on the host** | **Permissions** | **Purpose** | **Sizing recommendation** |
| --- | --- | --- | --- | --- |
| `mountpoint-dir` | `/var/lib/kubelet/pods` | Read-write necessary | Stores node information | N/A |
| `registration-dir` | `/var/lib/kubelet/plugins_registry` | Read-write necessary | Contains the CSI driver "registration" socket. This socket allows the registrar to use it to register the CSI driver. | 10 MB |
| `plugin-dir`, `data-dir` | `/var/lib/kubelet/plugins/csi.oneagent.dynatrace.com` | Read-write necessary | Stores all files required for the CSI driver's operation. | See [plugin directory directory disk usage](#operator-csi-plugin-dir) for all factors that influence storage consumption. |

#### Plugin directory disk usage

Contains the CSI driver components and enables `kubelet` to interact with the driver for operations like health checks.

Storage usage depends on your environment:

* Number of pods on the node
* Number of different code module versions
* Number of DynaKubes

If OneAgent is monitoring the host additional storage is consumed.

| Component | Disk usage | Notes |
| --- | --- | --- |
| OneAgent | 5 GB | Essential for OneAgent functionality. |
| Code Modules | see table below [1](#fn-1-1-def) |  |
| Runtime logs | 0.1-1 GB per pod | Logs and data generated at runtime. |
| Configuration | 20 MB per pod |  |

1

Disk usage per version is depending on the architecture. Without CSI driver the listed amount of storage is consumed per pod.

| Architecture | Disk usage |
| --- | --- |
| amd64 | 1.2 GB |
| arm64 | 800 MB |
| s390x | 500 MB |
| ppc64le | 500 MB |

## Extension Execution Controller volumes

Allows the Extension Execution Controller to store configuration, runtime data, logs, and secrets required for executing extensions.

| **Volume name** | **Volume Type** | **Mount path** | **Purpose** |
| --- | --- | --- | --- |
| `agent-runtime` | `PersistentVolumeClaim` | `/var/lib/dynatrace/remotepluginmodule/agent/runtime` | Persistent volume for storing extension runtime data and state.  By default, the persistent storage size is 1 GB. You can configure this value in the `.spec.templates.extensionExecutionController.persistentVolumeClaim` field of your Dynakube resource.  Look at [Dynakube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extension-execution-controller-template "List the available parameters for setting up Dynatrace Operator on Kubernetes.") for more information. |
| `runtime-configuration` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/agent/conf` | Ephemeral volume used for storing extension configuration. |
| `log` | `emptyDir` | `/var/lib/dynatrace/remotepluginmodule/log` | Ephemeral volume for storing extension logs. |

## SQL Extension Executor volumes

Allows the SQL Extension Executor to store temporary files (for example, certificates).

| **Volume name** | **Volume Type** | **Host path** | **Purpose** |
| --- | --- | --- | --- |
| `tmp-data` | `emptyDir` | `/tmp` | Ephemeral volume used for storing app data. |

## OneAgent volumes

Allows the OneAgent to persist its configuration.

| **Volume name** | **Volume Type** | **Host path** | **Purpose** |
| --- | --- | --- | --- |
| `volume-storage` | `hostPath` | `/var/opt/dynatrace` (default) [1](#fn-2-1-def) | Without CSI driver configuration is written directly to the host filesystem. |
| `volume-storage` | `csi` | `/var/lib/kubelet/plugins/plugins/csi.oneagent.dynatrace.com` | With CSI driver no configuration is written to an ephemeral volume, instead [plugin directory](#operator-csi-plugin-dir) on the host is used to persist OneAgent configuration. |

1

Configurable using `storageHostPath` field in the Dynakube. See [Dynakube parameters](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") for more information.

## Application pod volumes

These directories are specific to Dynatrace. They are injected into workloads by the [Webhook](#webhook) and don't require user management or configuration.

| **Volume name** | **Volume type** | **Purpose** | **Sizing recommendation** |
| --- | --- | --- | --- |
| `oneagent-bin` | `emptyDir` | Stores the OneAgent binary and logs. | An `emptyDir` is only used if CSI driver is not installed. [1](#fn-3-1-def)  Note: you can configure `emptyDir` volume size limit by annotating your workloads using  `volume.dynatrace.com/oneagent-bin: 1500Mi`. |
| `oneagent-bin` | `csi` | Stores the OneAgent binary and logs. | Used if CSI driver is installed. [1](#fn-3-1-def) |
| `dynatrace-config` | `emptyDir` | Stores configuration data and logs for the OneAgent, including custom CAs. Stores configuration data for metadata enrichment (`dt_metadata`). | Dynatrace Operator version 1.7.0+  You can configure `emptyDir` volume size limit by annotating your workloads using  `volume.dynatrace.com/dynatrace-config: <size>` [2](#fn-3-2-def).  The Operator puts `~5Mb` (mainly affected by how many certs the user has) of config files into the `dynatrace-config`, the rest is managed by the CodeModule according to [file aging mechanism](/managed/ingest-from/dynatrace-oneagent/oneagent-aging-mechanism "Learn how OneAgent deletes old files to minimize disk space usage."). All the certs provided will be replicated for each container, so they will be present in the `dynatrace-config` X times. (X is the number of injected containers in the pod). Example: if we have a Pod with 3 containers `<size>` would be 3Gi, because 3GB (~2.8Gi) according to the file aging docs and 3x5Mi=15Mi for certs/config and rounding to a nice number. |

1

Same disk usage as described in [plugin directory disk usage](#operator-csi-plugin-dir). You can save storage by configuring the [node image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.") feature.

2

More details about the format of `<size>` can be found in the [Kubernetes documentation﻿](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#meaning-of-memory).

## Ephemeral volumes

Overview of the volume size limits for ephemeral volumes of the Dynatrace Operator components and which Helm switches can be used to configure them.

### Ephemeral volume size limits

| Component | Container(s) | Volume name | Mount point | Helm value | Size limit default |
| --- | --- | --- | --- | --- | --- |
| dynatrace-webhook | webhook | certs-dir | `/tmp/k8s-webhook-server/serving-certs` | `webhook.volumes.certsDir.sizeLimit` | 10 Mi |

### Ephemeral storage limits

There are no default values for ephemeral storage resource configuration. They can be configured using the Helm switches shown in the following table:

| Component | Container(s) | Helm value |
| --- | --- | --- |
| dynatrace-operator | operator | `operator.requests.ephemeral-storage`  `operator.limits.ephemeral-storage` |
| dynatrace-webhook | webhook | `webhook.requests.ephemeral-storage`  `webhook.limits.ephemeral-storage` |
| dynatrace-csi-driver | init | `csidriver.csiInit.resources.requests.ephemeral-storage`  `csidriver.csiInit.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | provisioner | `csidriver.provisioner.resources.requests.ephemeral-storage`  `csidriver.provisioner.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | server | `csidriver.server.resources.requests.ephemeral-storage`  `csidriver.server.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | registrar | `csidriver.registrar.resources.requests.ephemeral-storage`  `csidriver.registrar.resources.limits.ephemeral-storage` |
| dynatrace-csi-driver | livenessprobe | `csidriver.livenessprobe.resources.requests.ephemeral-storage`  `csidriver.livenessprobe.resources.limits.ephemeral-storage` |
| codemodule-download-<hash> | codemodule-download | `csidriver.job.resources.requests.ephemeral-storage`  `csidriver.job.resources.limits.ephemeral-storage` |

The Helm switches can be used in a custom [`values.yaml`﻿](https://dt-url.net/helm-values) file to control the limits during Operator install with the Helm chart.