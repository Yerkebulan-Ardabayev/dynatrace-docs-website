---
title: Services
source: https://www.dynatrace.com/docs/observe/application-observability/services
scraped: 2026-03-06T21:10:36.219731
---

# Services

# Services

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Oct 23, 2025

Services are an application's fundamental building blocks. From an observability standpoint, they provide application owners with critical metrics to monitor application health.

[![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](services/services-app.md "Maintain centralized control over service health, performance, and resources with the Services app.") provides detailed insights into the performance and health of your services and includes useful features like [Service flow](services-classic/service-flow.md "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.") and [Backtrace](services-classic/service-backtrace.md "Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.").

## Prerequisites

### Permissions

Check the minimal set of permissions required to run ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

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

### Installation

Make sure ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** is [installed in your environment](../../manage/hub.md#install "See the information about Dynatrace Hub.").

## Get started

![View the real-time performance of all your services. Locate specific services using powerful filters.](https://cdn.hub.central.dynatrace.com/hub/1_DI39YNS_hQ7gBgG.png)![Analyze database queries executed by your services to discover which operations consume the most resources.](https://cdn.hub.central.dynatrace.com/hub/2_previously_5_7LmaiBa.png)![Use Dynatrace Intelligence's automated root cause analysis to quickly surface and pinpoint the source of issues in your application services, accelerating analysis.](https://cdn.hub.central.dynatrace.com/hub/3_lHZzEjb_zyT76Yj.png)![Failure analysis comparing timeframes.](https://cdn.hub.central.dynatrace.com/hub/failure-analysis-1990-6b9d85e513_38quxQP.png)

1 of 4View the real-time performance of all your services. Locate specific services using powerful filters.

In Dynatrace, go to ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** to launch the app.

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** provides detailed insights into the performance and health of your services. Use it to perform failure analysis, response times, query performance, and message processing. You can also utilize this app to filter by key attributes, for example, Kubernetes namespaces or HTTP endpoints, and examine relationships to Kubernetes, host, and cloud infrastructure. Moreover, you can view logs emitted by your services and jump directly to [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](distributed-tracing/distributed-tracing-app.md "Discover the functionalities of the new Distributed Tracing app.") for deeper analysis of specific transactions.

For more information, see [Services app](services/services-app.md "Maintain centralized control over service health, performance, and resources with the Services app.").

## Add services to Dynatrace

Add services to Dynatrace using OneAgent or OpenTelemetry integration.

Both options capture metrics, traces, and logs and include support for Serverless functions.

Choose one of the following options to learn more:

Cloud Workload

#### AWS

[AWS Lambda](../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration.md) [AWS Fargate](../../ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md) [Amazon EC2](../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Amazon ECS](../../ingest-from/amazon-web-services/integrate-into-aws/aws-ecs.md) [Amazon EKS](../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks.md) [AWS App Runner](../../ingest-from/amazon-web-services/integrate-into-aws/app-runner.md) [AWS Elastic Beanstalk](../../ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk.md) [All AWS cloud services](../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md) 

#### Microsoft Azure

[Azure Monitor metrics](../../ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide.md) [Azure Logs](../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md) [Azure Kubernetes Service (AKS)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-aks.md) [Azure App Service](../../ingest-from/microsoft-azure-services/azure-integrations/azure-appservice.md) [Azure Functions](../../ingest-from/microsoft-azure-services/azure-integrations/azure-functions.md) [Azure Virtual Machines (VM)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [Azure Virtual Machine Scale Set (VMSS)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-vmss.md) [Azure Service Fabric](../../ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric.md) [Azure Spring Apps](../../ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md) [All Azure cloud services](../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics.md) 

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](../../ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](../../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions.md) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](../../ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](../../ingest-from/google-cloud-platform/gcp-integrations/google-gke.md) [All Google Cloud services](../../ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new.md)

Kubernetes

[Kubernetes cluster](../../ingest-from/setup-on-k8s/deployment.md) [Envoy](../../ingest-from/opentelemetry/integrations/envoy.md) [Istio](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment.md)

Host-based

[AIX](../../ingest-from/dynatrace-oneagent/installation-and-operation/aix.md) [Linux](../../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md) [Solaris](../../ingest-from/dynatrace-oneagent/installation-and-operation/solaris.md) [Windows](../../ingest-from/dynatrace-oneagent/installation-and-operation/windows.md) [zOS](../../ingest-from/dynatrace-oneagent/installation-and-operation/zos.md) 

[Amazon EC2](../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Azure Virtual Machines (VM)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md)

OpenTelemetry

[OpenTelemetry](../../ingest-from/opentelemetry.md)

Other setup options

[Graal VM Native Image](../../ingest-from/technology-support/application-software/java/graalvm-native-image.md) [GitOps](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops.md) [Docker](../../ingest-from/setup-on-container-platforms/docker.md) [Heroku](../../ingest-from/setup-on-container-platforms/heroku.md) [Ingest data in Dynatrace](../../ingest-from.md)

[#### Service flow

Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.

* How-to guide

Read this guide](services-classic/service-flow.md)[#### Service backtrace

Trace the sequence of service calls all the way back up to the browser click that triggered the sequence of calls.

* How-to guide

Read this guide](services-classic/service-backtrace.md)

## Related topics

* [Service flow](services-classic/service-flow.md "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment.")
* [Distributed Traces Classic](distributed-traces.md "Gain observability into highly distributed, cloud-native architectures to effectively trace and analyze transactions in real time.")