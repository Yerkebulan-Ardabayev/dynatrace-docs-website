---
title: Мониторинг Amazon MSK (Kafka)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-msk-kafka
scraped: 2026-03-01T21:21:59.414254
---

# Мониторинг Amazon MSK (Kafka)

# Мониторинг Amazon MSK (Kafka)

* Практическое руководство
* Чтение: 14 мин
* Обновлено May 19, 2025

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая Amazon MSK (Kafka). Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга данного сервиса вам необходимо

* ActiveGate версии 1.197+

  + Для развертываний Dynatrace SaaS вам потребуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Интеграция метрик из Amazon CloudWatch.") так и [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) развертывании) вам потребуется [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.203+
* Обновленная [политика мониторинга AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.  
  Для [обновления политики AWS IAMï»¿](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса список дополнительных разрешений, специфичных для этого сервиса.

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

Ниже приведён пример политики JSON для одного отдельного сервиса.

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

* `"apigateway:GET"` for **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"`, and `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

### Конечные точки AWS, которые должны быть доступны из ActiveGate с соответствующими сервисами AWS

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

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

После добавления сервиса в мониторинг предустановленная панель мониторинга, содержащая все рекомендуемые метрики, автоматически появится на странице **Панели мониторинга**. Для поиска конкретных панелей мониторинга фильтруйте по **Preset** и затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленная панель мониторинга появилась на странице **Панели мониторинга**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленную панель мониторинга напрямую, но можете клонировать и редактировать её. Для клонирования панели мониторинга откройте меню обзора (**â¦**) и выберите **Clone**.

Для удаления панели мониторинга со страницы панелей мониторинга вы можете скрыть её. Для скрытия панели мониторинга откройте меню обзора (**â¦**) и выберите **Hide**.

Скрытие панели мониторинга не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Для проверки доступности предустановленных панелей мониторинга для каждого сервиса AWS см. список ниже.

### Список доступности предустановленных панелей мониторинга

| Сервис AWS | Предустановленная панель |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | Недоступна |
| AWS Lambda (built-in) | Недоступна |
| Amazon Application and Network Load Balancer (built-in) | Недоступна |
| Amazon DynamoDB (built-in) | Недоступна |
| Amazon EBS (built-in) | Недоступна |
| Amazon EC2 (built-in) | Недоступна |
| Amazon Elastic Load Balancer (ELB) (built-in) | Недоступна |
| Amazon RDS (built-in) | Недоступна |
| Amazon S3 (built-in) | Недоступна |
| AWS Certificate Manager Private Certificate Authority | Недоступна |
| All monitored Amazon services | Недоступна |
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

![Msk](https://dt-cdn.net/images/dashboard-71-2325-1b0eb2ef80.png)

## Доступные метрики

`Cluster Name` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| ActiveControllerCount | Only one controller per cluster should be active at any given time. | Count | Multi | Cluster Name | Доступна |
| ActiveControllerCount |  | Count | Sum | Cluster Name | Доступна |
| BytesInPerSec | The number of bytes per second received from clients | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| BytesInPerSec |  | Bytes/Second | Multi | Cluster Name, Broker ID, Topic |  |
| BytesInPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| BytesInPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID, Topic |  |
| BytesOutPerSec | The number of bytes per second sent to clients | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| BytesOutPerSec |  | Bytes/Second | Multi | Cluster Name, Broker ID, Topic |  |
| BytesOutPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| BytesOutPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID, Topic |  |
| CPUCreditBalance | The number of earned credits | Count | Multi | Cluster Name, Broker ID |  |
| CPUCreditBalance |  | Count | Sum | Cluster Name, Broker ID |  |
| CPUCreditUsage | The number of used credits | Count | Multi | Cluster Name, Broker ID |  |
| CPUCreditUsage |  | Count | Sum | Cluster Name, Broker ID |  |
| CpuIdle | The percentage of CPU idle time | Percent | Multi | Cluster Name, Broker ID | Доступна |
| CpuIdle |  | Percent | Sum | Cluster Name, Broker ID | Доступна |
| CpuSystem | The percentage of CPU in kernel space | Percent | Multi | Cluster Name, Broker ID | Доступна |
| CpuSystem |  | Percent | Sum | Cluster Name, Broker ID | Доступна |
| CpuUser | The percentage of CPU in user space | Percent | Multi | Cluster Name, Broker ID | Доступна |
| CpuUser |  | Percent | Sum | Cluster Name, Broker ID | Доступна |
| FetchConsumerLocalTimeMsMean | The mean time in milliseconds that the consumer request is processed at the leader | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerLocalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerRequestQueueTimeMsMean | The mean time in milliseconds that the consumer request waits in the request queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerRequestQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerResponseQueueTimeMsMean | The mean time in milliseconds that the consumer request waits in the response queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerResponseQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerResponseSendTimeMsMean |  | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerResponseSendTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerTotalTimeMsMean | The mean total time in milliseconds that consumers spend on fetching data from the broker | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerTotalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerLocalTimeMsMean | The mean time in milliseconds that the follower request is processed at the leader | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerLocalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerRequestQueueTimeMsMean | The mean time in milliseconds that the follower request waits in the request queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerRequestQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerResponseQueueTimeMsMean | The mean time in milliseconds that the follower request waits in the response queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerResponseQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerResponseSendTimeMsMean | The mean time in milliseconds for the follower to send a response | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerResponseSendTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerTotalTimeMsMean | The mean total time in milliseconds that followers spend on fetching data from the broker | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerTotalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec | The number of fetch message conversions per second for the broker | Count/Second | Multi | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec |  | Count/Second | Multi | Cluster Name, Broker ID, Topic |  |
| FetchMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID, Topic |  |
| FetchMessageConversionsTimeMsMean | The mean total time in milliseconds that messages being fetched spend converting | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchMessageConversionsTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchThrottleByteRate | The number of throttled bytes per second | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| FetchThrottleByteRate |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| FetchThrottleQueueSize | The number of messages in the throttle queue | Count | Multi | Cluster Name, Broker ID |  |
| FetchThrottleQueueSize |  | Count | Sum | Cluster Name, Broker ID |  |
| FetchThrottleTime | The average fetch throttle time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| GlobalPartitionCount | Total number of partitions across all brokers in the cluster | Count | Multi | Cluster Name | Доступна |
| GlobalPartitionCount |  | Count | Sum | Cluster Name | Доступна |
| GlobalTopicCount | Total number of topics across all brokers in the cluster | Count | Multi | Cluster Name | Доступна |
| GlobalTopicCount |  | Count | Sum | Cluster Name | Доступна |
| KafkaAppLogsDiskUsed | The percentage of disk space used for application logs | Percent | Multi | Cluster Name, Broker ID | Доступна |
| KafkaAppLogsDiskUsed |  | Percent | Sum | Cluster Name, Broker ID | Доступна |
| KafkaDataLogsDiskUsed | The percentage of disk space used for data logs | Percent | Multi | Cluster Name, Broker ID | Доступна |
| KafkaDataLogsDiskUsed |  | Percent | Sum | Cluster Name, Broker ID | Доступна |
| LeaderCount | The number of leader replicas | Count | Multi | Cluster Name, Broker ID |  |
| LeaderCount |  | Count | Sum | Cluster Name, Broker ID |  |
| MemoryBuffered | The size in bytes of buffered memory for the broker | Bytes | Multi | Cluster Name, Broker ID | Доступна |
| MemoryBuffered |  | Bytes | Sum | Cluster Name, Broker ID | Доступна |
| MemoryCached | The size in bytes of cached memory for the broker | Bytes | Multi | Cluster Name, Broker ID | Доступна |
| MemoryCached |  | Bytes | Sum | Cluster Name, Broker ID | Доступна |
| MemoryFree | The size in bytes of memory that is free and available for the broker | Bytes | Multi | Cluster Name, Broker ID | Доступна |
| MemoryFree |  | Bytes | Sum | Cluster Name, Broker ID | Доступна |
| MemoryUsed | The size in bytes of memory that is in use for the broker | Bytes | Multi | Cluster Name, Broker ID | Доступна |
| MemoryUsed |  | Bytes | Sum | Cluster Name, Broker ID | Доступна |
| MessagesInPerSec | The number of incoming messages per second for the broker | Count/Second | Multi | Cluster Name, Broker ID |  |
| MaxOffsetLag | The maximum offset lag across all partitions in a topic | Count | Multi | Cluster Name, Consumer Group, Topic |  |
| MaxOffsetLag | The maximum offset lag across all partitions in a topic | Count | Sum | Cluster Name, Consumer Group, Topic |  |
| MessagesInPerSec |  | Count/Second | Multi | Cluster Name, Broker ID, Topic |  |
| MessagesInPerSec |  | Count/Second | Sum | Cluster Name, Broker ID |  |
| MessagesInPerSec |  | Count/Second | Sum | Cluster Name, Broker ID, Topic |  |
| NetworkProcessorAvgIdlePercent | The average percentage of the time the network processors are idle | Percent | Multi | Cluster Name, Broker ID |  |
| NetworkProcessorAvgIdlePercent |  | Percent | Sum | Cluster Name, Broker ID |  |
| NetworkRxDropped | The number of dropped receive packages | Count | Multi | Cluster Name, Broker ID | Доступна |
| NetworkRxDropped |  | Count | Sum | Cluster Name, Broker ID | Доступна |
| NetworkRxErrors | The number of network receive errors for the broker | Count | Multi | Cluster Name, Broker ID | Доступна |
| NetworkRxErrors |  | Count | Sum | Cluster Name, Broker ID | Доступна |
| NetworkRxPackets | The number of packets received by the broker | Count | Multi | Cluster Name, Broker ID | Доступна |
| NetworkRxPackets |  | Count | Sum | Cluster Name, Broker ID | Доступна |
| NetworkTxDropped | The number of dropped transmit packages | Count | Multi | Cluster Name, Broker ID | Доступна |
| NetworkTxDropped |  | Count | Sum | Cluster Name, Broker ID | Доступна |
| NetworkTxErrors | The number of network transmit errors for the broker | Count | Multi | Cluster Name, Broker ID | Доступна |
| NetworkTxErrors |  | Count | Sum | Cluster Name, Broker ID | Доступна |
| NetworkTxPackets | The number of packets transmitted by the broker | Count | Multi | Cluster Name, Broker ID | Доступна |
| NetworkTxPackets |  | Count | Sum | Cluster Name, Broker ID | Доступна |
| OfflinePartitionsCount | Total number of partitions that are offline in the cluster | Count | Multi | Cluster Name | Доступна |
| OfflinePartitionsCount |  | Count | Sum | Cluster Name | Доступна |
| PartitionCount | The number of partitions for the broker | Count | Multi | Cluster Name, Broker ID |  |
| PartitionCount |  | Count | Sum | Cluster Name, Broker ID |  |
| ProduceLocalTimeMsMean | The mean time in milliseconds for the follower to send a response | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceLocalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec | The number of produce message conversions per second for the broker | Count/Second | Multi | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec |  | Count/Second | Multi | Cluster Name, Broker ID, Topic |  |
| ProduceMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID, Topic |  |
| ProduceMessageConversionsTimeMsMean | The mean time in milliseconds spent on message format conversions | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceMessageConversionsTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceRequestQueueTimeMsMean | The mean time in milliseconds that request messages spend in the queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceRequestQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceResponseQueueTimeMsMean | The mean time in milliseconds that response messages spend in the queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceResponseQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceResponseSendTimeMsMean | The mean time in milliseconds spent on sending response messages | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceResponseSendTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleByteRate | The number of throttled bytes per second | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleByteRate |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleQueueSize | The number of messages in the throttle queue | Count | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleQueueSize |  | Count | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleTime | The average produce throttle time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceTotalTimeMsMean | The mean produce time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceTotalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RequestBytesMean | The mean number of request bytes for the broker | Bytes | Multi | Cluster Name, Broker ID |  |
| RequestBytesMean |  | Bytes | Sum | Cluster Name, Broker ID |  |
| RequestExemptFromThrottleTime | The average time in milliseconds spent in broker network and I/O threads to process requests that are exempt from throttling | Milliseconds | Multi | Cluster Name, Broker ID |  |
| RequestExemptFromThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RequestHandlerAvgIdlePercent | The average percentage of the time the request handler threads are idle | Percent | Multi | Cluster Name, Broker ID |  |
| RequestHandlerAvgIdlePercent |  | Percent | Sum | Cluster Name, Broker ID |  |
| RequestThrottleQueueSize | The number of messages in the throttle queue | Count | Multi | Cluster Name, Broker ID |  |
| RequestThrottleQueueSize |  | Count | Sum | Cluster Name, Broker ID |  |
| RequestThrottleTime | The average request throttle time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| RequestThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RequestTime | The average time in milliseconds spent in broker network and I/O threads to process requests | Milliseconds | Multi | Cluster Name, Broker ID |  |
| RequestTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RootDiskUsed | The percentage of the root disk used by the broker | Percent | Multi | Cluster Name, Broker ID | Доступна |
| RootDiskUsed |  | Percent | Sum | Cluster Name, Broker ID | Доступна |
| SumOffsetLag | The aggregated offset lag for all the partitions in a topic | Count | Multi | Cluster Name, Consumer Group, Topic |  |
| SwapFree | The size in bytes of swap memory that is available for the broker | Bytes | Multi | Cluster Name, Broker ID | Доступна |
| SwapFree |  | Bytes | Sum | Cluster Name, Broker ID | Доступна |
| SwapUsed | The size in bytes of swap memory that is in use for the broker | Bytes | Multi | Cluster Name, Broker ID | Доступна |
| SwapUsed |  | Bytes | Sum | Cluster Name, Broker ID | Доступна |
| UnderMinIsrPartitionCount | The number of under minIsr partitions for the broker | Count | Multi | Cluster Name, Broker ID |  |
| UnderMinIsrPartitionCount |  | Count | Sum | Cluster Name, Broker ID |  |
| UnderReplicatedPartitions | The number of under-replicated partitions for the broker | Count | Multi | Cluster Name, Broker ID |  |
| UnderReplicatedPartitions |  | Count | Sum | Cluster Name, Broker ID |  |
| ZooKeeperRequestLatencyMsMean | Mean latency in milliseconds for ZooKeeper requests from broker | Milliseconds | Multi | Cluster Name, Broker ID | Доступна |
| ZooKeeperRequestLatencyMsMean |  | Milliseconds | Multi | Cluster Name | Доступна |
| ZooKeeperRequestLatencyMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID | Доступна |
| ZooKeeperRequestLatencyMsMean |  | Milliseconds | Sum | Cluster Name | Доступна |
| ZooKeeperSessionState | Connection status of broker's ZooKeeper session which may be one of the following: `NOT_CONNECTED`: `0.0`, `ASSOCIATING`: `0.1`, `CONNECTING`: `0.5`, `CONNECTEDREADONLY`: `0.8`, `CONNECTED`: `1.0`, `CLOSED`: `5.0`, `AUTH_FAILED`: `10.0`. | Count | Multi | Cluster Name, Broker ID | Доступна |
| ZooKeeperSessionState |  | Count | Multi | Cluster Name | Доступна |
| ZooKeeperSessionState |  | Count | Sum | Cluster Name, Broker ID |  |
| ZooKeeperSessionState |  | Count | Sum | Cluster Name |  |