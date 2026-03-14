---
title: Мониторинг Amazon Neptune
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-neptune
scraped: 2026-03-06T21:35:21.675210
---
# Мониторинг Amazon Neptune

# Мониторинг Amazon Neptune

* Классический
* Руководство по настройке
* 11-минутное чтение
* Опубликовано 06 июля 2020 г.

Dynatrace собирает метрики для нескольких предварительно выбранных пространств имен, включая Amazon Neptune. Вы можете просматривать метрики для каждого экземпляра службы, разделять метрики на несколько измерений и создавать пользовательские диаграммы, которые можно прикреплять к вашим панелям управления.

## Предварительные условия

Чтобы включить мониторинг для этой службы, вам необходимо:

* ActiveGate версии 1.197+

* Для развертывания Dynatrace SaaS, вам необходимо Environment ActiveGate или Multi-среду ActiveGate.

  Для доступа на основе ролей в [SaaS](../cloudwatch-metrics.md#role-based-access "Интегрируйте метрики из Amazon CloudWatch.") развертывании, вам необходимо [Environment ActiveGate](../../../dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.

* Dynatrace версии 1.200+
* Обновленную [политику мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Интегрируйте метрики из Amazon CloudWatch.") для включения дополнительных служб AWS.

Чтобы [обновить политику IAM AWS](https://dt-url.net/8q038eb), используйте JSON ниже, содержащий политику мониторинга (разрешения) для всех поддерживаемых служб.

JSON предопределенная политика для всех поддерживаемых служб

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

Если вы не хотите добавлять разрешения для всех служб и хотите выбрать разрешения только для определенных служб, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных служб AWS](../aws-all-services.md "Мониторинг всех облачных служб AWS с помощью Dynatrace и просмотр доступных метрик.") и, для каждой поддерживаемой службы, список необязательных разрешений, специфичных для этой службы.

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
| Все отслеживаемые сервисы Amazon Требуются | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
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

Пример политики JSON для одного сервиса.

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

В этом примере, из полного списка разрешений необходимо выбрать

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"` и `"ec2:DescribeAvailabilityZones"` для **Всех AWS облачных сервисов**.
### AWS конечные точки, которые должны быть доступны из ActiveGate с соответствующими AWS сервисами

| Конечная точка | Сервис |
| --- | --- |
| `autoscaling.<REGION>.amazonaws.com` | Amazon EC2 Auto Scaling (встроенный), Amazon EC2 Auto Scaling |
| `lambda.<REGION>.amazonaws.com` | AWS Lambda (встроенный), AWS Lambda |
| `elasticloadbalancing.<REGION>.amazonaws.com` | Amazon Application и Network Load Balancer (встроенный), Amazon Elastic Load Balancer (ELB) (встроенный) |
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

Чтобы узнать, как включить мониторинг служб, см. [Включение мониторинга служб](../aws-metrics-ingest/aws-enable-service-monitoring.md "Включение AWS мониторинга в Dynatrace.").

## Просмотр метрик служб

Вы можете просматривать метрики служб в вашей среде Dynatrace либо на странице **обзора пользовательского устройства**, либо на странице **Панели приборов**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы получить доступ к странице обзора пользовательского устройства

1. Перейдите к ![Технологии](https://dt-cdn.net/images/technologies-512-977161d83c.png "Технологии") **Технологии и процессы Classic**.
2. Отфильтруйте по имени службы и выберите соответствующую группу пользовательских устройств.
3. Как только вы выберете группу пользовательских устройств, вы окажетесь на странице **обзора группы пользовательских устройств**.
4. На странице **обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие к группе. Выберите экземпляр, чтобы просмотреть страницу **обзора пользовательского устройства**.

### Просмотр метрик на вашей панели приборов

После добавления службы к мониторингу предустановленная панель приборов, содержащая все рекомендуемые метрики, автоматически отображается на вашей странице **Панели приборов**. Чтобы найти конкретные панели приборов, отфильтруйте по **Предустановке**, а затем по **Имени**.

![AWS предустановки](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих отслеживаемых служб вам может потребоваться сохранить lại ваши учетные данные, чтобы предустановленная панель приборов появилась на странице **Панели приборов**. Чтобы сохранить lại ваши учетные данные, перейдите к **Настройки** > **Облачные и виртуализированные** > **AWS**, выберите желаемый экземпляр AWS, а затем выберите **Сохранить**.

Вы не можете вносить изменения в предустановленную панель приборов напрямую, но вы можете клонировать и редактировать ее. Чтобы клонировать панель приборов, откройте меню просмотра (**…**) и выберите **Клонировать**.

Чтобы удалить панель приборов со страницы панелей приборов, вы можете скрыть ее. Чтобы скрыть панель приборов, откройте меню просмотра (**…**) и выберите **Скрыть**.

Сокрытие панели приборов не влияет на других пользователей.

![Клонировать скрыть AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных панелей приборов для каждой службы AWS, см. список ниже.

### Список доступности предустановленных панелей приборов

| Служба AWS | Предустановленная панель приборов |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенная) | Не применимо |
| AWS Lambda (встроенная) | Не применимо |
| Amazon Application и Network Load Balancer (встроенная) | Не применимо |
| Amazon DynamoDB (встроенная) | Не применимо |
| Amazon EBS (встроенная) | Не применимо |
| Amazon EC2 (встроенная) | Не применимо |
| Amazon Elastic Load Balancer (ELB) (встроенная) | Не применимо |
| Amazon RDS (встроенная) | Не применимо |
| Amazon S3 (встроенная) | Не применимо |
| AWS Certificate Manager Private Certificate Authority | Не применимо |
| Все отслеживаемые службы Amazon | Не применимо |
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

![Neptune](https://dt-cdn.net/images/dashboard-27-2686-043659e494.png)
## Доступные метрики

`DBClusterIdentifier` является основным измерением.

| Имя | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| BackupRetentionPeriodStorageUsed | Общий объем хранилища резервных копий, в байтах, используемый для поддержки окна резервного копирования кластера Neptune DB | Байты | Мульти | DBClusterIdentifier |  |
| BackupRetentionPeriodStorageUsed |  | Байты | Мульти | Регион, EngineName |  |
| CPUUtilization | Процент использования процессора | Процент | Мульти | DBClusterIdentifier | Применимо |
| CPUUtilization |  | Процент | Мульти | DBClusterIdentifier | Применимо |
| CPUUtilization |  | Процент | Мульти | Регион | Применимо |
| CPUUtilization |  | Процент | Мульти | Регион, DBInstanceIdentifier | Применимо |
| CPUUtilization |  | Процент | Мульти | Регион, DatabaseClass | Применимо |
| CPUUtilization |  | Процент | Мульти | Регион, EngineName | Применимо |
| ClusterReplicaLag | Для чтения реплики, количество задержки при репликации обновлений из основной инстанции, в миллисекундах | Миллисекунды | Мульти | DBClusterIdentifier | Применимо |
| ClusterReplicaLag |  | Миллисекунды | Мульти | DBClusterIdentifier, Role | Применимо |
| ClusterReplicaLag |  | Миллисекунды | Мульти | Регион | Применимо |
| ClusterReplicaLag |  | Миллисекунды | Мульти | Регион, DBInstanceIdentifier | Применимо |
| ClusterReplicaLag |  | Миллисекунды | Мульти | Регион, DatabaseClass | Применимо |
| ClusterReplicaLag |  | Миллисекунды | Мульти | Регион, EngineName | Применимо |
| ClusterReplicaLagMaximum | Максимальное количество задержки между основной инстанцией и каждой инстанцией Neptune DB в кластере DB, в миллисекундах | Миллисекунды | Мульти | DBClusterIdentifier |  |
| ClusterReplicaLagMaximum |  | Миллисекунды | Мульти | DBClusterIdentifier, Role |  |
| ClusterReplicaLagMaximum |  | Миллисекунды | Мульти | Регион |  |
| ClusterReplicaLagMaximum |  | Миллисекунды | Мульти | Регион, DBInstanceIdentifier |  |
| ClusterReplicaLagMaximum |  | Миллисекунды | Мульти | Регион, DatabaseClass |  |
| ClusterReplicaLagMaximum |  | Миллисекунды | Мульти | Регион, EngineName |  |
| ClusterReplicaLagMinimum | Минимальное количество задержки между основной инстанцией и каждой инстанцией Neptune DB в кластере DB, в миллисекундах | Миллисекунды | Мульти | DBClusterIdentifier |  |
| ClusterReplicaLagMinimum |  | Миллисекунды | Мульти | DBClusterIdentifier, Role |  |
| ClusterReplicaLagMinimum |  | Миллисекунды | Мульти | Регион |  |
| ClusterReplicaLagMinimum |  | Миллисекунды | Мульти | Регион, DBInstanceIdentifier |  |
| ClusterReplicaLagMinimum |  | Миллисекунды | Мульти | Регион, DatabaseClass |  |
| ClusterReplicaLagMinimum |  | Миллисекунды | Мульти | Регион, EngineName |  |
| EngineUptime | Количество времени, в течение которого инстанция была запущена, в секундах | Секунды | Мульти | DBClusterIdentifier | Применимо |
| EngineUptime |  | Секунды | Мульти | DBClusterIdentifier, Role | Применимо |
| EngineUptime |  | Секунды | Мульти | Регион | Применимо |
| EngineUptime |  | Секунды | Мульти | Регион, DBInstanceIdentifier | Применимо |
| EngineUptime |  | Секунды | Мульти | Регион, DatabaseClass | Применимо |
| EngineUptime |  | Секунды | Мульти | Регион, EngineName | Применимо |
| FreeableMemory | Количество доступной оперативной памяти, в байтах | Байты | Мульти | DBClusterIdentifier | Применимо |
| FreeableMemory |  | Байты | Мульти | DBClusterIdentifier, Role | Применимо |
| FreeableMemory |  | Байты | Мульти | Регион | Применимо |
| FreeableMemory |  | Байты | Мульти | Регион, DBInstanceIdentifier | Применимо |
| FreeableMemory |  | Байты | Мульти | Регион, DatabaseClass | Применимо |
| FreeableMemory |  | Байты | Мульти | Регион, EngineName | Применимо |
| GremlinRequestsPerSec | Количество запросов в секунду к движку Gremlin | Запросы/секунда | Мульти | DBClusterIdentifier | Применимо |
| GremlinRequestsPerSec |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| GremlinRequestsPerSec |  | Запросы/секунда | Мульти | Регион | Применимо |
| GremlinRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| GremlinRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DatabaseClass | Применимо |
| GremlinRequestsPerSec |  | Запросы/секунда | Мульти | Регион, EngineName | Применимо |
| GremlinWebSocketOpenConnections | Количество открытых подключений WebSocket к Neptune | Подключения/секунда | Мульти | DBClusterIdentifier |  |
| GremlinWebSocketOpenConnections |  | Подключения/секунда | Мульти | DBClusterIdentifier, Role |  |
| GremlinWebSocketOpenConnections |  | Подключения/секунда | Мульти | Регион |  |
| GremlinWebSocketOpenConnections |  | Подключения/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| GremlinWebSocketOpenConnections |  | Подключения/секунда | Мульти | Регион, DatabaseClass |  |
| GremlinWebSocketOpenConnections |  | Подключения/секунда | Мульти | Регион, EngineName |  |
| LoaderRequestsPerSec | Количество запросов загрузчика в секунду | Запросы/секунда | Мульти | DBClusterIdentifier |  |
| LoaderRequestsPerSec |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role |  |
| LoaderRequestsPerSec |  | Запросы/секунда | Мульти | Регион |  |
| LoaderRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| LoaderRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DatabaseClass |  |
| LoaderRequestsPerSec |  | Запросы/секунда | Мульти | Регион, EngineName |  |
| MainRequestQueuePendingRequests | Количество запросов, ожидающих в очереди ввода, ожидая выполнения. Neptune начинает ограничивать запросы, когда они превышают максимальную емкость очереди | Запросы/секунда | Мульти | DBClusterIdentifier | Применимо |
| MainRequestQueuePendingRequests |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| MainRequestQueuePendingRequests |  | Запросы/секунда | Мульти | Регион | Применимо |
| MainRequestQueuePendingRequests |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| MainRequestQueuePendingRequests |  | Запросы/секунда | Мульти | Регион, DatabaseClass | Применимо |
| MainRequestQueuePendingRequests |  | Запросы/секунда | Мульти | Регион, EngineName | Применимо |
| NetworkReceiveThroughput | Входящий (принимающий) сетевой трафик на экземпляре DB, включая как трафик базы данных клиента, так и трафик Neptune, используемый для мониторинга и репликации, в байтах/секунду | Байты/секунда | Мульти | DBClusterIdentifier |  |
| NetworkReceiveThroughput |  | Байты/секунда | Мульти | DBClusterIdentifier, Role |  |
| NetworkReceiveThroughput |  | Байты/секунда | Мульти | Регион |  |
| NetworkReceiveThroughput |  | Байты/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| NetworkReceiveThroughput |  | Байты/секунда | Мульти | Регион, DatabaseClass |  |
| NetworkReceiveThroughput |  | Байты/секунда | Мульти | Регион, EngineName |  |
| NetworkThroughput | Объем сетевого трафика, принимаемого и передаваемого клиентам каждой инстанцией в кластере DB Neptune, в байтах в секунду. Этот трафик не включает сетевой трафик между инстанциями в кластере DB и томом кластера. | Байты/секунда | Мульти | DBClusterIdentifier | Применимо |
| NetworkThroughput |  | Байты/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| NetworkThroughput |  | Байты/секунда | Мульти | Регион | Применимо |
| NetworkThroughput |  | Байты/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| NetworkThroughput |  | Байты/секунда | Мульти | Регион, DatabaseClass | Применимо |
| NetworkThroughput |  | Байты/секунда | Мульти | Регион, EngineName | Применимо |
| NetworkTransmitThroughput | Исходящий (передающий) сетевой трафик на экземпляре DB, включая как трафик базы данных клиента, так и трафик Neptune, используемый для мониторинга и репликации, в байтах/секунду | Байты/секунда | Мульти | DBClusterIdentifier |  |
| NetworkTransmitThroughput |  | Байты/секунда | Мульти | DBClusterIdentifier, Role |  |
| NetworkTransmitThroughput |  | Байты/секунда | Мульти | Регион |  |
| NetworkTransmitThroughput |  | Байты/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| NetworkTransmitThroughput |  | Байты/секунда | Мульти | Регион, DatabaseClass |  |
| NetworkTransmitThroughput |  | Байты/секунда | Мульти | Регион, EngineName |  |
| NumTxCommitted | Количество успешно выполненных транзакций в секунду | Запросы/секунда | Мульти | DBClusterIdentifier |  |
| NumTxCommitted |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role |  |
| NumTxCommitted |  | Запросы/секунда | Мульти | Регион |  |
| NumTxCommitted |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| NumTxCommitted |  | Запросы/секунда | Мульти | Регион, DatabaseClass |  |
| NumTxCommitted |  | Запросы/секунда | Мульти | Регион, EngineName |  |
| NumTxOpened | Количество открытых транзакций на сервере в секунду | Запросы/секунда | Мульти | DBClusterIdentifier |  |
| NumTxOpened |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role |  |
| NumTxOpened |  | Запросы/секунда | Мульти | Регион |  |
| NumTxOpened |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| NumTxOpened |  | Запросы/секунда | Мульти | Регион, DatabaseClass |  |
| NumTxOpened |  | Запросы/секунда | Мульти | Регион, EngineName |  |
| NumTxRolledBack | Количество отмененных транзакций в секунду на сервере из-за ошибок | Запросы/секунда | Мульти | DBClusterIdentifier |  |
| NumTxRolledBack |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role |  |
| NumTxRolledBack |  | Запросы/секунда | Мульти | Регион |  |
| NumTxRolledBack |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier |  |
| NumTxRolledBack |  | Запросы/секунда | Мульти | Регион, DatabaseClass |  |
| NumTxRolledBack |  | Запросы/секунда | Мульти | Регион, EngineName |  |
| SnapshotStorageUsed | Общий объем хранилища резервных копий, потребляемый всеми снимками для кластера DB Neptune вне окна резервного копирования, в байтах | Байты | Мульти | DBClusterIdentifier |  |
| SnapshotStorageUsed |  | Байты | Мульти | Регион, EngineName |  |
| SparqlRequestsPerSec | Количество запросов в секунду к движку SPARQL | Запросы/секунда | Мульти | DBClusterIdentifier | Применимо |
| SparqlRequestsPerSec |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| SparqlRequestsPerSec |  | Запросы/секунда | Мульти | Регион | Применимо |
| SparqlRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| SparqlRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DatabaseClass | Применимо |
| SparqlRequestsPerSec |  | Запросы/секунда | Мульти | Регион, EngineName | Применимо |
| TotalBackupStorageBilled | Общий объем хранилища резервных копий, за который вы будете выставлены счет, для заданного кластера DB Neptune, в байтах | Байты | Мульти | DBClusterIdentifier |  |
| TotalBackupStorageBilled |  | Байты | Мульти | Регион, EngineName |  |
| TotalClientErrorsPerSec | Общее количество ошибок в секунду, возникших из-за проблем на стороне клиента | Ошибки/секунда | Мульти | DBClusterIdentifier | Применимо |
| TotalClientErrorsPerSec |  | Ошибки/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| TotalClientErrorsPerSec |  | Ошибки/секунда | Мульти | Регион | Применимо |
| TotalClientErrorsPerSec |  | Ошибки/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| TotalClientErrorsPerSec |  | Ошибки/секунда | Мульти | Регион, DatabaseClass | Применимо |
| TotalClientErrorsPerSec |  | Ошибки/секунда | Мульти | Регион, EngineName | Применимо |
| TotalRequestsPerSec | Общее количество запросов в секунду к серверу со всех источников | Запросы/секунда | Мульти | DBClusterIdentifier | Применимо |
| TotalRequestsPerSec |  | Запросы/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| TotalRequestsPerSec |  | Запросы/секунда | Мульти | Регион | Применимо |
| TotalRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| TotalRequestsPerSec |  | Запросы/секунда | Мульти | Регион, DatabaseClass | Применимо |
| TotalRequestsPerSec |  | Запросы/секунда | Мульти | Регион, EngineName | Применимо |
| TotalServerErrorsPerSec | Общее количество ошибок в секунду, возникших на сервере из-за внутренних сбоев | Ошибки/секунда | Мульти | DBClusterIdentifier | Применимо |
| TotalServerErrorsPerSec |  | Ошибки/секунда | Мульти | DBClusterIdentifier, Role | Применимо |
| TotalServerErrorsPerSec |  | Ошибки/секунда | Мульти | Регион | Применимо |
| TotalServerErrorsPerSec |  | Ошибки/секунда | Мульти | Регион, DBInstanceIdentifier | Применимо |
| TotalServerErrorsPerSec |  | Ошибки/секунда | Мульти | Регион, DatabaseClass | Применимо |
| TotalServerErrorsPerSec |  | Ошибки/секунда | Мульти | Регион, EngineName | Применимо |
| VolumeBytesUsed | Общий объем хранилища, выделенного для кластера DB Neptune, в байтах. Это объем хранилища, за который вы будете выставлены счет. Это максимальный объем хранилища, выделенный для вашего кластера DB, а не объем, который вы сейчас используете. | Байты | Мульти | DBClusterIdentifier | Применимо |
| VolumeBytesUsed | Объем хранилища, используемый вашей инстанцией DB Neptune, в байтах. | Байты | Мульти | Регион, EngineName | Применимо |
| VolumeBytesLeftTotal | Остаток доступного пространства для тома кластера, измеряемый в байтах | Байты | Мульти | DBClusterIdentifier | Применимо |
| VolumeBytesLeftTotal |  | Байты | Мульти | Регион | Применимо |
| VolumeBytesLeftTotal |  | Байты | Мульти | Регион, EngineName | Применимо |
| VolumeReadIOPs | Среднее количество операций ввода-вывода чтения с тома кластера, сообщаемое с интервалом 5 минут. | Байты | Мульти | DBClusterIdentifier | Применимо |
| VolumeReadIOPs |  | Байты | Мульти | Регион, EngineName | Применимо |
| VolumeWriteIOPs | Среднее количество операций ввода-вывода записи на том кластера, сообщаемое с интервалом 5 минут | Байты | Мульти | DBClusterIdentifier | Применимо |
| VolumeWriteIOPs |  | Байты | Мульти | Регион, EngineName | Применимо |