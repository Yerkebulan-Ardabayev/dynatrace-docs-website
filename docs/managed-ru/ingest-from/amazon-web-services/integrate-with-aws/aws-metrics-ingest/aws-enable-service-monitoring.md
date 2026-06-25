---
title: Включение мониторинга сервиса
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring
scraped: 2026-05-12T12:05:14.495477
---

# Включение мониторинга сервиса

# Включение мониторинга сервиса

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 9 ноября 2023 г.

Чтобы включить мониторинг этого сервиса, сначала необходимо интегрировать Dynatrace с Amazon Web Services:

* [Настройка интеграции Dynatrace SaaS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интеграция метрик из Amazon CloudWatch.")
* [Настройка интеграции Dynatrace Managed](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed "Подключите свою учётную запись Amazon к Dynatrace Managed и начните мониторинг.")

## Добавление сервиса в мониторинг

Чтобы просматривать метрики сервиса, необходимо добавить сервис в мониторинг в вашей среде Dynatrace.

Чтобы добавить сервис в мониторинг

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS прокрутите вниз и выберите нужный экземпляр AWS. Нажмите кнопку **Edit**.
3. Прокрутите вниз и выберите **Add service**. Выберите имя сервиса из выпадающего списка и нажмите **Add service**.
4. Нажмите **Save changes**.

Потребление мониторинга облачных сервисов

Все облачные сервисы потребляют [Davis data units (DDUs)](/managed/license/monitoring-consumption-classic/davis-data-units "Узнайте, как рассчитывается потребление мониторинга Dynatrace на основе Davis data units (DDU)."). Объём потребления DDU на экземпляр сервиса зависит от количества мониторируемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU).

После добавления облачных сервисов AWS в мониторинг может потребоваться от 15 до 20 минут, прежде чем отобразятся значения метрик.

## Мониторинг ресурсов на основе тегов

Вы можете выбрать мониторинг ресурсов на основе существующих тегов AWS, поскольку Dynatrace автоматически импортирует их из экземпляров сервисов. Тем не менее, переход от тегирования AWS к тегированию Dynatrace поддерживается не для всех сервисов AWS. Разверните таблицу ниже, чтобы увидеть, какие облачные сервисы фильтруются по тегам.

### Фильтрация по тегам для каждого сервиса

| Имя | Мониторинг и фильтрация по тегам |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | да |
| AWS Lambda (built-in) | да |
| Amazon Application and Network Load Balancer (built-in) | да |
| Amazon DynamoDB (built-in) | да |
| Amazon EBS (built-in) | да |
| Amazon EC2 (built-in) | да |
| Amazon Elastic Load Balancer (ELB) (built-in) | да |
| Amazon RDS (built-in) | да |
| Amazon S3 (built-in) | да |
| AWS Certificate Manager Private Certificate Authority | да |
| Amazon API Gateway | да |
| AWS App Runner | да |
| Amazon AppStream | да |
| AWS AppSync | да |
| Amazon Athena | да |
| Amazon Aurora | да |
| Amazon EC2 Auto Scaling | - |
| AWS Billing | - |
| Amazon Keyspaces | да |
| AWS Chatbot | - |
| Amazon CloudFront | да |
| AWS CloudHSM | да |
| Amazon CloudSearch | - |
| AWS CodeBuild | да |
| Amazon Cognito | - |
| Amazon Connect | - |
| AWS DataSync | да |
| Amazon DynamoDB Accelerator (DAX) | да |
| AWS Database Migration Service (AWS DMS) | да |
| Amazon DocumentDB | да |
| AWS Direct Connect | да |
| Amazon DynamoDB | да |
| Amazon EBS | да |
| Amazon EC2 Spot Fleet | - |
| Amazon EC2 API | - |
| Amazon Elastic Container Service (ECS) | да |
| Amazon ECS Container Insights | да |
| Amazon Elastic File System (EFS) | да |
| Amazon Elastic Kubernetes Service (EKS) | да |
| Amazon ElastiCache (EC) | да |
| AWS Elastic Beanstalk | да |
| Amazon Elastic Inference | да |
| Amazon Elastic Transcoder | - |
| Amazon Elastic Map Reduce (EMR) | да |
| Amazon Elasticsearch Service (ES) | да |
| Amazon EventBridge | да |
| Amazon FSx | да |
| Amazon GameLift | - |
| AWS Glue | да |
| Amazon Inspector | да |
| AWS Internet of Things (IoT) | - |
| AWS IoT Things Graph | - |
| AWS IoT Analytics | - |
| Amazon Managed Streaming for Kafka | да |
| Amazon Kinesis Data Analytics | да |
| Amazon Data Firehose | да |
| Amazon Kinesis Data Streams | да |
| Amazon Kinesis Video Streams | да |
| AWS Lambda | да |
| Amazon Lex | да |
| Amazon CloudWatch Logs | да |
| AWS Elemental MediaTailor | да |
| AWS Elemental MediaConnect | - |
| AWS Elemental MediaConvert | да |
| AWS Elemental MediaPackage Live | да |
| AWS Elemental MediaPackage Video on Demand | да |
| Amazon MQ | - |
| Amazon VPC NAT Gateways | да |
| Amazon Neptune | да |
| AWS OpsWorks | да |
| Amazon Polly | - |
| Amazon QLDB | да |
| Amazon RDS | да |
| Amazon Redshift | да |
| Amazon Rekognition | - |
| AWS RoboMaker | да |
| Amazon Route 53 | да |
| Amazon Route 53 Resolver | да |
| Amazon S3 | да |
| Amazon SageMaker Batch Transform Jobs | - |
| Amazon SageMaker Endpoints | да |
| Amazon SageMaker Endpoint Instances | да |
| Amazon SageMaker Ground Truth | - |
| Amazon SageMaker Processing Jobs | - |
| Amazon SageMaker Training Jobs | - |
| AWS Service Catalog | - |
| Amazon Simple Email Service (SES) | - |
| Amazon Simple Notification Service (SNS) | да |
| Amazon Simple Queue Service (SQS) | да |
| AWS Systems Manager - Run Command | - |
| AWS Step Functions | - |
| AWS Storage Gateway | да |
| Amazon SWF | - |
| Amazon Textract | - |
| AWS Transfer Family | да |
| AWS Transit Gateway | да |
| Amazon Translate | - |
| AWS Trusted Advisor | - |
| AWS API Usage | - |
| AWS Site-to-Site VPN | да |
| AWS WAF Classic | - |
| AWS WAF | - |
| Amazon WorkMail | да |
| Amazon WorkSpaces | да |

Чтобы настроить мониторинг ресурсов на основе тегов

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS** > **Edit** для нужного экземпляра AWS.
2. Для **Resources to be monitored** выберите **Monitor resources selected by tags**.
3. Введите **Key** и **Value**.
4. Нажмите **Save**.

## Настройка метрик сервиса

После добавления сервиса Dynatrace автоматически начинает собирать набор метрик для этого конкретного сервиса. Это **рекомендуемые** метрики.

Метрики уровня сервиса собираются для всего сервиса по всем регионам. Обычно такие метрики содержат измерения с именем **Region**. При выборе они отображаются на отдельной диаграмме при просмотре вашего развёртывания AWS в Dynatrace. Учтите, что доступные измерения различаются между сервисами.

Чтобы изменить **статистики** метрики, её нужно пересоздать, выбрав другие статистики. Можно выбирать из следующих статистик: **Sum**, **Minimum**, **Maximum**, **Average** и **Sample count**. Статистики **Average + Minimum + Maximum** позволяют собирать все три статистики как одну метрику вместо одной статистики на три отдельные метрики. Это может снизить ваши расходы на получение метрик из развёртывания AWS.

### Рекомендуемые метрики

* Включены по умолчанию
* Не могут быть отключены
* Могут иметь рекомендуемые измерения (включены по умолчанию, не могут быть отключены)
* Могут иметь необязательные измерения (отключены по умолчанию, могут быть включены)

### Необязательные метрики

Помимо рекомендуемых метрик, большинство сервисов имеют возможность включения **необязательных** метрик.

* Могут быть добавлены и настроены вручную

### Добавление и настройка метрик

1. Перейдите в **Settings** > **Cloud and virtualization** > **AWS**.
2. На странице обзора AWS прокрутите вниз и нажмите **Edit** для нужного экземпляра AWS.
3. Прокрутите вниз до раздела **Services** и нажмите **Manage services**.
4. Чтобы добавить метрику, выберите сервис, для которого хотите добавить метрики.
5. Нажмите **Add new metric**.
6. В меню выберите нужную метрику.
7. Нажмите **Add metric**, чтобы добавить метрику в мониторинг.
8. Чтобы настроить метрику, нажмите **Edit**.
9. Нажмите **Apply**, чтобы сохранить вашу конфигурацию.