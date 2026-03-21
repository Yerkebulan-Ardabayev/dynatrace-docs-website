---
title: Мониторинг AWS DMS (Database Migration Service)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-database-migration-service-dms
scraped: 2026-03-06T21:36:46.245735
---

* 9-min read

Dynatrace собирает метрики для множества предварительно выбранных пространств имен, включая AWS DMS. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate version 1.197+

* Для развертываний Dynatrace SaaS вам необходим Environment ActiveGate или Multi-environment ActiveGate.

  Для ролевого доступа в развертывании [SaaS](../cloudwatch-metrics.md#role-based-access "Integrate metrics from Amazon CloudWatch.") вам необходим [Environment ActiveGate](../../../dynatrace-activegate/installation.md "Learn how to configure ActiveGate") установленный на хосте Amazon EC2.

* Dynatrace version 1.200+
* Обновлённая [политика мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Integrate metrics from Amazon CloudWatch.") для включения дополнительных сервисов AWS.

Чтобы [обновить политику AWS IAM](https://dt-url.net/8q038eb), используйте приведенный ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

Предопределенная политика JSON для всех поддерживаемых сервисов

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

Если вы не хотите добавлять разрешения для всех сервисов и хотите выбрать разрешения только для определенных сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [All AWS cloud services](../aws-all-services.md "Monitor all AWS cloud services with Dynatrace and view available metrics.") и для каждого поддерживаемого сервиса список необязательных разрешений, специфичных для этого сервиса.

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
| All monitored Amazon services Required | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
| AWS Certificate Manager Private Certificate Authority | `acm-pca:ListCertificateAuthorities` |
| Amazon MQ |  |
| Amazon API Gateway | `apigateway:GET` |
| AWS App Runner | `apprunner:ListServices` |
| Amazon AppStream | `appstream:DescribeFleets` |
| AWS AppSync | `appsync:ListGraphqlApis` |
| Amazon Athena | `athena:ListWorkGroups` |
| Amazon Aurora | `rds:DescribeDBClusters` |
| Amazon EC2 Auto Scaling | `autoscaling:DescribeAutoScalingGroups` |
| Amazon EC2 Auto Scaling (built-in) | `autoscaling:DescribeAutoScalingGroups` |
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
| Amazon DynamoDB (built-in) | `dynamodb:ListTables`, `dynamodb:ListTagsOfResource` |
| Amazon EBS | `ec2:DescribeVolumes` |
| Amazon EBS (built-in) | `ec2:DescribeVolumes` |
| Amazon EC2 API |  |
| Amazon EC2 (built-in) | `ec2:DescribeInstances` |
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
| Amazon Elastic Load Balancer (ELB) (built-in) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
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
| AWS Lambda (built-in) | `lambda:ListFunctions`, `lambda:ListTags` |
| Amazon Lex | `lex:GetBots` |
| Amazon Application and Network Load Balancer (built-in) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
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
| Amazon RDS (built-in) | `rds:DescribeDBInstances`, `rds:DescribeEvents`, `rds:ListTagsForResource` |
| Amazon Redshift | `redshift:DescribeClusters` |
| Amazon Rekognition |  |
| AWS RoboMaker | `robomaker:ListSimulationJobs` |
| Amazon Route 53 | `route53:ListHostedZones` |
| Amazon Route 53 Resolver | `route53resolver:ListResolverEndpoints` |
| Amazon S3 | `s3:ListAllMyBuckets` |
| Amazon S3 (built-in) | `s3:ListAllMyBuckets` |
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

В этом примере из полного списка разрешений необходимо выбрать

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"`, and `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

### Конечные точки AWS, которые должны быть доступны из ActiveGate, с соответствующими сервисами AWS

| Конечная точка | Сервис |
| --- | --- |
| `autoscaling.<REGION>.amazonaws.com` | Amazon EC2 Auto Scaling (built-in), Amazon EC2 Auto Scaling |
| `lambda.<REGION>.amazonaws.com` | AWS Lambda (built-in), AWS Lambda |
| `elasticloadbalancing.<REGION>.amazonaws.com` | Amazon Application and Network Load Balancer (built-in), Amazon Elastic Load Balancer (ELB) (built-in) |
| `dynamodb.<REGION>.amazonaws.com` | Amazon DynamoDB (built-in), Amazon DynamoDB |
| `ec2.<REGION>.amazonaws.com` | Amazon EBS (built-in), Amazon EC2 (built-in), Amazon EBS, Amazon EC2 Spot Fleet, Amazon VPC NAT Gateways, AWS Transit Gateway, AWS Site-to-Site VPN |
| `rds.<REGION>.amazonaws.com` | Amazon RDS (built-in), Amazon Aurora, Amazon DocumentDB, Amazon Neptune, Amazon RDS |
| `s3.<REGION>.amazonaws.com` | Amazon S3 (built-in) |
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

Чтобы узнать, как включить мониторинг сервиса, смотрите [Включение мониторинга сервиса](../aws-metrics-ingest/aws-enable-service-monitoring.md "Enable AWS monitoring in Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. **Страница обзора группы пользовательских устройств** отображает все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

После добавления сервиса в мониторинг предустановленная панель мониторинга со всеми рекомендуемыми метриками автоматически появляется на вашей странице **Dashboards**. Для поиска конкретных панелей мониторинга отфильтруйте по **Preset**, а затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих мониторируемых сервисов может потребоваться повторное сохранение ваших учетных данных, чтобы предустановленная панель мониторинга появилась на странице **Dashboards**. Для повторного сохранения учетных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленную панель мониторинга напрямую, но можете клонировать и отредактировать её. Чтобы клонировать панель мониторинга, откройте меню (**...**) и выберите **Clone**.

Чтобы убрать панель мониторинга со страницы панелей мониторинга, вы можете скрыть её. Чтобы скрыть панель мониторинга, откройте меню (**...**) и выберите **Hide**.

Скрытие панели мониторинга не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Для проверки доступности предустановленных панелей мониторинга для каждого сервиса AWS смотрите список ниже.

### Список доступности предустановленных панелей мониторинга

| Сервис AWS | Предустановленная панель |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | Неприменимо |
| AWS Lambda (built-in) | Неприменимо |
| Amazon Application and Network Load Balancer (built-in) | Неприменимо |
| Amazon DynamoDB (built-in) | Неприменимо |
| Amazon EBS (built-in) | Неприменимо |
| Amazon EC2 (built-in) | Неприменимо |
| Amazon Elastic Load Balancer (ELB) (built-in) | Неприменимо |
| Amazon RDS (built-in) | Неприменимо |
| Amazon S3 (built-in) | Неприменимо |
| AWS Certificate Manager Private Certificate Authority | Неприменимо |
| All monitored Amazon services | Неприменимо |
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

![Database migration](https://dt-cdn.net/images/dashboard-23-1733-1da69ef82c.png)

## Доступные метрики

`ReplicationInstanceIdentifier` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| CDCChangesDiskSource | Количество строк, накапливающихся на диске и ожидающих фиксации из источника | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| CDCChangesDiskTarget | Количество строк, накапливающихся на диске и ожидающих фиксации в целевой базе данных | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| CDCChangesMemorySource | Количество строк, накапливающихся в памяти и ожидающих фиксации из источника | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| CDCChangesMemoryTarget | Количество строк, накапливающихся в памяти и ожидающих фиксации в целевой базе данных | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| CDCIncomingChanges | Общее количество событий изменений в определённый момент времени, ожидающих применения к целевой базе данных | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CDCLatencySource | Разрыв в секундах между последним событием, захваченным из конечной точки источника, и текущей системной меткой времени экземпляра AWS DMS. CDCLatencySource представляет задержку между источником и экземпляром репликации. | Seconds | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CDCLatencyTarget | Разрыв в секундах между меткой времени первого события, ожидающего фиксации в целевой базе данных, и текущей меткой времени экземпляра AWS DMS. CDCLatencyTarget представляет задержку между экземпляром репликации и целевой базой данных. | Seconds | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CDCThroughputBandwidthSource | Входящие данные, полученные из источника, в КБ в секунду | Kilobytes/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CDCThroughputBandwidthTarget | Исходящие данные, переданные в целевую базу данных, в КБ в секунду | Kilobytes/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CDCThroughputRowsSource | Входящие изменения задачи из источника в строках в секунду | Count/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CDCThroughputRowsTarget | Исходящие изменения задачи для целевой базы данных в строках в секунду | Count/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CPUAllocated | Процент CPU, максимально выделенный для задачи (0 означает отсутствие ограничения) | Percent | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| CPUUtilization | Объём использования CPU | Percent | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| CPUUtilization |  | Percent | Multi | ReplicationInstanceIdentifier | Применимо |
| CPUUtilization |  | Percent | Multi | Region, ReplicationInstanceExternalResourceId | Применимо |
| CPUUtilization |  | Percent | Multi | Region | Применимо |
| CPUUtilization |  | Percent | Multi | Region, InstanceClass |  |
| DiskQueueDepth | Количество невыполненных операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску | Count | Multi | Region, ReplicationInstanceExternalResourceId |  |
| DiskQueueDepth |  | Count | Multi | Region |  |
| DiskQueueDepth |  | Count | Multi | Region, InstanceClass |  |
| DiskQueueDepth |  | Count | Multi | ReplicationInstanceIdentifier |  |
| FreeStorageSpace | Объём доступного дискового пространства | Bytes | Multi | ReplicationInstanceIdentifier | Применимо |
| FreeStorageSpace |  | Bytes | Multi | Region, ReplicationInstanceExternalResourceId |  |
| FreeStorageSpace |  | Bytes | Multi | Region |  |
| FreeStorageSpace |  | Bytes | Multi | Region, InstanceClass |  |
| FreeableMemory | Объём доступной оперативной памяти | Bytes | Multi | ReplicationInstanceIdentifier | Применимо |
| FreeableMemory |  | Bytes | Multi | Region, ReplicationInstanceExternalResourceId |  |
| FreeableMemory |  | Bytes | Multi | Region |  |
| FreeableMemory |  | Bytes | Multi | Region, InstanceClass |  |
| FullLoadThroughputBandwidthSource | Входящие данные при полной загрузке из источника в килобайтах (КБ) в секунду | Kilobytes/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| FullLoadThroughputBandwidthTarget | Исходящие данные при полной загрузке для целевой базы данных в килобайтах (КБ) в секунду | Kilobytes/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| FullLoadThroughputRowsSource | Входящие изменения при полной загрузке из источника в строках в секунду | Count/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| FullLoadThroughputRowsTarget | Исходящие изменения при полной загрузке для целевой базы данных в строках в секунду | Count/Second | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| MemoryAllocated | Максимальное выделение памяти для задачи (0 означает отсутствие ограничений) | Megabytes | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| MemoryUsage | Размер резидентного набора (RSS), занимаемый задачей. Указывает долю памяти, занимаемую задачей в основной памяти (RAM). | Megabytes | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| NetworkReceiveThroughput | Входящий сетевой трафик на экземпляре репликации, включая как трафик клиентской базы данных, так и трафик AWS DMS, используемый для мониторинга и репликации | Bytes/Second | Multi | ReplicationInstanceIdentifier | Применимо |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region, ReplicationInstanceExternalResourceId |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region, InstanceClass |  |
| NetworkTransmitThroughput | Исходящий сетевой трафик на экземпляре репликации, включая как трафик клиентской базы данных, так и трафик AWS DMS, используемый для мониторинга и репликации | Bytes/Second | Multi | ReplicationInstanceIdentifier | Применимо |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region, ReplicationInstanceExternalResourceId |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region, InstanceClass |  |
| ReadIOPS | Среднее количество операций чтения ввода-вывода с диска в секунду | Count/Second | Multi | ReplicationInstanceIdentifier | Применимо |
| ReadIOPS |  | Count/Second | Multi | Region, ReplicationInstanceExternalResourceId |  |
| ReadIOPS |  | Count/Second | Multi | Region |  |
| ReadIOPS |  | Count/Second | Multi | Region, InstanceClass |  |
| ReadLatency | Среднее время, затраченное на одну операцию ввода-вывода (чтение) с диска | Seconds | Multi | ReplicationInstanceIdentifier | Применимо |
| ReadLatency |  | Seconds | Multi | Region, ReplicationInstanceExternalResourceId |  |
| ReadLatency |  | Seconds | Multi | Region |  |
| ReadLatency |  | Seconds | Multi | Region, InstanceClass |  |
| ReadThroughput | Среднее количество байтов, прочитанных с диска в секунду | Bytes/Second | Multi | ReplicationInstanceIdentifier | Применимо |
| ReadThroughput |  | Bytes/Second | Multi | Region, ReplicationInstanceExternalResourceId |  |
| ReadThroughput |  | Bytes/Second | Multi | Region |  |
| ReadThroughput |  | Bytes/Second | Multi | Region, InstanceClass |  |
| RecoveryCount |  | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| RunCounter |  | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| SwapUsage | Объём использованного пространства подкачки на экземпляре репликации | Bytes | Multi | ReplicationInstanceIdentifier | Применимо |
| SwapUsage |  | Bytes | Multi | Region, ReplicationInstanceExternalResourceId |  |
| SwapUsage |  | Bytes | Multi | Region |  |
| SwapUsage |  | Bytes | Multi | Region, InstanceClass |  |
| ValidationAttemptedRecordCount | Количество строк, для которых была предпринята попытка валидации, в минуту | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| ValidationBulkQuerySourceLatency | AWS DMS может выполнять массовую валидацию данных, особенно в определённых сценариях при полной загрузке или текущей репликации с большим количеством изменений. Эта метрика указывает задержку, необходимую для чтения массового набора данных из конечной точки источника. | Milliseconds | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| ValidationBulkQueryTargetLatency | AWS DMS может выполнять массовую валидацию данных, особенно в определённых сценариях при полной загрузке или текущей репликации с большим количеством изменений. Эта метрика указывает задержку, необходимую для чтения массового набора данных на целевой конечной точке. | Milliseconds | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| ValidationFailedOverallCount | Количество строк, для которых валидация завершилась неудачей | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| ValidationItemQuerySourceLatency | Во время текущей репликации валидация данных может выявлять текущие изменения и проверять их. Эта метрика указывает задержку при чтении этих изменений из источника. | Milliseconds | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| ValidationItemQueryTargetLatency | Во время текущей репликации валидация данных может выявлять текущие изменения и проверять их построчно. Эта метрика показывает задержку при чтении этих изменений из целевой базы данных. | Milliseconds | Multi | ReplicationInstanceIdentifier, ReplicationTaskIdentifier |  |
| ValidationPendingOverallCount | Количество строк, для которых валидация ещё не завершена | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| ValidationSucceededRecordCount | Количество строк, прошедших валидацию AWS DMS, в минуту | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| ValidationSuspendedOverallCount | Количество строк, для которых валидация была приостановлена | Count | Sum | ReplicationInstanceIdentifier, ReplicationTaskIdentifier | Применимо |
| WriteIOPS | Среднее количество операций записи ввода-вывода на диск в секунду | Count/Second | Multi | ReplicationInstanceIdentifier | Применимо |
| WriteIOPS |  | Count/Second | Multi | Region, ReplicationInstanceExternalResourceId |  |
| WriteIOPS |  | Count/Second | Multi | Region |  |
| WriteIOPS |  | Count/Second | Multi | Region, InstanceClass |  |
| WriteLatency | Среднее время, затраченное на одну операцию ввода-вывода (запись) на диск | Seconds | Multi | ReplicationInstanceIdentifier | Применимо |
| WriteLatency |  | Seconds | Multi | Region, ReplicationInstanceExternalResourceId |  |
| WriteLatency |  | Seconds | Multi | Region |  |
| WriteLatency |  | Seconds | Multi | Region, InstanceClass |  |
| WriteThroughput | Среднее количество байтов, записанных на диск в секунду | Bytes/Second | Multi | ReplicationInstanceIdentifier | Применимо |
| WriteThroughput |  | Bytes/Second | Multi | Region, ReplicationInstanceExternalResourceId |  |
| WriteThroughput |  | Bytes/Second | Multi | Region |  |
| WriteThroughput |  | Bytes/Second | Multi | Region, InstanceClass |  |

## Ограничения

Для сбора метрик об изменениях, захваченных задачей миграции (метрики CDC) на MySQL, должны быть включены настройки двоичного журналирования и автоматического резервного копирования.