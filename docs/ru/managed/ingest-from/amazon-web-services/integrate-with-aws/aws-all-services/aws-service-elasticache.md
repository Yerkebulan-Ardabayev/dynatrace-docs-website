---
title: Мониторинг Amazon ElastiCache
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticache
scraped: 2026-03-06T21:30:12.764840
---

# Мониторинг Amazon ElastiCache

# Мониторинг Amazon ElastiCache

* Classic
* Практическое руководство
* Чтение: 13 мин
* Опубликовано 15 октября 2020 г.

Dynatrace принимает метрики для множества предварительно выбранных пространств имен, включая Amazon ElastiCache. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate версии 1.181+, а именно:

  + Для развертываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Интеграция метрик из Amazon CloudWatch."), так и [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) необходим [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.182+
* Обновленная [политика мониторинга AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#aws-policy-and-authentication "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.
  Чтобы [обновить политику AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведенный ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

Предопределенная JSON-политика для всех поддерживаемых сервисов

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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определенных сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Вы также можете просматривать метрики в веб-интерфейсе Dynatrace на панелях мониторинга. Для этого сервиса нет предустановленной панели мониторинга, но вы можете [создать собственную панель мониторинга](/docs/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать панели мониторинга Dynatrace.").

Чтобы проверить наличие предустановленных панелей мониторинга для каждого сервиса AWS, см. список ниже.

### Список доступных предустановленных панелей мониторинга

| Сервис AWS | Предустановленная панель мониторинга |
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

## Доступные метрики

`CacheClusterId` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| ActiveDefragHits | Количество перераспределений значений в минуту, выполненных процессом активной дефрагментации. Получено из статистики `active_defrag_hits`. | Count | Sum | CacheClusterId, CacheNodeId |  |
| ActiveDefragHits |  | Count | Sum | CacheClusterId |  |
| BytesReadIntoMemcached | Количество байт, прочитанных из сети узлом кэша | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesReadIntoMemcached |  | Bytes | Sum | CacheClusterId |  |
| BytesUsedFworCacheItems |  | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForCacheItems | Количество байт, используемых для хранения элементов кэша | Bytes | Sum | CacheClusterId |  |
| BytesUsedForCache | Общее количество байт, выделенных Redis для всех целей, включая набор данных, буферы и т.д. Получено из статистики used\_memory. | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForCache |  | Bytes | Sum | CacheClusterId |  |
| BytesUsedForHash | Количество байт, используемых хэш-таблицами в данный момент | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForHash |  | Bytes | Sum | CacheClusterId |  |
| BytesWrittenOutFromMemcached | Количество байт, записанных в сеть узлом кэша | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesWrittenOutFromMemcached |  | Bytes | Sum | CacheClusterId |  |
| CPUUtilization | Процент использования ЦП для всего хоста | Percent | Multi | CacheClusterId, CacheNodeId |  |
| CPUUtilization |  | Percent | Multi | CacheClusterId | Доступна |
| CacheHits | Количество успешных поисков ключей только для чтения в основном словаре. Получено из статистики keyspace\_hits. | Count | Sum | CacheClusterId, CacheNodeId |  |
| CacheHits |  | Count | Sum | CacheClusterId |  |
| CacheMisses | Количество неудачных поисков ключей только для чтения в основном словаре. Получено из статистики keyspace\_misses. | Count | Sum | CacheClusterId, CacheNodeId |  |
| CacheMisses |  | Count | Sum | CacheClusterId |  |
| CasBadval | Количество запросов CAS (check and set), полученных кэшем, в которых значение CAS не совпало с сохраненным значением CAS | Count | Sum | CacheClusterId, CacheNodeId |  |
| CasBadval |  | Count | Sum | CacheClusterId |  |
| CasHits | Количество запросов CAS, полученных кэшем, в которых запрашиваемый ключ был найден и значение CAS совпало | Count | Sum | CacheClusterId, CacheNodeId |  |
| CasHits |  | Count | Sum | CacheClusterId |  |
| CasMisses | Количество запросов CAS, полученных кэшем, в которых запрашиваемый ключ не был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| CasMisses |  | Count | Sum | CacheClusterId |  |
| CmdConfigGet | Совокупное количество запросов config get | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdConfigGet |  | Count | Sum | CacheClusterId |  |
| CmdConfigSet | Совокупное количество запросов config set | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdConfigSet |  | Count | Sum | CacheClusterId |  |
| CmdFlush | Количество команд flush, полученных кэшем | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdFlush |  | Count | Sum | CacheClusterId |  |
| CmdGet | Количество команд get, полученных кэшем | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdGet |  | Count | Sum | CacheClusterId |  |
| CmdSet | Количество команд set, полученных кэшем | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdSet |  | Count | Sum | CacheClusterId |  |
| CmdTouch | Совокупное количество запросов touch | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdTouch |  | Count | Sum | CacheClusterId |  |
| CurrConfig | Текущее количество сохраненных конфигураций | Count | Sum | CacheClusterId, CacheNodeId |  |
| CurrConfig |  | Count | Sum | CacheClusterId |  |
| CurrConnections | Количество подключений к кэшу в данный момент. ElastiCache использует два-три подключения для мониторинга кластера. | Count | Multi | CacheClusterId, CacheNodeId |  |
| CurrConnections |  | Count | Multi | CacheClusterId | Доступна |
| CurrItems | Количество элементов, хранящихся в кэше в данный момент | Count | Multi | CacheClusterId, CacheNodeId |  |
| CurrItems |  | Count | Multi | CacheClusterId |  |
| DatabaseMemoryUsagePercentage |  | Percent | Multi | CacheClusterId, CacheNodeId |  |
| DatabaseMemoryUsagePercentage |  | Percent | Multi | CacheClusterId |  |
| DatabaseMemoryUsagePercentage |  | Percent | Multi | Region |  |
| DecrHits | Количество запросов на уменьшение, полученных кэшем, в которых запрашиваемый ключ был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| DecrHits |  | Count | Sum | CacheClusterId |  |
| DecrMisses | Количество запросов на уменьшение, полученных кэшем, в которых запрашиваемый ключ не был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| DecrMisses |  | Count | Sum | CacheClusterId |  |
| DeleteHits | Количество запросов на удаление, полученных кэшем, в которых запрашиваемый ключ был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| DeleteHits |  | Count | Sum | CacheClusterId |  |
| DeleteMisses | Количество запросов на удаление, полученных кэшем, в которых запрашиваемый ключ не был найден. | Count | Sum | CacheClusterId, CacheNodeId |  |
| DeleteMisses |  | Count | Sum | CacheClusterId |  |
| EngineCPUUtilization | Процент использования ЦП потоком движка Redis | Percent | Multi | CacheClusterId, CacheNodeId |  |
| EngineCPUUtilization |  | Percent | Multi | CacheClusterId |  |
| EvictedUnfetched | Количество валидных элементов, вытесненных из кэша по принципу наименее недавнего использования (LRU), которые ни разу не были запрошены после записи | Count | Sum | CacheClusterId, CacheNodeId |  |
| EvictedUnfetched |  | Count | Sum | CacheClusterId |  |
| Evictions | Количество не истекших элементов, вытесненных из кэша для освобождения места для новых записей | Count | Sum | CacheClusterId, CacheNodeId |  |
| Evictions |  | Count | Sum | CacheClusterId | Доступна |
| ExpiredUnfetched | Количество истекших элементов, извлеченных из LRU, которые ни разу не были запрошены после записи | Count | Sum | CacheClusterId, CacheNodeId |  |
| ExpiredUnfetched |  | Count | Sum | CacheClusterId |  |
| FreeableMemory | Объем свободной памяти, доступной на хосте. Получено из данных ОЗУ, буферов и кэша, которые ОС сообщает как свободные. | Bytes | Multi | CacheClusterId, CacheNodeId |  |
| FreeableMemory |  | Bytes | Multi | CacheClusterId |  |
| GetHits | Количество запросов get, полученных кэшем, в которых запрашиваемый ключ был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| GetHits |  | Count | Sum | CacheClusterId |  |
| GetMisses | Количество запросов get, полученных кэшем, в которых запрашиваемый ключ не был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| GetMisses |  | Count | Sum | CacheClusterId |  |
| GetTypeCmds | Общее количество команд типа только для чтения. Получено из статистики Redis commandstats путем суммирования всех команд типа только для чтения (get, hget, scard, lrange и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| GetTypeCmds |  | Count | Sum | CacheClusterId |  |
| HashBasedCmds | Общее количество команд, основанных на хэшах. Получено из статистики Redis commandstats путем суммирования всех команд, работающих с одним или несколькими хэшами (hget, hkeys, hvals, hdel и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| HashBasedCmds |  | Count | Sum | CacheClusterId |  |
| HyperLogLogBasedCmds | Общее количество команд, основанных на HyperLogLog | Count | Sum | CacheClusterId, CacheNodeId |  |
| HyperLogLogBasedCmds |  | Count | Sum | CacheClusterId |  |
| IncrHits | Количество запросов на увеличение, полученных кэшем, в которых запрашиваемый ключ был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| IncrHits |  | Count | Sum | CacheClusterId |  |
| IncrMisses | Количество запросов на увеличение, полученных кэшем, в которых запрашиваемый ключ не был найден | Count | Sum | CacheClusterId, CacheNodeId |  |
| IncrMisses |  | Count | Sum | CacheClusterId |  |
| KeyBasedCmds | Общее количество команд, основанных на ключах. Получено из статистики Redis commandstats путем суммирования всех команд, работающих с одним или несколькими ключами в нескольких структурах данных (del, expire, rename и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| KeyBasedCmds |  | Count | Sum | CacheClusterId |  |
| KeysTracked | Количество ключей, отслеживаемых функцией отслеживания ключей Redis, в процентах от tracking-table-max-keys. Отслеживание ключей используется для поддержки кэширования на стороне клиента и уведомляет клиентов при изменении ключей. | Count | Sum | CacheClusterId, CacheNodeId |  |
| KeysTracked |  | Count | Sum | CacheClusterId |  |
| KeysTracked |  | Count | Sum | Region |  |
| ListBasedCmds | Общее количество команд, основанных на списках. Получено из статистики Redis commandstats путем суммирования всех команд, работающих с одним или несколькими списками (lindex, lrange, lpush, ltrim и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| ListBasedCmds |  | Count | Sum | CacheClusterId |  |
| Network Packets Per Second Allowance Exceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| Network Packets Per Second Allowance Exceeded |  | Count | Sum | CacheClusterId |  |
| NetworkBandwidthInAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBandwidthInAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NetworkBandwidthOutAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBandwidthOutAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NetworkBytesIn | Количество байт, прочитанных хостом из сети | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBytesIn |  | Bytes | Sum | CacheClusterId |  |
| NetworkBytesOut | Количество байт, отправленных экземпляром через все сетевые интерфейсы | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBytesOut |  | Bytes | Sum | CacheClusterId |  |
| NetworkConntrackAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkConntrackAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NetworkLinkLocalAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkLinkLocalAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NewConnections | Количество новых подключений, полученных кэшем. Получено из статистики memcached total\_connections путем записи изменения total\_connections за период времени. | Count | Sum | CacheClusterId, CacheNodeId |  |
| NewConnections |  | Count | Sum | CacheClusterId |  |
| NewItems | Количество новых элементов, сохраненных кэшем. Получено из статистики memcached total\_items путем записи изменения total\_items за период времени. | Count | Sum | CacheClusterId, CacheNodeId |  |
| NewItems |  | Count | Sum | CacheClusterId |  |
| Reclaimed | Количество истекших элементов, вытесненных кэшем для освобождения места для новых записей | Count | Sum | CacheClusterId, CacheNodeId |  |
| Reclaimed |  | Count | Sum | CacheClusterId |  |
| ReplicationBytes | Для узлов в реплицированной конфигурации ReplicationBytes показывает количество байт, отправляемых основным узлом всем его репликам. Эта метрика отражает нагрузку на запись в группе репликации. Получено из статистики master\_repl\_offset. | Bytes | Multi | CacheClusterId, CacheNodeId |  |
| ReplicationBytes |  | Bytes | Multi | CacheClusterId |  |
| ReplicationLag | Эта метрика применима только для узла, работающего как реплика для чтения. Она показывает, насколько реплика отстает (в секундах) в применении изменений от основного узла. | Seconds | Multi | CacheClusterId, CacheNodeId |  |
| ReplicationLag |  | Seconds | Multi | CacheClusterId |  |
| SaveInProgress | Эта бинарная метрика возвращает 1, когда выполняется фоновое сохранение (с разветвлением или без), и 0 в противном случае. | Count | Multi | CacheClusterId, CacheNodeId |  |
| SaveInProgress |  | Count | Multi | CacheClusterId |  |
| SetBasedCmds | Общее количество команд, основанных на множествах. Получено из статистики Redis commandstats путем суммирования всех команд, работающих с одним или несколькими множествами (scard, sdiff, sadd, sunion и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| SetBasedCmds |  | Count | Sum | CacheClusterId |  |
| SetTypeCmds | Общее количество команд типа записи. Получено из статистики Redis commandstats путем суммирования всех мутирующих типов команд, работающих с данными (set, hset, sadd, lpop и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| SetTypeCmds |  | Count | Sum | CacheClusterId |  |
| SlabsMoved | Общее количество перемещенных страниц slab | Count | Sum | CacheClusterId, CacheNodeId |  |
| SlabsMoved |  | Count | Sum | CacheClusterId |  |
| SortedSetBasedCmds | Общее количество команд, основанных на отсортированных множествах. Получено из статистики Redis commandstats путем суммирования всех команд, работающих с одним или несколькими отсортированными множествами (zcount, zrange, zrank, zadd и т.д.). | Count | Sum | CacheClusterId, CacheNodeId |  |
| SortedSetBasedCmds | Общее количество команд, основанных на строках. Получено из статистики Redis commandstats путем суммирования всех команд, работающих с одной или несколькими строками (strlen, setex, setrange и т.д.). | Count | Sum | CacheClusterId |  |
| StringBasedCmds |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| StringBasedCmds |  | Count | Sum | CacheClusterId |  |
| SwapUsage | Объем используемого swap-пространства на хосте | Bytes | Multi | CacheClusterId, CacheNodeId |  |
| SwapUsage |  | Bytes | Multi | CacheClusterId | Доступна |
| TouchHits | Количество ключей, которые были затронуты и получили новое время истечения | Count | Sum | CacheClusterId, CacheNodeId |  |
| TouchHits |  | Count | Sum | CacheClusterId |  |
| TouchMisses | Количество элементов, которые были затронуты, но не были найдены | Count | Sum | CacheClusterId, CacheNodeId |  |
| TouchMisses |  | Count | Sum | CacheClusterId |  |
| UnusedMemory | Объем памяти, не используемой данными. Получено из статистики Memcached limit\_maxbytes и bytes путем вычитания bytes из limit\_maxbytes. | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| UnusedMemory |  | Bytes | Sum | CacheClusterId |  |
