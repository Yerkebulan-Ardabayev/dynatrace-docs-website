---
title: Мониторинг Amazon MSK (Kafka)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-msk-kafka
scraped: 2026-05-12T11:30:35.857321
---

# Мониторинг Amazon MSK (Kafka)

# Мониторинг Amazon MSK (Kafka)

* Практическое руководство
* Чтение: 14 мин
* Обновлено 19 мая 2025 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon MSK (Kafka). Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

## Предварительные требования

Чтобы включить мониторинг этого сервиса, необходимо

* ActiveGate версии 1.197+

  + Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развёртываний Dynatrace Managed можно использовать ActiveGate любого типа.

    Для доступа на основе ролей (в развёртывании [SaaS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Приём метрик Amazon CloudWatch.") или [Managed](/managed/ingest-from/amazon-web-services/set-up-aws-monitoring-with-managed#role-based-access "Подключите аккаунт Amazon к Dynatrace Managed и начните мониторинг.")) требуется [Environment ActiveGate](/managed/ingest-from/dynatrace-activegate/installation "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.203+
* Обновлённая [политика мониторинга AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Приём метрик Amazon CloudWatch."), включающая дополнительные сервисы AWS.
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

![Msk](https://dt-cdn.net/images/dashboard-71-2325-1b0eb2ef80.png)

Msk

## Доступные метрики

Основное измерение: `Cluster Name`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ActiveControllerCount | В любой момент времени активным должен быть только один контроллер на кластер. | Количество | Multi | Cluster Name | Применимо |
| ActiveControllerCount |  | Количество | Sum | Cluster Name | Применимо |
| BytesInPerSec | Количество байт в секунду, полученных от клиентов | Байт в секунду | Multi | Cluster Name, Broker ID |  |
| BytesInPerSec |  | Байт в секунду | Multi | Cluster Name, Broker ID, Topic |  |
| BytesInPerSec |  | Байт в секунду | Sum | Cluster Name, Broker ID |  |
| BytesInPerSec |  | Байт в секунду | Sum | Cluster Name, Broker ID, Topic |  |
| BytesOutPerSec | Количество байт в секунду, отправленных клиентам | Байт в секунду | Multi | Cluster Name, Broker ID |  |
| BytesOutPerSec |  | Байт в секунду | Multi | Cluster Name, Broker ID, Topic |  |
| BytesOutPerSec |  | Байт в секунду | Sum | Cluster Name, Broker ID |  |
| BytesOutPerSec |  | Байт в секунду | Sum | Cluster Name, Broker ID, Topic |  |
| CPUCreditBalance | Количество заработанных кредитов | Количество | Multi | Cluster Name, Broker ID |  |
| CPUCreditBalance |  | Количество | Sum | Cluster Name, Broker ID |  |
| CPUCreditUsage | Количество использованных кредитов | Количество | Multi | Cluster Name, Broker ID |  |
| CPUCreditUsage |  | Количество | Sum | Cluster Name, Broker ID |  |
| CpuIdle | Процент времени простоя CPU | Процент | Multi | Cluster Name, Broker ID | Применимо |
| CpuIdle |  | Процент | Sum | Cluster Name, Broker ID | Применимо |
| CpuSystem | Процент CPU в пространстве ядра | Процент | Multi | Cluster Name, Broker ID | Применимо |
| CpuSystem |  | Процент | Sum | Cluster Name, Broker ID | Применимо |
| CpuUser | Процент CPU в пользовательском пространстве | Процент | Multi | Cluster Name, Broker ID | Применимо |
| CpuUser |  | Процент | Sum | Cluster Name, Broker ID | Применимо |
| FetchConsumerLocalTimeMsMean | Среднее время в миллисекундах, в течение которого запрос потребителя обрабатывается на лидере | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchConsumerLocalTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchConsumerRequestQueueTimeMsMean | Среднее время в миллисекундах, в течение которого запрос потребителя ожидает в очереди запросов | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchConsumerRequestQueueTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchConsumerResponseQueueTimeMsMean | Среднее время в миллисекундах, в течение которого запрос потребителя ожидает в очереди ответов | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchConsumerResponseQueueTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchConsumerResponseSendTimeMsMean |  | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchConsumerResponseSendTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchConsumerTotalTimeMsMean | Среднее суммарное время в миллисекундах, которое потребители тратят на извлечение данных из брокера | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchConsumerTotalTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchFollowerLocalTimeMsMean | Среднее время в миллисекундах, в течение которого запрос фолловера обрабатывается на лидере | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchFollowerLocalTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchFollowerRequestQueueTimeMsMean | Среднее время в миллисекундах, в течение которого запрос фолловера ожидает в очереди запросов | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchFollowerRequestQueueTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchFollowerResponseQueueTimeMsMean | Среднее время в миллисекундах, в течение которого запрос фолловера ожидает в очереди ответов | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchFollowerResponseQueueTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchFollowerResponseSendTimeMsMean | Среднее время в миллисекундах, за которое фолловер отправляет ответ | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchFollowerResponseSendTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchFollowerTotalTimeMsMean | Среднее суммарное время в миллисекундах, которое фолловеры тратят на извлечение данных из брокера | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchFollowerTotalTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec | Количество преобразований сообщений при извлечении в секунду для брокера | Количество в секунду | Multi | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec |  | Количество в секунду | Multi | Cluster Name, Broker ID, Topic |  |
| FetchMessageConversionsPerSec |  | Количество в секунду | Sum | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec |  | Количество в секунду | Sum | Cluster Name, Broker ID, Topic |  |
| FetchMessageConversionsTimeMsMean | Среднее суммарное время в миллисекундах, которое извлекаемые сообщения тратят на преобразование | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchMessageConversionsTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| FetchThrottleByteRate | Количество байт в секунду, подвергнутых регулированию | Байт в секунду | Multi | Cluster Name, Broker ID |  |
| FetchThrottleByteRate |  | Байт в секунду | Sum | Cluster Name, Broker ID |  |
| FetchThrottleQueueSize | Количество сообщений в очереди регулирования | Количество | Multi | Cluster Name, Broker ID |  |
| FetchThrottleQueueSize |  | Количество | Sum | Cluster Name, Broker ID |  |
| FetchThrottleTime | Среднее время регулирования извлечения в миллисекундах | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| FetchThrottleTime |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| GlobalPartitionCount | Общее количество партиций на всех брокерах в кластере | Количество | Multi | Cluster Name | Применимо |
| GlobalPartitionCount |  | Количество | Sum | Cluster Name | Применимо |
| GlobalTopicCount | Общее количество топиков на всех брокерах в кластере | Количество | Multi | Cluster Name | Применимо |
| GlobalTopicCount |  | Количество | Sum | Cluster Name | Применимо |
| KafkaAppLogsDiskUsed | Процент дискового пространства, используемого для журналов приложения | Процент | Multi | Cluster Name, Broker ID | Применимо |
| KafkaAppLogsDiskUsed |  | Процент | Sum | Cluster Name, Broker ID | Применимо |
| KafkaDataLogsDiskUsed | Процент дискового пространства, используемого для журналов данных | Процент | Multi | Cluster Name, Broker ID | Применимо |
| KafkaDataLogsDiskUsed |  | Процент | Sum | Cluster Name, Broker ID | Применимо |
| LeaderCount | Количество реплик-лидеров | Количество | Multi | Cluster Name, Broker ID |  |
| LeaderCount |  | Количество | Sum | Cluster Name, Broker ID |  |
| MemoryBuffered | Размер в байтах буферизованной памяти для брокера | Байт | Multi | Cluster Name, Broker ID | Применимо |
| MemoryBuffered |  | Байт | Sum | Cluster Name, Broker ID | Применимо |
| MemoryCached | Размер в байтах кэшированной памяти для брокера | Байт | Multi | Cluster Name, Broker ID | Применимо |
| MemoryCached |  | Байт | Sum | Cluster Name, Broker ID | Применимо |
| MemoryFree | Размер в байтах памяти, свободной и доступной для брокера | Байт | Multi | Cluster Name, Broker ID | Применимо |
| MemoryFree |  | Байт | Sum | Cluster Name, Broker ID | Применимо |
| MemoryUsed | Размер в байтах памяти, используемой брокером | Байт | Multi | Cluster Name, Broker ID | Применимо |
| MemoryUsed |  | Байт | Sum | Cluster Name, Broker ID | Применимо |
| MessagesInPerSec | Количество входящих сообщений в секунду для брокера | Количество в секунду | Multi | Cluster Name, Broker ID |  |
| MaxOffsetLag | Максимальное отставание смещения по всем партициям в топике | Количество | Multi | Cluster Name, Consumer Group, Topic |  |
| MaxOffsetLag | Максимальное отставание смещения по всем партициям в топике | Количество | Sum | Cluster Name, Consumer Group, Topic |  |
| MessagesInPerSec |  | Количество в секунду | Multi | Cluster Name, Broker ID, Topic |  |
| MessagesInPerSec |  | Количество в секунду | Sum | Cluster Name, Broker ID |  |
| MessagesInPerSec |  | Количество в секунду | Sum | Cluster Name, Broker ID, Topic |  |
| NetworkProcessorAvgIdlePercent | Средний процент времени, в течение которого сетевые процессоры простаивают | Процент | Multi | Cluster Name, Broker ID |  |
| NetworkProcessorAvgIdlePercent |  | Процент | Sum | Cluster Name, Broker ID |  |
| NetworkRxDropped | Количество отброшенных пакетов при приёме | Количество | Multi | Cluster Name, Broker ID | Применимо |
| NetworkRxDropped |  | Количество | Sum | Cluster Name, Broker ID | Применимо |
| NetworkRxErrors | Количество сетевых ошибок приёма для брокера | Количество | Multi | Cluster Name, Broker ID | Применимо |
| NetworkRxErrors |  | Количество | Sum | Cluster Name, Broker ID | Применимо |
| NetworkRxPackets | Количество пакетов, полученных брокером | Количество | Multi | Cluster Name, Broker ID | Применимо |
| NetworkRxPackets |  | Количество | Sum | Cluster Name, Broker ID | Применимо |
| NetworkTxDropped | Количество отброшенных пакетов при передаче | Количество | Multi | Cluster Name, Broker ID | Применимо |
| NetworkTxDropped |  | Количество | Sum | Cluster Name, Broker ID | Применимо |
| NetworkTxErrors | Количество сетевых ошибок передачи для брокера | Количество | Multi | Cluster Name, Broker ID | Применимо |
| NetworkTxErrors |  | Количество | Sum | Cluster Name, Broker ID | Применимо |
| NetworkTxPackets | Количество пакетов, переданных брокером | Количество | Multi | Cluster Name, Broker ID | Применимо |
| NetworkTxPackets |  | Количество | Sum | Cluster Name, Broker ID | Применимо |
| OfflinePartitionsCount | Общее количество партиций, находящихся офлайн в кластере | Количество | Multi | Cluster Name | Применимо |
| OfflinePartitionsCount |  | Количество | Sum | Cluster Name | Применимо |
| PartitionCount | Количество партиций для брокера | Количество | Multi | Cluster Name, Broker ID |  |
| PartitionCount |  | Количество | Sum | Cluster Name, Broker ID |  |
| ProduceLocalTimeMsMean | Среднее время в миллисекундах, за которое фолловер отправляет ответ | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceLocalTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec | Количество преобразований сообщений при записи в секунду для брокера | Количество в секунду | Multi | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec |  | Количество в секунду | Multi | Cluster Name, Broker ID, Topic |  |
| ProduceMessageConversionsPerSec |  | Количество в секунду | Sum | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec |  | Количество в секунду | Sum | Cluster Name, Broker ID, Topic |  |
| ProduceMessageConversionsTimeMsMean | Среднее время в миллисекундах, затраченное на преобразование формата сообщений | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceMessageConversionsTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| ProduceRequestQueueTimeMsMean | Среднее время в миллисекундах, в течение которого сообщения запросов находятся в очереди | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceRequestQueueTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| ProduceResponseQueueTimeMsMean | Среднее время в миллисекундах, в течение которого сообщения ответов находятся в очереди | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceResponseQueueTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| ProduceResponseSendTimeMsMean | Среднее время в миллисекундах, затраченное на отправку сообщений ответов | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceResponseSendTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleByteRate | Количество байт в секунду, подвергнутых регулированию | Байт в секунду | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleByteRate |  | Байт в секунду | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleQueueSize | Количество сообщений в очереди регулирования | Количество | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleQueueSize |  | Количество | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleTime | Среднее время регулирования записи в миллисекундах | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleTime |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| ProduceTotalTimeMsMean | Среднее время записи в миллисекундах | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| ProduceTotalTimeMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| RequestBytesMean | Среднее количество байт запросов для брокера | Байт | Multi | Cluster Name, Broker ID |  |
| RequestBytesMean |  | Байт | Sum | Cluster Name, Broker ID |  |
| RequestExemptFromThrottleTime | Среднее время в миллисекундах, проведённое в сетевых потоках и потоках ввода-вывода брокера для обработки запросов, освобождённых от регулирования | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| RequestExemptFromThrottleTime |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| RequestHandlerAvgIdlePercent | Средний процент времени, в течение которого потоки обработчика запросов простаивают | Процент | Multi | Cluster Name, Broker ID |  |
| RequestHandlerAvgIdlePercent |  | Процент | Sum | Cluster Name, Broker ID |  |
| RequestThrottleQueueSize | Количество сообщений в очереди регулирования | Количество | Multi | Cluster Name, Broker ID |  |
| RequestThrottleQueueSize |  | Количество | Sum | Cluster Name, Broker ID |  |
| RequestThrottleTime | Среднее время регулирования запросов в миллисекундах | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| RequestThrottleTime |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| RequestTime | Среднее время в миллисекундах, проведённое в сетевых потоках и потоках ввода-вывода брокера для обработки запросов | Миллисекунда | Multi | Cluster Name, Broker ID |  |
| RequestTime |  | Миллисекунда | Sum | Cluster Name, Broker ID |  |
| RootDiskUsed | Процент корневого диска, используемого брокером | Процент | Multi | Cluster Name, Broker ID | Применимо |
| RootDiskUsed |  | Процент | Sum | Cluster Name, Broker ID | Применимо |
| SumOffsetLag | Совокупное отставание смещения по всем партициям в топике | Количество | Multi | Cluster Name, Consumer Group, Topic |  |
| SwapFree | Размер в байтах памяти подкачки, доступной для брокера | Байт | Multi | Cluster Name, Broker ID | Применимо |
| SwapFree |  | Байт | Sum | Cluster Name, Broker ID | Применимо |
| SwapUsed | Размер в байтах памяти подкачки, используемой брокером | Байт | Multi | Cluster Name, Broker ID | Применимо |
| SwapUsed |  | Байт | Sum | Cluster Name, Broker ID | Применимо |
| UnderMinIsrPartitionCount | Количество партиций ниже minIsr для брокера | Количество | Multi | Cluster Name, Broker ID |  |
| UnderMinIsrPartitionCount |  | Количество | Sum | Cluster Name, Broker ID |  |
| UnderReplicatedPartitions | Количество партиций с недостаточной репликацией для брокера | Количество | Multi | Cluster Name, Broker ID |  |
| UnderReplicatedPartitions |  | Количество | Sum | Cluster Name, Broker ID |  |
| ZooKeeperRequestLatencyMsMean | Средняя задержка в миллисекундах для запросов ZooKeeper от брокера | Миллисекунда | Multi | Cluster Name, Broker ID | Применимо |
| ZooKeeperRequestLatencyMsMean |  | Миллисекунда | Multi | Cluster Name | Применимо |
| ZooKeeperRequestLatencyMsMean |  | Миллисекунда | Sum | Cluster Name, Broker ID | Применимо |
| ZooKeeperRequestLatencyMsMean |  | Миллисекунда | Sum | Cluster Name | Применимо |
| ZooKeeperSessionState | Статус подключения сеанса ZooKeeper брокера, который может принимать одно из следующих значений: `NOT_CONNECTED`: `0.0`, `ASSOCIATING`: `0.1`, `CONNECTING`: `0.5`, `CONNECTEDREADONLY`: `0.8`, `CONNECTED`: `1.0`, `CLOSED`: `5.0`, `AUTH_FAILED`: `10.0`. | Количество | Multi | Cluster Name, Broker ID | Применимо |
| ZooKeeperSessionState |  | Количество | Multi | Cluster Name | Применимо |
| ZooKeeperSessionState |  | Количество | Sum | Cluster Name, Broker ID |  |
| ZooKeeperSessionState |  | Количество | Sum | Cluster Name |  |