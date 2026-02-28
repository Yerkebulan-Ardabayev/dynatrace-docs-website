---
title: Dynatrace Operator security
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/security
scraped: 2026-02-28T21:32:42.028039
---

# Dynatrace Operator security

# Dynatrace Operator security

* Latest Dynatrace
* 16-min read
* Updated on Jan 16, 2026

Kubernetes observability relies on components with different purposes, default configurations, and permissions. These different components need permissions to perform and maintain operational function of Dynatrace within your cluster.

While Dynatrace permissions adhere to the principle of least privilege, make sure to secure the `dynatrace` namespace and limit access to a closed group of administrators and operators.

## Permission list

### Dynatrace Operator

**Purpose:** Maintains the lifecycle of Dynatrace components. Replaces OneAgent Operator.

**Default configuration:** `1-replica-per-cluster`

**RBAC objects**:

* Service Account `dynatrace-operator`
* Cluster-Role `dynatrace-operator`
* Role `dynatrace-operator`

#### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `nodes` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/Update/Delete/List | `dynatrace-dynakube-config` `dynatrace-bootstrapper-config` `dynatrace-bootstrapper-certs` `dynatrace-metadata-enrichment-endpoint` `dynatrace-otlp-exporter-config` `dynatrace-otlp-exporter-certs` |
| `mutatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `validatingwebhookconfigurations` | `admissionregistration.k8s.io` | Get/Update | `dynatrace-webhook` |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `edgeconnects/finalizers` | `dynatrace.com` | Update |  |
| `dynakubes/status` | `dynatrace.com` | Update |  |
| `edgeconnects/status` | `dynatrace.com` | Update |  |
| `statefulsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `daemonsets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `replicasets` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `deployments` | `apps` | Get/List/Watch/Create/Update/Delete |  |
| `deployments/finalizers` | `apps` | Update |  |
| `configmaps` | `""` | Get/List/Watch/Create/Update/Delete |  |
| `pods` | `""` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch/Create/Update/Delete |  |
| `events` | `""` | Create/Get/List/Patch |  |
| `services` | `""` | Create/Update/Delete/Get/List/Watch |  |
| `serviceentries` | `networking.istio.io` | Get/List/Create/Update/Delete |  |
| `virtualservices` | `networking.istio.io` | Get/List/Create/Update/Delete |  |
| `leases` | `coordination.k8s.io` | Get/Update/Create |  |

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

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch/Update |  |
| `secrets` | `""` | Create |  |
| `secrets` | `""` | Get/List/Watch/Update | `dynatrace-dynakube-config` `dynatrace-bootstrapper-config` `dynatrace-bootstrapper-certs` `dynatrace-metadata-enrichment-endpoint` `dynatrace-otlp-exporter-config` `dynatrace-otlp-exporter-certs` |
| `replicationcontrollers` | `""` | Get |  |
| `replicasets` | `apps` | Get |  |
| `statefulsets` | `apps` | Get |  |
| `daemonsets` | `apps` | Get |  |
| `deployments` | `apps` | Get |  |
| `jobs` | `batch` | Get |  |
| `cronjobs` | `batch` | Get |  |
| `deploymentconfigs` | `apps.openshift.io` | Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `events` | `""` | Create/Patch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `pods` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |

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

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch |  |
| `secrets` | `""` | Get/List/Watch |  |
| `configmaps` | `""` | Get/List/Watch |  |
| `dynakubes/finalizers` | `dynatrace.com` | Update |  |
| `jobs` | `batch` | Get/List/Create/Delete/Watch |  |
| `events` | `""` | Create/Patch |  |

### ActiveGate



#### Kubernetes Platform Monitoring

**Purpose**: collects cluster and workload metrics, events, and status from the Kubernetes API.

**Default configuration**: `1-replica-per-cluster`, can be scaled

**RBAC objects**:

* Service Account: `dynatrace-kubernetes`
* Cluster-Roles:

  + `dynatrace-kubernetes-monitoring`

    - Used to aggregate all ClusterRoles with the label `rbac.dynatrace.com/aggregate-to-monitoring: "true"`
  + `dynatrace-kubernetes-monitoring-default`

    - Aggregated by `dynatrace-kubernetes-monitoring`, more details can be found in the [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.")

##### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `nodes` | `""` | List/Watch/Get |  |
| `pods` | `""` | List/Watch/Get |  |
| `namespaces` | `""` | List/Watch/Get |  |
| `replicationcontrollers` | `""` | List/Watch/Get |  |
| `events` | `""` | List/Watch/Get |  |
| `resourcequotas` | `""` | List/Watch/Get |  |
| `pods/proxy` | `""` | List/Watch/Get |  |
| `nodes/proxy` | `""` | List/Watch/Get |  |
| `nodes/metrics` | `""` | List/Watch/Get |  |
| `services` | `""` | List/Watch/Get |  |
| `persistentvolumeclaims` | `""` | List/Watch/Get |  |
| `persistentvolumes` | `""` | List/Watch/Get |  |
| `jobs` | `batch` | List/Watch/Get |  |
| `cronjobs` | `batch` | List/Watch/Get |  |
| `deployments` | `apps` | List/Watch/Get |  |
| `replicasets` | `apps` | List/Watch/Get |  |
| `statefulsets` | `apps` | List/Watch/Get |  |
| `daemonsets` | `apps` | List/Watch/Get |  |
| `deploymentconfigs` | `apps.openshift.io` | List/Watch/Get |  |
| `clusterversions` | `config.openshift.io` | List/Watch/Get |  |
| `dynakubes` | `dynatrace.com` | List/Watch/Get |  |
| `edgeconnects` | `dynatrace.com` | List/Watch/Get |  |
| `customresourcedefinitions` | `apiextensions.k8s.io` | List/Watch/Get |  |
| `ingresses` | `networking.k8s.io` | List/Watch/Get |  |
| `networkpolicies` | `networking.k8s.io` | List/Watch/Get |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` `nonroot-v2` |

#### Dynatrace Kubernetes Security Posture Management (KSPM)

**Purposes**: [Kubernetes Security Posture Management](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes.") detects, analyzes, and continuously watches for
misconfigurations, security hardening guidelines, and potential compliance violations in Kubernetes.

**Default configuration**: `1-replica-per-node` (deployed via a DaemonSet)

**RBAC objects**:

* Service Account `dynatrace-node-config-collector`
* Cluster-Role `dynatrace-kubernetes-monitoring-kspm`

  + Aggregated by the `dynatrace-kubernetes-monitoring` ClusterRole, more details can be found in the [ClusterRole aggregation documentation](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/cluster-role-aggregation "Understanding how the Dynatrace Operator uses ClusterRole aggregation to manage permissions for Kubernetes monitoring.")

##### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `namespaces` | `""` | Get/List/Watch |  |
| `nodes` | `""` | Get/List/Watch |  |
| `pods` | `""` | Get/List/Watch |  |
| `replicationcontrollers` | `""` | Get/List/Watch |  |
| `serviceaccounts` | `""` | Get/List/Watch |  |
| `services` | `""` | Get/List/Watch |  |
| `cronjobs` | `batch` | Get/List/Watch |  |
| `jobs` | `batch` | Get/List/Watch |  |
| `daemonsets` | `apps` | Get/List/Watch |  |
| `deployments` | `apps` | Get/List/Watch |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `statefulsets` | `apps` | Get/List/Watch |  |
| `networkpolicies` | `networking.k8s.io` | Get/List/Watch |  |
| `clusterrolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `clusterroles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `rolebindings` | `rbac.authorization.k8s.io` | Get/List/Watch |  |
| `roles` | `rbac.authorization.k8s.io` | Get/List/Watch |  |

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

| Resources accessed | API group | APIs used | Resource names |
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

* Enable [Dynatrace telemetry endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest

  + Ingest data via [OTLPï»¿](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaegerï»¿](https://www.jaegertracing.io/), [StatsDï»¿](https://github.com/statsd/statsd) or [Zipkinï»¿](https://zipkin.io/) endpoints
* Analyze context-rich data with built-in apps, DQL, Notebooks and Dashboards

**RBAC objects**:

* Service Accounts

  + `dynatrace-otel-collector`
* Cluster-Roles

  + `dynatrace-telemetry-ingest`

#### Cluster-wide permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | Get/Watch/List |  |
| `namespaces` | `""` | Get/Watch/List |  |
| `nodes` | `""` | Get/Watch/List |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

### Extensions

**Purposes**:

* Extensions extend Dynatrace analytics capabilities by ingesting data from various sources, such as third-party applications, services, and custom metrics. See [Extensions](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") for more information.

**Default configuration**:

The following components are required, regardless of which extensions are used:

* Extension Execution Controller (EEC): `1-replica-per-cluster`

**RBAC objects**:

Depending on the used extension, the following RBAC objects are required.

* Service Accounts

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`
* Roles

  + `dynatrace-extension-controller-prometheus`
  + `dynatrace-extension-controller-database`

##### Namespace `dynatrace` permissions

*Prometheus extension*

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `securitycontextconstraints` | `security.openshift.io` | Use | `privileged` |

*Database extension*

| Resources accessed | API group | APIs used | Resource names |
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

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | Get/List/Watch |  |
| `namespaces` | `""` | Get/List/Watch |  |
| `endpoints` | `""` | Get/List/Watch |  |
| `services` | `""` | Get/List/Watch |  |
| `nodes` | `""` | Get/List/Watch |  |
| `nodes/metrics` | `""` | Get/List/Watch |  |
| `deployments` | `apps` | Get/List/Watch |  |
| `daemonsets` | `apps` | Get/List/Watch |  |
| `replicasets` | `apps` | Get/List/Watch |  |
| `statefulsets` | `apps` | Get/List/Watch |  |
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

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods` | `""` | List |  |

### Dynatrace Operator supportability



**Purposes**:

* Allow Dynatrace Operator to execute [the support-archive command](/docs/ingest-from/setup-on-k8s/deployment/troubleshooting#support-archive "This page will assist you in navigating any challenges you may encounter while working with the Dynatrace Operator and its various components."). Necessary for troubleshooting Operator related issues.

**RBAC objects**:

* Role `dynatrace-operator-supportability`

**Opt-out**:

* You can opt out of this feature by setting the Dynatrace Operator Helm chart value `rbac.supportability` to `false`.

Disabling this feature will make it harder to provide the necessary information when opening support cases regarding Dynatrace Operator.

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `pods/log` | `""` | Get |  |
| `pods/exec` | `""` | Create |  |
| `jobs` | `batch` | Get/List |  |

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

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `customresourcedefinitions` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `customresourcedefinitions/status` | `apiextensions.k8s.io` | Get/Update | `dynakubes.dynatrace.com` `edgeconnects.dynatrace.com` |
| `securitycontextconstraints` | `security.openshift.io` | Use | `nonroot-v2` |

#### Namespace `dynatrace` permissions

| Resources accessed | API group | APIs used | Resource names |
| --- | --- | --- | --- |
| `dynakubes` | `dynatrace.com` | Get/List/Watch/Update |  |
| `edgeconnects` | `dynatrace.com` | Get/List/Watch/Update |  |

## Security Controls of Dynatrace Operator components



The following table presents a detailed analysis of the security controls for Kubernetes components: Dynatrace Operator, Dynatrace Operator webhook, and Dynatrace Operator CSI driver. This report is based on:

* [CIS Benchmarkï»¿](https://dt-url.net/zd0368p), a globally recognized standard for securing Kubernetes deployments.
* [POD Security Standard policiesï»¿](https://dt-url.net/mp0345l).
* Best practices.

| Security Control | Standard (\*) | Operator | Webhook | CSI driver | OneAgent | Extensions Controller | Dynatrace Collector | ActiveGate | EdgeConnect | KSPM |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Disallow privileged containers | CIS [1](#fn-1-1-def) 5.2.2 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [5](#fn-1-5-def) | Required [10](#fn-1-10-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow privilege escalation | CIS [1](#fn-1-1-def) 5.2.6 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Required [5](#fn-1-5-def) | Required [11](#fn-1-11-def) | Satisfied | Required [16](#fn-1-16-def) | Satisfied | Satisfied | Satisfied |
| Disallow containers running as root | CIS [1](#fn-1-1-def) 5.2.7 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Required [6](#fn-1-6-def) | Required [10](#fn-1-10-def) | Satisfied | Required [16](#fn-1-16-def) | Required [18](#fn-1-18-def) | Satisfied | Required [19](#fn-1-19-def) |
| Disallow use of too many or insecure capabilities | CIS [1](#fn-1-1-def) 5.2.8 / 5.2.9 / 5.2.10 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Satisfied | Required [12](#fn-1-12-def) | Satisfied | Satisfied | Required [18](#fn-1-18-def) | Satisfied | Required [24](#fn-1-24-def) |
| Limit access to secrets (RBAC) | CIS [1](#fn-1-1-def) 5.1.4 | Planned improvement [22](#fn-1-22-def) | Planned improvement [22](#fn-1-22-def) | Planned improvement [22](#fn-1-22-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow use of HostPath volumes | CIS [1](#fn-1-1-def) 5.2.12 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [7](#fn-1-7-def) | Required [10](#fn-1-10-def) | Satisfied | Satisfied | Satisfied | Satisfied | Required [20](#fn-1-20-def) |
| Disallow use of HostPorts | CIS [1](#fn-1-1-def) 5.2.13 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow access to host network | CIS [1](#fn-1-1-def) 5.2.5 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Required [13](#fn-1-13-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow use of host PID | CIS [1](#fn-1-1-def) 5.2.3 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Required [14](#fn-1-14-def) | Satisfied | Satisfied | Satisfied | Satisfied | Required [23](#fn-1-23-def) |
| Disallow use of host IPC | CIS [1](#fn-1-1-def) 5.2.4 / PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Require Resource limits | Best practice | Satisfied | Satisfied | Satisfied [9](#fn-1-9-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Demand seccomp to be used (at least default/runtime) | CIS [1](#fn-1-1-def) 5.7.2 / PSSR [3](#fn-1-3-def) | Satisfied | Satisfied | Satisfied | Required [15](#fn-1-15-def) | Satisfied | Satisfied | Required [18](#fn-1-18-def) | Required [21](#fn-1-21-def) | Required [19](#fn-1-19-def) |
| Disallow Secrets mounted as env variable | CIS [1](#fn-1-1-def) 5.4.1 | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Planned improvement [17](#fn-1-17-def) | Satisfied | Satisfied | Satisfied |
| Restrict sysctls | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict AppArmor | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Disallow SELinux | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Required [8](#fn-1-8-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |
| Restrict automounting of service account token | CIS [1](#fn-1-1-def) 5.1.6 | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) | Required [4](#fn-1-4-def) |
| /proc Mount Type | PSSB [2](#fn-1-2-def) | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied | Satisfied |

**Standard**:

1

[Center for Internet Security (CIS) Kubernetes benchmarkï»¿](https://dt-url.net/zd0368p).

2

[POD Security Standards Baseline profileï»¿](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).

3

[POD Security Standards Restricted profileï»¿](https://dt-url.net/ut4387d).

**General**:

4

Component needs to communicate with the Kubernetes API.

**CSI**:

5

CSI driver requires elevated permissions to create and manage mounts on the host system. For more details, see [CSI driver privileges](/docs/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver-privileges "Components of Dynatrace Operator").

6

CSI driver communicates with kubelet using a socket on the host, to access this socket the CSI driver needs to run as root.

7

CSI driver stores/caches the OneAgent binaries on the host's filesystem, in order to do that it needs a hostVolume mount.

8

CSI driver needs seLinux level s0 for the application pods to see files from the volume created by the CSI driver.

9

CSI driver provisioner has no resources limits by default in order to provide the best [performance during provisioning](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits#customize-resource-limits "Set resource limits for Dynatrace Operator components."); limits can be set via Helm chart values.

**OneAgent**:

10

OneAgent DaemonSet runs with host-level privileges for full-stack visibility (network, processes, file system).

11

Required for init containers that instrument processes before startup.

12

Requires limited Linux capabilities (e.g., NET\_RAW) for network observability.

13

Uses host network namespace to monitor network traffic.

14

Uses host PID namespace to correlate process metrics.

15

Uses default runtime seccomp profile; explicit setting planned.

**Extension Execution Controller / Dynatrace Collector**:

16

Dynatrace Collector and Extensions controller may require root or elevated privileges for metrics collection and sidecar operations.

17

Dynatrace Collector currently uses environment variables for tokens; migrating to secret files is planned.

**ActiveGate / EdgeConnect / KSPM**:

18

ActiveGate runs with minimal elevated privileges to manage inbound connections.

19

KSPM mounts the host root filesystem `/` to perform configuration and security scans; hostPath restriction evaluation is planned.

20

KSPM mounts the entire host filesystem for node-level scanning; improvement under review to restrict mounted paths.

21

EdgeConnect currently lacks an explicit seccomp profile; addition is planned in future releases. This control is being addressed in upcoming releases.

22

Namespace-scoped Roles for the Operator, Webhook, and CSI driver currently allow access to all secrets within their namespace. Improvement planned to restrict these Roles to specific secret names, consistent with ClusterRole configuration.

23

KSPM requires host PID namespace access for the node collector to gather process-level data. This requirement will be documented.

24

KSPM requires specific Linux capabilities to scan and collect system configuration and security data; this is by design and cannot be removed.

## Security Controls of components managed by Dynatrace Operator



The following table presents a detailed analysis of the security controls for Kubernetes components managed by Dynatrace Operator: ActiveGate, [OneAgent (CloudNative)](/docs/ingest-from/setup-on-k8s/how-it-works/cloud-native-fullstack "In-depth description of full-stack observability using Dynatrace Operator."), LogAgent. This report is based on:

* [CIS Benchmarkï»¿](https://dt-url.net/zd0368p), a globally recognized standard for securing Kubernetes deployments.
* [POD Security Standard policiesï»¿](https://dt-url.net/mp0345l).
* Best practices.

| Security Control | Standard (\*) | ActiveGate | OneAgent CloudNative | OneAgent Log Module |
| --- | --- | --- | --- | --- |
| Disallow privileged containers | CIS [1](#fn-2-1-def) 5.2.2 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Required [15](#fn-2-15-def) |
| Disallow privilege escalation | CIS [1](#fn-2-1-def) 5.2.6 / PSSR [3](#fn-2-3-def) | Satisfied | Required [6](#fn-2-6-def) | Required [16](#fn-2-16-def) |
| Disallow containers running as root | CIS [1](#fn-2-1-def) 5.2.7 / PSSR [3](#fn-2-3-def) | Satisfied | Satisfied | Satisfied |
| Disallow usage of too many or insecure capabilities | CIS [1](#fn-2-1-def) 5.2.8 / 5.2.9 / 5.2.10 / PSSR [3](#fn-2-3-def) | Satisfied | Required [7](#fn-2-7-def) | Required [17](#fn-2-17-def) |
| Disallow usage of HostPath volumes | CIS [1](#fn-2-1-def) 5.2.12 / PSSB [2](#fn-2-2-def) | Satisfied | Required [8](#fn-2-8-def) | Required [18](#fn-2-18-def) |
| Disallow usage of HostPorts | CIS [1](#fn-2-1-def) 5.2.13 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Disallow access to host network | CIS [1](#fn-2-1-def) 5.2.5 / PSSB [2](#fn-2-2-def) | Satisfied | Required [9](#fn-2-9-def) | Satisfied |
| Disallow usage of host PID | CIS [1](#fn-2-1-def) 5.2.3 / PSSB [2](#fn-2-2-def) | Satisfied | Required [10](#fn-2-10-def) | Satisfied |
| Disallow usage of host IPC | CIS [1](#fn-2-1-def) 5.2.4 / PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Require readOnlyRootFilesystem | Best practice | Satisfied | Satisfied | Satisfied |
| Require Resource limits | Best practice | Configurable [5](#fn-2-5-def) | Configurable [11](#fn-2-11-def) | Configurable [19](#fn-2-19-def) |
| Demand seccomp to be used (at least default/runtime) | CIS [1](#fn-2-1-def) 5.7.2 / PSSR [3](#fn-2-3-def) | Satisfied | Required [12](#fn-2-12-def) | Required [20](#fn-2-20-def) |
| Disallow Secrets mounted as env variable | CIS [1](#fn-2-1-def) 5.4.1 | Satisfied | Satisfied | Satisfied |
| Restrict sysctls | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Restrict AppArmor | PSSB [2](#fn-2-2-def) | Satisfied | Required [13](#fn-2-13-def) | Satisfied |
| Disallow SELinux | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |
| Restrict automounting of service account token | CIS [1](#fn-2-1-def) 5.1.6 | Required [4](#fn-2-4-def) | Configurable [14](#fn-2-14-def) | Required [4](#fn-2-4-def) |
| /proc Mount Type | PSSB [2](#fn-2-2-def) | Satisfied | Satisfied | Satisfied |

**Standard**:

1

[Center for Internet Security (CIS) Kubernetes benchmarkï»¿](https://dt-url.net/zd0368p).

2

[POD Security Standards Baseline profileï»¿](https://kubernetes.io/docs/concepts/security/pod-security-standards/#baseline).

3

[POD Security Standards Restricted profileï»¿](https://dt-url.net/ut4387d).

**General**:

4

Component needs to communicate with the Kubernetes API.

**ActiveGate**

5

The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

**OneAgent**

6

Privilege escalation is needed for processes inside OneAgent container to get Linux capabilities.

7

[Monitoring actions](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/oneagent-security-linux#operation "Learn about Dynatrace OneAgent security and modifications to your Linux-based system") executed by OneAgent processes need the following [capabilities](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/linux-non-privileged#linux-system-capabilities "Find out when Dynatrace OneAgent requires root privileges on Linux.").

8

Mounted host's root filesystem is accessed by all OneAgent modules and allows for log files access, disk metrics, and other host and process monitoring capabilities.

9

OneAgent needs access to host network namespace to provide host-level and process-level network health monitoring.

10

OneAgent needs access to host process table to collect performance metrics for all processes running on the host.

11

The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

12

OneAgent needs access to kernel syscalls beyond the RuntimeDefault set for monitoring purposes.

13

OneAgent needs access to the mount command which is blocked by the default AppArmor profile.

14

OneAgent component needs to communicate with the kubelet `/pods` endpoint. The K8s token is not mounted to the Pod if LogMonitoring is turned off via Helm values.

**OneAgent Log Module**:

15

LogAgent needs to run as privileged container on OCP cluster to access its persistent storage. [OCP persistent storage using hostPathï»¿](https://docs.redhat.com/en/documentation/openshift_container_platform/4.18/html/storage/configuring-persistent-storage#persistent-storage-using-hostpath).

16

AllowPrivilegeEscalation is always true when the container is run as privileged. [Configure a Security Context for a Pod or Containerï»¿](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/).

17

LogAgent needs additional capability to get access to all monitored log files.

18

Needs access to log files on the host's filesystem.

19

The limits are highly dependent on the amount of data processed. Can be set via DynaKube.

20

The seccomp profile can be set via DynaKube in order to run in secure computing mode.

## Pod security policies

These permissions used to be managed using a **PodSecurityPolicy** (PSP), but [in Kubernetes version 1.25 PSPs will be removedï»¿](https://dt-url.net/2403pxy) from the following components:

* [Dynatrace Operatorï»¿](https://dt-url.net/d7034gj) version 0.2.2
* **LEGACY** [Dynatrace OneAgent Operatorï»¿](https://dt-url.net/3023pvs) version 0.11.0
* [Corresponding Helm chartsï»¿](https://dt-url.net/rp43pl1)

**Dynatrace Operator version 0.2.1** is the last version in which PSPs are applied by default, so it's up to you to enforce these rules. As PSP alternatives, you can use other policy enforcement tools such as:

* [k-railï»¿](https://dt-url.net/qx63p3n)
* [Kyvernoï»¿](https://dt-url.net/6m83ppk)
* [Gatekeeperï»¿](https://dt-url.net/aha3ps4)

If you choose to use a PSP alternative, be sure to provide the necessary permissions to the Dynatrace components.

## Dynatrace Operator security context constraints

Dynatrace Operator version 0.12.0+

Starting with Dynatrace Operator version 0.12.0, the built-in creation of custom security context constraints (SCCs) has been removed for Dynatrace Operator and Dynatrace Operatorâmanaged components. This change was made to reduce complications caused by custom SCCs in unique OpenShift setups.

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