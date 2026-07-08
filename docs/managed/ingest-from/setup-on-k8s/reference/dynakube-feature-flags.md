---
title: DynaKube feature flags for Dynatrace Operator
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags
---

# DynaKube feature flags for Dynatrace Operator

# DynaKube feature flags for Dynatrace Operator

* 7-min read
* Updated on Mar 19, 2026

This page provides a list of feature flags that can be used to configure Dynatrace Operator on Kubernetes. Feature flags are used to enable or disable specific features.

## Set a feature flag

To set a feature flag.

1. Open the YAML file for your DynaKube custom resource (for example, `dynakube.yaml`).
2. In the metadata section, find or add the `annotations` field.
3. Under `annotations`, add the feature flag you want to set in the format `flag: value`.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/<flag>: <value>
   ```
4. Save your changes and apply the updated YAML file by executing `kubectl apply -f <file-name>.yaml`.

## Feature flags

| Feature flag | Default value | Data type | Description | Minimum Dynatrace Operator version |
| --- | --- | --- | --- | --- |
| `feature.dynatrace.com/label-version-detection` | `"false"` | boolean | Enables or disables build label propagation, providing build and version metadata information to the injected OneAgent about the newly deployed Pods. | 0.10.0 |
| `feature.dynatrace.com/automatic-injection` | `"true"` | boolean | Disables or enables automatic injection for namespaces that are monitored by this DynaKube. Dynatrace Operator can be set to monitor namespaces without injecting into any Pods, so you can choose which Pods to monitor. Pods that should be injected have to be annotated with `oneagent.dynatrace.com/inject: "true"`, `metadata-enrichment.dynatrace.com/inject: "true"`, or `otlp-exporter-configuration.dynatrace.com/inject: "true"` (depending on which features will be used). | 0.8.0 |
| `feature.dynatrace.com/no-proxy` | `""` | string | List of URLs to be excluded from the proxy configuration. Applies to all core components of the Dynatrace Operator and to the following components that are managed by Dynatrace Operator: OneAgent, OneAgent Log Module, ActiveGate, OpenTelemetry Collector. Use a comma-separated list of hostnames (for example, `host1,host2`). Hostname can also be specified using CIDR notation (for example, `1.2.3.0/24`). ActiveGate older than 1.335 requires a wildcard notation (for example, `1.2.3.*`). Use both notations if needed (for example, `1.2.3.0/24,1.2.3.*`). | 0.11.0 |
| `feature.dynatrace.com/injection-failure-policy` | `"silent"` | string | The failure policy determines what should happen when OneAgent injection fails for a particular Pod in a Kubernetes cluster. By default, the failure policy is set to silent. You can override the failure policy for all injected Pods that match the DynaKube.  * `silent`–if OneAgent injection fails for a particular Pod, the Pod will continue to run without monitoring. * `fail`–if OneAgent injection fails for a particular Pod, the Pod will not start, and the injection failure will be treated as an error. | 0.11.0 |
| `feature.dynatrace.com/init-container-seccomp-profile` | `"false"` | boolean | Enables or disables the adding of a default seccomp-profile to the Dynatrace init-container. The seccomp (secure computing mode) profile determines the system calls that a process in the initContainer can make. By default, the seccomp profile is not set. If enabled the `Runtime/default` seccomp profile added, see [Enable seccomp profile for Dynatrace init containers](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/security-configurations/seccomp#init-container "Overview of seccomp profile configuration for Dynatrace components."). | 0.11.2 |
| `feature.dynatrace.com/activegate-updates` | `"true"` | boolean | Configures auto updates for the ActiveGate Pods. | 0.3.0 |
| `feature.dynatrace.com/activegate-apparmor` | `"false"` | boolean | Sets AppArmor annotation on the ActiveGate Pod to `Runtime/Default`. | 0.7.0 |
| `feature.dynatrace.com/automatic-kubernetes-api-monitoring` | `"true"` | boolean | Connects a containerized ActiveGate to a local Kubernetes API endpoint. | 0.6.0 |
| `feature.dynatrace.com/automatic-kubernetes-api-monitoring-cluster-name` | `<your-dynakube>` | string | Specifies the name the Kubernetes cluster is identified by in Dynatrace. | 0.7.0 |
| `feature.dynatrace.com/oneagent-initial-connect-retry-ms` | `-1` | int | Configures the timeout in milliseconds for OneAgent for `cloudNativeFullStack` and `applicationMonitoring` to attempt to connect to the Dynatrace server. If the initial connection attempt is unsuccessful, OneAgent will wait for this specified timeout before retrying the connection. | 0.7.0 |
| `feature.dynatrace.com/max-csi-mount-attempts` | `10` | int | Defines the maximum number of attempts for the Dynatrace Operator CSI driver to mount a volume. If this limit is reached, the Pod will start with a dummy volume, which will result in missing out on deep monitoring data. | 0.9.0 |
| `feature.dynatrace.com/oneagent-privileged` | `false` | boolean | Configures OneAgent (and Log Agent if configured) container to run privileged. | 1.0.0 |
| `feature.dynatrace.com/max-csi-mount-timeout` | `10m` (10 minutes) | string | Defines the maximum timeout for the Dynatrace CSI driver to mount a volume. If this timeout is exceeded, the pod will start with a dummy volume and without being monitored. | 1.5.0 |
| `feature.dynatrace.com/automatic-tls-certificate` | `"true"` | boolean | Configures the Dynatrace Operator to manage the TLS certificate for the in-cluster ActiveGate and distribute it to components that communicate with it. Requires ActiveGate version 1.307+. | 1.5.0 |
| `feature.dynatrace.com/node-image-pull` | `"false"` | boolean | Configures the [node image pull feature](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull"). | 1.5.0 |
| `oneagent.dynatrace.com/technologies` | `""` | string | Known issue Due to a known issue, please refrain from using this feature flag. See [Dynatrace Operator version 1.5.1 release notes](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "Release notes for Dynatrace Operator, version 1.5.1") for details.  Can be applied to an application pod or your DynaKube to configure which Dynatrace code module technologies are provided. See our [node image pull feature guide](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull#configure-dynakube "Configure node image pull") for more information. | 1.5.0 |

## Deprecated feature flags

A list of feature flags that have been deprecated in the latest versions of Dynatrace Operator.

If the **Last Dynatrace Operator version** for a feature flag has passed, the flag has been officially removed and should no longer be used.

| Feature flag | Default value | Data type | Description | Minimum Dynatrace Operator version | Last Dynatrace Operator version |
| --- | --- | --- | --- | --- | --- |
| `feature.dynatrace.com/oneagent-readonly-host-fs` | `"true"` | boolean | Controls read-only mode for OneAgents in `cloudNativeFullStack` or `hostMonitoring` with CSI driver configurations. | 1.2.2 | 1.3.2 |
| `feature.dynatrace.com/activegate-readonly-fs` | `"true"` | boolean | Changes the securityContext on the ActiveGate Pod to enforce a readonly filesystem. | 0.6.0 | 0.15.0 |
| `feature.dynatrace.com/dynatrace-api-request-threshold` | `"15"` | string | The minimum time in minutest between requests from the Dynatrace Operator, which was previously hard coded to 15 minutes in order to reduce network load. The specified interval is counted independently for each of these request types. | 0.11.0 | 1.1.1 |
| `feature.dynatrace.com/oneagent-seccomp-profile` | `""` | string | Enables or disables the adding of a default seccomp-profile to the Dynatrace OneAgent. The seccomp (secure computing mode) profile determines the system calls that a process in the initContainer can make. By default, the seccomp profile is not set.  If enabled a custom seccomp profile is used, which needs to be added to the Cluster. | 0.11.0 | 1.1.1 |
| `feature.dynatrace.com/metadata-enrichment` | `"true"` | boolean | Configures the metadata-enrichment feature within the Dynatrace Operator. This feature enriches the metrics collected by the Dynatrace OneAgent with additional context, such as the host or process group instance from which the metrics were collected. | 0.8.0 | 1.1.1 |
| `feature.dynatrace.com/activegate-ignore-proxy` | `"false"` | boolean | Prevents propagation of the proxy setting from the DynaKube to the ActiveGate Pod. | 0.6.0 | 1.3.0 |
| `feature.dynatrace.com/oneagent-ignore-proxy` | `"false"` | boolean | Prevents propagation of the proxy setting from the DynaKube to the OneAgents. | 0.6.0 | 1.3.0 |
| `feature.dynatrace.com/injection-readonly-volume` | `"false"` | boolean | Configures the CSI volumes as read-only, when injected by the webhook. | 0.12.0 | 1.6.0 |
| `feature.dynatrace.com/oneagent-max-unavailable` | `1` | int | Sets the maximum number of unavailable OneAgent Pods during an update, equivalent to `UpdateStrategy.RollingUpdate.MaxUnavailable` in `DaemonSet`. | 0.6.0 | 1.10.0 |