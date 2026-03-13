---
title: All AWS cloud services
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services
scraped: 2026-03-06T21:18:24.141243
---

# Все облачные сервисы AWS

# Все облачные сервисы AWS

* Classic
* Обзор
* Время чтения: 12 мин
* Обновлено 12 фев. 2024

ActiveGate версии 1.245+

Благодаря интеграции мониторинга AWS классические (ранее называвшиеся «встроенными») сервисы отслеживаются автоматически. Вы также можете отслеживать другие сервисы AWS, которые влияют на производительность ваших приложений, размещённых в AWS.

Вы можете получать метрики Amazon CloudWatch для нескольких предопределённых сервисов. Вы можете просматривать графики для каждого экземпляра сервиса с набором измерений и создавать пользовательские графики, которые можно закреплять на дашбордах. Вы можете снизить затраты на CloudWatch и ограничение запросов, выбирая, какие дополнительные сервисы отслеживать. Кроме того, для неклассических сервисов вы можете выбирать, какие метрики отслеживать.

## Облачные сервисы AWS, отслеживаемые по умолчанию

В результате [интеграции мониторинга AWS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Интеграция метрик из Amazon CloudWatch.") некоторые сервисы отслеживаются автоматически. Такие сервисы отмечены как классические.

[Amazon Dynamo Database (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamo-db-builtin) [Amazon EC2 (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-builtin) [Amazon EC2 Auto Scaling (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling-builltin) [AWS Lambda (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin) [AWS Application and Network Load Balancer (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-application-and-network-load-balancer-builtin) [Elastic Load Balancer (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-load-balancer-builtin) [Amazon S3 (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3-builtin) [Amazon RDS (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-builtin) [Amazon EBS (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-block-store-ebs-builtin)

Информацию о различиях между классическими сервисами и другими сервисами см. в разделе [Миграция с классических (ранее «встроенных») сервисов AWS на облачные сервисы](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Миграция классических сервисов AWS на новые версии.").

## Другие облачные сервисы AWS

В дополнение к облачным сервисам, отслеживаемым по умолчанию, вы можете отслеживать другие сервисы AWS, влияющие на производительность ваших приложений, размещённых в AWS.

[Amazon DynamoDB](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb-new) [Amazon EBS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-ebs-new) [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lambda-new) [Amazon RDS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new) [AWS Certificate Manager Private Certificate Authority (ACM PCA)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-acm-pca) [Amazon API Gateway](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-gateway) [Amazon AppStream 2.0](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-appstream-2) [AWS AppSync](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-appsync) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [Amazon Athena](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-athena) [Amazon Aurora](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-aurora) [AWS Billing](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-billing) [AWS Chatbot](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-chatbot) [Amazon CloudFront](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudfront) [AWS CloudHSM (V2)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudhsm-v2) [Amazon CloudSearch](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudsearch) [Amazon CloudWatch Logs](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudwatch-logs) [AWS API Usage](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-usage) [AWS CodeBuild](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-codebuild) [Amazon Cognito](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cognito) [Amazon Connect](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-connect) [AWS Database Migration Service (AWS DMS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-database-migration-service-dms) [AWS DataSync](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-datasync) [AWS Direct Connect](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-direct-connect) [Amazon DocumentDB](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-documentdb) [Amazon DynamoDB Accelerator (DAX)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb) [Amazon EC2 API](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-api) [Amazon EC2 Auto Scaling](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling) [Amazon EC2 Spot Fleet](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-spot-fleet) [Amazon ECS Container Insights](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs/ecs-container-insights) [Amazon ElastiCache](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticache) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-elastic-beanstalk) [Amazon Elastic Container Service (ECS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs) [Amazon Elastic File System (EFS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-file-system-efs) [Amazon Elastic Inference](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-inference) [Amazon Elastic Kubernetes Service (EKS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [Amazon Elastic MapReduce (EMR)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-mapreduce-emr) [Amazon Elasticsearch Service (ES)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticsearch-service-es) [Amazon Elastic Transcoder](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-transcoder) [AWS Elemental MediaConnect](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconnect) [AWS Elemental MediaConvert](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconvert) [AWS Elemental MediaPackage](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediapackage) [AWS Elemental MediaTailor](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediatailor) [Amazon EventBridge](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-eventbridge) [Amazon FSx](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-fsx) [Amazon GameLift](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-gamelift) [AWS Glue](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-glue) [Amazon Inspector](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-inspector) [AWS IoT](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot) [AWS IoT Analytics](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-analytics) [AWS IoT Things Graph](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-things-graph) [Amazon Keyspaces (Cassandra)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-keyspaces-cassandra) [Amazon Kinesis](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-kinesis) [Amazon Lex](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lex) [Amazon MSK (Kafka)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-msk-kafka) [Amazon MQ](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-mq) [Amazon Neptune](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-neptune) [AWS OpsWorks](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-opsworks) [Amazon Polly](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-polly) [Amazon QLDB](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-quantum-ledger-database-qldb) [Amazon Redshift](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-redshift) [Amazon Rekognition](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-rekognition) [AWS RoboMaker](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-robomaker) [Amazon Route 53](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-route-53) [Amazon Route 53 Resolver](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-route-53-resolver) [Amazon SageMaker](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-sagemaker) [AWS Service Catalog](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-service-catalog) [Amazon Simple Email Service (SES)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-email-service-ses) [Amazon Simple Notification Service (SNS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-notification-service-sns) [Amazon Simple Queue Service (SQS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-queue-service-sqs) [Amazon Simple Storage Service (S3)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3) [Amazon Simple Workflow Service (SWF)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-workflow-service-swf) [AWS Step Functions](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-step-functions) [AWS Storage Gateway](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-storage-gateway) [AWS Systems Manager Run Command](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-systems-manager-run-command) [Amazon Textract](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-textract) [AWS Transfer Family](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-transfer-family) [AWS Transit Gateway](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-transit-gateway) [Amazon Translate](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-translate) [AWS Trusted Advisor](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-trusted-advisor) [Amazon VPC NAT Gateways](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-vpc) [AWS Site-to-Site VPN](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-site-to-site-vpn) [AWS WAF Classic](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-waf-classic) [AWS WAF](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-wafv2) [Amazon WorkMail](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-workmail) [Amazon WorkSpaces](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-workspaces)

## Облачные сервисы и соответствующие им типы сущностей Dynatrace

Не для всех облачных сервисов создаются сущности Dynatrace и не для всех можно импортировать теги из облака. Разверните таблицу ниже, чтобы увидеть облачные сервисы с соответствующими типами сущностей Dynatrace и проверить, импортируются ли для них теги от облачного провайдера.

### Список сервисов AWS с сущностями и тегами

Для каждого не встроенного сервиса измерение `CUSTOM_DEVICE` генерируется на основе основного измерения.

| Сервис | Облачный экземпляр | Мониторинг и фильтрация тегов | Тип сущности Dynatrace |
| --- | --- | --- | --- |
| Amazon EC2 Auto Scaling (built-in) | AutoScalingGroupName | Да | AUTO\_SCALING\_GROUP |
| AWS Lambda (built-in) | FunctionName | Да | AWS\_LAMBDA\_FUNCTION |
| Amazon Application and Network Load Balancer (built-in) | LoadBalancer | Да | AWS\_APPLICATION\_LOAD\_BALANCER |
| Amazon Application and Network Load Balancer (built-in) | LoadBalancer | Да | AWS\_NETWORK\_LOAD\_BALANCER |
| Amazon EBS (built-in) | VolumeId | Да | EBS\_VOLUME |
| Amazon EC2 (built-in) | InstanceId | Да | EC2\_INSTANCE |
| Amazon Elastic Load Balancer (ELB) (built-in) | LoadBalancerName | Да | ELASTIC\_LOAD\_BALANCER |
| Amazon RDS (built-in) | DBInstanceIdentifier | Да | RELATIONAL\_DATABASE\_SERVICE |
| AWS Certificate Manager Private Certificate Authority | PrivateCAArn | Да | cloud:aws:acmprivateca |
| Amazon API Gateway | ApiName | Да | cloud:aws:api\_gateway |
| AWS App Runner | ServiceName | Да | cloud:aws:app\_runner |
| Amazon AppStream | Fleet | Да | cloud:aws:appstream |
| AWS AppSync | GraphQLAPIId | Да | cloud:aws:appsync |
| Amazon Athena | WorkGroup | Да | cloud:aws:athena |
| Amazon Aurora | DBClusterIdentifier | Да | cloud:aws:aurora |
| Amazon EC2 Auto Scaling | AutoScalingGroupName | - | cloud:aws:autoscaling |
| Amazon CloudFront | DistributionId | Да | cloud:aws:cloud\_front |
| AWS CloudHSM | ClusterId | Да | cloud:aws:cloudhsm |
| Amazon CloudSearch | DomainName | - | cloud:aws:cloudsearch |
| AWS CodeBuild | ProjectName | Да | cloud:aws:codebuild |
| AWS DataSync | TaskId | Да | cloud:aws:datasync |
| Amazon DynamoDB Accelerator (DAX) | ClusterId | Да | cloud:aws:dax |
| AWS Database Migration Service (AWS DMS) | ReplicationInstanceIdentifier | Да | cloud:aws:dms |
| Amazon DocumentDB | DBClusterIdentifier | Да | cloud:aws:documentdb |
| AWS Direct Connect | ConnectionId | Да | cloud:aws:dxcon |
| Amazon DynamoDB | TableName | Да | cloud:aws:dynamodb |
| Amazon EBS | VolumeId | Да | cloud:aws:ebs |
| Amazon EC2 Spot Fleet | FleetRequestId | - | cloud:aws:ec2\_spot |
| Amazon Elastic Container Service (ECS) | ClusterName | Да | cloud:aws:ecs |
| Amazon ECS Container Insights | ClusterName | Да | cloud:aws:ecs:cluster |
| Amazon Elastic File System (EFS) | FileSystemId | Да | cloud:aws:efs |
| Amazon Elastic Kubernetes Service (EKS) | ClusterName | Да | cloud:aws:eks:cluster |
| Amazon ElastiCache (EC) | CacheClusterId | Да | cloud:aws:elasticache |
| AWS Elastic Beanstalk | EnvironmentName | Да | cloud:aws:elasticbeanstalk |
| Amazon Elastic Transcoder | PipelineId | - | cloud:aws:elastictranscoder |
| Amazon Elasticsearch Service (ES) | DomainName | Да | cloud:aws:es |
| Amazon EventBridge | EventBusName | Да | cloud:aws:events |
| Amazon FSx | FileSystemId | Да | cloud:aws:fsx |
| Amazon GameLift | FleetId | - | cloud:aws:gamelift |
| AWS Glue | JobName | Да | cloud:aws:glue |
| Amazon Inspector | AssessmentTemplateArn | Да | cloud:aws:inspector |
| Amazon Managed Streaming for Kafka | Cluster Name | Да | cloud:aws:kafka |
| AWS Lambda | FunctionName | Да | cloud:aws:lambda |
| Amazon Lex | BotName | Да | cloud:aws:lex |
| Amazon CloudWatch Logs | LogGroupName | Да | cloud:aws:logs |
| AWS Elemental MediaTailor | ConfigurationName | Да | cloud:aws:media\_tailor |
| AWS Elemental MediaConnect | FlowARN | - | cloud:aws:mediaconnect |
| AWS Elemental MediaPackage Live | Channel | Да | cloud:aws:mediapackagelive |
| AWS Elemental MediaPackage Video on Demand | PackagingConfiguration | Да | cloud:aws:mediapackagevod |
| Amazon VPC NAT Gateways | NatGatewayId | Да | cloud:aws:nat\_gateway |
| Amazon Neptune | DBClusterIdentifier | Да | cloud:aws:neptune |
| AWS OpsWorks | StackId | Да | cloud:aws:opsworks |
| Amazon QLDB | LedgerName | Да | cloud:aws:qldb |
| Amazon RDS | DBInstanceIdentifier | Да | cloud:aws:rds |
| Amazon Redshift | ClusterIdentifier | Да | cloud:aws:redshift |
| AWS RoboMaker | SimulationJobId | Да | cloud:aws:robomaker |
| Amazon Route 53 | HostedZoneId | Да | cloud:aws:route53 |
| Amazon Route 53 Resolver | EndpointId | Да | cloud:aws:route53resolver |
| Amazon SageMaker Endpoints | EndpointName | Да | cloud:aws:sage\_maker:endpoint |
| Amazon SageMaker Endpoint Instances | EndpointName | Да | cloud:aws:sage\_maker:endpoint\_instance |
| Amazon Simple Notification Service (SNS) | TopicName | Да | cloud:aws:sns |
| Amazon Simple Queue Service (SQS) | QueueName | Да | cloud:aws:sqs |
| AWS Storage Gateway | GatewayName | Да | cloud:aws:storagegateway |
| Amazon SWF | Domain | - | cloud:aws:swf |
| AWS Transfer Family | ServerId | Да | cloud:aws:transfer |
| AWS Transit Gateway | TransitGateway | Да | cloud:aws:transitgateway |
| AWS Site-to-Site VPN | VpnId | Да | cloud:aws:vpn |
| Amazon WorkMail | OrganizationId | Да | cloud:aws:workmail |
| Amazon WorkSpaces | WorkspaceId | Да | cloud:aws:workspaces |

## Configuration API

Для получения списка всех поддерживаемых сервисов AWS в вашем кластере текущей версии используйте [API поддерживаемых сервисов AWS](/docs/dynatrace-api/configuration-api/aws-supported-services "Получение списка поддерживаемых сервисов AWS через Dynatrace API.").

## Потребление мониторинга

Начиная с 2021 года все облачные сервисы потребляют DDU. Объём потребления DDU для каждого экземпляра сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU).
