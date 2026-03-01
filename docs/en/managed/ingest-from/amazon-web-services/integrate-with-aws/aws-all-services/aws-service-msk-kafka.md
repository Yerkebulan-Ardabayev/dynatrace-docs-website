---
title: Amazon MSK (Kafka) monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-msk-kafka
scraped: 2026-03-01T21:21:59.414254
---

# Amazon MSK (Kafka) monitoring

# Amazon MSK (Kafka) monitoring

* How-to guide
* 14-min read
* Updated on May 19, 2025

Dynatrace ingests metrics for multiple preselected namespaces, including Amazon MSK (Kafka). You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

## Prerequisites

To enable monitoring for this service, you need

* ActiveGate version 1.197+

  + For Dynatrace SaaS deployments, you need an Environment ActiveGate or a Multi-environment ActiveGate.
  + For Dynatrace Managed deployments, you can use any kind of ActiveGate.

    For role-based access (whether in a [SaaS](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#role-based-access "Integrate metrics from Amazon CloudWatch.") or [Managedï»¿](https://docs.dynatrace.com/managed/shortlink/aws-managed-deployment) deployment), you need an [Environment ActiveGate](/docs/ingest-from/dynatrace-activegate/installation "Learn how to configure ActiveGate") installed on an Amazon EC2 host.
* Dynatrace version 1.203+
* An updated [AWS monitoring policy](/docs/ingest-from/amazon-web-services/integrate-with-aws/cloudwatch-metrics#monitoring-policy "Integrate metrics from Amazon CloudWatch.") to include the additional AWS services.  
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

See the example of JSON policy for one single service below.

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

![Msk](https://dt-cdn.net/images/dashboard-71-2325-1b0eb2ef80.png)

## Available metrics

`Cluster Name` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| ActiveControllerCount | Only one controller per cluster should be active at any given time. | Count | Multi | Cluster Name | Applicable |
| ActiveControllerCount |  | Count | Sum | Cluster Name | Applicable |
| BytesInPerSec | The number of bytes per second received from clients | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| BytesInPerSec |  | Bytes/Second | Multi | Cluster Name, Broker ID, Topic |  |
| BytesInPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| BytesInPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID, Topic |  |
| BytesOutPerSec | The number of bytes per second sent to clients | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| BytesOutPerSec |  | Bytes/Second | Multi | Cluster Name, Broker ID, Topic |  |
| BytesOutPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| BytesOutPerSec |  | Bytes/Second | Sum | Cluster Name, Broker ID, Topic |  |
| CPUCreditBalance | The number of earned credits | Count | Multi | Cluster Name, Broker ID |  |
| CPUCreditBalance |  | Count | Sum | Cluster Name, Broker ID |  |
| CPUCreditUsage | The number of used credits | Count | Multi | Cluster Name, Broker ID |  |
| CPUCreditUsage |  | Count | Sum | Cluster Name, Broker ID |  |
| CpuIdle | The percentage of CPU idle time | Percent | Multi | Cluster Name, Broker ID | Applicable |
| CpuIdle |  | Percent | Sum | Cluster Name, Broker ID | Applicable |
| CpuSystem | The percentage of CPU in kernel space | Percent | Multi | Cluster Name, Broker ID | Applicable |
| CpuSystem |  | Percent | Sum | Cluster Name, Broker ID | Applicable |
| CpuUser | The percentage of CPU in user space | Percent | Multi | Cluster Name, Broker ID | Applicable |
| CpuUser |  | Percent | Sum | Cluster Name, Broker ID | Applicable |
| FetchConsumerLocalTimeMsMean | The mean time in milliseconds that the consumer request is processed at the leader | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerLocalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerRequestQueueTimeMsMean | The mean time in milliseconds that the consumer request waits in the request queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerRequestQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerResponseQueueTimeMsMean | The mean time in milliseconds that the consumer request waits in the response queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerResponseQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerResponseSendTimeMsMean |  | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerResponseSendTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchConsumerTotalTimeMsMean | The mean total time in milliseconds that consumers spend on fetching data from the broker | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchConsumerTotalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerLocalTimeMsMean | The mean time in milliseconds that the follower request is processed at the leader | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerLocalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerRequestQueueTimeMsMean | The mean time in milliseconds that the follower request waits in the request queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerRequestQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerResponseQueueTimeMsMean | The mean time in milliseconds that the follower request waits in the response queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerResponseQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerResponseSendTimeMsMean | The mean time in milliseconds for the follower to send a response | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerResponseSendTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchFollowerTotalTimeMsMean | The mean total time in milliseconds that followers spend on fetching data from the broker | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchFollowerTotalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec | The number of fetch message conversions per second for the broker | Count/Second | Multi | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec |  | Count/Second | Multi | Cluster Name, Broker ID, Topic |  |
| FetchMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID |  |
| FetchMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID, Topic |  |
| FetchMessageConversionsTimeMsMean | The mean total time in milliseconds that messages being fetched spend converting | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchMessageConversionsTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| FetchThrottleByteRate | The number of throttled bytes per second | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| FetchThrottleByteRate |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| FetchThrottleQueueSize | The number of messages in the throttle queue | Count | Multi | Cluster Name, Broker ID |  |
| FetchThrottleQueueSize |  | Count | Sum | Cluster Name, Broker ID |  |
| FetchThrottleTime | The average fetch throttle time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| FetchThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| GlobalPartitionCount | Total number of partitions across all brokers in the cluster | Count | Multi | Cluster Name | Applicable |
| GlobalPartitionCount |  | Count | Sum | Cluster Name | Applicable |
| GlobalTopicCount | Total number of topics across all brokers in the cluster | Count | Multi | Cluster Name | Applicable |
| GlobalTopicCount |  | Count | Sum | Cluster Name | Applicable |
| KafkaAppLogsDiskUsed | The percentage of disk space used for application logs | Percent | Multi | Cluster Name, Broker ID | Applicable |
| KafkaAppLogsDiskUsed |  | Percent | Sum | Cluster Name, Broker ID | Applicable |
| KafkaDataLogsDiskUsed | The percentage of disk space used for data logs | Percent | Multi | Cluster Name, Broker ID | Applicable |
| KafkaDataLogsDiskUsed |  | Percent | Sum | Cluster Name, Broker ID | Applicable |
| LeaderCount | The number of leader replicas | Count | Multi | Cluster Name, Broker ID |  |
| LeaderCount |  | Count | Sum | Cluster Name, Broker ID |  |
| MemoryBuffered | The size in bytes of buffered memory for the broker | Bytes | Multi | Cluster Name, Broker ID | Applicable |
| MemoryBuffered |  | Bytes | Sum | Cluster Name, Broker ID | Applicable |
| MemoryCached | The size in bytes of cached memory for the broker | Bytes | Multi | Cluster Name, Broker ID | Applicable |
| MemoryCached |  | Bytes | Sum | Cluster Name, Broker ID | Applicable |
| MemoryFree | The size in bytes of memory that is free and available for the broker | Bytes | Multi | Cluster Name, Broker ID | Applicable |
| MemoryFree |  | Bytes | Sum | Cluster Name, Broker ID | Applicable |
| MemoryUsed | The size in bytes of memory that is in use for the broker | Bytes | Multi | Cluster Name, Broker ID | Applicable |
| MemoryUsed |  | Bytes | Sum | Cluster Name, Broker ID | Applicable |
| MessagesInPerSec | The number of incoming messages per second for the broker | Count/Second | Multi | Cluster Name, Broker ID |  |
| MaxOffsetLag | The maximum offset lag across all partitions in a topic | Count | Multi | Cluster Name, Consumer Group, Topic |  |
| MaxOffsetLag | The maximum offset lag across all partitions in a topic | Count | Sum | Cluster Name, Consumer Group, Topic |  |
| MessagesInPerSec |  | Count/Second | Multi | Cluster Name, Broker ID, Topic |  |
| MessagesInPerSec |  | Count/Second | Sum | Cluster Name, Broker ID |  |
| MessagesInPerSec |  | Count/Second | Sum | Cluster Name, Broker ID, Topic |  |
| NetworkProcessorAvgIdlePercent | The average percentage of the time the network processors are idle | Percent | Multi | Cluster Name, Broker ID |  |
| NetworkProcessorAvgIdlePercent |  | Percent | Sum | Cluster Name, Broker ID |  |
| NetworkRxDropped | The number of dropped receive packages | Count | Multi | Cluster Name, Broker ID | Applicable |
| NetworkRxDropped |  | Count | Sum | Cluster Name, Broker ID | Applicable |
| NetworkRxErrors | The number of network receive errors for the broker | Count | Multi | Cluster Name, Broker ID | Applicable |
| NetworkRxErrors |  | Count | Sum | Cluster Name, Broker ID | Applicable |
| NetworkRxPackets | The number of packets received by the broker | Count | Multi | Cluster Name, Broker ID | Applicable |
| NetworkRxPackets |  | Count | Sum | Cluster Name, Broker ID | Applicable |
| NetworkTxDropped | The number of dropped transmit packages | Count | Multi | Cluster Name, Broker ID | Applicable |
| NetworkTxDropped |  | Count | Sum | Cluster Name, Broker ID | Applicable |
| NetworkTxErrors | The number of network transmit errors for the broker | Count | Multi | Cluster Name, Broker ID | Applicable |
| NetworkTxErrors |  | Count | Sum | Cluster Name, Broker ID | Applicable |
| NetworkTxPackets | The number of packets transmitted by the broker | Count | Multi | Cluster Name, Broker ID | Applicable |
| NetworkTxPackets |  | Count | Sum | Cluster Name, Broker ID | Applicable |
| OfflinePartitionsCount | Total number of partitions that are offline in the cluster | Count | Multi | Cluster Name | Applicable |
| OfflinePartitionsCount |  | Count | Sum | Cluster Name | Applicable |
| PartitionCount | The number of partitions for the broker | Count | Multi | Cluster Name, Broker ID |  |
| PartitionCount |  | Count | Sum | Cluster Name, Broker ID |  |
| ProduceLocalTimeMsMean | The mean time in milliseconds for the follower to send a response | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceLocalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec | The number of produce message conversions per second for the broker | Count/Second | Multi | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec |  | Count/Second | Multi | Cluster Name, Broker ID, Topic |  |
| ProduceMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID |  |
| ProduceMessageConversionsPerSec |  | Count/Second | Sum | Cluster Name, Broker ID, Topic |  |
| ProduceMessageConversionsTimeMsMean | The mean time in milliseconds spent on message format conversions | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceMessageConversionsTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceRequestQueueTimeMsMean | The mean time in milliseconds that request messages spend in the queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceRequestQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceResponseQueueTimeMsMean | The mean time in milliseconds that response messages spend in the queue | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceResponseQueueTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceResponseSendTimeMsMean | The mean time in milliseconds spent on sending response messages | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceResponseSendTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleByteRate | The number of throttled bytes per second | Bytes/Second | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleByteRate |  | Bytes/Second | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleQueueSize | The number of messages in the throttle queue | Count | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleQueueSize |  | Count | Sum | Cluster Name, Broker ID |  |
| ProduceThrottleTime | The average produce throttle time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| ProduceTotalTimeMsMean | The mean produce time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| ProduceTotalTimeMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RequestBytesMean | The mean number of request bytes for the broker | Bytes | Multi | Cluster Name, Broker ID |  |
| RequestBytesMean |  | Bytes | Sum | Cluster Name, Broker ID |  |
| RequestExemptFromThrottleTime | The average time in milliseconds spent in broker network and I/O threads to process requests that are exempt from throttling | Milliseconds | Multi | Cluster Name, Broker ID |  |
| RequestExemptFromThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RequestHandlerAvgIdlePercent | The average percentage of the time the request handler threads are idle | Percent | Multi | Cluster Name, Broker ID |  |
| RequestHandlerAvgIdlePercent |  | Percent | Sum | Cluster Name, Broker ID |  |
| RequestThrottleQueueSize | The number of messages in the throttle queue | Count | Multi | Cluster Name, Broker ID |  |
| RequestThrottleQueueSize |  | Count | Sum | Cluster Name, Broker ID |  |
| RequestThrottleTime | The average request throttle time in milliseconds | Milliseconds | Multi | Cluster Name, Broker ID |  |
| RequestThrottleTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RequestTime | The average time in milliseconds spent in broker network and I/O threads to process requests | Milliseconds | Multi | Cluster Name, Broker ID |  |
| RequestTime |  | Milliseconds | Sum | Cluster Name, Broker ID |  |
| RootDiskUsed | The percentage of the root disk used by the broker | Percent | Multi | Cluster Name, Broker ID | Applicable |
| RootDiskUsed |  | Percent | Sum | Cluster Name, Broker ID | Applicable |
| SumOffsetLag | The aggregated offset lag for all the partitions in a topic | Count | Multi | Cluster Name, Consumer Group, Topic |  |
| SwapFree | The size in bytes of swap memory that is available for the broker | Bytes | Multi | Cluster Name, Broker ID | Applicable |
| SwapFree |  | Bytes | Sum | Cluster Name, Broker ID | Applicable |
| SwapUsed | The size in bytes of swap memory that is in use for the broker | Bytes | Multi | Cluster Name, Broker ID | Applicable |
| SwapUsed |  | Bytes | Sum | Cluster Name, Broker ID | Applicable |
| UnderMinIsrPartitionCount | The number of under minIsr partitions for the broker | Count | Multi | Cluster Name, Broker ID |  |
| UnderMinIsrPartitionCount |  | Count | Sum | Cluster Name, Broker ID |  |
| UnderReplicatedPartitions | The number of under-replicated partitions for the broker | Count | Multi | Cluster Name, Broker ID |  |
| UnderReplicatedPartitions |  | Count | Sum | Cluster Name, Broker ID |  |
| ZooKeeperRequestLatencyMsMean | Mean latency in milliseconds for ZooKeeper requests from broker | Milliseconds | Multi | Cluster Name, Broker ID | Applicable |
| ZooKeeperRequestLatencyMsMean |  | Milliseconds | Multi | Cluster Name | Applicable |
| ZooKeeperRequestLatencyMsMean |  | Milliseconds | Sum | Cluster Name, Broker ID | Applicable |
| ZooKeeperRequestLatencyMsMean |  | Milliseconds | Sum | Cluster Name | Applicable |
| ZooKeeperSessionState | Connection status of broker's ZooKeeper session which may be one of the following: `NOT_CONNECTED`: `0.0`, `ASSOCIATING`: `0.1`, `CONNECTING`: `0.5`, `CONNECTEDREADONLY`: `0.8`, `CONNECTED`: `1.0`, `CLOSED`: `5.0`, `AUTH_FAILED`: `10.0`. | Count | Multi | Cluster Name, Broker ID | Applicable |
| ZooKeeperSessionState |  | Count | Multi | Cluster Name | Applicable |
| ZooKeeperSessionState |  | Count | Sum | Cluster Name, Broker ID |  |
| ZooKeeperSessionState |  | Count | Sum | Cluster Name |  |