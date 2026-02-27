---
title: Amazon Aurora monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-aurora
scraped: 2026-02-27T21:29:17.694397
---

# Amazon Aurora monitoring

# Amazon Aurora monitoring

* How-to guide
* 22-min read
* Published Oct 15, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon Aurora. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

To enable monitoring for this service, you need

* ActiveGate version 1.181+, as follows:

  + For Dynatrace SaaS deployments, you need an Environment ActiveGate or a Multi-environment ActiveGate.
  + For Dynatrace Managed deployments, you can use any kind of ActiveGate.

    For role-based access (whether in a [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") or [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) deployment), you need an [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") installed on an Amazon EC2 host.
* Dynatrace version 1.182+
* An updated [AWS monitoring policy](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#aws-policy-and-authentication "Integrate metrics from Amazon CloudWatch.") to include the additional AWS services.  
  To [update the AWS IAM policyï»¿](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-edit.html#edit-managed-policy-console), use the JSON below, containing the monitoring policy (permissions) for all supporting services.

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

This service monitors Amazon RDS clusters. You can find the already monitored resources on the AWS overview page in the **Cloud services** section.

To monitor RDS instances instead, check the Amazon RDS and the **RDS** section on the AWS overview page.

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

`DBClusterIdentifier` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| ActiveTransactions | The average number of current transactions executing on an Aurora database instance per second | Count/Second | Average | DBClusterIdentifier, Role |  |
| ActiveTransactions |  | Count/Second | Average | DBClusterIdentifier |  |
| ActiveTransactions |  | Count/Second | Average | DatabaseClass, Region |  |
| ActiveTransactions |  | Count/Second | Average | EngineName, Region |  |
| ActiveTransactions |  | Count/Second | Average | Region |  |
| ActiveTransactions |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| ActiveTransactions |  | Count/Second | Maximum | DBClusterIdentifier |  |
| ActiveTransactions |  | Count/Second | Maximum | DatabaseClass, Region |  |
| ActiveTransactions |  | Count/Second | Maximum | EngineName, Region |  |
| ActiveTransactions |  | Count/Second | Maximum | Region |  |
| AuroraBinlogReplicaLag | The amount of time a replica DB cluster running on Aurora with MySQL compatibility lags behind the source DB cluster | Seconds | Multi | DBClusterIdentifier, Role |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | DBClusterIdentifier |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | DatabaseClass, Region |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | EngineName, Region |  |
| AuroraBinlogReplicaLag |  | Seconds | Multi | Region |  |
| AuroraReplicaLagMaximum | The maximum amount of lag between the primary instance and each Aurora DB instance in the DB cluster | Milliseconds | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | DBClusterIdentifier |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | DatabaseClass, Region |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | EngineName, Region |  |
| AuroraReplicaLagMaximum |  | Milliseconds | Average | Region |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | DBClusterIdentifier |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | DatabaseClass, Region |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | EngineName, Region |  |
| AuroraReplicaLagMinimum |  | Milliseconds | Average | Region |  |
| AuroraReplicaLag | For an Aurora replica, the amount of lag when replicating updates from the primary instance | Milliseconds | Average | DBClusterIdentifier, Role |  |
| AuroraReplicaLag |  | Milliseconds | Average | DBClusterIdentifier |  |
| AuroraReplicaLag |  | Milliseconds | Average | DatabaseClass, Region |  |
| AuroraReplicaLag |  | Milliseconds | Average | EngineName, Region |  |
| AuroraReplicaLag |  | Milliseconds | Average | Region |  |
| BacktrackChangeRecordsCreationRate | The number of backtrack change records created over 5 minutes for your DB cluster | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | EngineName, Region |  |
| BacktrackChangeRecordsCreationRate |  | Count | Sum | Region |  |
| BacktrackChangeRecordsStored | The number of backtrack change records used by your DB cluster | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackChangeRecordsStored |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackChangeRecordsStored |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackChangeRecordsStored |  | Count | Sum | EngineName, Region |  |
| BacktrackChangeRecordsStored |  | Count | Sum | Region |  |
| BacktrackWindowActual | The difference between the target backtrack window and the actual backtrack window | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackWindowActual |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackWindowActual |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackWindowActual |  | Count | Sum | EngineName, Region |  |
| BacktrackWindowActual |  | Count | Sum | Region |  |
| BacktrackWindowAlert | The number of times that the actual backtrack window is smaller than the target backtrack window for a given period of time | Count | Sum | DBClusterIdentifier, Role |  |
| BacktrackWindowAlert |  | Count | Sum | DBClusterIdentifier |  |
| BacktrackWindowAlert |  | Count | Sum | DatabaseClass, Region |  |
| BacktrackWindowAlert |  | Count | Sum | EngineName, Region |  |
| BacktrackWindowAlert |  | Count | Sum | Region |  |
| BinLogDiskUsage | The amount of disk space occupied by binary logs on the primary instance | Bytes | Average | DBClusterIdentifier, Role |  |
| BinLogDiskUsage |  | Bytes | Average | DBClusterIdentifier |  |
| BinLogDiskUsage |  | Bytes | Average | DatabaseClass, Region |  |
| BinLogDiskUsage |  | Bytes | Average | EngineName, Region |  |
| BinLogDiskUsage |  | Bytes | Average | Region |  |
| BlockedTransactions | The average number of transactions in the database that are blocked per second | Count/Second | Average | DBClusterIdentifier, Role |  |
| BlockedTransactions |  | Count/Second | Average | DBClusterIdentifier |  |
| BlockedTransactions |  | Count/Second | Average | DatabaseClass, Region |  |
| BlockedTransactions |  | Count/Second | Average | EngineName, Region |  |
| BlockedTransactions |  | Count/Second | Average | Region |  |
| BlockedTransactions |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| BlockedTransactions |  | Count/Second | Maximum | DBClusterIdentifier |  |
| BlockedTransactions |  | Count/Second | Maximum | DatabaseClass, Region |  |
| BlockedTransactions |  | Count/Second | Maximum | EngineName, Region |  |
| BlockedTransactions |  | Count/Second | Maximum | Region |  |
| BufferCacheHitRatio | The percentage of requests that are served by the buffer cache | Percent | Average | DBClusterIdentifier, Role |  |
| BufferCacheHitRatio |  | Percent | Average | DBClusterIdentifier |  |
| BufferCacheHitRatio |  | Percent | Average | DatabaseClass, Region |  |
| BufferCacheHitRatio |  | Percent | Average | EngineName, Region |  |
| BufferCacheHitRatio |  | Percent | Average | Region |  |
| CPUCreditBalance | The number of CPU credits that an instance has accumulated, reported at 5-minute intervals. This metric applies only to `db.t2.small` and `db.t2.medium` instances. You can use this metric to determine how long an Aurora MySQL DB instance can burst beyond its baseline performance level at a given rate. | Count | Average | DBClusterIdentifier, Role |  |
| CPUCreditBalance |  | Count | Average | DBClusterIdentifier |  |
| CPUCreditBalance |  | Count | Average | DatabaseClass, Region |  |
| CPUCreditBalance |  | Count | Average | EngineName, Region |  |
| CPUCreditBalance |  | Count | Average | Region |  |
| CPUCreditUsage | The number of CPU credits consumed during the specified period, reported at 5-minute intervals. This metric applies only to `db.t2.small` and `db.t2.medium` instances. This metric measures the amount of time during which physical CPUs have been used for processing instructions by virtual CPUs allocated to the Aurora MySQL DB instance. | Count | Average | DBClusterIdentifier, Role |  |
| CPUCreditUsage |  | Count | Average | DBClusterIdentifier |  |
| CPUCreditUsage |  | Count | Average | DatabaseClass, Region |  |
| CPUCreditUsage |  | Count | Average | EngineName, Region |  |
| CPUCreditUsage |  | Count | Average | Region |  |
| CPUUtilization | The percentage of CPU used by an Aurora DB instance | Percent | Average | DBClusterIdentifier, Role |  |
| CPUUtilization |  | Percent | Average | DBClusterIdentifier |  |
| CPUUtilization |  | Percent | Average | DatabaseClass, Region |  |
| CPUUtilization |  | Percent | Average | EngineName, Region |  |
| CPUUtilization |  | Percent | Average | Region |  |
| CPUUtilization |  | Percent | Maximum | DBClusterIdentifier, Role |  |
| CPUUtilization |  | Percent | Maximum | DBClusterIdentifier |  |
| CPUUtilization |  | Percent | Maximum | DatabaseClass, Region |  |
| CPUUtilization |  | Percent | Maximum | EngineName, Region |  |
| CPUUtilization |  | Percent | Maximum | Region |  |
| CommitLatency | The latency for commit operations | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| CommitLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| CommitLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| CommitLatency |  | Milliseconds | Multi | EngineName, Region |  |
| CommitLatency |  | Milliseconds | Multi | Region |  |
| CommitThroughput | The average number of commit operations per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| CommitThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| CommitThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| CommitThroughput |  | Count/Second | Multi | EngineName, Region |  |
| CommitThroughput |  | Count/Second | Multi | Region |  |
| DDLLatency | The latency for data definition language (DDL) requests such as example, create, alter, and drop requests | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| DDLLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| DDLLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| DDLLatency |  | Milliseconds | Multi | EngineName, Region |  |
| DDLLatency |  | Milliseconds | Multi | Region |  |
| DDLThroughput | The average number of DDL requests per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| DDLThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| DDLThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| DDLThroughput |  | Count/Second | Multi | EngineName, Region |  |
| DDLThroughput |  | Count/Second | Multi | Region |  |
| DMLLatency | The latency for inserts, updates, and deletes | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| DMLLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| DMLLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| DMLLatency |  | Milliseconds | Multi | EngineName, Region |  |
| DMLLatency |  | Milliseconds | Multi | Region |  |
| DMLThroughput | The average number of inserts, updates, and deletes per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| DMLThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| DMLThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| DMLThroughput |  | Count/Second | Multi | EngineName, Region |  |
| DMLThroughput |  | Count/Second | Multi | Region |  |
| DatabaseConnections | The number of connections to an Aurora DB instance | Count | Average | DBClusterIdentifier, Role |  |
| DatabaseConnections |  | Count | Average | DBClusterIdentifier |  |
| DatabaseConnections |  | Count | Average | DatabaseClass, Region |  |
| DatabaseConnections |  | Count | Average | EngineName, Region |  |
| DatabaseConnections |  | Count | Average | Region |  |
| DatabaseConnections |  | Count | Maximum | DBClusterIdentifier, Role |  |
| DatabaseConnections |  | Count | Maximum | DBClusterIdentifier |  |
| DatabaseConnections |  | Count | Maximum | DatabaseClass, Region |  |
| DatabaseConnections |  | Count | Maximum | EngineName, Region |  |
| DatabaseConnections |  | Count | Maximum | Region |  |
| Deadlocks | The average number of deadlocks in the database per second | Count/Second | Average | DBClusterIdentifier, Role |  |
| Deadlocks |  | Count/Second | Average | DBClusterIdentifier |  |
| Deadlocks |  | Count/Second | Average | DatabaseClass, Region |  |
| Deadlocks |  | Count/Second | Average | EngineName, Region |  |
| Deadlocks |  | Count/Second | Average | Region |  |
| Deadlocks |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| Deadlocks |  | Count/Second | Maximum | DBClusterIdentifier |  |
| Deadlocks |  | Count/Second | Maximum | DatabaseClass, Region |  |
| Deadlocks |  | Count/Second | Maximum | EngineName, Region |  |
| Deadlocks |  | Count/Second | Maximum | Region |  |
| DeleteLatency | The latency for delete queries | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| DeleteLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| DeleteLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| DeleteLatency |  | Milliseconds | Multi | EngineName, Region |  |
| DeleteLatency |  | Milliseconds | Multi | Region |  |
| DeleteThroughput | The average number of delete queries per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| DeleteThroughput |  | Count/Second | Multi | DBClusterIdentifier | Applicable |
| DeleteThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| DeleteThroughput |  | Count/Second | Multi | EngineName, Region |  |
| DeleteThroughput |  | Count/Second | Multi | Region |  |
| DiskQueueDepth | The number of outstanding read/write requests waiting to access the disk | Count | Multi | DBClusterIdentifier, Role |  |
| DiskQueueDepth |  | Count | Multi | DBClusterIdentifier |  |
| DiskQueueDepth |  | Count | Multi | DatabaseClass, Region |  |
| DiskQueueDepth |  | Count | Multi | EngineName, Region |  |
| DiskQueueDepth |  | Count | Multi | Region |  |
| EngineUptime | The amount of time that the instance has been running | Seconds | Average | DBClusterIdentifier, Role |  |
| EngineUptime |  | Seconds | Average | DBClusterIdentifier |  |
| EngineUptime |  | Seconds | Average | DatabaseClass, Region |  |
| EngineUptime |  | Seconds | Average | EngineName, Region |  |
| EngineUptime |  | Seconds | Average | Region |  |
| FreeLocalStorage | The amount of local storage available for each DB instance. | Bytes | Average | DBClusterIdentifier, Role |  |
| FreeLocalStorage |  | Bytes | Average | DBClusterIdentifier |  |
| FreeLocalStorage |  | Bytes | Average | DatabaseClass, Region |  |
| FreeLocalStorage |  | Bytes | Average | EngineName, Region |  |
| FreeLocalStorage |  | Bytes | Average | Region |  |
| FreeableMemory | The amount of available random access memory | Bytes | Average | DBClusterIdentifier, Role |  |
| FreeableMemory |  | Bytes | Average | DBClusterIdentifier |  |
| FreeableMemory |  | Bytes | Average | DatabaseClass, Region |  |
| FreeableMemory |  | Bytes | Average | EngineName, Region |  |
| FreeableMemory |  | Bytes | Average | Region |  |
| InsertLatency | The latency for insert queries | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| InsertLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| InsertLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| InsertLatency |  | Milliseconds | Multi | EngineName, Region |  |
| InsertLatency |  | Milliseconds | Multi | Region |  |
| InsertThroughput | The average number of insert queries per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| InsertThroughput |  | Count/Second | Multi | DBClusterIdentifier | Applicable |
| InsertThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| InsertThroughput |  | Count/Second | Multi | EngineName, Region |  |
| InsertThroughput |  | Count/Second | Multi | Region |  |
| LoginFailures | The average number of failed login attempts per second | Count/Second | Average | DBClusterIdentifier, Role |  |
| LoginFailures |  | Count/Second | Average | DBClusterIdentifier |  |
| LoginFailures |  | Count/Second | Average | DatabaseClass, Region |  |
| LoginFailures |  | Count/Second | Average | EngineName, Region |  |
| LoginFailures |  | Count/Second | Average | Region |  |
| LoginFailures |  | Count/Second | Maximum | DBClusterIdentifier, Role |  |
| LoginFailures |  | Count/Second | Maximum | DBClusterIdentifier |  |
| LoginFailures |  | Count/Second | Maximum | DatabaseClass, Region |  |
| LoginFailures |  | Count/Second | Maximum | EngineName, Region |  |
| LoginFailures |  | Count/Second | Maximum | Region |  |
| MaximumUsedTransactionIDs | The age of the oldest unvacuumed transaction ID in transactions. If this value reaches `2`,`146`,`483`,`648` (2^31 - 1,000,000), the database is forced into read-only mode, to avoid transaction ID wraparound. | Count | Average | DBClusterIdentifier, Role |  |
| MaximumUsedTransactionIDs |  | Count | Average | DBClusterIdentifier |  |
| MaximumUsedTransactionIDs |  | Count | Average | DatabaseClass, Region |  |
| MaximumUsedTransactionIDs |  | Count | Average | EngineName, Region |  |
| MaximumUsedTransactionIDs |  | Count | Average | Region |  |
| NetworkReceiveThroughput | The amount of network throughput received from clients by each instance in the Aurora MySQL DB cluster. This throughput doesn't include network traffic between instances in the Aurora DB cluster and the cluster volume. | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| NetworkReceiveThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkThroughput | The amount of network throughput both received from and transmitted to clients by each instance in the Aurora MySQL DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume. | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| NetworkThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| NetworkThroughput |  | Bytes/Second | Multi | Region |  |
| NetworkTransmitThroughput | The amount of network throughput sent to clients by each instance in the Aurora DB cluster. This throughput doesn't include network traffic between instances in the DB cluster and the cluster volume. | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| NetworkTransmitThroughput |  | Bytes/Second | Multi | Region |  |
| Queries | The average number of queries executed per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| Queries |  | Count/Second | Multi | DBClusterIdentifier | Applicable |
| Queries |  | Count/Second | Multi | DatabaseClass, Region |  |
| Queries |  | Count/Second | Multi | EngineName, Region |  |
| Queries |  | Count/Second | Multi | Region |  |
| RDSToAuroraPostgreSQLReplicaLag | The lag when replicating updates from the primary RDS PostgreSQL instance to other nodes in the cluster | Seconds | Multi | DBClusterIdentifier, Role |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | DBClusterIdentifier |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | DatabaseClass, Region |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | EngineName, Region |  |
| RDSToAuroraPostgreSQLReplicaLag |  | Seconds | Multi | Region |  |
| ReadIOPS | The average number of disk I/O operations per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| ReadIOPS |  | Count/Second | Multi | DBClusterIdentifier |  |
| ReadIOPS |  | Count/Second | Multi | DatabaseClass, Region |  |
| ReadIOPS |  | Count/Second | Multi | EngineName, Region |  |
| ReadIOPS |  | Count/Second | Multi | Region |  |
| ReadLatency | The average amount of time taken per disk I/O operation | Seconds | Multi | DBClusterIdentifier, Role |  |
| ReadLatency |  | Seconds | Multi | DBClusterIdentifier |  |
| ReadLatency |  | Seconds | Multi | DatabaseClass, Region |  |
| ReadLatency |  | Seconds | Multi | EngineName, Region |  |
| ReadLatency |  | Seconds | Multi | Region |  |
| ReadThroughput | The average number of bytes read from disk per second | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| ReadThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| ReadThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| ReadThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| ReadThroughput |  | Bytes/Second | Multi | Region |  |
| ResultSetCacheHitRatio | The percentage of requests that are served by the resultset cache | Percent | Average | DBClusterIdentifier, Role |  |
| ResultSetCacheHitRatio |  | Percent | Average | DBClusterIdentifier |  |
| ResultSetCacheHitRatio |  | Percent | Average | DatabaseClass, Region |  |
| ResultSetCacheHitRatio |  | Percent | Average | EngineName, Region |  |
| ResultSetCacheHitRatio |  | Percent | Average | Region |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | DBClusterIdentifier, Role |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | DBClusterIdentifier |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | DatabaseClass, Region |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | EngineName, Region |  |
| ResultSetCacheHitRatio |  | Percent | Maximum | Region |  |
| SelectLatency | The latency for select queries | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| SelectLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| SelectLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| SelectLatency |  | Milliseconds | Multi | EngineName, Region |  |
| SelectLatency |  | Milliseconds | Multi | Region |  |
| SelectThroughput | The average number of select queries per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| SelectThroughput |  | Count/Second | Multi | DBClusterIdentifier |  |
| SelectThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| SelectThroughput |  | Count/Second | Multi | EngineName, Region |  |
| SelectThroughput |  | Count/Second | Multi | Region |  |
| SwapUsage | The amount of swap space used on the Aurora PostgreSQL DB instance | Bytes | Multi | DBClusterIdentifier, Role |  |
| SwapUsage |  | Bytes | Multi | DBClusterIdentifier |  |
| SwapUsage |  | Bytes | Multi | DatabaseClass, Region |  |
| SwapUsage |  | Bytes | Multi | EngineName, Region |  |
| SwapUsage |  | Bytes | Multi | Region |  |
| TransactionLogsDiskUsage | The amount of disk space consumed by transaction logs on the Aurora PostgreSQL DB instance. This metric is only generated when Aurora PostgreSQL is using logical replication or AWS Database Migration Service. By default, Aurora PostgreSQL uses log records, not transaction logs. When transaction logs aren't in use, the value for this metric is -1. | Bytes | Multi | DBClusterIdentifier, Role |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | DBClusterIdentifier |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | DatabaseClass, Region |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | EngineName, Region |  |
| TransactionLogsDiskUsage |  | Bytes | Multi | Region |  |
| UpdateLatency | The latency for update queries | Milliseconds | Multi | DBClusterIdentifier, Role |  |
| UpdateLatency |  | Milliseconds | Multi | DBClusterIdentifier |  |
| UpdateLatency |  | Milliseconds | Multi | DatabaseClass, Region |  |
| UpdateLatency |  | Milliseconds | Multi | EngineName, Region |  |
| UpdateLatency |  | Milliseconds | Multi | Region |  |
| UpdateThroughput | The average number of update queries per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| UpdateThroughput |  | Count/Second | Multi | DBClusterIdentifier | Applicable |
| UpdateThroughput |  | Count/Second | Multi | DatabaseClass, Region |  |
| UpdateThroughput |  | Count/Second | Multi | EngineName, Region |  |
| UpdateThroughput |  | Count/Second | Multi | Region |  |
| VolumeBytesUsed | The amount of storage used by your Aurora DB instance. This value affects the cost of the Aurora DB cluster. | Bytes | Multi | DBClusterIdentifier, Role |  |
| VolumeBytesUsed |  | Bytes | Multi | DBClusterIdentifier |  |
| VolumeBytesUsed |  | Bytes | Multi | DatabaseClass, Region |  |
| VolumeBytesUsed |  | Bytes | Multi | EngineName, Region |  |
| VolumeBytesUsed |  | Bytes | Multi | Region |  |
| VolumeReadIOPs | The number of billed read I/O operations from a cluster volume within a 5-minute interval | Count/Second | Multi | DBClusterIdentifier, Role |  |
| VolumeReadIOPs |  | Count/Second | Multi | DBClusterIdentifier |  |
| VolumeReadIOPs |  | Count/Second | Multi | DatabaseClass, Region |  |
| VolumeReadIOPs |  | Count/Second | Multi | EngineName, Region |  |
| VolumeReadIOPs |  | Count/Second | Multi | Region |  |
| VolumeWriteIOPs | The number of write disk I/O operations to the cluster volume, reported at 5-minute intervals | Count/Second | Multi | DBClusterIdentifier, Role |  |
| VolumeWriteIOPs |  | Count/Second | Multi | DBClusterIdentifier |  |
| VolumeWriteIOPs |  | Count/Second | Multi | DatabaseClass, Region |  |
| VolumeWriteIOPs |  | Count/Second | Multi | EngineName, Region |  |
| VolumeWriteIOPs |  | Count/Second | Multi | Region |  |
| WriteIOPS | The average number of disk I/O operations per second | Count/Second | Multi | DBClusterIdentifier, Role |  |
| WriteIOPS |  | Count/Second | Multi | DBClusterIdentifier |  |
| WriteIOPS |  | Count/Second | Multi | DatabaseClass, Region |  |
| WriteIOPS |  | Count/Second | Multi | EngineName, Region |  |
| WriteIOPS |  | Count/Second | Multi | Region |  |
| WriteLatency | The average amount of time taken per disk I/O operation | Seconds | Multi | DBClusterIdentifier, Role |  |
| WriteLatency |  | Seconds | Multi | DBClusterIdentifier |  |
| WriteLatency |  | Seconds | Multi | DatabaseClass, Region |  |
| WriteLatency |  | Seconds | Multi | EngineName, Region |  |
| WriteLatency |  | Seconds | Multi | Region |  |
| WriteThroughput | The average number of bytes written to disk | Bytes/Second | Multi | DBClusterIdentifier, Role |  |
| WriteThroughput |  | Bytes/Second | Multi | DBClusterIdentifier |  |
| WriteThroughput |  | Bytes/Second | Multi | DatabaseClass, Region |  |
| WriteThroughput |  | Bytes/Second | Multi | EngineName, Region |  |
| WriteThroughput |  | Bytes/Second | Multi | Region |  |