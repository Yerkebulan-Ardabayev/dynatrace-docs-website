---
title: Application and Infrastructure Monitoring (Host Units)
source: https://www.dynatrace.com/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring
scraped: 2026-02-25T21:18:40.046835
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