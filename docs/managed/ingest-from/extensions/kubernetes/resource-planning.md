---
title: Kubernetes resource planning
source: https://docs.dynatrace.com/managed/ingest-from/extensions/kubernetes/resource-planning
---

# Kubernetes resource planning

# Kubernetes resource planning

* Reference
* 5-min read
* Published Aug 25, 2026

This reference covers resource sizing for SQL Extension Executor pods and the Extension Execution Controller (EEC) on Kubernetes, including recommended profiles, deployment examples, and scaling strategies for production use.

## SQL Extension Executor

When planning your SQL Extension Executor deployment, base your sizing on the expected number of monitored endpoints, not monitoring configurations. A single monitoring configuration can define multiple endpoints, each of which consumes resources independently.

### Resource profiles

We recommend three resource profiles based on the expected number of endpoints per pod. These profiles cover all supported database vendors.

| Profile | Endpoints per pod | CPU request | CPU limit | Memory request | Memory limit |
| --- | --- | --- | --- | --- | --- |
| **Small** | up to 25 | 25m | 250m | 256Mi | 384Mi |
| **Medium** | up to 100 | 50m | 500m | 512Mi | 768Mi |
| **Large** | up to 150 | 100m | 1000m | 1024Mi | 1280Mi |

To apply a resource profile, set the `resources` field under your executor group in DynaKube. The following example configures the Small profile:

```
extensions:



databases:



- id: default



replicas: 2



resources:



requests:



cpu: 25m



memory: 256Mi



limits:



cpu: 250m



memory: 384Mi
```

#### Choose the right profile

Start by estimating the total number of endpoints that will be monitored across all your monitoring configurations. Divide that by the number of pods in the deployment to determine the per-pod endpoint count, then select the matching profile.

For example, if you plan to monitor 200 database endpoints and run three pods, each pod will handle approximately 65–70 endpoints—the Medium profile is appropriate.

#### Maximum endpoints per pod

We recommend a maximum of 150 endpoints per pod. Beyond this threshold, a pod's internal resource consumption may approach operating system-level limits that are outside the scope of Kubernetes pod resource configuration and can't be resolved by increasing CPU or memory.

If your deployment needs to monitor more than 150 endpoints, add more pods to the deployment instead of increasing the resource allocation on existing ones. See [Scaling strategy](#scaling-strategy).

### Deployment sizing

#### Minimum number of pods

For production deployments, we recommend a minimum of two pods. When a pod becomes unavailable, the platform automatically redistributes its endpoints to the remaining pods in the deployment. With only a single pod, there is no failover target—monitoring will stop until the pod recovers. Running at least two pods ensures continuity of monitoring during pod restarts, node maintenance, or unexpected failures.

#### Sizing examples

| Total endpoints | Recommended pods | Profile per pod | Notes |
| --- | --- | --- | --- |
| Up to 25 | 2 | Small | Minimum for redundancy |
| Up to 100 | 2 | Medium |  |
| Up to 200 | 2–3 | Medium | Stay within 100 endpoints per pod |
| Up to 300 | 3–4 | Medium to Large |  |
| 300+ | 4+ | Medium to Large | Prefer more pods over larger pods |

### Scaling strategy

When demand grows, prefer horizontal scaling (more pods) over vertical scaling (bigger pods).

Adding more pods to the deployment is more effective than increasing resource limits on existing pods for two reasons:

1. Each pod has its own operating system-level resource boundaries that are independent of Kubernetes CPU and memory settings. Scaling horizontally distributes the workload across these boundaries, while vertical scaling does not.
2. Horizontal scaling improves fault tolerance. With more pods, the impact of losing a single pod is smaller—fewer endpoints need to be redistributed, and the remaining pods are less likely to become overloaded during failover.

The platform handles load distribution automatically—endpoints are balanced across available pods without manual intervention.

#### When to scale

Consider adding pods when:

* The number of endpoints per pod approaches or exceeds 100
* You observe sustained high memory utilization (above 80% of the limit)
* Pod restarts or instability occurs under load

### Important considerations

* Resource consumption varies by vendor and configuration. The actual resource usage per endpoint depends on the database vendor, enabled feature sets, query intervals, and the complexity of the monitored environment.
* Monitor actual utilization after deployment. The recommended profiles serve as starting points. After deploying in your environment, observe actual CPU and memory usage over time and adjust resource limits as needed. If utilization is consistently low, switch to a smaller profile or consolidate more endpoints per pod. If utilization approaches limits, consider scaling out.
* Plan for growth. If you expect the number of monitored databases to increase over time, select a profile and pod count that leaves room for additional endpoints without requiring immediate reconfiguration.

## Extension Execution Controller

The Extension Execution Controller (EEC) runs as a single controller pod per cluster—there is always exactly one regardless of how many executor groups or endpoints are configured. Unlike executor pods, the EEC scales vertically. Controller pod sizing is therefore a vertical exercise: adjust CPU and memory requests and limits to match your workload.

The EEC acts as the coordination layer between executor pods and the Dynatrace backend. It receives extension definitions from the backend, distributes monitoring tasks to executor pods, and forwards collected signals upstream. Higher endpoint counts and ingest rates place proportionally more load on the EEC.

### Resource configuration

Configure EEC resources under [`spec.templates.extensionExecutionController.resources`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extension-execution-controller-template "List the available parameters for setting up Dynatrace Operator on Kubernetes.") in your DynaKube. The following values are recommended as a starting point for production deployments:

```
spec:



templates:



extensionExecutionController:



resources:



requests:



cpu: 1



memory: 1Gi



limits:



cpu: 2



memory: 3Gi
```

These values were validated using the following setup:

* Extension: PostgreSQL extension 3.2.1
* Database instances: 10 PostgreSQL databases, each with 15 tables and 75 indexes
* Executor pods: 20
* Total endpoints monitored: 1,000

### Maximum ingest capacity

The following values represent the absolute maximum ingest throughput of a single controller pod, measured using synthetic load tests where metrics and logs were ingested independently. Controller pod CPU and memory consumption were recorded at each load level.

| Signal type | Max/minute | EEC CPU | EEC memory |
| --- | --- | --- | --- |
| Metrics | 8.5 million | 3 cores | 750 MiB |
| Logs | 1.5 million | 1.5 cores | 700 MiB |

To estimate the metric ingest rate your extensions will generate, see the licensing cost sections of the [Oracle Database extension](/managed/observe/infrastructure-observability/databases/extensions/oracle-database#licensing-costs "Collect Oracle Database metrics and audit logs to monitor performance and security.") and [PostgreSQL extension](/managed/observe/infrastructure-observability/databases/extensions/postgresdb-remote-monitoring#licensing-costs "Collect PostgreSQL database performance metrics and query logs via remote ActiveGate monitoring to detect anomalies, blocking queries, and performance issues.") documentation.

### Monitor EEC utilization

After deploying, monitor actual resource usage in [![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes**](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."). Go to the controller pod under the `dynatrace` namespace to observe CPU and memory consumption over time, and adjust your resource configuration if needed.