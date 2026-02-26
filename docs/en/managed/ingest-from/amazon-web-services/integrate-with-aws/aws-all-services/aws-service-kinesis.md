---
title: Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams) monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-kinesis
scraped: 2026-02-26T21:20:48.678419
---

# Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams) monitoring

# Amazon Kinesis (Data Analytics, Data Firehose, Data Streams, Video Streams) monitoring

* How-to guide
* 33-min read
* Updated on Jan 10, 2025

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon Kinesis. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

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

### Amazon Kinesis Data Analytics

`Application` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| Bytes | The number of bytes read (per input stream) or written (per output stream). | Bytes | Sum | Application, Flow, Id | Applicable |
| InputProcessing.DroppedRecords | The number of records returned by a Lambda function that were marked with `Dropped` status. | Count | Sum | Application, Flow, Id |  |
| InputProcessing.Duration | The time taken for each AWS Lambda function invocation performed by Kinesis Data Analytics. | Milliseconds | Multi | Application, Flow, Id |  |
| InputProcessing.OkBytes | The sum of bytes of the records returned by a Lambda function that were marked with `OK` status. | Bytes | Sum | Application, Flow, Id |  |
| InputProcessing.OkRecords | The number of records returned by a Lambda function that were marked with `OK` status. | Count | Sum | Application, Flow, Id |  |
| InputProcessing.ProcessingFailedRecords | The number of records returned by a Lambda function that were marked with `ProcessingFailed` status. | Count | Sum | Application, Flow, Id |  |
| InputProcessing.Success | The number of successful Lambda invocations by Kinesis Data Analytics. | Count | Sum | Application, Flow, Id |  |
| KPUs | The number of Kinesis Processing Units that are used to run your stream processing application. | Count | Count | Application |  |
| KPUs |  | Count | Multi | Application |  |
| KPUs |  | Count | Sum | Application | Applicable |
| LambdaDelivery.DeliveryFailedRecords | The number of successful Lambda invocations by Kinesis Data Analytics. | Count | Sum | Application, Flow, Id |  |
| LambdaDelivery.Duration | The time taken for each Lambda function invocation performed by Kinesis Data Analytics. | Milliseconds | Multi | Application, Flow, Id |  |
| LambdaDelivery.OkRecords | The number of records returned by a Lambda function that were marked with `OK` status. | Count | Sum | Application, Flow, Id |  |
| MillisBehindLatest | Indicates how far behind from the current time an application is reading from the streaming source. | Milliseconds | Multi | Application; Application, Flow, Id |  |
| Records | The number of records read (per input stream) or written (per output stream). | Count | Sum | Application, Flow, Id | Applicable |
| Success | The number of successful deliveries. Every successful delivery attempt to the destination configured for your application is marked with `1`. Every failed delivery attempt is marked with `0`. | Count | Average | Application, Flow, Id | Applicable |
| backPressuredTimeMsPerSecond | The time (in milliseconds) this task or operator is back pressured per second. | Milliseconds | Count | Application |  |
| backPressuredTimeMsPerSecond |  | Milliseconds | Multi | Application |  |
| backPressuredTimeMsPerSecond |  | Milliseconds | Sum | Application |  |
| busyTimeMsPerSecond | The time (in milliseconds) this task or operator is busy (neither idle nor back pressured) per second. Can be NaN, if the value could not be calculated. | Milliseconds | Count | Application |  |
| busyTimeMsPerSecond |  | Milliseconds | Multi | Application |  |
| busyTimeMsPerSecond |  | Milliseconds | Sum | Application |  |
| bytes\_consumed\_rate | The average number of bytes consumed per second for a topic. | Bytes | Count | Application |  |
| bytes\_consumed\_rate |  | Bytes | Multi | Application |  |
| bytes\_consumed\_rate |  | Bytes | Sum | Application |  |
| commitsFailed | The total number of offset commit failures to Kafka, if offset committing and checkpointing are enabled. | Count | Count | Application |  |
| commitsFailed |  | Count | Multi | Application |  |
| commitsFailed |  | Count | Sum | Application |  |
| commitsSucceeded | The total number of successful offset commits to Kafka, if offset committing and checkpointing are enabled. | Count | Count | Application |  |
| commitsSucceeded |  | Count | Multi | Application |  |
| commitsSucceeded |  | Count | Sum | Application |  |
| committedOffsets | The last successfully committed offsets to Kafka, for each partition. A particular partition's metric can be specified by topic name and partition id. | Count | Count | Application |  |
| committedOffsets |  | Count | Multi | Application |  |
| committedOffsets |  | Count | Sum | Application |  |
| containerCPUUtilization | Overall percentage of CPU utilization across task manager containers in Flink application cluster. | Percent | Count | Application |  |
| containerCPUUtilization |  | Percent | Multi | Application |  |
| containerCPUUtilization |  | Percent | Sum | Application |  |
| containerDiskUtilization | Overall percentage of disk utilization across task manager containers in Flink application cluster. | Percent | Count | Application |  |
| containerDiskUtilization |  | Percent | Multi | Application |  |
| containerDiskUtilization |  | Percent | Sum | Application |  |
| containerMemoryUtilization | Overall percentage of memory utilization across task manager containers in Flink application cluster. | Percent | Count | Application |  |
| containerMemoryUtilization |  | Percent | Multi | Application |  |
| containerMemoryUtilization |  | Percent | Sum | Application |  |
| cpuUtilization | Overall percentage of CPU utilization across task managers. | Percent | Count | Application |  |
| cpuUtilization |  | Percent | Multi | Application |  |
| cpuUtilization |  | Percent | Sum | Application |  |
| currentInputWatermark | The last watermark this application/operator/task/thread has received. | Milliseconds | Count | Application |  |
| currentInputWatermark |  | Milliseconds | Multi | Application |  |
| currentInputWatermark |  | Milliseconds | Sum | Application |  |
| currentOffsets | The consumer's current read offset, for each partition. A particular partition's metric can be specified by topic name and partition id. | Count | Count | Application |  |
| currentOffsets |  | Count | Multi | Application |  |
| currentOffsets |  | Count | Sum | Application |  |
| currentOutputWatermark | The last watermark this application/operator/task/thread has emitted. | Milliseconds | Count | Application |  |
| currentOutputWatermark |  | Milliseconds | Multi | Application |  |
| currentOutputWatermark |  | Milliseconds | Sum | Application |  |
| downtime | For jobs currently in a failing/recovering situation, the time elapsed during this outage. | Milliseconds | Count | Application |  |
| downtime |  | Milliseconds | Multi | Application |  |
| downtime |  | Milliseconds | Sum | Application |  |
| fullRestarts | The total number of times this job has fully restarted since it was submitted. This metric does not measure fine-grained restarts. | Count | Count | Application |  |
| fullRestarts |  | Count | Multi | Application |  |
| fullRestarts |  | Count | Sum | Application |  |
| heapMemoryUtilization | Overall heap memory utilization across task managers. | Percent | Count | Application |  |
| heapMemoryUtilization |  | Percent | Multi | Application |  |
| heapMemoryUtilization |  | Percent | Sum | Application |  |
| idleTimeMsPerSecond | The time (in milliseconds) this task or operator is idle (has no data to process) per second. Idle time excludes back pressured time, so if the task is back pressured it is not idle. | Milliseconds | Count | Application |  |
| idleTimeMsPerSecond |  | Milliseconds | Multi | Application |  |
| idleTimeMsPerSecond |  | Milliseconds | Sum | Application |  |
| lastCheckpointDuration | The time it took to complete the last checkpoint. | Milliseconds | Count | Application |  |
| lastCheckpointDuration |  | Milliseconds | Multi | Application |  |
| lastCheckpointDuration |  | Milliseconds | Sum | Application |  |
| lastCheckpointSize | The total size of the last checkpoint | Bytes | Count | Application |  |
| lastCheckpointSize |  | Bytes | Multi | Application |  |
| lastCheckpointSize |  | Bytes | Sum | Application |  |
| numRecordsInPerSecond | The total number of records this application, operator or task has received per second. | Count/Second | Count | Application |  |
| numRecordsInPerSecond |  | Count/Second | Multi | Application |  |
| numRecordsInPerSecond |  | Count/Second | Sum | Application |  |
| numRecordsIn | The total number of records this application, operator, or task has received. | Count | Count | Application |  |
| numRecordsIn |  | Count | Multi | Application |  |
| numRecordsIn |  | Count | Sum | Application |  |
| numRecordsOutPerSecond | The total number of records this application, operator or task has emitted per second. | Count/Second | Count | Application |  |
| numRecordsOutPerSecond |  | Count/Second | Multi | Application |  |
| numRecordsOutPerSecond |  | Count/Second | Sum | Application |  |
| numRecordsOut | The total number of records this application, operator or task has emitted. | Count | Count | Application |  |
| numRecordsOut |  | Count | Multi | Application |  |
| numRecordsOut |  | Count | Sum | Application |  |
| numRestarts |  | Count | Count | Application |  |
| numRestarts |  | Count | Multi | Application |  |
| numRestarts |  | Count | Sum | Application |  |
| numberOfFailedCheckpoints | The number of times checkpointing has failed. | Count | Count | Application |  |
| numberOfFailedCheckpoints |  | Count | Multi | Application |  |
| numberOfFailedCheckpoints |  | Count | Sum | Application |  |
| oldGenerationGCCount | The total number of old garbage collection operations that have occurred across all task managers. | Count | Count | Application |  |
| oldGenerationGCCount |  | Count | Multi | Application |  |
| oldGenerationGCCount |  | Count | Sum | Application |  |
| oldGenerationGCTime | The total time spent performing old garbage collection operations. | Milliseconds | Count | Application |  |
| oldGenerationGCTime |  | Milliseconds | Multi | Application |  |
| oldGenerationGCTime |  | Milliseconds | Sum | Application |  |
| processElementavg |  | Count | Count | Application, Service |  |
| processElementavg |  | Count | Multi | Application, Service |  |
| processElementavg |  | Count | Sum | Application, Service |  |
| readDocsavg |  | Count | Count | Application, Service |  |
| readDocsavg |  | Count | Multi | Application, Service |  |
| readDocsavg |  | Count | Sum | Application, Service |  |
| records\_lag\_max | The maximum lag in terms of number of records for any partition in this window | Count | Count | Application |  |
| records\_lag\_max |  | Count | Multi | Application |  |
| records\_lag\_max |  | Count | Sum | Application |  |
| threadsCount |  | Count | Count | Application |  |
| threadsCount |  | Count | Multi | Application |  |
| threadsCount |  | Count | Sum | Application |  |
| updatesavg |  | Count | Count | Application, Service |  |
| updatesavg |  | Count | Multi | Application, Service |  |
| updatesavg |  | Count | Sum | Application, Service |  |
| uptime | The time that the job has been running without interruption. | Milliseconds | Count | Application |  |
| uptime |  | Milliseconds | Multi | Application |  |
| uptime |  | Milliseconds | Sum | Application |  |

### Amazon Data Firehose

`DeliveryStreamName` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| BackupToS3.Bytes | The number of bytes delivered to Amazon S3 for backup over the specified time period. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled. | Bytes | Sum | Region |  |
| BackupToS3.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| BackupToS3.DataFreshness | Age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose. Any record older than this age has been delivered to the Amazon S3 bucket for backup. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled. | Seconds | Maximum | Region |  |
| BackupToS3.DataFreshness |  | Seconds | Maximum | DeliveryStreamName |  |
| BackupToS3.Records | The number of records delivered to Amazon S3 for backup over the specified time period. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled. | Count | Sum | Region |  |
| BackupToS3.Records |  | Count | Sum | DeliveryStreamName |  |
| BackupToS3.Success | Sum of successful Amazon S3 put commands for backup over sum of all Amazon S3 backup put commands. Amazon Data Firehose emits this metric when backup to Amazon S3 is enabled. | Count | Count | Region |  |
| BackupToS3.Success |  | Count | Count | DeliveryStreamName |  |
| DataReadFromKinesisStream.Bytes | When the data source is a Kinesis data stream, this metric indicates the number of bytes read from that data stream. This number includes rereads due to failovers. | Bytes | Sum | Region |  |
| DataReadFromKinesisStream.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DataReadFromKinesisStream.Records | When the data source is a Kinesis data stream, this metric indicates the number of records read from that data stream. This number includes rereads due to failovers. | Count | Sum | Region |  |
| DataReadFromKinesisStream.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Bytes | The number of bytes indexed to Amazon ES over the specified time period | Bytes | Sum | Region |  |
| DeliveryToElasticsearch.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Records | The number of records indexed to Amazon ES over the specified time period | Count | Sum | Region |  |
| DeliveryToElasticsearch.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToElasticsearch.Success | The sum of the successfully indexed records over the sum of records that were attempted | Count | Count | Region |  |
| DeliveryToElasticsearch.Success |  | Count | Count | DeliveryStreamName |  |
| DeliveryToRedshift.Bytes | The number of bytes copied to Amazon Redshift over the specified time period | Bytes | Sum | Region |  |
| DeliveryToRedshift.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToRedshift.Records | The number of records copied to Amazon Redshift over the specified time period | Count | Sum | Region |  |
| DeliveryToRedshift.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToRedshift.Success | The sum of successful Amazon Redshift `COPY` commands over the sum of all Amazon Redshift `COPY` commands | Count | Count | Region |  |
| DeliveryToRedshift.Success |  | Count | Count | DeliveryStreamName |  |
| DeliveryToS3.Bytes | The number of bytes delivered to Amazon S3 over the specified time period | Bytes | Sum | Region |  |
| DeliveryToS3.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToS3.DataFreshness | The age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose. Any record older than this age has been delivered to the S3 bucket. | Seconds | Maximum | Region |  |
| DeliveryToS3.DataFreshness |  | Seconds | Maximum | DeliveryStreamName |  |
| DeliveryToS3.Records | The number of records delivered to Amazon S3 over the specified time period | Count | Sum | Region |  |
| DeliveryToS3.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToS3.Success | The sum of successful Amazon S3 put commands over the sum of all Amazon S3 put commands | Count | Count | Region |  |
| DeliveryToS3.Success |  | Count | Count | DeliveryStreamName |  |
| DeliveryToSplunk.Bytes | The number of bytes delivered to Splunk over the specified time period | Bytes | Sum | Region |  |
| DeliveryToSplunk.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| DeliveryToSplunk.DataAckLatency | The approximate duration it takes to receive an acknowledgment from Splunk after Amazon Data Firehose sends it data | Seconds | Average | Region |  |
| DeliveryToSplunk.DataAckLatency |  | Seconds | Average | DeliveryStreamName |  |
| DeliveryToSplunk.DataFreshness | Age (from getting into Amazon Data Firehose to now) of the oldest record in Amazon Data Firehose. Any record older than this age has been delivered to Splunk. | Seconds | Maximum | Region |  |
| DeliveryToSplunk.DataFreshness |  | Seconds | Maximum | DeliveryStreamName |  |
| DeliveryToSplunk.Records | The number of records delivered to Splunk over the specified time period | Count | Sum | Region |  |
| DeliveryToSplunk.Records |  | Count | Sum | DeliveryStreamName |  |
| DeliveryToSplunk.Success | The sum of the successfully indexed records over the sum of records that were attempted | Count | Count | Region |  |
| DeliveryToSplunk.Success |  | Count | Count | DeliveryStreamName |  |
| DescribeDeliveryStream.Latency | The time taken per `DescribeDeliveryStream` operation, measured over the specified time period | Milliseconds | Multi | Region |  |
| DescribeDeliveryStream.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| DescribeDeliveryStream.Requests | The total number of `DescribeDeliveryStream` requests | Count | Sum | Region |  |
| DescribeDeliveryStream.Requests |  | Count | Sum | DeliveryStreamName |  |
| ExecuteProcessing.Duration | The time it takes for each Lambda function invocation performed by Amazon Data Firehose | Milliseconds | Multi | Region |  |
| ExecuteProcessing.Duration |  | Milliseconds | Multi | DeliveryStreamName |  |
| ExecuteProcessing.Success | The sum of the successful Lambda function invocations over the sum of the total Lambda function invocations | Count | Count | Region |  |
| ExecuteProcessing.Success |  | Count | Count | DeliveryStreamName |  |
| FailedConversion.Bytes | The size of the records that could not be converted | Bytes | Sum | Region |  |
| FailedConversion.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| FailedConversion.Records | The number of records that could not be converted | Count | Sum | Region |  |
| FailedConversion.Records |  | Count | Sum | DeliveryStreamName |  |
| IncomingBytes | The number of bytes ingested successfully into the delivery stream over the specified time period after throttling | Bytes | Sum | Region |  |
| IncomingBytes |  | Bytes | Sum | DeliveryStreamName | Applicable |
| IncomingRecords | The number of records ingested successfully into the delivery stream over the specified time period after throttling | Count | Sum | Region |  |
| IncomingRecords |  | Count | Sum | DeliveryStreamName | Applicable |
| KinesisMillisBehindLatest | When the data source is a Kinesis data stream, this metric indicates the number of milliseconds that the last read record is behind the newest record in the Kinesis data stream | Milliseconds | Average | Region |  |
| KinesisMillisBehindLatest |  | Milliseconds | Average | DeliveryStreamName |  |
| ListDeliveryStreams.Latency | The time taken per `ListDeliveryStream` operation, measured over the specified time period | Milliseconds | Multi | Region |  |
| ListDeliveryStreams.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| ListDeliveryStreams.Requests | The total number of `ListFirehose` requests | Count | Sum | Region |  |
| ListDeliveryStreams.Requests |  | Count | Sum | DeliveryStreamName |  |
| PutRecordBatch.Bytes | The number of bytes put to the Amazon Data Firehose delivery stream using `PutRecordBatch` over the specified time period | Bytes | Sum | Region |  |
| PutRecordBatch.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| PutRecordBatch.Latency | The time taken per `PutRecordBatch` operation, measured over the specified time period | Milliseconds | Multi | Region |  |
| PutRecordBatch.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| PutRecordBatch.Records | The total number of records from `PutRecordBatch` operations | Count | Sum | Region |  |
| PutRecordBatch.Records |  | Count | Sum | DeliveryStreamName |  |
| PutRecordBatch.Requests | The total number of `PutRecordBatch` requests | Count | Sum | Region |  |
| PutRecordBatch.Requests |  | Count | Sum | DeliveryStreamName |  |
| PutRecord.Bytes | The number of bytes put to the Amazon Data Firehose delivery stream using `PutRecord` over the specified time period | Bytes | Sum | Region |  |
| PutRecord.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| PutRecord.Latency | The time taken per `PutRecord` operation, measured over the specified time period | Milliseconds | Multi | Region |  |
| PutRecord.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| PutRecord.Requests | The total number of `PutRecord` requests, which is equal to the total number of records from `PutRecord` operations | Count | Sum | Region |  |
| PutRecord.Requests |  | Count | Sum | DeliveryStreamName |  |
| SucceedConversion.Bytes | The size of the successfully converted records | Bytes | Sum | Region |  |
| SucceedConversion.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| SucceedConversion.Records | The number of successfully converted records | Count | Sum | Region |  |
| SucceedConversion.Records |  | Count | Sum | DeliveryStreamName |  |
| SucceedProcessing.Bytes | The number of successfully processed bytes over the specified time period | Bytes | Sum | Region |  |
| SucceedProcessing.Bytes |  | Bytes | Sum | DeliveryStreamName |  |
| SucceedProcessing.Records | The number of successfully processed records over the specified time period | Count | Sum | Region |  |
| SucceedProcessing.Records |  | Count | Sum | DeliveryStreamName |  |
| ThrottledDescribeStream | The total number of times the `DescribeStream` operation is throttled when the data source is a Kinesis data stream | Count | Average | Region |  |
| ThrottledDescribeStream |  | Count | Average | DeliveryStreamName |  |
| ThrottledGetRecords | The total number of times the `GetRecords` operation is throttled when the data source is a Kinesis data stream | Count | Average | Region |  |
| ThrottledGetRecords |  | Count | Average | DeliveryStreamName |  |
| ThrottledGetShardIterator | The total number of times the `GetShardIterator` operation is throttled when the data source is a Kinesis data stream | Count | Average | Region |  |
| ThrottledGetShardIterator |  | Count | Average | DeliveryStreamName |  |
| UpdateDeliveryStream.Latency | The time taken per `UpdateDeliveryStream` operation, measured over the specified time period | Milliseconds | Multi | Region |  |
| UpdateDeliveryStream.Latency |  | Milliseconds | Multi | DeliveryStreamName |  |
| UpdateDeliveryStream.Requests | The total number of `UpdateDeliveryStream` requests | Count | Sum | Region |  |
| UpdateDeliveryStream.Requests |  | Count | Sum | DeliveryStreamName |  |

### Amazon Kinesis Data Streams (KDS)

`StreamName` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| GetRecords.Bytes | The number of bytes retrieved from the Kinesis stream, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes in a single `GetRecords` operation for the stream in the specified time period. | Bytes | Sum | StreamName |  |
| GetRecords.Bytes |  | Bytes | Multi | StreamName |  |
| GetRecords.Bytes |  | Bytes | Count | StreamName |  |
| GetRecords.IteratorAgeMilliseconds | The age of the last record in all `GetRecords` calls made against a Kinesis stream, measured over the specified time period. Age is the difference between the current time and when the last record of the `GetRecords` call was written to the stream. The minimum and maximum statistics can be used to track the progress of Kinesis consumer applications. A value of `0` indicates that the records being read are completely caught up with the stream. | Milliseconds | Multi | StreamName | Applicable |
| GetRecords.IteratorAgeMilliseconds |  | Milliseconds | Count | StreamName |  |
| GetRecords.Latency | The time taken per GetRecords operation, measured over the specified time period | Milliseconds | Multi | StreamName |  |
| GetRecords.Records | The number of records retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records in a single `GetRecords` operation for the stream in the specified time period. | Count | Sum | StreamName |  |
| GetRecords.Records |  | Count | Multi | StreamName |  |
| GetRecords.Records |  | Count | Count | StreamName |  |
| GetRecords.Success | The number of successful `GetRecords` operations per stream, measured over the specified time period | Count | Sum | StreamName |  |
| GetRecords.Success |  | Count | Average | StreamName | Applicable |
| GetRecords.Success |  | Count | Count | StreamName |  |
| IncomingBytes | The number of bytes successfully put to the Kinesis stream over the specified time period. This metric includes bytes from `PutRecord` and `PutRecords` operations. Minimum, maximum, and average statistics represent the bytes in a single put operation for the stream in the specified time period. | Bytes | Count | ShardId, StreamName |  |
| IncomingBytes |  | Bytes | Count | StreamName |  |
| IncomingBytes |  | Bytes | Multi | ShardId, StreamName |  |
| IncomingBytes |  | Bytes | Multi | StreamName |  |
| IncomingBytes |  | Bytes | Sum | ShardId, StreamName |  |
| IncomingBytes |  | Bytes | Sum | StreamName |  |
| IncomingRecords | The number of records successfully put to the Kinesis stream over the specified time period. This metric includes record counts from `PutRecord` and `PutRecords` operations. Minimum, maximum, and average statistics represent the records in a single put operation for the stream in the specified time period. | Count | Count | ShardId, StreamName |  |
| IncomingRecords |  | Count | Count | StreamName |  |
| IncomingRecords |  | Count | Multi | ShardId, StreamName |  |
| IncomingRecords |  | Count | Multi | StreamName |  |
| IncomingRecords |  | Count | Sum | ShardId, StreamName |  |
| IteratorAgeMilliseconds | The age of the last record in all `GetRecords` calls made against a shard, measured over the specified time period. Age is the difference between the current time and when the last record of the `GetRecords` call was written to the stream. The minimum and maximum statistics can be used to track the progress of Kinesis consumer applications. A value of `0` indicates that the records being read are completely caught up with the stream. | Milliseconds | Multi | StreamName, ShardId |  |
| IteratorAgeMilliseconds |  | Milliseconds | Count | StreamName, ShardId |  |
| OutgoingBytes | The number of bytes retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes returned in a single `GetRecords` operation or published in a single `SubscribeToShard` event for the shard in the specified time period. | Bytes | Sum | StreamName, ShardId |  |
| OutgoingBytes |  | Bytes | Multi | StreamName, ShardId |  |
| OutgoingBytes |  | Bytes | Count | StreamName, ShardId |  |
| OutgoingRecords | The number of records retrieved from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records returned in a single `GetRecords` operation or published in a single `SubscribeToShard` event for the shard in the specified time period. | Count | Sum | StreamName, ShardId |  |
| OutgoingRecords |  | Count | Multi | StreamName, ShardId |  |
| OutgoingRecords |  | Count | Count | StreamName, ShardId |  |
| PutRecord.Bytes | The number of bytes put to the Kinesis stream using the `PutRecord` operation over the specified time period | Bytes | Sum | StreamName |  |
| PutRecord.Bytes |  | Bytes | Multi | StreamName |  |
| PutRecord.Bytes |  | Bytes | Count | StreamName |  |
| PutRecord.Latency | The time taken per `PutRecord` operation, measured over the specified time period | Milliseconds | Multi | StreamName |  |
| PutRecord.Success | The number of successful `PutRecord` operations per Kinesis stream, measured over the specified time period. Average reflects the percentage of successful writes to a stream. | Count | Sum | StreamName |  |
| PutRecord.Success |  | Count | Average | StreamName | Applicable |
| PutRecord.Success |  | Count | Count | StreamName |  |
| PutRecords.Bytes | The number of bytes put to the Kinesis stream using the `PutRecords` operation over the specified time period | Bytes | Sum | StreamName |  |
| PutRecords.Bytes |  | Bytes | Multi | StreamName |  |
| PutRecords.Bytes |  | Bytes | Count | StreamName |  |
| PutRecords.Latency | The time taken per `PutRecords` operation, measured over the specified time period | Milliseconds | Multi | StreamName |  |
| PutRecords.Records | The number of successful records in a `PutRecords` operation per Kinesis stream, measured over the specified time period | Count | Sum | StreamName |  |
| PutRecords.Records |  | Count | Multi | StreamName |  |
| PutRecords.Records |  | Count | Count | StreamName |  |
| PutRecords.Success | The number of `PutRecords` operations where at least one record succeeded, per Kinesis stream, measured over the specified time period | Count | Sum | StreamName |  |
| PutRecords.Success |  | Count | Average | StreamName |  |
| PutRecords.Success |  | Count | Count | StreamName |  |
| ReadProvisionedThroughputExceeded | The number of `GetRecords` calls throttled for the stream over the specified time period | Count | Sum | StreamName |  |
| ReadProvisionedThroughputExceeded |  | Count | Multi | StreamName | Applicable |
| ReadProvisionedThroughputExceeded |  | Count | Count | StreamName |  |
| SubscribeToShardEvent.Bytes | The number of bytes received from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the bytes published in a single event for the specified time period. | Bytes | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Bytes |  | Bytes | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Bytes |  | Bytes | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.MillisBehindLatest | The difference between the current time and when the last record of the `SubscribeToShard` event was written to the stream | Milliseconds | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.MillisBehindLatest |  | Milliseconds | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records | The number of records received from the shard, measured over the specified time period. Minimum, maximum, and average statistics represent the records in a single event for the specified time period. | Count | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records |  | Count | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Records |  | Count | Count | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success | This metric is emitted every time an event is published successfully. Only emitted when there's an active subscription. | Count | Sum | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success |  | Count | Multi | StreamName, ConsumerName |  |
| SubscribeToShardEvent.Success |  | Count | Count | StreamName, ConsumerName |  |
| SubscribeToShard.RateExceeded | This metric is emitted when a new subscription attempt fails because there already is an active subscription by the same consumer or if you exceed the number of calls per second allowed for this operation | Count | Minimum | StreamName, ConsumerName |  |
| SubscribeToShard.Success |  | Count | Minimum | StreamName, ConsumerName |  |
| WriteProvisionedThroughputExceeded | The number of records rejected due to throttling for the stream over the specified time period. This metric includes throttling from `PutRecord` and `PutRecords` operations. | Count | Sum | StreamName |  |
| WriteProvisionedThroughputExceeded |  | Count | Multi | StreamName | Applicable |
| WriteProvisionedThroughputExceeded |  | Count | Count | StreamName |  |

### Amazon Kinesis Video Streams

`StreamName` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| GetHLSMasterPlaylist.Latency | Latency of the `GetHLSMasterPlaylist` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetHLSMasterPlaylist.Requests | Number of `GetHLSMasterPlaylist` API requests for a given stream | Count | Sum | StreamName |  |
| GetHLSMasterPlaylist.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetHLSMediaPlaylist.Latency | Latency of the `GetHLSMediaPlaylist` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetHLSMediaPlaylist.Requests | Number of `GetHLSMediaPlaylist` API requests for a given stream | Count | Sum | StreamName |  |
| GetHLSMediaPlaylist.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetHLSStreamingSessionURL.Latency | Latency of the `GetHLSStreamingSessionURL` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetHLSStreamingSessionURL.Requests | Number of `GetHLSStreamingSessionURL` API requests for a given stream | Count | Sum | StreamName |  |
| GetHLSStreamingSessionURL.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetMP4InitFragment.Latency | Latency of the `GetMP4InitFragment` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetMP4InitFragment.Requests | Number of `GetMP4InitFragment` API requests for a given stream | Count | Sum | StreamName |  |
| GetMP4InitFragment.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetMP4MediaFragment.Latency | Latency of the `GetMP4MediaFragment` API calls for the given stream name | Milliseconds | Multi | StreamName |  |
| GetMP4MediaFragment.OutgoingBytes | Total number of bytes sent out from the service as part of the `GetMP4MediaFragment` API for a given stream | Bytes | Sum | StreamName |  |
| GetMP4MediaFragment.Requests | Number of `GetMP4MediaFragment` API requests for a given stream | Count | Sum | StreamName |  |
| GetMP4MediaFragment.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Sum | StreamName |  |
| GetMedia.ConnectionErrors | The number of connections that were not successfully established | Count | Sum | StreamName | Applicable |
| GetMediaForFragmentList.OutgoingBytes | Total number of bytes sent out from the service as part of the `GetMediaForFragmentList` API for a given stream | Bytes | Sum | StreamName |  |
| GetMediaForFragmentList.OutgoingFragments | Total number of fragments sent out from the service as part of the `GetMediaForFragmentList` API for a given stream | Count | Sum | StreamName |  |
| GetMediaForFragmentList.OutgoingFrames | Total number of frames sent out from the service as part of the `GetMediaForFragmentList` API for a given stream | Count | Sum | StreamName |  |
| GetMediaForFragmentList.Requests | Number of `GetMediaForFragmentList` API requests for a given stream | Count | Sum | StreamName |  |
| GetMediaForFragmentList.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName |  |
| GetMedia.MillisBehindNow | Time difference between the current server timestamp and the server timestamp of the last fragment sent | Milliseconds | Multi | StreamName |  |
| GetMedia.OutgoingBytes | Total number of bytes sent out from the service as part of the `GetMedia` API for a given stream | Bytes | Sum | StreamName |  |
| GetMedia.OutgoingFragments | Number of fragments sent while doing `GetMedia` for the stream | Count | Sum | StreamName |  |
| GetMedia.OutgoingFrames | Number of frames sent during `GetMedia` on the given stream | Count | Sum | StreamName |  |
| GetMedia.Requests | Number of `GetMedia` API requests for a given stream | Count | Sum | StreamName |  |
| GetMedia.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName | Applicable |
| ListFragments.Latency | Latency of the `ListFragments` API calls for the given stream name | Milliseconds | Multi | StreamName | Applicable |
| PutMedia.ActiveConnections | The total number of connections to the service host | Count | Sum | StreamName |  |
| PutMedia.BufferingAckLatency | Time difference between when the first byte of a new fragment is received by Kinesis Video Streams and when the `Buffering ACK` is sent for the fragment | Milliseconds | Multi | StreamName |  |
| PutMedia.ConnectionErrors | Errors while establishing `PutMedia` connection for the stream | Count | Sum | StreamName | Applicable |
| PutMedia.ErrorAckCount | Number of Error ACKs sent while doing `PutMedia` for the stream | Count | Sum | StreamName |  |
| PutMedia.FragmentIngestionLatency | Time difference between when the first and last bytes of a fragment are received by Kinesis Video Streams | Milliseconds | Multi | StreamName |  |
| PutMedia.FragmentPersistLatency | Time taken from when the complete fragment data is received and archived | Milliseconds | Multi | StreamName |  |
| PutMedia.IncomingBytes | Number of bytes received as part of `PutMedia` for the stream | Bytes | Sum | StreamName |  |
| PutMedia.IncomingFragments | Number of complete fragments received as part of `PutMedia` for the stream | Count | Sum | StreamName |  |
| PutMedia.IncomingFrames | Number of complete frames received as part of `PutMedia` for the stream | Count | Sum | StreamName |  |
| PutMedia.Latency | Time difference between the request and the HTTP response from `InletService` while establishing the connection | Milliseconds | Multi | StreamName |  |
| PutMedia.PersistedAckLatency | Time difference between when the last byte of a new fragment is received by Kinesis Video Streams and when the `Persisted ACK` is sent for the fragment | Milliseconds | Multi | StreamName |  |
| PutMedia.ReceivedAckLatency | Time difference between when the last byte of a new fragment is received by Kinesis Video Streams and when the `Received ACK` is sent for the fragment | Milliseconds | Multi | StreamName |  |
| PutMedia.Requests | Number of `PutMedia` API requests for a given stream | Count | Sum | StreamName |  |
| PutMedia.Success | The rate of success, `1` being the value for every successful request, and `0` the value for every failure | Count | Average | StreamName | Applicable |