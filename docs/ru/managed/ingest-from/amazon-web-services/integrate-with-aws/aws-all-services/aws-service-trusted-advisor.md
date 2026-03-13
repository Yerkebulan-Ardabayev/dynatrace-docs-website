---
title: AWS Trusted Advisor monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-trusted-advisor
scraped: 2026-03-06T21:25:55.282868
---

# Мониторинг AWS Trusted Advisor

# Мониторинг AWS Trusted Advisor

* Classic
* Руководство
* Чтение: 1 мин
* Обновлено 20 июня 2022 г.

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая AWS Trusted Advisor. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские диаграммы, которые можно закрепить на ваших дашбордах.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимы

* ActiveGate версии 1.197+

  + Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развёртываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (будь то развёртывание [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Integrate metrics from Amazon CloudWatch.") или [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment)) требуется [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Learn how to configure ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.203+
* Обновлённая [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#monitoring-policy "Integrate metrics from Amazon CloudWatch.") для включения дополнительных сервисов AWS.
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

Если вы не хотите добавлять разрешения для всех сервисов и хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [всех облачных сервисов AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Monitor all AWS cloud services with Dynatrace and view available metrics."), и для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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
| Все мониторируемые сервисы Amazon (обязательные) | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
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

Пример JSON-политики для одного сервиса приведён ниже.

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

Для AWS Trusted Advisor на странице обзора группы пользовательских устройств нет экземпляров (пользовательских устройств). Метрики сервиса находятся в разделе **Further details** на странице обзора группы пользовательских устройств.

Метрики CloudWatch для AWS Trusted Advisor доступны **только** для планов поддержки Business и Enterprise.

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Включение мониторинга сервиса](../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Enable AWS monitoring in Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашей среде Dynatrace на **странице обзора пользовательского устройства** или на странице **Dashboards**.

### Просмотр метрик на странице обзора пользовательского устройства

Чтобы перейти на страницу обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на **странице обзора группы пользовательских устройств**.
4. На **странице обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр для просмотра **страницы обзора пользовательского устройства**.

### Просмотр метрик на дашборде

После добавления сервиса в мониторинг на странице **Dashboards** автоматически появляется предустановленный дашборд со всеми рекомендуемыми метриками. Для поиска конкретных дашбордов отфильтруйте по **Preset**, а затем по **Name**.

![Предустановки AWS](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для существующих мониторируемых сервисов может потребоваться повторно сохранить учётные данные, чтобы предустановленный дашборд появился на странице **Dashboards**. Чтобы повторно сохранить учётные данные, перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленный дашборд напрямую, но можете клонировать и редактировать его. Чтобы клонировать дашборд, откройте меню обзора (**...**) и выберите **Clone**.

Чтобы удалить дашборд со страницы дашбордов, вы можете его скрыть. Чтобы скрыть дашборд, откройте меню обзора (**...**) и выберите **Hide**.

Скрытие дашборда не влияет на других пользователей.

![Клонирование и скрытие AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

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
| Все мониторируемые сервисы Amazon | Недоступен |
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

![Trusted](https://dt-cdn.net/images/2021-03-12-10-16-15-1493-7377e86387.png)

## Доступные метрики

| Название | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- |
| GreenChecks | Count | Sum | Region, Category |  |
| RedChecks | Count | Sum | Region, Category | Доступен |
| RedResources | Count | Sum | Region, CheckName | Доступен |
| ServiceLimitUsage | Percent | Multi | Region, ServiceLimit, ServiceName | Доступен |
| YellowChecks | Count | Sum | Region, Category | Доступен |
| YellowResources | Count | Sum | Region, CheckName | Доступен |