---
title: DynaKube parameters for Dynatrace Operator
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/reference/dynakube-parameters
scraped: 2026-02-23T21:32:47.975133
---

# DynaKube parameters for Dynatrace Operator

# DynaKube parameters for Dynatrace Operator

* Latest Dynatrace
* 57-min read
* Updated on Feb 12, 2026

This page will help you to understand and configure the DynaKube [Kubernetes Custom Resourceï»¿](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/), enabling you to optimize your Dynatrace Operator setup according to your specific requirements.

The table below specifies the required Dynatrace Operator versions corresponding to each DynaKube API version.

| DynaKube API version | Minimum Dynatrace Operator version | Maximum Dynatrace Operator version [1](#fn-1-1-def) |
| --- | --- | --- |
| `v1beta6` | 1.8 |  |
| `v1beta5` | 1.6 |  |
| `v1beta4` | 1.5 |  |
| `v1beta3` | 1.4 | 1.7 |
| `v1beta2` | 1.2 | 1.6 |
| `v1beta1` | All versions | 1.6 |

1

The corresponding DynaKube API versions will be removed from the Dynatrace Operator in the subsequent minor or major release.

See the DynaKube YAML samples on [GitHubï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.5.0/assets/samples/dynakube).

v1beta6

v1beta5

v1beta4

v1beta3

v1beta2

v1beta1

Dynatrace Operator version 1.8.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified in an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-2-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-2-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `terminationGracePeriodSeconds` | Configures the terminationGracePeriodSeconds parameter of the ActiveGate pod. Kubernetes defaults and rules apply. | Not applicable | int |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |
| `volumeClaimTemplate` | Describes the common attributes of storage devices and allows a Source for provider-specific attributes. | Not applicable | corev1.PersistentVolumeClaimSpec |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `prometheus` | Enables prometheus extension. | Not applicable |  |
| `databases` | List of database extensions. | Not applicable | [[]DatabaseSpec](#extensions-databases) |

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.extensions.databases`

Available with a future Dynatrace version.

* All parameters besides `id` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `id` | Unique Kubernetes object name. | Not applicable | string |
| `replicas` | Number of SQL Extension Executor replicas. | 1 | int32 |
| `volumes` | Volumes for file-based authentication. | Not applicable | []Volume |
| `volumeMounts` | Volume mounts for file-based authentication. | Not applicable | []VolumeMount |
| `serviceAccountName` | ServiceAccount for IAM-based authentication. | Not applicable | string |
| `labels` | SQL Extension Executor labels. | Not applicable | []Label |
| `annotations` | SQL Extension Executor annotations. | Not applicable | []Annotation |
| `affinity` | SQL Extension Executor affinities. | Not applicable | []Affinity |
| `resources` | SQL Extension Executor resources. | Not applicable | ResourcesSpec |
| `nodeSelector` | SQL Extension Executor node selector. | Not applicable | NodeSelectorSpec |
| `topologySpreadConstraints` | SQL Extension Executor topology spread constraints. | Not applicable | TopologySpreadConstraints |

On OpenShift, using volumes of type `hostPath` is prohibited by default SCC and will cause failures. If `hostPath` is required, create a role with sufficient privileges and bind it to the respective service account. In this example, the created role is bound to a service account named `custom-sql-extension-executor-sa`:

```
apiVersion: v1



kind: ServiceAccount



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-sa



namespace: dynatrace



---



apiVersion: rbac.authorization.k8s.io/v1



kind: Role



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-role



namespace: dynatrace



rules:



- apiGroups:



- ""



resources:



- pods



verbs:



- list



- apiGroups:



- security.openshift.io



resourceNames:



- nonroot-v2



resources:



- securitycontextconstraints



verbs:



- use



---



kind: RoleBinding



metadata:



labels:



app.kubernetes.io/component: dynatrace-sql-extension-executor



app.kubernetes.io/name: dynatrace-operator



name: custom-sql-extension-executor-rolebinding



namespace: dynatrace



roleRef:



apiGroup: rbac.authorization.k8s.io



kind: Role



name: custom-sql-extension-executor-role



subjects:



- kind: ServiceAccount



name: custom-sql-extension-executor-sa



namespace: dynatrace



---



kind: Dynakube



spec:



extensions:



databases:



- id: my-sql-db



serviceAccountName: custom-sql-extension-executor-sa
```

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.kspm` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Specifies the host paths that are mounted to the NCC container. | Not applicable | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring:

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator version 1.6.0+

Enable additional [telemetry ingest endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest using 3rd-party protocols. Adding this section deploys the Dynatrace Collector workload to the cluster.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `protocols` | Specifies the protocols that will be ingested by the Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Specifies the name of the service to be used. If not specified the serviceName is set to a default. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret containing a TLS certificate used by telemetryIngest. | Not applicable | string |

## `.spec.otlpExporterConfiguration`

Dynatrace Operator version 1.8.0+

Enable automatic [OTLP exporter configuration](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.") for application pods that are already instrumented with OpenTelemetry SDK.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `signals` | The OpenTelemetry signals that will be automatically ingested into Dynatrace. | Not applicable | [signalConfiguration](#otlp-exporter-signals) |
| `namespaceSelector` | The namespaces where OTLP exporter configuration will be injected. For more information, see [Configure monitoring for namespaces and pods](/docs/ingest-from/setup-on-k8s/guides#annotate "Detailed description of installation and configuration options for specific use-cases") | Not applicable | LabelSelector |
| `overrideEnvVars` | Enable overriding of existing configuration environment variables of the OTLP exporter. | false | boolean |

## `.spec.otlpExporterConfiguration.signals`

Dynatrace Operator version 1.8.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `logs` | Enables the automatic OTLP exporter configuration for logs. See [endpoint urls for otlphttpï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | - | object |
| `metrics` | Enables the automatic OTLP exporter configuration for metrics. See [endpoint urls for otlphttpï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp). | - | object |
| `traces` | Enables the automatic OTLP exporter configuration for traces. See [endpoint urls for otlphttpï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp) | - | object |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Node Configuration Collector image. | Not applicable | string |
| `tag` | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `tolerations` | Set tolerations for the LogMonitoring pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring init container. | Not applicable | []string |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified, a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Labels applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller pod. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | Not applicable | string |
| `tag` | Tag for Dynatrace Collector image. | Not applicable | string |

## `.spec.templates.sqlExtensionExecutor`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for SQL Extension Executor. | Not applicable | [imageRef](#extensions-sql-extension-executor-image-ref) |
| `tolerations` | Tolerations for SQL Extension Executor pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |

## `.spec.templates.sqlExtensionExecutor.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of SQL Extension Executor image. | Not applicable | string |
| `tag` | Tag for SQL Extension Executor image. | Not applicable | string |

Dynatrace Operator version 1.6.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified in an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-3-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-3-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `terminationGracePeriodSeconds` | Configures the terminationGracePeriodSeconds parameter of the ActiveGate pod. Kubernetes defaults and rules apply. | Not applicable | int |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |
| `volumeClaimTemplate` | Describes the common attributes of storage devices and allows a Source for provider-specific attributes. | Not applicable | corev1.PersistentVolumeClaimSpec |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

Adding this section enables extension support in Kubernetes. To use extensions

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.kspm` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `mappedHostPaths` | Specifies the host paths that are mounted to the NCC container. | Not applicable | [[]string](#kspm-mappedHostPaths) |

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator version 1.6.0+

Enable Dynatrace [telemetry endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") in Kubernetes for cluster-local data ingest. Adding this section deploys the Dynatrace Collector by Dynatrace Operator.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `protocols` | Specifies the protocols that will be ingested by the Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Specifies the name of the service to be used. If not specified the serviceName is set to a default. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret containing a TLS certificate used by telemetryIngest. | Not applicable | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Node Configuration Collector image. | Not applicable | string |
| `tag` | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `tolerations` | Set tolerations for the LogMonitoring pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring init container. | Not applicable | []string |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified, a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Labels applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller pod. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Tag for Dynatrace Collector image. | `latest` | string |

Dynatrace Operator version 1.5.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified in an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/v1.5.0/assets/samples/dynakube). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `storageHostPath` | Writeable directory on the host filesystem where OneAgent configurations will be stored. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-4-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-4-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `terminationGracePeriodSeconds` | Configures the terminationGracePeriodSeconds parameter of the ActiveGate pod. Kubernetes defaults and rules apply. | Not applicable | int |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |
| `persistentVolumeClaim` | Describes the common attributes of storage devices and allows a Source for provider-specific attributes. | Not applicable | corev1.PersistentVolumeClaimSpec |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

Adding this section enables extension support in Kubernetes. To use extensions

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.telemetryIngest`

Dynatrace Operator version 1.6.0+

Adding this section deploys the Dynatrace Collector by the Operator.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `protocols` | Specifies the protocols that will be ingested by the Dynatrace Collector. | "otlp, jaeger, statsd, zipkin" | []string |
| `serviceName` | Specifies the name of the service to be used. If not specified the serviceName is set to a default. | "*dynakube.name*-telemetry-ingest" | string |
| `tlsRefName` | Secret containing a TLS certificate used by telemetryIngest. | Not applicable | string |

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Node Configuration Collector image. | Not applicable | string |
| `tag` | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring Pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring Pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring Pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring Pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring Pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `tolerations` | Set tolerations for the LogMonitoring Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring init container. | Not applicable | []string |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Lables applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller Pod. | Not applicable | []corev1.TopologySpreadConstraint |
| `useEphemeralVolume` | Indicates whether to use ephemeral volume for storage. | Not applicable | boolean |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Dynatrace Operator version 1.6.0+

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector Pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Dynatrace Operator version 1.6.0+

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Tag for Dynatrace Collector image. | `latest` | string |

Dynatrace Operator version 1.4.0+

## `.spec`

* `apiUrl` parameter is Required and immutable. Once set, it cannot be modified on an existing DynaKube.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-5-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-5-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `false` by default. | `false` | boolean |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.extensions`

Available with a future Dynatrace version.

Adding this section enables extension support in Kubernetes. To use extensions

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.kspm`

Adding this section enables [Kubernetes Security Posture Management (KSPM)](/docs/ingest-from/setup-on-k8s/deployment/security-posture-management "Configure and enable Security Posture Management in Kubernetes."). To use KSPM

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities` and
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.

## `.spec.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

To use Log Monitoring

* `kubernetes-monitoring` is mandatory and has to be added to the [list of ActiveGate capabilities](#active-gate) in `.spec.activeGate.capabilities`
* The feature flag `feature.dynatrace.com/automatic-kubernetes-api-monitoring` must not be set to `false`.
* All parameters in `.spec.logMonitoring` are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `ingestRuleMatchers` | Specifies the rules and conditions for matching ingest attributes. | Not applicable | [[]IngestRuleMatchers](#log-monitoring-ingest-rule-matchers) |

### `.spec.logMonitoring.ingestRuleMatchers`

This field is immutable. Once set, it will no longer be updated.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `attribute` | Specifies the attribute name for matching ingest rules. | Not applicable | string |
| `values` | Lists the values that the `attribute` must match for an ingest rule to apply. | Not applicable | []string |

#### Example:

```
ingestRuleMatchers:



- attribute: "k8s.namespace.name"



values:



- "kube-system"



- "dynatrace"



- "default"



- attribute: "k8s.pod.annotation"



values:



- "logs.dynatrace.com/ingest=true"



- "category=security"
```

## `.spec.templates`

## `.spec.templates.kspmNodeConfigurationCollector`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `updateStrategy` | Define the Node Configuration Collector daemonSet updateStrategy | Not applicable | DaemonSetUpdateStrategy |
| `labels` | Add custom labels to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `annotations` | Add custom annotations to the Node Configuration Collector Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the Node Configuration Collector Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image. | Not applicable | [imageRef](#kspm-image-ref) |
| `priorityClassName` | If specified, indicates the Pod's priority. Name must be defined by creating a PriorityClass object wiht that name. If not specified the setting will be removed from the DaemonSet. | Not applicable | string |
| `resources` | Define resource requests and limits for Node Configuration Collector Pods. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the Node Configuration Collector | Not applicable | NodeAffinity |
| `tolerations` | Set tolerations for the Node Configuration Collector Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the Node Configuration Collector main container. | Not applicable | []string |
| `env` | Set additional environment variables for the Node Configuration Collector main container. | Not applicable | []string |

## `.spec.templates.kspmNodeConfigurationCollector.imageRef`

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| repository | URL of Node Configuration Collector image. | Not applicable | string |
| tag | Tag for Node Configuration Collector image. | Not applicable | string |

## `.spec.templates.logMonitoring`

Available with Dynatrace version 1.306 and OneAgent 1.305

* `imageRef` parameter is Required.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom annotations to the LogMonitoring Pods. | Not applicable | map[string]string |
| `labels` | Add custom labels to the LogMonitoring Pods. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes the LogMonitoring Pods will be deployed. | Not applicable | map[string]string |
| `imageRef` | Overrides the default image for the LogMonitoring Pods. | Not applicable | [imageRef](#log-monitoring-image-ref) |
| `dnsPolicy` | Set the DNS policy for LogMonitoring Pods. | `ClusterFirst` | string |
| `priorityClassName` | Assign a priority class to the LogMonitoring Pods. By default, no class is set. | Not applicable | string |
| `secCompProfile` | Configures a SecComp profile to enable secure computing mode for the LogMonitoring Pods. | Not applicable | string |
| `resources` | Define resource requests and limits for LogMonitoring's main and init-container. | Not applicable | ResourceRequirements |
| `nodeAffinity` | Define the nodeAffinity for the DaemonSet of the NodeConfigurationCollector | Not applicable | corev1.NodeAffinity |
| `tolerations` | Set tolerations for the LogMonitoring Pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `args` | Set additional arguments for the LogMonitoring init container. | Not applicable | []string |
| `updateStrategy` | Define the NodeConfigurationCollector daemonSet updateStrategy. | Not applicable | appsv1.DaemonSetUpdateStrategy |

## `.spec.templates.logMonitoring.imageRef`

Available with Dynatrace version 1.306 and OneAgent 1.305

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of LogMonitoring image. | Not applicable | string |
| `tag` | Tag for LogMonitoring image. | Not applicable | string |

## `.spec.templates.extensionExecutionController`

Available with a future Dynatrace version.

* `imageRef` parameter is Required.
* All other parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Extension Execution Controller. This field is mandatory. | Not applicable | [imageRef](#extension-controller-image-ref) |
| `persistentVolumeClaim` | PVC for the Extension Execution Controller. If not specified a default PVC is used. | Not applicable | PersistentVolumeClaim |
| `labels` | Lables applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Extension Execution Controller Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate for communication between Extension Execution Controller and Dynatrace Collector. | Not applicable | string |
| `customConfig` | ConfigMap holding a custom Extension Execution Controller configuration. | Not applicable | string |
| `customExtensionCertificates` | Secret holding certificates that have been used to sign custom extensions. Needed for extensions signature validation by Extension Execution Controller. | Not applicable | string |
| `resources` | Resource settings for Extension Execution Controller Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Extension Execution Controller Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Extension Execution Controller Pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.extensionExecutionController.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Extension Execution Controller image. | Not applicable | string |
| `tag` | Tag for Extension Execution Controller image. | Not applicable | string |

## `.spec.templates.otelCollector`

Available with a future Dynatrace version.

* All parameters are Optional.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `imageRef` | Image that is used for Dynatrace Collector. | Not applicable | [imageRef](#extensions-collector-image-ref) |
| `replicas` | Number of Dynatrace Collector replicas. | 1 | int32 |
| `labels` | Labels applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `annotations` | Annotations applied to Dynatrace Collector Pod. | Not applicable | map[string]string |
| `tlsRefName` | Secret containing a TLS certificate used by Dynatrace Collector to verify connections to endpoints of other components. | Not applicable | string |
| `resources` | Resource settings for Dynatrace Collector Pod. | Not applicable | ResourceRequirements |
| `tolerations` | Tolerations for Dynatrace Collector Pod. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Topology spread constraints for Dynatrace Collector Pod. | Not applicable | []corev1.TopologySpreadConstraint |

## `.spec.templates.otelCollector.imageRef`

Available with a future Dynatrace version.

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `repository` | URL of Dynatrace Collector image. | `public.ecr.aws/dynatrace/dynatrace-otel-collector` | string |
| `tag` | Tag for Dynatrace Collector image. | `latest` | string |

Dynatrace Operator version 1.2.0 - 1.6.0

Deprecation notice

DynaKube API version `v1beta2` is no longer available with Dynatrace Operator version 1.7.0+.

## `.spec`

* `apiUrl` parameter is Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.") | - | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | - | string |
| `dynatraceApiRequestThreshold` | Minimum minutes between Dynatrace API requests. | 15 | integer |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | - | boolean |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | - | string |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | - | DynaKubeProxy |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | - | boolean |
| `tokens` | Name of the secret holding the tokens used for connecting to Dynatrace. | - | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. The key to the data must be `certs`. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | - | string |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | - | LabelSelector |
| `useCSIDriver` | Set if you want to use the CSIDriver. Don't enable it if you do not have access to Kubernetes nodes or if you lack privileges. | `false` | boolean |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `secCompProfile` | The SecComp Profile that will be configured in order to run in secure computing mode. | - | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-6-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-6-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.

## `.spec.metadataEnrichment`

* All parameters are Optional.

See [Configure enrichment directory](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") for additional information

| Parameter | Description | Default value | Data type |
| --- | --- | --- | --- |
| `enabled` | Enables MetadataEnrichment, `true` by default. | `true` | boolean |

DynaKube API version `v1beta1` is no longer available with Dynatrace Operator version 1.6.0+.
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | ![Not applicable](https://dt-cdn.net/images/icon-red-cross-1f1142a5dc.svg "Not applicable") | LabelSelector |

Dynatrace Operator version <=1.6.0

Deprecation notice

DynaKube API version `v1beta1` is no longer available with Dynatrace Operator version 1.7.0+.

## `.spec`

* `apiUrl` parameter is Required.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `apiUrl` | Dynatrace `apiUrl`, including the `/api` path at the end. - For SaaS, set `YOUR_ENVIRONMENT_ID` to your environment ID. - For Managed, change the `apiUrl` address. For instructions on how to determine the environment ID and how to configure the apiUrl address, see [Environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments."). | Not applicable | string |
| `tokens` | Name of the secret holding the tokens. | Name of custom resource (`.metadata.name`) if unset | string |
| `skipCertCheck` | Disable certificate check for the connection between Dynatrace Operator and the Dynatrace Cluster. Set to `true` if you want to skip certification validation checks. | `false` | boolean |
| `proxy` | Set custom proxy settings either directly or from a secret with the field `proxy`. Applies to Dynatrace Operator, ActiveGate, and OneAgents. | Not applicable | string |
| `trustedCAs` | Adds custom RootCAs from a configmap. Put the certificate under `certs` within your configmap. This applies to Dynatrace Operator, OneAgent, and ActiveGate. | Not applicable | string |
| `networkZone` | Sets a network zone for the OneAgent and ActiveGate Pods. | Not applicable | string |
| `customPullSecret` | Defines a custom pull secret in case you use a private registry when pulling images from the Dynatrace environment. Note: For the [node image pull feature](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull") without the CSI driver, you must manually ensure that pull secrets are available on the injected pod. See [node image pull prerequisites](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#prerequisites "Configure node image pull") for more details. To define a custom pull secret and learn about the expected behavior, see [Configure `customPullSecret`](/docs/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#create-pull-secret "Use a private registry"). | Not applicable | string |
| `enableIstio` | When enabled, and if Istio is installed on the Kubernetes environment, Dynatrace Operator will create the corresponding VirtualService and ServiceEntry objects to allow access to the Dynatrace Cluster from the OneAgent or ActiveGate. Disabled by default. | `false` | boolean |
| `namespaceSelector` | Applicable only for `applicationMonitoring` or `cloudNativeFullStack` configuration types. The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.oneAgent`

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |

## `.spec.oneAgent.cloudNativeFullStack`

* All parameters are Optional.

Recommended

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `version` | The OneAgent version to be used for host monitoring OneAgents running in the dedicated Pod. This setting doesn't affect the OneAgent version used for application monitoring. | The latest version is used by default. | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.oneAgent.classicFullStack`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |
| `image` | Use a custom OneAgent Docker image. Defaults to the image from the Dynatrace cluster. | Name of the image. | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |

## `.spec.oneAgent.applicationMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `codeModulesImage` | The OneAgent image that is used to inject into Pods | Not applicable | string |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |
| `useCSIDriver` | Set if you want to use the CSI driver. Don't enable it if you do not have access to Kubernetes nodes or if you lack privileges. | `false` | boolean |
| `initResources` | Define resources requests and limits for the initContainer. For details, see [Managing resources for containersï»¿](https://dt-url.net/atc371q). | Not applicable | ResourceRequirements |
| `hostGroup` | Specify the name of the group to which you want to assign the host. This method is preferred over the now obsolete `--set-host-group` argument. If both settings are used, this field takes precedence over the `--set-host-group` argument. | Not applicable | string |
| `namespaceSelector` | The namespaces where you want Dynatrace Operator to inject. For more information, see [Configure monitoring for namespaces and Pods](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate "Configure monitoring for namespaces and pods"). | Not applicable | LabelSelector |

## `.spec.oneAgent.hostMonitoring`

* All parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `version` | The OneAgent version to be used. | The latest version is used by default. | string |
| `image` | Use a custom OneAgent Docker image. | The image from the Dynatrace cluster. | string |
| `nodeSelector` | Specify the node selector that controls on which nodes OneAgent will be deployed. | Not applicable | map[string]string |
| `priorityClassName` | Assign a priority class to the OneAgent Pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `tolerations` | Tolerations to include with the OneAgent DaemonSet. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `oneAgentResources` | Resource settings for OneAgent container. Consumption of the OneAgent heavily depends on the workload to monitor. You can use the default settings in the [CRï»¿](https://dt-url.net/dynakube-samples). `resource.requests` shows the values needed to run; `resource.limits` shows the maximum limits for the Pod. | Not applicable | ResourceRequirements |
| `autoUpdate` (**deprecated**) | Deprecated field to be removed in a future release. [Pin the OneAgent version on your tenant to configure auto-update](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/updates-and-maintenance/auto-update-components#configure-oneagent-auto-update "Configure auto-updates for components managed by Dynatrace Operator (OneAgent, ActiveGate, and EdgeConnect)."). Auto-update is disabled when the `version` or `image` fields are set. | `true` | boolean |
| `dnsPolicy` | Set the DNS Policy for OneAgent Pods. For details, see [Pods DNS Policyï»¿](https://dt-url.net/2t2375a). | `ClusterFirstWithHostNet` | string |
| `annotations` | Add custom OneAgent annotations. | Not applicable | map[string]string |
| `labels` | Your defined labels for OneAgent Pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the OneAgent Pods. | Not applicable | []EnvVar |
| `args` | Set additional arguments to the OneAgent installer. For available options, see [Linux custom installation](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux/installation/customize-oneagent-installation-on-linux "Learn how to use the Linux installer with command line parameters."). For the list of limitations, see [Limitations](/docs/ingest-from/setup-on-container-platforms/docker/set-up-dynatrace-oneagent-as-docker-container#limitations "Install and update Dynatrace OneAgent as a Docker container."). | Not applicable | []string |

## `.spec.activeGate`

* `capabilities` parameter is Required.
* `resources` and `group` parameters are Recommended.
* All other parameters are Optional.

| **Parameter** | **Description** | **Default value** | **Data type** |
| --- | --- | --- | --- |
| `capabilities` | Defines the ActiveGate pod capabilities: what functionality should be enabled. Possible values: - `routing` enables OneAgent routing. - `kubernetes-monitoring` enables Kubernetes API monitoring. - `metrics-ingest`[1](#fn-7-1-def) opens the metrics ingest endpoint on the DynaKube ActiveGate and redirects all pods to it. - `dynatrace-api`[1](#fn-7-1-def) enables calling the Dynatrace API via ActiveGate. - `debugging` enables the [Live Debugging module](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#debugging "Learn which ActiveGate properties you can configure based on your needs and requirements.") in ActiveGate. | Not applicable | string |
| `image` | Use a custom ActiveGate image. Defaults to the latest ActiveGate image from the Dynatrace cluster. | Not applicable | string |
| `replicas` | Number of replicas of ActiveGate pods. | 1 | int |
| `tolerations` | Set tolerations for the ActiveGate pods. For details, see [Taints and Tolerationsï»¿](https://dt-url.net/od03765). | Not applicable | []Toleration |
| `nodeSelector` | Specify the node selector that controls on which nodes ActiveGate will be deployed. | Not applicable | map[string]string |
| `resources` | Resource settings for ActiveGate container. Consumption of the ActiveGate heavily depends on the workload to monitor; adjust values accordingly. | Not applicable | ResourceRequirements |
| `labels` | Your defined labels for ActiveGate pods in order to structure workloads as desired. | Not applicable | map[string]string |
| `env` | Set additional environment variables for the ActiveGate pods. | Not applicable | []EnvVar |
| `group` | Set activation group for ActiveGate. See [Customize ActiveGate properties](/docs/ingest-from/dynatrace-activegate/configuration/configure-activegate#collect "Learn which ActiveGate properties you can configure based on your needs and requirements.") for details. | Not applicable | string |
| `customProperties` | Add a custom properties file by providing it as a value or by referencing it from a secret. When referencing a custom properties file from a secret, make sure that the key is named `customProperties`. See [How to add a custom properties file](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/custom-properties-file "Add a custom properties file") for details. | Not applicable | string |
| `tlsSecretName` | Name of a secret containing ActiveGate TLS certificate, key, and password. If not set, a self-signed certificate is used. For details, see [How to add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations#tls-certificate "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations."). | Not applicable | string |
| `dnsPolicy` | Set the DNS policy for ActiveGate pods. | `ClusterFirstWithHostNet` | string |
| `priorityClassName` | Assign a priority class to the ActiveGate pods. By default, no class is set. For details, see [Pod Priority and Preemptionï»¿](https://dt-url.net/n8437bl). | Not applicable | string |
| `annotations` | Add custom ActiveGate annotations. | Not applicable | map[string]string |
| `topologySpreadConstraints` | Adds [topology spread constraintsï»¿](https://dt-url.net/xc03ysw) to the ActiveGate pods. | Not applicable | []corev1.TopologySpreadConstraint |

1

A custom certificate is required for this capability. See the `tlsSecretName` parameter for details.