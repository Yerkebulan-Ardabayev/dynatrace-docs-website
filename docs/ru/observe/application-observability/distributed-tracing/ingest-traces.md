---
title: Ingest traces
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/ingest-traces
scraped: 2026-03-06T21:12:03.627298
---

# Приём трейсов

# Приём трейсов

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Feb 07, 2025

Вы можете использовать OneAgent или интеграцию с OpenTelemetry для добавления трейсов в Dynatrace, включая данные трейсов из специальных расширений для сторонних систем, таких как Serverless-функции и Adobe Experience Manager (AEM) Cloud Service. Это обеспечивает сбор детальных данных трейсов для анализа поведения и производительности ваших приложений.

* OneAgent

  Dynatrace OneAgent — это самый простой способ сбора данных трейсов. Установив OneAgent на ваши хосты, вы можете автоматически собирать распределённые трейсы из ваших приложений.
* Интеграция с OpenTelemetry

  Если вы используете OpenTelemetry, вы можете настроить его для отправки данных трейсов в Dynatrace. Для этого необходимо настроить OpenTelemetry Collector и сконфигурировать его для экспорта трейсов в Dynatrace.

Выберите один из следующих вариантов, чтобы узнать больше о конфигурации.

Облачные рабочие нагрузки

#### AWS

[AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration) [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate) [Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Amazon ECS](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs) [Amazon EKS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk) [Все облачные сервисы AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services)

#### Microsoft Azure

[Метрики Azure Monitor](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide) [Логи Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure) [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks) [Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice) [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [Azure Virtual Machine Scale Set (VMSS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring) [Все облачные сервисы Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics)

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke) [Все сервисы Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new)

Kubernetes

[Кластер Kubernetes](/docs/ingest-from/setup-on-k8s/deployment) [Envoy](/docs/ingest-from/opentelemetry/integrations/envoy) [Istio](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment)

На основе хоста

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

[Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine)

OpenTelemetry

[OpenTelemetry](/docs/ingest-from/opentelemetry)

Другие варианты настройки

[Graal VM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image) [GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops) [Docker](/docs/ingest-from/setup-on-container-platforms/docker) [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [Приём данных в Dynatrace](/docs/ingest-from)

## Связанные темы

* [Dynatrace OneAgent](/docs/ingest-from/dynatrace-oneagent "Ознакомьтесь с основными концепциями OneAgent и узнайте, как установить и использовать OneAgent на различных платформах.")
* [Начало работы с OpenTelemetry и Dynatrace](/docs/ingest-from/opentelemetry/getting-started "Как отправить данные OpenTelemetry в Dynatrace.")
* [Расширение распределённой трассировки](/docs/ingest-from/extend-dynatrace/extend-tracing "Узнайте, как расширить наблюдаемость трейсов в Dynatrace.")
* [Adaptive Traffic Management для распределённой трассировки](/docs/ingest-from/dynatrace-oneagent/adaptive-traffic-management "Dynatrace Adaptive Traffic Management обеспечивает динамическую выборку для контроля объёма захваченных трейсов в рамках включённого объёма трейсов Full-Stack Monitoring.")
