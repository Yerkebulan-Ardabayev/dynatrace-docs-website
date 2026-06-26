---
title: Настройка метрических событий для оповещений
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-set-up-metric-events-for-alerting
scraped: 2026-05-12T11:27:37.022242
---

# Настройка метрических событий для оповещений

# Настройка метрических событий для оповещений

* Практическое руководство
* Чтение: 16 мин
* Опубликовано 19 января 2024 г.

Для настройки метрических событий для оповещений

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. В разделе **Metric events for alerting** нажмите **Manage alerting rules**.
3. На странице **Metric events for alerting** можно создавать, включать/отключать и настраивать рекомендованные правила оповещений.

Для обзора всех рекомендованных правил оповещений для всех поддерживаемых сервисов см. список ниже.

### Список предустановленных правил оповещений для каждого поддерживаемого сервиса

| Название | Правила оповещений |
| --- | --- |
| Amazon MQ | Amazon MQ store percent usage (Статический порог: выше 95 %), Amazon MQ temp percent usage (Статический порог: выше 95 %), Amazon MQ memory usage (by topic) (Статический порог: выше 95 %), Amazon MQ memory usage (by queue) (Статический порог: выше 95 %), Amazon MQ CPU utilization (Статический порог: выше 95 %), Amazon MQ heap usage (Статический порог: выше 95 %), Amazon MQ job scheduler store percent usage (Статический порог: выше 95 %), Amazon RabbitMQ CPU utilization (Статический порог: выше 95 %) |
| AWS App Runner | AWS App Runner CPU utilization (by instance/service ID) (Статический порог: выше 95 %) |
| Amazon AppStream | Amazon AppStream capacity utilization (Статический порог: выше 95 %) |
| Amazon Aurora | Amazon Aurora CPU utilization (average, by region) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (average, by region/engine) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (average, by region/database class) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (average) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (average, by role) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (maximum, by region) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (maximum, by region/engine) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (maximum, by region/database class) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (maximum) (Статический порог: выше 95 %), Amazon Aurora CPU utilization (maximum, by role) (Статический порог: выше 95 %) |
| Amazon Keyspaces | Amazon Keyspaces account provisioned read capacity utilization (by region) (Статический порог: выше 95 %), Amazon Keyspaces account provisioned write capacity utilization (by region) (Статический порог: выше 95 %), Amazon Keyspaces max provisioned table read capacity utilization (by region) (Статический порог: выше 95 %), Amazon Keyspaces max provisioned table write capacity utilization (by region) (Статический порог: выше 95 %) |
| Amazon CloudFront | Amazon CloudFront total error rate (by region) (Статический порог: выше 5 %), Amazon CloudFront 4xx error rate (by region) (Статический порог: выше 5 %), Amazon CloudFront 5xx error rate (by region) (Статический порог: выше 5 %) |
| Amazon CloudSearch | Amazon CloudSearch index utilization (Статический порог: выше 95 %) |
| AWS CodeBuild | AWS CodeBuild CPU utilized percent (Статический порог: выше 95 %), AWS CodeBuild CPU utilized percent (by build id/build number) (Статический порог: выше 95 %), AWS CodeBuild memory utilized percent (Статический порог: выше 95 %), AWS CodeBuild memory utilized percent (by build id/build number) (Статический порог: выше 95 %) |
| Amazon Connect | Amazon Connect the percentage of the concurrent calls service quota (by metric group) (Статический порог: выше 95 %) |
| Amazon Elastic Kubernetes Service (EKS) | Amazon EKS Node CPU utilization (by instance id/node name) (Статический порог: выше 95 %), Amazon EKS Node memory utilization (by instance id/node name) (Статический порог: выше 95 %), Amazon EKS Pod CPU utilization over pod limit (by namespace) (Статический порог: выше 95 %), Amazon EKS Pod CPU utilization over pod limit (by namespace/pod name) (Статический порог: выше 95 %), Amazon EKS Pod CPU utilization over pod limit (Статический порог: выше 95 %), Amazon EKS Node filesystem utilization (by instance id/node name) (Статический порог: выше 95 %), Amazon EKS Pod memory utilization (by namespace) (Статический порог: выше 95 %), Amazon EKS Pod memory utilization (by namespace/pod name) (Статический порог: выше 95 %), Amazon EKS Service Pod memory utilization (Статический порог: выше 95 %), Amazon EKS Pod CPU utilization (by namespace) (Статический порог: выше 95 %), Amazon EKS Pod CPU utilization (by namespace/pod name) (Статический порог: выше 95 %), Amazon EKS Pod CPU utilization (Статический порог: выше 95 %), Amazon EKS Pod CPU reserved capacity (by namespace/pod name) (Статический порог: выше 95 %), Amazon EKS Pod CPU reserved capacity (Статический порог: выше 95 %), Amazon EKS Pod memory utilization over pod limit (by namespace) (Статический порог: выше 95 %), Amazon EKS Pod memory utilization over pod limit (by namespace/pod name) (Статический порог: выше 95 %), Amazon EKS Pod memory utilization over pod limit (Статический порог: выше 95 %), Amazon EKS Pod memory reserved capacity (by namespace/pod name) (Статический порог: выше 95 %), Amazon EKS Pod memory reserved capacity (Статический порог: выше 95 %), Amazon EKS Node CPU reserved capacity (by instance id/node name) (Статический порог: выше 95 %), Amazon EKS Node CPU reserved capacity (Статический порог: выше 95 %), Amazon EKS Node memory reserved capacity (by instance id/node name) (Статический порог: выше 95 %), Amazon EKS Node memory reserved capacity (Статический порог: выше 95 %), Amazon EKS Node CPU utilization (Статический порог: выше 95 %), Amazon EKS Node memory utilization (Статический порог: выше 95 %), Amazon EKS Node filesystem utilization (Статический порог: выше 95 %) |
| Amazon DynamoDB Accelerator (DAX) | Amazon DynamoDB Accelerator CPU utilization (Статический порог: выше 95 %), Amazon DynamoDB Accelerator CPU utilization (by node id) (Статический порог: выше 95 %), Amazon DynamoDB Accelerator CPU utilization (by region) (Статический порог: выше 95 %) |
| AWS Database Migration Service | AWS Database Migration Service CPU utilization (by replication task identifier) (Статический порог: выше 95 %), AWS Database Migration Service CPU utilization (Статический порог: выше 95 %), AWS Database Migration Service CPU utilization (by replication instance/external resource id) (Статический порог: выше 95 %), AWS Database Migration Service CPU utilization (by region) (Статический порог: выше 95 %), AWS Database Migration Service CPU utilization (by region/instance class) (Статический порог: выше 95 %) |
| Amazon DocumentDB | Amazon DocumentDB CPU utilization (by region/DB instance identifier) (Статический порог: выше 95 %), Amazon DocumentDB CPU utilization (by role) (Статический порог: выше 95 %), Amazon DocumentDB CPU utilization (Статический порог: выше 95 %) |
| Amazon Elastic Container Service (ECS) | Amazon ECS CPU reservation (Статический порог: выше 95 %), Amazon ECS CPU utilization (Статический порог: выше 95 %), Amazon ECS CPU utilization (by service name) (Статический порог: выше 95 %), Amazon ECS Memory reservation (Статический порог: выше 95 %), Amazon ECS Memory utilization (Статический порог: выше 95 %), Amazon ECS Memory utilization (by service name) (Статический порог: выше 95 %) |
| Amazon ECS ContainerInsights | Amazon ECS ContainerInsights instance memory utilization (by container instance id/instance id) (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance memory utilization (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance memory reserved capacity (by container instance id/instance id) (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance memory reserved capacity (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance CPU utilization (by container instance id/instance id) (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance CPU utilization (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance filesystem utilization (by container instance id/instance id) (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance filesystem utilization (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance CPU reserved capacity (by container instance id/instance id) (Статический порог: выше 95 %), Amazon ECS ContainerInsights instance CPU reserved capacity (Статический порог: выше 95 %) |
| Amazon ElastiCache (EC) | Amazon ElastiCache CPU utilization (Статический порог: выше 95 %), Amazon ElastiCache CPU utilization (by cache/node id) (Статический порог: выше 95 %), Amazon ElastiCache engine CPU utilization (Статический порог: выше 95 %), Amazon ElastiCache engine CPU utilization (by cache/node id) (Статический порог: выше 95 %) |
| AWS Elastic Beanstalk | AWS Elastic Beanstalk root filesystem util (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk root filesystem util (Статический порог: выше 95 %), AWS Elastic Beanstalk load average 1min (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk load average 5min (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU user (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU nice (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU idle (by instance id) (Статический порог: ниже 5 %), AWS Elastic Beanstalk CPU IO wait (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU irq (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU softirq (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU system (by instance id) (Статический порог: выше 95 %), AWS Elastic Beanstalk CPU privileged (by instance id) (Статический порог: выше 95 %) |
| Amazon Elastic File System (EFS) | Amazon EFS percent IO limit (Статический порог: выше 95 %) |
| Amazon Elastic Inference | Amazon Elastic Inference accelerator utilization (by Elastic Inference accelerator id) (Статический порог: выше 95 %) |
| Amazon Elastic Map Reduce (EMR) | Amazon Elastic MapReduce YARN memory available percentage (Статический порог: ниже 5 %), Amazon Elastic MapReduce YARN memory available percentage (by job id) (Статический порог: ниже 5 %), Amazon Elastic MapReduce HDFS utilization (Статический порог: выше 95 %), Amazon Elastic MapReduce HDFS utilization (by job id) (Статический порог: выше 95 %) |
| Amazon Elasticsearch Service (ES) | Amazon Elasticsearch Service CPU utilization (maximum, by client id) (Статический порог: выше 95 %), Amazon Elasticsearch Service CPU utilization (by client id) (Статический порог: выше 95 %), Amazon Elasticsearch Service JVM memory pressure (high, by client id) (Статический порог: выше 75 %), Amazon Elasticsearch Service JVM memory pressure (critical, by client id) (Статический порог: выше 90 %), Amazon Elasticsearch Service master CPU utilization (by client id) (Статический порог: выше 95 %), Amazon Elasticsearch Service master JVM memory pressure (high) (Статический порог: выше 75 %), Amazon Elasticsearch Service master JVM memory pressure (critical) (Статический порог: выше 90 %) |
| Amazon GameLift | Amazon GameLift percent idle instances (Статический порог: ниже 5 %), Amazon GameLift percent idle instances (by region/metric groups) (Статический порог: ниже 5 %), Amazon GameLift percent healthy server processes (Статический порог: ниже 95 %), Amazon GameLift Percent healthy server processes (by region/metric groups) (Статический порог: ниже 95 %), Amazon GameLift percent available game sessions (Статический порог: ниже 5 %), Amazon GameLift percent available game sessions (by region/metric groups) (Статический порог: ниже 5 %) |
| AWS Glue | AWS Glue driver JVM heap usage (by job run id/type) (Статический порог: выше 95 %), AWS Glue ALL JVM heap usage (by job run id/type) (Статический порог: выше 95 %), AWS Glue driver CPU system load (by job run id/type) (Статический порог: выше 95 %), AWS Glue ALL CPU system load (by job run id/type) (Статический порог: выше 95 %) |
| Amazon Managed Streaming for Kafka | Amazon Managed Streaming for Kafka root disk used (by broker id) (Статический порог: выше 95 %), Amazon Managed Streaming for Kafka network processor avg idle percent (by broker id) (Статический порог: ниже 5 %), Amazon Managed Streaming for Kafka request handler avg idle percent (by broker id) (Статический порог: ниже 5 %), Amazon Managed Streaming for Kafka app logs disk used (by broker id) (Статический порог: выше 95 %), Amazon Managed Streaming for Kafka data logs disk used (by broker id) (Статический порог: выше 95 %), Amazon Managed Streaming for Kafka the percentage of CPU in user space (by broker id) (Статический порог: выше 95 %), Amazon Managed Streaming for Kafka the percentage of CPU idle time (by broker id) (Статический порог: ниже 5 %), Amazon Managed Streaming for Kafka the percentage of CPU in kernel space (by broker id) (Статический порог: выше 95 %) |
| AWS Lambda | AWS Lambda error rate (based on errorsSum and invocationsSum) (Статический порог: выше 5 %) |
| AWS Elemental MediaConnect | AWS Elemental MediaConnect source packet loss percent (Статический порог: выше 5 %), AWS Elemental MediaConnect packet loss percent (by region) (Статический порог: выше 5 %), AWS Elemental MediaConnect packet loss percent (by region/availability zone) (Статический порог: выше 5 %), AWS Elemental MediaConnect source packet loss percent (by region) (Статический порог: выше 5 %), AWS Elemental MediaConnect source packet loss percent (by region/availability zone) (Статический порог: выше 5 %), AWS Elemental MediaConnect source packet loss percent (by region/source arn) (Статический порог: выше 5 %), AWS Elemental MediaConnect packet loss percent (Статический порог: выше 5 %) |
| Amazon Neptune | Amazon Neptune CPU utilization (Статический порог: выше 95 %), Amazon Neptune CPU utilization (by role) (Статический порог: выше 95 %), Amazon Neptune CPU utilization (by region) (Статический порог: выше 95 %), Amazon Neptune CPU utilization (by region/DB instance identifier) (Статический порог: выше 95 %), Amazon Neptune CPU utilization (by region/database class) (Статический порог: выше 95 %), Amazon Neptune CPU utilization (by region/engine name) (Статический порог: выше 95 %) |
| AWS OpsWorks | AWS OpsWorks CPU system (Статический порог: выше 95 %), AWS OpsWorks CPU user (Статический порог: выше 95 %), AWS OpsWorks CPU nice (Статический порог: выше 95 %), AWS OpsWorks CPU IO wait (Статический порог: выше 95 %), AWS OpsWorks CPU steal (Статический порог: выше 95 %), AWS OpsWorks CPU idle (Статический порог: ниже 5 %), AWS OpsWorks CPU system (by region/instance id) (Статический порог: выше 95 %), AWS OpsWorks CPU system (by region/layer id) (Статический порог: выше 95 %), AWS OpsWorks CPU user (by region/instance id) (Статический порог: выше 95 %), AWS OpsWorks CPU user (by region/layer id) (Статический порог: выше 95 %), AWS OpsWorks CPU nice (by region/instance id) (Статический порог: выше 95 %), AWS OpsWorks CPU nice (by region/layer id) (Статический порог: выше 95 %), AWS OpsWorks CPU IO wait (by region/instance id) (Статический порог: выше 95 %), AWS OpsWorks CPU IO wait (by region/layer id) (Статический порог: выше 95 %), AWS OpsWorks CPU steal (by region/instance id) (Статический порог: выше 95 %), AWS OpsWorks CPU steal (by region/layer id) (Статический порог: выше 95 %), AWS OpsWorks CPU idle (by region/instance id) (Статический порог: ниже 5 %), AWS OpsWorks CPU idle (by region/layer id) (Статический порог: ниже 5 %) |
| Amazon Redshift | Amazon Redshift CPU utilization (Статический порог: выше 95 %), Amazon Redshift CPU utilization (by node id) (Статический порог: выше 95 %), Amazon Redshift percentage disk space used (Статический порог: выше 95 %), Amazon Redshift percentage disk space used (by node id) (Статический порог: выше 95 %) |
| Amazon Route 53 | Amazon Route 53 percentage healthy (by region/health check id) (Статический порог: ниже 95 %) |
| Amazon SageMaker Batch Transform Jobs | Amazon SageMaker Batch Transform Jobs CPU utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Batch Transform Jobs memory utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Batch Transform Jobs GPU utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Batch Transform Jobs GPU memory utilization (by region/host) (Статический порог: выше 95 %) |
| Amazon SageMaker Endpoint Instances | Amazon SageMaker Endpoint Instances CPU utilization (by variant name) (Статический порог: выше 95 %), Amazon SageMaker Endpoint Instances memory utilization (by variant name) (Статический порог: выше 95 %), Amazon SageMaker Endpoint Instances GPU utilization (by variant name) (Статический порог: выше 95 %), Amazon SageMaker Endpoint Instances GPU memory utilization (by variant name) (Статический порог: выше 95 %), Amazon SageMaker Endpoint Instances disk utilization (by variant name) (Статический порог: выше 95 %) |
| Amazon SageMaker Processing Jobs | Amazon SageMaker Processing Jobs CPU utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Processing Jobs memory utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Processing Jobs GPU utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Processing Jobs GPU memory utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Processing Jobs disk utilization (by region/host) (Статический порог: выше 95 %) |
| Amazon SageMaker Training Jobs | Amazon SageMaker Training Jobs CPU utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Training Jobs memory utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Training Jobs GPU utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Training Jobs GPU memory utilization (by region/host) (Статический порог: выше 95 %), Amazon SageMaker Training Jobs disk utilization (by region/host) (Статический порог: выше 95 %) |
| Amazon Simple Email Service (SES) | Amazon SES reputation bounce rate (by region) (Статический порог: выше 5 %), Amazon SES reputation complaint rate (by region) (Статический порог: выше 0,1 %) |
| AWS Storage Gateway | AWS Storage Gateway cache percent dirty (by region/share id) (Статический порог: выше 80 %), AWS Storage Gateway cache percent dirty (by region/volume id) (Статический порог: выше 80 %), AWS Storage Gateway cache percent dirty (by gateway id) (Статический порог: выше 80 %), AWS Storage Gateway user CPU percent (Статический порог: выше 95 %), AWS Storage Gateway IO wait percent (Статический порог: выше 20 %), AWS Storage Gateway upload buffer percent used (by gateway id) (Статический порог: выше 95 %), AWS Storage Gateway working storage percent used (by gateway id) (Статический порог: выше 95 %) |
| AWS Trusted Advisor | AWS Trusted Advisor service limit usage (by region/service limit/service name) (Статический порог: выше 95 %) |

Количество рекомендованных правил оповещений зависит от числа отслеживаемых поддерживаемых сервисов.
Для добавления рекомендованных правил оповещений для нового поддерживаемого сервиса сначала необходимо добавить его в мониторинг.

Как добавить сервис в мониторинг

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS нажмите кнопку редактирования (значок карандаша) для экземпляра AWS, который требуется изменить.
3. Нажмите **Manage services** и **Add service**, выберите имя сервиса из списка и нажмите **Add service**.
4. Нажмите **Save changes**.

![Add AWS service](https://dt-cdn.net/images/2021-01-08-09-20-20-1250-d30e419947.png)

Add AWS service

Обратите внимание, что не для всех поддерживаемых сервисов предусмотрены собственные предустановленные правила оповещений.

1. Создайте и включите правила оповещений.

   Для включения рекомендованных правил оповещений сначала необходимо их создать. Можно создать правила оповещений и автоматически включить их, либо (если снять флажок **Automatically enable created rules**) создать их и включить вручную после возможных изменений конфигурации.

   ![Create alerting rules AWS](https://dt-cdn.net/images/2021-01-08-09-31-46-1066-8094b276de.png)

   Create alerting rules AWS

   Например, можно создать и автоматически включить первый пакет оповещений. При начале мониторинга новых сервисов можно создать оповещения для них без автоматического включения (если сначала требуется их настроить).
2. Настройте правила оповещений.
   Способ редактирования правил зависит от того, было ли выбрано автоматическое включение оповещений.

   * Если при создании было выбрано автоматическое включение оповещений, перейдите в **Adjust recommended alerting rules**, разверните **Enabled recommended alerting rules** и выберите любое правило. Откроется страница **Edit custom event for alerting**, где можно изменить правила конфигурации для конкретного сервиса.

     ![Conf alerts AWS](https://dt-cdn.net/images/2021-01-08-09-38-16-764-929c3322ec.png)

     Conf alerts AWS
   * Если при создании автоматическое включение оповещений не было выбрано, перейдите в **Enable recommended alerting rules**, разверните **Disabled recommended alerting rules** и выберите любое отключённое правило. Откроется та же страница **Edit custom event for alerting**.

     ![Enable rules AWS](https://dt-cdn.net/images/2021-01-08-09-40-39-1101-7b646572a9.png)

     Enable rules AWS
3. Отключите правила оповещений.
4. Можно отключить все правила оповещений или выборочно отключить/удалить отдельные.

   ![Disable rules AWS](https://dt-cdn.net/images/2021-01-08-09-42-55-1088-75a3e8656b.png)

   Disable rules AWS

   * Для отключения всех правил оповещений перейдите в **Adjust recommended alerting rules** и нажмите **Disable all enabled recommended alerting rules**.
   * Для выборочного отключения или удаления правил оповещений перейдите в **Adjust recommended alerting rules** и выберите **Metric events**. На странице **Metric events** можно отключить оповещение в столбце **On/Off** или удалить его, нажав `x` в столбце **Delete**.

   ![Custom events AWS](https://dt-cdn.net/images/2021-01-08-09-45-10-1106-1d8aa30d26.png)

   Custom events AWS

   Если отключить часть или все правила оповещений, их всегда можно включить повторно.

   ![Reenable AWS](https://dt-cdn.net/images/2021-01-08-09-46-58-1110-6a3d0682bb.png)

   Reenable AWS