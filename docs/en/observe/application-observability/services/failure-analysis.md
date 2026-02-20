---
title: Failure Analysis
source: https://www.dynatrace.com/docs/observe/application-observability/services/failure-analysis
scraped: 2026-02-20T21:07:46.044501
---

# Failure Analysis

# Failure Analysis

* Latest Dynatrace
* Tutorial
* 4-min read
* Updated on Oct 23, 2025

Modern distributed systems generate complex failure patterns that require fast, reliable analysis.

**Failure Analysis** in Dynatrace addresses this need by offering a focused experience for investigating service failures, helping you uncover patterns and contributing factors across your environments.

## What is Failure Analysis?

In Dynatrace, a failure refers to any request or transaction that does not complete successfully. Failures may result from HTTP errors, unhandled exceptions, or custom-defined conditions that indicate unexpected behavior.

**Failure Analysis** helps you detect, investigate, and resolve service failures faster and more effectively. It modernizes the Dynatrace experience by introducing a user-focused interface and new capabilities that support both reactive and proactive troubleshooting.

You can access **Failure Analysis** directly from the problems-specific drill-down options when a failure rate increase is detected, or explore it manually from the **Failures** tab in ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

This feature is designed for SREs, developers, and DevOps teams who need fast, actionable insights into service health and failure patterns.

**Failure Analysis** provides:

* A clear view of why service requests are failing
* Advanced filtering by service, endpoint, failure type, and timeframe
* In-depth analysis and visual comparison of failure trends across time periods, including precise insights into how failure counts evolve and what causes them
* Contextual logs linked to failed requests
* Insights into related outgoing calls and database failures

## Key capabilities

### Core capabilities

* **Advanced filtering**  
  Use Dynatrace filters to narrow down failures by attributes such as service, endpoint, failure type, and more.
  Timeframe filters allow users to isolate failures within specific periods or compare across time ranges.
* **Comparison mode**  
  Visually compare failure rates across different timeframes to identify trends, assess the impact of changes, or validate fixes.
  Interactive annotationsâlabels displayed above the graph, provide additional context for specific timeframes when hovered over, highlighting key failure events for deeper insights.
* **Contextual log integration**  
  View logs directly associated with failed service calls (via trace/span IDs).
  This provides essential context for understanding the root cause.
* **Outgoing call analysis**  
  Investigate failures in downstream dependencies such as HTTP requests, gRPC calls, or third-party APIs.
  Dynatrace detects failed states based on HTTP/gRPC response codes, span status, and the presence of exceptions within traces.
* **Database failure insights**  
  Analyze failed database interactions, including query-level visibility for supported databases.
  This helps identify backend issues contributing to service instability.
* **Exploratory and contextual access**  
  Access the Failure Analysis page with or without predefined context. When accessed via the problems-specific drill-down options, filters are pre-applied.
  Users can also explore failures manually by adjusting filters.

### Integration with Dynatrace

* Embedded in the ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** application as a new **Failures** tab
* Integrated into the **Dynatrace problems-specific drill-down options** when failure rate increases are detected as [root causes](/docs/dynatrace-intelligence/davis-problems-app#streamline-problem-resolution-with-problems-specific-drill-down-options "Use the Problems app to quickly get to the root cause of incidents in your environment.")
* Replaces the legacy **Failure Analysis** page for DPS customers

## Access and navigation

The new **Failure Analysis** feature is available as a dedicated **Failures** tab in Dynatrace **Services**. It is designed to support both contextual and exploratory workflows.

### How to access

* **Contextual Access via problems-specific drill-down options**  
  When a failure rate increase is identified as the root cause of a problem, you are directed to the **Failure Analysis** page with pre-applied filters based on the affected service and endpoint.
* **Exploratory Access**  
  You can also navigate to the **Failures** tab manually and adjust filters to explore failures across services, endpoints, and timeframes.

### Prerequisites

* DPS license
* SaaS environment with the new Dynatrace platform enabled

## Get started

To get started troubleshooting a service failure

1. Go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** and select the **Failures** tab.
2. Apply filters for service, endpoint, and timeframe.
3. Use **compare to** (for example, select `Same timeframe last week`) to detect anomalies.
4. Open the log view to examine logs emitted during failed traces.
5. Check outgoing calls and database queries.

## Limitations

While the new **Failure Analysis** experience introduces significant improvements in usability and functionality, you may occasionally experience slower load times when accessing **Failure Analysis** in environments with high trace volumes or complex service architectures. Dynatrace is actively monitoring performance and continuously optimizing the experience.

## Related resources and next steps

To deepen your understanding of failure detection and troubleshooting in Dynatrace, explore the following resources:

* [Configure service failure detection](/docs/observe/application-observability/services/service-detection/service-detection-v1/configure-service-failure-detection "Discover which service error types Dynatrace automatically detects and learn how to adjust failure detection settings to meet your specific requirements.")
* [Root cause analysis concepts](/docs/dynatrace-intelligence/root-cause-analysis/concepts "Get acquainted with root cause analysis concepts.")
* [Triage and investigate incidents in the Problems app](/docs/dynatrace-intelligence/davis-problems-app "Use the Problems app to quickly get to the root cause of incidents in your environment.")

### Join the conversation

Weâd love to hear your feedback and questions about the new **Failure Analysis** experience.  
[Visit the Feedback Channel in the Dynatrace Communityï»¿](https://community.dynatrace.com/t5/Feedback-channel/Feedback-channel-for-the-new-Failure-Analysis-feature/td-p/282050)