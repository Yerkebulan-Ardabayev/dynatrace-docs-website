---
title: Service analysis timings
source: https://www.dynatrace.com/docs/observe/application-observability/services-classic/service-analysis-timing
scraped: 2026-02-23T21:20:30.191036
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

Time

Appears in

Description

Response time

DT  
SF

The total execution time of the first node of a distributed trace.

* Server side The time between moments when the distributed trace is started on the server side and when the response is sent back to the client.
* Client side The time between moments when the client triggers the request and receives the response.

Response time

RT

The total execution time of the method.

* Server side The processing time of the method.
* Client side The time between moments when the client triggers the request and receives the response.

Processing time

DT  
RT

The duration of the distributed trace from start to end.

It is the *wall-clock time* (difference between start and end time), not the sum of all asynchronous executions.

Execution time

RT

The total time taken to execute the code.

It is the **sum of all asynchronous executions**, so it might be longer than the processing time.

Suspension

DT  
RT

The time during which any code execution is halted. It is usually caused by garbage collection.

Wait time

DT

The time during which the code actively waits for something (for example, `Object.wait()` or a similar functionality).

Lock wait

RT

The time during which the code is blocked. It usually caused by wait time prior to entry into a synchronized code block or by wait time to acquire a spinlock.

Active wait

RT

The time during which the code in *this node* is waiting for something. The wait caused by child calls is not included.

Lock time

DT

The time during which the code is blocked by waiting for a synchronous code block.

Network I/O

DT  
RT

The time during which the code is actively waiting for *native* network functions (for example, `java.net.SocketInputStream.socketRead0`).

For response time analysis, the wait caused by child calls is not included.

Disk I/O

DT  
RT

The time during which the code is actively reading from or writing to a disk or waiting for disk input/output.

For response time analysis, the wait caused by child calls is not included.

Total I/O

-

In a node, this is **the sum of Network I/O and Disk I/O**.

When these metrics aren't available, and if the node is the direct parent of a synchronously invoked child service that isn't a custom service, the node Total I/O can be estimated as **the node Duration minus the node CPU Self time**.

CPU time

DT  
RT

The time during which the CPU executes code related to the distributed trace. The measurement is provided by OneAgent.

Self time

DT  
RT

The processing time of a particular node in the distributed trace.

Other

DT

Any unclassified fraction of the self time.

Elapsed time

DT

The time between executions, from when the distributed trace is created to when the method enters.

Duration

DT

Timeframe that represents the duration of a node, including its synchronous children nodes, from its start time to its end time.

Code execution

MH

Percentage of measured samples in which the method code is actively executed.

Disk I/O

MH

Percentage of measured samples in which the method is actively reading from or writing to a disk or waiting for disk input/output.

Network I/O

MH

Percentage of measured samples in which the method is actively waiting for *native* network functions.

Waiting

MH

Percentage of measured samples in which the method is actively waiting for something (for example, `Object.wait()` or a similar functionality).

Locking

MH

Percentage of measured samples in which the method is blocked by waiting for a synchronous code block.

## Related topics

* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")
* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Multidimensional analysis](/docs/observe/application-observability/multidimensional-analysis "Configure a multidimensional analysis view and save it as a calculated metric.")