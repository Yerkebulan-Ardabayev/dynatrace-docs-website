# Документация Dynatrace: dynatrace-intelligence/root-cause-analysis
Язык: Русский (RU)
Сгенерировано: 2026-02-19
Файлов в разделе: 3
---

## dynatrace-intelligence/root-cause-analysis/concepts.md

---
title: Root cause analysis concepts
source: https://www.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis/concepts
scraped: 2026-02-19T21:13:00.277024
---

# Root cause analysis concepts

# Root cause analysis concepts

* Latest Dynatrace
* Explanation
* 11-min read
* Updated on Jan 28, 2026

As dynamic systems architectures increase in complexity and scale, IT teams face mounting pressure to quickly detect and react to business-critical incidents across their multi-cloud environments. Incidents might affect one or more IT components, ultimately leading to large-scale outages that take down critical business services and applications. Such services and applications (for example, accounting systems or web shops) consist of many different components that depend on each other to work reliably and to deliver excellent user experience. If a critical component fails, the ripple effect negatively influences many other dependent components, triggering a large-scale incident.

Concepts such as Service Level Objectives (SLOs) establish a framework of trust between individual components and shift responsibility toward the teams building and owning those components. While SLOs are great to gain a machine-processable understanding of what the normal boundaries of operation for individual services are, they fail to deliver a deeper understanding on the cause of the problem and the best remediation.

Root cause analysis aims to fill this gap by using all available context information to evaluate an incident and determine its precise root cause. It is equally important to evaluate the impact of an incident, allowing the operations team to quickly triage the incident and reduce the mean time to repair (MTTR).

This page introduces the following core concepts:

[Incidents and problems](#incidents-problems)  
[Davis Events](#events)  
[Root cause analysis](#root-cause-analysis)  
[Fault tree analysis](#fault-tree-analysis)  
[Impact analysis](#impact-analysis)  
[Problem lifecycle](#problem-lifecycle)  
[Problem timing](#problem-timing)  
[Duplicate problems](#duplicate-problems)

## Incidents and problems

An **incident** is an abnormality in your environmentâin an application, infrastructure, and so on. A **problem** is an entity that represents the incident in Dynatrace. A problem is the result of automatic Dynatrace Intelligence root cause and impact analysis of an incident. Problems (just like underlying incidents) can span across multiple dependent components, sharing the same impact and root cause.

A problem might result from single or multiple Davis events occurring simultaneously within the same topology, which is often the case in complex environments. To prevent over-alerting, Dynatrace correlates all Davis events with the same root cause into a single problem.

All detected problems are listed in the problem feed and Dynatrace automatically updates them in real time with all incoming Davis events and findings.

## Davis events

Events represent different types of singular anomalies, such as a metric breaching a threshold, baseline degradations, or point-in-time Davis events, such as process crashes. Dynatrace also detects and processes informational Davis events such as new software deployments, configuration changes, and other Davis event types.

Dynatrace ingests and stores Davis events from multiple sources. Those events can trigger root cause analysis, an automation, or serve as raw data for dashboards and reports. Together with logs, metrics, and traces, Davis events provide the input for root cause and impact analysis.

Most Davis events don't indicate abnormal or unhealthy states, therefore only a small fraction of Davis events are considered within problems.

## Root cause analysis

Root cause analysis uses all the available context informationâsuch as topology, transaction, and code-level informationâto identify Davis events that share the same root cause and impact.

To identify the root cause of problems, time correlation alone is not sufficient. Dynatrace follows a context-aware approach, detecting interdependent Davis events across time, processes, hosts, services, applications, and both vertical and horizontal topological monitoring perspectives. This approach combines multiple standalone anomalies into a single consistent problem, dramatically reducing the alert load.

The image below illustrates how Dynatrace Intelligence analyzes all horizontal and vertical dependencies of a problem. In this example, the application shows abnormal behavior, while the underlying vertical stack operates normally. The analysis follows the transactions of the application, detecting dependency on a service (`Service 1`) that also shows abnormal behavior. In turn, all of the service's dependencies behave abnormally as well and are part of the same problem.

![Correlation diagram](https://dt-cdn.net/images/correlation-diagram-1256-6a1abf3bdb.png)

Dynatrace Intelligence includes all relevant abnormalities and ranks all root cause contributors, determining which is the primary negative impact. You can drill down to the component level and analyze the root cause down to the source code level. For example, Dynatrace can show failing methods within your service code or high GC activity on underlying Java processes.

Why is context correlation important?

A problem is rarely a one-time Davis event. Often they appear in regular patterns and are symptoms of larger issues within your environment. If multiple entities depending on an affected component experience issues around the same time, all those entities are included into root cause analysis.

Time correlation alone is, however, is not enough to identify the root cause of many application and service problems. Consider, for example, a simple time correlation in which the `Booking` service calls the `Verification` service, and the `Verification` service experiences a slowdown. The first Davis event in the problem evolution is a slowdown of the `Verification` service. Subsequently, the `Booking` service experiences a slowdown too, caused by dependency on the `Verification` service. In this case, time correlation works well in detecting the root cause of the problem: a slowdown of the `Verification` service. However, this is an oversimplified description of what happens in real applications.

What if the Davis events in the problem evolution sequence are more nuanced and open to interpretation? What if, for example, the `Booking` service has a long history of performance problems? Without the complete context, it becomes impossible to decisively conclude that the slowdown of the `Booking` service is caused by the slowdown of the `Verfication` service. There is a possibility that `Booking` service is experiencing another performance issue, unrelated to the `Verfication` service.

Dynatrace Intelligence root cause analysis uses all related monitoring data to identify interdependencies between the problem and other components that took place around the same time and within a dependent topology. That is, all topological dependencies, vertical and horizontal, are part of the analysis.

## Fault tree analysis

Dynatrace Intelligence context model is built on known dependency information from Smartscape, OneAgent, and cloud integration. Dynatrace Intelligence uses this information to quickly conduct a fault tree analysis to analyze millions of dependencies and arrive at the most probable root cause of a problem.

## Impact analysis

The impact of a problem is equally as important as its root cause, since both represent essential information for triaging and remediating the underlying incidentâthe problems that threaten your company's business most have higher priority to resolve.

Impact analysis identifies which applications' entry-point services are affected by an incident and the size of the overall "blast radius" in terms of the total number of affected entities. Impact analysis also delivers the number of affected SLOs as well as the number of potentially affected real users.

Ultimately, impact analysis strives to determine how badly the incident affects your business.

## Problem lifecycle

Dynatrace opens a problem upon receiving the first indicator of an incident, which is typically a single Davis event representing abnormal behavior, such as a service slowdown, node saturation, or a workload crash and restart.

A problem automatically follows a lifecycle and remains in the active state while there is still an affected entity in the unhealthy or abnormal state, mostly indicated by an active Davis event.

In the following scenario, a problem that has a performance incident in the infrastructure layer is the root cause.

![Problem lifespan](https://dt-cdn.net/images/problemlifespan-2275-dfec42340b.png)

1. Dynatrace detects an infrastructure-level performance incident and creates a new problem for tracking purposes. A notification is sent out as well.
2. After a few minutes, the infrastructure problem leads to the appearance of a performance degradation problem in one of the application's services.
3. Additional service-level performance degradation problems begin to appear. What began as an isolated infrastructure-only problem has grown into a series of service-level problems that each have their root cause in the original incident in the infrastructure layer.
4. Eventually, the service-level problems begin to affect the user experience of customers who are interacting with the application via desktop or mobile browsers. At this point in the problem life span, you have an application problem with one root cause in the infrastructure layer and additional root causes in the service layer.
5. Because Dynatrace understands all the dependencies in your environment, it correlates the performance degradation problem your customers are experiencing with the original performance problem in the infrastructure layer, facilitating quick problem resolution.



## Problem timing

The Dynatrace Intelligence root-cause engine collects all Davis events that belong to the same incident. As a result, Dynatrace Intelligence causal AI generates a problem that references all incident-relevant information such as individual Davis events that were detected on the impacted topology graph.

The following shows how two individual Davis events are analyzed within one problem generated by Dynatrace Intelligence causal AI.

* Each Davis event comes with its own start and end timestamps.
* Each Davis event producer uses various observation sliding time windows, which we call event analysis time (shown in yellow).

![Problem timing](https://dt-cdn.net/images/problem-lifecycle-drawio-2d5919c652.svg)

Consider an example of a metric Davis event configured to use a five-minute sliding window where three one-minute samples need to violate the threshold to raise a Davis event. In that case, the metric starts violating the threshold three minutes before the timestamp when the event is raised.

* The **event start analysis timestamp** is the earliest point in time when the violating state was observed.
* The **event end analysis timestamp** is the point in time after all necessary violation samples are collected and a problem is opened.
* Because each Davis event involved in the problem uses a sliding window, each problem has a trailing period during which a closed problem might be reopened. This is called the **reopening period**, and its maximum length is 30 minutes.
* If a problem remains open for longer than 90 minutes, no new events are merged into it after the 90-minute point. This prevents Dynatrace Intelligence causal AI from collecting unrelated information for long-lasting incidents (for example, a synthetic test constantly failing and keeping problems open for weeks).

#### Summary of the problem lifecycle timings:

* Individual Davis events use variable analysis sliding windows.
* A problem is raised at the **event end analysis timestamp**.
* A problem lifespan is defined by the lifespans of individual Davis events in the problem.
* A problem is closed when all Davis events in the problem are closed.
* A closed problem can be reopened during a reopening period of 30 minutes.
* If a problem lasts for longer than 90 minutes, no new Davis events will be merged after the 90-minute pointâa new problem will be raised instead.
* If the time gap between creation (start timestamp) of the first Davis events is longer than 5 minutes, the Davis events won't be merged into the same problem. Instead, they will be identified as two different problems.

## Duplicate problems

The detection and analysis of a large-scale incident always requires a balance between fast alerting and having a complete picture of the situation. Data collection is asynchronous by nature due to different observation windows, different synthetic check schedules, and different latencies of information originating from various data sources.

The asynchronous processing of incoming information leads to situations where root-cause detection identifies two problems that share the same root cause.

* At the time of detection, the root cause analysis might lack the necessary information to connect both problems into a single incident.
* After the delayed information is considered, and one main problem is identified, other identical problems are marked as duplicates (`dt.davis.is_duplicate=true`).

Duplicates could be avoided entirely by waiting for a longer period (for example, 30 minutes) to receive all possible information, but this would delay alerts to the operation teams.

Due to the criticality of real-time alerting, potentially incomplete information and problem duplicates are accepted to allow the fastest possible alerting.

## Problem processing state

After Dynatrace Intelligence causal AI detects a problem, it enters the `Processing` state. This means that the causal AI analyzes the Davis event to see if it needs to be merged into a more significant problem. The `Processing` state aims to avoid duplicate issues and false alarms, so no alerts are sent until the state changes. Analysis and information gathering necessary for causal AI to make a decision usually take up to 3 minutes.

Below, you can find the example of a problem in the `Processing` state.

![Detected Problem going through the "Processing" state](https://dt-cdn.net/images/problem-processing-state-934-2c9e3ab22e.png)

If you want to receive alerts immediately after the problem is detected, you can use Custom alert with [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace"). In this case, the Davis event flags `dt.davis.trigger_delay` and `dt.davis.analysis_time` will be set to `0`. The problem won't enter the `Processing` state, and no causal AI analysis will be performed.

Alternatively, you can set the processing state per Davis event source in [Log events](/docs/analyze-explore-automate/logs/lma-analysis "Explore log data with a log viewer or create custom attributes, log events, and metrics to process and analyze your log data in Dynatrace.") configuration.

---

## dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation.md

---
title: Event analysis and correlation
source: https://www.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation
scraped: 2026-02-19T21:28:53.201532
---

# Event analysis and correlation

# Event analysis and correlation

* Latest Dynatrace
* Explanation
* 9-min read
* Updated on Jan 28, 2026

Events represent different types of singular anomalies, such as a metric breaching a threshold, baseline degradations, or point-in-time events, such as process crashes. Dynatrace also detects and processes informational events such as new software deployments, configuration changes, and other event types.

Dynatrace ingests and stores events from multiple sources. Those events can trigger root cause analysis, an automation, or serve as raw data for dashboards and reports. Together with logs, metrics, and traces, events provide the input for root cause and impact analysis.

## Event correlation

Event correlation automates the analysis of the flood of individual events coming from thousands of various sources and tools. It supports events coming from OneAgent, external alerting tools, cloud platforms, and hundreds of observability integrations available through Dynatrace Hub.

The goal of event correlation is to extract problems from incoming events and derive actionable insights, allowing your teams to remediate incidents quickly.

## Event processing and analysis

Event processing and analysis in Dynatrace is a multi-step process that, from incoming events, raises problems, showing the root cause and business impact. It includes the following steps:

* [Ingestion](#ingest)
* [Normalization](#normalization)
* [Topology creation](#topology-creation)
* [Aggregation](#aggregation)
* [Deduplication](#deduplication)

![Event ingestion](https://dt-cdn.net/images/event-ingest-1624-fe34b0377c.png)

### Event ingestion

As a full-stack observability platform, Dynatrace offers a wide spectrum of event sources, including OneAgent, built-in integrations, and ingestion from third-party tools. For more information, see [Ingest dataï»¿](https://dt-url.net/d003q22).
Latest Dynatrace also offers OpenPipeline for your ingestion purposes. For more information, see [OpenPipeline](/docs/platform/openpipeline "Scale Dynatrace platform data handling with Dynatrace OpenPipeline.").

### Event normalization

Event normalization transforms all ingested events into the same semantic format, which allows Dynatrace Intelligence causal AI to correlate this data.

In event normalization, basic event property constraints are evaluated to make sure, for example, that:

* Event creation time is valid
* Event type is valid
* Names of event properties are unique

Normalization also ensures that incoming event properties are mapped correctly to the Dynatrace Semantic Dictionary.

If the event source attached references to existing entities, normalization ensures that these references are correctly mapped to your Smartscape topology.

### Topology creation

[Smartscape topology](/docs/analyze-explore-automate/smartscape-classic "Learn how Smartscape Classic visualizes all the entities and dependencies in your environment.") is a real-time representation of all the causal relationships within a running software environment, including deployment information as well as highly dynamic trace relationships. The topology is automatically created and updated from ingested data such as metrics, events, logs, and traces.

All the built-in technology support in Dynatrace comes with automatic topology creation capabilitiesâyou don't have to configure anything manually. Moreover, you can use custom topology extraction to automatically create the topology and relationships from ingested data such as events. Custom topology creation works independently from OneAgent and doesn't even require a running OneAgent instance. You can easily implement your own domain-specific models based on the ingested data.

To learn how to implement a custom topology model, see [Custom topology model](/docs/ingest-from/extend-dynatrace/extend-topology "Ensure that all incoming observations are context-rich and analyzed in the context of the monitored entities they relate to.").

### Aggregation

Aggregation collects and routes all incoming data from various sources into a single location. For example, it consolidates events, logs, metrics, and traces of a Kubernetes workload and presents it in a single workload-related location.

Dynatrace aggregates data on top of the dynamically created topology. Every observed entity has a dedicated entity page summarizing all collected data in a single location, ensuring a consistent view of data from multiple sources.

Additionally, the topology enables dynamic listing of all related entities in that view. For example, a host can show a list of disks, network interfaces, and process group instances running on the host.

### Deduplication

Deduplication attempts to group multiple events into a unified problem where all the events share the same root cause. For example, a single failing backend service can cause hundreds of upstream services to report violation events. Deduplication automatically groups all those events into a single problem. By default, Dynatrace deduplicates events on source, over time, and on causal topology.

#### Deduplication on event source

In deduplication on event source, events are grouped when they are of the same semantic type and from the same source. (Note that "source" here means the monitored entity reporting the event, not the tool that captured the event).

The image below shows an example where three different tools report three events of the **CPU saturation** semantic type from the same source (**Server-23**) at the same time. In this case, causal AI deduplicates all three events into a single problem. The same logic applies to all entity types in Dynatrace.

![Event deduplication on source](https://dt-cdn.net/images/event-deduplication-source-606-42cfeaeb29.png)

#### Deduplication over time

In deduplication over time, events are grouped when they are of the same type and from the same source, but with slightly different start times.

Dynatrace anomaly detection offers a 3-out-of-5-minutes observation time window to keep events active during detected anomalies. The observation window prevents noise from multiple single events in case of anomaly fluctuation. You can adapt the sensitivity of the observation window. Increasing sensitivity produces more noise, decreasing leads to events that stay open for longer. Deduplication over times further reduces the event noise by grouping the same violation events into a single problem.

The image below shows an example in which three **CPU saturation** events fluctuate over time. Causal AI deduplicates them into a single problem.

![Event deduplication over time](https://dt-cdn.net/images/event-deduplication-time-606-d002576297.png)

#### Deduplication over the causal topology

In deduplication over the causal topology, events are grouped if they were reported for the same situation. The "same situation" here means that all those event sources are part of a causal graph within the Smartscape topology. The causal graph can include the vertical deployment software stack or the horizontal service-to-service call relationships.

The image below shows an example where a frontend service, directly and indirectly, calls three other services. All those services show a slowdown event around the same time. causal AI analyzes the causal topology of those four services and concludes that the four events belong to the same anomaly, so causal AI groups the four events into a single problem.

![Event deduplication over topology](https://dt-cdn.net/images/event-deduplication-topology-606-eca1a0f402.png)

Note that the causal topology can span hundreds of entities where their events vary over time due to individual observation windows and load situation.

Deduplication of events based on the causal topology is a highly sophisticated process that, due to its nature, already belongs to the [root cause analysis](#root-cause) step.

### Custom-defined event correlation



While event correlation and deduplication are fully automatic, some use cases require more fine-grained control of deduplication. To achieve that, you can use Dynatrace Intelligence control properties of ingested events. For example, **dt.event.allow\_davis\_merge** defines whether Dynatrace Intelligence can merge events into a larger problem. Such properties are agnostic to the ingestion channel. See the list of available properties below.

Property

Type

Description

**dt.event.allow\_davis\_merge**

Boolean

The event can be merged into an existing problem (`true`), or a new problem must be created for it (`false`).

**dt.event.allow\_frequent\_issue\_detection**

Boolean

Dynatrace Intelligence frequent issue detection is active (`true`) or inactive (`false`).

If frequent issue detection is active, Dynatrace Intelligence can mute frequently occurring events, preventing event noise.

**dt.event.allow\_entity\_remapping**

Boolean

Event remapping is active (`true`) or inactive (`false`).

If remapping is active, Dynatrace Intelligence can remap the incoming event to a new entity type extracted from event properties.

**dt.event.is\_rootcause\_relevant**

Boolean

Dynatrace Intelligence can (`true`) or can't (`false`) consider the event in root cause analysis.

**dt.event.suppress\_problem**

Boolean

Problems suppression is active (`true`) or (`false`) inactive.

If suppression is active, Dynatrace Intelligence doesn't raise a problem and doesn't trigger event correlation and deduplication for the event. The event is stored and visualized in Dynatrace, but no problem is raised and analyzed based on it.

**dt.event.timeout**

String

The timeout (in minutes) of the event. It defines the time period until a refresh must arrive from the event source. If no refresh is received, the event is closed with the change reason `TIMED_OUT`.

Additionally, the processing of events can be influenced by the event sender or the source using `event.davis` field defined in the Semantic Dictionary. For more information, see [Semantic Dictionary](/docs/semantic-dictionary/model/davis#davis-ai-events "Get to know the Semantic Dictionary models related to Davis AI.").

## Root cause analysis

Root cause analysis automatically evaluates all captured and ingested information and highlights entities within the causal topology identified as the root cause of a complex situation.

During the analysis, causal AI traverses the causal topology, visits each affected entity, and evaluates all the findings, such as events and their severities. In addition, Dynatrace Intelligence root cause detection triggers on-demand analyses of metrics from the affected entities to identify abnormal behavior by automatically detecting metric change points.

Metric change point detection not only confirms or rejects metric-based events, but also discovers additional unknowns in metrics without an active custom alert.

After all related problems are identified, a ranking algorithm identifies the highest-ranking root cause candidate. The highest-ranking entity, along with its vertical stack, is presented as the root cause of the problem.

Root cause analysis differences between the previous Dynatrace and the latest Dynatrace

In the latest Dynatrace, a Davis problem in Grail might, in some cases, have more affected entities compared to the corresponding problem in the previous Dynatrace. This current approach provides a more detailed and accurate representation of the problem's impact.

* In the previous Dynatrace, during root cause analysis, any change point findings on entities without events were not treated as an affected entity.
* In the latest Dynatrace, all change point findings are ingested to Grail as Davis events.

This difference can become apparent when, for example, comparing health tile results in Dashboards Classic to the corresponding results in the latest Dynatrace.

## Business impact

In addition to finding the root cause of the problem, Dynatrace Intelligence traverses the causal graph in reverse to find all affected entry point applications and services. These entry points are also part of the affected topology and are touch points for real user experience.

Business impact analysis shows the number of potentially affected real users (collected from the incoming traces), the number of traces, and their service endpoints. It also provides a statistical evaluation of how strongly the individual endpoint and user actions are affected by the problem.

---

## dynatrace-intelligence/root-cause-analysis.md

---
title: Root cause analysis
source: https://www.dynatrace.com/docs/dynatrace-intelligence/root-cause-analysis
scraped: 2026-02-18T21:23:18.710933
---

# Root cause analysis

# Root cause analysis

* Latest Dynatrace
* Explanation
* 1-min read
* Updated on Jan 28, 2026

Dynatrace Intelligence causal AI root cause analysis automatically evaluates all captured and ingested information and highlights entities within the causal topology identified as the root cause of a complex situation. It offers a context-aware approach that uses available context information, such as the code-level information topology, to determine the precise cause of the issue.

## Use cases

* Save time by including all relevant anomalies and ranking root cause contributors to determine the primary cause.
* Reduce the alert load by combining multiple connected anomalies into a single problem.
* Improve the precision of root cause analysis using all the available data from multiple sources.

[#### Root cause analysis concepts

Get acquainted with root cause analysis concepts.

* Explanation

Read this explanation](/docs/dynatrace-intelligence/root-cause-analysis/concepts)[#### Event analysis and correlation

Gain an understanding of the Events section on each host, process, and service overview page.

* Explanation

Read this explanation](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation)[#### Detection of frequent issues

Understand how Dynatrace detects and manages recurring problem patterns as frequent issues.

* Explanation

Read this explanation](/docs/dynatrace-intelligence/root-cause-analysis/detection-of-frequent-issues)

---
