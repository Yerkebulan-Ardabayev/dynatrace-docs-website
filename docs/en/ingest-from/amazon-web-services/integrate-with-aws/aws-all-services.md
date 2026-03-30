---
title: All AWS cloud services
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services
scraped: 2026-03-06T21:18:24.141243
---

# All AWS cloud services


* Classic
* Overview
* 12-min read
* Updated on Feb 12, 2024

ActiveGate version 1.245+

With AWS monitoring integration, classic (formerly "built-in") services are monitored out-of-the-box. You can also monitor other AWS services that influence the performance of your AWS-hosted applications.

You can receive Amazon CloudWatch metrics for multiple predefined services. You can view graphs per service instance, with a set of dimensions, and create custom graphs that you can pin to your dashboards. You can reduce your CloudWatch costs and throttling by selecting which additional services to monitor. Additionally, for non-classic services, you can choose which metrics you want to monitor.

## AWS cloud services monitored by default

As a result of AWS monitoring integration, some services are monitored out-of-the-box. Such services are marked as classic.

Amazon Dynamo Database (classic) Amazon EC2 (classic) Amazon EC2 Auto Scaling (classic) AWS Lambda (classic) AWS Application and Network Load Balancer (classic) Elastic Load Balancer (classic) Amazon S3 (classic) Amazon RDS (classic) Amazon EBS (classic) 

For information about differences between classic services and other services, see Migrate from AWS classic (formerly 'built-in') services to cloud services.

## Other AWS cloud services

In addition to cloud services monitored by default, you can monitor other AWS services that affect the performance of your AWS-hosted applications.

[Amazon DynamoDB](aws-all-services/aws-service-dynamodb-new.md) [Amazon EBS](aws-all-services/aws-service-ebs-new.md) [AWS Lambda](aws-all-services/aws-service-lambda-new.md) [Amazon RDS](aws-all-services/aws-service-relational-database-service-rds-new.md) AWS Certificate Manager Private Certificate Authority (ACM PCA) Amazon API Gateway [Amazon AppStream 2.0](aws-all-services/aws-service-appstream-2.md) [AWS AppSync](aws-all-services/aws-service-appsync.md) [AWS App Runner](../integrate-into-aws/app-runner.md) Amazon Athena Amazon Aurora AWS Billing [AWS Chatbot](aws-all-services/aws-service-chatbot.md) Amazon CloudFront [AWS CloudHSM (V2)](aws-all-services/aws-service-cloudhsm-v2.md) Amazon CloudSearch [Amazon CloudWatch Logs](aws-all-services/aws-service-cloudwatch-logs.md) AWS API Usage [AWS CodeBuild](aws-all-services/aws-service-codebuild.md) Amazon Cognito [Amazon Connect](aws-all-services/aws-service-connect.md) [AWS Database Migration Service (AWS DMS)](aws-all-services/aws-service-database-migration-service-dms.md) AWS DataSync [AWS Direct Connect](aws-all-services/aws-service-direct-connect.md) Amazon DocumentDB Amazon DynamoDB Accelerator (DAX) Amazon EC2 API [Amazon EC2 Auto Scaling](cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling.md) Amazon EC2 Spot Fleet Amazon ECS Container Insights Amazon ElastiCache [AWS Elastic Beanstalk](cloudwatch-metrics/cloudwatch-elastic-beanstalk.md) Amazon Elastic Container Service (ECS) Amazon Elastic File System (EFS) [Amazon Elastic Inference](aws-all-services/aws-service-elastic-inference.md) [Amazon Elastic Kubernetes Service (EKS)](cloudwatch-metrics/cloudwatch-eks.md) Amazon Elastic MapReduce (EMR) Amazon Elasticsearch Service (ES) [Amazon Elastic Transcoder](aws-all-services/aws-service-elastic-transcoder.md) [AWS Elemental MediaConnect](aws-all-services/aws-service-elemental-mediaconnect.md) [AWS Elemental MediaConvert](aws-all-services/aws-service-elemental-mediaconvert.md) [AWS Elemental MediaPackage](aws-all-services/aws-service-elemental-mediapackage.md) [AWS Elemental MediaTailor](aws-all-services/aws-service-elemental-mediatailor.md) [Amazon EventBridge](aws-all-services/aws-service-eventbridge.md) [Amazon FSx](aws-all-services/aws-service-fsx.md) Amazon GameLift AWS Glue [Amazon Inspector](aws-all-services/aws-service-inspector.md) AWS IoT AWS IoT Analytics AWS IoT Things Graph Amazon Keyspaces (Cassandra) Amazon Kinesis Amazon Lex Amazon MSK (Kafka) [Amazon MQ](aws-all-services/aws-service-mq.md) [Amazon Neptune](aws-all-services/aws-service-neptune.md) [AWS OpsWorks](aws-all-services/aws-service-opsworks.md) [Amazon Polly](aws-all-services/aws-service-polly.md) [Amazon QLDB](aws-all-services/aws-service-quantum-ledger-database-qldb.md) Amazon Redshift [Amazon Rekognition](aws-all-services/aws-service-rekognition.md) [AWS RoboMaker](aws-all-services/aws-service-robomaker.md) [Amazon Route 53](aws-all-services/aws-service-route-53.md) [Amazon Route 53 Resolver](aws-all-services/aws-service-route-53-resolver.md) Amazon SageMaker AWS Service Catalog Amazon Simple Email Service (SES) Amazon Simple Notification Service (SNS) Amazon Simple Queue Service (SQS) Amazon Simple Storage Service (S3) [Amazon Simple Workflow Service (SWF)](aws-all-services/aws-service-simple-workflow-service-swf.md) [AWS Step Functions](aws-all-services/aws-service-step-functions.md) [AWS Storage Gateway](aws-all-services/aws-service-storage-gateway.md) [AWS Systems Manager Run Command](aws-all-services/aws-service-systems-manager-run-command.md) Amazon Textract [AWS Transfer Family](aws-all-services/aws-service-transfer-family.md) [AWS Transit Gateway](aws-all-services/aws-service-transit-gateway.md) Amazon Translate AWS Trusted Advisor Amazon VPC NAT Gateways [AWS Site-to-Site VPN](aws-all-services/aws-service-site-to-site-vpn.md) [AWS WAF Classic](aws-all-services/aws-service-waf-classic.md) AWS WAF [Amazon WorkMail](aws-all-services/aws-service-workmail.md) [Amazon WorkSpaces](aws-all-services/aws-service-workspaces.md) 

## Cloud services with their respective Dynatrace entity types

Not all cloud services have Dynatrace entities created for them and can have tags imported from the cloud. Expand the table below to see cloud services with their respective Dynatrace entity types and to check if they have tags imported from the cloud provider.

### List of AWS services with entities and tags

For each non-built-in service, the `CUSTOM_DEVICE` dimension is generated based on the main dimension

| Service | Cloud instance | Tag monitoring and filtering | Dynatrace entity type |
| --- | --- | --- | --- |
| Amazon EC2 Auto Scaling (built-in) | AutoScalingGroupName | Applicable | AUTO\_SCALING\_GROUP |
| AWS Lambda (built-in) | FunctionName | Applicable | AWS\_LAMBDA\_FUNCTION |
| Amazon Application and Network Load Balancer (built-in) | LoadBalancer | Applicable | AWS\_APPLICATION\_LOAD\_BALANCER |
| Amazon Application and Network Load Balancer (built-in) | LoadBalancer | Applicable | AWS\_NETWORK\_LOAD\_BALANCER |
| Amazon EBS (built-in) | VolumeId | Applicable | EBS\_VOLUME |
| Amazon EC2 (built-in) | InstanceId | Applicable | EC2\_INSTANCE |
| Amazon Elastic Load Balancer (ELB) (built-in) | LoadBalancerName | Applicable | ELASTIC\_LOAD\_BALANCER |
| Amazon RDS (built-in) | DBInstanceIdentifier | Applicable | RELATIONAL\_DATABASE\_SERVICE |
| AWS Certificate Manager Private Certificate Authority | PrivateCAArn | Applicable | cloud:aws:acmprivateca |
| Amazon API Gateway | ApiName | Applicable | cloud:aws:api\_gateway |
| AWS App Runner | ServiceName | Applicable | cloud:aws:app\_runner |
| Amazon AppStream | Fleet | Applicable | cloud:aws:appstream |
| AWS AppSync | GraphQLAPIId | Applicable | cloud:aws:appsync |
| Amazon Athena | WorkGroup | Applicable | cloud:aws:athena |
| Amazon Aurora | DBClusterIdentifier | Applicable | cloud:aws:aurora |
| Amazon EC2 Auto Scaling | AutoScalingGroupName | - | cloud:aws:autoscaling |
| Amazon CloudFront | DistributionId | Applicable | cloud:aws:cloud\_front |
| AWS CloudHSM | ClusterId | Applicable | cloud:aws:cloudhsm |
| Amazon CloudSearch | DomainName | - | cloud:aws:cloudsearch |
| AWS CodeBuild | ProjectName | Applicable | cloud:aws:codebuild |
| AWS DataSync | TaskId | Applicable | cloud:aws:datasync |
| Amazon DynamoDB Accelerator (DAX) | ClusterId | Applicable | cloud:aws:dax |
| AWS Database Migration Service (AWS DMS) | ReplicationInstanceIdentifier | Applicable | cloud:aws:dms |
| Amazon DocumentDB | DBClusterIdentifier | Applicable | cloud:aws:documentdb |
| AWS Direct Connect | ConnectionId | Applicable | cloud:aws:dxcon |
| Amazon DynamoDB | TableName | Applicable | cloud:aws:dynamodb |
| Amazon EBS | VolumeId | Applicable | cloud:aws:ebs |
| Amazon EC2 Spot Fleet | FleetRequestId | - | cloud:aws:ec2\_spot |
| Amazon Elastic Container Service (ECS) | ClusterName | Applicable | cloud:aws:ecs |
| Amazon ECS Container Insights | ClusterName | Applicable | cloud:aws:ecs:cluster |
| Amazon Elastic File System (EFS) | FileSystemId | Applicable | cloud:aws:efs |
| Amazon Elastic Kubernetes Service (EKS) | ClusterName | Applicable | cloud:aws:eks:cluster |
| Amazon ElastiCache (EC) | CacheClusterId | Applicable | cloud:aws:elasticache |
| AWS Elastic Beanstalk | EnvironmentName | Applicable | cloud:aws:elasticbeanstalk |
| Amazon Elastic Transcoder | PipelineId | - | cloud:aws:elastictranscoder |
| Amazon Elasticsearch Service (ES) | DomainName | Applicable | cloud:aws:es |
| Amazon EventBridge | EventBusName | Applicable | cloud:aws:events |
| Amazon FSx | FileSystemId | Applicable | cloud:aws:fsx |
| Amazon GameLift | FleetId | - | cloud:aws:gamelift |
| AWS Glue | JobName | Applicable | cloud:aws:glue |
| Amazon Inspector | AssessmentTemplateArn | Applicable | cloud:aws:inspector |
| Amazon Managed Streaming for Kafka | Cluster Name | Applicable | cloud:aws:kafka |
| AWS Lambda | FunctionName | Applicable | cloud:aws:lambda |
| Amazon Lex | BotName | Applicable | cloud:aws:lex |
| Amazon CloudWatch Logs | LogGroupName | Applicable | cloud:aws:logs |
| AWS Elemental MediaTailor | ConfigurationName | Applicable | cloud:aws:media\_tailor |
| AWS Elemental MediaConnect | FlowARN | - | cloud:aws:mediaconnect |
| AWS Elemental MediaPackage Live | Channel | Applicable | cloud:aws:mediapackagelive |
| AWS Elemental MediaPackage Video on Demand | PackagingConfiguration | Applicable | cloud:aws:mediapackagevod |
| Amazon VPC NAT Gateways | NatGatewayId | Applicable | cloud:aws:nat\_gateway |
| Amazon Neptune | DBClusterIdentifier | Applicable | cloud:aws:neptune |
| AWS OpsWorks | StackId | Applicable | cloud:aws:opsworks |
| Amazon QLDB | LedgerName | Applicable | cloud:aws:qldb |
| Amazon RDS | DBInstanceIdentifier | Applicable | cloud:aws:rds |
| Amazon Redshift | ClusterIdentifier | Applicable | cloud:aws:redshift |
| AWS RoboMaker | SimulationJobId | Applicable | cloud:aws:robomaker |
| Amazon Route 53 | HostedZoneId | Applicable | cloud:aws:route53 |
| Amazon Route 53 Resolver | EndpointId | Applicable | cloud:aws:route53resolver |
| Amazon SageMaker Endpoints | EndpointName | Applicable | cloud:aws:sage\_maker:endpoint |
| Amazon SageMaker Endpoint Instances | EndpointName | Applicable | cloud:aws:sage\_maker:endpoint\_instance |
| Amazon Simple Notification Service (SNS) | TopicName | Applicable | cloud:aws:sns |
| Amazon Simple Queue Service (SQS) | QueueName | Applicable | cloud:aws:sqs |
| AWS Storage Gateway | GatewayName | Applicable | cloud:aws:storagegateway |
| Amazon SWF | Domain | - | cloud:aws:swf |
| AWS Transfer Family | ServerId | Applicable | cloud:aws:transfer |
| AWS Transit Gateway | TransitGateway | Applicable | cloud:aws:transitgateway |
| AWS Site-to-Site VPN | VpnId | Applicable | cloud:aws:vpn |
| Amazon WorkMail | OrganizationId | Applicable | cloud:aws:workmail |
| Amazon WorkSpaces | WorkspaceId | Applicable | cloud:aws:workspaces |

## Configuration API

To list all AWS-supported services on your cluster by the current version, use the AWS-supported services API.

## Monitoring consumption

As of 2021, all cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs).