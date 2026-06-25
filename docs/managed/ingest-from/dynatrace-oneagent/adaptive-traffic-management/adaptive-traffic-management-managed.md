---
title: Adaptive Traffic Management for Dynatrace Managed
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-managed
scraped: 2026-05-12T11:14:34.396853
---

# Adaptive Traffic Management for Dynatrace Managed

# Adaptive Traffic Management for Dynatrace Managed

* Explanation
* Updated on Feb 20, 2026

Dynatrace Full-Stack Monitoring packages a variety of features, including fully automatic distributed tracing. Each monitored application or microservice is constantly monitored and the Dynatrace code module collects distributed traces, containing code-level and business insights, that are sent to Dynatrace.

Depending on the transaction volume, OneAgent captures end-to-end traces every minute up to a peak trace per minute. This is Dynatrace's intelligent sampling mechanism that ensures that your Managed cluster cannot be owerwhelmed with trace data during peak times. You can adjust this to your needs.

[PurePath](/managed/observe/application-observability/distributed-traces/use-cases/segment-request "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.")Â® distributed traces are end-to-end transactions captured by OneAgent. Each minute, a statistically relevant number of end-to-end distributed traces is captured within each monitored process. Each trace contains code-level and business insights derived from service-level calls to multiple tiers. Because each trace is captured fully and end-to-end, second- and third-level tiers often capture more total service calls than entry-point processes.

![Each OneAgent-monitored process captures a limited number of new PurePath traces every minute](https://dt-cdn.net/images/oneagent-adaptive-traffic-management-pipe-748-5b04a011d8.png)

Each OneAgent-monitored process captures a limited number of new PurePath traces every minute

When the volume of transactions is high, capturing all traces can increase network bandwidth demands. OneAgent provides a built-in limiter to manage such cases. Each process monitored by OneAgent is allowed to start only a given number of distributed traces per minute. Once the quota is reached, the monitored traffic is used in the most effective way possible via the intelligent mechanism of Adaptive Traffic Management.

## How is Adaptive Traffic Management different from other sampling mechanisms?

In typical applications, the distribution of requests is not even. It's rather a combination of: a large number of unique URLs, a medium number of important requests, and, finally, a few kinds of requests that make up the majority of the traffic (for example, image requests or status checks).

With Adaptive Traffic Management, OneAgent first calculates a list of top requests starting each minute, and then it captures:

* Most traces of unique and rare requests.
* A significant but lower volume of highly frequent requests.

Because the sampling is not random, all important data is captured while maintaining a statistically valid sample set.

Example

The following table represents a top-request calculation example, along with the respective capture rates.

| Request | Number of requests processed by the application | Capture factor | Captured distributed traces (per minute) |
| --- | --- | --- | --- |
| URI A | 900 | 1/2 | 450 |
| URI B | 440 | 1/2 | 220 |
| URI C | 250 | 1 | 250 |
| URI D | 60 | 1 | 60 |
| â¦50 other URIs | 100 | 1 | 100 |
| **Total:** | **1500** |  | **1080** |

In this example, OneAgent captures 1080 requests per minute, according to the configured target number of requests. Depending on the capture factor, URIs are captured each time (URIs C, D, and 50 other URIs) or only 50% of the time (URIs A and B).

You can see the effects of Adaptive Traffic Management in the distributed trace list. If OneAgent is sampling and not all requests are captured, then captured traces will point out that similar requests have not been captured with the message `[amount] more like this` in the distributed trace list.

In this way, OneAgent reduces the data sent to your environment, ensuring that the amount of captured traces stays within the limits of your Dynatrace agreement.

Using Adaptive Traffic Management to reduce the volume of processed data results in saving a lot of network bandwidth and, in the case of Dynatrace Managed environments, precious CPU, memory, network, and storage resources which would otherwise be required to process and store the additional data.

Dynatrace provides the **Configuring trace sampling rules for HTTP and RPC requests** configuration option to control which requests are captured when Adaptive Traffic Management is sampling. If a process monitored by OneAgent has a capture rate below 100%, you can prioritize specific HTTP or RPC requests to be captured more or less often relative to other request types. Increasing the trace capture rate for some requests automatically decreases it for others, so the ingested trace data volume stays roughly within the peak trace volume defined by your classic Full-Stack Monitoring license. For details, see [Adjust trace sampling for HTTP or RPC requests](#adjust-trace-sampling-for-web-requests).

## Quota per process

In Dynatrace Managed, the quota of new distributed traces/min that each process can send to Dynatrace is **1,000**. Because traffic management depends on your application architecture, network traffic is limited for high-volume entry points (such as a load balancer or NGINX) and spikes might occur.

### Adaptive capture control

You can manage the quota of new entry-point distributed traces captured per minute via **Adaptive capture control**, both on the environment level and per process or process group.

Adjusting adaptive capture control can help you in specific cases; for example, if a Dynatrace Managed environment for load testing consumes too many network, disk, and CPU resources, you'd instead use those resources for production monitoring. All analyses consider adjustments transparently without affecting service analysis features, except the distributed traces list or metrics.

To manage the quota of new distributed traces/min,

1. Go to **Cluster Management Console** > **Environments** and select your environement.
2. Optional In the **Cluster overload prevention settings**, you can set the environment quota of **Number of newly monitored entry point traces captured per process/minute**. The default value is 1,000, however, the environment quota can be increased to 100,000.
3. Select **Go to the environment**.
4. Go to **Settings** > **Server-side service monitoring** > **Deep monitoring** > **Adaptive capture control**.
5. Select **Global** or **Process group override**.

   You can reduce or increase the quota, respectively, to reduce the percentage of monitored incoming traffic or to ensure higher fidelity.

   If your environment quota is set to 100,000 and you set adaptive capture control to the highest value, OneAgent is effectively instructed to capture all requests, even rare ones, within high-volume environments.

Setting the environment quota and adaptive capture control values too high can cause resource shortages and increase hardware expenditures.

## Monitoring

You can use the preset dashboard **OneAgent Traces - Adaptive Traffic Management** to track usage and thresholds of Adaptive Traffic Management.

## Adaptive load reduction

Adaptive load reduction is a dynamic mechanism that targets environments with a high volume of traffic compared to their assigned host units. Because Dynatrace Managed environments can process a limited number of service calls per minute (depending on the node CPU amount and memory availability), this is particularly helpful for managing sporadic spikes in the volume of processed distributed traces.

When the amount of service calls that an environment can process is breached, adaptive load reduction is triggered:

1. New incoming distributed traces are skipped in a random fashion, reducing gradually the number of processed distributed traces.  
   Note that service calls of full distributed traces already in progress are not targeted.
2. The number of skipped distributed traces is taken into account to ensure stable statistical validity for all metrics, charts, baselining, and events.
3. You are informed about the reduction of processed data by

   * An alert message in the Dynatrace web UI: `Server [amount] activated adaptive load reduction`

   * A message in the distributed trace list: `[amount] more like this`

Data quality

Adaptive load reduction safeguards your Dynatrace environment from sporadic traffic spikes.

While occasional activation (for example, to cover spikes) will not harm the fidelity of your monitoring data, consistent use for intervals of 15 minutes or longer can impact the accuracy of your monitoring data and metrics because not all data is processed.

If your environment experiences frequent overloads, we recommend exploring long-term solutions.

Options include:

* Adding hardware and a [new Dynatrace Managed cluster node](/managed/managed-cluster/installation/add-cluster-node "Add a node to your Managed Cluster by downloading the installer, running it on the target host, and monitoring synchronization progress.") to provide your Dynatrace Managed cluster with the necessary resources to process the additional data.
* Adjusting OneAgent settings to reduce the incoming traffic.

These options should be considered whenever statistical accuracy of data capture is insufficient.

## Adjust trace sampling for HTTP or RPC requests

When you increase or decrease the sampling frequency of HTTP or RPC requests, these requests are captured more or less often relative to other request types.

* OneAgent version 1.331+ Reduction rules are always applied independent of the current OneAgent capture rate or adaptive trace sampling rate. This approach reduces trace volume more effectively, making it available for higherâpriority requests.
* OneAgent version 1.329 and earlier Reduction rules generally affect sampling only when the OneAgent module initiating the distributed trace captures less than 100% of traces.

### Effect of tracing deactivation on capture rate

Modifying trace sampling for HTTP or RPC requests does not change the overall capture rate for the process or the overall ingested trace data volume. However, if you deactivate tracing for specific HTTP and RPC requests, the capture rate is increased.

In all environments, there are transactions for which traces are of lower value. You can turn off tracing for specific HTTP and RPC requests completely at any time, freeing up trace volume for more important requests. This feature removes those traces completely from the capture rate calculation (they are no longer considered when computing the capture rate) and therefore leads to an overall increase in capture rate.

### Prerequisites

* For HTTP request trace sampling: OneAgent version 1.281+
* For RPC request trace sampling: OneAgent version 1.307+

### Available configuration scopes

You can configure web request trace sampling for the following [configuration scopes](/managed/manage/settings/settings-20#scope-and-hierarchy-of-settings "Introduction to the Settings 2.0 framework"): environment, host group, process group, Kubernetes cluster, and Kubernetes namespace.

* Any Dynatrace version For all traces in your environment.
* Dynatrace version 1.312+ For traces started within a particular host group, process group, Kubernetes cluster, or Kubernetes namespace. This is useful if you don't have environment permissions or want to modify trace sampling for a particular part of your environment.

### 1. Navigate to trace sampling configuration page

Navigate to the trace sampling configuration page depending on the entity for which you want to modify the sampling frequency of HTTP or RPC requests.

Environment

1. Go to **Settings** > **Server-side service monitoring** > **Trace sampling for HTTP requests** or **Trace sampling for RPC requests**.

Host group

1. Go to **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. From the navigation menu on the left, select **Trace sampling for HTTP requests** or **Trace sampling for RPC requests**.

Process group

1. Go to **Technologies & Processes** and choose a technology.

   Alternatively, go to **Hosts** and choose a host.
2. Find and select the required process group.
3. In the upper-right corner of the process group overview page, select **Settings**.
4. Select **Trace sampling for HTTP requests** or **Trace sampling for RPC requests**.

Kubernetes cluster or namespace

1. Go to **Kubernetes**.
2. Find and select the required Kubernetes cluster.
3. Go to the cluster or namespace settings page.

   * **Cluster**: In the upper-right corner of the cluster overview page, select **More** (**â¦**) > **Settings**.
   * **Namespace**: Find and select the required namespace, and then select **More** (**â¦**) > **Settings** in the upper-right corner of the namespace overview page.
4. Select **Trace sampling for HTTP requests** or **Trace sampling for RPC requests**.

### 2. Modify trace sampling

Adjust the trace sampling for your HTTP or RPC requests.

HTTP request

1. Select **Add URL**.
2. Choose how to adjust the trace sampling.

   * To never capture traces for the URL, regardless of the available trace volume, turn on **Disable tracing for matching HTTP requests**.
   * To increase or reduce the frequency of trace capture for the specific URL, set **Importance of a specific URL** to the required scaling factor.
3. To match the HTTP request, do one or a combination of the following:

   * Enter the URL path and select the comparison condition.

     Use wildcards (`**`) for URL paths with similar segments.

     For example, in `/api/product/**/detail`, all values between slashes are ignored; the path applies to both `/api/product/1/detail` and `/api/product/2/detail`.
   * Use the query parameters.

     1. Under **Query parameters**, select **Add item**.
     2. Enter a query parameter name.
     3. Enter the query parameter value, or turn on **Query parameter value is undefined**.
4. Optional To apply the scaling factor to specific HTTP methods, turn off **Any HTTP method**, and select the required HTTP methods.
5. Select **Save changes**.

RPC request

1. Select **Add RPC**.
2. Choose how to adjust the trace sampling.

   * To never capture traces for the RPC, regardless of the available trace volume, turn on **Disable tracing for matching RPC requests**.
   * To increase or reduce the frequency of trace capture for the specific RPC, set **Importance of a specific RPC** to the required scaling factor.
3. Specify the **Protocol**.
4. To match the RPC request, enter the name and the comparison condition of one or a combination of the following parameters:

   * **Remote operation name**
   * **Remote service name**
   * **Endpoint name**
5. Select **Save changes**.

### Use case examples

Check the examples below to understand how to properly adjust the trace sampling for your HTTP or RPC requests.

Example 1: Reduce capturing of a frequently executed health check request that provides values less than 60 times/minute

The following rule reduces the importance (by a factor of four) of requests that start with `_healthz`.

1. Navigate to the [**Trace sampling for HTTP requests** page for your environment](#trace-sampling-config-env).
2. Select **Add URL**.
3. From **Importance of a specific URL**, select **Reduce capturing by factor 4**.
4. Enter `/_healthz` for the URL path.
5. From **Path comparison condition**, select **Starts with**.
6. Turn on **Any HTTP method**.
7. Select **Save changes**.

Example 2: Never capture an HTTP OPTIONS request on web servers for a process group

The following rule ignores all requests (starting with `/`) that use `OPTIONS` as an HTTP method for a selected process group.

1. Navigate to the [**Trace sampling for HTTP requests** page for your process group](#trace-sampling-config-process-group).
2. Select **Add URL**.
3. Turn on **Ignore a specific URL**.
4. Enter `/` for the URL path.
5. From **Path comparison condition**, select **Starts with**.
6. Turn off **Any HTTP method**.
7. From the **HTTP method** list, turn on **OPTIONS**.
8. Select **Save changes**.
9. Optional Create a new rule for each process group that you want to target.

## FAQ

How does Adaptive Traffic Management affect charts, baselining, and alerting?

Usually not at all.

The shaping of traffic is accounted for transparently and done in a way that ensures statistical validity while capturing rare requests with high probability. All charts and analysis options show the total number of requests that your application processes with high statistical accuracy. You will not see a difference in charts or service call analysis data unless you're looking at a single distributed trace.

Does Adaptive Traffic Management affect service settings or (global) request monitoring settings?

No, Adaptive Traffic Management focuses only on the number of traces. Neither service settings nor (global) request settings are modified by Adaptive Traffic Management. Depending on the capture rate and [sampling](#sampling), a low-volume or unique request might not be captured. Service settings such as request naming rules and key request settings will apply only to captured traces.

Does Adaptive Traffic Management affect service metrics?

Yes, in a few cases, as service monitoring metrics are based on captured traces. The following are some known effects.

* For low-frequency requests in high-volume environments, [sampling](#sampling) and a low capture rate can impact the accuracy of metrics. Due to the low frequency of the requests, traces might be captured in a lower volume or not be captured at all. Consequentially some metrics values can't be collected. Note that this is reflected in service metric calculations to avoid distortions in charts.
* Because every single request is accounted for in charts with high resolution and in short timeframes, for high-volume services, [sampling](#sampling) and a low capture rate might impact the accuracy of metrics such as request count or error count. Conversely, the accuracy will statistically be better in charts with low resolutions and long timeframes.

Why can't I see a certain request?

If your Dynatrace Managed cluster is undersized or if a specific request you're interested in comes from a high-volume tier (more than 1,000 requests/min), Dynatrace might not be able to capture the request.

* You can increase the volume available for important requests by reducing the amount of traffic related to unimportant requests. To exclude unimportant requests from capture use [web request attributes](/managed/observe/application-observability/services/service-detection/service-detection-v1/set-up-request-naming#request-attributes-and-placeholders "Adjust request naming and define the operations your services offer.") and URL exclusion rules.
* You can also [increase the quota](#acc) of captured distributed traces.