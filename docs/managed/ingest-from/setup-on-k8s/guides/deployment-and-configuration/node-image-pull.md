---
title: Configure node image pull
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull
scraped: 2026-05-12T12:03:38.167936
---

# Configure node image pull

# Configure node image pull

* 6-min read
* Updated on Jan 27, 2026

Dynatrace Operator version 1.5

cloudNativeFullStack applicationMonitoring

The node image pull feature introduces new capabilities for image pulling of the Dynatrace code modules image, along with enhanced performance and security in the Dynatrace Operator. These enhancements enable the following improvements and use-cases:

* Cloud-native full-stack monitoring works independently of the CSI driver [1](#fn-1-1-def)

  + Cloud-native full-stack monitoring can be deployed via OpenShift OperatorHub
* Application monitoring works in combination with the public signed images
* Combination of non-CSI and CSI-based Dynatrace code module injection (for details, see [Enforce CSI-less application monitoring](#mixed-mode)) [1](#fn-1-1-def)

  + for mixed setups with/without node access like AWS Elastic Kubernetes Service with EC2 nodes and Fargate
  + for leveraging the benefits of the CSI driver, with specific exceptions for [NGINX instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.")

1

Deployments using the cloud-native full-stack mode require Dynatrace Operator version 1.6+ and OneAgent version 1.317+.

With the node image pull feature enabled, Kubernetes-native integration into supply chain security tooling is greatly simplified. Additionally, the feature configures the operator to always pull images via the Kubernetes nodes, reducing the need for a `customPullSecret` when sourcing images from private registries.

Dynatrace Operator deployments that do not utilize the CSI driver have increased storage requirements due to current Kubernetes concepts. Please refer to [Storage optimization without CSI driver](#storage-optimization) to learn how to minimize storage consumption.

## Prerequisites

* Dynatrace OneAgent version 1.311.72+

  + Recommended Dynatrace OneAgent version is 1.317+
* Dynatrace code modules image sourced from our [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry") or your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

When using a private registry, you must ensure that all nodes are authenticated to access the registry.

Alternatively, the following options are available for providing registry credentials:

* **With CSI driver**: You can specify a `customPullSecret` in the DynaKube configuration to provide the necessary credentials for image pulls.
* **Without CSI driver**: The `customPullSecret` will not be added to injected application pods. For security reasons, Dynatrace Operator does not replicate provided pull secrets into application namespaces or mount them to pods outside of Dynatrace Operator's control. Instead, you must manually configure pull secrets at one of the following levels:

  + **Node level**: Configure registry authentication directly on each node.
  + **Namespace level**: Add the pull secret to the namespace where application pods are deployed.
  + **Pod level**: Configure the pull secret via the `imagePullSecrets` field in the pod specification of your application pods.

For more information on manual pull secret configuration, see [Kubernetes documentation on pulling images from private registriesï»¿](https://kubernetes.io/docs/concepts/containers/images/#using-a-private-registry).

### Limitations

Note that the following configurations are not supported:

* Due to GKE Autopilot's dynamic provisioning of nodes and their sizes based on the aggregated resource requests of Pods to optimize resource utilization, GKE Autopilot is not suitable for the node image pull feature in combination with the CSI driver.

  + We recommend using the feature without the CSI driver on GKE Autopilot systems or, alternatively, using the CSI driver in a standard setup with node image pull disabled.

## Behavior and configuration

Known issue in Dynatrace Operator version 1.5

We have identified an issue with cloud-native full-stack without using the CSI driver with details provided in the [Dynatrace Operator version 1.5.1 release notes](/managed/whats-new/dynatrace-operator/dto-fix-1-5-1#known-issues "Release notes for Dynatrace Operator, version 1.5.1").

**This issue has been resolved with Dynatrace Operator version 1.6.0 and OneAgent version 1.317+.**

The feature is activated via a feature flag on DynaKube. The following two points outline the behavior and benefits of the feature based on whether the CSI driver has been deployed as part of the operator:

* **With CSI driver** - Instead of downloading the code modules into the CSI driver pod, Dynatrace code modules images are directly pulled through the node. Each CSI driver pod creates a job for the node to download the code modules to the host filesystem, where they will be used by the CSI driver as usual. This approach reduces the need for a `customPullSecret` when sourcing images from private registries. [1](#fn-2-1-def)
* **Without CSI driver** [2](#fn-2-2-def) - If the CSI driver is not installed in your cluster, you can leverage the node image pull feature with the code modules image to improve injection performance and resiliency. This approach prioritizes injection performance for a faster and more resilient injection over storage optimizations enabled by the CSI driver. **Note:** The `customPullSecret` is not supported with the node image pull feature when used without the CSI driver. When using private registries, you must manually configure pull secrets at the node, namespace, or pod level (see [Prerequisites](#prerequisites)).

1

Starting from [Dynatrace Operator version 1.8](/managed/whats-new/dynatrace-operator/dto-fix-1-8-0 "Release notes for Dynatrace Operator, version 1.8.0"), the download jobs inherit the same `PriorityClass` as the CSI driver to ensure fast scheduling and preemption on congested clusters. You can configure the value via `csidriver.priorityClassValue` in the Helm values file. For guidance, see [Use priorityClass for critical Dynatrace components](/managed/ingest-from/setup-on-k8s/guides/high-availability/priority "Use priorityClass for critical Dynatrace components").

2

Deployments using the cloud-native full-stack mode require Dynatrace Operator version 1.6+ and OneAgent version 1.317+.

Please refer to [Storage optimization without CSI driver](#storage-optimization) to learn how to minimize storage consumption.

### DynaKube configuration

Refer to the following DynaKube snippet for configuring the feature flag and specifying a Dynatrace code modules image from a [supported public](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry "Use a public registry") or [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry"):

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/node-image-pull: "true"



spec:



oneAgent:



# example, can also be used with `applicationMonitoring`



cloudNativeFullStack:



codeModulesImage: <dynatrace-codemodules-image>
```

Known issue

There is a known issue with OneAgent versions >= 1.313.0 to < 1.313.45. Please use Dynatrace code modules version 1.313.45+.

Example image tag for `codeModulesImage` field:

```
public.ecr.aws/dynatrace/dynatrace-codemodules:1.313.45.20250521-164818
```

For more details on repositories and tag information, explore our [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry").

## Storage optimization without CSI driver

OneAgent version 1.315+

Without the CSI driver, code module injection consumes ephemeral storage for each injection. OneAgent binaries are stored and mounted to the app pod in an `emptyDir` volume. To minimize storage consumption, you can either annotate individual application pods or configure this setting at the DynaKube level, as appropriate. These annotations should specify the application technology (e.g., Java), allowing precise control over code module injection into application containers and preventing unnecessary code module binaries from being copied.

If a CSI driver is deployed on the node, you can also manually configure code module injection to not use the CSI driver.
For more information, see [Enforce CSI-less application monitoring](#mixed-mode).

If storage optimization is not configured (i.e., the `oneagent.dynatrace.com/technologies` annotation is missing), storage consumption will follow the guidelines outlined in the [storage requirements](/managed/ingest-from/setup-on-k8s/reference/storage "A comprehensive overview of the storage requirements for different Dynatrace Operator deployment mode in Kubernetes environments").

Each configured technology, whether specified individually or as a comma-separated list, will be copied into a shared volume, consuming ephemeral storage.

### Technology identifiers

Here is a list of the identifiers you can use per technology:

| Technology | Identifier |
| --- | --- |
| [Java](/managed/ingest-from/technology-support/application-software/java "Learn about all aspects of Dynatrace support for Java application monitoring.") | `java` |
| [.NET, .NET Core and .NET Framework](/managed/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") | `dotnet` |
| [Node.js](/managed/ingest-from/technology-support/application-software/nodejs "Read about Dynatrace support for Node.js applications.") | `nodejs` |
| [Python](/managed/ingest-from/technology-support/application-software/python "Learn how to instrument your Python application with OpenTelemetry as a data source for Dynatrace.") | `python` |
| [PHP](/managed/ingest-from/technology-support/application-software/php "Read about Dynatrace support for PHP applications.") | `php` |
| [Go](/managed/ingest-from/technology-support/application-software/go "Read an overview of Dynatrace support for Go applications.") | `go` |
| Apache, IBM HTTP Server | `apache` |
| [NGINX](/managed/ingest-from/technology-support/application-software/nginx "Learn the details of Dynatrace support for NGINX.") | `nginx` |

### Annotate the application pod

To reduce the data copied into application pods, you can specify which OneAgent technologies are relevant for your application. Annotate your application pods as shown in the pod snippet below:

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"
```

When specifying a comma-separated list of technology identifiers, ensure there are no whitespace characters within the annotation value.

Annotation values must use the exact technology identifiers listed in the table above.

If no `oneagent.dynatrace.com/technologies` is provided, all technologies will be copied to application pods.

If a single technology is used across your cluster, or if you want to set a default technology for Dynatrace code module injection, you can configure it at the DynaKube level to apply to all injected application pods.

Configure on DynaKube-level

Modify your DynaKube configuration by enabling the feature and restricting it to a specific technology or a set of multiple technologies:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



annotations:



feature.dynatrace.com/node-image-pull: "true"



oneagent.dynatrace.com/technologies: "java"



spec:



...
```

When specifying a comma-separated list of technology identifiers, ensure there are no whitespace characters within the annotation value.

For more details on repositories and tag information, explore our [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Use a public registry").

## Enforce CSI-less application monitoring

applicationMonitoring cloudNativeFullStack OneAgent version 1.315+

You can selectively configure Dynatrace code module injection without involving the CSI driver, even if the driver is available on the node.
In this case, code module injection behaves as described in [Storage optimization without the CSI driver](#storage-optimization).

To do this, use the `oneagent.dynatrace.com/volume-type: "ephemeral"` annotation, as shown in the code block below.
(The `oneagent.dynatrace.com/technologies` annotation is additional and optional, see [Annotate the application pod](#technologies).)

```
metadata:



annotations:



oneagent.dynatrace.com/volume-type: "ephemeral" # no CSI driver involved



oneagent.dynatrace.com/technologies: "nginx"    # minimize storage consumption
```

To manually force the default behavior, set the `oneagent.dynatrace.com/volume-type: "csi"` annotation.

In this case, [a CSI driver](/managed/ingest-from/setup-on-k8s/how-it-works/components/dynatrace-operator#csidriver "Components of Dynatrace Operator") needs to be available on the node for code module injection to work.

This approach allows you to combine the best of both methods: the storage optimizations provided by the CSI driver and the performance gains and enhanced resiliency of injection without the CSI driver for selected pods and applications.

Example scenarios:

* [NGINX instrumentation](/managed/ingest-from/technology-support/application-software/nginx/manual-runtime-instrumentation "Learn how to force instrumenting patched/non-standard NGINX binaries during runtime.") and prior injection are recommended without the CSI driver for higher resiliency, while other workloads can be injected using the CSI driver, thus eliminating the need for any vendor-specific annotations.
* Mixed setups with and without node access, such as AWS Elastic Kubernetes Service (EKS) with EC2 nodes and Fargate, can be accommodated. Ensure the CSI driver is available on all nodes where code module injection based on CSI driver might occur.