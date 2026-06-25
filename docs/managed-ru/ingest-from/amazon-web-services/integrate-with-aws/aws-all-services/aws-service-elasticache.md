---
title: Мониторинг Amazon ElastiCache
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticache
scraped: 2026-05-12T11:29:22.646085
---

# Мониторинг Amazon ElastiCache

# Мониторинг Amazon ElastiCache

* Практическое руководство
* Чтение: 13 мин
* Опубликовано 15 октября 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon ElastiCache. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

## Предварительные требования

Чтобы включить мониторинг этого сервиса, необходимо

* ActiveGate версии 1.181+, а именно:

  + Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развёртываний Dynatrace Managed можно использовать ActiveGate любого типа.

    Для доступа на основе ролей (в развёртывании [SaaS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Приём метрик Amazon CloudWatch.") или [Managed](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#role-based-access "Подключите аккаунт Amazon к Dynatrace Managed и начните мониторинг.")) требуется [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.182+
* Обновлённая [политика мониторинга AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#aws-policy-and-authentication "Приём метрик Amazon CloudWatch."), включающая дополнительные сервисы AWS.
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

Основное измерение: `CacheClusterId`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ActiveDefragHits | Количество перераспределений значений в минуту, выполненных процессом активной дефрагментации. Вычисляется на основе статистики `active_defrag_hits`. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| ActiveDefragHits |  | Количество | Sum | CacheClusterId |  |
| BytesReadIntoMemcached | Количество байт, прочитанных из сети узлом кэша | Байт | Sum | CacheClusterId, CacheNodeId |  |
| BytesReadIntoMemcached |  | Байт | Sum | CacheClusterId |  |
| BytesUsedFworCacheItems |  | Байт | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForCacheItems | Количество байт, используемых для хранения элементов кэша | Байт | Sum | CacheClusterId |  |
| BytesUsedForCache | Общее количество байт, выделенных Redis для всех целей, включая набор данных, буферы и т. д. Вычисляется на основе статистики used_memory. | Байт | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForCache |  | Байт | Sum | CacheClusterId |  |
| BytesUsedForHash | Количество байт, используемых в настоящее время хеш-таблицами | Байт | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForHash |  | Байт | Sum | CacheClusterId |  |
| BytesWrittenOutFromMemcached | Количество байт, записанных в сеть узлом кэша | Байт | Sum | CacheClusterId, CacheNodeId |  |
| BytesWrittenOutFromMemcached |  | Байт | Sum | CacheClusterId |  |
| CPUUtilization | Процент загрузки CPU для всего хоста | Процент | Multi | CacheClusterId, CacheNodeId |  |
| CPUUtilization |  | Процент | Multi | CacheClusterId | Применимо |
| CacheHits | Количество успешных операций поиска ключей только для чтения в основном словаре. Вычисляется на основе статистики keyspace_hits. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CacheHits |  | Количество | Sum | CacheClusterId |  |
| CacheMisses | Количество неуспешных операций поиска ключей только для чтения в основном словаре. Вычисляется на основе статистики keyspace_misses. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CacheMisses |  | Количество | Sum | CacheClusterId |  |
| CasBadval | Количество запросов CAS (check and set), полученных кэшем, в которых значение CAS не совпало с сохранённым значением CAS | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CasBadval |  | Количество | Sum | CacheClusterId |  |
| CasHits | Количество запросов CAS, полученных кэшем, в которых запрошенный ключ был найден и значение CAS совпало | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CasHits |  | Количество | Sum | CacheClusterId |  |
| CasMisses | Количество запросов CAS, полученных кэшем, в которых запрошенный ключ не был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CasMisses |  | Количество | Sum | CacheClusterId |  |
| CmdConfigGet | Накопительное количество запросов config get | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CmdConfigGet |  | Количество | Sum | CacheClusterId |  |
| CmdConfigSet | Накопительное количество запросов config set | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CmdConfigSet |  | Количество | Sum | CacheClusterId |  |
| CmdFlush | Количество команд flush, полученных кэшем | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CmdFlush |  | Количество | Sum | CacheClusterId |  |
| CmdGet | Количество команд get, полученных кэшем | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CmdGet |  | Количество | Sum | CacheClusterId |  |
| CmdSet | Количество команд set, полученных кэшем | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CmdSet |  | Количество | Sum | CacheClusterId |  |
| CmdTouch | Накопительное количество запросов touch | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CmdTouch |  | Количество | Sum | CacheClusterId |  |
| CurrConfig | Текущее количество сохранённых конфигураций | Количество | Sum | CacheClusterId, CacheNodeId |  |
| CurrConfig |  | Количество | Sum | CacheClusterId |  |
| CurrConnections | Количество подключений, установленных к кэшу в определённый момент времени. ElastiCache использует два-три из этих подключений для мониторинга кластера. | Количество | Multi | CacheClusterId, CacheNodeId |  |
| CurrConnections |  | Количество | Multi | CacheClusterId | Применимо |
| CurrItems | Количество элементов, хранящихся в кэше в настоящее время | Количество | Multi | CacheClusterId, CacheNodeId |  |
| CurrItems |  | Количество | Multi | CacheClusterId |  |
| DatabaseMemoryUsagePercentage |  | Процент | Multi | CacheClusterId, CacheNodeId |  |
| DatabaseMemoryUsagePercentage |  | Процент | Multi | CacheClusterId |  |
| DatabaseMemoryUsagePercentage |  | Процент | Multi | Region |  |
| DecrHits | Количество запросов decrement, полученных кэшем, в которых запрошенный ключ был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| DecrHits |  | Количество | Sum | CacheClusterId |  |
| DecrMisses | Количество запросов decrement, полученных кэшем, в которых запрошенный ключ не был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| DecrMisses |  | Количество | Sum | CacheClusterId |  |
| DeleteHits | Количество запросов delete, полученных кэшем, в которых запрошенный ключ был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| DeleteHits |  | Количество | Sum | CacheClusterId |  |
| DeleteMisses | Количество запросов delete, полученных кэшем, в которых запрошенный ключ не был найден. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| DeleteMisses |  | Количество | Sum | CacheClusterId |  |
| EngineCPUUtilization | Предоставляет данные о загрузке CPU потоком движка Redis | Процент | Multi | CacheClusterId, CacheNodeId |  |
| EngineCPUUtilization |  | Процент | Multi | CacheClusterId |  |
| EvictedUnfetched | Количество действительных элементов, вытесненных из кэша наименее недавно использовавшихся (LRU), к которым ни разу не обращались после установки | Количество | Sum | CacheClusterId, CacheNodeId |  |
| EvictedUnfetched |  | Количество | Sum | CacheClusterId |  |
| Evictions | Количество неистёкших элементов, вытесненных кэшем для освобождения места под новые записи | Количество | Sum | CacheClusterId, CacheNodeId |  |
| Evictions |  | Количество | Sum | CacheClusterId | Применимо |
| ExpiredUnfetched | Количество истёкших элементов, освобождённых из LRU, к которым ни разу не обращались после установки | Количество | Sum | CacheClusterId, CacheNodeId |  |
| ExpiredUnfetched |  | Количество | Sum | CacheClusterId |  |
| FreeableMemory | Объём свободной памяти, доступной на хосте. Вычисляется на основе ОЗУ, буферов и кэша, которые ОС сообщает как освобождаемые. | Байт | Multi | CacheClusterId, CacheNodeId |  |
| FreeableMemory |  | Байт | Multi | CacheClusterId |  |
| GetHits | Количество запросов get, полученных кэшем, в которых запрошенный ключ был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| GetHits |  | Количество | Sum | CacheClusterId |  |
| GetMisses | Количество запросов get, полученных кэшем, в которых запрошенный ключ не был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| GetMisses |  | Количество | Sum | CacheClusterId |  |
| GetTypeCmds | Общее количество команд типа «только чтение». Вычисляется на основе статистики Redis commandstats путём суммирования всех команд типа «только чтение» (get, hget, scard, lrange и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| GetTypeCmds |  | Количество | Sum | CacheClusterId |  |
| HashBasedCmds | Общее количество команд, основанных на хешах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими хешами (hget, hkeys, hvals, hdel и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| HashBasedCmds |  | Количество | Sum | CacheClusterId |  |
| HyperLogLogBasedCmds | Общее количество команд на основе HyperLogLog | Количество | Sum | CacheClusterId, CacheNodeId |  |
| HyperLogLogBasedCmds |  | Количество | Sum | CacheClusterId |  |
| IncrHits | Количество запросов increment, полученных кэшем, в которых запрошенный ключ был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| IncrHits |  | Количество | Sum | CacheClusterId |  |
| IncrMisses | Количество запросов increment, полученных кэшем, в которых запрошенный ключ не был найден | Количество | Sum | CacheClusterId, CacheNodeId |  |
| IncrMisses |  | Количество | Sum | CacheClusterId |  |
| KeyBasedCmds | Общее количество команд, основанных на ключах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими ключами в разных структурах данных (del, expire, rename и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| KeyBasedCmds |  | Количество | Sum | CacheClusterId |  |
| KeysTracked | Количество ключей, отслеживаемых механизмом отслеживания ключей Redis, в процентах от tracking-table-max-keys. Отслеживание ключей помогает кэшированию на стороне клиента и уведомляет клиентов об изменении ключей. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| KeysTracked |  | Количество | Sum | CacheClusterId |  |
| KeysTracked |  | Количество | Sum | Region |  |
| ListBasedCmds | Общее количество команд, основанных на списках. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими списками (lindex, lrange, lpush, ltrim и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| ListBasedCmds |  | Количество | Sum | CacheClusterId |  |
| Network Packets Per Second Allowance Exceeded |  | Количество | Sum | CacheClusterId, CacheNodeId |  |
| Network Packets Per Second Allowance Exceeded |  | Количество | Sum | CacheClusterId |  |
| NetworkBandwidthInAllowanceExceeded |  | Количество | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBandwidthInAllowanceExceeded |  | Количество | Sum | CacheClusterId |  |
| NetworkBandwidthOutAllowanceExceeded |  | Количество | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBandwidthOutAllowanceExceeded |  | Количество | Sum | CacheClusterId |  |
| NetworkBytesIn | Количество байт, прочитанных хостом из сети | Байт | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBytesIn |  | Байт | Sum | CacheClusterId |  |
| NetworkBytesOut | Количество байт, отправленных на всех сетевых интерфейсах экземпляром | Байт | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBytesOut |  | Байт | Sum | CacheClusterId |  |
| NetworkConntrackAllowanceExceeded |  | Количество | Sum | CacheClusterId, CacheNodeId |  |
| NetworkConntrackAllowanceExceeded |  | Количество | Sum | CacheClusterId |  |
| NetworkLinkLocalAllowanceExceeded |  | Количество | Sum | CacheClusterId, CacheNodeId |  |
| NetworkLinkLocalAllowanceExceeded |  | Количество | Sum | CacheClusterId |  |
| NewConnections | Количество новых подключений, полученных кэшем. Вычисляется на основе статистики memcached total_connections путём фиксации изменения total_connections за период времени. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| NewConnections |  | Количество | Sum | CacheClusterId |  |
| NewItems | Количество новых элементов, сохранённых кэшем. Вычисляется на основе статистики memcached total_items путём фиксации изменения total_items за период времени. | Количество | Sum | CacheClusterId, CacheNodeId |  |
| NewItems |  | Количество | Sum | CacheClusterId |  |
| Reclaimed | Количество истёкших элементов, вытесненных кэшем для освобождения места под новые записи | Количество | Sum | CacheClusterId, CacheNodeId |  |
| Reclaimed |  | Количество | Sum | CacheClusterId |  |
| ReplicationBytes | Для узлов в реплицированной конфигурации ReplicationBytes сообщает количество байт, которые первичный узел отправляет всем своим репликам. Эта метрика отражает нагрузку записи на группу репликации. Вычисляется на основе статистики master_repl_offset. | Байт | Multi | CacheClusterId, CacheNodeId |  |
| ReplicationBytes |  | Байт | Multi | CacheClusterId |  |
| ReplicationLag | Эта метрика применима только к узлу, работающему как реплика чтения. Она показывает, насколько (в секундах) реплика отстаёт в применении изменений с первичного узла. | Секунда | Multi | CacheClusterId, CacheNodeId |  |
| ReplicationLag |  | Секунда | Multi | CacheClusterId |  |
| SaveInProgress | Эта двоичная метрика возвращает 1, когда выполняется фоновое сохранение (с ответвлением процесса или без него), и 0 в противном случае. | Количество | Multi | CacheClusterId, CacheNodeId |  |
| SaveInProgress |  | Количество | Multi | CacheClusterId |  |
| SetBasedCmds | Общее количество команд, основанных на множествах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими множествами (scard, sdiff, sadd, sunion и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| SetBasedCmds |  | Количество | Sum | CacheClusterId |  |
| SetTypeCmds | Общее количество команд типа «запись». Вычисляется на основе статистики Redis commandstats путём суммирования всех изменяющих типов команд, работающих с данными (set, hset, sadd, lpop и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| SetTypeCmds |  | Количество | Sum | CacheClusterId |  |
| SlabsMoved | Общее количество перемещённых страниц slab | Количество | Sum | CacheClusterId, CacheNodeId |  |
| SlabsMoved |  | Количество | Sum | CacheClusterId |  |
| SortedSetBasedCmds | Общее количество команд, основанных на упорядоченных множествах. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одним или несколькими упорядоченными множествами (zcount, zrange, zrank, zadd и т. д.). | Количество | Sum | CacheClusterId, CacheNodeId |  |
| SortedSetBasedCmds | Общее количество команд, основанных на строках. Вычисляется на основе статистики Redis commandstats путём суммирования всех команд, работающих с одной или несколькими строками (strlen, setex, setrange и т. д.). | Количество | Sum | CacheClusterId |  |
| StringBasedCmds |  | Количество | Sum | CacheClusterId, CacheNodeId |  |
| StringBasedCmds |  | Количество | Sum | CacheClusterId |  |
| SwapUsage | Объём пространства подкачки, используемого на хосте | Байт | Multi | CacheClusterId, CacheNodeId |  |
| SwapUsage |  | Байт | Multi | CacheClusterId | Применимо |
| TouchHits | Количество ключей, к которым обратились и которым было задано новое время истечения | Количество | Sum | CacheClusterId, CacheNodeId |  |
| TouchHits |  | Количество | Sum | CacheClusterId |  |
| TouchMisses | Количество элементов, к которым обратились, но которые не были найдены | Количество | Sum | CacheClusterId, CacheNodeId |  |
| TouchMisses |  | Количество | Sum | CacheClusterId |  |
| UnusedMemory | Объём памяти, не используемой данными. Вычисляется на основе статистик Memcached limit_maxbytes и bytes путём вычитания bytes из limit_maxbytes. | Байт | Sum | CacheClusterId, CacheNodeId |  |
| UnusedMemory |  | Байт | Sum | CacheClusterId |  |