---
title: Runtime contextualization of container findings
source: https://www.dynatrace.com/docs/secure/use-cases/runtime-contextualization-of-container-findings
scraped: 2026-02-25T21:18:27.817185
---

# Runtime contextualization of container findings

# Runtime contextualization of container findings

* Latest Dynatrace
* Tutorial
* Updated on Sep 30, 2025

Container image scanning is usually performed in artifact repositories, such as [AWS Elastic Container Registry (ECR)ï»¿](https://dt-url.net/mu03pcw), [GCP Artifact Registryï»¿](https://dt-url.net/9g03udo), and [Microsoft Azure Container Registryï»¿](https://dt-url.net/mn23u20). After the images are deployed in production, continuous reassessing of the container images is essential to ensure they're not affected by emerging critical vulnerabilities.

The number of vulnerability findings grows with the number of stored container images, and the development team might become overwhelmed by the number of critical findings. Some of the container images will never be deployed to your production environment. They might be part of your test environments or become obsolete and lay in the repository as a legacy.

In this context, Dynatrace helps you

* Reduce alert fatigue
* Focus remediation efforts on the critical vulnerability findings that significantly impact your production applications

![overview of vulnerability alert reduction](https://dt-cdn.net/images/final-final-v3-last-final-teo-500-f2e05b1ca1.png)

## Target audience

Site reliability engineers (SREs) and application owners who want to maintain the security hygiene and health of their applications.

## Scenario

* The development team stores container images in Amazon ECR. Later on, those images are deployed into staging and production environments running on Kubernetes.
* You monitor the health of your applications with Dynatrace OneAgent in Kubernetes.
* Several new critical vulnerabilities have been discovered recently by Amazon ECR in the container images.

### Request

* Triage critical vulnerabilities and assess the situation automatically.
* Automatically create tickets and notifications for emerging critical vulnerabilities that threaten your production application.

### Goal

Avoid critical vulnerability exposure in production applications on containers with vulnerable container images.

### Result

Our solution allows you to

* Filter for critical findings in production applications on containers with vulnerable container images
* Create notification automation workflows based on those findings

## Prerequisites

* [Set up Kubernetes observability with Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment/other/classic-full-stack "Deploy Dynatrace Operator in classic full-stack mode to Kubernetes")
* [Ingest Amazon ECR vulnerability findings and scan events](/docs/secure/threat-observability/security-events-ingest/ingest-aws-ecr-data "Ingest Amazon ECR container image vulnerability findings and scan events and analyze them in Dynatrace.")
* [Use Dynatrace release product/stage tags](/docs/deliver/release-monitoring/version-detection-strategies "Metadata for version detection in different technologies") for your containers

## Get started

1. Visualize

To view the summarized and unified list of recent vulnerability findings ingested from Amazon ECR

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.
2. Search for and select **Container Vulnerability Findings** for the Amazon ECR integration.

Example dashboard:

![dashboard sample for container vulnerabilities](https://dt-cdn.net/images/new-dashboard-4308-b95f9d6ec2.png)

2. Filter

1. Filter for `RuntimeStatus` to display contextualized findings affecting your runtime containers.

   ![runtime status filter](https://dt-cdn.net/images/2024-11-04-10-10-45-1835-6e0d130070.png)
2. Filter for `ProductStage` to display contextualized findings affecting your production services and applications.

   ![product stage filter](https://dt-cdn.net/images/2024-11-04-10-12-42-1829-24210337bc.png)

3. Automate

You can adjust our automation workflow samples to enrich and filter external container image vulnerability findings for runtime context. For details, see [Automate and orchestrate security findings](/docs/secure/use-cases/automate-and-orchestrate-security-findings "Regularly check for critical security findings and get automatic Jira tickets or Slack alerts.").

Example query to get new critical container image vulnerabilities with a list of the affected container images and running containers:

This query has been updated to align with the new Grail security events table. For the complete list of updates and actions needed to accomplish the migration, follow the steps in the [Grail security table migration guide](/docs/secure/threat-observability/migration "Understand the changes in the new Grail security table and learn how to migrate to it.").

```
// The query has a rolling window of 7 days and the last 24hrs.



// Vulnerability finding events which have already been reported



// before the current 24hr window will not be reported again.



fetch security.events, from: now() - 7d



| filter dt.system.bucket == "default_securityevents"



AND object.type == "CONTAINER_IMAGE"



AND event.type == "VULNERABILITY_FINDING"



AND dt.security.risk.level == "CRITICAL"



// now enrich the runtime context



| join [



fetch dt.entity.container_group_instance, from:now()-3h



| fieldsAdd entity.name, containerImageDigest, containerImageName, workloadName, containerStatus, processes=contains[dt.entity.process_group_instance]



| expand dt.entity.process=processes



| fieldsRemove processes



| join [



fetch dt.entity.process_group_instance, from:now()-3h



], on:{left[dt.entity.process]==right[id]}, kind:leftOuter, fields:{releasesProduct, releasesStage}



], on:{left[container_image.digest]==right[containerImageDigest]}, kind:leftOuter,



fields:{container_instance.id=id, container_instance.name=entity.name, container_image.name=containerImageName,



releasesProduct, releasesStage, containerStatus}



// summarize and filter



| dedup {object.id, vulnerability.id, component.name, component.version,



container_image.registry, container_image.repository}, sort: {timestamp desc}



| parse containerStatus, """LD* "state=" LD:containerStatus ("}" | ",")"""



| fieldsAdd containerStatus=if(isNull(containerStatus),"not running",else:containerStatus)



| fieldsAdd releasesStage=if(isNull(releasesStage), "None", else:releasesStage)



| filter containerStatus=="running" AND releasesStage=="production"



// Aggregate vulnerability findings per vulnerability, repository,



// component and component version.



| summarize {



affected_images_count = count(),



vulnerability_finding_events = collectArray(



record(



object.id = object.id,



event.provider = event.provider,



container_image.registry = container_image.registry,



container_image.repository = container_image.repository,



component.version = component.version,



component.name = component.name,



dt.security.risk.level = dt.security.risk.level,



ingest_time = timestamp



)



)



}, by:{ vulnerability.id, vulnerability.title, event.provider, container_image.registry, container_image.repository, component.name, component.version }



// Filter out, if this vulnerability for the repository and the component



// and version was already reported before the last 24 hours.



// For example, if the same vulnerability was reported multiple times



// during the last 7 days, don't report it again.



| filterOut iAny(vulnerability_finding_events[][ingest_time] < now() - 24h)



// Expand and deduplicate for repetitive findings if they



// were reported more than once in the last 24 hours.



| expand vulnerability_finding_events



| dedup { vulnerability.id, vulnerability.title, vulnerability_finding_events[object.id], vulnerability_finding_events[component.name], vulnerability_finding_events[component.version] }



// Aggregate again to count the unique affected images within each repository.



| summarize {



affected_images_count = count(),



vulnerability_finding_events = collectArray(



vulnerability_finding_events



)



}, by:{ vulnerability.id, vulnerability.title, event.provider, container_image.registry, container_image.repository, component.name, component.version }



| sort vulnerability_finding_events[][ingest_time] desc
```

Example result:

![Example result](https://dt-cdn.net/images/2024-11-04-09-48-57-1764-c397b99b5c.png)

4. Track alert reduction

To track the alert reduction process based on the progressive filtering in [step 2](#filter)

1. Open [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") and go to **Ready-made**.
2. Search for and select **Container image alert reduction** for the Amazon ECR integration.

Example result:

![funnel dashboard showing alert reduction](https://dt-cdn.net/images/funnel-dashboard-4308-16c82e5aa3.png)