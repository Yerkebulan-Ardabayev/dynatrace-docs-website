---
title: Мониторинг Amazon RDS (Relational Database Service)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new
scraped: 2026-03-03T21:30:57.407028
---

* 31 мин. чтения

Для получения информации о различиях между классическими сервисами и другими сервисами см. раздел Миграция с классических AWS-сервисов (ранее «встроенных») на облачные сервисы.

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая Amazon RDS. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на панелях управления.

## Предварительные требования

Для включения мониторинга этого сервиса необходимо:

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace требуется Environment ActiveGate или Multi-environment ActiveGate.

  Для доступа на основе ролей в развёртывании [Dynatrace](../cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") необходим Environment ActiveGate, установленный на хосте Amazon EC2.

* Dynatrace версии 1.200+
* Обновлённая [политика мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных AWS-сервисов.

Для [обновления политики AWS IAM](https://dt-url.net/8q038eb) используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

Предустановленная политика JSON для всех поддерживаемых сервисов

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

Если вы не хотите добавлять разрешения для всех сервисов, а только для отдельных, воспользуйтесь таблицей ниже. В ней указан набор разрешений, необходимых для всех AWS-сервисов, а также список дополнительных разрешений для каждого поддерживаемого сервиса.

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

Пример политики JSON для одного отдельного сервиса.

Политика JSON для Amazon API Gateway

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
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех AWS-сервисов**.

### Конечные точки AWS, которые должны быть доступны из ActiveGate, и соответствующие AWS-сервисы

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

Сведения о включении мониторинга сервиса см. в разделе Включение мониторинга сервиса.

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Панели управления**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в раздел ![Технологии](https://dt-cdn.net/images/technologies-512-977161d83c.png "Технологии") **Технологии и процессы Classic**.
2. Отфильтруйте по названию сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр, чтобы перейти на **страницу обзора пользовательского устройства**.

### Просмотр метрик на панели управления

Метрики также можно просматривать на панелях управления в веб-интерфейсе Dynatrace. Для этого сервиса предустановленная панель недоступна, но вы можете создать собственную панель управления.

Для проверки наличия предустановленных панелей для каждого AWS-сервиса см. список ниже.

### Список доступности предустановленных панелей управления

| AWS-сервис | Предустановленная панель |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Не применимо |
| AWS Lambda (встроенный) | Не применимо |
| Amazon Application and Network Load Balancer (встроенный) | Не применимо |
| Amazon DynamoDB (встроенный) | Не применимо |
| Amazon EBS (встроенный) | Не применимо |
| Amazon EC2 (встроенный) | Не применимо |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Не применимо |
| Amazon RDS (встроенный) | Не применимо |
| Amazon S3 (встроенный) | Не применимо |
| AWS Certificate Manager Private Certificate Authority | Не применимо |
| Все отслеживаемые сервисы Amazon | Не применимо |
| Amazon API Gateway | Не применимо |
| AWS App Runner | Не применимо |
| Amazon AppStream | Применимо |
| AWS AppSync | Применимо |
| Amazon Athena | Применимо |
| Amazon Aurora | Не применимо |
| Amazon EC2 Auto Scaling | Применимо |
| AWS Billing | Применимо |
| Amazon Keyspaces | Применимо |
| AWS Chatbot | Применимо |
| Amazon CloudFront | Не применимо |
| AWS CloudHSM | Применимо |
| Amazon CloudSearch | Применимо |
| AWS CodeBuild | Применимо |
| Amazon Cognito | Не применимо |
| Amazon Connect | Применимо |
| AWS DataSync | Применимо |
| Amazon DynamoDB Accelerator (DAX) | Применимо |
| AWS Database Migration Service (AWS DMS) | Применимо |
| Amazon DocumentDB | Применимо |
| AWS Direct Connect | Применимо |
| Amazon DynamoDB | Не применимо |
| Amazon EBS | Не применимо |
| Amazon EC2 Spot Fleet | Не применимо |
| Amazon EC2 API | Применимо |
| Amazon Elastic Container Service (ECS) | Не применимо |
| Amazon ECS Container Insights | Применимо |
| Amazon Elastic File System (EFS) | Не применимо |
| Amazon Elastic Kubernetes Service (EKS) | Применимо |
| Amazon ElastiCache (EC) | Не применимо |
| AWS Elastic Beanstalk | Применимо |
| Amazon Elastic Inference | Применимо |
| Amazon Elastic Transcoder | Применимо |
| Amazon Elastic Map Reduce (EMR) | Не применимо |
| Amazon Elasticsearch Service (ES) | Не применимо |
| Amazon EventBridge | Применимо |
| Amazon FSx | Применимо |
| Amazon GameLift | Применимо |
| AWS Glue | Не применимо |
| Amazon Inspector | Применимо |
| AWS Internet of Things (IoT) | Не применимо |
| AWS IoT Things Graph | Применимо |
| AWS IoT Analytics | Применимо |
| Amazon Managed Streaming for Kafka | Применимо |
| Amazon Kinesis Data Analytics | Не применимо |
| Amazon Data Firehose | Не применимо |
| Amazon Kinesis Data Streams | Не применимо |
| Amazon Kinesis Video Streams | Не применимо |
| AWS Lambda | Не применимо |
| Amazon Lex | Применимо |
| Amazon CloudWatch Logs | Применимо |
| AWS Elemental MediaTailor | Применимо |
| AWS Elemental MediaConnect | Применимо |
| AWS Elemental MediaConvert | Применимо |
| AWS Elemental MediaPackage Live | Применимо |
| AWS Elemental MediaPackage Video on Demand | Применимо |
| Amazon MQ | Применимо |
| Amazon VPC NAT Gateways | Не применимо |
| Amazon Neptune | Применимо |
| AWS OpsWorks | Применимо |
| Amazon Polly | Применимо |
| Amazon QLDB | Применимо |
| Amazon RDS | Не применимо |
| Amazon Redshift | Не применимо |
| Amazon Rekognition | Применимо |
| AWS RoboMaker | Применимо |
| Amazon Route 53 | Применимо |
| Amazon Route 53 Resolver | Применимо |
| Amazon S3 | Не применимо |
| Amazon SageMaker Batch Transform Jobs | Не применимо |
| Amazon SageMaker Endpoints | Не применимо |
| Amazon SageMaker Endpoint Instances | Не применимо |
| Amazon SageMaker Ground Truth | Не применимо |
| Amazon SageMaker Processing Jobs | Не применимо |
| Amazon SageMaker Training Jobs | Не применимо |
| AWS Service Catalog | Применимо |
| Amazon Simple Email Service (SES) | Не применимо |
| Amazon Simple Notification Service (SNS) | Не применимо |
| Amazon Simple Queue Service (SQS) | Не применимо |
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

## Доступные метрики

Данный сервис отслеживает часть Amazon RDS (AWS/RDS). При активном использовании этого сервиса нельзя одновременно включить сервис Amazon RDS (встроенный).

`DBInstanceIdentifier` — основное измерение.

| Название | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DBClusterIdentifier, Role | Count |  |
| SumBinaryLogSize |  | Region, DatabaseClass | Count |  |
| SumBinaryLogSize |  | Region, DBClusterIdentifier | Count |  |
| SumBinaryLogSize |  | Region | Count |  |
| SumBinaryLogSize |  | Region, EngineName | Count |  |
| SumBinaryLogSize |  | Region, DBClusterIdentifier, Role | Count |  |
| DeleteThroughput |  | DBInstanceIdentifier | Count/Second |  |
| Deadlocks |  | Region, DatabaseClass | Count/Second |  |
| Deadlocks |  | Region, DBClusterIdentifier | Count/Second |  |
| Deadlocks |  | Region | Count/Second |  |
| Deadlocks |  | Region, EngineName | Count/Second |  |
| Deadlocks |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DBClusterIdentifier, Role | Count |  |
| TotalBackupStorageBilled |  | Region, DBClusterIdentifier | Bytes |  |
| TotalBackupStorageBilled |  | Region, EngineName | Bytes |  |
| DeleteLatency |  | Region, DatabaseClass | Milliseconds |  |
| DeleteLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| DeleteLatency |  | Region | Milliseconds |  |
| DeleteLatency |  | Region, EngineName | Milliseconds |  |
| DeleteLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | DBInstanceIdentifier | Count |  |
| DDLLatency |  | Region, DatabaseClass | Milliseconds |  |
| DDLLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| DDLLatency |  | Region | Milliseconds |  |
| DDLLatency |  | Region, EngineName | Milliseconds |  |
| DDLLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| DMLLatency |  | Region, DatabaseClass | Milliseconds |  |
| DMLLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| DMLLatency |  | Region | Milliseconds |  |
| DMLLatency |  | Region, EngineName | Milliseconds |  |
| DMLLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| DDLThroughput |  | Region, DatabaseClass | Count/Second |  |
| DDLThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| DDLThroughput |  | Region | Count/Second |  |
| DDLThroughput |  | Region, EngineName | Count/Second |  |
| DDLThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| CommitThroughput |  | Region, DatabaseClass | Count/Second |  |
| CommitThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| CommitThroughput |  | Region | Count/Second |  |
| CommitThroughput |  | Region, EngineName | Count/Second |  |
| CommitThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| ForwardingReplicaReadWaitLatency |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DBClusterIdentifier, Role | Count |  |
| BlockedTransactions |  | Region, DatabaseClass | Count/Second |  |
| BlockedTransactions |  | Region, DBClusterIdentifier | Count/Second |  |
| BlockedTransactions |  | Region | Count/Second |  |
| BlockedTransactions |  | Region, EngineName | Count/Second |  |
| BlockedTransactions |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| EBSIOBalance% | Процент оставшихся кредитов ввода-вывода в корзине пакетного режима базы данных RDS. Эта метрика доступна для базового уровня | Region, DatabaseClass | Percent |  |
| EBSIOBalance% |  | Region, DBClusterIdentifier | Percent |  |
| EBSIOBalance% |  | Region | Percent |  |
| EBSIOBalance% |  | Region, EngineName | Percent | Применимо |
| EBSIOBalance% |  | Region, DBClusterIdentifier, Role | Percent |  |
| SwapUsage | Объём используемого пространства подкачки на экземпляре БД. | Region, DatabaseClass | Bytes |  |
| SwapUsage |  | Region, DBClusterIdentifier | Bytes |  |
| SwapUsage |  | Region | Bytes |  |
| SwapUsage |  | Region, EngineName | Bytes |  |
| SwapUsage |  | Region, DBClusterIdentifier, Role | Bytes |  |
| ForwardingReplicaDMLThroughput |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_attempted |  | DBInstanceIdentifier | Count |  |
| LoginFailures |  | Region, DatabaseClass | Count/Second |  |
| LoginFailures |  | Region, DBClusterIdentifier | Count/Second |  |
| LoginFailures |  | Region | Count/Second |  |
| LoginFailures |  | Region, EngineName | Count/Second |  |
| LoginFailures |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| NetworkTransmitThroughput | Исходящий (передающий) сетевой трафик на экземпляре БД, включая клиентский трафик базы данных и трафик Amazon RDS | Region, DatabaseClass | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region, EngineName | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| NumBinaryLogFiles |  | Region, DatabaseClass | Count |  |
| NumBinaryLogFiles |  | Region, DBClusterIdentifier | Count |  |
| NumBinaryLogFiles |  | Region | Count |  |
| NumBinaryLogFiles |  | Region, EngineName | Count |  |
| NumBinaryLogFiles |  | Region, DBClusterIdentifier, Role | Count |  |
| DBLoadCPU |  | DBInstanceIdentifier | None |  |
| Aurora\_pq\_request\_failed |  | DBInstanceIdentifier | Count |  |
| BlockedTransactions |  | DBInstanceIdentifier | Count/Second |  |
| ForwardingReplicaReadWaitThroughput |  | DBInstanceIdentifier | Count |  |
| ReadThroughput | Среднее количество байт, считываемых с диска в секунду. | Region, DatabaseClass | Bytes/Second |  |
| ReadThroughput |  | Region | Bytes/Second |  |
| ReadThroughput |  | Region, EngineName | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DBClusterIdentifier, Role | Count |  |
| DeleteThroughput |  | Region, DatabaseClass | Count/Second |  |
| DeleteThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| DeleteThroughput |  | Region | Count/Second |  |
| DeleteThroughput |  | Region, EngineName | Count/Second |  |
| DeleteThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| DBLoadCPU |  | Region | None |  |
| CommitLatency |  | Region, DatabaseClass | Milliseconds |  |
| CommitLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| CommitLatency |  | Region | Milliseconds |  |
| CommitLatency |  | Region, EngineName | Milliseconds |  |
| CommitLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| ForwardingReplicaOpenSessions |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaOpenSessions |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaOpenSessions |  | Region | Count |  |
| ForwardingReplicaOpenSessions |  | Region, EngineName | Count |  |
| ForwardingReplicaOpenSessions |  | Region, DBClusterIdentifier, Role | Count |  |
| BackupRetentionPeriodStorageUsed |  | Region, DBClusterIdentifier | Bytes |  |
| BackupRetentionPeriodStorageUsed |  | Region, EngineName | Bytes |  |
| InsertLatency |  | Region, DatabaseClass | Milliseconds |  |
| InsertLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| InsertLatency |  | Region | Milliseconds |  |
| InsertLatency |  | Region, EngineName | Milliseconds |  |
| InsertLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| DMLThroughput |  | Region, DatabaseClass | Count/Second |  |
| DMLThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| DMLThroughput |  | Region | Count/Second |  |
| DMLThroughput |  | Region, EngineName | Count/Second |  |
| DMLThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| Aurora\_pq\_request\_attempted |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_attempted |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_attempted |  | Region | Count |  |
| Aurora\_pq\_request\_attempted |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_attempted |  | Region, DBClusterIdentifier, Role | Count |  |
| DiskQueueDepth | Количество незавершённых операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску. | Region, DatabaseClass | Count |  |
| DiskQueueDepth |  | Region | Count |  |
| DiskQueueDepth |  | Region, EngineName | Count | Применимо |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DBClusterIdentifier, Role | Count |  |
| BinLogDiskUsage | Объём дискового пространства, занятого двоичными журналами. Если для экземпляров MySQL и MariaDB включено автоматическое резервное копирование, | Region, DatabaseClass | Bytes |  |
| BinLogDiskUsage |  | Region | Bytes |  |
| BinLogDiskUsage |  | Region, EngineName | Bytes | Применимо |
| BinLogDiskUsage |  | Region, EngineName | Bytes |  |
| ForwardingWriterDMLThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingWriterDMLThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingWriterDMLThroughput |  | Region | Count |  |
| ForwardingWriterDMLThroughput |  | Region, EngineName | Count |  |
| ForwardingWriterDMLThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| Queries |  | DBInstanceIdentifier | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, DatabaseClass | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, DBClusterIdentifier | Count |  |
| AuroraSlowConnectionHandleCount |  | Region | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, EngineName | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DBClusterIdentifier, Role | Count |  |
| CommitThroughput |  | DBInstanceIdentifier | Count/Second |  |
| RollbackSegmentHistoryListLength |  | Region, DatabaseClass | Count |  |
| RollbackSegmentHistoryListLength |  | Region, DBClusterIdentifier | Count |  |
| RollbackSegmentHistoryListLength |  | Region | Count |  |
| RollbackSegmentHistoryListLength |  | Region, EngineName | Count |  |
| RollbackSegmentHistoryListLength |  | Region, DBClusterIdentifier, Role | Count |  |
| SelectLatency |  | Region, DatabaseClass | Milliseconds |  |
| SelectLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| SelectLatency |  | Region | Milliseconds |  |
| SelectLatency |  | Region, EngineName | Milliseconds |  |
| SelectLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| ForwardingReplicaDMLLatency |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaDMLLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaDMLLatency |  | Region | Count |  |
| ForwardingReplicaDMLLatency |  | Region, EngineName | Count |  |
| ForwardingReplicaDMLLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| StorageNetworkThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | DBInstanceIdentifier | Count |  |
| DatabaseConnections | Количество клиентских сетевых подключений к экземпляру базы данных. | Region, DatabaseClass | Count |  |
| DatabaseConnections |  | Region, DBClusterIdentifier | Count |  |
| DatabaseConnections |  | Region | Count |  |
| DatabaseConnections |  | Region, EngineName | Count | Применимо |
| DatabaseConnections |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DBClusterIdentifier, Role | Count |  |
| EngineUptime |  | Region, DatabaseClass | Seconds |  |
| EngineUptime |  | Region, DBClusterIdentifier | Seconds |  |
| EngineUptime |  | Region | Seconds |  |
| EngineUptime |  | Region, EngineName | Seconds |  |
| EngineUptime |  | Region, DBClusterIdentifier, Role | Seconds |  |
| FreeStorageSpace | Объём доступного пространства для хранения данных. | Region, DatabaseClass | Bytes |  |
| FreeStorageSpace |  | Region | Bytes |  |
| FreeStorageSpace |  | Region, EngineName | Bytes | Применимо |
| FreeStorageSpace |  | Region, EngineName | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraVolumeBytesLeftTotal |  | DBInstanceIdentifier | Count |  |
| AbortedClients |  | Region, DatabaseClass | Count |  |
| AbortedClients |  | Region, DBClusterIdentifier | Count |  |
| AbortedClients |  | Region | Count |  |
| AbortedClients |  | Region, EngineName | Count |  |
| AbortedClients |  | Region, DBClusterIdentifier, Role | Count |  |
| BufferCacheHitRatio |  | Region, DatabaseClass | Percent |  |
| BufferCacheHitRatio |  | Region, DBClusterIdentifier | Percent |  |
| BufferCacheHitRatio |  | Region | Percent |  |
| BufferCacheHitRatio |  | Region, EngineName | Percent |  |
| BufferCacheHitRatio |  | Region, DBClusterIdentifier, Role | Percent |  |
| FreeLocalStorage |  | DBInstanceIdentifier | Bytes |  |
| AuroraSlowHandshakeCount |  | Region, DatabaseClass | Count |  |
| AuroraSlowHandshakeCount |  | Region, DBClusterIdentifier | Count |  |
| AuroraSlowHandshakeCount |  | Region | Count |  |
| AuroraSlowHandshakeCount |  | Region, EngineName | Count |  |
| AuroraSlowHandshakeCount |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingWriterDMLLatency |  | DBInstanceIdentifier | Count |  |
| Queries |  | Region, DatabaseClass | Count/Second |  |
| Queries |  | Region, DBClusterIdentifier | Count/Second |  |
| Queries |  | Region | Count/Second |  |
| Queries |  | Region, EngineName | Count/Second |  |
| Queries |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| EBSByteBalance% | Процент оставшихся кредитов пропускной способности в корзине пакетного режима базы данных RDS. Эта метрика доступна | Region, DatabaseClass | Percent |  |
| EBSByteBalance% |  | Region, DBClusterIdentifier | Percent |  |
| EBSByteBalance% |  | Region | Percent |  |
| EBSByteBalance% |  | Region, EngineName | Percent | Применимо |
| EBSByteBalance% |  | Region, DBClusterIdentifier, Role | Percent |  |
| ActiveTransactions |  | Region, DatabaseClass | Count/Second |  |
| ActiveTransactions |  | Region, DBClusterIdentifier | Count/Second |  |
| ActiveTransactions |  | Region | Count/Second |  |
| ActiveTransactions |  | Region, EngineName | Count/Second |  |
| ActiveTransactions |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| InsertThroughput |  | Region, DatabaseClass | Count/Second |  |
| InsertThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| InsertThroughput |  | Region | Count/Second |  |
| InsertThroughput |  | Region, EngineName | Count/Second |  |
| InsertThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| ForwardingWriterOpenSessions |  | Region, DatabaseClass | Count |  |
| ForwardingWriterOpenSessions |  | Region, DBClusterIdentifier | Count |  |
| ForwardingWriterOpenSessions |  | Region | Count |  |
| ForwardingWriterOpenSessions |  | Region, EngineName | Count |  |
| ForwardingWriterOpenSessions |  | Region, DBClusterIdentifier, Role | Count |  |
| SwapUsage | Объём используемого пространства подкачки на экземпляре БД. | DBInstanceIdentifier | Bytes |  |
| VolumeReadIOPs |  | Region, DbClusterIdentifier, EngineName | Count |  |
| VolumeReadIOPs |  | Region, DBClusterIdentifier | Count |  |
| VolumeReadIOPs |  | Region, EngineName | Count |  |
| ForwardingWriterDMLThroughput |  | DBInstanceIdentifier | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, DatabaseClass | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, DBClusterIdentifier | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, EngineName | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DBClusterIdentifier, Role | Count |  |
| VolumeBytesUsed |  | Region, DbClusterIdentifier, EngineName | Bytes |  |
| VolumeBytesUsed |  | Region, DBClusterIdentifier | Bytes |  |
| VolumeBytesUsed |  | Region, EngineName | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | DBInstanceIdentifier | Count |  |
| UpdateLatency |  | Region, DatabaseClass | Milliseconds |  |
| UpdateLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| UpdateLatency |  | Region | Milliseconds |  |
| UpdateLatency |  | Region, EngineName | Milliseconds |  |
| UpdateLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| UpdateThroughput |  | Region, DatabaseClass | Count/Second |  |
| UpdateThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| UpdateThroughput |  | Region | Count/Second |  |
| UpdateThroughput |  | Region, EngineName | Count/Second |  |
| UpdateThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| CPUUtilization | Процент использования ЦП. | Region, DatabaseClass | Percent |  |
| CPUUtilization |  | Region, DBClusterIdentifier | Percent |  |
| CPUUtilization |  | Region | Percent |  |
| CPUUtilization |  | Region, EngineName | Percent | Применимо |
| CPUUtilization |  | Region, DBClusterIdentifier, Role | Percent |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaDMLThroughput |  | Region | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, EngineName | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| LVMWriteIOPS |  | Region, DatabaseClass | Count/Second |  |
| LVMWriteIOPS |  | Region | Count/Second |  |
| LVMWriteIOPS |  | Region, EngineName | Count/Second | Применимо |
| ForwardingReplicaSelectThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaSelectThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaSelectThroughput |  | Region | Count |  |
| ForwardingReplicaSelectThroughput |  | Region, EngineName | Count |  |
| ForwardingReplicaSelectThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_failed |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_failed |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_failed |  | Region | Count |  |
| Aurora\_pq\_request\_failed |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_failed |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DBClusterIdentifier, Role | Count |  |
| EngineUptime |  | DBInstanceIdentifier | Seconds |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DBClusterIdentifier, Role | Count |  |
| ConnectionAttempts | Количество попыток подключения к экземпляру, успешных и неудачных. | Region, DatabaseClass | Count |  |
| ConnectionAttempts |  | Region, DBClusterIdentifier | Count |  |
| ConnectionAttempts |  | Region | Count |  |
| ConnectionAttempts |  | Region, EngineName | Count |  |
| ConnectionAttempts |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingWriterOpenSessions |  | DBInstanceIdentifier | Count |  |
| NetworkThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| NetworkThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| NetworkThroughput |  | Region | Bytes/Second |  |
| NetworkThroughput |  | Region, EngineName | Bytes/Second |  |
| NetworkThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| RollbackSegmentHistoryListLength |  | DBInstanceIdentifier | Count |  |
| SnapshotStorageUsed |  | Region, DBClusterIdentifier | Bytes |  |
| SnapshotStorageUsed |  | Region, EngineName | Bytes |  |
| AuroraBinlogReplicaLag |  | Region, DatabaseClass | Seconds |  |
| AuroraBinlogReplicaLag |  | Region, DBClusterIdentifier | Seconds |  |
| AuroraBinlogReplicaLag |  | Region | Seconds |  |
| AuroraBinlogReplicaLag |  | Region, EngineName | Seconds |  |
| AuroraBinlogReplicaLag |  | Region, DBClusterIdentifier, Role | Seconds |  |
| ForwardingReplicaSelectLatency |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaSelectLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaSelectLatency |  | Region | Count |  |
| ForwardingReplicaSelectLatency |  | Region, EngineName | Count |  |
| ForwardingReplicaSelectLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| LVMReadIOPS |  | Region, DatabaseClass | Count/Second |  |
| LVMReadIOPS |  | Region | Count/Second |  |
| LVMReadIOPS |  | Region, EngineName | Count/Second | Применимо |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | DBInstanceIdentifier | Count |  |
| FreeLocalStorage |  | Region, DatabaseClass | Bytes |  |
| FreeLocalStorage |  | Region, DBClusterIdentifier | Bytes |  |
| FreeLocalStorage |  | Region | Bytes |  |
| FreeLocalStorage |  | Region, EngineName | Bytes |  |
| FreeLocalStorage |  | Region, DBClusterIdentifier, Role | Bytes |  |
| StorageNetworkReceiveThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region, EngineName | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| Aurora\_pq\_request\_executed |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_executed |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_executed |  | Region | Count |  |
| Aurora\_pq\_request\_executed |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_executed |  | Region, DBClusterIdentifier, Role | Count |  |
| ReadLatency | Среднее время выполнения операции дискового ввода-вывода. | Region, DatabaseClass | Seconds |  |
| ReadLatency |  | Region, DBClusterIdentifier | Seconds |  |
| ReadLatency |  | Region | Seconds |  |
| ReadLatency |  | Region, EngineName | Seconds |  |
| ReadLatency |  | Region, DBClusterIdentifier, Role | Seconds |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DBClusterIdentifier, Role | Count |  |
| FreeableMemory | Объём доступной оперативной памяти. | DBInstanceIdentifier | Bytes | Применимо |
| FreeableMemory |  | DBInstanceIdentifier | Bytes |  |
| FreeableMemory |  | DBInstanceIdentifier | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraSlowConnectionHandleCount |  | DBInstanceIdentifier | Count |  |
| StorageNetworkThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| StorageNetworkThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| StorageNetworkThroughput |  | Region | Bytes/Second |  |
| StorageNetworkThroughput |  | Region, EngineName | Bytes/Second |  |
| StorageNetworkThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| ActiveTransactions |  | DBInstanceIdentifier | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DBClusterIdentifier, Role | Count |  |
| LoginFailures |  | DBInstanceIdentifier | Count/Second |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region, EngineName | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| SelectLatency |  | DBInstanceIdentifier | Milliseconds |  |
| VolumeWriteIOPs |  | Region, DbClusterIdentifier, EngineName | Count |  |
| VolumeWriteIOPs |  | Region, DBClusterIdentifier | Count |  |
| VolumeWriteIOPs |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraBinlogReplicaLag |  | DBInstanceIdentifier | Seconds |  |
| RowLockTime |  | Region, DatabaseClass | Count |  |
| RowLockTime |  | Region, DBClusterIdentifier | Count |  |
| RowLockTime |  | Region | Count |  |
| RowLockTime |  | Region, EngineName | Count |  |
| RowLockTime |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingWriterDMLLatency |  | Region, DatabaseClass | Count |  |
| ForwardingWriterDMLLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingWriterDMLLatency |  | Region | Count |  |
| ForwardingWriterDMLLatency |  | Region, EngineName | Count |  |
| ForwardingWriterDMLLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DBClusterIdentifier, Role | Count |  |
| CommitLatency |  | DBInstanceIdentifier | Milliseconds |  |
| ForwardingReplicaSelectLatency |  | DBInstanceIdentifier | Count |  |
| ReadIOPS | Среднее количество операций дискового ввода-вывода при чтении в секунду. | Region, DatabaseClass | Count/Second |  |
| ReadIOPS |  | Region | Count/Second |  |
| ReadIOPS |  | Region, EngineName | Count/Second |  |
| StorageNetworkTransmitThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | DBInstanceIdentifier | Count |  |
| WriteLatency | Среднее время выполнения операции дискового ввода-вывода. | Region, DatabaseClass | Seconds |  |
| WriteLatency |  | Region, DBClusterIdentifier | Seconds |  |
| WriteLatency |  | Region | Seconds |  |
| WriteLatency |  | Region, EngineName | Seconds |  |
| WriteLatency |  | Region, DBClusterIdentifier, Role | Seconds |  |
| SelectThroughput |  | Region, DatabaseClass | Count/Second |  |
| SelectThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| SelectThroughput |  | Region | Count/Second |  |
| SelectThroughput |  | Region, EngineName | Count/Second |  |
| SelectThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen |  | DBInstanceIdentifier | Count |  |
| FreeableMemory | Объём доступной оперативной памяти. | Region, DatabaseClass | Bytes |  |
| FreeableMemory |  | Region, DBClusterIdentifier | Bytes |  |
| FreeableMemory |  | Region | Bytes |  |
| FreeableMemory |  | Region, EngineName | Bytes | Применимо |
| FreeableMemory |  | Region, DBClusterIdentifier, Role | Bytes |  |
| FreeableMemory |  | Region, EngineName | Bytes |  |
| ReadLatency | Среднее время выполнения операции дискового ввода-вывода. | DBInstanceIdentifier | Seconds | Применимо |
| DMLLatency |  | DBInstanceIdentifier | Milliseconds |  |
| NetworkReceiveThroughput | Входящий (принимающий) сетевой трафик на экземпляре БД, включая клиентский трафик базы данных и трафик Amazon RDS | DBInstanceIdentifier | Bytes/Second | Применимо |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | DBInstanceIdentifier | Count |  |
| UpdateLatency |  | DBInstanceIdentifier | Milliseconds |  |
| DBLoad |  | DBInstanceIdentifier | None |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | DBInstanceIdentifier | Count |  |
| BinLogDiskUsage | Объём дискового пространства, занятого двоичными журналами. Если для экземпляров MySQL и MariaDB включено автоматическое резервное копирование, | DBInstanceIdentifier | Bytes | Применимо |
| BinLogDiskUsage |  | DBInstanceIdentifier | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | DBInstanceIdentifier | Count |  |
| DDLLatency |  | DBInstanceIdentifier | Milliseconds |  |
| SumBinaryLogSize |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_in\_progress |  | DBInstanceIdentifier | Count |  |
| DatabaseConnections | Количество клиентских сетевых подключений к экземпляру базы данных. | DBInstanceIdentifier | Count | Применимо |
| CPUUtilization | Процент использования ЦП. | DBInstanceIdentifier | Percent | Применимо |
| ForwardingReplicaReadWaitLatency |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region, EngineName | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| AbortedClients |  | DBInstanceIdentifier | Count |  |
| ReadThroughput | Среднее количество байт, считываемых с диска в секунду. | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_throttled |  | Region | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, DatabaseClass | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, DBClusterIdentifier | Count |  |
| AuroraDMLRejectedWriterFull |  | Region | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, EngineName | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingReplicaDMLLatency |  | DBInstanceIdentifier | Count |  |
| WriteThroughput | Среднее количество байт, записываемых на диск в секунду. | DBInstanceIdentifier | Bytes/Second |  |
| DiskQueueDepth | Количество незавершённых операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску. | DBInstanceIdentifier | Count | Применимо |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | DBInstanceIdentifier | Count |  |
| ForwardingReplicaOpenSessions |  | DBInstanceIdentifier | Count |  |
| StorageNetworkTransmitThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region, EngineName | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | DBInstanceIdentifier | Count |  |
| RowLockTime |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | DBInstanceIdentifier | Count |  |
| NetworkReceiveThroughput | Входящий (принимающий) сетевой трафик на экземпляре БД, включая клиентский трафик базы данных и трафик Amazon RDS | Region, DatabaseClass | Bytes/Second |  |
| NetworkReceiveThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| NetworkReceiveThroughput |  | Region | Bytes/Second |  |
| NetworkReceiveThroughput |  | Region, EngineName | Bytes/Second | Применимо |
| NetworkReceiveThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | DBInstanceIdentifier | Count |  |
| DBLoadNonCPU |  | DBInstanceIdentifier | None |  |
| WriteIOPS | Среднее количество операций дискового ввода-вывода при записи в секунду. | Region, DatabaseClass | Count/Second |  |
| WriteIOPS |  | Region | Count/Second |  |
| WriteIOPS |  | Region, EngineName | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | DBInstanceIdentifier | Count |  |
| BurstBalance | Процент доступных кредитов ввода-вывода для корзины пакетного режима General Purpose SSD (gp2). | DBInstanceIdentifier | Percent | Применимо |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DBClusterIdentifier, Role | Count |  |
| DMLThroughput |  | DBInstanceIdentifier | Count/Second |  |
| WriteIOPS | Среднее количество операций дискового ввода-вывода при записи в секунду. | DBInstanceIdentifier | Count/Second |  |
| WriteThroughput | Среднее количество байт, записываемых на диск в секунду. | Region, DatabaseClass | Bytes/Second |  |
| WriteThroughput |  | Region | Bytes/Second |  |
| WriteThroughput |  | Region, EngineName | Bytes/Second |  |
| BufferCacheHitRatio |  | DBInstanceIdentifier | Percent |  |
| ConnectionAttempts | Количество попыток подключения к экземпляру, успешных и неудачных. | DBInstanceIdentifier | Count |  |
| NetworkTransmitThroughput | Исходящий (передающий) сетевой трафик на экземпляре БД, включая клиентский трафик базы данных и трафик Amazon RDS | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_executed |  | DBInstanceIdentifier | Count |  |
| UpdateThroughput |  | DBInstanceIdentifier | Count/Second |  |
| ForwardingReplicaSelectThroughput |  | DBInstanceIdentifier | Count |  |
| StorageNetworkReceiveThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| DeleteLatency |  | DBInstanceIdentifier | Milliseconds |  |
| DDLThroughput |  | DBInstanceIdentifier | Count/Second |  |
| ReadIOPS | Среднее количество операций дискового ввода-вывода при чтении в секунду. | DBInstanceIdentifier | Count/Second |  |
| EBSByteBalance% | Процент оставшихся кредитов пропускной способности в корзине пакетного режима базы данных RDS. Эта метрика доступна | DBInstanceIdentifier | Percent | Применимо |
| NetworkThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| DBLoad |  | Region | None |  |
| Deadlocks |  | DBInstanceIdentifier | Count/Second |  |
| AuroraSlowHandshakeCount |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_throttled |  | DBInstanceIdentifier | Count |  |
| LVMReadIOPS |  | DBInstanceIdentifier | Count/Second | Применимо |
| NumBinaryLogFiles |  | DBInstanceIdentifier | Count |  |
| EBSIOBalance% | Процент оставшихся кредитов ввода-вывода в корзине пакетного режима базы данных RDS. Эта метрика доступна для базового уровня | DBInstanceIdentifier | Percent | Применимо |
| BurstBalance | Процент доступных кредитов ввода-вывода для корзины пакетного режима General Purpose SSD (gp2). | Region, DatabaseClass | Percent |  |
| BurstBalance |  | Region | Percent |  |
| BurstBalance |  | Region, EngineName | Percent | Применимо |
| FreeStorageSpace | Объём доступного пространства для хранения данных. | DBInstanceIdentifier | Bytes | Применимо |
| FreeStorageSpace |  | DBInstanceIdentifier | Bytes |  |
| FreeStorageSpace |  | DBInstanceIdentifier | Bytes |  |
| DBLoadNonCPU |  | Region | None |  |
| AuroraDMLRejectedWriterFull |  | DBInstanceIdentifier | Count |  |
| InsertLatency |  | DBInstanceIdentifier | Milliseconds |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | DBInstanceIdentifier | Count |  |
| SelectThroughput |  | DBInstanceIdentifier | Count/Second |  |
| InsertThroughput |  | DBInstanceIdentifier | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | DBInstanceIdentifier | Count |  |
| WriteLatency | Среднее время выполнения операции дискового ввода-вывода. | DBInstanceIdentifier | Seconds | Применимо |
| LVMWriteIOPS |  | DBInstanceIdentifier | Count/Second | Применимо |
