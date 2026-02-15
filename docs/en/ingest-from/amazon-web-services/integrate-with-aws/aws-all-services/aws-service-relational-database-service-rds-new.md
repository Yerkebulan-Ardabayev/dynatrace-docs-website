---
title: Amazon RDS (Relational Database Service) monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-relational-database-service-rds-new
scraped: 2026-02-15T21:23:41.223049
---

# Amazon RDS (Relational Database Service) monitoring

# Amazon RDS (Relational Database Service) monitoring

* How-to guide
* 31-min read
* Updated on Nov 15, 2023

For information about differences between classic services and other services, see [Migrate from AWS classic (formerly 'built-in') services to cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics/aws-migration-guide "Migrate AWS classic services to their new versions.").

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon RDS. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

To enable monitoring for this service, you need

* ActiveGate version 1.197+

* For Dynatrace SaaS deployments, you need an Environment ActiveGate or a Multi-environment ActiveGate.

  For role-based access in [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") deployment, you need an [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") installed on an Amazon EC2 host.

* Dynatrace version 1.200+
* An updated [AWS monitoring policy](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Integrate metrics from Amazon CloudWatch.") to include the additional AWS services.

To [update the AWS IAM policyï»¿](https://dt-url.net/8q038eb), use the JSON below, containing the monitoring policy (permissions) for all supporting services.

JSON predefined policy for all supporting services

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

If you don't want to add permissions to all services, and just select permissions for certain services, consult the table below. The table contains a set of permissions that are required for [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.") and, for each supporting service, a list of optional permissions specific to that service.

Permissions required for AWS monitoring integration:

* `"cloudwatch:GetMetricData"`
* `"cloudwatch:GetMetricStatistics"`
* `"cloudwatch:ListMetrics"`
* `"sts:GetCallerIdentity"`
* `"tag:GetResources"`
* `"tag:GetTagKeys"`
* `"ec2:DescribeAvailabilityZones"`

### Complete list of permissions for cloud services

| Name | Permissions |
| --- | --- |
| All monitored Amazon services Required | `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, `cloudwatch:ListMetrics`, `sts:GetCallerIdentity`, `tag:GetResources`, `tag:GetTagKeys`, `ec2:DescribeAvailabilityZones` |
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

Example of JSON policy for one single service.

JSON policy for Amazon API Gateway

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

In this example, from the complete list of permissions you need to select

* `"apigateway:GET"` for **Amazon API Gateway**
* `"cloudwatch:GetMetricData"`, `"cloudwatch:GetMetricStatistics"`, `"cloudwatch:ListMetrics"`, `"sts:GetCallerIdentity"`, `"tag:GetResources"`, `"tag:GetTagKeys"`, and `"ec2:DescribeAvailabilityZones"` for **All AWS cloud services**.

### AWS endpoints that need to be reachable from ActiveGate with corresponding AWS services

| Endpoint | Service |
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

## Enable monitoring

To learn how to enable service monitoring, see [Enable service monitoring](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-metrics-ingest/aws-enable-service-monitoring "Enable AWS monitoring in Dynatrace.").

## View service metrics

You can view the service metrics in your Dynatrace environment either on the **custom device overview page** or on your **Dashboards** page.

### View metrics on the custom device overview page

To access the custom device overview page

1. Go to ![Technologies](https://dt-cdn.net/images/technologies-512-977161d83c.png "Technologies") **Technologies & Processes Classic**.
2. Filter by service name and select the relevant custom device group.
3. Once you select the custom device group, you're on the **custom device group overview page**.
4. The **custom device group overview page** lists all instances (custom devices) belonging to the group. Select an instance to view the **custom device overview page**.

### View metrics on your dashboard

You can also view metrics in the Dynatrace web UI on dashboards. There is no preset dashboard available for this service, but you can [create your own dashboard](/docs/analyze-explore-automate/dashboards-classic/dashboards/create-dashboards "Learn how to create and edit Dynatrace dashboards.").

To check the availability of preset dashboards for each AWS service, see the list below.

### Preset dashboard availability list

| AWS service | Preset dashboard |
| --- | --- |
| Amazon EC2 Auto Scaling (built-in) | Not applicable |
| AWS Lambda (built-in) | Not applicable |
| Amazon Application and Network Load Balancer (built-in) | Not applicable |
| Amazon DynamoDB (built-in) | Not applicable |
| Amazon EBS (built-in) | Not applicable |
| Amazon EC2 (built-in) | Not applicable |
| Amazon Elastic Load Balancer (ELB) (built-in) | Not applicable |
| Amazon RDS (built-in) | Not applicable |
| Amazon S3 (built-in) | Not applicable |
| AWS Certificate Manager Private Certificate Authority | Not applicable |
| All monitored Amazon services | Not applicable |
| Amazon API Gateway | Not applicable |
| AWS App Runner | Not applicable |
| Amazon AppStream | Applicable |
| AWS AppSync | Applicable |
| Amazon Athena | Applicable |
| Amazon Aurora | Not applicable |
| Amazon EC2 Auto Scaling | Applicable |
| AWS Billing | Applicable |
| Amazon Keyspaces | Applicable |
| AWS Chatbot | Applicable |
| Amazon CloudFront | Not applicable |
| AWS CloudHSM | Applicable |
| Amazon CloudSearch | Applicable |
| AWS CodeBuild | Applicable |
| Amazon Cognito | Not applicable |
| Amazon Connect | Applicable |
| AWS DataSync | Applicable |
| Amazon DynamoDB Accelerator (DAX) | Applicable |
| AWS Database Migration Service (AWS DMS) | Applicable |
| Amazon DocumentDB | Applicable |
| AWS Direct Connect | Applicable |
| Amazon DynamoDB | Not applicable |
| Amazon EBS | Not applicable |
| Amazon EC2 Spot Fleet | Not applicable |
| Amazon EC2 API | Applicable |
| Amazon Elastic Container Service (ECS) | Not applicable |
| Amazon ECS Container Insights | Applicable |
| Amazon Elastic File System (EFS) | Not applicable |
| Amazon Elastic Kubernetes Service (EKS) | Applicable |
| Amazon ElastiCache (EC) | Not applicable |
| AWS Elastic Beanstalk | Applicable |
| Amazon Elastic Inference | Applicable |
| Amazon Elastic Transcoder | Applicable |
| Amazon Elastic Map Reduce (EMR) | Not applicable |
| Amazon Elasticsearch Service (ES) | Not applicable |
| Amazon EventBridge | Applicable |
| Amazon FSx | Applicable |
| Amazon GameLift | Applicable |
| AWS Glue | Not applicable |
| Amazon Inspector | Applicable |
| AWS Internet of Things (IoT) | Not applicable |
| AWS IoT Things Graph | Applicable |
| AWS IoT Analytics | Applicable |
| Amazon Managed Streaming for Kafka | Applicable |
| Amazon Kinesis Data Analytics | Not applicable |
| Amazon Data Firehose | Not applicable |
| Amazon Kinesis Data Streams | Not applicable |
| Amazon Kinesis Video Streams | Not applicable |
| AWS Lambda | Not applicable |
| Amazon Lex | Applicable |
| Amazon CloudWatch Logs | Applicable |
| AWS Elemental MediaTailor | Applicable |
| AWS Elemental MediaConnect | Applicable |
| AWS Elemental MediaConvert | Applicable |
| AWS Elemental MediaPackage Live | Applicable |
| AWS Elemental MediaPackage Video on Demand | Applicable |
| Amazon MQ | Applicable |
| Amazon VPC NAT Gateways | Not applicable |
| Amazon Neptune | Applicable |
| AWS OpsWorks | Applicable |
| Amazon Polly | Applicable |
| Amazon QLDB | Applicable |
| Amazon RDS | Not applicable |
| Amazon Redshift | Not applicable |
| Amazon Rekognition | Applicable |
| AWS RoboMaker | Applicable |
| Amazon Route 53 | Applicable |
| Amazon Route 53 Resolver | Applicable |
| Amazon S3 | Not applicable |
| Amazon SageMaker Batch Transform Jobs | Not applicable |
| Amazon SageMaker Endpoints | Not applicable |
| Amazon SageMaker Endpoint Instances | Not applicable |
| Amazon SageMaker Ground Truth | Not applicable |
| Amazon SageMaker Processing Jobs | Not applicable |
| Amazon SageMaker Training Jobs | Not applicable |
| AWS Service Catalog | Applicable |
| Amazon Simple Email Service (SES) | Not applicable |
| Amazon Simple Notification Service (SNS) | Not applicable |
| Amazon Simple Queue Service (SQS) | Not applicable |
| AWS Systems Manager - Run Command | Applicable |
| AWS Step Functions | Applicable |
| AWS Storage Gateway | Applicable |
| Amazon SWF | Applicable |
| Amazon Textract | Applicable |
| AWS Transfer Family | Applicable |
| AWS Transit Gateway | Applicable |
| Amazon Translate | Applicable |
| AWS Trusted Advisor | Applicable |
| AWS API Usage | Applicable |
| AWS Site-to-Site VPN | Applicable |
| AWS WAF Classic | Applicable |
| AWS WAF | Applicable |
| Amazon WorkMail | Applicable |
| Amazon WorkSpaces | Applicable |

## Available metrics

This service monitors a part of Amazon RDS (AWS/RDS). While you have this service configured, you can't have Amazon RDS (built-in) service turned on.

`DBInstanceIdentifier` is the main dimension.

| Name | Description | Dimensions | Unit | Recommended |
| --- | --- | --- | --- | --- |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | Region, DBClusterIdentifier, Role | Count |  |
| SumBinaryLogSize |  | Region, DatabaseClass | Count |  |
| SumBinaryLogSize |  | Region, DBClusterIdentifier | Count |  |
| SumBinaryLogSize |  | Region | Count |  |
| SumBinaryLogSize |  | Region, EngineName | Count |  |
| SumBinaryLogSize |  | Region, DBClusterIdentifier, Role | Count |  |
| DeleteThroughput |  | DBInstanceIdentifier | Count/Second |  |
| Deadlocks |  | Region, DatabaseClass | Count/Second |  |
| Deadlocks |  | Region, DBClusterIdentifier | Count/Second |  |
| Deadlocks |  | Region | Count/Second |  |
| Deadlocks |  | Region, EngineName | Count/Second |  |
| Deadlocks |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | Region, DBClusterIdentifier, Role | Count |  |
| TotalBackupStorageBilled |  | Region, DBClusterIdentifier | Bytes |  |
| TotalBackupStorageBilled |  | Region, EngineName | Bytes |  |
| DeleteLatency |  | Region, DatabaseClass | Milliseconds |  |
| DeleteLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| DeleteLatency |  | Region | Milliseconds |  |
| DeleteLatency |  | Region, EngineName | Milliseconds |  |
| DeleteLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | DBInstanceIdentifier | Count |  |
| DDLLatency |  | Region, DatabaseClass | Milliseconds |  |
| DDLLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| DDLLatency |  | Region | Milliseconds |  |
| DDLLatency |  | Region, EngineName | Milliseconds |  |
| DDLLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| DMLLatency |  | Region, DatabaseClass | Milliseconds |  |
| DMLLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| DMLLatency |  | Region | Milliseconds |  |
| DMLLatency |  | Region, EngineName | Milliseconds |  |
| DMLLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| DDLThroughput |  | Region, DatabaseClass | Count/Second |  |
| DDLThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| DDLThroughput |  | Region | Count/Second |  |
| DDLThroughput |  | Region, EngineName | Count/Second |  |
| DDLThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| CommitThroughput |  | Region, DatabaseClass | Count/Second |  |
| CommitThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| CommitThroughput |  | Region | Count/Second |  |
| CommitThroughput |  | Region, EngineName | Count/Second |  |
| CommitThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| ForwardingReplicaReadWaitLatency |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | Region, DBClusterIdentifier, Role | Count |  |
| BlockedTransactions |  | Region, DatabaseClass | Count/Second |  |
| BlockedTransactions |  | Region, DBClusterIdentifier | Count/Second |  |
| BlockedTransactions |  | Region | Count/Second |  |
| BlockedTransactions |  | Region, EngineName | Count/Second |  |
| BlockedTransactions |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| EBSIOBalance% | The percentage of I/O credits remaining in the burst bucket of your RDS database. This metric is available for basic | Region, DatabaseClass | Percent |  |
| EBSIOBalance% |  | Region, DBClusterIdentifier | Percent |  |
| EBSIOBalance% |  | Region | Percent |  |
| EBSIOBalance% |  | Region, EngineName | Percent | Applicable |
| EBSIOBalance% |  | Region, DBClusterIdentifier, Role | Percent |  |
| SwapUsage | The amount of swap space used on the DB instance. | Region, DatabaseClass | Bytes |  |
| SwapUsage |  | Region, DBClusterIdentifier | Bytes |  |
| SwapUsage |  | Region | Bytes |  |
| SwapUsage |  | Region, EngineName | Bytes |  |
| SwapUsage |  | Region, DBClusterIdentifier, Role | Bytes |  |
| ForwardingReplicaDMLThroughput |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_attempted |  | DBInstanceIdentifier | Count |  |
| LoginFailures |  | Region, DatabaseClass | Count/Second |  |
| LoginFailures |  | Region, DBClusterIdentifier | Count/Second |  |
| LoginFailures |  | Region | Count/Second |  |
| LoginFailures |  | Region, EngineName | Count/Second |  |
| LoginFailures |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| NetworkTransmitThroughput | The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Amazon RDS | Region, DatabaseClass | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region, EngineName | Bytes/Second |  |
| NetworkTransmitThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| NumBinaryLogFiles |  | Region, DatabaseClass | Count |  |
| NumBinaryLogFiles |  | Region, DBClusterIdentifier | Count |  |
| NumBinaryLogFiles |  | Region | Count |  |
| NumBinaryLogFiles |  | Region, EngineName | Count |  |
| NumBinaryLogFiles |  | Region, DBClusterIdentifier, Role | Count |  |
| DBLoadCPU |  | DBInstanceIdentifier | None |  |
| Aurora\_pq\_request\_failed |  | DBInstanceIdentifier | Count |  |
| BlockedTransactions |  | DBInstanceIdentifier | Count/Second |  |
| ForwardingReplicaReadWaitThroughput |  | DBInstanceIdentifier | Count |  |
| ReadThroughput | The average number of bytes read from disk per second. | Region, DatabaseClass | Bytes/Second |  |
| ReadThroughput |  | Region | Bytes/Second |  |
| ReadThroughput |  | Region, EngineName | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | Region, DBClusterIdentifier, Role | Count |  |
| DeleteThroughput |  | Region, DatabaseClass | Count/Second |  |
| DeleteThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| DeleteThroughput |  | Region | Count/Second |  |
| DeleteThroughput |  | Region, EngineName | Count/Second |  |
| DeleteThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| DBLoadCPU |  | Region | None |  |
| CommitLatency |  | Region, DatabaseClass | Milliseconds |  |
| CommitLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| CommitLatency |  | Region | Milliseconds |  |
| CommitLatency |  | Region, EngineName | Milliseconds |  |
| CommitLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| ForwardingReplicaOpenSessions |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaOpenSessions |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaOpenSessions |  | Region | Count |  |
| ForwardingReplicaOpenSessions |  | Region, EngineName | Count |  |
| ForwardingReplicaOpenSessions |  | Region, DBClusterIdentifier, Role | Count |  |
| BackupRetentionPeriodStorageUsed |  | Region, DBClusterIdentifier | Bytes |  |
| BackupRetentionPeriodStorageUsed |  | Region, EngineName | Bytes |  |
| InsertLatency |  | Region, DatabaseClass | Milliseconds |  |
| InsertLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| InsertLatency |  | Region | Milliseconds |  |
| InsertLatency |  | Region, EngineName | Milliseconds |  |
| InsertLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| DMLThroughput |  | Region, DatabaseClass | Count/Second |  |
| DMLThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| DMLThroughput |  | Region | Count/Second |  |
| DMLThroughput |  | Region, EngineName | Count/Second |  |
| DMLThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| Aurora\_pq\_request\_attempted |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_attempted |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_attempted |  | Region | Count |  |
| Aurora\_pq\_request\_attempted |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_attempted |  | Region, DBClusterIdentifier, Role | Count |  |
| DiskQueueDepth | The number of outstanding I/Os (read/write requests) waiting to access the disk. | Region, DatabaseClass | Count |  |
| DiskQueueDepth |  | Region | Count |  |
| DiskQueueDepth |  | Region, EngineName | Count | Applicable |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | Region, DBClusterIdentifier, Role | Count |  |
| BinLogDiskUsage | The amount of disk space occupied by binary logs. If automatic backups are enabled for MySQL and MariaDB instances, | Region, DatabaseClass | Bytes |  |
| BinLogDiskUsage |  | Region | Bytes |  |
| BinLogDiskUsage |  | Region, EngineName | Bytes | Applicable |
| BinLogDiskUsage |  | Region, EngineName | Bytes |  |
| ForwardingWriterDMLThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingWriterDMLThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingWriterDMLThroughput |  | Region | Count |  |
| ForwardingWriterDMLThroughput |  | Region, EngineName | Count |  |
| ForwardingWriterDMLThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| Queries |  | DBInstanceIdentifier | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, DatabaseClass | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, DBClusterIdentifier | Count |  |
| AuroraSlowConnectionHandleCount |  | Region | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, EngineName | Count |  |
| AuroraSlowConnectionHandleCount |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | Region, DBClusterIdentifier, Role | Count |  |
| CommitThroughput |  | DBInstanceIdentifier | Count/Second |  |
| RollbackSegmentHistoryListLength |  | Region, DatabaseClass | Count |  |
| RollbackSegmentHistoryListLength |  | Region, DBClusterIdentifier | Count |  |
| RollbackSegmentHistoryListLength |  | Region | Count |  |
| RollbackSegmentHistoryListLength |  | Region, EngineName | Count |  |
| RollbackSegmentHistoryListLength |  | Region, DBClusterIdentifier, Role | Count |  |
| SelectLatency |  | Region, DatabaseClass | Milliseconds |  |
| SelectLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| SelectLatency |  | Region | Milliseconds |  |
| SelectLatency |  | Region, EngineName | Milliseconds |  |
| SelectLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| ForwardingReplicaDMLLatency |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaDMLLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaDMLLatency |  | Region | Count |  |
| ForwardingReplicaDMLLatency |  | Region, EngineName | Count |  |
| ForwardingReplicaDMLLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| StorageNetworkThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | DBInstanceIdentifier | Count |  |
| DatabaseConnections | The number of client network connections to the database instance. | Region, DatabaseClass | Count |  |
| DatabaseConnections |  | Region, DBClusterIdentifier | Count |  |
| DatabaseConnections |  | Region | Count |  |
| DatabaseConnections |  | Region, EngineName | Count | Applicable |
| DatabaseConnections |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_custom\_charset |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | Region, DBClusterIdentifier, Role | Count |  |
| EngineUptime |  | Region, DatabaseClass | Seconds |  |
| EngineUptime |  | Region, DBClusterIdentifier | Seconds |  |
| EngineUptime |  | Region | Seconds |  |
| EngineUptime |  | Region, EngineName | Seconds |  |
| EngineUptime |  | Region, DBClusterIdentifier, Role | Seconds |  |
| FreeStorageSpace | The amount of available storage space. | Region, DatabaseClass | Bytes |  |
| FreeStorageSpace |  | Region | Bytes |  |
| FreeStorageSpace |  | Region, EngineName | Bytes | Applicable |
| FreeStorageSpace |  | Region, EngineName | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraVolumeBytesLeftTotal |  | DBInstanceIdentifier | Count |  |
| AbortedClients |  | Region, DatabaseClass | Count |  |
| AbortedClients |  | Region, DBClusterIdentifier | Count |  |
| AbortedClients |  | Region | Count |  |
| AbortedClients |  | Region, EngineName | Count |  |
| AbortedClients |  | Region, DBClusterIdentifier, Role | Count |  |
| BufferCacheHitRatio |  | Region, DatabaseClass | Percent |  |
| BufferCacheHitRatio |  | Region, DBClusterIdentifier | Percent |  |
| BufferCacheHitRatio |  | Region | Percent |  |
| BufferCacheHitRatio |  | Region, EngineName | Percent |  |
| BufferCacheHitRatio |  | Region, DBClusterIdentifier, Role | Percent |  |
| FreeLocalStorage |  | DBInstanceIdentifier | Bytes |  |
| AuroraSlowHandshakeCount |  | Region, DatabaseClass | Count |  |
| AuroraSlowHandshakeCount |  | Region, DBClusterIdentifier | Count |  |
| AuroraSlowHandshakeCount |  | Region | Count |  |
| AuroraSlowHandshakeCount |  | Region, EngineName | Count |  |
| AuroraSlowHandshakeCount |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingWriterDMLLatency |  | DBInstanceIdentifier | Count |  |
| Queries |  | Region, DatabaseClass | Count/Second |  |
| Queries |  | Region, DBClusterIdentifier | Count/Second |  |
| Queries |  | Region | Count/Second |  |
| Queries |  | Region, EngineName | Count/Second |  |
| Queries |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| EBSByteBalance% | The percentage of throughput credits remaining in the burst bucket of your RDS database. This metric is available | Region, DatabaseClass | Percent |  |
| EBSByteBalance% |  | Region, DBClusterIdentifier | Percent |  |
| EBSByteBalance% |  | Region | Percent |  |
| EBSByteBalance% |  | Region, EngineName | Percent | Applicable |
| EBSByteBalance% |  | Region, DBClusterIdentifier, Role | Percent |  |
| ActiveTransactions |  | Region, DatabaseClass | Count/Second |  |
| ActiveTransactions |  | Region, DBClusterIdentifier | Count/Second |  |
| ActiveTransactions |  | Region | Count/Second |  |
| ActiveTransactions |  | Region, EngineName | Count/Second |  |
| ActiveTransactions |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| InsertThroughput |  | Region, DatabaseClass | Count/Second |  |
| InsertThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| InsertThroughput |  | Region | Count/Second |  |
| InsertThroughput |  | Region, EngineName | Count/Second |  |
| InsertThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| ForwardingWriterOpenSessions |  | Region, DatabaseClass | Count |  |
| ForwardingWriterOpenSessions |  | Region, DBClusterIdentifier | Count |  |
| ForwardingWriterOpenSessions |  | Region | Count |  |
| ForwardingWriterOpenSessions |  | Region, EngineName | Count |  |
| ForwardingWriterOpenSessions |  | Region, DBClusterIdentifier, Role | Count |  |
| SwapUsage | The amount of swap space used on the DB instance. | DBInstanceIdentifier | Bytes |  |
| VolumeReadIOPs |  | Region, DbClusterIdentifier, EngineName | Count |  |
| VolumeReadIOPs |  | Region, DBClusterIdentifier | Count |  |
| VolumeReadIOPs |  | Region, EngineName | Count |  |
| ForwardingWriterDMLThroughput |  | DBInstanceIdentifier | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, DatabaseClass | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, DBClusterIdentifier | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, EngineName | Count |  |
| AuroraVolumeBytesLeftTotal |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | Region, DBClusterIdentifier, Role | Count |  |
| VolumeBytesUsed |  | Region, DbClusterIdentifier, EngineName | Bytes |  |
| VolumeBytesUsed |  | Region, DBClusterIdentifier | Bytes |  |
| VolumeBytesUsed |  | Region, EngineName | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | DBInstanceIdentifier | Count |  |
| UpdateLatency |  | Region, DatabaseClass | Milliseconds |  |
| UpdateLatency |  | Region, DBClusterIdentifier | Milliseconds |  |
| UpdateLatency |  | Region | Milliseconds |  |
| UpdateLatency |  | Region, EngineName | Milliseconds |  |
| UpdateLatency |  | Region, DBClusterIdentifier, Role | Milliseconds |  |
| UpdateThroughput |  | Region, DatabaseClass | Count/Second |  |
| UpdateThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| UpdateThroughput |  | Region | Count/Second |  |
| UpdateThroughput |  | Region, EngineName | Count/Second |  |
| UpdateThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| CPUUtilization | The percentage of CPU utilization. | Region, DatabaseClass | Percent |  |
| CPUUtilization |  | Region, DBClusterIdentifier | Percent |  |
| CPUUtilization |  | Region | Percent |  |
| CPUUtilization |  | Region, EngineName | Percent | Applicable |
| CPUUtilization |  | Region, DBClusterIdentifier, Role | Percent |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_in\_progress |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaDMLThroughput |  | Region | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, EngineName | Count |  |
| ForwardingReplicaDMLThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| LVMWriteIOPS |  | Region, DatabaseClass | Count/Second |  |
| LVMWriteIOPS |  | Region | Count/Second |  |
| LVMWriteIOPS |  | Region, EngineName | Count/Second | Applicable |
| ForwardingReplicaSelectThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaSelectThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaSelectThroughput |  | Region | Count |  |
| ForwardingReplicaSelectThroughput |  | Region, EngineName | Count |  |
| ForwardingReplicaSelectThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_failed |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_failed |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_failed |  | Region | Count |  |
| Aurora\_pq\_request\_failed |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_failed |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_range\_scan |  | Region, DBClusterIdentifier, Role | Count |  |
| EngineUptime |  | DBInstanceIdentifier | Seconds |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_few\_pages\_outside\_buffer\_pool |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen |  | Region, DBClusterIdentifier, Role | Count |  |
| ConnectionAttempts | The number of attempts to connect to an instance, whether successful or not. | Region, DatabaseClass | Count |  |
| ConnectionAttempts |  | Region, DBClusterIdentifier | Count |  |
| ConnectionAttempts |  | Region | Count |  |
| ConnectionAttempts |  | Region, EngineName | Count |  |
| ConnectionAttempts |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingWriterOpenSessions |  | DBInstanceIdentifier | Count |  |
| NetworkThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| NetworkThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| NetworkThroughput |  | Region | Bytes/Second |  |
| NetworkThroughput |  | Region, EngineName | Bytes/Second |  |
| NetworkThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| RollbackSegmentHistoryListLength |  | DBInstanceIdentifier | Count |  |
| SnapshotStorageUsed |  | Region, DBClusterIdentifier | Bytes |  |
| SnapshotStorageUsed |  | Region, EngineName | Bytes |  |
| AuroraBinlogReplicaLag |  | Region, DatabaseClass | Seconds |  |
| AuroraBinlogReplicaLag |  | Region, DBClusterIdentifier | Seconds |  |
| AuroraBinlogReplicaLag |  | Region | Seconds |  |
| AuroraBinlogReplicaLag |  | Region, EngineName | Seconds |  |
| AuroraBinlogReplicaLag |  | Region, DBClusterIdentifier, Role | Seconds |  |
| ForwardingReplicaSelectLatency |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaSelectLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaSelectLatency |  | Region | Count |  |
| ForwardingReplicaSelectLatency |  | Region, EngineName | Count |  |
| ForwardingReplicaSelectLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| LVMReadIOPS |  | Region, DatabaseClass | Count/Second |  |
| LVMReadIOPS |  | Region | Count/Second |  |
| LVMReadIOPS |  | Region, EngineName | Count/Second | Applicable |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | DBInstanceIdentifier | Count |  |
| FreeLocalStorage |  | Region, DatabaseClass | Bytes |  |
| FreeLocalStorage |  | Region, DBClusterIdentifier | Bytes |  |
| FreeLocalStorage |  | Region | Bytes |  |
| FreeLocalStorage |  | Region, EngineName | Bytes |  |
| FreeLocalStorage |  | Region, DBClusterIdentifier, Role | Bytes |  |
| StorageNetworkReceiveThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region, EngineName | Bytes/Second |  |
| StorageNetworkReceiveThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| Aurora\_pq\_request\_executed |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_executed |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_executed |  | Region | Count |  |
| Aurora\_pq\_request\_executed |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_executed |  | Region, DBClusterIdentifier, Role | Count |  |
| ReadLatency | The average amount of time taken per disk I/O operation. | Region, DatabaseClass | Seconds |  |
| ReadLatency |  | Region, DBClusterIdentifier | Seconds |  |
| ReadLatency |  | Region | Seconds |  |
| ReadLatency |  | Region, EngineName | Seconds |  |
| ReadLatency |  | Region, DBClusterIdentifier, Role | Seconds |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | Region, DBClusterIdentifier, Role | Count |  |
| FreeableMemory | The amount of available random access memory. | DBInstanceIdentifier | Bytes | Applicable |
| FreeableMemory |  | DBInstanceIdentifier | Bytes |  |
| FreeableMemory |  | DBInstanceIdentifier | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraSlowConnectionHandleCount |  | DBInstanceIdentifier | Count |  |
| StorageNetworkThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| StorageNetworkThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| StorageNetworkThroughput |  | Region | Bytes/Second |  |
| StorageNetworkThroughput |  | Region, EngineName | Bytes/Second |  |
| StorageNetworkThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| ActiveTransactions |  | DBInstanceIdentifier | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | Region, DBClusterIdentifier, Role | Count |  |
| LoginFailures |  | DBInstanceIdentifier | Count/Second |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region, EngineName | Count |  |
| ForwardingReplicaReadWaitThroughput |  | Region, DBClusterIdentifier, Role | Count |  |
| SelectLatency |  | DBInstanceIdentifier | Milliseconds |  |
| VolumeWriteIOPs |  | Region, DbClusterIdentifier, EngineName | Count |  |
| VolumeWriteIOPs |  | Region, DBClusterIdentifier | Count |  |
| VolumeWriteIOPs |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraBinlogReplicaLag |  | DBInstanceIdentifier | Seconds |  |
| RowLockTime |  | Region, DatabaseClass | Count |  |
| RowLockTime |  | Region, DBClusterIdentifier | Count |  |
| RowLockTime |  | Region | Count |  |
| RowLockTime |  | Region, EngineName | Count |  |
| RowLockTime |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_column\_bit |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_high\_buffer\_pool\_pct |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingWriterDMLLatency |  | Region, DatabaseClass | Count |  |
| ForwardingWriterDMLLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingWriterDMLLatency |  | Region | Count |  |
| ForwardingWriterDMLLatency |  | Region, EngineName | Count |  |
| ForwardingWriterDMLLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_index\_hint |  | Region, DBClusterIdentifier, Role | Count |  |
| CommitLatency |  | DBInstanceIdentifier | Milliseconds |  |
| ForwardingReplicaSelectLatency |  | DBInstanceIdentifier | Count |  |
| ReadIOPS | The average number of disk read I/O operations per second. | Region, DatabaseClass | Count/Second |  |
| ReadIOPS |  | Region | Count/Second |  |
| ReadIOPS |  | Region, EngineName | Count/Second |  |
| StorageNetworkTransmitThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_innodb\_table\_format |  | DBInstanceIdentifier | Count |  |
| WriteLatency | The average amount of time taken per disk I/O operation. | Region, DatabaseClass | Seconds |  |
| WriteLatency |  | Region, DBClusterIdentifier | Seconds |  |
| WriteLatency |  | Region | Seconds |  |
| WriteLatency |  | Region, EngineName | Seconds |  |
| WriteLatency |  | Region, DBClusterIdentifier, Role | Seconds |  |
| SelectThroughput |  | Region, DatabaseClass | Count/Second |  |
| SelectThroughput |  | Region, DBClusterIdentifier | Count/Second |  |
| SelectThroughput |  | Region | Count/Second |  |
| SelectThroughput |  | Region, EngineName | Count/Second |  |
| SelectThroughput |  | Region, DBClusterIdentifier, Role | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen |  | DBInstanceIdentifier | Count |  |
| FreeableMemory | The amount of available random access memory. | Region, DatabaseClass | Bytes |  |
| FreeableMemory |  | Region, DBClusterIdentifier | Bytes |  |
| FreeableMemory |  | Region | Bytes |  |
| FreeableMemory |  | Region, EngineName | Bytes | Applicable |
| FreeableMemory |  | Region, DBClusterIdentifier, Role | Bytes |  |
| FreeableMemory |  | Region, EngineName | Bytes |  |
| ReadLatency | The average amount of time taken per disk I/O operation. | DBInstanceIdentifier | Seconds | Applicable |
| DMLLatency |  | DBInstanceIdentifier | Milliseconds |  |
| NetworkReceiveThroughput | The incoming (receive) network traffic on the DB instance, including both customer database traffic and Amazon RDS | DBInstanceIdentifier | Bytes/Second | Applicable |
| Aurora\_pq\_request\_not\_chosen\_unsupported\_access |  | DBInstanceIdentifier | Count |  |
| UpdateLatency |  | DBInstanceIdentifier | Milliseconds |  |
| DBLoad |  | DBInstanceIdentifier | None |  |
| Aurora\_pq\_request\_not\_chosen\_row\_length\_too\_long |  | DBInstanceIdentifier | Count |  |
| BinLogDiskUsage | The amount of disk space occupied by binary logs. If automatic backups are enabled for MySQL and MariaDB instances, | DBInstanceIdentifier | Bytes | Applicable |
| BinLogDiskUsage |  | DBInstanceIdentifier | Bytes |  |
| Aurora\_pq\_request\_not\_chosen\_no\_where\_clause |  | DBInstanceIdentifier | Count |  |
| DDLLatency |  | DBInstanceIdentifier | Milliseconds |  |
| SumBinaryLogSize |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_below\_min\_rows |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_in\_progress |  | DBInstanceIdentifier | Count |  |
| DatabaseConnections | The number of client network connections to the database instance. | DBInstanceIdentifier | Count | Applicable |
| CPUUtilization | The percentage of CPU utilization. | DBInstanceIdentifier | Percent | Applicable |
| ForwardingReplicaReadWaitLatency |  | Region, DatabaseClass | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region, DBClusterIdentifier | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region, EngineName | Count |  |
| ForwardingReplicaReadWaitLatency |  | Region, DBClusterIdentifier, Role | Count |  |
| AbortedClients |  | DBInstanceIdentifier | Count |  |
| ReadThroughput | The average number of bytes read from disk per second. | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_virtual |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_throttled |  | Region | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_throttled |  | Region, DBClusterIdentifier, Role | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, DatabaseClass | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, DBClusterIdentifier | Count |  |
| AuroraDMLRejectedWriterFull |  | Region | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, EngineName | Count |  |
| AuroraDMLRejectedWriterFull |  | Region, DBClusterIdentifier, Role | Count |  |
| ForwardingReplicaDMLLatency |  | DBInstanceIdentifier | Count |  |
| WriteThroughput | The average number of bytes written to disk per second. | DBInstanceIdentifier | Bytes/Second |  |
| DiskQueueDepth | The number of outstanding I/Os (read/write requests) waiting to access the disk. | DBInstanceIdentifier | Count | Applicable |
| Aurora\_pq\_request\_not\_chosen\_full\_text\_index |  | DBInstanceIdentifier | Count |  |
| ForwardingReplicaOpenSessions |  | DBInstanceIdentifier | Count |  |
| StorageNetworkTransmitThroughput |  | Region, DatabaseClass | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region, EngineName | Bytes/Second |  |
| StorageNetworkTransmitThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_long\_trx |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_temporary\_table |  | DBInstanceIdentifier | Count |  |
| RowLockTime |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_tx\_isolation |  | DBInstanceIdentifier | Count |  |
| NetworkReceiveThroughput | The incoming (receive) network traffic on the DB instance, including both customer database traffic and Amazon RDS | Region, DatabaseClass | Bytes/Second |  |
| NetworkReceiveThroughput |  | Region, DBClusterIdentifier | Bytes/Second |  |
| NetworkReceiveThroughput |  | Region | Bytes/Second |  |
| NetworkReceiveThroughput |  | Region, EngineName | Bytes/Second | Applicable |
| NetworkReceiveThroughput |  | Region, DBClusterIdentifier, Role | Bytes/Second |  |
| Aurora\_pq\_request\_not\_chosen\_small\_table |  | DBInstanceIdentifier | Count |  |
| DBLoadNonCPU |  | DBInstanceIdentifier | None |  |
| WriteIOPS | The average number of disk write I/O operations per second. | Region, DatabaseClass | Count/Second |  |
| WriteIOPS |  | Region | Count/Second |  |
| WriteIOPS |  | Region, EngineName | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_lob |  | DBInstanceIdentifier | Count |  |
| BurstBalance | The percent of General Purpose SSD (gp2) burst-bucket I/O credits available. | DBInstanceIdentifier | Percent | Applicable |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DatabaseClass | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DBClusterIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, EngineName | Count |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | Region, DBClusterIdentifier, Role | Count |  |
| DMLThroughput |  | DBInstanceIdentifier | Count/Second |  |
| WriteIOPS | The average number of disk write I/O operations per second. | DBInstanceIdentifier | Count/Second |  |
| WriteThroughput | The average number of bytes written to disk per second. | Region, DatabaseClass | Bytes/Second |  |
| WriteThroughput |  | Region | Bytes/Second |  |
| WriteThroughput |  | Region, EngineName | Bytes/Second |  |
| BufferCacheHitRatio |  | DBInstanceIdentifier | Percent |  |
| ConnectionAttempts | The number of attempts to connect to an instance, whether successful or not. | DBInstanceIdentifier | Count |  |
| NetworkTransmitThroughput | The outgoing (transmit) network traffic on the DB instance, including both customer database traffic and Amazon RDS | DBInstanceIdentifier | Bytes/Second |  |
| Aurora\_pq\_request\_executed |  | DBInstanceIdentifier | Count |  |
| UpdateThroughput |  | DBInstanceIdentifier | Count/Second |  |
| ForwardingReplicaSelectThroughput |  | DBInstanceIdentifier | Count |  |
| StorageNetworkReceiveThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| DeleteLatency |  | DBInstanceIdentifier | Milliseconds |  |
| DDLThroughput |  | DBInstanceIdentifier | Count/Second |  |
| ReadIOPS | The average number of disk read I/O operations per second. | DBInstanceIdentifier | Count/Second |  |
| EBSByteBalance% | The percentage of throughput credits remaining in the burst bucket of your RDS database. This metric is available | DBInstanceIdentifier | Percent | Applicable |
| NetworkThroughput |  | DBInstanceIdentifier | Bytes/Second |  |
| DBLoad |  | Region | None |  |
| Deadlocks |  | DBInstanceIdentifier | Count/Second |  |
| AuroraSlowHandshakeCount |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_throttled |  | DBInstanceIdentifier | Count |  |
| LVMReadIOPS |  | DBInstanceIdentifier | Count/Second | Applicable |
| NumBinaryLogFiles |  | DBInstanceIdentifier | Count |  |
| EBSIOBalance% | The percentage of I/O credits remaining in the burst bucket of your RDS database. This metric is available for basic | DBInstanceIdentifier | Percent | Applicable |
| BurstBalance | The percent of General Purpose SSD (gp2) burst-bucket I/O credits available. | Region, DatabaseClass | Percent |  |
| BurstBalance |  | Region | Percent |  |
| BurstBalance |  | Region, EngineName | Percent | Applicable |
| FreeStorageSpace | The amount of available storage space. | DBInstanceIdentifier | Bytes | Applicable |
| FreeStorageSpace |  | DBInstanceIdentifier | Bytes |  |
| FreeStorageSpace |  | DBInstanceIdentifier | Bytes |  |
| DBLoadNonCPU |  | Region | None |  |
| AuroraDMLRejectedWriterFull |  | DBInstanceIdentifier | Count |  |
| InsertLatency |  | DBInstanceIdentifier | Milliseconds |  |
| Aurora\_pq\_request\_not\_chosen\_instant\_ddl |  | DBInstanceIdentifier | Count |  |
| Aurora\_pq\_request\_not\_chosen\_update\_delete\_stmts |  | DBInstanceIdentifier | Count |  |
| SelectThroughput |  | DBInstanceIdentifier | Count/Second |  |
| InsertThroughput |  | DBInstanceIdentifier | Count/Second |  |
| Aurora\_pq\_request\_not\_chosen\_column\_geometry |  | DBInstanceIdentifier | Count |  |
| WriteLatency | The average amount of time taken per disk I/O operation. | DBInstanceIdentifier | Seconds | Applicable |
| LVMWriteIOPS |  | DBInstanceIdentifier | Count/Second | Applicable |