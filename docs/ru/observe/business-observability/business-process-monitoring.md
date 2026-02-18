---
title: Business process monitoring
source: https://www.dynatrace.com/docs/observe/business-observability/business-process-monitoring
scraped: 2026-02-16T21:31:45.028451
---

# Business process monitoring

# Business process monitoring

* Latest Dynatrace
* Tutorial
* 3-min read
* Published Feb 19, 2025

Business processes are the automation backbone of modern businesses, and they must operate efficiently to meet business goals. Most business processes can impact customer experience, either positively or negatively. From procurement to order fulfillment, from customer onboarding to service request tracking, most organizations rely on hundreds, if not thousands, of business processes. These business processes depend on your IT systems to achieve their business goals efficiently and at scale.

## Introduction

Use Business Flow to monitor and optimize business processes. Gain real-time visibility into key performance indicators and detailed analytics to improve customer satisfaction, increase efficiency, and reduce cost.

With Business Flow, you can:

* Define the sequence of important process steps or process milestones, including branches and loops.
* Define business exceptions to report at each step.
* Analyze individual end-to-end process flows.
* Detect dropped or stalled process flows.
* Track process KPIs, including end-to-end process timing and inter-step delays

## Target audience

This article is intended for business analysts and process managers who understand how their businesses are performing in real time and look for optimal execution of their business processes. You should have a basic knowledge of how business events are captured and some domain knowledge of the business area you are trying to analyze.

## Prerequisites

Required

* Business events for each process step must be defined and active.
* Identify a unique identifier (correlation ID) that is common to all process steps (for example, `order\_id`). The name of the correlation ID may differ between steps; the value is used to connect steps into a single flow.

Recommended

* Identify business events that indicate incidents or business exceptions, such as credit card payment errors, product outages, shipping exceptions, or other non-IT process issues.
* Identify a business KPI of your choice (such as revenue) that can be extracted from a business event attribute.

## Use cases

### Track and report process KPIs

Business Flow reports three standard KPIs: Average duration, errors, and conversions. You can also add a business KPI of your choice.

In many cases, process duration is one of the most important indicators of process health. Many process optimization initiatives focus on reducing delays. In Business Flow, the average duration KPI represents end-to-end elapsed time. For each step, the average duration to the subsequent step(s) is also reported. These values help to focus improvement efforts on process "hot spots."

See a screenshot of Business Flow Details.

![Track and report process KPI](https://dt-cdn.net/images/bizflow-track-and-report-process-kpis-1-1920-2393a669bd.png)

See a screenshot of KPIs over time.

![Track and report process KPIs over time](https://dt-cdn.net/images/bizflow-track-and-report-process-kpis-2-1920-c383a1ab52.png)

### Analyze an individual process flow

You can analyze any process flow in detail.

For in-progress flows at any step, select the step box in the main tree panel. From the right-hand panel, choose **Explore**, then select the step of interest.

![Explore individual process flow](https://dt-cdn.net/images/bizflow-analyze-an-individual-process-flow-1-1920-fdfe34db1b.png)

You can open the resulting table in a Notebook for deeper exploratory analytics.

![Analyze an individual process flow](https://dt-cdn.net/images/bizflow-analyze-an-individual-process-flow-2-1920-c106d3b3fa.png)

### Analyze dropped or stalled process flows

When a process step takes longer than normal to reach a subsequent step, it is flagged as a drop. It may be stuck permanently, or it may simply be experiencing an unusually long delay.

For a list of the dropped flows at any step, select the step box in the main tree panel. In the right panel, you can filter to only show dropped.

![Explore dropped or stalled process flows](https://dt-cdn.net/images/bizflow-analyze-dropped-or-stalled-process-flows-1-1920-465ff57c95.png)

### Analyze business exceptions

For business exceptions, select a step box in the main tree panel that shows business exceptions; from the right-hand panel, filter by Business exceptions, then select the unique flow of interest.

![Explore Business exceptions ](https://dt-cdn.net/images/bizflow-analyze-business-exceptions-1-1920-b9d0d38fba.png)

![Analyze Business exceptions on detail](https://dt-cdn.net/images/bizflow-analyze-business-exceptions-2-1920-970495e9c7.png)

## Conclusion

Hereâs a brief list of some common business processes. Your organization will have a large portfolio of business processes, most of which are likely unmonitored. See a sampling list of such processes below.

* Customer support process
* Order processing
* Trade settlement
* Customer or employee onboarding or offboarding
* Procurement process
* Payment process
* IT service requests
* Loan approval
* Insurance claims processing
* Patient discharge
* Citizen requests for public services
* Free trial activation
* Quality assurance
* Subscription service fulfillment