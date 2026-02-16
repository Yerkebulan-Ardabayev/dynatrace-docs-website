---
title: Services
source: https://www.dynatrace.com/docs/observe/application-observability/services
scraped: 2026-02-16T09:15:04.398467
---

# Services

# Services

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Oct 23, 2025

Services are an application's fundamental building blocks. From an observability standpoint, they provide application owners with critical metrics to monitor application health.

[![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") provides detailed insights into the performance and health of your services and includes useful features like [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") and [Backtrace](/docs/observe/application-observability/services-classic/service-backtrace "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").

## Prerequisites

### Permissions

Check the minimal set of permissions required to run ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

Permission

Description

storage:events:read

Query events from GRAIL

storage:entities:read

Query entities from GRAIL

storage:logs:read

Query logs from GRAIL

storage:spans:read

Read span data

storage:metrics:read

Query metrics from GRAIL

storage:buckets:read

Read buckets

storage:smartscape:read

Read smartscape nodes and edges

hub:catalog:read

Read release details

storage:fieldsets:read

Read fieldsets from GRAIL

storage:filter-segments:read

Read filter-segments

10

rows per page

Page

1

of 1

### Installation

Make sure ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is [installed in your environment](/docs/manage/hub#install "See the information about Dynatrace Hub.").

## Get started

![View the real-time performance of all your services. Locate specific services using powerful filters.](https://cdn.hub.central.dynatrace.com/hub/1_DI39YNS_hQ7gBgG.png)![Analyze database queries executed by your services to discover which operations consume the most resources.](https://cdn.hub.central.dynatrace.com/hub/2_previously_5_7LmaiBa.png)![Use Dynatrace Intelligence's automated root cause analysis to quickly surface and pinpoint the source of issues in your application services, accelerating analysis.](https://cdn.hub.central.dynatrace.com/hub/3_lHZzEjb_zyT76Yj.png)![Failure analysis comparing timeframes.](https://cdn.hub.central.dynatrace.com/hub/failure-analysis-1990-6b9d85e513_38quxQP.png)

1 of 4View the real-time performance of all your services. Locate specific services using powerful filters.

In Dynatrace, go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** to launch the app.

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** provides detailed insights into the performance and health of your services. Use it to perform failure analysis, response times, query performance, and message processing. You can also utilize this app to filter by key attributes, for example, Kubernetes namespaces or HTTP endpoints, and examine relationships to Kubernetes, host, and cloud infrastructure. Moreover, you can view logs emitted by your services and jump directly to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Discover the functionalities of the new Distributed Tracing app.") for deeper analysis of specific transactions.

For more information, see [Services app](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.").

## Add services to Dynatrace

Add services to Dynatrace using OneAgent or OpenTelemetry integration.

Both options capture metrics, traces, and logs and include support for Serverless functions.

Choose one of the following options to learn more:

Cloud Workload

#### AWS

[AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration) [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate) [Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Amazon ECS](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs) [Amazon EKS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk) [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services) 

#### Microsoft Azure

[Azure Monitor metrics](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide) [Azure Logs](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure) [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks) [Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice) [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [Azure Virtual Machine Scale Set (VMSS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring) [All Azure cloud services](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics) 

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke) [All Google Cloud services](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new)

Kubernetes

[Kubernetes cluster](/docs/ingest-from/setup-on-k8s/deployment) [Envoy](/docs/ingest-from/opentelemetry/integrations/envoy) [Istio](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment)

Host-based

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos) 

[Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine)

OpenTelemetry

[OpenTelemetry](/docs/ingest-from/opentelemetry)

Other setup options

[Graal VM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image) [GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops) [Docker](/docs/ingest-from/setup-on-container-platforms/docker) [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [Ingest data in Dynatrace](/docs/ingest-from)

[#### Service flow

Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-flow)[#### Service backtrace

Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.

* How-to guide

Read this guide](/docs/observe/application-observability/services-classic/service-backtrace)

## Related topics

* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")