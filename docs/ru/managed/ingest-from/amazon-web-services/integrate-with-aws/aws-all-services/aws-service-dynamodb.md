---
title: Amazon DynamoDB Accelerator (DAX) monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-dynamodb
scraped: 2026-02-26T21:24:43.330923
---

# Amazon DynamoDB Accelerator (DAX) monitoring

# Amazon DynamoDB Accelerator (DAX) monitoring

* How-to guide
* 12-min read
* Published Jul 06, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon DynamoDB Accelerator (DAX). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

To enable monitoring for this service, you need:

* Any version of ActiveGate in both Dynatrace SaaS and Managed deployments.

  For role-based access (whether in a [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") or [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) deployment), you need an ActiveGate installed on an Amazon EC2 host.
* An updated [AWS monitoring policy](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#aws-policy-and-authentication "Integrate metrics from Amazon CloudWatch.") to include the additional AWS services.  
  To [update the AWS IAM policyï»¿](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), use the JSON below, containing the monitoring policy (permissions) for all cloud services.

JSON predefined policy for all cloud services

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

If you don't want to add permissions to all services, and just select permissions for certain services, consult the table below. The table contains a set of permissions that are required for [All AWS cloud services](/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services "Monitor all AWS cloud services with Dynatrace and view available metrics.") and, for each cloud service, a list of optional permissions specific to that service.

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
* To disable monitoring of built-in services, you need Environment ActiveGate version 1.245+ and Dynatrace version 1.247+.

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

After you add the service to monitoring, a preset dashboard containing all recommended metrics is automatically listed on your **Dashboards** page. To look for specific dashboards, filter by **Preset** and then by **Name**.

![AWS presets](https://dt-cdn.net/images/image-26-1645-389f58aa89.png)

For existing monitored services, you might need to resave your credentials for the preset dashboard to appear on the **Dashboards** page. To resave your credentials, go to **Settings** > **Cloud and virtualization** > **AWS**, select the desired AWS instance, and then select **Save**.

You can't make changes on a preset dashboard directly, but you can clone and edit it. To clone a dashboard, open the browse menu (**â¦**) and select **Clone**.

To remove a dashboard from the dashboards page, you can hide it. To hide a dashboard, open the browse menu (**â¦**) and select **Hide**.

Hiding a dashboard doesn't affect other users.

![Clone hide AWS](https://dt-cdn.net/images/2020-12-10-15-04-09-1502-b899a29d73.png)

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

![Dynamodb](https://dt-cdn.net/images/dashboard-24-1986-616089414a.png)

## Available metrics

`ClusterId` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| BatchGetItemRequestCount | The number of BatchGetItem requests handled by the node or cluster | Count | Multi | ClusterId |  |
| BatchGetItemRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| BatchGetItemRequestCount |  | Count | Sum | ClusterId | Applicable |
| BatchGetItemRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| BatchGetItemRequestCount |  | Count | Multi | Region |  |
| BatchGetItemRequestCount |  | Count | Sum | Region | Applicable |
| BatchWriteItemRequestCount | The number of BatchWriteItem requests handled by the node or cluster | Count | Multi | ClusterId |  |
| BatchWriteItemRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| BatchWriteItemRequestCount |  | Count | Sum | ClusterId | Applicable |
| BatchWriteItemRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| BatchWriteItemRequestCount |  | Count | Multi | Region |  |
| BatchWriteItemRequestCount |  | Count | Sum | Region | Applicable |
| CPUUtilization | The percentage of CPU utilization of the node or cluster | Percent | Multi | ClusterId | Applicable |
| CPUUtilization |  | Percent | Multi | ClusterId, NodeId | Applicable |
| CPUUtilization |  | Percent | Multi | Region | Applicable |
| ClientConnections | The number of simultaneous connections made by clients to the node or cluster | Count | Multi | ClusterId | Applicable |
| ClientConnections |  | Count | Multi | ClusterId, NodeId | Applicable |
| ClientConnections |  | Count | Sum | ClusterId | Applicable |
| ClientConnections |  | Count | Sum | ClusterId, NodeId | Applicable |
| ClientConnections |  | Count | Multi | Region | Applicable |
| ClientConnections |  | Count | Sum | Region | Applicable |
| DeleteItemRequestCount | The number of DeleteItem requests handled by the node or cluster | Count | Multi | ClusterId |  |
| DeleteItemRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| DeleteItemRequestCount |  | Count | Sum | ClusterId | Applicable |
| DeleteItemRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| DeleteItemRequestCount |  | Count | Multi | Region |  |
| DeleteItemRequestCount |  | Count | Sum | Region | Applicable |
| ErrorRequestCount | Total number of requests that resulted in a user error reported by the node or cluster. Requests that were throttled by the node or cluster are included. | Count | Multi | ClusterId |  |
| ErrorRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| ErrorRequestCount |  | Count | Sum | ClusterId | Applicable |
| ErrorRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| ErrorRequestCount |  | Count | Multi | Region |  |
| ErrorRequestCount |  | Count | Sum | Region | Applicable |
| EstimatedDbSize | An approximation of the amount of data cached in the item cache and the query cache by the node or cluster | Bytes | Multi | ClusterId | Applicable |
| EstimatedDbSize |  | Bytes | Multi | ClusterId, NodeId | Applicable |
| EstimatedDbSize |  | Bytes | Multi | Region | Applicable |
| EvictedSize | The amount of data that was evicted by the node or cluster to make room for newly requested data | Bytes | Multi | ClusterId | Applicable |
| EvictedSize |  | Bytes | Multi | ClusterId, NodeId | Applicable |
| EvictedSize |  | Bytes | Sum | ClusterId | Applicable |
| EvictedSize |  | Bytes | Sum | ClusterId, NodeId | Applicable |
| EvictedSize |  | Bytes | Multi | Region | Applicable |
| EvictedSize |  | Bytes | Sum | Region | Applicable |
| FailedRequestCount | Total number of requests that resulted in an error reported by the node or cluster | Count | Multi | ClusterId |  |
| FailedRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| FailedRequestCount |  | Count | Sum | ClusterId | Applicable |
| FailedRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| FailedRequestCount |  | Count | Multi | Region |  |
| FailedRequestCount |  | Count | Sum | Region | Applicable |
| FaultRequestCount | Total number of requests that resulted in an internal error reported by the node or cluster | Count | Multi | ClusterId |  |
| FaultRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| FaultRequestCount |  | Count | Sum | ClusterId | Applicable |
| FaultRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| FaultRequestCount |  | Count | Multi | Region |  |
| FaultRequestCount |  | Count | Sum | Region | Applicable |
| GetItemRequestCount | The number of GetItem requests handled by the node or cluster | Count | Multi | ClusterId |  |
| GetItemRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| GetItemRequestCount |  | Count | Sum | ClusterId | Applicable |
| GetItemRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| GetItemRequestCount |  | Count | Multi | Region |  |
| GetItemRequestCount |  | Count | Sum | Region | Applicable |
| ItemCacheHits | The number of times an item was returned from the cache by the node or cluster | Count | Multi | ClusterId |  |
| ItemCacheHits |  | Count | Multi | ClusterId, NodeId |  |
| ItemCacheHits |  | Count | Sum | ClusterId | Applicable |
| ItemCacheHits |  | Count | Sum | ClusterId, NodeId | Applicable |
| ItemCacheHits |  | Count | Multi | Region |  |
| ItemCacheHits |  | Count | Sum | Region | Applicable |
| ItemCacheMisses | The number of times an item was not in the node or cluster cache, and had to be retrieved from DynamoDB | Count | Multi | ClusterId |  |
| ItemCacheMisses |  | Count | Multi | ClusterId, NodeId |  |
| ItemCacheMisses |  | Count | Sum | ClusterId | Applicable |
| ItemCacheMisses |  | Count | Sum | ClusterId, NodeId | Applicable |
| ItemCacheMisses |  | Count | Multi | Region |  |
| ItemCacheMisses |  | Count | Sum | Region | Applicable |
| NetworkBytesIn | The number of bytes received on all network interfaces by the node or cluster | Bytes | Multi | ClusterId | Applicable |
| NetworkBytesIn |  | Bytes | Multi | ClusterId, NodeId | Applicable |
| NetworkBytesIn |  | Bytes | Multi | Region | Applicable |
| NetworkBytesOut | The number of bytes sent out on all network interfaces by the node or cluster. This metric identifies the volume of outgoing traffic in terms of the number of bytes on a single node or cluster. | Bytes | Multi | ClusterId | Applicable |
| NetworkBytesOut |  | Bytes | Multi | ClusterId, NodeId | Applicable |
| NetworkBytesOut |  | Bytes | Multi | Region | Applicable |
| NetworkPacketsIn | The number of packets received on all network interfaces by the node or cluster | Count | Multi | ClusterId | Applicable |
| NetworkPacketsIn |  | Count | Multi | ClusterId, NodeId | Applicable |
| NetworkPacketsIn |  | Count | Multi | Region | Applicable |
| NetworkPacketsOut | The number of packets sent out on all network interfaces by the node or cluster. This metric identifies the volume of outgoing traffic in terms of the number of packets on a single node or cluster. | Count | Multi | ClusterId | Applicable |
| NetworkPacketsOut |  | Count | Multi | ClusterId, NodeId | Applicable |
| NetworkPacketsOut |  | Count | Multi | Region | Applicable |
| PutItemRequestCount | The number of PutItem requests handled by the node or cluster | Count | Multi | ClusterId |  |
| PutItemRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| PutItemRequestCount |  | Count | Sum | ClusterId | Applicable |
| PutItemRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| PutItemRequestCount |  | Count | Multi | Region |  |
| PutItemRequestCount |  | Count | Sum | Region | Applicable |
| QueryCacheHits | The number of times a query result was returned from the node or cluster cache | Count | Multi | ClusterId |  |
| QueryCacheHits |  | Count | Multi | ClusterId, NodeId |  |
| QueryCacheHits |  | Count | Sum | ClusterId | Applicable |
| QueryCacheHits |  | Count | Sum | ClusterId, NodeId | Applicable |
| QueryCacheHits |  | Count | Multi | Region |  |
| QueryCacheHits |  | Count | Sum | Region | Applicable |
| QueryCacheMisses | The number of times a query result was not in the node or cluster cache, and had to be retrieved from DynamoDB | Count | Multi | ClusterId |  |
| QueryCacheMisses |  | Count | Multi | ClusterId, NodeId |  |
| QueryCacheMisses |  | Count | Sum | ClusterId | Applicable |
| QueryCacheMisses |  | Count | Sum | ClusterId, NodeId | Applicable |
| QueryCacheMisses |  | Count | Multi | Region |  |
| QueryCacheMisses |  | Count | Sum | Region | Applicable |
| QueryRequestCount | The number of query requests handled by the node or cluster | Count | Multi | ClusterId |  |
| QueryRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| QueryRequestCount |  | Count | Sum | ClusterId | Applicable |
| QueryRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| QueryRequestCount |  | Count | Multi | Region |  |
| QueryRequestCount |  | Count | Sum | Region | Applicable |
| ScanCacheHits | The number of times a scan result was returned from the node or cluster cache | Count | Multi | ClusterId |  |
| ScanCacheHits |  | Count | Multi | ClusterId, NodeId |  |
| ScanCacheHits |  | Count | Sum | ClusterId | Applicable |
| ScanCacheHits |  | Count | Sum | ClusterId, NodeId | Applicable |
| ScanCacheHits |  | Count | Multi | Region |  |
| ScanCacheHits |  | Count | Sum | Region | Applicable |
| ScanCacheMisses | The number of times a scan result was not in the node or cluster cache, and had to be retrieved from DynamoDB | Count | Multi | ClusterId |  |
| ScanCacheMisses |  | Count | Multi | ClusterId, NodeId |  |
| ScanCacheMisses |  | Count | Sum | ClusterId | Applicable |
| ScanCacheMisses |  | Count | Sum | ClusterId, NodeId | Applicable |
| ScanCacheMisses |  | Count | Multi | Region |  |
| ScanCacheMisses |  | Count | Sum | Region | Applicable |
| ScanRequestCount | The number of scan requests handled by the node or cluster | Count | Multi | ClusterId |  |
| ScanRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| ScanRequestCount |  | Count | Sum | ClusterId | Applicable |
| ScanRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| ScanRequestCount |  | Count | Multi | Region |  |
| ScanRequestCount |  | Count | Sum | Region | Applicable |
| ThrottledRequestCount | Total number of requests throttled by the node or cluster | Count | Multi | ClusterId |  |
| ThrottledRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| ThrottledRequestCount |  | Count | Sum | ClusterId | Applicable |
| ThrottledRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| ThrottledRequestCount |  | Count | Multi | Region |  |
| ThrottledRequestCount |  | Count | Sum | Region | Applicable |
| TotalRequestCount | Total number of requests handled by the node or cluster | Count | Multi | ClusterId |  |
| TotalRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| TotalRequestCount |  | Count | Sum | ClusterId | Applicable |
| TotalRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| TotalRequestCount |  | Count | Multi | Region |  |
| TotalRequestCount |  | Count | Sum | Region | Applicable |
| TransactGetItemsCount | The number of TransactGetItems requests handled by the node or cluster | Count | Multi | ClusterId |  |
| TransactGetItemsCount |  | Count | Multi | ClusterId, NodeId |  |
| TransactGetItemsCount |  | Count | Sum | ClusterId | Applicable |
| TransactGetItemsCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| TransactGetItemsCount |  | Count | Multi | Region |  |
| TransactGetItemsCount |  | Count | Sum | Region | Applicable |
| TransactWriteItemsCount | The number of TransactWriteItems requests handled by the node or cluster | Count | Multi | ClusterId |  |
| TransactWriteItemsCount |  | Count | Multi | ClusterId, NodeId |  |
| TransactWriteItemsCount |  | Count | Sum | ClusterId | Applicable |
| TransactWriteItemsCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| TransactWriteItemsCount |  | Count | Multi | Region |  |
| TransactWriteItemsCount |  | Count | Sum | Region | Applicable |
| UpdateItemRequestCount | The number of UpdateItem requests handled by the node or cluster | Count | Multi | ClusterId |  |
| UpdateItemRequestCount |  | Count | Multi | ClusterId, NodeId |  |
| UpdateItemRequestCount |  | Count | Sum | ClusterId | Applicable |
| UpdateItemRequestCount |  | Count | Sum | ClusterId, NodeId | Applicable |
| UpdateItemRequestCount |  | Count | Multi | Region |  |
| UpdateItemRequestCount |  | Count | Sum | Region | Applicable |