---
title: Service analysis timings
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-timing
scraped: 2026-02-27T21:10:14.824718
---

# Service analysis timings

# Service analysis timings

* Reference
* 5-min read
* Updated on Jul 24, 2023

Service analysis operates with many different timings, describing the behavior of the service. The table below provides an overview of such timings. Timings vary in different analysis types:

* DT: [Distributed traces](/docs/observe/application-observability/distributed-traces/use-cases/segment-request#pp-code-level-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").
* RT: [Response time](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.").
* SF: [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.").
* MH: [Method hotspots](/docs/observe/application-observability/services-classic/service-response-time-hotspots "Identify the activities that consume the most response time for each service.").

Regardless of which analysis you're running, it is not guaranteed that you'll see all of the timings listed here. The actual timings you see depend completely on how you're running your services. For example, if the distributed trace runs completely on one host without any networking involved, you won't see any network-related times.

## Related topics

* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Multidimensional analysis](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")