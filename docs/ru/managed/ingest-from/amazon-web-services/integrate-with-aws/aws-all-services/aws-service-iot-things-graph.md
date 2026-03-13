---
title: Мониторинг AWS IoT Things Graph
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-things-graph
scraped: 2026-03-01T21:23:17.710672
---

# Мониторинг AWS IoT Things Graph

# Мониторинг AWS IoT Things Graph

* Практическое руководство
* Чтение: 2 мин
* Опубликовано Jul 06, 2020

Dynatrace собирает метрики для множества предварительно выбранных пространств имён, включая AWS IoT Things Graph. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга данного сервиса вам необходимо

* ActiveGate версии 1.197+

  + Для развертываний Dynatrace SaaS вам потребуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развертываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (как в развертывании [SaaS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Интеграция метрик из Amazon CloudWatch.") так и [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) развертывании) вам потребуется [Environment ActiveGate](../../../../../ingest-from/dynatrace-activegate/installation.md "Узнайте, как настроить ActiveGate"), установленный на хосте Amazon EC2.
* Dynatrace версии 1.203+
* Обновленная [политика мониторинга AWS](../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#monitoring-policy "Интеграция метрик из Amazon CloudWatch.") для включения дополнительных сервисов AWS.  
  Для [обновления политики AWS IAMï»¿](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console) используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Ниже приведён пример политики JSON для одного отдельного сервиса.

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

* `"apigateway:GET"` for **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"`, and `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

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

После добавления сервиса в мониторинг предустановленная панель мониторинга, содержащая все рекомендуемые метрики, автоматически появится на странице **Панели мониторинга**. Для поиска конкретных панелей мониторинга фильтруйте по **Preset** и затем по **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

Для уже отслеживаемых сервисов может потребоваться повторное сохранение учётных данных, чтобы предустановленная панель мониторинга появилась на странице **Панели мониторинга**. Для повторного сохранения учётных данных перейдите в **Settings** > **Cloud and virtualization** > **AWS**, выберите нужный экземпляр AWS и нажмите **Save**.

Вы не можете вносить изменения в предустановленную панель мониторинга напрямую, но можете клонировать и редактировать её. Для клонирования панели мониторинга откройте меню обзора (**â¦**) и выберите **Clone**.

Для удаления панели мониторинга со страницы панелей мониторинга вы можете скрыть её. Для скрытия панели мониторинга откройте меню обзора (**â¦**) и выберите **Hide**.

Скрытие панели мониторинга не влияет на других пользователей.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

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

![IoT things](https://dt-cdn.net/images/dashboard-69-3840-1059a38762.png)

## Доступные метрики

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| FlowExecutionTime | The amount of time a flow execution step takes to complete | Milliseconds | Multi | Region, FlowTemplateId | Доступна |
| FlowExecutionTime |  | Milliseconds | Multi | Region, SystemTemplateId |  |
| FlowExecutionsAborted | The number of flow executions that are aborted | Count | Sum | Region, FlowTemplateId | Доступна |
| FlowExecutionsAborted |  | Count | Sum | Region, SystemTemplateId |  |
| FlowExecutionsFailed | The number of flow execution steps that failed | Count | Sum | Region, FlowTemplateId | Доступна |
| FlowExecutionsFailed |  | Count | Sum | Region, SystemTemplateId |  |
| FlowExecutionsStarted | The number of flow executions that started | Count | Sum | Region, FlowTemplateId | Доступна |
| FlowExecutionsStarted |  | Count | Sum | Region, SystemTemplateId |  |
| FlowExecutionsSucceeded | The number of flow execution steps that succeeded | Count | Sum | Region, FlowTemplateId | Доступна |
| FlowExecutionsSucceeded |  | Count | Sum | Region, SystemTemplateId |  |
| FlowStepExecutionTime | The amount of time a flow execution step takes to complete | Milliseconds | Multi | Region, FlowTemplateId, StepName |  |
| FlowStepExecutionTime |  | Milliseconds | Multi | Region, SystemTemplateId, StepName |  |
| FlowStepExecutionsFailed | The number of flow execution steps that failed | Count | Sum | Region, FlowTemplateId, StepName |  |
| FlowStepExecutionsFailed |  | Count | Sum | Region, SystemTemplateId, StepName |  |
| FlowStepExecutionsStarted | The number of flow execution steps that started | Count | Sum | Region, FlowTemplateId, StepName |  |
| FlowStepExecutionsStarted |  | Count | Sum | Region, SystemTemplateId, StepName |  |
| FlowStepExecutionsSucceeded | The number of flow execution steps that succeeded | Count | Sum | Region, FlowTemplateId, StepName |  |
| FlowStepExecutionsSucceeded |  | Count | Sum | Region, SystemTemplateId, StepName |  |
| FlowStepLambdaExecutionsFailed | The number of flow execution Lambda function steps that failed | Count | Sum | Region, LambdaArn |  |
| FlowStepLambdaExecutionsStarted | The number of flow execution Lambda function steps that started | Count | Sum | Region, LambdaArn |  |
| FlowStepLambdaExecutionsSucceeded | The number of flow execution Lambda function steps that succeeded | Count | Sum | Region, LambdaArn |  |