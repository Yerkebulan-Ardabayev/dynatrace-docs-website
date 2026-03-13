---
title: All AWS cloud services
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services
scraped: 2026-03-06T21:18:24.141243
---

# All AWS cloud services

# All AWS cloud services

* Classic
* Overview
* 12-min read
* Updated on Feb 12, 2024

ActiveGate version 1.245+

With AWS monitoring integration, classic (formerly "built-in") services are monitored out-of-the-box. You can also monitor other AWS services that influence the performance of your AWS-hosted applications.

You can receive Amazon CloudWatch metrics for multiple predefined services. You can view graphs per service instance, with a set of dimensions, and create custom graphs that you can pin to your dashboards. You can reduce your CloudWatch costs and throttling by selecting which additional services to monitor. Additionally, for non-classic services, you can choose which metrics you want to monitor.

## AWS cloud services monitored by default

As a result of [AWS monitoring integration](cloudwatch-metrics.md "Integrate metrics from Amazon CloudWatch."), some services are monitored out-of-the-box. Such services are marked as classic.

[Amazon Dynamo Database (classic)](aws-all-services/aws-service-dynamo-db-builtin.md) [Amazon EC2 (classic)](cloudwatch-metrics/cloudwatch-ec2/ec2-builtin.md) [Amazon EC2 Auto Scaling (classic)](cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling-builltin.md) [AWS Lambda (classic)](cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin.md) [AWS Application and Network Load Balancer (classic)](aws-all-services/aws-service-application-and-network-load-balancer-builtin.md) [Elastic Load Balancer (classic)](aws-all-services/aws-service-elastic-load-balancer-builtin.md) [Amazon S3 (classic)](aws-all-services/aws-service-simple-storage-service-s3-builtin.md) [Amazon RDS (classic)](aws-all-services/aws-service-relational-database-service-rds-builtin.md) [Amazon EBS (classic)](aws-all-services/aws-service-elastic-block-store-ebs-builtin.md) 

For information about differences between classic services and other services, see [Migrate from AWS classic (formerly 'built-in') services to cloud services](cloudwatch-metrics/aws-migration-guide.md "Migrate AWS classic services to their new versions.").

## Other AWS cloud services

In addition to cloud services monitored by default, you can monitor other AWS services that affect the performance of your AWS-hosted applications.

[Amazon DynamoDB](aws-all-services/aws-service-dynamodb-new.md) [Amazon EBS](aws-all-services/aws-service-ebs-new.md) [AWS Lambda](aws-all-services/aws-service-lambda-new.md) [Amazon RDS](aws-all-services/aws-service-relational-database-service-rds-new.md) [AWS Certificate Manager Private Certificate Authority (ACM PCA)](aws-all-services/aws-service-acm-pca.md) [Amazon API Gateway](aws-all-services/aws-service-api-gateway.md) [Amazon AppStream 2.0](aws-all-services/aws-service-appstream-2.md) [AWS AppSync](aws-all-services/aws-service-appsync.md) [AWS App Runner](../integrate-into-aws/app-runner.md) [Amazon Athena](aws-all-services/aws-service-athena.md) [Amazon Aurora](aws-all-services/aws-service-aurora.md) [AWS Billing](aws-all-services/aws-service-billing.md) [AWS Chatbot](aws-all-services/aws-service-chatbot.md) [Amazon CloudFront](aws-all-services/aws-service-cloudfront.md) [AWS CloudHSM (V2)](aws-all-services/aws-service-cloudhsm-v2.md) [Amazon CloudSearch](aws-all-services/aws-service-cloudsearch.md) [Amazon CloudWatch Logs](aws-all-services/aws-service-cloudwatch-logs.md) [AWS API Usage](aws-all-services/aws-service-api-usage.md) [AWS CodeBuild](aws-all-services/aws-service-codebuild.md) [Amazon Cognito](aws-all-services/aws-service-cognito.md) [Amazon Connect](aws-all-services/aws-service-connect.md) [AWS Database Migration Service (AWS DMS)](aws-all-services/aws-service-database-migration-service-dms.md) [AWS DataSync](aws-all-services/aws-service-datasync.md) [AWS Direct Connect](aws-all-services/aws-service-direct-connect.md) [Amazon DocumentDB](aws-all-services/aws-service-documentdb.md) [Amazon DynamoDB Accelerator (DAX)](aws-all-services/aws-service-dynamodb.md) [Amazon EC2 API](cloudwatch-metrics/cloudwatch-ec2/ec2-api.md) [Amazon EC2 Auto Scaling](cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling.md) [Amazon EC2 Spot Fleet](cloudwatch-metrics/cloudwatch-ec2/ec2-spot-fleet.md) [Amazon ECS Container Insights](cloudwatch-metrics/cloudwatch-ecs/ecs-container-insights.md) [Amazon ElastiCache](aws-all-services/aws-service-elasticache.md) [AWS Elastic Beanstalk](cloudwatch-metrics/cloudwatch-elastic-beanstalk.md) [Amazon Elastic Container Service (ECS)](cloudwatch-metrics/cloudwatch-ecs.md) [Amazon Elastic File System (EFS)](aws-all-services/aws-service-elastic-file-system-efs.md) [Amazon Elastic Inference](aws-all-services/aws-service-elastic-inference.md) [Amazon Elastic Kubernetes Service (EKS)](cloudwatch-metrics/cloudwatch-eks.md) [Amazon Elastic MapReduce (EMR)](aws-all-services/aws-service-elastic-mapreduce-emr.md) [Amazon Elasticsearch Service (ES)](aws-all-services/aws-service-elasticsearch-service-es.md) [Amazon Elastic Transcoder](aws-all-services/aws-service-elastic-transcoder.md) [AWS Elemental MediaConnect](aws-all-services/aws-service-elemental-mediaconnect.md) [AWS Elemental MediaConvert](aws-all-services/aws-service-elemental-mediaconvert.md) [AWS Elemental MediaPackage](aws-all-services/aws-service-elemental-mediapackage.md) [AWS Elemental MediaTailor](aws-all-services/aws-service-elemental-mediatailor.md) [Amazon EventBridge](aws-all-services/aws-service-eventbridge.md) [Amazon FSx](aws-all-services/aws-service-fsx.md) [Amazon GameLift](aws-all-services/aws-service-gamelift.md) [AWS Glue](aws-all-services/aws-service-glue.md) [Amazon Inspector](aws-all-services/aws-service-inspector.md) [AWS IoT](aws-all-services/aws-service-iot.md) [AWS IoT Analytics](aws-all-services/aws-service-iot-analytics.md) [AWS IoT Things Graph](aws-all-services/aws-service-iot-things-graph.md) [Amazon Keyspaces (Cassandra)](aws-all-services/aws-service-keyspaces-cassandra.md) [Amazon Kinesis](aws-all-services/aws-service-kinesis.md) [Amazon Lex](aws-all-services/aws-service-lex.md) [Amazon MSK (Kafka)](aws-all-services/aws-service-msk-kafka.md) [Amazon MQ](aws-all-services/aws-service-mq.md) [Amazon Neptune](aws-all-services/aws-service-neptune.md) [AWS OpsWorks](aws-all-services/aws-service-opsworks.md) [Amazon Polly](aws-all-services/aws-service-polly.md) [Amazon QLDB](aws-all-services/aws-service-quantum-ledger-database-qldb.md) [Amazon Redshift](aws-all-services/aws-service-redshift.md) [Amazon Rekognition](aws-all-services/aws-service-rekognition.md) [AWS RoboMaker](aws-all-services/aws-service-robomaker.md) [Amazon Route 53](aws-all-services/aws-service-route-53.md) [Amazon Route 53 Resolver](aws-all-services/aws-service-route-53-resolver.md) [Amazon SageMaker](aws-all-services/aws-service-sagemaker.md) [AWS Service Catalog](aws-all-services/aws-service-service-catalog.md) [Amazon Simple Email Service (SES)](aws-all-services/aws-service-simple-email-service-ses.md) [Amazon Simple Notification Service (SNS)](aws-all-services/aws-service-simple-notification-service-sns.md) [Amazon Simple Queue Service (SQS)](aws-all-services/aws-service-simple-queue-service-sqs.md) [Amazon Simple Storage Service (S3)](aws-all-services/aws-service-simple-storage-service-s3.md) [Amazon Simple Workflow Service (SWF)](aws-all-services/aws-service-simple-workflow-service-swf.md) [AWS Step Functions](aws-all-services/aws-service-step-functions.md) [AWS Storage Gateway](aws-all-services/aws-service-storage-gateway.md) [AWS Systems Manager Run Command](aws-all-services/aws-service-systems-manager-run-command.md) [Amazon Textract](aws-all-services/aws-service-textract.md) [AWS Transfer Family](aws-all-services/aws-service-transfer-family.md) [AWS Transit Gateway](aws-all-services/aws-service-transit-gateway.md) [Amazon Translate](aws-all-services/aws-service-translate.md) [AWS Trusted Advisor](aws-all-services/aws-service-trusted-advisor.md) [Amazon VPC NAT Gateways](aws-all-services/aws-service-vpc.md) [AWS Site-to-Site VPN](aws-all-services/aws-service-site-to-site-vpn.md) [AWS WAF Classic](aws-all-services/aws-service-waf-classic.md) [AWS WAF](aws-all-services/aws-service-wafv2.md) [Amazon WorkMail](aws-all-services/aws-service-workmail.md) [Amazon WorkSpaces](aws-all-services/aws-service-workspaces.md) 

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

To list all AWS-supported services on your cluster by the current version, use the [AWS-supported services API](../../../dynatrace-api/configuration-api/aws-supported-services.md "Fetch a list of AWS supported services via the Dynatrace API.").

## Monitoring consumption

As of 2021, all cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs).