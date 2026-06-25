---
title: Мониторинг Amazon Neptune
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-neptune
scraped: 2026-05-12T11:30:05.660900
---

# Мониторинг Amazon Neptune

# Мониторинг Amazon Neptune

* Практическое руководство
* Чтение: 11 мин
* Опубликовано 6 июля 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon Neptune. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

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

После добавления сервиса в мониторинг предустановленный дашборд со всеми рекомендуемыми метриками автоматически появляется на вашей странице **Dashboards**. Чтобы найти конкретные дашборды, отфильтруйте по **Preset**, а затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

AWS presets

Для уже отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд отобразился на странице **Dashboards**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS, затем нажмите **Save**.

Вы не можете вносить изменения непосредственно в предустановленный дашборд, но можете клонировать его и редактировать. Чтобы клонировать дашборд, откройте меню обзора (**…**) и выберите **Clone**.

Чтобы убрать дашборд со страницы дашбордов, его можно скрыть. Чтобы скрыть дашборд, откройте меню обзора (**…**) и выберите **Hide**.

Скрытие дашборда не затрагивает других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Clone hide AWS

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

![Neptune](https://dt-cdn.net/images/dashboard-27-2686-043659e494.png)

Neptune

## Доступные метрики

Основное измерение: `DBClusterIdentifier`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| BackupRetentionPeriodStorageUsed | Общий объём хранилища резервных копий в байтах, используемого для поддержки окна хранения резервных копий кластера БД Neptune | Байт | Multi | DBClusterIdentifier |  |
| BackupRetentionPeriodStorageUsed |  | Байт | Multi | Region, EngineName |  |
| CPUUtilization | Процент загрузки CPU | Процент | Multi | DBClusterIdentifier | Применимо |
| CPUUtilization |  | Процент | Multi | DBClusterIdentifier | Применимо |
| CPUUtilization |  | Процент | Multi | Region | Применимо |
| CPUUtilization |  | Процент | Multi | Region, DBInstanceIdentifier | Применимо |
| CPUUtilization |  | Процент | Multi | Region, DatabaseClass | Применимо |
| CPUUtilization |  | Процент | Multi | Region, EngineName | Применимо |
| ClusterReplicaLag | Для реплики чтения: величина отставания при репликации обновлений с первичного экземпляра, в миллисекундах | Миллисекунда | Multi | DBClusterIdentifier | Применимо |
| ClusterReplicaLag |  | Миллисекунда | Multi | DBClusterIdentifier, Role | Применимо |
| ClusterReplicaLag |  | Миллисекунда | Multi | Region | Применимо |
| ClusterReplicaLag |  | Миллисекунда | Multi | Region, DBInstanceIdentifier | Применимо |
| ClusterReplicaLag |  | Миллисекунда | Multi | Region, DatabaseClass | Применимо |
| ClusterReplicaLag |  | Миллисекунда | Multi | Region, EngineName | Применимо |
| ClusterReplicaLagMaximum | Максимальная величина отставания между первичным экземпляром и каждым экземпляром БД Neptune в кластере БД, в миллисекундах | Миллисекунда | Multi | DBClusterIdentifier |  |
| ClusterReplicaLagMaximum |  | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| ClusterReplicaLagMaximum |  | Миллисекунда | Multi | Region |  |
| ClusterReplicaLagMaximum |  | Миллисекунда | Multi | Region, DBInstanceIdentifier |  |
| ClusterReplicaLagMaximum |  | Миллисекунда | Multi | Region, DatabaseClass |  |
| ClusterReplicaLagMaximum |  | Миллисекунда | Multi | Region, EngineName |  |
| ClusterReplicaLagMinimum | Минимальная величина отставания между первичным экземпляром и каждым экземпляром БД Neptune в кластере БД, в миллисекундах | Миллисекунда | Multi | DBClusterIdentifier |  |
| ClusterReplicaLagMinimum |  | Миллисекунда | Multi | DBClusterIdentifier, Role |  |
| ClusterReplicaLagMinimum |  | Миллисекунда | Multi | Region |  |
| ClusterReplicaLagMinimum |  | Миллисекунда | Multi | Region, DBInstanceIdentifier |  |
| ClusterReplicaLagMinimum |  | Миллисекунда | Multi | Region, DatabaseClass |  |
| ClusterReplicaLagMinimum |  | Миллисекунда | Multi | Region, EngineName |  |
| EngineUptime | Время работы экземпляра, в секундах | Секунда | Multi | DBClusterIdentifier | Применимо |
| EngineUptime |  | Секунда | Multi | DBClusterIdentifier, Role | Применимо |
| EngineUptime |  | Секунда | Multi | Region | Применимо |
| EngineUptime |  | Секунда | Multi | Region, DBInstanceIdentifier | Применимо |
| EngineUptime |  | Секунда | Multi | Region, DatabaseClass | Применимо |
| EngineUptime |  | Секунда | Multi | Region, EngineName | Применимо |
| FreeableMemory | Объём доступной оперативной памяти, в байтах | Байт | Multi | DBClusterIdentifier | Применимо |
| FreeableMemory |  | Байт | Multi | DBClusterIdentifier, Role | Применимо |
| FreeableMemory |  | Байт | Multi | Region | Применимо |
| FreeableMemory |  | Байт | Multi | Region, DBInstanceIdentifier | Применимо |
| FreeableMemory |  | Байт | Multi | Region, DatabaseClass | Применимо |
| FreeableMemory |  | Байт | Multi | Region, EngineName | Применимо |
| GremlinRequestsPerSec | Количество запросов в секунду к движку Gremlin | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| GremlinRequestsPerSec |  | Количество в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| GremlinRequestsPerSec |  | Количество в секунду | Multi | Region | Применимо |
| GremlinRequestsPerSec |  | Количество в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| GremlinRequestsPerSec |  | Количество в секунду | Multi | Region, DatabaseClass | Применимо |
| GremlinRequestsPerSec |  | Количество в секунду | Multi | Region, EngineName | Применимо |
| GremlinWebSocketOpenConnections | Количество открытых подключений WebSocket к Neptune | Количество в секунду | Multi | DBClusterIdentifier |  |
| GremlinWebSocketOpenConnections |  | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| GremlinWebSocketOpenConnections |  | Количество в секунду | Multi | Region |  |
| GremlinWebSocketOpenConnections |  | Количество в секунду | Multi | Region, DBInstanceIdentifier |  |
| GremlinWebSocketOpenConnections |  | Количество в секунду | Multi | Region, DatabaseClass |  |
| GremlinWebSocketOpenConnections |  | Количество в секунду | Multi | Region, EngineName |  |
| LoaderRequestsPerSec | Количество запросов загрузчика в секунду | Количество в секунду | Multi | DBClusterIdentifier |  |
| LoaderRequestsPerSec |  | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| LoaderRequestsPerSec |  | Количество в секунду | Multi | Region |  |
| LoaderRequestsPerSec |  | Количество в секунду | Multi | Region, DBInstanceIdentifier |  |
| LoaderRequestsPerSec |  | Количество в секунду | Multi | Region, DatabaseClass |  |
| LoaderRequestsPerSec |  | Количество в секунду | Multi | Region, EngineName |  |
| MainRequestQueuePendingRequests | Количество запросов, ожидающих выполнения во входной очереди. Neptune начинает регулировать запросы, когда они превышают максимальную ёмкость очереди | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| MainRequestQueuePendingRequests |  | Количество в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| MainRequestQueuePendingRequests |  | Количество в секунду | Multi | Region | Применимо |
| MainRequestQueuePendingRequests |  | Количество в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| MainRequestQueuePendingRequests |  | Количество в секунду | Multi | Region, DatabaseClass | Применимо |
| MainRequestQueuePendingRequests |  | Количество в секунду | Multi | Region, EngineName | Применимо |
| NetworkReceiveThroughput | Входящий (принимаемый) сетевой трафик на экземпляре БД, включая как трафик клиентской базы данных, так и трафик Neptune, используемый для мониторинга и репликации, в байтах/секунду | Байт в секунду | Multi | DBClusterIdentifier |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | Region |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | Region, DBInstanceIdentifier |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | Region, DatabaseClass |  |
| NetworkReceiveThroughput |  | Байт в секунду | Multi | Region, EngineName |  |
| NetworkThroughput | Объём сетевой пропускной способности, как полученной от клиентов, так и переданной им каждым экземпляром в кластере БД Neptune, в байтах в секунду. Эта пропускная способность не включает сетевой трафик между экземплярами в кластере БД и томом кластера. | Байт в секунду | Multi | DBClusterIdentifier | Применимо |
| NetworkThroughput |  | Байт в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| NetworkThroughput |  | Байт в секунду | Multi | Region | Применимо |
| NetworkThroughput |  | Байт в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| NetworkThroughput |  | Байт в секунду | Multi | Region, DatabaseClass | Применимо |
| NetworkThroughput |  | Байт в секунду | Multi | Region, EngineName | Применимо |
| NetworkTransmitThroughput | Исходящий (передаваемый) сетевой трафик на экземпляре БД, включая как трафик клиентской базы данных, так и трафик Neptune, используемый для мониторинга и репликации, в байтах/секунду | Байт в секунду | Multi | DBClusterIdentifier |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | DBClusterIdentifier, Role |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | Region |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | Region, DBInstanceIdentifier |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | Region, DatabaseClass |  |
| NetworkTransmitThroughput |  | Байт в секунду | Multi | Region, EngineName |  |
| NumTxCommitted | Количество транзакций, успешно зафиксированных в секунду | Количество в секунду | Multi | DBClusterIdentifier |  |
| NumTxCommitted |  | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| NumTxCommitted |  | Количество в секунду | Multi | Region |  |
| NumTxCommitted |  | Количество в секунду | Multi | Region, DBInstanceIdentifier |  |
| NumTxCommitted |  | Количество в секунду | Multi | Region, DatabaseClass |  |
| NumTxCommitted |  | Количество в секунду | Multi | Region, EngineName |  |
| NumTxOpened | Количество транзакций, открытых на сервере в секунду | Количество в секунду | Multi | DBClusterIdentifier |  |
| NumTxOpened |  | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| NumTxOpened |  | Количество в секунду | Multi | Region |  |
| NumTxOpened |  | Количество в секунду | Multi | Region, DBInstanceIdentifier |  |
| NumTxOpened |  | Количество в секунду | Multi | Region, DatabaseClass |  |
| NumTxOpened |  | Количество в секунду | Multi | Region, EngineName |  |
| NumTxRolledBack | Количество транзакций в секунду, откатанных на сервере из-за ошибок | Количество в секунду | Multi | DBClusterIdentifier |  |
| NumTxRolledBack |  | Количество в секунду | Multi | DBClusterIdentifier, Role |  |
| NumTxRolledBack |  | Количество в секунду | Multi | Region |  |
| NumTxRolledBack |  | Количество в секунду | Multi | Region, DBInstanceIdentifier |  |
| NumTxRolledBack |  | Количество в секунду | Multi | Region, DatabaseClass |  |
| NumTxRolledBack |  | Количество в секунду | Multi | Region, EngineName |  |
| SnapshotStorageUsed | Общий объём хранилища резервных копий, занятого всеми снимками для кластера БД Neptune за пределами окна хранения резервных копий, в байтах | Байт | Multi | DBClusterIdentifier |  |
| SnapshotStorageUsed |  | Байт | Multi | Region, EngineName |  |
| SparqlRequestsPerSec | Количество запросов в секунду к движку SPARQL | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| SparqlRequestsPerSec |  | Количество в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| SparqlRequestsPerSec |  | Количество в секунду | Multi | Region | Применимо |
| SparqlRequestsPerSec |  | Количество в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| SparqlRequestsPerSec |  | Количество в секунду | Multi | Region, DatabaseClass | Применимо |
| SparqlRequestsPerSec |  | Количество в секунду | Multi | Region, EngineName | Применимо |
| TotalBackupStorageBilled | Общий объём хранилища резервных копий, за который начисляется плата для данного кластера БД Neptune, в байтах | Байт | Multi | DBClusterIdentifier |  |
| TotalBackupStorageBilled |  | Байт | Multi | Region, EngineName |  |
| TotalClientErrorsPerSec | Общее количество запросов в секунду, завершившихся ошибкой из-за проблем на стороне клиента | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| TotalClientErrorsPerSec |  | Количество в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| TotalClientErrorsPerSec |  | Количество в секунду | Multi | Region | Применимо |
| TotalClientErrorsPerSec |  | Количество в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| TotalClientErrorsPerSec |  | Количество в секунду | Multi | Region, DatabaseClass | Применимо |
| TotalClientErrorsPerSec |  | Количество в секунду | Multi | Region, EngineName | Применимо |
| TotalRequestsPerSec | Общее количество запросов в секунду к серверу из всех источников | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| TotalRequestsPerSec |  | Количество в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| TotalRequestsPerSec |  | Количество в секунду | Multi | Region | Применимо |
| TotalRequestsPerSec |  | Количество в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| TotalRequestsPerSec |  | Количество в секунду | Multi | Region, DatabaseClass | Применимо |
| TotalRequestsPerSec |  | Количество в секунду | Multi | Region, EngineName | Применимо |
| TotalServerErrorsPerSec | Общее количество запросов в секунду, завершившихся ошибкой на сервере из-за внутренних сбоев | Количество в секунду | Multi | DBClusterIdentifier | Применимо |
| TotalServerErrorsPerSec |  | Количество в секунду | Multi | DBClusterIdentifier, Role | Применимо |
| TotalServerErrorsPerSec |  | Количество в секунду | Multi | Region | Применимо |
| TotalServerErrorsPerSec |  | Количество в секунду | Multi | Region, DBInstanceIdentifier | Применимо |
| TotalServerErrorsPerSec |  | Количество в секунду | Multi | Region, DatabaseClass | Применимо |
| TotalServerErrorsPerSec |  | Количество в секунду | Multi | Region, EngineName | Применимо |
| VolumeBytesUsed | Общий объём хранилища, выделенного вашему кластеру БД Neptune, в байтах. Это объём хранилища, за который начисляется плата. Это максимальный объём хранилища, выделенный вашему кластеру БД в любой момент его существования, а не объём, который вы используете в настоящее время. | Байт | Multi | DBClusterIdentifier | Применимо |
| VolumeBytesUsed | Объём хранилища, используемого вашим экземпляром БД Neptune, в байтах. | Байт | Multi | Region, EngineName | Применимо |
| VolumeBytesLeftTotal | Оставшееся доступное пространство для тома кластера, измеряемое в байтах | Байт | Multi | DBClusterIdentifier | Применимо |
| VolumeBytesLeftTotal |  | Байт | Multi | Region | Применимо |
| VolumeBytesLeftTotal |  | Байт | Multi | Region, EngineName | Применимо |
| VolumeReadIOPs | Среднее количество оплачиваемых операций ввода-вывода чтения из тома кластера; регистрируется с интервалом в 5 минут. | Байт | Multi | DBClusterIdentifier | Применимо |
| VolumeReadIOPs |  | Байт | Multi | Region, EngineName | Применимо |
| VolumeWriteIOPs | Среднее количество дисковых операций ввода-вывода записи в том кластера; регистрируется с интервалом в 5 минут | Байт | Multi | DBClusterIdentifier | Применимо |
| VolumeWriteIOPs |  | Байт | Multi | Region, EngineName | Применимо |