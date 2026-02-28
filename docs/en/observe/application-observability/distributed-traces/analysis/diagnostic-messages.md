---
title: Treat diagnostic messages
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-traces/analysis/diagnostic-messages
scraped: 2026-02-28T21:24:48.887535
---

# Treat diagnostic messages

# Treat diagnostic messages

* 4-min read
* Updated on Jun 10, 2023

Captured distributed traces are the main source of data for Dynatrace DavisÂ® causal AI. Because Davis relies on high data quality and fidelity, certain standards must be met to analyze the collected data; all services, methods, timings, properties, and so on must be correctly captured and transmitted. If this doesn't happen, you'll be informed of the issue via a diagnostic message for the affected traces.

* In case the correct service can be determined, distributed traces with diagnostic messages are listed on the service's **Distributed traces** page, along with all other distributed traces related to the service.

  ![Distributed traces diagnostic message - capture error](https://dt-cdn.net/images/distributed-traces-capture-error-3112-189ed8979d.png)
* In case a related service can't be determined, for example, because of a missing service name or type, distributed traces are listed as **Unexpected services** in the list of services of the process for which distributed traces have been captured.

  Unexpected services may be caused by network issues (data lost in transition) or by the abrupt termination of the process (restart or scaling).

## Troubleshoot diagnostic messages

Via the content of diagnostic messages, you can understand the possible causes of missing capture or transmission of data and to what extent DavisÂ® AI can rely on the collected data. Sometimes diagnostic messages are symptoms of a setup issue that requires investigation.

To maintain good data quality, we recommend that you

* Use network error patterns to identify the source of a problem.

  For example, if all requests of a specific service have network-related errors, the cause may be a short-living process that isn't sending data to Dynatrace.
* Reduce the number of [request attributes](/docs/observe/application-observability/services/request-attributes "Understand what request attributes are and learn how to use them across all levels of all service-analysis views.") or change the definitions of [custom services](/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/custom-services "Define entry points (a method, class, or interface) for custom services that don't use standard protocols.") to reduce the number of requests.

## Truncation of trace data

A trace can be truncated because data isn't fully acquired, correlated, or visualized. This typically occurs when limits established to protect your environment's resources are exceeded. When trace data is truncated, you get a specific diagnostic message.

If you've configured [cross-environment tracing](/docs/observe/application-observability/distributed-traces/analysis/connect-environments "Analyze requests across environment boundaries."), data fetched from remote environments isn't truncated but aggregated.

While limits that protect your environment's resources can't usually be removed, you might influence truncation by intervening at the source of the problem. The following list includes some suggestions to help reduce the truncation of trace data.

* Reduce the number of nodes sent per trace, for example, by modifying custom services and OneAgent features active in your environment.

  OneAgent can send a limited number of nodes per trace. Once it runs into resource limitations, new nodes are no longer created. The trace is truncated at ingestion, and new incoming data isn't added to the trace. This can affect the correlation of entities and undermine your data quality.
* Investigate traces running for extended lengths of time.

  To protect your environment's resources, action is taken when traces run for extended lengths of time. For example, traces that are no longer active after running for 90 minutes are timed out, while traces for which the start time of the call is too far in the past are truncated. In both cases, new data isn't added to the trace. This can affect the correlation of entities and data quality.
* Investigate traces with limited or excessive amounts of data.

  + When trace data doesn't contain sufficient metadata on networks or not all nodes were received, correlating entities might be unsuccessful, leading to truncated traces.
  + When a call has too many in-progress dependencies or the trace has too many nodes, such a trace is truncated. We recommend investigating the related service and, in case of custom services, getting in touch with a Dynatrace product expert via live chat within your environment.
* Adapt the full-trace view to visualize the data you need.

  The full-trace view in Dynatrace is typically large enough to display the most important information for the entire trace. However, formatting can be modified to help you visualize all the data you need.