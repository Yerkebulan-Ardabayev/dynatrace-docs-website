---
title: Dynatrace Operator security
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/security
---

# Dynatrace Operator security

# Dynatrace Operator security

* Reference
* 16-min read
* Updated on May 20, 2026

Kubernetes observability relies on components with different purposes, default configurations, and permissions. These different components need permissions to perform and maintain operational function of Dynatrace within your cluster.

While Dynatrace permissions adhere to the principle of least privilege, make sure to secure the `dynatrace` namespace and limit access to a closed group of administrators and operators.

## Deployment permissions

Installing and upgrading Dynatrace Operator require administrative privileges. If you don't use the `cluster-admin` cluster role, ensure the deploying subject has the permissions listed in this section. The required permissions also include `patch` to support `helm upgrade` and permissions to manage `DynaKube` and `EdgeConnect` custom resources.

These permissions are required only for deploying (installing) the Operator. For the permissions required during runtime refer to [Permission list](#permission-list).

### Cluster-scoped resources

The deploying user or service account must be able to **create, update, patch, and delete** the following cluster-scoped resource types:

| Resource type | API group | Verbs | Resource names | Notes |
| --- | --- | --- | --- | --- |
| `CustomResourceDefinition` | `apiextensions.k8s.io` | `create`, `update`, `patch`, `delete` | `dynakubes.dynatrace.com`, `edgeconnects.dynatrace.com` | Required to install Dynatrace CRDs |
| `ClusterRole` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete`, `escalate`, `bind` |  | **Important:** Requires `escalate` or equivalent permissions. See [Deployer RBAC verbs](#deployment-rbac-verbs). |
| `ClusterRoleBinding` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete` |  |  |
| `MutatingWebhookConfiguration` | `admissionregistration.k8s.io` | `create`, `update`, `patch`, `delete` | `dynatrace-webhook` |  |
| `ValidatingWebhookConfiguration` | `admissionregistration.k8s.io` | `create`, `update`, `patch`, `delete` | `dynatrace-webhook` |  |
| `CSIDriver` | `storage.k8s.io` | `create`, `update`, `patch`, `delete` |  | Required for CSI driver |
| `PriorityClass` | `scheduling.k8s.io` | `create`, `update`, `patch`, `delete` |  | Required for CSI driver |
| `Namespace` | `""` | `create` |  | Required for `helm install --create-namespace` |

### Namespace-scoped resources

The deploying user or service account must be able to **create, update, patch, and delete** the following resource types in the operator namespace:

| Resource type | API group | Verbs |
| --- | --- | --- |
| `ServiceAccount` | `""` | `create`, `update`, `patch`, `delete` |
| `Role` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete` |
| `RoleBinding` | `rbac.authorization.k8s.io` | `create`, `update`, `patch`, `delete` |
| `Deployment` | `apps` | `create`, `update`, `patch`, `delete` |
| `DaemonSet` | `apps` | `create`, `update`, `patch`, `delete` |
| `Service` | `""` | `create`, `update`, `patch`, `delete` |
| `Secret` | `""` | `create`, `update`, `patch`, `delete` |
| `ConfigMap` | `""` | `create`, `update`, `patch`, `delete` |
| `PodDisruptionBudget` | `policy` | `create`, `update`, `patch`, `delete` |
| `DynaKube` | `dynatrace.com` | `create`, `update`, `patch`, `delete` |
| `EdgeConnect` | `dynatrace.com` | `create`, `update`, `patch`, `delete` |
| `Job` | `batch` | `create`, `update`, `patch`, `delete` |

For links to ClusterRole manifests for deploying Dynatrace Operator, see [Deployer RBAC verbs](#deployment-rbac-verbs).

### Platform-specific resources

Depending on the target platform, the Helm chart creates additional resources that require extra deployer permissions.

#### GKE Autopilot

On GKE Autopilot clusters, the Helm chart automatically detects the `auto.gke.io/v1/AllowlistSynchronizer` API and creates an `AllowlistSynchronizer` resource as a Helm pre-install hook. This allowlists the CSI driver, log monitoring, and CSI job workloads required by the Operator.

The deploying user or service account needs the following additional permission:

| API group | Resource | Verbs |
| --- | --- | --- |
| `auto.gke.io` | `allowlistsynchronizers` | `create`, `get`, `update`, `patch`, `delete`, `list` |

#### OpenShift

On OpenShift clusters (detected via the `security.openshift.io/v1` API or `--set platform=openshift`), the Helm chart creates additional ClusterRoles that grant `use` access to SecurityContextConstraints (`privileged`, `nonroot`, `nonroot-v2`). No additional deployer permissions are required if you use the recommended `escalate` approach described in [Deployer RBAC verbs](#deployment-rbac-verbs).

### Deployer RBAC verbs: `bind` and `escalate`

Kubernetes enforces [privilege escalation prevention﻿](https://kubernetes.io/docs/reference/access-authn-authz/rbac/#privilege-escalation-prevention-and-bootstrapping): you can't create a ClusterRole granting permissions you don't already hold, and you can't create a ClusterRoleBinding referencing a ClusterRole whose permissions you don't hold.

The Dynatrace Operator Helm chart creates several ClusterRoles (for example, reading nodes, pods, and metrics). The deployer account needs to be able to create these ClusterRoles and their bindings. There are two approaches:

The sample deployer ClusterRole manifests below include permissions to manage `DynaKube` and `EdgeConnect` custom resources. This assumes the same service account used for deploying the Operator is also used to deploy the custom resources that configure it. The samples also include platform-specific resources for GKE Autopilot and OpenShift.

These sample manifests match the permissions for the **current** Operator version. When upgrading to a new Operator version, use the manifests from the corresponding [release tag﻿](https://github.com/Dynatrace/dynatrace-operator/tags).

#### Option A: Use `escalate` and `bind`

Grant the `escalate` and `bind` verbs on RBAC resources to the deployer. This is a low-maintenance approach because the deployer's permissions don't need to be updated when the Operator's ClusterRoles change across versions.

* **`escalate`** on `clusterroles` allows creating or updating ClusterRole objects that contain permissions the deployer doesn't hold. It does **not** grant those permissions to the deployer itself—it only allows managing ClusterRole resources.
* **`bind`** on `clusterroles` and `clusterrolebindings` allows creating ClusterRoleBindings that reference ClusterRoles with permissions the deployer doesn't hold.

Granting `escalate` and `bind` disables Kubernetes privilege escalation prevention for the deployer, meaning it can create ClusterRoles with any permissions and bind them to any subject. These risks can be mitigated by using admission control policies that restrict which ClusterRoles and ClusterRoleBindings the deployer can create.

Sample deployer ClusterRole manifest (includes CSI driver, GKE Autopilot, and OpenShift permissions):

[With CSI driver﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/assets/samples/deployer/deployer-clusterrole-with-csi.yaml)

If you don't deploy the CSI driver, use [Without CSI driver﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/assets/samples/deployer/deployer-clusterrole-no-csi.yaml) instead — it omits the `CSIDriver` and `PriorityClass` permissions.

#### Option B: Expanded permissions if `escalate` or `bind` are prohibited

If your security policies prohibit the `escalate` or `bind` verbs, the deployer must already hold every permission that the Operator's runtime ClusterRoles grant. This means enumerating all Dynatrace Operator permissions in the deployer ClusterRole so that Kubernetes escalation prevention is never triggered.

The no-escalate ClusterRole directly grants all runtime permissions—secrets read/write, pods/exec, webhook mutation, DaemonSet management, and more. This makes the deployer itself a high-privilege principal with broad cluster access. Admission control is still recommended to limit what RBAC resources the deployer can create.

Sample deployer ClusterRole manifest (no escalate, includes CSI driver, GKE Autopilot, and OpenShift permissions):

[With CSI driver﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/assets/samples/deployer/deployer-clusterrole-no-escalate-with-csi.yaml)

If you don't deploy the CSI driver, use [Without CSI driver﻿](https://github.com/Dynatrace/dynatrace-operator/blob/v1.10.1/assets/samples/deployer/deployer-clusterrole-no-escalate-no-csi.yaml) instead — it omits the `CSIDriver` and `PriorityClass` permissions.

## Permission list

### Dynatrace Operator

**Purpose:** Maintains the lifecycle of Dynatrace components. Replaces OneAgent Operator.

**Default configuration:** `1-replica-per-cluster`

**RBAC objects**:

* Service Account `dynatrace-operator`
* Cluster-Role `dynatrace-operator`
* Role `dynatrace-operator`

#### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `nodes` | `""` | Get, List, Watch |  |
| `namespaces` | `""` | Get, List, Watch, Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get, Update, Delete, List | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |
| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get, Update | `dynatrace-webhook` |
| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get, Update | `dynatrace-webhook` |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get, List, Watch, Update |  |
| `edgeconnects` | `dynatrace.com` | Get, List, Watch, Update |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `edgeconnects/finalizers` | `dynatrace.com` | Update |  |
| `dynakubes/status` | `dynatrace.com` | Update |  |
| `edgeconnects/status` | `dynatrace.com` | Update |  |
| `statefulsets` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `daemonsets` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `replicasets` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `deployments` | `apps` | Get, List, Watch, Create, Update, Delete |  |
| `deployments/finalizers` | `apps` | Update |  |
| `configmaps` | `""` | Get, List, Watch, Create, Update, Delete |  |
| `pods` | `""` | Get, List, Watch |  |
| `secrets` | `""` | Get, List, Watch, Create, Update, Delete |  |
| `events` | `""` | Create, Get, List, Patch |  |
| `services` | `""` | Create, Update, Delete, Get, List, Watch |  |
| `serviceentries` | `networking.istio.io` | Get, List, Create, Update, Delete |  |
| `virtualservices` | `networking.istio.io` | Get, List, Create, Update, Delete |  |
| `leases` | `coordination.k8s.io` | Get, Update, Create |  |

### Dynatrace Operator Webhook Server

**Purposes**:

* Modifies pod definitions to include Dynatrace code modules for application observability
* Validates DynaKube custom resources
* Handles the DynaKube conversion between versions

**Default configuration**: `1-replica-per-cluster`, can be scaled

**RBAC objects**:

* Service Account `dynatrace-webhook`
* Cluster-Role `dynatrace-webhook`
* Role `dynatrace-webhook`

#### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get, List, Watch, Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get, List, Watch, Update | ``` dynatrace-dynakube-config``dynatrace-bootstrapper-config``dynatrace-bootstrapper-certs``dynatrace-metadata-enrichment-endpoint``dynatrace-otlp-exporter-config``dynatrace-otlp-exporter-certs ``` |
| `replicationcontrollers` | `""` | Get |  |
| `replicasets` | `apps` | Get |  |
| `statefulsets` | `apps` | Get |  |
| `daemonsets` | `apps` | Get |  |
| `deployments` | `apps` | Get |  |
| `jobs` | `batch` | Get |  |
| `cronjobs` | `batch` | Get |  |
| `deploymentconfigs` | `apps.openshift.io` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `events` | `""` | Create, Patch |  |
| `secrets` | `""` | Get, List, Watch |  |
| `configmaps` | `""` | Get, List, Watch |  |
| `dynakubes` | `dynatrace.com` | Get, List, Watch |  |

### Dynatrace Operator CSI driver

**Purpose**:

* For `applicationMonitoring` configurations, it provides the necessary OneAgent binary for application monitoring to the pods on each node.
* For `hostMonitoring` configurations, it provides a writable folder for the OneAgent configurations when a read-only host file system is used.
* For `cloudNativeFullStack`, it provides both of the above.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-oneagent-csi-driver`
* Cluster-Role `dynatrace-oneagent-csi-driver`
* Role `dynatrace-oneagent-csi-driver`

#### Cluster-wide permission

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get, List, Watch |  |
| `secrets` | `""` | Get, List, Watch |  |
| `configmaps` | `""` | Get, List, Watch |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `jobs` | `batch` | Get, List, Create, Delete, Watch |  |
| `events` | `""` | Create, Patch |  |

### ActiveGate

#### Kubernetes Platform Monitoring

**Purpose**: collects cluster and workload metrics, events, and status from the Kubernetes API.

**Default configuration**: `1-replica-per-cluster`, can be scaled

**RBAC objects**:

* Service Account: `dynatrace-kubernetes`
* ClusterRole: `dynatrace-kubernetes-monitoring`

In Dynatrace Operator version 1.8, `dynatrace-kubernetes-monitoring` was an aggregated ClusterRole. For details, see [ClusterRole aggregation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").

##### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `nodes` | `""` | List, Watch, Get |  |
| `pods` | `""` | List, Watch, Get |  |
| `namespaces` | `""` | List, Watch, Get |  |
| `replicationcontrollers` | `""` | List, Watch, Get |  |
| `events` | `""` | List, Watch, Get |  |
| `resourcequotas` | `""` | List, Watch, Get |  |
| `pods/proxy` | `""` | List, Watch, Get |  |
| `nodes/proxy` | `""` | List, Watch, Get |  |
| `nodes/metrics` | `""` | List, Watch, Get |  |
| `services` | `""` | List, Watch, Get |  |
| `persistentvolumeclaims` | `""` | List, Watch, Get |  |
| `persistentvolumes` | `""` | List, Watch, Get |  |
| `jobs` | `batch` | List, Watch, Get |  |
| `cronjobs` | `batch` | List, Watch, Get |  |
| `deployments` | `apps` | List, Watch, Get |  |
| `replicasets` | `apps` | List, Watch, Get |  |
| `statefulsets` | `apps` | List, Watch, Get |  |
| `daemonsets` | `apps` | List, Watch, Get |  |
| `deploymentconfigs` | `apps.openshift.io` | List, Watch, Get |  |
| `clusterversions` | `config.openshift.io` | List, Watch, Get |  |
| `dynakubes` | `dynatrace.com` | List, Watch, Get |  |
| `edgeconnects` | `dynatrace.com` | List, Watch, Get |  |
| `customresourcedefinitions` | `apiextensions.k8s.io` | List, Watch, Get |  |
| `ingresses` | `networking.k8s.io` | List, Watch, Get |  |
| `networkpolicies` | `networking.k8s.io` | List, Watch, Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | ``` privileged``nonroot-v2 ``` |

#### Dynatrace Kubernetes Security Posture Management (KSPM)

**Purposes**: [Kubernetes Security Posture Management](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") detects, analyzes, and continuously watches for
misconfigurations, security hardening guidelines, and potential compliance violations in Kubernetes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-node-config-collector`
* ClusterRole: `dynatrace-kubernetes-monitoring-kspm`

In Dynatrace Operator version 1.8, `dynatrace-kubernetes-monitoring-kspm` was aggregated by the `dynatrace-kubernetes-monitoring` ClusterRole. For details, see [ClusterRole aggregation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.").

##### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get, List, Watch |  |
| `nodes` | `""` | Get, List, Watch |  |
| `pods` | `""` | Get, List, Watch |  |
| `replicationcontrollers` | `""` | Get, List, Watch |  |
| `serviceaccounts` | `""` | Get, List, Watch |  |
| `services` | `""` | Get, List, Watch |  |
| `cronjobs` | `batch` | Get, List, Watch |  |
| `jobs` | `batch` | Get, List, Watch |  |
| `daemonsets` | `apps` | Get, List, Watch |  |
| `deployments` | `apps` | Get, List, Watch |  |
| `replicasets` | `apps` | Get, List, Watch |  |
| `statefulsets` | `apps` | Get, List, Watch |  |
| `networkpolicies` | `networking.k8s.io` | Get, List, Watch |  |
| `clusterrolebindings` | `rbac.authorization.k8s.io` | Get, List, Watch |  |
| `clusterroles` | `rbac.authorization.k8s.io` | Get, List, Watch |  |
| `rolebindings` | `rbac.authorization.k8s.io` | Get, List, Watch |  |
| `roles` | `rbac.authorization.k8s.io` | Get, List, Watch |  |

### OneAgent

**Purposes**:

* Collects host metrics from Kubernetes nodes.
* Detects new containers and injects Dynatrace code modules into application pods using classic full-stack injection. Optional
* Collects container logs from Kubernetes nodes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-dynakube-oneagent`
* Cluster-Role `dynatrace-logmonitoring`

**Policy settings**: Allows **HostNetwork**, **HostPID**, to use any volume types.

**Necessary capabilities**: `CHOWN`, `DAC_OVERRIDE`, `DAC_READ_SEARCH`, `FOWNER`, `FSETID`, `KILL`, `NET_ADMIN`, `NET_RAW`, `SETFCAP`, `SETGID`, `SETUID`, `SYS_ADMIN`, `SYS_CHROOT`, `SYS_PTRACE`, `SYS_RESOURCE`

#### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `nodes/proxy` | `""` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Dynatrace Log Module

**Purposes**:

* Collects container logs from Kubernetes nodes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-logmonitoring`
* Cluster-Role `dynatrace-logmonitoring`

#### Cluster-wide permissions

Log monitoring requires [the same cluster-wide permissions as OneAgent](#oneagent-permissions).

### Dynatrace telemetry ingest

**Purposes**:

* Enable [Dynatrace telemetry endpoints](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest

  + Ingest data via [OTLP﻿](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger﻿](https://www.jaegertracing.io/), [StatsD﻿](https://github.com/statsd/statsd) or [Zipkin﻿](https://zipkin.io/) endpoints
* Analyze context-rich data with built-in apps, DQL, Notebooks and Dashboards

**RBAC objects**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-telemetry-ingest`

#### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | Get, Watch, List |  |
| `namespaces` | `""` | Get, Watch, List |  |
| `nodes` | `""` | Get, Watch, List |  |
| `replicasets` | `apps` | Get, List, Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Extensions

**Purposes**:

* Extensions extend Dynatrace analytics capabilities by ingesting data from various sources, such as third-party applications, services, and custom metrics. See [Extensions](/managed/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") for more information.

**Default configuration**:

The following components are required, regardless of which extensions are used:

* Extension Execution Controller (EEC): `1-replica-per-cluster`

**RBAC objects**:

Depending on the used extension, the following RBAC objects are required.

* Service Accounts

  + `dynatrace-extension-controller`
* ClusterRoles

  + `dynatrace-extension-controller`
* Roles

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`

##### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | List, Watch |  |
| `services` | `""` | List, Watch |  |

##### Namespace `dynatrace` permissions

*Prometheus extension*

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

*Database extension*

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Prometheus extension

**Purpose**:

* Collects metrics from Prometheus endpoints in your cluster.

**Default configuration**:

* Prometheus datasource: `replicas-set-in-dynakube` (no default, replicas set in the DynaKube)

**RBAC objects**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-extensions-prometheus`

##### Cluster-wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | Get, List, Watch |  |
| `namespaces` | `""` | Get, List, Watch |  |
| `endpoints` | `""` | Get, List, Watch |  |
| `services` | `""` | Get, List, Watch |  |
| `nodes` | `""` | Get, List, Watch |  |
| `nodes/metrics` | `""` | Get, List, Watch |  |
| `deployments` | `apps` | Get, List, Watch |  |
| `daemonsets` | `apps` | Get, List, Watch |  |
| `replicasets` | `apps` | Get, List, Watch |  |
| `statefulsets` | `apps` | Get, List, Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Database extension

**Purpose**:

* Collects metrics from database endpoints in your cluster.

**Default configuration**:

* SQL Extension Executor: `replicas-set-in-dynakube` (no default, replicas set in the DynaKube)

**RBAC objects**:

* Service Accounts

  + `dynatrace-sql-ext-exec`
* Roles

  + `dynatrace-sql-ext-exec`

##### Namespace `dynatrace` permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |

### Dynatrace Operator supportability

**Purposes**:

* Allow Dynatrace Operator to execute [the support-archive command](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components."). Necessary for troubleshooting Operator related issues.

**RBAC objects**:

* Role `dynatrace-operator-supportability`

**Opt-out**:

* You can opt out of this feature by setting the Dynatrace Operator Helm chart value `rbac.supportability` to `false`.

Disabling this feature will make it harder to provide the necessary information when opening support cases regarding Dynatrace Operator.

#### Namespace `dynatrace` permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `pods/log` | `""` | Get |  |
| `pods/exec` | `""` | Create |  |
| `jobs` | `batch` | Get, List |  |

### Dynatrace Operator API upgrade support

**Purposes**:

* Start `dynatrace-operator-crd-storage-migration` Job for automatic cleanup of removed Dynakube API versions in `pre-upgrade` Helm hook.

**RBAC objects**:

* ClusterRole `dynatrace-crd-storage-migration`
* Role `dynatrace-crd-storage-migration`
* ServiceAccount `dynatrace-crd-storage-migration`

**Opt-in**:

* You can opt-out of this feature by setting the Dynatrace Operator Helm chart value `crdStorageMigrationJob` to `false`.

#### Cluster wide permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get, Update | ``` dynakubes.dynatrace.com``edgeconnects.dynatrace.com ``` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | Verbs | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get, List, Watch, Update |  |
| `edgeconnects` | `dynatrace.com` | Get, List, Watch, Update |  |

## Security Controls of Dynatrace Operator components

The following table presents a detailed analysis of the security controls for Kubernetes components: Dynatrace Operator, Dynatrace Operator webhook, and Dynatrace Operator CSI driver. This report is based on:

* [CIS Benchmark﻿](https://dt-url.net/zd0368p), a globally recognized standard for securing Kubernetes deployments.
* [POD Security Standard policies﻿](https://dt-url.net/mp0345l).
* Best practices.

**Standards and abbreviations**:

* **CIS**: [Center for Internet Security (CIS) Kubernetes Benchmark﻿](https://dt-url.net/zd0368p).
* **PSSB**: [Pod Security Standards – Baseline profile﻿](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).
* **PSSR**: [Pod Security Standards – Restricted profile﻿](https://dt-url.net/ut4387d).

The **Standard** column references these abbreviations.

### Dynatrace Operator components

![Green background check mark](https://dt-cdn.net/images/check-16-c4e463bb22.png "Green background check mark") Satisfied  
![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Exception (see expand below)  
![Configurable](https://dt-cdn.net/images/configurable-490-8b015913d4.svg "Configurable") Planned improvement (see expand below)

| Security control | Standard | Operator | Webhook | CSI driver |
| --- | --- | --- | --- | --- |
| Disallow privileged containers[1](#fn-1-1-def) | CIS 5.2.2 / PSS Baseline | Satisfied | Satisfied | Exception |
| Disallow privilege escalation[1](#fn-1-1-def) | CIS 5.2.6 / PSS Restricted | Satisfied | Satisfied | Exception |
| Disallow containers running as root[2](#fn-1-2-def) | CIS 5.2.7 / PSS Restricted | Satisfied | Satisfied | Exception |
| Limit access to secrets (RBAC) | CIS 5.1.4 | Planned improvement | Planned improvement | Planned improvement |
| Disallow use of HostPath volumes[3](#fn-1-3-def) | CIS 5.2.12 / PSS Baseline | Satisfied | Satisfied | Exception |
| Restrict automounting of service account token[4](#fn-1-4-def) | CIS 5.1.6 | Exception | Exception | Exception |
| Disallow use of too many or insecure capabilities | CIS 5.2.8 / 5.2.9 / 5.2.10 / PSS Restricted | Satisfied | Satisfied | Satisfied |
| Disallow use of HostPorts | CIS 5.2.13 / PSS Baseline | Satisfied | Satisfied | Satisfied |
| Disallow access to host network | CIS 5.2.5 / PSS Baseline | Satisfied | Satisfied | Satisfied |
| Disallow use of host PID | CIS 5.2.3 / PSS Baseline | Satisfied | Satisfied | Satisfied |
| Disallow use of host IPC | CIS 5.2.4 / PSS Baseline | Satisfied | Satisfied | Satisfied |
| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | Satisfied |
| Require resource limits[5](#fn-1-5-def) | Best practice | Satisfied | Satisfied | Satisfied |
| Demand seccomp (at least default/runtime) | CIS 5.7.2 / PSS Restricted | Satisfied | Satisfied | Satisfied |
| Disallow secrets mounted as env variable | CIS 5.4.1 | Satisfied | Satisfied | Satisfied |
| Restrict sysctls | PSS Baseline | Satisfied | Satisfied | Satisfied |
| Restrict AppArmor | PSS Baseline | Satisfied | Satisfied | Satisfied |
| Disallow SELinux[6](#fn-1-6-def) | PSS Baseline | Satisfied | Satisfied | Exception |
| /proc mount type | PSS Baseline | Satisfied | Satisfied | Satisfied |

1

CSI driver requires elevated permissions to create and manage mounts on the host system. For more details, see [CSI driver privileges](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "Components of Dynatrace Operator").

2

CSI driver communicates with kubelet using a socket on the host, to access this socket the CSI driver needs to run as root.

3

CSI driver stores/caches the OneAgent binaries on the host's filesystem, in order to do that it needs a hostVolume mount.

4

Dynatrace Operator, Webhook, and CSI driver components need to communicate with the Kubernetes API.

5

CSI driver provisioner has no resources limits by default in order to provide the best [performance during provisioning](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "Set resource limits for Dynatrace Operator components."); limits can be set via Helm chart values.

6

CSI driver needs seLinux level s0 for the application pods to see files from the volume created by the CSI driver.

**Planned improvement**:  
Namespace-scoped Roles for the Operator, Webhook, and CSI driver currently allow access to all secrets within their namespace. Improvement planned to restrict these Roles to specific secret names, consistent with ClusterRole configuration.

### Managed components

![Green background check mark](https://dt-cdn.net/images/check-16-c4e463bb22.png "Green background check mark") Satisfied  
![Warning](https://dt-cdn.net/images/warning-16-56c09ccf83.png "Warning") Exception (see expand below)  
![Configurable](https://dt-cdn.net/images/configurable-490-8b015913d4.svg "Configurable") Planned improvement (see expand below)

| Security control | Standard | OneAgent | Extensions controller | Dynatrace Collector | ActiveGate | EdgeConnect | KSPM | OneAgent Log Module |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Disallow privileged containers[1](#fn-2-1-def) | CIS 5.2.2 / PSSB | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Exception |
| Disallow privilege escalation[2](#fn-2-2-def) | CIS 5.2.6 / PSSR | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Exception |
| Disallow containers running as root[3](#fn-2-3-def) | CIS 5.2.7 / PSSR | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Exception | Satisfied |
| Disallow use of too many or insecure capabilities[4](#fn-2-4-def) | CIS 5.2.8 / 5.2.9 / 5.2.10 / PSSR | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Exception | Exception |
| Limit access to secrets (RBAC) | CIS 5.1.4 | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow use of HostPath volumes[5](#fn-2-5-def) | CIS 5.2.12 / PSSB | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Exception | Exception |
| Disallow use of HostPorts | CIS 5.2.13 / PSSB | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow access to host network[6](#fn-2-6-def) | CIS 5.2.5 / PSSB | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow use of host PID[7](#fn-2-7-def) | CIS 5.2.3 / PSSB | Exception | Satisfied | Satisfied | Satisfied | Satisfied | Exception | Satisfied |
| Disallow use of host IPC | CIS 5.2.4 / PSSB | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Require Resource limits[10](#fn-2-10-def) | Best practice | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Planned improvement |
| Demand seccomp to be used (at least default/runtime)[8](#fn-2-8-def) | CIS 5.7.2 / PSSR | Exception | Satisfied | Satisfied | Exception | Exception | Exception | Exception |
| Disallow Secrets mounted as env variable | CIS 5.4.1 | Satisfied | Satisfied | Planned improvement | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict sysctls | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict AppArmor | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow SELinux | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict automounting of service account token[9](#fn-2-9-def) | CIS 5.1.6 | Exception | Exception | Exception | Exception | Exception | Exception | Exception |
| /proc Mount Type | PSSB | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |

1

OneAgent: OneAgent DaemonSet runs with host-level privileges for full-stack visibility (network, processes, file system).  
OneAgent Log Module: LogAgent needs to run as privileged container on OCP cluster to access its persistent storage. [OCP persistent storage using hostPath﻿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).

2

OneAgent: Required for init containers that instrument processes before startup.  
OneAgent Log Module: `AllowPrivilegeEscalation` is always true when the container is run as privileged. [Configure a Security Context for a Pod or Container﻿](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

3

OneAgent: OneAgent DaemonSet runs with host-level privileges for full-stack visibility (network, processes, file system).  
KSPM: KSPM mounts the host root filesystem `/` to perform configuration and security scans; hostPath restriction evaluation is planned.

4

OneAgent: Requires limited Linux capabilities (for example, NET\_RAW) for network observability.  
KSPM: KSPM requires specific Linux capabilities to scan and collect system configuration and security data; this is by design and cannot be removed.  
OneAgent Log Module: LogAgent needs additional capability to get access to all monitored log files.

5

OneAgent: OneAgent DaemonSet runs with host-level privileges for full-stack visibility (network, processes, file system).  
KSPM: KSPM mounts the host root filesystem `/` for node-level scanning; improvement under review to restrict mounted paths.  
OneAgent Log Module: Needs access to log files on the host's filesystem.

6

OneAgent: Uses host network namespace to monitor network traffic.

7

OneAgent: Uses host PID namespace to correlate process metrics.  
KSPM: KSPM requires host PID namespace access for the node collector to gather process-level data. This requirement will be documented.

8

OneAgent: Uses default runtime seccomp profile; explicit setting planned.  
ActiveGate: ActiveGate runs with minimal elevated privileges to manage inbound connections.  
EdgeConnect: EdgeConnect currently lacks an explicit seccomp profile; addition is planned in future releases. This control is being addressed in upcoming releases.  
KSPM: KSPM mounts the host root filesystem `/` to perform configuration and security scans; hostPath restriction evaluation is planned.  
OneAgent Log Module: The seccomp profile can be set via DynaKube in order to run in secure computing mode.

9

OneAgent, Extensions Controller, Dynatrace Collector, ActiveGate, EdgeConnect, and KSPM components need to communicate with the Kubernetes API.

10

OneAgent Log Module: The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

**Planned improvement**:  
Disallow Secrets mounted as env variable: Dynatrace Collector currently uses environment variables for tokens; migrating to secret files is planned.

## Pod security policies

These permissions used to be managed using a **PodSecurityPolicy** (PSP), but [in Kubernetes version 1.25 PSPs will be removed﻿](https://dt-url.net/2403pxy) from the following components:

* [Dynatrace Operator﻿](https://dt-url.net/d7034gj) version 0.2.2
* **LEGACY** [Dynatrace OneAgent Operator﻿](https://dt-url.net/3023pvs) version 0.11.0
* [Corresponding Helm charts﻿](https://dt-url.net/rp43pl1)

**Dynatrace Operator version 0.2.1** is the last version in which PSPs are applied by default, so it's up to you to enforce these rules. As PSP alternatives, you can use other policy enforcement tools such as:

* [k-rail﻿](https://dt-url.net/qx63p3n)
* [Kyverno﻿](https://dt-url.net/6m83ppk)
* [Gatekeeper﻿](https://dt-url.net/aha3ps4)

If you choose to use a PSP alternative, be sure to provide the necessary permissions to the Dynatrace components.

## Dynatrace Operator security context constraints

Dynatrace Operator version 0.12.0+

Starting with Dynatrace Operator version 0.12.0, the built-in creation of custom security context constraints (SCCs) has been removed for Dynatrace Operator and Dynatrace Operator–managed components. This change was made to reduce complications caused by custom SCCs in unique OpenShift setups.

Despite this update, the components maintain the same permissions and security requirements as before.

The following tables show the SCCs used in different versions of Dynatrace Operator and OpenShift.

| Resources accessed | Custom SCC used in Dynatrace Operator versions earlier than 0.12.0 | SCC in Dynatrace Operator version 0.12.0+ and OpenShift earlier than 4.11 |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `privileged`[1](#fn-3-1-def) |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `privileged`[1](#fn-3-1-def) |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

| Resources accessed | Custom SCC used in Dynatrace Operator versions earlier than 0.12.0 | SCC in Dynatrace Operator version 0.12.0+ and OpenShift 4.11+ |
| --- | --- | --- |
| Dynatrace Operator | `dynatrace-operator` | `nonroot-v2` |
| Dynatrace Operator Webhook Server | `dynatrace-webhook` | `nonroot-v2` |
| Dynatrace Operator CSI driver | `dynatrace-oneagent-csi-driver` | `privileged`[1](#fn-3-1-def) |
| ActiveGate | `dynatrace-activegate` | `nonroot-v2` |
| OneAgent | `dynatrace-dynakube-oneagent-privileged` `dynatrace-dynakube-oneagent-unprivileged` | `privileged`[1](#fn-3-1-def) |

1

This SCC is the only built-in OpenShift SCC that allows usage of seccomp, which our components have set by default, and also the usage of CSI volumes.

It is still possible to create your own more permissive or restrictive SCCs that take your specific setup into consideration. You can safely remove the old SCCs that were created by a previous Dynatrace Operator version.

To remove the old SCCs, use the following command:

```
oc delete scc <scc-name>
```