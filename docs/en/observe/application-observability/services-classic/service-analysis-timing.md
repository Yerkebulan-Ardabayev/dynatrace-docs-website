---
title: Service analysis timings
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-timing
scraped: 2026-03-06T21:12:16.263242
---

# Service analysis timings


* Classic
* Reference
* 5-min read
* Updated on Jul 24, 2023

Service analysis operates with many different timings, describing the behavior of the service. The table below provides an overview of such timings. Timings vary in different analysis types:

* DT: [Distributed traces](../distributed-traces/use-cases/segment-request.md#pp-code-level-tab "Enhance your distributed system performance by segmenting requests with slow response time via Service flow and analyzing their distributed traces.").
* RT: Response time.
* SF: Service flow.
* MH: Method hotspots.

Regardless of which analysis you're running, it is not guaranteed that you'll see all of the timings listed here. The actual timings you see depend completely on how you're running your services. For example, if the distributed trace runs completely on one host without any networking involved, you won't see any network-related times.

## Related topics

* Distributed Traces Classic
* Service flow
* Multidimensional analysis