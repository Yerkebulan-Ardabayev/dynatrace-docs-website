---
title: Ограничение API-вызовов к AWS с помощью тегов
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/limit-api-calls-to-aws-using-tags
scraped: 2026-05-12T11:27:39.491231
---

# Ограничение API-вызовов к AWS с помощью тегов

# Ограничение API-вызовов к AWS с помощью тегов

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 19 июля 2017 г.

По умолчанию Dynatrace отслеживает все сервисы Amazon Web Services, указанные в политике разрешений. При необходимости можно использовать теги для ограничения ресурсов AWS (экземпляров сервисов AWS), отслеживаемых Dynatrace.

## Добавление тегов в AWS

Чтобы добавить тег

1. Войдите в AWS Management Console и перейдите на дашборд сервиса, которому необходимо присвоить тег.
2. Выберите **Instances**, чтобы просмотреть список окружений, затем выберите экземпляр.
3. На панели под списком выберите **Tags**.
4. Выберите **Add/Edit tags**, затем **Create tag**.
5. Введите пару ключ/значение тега (например, 'monitor\_dynatrace' для **Key** и 'true' для **Value**).
6. Нажмите **Save**.

Теги мониторинга Dynatrace работают со встроенными сервисами: EC2, RDS, ELB, EBS, группами автомасштабирования, DynamoDB, Lambda, а также большинством облачных сервисов.
Раскройте таблицу ниже, чтобы узнать, для каких сервисов доступна фильтрация по тегам.

### Фильтрация по тегам для каждого сервиса

| Название | Мониторинг и фильтрация по тегам |
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

## Настройка Dynatrace для использования тегов AWS

Dynatrace позволяет использовать до 10 тегов AWS одновременно. После настройки Dynatrace учитывает сервисы с тегами при запросе счётчиков производительности.

Пары ключ/значение тегов AWS обрабатываются с оператором OR. Ключи не обязаны быть уникальными.

Мониторинг AWS на основе тегов обладает высокой гибкостью и особенно полезен, если:

* используется несколько окружений Dynatrace и нужно отслеживать отдельные сервисы AWS, работающие в одной учётной записи AWS.
  **Примеры тегов:** `monitor_dynatrace : myenvironment1; monitor_dynatrace : myenvironment2`
* необходимо отслеживать одну учётную запись AWS, но разделять сервисы производственной среды и среды тестирования.
  **Примеры тегов:**
  `monitor_dynatrace : production; monitor_dynatrace : staging`

Чтобы назначить теги конкретному экземпляру AWS

1. [Настройте Dynatrace для мониторинга AWS](/managed/observe/infrastructure-observability/cloud-platform-monitoring/aws-monitoring "Мониторинг AWS с помощью Dynatrace").
2. В Dynatrace перейдите в **Settings** > **Cloud and virtualization** > **AWS** и выберите экземпляр AWS.
3. В поле **Resources to be monitored** выберите **Monitor resources selected by tags**.
4. Введите **Key** и **Value**.
5. Нажмите **Save**.