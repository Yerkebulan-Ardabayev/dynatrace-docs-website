---
title: Мониторинг Amazon GameLift
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-gamelift
scraped: 2026-05-12T11:29:44.603486
---

# Мониторинг Amazon GameLift

# Мониторинг Amazon GameLift

* Практическое руководство
* Чтение: 10 мин
* Опубликовано 6 июля 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon GameLift. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

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

![GameLift](https://dt-cdn.net/images/gamelift-dashboard-1-2982-7671d496d8.png)

GameLift

## Доступные метрики

Основное измерение: `FleetId`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ActivatingGameSessions | Игровые сессии со статусом `Activating`, что означает, что они находятся в процессе запуска | Количество | Multi | FleetId | Применимо |
| ActivatingGameSessions |  | Количество | Multi | Region, MetricGroups | Применимо |
| ActiveGameSessions | Игровые сессии со статусом `Active`, что означает, что они способны принимать игроков и обслуживают ноль или более игроков | Количество | Multi | FleetId | Применимо |
| ActiveGameSessions |  | Количество | Multi | Region, MetricGroups | Применимо |
| ActiveInstances | Экземпляры со статусом `Active`, что означает, что на них выполняются активные серверные процессы | Количество | Multi | FleetId | Применимо |
| ActiveInstances |  | Количество | Multi | Region, MetricGroups | Применимо |
| ActiveServerProcesses | Серверные процессы со статусом `Active`, что означает, что они выполняются и способны обслуживать игровую сессию | Количество | Multi | FleetId | Применимо |
| ActiveServerProcesses |  | Количество | Multi | Region, MetricGroups | Применимо |
| AvailableGameSessions | Активные, исправные серверные процессы, которые в настоящее время не используются для обслуживания игровой сессии и могут запустить новую игровую сессию без задержки на развёртывание новых серверных процессов или экземпляров | Количество | Multi | FleetId | Применимо |
| AvailableGameSessions |  | Количество | Multi | Region, MetricGroups | Применимо |
| AverageWaitTime | Среднее время, в течение которого запросы на размещение игровых сессий в очереди со статусом `Pending` ожидали выполнения | Секунда | Multi | Region, QueueName | Применимо |
| AverageWaitTime |  | Секунда | Sum | Region, QueueName | Применимо |
| CurrentPlayerSessions | Сессии игроков со статусом `Active` (игрок подключён к активной игровой сессии) или `Reserved` (игроку выделен слот в игровой сессии, но он ещё не подключился) | Количество | Multi | FleetId | Применимо |
| CurrentPlayerSessions |  | Количество | Multi | Region, MetricGroups | Применимо |
| CurrentTickets | Запросы на подбор игроков, которые в настоящее время обрабатываются или ожидают обработки | Количество | Multi | Region, ConfigurationName | Применимо |
| CurrentTickets |  | Количество | Sum | Region, ConfigurationName | Применимо |
| DesiredInstances | Целевое количество активных экземпляров, которое GameLift стремится поддерживать во флоте | Количество | Multi | FleetId |  |
| FirstChoiceNotViable | Игровые сессии, успешно размещённые, но не во флоте первого выбора, поскольку этот флот не считается жизнеспособным (например, spot-флот с высокой частотой прерываний) | Количество в минуту | Multi | Region |  |
| FirstChoiceNotViable |  | Количество в минуту | Multi | Region, QueueName |  |
| FirstChoiceNotViable |  | Количество в минуту | Sum | Region |  |
| FirstChoiceNotViable |  | Количество в минуту | Sum | Region, QueueName |  |
| FirstChoiceOutOfCapacity | Игровые сессии, успешно размещённые, но не во флоте первого выбора, поскольку у этого флота нет доступных ресурсов | Количество в минуту | Multi | Region | Применимо |
| FirstChoiceOutOfCapacity |  | Количество в минуту | Multi | Region, QueueName | Применимо |
| FirstChoiceOutOfCapacity |  | Количество в минуту | Sum | Region | Применимо |
| FirstChoiceOutOfCapacity |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| GameSessionInterruptions | Количество игровых сессий на spot-экземплярах, которые были прерваны | Количество в минуту | Multi | FleetId |  |
| GameSessionInterruptions |  | Количество в минуту | Multi | Region, MetricGroups |  |
| GameSessionInterruptions |  | Количество в минуту | Sum | FleetId |  |
| GameSessionInterruptions |  | Количество в минуту | Sum | Region, MetricGroups |  |
| HealthyServerProcesses | Активные серверные процессы, сообщающие об исправном состоянии | Количество | Multi | FleetId | Применимо |
| HealthyServerProcesses |  | Количество | Multi | Region, MetricGroups | Применимо |
| IdleInstances | Активные экземпляры, которые в настоящее время обслуживают ноль (0) игровых сессий. Эта метрика измеряет доступную, но неиспользуемую ёмкость. | Количество | Multi | FleetId | Применимо |
| IdleInstances |  | Количество | Multi | Region, MetricGroups | Применимо |
| InstanceInterruptions | Количество spot-экземпляров, которые были прерваны | Количество в минуту | Multi | FleetId |  |
| InstanceInterruptions |  | Количество в минуту | Multi | Region, MetricGroups |  |
| InstanceInterruptions |  | Количество в минуту | Sum | FleetId |  |
| InstanceInterruptions |  | Количество в минуту | Sum | Region, MetricGroups |  |
| LowestLatencyPlacement | Игровые сессии, успешно размещённые в регионе, который обеспечивает наименьшую возможную задержку очереди для игроков | Количество в минуту | Multi | Region | Применимо |
| LowestLatencyPlacement |  | Количество в минуту | Multi | Region, QueueName | Применимо |
| LowestLatencyPlacement |  | Количество в минуту | Sum | Region | Применимо |
| LowestLatencyPlacement |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| LowestPricePlacement | Игровые сессии, успешно размещённые во флоте с наименьшей возможной ценой очереди для выбранного региона | Количество в минуту | Multi | Region |  |
| LowestPricePlacement |  | Количество в минуту | Multi | Region, QueueName |  |
| LowestPricePlacement |  | Количество в минуту | Sum | Region |  |
| LowestPricePlacement |  | Количество в минуту | Sum | Region, QueueName |  |
| MatchAcceptancesTimedOut | Для конфигураций подбора игроков, требующих принятия, потенциальные матчи, время ожидания которых истекло во время принятия с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| MatchesAccepted | Для конфигураций подбора игроков, требующих принятия, потенциальные матчи, принятые с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| MatchesCreated | Потенциальные матчи, созданные с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| MatchesPlaced | Матчи, успешно размещённые в игровой сессии с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| MatchesRejected | Для конфигураций подбора игроков, требующих принятия, потенциальные матчи, отклонённые хотя бы одним игроком с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| MaxInstances | Максимальное количество экземпляров, разрешённое для флота | Количество | Multi | FleetId |  |
| MinInstances | Минимальное количество экземпляров, разрешённое для флота | Количество | Multi | FleetId |  |
| PercentAvailableGameSessions | Процент слотов игровых сессий на всех активных серверных процессах (исправных или неисправных), которые в настоящее время не используются (рассчитывается как `AvailableGameSessions` / [`ActiveGameSessions` + `AvailableGameSessions` + неисправные серверные процессы]) | Процент | Average | FleetId | Применимо |
| PercentAvailableGameSessions |  | Процент | Average | Region, MetricGroups | Применимо |
| PercentHealthyServerProcesses | Процент всех активных серверных процессов, сообщающих об исправном состоянии (рассчитывается как `HealthyServerProcesses` / `ActiveServerProcesses`) | Процент | Multi | FleetId | Применимо |
| PercentHealthyServerProcesses |  | Процент | Multi | Region, MetricGroups | Применимо |
| PercentIdleInstances | Процент всех активных экземпляров, простаивающих (рассчитывается как `IdleInstances` / `ActiveInstances`) | Процент | Multi | FleetId | Применимо |
| PercentIdleInstances |  | Процент | Multi | Region, MetricGroups | Применимо |
| PlacementsCanceled | Запросы на размещение игровых сессий, отменённые до истечения времени ожидания, с момента последнего отчёта | Количество в минуту | Multi | Region, QueueName | Применимо |
| PlacementsCanceled |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| PlacementsFailed | Запросы на размещение игровых сессий, завершившиеся неудачно по любой причине, с момента последнего отчёта | Количество в минуту | Multi | Region, QueueName | Применимо |
| PlacementsFailed |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| PlacementsStarted | Новые запросы на размещение игровых сессий, добавленные в очередь с момента последнего отчёта | Количество в минуту | Multi | Region, QueueName | Применимо |
| PlacementsStarted |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| PlacementsSucceeded | Запросы на размещение игровых сессий, приведшие к созданию новой игровой сессии, с момента последнего отчёта | Количество в минуту | Multi | Region, QueueName | Применимо |
| PlacementsSucceeded |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| PlacementsTimedOut | Запросы на размещение игровых сессий, достигшие предела времени ожидания очереди без выполнения, с момента последнего отчёта | Количество в минуту | Multi | Region, QueueName | Применимо |
| PlacementsTimedOut |  | Количество в минуту | Sum | Region, QueueName | Применимо |
| PlayerSessionActivations | Сессии игроков, перешедшие из статуса `Reserved` в `Active` с момента последнего отчёта | Количество в минуту | Multi | FleetId | Применимо |
| PlayerSessionActivations |  | Количество в минуту | Multi | Region, MetricGroups | Применимо |
| PlayerSessionActivations |  | Количество в минуту | Sum | FleetId | Применимо |
| PlayerSessionActivations |  | Количество в минуту | Sum | Region, MetricGroups | Применимо |
| PlayersStarted | Игроки в тикетах подбора игроков, добавленные с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| QueueDepth | Количество запросов на размещение игровых сессий в очереди со статусом `Pending` | Количество | Multi | Region, QueueName | Применимо |
| QueueDepth |  | Количество | Sum | Region, QueueName | Применимо |
| ServerProcessAbnormalTerminations | Серверные процессы, остановленные из-за нештатных обстоятельств, с момента последнего отчёта | Количество в минуту | Multi | FleetId | Применимо |
| ServerProcessAbnormalTerminations |  | Количество в минуту | Sum | FleetId | Применимо |
| ServerProcessAbnormalTerminations |  | Количество в минуту | Multi | Region, MetricGroups | Применимо |
| ServerProcessAbnormalTerminations |  | Количество в минуту | Sum | Region, MetricGroups | Применимо |
| ServerProcessActivations | Серверные процессы, успешно перешедшие из статуса `Activating` в `Active` с момента последнего отчёта | Количество в минуту | Multi | FleetId | Применимо |
| ServerProcessActivations |  | Количество в минуту | Sum | FleetId | Применимо |
| ServerProcessActivations |  | Количество в минуту | Multi | Region, MetricGroups | Применимо |
| ServerProcessActivations |  | Количество в минуту | Sum | Region, MetricGroups | Применимо |
| ServerProcessTerminations | Серверные процессы, остановленные с момента последнего отчёта | Количество в минуту | Multi | FleetId | Применимо |
| ServerProcessTerminations |  | Количество в минуту | Sum | FleetId | Применимо |
| ServerProcessTerminations |  | Количество в минуту | Multi | Region, MetricGroups | Применимо |
| ServerProcessTerminations |  | Количество в минуту | Sum | Region, MetricGroups | Применимо |
| TicketsFailed | Запросы на подбор игроков, завершившиеся неудачно, с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| TicketsStarted | Новые запросы на подбор игроков, созданные с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| TicketsTimedOut | Запросы на подбор игроков, достигшие предела времени ожидания, с момента последнего отчёта | Количество в минуту | Sum | Region, ConfigurationName | Применимо |
| TimeToMatch | Для запросов на подбор игроков, помещённых в потенциальный матч до последнего отчёта, время между созданием тикета и созданием потенциального матча | Секунда | Multi | Region, ConfigurationName | Применимо |
| TimeToTicketCancel | Для запросов на подбор игроков, отменённых до последнего отчёта, время между созданием тикета и отменой | Секунда | Multi | Region, ConfigurationName | Применимо |
| TimeToTicketSuccess | Для запросов на подбор игроков, успешно выполненных до последнего отчёта, время между созданием тикета и успешным размещением матча | Секунда | Multi | Region, ConfigurationName | Применимо |