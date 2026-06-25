---
title: Мониторинг Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-kinesis
scraped: 2026-05-12T11:30:20.093856
---

# Мониторинг Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams)

# Мониторинг Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams)

* Практическое руководство
* Чтение: 33 мин
* Обновлено 10 января 2025 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая Amazon Kinesis. Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

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

### Amazon Kinesis Data Analytics

Основное измерение: `Application`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| Bytes | Количество прочитанных байт (на входной поток) или записанных (на выходной поток). | Байт | Sum | Application, Flow, Id | Применимо |
| InputProcessing.DroppedRecords | Количество записей, возвращённых функцией Lambda и помеченных статусом `Dropped`. | Количество | Sum | Application, Flow, Id |  |
| InputProcessing.Duration | Время, затраченное на каждый вызов функции AWS Lambda, выполненный Kinesis Data Analytics. | Миллисекунда | Multi | Application, Flow, Id |  |
| InputProcessing.OkBytes | Сумма байт записей, возвращённых функцией Lambda и помеченных статусом `OK`. | Байт | Sum | Application, Flow, Id |  |
| InputProcessing.OkRecords | Количество записей, возвращённых функцией Lambda и помеченных статусом `OK`. | Количество | Sum | Application, Flow, Id |  |
| InputProcessing.ProcessingFailedRecords | Количество записей, возвращённых функцией Lambda и помеченных статусом `ProcessingFailed`. | Количество | Sum | Application, Flow, Id |  |
| InputProcessing.Success | Количество успешных вызовов Lambda, выполненных Kinesis Data Analytics. | Количество | Sum | Application, Flow, Id |  |
| KPUs | Количество единиц обработки Kinesis, используемых для запуска вашего приложения потоковой обработки. | Количество | Count | Application |  |
| KPUs |  | Количество | Multi | Application |  |
| KPUs |  | Количество | Sum | Application | Применимо |
| LambdaDelivery.DeliveryFailedRecords | Количество успешных вызовов Lambda, выполненных Kinesis Data Analytics. | Количество | Sum | Application, Flow, Id |  |
| LambdaDelivery.Duration | Время, затраченное на каждый вызов функции Lambda, выполненный Kinesis Data Analytics. | Миллисекунда | Multi | Application, Flow, Id |  |
| LambdaDelivery.OkRecords | Количество записей, возвращённых функцией Lambda и помеченных статусом `OK`. | Количество | Sum | Application, Flow, Id |  |
| MillisBehindLatest | Показывает, насколько относительно текущего времени приложение отстаёт при чтении из потокового источника. | Миллисекунда | Multi | Application; Application, Flow, Id |  |
| Records | Количество прочитанных записей (на входной поток) или записанных (на выходной поток). | Количество | Sum | Application, Flow, Id | Применимо |
| Success | Количество успешных доставок. Каждая успешная попытка доставки в место назначения, настроенное для вашего приложения, помечается значением `1`. Каждая неудачная попытка доставки помечается значением `0`. | Количество | Average | Application, Flow, Id | Применимо |
| backPressuredTimeMsPerSecond | Время (в миллисекундах), в течение которого эта задача или оператор находится под обратным давлением, в секунду. | Миллисекунда | Count | Application |  |
| backPressuredTimeMsPerSecond |  | Миллисекунда | Multi | Application |  |
| backPressuredTimeMsPerSecond |  | Миллисекунда | Sum | Application |  |
| busyTimeMsPerSecond | Время (в миллисекундах), в течение которого эта задача или оператор занят (не простаивает и не находится под обратным давлением), в секунду. Может быть NaN, если значение не удалось вычислить. | Миллисекунда | Count | Application |  |
| busyTimeMsPerSecond |  | Миллисекунда | Multi | Application |  |
| busyTimeMsPerSecond |  | Миллисекунда | Sum | Application |  |
| bytes\_consumed\_rate | Среднее количество байт, потребляемых в секунду для топика. | Байт | Count | Application |  |
| bytes\_consumed\_rate |  | Байт | Multi | Application |  |
| bytes\_consumed\_rate |  | Байт | Sum | Application |  |
| commitsFailed | Общее количество неудачных фиксаций смещения в Kafka, если включены фиксация смещения и создание контрольных точек. | Количество | Count | Application |  |
| commitsFailed |  | Количество | Multi | Application |  |
| commitsFailed |  | Количество | Sum | Application |  |
| commitsSucceeded | Общее количество успешных фиксаций смещения в Kafka, если включены фиксация смещения и создание контрольных точек. | Количество | Count | Application |  |
| commitsSucceeded |  | Количество | Multi | Application |  |
| commitsSucceeded |  | Количество | Sum | Application |  |
| committedOffsets | Последние успешно зафиксированные смещения в Kafka для каждой партиции. Метрику конкретной партиции можно указать по имени топика и id партиции. | Количество | Count | Application |  |
| committedOffsets |  | Количество | Multi | Application |  |
| committedOffsets |  | Количество | Sum | Application |  |
| containerCPUUtilization | Общий процент использования CPU по контейнерам менеджеров задач в кластере приложения Flink. | Процент | Count | Application |  |
| containerCPUUtilization |  | Процент | Multi | Application |  |
| containerCPUUtilization |  | Процент | Sum | Application |  |
| containerDiskUtilization | Общий процент использования диска по контейнерам менеджеров задач в кластере приложения Flink. | Процент | Count | Application |  |
| containerDiskUtilization |  | Процент | Multi | Application |  |
| containerDiskUtilization |  | Процент | Sum | Application |  |
| containerMemoryUtilization | Общий процент использования памяти по контейнерам менеджеров задач в кластере приложения Flink. | Процент | Count | Application |  |
| containerMemoryUtilization |  | Процент | Multi | Application |  |
| containerMemoryUtilization |  | Процент | Sum | Application |  |
| cpuUtilization | Общий процент использования CPU по менеджерам задач. | Процент | Count | Application |  |
| cpuUtilization |  | Процент | Multi | Application |  |
| cpuUtilization |  | Процент | Sum | Application |  |
| currentInputWatermark | Последний водяной знак, полученный этим приложением/оператором/задачей/потоком. | Миллисекунда | Count | Application |  |
| currentInputWatermark |  | Миллисекунда | Multi | Application |  |
| currentInputWatermark |  | Миллисекунда | Sum | Application |  |
| currentOffsets | Текущее смещение чтения потребителя для каждой партиции. Метрику конкретной партиции можно указать по имени топика и id партиции. | Количество | Count | Application |  |
| currentOffsets |  | Количество | Multi | Application |  |
| currentOffsets |  | Количество | Sum | Application |  |
| currentOutputWatermark | Последний водяной знак, отправленный этим приложением/оператором/задачей/потоком. | Миллисекунда | Count | Application |  |
| currentOutputWatermark |  | Миллисекунда | Multi | Application |  |
| currentOutputWatermark |  | Миллисекунда | Sum | Application |  |
| downtime | Для заданий, в данный момент находящихся в состоянии сбоя/восстановления, время, прошедшее в течение этого перебоя в работе. | Миллисекунда | Count | Application |  |
| downtime |  | Миллисекунда | Multi | Application |  |
| downtime |  | Миллисекунда | Sum | Application |  |
| fullRestarts | Общее количество полных перезапусков этого задания с момента его отправки. Эта метрика не учитывает точечные перезапуски. | Количество | Count | Application |  |
| fullRestarts |  | Количество | Multi | Application |  |
| fullRestarts |  | Количество | Sum | Application |  |
| heapMemoryUtilization | Общее использование памяти кучи по менеджерам задач. | Процент | Count | Application |  |
| heapMemoryUtilization |  | Процент | Multi | Application |  |
| heapMemoryUtilization |  | Процент | Sum | Application |  |
| idleTimeMsPerSecond | Время (в миллисекундах), в течение которого эта задача или оператор простаивает (нет данных для обработки), в секунду. Время простоя не включает время под обратным давлением, поэтому если задача находится под обратным давлением, она не простаивает. | Миллисекунда | Count | Application |  |
| idleTimeMsPerSecond |  | Миллисекунда | Multi | Application |  |
| idleTimeMsPerSecond |  | Миллисекунда | Sum | Application |  |
| lastCheckpointDuration | Время, которое потребовалось для завершения последней контрольной точки. | Миллисекунда | Count | Application |  |
| lastCheckpointDuration |  | Миллисекунда | Multi | Application |  |
| lastCheckpointDuration |  | Миллисекунда | Sum | Application |  |
| lastCheckpointSize | Общий размер последней контрольной точки | Байт | Count | Application |  |
| lastCheckpointSize |  | Байт | Multi | Application |  |
| lastCheckpointSize |  | Байт | Sum | Application |  |
| numRecordsInPerSecond | Общее количество записей, полученных этим приложением, оператором или задачей в секунду. | Количество в секунду | Count | Application |  |
| numRecordsInPerSecond |  | Количество в секунду | Multi | Application |  |
| numRecordsInPerSecond |  | Количество в секунду | Sum | Application |  |
| numRecordsIn | Общее количество записей, полученных этим приложением, оператором или задачей. | Количество | Count | Application |  |
| numRecordsIn |  | Количество | Multi | Application |  |
| numRecordsIn |  | Количество | Sum | Application |  |
| numRecordsOutPerSecond | Общее количество записей, отправленных этим приложением, оператором или задачей в секунду. | Количество в секунду | Count | Application |  |
| numRecordsOutPerSecond |  | Количество в секунду | Multi | Application |  |
| numRecordsOutPerSecond |  | Количество в секунду | Sum | Application |  |
| numRecordsOut | Общее количество записей, отправленных этим приложением, оператором или задачей. | Количество | Count | Application |  |
| numRecordsOut |  | Количество | Multi | Application |  |
| numRecordsOut |  | Количество | Sum | Application |  |
| numRestarts |  | Количество | Count | Application |  |
| numRestarts |  | Количество | Multi | Application |  |
| numRestarts |  | Количество | Sum | Application |  |
| numberOfFailedCheckpoints | Количество случаев сбоя при создании контрольных точек. | Количество | Count | Application |  |
| numberOfFailedCheckpoints |  | Количество | Multi | Application |  |
| numberOfFailedCheckpoints |  | Количество | Sum | Application |  |
| oldGenerationGCCount | Общее количество операций сборки мусора старого поколения, произошедших по всем менеджерам задач. | Количество | Count | Application |  |
| oldGenerationGCCount |  | Количество | Multi | Application |  |
| oldGenerationGCCount |  | Количество | Sum | Application |  |
| oldGenerationGCTime | Общее время, затраченное на выполнение операций сборки мусора старого поколения. | Миллисекунда | Count | Application |  |
| oldGenerationGCTime |  | Миллисекунда | Multi | Application |  |
| oldGenerationGCTime |  | Миллисекунда | Sum | Application |  |
| processElementavg |  | Количество | Count | Application, Service |  |
| processElementavg |  | Количество | Multi | Application, Service |  |
| processElementavg |  | Количество | Sum | Application, Service |  |
| readDocsavg |  | Количество | Count | Application, Service |  |
| readDocsavg |  | Количество | Multi | Application, Service |  |
| readDocsavg |  | Количество | Sum | Application, Service |  |
| records\_lag\_max | Максимальное отставание по числу записей для любой партиции в этом окне | Количество | Count | Application |  |
| records\_lag\_max |  | Количество | Multi | Application |  |
| records\_lag\_max |  | Количество | Sum | Application |  |
| threadsCount |  | Количество | Count | Application |  |
| threadsCount |  | Количество | Multi | Application |  |
| threadsCount |  | Количество | Sum | Application |  |
| updatesavg |  | Количество | Count | Application, Service |  |
| updatesavg |  | Количество | Multi | Application, Service |  |
| updatesavg |  | Количество | Sum | Application, Service |  |
| uptime | Время, в течение которого задание выполнялось без прерываний. | Миллисекунда | Count | Application |  |
| uptime |  | Миллисекунда | Multi | Application |  |
| uptime |  | Миллисекунда | Sum | Application |  |

### Amazon Data Firehose

Основное измерение: `DeliveryStreamName`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| BackupToS3.Bytes | Количество байт, доставленных в Amazon S3 для резервного копирования за указанный период времени. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3. | Байт | Sum | Region |  |
| BackupToS3.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| BackupToS3.DataFreshness | Возраст (с момента попадания в Amazon Data Firehose до настоящего момента) самой старой записи в Amazon Data Firehose. Любая запись старше этого возраста была доставлена в корзину Amazon S3 для резервного копирования. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3. | Секунда | Maximum | Region |  |
| BackupToS3.DataFreshness |  | Секунда | Maximum | DeliveryStreamName |  |
| BackupToS3.Records | Количество записей, доставленных в Amazon S3 для резервного копирования за указанный период времени. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3. | Количество | Sum | Region |  |
| BackupToS3.Records |  | Количество | Sum | DeliveryStreamName |  |
| BackupToS3.Success | Сумма успешных команд put в Amazon S3 для резервного копирования относительно суммы всех команд put резервного копирования в Amazon S3. Amazon Data Firehose отправляет эту метрику, когда включено резервное копирование в Amazon S3. | Количество | Count | Region |  |
| BackupToS3.Success |  | Количество | Count | DeliveryStreamName |  |
| DataReadFromKinesisStream.Bytes | Когда источником данных является поток данных Kinesis, эта метрика показывает количество байт, прочитанных из этого потока данных. Это число включает повторные чтения из-за отработки отказа. | Байт | Sum | Region |  |
| DataReadFromKinesisStream.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| DataReadFromKinesisStream.Records | Когда источником данных является поток данных Kinesis, эта метрика показывает количество записей, прочитанных из этого потока данных. Это число включает повторные чтения из-за отработки отказа. | Количество | Sum | Region |  |
| DataReadFromKinesisStream.Records |  | Количество | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Bytes | Количество байт, проиндексированных в Amazon ES за указанный период времени | Байт | Sum | Region |  |
| DeliveryToElasticsearch.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Records | Количество записей, проиндексированных в Amazon ES за указанный период времени | Количество | Sum | Region |  |
| DeliveryToElasticsearch.Records |  | Количество | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Success | Сумма успешно проиндексированных записей относительно суммы записей, по которым была предпринята попытка | Количество | Count | Region |  |
| DeliveryToElasticsearch.Success |  | Количество | Count | DeliveryStreamName |  |
| DeliveryToRedshift.Bytes | Количество байт, скопированных в Amazon Redshift за указанный период времени | Байт | Sum | Region |  |
| DeliveryToRedshift.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| DeliveryToRedshift.Records | Количество записей, скопированных в Amazon Redshift за указанный период времени | Количество | Sum | Region |  |
| DeliveryToRedshift.Records |  | Количество | Sum | DeliveryStreamName |  |
| DeliveryToRedshift.Success | Сумма успешных команд `COPY` в Amazon Redshift относительно суммы всех команд `COPY` в Amazon Redshift | Количество | Count | Region |  |
| DeliveryToRedshift.Success |  | Количество | Count | DeliveryStreamName |  |
| DeliveryToS3.Bytes | Количество байт, доставленных в Amazon S3 за указанный период времени | Байт | Sum | Region |  |
| DeliveryToS3.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| DeliveryToS3.DataFreshness | Возраст (с момента попадания в Amazon Data Firehose до настоящего момента) самой старой записи в Amazon Data Firehose. Любая запись старше этого возраста была доставлена в корзину S3. | Секунда | Maximum | Region |  |
| DeliveryToS3.DataFreshness |  | Секунда | Maximum | DeliveryStreamName |  |
| DeliveryToS3.Records | Количество записей, доставленных в Amazon S3 за указанный период времени | Количество | Sum | Region |  |
| DeliveryToS3.Records |  | Количество | Sum | DeliveryStreamName |  |
| DeliveryToS3.Success | Сумма успешных команд put в Amazon S3 относительно суммы всех команд put в Amazon S3 | Количество | Count | Region |  |
| DeliveryToS3.Success |  | Количество | Count | DeliveryStreamName |  |
| DeliveryToSplunk.Bytes | Количество байт, доставленных в Splunk за указанный период времени | Байт | Sum | Region |  |
| DeliveryToSplunk.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| DeliveryToSplunk.DataAckLatency | Приблизительная продолжительность получения подтверждения от Splunk после того, как Amazon Data Firehose отправляет ему данные | Секунда | Average | Region |  |
| DeliveryToSplunk.DataAckLatency |  | Секунда | Average | DeliveryStreamName |  |
| DeliveryToSplunk.DataFreshness | Возраст (с момента попадания в Amazon Data Firehose до настоящего момента) самой старой записи в Amazon Data Firehose. Любая запись старше этого возраста была доставлена в Splunk. | Секунда | Maximum | Region |  |
| DeliveryToSplunk.DataFreshness |  | Секунда | Maximum | DeliveryStreamName |  |
| DeliveryToSplunk.Records | Количество записей, доставленных в Splunk за указанный период времени | Количество | Sum | Region |  |
| DeliveryToSplunk.Records |  | Количество | Sum | DeliveryStreamName |  |
| DeliveryToSplunk.Success | Сумма успешно проиндексированных записей относительно суммы записей, по которым была предпринята попытка | Количество | Count | Region |  |
| DeliveryToSplunk.Success |  | Количество | Count | DeliveryStreamName |  |
| DescribeDeliveryStream.Latency | Время, затраченное на одну операцию `DescribeDeliveryStream`, измеренное за указанный период времени | Миллисекунда | Multi | Region |  |
| DescribeDeliveryStream.Latency |  | Миллисекунда | Multi | DeliveryStreamName |  |
| DescribeDeliveryStream.Requests | Общее количество запросов `DescribeDeliveryStream` | Количество | Sum | Region |  |
| DescribeDeliveryStream.Requests |  | Количество | Sum | DeliveryStreamName |  |
| ExecuteProcessing.Duration | Время, затрачиваемое на каждый вызов функции Lambda, выполненный Amazon Data Firehose | Миллисекунда | Multi | Region |  |
| ExecuteProcessing.Duration |  | Миллисекунда | Multi | DeliveryStreamName |  |
| ExecuteProcessing.Success | Сумма успешных вызовов функции Lambda относительно суммы всех вызовов функции Lambda | Количество | Count | Region |  |
| ExecuteProcessing.Success |  | Количество | Count | DeliveryStreamName |  |
| FailedConversion.Bytes | Размер записей, которые не удалось преобразовать | Байт | Sum | Region |  |
| FailedConversion.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| FailedConversion.Records | Количество записей, которые не удалось преобразовать | Количество | Sum | Region |  |
| FailedConversion.Records |  | Количество | Sum | DeliveryStreamName |  |
| IncomingBytes | Количество байт, успешно принятых в поток доставки за указанный период времени после регулирования | Байт | Sum | Region |  |
| IncomingBytes |  | Байт | Sum | DeliveryStreamName | Применимо |
| IncomingRecords | Количество записей, успешно принятых в поток доставки за указанный период времени после регулирования | Количество | Sum | Region |  |
| IncomingRecords |  | Количество | Sum | DeliveryStreamName | Применимо |
| KinesisMillisBehindLatest | Когда источником данных является поток данных Kinesis, эта метрика показывает количество миллисекунд, на которое последняя прочитанная запись отстаёт от новейшей записи в потоке данных Kinesis | Миллисекунда | Average | Region |  |
| KinesisMillisBehindLatest |  | Миллисекунда | Average | DeliveryStreamName |  |
| ListDeliveryStreams.Latency | Время, затраченное на одну операцию `ListDeliveryStream`, измеренное за указанный период времени | Миллисекунда | Multi | Region |  |
| ListDeliveryStreams.Latency |  | Миллисекунда | Multi | DeliveryStreamName |  |
| ListDeliveryStreams.Requests | Общее количество запросов `ListFirehose` | Количество | Sum | Region |  |
| ListDeliveryStreams.Requests |  | Количество | Sum | DeliveryStreamName |  |
| PutRecordBatch.Bytes | Количество байт, помещённых в поток доставки Amazon Data Firehose с помощью `PutRecordBatch` за указанный период времени | Байт | Sum | Region |  |
| PutRecordBatch.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| PutRecordBatch.Latency | Время, затраченное на одну операцию `PutRecordBatch`, измеренное за указанный период времени | Миллисекунда | Multi | Region |  |
| PutRecordBatch.Latency |  | Миллисекунда | Multi | DeliveryStreamName |  |
| PutRecordBatch.Records | Общее количество записей из операций `PutRecordBatch` | Количество | Sum | Region |  |
| PutRecordBatch.Records |  | Количество | Sum | DeliveryStreamName |  |
| PutRecordBatch.Requests | Общее количество запросов `PutRecordBatch` | Количество | Sum | Region |  |
| PutRecordBatch.Requests |  | Количество | Sum | DeliveryStreamName |  |
| PutRecord.Bytes | Количество байт, помещённых в поток доставки Amazon Data Firehose с помощью `PutRecord` за указанный период времени | Байт | Sum | Region |  |
| PutRecord.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| PutRecord.Latency | Время, затраченное на одну операцию `PutRecord`, измеренное за указанный период времени | Миллисекунда | Multi | Region |  |
| PutRecord.Latency |  | Миллисекунда | Multi | DeliveryStreamName |  |
| PutRecord.Requests | Общее количество запросов `PutRecord`, которое равно общему количеству записей из операций `PutRecord` | Количество | Sum | Region |  |
| PutRecord.Requests |  | Количество | Sum | DeliveryStreamName |  |
| SucceedConversion.Bytes | Размер успешно преобразованных записей | Байт | Sum | Region |  |
| SucceedConversion.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| SucceedConversion.Records | Количество успешно преобразованных записей | Количество | Sum | Region |  |
| SucceedConversion.Records |  | Количество | Sum | DeliveryStreamName |  |
| SucceedProcessing.Bytes | Количество успешно обработанных байт за указанный период времени | Байт | Sum | Region |  |
| SucceedProcessing.Bytes |  | Байт | Sum | DeliveryStreamName |  |
| SucceedProcessing.Records | Количество успешно обработанных записей за указанный период времени | Количество | Sum | Region |  |
| SucceedProcessing.Records |  | Количество | Sum | DeliveryStreamName |  |
| ThrottledDescribeStream | Общее количество случаев регулирования операции `DescribeStream`, когда источником данных является поток данных Kinesis | Количество | Average | Region |  |
| ThrottledDescribeStream |  | Количество | Average | DeliveryStreamName |  |
| ThrottledGetRecords | Общее количество случаев регулирования операции `GetRecords`, когда источником данных является поток данных Kinesis | Количество | Average | Region |  |
| ThrottledGetRecords |  | Количество | Average | DeliveryStreamName |  |
| ThrottledGetShardIterator | Общее количество случаев регулирования операции `GetShardIterator`, когда источником данных является поток данных Kinesis | Количество | Average | Region |  |
| ThrottledGetShardIterator |  | Количество | Average | DeliveryStreamName |  |
| UpdateDeliveryStream.Latency | Время, затраченное на одну операцию `UpdateDeliveryStream`, измеренное за указанный период времени | Миллисекунда | Multi | Region |  |
| UpdateDeliveryStream.Latency |  | Миллисекунда | Multi | DeliveryStreamName |  |
| UpdateDeliveryStream.Requests | Общее количество запросов `UpdateDeliveryStream` | Количество | Sum | Region |  |
| UpdateDeliveryStream.Requests |  | Количество | Sum | DeliveryStreamName |  |

### Amazon Kinesis Data Streams (KDS)

Основное измерение: `StreamName`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| GetRecords.Bytes | Количество байт, извлечённых из потока Kinesis, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют байты в одной операции `GetRecords` для потока за указанный период времени. | Байт | Sum | StreamName |  |
| GetRecords.Bytes |  | Байт | Multi | StreamName |  |
| GetRecords.Bytes |  | Байт | Count | StreamName |  |
| GetRecords.IteratorAgeMilliseconds | Возраст последней записи во всех вызовах `GetRecords`, выполненных к потоку Kinesis, измеренный за указанный период времени. Возраст представляет собой разницу между текущим временем и моментом, когда последняя запись вызова `GetRecords` была записана в поток. Статистики Minimum и Maximum можно использовать для отслеживания прогресса потребительских приложений Kinesis. Значение `0` означает, что считываемые записи полностью догнали поток. | Миллисекунда | Multi | StreamName | Применимо |
| GetRecords.IteratorAgeMilliseconds |  | Миллисекунда | Count | StreamName |  |
| GetRecords.Latency | Время, затраченное на одну операцию GetRecords, измеренное за указанный период времени | Миллисекунда | Multi | StreamName |  |
| GetRecords.Records | Количество записей, извлечённых из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют записи в одной операции `GetRecords` для потока за указанный период времени. | Количество | Sum | StreamName |  |
| GetRecords.Records |  | Количество | Multi | StreamName |  |
| GetRecords.Records |  | Количество | Count | StreamName |  |
| GetRecords.Success | Количество успешных операций `GetRecords` на поток, измеренное за указанный период времени | Количество | Sum | StreamName |  |
| GetRecords.Success |  | Количество | Average | StreamName | Применимо |
| GetRecords.Success |  | Количество | Count | StreamName |  |
| IncomingBytes | Количество байт, успешно помещённых в поток Kinesis за указанный период времени. Эта метрика включает байты из операций `PutRecord` и `PutRecords`. Статистики Minimum, Maximum и Average представляют байты в одной операции put для потока за указанный период времени. | Байт | Count | ShardId, StreamName |  |
| IncomingBytes |  | Байт | Count | StreamName |  |
| IncomingBytes |  | Байт | Multi | ShardId, StreamName |  |
| IncomingBytes |  | Байт | Multi | StreamName |  |
| IncomingBytes |  | Байт | Sum | ShardId, StreamName |  |
| IncomingBytes |  | Байт | Sum | StreamName |  |
| IncomingRecords | Количество записей, успешно помещённых в поток Kinesis за указанный период времени. Эта метрика включает количество записей из операций `PutRecord` и `PutRecords`. Статистики Minimum, Maximum и Average представляют записи в одной операции put для потока за указанный период времени. | Количество | Count | ShardId, StreamName |  |
| IncomingRecords |  | Количество | Count | StreamName |  |
| IncomingRecords |  | Количество | Multi | ShardId, StreamName |  |
| IncomingRecords |  | Количество | Multi | StreamName |  |
| IncomingRecords |  | Количество | Sum | ShardId, StreamName |  |
| IteratorAgeMilliseconds | Возраст последней записи во всех вызовах `GetRecords`, выполненных к шарду, измеренный за указанный период времени. Возраст представляет собой разницу между текущим временем и моментом, когда последняя запись вызова `GetRecords` была записана в поток. Статистики Minimum и Maximum можно использовать для отслеживания прогресса потребительских приложений Kinesis. Значение `0` означает, что считываемые записи полностью догнали поток. | Миллисекунда | Multi | StreamName, ShardId |  |
| IteratorAgeMilliseconds |  | Миллисекунда | Count | StreamName, ShardId |  |
| OutgoingBytes | Количество байт, извлечённых из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют байты, возвращённые в одной операции `GetRecords` или опубликованные в одном событии `SubscribeToShard` для шарда за указанный период времени. | Байт | Sum | StreamName, ShardId |  |
| OutgoingBytes |  | Байт | Multi | StreamName, ShardId |  |
| OutgoingBytes |  | Байт | Count | StreamName, ShardId |  |
| OutgoingRecords | Количество записей, извлечённых из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют записи, возвращённые в одной операции `GetRecords` или опубликованные в одном событии `SubscribeToShard` для шарда за указанный период времени. | Количество | Sum | StreamName, ShardId |  |
| OutgoingRecords |  | Количество | Multi | StreamName, ShardId |  |
| OutgoingRecords |  | Количество | Count | StreamName, ShardId |  |
| PutRecord.Bytes | Количество байт, помещённых в поток Kinesis с помощью операции `PutRecord` за указанный период времени | Байт | Sum | StreamName |  |
| PutRecord.Bytes |  | Байт | Multi | StreamName |  |
| PutRecord.Bytes |  | Байт | Count | StreamName |  |
| PutRecord.Latency | Время, затраченное на одну операцию `PutRecord`, измеренное за указанный период времени | Миллисекунда | Multi | StreamName |  |
| PutRecord.Success | Количество успешных операций `PutRecord` на поток Kinesis, измеренное за указанный период времени. Average отражает процент успешных записей в поток. | Количество | Sum | StreamName |  |
| PutRecord.Success |  | Количество | Average | StreamName | Применимо |
| PutRecord.Success |  | Количество | Count | StreamName |  |
| PutRecords.Bytes | Количество байт, помещённых в поток Kinesis с помощью операции `PutRecords` за указанный период времени | Байт | Sum | StreamName |  |
| PutRecords.Bytes |  | Байт | Multi | StreamName |  |
| PutRecords.Bytes |  | Байт | Count | StreamName |  |
| PutRecords.Latency | Время, затраченное на одну операцию `PutRecords`, измеренное за указанный период времени | Миллисекунда | Multi | StreamName |  |
| PutRecords.Records | Количество успешных записей в операции `PutRecords` на поток Kinesis, измеренное за указанный период времени | Количество | Sum | StreamName |  |
| PutRecords.Records |  | Количество | Multi | StreamName |  |
| PutRecords.Records |  | Количество | Count | StreamName |  |
| PutRecords.Success | Количество операций `PutRecords`, в которых успешно выполнена хотя бы одна запись, на поток Kinesis, измеренное за указанный период времени | Количество | Sum | StreamName |  |
| PutRecords.Success |  | Количество | Average | StreamName |  |
| PutRecords.Success |  | Количество | Count | StreamName |  |
| ReadProvisionedThroughputExceeded | Количество вызовов `GetRecords`, подвергнутых регулированию для потока за указанный период времени | Количество | Sum | StreamName |  |
| ReadProvisionedThroughputExceeded |  | Количество | Multi | StreamName | Применимо |
| ReadProvisionedThroughputExceeded |  | Количество | Count | StreamName |  |
| SubscribeToShardEvent.Bytes | Количество байт, полученных из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют байты, опубликованные в одном событии за указанный период времени. | Байт | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Bytes |  | Байт | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Bytes |  | Байт | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.MillisBehindLatest | Разница между текущим временем и моментом, когда последняя запись события `SubscribeToShard` была записана в поток | Миллисекунда | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.MillisBehindLatest |  | Миллисекунда | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records | Количество записей, полученных из шарда, измеренное за указанный период времени. Статистики Minimum, Maximum и Average представляют записи в одном событии за указанный период времени. | Количество | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records |  | Количество | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records |  | Количество | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success | Эта метрика отправляется каждый раз при успешной публикации события. Отправляется только при наличии активной подписки. | Количество | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success |  | Количество | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success |  | Количество | Count | StreamName, ConsumerName |  |
| SubscribeToShard.RateExceeded | Эта метрика отправляется, когда новая попытка подписки завершается неудачей, потому что уже существует активная подписка от того же потребителя, или если превышено допустимое для этой операции количество вызовов в секунду | Количество | Minimum | StreamName, ConsumerName |  |
| SubscribeToShard.Success |  | Количество | Minimum | StreamName, ConsumerName |  |
| WriteProvisionedThroughputExceeded | Количество записей, отклонённых из-за регулирования для потока за указанный период времени. Эта метрика включает регулирование из операций `PutRecord` и `PutRecords`. | Количество | Sum | StreamName |  |
| WriteProvisionedThroughputExceeded |  | Количество | Multi | StreamName | Применимо |
| WriteProvisionedThroughputExceeded |  | Количество | Count | StreamName |  |

### Amazon Kinesis Video Streams

Основное измерение: `StreamName`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| GetHLSMasterPlaylist.Latency | Задержка вызовов API `GetHLSMasterPlaylist` для данного имени потока | Миллисекунда | Multi | StreamName |  |
| GetHLSMasterPlaylist.Requests | Количество запросов API `GetHLSMasterPlaylist` для данного потока | Количество | Sum | StreamName |  |
| GetHLSMasterPlaylist.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName |  |
| GetHLSMediaPlaylist.Latency | Задержка вызовов API `GetHLSMediaPlaylist` для данного имени потока | Миллисекунда | Multi | StreamName |  |
| GetHLSMediaPlaylist.Requests | Количество запросов API `GetHLSMediaPlaylist` для данного потока | Количество | Sum | StreamName |  |
| GetHLSMediaPlaylist.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName |  |
| GetHLSStreamingSessionURL.Latency | Задержка вызовов API `GetHLSStreamingSessionURL` для данного имени потока | Миллисекунда | Multi | StreamName |  |
| GetHLSStreamingSessionURL.Requests | Количество запросов API `GetHLSStreamingSessionURL` для данного потока | Количество | Sum | StreamName |  |
| GetHLSStreamingSessionURL.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName |  |
| GetMP4InitFragment.Latency | Задержка вызовов API `GetMP4InitFragment` для данного имени потока | Миллисекунда | Multi | StreamName |  |
| GetMP4InitFragment.Requests | Количество запросов API `GetMP4InitFragment` для данного потока | Количество | Sum | StreamName |  |
| GetMP4InitFragment.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName |  |
| GetMP4MediaFragment.Latency | Задержка вызовов API `GetMP4MediaFragment` для данного имени потока | Миллисекунда | Multi | StreamName |  |
| GetMP4MediaFragment.OutgoingBytes | Общее количество байт, отправленных из сервиса в рамках API `GetMP4MediaFragment` для данного потока | Байт | Sum | StreamName |  |
| GetMP4MediaFragment.Requests | Количество запросов API `GetMP4MediaFragment` для данного потока | Количество | Sum | StreamName |  |
| GetMP4MediaFragment.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Sum | StreamName |  |
| GetMedia.ConnectionErrors | Количество соединений, которые не удалось успешно установить | Количество | Sum | StreamName | Применимо |
| GetMediaForFragmentList.OutgoingBytes | Общее количество байт, отправленных из сервиса в рамках API `GetMediaForFragmentList` для данного потока | Байт | Sum | StreamName |  |
| GetMediaForFragmentList.OutgoingFragments | Общее количество фрагментов, отправленных из сервиса в рамках API `GetMediaForFragmentList` для данного потока | Количество | Sum | StreamName |  |
| GetMediaForFragmentList.OutgoingFrames | Общее количество кадров, отправленных из сервиса в рамках API `GetMediaForFragmentList` для данного потока | Количество | Sum | StreamName |  |
| GetMediaForFragmentList.Requests | Количество запросов API `GetMediaForFragmentList` для данного потока | Количество | Sum | StreamName |  |
| GetMediaForFragmentList.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName |  |
| GetMedia.MillisBehindNow | Разница во времени между текущей серверной меткой времени и серверной меткой времени последнего отправленного фрагмента | Миллисекунда | Multi | StreamName |  |
| GetMedia.OutgoingBytes | Общее количество байт, отправленных из сервиса в рамках API `GetMedia` для данного потока | Байт | Sum | StreamName |  |
| GetMedia.OutgoingFragments | Количество фрагментов, отправленных при выполнении `GetMedia` для потока | Количество | Sum | StreamName |  |
| GetMedia.OutgoingFrames | Количество кадров, отправленных во время `GetMedia` для данного потока | Количество | Sum | StreamName |  |
| GetMedia.Requests | Количество запросов API `GetMedia` для данного потока | Количество | Sum | StreamName |  |
| GetMedia.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName | Применимо |
| ListFragments.Latency | Задержка вызовов API `ListFragments` для данного имени потока | Миллисекунда | Multi | StreamName | Применимо |
| PutMedia.ActiveConnections | Общее количество подключений к хосту сервиса | Количество | Sum | StreamName |  |
| PutMedia.BufferingAckLatency | Разница во времени между моментом, когда первый байт нового фрагмента получен Kinesis Video Streams, и моментом, когда для фрагмента отправляется `Buffering ACK` | Миллисекунда | Multi | StreamName |  |
| PutMedia.ConnectionErrors | Ошибки при установлении соединения `PutMedia` для потока | Количество | Sum | StreamName | Применимо |
| PutMedia.ErrorAckCount | Количество подтверждений Error ACK, отправленных при выполнении `PutMedia` для потока | Количество | Sum | StreamName |  |
| PutMedia.FragmentIngestionLatency | Разница во времени между моментом, когда первый и последний байты фрагмента получены Kinesis Video Streams | Миллисекунда | Multi | StreamName |  |
| PutMedia.FragmentPersistLatency | Время с момента получения и архивирования полных данных фрагмента | Миллисекунда | Multi | StreamName |  |
| PutMedia.IncomingBytes | Количество байт, полученных в рамках `PutMedia` для потока | Байт | Sum | StreamName |  |
| PutMedia.IncomingFragments | Количество полных фрагментов, полученных в рамках `PutMedia` для потока | Количество | Sum | StreamName |  |
| PutMedia.IncomingFrames | Количество полных кадров, полученных в рамках `PutMedia` для потока | Количество | Sum | StreamName |  |
| PutMedia.Latency | Разница во времени между запросом и HTTP-ответом от `InletService` при установлении соединения | Миллисекунда | Multi | StreamName |  |
| PutMedia.PersistedAckLatency | Разница во времени между моментом, когда последний байт нового фрагмента получен Kinesis Video Streams, и моментом, когда для фрагмента отправляется `Persisted ACK` | Миллисекунда | Multi | StreamName |  |
| PutMedia.ReceivedAckLatency | Разница во времени между моментом, когда последний байт нового фрагмента получен Kinesis Video Streams, и моментом, когда для фрагмента отправляется `Received ACK` | Миллисекунда | Multi | StreamName |  |
| PutMedia.Requests | Количество запросов API `PutMedia` для данного потока | Количество | Sum | StreamName |  |
| PutMedia.Success | Доля успешных запросов: значение `1` соответствует каждому успешному запросу, а значение `0` соответствует каждому сбою | Количество | Average | StreamName | Применимо |