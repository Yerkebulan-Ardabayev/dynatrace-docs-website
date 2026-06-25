---
title: Service-Level Objectives basics
source: https://docs.dynatrace.com/managed/deliver/service-level-objectives-classic/slo-basics
scraped: 2026-05-12T11:38:25.539308
---

# Service-Level Objectives basics

# Service-Level Objectives basics

* Explanation
* 2-min read
* Updated on Mar 25, 2024

Dynatrace provides all the necessary real-time information that your **Site-Reliability Engineering (SRE)** teams need to monitor their defined objectives.

An SRE team is responsible for finding good **service-level indicators** (**SLIs**) for a given service in order to closely monitor the reliable delivery of that service.
SLIs can differ from one service to the other, as not all services are equally critical in terms of time and error constraints.  
Dynatrace offers more than 2000 different metrics that are ready for use as dedicated SLIs.

Once the SRE team has selected a collection of indicator metrics, what remains is to define and monitor the operational goal within a **service-level objective** (**SLO**).

A typical SLO consists of the following fundamental data:

* **Service-Level Indicator (SLI)**: The indicator used to measure the successful service delivery. SLIs typically refer to metrics such as service success rate, crash-free mobile app users, successful synthetic test runs, or response time.
* **Target**: The target defines the planned goal to achieve in terms of service delivery. A target could be, for example, that 99.99% of all service calls must return without an error, or that 95% of all service requests must be fulfilled in under 2 secondsâ response time.
* **Evaluation period**: The evaluation period is necessary to standardize communication concerning the SLO result. Without a defined evaluation period, the notions of availability are subjective.

Each SLO definition can be evaluated by following result metrics:

* **SLO status**: The current evaluation result of the SLO, expressed as a percentage. The semantics of this percentage (for example, 99.3% of all service requests are successful, or 99.99% of all website users are âsatisfiedâ in terms of Apdex rating) and the target defined for this percentage are up to the SRE team.

  The SLO status must be normalized towards a percentage value in the range of 0â100%.
* **SLO error budget**: The remaining buffer until the defined SLO target is considered as failed. For example, if an SLO defines a 95% target and its current SLO status is evaluated as 98%, the remaining error budget is the difference between the SLO status and the SLO target, in this case 3%.

For more information on SLO normalized error budget and SLO error budget burn rate, see [Configure and monitor service-level objectives with Dynatrace](/managed/deliver/service-level-objectives-classic/configure-and-monitor-slo "Create, configure, and monitor service-level objectives with Dynatrace.").