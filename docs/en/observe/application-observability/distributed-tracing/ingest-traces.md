---
title: Ingest traces
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/ingest-traces
scraped: 2026-02-06T16:19:24.790909
---

# Ingest traces

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

## Related topics

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Get started with OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry/getting-started "How to get your OpenTelemetry data into Dynatrace.")
* [Extend distributed tracing](/docs/ingest-from/extend-dynatrace/extend-tracing "Learn how to extend trace observability in Dynatrace.")
* [Adaptive Traffic Management for distributed tracing](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management provides dynamic sampling to ensure that the amount of capture traces stays within the Full-Stack Monitoring included trace volume.")