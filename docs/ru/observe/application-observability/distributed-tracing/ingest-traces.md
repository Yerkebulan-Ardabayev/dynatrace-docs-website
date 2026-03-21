---
title: Приём трейсов
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing/ingest-traces
scraped: 2026-03-06T21:12:03.627298
---

Вы можете использовать OneAgent или интеграцию с OpenTelemetry для добавления трейсов в Dynatrace, включая данные трейсов из специальных расширений для сторонних систем, таких как Serverless-функции и Adobe Experience Manager (AEM) Cloud Service. Это обеспечивает сбор подробных данных трейсов для анализа поведения и производительности ваших приложений.

* OneAgent

  Dynatrace OneAgent — это самый простой способ сбора данных трейсов. Установив OneAgent на ваши хосты, вы можете автоматически собирать распределённые трейсы из ваших приложений.
* Интеграция с OpenTelemetry

  Если вы используете OpenTelemetry, вы можете настроить его для отправки данных трейсов в Dynatrace. Для этого необходимо настроить OpenTelemetry Collector и сконфигурировать экспорт трейсов в Dynatrace.

Выберите один из следующих вариантов, чтобы узнать больше о настройке.

Облачные рабочие нагрузки

#### AWS

[AWS Lambda](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration.md) [AWS Fargate](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md) [Amazon EC2](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Amazon ECS](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-ecs.md) [Amazon EKS](../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks.md) [AWS App Runner](../../../ingest-from/amazon-web-services/integrate-into-aws/app-runner.md) [AWS Elastic Beanstalk](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk.md) [Все облачные сервисы AWS](../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md)

#### Microsoft Azure

[Метрики Azure Monitor](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide.md) [Логи Azure](../../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md) [Azure Kubernetes Service (AKS)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-aks.md) [Azure App Service](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-appservice.md) [Azure Functions](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-functions.md) [Виртуальные машины Azure (VM)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [Масштабируемый набор виртуальных машин Azure (VMSS)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-vmss.md) [Azure Service Fabric](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric.md) [Azure Spring Apps](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md) [Все облачные сервисы Azure](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics.md)

#### Google Cloud

[![Google Cloud Run (управляемый)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (управляемый)](../../../ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions.md) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](../../../ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](../../../ingest-from/google-cloud-platform/gcp-integrations/google-gke.md) [Все сервисы Google Cloud](../../../ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new.md)

Kubernetes

[Кластер Kubernetes](../../../ingest-from/setup-on-k8s/deployment.md) [Envoy](../../../ingest-from/opentelemetry/integrations/envoy.md) [Istio](../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment.md)

На базе хостов

[AIX](../../../ingest-from/dynatrace-oneagent/installation-and-operation/aix.md) [Linux](../../../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md) [Solaris](../../../ingest-from/dynatrace-oneagent/installation-and-operation/solaris.md) [Windows](../../../ingest-from/dynatrace-oneagent/installation-and-operation/windows.md) [zOS](../../../ingest-from/dynatrace-oneagent/installation-and-operation/zos.md)

[Amazon EC2](../../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Виртуальные машины Azure (VM)](../../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md)

OpenTelemetry

[OpenTelemetry](../../../ingest-from/opentelemetry.md)

Другие варианты настройки

[Graal VM Native Image](../../../ingest-from/technology-support/application-software/java/graalvm-native-image.md) [GitOps](../../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops.md) [Docker](../../../ingest-from/setup-on-container-platforms/docker.md) [Heroku](../../../ingest-from/setup-on-container-platforms/heroku.md) [Приём данных в Dynatrace](../../../ingest-from.md)

## Связанные темы

* [Dynatrace OneAgent](../../../ingest-from/dynatrace-oneagent.md "Ознакомьтесь с основными концепциями OneAgent и узнайте, как установить и использовать OneAgent на различных платформах.")
* [Начало работы с OpenTelemetry и Dynatrace](../../../ingest-from/opentelemetry/getting-started.md "Как отправить данные OpenTelemetry в Dynatrace.")
* [Расширение распределённой трассировки](../../../ingest-from/extend-dynatrace/extend-tracing.md "Узнайте, как расширить возможности наблюдения за трейсами в Dynatrace.")
* [Адаптивное управление трафиком для распределённой трассировки](../../../ingest-from/dynatrace-oneagent/adaptive-traffic-management.md "Адаптивное управление трафиком Dynatrace обеспечивает динамическую выборку для поддержания объёма собираемых трейсов в рамках лимита, включённого в Full-Stack Monitoring.")
