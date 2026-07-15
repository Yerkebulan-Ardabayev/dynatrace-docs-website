---
title: Troubleshooting
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/deployment/troubleshooting
---

# Troubleshooting

# Troubleshooting

* 7-min read
* Updated on Jul 10, 2026

This page provides a comprehensive guide to help you diagnose and resolve common problems.

[#### Monitoring issues troubleshooting

Troubleshoot common issues that may arise when monitoring Kubernetes with Dynatrace.

Monitoring issues troubleshooting](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/monitoring-troubleshooting)[#### Connectivity issues between Dynatrace and Kubernetes cluster

Troubleshoot common connectivity issues between Dynatrace and your Kubernetes cluster.

Connectivity issues between Dynatrace and Kubernetes cluster](/managed/ingest-from/setup-on-k8s/deployment/troubleshooting/connectivity-issues)

## Initial troubleshooting steps

Before you begin with the specific troubleshooting sections, it's important to have a clear understanding of the current state of your Kubernetes cluster. The initial steps outlined below will help you gather essential information about your cluster's health and the status of its components.

1. Check the status of your DynaKube by executing the `kubectl get dynakubes -n dynatrace` command.
2. [Use the `troubleshoot` subcommand](#troubleshoot).
3. Check the status of the Dynatrace Pods  
   Use the `kubectl -n dynatrace get pods` command to check the status of the Dynatrace Operator, OneAgent or CSI driver Pods (the amount of Pods will vary depending on the selected deployment mode).
4. Inspect the logs  
   Use the `kubectl logs` command to inspect the logs of specific Pods. For example, `kubectl logs <pod-name>` will display the logs for a specific Pod.
5. Describe the resource  
   The `kubectl describe` command can provide detailed information about a specific resource. For example, `kubectl describe pod <pod-name>` will display detailed information about a specific Pod.

## General troubleshooting

General troubleshooting steps and guidance for common issues encountered when using Dynatrace with Kubernetes. It covers how to access debug logs, use the `troubleshoot` subcommand, or generate a support archive.

### Troubleshoot common Dynatrace Operator setup issues using the `troubleshoot` subcommand

Dynatrace Operator version 0.9.0+

Run the command below to retrieve a basic output on DynaKube status, such as:

* **Namespace:** If the `dynatrace` namespace exists (name can be overwritten via parameter)
* **DynaKube:**

  + If `CustomResourceDefinition` exists
  + If `CustomResource` with the given name exists (name can be overwritten via parameter)
  + If the API URL ends with `/api`
  + If the secret name is the same as DynaKube (or `.spec.tokens` if used)
  + If the secret has Dynatrace Operator and Data Ingest tokens set
  + If the secret for `customPullSecret` is defined
* **Environment:** If your environment is reachable from the Dynatrace Operator Pod using the same parameters as the Dynatrace Operator binary (such as proxy and certificate).
* **OneAgent and ActiveGate image:** If the registry is accessible; if the image is accessible from the Dynatrace Operator pod using the registry from the environment with (custom) pull secret.

```
kubectl exec deploy/dynatrace-operator -n dynatrace -- dynatrace-operator troubleshoot
```

If you use a different DynaKube name, add the `--dynakube <your_dynakube_name>` argument to the command.

Example output if there are no errors for the above-mentioned fields:

```
{"level":"info","ts":"2022-09-12T08:45:21.437Z","logger":"dynatrace-operator-version","msg":"dynatrace-operator","version":"<operator version>","gitCommit":"<commithash>","buildDate":"<release date>","goVersion":"<go version>","platform":"<platform>"}



[namespace ]     --- checking if namespace 'dynatrace' exists ...



[namespace ]      √  using namespace 'dynatrace'



[dynakube  ]     --- checking if 'dynatrace:dynakube' Dynakube is configured correctly



[dynakube  ]         CRD for Dynakube exists



[dynakube  ]         using 'dynatrace:dynakube' Dynakube



[dynakube  ]         checking if api url is valid



[dynakube  ]         api url is valid



[dynakube  ]         checking if secret is valid



[dynakube  ]         'dynatrace:dynakube' secret exists



[dynakube  ]         secret token 'apiToken' exists



[dynakube  ]         customPullSecret not used



[dynakube  ]         pull secret 'dynatrace:dynakube-pull-secret' exists



[dynakube  ]         secret token '.dockerconfigjson' exists



[dynakube  ]         proxy secret not used



[dynakube  ]      √  'dynatrace:dynakube' Dynakube is valid



[dtcluster ]     --- checking if tenant is accessible ...



[dtcluster ]      √  tenant is accessible
```

### Debug logs

By default, OneAgent logs are located in `/var/log/dynatrace/oneagent`.

To debug Dynatrace Operator issues, run

Kubernetes

OpenShift

```
kubectl -n dynatrace logs -f deployment/dynatrace-operator
```

```
oc -n dynatrace logs -f deployment/dynatrace-operator
```

You might also want to check the logs from OneAgent pods deployed through Dynatrace Operator.

Kubernetes

OpenShift

```
kubectl get pods -n dynatrace



NAME                                           READY     STATUS    RESTARTS   AGE



dynatrace-operator-64865586d4-nk5ng   1/1       Running   0          1d



dynakube-oneagent-<id>                             1/1       Running   0          22h
```

```
kubectl logs dynakube-oneagent-<id> -n dynatrace
```

```
oc get pods -n dynatrace



NAME                                           READY     STATUS    RESTARTS   AGE



dynatrace-operator-64865586d4-nk5ng            1/1       Running   0          1d



dynakube-classic-8r2kq                         1/1       Running   0          22h
```

```
oc logs oneagent-66qgb -n dynatrace
```

### Generate a support archive using the `support-archive` subcommand

Dynatrace Operator version 0.11.0+

Use `support-archive` to generate an archive of files that can be useful for support investigations:

* `kubernetes-version.txt` (Kubernetes server version of the cluster)
* `operator-version.txt` (Dynatrace Operator version information)
* `logs` (logs from all containers of the Dynatrace Operator pods and Dynatrace components deployed by the Dynatrace Operator in the Dynatrace Operator namespace, usually `dynatrace`; this also includes logs of previous containers, if available):

  + `activegate` (if [ActiveGate](/managed/ingest-from/dynatrace-activegate "Understand the basic concepts related to ActiveGate.") is deployed)
  + `dynakube-logmonitoring` (if Log Monitoring is using [Kubernetes Log Module](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."))
  + `dynatrace-oneagent` (if `cloudNativeFullStack` or `hostMonitoring` is used in [DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."))
  + `dynatrace-operator`
  + `dynatrace-webhook`
  + `dynatrace-oneagent-csi-driver` (if [CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") is deployed)

    - `liveness-probe`
    - `provisioner`
    - `registrar`
    - `server`
  + `extension-controller` (if Extensions are enabled)
  + `sql-ext-exec` (if SQL Extensions are enabled)
  + `otel-collector` (if [telemetryIngest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") is enabled)
  + `node-config-collector` (if [KSPM](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.") is enabled)
* `manifests` (Kubernetes manifests for Dynatrace Operator components and deployed DynaKubes in the Dynatrace Operator namespace)
* `troubleshoot.txt` (output of a troubleshooting command that is automatically executed by the `support-archive` subcommand)
* `supportarchive_console.log` (complete output of the `support-archive` subcommand)
* Extension Controller diagnostic files

  + all files found below `/var/lib/dynatrace/remotepluginmodule/log/extensions` inside the Extension Controller pod

#### Usage

To create a support archive, execute the following command:

```
kubectl exec -n dynatrace deployment/dynatrace-operator -- dynatrace-operator support-archive --stdout > operator-support-archive.zip
```

The contents of the support archive are written to `stdout`, allowing them to be redirected to a ZIP file. Other output is sent to `stderr` to maintain the integrity of the archive file.

Windows PowerShell not supported

Make sure to use the command prompt (`cmd.exe`) on Windows; PowerShell isn't supported.

#### Run `support-archive` in a standalone Pod

Dynatrace Operator version 1.0.0+

If the `operator` pod is not functioning due to severe startup issues, you can run the `support-archive` command in a standalone Pod using the following command. Keep in mind that running this command in a standalone pod is recommended only as a last resort.

```
kubectl run -n dynatrace support-archive --rm -i --overrides='{ "spec": { "serviceAccount": "dynatrace-operator" }  }' --restart Never --image <operator-image> -- support-archive --delay 10 --stdout > support-archive.zip
```

* Ensure that you use the same image as the `operator` pod.
* The `--delay 10` parameter is important because `kubectl run` tends to miss the first few lines of output, which could lead to corruption of the support archive.
* Specify the `serviceAccount` as `dynatrace-operator` in the command as it allows the standalone pod to access all necessary logs and Kubernetes manifests required for compiling the support archive. Note that this method relies on the Dynatrace Operator resources still being installed and available on the cluster.

#### Sample output

The following is sample output from running `support-archive` with the `--stdout` parameter.

```
kubectl exec -n dynatrace deployment/dynatrace-operator -- dynatrace-operator support-archive --stdout > operator-support-archive.zip
```

```
[support-archive]       dynatrace-operator      {"version": "v0.11.0", "gitCommit": "...", "buildDate": "...", "goVersion": "...", "platform": "linux/amd64"}



[support-archive]       Storing operator version into operator-version.txt



[support-archive]       Starting log collection



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/server.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/provisioner.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/registrar.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-bdnpc/liveness-probe.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/server.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/provisioner.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/registrar.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-cb4pc/liveness-probe.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/server.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/provisioner.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/registrar.log



[support-archive]       Successfully collected logs logs/dynatrace-oneagent-csi-driver-k8bl5/liveness-probe.log



[support-archive]       Successfully collected logs logs/dynatrace-operator-6d9fd9b9fc-sw5ll/dynatrace-operator.log



[support-archive]       Successfully collected logs logs/dynatrace-webhook-7d84599455-bfkmp/webhook.log



[support-archive]       Successfully collected logs logs/dynatrace-webhook-7d84599455-vhkrh/webhook.log



[support-archive]       Successfully collected logs logs/<dynakube name>-node-config-collector-dmg2b/node-config-collector.log



[support-archive]       Successfully collected logs logs/<dynakube name>-node-config-collector-kgscf/node-config-collector.log



[support-archive]       Successfully collected logs logs/<dynakube name>-node-config-collector-wstzt/node-config-collector.log



[support-archive]       Successfully collected logs logs/<dynakube name>-activegate-0/activegate.log



[support-archive]       Successfully collected logs logs/<dynakube name>-extension-controller-0/extension-controller.log



[support-archive]       Successfully collected logs logs/<dynakube name>-oneagent-6bhpx/dynatrace-oneagent.log



[support-archive]       Successfully collected logs logs/<dynakube name>-oneagent-9f7mm/dynatrace-oneagent.log



[support-archive]       Successfully collected logs logs/<dynakube name>-oneagent-hq4ks/dynatrace-oneagent.log



[support-archive]       Successfully collected logs logs/<dynakube name>-otel-collector-0/collector.log



[support-archive]       Successfully collected EEC diagnostic logs logs/<dynakube name>-extension-controller-0/var/lib/dynatrace/remotepluginmodule/log/extensions/ruxitagent_extensionsmodule_1.0.log



[support-archive]       Successfully collected EEC diagnostic logs logs/<dynakube name>-extension-controller-0/var/lib/dynatrace/remotepluginmodule/log/extensions/diagnostics/diag_executor.log



[support-archive]       Starting K8S object collection



[support-archive]       Collected manifest for manifests/injected_namespaces/namespace-default.yaml



[support-archive]       Collected manifest for manifests/dynatrace/namespace-dynatrace.yaml



[support-archive]       Collected manifest for manifests/dynatrace/deployment/dynatrace-operator.yaml



[support-archive]       Collected manifest for manifests/dynatrace/deployment/dynatrace-webhook.yaml



[support-archive]       Collected manifest for manifests/dynatrace/daemonset/dynatrace-oneagent-csi-driver.yaml



[support-archive]       Collected manifest for manifests/dynatrace/daemonset/<dynakube name>-node-config-collector.yaml



[support-archive]       Collected manifest for manifests/dynatrace/statefulset/<dynakube name>-activegate.yaml



[support-archive]       Collected manifest for manifests/dynatrace/statefulset/<dynakube name>-extension-controller.yaml



[support-archive]       Collected manifest for manifests/dynatrace/statefulset/<dynakube name>-otel-collector.yaml



[support-archive]       Collected manifest for manifests/dynatrace/daemonset/<dynakube name>-oneagent.yaml



[support-archive]       Collected manifest for manifests/dynatrace/dynakube/<dynakube name>.yaml



[support-archive]       Collected manifest for manifests/dynatrace/configmap/dynatrace-node-cache.yaml



[support-archive]       Collected manifest for manifests/webhook_configurations/mutatingwebhookconfiguration.yaml



[support-archive]       Collected manifest for manifests/webhook_configurations/validatingwebhookconfiguration.yaml



[support-archive]       Collected manifest for manifests/crds/customresourcedefinition-edgeconnects.yaml



[support-archive]       Collected manifest for manifests/crds/customresourcedefinition-dynakubes.yaml
```

### Debug configuration and monitoring issues using the Kubernetes Monitoring Statistics extension

The [Kubernetes Monitoring Statistics extension﻿](https://dt-url.net/n903xmb) can help you:

* Troubleshoot your Kubernetes Monitoring setup
* Troubleshoot your Prometheus integration setup
* Get detailed insights into queries from Dynatrace to the Kubernetes API
* Receive alerts when your Kubernetes platform monitoring setup experiences issues
* Get alerted on slow response times of your Kubernetes API

### Potential issues when changing the monitoring mode

* Changing the monitoring mode from `classicFullStack`to `cloudNativeFullStack` affects the host ID calculations for monitored hosts, leading to new IDs being assigned and no connection between old and new entities.
* If you want to change the monitoring method from `applicationMonitoring` or `cloudNativeFullstack` to `classicFullstack` or `hostMonitoring`, you need to restart all the Pods that were previously instrumented with `applicationMonitoring` or `cloudNativeFullstack`.

### Troubleshoot pod injection issues using pod annotations

If OneAgent, metadata enrichment, or the OTLP exporter configuration isn't injected as expected, check the annotations on the affected pod to find out why injection was skipped.

The following annotations indicate that the Dynatrace Operator webhook intentionally skipped injection for a pod:

```
oneagent.dynatrace.com/injected: "false"



metadata-enrichment.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/injected: "false"
```

The corresponding `reason` annotation explains why:

```
oneagent.dynatrace.com/reason: "MissingTenantUUID"



metadata-enrichment.dynatrace.com/reason: "OwnerLookupFailed"



otlp-exporter-configuration.dynatrace.com/reason: "IngestEndpointUnavailable"
```

#### Reasons for skipped injection

See the following reason values to narrow down the root cause.

| Reason | Affected components | Description | Details |
| --- | --- | --- | --- |
| `NoBootstrapperConfig` | * OneAgent * Metadata enrichment | The webhook can’t find or create a bootstrapper config Secret in the pod’s namespace at injection time. | This usually happens when DynaKube reconciliation isn’t complete or configuration issues prevent reconciliation. The bootstrapper config Secret contains required configuration (such as tokens) for CodeModule and metadata enrichment injection.  Two variants exist:  * `<dynakube name>-bootstrapper-config` in Dynatrace Operator namespace (usually `dynatrace`), which is copied if needed. * `dynatrace-bootstrapper-config` in the injected pod’s namespace, which is mounted into the pod and used during injection. |
| `NoMutationNeeded` | * OneAgent * Metadata enrichment | The webhook determines that the pod doesn’t require injection. | This typically occurs when injection is disabled via annotations. |
| `OwnerLookupFailed` | * OneAgent * Metadata enrichment * OTLP exporter configuration | The webhook can’t determine the pod owner (name and kind), which is required for injection. | This typically happens when the Kubernetes API is temporarily unreachable or slow to respond. |
| `MissingTenantUUID` | OneAgent | DynaKube reconciliation isn’t complete and the environment UUID hasn’t been verified at injection time. | This may occur during the initial Dynatrace Operator setup or when configuration issues prevent reconciliation. |
| `DynaKubeStatusNotReady` | OneAgent | DynaKube reconciliation isn’t complete and the CodeModules-related status isn’t ready at injection time. | Because the status is unavailable, the webhook can’t determine which CodeModule to inject. |
| `NoOTLPExporterConfigSecret` | OTLP exporter configuration | The webhook can’t find or create an OTLP exporter configuration Secret in the pod’s namespace at injection time. | This usually happens when DynaKube reconciliation isn’t complete or configuration issues prevent reconciliation.  Two variants exist:  * `<dynakube name>-otlp-exporter-config` in Dynatrace Operator namespace (source Secret). * `dynatrace-otlp-exporter-config` in the injected pod’s namespace, which is mounted into the pod. |
| `NoOTLPExporterActiveGateCertSecret` | OTLP exporter configuration | The webhook can’t find or create an ActiveGate certificate Secret in the pod’s namespace at injection time. | This usually happens when DynaKube reconciliation isn’t complete or configuration issues prevent reconciliation. This Secret is required only when the OTLP exporter communicates with ActiveGate over TLS.  Two variants exist:  * `<dynakube name>-otlp-exporter-certs` in Dynatrace Operator namespace (source Secret). * `dynatrace-otlp-exporter-certs` in the injected pod’s namespace, which is mounted into the pod. |
| `IngestEndpointUnavailable` | OTLP exporter configuration | The webhook can’t construct a valid ingest endpoint URL at injection time. | Without a valid ingest endpoint URL, the OTLP exporter configuration can’t be injected. |

### Injected pods fail with `ImagePullBackOff` on a private registry

If injected application pods fail to start with `ImagePullBackOff` while pulling the init container image from a private registry, the pods are missing valid registry credentials.

The DynaKube `customPullSecret` authenticates only the operator-managed components in the `dynatrace` namespace. It is not distributed to injected application pods. Every injected pod runs a Dynatrace init container (the Dynatrace Operator image, or the OneAgent code modules image for [node image pull](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes "Reference for how Dynatrace Operator delivers OneAgent code modules to application pods, including ephemeral volumes, CSI driver image pull, and ZIP download.")) that the Kubernetes node must pull, so you must provide the pull secret yourself.

This often surfaces after upgrading to Kubernetes 1.35, where the [`KubeletEnsureSecretPulledImages`﻿](https://kubernetes.io/docs/concepts/containers/images/#ensureimagepullcredentialverification) feature gate is enabled by default. The kubelet then verifies pull credentials per pod, even for images already cached on the node, so pods that previously reused a cached image now fail without their own credentials.

To resolve this, distribute a pull secret to your application namespaces, nodes, or pods. For details, see [Provide pull secrets for injected workloads](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry#injected-workloads "Use a private registry").