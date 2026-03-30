---
title: Мониторинг AWS Elemental MediaConnect
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconnect
scraped: 2026-03-03T21:29:24.014231
---

Dynatrace получает метрики для множества предварительно выбранных пространств имён, включая AWS Elemental MediaConnect. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо:

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace требуется Environment ActiveGate или Multi-environment ActiveGate.

  Для доступа на основе ролей в развёртывании [Dynatrace](../cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") требуется Environment ActiveGate, установленный на хосте Amazon EC2.

* Dynatrace версии 1.200+
* Обновлённая [политика мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.

Чтобы [обновить политику AWS IAM](https://dt-url.net/8q038eb), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для всех облачных сервисов AWS, а также для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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

Пример политики JSON для одного сервиса.

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

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг предустановленный дашборд, содержащий все рекомендованные метрики, автоматически отображается на странице **Дашборды**. Для поиска конкретных дашбордов используйте фильтр по **Предустановленные**, а затем по **Имени**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Дашборды**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.

Чтобы удалить дашборд со страницы дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

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

![Mediaconnect](https://dt-cdn.net/images/mediaconnect-dashboard-1857-cb8f145abd.png)

## Доступные метрики

`FlowARN` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендовано |
| --- | --- | --- | --- | --- | --- |
| ARQRecovered | Количество потерянных пакетов, восстановленных с помощью автоматического запроса повторной передачи (ARQ) | Count | Sum | FlowARN | Доступен |
| ARQRecovered |  | Count | Sum | Region |  |
| ARQRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| ARQRequests | Количество повторно переданных пакетов, запрошенных через автоматический запрос повторной передачи (ARQ) и полученных | Count | Sum | Region |  |
| ARQRequests |  | Count | Sum | Region, AvailabilityZone |  |
| ARQRequests |  | Count | Sum | FlowARN | Доступен |
| BitRate |  | Bits/Second | Multi | Region |  |
| BitRate |  | Bits/Second | Multi | Region, AvailabilityZone |  |
| BitRate |  | Bits/Second | Multi | FlowARN | Доступен |
| CATError | Количество возникновений ошибки таблицы условного доступа (CAT). Эта ошибка указывает на отсутствие CAT. | Count | Sum | FlowARN |  |
| CATError |  | Count | Sum | Region |  |
| CATError |  | Count | Sum | Region, AvailabilityZone |  |
| CRCError |  | Count | Sum | FlowARN |  |
| CRCError |  | Count | Sum | Region |  |
| CRCError |  | Count | Sum | Region, AvailabilityZone |  |
| Connected | Статус источника. Значение 1 указывает, что источник подключён, а значение 0 указывает, что источник отключён. | None | Multi | FlowARN |  |
| Connected |  | None | Sum | FlowARN |  |
| Connected |  | None | Multi | Region |  |
| Connected |  | None | Multi | Region, AvailabilityZone |  |
| Connected |  | None | Sum | Region |  |
| Connected |  | None | Sum | Region, AvailabilityZone |  |
| Connected |  | None | Count | Region |  |
| Connected |  | None | Count | Region, AvailabilityZone |  |
| ConnectedOutputs |  | Count | Sum | Region |  |
| ConnectedOutputs |  | Count | Sum | Region, AvailabilityZone |  |
| ConnectedOutputs |  | Count | Sum | FlowARN |  |
| ContinuityCounter | Количество возникновений ошибки непрерывности | Count | Sum | FlowARN |  |
| ContinuityCounter |  | Count | Sum | Region |  |
| ContinuityCounter |  | Count | Sum | Region, AvailabilityZone |  |
| Disconnections | Количество раз, когда статус источника изменился с подключённого на отключённый | Count | Sum | Region |  |
| Disconnections |  | Count | Sum | Region, AvailabilityZone |  |
| Disconnections |  | Count | Sum | FlowARN |  |
| DroppedPackets | Количество пакетов, потерянных при передаче | Count | Sum | Region |  |
| DroppedPackets |  | Count | Sum | Region, AvailabilityZone |  |
| DroppedPackets |  | Count | Sum | FlowARN | Доступен |
| FECPackets | Количество пакетов, переданных с использованием прямого исправления ошибок (FEC) и полученных | Count | Sum | FlowARN | Доступен |
| FECPackets |  | Count | Sum | Region |  |
| FECPackets |  | Count | Sum | Region, AvailabilityZone |  |
| FECRecovered | Количество пакетов, переданных с использованием прямого исправления ошибок (FEC), потерянных при передаче и восстановленных | Count | Sum | FlowARN | Доступен |
| FECRecovered |  | Count | Sum | Region |  |
| FECRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| NotRecoveredPackets | Количество пакетов, потерянных при передаче и не восстановленных с помощью коррекции ошибок | Count | Sum | FlowARN | Доступен |
| NotRecoveredPackets |  | Count | Sum | Region |  |
| NotRecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| OutputConnected |  | None | Multi | Region, OutputARN |  |
| OutputConnected |  | None | Multi | FlowARN |  |
| OutputConnected |  | None | Multi | Region |  |
| OutputConnected |  | None | Multi | Region, AvailabilityZone |  |
| OutputDisconnections |  | Count | Sum | Region, OutputARN |  |
| OutputDisconnections |  | Count | Sum | FlowARN |  |
| OutputDisconnections |  | Count | Sum | Region |  |
| OutputDisconnections |  | Count | Sum | Region, AvailabilityZone |  |
| OverflowPackets | Количество пакетов, потерянных при передаче из-за того, что видео требовало больше буфера, чем было доступно | Count | Sum | FlowARN | Доступен |
| OverflowPackets |  | Count | Sum | Region |  |
| OverflowPackets |  | Count | Sum | Region, AvailabilityZone |  |
| PATError | Количество возникновений ошибки таблицы ассоциации программ (PAT) | Count | Sum | Region |  |
| PATError |  | Count | Sum | Region, AvailabilityZone |  |
| PATError |  | Count | Sum | FlowARN |  |
| PCRAccuracyError | Количество возникновений ошибки точности регистра программных часов (PCR) | Count | Sum | Region |  |
| PCRAccuracyError |  | Count | Sum | Region, AvailabilityZone |  |
| PCRAccuracyError |  | Count | Sum | FlowARN |  |
| PCRError | Количество возникновений ошибки PCR | Count | Sum | FlowARN |  |
| PCRError |  | Count | Sum | Region |  |
| PCRError |  | Count | Sum | Region, AvailabilityZone |  |
| PIDError | Количество возникновений ошибки идентификатора пакета (PID) | Count | Sum | Region |  |
| PIDError |  | Count | Sum | Region, AvailabilityZone |  |
| PIDError |  | Count | Sum | FlowARN |  |
| PMTError | Количество возникновений ошибки таблицы карты программ (PMT) | Count | Sum | FlowARN |  |
| PMTError |  | Count | Sum | Region |  |
| PMTError |  | Count | Sum | Region, AvailabilityZone |  |
| PTSError | Количество возникновений ошибки метки времени представления (PTS) | Count | Sum | FlowARN |  |
| PTSError |  | Count | Sum | Region |  |
| PTSError |  | Count | Sum | Region, AvailabilityZone |  |
| PacketLossPercent | Процент пакетов, потерянных при передаче, даже если они были восстановлены | Percent | Multi | Region |  |
| PacketLossPercent |  | Percent | Multi | Region, AvailabilityZone |  |
| PacketLossPercent |  | Percent | Multi | FlowARN | Доступен |
| RecoveredPackets | Количество пакетов, потерянных при передаче, но восстановленных | Count | Sum | FlowARN | Доступен |
| RecoveredPackets |  | Count | Sum | Region |  |
| RecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| RoundTripTime | Время, необходимое источнику для отправки сигнала и получения подтверждения от AWS Elemental MediaConnect | Milliseconds | Multi | Region |  |
| RoundTripTime |  | Milliseconds | Multi | Region, AvailabilityZone |  |
| RoundTripTime |  | Milliseconds | Multi | FlowARN | Доступен |
| SourceARQRecovered |  | Count | Sum | Region |  |
| SourceARQRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| SourceARQRecovered |  | Count | Sum | Region, SourceARN |  |
| SourceARQRecovered |  | Count | Sum | FlowARN |  |
| SourceARQRequests |  | Count | Sum | FlowARN |  |
| SourceARQRequests |  | Count | Sum | Region |  |
| SourceARQRequests |  | Count | Sum | Region, AvailabilityZone |  |
| SourceARQRequests |  | Count | Sum | Region, SourceARN |  |
| SourceBitRate | Битрейт входящего (исходного) видео | Bits/Second | Multi | FlowARN |  |
| SourceBitRate |  | Bits/Second | Multi | Region |  |
| SourceBitRate |  | Bits/Second | Multi | Region, AvailabilityZone |  |
| SourceBitRate |  | Bits/Second | Multi | Region, SourceARN |  |
| SourceCATError |  | Count | Sum | FlowARN |  |
| SourceCATError |  | Count | Sum | Region |  |
| SourceCATError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceCATError |  | Count | Sum | Region, SourceARN |  |
| SourceCRCError |  | Count | Sum | FlowARN |  |
| SourceCRCError |  | Count | Sum | Region |  |
| SourceCRCError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceCRCError |  | Count | Sum | Region, SourceARN |  |
| SourceConnected |  | None | Multi | Region |  |
| SourceConnected |  | None | Multi | Region, AvailabilityZone |  |
| SourceConnected |  | None | Multi | Region, SourceARN |  |
| SourceConnected |  | None | Sum | Region |  |
| SourceConnected |  | None | Sum | Region, AvailabilityZone |  |
| SourceConnected |  | None | Sum | Region, SourceARN |  |
| SourceConnected |  | None | Count | Region |  |
| SourceConnected |  | None | Count | Region, AvailabilityZone |  |
| SourceConnected |  | None | Count | Region, SourceARN |  |
| SourceConnected |  | None | Multi | FlowARN |  |
| SourceConnected |  | None | Sum | FlowARN |  |
| SourceContinuityCounter |  | Count | Sum | Region |  |
| SourceContinuityCounter |  | Count | Sum | Region, AvailabilityZone |  |
| SourceContinuityCounter |  | Count | Sum | Region, SourceARN |  |
| SourceContinuityCounter |  | Count | Sum | FlowARN |  |
| SourceDisconnections |  | Count | Sum | FlowARN |  |
| SourceDisconnections |  | Count | Sum | Region |  |
| SourceDisconnections |  | Count | Sum | Region, AvailabilityZone |  |
| SourceDisconnections |  | Count | Sum | Region, SourceARN |  |
| SourceDroppedPackets |  | Count | Sum | Region |  |
| SourceDroppedPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceDroppedPackets |  | Count | Sum | Region, SourceARN |  |
| SourceDroppedPackets |  | Count | Sum | FlowARN |  |
| SourceFECPackets |  | Count | Sum | Region |  |
| SourceFECPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceFECPackets |  | Count | Sum | Region, SourceARN |  |
| SourceFECPackets |  | Count | Sum | FlowARN |  |
| SourceFECRecovered |  | Count | Sum | Region |  |
| SourceFECRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| SourceFECRecovered |  | Count | Sum | Region, SourceARN |  |
| SourceFECRecovered |  | Count | Sum | FlowARN |  |
| SourceNotRecoveredPackets |  | Count | Sum | Region |  |
| SourceNotRecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceNotRecoveredPackets |  | Count | Sum | Region, SourceARN |  |
| SourceNotRecoveredPackets |  | Count | Sum | FlowARN |  |
| SourceOverflowPackets |  | Count | Sum | Region |  |
| SourceOverflowPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceOverflowPackets |  | Count | Sum | Region, SourceARN |  |
| SourceOverflowPackets |  | Count | Sum | FlowARN |  |
| SourcePATError |  | Count | Sum | FlowARN |  |
| SourcePATError |  | Count | Sum | Region |  |
| SourcePATError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePATError |  | Count | Sum | Region, SourceARN |  |
| SourcePCRAccuracyError |  | Count | Sum | FlowARN |  |
| SourcePCRAccuracyError |  | Count | Sum | Region |  |
| SourcePCRAccuracyError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePCRAccuracyError |  | Count | Sum | Region, SourceARN |  |
| SourcePCRError |  | Count | Sum | Region |  |
| SourcePCRError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePCRError |  | Count | Sum | Region, SourceARN |  |
| SourcePCRError |  | Count | Sum | FlowARN |  |
| SourcePIDError |  | Count | Sum | FlowARN |  |
| SourcePIDError |  | Count | Sum | Region |  |
| SourcePIDError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePIDError |  | Count | Sum | Region, SourceARN |  |
| SourcePMTError |  | Count | Sum | Region |  |
| SourcePMTError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePMTError |  | Count | Sum | Region, SourceARN |  |
| SourcePMTError |  | Count | Sum | FlowARN |  |
| SourcePTSError |  | Count | Sum | Region |  |
| SourcePTSError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePTSError |  | Count | Sum | Region, SourceARN |  |
| SourcePTSError |  | Count | Sum | FlowARN |  |
| SourcePacketLossPercent |  | Percent | Multi | FlowARN |  |
| SourcePacketLossPercent |  | Percent | Multi | Region |  |
| SourcePacketLossPercent |  | Percent | Multi | Region, AvailabilityZone |  |
| SourcePacketLossPercent |  | Percent | Multi | Region, SourceARN |  |
| SourceRecoveredPackets |  | Count | Sum | FlowARN |  |
| SourceRecoveredPackets |  | Count | Sum | Region |  |
| SourceRecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceRecoveredPackets |  | Count | Sum | Region, SourceARN |  |
| SourceRoundTripTime |  | Milliseconds | Multi | Region |  |
| SourceRoundTripTime |  | Milliseconds | Multi | Region, AvailabilityZone |  |
| SourceRoundTripTime |  | Milliseconds | Multi | Region, SourceARN |  |
| SourceRoundTripTime |  | Milliseconds | Multi | FlowARN |  |
| SourceTSByteError |  | Count | Sum | Region |  |
| SourceTSByteError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTSByteError |  | Count | Sum | Region, SourceARN |  |
| SourceTSByteError |  | Count | Sum | FlowARN |  |
| SourceTSSyncLoss |  | Count | Sum | Region |  |
| SourceTSSyncLoss |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTSSyncLoss |  | Count | Sum | Region, SourceARN |  |
| SourceTSSyncLoss |  | Count | Sum | FlowARN |  |
| SourceTotalPackets |  | Count | Sum | Region |  |
| SourceTotalPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTotalPackets |  | Count | Sum | Region, SourceARN |  |
| SourceTotalPackets |  | Count | Sum | FlowARN |  |
| SourceTransportError |  | Count | Sum | FlowARN |  |
| SourceTransportError |  | Count | Sum | Region |  |
| SourceTransportError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTransportError |  | Count | Sum | Region, SourceARN |  |
| TSByteError | Количество возникновений ошибки байта транспортного потока (TS) | Count | Sum | Region |  |
| TSByteError |  | Count | Sum | Region, AvailabilityZone |  |
| TSByteError |  | Count | Sum | FlowARN |  |
| TSSyncLoss | Количество возникновений ошибки потери синхронизации транспортного потока (TS) | Count | Sum | FlowARN |  |
| TSSyncLoss |  | Count | Sum | Region |  |
| TSSyncLoss |  | Count | Sum | Region, AvailabilityZone |  |
| TotalPackets | Общее количество полученных пакетов | Count | Sum | Region |  |
| TotalPackets |  | Count | Sum | Region, AvailabilityZone |  |
| TotalPackets |  | Count | Sum | FlowARN | Доступен |
| TransportError | Количество возникновений первичной транспортной ошибки | Count | Sum | Region |  |
| TransportError |  | Count | Sum | Region, AvailabilityZone |  |
| TransportError |  | Count | Sum | FlowARN |  |