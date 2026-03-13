---
title: Мониторинг Amazon MQ
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-mq
scraped: 2026-03-06T21:27:52.227083
---

# Мониторинг Amazon MQ

# Мониторинг Amazon MQ

* Классический
* Практическое руководство
* Чтение: 7 мин
* Опубликовано 8 сентября 2020 г.

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая Amazon MQ. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.

Для доступа на основе ролей в развёртывании [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Интеграция метрик из Amazon CloudWatch.") необходим [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.

* Dynatrace версии 1.201+
* Обновлённая [политика мониторинга AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.

Чтобы [обновить политику AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

Предопределённая JSON-политика для всех поддерживаемых сервисов

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

Если вы не хотите добавлять разрешения для всех сервисов, а только для определённых, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также, для каждого поддерживаемого сервиса, список необязательных разрешений, специфичных для этого сервиса.

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

Пример JSON-политики для одного сервиса.

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

### Эндпоинты AWS, которые должны быть доступны из ActiveGate, с соответствующими сервисами AWS

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

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. **Страница обзора группы пользовательских устройств** содержит список всех экземпляров (пользовательских устройств), принадлежащих группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг предустановленный дашборд, содержащий все рекомендуемые метрики, автоматически отображается на странице **Дашборды**. Для поиска определённых дашбордов отфильтруйте по **Предустановленные**, а затем по **Названию**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Дашборды**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню обзора (**...**) и выберите **Clone**.

Чтобы удалить дашборд со страницы дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню обзора (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Недоступен |
| AWS Lambda (встроенный) | Недоступен |
| Amazon Application and Network Load Balancer (встроенный) | Недоступен |
| Amazon DynamoDB (встроенный) | Недоступен |
| Amazon EBS (встроенный) | Недоступен |
| Amazon EC2 (встроенный) | Недоступен |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Недоступен |
| Amazon RDS (встроенный) | Недоступен |
| Amazon S3 (встроенный) | Недоступен |
| AWS Certificate Manager Private Certificate Authority | Недоступен |
| Все отслеживаемые сервисы Amazon | Недоступен |
| Amazon API Gateway | Недоступен |
| AWS App Runner | Недоступен |
| Amazon AppStream | Доступен |
| AWS AppSync | Доступен |
| Amazon Athena | Доступен |
| Amazon Aurora | Недоступен |
| Amazon EC2 Auto Scaling | Доступен |
| AWS Billing | Доступен |
| Amazon Keyspaces | Доступен |
| AWS Chatbot | Доступен |
| Amazon CloudFront | Недоступен |
| AWS CloudHSM | Доступен |
| Amazon CloudSearch | Доступен |
| AWS CodeBuild | Доступен |
| Amazon Cognito | Недоступен |
| Amazon Connect | Доступен |
| AWS DataSync | Доступен |
| Amazon DynamoDB Accelerator (DAX) | Доступен |
| AWS Database Migration Service (AWS DMS) | Доступен |
| Amazon DocumentDB | Доступен |
| AWS Direct Connect | Доступен |
| Amazon DynamoDB | Недоступен |
| Amazon EBS | Недоступен |
| Amazon EC2 Spot Fleet | Недоступен |
| Amazon EC2 API | Доступен |
| Amazon Elastic Container Service (ECS) | Недоступен |
| Amazon ECS Container Insights | Доступен |
| Amazon Elastic File System (EFS) | Недоступен |
| Amazon Elastic Kubernetes Service (EKS) | Доступен |
| Amazon ElastiCache (EC) | Недоступен |
| AWS Elastic Beanstalk | Доступен |
| Amazon Elastic Inference | Доступен |
| Amazon Elastic Transcoder | Доступен |
| Amazon Elastic Map Reduce (EMR) | Недоступен |
| Amazon Elasticsearch Service (ES) | Недоступен |
| Amazon EventBridge | Доступен |
| Amazon FSx | Доступен |
| Amazon GameLift | Доступен |
| AWS Glue | Недоступен |
| Amazon Inspector | Доступен |
| AWS Internet of Things (IoT) | Недоступен |
| AWS IoT Things Graph | Доступен |
| AWS IoT Analytics | Доступен |
| Amazon Managed Streaming for Kafka | Доступен |
| Amazon Kinesis Data Analytics | Недоступен |
| Amazon Data Firehose | Недоступен |
| Amazon Kinesis Data Streams | Недоступен |
| Amazon Kinesis Video Streams | Недоступен |
| AWS Lambda | Недоступен |
| Amazon Lex | Доступен |
| Amazon CloudWatch Logs | Доступен |
| AWS Elemental MediaTailor | Доступен |
| AWS Elemental MediaConnect | Доступен |
| AWS Elemental MediaConvert | Доступен |
| AWS Elemental MediaPackage Live | Доступен |
| AWS Elemental MediaPackage Video on Demand | Доступен |
| Amazon MQ | Доступен |
| Amazon VPC NAT Gateways | Недоступен |
| Amazon Neptune | Доступен |
| AWS OpsWorks | Доступен |
| Amazon Polly | Доступен |
| Amazon QLDB | Доступен |
| Amazon RDS | Недоступен |
| Amazon Redshift | Недоступен |
| Amazon Rekognition | Доступен |
| AWS RoboMaker | Доступен |
| Amazon Route 53 | Доступен |
| Amazon Route 53 Resolver | Доступен |
| Amazon S3 | Недоступен |
| Amazon SageMaker Batch Transform Jobs | Недоступен |
| Amazon SageMaker Endpoints | Недоступен |
| Amazon SageMaker Endpoint Instances | Недоступен |
| Amazon SageMaker Ground Truth | Недоступен |
| Amazon SageMaker Processing Jobs | Недоступен |
| Amazon SageMaker Training Jobs | Недоступен |
| AWS Service Catalog | Доступен |
| Amazon Simple Email Service (SES) | Недоступен |
| Amazon Simple Notification Service (SNS) | Недоступен |
| Amazon Simple Queue Service (SQS) | Недоступен |
| AWS Systems Manager - Run Command | Доступен |
| AWS Step Functions | Доступен |
| AWS Storage Gateway | Доступен |
| Amazon SWF | Доступен |
| Amazon Textract | Доступен |
| AWS Transfer Family | Доступен |
| AWS Transit Gateway | Доступен |
| Amazon Translate | Доступен |
| AWS Trusted Advisor | Доступен |
| AWS API Usage | Доступен |
| AWS Site-to-Site VPN | Доступен |
| AWS WAF Classic | Доступен |
| AWS WAF | Доступен |
| Amazon WorkMail | Доступен |
| Amazon WorkSpaces | Доступен |

![Mqdash](https://dt-cdn.net/images/2021-03-12-09-28-26-1780-f1e633b57d.png)

## Доступные метрики

`Broker` является основным измерением.

### ActiveMQ

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ConsumerCount | Количество потребителей, подписанных на назначение | Count | Average | Broker, Topic |  |
| ConsumerCount |  | Count | Average | Broker, Queue |  |
| CpuCreditBalance | Количество заработанных кредитов CPU, которые экземпляр накопил с момента запуска (включая стартовые кредиты) | Count | Average | Broker | Доступен |
| CpuUtilization | Процент выделенных вычислительных единиц Amazon EC2, используемых брокером в данный момент | Percent | Average | Broker | Доступен |
| CurrentConnectionsCount | Текущее количество активных подключений к текущему брокеру | Count | Average | Broker | Доступен |
| DequeueCount | Количество сообщений, подтверждённых потребителями, в минуту | Count | Average | Broker, NetworkConnector, RemoteBroker |  |
| DequeueCount |  | Count | Average | Broker, Topic |  |
| DequeueCount |  | Count | Average | Broker, Queue |  |
| DispatchCount | Количество сообщений, отправленных потребителям, в минуту | Count | Average | Broker, Topic |  |
| DispatchCount |  | Count | Average | Broker, Queue |  |
| EnqueueCount | Количество сообщений, отправленных в назначение, в минуту | Count | Average | Broker, NetworkConnector, RemoteBroker |  |
| EnqueueCount |  | Count | Average | Broker, Topic |  |
| EnqueueCount |  | Count | Average | Broker, Queue |  |
| EnqueueTime | Сквозная задержка от поступления сообщения на брокер до его доставки потребителю | Milliseconds | Multi | Broker, Topic |  |
| EnqueueTime |  | Milliseconds | Multi | Broker, Queue |  |
| EstablishedConnectionsCount | Общее количество активных и неактивных подключений, установленных на брокере | Count | Average | Broker |  |
| ExpiredCount | Количество сообщений, которые не удалось доставить из-за истечения срока действия, в минуту | Count | Average | Broker, Topic |  |
| ExpiredCount |  | Count | Average | Broker, Queue |  |
| HeapUsage | Процент лимита памяти JVM ActiveMQ, используемый брокером в данный момент | Percent | Average | Broker | Доступен |
| InFlightCount | Количество сообщений, отправленных потребителям, но ещё не подтверждённых | Count | Average | Broker, Topic |  |
| InFlightCount |  | Count | Average | Broker, Queue |  |
| InactiveDurableTopicSubscribersCount | Количество неактивных подписчиков долговечных топиков, максимум 2000 | Count | Average | Broker |  |
| JobSchedulerStorePercentUsage | Процент дискового пространства, используемого хранилищем планировщика задач | Percent | Average | Broker |  |
| JournalFilesForFastRecovery | Количество файлов журнала, которые будут воспроизведены после чистого завершения работы | Count | Average | Broker |  |
| JournalFilesForFullRecovery | Количество файлов журнала, которые будут воспроизведены после нечистого завершения работы | Count | Average | Broker |  |
| MemoryUsage | Процент лимита памяти, используемый назначением в данный момент. | Percent | Average | Broker, Topic |  |
| MemoryUsage |  | Percent | Average | Broker, Queue |  |
| NetworkIn | Объём входящего трафика для брокера | Bytes | Average | Broker |  |
| NetworkIn |  | Bytes | Sum | Broker | Доступен |
| NetworkOut | Объём исходящего трафика для брокера | Bytes | Average | Broker |  |
| NetworkOut |  | Bytes | Sum | Broker | Доступен |
| OpenTransactionCount | Общее количество выполняемых транзакций | Count | Average | Broker |  |
| ProducerCount | Количество производителей для назначения | Count | Average | Broker, Topic |  |
| ProducerCount |  | Count | Average | Broker, Queue |  |
| QueueSize | Количество сообщений в очереди. Эта метрика применяется только к очередям. | Count | Average | Broker, Queue |  |
| ReceiveCount | Количество сообщений, полученных от удалённого брокера для дуплексного сетевого коннектора | Count | Average | Broker, NetworkConnector, RemoteBroker |  |
| StorePercentUsage | Процент использования лимита хранилища. Если достигнет 100, брокер будет отклонять сообщения. | Percent | Average | Broker |  |
| TempPercentUsage | Процент доступного временного хранилища, используемого непостоянными сообщениями | Percent | Average | Broker |  |
| TotalConsumerCount | Количество потребителей сообщений, подписанных на назначения текущего брокера | Count | Average | Broker | Доступен |
| TotalDequeueCount | Общее количество сообщений, потреблённых клиентами | Count | Average | Broker |  |
| TotalEnqueueCount | Общее количество сообщений, отправленных на брокер | Count | Average | Broker |  |
| TotalMessageCount | Количество сообщений, хранящихся на брокере | Count | Average | Broker | Доступен |
| TotalProducerCount | Количество активных производителей сообщений на назначениях текущего брокера | Count | Average | Broker | Доступен |

### RabbitMQ

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| AckRate | Скорость подтверждения сообщений потребителями. | Count/Second | Multi | Broker | Доступен |
| ChannelCount | Общее количество каналов, установленных на брокере. | Count | Average | Broker |  |
| ConfirmRate | Скорость, с которой сервер RabbitMQ подтверждает опубликованные сообщения. | Count/Second | Multi | Broker | Доступен |
| ConnectionCount | Общее количество подключений, установленных на брокере. | Count | Average | Broker |  |
| ConsumerCount | Общее количество потребителей, подключённых к брокеру. | Count | Average | Broker, Queue, VirtualHost |  |
| ConsumerCount |  | Count | Average | Broker | Доступен |
| ExchangeCount | Общее количество обменников, настроенных на брокере. | Count | Average | Broker |  |
| MessageCount | Общее количество сообщений в очередях. | Count | Average | Broker, Queue, VirtualHost |  |
| MessageCount |  | Count | Average | Broker | Доступен |
| MessageReadyCount | Общее количество готовых сообщений в очередях. | Count | Average | Broker, Queue, VirtualHost |  |
| MessageReadyCount |  | Count | Average | Broker | Доступен |
| MessageUnacknowledgedCount | Общее количество неподтверждённых сообщений в очередях. | Count | Average | Broker, Queue, VirtualHost |  |
| MessageUnacknowledgedCount |  | Count | Average | Broker | Доступен |
| PublishRate | Скорость публикации сообщений на брокере. | Count/Second | Multi | Broker | Доступен |
| QueueCount | Общее количество очередей, настроенных на брокере. | Count | Average | Broker |  |
| RabbitMQDiskFreeLimit | Лимит дискового пространства для узла RabbitMQ. | Bytes | Multi | Broker, Node | Доступен |
| RabbitMQDiskFree |  | Bytes | Multi | Broker, Node | Доступен |
| RabbitMQFdUsed | Количество используемых файловых дескрипторов. | Count | Average | Broker, Node |  |
| RabbitMQMemLimit |  | Bytes | Multi | Broker, Node | Доступен |
| RabbitMQMemUsed |  | Bytes | Multi | Broker, Node | Доступен |
| SystemCpuUtilization | Процент выделенных вычислительных единиц Amazon EC2, используемых брокером в данный момент. | Percent | Multi | Broker, Node | Доступен |

## Ограничения

Сущности Dynatrace этого сервиса AWS не обогащаются свойством ARN.
