---
title: Мониторинг Amazon RDS (Relational Database Service)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new
scraped: 2026-05-12T11:30:38.888091
---

# Мониторинг Amazon RDS (Relational Database Service)

# Мониторинг Amazon RDS (Relational Database Service)

* Практическое руководство
* Чтение: 31 мин
* Обновлено 15 ноября 2023 г.

Сведения о различиях между классическими сервисами и другими сервисами см. в разделе [Переход с классических (ранее «встроенных») сервисов AWS на облачные сервисы](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Переход с классических сервисов AWS на их новые версии.").

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon RDS. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

## Предварительные требования

Чтобы включить мониторинг этого сервиса, необходимо

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace Managed можно использовать ActiveGate любого типа.

  Для доступа на основе ролей в развёртывании [Managed](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#role-based-access "Подключите аккаунт Amazon к Dynatrace Managed и начните мониторинг.") требуется [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.

* Dynatrace версии 1.200+
* Обновлённая [политика мониторинга AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Приём метрик Amazon CloudWatch."), включающая дополнительные сервисы AWS.

Чтобы [обновить политику AWS IAM](https://dt-url.net/8q038eb), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов и предпочитаете выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. В таблице приведён набор разрешений, необходимых для [всех облачных сервисов AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS в Dynatrace и просмотр доступных метрик."), и для каждого поддерживаемого сервиса приведён список необязательных разрешений, специфичных для этого сервиса.

Разрешения, необходимые для интеграции мониторинга AWS:

* `"cloudwatch:GetMetricData"`
* `"cloudwatch:GetMetricStatistics"`
* `"cloudwatch:ListMetrics"`
* `"sts:GetCallerIdentity"`
* `"tag:GetResources"`
* `"tag:GetTagKeys"`
* `"ec2:DescribeAvailabilityZones"`

### Полный список разрешений для облачных сервисов

| Имя | Разрешения |
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
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **All AWS cloud services**.

### Конечные точки AWS, которые должны быть доступны с ActiveGate, и соответствующие им сервисы AWS

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

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства:

1. Перейдите в **Technologies & Processes**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

Вы также можете просматривать метрики в веб-интерфейсе Dynatrace на дашбордах. Для этого сервиса нет предустановленного дашборда, но вы можете [создать собственный дашборд](/managed/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Узнайте, как создавать и редактировать дашборды Dynatrace.").

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | Не применимо |
| AWS Lambda (built-in) | Не применимо |
| Amazon Application and Network Load Balancer (built-in) | Не применимо |
| Amazon DynamoDB (built-in) | Не применимо |
| Amazon EBS (built-in) | Не применимо |
| Amazon EC2 (built-in) | Не применимо |
| Amazon Elastic Load Balancer (ELB) (built-in) | Не применимо |
| Amazon RDS (built-in) | Не применимо |
| Amazon S3 (built-in) | Не применимо |
| AWS Certificate Manager Private Certificate Authority | Не применимо |
| All monitored Amazon services | Не применимо |
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

Этот сервис отслеживает часть Amazon RDS (AWS/RDS). Пока этот сервис настроен, вы не можете включить сервис Amazon RDS (built-in).

Основное измерение: `DBInstanceIdentifier`.

| Имя | Описание | Измерения | Единица измерения | Рекомендуется |
| --- | --- | --- | --- | --- |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DBClusterIdentifier, Role | Количество |  |
| SumBinaryLogSize |  | Region, DatabaseClass | Количество |  |
| SumBinaryLogSize |  | Region, DBClusterIdentifier | Количество |  |
| SumBinaryLogSize |  | Region | Количество |  |
| SumBinaryLogSize |  | Region, EngineName | Количество |  |
| SumBinaryLogSize |  | Region, DBClusterIdentifier, Role | Количество |  |
| DeleteThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| Deadlocks |  | Region, DatabaseClass | Количество в секунду |  |
| Deadlocks |  | Region, DBClusterIdentifier | Количество в секунду |  |
| Deadlocks |  | Region | Количество в секунду |  |
| Deadlocks |  | Region, EngineName | Количество в секунду |  |
| Deadlocks |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DBClusterIdentifier, Role | Количество |  |
| TotalBackupStorageBilled |  | Region, DBClusterIdentifier | Байт |  |
| TotalBackupStorageBilled |  | Region, EngineName | Байт |  |
| DeleteLatency |  | Region, DatabaseClass | Миллисекунда |  |
| DeleteLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| DeleteLatency |  | Region | Миллисекунда |  |
| DeleteLatency |  | Region, EngineName | Миллисекунда |  |
| DeleteLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | DBInstanceIdentifier | Количество |  |
| DDLLatency |  | Region, DatabaseClass | Миллисекунда |  |
| DDLLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| DDLLatency |  | Region | Миллисекунда |  |
| DDLLatency |  | Region, EngineName | Миллисекунда |  |
| DDLLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| DMLLatency |  | Region, DatabaseClass | Миллисекунда |  |
| DMLLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| DMLLatency |  | Region | Миллисекунда |  |
| DMLLatency |  | Region, EngineName | Миллисекунда |  |
| DMLLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| DDLThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| DDLThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| DDLThroughput |  | Region | Количество в секунду |  |
| DDLThroughput |  | Region, EngineName | Количество в секунду |  |
| DDLThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| CommitThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| CommitThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| CommitThroughput |  | Region | Количество в секунду |  |
| CommitThroughput |  | Region, EngineName | Количество в секунду |  |
| CommitThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| ForwardingReplicaReadWaitLatency |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DBClusterIdentifier, Role | Количество |  |
| BlockedTransactions |  | Region, DatabaseClass | Количество в секунду |  |
| BlockedTransactions |  | Region, DBClusterIdentifier | Количество в секунду |  |
| BlockedTransactions |  | Region | Количество в секунду |  |
| BlockedTransactions |  | Region, EngineName | Количество в секунду |  |
| BlockedTransactions |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| EBSIOBalance% | Процент кредитов ввода-вывода, оставшихся в корзине всплеска вашей базы данных RDS. Эта метрика доступна для basic | Region, DatabaseClass | Процент |  |
| EBSIOBalance% |  | Region, DBClusterIdentifier | Процент |  |
| EBSIOBalance% |  | Region | Процент |  |
| EBSIOBalance% |  | Region, EngineName | Процент | Применимо |
| EBSIOBalance% |  | Region, DBClusterIdentifier, Role | Процент |  |
| SwapUsage | Объём пространства подкачки, используемого на экземпляре БД. | Region, DatabaseClass | Байт |  |
| SwapUsage |  | Region, DBClusterIdentifier | Байт |  |
| SwapUsage |  | Region | Байт |  |
| SwapUsage |  | Region, EngineName | Байт |  |
| SwapUsage |  | Region, DBClusterIdentifier, Role | Байт |  |
| ForwardingReplicaDMLThroughput |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_attempted |  | DBInstanceIdentifier | Количество |  |
| LoginFailures |  | Region, DatabaseClass | Количество в секунду |  |
| LoginFailures |  | Region, DBClusterIdentifier | Количество в секунду |  |
| LoginFailures |  | Region | Количество в секунду |  |
| LoginFailures |  | Region, EngineName | Количество в секунду |  |
| LoginFailures |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| NetworkTransmitThroughput | Исходящий (передаваемый) сетевой трафик на экземпляре БД, включающий как трафик клиентской базы данных, так и трафик Amazon RDS | Region, DatabaseClass | Байт в секунду |  |
| NetworkTransmitThroughput |  | Region, DBClusterIdentifier | Байт в секунду |  |
| NetworkTransmitThroughput |  | Region | Байт в секунду |  |
| NetworkTransmitThroughput |  | Region, EngineName | Байт в секунду |  |
| NetworkTransmitThroughput |  | Region, DBClusterIdentifier, Role | Байт в секунду |  |
| NumBinaryLogFiles |  | Region, DatabaseClass | Количество |  |
| NumBinaryLogFiles |  | Region, DBClusterIdentifier | Количество |  |
| NumBinaryLogFiles |  | Region | Количество |  |
| NumBinaryLogFiles |  | Region, EngineName | Количество |  |
| NumBinaryLogFiles |  | Region, DBClusterIdentifier, Role | Количество |  |
| DBLoadCPU |  | DBInstanceIdentifier | None |  |
| Aurora\_pq\_request\_failed |  | DBInstanceIdentifier | Количество |  |
| BlockedTransactions |  | DBInstanceIdentifier | Количество в секунду |  |
| ForwardingReplicaReadWaitThroughput |  | DBInstanceIdentifier | Количество |  |
| ReadThroughput | Среднее количество байт, прочитанных с диска в секунду. | Region, DatabaseClass | Байт в секунду |  |
| ReadThroughput |  | Region | Байт в секунду |  |
| ReadThroughput |  | Region, EngineName | Байт в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DBClusterIdentifier, Role | Количество |  |
| DeleteThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| DeleteThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| DeleteThroughput |  | Region | Количество в секунду |  |
| DeleteThroughput |  | Region, EngineName | Количество в секунду |  |
| DeleteThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| DBLoadCPU |  | Region | None |  |
| CommitLatency |  | Region, DatabaseClass | Миллисекунда |  |
| CommitLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| CommitLatency |  | Region | Миллисекунда |  |
| CommitLatency |  | Region, EngineName | Миллисекунда |  |
| CommitLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| ForwardingReplicaOpenSessions |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaOpenSessions |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaOpenSessions |  | Region | Количество |  |
| ForwardingReplicaOpenSessions |  | Region, EngineName | Количество |  |
| ForwardingReplicaOpenSessions |  | Region, DBClusterIdentifier, Role | Количество |  |
| BackupRetentionPeriodStorageUsed |  | Region, DBClusterIdentifier | Байт |  |
| BackupRetentionPeriodStorageUsed |  | Region, EngineName | Байт |  |
| InsertLatency |  | Region, DatabaseClass | Миллисекунда |  |
| InsertLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| InsertLatency |  | Region | Миллисекунда |  |
| InsertLatency |  | Region, EngineName | Миллисекунда |  |
| InsertLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| DMLThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| DMLThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| DMLThroughput |  | Region | Количество в секунду |  |
| DMLThroughput |  | Region, EngineName | Количество в секунду |  |
| DMLThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| Aurora\_pq\_request\_attempted |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_attempted |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_attempted |  | Region | Количество |  |
| Aurora\_pq\_request\_attempted |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_attempted |  | Region, DBClusterIdentifier, Role | Количество |  |
| DiskQueueDepth | Количество необработанных операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску. | Region, DatabaseClass | Количество |  |
| DiskQueueDepth |  | Region | Количество |  |
| DiskQueueDepth |  | Region, EngineName | Количество | Применимо |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DBClusterIdentifier, Role | Количество |  |
| BinLogDiskUsage | Объём дискового пространства, занятого бинарными логами. Если для экземпляров MySQL и MariaDB включено автоматическое резервное копирование, | Region, DatabaseClass | Байт |  |
| BinLogDiskUsage |  | Region | Байт |  |
| BinLogDiskUsage |  | Region, EngineName | Байт | Применимо |
| BinLogDiskUsage |  | Region, EngineName | Байт |  |
| ForwardingWriterDMLThroughput |  | Region, DatabaseClass | Количество |  |
| ForwardingWriterDMLThroughput |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingWriterDMLThroughput |  | Region | Количество |  |
| ForwardingWriterDMLThroughput |  | Region, EngineName | Количество |  |
| ForwardingWriterDMLThroughput |  | Region, DBClusterIdentifier, Role | Количество |  |
| Queries |  | DBInstanceIdentifier | Количество в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DBClusterIdentifier, Role | Количество |  |
| AuroraSlowConnectionHandleCount |  | Region, DatabaseClass | Количество |  |
| AuroraSlowConnectionHandleCount |  | Region, DBClusterIdentifier | Количество |  |
| AuroraSlowConnectionHandleCount |  | Region | Количество |  |
| AuroraSlowConnectionHandleCount |  | Region, EngineName | Количество |  |
| AuroraSlowConnectionHandleCount |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DBClusterIdentifier, Role | Количество |  |
| CommitThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| RollbackSegmentHistoryListLength |  | Region, DatabaseClass | Количество |  |
| RollbackSegmentHistoryListLength |  | Region, DBClusterIdentifier | Количество |  |
| RollbackSegmentHistoryListLength |  | Region | Количество |  |
| RollbackSegmentHistoryListLength |  | Region, EngineName | Количество |  |
| RollbackSegmentHistoryListLength |  | Region, DBClusterIdentifier, Role | Количество |  |
| SelectLatency |  | Region, DatabaseClass | Миллисекунда |  |
| SelectLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| SelectLatency |  | Region | Миллисекунда |  |
| SelectLatency |  | Region, EngineName | Миллисекунда |  |
| SelectLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| ForwardingReplicaDMLLatency |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaDMLLatency |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaDMLLatency |  | Region | Количество |  |
| ForwardingReplicaDMLLatency |  | Region, EngineName | Количество |  |
| ForwardingReplicaDMLLatency |  | Region, DBClusterIdentifier, Role | Количество |  |
| StorageNetworkThroughput |  | DBInstanceIdentifier | Байт в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | DBInstanceIdentifier | Количество |  |
| DatabaseConnections | Количество клиентских сетевых подключений к экземпляру базы данных. | Region, DatabaseClass | Количество |  |
| DatabaseConnections |  | Region, DBClusterIdentifier | Количество |  |
| DatabaseConnections |  | Region | Количество |  |
| DatabaseConnections |  | Region, EngineName | Количество | Применимо |
| DatabaseConnections |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DBClusterIdentifier, Role | Количество |  |
| EngineUptime |  | Region, DatabaseClass | Секунда |  |
| EngineUptime |  | Region, DBClusterIdentifier | Секунда |  |
| EngineUptime |  | Region | Секунда |  |
| EngineUptime |  | Region, EngineName | Секунда |  |
| EngineUptime |  | Region, DBClusterIdentifier, Role | Секунда |  |
| FreeStorageSpace | Объём доступного дискового пространства. | Region, DatabaseClass | Байт |  |
| FreeStorageSpace |  | Region | Байт |  |
| FreeStorageSpace |  | Region, EngineName | Байт | Применимо |
| FreeStorageSpace |  | Region, EngineName | Байт |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DBClusterIdentifier, Role | Количество |  |
| AuroraVolumeBytesLeftTotal |  | DBInstanceIdentifier | Количество |  |
| AbortedClients |  | Region, DatabaseClass | Количество |  |
| AbortedClients |  | Region, DBClusterIdentifier | Количество |  |
| AbortedClients |  | Region | Количество |  |
| AbortedClients |  | Region, EngineName | Количество |  |
| AbortedClients |  | Region, DBClusterIdentifier, Role | Количество |  |
| BufferCacheHitRatio |  | Region, DatabaseClass | Процент |  |
| BufferCacheHitRatio |  | Region, DBClusterIdentifier | Процент |  |
| BufferCacheHitRatio |  | Region | Процент |  |
| BufferCacheHitRatio |  | Region, EngineName | Процент |  |
| BufferCacheHitRatio |  | Region, DBClusterIdentifier, Role | Процент |  |
| FreeLocalStorage |  | DBInstanceIdentifier | Байт |  |
| AuroraSlowHandshakeCount |  | Region, DatabaseClass | Количество |  |
| AuroraSlowHandshakeCount |  | Region, DBClusterIdentifier | Количество |  |
| AuroraSlowHandshakeCount |  | Region | Количество |  |
| AuroraSlowHandshakeCount |  | Region, EngineName | Количество |  |
| AuroraSlowHandshakeCount |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DBClusterIdentifier, Role | Количество |  |
| ForwardingWriterDMLLatency |  | DBInstanceIdentifier | Количество |  |
| Queries |  | Region, DatabaseClass | Количество в секунду |  |
| Queries |  | Region, DBClusterIdentifier | Количество в секунду |  |
| Queries |  | Region | Количество в секунду |  |
| Queries |  | Region, EngineName | Количество в секунду |  |
| Queries |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| EBSByteBalance% | Процент кредитов пропускной способности, оставшихся в корзине всплеска вашей базы данных RDS. Эта метрика доступна | Region, DatabaseClass | Процент |  |
| EBSByteBalance% |  | Region, DBClusterIdentifier | Процент |  |
| EBSByteBalance% |  | Region | Процент |  |
| EBSByteBalance% |  | Region, EngineName | Процент | Применимо |
| EBSByteBalance% |  | Region, DBClusterIdentifier, Role | Процент |  |
| ActiveTransactions |  | Region, DatabaseClass | Количество в секунду |  |
| ActiveTransactions |  | Region, DBClusterIdentifier | Количество в секунду |  |
| ActiveTransactions |  | Region | Количество в секунду |  |
| ActiveTransactions |  | Region, EngineName | Количество в секунду |  |
| ActiveTransactions |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| InsertThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| InsertThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| InsertThroughput |  | Region | Количество в секунду |  |
| InsertThroughput |  | Region, EngineName | Количество в секунду |  |
| InsertThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| ForwardingWriterOpenSessions |  | Region, DatabaseClass | Количество |  |
| ForwardingWriterOpenSessions |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingWriterOpenSessions |  | Region | Количество |  |
| ForwardingWriterOpenSessions |  | Region, EngineName | Количество |  |
| ForwardingWriterOpenSessions |  | Region, DBClusterIdentifier, Role | Количество |  |
| SwapUsage | Объём пространства подкачки, используемого на экземпляре БД. | DBInstanceIdentifier | Байт |  |
| VolumeReadIOPs |  | Region, DbClusterIdentifier, EngineName | Количество |  |
| VolumeReadIOPs |  | Region, DBClusterIdentifier | Количество |  |
| VolumeReadIOPs |  | Region, EngineName | Количество |  |
| ForwardingWriterDMLThroughput |  | DBInstanceIdentifier | Количество |  |
| AuroraVolumeBytesLeftTotal |  | Region, DatabaseClass | Количество |  |
| AuroraVolumeBytesLeftTotal |  | Region, DBClusterIdentifier | Количество |  |
| AuroraVolumeBytesLeftTotal |  | Region | Количество |  |
| AuroraVolumeBytesLeftTotal |  | Region, EngineName | Количество |  |
| AuroraVolumeBytesLeftTotal |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DBClusterIdentifier, Role | Количество |  |
| VolumeBytesUsed |  | Region, DbClusterIdentifier, EngineName | Байт |  |
| VolumeBytesUsed |  | Region, DBClusterIdentifier | Байт |  |
| VolumeBytesUsed |  | Region, EngineName | Байт |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | DBInstanceIdentifier | Количество |  |
| UpdateLatency |  | Region, DatabaseClass | Миллисекунда |  |
| UpdateLatency |  | Region, DBClusterIdentifier | Миллисекунда |  |
| UpdateLatency |  | Region | Миллисекунда |  |
| UpdateLatency |  | Region, EngineName | Миллисекунда |  |
| UpdateLatency |  | Region, DBClusterIdentifier, Role | Миллисекунда |  |
| UpdateThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| UpdateThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| UpdateThroughput |  | Region | Количество в секунду |  |
| UpdateThroughput |  | Region, EngineName | Количество в секунду |  |
| UpdateThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| CPUUtilization | Процент использования CPU. | Region, DatabaseClass | Процент |  |
| CPUUtilization |  | Region, DBClusterIdentifier | Процент |  |
| CPUUtilization |  | Region | Процент |  |
| CPUUtilization |  | Region, EngineName | Процент | Применимо |
| CPUUtilization |  | Region, DBClusterIdentifier, Role | Процент |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_in\_progress |  | Region | Количество |  |
| Aurora\_pq\_request\_in\_progress |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DBClusterIdentifier, Role | Количество |  |
| ForwardingReplicaDMLThroughput |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaDMLThroughput |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaDMLThroughput |  | Region | Количество |  |
| ForwardingReplicaDMLThroughput |  | Region, EngineName | Количество |  |
| ForwardingReplicaDMLThroughput |  | Region, DBClusterIdentifier, Role | Количество |  |
| LVMWriteIOPS |  | Region, DatabaseClass | Количество в секунду |  |
| LVMWriteIOPS |  | Region | Количество в секунду |  |
| LVMWriteIOPS |  | Region, EngineName | Количество в секунду | Применимо |
| ForwardingReplicaSelectThroughput |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaSelectThroughput |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaSelectThroughput |  | Region | Количество |  |
| ForwardingReplicaSelectThroughput |  | Region, EngineName | Количество |  |
| ForwardingReplicaSelectThroughput |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_failed |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_failed |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_failed |  | Region | Количество |  |
| Aurora\_pq\_request\_failed |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_failed |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DBClusterIdentifier, Role | Количество |  |
| EngineUptime |  | DBInstanceIdentifier | Секунда |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DBClusterIdentifier, Role | Количество |  |
| ConnectionAttempts | Количество попыток подключения к экземпляру, как успешных, так и неуспешных. | Region, DatabaseClass | Количество |  |
| ConnectionAttempts |  | Region, DBClusterIdentifier | Количество |  |
| ConnectionAttempts |  | Region | Количество |  |
| ConnectionAttempts |  | Region, EngineName | Количество |  |
| ConnectionAttempts |  | Region, DBClusterIdentifier, Role | Количество |  |
| ForwardingWriterOpenSessions |  | DBInstanceIdentifier | Количество |  |
| NetworkThroughput |  | Region, DatabaseClass | Байт в секунду |  |
| NetworkThroughput |  | Region, DBClusterIdentifier | Байт в секунду |  |
| NetworkThroughput |  | Region | Байт в секунду |  |
| NetworkThroughput |  | Region, EngineName | Байт в секунду |  |
| NetworkThroughput |  | Region, DBClusterIdentifier, Role | Байт в секунду |  |
| RollbackSegmentHistoryListLength |  | DBInstanceIdentifier | Количество |  |
| SnapshotStorageUsed |  | Region, DBClusterIdentifier | Байт |  |
| SnapshotStorageUsed |  | Region, EngineName | Байт |  |
| AuroraBinlogReplicaLag |  | Region, DatabaseClass | Секунда |  |
| AuroraBinlogReplicaLag |  | Region, DBClusterIdentifier | Секунда |  |
| AuroraBinlogReplicaLag |  | Region | Секунда |  |
| AuroraBinlogReplicaLag |  | Region, EngineName | Секунда |  |
| AuroraBinlogReplicaLag |  | Region, DBClusterIdentifier, Role | Секунда |  |
| ForwardingReplicaSelectLatency |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaSelectLatency |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaSelectLatency |  | Region | Количество |  |
| ForwardingReplicaSelectLatency |  | Region, EngineName | Количество |  |
| ForwardingReplicaSelectLatency |  | Region, DBClusterIdentifier, Role | Количество |  |
| LVMReadIOPS |  | Region, DatabaseClass | Количество в секунду |  |
| LVMReadIOPS |  | Region | Количество в секунду |  |
| LVMReadIOPS |  | Region, EngineName | Количество в секунду | Применимо |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | DBInstanceIdentifier | Количество |  |
| FreeLocalStorage |  | Region, DatabaseClass | Байт |  |
| FreeLocalStorage |  | Region, DBClusterIdentifier | Байт |  |
| FreeLocalStorage |  | Region | Байт |  |
| FreeLocalStorage |  | Region, EngineName | Байт |  |
| FreeLocalStorage |  | Region, DBClusterIdentifier, Role | Байт |  |
| StorageNetworkReceiveThroughput |  | Region, DatabaseClass | Байт в секунду |  |
| StorageNetworkReceiveThroughput |  | Region, DBClusterIdentifier | Байт в секунду |  |
| StorageNetworkReceiveThroughput |  | Region | Байт в секунду |  |
| StorageNetworkReceiveThroughput |  | Region, EngineName | Байт в секунду |  |
| StorageNetworkReceiveThroughput |  | Region, DBClusterIdentifier, Role | Байт в секунду |  |
| Aurora\_pq\_request\_executed |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_executed |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_executed |  | Region | Количество |  |
| Aurora\_pq\_request\_executed |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_executed |  | Region, DBClusterIdentifier, Role | Количество |  |
| ReadLatency | Среднее время, затрачиваемое на одну операцию ввода-вывода диска. | Region, DatabaseClass | Секунда |  |
| ReadLatency |  | Region, DBClusterIdentifier | Секунда |  |
| ReadLatency |  | Region | Секунда |  |
| ReadLatency |  | Region, EngineName | Секунда |  |
| ReadLatency |  | Region, DBClusterIdentifier, Role | Секунда |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DBClusterIdentifier, Role | Количество |  |
| FreeableMemory | Объём доступной оперативной памяти. | DBInstanceIdentifier | Байт | Применимо |
| FreeableMemory |  | DBInstanceIdentifier | Байт |  |
| FreeableMemory |  | DBInstanceIdentifier | Байт |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DBClusterIdentifier, Role | Количество |  |
| AuroraSlowConnectionHandleCount |  | DBInstanceIdentifier | Количество |  |
| StorageNetworkThroughput |  | Region, DatabaseClass | Байт в секунду |  |
| StorageNetworkThroughput |  | Region, DBClusterIdentifier | Байт в секунду |  |
| StorageNetworkThroughput |  | Region | Байт в секунду |  |
| StorageNetworkThroughput |  | Region, EngineName | Байт в секунду |  |
| StorageNetworkThroughput |  | Region, DBClusterIdentifier, Role | Байт в секунду |  |
| ActiveTransactions |  | DBInstanceIdentifier | Количество в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DBClusterIdentifier, Role | Количество |  |
| LoginFailures |  | DBInstanceIdentifier | Количество в секунду |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaReadWaitThroughput |  | Region | Количество |  |
| ForwardingReplicaReadWaitThroughput |  | Region, EngineName | Количество |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DBClusterIdentifier, Role | Количество |  |
| SelectLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| VolumeWriteIOPs |  | Region, DbClusterIdentifier, EngineName | Количество |  |
| VolumeWriteIOPs |  | Region, DBClusterIdentifier | Количество |  |
| VolumeWriteIOPs |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DBClusterIdentifier, Role | Количество |  |
| AuroraBinlogReplicaLag |  | DBInstanceIdentifier | Секунда |  |
| RowLockTime |  | Region, DatabaseClass | Количество |  |
| RowLockTime |  | Region, DBClusterIdentifier | Количество |  |
| RowLockTime |  | Region | Количество |  |
| RowLockTime |  | Region, EngineName | Количество |  |
| RowLockTime |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DBClusterIdentifier, Role | Количество |  |
| ForwardingWriterDMLLatency |  | Region, DatabaseClass | Количество |  |
| ForwardingWriterDMLLatency |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingWriterDMLLatency |  | Region | Количество |  |
| ForwardingWriterDMLLatency |  | Region, EngineName | Количество |  |
| ForwardingWriterDMLLatency |  | Region, DBClusterIdentifier, Role | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DBClusterIdentifier, Role | Количество |  |
| CommitLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| ForwardingReplicaSelectLatency |  | DBInstanceIdentifier | Количество |  |
| ReadIOPS | Среднее количество операций ввода-вывода чтения с диска в секунду. | Region, DatabaseClass | Количество в секунду |  |
| ReadIOPS |  | Region | Количество в секунду |  |
| ReadIOPS |  | Region, EngineName | Количество в секунду |  |
| StorageNetworkTransmitThroughput |  | DBInstanceIdentifier | Байт в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | DBInstanceIdentifier | Количество |  |
| WriteLatency | Среднее время, затрачиваемое на одну операцию ввода-вывода диска. | Region, DatabaseClass | Секунда |  |
| WriteLatency |  | Region, DBClusterIdentifier | Секунда |  |
| WriteLatency |  | Region | Секунда |  |
| WriteLatency |  | Region, EngineName | Секунда |  |
| WriteLatency |  | Region, DBClusterIdentifier, Role | Секунда |  |
| SelectThroughput |  | Region, DatabaseClass | Количество в секунду |  |
| SelectThroughput |  | Region, DBClusterIdentifier | Количество в секунду |  |
| SelectThroughput |  | Region | Количество в секунду |  |
| SelectThroughput |  | Region, EngineName | Количество в секунду |  |
| SelectThroughput |  | Region, DBClusterIdentifier, Role | Количество в секунду |  |
| Aurora\_pq\_request\_not\_chosen |  | DBInstanceIdentifier | Количество |  |
| FreeableMemory | Объём доступной оперативной памяти. | Region, DatabaseClass | Байт |  |
| FreeableMemory |  | Region, DBClusterIdentifier | Байт |  |
| FreeableMemory |  | Region | Байт |  |
| FreeableMemory |  | Region, EngineName | Байт | Применимо |
| FreeableMemory |  | Region, DBClusterIdentifier, Role | Байт |  |
| FreeableMemory |  | Region, EngineName | Байт |  |
| ReadLatency | Среднее время, затрачиваемое на одну операцию ввода-вывода диска. | DBInstanceIdentifier | Секунда | Применимо |
| DMLLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| NetworkReceiveThroughput | Входящий (принимаемый) сетевой трафик на экземпляре БД, включающий как трафик клиентской базы данных, так и трафик Amazon RDS | DBInstanceIdentifier | Байт в секунду | Применимо |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | DBInstanceIdentifier | Количество |  |
| UpdateLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| DBLoad |  | DBInstanceIdentifier | None |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | DBInstanceIdentifier | Количество |  |
| BinLogDiskUsage | Объём дискового пространства, занятого бинарными логами. Если для экземпляров MySQL и MariaDB включено автоматическое резервное копирование, | DBInstanceIdentifier | Байт | Применимо |
| BinLogDiskUsage |  | DBInstanceIdentifier | Байт |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | DBInstanceIdentifier | Количество |  |
| DDLLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| SumBinaryLogSize |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_in\_progress |  | DBInstanceIdentifier | Количество |  |
| DatabaseConnections | Количество клиентских сетевых подключений к экземпляру базы данных. | DBInstanceIdentifier | Количество | Применимо |
| CPUUtilization | Процент использования CPU. | DBInstanceIdentifier | Процент | Применимо |
| ForwardingReplicaReadWaitLatency |  | Region, DatabaseClass | Количество |  |
| ForwardingReplicaReadWaitLatency |  | Region, DBClusterIdentifier | Количество |  |
| ForwardingReplicaReadWaitLatency |  | Region | Количество |  |
| ForwardingReplicaReadWaitLatency |  | Region, EngineName | Количество |  |
| ForwardingReplicaReadWaitLatency |  | Region, DBClusterIdentifier, Role | Количество |  |
| AbortedClients |  | DBInstanceIdentifier | Количество |  |
| ReadThroughput | Среднее количество байт, прочитанных с диска в секунду. | DBInstanceIdentifier | Байт в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_throttled |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_throttled |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_throttled |  | Region | Количество |  |
| Aurora\_pq\_request\_throttled |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_throttled |  | Region, DBClusterIdentifier, Role | Количество |  |
| AuroraDMLRejectedWriterFull |  | Region, DatabaseClass | Количество |  |
| AuroraDMLRejectedWriterFull |  | Region, DBClusterIdentifier | Количество |  |
| AuroraDMLRejectedWriterFull |  | Region | Количество |  |
| AuroraDMLRejectedWriterFull |  | Region, EngineName | Количество |  |
| AuroraDMLRejectedWriterFull |  | Region, DBClusterIdentifier, Role | Количество |  |
| ForwardingReplicaDMLLatency |  | DBInstanceIdentifier | Количество |  |
| WriteThroughput | Среднее количество байт, записанных на диск в секунду. | DBInstanceIdentifier | Байт в секунду |  |
| DiskQueueDepth | Количество необработанных операций ввода-вывода (запросов чтения/записи), ожидающих доступа к диску. | DBInstanceIdentifier | Количество | Применимо |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | DBInstanceIdentifier | Количество |  |
| ForwardingReplicaOpenSessions |  | DBInstanceIdentifier | Количество |  |
| StorageNetworkTransmitThroughput |  | Region, DatabaseClass | Байт в секунду |  |
| StorageNetworkTransmitThroughput |  | Region, DBClusterIdentifier | Байт в секунду |  |
| StorageNetworkTransmitThroughput |  | Region | Байт в секунду |  |
| StorageNetworkTransmitThroughput |  | Region, EngineName | Байт в секунду |  |
| StorageNetworkTransmitThroughput |  | Region, DBClusterIdentifier, Role | Байт в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | DBInstanceIdentifier | Количество |  |
| RowLockTime |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | DBInstanceIdentifier | Количество |  |
| NetworkReceiveThroughput | Входящий (принимаемый) сетевой трафик на экземпляре БД, включающий как трафик клиентской базы данных, так и трафик Amazon RDS | Region, DatabaseClass | Байт в секунду |  |
| NetworkReceiveThroughput |  | Region, DBClusterIdentifier | Байт в секунду |  |
| NetworkReceiveThroughput |  | Region | Байт в секунду |  |
| NetworkReceiveThroughput |  | Region, EngineName | Байт в секунду | Применимо |
| NetworkReceiveThroughput |  | Region, DBClusterIdentifier, Role | Байт в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | DBInstanceIdentifier | Количество |  |
| DBLoadNonCPU |  | DBInstanceIdentifier | None |  |
| WriteIOPS | Среднее количество операций ввода-вывода записи на диск в секунду. | Region, DatabaseClass | Количество в секунду |  |
| WriteIOPS |  | Region | Количество в секунду |  |
| WriteIOPS |  | Region, EngineName | Количество в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | DBInstanceIdentifier | Количество |  |
| BurstBalance | Процент доступных кредитов ввода-вывода корзины всплеска для General Purpose SSD (gp2). | DBInstanceIdentifier | Процент | Применимо |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DatabaseClass | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DBClusterIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, EngineName | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DBClusterIdentifier, Role | Количество |  |
| DMLThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| WriteIOPS | Среднее количество операций ввода-вывода записи на диск в секунду. | DBInstanceIdentifier | Количество в секунду |  |
| WriteThroughput | Среднее количество байт, записанных на диск в секунду. | Region, DatabaseClass | Байт в секунду |  |
| WriteThroughput |  | Region | Байт в секунду |  |
| WriteThroughput |  | Region, EngineName | Байт в секунду |  |
| BufferCacheHitRatio |  | DBInstanceIdentifier | Процент |  |
| ConnectionAttempts | Количество попыток подключения к экземпляру, как успешных, так и неуспешных. | DBInstanceIdentifier | Количество |  |
| NetworkTransmitThroughput | Исходящий (передаваемый) сетевой трафик на экземпляре БД, включающий как трафик клиентской базы данных, так и трафик Amazon RDS | DBInstanceIdentifier | Байт в секунду |  |
| Aurora\_pq\_request\_executed |  | DBInstanceIdentifier | Количество |  |
| UpdateThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| ForwardingReplicaSelectThroughput |  | DBInstanceIdentifier | Количество |  |
| StorageNetworkReceiveThroughput |  | DBInstanceIdentifier | Байт в секунду |  |
| DeleteLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| DDLThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| ReadIOPS | Среднее количество операций ввода-вывода чтения с диска в секунду. | DBInstanceIdentifier | Количество в секунду |  |
| EBSByteBalance% | Процент кредитов пропускной способности, оставшихся в корзине всплеска вашей базы данных RDS. Эта метрика доступна | DBInstanceIdentifier | Процент | Применимо |
| NetworkThroughput |  | DBInstanceIdentifier | Байт в секунду |  |
| DBLoad |  | Region | None |  |
| Deadlocks |  | DBInstanceIdentifier | Количество в секунду |  |
| AuroraSlowHandshakeCount |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_throttled |  | DBInstanceIdentifier | Количество |  |
| LVMReadIOPS |  | DBInstanceIdentifier | Количество в секунду | Применимо |
| NumBinaryLogFiles |  | DBInstanceIdentifier | Количество |  |
| EBSIOBalance% | Процент кредитов ввода-вывода, оставшихся в корзине всплеска вашей базы данных RDS. Эта метрика доступна для basic | DBInstanceIdentifier | Процент | Применимо |
| BurstBalance | Процент доступных кредитов ввода-вывода корзины всплеска для General Purpose SSD (gp2). | Region, DatabaseClass | Процент |  |
| BurstBalance |  | Region | Процент |  |
| BurstBalance |  | Region, EngineName | Процент | Применимо |
| FreeStorageSpace | Объём доступного дискового пространства. | DBInstanceIdentifier | Байт | Применимо |
| FreeStorageSpace |  | DBInstanceIdentifier | Байт |  |
| FreeStorageSpace |  | DBInstanceIdentifier | Байт |  |
| DBLoadNonCPU |  | Region | None |  |
| AuroraDMLRejectedWriterFull |  | DBInstanceIdentifier | Количество |  |
| InsertLatency |  | DBInstanceIdentifier | Миллисекунда |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | DBInstanceIdentifier | Количество |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | DBInstanceIdentifier | Количество |  |
| SelectThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| InsertThroughput |  | DBInstanceIdentifier | Количество в секунду |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | DBInstanceIdentifier | Количество |  |
| WriteLatency | Среднее время, затрачиваемое на одну операцию ввода-вывода диска. | DBInstanceIdentifier | Секунда | Применимо |
| LVMWriteIOPS |  | DBInstanceIdentifier | Количество в секунду | Применимо |