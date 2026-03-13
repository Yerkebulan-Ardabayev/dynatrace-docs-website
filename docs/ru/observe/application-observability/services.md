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

[![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Централизованный контроль состояния, производительности и ресурсов сервисов с помощью приложения Services.") предоставляет детальную информацию о производительности и состоянии ваших сервисов и включает полезные функции, такие как [Service flow](/docs/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает отследить последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.") и [Backtrace](/docs/observe/application-observability/services-classic/service-backtrace "Отследите последовательность вызовов сервисов до самого нажатия в браузере, которое инициировало цепочку вызовов.").

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

Убедитесь, что ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** [установлен в вашей среде](/docs/manage/hub#install "См. информацию о Dynatrace Hub.").

## Начало работы

![Просмотр производительности всех сервисов в реальном времени. Поиск конкретных сервисов с помощью мощных фильтров.](https://cdn.hub.central.dynatrace.com/hub/1_DI39YNS_hQ7gBgG.png)![Анализ запросов к базам данных, выполняемых вашими сервисами, для выявления операций, потребляющих наибольшее количество ресурсов.](https://cdn.hub.central.dynatrace.com/hub/2_previously_5_7LmaiBa.png)![Используйте автоматический анализ первопричин Dynatrace Intelligence для быстрого обнаружения и определения источника проблем в сервисах вашего приложения, ускоряя анализ.](https://cdn.hub.central.dynatrace.com/hub/3_lHZzEjb_zyT76Yj.png)![Анализ сбоев с сравнением временных интервалов.](https://cdn.hub.central.dynatrace.com/hub/failure-analysis-1990-6b9d85e513_38quxQP.png)

1 из 4 -- Просмотр производительности всех сервисов в реальном времени. Поиск конкретных сервисов с помощью мощных фильтров.

В Dynatrace перейдите в ![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**, чтобы запустить приложение.

![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services** предоставляет детальную информацию о производительности и состоянии ваших сервисов. Используйте его для анализа сбоев, времени отклика, производительности запросов и обработки сообщений. Вы также можете фильтровать по ключевым атрибутам, например пространствам имён Kubernetes или HTTP-эндпоинтам, и исследовать взаимосвязи с Kubernetes, хостами и облачной инфраструктурой. Кроме того, вы можете просматривать логи, генерируемые вашими сервисами, и переходить непосредственно в [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing/distributed-tracing-app "Откройте для себя возможности нового приложения Distributed Tracing.") для более глубокого анализа конкретных транзакций.

Подробнее см. [Приложение Services](/docs/observe/application-observability/services/services-app "Централизованный контроль состояния, производительности и ресурсов сервисов с помощью приложения Services.").

## Добавление сервисов в Dynatrace

Добавляйте сервисы в Dynatrace с помощью OneAgent или интеграции OpenTelemetry.

Оба варианта обеспечивают сбор метрик, трассировок и логов и включают поддержку бессерверных функций.

Выберите один из следующих вариантов для получения дополнительной информации:

Облачные рабочие нагрузки

#### AWS

[AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration) [AWS Fargate](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-fargate) [Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Amazon ECS](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ecs) [Amazon EKS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-beanstalk) [Все облачные сервисы AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services)

#### Microsoft Azure

[Метрики Azure Monitor](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-monitoring-guide) [Логи Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/set-up-log-forwarder-azure) [Azure Kubernetes Service (AKS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-aks) [Azure App Service](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-appservice) [Azure Functions](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [Azure Virtual Machine Scale Set (VMSS)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vmss) [Azure Service Fabric](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-servicefabric) [Azure Spring Apps](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-spring) [Все облачные сервисы Azure](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-cloud-services-metrics)

#### Google Cloud

[![Google Cloud Run (managed)](https://cdn.bfldr.com/B686QPH3/at/7mr6q4h3nv5qjvgccbqm8x5/DT0184.svg?auto=webp&width=72&height=72 "Google Cloud Run (managed)")Google Cloud Run (managed)](/docs/ingest-from/google-cloud-platform/gcp-integrations/cloudrun) [![Google Cloud Functions](https://cdn.bfldr.com/B686QPH3/at/rc58vncw7jkjs8pf5m4wk8p/DT0172.svg?auto=webp&width=72&height=72 "Google Cloud Functions")Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions) [![Google Cloud App Engine](https://cdn.bfldr.com/B686QPH3/at/cs4628s93tzgrqp5vbqvf2x/DT0059.svg?auto=webp&width=72&height=72 "Google Cloud App Engine")Google App Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-app-engine) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine) [![Google Kubernetes Engine](https://cdn.bfldr.com/B686QPH3/at/sz8sx4wfhjf3bsb5m6sbj4k/DT0166.svg?auto=webp&width=72&height=72 "Google Kubernetes Engine")Google Kubernetes Engine (GKE)](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-gke) [Все сервисы Google Cloud](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-supported-service-metrics-new)

Kubernetes

[Кластер Kubernetes](/docs/ingest-from/setup-on-k8s/deployment) [Envoy](/docs/ingest-from/opentelemetry/integrations/envoy) [Istio](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment)

На базе хоста

[AIX](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/aix) [Linux](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/linux) [Solaris](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/solaris) [Windows](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/windows) [zOS](/docs/ingest-from/dynatrace-oneagent/installation-and-operation/zos)

[Amazon EC2](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-ec2) [Azure Virtual Machines (VM)](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-vm) [![Google Compute Engine](https://cdn.bfldr.com/B686QPH3/at/9qpgp4rfnnc556gbwgc32fs4/DT0220.svg?auto=webp&width=72&height=72 "Google Compute Engine")Google Compute Engine](/docs/ingest-from/google-cloud-platform/gcp-integrations/google-compute-engine)

OpenTelemetry

[OpenTelemetry](/docs/ingest-from/opentelemetry)

Другие варианты настройки

[Graal VM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image) [GitOps](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/using-gitops) [Docker](/docs/ingest-from/setup-on-container-platforms/docker) [Heroku](/docs/ingest-from/setup-on-container-platforms/heroku) [Приём данных в Dynatrace](/docs/ingest-from)

[#### Service flow

Узнайте, как Dynatrace помогает отследить последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.

* How-to guide

Читать руководство](/docs/observe/application-observability/services-classic/service-flow)[#### Service backtrace

Отследите последовательность вызовов сервисов до самого нажатия в браузере, которое инициировало цепочку вызовов.

* How-to guide

Читать руководство](/docs/observe/application-observability/services-classic/service-backtrace)

## Связанные темы

* [Service flow](/docs/observe/application-observability/services-classic/service-flow "Узнайте, как Dynatrace помогает отследить последовательность вызовов сервисов, инициированных каждым запросом к сервису в вашей среде.")
* [Distributed Traces Classic](/docs/observe/application-observability/distributed-traces "Получите наблюдаемость в высокораспределённых облачных архитектурах для эффективной трассировки и анализа транзакций в реальном времени.")
