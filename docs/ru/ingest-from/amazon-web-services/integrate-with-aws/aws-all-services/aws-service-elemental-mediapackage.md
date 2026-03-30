---
title: Мониторинг AWS Elemental MediaPackage (Live, Video on Demand)
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediapackage
scraped: 2026-03-05T21:40:02.914135
---

* 5 минут чтения

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имён, включая AWS Elemental MediaPackage (Live, Video on Demand). Вы можете просматривать метрики для каждого экземпляра сервиса, разбивать метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга этого сервиса необходимо:

* Environment или Cluster ActiveGate версии 1.197+
* Для AWS Elemental MediaPackage Live — Dynatrace версии 1.203+
* Для AWS Elemental MediaPackage Video on Demand — Dynatrace версии 1.204+
* Обновлённая [политика мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных AWS сервисов.
  Для [обновления политики AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) используйте JSON ниже.

Предопределённая политика в формате JSON

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

### Конечные точки AWS, доступные из ActiveGate, и соответствующие сервисы AWS

| Конечная точка | Сервис |
| --- | --- |
| `autoscaling.<REGION>.amazonaws.com` | Amazon EC2 Auto Scaling (встроенный), Amazon EC2 Auto Scaling |
| `lambda.<REGION>.amazonaws.com` | AWS Lambda (встроенный), AWS Lambda |
| `elasticloadbalancing.<REGION>.amazonaws.com` | Amazon Application and Network Load Balancer (встроенный), Amazon Elastic Load Balancer (ELB) (встроенный) |
| `dynamodb.<REGION>.amazonaws.com` | Amazon DynamoDB (встроенный), Amazon DynamoDB |
| `ec2.<REGION>.amazonaws.com` | Amazon EBS (встроенный), Amazon EC2 (встроенный), Amazon EBS, Amazon EC2 Spot Fleet, Amazon VPC NAT Gateways, AWS Transit Gateway, AWS Site-to-Site VPN |
| `rds.<REGION>.amazonaws.com` | Amazon RDS (встроенный), Amazon Aurora, Amazon DocumentDB, Amazon Neptune, Amazon RDS |
| `s3.<REGION>.amazonaws.com` | Amazon S3 (встроенный) |
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

Чтобы узнать, как включить мониторинг сервиса, см. раздел Включение мониторинга сервиса.

## Просмотр метрик сервиса

Метрики сервиса можно просматривать в среде Dynatrace на **странице обзора пользовательских устройств** или на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательских устройств

Для доступа к странице обзора пользовательских устройств:

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по названию сервиса и выберите нужную группу пользовательских устройств.
3. После выбора группы пользовательских устройств откроется **страница обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), входящие в группу. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

После добавления сервиса в мониторинг предустановленная панель мониторинга со всеми рекомендованными метриками автоматически появляется на странице **Панели мониторинга**. Для поиска конкретных панелей используйте фильтры **Preset** и **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленная панель появилась на странице **Панели мониторинга**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вносить изменения непосредственно в предустановленную панель нельзя, но её можно клонировать и редактировать. Для клонирования панели откройте меню обзора (**â¦**) и выберите **Clone**.

Чтобы убрать панель со страницы панелей мониторинга, её можно скрыть. Для скрытия панели откройте меню обзора (**â¦**) и выберите **Hide**.

Скрытие панели не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Для проверки доступности предустановленных панелей по каждому сервису AWS см. список ниже.

### Список доступности предустановленных панелей

| Сервис AWS | Предустановленная панель |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Неприменимо |
| AWS Lambda (встроенный) | Неприменимо |
| Amazon Application and Network Load Balancer (встроенный) | Неприменимо |
| Amazon DynamoDB (встроенный) | Неприменимо |
| Amazon EBS (встроенный) | Неприменимо |
| Amazon EC2 (встроенный) | Неприменимо |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Неприменимо |
| Amazon RDS (встроенный) | Неприменимо |
| Amazon S3 (встроенный) | Неприменимо |
| AWS Certificate Manager Private Certificate Authority | Неприменимо |
| Все отслеживаемые сервисы Amazon | Неприменимо |
| Amazon API Gateway | Неприменимо |
| AWS App Runner | Неприменимо |
| Amazon AppStream | Применимо |
| AWS AppSync | Применимо |
| Amazon Athena | Применимо |
| Amazon Aurora | Неприменимо |
| Amazon EC2 Auto Scaling | Применимо |
| AWS Billing | Применимо |
| Amazon Keyspaces | Применимо |
| AWS Chatbot | Применимо |
| Amazon CloudFront | Неприменимо |
| AWS CloudHSM | Применимо |
| Amazon CloudSearch | Применимо |
| AWS CodeBuild | Применимо |
| Amazon Cognito | Неприменимо |
| Amazon Connect | Применимо |
| AWS DataSync | Применимо |
| Amazon DynamoDB Accelerator (DAX) | Применимо |
| AWS Database Migration Service (AWS DMS) | Применимо |
| Amazon DocumentDB | Применимо |
| AWS Direct Connect | Применимо |
| Amazon DynamoDB | Неприменимо |
| Amazon EBS | Неприменимо |
| Amazon EC2 Spot Fleet | Неприменимо |
| Amazon EC2 API | Применимо |
| Amazon Elastic Container Service (ECS) | Неприменимо |
| Amazon ECS Container Insights | Применимо |
| Amazon Elastic File System (EFS) | Неприменимо |
| Amazon Elastic Kubernetes Service (EKS) | Применимо |
| Amazon ElastiCache (EC) | Неприменимо |
| AWS Elastic Beanstalk | Применимо |
| Amazon Elastic Inference | Применимо |
| Amazon Elastic Transcoder | Применимо |
| Amazon Elastic Map Reduce (EMR) | Неприменимо |
| Amazon Elasticsearch Service (ES) | Неприменимо |
| Amazon EventBridge | Применимо |
| Amazon FSx | Применимо |
| Amazon GameLift | Применимо |
| AWS Glue | Неприменимо |
| Amazon Inspector | Применимо |
| AWS Internet of Things (IoT) | Неприменимо |
| AWS IoT Things Graph | Применимо |
| AWS IoT Analytics | Применимо |
| Amazon Managed Streaming for Kafka | Применимо |
| Amazon Kinesis Data Analytics | Неприменимо |
| Amazon Data Firehose | Неприменимо |
| Amazon Kinesis Data Streams | Неприменимо |
| Amazon Kinesis Video Streams | Неприменимо |
| AWS Lambda | Неприменимо |
| Amazon Lex | Применимо |
| Amazon CloudWatch Logs | Применимо |
| AWS Elemental MediaTailor | Применимо |
| AWS Elemental MediaConnect | Применимо |
| AWS Elemental MediaConvert | Применимо |
| AWS Elemental MediaPackage Live | Применимо |
| AWS Elemental MediaPackage Video on Demand | Применимо |
| Amazon MQ | Применимо |
| Amazon VPC NAT Gateways | Неприменимо |
| Amazon Neptune | Применимо |
| AWS OpsWorks | Применимо |
| Amazon Polly | Применимо |
| Amazon QLDB | Применимо |
| Amazon RDS | Неприменимо |
| Amazon Redshift | Неприменимо |
| Amazon Rekognition | Применимо |
| AWS RoboMaker | Применимо |
| Amazon Route 53 | Применимо |
| Amazon Route 53 Resolver | Применимо |
| Amazon S3 | Неприменимо |
| Amazon SageMaker Batch Transform Jobs | Неприменимо |
| Amazon SageMaker Endpoints | Неприменимо |
| Amazon SageMaker Endpoint Instances | Неприменимо |
| Amazon SageMaker Ground Truth | Неприменимо |
| Amazon SageMaker Processing Jobs | Неприменимо |
| Amazon SageMaker Training Jobs | Неприменимо |
| AWS Service Catalog | Применимо |
| Amazon Simple Email Service (SES) | Неприменимо |
| Amazon Simple Notification Service (SNS) | Неприменимо |
| Amazon Simple Queue Service (SQS) | Неприменимо |
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

![Media dash](https://dt-cdn.net/images/2021-03-12-09-22-34-1758-2921e2b7ab.png)

![Vod dash](https://dt-cdn.net/images/dashboard-89-1240-9c7a554fa3.png)

## Доступные метрики

### AWS Elemental MediaPackage Live

`Channel` — основное измерение.

| Название | Описание | Единица | Статистика | Измерения | Рекомендовано |
| --- | --- | --- | --- | --- | --- |
| ActiveInput | Указывает, использовался ли входной поток в качестве источника для конечной точки в AWS Elemental MediaPackage (был ли он активен). Значение `1` означает, что входной поток был активен, `0` (ноль) — что не был. | Count | Multi | Region, IngestEndpoint, OriginEndpoint |  |
| EgressBytes | Количество байт, которое AWS Elemental MediaPackage успешно отправляет для каждого запроса. Если MediaPackage не получает запросов на вывод в указанный интервал, данные не предоставляются. | Bytes | Multi | Channel | Применимо |
| EgressBytes |  | Bytes | Sum | Channel | Применимо |
| EgressBytes |  | Count | Count | Channel |  |
| EgressBytes |  | Bytes | Multi | Channel, OriginEndpoint |  |
| EgressBytes |  | Bytes | Sum | Channel, OriginEndpoint | Применимо |
| EgressBytes |  | Count | Count | Channel, OriginEndpoint |  |
| EgressBytes |  | Bytes | Multi | Region | Применимо |
| EgressBytes |  | Bytes | Sum | Region | Применимо |
| EgressBytes |  | Count | Count | Region | Применимо |
| EgressRequestCount | Количество запросов контента, получаемых AWS Elemental MediaPackage. Если MediaPackage не получает запросов на вывод в указанный интервал, данные не предоставляются. | Count | Sum | Channel | Применимо |
| EgressRequestCount |  | Count | Sum | Channel, OriginEndpoint |  |
| EgressRequestCount |  | Count | Sum | Channel, StatusCodeRange | Применимо |
| EgressRequestCount |  | Count | Sum | Channel, OriginEndpoint, StatusCodeRange |  |
| EgressRequestCount |  | Count | Sum | Region, StatusCodeRange |  |
| EgressRequestCount |  | Count | Sum | Region | Применимо |
| EgressResponseTime | Время, которое требуется AWS Elemental MediaPackage для обработки каждого запроса на вывод. Если MediaPackage не получает запросов на вывод в указанный интервал, данные не предоставляются. | Milliseconds | Multi | Channel | Применимо |
| EgressResponseTime |  | Milliseconds | Sum | Channel | Применимо |
| EgressResponseTime |  | Count | Count | Channel |  |
| EgressResponseTime |  | Milliseconds | Multi | Channel, OriginEndpoint | Применимо |
| EgressResponseTime |  | Milliseconds | Sum | Channel, OriginEndpoint |  |
| EgressResponseTime |  | Count | Count | Channel, OriginEndpoint |  |
| IngressBytes | Количество байт контента, получаемых AWS Elemental MediaPackage для каждого входящего запроса. Если MediaPackage не получает запросов на ввод в указанный интервал, данные не предоставляются. | Bytes | Multi | Channel | Применимо |
| IngressBytes |  | Bytes | Sum | Channel | Применимо |
| IngressBytes |  | Count | Count | Channel |  |
| IngressBytes |  | Bytes | Multi | Channel, IngestEndpoint | Применимо |
| IngressBytes |  | Bytes | Sum | Channel, IngestEndpoint |  |
| IngressBytes |  | Count | Count | Channel, IngestEndpoint |  |
| IngressBytes |  | Bytes | Multi | Region |  |
| IngressBytes |  | Bytes | Sum | Region |  |
| IngressBytes |  | Count | Count | Region |  |
| IngressResponseTime | Время, которое требуется AWS Elemental MediaPackage для обработки каждого входящего запроса. Если MediaPackage не получает запросов на ввод в указанный интервал, данные не предоставляются. | Milliseconds | Multi | Channel | Применимо |
| IngressResponseTime |  | Milliseconds | Sum | Channel | Применимо |
| IngressResponseTime |  | Count | Count | Channel |  |
| IngressResponseTime |  | Milliseconds | Multi | Channel, IngestEndpoint | Применимо |
| IngressResponseTime |  | Milliseconds | Sum | Channel, IngestEndpoint |  |
| IngressResponseTime |  | Count | Count | Channel, IngestEndpoint |  |
| IngressResponseTime |  | Milliseconds | Multi | Region |  |
| IngressResponseTime |  | Milliseconds | Sum | Region |  |
| IngressResponseTime |  | Count | Count | Region |  |

### AWS Elemental MediaPackage Video on Demand (VOD)

`PackagingConfiguration` — основное измерение.

| Название | Описание | Единица | Статистика | Измерения | Рекомендовано |
| --- | --- | --- | --- | --- | --- |
| EgressBytes | Количество байт, которое AWS Elemental MediaPackage успешно отправляет для каждого запроса. Если MediaPackage не получает запросов на вывод в указанный интервал, данные не предоставляются. | Bytes | Multi | PackagingConfiguration | Применимо |
| EgressBytes |  | Bytes | Sum | PackagingConfiguration | Применимо |
| EgressBytes |  | Count | Count | PackagingConfiguration |  |
| EgressRequestCount | Количество запросов контента, получаемых AWS Elemental MediaPackage. Если MediaPackage не получает запросов на вывод в указанный интервал, данные не предоставляются. | Count | Sum | PackagingConfiguration | Применимо |
| EgressRequestCount |  | Count | Sum | PackagingConfiguration, StatusCodeRange |  |
| EgressResponseTime | Время, которое требуется AWS Elemental MediaPackage для обработки каждого запроса на вывод. Если MediaPackage не получает запросов на вывод в указанный интервал, данные не предоставляются. | Milliseconds | Multi | PackagingConfiguration | Применимо |
| EgressResponseTime |  | Milliseconds | Sum | PackagingConfiguration | Применимо |
| EgressResponseTime |  | Count | Count | PackagingConfiguration |  |
