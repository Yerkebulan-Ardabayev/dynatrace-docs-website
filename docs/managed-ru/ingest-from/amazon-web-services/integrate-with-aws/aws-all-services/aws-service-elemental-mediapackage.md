---
title: Мониторинг AWS Elemental MediaPackage (Live, Video on Demand)
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediapackage
scraped: 2026-05-12T11:28:35.741078
---

# Мониторинг AWS Elemental MediaPackage (Live, Video on Demand)

# Мониторинг AWS Elemental MediaPackage (Live, Video on Demand)

* Практическое руководство
* Чтение: 5 мин
* Опубликовано 6 июля 2020 г.

Dynatrace принимает метрики для множества предопределённых пространств имён, включая AWS Elemental MediaPackage (Live, Video on Demand). Можно просматривать метрики по каждому экземпляру сервиса, разбивать их на несколько измерений и создавать собственные графики, которые можно закреплять на дашбордах.

## Предварительные требования

Чтобы включить мониторинг этого сервиса, необходимо

* Environment ActiveGate или Cluster ActiveGate версия 1.197+
* Для AWS Elemental MediaPackage Live, Dynatrace версия 1.203+
* Для AWS Elemental MediaPackage Video on Demand, Dynatrace версия 1.204+
* Обновлённая [политика мониторинга AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Приём метрик Amazon CloudWatch."), включающая дополнительные сервисы AWS.
  Чтобы [обновить политику AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведённый ниже JSON.

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

![Media dash](https://dt-cdn.net/images/2021-03-12-09-22-34-1758-2921e2b7ab.png)

Media dash

![Vod dash](https://dt-cdn.net/images/dashboard-89-1240-9c7a554fa3.png)

Vod dash

## Доступные метрики

### AWS Elemental MediaPackage Live

Основное измерение: `Channel`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| ActiveInput | Указывает, использовался ли вход в качестве источника для конечной точки в AWS Elemental MediaPackage (был ли он активен). Значение `1` означает, что вход был активен, а `0` (ноль) означает, что нет. | Количество | Multi | Region, IngestEndpoint, OriginEndpoint |  |
| EgressBytes | Количество байт, которые AWS Elemental MediaPackage успешно отправляет на каждый запрос. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются. | Байт | Multi | Channel | Применимо |
| EgressBytes |  | Байт | Sum | Channel | Применимо |
| EgressBytes |  | Количество | Count | Channel |  |
| EgressBytes |  | Байт | Multi | Channel, OriginEndpoint |  |
| EgressBytes |  | Байт | Sum | Channel, OriginEndpoint | Применимо |
| EgressBytes |  | Количество | Count | Channel, OriginEndpoint |  |
| EgressBytes |  | Байт | Multi | Region | Применимо |
| EgressBytes |  | Байт | Sum | Region | Применимо |
| EgressBytes |  | Количество | Count | Region | Применимо |
| EgressRequestCount | Количество запросов контента, которые получает AWS Elemental MediaPackage. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются. | Количество | Sum | Channel | Применимо |
| EgressRequestCount |  | Количество | Sum | Channel, OriginEndpoint |  |
| EgressRequestCount |  | Количество | Sum | Channel, StatusCodeRange | Применимо |
| EgressRequestCount |  | Количество | Sum | Channel, OriginEndpoint, StatusCodeRange |  |
| EgressRequestCount |  | Количество | Sum | Region, StatusCodeRange |  |
| EgressRequestCount |  | Количество | Sum | Region | Применимо |
| EgressResponseTime | Время, которое требуется AWS Elemental MediaPackage для обработки каждого запроса на вывод. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются. | Миллисекунда | Multi | Channel | Применимо |
| EgressResponseTime |  | Миллисекунда | Sum | Channel | Применимо |
| EgressResponseTime |  | Количество | Count | Channel |  |
| EgressResponseTime |  | Миллисекунда | Multi | Channel, OriginEndpoint | Применимо |
| EgressResponseTime |  | Миллисекунда | Sum | Channel, OriginEndpoint |  |
| EgressResponseTime |  | Количество | Count | Channel, OriginEndpoint |  |
| IngressBytes | Количество байт контента, которые AWS Elemental MediaPackage получает на каждый входной запрос. Если MediaPackage не получает входных запросов в течение указанного интервала, данные не предоставляются. | Байт | Multi | Channel | Применимо |
| IngressBytes |  | Байт | Sum | Channel | Применимо |
| IngressBytes |  | Количество | Count | Channel |  |
| IngressBytes |  | Байт | Multi | Channel, IngestEndpoint | Применимо |
| IngressBytes |  | Байт | Sum | Channel, IngestEndpoint |  |
| IngressBytes |  | Количество | Count | Channel, IngestEndpoint |  |
| IngressBytes |  | Байт | Multi | Region |  |
| IngressBytes |  | Байт | Sum | Region |  |
| IngressBytes |  | Количество | Count | Region |  |
| IngressResponseTime | Время, которое требуется AWS Elemental MediaPackage для обработки каждого входного запроса. Если MediaPackage не получает входных запросов в течение указанного интервала, данные не предоставляются. | Миллисекунда | Multi | Channel | Применимо |
| IngressResponseTime |  | Миллисекунда | Sum | Channel | Применимо |
| IngressResponseTime |  | Количество | Count | Channel |  |
| IngressResponseTime |  | Миллисекунда | Multi | Channel, IngestEndpoint | Применимо |
| IngressResponseTime |  | Миллисекунда | Sum | Channel, IngestEndpoint |  |
| IngressResponseTime |  | Количество | Count | Channel, IngestEndpoint |  |
| IngressResponseTime |  | Миллисекунда | Multi | Region |  |
| IngressResponseTime |  | Миллисекунда | Sum | Region |  |
| IngressResponseTime |  | Количество | Count | Region |  |

### AWS Elemental MediaPackage Video on Demand (VOD)

Основное измерение: `PackagingConfiguration`.

| Имя | Описание | Единица измерения | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| EgressBytes | Количество байт, которые AWS Elemental MediaPackage успешно отправляет на каждый запрос. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются. | Байт | Multi | PackagingConfiguration | Применимо |
| EgressBytes |  | Байт | Sum | PackagingConfiguration | Применимо |
| EgressBytes |  | Количество | Count | PackagingConfiguration |  |
| EgressRequestCount | Количество запросов контента, которые получает AWS Elemental MediaPackage. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются. | Количество | Sum | PackagingConfiguration | Применимо |
| EgressRequestCount |  | Количество | Sum | PackagingConfiguration, StatusCodeRange |  |
| EgressResponseTime | Время, которое требуется AWS Elemental MediaPackage для обработки каждого запроса на вывод. Если MediaPackage не получает запросов на вывод в течение указанного интервала, данные не предоставляются. | Миллисекунда | Multi | PackagingConfiguration | Применимо |
| EgressResponseTime |  | Миллисекунда | Sum | PackagingConfiguration | Применимо |
| EgressResponseTime |  | Количество | Count | PackagingConfiguration |  |