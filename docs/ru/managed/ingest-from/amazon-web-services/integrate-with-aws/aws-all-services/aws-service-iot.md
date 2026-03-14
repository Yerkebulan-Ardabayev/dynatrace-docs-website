---
title: Мониторинг AWS IoT
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot
scraped: 2026-03-06T21:35:39.490747
---

# Мониторинг AWS IoT


* Classic
* Практическое руководство
* Чтение: 10 мин
* Опубликовано Oct 16, 2020

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая AWS IoT. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга данного сервиса вам необходимо

* ActiveGate версии 1.181+, а именно:

  + Для развертываний Dynatrace SaaS вам потребуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") так и [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) развертывании) вам потребуется [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.182+
* Обновленная [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#aws-policy-and-authentication "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.  
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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса список дополнительных разрешений, специфичных для этого сервиса.

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

Пример политики JSON для одного отдельного сервиса.

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

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace либо на **странице обзора пользовательского устройства**, либо на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Вы также можете просматривать метрики в веб-интерфейсе Dynatrace на панелях мониторинга. Для данного сервиса предустановленная панель мониторинга недоступна, но вы можете [создать собственную панель мониторинга](../../../../../analyze-explore-automate/dashboards-classic/dashboards/create-dashboards.md "Узнайте, как создавать и редактировать панели мониторинга Dynatrace.").

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

## Доступные метрики

| Название | Описание | Статистика | Единица | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| CanceledJobExecutionCount | Количество выполнений заданий, статус которых изменился на `CANCELED` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| CanceledJobExecutionTotalCount | Общее количество выполнений заданий со статусом `CANCELED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| ClientError | Количество клиентских ошибок, возникших при выполнении задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| Connect.AuthError | Количество запросов на подключение, которые не удалось авторизовать брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Count | Sum | Region, Protocol |  |
| Connect.ClientError | Количество запросов на подключение, отклонённых из-за несоответствия сообщения MQTT требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Count | Sum | Region, Protocol |  |
| Connect.ServerError | Количество запросов на подключение, завершившихся неудачей из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Count | Sum | Region, Protocol |  |
| Connect.Success | Количество успешных подключений к брокеру сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Count | Sum | Region, Protocol | Доступна |
| Connect.Throttle | Количество запросов на подключение, ограниченных из-за превышения допустимой частоты запросов на подключение для учётной записи. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Count | Sum | Region, Protocol |  |
| DeleteThingShadow.Accepted | Количество успешно обработанных запросов `DeleteThingShadow`. Измерение `Protocol` содержит протокол, использованный для выполнения запроса. | Count | Sum | Region, Protocol |  |
| FailedJobExecutionCount | Количество выполнений заданий, статус которых изменился на `FAILED` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| FailedJobExecutionTotalCount | Общее количество выполнений заданий со статусом `FAILED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| Failure | Количество неудачных вызовов действий правил. Измерение `RuleName` содержит имя правила, определяющего действие. Измерение `ActionType` содержит тип вызванного действия. | Count | Sum | Region, RuleName, ActionType |  |
| GetThingShadow.Accepted | Количество успешно обработанных запросов `GetThingShadow`. Измерение `Protocol` содержит протокол, использованный для выполнения запроса. | Count | Sum | Region, Protocol |  |
| InProgressJobExecutionCount | Количество выполнений заданий, статус которых изменился на `IN_PROGRESS` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| InProgressJobExecutionTotalCount | Общее количество выполнений заданий со статусом `IN_PROGRESS` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| NumLogBatchesFailedToPublishThrottled | Единичный пакет событий журнала, публикация которого не удалась из-за ошибок ограничения скорости | Count | Sum | Region |  |
| NumLogEventsFailedToPublishThrottled | Количество событий журнала в пакете, публикация которых не удалась из-за ошибок ограничения скорости | Count | Sum | Region |  |
| ParseError | Количество ошибок разбора JSON, произошедших в сообщениях, опубликованных в топике, на который подписано правило. Измерение `RuleName` содержит имя правила. | Count | Sum | Region, RuleName |  |
| Ping.Success | Количество ping-сообщений, полученных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки ping-сообщения. | Count | Sum | Region, Protocol |  |
| PublishIn.AuthError | Количество запросов на публикацию, которые брокер сообщений не смог авторизовать. Измерение `Protocol` содержит протокол, использованный для публикации сообщения. | Count | Sum | Region, Protocol |  |
| PublishIn.ClientError | Количество запросов на публикацию, отклонённых брокером сообщений из-за несоответствия требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для публикации сообщения. | Count | Sum | Region, Protocol |  |
| PublishIn.ServerError | Количество запросов на публикацию, которые брокер сообщений не смог обработать из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Count | Sum | Region, Protocol |  |
| PublishIn.Success | Количество запросов на публикацию, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Count | Sum | Region, Protocol | Доступна |
| PublishIn.Throttle | Количество запросов на публикацию, ограниченных из-за превышения клиентом допустимой частоты входящих сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Count | Sum | Region, Protocol |  |
| PublishOut.AuthError | Количество запросов на публикацию, выполненных брокером сообщений, которые не удалось авторизовать в AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Count | Sum | Region, Protocol |  |
| PublishOut.ClientError | Количество запросов на публикацию, выполненных брокером сообщений, которые были отклонены из-за несоответствия требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Count | Sum | Region, Protocol |  |
| PublishOut.Success | Количество запросов на публикацию, успешно выполненных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Count | Sum | Region, Protocol |  |
| QueuedJobExecutionCount | Количество выполнений заданий, статус которых изменился на `QUEUED` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| QueuedJobExecutionTotalCount | Общее количество выполнений заданий со статусом `QUEUED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| RejectedJobExecutionCount | Количество выполнений заданий, статус которых изменился на `REJECTED` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| RejectedJobExecutionTotalCount | Общее количество выполнений заданий со статусом `REJECTED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| RemovedJobExecutionCount | Количество выполнений заданий, статус которых изменился на `REMOVED` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| RemovedJobExecutionTotalCount | Общее количество выполнений заданий со статусом `REMOVED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| RuleMessageThrottled | Количество сообщений, ограниченных механизмом правил из-за вредоносного поведения или превышения лимита ограничения скорости механизма правил. Измерение `RuleName` содержит имя правила, которое должно быть активировано. | Count | Sum | Region, RuleName |  |
| RuleNotFound | Правило, которое должно быть активировано, не найдено. Измерение `RuleName` содержит имя правила. | Count | Sum | Region, RuleName |  |
| RulesExecuted | Количество выполненных правил AWS IoT | Count | Sum | Region | Доступна |
| ServerError | Количество запросов на подключение, завершившихся неудачей из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Count | Sum | Region, JobId |  |
| Subscribe.AuthError | Количество запросов на подписку от клиента, которые не удалось авторизовать. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| Subscribe.ClientError | Количество запросов на подписку, отклонённых из-за несоответствия сообщения `SUBSCRIBE` требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| Subscribe.ServerError | Количество запросов на подписку, отклонённых из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| Subscribe.Success | Количество запросов на подписку, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Count | Sum | Region, Protocol | Доступна |
| Subscribe.Throttle | Количество запросов на подписку, ограниченных из-за превышения клиентом допустимой частоты запросов на подписку. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| SuccededJobExecutionCount | Количество выполнений заданий, статус которых изменился на `SUCCESS` за период времени, определяемый CloudWatch. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| SuccededJobExecutionTotalCount | Общее количество выполнений заданий со статусом `SUCCESS` для данного задания. Измерение `JobId` содержит идентификатор задания. | Count | Sum | Region, JobId |  |
| Success | Количество успешных вызовов действий правил. Измерение `RuleName` содержит имя правила, определяющего действие. Измерение `ActionType` содержит тип вызванного действия. | Count | Sum | Region, RuleName, ActionType |  |
| TopicMatch | Количество входящих сообщений, опубликованных в топике, на который подписано правило. Измерение `RuleName` содержит имя правила. | Count | Sum | Region, RuleName |  |
| Unsubscribe.ClientError | Количество запросов на отписку, отклонённых из-за несоответствия сообщения `UNSUBSCRIBE` требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| Unsubscribe.ServerError | Количество запросов на отписку, отклонённых из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| Unsubscribe.Success | Количество запросов на отписку, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| Unsubscribe.Throttle | Количество запросов на отписку, отклонённых из-за превышения клиентом допустимой частоты запросов на отписку. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Count | Sum | Region, Protocol |  |
| UpdateThingShadow.Accepted | Количество успешно обработанных запросов `UpdateThingShadow`. Измерение `Protocol` содержит протокол, использованный для выполнения запроса. | Count | Sum | Region, Protocol |  |