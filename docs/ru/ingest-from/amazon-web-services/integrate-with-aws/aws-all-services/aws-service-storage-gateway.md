---
title: Мониторинг AWS Storage Gateway
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-storage-gateway
scraped: 2026-03-03T21:23:28.419697
---

# Мониторинг AWS Storage Gateway

# Мониторинг AWS Storage Gateway

* Практическое руководство
* 6 минут чтения
* Опубликовано 06 июля 2020 г.

Dynatrace получает метрики для нескольких предустановленных пространств имён, включая AWS Storage Gateway. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса необходимо

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.

  Для доступа на основе ролей в развёртывании [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Интеграция метрик из Amazon CloudWatch.") необходим [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.

* Dynatrace версии 1.200+
* Обновлённая [политика мониторинга AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.

Чтобы [обновить политику AWS IAM](https://dt-url.net/8q038eb), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса — список дополнительных разрешений, специфичных для этого сервиса.

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
| Все отслеживаемые сервисы Amazon Обязательно | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
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

В этом примере из полного списка разрешений необходимо выбрать

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

### Конечные точки AWS, которые должны быть доступны из ActiveGate, с соответствующими сервисами AWS

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

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в раздел ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Технологии и процессы Classic**.
2. Отфильтруйте по имени сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы перейдёте на **страницу обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр, чтобы перейти на **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг предустановленный дашборд, содержащий все рекомендуемые метрики, автоматически появится на странице **Дашборды**. Для поиска конкретных дашбордов используйте фильтр по **Preset**, затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете его клонировать и редактировать. Чтобы клонировать дашборд, откройте контекстное меню (**…**) и выберите **Clone**.

Чтобы убрать дашборд со страницы дашбордов, его можно скрыть. Чтобы скрыть дашборд, откройте контекстное меню (**…**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Не применяется |
| AWS Lambda (встроенный) | Не применяется |
| Amazon Application and Network Load Balancer (встроенный) | Не применяется |
| Amazon DynamoDB (встроенный) | Не применяется |
| Amazon EBS (встроенный) | Не применяется |
| Amazon EC2 (встроенный) | Не применяется |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Не применяется |
| Amazon RDS (встроенный) | Не применяется |
| Amazon S3 (встроенный) | Не применяется |
| AWS Certificate Manager Private Certificate Authority | Не применяется |
| Все отслеживаемые сервисы Amazon | Не применяется |
| Amazon API Gateway | Не применяется |
| AWS App Runner | Не применяется |
| Amazon AppStream | Применяется |
| AWS AppSync | Применяется |
| Amazon Athena | Применяется |
| Amazon Aurora | Не применяется |
| Amazon EC2 Auto Scaling | Применяется |
| AWS Billing | Применяется |
| Amazon Keyspaces | Применяется |
| AWS Chatbot | Применяется |
| Amazon CloudFront | Не применяется |
| AWS CloudHSM | Применяется |
| Amazon CloudSearch | Применяется |
| AWS CodeBuild | Применяется |
| Amazon Cognito | Не применяется |
| Amazon Connect | Применяется |
| AWS DataSync | Применяется |
| Amazon DynamoDB Accelerator (DAX) | Применяется |
| AWS Database Migration Service (AWS DMS) | Применяется |
| Amazon DocumentDB | Применяется |
| AWS Direct Connect | Применяется |
| Amazon DynamoDB | Не применяется |
| Amazon EBS | Не применяется |
| Amazon EC2 Spot Fleet | Не применяется |
| Amazon EC2 API | Применяется |
| Amazon Elastic Container Service (ECS) | Не применяется |
| Amazon ECS Container Insights | Применяется |
| Amazon Elastic File System (EFS) | Не применяется |
| Amazon Elastic Kubernetes Service (EKS) | Применяется |
| Amazon ElastiCache (EC) | Не применяется |
| AWS Elastic Beanstalk | Применяется |
| Amazon Elastic Inference | Применяется |
| Amazon Elastic Transcoder | Применяется |
| Amazon Elastic Map Reduce (EMR) | Не применяется |
| Amazon Elasticsearch Service (ES) | Не применяется |
| Amazon EventBridge | Применяется |
| Amazon FSx | Применяется |
| Amazon GameLift | Применяется |
| AWS Glue | Не применяется |
| Amazon Inspector | Применяется |
| AWS Internet of Things (IoT) | Не применяется |
| AWS IoT Things Graph | Применяется |
| AWS IoT Analytics | Применяется |
| Amazon Managed Streaming for Kafka | Применяется |
| Amazon Kinesis Data Analytics | Не применяется |
| Amazon Data Firehose | Не применяется |
| Amazon Kinesis Data Streams | Не применяется |
| Amazon Kinesis Video Streams | Не применяется |
| AWS Lambda | Не применяется |
| Amazon Lex | Применяется |
| Amazon CloudWatch Logs | Применяется |
| AWS Elemental MediaTailor | Применяется |
| AWS Elemental MediaConnect | Применяется |
| AWS Elemental MediaConvert | Применяется |
| AWS Elemental MediaPackage Live | Применяется |
| AWS Elemental MediaPackage Video on Demand | Применяется |
| Amazon MQ | Применяется |
| Amazon VPC NAT Gateways | Не применяется |
| Amazon Neptune | Применяется |
| AWS OpsWorks | Применяется |
| Amazon Polly | Применяется |
| Amazon QLDB | Применяется |
| Amazon RDS | Не применяется |
| Amazon Redshift | Не применяется |
| Amazon Rekognition | Применяется |
| AWS RoboMaker | Применяется |
| Amazon Route 53 | Применяется |
| Amazon Route 53 Resolver | Применяется |
| Amazon S3 | Не применяется |
| Amazon SageMaker Batch Transform Jobs | Не применяется |
| Amazon SageMaker Endpoints | Не применяется |
| Amazon SageMaker Endpoint Instances | Не применяется |
| Amazon SageMaker Ground Truth | Не применяется |
| Amazon SageMaker Processing Jobs | Не применяется |
| Amazon SageMaker Training Jobs | Не применяется |
| AWS Service Catalog | Применяется |
| Amazon Simple Email Service (SES) | Не применяется |
| Amazon Simple Notification Service (SNS) | Не применяется |
| Amazon Simple Queue Service (SQS) | Не применяется |
| AWS Systems Manager - Run Command | Применяется |
| AWS Step Functions | Применяется |
| AWS Storage Gateway | Применяется |
| Amazon SWF | Применяется |
| Amazon Textract | Применяется |
| AWS Transfer Family | Применяется |
| AWS Transit Gateway | Применяется |
| Amazon Translate | Применяется |
| AWS Trusted Advisor | Применяется |
| AWS API Usage | Применяется |
| AWS Site-to-Site VPN | Применяется |
| AWS WAF Classic | Применяется |
| AWS WAF | Применяется |
| Amazon WorkMail | Применяется |
| Amazon WorkSpaces | Применяется |

![Gateway](https://dt-cdn.net/images/dashboard-30-2545-bf9ff63be4.png)

## Доступные метрики

`GatewayName` — основное измерение.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| CacheFree | Общее количество байт, доступных в кэш-хранилище шлюза | Bytes | Sum | GatewayName, GatewayId | Применяется |
| CacheHitPercent | Процент операций чтения приложений, обслуженных из кэша | Percent | Multi | Region, ShareId | Применяется |
| CacheHitPercent |  | Percent | Multi | Region, VolumeId | Применяется |
| CacheHitPercent |  | Percent | Multi | GatewayName, GatewayId | Применяется |
| CachePercentDirty | Процент кэша, помеченного как «грязный», то есть содержащего содержимое, которое ещё не было загружено в AWS | Percent | Multi | Region, ShareId | Применяется |
| CachePercentDirty |  | Percent | Multi | Region, VolumeId | Применяется |
| CachePercentDirty |  | Percent | Multi | GatewayName, GatewayId | Применяется |
| CachePercentUsed | Процент используемого кэш-хранилища шлюза | Percent | Multi | Region, ShareId | Применяется |
| CachePercentUsed |  | Percent | Multi | Region, VolumeId | Применяется |
| CachePercentUsed |  | Percent | Multi | GatewayName, GatewayId | Применяется |
| CacheUsed | Общее количество байт, используемых в кэш-хранилище шлюза | Bytes | Sum | GatewayName, GatewayId | Применяется |
| CloudBytesDownloaded | Общее количество байт, отправленных шлюзом в облако за отчётный период. Эта метрика включает активность всех томов на шлюзе. | Bytes | Sum | Region, ShareId | Применяется |
| CloudBytesDownloaded |  | Bytes | Count | Region, ShareId |  |
| CloudBytesDownloaded |  | Bytes | Sum | GatewayName, GatewayId | Применяется |
| CloudBytesDownloaded |  | Bytes | Count | GatewayName, GatewayId |  |
| CloudBytesUploaded | Общее количество байт, отправленных шлюзом в облако за отчётный период | Bytes | Sum | Region, ShareId | Применяется |
| CloudBytesUploaded |  | Bytes | Count | Region, ShareId |  |
| CloudBytesUploaded |  | Bytes | Sum | GatewayName, GatewayId |  |
| CloudBytesUploaded |  | Bytes | Count | GatewayName, GatewayId |  |
| CloudDownloadLatency | Задержка при загрузке данных из облака на шлюз | Milliseconds | Multi | GatewayName, GatewayId |  |
| IndexFetches | Количество файлов, для которых были получены метаданные | Count | Sum | Region, ShareId | Применяется |
| IndexFetches |  | Count | Sum | GatewayName, GatewayId | Применяется |
| IoWaitPercent | Процент времени ожидания шлюзом ответа от локального диска | Percent | Multi | GatewayName | Применяется |
| MemTotalBytes | Объём оперативной памяти, выделенной для виртуальной машины шлюза, в байтах | Bytes | Sum | GatewayName | Применяется |
| MemUsedBytes | Объём оперативной памяти, используемой виртуальной машиной шлюза в данный момент, в байтах | Bytes | Sum | GatewayName | Применяется |
| NfsSessions | Количество активных сессий NFS на шлюзе | Count | Sum | GatewayName | Применяется |
| QueuedWrites | Количество байт, ожидающих записи в AWS, измеренных в конце отчётного периода для всех томов шлюза | Bytes | Sum | Region, VolumeId | Применяется |
| QueuedWrites |  | Bytes | Sum | GatewayName, GatewayId | Применяется |
| ReadBytes | Общее количество байт, считанных из локальных приложений за отчётный период для всех томов шлюза | Bytes | Sum | Region, VolumeId | Применяется |
| ReadBytes |  | Bytes | Count | Region, VolumeId |  |
| ReadBytes |  | Bytes | Sum | GatewayName, GatewayId | Применяется |
| ReadBytes |  | Bytes | Count | GatewayName, GatewayId |  |
| ReadTime | Общее количество миллисекунд, затраченных на операции чтения из локальных приложений за отчётный период для всех томов шлюза | Milliseconds | Multi | Region, VolumeId | Применяется |
| ReadTime |  | Milliseconds | Multi | GatewayNam, GatewayIde | Применяется |
| SmbV1Sessions | Количество активных сессий Server Message Block (SMB) версии 1 на шлюзе | Count | Sum | GatewayName |  |
| SmbV2Sessions | Количество активных сессий SMB версии 2 на шлюзе | Count | Sum | GatewayName |  |
| SmbV3Sessions | Количество активных сессий SMB версии 3 на шлюзе | Count | Sum | GatewayName |  |
| TimeSinceLastRecoveryPoint | Время с момента последней доступной точки восстановления | Seconds | Multi | Region, VolumeId | Применяется |
| TimeSinceLastRecoveryPoint |  | Seconds | Multi | GatewayName, GatewayId |  |
| TotalCacheSize | Общий размер кэша в байтах | Bytes | Sum | GatewayName, GatewayId | Применяется |
| UploadBufferFree |  | Bytes | Sum | GatewayName, GatewayId | Применяется |
| UploadBufferPercentUsed | Процент использования буфера загрузки шлюза | Percent | Multi | GatewayName, GatewayId | Применяется |
| UploadBufferUsed | Общее количество байт, используемых в буфере загрузки шлюза | Bytes | Sum | GatewayName, GatewayId | Применяется |
| UserCpuPercent | Процент времени ЦП, затраченного на обработку данных шлюзом, усреднённый по всем ядрам | Percent | Multi | GatewayName |  |
| WorkingStorageFree | Общий объём свободного пространства в рабочем хранилище шлюза | Bytes | Sum | GatewayName, GatewayId | Применяется |
| WorkingStoragePercentUsed | Процент использования буфера загрузки шлюза | Percent | Multi | GatewayName, GatewayId | Применяется |
| WorkingStorageUsed | Общее количество байт, используемых в буфере загрузки шлюза | Bytes | Sum | GatewayName, GatewayId | Применяется |
| WriteBytes | Общее количество байт, записанных в локальные приложения за отчётный период для всех томов шлюза | Bytes | Sum | Region, VolumeId | Применяется |
| WriteBytes |  | Bytes | Count | Region, VolumeId |  |
| WriteBytes |  | Bytes | Sum | GatewayName, GatewayId | Применяется |
| WriteBytes |  | Bytes | Count | GatewayName, GatewayId |  |
| WriteTime | Общее количество миллисекунд, затраченных на операции записи в локальные приложения за отчётный период для всех томов шлюза | Milliseconds | Multi | Region, VolumeId | Применяется |
| WriteTime |  | Milliseconds | Multi | GatewayName, GatewayId | Применяется |
