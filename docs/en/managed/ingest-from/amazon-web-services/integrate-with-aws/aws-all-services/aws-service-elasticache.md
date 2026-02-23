---
title: Amazon ElastiCache monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elasticache
scraped: 2026-02-23T21:34:57.680751
---

# Amazon ElastiCache monitoring

# Amazon ElastiCache monitoring

* How-to guide
* 13-min read
* Published Oct 15, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon ElastiCache. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

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

`CacheClusterId` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| ActiveDefragHits | The number of value reallocations per minute performed by the active defragmentation process. This is derived from `active_defrag_hits` statistic. | Count | Sum | CacheClusterId, CacheNodeId |  |
| ActiveDefragHits |  | Count | Sum | CacheClusterId |  |
| BytesReadIntoMemcached | The number of bytes that have been read from the network by the cache node | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesReadIntoMemcached |  | Bytes | Sum | CacheClusterId |  |
| BytesUsedFworCacheItems |  | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForCacheItems | The number of bytes used to store cache items | Bytes | Sum | CacheClusterId |  |
| BytesUsedForCache | The total number of bytes allocated by Redis for all purposes, including the dataset, buffers, and so on. This is derived from used\_memory statistic. | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForCache |  | Bytes | Sum | CacheClusterId |  |
| BytesUsedForHash | The number of bytes currently used by hash tables | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesUsedForHash |  | Bytes | Sum | CacheClusterId |  |
| BytesWrittenOutFromMemcached | The number of bytes that have been written to the network by the cache node | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| BytesWrittenOutFromMemcached |  | Bytes | Sum | CacheClusterId |  |
| CPUUtilization | The percentage of CPU utilization for the entire host | Percent | Multi | CacheClusterId, CacheNodeId |  |
| CPUUtilization |  | Percent | Multi | CacheClusterId | Applicable |
| CacheHits | The number of successful read-only key lookups in the main dictionary. This is derived from keyspace\_hits statistic. | Count | Sum | CacheClusterId, CacheNodeId |  |
| CacheHits |  | Count | Sum | CacheClusterId |  |
| CacheMisses | The number of unsuccessful read-only key lookups in the main dictionary. This is derived from keyspace\_misses statistic. | Count | Sum | CacheClusterId, CacheNodeId |  |
| CacheMisses |  | Count | Sum | CacheClusterId |  |
| CasBadval | The number of CAS (check and set) requests the cache has received where the CAS value did not match the CAS value stored | Count | Sum | CacheClusterId, CacheNodeId |  |
| CasBadval |  | Count | Sum | CacheClusterId |  |
| CasHits | The number of CAS requests the cache has received where the requested key was found and the CAS value matched | Count | Sum | CacheClusterId, CacheNodeId |  |
| CasHits |  | Count | Sum | CacheClusterId |  |
| CasMisses | The number of CAS requests the cache has received where the key requested was not found | Count | Sum | CacheClusterId, CacheNodeId |  |
| CasMisses |  | Count | Sum | CacheClusterId |  |
| CmdConfigGet | The cumulative number of config get requests | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdConfigGet |  | Count | Sum | CacheClusterId |  |
| CmdConfigSet | The cumulative number of config set requests | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdConfigSet |  | Count | Sum | CacheClusterId |  |
| CmdFlush | The number of flush commands the cache has received | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdFlush |  | Count | Sum | CacheClusterId |  |
| CmdGet | The number of get commands the cache has received | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdGet |  | Count | Sum | CacheClusterId |  |
| CmdSet | The number of set commands the cache has received | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdSet |  | Count | Sum | CacheClusterId |  |
| CmdTouch | The cumulative number of touch requests | Count | Sum | CacheClusterId, CacheNodeId |  |
| CmdTouch |  | Count | Sum | CacheClusterId |  |
| CurrConfig | The current number of configurations stored | Count | Sum | CacheClusterId, CacheNodeId |  |
| CurrConfig |  | Count | Sum | CacheClusterId |  |
| CurrConnections | A count of the number of connections connected to the cache at an instant in time. ElastiCache uses two to three of the connections to monitor the cluster. | Count | Multi | CacheClusterId, CacheNodeId |  |
| CurrConnections |  | Count | Multi | CacheClusterId | Applicable |
| CurrItems | A count of the number of items currently stored in the cache | Count | Multi | CacheClusterId, CacheNodeId |  |
| CurrItems |  | Count | Multi | CacheClusterId |  |
| DatabaseMemoryUsagePercentage |  | Percent | Multi | CacheClusterId, CacheNodeId |  |
| DatabaseMemoryUsagePercentage |  | Percent | Multi | CacheClusterId |  |
| DatabaseMemoryUsagePercentage |  | Percent | Multi | Region |  |
| DecrHits | The number of decrement requests the cache has received where the requested key was found | Count | Sum | CacheClusterId, CacheNodeId |  |
| DecrHits |  | Count | Sum | CacheClusterId |  |
| DecrMisses | The number of decrement requests the cache has received where the requested key was not found | Count | Sum | CacheClusterId, CacheNodeId |  |
| DecrMisses |  | Count | Sum | CacheClusterId |  |
| DeleteHits | The number of delete requests the cache has received where the requested key was found | Count | Sum | CacheClusterId, CacheNodeId |  |
| DeleteHits |  | Count | Sum | CacheClusterId |  |
| DeleteMisses | The number of delete requests the cache has received where the requested key was not found. | Count | Sum | CacheClusterId, CacheNodeId |  |
| DeleteMisses |  | Count | Sum | CacheClusterId |  |
| EngineCPUUtilization | Provides CPU utilization of the Redis engine thread | Percent | Multi | CacheClusterId, CacheNodeId |  |
| EngineCPUUtilization |  | Percent | Multi | CacheClusterId |  |
| EvictedUnfetched | The number of valid items evicted from the least recently used cache (LRU) which were never touched after being set | Count | Sum | CacheClusterId, CacheNodeId |  |
| EvictedUnfetched |  | Count | Sum | CacheClusterId |  |
| Evictions | The number of non-expired items the cache evicted to allow space for new writes | Count | Sum | CacheClusterId, CacheNodeId |  |
| Evictions |  | Count | Sum | CacheClusterId | Applicable |
| ExpiredUnfetched | The number of expired items reclaimed from the LRU which were never touched after being set | Count | Sum | CacheClusterId, CacheNodeId |  |
| ExpiredUnfetched |  | Count | Sum | CacheClusterId |  |
| FreeableMemory | The amount of free memory available on the host. This is derived from the RAM, buffers, and cache that the OS reports as freeable. | Bytes | Multi | CacheClusterId, CacheNodeId |  |
| FreeableMemory |  | Bytes | Multi | CacheClusterId |  |
| GetHits | The number of get requests the cache has received where the key requested was found | Count | Sum | CacheClusterId, CacheNodeId |  |
| GetHits |  | Count | Sum | CacheClusterId |  |
| GetMisses | The number of get requests the cache has received where the key requested was not found | Count | Sum | CacheClusterId, CacheNodeId |  |
| GetMisses |  | Count | Sum | CacheClusterId |  |
| GetTypeCmds | The total number of read-only type commands. This is derived from the Redis commandstats statistic by summing all of the read-only type commands (get, hget, scard, lrange, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| GetTypeCmds |  | Count | Sum | CacheClusterId |  |
| HashBasedCmds | The total number of commands that are hash-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more hashes (hget, hkeys, hvals, hdel, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| HashBasedCmds |  | Count | Sum | CacheClusterId |  |
| HyperLogLogBasedCmds | The total number of HyperLogLog-based commands | Count | Sum | CacheClusterId, CacheNodeId |  |
| HyperLogLogBasedCmds |  | Count | Sum | CacheClusterId |  |
| IncrHits | The number of increment requests the cache has received where the key requested was found | Count | Sum | CacheClusterId, CacheNodeId |  |
| IncrHits |  | Count | Sum | CacheClusterId |  |
| IncrMisses | The number of increment requests the cache has received where the key requested was not found | Count | Sum | CacheClusterId, CacheNodeId |  |
| IncrMisses |  | Count | Sum | CacheClusterId |  |
| KeyBasedCmds | The total number of commands that are key-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more keys across multiple data structures (del, expire, rename, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| KeyBasedCmds |  | Count | Sum | CacheClusterId |  |
| KeysTracked | The number of keys being tracked by Redis key tracking as a percentage of tracking-table-max-keys. Key tracking is used to aid client-side caching and notifies clients when keys are modified. | Count | Sum | CacheClusterId, CacheNodeId |  |
| KeysTracked |  | Count | Sum | CacheClusterId |  |
| KeysTracked |  | Count | Sum | Region |  |
| ListBasedCmds | The total number of commands that are list-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more lists (lindex, lrange, lpush, ltrim, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| ListBasedCmds |  | Count | Sum | CacheClusterId |  |
| Network Packets Per Second Allowance Exceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| Network Packets Per Second Allowance Exceeded |  | Count | Sum | CacheClusterId |  |
| NetworkBandwidthInAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBandwidthInAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NetworkBandwidthOutAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBandwidthOutAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NetworkBytesIn | The number of bytes the host has read from the network | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBytesIn |  | Bytes | Sum | CacheClusterId |  |
| NetworkBytesOut | The number of bytes sent out on all network interfaces by the instance | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| NetworkBytesOut |  | Bytes | Sum | CacheClusterId |  |
| NetworkConntrackAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkConntrackAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NetworkLinkLocalAllowanceExceeded |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| NetworkLinkLocalAllowanceExceeded |  | Count | Sum | CacheClusterId |  |
| NewConnections | The number of new connections the cache has received. This is derived from the memcached total\_connections statistic by recording the change in total\_connections across a period of time. | Count | Sum | CacheClusterId, CacheNodeId |  |
| NewConnections |  | Count | Sum | CacheClusterId |  |
| NewItems | The number of new items the cache has stored. This is derived from the memcached total\_items statistic by recording the change in total\_items across a period of time. | Count | Sum | CacheClusterId, CacheNodeId |  |
| NewItems |  | Count | Sum | CacheClusterId |  |
| Reclaimed | The number of expired items the cache evicted to allow space for new writes | Count | Sum | CacheClusterId, CacheNodeId |  |
| Reclaimed |  | Count | Sum | CacheClusterId |  |
| ReplicationBytes | For nodes in a replicated configuration, ReplicationBytes reports the number of bytes that the primary is sending to all of its replicas. This metric is representative of the write load on the replication group. This is derived from the master\_repl\_offset statistic. | Bytes | Multi | CacheClusterId, CacheNodeId |  |
| ReplicationBytes |  | Bytes | Multi | CacheClusterId |  |
| ReplicationLag | This metric is only applicable for a node running as a read replica. It represents how far behind, in seconds, the replica is in applying changes from the primary node. | Seconds | Multi | CacheClusterId, CacheNodeId |  |
| ReplicationLag |  | Seconds | Multi | CacheClusterId |  |
| SaveInProgress | This binary metric returns 1 whenever a background save (forked or forkless) is in progress, and 0 otherwise. | Count | Multi | CacheClusterId, CacheNodeId |  |
| SaveInProgress |  | Count | Multi | CacheClusterId |  |
| SetBasedCmds | The total number of commands that are set-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more sets (scard, sdiff, sadd, sunion, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| SetBasedCmds |  | Count | Sum | CacheClusterId |  |
| SetTypeCmds | The total number of write types of commands. This is derived from the Redis commandstats statistic by summing all of the mutative types of commands that operate on data (set, hset, sadd, lpop, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| SetTypeCmds |  | Count | Sum | CacheClusterId |  |
| SlabsMoved | The total number of slab pages that have been moved | Count | Sum | CacheClusterId, CacheNodeId |  |
| SlabsMoved |  | Count | Sum | CacheClusterId |  |
| SortedSetBasedCmds | The total number of commands that are sorted set-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more sorted sets (zcount, zrange, zrank, zadd, and so on). | Count | Sum | CacheClusterId, CacheNodeId |  |
| SortedSetBasedCmds | The total number of commands that are string-based. This is derived from the Redis commandstats statistic by summing all of the commands that act upon one or more strings (strlen, setex, setrange, and so on). | Count | Sum | CacheClusterId |  |
| StringBasedCmds |  | Count | Sum | CacheClusterId, CacheNodeId |  |
| StringBasedCmds |  | Count | Sum | CacheClusterId |  |
| SwapUsage | The amount of swap used on the host | Bytes | Multi | CacheClusterId, CacheNodeId |  |
| SwapUsage |  | Bytes | Multi | CacheClusterId | Applicable |
| TouchHits | The number of keys that have been touched and were given a new expiration time | Count | Sum | CacheClusterId, CacheNodeId |  |
| TouchHits |  | Count | Sum | CacheClusterId |  |
| TouchMisses | The number of items that have been touched, but were not found | Count | Sum | CacheClusterId, CacheNodeId |  |
| TouchMisses |  | Count | Sum | CacheClusterId |  |
| UnusedMemory | The amount of memory not used by data. This is derived from the Memcached statistics limit\_maxbytes and bytes by subtracting bytes from limit\_maxbytes. | Bytes | Sum | CacheClusterId, CacheNodeId |  |
| UnusedMemory |  | Bytes | Sum | CacheClusterId |  |