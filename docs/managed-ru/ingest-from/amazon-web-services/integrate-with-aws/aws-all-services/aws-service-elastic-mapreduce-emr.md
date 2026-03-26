---
title: Мониторинг Amazon EMR (Elastic MapReduce)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-mapreduce-emr
scraped: 2026-03-06T21:33:04.819493
---

Dynatrace принимает метрики для множества предварительно выбранных пространств имен, включая Amazon EMR. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate версии 1.181+, а именно:

  + Для развертываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch."), так и [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) необходим [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.182+
* Обновленная [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#aws-policy-and-authentication "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.
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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определенных сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Мониторинг всех облачных сервисов AWS с помощью Dynatrace и просмотр доступных метрик."), а также для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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
| Amazon EC2 Auto Scaling (встроенный) | `autoscaling:DescribeAutoScalingGroups` |
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
| Amazon DynamoDB (встроенный) | `dynamodb:ListTables`, `dynamodb:ListTagsOfResource` |
| Amazon EBS | `ec2:DescribeVolumes` |
| Amazon EBS (встроенный) | `ec2:DescribeVolumes` |
| Amazon EC2 API |  |
| Amazon EC2 (встроенный) | `ec2:DescribeInstances` |
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
| Amazon Elastic Load Balancer (ELB) (встроенный) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
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
| AWS Lambda (встроенный) | `lambda:ListFunctions`, `lambda:ListTags` |
| Amazon Lex | `lex:GetBots` |
| Amazon Application and Network Load Balancer (встроенный) | `elasticloadbalancing:DescribeInstanceHealth`, `elasticloadbalancing:DescribeListeners`, `elasticloadbalancing:DescribeLoadBalancers`, `elasticloadbalancing:DescribeRules`, `elasticloadbalancing:DescribeTags`, `elasticloadbalancing:DescribeTargetHealth` |
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
| Amazon RDS (встроенный) | `rds:DescribeDBInstances`, `rds:DescribeEvents`, `rds:ListTagsForResource` |
| Amazon Redshift | `redshift:DescribeClusters` |
| Amazon Rekognition |  |
| AWS RoboMaker | `robomaker:ListSimulationJobs` |
| Amazon Route 53 | `route53:ListHostedZones` |
| Amazon Route 53 Resolver | `route53resolver:ListResolverEndpoints` |
| Amazon S3 | `s3:ListAllMyBuckets` |
| Amazon S3 (встроенный) | `s3:ListAllMyBuckets` |
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
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Включение мониторинга AWS в Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

Вы также можете просматривать метрики в веб-интерфейсе Dynatrace на панелях мониторинга. Для этого сервиса нет предустановленной панели мониторинга, но вы можете [создать собственную панель мониторинга](../../../../../analyze-explore-automate/dashboards-classic/dashboards/create-dashboards.md "Узнайте, как создавать и редактировать панели мониторинга Dynatrace.").

Чтобы проверить наличие предустановленных панелей мониторинга для каждого сервиса AWS, см. список ниже.

### Список доступных предустановленных панелей мониторинга

| Сервис AWS | Предустановленная панель мониторинга |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Недоступна |
| AWS Lambda (встроенный) | Недоступна |
| Amazon Application and Network Load Balancer (встроенный) | Недоступна |
| Amazon DynamoDB (встроенный) | Недоступна |
| Amazon EBS (встроенный) | Недоступна |
| Amazon EC2 (встроенный) | Недоступна |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Недоступна |
| Amazon RDS (встроенный) | Недоступна |
| Amazon S3 (встроенный) | Недоступна |
| AWS Certificate Manager Private Certificate Authority | Недоступна |
| Все отслеживаемые сервисы Amazon | Недоступна |
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

`JobFlowId` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| AppsCompleted | Количество приложений, отправленных в YARN, которые завершились | Count | Sum | JobFlowId, JobId |  |
| AppsCompleted |  | Count | Sum | JobFlowId |  |
| AppsFailed | Количество приложений, отправленных в YARN, которые не завершились успешно | Count | Sum | JobFlowId, JobId |  |
| AppsFailed |  | Count | Sum | JobFlowId |  |
| AppsKilled | Количество приложений, отправленных в YARN, которые были принудительно завершены | Count | Sum | JobFlowId, JobId |  |
| AppsKilled |  | Count | Sum | JobFlowId |  |
| AppsPending | Количество приложений, отправленных в YARN, находящихся в состоянии ожидания | Count | Sum | JobFlowId, JobId |  |
| AppsPending |  | Count | Sum | JobFlowId |  |
| AppsRunning | Количество приложений, отправленных в YARN, которые выполняются | Count | Sum | JobFlowId, JobId | Доступна |
| AppsRunning |  | Count | Sum | JobFlowId | Доступна |
| AppsSubmitted | Количество приложений, отправленных в YARN | Count | Sum | JobFlowId, JobId |  |
| AppsSubmitted |  | Count | Sum | JobFlowId |  |
| BackupFailed | Показывает, завершилось ли последнее резервное копирование неудачно. По умолчанию установлено значение `0`, обновляется до `1`, если предыдущая попытка резервного копирования не удалась. Эта метрика доступна только для кластеров HBase. | Count | Sum | JobFlowId, JobId |  |
| BackupFailed |  | Count | Sum | JobFlowId |  |
| CapacityRemainingGB | Оставшаяся емкость диска HDFS | Count | Sum | JobFlowId, JobId |  |
| CapacityRemainingGB |  | Count | Sum | JobFlowId |  |
| ContainerAllocated | Количество контейнеров ресурсов, выделенных менеджером ресурсов | Count | Sum | JobFlowId, JobId |  |
| ContainerAllocated |  | Count | Sum | JobFlowId |  |
| ContainerPendingRatio | Соотношение (в числах) ожидающих контейнеров к выделенным контейнерам (`ContainerPendingRatio` = `ContainerPending` / `ContainerAllocated`). Если `ContainerAllocated` = `0`, то `ContainerPendingRatio` = `ContainerPending`. | Count | Sum | JobFlowId, JobId |  |
| ContainerPendingRatio |  | Count | Sum | JobFlowId |  |
| ContainerPending | Количество контейнеров в очереди, которые еще не были выделены | Count | Sum | JobFlowId, JobId |  |
| ContainerPending |  | Count | Sum | JobFlowId |  |
| ContainerReserved | Количество зарезервированных контейнеров | Count | Sum | JobFlowId, JobId |  |
| ContainerReserved |  | Count | Sum | JobFlowId |  |
| CoreNodesPending | Количество базовых узлов, ожидающих назначения (ожидающие запросы) | Count | Sum | JobFlowId, JobId |  |
| CoreNodesPending |  | Count | Sum | JobFlowId |  |
| CoreNodesRequested |  | Count | Sum | JobFlowId, JobId |  |
| CoreNodesRequested |  | Count | Sum | JobFlowId |  |
| CoreNodesRunning | Количество работающих базовых узлов | Count | Sum | JobFlowId, JobId |  |
| CoreNodesRunning |  | Count | Sum | JobFlowId |  |
| CoreUnitsRequested |  | Count | Sum | JobFlowId, JobId |  |
| CoreUnitsRequested |  | Count | Sum | JobFlowId |  |
| CoreUnitsRunning |  | Count | Sum | JobFlowId, JobId |  |
| CoreUnitsRunning |  | Count | Sum | JobFlowId |  |
| CoreVCPURequested |  | Count | Sum | JobFlowId, JobId |  |
| CoreVCPURequested |  | Count | Sum | JobFlowId |  |
| CoreVCPURunning |  | Count | Sum | JobFlowId, JobId |  |
| CoreVCPURunning |  | Count | Sum | JobFlowId |  |
| CorruptBlocks | Количество блоков, которые HDFS определяет как поврежденные | Count | Sum | JobFlowId, JobId |  |
| CorruptBlocks |  | Count | Sum | JobFlowId |  |
| DfsPendingReplicationBlocks | Состояние репликации блоков: блоки, находящиеся в процессе репликации, возраст запросов на репликацию и неудачные запросы на репликацию | Count | Sum | JobFlowId, JobId |  |
| DfsPendingReplicationBlocks |  | Count | Sum | JobFlowId |  |
| HDFSBytesRead | Количество байт, прочитанных из HDFS | Count | Sum | JobFlowId, JobId |  |
| HDFSBytesRead |  | Count | Sum | JobFlowId |  |
| HDFSBytesWritten | Количество байт, записанных в HDFS | Count | Sum | JobFlowId, JobId |  |
| HDFSBytesWritten |  | Count | Sum | JobFlowId |  |
| HDFSUtilization | Процент используемого хранилища HDFS | Percent | Average | JobFlowId, JobId | Доступна |
| HDFSUtilization |  | Percent | Average | JobFlowId | Доступна |
| HbaseBackupFailed | Показывает, завершилось ли последнее резервное копирование неудачно. По умолчанию установлено значение `0`, обновляется до `1`, если предыдущая попытка резервного копирования не удалась. Эта метрика доступна только для кластеров HBase. | Count | Minimum | JobFlowId, JobId |  |
| HbaseBackupFailed |  | Count | Minimum | JobFlowId |  |
| IsIdle | Указывает, что кластер больше не выполняет работу, но все еще активен и начисляет плату. Устанавливается в `1`, если нет запущенных задач и заданий, и в `0` в противном случае. Это значение проверяется каждые пять минут, и значение `1` означает лишь то, что кластер был неактивен на момент проверки, а не то, что он был неактивен все пять минут. | Count | Minimum | JobFlowId, JobId | Доступна |
| IsIdle |  | Count | Minimum | JobFlowId | Доступна |
| JobsFailed | Количество заданий в кластере, которые завершились неудачно | Count | Sum | JobFlowId, JobId |  |
| JobsFailed |  | Count | Sum | JobFlowId |  |
| JobsRunning | Количество заданий в кластере, которые выполняются в данный момент | Count | Sum | JobFlowId, JobId |  |
| JobsRunning |  | Count | Sum | JobFlowId |  |
| LiveDataNodes | Процент узлов данных, получающих работу от Hadoop | Count | Sum | JobFlowId, JobId |  |
| LiveDataNodes |  | Count | Sum | JobFlowId |  |
| LiveTaskTrackers | Процент функционирующих трекеров задач | Percent | Average | JobFlowId, JobId |  |
| LiveTaskTrackers |  | Percent | Average | JobFlowId |  |
| MRActiveNodes | Количество узлов, выполняющих задачи или задания MapReduce. Эквивалентно метрике YARN `mapred.resourcemanager.NoOfActiveNodes` | Count | Sum | JobFlowId, JobId |  |
| MRActiveNodes |  | Count | Sum | JobFlowId |  |
| MRDecommissionedNodes | Количество узлов, выделенных для приложений MapReduce, которые были помечены состоянием **Decommissioned** | Count | Sum | JobFlowId, JobId |  |
| MRDecommissionedNodes |  | Count | Sum | JobFlowId |  |
| MRLostNodes | Количество узлов, выделенных для MapReduce, которые были помечены состоянием **Lost** | Count | Sum | JobFlowId, JobId |  |
| MRLostNodes |  | Count | Sum | JobFlowId |  |
| MRRebootedNodes | Количество узлов, доступных для MapReduce, которые были перезагружены и помечены состоянием **Rebooted** | Count | Sum | JobFlowId, JobId |  |
| MRRebootedNodes |  | Count | Sum | JobFlowId |  |
| MRTotalNodes | Количество узлов, доступных для заданий MapReduce в данный момент | Count | Sum | JobFlowId, JobId |  |
| MRTotalNodes |  | Count | Sum | JobFlowId |  |
| MRUnhealthyNodes | Количество узлов, доступных для заданий MapReduce, помеченных состоянием **Unhealthy** | Count | Sum | JobFlowId, JobId |  |
| MRUnhealthyNodes |  | Count | Sum | JobFlowId |  |
| MapSlotsOpen | Неиспользуемая емкость задач map. Вычисляется как максимальное количество задач map для данного кластера за вычетом общего количества задач map, выполняющихся в данный момент. | Count | Sum | JobFlowId, JobId |  |
| MapSlotsOpen |  | Count | Sum | JobFlowId |  |
| MapTasksRemaining | Количество оставшихся задач map для каждого задания | Count | Sum | JobFlowId, JobId |  |
| MapTasksRemaining |  | Count | Sum | JobFlowId |  |
| MapTasksRunning | Количество выполняющихся задач map для каждого задания | Count | Sum | JobFlowId, JobId | Доступна |
| MapTasksRunning |  | Count | Sum | JobFlowId | Доступна |
| MemoryAllocatedMB | Объем памяти, выделенной кластеру | Count | Sum | JobFlowId, JobId |  |
| MemoryAllocatedMB |  | Count | Sum | JobFlowId |  |
| MemoryAvailableMB | Объем памяти, доступной для выделения | Count | Sum | JobFlowId, JobId |  |
| MemoryAvailableMB |  | Count | Sum | JobFlowId |  |
| MemoryReservedMB | Объем зарезервированной памяти | Count | Sum | JobFlowId, JobId |  |
| MemoryReservedMB |  | Count | Sum | JobFlowId |  |
| MemoryTotalMB | Общий объем памяти в кластере | Count | Sum | JobFlowId, JobId |  |
| MemoryTotalMB |  | Count | Sum | JobFlowId |  |
| MissingBlocks | Количество блоков, для которых HDFS не имеет реплик. Возможно, это поврежденные блоки. | Count | Sum | JobFlowId, JobId |  |
| MissingBlocks |  | Count | Sum | JobFlowId |  |
| MostRecentBackupDuration | Время, затраченное на выполнение предыдущего резервного копирования. Эта метрика устанавливается независимо от того, было ли последнее завершенное резервное копирование успешным или нет. Во время выполнения резервного копирования эта метрика возвращает количество минут с момента начала. Эта метрика доступна только для кластеров HBase. | Count | Sum | JobFlowId, JobId |  |
| MostRecentBackupDuration |  | Count | Sum | JobFlowId |  |
| PendingDeletionBlocks | Количество блоков, помеченных для удаления | Count | Sum | JobFlowId, JobId |  |
| PendingDeletionBlocks |  | Count | Sum | JobFlowId |  |
| ReduceSlotsOpen | Неиспользуемая емкость задач reduce. Вычисляется как максимальная емкость задач reduce для данного кластера за вычетом количества задач reduce, выполняющихся в данный момент. | Count | Sum | JobFlowId, JobId |  |
| ReduceSlotsOpen |  | Count | Sum | JobFlowId |  |
| ReduceTasksRemaining | Количество оставшихся задач reduce для каждого задания. Если установлен планировщик и выполняется несколько заданий, генерируются несколько графиков. | Count | Sum | JobFlowId |  |
| ReduceTasksRunning | Количество выполняющихся задач reduce для каждого задания. Если установлен планировщик и выполняется несколько заданий, генерируются несколько графиков. | Count | Sum | JobFlowId, JobId |  |
| ReduceTasksRunning |  | Count | Sum | JobFlowId |  |
| RemainingMapTasksPerSlot | Соотношение общего количества оставшихся задач map к общему количеству доступных слотов map в кластере | Percent | Average | JobFlowId, JobId |  |
| RemainingMapTasksPerSlot |  | Percent | Average | JobFlowId |  |
| S3BytesRead | Количество байт, прочитанных из Amazon S3. Эта метрика агрегирует только задания MapReduce и не применяется для других рабочих нагрузок на EMR. | Count | Sum | JobFlowId, JobId |  |
| S3BytesRead |  | Count | Sum | JobFlowId |  |
| S3BytesWritten | Количество байт, записанных в Amazon S3. Эта метрика агрегирует только задания MapReduce и не применяется для других рабочих нагрузок на EMR. | Count | Sum | JobFlowId, JobId |  |
| S3BytesWritten |  | Count | Sum | JobFlowId |  |
| TaskNodesPending | Количество вычислительных узлов, ожидающих назначения (ожидающие запросы) | Count | Sum | JobFlowId, JobId |  |
| TaskNodesPending |  | Count | Sum | JobFlowId |  |
| TaskNodesRequested |  | Count | Sum | JobFlowId, JobId |  |
| TaskNodesRequested |  | Count | Sum | JobFlowId |  |
| TaskNodesRunning | Количество работающих вычислительных узлов | Count | Sum | JobFlowId, JobId |  |
| TaskNodesRunning |  | Count | Sum | JobFlowId |  |
| TaskUnitsRequested |  | Count | Sum | JobFlowId, JobId |  |
| TaskUnitsRequested |  | Count | Sum | JobFlowId |  |
| TaskUnitsRunning |  | Count | Sum | JobFlowId, JobId |  |
| TaskUnitsRunning |  | Count | Sum | JobFlowId |  |
| TaskVCPURequested |  | Count | Sum | JobFlowId, JobId |  |
| TaskVCPURequested |  | Count | Sum | JobFlowId |  |
| TaskVCPURunning |  | Count | Sum | JobFlowId, JobId |  |
| TaskVCPURunning |  | Count | Sum | JobFlowId |  |
| TimeSinceLastSuccessfulBackup | Количество прошедших минут с момента начала последнего успешного резервного копирования HBase в вашем кластере. Эта метрика доступна только для кластеров HBase. | Count | Sum | JobFlowId, JobId |  |
| TimeSinceLastSuccessfulBackup |  | Count | Sum | JobFlowId |  |
| TotalLoad | Общее количество одновременных передач данных | Count | Sum | JobFlowId, JobId |  |
| TotalLoad |  | Count | Sum | JobFlowId |  |
| TotalNodesRequested |  | Count | Sum | JobFlowId, JobId |  |
| TotalNodesRequested |  | Count | Sum | JobFlowId |  |
| TotalNodesRunning |  | Count | Sum | JobFlowId, JobId |  |
| TotalNodesRunning |  | Count | Sum | JobFlowId |  |
| TotalUnitsRequested |  | Count | Sum | JobFlowId, JobId |  |
| TotalUnitsRequested |  | Count | Sum | JobFlowId |  |
| TotalUnitsRunning |  | Count | Sum | JobFlowId, JobId |  |
| TotalUnitsRunning |  | Count | Sum | JobFlowId |  |
| TotalVCPURequested |  | Count | Sum | JobFlowId |  |
| TotalVCPURunning |  | Count | Sum | JobFlowId, JobId |  |
| TotalVCPURunning |  | Count | Sum | JobFlowId |  |
| UnderReplicatedBlocks | Количество блоков, которые необходимо реплицировать один или более раз | Count | Sum | JobFlowId, JobId |  |
| UnderReplicatedBlocks |  | Count | Sum | JobFlowId |  |
| YARNMemoryAvailablePercentage | Процент оставшейся памяти, доступной для YARN (`YARNMemoryAvailablePercentage` = `MemoryAvailableMB` / `MemoryTotalMB`) | Percent | Average | JobFlowId, JobId |  |
| YARNMemoryAvailablePercentage |  | Percent | Average | JobFlowId |  |
