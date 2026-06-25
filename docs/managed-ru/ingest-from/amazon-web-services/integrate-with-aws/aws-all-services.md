---
title: Все облачные сервисы AWS
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services
scraped: 2026-05-12T11:07:03.014823
---

# Все облачные сервисы AWS

# Все облачные сервисы AWS

* Обзор
* Чтение: 12 мин
* Опубликовано 12 февраля 2024 г.

ActiveGate версии 1.245+

С интеграцией мониторинга AWS classic-сервисы (ранее «built-in») мониторятся из коробки. Также можно мониторить другие сервисы AWS, влияющие на производительность приложений, размещённых в AWS.

Можно получать метрики Amazon CloudWatch для множества предопределённых сервисов. Можно просматривать графики по каждому экземпляру сервиса с набором измерений, а также создавать собственные графики и закреплять их на дашбордах. Чтобы снизить затраты на CloudWatch и троттлинг, выберите, какие дополнительные сервисы мониторить. Кроме того, для non-classic сервисов можно выбрать, какие метрики требуется мониторить.

## Облачные сервисы AWS, мониторинг которых ведётся по умолчанию

Благодаря [интеграции мониторинга AWS](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Приём метрик Amazon CloudWatch.") некоторые сервисы мониторятся из коробки. Такие сервисы помечены как classic.

[Amazon Dynamo Database (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamo-db-builtin) [Amazon EC2 (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-builtin) [Amazon EC2 Auto Scaling (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling-builltin) [AWS Lambda (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin) [AWS Application and Network Load Balancer (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-application-and-network-load-balancer-builtin) [Elastic Load Balancer (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-load-balancer-builtin) [Amazon S3 (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3-builtin) [Amazon RDS (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-builtin) [Amazon EBS (classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-block-store-ebs-builtin) 

Информацию о различиях между classic-сервисами и другими сервисами см. в разделе [Миграция с classic-сервисов AWS (ранее «built-in») на облачные сервисы](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Миграция classic-сервисов AWS на их новые версии.").

## Прочие облачные сервисы AWS

Помимо облачных сервисов, мониторинг которых ведётся по умолчанию, можно мониторить другие сервисы AWS, влияющие на производительность приложений, размещённых в AWS.

[Amazon DynamoDB](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb-new) [Amazon EBS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-ebs-new) [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lambda-new) [Amazon RDS](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new) [AWS Certificate Manager Private Certificate Authority (ACM PCA)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-acm-pca) [Amazon API Gateway](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-gateway) [Amazon AppStream 2.0](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-appstream-2) [AWS AppSync](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-appsync) [AWS App Runner](/managed/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [Amazon Athena](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-athena) [Amazon Aurora](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-aurora) [AWS Billing](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-billing) [AWS Chatbot](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-chatbot) [Amazon CloudFront](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudfront) [AWS CloudHSM (V2)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudhsm-v2) [Amazon CloudSearch](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudsearch) [Amazon CloudWatch Logs](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudwatch-logs) [AWS API Usage](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-usage) [AWS CodeBuild](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-codebuild) [Amazon Cognito](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cognito) [Amazon Connect](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-connect) [AWS Database Migration Service (AWS DMS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-database-migration-service-dms) [AWS DataSync](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-datasync) [AWS Direct Connect](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-direct-connect) [Amazon DocumentDB](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-documentdb) [Amazon DynamoDB Accelerator (DAX)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb) [Amazon EC2 API](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-api) [Amazon EC2 Auto Scaling](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling) [Amazon EC2 Spot Fleet](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-spot-fleet) [Amazon ECS Container Insights](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs/ecs-container-insights) [Amazon ElastiCache](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticache) [AWS Elastic Beanstalk](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-elastic-beanstalk) [Amazon Elastic Container Service (ECS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs) [Amazon Elastic File System (EFS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-file-system-efs) [Amazon Elastic Inference](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-inference) [Amazon Elastic Kubernetes Service (EKS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [Amazon Elastic MapReduce (EMR)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-mapreduce-emr) [Amazon Elasticsearch Service (ES)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticsearch-service-es) [Amazon Elastic Transcoder](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-transcoder) [AWS Elemental MediaConnect](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconnect) [AWS Elemental MediaConvert](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconvert) [AWS Elemental MediaPackage](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediapackage) [AWS Elemental MediaTailor](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediatailor) [Amazon EventBridge](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-eventbridge) [Amazon FSx](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-fsx) [Amazon GameLift](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-gamelift) [AWS Glue](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-glue) [Amazon Inspector](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-inspector) [AWS IoT](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot) [AWS IoT Analytics](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-analytics) [AWS IoT Things Graph](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-things-graph) [Amazon Keyspaces (Cassandra)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-keyspaces-cassandra) [Amazon Kinesis](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-kinesis) [Amazon Lex](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lex) [Amazon MSK (Kafka)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-msk-kafka) [Amazon MQ](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-mq) [Amazon Neptune](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-neptune) [AWS OpsWorks](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-opsworks) [Amazon Polly](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-polly) [Amazon QLDB](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-quantum-ledger-database-qldb) [Amazon Redshift](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-redshift) [Amazon Rekognition](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-rekognition) [AWS RoboMaker](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-robomaker) [Amazon Route 53](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-route-53) [Amazon Route 53 Resolver](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-route-53-resolver) [Amazon SageMaker](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-sagemaker) [AWS Service Catalog](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-service-catalog) [Amazon Simple Email Service (SES)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-email-service-ses) [Amazon Simple Notification Service (SNS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-notification-service-sns) [Amazon Simple Queue Service (SQS)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-queue-service-sqs) [Amazon Simple Storage Service (S3)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3) [Amazon Simple Workflow Service (SWF)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-workflow-service-swf) [AWS Step Functions](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-step-functions) [AWS Storage Gateway](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-storage-gateway) [AWS Systems Manager Run Command](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-systems-manager-run-command) [Amazon Textract](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-textract) [AWS Transfer Family](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-transfer-family) [AWS Transit Gateway](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-transit-gateway) [Amazon Translate](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-translate) [AWS Trusted Advisor](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-trusted-advisor) [Amazon VPC NAT Gateways](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-vpc) [AWS Site-to-Site VPN](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-site-to-site-vpn) [AWS WAF Classic](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-waf-classic) [AWS WAF](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-wafv2) [Amazon WorkMail](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-workmail) [Amazon WorkSpaces](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-workspaces) 

## Облачные сервисы и соответствующие им типы сущностей Dynatrace

Не все облачные сервисы получают сущности Dynatrace и поддерживают импорт тегов из облака. Разверните таблицу ниже, чтобы посмотреть облачные сервисы и соответствующие им типы сущностей Dynatrace, а также проверить, импортируются ли для них теги от облачного провайдера.

### Список сервисов AWS с сущностями и тегами

Для каждого non-built-in сервиса измерение `CUSTOM_DEVICE` генерируется на основе основного измерения

| Сервис | Облачный экземпляр | Мониторинг и фильтрация по тегам | Тип сущности Dynatrace |
| --- | --- | --- | --- |
| Amazon EC2 Auto Scaling (built-in) | AutoScalingGroupName | Применимо | AUTO\_SCALING\_GROUP |
| AWS Lambda (built-in) | FunctionName | Применимо | AWS\_LAMBDA\_FUNCTION |
| Amazon Application and Network Load Balancer (built-in) | LoadBalancer | Применимо | AWS\_APPLICATION\_LOAD\_BALANCER |
| Amazon Application and Network Load Balancer (built-in) | LoadBalancer | Применимо | AWS\_NETWORK\_LOAD\_BALANCER |
| Amazon EBS (built-in) | VolumeId | Применимо | EBS\_VOLUME |
| Amazon EC2 (built-in) | InstanceId | Применимо | EC2\_INSTANCE |
| Amazon Elastic Load Balancer (ELB) (built-in) | LoadBalancerName | Применимо | ELASTIC\_LOAD\_BALANCER |
| Amazon RDS (built-in) | DBInstanceIdentifier | Применимо | RELATIONAL\_DATABASE\_SERVICE |
| AWS Certificate Manager Private Certificate Authority | PrivateCAArn | Применимо | cloud:aws:acmprivateca |
| Amazon API Gateway | ApiName | Применимо | cloud:aws:api\_gateway |
| AWS App Runner | ServiceName | Применимо | cloud:aws:app\_runner |
| Amazon AppStream | Fleet | Применимо | cloud:aws:appstream |
| AWS AppSync | GraphQLAPIId | Применимо | cloud:aws:appsync |
| Amazon Athena | WorkGroup | Применимо | cloud:aws:athena |
| Amazon Aurora | DBClusterIdentifier | Применимо | cloud:aws:aurora |
| Amazon EC2 Auto Scaling | AutoScalingGroupName | - | cloud:aws:autoscaling |
| Amazon CloudFront | DistributionId | Применимо | cloud:aws:cloud\_front |
| AWS CloudHSM | ClusterId | Применимо | cloud:aws:cloudhsm |
| Amazon CloudSearch | DomainName | - | cloud:aws:cloudsearch |
| AWS CodeBuild | ProjectName | Применимо | cloud:aws:codebuild |
| AWS DataSync | TaskId | Применимо | cloud:aws:datasync |
| Amazon DynamoDB Accelerator (DAX) | ClusterId | Применимо | cloud:aws:dax |
| AWS Database Migration Service (AWS DMS) | ReplicationInstanceIdentifier | Применимо | cloud:aws:dms |
| Amazon DocumentDB | DBClusterIdentifier | Применимо | cloud:aws:documentdb |
| AWS Direct Connect | ConnectionId | Применимо | cloud:aws:dxcon |
| Amazon DynamoDB | TableName | Применимо | cloud:aws:dynamodb |
| Amazon EBS | VolumeId | Применимо | cloud:aws:ebs |
| Amazon EC2 Spot Fleet | FleetRequestId | - | cloud:aws:ec2\_spot |
| Amazon Elastic Container Service (ECS) | ClusterName | Применимо | cloud:aws:ecs |
| Amazon ECS Container Insights | ClusterName | Применимо | cloud:aws:ecs:cluster |
| Amazon Elastic File System (EFS) | FileSystemId | Применимо | cloud:aws:efs |
| Amazon Elastic Kubernetes Service (EKS) | ClusterName | Применимо | cloud:aws:eks:cluster |
| Amazon ElastiCache (EC) | CacheClusterId | Применимо | cloud:aws:elasticache |
| AWS Elastic Beanstalk | EnvironmentName | Применимо | cloud:aws:elasticbeanstalk |
| Amazon Elastic Transcoder | PipelineId | - | cloud:aws:elastictranscoder |
| Amazon Elasticsearch Service (ES) | DomainName | Применимо | cloud:aws:es |
| Amazon EventBridge | EventBusName | Применимо | cloud:aws:events |
| Amazon FSx | FileSystemId | Применимо | cloud:aws:fsx |
| Amazon GameLift | FleetId | - | cloud:aws:gamelift |
| AWS Glue | JobName | Применимо | cloud:aws:glue |
| Amazon Inspector | AssessmentTemplateArn | Применимо | cloud:aws:inspector |
| Amazon Managed Streaming for Kafka | Cluster Name | Применимо | cloud:aws:kafka |
| AWS Lambda | FunctionName | Применимо | cloud:aws:lambda |
| Amazon Lex | BotName | Применимо | cloud:aws:lex |
| Amazon CloudWatch Logs | LogGroupName | Применимо | cloud:aws:logs |
| AWS Elemental MediaTailor | ConfigurationName | Применимо | cloud:aws:media\_tailor |
| AWS Elemental MediaConnect | FlowARN | - | cloud:aws:mediaconnect |
| AWS Elemental MediaPackage Live | Channel | Применимо | cloud:aws:mediapackagelive |
| AWS Elemental MediaPackage Video on Demand | PackagingConfiguration | Применимо | cloud:aws:mediapackagevod |
| Amazon VPC NAT Gateways | NatGatewayId | Применимо | cloud:aws:nat\_gateway |
| Amazon Neptune | DBClusterIdentifier | Применимо | cloud:aws:neptune |
| AWS OpsWorks | StackId | Применимо | cloud:aws:opsworks |
| Amazon QLDB | LedgerName | Применимо | cloud:aws:qldb |
| Amazon RDS | DBInstanceIdentifier | Применимо | cloud:aws:rds |
| Amazon Redshift | ClusterIdentifier | Применимо | cloud:aws:redshift |
| AWS RoboMaker | SimulationJobId | Применимо | cloud:aws:robomaker |
| Amazon Route 53 | HostedZoneId | Применимо | cloud:aws:route53 |
| Amazon Route 53 Resolver | EndpointId | Применимо | cloud:aws:route53resolver |
| Amazon SageMaker Endpoints | EndpointName | Применимо | cloud:aws:sage\_maker:endpoint |
| Amazon SageMaker Endpoint Instances | EndpointName | Применимо | cloud:aws:sage\_maker:endpoint\_instance |
| Amazon Simple Notification Service (SNS) | TopicName | Применимо | cloud:aws:sns |
| Amazon Simple Queue Service (SQS) | QueueName | Применимо | cloud:aws:sqs |
| AWS Storage Gateway | GatewayName | Применимо | cloud:aws:storagegateway |
| Amazon SWF | Domain | - | cloud:aws:swf |
| AWS Transfer Family | ServerId | Применимо | cloud:aws:transfer |
| AWS Transit Gateway | TransitGateway | Применимо | cloud:aws:transitgateway |
| AWS Site-to-Site VPN | VpnId | Применимо | cloud:aws:vpn |
| Amazon WorkMail | OrganizationId | Применимо | cloud:aws:workmail |
| Amazon WorkSpaces | WorkspaceId | Применимо | cloud:aws:workspaces |

## Configuration API

Чтобы получить список всех поддерживаемых сервисов AWS на вашем кластере в текущей версии, используйте [API поддерживаемых сервисов AWS](/managed/dynatrace-api/configuration-api/aws-supported-services "Получение списка поддерживаемых сервисов AWS через Dynatrace API.").

## Потребление мониторинга

С 2021 года все облачные сервисы потребляют DDU. Объём потребления DDU на экземпляр сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0.001 DDU).