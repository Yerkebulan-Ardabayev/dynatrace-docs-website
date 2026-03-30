---
title: Ingest traces
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/ingest-traces
scraped: 2026-03-06T21:12:03.627298
---

# Ingest traces


* Latest Dynatrace
* How-to guide
* 2-min read
* Published Feb 07, 2025

You can use OneAgent or OpenTelemetry integration to add traces to Dynatrace, including trace data from specific extensions for third-party systems, such as Serverless functions and Adobe Experience Manager (AEM) Cloud Service. This ensures, that you capture detailed trace data to analyze the behavior and performance of your applications.

* OneAgent

  Dynatrace OneAgent is the simplest way to capture trace data. By installing OneAgent on your hosts, you can automatically collect distributed traces from your applications.
* OpenTelemetry integration

  If you are using OpenTelemetry, you can configure it to send trace data to Dynatrace. This involves setting up the OpenTelemetry Collector and configuring it to export traces to Dynatrace.

Choose one of the following options to learn more about the configuration.

Cloud Workload

#### AWS

[AWS Lambda](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration.md) [AWS Fargate](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md) [Amazon EC2](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Amazon ECS](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-ecs.md) [Amazon EKS](../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks.md) [AWS App Runner](../../../ingest-from/amazon-web-services/integrate-into-aws/app-runner.md) [AWS Elastic Beanstalk](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk.md) [All AWS cloud services](../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md) 

#### Microsoft Azure

[Azure Monitor metrics](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide.md) [Azure Logs](../../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md) [Azure Kubernetes Service (AKS)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-aks.md) [Azure App Service](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-appservice.md) [Azure Functions](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-functions.md) [Azure Virtual Machines (VM)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [Azure Virtual Machine Scale Set (VMSS)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-vmss.md) [Azure Service Fabric](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric.md) [Azure Spring Apps](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md) [All Azure cloud services](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics.md) 

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](../../../ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions.md) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](../../../ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](../../../ingest-from/google-cloud-platform/gcp-integrations/google-gke.md) [All Google Cloud services](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new.md)

Kubernetes

[Kubernetes cluster](../../../ingest-from/setup-on-k8s/deployment.md) [Envoy](../../../ingest-from/opentelemetry/integrations/envoy.md) [Istio](../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment.md)

Host-based

[AIX](../../../ingest-from/dynatrace-oneagent/installation-and-operation/aix.md) [Linux](../../../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md) [Solaris](../../../ingest-from/dynatrace-oneagent/installation-and-operation/solaris.md) [Windows](../../../ingest-from/dynatrace-oneagent/installation-and-operation/windows.md) [zOS](../../../ingest-from/dynatrace-oneagent/installation-and-operation/zos.md) 

[Amazon EC2](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Azure Virtual Machines (VM)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md)

OpenTelemetry

[OpenTelemetry](../../../ingest-from/opentelemetry.md)

Other setup options

[Graal VM Native Image](../../../ingest-from/technology-support/application-software/java/graalvm-native-image.md) [GitOps](../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops.md) [Docker](../../../ingest-from/setup-on-container-platforms/docker.md) [Heroku](../../../ingest-from/setup-on-container-platforms/heroku.md) [Ingest data in Dynatrace](../../../ingest-from.md)

## Related topics

* Dynatrace OneAgent
* Get started with OpenTelemetry and Dynatrace
* Extend distributed tracing
* Adaptive Traffic Management for distributed tracing