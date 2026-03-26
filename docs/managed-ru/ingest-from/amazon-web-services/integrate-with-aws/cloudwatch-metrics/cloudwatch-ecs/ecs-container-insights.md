---
title: Метрики Amazon ECS Container Insights CloudWatch
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs/ecs-container-insights
scraped: 2026-03-05T21:34:49.077417
---

Dynatrace получает метрики для множества предварительно выбранных пространств имён, включая Amazon ECS Container Insights. Вы можете просматривать метрики для каждого экземпляра сервиса, разделять метрики по нескольким измерениям и создавать пользовательские графики, которые можно закрепить на панелях мониторинга.

## Предварительные требования

Для включения мониторинга этого сервиса вам необходимо

* ActiveGate version 1.197+

  + Для развёртываний Dynatrace SaaS требуется Environment ActiveGate или Multi-environment ActiveGate.
  + Для развёртываний Dynatrace Managed можно использовать любой тип ActiveGate.

    Для доступа на основе ролей (будь то в [SaaS](../../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#role-based-access "Integrate metrics from Amazon CloudWatch.") or [Managed](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) развёртывании) требуется [Environment ActiveGate](../../../../../../ingest-from/dynatrace-activegate/installation.md "Learn how to configure ActiveGate") установленный на хосте Amazon EC2.
* Dynatrace version 1.203+
* Обновлённая [AWS monitoring policy](../../../../../../ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics.md#monitoring-policy "Integrate metrics from Amazon CloudWatch.") для включения дополнительных сервисов AWS.  
  To [update the AWS IAM policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), используйте приведённый ниже JSON, содержащий политику мониторинга (разрешения) для всех поддерживаемых сервисов.

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

Если вы не хотите добавлять разрешения для всех сервисов и хотите выбрать разрешения только для определённых сервисов, обратитесь к таблице ниже. Таблица содержит набор разрешений, необходимых для [All AWS cloud services](../../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-all-services.md "Monitor all AWS cloud services with Dynatrace and view available metrics.") а также для каждого поддерживаемого сервиса — список необязательных разрешений, специфичных для этого сервиса.

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

See the example of JSON policy for one single service below.

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

В этом примере из полного списка разрешений вам необходимо выбрать

* `"apigateway:GET"` для **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"`, and `"ec2:DescribeAvailabilityZones"` для **всех облачных сервисов AWS**.

* A [CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS-instancelevel.html)
* [Set up Container Insights on Amazon ECS for cluster](https://dt-url.net/lb03sq2).

### Эндпоинты AWS, которые должны быть доступны из ActiveGate, с соответствующими сервисами AWS

| Эндпоинт | Сервис |
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

Container Insights needs to be set up on a cluster to have metrics reported.

Cluster name configured for Container Insights agent has to be the same as your actual EKS cluster. For details, see the [AWS documentation](https://dt-url.net/ec230i0).

## Включение мониторинга

Чтобы узнать, как включить мониторинг сервиса, см. [Enable service monitoring](../../../../../../ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring.md "Enable AWS monitoring in Dynatrace.").

## Просмотр метрик сервиса

Вы можете просматривать метрики сервиса в вашем окружении Dynatrace на странице **обзора пользовательского устройства** или на странице **Панели мониторинга**.

### Просмотр метрик на странице обзора пользовательского устройства

Для доступа к странице обзора пользовательского устройства

1. Перейдите в ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Технологии и процессы (Classic)**.
2. Отфильтруйте по имени сервиса и выберите соответствующую группу пользовательских устройств.
3. После выбора группы пользовательских устройств вы окажетесь на странице **обзора группы пользовательских устройств**.
4. На странице **обзора группы пользовательских устройств** перечислены все экземпляры (пользовательские устройства), принадлежащие группе. Выберите экземпляр, чтобы перейти на страницу **обзора пользовательского устройства**.

### Просмотр метрик на панели мониторинга

After you add the service to monitoring, a preset dashboard containing all recommended metrics is automatically listed on your **Dashboards** page. To look for specific dashboards, filter by **Preset** and then by **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **AWS**, select the desired AWS instance, and then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.

To remove a dashboard from the dashboards page, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

Чтобы проверить доступность предустановленных панелей мониторинга для каждого сервиса AWS, см. список ниже.

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

![Container insights](https://dt-cdn.net/images/dashboard-67-1734-a01d1f311c.png)

## Доступные метрики

`ClusterName` is the main dimension.

| Название | Описание | Единица | Статистика | Измерения | Рекомендуемая |
| --- | --- | --- | --- | --- | --- |
| ContainerInstanceCount | The number of EC2 instances running the Amazon ECS agent that are registered with a cluster | Count | Sum | ClusterName |  |
| CpuReserved | The CPU units reserved by tasks in the resource that is specified by the dimension set that you're using | None | Multi | ClusterName |  |
| CpuReserved |  | None | Multi | ClusterName, TaskDefinitionFamily |  |
| CpuReserved |  | None | Multi | ClusterName, ServiceName |  |
| CpuReserved |  | None | Sum | ClusterName |  |
| CpuReserved |  | None | Sum | ClusterName, TaskDefinitionFamily |  |
| CpuReserved |  | None | Sum | ClusterName, ServiceName |  |
| CpuReserved |  | None | Count | ClusterName |  |
| CpuReserved |  | None | Count | ClusterName, TaskDefinitionFamily |  |
| CpuReserved |  | None | Count | ClusterName, ServiceName |  |
| CpuUtilized |  | None | Multi | ClusterName | Доступна |
| CpuUtilized | The CPU units used by tasks in the resource that is specified by the dimension set that you're using | None | Multi | ClusterName, TaskDefinitionFamily |  |
| CpuUtilized |  | None | Multi | ClusterName, ServiceName | Доступна |
| CpuUtilized |  | None | Sum | ClusterName |  |
| CpuUtilized |  | None | Sum | ClusterName, TaskDefinitionFamily |  |
| CpuUtilized |  | None | Sum | ClusterName, ServiceName |  |
| CpuUtilized |  | None | Count | ClusterName |  |
| CpuUtilized |  | None | Count | ClusterName, TaskDefinitionFamily |  |
| CpuUtilized |  | None | Count | ClusterName, ServiceName |  |
| DeploymentCount | The number of deployments in an Amazon ECS service | Count | Multi | ClusterName, ServiceName |  |
| DeploymentCount |  | Count | Sum | ClusterName, ServiceName |  |
| DesiredTaskCount | The desired number of tasks for an Amazon ECS service | Count | Multi | ClusterName, ServiceName |  |
| DesiredTaskCount |  | Count | Sum | ClusterName, ServiceName |  |
| MemoryReserved | Память, зарезервированная задачами в ресурсе, указанном в используемом наборе измерений | Megabytes | Multi | ClusterName |  |
| MemoryReserved |  | Megabytes | Multi | ClusterName, TaskDefinitionFamily |  |
| MemoryReserved |  | Megabytes | Multi | ClusterName, ServiceName |  |
| MemoryReserved |  | Megabytes | Sum | ClusterName |  |
| MemoryReserved |  | Megabytes | Sum | ClusterName, TaskDefinitionFamily |  |
| MemoryReserved |  | Megabytes | Sum | ClusterName, ServiceName |  |
| MemoryReserved |  | Megabytes | Count | ClusterName |  |
| MemoryReserved |  | Megabytes | Count | ClusterName, TaskDefinitionFamily |  |
| MemoryReserved |  | Megabytes | Count | ClusterName, ServiceName |  |
| MemoryUtilized | Память, используемая задачами в ресурсе, указанном в используемом наборе измерений | Megabytes | Multi | ClusterName | Доступна |
| MemoryUtilized |  | Megabytes | Multi | ClusterName, TaskDefinitionFamily |  |
| MemoryUtilized |  | Megabytes | Multi | ClusterName, ServiceName | Доступна |
| MemoryUtilized |  | Megabytes | Sum | ClusterName |  |
| MemoryUtilized |  | Megabytes | Sum | ClusterName, TaskDefinitionFamily |  |
| MemoryUtilized |  | Megabytes | Sum | ClusterName, ServiceName |  |
| MemoryUtilized |  | Megabytes | Count | ClusterName |  |
| MemoryUtilized |  | Megabytes | Count | ClusterName, TaskDefinitionFamily |  |
| MemoryUtilized |  | Megabytes | Count | ClusterName, ServiceName |  |
| NetworkRxBytes | Количество байт, полученных ресурсом, указанным в используемых измерениях | Bytes/Second | Multi | ClusterName | Доступна |
| NetworkRxBytes |  | Bytes/Second | Multi | ClusterName, ServiceName | Доступна |
| NetworkRxBytes |  | Bytes/Second | Multi | ClusterName, TaskDefinitionFamily |  |
| NetworkTxBytes | Количество байт, переданных ресурсом, указанным в используемых измерениях | Bytes/Second | Multi | ClusterName, ServiceName | Доступна |
| NetworkTxBytes |  | Bytes/Second | Multi | ClusterName, TaskDefinitionFamily |  |
| NetworkTxBytes |  | Bytes/Second | Multi | ClusterName | Доступна |
| PendingTaskCount | The number of tasks currently in `Pending` state | Count | Multi | ClusterName, ServiceName |  |
| PendingTaskCount |  | Count | Sum | ClusterName, ServiceName |  |
| RunningTaskCount | The number of tasks currently in `Running` state | Count | Multi | ClusterName, ServiceName | Доступна |
| ServiceCount | The number of services in the cluster | Count | Sum | ClusterName |  |
| StorageReadBytes | The number of bytes read from storage in the resource that is specified by the dimensions that you're using | Bytes/Second | Multi | ClusterName | Доступна |
| StorageReadBytes |  | Bytes/Second | Multi | ClusterName, TaskDefinitionFamily |  |
| StorageReadBytes |  | Bytes/Second | Multi | ClusterName, ServiceName | Доступна |
| StorageWriteBytes | The number of bytes written to storage in the resource that is specified by the dimensions that you're using | Bytes/Second | Multi | ClusterName | Доступна |
| StorageWriteBytes |  | Bytes/Second | Multi | ClusterName, TaskDefinitionFamily |  |
| StorageWriteBytes |  | Bytes/Second | Multi | ClusterName, ServiceName | Доступна |
| TaskCount | The number of tasks running in the cluster | Count | Multi | ClusterName | Доступна |
| TaskSetCount | The number of task sets in the service | Count | Multi | ClusterName, ServiceName |  |
| TaskSetCount |  | Count | Sum | ClusterName, ServiceName |  |
| instance\_cpu\_limit | The maximum number of CPU units that can be assigned to a single EC2 instance in the cluster | None | Multi | ClusterName |  |
| instance\_cpu\_limit |  | None | Sum | ClusterName |  |
| instance\_cpu\_limit |  | None | Count | ClusterName |  |
| instance\_cpu\_reserved\_capacity | The percentage of CPU currently being reserved on a single EC2 instance in the cluster | Percent | Multi | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_cpu\_reserved\_capacity |  | Percent | Multi | ClusterName |  |
| instance\_cpu\_usage\_total | The number of CPU units being used on a single EC2 instance in the cluster | None | Multi | ClusterName |  |
| instance\_cpu\_usage\_total |  | None | Sum | ClusterName |  |
| instance\_cpu\_usage\_total |  | None | Count | ClusterName |  |
| instance\_cpu\_utilization | The total percentage of CPU units being used on a single EC2 instance in the cluster | Percent | Multi | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_cpu\_utilization |  | Percent | Multi | ClusterName | Доступна |
| instance\_filesystem\_utilization | The total percentage of file system capacity being used on a single EC2 instance in the cluster | Percent | Multi | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_filesystem\_utilization |  | Percent | Multi | ClusterName | Доступна |
| instance\_memory\_limit | The maximum amount of memory, in bytes, that can be assigned to a single EC2 instance in the cluster | Bytes | Multi | ClusterName |  |
| instance\_memory\_limit |  | Bytes | Sum | ClusterName |  |
| instance\_memory\_limit |  | Bytes | Count | ClusterName |  |
| instance\_memory\_reserved\_capacity | The percentage of memory currently being reserved on a single EC2 instance in the cluster | Percent | Multi | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_memory\_reserved\_capacity |  | Percent | Multi | ClusterName |  |
| instance\_memory\_utilization | The total percentage of memory being used on a single EC2 instance in the cluster | Percent | Multi | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_memory\_utilization |  | Percent | Multi | ClusterName | Доступна |
| instance\_memory\_working\_set | The amount of memory, in bytes, being used on a single EC2 instance in the cluster | Bytes | Multi | ClusterName |  |
| instance\_memory\_working\_set |  | Bytes | Sum | ClusterName |  |
| instance\_memory\_working\_set |  | Bytes | Count | ClusterName |  |
| instance\_network\_total\_bytes | The total number of bytes per second transmitted and received over the network on a single EC2 instance in the cluster | Bytes/Second | Multi | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_network\_total\_bytes |  | Bytes/Second | Multi | ClusterName | Доступна |
| instance\_number\_of\_running\_tasks | The number of running tasks on a single EC2 instance in the cluster | Count | Sum | ClusterName, ContainerInstanceId, InstanceId |  |
| instance\_number\_of\_running\_tasks |  | Count | Multi | ClusterName | Доступна |
| instance\_number\_of\_running\_tasks |  | Count | Sum | ClusterName |  |