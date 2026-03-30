---
title: Мониторинг Amazon Textract
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-textract
scraped: 2026-03-04T21:37:25.706615
---

Dynatrace собирает метрики для множества предварительно выбранных пространств имен, включая Amazon Textract. Вы можете просматривать графики для каждого экземпляра сервиса с набором измерений и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate версии 1.197+

  + Для развертываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании SaaS, так и в [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) необходим Environment ActiveGate, установленный на хосте Amazon EC2.
* Dynatrace версии 1.203+
* Обновленная политика мониторинга AWS для включения дополнительных сервисов AWS.
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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения для определенных сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для всех облачных сервисов AWS, а также для каждого поддерживаемого сервиса список дополнительных разрешений, специфичных для этого сервиса.

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

Ниже приведен пример JSON-политики для одного сервиса.

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

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг на странице **Dashboards** автоматически появляется предустановленный дашборд, содержащий все рекомендуемые метрики. Для поиска конкретных дашбордов отфильтруйте по **Preset**, а затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учетных данных, чтобы предустановленный дашборд появился на странице **Dashboards**. Для повторного сохранения учетных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.

Чтобы убрать дашборд со страницы дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | Недоступен |
| AWS Lambda (built-in) | Недоступен |
| Amazon Application and Network Load Balancer (built-in) | Недоступен |
| Amazon DynamoDB (built-in) | Недоступен |
| Amazon EBS (built-in) | Недоступен |
| Amazon EC2 (built-in) | Недоступен |
| Amazon Elastic Load Balancer (ELB) (built-in) | Недоступен |
| Amazon RDS (built-in) | Недоступен |
| Amazon S3 (built-in) | Недоступен |
| AWS Certificate Manager Private Certificate Authority | Недоступен |
| All monitored Amazon services | Недоступен |
| Amazon API Gateway | Недоступен |
| AWS App Runner | Недоступен |
| Amazon AppStream | Доступен |
| AWS AppSync | Доступен |
| Amazon Athena | Доступен |
| Amazon Aurora | Недоступен |
| Amazon EC2 Auto Scaling | Доступен |
| AWS Billing | Доступен |
| Amazon Keyspaces | Доступен |
| AWS Chatbot | Доступен |
| Amazon CloudFront | Недоступен |
| AWS CloudHSM | Доступен |
| Amazon CloudSearch | Доступен |
| AWS CodeBuild | Доступен |
| Amazon Cognito | Недоступен |
| Amazon Connect | Доступен |
| AWS DataSync | Доступен |
| Amazon DynamoDB Accelerator (DAX) | Доступен |
| AWS Database Migration Service (AWS DMS) | Доступен |
| Amazon DocumentDB | Доступен |
| AWS Direct Connect | Доступен |
| Amazon DynamoDB | Недоступен |
| Amazon EBS | Недоступен |
| Amazon EC2 Spot Fleet | Недоступен |
| Amazon EC2 API | Доступен |
| Amazon Elastic Container Service (ECS) | Недоступен |
| Amazon ECS Container Insights | Доступен |
| Amazon Elastic File System (EFS) | Недоступен |
| Amazon Elastic Kubernetes Service (EKS) | Доступен |
| Amazon ElastiCache (EC) | Недоступен |
| AWS Elastic Beanstalk | Доступен |
| Amazon Elastic Inference | Доступен |
| Amazon Elastic Transcoder | Доступен |
| Amazon Elastic Map Reduce (EMR) | Недоступен |
| Amazon Elasticsearch Service (ES) | Недоступен |
| Amazon EventBridge | Доступен |
| Amazon FSx | Доступен |
| Amazon GameLift | Доступен |
| AWS Glue | Недоступен |
| Amazon Inspector | Доступен |
| AWS Internet of Things (IoT) | Недоступен |
| AWS IoT Things Graph | Доступен |
| AWS IoT Analytics | Доступен |
| Amazon Managed Streaming for Kafka | Доступен |
| Amazon Kinesis Data Analytics | Недоступен |
| Amazon Data Firehose | Недоступен |
| Amazon Kinesis Data Streams | Недоступен |
| Amazon Kinesis Video Streams | Недоступен |
| AWS Lambda | Недоступен |
| Amazon Lex | Доступен |
| Amazon CloudWatch Logs | Доступен |
| AWS Elemental MediaTailor | Доступен |
| AWS Elemental MediaConnect | Доступен |
| AWS Elemental MediaConvert | Доступен |
| AWS Elemental MediaPackage Live | Доступен |
| AWS Elemental MediaPackage Video on Demand | Доступен |
| Amazon MQ | Доступен |
| Amazon VPC NAT Gateways | Недоступен |
| Amazon Neptune | Доступен |
| AWS OpsWorks | Доступен |
| Amazon Polly | Доступен |
| Amazon QLDB | Доступен |
| Amazon RDS | Недоступен |
| Amazon Redshift | Недоступен |
| Amazon Rekognition | Доступен |
| AWS RoboMaker | Доступен |
| Amazon Route 53 | Доступен |
| Amazon Route 53 Resolver | Доступен |
| Amazon S3 | Недоступен |
| Amazon SageMaker Batch Transform Jobs | Недоступен |
| Amazon SageMaker Endpoints | Недоступен |
| Amazon SageMaker Endpoint Instances | Недоступен |
| Amazon SageMaker Ground Truth | Недоступен |
| Amazon SageMaker Processing Jobs | Недоступен |
| Amazon SageMaker Training Jobs | Недоступен |
| AWS Service Catalog | Доступен |
| Amazon Simple Email Service (SES) | Недоступен |
| Amazon Simple Notification Service (SNS) | Недоступен |
| Amazon Simple Queue Service (SQS) | Недоступен |
| AWS Systems Manager - Run Command | Доступен |
| AWS Step Functions | Доступен |
| AWS Storage Gateway | Доступен |
| Amazon SWF | Доступен |
| Amazon Textract | Доступен |
| AWS Transfer Family | Доступен |
| AWS Transit Gateway | Доступен |
| Amazon Translate | Доступен |
| AWS Trusted Advisor | Доступен |
| AWS API Usage | Доступен |
| AWS Site-to-Site VPN | Доступен |
| AWS WAF Classic | Доступен |
| AWS WAF | Доступен |
| Amazon WorkMail | Доступен |
| Amazon WorkSpaces | Доступен |

![Textract-dash](https://dt-cdn.net/images/dashboard-2-1975-bd1bc93f1e.png)

## Доступные метрики

| Название | Описание | Единица измерения | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| ResponseTime | Время в миллисекундах, затраченное Amazon Textract на вычисление ответа | Milliseconds | Average | Region, Operation | Доступна |
| ResponseTime |  | Count | Count | Region, Operation |  |
| ServerErrorCount | Количество серверных ошибок | Count | Average | Region, Operation |  |
| ServerErrorCount |  | Count | Sum | Region, Operation | Доступна |
| SuccessfulRequestCount | Количество успешных запросов | Count | Average | Region, Operation |  |
| SuccessfulRequestCount |  | Count | Sum | Region, Operation | Доступна |
| ThrottledCount | Количество ограниченных запросов | Count | Average | Region, Operation |  |
| ThrottledCount |  | Count | Sum | Region, Operation | Доступна |
| UserErrorCount | Количество пользовательских ошибок (недопустимые параметры, недопустимое изображение, отсутствие разрешений и т.д.) | Count | Average | Region, Operation |  |
| UserErrorCount |  | Count | Sum | Region, Operation | Доступна |

## Ограничения

Поскольку Amazon Textract предоставляет API для оптического распознавания символов (OCR), **главное измерение** отсутствует.