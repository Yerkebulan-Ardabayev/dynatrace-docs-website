---
title: Все облачные сервисы AWS
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services
scraped: 2026-03-06T21:18:24.141243
---

ActiveGate версии 1.245+

Благодаря интеграции мониторинга AWS классические (ранее называвшиеся «встроенными») сервисы отслеживаются автоматически. Вы также можете отслеживать другие сервисы AWS, которые влияют на производительность ваших приложений, размещённых в AWS.

Вы можете получать метрики Amazon CloudWatch для нескольких предопределённых сервисов. Вы можете просматривать графики для каждого экземпляра сервиса с набором измерений и создавать пользовательские графики, которые можно закреплять на дашбордах. Вы можете снизить затраты на CloudWatch и ограничение запросов, выбирая, какие дополнительные сервисы отслеживать. Кроме того, для неклассических сервисов вы можете выбирать, какие метрики отслеживать.

## Облачные сервисы AWS, отслеживаемые по умолчанию

В результате [интеграции мониторинга AWS](cloudwatch-metrics.md "Интеграция метрик из Amazon CloudWatch.") некоторые сервисы отслеживаются автоматически. Такие сервисы отмечены как классические.

[Amazon Dynamo Database (классический)](aws-all-services/aws-service-dynamo-db-builtin.md) [Amazon EC2 (классический)](cloudwatch-metrics/cloudwatch-ec2/ec2-builtin.md) [Amazon EC2 Auto Scaling (классический)](cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling-builltin.md) [AWS Lambda (классический)](cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin.md) [AWS Application and Network Load Balancer (классический)](aws-all-services/aws-service-application-and-network-load-balancer-builtin.md) [Elastic Load Balancer (классический)](aws-all-services/aws-service-elastic-load-balancer-builtin.md) [Amazon S3 (классический)](aws-all-services/aws-service-simple-storage-service-s3-builtin.md) [Amazon RDS (классический)](aws-all-services/aws-service-relational-database-service-rds-builtin.md) [Amazon EBS (классический)](aws-all-services/aws-service-elastic-block-store-ebs-builtin.md)

Информацию о различиях между классическими сервисами и другими сервисами см. в разделе [Миграция с классических (ранее «встроенных») сервисов AWS на облачные сервисы](cloudwatch-metrics/aws-migration-guide.md "Миграция классических сервисов AWS на новые версии.").

## Другие облачные сервисы AWS

В дополнение к облачным сервисам, отслеживаемым по умолчанию, вы можете отслеживать другие сервисы AWS, влияющие на производительность ваших приложений, размещённых в AWS.

[Amazon DynamoDB](aws-all-services/aws-service-dynamodb-new.md) [Amazon EBS](aws-all-services/aws-service-ebs-new.md) [AWS Lambda](aws-all-services/aws-service-lambda-new.md) [Amazon RDS](aws-all-services/aws-service-relational-database-service-rds-new.md) [AWS Certificate Manager Private Certificate Authority (ACM PCA)](aws-all-services/aws-service-acm-pca.md) [Amazon API Gateway](aws-all-services/aws-service-api-gateway.md) [Amazon AppStream 2.0](aws-all-services/aws-service-appstream-2.md) [AWS AppSync](aws-all-services/aws-service-appsync.md) [AWS App Runner](../integrate-into-aws/app-runner.md) [Amazon Athena](aws-all-services/aws-service-athena.md) [Amazon Aurora](aws-all-services/aws-service-aurora.md) [AWS Billing](aws-all-services/aws-service-billing.md) [AWS Chatbot](aws-all-services/aws-service-chatbot.md) [Amazon CloudFront](aws-all-services/aws-service-cloudfront.md) [AWS CloudHSM (V2)](aws-all-services/aws-service-cloudhsm-v2.md) [Amazon CloudSearch](aws-all-services/aws-service-cloudsearch.md) [Amazon CloudWatch Logs](aws-all-services/aws-service-cloudwatch-logs.md) [AWS API Usage](aws-all-services/aws-service-api-usage.md) [AWS CodeBuild](aws-all-services/aws-service-codebuild.md) [Amazon Cognito](aws-all-services/aws-service-cognito.md) [Amazon Connect](aws-all-services/aws-service-connect.md) [AWS Database Migration Service (AWS DMS)](aws-all-services/aws-service-database-migration-service-dms.md) [AWS DataSync](aws-all-services/aws-service-datasync.md) [AWS Direct Connect](aws-all-services/aws-service-direct-connect.md) [Amazon DocumentDB](aws-all-services/aws-service-documentdb.md) [Amazon DynamoDB Accelerator (DAX)](aws-all-services/aws-service-dynamodb.md) [Amazon EC2 API](cloudwatch-metrics/cloudwatch-ec2/ec2-api.md) [Amazon EC2 Auto Scaling](cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling.md) [Amazon EC2 Spot Fleet](cloudwatch-metrics/cloudwatch-ec2/ec2-spot-fleet.md) [Amazon ECS Container Insights](cloudwatch-metrics/cloudwatch-ecs/ecs-container-insights.md) [Amazon ElastiCache](aws-all-services/aws-service-elasticache.md) [AWS Elastic Beanstalk](cloudwatch-metrics/cloudwatch-elastic-beanstalk.md) [Amazon Elastic Container Service (ECS)](cloudwatch-metrics/cloudwatch-ecs.md) [Amazon Elastic File System (EFS)](aws-all-services/aws-service-elastic-file-system-efs.md) [Amazon Elastic Inference](aws-all-services/aws-service-elastic-inference.md) [Amazon Elastic Kubernetes Service (EKS)](cloudwatch-metrics/cloudwatch-eks.md) [Amazon Elastic MapReduce (EMR)](aws-all-services/aws-service-elastic-mapreduce-emr.md) [Amazon Elasticsearch Service (ES)](aws-all-services/aws-service-elasticsearch-service-es.md) [Amazon Elastic Transcoder](aws-all-services/aws-service-elastic-transcoder.md) [AWS Elemental MediaConnect](aws-all-services/aws-service-elemental-mediaconnect.md) [AWS Elemental MediaConvert](aws-all-services/aws-service-elemental-mediaconvert.md) [AWS Elemental MediaPackage](aws-all-services/aws-service-elemental-mediapackage.md) [AWS Elemental MediaTailor](aws-all-services/aws-service-elemental-mediatailor.md) [Amazon EventBridge](aws-all-services/aws-service-eventbridge.md) [Amazon FSx](aws-all-services/aws-service-fsx.md) [Amazon GameLift](aws-all-services/aws-service-gamelift.md) [AWS Glue](aws-all-services/aws-service-glue.md) [Amazon Inspector](aws-all-services/aws-service-inspector.md) [AWS IoT](aws-all-services/aws-service-iot.md) [AWS IoT Analytics](aws-all-services/aws-service-iot-analytics.md) [AWS IoT Things Graph](aws-all-services/aws-service-iot-things-graph.md) [Amazon Keyspaces (Cassandra)](aws-all-services/aws-service-keyspaces-cassandra.md) [Amazon Kinesis](aws-all-services/aws-service-kinesis.md) [Amazon Lex](aws-all-services/aws-service-lex.md) [Amazon MSK (Kafka)](aws-all-services/aws-service-msk-kafka.md) [Amazon MQ](aws-all-services/aws-service-mq.md) [Amazon Neptune](aws-all-services/aws-service-neptune.md) [AWS OpsWorks](aws-all-services/aws-service-opsworks.md) [Amazon Polly](aws-all-services/aws-service-polly.md) [Amazon QLDB](aws-all-services/aws-service-quantum-ledger-database-qldb.md) [Amazon Redshift](aws-all-services/aws-service-redshift.md) [Amazon Rekognition](aws-all-services/aws-service-rekognition.md) [AWS RoboMaker](aws-all-services/aws-service-robomaker.md) [Amazon Route 53](aws-all-services/aws-service-route-53.md) [Amazon Route 53 Resolver](aws-all-services/aws-service-route-53-resolver.md) [Amazon SageMaker](aws-all-services/aws-service-sagemaker.md) [AWS Service Catalog](aws-all-services/aws-service-service-catalog.md) [Amazon Simple Email Service (SES)](aws-all-services/aws-service-simple-email-service-ses.md) [Amazon Simple Notification Service (SNS)](aws-all-services/aws-service-simple-notification-service-sns.md) [Amazon Simple Queue Service (SQS)](aws-all-services/aws-service-simple-queue-service-sqs.md) [Amazon Simple Storage Service (S3)](aws-all-services/aws-service-simple-storage-service-s3.md) [Amazon Simple Workflow Service (SWF)](aws-all-services/aws-service-simple-workflow-service-swf.md) [AWS Step Functions](aws-all-services/aws-service-step-functions.md) [AWS Storage Gateway](aws-all-services/aws-service-storage-gateway.md) [AWS Systems Manager Run Command](aws-all-services/aws-service-systems-manager-run-command.md) [Amazon Textract](aws-all-services/aws-service-textract.md) [AWS Transfer Family](aws-all-services/aws-service-transfer-family.md) [AWS Transit Gateway](aws-all-services/aws-service-transit-gateway.md) [Amazon Translate](aws-all-services/aws-service-translate.md) [AWS Trusted Advisor](aws-all-services/aws-service-trusted-advisor.md) [Amazon VPC NAT Gateways](aws-all-services/aws-service-vpc.md) [AWS Site-to-Site VPN](aws-all-services/aws-service-site-to-site-vpn.md) [AWS WAF Classic](aws-all-services/aws-service-waf-classic.md) [AWS WAF](aws-all-services/aws-service-wafv2.md) [Amazon WorkMail](aws-all-services/aws-service-workmail.md) [Amazon WorkSpaces](aws-all-services/aws-service-workspaces.md)

## Облачные сервисы и соответствующие им типы сущностей Dynatrace

Не для всех облачных сервисов создаются сущности Dynatrace и не для всех можно импортировать теги из облака. Разверните таблицу ниже, чтобы увидеть облачные сервисы с соответствующими типами сущностей Dynatrace и проверить, импортируются ли для них теги от облачного провайдера.

### Список сервисов AWS с сущностями и тегами

Для каждого не встроенного сервиса измерение `CUSTOM_DEVICE` генерируется на основе основного измерения.

| Сервис | Облачный экземпляр | Мониторинг и фильтрация тегов | Тип сущности Dynatrace |
| --- | --- | --- | --- |
| Amazon EC2 Auto Scaling (встроенный) | AutoScalingGroupName | Да | AUTO\_SCALING\_GROUP |
| AWS Lambda (встроенный) | FunctionName | Да | AWS\_LAMBDA\_FUNCTION |
| Amazon Application and Network Load Balancer (встроенный) | LoadBalancer | Да | AWS\_APPLICATION\_LOAD\_BALANCER |
| Amazon Application and Network Load Balancer (встроенный) | LoadBalancer | Да | AWS\_NETWORK\_LOAD\_BALANCER |
| Amazon EBS (встроенный) | VolumeId | Да | EBS\_VOLUME |
| Amazon EC2 (встроенный) | InstanceId | Да | EC2\_INSTANCE |
| Amazon Elastic Load Balancer (ELB) (встроенный) | LoadBalancerName | Да | ELASTIC\_LOAD\_BALANCER |
| Amazon RDS (встроенный) | DBInstanceIdentifier | Да | RELATIONAL\_DATABASE\_SERVICE |
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

## API конфигурации

Для получения списка всех поддерживаемых сервисов AWS в вашем кластере текущей версии используйте [API поддерживаемых сервисов AWS](../../../dynatrace-api/configuration-api/aws-supported-services.md "Получение списка поддерживаемых сервисов AWS через Dynatrace API.").

## Потребление мониторинга

Начиная с 2021 года все облачные сервисы потребляют DDU. Объём потребления DDU для каждого экземпляра сервиса зависит от количества отслеживаемых метрик и их измерений (каждое измерение метрики приводит к приёму 1 точки данных; 1 точка данных потребляет 0,001 DDU).
