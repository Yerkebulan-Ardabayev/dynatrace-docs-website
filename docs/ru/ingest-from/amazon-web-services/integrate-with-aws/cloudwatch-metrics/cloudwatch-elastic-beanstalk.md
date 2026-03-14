---
title: Мониторинг AWS Elastic Beanstalk с помощью метрик CloudWatch
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-elastic-beanstalk
scraped: 2026-03-04T21:32:41.685687
---

# Мониторинг AWS Elastic Beanstalk с помощью метрик CloudWatch


* Классический
* Практическое руководство
* Чтение: 6 мин
* Опубликовано 8 сентября 2020 г.

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая AWS Elastic Beanstalk. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимы

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.

Для доступа на основе ролей в развёртывании [SaaS](../cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") необходим [Environment ActiveGate](../../../dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.

* Dynatrace версии 1.201+
* Обновлённая [политика мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.

Чтобы [обновить политику AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

Предопределённая политика JSON для всех поддерживаемых сервисов

```
{


"Version": "2012-10-17",


"Statement": [


{


"Sid": "VisualEditor0",


"Effect": "Allow",


"Action": [


"acm-pca:ListCertificateAuthorities",


"apigateway:GET",


"apprunner:ListServices",


"appstream:DescribeFleets",


"appsync:ListGraphqlApis",


"athena:ListWorkGroups",


"autoscaling:DescribeAutoScalingGroups",


"cloudformation:ListStackResources",


"cloudfront:ListDistributions",


"cloudhsm:DescribeClusters",


"cloudsearch:DescribeDomains",


"cloudwatch:GetMetricData",


"cloudwatch:GetMetricStatistics",


"cloudwatch:ListMetrics",


"codebuild:ListProjects",


"datasync:ListTasks",


"dax:DescribeClusters",


"directconnect:DescribeConnections",


"dms:DescribeReplicationInstances",


"dynamodb:ListTables",


"dynamodb:ListTagsOfResource",


"ec2:DescribeAvailabilityZones",


"ec2:DescribeInstances",


"ec2:DescribeNatGateways",


"ec2:DescribeSpotFleetRequests",


"ec2:DescribeTransitGateways",


"ec2:DescribeVolumes",


"ec2:DescribeVpnConnections",


"ecs:ListClusters",


"eks:ListClusters",


"elasticache:DescribeCacheClusters",


"elasticbeanstalk:DescribeEnvironmentResources",


"elasticbeanstalk:DescribeEnvironments",


"elasticfilesystem:DescribeFileSystems",


"elasticloadbalancing:DescribeInstanceHealth",


"elasticloadbalancing:DescribeListeners",


"elasticloadbalancing:DescribeLoadBalancers",


"elasticloadbalancing:DescribeRules",


"elasticloadbalancing:DescribeTags",


"elasticloadbalancing:DescribeTargetHealth",


"elasticmapreduce:ListClusters",


"elastictranscoder:ListPipelines",


"es:ListDomainNames",


"events:ListEventBuses",


"firehose:ListDeliveryStreams",


"fsx:DescribeFileSystems",


"gamelift:ListFleets",


"glue:GetJobs",


"inspector:ListAssessmentTemplates",


"kafka:ListClusters",


"kinesis:ListStreams",


"kinesisanalytics:ListApplications",


"kinesisvideo:ListStreams",


"lambda:ListFunctions",


"lambda:ListTags",


"lex:GetBots",


"logs:DescribeLogGroups",


"mediaconnect:ListFlows",


"mediaconvert:DescribeEndpoints",


"mediapackage-vod:ListPackagingConfigurations",


"mediapackage:ListChannels",


"mediatailor:ListPlaybackConfigurations",


"opsworks:DescribeStacks",


"qldb:ListLedgers",


"rds:DescribeDBClusters",


"rds:DescribeDBInstances",


"rds:DescribeEvents",


"rds:ListTagsForResource",


"redshift:DescribeClusters",


"robomaker:ListSimulationJobs",


"route53:ListHostedZones",


"route53resolver:ListResolverEndpoints",


"s3:ListAllMyBuckets",


"sagemaker:ListEndpoints",


"sns:ListTopics",


"sqs:ListQueues",


"storagegateway:ListGateways",


"sts:GetCallerIdentity",


"swf:ListDomains",


"tag:GetResources",


"tag:GetTagKeys",


"transfer:ListServers",


"workmail:ListOrganizations",


"workspaces:DescribeWorkspaces"


],


"Resource": "*"


}


]


}
```

Если вы не хотите добавлять разрешения для всех сервисов и предпочитаете выбрать разрешения для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](../aws-all-services.md "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса список дополнительных разрешений, специфичных для этого сервиса.

Разрешения, необходимые для интеграции мониторинга AWS:

* `"cloudwatch:GetMetricData"`
* `"cloudwatch:GetMetricStatistics"`
* `"cloudwatch:ListMetrics"`
* `"sts:GetCallerIdentity"`
* `"tag:GetResources"`
* `"tag:GetTagKeys"`
* `"ec2:DescribeAvailabilityZones"`

### Полный список разрешений для облачных сервисов

| Название | Разрешения |
| --- | --- |
| Все отслеживаемые сервисы Amazon (обязательно) | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
| AWS Certificate Manager Private Certificate Authority | `acm-pca:ListCertificateAuthorities` |
| Amazon MQ |  |
| Amazon API Gateway | `apigateway:GET` |
| AWS App Runner | `apprunner:ListServices` |
| Amazon AppStream | `appstream:DescribeFleets` |
| AWS AppSync | `appsync:ListGraphqlApis` |
| Amazon Athena | `athena:ListWorkGroups` |
| Amazon Aurora | `rds:DescribeDBClusters` |
| Amazon EC2 Auto Scaling | `autoscaling:DescribeAutoScalingGroups` |
| Amazon EC2 Auto Scaling (встроенный) | `autoscaling:DescribeAutoScalingGroups` |
| AWS Billing |  |
| Amazon Keyspaces |  |
| AWS Chatbot |  |
| Amazon CloudFront | `cloudfront:ListDistributions` |
| AWS CloudHSM | `cloudhsm:DescribeClusters` |
| Amazon CloudSearch | `cloudsearch:DescribeDomains` |
| AWS CodeBuild | `codebuild:ListProjects` |
| Amazon Cognito |  |
| Amazon Connect |  |
| Amazon Elastic Kubernetes Service (EKS) | `eks:ListClusters` |
| AWS DataSync | `datasync:ListTasks` |
| Amazon DynamoDB Accelerator (DAX) | `dax:DescribeClusters` |
| AWS Database Migration Service (AWS DMS) | `dms:DescribeReplicationInstances` |
| Amazon DocumentDB | `rds:DescribeDBClusters` |
| AWS Direct Connect | `directconnect:DescribeConnections` |
| Amazon DynamoDB | `dynamodb:ListTables` |
| Amazon DynamoDB (встроенный) | `dynamodb:ListTables`, `dynamodb:ListTagsOfResource` |
| Amazon EBS | `ec2:DescribeVolumes` |
| Amazon EBS (встроенный) | `ec2:DescribeVolumes` |
| Amazon EC2 API |  |
| Amazon EC2 (встроенный) | `ec2:DescribeInstances` |
| Amazon EC2 Spot Fleet | `ec2:DescribeSpotFleetRequests` |
| Amazon Elastic Container Service (ECS) | `ecs:ListClusters` |
| Amazon ECS Container Insights | `ecs:ListClusters` |
| Amazon ElastiCache (EC) | `elasticache:DescribeCacheClusters` |
| AWS Elastic Beanstalk | `elasticbeanstalk:DescribeEnvironments` |
| Amazon Elastic File System (EFS) | `elasticfilesystem:DescribeFileSystems` |
| Amazon Elastic Inference |  |
| Amazon Elastic Map Reduce (EMR) | `elasticmapreduce:ListClusters` |
| Amazon Elasticsearch Service (ES) | `es:ListDomainNames` |
| Amazon Elastic Transcoder | `elastictranscoder:ListPipelines` |
| Amazon Elastic Load Balancer (ELB) (встроенный) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
| Amazon EventBridge | `events:ListEventBuses` |
| Amazon FSx | `fsx:DescribeFileSystems` |
| Amazon GameLift | `gamelift:ListFleets` |
| AWS Glue | `glue:GetJobs` |
| Amazon Inspector | `inspector:ListAssessmentTemplates` |
| AWS Internet of Things (IoT) |  |
| AWS IoT Analytics |  |
| Amazon Managed Streaming for Kafka | `kafka:ListClusters` |
| Amazon Kinesis Data Analytics | `kinesisanalytics:ListApplications` |
| Amazon Data Firehose | `firehose:ListDeliveryStreams` |
| Amazon Kinesis Data Streams | `kinesis:ListStreams` |
| Amazon Kinesis Video Streams | `kinesisvideo:ListStreams` |
| AWS Lambda | `lambda:ListFunctions` |
| AWS Lambda (встроенный) | `lambda:ListFunctions`, `lambda:ListTags` |
| Amazon Lex | `lex:GetBots` |
| Amazon Application and Network Load Balancer (встроенный) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
| Amazon CloudWatch Logs | `logs:DescribeLogGroups` |
| AWS Elemental MediaConnect | `mediaconnect:ListFlows` |
| AWS Elemental MediaConvert | `mediaconvert:DescribeEndpoints` |
| AWS Elemental MediaPackage Live | `mediapackage:ListChannels` |
| AWS Elemental MediaPackage Video on Demand | `mediapackage-vod:ListPackagingConfigurations` |
| AWS Elemental MediaTailor | `mediatailor:ListPlaybackConfigurations` |
| Amazon VPC NAT Gateways | `ec2:DescribeNatGateways` |
| Amazon Neptune | `rds:DescribeDBClusters` |
| AWS OpsWorks | `opsworks:DescribeStacks` |
| Amazon Polly |  |
| Amazon QLDB | `qldb:ListLedgers` |
| Amazon RDS | `rds:DescribeDBInstances` |
| Amazon RDS (встроенный) | `rds:DescribeDBInstances`, `rds:DescribeEvents`, `rds:ListTagsForResource` |
| Amazon Redshift | `redshift:DescribeClusters` |
| Amazon Rekognition |  |
| AWS RoboMaker | `robomaker:ListSimulationJobs` |
| Amazon Route 53 | `route53:ListHostedZones` |
| Amazon Route 53 Resolver | `route53resolver:ListResolverEndpoints` |
| Amazon S3 | `s3:ListAllMyBuckets` |
| Amazon S3 (встроенный) | `s3:ListAllMyBuckets` |
| Amazon SageMaker Batch Transform Jobs |  |
| Amazon SageMaker Endpoint Instances | `sagemaker:ListEndpoints` |
| Amazon SageMaker Endpoints | `sagemaker:ListEndpoints` |
| Amazon SageMaker Ground Truth |  |
| Amazon SageMaker Processing Jobs |  |
| Amazon SageMaker Training Jobs |  |
| AWS Service Catalog |  |
| Amazon Simple Email Service (SES) |  |
| Amazon Simple Notification Service (SNS) | `sns:ListTopics` |
| Amazon Simple Queue Service (SQS) | `sqs:ListQueues` |
| AWS Systems Manager - Run Command |  |
| AWS Step Functions |  |
| AWS Storage Gateway | `storagegateway:ListGateways` |
| Amazon SWF | `swf:ListDomains` |
| Amazon Textract |  |
| AWS IoT Things Graph |  |
| AWS Transfer Family | `transfer:ListServers` |
| AWS Transit Gateway | `ec2:DescribeTransitGateways` |
| Amazon Translate |  |
| AWS Trusted Advisor |  |
| AWS API Usage |  |
| AWS Site-to-Site VPN | `ec2:DescribeVpnConnections` |
| AWS WAF Classic |  |
| AWS WAF |  |
| Amazon WorkMail | `workmail:ListOrganizations` |
| Amazon WorkSpaces | `workspaces:DescribeWorkspaces` |

Пример JSON-политики для одного отдельного сервиса.

JSON-политика для Amazon API Gateway

```
{


"Version": "2012-10-17",


"Statement": [


{


"Sid": "VisualEditor0",


"Effect": "Allow",


"Action": [


"apigateway:GET",


"cloudwatch:GetMetricData",


"cloudwatch:GetMetricStatistics",


"cloudwatch:ListMetrics",


"sts:GetCallerIdentity",


"tag:GetResources",


"tag:GetTagKeys",


"ec2:DescribeAvailabilityZones"


],


"Resource": "*"


}


]


}
```

В этом примере из полного списка разрешений необходимо выбрать

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

## Установка OneAgent (необязательно)

Для установки и настройки OneAgent см. [Развёртывание OneAgent на AWS Elastic Beanstalk](../../integrate-into-aws/aws-beanstalk.md "Установка OneAgent на AWS Elastic Beanstalk.").

### Конечные точки AWS, которые должны быть доступны с ActiveGate, с соответствующими сервисами AWS

| Конечная точка | Сервис |
| --- | --- |
| `autoscaling.<REGION>.amazonaws.com` | Amazon EC2 Auto Scaling (встроенный), Amazon EC2 Auto Scaling |
| `lambda.<REGION>.amazonaws.com` | AWS Lambda (встроенный), AWS Lambda |
| `elasticloadbalancing.<REGION>.amazonaws.com` | Amazon Application and Network Load Balancer (встроенный), Amazon Elastic Load Balancer (ELB) (встроенный) |
| `dynamodb.<REGION>.amazonaws.com` | Amazon DynamoDB (встроенный), Amazon DynamoDB |
| `ec2.<REGION>.amazonaws.com` | Amazon EBS (встроенный), Amazon EC2 (встроенный), Amazon EBS, Amazon EC2 Spot Fleet, Amazon VPC NAT Gateways, AWS Transit Gateway, AWS Site-to-Site VPN |
| `rds.<REGION>.amazonaws.com` | Amazon RDS (встроенный), Amazon Aurora, Amazon DocumentDB, Amazon Neptune, Amazon RDS |
| `s3.<REGION>.amazonaws.com` | Amazon S3 (встроенный) |
| `acm-pca.<REGION>.amazonaws.com` | AWS Certificate Manager Private Certificate Authority |
| `apigateway.<REGION>.amazonaws.com` | Amazon API Gateway |
| `apprunner.<REGION>.amazonaws.com` | AWS App Runner |
| `appstream2.<REGION>.amazonaws.com` | Amazon AppStream |
| `appsync.<REGION>.amazonaws.com` | AWS AppSync |
| `athena.<REGION>.amazonaws.com` | Amazon Athena |
| `cloudfront.amazonaws.com` | Amazon CloudFront |
| `cloudhsmv2.<REGION>.amazonaws.com` | AWS CloudHSM |
| `cloudsearch.<REGION>.amazonaws.com` | Amazon CloudSearch |
| `codebuild.<REGION>.amazonaws.com` | AWS CodeBuild |
| `datasync.<REGION>.amazonaws.com` | AWS DataSync |
| `dax.<REGION>.amazonaws.com` | Amazon DynamoDB Accelerator (DAX) |
| `dms.<REGION>.amazonaws.com` | AWS Database Migration Service (AWS DMS) |
| `directconnect.<REGION>.amazonaws.com` | AWS Direct Connect |
| `ecs.<REGION>.amazonaws.com` | Amazon Elastic Container Service (ECS), Amazon ECS Container Insights |
| `elasticfilesystem.<REGION>.amazonaws.com` | Amazon Elastic File System (EFS) |
| `eks.<REGION>.amazonaws.com` | Amazon Elastic Kubernetes Service (EKS) |
| `elasticache.<REGION>.amazonaws.com` | Amazon ElastiCache (EC) |
| `elasticbeanstalk.<REGION>.amazonaws.com` | AWS Elastic Beanstalk |
| `elastictranscoder.<REGION>.amazonaws.com` | Amazon Elastic Transcoder |
| `es.<REGION>.amazonaws.com` | Amazon Elasticsearch Service (ES) |
| `events.<REGION>.amazonaws.com` | Amazon EventBridge |
| `fsx.<REGION>.amazonaws.com` | Amazon FSx |
| `gamelift.<REGION>.amazonaws.com` | Amazon GameLift |
| `glue.<REGION>.amazonaws.com` | AWS Glue |
| `inspector.<REGION>.amazonaws.com` | Amazon Inspector |
| `kafka.<REGION>.amazonaws.com` | Amazon Managed Streaming for Kafka |
| `models.lex.<REGION>.amazonaws.com` | Amazon Lex |
| `logs.<REGION>.amazonaws.com` | Amazon CloudWatch Logs |
| `api.mediatailor.<REGION>.amazonaws.com` | AWS Elemental MediaTailor |
| `mediaconnect.<REGION>.amazonaws.com` | AWS Elemental MediaConnect |
| `mediapackage.<REGION>.amazonaws.com` | AWS Elemental MediaPackage Live |
| `mediapackage-vod.<REGION>.amazonaws.com` | AWS Elemental MediaPackage Video on Demand |
| `opsworks.<REGION>.amazonaws.com` | AWS OpsWorks |
| `qldb.<REGION>.amazonaws.com` | Amazon QLDB |
| `redshift.<REGION>.amazonaws.com` | Amazon Redshift |
| `robomaker.<REGION>.amazonaws.com` | AWS RoboMaker |
| `route53.amazonaws.com` | Amazon Route 53 |
| `route53resolver.<REGION>.amazonaws.com` | Amazon Route 53 Resolver |
| `api.sagemaker.<REGION>.amazonaws.com` | Amazon SageMaker Endpoints, Amazon SageMaker Endpoint Instances |
| `sns.<REGION>.amazonaws.com` | Amazon Simple Notification Service (SNS) |
| `sqs.<REGION>.amazonaws.com` | Amazon Simple Queue Service (SQS) |
| `storagegateway.<REGION>.amazonaws.com` | AWS Storage Gateway |
| `swf.<REGION>.amazonaws.com` | Amazon SWF |
| `transfer.<REGION>.amazonaws.com` | AWS Transfer Family |
| `workmail.<REGION>.amazonaws.com` | Amazon WorkMail |
| `workspaces.<REGION>.amazonaws.com` | Amazon WorkSpaces |

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../aws-metrics-ingest/aws-enable-service-monitoring.md "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг предустановленный дашборд, содержащий все рекомендуемые метрики, автоматически появляется на вашей странице **Дашборды**. Для поиска конкретных дашбордов отфильтруйте по **Предустановленные**, а затем по **Название**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS, а затем нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.

Чтобы удалить дашборд со страницы дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Неприменимо |
| AWS Lambda (встроенный) | Неприменимо |
| Amazon Application and Network Load Balancer (встроенный) | Неприменимо |
| Amazon DynamoDB (встроенный) | Неприменимо |
| Amazon EBS (встроенный) | Неприменимо |
| Amazon EC2 (встроенный) | Неприменимо |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Неприменимо |
| Amazon RDS (встроенный) | Неприменимо |
| Amazon S3 (встроенный) | Неприменимо |
| AWS Certificate Manager Private Certificate Authority | Неприменимо |
| Все отслеживаемые сервисы Amazon | Неприменимо |
| Amazon API Gateway | Неприменимо |
| AWS App Runner | Неприменимо |
| Amazon AppStream | Применимо |
| AWS AppSync | Применимо |
| Amazon Athena | Применимо |
| Amazon Aurora | Неприменимо |
| Amazon EC2 Auto Scaling | Применимо |
| AWS Billing | Применимо |
| Amazon Keyspaces | Применимо |
| AWS Chatbot | Применимо |
| Amazon CloudFront | Неприменимо |
| AWS CloudHSM | Применимо |
| Amazon CloudSearch | Применимо |
| AWS CodeBuild | Применимо |
| Amazon Cognito | Неприменимо |
| Amazon Connect | Применимо |
| AWS DataSync | Применимо |
| Amazon DynamoDB Accelerator (DAX) | Применимо |
| AWS Database Migration Service (AWS DMS) | Применимо |
| Amazon DocumentDB | Применимо |
| AWS Direct Connect | Применимо |
| Amazon DynamoDB | Неприменимо |
| Amazon EBS | Неприменимо |
| Amazon EC2 Spot Fleet | Неприменимо |
| Amazon EC2 API | Применимо |
| Amazon Elastic Container Service (ECS) | Неприменимо |
| Amazon ECS Container Insights | Применимо |
| Amazon Elastic File System (EFS) | Неприменимо |
| Amazon Elastic Kubernetes Service (EKS) | Применимо |
| Amazon ElastiCache (EC) | Неприменимо |
| AWS Elastic Beanstalk | Применимо |
| Amazon Elastic Inference | Применимо |
| Amazon Elastic Transcoder | Применимо |
| Amazon Elastic Map Reduce (EMR) | Неприменимо |
| Amazon Elasticsearch Service (ES) | Неприменимо |
| Amazon EventBridge | Применимо |
| Amazon FSx | Применимо |
| Amazon GameLift | Применимо |
| AWS Glue | Неприменимо |
| Amazon Inspector | Применимо |
| AWS Internet of Things (IoT) | Неприменимо |
| AWS IoT Things Graph | Применимо |
| AWS IoT Analytics | Применимо |
| Amazon Managed Streaming for Kafka | Применимо |
| Amazon Kinesis Data Analytics | Неприменимо |
| Amazon Data Firehose | Неприменимо |
| Amazon Kinesis Data Streams | Неприменимо |
| Amazon Kinesis Video Streams | Неприменимо |
| AWS Lambda | Неприменимо |
| Amazon Lex | Применимо |
| Amazon CloudWatch Logs | Применимо |
| AWS Elemental MediaTailor | Применимо |
| AWS Elemental MediaConnect | Применимо |
| AWS Elemental MediaConvert | Применимо |
| AWS Elemental MediaPackage Live | Применимо |
| AWS Elemental MediaPackage Video on Demand | Применимо |
| Amazon MQ | Применимо |
| Amazon VPC NAT Gateways | Неприменимо |
| Amazon Neptune | Применимо |
| AWS OpsWorks | Применимо |
| Amazon Polly | Применимо |
| Amazon QLDB | Применимо |
| Amazon RDS | Неприменимо |
| Amazon Redshift | Неприменимо |
| Amazon Rekognition | Применимо |
| AWS RoboMaker | Применимо |
| Amazon Route 53 | Применимо |
| Amazon Route 53 Resolver | Применимо |
| Amazon S3 | Неприменимо |
| Amazon SageMaker Batch Transform Jobs | Неприменимо |
| Amazon SageMaker Endpoints | Неприменимо |
| Amazon SageMaker Endpoint Instances | Неприменимо |
| Amazon SageMaker Ground Truth | Неприменимо |
| Amazon SageMaker Processing Jobs | Неприменимо |
| Amazon SageMaker Training Jobs | Неприменимо |
| AWS Service Catalog | Применимо |
| Amazon Simple Email Service (SES) | Неприменимо |
| Amazon Simple Notification Service (SNS) | Неприменимо |
| Amazon Simple Queue Service (SQS) | Неприменимо |
| AWS Systems Manager - Run Command | Применимо |
| AWS Step Functions | Применимо |
| AWS Storage Gateway | Применимо |
| Amazon SWF | Применимо |
| Amazon Textract | Применимо |
| AWS Transfer Family | Применимо |
| AWS Transit Gateway | Применимо |
| Amazon Translate | Применимо |
| AWS Trusted Advisor | Применимо |
| AWS API Usage | Применимо |
| AWS Site-to-Site VPN | Применимо |
| AWS WAF Classic | Применимо |
| AWS WAF | Применимо |
| Amazon WorkMail | Применимо |
| Amazon WorkSpaces | Применимо |

![Elastic beanstalk](https://dt-cdn.net/images/dashboard-48-1016-8c1715cd7e.png)

## Доступные метрики

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ApplicationLatencyP10 | Среднее время в секундах для выполнения самых быстрых 10% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP10 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationLatencyP50 | Среднее время в секундах для выполнения самых быстрых 50% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP50 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationLatencyP75 | Среднее время в секундах для выполнения самых быстрых 75% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP75 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationLatencyP85 | Среднее время в секундах для выполнения самых быстрых 85% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP85 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationLatencyP90 | Среднее время в секундах для выполнения самых быстрых 90% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP90 |  | Seconds | Multi | EnvironmentName | Применимо |
| ApplicationLatencyP95 | Среднее время в секундах для выполнения самых быстрых 95% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP95 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationLatencyP99 | Среднее время в секундах для выполнения самых быстрых 99% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP99 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationLatencyP99.9 | Среднее время в секундах для выполнения самых быстрых 99.9% запросов (экземпляр и среда) | Seconds | Multi | EnvironmentName, InstanceId |  |
| ApplicationLatencyP99.9 |  | Seconds | Multi | EnvironmentName |  |
| ApplicationRequestsTotal | Общее количество запросов, выполненных экземпляром или средой | Count | Sum | EnvironmentName, InstanceId |  |
| ApplicationRequestsTotal |  | Count | Sum | EnvironmentName | Применимо |
| ApplicationRequests2xx | Количество запросов, завершённых с кодом состояния `2XX` (экземпляр и среда) | Count | Sum | EnvironmentName, InstanceId |  |
| ApplicationRequests2xx |  | Count | Sum | EnvironmentName |  |
| ApplicationRequests3xx | Количество запросов, завершённых с кодом состояния `3XX` (экземпляр и среда) | Count | Sum | EnvironmentName, InstanceId |  |
| ApplicationRequests3xx |  | Count | Sum | EnvironmentName |  |
| ApplicationRequests4xx | Количество запросов, завершённых с кодом состояния `4XX` (экземпляр и среда) | Count | Sum | EnvironmentName, InstanceId |  |
| ApplicationRequests4xx |  | Count | Sum | EnvironmentName | Применимо |
| ApplicationRequests5xx | Количество запросов, завершённых с кодом состояния `5XX` (экземпляр и среда) | Count | Sum | EnvironmentName, InstanceId |  |
| ApplicationRequests5xx |  | Count | Sum | EnvironmentName | Применимо |
| CPUIdle | Процент времени, в течение которого CPU находился в состоянии простоя за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUIowait | Процент времени, в течение которого CPU находился в состоянии `iowait` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUIrq | Процент времени, в течение которого CPU находился в состоянии `irq` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUNice | Процент времени, в течение которого CPU находился в состоянии `nice` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUPrivileged | Процент времени, в течение которого CPU находился в состоянии `privileged` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUSoftirq | Процент времени, в течение которого CPU находился в состоянии `softirq` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUSystem | Процент времени, в течение которого CPU находился в состоянии `system` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| CPUUser | Процент времени, в течение которого CPU находился в состоянии `user` за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| EnvironmentHealth | Текущее состояние работоспособности среды с семью возможными значениями: 0 - `OK`, 1 - `Info`, 5 - `Unknown`, 10 - `No data`, 15 - `Warning`, 20 - `Degraded` и 25 - `Severe` | None | Multi | EnvironmentName | Применимо |
| InstanceHealth | Текущее состояние работоспособности экземпляра с семью возможными значениями: 0 - `OK`, 1 - `Info`, 5 - `Unknown`, 10 - `No data`, 15 - `Warning`, 20 - `Degraded` и 25 - `Severe` | None | Multi | EnvironmentName, InstanceId | Применимо |
| InstancesDegraded | Количество экземпляров в среде со статусом работоспособности `degraded` (только среда) | Count | Multi | EnvironmentName |  |
| InstancesInfo | Количество экземпляров в среде со статусом работоспособности `info` (только среда) | Count | Multi | EnvironmentName |  |
| InstancesNoData | Количество экземпляров, для которых не получены данные (только среда) | Count | Multi | EnvironmentName |  |
| InstancesOk | Количество экземпляров в среде со статусом работоспособности `OK` (только среда) | Count | Multi | EnvironmentName |  |
| InstancesPending | Количество экземпляров в среде со статусом работоспособности `pending` (только среда) | Count | Multi | EnvironmentName |  |
| InstancesSevere | Количество экземпляров в среде со статусом работоспособности `severe` (только среда) | Count | Multi | EnvironmentName |  |
| InstancesUnknown | Количество экземпляров в среде со статусом работоспособности `unknown` (только среда) | Count | Multi | EnvironmentName |  |
| InstancesWarning | Количество экземпляров в среде со статусом работоспособности `warning` (только среда) | Count | Multi | EnvironmentName |  |
| LoadAverage1min | Средняя загрузка CPU экземпляра за последнюю минуту (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| LoadAverage5min | Средняя загрузка CPU экземпляра за последние пять минут (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| RootFilesystemUtil | Процент используемого дискового пространства (только экземпляр) | Percent | Multi | EnvironmentName, InstanceId |  |
| RootFilesystemUtil |  | Percent | Multi | EnvironmentName |  |
