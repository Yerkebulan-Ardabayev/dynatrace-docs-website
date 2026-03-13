---
title: Мониторинг Amazon GameLift
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-gamelift
scraped: 2026-03-04T21:33:02.411476
---

# Мониторинг Amazon GameLift

# Мониторинг Amazon GameLift

* Classic
* Практическое руководство
* Чтение: 10 мин
* Опубликовано Jul 06, 2020

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая Amazon GameLift. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

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

![GameLift](https://dt-cdn.net/images/gamelift-dashboard-1-2982-7671d496d8.png)

## Доступные метрики

`FleetId` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| ActivatingGameSessions | Game sessions with `Activating` status, which means they are in the process of starting up | Count | Multi | FleetId | Доступна |
| ActivatingGameSessions |  | Count | Multi | Region, MetricGroups | Доступна |
| ActiveGameSessions | Game sessions with `Active` status, which means they are able to host players, and are hosting zero or more players | Count | Multi | FleetId | Доступна |
| ActiveGameSessions |  | Count | Multi | Region, MetricGroups | Доступна |
| ActiveInstances | Instances with `Active` status, which means they are running active server processes | Count | Multi | FleetId | Доступна |
| ActiveInstances |  | Count | Multi | Region, MetricGroups | Доступна |
| ActiveServerProcesses | Server processes with `Active` status, which means they are running and able to host game session | Count | Multi | FleetId | Доступна |
| ActiveServerProcesses |  | Count | Multi | Region, MetricGroups | Доступна |
| AvailableGameSessions | Active, healthy server processes that are not currently being used to host a game session and can start a new game session without a delay to spin up new server processes or instances | Count | Multi | FleetId | Доступна |
| AvailableGameSessions |  | Count | Multi | Region, MetricGroups | Доступна |
| AverageWaitTime | Average amount of time that game session placement requests in the queue in `Pending` status have been waiting to be fulfilled | Seconds | Multi | Region, QueueName | Доступна |
| AverageWaitTime |  | Seconds | Sum | Region, QueueName | Доступна |
| CurrentPlayerSessions | Player sessions with either `Active` status (player is connected to an active game session) or `Reserved` status (player has been given a slot in a game session but hasn't yet connected) | Count | Multi | FleetId | Доступна |
| CurrentPlayerSessions |  | Count | Multi | Region, MetricGroups | Доступна |
| CurrentTickets | Matchmaking requests currently being processed or waiting to be processed | Count | Multi | Region, ConfigurationName | Доступна |
| CurrentTickets |  | Count | Sum | Region, ConfigurationName | Доступна |
| DesiredInstances | Target number of active instances that GameLift is working to maintain in the fleet | Count | Multi | FleetId |  |
| FirstChoiceNotViable | Game sessions successfully placed but that aren't in the first-choice fleet, because that fleet isn't considered viable (such as a spot fleet with a high interruption rate) | Count/Minute | Multi | Region |  |
| FirstChoiceNotViable |  | Count/Minute | Multi | Region, QueueName |  |
| FirstChoiceNotViable |  | Count/Minute | Sum | Region |  |
| FirstChoiceNotViable |  | Count/Minute | Sum | Region, QueueName |  |
| FirstChoiceOutOfCapacity | Game sessions successfully placed but that aren't in the first-choice fleet, because that fleet doesn't have any available resources | Count/Minute | Multi | Region | Доступна |
| FirstChoiceOutOfCapacity |  | Count/Minute | Multi | Region, QueueName | Доступна |
| FirstChoiceOutOfCapacity |  | Count/Minute | Sum | Region | Доступна |
| FirstChoiceOutOfCapacity |  | Count/Minute | Sum | Region, QueueName | Доступна |
| GameSessionInterruptions | Number of game sessions on spot instances that have been interrupted | Count/Minute | Multi | FleetId |  |
| GameSessionInterruptions |  | Count/Minute | Multi | Region, MetricGroups |  |
| GameSessionInterruptions |  | Count/Minute | Sum | FleetId |  |
| GameSessionInterruptions |  | Count/Minute | Sum | Region, MetricGroups |  |
| HealthyServerProcesses | Active server processes that are reporting healthy | Count | Multi | FleetId | Доступна |
| HealthyServerProcesses |  | Count | Multi | Region, MetricGroups | Доступна |
| IdleInstances | Active instances that are currently hosting zero (0) game sessions. This metric measures capacity that is available but unused. | Count | Multi | FleetId | Доступна |
| IdleInstances |  | Count | Multi | Region, MetricGroups | Доступна |
| InstanceInterruptions | Number of spot instances that have been interrupted | Count/Minute | Multi | FleetId |  |
| InstanceInterruptions |  | Count/Minute | Multi | Region, MetricGroups |  |
| InstanceInterruptions |  | Count/Minute | Sum | FleetId |  |
| InstanceInterruptions |  | Count/Minute | Sum | Region, MetricGroups |  |
| LowestLatencyPlacement | Game sessions that were successfully placed in a region that offers the queue's lowest possible latency for the players | Count/Minute | Multi | Region | Доступна |
| LowestLatencyPlacement |  | Count/Minute | Multi | Region, QueueName | Доступна |
| LowestLatencyPlacement |  | Count/Minute | Sum | Region | Доступна |
| LowestLatencyPlacement |  | Count/Minute | Sum | Region, QueueName | Доступна |
| LowestPricePlacement | Game sessions that were successfully placed in a fleet with the queue's lowest possible price for the chosen region | Count/Minute | Multi | Region |  |
| LowestPricePlacement |  | Count/Minute | Multi | Region, QueueName |  |
| LowestPricePlacement |  | Count/Minute | Sum | Region |  |
| LowestPricePlacement |  | Count/Minute | Sum | Region, QueueName |  |
| MatchAcceptancesTimedOut | For matchmaking configurations that require acceptance, the potential matches that timed out during acceptance since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| MatchesAccepted | For matchmaking configurations that require acceptance, the potential matches that were accepted since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| MatchesCreated | Potential matches that were created since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| MatchesPlaced | Matches that were successfully placed into a game session since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| MatchesRejected | For matchmaking configurations that require acceptance, the potential matches that were rejected by at least one player since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| MaxInstances | Maximum number of instances that are allowed for the fleet | Count | Multi | FleetId |  |
| MinInstances | Minimum number of instances allowed for the fleet | Count | Multi | FleetId |  |
| PercentAvailableGameSessions | Percentage of game session slots on all active server processes (healthy or unhealthy) that are not currently being used (calculated as `AvailableGameSessions` / [`ActiveGameSessions` + `AvailableGameSessions` + unhealthy server processes]) | Percent | Average | FleetId | Доступна |
| PercentAvailableGameSessions |  | Percent | Average | Region, MetricGroups | Доступна |
| PercentHealthyServerProcesses | Percentage of all active server processes that are reporting healthy (calculated as `HealthyServerProcesses` / `ActiveServerProcesses`) | Percent | Multi | FleetId | Доступна |
| PercentHealthyServerProcesses |  | Percent | Multi | Region, MetricGroups | Доступна |
| PercentIdleInstances | Percentage of all active instances that are idle (calculated as `IdleInstances` / `ActiveInstances`) | Percent | Multi | FleetId | Доступна |
| PercentIdleInstances |  | Percent | Multi | Region, MetricGroups | Доступна |
| PlacementsCanceled | Game session placement requests canceled before timing out since the last report | Count/Minute | Multi | Region, QueueName | Доступна |
| PlacementsCanceled |  | Count/Minute | Sum | Region, QueueName | Доступна |
| PlacementsFailed | Game session placement requests that failed for any reason since the last report | Count/Minute | Multi | Region, QueueName | Доступна |
| PlacementsFailed |  | Count/Minute | Sum | Region, QueueName | Доступна |
| PlacementsStarted | New game session placement requests added to the queue since the last report | Count/Minute | Multi | Region, QueueName | Доступна |
| PlacementsStarted |  | Count/Minute | Sum | Region, QueueName | Доступна |
| PlacementsSucceeded | Game session placement requests that resulted in a new game session since the last report | Count/Minute | Multi | Region, QueueName | Доступна |
| PlacementsSucceeded |  | Count/Minute | Sum | Region, QueueName | Доступна |
| PlacementsTimedOut | Game session placement requests that reached the queue's timeout limit without being fulfilled since the last report | Count/Minute | Multi | Region, QueueName | Доступна |
| PlacementsTimedOut |  | Count/Minute | Sum | Region, QueueName | Доступна |
| PlayerSessionActivations | Player sessions that transitioned from `Reserved` to `Active` status since the last report | Count/Minute | Multi | FleetId | Доступна |
| PlayerSessionActivations |  | Count/Minute | Multi | Region, MetricGroups | Доступна |
| PlayerSessionActivations |  | Count/Minute | Sum | FleetId | Доступна |
| PlayerSessionActivations |  | Count/Minute | Sum | Region, MetricGroups | Доступна |
| PlayersStarted | Players in matchmaking tickets that were added since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| QueueDepth | Number of game session placement requests in the queue with `Pending` status | Count | Multi | Region, QueueName | Доступна |
| QueueDepth |  | Count | Sum | Region, QueueName | Доступна |
| ServerProcessAbnormalTerminations | Server processes that were shut down due to abnormal circumstances since the last report | Count/Minute | Multi | FleetId | Доступна |
| ServerProcessAbnormalTerminations |  | Count/Minute | Sum | FleetId | Доступна |
| ServerProcessAbnormalTerminations |  | Count/Minute | Multi | Region, MetricGroups | Доступна |
| ServerProcessAbnormalTerminations |  | Count/Minute | Sum | Region, MetricGroups | Доступна |
| ServerProcessActivations | Server processes that successfully transitioned from `Activating` to `Active` status since the last report | Count/Minute | Multi | FleetId | Доступна |
| ServerProcessActivations |  | Count/Minute | Sum | FleetId | Доступна |
| ServerProcessActivations |  | Count/Minute | Multi | Region, MetricGroups | Доступна |
| ServerProcessActivations |  | Count/Minute | Sum | Region, MetricGroups | Доступна |
| ServerProcessTerminations | Server processes that were shut down since the last report | Count/Minute | Multi | FleetId | Доступна |
| ServerProcessTerminations |  | Count/Minute | Sum | FleetId | Доступна |
| ServerProcessTerminations |  | Count/Minute | Multi | Region, MetricGroups | Доступна |
| ServerProcessTerminations |  | Count/Minute | Sum | Region, MetricGroups | Доступна |
| TicketsFailed | Matchmaking requests that resulted in failure since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| TicketsStarted | New matchmaking requests that were created since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| TicketsTimedOut | Matchmaking requests that reached the timeout limit since the last report | Count/Minute | Sum | Region, ConfigurationName | Доступна |
| TimeToMatch | For matchmaking requests that were put into a potential match before the last report, the amount of time between ticket creation and potential match creation | Seconds | Multi | Region, ConfigurationName | Доступна |
| TimeToTicketCancel | For matchmaking requests that were canceled before the last report, the amount of time between ticket creation and cancellation | Seconds | Multi | Region, ConfigurationName | Доступна |
| TimeToTicketSuccess | For matchmaking requests that succeeded before the last report, the amount of time between ticket creation and successful match placement | Seconds | Multi | Region, ConfigurationName | Доступна |