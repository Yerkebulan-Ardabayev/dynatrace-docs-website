---
title: AWS Elemental MediaConnect monitoring
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-with-aws/aws-all-services/aws-service-elemental-mediaconnect
scraped: 2026-02-27T21:31:49.933771
---

# AWS Elemental MediaConnect monitoring

# AWS Elemental MediaConnect monitoring

* How-to guide
* 14-min read
* Published Jul 06, 2020

Dynatrace ingests metrics for multiple preselected namespaces, including AWS Elemental MediaConnect. You can view metrics for each service instance, split metrics into multiple dimensions, and create custom charts that you can pin to your dashboards.

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

![Mediaconnect](https://dt-cdn.net/images/mediaconnect-dashboard-1857-cb8f145abd.png)

## Available metrics

`FlowARN` is the main dimension.

| Name | Description | Unit | Statistics | Dimensions | Recommended |
| --- | --- | --- | --- | --- | --- |
| ARQRecovered | The number of dropped packets that were recovered by automatic repeat request (ARQ) | Count | Sum | FlowARN | Applicable |
| ARQRecovered |  | Count | Sum | Region |  |
| ARQRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| ARQRequests | The number of retransmitted packets that were requested through automatic repeat request (ARQ) and received | Count | Sum | Region |  |
| ARQRequests |  | Count | Sum | Region, AvailabilityZone |  |
| ARQRequests |  | Count | Sum | FlowARN | Applicable |
| BitRate |  | Bits/Second | Multi | Region |  |
| BitRate |  | Bits/Second | Multi | Region, AvailabilityZone |  |
| BitRate |  | Bits/Second | Multi | FlowARN | Applicable |
| CATError | The number of times that a conditional access table (CAT) error occurred. This error indicates that the CAT is not present. | Count | Sum | FlowARN |  |
| CATError |  | Count | Sum | Region |  |
| CATError |  | Count | Sum | Region, AvailabilityZone |  |
| CRCError |  | Count | Sum | FlowARN |  |
| CRCError |  | Count | Sum | Region |  |
| CRCError |  | Count | Sum | Region, AvailabilityZone |  |
| Connected | The status of the source. A value of one indicates that the source is connected and a value of zero indicates that the source is disconnected. | None | Multi | FlowARN |  |
| Connected |  | None | Sum | FlowARN |  |
| Connected |  | None | Multi | Region |  |
| Connected |  | None | Multi | Region, AvailabilityZone |  |
| Connected |  | None | Sum | Region |  |
| Connected |  | None | Sum | Region, AvailabilityZone |  |
| Connected |  | None | Count | Region |  |
| Connected |  | None | Count | Region, AvailabilityZone |  |
| ConnectedOutputs |  | Count | Sum | Region |  |
| ConnectedOutputs |  | Count | Sum | Region, AvailabilityZone |  |
| ConnectedOutputs |  | Count | Sum | FlowARN |  |
| ContinuityCounter | The number of times that a continuity error occurred | Count | Sum | FlowARN |  |
| ContinuityCounter |  | Count | Sum | Region |  |
| ContinuityCounter |  | Count | Sum | Region, AvailabilityZone |  |
| Disconnections | The number of times that the source status changed from connected to disconnected | Count | Sum | Region |  |
| Disconnections |  | Count | Sum | Region, AvailabilityZone |  |
| Disconnections |  | Count | Sum | FlowARN |  |
| DroppedPackets | The number of packets that were lost during transit | Count | Sum | Region |  |
| DroppedPackets |  | Count | Sum | Region, AvailabilityZone |  |
| DroppedPackets |  | Count | Sum | FlowARN | Applicable |
| FECPackets | The number of packets that were transmitted using forward error correction (FEC) and received | Count | Sum | FlowARN | Applicable |
| FECPackets |  | Count | Sum | Region |  |
| FECPackets |  | Count | Sum | Region, AvailabilityZone |  |
| FECRecovered | The number of packets that were transmitted using forward error correction (FEC), lost during transit, and recovered | Count | Sum | FlowARN | Applicable |
| FECRecovered |  | Count | Sum | Region |  |
| FECRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| NotRecoveredPackets | The number of packets that were lost during transit and were not recovered by error correction | Count | Sum | FlowARN | Applicable |
| NotRecoveredPackets |  | Count | Sum | Region |  |
| NotRecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| OutputConnected |  | None | Multi | Region, OutputARN |  |
| OutputConnected |  | None | Multi | FlowARN |  |
| OutputConnected |  | None | Multi | Region |  |
| OutputConnected |  | None | Multi | Region, AvailabilityZone |  |
| OutputDisconnections |  | Count | Sum | Region, OutputARN |  |
| OutputDisconnections |  | Count | Sum | FlowARN |  |
| OutputDisconnections |  | Count | Sum | Region |  |
| OutputDisconnections |  | Count | Sum | Region, AvailabilityZone |  |
| OverflowPackets | The number of packets that were lost in transit because the video required more buffer than was available | Count | Sum | FlowARN | Applicable |
| OverflowPackets |  | Count | Sum | Region |  |
| OverflowPackets |  | Count | Sum | Region, AvailabilityZone |  |
| PATError | The number of times that a program association table (PAT) error occurred | Count | Sum | Region |  |
| PATError |  | Count | Sum | Region, AvailabilityZone |  |
| PATError |  | Count | Sum | FlowARN |  |
| PCRAccuracyError | The number of times that a program clock register (PCR) accuracy error occurred | Count | Sum | Region |  |
| PCRAccuracyError |  | Count | Sum | Region, AvailabilityZone |  |
| PCRAccuracyError |  | Count | Sum | FlowARN |  |
| PCRError | The number of times that a PCR error occurred | Count | Sum | FlowARN |  |
| PCRError |  | Count | Sum | Region |  |
| PCRError |  | Count | Sum | Region, AvailabilityZone |  |
| PIDError | The number of times that a packet identifier (PID) error occurred | Count | Sum | Region |  |
| PIDError |  | Count | Sum | Region, AvailabilityZone |  |
| PIDError |  | Count | Sum | FlowARN |  |
| PMTError | The number of times that a program map table (PMT) error occurred | Count | Sum | FlowARN |  |
| PMTError |  | Count | Sum | Region |  |
| PMTError |  | Count | Sum | Region, AvailabilityZone |  |
| PTSError | The number of times that a presentation timestamp (PTS) error occurred | Count | Sum | FlowARN |  |
| PTSError |  | Count | Sum | Region |  |
| PTSError |  | Count | Sum | Region, AvailabilityZone |  |
| PacketLossPercent | The percentage of packets that were lost during transit, even if they were recovered | Percent | Multi | Region |  |
| PacketLossPercent |  | Percent | Multi | Region, AvailabilityZone |  |
| PacketLossPercent |  | Percent | Multi | FlowARN | Applicable |
| RecoveredPackets | The number of packets that were lost during transit, but recovered | Count | Sum | FlowARN | Applicable |
| RecoveredPackets |  | Count | Sum | Region |  |
| RecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| RoundTripTime | The amount of time it takes for the source to send a signal and receive an acknowledgment from AWS Elemental MediaConnect | Milliseconds | Multi | Region |  |
| RoundTripTime |  | Milliseconds | Multi | Region, AvailabilityZone |  |
| RoundTripTime |  | Milliseconds | Multi | FlowARN | Applicable |
| SourceARQRecovered |  | Count | Sum | Region |  |
| SourceARQRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| SourceARQRecovered |  | Count | Sum | Region, SourceARN |  |
| SourceARQRecovered |  | Count | Sum | FlowARN |  |
| SourceARQRequests |  | Count | Sum | FlowARN |  |
| SourceARQRequests |  | Count | Sum | Region |  |
| SourceARQRequests |  | Count | Sum | Region, AvailabilityZone |  |
| SourceARQRequests |  | Count | Sum | Region, SourceARN |  |
| SourceBitRate | The bitrate of the incoming (source) video | Bits/Second | Multi | FlowARN |  |
| SourceBitRate |  | Bits/Second | Multi | Region |  |
| SourceBitRate |  | Bits/Second | Multi | Region, AvailabilityZone |  |
| SourceBitRate |  | Bits/Second | Multi | Region, SourceARN |  |
| SourceCATError |  | Count | Sum | FlowARN |  |
| SourceCATError |  | Count | Sum | Region |  |
| SourceCATError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceCATError |  | Count | Sum | Region, SourceARN |  |
| SourceCRCError |  | Count | Sum | FlowARN |  |
| SourceCRCError |  | Count | Sum | Region |  |
| SourceCRCError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceCRCError |  | Count | Sum | Region, SourceARN |  |
| SourceConnected |  | None | Multi | Region |  |
| SourceConnected |  | None | Multi | Region, AvailabilityZone |  |
| SourceConnected |  | None | Multi | Region, SourceARN |  |
| SourceConnected |  | None | Sum | Region |  |
| SourceConnected |  | None | Sum | Region, AvailabilityZone |  |
| SourceConnected |  | None | Sum | Region, SourceARN |  |
| SourceConnected |  | None | Count | Region |  |
| SourceConnected |  | None | Count | Region, AvailabilityZone |  |
| SourceConnected |  | None | Count | Region, SourceARN |  |
| SourceConnected |  | None | Multi | FlowARN |  |
| SourceConnected |  | None | Sum | FlowARN |  |
| SourceContinuityCounter |  | Count | Sum | Region |  |
| SourceContinuityCounter |  | Count | Sum | Region, AvailabilityZone |  |
| SourceContinuityCounter |  | Count | Sum | Region, SourceARN |  |
| SourceContinuityCounter |  | Count | Sum | FlowARN |  |
| SourceDisconnections |  | Count | Sum | FlowARN |  |
| SourceDisconnections |  | Count | Sum | Region |  |
| SourceDisconnections |  | Count | Sum | Region, AvailabilityZone |  |
| SourceDisconnections |  | Count | Sum | Region, SourceARN |  |
| SourceDroppedPackets |  | Count | Sum | Region |  |
| SourceDroppedPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceDroppedPackets |  | Count | Sum | Region, SourceARN |  |
| SourceDroppedPackets |  | Count | Sum | FlowARN |  |
| SourceFECPackets |  | Count | Sum | Region |  |
| SourceFECPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceFECPackets |  | Count | Sum | Region, SourceARN |  |
| SourceFECPackets |  | Count | Sum | FlowARN |  |
| SourceFECRecovered |  | Count | Sum | Region |  |
| SourceFECRecovered |  | Count | Sum | Region, AvailabilityZone |  |
| SourceFECRecovered |  | Count | Sum | Region, SourceARN |  |
| SourceFECRecovered |  | Count | Sum | FlowARN |  |
| SourceNotRecoveredPackets |  | Count | Sum | Region |  |
| SourceNotRecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceNotRecoveredPackets |  | Count | Sum | Region, SourceARN |  |
| SourceNotRecoveredPackets |  | Count | Sum | FlowARN |  |
| SourceOverflowPackets |  | Count | Sum | Region |  |
| SourceOverflowPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceOverflowPackets |  | Count | Sum | Region, SourceARN |  |
| SourceOverflowPackets |  | Count | Sum | FlowARN |  |
| SourcePATError |  | Count | Sum | FlowARN |  |
| SourcePATError |  | Count | Sum | Region |  |
| SourcePATError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePATError |  | Count | Sum | Region, SourceARN |  |
| SourcePCRAccuracyError |  | Count | Sum | FlowARN |  |
| SourcePCRAccuracyError |  | Count | Sum | Region |  |
| SourcePCRAccuracyError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePCRAccuracyError |  | Count | Sum | Region, SourceARN |  |
| SourcePCRError |  | Count | Sum | Region |  |
| SourcePCRError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePCRError |  | Count | Sum | Region, SourceARN |  |
| SourcePCRError |  | Count | Sum | FlowARN |  |
| SourcePIDError |  | Count | Sum | FlowARN |  |
| SourcePIDError |  | Count | Sum | Region |  |
| SourcePIDError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePIDError |  | Count | Sum | Region, SourceARN |  |
| SourcePMTError |  | Count | Sum | Region |  |
| SourcePMTError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePMTError |  | Count | Sum | Region, SourceARN |  |
| SourcePMTError |  | Count | Sum | FlowARN |  |
| SourcePTSError |  | Count | Sum | Region |  |
| SourcePTSError |  | Count | Sum | Region, AvailabilityZone |  |
| SourcePTSError |  | Count | Sum | Region, SourceARN |  |
| SourcePTSError |  | Count | Sum | FlowARN |  |
| SourcePacketLossPercent |  | Percent | Multi | FlowARN |  |
| SourcePacketLossPercent |  | Percent | Multi | Region |  |
| SourcePacketLossPercent |  | Percent | Multi | Region, AvailabilityZone |  |
| SourcePacketLossPercent |  | Percent | Multi | Region, SourceARN |  |
| SourceRecoveredPackets |  | Count | Sum | FlowARN |  |
| SourceRecoveredPackets |  | Count | Sum | Region |  |
| SourceRecoveredPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceRecoveredPackets |  | Count | Sum | Region, SourceARN |  |
| SourceRoundTripTime |  | Milliseconds | Multi | Region |  |
| SourceRoundTripTime |  | Milliseconds | Multi | Region, AvailabilityZone |  |
| SourceRoundTripTime |  | Milliseconds | Multi | Region, SourceARN |  |
| SourceRoundTripTime |  | Milliseconds | Multi | FlowARN |  |
| SourceTSByteError |  | Count | Sum | Region |  |
| SourceTSByteError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTSByteError |  | Count | Sum | Region, SourceARN |  |
| SourceTSByteError |  | Count | Sum | FlowARN |  |
| SourceTSSyncLoss |  | Count | Sum | Region |  |
| SourceTSSyncLoss |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTSSyncLoss |  | Count | Sum | Region, SourceARN |  |
| SourceTSSyncLoss |  | Count | Sum | FlowARN |  |
| SourceTotalPackets |  | Count | Sum | Region |  |
| SourceTotalPackets |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTotalPackets |  | Count | Sum | Region, SourceARN |  |
| SourceTotalPackets |  | Count | Sum | FlowARN |  |
| SourceTransportError |  | Count | Sum | FlowARN |  |
| SourceTransportError |  | Count | Sum | Region |  |
| SourceTransportError |  | Count | Sum | Region, AvailabilityZone |  |
| SourceTransportError |  | Count | Sum | Region, SourceARN |  |
| TSByteError | The number of times that a transport stream (TS) byte error occurred | Count | Sum | Region |  |
| TSByteError |  | Count | Sum | Region, AvailabilityZone |  |
| TSByteError |  | Count | Sum | FlowARN |  |
| TSSyncLoss | The number of times that a transport stream (TS) sync loss error occurred | Count | Sum | FlowARN |  |
| TSSyncLoss |  | Count | Sum | Region |  |
| TSSyncLoss |  | Count | Sum | Region, AvailabilityZone |  |
| TotalPackets | The total number of packets that were received | Count | Sum | Region |  |
| TotalPackets |  | Count | Sum | Region, AvailabilityZone |  |
| TotalPackets |  | Count | Sum | FlowARN | Applicable |
| TransportError | The number of times that a primary transport error occurred | Count | Sum | Region |  |
| TransportError |  | Count | Sum | Region, AvailabilityZone |  |
| TransportError |  | Count | Sum | FlowARN |  |