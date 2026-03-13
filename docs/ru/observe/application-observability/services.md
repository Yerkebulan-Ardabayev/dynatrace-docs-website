---
title: Services
source: https://www.dynatrace.com/docs/observe/application-observability/services
scraped: 2026-03-06T21:10:36.219731
---

# Сервисы

# Сервисы

* Latest Dynatrace
* Overview
* 4-min read
* Updated on Oct 23, 2025

Сервисы -- это фундаментальные строительные блоки приложений. С точки зрения наблюдаемости они предоставляют владельцам приложений критически важные метрики для мониторинга состояния приложений.

[![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](services/services-app.md "Централизованный контроль состояния, производительности и ресурсов сервисов с помощью приложения Services.") предоставляет детальную информацию о производительности и состоянии ваших сервисов и включает полезные функции, такие как [Service flow](services-classic/service-flow.md "Узнайте, как Dynatrace помогает отследить последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.") и [Backtrace](services-classic/service-backtrace.md "Отследите последовательность вызовов сервисов до самого нажатия в браузере, которое инициировало цепочку вызовов.").

## Предварительные требования

### Разрешения

Проверьте минимальный набор разрешений, необходимых для запуска ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**.

storage:events:read

Запрос событий из Grail

storage:entities:read

Запрос сущностей из Grail

storage:logs:read

Запрос логов из Grail

storage:spans:read

Чтение данных span

storage:metrics:read

Запрос метрик из Grail

storage:buckets:read

Чтение бакетов

storage:smartscape:read

Чтение узлов и связей Smartscape

hub:catalog:read

Чтение информации о релизах

storage:fieldsets:read

Чтение наборов полей из Grail

storage:filter-segments:read

Чтение сегментов фильтров

### Установка

Убедитесь, что ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** [установлен в вашей среде](../../manage/hub.md#install "См. информацию о Dynatrace Hub.").

## Начало работы

![Просмотр производительности всех сервисов в реальном времени. Поиск конкретных сервисов с помощью мощных фильтров.](https://cdn.hub.central.dynatrace.com/hub/1_DI39YNS_hQ7gBgG.png)![Анализ запросов к базам данных, выполняемых вашими сервисами, для выявления операций, потребляющих наибольшее количество ресурсов.](https://cdn.hub.central.dynatrace.com/hub/2_previously_5_7LmaiBa.png)![Используйте автоматический анализ первопричин Dynatrace Intelligence для быстрого обнаружения и определения источника проблем в сервисах вашего приложения, ускоряя анализ.](https://cdn.hub.central.dynatrace.com/hub/3_lHZzEjb_zyT76Yj.png)![Анализ сбоев с сравнением временных интервалов.](https://cdn.hub.central.dynatrace.com/hub/failure-analysis-1990-6b9d85e513_38quxQP.png)

1 из 4 -- Просмотр производительности всех сервисов в реальном времени. Поиск конкретных сервисов с помощью мощных фильтров.

В Dynatrace перейдите в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, чтобы запустить приложение.

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** предоставляет детальную информацию о производительности и состоянии ваших сервисов. Используйте его для анализа сбоев, времени отклика, производительности запросов и обработки сообщений. Вы также можете фильтровать по ключевым атрибутам, например пространствам имён Kubernetes или HTTP-эндпоинтам, и исследовать взаимосвязи с Kubernetes, хостами и облачной инфраструктурой. Кроме того, вы можете просматривать логи, генерируемые вашими сервисами, и переходить непосредственно в [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](distributed-tracing/distributed-tracing-app.md "Откройте для себя возможности нового приложения Distributed Tracing.") для более глубокого анализа конкретных транзакций.

Подробнее см. [Приложение Services](services/services-app.md "Централизованный контроль состояния, производительности и ресурсов сервисов с помощью приложения Services.").

## Добавление сервисов в Dynatrace

Добавляйте сервисы в Dynatrace с помощью OneAgent или интеграции OpenTelemetry.

Оба варианта обеспечивают сбор метрик, трассировок и логов и включают поддержку бессерверных функций.

Выберите один из следующих вариантов для получения дополнительной информации:

Облачные рабочие нагрузки

#### AWS

[AWS Lambda](../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration.md) [AWS Fargate](../../ingest-from/amazon-web-services/integrate-into-aws/aws-fargate.md) [Amazon EC2](../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Amazon ECS](../../ingest-from/amazon-web-services/integrate-into-aws/aws-ecs.md) [Amazon EKS](../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks.md) [AWS App Runner](../../ingest-from/amazon-web-services/integrate-into-aws/app-runner.md) [AWS Elastic Beanstalk](../../ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk.md) [Все облачные сервисы AWS](../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md)

#### Microsoft Azure

[Метрики Azure Monitor](../../ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide.md) [Логи Azure](../../ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure.md) [Azure Kubernetes Service (AKS)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-aks.md) [Azure App Service](../../ingest-from/microsoft-azure-services/azure-integrations/azure-appservice.md) [Azure Functions](../../ingest-from/microsoft-azure-services/azure-integrations/azure-functions.md) [Azure Virtual Machines (VM)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [Azure Virtual Machine Scale Set (VMSS)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-vmss.md) [Azure Service Fabric](../../ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric.md) [Azure Spring Apps](../../ingest-from/microsoft-azure-services/azure-integrations/azure-spring.md) [Все облачные сервисы Azure](../../ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics.md)

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](../../ingest-from/google-cloud-platform/gcp-integrations/cloudrun.md) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](../../ingest-from/google-cloud-platform/gcp-integrations/gcp-functions.md) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](../../ingest-from/google-cloud-platform/gcp-integrations/google-app-engine.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](../../ingest-from/google-cloud-platform/gcp-integrations/google-gke.md) [Все сервисы Google Cloud](../../ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new.md)

Kubernetes

[Кластер Kubernetes](../../ingest-from/setup-on-k8s/deployment.md) [Envoy](../../ingest-from/opentelemetry/integrations/envoy.md) [Istio](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment.md)

На базе хоста

[AIX](../../ingest-from/dynatrace-oneagent/installation-and-operation/aix.md) [Linux](../../ingest-from/dynatrace-oneagent/installation-and-operation/linux.md) [Solaris](../../ingest-from/dynatrace-oneagent/installation-and-operation/solaris.md) [Windows](../../ingest-from/dynatrace-oneagent/installation-and-operation/windows.md) [zOS](../../ingest-from/dynatrace-oneagent/installation-and-operation/zos.md)

[Amazon EC2](../../ingest-from/amazon-web-services/integrate-into-aws/aws-ec2.md) [Azure Virtual Machines (VM)](../../ingest-from/microsoft-azure-services/azure-integrations/azure-vm.md) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](../../ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine.md)

OpenTelemetry

[OpenTelemetry](../../ingest-from/opentelemetry.md)

Другие варианты настройки

[Graal VM Native Image](../../ingest-from/technology-support/application-software/java/graalvm-native-image.md) [GitOps](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops.md) [Docker](../../ingest-from/setup-on-container-platforms/docker.md) [Heroku](../../ingest-from/setup-on-container-platforms/heroku.md) [Приём данных в Dynatrace](../../ingest-from.md)

[#### Service flow

Узнайте, как Dynatrace помогает отследить последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.

* How-to guide

Читать руководство](services-classic/service-flow.md)[#### Service backtrace

Отследите последовательность вызовов сервисов до самого нажатия в браузере, которое инициировало цепочку вызовов.

* How-to guide

Читать руководство](services-classic/service-backtrace.md)

## Связанные темы

* [Service flow](services-classic/service-flow.md "Узнайте, как Dynatrace помогает отследить последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.")
* [Distributed Traces Classic](distributed-traces.md "Получите наблюдаемость в высокораспределённых облачных архитектурах для эффективной трассировки и анализа транзакций в реальном времени.")
