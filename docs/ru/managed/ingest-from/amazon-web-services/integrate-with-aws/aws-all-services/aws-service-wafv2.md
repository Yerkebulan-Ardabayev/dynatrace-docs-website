---
title: Мониторинг AWS WAF
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-wafv2
scraped: 2026-03-06T21:34:02.834520
---

# Мониторинг AWS WAF

# Мониторинг AWS WAF

* Classic
* How-to guide
* 1-min read
* Published Jul 06, 2020

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая AWS WAF. Вы можете просматривать графики для каждого экземпляра сервиса с набором измерений и создавать пользовательские графики, которые можно закрепить на ваших дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate версии 1.197+

  + Для развёртываний Dynatrace SaaS необходим Environment ActiveGate или Multi-environment ActiveGate.
  + Для развёртываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (будь то в развёртывании [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") или [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) вам нужен [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.203+
* Обновлённая [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.
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

Если вы не хотите добавлять разрешения для всех сервисов и хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [Всех облачных сервисов AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса -- список дополнительных разрешений, специфичных для этого сервиса.

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

Пример JSON-политики для одного сервиса приведён ниже.

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

В этом примере из полного списка разрешений вам нужно выбрать

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **Всех облачных сервисов AWS**.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. **Страница обзора группы пользовательских устройств** содержит список всех экземпляров (пользовательских устройств), принадлежащих группе. Выберите экземпляр, чтобы просмотреть **страницу обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг предустановленный дашборд, содержащий все рекомендуемые метрики, автоматически появляется на вашей странице **Дашборды**. Для поиска конкретных дашбордов отфильтруйте по **Preset**, а затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих мониторируемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.

Чтобы удалить дашборд со страницы дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
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

![AWS wafv2](https://dt-cdn.net/images/dashboard-1390-969b949264.png)

## Доступные метрики

`WebACL` является основным измерением.

| Название | Описание | Единица измерения | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| AllowedRequests | Количество разрешённых веб-запросов | Count | Sum | WebACL, Region, Rule | Применимо |
| BlockedRequests | Количество заблокированных веб-запросов | Count | Sum | WebACL, Region, Rule | Применимо |
| CountedRequests | Количество подсчитанных веб-запросов | Count | Sum | WebACL, Region, Rule |  |

## Ограничения

Сущности Dynatrace для этого сервиса AWS не обогащаются свойством ARN.
