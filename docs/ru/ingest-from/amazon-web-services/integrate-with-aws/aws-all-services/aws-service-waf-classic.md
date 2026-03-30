---
title: Мониторинг AWS WAF Classic
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-waf-classic
scraped: 2026-03-02T21:20:45.764703
---

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая AWS WAF Classic. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate версии 1.197+

* Для развёртываний Dynatrace SaaS вам потребуется Environment ActiveGate или Multi-environment ActiveGate.

  Для доступа на основе ролей в развёртывании [SaaS](../cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") вам необходим Environment ActiveGate, установленный на хосте Amazon EC2.

* Dynatrace версии 1.200+
* Обновлённая [политика мониторинга AWS](../cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.

Чтобы [обновить политику AWS IAM](https://dt-url.net/8q038eb), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов, а хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для всех облачных сервисов AWS, и для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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

Чтобы узнать, как включить мониторинг сервиса, см. Включение мониторинга сервиса.

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Дашборды**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы открыть страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг предустановленный дашборд, содержащий все рекомендуемые метрики, автоматически появляется на странице **Дашборды**. Для поиска определённых дашбордов отфильтруйте по **Предустановленные**, а затем по **Имени**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих отслеживаемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Дашборды**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню (**...**) и выберите **Clone**.

Чтобы удалить дашборд со страницы дашбордов, вы можете скрыть его. Чтобы скрыть дашборд, откройте меню (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных дашбордов для каждого сервиса AWS, см. список ниже.

### Список доступности предустановленных дашбордов

| Сервис AWS | Предустановленный дашборд |
| --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | Недоступен |
| AWS Lambda (встроенный) | Недоступен |
| Amazon Application and Network Load Balancer (встроенный) | Недоступен |
| Amazon DynamoDB (встроенный) | Недоступен |
| Amazon EBS (встроенный) | Недоступен |
| Amazon EC2 (встроенный) | Недоступен |
| Amazon Elastic Load Balancer (ELB) (встроенный) | Недоступен |
| Amazon RDS (встроенный) | Недоступен |
| Amazon S3 (встроенный) | Недоступен |
| AWS Certificate Manager Private Certificate Authority | Недоступен |
| Все отслеживаемые сервисы Amazon | Недоступен |
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

![Waf clas](https://dt-cdn.net/images/2021-03-12-10-19-01-1673-9b97e50433.png)

## Доступные метрики

`WebACL` является основным измерением.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуется |
| --- | --- | --- | --- | --- | --- |
| AllowedRequests | Количество разрешённых веб-запросов | Количество | Сумма | WebACL, Region, Rule | Да |
| AllowedRequests |  | Количество | Сумма | WebACL, Region, RuleGroup | Да |
| AllowedRequests |  | Количество | Сумма | Region, Rule, RuleGroup | Да |
| AllowedRequests |  | Количество | Сумма | WebACL, Rule | Да |
| AllowedRequests |  | Количество | Сумма | WebACL, RuleGroup | Да |
| BlockedRequests | Количество заблокированных веб-запросов | Количество | Сумма | WebACL, Region, Rule | Да |
| BlockedRequests |  | Количество | Сумма | WebACL, Region, RuleGroup | Да |
| BlockedRequests |  | Количество | Сумма | Region, Rule, RuleGroup | Да |
| BlockedRequests |  | Количество | Сумма | WebACL, Rule | Да |
| BlockedRequests |  | Количество | Сумма | WebACL, RuleGroup | Да |
| CountedRequests | Количество подсчитанных веб-запросов | Количество | Сумма | WebACL, Region, Rule | Да |
| CountedRequests |  | Количество | Сумма | WebACL, Region, RuleGroup | Да |
| CountedRequests |  | Количество | Сумма | Region, Rule, RuleGroup | Да |
| CountedRequests |  | Количество | Сумма | WebACL, Rule | Да |
| CountedRequests |  | Количество | Сумма | WebACL, RuleGroup | Да |
| PassedRequests | Количество пропущенных запросов для группы правил | Количество | Сумма | WebACL, Region, Rule | Да |
| PassedRequests |  | Количество | Сумма | WebACL, Region, RuleGroup | Да |
| PassedRequests |  | Количество | Сумма | Region, Rule, RuleGroup | Да |
| PassedRequests |  | Количество | Сумма | WebACL, Rule | Да |
| PassedRequests |  | Количество | Сумма | WebACL, RuleGroup | Да |

## Ограничения

Сущности Dynatrace этого сервиса AWS не обогащаются свойством ARN.
