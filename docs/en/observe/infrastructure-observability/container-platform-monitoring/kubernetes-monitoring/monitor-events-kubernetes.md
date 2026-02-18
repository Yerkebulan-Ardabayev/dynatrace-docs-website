---
title: Monitor Kubernetes/OpenShift events
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-events-kubernetes
scraped: 2026-02-18T21:26:48.594935
---

# Monitor Kubernetes/OpenShift events

# Monitor Kubernetes/OpenShift events

* 8-min read
* Updated on Jul 05, 2024

## Prerequisites

* ActiveGate version 1.265+
* In Dynatrace, go to **Monitoring settings** > **Kubernetes** and make sure that **Monitor Kubernetes namespaces, services, workloads, and pods** is turned on.
* [Enable the latest version of Dynatrace log monitoring](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")

## Kubernetes events monitoring for analysis and alerting

For full observability into your Kubernetes events, automatic Davis analysis, and custom alerting, you need to enable Kubernetes event monitoring.

To enable event monitoring for specific Kubernetes clusters

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster and, in the **Actions** column, select **More** (**â¦**) > **Settings**.
3. On the **Monitoring Settings** tab, turn on **Monitor events**.
4. Select **Save changes**.

When you enable **Monitor events**, all events are ingested and all [important events](#important-events) are considered in the Davis root-cause detection. Alternatively, for maximum flexibility and fine-grained control over the events you want to ingest from Kubernetes, you can [filter events](#filter).

### Inferred Kubernetes events

Even if **Monitor events** is disabled, the so-called *inferred* Kubernetes events are still ingested. These inferred events aren't native Kubernetes events but are created by ActiveGate based on the information from the Kubernetes API server.

Examples of inferred events:

* cgroup OOM kill events
* Workload specification changes (replicas, images, environment variables, resources, probes) for

  + Deployments
  + StatefulSets
  + DaemonSets

These events aren't billed and are relevant for Davis root-cause analysis.

### View events

After enabling the Kubernetes event monitoring, you can view and analyze events from the Kubernetes cluster.

On your Kubernetes cluster details page, go to **Events**.

You can filter events by:

* Timeframe: select one of the timeframes in the chart to view open events for that timeframe
* Specific events: select one of the group labels below the chart to view specific events

For more information about an event, select **Details** for the event.

Kubernetes events are associated with Kubernetes entities. An event is displayed on the respective entity page and on related entity pages. For example, pod events are displayed on the cluster, namespace, workload, and pod details page.

You can also view events on the **Log viewer** page (in Dynatrace, go to ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**), which allows for advanced search and filtering.

If the environment is platform enabled the events are stored in Grail. The following DQL query can be used as a template to query for specific events in [**Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability dataâall in one collaborative, customizable workspace.") or [**Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.").

```
fetch events



| filter event.provider == "KUBERNETES_EVENT"
```

[Inferred Kubernetes events](#inferred) are not shown in **Log viewer**. They are directly ingested as events.

## Filter events to be monitored

Filtering is turned off by default, which means that all events are ingested. To set up monitoring only for certain events

1. Turn on **Filter events**.

   If you don't see the **Filter events** switch, make sure that **Monitor events** is turned on first.
2. [Set up multiple field selectors for every Kubernetes environment](#set-up-event-field-selectors).
3. Optional [Have Davis perform root cause analysis on all important Kubernetes events](#important-events).
4. Select **Save changes**.

### Set up event field selectors

Filtering follows the [Kubernetes-established syntax of field selectorsï»¿](https://kubernetes.io/docs/concepts/overview/working-with-objects/field-selectors/), so events can be chosen based on event resource fields such as `source.component`, `type`, or `involvedObject`.

A field selector expression must meet the following requirements:

* It must conform to the following regular expression: `^[\w\.]{1,1024}((=){1,2}|(!=))[^,!=]{0,256}(,[\w\.]{1,1024}?((=){1,2}|(!=))[^,!=]{0,256}){0,9}$`.
* It can have up to 10 selectors separated by commas. Events matching all comma-separated selectors will be ingested. The logical operator is `AND`.
* A selector consists of three parts:

  + **Key:** Contains up to 1,024 alphanumerical characters, underscores, and dots.
  + **Operator:** Is either `=` , `==` or `!=`.
  + Optional **Value:** Can contain up to 256 characters. Cannot contain exclamation marks, equal signs, or commas.

For example,

* If you set a field selector expression to `involvedObject.namespace=hipster-shop,type=Warning`, the expression will store all the events related to the namespace `hipster-shop` that are of type `Warning`.
* If you separate the expression into two independent field selectors, you'll get all events for namespace `hipster-shop` and all events of type `Warning`. The logical operator in this case is `OR`.

**Example event field selectors:**

| **Event field selectors** | **Field selector expression** |
| --- | --- |
| Get all `Node` events | `involvedObject.kind=Node` |
| Get all `Warning` events | `type=Warning` |
| Get all `Pod` events | `involvedObject.kind=Pod` |
| Get all events of objects related to a specific namespace | `involvedObject.namespace=<your_namespace>` (Make sure to replace `<your_namespace>` with the name of your own namespace) |
| Get all `BackOff` events for pods across all namespaces | `reason=BackOff` |
| Get all events with non-empty type field | `type!=` |
| Get all nginx container events | `involvedObject.fieldPath==spec.containers{nginx}` |

To set up event field selectors, select one of the options below:

Via web UI

Via CLI

Via API

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster and, in the **Actions** column, select **More** (**â¦**) > **Settings**.
3. On the **Monitoring Settings** tab

   * Turn on **Filter events**.
   * Select **Add events field selector**.
   * Enter a **Field selector name** and **Field selector expression**.
4. Select **Save changes**.

Example command:

```
kubectl get events --all-namespaces --field-selector involvedObject.namespace=hipster-shop,type=Warning
```

You can define the event field selectors via [Dynatrace API](/docs/dynatrace-api/configuration-api/k8s-credentials-api-api "Manage Kubernetes credentials via the Dynatrace configuration API.").

You can create a maximum of 20 event filter rules per Kubernetes cluster.

### Monitor important events

When problems with applications, microservices, or infrastructure are detected, Davis performs root cause analysis on all important Kubernetes events for nodes, namespaces, workloads, and pods.

A Kubernetes event is important (relevant for Davis root cause analysis) when at least one of the following two conditions is true.

* The event reason is in the predefined list of [important reasons](#important-event-reasons).
* The event type is `Warning`.

Important event reasons

`BackOff`,
`DeadlineExceeded`,
`Killing`,
`NodeNotSchedulable`,
`OutOfDisk`,
`Preempting`

By default, all these events are monitored when [**Monitor events**](#monitor-events) is turned on. If you choose to [Filter events](#filter), either predefined important events filter or custom events filters can be applied. If multiple filters are set, they are combined using a logical `OR`. The event is ingested, once a Kubernetes event matches any of the filters.

To enable monitoring of important events, when event filtering is turned on

1. Go to ![Kubernetes](https://dt-cdn.net/images/kubernetes-512-90e7075764.png "Kubernetes") **Kubernetes Classic**.
2. Find your Kubernetes cluster and, in the **Actions** column, select **More** (**â¦**) > **Settings**.
3. On the **Monitoring Settings** tab, turn on **Include important events**.

   If you don't see the **Include important events** switch, make sure that **Monitor events** and **Filter events** are turned on first.
4. Select **Save changes**.

## Charting and alerting

Kubernetes events are made available in the **Kubernetes: Event count** (`builtin:kubernetes.events`) metric. To filter the events count metric for the relevant events, use the `k8s.event.reason` and `k8s.event.type` dimensions.

* To help you understand the distribution and development of Kubernetes events over time, use [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") to create charts. You can use the charts to compare different timeframes, different entities, event filters, and the use of complex expressions.
* To trigger alerts whenever Kubernetes events occur (for example, always alert in case of an `Evicted` event), define [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace") based on the **Kubernetes: Event count** metric.

## Licensing

To estimate the number of events that consume DDUs, you can query the `dsfm:active_gate.kubernetes.events.processed` metric, which provides information about the number of events that are being ingested into Dynatrace per Kubernetes cluster.

Example query for a 24-hour timeframe:

`dsfm:active_gate.kubernetes.events.processed:splitBy("dt.entity.kubernetes_cluster"):sum:auto:sort(value(sum,descending)):limit(10)`

DDU consumption applies to Kubernetes event monitoring. For details, see [DDUs for custom Davis events](/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events "Understand how to calculate Davis data unit consumption and costs related to custom-configured and custom-ingested events.").

## Related topics

* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")