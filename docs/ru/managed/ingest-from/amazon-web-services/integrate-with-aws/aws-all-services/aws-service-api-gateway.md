---
title: Мониторинг Amazon API Gateway
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-gateway
scraped: 2026-02-27T21:20:40.379719
---

# Мониторинг Amazon API Gateway

# Мониторинг Amazon API Gateway

* Практическое руководство
* Чтение: 3 мин
* Обновлено 09 янв. 2026 г.

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая Amazon API Gateway. Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закреплять на дашбордах.

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

Чтобы получить метрики в данном наборе измерений [`ApiName`, `Method`, `Resource`, `Stage`], необходимо включить **детальные метрики CloudWatch**. Это можно сделать в консоли, выбрав **Enable detailed CloudWatch metrics** на вкладке **Logs** или **Tracing** этапа.

Также можно использовать команду AWS CLI `update-stage` для обновления свойства `metricsEnabled` до значения `true`.

[Amazon API Gateway Version 2 API (WebSocket и HTTP API)](https://dt-url.net/dt03xj6) в настоящее время не поддерживается для Amazon API Gateway. Поддерживается только [Amazon API Gateway Version 1 API (REST APIs)](https://dt-url.net/l523xes).

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

`ApiName` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендовано |
| --- | --- | --- | --- | --- | --- |
| 4XXError | Количество ошибок на стороне клиента за заданный период | Count | Sum | ApiName | Доступно |
| 4XXError |  | Count | Sum | ApiName, Stage |  |
| 4XXError |  | Count | Sum | ApiName, Method, Resource, Stage |  |
| 5XXError | Количество ошибок на стороне сервера за заданный период | Count | Sum | ApiName | Доступно |
| 5XXError |  | Count | Sum | ApiName, Stage |  |
| 5XXError |  | Count | Sum | ApiName, Method, Resource, Stage |  |
| CacheHitCount | Количество запросов, обслуженных из кэша API за заданный период | Count | Sum | ApiName |  |
| CacheHitCount |  | Count | Sum | ApiName, Method, Resource, Stage |  |
| CacheHitCount |  | Count | Sum | ApiName, Method, Resource, Stage |  |
| CacheMissCount | Количество запросов, обслуженных из бэкенда за заданный период, когда кэширование API включено | Count | Sum | ApiName |  |
| CacheMissCount |  | Count | Sum | ApiName, Stage |  |
| CacheMissCount |  | Count | Sum | ApiName, Method, Resource, Stage |  |
| Count | Общее количество API-запросов за заданный период | Count | Count | Region |  |
| Count |  | Count | Count | ApiName | Доступно |
| Count |  | Count | Count | ApiName, Stage |  |
| Count |  | Count | Count | ApiName, Method, Resource, Stage |  |
| IntegrationLatency | Время между передачей запроса API Gateway бэкенду и получением ответа от бэкенда | Milliseconds | Multi | ApiName | Доступно |
| IntegrationLatency |  | Milliseconds | Multi | ApiName, Stage |  |
| IntegrationLatency |  | Milliseconds | Multi | ApiName, Method, Resource, Stage |  |
| Latency | Время между получением API Gateway запроса от клиента и возвратом ответа клиенту. Задержка включает задержку интеграции и другие накладные расходы API Gateway. | Milliseconds | Multi | ApiName | Доступно |
| Latency |  | Milliseconds | Multi | ApiName, Stage |  |
| Latency |  | Milliseconds | Multi | ApiName, Method, Resource, Stage |  |
