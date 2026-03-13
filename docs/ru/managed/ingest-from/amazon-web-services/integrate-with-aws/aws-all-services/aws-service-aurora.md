---
title: Мониторинг Amazon Aurora
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-aurora
scraped: 2026-03-06T21:37:03.991711
---

# Мониторинг Amazon Aurora

# Мониторинг Amazon Aurora

* Classic
* Практическое руководство
* Чтение: 22 мин
* Опубликовано 15 окт. 2020 г.

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая Amazon Aurora. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса необходимо:

* ActiveGate версии 1.181+, а именно:

  + Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развёртываний Dynatrace Managed можно использовать любой вид ActiveGate.

    Для доступа на основе ролей (в развёртываниях [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") или [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) требуется [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.182+
* Обновлённая [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#aws-policy-and-authentication "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных AWS сервисов.
  Для [обновления политики AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) используйте JSON ниже, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. В таблице содержится набор разрешений, необходимых для [всех AWS облачных сервисов](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Мониторинг всех AWS облачных сервисов с Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех AWS облачных сервисов**.

### Конечные точки AWS, которые должны быть доступны из ActiveGate, с соответствующими AWS сервисами

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

Этот сервис отслеживает кластеры Amazon RDS. Уже отслеживаемые ресурсы можно найти на странице обзора AWS в разделе **Cloud services**.

Для мониторинга экземпляров RDS вместо кластеров обратитесь к сервису Amazon RDS и разделу **RDS** на странице обзора AWS.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Выполните фильтрацию по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы попадёте на **страницу обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Вы также можете просматривать метрики в веб-интерфейсе Dynatrace на дашбордах. Для этого сервиса нет стандартного дашборда, но вы можете [создать собственный дашборд](../../../../../analyze-explore-automate/dashboards-classic/dashboards/create-dashboards.md "Узнайте, как создавать и редактировать дашборды Dynatrace.").

Для проверки наличия стандартных дашбордов для каждого AWS сервиса см. список ниже.

### Список наличия стандартных дашбордов

| AWS сервис | Стандартный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Недоступно |
| AWS Lambda (встроенный) | Недоступно |
| Amazon Application and Network Load Balancer (встроенный) | Недоступно |
| Amazon DynamoDB (встроенный) | Недоступно |
| Amazon EBS (встроенный) | Недоступно |
| Amazon EC2 (встроенный) | Недоступно |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Недоступно |
| Amazon RDS (встроенный) | Недоступно |
| Amazon S3 (встроенный) | Недоступно |
| AWS Certificate Manager Private Certificate Authority | Недоступно |
| Все отслеживаемые сервисы Amazon | Недоступно |
| Amazon API Gateway | Недоступно |
| AWS App Runner | Недоступно |
| Amazon AppStream | Доступно |
| AWS AppSync | Доступно |
| Amazon Athena | Доступно |
| Amazon Aurora | Недоступно |
| Amazon EC2 Auto Scaling | Доступно |
| AWS Billing | Доступно |
| Amazon Keyspaces | Доступно |
| AWS Chatbot | Доступно |
| Amazon CloudFront | Недоступно |
| AWS CloudHSM | Доступно |
| Amazon CloudSearch | Доступно |
| AWS CodeBuild | Доступно |
| Amazon Cognito | Недоступно |
| Amazon Connect | Доступно |
| AWS DataSync | Доступно |
| Amazon DynamoDB Accelerator (DAX) | Доступно |
| AWS Database Migration Service (AWS DMS) | Доступно |
| Amazon DocumentDB | Доступно |
| AWS Direct Connect | Доступно |
| Amazon DynamoDB | Недоступно |
| Amazon EBS | Недоступно |
| Amazon EC2 Spot Fleet | Недоступно |
| Amazon EC2 API | Доступно |
| Amazon Elastic Container Service (ECS) | Недоступно |
| Amazon ECS Container Insights | Доступно |
| Amazon Elastic File System (EFS) | Недоступно |
| Amazon Elastic Kubernetes Service (EKS) | Доступно |
| Amazon ElastiCache (EC) | Недоступно |
| AWS Elastic Beanstalk | Доступно |
| Amazon Elastic Inference | Доступно |
| Amazon Elastic Transcoder | Доступно |
| Amazon Elastic Map Reduce (EMR) | Недоступно |
| Amazon Elasticsearch Service (ES) | Недоступно |
| Amazon EventBridge | Доступно |
| Amazon FSx | Доступно |
| Amazon GameLift | Доступно |
| AWS Glue | Недоступно |
| Amazon Inspector | Доступно |
| AWS Internet of Things (IoT) | Недоступно |
| AWS IoT Things Graph | Доступно |
| AWS IoT Analytics | Доступно |
| Amazon Managed Streaming for Kafka | Доступно |
| Amazon Kinesis Data Analytics | Недоступно |
| Amazon Data Firehose | Недоступно |
| Amazon Kinesis Data Streams | Недоступно |
| Amazon Kinesis Video Streams | Недоступно |
| AWS Lambda | Недоступно |
| Amazon Lex | Доступно |
| Amazon CloudWatch Logs | Доступно |
| AWS Elemental MediaTailor | Доступно |
| AWS Elemental MediaConnect | Доступно |
| AWS Elemental MediaConvert | Доступно |
| AWS Elemental MediaPackage Live | Доступно |
| AWS Elemental MediaPackage Video on Demand | Доступно |
| Amazon MQ | Доступно |
| Amazon VPC NAT Gateways | Недоступно |
| Amazon Neptune | Доступно |
| AWS OpsWorks | Доступно |
| Amazon Polly | Доступно |
| Amazon QLDB | Доступно |
| Amazon RDS | Недоступно |
| Amazon Redshift | Недоступно |
| Amazon Rekognition | Доступно |
| AWS RoboMaker | Доступно |
| Amazon Route 53 | Доступно |
| Amazon Route 53 Resolver | Доступно |
| Amazon S3 | Недоступно |
| Amazon SageMaker Batch Transform Jobs | Недоступно |
| Amazon SageMaker Endpoints | Недоступно |
| Amazon SageMaker Endpoint Instances | Недоступно |
| Amazon SageMaker Ground Truth | Недоступно |
| Amazon SageMaker Processing Jobs | Недоступно |
| Amazon SageMaker Training Jobs | Недоступно |
| AWS Service Catalog | Доступно |
| Amazon Simple Email Service (SES) | Недоступно |
| Amazon Simple Notification Service (SNS) | Недоступно |
| Amazon Simple Queue Service (SQS) | Недоступно |
| AWS Systems Manager - Run Command | Доступно |
| AWS Step Functions | Доступно |
| AWS Storage Gateway | Доступно |
| Amazon SWF | Доступно |
| Amazon Textract | Доступно |
| AWS Transfer Family | Доступно |
| AWS Transit Gateway | Доступно |
| Amazon Translate | Доступно |
| AWS Trusted Advisor | Доступно |
| AWS API Usage | Доступно |
| AWS Site-to-Site VPN | Доступно |
| AWS WAF Classic | Доступно |
| AWS WAF | Доступно |
| Amazon WorkMail | Доступно |
| Amazon WorkSpaces | Доступно |

## Доступные метрики

`DBClusterIdentifier` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендовано |
| --- | --- | --- | --- | --- | --- |
| ActiveTransactions | Среднее количество текущих транзакций, выполняемых на экземпляре базы данных Aurora в секунду | Count/Second | Average | DBClusterIdentifier, Role |  |
| ActiveTransactions |  | Count/Second | Average | DBClusterIdentifier |  |
| ActiveTransactions |  | Count/Second | Average | DatabaseClass, Region |  |
| ActiveTransactions |  | Count/Second | Average | EngineName, Region |  |
| ActiveTransactions |  | Count/Second | Average | Region |  |
| ActiveTransactions |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| ActiveTransactions |  | Count/Second | Maximum | DBClusterIdentifier |  |
| ActiveTransactions |  | Count/Second | Maximum | DatabaseClass, Region |  |
| ActiveTransactions |  | Count/Second | Maximum | EngineName, Region |  |
| ActiveTransactions |  | Count/Second | Maximum | Region |  |
| AuroraBinlogReplicaLag | Время отставания реплики кластера БД на Aurora с совместимостью MySQL от исходного кластера БД | Seconds | Multi | DBClusterIdentifier, Role |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | DBClusterIdentifier |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | DatabaseClass, Region |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | EngineName, Region |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | Region |  |
| AuroraReplicaLagMaximum | Максимальное отставание между основным экземпляром и каждым экземпляром Aurora БД в кластере БД | Milliseconds | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | DBClusterIdentifier |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | DatabaseClass, Region |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | EngineName, Region |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | Region |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | DBClusterIdentifier |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | DatabaseClass, Region |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | EngineName, Region |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | Region |  |
| AuroraReplicaLag | Для реплики Aurora: время отставания при репликации обновлений от основного экземпляра | Milliseconds | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLag |  | Milliseconds | Average | DBClusterIdentifier |  |
| AuroraReplicaLag |  | Milliseconds | Average | DatabaseClass, Region |  |
| AuroraReplicaLag |  | Milliseconds | Average | EngineName, Region |  |
| AuroraReplicaLag |  | Milliseconds | Average | Region |  |
| BacktrackChangeRecordsCreationRate | Количество записей об изменениях для отслеживания, созданных за 5 минут для вашего кластера БД | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | EngineName, Region |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | Region |  |
| BacktrackChangeRecordsStored | Количество записей об изменениях для отслеживания, используемых вашим кластером БД | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackChangeRecordsStored |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackChangeRecordsStored |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackChangeRecordsStored |  | Count | Sum | EngineName, Region |  |
| BacktrackChangeRecordsStored |  | Count | Sum | Region |  |
| BacktrackWindowActual | Разница между целевым и фактическим окном отслеживания | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackWindowActual |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackWindowActual |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackWindowActual |  | Count | Sum | EngineName, Region |  |
| BacktrackWindowActual |  | Count | Sum | Region |  |
| BacktrackWindowAlert | Количество случаев, когда фактическое окно отслеживания меньше целевого за заданный период | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackWindowAlert |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackWindowAlert |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackWindowAlert |  | Count | Sum | EngineName, Region |  |
| BacktrackWindowAlert |  | Count | Sum | Region |  |
| BinLogDiskUsage | Объём дискового пространства, занятого двоичными журналами на основном экземпляре | Bytes | Average | DBClusterIdentifier, Role |  |
| BinLogDiskUsage |  | Bytes | Average | DBClusterIdentifier |  |
| BinLogDiskUsage |  | Bytes | Average | DatabaseClass, Region |  |
| BinLogDiskUsage |  | Bytes | Average | EngineName, Region |  |
| BinLogDiskUsage |  | Bytes | Average | Region |  |
| BlockedTransactions | Среднее количество заблокированных транзакций в базе данных в секунду | Count/Second | Average | DBClusterIdentifier, Role |  |
| BlockedTransactions |  | Count/Second | Average | DBClusterIdentifier |  |
| BlockedTransactions |  | Count/Second | Average | DatabaseClass, Region |  |
| BlockedTransactions |  | Count/Second | Average | EngineName, Region |  |
| BlockedTransactions |  | Count/Second | Average | Region |  |
| BlockedTransactions |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| BlockedTransactions |  | Count/Second | Maximum | DBClusterIdentifier |  |
| BlockedTransactions |  | Count/Second | Maximum | DatabaseClass, Region |  |
| BlockedTransactions |  | Count/Second | Maximum | EngineName, Region |  |
| BlockedTransactions |  | Count/Second | Maximum | Region |  |
| BufferCacheHitRatio | Процент запросов, обслуженных из кэша буфера | Percent | Average | DBClusterIdentifier, Role |  |
| BufferCacheHitRatio |  | Percent | Average | DBClusterIdentifier |  |
| BufferCacheHitRatio |  | Percent | Average | DatabaseClass, Region |  |
| BufferCacheHitRatio |  | Percent | Average | EngineName, Region |  |
| BufferCacheHitRatio |  | Percent | Average | Region |  |
| CPUCreditBalance | Количество кредитов ЦПУ, накопленных экземпляром, отчитывается с интервалом 5 минут. Метрика применима только к экземплярам `db.t2.small` и `db.t2.medium`. Используйте её для определения, как долго экземпляр Aurora MySQL DB может работать сверх базового уровня производительности с заданной скоростью. | Count | Average | DBClusterIdentifier, Role |  |
| CPUCreditBalance |  | Count | Average | DBClusterIdentifier |  |
| CPUCreditBalance |  | Count | Average | DatabaseClass, Region |  |
| CPUCreditBalance |  | Count | Average | EngineName, Region |  |
| CPUCreditBalance |  | Count | Average | Region |  |
| CPUCreditUsage | Количество кредитов ЦПУ, использованных за указанный период, отчитывается с интервалом 5 минут. Метрика применима только к экземплярам `db.t2.small` и `db.t2.medium`. Измеряет время, в течение которого физические ЦПУ использовались для обработки инструкций виртуальными ЦПУ, выделенными экземпляру Aurora MySQL DB. | Count | Average | DBClusterIdentifier, Role |  |
| CPUCreditUsage |  | Count | Average | DBClusterIdentifier |  |
| CPUCreditUsage |  | Count | Average | DatabaseClass, Region |  |
| CPUCreditUsage |  | Count | Average | EngineName, Region |  |
| CPUCreditUsage |  | Count | Average | Region |  |
| CPUUtilization | Процент использования ЦПУ экземпляром Aurora DB | Percent | Average | DBClusterIdentifier, Role |  |
| CPUUtilization |  | Percent | Average | DBClusterIdentifier |  |
| CPUUtilization |  | Percent | Average | DatabaseClass, Region |  |
| CPUUtilization |  | Percent | Average | EngineName, Region |  |
| CPUUtilization |  | Percent | Average | Region |  |
| CPUUtilization |  | Percent | Maximum | DBClusterIdentifier, Role |  |
| CPUUtilization |  | Percent | Maximum | DBClusterIdentifier |  |
| CPUUtilization |  | Percent | Maximum | DatabaseClass, Region |  |
| CPUUtilization |  | Percent | Maximum | EngineName, Region |  |
| CPUUtilization |  | Percent | Maximum | Region |  |
| CommitLatency | Задержка операций фиксации | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| CommitLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| CommitLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| CommitLatency |  | Milliseconds | Multi | EngineName, Region |  |
| CommitLatency |  | Milliseconds | Multi | Region |  |
| CommitThroughput | Среднее количество операций фиксации в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| CommitThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| CommitThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| CommitThroughput |  | Count/Second | Multi | EngineName, Region |  |
| CommitThroughput |  | Count/Second | Multi | Region |  |
| DDLLatency | Задержка запросов языка определения данных (DDL), таких как create, alter и drop | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| DDLLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| DDLLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| DDLLatency |  | Milliseconds | Multi | EngineName, Region |  |
| DDLLatency |  | Milliseconds | Multi | Region |  |
| DDLThroughput | Среднее количество DDL-запросов в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| DDLThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| DDLThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| DDLThroughput |  | Count/Second | Multi | EngineName, Region |  |
| DDLThroughput |  | Count/Second | Multi | Region |  |
| DMLLatency | Задержка операций вставки, обновления и удаления | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| DMLLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| DMLLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| DMLLatency |  | Milliseconds | Multi | EngineName, Region |  |
| DMLLatency |  | Milliseconds | Multi | Region |  |
| DMLThroughput | Среднее количество операций вставки, обновления и удаления в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| DMLThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| DMLThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| DMLThroughput |  | Count/Second | Multi | EngineName, Region |  |
| DMLThroughput |  | Count/Second | Multi | Region |  |
| DatabaseConnections | Количество подключений к экземпляру Aurora DB | Count | Average | DBClusterIdentifier, Role |  |
| DatabaseConnections |  | Count | Average | DBClusterIdentifier |  |
| DatabaseConnections |  | Count | Average | DatabaseClass, Region |  |
| DatabaseConnections |  | Count | Average | EngineName, Region |  |
| DatabaseConnections |  | Count | Average | Region |  |
| DatabaseConnections |  | Count | Maximum | DBClusterIdentifier, Role |  |
| DatabaseConnections |  | Count | Maximum | DBClusterIdentifier |  |
| DatabaseConnections |  | Count | Maximum | DatabaseClass, Region |  |
| DatabaseConnections |  | Count | Maximum | EngineName, Region |  |
| DatabaseConnections |  | Count | Maximum | Region |  |
| Deadlocks | Среднее количество взаимоблокировок в базе данных в секунду | Count/Second | Average | DBClusterIdentifier, Role |  |
| Deadlocks |  | Count/Second | Average | DBClusterIdentifier |  |
| Deadlocks |  | Count/Second | Average | DatabaseClass, Region |  |
| Deadlocks |  | Count/Second | Average | EngineName, Region |  |
| Deadlocks |  | Count/Second | Average | Region |  |
| Deadlocks |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| Deadlocks |  | Count/Second | Maximum | DBClusterIdentifier |  |
| Deadlocks |  | Count/Second | Maximum | DatabaseClass, Region |  |
| Deadlocks |  | Count/Second | Maximum | EngineName, Region |  |
| Deadlocks |  | Count/Second | Maximum | Region |  |
| DeleteLatency | Задержка запросов удаления | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| DeleteLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| DeleteLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| DeleteLatency |  | Milliseconds | Multi | EngineName, Region |  |
| DeleteLatency |  | Milliseconds | Multi | Region |  |
| DeleteThroughput | Среднее количество запросов удаления в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| DeleteThroughput |  | Count/Second | Multi | DBClusterIdentifier | Доступно |
| DeleteThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| DeleteThroughput |  | Count/Second | Multi | EngineName, Region |  |
| DeleteThroughput |  | Count/Second | Multi | Region |  |
| DiskQueueDepth | Количество ожидающих запросов чтения/записи на диск | Count | Multi | DBClusterIdentifier, Role |  |
| DiskQueueDepth |  | Count | Multi | DBClusterIdentifier |  |
| DiskQueueDepth |  | Count | Multi | DatabaseClass, Region |  |
| DiskQueueDepth |  | Count | Multi | EngineName, Region |  |
| DiskQueueDepth |  | Count | Multi | Region |  |
| EngineUptime | Время работы экземпляра | Seconds | Average | DBClusterIdentifier, Role |  |
| EngineUptime |  | Seconds | Average | DBClusterIdentifier |  |
| EngineUptime |  | Seconds | Average | DatabaseClass, Region |  |
| EngineUptime |  | Seconds | Average | EngineName, Region |  |
| EngineUptime |  | Seconds | Average | Region |  |
| FreeLocalStorage | Объём локального хранилища, доступного для каждого экземпляра БД. | Bytes | Average | DBClusterIdentifier, Role |  |
| FreeLocalStorage |  | Bytes | Average | DBClusterIdentifier |  |
| FreeLocalStorage |  | Bytes | Average | DatabaseClass, Region |  |
| FreeLocalStorage |  | Bytes | Average | EngineName, Region |  |
| FreeLocalStorage |  | Bytes | Average | Region |  |
| FreeableMemory | Объём доступной оперативной памяти | Bytes | Average | DBClusterIdentifier, Role |  |
| FreeableMemory |  | Bytes | Average | DBClusterIdentifier |  |
| FreeableMemory |  | Bytes | Average | DatabaseClass, Region |  |
| FreeableMemory |  | Bytes | Average | EngineName, Region |  |
| FreeableMemory |  | Bytes | Average | Region |  |
| InsertLatency | Задержка запросов вставки | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| InsertLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| InsertLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| InsertLatency |  | Milliseconds | Multi | EngineName, Region |  |
| InsertLatency |  | Milliseconds | Multi | Region |  |
| InsertThroughput | Среднее количество запросов вставки в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| InsertThroughput |  | Count/Second | Multi | DBClusterIdentifier | Доступно |
| InsertThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| InsertThroughput |  | Count/Second | Multi | EngineName, Region |  |
| InsertThroughput |  | Count/Second | Multi | Region |  |
| LoginFailures | Среднее количество неудачных попыток входа в секунду | Count/Second | Average | DBClusterIdentifier, Role |  |
| LoginFailures |  | Count/Second | Average | DBClusterIdentifier |  |
| LoginFailures |  | Count/Second | Average | DatabaseClass, Region |  |
| LoginFailures |  | Count/Second | Average | EngineName, Region |  |
| LoginFailures |  | Count/Second | Average | Region |  |
| LoginFailures |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| LoginFailures |  | Count/Second | Maximum | DBClusterIdentifier |  |
| LoginFailures |  | Count/Second | Maximum | DatabaseClass, Region |  |
| LoginFailures |  | Count/Second | Maximum | EngineName, Region |  |
| LoginFailures |  | Count/Second | Maximum | Region |  |
| MaximumUsedTransactionIDs | Возраст самой старой незавершённой транзакции в транзакциях. Если это значение достигает `2`,`146`,`483`,`648` (2^31 - 1 000 000), база данных переводится в режим только для чтения во избежание переполнения идентификатора транзакции. | Count | Average | DBClusterIdentifier, Role |  |
| MaximumUsedTransactionIDs |  | Count | Average | DBClusterIdentifier |  |
| MaximumUsedTransactionIDs |  | Count | Average | DatabaseClass, Region |  |
| MaximumUsedTransactionIDs |  | Count | Average | EngineName, Region |  |
| MaximumUsedTransactionIDs |  | Count | Average | Region |  |
| NetworkReceiveThroughput | Объём сетевой пропускной способности, полученной от клиентов каждым экземпляром кластера Aurora MySQL DB. Не включает сетевой трафик между экземплярами кластера Aurora DB и томом кластера. | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkThroughput | Объём сетевой пропускной способности, полученной от клиентов и переданной клиентам каждым экземпляром кластера Aurora MySQL DB. Не включает сетевой трафик между экземплярами кластера БД и томом кластера. | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| NetworkThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| NetworkThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkTransmitThroughput | Объём сетевой пропускной способности, переданной клиентам каждым экземпляром кластера Aurora DB. Не включает сетевой трафик между экземплярами кластера БД и томом кластера. | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region |  |
| Queries | Среднее количество запросов в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| Queries |  | Count/Second | Multi | DBClusterIdentifier | Доступно |
| Queries |  | Count/Second | Multi | DatabaseClass, Region |  |
| Queries |  | Count/Second | Multi | EngineName, Region |  |
| Queries |  | Count/Second | Multi | Region |  |
| RDSToAuroraPostgreSQLReplicaLag | Отставание при репликации обновлений от основного экземпляра RDS PostgreSQL в другие узлы кластера | Seconds | Multi | DBClusterIdentifier, Role |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | DBClusterIdentifier |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | DatabaseClass, Region |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | EngineName, Region |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | Region |  |
| ReadIOPS | Среднее количество дисковых операций ввода-вывода в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| ReadIOPS |  | Count/Second | Multi | DBClusterIdentifier |  |
| ReadIOPS |  | Count/Second | Multi | DatabaseClass, Region |  |
| ReadIOPS |  | Count/Second | Multi | EngineName, Region |  |
| ReadIOPS |  | Count/Second | Multi | Region |  |
| ReadLatency | Среднее время выполнения одной дисковой операции ввода-вывода | Seconds | Multi | DBClusterIdentifier, Role |  |
| ReadLatency |  | Seconds | Multi | DBClusterIdentifier |  |
| ReadLatency |  | Seconds | Multi | DatabaseClass, Region |  |
| ReadLatency |  | Seconds | Multi | EngineName, Region |  |
| ReadLatency |  | Seconds | Multi | Region |  |
| ReadThroughput | Среднее количество байт, считываемых с диска в секунду | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| ReadThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| ReadThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| ReadThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| ReadThroughput |  | Bytes/Second | Multi | Region |  |
| ResultSetCacheHitRatio | Процент запросов, обслуженных из кэша наборов результатов | Percent | Average | DBClusterIdentifier, Role |  |
| ResultSetCacheHitRatio |  | Percent | Average | DBClusterIdentifier |  |
| ResultSetCacheHitRatio |  | Percent | Average | DatabaseClass, Region |  |
| ResultSetCacheHitRatio |  | Percent | Average | EngineName, Region |  |
| ResultSetCacheHitRatio |  | Percent | Average | Region |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | DBClusterIdentifier, Role |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | DBClusterIdentifier |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | DatabaseClass, Region |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | EngineName, Region |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | Region |  |
| SelectLatency | Задержка запросов выборки | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| SelectLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| SelectLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| SelectLatency |  | Milliseconds | Multi | EngineName, Region |  |
| SelectLatency |  | Milliseconds | Multi | Region |  |
| SelectThroughput | Среднее количество запросов выборки в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| SelectThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| SelectThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| SelectThroughput |  | Count/Second | Multi | EngineName, Region |  |
| SelectThroughput |  | Count/Second | Multi | Region |  |
| SwapUsage | Объём используемого swap-пространства на экземпляре Aurora PostgreSQL DB | Bytes | Multi | DBClusterIdentifier, Role |  |
| SwapUsage |  | Bytes | Multi | DBClusterIdentifier |  |
| SwapUsage |  | Bytes | Multi | DatabaseClass, Region |  |
| SwapUsage |  | Bytes | Multi | EngineName, Region |  |
| SwapUsage |  | Bytes | Multi | Region |  |
| TransactionLogsDiskUsage | Объём дискового пространства, занятого журналами транзакций на экземпляре Aurora PostgreSQL DB. Метрика генерируется только при использовании Aurora PostgreSQL с логической репликацией или AWS Database Migration Service. По умолчанию Aurora PostgreSQL использует записи журнала, а не журналы транзакций. Когда журналы транзакций не используются, значение этой метрики равно -1. | Bytes | Multi | DBClusterIdentifier, Role |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | DBClusterIdentifier |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | DatabaseClass, Region |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | EngineName, Region |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | Region |  |
| UpdateLatency | Задержка запросов обновления | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| UpdateLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| UpdateLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| UpdateLatency |  | Milliseconds | Multi | EngineName, Region |  |
| UpdateLatency |  | Milliseconds | Multi | Region |  |
| UpdateThroughput | Среднее количество запросов обновления в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| UpdateThroughput |  | Count/Second | Multi | DBClusterIdentifier | Доступно |
| UpdateThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| UpdateThroughput |  | Count/Second | Multi | EngineName, Region |  |
| UpdateThroughput |  | Count/Second | Multi | Region |  |
| VolumeBytesUsed | Объём хранилища, используемого вашим экземпляром Aurora DB. Это значение влияет на стоимость кластера Aurora DB. | Bytes | Multi | DBClusterIdentifier, Role |  |
| VolumeBytesUsed |  | Bytes | Multi | DBClusterIdentifier |  |
| VolumeBytesUsed |  | Bytes | Multi | DatabaseClass, Region |  |
| VolumeBytesUsed |  | Bytes | Multi | EngineName, Region |  |
| VolumeBytesUsed |  | Bytes | Multi | Region |  |
| VolumeReadIOPs | Количество оплачиваемых операций чтения ввода-вывода из тома кластера за 5-минутный интервал | Count/Second | Multi | DBClusterIdentifier, Role |  |
| VolumeReadIOPs |  | Count/Second | Multi | DBClusterIdentifier |  |
| VolumeReadIOPs |  | Count/Second | Multi | DatabaseClass, Region |  |
| VolumeReadIOPs |  | Count/Second | Multi | EngineName, Region |  |
| VolumeReadIOPs |  | Count/Second | Multi | Region |  |
| VolumeWriteIOPs | Количество операций записи дискового ввода-вывода в том кластера, отчитывается с интервалом 5 минут | Count/Second | Multi | DBClusterIdentifier, Role |  |
| VolumeWriteIOPs |  | Count/Second | Multi | DBClusterIdentifier |  |
| VolumeWriteIOPs |  | Count/Second | Multi | DatabaseClass, Region |  |
| VolumeWriteIOPs |  | Count/Second | Multi | EngineName, Region |  |
| VolumeWriteIOPs |  | Count/Second | Multi | Region |  |
| WriteIOPS | Среднее количество дисковых операций ввода-вывода в секунду | Count/Second | Multi | DBClusterIdentifier, Role |  |
| WriteIOPS |  | Count/Second | Multi | DBClusterIdentifier |  |
| WriteIOPS |  | Count/Second | Multi | DatabaseClass, Region |  |
| WriteIOPS |  | Count/Second | Multi | EngineName, Region |  |
| WriteIOPS |  | Count/Second | Multi | Region |  |
| WriteLatency | Среднее время выполнения одной дисковой операции ввода-вывода | Seconds | Multi | DBClusterIdentifier, Role |  |
| WriteLatency |  | Seconds | Multi | DBClusterIdentifier |  |
| WriteLatency |  | Seconds | Multi | DatabaseClass, Region |  |
| WriteLatency |  | Seconds | Multi | EngineName, Region |  |
| WriteLatency |  | Seconds | Multi | Region |  |
| WriteThroughput | Среднее количество байт, записываемых на диск | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| WriteThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| WriteThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| WriteThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| WriteThroughput |  | Bytes/Second | Multi | Region |  |
