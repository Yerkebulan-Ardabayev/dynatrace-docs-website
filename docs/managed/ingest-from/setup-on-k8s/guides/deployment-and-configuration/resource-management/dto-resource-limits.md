---
title: Set resource limits for Dynatrace Operator components
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/dto-resource-limits
scraped: 2026-05-12T12:05:28.340010
---

# Set resource limits for Dynatrace Operator components

# Set resource limits for Dynatrace Operator components

* 2-min read
* Updated on Feb 27, 2026

Properly configured resource limits ensure optimal performance and stability of Dynatrace Operator components while preventing resource contention in your Kubernetes cluster. This guide helps you understand how to set appropriate resource limits based on your environment size and usage patterns.

## Default resource limits baseline

The provided default resource limits have been validated through performance testing. These defaults performed well in the following environment:

* 25 nodes (e2-standard-32 nodetype on Google Kubernetes Engine)
* 20 DynaKubes
* 2,500 namespaces
* 5,000 pods

## Resource consumption factors

The following five key indicators influence resource consumption across different Dynatrace Operator components:

| **Indicator** | **Dynatrace Operator** | **Webhook** | **CSI driver** |
| --- | --- | --- | --- |
| Namespaces | Applicable | Applicable |  |
| Nodes | Applicable |  |  |
| DynaKubes | Applicable |  | Applicable |
| Pods |  | Applicable | Applicable |
| Number of OneAgent versions |  |  | Applicable |

### Understanding the impact indicators

* **Namespaces**: More namespaces increase the workload for the Operator and webhook as they need to monitor and manage resources across all namespaces.

  + Impact:

    - Increases CPU/memory usage of Operator
    - Increases CPU usage of webhook
* **Nodes**: Additional nodes require more resources as the Operator keeps a list of all available nodes on the Kubernetes clusters and verifies that they match the available hosts on the Dynatrace server.

  + Impact:

    - Increases CPU/memory usage of Operator
* **DynaKubes**: Each DynaKube resource represents a separate Dynatrace deployment that needs individual management.

  + Impact:

    - Increases CPU/memory usage of Operator
    - Increases CPU/memory usage of webhook
    - Increases CPU/memory usage of CSI driver provisioner
* **Pods**: The webhook processes admission requests for every pod, while the CSI driver handles volume mounting for pods using OneAgent.

  + Impact:

    - Increases CPU/memory usage of CSI driver server/liveness-probe/registrar
* **OneAgent versions**: The CSI driver needs to manage and provide access to different OneAgent versions, requiring additional storage and processing resources.

  + Impact:

    - Increases CPU/memory usage of CSI driver provisioner

### Minimize impacts of large number of Node

By default, Dynatrace Operator monitors host availability in your cluster to detect expected removal of host OneAgent pods especially in scaling scenarios. This monitoring is not necessary in serverless environments.

#### When to disable host availability detection

This functionality is present in all versions of the Operator before 1.6.0 and it can't be turned off.

It can be turned off in 1.6.3 and 1.7.3 or in newer Operator versions.

applicationMonitoring

You can reduce the Operator's resource consumption by disabling host availability detection if your DynaKubes:

* **only** use application-only monitoring modes and
* do **not** use any of the host-based monitoring features.

#### How to disable host availability detection

To disable host availability detection, set the following Helm value:

```
operator:



hostAvailabilityDetection: false
```

This optimization can reduce CPU and memory usage of the Operator, especially in large clusters with many nodes.

**Cluster-wide setting**: `operator.hostAvailabilityDetection` affects all DynaKubes managed by the Operator. Only disable this if you are certain that **none** of your DynaKubes require host-based monitoring. Disabling it when host OneAgents are required can cause false-positive host missing warnings during node scaling or other node-related operations.

## Customize resource limits

While the default resource limits should be sufficient for most use cases, you can customize them based on your specific needs.

Modify `values.yaml` to set resource limits for Dynatrace Operator, webhook, or CSI driver.

* **Dynatrace Operator**

  ```
  operator:



  requests:



  cpu: 50m



  memory: 64Mi



  limits:



  cpu: 100m



  memory: 128Mi
  ```
* **Webhook**

  ```
  webhook:



  requests:



  cpu: 300m



  memory: 128Mi



  limits:



  cpu: 300m



  memory: 128Mi
  ```
* **CSI driver**

  ```
  csidriver:



  csiInit:



  resources:



  requests:



  cpu: 50m



  memory: 100Mi



  limits:



  cpu: 50m



  memory: 100Mi



  server:



  resources:



  requests:



  cpu: 50m



  memory: 100Mi



  limits:



  cpu: 50m



  memory: 100Mi



  provisioner:



  resources:



  requests:



  cpu: 300m



  memory: 100Mi



  job:



  resources:



  requests:



  cpu: 200m



  memory: 30Mi



  registrar:



  resources:



  requests:



  cpu: 20m



  memory: 30Mi



  limits:



  cpu: 20m



  memory: 30Mi



  livenessprobe:



  resources:



  requests:



  cpu: 20m



  memory: 30Mi



  limits:



  cpu: 20m



  memory: 30Mi
  ```

The CSI driver `provisioner` and `job` components do not have default resource limits specified. This allows them to use additional resources when available, improving performance.

The `job` component is only used with [node-image-pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Configure node image pull").

Note that if the limits are set too low, this can lead to increased pod startup times due to CPU throttling or, OOM kills in the CSI driver due to insufficient memory, which can prevent applications from starting.

### Scaling resource limits for different environments

The default resource requests and limits are designed for medium-scale environments. Use the following guidelines to adjust limits based on your environment size. These are starting recommendationsâ-always monitor actual resource usage in your environment and adjust accordingly.

**Pod Quality of Service Classes**: Some components have their limits and requests set to the same value to ensure a [Guaranteed Pod Quality of Serviceï»¿](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed). When scaling the limits of such components, always scale the requests proportionally as well.

**Proportional fairness:** Having low CPU requests on a container can cause throttling due to the CPU management policy of the node. The requests serve as a **minimum guarantee**. On a heavily utilized node, therefore, containers with smaller requests will be throttled more compared to containers with larger requests, regardless of their limit. When scaling the limits, always consider scaling the requests as well.

The CSI driver `job` resource requests and limits do not need to scale based on environment size. They are independent of node count, pod count, and DynaKube count. However, you can adjust the CPU request to control how quickly the job completes, which determines how soon the CSI driver is ready to mount volumes:

| CPU request | Approximate completion time |
| --- | --- |
| 100m | ~1 min |
| 200m (default) | ~30 sec |
| 300m | ~25 sec |

This only affects the job's `Running` duration. It doesn't impact `ContainerCreation` or `PodScheduling` times.

Starting with Dynatrace Operator version 1.9.0, the webhook's `replicas` can be customized in Helm in addition to its resource limits. This allows you to scale the Webhook horizontally in larger environments, providing better performance and availability.

The resource recommendation below is for two webhook replicas. If you choose to use a different number of replicas, adjust the resource limits accordingly.

* Example: If you want to use 3 replicas instead of 2, you can reduce the CPU/Memory requests/limits by approximately 30% while maintaining overall performance but gain higher availability.

For details on configuring the webhook's `replicas` and related values, see [Configure high availability](#high-availability-helm).

#### Large environments (> 50 nodes, > 10,000 pods)

Increase the default requests/limits by 50â100%:

* **Dynatrace Operator**:

  + Request: CPU 100m, Memory 128Mi
  + Limits: CPU 200m, Memory 256Mi
* **Webhook**:

  + Requests: CPU 600m, Memory 256Mi
  + Limits: CPU 600m, Memory 256Mi
* **CSI driver provisioner**:

  + Requests: CPU 600m, Memory 200Mi
* **CSI driver server**:

  + Requests: CPU 100m, Memory 200Mi
  + Limits: CPU 100m, Memory 200Mi
* **CSI driver liveness-probe**:

  + Requests: CPU 30m, Memory 50Mi
  + Limits: CPU 30m, Memory 50Mi
* **CSI driver registrar**:

  + Requests: CPU 30m, Memory 50Mi
  + Limits: CPU 30m, Memory 50Mi

#### Enterprise environments (> 100 nodes, > 25,000 pods)

Increase the default requests/limits by 100â200%:

* **Dynatrace Operator**: CPU 400m, Memory 512Mi

  + Request: CPU 200m, Memory 256Mi
  + Limits: CPU 400m, Memory 512Mi
* **Webhook**:

  + Requests: CPU 1000m, Memory 512Mi
  + Limits: CPU 1000m, Memory 512Mi
* **CSI driver provisioner**:

  + Requests: CPU 900m, Memory 300Mi
* **CSI driver server**:

  + Requests: CPU 150m, Memory 300Mi
  + Limits: CPU 150m, Memory 300Mi
* **CSI driver liveness-probe**:

  + Requests: CPU 50m, Memory 70Mi
  + Limits: CPU 50m, Memory 70Mi
* **CSI driver registrar**:

  + Requests: CPU 50m, Memory 70Mi
  + Limits: CPU 50m, Memory 70Mi