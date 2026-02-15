---
title: Amazon EMR (Elastic MapReduce) monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elastic-mapreduce-emr
scraped: 2026-02-15T21:24:38.814686
---

# Amazon EMR (Elastic MapReduce) monitoring

# Amazon EMR (Elastic MapReduce) monitoring

* How-to guide
* 12-min read
* Published Oct 15, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon EMR. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

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

`JobFlowId` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| AppsCompleted | The number of applications submitted to YARN that have completed | Count | Sum | JobFlowId, JobId |  |
| AppsCompleted |  | Count | Sum | JobFlowId |  |
| AppsFailed | The number of applications submitted to YARN that have failed to complete | Count | Sum | JobFlowId, JobId |  |
| AppsFailed |  | Count | Sum | JobFlowId |  |
| AppsKilled | The number of applications submitted to YARN that have been killed | Count | Sum | JobFlowId, JobId |  |
| AppsKilled |  | Count | Sum | JobFlowId |  |
| AppsPending | The number of applications submitted to YARN that are in a Pending state | Count | Sum | JobFlowId, JobId |  |
| AppsPending |  | Count | Sum | JobFlowId |  |
| AppsRunning | The number of applications submitted to YARN that are running | Count | Sum | JobFlowId, JobId | Applicable |
| AppsRunning |  | Count | Sum | JobFlowId | Applicable |
| AppsSubmitted | The number of applications submitted to YARN | Count | Sum | JobFlowId, JobId |  |
| AppsSubmitted |  | Count | Sum | JobFlowId |  |
| BackupFailed | Shows if the last backup failed. Set to `0` by default and updated to `1` if the previous backup attempt failed. This metric is only reported for HBase clusters. | Count | Sum | JobFlowId, JobId |  |
| BackupFailed |  | Count | Sum | JobFlowId |  |
| CapacityRemainingGB | The amount of remaining HDFS disk capacity | Count | Sum | JobFlowId, JobId |  |
| CapacityRemainingGB |  | Count | Sum | JobFlowId |  |
| ContainerAllocated | The number of resource containers allocated by the resource manager | Count | Sum | JobFlowId, JobId |  |
| ContainerAllocated |  | Count | Sum | JobFlowId |  |
| ContainerPendingRatio | The ratio (in numbers) of pending containers to containers allocated (`ContainerPendingRatio` = `ContainerPending` / `ContainerAllocated`). If `ContainerAllocated` = `0`, then `ContainerPendingRatio` = `ContainerPending`. | Count | Sum | JobFlowId, JobId |  |
| ContainerPendingRatio |  | Count | Sum | JobFlowId |  |
| ContainerPending | The number of containers in the queue that have not yet been allocated | Count | Sum | JobFlowId, JobId |  |
| ContainerPending |  | Count | Sum | JobFlowId |  |
| ContainerReserved | The number of containers reserved | Count | Sum | JobFlowId, JobId |  |
| ContainerReserved |  | Count | Sum | JobFlowId |  |
| CoreNodesPending | The number of core nodes waiting to be assigned (pending requests) | Count | Sum | JobFlowId, JobId |  |
| CoreNodesPending |  | Count | Sum | JobFlowId |  |
| CoreNodesRequested |  | Count | Sum | JobFlowId, JobId |  |
| CoreNodesRequested |  | Count | Sum | JobFlowId |  |
| CoreNodesRunning | The number of working core nodes | Count | Sum | JobFlowId, JobId |  |
| CoreNodesRunning |  | Count | Sum | JobFlowId |  |
| CoreUnitsRequested |  | Count | Sum | JobFlowId, JobId |  |
| CoreUnitsRequested |  | Count | Sum | JobFlowId |  |
| CoreUnitsRunning |  | Count | Sum | JobFlowId, JobId |  |
| CoreUnitsRunning |  | Count | Sum | JobFlowId |  |
| CoreVCPURequested |  | Count | Sum | JobFlowId, JobId |  |
| CoreVCPURequested |  | Count | Sum | JobFlowId |  |
| CoreVCPURunning |  | Count | Sum | JobFlowId, JobId |  |
| CoreVCPURunning |  | Count | Sum | JobFlowId |  |
| CorruptBlocks | The number of blocks that HDFS reports as corrupted | Count | Sum | JobFlowId, JobId |  |
| CorruptBlocks |  | Count | Sum | JobFlowId |  |
| DfsPendingReplicationBlocks | The status of block replication: blocks being replicated, age of replication requests, and unsuccessful replication requests | Count | Sum | JobFlowId, JobId |  |
| DfsPendingReplicationBlocks |  | Count | Sum | JobFlowId |  |
| HDFSBytesRead | The number of bytes read from HDFS | Count | Sum | JobFlowId, JobId |  |
| HDFSBytesRead |  | Count | Sum | JobFlowId |  |
| HDFSBytesWritten | The number of bytes written to HDFS | Count | Sum | JobFlowId, JobId |  |
| HDFSBytesWritten |  | Count | Sum | JobFlowId |  |
| HDFSUtilization | The percentage of HDFS storage currently used | Percent | Average | JobFlowId, JobId | Applicable |
| HDFSUtilization |  | Percent | Average | JobFlowId | Applicable |
| HbaseBackupFailed | Shows if the last backup failed. Set to `0` by default and updated to `1` if the previous backup attempt failed. This metric is only reported for HBase clusters. | Count | Minimum | JobFlowId, JobId |  |
| HbaseBackupFailed |  | Count | Minimum | JobFlowId |  |
| IsIdle | Indicates that a cluster is no longer performing work, but is still alive and accruing charges. Set to `1` if no tasks are running and no jobs are running, and to `0` otherwise. This value is checked at five-minute intervals and a value of `1` indicates only that the cluster was idle when checked, not that it was idle for the entire five minutes. | Count | Minimum | JobFlowId, JobId | Applicable |
| IsIdle |  | Count | Minimum | JobFlowId | Applicable |
| JobsFailed | The number of jobs in the cluster that have failed | Count | Sum | JobFlowId, JobId |  |
| JobsFailed |  | Count | Sum | JobFlowId |  |
| JobsRunning | The number of jobs in the cluster that are currently running | Count | Sum | JobFlowId, JobId |  |
| JobsRunning |  | Count | Sum | JobFlowId |  |
| LiveDataNodes | The percentage of data nodes that are receiving work from Hadoop | Count | Sum | JobFlowId, JobId |  |
| LiveDataNodes |  | Count | Sum | JobFlowId |  |
| LiveTaskTrackers | The percentage of task trackers that are functional | Percent | Average | JobFlowId, JobId |  |
| LiveTaskTrackers |  | Percent | Average | JobFlowId |  |
| MRActiveNodes | The number of nodes presently running MapReduce tasks or jobs. Equivalent to YARN metric `mapred.resourcemanager.NoOfActiveNodes` | Count | Sum | JobFlowId, JobId |  |
| MRActiveNodes |  | Count | Sum | JobFlowId |  |
| MRDecommissionedNodes | The number of nodes allocated to MapReduce applications that have been marked in a **Decommissioned** state | Count | Sum | JobFlowId, JobId |  |
| MRDecommissionedNodes |  | Count | Sum | JobFlowId |  |
| MRLostNodes | The number of nodes allocated to MapReduce that have been marked in a **Lost** state | Count | Sum | JobFlowId, JobId |  |
| MRLostNodes |  | Count | Sum | JobFlowId |  |
| MRRebootedNodes | The number of nodes available to MapReduce that have been rebooted and marked in a **Rebooted** state | Count | Sum | JobFlowId, JobId |  |
| MRRebootedNodes |  | Count | Sum | JobFlowId |  |
| MRTotalNodes | The number of nodes presently available to MapReduce jobs | Count | Sum | JobFlowId, JobId |  |
| MRTotalNodes |  | Count | Sum | JobFlowId |  |
| MRUnhealthyNodes | The number of nodes available to MapReduce jobs marked in an **Unhealthy** state | Count | Sum | JobFlowId, JobId |  |
| MRUnhealthyNodes |  | Count | Sum | JobFlowId |  |
| MapSlotsOpen | The unused map task capacity. This is calculated as the maximum number of map tasks for a given cluster, less the total number of map tasks currently running in that cluster. | Count | Sum | JobFlowId, JobId |  |
| MapSlotsOpen |  | Count | Sum | JobFlowId |  |
| MapTasksRemaining | The number of remaining map tasks for each job | Count | Sum | JobFlowId, JobId |  |
| MapTasksRemaining |  | Count | Sum | JobFlowId |  |
| MapTasksRunning | The number of running map tasks for each job | Count | Sum | JobFlowId, JobId | Applicable |
| MapTasksRunning |  | Count | Sum | JobFlowId | Applicable |
| MemoryAllocatedMB | The amount of memory allocated to the cluster | Count | Sum | JobFlowId, JobId |  |
| MemoryAllocatedMB |  | Count | Sum | JobFlowId |  |
| MemoryAvailableMB | The amount of memory available for allocation | Count | Sum | JobFlowId, JobId |  |
| MemoryAvailableMB |  | Count | Sum | JobFlowId |  |
| MemoryReservedMB | The amount of memory reserved for allocation | Count | Sum | JobFlowId, JobId |  |
| MemoryReservedMB |  | Count | Sum | JobFlowId |  |
| MemoryTotalMB | The total amount of memory in the cluster | Count | Sum | JobFlowId, JobId |  |
| MemoryTotalMB |  | Count | Sum | JobFlowId |  |
| MissingBlocks | The number of blocks in which HDFS has no replicas. These might be corrupt blocks. | Count | Sum | JobFlowId, JobId |  |
| MissingBlocks |  | Count | Sum | JobFlowId |  |
| MostRecentBackupDuration | The amount of time it took the previous backup to complete. This metric is set regardless of whether the last completed backup succeeded or failed. While the backup is ongoing, this metric returns the number of minutes after the backup started. This metric is only reported for HBase clusters. | Count | Sum | JobFlowId, JobId |  |
| MostRecentBackupDuration |  | Count | Sum | JobFlowId |  |
| PendingDeletionBlocks | The number of blocks marked for deletion | Count | Sum | JobFlowId, JobId |  |
| PendingDeletionBlocks |  | Count | Sum | JobFlowId |  |
| ReduceSlotsOpen | Unused reduce task capacity. This is calculated as the maximum reduce task capacity for a given cluster, less the number of reduce tasks currently running in that cluster. | Count | Sum | JobFlowId, JobId |  |
| ReduceSlotsOpen |  | Count | Sum | JobFlowId |  |
| ReduceTasksRemaining | The number of remaining reduce tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated. | Count | Sum | JobFlowId |  |
| ReduceTasksRunning | The number of running reduce tasks for each job. If you have a scheduler installed and multiple jobs running, multiple graphs are generated. | Count | Sum | JobFlowId, JobId |  |
| ReduceTasksRunning |  | Count | Sum | JobFlowId |  |
| RemainingMapTasksPerSlot | The ratio of the total map tasks remaining to the total map slots available in the cluster | Percent | Average | JobFlowId, JobId |  |
| RemainingMapTasksPerSlot |  | Percent | Average | JobFlowId |  |
| S3BytesRead | The number of bytes read from Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on EMR. | Count | Sum | JobFlowId, JobId |  |
| S3BytesRead |  | Count | Sum | JobFlowId |  |
| S3BytesWritten | The number of bytes written to Amazon S3. This metric aggregates MapReduce jobs only, and does not apply for other workloads on EMR. | Count | Sum | JobFlowId, JobId |  |
| S3BytesWritten |  | Count | Sum | JobFlowId |  |
| TaskNodesPending | The number of task nodes waiting to be assigned (pending requests) | Count | Sum | JobFlowId, JobId |  |
| TaskNodesPending |  | Count | Sum | JobFlowId |  |
| TaskNodesRequested |  | Count | Sum | JobFlowId, JobId |  |
| TaskNodesRequested |  | Count | Sum | JobFlowId |  |
| TaskNodesRunning | The number of working task nodes | Count | Sum | JobFlowId, JobId |  |
| TaskNodesRunning |  | Count | Sum | JobFlowId |  |
| TaskUnitsRequested |  | Count | Sum | JobFlowId, JobId |  |
| TaskUnitsRequested |  | Count | Sum | JobFlowId |  |
| TaskUnitsRunning |  | Count | Sum | JobFlowId, JobId |  |
| TaskUnitsRunning |  | Count | Sum | JobFlowId |  |
| TaskVCPURequested |  | Count | Sum | JobFlowId, JobId |  |
| TaskVCPURequested |  | Count | Sum | JobFlowId |  |
| TaskVCPURunning |  | Count | Sum | JobFlowId, JobId |  |
| TaskVCPURunning |  | Count | Sum | JobFlowId |  |
| TimeSinceLastSuccessfulBackup | The number of elapsed minutes after the last successful HBase backup started on your cluster. This metric is only reported for HBase clusters. | Count | Sum | JobFlowId, JobId |  |
| TimeSinceLastSuccessfulBackup |  | Count | Sum | JobFlowId |  |
| TotalLoad | The total number of concurrent data transfers | Count | Sum | JobFlowId, JobId |  |
| TotalLoad |  | Count | Sum | JobFlowId |  |
| TotalNodesRequested |  | Count | Sum | JobFlowId, JobId |  |
| TotalNodesRequested |  | Count | Sum | JobFlowId |  |
| TotalNodesRunning |  | Count | Sum | JobFlowId, JobId |  |
| TotalNodesRunning |  | Count | Sum | JobFlowId |  |
| TotalUnitsRequested |  | Count | Sum | JobFlowId, JobId |  |
| TotalUnitsRequested |  | Count | Sum | JobFlowId |  |
| TotalUnitsRunning |  | Count | Sum | JobFlowId, JobId |  |
| TotalUnitsRunning |  | Count | Sum | JobFlowId |  |
| TotalVCPURequested |  | Count | Sum | JobFlowId |  |
| TotalVCPURunning |  | Count | Sum | JobFlowId, JobId |  |
| TotalVCPURunning |  | Count | Sum | JobFlowId |  |
| UnderReplicatedBlocks | The number of blocks that need to be replicated one or more times | Count | Sum | JobFlowId, JobId |  |
| UnderReplicatedBlocks |  | Count | Sum | JobFlowId |  |
| YARNMemoryAvailablePercentage | he percentage of remaining memory available to YARN (`YARNMemoryAvailablePercentage` = `MemoryAvailableMB` / `MemoryTotalMB`) | Percent | Average | JobFlowId, JobId |  |
| YARNMemoryAvailablePercentage |  | Percent | Average | JobFlowId |  |