---
title: Мониторинг Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-kinesis
scraped: 2026-03-06T21:30:32.569536
---

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая Amazon Kinesis. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга данного сервиса вам необходимо

* ActiveGate версии 1.181+, а именно:

  + Для развертываний Dynatrace SaaS вам потребуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") так и [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) развертывании) вам потребуется [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.182+
* Обновленная [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#aws-policy-and-authentication "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.  
  Для [обновления политики AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

### Amazon Kinesis Data Analytics

`Application` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| Bytes | Количество байт, прочитанных (на входной поток) или записанных (на выходной поток). | Bytes | Sum | Application, Flow, Id | Доступна |
| InputProcessing.DroppedRecords | Количество записей, возвращённых функцией Lambda со статусом `Dropped`. | Count | Sum | Application, Flow, Id |  |
| InputProcessing.Duration | Время, затраченное на каждый вызов функции AWS Lambda, выполненный Kinesis Data Analytics. | Milliseconds | Multi | Application, Flow, Id |  |
| InputProcessing.OkBytes | Сумма байт записей, возвращённых функцией Lambda со статусом `OK`. | Bytes | Sum | Application, Flow, Id |  |
| InputProcessing.OkRecords | Количество записей, возвращённых функцией Lambda со статусом `OK`. | Count | Sum | Application, Flow, Id |  |
| InputProcessing.ProcessingFailedRecords | Количество записей, возвращённых функцией Lambda со статусом `ProcessingFailed`. | Count | Sum | Application, Flow, Id |  |
| InputProcessing.Success | Количество успешных вызовов Lambda, выполненных Kinesis Data Analytics. | Count | Sum | Application, Flow, Id |  |
| KPUs | Количество единиц обработки Kinesis (KPU), используемых для запуска приложения потоковой обработки. | Count | Count | Application |  |
| KPUs |  | Count | Multi | Application |  |
| KPUs |  | Count | Sum | Application | Доступна |
| LambdaDelivery.DeliveryFailedRecords | Количество неудачных вызовов Lambda в Kinesis Data Analytics. | Count | Sum | Application, Flow, Id |  |
| LambdaDelivery.Duration | Время, затраченное на каждый вызов функции Lambda, выполненный Kinesis Data Analytics. | Milliseconds | Multi | Application, Flow, Id |  |
| LambdaDelivery.OkRecords | Количество записей, возвращённых функцией Lambda со статусом `OK`. | Count | Sum | Application, Flow, Id |  |
| MillisBehindLatest | Показывает, насколько приложение отстаёт от текущего времени при чтении из потокового источника. | Milliseconds | Multi | Application; Application, Flow, Id |  |
| Records | Количество записей, прочитанных (на входной поток) или записанных (на выходной поток). | Count | Sum | Application, Flow, Id | Доступна |
| Success | Количество успешных доставок. Каждая успешная попытка доставки в настроенное назначение приложения отмечается значением `1`. Каждая неудачная попытка доставки отмечается значением `0`. | Count | Average | Application, Flow, Id | Доступна |
| backPressuredTimeMsPerSecond | Время (в миллисекундах) противодавления на задачу или оператор в секунду. | Milliseconds | Count | Application |  |
| backPressuredTimeMsPerSecond |  | Milliseconds | Multi | Application |  |
| backPressuredTimeMsPerSecond |  | Milliseconds | Sum | Application |  |
| busyTimeMsPerSecond | Время (в миллисекундах), в течение которого задача или оператор занят (не простаивает и не испытывает противодавления) в секунду. Может быть NaN, если значение не удалось вычислить. | Milliseconds | Count | Application |  |
| busyTimeMsPerSecond |  | Milliseconds | Multi | Application |  |
| busyTimeMsPerSecond |  | Milliseconds | Sum | Application |  |
| bytes\_consumed\_rate | Среднее количество байт, потребляемых в секунду для топика. | Bytes | Count | Application |  |
| bytes\_consumed\_rate |  | Bytes | Multi | Application |  |
| bytes\_consumed\_rate |  | Bytes | Sum | Application |  |
| commitsFailed | Общее количество неудачных фиксаций смещения в Kafka, если фиксация смещений и контрольные точки включены. | Count | Count | Application |  |
| commitsFailed |  | Count | Multi | Application |  |
| commitsFailed |  | Count | Sum | Application |  |
| commitsSucceeded | Общее количество успешных фиксаций смещения в Kafka, если фиксация смещений и контрольные точки включены. | Count | Count | Application |  |
| commitsSucceeded |  | Count | Multi | Application |  |
| commitsSucceeded |  | Count | Sum | Application |  |
| committedOffsets | Последние успешно зафиксированные смещения в Kafka для каждого раздела. Метрику конкретного раздела можно указать по имени топика и идентификатору раздела. | Count | Count | Application |  |
| committedOffsets |  | Count | Multi | Application |  |
| committedOffsets |  | Count | Sum | Application |  |
| containerCPUUtilization | Общий процент использования ЦПУ по всем контейнерам менеджеров задач в кластере приложения Flink. | Percent | Count | Application |  |
| containerCPUUtilization |  | Percent | Multi | Application |  |
| containerCPUUtilization |  | Percent | Sum | Application |  |
| containerDiskUtilization | Общий процент использования диска по всем контейнерам менеджеров задач в кластере приложения Flink. | Percent | Count | Application |  |
| containerDiskUtilization |  | Percent | Multi | Application |  |
| containerDiskUtilization |  | Percent | Sum | Application |  |
| containerMemoryUtilization | Общий процент использования памяти по всем контейнерам менеджеров задач в кластере приложения Flink. | Percent | Count | Application |  |
| containerMemoryUtilization |  | Percent | Multi | Application |  |
| containerMemoryUtilization |  | Percent | Sum | Application |  |
| cpuUtilization | Общий процент использования ЦПУ по всем менеджерам задач. | Percent | Count | Application |  |
| cpuUtilization |  | Percent | Multi | Application |  |
| cpuUtilization |  | Percent | Sum | Application |  |
| currentInputWatermark | Последний водяной знак, полученный этим приложением/оператором/задачей/потоком. | Milliseconds | Count | Application |  |
| currentInputWatermark |  | Milliseconds | Multi | Application |  |
| currentInputWatermark |  | Milliseconds | Sum | Application |  |
| currentOffsets | Текущее смещение чтения потребителя для каждого раздела. Метрику конкретного раздела можно указать по имени топика и идентификатору раздела. | Count | Count | Application |  |
| currentOffsets |  | Count | Multi | Application |  |
| currentOffsets |  | Count | Sum | Application |  |
| currentOutputWatermark | Последний водяной знак, отправленный этим приложением/оператором/задачей/потоком. | Milliseconds | Count | Application |  |
| currentOutputWatermark |  | Milliseconds | Multi | Application |  |
| currentOutputWatermark |  | Milliseconds | Sum | Application |  |
| downtime | Для заданий, находящихся в состоянии сбоя/восстановления, время, прошедшее с начала простоя. | Milliseconds | Count | Application |  |
| downtime |  | Milliseconds | Multi | Application |  |
| downtime |  | Milliseconds | Sum | Application |  |
| fullRestarts | Общее количество полных перезапусков задания с момента его отправки. Эта метрика не измеряет частичные перезапуски. | Count | Count | Application |  |
| fullRestarts |  | Count | Multi | Application |  |
| fullRestarts |  | Count | Sum | Application |  |
| heapMemoryUtilization | Общее использование памяти кучи по всем менеджерам задач. | Percent | Count | Application |  |
| heapMemoryUtilization |  | Percent | Multi | Application |  |
| heapMemoryUtilization |  | Percent | Sum | Application |  |
| idleTimeMsPerSecond | Время (в миллисекундах) простоя задачи или оператора (нет данных для обработки) в секунду. Время простоя исключает время противодавления, поэтому если задача испытывает противодавление, она не считается простаивающей. | Milliseconds | Count | Application |  |
| idleTimeMsPerSecond |  | Milliseconds | Multi | Application |  |
| idleTimeMsPerSecond |  | Milliseconds | Sum | Application |  |
| lastCheckpointDuration | Время, затраченное на завершение последней контрольной точки. | Milliseconds | Count | Application |  |
| lastCheckpointDuration |  | Milliseconds | Multi | Application |  |
| lastCheckpointDuration |  | Milliseconds | Sum | Application |  |
| lastCheckpointSize | Общий размер последней контрольной точки | Bytes | Count | Application |  |
| lastCheckpointSize |  | Bytes | Multi | Application |  |
| lastCheckpointSize |  | Bytes | Sum | Application |  |
| numRecordsInPerSecond | Общее количество записей, полученных этим приложением, оператором или задачей в секунду. | Count/Second | Count | Application |  |
| numRecordsInPerSecond |  | Count/Second | Multi | Application |  |
| numRecordsInPerSecond |  | Count/Second | Sum | Application |  |
| numRecordsIn | Общее количество записей, полученных этим приложением, оператором или задачей. | Count | Count | Application |  |
| numRecordsIn |  | Count | Multi | Application |  |
| numRecordsIn |  | Count | Sum | Application |  |
| numRecordsOutPerSecond | Общее количество записей, отправленных этим приложением, оператором или задачей в секунду. | Count/Second | Count | Application |  |
| numRecordsOutPerSecond |  | Count/Second | Multi | Application |  |
| numRecordsOutPerSecond |  | Count/Second | Sum | Application |  |
| numRecordsOut | Общее количество записей, отправленных этим приложением, оператором или задачей. | Count | Count | Application |  |
| numRecordsOut |  | Count | Multi | Application |  |
| numRecordsOut |  | Count | Sum | Application |  |
| numRestarts |  | Count | Count | Application |  |
| numRestarts |  | Count | Multi | Application |  |
| numRestarts |  | Count | Sum | Application |  |
| numberOfFailedCheckpoints | Количество неудачных контрольных точек. | Count | Count | Application |  |
| numberOfFailedCheckpoints |  | Count | Multi | Application |  |
| numberOfFailedCheckpoints |  | Count | Sum | Application |  |
| oldGenerationGCCount | Общее количество операций сборки мусора старого поколения по всем менеджерам задач. | Count | Count | Application |  |
| oldGenerationGCCount |  | Count | Multi | Application |  |
| oldGenerationGCCount |  | Count | Sum | Application |  |
| oldGenerationGCTime | Общее время, затраченное на операции сборки мусора старого поколения. | Milliseconds | Count | Application |  |
| oldGenerationGCTime |  | Milliseconds | Multi | Application |  |
| oldGenerationGCTime |  | Milliseconds | Sum | Application |  |
| processElementavg |  | Count | Count | Application, Service |  |
| processElementavg |  | Count | Multi | Application, Service |  |
| processElementavg |  | Count | Sum | Application, Service |  |
| readDocsavg |  | Count | Count | Application, Service |  |
| readDocsavg |  | Count | Multi | Application, Service |  |
| readDocsavg |  | Count | Sum | Application, Service |  |
| records\_lag\_max | Максимальное отставание по количеству записей для любого раздела в данном окне | Count | Count | Application |  |
| records\_lag\_max |  | Count | Multi | Application |  |
| records\_lag\_max |  | Count | Sum | Application |  |
| threadsCount |  | Count | Count | Application |  |
| threadsCount |  | Count | Multi | Application |  |
| threadsCount |  | Count | Sum | Application |  |
| updatesavg |  | Count | Count | Application, Service |  |
| updatesavg |  | Count | Multi | Application, Service |  |
| updatesavg |  | Count | Sum | Application, Service |  |
| uptime | Время непрерывной работы задания. | Milliseconds | Count | Application |  |
| uptime |  | Milliseconds | Multi | Application |  |
| uptime |  | Milliseconds | Sum | Application |  |

### Amazon Data Firehose

`DeliveryStreamName` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| BackupToS3.Bytes | Количество байт, доставленных в Amazon S3 для резервного копирования за указанный период. Amazon Data Firehose отправляет эту метрику при включённом резервном копировании в Amazon S3. | Bytes | Sum | Region |  |
| BackupToS3.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| BackupToS3.DataFreshness | Возраст (от поступления в Amazon Data Firehose до текущего момента) самой старой записи в Amazon Data Firehose. Записи старше этого возраста доставлены в корзину Amazon S3 для резервного копирования. Amazon Data Firehose отправляет эту метрику при включённом резервном копировании в Amazon S3. | Seconds | Maximum | Region |  |
| BackupToS3.DataFreshness |  | Seconds | Maximum | DeliveryStreamName |  |
| BackupToS3.Records | Количество записей, доставленных в Amazon S3 для резервного копирования за указанный период. Amazon Data Firehose отправляет эту метрику при включённом резервном копировании в Amazon S3. | Count | Sum | Region |  |
| BackupToS3.Records |  | Count | Sum | DeliveryStreamName |  |
| BackupToS3.Success | Сумма успешных команд put в Amazon S3 для резервного копирования относительно суммы всех команд put для резервного копирования в Amazon S3. Amazon Data Firehose отправляет эту метрику при включённом резервном копировании в Amazon S3. | Count | Count | Region |  |
| BackupToS3.Success |  | Count | Count | DeliveryStreamName |  |
| DataReadFromKinesisStream.Bytes | Когда источником данных является поток Kinesis, эта метрика показывает количество байт, прочитанных из этого потока. Это число включает повторные чтения из-за отказов. | Bytes | Sum | Region |  |
| DataReadFromKinesisStream.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DataReadFromKinesisStream.Records | Когда источником данных является поток Kinesis, эта метрика показывает количество записей, прочитанных из этого потока. Это число включает повторные чтения из-за отказов. | Count | Sum | Region |  |
| DataReadFromKinesisStream.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Bytes | Количество байт, индексированных в Amazon ES за указанный период | Bytes | Sum | Region |  |
| DeliveryToElasticsearch.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Records | Количество записей, индексированных в Amazon ES за указанный период | Count | Sum | Region |  |
| DeliveryToElasticsearch.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Success | Сумма успешно индексированных записей относительно суммы всех попыток индексирования | Count | Count | Region |  |
| DeliveryToElasticsearch.Success |  | Count | Count | DeliveryStreamName |  |
| DeliveryToRedshift.Bytes | Количество байт, скопированных в Amazon Redshift за указанный период | Bytes | Sum | Region |  |
| DeliveryToRedshift.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToRedshift.Records | Количество записей, скопированных в Amazon Redshift за указанный период | Count | Sum | Region |  |
| DeliveryToRedshift.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToRedshift.Success | Сумма успешных команд Amazon Redshift `COPY` относительно суммы всех команд Amazon Redshift `COPY` | Count | Count | Region |  |
| DeliveryToRedshift.Success |  | Count | Count | DeliveryStreamName |  |
| DeliveryToS3.Bytes | Количество байт, доставленных в Amazon S3 за указанный период | Bytes | Sum | Region |  |
| DeliveryToS3.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToS3.DataFreshness | Возраст (от поступления в Amazon Data Firehose до текущего момента) самой старой записи в Amazon Data Firehose. Записи старше этого возраста доставлены в корзину S3. | Seconds | Maximum | Region |  |
| DeliveryToS3.DataFreshness |  | Seconds | Maximum | DeliveryStreamName |  |
| DeliveryToS3.Records | Количество записей, доставленных в Amazon S3 за указанный период | Count | Sum | Region |  |
| DeliveryToS3.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToS3.Success | Сумма успешных команд put в Amazon S3 относительно суммы всех команд put в Amazon S3 | Count | Count | Region |  |
| DeliveryToS3.Success |  | Count | Count | DeliveryStreamName |  |
| DeliveryToSplunk.Bytes | Количество байт, доставленных в Splunk за указанный период | Bytes | Sum | Region |  |
| DeliveryToSplunk.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToSplunk.DataAckLatency | Приблизительное время получения подтверждения от Splunk после отправки данных Amazon Data Firehose | Seconds | Average | Region |  |
| DeliveryToSplunk.DataAckLatency |  | Seconds | Average | DeliveryStreamName |  |
| DeliveryToSplunk.DataFreshness | Возраст (от поступления в Amazon Data Firehose до текущего момента) самой старой записи в Amazon Data Firehose. Записи старше этого возраста доставлены в Splunk. | Seconds | Maximum | Region |  |
| DeliveryToSplunk.DataFreshness |  | Seconds | Maximum | DeliveryStreamName |  |
| DeliveryToSplunk.Records | Количество записей, доставленных в Splunk за указанный период | Count | Sum | Region |  |
| DeliveryToSplunk.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToSplunk.Success | Сумма успешно индексированных записей относительно суммы всех попыток индексирования | Count | Count | Region |  |
| DeliveryToSplunk.Success |  | Count | Count | DeliveryStreamName |  |
| DescribeDeliveryStream.Latency | Время, затраченное на каждую операцию `DescribeDeliveryStream`, измеренное за указанный период | Milliseconds | Multi | Region |  |
| DescribeDeliveryStream.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| DescribeDeliveryStream.Requests | Общее количество запросов `DescribeDeliveryStream` | Count | Sum | Region |  |
| DescribeDeliveryStream.Requests |  | Count | Sum | DeliveryStreamName |  |
| ExecuteProcessing.Duration | Время, затраченное на каждый вызов функции Lambda, выполненный Amazon Data Firehose | Milliseconds | Multi | Region |  |
| ExecuteProcessing.Duration |  | Milliseconds | Multi | DeliveryStreamName |  |
| ExecuteProcessing.Success | Сумма успешных вызовов функций Lambda относительно суммы всех вызовов функций Lambda | Count | Count | Region |  |
| ExecuteProcessing.Success |  | Count | Count | DeliveryStreamName |  |
| FailedConversion.Bytes | Размер записей, которые не удалось преобразовать | Bytes | Sum | Region |  |
| FailedConversion.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| FailedConversion.Records | Количество записей, которые не удалось преобразовать | Count | Sum | Region |  |
| FailedConversion.Records |  | Count | Sum | DeliveryStreamName |  |
| IncomingBytes | Количество байт, успешно принятых в поток доставки за указанный период после ограничения скорости | Bytes | Sum | Region |  |
| IncomingBytes |  | Bytes | Sum | DeliveryStreamName | Доступна |
| IncomingRecords | Количество записей, успешно принятых в поток доставки за указанный период после ограничения скорости | Count | Sum | Region |  |
| IncomingRecords |  | Count | Sum | DeliveryStreamName | Доступна |
| KinesisMillisBehindLatest | Когда источником данных является поток Kinesis, эта метрика показывает количество миллисекунд, на которое последняя прочитанная запись отстаёт от самой новой записи в потоке Kinesis | Milliseconds | Average | Region |  |
| KinesisMillisBehindLatest |  | Milliseconds | Average | DeliveryStreamName |  |
| ListDeliveryStreams.Latency | Время, затраченное на каждую операцию `ListDeliveryStream`, измеренное за указанный период | Milliseconds | Multi | Region |  |
| ListDeliveryStreams.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| ListDeliveryStreams.Requests | Общее количество запросов `ListFirehose` | Count | Sum | Region |  |
| ListDeliveryStreams.Requests |  | Count | Sum | DeliveryStreamName |  |
| PutRecordBatch.Bytes | Количество байт, отправленных в поток доставки Amazon Data Firehose с помощью `PutRecordBatch` за указанный период | Bytes | Sum | Region |  |
| PutRecordBatch.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| PutRecordBatch.Latency | Время, затраченное на каждую операцию `PutRecordBatch`, измеренное за указанный период | Milliseconds | Multi | Region |  |
| PutRecordBatch.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| PutRecordBatch.Records | Общее количество записей из операций `PutRecordBatch` | Count | Sum | Region |  |
| PutRecordBatch.Records |  | Count | Sum | DeliveryStreamName |  |
| PutRecordBatch.Requests | Общее количество запросов `PutRecordBatch` | Count | Sum | Region |  |
| PutRecordBatch.Requests |  | Count | Sum | DeliveryStreamName |  |
| PutRecord.Bytes | Количество байт, отправленных в поток доставки Amazon Data Firehose с помощью `PutRecord` за указанный период | Bytes | Sum | Region |  |
| PutRecord.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| PutRecord.Latency | Время, затраченное на каждую операцию `PutRecord`, измеренное за указанный период | Milliseconds | Multi | Region |  |
| PutRecord.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| PutRecord.Requests | Общее количество запросов `PutRecord`, равное общему количеству записей из операций `PutRecord` | Count | Sum | Region |  |
| PutRecord.Requests |  | Count | Sum | DeliveryStreamName |  |
| SucceedConversion.Bytes | Размер успешно преобразованных записей | Bytes | Sum | Region |  |
| SucceedConversion.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| SucceedConversion.Records | Количество успешно преобразованных записей | Count | Sum | Region |  |
| SucceedConversion.Records |  | Count | Sum | DeliveryStreamName |  |
| SucceedProcessing.Bytes | Количество успешно обработанных байт за указанный период | Bytes | Sum | Region |  |
| SucceedProcessing.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| SucceedProcessing.Records | Количество успешно обработанных записей за указанный период | Count | Sum | Region |  |
| SucceedProcessing.Records |  | Count | Sum | DeliveryStreamName |  |
| ThrottledDescribeStream | Общее количество ограничений операции `DescribeStream`, когда источником данных является поток Kinesis | Count | Average | Region |  |
| ThrottledDescribeStream |  | Count | Average | DeliveryStreamName |  |
| ThrottledGetRecords | Общее количество ограничений операции `GetRecords`, когда источником данных является поток Kinesis | Count | Average | Region |  |
| ThrottledGetRecords |  | Count | Average | DeliveryStreamName |  |
| ThrottledGetShardIterator | Общее количество ограничений операции `GetShardIterator`, когда источником данных является поток Kinesis | Count | Average | Region |  |
| ThrottledGetShardIterator |  | Count | Average | DeliveryStreamName |  |
| UpdateDeliveryStream.Latency | Время, затраченное на каждую операцию `UpdateDeliveryStream`, измеренное за указанный период | Milliseconds | Multi | Region |  |
| UpdateDeliveryStream.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| UpdateDeliveryStream.Requests | Общее количество запросов `UpdateDeliveryStream` | Count | Sum | Region |  |
| UpdateDeliveryStream.Requests |  | Count | Sum | DeliveryStreamName |  |

### Amazon Kinesis Data Streams (KDS)

`StreamName` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| GetRecords.Bytes | The number of bytes retrieved from the Kinesis stream, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes in a single `GetRecords` operation for the stream in the specified time period. | Bytes | Sum | StreamName |  |
| GetRecords.Bytes |  | Bytes | Multi | StreamName |  |
| GetRecords.Bytes |  | Bytes | Count | StreamName |  |
| GetRecords.IteratorAgeMilliseconds | The age of the last record in all `GetRecords` calls made against a Kinesis stream, measured over the specified time period. Age is the difference between the current time and when the last record of the `GetRecords` call was written to the stream. The minimum and maximum statistics can be used to track the progress of Kinesis consumer applications. A value of `0` indicates that the records being read are completely caught up with the stream. | Milliseconds | Multi | StreamName | Доступна |
| GetRecords.IteratorAgeMilliseconds |  | Milliseconds | Count | StreamName |  |
| GetRecords.Latency | The time taken per GetRecords operation, measured over the specified time period | Milliseconds | Multi | StreamName |  |
| GetRecords.Records | The number of records retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records in a single `GetRecords` operation for the stream in the specified time period. | Count | Sum | StreamName |  |
| GetRecords.Records |  | Count | Multi | StreamName |  |
| GetRecords.Records |  | Count | Count | StreamName |  |
| GetRecords.Success | The number of successful `GetRecords` operations per stream, measured over the specified time period | Count | Sum | StreamName |  |
| GetRecords.Success |  | Count | Average | StreamName | Доступна |
| GetRecords.Success |  | Count | Count | StreamName |  |
| IncomingBytes | The number of bytes successfully put to the Kinesis stream over the specified time period. This metric includes bytes from `PutRecord` and `PutRecords` operations. Minimum, maximum, and average statistics represent the bytes in a single put operation for the stream in the specified time period. | Bytes | Count | ShardId, StreamName |  |
| IncomingBytes |  | Bytes | Count | StreamName |  |
| IncomingBytes |  | Bytes | Multi | ShardId, StreamName |  |
| IncomingBytes |  | Bytes | Multi | StreamName |  |
| IncomingBytes |  | Bytes | Sum | ShardId, StreamName |  |
| IncomingBytes |  | Bytes | Sum | StreamName |  |
| IncomingRecords | The number of records successfully put to the Kinesis stream over the specified time period. This metric includes record counts from `PutRecord` and `PutRecords` operations. Minimum, maximum, and average statistics represent the records in a single put operation for the stream in the specified time period. | Count | Count | ShardId, StreamName |  |
| IncomingRecords |  | Count | Count | StreamName |  |
| IncomingRecords |  | Count | Multi | ShardId, StreamName |  |
| IncomingRecords |  | Count | Multi | StreamName |  |
| IncomingRecords |  | Count | Sum | ShardId, StreamName |  |
| IteratorAgeMilliseconds | The age of the last record in all `GetRecords` calls made against a shard, measured over the specified time period. Age is the difference between the current time and when the last record of the `GetRecords` call was written to the stream. The minimum and maximum statistics can be used to track the progress of Kinesis consumer applications. A value of `0` indicates that the records being read are completely caught up with the stream. | Milliseconds | Multi | StreamName, ShardId |  |
| IteratorAgeMilliseconds |  | Milliseconds | Count | StreamName, ShardId |  |
| OutgoingBytes | The number of bytes retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes returned in a single `GetRecords` operation or published in a single `SubscribeToShard` event for the shard in the specified time period. | Bytes | Sum | StreamName, ShardId |  |
| OutgoingBytes |  | Bytes | Multi | StreamName, ShardId |  |
| OutgoingBytes |  | Bytes | Count | StreamName, ShardId |  |
| OutgoingRecords | The number of records retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records returned in a single `GetRecords` operation or published in a single `SubscribeToShard` event for the shard in the specified time period. | Count | Sum | StreamName, ShardId |  |
| OutgoingRecords |  | Count | Multi | StreamName, ShardId |  |
| OutgoingRecords |  | Count | Count | StreamName, ShardId |  |
| PutRecord.Bytes | The number of bytes put to the Kinesis stream using the `PutRecord` operation over the specified time period | Bytes | Sum | StreamName |  |
| PutRecord.Bytes |  | Bytes | Multi | StreamName |  |
| PutRecord.Bytes |  | Bytes | Count | StreamName |  |
| PutRecord.Latency | The time taken per `PutRecord` operation, measured over the specified time period | Milliseconds | Multi | StreamName |  |
| PutRecord.Success | The number of successful `PutRecord` operations per Kinesis stream, measured over the specified time period. Average reflects the percentage of successful writes to a stream. | Count | Sum | StreamName |  |
| PutRecord.Success |  | Count | Average | StreamName | Доступна |
| PutRecord.Success |  | Count | Count | StreamName |  |
| PutRecords.Bytes | The number of bytes put to the Kinesis stream using the `PutRecords` operation over the specified time period | Bytes | Sum | StreamName |  |
| PutRecords.Bytes |  | Bytes | Multi | StreamName |  |
| PutRecords.Bytes |  | Bytes | Count | StreamName |  |
| PutRecords.Latency | The time taken per `PutRecords` operation, measured over the specified time period | Milliseconds | Multi | StreamName |  |
| PutRecords.Records | The number of successful records in a `PutRecords` operation per Kinesis stream, measured over the specified time period | Count | Sum | StreamName |  |
| PutRecords.Records |  | Count | Multi | StreamName |  |
| PutRecords.Records |  | Count | Count | StreamName |  |
| PutRecords.Success | The number of `PutRecords` operations where at least one record succeeded, per Kinesis stream, measured over the specified time period | Count | Sum | StreamName |  |
| PutRecords.Success |  | Count | Average | StreamName |  |
| PutRecords.Success |  | Count | Count | StreamName |  |
| ReadProvisionedThroughputExceeded | The number of `GetRecords` calls throttled for the stream over the specified time period | Count | Sum | StreamName |  |
| ReadProvisionedThroughputExceeded |  | Count | Multi | StreamName | Доступна |
| ReadProvisionedThroughputExceeded |  | Count | Count | StreamName |  |
| SubscribeToShardEvent.Bytes | The number of bytes received from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes published in a single event for the specified time period. | Bytes | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Bytes |  | Bytes | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Bytes |  | Bytes | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.MillisBehindLatest | The difference between the current time and when the last record of the `SubscribeToShard` event was written to the stream | Milliseconds | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.MillisBehindLatest |  | Milliseconds | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records | The number of records received from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records in a single event for the specified time period. | Count | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records |  | Count | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records |  | Count | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success | This metric is emitted every time an event is published successfully. Only emitted when there's an active subscription. | Count | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success |  | Count | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success |  | Count | Count | StreamName, ConsumerName |  |
| SubscribeToShard.RateExceeded | This metric is emitted when a new subscription attempt fails because there already is an active subscription by the same consumer or if you exceed the number of calls per second allowed for this operation | Count | Minimum | StreamName, ConsumerName |  |
| SubscribeToShard.Success |  | Count | Minimum | StreamName, ConsumerName |  |
| WriteProvisionedThroughputExceeded | The number of records rejected due to throttling for the stream over the specified time period. This metric includes throttling from `PutRecord` and `PutRecords` operations. | Count | Sum | StreamName |  |
| WriteProvisionedThroughputExceeded |  | Count | Multi | StreamName | Доступна |
| WriteProvisionedThroughputExceeded |  | Count | Count | StreamName |  |

### Amazon Kinesis Video Streams

`StreamName` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| GetHLSMasterPlaylist.Latency | Latency of the `GetHLSMasterPlaylist` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetHLSMasterPlaylist.Requests | Number of `GetHLSMasterPlaylist` API requests for a given stream | Count | Sum | StreamName |  |
| GetHLSMasterPlaylist.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetHLSMediaPlaylist.Latency | Latency of the `GetHLSMediaPlaylist` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetHLSMediaPlaylist.Requests | Number of `GetHLSMediaPlaylist` API requests for a given stream | Count | Sum | StreamName |  |
| GetHLSMediaPlaylist.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetHLSStreamingSessionURL.Latency | Latency of the `GetHLSStreamingSessionURL` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetHLSStreamingSessionURL.Requests | Number of `GetHLSStreamingSessionURL` API requests for a given stream | Count | Sum | StreamName |  |
| GetHLSStreamingSessionURL.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetMP4InitFragment.Latency | Latency of the `GetMP4InitFragment` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetMP4InitFragment.Requests | Number of `GetMP4InitFragment` API requests for a given stream | Count | Sum | StreamName |  |
| GetMP4InitFragment.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetMP4MediaFragment.Latency | Latency of the `GetMP4MediaFragment` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetMP4MediaFragment.OutgoingBytes | Total number of bytes sent out from the service as part of the `GetMP4MediaFragment` API for a given stream | Bytes | Sum | StreamName |  |
| GetMP4MediaFragment.Requests | Number of `GetMP4MediaFragment` API requests for a given stream | Count | Sum | StreamName |  |
| GetMP4MediaFragment.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Sum | StreamName |  |
| GetMedia.ConnectionErrors | The number of connections that were not successfully established | Count | Sum | StreamName | Доступна |
| GetMediaForFragmentList.OutgoingBytes | Total number of bytes sent out from the service as part of the `GetMediaForFragmentList` API for a given stream | Bytes | Sum | StreamName |  |
| GetMediaForFragmentList.OutgoingFragments | Total number of fragments sent out from the service as part of the `GetMediaForFragmentList` API for a given stream | Count | Sum | StreamName |  |
| GetMediaForFragmentList.OutgoingFrames | Total number of frames sent out from the service as part of the `GetMediaForFragmentList` API for a given stream | Count | Sum | StreamName |  |
| GetMediaForFragmentList.Requests | Number of `GetMediaForFragmentList` API requests for a given stream | Count | Sum | StreamName |  |
| GetMediaForFragmentList.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetMedia.MillisBehindNow | Time difference between the current server timestamp and the server timestamp of the last fragment sent | Milliseconds | Multi | StreamName |  |
| GetMedia.OutgoingBytes | Total number of bytes sent out from the service as part of the `GetMedia` API for a given stream | Bytes | Sum | StreamName |  |
| GetMedia.OutgoingFragments | Number of fragments sent while doing `GetMedia` for the stream | Count | Sum | StreamName |  |
| GetMedia.OutgoingFrames | Number of frames sent during `GetMedia` on the given stream | Count | Sum | StreamName |  |
| GetMedia.Requests | Number of `GetMedia` API requests for a given stream | Count | Sum | StreamName |  |
| GetMedia.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName | Доступна |
| ListFragments.Latency | Latency of the `ListFragments` API calls for the given stream name | Milliseconds | Multi | StreamName | Доступна |
| PutMedia.ActiveConnections | The total number of connections to the service host | Count | Sum | StreamName |  |
| PutMedia.BufferingAckLatency | Time difference between when the first byte of a new fragment is received by Kinesis Video Streams and when the `Buffering ACK` is sent for the fragment | Milliseconds | Multi | StreamName |  |
| PutMedia.ConnectionErrors | Errors while establishing `PutMedia` connection for the stream | Count | Sum | StreamName | Доступна |
| PutMedia.ErrorAckCount | Number of Error ACKs sent while doing `PutMedia` for the stream | Count | Sum | StreamName |  |
| PutMedia.FragmentIngestionLatency | Time difference between when the first and last bytes of a fragment are received by Kinesis Video Streams | Milliseconds | Multi | StreamName |  |
| PutMedia.FragmentPersistLatency | Time taken from when the complete fragment data is received and archived | Milliseconds | Multi | StreamName |  |
| PutMedia.IncomingBytes | Number of bytes received as part of `PutMedia` for the stream | Bytes | Sum | StreamName |  |
| PutMedia.IncomingFragments | Number of complete fragments received as part of `PutMedia` for the stream | Count | Sum | StreamName |  |
| PutMedia.IncomingFrames | Number of complete frames received as part of `PutMedia` for the stream | Count | Sum | StreamName |  |
| PutMedia.Latency | Time difference between the request and the HTTP response from `InletService` while establishing the connection | Milliseconds | Multi | StreamName |  |
| PutMedia.PersistedAckLatency | Time difference between when the last byte of a new fragment is received by Kinesis Video Streams and when the `Persisted ACK` is sent for the fragment | Milliseconds | Multi | StreamName |  |
| PutMedia.ReceivedAckLatency | Time difference between when the last byte of a new fragment is received by Kinesis Video Streams and when the `Received ACK` is sent for the fragment | Milliseconds | Multi | StreamName |  |
| PutMedia.Requests | Number of `PutMedia` API requests for a given stream | Count | Sum | StreamName |  |
| PutMedia.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName | Доступна |