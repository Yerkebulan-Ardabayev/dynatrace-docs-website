---
title: Мониторинг AWS IoT
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot
scraped: 2026-05-12T11:30:52.639805
---

# Мониторинг AWS IoT

# Мониторинг AWS IoT

* Практическое руководство
* Чтение: 10 мин
* Опубликовано 16 октября 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая AWS IoT. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

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

| Имя | Описание | Статистика | Единица измерения | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| CanceledJobExecutionCount | Количество выполнений задания, статус которых изменился на `CANCELED` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| CanceledJobExecutionTotalCount | Общее количество выполнений задания со статусом `CANCELED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| ClientError | Количество клиентских ошибок, возникших при выполнении задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| Connect.AuthError | Количество запросов на подключение, которые не удалось авторизовать брокеру сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Количество | Sum | Region, Protocol |  |
| Connect.ClientError | Количество запросов на подключение, отклонённых из-за того, что сообщение MQTT не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Количество | Sum | Region, Protocol |  |
| Connect.ServerError | Количество запросов на подключение, которые завершились неудачей из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Количество | Sum | Region, Protocol |  |
| Connect.Success | Количество успешных подключений к брокеру сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Количество | Sum | Region, Protocol | Применимо |
| Connect.Throttle | Количество запросов на подключение, подвергнутых регулированию из-за того, что аккаунт превысил допустимую частоту запросов на подключение. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Количество | Sum | Region, Protocol |  |
| DeleteThingShadow.Accepted | Количество запросов `DeleteThingShadow`, обработанных успешно. Измерение `Protocol` содержит протокол, использованный для выполнения запроса. | Количество | Sum | Region, Protocol |  |
| FailedJobExecutionCount | Количество выполнений задания, статус которых изменился на `FAILED` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| FailedJobExecutionTotalCount | Общее количество выполнений задания со статусом `FAILED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| Failure | Количество неуспешных вызовов действий правила. Измерение `RuleName` содержит имя правила, задающего действие. Измерение `ActionType` содержит тип вызванного действия. | Количество | Sum | Region, RuleName, ActionType |  |
| GetThingShadow.Accepted | Количество запросов `GetThingShadow`, обработанных успешно. Измерение `Protocol` содержит протокол, использованный для выполнения запроса. | Количество | Sum | Region, Protocol |  |
| InProgressJobExecutionCount | Количество выполнений задания, статус которых изменился на `IN_PROGRESS` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| InProgressJobExecutionTotalCount | Общее количество выполнений задания со статусом `IN_PROGRESS` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| NumLogBatchesFailedToPublishThrottled | Отдельный пакет событий журнала, который не удалось опубликовать из-за ошибок регулирования | Количество | Sum | Region |  |
| NumLogEventsFailedToPublishThrottled | Количество событий журнала в пакете, которые не удалось опубликовать из-за ошибок регулирования | Количество | Sum | Region |  |
| ParseError | Количество ошибок разбора JSON, возникших в сообщениях, опубликованных в топике, который прослушивает правило. Измерение `RuleName` содержит имя правила. | Количество | Sum | Region, RuleName |  |
| Ping.Success | Количество ping-сообщений, полученных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки ping-сообщения. | Количество | Sum | Region, Protocol |  |
| PublishIn.AuthError | Количество запросов на публикацию, которые брокер сообщений не смог авторизовать. Измерение `Protocol` содержит протокол, использованный для публикации сообщения. | Количество | Sum | Region, Protocol |  |
| PublishIn.ClientError | Количество запросов на публикацию, отклонённых брокером сообщений из-за того, что сообщение не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для публикации сообщения. | Количество | Sum | Region, Protocol |  |
| PublishIn.ServerError | Количество запросов на публикацию, которые брокер сообщений не смог обработать из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Количество | Sum | Region, Protocol |  |
| PublishIn.Success | Количество запросов на публикацию, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Количество | Sum | Region, Protocol | Применимо |
| PublishIn.Throttle | Количество запросов на публикацию, подвергнутых регулированию из-за того, что клиент превысил допустимую частоту входящих сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Количество | Sum | Region, Protocol |  |
| PublishOut.AuthError | Количество запросов на публикацию, сделанных брокером сообщений, которые не удалось авторизовать в AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Количество | Sum | Region, Protocol |  |
| PublishOut.ClientError | Количество запросов на публикацию, сделанных брокером сообщений, которые были отклонены из-за того, что сообщение не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Количество | Sum | Region, Protocol |  |
| PublishOut.Success | Количество запросов на публикацию, успешно сделанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `PUBLISH`. | Количество | Sum | Region, Protocol |  |
| QueuedJobExecutionCount | Количество выполнений задания, статус которых изменился на `QUEUED` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| QueuedJobExecutionTotalCount | Общее количество выполнений задания со статусом `QUEUED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| RejectedJobExecutionCount | Количество выполнений задания, статус которых изменился на `REJECTED` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| RejectedJobExecutionTotalCount | Общее количество выполнений задания со статусом `REJECTED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| RemovedJobExecutionCount | Количество выполнений задания, статус которых изменился на `REMOVED` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| RemovedJobExecutionTotalCount | Общее количество выполнений задания со статусом `REMOVED` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| RuleMessageThrottled | Количество сообщений, подвергнутых регулированию механизмом правил из-за вредоносного поведения или из-за того, что количество сообщений превышает лимит регулирования механизма правил. Измерение `RuleName` содержит имя правила, которое должно быть запущено. | Количество | Sum | Region, RuleName |  |
| RuleNotFound | Не удалось найти правило, которое должно быть запущено. Измерение `RuleName` содержит имя правила. | Количество | Sum | Region, RuleName |  |
| RulesExecuted | Количество выполненных правил AWS IoT | Количество | Sum | Region | Применимо |
| ServerError | Количество запросов на подключение, которые завершились неудачей из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `CONNECT`. | Количество | Sum | Region, JobId |  |
| Subscribe.AuthError | Количество запросов на подписку, сделанных клиентом, которые не удалось авторизовать. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| Subscribe.ClientError | Количество запросов на подписку, отклонённых из-за того, что сообщение `SUBSCRIBE` не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| Subscribe.ServerError | Количество запросов на подписку, отклонённых из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| Subscribe.Success | Количество запросов на подписку, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Количество | Sum | Region, Protocol | Применимо |
| Subscribe.Throttle | Количество запросов на подписку, подвергнутых регулированию из-за того, что клиент превысил допустимую частоту запросов на подписку. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `SUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| SuccededJobExecutionCount | Количество выполнений задания, статус которых изменился на `SUCCESS` в течение периода времени, определяемого CloudWatch. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| SuccededJobExecutionTotalCount | Общее количество выполнений задания со статусом `SUCCESS` для данного задания. Измерение `JobId` содержит идентификатор задания. | Количество | Sum | Region, JobId |  |
| Success | Количество успешных вызовов действий правила. Измерение `RuleName` содержит имя правила, задающего действие. Измерение `ActionType` содержит тип вызванного действия. | Количество | Sum | Region, RuleName, ActionType |  |
| TopicMatch | Количество входящих сообщений, опубликованных в топике, который прослушивает правило. Измерение `RuleName` содержит имя правила. | Количество | Sum | Region, RuleName |  |
| Unsubscribe.ClientError | Количество запросов на отписку, отклонённых из-за того, что сообщение `UNSUBSCRIBE` не соответствовало требованиям, определённым в квотах AWS IoT. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| Unsubscribe.ServerError | Количество запросов на отписку, отклонённых из-за внутренней ошибки. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| Unsubscribe.Success | Количество запросов на отписку, успешно обработанных брокером сообщений. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| Unsubscribe.Throttle | Количество запросов на отписку, отклонённых из-за того, что клиент превысил допустимую частоту запросов на отписку. Измерение `Protocol` содержит протокол, использованный для отправки сообщения `UNSUBSCRIBE`. | Количество | Sum | Region, Protocol |  |
| UpdateThingShadow.Accepted | Количество запросов `UpdateThingShadow`, обработанных успешно. Измерение `Protocol` содержит протокол, использованный для выполнения запроса. | Количество | Sum | Region, Protocol |  |