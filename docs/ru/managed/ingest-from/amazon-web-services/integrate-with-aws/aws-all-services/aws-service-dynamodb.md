---
title: Мониторинг Amazon DynamoDB Accelerator (DAX)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb
scraped: 2026-03-05T21:35:33.055327
---

# Мониторинг Amazon DynamoDB Accelerator (DAX)


* Classic
* Практическое руководство
* Чтение: 12 минут
* Опубликовано 6 июля 2020 г.

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая Amazon DynamoDB Accelerator (DAX). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга этого сервиса необходимо:

* Любая версия ActiveGate в развёртываниях Dynatrace SaaS и Managed.

  Для доступа на основе ролей (в развёртывании [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") или [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) необходим ActiveGate, установленный на хосте Amazon EC2.
* Обновлённая [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#aws-policy-and-authentication "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.
  Для [обновления политики AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех облачных сервисов.

Предопределённая JSON-политика для всех облачных сервисов

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

Если вы не хотите добавлять разрешения для всех сервисов и хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а для каждого облачного сервиса — список дополнительных разрешений, специфичных для него.

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

В этом примере из полного списка разрешений необходимо выбрать:

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.
* Для отключения мониторинга встроенных сервисов требуется Environment ActiveGate версии 1.245+ и Dynatrace версии 1.247+.

### Эндпоинты AWS, доступные из ActiveGate, с соответствующими сервисами AWS

| Эндпоинт | Сервис |
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

Чтобы узнать, как включить мониторинг сервиса, см. раздел [Включение мониторинга сервиса](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **страница обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

После добавления сервиса в мониторинг на странице **Панели мониторинга** автоматически появляется стандартная панель со всеми рекомендуемыми метриками. Для поиска определённых панелей используйте фильтры **Preset** (Стандартная) и **Name** (Название).

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы стандартная панель отобразилась на странице **Панели мониторинга**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вносить изменения непосредственно в стандартную панель нельзя, но её можно клонировать и редактировать. Для клонирования панели откройте меню (**...**) и выберите **Clone**.

Для удаления панели со страницы панелей мониторинга её можно скрыть. Для скрытия панели откройте меню (**...**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Для проверки доступности стандартных панелей для каждого сервиса AWS см. список ниже.

### Список доступности стандартных панелей

| Сервис AWS | Стандартная панель |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Недоступна |
| AWS Lambda (встроенный) | Недоступна |
| Amazon Application and Network Load Balancer (встроенный) | Недоступна |
| Amazon DynamoDB (встроенный) | Недоступна |
| Amazon EBS (встроенный) | Недоступна |
| Amazon EC2 (встроенный) | Недоступна |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Недоступна |
| Amazon RDS (встроенный) | Недоступна |
| Amazon S3 (встроенный) | Недоступна |
| AWS Certificate Manager Private Certificate Authority | Недоступна |
| Все отслеживаемые сервисы Amazon | Недоступна |
| Amazon API Gateway | Недоступна |
| AWS App Runner | Недоступна |
| Amazon AppStream | Доступна |
| AWS AppSync | Доступна |
| Amazon Athena | Доступна |
| Amazon Aurora | Недоступна |
| Amazon EC2 Auto Scaling | Доступна |
| AWS Billing | Доступна |
| Amazon Keyspaces | Доступна |
| AWS Chatbot | Доступна |
| Amazon CloudFront | Недоступна |
| AWS CloudHSM | Доступна |
| Amazon CloudSearch | Доступна |
| AWS CodeBuild | Доступна |
| Amazon Cognito | Недоступна |
| Amazon Connect | Доступна |
| AWS DataSync | Доступна |
| Amazon DynamoDB Accelerator (DAX) | Доступна |
| AWS Database Migration Service (AWS DMS) | Доступна |
| Amazon DocumentDB | Доступна |
| AWS Direct Connect | Доступна |
| Amazon DynamoDB | Недоступна |
| Amazon EBS | Недоступна |
| Amazon EC2 Spot Fleet | Недоступна |
| Amazon EC2 API | Доступна |
| Amazon Elastic Container Service (ECS) | Недоступна |
| Amazon ECS Container Insights | Доступна |
| Amazon Elastic File System (EFS) | Недоступна |
| Amazon Elastic Kubernetes Service (EKS) | Доступна |
| Amazon ElastiCache (EC) | Недоступна |
| AWS Elastic Beanstalk | Доступна |
| Amazon Elastic Inference | Доступна |
| Amazon Elastic Transcoder | Доступна |
| Amazon Elastic Map Reduce (EMR) | Недоступна |
| Amazon Elasticsearch Service (ES) | Недоступна |
| Amazon EventBridge | Доступна |
| Amazon FSx | Доступна |
| Amazon GameLift | Доступна |
| AWS Glue | Недоступна |
| Amazon Inspector | Доступна |
| AWS Internet of Things (IoT) | Недоступна |
| AWS IoT Things Graph | Доступна |
| AWS IoT Analytics | Доступна |
| Amazon Managed Streaming for Kafka | Доступна |
| Amazon Kinesis Data Analytics | Недоступна |
| Amazon Data Firehose | Недоступна |
| Amazon Kinesis Data Streams | Недоступна |
| Amazon Kinesis Video Streams | Недоступна |
| AWS Lambda | Недоступна |
| Amazon Lex | Доступна |
| Amazon CloudWatch Logs | Доступна |
| AWS Elemental MediaTailor | Доступна |
| AWS Elemental MediaConnect | Доступна |
| AWS Elemental MediaConvert | Доступна |
| AWS Elemental MediaPackage Live | Доступна |
| AWS Elemental MediaPackage Video on Demand | Доступна |
| Amazon MQ | Доступна |
| Amazon VPC NAT Gateways | Недоступна |
| Amazon Neptune | Доступна |
| AWS OpsWorks | Доступна |
| Amazon Polly | Доступна |
| Amazon QLDB | Доступна |
| Amazon RDS | Недоступна |
| Amazon Redshift | Недоступна |
| Amazon Rekognition | Доступна |
| AWS RoboMaker | Доступна |
| Amazon Route 53 | Доступна |
| Amazon Route 53 Resolver | Доступна |
| Amazon S3 | Недоступна |
| Amazon SageMaker Batch Transform Jobs | Недоступна |
| Amazon SageMaker Endpoints | Недоступна |
| Amazon SageMaker Endpoint Instances | Недоступна |
| Amazon SageMaker Ground Truth | Недоступна |
| Amazon SageMaker Processing Jobs | Недоступна |
| Amazon SageMaker Training Jobs | Недоступна |
| AWS Service Catalog | Доступна |
| Amazon Simple Email Service (SES) | Недоступна |
| Amazon Simple Notification Service (SNS) | Недоступна |
| Amazon Simple Queue Service (SQS) | Недоступна |
| AWS Systems Manager - Run Command | Доступна |
| AWS Step Functions | Доступна |
| AWS Storage Gateway | Доступна |
| Amazon SWF | Доступна |
| Amazon Textract | Доступна |
| AWS Transfer Family | Доступна |
| AWS Transit Gateway | Доступна |
| Amazon Translate | Доступна |
| AWS Trusted Advisor | Доступна |
| AWS API Usage | Доступна |
| AWS Site-to-Site VPN | Доступна |
| AWS WAF Classic | Доступна |
| AWS WAF | Доступна |
| Amazon WorkMail | Доступна |
| Amazon WorkSpaces | Доступна |

![Dynamodb](https://dt-cdn.net/images/dashboard-24-1986-616089414a.png)

## Доступные метрики

`ClusterId` — основное измерение.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| BatchGetItemRequestCount | Количество запросов BatchGetItem, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| BatchGetItemRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| BatchGetItemRequestCount |  | Количество | Sum | ClusterId | Доступна |
| BatchGetItemRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| BatchGetItemRequestCount |  | Количество | Multi | Region |  |
| BatchGetItemRequestCount |  | Количество | Sum | Region | Доступна |
| BatchWriteItemRequestCount | Количество запросов BatchWriteItem, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| BatchWriteItemRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| BatchWriteItemRequestCount |  | Количество | Sum | ClusterId | Доступна |
| BatchWriteItemRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| BatchWriteItemRequestCount |  | Количество | Multi | Region |  |
| BatchWriteItemRequestCount |  | Количество | Sum | Region | Доступна |
| CPUUtilization | Процент использования ЦП узлом или кластером | Процент | Multi | ClusterId | Доступна |
| CPUUtilization |  | Процент | Multi | ClusterId, NodeId | Доступна |
| CPUUtilization |  | Процент | Multi | Region | Доступна |
| ClientConnections | Количество одновременных соединений клиентов с узлом или кластером | Количество | Multi | ClusterId | Доступна |
| ClientConnections |  | Количество | Multi | ClusterId, NodeId | Доступна |
| ClientConnections |  | Количество | Sum | ClusterId | Доступна |
| ClientConnections |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ClientConnections |  | Количество | Multi | Region | Доступна |
| ClientConnections |  | Количество | Sum | Region | Доступна |
| DeleteItemRequestCount | Количество запросов DeleteItem, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| DeleteItemRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| DeleteItemRequestCount |  | Количество | Sum | ClusterId | Доступна |
| DeleteItemRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| DeleteItemRequestCount |  | Количество | Multi | Region |  |
| DeleteItemRequestCount |  | Количество | Sum | Region | Доступна |
| ErrorRequestCount | Общее количество запросов, завершившихся ошибкой пользователя, зафиксированной узлом или кластером. Включает запросы, ограниченные по скорости узлом или кластером. | Количество | Multi | ClusterId |  |
| ErrorRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| ErrorRequestCount |  | Количество | Sum | ClusterId | Доступна |
| ErrorRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ErrorRequestCount |  | Количество | Multi | Region |  |
| ErrorRequestCount |  | Количество | Sum | Region | Доступна |
| EstimatedDbSize | Приблизительный объём данных, кэшированных в кэше элементов и кэше запросов узлом или кластером | Байты | Multi | ClusterId | Доступна |
| EstimatedDbSize |  | Байты | Multi | ClusterId, NodeId | Доступна |
| EstimatedDbSize |  | Байты | Multi | Region | Доступна |
| EvictedSize | Объём данных, вытесненных узлом или кластером для освобождения места для новых запрошенных данных | Байты | Multi | ClusterId | Доступна |
| EvictedSize |  | Байты | Multi | ClusterId, NodeId | Доступна |
| EvictedSize |  | Байты | Sum | ClusterId | Доступна |
| EvictedSize |  | Байты | Sum | ClusterId, NodeId | Доступна |
| EvictedSize |  | Байты | Multi | Region | Доступна |
| EvictedSize |  | Байты | Sum | Region | Доступна |
| FailedRequestCount | Общее количество запросов, завершившихся ошибкой, зафиксированной узлом или кластером | Количество | Multi | ClusterId |  |
| FailedRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| FailedRequestCount |  | Количество | Sum | ClusterId | Доступна |
| FailedRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| FailedRequestCount |  | Количество | Multi | Region |  |
| FailedRequestCount |  | Количество | Sum | Region | Доступна |
| FaultRequestCount | Общее количество запросов, завершившихся внутренней ошибкой, зафиксированной узлом или кластером | Количество | Multi | ClusterId |  |
| FaultRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| FaultRequestCount |  | Количество | Sum | ClusterId | Доступна |
| FaultRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| FaultRequestCount |  | Количество | Multi | Region |  |
| FaultRequestCount |  | Количество | Sum | Region | Доступна |
| GetItemRequestCount | Количество запросов GetItem, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| GetItemRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| GetItemRequestCount |  | Количество | Sum | ClusterId | Доступна |
| GetItemRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| GetItemRequestCount |  | Количество | Multi | Region |  |
| GetItemRequestCount |  | Количество | Sum | Region | Доступна |
| ItemCacheHits | Количество случаев, когда элемент был возвращён из кэша узлом или кластером | Количество | Multi | ClusterId |  |
| ItemCacheHits |  | Количество | Multi | ClusterId, NodeId |  |
| ItemCacheHits |  | Количество | Sum | ClusterId | Доступна |
| ItemCacheHits |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ItemCacheHits |  | Количество | Multi | Region |  |
| ItemCacheHits |  | Количество | Sum | Region | Доступна |
| ItemCacheMisses | Количество случаев, когда элемент отсутствовал в кэше узла или кластера и должен был быть получен из DynamoDB | Количество | Multi | ClusterId |  |
| ItemCacheMisses |  | Количество | Multi | ClusterId, NodeId |  |
| ItemCacheMisses |  | Количество | Sum | ClusterId | Доступна |
| ItemCacheMisses |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ItemCacheMisses |  | Количество | Multi | Region |  |
| ItemCacheMisses |  | Количество | Sum | Region | Доступна |
| NetworkBytesIn | Количество байт, полученных через все сетевые интерфейсы узлом или кластером | Байты | Multi | ClusterId | Доступна |
| NetworkBytesIn |  | Байты | Multi | ClusterId, NodeId | Доступна |
| NetworkBytesIn |  | Байты | Multi | Region | Доступна |
| NetworkBytesOut | Количество байт, отправленных через все сетевые интерфейсы узлом или кластером. Эта метрика отражает объём исходящего трафика в байтах для одного узла или кластера. | Байты | Multi | ClusterId | Доступна |
| NetworkBytesOut |  | Байты | Multi | ClusterId, NodeId | Доступна |
| NetworkBytesOut |  | Байты | Multi | Region | Доступна |
| NetworkPacketsIn | Количество пакетов, полученных через все сетевые интерфейсы узлом или кластером | Количество | Multi | ClusterId | Доступна |
| NetworkPacketsIn |  | Количество | Multi | ClusterId, NodeId | Доступна |
| NetworkPacketsIn |  | Количество | Multi | Region | Доступна |
| NetworkPacketsOut | Количество пакетов, отправленных через все сетевые интерфейсы узлом или кластером. Эта метрика отражает объём исходящего трафика в пакетах для одного узла или кластера. | Количество | Multi | ClusterId | Доступна |
| NetworkPacketsOut |  | Количество | Multi | ClusterId, NodeId | Доступна |
| NetworkPacketsOut |  | Количество | Multi | Region | Доступна |
| PutItemRequestCount | Количество запросов PutItem, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| PutItemRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| PutItemRequestCount |  | Количество | Sum | ClusterId | Доступна |
| PutItemRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| PutItemRequestCount |  | Количество | Multi | Region |  |
| PutItemRequestCount |  | Количество | Sum | Region | Доступна |
| QueryCacheHits | Количество случаев, когда результат запроса был возвращён из кэша узла или кластера | Количество | Multi | ClusterId |  |
| QueryCacheHits |  | Количество | Multi | ClusterId, NodeId |  |
| QueryCacheHits |  | Количество | Sum | ClusterId | Доступна |
| QueryCacheHits |  | Количество | Sum | ClusterId, NodeId | Доступна |
| QueryCacheHits |  | Количество | Multi | Region |  |
| QueryCacheHits |  | Количество | Sum | Region | Доступна |
| QueryCacheMisses | Количество случаев, когда результат запроса отсутствовал в кэше узла или кластера и должен был быть получен из DynamoDB | Количество | Multi | ClusterId |  |
| QueryCacheMisses |  | Количество | Multi | ClusterId, NodeId |  |
| QueryCacheMisses |  | Количество | Sum | ClusterId | Доступна |
| QueryCacheMisses |  | Количество | Sum | ClusterId, NodeId | Доступна |
| QueryCacheMisses |  | Количество | Multi | Region |  |
| QueryCacheMisses |  | Количество | Sum | Region | Доступна |
| QueryRequestCount | Количество запросов на выборку, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| QueryRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| QueryRequestCount |  | Количество | Sum | ClusterId | Доступна |
| QueryRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| QueryRequestCount |  | Количество | Multi | Region |  |
| QueryRequestCount |  | Количество | Sum | Region | Доступна |
| ScanCacheHits | Количество случаев, когда результат сканирования был возвращён из кэша узла или кластера | Количество | Multi | ClusterId |  |
| ScanCacheHits |  | Количество | Multi | ClusterId, NodeId |  |
| ScanCacheHits |  | Количество | Sum | ClusterId | Доступна |
| ScanCacheHits |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ScanCacheHits |  | Количество | Multi | Region |  |
| ScanCacheHits |  | Количество | Sum | Region | Доступна |
| ScanCacheMisses | Количество случаев, когда результат сканирования отсутствовал в кэше узла или кластера и должен был быть получен из DynamoDB | Количество | Multi | ClusterId |  |
| ScanCacheMisses |  | Количество | Multi | ClusterId, NodeId |  |
| ScanCacheMisses |  | Количество | Sum | ClusterId | Доступна |
| ScanCacheMisses |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ScanCacheMisses |  | Количество | Multi | Region |  |
| ScanCacheMisses |  | Количество | Sum | Region | Доступна |
| ScanRequestCount | Количество запросов на сканирование, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| ScanRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| ScanRequestCount |  | Количество | Sum | ClusterId | Доступна |
| ScanRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ScanRequestCount |  | Количество | Multi | Region |  |
| ScanRequestCount |  | Количество | Sum | Region | Доступна |
| ThrottledRequestCount | Общее количество запросов, ограниченных по скорости узлом или кластером | Количество | Multi | ClusterId |  |
| ThrottledRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| ThrottledRequestCount |  | Количество | Sum | ClusterId | Доступна |
| ThrottledRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| ThrottledRequestCount |  | Количество | Multi | Region |  |
| ThrottledRequestCount |  | Количество | Sum | Region | Доступна |
| TotalRequestCount | Общее количество запросов, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| TotalRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| TotalRequestCount |  | Количество | Sum | ClusterId | Доступна |
| TotalRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| TotalRequestCount |  | Количество | Multi | Region |  |
| TotalRequestCount |  | Количество | Sum | Region | Доступна |
| TransactGetItemsCount | Количество запросов TransactGetItems, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| TransactGetItemsCount |  | Количество | Multi | ClusterId, NodeId |  |
| TransactGetItemsCount |  | Количество | Sum | ClusterId | Доступна |
| TransactGetItemsCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| TransactGetItemsCount |  | Количество | Multi | Region |  |
| TransactGetItemsCount |  | Количество | Sum | Region | Доступна |
| TransactWriteItemsCount | Количество запросов TransactWriteItems, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| TransactWriteItemsCount |  | Количество | Multi | ClusterId, NodeId |  |
| TransactWriteItemsCount |  | Количество | Sum | ClusterId | Доступна |
| TransactWriteItemsCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| TransactWriteItemsCount |  | Количество | Multi | Region |  |
| TransactWriteItemsCount |  | Количество | Sum | Region | Доступна |
| UpdateItemRequestCount | Количество запросов UpdateItem, обработанных узлом или кластером | Количество | Multi | ClusterId |  |
| UpdateItemRequestCount |  | Количество | Multi | ClusterId, NodeId |  |
| UpdateItemRequestCount |  | Количество | Sum | ClusterId | Доступна |
| UpdateItemRequestCount |  | Количество | Sum | ClusterId, NodeId | Доступна |
| UpdateItemRequestCount |  | Количество | Multi | Region |  |
| UpdateItemRequestCount |  | Количество | Sum | Region | Доступна |
