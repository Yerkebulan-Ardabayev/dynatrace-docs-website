---
title: All AWS cloud services
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services
scraped: 2026-02-22T21:11:03.664641
---

# All AWS cloud services

# All AWS cloud services

* Overview
* 12-min read
* Updated on Feb 12, 2024

ActiveGate version 1.245+

With AWS monitoring integration, classic (formerly "built-in") services are monitored out-of-the-box. You can also monitor other AWS services that influence the performance of your AWS-hosted applications.

You can receive Amazon CloudWatch metrics for multiple predefined services. You can view graphs per service instance, with a set of dimensions, and create custom graphs that you can pin to your dashboards. You can reduce your CloudWatch costs and throttling by selecting which additional services to monitor. Additionally, for non-classic services, you can choose which metrics you want to monitor.

## AWS cloud services monitored by default

As a result of [AWS monitoring integration](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics "Integrate metrics from Amazon CloudWatch."), some services are monitored out-of-the-box. Such services are marked as classic.

[Amazon Dynamo Database (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamo-db-builtin) [Amazon EC2 (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-builtin) [Amazon EC2 Auto Scaling (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling-builltin) [AWS Lambda (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-lambda-cloudwatch-metrics/lambda-builtin) [AWS Application and Network Load Balancer (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-application-and-network-load-balancer-builtin) [Elastic Load Balancer (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-load-balancer-builtin) [Amazon S3 (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3-builtin) [Amazon RDS (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-builtin) [Amazon EBS (classic)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-block-store-ebs-builtin) 

For information about differences between classic services and other services, see [Migrate from AWS classic (formerly 'built-in') services to cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Migrate AWS classic services to their new versions.").

## Other AWS cloud services

In addition to cloud services monitored by default, you can monitor other AWS services that affect the performance of your AWS-hosted applications.

[Amazon DynamoDB](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb-new) [Amazon EBS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-ebs-new) [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lambda-new) [Amazon RDS](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new) [AWS Certificate Manager Private Certificate Authority (ACM PCA)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-acm-pca) [Amazon API Gateway](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-gateway) [Amazon AppStream 2.0](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-appstream-2) [AWS AppSync](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-appsync) [AWS App Runner](/docs/ingest-from/amazon-web-services/integrate-into-aws/app-runner) [Amazon Athena](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-athena) [Amazon Aurora](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-aurora) [AWS Billing](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-billing) [AWS Chatbot](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-chatbot) [Amazon CloudFront](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudfront) [AWS CloudHSM (V2)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudhsm-v2) [Amazon CloudSearch](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudsearch) [Amazon CloudWatch Logs](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cloudwatch-logs) [AWS API Usage](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-api-usage) [AWS CodeBuild](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-codebuild) [Amazon Cognito](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-cognito) [Amazon Connect](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-connect) [AWS Database Migration Service (AWS DMS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-database-migration-service-dms) [AWS DataSync](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-datasync) [AWS Direct Connect](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-direct-connect) [Amazon DocumentDB](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-documentdb) [Amazon DynamoDB Accelerator (DAX)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb) [Amazon EC2 API](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-api) [Amazon EC2 Auto Scaling](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-auto-scaling) [Amazon EC2 Spot Fleet](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ec2/ec2-spot-fleet) [Amazon ECS Container Insights](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs/ecs-container-insights) [Amazon ElastiCache](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticache) [AWS Elastic Beanstalk](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-elastic-beanstalk) [Amazon Elastic Container Service (ECS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-ecs) [Amazon Elastic File System (EFS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-file-system-efs) [Amazon Elastic Inference](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-inference) [Amazon Elastic Kubernetes Service (EKS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/cloudwatch-eks) [Amazon Elastic MapReduce (EMR)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-mapreduce-emr) [Amazon Elasticsearch Service (ES)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticsearch-service-es) [Amazon Elastic Transcoder](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-transcoder) [AWS Elemental MediaConnect](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconnect) [AWS Elemental MediaConvert](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconvert) [AWS Elemental MediaPackage](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediapackage) [AWS Elemental MediaTailor](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediatailor) [Amazon EventBridge](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-eventbridge) [Amazon FSx](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-fsx) [Amazon GameLift](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-gamelift) [AWS Glue](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-glue) [Amazon Inspector](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-inspector) [AWS IoT](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot) [AWS IoT Analytics](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-analytics) [AWS IoT Things Graph](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-iot-things-graph) [Amazon Keyspaces (Cassandra)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-keyspaces-cassandra) [Amazon Kinesis](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-kinesis) [Amazon Lex](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-lex) [Amazon MSK (Kafka)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-msk-kafka) [Amazon MQ](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-mq) [Amazon Neptune](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-neptune) [AWS OpsWorks](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-opsworks) [Amazon Polly](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-polly) [Amazon QLDB](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-quantum-ledger-database-qldb) [Amazon Redshift](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-redshift) [Amazon Rekognition](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-rekognition) [AWS RoboMaker](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-robomaker) [Amazon Route 53](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-route-53) [Amazon Route 53 Resolver](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-route-53-resolver) [Amazon SageMaker](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-sagemaker) [AWS Service Catalog](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-service-catalog) [Amazon Simple Email Service (SES)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-email-service-ses) [Amazon Simple Notification Service (SNS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-notification-service-sns) [Amazon Simple Queue Service (SQS)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-queue-service-sqs) [Amazon Simple Storage Service (S3)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-storage-service-s3) [Amazon Simple Workflow Service (SWF)](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-simple-workflow-service-swf) [AWS Step Functions](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-step-functions) [AWS Storage Gateway](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-storage-gateway) [AWS Systems Manager Run Command](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-systems-manager-run-command) [Amazon Textract](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-textract) [AWS Transfer Family](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-transfer-family) [AWS Transit Gateway](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-transit-gateway) [Amazon Translate](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-translate) [AWS Trusted Advisor](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-trusted-advisor) [Amazon VPC NAT Gateways](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-vpc) [AWS Site-to-Site VPN](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-site-to-site-vpn) [AWS WAF Classic](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-waf-classic) [AWS WAF](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-wafv2) [Amazon WorkMail](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-workmail) [Amazon WorkSpaces](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-workspaces) 

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

To list all AWS-supported services on your cluster by the current version, use the [AWS-supported services API](/docs/dynatrace-api/configuration-api/aws-supported-services "Fetch a list of AWS supported services via the Dynatrace API.").

## Monitoring consumption

As of 2021, all cloud services consume DDUs. The amount of DDU consumption per service instance depends on the number of monitored metrics and their dimensions (each metric dimension results in the ingestion of 1 data point; 1 data point consumes 0.001 DDUs).