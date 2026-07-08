---
title: Settings API - Built-in container monitoring rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-container-built-in-monitoring-rule
---

# Settings API - Built-in container monitoring rules schema table

# Settings API - Built-in container monitoring rules schema table

* Published Dec 05, 2023

### Built-in container monitoring rules (`builtin:container.built-in-monitoring-rule)`

Dynatrace disables monitoring of containers that do not run any applications.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:container.built-in-monitoring-rule` | * `group:processes-and-containers.containers` * `group:processes-and-containers` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.built-in-monitoring-rule` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:container.built-in-monitoring-rule` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:container.built-in-monitoring-rule` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Do not monitor containers where Kubernetes container name equals 'POD' `ignoreKubernetesPauseContainer` | boolean | Disable monitoring of platform internal pause containers in Kubernetes and OpenShift. | Required |
| Do not monitor containers where Docker stripped image name contains 'pause-amd64' `ignoreDockerPauseContainer` | boolean | Disable monitoring of platform internal pause containers in Kubernetes and OpenShift. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-sdn' `ignoreOpenShiftSdnNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-sdn namespace. | Required |
| Do not monitor containers where Kubernetes full pod name ends with '-build' `ignoreOpenShiftBuildPodName` | boolean | Disable monitoring of intermediate containers created during image build. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-ovn-kubernetes' `ignoreOpenShiftOvnKubernetesNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-ovn-kubernetes namespace. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-etcd' `ignoreOpenShiftEtcdNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-etcd namespace. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-kube-apiserver' `ignoreOpenShiftKubeApiserverNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-kube-apiserver namespace. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-monitoring' `ignoreOpenShiftMonitoringNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-monitoring namespace. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-machine-config-operator' `ignoreOpenShiftMachineConfigOperatorNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-machine-config-operator namespace. | Required |
| Do not monitor containers where Kubernetes namespace equals 'openshift-ingress-canary' `ignoreOpenShiftIngressCanaryNamespace` | boolean | Disable monitoring of platform internal containers in the openshift-ingress-canary namespace. | Required |