# Документация Dynatrace: license/monitoring-consumption-classic
Язык: Русский (RU)
Сгенерировано: 2026-02-21
Файлов в разделе: 5
---

## license/monitoring-consumption-classic/application-and-infrastructure-monitoring.md

---
title: Application and Infrastructure Monitoring (Host Units)
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring
scraped: 2026-02-21T21:15:20.096258
---

# Application and Infrastructure Monitoring (Host Units)

# Application and Infrastructure Monitoring (Host Units)

* 12-min read
* Updated on Aug 20, 2025

Dynatrace application and infrastructure monitoring is provided via installation of a single [Dynatrace OneAgent](/docs/platform/oneagent "Learn the monitoring capabilities of OneAgent.") on each monitored host in your environment. OneAgent is licensed on a per-host basis (virtual or physical server).

However, not all hosts are of equal size. Larger hosts consume more host units than do smaller-sized hosts. We use the amount of RAM on a monitored server as a measuring stick to determine the size of a host (that is how many host units it comprises). The advantage of this approach is its simplicity. You can have 10 JVMs or 1,000 JVMs; such factors don't affect the amount of monitoring that an environment consumes.

OneAgent can operate in two different modes. By default, OneAgent operates in Full-Stack Monitoring mode. Alternatively, you can use [Infrastructure monitoring mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes#infrastructure-only "Find out more about the available monitoring modes when using OneAgent.") to monitor hosts that don't require full-stack visibility. Infrastructure mode consumes fewer host units than Full-Stack mode.

## Host units

Refer to the host unit weighting table below to see how many host units are consumed based on the amount of RAM a monitored server has. Total host-unit consumption is calculated based on the sum of all host units of all modes and monitored systems. For details about the host unit quota split, see [Quotas and overages](/docs/manage/account-management/license-subscription/license-overview-classic#quotas-and-overages "View your Dynatrace classic licensing usage and details.").

| Max. RAM | Host units (Full-Stack[1](#fn-1-1-def)) | Host units (Infrastructure[2](#fn-1-2-def)) |
| --- | --- | --- |
| 1.6 GiB | 0.10 | 0.03 |
| 4 GiB | 0.25 | 0.075 |
| 8 GiB | 0.50 | 0.15 |
| 16 GiB | 1.0 | 0.3 |
| 32 GiB | 2.0 | 0.6 |
| 48 GiB | 3.0 | 0.9 |
| 64 GiB | 4.0 | 1.0 |
| 80 GiB | 5.0 | 1.0 |
| 96 GiB | 6.0 | 1.0 |
| 112 GiB | 7.0 | 1.0 |
| nx16 GiB | n | 1.0 |

1

When the amount of RAM on a host falls between the values listed in the table above, the number is rounded up. For example, a host with 12 GiB RAM consumes 1 host unit because 12 GiB falls between 8 GiB and 16 GiB.

2

For [Infrastructure Monitoring mode](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent."), the same rounding principle applies. If a host unit cap is enabled for your Cloud Infrastructure license, the number of host units consumed by a host is capped at 1.0. If you have an existing agreement that doesn't reflect the `1.0` cap on host units per host, please [contact your Dynatrace Sales representativeï»¿](https://www.dynatrace.com/contact/).

### Host unit hours

A host unit hour represents the consumption of a host unit over a time period. 1 host unit hour equates to 1 host unit being consumed for 1 hour. A host with 16 GiB of RAM (that is 1 host unit) running for a full day consumes 24 host unit hours.

Host unit hours calculation example

For example, say you have 1,000 host unit hours available and you want to monitor a host that has 64 GiB RAM (which equates to 4 host units). If you keep the host running for a full day, it will consume 96 host unit hours.  
`4 (host units) Ã 24 (hours a day) = 96 (host unit hours)`

The 1,000 host unit hours will be consumed in slightly more than 10 days.  
`4 (host units) Ã 24 (hours) Ã 10 (days) = 960 host unit hours`

True concurrency in host unit hour calculations

Each minute, Dynatrace calculates host-unit consumption based on true concurrency. This means that two hosts running within the same hour will consume two hosts units if both hosts run at the same time. Host-unit hours are counted in calendar hours (for example, 10:00 â 11:00 AM) and not usage hours (for example, 10:23 â 11:23 AM).

If a host runs for less than 5 minutes, it doesn't count against your host unit hour quota. A host running for 5 minutes or longer is rounded up to `1 host unit hour`.

When the monitoring of a host stops for any reason, that host's consumed host units are released and made available to another host within about five minutes.

#### Example 1

You have a host with 16 GiB RAM (which equals 1 host unit) running from 10:00-10:30 AM. At 10:30 you spin up another host of the same size. Dynatrace considers this a single host unit because the hosts don't run concurrently.

#### Example 2

You start the first host at 10:00 AM and launch another host at 10:30 AM. Then, both hosts run together for 30 minutes and are shut down at the same time. Dynatrace considers this to be 2 host units because both hosts run at the same time.

#### Example 3

One host of size 16 GiB RAM is started and stopped three times within an hour:

`12:10 - Server start`  
`12:20 - Server stop`

`12:30 - Server start`  
`12:40 - Server stop`

`12:50 - Start`  
`13:00 - Stop`

Such a scenario equates to `1 host unit hour` because true concurrency is taken into account.

#### Example 4

You have a host with 16 GiB RAM (which equals 1 host unit) running from 10:23-11:23 AM. Since the host is running for 2 calendar hours (10:00 â 11:00 AM and 11:00 â 12:00 AM), it equates to `2 host unit hours`.

Free-trial host unit hours

Host unit hours are used for Dynatrace free trials. When you sign up for a Dynatrace free trial, you receive a certain number of host unit hours to evaluate Dynatrace.

Apply host unit hours to demand spikes and select projects

If you know in advance that your base quota of host units will be exceeded due to holiday demand or a short-lived project (for example, on Black Friday or during a one-time testing initiative), you can use host unit hours rather than host units to manage variable traffic spikes. For example, if you have a pool of 9,000 host unit hours and 100 host units, during Black Friday, you'll need more hosts to scale up for the increased traffic on your site. In such a case, you have the option of using all 9,000 host unit hours in a single day. This would enable you to connect an additional 375 host units (475 total maximum) to Dynatrace for one day.  
`9,000 (host unit hours) / 24 (hours) + 100 (base quota of host units) = 475 (max. host units)`

Overages and multiple environments

If your account has multiple monitoring environments, for example, one for development and the other one for production, then overages are calculated per account and not per environment. Only when the account quota is exceeded, then overages are incurred.

For example, you licensed 100 host units and you have two environments, one for production and one for testing. You assign 80 host units to the production environment and 20 host units to the testing environment. Your license entitles you for overages (you can see this in the account overview below the host units circle).
If production uses 70 host units but testing uses 30 host units, the total account quota of 100 host units is not exceeded thus no overages are incurred. Only if both environments use more than 100 host units overages are incurred.

### Host unit overages Optional

If you've arranged for an allotment of host units to monitor your hosts and you're entitled to exceed this number (that is overages are allowed for your account), the overages will be calculated in host unit hours. For example, if you've arranged to monitor up to 10 host units (a maximum of 160 GiB total RAM) and your account allows for overages, if you connect another host that equates to 2 host units you'll have 12 host units in total and will, therefore, have exceeded your quota by 2 host units. If you continue to monitor your hosts using 12 host units for a full week, you'll accrue an overage of 336 host unit hours.  
`2 (host units) Ã 24 (hours a day) Ã 7 (days) = 336 (host unit hours overage)`  
To add or remove overages from your account, [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/).

## Application-only monitoring



Dynatrace provides application-only monitoring for container platforms.
This is useful with platforms (such as Kubernetes or Amazon Elastic Container Service (ECS)) when you:

* Want to deploy, monitor, and license at the container level.
* Lack access to the underlying VM.

Example scenarios include, but are not limited to:

* [Amazon ECSï»¿](https://docs.aws.amazon.com/whitepapers/latest/aws-overview/compute-services.html)

  + [AWS ECS daemon](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs/deploy-oneagent-on-ecs "Monitor ECS clusters as a daemon service, with the EC2 launch type.")
  + [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk "Install OneAgent on AWS Elastic Beanstalk.")
  + [AWS Elastic Kubernetes Service](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-eks "Install OneAgent on Elastic Kubernetes Service.")
* [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate "Install OneAgent on AWS Fargate.")
* [Azure App Service](/docs/observe/infrastructure-observability/cloud-platform-monitoring/azure-monitoring "Monitor Azure with Dynatrace") including [Azure Functions on App-Service (Dedicated) Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/integrate-oneagent-on-azure-functions "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions using an Azure site extension.")
* [Azure Container instancesï»¿](https://docs.microsoft.com/en-us/azure/container-instances/)

  + [Azure Kubernetes Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks "Learn how to deploy, operate, and maintain OneAgent on Azure Kubernetes Service.")
* [Cloud Foundry](/docs/ingest-from/setup-on-container-platforms/cloud-foundry/deploy-oneagent-on-cloud-foundry-for-application-only-monitoring "Install OneAgent on Cloud Foundry.")

* [Kubernetes](/docs/ingest-from/setup-on-k8s/deployment/application-observability "Deploy Dynatrace Operator in application monitoring mode to Kubernetes")

* [Red Hat OpenShift Container Platformï»¿](https://www.redhat.com/en/technologies/cloud-computing/openshift/container-platform)

For application-only monitoring, Dynatrace uses [universal injection](/docs/ingest-from/technology-support/oneagent-platform-and-capability-support-matrix#universal-injection "Learn which capabilities are supported by OneAgent on different operating systems and platforms.") to inject OneAgent code modules into applications in a unified way across multiple platforms.

Host unit calculations for application-only monitoring are based on the detected memory limit, such as a container memory limit.
This memory is detected at the level of the OS instance or container.
If no memory limits are detected, host unit calculations may use the underlying host memory, which may reflect a higher number of host units.
Dynatrace OneAgent integrations for serverless compute services consume [host units](#classic-host-units), and calculations use [Full-Stack host-unit value weighting](#classic-host-units).
Examples of host unit calculations are shown at [Host unit hours calculation example (application-only monitoring)](#application-only-host-unit-example).

The following scenarios have their own calculations for host units and host unit hours, as described in the table below.

| Scenario | Description |
| --- | --- |
| Azure App Services (running on the App Service (dedicated) plan for Windows) | Consumption is based on the number and memory of the plan's instances. It does not matter how many applications run on the instances. |
| Azure App Service (running on Linux OS or Linux containers) | Consumption is based on the memory of a plans instance, multiplied by the number of running containers. This is because container resource limits cannot be set. |
| Oracle Solaris Zones | Solaris Zones are counted as hosts. |
| Monitored containers that are not detected as containers | These containers are counted as hosts. |
| Serverless functions | Serverless functions consume [DDUs for serverless functions](/docs/license/monitoring-consumption-classic/davis-data-units/serverless-monitoring "Understand how serverless monitoring consumption is calculated."). |

Host unit hours calculation example (application-only monitoring)

The table below shows how host unit hours are calculated in four different application-only monitoring scenarios.

| Monitored entities | Memory limit per entity | Host-unit weight per entity | Monitoring time | Calculation |
| --- | --- | --- | --- | --- |
| 4 serverless containers, running concurrently | 1 GiB RAM | 0.1 | 1 hour | `4 * 0.1 * 1 = 0.4 host unit hours` |
| 2 Docker containers, running on 1 host | 16 GiB RAM[1](#fn-2-1-def) | 1.0 | 1 hour | `2 * 1.0 * 1 = 2.0 host unit hours` |
| Azure App Service Premium Service Plan, with 4 App Services on Windows, scaled out on 2 instances | 16 GiB RAM | 1.0 | 1 hour | `2 * 1.0 * 1 = 2.0 host unit hours` |
| Azure App Service Premium Service Plan, with 8 containers | 16 GiB RAM | 1.0 | 1 hour | `8 * 1.0 * 1 = 8.0 host unit hours` |

1

The host has 16 GiB RAM, but no container memory limits are detected. Therefore, each container consumes 16 GiB RAM in the calculation.

## Distributed traces

Full-Stack Monitoring includes a defined amount of trace data volume. The included peak trace volume available in an environment at any time depends on the active host units in that environment. Each environment processes a minimum of 5,000 full-service calls per minute, regardless of the number of active host units. Every active host unit increases the environment's peak trace volume by 250 full-service calls per minute. You can calculate the peak trace volume with the following calculation: `peak trace volume = (number of active host units) * 250`.

The source distributed trace data is Dynatrace OneAgent. OneAgent automatically manages the volume of captured trace data via [Adaptive Traffic Management](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management/adaptive-traffic-management-saas-classic "Learn how Adaptive Traffic Management works with Dynatrace classic license and how to adjust trace sampling for HTTP and RPC requests."). It automatically and continuously adjusts the sampling rate in an intelligent way and keeps the ingested trace data volume roughly within your included trace data volume.

## Mainframe monitoring on IBM z/OS

Monitoring of the [CICS, IMS, and z/OS Java code modules](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos "Install, configure, and manage Dynatrace modules on z/OS.") that run on IBM z/OS are consumed based on million service units (MSUs). Therefore, mainframe monitoring doesn't contribute to the consumption of host units or host unit hours.

An MSU is an IBM measurement of the amount of processing workload an IBM Z mainframe can perform per hour. The amount of consumed MSUs in [sub-capacity licensingï»¿](https://www.ibm.com/it-infrastructure/z/pricing-licensing) is calculated based on peak rolling 4-hour average MSU values of the most recent month from IBM system management facility data per monitored logical partition (LPAR) or subsystem.

The peak rolling 4-hour average MSU values per monitored LPAR can be derived from Dynatrace or section N5 of the [sub-capacity reporting toolï»¿](https://www.ibm.com/docs/en/zos/2.5.0?topic=tool-about-sub-capacity-reporting) (SCRT) report. The peak rolling 4-hour average MSU values per subsystem can be derived from section P5 of the SCRT report.

## Premium High Availability

The [Premium High Availabilityï»¿](https://docs.dynatrace.com/managed/shortlink/managed-multi-data-center) deployment model is licensed separately based only on the concurrent host units limit. Premium High Availability doesn't contribute to the consumption of concurrent host units or host unit hours.

## How consumption of Synthetic NAM Monitoring affects billing

Network availability monitoring (NAM) monitors don't have a separate line on the Dynatrace rate card. Instead, you're billed based on the [number of metric data points](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.") generated during each execution of a NAM test. For more information, please contact your Dynatrace account manager.

Metric data point calculations

The following details apply to metric data points:

* Metric data points related to monitor and step execution are non-billable.
* Only the consumption of metrics produced at the request level affects your billing.
* Each request execution within ping tests generates 6 metric data points.

  + The number of packets used in a ping test does not impact the number of metrics produced or your billing.
  + The number of packets does not affect the price.
* Each request execution within TCP/DNS tests generates 3 metric data points.
* The price stays the same regardless of whether you create several tests containing a single request, or you create one test with numerous requests for the same set of hosts or devices.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [Extend metric observability](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")
* [DDUs for Log Monitoring Classic](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic.")

---

## license/monitoring-consumption-classic/davis-data-units/custom-traces.md

---
title: DDUs for custom traces (Trace API)
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces
scraped: 2026-02-21T21:17:05.826807
---

# DDUs for custom traces (Trace API)

# DDUs for custom traces (Trace API)

* 2-min read
* Published Mar 30, 2021

While there are no additional costs or licensing involved in the integration of OpenTracing and OpenTelemetry span data into Dynatrace via OneAgent, you have the option to configure the Dynatrace Trace API to ingest OpenTelemetry and OpenTracing spans; these are known as "custom traces." This approach is useful for seamlessly integrating OpenTelemetry trace data that's emitted by third-party services. Ingestion of spans via the Trace API endpoint consumes [Davis data units](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") because this approach requires more processing and analytical power than ingestion via OneAgent.

For details on OneAgent-based ingestion of OpenTelemetry and OpenTracing spans, which does not consume DDUs, see [OneAgent OpenTracing and OpenTelemetry support](/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing "Learn how to integrate OpenTracing with Dynatrace.").

## DDU consumption for custom trace ingestion

While a trace may contain spans captured with OneAgent and the Dynatrace Trace API, only spans that are ingested via the Dynatrace Trace API consume DDUs. For an API service that is instrumented with OpenTelemetry and spans are captured via OneAgent, no DDUs are consumed. Custom traces ingested via the Dynatrace Trace API are licensed on the basis of ingestion of spans (each span equates to a single operation within a trace).

### DDU consumption example

To calculate the DDU consumption for custom traces, multiply the total number of invocations by the total number of spans times the DDU weight, for the measured time period. Consider an API service that's instrumented with OpenTelemetry that ingests on average 10 spans per API call via the Dynatrace Trace API. If the average number of API calls per month is 1 million, the monthly DDU consumption is 7,000 DDUs (`1,000,000 invocations Ã 10 spans Ã .0007 DDUs = 7,000 DDUs`), with an annual equivalent of 84,000 DDUs (`7,000 DDUs Ã 12 months = 84,000 DDUs`).

Davis data unit pools

[Davis data units pools for traces](/docs/license/monitoring-consumption-classic/davis-data-units#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") allow you to set hard limits on your DDU consumption for traces. Go to **Settings** > **Consumption** > **Davis data units pools** and turn on **Enable limit** in the **Traces** section to set an annual or monthly limit.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [License Dynatrace](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Extending Dynatrace (Davis data units)](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")
* [DDUs for metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.")
* [Extend metric observability](/docs/ingest-from/extend-dynatrace/extend-metrics "Learn how to extend metric observability in Dynatrace.")

---

## license/monitoring-consumption-classic/davis-data-units/ddu-events.md

---
title: DDUs for custom Davis events
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/ddu-events
scraped: 2026-02-21T21:17:54.033706
---

# DDUs for custom Davis events

# DDUs for custom Davis events

* 2-min read
* Published Jul 09, 2021

While there are no additional costs or licensing involved in the default monitoring and reporting of built-in event types via OneAgent or cloud integrations, you have the option to configure custom events and/or event-ingestion channels. Such event-related customizations do result in the consumption of [Davis data units](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU)."). Custom Davis event ingestion consumes DDUs because it requires significantly more processing and analytical power than does built-in event ingestion via OneAgent of cloud integrations.

## Custom Davis event types that consume DDUs

Custom created/ingested or subscribed events that you might configure for your environment and thereby consume DDUs include:

* Any custom event sent to Dynatrace using the [Events API v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.") or the [OneAgent API](/docs/ingest-from/extend-dynatrace/extend-events#oneagent "Learn how to extend event observability in Dynatrace.")
* Any custom event (such as a Kubernetes event) created from log messages by a [log event](/docs/analyze-explore-automate/log-monitoring/analyze-log-data/log-events "Learn how to create and use Dynatrace log events to analyze log data.") extraction rule

## How DDU consumption is calculated for custom Davis events

DDU consumption for custom Davis events is equivalent to [custom metric data point licensing](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#calculation-details "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). Every ingested custom event consumes 0.001 DDU. This also applies to updates custom events already sent.

Davis data unit pools

[Davis data units pools for events](/docs/license/monitoring-consumption-classic/davis-data-units#ddu-pools "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).") allow you to set hard limits on your DDU consumption for events. Go to **Settings** > **Consumption** > **Davis data units pools** and turn on **Enable limit** in the **Events** section to set an annual or monthly limit.

## FAQ

### What can cause consumption shown as entity "Not related to a monitored entity"

The consumption can be caused by events v2 API if no entity selector is provided. See [Events v2](/docs/dynatrace-api/environment-api/events-v2 "Find out what you can do with the Dynatrace Events API v2.").

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)

---

## license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics.md

---
title: DDUs for Log Management and Analytics
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/davis-data-units/log-management-and-analytics
scraped: 2026-02-21T21:23:30.575111
---

# DDUs for Log Management and Analytics

# DDUs for Log Management and Analytics

* 12-min read
* Updated on Apr 07, 2025

The DDU consumption model outlined here for Log Management and Analytics only affects Dynatrace SaaS environments that are activated for Dynatrace Grail for log data management. DDU consumption for all other DDU capability types, including [Log Monitoring for Dynatrace SaaS & Managed](/docs/license/monitoring-consumption-classic/davis-data-units/log-monitoring-consumption "Understand how the volume of DDU consumption is calculated for Dynatrace Log Monitoring Classic."), remains unchanged. For details about activating Log Management and Analytics for your Dynatrace environment, contact a Dynatrace product expert via live chat within your Dynatrace environment.

This page explains how DDUs are consumed by Dynatrace Log Management and Analytics and how you can estimate and track your environmentâs DDU consumption.

## DDU consumption model for Log Management and Analytics

The DDU consumption model for Log Management and Analytics is based on three dimensions of data usage (Ingest & Process, Retain, and Query). The unit of measure for consumed data volume is gigabytes (GB). Each of the three data usage dimensions consumes DDUs based on a different weight (see the "DDU consumption" row in the table below for details).

Total DDU consumption for Log Management and Analytics is calculated by multiplying the DDU weight of each of the three data-usage dimensions with the data volume in GB.

Unit of measure

Ingest & Process

Retain

Query

Definition

Ingested data is the amount of raw data in bytes (logs and events) sent to Dynatrace after decompression and before enrichment and transformation.

Retained data is the amount of data saved to storage after data parsing, enrichment, transformation, and filtering but before compression.

Queried data is the data read during the execution of a DQL query, including sampled data.

DDU consumption

100.00 DDUs per GB

0.30 DDUs per GB retained per day

1.70 DDUs per GB read

## Ingest & Process

Whatâs included with the Ingest & Process data-usage dimension?

Concept

Explanation

Data delivery

* Delivery of log data via OneAgent or the Log ingestion API (via ActiveGate)

Topology enrichment

* Enrichment of log events with data source and topology metadata

Data transformation

* Add, edit, or drop any log attribute
* Perform mathematical transformations on numerical values (for example, creating new attributes based on calculations of existing attributes)
* Extract business, infrastructure, application, or other data from raw logs. This can be a single character, string, number, array of values, or other. Extracted data can be turned into a new attribute allowing additional querying, filtering, etc. Metrics can be created from newly extracted attributes (see "Conversion to time series" below), or extracted attributes can be queried for ad-hoc analysis
* Mask sensitive data by replacing either the whole log record, one specific log record attribute, or certain text with a masked string

Data-retention control

* Filter incoming logs based on content, topology, or metadata to reduce noise. Log filtering consumes DDUs during Ingest & Process, but not for Retain.
* Manage data retention periods of incoming logs based on data-retention rules

Conversion to time series

* Create metrics from log records or attributes (note that creating [custom metrics consumes additional DDUs](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.") beyond those consumed for ingestion and processing.)

Apply the following calculation to determine your DDU consumption for the Ingest & Process data-usage dimension:  
`(number of GBs ingested) Ã (100.00 DDU weight) = DDUs consumed`

Be aware that data enrichment and processing can increase your data volume significantly. Depending on the source of the data, the technology, the attributes, and metadata added during processing, the total data volume after processing can increase by a factor of 2 or more.

## Retain

Whatâs included with the Retain data-usage dimension?

Concept

Explanation

Data availability

* Retained data is accessible for analysis and querying until the end of the retention period.

Retention periods

* Choose a desired retention period

  + 10 days (10 days)
  + 2 weeks (15 days)
  + 1 month (35 days) default
  + 3 months (95 days)
  + 1 year (372 days)

  + 15 months (462 days)
  + 3 years (1,102 days)
  + 5 years (1,832 days)
  + 7 years (2,562 days)
  + 10 years (3,657 days)

Apply the following calculation to determine your DDU consumption for the Retain data-usage dimension:  
`(number of GB of processed data ingested) Ã (retention period in days) Ã (0.30 DDU weight) Ã (number of days that data is stored) = DDUs consumed`

## Query

Query data usage occurs when:

* Running the query in the Log & Events viewer.
* Submitting custom DQL queries in the Logs & Events viewer in advanced mode.
* Unified analysis pages show the log data of a specific entity.
* Dashboard tiles that are based on log data trigger the execution of DQL queries on refresh and include sampled data.
* Executing DQL queries via API.

Dynatrace Query Language (DQL) queries consume Davis data units (DDUs) while they are active, even when the results of such queries are not returned. To avoid unnecessary consumption of DDUs, cancel ongoing queries for logs and aggregations that are no longer necessary. Otherwise, you might be billed for incomplete queries.

Whatâs included with the Query data-usage dimension?

Concept

Explanation

On-read parsing

* Use DQL to query historical logs in storage and extract business, infrastructure, or other data across any timeframe, and use extracted data for follow-up analysis.
* No upfront indexes or schema required for on-read parsing

Aggregation

* Perform aggregation, summarization, or statistical analysis of data in logs across specific timeframes or time patterns (for example, data occurrences in 30-second or 10-minute intervals), mathematical, or logical functions.

Reporting

* Create reports or summaries with customized fields (columns) by adding, modifying, or dropping existing log attributes.

Context

* Use DQL to analyze log data in context with relevant data on the Dynatrace platform, for example, user sessions or distributed traces.

Apply the following calculation to determine your DDU consumption for the Query data-usage dimension:  
`(number of GB of uncompressed data read during query execution) Ã (1.70 DDU weight) = DDUs consumed`

## Calculate DDU consumption across data-usage dimensions

Following are example DDU calculations which show how each data-usage dimension contributes to overall DDU consumption.

### Step 1 â Ingest & Process

For example, say that you produce 500 GB of log data per day which you ingest into Log Management and Analytics for processing. The monthly DDU consumption for Ingest & Process in this case would be 1,500,000 DDUs:

Ingest volume per day

500 GB

Ingest volume per month

15,000 GB

`500 (GB data per day) Ã 30 (days)`

DDU consumption per month

1,500,000 DDUs

`15,000 (GB per month) Ã 100.00 (DDUs per GB)`

### Step 2 - Retain

Following the Ingest & Process step, your data is retained and enriched on an on-going basis. If you ingested 500 GB of raw data in step 1, 900 GB of enriched data (`500 GB Ã 1.8 for enrichment`) is added to your storage daily. In this example, your enriched data is retained for 35 days. The monthly DDU consumption (after a ramp-up period of 35 days) for Retain in this case is 283,500 DDUs:

Retained volume for 1 day

900 GB

`500 (GB data per day) Ã 1.8 (enrichment)`

Retained volume for 35 days

31,500 GB

`900 (GB data per day) Ã 35 (days)`

DDU consumption per day

9,450 DDUs

`31,500 (GB) Ã 0.3 (DDUs per GB per day)`

DDU consumption per month

283,500 DDUs

`9,450 (DDUs) Ã 30 (days)`

If the same amount of processed data is to be retained for a year, the monthly DDU consumption (after a ramp-up of 365 days in this case) for Retain is 2,956,500 DDUs.

Retained volume for 1 day

900 GB

`500 (GB data per day) Ã 1.8 (enrichment)`

Retained volume for 365 days

328,500 GB

`900 (GB data per day) Ã 365 (days)`

DDU consumption per day

98,550 DDUs

328,500 (GB) Ã 0.3 (DDUs per GB per day)

DDU consumption per month

2,956,500 DDUs

`98,550 (DDUs) Ã 30 (days)`

### Step 3 - Query

Letâs assume that to resolve incidents and analyze performance issues your team executes DQL queries with a total of 25 TB of data read per day. The monthly DDU consumption for Query in this case is 1,275,000 DDUs.

Data volume read per day

25,000 GB

Data volume read per month

750,000 GB

`25,000 (GB data per day) Ã 30 (days)`

DDU consumption per month

1,275,000 DDUs

`750,000 (GB per month) Ã 1.70 (DDUs per GB)`

### Step 4 â Total DDU consumption

The total monthly DDU consumption for this example scenario of 35 days of data retention is 3,058,500 DDUs.

Ingest â DDU consumption per month

1,500,000 DDUs

Retain â DDU consumption per month

283,500 DDUs

Query â DDU consumption per month

1,275,000 DDUs

Total DDU consumption per month

3,058,500 DDUs

## FAQ

### Can I change the retention period for Log Management and Analytics?

Yes. The following retention periods apply to log buckets:

* 10 days (10 days)
* 2 weeks (15 days)
* 1 month (35 days) default
* 3 months (95 days)
* 1 year (372 days)

* 15 months (462 days)
* 3 years (1,102 days)
* 5 years (1,832 days)
* 7 years (2,562 days)
* 10 years (3,657 days)



### Where can I check my environmentâs DDU consumption for logs and events?

1. Go to [**Account Management**ï»¿](https://myaccount.dynatrace.com/) > **License** / **Subscription** > **Overview**. Youâll need the change monitoring settings permission or an admin account to access this page.
2. On the **Davis data units (DDU)** page:  
   a. In the **Consumption by DDU pool** table, see the **Log Monitoring** row.  
   b. In the **DDU consumption details** section, go to the **Log Monitoring** tab.

### What is the DDU weight of one log or event record?

For Log Management and Analytics, volume of data in gigabytes (GB) is the unit of measure. Consumption is based on three data-usage dimensions. The weight of DDU consumption per dimension is as follows:

* Ingest & Process: 100.00 DDUs per GB of data ingested and processed
* Retain: 0.30 DDUs per GB per day for data stored
* Query: 1.70 DDUs per GB for data read from storage during query execution

### What is the size of one log or event record?

The number and size of individual log records isnât relevant for DDU consumption. For Log Management and Analytics, DDU consumption for a given period is calculated based on volume of data ingested and processed, volume of data stored per day, and volume of data read from storage during query execution.

### Are there any host-included DDUs available for Log Management and Analytics?

No. Log Management and Analytics always consumes DDUs for Ingest & Process, Retain, and Query. Note that you can choose to only ingest and process data without storing it or querying it. Each Dynatrace environment includes a free tier of 200,000 DDUs per year, which can be used for Ingest & Process, Retain, and Query.

### Iâm currently using my DDUs for Log Monitoring for Dynatrace SaaS & Managed, custom metrics, custom traces, custom events, and serverless functions and I donât plan to migrate. Will anything change for me?

No. The DDU consumption model outlined here for Log Management and Analytics only affects Dynatrace SaaS environments that are activated for and connected to a Dynatrace GrailTM cluster for log data management. DDU consumption for all other DDU capability types, including Log Monitoring for Dynatrace SaaS & Managed, remains unchanged.

### Iâm considering migrating to Log Management and Analytics. What will change for me?

If Log Management and Analytics is activated for your environment, the DDU consumption model that uses gigabytes as the unit of measure will replace the event-based consumption model thatâs used for Log Monitoring for Dynatrace SaaS & Managed. Consumption of other DDU-based capability types, including Log Monitoring for Dynatrace SaaS & Managed (if you continue to use it in parallel) will remain unchanged.

### Does the Dynatrace platform consume DDUs for fractional GBs? Would 0.5 GB of Ingest & Process consume only 50 DDUs?

Yes. Every ingested GB (or fraction thereof, before enrichment and processing) is added together and then multiplied by the DDU weight of 100.00 DDUs. For example, DDU consumption for Ingest & Process of 10.50 GB equates to 1,050 DDUs.

`10.50 (GB log data) Ã 100.00 (DDU weight) = 1,050 DDUs`

### I want to convert my log messages into metrics. How will this affect my environmentâs DDU consumption?

While writing ingested logs to time series is a cost-effective way of visualizing log-based metrics, this approach consumes additional DDUs for creating custom metrics in addition to the DDUs consumed for Ingest & Process.

### Do failed query executions consume DDUs?

No, when internal failures occur while executing a query (for example, a time-out) no DDUs are consumed.

### Do canceled query executions consume DDUs?

If you cancel a query execution, all data read before the cancellation will be factored into your DDU consumption.

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)
* [Log Monitoring Classic](/docs/analyze-explore-automate/log-monitoring "Learn how to enable Log Monitoring, the insights that Log Monitoring can provide, and more.")

---

## license/monitoring-consumption-classic.md

---
title: Dynatrace classic licensing
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic
scraped: 2026-02-21T21:15:23.885611
---

# Dynatrace classic licensing

# Dynatrace classic licensing

* 1-min read
* Published Mar 30, 2021

Monitoring consumption for Dynatrace classic licensing is based on various monitoring units that are consumed by your Dynatrace environment as your organization uses Dynatrace platform capabilities. If you have a Dynatrace Platform Subscription, please refer to [Dynatrace Platform Subscription (DPS) documentation](/docs/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

To get started using Dynatrace, [contact Dynatrace Salesï»¿](https://www.dynatrace.com/contact/). Your sales representative will provide you with further details.

This page is provided for informational purposes only. The terms of the Dynatrace free trial offer and/or your Dynatrace license will be applied to any use of Dynatrace products or services.

[### Dynatrace license lifecycle

Get to know the lifecycle of Dynatrace SaaS licenses and understand how licenses affect your consumption of Dynatrace services.](/docs/license/license-lifecycle "Understand your Dynatrace DPS or Classic license lifecycle, and how it affects your consumption of Dynatrace services.")[### Application and infrastructure monitoring (host units)

Each OneAgent-monitored host in your environment consumes host units.](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.")[### Davis data units (DDUs)

Davis data units (DDU) provide a simple means of licensing certain capabilities (custom metrics, traces, log monitoring, and custom events) on the Dynatrace platform.](/docs/license/monitoring-consumption-classic/davis-data-units "Understand how Dynatrace monitoring consumption is calculated based on Davis data units (DDU).")[### Digital Experience monitoring (DEM units)

Dynatrace Synthetic Monitoring, Real User Monitoring, and Session Replay consume DEM units.](/docs/license/monitoring-consumption-classic/digital-experience-monitoring-units "Understand how Dynatrace Digital Experience Monitoring consumption is calculated based on DEM units.")[### Application Security monitoring (ASUs)

Dynatrace Application Security consumes Application Security units (ASUs).](/docs/license/monitoring-consumption-classic/application-security-units "Understand how Dynatrace Application Security and Runecast SPM consumption are calculated.")

## Related topics

* [Dynatrace pricingï»¿](https://www.dynatrace.com/pricing/)

---
