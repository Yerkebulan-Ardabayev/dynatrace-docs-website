---
title: Мониторинг Amazon Aurora
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-aurora
scraped: 2026-05-12T11:31:12.237731
---

# Мониторинг Amazon Aurora

# Мониторинг Amazon Aurora

* Практическое руководство
* Чтение: 22 мин
* Опубликовано 15 октября 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon Aurora. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

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

Этот сервис отслеживает кластеры Amazon RDS. Уже отслеживаемые ресурсы можно найти на странице обзора AWS в разделе **Cloud services**.

Чтобы вместо этого отслеживать экземпляры RDS, см. Amazon RDS и раздел **RDS** на странице обзора AWS.

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

Основное измерение: `DBClusterIdentifier`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ActiveTransactions | Среднее количество текущих транзакций, выполняемых на экземпляре базы данных Aurora, в секунду | Количество в секунду | Average | DBClusterIdentifier, Role |  |
| ActiveTransactions |  | Количество в секунду | Average | DBClusterIdentifier |  |
| ActiveTransactions |  | Количество в секунду | Average | DatabaseClass, Region |  |
| ActiveTransactions |  | Количество в секунду | Average | EngineName, Region |  |
| ActiveTransactions |  | Количество в секунду | Average | Region |  |
| ActiveTransactions |  | Количество в секунду | Maximum | DBClusterIdentifier, Role |  |
| ActiveTransactions |  | Количество в секунду | Maximum | DBClusterIdentifier |  |
| ActiveTransactions |  | Количество в секунду | Maximum | DatabaseClass, Region |  |
| ActiveTransactions |  | Количество в секунду | Maximum | EngineName, Region |  |
| ActiveTransactions |  | Количество в секунду | Maximum | Region |  |
| AuroraBinlogReplicaLag | Время, на которое реплика кластера БД, работающая на Aurora с совместимостью MySQL, отстаёт от исходного кластера БД | Секунда | Multi | DBClusterIdentifier, Role |  |
| AuroraBinlogReplicaLag |  | Секунда | Multi | DBClusterIdentifier |  |
| AuroraBinlogReplicaLag |  | Секунда | Multi | DatabaseClass, Region |  |
| AuroraBinlogReplicaLag |  | Секунда | Multi | EngineName, Region |  |
| AuroraBinlogReplicaLag |  | Секунда | Multi | Region |  |
| AuroraReplicaLagMaximum | Максимальная величина отставания между первичным экземпляром и каждым экземпляром БД Aurora в кластере БД | Миллисекунда | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLagMaximum |  | Миллисекунда | Average | DBClusterIdentifier |  |
| AuroraReplicaLagMaximum |  | Миллисекунда | Average | DatabaseClass, Region |  |
| AuroraReplicaLagMaximum |  | Миллисекунда | Average | EngineName, Region |  |
| AuroraReplicaLagMaximum |  | Миллисекунда | Average | Region |  |
| AuroraReplicaLagMinimum |  | Миллисекунда | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLagMinimum |  | Миллисекунда | Average | DBClusterIdentifier |  |
| AuroraReplicaLagMinimum |  | Миллисекунда | Average | DatabaseClass, Region |  |
| AuroraReplicaLagMinimum |  | Миллисекунда | Average | EngineName, Region |  |
| AuroraReplicaLagMinimum |  | Миллисекунда | Average | Region |  |
| AuroraReplicaLag | Для реплики Aurora: величина отставания при репликации обновлений с первичного экземпляра | Миллисекунда | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLag |  | Миллисекунда | Average | DBClusterIdentifier |  |
| AuroraReplicaLag |  | Миллисекунда | Average | DatabaseClass, Region |  |
| AuroraReplicaLag |  | Миллисекунда | Average | EngineName, Region |  |
| AuroraReplicaLag |  | Миллисекунда | Average | Region |  |
| BacktrackChangeRecordsCreationRate | Количество записей изменений backtrack, созданных за 5 минут для вашего кластера БД | Количество | Sum | DBClusterIdentifier, Role |  |
| BacktrackChangeRecordsCreationRate |  | Количество | Sum | DBClusterIdentifier |  |
| BacktrackChangeRecordsCreationRate |  | Количество | Sum | DatabaseClass, Region |  |
| BacktrackChangeRecordsCreationRate |  | Количество | Sum | EngineName, Region |  |
| BacktrackChangeRecordsCreationRate |  | Количество | Sum | Region |  |
| BacktrackChangeRecordsStored | Количество записей изменений backtrack, использованных вашим кластером БД | Количество | Sum | DBClusterIdentifier, Role |  |
| BacktrackChangeRecordsStored |  | Количество | Sum | DBClusterIdentifier |  |
| BacktrackChangeRecordsStored |  | Количество | Sum | DatabaseClass, Region |  |
| BacktrackChangeRecordsStored |  | Количество | Sum | EngineName, Region |  |
| BacktrackChangeRecordsStored |  | Количество | Sum | Region |  |
| BacktrackWindowActual | Разница между целевым окном backtrack и фактическим окном backtrack | Количество | Sum | DBClusterIdentifier, Role |  |
| BacktrackWindowActual |  | Количество | Sum | DBClusterIdentifier |  |
| BacktrackWindowActual |  | Количество | Sum | DatabaseClass, Region |  |
| BacktrackWindowActual |  | Количество | Sum | EngineName, Region |  |
| BacktrackWindowActual |  | Количество | Sum | Region |  |
| BacktrackWindowAlert | Количество случаев, когда фактическое окно backtrack меньше целевого окна backtrack за заданный период времени | Количество | Sum | DBClusterIdentifier, Role |  |
| BacktrackWindowAlert |  | Количество | Sum | DBClusterIdentifier |  |
| BacktrackWindowAlert |  | Количество | Sum | DatabaseClass, Region |  |
| BacktrackWindowAlert |  | Количество | Sum | EngineName, Region |  |
| BacktrackWindowAlert |  | Количество | Sum | Region |  |
| BinLogDiskUsage | Объём дискового пространства, занятого двоичными журналами на первичном экземпляре | Байт | Average | DBClusterIdentifier, Role |  |
| BinLogDiskUsage |  | Байт | Average | DBClusterIdentifier |  |
| BinLogDiskUsage |  | Байт | Average | DatabaseClass, Region |  |
| BinLogDiskUsage |  | Байт | Average | EngineName, Region |  |
| BinLogDiskUsage |  | Байт | Average | Region |  |
| BlockedTransactions | Среднее количество транзакций в базе данных, заблокированных в секунду | Количество в секунду | Average | DBClusterIdentifier, Role |  |
| BlockedTransactions |  | Количество в секунду | Average | DBClusterIdentifier |  |
| BlockedTransactions |  | Количество в секунду | Average | DatabaseClass, Region |  |
| BlockedTransactions |  | Количество в секунду | Average | EngineName, Region |  |
| BlockedTransactions |  | Количество в секунду | Average | Region |  |
| BlockedTransactions |  | Количество в секунду | Maximum | DBClusterIdentifier, Role |  |
| BlockedTransactions |  | Количество в секунду | Maximum | DBClusterIdentifier |  |
| BlockedTransactions |  | Количество в секунду | Maximum | DatabaseClass, Region |  |
| BlockedTransactions |  | Количество в секунду | Maximum | EngineName, Region |  |
| BlockedTransactions |  | Количество в секунду | Maximum | Region |  |
| BufferCacheHitRatio | Процент запросов, обслуженных буферным кэшем | Процент | Average | DBClusterIdentifier, Role |  |
| BufferCacheHitRatio |  | Процент | Average | DBClusterIdentifier |  |
| BufferCacheHitRatio |  | Процент | Average | DatabaseClass, Region |  |
| BufferCacheHitRatio |  | Процент | Average | EngineName, Region |  |
| BufferCacheHitRatio |  | Процент | Average | Region |  |
| CPUCreditBalance | Количество кредитов CPU, накопленных экземпляром; регистрируется с интервалом в 5 минут. Эта метрика применима только к экземплярам `db.t2.small` и `db.t2.medium`. С помощью этой метрики можно определить, как долго экземпляр БД Aurora MySQL может работать в режиме всплеска сверх базового уровня производительности при заданной интенсивности. | Количество | Average | DBClusterIdentifier, Role |  |
| CPUCreditBalance |  | Количество | Average | DBClusterIdentifier |  |
| CPUCreditBalance |  | Количество | Average | DatabaseClass, Region |  |
| CPUCreditBalance |  | Количество | Average | EngineName, Region |  |
| CPUCreditBalance |  | Количество | Average | Region |  |
| CPUCreditUsage | Количество кредитов CPU, израсходованных за указанный период; регистрируется с интервалом в 5 минут. Эта метрика применима только к экземплярам `db.t2.small` и `db.t2.medium`. Эта метрика измеряет количество времени, в течение которого физические CPU использовались для обработки инструкций виртуальными CPU, выделенными экземпляру БД Aurora MySQL. | Количество | Average | DBClusterIdentifier, Role |  |
| CPUCreditUsage |  | Количество | Average | DBClusterIdentifier |  |
| CPUCreditUsage |  | Количество | Average | DatabaseClass, Region |  |
| CPUCreditUsage |  | Количество | Average | EngineName, Region |  |
| CPUCreditUsage |  | Количество | Average | Region |  |
| CPUUtilization | Процент CPU, используемого экземпляром БД Aurora | Процент | Average | DBClusterIdentifier, Role |  |
| CPUUtilization |  | Процент | Average | DBClusterIdentifier |  |
| CPUUtilization |  | Процент | Average | DatabaseClass, Region |  |
| CPUUtilization |  | Процент | Average | EngineName, Region |  |
| CPUUtilization |  | Процент | Average | Region |  |
| CPUUtilization |  | Процент | Maximum | DBClusterIdentifier, Role |  |
| CPUUtilization |  | Процент | Maximum | DBClusterIdentifier |  |
| CPUUtilization |  | Процент | Maximum | DatabaseClass, Region |  |
| CPUUtilization |  | Процент | Maximum | EngineName, Region |  |
| CPUUtilization |  | Процент | Maximum | Region |  |
| CommitLatency | Задержка операций фиксации | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| CommitLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| CommitLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| CommitLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| CommitLatency |  | Миллисекунда | Multi | Region |  |
| CommitThroughput | Среднее количество операций фиксации в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| CommitThroughput |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| CommitThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| CommitThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| CommitThroughput |  | Количество в секунду | Multi | Region |  |
| DDLLatency | Задержка запросов языка определения данных (DDL), например запросов create, alter и drop | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| DDLLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| DDLLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| DDLLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| DDLLatency |  | Миллисекунда | Multi | Region |  |
| DDLThroughput | Среднее количество запросов DDL в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| DDLThroughput |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| DDLThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| DDLThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| DDLThroughput |  | Количество в секунду | Multi | Region |  |
| DMLLatency | Задержка операций вставки, обновления и удаления | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| DMLLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| DMLLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| DMLLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| DMLLatency |  | Миллисекунда | Multi | Region |  |
| DMLThroughput | Среднее количество операций вставки, обновления и удаления в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| DMLThroughput |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| DMLThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| DMLThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| DMLThroughput |  | Количество в секунду | Multi | Region |  |
| DatabaseConnections | Количество подключений к экземпляру БД Aurora | Количество | Average | DBClusterIdentifier, Role |  |
| DatabaseConnections |  | Количество | Average | DBClusterIdentifier |  |
| DatabaseConnections |  | Количество | Average | DatabaseClass, Region |  |
| DatabaseConnections |  | Количество | Average | EngineName, Region |  |
| DatabaseConnections |  | Количество | Average | Region |  |
| DatabaseConnections |  | Количество | Maximum | DBClusterIdentifier, Role |  |
| DatabaseConnections |  | Количество | Maximum | DBClusterIdentifier |  |
| DatabaseConnections |  | Количество | Maximum | DatabaseClass, Region |  |
| DatabaseConnections |  | Количество | Maximum | EngineName, Region |  |
| DatabaseConnections |  | Количество | Maximum | Region |  |
| Deadlocks | Среднее количество взаимоблокировок в базе данных в секунду | Количество в секунду | Average | DBClusterIdentifier, Role |  |
| Deadlocks |  | Количество в секунду | Average | DBClusterIdentifier |  |
| Deadlocks |  | Количество в секунду | Average | DatabaseClass, Region |  |
| Deadlocks |  | Количество в секунду | Average | EngineName, Region |  |
| Deadlocks |  | Количество в секунду | Average | Region |  |
| Deadlocks |  | Количество в секунду | Maximum | DBClusterIdentifier, Role |  |
| Deadlocks |  | Количество в секунду | Maximum | DBClusterIdentifier |  |
| Deadlocks |  | Количество в секунду | Maximum | DatabaseClass, Region |  |
| Deadlocks |  | Количество в секунду | Maximum | EngineName, Region |  |
| Deadlocks |  | Количество в секунду | Maximum | Region |  |
| DeleteLatency | Задержка запросов удаления | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| DeleteLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| DeleteLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| DeleteLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| DeleteLatency |  | Миллисекунда | Multi | Region |  |
| DeleteThroughput | Среднее количество запросов удаления в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| DeleteThroughput |  | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| DeleteThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| DeleteThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| DeleteThroughput |  | Количество в секунду | Multi | Region |  |
| DiskQueueDepth | Количество незавершённых запросов чтения/записи, ожидающих доступа к диску | Количество | Multi | DBClusterIdentifier, Role |  |
| DiskQueueDepth |  | Количество | Multi | DBClusterIdentifier |  |
| DiskQueueDepth |  | Количество | Multi | DatabaseClass, Region |  |
| DiskQueueDepth |  | Количество | Multi | EngineName, Region |  |
| DiskQueueDepth |  | Количество | Multi | Region |  |
| EngineUptime | Время работы экземпляра | Секунда | Average | DBClusterIdentifier, Role |  |
| EngineUptime |  | Секунда | Average | DBClusterIdentifier |  |
| EngineUptime |  | Секунда | Average | DatabaseClass, Region |  |
| EngineUptime |  | Секунда | Average | EngineName, Region |  |
| EngineUptime |  | Секунда | Average | Region |  |
| FreeLocalStorage | Объём локального хранилища, доступного для каждого экземпляра БД. | Байт | Average | DBClusterIdentifier, Role |  |
| FreeLocalStorage |  | Байт | Average | DBClusterIdentifier |  |
| FreeLocalStorage |  | Байт | Average | DatabaseClass, Region |  |
| FreeLocalStorage |  | Байт | Average | EngineName, Region |  |
| FreeLocalStorage |  | Байт | Average | Region |  |
| FreeableMemory | Объём доступной оперативной памяти | Байт | Average | DBClusterIdentifier, Role |  |
| FreeableMemory |  | Байт | Average | DBClusterIdentifier |  |
| FreeableMemory |  | Байт | Average | DatabaseClass, Region |  |
| FreeableMemory |  | Байт | Average | EngineName, Region |  |
| FreeableMemory |  | Байт | Average | Region |  |
| InsertLatency | Задержка запросов вставки | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| InsertLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| InsertLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| InsertLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| InsertLatency |  | Миллисекунда | Multi | Region |  |
| InsertThroughput | Среднее количество запросов вставки в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| InsertThroughput |  | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| InsertThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| InsertThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| InsertThroughput |  | Количество в секунду | Multi | Region |  |
| LoginFailures | Среднее количество неудачных попыток входа в секунду | Количество в секунду | Average | DBClusterIdentifier, Role |  |
| LoginFailures |  | Количество в секунду | Average | DBClusterIdentifier |  |
| LoginFailures |  | Количество в секунду | Average | DatabaseClass, Region |  |
| LoginFailures |  | Количество в секунду | Average | EngineName, Region |  |
| LoginFailures |  | Количество в секунду | Average | Region |  |
| LoginFailures |  | Количество в секунду | Maximum | DBClusterIdentifier, Role |  |
| LoginFailures |  | Количество в секунду | Maximum | DBClusterIdentifier |  |
| LoginFailures |  | Количество в секунду | Maximum | DatabaseClass, Region |  |
| LoginFailures |  | Количество в секунду | Maximum | EngineName, Region |  |
| LoginFailures |  | Количество в секунду | Maximum | Region |  |
| MaximumUsedTransactionIDs | Возраст самого старого неочищенного идентификатора транзакции, в транзакциях. Если это значение достигает `2`,`146`,`483`,`648` (2^31 - 1 000 000), база данных принудительно переводится в режим только для чтения во избежание зацикливания идентификаторов транзакций. | Количество | Average | DBClusterIdentifier, Role |  |
| MaximumUsedTransactionIDs |  | Количество | Average | DBClusterIdentifier |  |
| MaximumUsedTransactionIDs |  | Количество | Average | DatabaseClass, Region |  |
| MaximumUsedTransactionIDs |  | Количество | Average | EngineName, Region |  |
| MaximumUsedTransactionIDs |  | Количество | Average | Region |  |
| NetworkReceiveThroughput | Объём сетевой пропускной способности, полученной от клиентов каждым экземпляром в кластере БД Aurora MySQL. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД Aurora и томом кластера. | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | DBClusterIdentifier |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | DatabaseClass, Region |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | EngineName, Region |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | Region |  |
| NetworkThroughput | Объём сетевой пропускной способности, как полученной от клиентов, так и переданной им каждым экземпляром в кластере БД Aurora MySQL. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД и томом кластера. | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| NetworkThroughput |  | Байт в секунду | Multi | DBClusterIdentifier |  |
| NetworkThroughput |  | Байт в секунду | Multi | DatabaseClass, Region |  |
| NetworkThroughput |  | Байт в секунду | Multi | EngineName, Region |  |
| NetworkThroughput |  | Байт в секунду | Multi | Region |  |
| NetworkTransmitThroughput | Объём сетевой пропускной способности, отправленной клиентам каждым экземпляром в кластере БД Aurora. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД и томом кластера. | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | DBClusterIdentifier |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | DatabaseClass, Region |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | EngineName, Region |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | Region |  |
| Queries | Среднее количество запросов, выполненных в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| Queries |  | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| Queries |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| Queries |  | Количество в секунду | Multi | EngineName, Region |  |
| Queries |  | Количество в секунду | Multi | Region |  |
| RDSToAuroraPostgreSQLReplicaLag | Отставание при репликации обновлений с первичного экземпляра RDS PostgreSQL на другие узлы в кластере | Секунда | Multi | DBClusterIdentifier, Role |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Секунда | Multi | DBClusterIdentifier |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Секунда | Multi | DatabaseClass, Region |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Секунда | Multi | EngineName, Region |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Секунда | Multi | Region |  |
| ReadIOPS | Среднее количество дисковых операций ввода-вывода в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| ReadIOPS |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| ReadIOPS |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| ReadIOPS |  | Количество в секунду | Multi | EngineName, Region |  |
| ReadIOPS |  | Количество в секунду | Multi | Region |  |
| ReadLatency | Среднее время, затрачиваемое на одну дисковую операцию ввода-вывода | Секунда | Multi | DBClusterIdentifier, Role |  |
| ReadLatency |  | Секунда | Multi | DBClusterIdentifier |  |
| ReadLatency |  | Секунда | Multi | DatabaseClass, Region |  |
| ReadLatency |  | Секунда | Multi | EngineName, Region |  |
| ReadLatency |  | Секунда | Multi | Region |  |
| ReadThroughput | Среднее количество байт, считываемых с диска в секунду | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| ReadThroughput |  | Байт в секунду | Multi | DBClusterIdentifier |  |
| ReadThroughput |  | Байт в секунду | Multi | DatabaseClass, Region |  |
| ReadThroughput |  | Байт в секунду | Multi | EngineName, Region |  |
| ReadThroughput |  | Байт в секунду | Multi | Region |  |
| ResultSetCacheHitRatio | Процент запросов, обслуженных кэшем результирующих наборов | Процент | Average | DBClusterIdentifier, Role |  |
| ResultSetCacheHitRatio |  | Процент | Average | DBClusterIdentifier |  |
| ResultSetCacheHitRatio |  | Процент | Average | DatabaseClass, Region |  |
| ResultSetCacheHitRatio |  | Процент | Average | EngineName, Region |  |
| ResultSetCacheHitRatio |  | Процент | Average | Region |  |
| ResultSetCacheHitRatio |  | Процент | Maximum | DBClusterIdentifier, Role |  |
| ResultSetCacheHitRatio |  | Процент | Maximum | DBClusterIdentifier |  |
| ResultSetCacheHitRatio |  | Процент | Maximum | DatabaseClass, Region |  |
| ResultSetCacheHitRatio |  | Процент | Maximum | EngineName, Region |  |
| ResultSetCacheHitRatio |  | Процент | Maximum | Region |  |
| SelectLatency | Задержка запросов выборки | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| SelectLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| SelectLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| SelectLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| SelectLatency |  | Миллисекунда | Multi | Region |  |
| SelectThroughput | Среднее количество запросов выборки в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| SelectThroughput |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| SelectThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| SelectThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| SelectThroughput |  | Количество в секунду | Multi | Region |  |
| SwapUsage | Объём пространства подкачки, используемого на экземпляре БД Aurora PostgreSQL | Байт | Multi | DBClusterIdentifier, Role |  |
| SwapUsage |  | Байт | Multi | DBClusterIdentifier |  |
| SwapUsage |  | Байт | Multi | DatabaseClass, Region |  |
| SwapUsage |  | Байт | Multi | EngineName, Region |  |
| SwapUsage |  | Байт | Multi | Region |  |
| TransactionLogsDiskUsage | Объём дискового пространства, занятого журналами транзакций на экземпляре БД Aurora PostgreSQL. Эта метрика формируется только тогда, когда Aurora PostgreSQL использует логическую репликацию или AWS Database Migration Service. По умолчанию Aurora PostgreSQL использует записи журнала, а не журналы транзакций. Когда журналы транзакций не используются, значение этой метрики равно -1. | Байт | Multi | DBClusterIdentifier, Role |  |
| TransactionLogsDiskUsage |  | Байт | Multi | DBClusterIdentifier |  |
| TransactionLogsDiskUsage |  | Байт | Multi | DatabaseClass, Region |  |
| TransactionLogsDiskUsage |  | Байт | Multi | EngineName, Region |  |
| TransactionLogsDiskUsage |  | Байт | Multi | Region |  |
| UpdateLatency | Задержка запросов обновления | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| UpdateLatency |  | Миллисекунда | Multi | DBClusterIdentifier |  |
| UpdateLatency |  | Миллисекунда | Multi | DatabaseClass, Region |  |
| UpdateLatency |  | Миллисекунда | Multi | EngineName, Region |  |
| UpdateLatency |  | Миллисекунда | Multi | Region |  |
| UpdateThroughput | Среднее количество запросов обновления в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| UpdateThroughput |  | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| UpdateThroughput |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| UpdateThroughput |  | Количество в секунду | Multi | EngineName, Region |  |
| UpdateThroughput |  | Количество в секунду | Multi | Region |  |
| VolumeBytesUsed | Объём хранилища, используемого вашим экземпляром БД Aurora. Это значение влияет на стоимость кластера БД Aurora. | Байт | Multi | DBClusterIdentifier, Role |  |
| VolumeBytesUsed |  | Байт | Multi | DBClusterIdentifier |  |
| VolumeBytesUsed |  | Байт | Multi | DatabaseClass, Region |  |
| VolumeBytesUsed |  | Байт | Multi | EngineName, Region |  |
| VolumeBytesUsed |  | Байт | Multi | Region |  |
| VolumeReadIOPs | Количество оплачиваемых операций ввода-вывода чтения из тома кластера за 5-минутный интервал | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| VolumeReadIOPs |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| VolumeReadIOPs |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| VolumeReadIOPs |  | Количество в секунду | Multi | EngineName, Region |  |
| VolumeReadIOPs |  | Количество в секунду | Multi | Region |  |
| VolumeWriteIOPs | Количество дисковых операций ввода-вывода записи в том кластера; регистрируется с интервалом в 5 минут | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| VolumeWriteIOPs |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| VolumeWriteIOPs |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| VolumeWriteIOPs |  | Количество в секунду | Multi | EngineName, Region |  |
| VolumeWriteIOPs |  | Количество в секунду | Multi | Region |  |
| WriteIOPS | Среднее количество дисковых операций ввода-вывода в секунду | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| WriteIOPS |  | Количество в секунду | Multi | DBClusterIdentifier |  |
| WriteIOPS |  | Количество в секунду | Multi | DatabaseClass, Region |  |
| WriteIOPS |  | Количество в секунду | Multi | EngineName, Region |  |
| WriteIOPS |  | Количество в секунду | Multi | Region |  |
| WriteLatency | Среднее время, затрачиваемое на одну дисковую операцию ввода-вывода | Секунда | Multi | DBClusterIdentifier, Role |  |
| WriteLatency |  | Секунда | Multi | DBClusterIdentifier |  |
| WriteLatency |  | Секунда | Multi | DatabaseClass, Region |  |
| WriteLatency |  | Секунда | Multi | EngineName, Region |  |
| WriteLatency |  | Секунда | Multi | Region |  |
| WriteThroughput | Среднее количество байт, записанных на диск | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| WriteThroughput |  | Байт в секунду | Multi | DBClusterIdentifier |  |
| WriteThroughput |  | Байт в секунду | Multi | DatabaseClass, Region |  |
| WriteThroughput |  | Байт в секунду | Multi | EngineName, Region |  |
| WriteThroughput |  | Байт в секунду | Multi | Region |  |