---
title: Мониторинг Amazon EMR (Elastic MapReduce)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-mapreduce-emr
scraped: 2026-05-12T11:31:00.831781
---

# Мониторинг Amazon EMR (Elastic MapReduce)

# Мониторинг Amazon EMR (Elastic MapReduce)

* Практическое руководство
* Чтение: 12 мин
* Опубликовано 15 октября 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon EMR. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

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

Основное измерение: `JobFlowId`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| AppsCompleted | Количество приложений, отправленных в YARN, которые завершились | Количество | Sum | JobFlowId, JobId |  |
| AppsCompleted |  | Количество | Sum | JobFlowId |  |
| AppsFailed | Количество приложений, отправленных в YARN, которые не удалось завершить | Количество | Sum | JobFlowId, JobId |  |
| AppsFailed |  | Количество | Sum | JobFlowId |  |
| AppsKilled | Количество приложений, отправленных в YARN, которые были принудительно завершены | Количество | Sum | JobFlowId, JobId |  |
| AppsKilled |  | Количество | Sum | JobFlowId |  |
| AppsPending | Количество приложений, отправленных в YARN, которые находятся в состоянии ожидания (Pending) | Количество | Sum | JobFlowId, JobId |  |
| AppsPending |  | Количество | Sum | JobFlowId |  |
| AppsRunning | Количество приложений, отправленных в YARN, которые выполняются | Количество | Sum | JobFlowId, JobId | Применимо |
| AppsRunning |  | Количество | Sum | JobFlowId | Применимо |
| AppsSubmitted | Количество приложений, отправленных в YARN | Количество | Sum | JobFlowId, JobId |  |
| AppsSubmitted |  | Количество | Sum | JobFlowId |  |
| BackupFailed | Показывает, завершилось ли последнее резервное копирование неудачей. По умолчанию установлено в `0` и обновляется до `1`, если предыдущая попытка резервного копирования завершилась неудачей. Эта метрика регистрируется только для кластеров HBase. | Количество | Sum | JobFlowId, JobId |  |
| BackupFailed |  | Количество | Sum | JobFlowId |  |
| CapacityRemainingGB | Объём оставшейся дисковой ёмкости HDFS | Количество | Sum | JobFlowId, JobId |  |
| CapacityRemainingGB |  | Количество | Sum | JobFlowId |  |
| ContainerAllocated | Количество контейнеров ресурсов, выделенных менеджером ресурсов | Количество | Sum | JobFlowId, JobId |  |
| ContainerAllocated |  | Количество | Sum | JobFlowId |  |
| ContainerPendingRatio | Соотношение (в числах) ожидающих контейнеров к выделенным контейнерам (`ContainerPendingRatio` = `ContainerPending` / `ContainerAllocated`). Если `ContainerAllocated` = `0`, то `ContainerPendingRatio` = `ContainerPending`. | Количество | Sum | JobFlowId, JobId |  |
| ContainerPendingRatio |  | Количество | Sum | JobFlowId |  |
| ContainerPending | Количество контейнеров в очереди, которые ещё не были выделены | Количество | Sum | JobFlowId, JobId |  |
| ContainerPending |  | Количество | Sum | JobFlowId |  |
| ContainerReserved | Количество зарезервированных контейнеров | Количество | Sum | JobFlowId, JobId |  |
| ContainerReserved |  | Количество | Sum | JobFlowId |  |
| CoreNodesPending | Количество основных узлов, ожидающих назначения (ожидающие запросы) | Количество | Sum | JobFlowId, JobId |  |
| CoreNodesPending |  | Количество | Sum | JobFlowId |  |
| CoreNodesRequested |  | Количество | Sum | JobFlowId, JobId |  |
| CoreNodesRequested |  | Количество | Sum | JobFlowId |  |
| CoreNodesRunning | Количество работающих основных узлов | Количество | Sum | JobFlowId, JobId |  |
| CoreNodesRunning |  | Количество | Sum | JobFlowId |  |
| CoreUnitsRequested |  | Количество | Sum | JobFlowId, JobId |  |
| CoreUnitsRequested |  | Количество | Sum | JobFlowId |  |
| CoreUnitsRunning |  | Количество | Sum | JobFlowId, JobId |  |
| CoreUnitsRunning |  | Количество | Sum | JobFlowId |  |
| CoreVCPURequested |  | Количество | Sum | JobFlowId, JobId |  |
| CoreVCPURequested |  | Количество | Sum | JobFlowId |  |
| CoreVCPURunning |  | Количество | Sum | JobFlowId, JobId |  |
| CoreVCPURunning |  | Количество | Sum | JobFlowId |  |
| CorruptBlocks | Количество блоков, которые HDFS сообщает как повреждённые | Количество | Sum | JobFlowId, JobId |  |
| CorruptBlocks |  | Количество | Sum | JobFlowId |  |
| DfsPendingReplicationBlocks | Состояние репликации блоков: реплицируемые блоки, возраст запросов на репликацию и неуспешные запросы на репликацию | Количество | Sum | JobFlowId, JobId |  |
| DfsPendingReplicationBlocks |  | Количество | Sum | JobFlowId |  |
| HDFSBytesRead | Количество байт, прочитанных из HDFS | Количество | Sum | JobFlowId, JobId |  |
| HDFSBytesRead |  | Количество | Sum | JobFlowId |  |
| HDFSBytesWritten | Количество байт, записанных в HDFS | Количество | Sum | JobFlowId, JobId |  |
| HDFSBytesWritten |  | Количество | Sum | JobFlowId |  |
| HDFSUtilization | Процент хранилища HDFS, используемого в данный момент | Процент | Average | JobFlowId, JobId | Применимо |
| HDFSUtilization |  | Процент | Average | JobFlowId | Применимо |
| HbaseBackupFailed | Показывает, завершилось ли последнее резервное копирование неудачей. По умолчанию установлено в `0` и обновляется до `1`, если предыдущая попытка резервного копирования завершилась неудачей. Эта метрика регистрируется только для кластеров HBase. | Количество | Minimum | JobFlowId, JobId |  |
| HbaseBackupFailed |  | Количество | Minimum | JobFlowId |  |
| IsIdle | Указывает, что кластер больше не выполняет работу, но всё ещё активен и продолжает накапливать расходы. Устанавливается в `1`, если не выполняется ни одна задача и ни одно задание, и в `0` в противном случае. Это значение проверяется с интервалом в пять минут, и значение `1` указывает лишь на то, что кластер простаивал в момент проверки, а не на то, что он простаивал в течение всех пяти минут. | Количество | Minimum | JobFlowId, JobId | Применимо |
| IsIdle |  | Количество | Minimum | JobFlowId | Применимо |
| JobsFailed | Количество заданий в кластере, которые завершились неудачей | Количество | Sum | JobFlowId, JobId |  |
| JobsFailed |  | Количество | Sum | JobFlowId |  |
| JobsRunning | Количество заданий в кластере, которые выполняются в данный момент | Количество | Sum | JobFlowId, JobId |  |
| JobsRunning |  | Количество | Sum | JobFlowId |  |
| LiveDataNodes | Процент узлов данных, получающих работу от Hadoop | Количество | Sum | JobFlowId, JobId |  |
| LiveDataNodes |  | Количество | Sum | JobFlowId |  |
| LiveTaskTrackers | Процент трекеров задач, которые функционируют | Процент | Average | JobFlowId, JobId |  |
| LiveTaskTrackers |  | Процент | Average | JobFlowId |  |
| MRActiveNodes | Количество узлов, на которых в настоящее время выполняются задачи или задания MapReduce. Эквивалентно метрике YARN `mapred.resourcemanager.NoOfActiveNodes` | Количество | Sum | JobFlowId, JobId |  |
| MRActiveNodes |  | Количество | Sum | JobFlowId |  |
| MRDecommissionedNodes | Количество узлов, выделенных приложениям MapReduce, которые были помечены в состояние **Decommissioned** | Количество | Sum | JobFlowId, JobId |  |
| MRDecommissionedNodes |  | Количество | Sum | JobFlowId |  |
| MRLostNodes | Количество узлов, выделенных MapReduce, которые были помечены в состояние **Lost** | Количество | Sum | JobFlowId, JobId |  |
| MRLostNodes |  | Количество | Sum | JobFlowId |  |
| MRRebootedNodes | Количество узлов, доступных MapReduce, которые были перезагружены и помечены в состояние **Rebooted** | Количество | Sum | JobFlowId, JobId |  |
| MRRebootedNodes |  | Количество | Sum | JobFlowId |  |
| MRTotalNodes | Количество узлов, доступных в настоящее время заданиям MapReduce | Количество | Sum | JobFlowId, JobId |  |
| MRTotalNodes |  | Количество | Sum | JobFlowId |  |
| MRUnhealthyNodes | Количество узлов, доступных заданиям MapReduce, помеченных в состояние **Unhealthy** | Количество | Sum | JobFlowId, JobId |  |
| MRUnhealthyNodes |  | Количество | Sum | JobFlowId |  |
| MapSlotsOpen | Неиспользуемая ёмкость задач map. Вычисляется как максимальное количество задач map для данного кластера за вычетом общего количества задач map, выполняющихся в этом кластере в данный момент. | Количество | Sum | JobFlowId, JobId |  |
| MapSlotsOpen |  | Количество | Sum | JobFlowId |  |
| MapTasksRemaining | Количество оставшихся задач map для каждого задания | Количество | Sum | JobFlowId, JobId |  |
| MapTasksRemaining |  | Количество | Sum | JobFlowId |  |
| MapTasksRunning | Количество выполняющихся задач map для каждого задания | Количество | Sum | JobFlowId, JobId | Применимо |
| MapTasksRunning |  | Количество | Sum | JobFlowId | Применимо |
| MemoryAllocatedMB | Объём памяти, выделенной кластеру | Количество | Sum | JobFlowId, JobId |  |
| MemoryAllocatedMB |  | Количество | Sum | JobFlowId |  |
| MemoryAvailableMB | Объём памяти, доступной для выделения | Количество | Sum | JobFlowId, JobId |  |
| MemoryAvailableMB |  | Количество | Sum | JobFlowId |  |
| MemoryReservedMB | Объём памяти, зарезервированной для выделения | Количество | Sum | JobFlowId, JobId |  |
| MemoryReservedMB |  | Количество | Sum | JobFlowId |  |
| MemoryTotalMB | Общий объём памяти в кластере | Количество | Sum | JobFlowId, JobId |  |
| MemoryTotalMB |  | Количество | Sum | JobFlowId |  |
| MissingBlocks | Количество блоков, для которых у HDFS нет реплик. Это могут быть повреждённые блоки. | Количество | Sum | JobFlowId, JobId |  |
| MissingBlocks |  | Количество | Sum | JobFlowId |  |
| MostRecentBackupDuration | Количество времени, которое потребовалось предыдущему резервному копированию для завершения. Эта метрика устанавливается независимо от того, завершилось ли последнее резервное копирование успешно или неудачей. Пока резервное копирование выполняется, эта метрика возвращает количество минут с момента начала резервного копирования. Эта метрика регистрируется только для кластеров HBase. | Количество | Sum | JobFlowId, JobId |  |
| MostRecentBackupDuration |  | Количество | Sum | JobFlowId |  |
| PendingDeletionBlocks | Количество блоков, помеченных для удаления | Количество | Sum | JobFlowId, JobId |  |
| PendingDeletionBlocks |  | Количество | Sum | JobFlowId |  |
| ReduceSlotsOpen | Неиспользуемая ёмкость задач reduce. Вычисляется как максимальная ёмкость задач reduce для данного кластера за вычетом количества задач reduce, выполняющихся в этом кластере в данный момент. | Количество | Sum | JobFlowId, JobId |  |
| ReduceSlotsOpen |  | Количество | Sum | JobFlowId |  |
| ReduceTasksRemaining | Количество оставшихся задач reduce для каждого задания. Если у вас установлен планировщик и выполняется несколько заданий, создаётся несколько графиков. | Количество | Sum | JobFlowId |  |
| ReduceTasksRunning | Количество выполняющихся задач reduce для каждого задания. Если у вас установлен планировщик и выполняется несколько заданий, создаётся несколько графиков. | Количество | Sum | JobFlowId, JobId |  |
| ReduceTasksRunning |  | Количество | Sum | JobFlowId |  |
| RemainingMapTasksPerSlot | Соотношение общего количества оставшихся задач map к общему количеству доступных слотов map в кластере | Процент | Average | JobFlowId, JobId |  |
| RemainingMapTasksPerSlot |  | Процент | Average | JobFlowId |  |
| S3BytesRead | Количество байт, прочитанных из Amazon S3. Эта метрика агрегирует только задания MapReduce и не применяется к другим рабочим нагрузкам в EMR. | Количество | Sum | JobFlowId, JobId |  |
| S3BytesRead |  | Количество | Sum | JobFlowId |  |
| S3BytesWritten | Количество байт, записанных в Amazon S3. Эта метрика агрегирует только задания MapReduce и не применяется к другим рабочим нагрузкам в EMR. | Количество | Sum | JobFlowId, JobId |  |
| S3BytesWritten |  | Количество | Sum | JobFlowId |  |
| TaskNodesPending | Количество узлов задач, ожидающих назначения (ожидающие запросы) | Количество | Sum | JobFlowId, JobId |  |
| TaskNodesPending |  | Количество | Sum | JobFlowId |  |
| TaskNodesRequested |  | Количество | Sum | JobFlowId, JobId |  |
| TaskNodesRequested |  | Количество | Sum | JobFlowId |  |
| TaskNodesRunning | Количество работающих узлов задач | Количество | Sum | JobFlowId, JobId |  |
| TaskNodesRunning |  | Количество | Sum | JobFlowId |  |
| TaskUnitsRequested |  | Количество | Sum | JobFlowId, JobId |  |
| TaskUnitsRequested |  | Количество | Sum | JobFlowId |  |
| TaskUnitsRunning |  | Количество | Sum | JobFlowId, JobId |  |
| TaskUnitsRunning |  | Количество | Sum | JobFlowId |  |
| TaskVCPURequested |  | Количество | Sum | JobFlowId, JobId |  |
| TaskVCPURequested |  | Количество | Sum | JobFlowId |  |
| TaskVCPURunning |  | Количество | Sum | JobFlowId, JobId |  |
| TaskVCPURunning |  | Количество | Sum | JobFlowId |  |
| TimeSinceLastSuccessfulBackup | Количество прошедших минут с момента начала последнего успешного резервного копирования HBase на вашем кластере. Эта метрика регистрируется только для кластеров HBase. | Количество | Sum | JobFlowId, JobId |  |
| TimeSinceLastSuccessfulBackup |  | Количество | Sum | JobFlowId |  |
| TotalLoad | Общее количество одновременных передач данных | Количество | Sum | JobFlowId, JobId |  |
| TotalLoad |  | Количество | Sum | JobFlowId |  |
| TotalNodesRequested |  | Количество | Sum | JobFlowId, JobId |  |
| TotalNodesRequested |  | Количество | Sum | JobFlowId |  |
| TotalNodesRunning |  | Количество | Sum | JobFlowId, JobId |  |
| TotalNodesRunning |  | Количество | Sum | JobFlowId |  |
| TotalUnitsRequested |  | Количество | Sum | JobFlowId, JobId |  |
| TotalUnitsRequested |  | Количество | Sum | JobFlowId |  |
| TotalUnitsRunning |  | Количество | Sum | JobFlowId, JobId |  |
| TotalUnitsRunning |  | Количество | Sum | JobFlowId |  |
| TotalVCPURequested |  | Количество | Sum | JobFlowId |  |
| TotalVCPURunning |  | Количество | Sum | JobFlowId, JobId |  |
| TotalVCPURunning |  | Количество | Sum | JobFlowId |  |
| UnderReplicatedBlocks | Количество блоков, которые необходимо реплицировать один или несколько раз | Количество | Sum | JobFlowId, JobId |  |
| UnderReplicatedBlocks |  | Количество | Sum | JobFlowId |  |
| YARNMemoryAvailablePercentage | Процент оставшейся памяти, доступной для YARN (`YARNMemoryAvailablePercentage` = `MemoryAvailableMB` / `MemoryTotalMB`) | Процент | Average | JobFlowId, JobId |  |
| YARNMemoryAvailablePercentage |  | Процент | Average | JobFlowId |  |